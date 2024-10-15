# SNMP MIB module (NHRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NHRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:13 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

nhrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 71)
)
nhrpMIB.setRevisions(
        ("1999-08-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NhrpGenAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



# MIB Managed Objects in the order of their OIDs

_NhrpObjects_ObjectIdentity = ObjectIdentity
nhrpObjects = _NhrpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 71, 1)
)
_NhrpGeneralObjects_ObjectIdentity = ObjectIdentity
nhrpGeneralObjects = _NhrpGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 71, 1, 1)
)
_NhrpNextIndex_Type = Unsigned32
_NhrpNextIndex_Object = MibScalar
nhrpNextIndex = _NhrpNextIndex_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 1),
    _NhrpNextIndex_Type()
)
nhrpNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpNextIndex.setStatus("current")
_NhrpCacheTable_Object = MibTable
nhrpCacheTable = _NhrpCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2)
)
if mibBuilder.loadTexts:
    nhrpCacheTable.setStatus("current")
_NhrpCacheEntry_Object = MibTableRow
nhrpCacheEntry = _NhrpCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1)
)
nhrpCacheEntry.setIndexNames(
    (0, "NHRP-MIB", "nhrpCacheInternetworkAddrType"),
    (0, "NHRP-MIB", "nhrpCacheInternetworkAddr"),
    (0, "IF-MIB", "ifIndex"),
    (0, "NHRP-MIB", "nhrpCacheIndex"),
)
if mibBuilder.loadTexts:
    nhrpCacheEntry.setStatus("current")
_NhrpCacheInternetworkAddrType_Type = AddressFamilyNumbers
_NhrpCacheInternetworkAddrType_Object = MibTableColumn
nhrpCacheInternetworkAddrType = _NhrpCacheInternetworkAddrType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 1),
    _NhrpCacheInternetworkAddrType_Type()
)
nhrpCacheInternetworkAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhrpCacheInternetworkAddrType.setStatus("current")
_NhrpCacheInternetworkAddr_Type = NhrpGenAddr
_NhrpCacheInternetworkAddr_Object = MibTableColumn
nhrpCacheInternetworkAddr = _NhrpCacheInternetworkAddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 2),
    _NhrpCacheInternetworkAddr_Type()
)
nhrpCacheInternetworkAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhrpCacheInternetworkAddr.setStatus("current")


class _NhrpCacheIndex_Type(Unsigned32):
    """Custom type nhrpCacheIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NhrpCacheIndex_Type.__name__ = "Unsigned32"
_NhrpCacheIndex_Object = MibTableColumn
nhrpCacheIndex = _NhrpCacheIndex_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 3),
    _NhrpCacheIndex_Type()
)
nhrpCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhrpCacheIndex.setStatus("current")


class _NhrpCachePrefixLength_Type(Integer32):
    """Custom type nhrpCachePrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NhrpCachePrefixLength_Type.__name__ = "Integer32"
_NhrpCachePrefixLength_Object = MibTableColumn
nhrpCachePrefixLength = _NhrpCachePrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 4),
    _NhrpCachePrefixLength_Type()
)
nhrpCachePrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpCachePrefixLength.setStatus("current")
_NhrpCacheNextHopInternetworkAddr_Type = NhrpGenAddr
_NhrpCacheNextHopInternetworkAddr_Object = MibTableColumn
nhrpCacheNextHopInternetworkAddr = _NhrpCacheNextHopInternetworkAddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 5),
    _NhrpCacheNextHopInternetworkAddr_Type()
)
nhrpCacheNextHopInternetworkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpCacheNextHopInternetworkAddr.setStatus("current")
_NhrpCacheNbmaAddrType_Type = AddressFamilyNumbers
_NhrpCacheNbmaAddrType_Object = MibTableColumn
nhrpCacheNbmaAddrType = _NhrpCacheNbmaAddrType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 6),
    _NhrpCacheNbmaAddrType_Type()
)
nhrpCacheNbmaAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpCacheNbmaAddrType.setStatus("current")
_NhrpCacheNbmaAddr_Type = NhrpGenAddr
_NhrpCacheNbmaAddr_Object = MibTableColumn
nhrpCacheNbmaAddr = _NhrpCacheNbmaAddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 7),
    _NhrpCacheNbmaAddr_Type()
)
nhrpCacheNbmaAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpCacheNbmaAddr.setStatus("current")
_NhrpCacheNbmaSubaddr_Type = NhrpGenAddr
_NhrpCacheNbmaSubaddr_Object = MibTableColumn
nhrpCacheNbmaSubaddr = _NhrpCacheNbmaSubaddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 8),
    _NhrpCacheNbmaSubaddr_Type()
)
nhrpCacheNbmaSubaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpCacheNbmaSubaddr.setStatus("current")


class _NhrpCacheType_Type(Integer32):
    """Custom type nhrpCacheType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("administrativelyAdded", 6),
          ("atmarp", 7),
          ("other", 1),
          ("register", 2),
          ("resolveAuthoritative", 3),
          ("resoveNonauthoritative", 4),
          ("scsp", 8),
          ("transit", 5))
    )


_NhrpCacheType_Type.__name__ = "Integer32"
_NhrpCacheType_Object = MibTableColumn
nhrpCacheType = _NhrpCacheType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 9),
    _NhrpCacheType_Type()
)
nhrpCacheType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpCacheType.setStatus("current")


class _NhrpCacheState_Type(Integer32):
    """Custom type nhrpCacheState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ackReply", 2),
          ("incomplete", 1),
          ("nakReply", 3))
    )


_NhrpCacheState_Type.__name__ = "Integer32"
_NhrpCacheState_Object = MibTableColumn
nhrpCacheState = _NhrpCacheState_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 10),
    _NhrpCacheState_Type()
)
nhrpCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpCacheState.setStatus("current")
_NhrpCacheHoldingTimeValid_Type = TruthValue
_NhrpCacheHoldingTimeValid_Object = MibTableColumn
nhrpCacheHoldingTimeValid = _NhrpCacheHoldingTimeValid_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 11),
    _NhrpCacheHoldingTimeValid_Type()
)
nhrpCacheHoldingTimeValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpCacheHoldingTimeValid.setStatus("current")


class _NhrpCacheHoldingTime_Type(Unsigned32):
    """Custom type nhrpCacheHoldingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NhrpCacheHoldingTime_Type.__name__ = "Unsigned32"
_NhrpCacheHoldingTime_Object = MibTableColumn
nhrpCacheHoldingTime = _NhrpCacheHoldingTime_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 12),
    _NhrpCacheHoldingTime_Type()
)
nhrpCacheHoldingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpCacheHoldingTime.setStatus("current")
if mibBuilder.loadTexts:
    nhrpCacheHoldingTime.setUnits("seconds")


class _NhrpCacheNegotiatedMtu_Type(Integer32):
    """Custom type nhrpCacheNegotiatedMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NhrpCacheNegotiatedMtu_Type.__name__ = "Integer32"
_NhrpCacheNegotiatedMtu_Object = MibTableColumn
nhrpCacheNegotiatedMtu = _NhrpCacheNegotiatedMtu_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 13),
    _NhrpCacheNegotiatedMtu_Type()
)
nhrpCacheNegotiatedMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpCacheNegotiatedMtu.setStatus("current")


class _NhrpCachePreference_Type(Integer32):
    """Custom type nhrpCachePreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NhrpCachePreference_Type.__name__ = "Integer32"
_NhrpCachePreference_Object = MibTableColumn
nhrpCachePreference = _NhrpCachePreference_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 14),
    _NhrpCachePreference_Type()
)
nhrpCachePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpCachePreference.setStatus("current")


class _NhrpCacheStorageType_Type(StorageType):
    """Custom type nhrpCacheStorageType based on StorageType"""


_NhrpCacheStorageType_Object = MibTableColumn
nhrpCacheStorageType = _NhrpCacheStorageType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 15),
    _NhrpCacheStorageType_Type()
)
nhrpCacheStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpCacheStorageType.setStatus("current")
_NhrpCacheRowStatus_Type = RowStatus
_NhrpCacheRowStatus_Object = MibTableColumn
nhrpCacheRowStatus = _NhrpCacheRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 2, 1, 16),
    _NhrpCacheRowStatus_Type()
)
nhrpCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpCacheRowStatus.setStatus("current")
_NhrpPurgeReqTable_Object = MibTable
nhrpPurgeReqTable = _NhrpPurgeReqTable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 3)
)
if mibBuilder.loadTexts:
    nhrpPurgeReqTable.setStatus("current")
_NhrpPurgeReqEntry_Object = MibTableRow
nhrpPurgeReqEntry = _NhrpPurgeReqEntry_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 3, 1)
)
nhrpPurgeReqEntry.setIndexNames(
    (0, "NHRP-MIB", "nhrpPurgeIndex"),
)
if mibBuilder.loadTexts:
    nhrpPurgeReqEntry.setStatus("current")


class _NhrpPurgeIndex_Type(Unsigned32):
    """Custom type nhrpPurgeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NhrpPurgeIndex_Type.__name__ = "Unsigned32"
_NhrpPurgeIndex_Object = MibTableColumn
nhrpPurgeIndex = _NhrpPurgeIndex_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 3, 1, 1),
    _NhrpPurgeIndex_Type()
)
nhrpPurgeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhrpPurgeIndex.setStatus("current")


class _NhrpPurgeCacheIdentifier_Type(Unsigned32):
    """Custom type nhrpPurgeCacheIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NhrpPurgeCacheIdentifier_Type.__name__ = "Unsigned32"
_NhrpPurgeCacheIdentifier_Object = MibTableColumn
nhrpPurgeCacheIdentifier = _NhrpPurgeCacheIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 3, 1, 2),
    _NhrpPurgeCacheIdentifier_Type()
)
nhrpPurgeCacheIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpPurgeCacheIdentifier.setStatus("current")


class _NhrpPurgePrefixLength_Type(Integer32):
    """Custom type nhrpPurgePrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NhrpPurgePrefixLength_Type.__name__ = "Integer32"
_NhrpPurgePrefixLength_Object = MibTableColumn
nhrpPurgePrefixLength = _NhrpPurgePrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 3, 1, 3),
    _NhrpPurgePrefixLength_Type()
)
nhrpPurgePrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpPurgePrefixLength.setStatus("current")
_NhrpPurgeRequestID_Type = Unsigned32
_NhrpPurgeRequestID_Object = MibTableColumn
nhrpPurgeRequestID = _NhrpPurgeRequestID_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 3, 1, 4),
    _NhrpPurgeRequestID_Type()
)
nhrpPurgeRequestID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpPurgeRequestID.setStatus("current")
_NhrpPurgeReplyExpected_Type = TruthValue
_NhrpPurgeReplyExpected_Object = MibTableColumn
nhrpPurgeReplyExpected = _NhrpPurgeReplyExpected_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 3, 1, 5),
    _NhrpPurgeReplyExpected_Type()
)
nhrpPurgeReplyExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpPurgeReplyExpected.setStatus("current")
_NhrpPurgeRowStatus_Type = RowStatus
_NhrpPurgeRowStatus_Object = MibTableColumn
nhrpPurgeRowStatus = _NhrpPurgeRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 1, 3, 1, 6),
    _NhrpPurgeRowStatus_Type()
)
nhrpPurgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpPurgeRowStatus.setStatus("current")
_NhrpClientObjects_ObjectIdentity = ObjectIdentity
nhrpClientObjects = _NhrpClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 71, 1, 2)
)
_NhrpClientTable_Object = MibTable
nhrpClientTable = _NhrpClientTable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nhrpClientTable.setStatus("current")
_NhrpClientEntry_Object = MibTableRow
nhrpClientEntry = _NhrpClientEntry_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1)
)
nhrpClientEntry.setIndexNames(
    (0, "NHRP-MIB", "nhrpClientIndex"),
)
if mibBuilder.loadTexts:
    nhrpClientEntry.setStatus("current")


