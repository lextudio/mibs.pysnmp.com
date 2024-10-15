# SNMP MIB module (CABH-CDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CABH-CDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:51:59 2024
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

cabhCdpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CabhCdpObjects_ObjectIdentity = ObjectIdentity
cabhCdpObjects = _CabhCdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1)
)
_CabhCdpBase_ObjectIdentity = ObjectIdentity
cabhCdpBase = _CabhCdpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 1)
)
_CabhCdpSetToFactory_Type = TruthValue
_CabhCdpSetToFactory_Object = MibScalar
cabhCdpSetToFactory = _CabhCdpSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 1, 1),
    _CabhCdpSetToFactory_Type()
)
cabhCdpSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpSetToFactory.setStatus("current")
_CabhCdpLanTransCurCount_Type = Unsigned32
_CabhCdpLanTransCurCount_Object = MibScalar
cabhCdpLanTransCurCount = _CabhCdpLanTransCurCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 1, 2),
    _CabhCdpLanTransCurCount_Type()
)
cabhCdpLanTransCurCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpLanTransCurCount.setStatus("current")


class _CabhCdpLanTransThreshold_Type(Integer32):
    """Custom type cabhCdpLanTransThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65533),
    )


_CabhCdpLanTransThreshold_Type.__name__ = "Integer32"
_CabhCdpLanTransThreshold_Object = MibScalar
cabhCdpLanTransThreshold = _CabhCdpLanTransThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 1, 3),
    _CabhCdpLanTransThreshold_Type()
)
cabhCdpLanTransThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpLanTransThreshold.setStatus("current")


class _CabhCdpLanTransAction_Type(Integer32):
    """Custom type cabhCdpLanTransAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAssignment", 2),
          ("normal", 1))
    )


_CabhCdpLanTransAction_Type.__name__ = "Integer32"
_CabhCdpLanTransAction_Object = MibScalar
cabhCdpLanTransAction = _CabhCdpLanTransAction_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 1, 4),
    _CabhCdpLanTransAction_Type()
)
cabhCdpLanTransAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpLanTransAction.setStatus("current")


class _CabhCdpWanDataIpAddrCount_Type(Integer32):
    """Custom type cabhCdpWanDataIpAddrCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CabhCdpWanDataIpAddrCount_Type.__name__ = "Integer32"
_CabhCdpWanDataIpAddrCount_Object = MibScalar
cabhCdpWanDataIpAddrCount = _CabhCdpWanDataIpAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 1, 5),
    _CabhCdpWanDataIpAddrCount_Type()
)
cabhCdpWanDataIpAddrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpWanDataIpAddrCount.setStatus("current")
_CabhCdpLastSetToFactory_Type = TimeStamp
_CabhCdpLastSetToFactory_Object = MibScalar
cabhCdpLastSetToFactory = _CabhCdpLastSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 1, 6),
    _CabhCdpLastSetToFactory_Type()
)
cabhCdpLastSetToFactory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpLastSetToFactory.setStatus("current")


class _CabhCdpTimeOffsetSelection_Type(Integer32):
    """Custom type cabhCdpTimeOffsetSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useDhcpOption2", 1),
          ("useSnmpSetOffset", 2))
    )


_CabhCdpTimeOffsetSelection_Type.__name__ = "Integer32"
_CabhCdpTimeOffsetSelection_Object = MibScalar
cabhCdpTimeOffsetSelection = _CabhCdpTimeOffsetSelection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 1, 7),
    _CabhCdpTimeOffsetSelection_Type()
)
cabhCdpTimeOffsetSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpTimeOffsetSelection.setStatus("current")


