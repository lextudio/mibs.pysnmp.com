# SNMP MIB module (CIENA-CES-MCAST-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-MCAST-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:59 2024
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications,
 cienaCesStatistics) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications",
    "cienaCesStatistics")

(CienaGlobalState,
 CienaMacAddress,
 CienaStatsClear) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState",
    "CienaMacAddress",
    "CienaStatsClear")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesMcastFilterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37)
)
cienaCesMcastFilterMIB.setRevisions(
        ("2016-09-30 00:00",
         "2015-03-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceType(Integer32, TextualConvention):
    status = "current"
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
        *(("mplsVc", 4),
          ("pbtsi", 2),
          ("subport", 1),
          ("vlanport", 3))
    )



class IgmpCompatibilityMode(Integer32, TextualConvention):
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
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesMcastFilterMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesMcastFilterMIBObjects = _CienaCesMcastFilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1)
)
_CienaCesMcastFilterConfig_ObjectIdentity = ObjectIdentity
cienaCesMcastFilterConfig = _CienaCesMcastFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1)
)
_CienaCesMcastGlobalAdminState_Type = CienaGlobalState
_CienaCesMcastGlobalAdminState_Object = MibScalar
cienaCesMcastGlobalAdminState = _CienaCesMcastGlobalAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 1),
    _CienaCesMcastGlobalAdminState_Type()
)
cienaCesMcastGlobalAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastGlobalAdminState.setStatus("current")
_CienaCesMcastFilterServiceTable_Object = MibTable
cienaCesMcastFilterServiceTable = _CienaCesMcastFilterServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesMcastFilterServiceTable.setStatus("current")
_CienaCesMcastFilterServiceEntry_Object = MibTableRow
cienaCesMcastFilterServiceEntry = _CienaCesMcastFilterServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 2, 1)
)
cienaCesMcastFilterServiceEntry.setIndexNames(
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMcastFilterServiceEntry.setStatus("current")


class _CienaCesMcastFilterServiceType_Type(Integer32):
    """Custom type cienaCesMcastFilterServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("vs", 2))
    )


_CienaCesMcastFilterServiceType_Type.__name__ = "Integer32"
_CienaCesMcastFilterServiceType_Object = MibTableColumn
cienaCesMcastFilterServiceType = _CienaCesMcastFilterServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 2, 1, 1),
    _CienaCesMcastFilterServiceType_Type()
)
cienaCesMcastFilterServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterServiceType.setStatus("current")
_CienaCesMcastFilterServiceIndex_Type = Unsigned32
_CienaCesMcastFilterServiceIndex_Object = MibTableColumn
cienaCesMcastFilterServiceIndex = _CienaCesMcastFilterServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 2, 1, 2),
    _CienaCesMcastFilterServiceIndex_Type()
)
cienaCesMcastFilterServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterServiceIndex.setStatus("current")
_CienaCesMcastFilterServiceAdminState_Type = CienaGlobalState
_CienaCesMcastFilterServiceAdminState_Object = MibTableColumn
cienaCesMcastFilterServiceAdminState = _CienaCesMcastFilterServiceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 2, 1, 3),
    _CienaCesMcastFilterServiceAdminState_Type()
)
cienaCesMcastFilterServiceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterServiceAdminState.setStatus("current")
_CienaCesMcastFilterServiceOperState_Type = CienaGlobalState
_CienaCesMcastFilterServiceOperState_Object = MibTableColumn
cienaCesMcastFilterServiceOperState = _CienaCesMcastFilterServiceOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 2, 1, 4),
    _CienaCesMcastFilterServiceOperState_Type()
)
cienaCesMcastFilterServiceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterServiceOperState.setStatus("current")


class _CienaCesMcastFilterServiceUMFState_Type(Integer32):
    """Custom type cienaCesMcastFilterServiceUMFState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("flood", 2))
    )


_CienaCesMcastFilterServiceUMFState_Type.__name__ = "Integer32"
_CienaCesMcastFilterServiceUMFState_Object = MibTableColumn
cienaCesMcastFilterServiceUMFState = _CienaCesMcastFilterServiceUMFState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 2, 1, 5),
    _CienaCesMcastFilterServiceUMFState_Type()
)
cienaCesMcastFilterServiceUMFState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterServiceUMFState.setStatus("current")
_CienaCesMcastFilterServerInterfaceTable_Object = MibTable
cienaCesMcastFilterServerInterfaceTable = _CienaCesMcastFilterServerInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cienaCesMcastFilterServerInterfaceTable.setStatus("current")
_CienaCesMcastFilterServerInterfaceEntry_Object = MibTableRow
cienaCesMcastFilterServerInterfaceEntry = _CienaCesMcastFilterServerInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 3, 1)
)
cienaCesMcastFilterServerInterfaceEntry.setIndexNames(
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceIndex"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServerInterfaceType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServerInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMcastFilterServerInterfaceEntry.setStatus("current")
_CienaCesMcastFilterServerInterfaceType_Type = InterfaceType
_CienaCesMcastFilterServerInterfaceType_Object = MibTableColumn
cienaCesMcastFilterServerInterfaceType = _CienaCesMcastFilterServerInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 3, 1, 1),
    _CienaCesMcastFilterServerInterfaceType_Type()
)
cienaCesMcastFilterServerInterfaceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterServerInterfaceType.setStatus("current")


class _CienaCesMcastFilterServerInterfaceIndex_Type(Integer32):
    """Custom type cienaCesMcastFilterServerInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesMcastFilterServerInterfaceIndex_Type.__name__ = "Integer32"
_CienaCesMcastFilterServerInterfaceIndex_Object = MibTableColumn
cienaCesMcastFilterServerInterfaceIndex = _CienaCesMcastFilterServerInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 3, 1, 2),
    _CienaCesMcastFilterServerInterfaceIndex_Type()
)
cienaCesMcastFilterServerInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterServerInterfaceIndex.setStatus("current")
_CienaCesMcastFilterServerInterfaceLiType_Type = InterfaceType
_CienaCesMcastFilterServerInterfaceLiType_Object = MibTableColumn
cienaCesMcastFilterServerInterfaceLiType = _CienaCesMcastFilterServerInterfaceLiType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 3, 1, 3),
    _CienaCesMcastFilterServerInterfaceLiType_Type()
)
cienaCesMcastFilterServerInterfaceLiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterServerInterfaceLiType.setStatus("current")


class _CienaCesMcastFilterServerInterfaceLiIndex_Type(Integer32):
    """Custom type cienaCesMcastFilterServerInterfaceLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesMcastFilterServerInterfaceLiIndex_Type.__name__ = "Integer32"
_CienaCesMcastFilterServerInterfaceLiIndex_Object = MibTableColumn
cienaCesMcastFilterServerInterfaceLiIndex = _CienaCesMcastFilterServerInterfaceLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 3, 1, 4),
    _CienaCesMcastFilterServerInterfaceLiIndex_Type()
)
cienaCesMcastFilterServerInterfaceLiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterServerInterfaceLiIndex.setStatus("current")
_CienaCesMcastGlobalSnoopState_Type = CienaGlobalState
_CienaCesMcastGlobalSnoopState_Object = MibScalar
cienaCesMcastGlobalSnoopState = _CienaCesMcastGlobalSnoopState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 4),
    _CienaCesMcastGlobalSnoopState_Type()
)
cienaCesMcastGlobalSnoopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastGlobalSnoopState.setStatus("current")
_CienaCesMcastIgmpSnoopTable_Object = MibTable
cienaCesMcastIgmpSnoopTable = _CienaCesMcastIgmpSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopTable.setStatus("current")
_CienaCesMcastIgmpSnoopEntry_Object = MibTableRow
cienaCesMcastIgmpSnoopEntry = _CienaCesMcastIgmpSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1)
)
cienaCesMcastIgmpSnoopEntry.setIndexNames(
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopEntry.setStatus("current")
_CienaCesMcastIgmpSnoopEnable_Type = CienaGlobalState
_CienaCesMcastIgmpSnoopEnable_Object = MibTableColumn
cienaCesMcastIgmpSnoopEnable = _CienaCesMcastIgmpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 1),
    _CienaCesMcastIgmpSnoopEnable_Type()
)
cienaCesMcastIgmpSnoopEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopEnable.setStatus("current")


class _CienaCesMcastIgmpSnoopRobustness_Type(Integer32):
    """Custom type cienaCesMcastIgmpSnoopRobustness based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CienaCesMcastIgmpSnoopRobustness_Type.__name__ = "Integer32"
_CienaCesMcastIgmpSnoopRobustness_Object = MibTableColumn
cienaCesMcastIgmpSnoopRobustness = _CienaCesMcastIgmpSnoopRobustness_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 2),
    _CienaCesMcastIgmpSnoopRobustness_Type()
)
cienaCesMcastIgmpSnoopRobustness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopRobustness.setStatus("current")


class _CienaCesMcastIgmpSnoopProxyQueryInterval_Type(Integer32):
    """Custom type cienaCesMcastIgmpSnoopProxyQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 999999),
    )


_CienaCesMcastIgmpSnoopProxyQueryInterval_Type.__name__ = "Integer32"
_CienaCesMcastIgmpSnoopProxyQueryInterval_Object = MibTableColumn
cienaCesMcastIgmpSnoopProxyQueryInterval = _CienaCesMcastIgmpSnoopProxyQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 3),
    _CienaCesMcastIgmpSnoopProxyQueryInterval_Type()
)
cienaCesMcastIgmpSnoopProxyQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopProxyQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopProxyQueryInterval.setUnits("seconds")


class _CienaCesMcastIgmpSnoopProxyQueryReplyTmo_Type(Integer32):
    """Custom type cienaCesMcastIgmpSnoopProxyQueryReplyTmo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_CienaCesMcastIgmpSnoopProxyQueryReplyTmo_Type.__name__ = "Integer32"
_CienaCesMcastIgmpSnoopProxyQueryReplyTmo_Object = MibTableColumn
cienaCesMcastIgmpSnoopProxyQueryReplyTmo = _CienaCesMcastIgmpSnoopProxyQueryReplyTmo_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 4),
    _CienaCesMcastIgmpSnoopProxyQueryReplyTmo_Type()
)
cienaCesMcastIgmpSnoopProxyQueryReplyTmo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopProxyQueryReplyTmo.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopProxyQueryReplyTmo.setUnits("seconds")


class _CienaCesMcastIgmpSnoopProxyQueryDelay_Type(Integer32):
    """Custom type cienaCesMcastIgmpSnoopProxyQueryDelay based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CienaCesMcastIgmpSnoopProxyQueryDelay_Type.__name__ = "Integer32"