class _NhrpClientIndex_Type(Unsigned32):
    """Custom type nhrpClientIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NhrpClientIndex_Type.__name__ = "Unsigned32"
_NhrpClientIndex_Object = MibTableColumn
nhrpClientIndex = _NhrpClientIndex_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 1),
    _NhrpClientIndex_Type()
)
nhrpClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhrpClientIndex.setStatus("current")
_NhrpClientInternetworkAddrType_Type = AddressFamilyNumbers
_NhrpClientInternetworkAddrType_Object = MibTableColumn
nhrpClientInternetworkAddrType = _NhrpClientInternetworkAddrType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 2),
    _NhrpClientInternetworkAddrType_Type()
)
nhrpClientInternetworkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientInternetworkAddrType.setStatus("current")
_NhrpClientInternetworkAddr_Type = NhrpGenAddr
_NhrpClientInternetworkAddr_Object = MibTableColumn
nhrpClientInternetworkAddr = _NhrpClientInternetworkAddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 3),
    _NhrpClientInternetworkAddr_Type()
)
nhrpClientInternetworkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientInternetworkAddr.setStatus("current")
_NhrpClientNbmaAddrType_Type = AddressFamilyNumbers
_NhrpClientNbmaAddrType_Object = MibTableColumn
nhrpClientNbmaAddrType = _NhrpClientNbmaAddrType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 4),
    _NhrpClientNbmaAddrType_Type()
)
nhrpClientNbmaAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientNbmaAddrType.setStatus("current")
_NhrpClientNbmaAddr_Type = NhrpGenAddr
_NhrpClientNbmaAddr_Object = MibTableColumn
nhrpClientNbmaAddr = _NhrpClientNbmaAddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 5),
    _NhrpClientNbmaAddr_Type()
)
nhrpClientNbmaAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientNbmaAddr.setStatus("current")
_NhrpClientNbmaSubaddr_Type = NhrpGenAddr
_NhrpClientNbmaSubaddr_Object = MibTableColumn
nhrpClientNbmaSubaddr = _NhrpClientNbmaSubaddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 6),
    _NhrpClientNbmaSubaddr_Type()
)
nhrpClientNbmaSubaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientNbmaSubaddr.setStatus("current")


class _NhrpClientInitialRequestTimeout_Type(Integer32):
    """Custom type nhrpClientInitialRequestTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_NhrpClientInitialRequestTimeout_Type.__name__ = "Integer32"
_NhrpClientInitialRequestTimeout_Object = MibTableColumn
nhrpClientInitialRequestTimeout = _NhrpClientInitialRequestTimeout_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 7),
    _NhrpClientInitialRequestTimeout_Type()
)
nhrpClientInitialRequestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientInitialRequestTimeout.setStatus("current")
if mibBuilder.loadTexts:
    nhrpClientInitialRequestTimeout.setUnits("seconds")


class _NhrpClientRegistrationRequestRetries_Type(Integer32):
    """Custom type nhrpClientRegistrationRequestRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NhrpClientRegistrationRequestRetries_Type.__name__ = "Integer32"
_NhrpClientRegistrationRequestRetries_Object = MibTableColumn
nhrpClientRegistrationRequestRetries = _NhrpClientRegistrationRequestRetries_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 8),
    _NhrpClientRegistrationRequestRetries_Type()
)
nhrpClientRegistrationRequestRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientRegistrationRequestRetries.setStatus("current")


class _NhrpClientResolutionRequestRetries_Type(Integer32):
    """Custom type nhrpClientResolutionRequestRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NhrpClientResolutionRequestRetries_Type.__name__ = "Integer32"
_NhrpClientResolutionRequestRetries_Object = MibTableColumn
nhrpClientResolutionRequestRetries = _NhrpClientResolutionRequestRetries_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 9),
    _NhrpClientResolutionRequestRetries_Type()
)
nhrpClientResolutionRequestRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientResolutionRequestRetries.setStatus("current")


class _NhrpClientPurgeRequestRetries_Type(Integer32):
    """Custom type nhrpClientPurgeRequestRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NhrpClientPurgeRequestRetries_Type.__name__ = "Integer32"
_NhrpClientPurgeRequestRetries_Object = MibTableColumn
nhrpClientPurgeRequestRetries = _NhrpClientPurgeRequestRetries_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 10),
    _NhrpClientPurgeRequestRetries_Type()
)
nhrpClientPurgeRequestRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientPurgeRequestRetries.setStatus("current")


class _NhrpClientDefaultMtu_Type(Unsigned32):
    """Custom type nhrpClientDefaultMtu based on Unsigned32"""
    defaultValue = 9180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NhrpClientDefaultMtu_Type.__name__ = "Unsigned32"
_NhrpClientDefaultMtu_Object = MibTableColumn
nhrpClientDefaultMtu = _NhrpClientDefaultMtu_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 11),
    _NhrpClientDefaultMtu_Type()
)
nhrpClientDefaultMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientDefaultMtu.setStatus("current")


class _NhrpClientHoldTime_Type(Unsigned32):
    """Custom type nhrpClientHoldTime based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NhrpClientHoldTime_Type.__name__ = "Unsigned32"
_NhrpClientHoldTime_Object = MibTableColumn
nhrpClientHoldTime = _NhrpClientHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 12),
    _NhrpClientHoldTime_Type()
)
nhrpClientHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    nhrpClientHoldTime.setUnits("seconds")
_NhrpClientRequestID_Type = Unsigned32
_NhrpClientRequestID_Object = MibTableColumn
nhrpClientRequestID = _NhrpClientRequestID_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 13),
    _NhrpClientRequestID_Type()
)
nhrpClientRequestID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientRequestID.setStatus("current")


class _NhrpClientStorageType_Type(StorageType):
    """Custom type nhrpClientStorageType based on StorageType"""


_NhrpClientStorageType_Object = MibTableColumn
nhrpClientStorageType = _NhrpClientStorageType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 14),
    _NhrpClientStorageType_Type()
)
nhrpClientStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientStorageType.setStatus("current")
_NhrpClientRowStatus_Type = RowStatus
_NhrpClientRowStatus_Object = MibTableColumn
nhrpClientRowStatus = _NhrpClientRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 1, 1, 15),
    _NhrpClientRowStatus_Type()
)
nhrpClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientRowStatus.setStatus("current")
_NhrpClientRegistrationTable_Object = MibTable
nhrpClientRegistrationTable = _NhrpClientRegistrationTable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 2)
)
if mibBuilder.loadTexts:
    nhrpClientRegistrationTable.setStatus("current")
_NhrpClientRegistrationEntry_Object = MibTableRow
nhrpClientRegistrationEntry = _NhrpClientRegistrationEntry_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 2, 1)
)
nhrpClientRegistrationEntry.setIndexNames(
    (0, "NHRP-MIB", "nhrpClientIndex"),
    (0, "NHRP-MIB", "nhrpClientRegIndex"),
)
if mibBuilder.loadTexts:
    nhrpClientRegistrationEntry.setStatus("current")


class _NhrpClientRegIndex_Type(Unsigned32):
    """Custom type nhrpClientRegIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NhrpClientRegIndex_Type.__name__ = "Unsigned32"
_NhrpClientRegIndex_Object = MibTableColumn
nhrpClientRegIndex = _NhrpClientRegIndex_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 2, 1, 1),
    _NhrpClientRegIndex_Type()
)
nhrpClientRegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhrpClientRegIndex.setStatus("current")


class _NhrpClientRegUniqueness_Type(Integer32):
    """Custom type nhrpClientRegUniqueness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("requestNotUnique", 2),
          ("requestUnique", 1))
    )


_NhrpClientRegUniqueness_Type.__name__ = "Integer32"
_NhrpClientRegUniqueness_Object = MibTableColumn
nhrpClientRegUniqueness = _NhrpClientRegUniqueness_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 2, 1, 2),
    _NhrpClientRegUniqueness_Type()
)
nhrpClientRegUniqueness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientRegUniqueness.setStatus("current")


class _NhrpClientRegState_Type(Integer32):
    """Custom type nhrpClientRegState based on Integer32"""
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
        *(("ackRegisterReply", 3),
          ("nakRegisterReply", 4),
          ("other", 1),
          ("registering", 2))
    )


_NhrpClientRegState_Type.__name__ = "Integer32"
_NhrpClientRegState_Object = MibTableColumn
nhrpClientRegState = _NhrpClientRegState_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 2, 1, 3),
    _NhrpClientRegState_Type()
)
nhrpClientRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientRegState.setStatus("current")
_NhrpClientRegRowStatus_Type = RowStatus
_NhrpClientRegRowStatus_Object = MibTableColumn
nhrpClientRegRowStatus = _NhrpClientRegRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 2, 1, 4),
    _NhrpClientRegRowStatus_Type()
)
nhrpClientRegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientRegRowStatus.setStatus("current")
_NhrpClientNhsTable_Object = MibTable
nhrpClientNhsTable = _NhrpClientNhsTable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 3)
)
if mibBuilder.loadTexts:
    nhrpClientNhsTable.setStatus("current")
_NhrpClientNhsEntry_Object = MibTableRow
nhrpClientNhsEntry = _NhrpClientNhsEntry_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 3, 1)
)
nhrpClientNhsEntry.setIndexNames(
    (0, "NHRP-MIB", "nhrpClientIndex"),
    (0, "NHRP-MIB", "nhrpClientNhsIndex"),
)
if mibBuilder.loadTexts:
    nhrpClientNhsEntry.setStatus("current")


