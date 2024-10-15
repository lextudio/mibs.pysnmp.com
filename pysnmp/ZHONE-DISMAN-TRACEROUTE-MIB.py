# SNMP MIB module (ZHONE-DISMAN-TRACEROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-DISMAN-TRACEROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:28 2024
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

(OperationResponseStatus,) = mibBuilder.importSymbols(
    "ZHONE-DISMAN-PING-MIB",
    "OperationResponseStatus")

(zhoneIp,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp")


# MODULE-IDENTITY

zhoneTraceRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20)
)
zhoneTraceRouteMIB.setRevisions(
        ("2000-09-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneTraceRouteNotifications_ObjectIdentity = ObjectIdentity
zhoneTraceRouteNotifications = _ZhoneTraceRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 0)
)
_ZhoneTraceRouteObjects_ObjectIdentity = ObjectIdentity
zhoneTraceRouteObjects = _ZhoneTraceRouteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1)
)


class _ZhoneTraceRouteMaxConcurrentRequests_Type(Unsigned32):
    """Custom type zhoneTraceRouteMaxConcurrentRequests based on Unsigned32"""
    defaultValue = 10


_ZhoneTraceRouteMaxConcurrentRequests_Object = MibScalar
zhoneTraceRouteMaxConcurrentRequests = _ZhoneTraceRouteMaxConcurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 1),
    _ZhoneTraceRouteMaxConcurrentRequests_Type()
)
zhoneTraceRouteMaxConcurrentRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneTraceRouteMaxConcurrentRequests.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteMaxConcurrentRequests.setUnits("requests")


class _ZhoneTraceRouteCtlIndexNext_Type(Integer32):
    """Custom type zhoneTraceRouteCtlIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneTraceRouteCtlIndexNext_Type.__name__ = "Integer32"
_ZhoneTraceRouteCtlIndexNext_Object = MibScalar
zhoneTraceRouteCtlIndexNext = _ZhoneTraceRouteCtlIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 2),
    _ZhoneTraceRouteCtlIndexNext_Type()
)
zhoneTraceRouteCtlIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlIndexNext.setStatus("current")
_ZhoneTraceRouteCtlTable_Object = MibTable
zhoneTraceRouteCtlTable = _ZhoneTraceRouteCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3)
)
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlTable.setStatus("current")
_ZhoneTraceRouteCtlEntry_Object = MibTableRow
zhoneTraceRouteCtlEntry = _ZhoneTraceRouteCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1)
)
zhoneTraceRouteCtlEntry.setIndexNames(
    (0, "ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlIndex"),
)
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlEntry.setStatus("current")


class _ZhoneTraceRouteCtlIndex_Type(Integer32):
    """Custom type zhoneTraceRouteCtlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneTraceRouteCtlIndex_Type.__name__ = "Integer32"
_ZhoneTraceRouteCtlIndex_Object = MibTableColumn
zhoneTraceRouteCtlIndex = _ZhoneTraceRouteCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 1),
    _ZhoneTraceRouteCtlIndex_Type()
)
zhoneTraceRouteCtlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlIndex.setStatus("current")


class _ZhoneTraceRouteCtlTargetAddressType_Type(InetAddressType):
    """Custom type zhoneTraceRouteCtlTargetAddressType based on InetAddressType"""


_ZhoneTraceRouteCtlTargetAddressType_Object = MibTableColumn
zhoneTraceRouteCtlTargetAddressType = _ZhoneTraceRouteCtlTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 2),
    _ZhoneTraceRouteCtlTargetAddressType_Type()
)
zhoneTraceRouteCtlTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlTargetAddressType.setStatus("current")
_ZhoneTraceRouteCtlTargetAddress_Type = InetAddress
_ZhoneTraceRouteCtlTargetAddress_Object = MibTableColumn
zhoneTraceRouteCtlTargetAddress = _ZhoneTraceRouteCtlTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 3),
    _ZhoneTraceRouteCtlTargetAddress_Type()
)
zhoneTraceRouteCtlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlTargetAddress.setStatus("current")


class _ZhoneTraceRouteCtlByPassRouteTable_Type(TruthValue):
    """Custom type zhoneTraceRouteCtlByPassRouteTable based on TruthValue"""


_ZhoneTraceRouteCtlByPassRouteTable_Object = MibTableColumn
zhoneTraceRouteCtlByPassRouteTable = _ZhoneTraceRouteCtlByPassRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 4),
    _ZhoneTraceRouteCtlByPassRouteTable_Type()
)
zhoneTraceRouteCtlByPassRouteTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlByPassRouteTable.setStatus("current")


