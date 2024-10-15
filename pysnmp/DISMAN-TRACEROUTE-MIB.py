# SNMP MIB module (DISMAN-TRACEROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DISMAN-TRACEROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:18 2024
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

(OperationResponseStatus,) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "OperationResponseStatus")

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

traceRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 81)
)
traceRouteMIB.setRevisions(
        ("2006-06-13 00:00",
         "2000-09-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TraceRouteNotifications_ObjectIdentity = ObjectIdentity
traceRouteNotifications = _TraceRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 81, 0)
)
_TraceRouteObjects_ObjectIdentity = ObjectIdentity
traceRouteObjects = _TraceRouteObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 81, 1)
)


class _TraceRouteMaxConcurrentRequests_Type(Unsigned32):
    """Custom type traceRouteMaxConcurrentRequests based on Unsigned32"""
    defaultValue = 10


_TraceRouteMaxConcurrentRequests_Object = MibScalar
traceRouteMaxConcurrentRequests = _TraceRouteMaxConcurrentRequests_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 1),
    _TraceRouteMaxConcurrentRequests_Type()
)
traceRouteMaxConcurrentRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRouteMaxConcurrentRequests.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteMaxConcurrentRequests.setUnits("requests")
_TraceRouteCtlTable_Object = MibTable
traceRouteCtlTable = _TraceRouteCtlTable_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2)
)
if mibBuilder.loadTexts:
    traceRouteCtlTable.setStatus("current")
_TraceRouteCtlEntry_Object = MibTableRow
traceRouteCtlEntry = _TraceRouteCtlEntry_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1)
)
traceRouteCtlEntry.setIndexNames(
    (0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlOwnerIndex"),
    (0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlTestName"),
)
if mibBuilder.loadTexts:
    traceRouteCtlEntry.setStatus("current")


class _TraceRouteCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type traceRouteCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TraceRouteCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_TraceRouteCtlOwnerIndex_Object = MibTableColumn
traceRouteCtlOwnerIndex = _TraceRouteCtlOwnerIndex_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 1),
    _TraceRouteCtlOwnerIndex_Type()
)
traceRouteCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteCtlOwnerIndex.setStatus("current")


class _TraceRouteCtlTestName_Type(SnmpAdminString):
    """Custom type traceRouteCtlTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TraceRouteCtlTestName_Type.__name__ = "SnmpAdminString"
_TraceRouteCtlTestName_Object = MibTableColumn
traceRouteCtlTestName = _TraceRouteCtlTestName_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 2),
    _TraceRouteCtlTestName_Type()
)
traceRouteCtlTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteCtlTestName.setStatus("current")


class _TraceRouteCtlTargetAddressType_Type(InetAddressType):
    """Custom type traceRouteCtlTargetAddressType based on InetAddressType"""


_TraceRouteCtlTargetAddressType_Object = MibTableColumn
traceRouteCtlTargetAddressType = _TraceRouteCtlTargetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 3),
    _TraceRouteCtlTargetAddressType_Type()
)
traceRouteCtlTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlTargetAddressType.setStatus("current")
_TraceRouteCtlTargetAddress_Type = InetAddress
_TraceRouteCtlTargetAddress_Object = MibTableColumn
traceRouteCtlTargetAddress = _TraceRouteCtlTargetAddress_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 4),
    _TraceRouteCtlTargetAddress_Type()
)
traceRouteCtlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlTargetAddress.setStatus("current")


class _TraceRouteCtlByPassRouteTable_Type(TruthValue):
    """Custom type traceRouteCtlByPassRouteTable based on TruthValue"""


_TraceRouteCtlByPassRouteTable_Object = MibTableColumn
traceRouteCtlByPassRouteTable = _TraceRouteCtlByPassRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 5),
    _TraceRouteCtlByPassRouteTable_Type()
)
traceRouteCtlByPassRouteTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlByPassRouteTable.setStatus("current")


class _TraceRouteCtlDataSize_Type(Unsigned32):
    """Custom type traceRouteCtlDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65507),
    )


_TraceRouteCtlDataSize_Type.__name__ = "Unsigned32"
_TraceRouteCtlDataSize_Object = MibTableColumn
traceRouteCtlDataSize = _TraceRouteCtlDataSize_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 6),
    _TraceRouteCtlDataSize_Type()
)
traceRouteCtlDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlDataSize.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlDataSize.setUnits("octets")


class _TraceRouteCtlTimeOut_Type(Unsigned32):
    """Custom type traceRouteCtlTimeOut based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TraceRouteCtlTimeOut_Type.__name__ = "Unsigned32"
_TraceRouteCtlTimeOut_Object = MibTableColumn
traceRouteCtlTimeOut = _TraceRouteCtlTimeOut_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 7),
    _TraceRouteCtlTimeOut_Type()
)
traceRouteCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlTimeOut.setUnits("seconds")


class _TraceRouteCtlProbesPerHop_Type(Unsigned32):
    """Custom type traceRouteCtlProbesPerHop based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TraceRouteCtlProbesPerHop_Type.__name__ = "Unsigned32"
