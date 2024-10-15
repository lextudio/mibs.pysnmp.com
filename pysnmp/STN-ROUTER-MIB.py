# SNMP MIB module (STN-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:01 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(stnNotification,
 stnSystems) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification",
    "stnSystems")

(stnEngineCpu,
 stnEngineIndex,
 stnEngineSlot) = mibBuilder.importSymbols(
    "STN-CHASSIS-MIB",
    "stnEngineCpu",
    "stnEngineIndex",
    "stnEngineSlot")


# MODULE-IDENTITY

stnRouter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceConnectionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("customer", 1),
          ("home", 6),
          ("ppp", 4),
          ("pppoe", 5),
          ("provider", 2))
    )



class OperationState(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 4),
          ("assignpend", 3),
          ("bufpend", 2),
          ("error", 8),
          ("failedassign", 7),
          ("unassignbufpend", 5),
          ("unassigned", 1),
          ("unassignpend", 6))
    )



# MIB Managed Objects in the order of their OIDs

_StnRouterObjects_ObjectIdentity = ObjectIdentity
stnRouterObjects = _StnRouterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1)
)
_StnRouterTable_Object = MibTable
stnRouterTable = _StnRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    stnRouterTable.setStatus("current")
_StnRouterEntry_Object = MibTableRow
stnRouterEntry = _StnRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1)
)
stnRouterEntry.setIndexNames(
    (0, "STN-ROUTER-MIB", "stnRouterIndex"),
)
if mibBuilder.loadTexts:
    stnRouterEntry.setStatus("current")
_StnRouterIndex_Type = Integer32
_StnRouterIndex_Object = MibTableColumn
stnRouterIndex = _StnRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 1),
    _StnRouterIndex_Type()
)
stnRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterIndex.setStatus("current")


class _StnRouterType_Type(Integer32):
    """Custom type stnRouterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admin", 3),
          ("customer", 1),
          ("provider", 2))
    )


_StnRouterType_Type.__name__ = "Integer32"
_StnRouterType_Object = MibTableColumn
stnRouterType = _StnRouterType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 2),
    _StnRouterType_Type()
)
stnRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterType.setStatus("current")
_StnRouterState_Type = OperationState
_StnRouterState_Object = MibTableColumn
stnRouterState = _StnRouterState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 3),
    _StnRouterState_Type()
)
stnRouterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterState.setStatus("current")
_StnRouterEngineID_Type = Integer32
_StnRouterEngineID_Object = MibTableColumn
stnRouterEngineID = _StnRouterEngineID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 4),
    _StnRouterEngineID_Type()
)
stnRouterEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterEngineID.setStatus("current")
_StnRouterHomeIpAddress_Type = IpAddress
_StnRouterHomeIpAddress_Object = MibTableColumn
stnRouterHomeIpAddress = _StnRouterHomeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 5),
    _StnRouterHomeIpAddress_Type()
)
stnRouterHomeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterHomeIpAddress.setStatus("current")


class _StnRouterEnabled_Type(Integer32):
    """Custom type stnRouterEnabled based on Integer32"""
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


_StnRouterEnabled_Type.__name__ = "Integer32"
_StnRouterEnabled_Object = MibTableColumn
stnRouterEnabled = _StnRouterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 6),
    _StnRouterEnabled_Type()
)
stnRouterEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterEnabled.setStatus("current")


class _StnRouterName_Type(DisplayString):
    """Custom type stnRouterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StnRouterName_Type.__name__ = "DisplayString"