class _ZhoneTraceRouteCtlDataSize_Type(Unsigned32):
    """Custom type zhoneTraceRouteCtlDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65507),
    )


_ZhoneTraceRouteCtlDataSize_Type.__name__ = "Unsigned32"
_ZhoneTraceRouteCtlDataSize_Object = MibTableColumn
zhoneTraceRouteCtlDataSize = _ZhoneTraceRouteCtlDataSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 5),
    _ZhoneTraceRouteCtlDataSize_Type()
)
zhoneTraceRouteCtlDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlDataSize.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlDataSize.setUnits("octets")


class _ZhoneTraceRouteCtlTimeOut_Type(Unsigned32):
    """Custom type zhoneTraceRouteCtlTimeOut based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZhoneTraceRouteCtlTimeOut_Type.__name__ = "Unsigned32"
_ZhoneTraceRouteCtlTimeOut_Object = MibTableColumn
zhoneTraceRouteCtlTimeOut = _ZhoneTraceRouteCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 6),
    _ZhoneTraceRouteCtlTimeOut_Type()
)
zhoneTraceRouteCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlTimeOut.setUnits("seconds")


class _ZhoneTraceRouteCtlProbesPerHop_Type(Unsigned32):
    """Custom type zhoneTraceRouteCtlProbesPerHop based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZhoneTraceRouteCtlProbesPerHop_Type.__name__ = "Unsigned32"
_ZhoneTraceRouteCtlProbesPerHop_Object = MibTableColumn
zhoneTraceRouteCtlProbesPerHop = _ZhoneTraceRouteCtlProbesPerHop_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 7),
    _ZhoneTraceRouteCtlProbesPerHop_Type()
)
zhoneTraceRouteCtlProbesPerHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlProbesPerHop.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlProbesPerHop.setUnits("probes")


class _ZhoneTraceRouteCtlPort_Type(Unsigned32):
    """Custom type zhoneTraceRouteCtlPort based on Unsigned32"""
    defaultValue = 33434

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZhoneTraceRouteCtlPort_Type.__name__ = "Unsigned32"
_ZhoneTraceRouteCtlPort_Object = MibTableColumn
zhoneTraceRouteCtlPort = _ZhoneTraceRouteCtlPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 8),
    _ZhoneTraceRouteCtlPort_Type()
)
zhoneTraceRouteCtlPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlPort.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlPort.setUnits("UDP Port")


class _ZhoneTraceRouteCtlMaxTtl_Type(Unsigned32):
    """Custom type zhoneTraceRouteCtlMaxTtl based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZhoneTraceRouteCtlMaxTtl_Type.__name__ = "Unsigned32"
_ZhoneTraceRouteCtlMaxTtl_Object = MibTableColumn
zhoneTraceRouteCtlMaxTtl = _ZhoneTraceRouteCtlMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 9),
    _ZhoneTraceRouteCtlMaxTtl_Type()
)
zhoneTraceRouteCtlMaxTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlMaxTtl.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlMaxTtl.setUnits("time-to-live value")


class _ZhoneTraceRouteCtlDSField_Type(Unsigned32):
    """Custom type zhoneTraceRouteCtlDSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneTraceRouteCtlDSField_Type.__name__ = "Unsigned32"
_ZhoneTraceRouteCtlDSField_Object = MibTableColumn
zhoneTraceRouteCtlDSField = _ZhoneTraceRouteCtlDSField_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 10),
    _ZhoneTraceRouteCtlDSField_Type()
)
zhoneTraceRouteCtlDSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlDSField.setStatus("current")


class _ZhoneTraceRouteCtlSourceAddressType_Type(InetAddressType):
    """Custom type zhoneTraceRouteCtlSourceAddressType based on InetAddressType"""


_ZhoneTraceRouteCtlSourceAddressType_Object = MibTableColumn
zhoneTraceRouteCtlSourceAddressType = _ZhoneTraceRouteCtlSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 11),
    _ZhoneTraceRouteCtlSourceAddressType_Type()
)
zhoneTraceRouteCtlSourceAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlSourceAddressType.setStatus("current")


class _ZhoneTraceRouteCtlSourceAddress_Type(InetAddress):
    """Custom type zhoneTraceRouteCtlSourceAddress based on InetAddress"""
    defaultHexValue = "0"


_ZhoneTraceRouteCtlSourceAddress_Object = MibTableColumn
zhoneTraceRouteCtlSourceAddress = _ZhoneTraceRouteCtlSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 12),
    _ZhoneTraceRouteCtlSourceAddress_Type()
)
zhoneTraceRouteCtlSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlSourceAddress.setStatus("current")


class _ZhoneTraceRouteCtlIfIndex_Type(InterfaceIndexOrZero):
    """Custom type zhoneTraceRouteCtlIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_ZhoneTraceRouteCtlIfIndex_Object = MibTableColumn
