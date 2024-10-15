# SNMP MIB module (CABH-CAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CABH-CAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:51:58 2024
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

(clabProjCableHome,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjCableHome")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cabhCapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3)
)
cabhCapMib.setRevisions(
        ("2005-02-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CabhCapObjects_ObjectIdentity = ObjectIdentity
cabhCapObjects = _CabhCapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1)
)
_CabhCapBase_ObjectIdentity = ObjectIdentity
cabhCapBase = _CabhCapBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1)
)


class _CabhCapTcpTimeWait_Type(Unsigned32):
    """Custom type cabhCapTcpTimeWait based on Unsigned32"""
    defaultValue = 300


_CabhCapTcpTimeWait_Object = MibScalar
cabhCapTcpTimeWait = _CabhCapTcpTimeWait_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 1),
    _CabhCapTcpTimeWait_Type()
)
cabhCapTcpTimeWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCapTcpTimeWait.setStatus("current")
if mibBuilder.loadTexts:
    cabhCapTcpTimeWait.setUnits("seconds")


class _CabhCapUdpTimeWait_Type(Unsigned32):
    """Custom type cabhCapUdpTimeWait based on Unsigned32"""
    defaultValue = 300


_CabhCapUdpTimeWait_Object = MibScalar
cabhCapUdpTimeWait = _CabhCapUdpTimeWait_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 2),
    _CabhCapUdpTimeWait_Type()
)
cabhCapUdpTimeWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCapUdpTimeWait.setStatus("current")
if mibBuilder.loadTexts:
    cabhCapUdpTimeWait.setUnits("seconds")


class _CabhCapIcmpTimeWait_Type(Unsigned32):
    """Custom type cabhCapIcmpTimeWait based on Unsigned32"""
    defaultValue = 300


_CabhCapIcmpTimeWait_Object = MibScalar
cabhCapIcmpTimeWait = _CabhCapIcmpTimeWait_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 3),
    _CabhCapIcmpTimeWait_Type()
)
cabhCapIcmpTimeWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCapIcmpTimeWait.setStatus("current")
if mibBuilder.loadTexts:
    cabhCapIcmpTimeWait.setUnits("seconds")


class _CabhCapPrimaryMode_Type(Integer32):
    """Custom type cabhCapPrimaryMode based on Integer32"""
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
        *(("napt", 1),
          ("nat", 2),
          ("passthrough", 3))
    )


_CabhCapPrimaryMode_Type.__name__ = "Integer32"
_CabhCapPrimaryMode_Object = MibScalar
cabhCapPrimaryMode = _CabhCapPrimaryMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 4),
    _CabhCapPrimaryMode_Type()
)
cabhCapPrimaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCapPrimaryMode.setStatus("current")
_CabhCapSetToFactory_Type = TruthValue
_CabhCapSetToFactory_Object = MibScalar
cabhCapSetToFactory = _CabhCapSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 5),
    _CabhCapSetToFactory_Type()
)
cabhCapSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCapSetToFactory.setStatus("current")
_CabhCapLastSetToFactory_Type = TimeStamp
_CabhCapLastSetToFactory_Object = MibScalar
cabhCapLastSetToFactory = _CabhCapLastSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 6),
    _CabhCapLastSetToFactory_Type()
)
cabhCapLastSetToFactory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCapLastSetToFactory.setStatus("current")


class _CabhCapUpnpPortForwardingEnable_Type(TruthValue):
    """Custom type cabhCapUpnpPortForwardingEnable based on TruthValue"""
    defaultValue = 1


_CabhCapUpnpPortForwardingEnable_Object = MibScalar
cabhCapUpnpPortForwardingEnable = _CabhCapUpnpPortForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 7),
    _CabhCapUpnpPortForwardingEnable_Type()
)
cabhCapUpnpPortForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCapUpnpPortForwardingEnable.setStatus("current")


class _CabhCapUpnpTimeWait_Type(Unsigned32):
    """Custom type cabhCapUpnpTimeWait based on Unsigned32"""
    defaultValue = 0


