# SNMP MIB module (APPLICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPLICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:52 2024
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
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "mib-2",
    "zeroDotZero")

(DateAndTime,
 DisplayString,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")

(LongUtf8String,
 sysApplElmtRunIndex) = mibBuilder.importSymbols(
    "SYSAPPL-MIB",
    "LongUtf8String",
    "sysApplElmtRunIndex")


# MODULE-IDENTITY

applicationMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 62)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Unsigned64TC(Counter64, TextualConvention):
    status = "current"


class ApplTAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_ApplicationMibObjects_ObjectIdentity = ObjectIdentity
applicationMibObjects = _ApplicationMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 62, 1)
)
_ApplServiceGroup_ObjectIdentity = ObjectIdentity
applServiceGroup = _ApplServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 62, 1, 1)
)
_ApplSrvNameToSrvInstTable_Object = MibTable
applSrvNameToSrvInstTable = _ApplSrvNameToSrvInstTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 1, 1)
)
if mibBuilder.loadTexts:
    applSrvNameToSrvInstTable.setStatus("current")
_ApplSrvNameToSrvInstEntry_Object = MibTableRow
applSrvNameToSrvInstEntry = _ApplSrvNameToSrvInstEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 1, 1, 1)
)
applSrvNameToSrvInstEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applSrvName"),
    (0, "APPLICATION-MIB", "applSrvIndex"),
)
if mibBuilder.loadTexts:
    applSrvNameToSrvInstEntry.setStatus("current")
_ApplSrvInstQual_Type = SnmpAdminString
_ApplSrvInstQual_Object = MibTableColumn
applSrvInstQual = _ApplSrvInstQual_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 1, 1, 1, 1),
    _ApplSrvInstQual_Type()
)
applSrvInstQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applSrvInstQual.setStatus("current")
_ApplSrvInstToSrvNameTable_Object = MibTable
applSrvInstToSrvNameTable = _ApplSrvInstToSrvNameTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 1, 2)
)
if mibBuilder.loadTexts:
    applSrvInstToSrvNameTable.setStatus("current")
_ApplSrvInstToSrvNameEntry_Object = MibTableRow
applSrvInstToSrvNameEntry = _ApplSrvInstToSrvNameEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 1, 2, 1)
)
applSrvInstToSrvNameEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applSrvIndex"),
    (0, "APPLICATION-MIB", "applSrvName"),
)
if mibBuilder.loadTexts:
    applSrvInstToSrvNameEntry.setStatus("current")
_ApplSrvName_Type = SnmpAdminString
_ApplSrvName_Object = MibTableColumn
applSrvName = _ApplSrvName_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 1, 2, 1, 1),
    _ApplSrvName_Type()
)
applSrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applSrvName.setStatus("current")
_ApplSrvInstToRunApplElmtTable_Object = MibTable
applSrvInstToRunApplElmtTable = _ApplSrvInstToRunApplElmtTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 1, 3)
)
if mibBuilder.loadTexts:
    applSrvInstToRunApplElmtTable.setStatus("current")
_ApplSrvInstToRunApplElmtEntry_Object = MibTableRow
applSrvInstToRunApplElmtEntry = _ApplSrvInstToRunApplElmtEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 1, 3, 1)
)
applSrvInstToRunApplElmtEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applSrvIndex"),
    (0, "SYSAPPL-MIB", "sysApplElmtRunIndex"),
)
if mibBuilder.loadTexts:
    applSrvInstToRunApplElmtEntry.setStatus("current")


class _ApplSrvIndex_Type(Unsigned32):
    """Custom type applSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApplSrvIndex_Type.__name__ = "Unsigned32"
_ApplSrvIndex_Object = MibTableColumn
applSrvIndex = _ApplSrvIndex_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 1, 3, 1, 1),
    _ApplSrvIndex_Type()
)
applSrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applSrvIndex.setStatus("current")
_ApplRunApplElmtToSrvInstTable_Object = MibTable
applRunApplElmtToSrvInstTable = _ApplRunApplElmtToSrvInstTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 1, 4)
)
if mibBuilder.loadTexts:
    applRunApplElmtToSrvInstTable.setStatus("current")
_ApplRunApplElmtToSrvInstEntry_Object = MibTableRow
applRunApplElmtToSrvInstEntry = _ApplRunApplElmtToSrvInstEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 1, 4, 1)
)
applRunApplElmtToSrvInstEntry.setIndexNames(
    (0, "SYSAPPL-MIB", "sysApplElmtRunIndex"),
    (0, "APPLICATION-MIB", "applSrvInstance"),
)
if mibBuilder.loadTexts:
    applRunApplElmtToSrvInstEntry.setStatus("current")


class _ApplSrvInstance_Type(Unsigned32):
    """Custom type applSrvInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApplSrvInstance_Type.__name__ = "Unsigned32"
_ApplSrvInstance_Object = MibTableColumn
applSrvInstance = _ApplSrvInstance_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 1, 4, 1, 1),
    _ApplSrvInstance_Type()
)
applSrvInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applSrvInstance.setStatus("current")
_ApplChannelGroup_ObjectIdentity = ObjectIdentity
applChannelGroup = _ApplChannelGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 62, 1, 2)
)
_ApplOpenChannelTable_Object = MibTable
applOpenChannelTable = _ApplOpenChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1)
)
if mibBuilder.loadTexts:
    applOpenChannelTable.setStatus("current")
_ApplOpenChannelEntry_Object = MibTableRow
applOpenChannelEntry = _ApplOpenChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1)
)
applOpenChannelEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
    (0, "APPLICATION-MIB", "applOpenChannelIndex"),
)
if mibBuilder.loadTexts:
    applOpenChannelEntry.setStatus("current")


class _ApplElmtOrSvc_Type(Integer32):
    """Custom type applElmtOrSvc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("element", 2),
          ("service", 1))
    )


_ApplElmtOrSvc_Type.__name__ = "Integer32"
_ApplElmtOrSvc_Object = MibTableColumn
applElmtOrSvc = _ApplElmtOrSvc_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 1),
    _ApplElmtOrSvc_Type()
)
applElmtOrSvc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    applElmtOrSvc.setStatus("current")


class _ApplElmtOrSvcId_Type(Unsigned32):
    """Custom type applElmtOrSvcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApplElmtOrSvcId_Type.__name__ = "Unsigned32"
_ApplElmtOrSvcId_Object = MibTableColumn
applElmtOrSvcId = _ApplElmtOrSvcId_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 2),
    _ApplElmtOrSvcId_Type()
)
applElmtOrSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    applElmtOrSvcId.setStatus("current")
_ApplOpenChannelIndex_Type = Unsigned32
_ApplOpenChannelIndex_Object = MibTableColumn
applOpenChannelIndex = _ApplOpenChannelIndex_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 3),
    _ApplOpenChannelIndex_Type()
)
applOpenChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    applOpenChannelIndex.setStatus("current")
_ApplOpenChannelOpenTime_Type = TimeStamp
_ApplOpenChannelOpenTime_Object = MibTableColumn
applOpenChannelOpenTime = _ApplOpenChannelOpenTime_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 4),
    _ApplOpenChannelOpenTime_Type()
)
applOpenChannelOpenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelOpenTime.setStatus("current")
_ApplOpenChannelReadRequests_Type = Counter64
_ApplOpenChannelReadRequests_Object = MibTableColumn
applOpenChannelReadRequests = _ApplOpenChannelReadRequests_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 5),
    _ApplOpenChannelReadRequests_Type()
)
applOpenChannelReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelReadRequests.setStatus("current")
if mibBuilder.loadTexts:
    applOpenChannelReadRequests.setUnits("read requests")
_ApplOpenChannelReadRequestsLow_Type = Counter32
_ApplOpenChannelReadRequestsLow_Object = MibTableColumn
applOpenChannelReadRequestsLow = _ApplOpenChannelReadRequestsLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 6),
    _ApplOpenChannelReadRequestsLow_Type()
)
applOpenChannelReadRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelReadRequestsLow.setStatus("current")
if mibBuilder.loadTexts:
    applOpenChannelReadRequestsLow.setUnits("read requests")
_ApplOpenChannelReadFailures_Type = Counter32
_ApplOpenChannelReadFailures_Object = MibTableColumn
applOpenChannelReadFailures = _ApplOpenChannelReadFailures_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 7),
    _ApplOpenChannelReadFailures_Type()
)
applOpenChannelReadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelReadFailures.setStatus("current")
if mibBuilder.loadTexts:
    applOpenChannelReadFailures.setUnits("failed read requests")
_ApplOpenChannelBytesRead_Type = Counter64
_ApplOpenChannelBytesRead_Object = MibTableColumn
applOpenChannelBytesRead = _ApplOpenChannelBytesRead_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 8),
    _ApplOpenChannelBytesRead_Type()
)
applOpenChannelBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelBytesRead.setStatus("current")
if mibBuilder.loadTexts:
    applOpenChannelBytesRead.setUnits("bytes")
_ApplOpenChannelBytesReadLow_Type = Counter32
_ApplOpenChannelBytesReadLow_Object = MibTableColumn
applOpenChannelBytesReadLow = _ApplOpenChannelBytesReadLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 9),
    _ApplOpenChannelBytesReadLow_Type()
)
applOpenChannelBytesReadLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelBytesReadLow.setStatus("current")
if mibBuilder.loadTexts:
    applOpenChannelBytesReadLow.setUnits("bytes")


