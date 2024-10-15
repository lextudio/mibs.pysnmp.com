# SNMP MIB module (ZHONE-DISMAN-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-DISMAN-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:27 2024
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

(zhoneIp,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp")


# MODULE-IDENTITY

zhonePingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19)
)
zhonePingMIB.setRevisions(
        ("2003-01-27 00:00",)
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

_ZhonePingNotifications_ObjectIdentity = ObjectIdentity
zhonePingNotifications = _ZhonePingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 0)
)
_ZhonePingObjects_ObjectIdentity = ObjectIdentity
zhonePingObjects = _ZhonePingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1)
)


class _ZhonePingMaxConcurrentRequests_Type(Unsigned32):
    """Custom type zhonePingMaxConcurrentRequests based on Unsigned32"""
    defaultValue = 10


_ZhonePingMaxConcurrentRequests_Object = MibScalar
zhonePingMaxConcurrentRequests = _ZhonePingMaxConcurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 1),
    _ZhonePingMaxConcurrentRequests_Type()
)
zhonePingMaxConcurrentRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhonePingMaxConcurrentRequests.setStatus("current")
if mibBuilder.loadTexts:
    zhonePingMaxConcurrentRequests.setUnits("requests")


class _ZhonePingCtlIndexNext_Type(Integer32):
    """Custom type zhonePingCtlIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhonePingCtlIndexNext_Type.__name__ = "Integer32"
_ZhonePingCtlIndexNext_Object = MibScalar
zhonePingCtlIndexNext = _ZhonePingCtlIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 2),
    _ZhonePingCtlIndexNext_Type()
)
zhonePingCtlIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePingCtlIndexNext.setStatus("current")
_ZhonePingCtlTable_Object = MibTable
zhonePingCtlTable = _ZhonePingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3)
)
if mibBuilder.loadTexts:
    zhonePingCtlTable.setStatus("current")
_ZhonePingCtlEntry_Object = MibTableRow
zhonePingCtlEntry = _ZhonePingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1)
)
zhonePingCtlEntry.setIndexNames(
    (0, "ZHONE-DISMAN-PING-MIB", "zhonePingCtlIndex"),
)
if mibBuilder.loadTexts:
    zhonePingCtlEntry.setStatus("current")


class _ZhonePingCtlIndex_Type(Integer32):
    """Custom type zhonePingCtlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhonePingCtlIndex_Type.__name__ = "Integer32"
_ZhonePingCtlIndex_Object = MibTableColumn
zhonePingCtlIndex = _ZhonePingCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 1),
    _ZhonePingCtlIndex_Type()
)
zhonePingCtlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePingCtlIndex.setStatus("current")


class _ZhonePingCtlTargetAddressType_Type(InetAddressType):
    """Custom type zhonePingCtlTargetAddressType based on InetAddressType"""


_ZhonePingCtlTargetAddressType_Object = MibTableColumn
zhonePingCtlTargetAddressType = _ZhonePingCtlTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 2),
    _ZhonePingCtlTargetAddressType_Type()
)
zhonePingCtlTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlTargetAddressType.setStatus("current")


class _ZhonePingCtlTargetAddress_Type(InetAddress):
    """Custom type zhonePingCtlTargetAddress based on InetAddress"""
    defaultHexValue = "0"


_ZhonePingCtlTargetAddress_Object = MibTableColumn
zhonePingCtlTargetAddress = _ZhonePingCtlTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 3),
    _ZhonePingCtlTargetAddress_Type()
)
zhonePingCtlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlTargetAddress.setStatus("current")


class _ZhonePingCtlDataSize_Type(Unsigned32):
    """Custom type zhonePingCtlDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65507),
    )


_ZhonePingCtlDataSize_Type.__name__ = "Unsigned32"
_ZhonePingCtlDataSize_Object = MibTableColumn
zhonePingCtlDataSize = _ZhonePingCtlDataSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 4),
    _ZhonePingCtlDataSize_Type()
)
zhonePingCtlDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlDataSize.setStatus("current")
if mibBuilder.loadTexts:
    zhonePingCtlDataSize.setUnits("octets")


class _ZhonePingCtlTimeOut_Type(Unsigned32):
    """Custom type zhonePingCtlTimeOut based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZhonePingCtlTimeOut_Type.__name__ = "Unsigned32"
