# SNMP MIB module (TMS-L3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TMS-L3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:25 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tmsGeneric,) = mibBuilder.importSymbols(
    "WRS-MASTER-MIB",
    "tmsGeneric")


# MODULE-IDENTITY

tmsL3Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2)
)
tmsL3Mib.setRevisions(
        ("2001-04-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmsL3IpMisc_ObjectIdentity = ObjectIdentity
tmsL3IpMisc = _TmsL3IpMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 1)
)
_TmsL3IpMiscNumLogicalPorts_Type = Integer32
_TmsL3IpMiscNumLogicalPorts_Object = MibScalar
tmsL3IpMiscNumLogicalPorts = _TmsL3IpMiscNumLogicalPorts_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 1, 1),
    _TmsL3IpMiscNumLogicalPorts_Type()
)
tmsL3IpMiscNumLogicalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpMiscNumLogicalPorts.setStatus("current")


class _TmsL3IpMiscRoutingProtocol_Type(Integer32):
    """Custom type tmsL3IpMiscRoutingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ospf", 3),
          ("rip", 2))
    )


_TmsL3IpMiscRoutingProtocol_Type.__name__ = "Integer32"
_TmsL3IpMiscRoutingProtocol_Object = MibScalar
tmsL3IpMiscRoutingProtocol = _TmsL3IpMiscRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 1, 2),
    _TmsL3IpMiscRoutingProtocol_Type()
)
tmsL3IpMiscRoutingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsL3IpMiscRoutingProtocol.setStatus("current")


class _TmsL3IpMiscOspfv2Config_Type(OctetString):
    """Custom type tmsL3IpMiscOspfv2Config based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_TmsL3IpMiscOspfv2Config_Type.__name__ = "OctetString"
_TmsL3IpMiscOspfv2Config_Object = MibScalar
tmsL3IpMiscOspfv2Config = _TmsL3IpMiscOspfv2Config_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 1, 3),
    _TmsL3IpMiscOspfv2Config_Type()
)
tmsL3IpMiscOspfv2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpMiscOspfv2Config.setStatus("current")
_TmsL3IpSubnet_ObjectIdentity = ObjectIdentity
tmsL3IpSubnet = _TmsL3IpSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 2)
)
_TmsL3IpSubnetMaxRows_Type = Unsigned32
_TmsL3IpSubnetMaxRows_Object = MibScalar
tmsL3IpSubnetMaxRows = _TmsL3IpSubnetMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 2, 1),
    _TmsL3IpSubnetMaxRows_Type()
)
tmsL3IpSubnetMaxRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpSubnetMaxRows.setStatus("current")
_TmsL3IpSubnetCurrentRows_Type = Unsigned32
_TmsL3IpSubnetCurrentRows_Object = MibScalar
tmsL3IpSubnetCurrentRows = _TmsL3IpSubnetCurrentRows_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 2, 2),
    _TmsL3IpSubnetCurrentRows_Type()
)
tmsL3IpSubnetCurrentRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpSubnetCurrentRows.setStatus("current")
_TmsL3IpSubnetTable_Object = MibTable
tmsL3IpSubnetTable = _TmsL3IpSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tmsL3IpSubnetTable.setStatus("current")
_TmsL3IpSubnetEntry_Object = MibTableRow
tmsL3IpSubnetEntry = _TmsL3IpSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 2, 3, 1)
)
tmsL3IpSubnetEntry.setIndexNames(
    (0, "TMS-L3-MIB", "tmsL3IpSubnetIfIndex"),
    (0, "TMS-L3-MIB", "tmsL3IpSubnetAgentIpAddr"),
)
if mibBuilder.loadTexts:
    tmsL3IpSubnetEntry.setStatus("current")
_TmsL3IpSubnetIfIndex_Type = Integer32
_TmsL3IpSubnetIfIndex_Object = MibTableColumn
tmsL3IpSubnetIfIndex = _TmsL3IpSubnetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 2, 3, 1, 1),
    _TmsL3IpSubnetIfIndex_Type()
)
tmsL3IpSubnetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmsL3IpSubnetIfIndex.setStatus("current")
_TmsL3IpSubnetAgentIpAddr_Type = IpAddress
_TmsL3IpSubnetAgentIpAddr_Object = MibTableColumn
tmsL3IpSubnetAgentIpAddr = _TmsL3IpSubnetAgentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 2, 3, 1, 2),
    _TmsL3IpSubnetAgentIpAddr_Type()
)
tmsL3IpSubnetAgentIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmsL3IpSubnetAgentIpAddr.setStatus("current")
_TmsL3IpSubnetMask_Type = IpAddress
_TmsL3IpSubnetMask_Object = MibTableColumn
tmsL3IpSubnetMask = _TmsL3IpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 2, 3, 1, 3),
    _TmsL3IpSubnetMask_Type()
)
tmsL3IpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpSubnetMask.setStatus("current")


