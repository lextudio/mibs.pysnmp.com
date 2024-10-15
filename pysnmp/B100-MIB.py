# SNMP MIB module (B100-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/B100-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:13 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(one4net,) = mibBuilder.importSymbols(
    "ONE4NET-MIB",
    "one4net")

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
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

b100 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12196, 13)
)
b100.setRevisions(
        ("2011-12-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _Version_Type(OctetString):
    """Custom type version based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Version_Type.__name__ = "OctetString"
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")


class _NumServices_Type(Integer32):
    """Custom type numServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_NumServices_Type.__name__ = "Integer32"
_NumServices_Object = MibScalar
numServices = _NumServices_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 2),
    _NumServices_Type()
)
numServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numServices.setStatus("current")
_HashTableSize_Type = Integer32
_HashTableSize_Object = MibScalar
hashTableSize = _HashTableSize_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 3),
    _HashTableSize_Type()
)
hashTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hashTableSize.setStatus("current")
_TcpTimeOut_Type = TimeInterval
_TcpTimeOut_Object = MibScalar
tcpTimeOut = _TcpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 4),
    _TcpTimeOut_Type()
)
tcpTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpTimeOut.setStatus("current")
_TcpFinTimeOut_Type = TimeInterval
_TcpFinTimeOut_Object = MibScalar
tcpFinTimeOut = _TcpFinTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 5),
    _TcpFinTimeOut_Type()
)
tcpFinTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpFinTimeOut.setStatus("current")
_UdpTimeOut_Type = TimeInterval
_UdpTimeOut_Object = MibScalar
udpTimeOut = _UdpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 6),
    _UdpTimeOut_Type()
)
udpTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpTimeOut.setStatus("current")


class _DaemonState_Type(Integer32):
    """Custom type daemonState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("master", 1),
          ("none", 0))
    )


_DaemonState_Type.__name__ = "Integer32"
_DaemonState_Object = MibScalar
daemonState = _DaemonState_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 7),
    _DaemonState_Type()
)
daemonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daemonState.setStatus("current")


class _McastInterface_Type(OctetString):
    """Custom type mcastInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_McastInterface_Type.__name__ = "OctetString"
_McastInterface_Object = MibScalar
mcastInterface = _McastInterface_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 8),
    _McastInterface_Type()
)
mcastInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastInterface.setStatus("current")


class _HAstate_Type(Integer32):
    """Custom type hAstate based on Integer32"""
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
        *(("master", 1),
          ("none", 0),
          ("passive", 3),
          ("standby", 2))
    )


_HAstate_Type.__name__ = "Integer32"
_HAstate_Object = MibScalar
hAstate = _HAstate_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 9),
    _HAstate_Type()
)
hAstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hAstate.setStatus("current")


class _PatchVersion_Type(OctetString):
    """Custom type patchVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PatchVersion_Type.__name__ = "OctetString"
_PatchVersion_Object = MibScalar
patchVersion = _PatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 10),
    _PatchVersion_Type()
)
patchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    patchVersion.setStatus("current")
_TotalTps_Type = Integer32
_TotalTps_Object = MibScalar
totalTps = _TotalTps_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 11),
    _TotalTps_Type()
)
totalTps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalTps.setStatus("current")
_SslTps_Type = Integer32
_SslTps_Object = MibScalar
sslTps = _SslTps_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 0, 12),
    _SslTps_Type()
)
sslTps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslTps.setStatus("current")
_B100VSTable_Object = MibTable
b100VSTable = _B100VSTable_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1)
)
if mibBuilder.loadTexts:
    b100VSTable.setStatus("current")
_VsEntry_Object = MibTableRow
vsEntry = _VsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1)
)
vsEntry.setIndexNames(
    (0, "B100-MIB", "vSidx"),
)
if mibBuilder.loadTexts:
    vsEntry.setStatus("current")


class _VSidx_Type(Integer32):
    """Custom type vSidx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_VSidx_Type.__name__ = "Integer32"