_CienaCesMcastIgmpSnoopProxyQueryDelay_Object = MibTableColumn
cienaCesMcastIgmpSnoopProxyQueryDelay = _CienaCesMcastIgmpSnoopProxyQueryDelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 5),
    _CienaCesMcastIgmpSnoopProxyQueryDelay_Type()
)
cienaCesMcastIgmpSnoopProxyQueryDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopProxyQueryDelay.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopProxyQueryDelay.setUnits("seconds")


class _CienaCesMcastIgmpSnoopLingerTmo_Type(Integer32):
    """Custom type cienaCesMcastIgmpSnoopLingerTmo based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_CienaCesMcastIgmpSnoopLingerTmo_Type.__name__ = "Integer32"
_CienaCesMcastIgmpSnoopLingerTmo_Object = MibTableColumn
cienaCesMcastIgmpSnoopLingerTmo = _CienaCesMcastIgmpSnoopLingerTmo_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 6),
    _CienaCesMcastIgmpSnoopLingerTmo_Type()
)
cienaCesMcastIgmpSnoopLingerTmo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopLingerTmo.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopLingerTmo.setUnits("seconds")
_CienaCesMcastIgmpQueryEngineState_Type = CienaGlobalState
_CienaCesMcastIgmpQueryEngineState_Object = MibTableColumn
cienaCesMcastIgmpQueryEngineState = _CienaCesMcastIgmpQueryEngineState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 7),
    _CienaCesMcastIgmpQueryEngineState_Type()
)
cienaCesMcastIgmpQueryEngineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpQueryEngineState.setStatus("current")
_CienaCesMcastIgmpProxyQuerySrcIpAddrType_Type = InetAddressType
_CienaCesMcastIgmpProxyQuerySrcIpAddrType_Object = MibTableColumn
cienaCesMcastIgmpProxyQuerySrcIpAddrType = _CienaCesMcastIgmpProxyQuerySrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 8),
    _CienaCesMcastIgmpProxyQuerySrcIpAddrType_Type()
)
cienaCesMcastIgmpProxyQuerySrcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpProxyQuerySrcIpAddrType.setStatus("current")
_CienaCesMcastIgmpProxyQuerySrcIpAddr_Type = InetAddress
_CienaCesMcastIgmpProxyQuerySrcIpAddr_Object = MibTableColumn
cienaCesMcastIgmpProxyQuerySrcIpAddr = _CienaCesMcastIgmpProxyQuerySrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 9),
    _CienaCesMcastIgmpProxyQuerySrcIpAddr_Type()
)
cienaCesMcastIgmpProxyQuerySrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpProxyQuerySrcIpAddr.setStatus("current")


class _CienaCesMcastIgmpRouterQueryInterval_Type(Integer32):
    """Custom type cienaCesMcastIgmpRouterQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 999999),
    )


_CienaCesMcastIgmpRouterQueryInterval_Type.__name__ = "Integer32"
_CienaCesMcastIgmpRouterQueryInterval_Object = MibTableColumn
cienaCesMcastIgmpRouterQueryInterval = _CienaCesMcastIgmpRouterQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 10),
    _CienaCesMcastIgmpRouterQueryInterval_Type()
)
cienaCesMcastIgmpRouterQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpRouterQueryInterval.setStatus("current")


class _CienaCesMcastIgmpMinResponseTime_Type(Integer32):
    """Custom type cienaCesMcastIgmpMinResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 600),
    )


_CienaCesMcastIgmpMinResponseTime_Type.__name__ = "Integer32"
_CienaCesMcastIgmpMinResponseTime_Object = MibTableColumn
cienaCesMcastIgmpMinResponseTime = _CienaCesMcastIgmpMinResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 11),
    _CienaCesMcastIgmpMinResponseTime_Type()
)
cienaCesMcastIgmpMinResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpMinResponseTime.setStatus("current")
_CienaCesMcastIgmpDefaultRouterInterfaceType_Type = InterfaceType
_CienaCesMcastIgmpDefaultRouterInterfaceType_Object = MibTableColumn
cienaCesMcastIgmpDefaultRouterInterfaceType = _CienaCesMcastIgmpDefaultRouterInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 12),
    _CienaCesMcastIgmpDefaultRouterInterfaceType_Type()
)
cienaCesMcastIgmpDefaultRouterInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpDefaultRouterInterfaceType.setStatus("current")


class _CienaCesMcastIgmpDefaultRouterInterfaceId_Type(Integer32):
    """Custom type cienaCesMcastIgmpDefaultRouterInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesMcastIgmpDefaultRouterInterfaceId_Type.__name__ = "Integer32"
_CienaCesMcastIgmpDefaultRouterInterfaceId_Object = MibTableColumn
cienaCesMcastIgmpDefaultRouterInterfaceId = _CienaCesMcastIgmpDefaultRouterInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 13),
    _CienaCesMcastIgmpDefaultRouterInterfaceId_Type()
)
cienaCesMcastIgmpDefaultRouterInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpDefaultRouterInterfaceId.setStatus("current")
_CienaCesMcastIgmpInquisitiveLeaveState_Type = CienaGlobalState
_CienaCesMcastIgmpInquisitiveLeaveState_Object = MibTableColumn
cienaCesMcastIgmpInquisitiveLeaveState = _CienaCesMcastIgmpInquisitiveLeaveState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 14),
    _CienaCesMcastIgmpInquisitiveLeaveState_Type()
)
cienaCesMcastIgmpInquisitiveLeaveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpInquisitiveLeaveState.setStatus("current")


class _CienaCesMcastIgmpLastMemberQueryInterval_Type(Integer32):
    """Custom type cienaCesMcastIgmpLastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_CienaCesMcastIgmpLastMemberQueryInterval_Type.__name__ = "Integer32"
_CienaCesMcastIgmpLastMemberQueryInterval_Object = MibTableColumn
cienaCesMcastIgmpLastMemberQueryInterval = _CienaCesMcastIgmpLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 15),
    _CienaCesMcastIgmpLastMemberQueryInterval_Type()
)
cienaCesMcastIgmpLastMemberQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpLastMemberQueryInterval.setStatus("current")


class _CienaCesMcastIgmpPriority_Type(Integer32):
    """Custom type cienaCesMcastIgmpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMcastIgmpPriority_Type.__name__ = "Integer32"
_CienaCesMcastIgmpPriority_Object = MibTableColumn
cienaCesMcastIgmpPriority = _CienaCesMcastIgmpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 16),
    _CienaCesMcastIgmpPriority_Type()
)
cienaCesMcastIgmpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpPriority.setStatus("current")
_CienaCesMcastIgmpSnoopRouterRangeStartIpAddrType_Type = InetAddressType
_CienaCesMcastIgmpSnoopRouterRangeStartIpAddrType_Object = MibTableColumn
cienaCesMcastIgmpSnoopRouterRangeStartIpAddrType = _CienaCesMcastIgmpSnoopRouterRangeStartIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 17),
    _CienaCesMcastIgmpSnoopRouterRangeStartIpAddrType_Type()
)
cienaCesMcastIgmpSnoopRouterRangeStartIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopRouterRangeStartIpAddrType.setStatus("current")
_CienaCesMcastIgmpSnoopRouterRangeStartIpAddr_Type = InetAddress
_CienaCesMcastIgmpSnoopRouterRangeStartIpAddr_Object = MibTableColumn
cienaCesMcastIgmpSnoopRouterRangeStartIpAddr = _CienaCesMcastIgmpSnoopRouterRangeStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 18),
    _CienaCesMcastIgmpSnoopRouterRangeStartIpAddr_Type()
)
cienaCesMcastIgmpSnoopRouterRangeStartIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopRouterRangeStartIpAddr.setStatus("current")
_CienaCesMcastIgmpSnoopRouterRangeEndIpAddrType_Type = InetAddressType
_CienaCesMcastIgmpSnoopRouterRangeEndIpAddrType_Object = MibTableColumn
cienaCesMcastIgmpSnoopRouterRangeEndIpAddrType = _CienaCesMcastIgmpSnoopRouterRangeEndIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 19),
    _CienaCesMcastIgmpSnoopRouterRangeEndIpAddrType_Type()
)
cienaCesMcastIgmpSnoopRouterRangeEndIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopRouterRangeEndIpAddrType.setStatus("current")
_CienaCesMcastIgmpSnoopRouterRangeEndIpAddr_Type = InetAddress
_CienaCesMcastIgmpSnoopRouterRangeEndIpAddr_Object = MibTableColumn
cienaCesMcastIgmpSnoopRouterRangeEndIpAddr = _CienaCesMcastIgmpSnoopRouterRangeEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 20),
    _CienaCesMcastIgmpSnoopRouterRangeEndIpAddr_Type()
)
cienaCesMcastIgmpSnoopRouterRangeEndIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopRouterRangeEndIpAddr.setStatus("current")


class _CienaCesMcastIgmpSnoopActiveLingerTimeout_Type(Integer32):
    """Custom type cienaCesMcastIgmpSnoopActiveLingerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CienaCesMcastIgmpSnoopActiveLingerTimeout_Type.__name__ = "Integer32"
_CienaCesMcastIgmpSnoopActiveLingerTimeout_Object = MibTableColumn
cienaCesMcastIgmpSnoopActiveLingerTimeout = _CienaCesMcastIgmpSnoopActiveLingerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 21),
    _CienaCesMcastIgmpSnoopActiveLingerTimeout_Type()
)
cienaCesMcastIgmpSnoopActiveLingerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopActiveLingerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopActiveLingerTimeout.setUnits("seconds")


class _CienaCesMcastIgmpSnoopServerTopology_Type(Integer32):
    """Custom type cienaCesMcastIgmpSnoopServerTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("centralized", 1),
          ("distributed", 2))
    )


_CienaCesMcastIgmpSnoopServerTopology_Type.__name__ = "Integer32"
_CienaCesMcastIgmpSnoopServerTopology_Object = MibTableColumn
cienaCesMcastIgmpSnoopServerTopology = _CienaCesMcastIgmpSnoopServerTopology_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 22),
    _CienaCesMcastIgmpSnoopServerTopology_Type()
)
cienaCesMcastIgmpSnoopServerTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopServerTopology.setStatus("current")


