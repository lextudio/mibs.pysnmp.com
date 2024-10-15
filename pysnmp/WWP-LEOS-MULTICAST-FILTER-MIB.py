# SNMP MIB module (WWP-LEOS-MULTICAST-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-MULTICAST-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:58 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosMcastFilterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7)
)
wwpLeosMcastFilterMIB.setRevisions(
        ("2008-10-02 19:00",
         "2008-06-19 00:00",
         "2003-02-10 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosMcastFilterMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosMcastFilterMIBObjects = _WwpLeosMcastFilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1)
)
_WwpLeosMcastFilterConfig_ObjectIdentity = ObjectIdentity
wwpLeosMcastFilterConfig = _WwpLeosMcastFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1)
)


class _WwpLeosMcastConfigState_Type(Integer32):
    """Custom type wwpLeosMcastConfigState based on Integer32"""
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


_WwpLeosMcastConfigState_Type.__name__ = "Integer32"
_WwpLeosMcastConfigState_Object = MibScalar
wwpLeosMcastConfigState = _WwpLeosMcastConfigState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 1),
    _WwpLeosMcastConfigState_Type()
)
wwpLeosMcastConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastConfigState.setStatus("current")
_WwpLeosMcastFilterActivationTable_Object = MibTable
wwpLeosMcastFilterActivationTable = _WwpLeosMcastFilterActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosMcastFilterActivationTable.setStatus("current")
_WwpLeosMcastFilterActivationEntry_Object = MibTableRow
wwpLeosMcastFilterActivationEntry = _WwpLeosMcastFilterActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 2, 1)
)
wwpLeosMcastFilterActivationEntry.setIndexNames(
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosMcastFilterActivationEntry.setStatus("current")
_WwpLeosMcastVlanId_Type = VlanId
_WwpLeosMcastVlanId_Object = MibTableColumn
wwpLeosMcastVlanId = _WwpLeosMcastVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 2, 1, 1),
    _WwpLeosMcastVlanId_Type()
)
wwpLeosMcastVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastVlanId.setStatus("current")


class _WwpLeosMcastFilterAdminState_Type(Integer32):
    """Custom type wwpLeosMcastFilterAdminState based on Integer32"""
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


_WwpLeosMcastFilterAdminState_Type.__name__ = "Integer32"
_WwpLeosMcastFilterAdminState_Object = MibTableColumn
wwpLeosMcastFilterAdminState = _WwpLeosMcastFilterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 2, 1, 2),
    _WwpLeosMcastFilterAdminState_Type()
)
wwpLeosMcastFilterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastFilterAdminState.setStatus("current")


class _WwpLeosMcastFilterOperState_Type(Integer32):
    """Custom type wwpLeosMcastFilterOperState based on Integer32"""
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


_WwpLeosMcastFilterOperState_Type.__name__ = "Integer32"
_WwpLeosMcastFilterOperState_Object = MibTableColumn
wwpLeosMcastFilterOperState = _WwpLeosMcastFilterOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 2, 1, 3),
    _WwpLeosMcastFilterOperState_Type()
)
wwpLeosMcastFilterOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastFilterOperState.setStatus("current")
_WwpLeosMcastFilterState_Type = RowStatus
_WwpLeosMcastFilterState_Object = MibTableColumn
wwpLeosMcastFilterState = _WwpLeosMcastFilterState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 2, 1, 4),
    _WwpLeosMcastFilterState_Type()
)
wwpLeosMcastFilterState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMcastFilterState.setStatus("current")
_WwpLeosMcastFilterServerPortTable_Object = MibTable
wwpLeosMcastFilterServerPortTable = _WwpLeosMcastFilterServerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLeosMcastFilterServerPortTable.setStatus("current")
_WwpLeosMcastFilterServerPortEntry_Object = MibTableRow
wwpLeosMcastFilterServerPortEntry = _WwpLeosMcastFilterServerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 3, 1)
)
wwpLeosMcastFilterServerPortEntry.setIndexNames(
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastVlanId"),
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastServerPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosMcastFilterServerPortEntry.setStatus("current")


class _WwpLeosMcastServerPortId_Type(Integer32):
    """Custom type wwpLeosMcastServerPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosMcastServerPortId_Type.__name__ = "Integer32"
_WwpLeosMcastServerPortId_Object = MibTableColumn
wwpLeosMcastServerPortId = _WwpLeosMcastServerPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 3, 1, 1),
    _WwpLeosMcastServerPortId_Type()
)
wwpLeosMcastServerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastServerPortId.setStatus("current")
_WwpLeosMcastServerPortStatus_Type = RowStatus
_WwpLeosMcastServerPortStatus_Object = MibTableColumn
wwpLeosMcastServerPortStatus = _WwpLeosMcastServerPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 3, 1, 2),
    _WwpLeosMcastServerPortStatus_Type()
)
wwpLeosMcastServerPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMcastServerPortStatus.setStatus("current")
_WwpLeosMcastIgmpSnoopTable_Object = MibTable
wwpLeosMcastIgmpSnoopTable = _WwpLeosMcastIgmpSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopTable.setStatus("current")
_WwpLeosMcastIgmpSnoopEntry_Object = MibTableRow
wwpLeosMcastIgmpSnoopEntry = _WwpLeosMcastIgmpSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1)
)
wwpLeosMcastIgmpSnoopEntry.setIndexNames(
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopEntry.setStatus("current")


class _WwpLeosMcastIgmpSnoopEnable_Type(TruthValue):
    """Custom type wwpLeosMcastIgmpSnoopEnable based on TruthValue"""


_WwpLeosMcastIgmpSnoopEnable_Object = MibTableColumn
wwpLeosMcastIgmpSnoopEnable = _WwpLeosMcastIgmpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 1),
    _WwpLeosMcastIgmpSnoopEnable_Type()
)
wwpLeosMcastIgmpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopEnable.setStatus("current")


class _WwpLeosMcastIgmpSnoopRobustness_Type(Integer32):
    """Custom type wwpLeosMcastIgmpSnoopRobustness based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WwpLeosMcastIgmpSnoopRobustness_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpSnoopRobustness_Object = MibTableColumn
wwpLeosMcastIgmpSnoopRobustness = _WwpLeosMcastIgmpSnoopRobustness_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 2),
    _WwpLeosMcastIgmpSnoopRobustness_Type()
)
wwpLeosMcastIgmpSnoopRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopRobustness.setStatus("current")