class _TmsL3IpSubnetVidIface_Type(Integer32):
    """Custom type tmsL3IpSubnetVidIface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TmsL3IpSubnetVidIface_Type.__name__ = "Integer32"
_TmsL3IpSubnetVidIface_Object = MibTableColumn
tmsL3IpSubnetVidIface = _TmsL3IpSubnetVidIface_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 2, 3, 1, 4),
    _TmsL3IpSubnetVidIface_Type()
)
tmsL3IpSubnetVidIface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpSubnetVidIface.setStatus("current")


class _TmsL3IpSubnetName_Type(DisplayString):
    """Custom type tmsL3IpSubnetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmsL3IpSubnetName_Type.__name__ = "DisplayString"
_TmsL3IpSubnetName_Object = MibTableColumn
tmsL3IpSubnetName = _TmsL3IpSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 2, 3, 1, 5),
    _TmsL3IpSubnetName_Type()
)
tmsL3IpSubnetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpSubnetName.setStatus("current")
_TmsL3IpSubnetRowStatus_Type = RowStatus
_TmsL3IpSubnetRowStatus_Object = MibTableColumn
tmsL3IpSubnetRowStatus = _TmsL3IpSubnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 2, 3, 1, 6),
    _TmsL3IpSubnetRowStatus_Type()
)
tmsL3IpSubnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpSubnetRowStatus.setStatus("current")
_TmsL3IpStatic_ObjectIdentity = ObjectIdentity
tmsL3IpStatic = _TmsL3IpStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3)
)
_TmsL3IpStaticMaxHwHosts_Type = Unsigned32
_TmsL3IpStaticMaxHwHosts_Object = MibScalar
tmsL3IpStaticMaxHwHosts = _TmsL3IpStaticMaxHwHosts_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 1),
    _TmsL3IpStaticMaxHwHosts_Type()
)
tmsL3IpStaticMaxHwHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpStaticMaxHwHosts.setStatus("current")
_TmsL3IpStaticNumStaticHwHosts_Type = Unsigned32
_TmsL3IpStaticNumStaticHwHosts_Object = MibScalar
tmsL3IpStaticNumStaticHwHosts = _TmsL3IpStaticNumStaticHwHosts_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 2),
    _TmsL3IpStaticNumStaticHwHosts_Type()
)
tmsL3IpStaticNumStaticHwHosts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsL3IpStaticNumStaticHwHosts.setStatus("current")
_TmsL3IpStaticMaxHwSubnets_Type = Unsigned32
_TmsL3IpStaticMaxHwSubnets_Object = MibScalar
tmsL3IpStaticMaxHwSubnets = _TmsL3IpStaticMaxHwSubnets_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 3),
    _TmsL3IpStaticMaxHwSubnets_Type()
)
tmsL3IpStaticMaxHwSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpStaticMaxHwSubnets.setStatus("current")
_TmsL3IpStaticNumStaticHwSubnets_Type = Unsigned32
_TmsL3IpStaticNumStaticHwSubnets_Object = MibScalar
tmsL3IpStaticNumStaticHwSubnets = _TmsL3IpStaticNumStaticHwSubnets_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 4),
    _TmsL3IpStaticNumStaticHwSubnets_Type()
)
tmsL3IpStaticNumStaticHwSubnets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmsL3IpStaticNumStaticHwSubnets.setStatus("current")
_TmsL3IpStaticRouteMaxRows_Type = Unsigned32
_TmsL3IpStaticRouteMaxRows_Object = MibScalar
tmsL3IpStaticRouteMaxRows = _TmsL3IpStaticRouteMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 5),
    _TmsL3IpStaticRouteMaxRows_Type()
)
tmsL3IpStaticRouteMaxRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpStaticRouteMaxRows.setStatus("current")
_TmsL3IpStaticRouteCurrentRows_Type = Unsigned32
_TmsL3IpStaticRouteCurrentRows_Object = MibScalar
tmsL3IpStaticRouteCurrentRows = _TmsL3IpStaticRouteCurrentRows_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 6),
    _TmsL3IpStaticRouteCurrentRows_Type()
)
tmsL3IpStaticRouteCurrentRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpStaticRouteCurrentRows.setStatus("current")
_TmsL3IpStaticRouteTable_Object = MibTable
tmsL3IpStaticRouteTable = _TmsL3IpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 7)
)
if mibBuilder.loadTexts:
    tmsL3IpStaticRouteTable.setStatus("current")