class _CienaCesMcastIgmpSnoopRapidRecoveryMode_Type(Integer32):
    """Custom type cienaCesMcastIgmpSnoopRapidRecoveryMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesMcastIgmpSnoopRapidRecoveryMode_Type.__name__ = "Integer32"
_CienaCesMcastIgmpSnoopRapidRecoveryMode_Object = MibTableColumn
cienaCesMcastIgmpSnoopRapidRecoveryMode = _CienaCesMcastIgmpSnoopRapidRecoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 23),
    _CienaCesMcastIgmpSnoopRapidRecoveryMode_Type()
)
cienaCesMcastIgmpSnoopRapidRecoveryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopRapidRecoveryMode.setStatus("current")


class _CienaCesMcastIgmpSnoopQuerierCompatibilityMode_Type(IgmpCompatibilityMode):
    """Custom type cienaCesMcastIgmpSnoopQuerierCompatibilityMode based on IgmpCompatibilityMode"""


_CienaCesMcastIgmpSnoopQuerierCompatibilityMode_Object = MibTableColumn
cienaCesMcastIgmpSnoopQuerierCompatibilityMode = _CienaCesMcastIgmpSnoopQuerierCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 24),
    _CienaCesMcastIgmpSnoopQuerierCompatibilityMode_Type()
)
cienaCesMcastIgmpSnoopQuerierCompatibilityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopQuerierCompatibilityMode.setStatus("current")


class _CienaCesMcastIgmpSnoopForkMode_Type(Integer32):
    """Custom type cienaCesMcastIgmpSnoopForkMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesMcastIgmpSnoopForkMode_Type.__name__ = "Integer32"
_CienaCesMcastIgmpSnoopForkMode_Object = MibTableColumn
cienaCesMcastIgmpSnoopForkMode = _CienaCesMcastIgmpSnoopForkMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 25),
    _CienaCesMcastIgmpSnoopForkMode_Type()
)
cienaCesMcastIgmpSnoopForkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopForkMode.setStatus("current")
_CienaCesMcastIgmpSnoopEnableOperState_Type = CienaGlobalState
_CienaCesMcastIgmpSnoopEnableOperState_Object = MibTableColumn
cienaCesMcastIgmpSnoopEnableOperState = _CienaCesMcastIgmpSnoopEnableOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 26),
    _CienaCesMcastIgmpSnoopEnableOperState_Type()
)
cienaCesMcastIgmpSnoopEnableOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpSnoopEnableOperState.setStatus("current")
_CienaCesMcastRouterSrcMacAddr_Type = MacAddress
_CienaCesMcastRouterSrcMacAddr_Object = MibTableColumn
cienaCesMcastRouterSrcMacAddr = _CienaCesMcastRouterSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 27),
    _CienaCesMcastRouterSrcMacAddr_Type()
)
cienaCesMcastRouterSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastRouterSrcMacAddr.setStatus("current")
_CienaCesMcastRouterSrcIpAddrType_Type = InetAddressType
_CienaCesMcastRouterSrcIpAddrType_Object = MibTableColumn
cienaCesMcastRouterSrcIpAddrType = _CienaCesMcastRouterSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 28),
    _CienaCesMcastRouterSrcIpAddrType_Type()
)
cienaCesMcastRouterSrcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastRouterSrcIpAddrType.setStatus("current")
_CienaCesMcastRouterSrcIpAddr_Type = InetAddress
_CienaCesMcastRouterSrcIpAddr_Object = MibTableColumn
cienaCesMcastRouterSrcIpAddr = _CienaCesMcastRouterSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 29),
    _CienaCesMcastRouterSrcIpAddr_Type()
)
cienaCesMcastRouterSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastRouterSrcIpAddr.setStatus("current")
_CienaCesMcastRouterInterfaceType_Type = InterfaceType
_CienaCesMcastRouterInterfaceType_Object = MibTableColumn
cienaCesMcastRouterInterfaceType = _CienaCesMcastRouterInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 30),
    _CienaCesMcastRouterInterfaceType_Type()
)
cienaCesMcastRouterInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastRouterInterfaceType.setStatus("current")


class _CienaCesMcastRouterInterfaceId_Type(Integer32):
    """Custom type cienaCesMcastRouterInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesMcastRouterInterfaceId_Type.__name__ = "Integer32"
_CienaCesMcastRouterInterfaceId_Object = MibTableColumn
cienaCesMcastRouterInterfaceId = _CienaCesMcastRouterInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 31),
    _CienaCesMcastRouterInterfaceId_Type()
)
cienaCesMcastRouterInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastRouterInterfaceId.setStatus("current")
_CienaCesMcastReportSendInterfaceType_Type = InterfaceType
_CienaCesMcastReportSendInterfaceType_Object = MibTableColumn
cienaCesMcastReportSendInterfaceType = _CienaCesMcastReportSendInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 32),
    _CienaCesMcastReportSendInterfaceType_Type()
)
cienaCesMcastReportSendInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastReportSendInterfaceType.setStatus("current")


class _CienaCesMcastReportSendInterfaceId_Type(Integer32):
    """Custom type cienaCesMcastReportSendInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesMcastReportSendInterfaceId_Type.__name__ = "Integer32"
_CienaCesMcastReportSendInterfaceId_Object = MibTableColumn
cienaCesMcastReportSendInterfaceId = _CienaCesMcastReportSendInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 33),
    _CienaCesMcastReportSendInterfaceId_Type()
)
cienaCesMcastReportSendInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastReportSendInterfaceId.setStatus("current")
_CienaCesMcastRouterCompatibilityMode_Type = IgmpCompatibilityMode
_CienaCesMcastRouterCompatibilityMode_Object = MibTableColumn
cienaCesMcastRouterCompatibilityMode = _CienaCesMcastRouterCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 34),
    _CienaCesMcastRouterCompatibilityMode_Type()
)
cienaCesMcastRouterCompatibilityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastRouterCompatibilityMode.setStatus("current")


class _CienaCesMcastReportSendInterfaceIsMeshVc_Type(Integer32):
    """Custom type cienaCesMcastReportSendInterfaceIsMeshVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("undefined", 3),
          ("yes", 1))
    )


_CienaCesMcastReportSendInterfaceIsMeshVc_Type.__name__ = "Integer32"
_CienaCesMcastReportSendInterfaceIsMeshVc_Object = MibTableColumn
cienaCesMcastReportSendInterfaceIsMeshVc = _CienaCesMcastReportSendInterfaceIsMeshVc_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 35),
    _CienaCesMcastReportSendInterfaceIsMeshVc_Type()
)
cienaCesMcastReportSendInterfaceIsMeshVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastReportSendInterfaceIsMeshVc.setStatus("current")


class _CienaCesMcastIgmpQueryEngineOperState_Type(Integer32):
    """Custom type cienaCesMcastIgmpQueryEngineOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disabled", 3),
          ("inactive", 2))
    )


_CienaCesMcastIgmpQueryEngineOperState_Type.__name__ = "Integer32"
_CienaCesMcastIgmpQueryEngineOperState_Object = MibTableColumn
cienaCesMcastIgmpQueryEngineOperState = _CienaCesMcastIgmpQueryEngineOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 36),
    _CienaCesMcastIgmpQueryEngineOperState_Type()
)
cienaCesMcastIgmpQueryEngineOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastIgmpQueryEngineOperState.setStatus("current")
_CienaCesMcastRouterOlderVersionQuerierTimeRemaining_Type = Integer32
_CienaCesMcastRouterOlderVersionQuerierTimeRemaining_Object = MibTableColumn
cienaCesMcastRouterOlderVersionQuerierTimeRemaining = _CienaCesMcastRouterOlderVersionQuerierTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 37),
    _CienaCesMcastRouterOlderVersionQuerierTimeRemaining_Type()
)
cienaCesMcastRouterOlderVersionQuerierTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastRouterOlderVersionQuerierTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesMcastRouterOlderVersionQuerierTimeRemaining.setUnits("seconds")
_CienaCesMcastRouterQueryIntervalTimeRemaining_Type = Integer32
_CienaCesMcastRouterQueryIntervalTimeRemaining_Object = MibTableColumn
cienaCesMcastRouterQueryIntervalTimeRemaining = _CienaCesMcastRouterQueryIntervalTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 5, 1, 38),
    _CienaCesMcastRouterQueryIntervalTimeRemaining_Type()
)
cienaCesMcastRouterQueryIntervalTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastRouterQueryIntervalTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesMcastRouterQueryIntervalTimeRemaining.setUnits("seconds")
_CienaCesMcastChannelStreamTable_Object = MibTable
cienaCesMcastChannelStreamTable = _CienaCesMcastChannelStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cienaCesMcastChannelStreamTable.setStatus("current")
_CienaCesMcastChannelStreamEntry_Object = MibTableRow
cienaCesMcastChannelStreamEntry = _CienaCesMcastChannelStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 6, 1)
)
cienaCesMcastChannelStreamEntry.setIndexNames(
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceIndex"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastChanelStreamStartGroupAddrType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastChanelStreamStartGroupAddr"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastChanelStreamStartGroupAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    cienaCesMcastChannelStreamEntry.setStatus("current")
_CienaCesMcastChanelStreamStartGroupAddrType_Type = InetAddressType
_CienaCesMcastChanelStreamStartGroupAddrType_Object = MibTableColumn
cienaCesMcastChanelStreamStartGroupAddrType = _CienaCesMcastChanelStreamStartGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 6, 1, 1),
    _CienaCesMcastChanelStreamStartGroupAddrType_Type()
)
cienaCesMcastChanelStreamStartGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastChanelStreamStartGroupAddrType.setStatus("current")
_CienaCesMcastChanelStreamStartGroupAddr_Type = InetAddress
_CienaCesMcastChanelStreamStartGroupAddr_Object = MibTableColumn
cienaCesMcastChanelStreamStartGroupAddr = _CienaCesMcastChanelStreamStartGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 6, 1, 2),
    _CienaCesMcastChanelStreamStartGroupAddr_Type()
)
cienaCesMcastChanelStreamStartGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastChanelStreamStartGroupAddr.setStatus("current")
_CienaCesMcastChanelStreamStartGroupAddrPrefixLen_Type = InetAddressPrefixLength
_CienaCesMcastChanelStreamStartGroupAddrPrefixLen_Object = MibTableColumn
cienaCesMcastChanelStreamStartGroupAddrPrefixLen = _CienaCesMcastChanelStreamStartGroupAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 6, 1, 3),
    _CienaCesMcastChanelStreamStartGroupAddrPrefixLen_Type()
)
cienaCesMcastChanelStreamStartGroupAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastChanelStreamStartGroupAddrPrefixLen.setStatus("current")
_CienaCesMcastChanelStreamEndGroupAddrType_Type = InetAddressType
_CienaCesMcastChanelStreamEndGroupAddrType_Object = MibTableColumn
cienaCesMcastChanelStreamEndGroupAddrType = _CienaCesMcastChanelStreamEndGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 6, 1, 4),
    _CienaCesMcastChanelStreamEndGroupAddrType_Type()
)
cienaCesMcastChanelStreamEndGroupAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastChanelStreamEndGroupAddrType.setStatus("current")
_CienaCesMcastChanelStreamEndGroupAddr_Type = InetAddress
_CienaCesMcastChanelStreamEndGroupAddr_Object = MibTableColumn
cienaCesMcastChanelStreamEndGroupAddr = _CienaCesMcastChanelStreamEndGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 6, 1, 5),
    _CienaCesMcastChanelStreamEndGroupAddr_Type()
)
cienaCesMcastChanelStreamEndGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastChanelStreamEndGroupAddr.setStatus("current")
_CienaCesMcastChannelStreamExIfcMemTable_Object = MibTable
cienaCesMcastChannelStreamExIfcMemTable = _CienaCesMcastChannelStreamExIfcMemTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cienaCesMcastChannelStreamExIfcMemTable.setStatus("current")
_CienaCesMcastChannelStreamExIfcMemEntry_Object = MibTableRow
cienaCesMcastChannelStreamExIfcMemEntry = _CienaCesMcastChannelStreamExIfcMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 7, 1)
)
cienaCesMcastChannelStreamExIfcMemEntry.setIndexNames(
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceIndex"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastChannelStreamExIfcType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastChannelStreamExIfcIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMcastChannelStreamExIfcMemEntry.setStatus("current")
_CienaCesMcastChannelStreamExIfcType_Type = InterfaceType
_CienaCesMcastChannelStreamExIfcType_Object = MibTableColumn
cienaCesMcastChannelStreamExIfcType = _CienaCesMcastChannelStreamExIfcType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 7, 1, 1),
    _CienaCesMcastChannelStreamExIfcType_Type()
)
cienaCesMcastChannelStreamExIfcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastChannelStreamExIfcType.setStatus("current")