_VSidx_Object = MibTableColumn
vSidx = _VSidx_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 1),
    _VSidx_Type()
)
vSidx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSidx.setStatus("current")
_VSip_Type = InetAddress
_VSip_Object = MibTableColumn
vSip = _VSip_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 2),
    _VSip_Type()
)
vSip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSip.setStatus("current")
_VSport_Type = InetPortNumber
_VSport_Object = MibTableColumn
vSport = _VSport_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 3),
    _VSport_Type()
)
vSport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSport.setStatus("current")
_VSaddrtype_Type = InetAddressType
_VSaddrtype_Object = MibTableColumn
vSaddrtype = _VSaddrtype_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 4),
    _VSaddrtype_Type()
)
vSaddrtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSaddrtype.setStatus("current")


class _VSprotocol_Type(Integer32):
    """Custom type vSprotocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_VSprotocol_Type.__name__ = "Integer32"
_VSprotocol_Object = MibTableColumn
vSprotocol = _VSprotocol_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 5),
    _VSprotocol_Type()
)
vSprotocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSprotocol.setStatus("current")


class _VSschedulingMethod_Type(OctetString):
    """Custom type vSschedulingMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VSschedulingMethod_Type.__name__ = "OctetString"
_VSschedulingMethod_Object = MibTableColumn
vSschedulingMethod = _VSschedulingMethod_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 6),
    _VSschedulingMethod_Type()
)
vSschedulingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSschedulingMethod.setStatus("current")
_VSpersistenceTimeout_Type = TimeInterval
_VSpersistenceTimeout_Object = MibTableColumn
vSpersistenceTimeout = _VSpersistenceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 7),
    _VSpersistenceTimeout_Type()
)
vSpersistenceTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSpersistenceTimeout.setStatus("current")


class _VScheckerType_Type(OctetString):
    """Custom type vScheckerType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VScheckerType_Type.__name__ = "OctetString"
_VScheckerType_Object = MibTableColumn
vScheckerType = _VScheckerType_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 8),
    _VScheckerType_Type()
)
vScheckerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vScheckerType.setStatus("current")


class _VSadaptiveMethod_Type(OctetString):
    """Custom type vSadaptiveMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VSadaptiveMethod_Type.__name__ = "OctetString"
_VSadaptiveMethod_Object = MibTableColumn
vSadaptiveMethod = _VSadaptiveMethod_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 9),
    _VSadaptiveMethod_Type()
)
vSadaptiveMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSadaptiveMethod.setStatus("current")


class _VSnumDests_Type(Integer32):
    """Custom type vSnumDests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VSnumDests_Type.__name__ = "Integer32"
_VSnumDests_Object = MibTableColumn
vSnumDests = _VSnumDests_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 10),
    _VSnumDests_Type()
)
vSnumDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSnumDests.setStatus("current")


class _VSl7persist_Type(OctetString):
    """Custom type vSl7persist based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VSl7persist_Type.__name__ = "OctetString"
_VSl7persist_Object = MibTableColumn
vSl7persist = _VSl7persist_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 11),
    _VSl7persist_Type()
)
vSl7persist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSl7persist.setStatus("current")


class _VSl7cookieId_Type(OctetString):
    """Custom type vSl7cookieId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VSl7cookieId_Type.__name__ = "OctetString"
_VSl7cookieId_Object = MibTableColumn
vSl7cookieId = _VSl7cookieId_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 12),
    _VSl7cookieId_Type()
)
vSl7cookieId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSl7cookieId.setStatus("current")


class _VSname_Type(OctetString):
    """Custom type vSname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VSname_Type.__name__ = "OctetString"
_VSname_Object = MibTableColumn
vSname = _VSname_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 13),
    _VSname_Type()
)
vSname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSname.setStatus("current")