class _CabhCdpSnmpSetTimeOffset_Type(Integer32):
    """Custom type cabhCdpSnmpSetTimeOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-43200, 46800),
    )


_CabhCdpSnmpSetTimeOffset_Type.__name__ = "Integer32"
_CabhCdpSnmpSetTimeOffset_Object = MibScalar
cabhCdpSnmpSetTimeOffset = _CabhCdpSnmpSetTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 1, 8),
    _CabhCdpSnmpSetTimeOffset_Type()
)
cabhCdpSnmpSetTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpSnmpSetTimeOffset.setStatus("current")
if mibBuilder.loadTexts:
    cabhCdpSnmpSetTimeOffset.setUnits("seconds")


class _CabhCdpDaylightSavingTimeEnable_Type(Integer32):
    """Custom type cabhCdpDaylightSavingTimeEnable based on Integer32"""
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


_CabhCdpDaylightSavingTimeEnable_Type.__name__ = "Integer32"
_CabhCdpDaylightSavingTimeEnable_Object = MibScalar
cabhCdpDaylightSavingTimeEnable = _CabhCdpDaylightSavingTimeEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 1, 9),
    _CabhCdpDaylightSavingTimeEnable_Type()
)
cabhCdpDaylightSavingTimeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpDaylightSavingTimeEnable.setStatus("current")
_CabhCdpAddr_ObjectIdentity = ObjectIdentity
cabhCdpAddr = _CabhCdpAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2)
)
_CabhCdpLanAddrTable_Object = MibTable
cabhCdpLanAddrTable = _CabhCdpLanAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cabhCdpLanAddrTable.setStatus("current")
_CabhCdpLanAddrEntry_Object = MibTableRow
cabhCdpLanAddrEntry = _CabhCdpLanAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 1, 1)
)
cabhCdpLanAddrEntry.setIndexNames(
    (0, "CABH-CDP-MIB", "cabhCdpLanAddrIpType"),
    (0, "CABH-CDP-MIB", "cabhCdpLanAddrIp"),
)
if mibBuilder.loadTexts:
    cabhCdpLanAddrEntry.setStatus("current")
_CabhCdpLanAddrIpType_Type = InetAddressType
_CabhCdpLanAddrIpType_Object = MibTableColumn
cabhCdpLanAddrIpType = _CabhCdpLanAddrIpType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 1, 1, 1),
    _CabhCdpLanAddrIpType_Type()
)
cabhCdpLanAddrIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhCdpLanAddrIpType.setStatus("current")
_CabhCdpLanAddrIp_Type = InetAddress
_CabhCdpLanAddrIp_Object = MibTableColumn
cabhCdpLanAddrIp = _CabhCdpLanAddrIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 1, 1, 2),
    _CabhCdpLanAddrIp_Type()
)
cabhCdpLanAddrIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhCdpLanAddrIp.setStatus("current")
_CabhCdpLanAddrClientID_Type = PhysAddress
_CabhCdpLanAddrClientID_Object = MibTableColumn
cabhCdpLanAddrClientID = _CabhCdpLanAddrClientID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 1, 1, 3),
    _CabhCdpLanAddrClientID_Type()
)
cabhCdpLanAddrClientID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCdpLanAddrClientID.setStatus("current")
_CabhCdpLanAddrLeaseCreateTime_Type = DateAndTime
_CabhCdpLanAddrLeaseCreateTime_Object = MibTableColumn
cabhCdpLanAddrLeaseCreateTime = _CabhCdpLanAddrLeaseCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 1, 1, 4),
    _CabhCdpLanAddrLeaseCreateTime_Type()
)
cabhCdpLanAddrLeaseCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpLanAddrLeaseCreateTime.setStatus("current")
_CabhCdpLanAddrLeaseExpireTime_Type = DateAndTime
_CabhCdpLanAddrLeaseExpireTime_Object = MibTableColumn
cabhCdpLanAddrLeaseExpireTime = _CabhCdpLanAddrLeaseExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 1, 1, 5),
    _CabhCdpLanAddrLeaseExpireTime_Type()
)
cabhCdpLanAddrLeaseExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpLanAddrLeaseExpireTime.setStatus("current")


class _CabhCdpLanAddrMethod_Type(Integer32):
    """Custom type cabhCdpLanAddrMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dynamicActive", 4),
          ("dynamicInactive", 3),
          ("mgmtReservationActive", 2),
          ("mgmtReservationInactive", 1),
          ("psReservationActive", 6),
          ("psReservationInactive", 5))
    )


_CabhCdpLanAddrMethod_Type.__name__ = "Integer32"
_CabhCdpLanAddrMethod_Object = MibTableColumn
cabhCdpLanAddrMethod = _CabhCdpLanAddrMethod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 1, 1, 6),
    _CabhCdpLanAddrMethod_Type()
)
cabhCdpLanAddrMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpLanAddrMethod.setStatus("current")


class _CabhCdpLanAddrHostName_Type(SnmpAdminString):
    """Custom type cabhCdpLanAddrHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CabhCdpLanAddrHostName_Type.__name__ = "SnmpAdminString"
_CabhCdpLanAddrHostName_Object = MibTableColumn
cabhCdpLanAddrHostName = _CabhCdpLanAddrHostName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 1, 1, 7),
    _CabhCdpLanAddrHostName_Type()
)
cabhCdpLanAddrHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpLanAddrHostName.setStatus("current")
_CabhCdpLanAddrRowStatus_Type = RowStatus
_CabhCdpLanAddrRowStatus_Object = MibTableColumn
cabhCdpLanAddrRowStatus = _CabhCdpLanAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 1, 1, 8),
    _CabhCdpLanAddrRowStatus_Type()
)
cabhCdpLanAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCdpLanAddrRowStatus.setStatus("current")
_CabhCdpWanDataAddrTable_Object = MibTable
cabhCdpWanDataAddrTable = _CabhCdpWanDataAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cabhCdpWanDataAddrTable.setStatus("current")
_CabhCdpWanDataAddrEntry_Object = MibTableRow
cabhCdpWanDataAddrEntry = _CabhCdpWanDataAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 2, 1)
)
cabhCdpWanDataAddrEntry.setIndexNames(
    (0, "CABH-CDP-MIB", "cabhCdpWanDataAddrIndex"),
)
if mibBuilder.loadTexts:
    cabhCdpWanDataAddrEntry.setStatus("current")


class _CabhCdpWanDataAddrIndex_Type(Integer32):
    """Custom type cabhCdpWanDataAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CabhCdpWanDataAddrIndex_Type.__name__ = "Integer32"