class _NhrpClientNhsIndex_Type(Unsigned32):
    """Custom type nhrpClientNhsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NhrpClientNhsIndex_Type.__name__ = "Unsigned32"
_NhrpClientNhsIndex_Object = MibTableColumn
nhrpClientNhsIndex = _NhrpClientNhsIndex_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 3, 1, 1),
    _NhrpClientNhsIndex_Type()
)
nhrpClientNhsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhrpClientNhsIndex.setStatus("current")
_NhrpClientNhsInternetworkAddrType_Type = AddressFamilyNumbers
_NhrpClientNhsInternetworkAddrType_Object = MibTableColumn
nhrpClientNhsInternetworkAddrType = _NhrpClientNhsInternetworkAddrType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 3, 1, 2),
    _NhrpClientNhsInternetworkAddrType_Type()
)
nhrpClientNhsInternetworkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientNhsInternetworkAddrType.setStatus("current")
_NhrpClientNhsInternetworkAddr_Type = NhrpGenAddr
_NhrpClientNhsInternetworkAddr_Object = MibTableColumn
nhrpClientNhsInternetworkAddr = _NhrpClientNhsInternetworkAddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 3, 1, 3),
    _NhrpClientNhsInternetworkAddr_Type()
)
nhrpClientNhsInternetworkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientNhsInternetworkAddr.setStatus("current")
_NhrpClientNhsNbmaAddrType_Type = AddressFamilyNumbers
_NhrpClientNhsNbmaAddrType_Object = MibTableColumn
nhrpClientNhsNbmaAddrType = _NhrpClientNhsNbmaAddrType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 3, 1, 4),
    _NhrpClientNhsNbmaAddrType_Type()
)
nhrpClientNhsNbmaAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientNhsNbmaAddrType.setStatus("current")
_NhrpClientNhsNbmaAddr_Type = NhrpGenAddr
_NhrpClientNhsNbmaAddr_Object = MibTableColumn
nhrpClientNhsNbmaAddr = _NhrpClientNhsNbmaAddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 3, 1, 5),
    _NhrpClientNhsNbmaAddr_Type()
)
nhrpClientNhsNbmaAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientNhsNbmaAddr.setStatus("current")
_NhrpClientNhsNbmaSubaddr_Type = NhrpGenAddr
_NhrpClientNhsNbmaSubaddr_Object = MibTableColumn
nhrpClientNhsNbmaSubaddr = _NhrpClientNhsNbmaSubaddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 3, 1, 6),
    _NhrpClientNhsNbmaSubaddr_Type()
)
nhrpClientNhsNbmaSubaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientNhsNbmaSubaddr.setStatus("current")
_NhrpClientNhsInUse_Type = TruthValue
_NhrpClientNhsInUse_Object = MibTableColumn
nhrpClientNhsInUse = _NhrpClientNhsInUse_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 3, 1, 7),
    _NhrpClientNhsInUse_Type()
)
nhrpClientNhsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientNhsInUse.setStatus("current")
_NhrpClientNhsRowStatus_Type = RowStatus
_NhrpClientNhsRowStatus_Object = MibTableColumn
nhrpClientNhsRowStatus = _NhrpClientNhsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 3, 1, 8),
    _NhrpClientNhsRowStatus_Type()
)
nhrpClientNhsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpClientNhsRowStatus.setStatus("current")
_NhrpClientStatTable_Object = MibTable
nhrpClientStatTable = _NhrpClientStatTable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4)
)
if mibBuilder.loadTexts:
    nhrpClientStatTable.setStatus("current")
_NhrpClientStatEntry_Object = MibTableRow
nhrpClientStatEntry = _NhrpClientStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1)
)
nhrpClientStatEntry.setIndexNames(
    (0, "NHRP-MIB", "nhrpClientIndex"),
)
if mibBuilder.loadTexts:
    nhrpClientStatEntry.setStatus("current")
_NhrpClientStatTxResolveReq_Type = Counter32
_NhrpClientStatTxResolveReq_Object = MibTableColumn
nhrpClientStatTxResolveReq = _NhrpClientStatTxResolveReq_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 1),
    _NhrpClientStatTxResolveReq_Type()
)
nhrpClientStatTxResolveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatTxResolveReq.setStatus("current")
_NhrpClientStatRxResolveReplyAck_Type = Counter32
_NhrpClientStatRxResolveReplyAck_Object = MibTableColumn
nhrpClientStatRxResolveReplyAck = _NhrpClientStatRxResolveReplyAck_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 2),
    _NhrpClientStatRxResolveReplyAck_Type()
)
nhrpClientStatRxResolveReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxResolveReplyAck.setStatus("current")
_NhrpClientStatRxResolveReplyNakProhibited_Type = Counter32
_NhrpClientStatRxResolveReplyNakProhibited_Object = MibTableColumn
nhrpClientStatRxResolveReplyNakProhibited = _NhrpClientStatRxResolveReplyNakProhibited_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 3),
    _NhrpClientStatRxResolveReplyNakProhibited_Type()
)
nhrpClientStatRxResolveReplyNakProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxResolveReplyNakProhibited.setStatus("current")
_NhrpClientStatRxResolveReplyNakInsufResources_Type = Counter32
_NhrpClientStatRxResolveReplyNakInsufResources_Object = MibTableColumn
nhrpClientStatRxResolveReplyNakInsufResources = _NhrpClientStatRxResolveReplyNakInsufResources_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 4),
    _NhrpClientStatRxResolveReplyNakInsufResources_Type()
)
nhrpClientStatRxResolveReplyNakInsufResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxResolveReplyNakInsufResources.setStatus("current")
_NhrpClientStatRxResolveReplyNakNoBinding_Type = Counter32
_NhrpClientStatRxResolveReplyNakNoBinding_Object = MibTableColumn
nhrpClientStatRxResolveReplyNakNoBinding = _NhrpClientStatRxResolveReplyNakNoBinding_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 5),
    _NhrpClientStatRxResolveReplyNakNoBinding_Type()
)
nhrpClientStatRxResolveReplyNakNoBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxResolveReplyNakNoBinding.setStatus("current")
_NhrpClientStatRxResolveReplyNakNotUnique_Type = Counter32
_NhrpClientStatRxResolveReplyNakNotUnique_Object = MibTableColumn
nhrpClientStatRxResolveReplyNakNotUnique = _NhrpClientStatRxResolveReplyNakNotUnique_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 6),
    _NhrpClientStatRxResolveReplyNakNotUnique_Type()
)
nhrpClientStatRxResolveReplyNakNotUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxResolveReplyNakNotUnique.setStatus("current")
_NhrpClientStatTxRegisterReq_Type = Counter32
_NhrpClientStatTxRegisterReq_Object = MibTableColumn
nhrpClientStatTxRegisterReq = _NhrpClientStatTxRegisterReq_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 7),
    _NhrpClientStatTxRegisterReq_Type()
)
nhrpClientStatTxRegisterReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatTxRegisterReq.setStatus("current")
_NhrpClientStatRxRegisterAck_Type = Counter32
_NhrpClientStatRxRegisterAck_Object = MibTableColumn
nhrpClientStatRxRegisterAck = _NhrpClientStatRxRegisterAck_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 8),
    _NhrpClientStatRxRegisterAck_Type()
)
nhrpClientStatRxRegisterAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxRegisterAck.setStatus("current")
_NhrpClientStatRxRegisterNakProhibited_Type = Counter32
_NhrpClientStatRxRegisterNakProhibited_Object = MibTableColumn
nhrpClientStatRxRegisterNakProhibited = _NhrpClientStatRxRegisterNakProhibited_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 9),
    _NhrpClientStatRxRegisterNakProhibited_Type()
)
nhrpClientStatRxRegisterNakProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxRegisterNakProhibited.setStatus("current")
_NhrpClientStatRxRegisterNakInsufResources_Type = Counter32
_NhrpClientStatRxRegisterNakInsufResources_Object = MibTableColumn
nhrpClientStatRxRegisterNakInsufResources = _NhrpClientStatRxRegisterNakInsufResources_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 10),
    _NhrpClientStatRxRegisterNakInsufResources_Type()
)
nhrpClientStatRxRegisterNakInsufResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxRegisterNakInsufResources.setStatus("current")
_NhrpClientStatRxRegisterNakAlreadyReg_Type = Counter32
_NhrpClientStatRxRegisterNakAlreadyReg_Object = MibTableColumn
nhrpClientStatRxRegisterNakAlreadyReg = _NhrpClientStatRxRegisterNakAlreadyReg_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 11),
    _NhrpClientStatRxRegisterNakAlreadyReg_Type()
)
nhrpClientStatRxRegisterNakAlreadyReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxRegisterNakAlreadyReg.setStatus("current")
_NhrpClientStatRxPurgeReq_Type = Counter32
_NhrpClientStatRxPurgeReq_Object = MibTableColumn
nhrpClientStatRxPurgeReq = _NhrpClientStatRxPurgeReq_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 12),
    _NhrpClientStatRxPurgeReq_Type()
)
nhrpClientStatRxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxPurgeReq.setStatus("current")
_NhrpClientStatTxPurgeReq_Type = Counter32
_NhrpClientStatTxPurgeReq_Object = MibTableColumn
nhrpClientStatTxPurgeReq = _NhrpClientStatTxPurgeReq_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 13),
    _NhrpClientStatTxPurgeReq_Type()
)
nhrpClientStatTxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatTxPurgeReq.setStatus("current")
_NhrpClientStatRxPurgeReply_Type = Counter32
_NhrpClientStatRxPurgeReply_Object = MibTableColumn
nhrpClientStatRxPurgeReply = _NhrpClientStatRxPurgeReply_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 14),
    _NhrpClientStatRxPurgeReply_Type()
)
nhrpClientStatRxPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxPurgeReply.setStatus("current")
_NhrpClientStatTxPurgeReply_Type = Counter32
_NhrpClientStatTxPurgeReply_Object = MibTableColumn
nhrpClientStatTxPurgeReply = _NhrpClientStatTxPurgeReply_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 15),
    _NhrpClientStatTxPurgeReply_Type()
)
nhrpClientStatTxPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatTxPurgeReply.setStatus("current")
_NhrpClientStatTxErrorIndication_Type = Counter32
_NhrpClientStatTxErrorIndication_Object = MibTableColumn
nhrpClientStatTxErrorIndication = _NhrpClientStatTxErrorIndication_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 16),
    _NhrpClientStatTxErrorIndication_Type()
)
nhrpClientStatTxErrorIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatTxErrorIndication.setStatus("current")
_NhrpClientStatRxErrUnrecognizedExtension_Type = Counter32
_NhrpClientStatRxErrUnrecognizedExtension_Object = MibTableColumn
nhrpClientStatRxErrUnrecognizedExtension = _NhrpClientStatRxErrUnrecognizedExtension_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 17),
    _NhrpClientStatRxErrUnrecognizedExtension_Type()
)
nhrpClientStatRxErrUnrecognizedExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxErrUnrecognizedExtension.setStatus("current")
_NhrpClientStatRxErrLoopDetected_Type = Counter32
_NhrpClientStatRxErrLoopDetected_Object = MibTableColumn
nhrpClientStatRxErrLoopDetected = _NhrpClientStatRxErrLoopDetected_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 18),
    _NhrpClientStatRxErrLoopDetected_Type()
)
nhrpClientStatRxErrLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxErrLoopDetected.setStatus("current")
_NhrpClientStatRxErrProtoAddrUnreachable_Type = Counter32
_NhrpClientStatRxErrProtoAddrUnreachable_Object = MibTableColumn
nhrpClientStatRxErrProtoAddrUnreachable = _NhrpClientStatRxErrProtoAddrUnreachable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 19),
    _NhrpClientStatRxErrProtoAddrUnreachable_Type()
)
nhrpClientStatRxErrProtoAddrUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxErrProtoAddrUnreachable.setStatus("current")
_NhrpClientStatRxErrProtoError_Type = Counter32
_NhrpClientStatRxErrProtoError_Object = MibTableColumn
nhrpClientStatRxErrProtoError = _NhrpClientStatRxErrProtoError_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 20),
    _NhrpClientStatRxErrProtoError_Type()
)
nhrpClientStatRxErrProtoError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxErrProtoError.setStatus("current")
_NhrpClientStatRxErrSduSizeExceeded_Type = Counter32
_NhrpClientStatRxErrSduSizeExceeded_Object = MibTableColumn
nhrpClientStatRxErrSduSizeExceeded = _NhrpClientStatRxErrSduSizeExceeded_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 21),
    _NhrpClientStatRxErrSduSizeExceeded_Type()
)
nhrpClientStatRxErrSduSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxErrSduSizeExceeded.setStatus("current")
_NhrpClientStatRxErrInvalidExtension_Type = Counter32
_NhrpClientStatRxErrInvalidExtension_Object = MibTableColumn
nhrpClientStatRxErrInvalidExtension = _NhrpClientStatRxErrInvalidExtension_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 22),
    _NhrpClientStatRxErrInvalidExtension_Type()
)
nhrpClientStatRxErrInvalidExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxErrInvalidExtension.setStatus("current")
_NhrpClientStatRxErrAuthenticationFailure_Type = Counter32
_NhrpClientStatRxErrAuthenticationFailure_Object = MibTableColumn
nhrpClientStatRxErrAuthenticationFailure = _NhrpClientStatRxErrAuthenticationFailure_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 23),
    _NhrpClientStatRxErrAuthenticationFailure_Type()
)
nhrpClientStatRxErrAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxErrAuthenticationFailure.setStatus("current")
_NhrpClientStatRxErrHopCountExceeded_Type = Counter32
_NhrpClientStatRxErrHopCountExceeded_Object = MibTableColumn
nhrpClientStatRxErrHopCountExceeded = _NhrpClientStatRxErrHopCountExceeded_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 24),
    _NhrpClientStatRxErrHopCountExceeded_Type()
)
nhrpClientStatRxErrHopCountExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatRxErrHopCountExceeded.setStatus("current")
_NhrpClientStatDiscontinuityTime_Type = TimeStamp
_NhrpClientStatDiscontinuityTime_Object = MibTableColumn
nhrpClientStatDiscontinuityTime = _NhrpClientStatDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 2, 4, 1, 25),
    _NhrpClientStatDiscontinuityTime_Type()
)
nhrpClientStatDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpClientStatDiscontinuityTime.setStatus("current")
_NhrpServerObjects_ObjectIdentity = ObjectIdentity
nhrpServerObjects = _NhrpServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 71, 1, 3)
)
_NhrpServerTable_Object = MibTable
nhrpServerTable = _NhrpServerTable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nhrpServerTable.setStatus("current")
_NhrpServerEntry_Object = MibTableRow
nhrpServerEntry = _NhrpServerEntry_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 1, 1)
)
nhrpServerEntry.setIndexNames(
    (0, "NHRP-MIB", "nhrpServerIndex"),
)
if mibBuilder.loadTexts:
    nhrpServerEntry.setStatus("current")


class _NhrpServerIndex_Type(Unsigned32):
    """Custom type nhrpServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NhrpServerIndex_Type.__name__ = "Unsigned32"
