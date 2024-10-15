# SNMP MIB module (REDSTONE-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:41 2024
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

(ipCidrRouteEntry,) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteEntry")

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsEnable,
 RsIpAddrLessIf,
 RsNextIfIndex) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsEnable",
    "RsIpAddrLessIf",
    "RsNextIfIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rsIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12)
)
rsIpMIB.setRevisions(
        ("1999-09-16 00:00",
         "1999-08-13 00:00",
         "1998-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsIpObjects_ObjectIdentity = ObjectIdentity
rsIpObjects = _RsIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1)
)
_RsIpInterface_ObjectIdentity = ObjectIdentity
rsIpInterface = _RsIpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 1)
)
_RsIpNextIfIndex_Type = RsNextIfIndex
_RsIpNextIfIndex_Object = MibScalar
rsIpNextIfIndex = _RsIpNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 1, 1),
    _RsIpNextIfIndex_Type()
)
rsIpNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpNextIfIndex.setStatus("current")
_RsIpIfTable_Object = MibTable
rsIpIfTable = _RsIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rsIpIfTable.setStatus("current")
_RsIpIfEntry_Object = MibTableRow
rsIpIfEntry = _RsIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 1, 2, 1)
)
rsIpIfEntry.setIndexNames(
    (0, "REDSTONE-IP-MIB", "rsIpIfIndex"),
)
if mibBuilder.loadTexts:
    rsIpIfEntry.setStatus("current")
_RsIpIfIndex_Type = InterfaceIndex
_RsIpIfIndex_Object = MibTableColumn
rsIpIfIndex = _RsIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 1, 2, 1, 1),
    _RsIpIfIndex_Type()
)
rsIpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsIpIfIndex.setStatus("current")
_RsIpIfRowStatus_Type = RowStatus
_RsIpIfRowStatus_Object = MibTableColumn
rsIpIfRowStatus = _RsIpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 1, 2, 1, 2),
    _RsIpIfRowStatus_Type()
)
rsIpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpIfRowStatus.setStatus("current")
_RsIpIfLowerIfIndex_Type = InterfaceIndexOrZero
_RsIpIfLowerIfIndex_Object = MibTableColumn
rsIpIfLowerIfIndex = _RsIpIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 1, 2, 1, 3),
    _RsIpIfLowerIfIndex_Type()
)
rsIpIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpIfLowerIfIndex.setStatus("current")


class _RsIpIfType_Type(Integer32):
    """Custom type rsIpIfType based on Integer32"""
    defaultValue = 2

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
        *(("broadcast", 1),
          ("loopback", 4),
          ("nbma", 3),
          ("other", 0),
          ("pointToPoint", 2))
    )


_RsIpIfType_Type.__name__ = "Integer32"
_RsIpIfType_Object = MibTableColumn
rsIpIfType = _RsIpIfType_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 1, 2, 1, 4),
    _RsIpIfType_Type()
)
rsIpIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpIfType.setStatus("current")
_RsIpAddress_ObjectIdentity = ObjectIdentity
rsIpAddress = _RsIpAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2)
)
_RsIpAddrGlobals_ObjectIdentity = ObjectIdentity
rsIpAddrGlobals = _RsIpAddrGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 1)
)


class _RsIpArpTimeout_Type(Integer32):
    """Custom type rsIpArpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RsIpArpTimeout_Type.__name__ = "Integer32"
_RsIpArpTimeout_Object = MibScalar
rsIpArpTimeout = _RsIpArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 1, 1),
    _RsIpArpTimeout_Type()
)
rsIpArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpArpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rsIpArpTimeout.setUnits("seconds")
_RsIpAddrTable_Object = MibTable
rsIpAddrTable = _RsIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rsIpAddrTable.setStatus("current")
_RsIpAddrEntry_Object = MibTableRow
rsIpAddrEntry = _RsIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1)
)
rsIpAddrEntry.setIndexNames(
    (0, "REDSTONE-IP-MIB", "rsIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    rsIpAddrEntry.setStatus("current")
_RsIpAdEntAddr_Type = RsIpAddrLessIf
_RsIpAdEntAddr_Object = MibTableColumn
rsIpAdEntAddr = _RsIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 1),
    _RsIpAdEntAddr_Type()
)
rsIpAdEntAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsIpAdEntAddr.setStatus("current")
_RsIpAdEntIfIndex_Type = InterfaceIndex
_RsIpAdEntIfIndex_Object = MibTableColumn
rsIpAdEntIfIndex = _RsIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 2),
    _RsIpAdEntIfIndex_Type()
)
rsIpAdEntIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntIfIndex.setStatus("current")


class _RsIpAdEntNetMask_Type(IpAddress):
    """Custom type rsIpAdEntNetMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_RsIpAdEntNetMask_Object = MibTableColumn