class _VSstate_Type(Integer32):
    """Custom type vSstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("errormsg", 7),
          ("inService", 1),
          ("outOfService", 2),
          ("redirect", 6),
          ("sorry", 5))
    )


_VSstate_Type.__name__ = "Integer32"
_VSstate_Object = MibTableColumn
vSstate = _VSstate_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 14),
    _VSstate_Type()
)
vSstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSstate.setStatus("current")
_VSfollow_Type = InetPortNumber
_VSfollow_Object = MibTableColumn
vSfollow = _VSfollow_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 15),
    _VSfollow_Type()
)
vSfollow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSfollow.setStatus("current")
_VSConns_Type = Counter32
_VSConns_Object = MibTableColumn
vSConns = _VSConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 16),
    _VSConns_Type()
)
vSConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSConns.setStatus("current")
_VSInPkts_Type = Counter32
_VSInPkts_Object = MibTableColumn
vSInPkts = _VSInPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 17),
    _VSInPkts_Type()
)
vSInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSInPkts.setStatus("current")
_VSOutPkts_Type = Counter32
_VSOutPkts_Object = MibTableColumn
vSOutPkts = _VSOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 18),
    _VSOutPkts_Type()
)
vSOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSOutPkts.setStatus("current")
_VSInBytes_Type = Counter64
_VSInBytes_Object = MibTableColumn
vSInBytes = _VSInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 19),
    _VSInBytes_Type()
)
vSInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSInBytes.setStatus("current")
_VSOutBytes_Type = Counter64
_VSOutBytes_Object = MibTableColumn
vSOutBytes = _VSOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 20),
    _VSOutBytes_Type()
)
vSOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSOutBytes.setStatus("current")
_VSActivConns_Type = Counter32
_VSActivConns_Object = MibTableColumn
vSActivConns = _VSActivConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 21),
    _VSActivConns_Type()
)
vSActivConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSActivConns.setStatus("current")
_B100RSTable_Object = MibTable
b100RSTable = _B100RSTable_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2)
)
if mibBuilder.loadTexts:
    b100RSTable.setStatus("current")
_RsEntry_Object = MibTableRow
rsEntry = _RsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1)
)
rsEntry.setIndexNames(
    (0, "B100-MIB", "rSidx"),
)
if mibBuilder.loadTexts:
    rsEntry.setStatus("current")


class _RSvsidx_Type(Integer32):
    """Custom type rSvsidx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RSvsidx_Type.__name__ = "Integer32"
_RSvsidx_Object = MibTableColumn
rSvsidx = _RSvsidx_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 1),
    _RSvsidx_Type()
)
rSvsidx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSvsidx.setStatus("current")
_RSip_Type = InetAddress
_RSip_Object = MibTableColumn
rSip = _RSip_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 2),
    _RSip_Type()
)
rSip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSip.setStatus("current")
_RSport_Type = InetPortNumber
_RSport_Object = MibTableColumn
rSport = _RSport_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 3),
    _RSport_Type()
)
rSport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSport.setStatus("current")
_RSaddrtype_Type = InetAddressType
_RSaddrtype_Object = MibTableColumn
rSaddrtype = _RSaddrtype_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 4),
    _RSaddrtype_Type()
)
rSaddrtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSaddrtype.setStatus("current")


class _RSidx_Type(Integer32):
    """Custom type rSidx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RSidx_Type.__name__ = "Integer32"
_RSidx_Object = MibTableColumn
rSidx = _RSidx_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 5),
    _RSidx_Type()
)
rSidx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSidx.setStatus("current")


class _RSforwardingMethod_Type(OctetString):
    """Custom type rSforwardingMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RSforwardingMethod_Type.__name__ = "OctetString"
_RSforwardingMethod_Object = MibTableColumn
rSforwardingMethod = _RSforwardingMethod_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 6),
    _RSforwardingMethod_Type()
)
rSforwardingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSforwardingMethod.setStatus("current")