_StnRouterName_Object = MibTableColumn
stnRouterName = _StnRouterName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 7),
    _StnRouterName_Type()
)
stnRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterName.setStatus("current")
_StnRouterUpTime_Type = TimeTicks
_StnRouterUpTime_Object = MibTableColumn
stnRouterUpTime = _StnRouterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 8),
    _StnRouterUpTime_Type()
)
stnRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterUpTime.setStatus("current")
_StnRouterActiveSlot_Type = Integer32
_StnRouterActiveSlot_Object = MibTableColumn
stnRouterActiveSlot = _StnRouterActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 9),
    _StnRouterActiveSlot_Type()
)
stnRouterActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterActiveSlot.setStatus("current")
_StnRouterActiveCpu_Type = Integer32
_StnRouterActiveCpu_Object = MibTableColumn
stnRouterActiveCpu = _StnRouterActiveCpu_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 10),
    _StnRouterActiveCpu_Type()
)
stnRouterActiveCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterActiveCpu.setStatus("current")
_StnRouterConfiguredSlot_Type = Integer32
_StnRouterConfiguredSlot_Object = MibTableColumn
stnRouterConfiguredSlot = _StnRouterConfiguredSlot_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 11),
    _StnRouterConfiguredSlot_Type()
)
stnRouterConfiguredSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterConfiguredSlot.setStatus("current")
_StnRouterConfiguredCpu_Type = Integer32
_StnRouterConfiguredCpu_Object = MibTableColumn
stnRouterConfiguredCpu = _StnRouterConfiguredCpu_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 12),
    _StnRouterConfiguredCpu_Type()
)
stnRouterConfiguredCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterConfiguredCpu.setStatus("current")
_StnRouterStandbySlot_Type = Integer32
_StnRouterStandbySlot_Object = MibTableColumn
stnRouterStandbySlot = _StnRouterStandbySlot_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 13),
    _StnRouterStandbySlot_Type()
)
stnRouterStandbySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterStandbySlot.setStatus("current")
_StnRouterStandbyCpu_Type = Integer32
_StnRouterStandbyCpu_Object = MibTableColumn
stnRouterStandbyCpu = _StnRouterStandbyCpu_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 14),
    _StnRouterStandbyCpu_Type()
)
stnRouterStandbyCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterStandbyCpu.setStatus("current")


class _StnRouterReassignOnFault_Type(Integer32):
    """Custom type stnRouterReassignOnFault based on Integer32"""
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


_StnRouterReassignOnFault_Type.__name__ = "Integer32"
_StnRouterReassignOnFault_Object = MibTableColumn
stnRouterReassignOnFault = _StnRouterReassignOnFault_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 15),
    _StnRouterReassignOnFault_Type()
)
stnRouterReassignOnFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterReassignOnFault.setStatus("current")


