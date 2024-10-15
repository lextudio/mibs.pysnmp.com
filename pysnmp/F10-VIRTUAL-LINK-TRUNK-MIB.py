# SNMP MIB module (F10-VIRTUAL-LINK-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F10-VIRTUAL-LINK-TRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:29 2024
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

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

f10VirtualLinkTrunkMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17)
)
f10VirtualLinkTrunkMib.setRevisions(
        ("2012-11-28 00:00",
         "2012-05-21 00:00",
         "2012-05-14 00:00",
         "2012-04-02 00:00",
         "2011-05-06 00:00",
         "2011-03-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class F10VLTMemberLinkStatus(Integer32, TextualConvention):
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

_F10VirtualLinkTrunkObjects_ObjectIdentity = ObjectIdentity
f10VirtualLinkTrunkObjects = _F10VirtualLinkTrunkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1)
)
_F10VirtualLinkTrunkTable_Object = MibTable
f10VirtualLinkTrunkTable = _F10VirtualLinkTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1)
)
if mibBuilder.loadTexts:
    f10VirtualLinkTrunkTable.setStatus("current")
_F10VirtualLinkTrunkTableEntry_Object = MibTableRow
f10VirtualLinkTrunkTableEntry = _F10VirtualLinkTrunkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1)
)
f10VirtualLinkTrunkTableEntry.setIndexNames(
    (0, "F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDomainId"),
)
if mibBuilder.loadTexts:
    f10VirtualLinkTrunkTableEntry.setStatus("current")
_F10VLTDomainId_Type = Unsigned32
_F10VLTDomainId_Object = MibTableColumn
f10VLTDomainId = _F10VLTDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 1),
    _F10VLTDomainId_Type()
)
f10VLTDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTDomainId.setStatus("current")
_F10VLTMacAddr_Type = MacAddress
_F10VLTMacAddr_Object = MibTableColumn
f10VLTMacAddr = _F10VLTMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 2),
    _F10VLTMacAddr_Type()
)
f10VLTMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTMacAddr.setStatus("current")


class _F10VLTPriority_Type(Unsigned32):
    """Custom type f10VLTPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F10VLTPriority_Type.__name__ = "Unsigned32"
_F10VLTPriority_Object = MibTableColumn
f10VLTPriority = _F10VLTPriority_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 3),
    _F10VLTPriority_Type()
)
f10VLTPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTPriority.setStatus("current")
_F10VLTIclIfIndex_Type = InterfaceIndex
_F10VLTIclIfIndex_Object = MibTableColumn
f10VLTIclIfIndex = _F10VLTIclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 4),
    _F10VLTIclIfIndex_Type()
)
f10VLTIclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTIclIfIndex.setStatus("current")


class _F10VLTRole_Type(Integer32):
    """Custom type f10VLTRole based on Integer32"""
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


_F10VLTRole_Type.__name__ = "Integer32"
_F10VLTRole_Object = MibTableColumn
f10VLTRole = _F10VLTRole_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 5),
    _F10VLTRole_Type()
)
f10VLTRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTRole.setStatus("current")


class _F10VLTPeerStatus_Type(Integer32):
    """Custom type f10VLTPeerStatus based on Integer32"""
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


_F10VLTPeerStatus_Type.__name__ = "Integer32"
_F10VLTPeerStatus_Object = MibTableColumn
f10VLTPeerStatus = _F10VLTPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 6),
    _F10VLTPeerStatus_Type()
)
f10VLTPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTPeerStatus.setStatus("current")
_F10VLTIclStatus_Type = F10VLTMemberLinkStatus
_F10VLTIclStatus_Object = MibTableColumn
f10VLTIclStatus = _F10VLTIclStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 7),
    _F10VLTIclStatus_Type()
)
f10VLTIclStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTIclStatus.setStatus("current")
_F10VLTHBeatStatus_Type = F10VLTMemberLinkStatus
_F10VLTHBeatStatus_Object = MibTableColumn
f10VLTHBeatStatus = _F10VLTHBeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 8),
    _F10VLTHBeatStatus_Type()
)
f10VLTHBeatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTHBeatStatus.setStatus("current")
_F10VLTBkUpIpAddrType_Type = InetAddressType
_F10VLTBkUpIpAddrType_Object = MibTableColumn
f10VLTBkUpIpAddrType = _F10VLTBkUpIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 9),
    _F10VLTBkUpIpAddrType_Type()
)
f10VLTBkUpIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTBkUpIpAddrType.setStatus("current")
_F10VLTBkUpIpAddr_Type = InetAddress
_F10VLTBkUpIpAddr_Object = MibTableColumn
f10VLTBkUpIpAddr = _F10VLTBkUpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 10),
    _F10VLTBkUpIpAddr_Type()
)
f10VLTBkUpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTBkUpIpAddr.setStatus("current")


class _F10VLTBkUpInterval_Type(TimeInterval):
    """Custom type f10VLTBkUpInterval based on TimeInterval"""
    defaultValue = 100

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 500),
    )


_F10VLTBkUpInterval_Type.__name__ = "TimeInterval"
_F10VLTBkUpInterval_Object = MibTableColumn
f10VLTBkUpInterval = _F10VLTBkUpInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 11),
    _F10VLTBkUpInterval_Type()
)
f10VLTBkUpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTBkUpInterval.setStatus("current")
_F10VLTRemoteMacAddr_Type = MacAddress
_F10VLTRemoteMacAddr_Object = MibTableColumn
f10VLTRemoteMacAddr = _F10VLTRemoteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 12),
    _F10VLTRemoteMacAddr_Type()
)
f10VLTRemoteMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTRemoteMacAddr.setStatus("current")


class _F10VLTRemoteRolePriority_Type(Unsigned32):
    """Custom type f10VLTRemoteRolePriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F10VLTRemoteRolePriority_Type.__name__ = "Unsigned32"