class _ApplOpenChannelLastReadTime_Type(DateAndTime):
    """Custom type applOpenChannelLastReadTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_ApplOpenChannelLastReadTime_Object = MibTableColumn
applOpenChannelLastReadTime = _ApplOpenChannelLastReadTime_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 10),
    _ApplOpenChannelLastReadTime_Type()
)
applOpenChannelLastReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelLastReadTime.setStatus("current")
_ApplOpenChannelWriteRequests_Type = Counter64
_ApplOpenChannelWriteRequests_Object = MibTableColumn
applOpenChannelWriteRequests = _ApplOpenChannelWriteRequests_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 11),
    _ApplOpenChannelWriteRequests_Type()
)
applOpenChannelWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelWriteRequests.setStatus("current")
if mibBuilder.loadTexts:
    applOpenChannelWriteRequests.setUnits("write requests")
_ApplOpenChannelWriteRequestsLow_Type = Counter32
_ApplOpenChannelWriteRequestsLow_Object = MibTableColumn
applOpenChannelWriteRequestsLow = _ApplOpenChannelWriteRequestsLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 12),
    _ApplOpenChannelWriteRequestsLow_Type()
)
applOpenChannelWriteRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelWriteRequestsLow.setStatus("current")
if mibBuilder.loadTexts:
    applOpenChannelWriteRequestsLow.setUnits("write requests")
_ApplOpenChannelWriteFailures_Type = Counter32
_ApplOpenChannelWriteFailures_Object = MibTableColumn
applOpenChannelWriteFailures = _ApplOpenChannelWriteFailures_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 13),
    _ApplOpenChannelWriteFailures_Type()
)
applOpenChannelWriteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelWriteFailures.setStatus("current")
if mibBuilder.loadTexts:
    applOpenChannelWriteFailures.setUnits("failed write requests")
_ApplOpenChannelBytesWritten_Type = Counter64
_ApplOpenChannelBytesWritten_Object = MibTableColumn
applOpenChannelBytesWritten = _ApplOpenChannelBytesWritten_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 14),
    _ApplOpenChannelBytesWritten_Type()
)
applOpenChannelBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelBytesWritten.setStatus("current")
if mibBuilder.loadTexts:
    applOpenChannelBytesWritten.setUnits("bytes")
_ApplOpenChannelBytesWrittenLow_Type = Counter32
_ApplOpenChannelBytesWrittenLow_Object = MibTableColumn
applOpenChannelBytesWrittenLow = _ApplOpenChannelBytesWrittenLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 15),
    _ApplOpenChannelBytesWrittenLow_Type()
)
applOpenChannelBytesWrittenLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelBytesWrittenLow.setStatus("current")
if mibBuilder.loadTexts:
    applOpenChannelBytesWrittenLow.setUnits("bytes")


class _ApplOpenChannelLastWriteTime_Type(DateAndTime):
    """Custom type applOpenChannelLastWriteTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_ApplOpenChannelLastWriteTime_Object = MibTableColumn
applOpenChannelLastWriteTime = _ApplOpenChannelLastWriteTime_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 1, 1, 16),
    _ApplOpenChannelLastWriteTime_Type()
)
applOpenChannelLastWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenChannelLastWriteTime.setStatus("current")
_ApplOpenFileTable_Object = MibTable
applOpenFileTable = _ApplOpenFileTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 2)
)
if mibBuilder.loadTexts:
    applOpenFileTable.setStatus("current")
_ApplOpenFileEntry_Object = MibTableRow
applOpenFileEntry = _ApplOpenFileEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 2, 1)
)
applOpenFileEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
    (0, "APPLICATION-MIB", "applOpenChannelIndex"),
)
if mibBuilder.loadTexts:
    applOpenFileEntry.setStatus("current")
_ApplOpenFileName_Type = LongUtf8String
_ApplOpenFileName_Object = MibTableColumn
applOpenFileName = _ApplOpenFileName_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 2, 1, 1),
    _ApplOpenFileName_Type()
)
applOpenFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenFileName.setStatus("current")
_ApplOpenFileSizeHigh_Type = Unsigned32
_ApplOpenFileSizeHigh_Object = MibTableColumn
applOpenFileSizeHigh = _ApplOpenFileSizeHigh_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 2, 1, 2),
    _ApplOpenFileSizeHigh_Type()
)
applOpenFileSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenFileSizeHigh.setStatus("current")
if mibBuilder.loadTexts:
    applOpenFileSizeHigh.setUnits("2^32 byte blocks")
_ApplOpenFileSizeLow_Type = Unsigned32
_ApplOpenFileSizeLow_Object = MibTableColumn
applOpenFileSizeLow = _ApplOpenFileSizeLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 2, 1, 3),
    _ApplOpenFileSizeLow_Type()
)
applOpenFileSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenFileSizeLow.setStatus("current")
if mibBuilder.loadTexts:
    applOpenFileSizeLow.setUnits("bytes")


class _ApplOpenFileMode_Type(Integer32):
    """Custom type applOpenFileMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("readWrite", 3),
          ("write", 2))
    )


_ApplOpenFileMode_Type.__name__ = "Integer32"
_ApplOpenFileMode_Object = MibTableColumn
applOpenFileMode = _ApplOpenFileMode_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 2, 1, 4),
    _ApplOpenFileMode_Type()
)
applOpenFileMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenFileMode.setStatus("current")
_ApplOpenConnectionTable_Object = MibTable
applOpenConnectionTable = _ApplOpenConnectionTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 3)
)
if mibBuilder.loadTexts:
    applOpenConnectionTable.setStatus("current")
_ApplOpenConnectionEntry_Object = MibTableRow
applOpenConnectionEntry = _ApplOpenConnectionEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 3, 1)
)
applOpenConnectionEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
    (0, "APPLICATION-MIB", "applOpenChannelIndex"),
)
if mibBuilder.loadTexts:
    applOpenConnectionEntry.setStatus("current")


class _ApplOpenConnectionTransport_Type(TDomain):
    """Custom type applOpenConnectionTransport based on TDomain"""
    defaultValue = (0, 0)


_ApplOpenConnectionTransport_Object = MibTableColumn
applOpenConnectionTransport = _ApplOpenConnectionTransport_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 3, 1, 1),
    _ApplOpenConnectionTransport_Type()
)
applOpenConnectionTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenConnectionTransport.setStatus("current")
_ApplOpenConnectionNearEndAddr_Type = ApplTAddress
_ApplOpenConnectionNearEndAddr_Object = MibTableColumn
applOpenConnectionNearEndAddr = _ApplOpenConnectionNearEndAddr_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 3, 1, 2),
    _ApplOpenConnectionNearEndAddr_Type()
)
applOpenConnectionNearEndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenConnectionNearEndAddr.setStatus("current")
_ApplOpenConnectionNearEndpoint_Type = SnmpAdminString
_ApplOpenConnectionNearEndpoint_Object = MibTableColumn
applOpenConnectionNearEndpoint = _ApplOpenConnectionNearEndpoint_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 3, 1, 3),
    _ApplOpenConnectionNearEndpoint_Type()
)
applOpenConnectionNearEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenConnectionNearEndpoint.setStatus("current")
_ApplOpenConnectionFarEndAddr_Type = ApplTAddress
_ApplOpenConnectionFarEndAddr_Object = MibTableColumn
applOpenConnectionFarEndAddr = _ApplOpenConnectionFarEndAddr_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 3, 1, 4),
    _ApplOpenConnectionFarEndAddr_Type()
)
applOpenConnectionFarEndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenConnectionFarEndAddr.setStatus("current")
_ApplOpenConnectionFarEndpoint_Type = SnmpAdminString
_ApplOpenConnectionFarEndpoint_Object = MibTableColumn
applOpenConnectionFarEndpoint = _ApplOpenConnectionFarEndpoint_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 3, 1, 5),
    _ApplOpenConnectionFarEndpoint_Type()
)
applOpenConnectionFarEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenConnectionFarEndpoint.setStatus("current")
_ApplOpenConnectionApplication_Type = SnmpAdminString
_ApplOpenConnectionApplication_Object = MibTableColumn
applOpenConnectionApplication = _ApplOpenConnectionApplication_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 3, 1, 6),
    _ApplOpenConnectionApplication_Type()
)
applOpenConnectionApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOpenConnectionApplication.setStatus("current")
_ApplTransactionStreamTable_Object = MibTable
applTransactionStreamTable = _ApplTransactionStreamTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 4)
)
if mibBuilder.loadTexts:
    applTransactionStreamTable.setStatus("current")
_ApplTransactionStreamEntry_Object = MibTableRow
applTransactionStreamEntry = _ApplTransactionStreamEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 4, 1)
)
applTransactionStreamEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
    (0, "APPLICATION-MIB", "applOpenChannelIndex"),
)
if mibBuilder.loadTexts:
    applTransactionStreamEntry.setStatus("current")
_ApplTransactStreamDescr_Type = SnmpAdminString
_ApplTransactStreamDescr_Object = MibTableColumn
applTransactStreamDescr = _ApplTransactStreamDescr_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 4, 1, 1),
    _ApplTransactStreamDescr_Type()
)
applTransactStreamDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactStreamDescr.setStatus("current")
_ApplTransactStreamUnitOfWork_Type = SnmpAdminString
_ApplTransactStreamUnitOfWork_Object = MibTableColumn
applTransactStreamUnitOfWork = _ApplTransactStreamUnitOfWork_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 4, 1, 2),
    _ApplTransactStreamUnitOfWork_Type()
)
applTransactStreamUnitOfWork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactStreamUnitOfWork.setStatus("current")
_ApplTransactStreamInvokes_Type = Counter64
_ApplTransactStreamInvokes_Object = MibTableColumn
applTransactStreamInvokes = _ApplTransactStreamInvokes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 4, 1, 3),
    _ApplTransactStreamInvokes_Type()
)
applTransactStreamInvokes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactStreamInvokes.setStatus("current")
if mibBuilder.loadTexts:
    applTransactStreamInvokes.setUnits("transactions")
_ApplTransactStreamInvokesLow_Type = Counter32
_ApplTransactStreamInvokesLow_Object = MibTableColumn
applTransactStreamInvokesLow = _ApplTransactStreamInvokesLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 4, 1, 4),
    _ApplTransactStreamInvokesLow_Type()
)
applTransactStreamInvokesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactStreamInvokesLow.setStatus("current")
if mibBuilder.loadTexts:
    applTransactStreamInvokesLow.setUnits("transactions")
_ApplTransactStreamInvCumTimes_Type = Counter32
_ApplTransactStreamInvCumTimes_Object = MibTableColumn
applTransactStreamInvCumTimes = _ApplTransactStreamInvCumTimes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 4, 1, 5),
    _ApplTransactStreamInvCumTimes_Type()
)
applTransactStreamInvCumTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactStreamInvCumTimes.setStatus("current")
if mibBuilder.loadTexts:
    applTransactStreamInvCumTimes.setUnits("milliseconds")
_ApplTransactStreamInvRspTimes_Type = Counter32
_ApplTransactStreamInvRspTimes_Object = MibTableColumn
applTransactStreamInvRspTimes = _ApplTransactStreamInvRspTimes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 4, 1, 6),
    _ApplTransactStreamInvRspTimes_Type()
)
applTransactStreamInvRspTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactStreamInvRspTimes.setStatus("current")
if mibBuilder.loadTexts:
    applTransactStreamInvRspTimes.setUnits("milliseconds")
_ApplTransactStreamPerforms_Type = Counter64
_ApplTransactStreamPerforms_Object = MibTableColumn
applTransactStreamPerforms = _ApplTransactStreamPerforms_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 4, 1, 7),
    _ApplTransactStreamPerforms_Type()
)
applTransactStreamPerforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactStreamPerforms.setStatus("current")
if mibBuilder.loadTexts:
    applTransactStreamPerforms.setUnits("transactions")
_ApplTransactStreamPerformsLow_Type = Counter32
_ApplTransactStreamPerformsLow_Object = MibTableColumn
applTransactStreamPerformsLow = _ApplTransactStreamPerformsLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 4, 1, 8),
    _ApplTransactStreamPerformsLow_Type()
)
applTransactStreamPerformsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactStreamPerformsLow.setStatus("current")
if mibBuilder.loadTexts:
    applTransactStreamPerformsLow.setUnits("transactions")
_ApplTransactStreamPrfCumTimes_Type = Counter32
_ApplTransactStreamPrfCumTimes_Object = MibTableColumn
applTransactStreamPrfCumTimes = _ApplTransactStreamPrfCumTimes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 4, 1, 9),
    _ApplTransactStreamPrfCumTimes_Type()
)
applTransactStreamPrfCumTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactStreamPrfCumTimes.setStatus("current")
if mibBuilder.loadTexts:
    applTransactStreamPrfCumTimes.setUnits("milliseconds")
_ApplTransactStreamPrfRspTimes_Type = Counter32
_ApplTransactStreamPrfRspTimes_Object = MibTableColumn
applTransactStreamPrfRspTimes = _ApplTransactStreamPrfRspTimes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 4, 1, 10),
    _ApplTransactStreamPrfRspTimes_Type()
)
applTransactStreamPrfRspTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactStreamPrfRspTimes.setStatus("current")
if mibBuilder.loadTexts:
    applTransactStreamPrfRspTimes.setUnits("milliseconds")
_ApplTransactFlowTable_Object = MibTable
applTransactFlowTable = _ApplTransactFlowTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 5)
)
if mibBuilder.loadTexts:
    applTransactFlowTable.setStatus("current")
_ApplTransactFlowEntry_Object = MibTableRow
applTransactFlowEntry = _ApplTransactFlowEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 5, 1)
)
applTransactFlowEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
    (0, "APPLICATION-MIB", "applOpenChannelIndex"),
    (0, "APPLICATION-MIB", "applTransactFlowDirection"),
    (0, "APPLICATION-MIB", "applTransactFlowReqRsp"),
)
if mibBuilder.loadTexts:
    applTransactFlowEntry.setStatus("current")


class _ApplTransactFlowDirection_Type(Integer32):
    """Custom type applTransactFlowDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 2),
          ("transmit", 1))
    )