class _CienaCesMcastChannelStreamExIfcIndex_Type(Integer32):
    """Custom type cienaCesMcastChannelStreamExIfcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMcastChannelStreamExIfcIndex_Type.__name__ = "Integer32"
_CienaCesMcastChannelStreamExIfcIndex_Object = MibTableColumn
cienaCesMcastChannelStreamExIfcIndex = _CienaCesMcastChannelStreamExIfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 7, 1, 2),
    _CienaCesMcastChannelStreamExIfcIndex_Type()
)
cienaCesMcastChannelStreamExIfcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastChannelStreamExIfcIndex.setStatus("current")
_CienaCesMcastChannelStreamExIfcLiType_Type = InterfaceType
_CienaCesMcastChannelStreamExIfcLiType_Object = MibTableColumn
cienaCesMcastChannelStreamExIfcLiType = _CienaCesMcastChannelStreamExIfcLiType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 7, 1, 3),
    _CienaCesMcastChannelStreamExIfcLiType_Type()
)
cienaCesMcastChannelStreamExIfcLiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastChannelStreamExIfcLiType.setStatus("current")


class _CienaCesMcastChannelStreamExIfcLiIndex_Type(Integer32):
    """Custom type cienaCesMcastChannelStreamExIfcLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMcastChannelStreamExIfcLiIndex_Type.__name__ = "Integer32"
_CienaCesMcastChannelStreamExIfcLiIndex_Object = MibTableColumn
cienaCesMcastChannelStreamExIfcLiIndex = _CienaCesMcastChannelStreamExIfcLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 7, 1, 4),
    _CienaCesMcastChannelStreamExIfcLiIndex_Type()
)
cienaCesMcastChannelStreamExIfcLiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastChannelStreamExIfcLiIndex.setStatus("current")
_CienaCesMcastGlobalSnoopAdminState_Type = CienaGlobalState
_CienaCesMcastGlobalSnoopAdminState_Object = MibScalar
cienaCesMcastGlobalSnoopAdminState = _CienaCesMcastGlobalSnoopAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 1, 8),
    _CienaCesMcastGlobalSnoopAdminState_Type()
)
cienaCesMcastGlobalSnoopAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastGlobalSnoopAdminState.setStatus("current")
_CienaCesMcastFilterStatus_ObjectIdentity = ObjectIdentity
cienaCesMcastFilterStatus = _CienaCesMcastFilterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2)
)
_CienaCesMcastFilterGroupTable_Object = MibTable
cienaCesMcastFilterGroupTable = _CienaCesMcastFilterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupTable.setStatus("current")
_CienaCesMcastFilterGroupEntry_Object = MibTableRow
cienaCesMcastFilterGroupEntry = _CienaCesMcastFilterGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1)
)
cienaCesMcastFilterGroupEntry.setIndexNames(
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceIndex"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupAddrType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupAddr"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupEntry.setStatus("current")
_CienaCesMcastFilterGroupAddrType_Type = InetAddressType
_CienaCesMcastFilterGroupAddrType_Object = MibTableColumn
cienaCesMcastFilterGroupAddrType = _CienaCesMcastFilterGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 1),
    _CienaCesMcastFilterGroupAddrType_Type()
)
cienaCesMcastFilterGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupAddrType.setStatus("current")
_CienaCesMcastFilterGroupAddr_Type = InetAddress
_CienaCesMcastFilterGroupAddr_Object = MibTableColumn
cienaCesMcastFilterGroupAddr = _CienaCesMcastFilterGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 2),
    _CienaCesMcastFilterGroupAddr_Type()
)
cienaCesMcastFilterGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupAddr.setStatus("current")
_CienaCesMcastFilterGroupAddrPrefixLen_Type = InetAddressPrefixLength
_CienaCesMcastFilterGroupAddrPrefixLen_Object = MibTableColumn
cienaCesMcastFilterGroupAddrPrefixLen = _CienaCesMcastFilterGroupAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 3),
    _CienaCesMcastFilterGroupAddrPrefixLen_Type()
)
cienaCesMcastFilterGroupAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupAddrPrefixLen.setStatus("current")


class _CienaCesMcastFilterGroupState_Type(Integer32):
    """Custom type cienaCesMcastFilterGroupState based on Integer32"""
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
        *(("active", 1),
          ("activelinger", 3),
          ("linger", 4),
          ("query", 2))
    )


_CienaCesMcastFilterGroupState_Type.__name__ = "Integer32"
_CienaCesMcastFilterGroupState_Object = MibTableColumn
cienaCesMcastFilterGroupState = _CienaCesMcastFilterGroupState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 4),
    _CienaCesMcastFilterGroupState_Type()
)
cienaCesMcastFilterGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupState.setStatus("current")


class _CienaCesMcastFilterGroupType_Type(Integer32):
    """Custom type cienaCesMcastFilterGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CienaCesMcastFilterGroupType_Type.__name__ = "Integer32"
_CienaCesMcastFilterGroupType_Object = MibTableColumn
cienaCesMcastFilterGroupType = _CienaCesMcastFilterGroupType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 5),
    _CienaCesMcastFilterGroupType_Type()
)
cienaCesMcastFilterGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupType.setStatus("current")


class _CienaCesMcastFilterGroupSource_Type(Integer32):
    """Custom type cienaCesMcastFilterGroupSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("router", 1),
          ("server", 2))
    )


_CienaCesMcastFilterGroupSource_Type.__name__ = "Integer32"
_CienaCesMcastFilterGroupSource_Object = MibTableColumn
cienaCesMcastFilterGroupSource = _CienaCesMcastFilterGroupSource_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 6),
    _CienaCesMcastFilterGroupSource_Type()
)
cienaCesMcastFilterGroupSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupSource.setStatus("current")
_CienaCesMcastFilterGroupMemberCount_Type = Counter32
_CienaCesMcastFilterGroupMemberCount_Object = MibTableColumn
cienaCesMcastFilterGroupMemberCount = _CienaCesMcastFilterGroupMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 7),
    _CienaCesMcastFilterGroupMemberCount_Type()
)
cienaCesMcastFilterGroupMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupMemberCount.setStatus("current")
_CienaCesMcastFilterGroupCompatibilityMode_Type = IgmpCompatibilityMode
_CienaCesMcastFilterGroupCompatibilityMode_Object = MibTableColumn
cienaCesMcastFilterGroupCompatibilityMode = _CienaCesMcastFilterGroupCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 8),
    _CienaCesMcastFilterGroupCompatibilityMode_Type()
)
cienaCesMcastFilterGroupCompatibilityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupCompatibilityMode.setStatus("current")


class _CienaCesMcastFilterGroupIGMPV1HostPresentTimeRemainingValue_Type(OctetString):
    """Custom type cienaCesMcastFilterGroupIGMPV1HostPresentTimeRemainingValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CienaCesMcastFilterGroupIGMPV1HostPresentTimeRemainingValue_Type.__name__ = "OctetString"
_CienaCesMcastFilterGroupIGMPV1HostPresentTimeRemainingValue_Object = MibTableColumn
cienaCesMcastFilterGroupIGMPV1HostPresentTimeRemainingValue = _CienaCesMcastFilterGroupIGMPV1HostPresentTimeRemainingValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 9),
    _CienaCesMcastFilterGroupIGMPV1HostPresentTimeRemainingValue_Type()
)
cienaCesMcastFilterGroupIGMPV1HostPresentTimeRemainingValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupIGMPV1HostPresentTimeRemainingValue.setStatus("current")


class _CienaCesMcastFilterGroupIGMPV2HostPresentTimeRemainingValue_Type(OctetString):
    """Custom type cienaCesMcastFilterGroupIGMPV2HostPresentTimeRemainingValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CienaCesMcastFilterGroupIGMPV2HostPresentTimeRemainingValue_Type.__name__ = "OctetString"
_CienaCesMcastFilterGroupIGMPV2HostPresentTimeRemainingValue_Object = MibTableColumn
cienaCesMcastFilterGroupIGMPV2HostPresentTimeRemainingValue = _CienaCesMcastFilterGroupIGMPV2HostPresentTimeRemainingValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 10),
    _CienaCesMcastFilterGroupIGMPV2HostPresentTimeRemainingValue_Type()
)
cienaCesMcastFilterGroupIGMPV2HostPresentTimeRemainingValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupIGMPV2HostPresentTimeRemainingValue.setStatus("current")