rsIpAdEntNetMask = _RsIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 3),
    _RsIpAdEntNetMask_Type()
)
rsIpAdEntNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntNetMask.setStatus("current")


class _RsIpAdEntBcastAddr_Type(Integer32):
    """Custom type rsIpAdEntBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RsIpAdEntBcastAddr_Type.__name__ = "Integer32"
_RsIpAdEntBcastAddr_Object = MibTableColumn
rsIpAdEntBcastAddr = _RsIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 4),
    _RsIpAdEntBcastAddr_Type()
)
rsIpAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAdEntBcastAddr.setStatus("current")


class _RsIpAdEntReasmMaxSize_Type(Integer32):
    """Custom type rsIpAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_RsIpAdEntReasmMaxSize_Object = MibTableColumn
rsIpAdEntReasmMaxSize = _RsIpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 5),
    _RsIpAdEntReasmMaxSize_Type()
)
rsIpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAdEntReasmMaxSize.setStatus("current")
_RsIpAdEntRowStatus_Type = RowStatus
_RsIpAdEntRowStatus_Object = MibTableColumn
rsIpAdEntRowStatus = _RsIpAdEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 6),
    _RsIpAdEntRowStatus_Type()
)
rsIpAdEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntRowStatus.setStatus("current")


class _RsIpAdEntAdminStatus_Type(RsEnable):
    """Custom type rsIpAdEntAdminStatus based on RsEnable"""


_RsIpAdEntAdminStatus_Object = MibTableColumn
rsIpAdEntAdminStatus = _RsIpAdEntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 7),
    _RsIpAdEntAdminStatus_Type()
)
rsIpAdEntAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntAdminStatus.setStatus("current")


class _RsIpAdEntArpRspEnable_Type(RsEnable):
    """Custom type rsIpAdEntArpRspEnable based on RsEnable"""


_RsIpAdEntArpRspEnable_Object = MibTableColumn
rsIpAdEntArpRspEnable = _RsIpAdEntArpRspEnable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 8),
    _RsIpAdEntArpRspEnable_Type()
)
rsIpAdEntArpRspEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntArpRspEnable.setStatus("current")


class _RsIpAdEntProxyArpRspEnable_Type(RsEnable):
    """Custom type rsIpAdEntProxyArpRspEnable based on RsEnable"""


_RsIpAdEntProxyArpRspEnable_Object = MibTableColumn
rsIpAdEntProxyArpRspEnable = _RsIpAdEntProxyArpRspEnable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 9),
    _RsIpAdEntProxyArpRspEnable_Type()
)
rsIpAdEntProxyArpRspEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntProxyArpRspEnable.setStatus("current")


class _RsIpAdEntIgmpEnable_Type(RsEnable):
    """Custom type rsIpAdEntIgmpEnable based on RsEnable"""


_RsIpAdEntIgmpEnable_Object = MibTableColumn
rsIpAdEntIgmpEnable = _RsIpAdEntIgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 10),
    _RsIpAdEntIgmpEnable_Type()
)
rsIpAdEntIgmpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntIgmpEnable.setStatus("current")


class _RsIpAdEntDirectedBcastEnable_Type(RsEnable):
    """Custom type rsIpAdEntDirectedBcastEnable based on RsEnable"""