_ApplTransactFlowDirection_Type.__name__ = "Integer32"
_ApplTransactFlowDirection_Object = MibTableColumn
applTransactFlowDirection = _ApplTransactFlowDirection_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 5, 1, 1),
    _ApplTransactFlowDirection_Type()
)
applTransactFlowDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    applTransactFlowDirection.setStatus("current")


class _ApplTransactFlowReqRsp_Type(Integer32):
    """Custom type applTransactFlowReqRsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("request", 1),
          ("response", 2))
    )


_ApplTransactFlowReqRsp_Type.__name__ = "Integer32"
_ApplTransactFlowReqRsp_Object = MibTableColumn
applTransactFlowReqRsp = _ApplTransactFlowReqRsp_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 5, 1, 2),
    _ApplTransactFlowReqRsp_Type()
)
applTransactFlowReqRsp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    applTransactFlowReqRsp.setStatus("current")
_ApplTransactFlowTrans_Type = Counter64
_ApplTransactFlowTrans_Object = MibTableColumn
applTransactFlowTrans = _ApplTransactFlowTrans_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 5, 1, 3),
    _ApplTransactFlowTrans_Type()
)
applTransactFlowTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactFlowTrans.setStatus("current")
if mibBuilder.loadTexts:
    applTransactFlowTrans.setUnits("transactions")
_ApplTransactFlowTransLow_Type = Counter32
_ApplTransactFlowTransLow_Object = MibTableColumn
applTransactFlowTransLow = _ApplTransactFlowTransLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 5, 1, 4),
    _ApplTransactFlowTransLow_Type()
)
applTransactFlowTransLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactFlowTransLow.setStatus("current")
if mibBuilder.loadTexts:
    applTransactFlowTransLow.setUnits("transactions")
_ApplTransactFlowBytes_Type = Counter64
_ApplTransactFlowBytes_Object = MibTableColumn
applTransactFlowBytes = _ApplTransactFlowBytes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 5, 1, 5),
    _ApplTransactFlowBytes_Type()
)
applTransactFlowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactFlowBytes.setStatus("current")
if mibBuilder.loadTexts:
    applTransactFlowBytes.setUnits("bytes")
_ApplTransactFlowBytesLow_Type = Counter32
_ApplTransactFlowBytesLow_Object = MibTableColumn
applTransactFlowBytesLow = _ApplTransactFlowBytesLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 5, 1, 6),
    _ApplTransactFlowBytesLow_Type()
)
applTransactFlowBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactFlowBytesLow.setStatus("current")
if mibBuilder.loadTexts:
    applTransactFlowBytesLow.setUnits("bytes")


class _ApplTransactFlowTime_Type(DateAndTime):
    """Custom type applTransactFlowTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_ApplTransactFlowTime_Object = MibTableColumn
applTransactFlowTime = _ApplTransactFlowTime_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 5, 1, 7),
    _ApplTransactFlowTime_Type()
)
applTransactFlowTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactFlowTime.setStatus("current")
_ApplTransactKindTable_Object = MibTable
applTransactKindTable = _ApplTransactKindTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 6)
)
if mibBuilder.loadTexts:
    applTransactKindTable.setStatus("current")
_ApplTransactKindEntry_Object = MibTableRow
applTransactKindEntry = _ApplTransactKindEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 6, 1)
)
applTransactKindEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
    (0, "APPLICATION-MIB", "applOpenChannelIndex"),
    (0, "APPLICATION-MIB", "applTransactFlowDirection"),
    (0, "APPLICATION-MIB", "applTransactFlowReqRsp"),
    (0, "APPLICATION-MIB", "applTransactKind"),
)
if mibBuilder.loadTexts:
    applTransactKindEntry.setStatus("current")


class _ApplTransactKind_Type(SnmpAdminString):
    """Custom type applTransactKind based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApplTransactKind_Type.__name__ = "SnmpAdminString"
_ApplTransactKind_Object = MibTableColumn
applTransactKind = _ApplTransactKind_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 6, 1, 1),
    _ApplTransactKind_Type()
)
applTransactKind.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    applTransactKind.setStatus("current")
_ApplTransactKindTrans_Type = Counter64
_ApplTransactKindTrans_Object = MibTableColumn
applTransactKindTrans = _ApplTransactKindTrans_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 6, 1, 2),
    _ApplTransactKindTrans_Type()
)
applTransactKindTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactKindTrans.setStatus("current")
if mibBuilder.loadTexts:
    applTransactKindTrans.setUnits("transactions")
_ApplTransactKindTransLow_Type = Counter32
_ApplTransactKindTransLow_Object = MibTableColumn
applTransactKindTransLow = _ApplTransactKindTransLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 6, 1, 3),
    _ApplTransactKindTransLow_Type()
)
applTransactKindTransLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactKindTransLow.setStatus("current")
if mibBuilder.loadTexts:
    applTransactKindTransLow.setUnits("transactions")
_ApplTransactKindBytes_Type = Counter64
_ApplTransactKindBytes_Object = MibTableColumn
applTransactKindBytes = _ApplTransactKindBytes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 6, 1, 4),
    _ApplTransactKindBytes_Type()
)
applTransactKindBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactKindBytes.setStatus("current")
if mibBuilder.loadTexts:
    applTransactKindBytes.setUnits("bytes")
_ApplTransactKindBytesLow_Type = Counter32
_ApplTransactKindBytesLow_Object = MibTableColumn
applTransactKindBytesLow = _ApplTransactKindBytesLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 6, 1, 5),
    _ApplTransactKindBytesLow_Type()
)
applTransactKindBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactKindBytesLow.setStatus("current")
if mibBuilder.loadTexts:
    applTransactKindBytesLow.setUnits("bytes")


class _ApplTransactKindTime_Type(DateAndTime):
    """Custom type applTransactKindTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_ApplTransactKindTime_Object = MibTableColumn
applTransactKindTime = _ApplTransactKindTime_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 2, 6, 1, 6),
    _ApplTransactKindTime_Type()
)
applTransactKindTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTransactKindTime.setStatus("current")
_ApplPastChannelGroup_ObjectIdentity = ObjectIdentity
applPastChannelGroup = _ApplPastChannelGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 62, 1, 3)
)
_ApplPastChannelControlTable_Object = MibTable
applPastChannelControlTable = _ApplPastChannelControlTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 1)
)
if mibBuilder.loadTexts:
    applPastChannelControlTable.setStatus("current")
_ApplPastChannelControlEntry_Object = MibTableRow
applPastChannelControlEntry = _ApplPastChannelControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 1, 1)
)
applPastChannelControlEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
)
if mibBuilder.loadTexts:
    applPastChannelControlEntry.setStatus("current")