_ZhonePingCtlTimeOut_Object = MibTableColumn
zhonePingCtlTimeOut = _ZhonePingCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 5),
    _ZhonePingCtlTimeOut_Type()
)
zhonePingCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    zhonePingCtlTimeOut.setUnits("seconds")


class _ZhonePingCtlProbeCount_Type(Unsigned32):
    """Custom type zhonePingCtlProbeCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ZhonePingCtlProbeCount_Type.__name__ = "Unsigned32"
_ZhonePingCtlProbeCount_Object = MibTableColumn
zhonePingCtlProbeCount = _ZhonePingCtlProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 6),
    _ZhonePingCtlProbeCount_Type()
)
zhonePingCtlProbeCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    zhonePingCtlProbeCount.setUnits("probes")


class _ZhonePingCtlAdminStatus_Type(Integer32):
    """Custom type zhonePingCtlAdminStatus based on Integer32"""
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


_ZhonePingCtlAdminStatus_Type.__name__ = "Integer32"
_ZhonePingCtlAdminStatus_Object = MibTableColumn
zhonePingCtlAdminStatus = _ZhonePingCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 7),
    _ZhonePingCtlAdminStatus_Type()
)
zhonePingCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlAdminStatus.setStatus("current")


class _ZhonePingCtlDataFill_Type(OctetString):
    """Custom type zhonePingCtlDataFill based on OctetString"""
    defaultHexValue = "0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ZhonePingCtlDataFill_Type.__name__ = "OctetString"
_ZhonePingCtlDataFill_Object = MibTableColumn
zhonePingCtlDataFill = _ZhonePingCtlDataFill_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 8),
    _ZhonePingCtlDataFill_Type()
)
zhonePingCtlDataFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlDataFill.setStatus("current")


class _ZhonePingCtlFrequency_Type(Unsigned32):
    """Custom type zhonePingCtlFrequency based on Unsigned32"""
    defaultValue = 0


_ZhonePingCtlFrequency_Object = MibTableColumn
zhonePingCtlFrequency = _ZhonePingCtlFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 9),
    _ZhonePingCtlFrequency_Type()
)
zhonePingCtlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlFrequency.setStatus("current")
if mibBuilder.loadTexts:
    zhonePingCtlFrequency.setUnits("seconds")


class _ZhonePingCtlMaxRows_Type(Unsigned32):
    """Custom type zhonePingCtlMaxRows based on Unsigned32"""
    defaultValue = 50


_ZhonePingCtlMaxRows_Object = MibTableColumn
zhonePingCtlMaxRows = _ZhonePingCtlMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 10),
    _ZhonePingCtlMaxRows_Type()
)
zhonePingCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlMaxRows.setStatus("current")
if mibBuilder.loadTexts:
    zhonePingCtlMaxRows.setUnits("rows")


class _ZhonePingCtlStorageType_Type(StorageType):
    """Custom type zhonePingCtlStorageType based on StorageType"""


_ZhonePingCtlStorageType_Object = MibTableColumn
zhonePingCtlStorageType = _ZhonePingCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 11),
    _ZhonePingCtlStorageType_Type()
)
zhonePingCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlStorageType.setStatus("current")


class _ZhonePingCtlTrapGeneration_Type(Bits):
    """Custom type zhonePingCtlTrapGeneration based on Bits"""
    namedValues = NamedValues(
        *(("probeFailure", 0),
          ("testCompletion", 2),
          ("testFailure", 1))
    )

_ZhonePingCtlTrapGeneration_Type.__name__ = "Bits"
_ZhonePingCtlTrapGeneration_Object = MibTableColumn
zhonePingCtlTrapGeneration = _ZhonePingCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 12),
    _ZhonePingCtlTrapGeneration_Type()
)
zhonePingCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlTrapGeneration.setStatus("current")


class _ZhonePingCtlTrapProbeFailureFilter_Type(Unsigned32):
    """Custom type zhonePingCtlTrapProbeFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZhonePingCtlTrapProbeFailureFilter_Type.__name__ = "Unsigned32"