class _WwpLeosMcastIgmpSnoopProxyQueryInterval_Type(Integer32):
    """Custom type wwpLeosMcastIgmpSnoopProxyQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 999999),
    )


_WwpLeosMcastIgmpSnoopProxyQueryInterval_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpSnoopProxyQueryInterval_Object = MibTableColumn
wwpLeosMcastIgmpSnoopProxyQueryInterval = _WwpLeosMcastIgmpSnoopProxyQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 3),
    _WwpLeosMcastIgmpSnoopProxyQueryInterval_Type()
)
wwpLeosMcastIgmpSnoopProxyQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopProxyQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopProxyQueryInterval.setUnits("seconds")


class _WwpLeosMcastIgmpSnoopProxyQueryReplyTmo_Type(Integer32):
    """Custom type wwpLeosMcastIgmpSnoopProxyQueryReplyTmo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_WwpLeosMcastIgmpSnoopProxyQueryReplyTmo_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpSnoopProxyQueryReplyTmo_Object = MibTableColumn
wwpLeosMcastIgmpSnoopProxyQueryReplyTmo = _WwpLeosMcastIgmpSnoopProxyQueryReplyTmo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 4),
    _WwpLeosMcastIgmpSnoopProxyQueryReplyTmo_Type()
)
wwpLeosMcastIgmpSnoopProxyQueryReplyTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopProxyQueryReplyTmo.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopProxyQueryReplyTmo.setUnits("seconds")


class _WwpLeosMcastIgmpSnoopProxyQueryDelay_Type(Integer32):
    """Custom type wwpLeosMcastIgmpSnoopProxyQueryDelay based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosMcastIgmpSnoopProxyQueryDelay_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpSnoopProxyQueryDelay_Object = MibTableColumn
wwpLeosMcastIgmpSnoopProxyQueryDelay = _WwpLeosMcastIgmpSnoopProxyQueryDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 5),
    _WwpLeosMcastIgmpSnoopProxyQueryDelay_Type()
)
wwpLeosMcastIgmpSnoopProxyQueryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopProxyQueryDelay.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopProxyQueryDelay.setUnits("seconds")


class _WwpLeosMcastIgmpSnoopLingerTmo_Type(Integer32):
    """Custom type wwpLeosMcastIgmpSnoopLingerTmo based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_WwpLeosMcastIgmpSnoopLingerTmo_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpSnoopLingerTmo_Object = MibTableColumn
wwpLeosMcastIgmpSnoopLingerTmo = _WwpLeosMcastIgmpSnoopLingerTmo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 6),
    _WwpLeosMcastIgmpSnoopLingerTmo_Type()
)
wwpLeosMcastIgmpSnoopLingerTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopLingerTmo.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopLingerTmo.setUnits("seconds")


class _WwpLeosMcastIgmpQueryEngineState_Type(Integer32):
    """Custom type wwpLeosMcastIgmpQueryEngineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_WwpLeosMcastIgmpQueryEngineState_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpQueryEngineState_Object = MibTableColumn
wwpLeosMcastIgmpQueryEngineState = _WwpLeosMcastIgmpQueryEngineState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 7),
    _WwpLeosMcastIgmpQueryEngineState_Type()
)
wwpLeosMcastIgmpQueryEngineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpQueryEngineState.setStatus("current")
_WwpLeosMcastIgmpProxyQuerySrcIp_Type = IpAddress
_WwpLeosMcastIgmpProxyQuerySrcIp_Object = MibTableColumn
wwpLeosMcastIgmpProxyQuerySrcIp = _WwpLeosMcastIgmpProxyQuerySrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 8),
    _WwpLeosMcastIgmpProxyQuerySrcIp_Type()
)
wwpLeosMcastIgmpProxyQuerySrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpProxyQuerySrcIp.setStatus("current")


class _WwpLeosMcastIgmpRouterQueryInterval_Type(Integer32):
    """Custom type wwpLeosMcastIgmpRouterQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 999999),
    )


_WwpLeosMcastIgmpRouterQueryInterval_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpRouterQueryInterval_Object = MibTableColumn
wwpLeosMcastIgmpRouterQueryInterval = _WwpLeosMcastIgmpRouterQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 9),
    _WwpLeosMcastIgmpRouterQueryInterval_Type()
)
wwpLeosMcastIgmpRouterQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpRouterQueryInterval.setStatus("current")


class _WwpLeosMcastIgmpMinResponseTime_Type(Integer32):
    """Custom type wwpLeosMcastIgmpMinResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 600),
    )


_WwpLeosMcastIgmpMinResponseTime_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpMinResponseTime_Object = MibTableColumn
wwpLeosMcastIgmpMinResponseTime = _WwpLeosMcastIgmpMinResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 10),
    _WwpLeosMcastIgmpMinResponseTime_Type()
)
wwpLeosMcastIgmpMinResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpMinResponseTime.setStatus("current")


class _WwpLeosMcastIgmpDefaultRouterPort_Type(Integer32):
    """Custom type wwpLeosMcastIgmpDefaultRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosMcastIgmpDefaultRouterPort_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpDefaultRouterPort_Object = MibTableColumn
wwpLeosMcastIgmpDefaultRouterPort = _WwpLeosMcastIgmpDefaultRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 11),
    _WwpLeosMcastIgmpDefaultRouterPort_Type()
)
wwpLeosMcastIgmpDefaultRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpDefaultRouterPort.setStatus("current")


class _WwpLeosMcastIgmpInquisitiveLeaveState_Type(Integer32):
    """Custom type wwpLeosMcastIgmpInquisitiveLeaveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_WwpLeosMcastIgmpInquisitiveLeaveState_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpInquisitiveLeaveState_Object = MibTableColumn
wwpLeosMcastIgmpInquisitiveLeaveState = _WwpLeosMcastIgmpInquisitiveLeaveState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 12),
    _WwpLeosMcastIgmpInquisitiveLeaveState_Type()
)
wwpLeosMcastIgmpInquisitiveLeaveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpInquisitiveLeaveState.setStatus("current")


class _WwpLeosMcastIgmpLastMemberQueryInterval_Type(Integer32):
    """Custom type wwpLeosMcastIgmpLastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_WwpLeosMcastIgmpLastMemberQueryInterval_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpLastMemberQueryInterval_Object = MibTableColumn
