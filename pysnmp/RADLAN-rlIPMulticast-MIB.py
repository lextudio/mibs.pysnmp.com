# SNMP MIB module (RADLAN-rlIPMulticast-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-rlIPMulticast-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:09 2024
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

(rnd,
 rndErrorDesc,
 rndErrorSeverity,
 rndNotifications) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd",
    "rndErrorDesc",
    "rndErrorSeverity",
    "rndNotifications")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rlIPmulticast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 46)
)
rlIPmulticast.setRevisions(
        ("2004-04-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlIpmRouterEnable_Type(Integer32):
    """Custom type rlIpmRouterEnable based on Integer32"""
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


_RlIpmRouterEnable_Type.__name__ = "Integer32"
_RlIpmRouterEnable_Object = MibScalar
rlIpmRouterEnable = _RlIpmRouterEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 1),
    _RlIpmRouterEnable_Type()
)
rlIpmRouterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpmRouterEnable.setStatus("current")
_RlIgmp_ObjectIdentity = ObjectIdentity
rlIgmp = _RlIgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 46, 2)
)
_RlIgmpMibVersion_Type = Integer32
_RlIgmpMibVersion_Object = MibScalar
rlIgmpMibVersion = _RlIgmpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 2, 1),
    _RlIgmpMibVersion_Type()
)
rlIgmpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMibVersion.setStatus("current")
_RlPim_ObjectIdentity = ObjectIdentity
rlPim = _RlPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 46, 3)
)
_RlPimMibVersion_Type = Integer32
_RlPimMibVersion_Object = MibScalar
rlPimMibVersion = _RlPimMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 3, 2),
    _RlPimMibVersion_Type()
)
rlPimMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimMibVersion.setStatus("current")


class _RlPimEnable_Type(Integer32):
    """Custom type rlPimEnable based on Integer32"""
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


_RlPimEnable_Type.__name__ = "Integer32"
_RlPimEnable_Object = MibScalar
rlPimEnable = _RlPimEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 3, 7),
    _RlPimEnable_Type()
)
rlPimEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPimEnable.setStatus("current")
_RlDvmrp_ObjectIdentity = ObjectIdentity
rlDvmrp = _RlDvmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 46, 4)
)
_RlIgmpProxy_ObjectIdentity = ObjectIdentity
rlIgmpProxy = _RlIgmpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 46, 5)
)


class _RlIgmpProxyEnable_Type(Integer32):
    """Custom type rlIgmpProxyEnable based on Integer32"""
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


_RlIgmpProxyEnable_Type.__name__ = "Integer32"
_RlIgmpProxyEnable_Object = MibScalar
rlIgmpProxyEnable = _RlIgmpProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 5, 1),
    _RlIgmpProxyEnable_Type()
)
rlIgmpProxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpProxyEnable.setStatus("current")
_RlIgmpFilter_ObjectIdentity = ObjectIdentity
rlIgmpFilter = _RlIgmpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 46, 6)
)


class _RlIgmpFilterEnable_Type(Integer32):
    """Custom type rlIgmpFilterEnable based on Integer32"""
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


_RlIgmpFilterEnable_Type.__name__ = "Integer32"
_RlIgmpFilterEnable_Object = MibScalar
rlIgmpFilterEnable = _RlIgmpFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 6, 1),
    _RlIgmpFilterEnable_Type()
)
rlIgmpFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpFilterEnable.setStatus("current")
_RlIgmpFilterTable_Object = MibTable
rlIgmpFilterTable = _RlIgmpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 6, 2)
)
if mibBuilder.loadTexts:
    rlIgmpFilterTable.setStatus("current")
_RlIgmpFilterEntry_Object = MibTableRow
rlIgmpFilterEntry = _RlIgmpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 6, 2, 1)
)
rlIgmpFilterEntry.setIndexNames(
    (0, "RADLAN-rlIPMulticast-MIB", "rlIgmpFilterIfIndex"),
    (0, "RADLAN-rlIPMulticast-MIB", "rlIgmpFilterAddressFrom"),
    (0, "RADLAN-rlIPMulticast-MIB", "rlIgmpFilterAddressTo"),
)
if mibBuilder.loadTexts:
    rlIgmpFilterEntry.setStatus("current")