_ZhonePingCtlTrapProbeFailureFilter_Object = MibTableColumn
zhonePingCtlTrapProbeFailureFilter = _ZhonePingCtlTrapProbeFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 13),
    _ZhonePingCtlTrapProbeFailureFilter_Type()
)
zhonePingCtlTrapProbeFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlTrapProbeFailureFilter.setStatus("current")


class _ZhonePingCtlTrapTestFailureFilter_Type(Unsigned32):
    """Custom type zhonePingCtlTrapTestFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZhonePingCtlTrapTestFailureFilter_Type.__name__ = "Unsigned32"
_ZhonePingCtlTrapTestFailureFilter_Object = MibTableColumn
zhonePingCtlTrapTestFailureFilter = _ZhonePingCtlTrapTestFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 14),
    _ZhonePingCtlTrapTestFailureFilter_Type()
)
zhonePingCtlTrapTestFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlTrapTestFailureFilter.setStatus("current")


class _ZhonePingCtlType_Type(ObjectIdentifier):
    """Custom type zhonePingCtlType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 3, 1)


_ZhonePingCtlType_Object = MibTableColumn
zhonePingCtlType = _ZhonePingCtlType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 15),
    _ZhonePingCtlType_Type()
)
zhonePingCtlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlType.setStatus("current")


class _ZhonePingCtlDescr_Type(SnmpAdminString):
    """Custom type zhonePingCtlDescr based on SnmpAdminString"""
    defaultHexValue = "0"


_ZhonePingCtlDescr_Object = MibTableColumn
zhonePingCtlDescr = _ZhonePingCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 16),
    _ZhonePingCtlDescr_Type()
)
zhonePingCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlDescr.setStatus("current")


class _ZhonePingCtlSourceAddressType_Type(InetAddressType):
    """Custom type zhonePingCtlSourceAddressType based on InetAddressType"""


_ZhonePingCtlSourceAddressType_Object = MibTableColumn
zhonePingCtlSourceAddressType = _ZhonePingCtlSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 17),
    _ZhonePingCtlSourceAddressType_Type()
)
zhonePingCtlSourceAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlSourceAddressType.setStatus("current")


class _ZhonePingCtlSourceAddress_Type(InetAddress):
    """Custom type zhonePingCtlSourceAddress based on InetAddress"""
    defaultHexValue = "0"


_ZhonePingCtlSourceAddress_Object = MibTableColumn
zhonePingCtlSourceAddress = _ZhonePingCtlSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 18),
    _ZhonePingCtlSourceAddress_Type()
)
zhonePingCtlSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlSourceAddress.setStatus("current")


class _ZhonePingCtlIfIndex_Type(InterfaceIndexOrZero):
    """Custom type zhonePingCtlIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_ZhonePingCtlIfIndex_Object = MibTableColumn
zhonePingCtlIfIndex = _ZhonePingCtlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 19),
    _ZhonePingCtlIfIndex_Type()
)
zhonePingCtlIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlIfIndex.setStatus("current")


class _ZhonePingCtlByPassRouteTable_Type(TruthValue):
    """Custom type zhonePingCtlByPassRouteTable based on TruthValue"""


_ZhonePingCtlByPassRouteTable_Object = MibTableColumn
zhonePingCtlByPassRouteTable = _ZhonePingCtlByPassRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 20),
    _ZhonePingCtlByPassRouteTable_Type()
)
zhonePingCtlByPassRouteTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlByPassRouteTable.setStatus("current")


class _ZhonePingCtlDSField_Type(Unsigned32):
    """Custom type zhonePingCtlDSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhonePingCtlDSField_Type.__name__ = "Unsigned32"
_ZhonePingCtlDSField_Object = MibTableColumn
zhonePingCtlDSField = _ZhonePingCtlDSField_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 21),
    _ZhonePingCtlDSField_Type()
)
zhonePingCtlDSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlDSField.setStatus("current")
_ZhonePingCtlRowStatus_Type = RowStatus
_ZhonePingCtlRowStatus_Object = MibTableColumn
zhonePingCtlRowStatus = _ZhonePingCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 3, 1, 22),
    _ZhonePingCtlRowStatus_Type()
)
zhonePingCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePingCtlRowStatus.setStatus("current")
_ZhonePingResultsTable_Object = MibTable
zhonePingResultsTable = _ZhonePingResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 4)
)
if mibBuilder.loadTexts:
    zhonePingResultsTable.setStatus("current")
