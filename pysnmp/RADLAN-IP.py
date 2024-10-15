# SNMP MIB module (RADLAN-IP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-IP
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:02 2024
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

(ipCidrRouteDest,
 ipCidrRouteEntry,
 ipCidrRouteMask,
 ipCidrRouteNextHop,
 ipCidrRouteTos) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteDest",
    "ipCidrRouteEntry",
    "ipCidrRouteMask",
    "ipCidrRouteNextHop",
    "ipCidrRouteTos")

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

(rip2IfConfEntry,) = mibBuilder.importSymbols(
    "RFC1389-MIB",
    "rip2IfConfEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(DisplayString,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString")


# MODULE-IDENTITY

ipSpec = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26)
)
ipSpec.setRevisions(
        ("2005-09-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsIpAddrTable_Object = MibTable
rsIpAddrTable = _RsIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1)
)
if mibBuilder.loadTexts:
    rsIpAddrTable.setStatus("current")
_RsIpAddrEntry_Object = MibTableRow
rsIpAddrEntry = _RsIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1)
)
rsIpAddrEntry.setIndexNames(
    (0, "RADLAN-IP", "rsIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    rsIpAddrEntry.setStatus("current")
_RsIpAdEntAddr_Type = IpAddress
_RsIpAdEntAddr_Object = MibTableColumn
rsIpAdEntAddr = _RsIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 1),
    _RsIpAdEntAddr_Type()
)
rsIpAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAdEntAddr.setStatus("current")
_RsIpAdEntIfIndex_Type = Integer32
_RsIpAdEntIfIndex_Object = MibTableColumn
rsIpAdEntIfIndex = _RsIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 2),
    _RsIpAdEntIfIndex_Type()
)
rsIpAdEntIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntIfIndex.setStatus("current")
_RsIpAdEntNetMask_Type = IpAddress
_RsIpAdEntNetMask_Object = MibTableColumn
rsIpAdEntNetMask = _RsIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 3),
    _RsIpAdEntNetMask_Type()
)
rsIpAdEntNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntNetMask.setStatus("current")


class _RsIpAdEntForwardIpBroadcast_Type(Integer32):
    """Custom type rsIpAdEntForwardIpBroadcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIpAdEntForwardIpBroadcast_Type.__name__ = "Integer32"
_RsIpAdEntForwardIpBroadcast_Object = MibTableColumn
rsIpAdEntForwardIpBroadcast = _RsIpAdEntForwardIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 4),
    _RsIpAdEntForwardIpBroadcast_Type()
)
rsIpAdEntForwardIpBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntForwardIpBroadcast.setStatus("current")
_RsIpAdEntBackupAddr_Type = IpAddress
_RsIpAdEntBackupAddr_Object = MibTableColumn
rsIpAdEntBackupAddr = _RsIpAdEntBackupAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 5),
    _RsIpAdEntBackupAddr_Type()
)
rsIpAdEntBackupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntBackupAddr.setStatus("current")


class _RsIpAdEntStatus_Type(Integer32):
    """Custom type rsIpAdEntStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_RsIpAdEntStatus_Type.__name__ = "Integer32"
_RsIpAdEntStatus_Object = MibTableColumn
rsIpAdEntStatus = _RsIpAdEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 6),
    _RsIpAdEntStatus_Type()
)
rsIpAdEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntStatus.setStatus("current")


class _RsIpAdEntBcastAddr_Type(Integer32):
    """Custom type rsIpAdEntBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RsIpAdEntBcastAddr_Type.__name__ = "Integer32"
_RsIpAdEntBcastAddr_Object = MibTableColumn
rsIpAdEntBcastAddr = _RsIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 7),
    _RsIpAdEntBcastAddr_Type()
)
rsIpAdEntBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntBcastAddr.setStatus("current")


class _RsIpAdEntArpServer_Type(Integer32):
    """Custom type rsIpAdEntArpServer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIpAdEntArpServer_Type.__name__ = "Integer32"