wwpLeosMcastIgmpLastMemberQueryInterval = _WwpLeosMcastIgmpLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 13),
    _WwpLeosMcastIgmpLastMemberQueryInterval_Type()
)
wwpLeosMcastIgmpLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpLastMemberQueryInterval.setStatus("current")


class _WwpLeosMcastIgmpPriority_Type(Integer32):
    """Custom type wwpLeosMcastIgmpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosMcastIgmpPriority_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpPriority_Object = MibTableColumn
wwpLeosMcastIgmpPriority = _WwpLeosMcastIgmpPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 14),
    _WwpLeosMcastIgmpPriority_Type()
)
wwpLeosMcastIgmpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpPriority.setStatus("current")
_WwpLeosMcastIgmpSnoopRouterRangeStartIpAddr_Type = IpAddress
_WwpLeosMcastIgmpSnoopRouterRangeStartIpAddr_Object = MibTableColumn
wwpLeosMcastIgmpSnoopRouterRangeStartIpAddr = _WwpLeosMcastIgmpSnoopRouterRangeStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 15),
    _WwpLeosMcastIgmpSnoopRouterRangeStartIpAddr_Type()
)
wwpLeosMcastIgmpSnoopRouterRangeStartIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopRouterRangeStartIpAddr.setStatus("current")
_WwpLeosMcastIgmpSnoopRouterRangeEndIpAddr_Type = IpAddress
_WwpLeosMcastIgmpSnoopRouterRangeEndIpAddr_Object = MibTableColumn
wwpLeosMcastIgmpSnoopRouterRangeEndIpAddr = _WwpLeosMcastIgmpSnoopRouterRangeEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 16),
    _WwpLeosMcastIgmpSnoopRouterRangeEndIpAddr_Type()
)
wwpLeosMcastIgmpSnoopRouterRangeEndIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopRouterRangeEndIpAddr.setStatus("current")


class _WwpLeosMcastIgmpSnoopActiveLingerTimeout_Type(Integer32):
    """Custom type wwpLeosMcastIgmpSnoopActiveLingerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_WwpLeosMcastIgmpSnoopActiveLingerTimeout_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpSnoopActiveLingerTimeout_Object = MibTableColumn
wwpLeosMcastIgmpSnoopActiveLingerTimeout = _WwpLeosMcastIgmpSnoopActiveLingerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 17),
    _WwpLeosMcastIgmpSnoopActiveLingerTimeout_Type()
)
wwpLeosMcastIgmpSnoopActiveLingerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopActiveLingerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopActiveLingerTimeout.setUnits("seconds")


class _WwpLeosMcastIgmpSnoopServerTopology_Type(Integer32):
    """Custom type wwpLeosMcastIgmpSnoopServerTopology based on Integer32"""
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


_WwpLeosMcastIgmpSnoopServerTopology_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpSnoopServerTopology_Object = MibTableColumn
wwpLeosMcastIgmpSnoopServerTopology = _WwpLeosMcastIgmpSnoopServerTopology_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 18),
    _WwpLeosMcastIgmpSnoopServerTopology_Type()
)
wwpLeosMcastIgmpSnoopServerTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopServerTopology.setStatus("current")


class _WwpLeosMcastIgmpSnoopRapidRecoveryMode_Type(Integer32):
    """Custom type wwpLeosMcastIgmpSnoopRapidRecoveryMode based on Integer32"""
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


_WwpLeosMcastIgmpSnoopRapidRecoveryMode_Type.__name__ = "Integer32"
_WwpLeosMcastIgmpSnoopRapidRecoveryMode_Object = MibTableColumn
wwpLeosMcastIgmpSnoopRapidRecoveryMode = _WwpLeosMcastIgmpSnoopRapidRecoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 4, 1, 19),
    _WwpLeosMcastIgmpSnoopRapidRecoveryMode_Type()
)
wwpLeosMcastIgmpSnoopRapidRecoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastIgmpSnoopRapidRecoveryMode.setStatus("current")
_WwpLeosMcastChannelStreamTable_Object = MibTable
wwpLeosMcastChannelStreamTable = _WwpLeosMcastChannelStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosMcastChannelStreamTable.setStatus("current")
_WwpLeosMcastChannelStreamEntry_Object = MibTableRow
wwpLeosMcastChannelStreamEntry = _WwpLeosMcastChannelStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 5, 1)
)
wwpLeosMcastChannelStreamEntry.setIndexNames(
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastVlanId"),
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastChanelStreamStartGroupAddr"),
)
if mibBuilder.loadTexts:
    wwpLeosMcastChannelStreamEntry.setStatus("current")
_WwpLeosMcastChanelStreamStartGroupAddr_Type = IpAddress
_WwpLeosMcastChanelStreamStartGroupAddr_Object = MibTableColumn
wwpLeosMcastChanelStreamStartGroupAddr = _WwpLeosMcastChanelStreamStartGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 5, 1, 1),
    _WwpLeosMcastChanelStreamStartGroupAddr_Type()
)
wwpLeosMcastChanelStreamStartGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastChanelStreamStartGroupAddr.setStatus("current")
_WwpLeosMcastChanelStreamEndGroupAddr_Type = IpAddress
_WwpLeosMcastChanelStreamEndGroupAddr_Object = MibTableColumn
wwpLeosMcastChanelStreamEndGroupAddr = _WwpLeosMcastChanelStreamEndGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 5, 1, 2),
    _WwpLeosMcastChanelStreamEndGroupAddr_Type()
)
wwpLeosMcastChanelStreamEndGroupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastChanelStreamEndGroupAddr.setStatus("current")
_WwpLeosMcastChannelStreamStatus_Type = RowStatus
_WwpLeosMcastChannelStreamStatus_Object = MibTableColumn
wwpLeosMcastChannelStreamStatus = _WwpLeosMcastChannelStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 5, 1, 3),
    _WwpLeosMcastChannelStreamStatus_Type()
)
wwpLeosMcastChannelStreamStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMcastChannelStreamStatus.setStatus("current")
_WwpLeosMcastFilterConfigTable_Object = MibTable
wwpLeosMcastFilterConfigTable = _WwpLeosMcastFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpLeosMcastFilterConfigTable.setStatus("current")
_WwpLeosMcastFilterConfigEntry_Object = MibTableRow
wwpLeosMcastFilterConfigEntry = _WwpLeosMcastFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 6, 1)
)
wwpLeosMcastFilterConfigEntry.setIndexNames(
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosMcastFilterConfigEntry.setStatus("current")


class _WwpLeosMcastFilterUPFActivate_Type(TruthValue):
    """Custom type wwpLeosMcastFilterUPFActivate based on TruthValue"""


_WwpLeosMcastFilterUPFActivate_Object = MibTableColumn
wwpLeosMcastFilterUPFActivate = _WwpLeosMcastFilterUPFActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 6, 1, 1),
    _WwpLeosMcastFilterUPFActivate_Type()
)
wwpLeosMcastFilterUPFActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastFilterUPFActivate.setStatus("current")


