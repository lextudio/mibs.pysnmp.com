# SNMP MIB module (ZHONE-COM-IP-ZEDGE-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-ZEDGE-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:21 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(zhoneIp,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

comIpZEdgeNat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 66)
)
comIpZEdgeNat.setRevisions(
        ("2010-10-20 05:52",
         "2008-07-22 07:28",
         "2003-12-11 02:58",
         "2003-03-19 09:02",
         "2000-10-04 15:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZedgeNat_ObjectIdentity = ObjectIdentity
zedgeNat = _ZedgeNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16)
)
if mibBuilder.loadTexts:
    zedgeNat.setStatus("current")
_NatConfigGroup_ObjectIdentity = ObjectIdentity
natConfigGroup = _NatConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 1)
)
if mibBuilder.loadTexts:
    natConfigGroup.setStatus("current")


class _NatTcpTimeout_Type(Unsigned32):
    """Custom type natTcpTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_NatTcpTimeout_Type.__name__ = "Unsigned32"
_NatTcpTimeout_Object = MibScalar
natTcpTimeout = _NatTcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 1, 1),
    _NatTcpTimeout_Type()
)
natTcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natTcpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    natTcpTimeout.setUnits("seconds")


class _NatUdpTimeout_Type(Unsigned32):
    """Custom type natUdpTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_NatUdpTimeout_Type.__name__ = "Unsigned32"
_NatUdpTimeout_Object = MibScalar
natUdpTimeout = _NatUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 1, 2),
    _NatUdpTimeout_Type()
)
natUdpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natUdpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    natUdpTimeout.setUnits("seconds")
_NatClearBindings_Type = TruthValue
_NatClearBindings_Object = MibScalar
natClearBindings = _NatClearBindings_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 1, 3),
    _NatClearBindings_Type()
)
natClearBindings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natClearBindings.setStatus("current")
_NatStatsGroup_ObjectIdentity = ObjectIdentity
natStatsGroup = _NatStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 2)
)
if mibBuilder.loadTexts:
    natStatsGroup.setStatus("current")
_NatNumCurrentBindings_Type = Gauge32
_NatNumCurrentBindings_Object = MibScalar
natNumCurrentBindings = _NatNumCurrentBindings_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 2, 1),
    _NatNumCurrentBindings_Type()
)
natNumCurrentBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natNumCurrentBindings.setStatus("current")
_NatNumExpiredBindings_Type = Gauge32
_NatNumExpiredBindings_Object = MibScalar
natNumExpiredBindings = _NatNumExpiredBindings_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 2, 2),
    _NatNumExpiredBindings_Type()
)
natNumExpiredBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natNumExpiredBindings.setStatus("current")
_NatTotalPkts_Type = Counter32
_NatTotalPkts_Object = MibScalar
natTotalPkts = _NatTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 2, 3),
    _NatTotalPkts_Type()
)
natTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natTotalPkts.setStatus("current")
_NatDroppedPkts_Type = Counter32
_NatDroppedPkts_Object = MibScalar
natDroppedPkts = _NatDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 2, 4),
    _NatDroppedPkts_Type()
)
natDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natDroppedPkts.setStatus("current")
_NatBindingsTable_Object = MibTable
natBindingsTable = _NatBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 3)
)
if mibBuilder.loadTexts:
    natBindingsTable.setStatus("current")
_NatBindingsEntry_Object = MibTableRow
natBindingsEntry = _NatBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 3, 1)
)
natBindingsEntry.setIndexNames(
    (0, "ZHONE-COM-IP-ZEDGE-NAT-MIB", "natBindingsIfIndex"),
    (0, "ZHONE-COM-IP-ZEDGE-NAT-MIB", "natBindingLocalAddr"),
    (0, "ZHONE-COM-IP-ZEDGE-NAT-MIB", "natBindingLocalPort"),
    (0, "ZHONE-COM-IP-ZEDGE-NAT-MIB", "natBindingPublicAddr"),
    (0, "ZHONE-COM-IP-ZEDGE-NAT-MIB", "natBindingPublicPort"),
)
if mibBuilder.loadTexts:
    natBindingsEntry.setStatus("current")