_TmsL3IpStaticRouteEntry_Object = MibTableRow
tmsL3IpStaticRouteEntry = _TmsL3IpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 7, 1)
)
tmsL3IpStaticRouteEntry.setIndexNames(
    (0, "TMS-L3-MIB", "tmsL3IpStaticDestIpAddr"),
)
if mibBuilder.loadTexts:
    tmsL3IpStaticRouteEntry.setStatus("current")
_TmsL3IpStaticDestIpAddr_Type = IpAddress
_TmsL3IpStaticDestIpAddr_Object = MibTableColumn
tmsL3IpStaticDestIpAddr = _TmsL3IpStaticDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 7, 1, 1),
    _TmsL3IpStaticDestIpAddr_Type()
)
tmsL3IpStaticDestIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmsL3IpStaticDestIpAddr.setStatus("current")
_TmsL3IpStaticMask_Type = IpAddress
_TmsL3IpStaticMask_Object = MibTableColumn
tmsL3IpStaticMask = _TmsL3IpStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 7, 1, 2),
    _TmsL3IpStaticMask_Type()
)
tmsL3IpStaticMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpStaticMask.setStatus("current")
_TmsL3IpStaticNextHop_Type = IpAddress
_TmsL3IpStaticNextHop_Object = MibTableColumn
tmsL3IpStaticNextHop = _TmsL3IpStaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 7, 1, 3),
    _TmsL3IpStaticNextHop_Type()
)
tmsL3IpStaticNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpStaticNextHop.setStatus("current")


class _TmsL3IpStaticName_Type(DisplayString):
    """Custom type tmsL3IpStaticName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmsL3IpStaticName_Type.__name__ = "DisplayString"
_TmsL3IpStaticName_Object = MibTableColumn
tmsL3IpStaticName = _TmsL3IpStaticName_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 7, 1, 4),
    _TmsL3IpStaticName_Type()
)
tmsL3IpStaticName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpStaticName.setStatus("current")


class _TmsL3IpStaticUseHw_Type(TruthValue):
    """Custom type tmsL3IpStaticUseHw based on TruthValue"""


_TmsL3IpStaticUseHw_Object = MibTableColumn
tmsL3IpStaticUseHw = _TmsL3IpStaticUseHw_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 7, 1, 5),
    _TmsL3IpStaticUseHw_Type()
)
tmsL3IpStaticUseHw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpStaticUseHw.setStatus("current")
_TmsL3IpStaticInHw_Type = TruthValue
_TmsL3IpStaticInHw_Object = MibTableColumn
tmsL3IpStaticInHw = _TmsL3IpStaticInHw_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 7, 1, 6),
    _TmsL3IpStaticInHw_Type()
)
tmsL3IpStaticInHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpStaticInHw.setStatus("current")


class _TmsL3IpStaticGateway_Type(TruthValue):
    """Custom type tmsL3IpStaticGateway based on TruthValue"""


_TmsL3IpStaticGateway_Object = MibTableColumn
tmsL3IpStaticGateway = _TmsL3IpStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 7, 1, 7),
    _TmsL3IpStaticGateway_Type()
)
tmsL3IpStaticGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpStaticGateway.setStatus("current")
_TmsL3IpStaticRowStatus_Type = RowStatus
_TmsL3IpStaticRowStatus_Object = MibTableColumn
tmsL3IpStaticRowStatus = _TmsL3IpStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 3, 7, 1, 8),
    _TmsL3IpStaticRowStatus_Type()
)
tmsL3IpStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpStaticRowStatus.setStatus("current")
_TmsL3IpDynamic_ObjectIdentity = ObjectIdentity
tmsL3IpDynamic = _TmsL3IpDynamic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 4)
)
_TmsL3IpDynamicRouteCurrentRows_Type = Unsigned32
_TmsL3IpDynamicRouteCurrentRows_Object = MibScalar
tmsL3IpDynamicRouteCurrentRows = _TmsL3IpDynamicRouteCurrentRows_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 4, 1),
    _TmsL3IpDynamicRouteCurrentRows_Type()
)
tmsL3IpDynamicRouteCurrentRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpDynamicRouteCurrentRows.setStatus("current")
_TmsL3IpDynamicRouteTable_Object = MibTable
tmsL3IpDynamicRouteTable = _TmsL3IpDynamicRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tmsL3IpDynamicRouteTable.setStatus("current")
_TmsL3IpDynamicRouteEntry_Object = MibTableRow
tmsL3IpDynamicRouteEntry = _TmsL3IpDynamicRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 4, 2, 1)
)
tmsL3IpDynamicRouteEntry.setIndexNames(
    (0, "TMS-L3-MIB", "tmsL3IpDynamicDestIpAddr"),
)
if mibBuilder.loadTexts:
    tmsL3IpDynamicRouteEntry.setStatus("current")
_TmsL3IpDynamicDestIpAddr_Type = IpAddress
_TmsL3IpDynamicDestIpAddr_Object = MibTableColumn
tmsL3IpDynamicDestIpAddr = _TmsL3IpDynamicDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 4, 2, 1, 1),
    _TmsL3IpDynamicDestIpAddr_Type()
)
tmsL3IpDynamicDestIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmsL3IpDynamicDestIpAddr.setStatus("current")
_TmsL3IpDynamicMask_Type = IpAddress
_TmsL3IpDynamicMask_Object = MibTableColumn
tmsL3IpDynamicMask = _TmsL3IpDynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 4, 2, 1, 2),
    _TmsL3IpDynamicMask_Type()
)
tmsL3IpDynamicMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpDynamicMask.setStatus("current")
_TmsL3IpDynamicNextHop_Type = IpAddress
_TmsL3IpDynamicNextHop_Object = MibTableColumn
tmsL3IpDynamicNextHop = _TmsL3IpDynamicNextHop_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 4, 2, 1, 3),
    _TmsL3IpDynamicNextHop_Type()
)
tmsL3IpDynamicNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpDynamicNextHop.setStatus("current")


class _TmsL3IpDynamicName_Type(DisplayString):
    """Custom type tmsL3IpDynamicName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmsL3IpDynamicName_Type.__name__ = "DisplayString"