_CabhCapUpnpTimeWait_Object = MibScalar
cabhCapUpnpTimeWait = _CabhCapUpnpTimeWait_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 8),
    _CabhCapUpnpTimeWait_Type()
)
cabhCapUpnpTimeWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCapUpnpTimeWait.setStatus("current")
if mibBuilder.loadTexts:
    cabhCapUpnpTimeWait.setUnits("seconds")
_CabhCapMap_ObjectIdentity = ObjectIdentity
cabhCapMap = _CabhCapMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2)
)
_CabhCapMappingTable_Object = MibTable
cabhCapMappingTable = _CabhCapMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cabhCapMappingTable.setStatus("current")
_CabhCapMappingEntry_Object = MibTableRow
cabhCapMappingEntry = _CabhCapMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1)
)
cabhCapMappingEntry.setIndexNames(
    (0, "CABH-CAP-MIB", "cabhCapMappingIndex"),
)
if mibBuilder.loadTexts:
    cabhCapMappingEntry.setStatus("current")


class _CabhCapMappingIndex_Type(Integer32):
    """Custom type cabhCapMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CabhCapMappingIndex_Type.__name__ = "Integer32"
_CabhCapMappingIndex_Object = MibTableColumn
cabhCapMappingIndex = _CabhCapMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 1),
    _CabhCapMappingIndex_Type()
)
cabhCapMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhCapMappingIndex.setStatus("current")


class _CabhCapMappingWanAddrType_Type(InetAddressType):
    """Custom type cabhCapMappingWanAddrType based on InetAddressType"""


_CabhCapMappingWanAddrType_Object = MibTableColumn
cabhCapMappingWanAddrType = _CabhCapMappingWanAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 2),
    _CabhCapMappingWanAddrType_Type()
)
cabhCapMappingWanAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapMappingWanAddrType.setStatus("current")
_CabhCapMappingWanAddr_Type = InetAddress
_CabhCapMappingWanAddr_Object = MibTableColumn
cabhCapMappingWanAddr = _CabhCapMappingWanAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 3),
    _CabhCapMappingWanAddr_Type()
)
cabhCapMappingWanAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapMappingWanAddr.setStatus("current")


class _CabhCapMappingWanPort_Type(InetPortNumber):
    """Custom type cabhCapMappingWanPort based on InetPortNumber"""
    defaultValue = 0


_CabhCapMappingWanPort_Object = MibTableColumn
cabhCapMappingWanPort = _CabhCapMappingWanPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 4),
    _CabhCapMappingWanPort_Type()
)
cabhCapMappingWanPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapMappingWanPort.setStatus("current")


class _CabhCapMappingLanAddrType_Type(InetAddressType):
    """Custom type cabhCapMappingLanAddrType based on InetAddressType"""


_CabhCapMappingLanAddrType_Object = MibTableColumn
cabhCapMappingLanAddrType = _CabhCapMappingLanAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 5),
    _CabhCapMappingLanAddrType_Type()
)
cabhCapMappingLanAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapMappingLanAddrType.setStatus("current")
_CabhCapMappingLanAddr_Type = InetAddress
_CabhCapMappingLanAddr_Object = MibTableColumn
cabhCapMappingLanAddr = _CabhCapMappingLanAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 6),
    _CabhCapMappingLanAddr_Type()
)
cabhCapMappingLanAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapMappingLanAddr.setStatus("current")


class _CabhCapMappingLanPort_Type(InetPortNumber):
    """Custom type cabhCapMappingLanPort based on InetPortNumber"""
    defaultValue = 0


_CabhCapMappingLanPort_Object = MibTableColumn
cabhCapMappingLanPort = _CabhCapMappingLanPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 7),
    _CabhCapMappingLanPort_Type()
)
cabhCapMappingLanPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapMappingLanPort.setStatus("current")


class _CabhCapMappingMethod_Type(Integer32):
    """Custom type cabhCapMappingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1),
          ("upnp", 3))
    )


_CabhCapMappingMethod_Type.__name__ = "Integer32"
_CabhCapMappingMethod_Object = MibTableColumn
cabhCapMappingMethod = _CabhCapMappingMethod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 8),
    _CabhCapMappingMethod_Type()
)
cabhCapMappingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCapMappingMethod.setStatus("current")