class _WwpLeosMcastUnresolvedAction_Type(Integer32):
    """Custom type wwpLeosMcastUnresolvedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("flood", 1))
    )


_WwpLeosMcastUnresolvedAction_Type.__name__ = "Integer32"
_WwpLeosMcastUnresolvedAction_Object = MibTableColumn
wwpLeosMcastUnresolvedAction = _WwpLeosMcastUnresolvedAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 6, 1, 2),
    _WwpLeosMcastUnresolvedAction_Type()
)
wwpLeosMcastUnresolvedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastUnresolvedAction.setStatus("current")


class _WwpLeosMcastFilterWKMFLocalActivate_Type(Integer32):
    """Custom type wwpLeosMcastFilterWKMFLocalActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("flood", 1))
    )


_WwpLeosMcastFilterWKMFLocalActivate_Type.__name__ = "Integer32"
_WwpLeosMcastFilterWKMFLocalActivate_Object = MibTableColumn
wwpLeosMcastFilterWKMFLocalActivate = _WwpLeosMcastFilterWKMFLocalActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 6, 1, 3),
    _WwpLeosMcastFilterWKMFLocalActivate_Type()
)
wwpLeosMcastFilterWKMFLocalActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastFilterWKMFLocalActivate.setStatus("current")


class _WwpLeosMcastFilterWKMFInternetActivate_Type(Integer32):
    """Custom type wwpLeosMcastFilterWKMFInternetActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("flood", 1))
    )


_WwpLeosMcastFilterWKMFInternetActivate_Type.__name__ = "Integer32"
_WwpLeosMcastFilterWKMFInternetActivate_Object = MibTableColumn
wwpLeosMcastFilterWKMFInternetActivate = _WwpLeosMcastFilterWKMFInternetActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 6, 1, 4),
    _WwpLeosMcastFilterWKMFInternetActivate_Type()
)
wwpLeosMcastFilterWKMFInternetActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastFilterWKMFInternetActivate.setStatus("current")


class _WwpLeosMcastFilterWKMFAdhocActivate_Type(Integer32):
    """Custom type wwpLeosMcastFilterWKMFAdhocActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("flood", 1))
    )


_WwpLeosMcastFilterWKMFAdhocActivate_Type.__name__ = "Integer32"
_WwpLeosMcastFilterWKMFAdhocActivate_Object = MibTableColumn
wwpLeosMcastFilterWKMFAdhocActivate = _WwpLeosMcastFilterWKMFAdhocActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 6, 1, 5),
    _WwpLeosMcastFilterWKMFAdhocActivate_Type()
)
wwpLeosMcastFilterWKMFAdhocActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastFilterWKMFAdhocActivate.setStatus("current")


class _WwpLeosMcastFilterWKMFStMulticastActivate_Type(Integer32):
    """Custom type wwpLeosMcastFilterWKMFStMulticastActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("flood", 1))
    )


_WwpLeosMcastFilterWKMFStMulticastActivate_Type.__name__ = "Integer32"
_WwpLeosMcastFilterWKMFStMulticastActivate_Object = MibTableColumn
wwpLeosMcastFilterWKMFStMulticastActivate = _WwpLeosMcastFilterWKMFStMulticastActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 6, 1, 6),
    _WwpLeosMcastFilterWKMFStMulticastActivate_Type()
)
wwpLeosMcastFilterWKMFStMulticastActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastFilterWKMFStMulticastActivate.setStatus("current")


class _WwpLeosMcastFilterWKMFSdpSapActivate_Type(Integer32):
    """Custom type wwpLeosMcastFilterWKMFSdpSapActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("flood", 1))
    )


_WwpLeosMcastFilterWKMFSdpSapActivate_Type.__name__ = "Integer32"
_WwpLeosMcastFilterWKMFSdpSapActivate_Object = MibTableColumn
wwpLeosMcastFilterWKMFSdpSapActivate = _WwpLeosMcastFilterWKMFSdpSapActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 6, 1, 7),
    _WwpLeosMcastFilterWKMFSdpSapActivate_Type()
)
wwpLeosMcastFilterWKMFSdpSapActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastFilterWKMFSdpSapActivate.setStatus("current")
_WwpLeosMcastChannelStreamExPortMemTable_Object = MibTable
wwpLeosMcastChannelStreamExPortMemTable = _WwpLeosMcastChannelStreamExPortMemTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 7)
)
if mibBuilder.loadTexts:
    wwpLeosMcastChannelStreamExPortMemTable.setStatus("current")
