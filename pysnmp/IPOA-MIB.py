# SNMP MIB module (IPOA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPOA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:02 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(ipAdEntAddr,
 ipNetToMediaIfIndex,
 ipNetToMediaNetAddress,
 ipNetToMediaPhysAddress) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntAddr",
    "ipNetToMediaIfIndex",
    "ipNetToMediaNetAddress",
    "ipNetToMediaPhysAddress")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ipoaMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 46)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IpoaEncapsType(Integer32, TextualConvention):
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
        *(("llcSnap", 1),
          ("other", 3),
          ("vcMuxed", 2))
    )



class IpoaVpiInteger(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class IpoaVciInteger(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IpoaAtmAddr(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



class IpoaAtmConnKind(Integer32, TextualConvention):
    status = "current"
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
        *(("pvc", 1),
          ("spvcInitiator", 4),
          ("spvcTarget", 5),
          ("svcIncoming", 2),
          ("svcOutgoing", 3))
    )



# MIB Managed Objects in the order of their OIDs

_IpoaObjects_ObjectIdentity = ObjectIdentity
ipoaObjects = _IpoaObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 46, 1)
)


class _IpoaLisTrapEnable_Type(Integer32):
    """Custom type ipoaLisTrapEnable based on Integer32"""
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


_IpoaLisTrapEnable_Type.__name__ = "Integer32"
_IpoaLisTrapEnable_Object = MibScalar
ipoaLisTrapEnable = _IpoaLisTrapEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 1),
    _IpoaLisTrapEnable_Type()
)
ipoaLisTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipoaLisTrapEnable.setStatus("current")
_IpoaLisTable_Object = MibTable
ipoaLisTable = _IpoaLisTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2)
)
if mibBuilder.loadTexts:
    ipoaLisTable.setStatus("current")
_IpoaLisEntry_Object = MibTableRow
ipoaLisEntry = _IpoaLisEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1)
)
ipoaLisEntry.setIndexNames(
    (0, "IPOA-MIB", "ipoaLisSubnetAddr"),
)
if mibBuilder.loadTexts:
    ipoaLisEntry.setStatus("current")
_IpoaLisSubnetAddr_Type = IpAddress
_IpoaLisSubnetAddr_Object = MibTableColumn
ipoaLisSubnetAddr = _IpoaLisSubnetAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 1),
    _IpoaLisSubnetAddr_Type()
)
ipoaLisSubnetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaLisSubnetAddr.setStatus("current")


class _IpoaLisDefaultMtu_Type(Integer32):
    """Custom type ipoaLisDefaultMtu based on Integer32"""
    defaultValue = 9180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpoaLisDefaultMtu_Type.__name__ = "Integer32"
_IpoaLisDefaultMtu_Object = MibTableColumn
ipoaLisDefaultMtu = _IpoaLisDefaultMtu_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 2),
    _IpoaLisDefaultMtu_Type()
)
ipoaLisDefaultMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaLisDefaultMtu.setStatus("current")


class _IpoaLisDefaultEncapsType_Type(IpoaEncapsType):
    """Custom type ipoaLisDefaultEncapsType based on IpoaEncapsType"""


_IpoaLisDefaultEncapsType_Object = MibTableColumn
ipoaLisDefaultEncapsType = _IpoaLisDefaultEncapsType_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 3),
    _IpoaLisDefaultEncapsType_Type()
)
ipoaLisDefaultEncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaLisDefaultEncapsType.setStatus("current")


class _IpoaLisInactivityTimer_Type(Integer32):
    """Custom type ipoaLisInactivityTimer based on Integer32"""
    defaultValue = 1200


_IpoaLisInactivityTimer_Object = MibTableColumn
ipoaLisInactivityTimer = _IpoaLisInactivityTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 4),
    _IpoaLisInactivityTimer_Type()
)
ipoaLisInactivityTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaLisInactivityTimer.setStatus("current")
if mibBuilder.loadTexts:
    ipoaLisInactivityTimer.setUnits("seconds")


class _IpoaLisMinHoldingTime_Type(Integer32):
    """Custom type ipoaLisMinHoldingTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpoaLisMinHoldingTime_Type.__name__ = "Integer32"
_IpoaLisMinHoldingTime_Object = MibTableColumn
ipoaLisMinHoldingTime = _IpoaLisMinHoldingTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 5),
    _IpoaLisMinHoldingTime_Type()
)
ipoaLisMinHoldingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaLisMinHoldingTime.setStatus("current")
if mibBuilder.loadTexts:
    ipoaLisMinHoldingTime.setUnits("seconds")


class _IpoaLisQDepth_Type(Integer32):
    """Custom type ipoaLisQDepth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpoaLisQDepth_Type.__name__ = "Integer32"
_IpoaLisQDepth_Object = MibTableColumn
ipoaLisQDepth = _IpoaLisQDepth_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 6),
    _IpoaLisQDepth_Type()
)
ipoaLisQDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaLisQDepth.setStatus("current")
if mibBuilder.loadTexts:
    ipoaLisQDepth.setUnits("packets")


class _IpoaLisMaxCalls_Type(Integer32):
    """Custom type ipoaLisMaxCalls based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpoaLisMaxCalls_Type.__name__ = "Integer32"
_IpoaLisMaxCalls_Object = MibTableColumn
ipoaLisMaxCalls = _IpoaLisMaxCalls_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 7),
    _IpoaLisMaxCalls_Type()
)
ipoaLisMaxCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaLisMaxCalls.setStatus("current")


class _IpoaLisCacheEntryAge_Type(Integer32):
    """Custom type ipoaLisCacheEntryAge based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1200),
    )


_IpoaLisCacheEntryAge_Type.__name__ = "Integer32"
_IpoaLisCacheEntryAge_Object = MibTableColumn
ipoaLisCacheEntryAge = _IpoaLisCacheEntryAge_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 8),
    _IpoaLisCacheEntryAge_Type()
)
ipoaLisCacheEntryAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaLisCacheEntryAge.setStatus("current")
if mibBuilder.loadTexts:
    ipoaLisCacheEntryAge.setUnits("seconds")