class _CabhCapMappingProtocol_Type(Integer32):
    """Custom type cabhCapMappingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("all", 255),
          ("icmp", 2),
          ("other", 1),
          ("tcp", 4),
          ("udp", 3))
    )


_CabhCapMappingProtocol_Type.__name__ = "Integer32"
_CabhCapMappingProtocol_Object = MibTableColumn
cabhCapMappingProtocol = _CabhCapMappingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 9),
    _CabhCapMappingProtocol_Type()
)
cabhCapMappingProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapMappingProtocol.setStatus("current")
_CabhCapMappingRowStatus_Type = RowStatus
_CabhCapMappingRowStatus_Object = MibTableColumn
cabhCapMappingRowStatus = _CabhCapMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 10),
    _CabhCapMappingRowStatus_Type()
)
cabhCapMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapMappingRowStatus.setStatus("current")


class _CabhCapMappingNumPorts_Type(Unsigned32):
    """Custom type cabhCapMappingNumPorts based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CabhCapMappingNumPorts_Type.__name__ = "Unsigned32"
_CabhCapMappingNumPorts_Object = MibTableColumn
cabhCapMappingNumPorts = _CabhCapMappingNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 11),
    _CabhCapMappingNumPorts_Type()
)
cabhCapMappingNumPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapMappingNumPorts.setStatus("current")


class _CabhCapMappingRowDescr_Type(SnmpAdminString):
    """Custom type cabhCapMappingRowDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhCapMappingRowDescr_Type.__name__ = "SnmpAdminString"
_CabhCapMappingRowDescr_Object = MibTableColumn
cabhCapMappingRowDescr = _CabhCapMappingRowDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 12),
    _CabhCapMappingRowDescr_Type()
)
cabhCapMappingRowDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapMappingRowDescr.setStatus("current")
_CabhCapMappingCreateTime_Type = DateAndTime
_CabhCapMappingCreateTime_Object = MibTableColumn
cabhCapMappingCreateTime = _CabhCapMappingCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 13),
    _CabhCapMappingCreateTime_Type()
)
cabhCapMappingCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCapMappingCreateTime.setStatus("current")
_CabhCapMappingLastUpdateTime_Type = DateAndTime
_CabhCapMappingLastUpdateTime_Object = MibTableColumn
cabhCapMappingLastUpdateTime = _CabhCapMappingLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 14),
    _CabhCapMappingLastUpdateTime_Type()
)
cabhCapMappingLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCapMappingLastUpdateTime.setStatus("current")


class _CabhCapMappingDuration_Type(Integer32):
    """Custom type cabhCapMappingDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_CabhCapMappingDuration_Type.__name__ = "Integer32"
_CabhCapMappingDuration_Object = MibTableColumn
cabhCapMappingDuration = _CabhCapMappingDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 15),
    _CabhCapMappingDuration_Type()
)
cabhCapMappingDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapMappingDuration.setStatus("current")
if mibBuilder.loadTexts:
    cabhCapMappingDuration.setUnits("seconds")


class _CabhCapMappingRemoteHostAddrType_Type(InetAddressType):
    """Custom type cabhCapMappingRemoteHostAddrType based on InetAddressType"""


_CabhCapMappingRemoteHostAddrType_Object = MibTableColumn
cabhCapMappingRemoteHostAddrType = _CabhCapMappingRemoteHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 16),
    _CabhCapMappingRemoteHostAddrType_Type()
)
cabhCapMappingRemoteHostAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCapMappingRemoteHostAddrType.setStatus("current")


class _CabhCapMappingRemoteHostAddr_Type(InetAddress):
    """Custom type cabhCapMappingRemoteHostAddr based on InetAddress"""
    defaultHexValue = "00000000"


_CabhCapMappingRemoteHostAddr_Object = MibTableColumn
cabhCapMappingRemoteHostAddr = _CabhCapMappingRemoteHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 17),
    _CabhCapMappingRemoteHostAddr_Type()
)
cabhCapMappingRemoteHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCapMappingRemoteHostAddr.setStatus("current")


class _CabhCapMappingEnable_Type(TruthValue):
    """Custom type cabhCapMappingEnable based on TruthValue"""