_RsIpAdEntDirectedBcastEnable_Object = MibTableColumn
rsIpAdEntDirectedBcastEnable = _RsIpAdEntDirectedBcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 11),
    _RsIpAdEntDirectedBcastEnable_Type()
)
rsIpAdEntDirectedBcastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntDirectedBcastEnable.setStatus("current")


class _RsIpAdEntIcmpRedirectEnable_Type(RsEnable):
    """Custom type rsIpAdEntIcmpRedirectEnable based on RsEnable"""


_RsIpAdEntIcmpRedirectEnable_Object = MibTableColumn
rsIpAdEntIcmpRedirectEnable = _RsIpAdEntIcmpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 12),
    _RsIpAdEntIcmpRedirectEnable_Type()
)
rsIpAdEntIcmpRedirectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntIcmpRedirectEnable.setStatus("current")


class _RsIpAdEntIcmpMaskReplyEnable_Type(RsEnable):
    """Custom type rsIpAdEntIcmpMaskReplyEnable based on RsEnable"""


_RsIpAdEntIcmpMaskReplyEnable_Object = MibTableColumn
rsIpAdEntIcmpMaskReplyEnable = _RsIpAdEntIcmpMaskReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 13),
    _RsIpAdEntIcmpMaskReplyEnable_Type()
)
rsIpAdEntIcmpMaskReplyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntIcmpMaskReplyEnable.setStatus("current")


class _RsIpAdEntIcmpUnreachEnable_Type(RsEnable):
    """Custom type rsIpAdEntIcmpUnreachEnable based on RsEnable"""


_RsIpAdEntIcmpUnreachEnable_Object = MibTableColumn
rsIpAdEntIcmpUnreachEnable = _RsIpAdEntIcmpUnreachEnable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 14),
    _RsIpAdEntIcmpUnreachEnable_Type()
)
rsIpAdEntIcmpUnreachEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntIcmpUnreachEnable.setStatus("current")


class _RsIpAdEntMtu_Type(Integer32):
    """Custom type rsIpAdEntMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpAdEntMtu_Type.__name__ = "Integer32"
_RsIpAdEntMtu_Object = MibTableColumn
rsIpAdEntMtu = _RsIpAdEntMtu_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 15),
    _RsIpAdEntMtu_Type()
)
rsIpAdEntMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntMtu.setStatus("current")


class _RsIpAdEntUnnumLoopbackIfIndex_Type(InterfaceIndexOrZero):
    """Custom type rsIpAdEntUnnumLoopbackIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_RsIpAdEntUnnumLoopbackIfIndex_Object = MibTableColumn
rsIpAdEntUnnumLoopbackIfIndex = _RsIpAdEntUnnumLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 16),
    _RsIpAdEntUnnumLoopbackIfIndex_Type()
)
rsIpAdEntUnnumLoopbackIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntUnnumLoopbackIfIndex.setStatus("current")


class _RsIpAdEntIrdpEnable_Type(RsEnable):
    """Custom type rsIpAdEntIrdpEnable based on RsEnable"""


_RsIpAdEntIrdpEnable_Object = MibTableColumn
rsIpAdEntIrdpEnable = _RsIpAdEntIrdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 17),
    _RsIpAdEntIrdpEnable_Type()
)
rsIpAdEntIrdpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntIrdpEnable.setStatus("current")


class _RsIpAdEntAccessRouteEnable_Type(RsEnable):
    """Custom type rsIpAdEntAccessRouteEnable based on RsEnable"""