_TraceRouteCtlProbesPerHop_Object = MibTableColumn
traceRouteCtlProbesPerHop = _TraceRouteCtlProbesPerHop_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 8),
    _TraceRouteCtlProbesPerHop_Type()
)
traceRouteCtlProbesPerHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlProbesPerHop.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlProbesPerHop.setUnits("probes")


class _TraceRouteCtlPort_Type(Unsigned32):
    """Custom type traceRouteCtlPort based on Unsigned32"""
    defaultValue = 33434

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TraceRouteCtlPort_Type.__name__ = "Unsigned32"
_TraceRouteCtlPort_Object = MibTableColumn
traceRouteCtlPort = _TraceRouteCtlPort_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 9),
    _TraceRouteCtlPort_Type()
)
traceRouteCtlPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlPort.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlPort.setUnits("UDP Port")


class _TraceRouteCtlMaxTtl_Type(Unsigned32):
    """Custom type traceRouteCtlMaxTtl based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TraceRouteCtlMaxTtl_Type.__name__ = "Unsigned32"
_TraceRouteCtlMaxTtl_Object = MibTableColumn
traceRouteCtlMaxTtl = _TraceRouteCtlMaxTtl_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 10),
    _TraceRouteCtlMaxTtl_Type()
)
traceRouteCtlMaxTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlMaxTtl.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlMaxTtl.setUnits("time-to-live value")


class _TraceRouteCtlDSField_Type(Unsigned32):
    """Custom type traceRouteCtlDSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TraceRouteCtlDSField_Type.__name__ = "Unsigned32"
_TraceRouteCtlDSField_Object = MibTableColumn
traceRouteCtlDSField = _TraceRouteCtlDSField_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 11),
    _TraceRouteCtlDSField_Type()
)
traceRouteCtlDSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlDSField.setStatus("current")


class _TraceRouteCtlSourceAddressType_Type(InetAddressType):
    """Custom type traceRouteCtlSourceAddressType based on InetAddressType"""


_TraceRouteCtlSourceAddressType_Object = MibTableColumn
traceRouteCtlSourceAddressType = _TraceRouteCtlSourceAddressType_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 12),
    _TraceRouteCtlSourceAddressType_Type()
)
traceRouteCtlSourceAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlSourceAddressType.setStatus("current")


class _TraceRouteCtlSourceAddress_Type(InetAddress):
    """Custom type traceRouteCtlSourceAddress based on InetAddress"""
    defaultHexValue = ""


_TraceRouteCtlSourceAddress_Object = MibTableColumn
traceRouteCtlSourceAddress = _TraceRouteCtlSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 13),
    _TraceRouteCtlSourceAddress_Type()
)
traceRouteCtlSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlSourceAddress.setStatus("current")


class _TraceRouteCtlIfIndex_Type(InterfaceIndexOrZero):
    """Custom type traceRouteCtlIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TraceRouteCtlIfIndex_Object = MibTableColumn
traceRouteCtlIfIndex = _TraceRouteCtlIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 14),
    _TraceRouteCtlIfIndex_Type()
)
traceRouteCtlIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlIfIndex.setStatus("current")


class _TraceRouteCtlMiscOptions_Type(SnmpAdminString):
    """Custom type traceRouteCtlMiscOptions based on SnmpAdminString"""
    defaultHexValue = ""


_TraceRouteCtlMiscOptions_Object = MibTableColumn
traceRouteCtlMiscOptions = _TraceRouteCtlMiscOptions_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 15),
    _TraceRouteCtlMiscOptions_Type()
)
traceRouteCtlMiscOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlMiscOptions.setStatus("current")


class _TraceRouteCtlMaxFailures_Type(Unsigned32):
    """Custom type traceRouteCtlMaxFailures based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TraceRouteCtlMaxFailures_Type.__name__ = "Unsigned32"
_TraceRouteCtlMaxFailures_Object = MibTableColumn
traceRouteCtlMaxFailures = _TraceRouteCtlMaxFailures_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 16),
    _TraceRouteCtlMaxFailures_Type()
)
traceRouteCtlMaxFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlMaxFailures.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlMaxFailures.setUnits("timeouts")


class _TraceRouteCtlDontFragment_Type(TruthValue):
    """Custom type traceRouteCtlDontFragment based on TruthValue"""


_TraceRouteCtlDontFragment_Object = MibTableColumn
traceRouteCtlDontFragment = _TraceRouteCtlDontFragment_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 17),
    _TraceRouteCtlDontFragment_Type()
)
traceRouteCtlDontFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlDontFragment.setStatus("current")


