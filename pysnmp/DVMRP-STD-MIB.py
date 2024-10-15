# SNMP MIB module (DVMRP-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DVMRP-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:57 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dvmrpStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 62)
)
dvmrpStdMIB.setRevisions(
        ("2001-11-21 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DvmrpMIBObjects_ObjectIdentity = ObjectIdentity
dvmrpMIBObjects = _DvmrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 62, 1)
)
_Dvmrp_ObjectIdentity = ObjectIdentity
dvmrp = _Dvmrp_ObjectIdentity(
    (1, 3, 6, 1, 3, 62, 1, 1)
)
_DvmrpScalar_ObjectIdentity = ObjectIdentity
dvmrpScalar = _DvmrpScalar_ObjectIdentity(
    (1, 3, 6, 1, 3, 62, 1, 1, 1)
)
_DvmrpVersionString_Type = DisplayString
_DvmrpVersionString_Object = MibScalar
dvmrpVersionString = _DvmrpVersionString_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 1, 1),
    _DvmrpVersionString_Type()
)
dvmrpVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpVersionString.setStatus("current")
_DvmrpNumRoutes_Type = Gauge32
_DvmrpNumRoutes_Object = MibScalar
dvmrpNumRoutes = _DvmrpNumRoutes_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 1, 3),
    _DvmrpNumRoutes_Type()
)
dvmrpNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNumRoutes.setStatus("current")
_DvmrpReachableRoutes_Type = Gauge32
_DvmrpReachableRoutes_Object = MibScalar
dvmrpReachableRoutes = _DvmrpReachableRoutes_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 1, 4),
    _DvmrpReachableRoutes_Type()
)
dvmrpReachableRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpReachableRoutes.setStatus("current")
_DvmrpInterfaceTable_Object = MibTable
dvmrpInterfaceTable = _DvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dvmrpInterfaceTable.setStatus("current")
_DvmrpInterfaceEntry_Object = MibTableRow
dvmrpInterfaceEntry = _DvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2, 1)
)
dvmrpInterfaceEntry.setIndexNames(
    (0, "DVMRP-STD-MIB", "dvmrpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    dvmrpInterfaceEntry.setStatus("current")
_DvmrpInterfaceIndex_Type = InterfaceIndex
_DvmrpInterfaceIndex_Object = MibTableColumn
dvmrpInterfaceIndex = _DvmrpInterfaceIndex_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 1),
    _DvmrpInterfaceIndex_Type()
)
dvmrpInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpInterfaceIndex.setStatus("current")
_DvmrpInterfaceLocalAddress_Type = IpAddress
_DvmrpInterfaceLocalAddress_Object = MibTableColumn
dvmrpInterfaceLocalAddress = _DvmrpInterfaceLocalAddress_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 2),
    _DvmrpInterfaceLocalAddress_Type()
)
dvmrpInterfaceLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceLocalAddress.setStatus("current")