class _IpoaLisRetries_Type(Integer32):
    """Custom type ipoaLisRetries based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_IpoaLisRetries_Type.__name__ = "Integer32"
_IpoaLisRetries_Object = MibTableColumn
ipoaLisRetries = _IpoaLisRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 9),
    _IpoaLisRetries_Type()
)
ipoaLisRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaLisRetries.setStatus("current")


class _IpoaLisTimeout_Type(Integer32):
    """Custom type ipoaLisTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_IpoaLisTimeout_Type.__name__ = "Integer32"
_IpoaLisTimeout_Object = MibTableColumn
ipoaLisTimeout = _IpoaLisTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 10),
    _IpoaLisTimeout_Type()
)
ipoaLisTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaLisTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ipoaLisTimeout.setUnits("seconds")
_IpoaLisDefaultPeakCellRate_Type = Integer32
_IpoaLisDefaultPeakCellRate_Object = MibTableColumn
ipoaLisDefaultPeakCellRate = _IpoaLisDefaultPeakCellRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 11),
    _IpoaLisDefaultPeakCellRate_Type()
)
ipoaLisDefaultPeakCellRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaLisDefaultPeakCellRate.setStatus("current")
_IpoaLisActiveVcs_Type = Gauge32
_IpoaLisActiveVcs_Object = MibTableColumn
ipoaLisActiveVcs = _IpoaLisActiveVcs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 12),
    _IpoaLisActiveVcs_Type()
)
ipoaLisActiveVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaLisActiveVcs.setStatus("current")
_IpoaLisRowStatus_Type = RowStatus
_IpoaLisRowStatus_Object = MibTableColumn
ipoaLisRowStatus = _IpoaLisRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 13),
    _IpoaLisRowStatus_Type()
)
ipoaLisRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaLisRowStatus.setStatus("current")
_IpoaLisIfMappingTable_Object = MibTable
ipoaLisIfMappingTable = _IpoaLisIfMappingTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 3)
)
if mibBuilder.loadTexts:
    ipoaLisIfMappingTable.setStatus("current")
_IpoaLisIfMappingEntry_Object = MibTableRow
ipoaLisIfMappingEntry = _IpoaLisIfMappingEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 3, 1)
)
ipoaLisIfMappingEntry.setIndexNames(
    (0, "IPOA-MIB", "ipoaLisSubnetAddr"),
    (0, "IPOA-MIB", "ipoaLisIfMappingIfIndex"),
)
if mibBuilder.loadTexts:
    ipoaLisIfMappingEntry.setStatus("current")
_IpoaLisIfMappingIfIndex_Type = InterfaceIndex
_IpoaLisIfMappingIfIndex_Object = MibTableColumn
ipoaLisIfMappingIfIndex = _IpoaLisIfMappingIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 3, 1, 1),
    _IpoaLisIfMappingIfIndex_Type()
)
ipoaLisIfMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipoaLisIfMappingIfIndex.setStatus("current")
_IpoaLisIfMappingRowStatus_Type = RowStatus
_IpoaLisIfMappingRowStatus_Object = MibTableColumn
ipoaLisIfMappingRowStatus = _IpoaLisIfMappingRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 3, 1, 2),
    _IpoaLisIfMappingRowStatus_Type()
)
ipoaLisIfMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaLisIfMappingRowStatus.setStatus("current")
_IpoaArpClientTable_Object = MibTable
ipoaArpClientTable = _IpoaArpClientTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4)
)
if mibBuilder.loadTexts:
    ipoaArpClientTable.setStatus("current")
_IpoaArpClientEntry_Object = MibTableRow
ipoaArpClientEntry = _IpoaArpClientEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1)
)
ipoaArpClientEntry.setIndexNames(
    (0, "IP-MIB", "ipAdEntAddr"),
)
if mibBuilder.loadTexts:
    ipoaArpClientEntry.setStatus("current")
_IpoaArpClientAtmAddr_Type = IpoaAtmAddr
_IpoaArpClientAtmAddr_Object = MibTableColumn
ipoaArpClientAtmAddr = _IpoaArpClientAtmAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 1),
    _IpoaArpClientAtmAddr_Type()
)
ipoaArpClientAtmAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaArpClientAtmAddr.setStatus("current")


class _IpoaArpClientSrvrInUse_Type(IpoaAtmAddr):
    """Custom type ipoaArpClientSrvrInUse based on IpoaAtmAddr"""
    defaultHexValue = ""