_WwpLeosMcastChannelStreamExPortMemEntry_Object = MibTableRow
wwpLeosMcastChannelStreamExPortMemEntry = _WwpLeosMcastChannelStreamExPortMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 7, 1)
)
wwpLeosMcastChannelStreamExPortMemEntry.setIndexNames(
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastVlanId"),
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastChannelStreamExPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosMcastChannelStreamExPortMemEntry.setStatus("current")


class _WwpLeosMcastChannelStreamExPortId_Type(Integer32):
    """Custom type wwpLeosMcastChannelStreamExPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosMcastChannelStreamExPortId_Type.__name__ = "Integer32"
_WwpLeosMcastChannelStreamExPortId_Object = MibTableColumn
wwpLeosMcastChannelStreamExPortId = _WwpLeosMcastChannelStreamExPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 7, 1, 1),
    _WwpLeosMcastChannelStreamExPortId_Type()
)
wwpLeosMcastChannelStreamExPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastChannelStreamExPortId.setStatus("current")
_WwpLeosMcastChannelStreamExPortMemStatus_Type = RowStatus
_WwpLeosMcastChannelStreamExPortMemStatus_Object = MibTableColumn
wwpLeosMcastChannelStreamExPortMemStatus = _WwpLeosMcastChannelStreamExPortMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 7, 1, 2),
    _WwpLeosMcastChannelStreamExPortMemStatus_Type()
)
wwpLeosMcastChannelStreamExPortMemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMcastChannelStreamExPortMemStatus.setStatus("current")


class _WwpLeosMcastSnoopState_Type(TruthValue):
    """Custom type wwpLeosMcastSnoopState based on TruthValue"""


_WwpLeosMcastSnoopState_Object = MibScalar
wwpLeosMcastSnoopState = _WwpLeosMcastSnoopState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 8),
    _WwpLeosMcastSnoopState_Type()
)
wwpLeosMcastSnoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastSnoopState.setStatus("current")


class _WwpLeosMcastGlobalStatsClear_Type(Integer32):
    """Custom type wwpLeosMcastGlobalStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosMcastGlobalStatsClear_Type.__name__ = "Integer32"
_WwpLeosMcastGlobalStatsClear_Object = MibScalar
wwpLeosMcastGlobalStatsClear = _WwpLeosMcastGlobalStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 1, 10),
    _WwpLeosMcastGlobalStatsClear_Type()
)
wwpLeosMcastGlobalStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastGlobalStatsClear.setStatus("current")
_WwpLeosMcastFilterStatus_ObjectIdentity = ObjectIdentity
wwpLeosMcastFilterStatus = _WwpLeosMcastFilterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 2)
)
_WwpLeosMcastGroupTable_Object = MibTable
wwpLeosMcastGroupTable = _WwpLeosMcastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosMcastGroupTable.setStatus("current")
_WwpLeosMcastGroupEntry_Object = MibTableRow
wwpLeosMcastGroupEntry = _WwpLeosMcastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 2, 1, 1)
)
wwpLeosMcastGroupEntry.setIndexNames(
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastVlanId"),
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastGroupAddr"),
)
if mibBuilder.loadTexts:
    wwpLeosMcastGroupEntry.setStatus("current")
_WwpLeosMcastGroupAddr_Type = IpAddress
_WwpLeosMcastGroupAddr_Object = MibTableColumn
wwpLeosMcastGroupAddr = _WwpLeosMcastGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 2, 1, 1, 1),
    _WwpLeosMcastGroupAddr_Type()
)
wwpLeosMcastGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastGroupAddr.setStatus("current")


class _WwpLeosMcastState_Type(Integer32):
    """Custom type wwpLeosMcastState based on Integer32"""
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
          ("linger", 3),
          ("query", 2))
    )


_WwpLeosMcastState_Type.__name__ = "Integer32"
_WwpLeosMcastState_Object = MibTableColumn
wwpLeosMcastState = _WwpLeosMcastState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 2, 1, 1, 2),
    _WwpLeosMcastState_Type()
)
wwpLeosMcastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastState.setStatus("current")


class _WwpLeosMcastType_Type(Integer32):
    """Custom type wwpLeosMcastType based on Integer32"""
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


_WwpLeosMcastType_Type.__name__ = "Integer32"
_WwpLeosMcastType_Object = MibTableColumn
wwpLeosMcastType = _WwpLeosMcastType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 2, 1, 1, 3),
    _WwpLeosMcastType_Type()
)
wwpLeosMcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastType.setStatus("current")


class _WwpLeosMcastSource_Type(Integer32):
    """Custom type wwpLeosMcastSource based on Integer32"""
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