class _DvmrpInterfaceMetric_Type(Integer32):
    """Custom type dvmrpInterfaceMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DvmrpInterfaceMetric_Type.__name__ = "Integer32"
_DvmrpInterfaceMetric_Object = MibTableColumn
dvmrpInterfaceMetric = _DvmrpInterfaceMetric_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 3),
    _DvmrpInterfaceMetric_Type()
)
dvmrpInterfaceMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceMetric.setStatus("current")
_DvmrpInterfaceStatus_Type = RowStatus
_DvmrpInterfaceStatus_Object = MibTableColumn
dvmrpInterfaceStatus = _DvmrpInterfaceStatus_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 4),
    _DvmrpInterfaceStatus_Type()
)
dvmrpInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceStatus.setStatus("current")
_DvmrpInterfaceRcvBadPkts_Type = Counter32
_DvmrpInterfaceRcvBadPkts_Object = MibTableColumn
dvmrpInterfaceRcvBadPkts = _DvmrpInterfaceRcvBadPkts_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 5),
    _DvmrpInterfaceRcvBadPkts_Type()
)
dvmrpInterfaceRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceRcvBadPkts.setStatus("current")
_DvmrpInterfaceRcvBadRoutes_Type = Counter32
_DvmrpInterfaceRcvBadRoutes_Object = MibTableColumn
dvmrpInterfaceRcvBadRoutes = _DvmrpInterfaceRcvBadRoutes_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 6),
    _DvmrpInterfaceRcvBadRoutes_Type()
)
dvmrpInterfaceRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceRcvBadRoutes.setStatus("current")
_DvmrpInterfaceSentRoutes_Type = Counter32
_DvmrpInterfaceSentRoutes_Object = MibTableColumn
dvmrpInterfaceSentRoutes = _DvmrpInterfaceSentRoutes_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 7),
    _DvmrpInterfaceSentRoutes_Type()
)
dvmrpInterfaceSentRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceSentRoutes.setStatus("current")
_DvmrpInterfaceKey_Type = SnmpAdminString
_DvmrpInterfaceKey_Object = MibTableColumn
dvmrpInterfaceKey = _DvmrpInterfaceKey_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 8),
    _DvmrpInterfaceKey_Type()
)
dvmrpInterfaceKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceKey.setStatus("current")
_DvmrpInterfaceKeyVersion_Type = Integer32
_DvmrpInterfaceKeyVersion_Object = MibTableColumn
dvmrpInterfaceKeyVersion = _DvmrpInterfaceKeyVersion_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 9),
    _DvmrpInterfaceKeyVersion_Type()
)
dvmrpInterfaceKeyVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceKeyVersion.setStatus("current")
_DvmrpInterfaceGenerationId_Type = Integer32
_DvmrpInterfaceGenerationId_Object = MibTableColumn
dvmrpInterfaceGenerationId = _DvmrpInterfaceGenerationId_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 10),
    _DvmrpInterfaceGenerationId_Type()
)
dvmrpInterfaceGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceGenerationId.setStatus("current")
_DvmrpNeighborTable_Object = MibTable
dvmrpNeighborTable = _DvmrpNeighborTable_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dvmrpNeighborTable.setStatus("current")
_DvmrpNeighborEntry_Object = MibTableRow
dvmrpNeighborEntry = _DvmrpNeighborEntry_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1)
)
dvmrpNeighborEntry.setIndexNames(
    (0, "DVMRP-STD-MIB", "dvmrpNeighborIfIndex"),
    (0, "DVMRP-STD-MIB", "dvmrpNeighborAddress"),
)
if mibBuilder.loadTexts:
    dvmrpNeighborEntry.setStatus("current")
_DvmrpNeighborIfIndex_Type = InterfaceIndex
_DvmrpNeighborIfIndex_Object = MibTableColumn
dvmrpNeighborIfIndex = _DvmrpNeighborIfIndex_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 1),
    _DvmrpNeighborIfIndex_Type()
)
dvmrpNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpNeighborIfIndex.setStatus("current")
_DvmrpNeighborAddress_Type = IpAddress
_DvmrpNeighborAddress_Object = MibTableColumn
dvmrpNeighborAddress = _DvmrpNeighborAddress_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 2),
    _DvmrpNeighborAddress_Type()
)
dvmrpNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpNeighborAddress.setStatus("current")
_DvmrpNeighborUpTime_Type = TimeTicks
_DvmrpNeighborUpTime_Object = MibTableColumn
dvmrpNeighborUpTime = _DvmrpNeighborUpTime_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 3),
    _DvmrpNeighborUpTime_Type()
)
dvmrpNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborUpTime.setStatus("current")
_DvmrpNeighborExpiryTime_Type = TimeTicks
_DvmrpNeighborExpiryTime_Object = MibTableColumn
dvmrpNeighborExpiryTime = _DvmrpNeighborExpiryTime_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 4),
    _DvmrpNeighborExpiryTime_Type()
)
dvmrpNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborExpiryTime.setStatus("current")
_DvmrpNeighborGenerationId_Type = Integer32
_DvmrpNeighborGenerationId_Object = MibTableColumn
dvmrpNeighborGenerationId = _DvmrpNeighborGenerationId_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 5),
    _DvmrpNeighborGenerationId_Type()
)
dvmrpNeighborGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborGenerationId.setStatus("current")


class _DvmrpNeighborMajorVersion_Type(Integer32):
    """Custom type dvmrpNeighborMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DvmrpNeighborMajorVersion_Type.__name__ = "Integer32"