class _ApplPastChannelControlCollect_Type(Integer32):
    """Custom type applPastChannelControlCollect based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 1),
          ("frozen", 2))
    )


_ApplPastChannelControlCollect_Type.__name__ = "Integer32"
_ApplPastChannelControlCollect_Object = MibTableColumn
applPastChannelControlCollect = _ApplPastChannelControlCollect_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 1, 1, 1),
    _ApplPastChannelControlCollect_Type()
)
applPastChannelControlCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applPastChannelControlCollect.setStatus("current")


class _ApplPastChannelControlMaxRows_Type(Unsigned32):
    """Custom type applPastChannelControlMaxRows based on Unsigned32"""
    defaultValue = 500


_ApplPastChannelControlMaxRows_Object = MibTableColumn
applPastChannelControlMaxRows = _ApplPastChannelControlMaxRows_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 1, 1, 2),
    _ApplPastChannelControlMaxRows_Type()
)
applPastChannelControlMaxRows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applPastChannelControlMaxRows.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelControlMaxRows.setUnits("channel history entries")


class _ApplPastChannelControlTimeLimit_Type(Unsigned32):
    """Custom type applPastChannelControlTimeLimit based on Unsigned32"""
    defaultValue = 7200


_ApplPastChannelControlTimeLimit_Object = MibTableColumn
applPastChannelControlTimeLimit = _ApplPastChannelControlTimeLimit_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 1, 1, 3),
    _ApplPastChannelControlTimeLimit_Type()
)
applPastChannelControlTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applPastChannelControlTimeLimit.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelControlTimeLimit.setUnits("seconds")
_ApplPastChannelControlRemItems_Type = Counter32
_ApplPastChannelControlRemItems_Object = MibTableColumn
applPastChannelControlRemItems = _ApplPastChannelControlRemItems_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 1, 1, 4),
    _ApplPastChannelControlRemItems_Type()
)
applPastChannelControlRemItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelControlRemItems.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelControlRemItems.setUnits("channel history entries")
_ApplPastChannelTable_Object = MibTable
applPastChannelTable = _ApplPastChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2)
)
if mibBuilder.loadTexts:
    applPastChannelTable.setStatus("current")
_ApplPastChannelEntry_Object = MibTableRow
applPastChannelEntry = _ApplPastChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1)
)
applPastChannelEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
    (0, "APPLICATION-MIB", "applPastChannelIndex"),
)
if mibBuilder.loadTexts:
    applPastChannelEntry.setStatus("current")


class _ApplPastChannelIndex_Type(Unsigned32):
    """Custom type applPastChannelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApplPastChannelIndex_Type.__name__ = "Unsigned32"
_ApplPastChannelIndex_Object = MibTableColumn
applPastChannelIndex = _ApplPastChannelIndex_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 1),
    _ApplPastChannelIndex_Type()
)
applPastChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    applPastChannelIndex.setStatus("current")
_ApplPastChannelOpenTime_Type = DateAndTime
_ApplPastChannelOpenTime_Object = MibTableColumn
applPastChannelOpenTime = _ApplPastChannelOpenTime_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 2),
    _ApplPastChannelOpenTime_Type()
)
applPastChannelOpenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelOpenTime.setStatus("current")
_ApplPastChannelCloseTime_Type = DateAndTime
_ApplPastChannelCloseTime_Object = MibTableColumn
applPastChannelCloseTime = _ApplPastChannelCloseTime_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 3),
    _ApplPastChannelCloseTime_Type()
)
applPastChannelCloseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelCloseTime.setStatus("current")
_ApplPastChannelReadRequests_Type = Unsigned64TC
_ApplPastChannelReadRequests_Object = MibTableColumn
applPastChannelReadRequests = _ApplPastChannelReadRequests_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 4),
    _ApplPastChannelReadRequests_Type()
)
applPastChannelReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelReadRequests.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelReadRequests.setUnits("read requests")
_ApplPastChannelReadReqsLow_Type = Unsigned32
_ApplPastChannelReadReqsLow_Object = MibTableColumn
applPastChannelReadReqsLow = _ApplPastChannelReadReqsLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 5),
    _ApplPastChannelReadReqsLow_Type()
)
applPastChannelReadReqsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelReadReqsLow.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelReadReqsLow.setUnits("read requests")
_ApplPastChannelReadFailures_Type = Unsigned32
_ApplPastChannelReadFailures_Object = MibTableColumn
applPastChannelReadFailures = _ApplPastChannelReadFailures_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 6),
    _ApplPastChannelReadFailures_Type()
)
applPastChannelReadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelReadFailures.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelReadFailures.setUnits("failed read requests")
_ApplPastChannelBytesRead_Type = Unsigned64TC
_ApplPastChannelBytesRead_Object = MibTableColumn
applPastChannelBytesRead = _ApplPastChannelBytesRead_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 7),
    _ApplPastChannelBytesRead_Type()
)
applPastChannelBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelBytesRead.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelBytesRead.setUnits("bytes")
_ApplPastChannelBytesReadLow_Type = Unsigned32
_ApplPastChannelBytesReadLow_Object = MibTableColumn
applPastChannelBytesReadLow = _ApplPastChannelBytesReadLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 8),
    _ApplPastChannelBytesReadLow_Type()
)
applPastChannelBytesReadLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelBytesReadLow.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelBytesReadLow.setUnits("bytes")


class _ApplPastChannelLastReadTime_Type(DateAndTime):
    """Custom type applPastChannelLastReadTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_ApplPastChannelLastReadTime_Object = MibTableColumn
applPastChannelLastReadTime = _ApplPastChannelLastReadTime_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 9),
    _ApplPastChannelLastReadTime_Type()
)
applPastChannelLastReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelLastReadTime.setStatus("current")
_ApplPastChannelWriteRequests_Type = Unsigned64TC
_ApplPastChannelWriteRequests_Object = MibTableColumn
applPastChannelWriteRequests = _ApplPastChannelWriteRequests_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 10),
    _ApplPastChannelWriteRequests_Type()
)
applPastChannelWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelWriteRequests.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelWriteRequests.setUnits("write requests")
_ApplPastChannelWriteReqsLow_Type = Unsigned32
_ApplPastChannelWriteReqsLow_Object = MibTableColumn
applPastChannelWriteReqsLow = _ApplPastChannelWriteReqsLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 11),
    _ApplPastChannelWriteReqsLow_Type()
)
applPastChannelWriteReqsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelWriteReqsLow.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelWriteReqsLow.setUnits("write requests")
_ApplPastChannelWriteFailures_Type = Unsigned32
_ApplPastChannelWriteFailures_Object = MibTableColumn
applPastChannelWriteFailures = _ApplPastChannelWriteFailures_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 12),
    _ApplPastChannelWriteFailures_Type()
)
applPastChannelWriteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelWriteFailures.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelWriteFailures.setUnits("failed write requests")
_ApplPastChannelBytesWritten_Type = Unsigned64TC
_ApplPastChannelBytesWritten_Object = MibTableColumn
applPastChannelBytesWritten = _ApplPastChannelBytesWritten_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 13),
    _ApplPastChannelBytesWritten_Type()
)
applPastChannelBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelBytesWritten.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelBytesWritten.setUnits("bytes")
_ApplPastChannelBytesWritLow_Type = Unsigned32
_ApplPastChannelBytesWritLow_Object = MibTableColumn
applPastChannelBytesWritLow = _ApplPastChannelBytesWritLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 14),
    _ApplPastChannelBytesWritLow_Type()
)
applPastChannelBytesWritLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelBytesWritLow.setStatus("current")
if mibBuilder.loadTexts:
    applPastChannelBytesWritLow.setUnits("bytes")


class _ApplPastChannelLastWriteTime_Type(DateAndTime):
    """Custom type applPastChannelLastWriteTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_ApplPastChannelLastWriteTime_Object = MibTableColumn
applPastChannelLastWriteTime = _ApplPastChannelLastWriteTime_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 2, 1, 15),
    _ApplPastChannelLastWriteTime_Type()
)
applPastChannelLastWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastChannelLastWriteTime.setStatus("current")
_ApplPastFileTable_Object = MibTable
applPastFileTable = _ApplPastFileTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 3)
)
if mibBuilder.loadTexts:
    applPastFileTable.setStatus("current")
_ApplPastFileEntry_Object = MibTableRow
applPastFileEntry = _ApplPastFileEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 3, 1)
)
applPastFileEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
    (0, "APPLICATION-MIB", "applPastChannelIndex"),
)
if mibBuilder.loadTexts:
    applPastFileEntry.setStatus("current")
_ApplPastFileName_Type = LongUtf8String
_ApplPastFileName_Object = MibTableColumn
applPastFileName = _ApplPastFileName_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 3, 1, 1),
    _ApplPastFileName_Type()
)
applPastFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastFileName.setStatus("current")
_ApplPastFileSizeHigh_Type = Unsigned32
_ApplPastFileSizeHigh_Object = MibTableColumn
applPastFileSizeHigh = _ApplPastFileSizeHigh_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 3, 1, 2),
    _ApplPastFileSizeHigh_Type()
)
applPastFileSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastFileSizeHigh.setStatus("current")
if mibBuilder.loadTexts:
    applPastFileSizeHigh.setUnits("2^32 byte blocks")
_ApplPastFileSizeLow_Type = Unsigned32
_ApplPastFileSizeLow_Object = MibTableColumn
applPastFileSizeLow = _ApplPastFileSizeLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 3, 1, 3),
    _ApplPastFileSizeLow_Type()
)
applPastFileSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastFileSizeLow.setStatus("current")
if mibBuilder.loadTexts:
    applPastFileSizeLow.setUnits("bytes")