class _StnRouterServiceName_Type(DisplayString):
    """Custom type stnRouterServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_StnRouterServiceName_Type.__name__ = "DisplayString"
_StnRouterServiceName_Object = MibTableColumn
stnRouterServiceName = _StnRouterServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 16),
    _StnRouterServiceName_Type()
)
stnRouterServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterServiceName.setStatus("current")
_StnRouterServiceDomain_Type = Integer32
_StnRouterServiceDomain_Object = MibTableColumn
stnRouterServiceDomain = _StnRouterServiceDomain_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 17),
    _StnRouterServiceDomain_Type()
)
stnRouterServiceDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterServiceDomain.setStatus("current")


class _StnRouterDefaultPolicyAction_Type(Integer32):
    """Custom type stnRouterDefaultPolicyAction based on Integer32"""
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


_StnRouterDefaultPolicyAction_Type.__name__ = "Integer32"
_StnRouterDefaultPolicyAction_Object = MibTableColumn
stnRouterDefaultPolicyAction = _StnRouterDefaultPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 18),
    _StnRouterDefaultPolicyAction_Type()
)
stnRouterDefaultPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRouterDefaultPolicyAction.setStatus("current")
_StnSubnetInterfaceTable_Object = MibTable
stnSubnetInterfaceTable = _StnSubnetInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    stnSubnetInterfaceTable.setStatus("current")
_StnSubnetInterfaceEntry_Object = MibTableRow
stnSubnetInterfaceEntry = _StnSubnetInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1)
)
stnSubnetInterfaceEntry.setIndexNames(
    (0, "STN-ROUTER-MIB", "stnSubnetInterfaceIndex"),
)
if mibBuilder.loadTexts:
    stnSubnetInterfaceEntry.setStatus("current")
_StnSubnetInterfaceIndex_Type = Unsigned32
_StnSubnetInterfaceIndex_Object = MibTableColumn
stnSubnetInterfaceIndex = _StnSubnetInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 1),
    _StnSubnetInterfaceIndex_Type()
)
stnSubnetInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubnetInterfaceIndex.setStatus("current")


class _StnSubnetInterfaceEnabled_Type(Integer32):
    """Custom type stnSubnetInterfaceEnabled based on Integer32"""
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


_StnSubnetInterfaceEnabled_Type.__name__ = "Integer32"
_StnSubnetInterfaceEnabled_Object = MibTableColumn
stnSubnetInterfaceEnabled = _StnSubnetInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 2),
    _StnSubnetInterfaceEnabled_Type()
)
stnSubnetInterfaceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubnetInterfaceEnabled.setStatus("current")
_StnSubnetInterfaceAddress_Type = IpAddress
_StnSubnetInterfaceAddress_Object = MibTableColumn
stnSubnetInterfaceAddress = _StnSubnetInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 3),
    _StnSubnetInterfaceAddress_Type()
)
stnSubnetInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubnetInterfaceAddress.setStatus("current")
_StnSubnetInterfaceMask_Type = IpAddress
_StnSubnetInterfaceMask_Object = MibTableColumn
stnSubnetInterfaceMask = _StnSubnetInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 4),
    _StnSubnetInterfaceMask_Type()
)
stnSubnetInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubnetInterfaceMask.setStatus("current")
_StnSubnetInterfaceVclid_Type = Integer32
_StnSubnetInterfaceVclid_Object = MibTableColumn
stnSubnetInterfaceVclid = _StnSubnetInterfaceVclid_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 5),
    _StnSubnetInterfaceVclid_Type()
)
stnSubnetInterfaceVclid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubnetInterfaceVclid.setStatus("deprecated")
_StnSubnetInterfaceType_Type = InterfaceConnectionType
_StnSubnetInterfaceType_Object = MibTableColumn
stnSubnetInterfaceType = _StnSubnetInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 6),
    _StnSubnetInterfaceType_Type()
)
stnSubnetInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubnetInterfaceType.setStatus("current")
_StnSubnetInterfaceState_Type = OperationState
_StnSubnetInterfaceState_Object = MibTableColumn
stnSubnetInterfaceState = _StnSubnetInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 7),
    _StnSubnetInterfaceState_Type()
)
stnSubnetInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubnetInterfaceState.setStatus("current")
_StnSubnetInterfaceRouterIndex_Type = Integer32
_StnSubnetInterfaceRouterIndex_Object = MibTableColumn
stnSubnetInterfaceRouterIndex = _StnSubnetInterfaceRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 8),
    _StnSubnetInterfaceRouterIndex_Type()
)
stnSubnetInterfaceRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubnetInterfaceRouterIndex.setStatus("current")


class _StnSubnetInterfaceLinkType_Type(Integer32):
    """Custom type stnSubnetInterfaceLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("home", 3),
          ("vcLink", 1),
          ("vei", 2))
    )


_StnSubnetInterfaceLinkType_Type.__name__ = "Integer32"
_StnSubnetInterfaceLinkType_Object = MibTableColumn
stnSubnetInterfaceLinkType = _StnSubnetInterfaceLinkType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 9),
    _StnSubnetInterfaceLinkType_Type()
)
stnSubnetInterfaceLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubnetInterfaceLinkType.setStatus("current")
_StnSubnetInterfaceLinkInstance_Type = Integer32
_StnSubnetInterfaceLinkInstance_Object = MibTableColumn
stnSubnetInterfaceLinkInstance = _StnSubnetInterfaceLinkInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 10),
    _StnSubnetInterfaceLinkInstance_Type()
)
stnSubnetInterfaceLinkInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubnetInterfaceLinkInstance.setStatus("current")
_StnSubnetInterfaceForcedNextHop_Type = IpAddress
_StnSubnetInterfaceForcedNextHop_Object = MibTableColumn
stnSubnetInterfaceForcedNextHop = _StnSubnetInterfaceForcedNextHop_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 11),
    _StnSubnetInterfaceForcedNextHop_Type()
)
stnSubnetInterfaceForcedNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubnetInterfaceForcedNextHop.setStatus("current")