_RsIpAdEntArpServer_Object = MibTableColumn
rsIpAdEntArpServer = _RsIpAdEntArpServer_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 8),
    _RsIpAdEntArpServer_Type()
)
rsIpAdEntArpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntArpServer.setStatus("current")


class _RsIpAdEntName_Type(DisplayString):
    """Custom type rsIpAdEntName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsIpAdEntName_Type.__name__ = "DisplayString"
_RsIpAdEntName_Object = MibTableColumn
rsIpAdEntName = _RsIpAdEntName_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 9),
    _RsIpAdEntName_Type()
)
rsIpAdEntName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntName.setStatus("current")


class _RsIpAdEntOwner_Type(Integer32):
    """Custom type rsIpAdEntOwner based on Integer32"""
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
        *(("default", 4),
          ("dhcp", 2),
          ("internal", 3),
          ("static", 1))
    )


_RsIpAdEntOwner_Type.__name__ = "Integer32"
_RsIpAdEntOwner_Object = MibTableColumn
rsIpAdEntOwner = _RsIpAdEntOwner_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 10),
    _RsIpAdEntOwner_Type()
)
rsIpAdEntOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntOwner.setStatus("current")


class _RsIpAdEntAdminStatus_Type(Integer32):
    """Custom type rsIpAdEntAdminStatus based on Integer32"""
    defaultValue = 1

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


_RsIpAdEntAdminStatus_Type.__name__ = "Integer32"
_RsIpAdEntAdminStatus_Object = MibTableColumn
rsIpAdEntAdminStatus = _RsIpAdEntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 11),
    _RsIpAdEntAdminStatus_Type()
)
rsIpAdEntAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntAdminStatus.setStatus("current")


class _RsIpAdEntOperStatus_Type(Integer32):
    """Custom type rsIpAdEntOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RsIpAdEntOperStatus_Type.__name__ = "Integer32"
_RsIpAdEntOperStatus_Object = MibTableColumn
rsIpAdEntOperStatus = _RsIpAdEntOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 12),
    _RsIpAdEntOperStatus_Type()
)
rsIpAdEntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAdEntOperStatus.setStatus("current")
_IcmpSpec_ObjectIdentity = ObjectIdentity
icmpSpec = _IcmpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 2)
)


class _RsIcmpGenErrMsgEnable_Type(Integer32):
    """Custom type rsIcmpGenErrMsgEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIcmpGenErrMsgEnable_Type.__name__ = "Integer32"
_RsIcmpGenErrMsgEnable_Object = MibScalar
rsIcmpGenErrMsgEnable = _RsIcmpGenErrMsgEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 1),
    _RsIcmpGenErrMsgEnable_Type()
)
rsIcmpGenErrMsgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpGenErrMsgEnable.setStatus("current")
_RsIcmpRdTable_Object = MibTable
rsIcmpRdTable = _RsIcmpRdTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2)
)
if mibBuilder.loadTexts:
    rsIcmpRdTable.setStatus("current")
_RsIcmpRdEntry_Object = MibTableRow
rsIcmpRdEntry = _RsIcmpRdEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1)
)
rsIcmpRdEntry.setIndexNames(
    (0, "RADLAN-IP", "rsIcmpRdIpAddr"),
)
if mibBuilder.loadTexts:
    rsIcmpRdEntry.setStatus("current")
_RsIcmpRdIpAddr_Type = IpAddress
_RsIcmpRdIpAddr_Object = MibTableColumn
rsIcmpRdIpAddr = _RsIcmpRdIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 1),
    _RsIcmpRdIpAddr_Type()
)
rsIcmpRdIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIcmpRdIpAddr.setStatus("current")


class _RsIcmpRdIpAdvertAddr_Type(IpAddress):
    """Custom type rsIcmpRdIpAdvertAddr based on IpAddress"""
    defaultHexValue = "E0000001"


_RsIcmpRdIpAdvertAddr_Object = MibTableColumn
rsIcmpRdIpAdvertAddr = _RsIcmpRdIpAdvertAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 2),
    _RsIcmpRdIpAdvertAddr_Type()
)
rsIcmpRdIpAdvertAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdIpAdvertAddr.setStatus("current")


class _RsIcmpRdMaxAdvertInterval_Type(Integer32):
    """Custom type rsIcmpRdMaxAdvertInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_RsIcmpRdMaxAdvertInterval_Type.__name__ = "Integer32"