_IpoaArpClientSrvrInUse_Object = MibTableColumn
ipoaArpClientSrvrInUse = _IpoaArpClientSrvrInUse_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 2),
    _IpoaArpClientSrvrInUse_Type()
)
ipoaArpClientSrvrInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientSrvrInUse.setStatus("current")
_IpoaArpClientInArpInReqs_Type = Counter32
_IpoaArpClientInArpInReqs_Object = MibTableColumn
ipoaArpClientInArpInReqs = _IpoaArpClientInArpInReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 3),
    _IpoaArpClientInArpInReqs_Type()
)
ipoaArpClientInArpInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientInArpInReqs.setStatus("current")
_IpoaArpClientInArpOutReqs_Type = Counter32
_IpoaArpClientInArpOutReqs_Object = MibTableColumn
ipoaArpClientInArpOutReqs = _IpoaArpClientInArpOutReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 4),
    _IpoaArpClientInArpOutReqs_Type()
)
ipoaArpClientInArpOutReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientInArpOutReqs.setStatus("current")
_IpoaArpClientInArpInReplies_Type = Counter32
_IpoaArpClientInArpInReplies_Object = MibTableColumn
ipoaArpClientInArpInReplies = _IpoaArpClientInArpInReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 5),
    _IpoaArpClientInArpInReplies_Type()
)
ipoaArpClientInArpInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientInArpInReplies.setStatus("current")
_IpoaArpClientInArpOutReplies_Type = Counter32
_IpoaArpClientInArpOutReplies_Object = MibTableColumn
ipoaArpClientInArpOutReplies = _IpoaArpClientInArpOutReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 6),
    _IpoaArpClientInArpOutReplies_Type()
)
ipoaArpClientInArpOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientInArpOutReplies.setStatus("current")
_IpoaArpClientInArpInvalidInReqs_Type = Counter32
_IpoaArpClientInArpInvalidInReqs_Object = MibTableColumn
ipoaArpClientInArpInvalidInReqs = _IpoaArpClientInArpInvalidInReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 7),
    _IpoaArpClientInArpInvalidInReqs_Type()
)
ipoaArpClientInArpInvalidInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientInArpInvalidInReqs.setStatus("current")
_IpoaArpClientInArpInvalidOutReqs_Type = Counter32
_IpoaArpClientInArpInvalidOutReqs_Object = MibTableColumn
ipoaArpClientInArpInvalidOutReqs = _IpoaArpClientInArpInvalidOutReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 8),
    _IpoaArpClientInArpInvalidOutReqs_Type()
)
ipoaArpClientInArpInvalidOutReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientInArpInvalidOutReqs.setStatus("current")
_IpoaArpClientArpInReqs_Type = Counter32
_IpoaArpClientArpInReqs_Object = MibTableColumn
ipoaArpClientArpInReqs = _IpoaArpClientArpInReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 9),
    _IpoaArpClientArpInReqs_Type()
)
ipoaArpClientArpInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientArpInReqs.setStatus("current")
_IpoaArpClientArpOutReqs_Type = Counter32
_IpoaArpClientArpOutReqs_Object = MibTableColumn
ipoaArpClientArpOutReqs = _IpoaArpClientArpOutReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 10),
    _IpoaArpClientArpOutReqs_Type()
)
ipoaArpClientArpOutReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientArpOutReqs.setStatus("current")
_IpoaArpClientArpInReplies_Type = Counter32
_IpoaArpClientArpInReplies_Object = MibTableColumn
ipoaArpClientArpInReplies = _IpoaArpClientArpInReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 11),
    _IpoaArpClientArpInReplies_Type()
)
ipoaArpClientArpInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientArpInReplies.setStatus("current")
_IpoaArpClientArpOutReplies_Type = Counter32
_IpoaArpClientArpOutReplies_Object = MibTableColumn
ipoaArpClientArpOutReplies = _IpoaArpClientArpOutReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 12),
    _IpoaArpClientArpOutReplies_Type()
)
ipoaArpClientArpOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientArpOutReplies.setStatus("current")
_IpoaArpClientArpInNaks_Type = Counter32
_IpoaArpClientArpInNaks_Object = MibTableColumn
ipoaArpClientArpInNaks = _IpoaArpClientArpInNaks_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 13),
    _IpoaArpClientArpInNaks_Type()
)
ipoaArpClientArpInNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientArpInNaks.setStatus("current")
_IpoaArpClientArpOutNaks_Type = Counter32
_IpoaArpClientArpOutNaks_Object = MibTableColumn
ipoaArpClientArpOutNaks = _IpoaArpClientArpOutNaks_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 14),
    _IpoaArpClientArpOutNaks_Type()
)
ipoaArpClientArpOutNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientArpOutNaks.setStatus("current")
_IpoaArpClientArpUnknownOps_Type = Counter32
_IpoaArpClientArpUnknownOps_Object = MibTableColumn
ipoaArpClientArpUnknownOps = _IpoaArpClientArpUnknownOps_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 15),
    _IpoaArpClientArpUnknownOps_Type()
)
ipoaArpClientArpUnknownOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientArpUnknownOps.setStatus("current")
_IpoaArpClientArpNoSrvrResps_Type = Counter32
_IpoaArpClientArpNoSrvrResps_Object = MibTableColumn
ipoaArpClientArpNoSrvrResps = _IpoaArpClientArpNoSrvrResps_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 16),
    _IpoaArpClientArpNoSrvrResps_Type()
)
ipoaArpClientArpNoSrvrResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpClientArpNoSrvrResps.setStatus("current")
_IpoaArpClientRowStatus_Type = RowStatus
_IpoaArpClientRowStatus_Object = MibTableColumn
ipoaArpClientRowStatus = _IpoaArpClientRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 17),
    _IpoaArpClientRowStatus_Type()
)
ipoaArpClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaArpClientRowStatus.setStatus("current")
_IpoaArpSrvrTable_Object = MibTable
ipoaArpSrvrTable = _IpoaArpSrvrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5)
)
if mibBuilder.loadTexts:
    ipoaArpSrvrTable.setStatus("current")
_IpoaArpSrvrEntry_Object = MibTableRow
ipoaArpSrvrEntry = _IpoaArpSrvrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1)
)
ipoaArpSrvrEntry.setIndexNames(
    (0, "IP-MIB", "ipAdEntAddr"),
    (0, "IPOA-MIB", "ipoaArpSrvrAddr"),
)
if mibBuilder.loadTexts:
    ipoaArpSrvrEntry.setStatus("current")