_CabhCapMappingEnable_Object = MibTableColumn
cabhCapMappingEnable = _CabhCapMappingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 18),
    _CabhCapMappingEnable_Type()
)
cabhCapMappingEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCapMappingEnable.setStatus("current")
_CabhCapPassthroughTable_Object = MibTable
cabhCapPassthroughTable = _CabhCapPassthroughTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cabhCapPassthroughTable.setStatus("current")
_CabhCapPassthroughEntry_Object = MibTableRow
cabhCapPassthroughEntry = _CabhCapPassthroughEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 2, 1)
)
cabhCapPassthroughEntry.setIndexNames(
    (0, "CABH-CAP-MIB", "cabhCapPassthroughIndex"),
)
if mibBuilder.loadTexts:
    cabhCapPassthroughEntry.setStatus("current")


class _CabhCapPassthroughIndex_Type(Integer32):
    """Custom type cabhCapPassthroughIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CabhCapPassthroughIndex_Type.__name__ = "Integer32"
_CabhCapPassthroughIndex_Object = MibTableColumn
cabhCapPassthroughIndex = _CabhCapPassthroughIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 2, 1, 1),
    _CabhCapPassthroughIndex_Type()
)
cabhCapPassthroughIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhCapPassthroughIndex.setStatus("current")


class _CabhCapPassthroughMacAddr_Type(PhysAddress):
    """Custom type cabhCapPassthroughMacAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CabhCapPassthroughMacAddr_Type.__name__ = "PhysAddress"
_CabhCapPassthroughMacAddr_Object = MibTableColumn
cabhCapPassthroughMacAddr = _CabhCapPassthroughMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 2, 1, 2),
    _CabhCapPassthroughMacAddr_Type()
)
cabhCapPassthroughMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapPassthroughMacAddr.setStatus("current")
_CabhCapPassthroughRowStatus_Type = RowStatus
_CabhCapPassthroughRowStatus_Object = MibTableColumn
cabhCapPassthroughRowStatus = _CabhCapPassthroughRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 2, 1, 3),
    _CabhCapPassthroughRowStatus_Type()
)
cabhCapPassthroughRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCapPassthroughRowStatus.setStatus("current")
_CabhCapNotification_ObjectIdentity = ObjectIdentity
cabhCapNotification = _CabhCapNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 2, 0)
)
_CabhCapConformance_ObjectIdentity = ObjectIdentity
cabhCapConformance = _CabhCapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 3)
)
_CabhCapCompliances_ObjectIdentity = ObjectIdentity
cabhCapCompliances = _CabhCapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 3, 1)
)
_CabhCapGroups_ObjectIdentity = ObjectIdentity
cabhCapGroups = _CabhCapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 3, 2)
)

# Managed Objects groups

cabhCapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 3, 2, 1)
)
cabhCapGroup.setObjects(
      *(("CABH-CAP-MIB", "cabhCapTcpTimeWait"),
        ("CABH-CAP-MIB", "cabhCapUdpTimeWait"),
        ("CABH-CAP-MIB", "cabhCapIcmpTimeWait"),
        ("CABH-CAP-MIB", "cabhCapPrimaryMode"),
        ("CABH-CAP-MIB", "cabhCapSetToFactory"),
        ("CABH-CAP-MIB", "cabhCapLastSetToFactory"),
        ("CABH-CAP-MIB", "cabhCapMappingWanAddrType"),
        ("CABH-CAP-MIB", "cabhCapMappingWanAddr"),
        ("CABH-CAP-MIB", "cabhCapMappingWanPort"),
        ("CABH-CAP-MIB", "cabhCapMappingLanAddrType"),
        ("CABH-CAP-MIB", "cabhCapMappingLanAddr"),
        ("CABH-CAP-MIB", "cabhCapMappingLanPort"),
        ("CABH-CAP-MIB", "cabhCapMappingMethod"),
        ("CABH-CAP-MIB", "cabhCapMappingProtocol"),
        ("CABH-CAP-MIB", "cabhCapMappingRowStatus"),
        ("CABH-CAP-MIB", "cabhCapPassthroughMacAddr"),
        ("CABH-CAP-MIB", "cabhCapPassthroughRowStatus"),
        ("CABH-CAP-MIB", "cabhCapMappingNumPorts"),
        ("CABH-CAP-MIB", "cabhCapMappingRowDescr"),
        ("CABH-CAP-MIB", "cabhCapMappingCreateTime"),
        ("CABH-CAP-MIB", "cabhCapMappingLastUpdateTime"),
        ("CABH-CAP-MIB", "cabhCapMappingDuration"),
        ("CABH-CAP-MIB", "cabhCapUpnpPortForwardingEnable"),
        ("CABH-CAP-MIB", "cabhCapUpnpTimeWait"),
        ("CABH-CAP-MIB", "cabhCapMappingRemoteHostAddrType"),
        ("CABH-CAP-MIB", "cabhCapMappingRemoteHostAddr"),
        ("CABH-CAP-MIB", "cabhCapMappingEnable"))
)
if mibBuilder.loadTexts:
    cabhCapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cabhCapBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cabhCapBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CABH-CAP-MIB",
    **{"cabhCapMib": cabhCapMib,
       "cabhCapObjects": cabhCapObjects,
       "cabhCapBase": cabhCapBase,
       "cabhCapTcpTimeWait": cabhCapTcpTimeWait,
       "cabhCapUdpTimeWait": cabhCapUdpTimeWait,
       "cabhCapIcmpTimeWait": cabhCapIcmpTimeWait,
       "cabhCapPrimaryMode": cabhCapPrimaryMode,
       "cabhCapSetToFactory": cabhCapSetToFactory,
       "cabhCapLastSetToFactory": cabhCapLastSetToFactory,
       "cabhCapUpnpPortForwardingEnable": cabhCapUpnpPortForwardingEnable,
       "cabhCapUpnpTimeWait": cabhCapUpnpTimeWait,
       "cabhCapMap": cabhCapMap,
       "cabhCapMappingTable": cabhCapMappingTable,
       "cabhCapMappingEntry": cabhCapMappingEntry,
       "cabhCapMappingIndex": cabhCapMappingIndex,
       "cabhCapMappingWanAddrType": cabhCapMappingWanAddrType,
       "cabhCapMappingWanAddr": cabhCapMappingWanAddr,
       "cabhCapMappingWanPort": cabhCapMappingWanPort,
       "cabhCapMappingLanAddrType": cabhCapMappingLanAddrType,
       "cabhCapMappingLanAddr": cabhCapMappingLanAddr,
       "cabhCapMappingLanPort": cabhCapMappingLanPort,
       "cabhCapMappingMethod": cabhCapMappingMethod,
       "cabhCapMappingProtocol": cabhCapMappingProtocol,
       "cabhCapMappingRowStatus": cabhCapMappingRowStatus,
       "cabhCapMappingNumPorts": cabhCapMappingNumPorts,
       "cabhCapMappingRowDescr": cabhCapMappingRowDescr,
       "cabhCapMappingCreateTime": cabhCapMappingCreateTime,
       "cabhCapMappingLastUpdateTime": cabhCapMappingLastUpdateTime,
       "cabhCapMappingDuration": cabhCapMappingDuration,
       "cabhCapMappingRemoteHostAddrType": cabhCapMappingRemoteHostAddrType,
       "cabhCapMappingRemoteHostAddr": cabhCapMappingRemoteHostAddr,
       "cabhCapMappingEnable": cabhCapMappingEnable,
       "cabhCapPassthroughTable": cabhCapPassthroughTable,
       "cabhCapPassthroughEntry": cabhCapPassthroughEntry,
       "cabhCapPassthroughIndex": cabhCapPassthroughIndex,
       "cabhCapPassthroughMacAddr": cabhCapPassthroughMacAddr,
       "cabhCapPassthroughRowStatus": cabhCapPassthroughRowStatus,
       "cabhCapNotification": cabhCapNotification,
       "cabhCapConformance": cabhCapConformance,
       "cabhCapCompliances": cabhCapCompliances,
       "cabhCapBasicCompliance": cabhCapBasicCompliance,
       "cabhCapGroups": cabhCapGroups,
       "cabhCapGroup": cabhCapGroup}
)