zhoneTraceRouteCtlIfIndex = _ZhoneTraceRouteCtlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 13),
    _ZhoneTraceRouteCtlIfIndex_Type()
)
zhoneTraceRouteCtlIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlIfIndex.setStatus("current")


class _ZhoneTraceRouteCtlMiscOptions_Type(SnmpAdminString):
    """Custom type zhoneTraceRouteCtlMiscOptions based on SnmpAdminString"""
    defaultHexValue = "0"


_ZhoneTraceRouteCtlMiscOptions_Object = MibTableColumn
zhoneTraceRouteCtlMiscOptions = _ZhoneTraceRouteCtlMiscOptions_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 14),
    _ZhoneTraceRouteCtlMiscOptions_Type()
)
zhoneTraceRouteCtlMiscOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlMiscOptions.setStatus("current")


class _ZhoneTraceRouteCtlMaxFailures_Type(Unsigned32):
    """Custom type zhoneTraceRouteCtlMaxFailures based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneTraceRouteCtlMaxFailures_Type.__name__ = "Unsigned32"
_ZhoneTraceRouteCtlMaxFailures_Object = MibTableColumn
zhoneTraceRouteCtlMaxFailures = _ZhoneTraceRouteCtlMaxFailures_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 15),
    _ZhoneTraceRouteCtlMaxFailures_Type()
)
zhoneTraceRouteCtlMaxFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlMaxFailures.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlMaxFailures.setUnits("timeouts")


class _ZhoneTraceRouteCtlDontFragment_Type(TruthValue):
    """Custom type zhoneTraceRouteCtlDontFragment based on TruthValue"""


_ZhoneTraceRouteCtlDontFragment_Object = MibTableColumn
zhoneTraceRouteCtlDontFragment = _ZhoneTraceRouteCtlDontFragment_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 16),
    _ZhoneTraceRouteCtlDontFragment_Type()
)
zhoneTraceRouteCtlDontFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlDontFragment.setStatus("current")


class _ZhoneTraceRouteCtlInitialTtl_Type(Unsigned32):
    """Custom type zhoneTraceRouteCtlInitialTtl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneTraceRouteCtlInitialTtl_Type.__name__ = "Unsigned32"
_ZhoneTraceRouteCtlInitialTtl_Object = MibTableColumn
zhoneTraceRouteCtlInitialTtl = _ZhoneTraceRouteCtlInitialTtl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 17),
    _ZhoneTraceRouteCtlInitialTtl_Type()
)
zhoneTraceRouteCtlInitialTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlInitialTtl.setStatus("current")


class _ZhoneTraceRouteCtlFrequency_Type(Unsigned32):
    """Custom type zhoneTraceRouteCtlFrequency based on Unsigned32"""
    defaultValue = 0


_ZhoneTraceRouteCtlFrequency_Object = MibTableColumn
zhoneTraceRouteCtlFrequency = _ZhoneTraceRouteCtlFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 18),
    _ZhoneTraceRouteCtlFrequency_Type()
)
zhoneTraceRouteCtlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlFrequency.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlFrequency.setUnits("seconds")


class _ZhoneTraceRouteCtlStorageType_Type(StorageType):
    """Custom type zhoneTraceRouteCtlStorageType based on StorageType"""


_ZhoneTraceRouteCtlStorageType_Object = MibTableColumn
zhoneTraceRouteCtlStorageType = _ZhoneTraceRouteCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 19),
    _ZhoneTraceRouteCtlStorageType_Type()
)
zhoneTraceRouteCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlStorageType.setStatus("current")


class _ZhoneTraceRouteCtlAdminStatus_Type(Integer32):
    """Custom type zhoneTraceRouteCtlAdminStatus based on Integer32"""
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


_ZhoneTraceRouteCtlAdminStatus_Type.__name__ = "Integer32"
_ZhoneTraceRouteCtlAdminStatus_Object = MibTableColumn
zhoneTraceRouteCtlAdminStatus = _ZhoneTraceRouteCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 20),
    _ZhoneTraceRouteCtlAdminStatus_Type()
)
zhoneTraceRouteCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlAdminStatus.setStatus("current")


class _ZhoneTraceRouteCtlDescr_Type(SnmpAdminString):
    """Custom type zhoneTraceRouteCtlDescr based on SnmpAdminString"""
    defaultHexValue = "0"