_NatBindingsIfIndex_Type = InterfaceIndex
_NatBindingsIfIndex_Object = MibTableColumn
natBindingsIfIndex = _NatBindingsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 3, 1, 1),
    _NatBindingsIfIndex_Type()
)
natBindingsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natBindingsIfIndex.setStatus("current")
_NatBindingLocalAddr_Type = IpAddress
_NatBindingLocalAddr_Object = MibTableColumn
natBindingLocalAddr = _NatBindingLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 3, 1, 2),
    _NatBindingLocalAddr_Type()
)
natBindingLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natBindingLocalAddr.setStatus("current")
_NatBindingLocalPort_Type = Unsigned32
_NatBindingLocalPort_Object = MibTableColumn
natBindingLocalPort = _NatBindingLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 3, 1, 3),
    _NatBindingLocalPort_Type()
)
natBindingLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natBindingLocalPort.setStatus("current")
_NatBindingPublicAddr_Type = IpAddress
_NatBindingPublicAddr_Object = MibTableColumn
natBindingPublicAddr = _NatBindingPublicAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 3, 1, 4),
    _NatBindingPublicAddr_Type()
)
natBindingPublicAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natBindingPublicAddr.setStatus("current")
_NatBindingPublicPort_Type = Unsigned32
_NatBindingPublicPort_Object = MibTableColumn
natBindingPublicPort = _NatBindingPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 3, 1, 5),
    _NatBindingPublicPort_Type()
)
natBindingPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natBindingPublicPort.setStatus("current")
_ZhonePATBindings_ObjectIdentity = ObjectIdentity
zhonePATBindings = _ZhonePATBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 4)
)
_PatBindNextIndex_Type = Integer32
_PatBindNextIndex_Object = MibScalar
patBindNextIndex = _PatBindNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 4, 1),
    _PatBindNextIndex_Type()
)
patBindNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    patBindNextIndex.setStatus("current")
_PatTable_Object = MibTable
patTable = _PatTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 4, 2)
)
if mibBuilder.loadTexts:
    patTable.setStatus("current")
_PatEntry_Object = MibTableRow
patEntry = _PatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 4, 2, 1)
)
patEntry.setIndexNames(
    (0, "ZHONE-COM-IP-ZEDGE-NAT-MIB", "zhonePATBindIndex"),
)
if mibBuilder.loadTexts:
    patEntry.setStatus("current")


class _ZhonePATBindIndex_Type(Integer32):
    """Custom type zhonePATBindIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4320),
    )


_ZhonePATBindIndex_Type.__name__ = "Integer32"
_ZhonePATBindIndex_Object = MibTableColumn
zhonePATBindIndex = _ZhonePATBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 4, 2, 1, 1),
    _ZhonePATBindIndex_Type()
)
zhonePATBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhonePATBindIndex.setStatus("current")
_ZhonePATBindRowStatus_Type = ZhoneRowStatus
_ZhonePATBindRowStatus_Object = MibTableColumn
zhonePATBindRowStatus = _ZhonePATBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 4, 2, 1, 2),
    _ZhonePATBindRowStatus_Type()
)
zhonePATBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePATBindRowStatus.setStatus("current")
_PublicAddr_Type = IpAddress
_PublicAddr_Object = MibTableColumn
publicAddr = _PublicAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 4, 2, 1, 3),
    _PublicAddr_Type()
)
publicAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    publicAddr.setStatus("current")


class _PublicPort_Type(Integer32):
    """Custom type publicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(51921, 56250),
    )


_PublicPort_Type.__name__ = "Integer32"
_PublicPort_Object = MibTableColumn
publicPort = _PublicPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 4, 2, 1, 4),
    _PublicPort_Type()
)
publicPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    publicPort.setStatus("current")
_LocalAddr_Type = IpAddress
_LocalAddr_Object = MibTableColumn
localAddr = _LocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 4, 2, 1, 5),
    _LocalAddr_Type()
)
localAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    localAddr.setStatus("current")