_RlIgmpFilterIfIndex_Type = InterfaceIndex
_RlIgmpFilterIfIndex_Object = MibTableColumn
rlIgmpFilterIfIndex = _RlIgmpFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 6, 2, 1, 1),
    _RlIgmpFilterIfIndex_Type()
)
rlIgmpFilterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIgmpFilterIfIndex.setStatus("current")
_RlIgmpFilterAddressFrom_Type = IpAddress
_RlIgmpFilterAddressFrom_Object = MibTableColumn
rlIgmpFilterAddressFrom = _RlIgmpFilterAddressFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 6, 2, 1, 2),
    _RlIgmpFilterAddressFrom_Type()
)
rlIgmpFilterAddressFrom.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIgmpFilterAddressFrom.setStatus("current")
_RlIgmpFilterAddressTo_Type = IpAddress
_RlIgmpFilterAddressTo_Object = MibTableColumn
rlIgmpFilterAddressTo = _RlIgmpFilterAddressTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 6, 2, 1, 3),
    _RlIgmpFilterAddressTo_Type()
)
rlIgmpFilterAddressTo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIgmpFilterAddressTo.setStatus("current")
_RlIgmpFilterUpTime_Type = TimeTicks
_RlIgmpFilterUpTime_Object = MibTableColumn
rlIgmpFilterUpTime = _RlIgmpFilterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 6, 2, 1, 4),
    _RlIgmpFilterUpTime_Type()
)
rlIgmpFilterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpFilterUpTime.setStatus("current")
_RlIgmpFilterStatus_Type = RowStatus
_RlIgmpFilterStatus_Object = MibTableColumn
rlIgmpFilterStatus = _RlIgmpFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 6, 2, 1, 5),
    _RlIgmpFilterStatus_Type()
)
rlIgmpFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpFilterStatus.setStatus("current")


class _RlIgmpFilterAction_Type(Integer32):
    """Custom type rlIgmpFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RlIgmpFilterAction_Type.__name__ = "Integer32"
_RlIgmpFilterAction_Object = MibTableColumn
rlIgmpFilterAction = _RlIgmpFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 6, 2, 1, 6),
    _RlIgmpFilterAction_Type()
)
rlIgmpFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpFilterAction.setStatus("current")
_RlPimSM_ObjectIdentity = ObjectIdentity
rlPimSM = _RlPimSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 46, 7)
)


class _RlPimSMEnable_Type(Integer32):
    """Custom type rlPimSMEnable based on Integer32"""
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


_RlPimSMEnable_Type.__name__ = "Integer32"
_RlPimSMEnable_Object = MibScalar
rlPimSMEnable = _RlPimSMEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 7, 1),
    _RlPimSMEnable_Type()
)
rlPimSMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPimSMEnable.setStatus("current")
_RlPimSMMibVersion_Type = Integer32
_RlPimSMMibVersion_Object = MibScalar
rlPimSMMibVersion = _RlPimSMMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 7, 2),
    _RlPimSMMibVersion_Type()
)
rlPimSMMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPimSMMibVersion.setStatus("current")


class _RlPimSMDREnable_Type(Integer32):
    """Custom type rlPimSMDREnable based on Integer32"""
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


_RlPimSMDREnable_Type.__name__ = "Integer32"
_RlPimSMDREnable_Object = MibScalar
rlPimSMDREnable = _RlPimSMDREnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 7, 4),
    _RlPimSMDREnable_Type()
)
rlPimSMDREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPimSMDREnable.setStatus("current")


class _RlPimSMDirectedConnectedSourceEnable_Type(Integer32):
    """Custom type rlPimSMDirectedConnectedSourceEnable based on Integer32"""
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


_RlPimSMDirectedConnectedSourceEnable_Type.__name__ = "Integer32"
_RlPimSMDirectedConnectedSourceEnable_Object = MibScalar
rlPimSMDirectedConnectedSourceEnable = _RlPimSMDirectedConnectedSourceEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 7, 5),
    _RlPimSMDirectedConnectedSourceEnable_Type()
)
rlPimSMDirectedConnectedSourceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPimSMDirectedConnectedSourceEnable.setStatus("current")


class _RlPimSMRPEnable_Type(Integer32):
    """Custom type rlPimSMRPEnable based on Integer32"""
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


_RlPimSMRPEnable_Type.__name__ = "Integer32"
_RlPimSMRPEnable_Object = MibScalar
rlPimSMRPEnable = _RlPimSMRPEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 7, 6),
    _RlPimSMRPEnable_Type()
)
rlPimSMRPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPimSMRPEnable.setStatus("current")


class _RlPimSMSPTSwitchEnable_Type(Integer32):
    """Custom type rlPimSMSPTSwitchEnable based on Integer32"""
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


_RlPimSMSPTSwitchEnable_Type.__name__ = "Integer32"
_RlPimSMSPTSwitchEnable_Object = MibScalar
rlPimSMSPTSwitchEnable = _RlPimSMSPTSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 7, 7),
    _RlPimSMSPTSwitchEnable_Type()
)
rlPimSMSPTSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPimSMSPTSwitchEnable.setStatus("current")


class _RlPimSmRPSetConfigurationType_Type(Integer32):
    """Custom type rlPimSmRPSetConfigurationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootstrap", 2),
          ("manual", 1))
    )