_F10VLTRemoteRolePriority_Object = MibTableColumn
f10VLTRemoteRolePriority = _F10VLTRemoteRolePriority_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 13),
    _F10VLTRemoteRolePriority_Type()
)
f10VLTRemoteRolePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTRemoteRolePriority.setStatus("current")
_F10VLTUnitId_Type = Unsigned32
_F10VLTUnitId_Object = MibTableColumn
f10VLTUnitId = _F10VLTUnitId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 14),
    _F10VLTUnitId_Type()
)
f10VLTUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTUnitId.setStatus("current")
_F10VLTVersionMajor_Type = Unsigned32
_F10VLTVersionMajor_Object = MibTableColumn
f10VLTVersionMajor = _F10VLTVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 15),
    _F10VLTVersionMajor_Type()
)
f10VLTVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTVersionMajor.setStatus("current")
_F10VLTVersionMinor_Type = Unsigned32
_F10VLTVersionMinor_Object = MibTableColumn
f10VLTVersionMinor = _F10VLTVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 16),
    _F10VLTVersionMinor_Type()
)
f10VLTVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTVersionMinor.setStatus("current")
_F10VLTRemoteUnitId_Type = Unsigned32
_F10VLTRemoteUnitId_Object = MibTableColumn
f10VLTRemoteUnitId = _F10VLTRemoteUnitId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 17),
    _F10VLTRemoteUnitId_Type()
)
f10VLTRemoteUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTRemoteUnitId.setStatus("current")
_F10VLTRemoteVersionMajor_Type = Unsigned32
_F10VLTRemoteVersionMajor_Object = MibTableColumn
f10VLTRemoteVersionMajor = _F10VLTRemoteVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 18),
    _F10VLTRemoteVersionMajor_Type()
)
f10VLTRemoteVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTRemoteVersionMajor.setStatus("current")
_F10VLTRemoteVersionMinor_Type = Unsigned32
_F10VLTRemoteVersionMinor_Object = MibTableColumn
f10VLTRemoteVersionMinor = _F10VLTRemoteVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 19),
    _F10VLTRemoteVersionMinor_Type()
)
f10VLTRemoteVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTRemoteVersionMinor.setStatus("current")


class _F10VLTIclBwStatus_Type(Integer32):
    """Custom type f10VLTIclBwStatus based on Integer32"""
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


_F10VLTIclBwStatus_Type.__name__ = "Integer32"
_F10VLTIclBwStatus_Object = MibTableColumn
f10VLTIclBwStatus = _F10VLTIclBwStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 20),
    _F10VLTIclBwStatus_Type()
)
f10VLTIclBwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTIclBwStatus.setStatus("current")
_F10VLTCfgSysMacAddr_Type = MacAddress
_F10VLTCfgSysMacAddr_Object = MibTableColumn
f10VLTCfgSysMacAddr = _F10VLTCfgSysMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 21),
    _F10VLTCfgSysMacAddr_Type()
)
f10VLTCfgSysMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTCfgSysMacAddr.setStatus("current")