_RsIpAdEntAccessRouteEnable_Object = MibTableColumn
rsIpAdEntAccessRouteEnable = _RsIpAdEntAccessRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 18),
    _RsIpAdEntAccessRouteEnable_Type()
)
rsIpAdEntAccessRouteEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAdEntAccessRouteEnable.setStatus("current")
_RsIpAdEntAccessRouteHost_Type = IpAddress
_RsIpAdEntAccessRouteHost_Object = MibTableColumn
rsIpAdEntAccessRouteHost = _RsIpAdEntAccessRouteHost_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 2, 2, 1, 19),
    _RsIpAdEntAccessRouteHost_Type()
)
rsIpAdEntAccessRouteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAdEntAccessRouteHost.setStatus("current")
_RsIpRoute_ObjectIdentity = ObjectIdentity
rsIpRoute = _RsIpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3)
)
_RsIpRouteGlobals_ObjectIdentity = ObjectIdentity
rsIpRouteGlobals = _RsIpRouteGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 1)
)
_RsIpRouteLimit_Type = Integer32
_RsIpRouteLimit_Object = MibScalar
rsIpRouteLimit = _RsIpRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 1, 1),
    _RsIpRouteLimit_Type()
)
rsIpRouteLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRouteLimit.setStatus("current")
_RsIpRouteStaticTable_Object = MibTable
rsIpRouteStaticTable = _RsIpRouteStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rsIpRouteStaticTable.setStatus("current")
_RsIpRouteStaticEntry_Object = MibTableRow
rsIpRouteStaticEntry = _RsIpRouteStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 2, 1)
)
rsIpRouteStaticEntry.setIndexNames(
    (0, "REDSTONE-IP-MIB", "rsIpRouteStaticDest"),
    (0, "REDSTONE-IP-MIB", "rsIpRouteStaticMask"),
    (0, "REDSTONE-IP-MIB", "rsIpRouteStaticPref"),
    (0, "REDSTONE-IP-MIB", "rsIpRouteStaticNextHop"),
)
if mibBuilder.loadTexts:
    rsIpRouteStaticEntry.setStatus("current")
_RsIpRouteStaticDest_Type = IpAddress
_RsIpRouteStaticDest_Object = MibTableColumn
rsIpRouteStaticDest = _RsIpRouteStaticDest_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 2, 1, 1),
    _RsIpRouteStaticDest_Type()
)
rsIpRouteStaticDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRouteStaticDest.setStatus("current")
_RsIpRouteStaticMask_Type = IpAddress
_RsIpRouteStaticMask_Object = MibTableColumn
rsIpRouteStaticMask = _RsIpRouteStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 2, 1, 2),
    _RsIpRouteStaticMask_Type()
)
rsIpRouteStaticMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRouteStaticMask.setStatus("current")


class _RsIpRouteStaticPref_Type(Integer32):
    """Custom type rsIpRouteStaticPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsIpRouteStaticPref_Type.__name__ = "Integer32"
_RsIpRouteStaticPref_Object = MibTableColumn
rsIpRouteStaticPref = _RsIpRouteStaticPref_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 2, 1, 3),
    _RsIpRouteStaticPref_Type()
)
rsIpRouteStaticPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRouteStaticPref.setStatus("current")
_RsIpRouteStaticNextHop_Type = IpAddress
_RsIpRouteStaticNextHop_Object = MibTableColumn
rsIpRouteStaticNextHop = _RsIpRouteStaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 2, 1, 4),
    _RsIpRouteStaticNextHop_Type()
)
rsIpRouteStaticNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRouteStaticNextHop.setStatus("current")
_RsIpRouteStaticRowStatus_Type = RowStatus
_RsIpRouteStaticRowStatus_Object = MibTableColumn
rsIpRouteStaticRowStatus = _RsIpRouteStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 2, 1, 5),
    _RsIpRouteStaticRowStatus_Type()
)
rsIpRouteStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpRouteStaticRowStatus.setStatus("current")


class _RsIpRouteStaticIfIndex_Type(Integer32):
    """Custom type rsIpRouteStaticIfIndex based on Integer32"""
    defaultValue = 0


_RsIpRouteStaticIfIndex_Object = MibTableColumn
rsIpRouteStaticIfIndex = _RsIpRouteStaticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 2, 1, 6),
    _RsIpRouteStaticIfIndex_Type()
)
rsIpRouteStaticIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpRouteStaticIfIndex.setStatus("current")


class _RsIpRouteStaticStatus_Type(Integer32):
    """Custom type rsIpRouteStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1),
          ("incomplete", 2))
    )


