# SNMP MIB module (DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:01 2024
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

dellNetVirtualLinkTrunkMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17)
)
dellNetVirtualLinkTrunkMib.setRevisions(
        ("2012-11-28 00:00",
         "2012-05-21 00:00",
         "2012-05-14 00:00",
         "2012-04-02 00:00",
         "2011-05-06 00:00",
         "2011-03-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DellNetVLTMemberLinkStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("linkDown", 2),
          ("linkError", 3),
          ("linkNotEstablished", 0),
          ("linkUp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_DellNetVirtualLinkTrunkObjects_ObjectIdentity = ObjectIdentity
dellNetVirtualLinkTrunkObjects = _DellNetVirtualLinkTrunkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1)
)
_DellNetVirtualLinkTrunkTable_Object = MibTable
dellNetVirtualLinkTrunkTable = _DellNetVirtualLinkTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetVirtualLinkTrunkTable.setStatus("current")
_DellNetVirtualLinkTrunkTableEntry_Object = MibTableRow
dellNetVirtualLinkTrunkTableEntry = _DellNetVirtualLinkTrunkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1)
)
dellNetVirtualLinkTrunkTableEntry.setIndexNames(
    (0, "DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDomainId"),
)
if mibBuilder.loadTexts:
    dellNetVirtualLinkTrunkTableEntry.setStatus("current")
_DellNetVLTDomainId_Type = Unsigned32
_DellNetVLTDomainId_Object = MibTableColumn
dellNetVLTDomainId = _DellNetVLTDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 1),
    _DellNetVLTDomainId_Type()
)
dellNetVLTDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTDomainId.setStatus("current")
_DellNetVLTMacAddr_Type = MacAddress
_DellNetVLTMacAddr_Object = MibTableColumn
dellNetVLTMacAddr = _DellNetVLTMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 2),
    _DellNetVLTMacAddr_Type()
)
dellNetVLTMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTMacAddr.setStatus("current")


class _DellNetVLTPriority_Type(Unsigned32):
    """Custom type dellNetVLTPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DellNetVLTPriority_Type.__name__ = "Unsigned32"
_DellNetVLTPriority_Object = MibTableColumn
dellNetVLTPriority = _DellNetVLTPriority_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 3),
    _DellNetVLTPriority_Type()
)
dellNetVLTPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTPriority.setStatus("current")
_DellNetVLTIclIfIndex_Type = InterfaceIndex
_DellNetVLTIclIfIndex_Object = MibTableColumn
dellNetVLTIclIfIndex = _DellNetVLTIclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 4),
    _DellNetVLTIclIfIndex_Type()
)
dellNetVLTIclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTIclIfIndex.setStatus("current")


class _DellNetVLTRole_Type(Integer32):
    """Custom type dellNetVLTRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("standAlone", 0))
    )


_DellNetVLTRole_Type.__name__ = "Integer32"
_DellNetVLTRole_Object = MibTableColumn
dellNetVLTRole = _DellNetVLTRole_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 5),
    _DellNetVLTRole_Type()
)
dellNetVLTRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTRole.setStatus("current")


class _DellNetVLTPeerStatus_Type(Integer32):
    """Custom type dellNetVLTPeerStatus based on Integer32"""
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
        *(("linkDown", 3),
          ("notEstablished", 0),
          ("peerDown", 2),
          ("peerUp", 1))
    )