_NhrpServerIndex_Object = MibTableColumn
nhrpServerIndex = _NhrpServerIndex_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 1, 1, 1),
    _NhrpServerIndex_Type()
)
nhrpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhrpServerIndex.setStatus("current")
_NhrpServerInternetworkAddrType_Type = AddressFamilyNumbers
_NhrpServerInternetworkAddrType_Object = MibTableColumn
nhrpServerInternetworkAddrType = _NhrpServerInternetworkAddrType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 1, 1, 2),
    _NhrpServerInternetworkAddrType_Type()
)
nhrpServerInternetworkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerInternetworkAddrType.setStatus("current")
_NhrpServerInternetworkAddr_Type = NhrpGenAddr
_NhrpServerInternetworkAddr_Object = MibTableColumn
nhrpServerInternetworkAddr = _NhrpServerInternetworkAddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 1, 1, 3),
    _NhrpServerInternetworkAddr_Type()
)
nhrpServerInternetworkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerInternetworkAddr.setStatus("current")
_NhrpServerNbmaAddrType_Type = AddressFamilyNumbers
_NhrpServerNbmaAddrType_Object = MibTableColumn
nhrpServerNbmaAddrType = _NhrpServerNbmaAddrType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 1, 1, 4),
    _NhrpServerNbmaAddrType_Type()
)
nhrpServerNbmaAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerNbmaAddrType.setStatus("current")
_NhrpServerNbmaAddr_Type = NhrpGenAddr
_NhrpServerNbmaAddr_Object = MibTableColumn
nhrpServerNbmaAddr = _NhrpServerNbmaAddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 1, 1, 5),
    _NhrpServerNbmaAddr_Type()
)
nhrpServerNbmaAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerNbmaAddr.setStatus("current")
_NhrpServerNbmaSubaddr_Type = NhrpGenAddr
_NhrpServerNbmaSubaddr_Object = MibTableColumn
nhrpServerNbmaSubaddr = _NhrpServerNbmaSubaddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 1, 1, 6),
    _NhrpServerNbmaSubaddr_Type()
)
nhrpServerNbmaSubaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerNbmaSubaddr.setStatus("current")


class _NhrpServerStorageType_Type(StorageType):
    """Custom type nhrpServerStorageType based on StorageType"""


_NhrpServerStorageType_Object = MibTableColumn
nhrpServerStorageType = _NhrpServerStorageType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 1, 1, 7),
    _NhrpServerStorageType_Type()
)
nhrpServerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerStorageType.setStatus("current")
_NhrpServerRowStatus_Type = RowStatus
_NhrpServerRowStatus_Object = MibTableColumn
nhrpServerRowStatus = _NhrpServerRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 1, 1, 8),
    _NhrpServerRowStatus_Type()
)
nhrpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerRowStatus.setStatus("current")
_NhrpServerCacheTable_Object = MibTable
nhrpServerCacheTable = _NhrpServerCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 2)
)
if mibBuilder.loadTexts:
    nhrpServerCacheTable.setStatus("current")
_NhrpServerCacheEntry_Object = MibTableRow
nhrpServerCacheEntry = _NhrpServerCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 2, 1)
)
nhrpServerCacheEntry.setIndexNames(
    (0, "NHRP-MIB", "nhrpCacheInternetworkAddrType"),
    (0, "NHRP-MIB", "nhrpCacheInternetworkAddr"),
    (0, "IF-MIB", "ifIndex"),
    (0, "NHRP-MIB", "nhrpCacheIndex"),
)
if mibBuilder.loadTexts:
    nhrpServerCacheEntry.setStatus("current")
_NhrpServerCacheAuthoritative_Type = TruthValue
_NhrpServerCacheAuthoritative_Object = MibTableColumn
nhrpServerCacheAuthoritative = _NhrpServerCacheAuthoritative_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 2, 1, 1),
    _NhrpServerCacheAuthoritative_Type()
)
nhrpServerCacheAuthoritative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerCacheAuthoritative.setStatus("current")
_NhrpServerCacheUniqueness_Type = TruthValue
_NhrpServerCacheUniqueness_Object = MibTableColumn
nhrpServerCacheUniqueness = _NhrpServerCacheUniqueness_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 2, 1, 2),
    _NhrpServerCacheUniqueness_Type()
)
nhrpServerCacheUniqueness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerCacheUniqueness.setStatus("current")
_NhrpServerNhcTable_Object = MibTable
nhrpServerNhcTable = _NhrpServerNhcTable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 3)
)
if mibBuilder.loadTexts:
    nhrpServerNhcTable.setStatus("current")
_NhrpServerNhcEntry_Object = MibTableRow
nhrpServerNhcEntry = _NhrpServerNhcEntry_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 3, 1)
)
nhrpServerNhcEntry.setIndexNames(
    (0, "NHRP-MIB", "nhrpServerIndex"),
    (0, "NHRP-MIB", "nhrpServerNhcIndex"),
)
if mibBuilder.loadTexts:
    nhrpServerNhcEntry.setStatus("current")


class _NhrpServerNhcIndex_Type(Unsigned32):
    """Custom type nhrpServerNhcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NhrpServerNhcIndex_Type.__name__ = "Unsigned32"
_NhrpServerNhcIndex_Object = MibTableColumn
nhrpServerNhcIndex = _NhrpServerNhcIndex_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 3, 1, 1),
    _NhrpServerNhcIndex_Type()
)
nhrpServerNhcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhrpServerNhcIndex.setStatus("current")


class _NhrpServerNhcPrefixLength_Type(Integer32):
    """Custom type nhrpServerNhcPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NhrpServerNhcPrefixLength_Type.__name__ = "Integer32"
_NhrpServerNhcPrefixLength_Object = MibTableColumn
nhrpServerNhcPrefixLength = _NhrpServerNhcPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 3, 1, 2),
    _NhrpServerNhcPrefixLength_Type()
)
nhrpServerNhcPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerNhcPrefixLength.setStatus("current")
_NhrpServerNhcInternetworkAddrType_Type = AddressFamilyNumbers
_NhrpServerNhcInternetworkAddrType_Object = MibTableColumn
nhrpServerNhcInternetworkAddrType = _NhrpServerNhcInternetworkAddrType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 3, 1, 3),
    _NhrpServerNhcInternetworkAddrType_Type()
)
nhrpServerNhcInternetworkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerNhcInternetworkAddrType.setStatus("current")
_NhrpServerNhcInternetworkAddr_Type = NhrpGenAddr
_NhrpServerNhcInternetworkAddr_Object = MibTableColumn
nhrpServerNhcInternetworkAddr = _NhrpServerNhcInternetworkAddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 3, 1, 4),
    _NhrpServerNhcInternetworkAddr_Type()
)
nhrpServerNhcInternetworkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerNhcInternetworkAddr.setStatus("current")
_NhrpServerNhcNbmaAddrType_Type = AddressFamilyNumbers
_NhrpServerNhcNbmaAddrType_Object = MibTableColumn
nhrpServerNhcNbmaAddrType = _NhrpServerNhcNbmaAddrType_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 3, 1, 5),
    _NhrpServerNhcNbmaAddrType_Type()
)
nhrpServerNhcNbmaAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerNhcNbmaAddrType.setStatus("current")
_NhrpServerNhcNbmaAddr_Type = NhrpGenAddr
_NhrpServerNhcNbmaAddr_Object = MibTableColumn
nhrpServerNhcNbmaAddr = _NhrpServerNhcNbmaAddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 3, 1, 6),
    _NhrpServerNhcNbmaAddr_Type()
)
nhrpServerNhcNbmaAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerNhcNbmaAddr.setStatus("current")
_NhrpServerNhcNbmaSubaddr_Type = NhrpGenAddr
_NhrpServerNhcNbmaSubaddr_Object = MibTableColumn
nhrpServerNhcNbmaSubaddr = _NhrpServerNhcNbmaSubaddr_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 3, 1, 7),
    _NhrpServerNhcNbmaSubaddr_Type()
)
nhrpServerNhcNbmaSubaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerNhcNbmaSubaddr.setStatus("current")
_NhrpServerNhcInUse_Type = TruthValue
_NhrpServerNhcInUse_Object = MibTableColumn
nhrpServerNhcInUse = _NhrpServerNhcInUse_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 3, 1, 8),
    _NhrpServerNhcInUse_Type()
)
nhrpServerNhcInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerNhcInUse.setStatus("current")
_NhrpServerNhcRowStatus_Type = RowStatus
_NhrpServerNhcRowStatus_Object = MibTableColumn
nhrpServerNhcRowStatus = _NhrpServerNhcRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 3, 1, 9),
    _NhrpServerNhcRowStatus_Type()
)
nhrpServerNhcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhrpServerNhcRowStatus.setStatus("current")
_NhrpServerStatTable_Object = MibTable
nhrpServerStatTable = _NhrpServerStatTable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4)
)
if mibBuilder.loadTexts:
    nhrpServerStatTable.setStatus("current")