_RsIcmpRdMaxAdvertInterval_Object = MibTableColumn
rsIcmpRdMaxAdvertInterval = _RsIcmpRdMaxAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 3),
    _RsIcmpRdMaxAdvertInterval_Type()
)
rsIcmpRdMaxAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdMaxAdvertInterval.setStatus("current")


class _RsIcmpRdMinAdvertInterval_Type(Integer32):
    """Custom type rsIcmpRdMinAdvertInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_RsIcmpRdMinAdvertInterval_Type.__name__ = "Integer32"
_RsIcmpRdMinAdvertInterval_Object = MibTableColumn
rsIcmpRdMinAdvertInterval = _RsIcmpRdMinAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 4),
    _RsIcmpRdMinAdvertInterval_Type()
)
rsIcmpRdMinAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdMinAdvertInterval.setStatus("current")


class _RsIcmpRdAdvertLifetime_Type(Integer32):
    """Custom type rsIcmpRdAdvertLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9000),
    )


_RsIcmpRdAdvertLifetime_Type.__name__ = "Integer32"
_RsIcmpRdAdvertLifetime_Object = MibTableColumn
rsIcmpRdAdvertLifetime = _RsIcmpRdAdvertLifetime_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 5),
    _RsIcmpRdAdvertLifetime_Type()
)
rsIcmpRdAdvertLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdAdvertLifetime.setStatus("current")


class _RsIcmpRdAdvertise_Type(Integer32):
    """Custom type rsIcmpRdAdvertise based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsIcmpRdAdvertise_Type.__name__ = "Integer32"
_RsIcmpRdAdvertise_Object = MibTableColumn
rsIcmpRdAdvertise = _RsIcmpRdAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 6),
    _RsIcmpRdAdvertise_Type()
)
rsIcmpRdAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdAdvertise.setStatus("current")


class _RsIcmpRdPreferenceLevel_Type(Integer32):
    """Custom type rsIcmpRdPreferenceLevel based on Integer32"""
    defaultValue = 0


_RsIcmpRdPreferenceLevel_Object = MibTableColumn
rsIcmpRdPreferenceLevel = _RsIcmpRdPreferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 7),
    _RsIcmpRdPreferenceLevel_Type()
)
rsIcmpRdPreferenceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdPreferenceLevel.setStatus("current")
_RsIcmpRdEntStatus_Type = Integer32
_RsIcmpRdEntStatus_Object = MibTableColumn
rsIcmpRdEntStatus = _RsIcmpRdEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 8),
    _RsIcmpRdEntStatus_Type()
)
rsIcmpRdEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdEntStatus.setStatus("current")
_Rip2Spec_ObjectIdentity = ObjectIdentity
rip2Spec = _Rip2Spec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 3)
)
_ArpSpec_ObjectIdentity = ObjectIdentity
arpSpec = _ArpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 4)
)


class _RsArpDeleteTable_Type(Integer32):
    """Custom type rsArpDeleteTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deleteArpTab", 1),
          ("deleteIpArpDelDynamicRefreshStatic", 4),
          ("deleteIpArpDynamicEntries", 2),
          ("deleteIpArpStaticEntries", 3),
          ("noAction", 0))
    )


_RsArpDeleteTable_Type.__name__ = "Integer32"
_RsArpDeleteTable_Object = MibScalar
rsArpDeleteTable = _RsArpDeleteTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 1),
    _RsArpDeleteTable_Type()
)
rsArpDeleteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsArpDeleteTable.setStatus("current")