_ZhonePingResultsEntry_Object = MibTableRow
zhonePingResultsEntry = _ZhonePingResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 4, 1)
)
zhonePingResultsEntry.setIndexNames(
    (0, "ZHONE-DISMAN-PING-MIB", "zhonePingCtlIndex"),
)
if mibBuilder.loadTexts:
    zhonePingResultsEntry.setStatus("current")


class _ZhonePingResultsOperStatus_Type(Integer32):
    """Custom type zhonePingResultsOperStatus based on Integer32"""
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


_ZhonePingResultsOperStatus_Type.__name__ = "Integer32"
_ZhonePingResultsOperStatus_Object = MibTableColumn
zhonePingResultsOperStatus = _ZhonePingResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 4, 1, 1),
    _ZhonePingResultsOperStatus_Type()
)
zhonePingResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePingResultsOperStatus.setStatus("current")


class _ZhonePingResultsIpTargetAddressType_Type(InetAddressType):
    """Custom type zhonePingResultsIpTargetAddressType based on InetAddressType"""


_ZhonePingResultsIpTargetAddressType_Object = MibTableColumn
zhonePingResultsIpTargetAddressType = _ZhonePingResultsIpTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 4, 1, 2),
    _ZhonePingResultsIpTargetAddressType_Type()
)
zhonePingResultsIpTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePingResultsIpTargetAddressType.setStatus("current")


class _ZhonePingResultsIpTargetAddress_Type(InetAddress):
    """Custom type zhonePingResultsIpTargetAddress based on InetAddress"""
    defaultHexValue = "0"


_ZhonePingResultsIpTargetAddress_Object = MibTableColumn
zhonePingResultsIpTargetAddress = _ZhonePingResultsIpTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 4, 1, 3),
    _ZhonePingResultsIpTargetAddress_Type()
)
zhonePingResultsIpTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePingResultsIpTargetAddress.setStatus("current")
_ZhonePingResultsMinRtt_Type = Unsigned32
_ZhonePingResultsMinRtt_Object = MibTableColumn
zhonePingResultsMinRtt = _ZhonePingResultsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 4, 1, 4),
    _ZhonePingResultsMinRtt_Type()
)
zhonePingResultsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePingResultsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    zhonePingResultsMinRtt.setUnits("milliseconds")
_ZhonePingResultsMaxRtt_Type = Unsigned32
_ZhonePingResultsMaxRtt_Object = MibTableColumn
zhonePingResultsMaxRtt = _ZhonePingResultsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 4, 1, 5),
    _ZhonePingResultsMaxRtt_Type()
)
zhonePingResultsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePingResultsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    zhonePingResultsMaxRtt.setUnits("milliseconds")
_ZhonePingResultsAverageRtt_Type = Unsigned32
_ZhonePingResultsAverageRtt_Object = MibTableColumn
zhonePingResultsAverageRtt = _ZhonePingResultsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 4, 1, 6),
    _ZhonePingResultsAverageRtt_Type()
)
zhonePingResultsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePingResultsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    zhonePingResultsAverageRtt.setUnits("milliseconds")
_ZhonePingResultsProbeResponses_Type = Unsigned32
_ZhonePingResultsProbeResponses_Object = MibTableColumn
zhonePingResultsProbeResponses = _ZhonePingResultsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 4, 1, 7),
    _ZhonePingResultsProbeResponses_Type()
)
zhonePingResultsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePingResultsProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    zhonePingResultsProbeResponses.setUnits("responses")
_ZhonePingResultsSentProbes_Type = Unsigned32
_ZhonePingResultsSentProbes_Object = MibTableColumn
zhonePingResultsSentProbes = _ZhonePingResultsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 4, 1, 8),
    _ZhonePingResultsSentProbes_Type()
)
zhonePingResultsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePingResultsSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    zhonePingResultsSentProbes.setUnits("probes")
_ZhonePingResultsRttSumOfSquares_Type = Unsigned32
_ZhonePingResultsRttSumOfSquares_Object = MibTableColumn
zhonePingResultsRttSumOfSquares = _ZhonePingResultsRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 4, 1, 9),
    _ZhonePingResultsRttSumOfSquares_Type()
)
zhonePingResultsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePingResultsRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    zhonePingResultsRttSumOfSquares.setUnits("milliseconds")
_ZhonePingResultsLastGoodProbe_Type = DateAndTime
_ZhonePingResultsLastGoodProbe_Object = MibTableColumn
zhonePingResultsLastGoodProbe = _ZhonePingResultsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 1, 4, 1, 10),
    _ZhonePingResultsLastGoodProbe_Type()
)
zhonePingResultsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePingResultsLastGoodProbe.setStatus("current")
_ZhonePingConformance_ObjectIdentity = ObjectIdentity
zhonePingConformance = _ZhonePingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 2)
)
_ZhonePingGroups_ObjectIdentity = ObjectIdentity
zhonePingGroups = _ZhonePingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 2, 2)
)
_ZhonePingImplementationTypeDomains_ObjectIdentity = ObjectIdentity
zhonePingImplementationTypeDomains = _ZhonePingImplementationTypeDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 3)
)
_ZhonePingIcmpEcho_ObjectIdentity = ObjectIdentity
zhonePingIcmpEcho = _ZhonePingIcmpEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 3, 1)
)
if mibBuilder.loadTexts:
    zhonePingIcmpEcho.setStatus("current")