class _LocalPort_Type(Integer32):
    """Custom type localPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 49151),
    )


_LocalPort_Type.__name__ = "Integer32"
_LocalPort_Object = MibTableColumn
localPort = _LocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 4, 2, 1, 6),
    _LocalPort_Type()
)
localPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    localPort.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
    defaultValue = 1

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
        *(("cpemgr", 3),
          ("cpemgrsecure", 4),
          ("tcp", 1),
          ("udp", 2))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 4, 2, 1, 7),
    _PortType_Type()
)
portType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portType.setStatus("current")
_ZhoneNATExclusion_ObjectIdentity = ObjectIdentity
zhoneNATExclusion = _ZhoneNATExclusion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 5)
)
_NatExcludeNextIndex_Type = Integer32
_NatExcludeNextIndex_Object = MibScalar
natExcludeNextIndex = _NatExcludeNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 5, 1),
    _NatExcludeNextIndex_Type()
)
natExcludeNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natExcludeNextIndex.setStatus("current")
_NatExcludeTable_Object = MibTable
natExcludeTable = _NatExcludeTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 5, 2)
)
if mibBuilder.loadTexts:
    natExcludeTable.setStatus("current")
_NatExcludeEntry_Object = MibTableRow
natExcludeEntry = _NatExcludeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 5, 2, 1)
)
natExcludeEntry.setIndexNames(
    (0, "ZHONE-COM-IP-ZEDGE-NAT-MIB", "zhoneNATExcludeIndex"),
)
if mibBuilder.loadTexts:
    natExcludeEntry.setStatus("current")


class _ZhoneNATExcludeIndex_Type(Integer32):
    """Custom type zhoneNATExcludeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ZhoneNATExcludeIndex_Type.__name__ = "Integer32"
_ZhoneNATExcludeIndex_Object = MibTableColumn
zhoneNATExcludeIndex = _ZhoneNATExcludeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 5, 2, 1, 1),
    _ZhoneNATExcludeIndex_Type()
)
zhoneNATExcludeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneNATExcludeIndex.setStatus("current")
_ZhoneNATExcludeRowStatus_Type = ZhoneRowStatus
_ZhoneNATExcludeRowStatus_Object = MibTableColumn
zhoneNATExcludeRowStatus = _ZhoneNATExcludeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 5, 2, 1, 2),
    _ZhoneNATExcludeRowStatus_Type()
)
zhoneNATExcludeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneNATExcludeRowStatus.setStatus("current")
_IpStartAddr_Type = IpAddress
_IpStartAddr_Object = MibTableColumn
ipStartAddr = _IpStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 5, 2, 1, 3),
    _IpStartAddr_Type()
)
ipStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipStartAddr.setStatus("current")
_IpEndAddr_Type = IpAddress
_IpEndAddr_Object = MibTableColumn
ipEndAddr = _IpEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 16, 5, 2, 1, 4),
    _IpEndAddr_Type()
)
ipEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipEndAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-ZEDGE-NAT-MIB",
    **{"zedgeNat": zedgeNat,
       "natConfigGroup": natConfigGroup,
       "natTcpTimeout": natTcpTimeout,
       "natUdpTimeout": natUdpTimeout,
       "natClearBindings": natClearBindings,
       "natStatsGroup": natStatsGroup,
       "natNumCurrentBindings": natNumCurrentBindings,
       "natNumExpiredBindings": natNumExpiredBindings,
       "natTotalPkts": natTotalPkts,
       "natDroppedPkts": natDroppedPkts,
       "natBindingsTable": natBindingsTable,
       "natBindingsEntry": natBindingsEntry,
       "natBindingsIfIndex": natBindingsIfIndex,
       "natBindingLocalAddr": natBindingLocalAddr,
       "natBindingLocalPort": natBindingLocalPort,
       "natBindingPublicAddr": natBindingPublicAddr,
       "natBindingPublicPort": natBindingPublicPort,
       "zhonePATBindings": zhonePATBindings,
       "patBindNextIndex": patBindNextIndex,
       "patTable": patTable,
       "patEntry": patEntry,
       "zhonePATBindIndex": zhonePATBindIndex,
       "zhonePATBindRowStatus": zhonePATBindRowStatus,
       "publicAddr": publicAddr,
       "publicPort": publicPort,
       "localAddr": localAddr,
       "localPort": localPort,
       "portType": portType,
       "zhoneNATExclusion": zhoneNATExclusion,
       "natExcludeNextIndex": natExcludeNextIndex,
       "natExcludeTable": natExcludeTable,
       "natExcludeEntry": natExcludeEntry,
       "zhoneNATExcludeIndex": zhoneNATExcludeIndex,
       "zhoneNATExcludeRowStatus": zhoneNATExcludeRowStatus,
       "ipStartAddr": ipStartAddr,
       "ipEndAddr": ipEndAddr,
       "comIpZEdgeNat": comIpZEdgeNat}
)