class _StnSubnetInterfaceServiceName_Type(DisplayString):
    """Custom type stnSubnetInterfaceServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_StnSubnetInterfaceServiceName_Type.__name__ = "DisplayString"
_StnSubnetInterfaceServiceName_Object = MibTableColumn
stnSubnetInterfaceServiceName = _StnSubnetInterfaceServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 12),
    _StnSubnetInterfaceServiceName_Type()
)
stnSubnetInterfaceServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubnetInterfaceServiceName.setStatus("current")
_StnPppoeTable_Object = MibTable
stnPppoeTable = _StnPppoeTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    stnPppoeTable.setStatus("current")
_StnPppoeEntry_Object = MibTableRow
stnPppoeEntry = _StnPppoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1)
)
stnPppoeEntry.setIndexNames(
    (0, "STN-ROUTER-MIB", "stnPppoeIndex"),
)
if mibBuilder.loadTexts:
    stnPppoeEntry.setStatus("current")
_StnPppoeIndex_Type = Integer32
_StnPppoeIndex_Object = MibTableColumn
stnPppoeIndex = _StnPppoeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 1),
    _StnPppoeIndex_Type()
)
stnPppoeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppoeIndex.setStatus("current")
_StnPppoeType_Type = InterfaceConnectionType
_StnPppoeType_Object = MibTableColumn
stnPppoeType = _StnPppoeType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 2),
    _StnPppoeType_Type()
)
stnPppoeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppoeType.setStatus("current")
_StnPppoeState_Type = OperationState
_StnPppoeState_Object = MibTableColumn
stnPppoeState = _StnPppoeState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 3),
    _StnPppoeState_Type()
)
stnPppoeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppoeState.setStatus("current")
_StnPppoeVclid_Type = Integer32
_StnPppoeVclid_Object = MibTableColumn
stnPppoeVclid = _StnPppoeVclid_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 4),
    _StnPppoeVclid_Type()
)
stnPppoeVclid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppoeVclid.setStatus("deprecated")
_StnPppoeIfIndex_Type = InterfaceIndex
_StnPppoeIfIndex_Object = MibTableColumn
stnPppoeIfIndex = _StnPppoeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 5),
    _StnPppoeIfIndex_Type()
)
stnPppoeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppoeIfIndex.setStatus("current")
_StnPppoeRouterIndex_Type = Integer32
_StnPppoeRouterIndex_Object = MibTableColumn
stnPppoeRouterIndex = _StnPppoeRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 6),
    _StnPppoeRouterIndex_Type()
)
stnPppoeRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppoeRouterIndex.setStatus("current")


class _StnPppoeLinkType_Type(Integer32):
    """Custom type stnPppoeLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vcLink", 1),
          ("vei", 2))
    )


_StnPppoeLinkType_Type.__name__ = "Integer32"
_StnPppoeLinkType_Object = MibTableColumn
stnPppoeLinkType = _StnPppoeLinkType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 7),
    _StnPppoeLinkType_Type()
)
stnPppoeLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppoeLinkType.setStatus("current")
_StnPppoeLinkInstance_Type = Integer32
_StnPppoeLinkInstance_Object = MibTableColumn
stnPppoeLinkInstance = _StnPppoeLinkInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 8),
    _StnPppoeLinkInstance_Type()
)
stnPppoeLinkInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppoeLinkInstance.setStatus("current")
_StnPppTable_Object = MibTable
stnPppTable = _StnPppTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    stnPppTable.setStatus("current")
_StnPppEntry_Object = MibTableRow
stnPppEntry = _StnPppEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1)
)
stnPppEntry.setIndexNames(
    (0, "STN-ROUTER-MIB", "stnPppIndex"),
)
if mibBuilder.loadTexts:
    stnPppEntry.setStatus("current")
_StnPppIndex_Type = Integer32
_StnPppIndex_Object = MibTableColumn
stnPppIndex = _StnPppIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1, 1),
    _StnPppIndex_Type()
)
stnPppIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppIndex.setStatus("current")
_StnPppType_Type = InterfaceConnectionType
_StnPppType_Object = MibTableColumn
stnPppType = _StnPppType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1, 2),
    _StnPppType_Type()
)
stnPppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppType.setStatus("current")
_StnPppState_Type = OperationState
_StnPppState_Object = MibTableColumn
stnPppState = _StnPppState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1, 3),
    _StnPppState_Type()
)
stnPppState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppState.setStatus("current")
_StnPppVclid_Type = Integer32
_StnPppVclid_Object = MibTableColumn
stnPppVclid = _StnPppVclid_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1, 4),
    _StnPppVclid_Type()
)
stnPppVclid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppVclid.setStatus("current")
_StnPppIfIndex_Type = InterfaceIndex
_StnPppIfIndex_Object = MibTableColumn
stnPppIfIndex = _StnPppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1, 5),
    _StnPppIfIndex_Type()
)
stnPppIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppIfIndex.setStatus("current")
_StnPppRouterIndex_Type = Integer32
_StnPppRouterIndex_Object = MibTableColumn
stnPppRouterIndex = _StnPppRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1, 6),
    _StnPppRouterIndex_Type()
)
stnPppRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPppRouterIndex.setStatus("current")
_StnRouterNAT_ObjectIdentity = ObjectIdentity
stnRouterNAT = _StnRouterNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5)
)
_StnRouterVEI_ObjectIdentity = ObjectIdentity
stnRouterVEI = _StnRouterVEI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6)
)
_StnRouterAtmVpn_ObjectIdentity = ObjectIdentity
stnRouterAtmVpn = _StnRouterAtmVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7)
)
_StnRouterVimuxMpls_ObjectIdentity = ObjectIdentity
stnRouterVimuxMpls = _StnRouterVimuxMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8)
)
_StnRouterVTI_ObjectIdentity = ObjectIdentity
stnRouterVTI = _StnRouterVTI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9)
)
_StnRouterMibConformance_ObjectIdentity = ObjectIdentity
stnRouterMibConformance = _StnRouterMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 2)
)