_ZhonePingUdpEcho_ObjectIdentity = ObjectIdentity
zhonePingUdpEcho = _ZhonePingUdpEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 3, 2)
)
if mibBuilder.loadTexts:
    zhonePingUdpEcho.setStatus("current")
_ZhonePingSnmpQuery_ObjectIdentity = ObjectIdentity
zhonePingSnmpQuery = _ZhonePingSnmpQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 3, 3)
)
if mibBuilder.loadTexts:
    zhonePingSnmpQuery.setStatus("current")
_ZhonePingTcpConnectionAttempt_ObjectIdentity = ObjectIdentity
zhonePingTcpConnectionAttempt = _ZhonePingTcpConnectionAttempt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 3, 4)
)
if mibBuilder.loadTexts:
    zhonePingTcpConnectionAttempt.setStatus("current")

# Managed Objects groups

zhonePingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 2, 2, 1)
)
zhonePingGroup.setObjects(
      *(("ZHONE-DISMAN-PING-MIB", "zhonePingMaxConcurrentRequests"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlTargetAddressType"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlTargetAddress"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlDataSize"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlTimeOut"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlProbeCount"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlAdminStatus"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlDataFill"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlFrequency"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlMaxRows"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlStorageType"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlTrapGeneration"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlTrapProbeFailureFilter"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlTrapTestFailureFilter"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlType"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlDescr"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlByPassRouteTable"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlSourceAddressType"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlSourceAddress"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlIfIndex"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlDSField"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingCtlRowStatus"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsOperStatus"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsIpTargetAddressType"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsIpTargetAddress"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsMinRtt"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsMaxRtt"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsAverageRtt"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsProbeResponses"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsSentProbes"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsRttSumOfSquares"))
)
if mibBuilder.loadTexts:
    zhonePingGroup.setStatus("current")

zhonePingTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 2, 2, 2)
)
zhonePingTimeStampGroup.setObjects(
    ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsLastGoodProbe")
)
if mibBuilder.loadTexts:
    zhonePingTimeStampGroup.setStatus("current")


# Notification objects

zhonePingTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 0, 1)
)
zhonePingTestCompleted.setObjects(
      *(("ZHONE-DISMAN-PING-MIB", "zhonePingResultsIpTargetAddress"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsMinRtt"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsMaxRtt"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsAverageRtt"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsProbeResponses"),
        ("ZHONE-DISMAN-PING-MIB", "zhonePingResultsSentProbes"))
)
if mibBuilder.loadTexts:
    zhonePingTestCompleted.setStatus(
        "current"
    )


# Notifications groups

zhonePingNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 19, 2, 2, 3)
)
zhonePingNotificationsGroup.setObjects(
    ("ZHONE-DISMAN-PING-MIB", "zhonePingTestCompleted")
)
if mibBuilder.loadTexts:
    zhonePingNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-DISMAN-PING-MIB",
    **{"OperationResponseStatus": OperationResponseStatus,
       "zhonePingMIB": zhonePingMIB,
       "zhonePingNotifications": zhonePingNotifications,
       "zhonePingTestCompleted": zhonePingTestCompleted,
       "zhonePingObjects": zhonePingObjects,
       "zhonePingMaxConcurrentRequests": zhonePingMaxConcurrentRequests,
       "zhonePingCtlIndexNext": zhonePingCtlIndexNext,
       "zhonePingCtlTable": zhonePingCtlTable,
       "zhonePingCtlEntry": zhonePingCtlEntry,
       "zhonePingCtlIndex": zhonePingCtlIndex,
       "zhonePingCtlTargetAddressType": zhonePingCtlTargetAddressType,
       "zhonePingCtlTargetAddress": zhonePingCtlTargetAddress,
       "zhonePingCtlDataSize": zhonePingCtlDataSize,
       "zhonePingCtlTimeOut": zhonePingCtlTimeOut,
       "zhonePingCtlProbeCount": zhonePingCtlProbeCount,
       "zhonePingCtlAdminStatus": zhonePingCtlAdminStatus,
       "zhonePingCtlDataFill": zhonePingCtlDataFill,
       "zhonePingCtlFrequency": zhonePingCtlFrequency,
       "zhonePingCtlMaxRows": zhonePingCtlMaxRows,
       "zhonePingCtlStorageType": zhonePingCtlStorageType,
       "zhonePingCtlTrapGeneration": zhonePingCtlTrapGeneration,
       "zhonePingCtlTrapProbeFailureFilter": zhonePingCtlTrapProbeFailureFilter,
       "zhonePingCtlTrapTestFailureFilter": zhonePingCtlTrapTestFailureFilter,
       "zhonePingCtlType": zhonePingCtlType,
       "zhonePingCtlDescr": zhonePingCtlDescr,
       "zhonePingCtlSourceAddressType": zhonePingCtlSourceAddressType,
       "zhonePingCtlSourceAddress": zhonePingCtlSourceAddress,
       "zhonePingCtlIfIndex": zhonePingCtlIfIndex,
       "zhonePingCtlByPassRouteTable": zhonePingCtlByPassRouteTable,
       "zhonePingCtlDSField": zhonePingCtlDSField,
       "zhonePingCtlRowStatus": zhonePingCtlRowStatus,
       "zhonePingResultsTable": zhonePingResultsTable,
       "zhonePingResultsEntry": zhonePingResultsEntry,
       "zhonePingResultsOperStatus": zhonePingResultsOperStatus,
       "zhonePingResultsIpTargetAddressType": zhonePingResultsIpTargetAddressType,
       "zhonePingResultsIpTargetAddress": zhonePingResultsIpTargetAddress,
       "zhonePingResultsMinRtt": zhonePingResultsMinRtt,
       "zhonePingResultsMaxRtt": zhonePingResultsMaxRtt,
       "zhonePingResultsAverageRtt": zhonePingResultsAverageRtt,
       "zhonePingResultsProbeResponses": zhonePingResultsProbeResponses,
       "zhonePingResultsSentProbes": zhonePingResultsSentProbes,
       "zhonePingResultsRttSumOfSquares": zhonePingResultsRttSumOfSquares,
       "zhonePingResultsLastGoodProbe": zhonePingResultsLastGoodProbe,
       "zhonePingConformance": zhonePingConformance,
       "zhonePingGroups": zhonePingGroups,
       "zhonePingGroup": zhonePingGroup,
       "zhonePingTimeStampGroup": zhonePingTimeStampGroup,
       "zhonePingNotificationsGroup": zhonePingNotificationsGroup,
       "zhonePingImplementationTypeDomains": zhonePingImplementationTypeDomains,
       "zhonePingIcmpEcho": zhonePingIcmpEcho,
       "zhonePingUdpEcho": zhonePingUdpEcho,
       "zhonePingSnmpQuery": zhonePingSnmpQuery,
       "zhonePingTcpConnectionAttempt": zhonePingTcpConnectionAttempt}
)