_RsIpRouteStaticStatus_Type.__name__ = "Integer32"
_RsIpRouteStaticStatus_Object = MibTableColumn
rsIpRouteStaticStatus = _RsIpRouteStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 2, 1, 7),
    _RsIpRouteStaticStatus_Type()
)
rsIpRouteStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRouteStaticStatus.setStatus("current")


class _RsIpRouteStaticNextHopAS_Type(Integer32):
    """Custom type rsIpRouteStaticNextHopAS based on Integer32"""
    defaultValue = 0


_RsIpRouteStaticNextHopAS_Object = MibTableColumn
rsIpRouteStaticNextHopAS = _RsIpRouteStaticNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 2, 1, 8),
    _RsIpRouteStaticNextHopAS_Type()
)
rsIpRouteStaticNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpRouteStaticNextHopAS.setStatus("current")


class _RsIpRouteStaticMetric_Type(Integer32):
    """Custom type rsIpRouteStaticMetric based on Integer32"""
    defaultValue = -1


_RsIpRouteStaticMetric_Object = MibTableColumn
rsIpRouteStaticMetric = _RsIpRouteStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 2, 1, 9),
    _RsIpRouteStaticMetric_Type()
)
rsIpRouteStaticMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpRouteStaticMetric.setStatus("current")


class _RsIpRouteStaticTag_Type(Unsigned32):
    """Custom type rsIpRouteStaticTag based on Unsigned32"""
    defaultValue = 0


_RsIpRouteStaticTag_Object = MibTableColumn
rsIpRouteStaticTag = _RsIpRouteStaticTag_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 2, 1, 10),
    _RsIpRouteStaticTag_Type()
)
rsIpRouteStaticTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpRouteStaticTag.setStatus("current")
_RsIpCidrRouteTable_Object = MibTable
rsIpCidrRouteTable = _RsIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 3)
)
if mibBuilder.loadTexts:
    rsIpCidrRouteTable.setStatus("current")
_RsIpCidrRouteEntry_Object = MibTableRow
rsIpCidrRouteEntry = _RsIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    rsIpCidrRouteEntry.setStatus("current")