class _ApplPastFileMode_Type(Integer32):
    """Custom type applPastFileMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("readWrite", 3),
          ("write", 2))
    )


_ApplPastFileMode_Type.__name__ = "Integer32"
_ApplPastFileMode_Object = MibTableColumn
applPastFileMode = _ApplPastFileMode_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 3, 1, 4),
    _ApplPastFileMode_Type()
)
applPastFileMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastFileMode.setStatus("current")
_ApplPastConTable_Object = MibTable
applPastConTable = _ApplPastConTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 4)
)
if mibBuilder.loadTexts:
    applPastConTable.setStatus("current")
_ApplPastConEntry_Object = MibTableRow
applPastConEntry = _ApplPastConEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 4, 1)
)
applPastConEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
    (0, "APPLICATION-MIB", "applPastChannelIndex"),
)
if mibBuilder.loadTexts:
    applPastConEntry.setStatus("current")


class _ApplPastConTransport_Type(TDomain):
    """Custom type applPastConTransport based on TDomain"""
    defaultValue = (0, 0)


_ApplPastConTransport_Object = MibTableColumn
applPastConTransport = _ApplPastConTransport_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 4, 1, 1),
    _ApplPastConTransport_Type()
)
applPastConTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastConTransport.setStatus("current")
_ApplPastConNearEndAddr_Type = ApplTAddress
_ApplPastConNearEndAddr_Object = MibTableColumn
applPastConNearEndAddr = _ApplPastConNearEndAddr_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 4, 1, 2),
    _ApplPastConNearEndAddr_Type()
)
applPastConNearEndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastConNearEndAddr.setStatus("current")
_ApplPastConNearEndpoint_Type = SnmpAdminString
_ApplPastConNearEndpoint_Object = MibTableColumn
applPastConNearEndpoint = _ApplPastConNearEndpoint_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 4, 1, 3),
    _ApplPastConNearEndpoint_Type()
)
applPastConNearEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastConNearEndpoint.setStatus("current")
_ApplPastConFarEndAddr_Type = ApplTAddress
_ApplPastConFarEndAddr_Object = MibTableColumn
applPastConFarEndAddr = _ApplPastConFarEndAddr_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 4, 1, 4),
    _ApplPastConFarEndAddr_Type()
)
applPastConFarEndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastConFarEndAddr.setStatus("current")
_ApplPastConFarEndpoint_Type = SnmpAdminString
_ApplPastConFarEndpoint_Object = MibTableColumn
applPastConFarEndpoint = _ApplPastConFarEndpoint_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 4, 1, 5),
    _ApplPastConFarEndpoint_Type()
)
applPastConFarEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastConFarEndpoint.setStatus("current")
_ApplPastConApplication_Type = SnmpAdminString
_ApplPastConApplication_Object = MibTableColumn
applPastConApplication = _ApplPastConApplication_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 4, 1, 6),
    _ApplPastConApplication_Type()
)
applPastConApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastConApplication.setStatus("current")
_ApplPastTransStreamTable_Object = MibTable
applPastTransStreamTable = _ApplPastTransStreamTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 5)
)
if mibBuilder.loadTexts:
    applPastTransStreamTable.setStatus("current")
_ApplPastTransStreamEntry_Object = MibTableRow
applPastTransStreamEntry = _ApplPastTransStreamEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 5, 1)
)
applPastTransStreamEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
    (0, "APPLICATION-MIB", "applPastChannelIndex"),
)
if mibBuilder.loadTexts:
    applPastTransStreamEntry.setStatus("current")
_ApplPastTransStreamDescr_Type = SnmpAdminString
_ApplPastTransStreamDescr_Object = MibTableColumn
applPastTransStreamDescr = _ApplPastTransStreamDescr_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 5, 1, 1),
    _ApplPastTransStreamDescr_Type()
)
applPastTransStreamDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransStreamDescr.setStatus("current")
_ApplPastTransStreamUnitOfWork_Type = SnmpAdminString
_ApplPastTransStreamUnitOfWork_Object = MibTableColumn
applPastTransStreamUnitOfWork = _ApplPastTransStreamUnitOfWork_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 5, 1, 2),
    _ApplPastTransStreamUnitOfWork_Type()
)
applPastTransStreamUnitOfWork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransStreamUnitOfWork.setStatus("current")
_ApplPastTransStreamInvokes_Type = Unsigned64TC
_ApplPastTransStreamInvokes_Object = MibTableColumn
applPastTransStreamInvokes = _ApplPastTransStreamInvokes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 5, 1, 3),
    _ApplPastTransStreamInvokes_Type()
)
applPastTransStreamInvokes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransStreamInvokes.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransStreamInvokes.setUnits("transactions")
_ApplPastTransStreamInvokesLow_Type = Unsigned32
_ApplPastTransStreamInvokesLow_Object = MibTableColumn
applPastTransStreamInvokesLow = _ApplPastTransStreamInvokesLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 5, 1, 4),
    _ApplPastTransStreamInvokesLow_Type()
)
applPastTransStreamInvokesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransStreamInvokesLow.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransStreamInvokesLow.setUnits("transactions")
_ApplPastTransStreamInvCumTimes_Type = Unsigned32
_ApplPastTransStreamInvCumTimes_Object = MibTableColumn
applPastTransStreamInvCumTimes = _ApplPastTransStreamInvCumTimes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 5, 1, 5),
    _ApplPastTransStreamInvCumTimes_Type()
)
applPastTransStreamInvCumTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransStreamInvCumTimes.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransStreamInvCumTimes.setUnits("milliseconds")
_ApplPastTransStreamInvRspTimes_Type = Unsigned32
_ApplPastTransStreamInvRspTimes_Object = MibTableColumn
applPastTransStreamInvRspTimes = _ApplPastTransStreamInvRspTimes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 5, 1, 6),
    _ApplPastTransStreamInvRspTimes_Type()
)
applPastTransStreamInvRspTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransStreamInvRspTimes.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransStreamInvRspTimes.setUnits("milliseconds")
_ApplPastTransStreamPerforms_Type = Unsigned64TC
_ApplPastTransStreamPerforms_Object = MibTableColumn
applPastTransStreamPerforms = _ApplPastTransStreamPerforms_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 5, 1, 7),
    _ApplPastTransStreamPerforms_Type()
)
applPastTransStreamPerforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransStreamPerforms.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransStreamPerforms.setUnits("transactions")
_ApplPastTransStreamPerformsLow_Type = Unsigned32
_ApplPastTransStreamPerformsLow_Object = MibTableColumn
applPastTransStreamPerformsLow = _ApplPastTransStreamPerformsLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 5, 1, 8),
    _ApplPastTransStreamPerformsLow_Type()
)
applPastTransStreamPerformsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransStreamPerformsLow.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransStreamPerformsLow.setUnits("transactions")
_ApplPastTransStreamPrfCumTimes_Type = Unsigned32
_ApplPastTransStreamPrfCumTimes_Object = MibTableColumn
applPastTransStreamPrfCumTimes = _ApplPastTransStreamPrfCumTimes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 5, 1, 9),
    _ApplPastTransStreamPrfCumTimes_Type()
)
applPastTransStreamPrfCumTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransStreamPrfCumTimes.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransStreamPrfCumTimes.setUnits("milliseconds")
_ApplPastTransStreamPrfRspTimes_Type = Unsigned32
_ApplPastTransStreamPrfRspTimes_Object = MibTableColumn
applPastTransStreamPrfRspTimes = _ApplPastTransStreamPrfRspTimes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 5, 1, 10),
    _ApplPastTransStreamPrfRspTimes_Type()
)
applPastTransStreamPrfRspTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransStreamPrfRspTimes.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransStreamPrfRspTimes.setUnits("milliseconds")
_ApplPastTransFlowTable_Object = MibTable
applPastTransFlowTable = _ApplPastTransFlowTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 6)
)
if mibBuilder.loadTexts:
    applPastTransFlowTable.setStatus("current")
_ApplPastTransFlowEntry_Object = MibTableRow
applPastTransFlowEntry = _ApplPastTransFlowEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 6, 1)
)
applPastTransFlowEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
    (0, "APPLICATION-MIB", "applPastChannelIndex"),
    (0, "APPLICATION-MIB", "applPastTransFlowDirection"),
    (0, "APPLICATION-MIB", "applPastTransFlowReqRsp"),
)
if mibBuilder.loadTexts:
    applPastTransFlowEntry.setStatus("current")


class _ApplPastTransFlowDirection_Type(Integer32):
    """Custom type applPastTransFlowDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 2),
          ("transmit", 1))
    )


_ApplPastTransFlowDirection_Type.__name__ = "Integer32"
_ApplPastTransFlowDirection_Object = MibTableColumn
applPastTransFlowDirection = _ApplPastTransFlowDirection_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 6, 1, 1),
    _ApplPastTransFlowDirection_Type()
)
applPastTransFlowDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    applPastTransFlowDirection.setStatus("current")


class _ApplPastTransFlowReqRsp_Type(Integer32):
    """Custom type applPastTransFlowReqRsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("request", 1),
          ("response", 2))
    )


_ApplPastTransFlowReqRsp_Type.__name__ = "Integer32"
_ApplPastTransFlowReqRsp_Object = MibTableColumn
applPastTransFlowReqRsp = _ApplPastTransFlowReqRsp_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 6, 1, 2),
    _ApplPastTransFlowReqRsp_Type()
)
applPastTransFlowReqRsp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    applPastTransFlowReqRsp.setStatus("current")
_ApplPastTransFlowTrans_Type = Unsigned64TC
_ApplPastTransFlowTrans_Object = MibTableColumn
applPastTransFlowTrans = _ApplPastTransFlowTrans_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 6, 1, 3),
    _ApplPastTransFlowTrans_Type()
)
applPastTransFlowTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransFlowTrans.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransFlowTrans.setUnits("transactions")
_ApplPastTransFlowTransLow_Type = Unsigned32
_ApplPastTransFlowTransLow_Object = MibTableColumn
applPastTransFlowTransLow = _ApplPastTransFlowTransLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 6, 1, 4),
    _ApplPastTransFlowTransLow_Type()
)
applPastTransFlowTransLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransFlowTransLow.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransFlowTransLow.setUnits("transactions")
_ApplPastTransFlowBytes_Type = Unsigned64TC
_ApplPastTransFlowBytes_Object = MibTableColumn
applPastTransFlowBytes = _ApplPastTransFlowBytes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 6, 1, 5),
    _ApplPastTransFlowBytes_Type()
)
applPastTransFlowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransFlowBytes.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransFlowBytes.setUnits("bytes")
_ApplPastTransFlowBytesLow_Type = Unsigned32
_ApplPastTransFlowBytesLow_Object = MibTableColumn
applPastTransFlowBytesLow = _ApplPastTransFlowBytesLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 6, 1, 6),
    _ApplPastTransFlowBytesLow_Type()
)
applPastTransFlowBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransFlowBytesLow.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransFlowBytesLow.setUnits("bytes")


class _ApplPastTransFlowTime_Type(DateAndTime):
    """Custom type applPastTransFlowTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_ApplPastTransFlowTime_Object = MibTableColumn