_DellNetVLTPeerStatus_Type.__name__ = "Integer32"
_DellNetVLTPeerStatus_Object = MibTableColumn
dellNetVLTPeerStatus = _DellNetVLTPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 6),
    _DellNetVLTPeerStatus_Type()
)
dellNetVLTPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTPeerStatus.setStatus("current")
_DellNetVLTIclStatus_Type = DellNetVLTMemberLinkStatus
_DellNetVLTIclStatus_Object = MibTableColumn
dellNetVLTIclStatus = _DellNetVLTIclStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 7),
    _DellNetVLTIclStatus_Type()
)
dellNetVLTIclStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTIclStatus.setStatus("current")
_DellNetVLTHBeatStatus_Type = DellNetVLTMemberLinkStatus
_DellNetVLTHBeatStatus_Object = MibTableColumn
dellNetVLTHBeatStatus = _DellNetVLTHBeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 8),
    _DellNetVLTHBeatStatus_Type()
)
dellNetVLTHBeatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTHBeatStatus.setStatus("current")
_DellNetVLTBkUpIpAddrType_Type = InetAddressType
_DellNetVLTBkUpIpAddrType_Object = MibTableColumn
dellNetVLTBkUpIpAddrType = _DellNetVLTBkUpIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 9),
    _DellNetVLTBkUpIpAddrType_Type()
)
dellNetVLTBkUpIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTBkUpIpAddrType.setStatus("current")
_DellNetVLTBkUpIpAddr_Type = InetAddress
_DellNetVLTBkUpIpAddr_Object = MibTableColumn
dellNetVLTBkUpIpAddr = _DellNetVLTBkUpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 10),
    _DellNetVLTBkUpIpAddr_Type()
)
dellNetVLTBkUpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTBkUpIpAddr.setStatus("current")


class _DellNetVLTBkUpInterval_Type(TimeInterval):
    """Custom type dellNetVLTBkUpInterval based on TimeInterval"""
    defaultValue = 100

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 500),
    )


_DellNetVLTBkUpInterval_Type.__name__ = "TimeInterval"
_DellNetVLTBkUpInterval_Object = MibTableColumn
dellNetVLTBkUpInterval = _DellNetVLTBkUpInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 11),
    _DellNetVLTBkUpInterval_Type()
)
dellNetVLTBkUpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTBkUpInterval.setStatus("current")
_DellNetVLTRemoteMacAddr_Type = MacAddress
_DellNetVLTRemoteMacAddr_Object = MibTableColumn
dellNetVLTRemoteMacAddr = _DellNetVLTRemoteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 12),
    _DellNetVLTRemoteMacAddr_Type()
)
dellNetVLTRemoteMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTRemoteMacAddr.setStatus("current")


class _DellNetVLTRemoteRolePriority_Type(Unsigned32):
    """Custom type dellNetVLTRemoteRolePriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DellNetVLTRemoteRolePriority_Type.__name__ = "Unsigned32"
_DellNetVLTRemoteRolePriority_Object = MibTableColumn
dellNetVLTRemoteRolePriority = _DellNetVLTRemoteRolePriority_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 13),
    _DellNetVLTRemoteRolePriority_Type()
)
dellNetVLTRemoteRolePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTRemoteRolePriority.setStatus("current")
_DellNetVLTUnitId_Type = Unsigned32
_DellNetVLTUnitId_Object = MibTableColumn
dellNetVLTUnitId = _DellNetVLTUnitId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 14),
    _DellNetVLTUnitId_Type()
)
dellNetVLTUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTUnitId.setStatus("current")
_DellNetVLTVersionMajor_Type = Unsigned32
_DellNetVLTVersionMajor_Object = MibTableColumn
dellNetVLTVersionMajor = _DellNetVLTVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 15),
    _DellNetVLTVersionMajor_Type()
)
dellNetVLTVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTVersionMajor.setStatus("current")
_DellNetVLTVersionMinor_Type = Unsigned32
_DellNetVLTVersionMinor_Object = MibTableColumn
dellNetVLTVersionMinor = _DellNetVLTVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 16),
    _DellNetVLTVersionMinor_Type()
)
dellNetVLTVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTVersionMinor.setStatus("current")
_DellNetVLTRemoteUnitId_Type = Unsigned32
_DellNetVLTRemoteUnitId_Object = MibTableColumn
dellNetVLTRemoteUnitId = _DellNetVLTRemoteUnitId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 17),
    _DellNetVLTRemoteUnitId_Type()
)
dellNetVLTRemoteUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTRemoteUnitId.setStatus("current")
_DellNetVLTRemoteVersionMajor_Type = Unsigned32
_DellNetVLTRemoteVersionMajor_Object = MibTableColumn
dellNetVLTRemoteVersionMajor = _DellNetVLTRemoteVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 18),
    _DellNetVLTRemoteVersionMajor_Type()
)
dellNetVLTRemoteVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTRemoteVersionMajor.setStatus("current")
_DellNetVLTRemoteVersionMinor_Type = Unsigned32
_DellNetVLTRemoteVersionMinor_Object = MibTableColumn
dellNetVLTRemoteVersionMinor = _DellNetVLTRemoteVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 19),
    _DellNetVLTRemoteVersionMinor_Type()
)
dellNetVLTRemoteVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTRemoteVersionMinor.setStatus("current")


class _DellNetVLTIclBwStatus_Type(Integer32):
    """Custom type dellNetVLTIclBwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("abovethreshold", 1),
          ("belowthreshold", 0))
    )