class _TraceRouteCtlInitialTtl_Type(Unsigned32):
    """Custom type traceRouteCtlInitialTtl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TraceRouteCtlInitialTtl_Type.__name__ = "Unsigned32"
_TraceRouteCtlInitialTtl_Object = MibTableColumn
traceRouteCtlInitialTtl = _TraceRouteCtlInitialTtl_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 18),
    _TraceRouteCtlInitialTtl_Type()
)
traceRouteCtlInitialTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlInitialTtl.setStatus("current")


class _TraceRouteCtlFrequency_Type(Unsigned32):
    """Custom type traceRouteCtlFrequency based on Unsigned32"""
    defaultValue = 0


_TraceRouteCtlFrequency_Object = MibTableColumn
traceRouteCtlFrequency = _TraceRouteCtlFrequency_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 19),
    _TraceRouteCtlFrequency_Type()
)
traceRouteCtlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlFrequency.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlFrequency.setUnits("seconds")


class _TraceRouteCtlStorageType_Type(StorageType):
    """Custom type traceRouteCtlStorageType based on StorageType"""


_TraceRouteCtlStorageType_Object = MibTableColumn
traceRouteCtlStorageType = _TraceRouteCtlStorageType_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 20),
    _TraceRouteCtlStorageType_Type()
)
traceRouteCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlStorageType.setStatus("current")


class _TraceRouteCtlAdminStatus_Type(Integer32):
    """Custom type traceRouteCtlAdminStatus based on Integer32"""
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


_TraceRouteCtlAdminStatus_Type.__name__ = "Integer32"
_TraceRouteCtlAdminStatus_Object = MibTableColumn
traceRouteCtlAdminStatus = _TraceRouteCtlAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 21),
    _TraceRouteCtlAdminStatus_Type()
)
traceRouteCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlAdminStatus.setStatus("current")


class _TraceRouteCtlDescr_Type(SnmpAdminString):
    """Custom type traceRouteCtlDescr based on SnmpAdminString"""
    defaultHexValue = ""


_TraceRouteCtlDescr_Object = MibTableColumn
traceRouteCtlDescr = _TraceRouteCtlDescr_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 22),
    _TraceRouteCtlDescr_Type()
)
traceRouteCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlDescr.setStatus("current")


class _TraceRouteCtlMaxRows_Type(Unsigned32):
    """Custom type traceRouteCtlMaxRows based on Unsigned32"""
    defaultValue = 50


_TraceRouteCtlMaxRows_Object = MibTableColumn
traceRouteCtlMaxRows = _TraceRouteCtlMaxRows_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 23),
    _TraceRouteCtlMaxRows_Type()
)
traceRouteCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlMaxRows.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlMaxRows.setUnits("rows")


class _TraceRouteCtlTrapGeneration_Type(Bits):
    """Custom type traceRouteCtlTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("pathChange", 0),
          ("testCompletion", 2),
          ("testFailure", 1))
    )

_TraceRouteCtlTrapGeneration_Type.__name__ = "Bits"
_TraceRouteCtlTrapGeneration_Object = MibTableColumn
traceRouteCtlTrapGeneration = _TraceRouteCtlTrapGeneration_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 24),
    _TraceRouteCtlTrapGeneration_Type()
)
traceRouteCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlTrapGeneration.setStatus("current")


class _TraceRouteCtlCreateHopsEntries_Type(TruthValue):
    """Custom type traceRouteCtlCreateHopsEntries based on TruthValue"""


_TraceRouteCtlCreateHopsEntries_Object = MibTableColumn
traceRouteCtlCreateHopsEntries = _TraceRouteCtlCreateHopsEntries_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 25),
    _TraceRouteCtlCreateHopsEntries_Type()
)
traceRouteCtlCreateHopsEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlCreateHopsEntries.setStatus("current")