_TmsL3IpDynamicName_Object = MibTableColumn
tmsL3IpDynamicName = _TmsL3IpDynamicName_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 4, 2, 1, 4),
    _TmsL3IpDynamicName_Type()
)
tmsL3IpDynamicName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpDynamicName.setStatus("current")


class _TmsL3IpDynamicUseHw_Type(TruthValue):
    """Custom type tmsL3IpDynamicUseHw based on TruthValue"""


_TmsL3IpDynamicUseHw_Object = MibTableColumn
tmsL3IpDynamicUseHw = _TmsL3IpDynamicUseHw_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 4, 2, 1, 5),
    _TmsL3IpDynamicUseHw_Type()
)
tmsL3IpDynamicUseHw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpDynamicUseHw.setStatus("current")
_TmsL3IpDynamicInHw_Type = TruthValue
_TmsL3IpDynamicInHw_Object = MibTableColumn
tmsL3IpDynamicInHw = _TmsL3IpDynamicInHw_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 4, 2, 1, 6),
    _TmsL3IpDynamicInHw_Type()
)
tmsL3IpDynamicInHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpDynamicInHw.setStatus("current")


class _TmsL3IpDynamicGateway_Type(TruthValue):
    """Custom type tmsL3IpDynamicGateway based on TruthValue"""


_TmsL3IpDynamicGateway_Object = MibTableColumn
tmsL3IpDynamicGateway = _TmsL3IpDynamicGateway_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 4, 2, 1, 7),
    _TmsL3IpDynamicGateway_Type()
)
tmsL3IpDynamicGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpDynamicGateway.setStatus("current")
_TmsL3IpDynamicRowStatus_Type = RowStatus
_TmsL3IpDynamicRowStatus_Object = MibTableColumn
tmsL3IpDynamicRowStatus = _TmsL3IpDynamicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 4, 2, 1, 8),
    _TmsL3IpDynamicRowStatus_Type()
)
tmsL3IpDynamicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpDynamicRowStatus.setStatus("current")
_TmsL3IpRoute_ObjectIdentity = ObjectIdentity
tmsL3IpRoute = _TmsL3IpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5)
)
_TmsL3IpRouteTableCurrentSwEntries_Type = Unsigned32
_TmsL3IpRouteTableCurrentSwEntries_Object = MibScalar
tmsL3IpRouteTableCurrentSwEntries = _TmsL3IpRouteTableCurrentSwEntries_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 1),
    _TmsL3IpRouteTableCurrentSwEntries_Type()
)
tmsL3IpRouteTableCurrentSwEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteTableCurrentSwEntries.setStatus("current")
_TmsL3IpRouteCurrentHwHosts_Type = Unsigned32
_TmsL3IpRouteCurrentHwHosts_Object = MibScalar
tmsL3IpRouteCurrentHwHosts = _TmsL3IpRouteCurrentHwHosts_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 2),
    _TmsL3IpRouteCurrentHwHosts_Type()
)
tmsL3IpRouteCurrentHwHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteCurrentHwHosts.setStatus("current")
_TmsL3IpRouteCurrentHwSubnets_Type = Unsigned32
_TmsL3IpRouteCurrentHwSubnets_Object = MibScalar
tmsL3IpRouteCurrentHwSubnets = _TmsL3IpRouteCurrentHwSubnets_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 3),
    _TmsL3IpRouteCurrentHwSubnets_Type()
)
tmsL3IpRouteCurrentHwSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteCurrentHwSubnets.setStatus("current")
_TmsL3IpRouteTable_Object = MibTable
tmsL3IpRouteTable = _TmsL3IpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4)
)
if mibBuilder.loadTexts:
    tmsL3IpRouteTable.setStatus("current")