_ZhoneTraceRouteCtlDescr_Object = MibTableColumn
zhoneTraceRouteCtlDescr = _ZhoneTraceRouteCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 21),
    _ZhoneTraceRouteCtlDescr_Type()
)
zhoneTraceRouteCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlDescr.setStatus("current")


class _ZhoneTraceRouteCtlMaxRows_Type(Unsigned32):
    """Custom type zhoneTraceRouteCtlMaxRows based on Unsigned32"""
    defaultValue = 50


_ZhoneTraceRouteCtlMaxRows_Object = MibTableColumn
zhoneTraceRouteCtlMaxRows = _ZhoneTraceRouteCtlMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 22),
    _ZhoneTraceRouteCtlMaxRows_Type()
)
zhoneTraceRouteCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlMaxRows.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlMaxRows.setUnits("rows")


class _ZhoneTraceRouteCtlTrapGeneration_Type(Bits):
    """Custom type zhoneTraceRouteCtlTrapGeneration based on Bits"""
    namedValues = NamedValues(
        *(("pathChange", 0),
          ("testCompletion", 2),
          ("testFailure", 1))
    )

_ZhoneTraceRouteCtlTrapGeneration_Type.__name__ = "Bits"
_ZhoneTraceRouteCtlTrapGeneration_Object = MibTableColumn
zhoneTraceRouteCtlTrapGeneration = _ZhoneTraceRouteCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 23),
    _ZhoneTraceRouteCtlTrapGeneration_Type()
)
zhoneTraceRouteCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlTrapGeneration.setStatus("current")


class _ZhoneTraceRouteCtlCreateHopsEntries_Type(TruthValue):
    """Custom type zhoneTraceRouteCtlCreateHopsEntries based on TruthValue"""


_ZhoneTraceRouteCtlCreateHopsEntries_Object = MibTableColumn
zhoneTraceRouteCtlCreateHopsEntries = _ZhoneTraceRouteCtlCreateHopsEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 24),
    _ZhoneTraceRouteCtlCreateHopsEntries_Type()
)
zhoneTraceRouteCtlCreateHopsEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlCreateHopsEntries.setStatus("current")