class _CienaCesMcastFilterGroupFilterMode_Type(Integer32):
    """Custom type cienaCesMcastFilterGroupFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ex", 2),
          ("in", 1))
    )


_CienaCesMcastFilterGroupFilterMode_Type.__name__ = "Integer32"
_CienaCesMcastFilterGroupFilterMode_Object = MibTableColumn
cienaCesMcastFilterGroupFilterMode = _CienaCesMcastFilterGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 11),
    _CienaCesMcastFilterGroupFilterMode_Type()
)
cienaCesMcastFilterGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupFilterMode.setStatus("current")
_CienaCesMcastFilterGroupNumOfSrcAddrs_Type = Integer32
_CienaCesMcastFilterGroupNumOfSrcAddrs_Object = MibTableColumn
cienaCesMcastFilterGroupNumOfSrcAddrs = _CienaCesMcastFilterGroupNumOfSrcAddrs_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 12),
    _CienaCesMcastFilterGroupNumOfSrcAddrs_Type()
)
cienaCesMcastFilterGroupNumOfSrcAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupNumOfSrcAddrs.setStatus("current")


class _CienaCesMcastFilterGroupTimer_Type(OctetString):
    """Custom type cienaCesMcastFilterGroupTimer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CienaCesMcastFilterGroupTimer_Type.__name__ = "OctetString"
_CienaCesMcastFilterGroupTimer_Object = MibTableColumn
cienaCesMcastFilterGroupTimer = _CienaCesMcastFilterGroupTimer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 1, 1, 13),
    _CienaCesMcastFilterGroupTimer_Type()
)
cienaCesMcastFilterGroupTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupTimer.setStatus("current")
_CienaCesMcastFilterGroupSrcRecordTable_Object = MibTable
cienaCesMcastFilterGroupSrcRecordTable = _CienaCesMcastFilterGroupSrcRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupSrcRecordTable.setStatus("current")
_CienaCesMcastFilterGroupSrcRecordEntry_Object = MibTableRow
cienaCesMcastFilterGroupSrcRecordEntry = _CienaCesMcastFilterGroupSrcRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 2, 1)
)
cienaCesMcastFilterGroupSrcRecordEntry.setIndexNames(
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceIndex"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupAddrType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupAddr"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupAddrPrefixLen"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupSrcRecordSrcIpAddrType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupSrcRecordSrcIp"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupSrcRecordSrcIpAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupSrcRecordEntry.setStatus("current")
_CienaCesMcastFilterGroupSrcRecordSrcIpAddrType_Type = InetAddressType
_CienaCesMcastFilterGroupSrcRecordSrcIpAddrType_Object = MibTableColumn
cienaCesMcastFilterGroupSrcRecordSrcIpAddrType = _CienaCesMcastFilterGroupSrcRecordSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 2, 1, 1),
    _CienaCesMcastFilterGroupSrcRecordSrcIpAddrType_Type()
)
cienaCesMcastFilterGroupSrcRecordSrcIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupSrcRecordSrcIpAddrType.setStatus("current")
_CienaCesMcastFilterGroupSrcRecordSrcIp_Type = InetAddress
_CienaCesMcastFilterGroupSrcRecordSrcIp_Object = MibTableColumn
cienaCesMcastFilterGroupSrcRecordSrcIp = _CienaCesMcastFilterGroupSrcRecordSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 2, 1, 2),
    _CienaCesMcastFilterGroupSrcRecordSrcIp_Type()
)
cienaCesMcastFilterGroupSrcRecordSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupSrcRecordSrcIp.setStatus("current")
_CienaCesMcastFilterGroupSrcRecordSrcIpAddrPrefixLen_Type = InetAddressPrefixLength
_CienaCesMcastFilterGroupSrcRecordSrcIpAddrPrefixLen_Object = MibTableColumn
cienaCesMcastFilterGroupSrcRecordSrcIpAddrPrefixLen = _CienaCesMcastFilterGroupSrcRecordSrcIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 2, 1, 3),
    _CienaCesMcastFilterGroupSrcRecordSrcIpAddrPrefixLen_Type()
)
cienaCesMcastFilterGroupSrcRecordSrcIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupSrcRecordSrcIpAddrPrefixLen.setStatus("current")
_CienaCesMcastFilterGroupSrcRecordSrcIpAddress_Type = InetAddress
_CienaCesMcastFilterGroupSrcRecordSrcIpAddress_Object = MibTableColumn
cienaCesMcastFilterGroupSrcRecordSrcIpAddress = _CienaCesMcastFilterGroupSrcRecordSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 2, 1, 4),
    _CienaCesMcastFilterGroupSrcRecordSrcIpAddress_Type()
)
cienaCesMcastFilterGroupSrcRecordSrcIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupSrcRecordSrcIpAddress.setStatus("current")


class _CienaCesMcastFilterGroupSrcRecordSrcTimer_Type(OctetString):
    """Custom type cienaCesMcastFilterGroupSrcRecordSrcTimer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CienaCesMcastFilterGroupSrcRecordSrcTimer_Type.__name__ = "OctetString"
_CienaCesMcastFilterGroupSrcRecordSrcTimer_Object = MibTableColumn
cienaCesMcastFilterGroupSrcRecordSrcTimer = _CienaCesMcastFilterGroupSrcRecordSrcTimer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 2, 1, 5),
    _CienaCesMcastFilterGroupSrcRecordSrcTimer_Type()
)
cienaCesMcastFilterGroupSrcRecordSrcTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupSrcRecordSrcTimer.setStatus("current")
_CienaCesMcastFilterGroupMemberTable_Object = MibTable
cienaCesMcastFilterGroupMemberTable = _CienaCesMcastFilterGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupMemberTable.setStatus("current")
_CienaCesMcastFilterGroupMemberEntry_Object = MibTableRow
cienaCesMcastFilterGroupMemberEntry = _CienaCesMcastFilterGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 3, 1)
)
cienaCesMcastFilterGroupMemberEntry.setIndexNames(
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceIndex"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupAddrType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupAddr"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupAddrPrefixLen"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupMemberInterfaceType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterGroupMemberInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupMemberEntry.setStatus("current")
_CienaCesMcastFilterGroupMemberInterfaceType_Type = InterfaceType
_CienaCesMcastFilterGroupMemberInterfaceType_Object = MibTableColumn
cienaCesMcastFilterGroupMemberInterfaceType = _CienaCesMcastFilterGroupMemberInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 3, 1, 1),
    _CienaCesMcastFilterGroupMemberInterfaceType_Type()
)
cienaCesMcastFilterGroupMemberInterfaceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupMemberInterfaceType.setStatus("current")


class _CienaCesMcastFilterGroupMemberInterfaceIndex_Type(Integer32):
    """Custom type cienaCesMcastFilterGroupMemberInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMcastFilterGroupMemberInterfaceIndex_Type.__name__ = "Integer32"
_CienaCesMcastFilterGroupMemberInterfaceIndex_Object = MibTableColumn
cienaCesMcastFilterGroupMemberInterfaceIndex = _CienaCesMcastFilterGroupMemberInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 3, 1, 2),
    _CienaCesMcastFilterGroupMemberInterfaceIndex_Type()
)
cienaCesMcastFilterGroupMemberInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupMemberInterfaceIndex.setStatus("current")
_CienaCesMcastFilterGroupMemberInterfaceLiType_Type = InterfaceType
_CienaCesMcastFilterGroupMemberInterfaceLiType_Object = MibTableColumn
cienaCesMcastFilterGroupMemberInterfaceLiType = _CienaCesMcastFilterGroupMemberInterfaceLiType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 3, 1, 3),
    _CienaCesMcastFilterGroupMemberInterfaceLiType_Type()
)
cienaCesMcastFilterGroupMemberInterfaceLiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupMemberInterfaceLiType.setStatus("current")