_DvmrpNeighborMajorVersion_Object = MibTableColumn
dvmrpNeighborMajorVersion = _DvmrpNeighborMajorVersion_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 6),
    _DvmrpNeighborMajorVersion_Type()
)
dvmrpNeighborMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborMajorVersion.setStatus("current")


class _DvmrpNeighborMinorVersion_Type(Integer32):
    """Custom type dvmrpNeighborMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DvmrpNeighborMinorVersion_Type.__name__ = "Integer32"
_DvmrpNeighborMinorVersion_Object = MibTableColumn
dvmrpNeighborMinorVersion = _DvmrpNeighborMinorVersion_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 7),
    _DvmrpNeighborMinorVersion_Type()
)
dvmrpNeighborMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborMinorVersion.setStatus("current")


class _DvmrpNeighborCapabilities_Type(Bits):
    """Custom type dvmrpNeighborCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("generationID", 2),
          ("leaf", 0),
          ("mtrace", 3),
          ("prune", 1))
    )

_DvmrpNeighborCapabilities_Type.__name__ = "Bits"
_DvmrpNeighborCapabilities_Object = MibTableColumn
dvmrpNeighborCapabilities = _DvmrpNeighborCapabilities_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 8),
    _DvmrpNeighborCapabilities_Type()
)
dvmrpNeighborCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborCapabilities.setStatus("current")
_DvmrpNeighborRcvRoutes_Type = Counter32
_DvmrpNeighborRcvRoutes_Object = MibTableColumn
dvmrpNeighborRcvRoutes = _DvmrpNeighborRcvRoutes_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 9),
    _DvmrpNeighborRcvRoutes_Type()
)
dvmrpNeighborRcvRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborRcvRoutes.setStatus("current")
_DvmrpNeighborRcvBadPkts_Type = Counter32
_DvmrpNeighborRcvBadPkts_Object = MibTableColumn
dvmrpNeighborRcvBadPkts = _DvmrpNeighborRcvBadPkts_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 10),
    _DvmrpNeighborRcvBadPkts_Type()
)
dvmrpNeighborRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborRcvBadPkts.setStatus("current")
_DvmrpNeighborRcvBadRoutes_Type = Counter32
_DvmrpNeighborRcvBadRoutes_Object = MibTableColumn
dvmrpNeighborRcvBadRoutes = _DvmrpNeighborRcvBadRoutes_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 11),
    _DvmrpNeighborRcvBadRoutes_Type()
)
dvmrpNeighborRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborRcvBadRoutes.setStatus("current")


class _DvmrpNeighborState_Type(Integer32):
    """Custom type dvmrpNeighborState based on Integer32"""
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
        *(("active", 2),
          ("down", 4),
          ("ignoring", 3),
          ("oneway", 1))
    )


_DvmrpNeighborState_Type.__name__ = "Integer32"
_DvmrpNeighborState_Object = MibTableColumn
dvmrpNeighborState = _DvmrpNeighborState_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 12),
    _DvmrpNeighborState_Type()
)
dvmrpNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborState.setStatus("current")
_DvmrpRouteTable_Object = MibTable
dvmrpRouteTable = _DvmrpRouteTable_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dvmrpRouteTable.setStatus("current")
_DvmrpRouteEntry_Object = MibTableRow
dvmrpRouteEntry = _DvmrpRouteEntry_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1)
)
dvmrpRouteEntry.setIndexNames(
    (0, "DVMRP-STD-MIB", "dvmrpRouteSource"),
    (0, "DVMRP-STD-MIB", "dvmrpRouteSourceMask"),
)
if mibBuilder.loadTexts:
    dvmrpRouteEntry.setStatus("current")