_IpoaArpSrvrAddr_Type = IpoaAtmAddr
_IpoaArpSrvrAddr_Object = MibTableColumn
ipoaArpSrvrAddr = _IpoaArpSrvrAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 1),
    _IpoaArpSrvrAddr_Type()
)
ipoaArpSrvrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipoaArpSrvrAddr.setStatus("current")
_IpoaArpSrvrLis_Type = IpAddress
_IpoaArpSrvrLis_Object = MibTableColumn
ipoaArpSrvrLis = _IpoaArpSrvrLis_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 2),
    _IpoaArpSrvrLis_Type()
)
ipoaArpSrvrLis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaArpSrvrLis.setStatus("current")
_IpoaArpSrvrInArpInReqs_Type = Counter32
_IpoaArpSrvrInArpInReqs_Object = MibTableColumn
ipoaArpSrvrInArpInReqs = _IpoaArpSrvrInArpInReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 3),
    _IpoaArpSrvrInArpInReqs_Type()
)
ipoaArpSrvrInArpInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpSrvrInArpInReqs.setStatus("current")
_IpoaArpSrvrInArpOutReqs_Type = Counter32
_IpoaArpSrvrInArpOutReqs_Object = MibTableColumn
ipoaArpSrvrInArpOutReqs = _IpoaArpSrvrInArpOutReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 4),
    _IpoaArpSrvrInArpOutReqs_Type()
)
ipoaArpSrvrInArpOutReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpSrvrInArpOutReqs.setStatus("current")
_IpoaArpSrvrInArpInReplies_Type = Counter32
_IpoaArpSrvrInArpInReplies_Object = MibTableColumn
ipoaArpSrvrInArpInReplies = _IpoaArpSrvrInArpInReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 5),
    _IpoaArpSrvrInArpInReplies_Type()
)
ipoaArpSrvrInArpInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpSrvrInArpInReplies.setStatus("current")
_IpoaArpSrvrInArpOutReplies_Type = Counter32
_IpoaArpSrvrInArpOutReplies_Object = MibTableColumn
ipoaArpSrvrInArpOutReplies = _IpoaArpSrvrInArpOutReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 6),
    _IpoaArpSrvrInArpOutReplies_Type()
)
ipoaArpSrvrInArpOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpSrvrInArpOutReplies.setStatus("current")
_IpoaArpSrvrInArpInvalidInReqs_Type = Counter32
_IpoaArpSrvrInArpInvalidInReqs_Object = MibTableColumn
ipoaArpSrvrInArpInvalidInReqs = _IpoaArpSrvrInArpInvalidInReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 7),
    _IpoaArpSrvrInArpInvalidInReqs_Type()
)
ipoaArpSrvrInArpInvalidInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpSrvrInArpInvalidInReqs.setStatus("current")
_IpoaArpSrvrInArpInvalidOutReqs_Type = Counter32
_IpoaArpSrvrInArpInvalidOutReqs_Object = MibTableColumn
ipoaArpSrvrInArpInvalidOutReqs = _IpoaArpSrvrInArpInvalidOutReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 8),
    _IpoaArpSrvrInArpInvalidOutReqs_Type()
)
ipoaArpSrvrInArpInvalidOutReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpSrvrInArpInvalidOutReqs.setStatus("current")
_IpoaArpSrvrArpInReqs_Type = Counter32
_IpoaArpSrvrArpInReqs_Object = MibTableColumn
ipoaArpSrvrArpInReqs = _IpoaArpSrvrArpInReqs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 9),
    _IpoaArpSrvrArpInReqs_Type()
)
ipoaArpSrvrArpInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpSrvrArpInReqs.setStatus("current")
_IpoaArpSrvrArpOutReplies_Type = Counter32
_IpoaArpSrvrArpOutReplies_Object = MibTableColumn
ipoaArpSrvrArpOutReplies = _IpoaArpSrvrArpOutReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 10),
    _IpoaArpSrvrArpOutReplies_Type()
)
ipoaArpSrvrArpOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpSrvrArpOutReplies.setStatus("current")
_IpoaArpSrvrArpOutNaks_Type = Counter32
_IpoaArpSrvrArpOutNaks_Object = MibTableColumn
ipoaArpSrvrArpOutNaks = _IpoaArpSrvrArpOutNaks_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 11),
    _IpoaArpSrvrArpOutNaks_Type()
)
ipoaArpSrvrArpOutNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpSrvrArpOutNaks.setStatus("current")
_IpoaArpSrvrArpDupIpAddrs_Type = Counter32
_IpoaArpSrvrArpDupIpAddrs_Object = MibTableColumn
ipoaArpSrvrArpDupIpAddrs = _IpoaArpSrvrArpDupIpAddrs_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 12),
    _IpoaArpSrvrArpDupIpAddrs_Type()
)
ipoaArpSrvrArpDupIpAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpSrvrArpDupIpAddrs.setStatus("current")
_IpoaArpSrvrArpUnknownOps_Type = Counter32
_IpoaArpSrvrArpUnknownOps_Object = MibTableColumn
ipoaArpSrvrArpUnknownOps = _IpoaArpSrvrArpUnknownOps_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 13),
    _IpoaArpSrvrArpUnknownOps_Type()
)
ipoaArpSrvrArpUnknownOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpSrvrArpUnknownOps.setStatus("current")
_IpoaArpSrvrRowStatus_Type = RowStatus
_IpoaArpSrvrRowStatus_Object = MibTableColumn
ipoaArpSrvrRowStatus = _IpoaArpSrvrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 14),
    _IpoaArpSrvrRowStatus_Type()
)
ipoaArpSrvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaArpSrvrRowStatus.setStatus("current")
_IpoaArpRemoteSrvrTable_Object = MibTable
ipoaArpRemoteSrvrTable = _IpoaArpRemoteSrvrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 6)
)
if mibBuilder.loadTexts:
    ipoaArpRemoteSrvrTable.setStatus("current")
_IpoaArpRemoteSrvrEntry_Object = MibTableRow
ipoaArpRemoteSrvrEntry = _IpoaArpRemoteSrvrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1)
)
ipoaArpRemoteSrvrEntry.setIndexNames(
    (0, "IPOA-MIB", "ipoaLisSubnetAddr"),
    (0, "IPOA-MIB", "ipoaArpRemoteSrvrAtmAddr"),
    (0, "IPOA-MIB", "ipoaArpRemoteSrvrIfIndex"),
)
if mibBuilder.loadTexts:
    ipoaArpRemoteSrvrEntry.setStatus("current")