applPastTransFlowTime = _ApplPastTransFlowTime_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 6, 1, 7),
    _ApplPastTransFlowTime_Type()
)
applPastTransFlowTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransFlowTime.setStatus("current")
_ApplPastTransKindTable_Object = MibTable
applPastTransKindTable = _ApplPastTransKindTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 7)
)
if mibBuilder.loadTexts:
    applPastTransKindTable.setStatus("current")
_ApplPastTransKindEntry_Object = MibTableRow
applPastTransKindEntry = _ApplPastTransKindEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 7, 1)
)
applPastTransKindEntry.setIndexNames(
    (0, "APPLICATION-MIB", "applElmtOrSvc"),
    (0, "APPLICATION-MIB", "applElmtOrSvcId"),
    (0, "APPLICATION-MIB", "applPastChannelIndex"),
    (0, "APPLICATION-MIB", "applPastTransFlowDirection"),
    (0, "APPLICATION-MIB", "applPastTransFlowReqRsp"),
    (0, "APPLICATION-MIB", "applPastTransKind"),
)
if mibBuilder.loadTexts:
    applPastTransKindEntry.setStatus("current")


class _ApplPastTransKind_Type(SnmpAdminString):
    """Custom type applPastTransKind based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApplPastTransKind_Type.__name__ = "SnmpAdminString"
_ApplPastTransKind_Object = MibTableColumn
applPastTransKind = _ApplPastTransKind_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 7, 1, 1),
    _ApplPastTransKind_Type()
)
applPastTransKind.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    applPastTransKind.setStatus("current")
_ApplPastTransKindTrans_Type = Unsigned64TC
_ApplPastTransKindTrans_Object = MibTableColumn
applPastTransKindTrans = _ApplPastTransKindTrans_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 7, 1, 2),
    _ApplPastTransKindTrans_Type()
)
applPastTransKindTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransKindTrans.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransKindTrans.setUnits("transactions")
_ApplPastTransKindTransLow_Type = Unsigned32
_ApplPastTransKindTransLow_Object = MibTableColumn
applPastTransKindTransLow = _ApplPastTransKindTransLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 7, 1, 3),
    _ApplPastTransKindTransLow_Type()
)
applPastTransKindTransLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransKindTransLow.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransKindTransLow.setUnits("transactions")
_ApplPastTransKindBytes_Type = Unsigned64TC
_ApplPastTransKindBytes_Object = MibTableColumn
applPastTransKindBytes = _ApplPastTransKindBytes_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 7, 1, 4),
    _ApplPastTransKindBytes_Type()
)
applPastTransKindBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransKindBytes.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransKindBytes.setUnits("bytes")
_ApplPastTransKindBytesLow_Type = Unsigned32
_ApplPastTransKindBytesLow_Object = MibTableColumn
applPastTransKindBytesLow = _ApplPastTransKindBytesLow_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 7, 1, 5),
    _ApplPastTransKindBytesLow_Type()
)
applPastTransKindBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransKindBytesLow.setStatus("current")
if mibBuilder.loadTexts:
    applPastTransKindBytesLow.setUnits("bytes")


class _ApplPastTransKindTime_Type(DateAndTime):
    """Custom type applPastTransKindTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_ApplPastTransKindTime_Object = MibTableColumn
applPastTransKindTime = _ApplPastTransKindTime_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 3, 7, 1, 6),
    _ApplPastTransKindTime_Type()
)
applPastTransKindTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPastTransKindTime.setStatus("current")
_ApplElmtRunControlGroup_ObjectIdentity = ObjectIdentity
applElmtRunControlGroup = _ApplElmtRunControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 62, 1, 4)
)
_ApplElmtRunStatusTable_Object = MibTable
applElmtRunStatusTable = _ApplElmtRunStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 1)
)
if mibBuilder.loadTexts:
    applElmtRunStatusTable.setStatus("current")
_ApplElmtRunStatusEntry_Object = MibTableRow
applElmtRunStatusEntry = _ApplElmtRunStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 1, 1)
)
applElmtRunStatusEntry.setIndexNames(
    (0, "SYSAPPL-MIB", "sysApplElmtRunIndex"),
)
if mibBuilder.loadTexts:
    applElmtRunStatusEntry.setStatus("current")
_ApplElmtRunStatusSuspended_Type = TruthValue
_ApplElmtRunStatusSuspended_Object = MibTableColumn
applElmtRunStatusSuspended = _ApplElmtRunStatusSuspended_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 1, 1, 1),
    _ApplElmtRunStatusSuspended_Type()
)
applElmtRunStatusSuspended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applElmtRunStatusSuspended.setStatus("current")
_ApplElmtRunStatusHeapUsage_Type = Unsigned32
_ApplElmtRunStatusHeapUsage_Object = MibTableColumn
applElmtRunStatusHeapUsage = _ApplElmtRunStatusHeapUsage_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 1, 1, 2),
    _ApplElmtRunStatusHeapUsage_Type()
)
applElmtRunStatusHeapUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applElmtRunStatusHeapUsage.setStatus("current")
if mibBuilder.loadTexts:
    applElmtRunStatusHeapUsage.setUnits("bytes")
_ApplElmtRunStatusOpenConnections_Type = Unsigned32
_ApplElmtRunStatusOpenConnections_Object = MibTableColumn
applElmtRunStatusOpenConnections = _ApplElmtRunStatusOpenConnections_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 1, 1, 3),
    _ApplElmtRunStatusOpenConnections_Type()
)
applElmtRunStatusOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applElmtRunStatusOpenConnections.setStatus("current")
if mibBuilder.loadTexts:
    applElmtRunStatusOpenConnections.setUnits("connections")
_ApplElmtRunStatusOpenFiles_Type = Gauge32
_ApplElmtRunStatusOpenFiles_Object = MibTableColumn
applElmtRunStatusOpenFiles = _ApplElmtRunStatusOpenFiles_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 1, 1, 4),
    _ApplElmtRunStatusOpenFiles_Type()
)
applElmtRunStatusOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applElmtRunStatusOpenFiles.setStatus("current")
if mibBuilder.loadTexts:
    applElmtRunStatusOpenFiles.setUnits("files")
_ApplElmtRunStatusLastErrorMsg_Type = SnmpAdminString
_ApplElmtRunStatusLastErrorMsg_Object = MibTableColumn
applElmtRunStatusLastErrorMsg = _ApplElmtRunStatusLastErrorMsg_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 1, 1, 5),
    _ApplElmtRunStatusLastErrorMsg_Type()
)
applElmtRunStatusLastErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applElmtRunStatusLastErrorMsg.setStatus("current")