_DellNetVLTIclBwStatus_Type.__name__ = "Integer32"
_DellNetVLTIclBwStatus_Object = MibTableColumn
dellNetVLTIclBwStatus = _DellNetVLTIclBwStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 20),
    _DellNetVLTIclBwStatus_Type()
)
dellNetVLTIclBwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTIclBwStatus.setStatus("current")
_DellNetVLTCfgSysMacAddr_Type = MacAddress
_DellNetVLTCfgSysMacAddr_Object = MibTableColumn
dellNetVLTCfgSysMacAddr = _DellNetVLTCfgSysMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 21),
    _DellNetVLTCfgSysMacAddr_Type()
)
dellNetVLTCfgSysMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTCfgSysMacAddr.setStatus("current")


class _DellNetVLTPeerRouting_Type(Integer32):
    """Custom type dellNetVLTPeerRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DellNetVLTPeerRouting_Type.__name__ = "Integer32"
_DellNetVLTPeerRouting_Object = MibTableColumn
dellNetVLTPeerRouting = _DellNetVLTPeerRouting_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 22),
    _DellNetVLTPeerRouting_Type()
)
dellNetVLTPeerRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTPeerRouting.setStatus("current")


class _DellNetVLTPeerRoutingTimeout_Type(TimeInterval):
    """Custom type dellNetVLTPeerRoutingTimeout based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DellNetVLTPeerRoutingTimeout_Type.__name__ = "TimeInterval"
_DellNetVLTPeerRoutingTimeout_Object = MibTableColumn
dellNetVLTPeerRoutingTimeout = _DellNetVLTPeerRoutingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 23),
    _DellNetVLTPeerRoutingTimeout_Type()
)
dellNetVLTPeerRoutingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTPeerRoutingTimeout.setStatus("current")