_CabhCdpWanDataAddrIndex_Object = MibTableColumn
cabhCdpWanDataAddrIndex = _CabhCdpWanDataAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 2, 1, 1),
    _CabhCdpWanDataAddrIndex_Type()
)
cabhCdpWanDataAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhCdpWanDataAddrIndex.setStatus("current")


class _CabhCdpWanDataAddrClientId_Type(OctetString):
    """Custom type cabhCdpWanDataAddrClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CabhCdpWanDataAddrClientId_Type.__name__ = "OctetString"
_CabhCdpWanDataAddrClientId_Object = MibTableColumn
cabhCdpWanDataAddrClientId = _CabhCdpWanDataAddrClientId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 2, 1, 2),
    _CabhCdpWanDataAddrClientId_Type()
)
cabhCdpWanDataAddrClientId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCdpWanDataAddrClientId.setStatus("current")


class _CabhCdpWanDataAddrIpType_Type(InetAddressType):
    """Custom type cabhCdpWanDataAddrIpType based on InetAddressType"""


_CabhCdpWanDataAddrIpType_Object = MibTableColumn
cabhCdpWanDataAddrIpType = _CabhCdpWanDataAddrIpType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 2, 1, 3),
    _CabhCdpWanDataAddrIpType_Type()
)
cabhCdpWanDataAddrIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpWanDataAddrIpType.setStatus("current")
_CabhCdpWanDataAddrIp_Type = InetAddress
_CabhCdpWanDataAddrIp_Object = MibTableColumn
cabhCdpWanDataAddrIp = _CabhCdpWanDataAddrIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 2, 1, 4),
    _CabhCdpWanDataAddrIp_Type()
)
cabhCdpWanDataAddrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpWanDataAddrIp.setStatus("current")
_CabhCdpWanDataAddrRenewalTime_Type = Integer32
_CabhCdpWanDataAddrRenewalTime_Object = MibTableColumn
cabhCdpWanDataAddrRenewalTime = _CabhCdpWanDataAddrRenewalTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 2, 1, 5),
    _CabhCdpWanDataAddrRenewalTime_Type()
)
cabhCdpWanDataAddrRenewalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpWanDataAddrRenewalTime.setStatus("deprecated")
_CabhCdpWanDataAddrRowStatus_Type = RowStatus
_CabhCdpWanDataAddrRowStatus_Object = MibTableColumn
cabhCdpWanDataAddrRowStatus = _CabhCdpWanDataAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 2, 1, 6),
    _CabhCdpWanDataAddrRowStatus_Type()
)
cabhCdpWanDataAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhCdpWanDataAddrRowStatus.setStatus("current")
_CabhCdpWanDataAddrLeaseCreateTime_Type = DateAndTime
_CabhCdpWanDataAddrLeaseCreateTime_Object = MibTableColumn
cabhCdpWanDataAddrLeaseCreateTime = _CabhCdpWanDataAddrLeaseCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 2, 1, 7),
    _CabhCdpWanDataAddrLeaseCreateTime_Type()
)
cabhCdpWanDataAddrLeaseCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpWanDataAddrLeaseCreateTime.setStatus("current")
_CabhCdpWanDataAddrLeaseExpireTime_Type = DateAndTime
_CabhCdpWanDataAddrLeaseExpireTime_Object = MibTableColumn
cabhCdpWanDataAddrLeaseExpireTime = _CabhCdpWanDataAddrLeaseExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 2, 1, 8),
    _CabhCdpWanDataAddrLeaseExpireTime_Type()
)
cabhCdpWanDataAddrLeaseExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpWanDataAddrLeaseExpireTime.setStatus("current")
_CabhCdpWanDnsServerTable_Object = MibTable
cabhCdpWanDnsServerTable = _CabhCdpWanDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cabhCdpWanDnsServerTable.setStatus("current")
_CabhCdpWanDnsServerEntry_Object = MibTableRow
cabhCdpWanDnsServerEntry = _CabhCdpWanDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 3, 1)
)
cabhCdpWanDnsServerEntry.setIndexNames(
    (0, "CABH-CDP-MIB", "cabhCdpWanDnsServerOrder"),
)
if mibBuilder.loadTexts:
    cabhCdpWanDnsServerEntry.setStatus("current")


class _CabhCdpWanDnsServerOrder_Type(Integer32):
    """Custom type cabhCdpWanDnsServerOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_CabhCdpWanDnsServerOrder_Type.__name__ = "Integer32"