class _RsArpInactiveTimeOut_Type(Unsigned32):
    """Custom type rsArpInactiveTimeOut based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40000000),
    )


_RsArpInactiveTimeOut_Type.__name__ = "Unsigned32"
_RsArpInactiveTimeOut_Object = MibScalar
rsArpInactiveTimeOut = _RsArpInactiveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 2),
    _RsArpInactiveTimeOut_Type()
)
rsArpInactiveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsArpInactiveTimeOut.setStatus("current")


class _RsArpProxy_Type(Integer32):
    """Custom type rsArpProxy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsArpProxy_Type.__name__ = "Integer32"
_RsArpProxy_Object = MibScalar
rsArpProxy = _RsArpProxy_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 3),
    _RsArpProxy_Type()
)
rsArpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsArpProxy.setStatus("current")
_RsArpRequestsSent_Type = Counter32
_RsArpRequestsSent_Object = MibScalar
rsArpRequestsSent = _RsArpRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 4),
    _RsArpRequestsSent_Type()
)
rsArpRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsArpRequestsSent.setStatus("current")
_RsArpRepliesSent_Type = Counter32
_RsArpRepliesSent_Object = MibScalar
rsArpRepliesSent = _RsArpRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 5),
    _RsArpRepliesSent_Type()
)
rsArpRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsArpRepliesSent.setStatus("current")
_RsArpProxyRepliesSent_Type = Counter32
_RsArpProxyRepliesSent_Object = MibScalar
rsArpProxyRepliesSent = _RsArpProxyRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 6),
    _RsArpProxyRepliesSent_Type()
)
rsArpProxyRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsArpProxyRepliesSent.setStatus("current")
_RsArpUnresolveTimer_Type = Integer32
_RsArpUnresolveTimer_Object = MibScalar
rsArpUnresolveTimer = _RsArpUnresolveTimer_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 7),
    _RsArpUnresolveTimer_Type()
)
rsArpUnresolveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsArpUnresolveTimer.setStatus("current")
_RsArpMibVersion_Type = Integer32
_RsArpMibVersion_Object = MibScalar
rsArpMibVersion = _RsArpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 8),
    _RsArpMibVersion_Type()
)
rsArpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsArpMibVersion.setStatus("current")
_Tftp_ObjectIdentity = ObjectIdentity
tftp = _Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 5)
)


class _RsTftpRetryTimeOut_Type(Integer32):
    """Custom type rsTftpRetryTimeOut based on Integer32"""
    defaultValue = 15


_RsTftpRetryTimeOut_Object = MibScalar
rsTftpRetryTimeOut = _RsTftpRetryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 1),
    _RsTftpRetryTimeOut_Type()
)
rsTftpRetryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTftpRetryTimeOut.setStatus("current")


class _RsTftpTotalTimeOut_Type(Integer32):
    """Custom type rsTftpTotalTimeOut based on Integer32"""
    defaultValue = 60


_RsTftpTotalTimeOut_Object = MibScalar
rsTftpTotalTimeOut = _RsTftpTotalTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 2),
    _RsTftpTotalTimeOut_Type()
)
rsTftpTotalTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTftpTotalTimeOut.setStatus("current")
_RsSendConfigFile_Type = DisplayString
_RsSendConfigFile_Object = MibScalar
rsSendConfigFile = _RsSendConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 3),
    _RsSendConfigFile_Type()
)
rsSendConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSendConfigFile.setStatus("current")
_RsGetConfigFile_Type = DisplayString
_RsGetConfigFile_Object = MibScalar
rsGetConfigFile = _RsGetConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 4),
    _RsGetConfigFile_Type()
)
rsGetConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsGetConfigFile.setStatus("current")
_RsLoadSoftware_Type = DisplayString
_RsLoadSoftware_Object = MibScalar
rsLoadSoftware = _RsLoadSoftware_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 5),
    _RsLoadSoftware_Type()
)
rsLoadSoftware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLoadSoftware.setStatus("current")
_RsFileServerAddress_Type = IpAddress
_RsFileServerAddress_Object = MibScalar
rsFileServerAddress = _RsFileServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 6),
    _RsFileServerAddress_Type()
)
rsFileServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFileServerAddress.setStatus("current")