class _RSweight_Type(Integer32):
    """Custom type rSweight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RSweight_Type.__name__ = "Integer32"
_RSweight_Object = MibTableColumn
rSweight = _RSweight_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 7),
    _RSweight_Type()
)
rSweight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSweight.setStatus("current")


class _RSstate_Type(Integer32):
    """Custom type rSstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("inService", 1),
          ("outOfService", 2))
    )


_RSstate_Type.__name__ = "Integer32"
_RSstate_Object = MibTableColumn
rSstate = _RSstate_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 8),
    _RSstate_Type()
)
rSstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSstate.setStatus("current")
_RSConns_Type = Counter32
_RSConns_Object = MibTableColumn
rSConns = _RSConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 12),
    _RSConns_Type()
)
rSConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSConns.setStatus("current")
_RSInPkts_Type = Counter32
_RSInPkts_Object = MibTableColumn
rSInPkts = _RSInPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 13),
    _RSInPkts_Type()
)
rSInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSInPkts.setStatus("current")
_RSOutPkts_Type = Counter32
_RSOutPkts_Object = MibTableColumn
rSOutPkts = _RSOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 14),
    _RSOutPkts_Type()
)
rSOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSOutPkts.setStatus("current")
_RSInBytes_Type = Counter64
_RSInBytes_Object = MibTableColumn
rSInBytes = _RSInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 15),
    _RSInBytes_Type()
)
rSInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSInBytes.setStatus("current")
_RSOutBytes_Type = Counter64
_RSOutBytes_Object = MibTableColumn
rSOutBytes = _RSOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 16),
    _RSOutBytes_Type()
)
rSOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSOutBytes.setStatus("current")
_RSActiveConns_Type = Counter32
_RSActiveConns_Object = MibTableColumn
rSActiveConns = _RSActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 17),
    _RSActiveConns_Type()
)
rSActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSActiveConns.setStatus("current")
_RSInactiveConns_Type = Counter32
_RSInactiveConns_Object = MibTableColumn
rSInactiveConns = _RSInactiveConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 18),
    _RSInactiveConns_Type()
)
rSInactiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSInactiveConns.setStatus("current")
_B100NotificationsPrefix_ObjectIdentity = ObjectIdentity
b100NotificationsPrefix = _B100NotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12196, 13, 3)
)
_B100Notifications_ObjectIdentity = ObjectIdentity
b100Notifications = _B100Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12196, 13, 3, 1)
)


class _AdaptivInterval_Type(Integer32):
    """Custom type adaptivInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdaptivInterval_Type.__name__ = "Integer32"
_AdaptivInterval_Object = MibScalar
adaptivInterval = _AdaptivInterval_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 13),
    _AdaptivInterval_Type()
)
adaptivInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptivInterval.setStatus("current")


class _AdaptivUrl_Type(OctetString):
    """Custom type adaptivUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_AdaptivUrl_Type.__name__ = "OctetString"
_AdaptivUrl_Object = MibScalar
adaptivUrl = _AdaptivUrl_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 14),
    _AdaptivUrl_Type()
)
adaptivUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptivUrl.setStatus("current")


class _AdaptivCtrlMinP_Type(Integer32):
    """Custom type adaptivCtrlMinP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdaptivCtrlMinP_Type.__name__ = "Integer32"
_AdaptivCtrlMinP_Object = MibScalar
adaptivCtrlMinP = _AdaptivCtrlMinP_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 15),
    _AdaptivCtrlMinP_Type()
)
adaptivCtrlMinP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptivCtrlMinP.setStatus("current")


class _AdaptivMinWeight_Type(Integer32):
    """Custom type adaptivMinWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdaptivMinWeight_Type.__name__ = "Integer32"
_AdaptivMinWeight_Object = MibScalar
adaptivMinWeight = _AdaptivMinWeight_Object(
    (1, 3, 6, 1, 4, 1, 12196, 13, 16),
    _AdaptivMinWeight_Type()
)
adaptivMinWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptivMinWeight.setStatus("current")

# Managed Objects groups


# Notification objects

vSstateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 1)
)
vSstateChange.setObjects(
      *(("B100-MIB", "vSstate"),
        ("B100-MIB", "vSip"),
        ("B100-MIB", "vSport"),
        ("B100-MIB", "vSaddrtype"),
        ("B100-MIB", "vSname"),
        ("B100-MIB", "vSidx"))
)
if mibBuilder.loadTexts:
    vSstateChange.setStatus(
        "current"
    )

rSstateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 2)
)
rSstateChange.setObjects(
      *(("B100-MIB", "rSstate"),
        ("B100-MIB", "rSip"),
        ("B100-MIB", "rSport"),
        ("B100-MIB", "rSaddrtype"),
        ("B100-MIB", "rSidx"),
        ("B100-MIB", "vSip"),
        ("B100-MIB", "vSport"),
        ("B100-MIB", "vSaddrtype"),
        ("B100-MIB", "vSname"),
        ("B100-MIB", "vSidx"))
)
if mibBuilder.loadTexts:
    rSstateChange.setStatus(
        "current"
    )

hAstateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 3)
)
hAstateChange.setObjects(
    ("B100-MIB", "hAstate")
)
if mibBuilder.loadTexts:
    hAstateChange.setStatus(
        "current"
    )

licenseExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 4)
)
if mibBuilder.loadTexts:
    licenseExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "B100-MIB",
    **{"b100": b100,
       "version": version,
       "numServices": numServices,
       "hashTableSize": hashTableSize,
       "tcpTimeOut": tcpTimeOut,
       "tcpFinTimeOut": tcpFinTimeOut,
       "udpTimeOut": udpTimeOut,
       "daemonState": daemonState,
       "mcastInterface": mcastInterface,
       "hAstate": hAstate,
       "patchVersion": patchVersion,
       "totalTps": totalTps,
       "sslTps": sslTps,
       "b100VSTable": b100VSTable,
       "vsEntry": vsEntry,
       "vSidx": vSidx,
       "vSip": vSip,
       "vSport": vSport,
       "vSaddrtype": vSaddrtype,
       "vSprotocol": vSprotocol,
       "vSschedulingMethod": vSschedulingMethod,
       "vSpersistenceTimeout": vSpersistenceTimeout,
       "vScheckerType": vScheckerType,
       "vSadaptiveMethod": vSadaptiveMethod,
       "vSnumDests": vSnumDests,
       "vSl7persist": vSl7persist,
       "vSl7cookieId": vSl7cookieId,
       "vSname": vSname,
       "vSstate": vSstate,
       "vSfollow": vSfollow,
       "vSConns": vSConns,
       "vSInPkts": vSInPkts,
       "vSOutPkts": vSOutPkts,
       "vSInBytes": vSInBytes,
       "vSOutBytes": vSOutBytes,
       "vSActivConns": vSActivConns,
       "b100RSTable": b100RSTable,
       "rsEntry": rsEntry,
       "rSvsidx": rSvsidx,
       "rSip": rSip,
       "rSport": rSport,
       "rSaddrtype": rSaddrtype,
       "rSidx": rSidx,
       "rSforwardingMethod": rSforwardingMethod,
       "rSweight": rSweight,
       "rSstate": rSstate,
       "rSConns": rSConns,
       "rSInPkts": rSInPkts,
       "rSOutPkts": rSOutPkts,
       "rSInBytes": rSInBytes,
       "rSOutBytes": rSOutBytes,
       "rSActiveConns": rSActiveConns,
       "rSInactiveConns": rSInactiveConns,
       "b100NotificationsPrefix": b100NotificationsPrefix,
       "b100Notifications": b100Notifications,
       "vSstateChange": vSstateChange,
       "rSstateChange": rSstateChange,
       "hAstateChange": hAstateChange,
       "licenseExceeded": licenseExceeded,
       "adaptivInterval": adaptivInterval,
       "adaptivUrl": adaptivUrl,
       "adaptivCtrlMinP": adaptivCtrlMinP,
       "adaptivMinWeight": adaptivMinWeight}
)