_CabhCdpWanDnsServerOrder_Object = MibTableColumn
cabhCdpWanDnsServerOrder = _CabhCdpWanDnsServerOrder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 3, 1, 1),
    _CabhCdpWanDnsServerOrder_Type()
)
cabhCdpWanDnsServerOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhCdpWanDnsServerOrder.setStatus("current")


class _CabhCdpWanDnsServerIpType_Type(InetAddressType):
    """Custom type cabhCdpWanDnsServerIpType based on InetAddressType"""


_CabhCdpWanDnsServerIpType_Object = MibTableColumn
cabhCdpWanDnsServerIpType = _CabhCdpWanDnsServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 3, 1, 2),
    _CabhCdpWanDnsServerIpType_Type()
)
cabhCdpWanDnsServerIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpWanDnsServerIpType.setStatus("current")
_CabhCdpWanDnsServerIp_Type = InetAddress
_CabhCdpWanDnsServerIp_Object = MibTableColumn
cabhCdpWanDnsServerIp = _CabhCdpWanDnsServerIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 2, 3, 1, 3),
    _CabhCdpWanDnsServerIp_Type()
)
cabhCdpWanDnsServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpWanDnsServerIp.setStatus("current")
_CabhCdpServer_ObjectIdentity = ObjectIdentity
cabhCdpServer = _CabhCdpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3)
)


class _CabhCdpLanPoolStartType_Type(InetAddressType):
    """Custom type cabhCdpLanPoolStartType based on InetAddressType"""


_CabhCdpLanPoolStartType_Object = MibScalar
cabhCdpLanPoolStartType = _CabhCdpLanPoolStartType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 1),
    _CabhCdpLanPoolStartType_Type()
)
cabhCdpLanPoolStartType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpLanPoolStartType.setStatus("current")


class _CabhCdpLanPoolStart_Type(InetAddress):
    """Custom type cabhCdpLanPoolStart based on InetAddress"""
    defaultHexValue = "c0a8000a"


_CabhCdpLanPoolStart_Object = MibScalar
cabhCdpLanPoolStart = _CabhCdpLanPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 2),
    _CabhCdpLanPoolStart_Type()
)
cabhCdpLanPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpLanPoolStart.setStatus("current")


class _CabhCdpLanPoolEndType_Type(InetAddressType):
    """Custom type cabhCdpLanPoolEndType based on InetAddressType"""


_CabhCdpLanPoolEndType_Object = MibScalar
cabhCdpLanPoolEndType = _CabhCdpLanPoolEndType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 3),
    _CabhCdpLanPoolEndType_Type()
)
cabhCdpLanPoolEndType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpLanPoolEndType.setStatus("current")


class _CabhCdpLanPoolEnd_Type(InetAddress):
    """Custom type cabhCdpLanPoolEnd based on InetAddress"""
    defaultHexValue = "c0a800fe"


_CabhCdpLanPoolEnd_Object = MibScalar
cabhCdpLanPoolEnd = _CabhCdpLanPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 4),
    _CabhCdpLanPoolEnd_Type()
)
cabhCdpLanPoolEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpLanPoolEnd.setStatus("current")


class _CabhCdpServerNetworkNumberType_Type(InetAddressType):
    """Custom type cabhCdpServerNetworkNumberType based on InetAddressType"""


_CabhCdpServerNetworkNumberType_Object = MibScalar
cabhCdpServerNetworkNumberType = _CabhCdpServerNetworkNumberType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 5),
    _CabhCdpServerNetworkNumberType_Type()
)
cabhCdpServerNetworkNumberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerNetworkNumberType.setStatus("current")


class _CabhCdpServerNetworkNumber_Type(InetAddress):
    """Custom type cabhCdpServerNetworkNumber based on InetAddress"""
    defaultHexValue = "c0a80000"


_CabhCdpServerNetworkNumber_Object = MibScalar
cabhCdpServerNetworkNumber = _CabhCdpServerNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 6),
    _CabhCdpServerNetworkNumber_Type()
)
cabhCdpServerNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerNetworkNumber.setStatus("current")


class _CabhCdpServerSubnetMaskType_Type(InetAddressType):
    """Custom type cabhCdpServerSubnetMaskType based on InetAddressType"""


_CabhCdpServerSubnetMaskType_Object = MibScalar
cabhCdpServerSubnetMaskType = _CabhCdpServerSubnetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 7),
    _CabhCdpServerSubnetMaskType_Type()
)
cabhCdpServerSubnetMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerSubnetMaskType.setStatus("current")


class _CabhCdpServerSubnetMask_Type(InetAddress):
    """Custom type cabhCdpServerSubnetMask based on InetAddress"""
    defaultHexValue = "ffffff00"