class _RsSoftwareDeviceName_Type(DisplayString):
    """Custom type rsSoftwareDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RsSoftwareDeviceName_Type.__name__ = "DisplayString"
_RsSoftwareDeviceName_Object = MibScalar
rsSoftwareDeviceName = _RsSoftwareDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 7),
    _RsSoftwareDeviceName_Type()
)
rsSoftwareDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSoftwareDeviceName.setStatus("current")


class _RsSoftwareFileAction_Type(Integer32):
    """Custom type rsSoftwareFileAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 2))
    )


_RsSoftwareFileAction_Type.__name__ = "Integer32"
_RsSoftwareFileAction_Object = MibScalar
rsSoftwareFileAction = _RsSoftwareFileAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 8),
    _RsSoftwareFileAction_Type()
)
rsSoftwareFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSoftwareFileAction.setStatus("current")
_IpRedundancy_ObjectIdentity = ObjectIdentity
ipRedundancy = _IpRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 6)
)
_IpRouteLeaking_ObjectIdentity = ObjectIdentity
ipRouteLeaking = _IpRouteLeaking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 7)
)
_IpRipFilter_ObjectIdentity = ObjectIdentity
ipRipFilter = _IpRipFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 8)
)


class _RsRipEnable_Type(Integer32):
    """Custom type rsRipEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RsRipEnable_Type.__name__ = "Integer32"
_RsRipEnable_Object = MibScalar
rsRipEnable = _RsRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 9),
    _RsRipEnable_Type()
)
rsRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRipEnable.setStatus("current")
_RsTelnetPassword_Type = OctetString
_RsTelnetPassword_Object = MibScalar
rsTelnetPassword = _RsTelnetPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 11),
    _RsTelnetPassword_Type()
)
rsTelnetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTelnetPassword.setStatus("current")
_RlTranslationNameToIpTable_Object = MibTable
rlTranslationNameToIpTable = _RlTranslationNameToIpTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12)
)
if mibBuilder.loadTexts:
    rlTranslationNameToIpTable.setStatus("current")
_RlTranslationNameToIpEntry_Object = MibTableRow
rlTranslationNameToIpEntry = _RlTranslationNameToIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12, 1)
)
rlTranslationNameToIpEntry.setIndexNames(
    (1, "RADLAN-IP", "rlTranslationNameToIpName"),
)
if mibBuilder.loadTexts:
    rlTranslationNameToIpEntry.setStatus("current")


class _RlTranslationNameToIpName_Type(DisplayString):
    """Custom type rlTranslationNameToIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RlTranslationNameToIpName_Type.__name__ = "DisplayString"
_RlTranslationNameToIpName_Object = MibTableColumn
rlTranslationNameToIpName = _RlTranslationNameToIpName_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12, 1, 1),
    _RlTranslationNameToIpName_Type()
)
rlTranslationNameToIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTranslationNameToIpName.setStatus("current")
_RlTranslationNameToIpIpAddr_Type = IpAddress
_RlTranslationNameToIpIpAddr_Object = MibTableColumn
rlTranslationNameToIpIpAddr = _RlTranslationNameToIpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 12, 1, 2),
    _RlTranslationNameToIpIpAddr_Type()
)
rlTranslationNameToIpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTranslationNameToIpIpAddr.setStatus("current")
_RlIpRoutingProtPreference_ObjectIdentity = ObjectIdentity
rlIpRoutingProtPreference = _RlIpRoutingProtPreference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 13)
)
_RlOspf_ObjectIdentity = ObjectIdentity
rlOspf = _RlOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 14)
)
_RlIpAddrTableMibVersion_Type = Integer32
_RlIpAddrTableMibVersion_Object = MibScalar
rlIpAddrTableMibVersion = _RlIpAddrTableMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 15),
    _RlIpAddrTableMibVersion_Type()
)
rlIpAddrTableMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpAddrTableMibVersion.setStatus("current")
_RlIpCidrRouteExtTable_Object = MibTable
rlIpCidrRouteExtTable = _RlIpCidrRouteExtTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 16)
)
if mibBuilder.loadTexts:
    rlIpCidrRouteExtTable.setStatus("current")