_IpoaArpRemoteSrvrAtmAddr_Type = IpoaAtmAddr
_IpoaArpRemoteSrvrAtmAddr_Object = MibTableColumn
ipoaArpRemoteSrvrAtmAddr = _IpoaArpRemoteSrvrAtmAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 1),
    _IpoaArpRemoteSrvrAtmAddr_Type()
)
ipoaArpRemoteSrvrAtmAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipoaArpRemoteSrvrAtmAddr.setStatus("current")
_IpoaArpRemoteSrvrRowStatus_Type = RowStatus
_IpoaArpRemoteSrvrRowStatus_Object = MibTableColumn
ipoaArpRemoteSrvrRowStatus = _IpoaArpRemoteSrvrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 2),
    _IpoaArpRemoteSrvrRowStatus_Type()
)
ipoaArpRemoteSrvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaArpRemoteSrvrRowStatus.setStatus("current")
_IpoaArpRemoteSrvrIfIndex_Type = InterfaceIndexOrZero
_IpoaArpRemoteSrvrIfIndex_Object = MibTableColumn
ipoaArpRemoteSrvrIfIndex = _IpoaArpRemoteSrvrIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 3),
    _IpoaArpRemoteSrvrIfIndex_Type()
)
ipoaArpRemoteSrvrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipoaArpRemoteSrvrIfIndex.setStatus("current")


class _IpoaArpRemoteSrvrIpAddr_Type(IpAddress):
    """Custom type ipoaArpRemoteSrvrIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpoaArpRemoteSrvrIpAddr_Object = MibTableColumn
ipoaArpRemoteSrvrIpAddr = _IpoaArpRemoteSrvrIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 4),
    _IpoaArpRemoteSrvrIpAddr_Type()
)
ipoaArpRemoteSrvrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpRemoteSrvrIpAddr.setStatus("current")


class _IpoaArpRemoteSrvrAdminStatus_Type(Integer32):
    """Custom type ipoaArpRemoteSrvrAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_IpoaArpRemoteSrvrAdminStatus_Type.__name__ = "Integer32"
_IpoaArpRemoteSrvrAdminStatus_Object = MibTableColumn
ipoaArpRemoteSrvrAdminStatus = _IpoaArpRemoteSrvrAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 5),
    _IpoaArpRemoteSrvrAdminStatus_Type()
)
ipoaArpRemoteSrvrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaArpRemoteSrvrAdminStatus.setStatus("current")


class _IpoaArpRemoteSrvrOperStatus_Type(Integer32):
    """Custom type ipoaArpRemoteSrvrOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_IpoaArpRemoteSrvrOperStatus_Type.__name__ = "Integer32"
_IpoaArpRemoteSrvrOperStatus_Object = MibTableColumn
ipoaArpRemoteSrvrOperStatus = _IpoaArpRemoteSrvrOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 6),
    _IpoaArpRemoteSrvrOperStatus_Type()
)
ipoaArpRemoteSrvrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaArpRemoteSrvrOperStatus.setStatus("current")
_IpoaVcTable_Object = MibTable
ipoaVcTable = _IpoaVcTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 7)
)
if mibBuilder.loadTexts:
    ipoaVcTable.setStatus("current")
_IpoaVcEntry_Object = MibTableRow
ipoaVcEntry = _IpoaVcEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1)
)
ipoaVcEntry.setIndexNames(
    (0, "IP-MIB", "ipNetToMediaIfIndex"),
    (0, "IP-MIB", "ipNetToMediaNetAddress"),
    (0, "IPOA-MIB", "ipoaVcVpi"),
    (0, "IPOA-MIB", "ipoaVcVci"),
)
if mibBuilder.loadTexts:
    ipoaVcEntry.setStatus("current")
_IpoaVcVpi_Type = IpoaVpiInteger
_IpoaVcVpi_Object = MibTableColumn
ipoaVcVpi = _IpoaVcVpi_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 1),
    _IpoaVcVpi_Type()
)
ipoaVcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipoaVcVpi.setStatus("current")
_IpoaVcVci_Type = IpoaVciInteger
_IpoaVcVci_Object = MibTableColumn
ipoaVcVci = _IpoaVcVci_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 2),
    _IpoaVcVci_Type()
)
ipoaVcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipoaVcVci.setStatus("current")
_IpoaVcType_Type = IpoaAtmConnKind
_IpoaVcType_Object = MibTableColumn
ipoaVcType = _IpoaVcType_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 3),
    _IpoaVcType_Type()
)
ipoaVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaVcType.setStatus("current")
_IpoaVcNegotiatedEncapsType_Type = IpoaEncapsType
_IpoaVcNegotiatedEncapsType_Object = MibTableColumn
ipoaVcNegotiatedEncapsType = _IpoaVcNegotiatedEncapsType_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 4),
    _IpoaVcNegotiatedEncapsType_Type()
)
ipoaVcNegotiatedEncapsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaVcNegotiatedEncapsType.setStatus("current")


class _IpoaVcNegotiatedMtu_Type(Integer32):
    """Custom type ipoaVcNegotiatedMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpoaVcNegotiatedMtu_Type.__name__ = "Integer32"
_IpoaVcNegotiatedMtu_Object = MibTableColumn
ipoaVcNegotiatedMtu = _IpoaVcNegotiatedMtu_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 5),
    _IpoaVcNegotiatedMtu_Type()
)
ipoaVcNegotiatedMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoaVcNegotiatedMtu.setStatus("current")
_IpoaConfigPvcTable_Object = MibTable
ipoaConfigPvcTable = _IpoaConfigPvcTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 8)
)
if mibBuilder.loadTexts:
    ipoaConfigPvcTable.setStatus("current")
_IpoaConfigPvcEntry_Object = MibTableRow
ipoaConfigPvcEntry = _IpoaConfigPvcEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1)
)
ipoaConfigPvcEntry.setIndexNames(
    (0, "IPOA-MIB", "ipoaConfigPvcIfIndex"),
    (0, "IPOA-MIB", "ipoaConfigPvcVpi"),
    (0, "IPOA-MIB", "ipoaConfigPvcVci"),
)
if mibBuilder.loadTexts:
    ipoaConfigPvcEntry.setStatus("current")