_NhrpServerStatEntry_Object = MibTableRow
nhrpServerStatEntry = _NhrpServerStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1)
)
nhrpServerStatEntry.setIndexNames(
    (0, "NHRP-MIB", "nhrpServerIndex"),
)
if mibBuilder.loadTexts:
    nhrpServerStatEntry.setStatus("current")
_NhrpServerStatRxResolveReq_Type = Counter32
_NhrpServerStatRxResolveReq_Object = MibTableColumn
nhrpServerStatRxResolveReq = _NhrpServerStatRxResolveReq_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 1),
    _NhrpServerStatRxResolveReq_Type()
)
nhrpServerStatRxResolveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxResolveReq.setStatus("current")
_NhrpServerStatTxResolveReplyAck_Type = Counter32
_NhrpServerStatTxResolveReplyAck_Object = MibTableColumn
nhrpServerStatTxResolveReplyAck = _NhrpServerStatTxResolveReplyAck_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 2),
    _NhrpServerStatTxResolveReplyAck_Type()
)
nhrpServerStatTxResolveReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxResolveReplyAck.setStatus("current")
_NhrpServerStatTxResolveReplyNakProhibited_Type = Counter32
_NhrpServerStatTxResolveReplyNakProhibited_Object = MibTableColumn
nhrpServerStatTxResolveReplyNakProhibited = _NhrpServerStatTxResolveReplyNakProhibited_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 3),
    _NhrpServerStatTxResolveReplyNakProhibited_Type()
)
nhrpServerStatTxResolveReplyNakProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxResolveReplyNakProhibited.setStatus("current")
_NhrpServerStatTxResolveReplyNakInsufResources_Type = Counter32
_NhrpServerStatTxResolveReplyNakInsufResources_Object = MibTableColumn
nhrpServerStatTxResolveReplyNakInsufResources = _NhrpServerStatTxResolveReplyNakInsufResources_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 4),
    _NhrpServerStatTxResolveReplyNakInsufResources_Type()
)
nhrpServerStatTxResolveReplyNakInsufResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxResolveReplyNakInsufResources.setStatus("current")
_NhrpServerStatTxResolveReplyNakNoBinding_Type = Counter32
_NhrpServerStatTxResolveReplyNakNoBinding_Object = MibTableColumn
nhrpServerStatTxResolveReplyNakNoBinding = _NhrpServerStatTxResolveReplyNakNoBinding_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 5),
    _NhrpServerStatTxResolveReplyNakNoBinding_Type()
)
nhrpServerStatTxResolveReplyNakNoBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxResolveReplyNakNoBinding.setStatus("current")
_NhrpServerStatTxResolveReplyNakNotUnique_Type = Counter32
_NhrpServerStatTxResolveReplyNakNotUnique_Object = MibTableColumn
nhrpServerStatTxResolveReplyNakNotUnique = _NhrpServerStatTxResolveReplyNakNotUnique_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 6),
    _NhrpServerStatTxResolveReplyNakNotUnique_Type()
)
nhrpServerStatTxResolveReplyNakNotUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxResolveReplyNakNotUnique.setStatus("current")
_NhrpServerStatRxRegisterReq_Type = Counter32
_NhrpServerStatRxRegisterReq_Object = MibTableColumn
nhrpServerStatRxRegisterReq = _NhrpServerStatRxRegisterReq_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 7),
    _NhrpServerStatRxRegisterReq_Type()
)
nhrpServerStatRxRegisterReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxRegisterReq.setStatus("current")
_NhrpServerStatTxRegisterAck_Type = Counter32
_NhrpServerStatTxRegisterAck_Object = MibTableColumn
nhrpServerStatTxRegisterAck = _NhrpServerStatTxRegisterAck_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 8),
    _NhrpServerStatTxRegisterAck_Type()
)
nhrpServerStatTxRegisterAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxRegisterAck.setStatus("current")
_NhrpServerStatTxRegisterNakProhibited_Type = Counter32
_NhrpServerStatTxRegisterNakProhibited_Object = MibTableColumn
nhrpServerStatTxRegisterNakProhibited = _NhrpServerStatTxRegisterNakProhibited_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 9),
    _NhrpServerStatTxRegisterNakProhibited_Type()
)
nhrpServerStatTxRegisterNakProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxRegisterNakProhibited.setStatus("current")
_NhrpServerStatTxRegisterNakInsufResources_Type = Counter32
_NhrpServerStatTxRegisterNakInsufResources_Object = MibTableColumn
nhrpServerStatTxRegisterNakInsufResources = _NhrpServerStatTxRegisterNakInsufResources_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 10),
    _NhrpServerStatTxRegisterNakInsufResources_Type()
)
nhrpServerStatTxRegisterNakInsufResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxRegisterNakInsufResources.setStatus("current")
_NhrpServerStatTxRegisterNakAlreadyReg_Type = Counter32
_NhrpServerStatTxRegisterNakAlreadyReg_Object = MibTableColumn
nhrpServerStatTxRegisterNakAlreadyReg = _NhrpServerStatTxRegisterNakAlreadyReg_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 11),
    _NhrpServerStatTxRegisterNakAlreadyReg_Type()
)
nhrpServerStatTxRegisterNakAlreadyReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxRegisterNakAlreadyReg.setStatus("current")
_NhrpServerStatRxPurgeReq_Type = Counter32
_NhrpServerStatRxPurgeReq_Object = MibTableColumn
nhrpServerStatRxPurgeReq = _NhrpServerStatRxPurgeReq_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 12),
    _NhrpServerStatRxPurgeReq_Type()
)
nhrpServerStatRxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxPurgeReq.setStatus("current")
_NhrpServerStatTxPurgeReq_Type = Counter32
_NhrpServerStatTxPurgeReq_Object = MibTableColumn
nhrpServerStatTxPurgeReq = _NhrpServerStatTxPurgeReq_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 13),
    _NhrpServerStatTxPurgeReq_Type()
)
nhrpServerStatTxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxPurgeReq.setStatus("current")
_NhrpServerStatRxPurgeReply_Type = Counter32
_NhrpServerStatRxPurgeReply_Object = MibTableColumn
nhrpServerStatRxPurgeReply = _NhrpServerStatRxPurgeReply_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 14),
    _NhrpServerStatRxPurgeReply_Type()
)
nhrpServerStatRxPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxPurgeReply.setStatus("current")
_NhrpServerStatTxPurgeReply_Type = Counter32
_NhrpServerStatTxPurgeReply_Object = MibTableColumn
nhrpServerStatTxPurgeReply = _NhrpServerStatTxPurgeReply_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 15),
    _NhrpServerStatTxPurgeReply_Type()
)
nhrpServerStatTxPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxPurgeReply.setStatus("current")
_NhrpServerStatRxErrUnrecognizedExtension_Type = Counter32
_NhrpServerStatRxErrUnrecognizedExtension_Object = MibTableColumn
nhrpServerStatRxErrUnrecognizedExtension = _NhrpServerStatRxErrUnrecognizedExtension_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 16),
    _NhrpServerStatRxErrUnrecognizedExtension_Type()
)
nhrpServerStatRxErrUnrecognizedExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxErrUnrecognizedExtension.setStatus("current")
_NhrpServerStatRxErrLoopDetected_Type = Counter32
_NhrpServerStatRxErrLoopDetected_Object = MibTableColumn
nhrpServerStatRxErrLoopDetected = _NhrpServerStatRxErrLoopDetected_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 17),
    _NhrpServerStatRxErrLoopDetected_Type()
)
nhrpServerStatRxErrLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxErrLoopDetected.setStatus("current")
_NhrpServerStatRxErrProtoAddrUnreachable_Type = Counter32
_NhrpServerStatRxErrProtoAddrUnreachable_Object = MibTableColumn
nhrpServerStatRxErrProtoAddrUnreachable = _NhrpServerStatRxErrProtoAddrUnreachable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 18),
    _NhrpServerStatRxErrProtoAddrUnreachable_Type()
)
nhrpServerStatRxErrProtoAddrUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxErrProtoAddrUnreachable.setStatus("current")
_NhrpServerStatRxErrProtoError_Type = Counter32
_NhrpServerStatRxErrProtoError_Object = MibTableColumn
nhrpServerStatRxErrProtoError = _NhrpServerStatRxErrProtoError_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 19),
    _NhrpServerStatRxErrProtoError_Type()
)
nhrpServerStatRxErrProtoError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxErrProtoError.setStatus("current")
_NhrpServerStatRxErrSduSizeExceeded_Type = Counter32
_NhrpServerStatRxErrSduSizeExceeded_Object = MibTableColumn
nhrpServerStatRxErrSduSizeExceeded = _NhrpServerStatRxErrSduSizeExceeded_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 20),
    _NhrpServerStatRxErrSduSizeExceeded_Type()
)
nhrpServerStatRxErrSduSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxErrSduSizeExceeded.setStatus("current")
_NhrpServerStatRxErrInvalidExtension_Type = Counter32
_NhrpServerStatRxErrInvalidExtension_Object = MibTableColumn
nhrpServerStatRxErrInvalidExtension = _NhrpServerStatRxErrInvalidExtension_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 21),
    _NhrpServerStatRxErrInvalidExtension_Type()
)
nhrpServerStatRxErrInvalidExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxErrInvalidExtension.setStatus("current")
_NhrpServerStatRxErrInvalidResReplyReceived_Type = Counter32
_NhrpServerStatRxErrInvalidResReplyReceived_Object = MibTableColumn
nhrpServerStatRxErrInvalidResReplyReceived = _NhrpServerStatRxErrInvalidResReplyReceived_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 22),
    _NhrpServerStatRxErrInvalidResReplyReceived_Type()
)
nhrpServerStatRxErrInvalidResReplyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxErrInvalidResReplyReceived.setStatus("current")
_NhrpServerStatRxErrAuthenticationFailure_Type = Counter32
_NhrpServerStatRxErrAuthenticationFailure_Object = MibTableColumn
nhrpServerStatRxErrAuthenticationFailure = _NhrpServerStatRxErrAuthenticationFailure_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 23),
    _NhrpServerStatRxErrAuthenticationFailure_Type()
)
nhrpServerStatRxErrAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxErrAuthenticationFailure.setStatus("current")
_NhrpServerStatRxErrHopCountExceeded_Type = Counter32
_NhrpServerStatRxErrHopCountExceeded_Object = MibTableColumn
nhrpServerStatRxErrHopCountExceeded = _NhrpServerStatRxErrHopCountExceeded_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 24),
    _NhrpServerStatRxErrHopCountExceeded_Type()
)
nhrpServerStatRxErrHopCountExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatRxErrHopCountExceeded.setStatus("current")
_NhrpServerStatTxErrUnrecognizedExtension_Type = Counter32
_NhrpServerStatTxErrUnrecognizedExtension_Object = MibTableColumn
nhrpServerStatTxErrUnrecognizedExtension = _NhrpServerStatTxErrUnrecognizedExtension_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 25),
    _NhrpServerStatTxErrUnrecognizedExtension_Type()
)
nhrpServerStatTxErrUnrecognizedExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxErrUnrecognizedExtension.setStatus("current")
_NhrpServerStatTxErrLoopDetected_Type = Counter32
_NhrpServerStatTxErrLoopDetected_Object = MibTableColumn
nhrpServerStatTxErrLoopDetected = _NhrpServerStatTxErrLoopDetected_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 26),
    _NhrpServerStatTxErrLoopDetected_Type()
)
nhrpServerStatTxErrLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxErrLoopDetected.setStatus("current")
_NhrpServerStatTxErrProtoAddrUnreachable_Type = Counter32
_NhrpServerStatTxErrProtoAddrUnreachable_Object = MibTableColumn
nhrpServerStatTxErrProtoAddrUnreachable = _NhrpServerStatTxErrProtoAddrUnreachable_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 27),
    _NhrpServerStatTxErrProtoAddrUnreachable_Type()
)
nhrpServerStatTxErrProtoAddrUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxErrProtoAddrUnreachable.setStatus("current")
_NhrpServerStatTxErrProtoError_Type = Counter32
_NhrpServerStatTxErrProtoError_Object = MibTableColumn
nhrpServerStatTxErrProtoError = _NhrpServerStatTxErrProtoError_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 28),
    _NhrpServerStatTxErrProtoError_Type()
)
nhrpServerStatTxErrProtoError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxErrProtoError.setStatus("current")
_NhrpServerStatTxErrSduSizeExceeded_Type = Counter32
_NhrpServerStatTxErrSduSizeExceeded_Object = MibTableColumn
nhrpServerStatTxErrSduSizeExceeded = _NhrpServerStatTxErrSduSizeExceeded_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 29),
    _NhrpServerStatTxErrSduSizeExceeded_Type()
)
nhrpServerStatTxErrSduSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxErrSduSizeExceeded.setStatus("current")
_NhrpServerStatTxErrInvalidExtension_Type = Counter32
_NhrpServerStatTxErrInvalidExtension_Object = MibTableColumn
nhrpServerStatTxErrInvalidExtension = _NhrpServerStatTxErrInvalidExtension_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 30),
    _NhrpServerStatTxErrInvalidExtension_Type()
)
nhrpServerStatTxErrInvalidExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxErrInvalidExtension.setStatus("current")
_NhrpServerStatTxErrAuthenticationFailure_Type = Counter32
_NhrpServerStatTxErrAuthenticationFailure_Object = MibTableColumn
nhrpServerStatTxErrAuthenticationFailure = _NhrpServerStatTxErrAuthenticationFailure_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 31),
    _NhrpServerStatTxErrAuthenticationFailure_Type()
)
nhrpServerStatTxErrAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxErrAuthenticationFailure.setStatus("current")
_NhrpServerStatTxErrHopCountExceeded_Type = Counter32
_NhrpServerStatTxErrHopCountExceeded_Object = MibTableColumn
nhrpServerStatTxErrHopCountExceeded = _NhrpServerStatTxErrHopCountExceeded_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 32),
    _NhrpServerStatTxErrHopCountExceeded_Type()
)
nhrpServerStatTxErrHopCountExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatTxErrHopCountExceeded.setStatus("current")
_NhrpServerStatFwResolveReq_Type = Counter32
_NhrpServerStatFwResolveReq_Object = MibTableColumn
nhrpServerStatFwResolveReq = _NhrpServerStatFwResolveReq_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 33),
    _NhrpServerStatFwResolveReq_Type()
)
nhrpServerStatFwResolveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatFwResolveReq.setStatus("current")
_NhrpServerStatFwResolveReply_Type = Counter32
_NhrpServerStatFwResolveReply_Object = MibTableColumn
nhrpServerStatFwResolveReply = _NhrpServerStatFwResolveReply_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 34),
    _NhrpServerStatFwResolveReply_Type()
)
nhrpServerStatFwResolveReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatFwResolveReply.setStatus("current")
_NhrpServerStatFwRegisterReq_Type = Counter32
_NhrpServerStatFwRegisterReq_Object = MibTableColumn
nhrpServerStatFwRegisterReq = _NhrpServerStatFwRegisterReq_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 35),
    _NhrpServerStatFwRegisterReq_Type()
)
nhrpServerStatFwRegisterReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatFwRegisterReq.setStatus("current")
_NhrpServerStatFwRegisterReply_Type = Counter32
_NhrpServerStatFwRegisterReply_Object = MibTableColumn
nhrpServerStatFwRegisterReply = _NhrpServerStatFwRegisterReply_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 36),
    _NhrpServerStatFwRegisterReply_Type()
)
nhrpServerStatFwRegisterReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatFwRegisterReply.setStatus("current")
_NhrpServerStatFwPurgeReq_Type = Counter32
_NhrpServerStatFwPurgeReq_Object = MibTableColumn
nhrpServerStatFwPurgeReq = _NhrpServerStatFwPurgeReq_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 37),
    _NhrpServerStatFwPurgeReq_Type()
)
nhrpServerStatFwPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatFwPurgeReq.setStatus("current")
_NhrpServerStatFwPurgeReply_Type = Counter32
_NhrpServerStatFwPurgeReply_Object = MibTableColumn
nhrpServerStatFwPurgeReply = _NhrpServerStatFwPurgeReply_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 38),
    _NhrpServerStatFwPurgeReply_Type()
)
nhrpServerStatFwPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatFwPurgeReply.setStatus("current")
_NhrpServerStatFwErrorIndication_Type = Counter32
_NhrpServerStatFwErrorIndication_Object = MibTableColumn
nhrpServerStatFwErrorIndication = _NhrpServerStatFwErrorIndication_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 39),
    _NhrpServerStatFwErrorIndication_Type()
)
nhrpServerStatFwErrorIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatFwErrorIndication.setStatus("current")
_NhrpServerStatDiscontinuityTime_Type = TimeStamp
_NhrpServerStatDiscontinuityTime_Object = MibTableColumn
nhrpServerStatDiscontinuityTime = _NhrpServerStatDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 71, 1, 3, 4, 1, 40),
    _NhrpServerStatDiscontinuityTime_Type()
)
nhrpServerStatDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhrpServerStatDiscontinuityTime.setStatus("current")
_NhrpConformance_ObjectIdentity = ObjectIdentity
nhrpConformance = _NhrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 71, 2)
)
_NhrpCompliances_ObjectIdentity = ObjectIdentity
nhrpCompliances = _NhrpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 71, 2, 1)
)
_NhrpGroups_ObjectIdentity = ObjectIdentity
nhrpGroups = _NhrpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 71, 2, 2)
)