_CabhCdpServerSubnetMask_Object = MibScalar
cabhCdpServerSubnetMask = _CabhCdpServerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 8),
    _CabhCdpServerSubnetMask_Type()
)
cabhCdpServerSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerSubnetMask.setStatus("current")


class _CabhCdpServerTimeOffset_Type(Integer32):
    """Custom type cabhCdpServerTimeOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-86400, 86400),
    )


_CabhCdpServerTimeOffset_Type.__name__ = "Integer32"
_CabhCdpServerTimeOffset_Object = MibScalar
cabhCdpServerTimeOffset = _CabhCdpServerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 9),
    _CabhCdpServerTimeOffset_Type()
)
cabhCdpServerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerTimeOffset.setStatus("current")
if mibBuilder.loadTexts:
    cabhCdpServerTimeOffset.setUnits("seconds")


class _CabhCdpServerRouterType_Type(InetAddressType):
    """Custom type cabhCdpServerRouterType based on InetAddressType"""


_CabhCdpServerRouterType_Object = MibScalar
cabhCdpServerRouterType = _CabhCdpServerRouterType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 10),
    _CabhCdpServerRouterType_Type()
)
cabhCdpServerRouterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerRouterType.setStatus("current")


class _CabhCdpServerRouter_Type(InetAddress):
    """Custom type cabhCdpServerRouter based on InetAddress"""
    defaultHexValue = "c0a80001"


_CabhCdpServerRouter_Object = MibScalar
cabhCdpServerRouter = _CabhCdpServerRouter_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 11),
    _CabhCdpServerRouter_Type()
)
cabhCdpServerRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerRouter.setStatus("current")


class _CabhCdpServerDnsAddressType_Type(InetAddressType):
    """Custom type cabhCdpServerDnsAddressType based on InetAddressType"""


_CabhCdpServerDnsAddressType_Object = MibScalar
cabhCdpServerDnsAddressType = _CabhCdpServerDnsAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 12),
    _CabhCdpServerDnsAddressType_Type()
)
cabhCdpServerDnsAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerDnsAddressType.setStatus("current")
_CabhCdpServerDnsAddress_Type = InetAddress
_CabhCdpServerDnsAddress_Object = MibScalar
cabhCdpServerDnsAddress = _CabhCdpServerDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 13),
    _CabhCdpServerDnsAddress_Type()
)
cabhCdpServerDnsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerDnsAddress.setStatus("current")


class _CabhCdpServerSyslogAddressType_Type(InetAddressType):
    """Custom type cabhCdpServerSyslogAddressType based on InetAddressType"""


_CabhCdpServerSyslogAddressType_Object = MibScalar
cabhCdpServerSyslogAddressType = _CabhCdpServerSyslogAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 14),
    _CabhCdpServerSyslogAddressType_Type()
)
cabhCdpServerSyslogAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerSyslogAddressType.setStatus("current")


class _CabhCdpServerSyslogAddress_Type(InetAddress):
    """Custom type cabhCdpServerSyslogAddress based on InetAddress"""
    defaultHexValue = "00000000"


_CabhCdpServerSyslogAddress_Object = MibScalar
cabhCdpServerSyslogAddress = _CabhCdpServerSyslogAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 15),
    _CabhCdpServerSyslogAddress_Type()
)
cabhCdpServerSyslogAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerSyslogAddress.setStatus("current")


class _CabhCdpServerDomainName_Type(SnmpAdminString):
    """Custom type cabhCdpServerDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CabhCdpServerDomainName_Type.__name__ = "SnmpAdminString"
_CabhCdpServerDomainName_Object = MibScalar
cabhCdpServerDomainName = _CabhCdpServerDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 16),
    _CabhCdpServerDomainName_Type()
)
cabhCdpServerDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerDomainName.setStatus("current")


class _CabhCdpServerTTL_Type(Integer32):
    """Custom type cabhCdpServerTTL based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CabhCdpServerTTL_Type.__name__ = "Integer32"
_CabhCdpServerTTL_Object = MibScalar
cabhCdpServerTTL = _CabhCdpServerTTL_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 17),
    _CabhCdpServerTTL_Type()
)
cabhCdpServerTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerTTL.setStatus("current")


class _CabhCdpServerInterfaceMTU_Type(Integer32):
    """Custom type cabhCdpServerInterfaceMTU based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(68, 4096),
    )


_CabhCdpServerInterfaceMTU_Type.__name__ = "Integer32"
_CabhCdpServerInterfaceMTU_Object = MibScalar
cabhCdpServerInterfaceMTU = _CabhCdpServerInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 18),
    _CabhCdpServerInterfaceMTU_Type()
)
cabhCdpServerInterfaceMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerInterfaceMTU.setStatus("current")