_RlPimSmRPSetConfigurationType_Type.__name__ = "Integer32"
_RlPimSmRPSetConfigurationType_Object = MibScalar
rlPimSmRPSetConfigurationType = _RlPimSmRPSetConfigurationType_Object(
    (1, 3, 6, 1, 4, 1, 89, 46, 7, 8),
    _RlPimSmRPSetConfigurationType_Type()
)
rlPimSmRPSetConfigurationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPimSmRPSetConfigurationType.setStatus("current")

# Managed Objects groups


# Notification objects

rlIgmpTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 143)
)
rlIgmpTableOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIgmpTableOverflow.setStatus(
        "current"
    )

rlPimTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 144)
)
rlPimTableOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPimTableOverflow.setStatus(
        "current"
    )

rlPimSmInterfaceTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 163)
)
rlPimSmInterfaceTableOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPimSmInterfaceTableOverflow.setStatus(
        "current"
    )

rlPimSmNextHopTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 164)
)
rlPimSmNextHopTableOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPimSmNextHopTableOverflow.setStatus(
        "current"
    )

rlPimSmMulticastRouteTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 165)
)
rlPimSmMulticastRouteTableOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPimSmMulticastRouteTableOverflow.setStatus(
        "current"
    )

rlPimSmTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 166)
)
rlPimSmTableOverflow.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPimSmTableOverflow.setStatus(
        "current"
    )

rlPimSmSrcUnreacable = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 167)
)
rlPimSmSrcUnreacable.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPimSmSrcUnreacable.setStatus(
        "current"
    )

rlPimSmParallelPathToLAN = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 168)
)
rlPimSmParallelPathToLAN.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPimSmParallelPathToLAN.setStatus(
        "current"
    )

rlPimSmNotSMUpstreamNeighbor = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 169)
)
rlPimSmNotSMUpstreamNeighbor.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPimSmNotSMUpstreamNeighbor.setStatus(
        "current"
    )

rlIpmAddOutgoingInterfaceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 182)
)
rlIpmAddOutgoingInterfaceFailed.setObjects(
      *(("RADLAN-MIB", "rndErrorDesc"),
        ("RADLAN-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIpmAddOutgoingInterfaceFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-rlIPMulticast-MIB",
    **{"rlIgmpTableOverflow": rlIgmpTableOverflow,
       "rlPimTableOverflow": rlPimTableOverflow,
       "rlPimSmInterfaceTableOverflow": rlPimSmInterfaceTableOverflow,
       "rlPimSmNextHopTableOverflow": rlPimSmNextHopTableOverflow,
       "rlPimSmMulticastRouteTableOverflow": rlPimSmMulticastRouteTableOverflow,
       "rlPimSmTableOverflow": rlPimSmTableOverflow,
       "rlPimSmSrcUnreacable": rlPimSmSrcUnreacable,
       "rlPimSmParallelPathToLAN": rlPimSmParallelPathToLAN,
       "rlPimSmNotSMUpstreamNeighbor": rlPimSmNotSMUpstreamNeighbor,
       "rlIpmAddOutgoingInterfaceFailed": rlIpmAddOutgoingInterfaceFailed,
       "rlIPmulticast": rlIPmulticast,
       "rlIpmRouterEnable": rlIpmRouterEnable,
       "rlIgmp": rlIgmp,
       "rlIgmpMibVersion": rlIgmpMibVersion,
       "rlPim": rlPim,
       "rlPimMibVersion": rlPimMibVersion,
       "rlPimEnable": rlPimEnable,
       "rlDvmrp": rlDvmrp,
       "rlIgmpProxy": rlIgmpProxy,
       "rlIgmpProxyEnable": rlIgmpProxyEnable,
       "rlIgmpFilter": rlIgmpFilter,
       "rlIgmpFilterEnable": rlIgmpFilterEnable,
       "rlIgmpFilterTable": rlIgmpFilterTable,
       "rlIgmpFilterEntry": rlIgmpFilterEntry,
       "rlIgmpFilterIfIndex": rlIgmpFilterIfIndex,
       "rlIgmpFilterAddressFrom": rlIgmpFilterAddressFrom,
       "rlIgmpFilterAddressTo": rlIgmpFilterAddressTo,
       "rlIgmpFilterUpTime": rlIgmpFilterUpTime,
       "rlIgmpFilterStatus": rlIgmpFilterStatus,
       "rlIgmpFilterAction": rlIgmpFilterAction,
       "rlPimSM": rlPimSM,
       "rlPimSMEnable": rlPimSMEnable,
       "rlPimSMMibVersion": rlPimSMMibVersion,
       "rlPimSMDREnable": rlPimSMDREnable,
       "rlPimSMDirectedConnectedSourceEnable": rlPimSMDirectedConnectedSourceEnable,
       "rlPimSMRPEnable": rlPimSMRPEnable,
       "rlPimSMSPTSwitchEnable": rlPimSMSPTSwitchEnable,
       "rlPimSmRPSetConfigurationType": rlPimSmRPSetConfigurationType}
)