_TmsL3IpRouteEntry_Object = MibTableRow
tmsL3IpRouteEntry = _TmsL3IpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1)
)
tmsL3IpRouteEntry.setIndexNames(
    (0, "TMS-L3-MIB", "tmsL3IpRouteDest"),
)
if mibBuilder.loadTexts:
    tmsL3IpRouteEntry.setStatus("current")
_TmsL3IpRouteDest_Type = IpAddress
_TmsL3IpRouteDest_Object = MibTableColumn
tmsL3IpRouteDest = _TmsL3IpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 1),
    _TmsL3IpRouteDest_Type()
)
tmsL3IpRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmsL3IpRouteDest.setStatus("current")
_TmsL3IpRouteMask_Type = IpAddress
_TmsL3IpRouteMask_Object = MibTableColumn
tmsL3IpRouteMask = _TmsL3IpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 2),
    _TmsL3IpRouteMask_Type()
)
tmsL3IpRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpRouteMask.setStatus("current")
_TmsL3IpRouteNextHopIp_Type = IpAddress
_TmsL3IpRouteNextHopIp_Object = MibTableColumn
tmsL3IpRouteNextHopIp = _TmsL3IpRouteNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 3),
    _TmsL3IpRouteNextHopIp_Type()
)
tmsL3IpRouteNextHopIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpRouteNextHopIp.setStatus("current")
_TmsL3IpRouteNextHopMac_Type = MacAddress
_TmsL3IpRouteNextHopMac_Object = MibTableColumn
tmsL3IpRouteNextHopMac = _TmsL3IpRouteNextHopMac_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 4),
    _TmsL3IpRouteNextHopMac_Type()
)
tmsL3IpRouteNextHopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteNextHopMac.setStatus("current")
_TmsL3IpRouteIfIndex_Type = Integer32
_TmsL3IpRouteIfIndex_Object = MibTableColumn
tmsL3IpRouteIfIndex = _TmsL3IpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 5),
    _TmsL3IpRouteIfIndex_Type()
)
tmsL3IpRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteIfIndex.setStatus("current")


class _TmsL3IpRouteType_Type(Integer32):
    """Custom type tmsL3IpRouteType based on Integer32"""
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
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_TmsL3IpRouteType_Type.__name__ = "Integer32"
_TmsL3IpRouteType_Object = MibTableColumn
tmsL3IpRouteType = _TmsL3IpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 6),
    _TmsL3IpRouteType_Type()
)
tmsL3IpRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpRouteType.setStatus("current")