_WwpLeosMcastSource_Type.__name__ = "Integer32"
_WwpLeosMcastSource_Object = MibTableColumn
wwpLeosMcastSource = _WwpLeosMcastSource_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 2, 1, 1, 4),
    _WwpLeosMcastSource_Type()
)
wwpLeosMcastSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastSource.setStatus("current")
_WwpLeosMcastMemberCount_Type = Counter32
_WwpLeosMcastMemberCount_Object = MibTableColumn
wwpLeosMcastMemberCount = _WwpLeosMcastMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 2, 1, 1, 5),
    _WwpLeosMcastMemberCount_Type()
)
wwpLeosMcastMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastMemberCount.setStatus("current")
_WwpLeosMcastGroupMemberTable_Object = MibTable
wwpLeosMcastGroupMemberTable = _WwpLeosMcastGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwpLeosMcastGroupMemberTable.setStatus("current")
_WwpLeosMcastGroupMemberEntry_Object = MibTableRow
wwpLeosMcastGroupMemberEntry = _WwpLeosMcastGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 2, 2, 1)
)
wwpLeosMcastGroupMemberEntry.setIndexNames(
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastVlanId"),
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastGroupAddr"),
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosMcastGroupMemberEntry.setStatus("current")


class _WwpLeosMcastPortId_Type(Integer32):
    """Custom type wwpLeosMcastPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosMcastPortId_Type.__name__ = "Integer32"
_WwpLeosMcastPortId_Object = MibTableColumn
wwpLeosMcastPortId = _WwpLeosMcastPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 2, 2, 1, 1),
    _WwpLeosMcastPortId_Type()
)
wwpLeosMcastPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastPortId.setStatus("current")


class _WwpLeosMcastPortTagId_Type(Integer32):
    """Custom type wwpLeosMcastPortTagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WwpLeosMcastPortTagId_Type.__name__ = "Integer32"
_WwpLeosMcastPortTagId_Object = MibTableColumn
wwpLeosMcastPortTagId = _WwpLeosMcastPortTagId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 2, 2, 1, 2),
    _WwpLeosMcastPortTagId_Type()
)
wwpLeosMcastPortTagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastPortTagId.setStatus("current")
_WwpLeosMcastFilterStats_ObjectIdentity = ObjectIdentity
wwpLeosMcastFilterStats = _WwpLeosMcastFilterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3)
)
_WwpLeosMcastFilterStatsTable_Object = MibTable
wwpLeosMcastFilterStatsTable = _WwpLeosMcastFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wwpLeosMcastFilterStatsTable.setStatus("current")
_WwpLeosMcastFilterStatsEntry_Object = MibTableRow
wwpLeosMcastFilterStatsEntry = _WwpLeosMcastFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1)
)
wwpLeosMcastFilterStatsEntry.setIndexNames(
    (0, "WWP-LEOS-MULTICAST-FILTER-MIB", "wwpLeosMcastVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosMcastFilterStatsEntry.setStatus("current")


class _WwpLeosMcastStaticGrpCount_Type(Integer32):
    """Custom type wwpLeosMcastStaticGrpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosMcastStaticGrpCount_Type.__name__ = "Integer32"
_WwpLeosMcastStaticGrpCount_Object = MibTableColumn
wwpLeosMcastStaticGrpCount = _WwpLeosMcastStaticGrpCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 1),
    _WwpLeosMcastStaticGrpCount_Type()
)
wwpLeosMcastStaticGrpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastStaticGrpCount.setStatus("current")


class _WwpLeosMcastDynamicGrpCount_Type(Integer32):
    """Custom type wwpLeosMcastDynamicGrpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosMcastDynamicGrpCount_Type.__name__ = "Integer32"
_WwpLeosMcastDynamicGrpCount_Object = MibTableColumn
wwpLeosMcastDynamicGrpCount = _WwpLeosMcastDynamicGrpCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 2),
    _WwpLeosMcastDynamicGrpCount_Type()
)
wwpLeosMcastDynamicGrpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastDynamicGrpCount.setStatus("current")
_WwpLeosMcastJoinMessages_Type = Counter32
_WwpLeosMcastJoinMessages_Object = MibTableColumn
wwpLeosMcastJoinMessages = _WwpLeosMcastJoinMessages_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 3),
    _WwpLeosMcastJoinMessages_Type()
)
wwpLeosMcastJoinMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastJoinMessages.setStatus("current")
_WwpLeosMcastLeaveMessages_Type = Counter32
_WwpLeosMcastLeaveMessages_Object = MibTableColumn
wwpLeosMcastLeaveMessages = _WwpLeosMcastLeaveMessages_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 4),
    _WwpLeosMcastLeaveMessages_Type()
)
wwpLeosMcastLeaveMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastLeaveMessages.setStatus("current")
_WwpLeosMcastQueryMessages_Type = Counter32
_WwpLeosMcastQueryMessages_Object = MibTableColumn
wwpLeosMcastQueryMessages = _WwpLeosMcastQueryMessages_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 5),
    _WwpLeosMcastQueryMessages_Type()
)
wwpLeosMcastQueryMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastQueryMessages.setStatus("current")
_WwpLeosMcastQueryDiscards_Type = Counter32
_WwpLeosMcastQueryDiscards_Object = MibTableColumn
wwpLeosMcastQueryDiscards = _WwpLeosMcastQueryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 6),
    _WwpLeosMcastQueryDiscards_Type()
)
wwpLeosMcastQueryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastQueryDiscards.setStatus("current")
_WwpLeosMcastQueryTimeouts_Type = Counter32
_WwpLeosMcastQueryTimeouts_Object = MibTableColumn
wwpLeosMcastQueryTimeouts = _WwpLeosMcastQueryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 7),
    _WwpLeosMcastQueryTimeouts_Type()
)
wwpLeosMcastQueryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastQueryTimeouts.setStatus("current")
_WwpLeosMcastUnknownPktType_Type = Counter32
_WwpLeosMcastUnknownPktType_Object = MibTableColumn
wwpLeosMcastUnknownPktType = _WwpLeosMcastUnknownPktType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 8),
    _WwpLeosMcastUnknownPktType_Type()
)
wwpLeosMcastUnknownPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastUnknownPktType.setStatus("current")
_WwpLeosMcastRouterDiscards_Type = Counter32
_WwpLeosMcastRouterDiscards_Object = MibTableColumn
wwpLeosMcastRouterDiscards = _WwpLeosMcastRouterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 9),
    _WwpLeosMcastRouterDiscards_Type()
)
wwpLeosMcastRouterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastRouterDiscards.setStatus("current")
_WwpLeosMcastHostDiscards_Type = Counter32
_WwpLeosMcastHostDiscards_Object = MibTableColumn
wwpLeosMcastHostDiscards = _WwpLeosMcastHostDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 10),
    _WwpLeosMcastHostDiscards_Type()
)
wwpLeosMcastHostDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastHostDiscards.setStatus("current")
_WwpLeosMcastBadChecksum_Type = Counter32
_WwpLeosMcastBadChecksum_Object = MibTableColumn
wwpLeosMcastBadChecksum = _WwpLeosMcastBadChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 11),
    _WwpLeosMcastBadChecksum_Type()
)
wwpLeosMcastBadChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastBadChecksum.setStatus("current")
_WwpLeosMcastL2L3Mismatch_Type = Counter32
_WwpLeosMcastL2L3Mismatch_Object = MibTableColumn
wwpLeosMcastL2L3Mismatch = _WwpLeosMcastL2L3Mismatch_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 12),
    _WwpLeosMcastL2L3Mismatch_Type()
)
wwpLeosMcastL2L3Mismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastL2L3Mismatch.setStatus("current")
_WwpLeosMcastTotalMembers_Type = Counter32
_WwpLeosMcastTotalMembers_Object = MibTableColumn
wwpLeosMcastTotalMembers = _WwpLeosMcastTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 13),
    _WwpLeosMcastTotalMembers_Type()
)
wwpLeosMcastTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastTotalMembers.setStatus("current")
_WwpLeosMcastLingerCount_Type = Counter32
_WwpLeosMcastLingerCount_Object = MibTableColumn
wwpLeosMcastLingerCount = _WwpLeosMcastLingerCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 14),
    _WwpLeosMcastLingerCount_Type()
)
wwpLeosMcastLingerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastLingerCount.setStatus("current")
_WwpLeosMcastRouterSrcMacAddr_Type = MacAddress
_WwpLeosMcastRouterSrcMacAddr_Object = MibTableColumn
wwpLeosMcastRouterSrcMacAddr = _WwpLeosMcastRouterSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 15),
    _WwpLeosMcastRouterSrcMacAddr_Type()
)
wwpLeosMcastRouterSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastRouterSrcMacAddr.setStatus("current")
_WwpLeosMcastRouterSrcIpAddr_Type = IpAddress
_WwpLeosMcastRouterSrcIpAddr_Object = MibTableColumn
wwpLeosMcastRouterSrcIpAddr = _WwpLeosMcastRouterSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 16),
    _WwpLeosMcastRouterSrcIpAddr_Type()
)
wwpLeosMcastRouterSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastRouterSrcIpAddr.setStatus("current")