class _DellNetVLTRemotePeerRouting_Type(Integer32):
    """Custom type dellNetVLTRemotePeerRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DellNetVLTRemotePeerRouting_Type.__name__ = "Integer32"
_DellNetVLTRemotePeerRouting_Object = MibTableColumn
dellNetVLTRemotePeerRouting = _DellNetVLTRemotePeerRouting_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 24),
    _DellNetVLTRemotePeerRouting_Type()
)
dellNetVLTRemotePeerRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTRemotePeerRouting.setStatus("current")
_DellNetVirtualLinkStatsTable_Object = MibTable
dellNetVirtualLinkStatsTable = _DellNetVirtualLinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2)
)
if mibBuilder.loadTexts:
    dellNetVirtualLinkStatsTable.setStatus("current")
_DellNetVirtualLinkStatsTableEntry_Object = MibTableRow
dellNetVirtualLinkStatsTableEntry = _DellNetVirtualLinkStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dellNetVirtualLinkStatsTableEntry.setStatus("current")
_DellNetVLTStatNumHelloSent_Type = Counter32
_DellNetVLTStatNumHelloSent_Object = MibTableColumn
dellNetVLTStatNumHelloSent = _DellNetVLTStatNumHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 1),
    _DellNetVLTStatNumHelloSent_Type()
)
dellNetVLTStatNumHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTStatNumHelloSent.setStatus("current")
_DellNetVLTStatNumHelloRcvd_Type = Counter32
_DellNetVLTStatNumHelloRcvd_Object = MibTableColumn
dellNetVLTStatNumHelloRcvd = _DellNetVLTStatNumHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 2),
    _DellNetVLTStatNumHelloRcvd_Type()
)
dellNetVLTStatNumHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTStatNumHelloRcvd.setStatus("current")
_DellNetVLTStatNumHbeatSent_Type = Counter32
_DellNetVLTStatNumHbeatSent_Object = MibTableColumn
dellNetVLTStatNumHbeatSent = _DellNetVLTStatNumHbeatSent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 3),
    _DellNetVLTStatNumHbeatSent_Type()
)
dellNetVLTStatNumHbeatSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTStatNumHbeatSent.setStatus("current")
_DellNetVLTStatNumHbeatRcvd_Type = Counter32
_DellNetVLTStatNumHbeatRcvd_Object = MibTableColumn
dellNetVLTStatNumHbeatRcvd = _DellNetVLTStatNumHbeatRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 4),
    _DellNetVLTStatNumHbeatRcvd_Type()
)
dellNetVLTStatNumHbeatRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTStatNumHbeatRcvd.setStatus("current")
_DellNetVLTStatNumDomainErrors_Type = Counter32
_DellNetVLTStatNumDomainErrors_Object = MibTableColumn
dellNetVLTStatNumDomainErrors = _DellNetVLTStatNumDomainErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 5),
    _DellNetVLTStatNumDomainErrors_Type()
)
dellNetVLTStatNumDomainErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTStatNumDomainErrors.setStatus("current")
_DellNetVLTStatNumVersionErrors_Type = Counter32
_DellNetVLTStatNumVersionErrors_Object = MibTableColumn
dellNetVLTStatNumVersionErrors = _DellNetVLTStatNumVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 6),
    _DellNetVLTStatNumVersionErrors_Type()
)
dellNetVLTStatNumVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTStatNumVersionErrors.setStatus("current")
_DellNetVirtualLinkDetailsTable_Object = MibTable
dellNetVirtualLinkDetailsTable = _DellNetVirtualLinkDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3)
)
if mibBuilder.loadTexts:
    dellNetVirtualLinkDetailsTable.setStatus("current")
_DellNetVirtualLinkDetailsTableEntry_Object = MibTableRow
dellNetVirtualLinkDetailsTableEntry = _DellNetVirtualLinkDetailsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1)
)
dellNetVirtualLinkDetailsTableEntry.setIndexNames(
    (0, "DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDetailLocalLagID"),
)
if mibBuilder.loadTexts:
    dellNetVirtualLinkDetailsTableEntry.setStatus("current")


class _DellNetVLTDetailLocalLagID_Type(Unsigned32):
    """Custom type dellNetVLTDetailLocalLagID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DellNetVLTDetailLocalLagID_Type.__name__ = "Unsigned32"
_DellNetVLTDetailLocalLagID_Object = MibTableColumn
dellNetVLTDetailLocalLagID = _DellNetVLTDetailLocalLagID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 1),
    _DellNetVLTDetailLocalLagID_Type()
)
dellNetVLTDetailLocalLagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTDetailLocalLagID.setStatus("current")


class _DellNetVLTDetailPeerLagID_Type(Unsigned32):
    """Custom type dellNetVLTDetailPeerLagID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DellNetVLTDetailPeerLagID_Type.__name__ = "Unsigned32"
_DellNetVLTDetailPeerLagID_Object = MibTableColumn
dellNetVLTDetailPeerLagID = _DellNetVLTDetailPeerLagID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 2),
    _DellNetVLTDetailPeerLagID_Type()
)
dellNetVLTDetailPeerLagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTDetailPeerLagID.setStatus("current")


class _DellNetVLTDetailLocalStatus_Type(Integer32):
    """Custom type dellNetVLTDetailLocalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_DellNetVLTDetailLocalStatus_Type.__name__ = "Integer32"