class _TraceRouteCtlType_Type(ObjectIdentifier):
    """Custom type traceRouteCtlType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 2, 1, 81, 3, 1)


_TraceRouteCtlType_Object = MibTableColumn
traceRouteCtlType = _TraceRouteCtlType_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 26),
    _TraceRouteCtlType_Type()
)
traceRouteCtlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlType.setStatus("current")
_TraceRouteCtlRowStatus_Type = RowStatus
_TraceRouteCtlRowStatus_Object = MibTableColumn
traceRouteCtlRowStatus = _TraceRouteCtlRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 27),
    _TraceRouteCtlRowStatus_Type()
)
traceRouteCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlRowStatus.setStatus("current")
_TraceRouteResultsTable_Object = MibTable
traceRouteResultsTable = _TraceRouteResultsTable_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 3)
)
if mibBuilder.loadTexts:
    traceRouteResultsTable.setStatus("current")
_TraceRouteResultsEntry_Object = MibTableRow
traceRouteResultsEntry = _TraceRouteResultsEntry_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 3, 1)
)
traceRouteResultsEntry.setIndexNames(
    (0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlOwnerIndex"),
    (0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlTestName"),
)
if mibBuilder.loadTexts:
    traceRouteResultsEntry.setStatus("current")


class _TraceRouteResultsOperStatus_Type(Integer32):
    """Custom type traceRouteResultsOperStatus based on Integer32"""
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


_TraceRouteResultsOperStatus_Type.__name__ = "Integer32"
_TraceRouteResultsOperStatus_Object = MibTableColumn
traceRouteResultsOperStatus = _TraceRouteResultsOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 1),
    _TraceRouteResultsOperStatus_Type()
)
traceRouteResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsOperStatus.setStatus("current")
_TraceRouteResultsCurHopCount_Type = Gauge32
_TraceRouteResultsCurHopCount_Object = MibTableColumn
traceRouteResultsCurHopCount = _TraceRouteResultsCurHopCount_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 2),
    _TraceRouteResultsCurHopCount_Type()
)
traceRouteResultsCurHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsCurHopCount.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteResultsCurHopCount.setUnits("hops")
_TraceRouteResultsCurProbeCount_Type = Gauge32
_TraceRouteResultsCurProbeCount_Object = MibTableColumn
traceRouteResultsCurProbeCount = _TraceRouteResultsCurProbeCount_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 3),
    _TraceRouteResultsCurProbeCount_Type()
)
traceRouteResultsCurProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsCurProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteResultsCurProbeCount.setUnits("probes")
_TraceRouteResultsIpTgtAddrType_Type = InetAddressType
_TraceRouteResultsIpTgtAddrType_Object = MibTableColumn
traceRouteResultsIpTgtAddrType = _TraceRouteResultsIpTgtAddrType_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 4),
    _TraceRouteResultsIpTgtAddrType_Type()
)
traceRouteResultsIpTgtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsIpTgtAddrType.setStatus("current")
_TraceRouteResultsIpTgtAddr_Type = InetAddress
_TraceRouteResultsIpTgtAddr_Object = MibTableColumn
traceRouteResultsIpTgtAddr = _TraceRouteResultsIpTgtAddr_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 5),
    _TraceRouteResultsIpTgtAddr_Type()
)
traceRouteResultsIpTgtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsIpTgtAddr.setStatus("current")
_TraceRouteResultsTestAttempts_Type = Gauge32
_TraceRouteResultsTestAttempts_Object = MibTableColumn
traceRouteResultsTestAttempts = _TraceRouteResultsTestAttempts_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 6),
    _TraceRouteResultsTestAttempts_Type()
)
traceRouteResultsTestAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsTestAttempts.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteResultsTestAttempts.setUnits("tests")
_TraceRouteResultsTestSuccesses_Type = Gauge32
_TraceRouteResultsTestSuccesses_Object = MibTableColumn
traceRouteResultsTestSuccesses = _TraceRouteResultsTestSuccesses_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 7),
    _TraceRouteResultsTestSuccesses_Type()
)
traceRouteResultsTestSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsTestSuccesses.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteResultsTestSuccesses.setUnits("tests")
_TraceRouteResultsLastGoodPath_Type = DateAndTime
_TraceRouteResultsLastGoodPath_Object = MibTableColumn
traceRouteResultsLastGoodPath = _TraceRouteResultsLastGoodPath_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 8),
    _TraceRouteResultsLastGoodPath_Type()
)
traceRouteResultsLastGoodPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsLastGoodPath.setStatus("current")
_TraceRouteProbeHistoryTable_Object = MibTable
traceRouteProbeHistoryTable = _TraceRouteProbeHistoryTable_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 4)
)
if mibBuilder.loadTexts:
    traceRouteProbeHistoryTable.setStatus("current")
_TraceRouteProbeHistoryEntry_Object = MibTableRow
traceRouteProbeHistoryEntry = _TraceRouteProbeHistoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 4, 1)
)
traceRouteProbeHistoryEntry.setIndexNames(
    (0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlOwnerIndex"),
    (0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlTestName"),
    (0, "DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryIndex"),
    (0, "DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryHopIndex"),
    (0, "DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    traceRouteProbeHistoryEntry.setStatus("current")


class _TraceRouteProbeHistoryIndex_Type(Unsigned32):
    """Custom type traceRouteProbeHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TraceRouteProbeHistoryIndex_Type.__name__ = "Unsigned32"
_TraceRouteProbeHistoryIndex_Object = MibTableColumn
traceRouteProbeHistoryIndex = _TraceRouteProbeHistoryIndex_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 1),
    _TraceRouteProbeHistoryIndex_Type()
)
traceRouteProbeHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryIndex.setStatus("current")


class _TraceRouteProbeHistoryHopIndex_Type(Unsigned32):
    """Custom type traceRouteProbeHistoryHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TraceRouteProbeHistoryHopIndex_Type.__name__ = "Unsigned32"
_TraceRouteProbeHistoryHopIndex_Object = MibTableColumn
traceRouteProbeHistoryHopIndex = _TraceRouteProbeHistoryHopIndex_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 2),
    _TraceRouteProbeHistoryHopIndex_Type()
)
traceRouteProbeHistoryHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryHopIndex.setStatus("current")


class _TraceRouteProbeHistoryProbeIndex_Type(Unsigned32):
    """Custom type traceRouteProbeHistoryProbeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TraceRouteProbeHistoryProbeIndex_Type.__name__ = "Unsigned32"