class _WwpLeosMcastRouterPortId_Type(Integer32):
    """Custom type wwpLeosMcastRouterPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosMcastRouterPortId_Type.__name__ = "Integer32"
_WwpLeosMcastRouterPortId_Object = MibTableColumn
wwpLeosMcastRouterPortId = _WwpLeosMcastRouterPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 17),
    _WwpLeosMcastRouterPortId_Type()
)
wwpLeosMcastRouterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastRouterPortId.setStatus("current")


class _WwpLeosMcastReportSendPortId_Type(Integer32):
    """Custom type wwpLeosMcastReportSendPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosMcastReportSendPortId_Type.__name__ = "Integer32"
_WwpLeosMcastReportSendPortId_Object = MibTableColumn
wwpLeosMcastReportSendPortId = _WwpLeosMcastReportSendPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 18),
    _WwpLeosMcastReportSendPortId_Type()
)
wwpLeosMcastReportSendPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastReportSendPortId.setStatus("current")


class _WwpLeosMcastStatsClear_Type(Integer32):
    """Custom type wwpLeosMcastStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosMcastStatsClear_Type.__name__ = "Integer32"
_WwpLeosMcastStatsClear_Object = MibTableColumn
wwpLeosMcastStatsClear = _WwpLeosMcastStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 19),
    _WwpLeosMcastStatsClear_Type()
)
wwpLeosMcastStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMcastStatsClear.setStatus("current")
_WwpLeosMcastStatsQuerySrcIpZeroDiscard_Type = Counter32
_WwpLeosMcastStatsQuerySrcIpZeroDiscard_Object = MibTableColumn
wwpLeosMcastStatsQuerySrcIpZeroDiscard = _WwpLeosMcastStatsQuerySrcIpZeroDiscard_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 1, 3, 1, 1, 20),
    _WwpLeosMcastStatsQuerySrcIpZeroDiscard_Type()
)
wwpLeosMcastStatsQuerySrcIpZeroDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMcastStatsQuerySrcIpZeroDiscard.setStatus("current")
_WwpLeosMcastFilterMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosMcastFilterMIBNotificationPrefix = _WwpLeosMcastFilterMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 2)
)
_WwpLeosMcastFilterMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosMcastFilterMIBNotifications = _WwpLeosMcastFilterMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 2, 0)
)
_WwpLeosMcastFilterMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosMcastFilterMIBConformance = _WwpLeosMcastFilterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 3)
)
_WwpLeosMcastFilterMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosMcastFilterMIBCompliances = _WwpLeosMcastFilterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 3, 1)
)
_WwpLeosMcastFilterMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosMcastFilterMIBGroups = _WwpLeosMcastFilterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosMcastAddrOverlapNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 7, 2, 0, 1)
)
if mibBuilder.loadTexts:
    wwpLeosMcastAddrOverlapNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-MULTICAST-FILTER-MIB",
    **{"VlanId": VlanId,
       "wwpLeosMcastFilterMIB": wwpLeosMcastFilterMIB,
       "wwpLeosMcastFilterMIBObjects": wwpLeosMcastFilterMIBObjects,
       "wwpLeosMcastFilterConfig": wwpLeosMcastFilterConfig,
       "wwpLeosMcastConfigState": wwpLeosMcastConfigState,
       "wwpLeosMcastFilterActivationTable": wwpLeosMcastFilterActivationTable,
       "wwpLeosMcastFilterActivationEntry": wwpLeosMcastFilterActivationEntry,
       "wwpLeosMcastVlanId": wwpLeosMcastVlanId,
       "wwpLeosMcastFilterAdminState": wwpLeosMcastFilterAdminState,
       "wwpLeosMcastFilterOperState": wwpLeosMcastFilterOperState,
       "wwpLeosMcastFilterState": wwpLeosMcastFilterState,
       "wwpLeosMcastFilterServerPortTable": wwpLeosMcastFilterServerPortTable,
       "wwpLeosMcastFilterServerPortEntry": wwpLeosMcastFilterServerPortEntry,
       "wwpLeosMcastServerPortId": wwpLeosMcastServerPortId,
       "wwpLeosMcastServerPortStatus": wwpLeosMcastServerPortStatus,
       "wwpLeosMcastIgmpSnoopTable": wwpLeosMcastIgmpSnoopTable,
       "wwpLeosMcastIgmpSnoopEntry": wwpLeosMcastIgmpSnoopEntry,
       "wwpLeosMcastIgmpSnoopEnable": wwpLeosMcastIgmpSnoopEnable,
       "wwpLeosMcastIgmpSnoopRobustness": wwpLeosMcastIgmpSnoopRobustness,
       "wwpLeosMcastIgmpSnoopProxyQueryInterval": wwpLeosMcastIgmpSnoopProxyQueryInterval,
       "wwpLeosMcastIgmpSnoopProxyQueryReplyTmo": wwpLeosMcastIgmpSnoopProxyQueryReplyTmo,
       "wwpLeosMcastIgmpSnoopProxyQueryDelay": wwpLeosMcastIgmpSnoopProxyQueryDelay,
       "wwpLeosMcastIgmpSnoopLingerTmo": wwpLeosMcastIgmpSnoopLingerTmo,
       "wwpLeosMcastIgmpQueryEngineState": wwpLeosMcastIgmpQueryEngineState,
       "wwpLeosMcastIgmpProxyQuerySrcIp": wwpLeosMcastIgmpProxyQuerySrcIp,
       "wwpLeosMcastIgmpRouterQueryInterval": wwpLeosMcastIgmpRouterQueryInterval,
       "wwpLeosMcastIgmpMinResponseTime": wwpLeosMcastIgmpMinResponseTime,
       "wwpLeosMcastIgmpDefaultRouterPort": wwpLeosMcastIgmpDefaultRouterPort,
       "wwpLeosMcastIgmpInquisitiveLeaveState": wwpLeosMcastIgmpInquisitiveLeaveState,
       "wwpLeosMcastIgmpLastMemberQueryInterval": wwpLeosMcastIgmpLastMemberQueryInterval,
       "wwpLeosMcastIgmpPriority": wwpLeosMcastIgmpPriority,
       "wwpLeosMcastIgmpSnoopRouterRangeStartIpAddr": wwpLeosMcastIgmpSnoopRouterRangeStartIpAddr,
       "wwpLeosMcastIgmpSnoopRouterRangeEndIpAddr": wwpLeosMcastIgmpSnoopRouterRangeEndIpAddr,
       "wwpLeosMcastIgmpSnoopActiveLingerTimeout": wwpLeosMcastIgmpSnoopActiveLingerTimeout,
       "wwpLeosMcastIgmpSnoopServerTopology": wwpLeosMcastIgmpSnoopServerTopology,
       "wwpLeosMcastIgmpSnoopRapidRecoveryMode": wwpLeosMcastIgmpSnoopRapidRecoveryMode,
       "wwpLeosMcastChannelStreamTable": wwpLeosMcastChannelStreamTable,
       "wwpLeosMcastChannelStreamEntry": wwpLeosMcastChannelStreamEntry,
       "wwpLeosMcastChanelStreamStartGroupAddr": wwpLeosMcastChanelStreamStartGroupAddr,
       "wwpLeosMcastChanelStreamEndGroupAddr": wwpLeosMcastChanelStreamEndGroupAddr,
       "wwpLeosMcastChannelStreamStatus": wwpLeosMcastChannelStreamStatus,
       "wwpLeosMcastFilterConfigTable": wwpLeosMcastFilterConfigTable,
       "wwpLeosMcastFilterConfigEntry": wwpLeosMcastFilterConfigEntry,
       "wwpLeosMcastFilterUPFActivate": wwpLeosMcastFilterUPFActivate,
       "wwpLeosMcastUnresolvedAction": wwpLeosMcastUnresolvedAction,
       "wwpLeosMcastFilterWKMFLocalActivate": wwpLeosMcastFilterWKMFLocalActivate,
       "wwpLeosMcastFilterWKMFInternetActivate": wwpLeosMcastFilterWKMFInternetActivate,
       "wwpLeosMcastFilterWKMFAdhocActivate": wwpLeosMcastFilterWKMFAdhocActivate,
       "wwpLeosMcastFilterWKMFStMulticastActivate": wwpLeosMcastFilterWKMFStMulticastActivate,
       "wwpLeosMcastFilterWKMFSdpSapActivate": wwpLeosMcastFilterWKMFSdpSapActivate,
       "wwpLeosMcastChannelStreamExPortMemTable": wwpLeosMcastChannelStreamExPortMemTable,
       "wwpLeosMcastChannelStreamExPortMemEntry": wwpLeosMcastChannelStreamExPortMemEntry,
       "wwpLeosMcastChannelStreamExPortId": wwpLeosMcastChannelStreamExPortId,
       "wwpLeosMcastChannelStreamExPortMemStatus": wwpLeosMcastChannelStreamExPortMemStatus,
       "wwpLeosMcastSnoopState": wwpLeosMcastSnoopState,
       "wwpLeosMcastGlobalStatsClear": wwpLeosMcastGlobalStatsClear,
       "wwpLeosMcastFilterStatus": wwpLeosMcastFilterStatus,
       "wwpLeosMcastGroupTable": wwpLeosMcastGroupTable,
       "wwpLeosMcastGroupEntry": wwpLeosMcastGroupEntry,
       "wwpLeosMcastGroupAddr": wwpLeosMcastGroupAddr,
       "wwpLeosMcastState": wwpLeosMcastState,
       "wwpLeosMcastType": wwpLeosMcastType,
       "wwpLeosMcastSource": wwpLeosMcastSource,
       "wwpLeosMcastMemberCount": wwpLeosMcastMemberCount,
       "wwpLeosMcastGroupMemberTable": wwpLeosMcastGroupMemberTable,
       "wwpLeosMcastGroupMemberEntry": wwpLeosMcastGroupMemberEntry,
       "wwpLeosMcastPortId": wwpLeosMcastPortId,
       "wwpLeosMcastPortTagId": wwpLeosMcastPortTagId,
       "wwpLeosMcastFilterStats": wwpLeosMcastFilterStats,
       "wwpLeosMcastFilterStatsTable": wwpLeosMcastFilterStatsTable,
       "wwpLeosMcastFilterStatsEntry": wwpLeosMcastFilterStatsEntry,
       "wwpLeosMcastStaticGrpCount": wwpLeosMcastStaticGrpCount,
       "wwpLeosMcastDynamicGrpCount": wwpLeosMcastDynamicGrpCount,
       "wwpLeosMcastJoinMessages": wwpLeosMcastJoinMessages,
       "wwpLeosMcastLeaveMessages": wwpLeosMcastLeaveMessages,
       "wwpLeosMcastQueryMessages": wwpLeosMcastQueryMessages,
       "wwpLeosMcastQueryDiscards": wwpLeosMcastQueryDiscards,
       "wwpLeosMcastQueryTimeouts": wwpLeosMcastQueryTimeouts,
       "wwpLeosMcastUnknownPktType": wwpLeosMcastUnknownPktType,
       "wwpLeosMcastRouterDiscards": wwpLeosMcastRouterDiscards,
       "wwpLeosMcastHostDiscards": wwpLeosMcastHostDiscards,
       "wwpLeosMcastBadChecksum": wwpLeosMcastBadChecksum,
       "wwpLeosMcastL2L3Mismatch": wwpLeosMcastL2L3Mismatch,
       "wwpLeosMcastTotalMembers": wwpLeosMcastTotalMembers,
       "wwpLeosMcastLingerCount": wwpLeosMcastLingerCount,
       "wwpLeosMcastRouterSrcMacAddr": wwpLeosMcastRouterSrcMacAddr,
       "wwpLeosMcastRouterSrcIpAddr": wwpLeosMcastRouterSrcIpAddr,
       "wwpLeosMcastRouterPortId": wwpLeosMcastRouterPortId,
       "wwpLeosMcastReportSendPortId": wwpLeosMcastReportSendPortId,
       "wwpLeosMcastStatsClear": wwpLeosMcastStatsClear,
       "wwpLeosMcastStatsQuerySrcIpZeroDiscard": wwpLeosMcastStatsQuerySrcIpZeroDiscard,
       "wwpLeosMcastFilterMIBNotificationPrefix": wwpLeosMcastFilterMIBNotificationPrefix,
       "wwpLeosMcastFilterMIBNotifications": wwpLeosMcastFilterMIBNotifications,
       "wwpLeosMcastAddrOverlapNotification": wwpLeosMcastAddrOverlapNotification,
       "wwpLeosMcastFilterMIBConformance": wwpLeosMcastFilterMIBConformance,
       "wwpLeosMcastFilterMIBCompliances": wwpLeosMcastFilterMIBCompliances,
       "wwpLeosMcastFilterMIBGroups": wwpLeosMcastFilterMIBGroups}
)