_DellNetVLTDetailLocalStatus_Object = MibTableColumn
dellNetVLTDetailLocalStatus = _DellNetVLTDetailLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 3),
    _DellNetVLTDetailLocalStatus_Type()
)
dellNetVLTDetailLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTDetailLocalStatus.setStatus("current")


class _DellNetVLTDetailPeerStatus_Type(Integer32):
    """Custom type dellNetVLTDetailPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_DellNetVLTDetailPeerStatus_Type.__name__ = "Integer32"
_DellNetVLTDetailPeerStatus_Object = MibTableColumn
dellNetVLTDetailPeerStatus = _DellNetVLTDetailPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 4),
    _DellNetVLTDetailPeerStatus_Type()
)
dellNetVLTDetailPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetVLTDetailPeerStatus.setStatus("current")


class _DellNetVLTErrorReason_Type(Integer32):
    """Custom type dellNetVLTErrorReason based on Integer32"""
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
        *(("domainIdMismatch", 2),
          ("noError", 1),
          ("peerRoutingMismatch", 6),
          ("sysMacMismatch", 5),
          ("unitIdMismatch", 3),
          ("versionMismatch", 4))
    )


_DellNetVLTErrorReason_Type.__name__ = "Integer32"
_DellNetVLTErrorReason_Object = MibScalar
dellNetVLTErrorReason = _DellNetVLTErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 4),
    _DellNetVLTErrorReason_Type()
)
dellNetVLTErrorReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetVLTErrorReason.setStatus("current")
_DellNetVirtualLinkTrunkNotifObjects_ObjectIdentity = ObjectIdentity
dellNetVirtualLinkTrunkNotifObjects = _DellNetVirtualLinkTrunkNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2)
)
_DellNetVirtualLinkTrunkNotifications_ObjectIdentity = ObjectIdentity
dellNetVirtualLinkTrunkNotifications = _DellNetVirtualLinkTrunkNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0)
)
_DellNetVirtualLinkTrunkConformance_ObjectIdentity = ObjectIdentity
dellNetVirtualLinkTrunkConformance = _DellNetVirtualLinkTrunkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3)
)
_DellNetVirtualLinkTrunkCompliances_ObjectIdentity = ObjectIdentity
dellNetVirtualLinkTrunkCompliances = _DellNetVirtualLinkTrunkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 1)
)
_DellNetVirtualLinkTrunkGroups_ObjectIdentity = ObjectIdentity
dellNetVirtualLinkTrunkGroups = _DellNetVirtualLinkTrunkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2)
)
dellNetVirtualLinkTrunkTableEntry.registerAugmentions(
    ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB",
     "dellNetVirtualLinkStatsTableEntry")
)
dellNetVirtualLinkStatsTableEntry.setIndexNames(*dellNetVirtualLinkTrunkTableEntry.getIndexNames())

# Managed Objects groups

dellNetVirtualLinkTrunkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 1)
)
dellNetVirtualLinkTrunkGroup.setObjects(
      *(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDomainId"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTMacAddr"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTPriority"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclIfIndex"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRole"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTPeerStatus"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclStatus"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTHBeatStatus"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTBkUpIpAddrType"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTBkUpIpAddr"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTBkUpInterval"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRemoteMacAddr"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRemoteRolePriority"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTUnitId"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTVersionMajor"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTVersionMinor"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRemoteUnitId"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRemoteVersionMajor"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRemoteVersionMinor"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclBwStatus"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTCfgSysMacAddr"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTPeerRouting"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTPeerRoutingTimeout"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRemotePeerRouting"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTErrorReason"))
)
if mibBuilder.loadTexts:
    dellNetVirtualLinkTrunkGroup.setStatus("current")

dellNetVirtualLinkStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 2)
)
dellNetVirtualLinkStatisticsGroup.setObjects(
      *(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTStatNumHelloSent"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTStatNumHelloRcvd"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTStatNumHbeatSent"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTStatNumHbeatRcvd"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTStatNumDomainErrors"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTStatNumVersionErrors"))
)
if mibBuilder.loadTexts:
    dellNetVirtualLinkStatisticsGroup.setStatus("current")

dellNetVirtualLinkDetailsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 4)
)
dellNetVirtualLinkDetailsTableGroup.setObjects(
      *(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDetailLocalLagID"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDetailPeerLagID"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDetailLocalStatus"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDetailPeerStatus"))
)
if mibBuilder.loadTexts:
    dellNetVirtualLinkDetailsTableGroup.setStatus("current")


# Notification objects

dellNetVLTRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 1)
)
dellNetVLTRoleChange.setObjects(
    ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRole")
)
if mibBuilder.loadTexts:
    dellNetVLTRoleChange.setStatus(
        "current"
    )

dellNetVLTIclStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 2)
)
dellNetVLTIclStatusChange.setObjects(
    ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclStatus")
)
if mibBuilder.loadTexts:
    dellNetVLTIclStatusChange.setStatus(
        "current"
    )

dellNetVLTPeerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 3)
)
dellNetVLTPeerStatusChange.setObjects(
    ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTPeerStatus")
)
if mibBuilder.loadTexts:
    dellNetVLTPeerStatusChange.setStatus(
        "current"
    )

dellNetVLTHBeatStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 4)
)
dellNetVLTHBeatStatusChange.setObjects(
    ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTHBeatStatus")
)
if mibBuilder.loadTexts:
    dellNetVLTHBeatStatusChange.setStatus(
        "current"
    )

dellNetVLTIclBwUsageExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 5)
)
dellNetVLTIclBwUsageExceed.setObjects(
      *(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclIfIndex"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclBwStatus"))
)
if mibBuilder.loadTexts:
    dellNetVLTIclBwUsageExceed.setStatus(
        "current"
    )

dellNetVLTDomainConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 6)
)
dellNetVLTDomainConfigError.setObjects(
    ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTErrorReason")
)
if mibBuilder.loadTexts:
    dellNetVLTDomainConfigError.setStatus(
        "current"
    )


# Notifications groups

dellNetVirtualLinkNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 3)
)
dellNetVirtualLinkNotificationGroup.setObjects(
      *(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRoleChange"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclStatusChange"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTPeerStatusChange"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTHBeatStatusChange"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclBwUsageExceed"),
        ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDomainConfigError"))
)
if mibBuilder.loadTexts:
    dellNetVirtualLinkNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dellNetVirtualLinkTrunkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetVirtualLinkTrunkCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB",
    **{"DellNetVLTMemberLinkStatus": DellNetVLTMemberLinkStatus,
       "dellNetVirtualLinkTrunkMib": dellNetVirtualLinkTrunkMib,
       "dellNetVirtualLinkTrunkObjects": dellNetVirtualLinkTrunkObjects,
       "dellNetVirtualLinkTrunkTable": dellNetVirtualLinkTrunkTable,
       "dellNetVirtualLinkTrunkTableEntry": dellNetVirtualLinkTrunkTableEntry,
       "dellNetVLTDomainId": dellNetVLTDomainId,
       "dellNetVLTMacAddr": dellNetVLTMacAddr,
       "dellNetVLTPriority": dellNetVLTPriority,
       "dellNetVLTIclIfIndex": dellNetVLTIclIfIndex,
       "dellNetVLTRole": dellNetVLTRole,
       "dellNetVLTPeerStatus": dellNetVLTPeerStatus,
       "dellNetVLTIclStatus": dellNetVLTIclStatus,
       "dellNetVLTHBeatStatus": dellNetVLTHBeatStatus,
       "dellNetVLTBkUpIpAddrType": dellNetVLTBkUpIpAddrType,
       "dellNetVLTBkUpIpAddr": dellNetVLTBkUpIpAddr,
       "dellNetVLTBkUpInterval": dellNetVLTBkUpInterval,
       "dellNetVLTRemoteMacAddr": dellNetVLTRemoteMacAddr,
       "dellNetVLTRemoteRolePriority": dellNetVLTRemoteRolePriority,
       "dellNetVLTUnitId": dellNetVLTUnitId,
       "dellNetVLTVersionMajor": dellNetVLTVersionMajor,
       "dellNetVLTVersionMinor": dellNetVLTVersionMinor,
       "dellNetVLTRemoteUnitId": dellNetVLTRemoteUnitId,
       "dellNetVLTRemoteVersionMajor": dellNetVLTRemoteVersionMajor,
       "dellNetVLTRemoteVersionMinor": dellNetVLTRemoteVersionMinor,
       "dellNetVLTIclBwStatus": dellNetVLTIclBwStatus,
       "dellNetVLTCfgSysMacAddr": dellNetVLTCfgSysMacAddr,
       "dellNetVLTPeerRouting": dellNetVLTPeerRouting,
       "dellNetVLTPeerRoutingTimeout": dellNetVLTPeerRoutingTimeout,
       "dellNetVLTRemotePeerRouting": dellNetVLTRemotePeerRouting,
       "dellNetVirtualLinkStatsTable": dellNetVirtualLinkStatsTable,
       "dellNetVirtualLinkStatsTableEntry": dellNetVirtualLinkStatsTableEntry,
       "dellNetVLTStatNumHelloSent": dellNetVLTStatNumHelloSent,
       "dellNetVLTStatNumHelloRcvd": dellNetVLTStatNumHelloRcvd,
       "dellNetVLTStatNumHbeatSent": dellNetVLTStatNumHbeatSent,
       "dellNetVLTStatNumHbeatRcvd": dellNetVLTStatNumHbeatRcvd,
       "dellNetVLTStatNumDomainErrors": dellNetVLTStatNumDomainErrors,
       "dellNetVLTStatNumVersionErrors": dellNetVLTStatNumVersionErrors,
       "dellNetVirtualLinkDetailsTable": dellNetVirtualLinkDetailsTable,
       "dellNetVirtualLinkDetailsTableEntry": dellNetVirtualLinkDetailsTableEntry,
       "dellNetVLTDetailLocalLagID": dellNetVLTDetailLocalLagID,
       "dellNetVLTDetailPeerLagID": dellNetVLTDetailPeerLagID,
       "dellNetVLTDetailLocalStatus": dellNetVLTDetailLocalStatus,
       "dellNetVLTDetailPeerStatus": dellNetVLTDetailPeerStatus,
       "dellNetVLTErrorReason": dellNetVLTErrorReason,
       "dellNetVirtualLinkTrunkNotifObjects": dellNetVirtualLinkTrunkNotifObjects,
       "dellNetVirtualLinkTrunkNotifications": dellNetVirtualLinkTrunkNotifications,
       "dellNetVLTRoleChange": dellNetVLTRoleChange,
       "dellNetVLTIclStatusChange": dellNetVLTIclStatusChange,
       "dellNetVLTPeerStatusChange": dellNetVLTPeerStatusChange,
       "dellNetVLTHBeatStatusChange": dellNetVLTHBeatStatusChange,
       "dellNetVLTIclBwUsageExceed": dellNetVLTIclBwUsageExceed,
       "dellNetVLTDomainConfigError": dellNetVLTDomainConfigError,
       "dellNetVirtualLinkTrunkConformance": dellNetVirtualLinkTrunkConformance,
       "dellNetVirtualLinkTrunkCompliances": dellNetVirtualLinkTrunkCompliances,
       "dellNetVirtualLinkTrunkCompliance": dellNetVirtualLinkTrunkCompliance,
       "dellNetVirtualLinkTrunkGroups": dellNetVirtualLinkTrunkGroups,
       "dellNetVirtualLinkTrunkGroup": dellNetVirtualLinkTrunkGroup,
       "dellNetVirtualLinkStatisticsGroup": dellNetVirtualLinkStatisticsGroup,
       "dellNetVirtualLinkNotificationGroup": dellNetVirtualLinkNotificationGroup,
       "dellNetVirtualLinkDetailsTableGroup": dellNetVirtualLinkDetailsTableGroup}
)