# Managed Objects groups


# Notification objects

stnRouterUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 26)
)
stnRouterUp.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-ROUTER-MIB", "stnRouterState"),
        ("STN-ROUTER-MIB", "stnRouterName"),
        ("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnRouterUp.setStatus(
        "current"
    )

stnRouterDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 27)
)
stnRouterDown.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-ROUTER-MIB", "stnRouterState"),
        ("STN-ROUTER-MIB", "stnRouterName"),
        ("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnRouterDown.setStatus(
        "current"
    )

stnRouterReassigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 28)
)
stnRouterReassigned.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-ROUTER-MIB", "stnRouterState"),
        ("STN-ROUTER-MIB", "stnRouterName"),
        ("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnRouterReassigned.setStatus(
        "current"
    )

stnRouterReassignFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 29)
)
stnRouterReassignFailure.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-ROUTER-MIB", "stnRouterState"),
        ("STN-ROUTER-MIB", "stnRouterName"),
        ("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnRouterReassignFailure.setStatus(
        "current"
    )

stnSubnetIfAssignFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 30)
)
stnSubnetIfAssignFailure.setObjects(
      *(("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"),
        ("STN-ROUTER-MIB", "stnSubnetInterfaceAddress"),
        ("STN-ROUTER-MIB", "stnSubnetInterfaceVclid"),
        ("STN-ROUTER-MIB", "stnSubnetInterfaceState"),
        ("STN-ROUTER-MIB", "stnSubnetInterfaceRouterIndex"),
        ("STN-ROUTER-MIB", "stnSubnetInterfaceLinkType"),
        ("STN-ROUTER-MIB", "stnSubnetInterfaceLinkInstance"))
)
if mibBuilder.loadTexts:
    stnSubnetIfAssignFailure.setStatus(
        "current"
    )

stnConfigAuditRouterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 33)
)
stnConfigAuditRouterFailure.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"),
        ("STN-ROUTER-MIB", "stnRouterIndex"))
)
if mibBuilder.loadTexts:
    stnConfigAuditRouterFailure.setStatus(
        "current"
    )

stnConfigAuditSubnetIfFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 34)
)
stnConfigAuditSubnetIfFailure.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"),
        ("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"))
)
if mibBuilder.loadTexts:
    stnConfigAuditSubnetIfFailure.setStatus(
        "current"
    )

stnConfigAuditPppoeIfFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 35)
)
stnConfigAuditPppoeIfFailure.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"),
        ("STN-ROUTER-MIB", "stnPppoeRouterIndex"))
)
if mibBuilder.loadTexts:
    stnConfigAuditPppoeIfFailure.setStatus(
        "current"
    )

stnConfigAuditPppIfFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 36)
)
stnConfigAuditPppIfFailure.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"),
        ("STN-ROUTER-MIB", "stnPppRouterIndex"))
)
if mibBuilder.loadTexts:
    stnConfigAuditPppIfFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-ROUTER-MIB",
    **{"InterfaceConnectionType": InterfaceConnectionType,
       "OperationState": OperationState,
       "stnRouter": stnRouter,
       "stnRouterObjects": stnRouterObjects,
       "stnRouterTable": stnRouterTable,
       "stnRouterEntry": stnRouterEntry,
       "stnRouterIndex": stnRouterIndex,
       "stnRouterType": stnRouterType,
       "stnRouterState": stnRouterState,
       "stnRouterEngineID": stnRouterEngineID,
       "stnRouterHomeIpAddress": stnRouterHomeIpAddress,
       "stnRouterEnabled": stnRouterEnabled,
       "stnRouterName": stnRouterName,
       "stnRouterUpTime": stnRouterUpTime,
       "stnRouterActiveSlot": stnRouterActiveSlot,
       "stnRouterActiveCpu": stnRouterActiveCpu,
       "stnRouterConfiguredSlot": stnRouterConfiguredSlot,
       "stnRouterConfiguredCpu": stnRouterConfiguredCpu,
       "stnRouterStandbySlot": stnRouterStandbySlot,
       "stnRouterStandbyCpu": stnRouterStandbyCpu,
       "stnRouterReassignOnFault": stnRouterReassignOnFault,
       "stnRouterServiceName": stnRouterServiceName,
       "stnRouterServiceDomain": stnRouterServiceDomain,
       "stnRouterDefaultPolicyAction": stnRouterDefaultPolicyAction,
       "stnSubnetInterfaceTable": stnSubnetInterfaceTable,
       "stnSubnetInterfaceEntry": stnSubnetInterfaceEntry,
       "stnSubnetInterfaceIndex": stnSubnetInterfaceIndex,
       "stnSubnetInterfaceEnabled": stnSubnetInterfaceEnabled,
       "stnSubnetInterfaceAddress": stnSubnetInterfaceAddress,
       "stnSubnetInterfaceMask": stnSubnetInterfaceMask,
       "stnSubnetInterfaceVclid": stnSubnetInterfaceVclid,
       "stnSubnetInterfaceType": stnSubnetInterfaceType,
       "stnSubnetInterfaceState": stnSubnetInterfaceState,
       "stnSubnetInterfaceRouterIndex": stnSubnetInterfaceRouterIndex,
       "stnSubnetInterfaceLinkType": stnSubnetInterfaceLinkType,
       "stnSubnetInterfaceLinkInstance": stnSubnetInterfaceLinkInstance,
       "stnSubnetInterfaceForcedNextHop": stnSubnetInterfaceForcedNextHop,
       "stnSubnetInterfaceServiceName": stnSubnetInterfaceServiceName,
       "stnPppoeTable": stnPppoeTable,
       "stnPppoeEntry": stnPppoeEntry,
       "stnPppoeIndex": stnPppoeIndex,
       "stnPppoeType": stnPppoeType,
       "stnPppoeState": stnPppoeState,
       "stnPppoeVclid": stnPppoeVclid,
       "stnPppoeIfIndex": stnPppoeIfIndex,
       "stnPppoeRouterIndex": stnPppoeRouterIndex,
       "stnPppoeLinkType": stnPppoeLinkType,
       "stnPppoeLinkInstance": stnPppoeLinkInstance,
       "stnPppTable": stnPppTable,
       "stnPppEntry": stnPppEntry,
       "stnPppIndex": stnPppIndex,
       "stnPppType": stnPppType,
       "stnPppState": stnPppState,
       "stnPppVclid": stnPppVclid,
       "stnPppIfIndex": stnPppIfIndex,
       "stnPppRouterIndex": stnPppRouterIndex,
       "stnRouterNAT": stnRouterNAT,
       "stnRouterVEI": stnRouterVEI,
       "stnRouterAtmVpn": stnRouterAtmVpn,
       "stnRouterVimuxMpls": stnRouterVimuxMpls,
       "stnRouterVTI": stnRouterVTI,
       "stnRouterMibConformance": stnRouterMibConformance,
       "stnRouterUp": stnRouterUp,
       "stnRouterDown": stnRouterDown,
       "stnRouterReassigned": stnRouterReassigned,
       "stnRouterReassignFailure": stnRouterReassignFailure,
       "stnSubnetIfAssignFailure": stnSubnetIfAssignFailure,
       "stnConfigAuditRouterFailure": stnConfigAuditRouterFailure,
       "stnConfigAuditSubnetIfFailure": stnConfigAuditSubnetIfFailure,
       "stnConfigAuditPppoeIfFailure": stnConfigAuditPppoeIfFailure,
       "stnConfigAuditPppIfFailure": stnConfigAuditPppIfFailure}
)