class _TmsL3IpRouteProto_Type(Integer32):
    """Custom type tmsL3IpRouteProto based on Integer32"""
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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("es-is", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("is-is", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_TmsL3IpRouteProto_Type.__name__ = "Integer32"
_TmsL3IpRouteProto_Object = MibTableColumn
tmsL3IpRouteProto = _TmsL3IpRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 7),
    _TmsL3IpRouteProto_Type()
)
tmsL3IpRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteProto.setStatus("current")
_TmsL3IpRouteAge_Type = Unsigned32
_TmsL3IpRouteAge_Object = MibTableColumn
tmsL3IpRouteAge = _TmsL3IpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 8),
    _TmsL3IpRouteAge_Type()
)
tmsL3IpRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteAge.setStatus("current")
_TmsL3IpRouteMetric1_Type = Integer32
_TmsL3IpRouteMetric1_Object = MibTableColumn
tmsL3IpRouteMetric1 = _TmsL3IpRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 9),
    _TmsL3IpRouteMetric1_Type()
)
tmsL3IpRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteMetric1.setStatus("current")
_TmsL3IpRouteUsingHw_Type = TruthValue
_TmsL3IpRouteUsingHw_Object = MibTableColumn
tmsL3IpRouteUsingHw = _TmsL3IpRouteUsingHw_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 10),
    _TmsL3IpRouteUsingHw_Type()
)
tmsL3IpRouteUsingHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteUsingHw.setStatus("current")
_TmsL3IpRouteIsStatic_Type = TruthValue
_TmsL3IpRouteIsStatic_Object = MibTableColumn
tmsL3IpRouteIsStatic = _TmsL3IpRouteIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 11),
    _TmsL3IpRouteIsStatic_Type()
)
tmsL3IpRouteIsStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteIsStatic.setStatus("current")
_TmsL3IpRouteFlags_Type = Unsigned32
_TmsL3IpRouteFlags_Object = MibTableColumn
tmsL3IpRouteFlags = _TmsL3IpRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 12),
    _TmsL3IpRouteFlags_Type()
)
tmsL3IpRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteFlags.setStatus("current")
_TmsL3IpRouteRef_Type = Gauge32
_TmsL3IpRouteRef_Object = MibTableColumn
tmsL3IpRouteRef = _TmsL3IpRouteRef_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 13),
    _TmsL3IpRouteRef_Type()
)
tmsL3IpRouteRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteRef.setStatus("current")
_TmsL3IpRouteUse_Type = Counter32
_TmsL3IpRouteUse_Object = MibTableColumn
tmsL3IpRouteUse = _TmsL3IpRouteUse_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 14),
    _TmsL3IpRouteUse_Type()
)
tmsL3IpRouteUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsL3IpRouteUse.setStatus("current")
_TmsL3IpRouteRowStatus_Type = RowStatus
_TmsL3IpRouteRowStatus_Object = MibTableColumn
tmsL3IpRouteRowStatus = _TmsL3IpRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 5, 4, 1, 15),
    _TmsL3IpRouteRowStatus_Type()
)
tmsL3IpRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmsL3IpRouteRowStatus.setStatus("current")
_TmsL3MibConformance_ObjectIdentity = ObjectIdentity
tmsL3MibConformance = _TmsL3MibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 6)
)
_TmsL3MibGroups_ObjectIdentity = ObjectIdentity
tmsL3MibGroups = _TmsL3MibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 6, 1)
)
_TmsL3MibCompliances_ObjectIdentity = ObjectIdentity
tmsL3MibCompliances = _TmsL3MibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 6, 2)
)

# Managed Objects groups

tmsL3IpMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 6, 1, 1)
)
tmsL3IpMiscGroup.setObjects(
      *(("TMS-L3-MIB", "tmsL3IpMiscNumLogicalPorts"),
        ("TMS-L3-MIB", "tmsL3IpMiscRoutingProtocol"),
        ("TMS-L3-MIB", "tmsL3IpMiscOspfv2Config"))
)
if mibBuilder.loadTexts:
    tmsL3IpMiscGroup.setStatus("current")

tmsL3IpSubnetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 6, 1, 2)
)
tmsL3IpSubnetGroup.setObjects(
      *(("TMS-L3-MIB", "tmsL3IpSubnetMaxRows"),
        ("TMS-L3-MIB", "tmsL3IpSubnetCurrentRows"),
        ("TMS-L3-MIB", "tmsL3IpSubnetMask"),
        ("TMS-L3-MIB", "tmsL3IpSubnetVidIface"),
        ("TMS-L3-MIB", "tmsL3IpSubnetName"),
        ("TMS-L3-MIB", "tmsL3IpSubnetRowStatus"))
)
if mibBuilder.loadTexts:
    tmsL3IpSubnetGroup.setStatus("current")

tmsL3IpStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 6, 1, 3)
)
tmsL3IpStaticGroup.setObjects(
      *(("TMS-L3-MIB", "tmsL3IpStaticMaxHwHosts"),
        ("TMS-L3-MIB", "tmsL3IpStaticNumStaticHwHosts"),
        ("TMS-L3-MIB", "tmsL3IpStaticMaxHwSubnets"),
        ("TMS-L3-MIB", "tmsL3IpStaticNumStaticHwSubnets"),
        ("TMS-L3-MIB", "tmsL3IpStaticRouteMaxRows"),
        ("TMS-L3-MIB", "tmsL3IpStaticRouteCurrentRows"),
        ("TMS-L3-MIB", "tmsL3IpStaticMask"),
        ("TMS-L3-MIB", "tmsL3IpStaticNextHop"),
        ("TMS-L3-MIB", "tmsL3IpStaticName"),
        ("TMS-L3-MIB", "tmsL3IpStaticUseHw"),
        ("TMS-L3-MIB", "tmsL3IpStaticInHw"),
        ("TMS-L3-MIB", "tmsL3IpStaticGateway"),
        ("TMS-L3-MIB", "tmsL3IpStaticRowStatus"))
)
if mibBuilder.loadTexts:
    tmsL3IpStaticGroup.setStatus("current")