_RlIpCidrRouteExtEntry_Object = MibTableRow
rlIpCidrRouteExtEntry = _RlIpCidrRouteExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 16, 1)
)
if mibBuilder.loadTexts:
    rlIpCidrRouteExtEntry.setStatus("current")


class _RlIpCidrRouteProto_Type(Integer32):
    """Custom type rlIpCidrRouteProto based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("aggregateRoute", 9),
          ("bgp4External", 8),
          ("bgp4Internal", 7),
          ("local", 1),
          ("netmgmt", 2),
          ("ospfAggregateNetRange", 6),
          ("ospfExternal", 5),
          ("ospfInternal", 4),
          ("other", 10),
          ("rip", 3))
    )


_RlIpCidrRouteProto_Type.__name__ = "Integer32"
_RlIpCidrRouteProto_Object = MibTableColumn
rlIpCidrRouteProto = _RlIpCidrRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 16, 1, 1),
    _RlIpCidrRouteProto_Type()
)
rlIpCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpCidrRouteProto.setStatus("current")
_RlIpStaticRoute_ObjectIdentity = ObjectIdentity
rlIpStaticRoute = _RlIpStaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 17)
)
_RlIpStaticRouteTable_Object = MibTable
rlIpStaticRouteTable = _RlIpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 17, 1)
)
if mibBuilder.loadTexts:
    rlIpStaticRouteTable.setStatus("current")
_RlIpStaticRouteEntry_Object = MibTableRow
rlIpStaticRouteEntry = _RlIpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 17, 1, 1)
)
rlIpStaticRouteEntry.setIndexNames(
    (0, "RADLAN-IP", "rlIpStaticRouteDest"),
    (0, "RADLAN-IP", "rlIpStaticRouteMask"),
    (0, "RADLAN-IP", "rlIpStaticRouteTos"),
    (0, "RADLAN-IP", "rlIpStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    rlIpStaticRouteEntry.setStatus("current")
_RlIpStaticRouteDest_Type = IpAddress
_RlIpStaticRouteDest_Object = MibTableColumn
rlIpStaticRouteDest = _RlIpStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 17, 1, 1, 1),
    _RlIpStaticRouteDest_Type()
)
rlIpStaticRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpStaticRouteDest.setStatus("current")
_RlIpStaticRouteMask_Type = IpAddress
_RlIpStaticRouteMask_Object = MibTableColumn
rlIpStaticRouteMask = _RlIpStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 17, 1, 1, 2),
    _RlIpStaticRouteMask_Type()
)
rlIpStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpStaticRouteMask.setStatus("current")
_RlIpStaticRouteTos_Type = Integer32
_RlIpStaticRouteTos_Object = MibTableColumn
rlIpStaticRouteTos = _RlIpStaticRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 17, 1, 1, 3),
    _RlIpStaticRouteTos_Type()
)
rlIpStaticRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpStaticRouteTos.setStatus("current")
_RlIpStaticRouteNextHop_Type = IpAddress
_RlIpStaticRouteNextHop_Object = MibTableColumn
rlIpStaticRouteNextHop = _RlIpStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 17, 1, 1, 4),
    _RlIpStaticRouteNextHop_Type()
)
rlIpStaticRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpStaticRouteNextHop.setStatus("current")
_RlIpStaticRouteMetric_Type = Integer32
_RlIpStaticRouteMetric_Object = MibTableColumn
rlIpStaticRouteMetric = _RlIpStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 17, 1, 1, 5),
    _RlIpStaticRouteMetric_Type()
)
rlIpStaticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStaticRouteMetric.setStatus("current")


class _RlIpStaticRouteType_Type(Integer32):
    """Custom type rlIpStaticRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("reject", 1),
          ("remote", 3))
    )