class _RsIpCidrRoutePref_Type(Integer32):
    """Custom type rsIpCidrRoutePref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsIpCidrRoutePref_Type.__name__ = "Integer32"
_RsIpCidrRoutePref_Object = MibTableColumn
rsIpCidrRoutePref = _RsIpCidrRoutePref_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 3, 1, 1),
    _RsIpCidrRoutePref_Type()
)
rsIpCidrRoutePref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpCidrRoutePref.setStatus("current")
_RsIpCidrRouteArea_Type = IpAddress
_RsIpCidrRouteArea_Object = MibTableColumn
rsIpCidrRouteArea = _RsIpCidrRouteArea_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 3, 1, 2),
    _RsIpCidrRouteArea_Type()
)
rsIpCidrRouteArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpCidrRouteArea.setStatus("current")
_RsIpCidrRouteTag_Type = Unsigned32
_RsIpCidrRouteTag_Object = MibTableColumn
rsIpCidrRouteTag = _RsIpCidrRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 1, 3, 3, 1, 3),
    _RsIpCidrRouteTag_Type()
)
rsIpCidrRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpCidrRouteTag.setStatus("current")
_RsIpConformance_ObjectIdentity = ObjectIdentity
rsIpConformance = _RsIpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 4)
)
_RsIpCompliances_ObjectIdentity = ObjectIdentity
rsIpCompliances = _RsIpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 4, 1)
)
_RsIpGroups_ObjectIdentity = ObjectIdentity
rsIpGroups = _RsIpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 4, 2)
)
ipCidrRouteEntry.registerAugmentions(
    ("REDSTONE-IP-MIB",
     "rsIpCidrRouteEntry")
)
rsIpCidrRouteEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())

# Managed Objects groups

rsIpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 4, 2, 1)
)
rsIpInterfaceGroup.setObjects(
      *(("REDSTONE-IP-MIB", "rsIpNextIfIndex"),
        ("REDSTONE-IP-MIB", "rsIpIfRowStatus"),
        ("REDSTONE-IP-MIB", "rsIpIfLowerIfIndex"),
        ("REDSTONE-IP-MIB", "rsIpIfType"))
)
if mibBuilder.loadTexts:
    rsIpInterfaceGroup.setStatus("current")

rsIpAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 4, 2, 2)
)
rsIpAddressGroup.setObjects(
      *(("REDSTONE-IP-MIB", "rsIpArpTimeout"),
        ("REDSTONE-IP-MIB", "rsIpAdEntRowStatus"),
        ("REDSTONE-IP-MIB", "rsIpAdEntIfIndex"),
        ("REDSTONE-IP-MIB", "rsIpAdEntNetMask"),
        ("REDSTONE-IP-MIB", "rsIpAdEntAdminStatus"),
        ("REDSTONE-IP-MIB", "rsIpAdEntArpRspEnable"),
        ("REDSTONE-IP-MIB", "rsIpAdEntProxyArpRspEnable"),
        ("REDSTONE-IP-MIB", "rsIpAdEntIgmpEnable"),
        ("REDSTONE-IP-MIB", "rsIpAdEntDirectedBcastEnable"),
        ("REDSTONE-IP-MIB", "rsIpAdEntIcmpRedirectEnable"),
        ("REDSTONE-IP-MIB", "rsIpAdEntIcmpMaskReplyEnable"),
        ("REDSTONE-IP-MIB", "rsIpAdEntIcmpUnreachEnable"),
        ("REDSTONE-IP-MIB", "rsIpAdEntMtu"),
        ("REDSTONE-IP-MIB", "rsIpAdEntUnnumLoopbackIfIndex"),
        ("REDSTONE-IP-MIB", "rsIpAdEntIrdpEnable"),
        ("REDSTONE-IP-MIB", "rsIpAdEntAccessRouteEnable"),
        ("REDSTONE-IP-MIB", "rsIpAdEntAccessRouteHost"))
)
if mibBuilder.loadTexts:
    rsIpAddressGroup.setStatus("current")

rsIpRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 4, 2, 3)
)
rsIpRouteGroup.setObjects(
      *(("REDSTONE-IP-MIB", "rsIpRouteLimit"),
        ("REDSTONE-IP-MIB", "rsIpRouteStaticDest"),
        ("REDSTONE-IP-MIB", "rsIpRouteStaticMask"),
        ("REDSTONE-IP-MIB", "rsIpRouteStaticPref"),
        ("REDSTONE-IP-MIB", "rsIpRouteStaticNextHop"),
        ("REDSTONE-IP-MIB", "rsIpRouteStaticRowStatus"),
        ("REDSTONE-IP-MIB", "rsIpRouteStaticIfIndex"),
        ("REDSTONE-IP-MIB", "rsIpRouteStaticStatus"),
        ("REDSTONE-IP-MIB", "rsIpRouteStaticNextHopAS"),
        ("REDSTONE-IP-MIB", "rsIpRouteStaticMetric"),
        ("REDSTONE-IP-MIB", "rsIpRouteStaticTag"),
        ("REDSTONE-IP-MIB", "rsIpCidrRoutePref"),
        ("REDSTONE-IP-MIB", "rsIpCidrRouteArea"),
        ("REDSTONE-IP-MIB", "rsIpCidrRouteTag"))
)
if mibBuilder.loadTexts:
    rsIpRouteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 12, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsIpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-IP-MIB",
    **{"rsIpMIB": rsIpMIB,
       "rsIpObjects": rsIpObjects,
       "rsIpInterface": rsIpInterface,
       "rsIpNextIfIndex": rsIpNextIfIndex,
       "rsIpIfTable": rsIpIfTable,
       "rsIpIfEntry": rsIpIfEntry,
       "rsIpIfIndex": rsIpIfIndex,
       "rsIpIfRowStatus": rsIpIfRowStatus,
       "rsIpIfLowerIfIndex": rsIpIfLowerIfIndex,
       "rsIpIfType": rsIpIfType,
       "rsIpAddress": rsIpAddress,
       "rsIpAddrGlobals": rsIpAddrGlobals,
       "rsIpArpTimeout": rsIpArpTimeout,
       "rsIpAddrTable": rsIpAddrTable,
       "rsIpAddrEntry": rsIpAddrEntry,
       "rsIpAdEntAddr": rsIpAdEntAddr,
       "rsIpAdEntIfIndex": rsIpAdEntIfIndex,
       "rsIpAdEntNetMask": rsIpAdEntNetMask,
       "rsIpAdEntBcastAddr": rsIpAdEntBcastAddr,
       "rsIpAdEntReasmMaxSize": rsIpAdEntReasmMaxSize,
       "rsIpAdEntRowStatus": rsIpAdEntRowStatus,
       "rsIpAdEntAdminStatus": rsIpAdEntAdminStatus,
       "rsIpAdEntArpRspEnable": rsIpAdEntArpRspEnable,
       "rsIpAdEntProxyArpRspEnable": rsIpAdEntProxyArpRspEnable,
       "rsIpAdEntIgmpEnable": rsIpAdEntIgmpEnable,
       "rsIpAdEntDirectedBcastEnable": rsIpAdEntDirectedBcastEnable,
       "rsIpAdEntIcmpRedirectEnable": rsIpAdEntIcmpRedirectEnable,
       "rsIpAdEntIcmpMaskReplyEnable": rsIpAdEntIcmpMaskReplyEnable,
       "rsIpAdEntIcmpUnreachEnable": rsIpAdEntIcmpUnreachEnable,
       "rsIpAdEntMtu": rsIpAdEntMtu,
       "rsIpAdEntUnnumLoopbackIfIndex": rsIpAdEntUnnumLoopbackIfIndex,
       "rsIpAdEntIrdpEnable": rsIpAdEntIrdpEnable,
       "rsIpAdEntAccessRouteEnable": rsIpAdEntAccessRouteEnable,
       "rsIpAdEntAccessRouteHost": rsIpAdEntAccessRouteHost,
       "rsIpRoute": rsIpRoute,
       "rsIpRouteGlobals": rsIpRouteGlobals,
       "rsIpRouteLimit": rsIpRouteLimit,
       "rsIpRouteStaticTable": rsIpRouteStaticTable,
       "rsIpRouteStaticEntry": rsIpRouteStaticEntry,
       "rsIpRouteStaticDest": rsIpRouteStaticDest,
       "rsIpRouteStaticMask": rsIpRouteStaticMask,
       "rsIpRouteStaticPref": rsIpRouteStaticPref,
       "rsIpRouteStaticNextHop": rsIpRouteStaticNextHop,
       "rsIpRouteStaticRowStatus": rsIpRouteStaticRowStatus,
       "rsIpRouteStaticIfIndex": rsIpRouteStaticIfIndex,
       "rsIpRouteStaticStatus": rsIpRouteStaticStatus,
       "rsIpRouteStaticNextHopAS": rsIpRouteStaticNextHopAS,
       "rsIpRouteStaticMetric": rsIpRouteStaticMetric,
       "rsIpRouteStaticTag": rsIpRouteStaticTag,
       "rsIpCidrRouteTable": rsIpCidrRouteTable,
       "rsIpCidrRouteEntry": rsIpCidrRouteEntry,
       "rsIpCidrRoutePref": rsIpCidrRoutePref,
       "rsIpCidrRouteArea": rsIpCidrRouteArea,
       "rsIpCidrRouteTag": rsIpCidrRouteTag,
       "rsIpConformance": rsIpConformance,
       "rsIpCompliances": rsIpCompliances,
       "rsIpCompliance": rsIpCompliance,
       "rsIpGroups": rsIpGroups,
       "rsIpInterfaceGroup": rsIpInterfaceGroup,
       "rsIpAddressGroup": rsIpAddressGroup,
       "rsIpRouteGroup": rsIpRouteGroup}
)