_TraceRouteProbeHistoryProbeIndex_Object = MibTableColumn
traceRouteProbeHistoryProbeIndex = _TraceRouteProbeHistoryProbeIndex_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 3),
    _TraceRouteProbeHistoryProbeIndex_Type()
)
traceRouteProbeHistoryProbeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryProbeIndex.setStatus("current")
_TraceRouteProbeHistoryHAddrType_Type = InetAddressType
_TraceRouteProbeHistoryHAddrType_Object = MibTableColumn
traceRouteProbeHistoryHAddrType = _TraceRouteProbeHistoryHAddrType_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 4),
    _TraceRouteProbeHistoryHAddrType_Type()
)
traceRouteProbeHistoryHAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryHAddrType.setStatus("current")
_TraceRouteProbeHistoryHAddr_Type = InetAddress
_TraceRouteProbeHistoryHAddr_Object = MibTableColumn
traceRouteProbeHistoryHAddr = _TraceRouteProbeHistoryHAddr_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 5),
    _TraceRouteProbeHistoryHAddr_Type()
)
traceRouteProbeHistoryHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryHAddr.setStatus("current")
_TraceRouteProbeHistoryResponse_Type = Unsigned32
_TraceRouteProbeHistoryResponse_Object = MibTableColumn
traceRouteProbeHistoryResponse = _TraceRouteProbeHistoryResponse_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 6),
    _TraceRouteProbeHistoryResponse_Type()
)
traceRouteProbeHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryResponse.setUnits("milliseconds")
_TraceRouteProbeHistoryStatus_Type = OperationResponseStatus
_TraceRouteProbeHistoryStatus_Object = MibTableColumn
traceRouteProbeHistoryStatus = _TraceRouteProbeHistoryStatus_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 7),
    _TraceRouteProbeHistoryStatus_Type()
)
traceRouteProbeHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryStatus.setStatus("current")
_TraceRouteProbeHistoryLastRC_Type = Integer32
_TraceRouteProbeHistoryLastRC_Object = MibTableColumn
traceRouteProbeHistoryLastRC = _TraceRouteProbeHistoryLastRC_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 8),
    _TraceRouteProbeHistoryLastRC_Type()
)
traceRouteProbeHistoryLastRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryLastRC.setStatus("current")
_TraceRouteProbeHistoryTime_Type = DateAndTime
_TraceRouteProbeHistoryTime_Object = MibTableColumn
traceRouteProbeHistoryTime = _TraceRouteProbeHistoryTime_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 9),
    _TraceRouteProbeHistoryTime_Type()
)
traceRouteProbeHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryTime.setStatus("current")
_TraceRouteHopsTable_Object = MibTable
traceRouteHopsTable = _TraceRouteHopsTable_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 5)
)
if mibBuilder.loadTexts:
    traceRouteHopsTable.setStatus("current")