_IpoaConfigPvcIfIndex_Type = InterfaceIndex
_IpoaConfigPvcIfIndex_Object = MibTableColumn
ipoaConfigPvcIfIndex = _IpoaConfigPvcIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 1),
    _IpoaConfigPvcIfIndex_Type()
)
ipoaConfigPvcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipoaConfigPvcIfIndex.setStatus("current")
_IpoaConfigPvcVpi_Type = IpoaVpiInteger
_IpoaConfigPvcVpi_Object = MibTableColumn
ipoaConfigPvcVpi = _IpoaConfigPvcVpi_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 2),
    _IpoaConfigPvcVpi_Type()
)
ipoaConfigPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipoaConfigPvcVpi.setStatus("current")
_IpoaConfigPvcVci_Type = IpoaVciInteger
_IpoaConfigPvcVci_Object = MibTableColumn
ipoaConfigPvcVci = _IpoaConfigPvcVci_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 3),
    _IpoaConfigPvcVci_Type()
)
ipoaConfigPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipoaConfigPvcVci.setStatus("current")


class _IpoaConfigPvcDefaultMtu_Type(Integer32):
    """Custom type ipoaConfigPvcDefaultMtu based on Integer32"""
    defaultValue = 9180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpoaConfigPvcDefaultMtu_Type.__name__ = "Integer32"
_IpoaConfigPvcDefaultMtu_Object = MibTableColumn
ipoaConfigPvcDefaultMtu = _IpoaConfigPvcDefaultMtu_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 4),
    _IpoaConfigPvcDefaultMtu_Type()
)
ipoaConfigPvcDefaultMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaConfigPvcDefaultMtu.setStatus("current")
_IpoaConfigPvcRowStatus_Type = RowStatus
_IpoaConfigPvcRowStatus_Object = MibTableColumn
ipoaConfigPvcRowStatus = _IpoaConfigPvcRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 5),
    _IpoaConfigPvcRowStatus_Type()
)
ipoaConfigPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipoaConfigPvcRowStatus.setStatus("current")
_IpoaNotifications_ObjectIdentity = ObjectIdentity
ipoaNotifications = _IpoaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 46, 2)
)
_IpoaTrapPrefix_ObjectIdentity = ObjectIdentity
ipoaTrapPrefix = _IpoaTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 46, 2, 0)
)
_IpoaConformance_ObjectIdentity = ObjectIdentity
ipoaConformance = _IpoaConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 46, 3)
)
_IpoaGroups_ObjectIdentity = ObjectIdentity
ipoaGroups = _IpoaGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 46, 3, 1)
)
_IpoaCompliances_ObjectIdentity = ObjectIdentity
ipoaCompliances = _IpoaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 46, 3, 2)
)

# Managed Objects groups

ipoaGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 1)
)
ipoaGeneralGroup.setObjects(
      *(("IPOA-MIB", "ipoaVcType"),
        ("IPOA-MIB", "ipoaVcNegotiatedEncapsType"),
        ("IPOA-MIB", "ipoaVcNegotiatedMtu"),
        ("IPOA-MIB", "ipoaConfigPvcDefaultMtu"),
        ("IPOA-MIB", "ipoaConfigPvcRowStatus"))
)
if mibBuilder.loadTexts:
    ipoaGeneralGroup.setStatus("current")

ipoaClientGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 2)
)
ipoaClientGroup.setObjects(
      *(("IPOA-MIB", "ipoaArpClientAtmAddr"),
        ("IPOA-MIB", "ipoaArpClientSrvrInUse"),
        ("IPOA-MIB", "ipoaArpClientInArpInReqs"),
        ("IPOA-MIB", "ipoaArpClientInArpOutReqs"),
        ("IPOA-MIB", "ipoaArpClientInArpInReplies"),
        ("IPOA-MIB", "ipoaArpClientInArpOutReplies"),
        ("IPOA-MIB", "ipoaArpClientInArpInvalidInReqs"),
        ("IPOA-MIB", "ipoaArpClientInArpInvalidOutReqs"),
        ("IPOA-MIB", "ipoaArpClientArpInReqs"),
        ("IPOA-MIB", "ipoaArpClientArpOutReqs"),
        ("IPOA-MIB", "ipoaArpClientArpInReplies"),
        ("IPOA-MIB", "ipoaArpClientArpOutReplies"),
        ("IPOA-MIB", "ipoaArpClientArpInNaks"),
        ("IPOA-MIB", "ipoaArpClientArpOutNaks"),
        ("IPOA-MIB", "ipoaArpClientArpUnknownOps"),
        ("IPOA-MIB", "ipoaArpClientArpNoSrvrResps"),
        ("IPOA-MIB", "ipoaArpClientRowStatus"))
)
if mibBuilder.loadTexts:
    ipoaClientGroup.setStatus("current")

ipoaSrvrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 3)
)
ipoaSrvrGroup.setObjects(
      *(("IPOA-MIB", "ipoaArpSrvrLis"),
        ("IPOA-MIB", "ipoaArpSrvrInArpInReqs"),
        ("IPOA-MIB", "ipoaArpSrvrInArpOutReqs"),
        ("IPOA-MIB", "ipoaArpSrvrInArpInReplies"),
        ("IPOA-MIB", "ipoaArpSrvrInArpOutReplies"),
        ("IPOA-MIB", "ipoaArpSrvrInArpInvalidInReqs"),
        ("IPOA-MIB", "ipoaArpSrvrInArpInvalidOutReqs"),
        ("IPOA-MIB", "ipoaArpSrvrArpInReqs"),
        ("IPOA-MIB", "ipoaArpSrvrArpOutReplies"),
        ("IPOA-MIB", "ipoaArpSrvrArpOutNaks"),
        ("IPOA-MIB", "ipoaArpSrvrArpDupIpAddrs"),
        ("IPOA-MIB", "ipoaArpSrvrArpUnknownOps"),
        ("IPOA-MIB", "ipoaArpSrvrRowStatus"))
)
if mibBuilder.loadTexts:
    ipoaSrvrGroup.setStatus("current")

ipoaLisTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 7)
)
ipoaLisTableGroup.setObjects(
      *(("IPOA-MIB", "ipoaLisTrapEnable"),
        ("IPOA-MIB", "ipoaLisSubnetAddr"),
        ("IPOA-MIB", "ipoaLisDefaultMtu"),
        ("IPOA-MIB", "ipoaLisDefaultEncapsType"),
        ("IPOA-MIB", "ipoaLisInactivityTimer"),
        ("IPOA-MIB", "ipoaLisMinHoldingTime"),
        ("IPOA-MIB", "ipoaLisQDepth"),
        ("IPOA-MIB", "ipoaLisMaxCalls"),
        ("IPOA-MIB", "ipoaLisCacheEntryAge"),
        ("IPOA-MIB", "ipoaLisRetries"),
        ("IPOA-MIB", "ipoaLisTimeout"),
        ("IPOA-MIB", "ipoaLisDefaultPeakCellRate"),
        ("IPOA-MIB", "ipoaLisActiveVcs"),
        ("IPOA-MIB", "ipoaLisRowStatus"),
        ("IPOA-MIB", "ipoaLisIfMappingRowStatus"),
        ("IPOA-MIB", "ipoaArpRemoteSrvrRowStatus"),
        ("IPOA-MIB", "ipoaArpRemoteSrvrIpAddr"),
        ("IPOA-MIB", "ipoaArpRemoteSrvrAdminStatus"),
        ("IPOA-MIB", "ipoaArpRemoteSrvrOperStatus"))
)
if mibBuilder.loadTexts:
    ipoaLisTableGroup.setStatus("current")


# Notification objects

ipoaMtuExceeded = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 1)
)
ipoaMtuExceeded.setObjects(
    ("IPOA-MIB", "ipoaVcNegotiatedMtu")
)
if mibBuilder.loadTexts:
    ipoaMtuExceeded.setStatus(
        "current"
    )

ipoaDuplicateIpAddress = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 2)
)
ipoaDuplicateIpAddress.setObjects(
      *(("IP-MIB", "ipNetToMediaIfIndex"),
        ("IP-MIB", "ipNetToMediaNetAddress"),
        ("IP-MIB", "ipNetToMediaPhysAddress"),
        ("IP-MIB", "ipNetToMediaPhysAddress"))
)
if mibBuilder.loadTexts:
    ipoaDuplicateIpAddress.setStatus(
        "current"
    )

ipoaLisCreate = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 3)
)
ipoaLisCreate.setObjects(
    ("IPOA-MIB", "ipoaLisSubnetAddr")
)
if mibBuilder.loadTexts:
    ipoaLisCreate.setStatus(
        "current"
    )

ipoaLisDelete = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 4)
)
ipoaLisDelete.setObjects(
    ("IPOA-MIB", "ipoaLisSubnetAddr")
)
if mibBuilder.loadTexts:
    ipoaLisDelete.setStatus(
        "current"
    )


# Notifications groups

ipoaBasicNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 4)
)
ipoaBasicNotificationsGroup.setObjects(
    ("IPOA-MIB", "ipoaMtuExceeded")
)
if mibBuilder.loadTexts:
    ipoaBasicNotificationsGroup.setStatus(
        "current"
    )

ipoaSrvrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 5)
)
ipoaSrvrNotificationsGroup.setObjects(
    ("IPOA-MIB", "ipoaDuplicateIpAddress")
)
if mibBuilder.loadTexts:
    ipoaSrvrNotificationsGroup.setStatus(
        "current"
    )

ipoaLisNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 6)
)
ipoaLisNotificationsGroup.setObjects(
      *(("IPOA-MIB", "ipoaLisCreate"),
        ("IPOA-MIB", "ipoaLisDelete"))
)
if mibBuilder.loadTexts:
    ipoaLisNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ipoaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 46, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ipoaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPOA-MIB",
    **{"IpoaEncapsType": IpoaEncapsType,
       "IpoaVpiInteger": IpoaVpiInteger,
       "IpoaVciInteger": IpoaVciInteger,
       "IpoaAtmAddr": IpoaAtmAddr,
       "IpoaAtmConnKind": IpoaAtmConnKind,
       "ipoaMIB": ipoaMIB,
       "ipoaObjects": ipoaObjects,
       "ipoaLisTrapEnable": ipoaLisTrapEnable,
       "ipoaLisTable": ipoaLisTable,
       "ipoaLisEntry": ipoaLisEntry,
       "ipoaLisSubnetAddr": ipoaLisSubnetAddr,
       "ipoaLisDefaultMtu": ipoaLisDefaultMtu,
       "ipoaLisDefaultEncapsType": ipoaLisDefaultEncapsType,
       "ipoaLisInactivityTimer": ipoaLisInactivityTimer,
       "ipoaLisMinHoldingTime": ipoaLisMinHoldingTime,
       "ipoaLisQDepth": ipoaLisQDepth,
       "ipoaLisMaxCalls": ipoaLisMaxCalls,
       "ipoaLisCacheEntryAge": ipoaLisCacheEntryAge,
       "ipoaLisRetries": ipoaLisRetries,
       "ipoaLisTimeout": ipoaLisTimeout,
       "ipoaLisDefaultPeakCellRate": ipoaLisDefaultPeakCellRate,
       "ipoaLisActiveVcs": ipoaLisActiveVcs,
       "ipoaLisRowStatus": ipoaLisRowStatus,
       "ipoaLisIfMappingTable": ipoaLisIfMappingTable,
       "ipoaLisIfMappingEntry": ipoaLisIfMappingEntry,
       "ipoaLisIfMappingIfIndex": ipoaLisIfMappingIfIndex,
       "ipoaLisIfMappingRowStatus": ipoaLisIfMappingRowStatus,
       "ipoaArpClientTable": ipoaArpClientTable,
       "ipoaArpClientEntry": ipoaArpClientEntry,
       "ipoaArpClientAtmAddr": ipoaArpClientAtmAddr,
       "ipoaArpClientSrvrInUse": ipoaArpClientSrvrInUse,
       "ipoaArpClientInArpInReqs": ipoaArpClientInArpInReqs,
       "ipoaArpClientInArpOutReqs": ipoaArpClientInArpOutReqs,
       "ipoaArpClientInArpInReplies": ipoaArpClientInArpInReplies,
       "ipoaArpClientInArpOutReplies": ipoaArpClientInArpOutReplies,
       "ipoaArpClientInArpInvalidInReqs": ipoaArpClientInArpInvalidInReqs,
       "ipoaArpClientInArpInvalidOutReqs": ipoaArpClientInArpInvalidOutReqs,
       "ipoaArpClientArpInReqs": ipoaArpClientArpInReqs,
       "ipoaArpClientArpOutReqs": ipoaArpClientArpOutReqs,
       "ipoaArpClientArpInReplies": ipoaArpClientArpInReplies,
       "ipoaArpClientArpOutReplies": ipoaArpClientArpOutReplies,
       "ipoaArpClientArpInNaks": ipoaArpClientArpInNaks,
       "ipoaArpClientArpOutNaks": ipoaArpClientArpOutNaks,
       "ipoaArpClientArpUnknownOps": ipoaArpClientArpUnknownOps,
       "ipoaArpClientArpNoSrvrResps": ipoaArpClientArpNoSrvrResps,
       "ipoaArpClientRowStatus": ipoaArpClientRowStatus,
       "ipoaArpSrvrTable": ipoaArpSrvrTable,
       "ipoaArpSrvrEntry": ipoaArpSrvrEntry,
       "ipoaArpSrvrAddr": ipoaArpSrvrAddr,
       "ipoaArpSrvrLis": ipoaArpSrvrLis,
       "ipoaArpSrvrInArpInReqs": ipoaArpSrvrInArpInReqs,
       "ipoaArpSrvrInArpOutReqs": ipoaArpSrvrInArpOutReqs,
       "ipoaArpSrvrInArpInReplies": ipoaArpSrvrInArpInReplies,
       "ipoaArpSrvrInArpOutReplies": ipoaArpSrvrInArpOutReplies,
       "ipoaArpSrvrInArpInvalidInReqs": ipoaArpSrvrInArpInvalidInReqs,
       "ipoaArpSrvrInArpInvalidOutReqs": ipoaArpSrvrInArpInvalidOutReqs,
       "ipoaArpSrvrArpInReqs": ipoaArpSrvrArpInReqs,
       "ipoaArpSrvrArpOutReplies": ipoaArpSrvrArpOutReplies,
       "ipoaArpSrvrArpOutNaks": ipoaArpSrvrArpOutNaks,
       "ipoaArpSrvrArpDupIpAddrs": ipoaArpSrvrArpDupIpAddrs,
       "ipoaArpSrvrArpUnknownOps": ipoaArpSrvrArpUnknownOps,
       "ipoaArpSrvrRowStatus": ipoaArpSrvrRowStatus,
       "ipoaArpRemoteSrvrTable": ipoaArpRemoteSrvrTable,
       "ipoaArpRemoteSrvrEntry": ipoaArpRemoteSrvrEntry,
       "ipoaArpRemoteSrvrAtmAddr": ipoaArpRemoteSrvrAtmAddr,
       "ipoaArpRemoteSrvrRowStatus": ipoaArpRemoteSrvrRowStatus,
       "ipoaArpRemoteSrvrIfIndex": ipoaArpRemoteSrvrIfIndex,
       "ipoaArpRemoteSrvrIpAddr": ipoaArpRemoteSrvrIpAddr,
       "ipoaArpRemoteSrvrAdminStatus": ipoaArpRemoteSrvrAdminStatus,
       "ipoaArpRemoteSrvrOperStatus": ipoaArpRemoteSrvrOperStatus,
       "ipoaVcTable": ipoaVcTable,
       "ipoaVcEntry": ipoaVcEntry,
       "ipoaVcVpi": ipoaVcVpi,
       "ipoaVcVci": ipoaVcVci,
       "ipoaVcType": ipoaVcType,
       "ipoaVcNegotiatedEncapsType": ipoaVcNegotiatedEncapsType,
       "ipoaVcNegotiatedMtu": ipoaVcNegotiatedMtu,
       "ipoaConfigPvcTable": ipoaConfigPvcTable,
       "ipoaConfigPvcEntry": ipoaConfigPvcEntry,
       "ipoaConfigPvcIfIndex": ipoaConfigPvcIfIndex,
       "ipoaConfigPvcVpi": ipoaConfigPvcVpi,
       "ipoaConfigPvcVci": ipoaConfigPvcVci,
       "ipoaConfigPvcDefaultMtu": ipoaConfigPvcDefaultMtu,
       "ipoaConfigPvcRowStatus": ipoaConfigPvcRowStatus,
       "ipoaNotifications": ipoaNotifications,
       "ipoaTrapPrefix": ipoaTrapPrefix,
       "ipoaMtuExceeded": ipoaMtuExceeded,
       "ipoaDuplicateIpAddress": ipoaDuplicateIpAddress,
       "ipoaLisCreate": ipoaLisCreate,
       "ipoaLisDelete": ipoaLisDelete,
       "ipoaConformance": ipoaConformance,
       "ipoaGroups": ipoaGroups,
       "ipoaGeneralGroup": ipoaGeneralGroup,
       "ipoaClientGroup": ipoaClientGroup,
       "ipoaSrvrGroup": ipoaSrvrGroup,
       "ipoaBasicNotificationsGroup": ipoaBasicNotificationsGroup,
       "ipoaSrvrNotificationsGroup": ipoaSrvrNotificationsGroup,
       "ipoaLisNotificationsGroup": ipoaLisNotificationsGroup,
       "ipoaLisTableGroup": ipoaLisTableGroup,
       "ipoaCompliances": ipoaCompliances,
       "ipoaCompliance": ipoaCompliance}
)