class _CienaCesMcastFilterGroupMemberInterfaceLiIndex_Type(Integer32):
    """Custom type cienaCesMcastFilterGroupMemberInterfaceLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMcastFilterGroupMemberInterfaceLiIndex_Type.__name__ = "Integer32"
_CienaCesMcastFilterGroupMemberInterfaceLiIndex_Object = MibTableColumn
cienaCesMcastFilterGroupMemberInterfaceLiIndex = _CienaCesMcastFilterGroupMemberInterfaceLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 2, 3, 1, 4),
    _CienaCesMcastFilterGroupMemberInterfaceLiIndex_Type()
)
cienaCesMcastFilterGroupMemberInterfaceLiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastFilterGroupMemberInterfaceLiIndex.setStatus("current")
_CienaCesMcastGlobalResources_ObjectIdentity = ObjectIdentity
cienaCesMcastGlobalResources = _CienaCesMcastGlobalResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3)
)
_CienaCesMcastMaxServiceInstances_Type = Unsigned32
_CienaCesMcastMaxServiceInstances_Object = MibScalar
cienaCesMcastMaxServiceInstances = _CienaCesMcastMaxServiceInstances_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3, 1),
    _CienaCesMcastMaxServiceInstances_Type()
)
cienaCesMcastMaxServiceInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastMaxServiceInstances.setStatus("current")
_CienaCesMcastCurrentServiceInstances_Type = Unsigned32
_CienaCesMcastCurrentServiceInstances_Object = MibScalar
cienaCesMcastCurrentServiceInstances = _CienaCesMcastCurrentServiceInstances_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3, 2),
    _CienaCesMcastCurrentServiceInstances_Type()
)
cienaCesMcastCurrentServiceInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastCurrentServiceInstances.setStatus("current")
_CienaCesMcastMaxMcastGroups_Type = Unsigned32
_CienaCesMcastMaxMcastGroups_Object = MibScalar
cienaCesMcastMaxMcastGroups = _CienaCesMcastMaxMcastGroups_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3, 3),
    _CienaCesMcastMaxMcastGroups_Type()
)
cienaCesMcastMaxMcastGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastMaxMcastGroups.setStatus("current")
_CienaCesMcastCurrentMcastGroups_Type = Unsigned32
_CienaCesMcastCurrentMcastGroups_Object = MibScalar
cienaCesMcastCurrentMcastGroups = _CienaCesMcastCurrentMcastGroups_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3, 4),
    _CienaCesMcastCurrentMcastGroups_Type()
)
cienaCesMcastCurrentMcastGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastCurrentMcastGroups.setStatus("current")
_CienaCesMcastMaxSrcAddrRecords_Type = Unsigned32
_CienaCesMcastMaxSrcAddrRecords_Object = MibScalar
cienaCesMcastMaxSrcAddrRecords = _CienaCesMcastMaxSrcAddrRecords_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3, 5),
    _CienaCesMcastMaxSrcAddrRecords_Type()
)
cienaCesMcastMaxSrcAddrRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastMaxSrcAddrRecords.setStatus("current")
_CienaCesMcastCurrentSrcAddrRecords_Type = Unsigned32
_CienaCesMcastCurrentSrcAddrRecords_Object = MibScalar
cienaCesMcastCurrentSrcAddrRecords = _CienaCesMcastCurrentSrcAddrRecords_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3, 6),
    _CienaCesMcastCurrentSrcAddrRecords_Type()
)
cienaCesMcastCurrentSrcAddrRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastCurrentSrcAddrRecords.setStatus("current")
_CienaCesMcastMaxTimers_Type = Unsigned32
_CienaCesMcastMaxTimers_Object = MibScalar
cienaCesMcastMaxTimers = _CienaCesMcastMaxTimers_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3, 7),
    _CienaCesMcastMaxTimers_Type()
)
cienaCesMcastMaxTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastMaxTimers.setStatus("current")
_CienaCesMcastCurrentTimers_Type = Unsigned32
_CienaCesMcastCurrentTimers_Object = MibScalar
cienaCesMcastCurrentTimers = _CienaCesMcastCurrentTimers_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3, 8),
    _CienaCesMcastCurrentTimers_Type()
)
cienaCesMcastCurrentTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastCurrentTimers.setStatus("current")
_CienaCesMcastMaxLogicalInterfaces_Type = Unsigned32
_CienaCesMcastMaxLogicalInterfaces_Object = MibScalar
cienaCesMcastMaxLogicalInterfaces = _CienaCesMcastMaxLogicalInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3, 9),
    _CienaCesMcastMaxLogicalInterfaces_Type()
)
cienaCesMcastMaxLogicalInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastMaxLogicalInterfaces.setStatus("current")
_CienaCesMcastCurrentLogicalInterfaces_Type = Unsigned32
_CienaCesMcastCurrentLogicalInterfaces_Object = MibScalar
cienaCesMcastCurrentLogicalInterfaces = _CienaCesMcastCurrentLogicalInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3, 10),
    _CienaCesMcastCurrentLogicalInterfaces_Type()
)
cienaCesMcastCurrentLogicalInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastCurrentLogicalInterfaces.setStatus("current")
_CienaCesMcastMaxGrpMemberInterfaces_Type = Unsigned32
_CienaCesMcastMaxGrpMemberInterfaces_Object = MibScalar
cienaCesMcastMaxGrpMemberInterfaces = _CienaCesMcastMaxGrpMemberInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3, 11),
    _CienaCesMcastMaxGrpMemberInterfaces_Type()
)
cienaCesMcastMaxGrpMemberInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastMaxGrpMemberInterfaces.setStatus("current")
_CienaCesMcastCurrentGrpMemberInterfaces_Type = Unsigned32
_CienaCesMcastCurrentGrpMemberInterfaces_Object = MibScalar
cienaCesMcastCurrentGrpMemberInterfaces = _CienaCesMcastCurrentGrpMemberInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 37, 1, 3, 12),
    _CienaCesMcastCurrentGrpMemberInterfaces_Type()
)
cienaCesMcastCurrentGrpMemberInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastCurrentGrpMemberInterfaces.setStatus("current")
_CienaCesMcastFilterMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesMcastFilterMIBNotificationPrefix = _CienaCesMcastFilterMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 100)
)
_CienaCesMcastFilterMIBNotification_ObjectIdentity = ObjectIdentity
cienaCesMcastFilterMIBNotification = _CienaCesMcastFilterMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 100, 0)
)
_CienaCesMcastFilterStats_ObjectIdentity = ObjectIdentity
cienaCesMcastFilterStats = _CienaCesMcastFilterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8)
)
_CienaCesMcastFilterStatsTable_Object = MibTable
cienaCesMcastFilterStatsTable = _CienaCesMcastFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1)
)
if mibBuilder.loadTexts:
    cienaCesMcastFilterStatsTable.setStatus("current")
_CienaCesMcastFilterStatsEntry_Object = MibTableRow
cienaCesMcastFilterStatsEntry = _CienaCesMcastFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1)
)
cienaCesMcastFilterStatsEntry.setIndexNames(
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceType"),
    (0, "CIENA-CES-MCAST-FILTER-MIB", "cienaCesMcastFilterServiceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMcastFilterStatsEntry.setStatus("current")


class _CienaCesMcastStaticGrpCount_Type(Integer32):
    """Custom type cienaCesMcastStaticGrpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesMcastStaticGrpCount_Type.__name__ = "Integer32"
_CienaCesMcastStaticGrpCount_Object = MibTableColumn
cienaCesMcastStaticGrpCount = _CienaCesMcastStaticGrpCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 1),
    _CienaCesMcastStaticGrpCount_Type()
)
cienaCesMcastStaticGrpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastStaticGrpCount.setStatus("current")


