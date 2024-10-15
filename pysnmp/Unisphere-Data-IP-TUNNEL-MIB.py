# SNMP MIB module (Unisphere-Data-IP-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-IP-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:57 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdName,
 UsdNextIfIndex) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdName",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdIpTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51)
)
usdIpTunnelMIB.setRevisions(
        ("2001-07-23 20:57",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdIpTunnelInterfaceObjects_ObjectIdentity = ObjectIdentity
usdIpTunnelInterfaceObjects = _UsdIpTunnelInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1)
)
_UsdIpTunnelNextIfIndex_Type = UsdNextIfIndex
_UsdIpTunnelNextIfIndex_Object = MibScalar
usdIpTunnelNextIfIndex = _UsdIpTunnelNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 1),
    _UsdIpTunnelNextIfIndex_Type()
)
usdIpTunnelNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpTunnelNextIfIndex.setStatus("current")
_UsdIpTunnelInterfaceTable_Object = MibTable
usdIpTunnelInterfaceTable = _UsdIpTunnelInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2)
)
if mibBuilder.loadTexts:
    usdIpTunnelInterfaceTable.setStatus("current")
_UsdIpTunnelInterfaceEntry_Object = MibTableRow
usdIpTunnelInterfaceEntry = _UsdIpTunnelInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1)
)
usdIpTunnelInterfaceEntry.setIndexNames(
    (0, "Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    usdIpTunnelInterfaceEntry.setStatus("current")
_UsdIpTunnelIfIndex_Type = InterfaceIndex
_UsdIpTunnelIfIndex_Object = MibTableColumn
usdIpTunnelIfIndex = _UsdIpTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 1),
    _UsdIpTunnelIfIndex_Type()
)
usdIpTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpTunnelIfIndex.setStatus("current")


class _UsdIpTunnelName_Type(DisplayString):
    """Custom type usdIpTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UsdIpTunnelName_Type.__name__ = "DisplayString"
_UsdIpTunnelName_Object = MibTableColumn
usdIpTunnelName = _UsdIpTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 2),
    _UsdIpTunnelName_Type()
)
usdIpTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpTunnelName.setStatus("current")


class _UsdIpTunnelMode_Type(Integer32):
    """Custom type usdIpTunnelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipTunnelModeDvmrp", 1),
          ("ipTunnelModeGre", 0))
    )


_UsdIpTunnelMode_Type.__name__ = "Integer32"
_UsdIpTunnelMode_Object = MibTableColumn
usdIpTunnelMode = _UsdIpTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 3),
    _UsdIpTunnelMode_Type()
)
usdIpTunnelMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpTunnelMode.setStatus("current")


class _UsdIpTunnelVirtualRouter_Type(UsdName):
    """Custom type usdIpTunnelVirtualRouter based on UsdName"""
    defaultValue = OctetString("default")


_UsdIpTunnelVirtualRouter_Object = MibTableColumn
usdIpTunnelVirtualRouter = _UsdIpTunnelVirtualRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 4),
    _UsdIpTunnelVirtualRouter_Type()
)
usdIpTunnelVirtualRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpTunnelVirtualRouter.setStatus("current")


class _UsdIpTunnelChecksum_Type(TruthValue):
    """Custom type usdIpTunnelChecksum based on TruthValue"""


_UsdIpTunnelChecksum_Object = MibTableColumn
usdIpTunnelChecksum = _UsdIpTunnelChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 5),
    _UsdIpTunnelChecksum_Type()
)
usdIpTunnelChecksum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpTunnelChecksum.setStatus("current")


class _UsdIpTunnelMtu_Type(Integer32):
    """Custom type usdIpTunnelMtu based on Integer32"""
    defaultValue = 10240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 10240),
    )


_UsdIpTunnelMtu_Type.__name__ = "Integer32"
_UsdIpTunnelMtu_Object = MibTableColumn
usdIpTunnelMtu = _UsdIpTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 6),
    _UsdIpTunnelMtu_Type()
)
usdIpTunnelMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpTunnelMtu.setStatus("current")


class _UsdIpTunnelDestination_Type(IpAddress):
    """Custom type usdIpTunnelDestination based on IpAddress"""
    defaultValue = 0


_UsdIpTunnelDestination_Object = MibTableColumn
usdIpTunnelDestination = _UsdIpTunnelDestination_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 7),
    _UsdIpTunnelDestination_Type()
)
usdIpTunnelDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpTunnelDestination.setStatus("current")


class _UsdIpTunnelSource_Type(IpAddress):
    """Custom type usdIpTunnelSource based on IpAddress"""
    defaultValue = 0


_UsdIpTunnelSource_Object = MibTableColumn
usdIpTunnelSource = _UsdIpTunnelSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 8),
    _UsdIpTunnelSource_Type()
)
usdIpTunnelSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpTunnelSource.setStatus("current")
_UsdIpTunnelRowStatus_Type = RowStatus
_UsdIpTunnelRowStatus_Object = MibTableColumn
usdIpTunnelRowStatus = _UsdIpTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 9),
    _UsdIpTunnelRowStatus_Type()
)
usdIpTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpTunnelRowStatus.setStatus("current")
_UsdIpTunnelConformance_ObjectIdentity = ObjectIdentity
usdIpTunnelConformance = _UsdIpTunnelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2)
)
_UsdIpTunnelCompliances_ObjectIdentity = ObjectIdentity
usdIpTunnelCompliances = _UsdIpTunnelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 1)
)
_UsdIpTunnelGroups_ObjectIdentity = ObjectIdentity
usdIpTunnelGroups = _UsdIpTunnelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 2)
)

# Managed Objects groups

usdIpTunnelInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 2, 1)
)
usdIpTunnelInterfaceGroup.setObjects(
      *(("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelNextIfIndex"),
        ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelName"),
        ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelMode"),
        ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelVirtualRouter"),
        ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelChecksum"),
        ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelMtu"),
        ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelSource"),
        ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelDestination"),
        ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelRowStatus"))
)
if mibBuilder.loadTexts:
    usdIpTunnelInterfaceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdIpTunnnelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdIpTunnnelCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-IP-TUNNEL-MIB",
    **{"usdIpTunnelMIB": usdIpTunnelMIB,
       "usdIpTunnelInterfaceObjects": usdIpTunnelInterfaceObjects,
       "usdIpTunnelNextIfIndex": usdIpTunnelNextIfIndex,
       "usdIpTunnelInterfaceTable": usdIpTunnelInterfaceTable,
       "usdIpTunnelInterfaceEntry": usdIpTunnelInterfaceEntry,
       "usdIpTunnelIfIndex": usdIpTunnelIfIndex,
       "usdIpTunnelName": usdIpTunnelName,
       "usdIpTunnelMode": usdIpTunnelMode,
       "usdIpTunnelVirtualRouter": usdIpTunnelVirtualRouter,
       "usdIpTunnelChecksum": usdIpTunnelChecksum,
       "usdIpTunnelMtu": usdIpTunnelMtu,
       "usdIpTunnelDestination": usdIpTunnelDestination,
       "usdIpTunnelSource": usdIpTunnelSource,
       "usdIpTunnelRowStatus": usdIpTunnelRowStatus,
       "usdIpTunnelConformance": usdIpTunnelConformance,
       "usdIpTunnelCompliances": usdIpTunnelCompliances,
       "usdIpTunnnelCompliance": usdIpTunnnelCompliance,
       "usdIpTunnelGroups": usdIpTunnelGroups,
       "usdIpTunnelInterfaceGroup": usdIpTunnelInterfaceGroup}
)