_TraceRouteHopsEntry_Object = MibTableRow
traceRouteHopsEntry = _TraceRouteHopsEntry_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 5, 1)
)
traceRouteHopsEntry.setIndexNames(
    (0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlOwnerIndex"),
    (0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlTestName"),
    (0, "DISMAN-TRACEROUTE-MIB", "traceRouteHopsHopIndex"),
)
if mibBuilder.loadTexts:
    traceRouteHopsEntry.setStatus("current")


class _TraceRouteHopsHopIndex_Type(Unsigned32):
    """Custom type traceRouteHopsHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TraceRouteHopsHopIndex_Type.__name__ = "Unsigned32"
_TraceRouteHopsHopIndex_Object = MibTableColumn
traceRouteHopsHopIndex = _TraceRouteHopsHopIndex_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 1),
    _TraceRouteHopsHopIndex_Type()
)
traceRouteHopsHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteHopsHopIndex.setStatus("current")
_TraceRouteHopsIpTgtAddressType_Type = InetAddressType
_TraceRouteHopsIpTgtAddressType_Object = MibTableColumn
traceRouteHopsIpTgtAddressType = _TraceRouteHopsIpTgtAddressType_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 2),
    _TraceRouteHopsIpTgtAddressType_Type()
)
traceRouteHopsIpTgtAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsIpTgtAddressType.setStatus("current")
_TraceRouteHopsIpTgtAddress_Type = InetAddress
_TraceRouteHopsIpTgtAddress_Object = MibTableColumn
traceRouteHopsIpTgtAddress = _TraceRouteHopsIpTgtAddress_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 3),
    _TraceRouteHopsIpTgtAddress_Type()
)
traceRouteHopsIpTgtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsIpTgtAddress.setStatus("current")
_TraceRouteHopsMinRtt_Type = Unsigned32
_TraceRouteHopsMinRtt_Object = MibTableColumn
traceRouteHopsMinRtt = _TraceRouteHopsMinRtt_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 4),
    _TraceRouteHopsMinRtt_Type()
)
traceRouteHopsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsMinRtt.setStatus("current")
_TraceRouteHopsMaxRtt_Type = Unsigned32
_TraceRouteHopsMaxRtt_Object = MibTableColumn
traceRouteHopsMaxRtt = _TraceRouteHopsMaxRtt_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 5),
    _TraceRouteHopsMaxRtt_Type()
)
traceRouteHopsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsMaxRtt.setStatus("current")
_TraceRouteHopsAverageRtt_Type = Unsigned32
_TraceRouteHopsAverageRtt_Object = MibTableColumn
traceRouteHopsAverageRtt = _TraceRouteHopsAverageRtt_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 6),
    _TraceRouteHopsAverageRtt_Type()
)
traceRouteHopsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsAverageRtt.setStatus("current")
_TraceRouteHopsRttSumOfSquares_Type = Unsigned32
_TraceRouteHopsRttSumOfSquares_Object = MibTableColumn
traceRouteHopsRttSumOfSquares = _TraceRouteHopsRttSumOfSquares_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 7),
    _TraceRouteHopsRttSumOfSquares_Type()
)
traceRouteHopsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsRttSumOfSquares.setStatus("current")
_TraceRouteHopsSentProbes_Type = Unsigned32
_TraceRouteHopsSentProbes_Object = MibTableColumn
traceRouteHopsSentProbes = _TraceRouteHopsSentProbes_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 8),
    _TraceRouteHopsSentProbes_Type()
)
traceRouteHopsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsSentProbes.setStatus("current")
_TraceRouteHopsProbeResponses_Type = Unsigned32
_TraceRouteHopsProbeResponses_Object = MibTableColumn
traceRouteHopsProbeResponses = _TraceRouteHopsProbeResponses_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 9),
    _TraceRouteHopsProbeResponses_Type()
)
traceRouteHopsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsProbeResponses.setStatus("current")
_TraceRouteHopsLastGoodProbe_Type = DateAndTime
_TraceRouteHopsLastGoodProbe_Object = MibTableColumn
traceRouteHopsLastGoodProbe = _TraceRouteHopsLastGoodProbe_Object(
    (1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 10),
    _TraceRouteHopsLastGoodProbe_Type()
)
traceRouteHopsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsLastGoodProbe.setStatus("current")
_TraceRouteConformance_ObjectIdentity = ObjectIdentity
traceRouteConformance = _TraceRouteConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 81, 2)
)
_TraceRouteCompliances_ObjectIdentity = ObjectIdentity
traceRouteCompliances = _TraceRouteCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 81, 2, 1)
)
_TraceRouteGroups_ObjectIdentity = ObjectIdentity
traceRouteGroups = _TraceRouteGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 81, 2, 2)
)
_TraceRouteImplementationTypeDomains_ObjectIdentity = ObjectIdentity
traceRouteImplementationTypeDomains = _TraceRouteImplementationTypeDomains_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 81, 3)
)
_TraceRouteUsingUdpProbes_ObjectIdentity = ObjectIdentity
traceRouteUsingUdpProbes = _TraceRouteUsingUdpProbes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 81, 3, 1)
)
if mibBuilder.loadTexts:
    traceRouteUsingUdpProbes.setStatus("current")

# Managed Objects groups

traceRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 81, 2, 2, 1)
)
traceRouteGroup.setObjects(
      *(("DISMAN-TRACEROUTE-MIB", "traceRouteMaxConcurrentRequests"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddressType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddress"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlByPassRouteTable"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDataSize"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTimeOut"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlProbesPerHop"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlPort"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMaxTtl"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDSField"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlSourceAddressType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlSourceAddress"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlIfIndex"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMiscOptions"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMaxFailures"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDontFragment"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlInitialTtl"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlFrequency"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlStorageType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlAdminStatus"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMaxRows"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTrapGeneration"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDescr"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlCreateHopsEntries"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlRowStatus"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsOperStatus"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsCurHopCount"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsCurProbeCount"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddrType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddr"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsTestAttempts"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsTestSuccesses"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryHAddrType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryHAddr"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryResponse"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryStatus"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryLastRC"))
)
if mibBuilder.loadTexts:
    traceRouteGroup.setStatus("deprecated")

traceRouteTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 81, 2, 2, 2)
)
traceRouteTimeStampGroup.setObjects(
      *(("DISMAN-TRACEROUTE-MIB", "traceRouteResultsLastGoodPath"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryTime"))
)
if mibBuilder.loadTexts:
    traceRouteTimeStampGroup.setStatus("deprecated")

traceRouteHopsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 81, 2, 2, 4)
)
traceRouteHopsTableGroup.setObjects(
      *(("DISMAN-TRACEROUTE-MIB", "traceRouteHopsIpTgtAddressType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsIpTgtAddress"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsMinRtt"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsMaxRtt"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsAverageRtt"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsRttSumOfSquares"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsSentProbes"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsProbeResponses"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    traceRouteHopsTableGroup.setStatus("current")

traceRouteMinimumGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 81, 2, 2, 5)
)
traceRouteMinimumGroup.setObjects(
      *(("DISMAN-TRACEROUTE-MIB", "traceRouteMaxConcurrentRequests"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddressType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddress"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlByPassRouteTable"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDataSize"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTimeOut"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlProbesPerHop"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlPort"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMaxTtl"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDSField"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlSourceAddressType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlSourceAddress"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlIfIndex"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMiscOptions"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMaxFailures"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDontFragment"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlInitialTtl"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlFrequency"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlStorageType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlAdminStatus"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMaxRows"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTrapGeneration"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDescr"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlCreateHopsEntries"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsOperStatus"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsCurHopCount"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsCurProbeCount"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddrType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddr"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsTestAttempts"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsTestSuccesses"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsLastGoodPath"))
)
if mibBuilder.loadTexts:
    traceRouteMinimumGroup.setStatus("current")

traceRouteCtlRowStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 81, 2, 2, 6)
)
traceRouteCtlRowStatusGroup.setObjects(
    ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlRowStatus")
)
if mibBuilder.loadTexts:
    traceRouteCtlRowStatusGroup.setStatus("current")

traceRouteHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 81, 2, 2, 7)
)
traceRouteHistoryGroup.setObjects(
      *(("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryHAddrType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryHAddr"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryResponse"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryStatus"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryLastRC"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryTime"))
)
if mibBuilder.loadTexts:
    traceRouteHistoryGroup.setStatus("current")


# Notification objects

traceRoutePathChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 81, 0, 1)
)
traceRoutePathChange.setObjects(
      *(("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddressType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddress"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddrType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddr"))
)
if mibBuilder.loadTexts:
    traceRoutePathChange.setStatus(
        "current"
    )

traceRouteTestFailed = NotificationType(
    (1, 3, 6, 1, 2, 1, 81, 0, 2)
)
traceRouteTestFailed.setObjects(
      *(("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddressType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddress"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddrType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddr"))
)
if mibBuilder.loadTexts:
    traceRouteTestFailed.setStatus(
        "current"
    )

traceRouteTestCompleted = NotificationType(
    (1, 3, 6, 1, 2, 1, 81, 0, 3)
)
traceRouteTestCompleted.setObjects(
      *(("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddressType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddress"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddrType"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddr"))
)
if mibBuilder.loadTexts:
    traceRouteTestCompleted.setStatus(
        "current"
    )


# Notifications groups

traceRouteNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 81, 2, 2, 3)
)
traceRouteNotificationsGroup.setObjects(
      *(("DISMAN-TRACEROUTE-MIB", "traceRoutePathChange"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteTestFailed"),
        ("DISMAN-TRACEROUTE-MIB", "traceRouteTestCompleted"))
)
if mibBuilder.loadTexts:
    traceRouteNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

traceRouteCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 81, 2, 1, 1)
)
if mibBuilder.loadTexts:
    traceRouteCompliance.setStatus(
        "deprecated"
    )

traceRouteFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 81, 2, 1, 2)
)
if mibBuilder.loadTexts:
    traceRouteFullCompliance.setStatus(
        "current"
    )

traceRouteMinimumCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 81, 2, 1, 3)
)
if mibBuilder.loadTexts:
    traceRouteMinimumCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DISMAN-TRACEROUTE-MIB",
    **{"traceRouteMIB": traceRouteMIB,
       "traceRouteNotifications": traceRouteNotifications,
       "traceRoutePathChange": traceRoutePathChange,
       "traceRouteTestFailed": traceRouteTestFailed,
       "traceRouteTestCompleted": traceRouteTestCompleted,
       "traceRouteObjects": traceRouteObjects,
       "traceRouteMaxConcurrentRequests": traceRouteMaxConcurrentRequests,
       "traceRouteCtlTable": traceRouteCtlTable,
       "traceRouteCtlEntry": traceRouteCtlEntry,
       "traceRouteCtlOwnerIndex": traceRouteCtlOwnerIndex,
       "traceRouteCtlTestName": traceRouteCtlTestName,
       "traceRouteCtlTargetAddressType": traceRouteCtlTargetAddressType,
       "traceRouteCtlTargetAddress": traceRouteCtlTargetAddress,
       "traceRouteCtlByPassRouteTable": traceRouteCtlByPassRouteTable,
       "traceRouteCtlDataSize": traceRouteCtlDataSize,
       "traceRouteCtlTimeOut": traceRouteCtlTimeOut,
       "traceRouteCtlProbesPerHop": traceRouteCtlProbesPerHop,
       "traceRouteCtlPort": traceRouteCtlPort,
       "traceRouteCtlMaxTtl": traceRouteCtlMaxTtl,
       "traceRouteCtlDSField": traceRouteCtlDSField,
       "traceRouteCtlSourceAddressType": traceRouteCtlSourceAddressType,
       "traceRouteCtlSourceAddress": traceRouteCtlSourceAddress,
       "traceRouteCtlIfIndex": traceRouteCtlIfIndex,
       "traceRouteCtlMiscOptions": traceRouteCtlMiscOptions,
       "traceRouteCtlMaxFailures": traceRouteCtlMaxFailures,
       "traceRouteCtlDontFragment": traceRouteCtlDontFragment,
       "traceRouteCtlInitialTtl": traceRouteCtlInitialTtl,
       "traceRouteCtlFrequency": traceRouteCtlFrequency,
       "traceRouteCtlStorageType": traceRouteCtlStorageType,
       "traceRouteCtlAdminStatus": traceRouteCtlAdminStatus,
       "traceRouteCtlDescr": traceRouteCtlDescr,
       "traceRouteCtlMaxRows": traceRouteCtlMaxRows,
       "traceRouteCtlTrapGeneration": traceRouteCtlTrapGeneration,
       "traceRouteCtlCreateHopsEntries": traceRouteCtlCreateHopsEntries,
       "traceRouteCtlType": traceRouteCtlType,
       "traceRouteCtlRowStatus": traceRouteCtlRowStatus,
       "traceRouteResultsTable": traceRouteResultsTable,
       "traceRouteResultsEntry": traceRouteResultsEntry,
       "traceRouteResultsOperStatus": traceRouteResultsOperStatus,
       "traceRouteResultsCurHopCount": traceRouteResultsCurHopCount,
       "traceRouteResultsCurProbeCount": traceRouteResultsCurProbeCount,
       "traceRouteResultsIpTgtAddrType": traceRouteResultsIpTgtAddrType,
       "traceRouteResultsIpTgtAddr": traceRouteResultsIpTgtAddr,
       "traceRouteResultsTestAttempts": traceRouteResultsTestAttempts,
       "traceRouteResultsTestSuccesses": traceRouteResultsTestSuccesses,
       "traceRouteResultsLastGoodPath": traceRouteResultsLastGoodPath,
       "traceRouteProbeHistoryTable": traceRouteProbeHistoryTable,
       "traceRouteProbeHistoryEntry": traceRouteProbeHistoryEntry,
       "traceRouteProbeHistoryIndex": traceRouteProbeHistoryIndex,
       "traceRouteProbeHistoryHopIndex": traceRouteProbeHistoryHopIndex,
       "traceRouteProbeHistoryProbeIndex": traceRouteProbeHistoryProbeIndex,
       "traceRouteProbeHistoryHAddrType": traceRouteProbeHistoryHAddrType,
       "traceRouteProbeHistoryHAddr": traceRouteProbeHistoryHAddr,
       "traceRouteProbeHistoryResponse": traceRouteProbeHistoryResponse,
       "traceRouteProbeHistoryStatus": traceRouteProbeHistoryStatus,
       "traceRouteProbeHistoryLastRC": traceRouteProbeHistoryLastRC,
       "traceRouteProbeHistoryTime": traceRouteProbeHistoryTime,
       "traceRouteHopsTable": traceRouteHopsTable,
       "traceRouteHopsEntry": traceRouteHopsEntry,
       "traceRouteHopsHopIndex": traceRouteHopsHopIndex,
       "traceRouteHopsIpTgtAddressType": traceRouteHopsIpTgtAddressType,
       "traceRouteHopsIpTgtAddress": traceRouteHopsIpTgtAddress,
       "traceRouteHopsMinRtt": traceRouteHopsMinRtt,
       "traceRouteHopsMaxRtt": traceRouteHopsMaxRtt,
       "traceRouteHopsAverageRtt": traceRouteHopsAverageRtt,
       "traceRouteHopsRttSumOfSquares": traceRouteHopsRttSumOfSquares,
       "traceRouteHopsSentProbes": traceRouteHopsSentProbes,
       "traceRouteHopsProbeResponses": traceRouteHopsProbeResponses,
       "traceRouteHopsLastGoodProbe": traceRouteHopsLastGoodProbe,
       "traceRouteConformance": traceRouteConformance,
       "traceRouteCompliances": traceRouteCompliances,
       "traceRouteCompliance": traceRouteCompliance,
       "traceRouteFullCompliance": traceRouteFullCompliance,
       "traceRouteMinimumCompliance": traceRouteMinimumCompliance,
       "traceRouteGroups": traceRouteGroups,
       "traceRouteGroup": traceRouteGroup,
       "traceRouteTimeStampGroup": traceRouteTimeStampGroup,
       "traceRouteNotificationsGroup": traceRouteNotificationsGroup,
       "traceRouteHopsTableGroup": traceRouteHopsTableGroup,
       "traceRouteMinimumGroup": traceRouteMinimumGroup,
       "traceRouteCtlRowStatusGroup": traceRouteCtlRowStatusGroup,
       "traceRouteHistoryGroup": traceRouteHistoryGroup,
       "traceRouteImplementationTypeDomains": traceRouteImplementationTypeDomains,
       "traceRouteUsingUdpProbes": traceRouteUsingUdpProbes}
)