class _CienaCesMcastDynamicGrpCount_Type(Integer32):
    """Custom type cienaCesMcastDynamicGrpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesMcastDynamicGrpCount_Type.__name__ = "Integer32"
_CienaCesMcastDynamicGrpCount_Object = MibTableColumn
cienaCesMcastDynamicGrpCount = _CienaCesMcastDynamicGrpCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 2),
    _CienaCesMcastDynamicGrpCount_Type()
)
cienaCesMcastDynamicGrpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastDynamicGrpCount.setStatus("current")
_CienaCesMcastJoinMessagesRx_Type = Counter32
_CienaCesMcastJoinMessagesRx_Object = MibTableColumn
cienaCesMcastJoinMessagesRx = _CienaCesMcastJoinMessagesRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 3),
    _CienaCesMcastJoinMessagesRx_Type()
)
cienaCesMcastJoinMessagesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastJoinMessagesRx.setStatus("current")
_CienaCesMcastLeaveMessagesRx_Type = Counter32
_CienaCesMcastLeaveMessagesRx_Object = MibTableColumn
cienaCesMcastLeaveMessagesRx = _CienaCesMcastLeaveMessagesRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 4),
    _CienaCesMcastLeaveMessagesRx_Type()
)
cienaCesMcastLeaveMessagesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastLeaveMessagesRx.setStatus("current")
_CienaCesMcastV3ReportsRx_Type = Counter32
_CienaCesMcastV3ReportsRx_Object = MibTableColumn
cienaCesMcastV3ReportsRx = _CienaCesMcastV3ReportsRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 5),
    _CienaCesMcastV3ReportsRx_Type()
)
cienaCesMcastV3ReportsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastV3ReportsRx.setStatus("current")
_CienaCesMcastQueryMessagesRx_Type = Counter32
_CienaCesMcastQueryMessagesRx_Object = MibTableColumn
cienaCesMcastQueryMessagesRx = _CienaCesMcastQueryMessagesRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 6),
    _CienaCesMcastQueryMessagesRx_Type()
)
cienaCesMcastQueryMessagesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastQueryMessagesRx.setStatus("current")
_CienaCesMcastQueryRxDiscards_Type = Counter32
_CienaCesMcastQueryRxDiscards_Object = MibTableColumn
cienaCesMcastQueryRxDiscards = _CienaCesMcastQueryRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 7),
    _CienaCesMcastQueryRxDiscards_Type()
)
cienaCesMcastQueryRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastQueryRxDiscards.setStatus("current")
_CienaCesMcastQueryTimeouts_Type = Counter32
_CienaCesMcastQueryTimeouts_Object = MibTableColumn
cienaCesMcastQueryTimeouts = _CienaCesMcastQueryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 8),
    _CienaCesMcastQueryTimeouts_Type()
)
cienaCesMcastQueryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastQueryTimeouts.setStatus("current")
_CienaCesMcastUnknownPktTypeRx_Type = Counter32
_CienaCesMcastUnknownPktTypeRx_Object = MibTableColumn
cienaCesMcastUnknownPktTypeRx = _CienaCesMcastUnknownPktTypeRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 9),
    _CienaCesMcastUnknownPktTypeRx_Type()
)
cienaCesMcastUnknownPktTypeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastUnknownPktTypeRx.setStatus("current")
_CienaCesMcastRouterRxDiscards_Type = Counter32
_CienaCesMcastRouterRxDiscards_Object = MibTableColumn
cienaCesMcastRouterRxDiscards = _CienaCesMcastRouterRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 10),
    _CienaCesMcastRouterRxDiscards_Type()
)
cienaCesMcastRouterRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastRouterRxDiscards.setStatus("current")
_CienaCesMcastHostRxDiscards_Type = Counter32
_CienaCesMcastHostRxDiscards_Object = MibTableColumn
cienaCesMcastHostRxDiscards = _CienaCesMcastHostRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 11),
    _CienaCesMcastHostRxDiscards_Type()
)
cienaCesMcastHostRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastHostRxDiscards.setStatus("current")
_CienaCesMcastBadChecksumRx_Type = Counter32
_CienaCesMcastBadChecksumRx_Object = MibTableColumn
cienaCesMcastBadChecksumRx = _CienaCesMcastBadChecksumRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 12),
    _CienaCesMcastBadChecksumRx_Type()
)
cienaCesMcastBadChecksumRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastBadChecksumRx.setStatus("current")
_CienaCesMcastL2L3MismatchRx_Type = Counter32
_CienaCesMcastL2L3MismatchRx_Object = MibTableColumn
cienaCesMcastL2L3MismatchRx = _CienaCesMcastL2L3MismatchRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 13),
    _CienaCesMcastL2L3MismatchRx_Type()
)
cienaCesMcastL2L3MismatchRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastL2L3MismatchRx.setStatus("current")
_CienaCesMcastTotalMembers_Type = Counter32
_CienaCesMcastTotalMembers_Object = MibTableColumn
cienaCesMcastTotalMembers = _CienaCesMcastTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 14),
    _CienaCesMcastTotalMembers_Type()
)
cienaCesMcastTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastTotalMembers.setStatus("current")
_CienaCesMcastLingerCount_Type = Counter32
_CienaCesMcastLingerCount_Object = MibTableColumn
cienaCesMcastLingerCount = _CienaCesMcastLingerCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 15),
    _CienaCesMcastLingerCount_Type()
)
cienaCesMcastLingerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastLingerCount.setStatus("current")
_CienaCesMcastStatsQuerySrcIpZeroDiscard_Type = Counter32
_CienaCesMcastStatsQuerySrcIpZeroDiscard_Object = MibTableColumn
cienaCesMcastStatsQuerySrcIpZeroDiscard = _CienaCesMcastStatsQuerySrcIpZeroDiscard_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 16),
    _CienaCesMcastStatsQuerySrcIpZeroDiscard_Type()
)
cienaCesMcastStatsQuerySrcIpZeroDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastStatsQuerySrcIpZeroDiscard.setStatus("current")
_CienaCesMcastCompatibilityModeDiscards_Type = Counter32
_CienaCesMcastCompatibilityModeDiscards_Object = MibTableColumn
cienaCesMcastCompatibilityModeDiscards = _CienaCesMcastCompatibilityModeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 17),
    _CienaCesMcastCompatibilityModeDiscards_Type()
)
cienaCesMcastCompatibilityModeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastCompatibilityModeDiscards.setStatus("current")
_CienaCesMcastReplyTimeouts_Type = Counter32
_CienaCesMcastReplyTimeouts_Object = MibTableColumn
cienaCesMcastReplyTimeouts = _CienaCesMcastReplyTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 18),
    _CienaCesMcastReplyTimeouts_Type()
)
cienaCesMcastReplyTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastReplyTimeouts.setStatus("current")
_CienaCesMcastResourceExceed_Type = Counter32
_CienaCesMcastResourceExceed_Object = MibTableColumn
cienaCesMcastResourceExceed = _CienaCesMcastResourceExceed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 19),
    _CienaCesMcastResourceExceed_Type()
)
cienaCesMcastResourceExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastResourceExceed.setStatus("current")
_CienaCesMcastV3ReportsRxIsIn_Type = Counter32
_CienaCesMcastV3ReportsRxIsIn_Object = MibTableColumn
cienaCesMcastV3ReportsRxIsIn = _CienaCesMcastV3ReportsRxIsIn_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 20),
    _CienaCesMcastV3ReportsRxIsIn_Type()
)
cienaCesMcastV3ReportsRxIsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastV3ReportsRxIsIn.setStatus("current")
_CienaCesMcastV3ReportsRxIsEx_Type = Counter32
_CienaCesMcastV3ReportsRxIsEx_Object = MibTableColumn
cienaCesMcastV3ReportsRxIsEx = _CienaCesMcastV3ReportsRxIsEx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 21),
    _CienaCesMcastV3ReportsRxIsEx_Type()
)
cienaCesMcastV3ReportsRxIsEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastV3ReportsRxIsEx.setStatus("current")
_CienaCesMcastV3ReportsRxToIn_Type = Counter32
_CienaCesMcastV3ReportsRxToIn_Object = MibTableColumn
cienaCesMcastV3ReportsRxToIn = _CienaCesMcastV3ReportsRxToIn_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 22),
    _CienaCesMcastV3ReportsRxToIn_Type()
)
cienaCesMcastV3ReportsRxToIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastV3ReportsRxToIn.setStatus("current")
_CienaCesMcastV3ReportsRxToEx_Type = Counter32
_CienaCesMcastV3ReportsRxToEx_Object = MibTableColumn
cienaCesMcastV3ReportsRxToEx = _CienaCesMcastV3ReportsRxToEx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 23),
    _CienaCesMcastV3ReportsRxToEx_Type()
)
cienaCesMcastV3ReportsRxToEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastV3ReportsRxToEx.setStatus("current")
_CienaCesMcastV3ReportsRxAllow_Type = Counter32
_CienaCesMcastV3ReportsRxAllow_Object = MibTableColumn
cienaCesMcastV3ReportsRxAllow = _CienaCesMcastV3ReportsRxAllow_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 24),
    _CienaCesMcastV3ReportsRxAllow_Type()
)
cienaCesMcastV3ReportsRxAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastV3ReportsRxAllow.setStatus("current")
_CienaCesMcastV3ReportsRxBlock_Type = Counter32
_CienaCesMcastV3ReportsRxBlock_Object = MibTableColumn
cienaCesMcastV3ReportsRxBlock = _CienaCesMcastV3ReportsRxBlock_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 8, 1, 1, 25),
    _CienaCesMcastV3ReportsRxBlock_Type()
)
cienaCesMcastV3ReportsRxBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMcastV3ReportsRxBlock.setStatus("current")

# Managed Objects groups


# Notification objects

cienaCesMcastAddrOverlapNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 100, 0, 1)
)
cienaCesMcastAddrOverlapNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"))
)
if mibBuilder.loadTexts:
    cienaCesMcastAddrOverlapNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-MCAST-FILTER-MIB",
    **{"InterfaceType": InterfaceType,
       "IgmpCompatibilityMode": IgmpCompatibilityMode,
       "cienaCesMcastFilterMIB": cienaCesMcastFilterMIB,
       "cienaCesMcastFilterMIBObjects": cienaCesMcastFilterMIBObjects,
       "cienaCesMcastFilterConfig": cienaCesMcastFilterConfig,
       "cienaCesMcastGlobalAdminState": cienaCesMcastGlobalAdminState,
       "cienaCesMcastFilterServiceTable": cienaCesMcastFilterServiceTable,
       "cienaCesMcastFilterServiceEntry": cienaCesMcastFilterServiceEntry,
       "cienaCesMcastFilterServiceType": cienaCesMcastFilterServiceType,
       "cienaCesMcastFilterServiceIndex": cienaCesMcastFilterServiceIndex,
       "cienaCesMcastFilterServiceAdminState": cienaCesMcastFilterServiceAdminState,
       "cienaCesMcastFilterServiceOperState": cienaCesMcastFilterServiceOperState,
       "cienaCesMcastFilterServiceUMFState": cienaCesMcastFilterServiceUMFState,
       "cienaCesMcastFilterServerInterfaceTable": cienaCesMcastFilterServerInterfaceTable,
       "cienaCesMcastFilterServerInterfaceEntry": cienaCesMcastFilterServerInterfaceEntry,
       "cienaCesMcastFilterServerInterfaceType": cienaCesMcastFilterServerInterfaceType,
       "cienaCesMcastFilterServerInterfaceIndex": cienaCesMcastFilterServerInterfaceIndex,
       "cienaCesMcastFilterServerInterfaceLiType": cienaCesMcastFilterServerInterfaceLiType,
       "cienaCesMcastFilterServerInterfaceLiIndex": cienaCesMcastFilterServerInterfaceLiIndex,
       "cienaCesMcastGlobalSnoopState": cienaCesMcastGlobalSnoopState,
       "cienaCesMcastIgmpSnoopTable": cienaCesMcastIgmpSnoopTable,
       "cienaCesMcastIgmpSnoopEntry": cienaCesMcastIgmpSnoopEntry,
       "cienaCesMcastIgmpSnoopEnable": cienaCesMcastIgmpSnoopEnable,
       "cienaCesMcastIgmpSnoopRobustness": cienaCesMcastIgmpSnoopRobustness,
       "cienaCesMcastIgmpSnoopProxyQueryInterval": cienaCesMcastIgmpSnoopProxyQueryInterval,
       "cienaCesMcastIgmpSnoopProxyQueryReplyTmo": cienaCesMcastIgmpSnoopProxyQueryReplyTmo,
       "cienaCesMcastIgmpSnoopProxyQueryDelay": cienaCesMcastIgmpSnoopProxyQueryDelay,
       "cienaCesMcastIgmpSnoopLingerTmo": cienaCesMcastIgmpSnoopLingerTmo,
       "cienaCesMcastIgmpQueryEngineState": cienaCesMcastIgmpQueryEngineState,
       "cienaCesMcastIgmpProxyQuerySrcIpAddrType": cienaCesMcastIgmpProxyQuerySrcIpAddrType,
       "cienaCesMcastIgmpProxyQuerySrcIpAddr": cienaCesMcastIgmpProxyQuerySrcIpAddr,
       "cienaCesMcastIgmpRouterQueryInterval": cienaCesMcastIgmpRouterQueryInterval,
       "cienaCesMcastIgmpMinResponseTime": cienaCesMcastIgmpMinResponseTime,
       "cienaCesMcastIgmpDefaultRouterInterfaceType": cienaCesMcastIgmpDefaultRouterInterfaceType,
       "cienaCesMcastIgmpDefaultRouterInterfaceId": cienaCesMcastIgmpDefaultRouterInterfaceId,
       "cienaCesMcastIgmpInquisitiveLeaveState": cienaCesMcastIgmpInquisitiveLeaveState,
       "cienaCesMcastIgmpLastMemberQueryInterval": cienaCesMcastIgmpLastMemberQueryInterval,
       "cienaCesMcastIgmpPriority": cienaCesMcastIgmpPriority,
       "cienaCesMcastIgmpSnoopRouterRangeStartIpAddrType": cienaCesMcastIgmpSnoopRouterRangeStartIpAddrType,
       "cienaCesMcastIgmpSnoopRouterRangeStartIpAddr": cienaCesMcastIgmpSnoopRouterRangeStartIpAddr,
       "cienaCesMcastIgmpSnoopRouterRangeEndIpAddrType": cienaCesMcastIgmpSnoopRouterRangeEndIpAddrType,
       "cienaCesMcastIgmpSnoopRouterRangeEndIpAddr": cienaCesMcastIgmpSnoopRouterRangeEndIpAddr,
       "cienaCesMcastIgmpSnoopActiveLingerTimeout": cienaCesMcastIgmpSnoopActiveLingerTimeout,
       "cienaCesMcastIgmpSnoopServerTopology": cienaCesMcastIgmpSnoopServerTopology,
       "cienaCesMcastIgmpSnoopRapidRecoveryMode": cienaCesMcastIgmpSnoopRapidRecoveryMode,
       "cienaCesMcastIgmpSnoopQuerierCompatibilityMode": cienaCesMcastIgmpSnoopQuerierCompatibilityMode,
       "cienaCesMcastIgmpSnoopForkMode": cienaCesMcastIgmpSnoopForkMode,
       "cienaCesMcastIgmpSnoopEnableOperState": cienaCesMcastIgmpSnoopEnableOperState,
       "cienaCesMcastRouterSrcMacAddr": cienaCesMcastRouterSrcMacAddr,
       "cienaCesMcastRouterSrcIpAddrType": cienaCesMcastRouterSrcIpAddrType,
       "cienaCesMcastRouterSrcIpAddr": cienaCesMcastRouterSrcIpAddr,
       "cienaCesMcastRouterInterfaceType": cienaCesMcastRouterInterfaceType,
       "cienaCesMcastRouterInterfaceId": cienaCesMcastRouterInterfaceId,
       "cienaCesMcastReportSendInterfaceType": cienaCesMcastReportSendInterfaceType,
       "cienaCesMcastReportSendInterfaceId": cienaCesMcastReportSendInterfaceId,
       "cienaCesMcastRouterCompatibilityMode": cienaCesMcastRouterCompatibilityMode,
       "cienaCesMcastReportSendInterfaceIsMeshVc": cienaCesMcastReportSendInterfaceIsMeshVc,
       "cienaCesMcastIgmpQueryEngineOperState": cienaCesMcastIgmpQueryEngineOperState,
       "cienaCesMcastRouterOlderVersionQuerierTimeRemaining": cienaCesMcastRouterOlderVersionQuerierTimeRemaining,
       "cienaCesMcastRouterQueryIntervalTimeRemaining": cienaCesMcastRouterQueryIntervalTimeRemaining,
       "cienaCesMcastChannelStreamTable": cienaCesMcastChannelStreamTable,
       "cienaCesMcastChannelStreamEntry": cienaCesMcastChannelStreamEntry,
       "cienaCesMcastChanelStreamStartGroupAddrType": cienaCesMcastChanelStreamStartGroupAddrType,
       "cienaCesMcastChanelStreamStartGroupAddr": cienaCesMcastChanelStreamStartGroupAddr,
       "cienaCesMcastChanelStreamStartGroupAddrPrefixLen": cienaCesMcastChanelStreamStartGroupAddrPrefixLen,
       "cienaCesMcastChanelStreamEndGroupAddrType": cienaCesMcastChanelStreamEndGroupAddrType,
       "cienaCesMcastChanelStreamEndGroupAddr": cienaCesMcastChanelStreamEndGroupAddr,
       "cienaCesMcastChannelStreamExIfcMemTable": cienaCesMcastChannelStreamExIfcMemTable,
       "cienaCesMcastChannelStreamExIfcMemEntry": cienaCesMcastChannelStreamExIfcMemEntry,
       "cienaCesMcastChannelStreamExIfcType": cienaCesMcastChannelStreamExIfcType,
       "cienaCesMcastChannelStreamExIfcIndex": cienaCesMcastChannelStreamExIfcIndex,
       "cienaCesMcastChannelStreamExIfcLiType": cienaCesMcastChannelStreamExIfcLiType,
       "cienaCesMcastChannelStreamExIfcLiIndex": cienaCesMcastChannelStreamExIfcLiIndex,
       "cienaCesMcastGlobalSnoopAdminState": cienaCesMcastGlobalSnoopAdminState,
       "cienaCesMcastFilterStatus": cienaCesMcastFilterStatus,
       "cienaCesMcastFilterGroupTable": cienaCesMcastFilterGroupTable,
       "cienaCesMcastFilterGroupEntry": cienaCesMcastFilterGroupEntry,
       "cienaCesMcastFilterGroupAddrType": cienaCesMcastFilterGroupAddrType,
       "cienaCesMcastFilterGroupAddr": cienaCesMcastFilterGroupAddr,
       "cienaCesMcastFilterGroupAddrPrefixLen": cienaCesMcastFilterGroupAddrPrefixLen,
       "cienaCesMcastFilterGroupState": cienaCesMcastFilterGroupState,
       "cienaCesMcastFilterGroupType": cienaCesMcastFilterGroupType,
       "cienaCesMcastFilterGroupSource": cienaCesMcastFilterGroupSource,
       "cienaCesMcastFilterGroupMemberCount": cienaCesMcastFilterGroupMemberCount,
       "cienaCesMcastFilterGroupCompatibilityMode": cienaCesMcastFilterGroupCompatibilityMode,
       "cienaCesMcastFilterGroupIGMPV1HostPresentTimeRemainingValue": cienaCesMcastFilterGroupIGMPV1HostPresentTimeRemainingValue,
       "cienaCesMcastFilterGroupIGMPV2HostPresentTimeRemainingValue": cienaCesMcastFilterGroupIGMPV2HostPresentTimeRemainingValue,
       "cienaCesMcastFilterGroupFilterMode": cienaCesMcastFilterGroupFilterMode,
       "cienaCesMcastFilterGroupNumOfSrcAddrs": cienaCesMcastFilterGroupNumOfSrcAddrs,
       "cienaCesMcastFilterGroupTimer": cienaCesMcastFilterGroupTimer,
       "cienaCesMcastFilterGroupSrcRecordTable": cienaCesMcastFilterGroupSrcRecordTable,
       "cienaCesMcastFilterGroupSrcRecordEntry": cienaCesMcastFilterGroupSrcRecordEntry,
       "cienaCesMcastFilterGroupSrcRecordSrcIpAddrType": cienaCesMcastFilterGroupSrcRecordSrcIpAddrType,
       "cienaCesMcastFilterGroupSrcRecordSrcIp": cienaCesMcastFilterGroupSrcRecordSrcIp,
       "cienaCesMcastFilterGroupSrcRecordSrcIpAddrPrefixLen": cienaCesMcastFilterGroupSrcRecordSrcIpAddrPrefixLen,
       "cienaCesMcastFilterGroupSrcRecordSrcIpAddress": cienaCesMcastFilterGroupSrcRecordSrcIpAddress,
       "cienaCesMcastFilterGroupSrcRecordSrcTimer": cienaCesMcastFilterGroupSrcRecordSrcTimer,
       "cienaCesMcastFilterGroupMemberTable": cienaCesMcastFilterGroupMemberTable,
       "cienaCesMcastFilterGroupMemberEntry": cienaCesMcastFilterGroupMemberEntry,
       "cienaCesMcastFilterGroupMemberInterfaceType": cienaCesMcastFilterGroupMemberInterfaceType,
       "cienaCesMcastFilterGroupMemberInterfaceIndex": cienaCesMcastFilterGroupMemberInterfaceIndex,
       "cienaCesMcastFilterGroupMemberInterfaceLiType": cienaCesMcastFilterGroupMemberInterfaceLiType,
       "cienaCesMcastFilterGroupMemberInterfaceLiIndex": cienaCesMcastFilterGroupMemberInterfaceLiIndex,
       "cienaCesMcastGlobalResources": cienaCesMcastGlobalResources,
       "cienaCesMcastMaxServiceInstances": cienaCesMcastMaxServiceInstances,
       "cienaCesMcastCurrentServiceInstances": cienaCesMcastCurrentServiceInstances,
       "cienaCesMcastMaxMcastGroups": cienaCesMcastMaxMcastGroups,
       "cienaCesMcastCurrentMcastGroups": cienaCesMcastCurrentMcastGroups,
       "cienaCesMcastMaxSrcAddrRecords": cienaCesMcastMaxSrcAddrRecords,
       "cienaCesMcastCurrentSrcAddrRecords": cienaCesMcastCurrentSrcAddrRecords,
       "cienaCesMcastMaxTimers": cienaCesMcastMaxTimers,
       "cienaCesMcastCurrentTimers": cienaCesMcastCurrentTimers,
       "cienaCesMcastMaxLogicalInterfaces": cienaCesMcastMaxLogicalInterfaces,
       "cienaCesMcastCurrentLogicalInterfaces": cienaCesMcastCurrentLogicalInterfaces,
       "cienaCesMcastMaxGrpMemberInterfaces": cienaCesMcastMaxGrpMemberInterfaces,
       "cienaCesMcastCurrentGrpMemberInterfaces": cienaCesMcastCurrentGrpMemberInterfaces,
       "cienaCesMcastFilterMIBNotificationPrefix": cienaCesMcastFilterMIBNotificationPrefix,
       "cienaCesMcastFilterMIBNotification": cienaCesMcastFilterMIBNotification,
       "cienaCesMcastAddrOverlapNotification": cienaCesMcastAddrOverlapNotification,
       "cienaCesMcastFilterStats": cienaCesMcastFilterStats,
       "cienaCesMcastFilterStatsTable": cienaCesMcastFilterStatsTable,
       "cienaCesMcastFilterStatsEntry": cienaCesMcastFilterStatsEntry,
       "cienaCesMcastStaticGrpCount": cienaCesMcastStaticGrpCount,
       "cienaCesMcastDynamicGrpCount": cienaCesMcastDynamicGrpCount,
       "cienaCesMcastJoinMessagesRx": cienaCesMcastJoinMessagesRx,
       "cienaCesMcastLeaveMessagesRx": cienaCesMcastLeaveMessagesRx,
       "cienaCesMcastV3ReportsRx": cienaCesMcastV3ReportsRx,
       "cienaCesMcastQueryMessagesRx": cienaCesMcastQueryMessagesRx,
       "cienaCesMcastQueryRxDiscards": cienaCesMcastQueryRxDiscards,
       "cienaCesMcastQueryTimeouts": cienaCesMcastQueryTimeouts,
       "cienaCesMcastUnknownPktTypeRx": cienaCesMcastUnknownPktTypeRx,
       "cienaCesMcastRouterRxDiscards": cienaCesMcastRouterRxDiscards,
       "cienaCesMcastHostRxDiscards": cienaCesMcastHostRxDiscards,
       "cienaCesMcastBadChecksumRx": cienaCesMcastBadChecksumRx,
       "cienaCesMcastL2L3MismatchRx": cienaCesMcastL2L3MismatchRx,
       "cienaCesMcastTotalMembers": cienaCesMcastTotalMembers,
       "cienaCesMcastLingerCount": cienaCesMcastLingerCount,
       "cienaCesMcastStatsQuerySrcIpZeroDiscard": cienaCesMcastStatsQuerySrcIpZeroDiscard,
       "cienaCesMcastCompatibilityModeDiscards": cienaCesMcastCompatibilityModeDiscards,
       "cienaCesMcastReplyTimeouts": cienaCesMcastReplyTimeouts,
       "cienaCesMcastResourceExceed": cienaCesMcastResourceExceed,
       "cienaCesMcastV3ReportsRxIsIn": cienaCesMcastV3ReportsRxIsIn,
       "cienaCesMcastV3ReportsRxIsEx": cienaCesMcastV3ReportsRxIsEx,
       "cienaCesMcastV3ReportsRxToIn": cienaCesMcastV3ReportsRxToIn,
       "cienaCesMcastV3ReportsRxToEx": cienaCesMcastV3ReportsRxToEx,
       "cienaCesMcastV3ReportsRxAllow": cienaCesMcastV3ReportsRxAllow,
       "cienaCesMcastV3ReportsRxBlock": cienaCesMcastV3ReportsRxBlock}
)