_DvmrpRouteSource_Type = IpAddress
_DvmrpRouteSource_Object = MibTableColumn
dvmrpRouteSource = _DvmrpRouteSource_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 1),
    _DvmrpRouteSource_Type()
)
dvmrpRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteSource.setStatus("current")
_DvmrpRouteSourceMask_Type = IpAddress
_DvmrpRouteSourceMask_Object = MibTableColumn
dvmrpRouteSourceMask = _DvmrpRouteSourceMask_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 2),
    _DvmrpRouteSourceMask_Type()
)
dvmrpRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteSourceMask.setStatus("current")
_DvmrpRouteUpstreamNeighbor_Type = IpAddress
_DvmrpRouteUpstreamNeighbor_Object = MibTableColumn
dvmrpRouteUpstreamNeighbor = _DvmrpRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 3),
    _DvmrpRouteUpstreamNeighbor_Type()
)
dvmrpRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteUpstreamNeighbor.setStatus("current")
_DvmrpRouteIfIndex_Type = InterfaceIndexOrZero
_DvmrpRouteIfIndex_Object = MibTableColumn
dvmrpRouteIfIndex = _DvmrpRouteIfIndex_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 4),
    _DvmrpRouteIfIndex_Type()
)
dvmrpRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteIfIndex.setStatus("current")


class _DvmrpRouteMetric_Type(Integer32):
    """Custom type dvmrpRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DvmrpRouteMetric_Type.__name__ = "Integer32"
_DvmrpRouteMetric_Object = MibTableColumn
dvmrpRouteMetric = _DvmrpRouteMetric_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 5),
    _DvmrpRouteMetric_Type()
)
dvmrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteMetric.setStatus("current")
_DvmrpRouteExpiryTime_Type = TimeTicks
_DvmrpRouteExpiryTime_Object = MibTableColumn
dvmrpRouteExpiryTime = _DvmrpRouteExpiryTime_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 6),
    _DvmrpRouteExpiryTime_Type()
)
dvmrpRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteExpiryTime.setStatus("current")
_DvmrpRouteUpTime_Type = TimeTicks
_DvmrpRouteUpTime_Object = MibTableColumn
dvmrpRouteUpTime = _DvmrpRouteUpTime_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 7),
    _DvmrpRouteUpTime_Type()
)
dvmrpRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteUpTime.setStatus("current")
_DvmrpRouteNextHopTable_Object = MibTable
dvmrpRouteNextHopTable = _DvmrpRouteNextHopTable_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dvmrpRouteNextHopTable.setStatus("current")
_DvmrpRouteNextHopEntry_Object = MibTableRow
dvmrpRouteNextHopEntry = _DvmrpRouteNextHopEntry_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1)
)
dvmrpRouteNextHopEntry.setIndexNames(
    (0, "DVMRP-STD-MIB", "dvmrpRouteNextHopSource"),
    (0, "DVMRP-STD-MIB", "dvmrpRouteNextHopSourceMask"),
    (0, "DVMRP-STD-MIB", "dvmrpRouteNextHopIfIndex"),
)
if mibBuilder.loadTexts:
    dvmrpRouteNextHopEntry.setStatus("current")
_DvmrpRouteNextHopSource_Type = IpAddress
_DvmrpRouteNextHopSource_Object = MibTableColumn
dvmrpRouteNextHopSource = _DvmrpRouteNextHopSource_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 1),
    _DvmrpRouteNextHopSource_Type()
)
dvmrpRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopSource.setStatus("current")
_DvmrpRouteNextHopSourceMask_Type = IpAddress
_DvmrpRouteNextHopSourceMask_Object = MibTableColumn
dvmrpRouteNextHopSourceMask = _DvmrpRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 2),
    _DvmrpRouteNextHopSourceMask_Type()
)
dvmrpRouteNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopSourceMask.setStatus("current")
_DvmrpRouteNextHopIfIndex_Type = InterfaceIndex
_DvmrpRouteNextHopIfIndex_Object = MibTableColumn
dvmrpRouteNextHopIfIndex = _DvmrpRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 3),
    _DvmrpRouteNextHopIfIndex_Type()
)
dvmrpRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopIfIndex.setStatus("current")


class _DvmrpRouteNextHopType_Type(Integer32):
    """Custom type dvmrpRouteNextHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("branch", 2),
          ("leaf", 1))
    )