class _ApplElmtRunStatusLastErrorTime_Type(DateAndTime):
    """Custom type applElmtRunStatusLastErrorTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_ApplElmtRunStatusLastErrorTime_Object = MibTableColumn
applElmtRunStatusLastErrorTime = _ApplElmtRunStatusLastErrorTime_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 1, 1, 6),
    _ApplElmtRunStatusLastErrorTime_Type()
)
applElmtRunStatusLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applElmtRunStatusLastErrorTime.setStatus("current")
_ApplElmtRunControlTable_Object = MibTable
applElmtRunControlTable = _ApplElmtRunControlTable_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 2)
)
if mibBuilder.loadTexts:
    applElmtRunControlTable.setStatus("current")
_ApplElmtRunControlEntry_Object = MibTableRow
applElmtRunControlEntry = _ApplElmtRunControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 2, 1)
)
applElmtRunControlEntry.setIndexNames(
    (0, "SYSAPPL-MIB", "sysApplElmtRunIndex"),
)
if mibBuilder.loadTexts:
    applElmtRunControlEntry.setStatus("current")


class _ApplElmtRunControlSuspend_Type(TruthValue):
    """Custom type applElmtRunControlSuspend based on TruthValue"""


_ApplElmtRunControlSuspend_Object = MibTableColumn
applElmtRunControlSuspend = _ApplElmtRunControlSuspend_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 2, 1, 1),
    _ApplElmtRunControlSuspend_Type()
)
applElmtRunControlSuspend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applElmtRunControlSuspend.setStatus("current")
_ApplElmtRunControlReconfigure_Type = TestAndIncr
_ApplElmtRunControlReconfigure_Object = MibTableColumn
applElmtRunControlReconfigure = _ApplElmtRunControlReconfigure_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 2, 1, 2),
    _ApplElmtRunControlReconfigure_Type()
)
applElmtRunControlReconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applElmtRunControlReconfigure.setStatus("current")


class _ApplElmtRunControlTerminate_Type(TruthValue):
    """Custom type applElmtRunControlTerminate based on TruthValue"""


_ApplElmtRunControlTerminate_Object = MibTableColumn
applElmtRunControlTerminate = _ApplElmtRunControlTerminate_Object(
    (1, 3, 6, 1, 2, 1, 62, 1, 4, 2, 1, 3),
    _ApplElmtRunControlTerminate_Type()
)
applElmtRunControlTerminate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applElmtRunControlTerminate.setStatus("current")
_ApplicationMibConformance_ObjectIdentity = ObjectIdentity
applicationMibConformance = _ApplicationMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 62, 2)
)
_ApplicationMibGroups_ObjectIdentity = ObjectIdentity
applicationMibGroups = _ApplicationMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 62, 2, 1)
)

# Managed Objects groups

applicationMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 62, 2, 1, 1)
)
applicationMonitorGroup.setObjects(
      *(("APPLICATION-MIB", "applSrvInstQual"),
        ("APPLICATION-MIB", "applSrvName"),
        ("APPLICATION-MIB", "applSrvIndex"),
        ("APPLICATION-MIB", "applSrvInstance"),
        ("APPLICATION-MIB", "applOpenChannelOpenTime"),
        ("APPLICATION-MIB", "applOpenChannelReadRequestsLow"),
        ("APPLICATION-MIB", "applOpenChannelReadFailures"),
        ("APPLICATION-MIB", "applOpenChannelBytesReadLow"),
        ("APPLICATION-MIB", "applOpenChannelLastReadTime"),
        ("APPLICATION-MIB", "applOpenChannelWriteRequestsLow"),
        ("APPLICATION-MIB", "applOpenChannelWriteFailures"),
        ("APPLICATION-MIB", "applOpenChannelBytesWrittenLow"),
        ("APPLICATION-MIB", "applOpenChannelLastWriteTime"),
        ("APPLICATION-MIB", "applOpenFileName"),
        ("APPLICATION-MIB", "applOpenFileSizeHigh"),
        ("APPLICATION-MIB", "applOpenFileSizeLow"),
        ("APPLICATION-MIB", "applOpenFileMode"),
        ("APPLICATION-MIB", "applOpenConnectionTransport"),
        ("APPLICATION-MIB", "applOpenConnectionNearEndAddr"),
        ("APPLICATION-MIB", "applOpenConnectionNearEndpoint"),
        ("APPLICATION-MIB", "applOpenConnectionFarEndAddr"),
        ("APPLICATION-MIB", "applOpenConnectionFarEndpoint"),
        ("APPLICATION-MIB", "applOpenConnectionApplication"))
)
if mibBuilder.loadTexts:
    applicationMonitorGroup.setStatus("current")

applicationFastMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 62, 2, 1, 2)
)
applicationFastMonitorGroup.setObjects(
      *(("APPLICATION-MIB", "applOpenChannelReadRequests"),
        ("APPLICATION-MIB", "applOpenChannelBytesRead"),
        ("APPLICATION-MIB", "applOpenChannelWriteRequests"),
        ("APPLICATION-MIB", "applOpenChannelBytesWritten"))
)
if mibBuilder.loadTexts:
    applicationFastMonitorGroup.setStatus("current")

applicationTransactGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 62, 2, 1, 3)
)
applicationTransactGroup.setObjects(
      *(("APPLICATION-MIB", "applTransactStreamDescr"),
        ("APPLICATION-MIB", "applTransactStreamUnitOfWork"),
        ("APPLICATION-MIB", "applTransactStreamInvokesLow"),
        ("APPLICATION-MIB", "applTransactStreamInvCumTimes"),
        ("APPLICATION-MIB", "applTransactStreamInvRspTimes"),
        ("APPLICATION-MIB", "applTransactStreamPerformsLow"),
        ("APPLICATION-MIB", "applTransactStreamPrfCumTimes"),
        ("APPLICATION-MIB", "applTransactStreamPrfRspTimes"),
        ("APPLICATION-MIB", "applTransactFlowTransLow"),
        ("APPLICATION-MIB", "applTransactFlowBytesLow"),
        ("APPLICATION-MIB", "applTransactFlowTime"),
        ("APPLICATION-MIB", "applTransactKindTransLow"),
        ("APPLICATION-MIB", "applTransactKindBytesLow"),
        ("APPLICATION-MIB", "applTransactKindTime"))
)
if mibBuilder.loadTexts:
    applicationTransactGroup.setStatus("current")

applicationFastTransactGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 62, 2, 1, 4)
)
applicationFastTransactGroup.setObjects(
      *(("APPLICATION-MIB", "applTransactStreamInvokes"),
        ("APPLICATION-MIB", "applTransactStreamPerforms"),
        ("APPLICATION-MIB", "applTransactFlowTrans"),
        ("APPLICATION-MIB", "applTransactFlowBytes"),
        ("APPLICATION-MIB", "applTransactKindTrans"),
        ("APPLICATION-MIB", "applTransactKindBytes"))
)
if mibBuilder.loadTexts:
    applicationFastTransactGroup.setStatus("current")

applicationHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 62, 2, 1, 5)
)
applicationHistoryGroup.setObjects(
      *(("APPLICATION-MIB", "applPastChannelControlCollect"),
        ("APPLICATION-MIB", "applPastChannelControlMaxRows"),
        ("APPLICATION-MIB", "applPastChannelControlTimeLimit"),
        ("APPLICATION-MIB", "applPastChannelControlRemItems"),
        ("APPLICATION-MIB", "applPastChannelOpenTime"),
        ("APPLICATION-MIB", "applPastChannelCloseTime"),
        ("APPLICATION-MIB", "applPastChannelReadReqsLow"),
        ("APPLICATION-MIB", "applPastChannelReadFailures"),
        ("APPLICATION-MIB", "applPastChannelBytesReadLow"),
        ("APPLICATION-MIB", "applPastChannelLastReadTime"),
        ("APPLICATION-MIB", "applPastChannelWriteReqsLow"),
        ("APPLICATION-MIB", "applPastChannelWriteFailures"),
        ("APPLICATION-MIB", "applPastChannelBytesWritLow"),
        ("APPLICATION-MIB", "applPastChannelLastWriteTime"),
        ("APPLICATION-MIB", "applPastFileName"),
        ("APPLICATION-MIB", "applPastFileSizeHigh"),
        ("APPLICATION-MIB", "applPastFileSizeLow"),
        ("APPLICATION-MIB", "applPastFileMode"),
        ("APPLICATION-MIB", "applPastConTransport"),
        ("APPLICATION-MIB", "applPastConNearEndAddr"),
        ("APPLICATION-MIB", "applPastConNearEndpoint"),
        ("APPLICATION-MIB", "applPastConFarEndAddr"),
        ("APPLICATION-MIB", "applPastConFarEndpoint"),
        ("APPLICATION-MIB", "applPastConApplication"))
)
if mibBuilder.loadTexts:
    applicationHistoryGroup.setStatus("current")

applicationFastHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 62, 2, 1, 6)
)
applicationFastHistoryGroup.setObjects(
      *(("APPLICATION-MIB", "applPastChannelReadRequests"),
        ("APPLICATION-MIB", "applPastChannelBytesRead"),
        ("APPLICATION-MIB", "applPastChannelWriteRequests"),
        ("APPLICATION-MIB", "applPastChannelBytesWritten"))
)
if mibBuilder.loadTexts:
    applicationFastHistoryGroup.setStatus("current")

applicationTransHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 62, 2, 1, 7)
)
applicationTransHistoryGroup.setObjects(
      *(("APPLICATION-MIB", "applPastTransStreamDescr"),
        ("APPLICATION-MIB", "applPastTransStreamUnitOfWork"),
        ("APPLICATION-MIB", "applPastTransStreamInvokesLow"),
        ("APPLICATION-MIB", "applPastTransStreamInvCumTimes"),
        ("APPLICATION-MIB", "applPastTransStreamInvRspTimes"),
        ("APPLICATION-MIB", "applPastTransStreamPerformsLow"),
        ("APPLICATION-MIB", "applPastTransStreamPrfCumTimes"),
        ("APPLICATION-MIB", "applPastTransStreamPrfRspTimes"),
        ("APPLICATION-MIB", "applPastTransFlowTransLow"),
        ("APPLICATION-MIB", "applPastTransFlowBytesLow"),
        ("APPLICATION-MIB", "applPastTransFlowTime"),
        ("APPLICATION-MIB", "applPastTransKindTransLow"),
        ("APPLICATION-MIB", "applPastTransKindBytesLow"),
        ("APPLICATION-MIB", "applPastTransKindTime"))
)
if mibBuilder.loadTexts:
    applicationTransHistoryGroup.setStatus("current")

applicationFastTransHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 62, 2, 1, 8)
)
applicationFastTransHistoryGroup.setObjects(
      *(("APPLICATION-MIB", "applPastTransFlowTrans"),
        ("APPLICATION-MIB", "applPastTransFlowBytes"),
        ("APPLICATION-MIB", "applPastTransKindTrans"),
        ("APPLICATION-MIB", "applPastTransKindBytes"),
        ("APPLICATION-MIB", "applPastTransStreamPerforms"),
        ("APPLICATION-MIB", "applPastTransStreamInvokes"))
)
if mibBuilder.loadTexts:
    applicationFastTransHistoryGroup.setStatus("current")

applicationRunGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 62, 2, 1, 9)
)
applicationRunGroup.setObjects(
      *(("APPLICATION-MIB", "applElmtRunStatusSuspended"),
        ("APPLICATION-MIB", "applElmtRunStatusHeapUsage"),
        ("APPLICATION-MIB", "applElmtRunStatusOpenConnections"),
        ("APPLICATION-MIB", "applElmtRunStatusOpenFiles"),
        ("APPLICATION-MIB", "applElmtRunStatusLastErrorMsg"),
        ("APPLICATION-MIB", "applElmtRunStatusLastErrorTime"),
        ("APPLICATION-MIB", "applElmtRunControlSuspend"),
        ("APPLICATION-MIB", "applElmtRunControlReconfigure"),
        ("APPLICATION-MIB", "applElmtRunControlTerminate"))
)
if mibBuilder.loadTexts:
    applicationRunGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

applicationMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 62, 2, 2)
)
if mibBuilder.loadTexts:
    applicationMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPLICATION-MIB",
    **{"Unsigned64TC": Unsigned64TC,
       "ApplTAddress": ApplTAddress,
       "applicationMib": applicationMib,
       "applicationMibObjects": applicationMibObjects,
       "applServiceGroup": applServiceGroup,
       "applSrvNameToSrvInstTable": applSrvNameToSrvInstTable,
       "applSrvNameToSrvInstEntry": applSrvNameToSrvInstEntry,
       "applSrvInstQual": applSrvInstQual,
       "applSrvInstToSrvNameTable": applSrvInstToSrvNameTable,
       "applSrvInstToSrvNameEntry": applSrvInstToSrvNameEntry,
       "applSrvName": applSrvName,
       "applSrvInstToRunApplElmtTable": applSrvInstToRunApplElmtTable,
       "applSrvInstToRunApplElmtEntry": applSrvInstToRunApplElmtEntry,
       "applSrvIndex": applSrvIndex,
       "applRunApplElmtToSrvInstTable": applRunApplElmtToSrvInstTable,
       "applRunApplElmtToSrvInstEntry": applRunApplElmtToSrvInstEntry,
       "applSrvInstance": applSrvInstance,
       "applChannelGroup": applChannelGroup,
       "applOpenChannelTable": applOpenChannelTable,
       "applOpenChannelEntry": applOpenChannelEntry,
       "applElmtOrSvc": applElmtOrSvc,
       "applElmtOrSvcId": applElmtOrSvcId,
       "applOpenChannelIndex": applOpenChannelIndex,
       "applOpenChannelOpenTime": applOpenChannelOpenTime,
       "applOpenChannelReadRequests": applOpenChannelReadRequests,
       "applOpenChannelReadRequestsLow": applOpenChannelReadRequestsLow,
       "applOpenChannelReadFailures": applOpenChannelReadFailures,
       "applOpenChannelBytesRead": applOpenChannelBytesRead,
       "applOpenChannelBytesReadLow": applOpenChannelBytesReadLow,
       "applOpenChannelLastReadTime": applOpenChannelLastReadTime,
       "applOpenChannelWriteRequests": applOpenChannelWriteRequests,
       "applOpenChannelWriteRequestsLow": applOpenChannelWriteRequestsLow,
       "applOpenChannelWriteFailures": applOpenChannelWriteFailures,
       "applOpenChannelBytesWritten": applOpenChannelBytesWritten,
       "applOpenChannelBytesWrittenLow": applOpenChannelBytesWrittenLow,
       "applOpenChannelLastWriteTime": applOpenChannelLastWriteTime,
       "applOpenFileTable": applOpenFileTable,
       "applOpenFileEntry": applOpenFileEntry,
       "applOpenFileName": applOpenFileName,
       "applOpenFileSizeHigh": applOpenFileSizeHigh,
       "applOpenFileSizeLow": applOpenFileSizeLow,
       "applOpenFileMode": applOpenFileMode,
       "applOpenConnectionTable": applOpenConnectionTable,
       "applOpenConnectionEntry": applOpenConnectionEntry,
       "applOpenConnectionTransport": applOpenConnectionTransport,
       "applOpenConnectionNearEndAddr": applOpenConnectionNearEndAddr,
       "applOpenConnectionNearEndpoint": applOpenConnectionNearEndpoint,
       "applOpenConnectionFarEndAddr": applOpenConnectionFarEndAddr,
       "applOpenConnectionFarEndpoint": applOpenConnectionFarEndpoint,
       "applOpenConnectionApplication": applOpenConnectionApplication,
       "applTransactionStreamTable": applTransactionStreamTable,
       "applTransactionStreamEntry": applTransactionStreamEntry,
       "applTransactStreamDescr": applTransactStreamDescr,
       "applTransactStreamUnitOfWork": applTransactStreamUnitOfWork,
       "applTransactStreamInvokes": applTransactStreamInvokes,
       "applTransactStreamInvokesLow": applTransactStreamInvokesLow,
       "applTransactStreamInvCumTimes": applTransactStreamInvCumTimes,
       "applTransactStreamInvRspTimes": applTransactStreamInvRspTimes,
       "applTransactStreamPerforms": applTransactStreamPerforms,
       "applTransactStreamPerformsLow": applTransactStreamPerformsLow,
       "applTransactStreamPrfCumTimes": applTransactStreamPrfCumTimes,
       "applTransactStreamPrfRspTimes": applTransactStreamPrfRspTimes,
       "applTransactFlowTable": applTransactFlowTable,
       "applTransactFlowEntry": applTransactFlowEntry,
       "applTransactFlowDirection": applTransactFlowDirection,
       "applTransactFlowReqRsp": applTransactFlowReqRsp,
       "applTransactFlowTrans": applTransactFlowTrans,
       "applTransactFlowTransLow": applTransactFlowTransLow,
       "applTransactFlowBytes": applTransactFlowBytes,
       "applTransactFlowBytesLow": applTransactFlowBytesLow,
       "applTransactFlowTime": applTransactFlowTime,
       "applTransactKindTable": applTransactKindTable,
       "applTransactKindEntry": applTransactKindEntry,
       "applTransactKind": applTransactKind,
       "applTransactKindTrans": applTransactKindTrans,
       "applTransactKindTransLow": applTransactKindTransLow,
       "applTransactKindBytes": applTransactKindBytes,
       "applTransactKindBytesLow": applTransactKindBytesLow,
       "applTransactKindTime": applTransactKindTime,
       "applPastChannelGroup": applPastChannelGroup,
       "applPastChannelControlTable": applPastChannelControlTable,
       "applPastChannelControlEntry": applPastChannelControlEntry,
       "applPastChannelControlCollect": applPastChannelControlCollect,
       "applPastChannelControlMaxRows": applPastChannelControlMaxRows,
       "applPastChannelControlTimeLimit": applPastChannelControlTimeLimit,
       "applPastChannelControlRemItems": applPastChannelControlRemItems,
       "applPastChannelTable": applPastChannelTable,
       "applPastChannelEntry": applPastChannelEntry,
       "applPastChannelIndex": applPastChannelIndex,
       "applPastChannelOpenTime": applPastChannelOpenTime,
       "applPastChannelCloseTime": applPastChannelCloseTime,
       "applPastChannelReadRequests": applPastChannelReadRequests,
       "applPastChannelReadReqsLow": applPastChannelReadReqsLow,
       "applPastChannelReadFailures": applPastChannelReadFailures,
       "applPastChannelBytesRead": applPastChannelBytesRead,
       "applPastChannelBytesReadLow": applPastChannelBytesReadLow,
       "applPastChannelLastReadTime": applPastChannelLastReadTime,
       "applPastChannelWriteRequests": applPastChannelWriteRequests,
       "applPastChannelWriteReqsLow": applPastChannelWriteReqsLow,
       "applPastChannelWriteFailures": applPastChannelWriteFailures,
       "applPastChannelBytesWritten": applPastChannelBytesWritten,
       "applPastChannelBytesWritLow": applPastChannelBytesWritLow,
       "applPastChannelLastWriteTime": applPastChannelLastWriteTime,
       "applPastFileTable": applPastFileTable,
       "applPastFileEntry": applPastFileEntry,
       "applPastFileName": applPastFileName,
       "applPastFileSizeHigh": applPastFileSizeHigh,
       "applPastFileSizeLow": applPastFileSizeLow,
       "applPastFileMode": applPastFileMode,
       "applPastConTable": applPastConTable,
       "applPastConEntry": applPastConEntry,
       "applPastConTransport": applPastConTransport,
       "applPastConNearEndAddr": applPastConNearEndAddr,
       "applPastConNearEndpoint": applPastConNearEndpoint,
       "applPastConFarEndAddr": applPastConFarEndAddr,
       "applPastConFarEndpoint": applPastConFarEndpoint,
       "applPastConApplication": applPastConApplication,
       "applPastTransStreamTable": applPastTransStreamTable,
       "applPastTransStreamEntry": applPastTransStreamEntry,
       "applPastTransStreamDescr": applPastTransStreamDescr,
       "applPastTransStreamUnitOfWork": applPastTransStreamUnitOfWork,
       "applPastTransStreamInvokes": applPastTransStreamInvokes,
       "applPastTransStreamInvokesLow": applPastTransStreamInvokesLow,
       "applPastTransStreamInvCumTimes": applPastTransStreamInvCumTimes,
       "applPastTransStreamInvRspTimes": applPastTransStreamInvRspTimes,
       "applPastTransStreamPerforms": applPastTransStreamPerforms,
       "applPastTransStreamPerformsLow": applPastTransStreamPerformsLow,
       "applPastTransStreamPrfCumTimes": applPastTransStreamPrfCumTimes,
       "applPastTransStreamPrfRspTimes": applPastTransStreamPrfRspTimes,
       "applPastTransFlowTable": applPastTransFlowTable,
       "applPastTransFlowEntry": applPastTransFlowEntry,
       "applPastTransFlowDirection": applPastTransFlowDirection,
       "applPastTransFlowReqRsp": applPastTransFlowReqRsp,
       "applPastTransFlowTrans": applPastTransFlowTrans,
       "applPastTransFlowTransLow": applPastTransFlowTransLow,
       "applPastTransFlowBytes": applPastTransFlowBytes,
       "applPastTransFlowBytesLow": applPastTransFlowBytesLow,
       "applPastTransFlowTime": applPastTransFlowTime,
       "applPastTransKindTable": applPastTransKindTable,
       "applPastTransKindEntry": applPastTransKindEntry,
       "applPastTransKind": applPastTransKind,
       "applPastTransKindTrans": applPastTransKindTrans,
       "applPastTransKindTransLow": applPastTransKindTransLow,
       "applPastTransKindBytes": applPastTransKindBytes,
       "applPastTransKindBytesLow": applPastTransKindBytesLow,
       "applPastTransKindTime": applPastTransKindTime,
       "applElmtRunControlGroup": applElmtRunControlGroup,
       "applElmtRunStatusTable": applElmtRunStatusTable,
       "applElmtRunStatusEntry": applElmtRunStatusEntry,
       "applElmtRunStatusSuspended": applElmtRunStatusSuspended,
       "applElmtRunStatusHeapUsage": applElmtRunStatusHeapUsage,
       "applElmtRunStatusOpenConnections": applElmtRunStatusOpenConnections,
       "applElmtRunStatusOpenFiles": applElmtRunStatusOpenFiles,
       "applElmtRunStatusLastErrorMsg": applElmtRunStatusLastErrorMsg,
       "applElmtRunStatusLastErrorTime": applElmtRunStatusLastErrorTime,
       "applElmtRunControlTable": applElmtRunControlTable,
       "applElmtRunControlEntry": applElmtRunControlEntry,
       "applElmtRunControlSuspend": applElmtRunControlSuspend,
       "applElmtRunControlReconfigure": applElmtRunControlReconfigure,
       "applElmtRunControlTerminate": applElmtRunControlTerminate,
       "applicationMibConformance": applicationMibConformance,
       "applicationMibGroups": applicationMibGroups,
       "applicationMonitorGroup": applicationMonitorGroup,
       "applicationFastMonitorGroup": applicationFastMonitorGroup,
       "applicationTransactGroup": applicationTransactGroup,
       "applicationFastTransactGroup": applicationFastTransactGroup,
       "applicationHistoryGroup": applicationHistoryGroup,
       "applicationFastHistoryGroup": applicationFastHistoryGroup,
       "applicationTransHistoryGroup": applicationTransHistoryGroup,
       "applicationFastTransHistoryGroup": applicationFastTransHistoryGroup,
       "applicationRunGroup": applicationRunGroup,
       "applicationMibCompliance": applicationMibCompliance}
)