class _F10VLTPeerRouting_Type(Integer32):
    """Custom type f10VLTPeerRouting based on Integer32"""
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


_F10VLTPeerRouting_Type.__name__ = "Integer32"
_F10VLTPeerRouting_Object = MibTableColumn
f10VLTPeerRouting = _F10VLTPeerRouting_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 22),
    _F10VLTPeerRouting_Type()
)
f10VLTPeerRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTPeerRouting.setStatus("current")


class _F10VLTPeerRoutingTimeout_Type(TimeInterval):
    """Custom type f10VLTPeerRoutingTimeout based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_F10VLTPeerRoutingTimeout_Type.__name__ = "TimeInterval"
_F10VLTPeerRoutingTimeout_Object = MibTableColumn
f10VLTPeerRoutingTimeout = _F10VLTPeerRoutingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 23),
    _F10VLTPeerRoutingTimeout_Type()
)
f10VLTPeerRoutingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTPeerRoutingTimeout.setStatus("current")


class _F10VLTRemotePeerRouting_Type(Integer32):
    """Custom type f10VLTRemotePeerRouting based on Integer32"""
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


_F10VLTRemotePeerRouting_Type.__name__ = "Integer32"
_F10VLTRemotePeerRouting_Object = MibTableColumn
f10VLTRemotePeerRouting = _F10VLTRemotePeerRouting_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 24),
    _F10VLTRemotePeerRouting_Type()
)
f10VLTRemotePeerRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTRemotePeerRouting.setStatus("current")
_F10VirtualLinkStatsTable_Object = MibTable
f10VirtualLinkStatsTable = _F10VirtualLinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2)
)
if mibBuilder.loadTexts:
    f10VirtualLinkStatsTable.setStatus("current")
_F10VirtualLinkStatsTableEntry_Object = MibTableRow
f10VirtualLinkStatsTableEntry = _F10VirtualLinkStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    f10VirtualLinkStatsTableEntry.setStatus("current")
_F10VLTStatNumHelloSent_Type = Counter32
_F10VLTStatNumHelloSent_Object = MibTableColumn
f10VLTStatNumHelloSent = _F10VLTStatNumHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 1),
    _F10VLTStatNumHelloSent_Type()
)
f10VLTStatNumHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTStatNumHelloSent.setStatus("current")
_F10VLTStatNumHelloRcvd_Type = Counter32
_F10VLTStatNumHelloRcvd_Object = MibTableColumn
f10VLTStatNumHelloRcvd = _F10VLTStatNumHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 2),
    _F10VLTStatNumHelloRcvd_Type()
)
f10VLTStatNumHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTStatNumHelloRcvd.setStatus("current")
_F10VLTStatNumHbeatSent_Type = Counter32
_F10VLTStatNumHbeatSent_Object = MibTableColumn
f10VLTStatNumHbeatSent = _F10VLTStatNumHbeatSent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 3),
    _F10VLTStatNumHbeatSent_Type()
)
f10VLTStatNumHbeatSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTStatNumHbeatSent.setStatus("current")
_F10VLTStatNumHbeatRcvd_Type = Counter32
_F10VLTStatNumHbeatRcvd_Object = MibTableColumn
f10VLTStatNumHbeatRcvd = _F10VLTStatNumHbeatRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 4),
    _F10VLTStatNumHbeatRcvd_Type()
)
f10VLTStatNumHbeatRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTStatNumHbeatRcvd.setStatus("current")
_F10VLTStatNumDomainErrors_Type = Counter32
_F10VLTStatNumDomainErrors_Object = MibTableColumn
f10VLTStatNumDomainErrors = _F10VLTStatNumDomainErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 5),
    _F10VLTStatNumDomainErrors_Type()
)
f10VLTStatNumDomainErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTStatNumDomainErrors.setStatus("current")
_F10VLTStatNumVersionErrors_Type = Counter32
_F10VLTStatNumVersionErrors_Object = MibTableColumn
f10VLTStatNumVersionErrors = _F10VLTStatNumVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 6),
    _F10VLTStatNumVersionErrors_Type()
)
f10VLTStatNumVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTStatNumVersionErrors.setStatus("current")
_F10VirtualLinkDetailsTable_Object = MibTable
f10VirtualLinkDetailsTable = _F10VirtualLinkDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3)
)
if mibBuilder.loadTexts:
    f10VirtualLinkDetailsTable.setStatus("current")
_F10VirtualLinkDetailsTableEntry_Object = MibTableRow
f10VirtualLinkDetailsTableEntry = _F10VirtualLinkDetailsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1)
)
f10VirtualLinkDetailsTableEntry.setIndexNames(
    (0, "F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailLocalLagID"),
)
if mibBuilder.loadTexts:
    f10VirtualLinkDetailsTableEntry.setStatus("current")


class _F10VLTDetailLocalLagID_Type(Unsigned32):
    """Custom type f10VLTDetailLocalLagID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F10VLTDetailLocalLagID_Type.__name__ = "Unsigned32"