_DvmrpRouteNextHopType_Type.__name__ = "Integer32"
_DvmrpRouteNextHopType_Object = MibTableColumn
dvmrpRouteNextHopType = _DvmrpRouteNextHopType_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 4),
    _DvmrpRouteNextHopType_Type()
)
dvmrpRouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopType.setStatus("current")
_DvmrpPruneTable_Object = MibTable
dvmrpPruneTable = _DvmrpPruneTable_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dvmrpPruneTable.setStatus("current")
_DvmrpPruneEntry_Object = MibTableRow
dvmrpPruneEntry = _DvmrpPruneEntry_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 6, 1)
)
dvmrpPruneEntry.setIndexNames(
    (0, "DVMRP-STD-MIB", "dvmrpPruneGroup"),
    (0, "DVMRP-STD-MIB", "dvmrpPruneSource"),
    (0, "DVMRP-STD-MIB", "dvmrpPruneSourceMask"),
)
if mibBuilder.loadTexts:
    dvmrpPruneEntry.setStatus("current")
_DvmrpPruneGroup_Type = IpAddress
_DvmrpPruneGroup_Object = MibTableColumn
dvmrpPruneGroup = _DvmrpPruneGroup_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 1),
    _DvmrpPruneGroup_Type()
)
dvmrpPruneGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpPruneGroup.setStatus("current")
_DvmrpPruneSource_Type = IpAddress
_DvmrpPruneSource_Object = MibTableColumn
dvmrpPruneSource = _DvmrpPruneSource_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 2),
    _DvmrpPruneSource_Type()
)
dvmrpPruneSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpPruneSource.setStatus("current")
_DvmrpPruneSourceMask_Type = IpAddress
_DvmrpPruneSourceMask_Object = MibTableColumn
dvmrpPruneSourceMask = _DvmrpPruneSourceMask_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 3),
    _DvmrpPruneSourceMask_Type()
)
dvmrpPruneSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpPruneSourceMask.setStatus("current")
_DvmrpPruneExpiryTime_Type = TimeTicks
_DvmrpPruneExpiryTime_Object = MibTableColumn
dvmrpPruneExpiryTime = _DvmrpPruneExpiryTime_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 4),
    _DvmrpPruneExpiryTime_Type()
)
dvmrpPruneExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpPruneExpiryTime.setStatus("current")
_DvmrpTraps_ObjectIdentity = ObjectIdentity
dvmrpTraps = _DvmrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 3, 62, 1, 1, 7)
)
_DvmrpMIBConformance_ObjectIdentity = ObjectIdentity
dvmrpMIBConformance = _DvmrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 62, 2)
)
_DvmrpMIBCompliances_ObjectIdentity = ObjectIdentity
dvmrpMIBCompliances = _DvmrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 62, 2, 1)
)
_DvmrpMIBGroups_ObjectIdentity = ObjectIdentity
dvmrpMIBGroups = _DvmrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 62, 2, 2)
)

# Managed Objects groups

dvmrpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 2)
)
dvmrpGeneralGroup.setObjects(
      *(("DVMRP-STD-MIB", "dvmrpVersionString"),
        ("DVMRP-STD-MIB", "dvmrpNumRoutes"),
        ("DVMRP-STD-MIB", "dvmrpReachableRoutes"))
)
if mibBuilder.loadTexts:
    dvmrpGeneralGroup.setStatus("current")

dvmrpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 3)
)
dvmrpInterfaceGroup.setObjects(
      *(("DVMRP-STD-MIB", "dvmrpInterfaceLocalAddress"),
        ("DVMRP-STD-MIB", "dvmrpInterfaceMetric"),
        ("DVMRP-STD-MIB", "dvmrpInterfaceStatus"),
        ("DVMRP-STD-MIB", "dvmrpInterfaceGenerationId"),
        ("DVMRP-STD-MIB", "dvmrpInterfaceRcvBadPkts"),
        ("DVMRP-STD-MIB", "dvmrpInterfaceRcvBadRoutes"),
        ("DVMRP-STD-MIB", "dvmrpInterfaceSentRoutes"))
)
if mibBuilder.loadTexts:
    dvmrpInterfaceGroup.setStatus("current")

dvmrpNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 4)
)
dvmrpNeighborGroup.setObjects(
      *(("DVMRP-STD-MIB", "dvmrpNeighborUpTime"),
        ("DVMRP-STD-MIB", "dvmrpNeighborExpiryTime"),
        ("DVMRP-STD-MIB", "dvmrpNeighborGenerationId"),
        ("DVMRP-STD-MIB", "dvmrpNeighborMajorVersion"),
        ("DVMRP-STD-MIB", "dvmrpNeighborMinorVersion"),
        ("DVMRP-STD-MIB", "dvmrpNeighborCapabilities"),
        ("DVMRP-STD-MIB", "dvmrpNeighborRcvRoutes"),
        ("DVMRP-STD-MIB", "dvmrpNeighborRcvBadPkts"),
        ("DVMRP-STD-MIB", "dvmrpNeighborRcvBadRoutes"),
        ("DVMRP-STD-MIB", "dvmrpNeighborState"))
)
if mibBuilder.loadTexts:
    dvmrpNeighborGroup.setStatus("current")

dvmrpRoutingGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 5)
)
dvmrpRoutingGroup.setObjects(
      *(("DVMRP-STD-MIB", "dvmrpRouteUpstreamNeighbor"),
        ("DVMRP-STD-MIB", "dvmrpRouteIfIndex"),
        ("DVMRP-STD-MIB", "dvmrpRouteMetric"),
        ("DVMRP-STD-MIB", "dvmrpRouteExpiryTime"),
        ("DVMRP-STD-MIB", "dvmrpRouteUpTime"),
        ("DVMRP-STD-MIB", "dvmrpRouteNextHopType"))
)
if mibBuilder.loadTexts:
    dvmrpRoutingGroup.setStatus("current")

dvmrpSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 6)
)
dvmrpSecurityGroup.setObjects(
      *(("DVMRP-STD-MIB", "dvmrpInterfaceKey"),
        ("DVMRP-STD-MIB", "dvmrpInterfaceKeyVersion"))
)
if mibBuilder.loadTexts:
    dvmrpSecurityGroup.setStatus("current")

dvmrpTreeGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 7)
)
dvmrpTreeGroup.setObjects(
    ("DVMRP-STD-MIB", "dvmrpPruneExpiryTime")
)
if mibBuilder.loadTexts:
    dvmrpTreeGroup.setStatus("current")


# Notification objects

dvmrpNeighborLoss = NotificationType(
    (1, 3, 6, 1, 3, 62, 1, 1, 7, 1)
)
dvmrpNeighborLoss.setObjects(
      *(("DVMRP-STD-MIB", "dvmrpInterfaceLocalAddress"),
        ("DVMRP-STD-MIB", "dvmrpNeighborState"))
)
if mibBuilder.loadTexts:
    dvmrpNeighborLoss.setStatus(
        "current"
    )

dvmrpNeighborNotPruning = NotificationType(
    (1, 3, 6, 1, 3, 62, 1, 1, 7, 2)
)
dvmrpNeighborNotPruning.setObjects(
      *(("DVMRP-STD-MIB", "dvmrpInterfaceLocalAddress"),
        ("DVMRP-STD-MIB", "dvmrpNeighborCapabilities"))
)
if mibBuilder.loadTexts:
    dvmrpNeighborNotPruning.setStatus(
        "current"
    )


# Notifications groups

dvmrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 8)
)
dvmrpNotificationGroup.setObjects(
      *(("DVMRP-STD-MIB", "dvmrpNeighborLoss"),
        ("DVMRP-STD-MIB", "dvmrpNeighborNotPruning"))
)
if mibBuilder.loadTexts:
    dvmrpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dvmrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 62, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dvmrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DVMRP-STD-MIB",
    **{"dvmrpStdMIB": dvmrpStdMIB,
       "dvmrpMIBObjects": dvmrpMIBObjects,
       "dvmrp": dvmrp,
       "dvmrpScalar": dvmrpScalar,
       "dvmrpVersionString": dvmrpVersionString,
       "dvmrpNumRoutes": dvmrpNumRoutes,
       "dvmrpReachableRoutes": dvmrpReachableRoutes,
       "dvmrpInterfaceTable": dvmrpInterfaceTable,
       "dvmrpInterfaceEntry": dvmrpInterfaceEntry,
       "dvmrpInterfaceIndex": dvmrpInterfaceIndex,
       "dvmrpInterfaceLocalAddress": dvmrpInterfaceLocalAddress,
       "dvmrpInterfaceMetric": dvmrpInterfaceMetric,
       "dvmrpInterfaceStatus": dvmrpInterfaceStatus,
       "dvmrpInterfaceRcvBadPkts": dvmrpInterfaceRcvBadPkts,
       "dvmrpInterfaceRcvBadRoutes": dvmrpInterfaceRcvBadRoutes,
       "dvmrpInterfaceSentRoutes": dvmrpInterfaceSentRoutes,
       "dvmrpInterfaceKey": dvmrpInterfaceKey,
       "dvmrpInterfaceKeyVersion": dvmrpInterfaceKeyVersion,
       "dvmrpInterfaceGenerationId": dvmrpInterfaceGenerationId,
       "dvmrpNeighborTable": dvmrpNeighborTable,
       "dvmrpNeighborEntry": dvmrpNeighborEntry,
       "dvmrpNeighborIfIndex": dvmrpNeighborIfIndex,
       "dvmrpNeighborAddress": dvmrpNeighborAddress,
       "dvmrpNeighborUpTime": dvmrpNeighborUpTime,
       "dvmrpNeighborExpiryTime": dvmrpNeighborExpiryTime,
       "dvmrpNeighborGenerationId": dvmrpNeighborGenerationId,
       "dvmrpNeighborMajorVersion": dvmrpNeighborMajorVersion,
       "dvmrpNeighborMinorVersion": dvmrpNeighborMinorVersion,
       "dvmrpNeighborCapabilities": dvmrpNeighborCapabilities,
       "dvmrpNeighborRcvRoutes": dvmrpNeighborRcvRoutes,
       "dvmrpNeighborRcvBadPkts": dvmrpNeighborRcvBadPkts,
       "dvmrpNeighborRcvBadRoutes": dvmrpNeighborRcvBadRoutes,
       "dvmrpNeighborState": dvmrpNeighborState,
       "dvmrpRouteTable": dvmrpRouteTable,
       "dvmrpRouteEntry": dvmrpRouteEntry,
       "dvmrpRouteSource": dvmrpRouteSource,
       "dvmrpRouteSourceMask": dvmrpRouteSourceMask,
       "dvmrpRouteUpstreamNeighbor": dvmrpRouteUpstreamNeighbor,
       "dvmrpRouteIfIndex": dvmrpRouteIfIndex,
       "dvmrpRouteMetric": dvmrpRouteMetric,
       "dvmrpRouteExpiryTime": dvmrpRouteExpiryTime,
       "dvmrpRouteUpTime": dvmrpRouteUpTime,
       "dvmrpRouteNextHopTable": dvmrpRouteNextHopTable,
       "dvmrpRouteNextHopEntry": dvmrpRouteNextHopEntry,
       "dvmrpRouteNextHopSource": dvmrpRouteNextHopSource,
       "dvmrpRouteNextHopSourceMask": dvmrpRouteNextHopSourceMask,
       "dvmrpRouteNextHopIfIndex": dvmrpRouteNextHopIfIndex,
       "dvmrpRouteNextHopType": dvmrpRouteNextHopType,
       "dvmrpPruneTable": dvmrpPruneTable,
       "dvmrpPruneEntry": dvmrpPruneEntry,
       "dvmrpPruneGroup": dvmrpPruneGroup,
       "dvmrpPruneSource": dvmrpPruneSource,
       "dvmrpPruneSourceMask": dvmrpPruneSourceMask,
       "dvmrpPruneExpiryTime": dvmrpPruneExpiryTime,
       "dvmrpTraps": dvmrpTraps,
       "dvmrpNeighborLoss": dvmrpNeighborLoss,
       "dvmrpNeighborNotPruning": dvmrpNeighborNotPruning,
       "dvmrpMIBConformance": dvmrpMIBConformance,
       "dvmrpMIBCompliances": dvmrpMIBCompliances,
       "dvmrpMIBCompliance": dvmrpMIBCompliance,
       "dvmrpMIBGroups": dvmrpMIBGroups,
       "dvmrpGeneralGroup": dvmrpGeneralGroup,
       "dvmrpInterfaceGroup": dvmrpInterfaceGroup,
       "dvmrpNeighborGroup": dvmrpNeighborGroup,
       "dvmrpRoutingGroup": dvmrpRoutingGroup,
       "dvmrpSecurityGroup": dvmrpSecurityGroup,
       "dvmrpTreeGroup": dvmrpTreeGroup,
       "dvmrpNotificationGroup": dvmrpNotificationGroup}
)