class _ZhoneTraceRouteCtlType_Type(ObjectIdentifier):
    """Custom type zhoneTraceRouteCtlType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 3, 1)


_ZhoneTraceRouteCtlType_Object = MibTableColumn
zhoneTraceRouteCtlType = _ZhoneTraceRouteCtlType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 25),
    _ZhoneTraceRouteCtlType_Type()
)
zhoneTraceRouteCtlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlType.setStatus("current")
_ZhoneTraceRouteCtlRowStatus_Type = RowStatus
_ZhoneTraceRouteCtlRowStatus_Object = MibTableColumn
zhoneTraceRouteCtlRowStatus = _ZhoneTraceRouteCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 3, 1, 26),
    _ZhoneTraceRouteCtlRowStatus_Type()
)
zhoneTraceRouteCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneTraceRouteCtlRowStatus.setStatus("current")
_ZhoneTraceRouteResultsTable_Object = MibTable
zhoneTraceRouteResultsTable = _ZhoneTraceRouteResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 4)
)
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsTable.setStatus("current")
_ZhoneTraceRouteResultsEntry_Object = MibTableRow
zhoneTraceRouteResultsEntry = _ZhoneTraceRouteResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 4, 1)
)
zhoneTraceRouteResultsEntry.setIndexNames(
    (0, "ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlIndex"),
)
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsEntry.setStatus("current")


class _ZhoneTraceRouteResultsOperStatus_Type(Integer32):
    """Custom type zhoneTraceRouteResultsOperStatus based on Integer32"""
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


_ZhoneTraceRouteResultsOperStatus_Type.__name__ = "Integer32"
_ZhoneTraceRouteResultsOperStatus_Object = MibTableColumn
zhoneTraceRouteResultsOperStatus = _ZhoneTraceRouteResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 4, 1, 1),
    _ZhoneTraceRouteResultsOperStatus_Type()
)
zhoneTraceRouteResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsOperStatus.setStatus("current")
_ZhoneTraceRouteResultsCurHopCount_Type = Gauge32
_ZhoneTraceRouteResultsCurHopCount_Object = MibTableColumn
zhoneTraceRouteResultsCurHopCount = _ZhoneTraceRouteResultsCurHopCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 4, 1, 2),
    _ZhoneTraceRouteResultsCurHopCount_Type()
)
zhoneTraceRouteResultsCurHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsCurHopCount.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsCurHopCount.setUnits("hops")
_ZhoneTraceRouteResultsCurProbeCount_Type = Gauge32
_ZhoneTraceRouteResultsCurProbeCount_Object = MibTableColumn
zhoneTraceRouteResultsCurProbeCount = _ZhoneTraceRouteResultsCurProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 4, 1, 3),
    _ZhoneTraceRouteResultsCurProbeCount_Type()
)
zhoneTraceRouteResultsCurProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsCurProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsCurProbeCount.setUnits("probes")
_ZhoneTraceRouteResultsIpTgtAddrType_Type = InetAddressType
_ZhoneTraceRouteResultsIpTgtAddrType_Object = MibTableColumn
zhoneTraceRouteResultsIpTgtAddrType = _ZhoneTraceRouteResultsIpTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 4, 1, 4),
    _ZhoneTraceRouteResultsIpTgtAddrType_Type()
)
zhoneTraceRouteResultsIpTgtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsIpTgtAddrType.setStatus("current")
_ZhoneTraceRouteResultsIpTgtAddr_Type = InetAddress
_ZhoneTraceRouteResultsIpTgtAddr_Object = MibTableColumn
zhoneTraceRouteResultsIpTgtAddr = _ZhoneTraceRouteResultsIpTgtAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 4, 1, 5),
    _ZhoneTraceRouteResultsIpTgtAddr_Type()
)
zhoneTraceRouteResultsIpTgtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsIpTgtAddr.setStatus("current")
_ZhoneTraceRouteResultsTestAttempts_Type = Unsigned32
_ZhoneTraceRouteResultsTestAttempts_Object = MibTableColumn
zhoneTraceRouteResultsTestAttempts = _ZhoneTraceRouteResultsTestAttempts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 4, 1, 6),
    _ZhoneTraceRouteResultsTestAttempts_Type()
)
zhoneTraceRouteResultsTestAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsTestAttempts.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsTestAttempts.setUnits("tests")
_ZhoneTraceRouteResultsTestSuccesses_Type = Unsigned32
_ZhoneTraceRouteResultsTestSuccesses_Object = MibTableColumn
zhoneTraceRouteResultsTestSuccesses = _ZhoneTraceRouteResultsTestSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 4, 1, 7),
    _ZhoneTraceRouteResultsTestSuccesses_Type()
)
zhoneTraceRouteResultsTestSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsTestSuccesses.setStatus("current")
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsTestSuccesses.setUnits("tests")
_ZhoneTraceRouteResultsLastGoodPath_Type = DateAndTime
_ZhoneTraceRouteResultsLastGoodPath_Object = MibTableColumn
zhoneTraceRouteResultsLastGoodPath = _ZhoneTraceRouteResultsLastGoodPath_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 4, 1, 8),
    _ZhoneTraceRouteResultsLastGoodPath_Type()
)
zhoneTraceRouteResultsLastGoodPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteResultsLastGoodPath.setStatus("current")
_ZhoneTraceRouteHopsTable_Object = MibTable
zhoneTraceRouteHopsTable = _ZhoneTraceRouteHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 5)
)
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsTable.setStatus("current")
_ZhoneTraceRouteHopsEntry_Object = MibTableRow
zhoneTraceRouteHopsEntry = _ZhoneTraceRouteHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 5, 1)
)
zhoneTraceRouteHopsEntry.setIndexNames(
    (0, "ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlIndex"),
    (0, "ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteHopsHopIndex"),
)
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsEntry.setStatus("current")
_ZhoneTraceRouteHopsHopIndex_Type = Unsigned32
_ZhoneTraceRouteHopsHopIndex_Object = MibTableColumn
zhoneTraceRouteHopsHopIndex = _ZhoneTraceRouteHopsHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 5, 1, 1),
    _ZhoneTraceRouteHopsHopIndex_Type()
)
zhoneTraceRouteHopsHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsHopIndex.setStatus("current")
_ZhoneTraceRouteHopsIpTgtAddressType_Type = InetAddressType
_ZhoneTraceRouteHopsIpTgtAddressType_Object = MibTableColumn
zhoneTraceRouteHopsIpTgtAddressType = _ZhoneTraceRouteHopsIpTgtAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 5, 1, 2),
    _ZhoneTraceRouteHopsIpTgtAddressType_Type()
)
zhoneTraceRouteHopsIpTgtAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsIpTgtAddressType.setStatus("current")
_ZhoneTraceRouteHopsIpTgtAddress_Type = InetAddress
_ZhoneTraceRouteHopsIpTgtAddress_Object = MibTableColumn
zhoneTraceRouteHopsIpTgtAddress = _ZhoneTraceRouteHopsIpTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 5, 1, 3),
    _ZhoneTraceRouteHopsIpTgtAddress_Type()
)
zhoneTraceRouteHopsIpTgtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsIpTgtAddress.setStatus("current")
_ZhoneTraceRouteHopsMinRtt_Type = Unsigned32
_ZhoneTraceRouteHopsMinRtt_Object = MibTableColumn
zhoneTraceRouteHopsMinRtt = _ZhoneTraceRouteHopsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 5, 1, 4),
    _ZhoneTraceRouteHopsMinRtt_Type()
)
zhoneTraceRouteHopsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsMinRtt.setStatus("current")
_ZhoneTraceRouteHopsMaxRtt_Type = Unsigned32
_ZhoneTraceRouteHopsMaxRtt_Object = MibTableColumn
zhoneTraceRouteHopsMaxRtt = _ZhoneTraceRouteHopsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 5, 1, 5),
    _ZhoneTraceRouteHopsMaxRtt_Type()
)
zhoneTraceRouteHopsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsMaxRtt.setStatus("current")
_ZhoneTraceRouteHopsAverageRtt_Type = Unsigned32
_ZhoneTraceRouteHopsAverageRtt_Object = MibTableColumn
zhoneTraceRouteHopsAverageRtt = _ZhoneTraceRouteHopsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 5, 1, 6),
    _ZhoneTraceRouteHopsAverageRtt_Type()
)
zhoneTraceRouteHopsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsAverageRtt.setStatus("current")
_ZhoneTraceRouteHopsRttSumOfSquares_Type = Unsigned32
_ZhoneTraceRouteHopsRttSumOfSquares_Object = MibTableColumn
zhoneTraceRouteHopsRttSumOfSquares = _ZhoneTraceRouteHopsRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 5, 1, 7),
    _ZhoneTraceRouteHopsRttSumOfSquares_Type()
)
zhoneTraceRouteHopsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsRttSumOfSquares.setStatus("current")
_ZhoneTraceRouteHopsSentProbes_Type = Unsigned32
_ZhoneTraceRouteHopsSentProbes_Object = MibTableColumn
zhoneTraceRouteHopsSentProbes = _ZhoneTraceRouteHopsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 5, 1, 8),
    _ZhoneTraceRouteHopsSentProbes_Type()
)
zhoneTraceRouteHopsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsSentProbes.setStatus("current")
_ZhoneTraceRouteHopsProbeResponses_Type = Unsigned32
_ZhoneTraceRouteHopsProbeResponses_Object = MibTableColumn
zhoneTraceRouteHopsProbeResponses = _ZhoneTraceRouteHopsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 5, 1, 9),
    _ZhoneTraceRouteHopsProbeResponses_Type()
)
zhoneTraceRouteHopsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsProbeResponses.setStatus("current")
_ZhoneTraceRouteHopsLastGoodProbe_Type = DateAndTime
_ZhoneTraceRouteHopsLastGoodProbe_Object = MibTableColumn
zhoneTraceRouteHopsLastGoodProbe = _ZhoneTraceRouteHopsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 1, 5, 1, 10),
    _ZhoneTraceRouteHopsLastGoodProbe_Type()
)
zhoneTraceRouteHopsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsLastGoodProbe.setStatus("current")
_ZhoneTraceRouteConformance_ObjectIdentity = ObjectIdentity
zhoneTraceRouteConformance = _ZhoneTraceRouteConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 2)
)
_ZhoneTraceRouteGroups_ObjectIdentity = ObjectIdentity
zhoneTraceRouteGroups = _ZhoneTraceRouteGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 2, 1)
)
_ZhoneTraceRouteImplementationTypeDomains_ObjectIdentity = ObjectIdentity
zhoneTraceRouteImplementationTypeDomains = _ZhoneTraceRouteImplementationTypeDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 3)
)
_ZhoneTraceRouteUsingUdpProbes_ObjectIdentity = ObjectIdentity
zhoneTraceRouteUsingUdpProbes = _ZhoneTraceRouteUsingUdpProbes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 3, 1)
)
if mibBuilder.loadTexts:
    zhoneTraceRouteUsingUdpProbes.setStatus("current")

# Managed Objects groups

zhoneTraceRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 2, 1, 1)
)
zhoneTraceRouteGroup.setObjects(
      *(("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteMaxConcurrentRequests"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlTargetAddressType"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlTargetAddress"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlByPassRouteTable"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlDataSize"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlTimeOut"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlProbesPerHop"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlPort"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlMaxTtl"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlDSField"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlSourceAddressType"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlSourceAddress"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlIfIndex"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlMiscOptions"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlMaxFailures"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlDontFragment"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlInitialTtl"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlFrequency"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlStorageType"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlAdminStatus"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlMaxRows"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlTrapGeneration"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlDescr"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlCreateHopsEntries"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlType"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteCtlRowStatus"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteResultsOperStatus"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteResultsCurHopCount"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteResultsCurProbeCount"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteResultsIpTgtAddrType"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteResultsIpTgtAddr"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteResultsTestAttempts"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteResultsTestSuccesses"))
)
if mibBuilder.loadTexts:
    zhoneTraceRouteGroup.setStatus("current")

zhoneTraceRouteTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 2, 1, 2)
)
zhoneTraceRouteTimeStampGroup.setObjects(
    ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteResultsLastGoodPath")
)
if mibBuilder.loadTexts:
    zhoneTraceRouteTimeStampGroup.setStatus("current")

zhoneTraceRouteHopsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 2, 1, 4)
)
zhoneTraceRouteHopsTableGroup.setObjects(
      *(("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteHopsIpTgtAddressType"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteHopsIpTgtAddress"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteHopsMinRtt"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteHopsMaxRtt"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteHopsAverageRtt"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteHopsRttSumOfSquares"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteHopsSentProbes"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteHopsProbeResponses"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteHopsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    zhoneTraceRouteHopsTableGroup.setStatus("current")


# Notification objects

zhoneTraceRoutePathChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 0, 1)
)
zhoneTraceRoutePathChange.setObjects(
    ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteResultsIpTgtAddr")
)
if mibBuilder.loadTexts:
    zhoneTraceRoutePathChange.setStatus(
        "current"
    )

zhoneTraceRouteTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 0, 2)
)
zhoneTraceRouteTestFailed.setObjects(
    ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteResultsIpTgtAddr")
)
if mibBuilder.loadTexts:
    zhoneTraceRouteTestFailed.setStatus(
        "current"
    )

zhoneTraceRouteTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 0, 3)
)
zhoneTraceRouteTestCompleted.setObjects(
    ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteResultsIpTgtAddr")
)
if mibBuilder.loadTexts:
    zhoneTraceRouteTestCompleted.setStatus(
        "current"
    )


# Notifications groups

zhoneTraceRouteNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 20, 2, 1, 3)
)
zhoneTraceRouteNotificationsGroup.setObjects(
      *(("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRoutePathChange"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteTestFailed"),
        ("ZHONE-DISMAN-TRACEROUTE-MIB", "zhoneTraceRouteTestCompleted"))
)
if mibBuilder.loadTexts:
    zhoneTraceRouteNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-DISMAN-TRACEROUTE-MIB",
    **{"zhoneTraceRouteMIB": zhoneTraceRouteMIB,
       "zhoneTraceRouteNotifications": zhoneTraceRouteNotifications,
       "zhoneTraceRoutePathChange": zhoneTraceRoutePathChange,
       "zhoneTraceRouteTestFailed": zhoneTraceRouteTestFailed,
       "zhoneTraceRouteTestCompleted": zhoneTraceRouteTestCompleted,
       "zhoneTraceRouteObjects": zhoneTraceRouteObjects,
       "zhoneTraceRouteMaxConcurrentRequests": zhoneTraceRouteMaxConcurrentRequests,
       "zhoneTraceRouteCtlIndexNext": zhoneTraceRouteCtlIndexNext,
       "zhoneTraceRouteCtlTable": zhoneTraceRouteCtlTable,
       "zhoneTraceRouteCtlEntry": zhoneTraceRouteCtlEntry,
       "zhoneTraceRouteCtlIndex": zhoneTraceRouteCtlIndex,
       "zhoneTraceRouteCtlTargetAddressType": zhoneTraceRouteCtlTargetAddressType,
       "zhoneTraceRouteCtlTargetAddress": zhoneTraceRouteCtlTargetAddress,
       "zhoneTraceRouteCtlByPassRouteTable": zhoneTraceRouteCtlByPassRouteTable,
       "zhoneTraceRouteCtlDataSize": zhoneTraceRouteCtlDataSize,
       "zhoneTraceRouteCtlTimeOut": zhoneTraceRouteCtlTimeOut,
       "zhoneTraceRouteCtlProbesPerHop": zhoneTraceRouteCtlProbesPerHop,
       "zhoneTraceRouteCtlPort": zhoneTraceRouteCtlPort,
       "zhoneTraceRouteCtlMaxTtl": zhoneTraceRouteCtlMaxTtl,
       "zhoneTraceRouteCtlDSField": zhoneTraceRouteCtlDSField,
       "zhoneTraceRouteCtlSourceAddressType": zhoneTraceRouteCtlSourceAddressType,
       "zhoneTraceRouteCtlSourceAddress": zhoneTraceRouteCtlSourceAddress,
       "zhoneTraceRouteCtlIfIndex": zhoneTraceRouteCtlIfIndex,
       "zhoneTraceRouteCtlMiscOptions": zhoneTraceRouteCtlMiscOptions,
       "zhoneTraceRouteCtlMaxFailures": zhoneTraceRouteCtlMaxFailures,
       "zhoneTraceRouteCtlDontFragment": zhoneTraceRouteCtlDontFragment,
       "zhoneTraceRouteCtlInitialTtl": zhoneTraceRouteCtlInitialTtl,
       "zhoneTraceRouteCtlFrequency": zhoneTraceRouteCtlFrequency,
       "zhoneTraceRouteCtlStorageType": zhoneTraceRouteCtlStorageType,
       "zhoneTraceRouteCtlAdminStatus": zhoneTraceRouteCtlAdminStatus,
       "zhoneTraceRouteCtlDescr": zhoneTraceRouteCtlDescr,
       "zhoneTraceRouteCtlMaxRows": zhoneTraceRouteCtlMaxRows,
       "zhoneTraceRouteCtlTrapGeneration": zhoneTraceRouteCtlTrapGeneration,
       "zhoneTraceRouteCtlCreateHopsEntries": zhoneTraceRouteCtlCreateHopsEntries,
       "zhoneTraceRouteCtlType": zhoneTraceRouteCtlType,
       "zhoneTraceRouteCtlRowStatus": zhoneTraceRouteCtlRowStatus,
       "zhoneTraceRouteResultsTable": zhoneTraceRouteResultsTable,
       "zhoneTraceRouteResultsEntry": zhoneTraceRouteResultsEntry,
       "zhoneTraceRouteResultsOperStatus": zhoneTraceRouteResultsOperStatus,
       "zhoneTraceRouteResultsCurHopCount": zhoneTraceRouteResultsCurHopCount,
       "zhoneTraceRouteResultsCurProbeCount": zhoneTraceRouteResultsCurProbeCount,
       "zhoneTraceRouteResultsIpTgtAddrType": zhoneTraceRouteResultsIpTgtAddrType,
       "zhoneTraceRouteResultsIpTgtAddr": zhoneTraceRouteResultsIpTgtAddr,
       "zhoneTraceRouteResultsTestAttempts": zhoneTraceRouteResultsTestAttempts,
       "zhoneTraceRouteResultsTestSuccesses": zhoneTraceRouteResultsTestSuccesses,
       "zhoneTraceRouteResultsLastGoodPath": zhoneTraceRouteResultsLastGoodPath,
       "zhoneTraceRouteHopsTable": zhoneTraceRouteHopsTable,
       "zhoneTraceRouteHopsEntry": zhoneTraceRouteHopsEntry,
       "zhoneTraceRouteHopsHopIndex": zhoneTraceRouteHopsHopIndex,
       "zhoneTraceRouteHopsIpTgtAddressType": zhoneTraceRouteHopsIpTgtAddressType,
       "zhoneTraceRouteHopsIpTgtAddress": zhoneTraceRouteHopsIpTgtAddress,
       "zhoneTraceRouteHopsMinRtt": zhoneTraceRouteHopsMinRtt,
       "zhoneTraceRouteHopsMaxRtt": zhoneTraceRouteHopsMaxRtt,
       "zhoneTraceRouteHopsAverageRtt": zhoneTraceRouteHopsAverageRtt,
       "zhoneTraceRouteHopsRttSumOfSquares": zhoneTraceRouteHopsRttSumOfSquares,
       "zhoneTraceRouteHopsSentProbes": zhoneTraceRouteHopsSentProbes,
       "zhoneTraceRouteHopsProbeResponses": zhoneTraceRouteHopsProbeResponses,
       "zhoneTraceRouteHopsLastGoodProbe": zhoneTraceRouteHopsLastGoodProbe,
       "zhoneTraceRouteConformance": zhoneTraceRouteConformance,
       "zhoneTraceRouteGroups": zhoneTraceRouteGroups,
       "zhoneTraceRouteGroup": zhoneTraceRouteGroup,
       "zhoneTraceRouteTimeStampGroup": zhoneTraceRouteTimeStampGroup,
       "zhoneTraceRouteNotificationsGroup": zhoneTraceRouteNotificationsGroup,
       "zhoneTraceRouteHopsTableGroup": zhoneTraceRouteHopsTableGroup,
       "zhoneTraceRouteImplementationTypeDomains": zhoneTraceRouteImplementationTypeDomains,
       "zhoneTraceRouteUsingUdpProbes": zhoneTraceRouteUsingUdpProbes}
)