_F10VLTDetailLocalLagID_Object = MibTableColumn
f10VLTDetailLocalLagID = _F10VLTDetailLocalLagID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 1),
    _F10VLTDetailLocalLagID_Type()
)
f10VLTDetailLocalLagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTDetailLocalLagID.setStatus("current")


class _F10VLTDetailPeerLagID_Type(Unsigned32):
    """Custom type f10VLTDetailPeerLagID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F10VLTDetailPeerLagID_Type.__name__ = "Unsigned32"
_F10VLTDetailPeerLagID_Object = MibTableColumn
f10VLTDetailPeerLagID = _F10VLTDetailPeerLagID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 2),
    _F10VLTDetailPeerLagID_Type()
)
f10VLTDetailPeerLagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTDetailPeerLagID.setStatus("current")


class _F10VLTDetailLocalStatus_Type(Integer32):
    """Custom type f10VLTDetailLocalStatus based on Integer32"""
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


_F10VLTDetailLocalStatus_Type.__name__ = "Integer32"
_F10VLTDetailLocalStatus_Object = MibTableColumn
f10VLTDetailLocalStatus = _F10VLTDetailLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 3),
    _F10VLTDetailLocalStatus_Type()
)
f10VLTDetailLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTDetailLocalStatus.setStatus("current")


class _F10VLTDetailPeerStatus_Type(Integer32):
    """Custom type f10VLTDetailPeerStatus based on Integer32"""
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


_F10VLTDetailPeerStatus_Type.__name__ = "Integer32"
_F10VLTDetailPeerStatus_Object = MibTableColumn
f10VLTDetailPeerStatus = _F10VLTDetailPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 4),
    _F10VLTDetailPeerStatus_Type()
)
f10VLTDetailPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10VLTDetailPeerStatus.setStatus("current")


class _F10VLTErrorReason_Type(Integer32):
    """Custom type f10VLTErrorReason based on Integer32"""
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


_F10VLTErrorReason_Type.__name__ = "Integer32"
_F10VLTErrorReason_Object = MibScalar
f10VLTErrorReason = _F10VLTErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 4),
    _F10VLTErrorReason_Type()
)
f10VLTErrorReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    f10VLTErrorReason.setStatus("current")
_F10VirtualLinkTrunkNotifObjects_ObjectIdentity = ObjectIdentity
f10VirtualLinkTrunkNotifObjects = _F10VirtualLinkTrunkNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2)
)
_F10VirtualLinkTrunkNotifications_ObjectIdentity = ObjectIdentity
f10VirtualLinkTrunkNotifications = _F10VirtualLinkTrunkNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0)
)
_F10VirtualLinkTrunkConformance_ObjectIdentity = ObjectIdentity
f10VirtualLinkTrunkConformance = _F10VirtualLinkTrunkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3)
)
_F10VirtualLinkTrunkCompliances_ObjectIdentity = ObjectIdentity
f10VirtualLinkTrunkCompliances = _F10VirtualLinkTrunkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 1)
)
_F10VirtualLinkTrunkGroups_ObjectIdentity = ObjectIdentity
f10VirtualLinkTrunkGroups = _F10VirtualLinkTrunkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2)
)
f10VirtualLinkTrunkTableEntry.registerAugmentions(
    ("F10-VIRTUAL-LINK-TRUNK-MIB",
     "f10VirtualLinkStatsTableEntry")
)
f10VirtualLinkStatsTableEntry.setIndexNames(*f10VirtualLinkTrunkTableEntry.getIndexNames())

# Managed Objects groups

f10VirtualLinkTrunkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 1)
)
f10VirtualLinkTrunkGroup.setObjects(
      *(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDomainId"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTMacAddr"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPriority"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclIfIndex"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRole"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerStatus"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclStatus"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTHBeatStatus"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTBkUpIpAddrType"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTBkUpIpAddr"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTBkUpInterval"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteMacAddr"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteRolePriority"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTUnitId"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTVersionMajor"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTVersionMinor"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteUnitId"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteVersionMajor"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteVersionMinor"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclBwStatus"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTCfgSysMacAddr"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerRouting"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerRoutingTimeout"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemotePeerRouting"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTErrorReason"))
)
if mibBuilder.loadTexts:
    f10VirtualLinkTrunkGroup.setStatus("current")

f10VirtualLinkStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 2)
)
f10VirtualLinkStatisticsGroup.setObjects(
      *(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumHelloSent"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumHelloRcvd"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumHbeatSent"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumHbeatRcvd"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumDomainErrors"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumVersionErrors"))
)
if mibBuilder.loadTexts:
    f10VirtualLinkStatisticsGroup.setStatus("current")

f10VirtualLinkDetailsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 4)
)
f10VirtualLinkDetailsTableGroup.setObjects(
      *(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailLocalLagID"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailPeerLagID"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailLocalStatus"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailPeerStatus"))
)
if mibBuilder.loadTexts:
    f10VirtualLinkDetailsTableGroup.setStatus("current")


# Notification objects

f10VLTRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 1)
)
f10VLTRoleChange.setObjects(
    ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRole")
)
if mibBuilder.loadTexts:
    f10VLTRoleChange.setStatus(
        "current"
    )

f10VLTIclStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 2)
)
f10VLTIclStatusChange.setObjects(
    ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclStatus")
)
if mibBuilder.loadTexts:
    f10VLTIclStatusChange.setStatus(
        "current"
    )

f10VLTPeerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 3)
)
f10VLTPeerStatusChange.setObjects(
    ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerStatus")
)
if mibBuilder.loadTexts:
    f10VLTPeerStatusChange.setStatus(
        "current"
    )

f10VLTHBeatStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 4)
)
f10VLTHBeatStatusChange.setObjects(
    ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTHBeatStatus")
)
if mibBuilder.loadTexts:
    f10VLTHBeatStatusChange.setStatus(
        "current"
    )

f10VLTIclBwUsageExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 5)
)
f10VLTIclBwUsageExceed.setObjects(
      *(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclIfIndex"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclBwStatus"))
)
if mibBuilder.loadTexts:
    f10VLTIclBwUsageExceed.setStatus(
        "current"
    )

f10VLTDomainConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 6)
)
f10VLTDomainConfigError.setObjects(
    ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTErrorReason")
)
if mibBuilder.loadTexts:
    f10VLTDomainConfigError.setStatus(
        "current"
    )


# Notifications groups

f10VirtualLinkNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 3)
)
f10VirtualLinkNotificationGroup.setObjects(
      *(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRoleChange"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclStatusChange"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerStatusChange"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTHBeatStatusChange"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclBwUsageExceed"),
        ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDomainConfigError"))
)
if mibBuilder.loadTexts:
    f10VirtualLinkNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

f10VirtualLinkTrunkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 1, 1)
)
if mibBuilder.loadTexts:
    f10VirtualLinkTrunkCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-VIRTUAL-LINK-TRUNK-MIB",
    **{"F10VLTMemberLinkStatus": F10VLTMemberLinkStatus,
       "f10VirtualLinkTrunkMib": f10VirtualLinkTrunkMib,
       "f10VirtualLinkTrunkObjects": f10VirtualLinkTrunkObjects,
       "f10VirtualLinkTrunkTable": f10VirtualLinkTrunkTable,
       "f10VirtualLinkTrunkTableEntry": f10VirtualLinkTrunkTableEntry,
       "f10VLTDomainId": f10VLTDomainId,
       "f10VLTMacAddr": f10VLTMacAddr,
       "f10VLTPriority": f10VLTPriority,
       "f10VLTIclIfIndex": f10VLTIclIfIndex,
       "f10VLTRole": f10VLTRole,
       "f10VLTPeerStatus": f10VLTPeerStatus,
       "f10VLTIclStatus": f10VLTIclStatus,
       "f10VLTHBeatStatus": f10VLTHBeatStatus,
       "f10VLTBkUpIpAddrType": f10VLTBkUpIpAddrType,
       "f10VLTBkUpIpAddr": f10VLTBkUpIpAddr,
       "f10VLTBkUpInterval": f10VLTBkUpInterval,
       "f10VLTRemoteMacAddr": f10VLTRemoteMacAddr,
       "f10VLTRemoteRolePriority": f10VLTRemoteRolePriority,
       "f10VLTUnitId": f10VLTUnitId,
       "f10VLTVersionMajor": f10VLTVersionMajor,
       "f10VLTVersionMinor": f10VLTVersionMinor,
       "f10VLTRemoteUnitId": f10VLTRemoteUnitId,
       "f10VLTRemoteVersionMajor": f10VLTRemoteVersionMajor,
       "f10VLTRemoteVersionMinor": f10VLTRemoteVersionMinor,
       "f10VLTIclBwStatus": f10VLTIclBwStatus,
       "f10VLTCfgSysMacAddr": f10VLTCfgSysMacAddr,
       "f10VLTPeerRouting": f10VLTPeerRouting,
       "f10VLTPeerRoutingTimeout": f10VLTPeerRoutingTimeout,
       "f10VLTRemotePeerRouting": f10VLTRemotePeerRouting,
       "f10VirtualLinkStatsTable": f10VirtualLinkStatsTable,
       "f10VirtualLinkStatsTableEntry": f10VirtualLinkStatsTableEntry,
       "f10VLTStatNumHelloSent": f10VLTStatNumHelloSent,
       "f10VLTStatNumHelloRcvd": f10VLTStatNumHelloRcvd,
       "f10VLTStatNumHbeatSent": f10VLTStatNumHbeatSent,
       "f10VLTStatNumHbeatRcvd": f10VLTStatNumHbeatRcvd,
       "f10VLTStatNumDomainErrors": f10VLTStatNumDomainErrors,
       "f10VLTStatNumVersionErrors": f10VLTStatNumVersionErrors,
       "f10VirtualLinkDetailsTable": f10VirtualLinkDetailsTable,
       "f10VirtualLinkDetailsTableEntry": f10VirtualLinkDetailsTableEntry,
       "f10VLTDetailLocalLagID": f10VLTDetailLocalLagID,
       "f10VLTDetailPeerLagID": f10VLTDetailPeerLagID,
       "f10VLTDetailLocalStatus": f10VLTDetailLocalStatus,
       "f10VLTDetailPeerStatus": f10VLTDetailPeerStatus,
       "f10VLTErrorReason": f10VLTErrorReason,
       "f10VirtualLinkTrunkNotifObjects": f10VirtualLinkTrunkNotifObjects,
       "f10VirtualLinkTrunkNotifications": f10VirtualLinkTrunkNotifications,
       "f10VLTRoleChange": f10VLTRoleChange,
       "f10VLTIclStatusChange": f10VLTIclStatusChange,
       "f10VLTPeerStatusChange": f10VLTPeerStatusChange,
       "f10VLTHBeatStatusChange": f10VLTHBeatStatusChange,
       "f10VLTIclBwUsageExceed": f10VLTIclBwUsageExceed,
       "f10VLTDomainConfigError": f10VLTDomainConfigError,
       "f10VirtualLinkTrunkConformance": f10VirtualLinkTrunkConformance,
       "f10VirtualLinkTrunkCompliances": f10VirtualLinkTrunkCompliances,
       "f10VirtualLinkTrunkCompliance": f10VirtualLinkTrunkCompliance,
       "f10VirtualLinkTrunkGroups": f10VirtualLinkTrunkGroups,
       "f10VirtualLinkTrunkGroup": f10VirtualLinkTrunkGroup,
       "f10VirtualLinkStatisticsGroup": f10VirtualLinkStatisticsGroup,
       "f10VirtualLinkNotificationGroup": f10VirtualLinkNotificationGroup,
       "f10VirtualLinkDetailsTableGroup": f10VirtualLinkDetailsTableGroup}
)