class _CabhCdpServerVendorSpecific_Type(OctetString):
    """Custom type cabhCdpServerVendorSpecific based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CabhCdpServerVendorSpecific_Type.__name__ = "OctetString"
_CabhCdpServerVendorSpecific_Object = MibScalar
cabhCdpServerVendorSpecific = _CabhCdpServerVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 19),
    _CabhCdpServerVendorSpecific_Type()
)
cabhCdpServerVendorSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerVendorSpecific.setStatus("current")


class _CabhCdpServerLeaseTime_Type(Unsigned32):
    """Custom type cabhCdpServerLeaseTime based on Unsigned32"""
    defaultValue = 3600


_CabhCdpServerLeaseTime_Object = MibScalar
cabhCdpServerLeaseTime = _CabhCdpServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 20),
    _CabhCdpServerLeaseTime_Type()
)
cabhCdpServerLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    cabhCdpServerLeaseTime.setUnits("seconds")


class _CabhCdpServerDhcpAddressType_Type(InetAddressType):
    """Custom type cabhCdpServerDhcpAddressType based on InetAddressType"""


_CabhCdpServerDhcpAddressType_Object = MibScalar
cabhCdpServerDhcpAddressType = _CabhCdpServerDhcpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 21),
    _CabhCdpServerDhcpAddressType_Type()
)
cabhCdpServerDhcpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpServerDhcpAddressType.setStatus("current")
_CabhCdpServerDhcpAddress_Type = InetAddress
_CabhCdpServerDhcpAddress_Object = MibScalar
cabhCdpServerDhcpAddress = _CabhCdpServerDhcpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 22),
    _CabhCdpServerDhcpAddress_Type()
)
cabhCdpServerDhcpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpServerDhcpAddress.setStatus("current")


class _CabhCdpServerControl_Type(Integer32):
    """Custom type cabhCdpServerControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commitConfig", 2),
          ("restoreConfig", 1))
    )


_CabhCdpServerControl_Type.__name__ = "Integer32"
_CabhCdpServerControl_Object = MibScalar
cabhCdpServerControl = _CabhCdpServerControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 23),
    _CabhCdpServerControl_Type()
)
cabhCdpServerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerControl.setStatus("current")


class _CabhCdpServerCommitStatus_Type(Integer32):
    """Custom type cabhCdpServerCommitStatus based on Integer32"""
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
        *(("commitFailed", 3),
          ("commitNeeded", 2),
          ("commitSucceeded", 1))
    )


_CabhCdpServerCommitStatus_Type.__name__ = "Integer32"
_CabhCdpServerCommitStatus_Object = MibScalar
cabhCdpServerCommitStatus = _CabhCdpServerCommitStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 24),
    _CabhCdpServerCommitStatus_Type()
)
cabhCdpServerCommitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCdpServerCommitStatus.setStatus("current")


class _CabhCdpServerUseCableDataNwDnsAddr_Type(TruthValue):
    """Custom type cabhCdpServerUseCableDataNwDnsAddr based on TruthValue"""


_CabhCdpServerUseCableDataNwDnsAddr_Object = MibScalar
cabhCdpServerUseCableDataNwDnsAddr = _CabhCdpServerUseCableDataNwDnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 1, 3, 25),
    _CabhCdpServerUseCableDataNwDnsAddr_Type()
)
cabhCdpServerUseCableDataNwDnsAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCdpServerUseCableDataNwDnsAddr.setStatus("current")
_CabhCdpNotification_ObjectIdentity = ObjectIdentity
cabhCdpNotification = _CabhCdpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 2)
)
_CabhCdpNotifications_ObjectIdentity = ObjectIdentity
cabhCdpNotifications = _CabhCdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 2, 0)
)
_CabhCdpConformance_ObjectIdentity = ObjectIdentity
cabhCdpConformance = _CabhCdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 3)
)
_CabhCdpCompliances_ObjectIdentity = ObjectIdentity
cabhCdpCompliances = _CabhCdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 3, 1)
)
_CabhCdpGroups_ObjectIdentity = ObjectIdentity
cabhCdpGroups = _CabhCdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 3, 2)
)

# Managed Objects groups

cabhCdpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 3, 2, 1)
)
cabhCdpGroup.setObjects(
      *(("CABH-CDP-MIB", "cabhCdpSetToFactory"),
        ("CABH-CDP-MIB", "cabhCdpLanTransCurCount"),
        ("CABH-CDP-MIB", "cabhCdpLanTransThreshold"),
        ("CABH-CDP-MIB", "cabhCdpLanTransAction"),
        ("CABH-CDP-MIB", "cabhCdpWanDataIpAddrCount"),
        ("CABH-CDP-MIB", "cabhCdpLastSetToFactory"),
        ("CABH-CDP-MIB", "cabhCdpTimeOffsetSelection"),
        ("CABH-CDP-MIB", "cabhCdpSnmpSetTimeOffset"),
        ("CABH-CDP-MIB", "cabhCdpDaylightSavingTimeEnable"),
        ("CABH-CDP-MIB", "cabhCdpLanAddrClientID"),
        ("CABH-CDP-MIB", "cabhCdpLanAddrLeaseCreateTime"),
        ("CABH-CDP-MIB", "cabhCdpLanAddrLeaseExpireTime"),
        ("CABH-CDP-MIB", "cabhCdpLanAddrMethod"),
        ("CABH-CDP-MIB", "cabhCdpLanAddrHostName"),
        ("CABH-CDP-MIB", "cabhCdpLanAddrRowStatus"),
        ("CABH-CDP-MIB", "cabhCdpWanDataAddrClientId"),
        ("CABH-CDP-MIB", "cabhCdpWanDataAddrIpType"),
        ("CABH-CDP-MIB", "cabhCdpWanDataAddrIp"),
        ("CABH-CDP-MIB", "cabhCdpWanDataAddrRowStatus"),
        ("CABH-CDP-MIB", "cabhCdpWanDataAddrLeaseCreateTime"),
        ("CABH-CDP-MIB", "cabhCdpWanDataAddrLeaseExpireTime"),
        ("CABH-CDP-MIB", "cabhCdpWanDnsServerIpType"),
        ("CABH-CDP-MIB", "cabhCdpWanDnsServerIp"),
        ("CABH-CDP-MIB", "cabhCdpLanPoolStartType"),
        ("CABH-CDP-MIB", "cabhCdpLanPoolStart"),
        ("CABH-CDP-MIB", "cabhCdpLanPoolEndType"),
        ("CABH-CDP-MIB", "cabhCdpLanPoolEnd"),
        ("CABH-CDP-MIB", "cabhCdpServerNetworkNumberType"),
        ("CABH-CDP-MIB", "cabhCdpServerNetworkNumber"),
        ("CABH-CDP-MIB", "cabhCdpServerSubnetMaskType"),
        ("CABH-CDP-MIB", "cabhCdpServerSubnetMask"),
        ("CABH-CDP-MIB", "cabhCdpServerTimeOffset"),
        ("CABH-CDP-MIB", "cabhCdpServerRouterType"),
        ("CABH-CDP-MIB", "cabhCdpServerRouter"),
        ("CABH-CDP-MIB", "cabhCdpServerDnsAddressType"),
        ("CABH-CDP-MIB", "cabhCdpServerDnsAddress"),
        ("CABH-CDP-MIB", "cabhCdpServerSyslogAddressType"),
        ("CABH-CDP-MIB", "cabhCdpServerSyslogAddress"),
        ("CABH-CDP-MIB", "cabhCdpServerDomainName"),
        ("CABH-CDP-MIB", "cabhCdpServerTTL"),
        ("CABH-CDP-MIB", "cabhCdpServerInterfaceMTU"),
        ("CABH-CDP-MIB", "cabhCdpServerVendorSpecific"),
        ("CABH-CDP-MIB", "cabhCdpServerLeaseTime"),
        ("CABH-CDP-MIB", "cabhCdpServerDhcpAddressType"),
        ("CABH-CDP-MIB", "cabhCdpServerDhcpAddress"),
        ("CABH-CDP-MIB", "cabhCdpServerControl"),
        ("CABH-CDP-MIB", "cabhCdpServerCommitStatus"),
        ("CABH-CDP-MIB", "cabhCdpServerUseCableDataNwDnsAddr"))
)
if mibBuilder.loadTexts:
    cabhCdpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cabhCdpBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 4, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cabhCdpBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CABH-CDP-MIB",
    **{"cabhCdpMib": cabhCdpMib,
       "cabhCdpObjects": cabhCdpObjects,
       "cabhCdpBase": cabhCdpBase,
       "cabhCdpSetToFactory": cabhCdpSetToFactory,
       "cabhCdpLanTransCurCount": cabhCdpLanTransCurCount,
       "cabhCdpLanTransThreshold": cabhCdpLanTransThreshold,
       "cabhCdpLanTransAction": cabhCdpLanTransAction,
       "cabhCdpWanDataIpAddrCount": cabhCdpWanDataIpAddrCount,
       "cabhCdpLastSetToFactory": cabhCdpLastSetToFactory,
       "cabhCdpTimeOffsetSelection": cabhCdpTimeOffsetSelection,
       "cabhCdpSnmpSetTimeOffset": cabhCdpSnmpSetTimeOffset,
       "cabhCdpDaylightSavingTimeEnable": cabhCdpDaylightSavingTimeEnable,
       "cabhCdpAddr": cabhCdpAddr,
       "cabhCdpLanAddrTable": cabhCdpLanAddrTable,
       "cabhCdpLanAddrEntry": cabhCdpLanAddrEntry,
       "cabhCdpLanAddrIpType": cabhCdpLanAddrIpType,
       "cabhCdpLanAddrIp": cabhCdpLanAddrIp,
       "cabhCdpLanAddrClientID": cabhCdpLanAddrClientID,
       "cabhCdpLanAddrLeaseCreateTime": cabhCdpLanAddrLeaseCreateTime,
       "cabhCdpLanAddrLeaseExpireTime": cabhCdpLanAddrLeaseExpireTime,
       "cabhCdpLanAddrMethod": cabhCdpLanAddrMethod,
       "cabhCdpLanAddrHostName": cabhCdpLanAddrHostName,
       "cabhCdpLanAddrRowStatus": cabhCdpLanAddrRowStatus,
       "cabhCdpWanDataAddrTable": cabhCdpWanDataAddrTable,
       "cabhCdpWanDataAddrEntry": cabhCdpWanDataAddrEntry,
       "cabhCdpWanDataAddrIndex": cabhCdpWanDataAddrIndex,
       "cabhCdpWanDataAddrClientId": cabhCdpWanDataAddrClientId,
       "cabhCdpWanDataAddrIpType": cabhCdpWanDataAddrIpType,
       "cabhCdpWanDataAddrIp": cabhCdpWanDataAddrIp,
       "cabhCdpWanDataAddrRenewalTime": cabhCdpWanDataAddrRenewalTime,
       "cabhCdpWanDataAddrRowStatus": cabhCdpWanDataAddrRowStatus,
       "cabhCdpWanDataAddrLeaseCreateTime": cabhCdpWanDataAddrLeaseCreateTime,
       "cabhCdpWanDataAddrLeaseExpireTime": cabhCdpWanDataAddrLeaseExpireTime,
       "cabhCdpWanDnsServerTable": cabhCdpWanDnsServerTable,
       "cabhCdpWanDnsServerEntry": cabhCdpWanDnsServerEntry,
       "cabhCdpWanDnsServerOrder": cabhCdpWanDnsServerOrder,
       "cabhCdpWanDnsServerIpType": cabhCdpWanDnsServerIpType,
       "cabhCdpWanDnsServerIp": cabhCdpWanDnsServerIp,
       "cabhCdpServer": cabhCdpServer,
       "cabhCdpLanPoolStartType": cabhCdpLanPoolStartType,
       "cabhCdpLanPoolStart": cabhCdpLanPoolStart,
       "cabhCdpLanPoolEndType": cabhCdpLanPoolEndType,
       "cabhCdpLanPoolEnd": cabhCdpLanPoolEnd,
       "cabhCdpServerNetworkNumberType": cabhCdpServerNetworkNumberType,
       "cabhCdpServerNetworkNumber": cabhCdpServerNetworkNumber,
       "cabhCdpServerSubnetMaskType": cabhCdpServerSubnetMaskType,
       "cabhCdpServerSubnetMask": cabhCdpServerSubnetMask,
       "cabhCdpServerTimeOffset": cabhCdpServerTimeOffset,
       "cabhCdpServerRouterType": cabhCdpServerRouterType,
       "cabhCdpServerRouter": cabhCdpServerRouter,
       "cabhCdpServerDnsAddressType": cabhCdpServerDnsAddressType,
       "cabhCdpServerDnsAddress": cabhCdpServerDnsAddress,
       "cabhCdpServerSyslogAddressType": cabhCdpServerSyslogAddressType,
       "cabhCdpServerSyslogAddress": cabhCdpServerSyslogAddress,
       "cabhCdpServerDomainName": cabhCdpServerDomainName,
       "cabhCdpServerTTL": cabhCdpServerTTL,
       "cabhCdpServerInterfaceMTU": cabhCdpServerInterfaceMTU,
       "cabhCdpServerVendorSpecific": cabhCdpServerVendorSpecific,
       "cabhCdpServerLeaseTime": cabhCdpServerLeaseTime,
       "cabhCdpServerDhcpAddressType": cabhCdpServerDhcpAddressType,
       "cabhCdpServerDhcpAddress": cabhCdpServerDhcpAddress,
       "cabhCdpServerControl": cabhCdpServerControl,
       "cabhCdpServerCommitStatus": cabhCdpServerCommitStatus,
       "cabhCdpServerUseCableDataNwDnsAddr": cabhCdpServerUseCableDataNwDnsAddr,
       "cabhCdpNotification": cabhCdpNotification,
       "cabhCdpNotifications": cabhCdpNotifications,
       "cabhCdpConformance": cabhCdpConformance,
       "cabhCdpCompliances": cabhCdpCompliances,
       "cabhCdpBasicCompliance": cabhCdpBasicCompliance,
       "cabhCdpGroups": cabhCdpGroups,
       "cabhCdpGroup": cabhCdpGroup}
)