# Managed Objects groups

nhrpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 71, 2, 2, 1)
)
nhrpGeneralGroup.setObjects(
      *(("NHRP-MIB", "nhrpNextIndex"),
        ("NHRP-MIB", "nhrpCachePrefixLength"),
        ("NHRP-MIB", "nhrpCacheNextHopInternetworkAddr"),
        ("NHRP-MIB", "nhrpCacheNbmaAddrType"),
        ("NHRP-MIB", "nhrpCacheNbmaAddr"),
        ("NHRP-MIB", "nhrpCacheNbmaSubaddr"),
        ("NHRP-MIB", "nhrpCacheType"),
        ("NHRP-MIB", "nhrpCacheState"),
        ("NHRP-MIB", "nhrpCacheHoldingTimeValid"),
        ("NHRP-MIB", "nhrpCacheHoldingTime"),
        ("NHRP-MIB", "nhrpCacheNegotiatedMtu"),
        ("NHRP-MIB", "nhrpCachePreference"),
        ("NHRP-MIB", "nhrpCacheStorageType"),
        ("NHRP-MIB", "nhrpCacheRowStatus"),
        ("NHRP-MIB", "nhrpPurgeCacheIdentifier"),
        ("NHRP-MIB", "nhrpPurgePrefixLength"),
        ("NHRP-MIB", "nhrpPurgeRequestID"),
        ("NHRP-MIB", "nhrpPurgeReplyExpected"),
        ("NHRP-MIB", "nhrpPurgeRowStatus"))
)
if mibBuilder.loadTexts:
    nhrpGeneralGroup.setStatus("current")

nhrpClientGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 71, 2, 2, 2)
)
nhrpClientGroup.setObjects(
      *(("NHRP-MIB", "nhrpClientInternetworkAddrType"),
        ("NHRP-MIB", "nhrpClientInternetworkAddr"),
        ("NHRP-MIB", "nhrpClientNbmaAddrType"),
        ("NHRP-MIB", "nhrpClientNbmaAddr"),
        ("NHRP-MIB", "nhrpClientNbmaSubaddr"),
        ("NHRP-MIB", "nhrpClientInitialRequestTimeout"),
        ("NHRP-MIB", "nhrpClientRegistrationRequestRetries"),
        ("NHRP-MIB", "nhrpClientResolutionRequestRetries"),
        ("NHRP-MIB", "nhrpClientPurgeRequestRetries"),
        ("NHRP-MIB", "nhrpClientDefaultMtu"),
        ("NHRP-MIB", "nhrpClientHoldTime"),
        ("NHRP-MIB", "nhrpClientRequestID"),
        ("NHRP-MIB", "nhrpClientStorageType"),
        ("NHRP-MIB", "nhrpClientRowStatus"),
        ("NHRP-MIB", "nhrpClientRegUniqueness"),
        ("NHRP-MIB", "nhrpClientRegState"),
        ("NHRP-MIB", "nhrpClientRegRowStatus"),
        ("NHRP-MIB", "nhrpClientNhsInternetworkAddrType"),
        ("NHRP-MIB", "nhrpClientNhsInternetworkAddr"),
        ("NHRP-MIB", "nhrpClientNhsNbmaAddrType"),
        ("NHRP-MIB", "nhrpClientNhsNbmaAddr"),
        ("NHRP-MIB", "nhrpClientNhsNbmaSubaddr"),
        ("NHRP-MIB", "nhrpClientNhsInUse"),
        ("NHRP-MIB", "nhrpClientNhsRowStatus"),
        ("NHRP-MIB", "nhrpClientStatTxResolveReq"),
        ("NHRP-MIB", "nhrpClientStatRxResolveReplyAck"),
        ("NHRP-MIB", "nhrpClientStatRxResolveReplyNakProhibited"),
        ("NHRP-MIB", "nhrpClientStatRxResolveReplyNakInsufResources"),
        ("NHRP-MIB", "nhrpClientStatRxResolveReplyNakNoBinding"),
        ("NHRP-MIB", "nhrpClientStatRxResolveReplyNakNotUnique"),
        ("NHRP-MIB", "nhrpClientStatTxRegisterReq"),
        ("NHRP-MIB", "nhrpClientStatRxRegisterAck"),
        ("NHRP-MIB", "nhrpClientStatRxRegisterNakProhibited"),
        ("NHRP-MIB", "nhrpClientStatRxRegisterNakInsufResources"),
        ("NHRP-MIB", "nhrpClientStatRxRegisterNakAlreadyReg"),
        ("NHRP-MIB", "nhrpClientStatRxPurgeReq"),
        ("NHRP-MIB", "nhrpClientStatTxPurgeReq"),
        ("NHRP-MIB", "nhrpClientStatRxPurgeReply"),
        ("NHRP-MIB", "nhrpClientStatTxPurgeReply"),
        ("NHRP-MIB", "nhrpClientStatTxErrorIndication"),
        ("NHRP-MIB", "nhrpClientStatRxErrUnrecognizedExtension"),
        ("NHRP-MIB", "nhrpClientStatRxErrLoopDetected"),
        ("NHRP-MIB", "nhrpClientStatRxErrProtoAddrUnreachable"),
        ("NHRP-MIB", "nhrpClientStatRxErrProtoError"),
        ("NHRP-MIB", "nhrpClientStatRxErrSduSizeExceeded"),
        ("NHRP-MIB", "nhrpClientStatRxErrInvalidExtension"),
        ("NHRP-MIB", "nhrpClientStatRxErrAuthenticationFailure"),
        ("NHRP-MIB", "nhrpClientStatRxErrHopCountExceeded"),
        ("NHRP-MIB", "nhrpClientStatDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    nhrpClientGroup.setStatus("current")

nhrpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 71, 2, 2, 3)
)
nhrpServerGroup.setObjects(
      *(("NHRP-MIB", "nhrpServerInternetworkAddrType"),
        ("NHRP-MIB", "nhrpServerInternetworkAddr"),
        ("NHRP-MIB", "nhrpServerNbmaAddrType"),
        ("NHRP-MIB", "nhrpServerNbmaAddr"),
        ("NHRP-MIB", "nhrpServerNbmaSubaddr"),
        ("NHRP-MIB", "nhrpServerStorageType"),
        ("NHRP-MIB", "nhrpServerRowStatus"),
        ("NHRP-MIB", "nhrpServerCacheAuthoritative"),
        ("NHRP-MIB", "nhrpServerCacheUniqueness"),
        ("NHRP-MIB", "nhrpServerNhcPrefixLength"),
        ("NHRP-MIB", "nhrpServerNhcInternetworkAddrType"),
        ("NHRP-MIB", "nhrpServerNhcInternetworkAddr"),
        ("NHRP-MIB", "nhrpServerNhcNbmaAddrType"),
        ("NHRP-MIB", "nhrpServerNhcNbmaAddr"),
        ("NHRP-MIB", "nhrpServerNhcNbmaSubaddr"),
        ("NHRP-MIB", "nhrpServerNhcInUse"),
        ("NHRP-MIB", "nhrpServerNhcRowStatus"),
        ("NHRP-MIB", "nhrpServerStatRxResolveReq"),
        ("NHRP-MIB", "nhrpServerStatTxResolveReplyAck"),
        ("NHRP-MIB", "nhrpServerStatTxResolveReplyNakProhibited"),
        ("NHRP-MIB", "nhrpServerStatTxResolveReplyNakInsufResources"),
        ("NHRP-MIB", "nhrpServerStatTxResolveReplyNakNoBinding"),
        ("NHRP-MIB", "nhrpServerStatTxResolveReplyNakNotUnique"),
        ("NHRP-MIB", "nhrpServerStatRxRegisterReq"),
        ("NHRP-MIB", "nhrpServerStatTxRegisterAck"),
        ("NHRP-MIB", "nhrpServerStatTxRegisterNakProhibited"),
        ("NHRP-MIB", "nhrpServerStatTxRegisterNakInsufResources"),
        ("NHRP-MIB", "nhrpServerStatTxRegisterNakAlreadyReg"),
        ("NHRP-MIB", "nhrpServerStatRxPurgeReq"),
        ("NHRP-MIB", "nhrpServerStatTxPurgeReq"),
        ("NHRP-MIB", "nhrpServerStatRxPurgeReply"),
        ("NHRP-MIB", "nhrpServerStatTxPurgeReply"),
        ("NHRP-MIB", "nhrpServerStatRxErrUnrecognizedExtension"),
        ("NHRP-MIB", "nhrpServerStatRxErrLoopDetected"),
        ("NHRP-MIB", "nhrpServerStatRxErrProtoAddrUnreachable"),
        ("NHRP-MIB", "nhrpServerStatRxErrProtoError"),
        ("NHRP-MIB", "nhrpServerStatRxErrSduSizeExceeded"),
        ("NHRP-MIB", "nhrpServerStatRxErrInvalidExtension"),
        ("NHRP-MIB", "nhrpServerStatRxErrInvalidResReplyReceived"),
        ("NHRP-MIB", "nhrpServerStatRxErrAuthenticationFailure"),
        ("NHRP-MIB", "nhrpServerStatRxErrHopCountExceeded"),
        ("NHRP-MIB", "nhrpServerStatTxErrUnrecognizedExtension"),
        ("NHRP-MIB", "nhrpServerStatTxErrLoopDetected"),
        ("NHRP-MIB", "nhrpServerStatTxErrProtoAddrUnreachable"),
        ("NHRP-MIB", "nhrpServerStatTxErrProtoError"),
        ("NHRP-MIB", "nhrpServerStatTxErrSduSizeExceeded"),
        ("NHRP-MIB", "nhrpServerStatTxErrInvalidExtension"),
        ("NHRP-MIB", "nhrpServerStatTxErrAuthenticationFailure"),
        ("NHRP-MIB", "nhrpServerStatTxErrHopCountExceeded"),
        ("NHRP-MIB", "nhrpServerStatFwResolveReq"),
        ("NHRP-MIB", "nhrpServerStatFwResolveReply"),
        ("NHRP-MIB", "nhrpServerStatFwRegisterReq"),
        ("NHRP-MIB", "nhrpServerStatFwRegisterReply"),
        ("NHRP-MIB", "nhrpServerStatFwPurgeReq"),
        ("NHRP-MIB", "nhrpServerStatFwPurgeReply"),
        ("NHRP-MIB", "nhrpServerStatFwErrorIndication"),
        ("NHRP-MIB", "nhrpServerStatDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    nhrpServerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nhrpModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 71, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nhrpModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NHRP-MIB",
    **{"NhrpGenAddr": NhrpGenAddr,
       "nhrpMIB": nhrpMIB,
       "nhrpObjects": nhrpObjects,
       "nhrpGeneralObjects": nhrpGeneralObjects,
       "nhrpNextIndex": nhrpNextIndex,
       "nhrpCacheTable": nhrpCacheTable,
       "nhrpCacheEntry": nhrpCacheEntry,
       "nhrpCacheInternetworkAddrType": nhrpCacheInternetworkAddrType,
       "nhrpCacheInternetworkAddr": nhrpCacheInternetworkAddr,
       "nhrpCacheIndex": nhrpCacheIndex,
       "nhrpCachePrefixLength": nhrpCachePrefixLength,
       "nhrpCacheNextHopInternetworkAddr": nhrpCacheNextHopInternetworkAddr,
       "nhrpCacheNbmaAddrType": nhrpCacheNbmaAddrType,
       "nhrpCacheNbmaAddr": nhrpCacheNbmaAddr,
       "nhrpCacheNbmaSubaddr": nhrpCacheNbmaSubaddr,
       "nhrpCacheType": nhrpCacheType,
       "nhrpCacheState": nhrpCacheState,
       "nhrpCacheHoldingTimeValid": nhrpCacheHoldingTimeValid,
       "nhrpCacheHoldingTime": nhrpCacheHoldingTime,
       "nhrpCacheNegotiatedMtu": nhrpCacheNegotiatedMtu,
       "nhrpCachePreference": nhrpCachePreference,
       "nhrpCacheStorageType": nhrpCacheStorageType,
       "nhrpCacheRowStatus": nhrpCacheRowStatus,
       "nhrpPurgeReqTable": nhrpPurgeReqTable,
       "nhrpPurgeReqEntry": nhrpPurgeReqEntry,
       "nhrpPurgeIndex": nhrpPurgeIndex,
       "nhrpPurgeCacheIdentifier": nhrpPurgeCacheIdentifier,
       "nhrpPurgePrefixLength": nhrpPurgePrefixLength,
       "nhrpPurgeRequestID": nhrpPurgeRequestID,
       "nhrpPurgeReplyExpected": nhrpPurgeReplyExpected,
       "nhrpPurgeRowStatus": nhrpPurgeRowStatus,
       "nhrpClientObjects": nhrpClientObjects,
       "nhrpClientTable": nhrpClientTable,
       "nhrpClientEntry": nhrpClientEntry,
       "nhrpClientIndex": nhrpClientIndex,
       "nhrpClientInternetworkAddrType": nhrpClientInternetworkAddrType,
       "nhrpClientInternetworkAddr": nhrpClientInternetworkAddr,
       "nhrpClientNbmaAddrType": nhrpClientNbmaAddrType,
       "nhrpClientNbmaAddr": nhrpClientNbmaAddr,
       "nhrpClientNbmaSubaddr": nhrpClientNbmaSubaddr,
       "nhrpClientInitialRequestTimeout": nhrpClientInitialRequestTimeout,
       "nhrpClientRegistrationRequestRetries": nhrpClientRegistrationRequestRetries,
       "nhrpClientResolutionRequestRetries": nhrpClientResolutionRequestRetries,
       "nhrpClientPurgeRequestRetries": nhrpClientPurgeRequestRetries,
       "nhrpClientDefaultMtu": nhrpClientDefaultMtu,
       "nhrpClientHoldTime": nhrpClientHoldTime,
       "nhrpClientRequestID": nhrpClientRequestID,
       "nhrpClientStorageType": nhrpClientStorageType,
       "nhrpClientRowStatus": nhrpClientRowStatus,
       "nhrpClientRegistrationTable": nhrpClientRegistrationTable,
       "nhrpClientRegistrationEntry": nhrpClientRegistrationEntry,
       "nhrpClientRegIndex": nhrpClientRegIndex,
       "nhrpClientRegUniqueness": nhrpClientRegUniqueness,
       "nhrpClientRegState": nhrpClientRegState,
       "nhrpClientRegRowStatus": nhrpClientRegRowStatus,
       "nhrpClientNhsTable": nhrpClientNhsTable,
       "nhrpClientNhsEntry": nhrpClientNhsEntry,
       "nhrpClientNhsIndex": nhrpClientNhsIndex,
       "nhrpClientNhsInternetworkAddrType": nhrpClientNhsInternetworkAddrType,
       "nhrpClientNhsInternetworkAddr": nhrpClientNhsInternetworkAddr,
       "nhrpClientNhsNbmaAddrType": nhrpClientNhsNbmaAddrType,
       "nhrpClientNhsNbmaAddr": nhrpClientNhsNbmaAddr,
       "nhrpClientNhsNbmaSubaddr": nhrpClientNhsNbmaSubaddr,
       "nhrpClientNhsInUse": nhrpClientNhsInUse,
       "nhrpClientNhsRowStatus": nhrpClientNhsRowStatus,
       "nhrpClientStatTable": nhrpClientStatTable,
       "nhrpClientStatEntry": nhrpClientStatEntry,
       "nhrpClientStatTxResolveReq": nhrpClientStatTxResolveReq,
       "nhrpClientStatRxResolveReplyAck": nhrpClientStatRxResolveReplyAck,
       "nhrpClientStatRxResolveReplyNakProhibited": nhrpClientStatRxResolveReplyNakProhibited,
       "nhrpClientStatRxResolveReplyNakInsufResources": nhrpClientStatRxResolveReplyNakInsufResources,
       "nhrpClientStatRxResolveReplyNakNoBinding": nhrpClientStatRxResolveReplyNakNoBinding,
       "nhrpClientStatRxResolveReplyNakNotUnique": nhrpClientStatRxResolveReplyNakNotUnique,
       "nhrpClientStatTxRegisterReq": nhrpClientStatTxRegisterReq,
       "nhrpClientStatRxRegisterAck": nhrpClientStatRxRegisterAck,
       "nhrpClientStatRxRegisterNakProhibited": nhrpClientStatRxRegisterNakProhibited,
       "nhrpClientStatRxRegisterNakInsufResources": nhrpClientStatRxRegisterNakInsufResources,
       "nhrpClientStatRxRegisterNakAlreadyReg": nhrpClientStatRxRegisterNakAlreadyReg,
       "nhrpClientStatRxPurgeReq": nhrpClientStatRxPurgeReq,
       "nhrpClientStatTxPurgeReq": nhrpClientStatTxPurgeReq,
       "nhrpClientStatRxPurgeReply": nhrpClientStatRxPurgeReply,
       "nhrpClientStatTxPurgeReply": nhrpClientStatTxPurgeReply,
       "nhrpClientStatTxErrorIndication": nhrpClientStatTxErrorIndication,
       "nhrpClientStatRxErrUnrecognizedExtension": nhrpClientStatRxErrUnrecognizedExtension,
       "nhrpClientStatRxErrLoopDetected": nhrpClientStatRxErrLoopDetected,
       "nhrpClientStatRxErrProtoAddrUnreachable": nhrpClientStatRxErrProtoAddrUnreachable,
       "nhrpClientStatRxErrProtoError": nhrpClientStatRxErrProtoError,
       "nhrpClientStatRxErrSduSizeExceeded": nhrpClientStatRxErrSduSizeExceeded,
       "nhrpClientStatRxErrInvalidExtension": nhrpClientStatRxErrInvalidExtension,
       "nhrpClientStatRxErrAuthenticationFailure": nhrpClientStatRxErrAuthenticationFailure,
       "nhrpClientStatRxErrHopCountExceeded": nhrpClientStatRxErrHopCountExceeded,
       "nhrpClientStatDiscontinuityTime": nhrpClientStatDiscontinuityTime,
       "nhrpServerObjects": nhrpServerObjects,
       "nhrpServerTable": nhrpServerTable,
       "nhrpServerEntry": nhrpServerEntry,
       "nhrpServerIndex": nhrpServerIndex,
       "nhrpServerInternetworkAddrType": nhrpServerInternetworkAddrType,
       "nhrpServerInternetworkAddr": nhrpServerInternetworkAddr,
       "nhrpServerNbmaAddrType": nhrpServerNbmaAddrType,
       "nhrpServerNbmaAddr": nhrpServerNbmaAddr,
       "nhrpServerNbmaSubaddr": nhrpServerNbmaSubaddr,
       "nhrpServerStorageType": nhrpServerStorageType,
       "nhrpServerRowStatus": nhrpServerRowStatus,
       "nhrpServerCacheTable": nhrpServerCacheTable,
       "nhrpServerCacheEntry": nhrpServerCacheEntry,
       "nhrpServerCacheAuthoritative": nhrpServerCacheAuthoritative,
       "nhrpServerCacheUniqueness": nhrpServerCacheUniqueness,
       "nhrpServerNhcTable": nhrpServerNhcTable,
       "nhrpServerNhcEntry": nhrpServerNhcEntry,
       "nhrpServerNhcIndex": nhrpServerNhcIndex,
       "nhrpServerNhcPrefixLength": nhrpServerNhcPrefixLength,
       "nhrpServerNhcInternetworkAddrType": nhrpServerNhcInternetworkAddrType,
       "nhrpServerNhcInternetworkAddr": nhrpServerNhcInternetworkAddr,
       "nhrpServerNhcNbmaAddrType": nhrpServerNhcNbmaAddrType,
       "nhrpServerNhcNbmaAddr": nhrpServerNhcNbmaAddr,
       "nhrpServerNhcNbmaSubaddr": nhrpServerNhcNbmaSubaddr,
       "nhrpServerNhcInUse": nhrpServerNhcInUse,
       "nhrpServerNhcRowStatus": nhrpServerNhcRowStatus,
       "nhrpServerStatTable": nhrpServerStatTable,
       "nhrpServerStatEntry": nhrpServerStatEntry,
       "nhrpServerStatRxResolveReq": nhrpServerStatRxResolveReq,
       "nhrpServerStatTxResolveReplyAck": nhrpServerStatTxResolveReplyAck,
       "nhrpServerStatTxResolveReplyNakProhibited": nhrpServerStatTxResolveReplyNakProhibited,
       "nhrpServerStatTxResolveReplyNakInsufResources": nhrpServerStatTxResolveReplyNakInsufResources,
       "nhrpServerStatTxResolveReplyNakNoBinding": nhrpServerStatTxResolveReplyNakNoBinding,
       "nhrpServerStatTxResolveReplyNakNotUnique": nhrpServerStatTxResolveReplyNakNotUnique,
       "nhrpServerStatRxRegisterReq": nhrpServerStatRxRegisterReq,
       "nhrpServerStatTxRegisterAck": nhrpServerStatTxRegisterAck,
       "nhrpServerStatTxRegisterNakProhibited": nhrpServerStatTxRegisterNakProhibited,
       "nhrpServerStatTxRegisterNakInsufResources": nhrpServerStatTxRegisterNakInsufResources,
       "nhrpServerStatTxRegisterNakAlreadyReg": nhrpServerStatTxRegisterNakAlreadyReg,
       "nhrpServerStatRxPurgeReq": nhrpServerStatRxPurgeReq,
       "nhrpServerStatTxPurgeReq": nhrpServerStatTxPurgeReq,
       "nhrpServerStatRxPurgeReply": nhrpServerStatRxPurgeReply,
       "nhrpServerStatTxPurgeReply": nhrpServerStatTxPurgeReply,
       "nhrpServerStatRxErrUnrecognizedExtension": nhrpServerStatRxErrUnrecognizedExtension,
       "nhrpServerStatRxErrLoopDetected": nhrpServerStatRxErrLoopDetected,
       "nhrpServerStatRxErrProtoAddrUnreachable": nhrpServerStatRxErrProtoAddrUnreachable,
       "nhrpServerStatRxErrProtoError": nhrpServerStatRxErrProtoError,
       "nhrpServerStatRxErrSduSizeExceeded": nhrpServerStatRxErrSduSizeExceeded,
       "nhrpServerStatRxErrInvalidExtension": nhrpServerStatRxErrInvalidExtension,
       "nhrpServerStatRxErrInvalidResReplyReceived": nhrpServerStatRxErrInvalidResReplyReceived,
       "nhrpServerStatRxErrAuthenticationFailure": nhrpServerStatRxErrAuthenticationFailure,
       "nhrpServerStatRxErrHopCountExceeded": nhrpServerStatRxErrHopCountExceeded,
       "nhrpServerStatTxErrUnrecognizedExtension": nhrpServerStatTxErrUnrecognizedExtension,
       "nhrpServerStatTxErrLoopDetected": nhrpServerStatTxErrLoopDetected,
       "nhrpServerStatTxErrProtoAddrUnreachable": nhrpServerStatTxErrProtoAddrUnreachable,
       "nhrpServerStatTxErrProtoError": nhrpServerStatTxErrProtoError,
       "nhrpServerStatTxErrSduSizeExceeded": nhrpServerStatTxErrSduSizeExceeded,
       "nhrpServerStatTxErrInvalidExtension": nhrpServerStatTxErrInvalidExtension,
       "nhrpServerStatTxErrAuthenticationFailure": nhrpServerStatTxErrAuthenticationFailure,
       "nhrpServerStatTxErrHopCountExceeded": nhrpServerStatTxErrHopCountExceeded,
       "nhrpServerStatFwResolveReq": nhrpServerStatFwResolveReq,
       "nhrpServerStatFwResolveReply": nhrpServerStatFwResolveReply,
       "nhrpServerStatFwRegisterReq": nhrpServerStatFwRegisterReq,
       "nhrpServerStatFwRegisterReply": nhrpServerStatFwRegisterReply,
       "nhrpServerStatFwPurgeReq": nhrpServerStatFwPurgeReq,
       "nhrpServerStatFwPurgeReply": nhrpServerStatFwPurgeReply,
       "nhrpServerStatFwErrorIndication": nhrpServerStatFwErrorIndication,
       "nhrpServerStatDiscontinuityTime": nhrpServerStatDiscontinuityTime,
       "nhrpConformance": nhrpConformance,
       "nhrpCompliances": nhrpCompliances,
       "nhrpModuleCompliance": nhrpModuleCompliance,
       "nhrpGroups": nhrpGroups,
       "nhrpGeneralGroup": nhrpGeneralGroup,
       "nhrpClientGroup": nhrpClientGroup,
       "nhrpServerGroup": nhrpServerGroup}
)