_RlIpStaticRouteType_Type.__name__ = "Integer32"
_RlIpStaticRouteType_Object = MibTableColumn
rlIpStaticRouteType = _RlIpStaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 17, 1, 1, 6),
    _RlIpStaticRouteType_Type()
)
rlIpStaticRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStaticRouteType.setStatus("current")


class _RlIpStaticRouteNextHopAS_Type(Integer32):
    """Custom type rlIpStaticRouteNextHopAS based on Integer32"""
    defaultValue = 0


_RlIpStaticRouteNextHopAS_Object = MibTableColumn
rlIpStaticRouteNextHopAS = _RlIpStaticRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 17, 1, 1, 7),
    _RlIpStaticRouteNextHopAS_Type()
)
rlIpStaticRouteNextHopAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStaticRouteNextHopAS.setStatus("current")


class _RlIpStaticRouteForwardingStatus_Type(Integer32):
    """Custom type rlIpStaticRouteForwardingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RlIpStaticRouteForwardingStatus_Type.__name__ = "Integer32"
_RlIpStaticRouteForwardingStatus_Object = MibTableColumn
rlIpStaticRouteForwardingStatus = _RlIpStaticRouteForwardingStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 17, 1, 1, 8),
    _RlIpStaticRouteForwardingStatus_Type()
)
rlIpStaticRouteForwardingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpStaticRouteForwardingStatus.setStatus("current")
_RlIpStaticRouteRowStatus_Type = RowStatus
_RlIpStaticRouteRowStatus_Object = MibTableColumn
rlIpStaticRouteRowStatus = _RlIpStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 17, 1, 1, 9),
    _RlIpStaticRouteRowStatus_Type()
)
rlIpStaticRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpStaticRouteRowStatus.setStatus("current")


class _RlIpStaticRouteOwner_Type(Integer32):
    """Custom type rlIpStaticRouteOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("dhcp", 2),
          ("static", 1))
    )