tmsL3IpDynamicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 6, 1, 4)
)
tmsL3IpDynamicGroup.setObjects(
      *(("TMS-L3-MIB", "tmsL3IpDynamicRouteCurrentRows"),
        ("TMS-L3-MIB", "tmsL3IpDynamicMask"),
        ("TMS-L3-MIB", "tmsL3IpDynamicNextHop"),
        ("TMS-L3-MIB", "tmsL3IpDynamicName"),
        ("TMS-L3-MIB", "tmsL3IpDynamicUseHw"),
        ("TMS-L3-MIB", "tmsL3IpDynamicInHw"),
        ("TMS-L3-MIB", "tmsL3IpDynamicGateway"),
        ("TMS-L3-MIB", "tmsL3IpDynamicRowStatus"))
)
if mibBuilder.loadTexts:
    tmsL3IpDynamicGroup.setStatus("current")

tmsL3IpRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 6, 1, 5)
)
tmsL3IpRouteGroup.setObjects(
      *(("TMS-L3-MIB", "tmsL3IpRouteTableCurrentSwEntries"),
        ("TMS-L3-MIB", "tmsL3IpRouteCurrentHwHosts"),
        ("TMS-L3-MIB", "tmsL3IpRouteCurrentHwSubnets"),
        ("TMS-L3-MIB", "tmsL3IpRouteMask"),
        ("TMS-L3-MIB", "tmsL3IpRouteNextHopIp"),
        ("TMS-L3-MIB", "tmsL3IpRouteNextHopMac"),
        ("TMS-L3-MIB", "tmsL3IpRouteIfIndex"),
        ("TMS-L3-MIB", "tmsL3IpRouteType"),
        ("TMS-L3-MIB", "tmsL3IpRouteProto"),
        ("TMS-L3-MIB", "tmsL3IpRouteAge"),
        ("TMS-L3-MIB", "tmsL3IpRouteMetric1"),
        ("TMS-L3-MIB", "tmsL3IpRouteUsingHw"),
        ("TMS-L3-MIB", "tmsL3IpRouteIsStatic"),
        ("TMS-L3-MIB", "tmsL3IpRouteFlags"),
        ("TMS-L3-MIB", "tmsL3IpRouteRef"),
        ("TMS-L3-MIB", "tmsL3IpRouteUse"),
        ("TMS-L3-MIB", "tmsL3IpRouteRowStatus"))
)
if mibBuilder.loadTexts:
    tmsL3IpRouteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmsL3MibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 731, 2, 2, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    tmsL3MibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TMS-L3-MIB",
    **{"tmsL3Mib": tmsL3Mib,
       "tmsL3IpMisc": tmsL3IpMisc,
       "tmsL3IpMiscNumLogicalPorts": tmsL3IpMiscNumLogicalPorts,
       "tmsL3IpMiscRoutingProtocol": tmsL3IpMiscRoutingProtocol,
       "tmsL3IpMiscOspfv2Config": tmsL3IpMiscOspfv2Config,
       "tmsL3IpSubnet": tmsL3IpSubnet,
       "tmsL3IpSubnetMaxRows": tmsL3IpSubnetMaxRows,
       "tmsL3IpSubnetCurrentRows": tmsL3IpSubnetCurrentRows,
       "tmsL3IpSubnetTable": tmsL3IpSubnetTable,
       "tmsL3IpSubnetEntry": tmsL3IpSubnetEntry,
       "tmsL3IpSubnetIfIndex": tmsL3IpSubnetIfIndex,
       "tmsL3IpSubnetAgentIpAddr": tmsL3IpSubnetAgentIpAddr,
       "tmsL3IpSubnetMask": tmsL3IpSubnetMask,
       "tmsL3IpSubnetVidIface": tmsL3IpSubnetVidIface,
       "tmsL3IpSubnetName": tmsL3IpSubnetName,
       "tmsL3IpSubnetRowStatus": tmsL3IpSubnetRowStatus,
       "tmsL3IpStatic": tmsL3IpStatic,
       "tmsL3IpStaticMaxHwHosts": tmsL3IpStaticMaxHwHosts,
       "tmsL3IpStaticNumStaticHwHosts": tmsL3IpStaticNumStaticHwHosts,
       "tmsL3IpStaticMaxHwSubnets": tmsL3IpStaticMaxHwSubnets,
       "tmsL3IpStaticNumStaticHwSubnets": tmsL3IpStaticNumStaticHwSubnets,
       "tmsL3IpStaticRouteMaxRows": tmsL3IpStaticRouteMaxRows,
       "tmsL3IpStaticRouteCurrentRows": tmsL3IpStaticRouteCurrentRows,
       "tmsL3IpStaticRouteTable": tmsL3IpStaticRouteTable,
       "tmsL3IpStaticRouteEntry": tmsL3IpStaticRouteEntry,
       "tmsL3IpStaticDestIpAddr": tmsL3IpStaticDestIpAddr,
       "tmsL3IpStaticMask": tmsL3IpStaticMask,
       "tmsL3IpStaticNextHop": tmsL3IpStaticNextHop,
       "tmsL3IpStaticName": tmsL3IpStaticName,
       "tmsL3IpStaticUseHw": tmsL3IpStaticUseHw,
       "tmsL3IpStaticInHw": tmsL3IpStaticInHw,
       "tmsL3IpStaticGateway": tmsL3IpStaticGateway,
       "tmsL3IpStaticRowStatus": tmsL3IpStaticRowStatus,
       "tmsL3IpDynamic": tmsL3IpDynamic,
       "tmsL3IpDynamicRouteCurrentRows": tmsL3IpDynamicRouteCurrentRows,
       "tmsL3IpDynamicRouteTable": tmsL3IpDynamicRouteTable,
       "tmsL3IpDynamicRouteEntry": tmsL3IpDynamicRouteEntry,
       "tmsL3IpDynamicDestIpAddr": tmsL3IpDynamicDestIpAddr,
       "tmsL3IpDynamicMask": tmsL3IpDynamicMask,
       "tmsL3IpDynamicNextHop": tmsL3IpDynamicNextHop,
       "tmsL3IpDynamicName": tmsL3IpDynamicName,
       "tmsL3IpDynamicUseHw": tmsL3IpDynamicUseHw,
       "tmsL3IpDynamicInHw": tmsL3IpDynamicInHw,
       "tmsL3IpDynamicGateway": tmsL3IpDynamicGateway,
       "tmsL3IpDynamicRowStatus": tmsL3IpDynamicRowStatus,
       "tmsL3IpRoute": tmsL3IpRoute,
       "tmsL3IpRouteTableCurrentSwEntries": tmsL3IpRouteTableCurrentSwEntries,
       "tmsL3IpRouteCurrentHwHosts": tmsL3IpRouteCurrentHwHosts,
       "tmsL3IpRouteCurrentHwSubnets": tmsL3IpRouteCurrentHwSubnets,
       "tmsL3IpRouteTable": tmsL3IpRouteTable,
       "tmsL3IpRouteEntry": tmsL3IpRouteEntry,
       "tmsL3IpRouteDest": tmsL3IpRouteDest,
       "tmsL3IpRouteMask": tmsL3IpRouteMask,
       "tmsL3IpRouteNextHopIp": tmsL3IpRouteNextHopIp,
       "tmsL3IpRouteNextHopMac": tmsL3IpRouteNextHopMac,
       "tmsL3IpRouteIfIndex": tmsL3IpRouteIfIndex,
       "tmsL3IpRouteType": tmsL3IpRouteType,
       "tmsL3IpRouteProto": tmsL3IpRouteProto,
       "tmsL3IpRouteAge": tmsL3IpRouteAge,
       "tmsL3IpRouteMetric1": tmsL3IpRouteMetric1,
       "tmsL3IpRouteUsingHw": tmsL3IpRouteUsingHw,
       "tmsL3IpRouteIsStatic": tmsL3IpRouteIsStatic,
       "tmsL3IpRouteFlags": tmsL3IpRouteFlags,
       "tmsL3IpRouteRef": tmsL3IpRouteRef,
       "tmsL3IpRouteUse": tmsL3IpRouteUse,
       "tmsL3IpRouteRowStatus": tmsL3IpRouteRowStatus,
       "tmsL3MibConformance": tmsL3MibConformance,
       "tmsL3MibGroups": tmsL3MibGroups,
       "tmsL3IpMiscGroup": tmsL3IpMiscGroup,
       "tmsL3IpSubnetGroup": tmsL3IpSubnetGroup,
       "tmsL3IpStaticGroup": tmsL3IpStaticGroup,
       "tmsL3IpDynamicGroup": tmsL3IpDynamicGroup,
       "tmsL3IpRouteGroup": tmsL3IpRouteGroup,
       "tmsL3MibCompliances": tmsL3MibCompliances,
       "tmsL3MibCompliance": tmsL3MibCompliance}
)