_RlIpStaticRouteOwner_Type.__name__ = "Integer32"
_RlIpStaticRouteOwner_Object = MibTableColumn
rlIpStaticRouteOwner = _RlIpStaticRouteOwner_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 17, 1, 1, 10),
    _RlIpStaticRouteOwner_Type()
)
rlIpStaticRouteOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpStaticRouteOwner.setStatus("current")
_RlIpRouter_ObjectIdentity = ObjectIdentity
rlIpRouter = _RlIpRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 18)
)
ipCidrRouteEntry.registerAugmentions(
    ("RADLAN-IP",
     "rlIpCidrRouteExtEntry")
)
rlIpCidrRouteExtEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-IP",
    **{"ipSpec": ipSpec,
       "rsIpAddrTable": rsIpAddrTable,
       "rsIpAddrEntry": rsIpAddrEntry,
       "rsIpAdEntAddr": rsIpAdEntAddr,
       "rsIpAdEntIfIndex": rsIpAdEntIfIndex,
       "rsIpAdEntNetMask": rsIpAdEntNetMask,
       "rsIpAdEntForwardIpBroadcast": rsIpAdEntForwardIpBroadcast,
       "rsIpAdEntBackupAddr": rsIpAdEntBackupAddr,
       "rsIpAdEntStatus": rsIpAdEntStatus,
       "rsIpAdEntBcastAddr": rsIpAdEntBcastAddr,
       "rsIpAdEntArpServer": rsIpAdEntArpServer,
       "rsIpAdEntName": rsIpAdEntName,
       "rsIpAdEntOwner": rsIpAdEntOwner,
       "rsIpAdEntAdminStatus": rsIpAdEntAdminStatus,
       "rsIpAdEntOperStatus": rsIpAdEntOperStatus,
       "icmpSpec": icmpSpec,
       "rsIcmpGenErrMsgEnable": rsIcmpGenErrMsgEnable,
       "rsIcmpRdTable": rsIcmpRdTable,
       "rsIcmpRdEntry": rsIcmpRdEntry,
       "rsIcmpRdIpAddr": rsIcmpRdIpAddr,
       "rsIcmpRdIpAdvertAddr": rsIcmpRdIpAdvertAddr,
       "rsIcmpRdMaxAdvertInterval": rsIcmpRdMaxAdvertInterval,
       "rsIcmpRdMinAdvertInterval": rsIcmpRdMinAdvertInterval,
       "rsIcmpRdAdvertLifetime": rsIcmpRdAdvertLifetime,
       "rsIcmpRdAdvertise": rsIcmpRdAdvertise,
       "rsIcmpRdPreferenceLevel": rsIcmpRdPreferenceLevel,
       "rsIcmpRdEntStatus": rsIcmpRdEntStatus,
       "rip2Spec": rip2Spec,
       "arpSpec": arpSpec,
       "rsArpDeleteTable": rsArpDeleteTable,
       "rsArpInactiveTimeOut": rsArpInactiveTimeOut,
       "rsArpProxy": rsArpProxy,
       "rsArpRequestsSent": rsArpRequestsSent,
       "rsArpRepliesSent": rsArpRepliesSent,
       "rsArpProxyRepliesSent": rsArpProxyRepliesSent,
       "rsArpUnresolveTimer": rsArpUnresolveTimer,
       "rsArpMibVersion": rsArpMibVersion,
       "tftp": tftp,
       "rsTftpRetryTimeOut": rsTftpRetryTimeOut,
       "rsTftpTotalTimeOut": rsTftpTotalTimeOut,
       "rsSendConfigFile": rsSendConfigFile,
       "rsGetConfigFile": rsGetConfigFile,
       "rsLoadSoftware": rsLoadSoftware,
       "rsFileServerAddress": rsFileServerAddress,
       "rsSoftwareDeviceName": rsSoftwareDeviceName,
       "rsSoftwareFileAction": rsSoftwareFileAction,
       "ipRedundancy": ipRedundancy,
       "ipRouteLeaking": ipRouteLeaking,
       "ipRipFilter": ipRipFilter,
       "rsRipEnable": rsRipEnable,
       "rsTelnetPassword": rsTelnetPassword,
       "rlTranslationNameToIpTable": rlTranslationNameToIpTable,
       "rlTranslationNameToIpEntry": rlTranslationNameToIpEntry,
       "rlTranslationNameToIpName": rlTranslationNameToIpName,
       "rlTranslationNameToIpIpAddr": rlTranslationNameToIpIpAddr,
       "rlIpRoutingProtPreference": rlIpRoutingProtPreference,
       "rlOspf": rlOspf,
       "rlIpAddrTableMibVersion": rlIpAddrTableMibVersion,
       "rlIpCidrRouteExtTable": rlIpCidrRouteExtTable,
       "rlIpCidrRouteExtEntry": rlIpCidrRouteExtEntry,
       "rlIpCidrRouteProto": rlIpCidrRouteProto,
       "rlIpStaticRoute": rlIpStaticRoute,
       "rlIpStaticRouteTable": rlIpStaticRouteTable,
       "rlIpStaticRouteEntry": rlIpStaticRouteEntry,
       "rlIpStaticRouteDest": rlIpStaticRouteDest,
       "rlIpStaticRouteMask": rlIpStaticRouteMask,
       "rlIpStaticRouteTos": rlIpStaticRouteTos,
       "rlIpStaticRouteNextHop": rlIpStaticRouteNextHop,
       "rlIpStaticRouteMetric": rlIpStaticRouteMetric,
       "rlIpStaticRouteType": rlIpStaticRouteType,
       "rlIpStaticRouteNextHopAS": rlIpStaticRouteNextHopAS,
       "rlIpStaticRouteForwardingStatus": rlIpStaticRouteForwardingStatus,
       "rlIpStaticRouteRowStatus": rlIpStaticRouteRowStatus,
       "rlIpStaticRouteOwner": rlIpStaticRouteOwner,
       "rlIpRouter": rlIpRouter}
)
