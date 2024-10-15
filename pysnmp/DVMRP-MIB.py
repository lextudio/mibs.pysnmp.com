# SNMP MIB module (DVMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DVMRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:54 2024
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

dvmrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 62)
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
_DvmrpVersionString_Type = DisplayString
_DvmrpVersionString_Object = MibScalar
dvmrpVersionString = _DvmrpVersionString_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 1),
    _DvmrpVersionString_Type()
)
dvmrpVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpVersionString.setStatus("current")
_DvmrpGenerationId_Type = Integer32
_DvmrpGenerationId_Object = MibScalar
dvmrpGenerationId = _DvmrpGenerationId_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 2),
    _DvmrpGenerationId_Type()
)
dvmrpGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpGenerationId.setStatus("current")
_DvmrpInterfaceTable_Object = MibTable
dvmrpInterfaceTable = _DvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dvmrpInterfaceTable.setStatus("current")
_DvmrpInterfaceEntry_Object = MibTableRow
dvmrpInterfaceEntry = _DvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1)
)
dvmrpInterfaceEntry.setIndexNames(
    (0, "DVMRP-MIB", "dvmrpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    dvmrpInterfaceEntry.setStatus("current")
_DvmrpInterfaceIfIndex_Type = Integer32
_DvmrpInterfaceIfIndex_Object = MibTableColumn
dvmrpInterfaceIfIndex = _DvmrpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 1),
    _DvmrpInterfaceIfIndex_Type()
)
dvmrpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpInterfaceIfIndex.setStatus("current")


class _DvmrpInterfaceType_Type(Integer32):
    """Custom type dvmrpInterfaceType based on Integer32"""
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
        *(("querier", 3),
          ("srcrt", 2),
          ("subnet", 4),
          ("tunnel", 1))
    )


_DvmrpInterfaceType_Type.__name__ = "Integer32"
_DvmrpInterfaceType_Object = MibTableColumn
dvmrpInterfaceType = _DvmrpInterfaceType_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 2),
    _DvmrpInterfaceType_Type()
)
dvmrpInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceType.setStatus("deprecated")


class _DvmrpInterfaceOperState_Type(Integer32):
    """Custom type dvmrpInterfaceOperState based on Integer32"""
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


_DvmrpInterfaceOperState_Type.__name__ = "Integer32"
_DvmrpInterfaceOperState_Object = MibTableColumn
dvmrpInterfaceOperState = _DvmrpInterfaceOperState_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 3),
    _DvmrpInterfaceOperState_Type()
)
dvmrpInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceOperState.setStatus("deprecated")
_DvmrpInterfaceLocalAddress_Type = IpAddress
_DvmrpInterfaceLocalAddress_Object = MibTableColumn
dvmrpInterfaceLocalAddress = _DvmrpInterfaceLocalAddress_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 4),
    _DvmrpInterfaceLocalAddress_Type()
)
dvmrpInterfaceLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceLocalAddress.setStatus("current")
_DvmrpInterfaceRemoteAddress_Type = IpAddress
_DvmrpInterfaceRemoteAddress_Object = MibTableColumn
dvmrpInterfaceRemoteAddress = _DvmrpInterfaceRemoteAddress_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 5),
    _DvmrpInterfaceRemoteAddress_Type()
)
dvmrpInterfaceRemoteAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceRemoteAddress.setStatus("deprecated")
_DvmrpInterfaceRemoteSubnetMask_Type = IpAddress
_DvmrpInterfaceRemoteSubnetMask_Object = MibTableColumn
dvmrpInterfaceRemoteSubnetMask = _DvmrpInterfaceRemoteSubnetMask_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 6),
    _DvmrpInterfaceRemoteSubnetMask_Type()
)
dvmrpInterfaceRemoteSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceRemoteSubnetMask.setStatus("deprecated")


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
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 7),
    _DvmrpInterfaceMetric_Type()
)
dvmrpInterfaceMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceMetric.setStatus("current")


class _DvmrpInterfaceRateLimit_Type(Integer32):
    """Custom type dvmrpInterfaceRateLimit based on Integer32"""
    defaultValue = 0


_DvmrpInterfaceRateLimit_Object = MibTableColumn
dvmrpInterfaceRateLimit = _DvmrpInterfaceRateLimit_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 8),
    _DvmrpInterfaceRateLimit_Type()
)
dvmrpInterfaceRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceRateLimit.setStatus("deprecated")
_DvmrpInterfaceInPkts_Type = Counter32
_DvmrpInterfaceInPkts_Object = MibTableColumn
dvmrpInterfaceInPkts = _DvmrpInterfaceInPkts_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 9),
    _DvmrpInterfaceInPkts_Type()
)
dvmrpInterfaceInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceInPkts.setStatus("deprecated")
_DvmrpInterfaceOutPkts_Type = Counter32
_DvmrpInterfaceOutPkts_Object = MibTableColumn
dvmrpInterfaceOutPkts = _DvmrpInterfaceOutPkts_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 10),
    _DvmrpInterfaceOutPkts_Type()
)
dvmrpInterfaceOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceOutPkts.setStatus("deprecated")
_DvmrpInterfaceInOctets_Type = Counter32
_DvmrpInterfaceInOctets_Object = MibTableColumn
dvmrpInterfaceInOctets = _DvmrpInterfaceInOctets_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 11),
    _DvmrpInterfaceInOctets_Type()
)
dvmrpInterfaceInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceInOctets.setStatus("deprecated")
_DvmrpInterfaceOutOctets_Type = Counter32
_DvmrpInterfaceOutOctets_Object = MibTableColumn
dvmrpInterfaceOutOctets = _DvmrpInterfaceOutOctets_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 12),
    _DvmrpInterfaceOutOctets_Type()
)
dvmrpInterfaceOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceOutOctets.setStatus("deprecated")
_DvmrpInterfaceStatus_Type = RowStatus
_DvmrpInterfaceStatus_Object = MibTableColumn
dvmrpInterfaceStatus = _DvmrpInterfaceStatus_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 13),
    _DvmrpInterfaceStatus_Type()
)
dvmrpInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceStatus.setStatus("current")
_DvmrpInterfaceRcvBadPkts_Type = Counter32
_DvmrpInterfaceRcvBadPkts_Object = MibTableColumn
dvmrpInterfaceRcvBadPkts = _DvmrpInterfaceRcvBadPkts_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 14),
    _DvmrpInterfaceRcvBadPkts_Type()
)
dvmrpInterfaceRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceRcvBadPkts.setStatus("current")
_DvmrpInterfaceRcvBadRoutes_Type = Counter32
_DvmrpInterfaceRcvBadRoutes_Object = MibTableColumn
dvmrpInterfaceRcvBadRoutes = _DvmrpInterfaceRcvBadRoutes_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 15),
    _DvmrpInterfaceRcvBadRoutes_Type()
)
dvmrpInterfaceRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceRcvBadRoutes.setStatus("current")
_DvmrpInterfaceSentRoutes_Type = Counter32
_DvmrpInterfaceSentRoutes_Object = MibTableColumn
dvmrpInterfaceSentRoutes = _DvmrpInterfaceSentRoutes_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 16),
    _DvmrpInterfaceSentRoutes_Type()
)
dvmrpInterfaceSentRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceSentRoutes.setStatus("current")
_DvmrpInterfaceMasterKey_Type = DisplayString
_DvmrpInterfaceMasterKey_Object = MibTableColumn
dvmrpInterfaceMasterKey = _DvmrpInterfaceMasterKey_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 17),
    _DvmrpInterfaceMasterKey_Type()
)
dvmrpInterfaceMasterKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceMasterKey.setStatus("current")
_DvmrpInterfaceMasterKeyVersion_Type = Integer32
_DvmrpInterfaceMasterKeyVersion_Object = MibTableColumn
dvmrpInterfaceMasterKeyVersion = _DvmrpInterfaceMasterKeyVersion_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 18),
    _DvmrpInterfaceMasterKeyVersion_Type()
)
dvmrpInterfaceMasterKeyVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceMasterKeyVersion.setStatus("current")
_DvmrpNeighborTable_Object = MibTable
dvmrpNeighborTable = _DvmrpNeighborTable_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dvmrpNeighborTable.setStatus("current")
_DvmrpNeighborEntry_Object = MibTableRow
dvmrpNeighborEntry = _DvmrpNeighborEntry_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1)
)
dvmrpNeighborEntry.setIndexNames(
    (0, "DVMRP-MIB", "dvmrpNeighborIfIndex"),
    (0, "DVMRP-MIB", "dvmrpNeighborAddress"),
)
if mibBuilder.loadTexts:
    dvmrpNeighborEntry.setStatus("current")
_DvmrpNeighborIfIndex_Type = Integer32
_DvmrpNeighborIfIndex_Object = MibTableColumn
dvmrpNeighborIfIndex = _DvmrpNeighborIfIndex_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 1),
    _DvmrpNeighborIfIndex_Type()
)
dvmrpNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborIfIndex.setStatus("current")
_DvmrpNeighborAddress_Type = IpAddress
_DvmrpNeighborAddress_Object = MibTableColumn
dvmrpNeighborAddress = _DvmrpNeighborAddress_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 2),
    _DvmrpNeighborAddress_Type()
)
dvmrpNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborAddress.setStatus("current")
_DvmrpNeighborUpTime_Type = TimeTicks
_DvmrpNeighborUpTime_Object = MibTableColumn
dvmrpNeighborUpTime = _DvmrpNeighborUpTime_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 3),
    _DvmrpNeighborUpTime_Type()
)
dvmrpNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborUpTime.setStatus("current")
_DvmrpNeighborExpiryTime_Type = TimeTicks
_DvmrpNeighborExpiryTime_Object = MibTableColumn
dvmrpNeighborExpiryTime = _DvmrpNeighborExpiryTime_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 4),
    _DvmrpNeighborExpiryTime_Type()
)
dvmrpNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborExpiryTime.setStatus("current")
_DvmrpNeighborGenerationId_Type = Integer32
_DvmrpNeighborGenerationId_Object = MibTableColumn
dvmrpNeighborGenerationId = _DvmrpNeighborGenerationId_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 6),
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
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 7),
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
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 8),
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
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 9),
    _DvmrpNeighborCapabilities_Type()
)
dvmrpNeighborCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborCapabilities.setStatus("current")
_DvmrpNeighborRcvRoutes_Type = Counter32
_DvmrpNeighborRcvRoutes_Object = MibTableColumn
dvmrpNeighborRcvRoutes = _DvmrpNeighborRcvRoutes_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 10),
    _DvmrpNeighborRcvRoutes_Type()
)
dvmrpNeighborRcvRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborRcvRoutes.setStatus("current")
_DvmrpNeighborRcvBadPkts_Type = Counter32
_DvmrpNeighborRcvBadPkts_Object = MibTableColumn
dvmrpNeighborRcvBadPkts = _DvmrpNeighborRcvBadPkts_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 11),
    _DvmrpNeighborRcvBadPkts_Type()
)
dvmrpNeighborRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborRcvBadPkts.setStatus("current")
_DvmrpNeighborRcvBadRoutes_Type = Counter32
_DvmrpNeighborRcvBadRoutes_Object = MibTableColumn
dvmrpNeighborRcvBadRoutes = _DvmrpNeighborRcvBadRoutes_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 12),
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
    (1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 13),
    _DvmrpNeighborState_Type()
)
dvmrpNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborState.setStatus("current")
_DvmrpRouteTable_Object = MibTable
dvmrpRouteTable = _DvmrpRouteTable_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dvmrpRouteTable.setStatus("current")
_DvmrpRouteEntry_Object = MibTableRow
dvmrpRouteEntry = _DvmrpRouteEntry_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1)
)
dvmrpRouteEntry.setIndexNames(
    (0, "DVMRP-MIB", "dvmrpRouteSource"),
    (0, "DVMRP-MIB", "dvmrpRouteSourceMask"),
)
if mibBuilder.loadTexts:
    dvmrpRouteEntry.setStatus("current")
_DvmrpRouteSource_Type = IpAddress
_DvmrpRouteSource_Object = MibTableColumn
dvmrpRouteSource = _DvmrpRouteSource_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 1),
    _DvmrpRouteSource_Type()
)
dvmrpRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteSource.setStatus("current")
_DvmrpRouteSourceMask_Type = IpAddress
_DvmrpRouteSourceMask_Object = MibTableColumn
dvmrpRouteSourceMask = _DvmrpRouteSourceMask_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 2),
    _DvmrpRouteSourceMask_Type()
)
dvmrpRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteSourceMask.setStatus("current")
_DvmrpRouteUpstreamNeighbor_Type = IpAddress
_DvmrpRouteUpstreamNeighbor_Object = MibTableColumn
dvmrpRouteUpstreamNeighbor = _DvmrpRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 3),
    _DvmrpRouteUpstreamNeighbor_Type()
)
dvmrpRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteUpstreamNeighbor.setStatus("current")
_DvmrpRouteIfIndex_Type = Integer32
_DvmrpRouteIfIndex_Object = MibTableColumn
dvmrpRouteIfIndex = _DvmrpRouteIfIndex_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 4),
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
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 5),
    _DvmrpRouteMetric_Type()
)
dvmrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteMetric.setStatus("current")
_DvmrpRouteExpiryTime_Type = TimeTicks
_DvmrpRouteExpiryTime_Object = MibTableColumn
dvmrpRouteExpiryTime = _DvmrpRouteExpiryTime_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 6),
    _DvmrpRouteExpiryTime_Type()
)
dvmrpRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteExpiryTime.setStatus("current")
_DvmrpRouteUpTime_Type = TimeTicks
_DvmrpRouteUpTime_Object = MibTableColumn
dvmrpRouteUpTime = _DvmrpRouteUpTime_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 7),
    _DvmrpRouteUpTime_Type()
)
dvmrpRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteUpTime.setStatus("current")
_DvmrpRouteNextHopTable_Object = MibTable
dvmrpRouteNextHopTable = _DvmrpRouteNextHopTable_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dvmrpRouteNextHopTable.setStatus("current")
_DvmrpRouteNextHopEntry_Object = MibTableRow
dvmrpRouteNextHopEntry = _DvmrpRouteNextHopEntry_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 6, 1)
)
dvmrpRouteNextHopEntry.setIndexNames(
    (0, "DVMRP-MIB", "dvmrpRouteNextHopSource"),
    (0, "DVMRP-MIB", "dvmrpRouteNextHopSourceMask"),
    (0, "DVMRP-MIB", "dvmrpRouteNextHopIfIndex"),
)
if mibBuilder.loadTexts:
    dvmrpRouteNextHopEntry.setStatus("current")
_DvmrpRouteNextHopSource_Type = IpAddress
_DvmrpRouteNextHopSource_Object = MibTableColumn
dvmrpRouteNextHopSource = _DvmrpRouteNextHopSource_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 1),
    _DvmrpRouteNextHopSource_Type()
)
dvmrpRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopSource.setStatus("current")
_DvmrpRouteNextHopSourceMask_Type = IpAddress
_DvmrpRouteNextHopSourceMask_Object = MibTableColumn
dvmrpRouteNextHopSourceMask = _DvmrpRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 2),
    _DvmrpRouteNextHopSourceMask_Type()
)
dvmrpRouteNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopSourceMask.setStatus("current")
_DvmrpRouteNextHopIfIndex_Type = Integer32
_DvmrpRouteNextHopIfIndex_Object = MibTableColumn
dvmrpRouteNextHopIfIndex = _DvmrpRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 3),
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
    (1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 4),
    _DvmrpRouteNextHopType_Type()
)
dvmrpRouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopType.setStatus("current")
_DvmrpAltNetTable_Object = MibTable
dvmrpAltNetTable = _DvmrpAltNetTable_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 8)
)
if mibBuilder.loadTexts:
    dvmrpAltNetTable.setStatus("deprecated")
_DvmrpAltNetEntry_Object = MibTableRow
dvmrpAltNetEntry = _DvmrpAltNetEntry_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 8, 1)
)
dvmrpAltNetEntry.setIndexNames(
    (0, "DVMRP-MIB", "dvmrpAltNetIfIndex"),
    (0, "DVMRP-MIB", "dvmrpAltNetAddress"),
    (0, "DVMRP-MIB", "dvmrpAltNetMask"),
)
if mibBuilder.loadTexts:
    dvmrpAltNetEntry.setStatus("deprecated")
_DvmrpAltNetIfIndex_Type = Integer32
_DvmrpAltNetIfIndex_Object = MibTableColumn
dvmrpAltNetIfIndex = _DvmrpAltNetIfIndex_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 8, 1, 1),
    _DvmrpAltNetIfIndex_Type()
)
dvmrpAltNetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpAltNetIfIndex.setStatus("deprecated")
_DvmrpAltNetAddress_Type = IpAddress
_DvmrpAltNetAddress_Object = MibTableColumn
dvmrpAltNetAddress = _DvmrpAltNetAddress_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 8, 1, 2),
    _DvmrpAltNetAddress_Type()
)
dvmrpAltNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpAltNetAddress.setStatus("deprecated")
_DvmrpAltNetMask_Type = IpAddress
_DvmrpAltNetMask_Object = MibTableColumn
dvmrpAltNetMask = _DvmrpAltNetMask_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 8, 1, 3),
    _DvmrpAltNetMask_Type()
)
dvmrpAltNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpAltNetMask.setStatus("deprecated")
_DvmrpAltNetStatus_Type = RowStatus
_DvmrpAltNetStatus_Object = MibTableColumn
dvmrpAltNetStatus = _DvmrpAltNetStatus_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 8, 1, 4),
    _DvmrpAltNetStatus_Type()
)
dvmrpAltNetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpAltNetStatus.setStatus("deprecated")
_DvmrpNumRoutes_Type = Gauge32
_DvmrpNumRoutes_Object = MibScalar
dvmrpNumRoutes = _DvmrpNumRoutes_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 9),
    _DvmrpNumRoutes_Type()
)
dvmrpNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNumRoutes.setStatus("current")
_DvmrpReachableRoutes_Type = Gauge32
_DvmrpReachableRoutes_Object = MibScalar
dvmrpReachableRoutes = _DvmrpReachableRoutes_Object(
    (1, 3, 6, 1, 3, 62, 1, 1, 10),
    _DvmrpReachableRoutes_Type()
)
dvmrpReachableRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpReachableRoutes.setStatus("current")
_DvmrpTraps_ObjectIdentity = ObjectIdentity
dvmrpTraps = _DvmrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 3, 62, 1, 1, 11)
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

dvmrpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 1)
)
dvmrpMIBGroup.setObjects(
      *(("DVMRP-MIB", "dvmrpVersionString"),
        ("DVMRP-MIB", "dvmrpGenerationId"),
        ("DVMRP-MIB", "dvmrpNumRoutes"),
        ("DVMRP-MIB", "dvmrpReachableRoutes"),
        ("DVMRP-MIB", "dvmrpInterfaceType"),
        ("DVMRP-MIB", "dvmrpInterfaceOperState"),
        ("DVMRP-MIB", "dvmrpInterfaceLocalAddress"),
        ("DVMRP-MIB", "dvmrpInterfaceRemoteAddress"),
        ("DVMRP-MIB", "dvmrpInterfaceRemoteSubnetMask"),
        ("DVMRP-MIB", "dvmrpInterfaceMetric"),
        ("DVMRP-MIB", "dvmrpInterfaceRateLimit"),
        ("DVMRP-MIB", "dvmrpInterfaceInPkts"),
        ("DVMRP-MIB", "dvmrpInterfaceOutPkts"),
        ("DVMRP-MIB", "dvmrpInterfaceInOctets"),
        ("DVMRP-MIB", "dvmrpInterfaceOutOctets"),
        ("DVMRP-MIB", "dvmrpInterfaceStatus"),
        ("DVMRP-MIB", "dvmrpNeighborUpTime"),
        ("DVMRP-MIB", "dvmrpNeighborExpiryTime"),
        ("DVMRP-MIB", "dvmrpNeighborGenerationId"),
        ("DVMRP-MIB", "dvmrpNeighborMajorVersion"),
        ("DVMRP-MIB", "dvmrpNeighborMinorVersion"),
        ("DVMRP-MIB", "dvmrpNeighborCapabilities"),
        ("DVMRP-MIB", "dvmrpRouteUpstreamNeighbor"),
        ("DVMRP-MIB", "dvmrpRouteIfIndex"),
        ("DVMRP-MIB", "dvmrpRouteMetric"),
        ("DVMRP-MIB", "dvmrpRouteExpiryTime"),
        ("DVMRP-MIB", "dvmrpRouteNextHopType"),
        ("DVMRP-MIB", "dvmrpAltNetStatus"))
)
if mibBuilder.loadTexts:
    dvmrpMIBGroup.setStatus("deprecated")

dvmrpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 2)
)
dvmrpGeneralGroup.setObjects(
      *(("DVMRP-MIB", "dvmrpVersionString"),
        ("DVMRP-MIB", "dvmrpGenerationId"),
        ("DVMRP-MIB", "dvmrpNumRoutes"),
        ("DVMRP-MIB", "dvmrpReachableRoutes"))
)
if mibBuilder.loadTexts:
    dvmrpGeneralGroup.setStatus("current")

dvmrpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 3)
)
dvmrpInterfaceGroup.setObjects(
      *(("DVMRP-MIB", "dvmrpInterfaceLocalAddress"),
        ("DVMRP-MIB", "dvmrpInterfaceMetric"),
        ("DVMRP-MIB", "dvmrpInterfaceStatus"),
        ("DVMRP-MIB", "dvmrpInterfaceRcvBadPkts"),
        ("DVMRP-MIB", "dvmrpInterfaceRcvBadRoutes"),
        ("DVMRP-MIB", "dvmrpInterfaceSentRoutes"))
)
if mibBuilder.loadTexts:
    dvmrpInterfaceGroup.setStatus("current")

dvmrpNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 4)
)
dvmrpNeighborGroup.setObjects(
      *(("DVMRP-MIB", "dvmrpNeighborUpTime"),
        ("DVMRP-MIB", "dvmrpNeighborExpiryTime"),
        ("DVMRP-MIB", "dvmrpNeighborGenerationId"),
        ("DVMRP-MIB", "dvmrpNeighborMajorVersion"),
        ("DVMRP-MIB", "dvmrpNeighborMinorVersion"),
        ("DVMRP-MIB", "dvmrpNeighborCapabilities"),
        ("DVMRP-MIB", "dvmrpNeighborRcvRoutes"),
        ("DVMRP-MIB", "dvmrpNeighborRcvBadPkts"),
        ("DVMRP-MIB", "dvmrpNeighborRcvBadRoutes"),
        ("DVMRP-MIB", "dvmrpNeighborState"))
)
if mibBuilder.loadTexts:
    dvmrpNeighborGroup.setStatus("current")

dvmrpRoutingGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 5)
)
dvmrpRoutingGroup.setObjects(
      *(("DVMRP-MIB", "dvmrpRouteUpstreamNeighbor"),
        ("DVMRP-MIB", "dvmrpRouteIfIndex"),
        ("DVMRP-MIB", "dvmrpRouteMetric"),
        ("DVMRP-MIB", "dvmrpRouteExpiryTime"),
        ("DVMRP-MIB", "dvmrpRouteUpTime"),
        ("DVMRP-MIB", "dvmrpRouteNextHopType"))
)
if mibBuilder.loadTexts:
    dvmrpRoutingGroup.setStatus("current")

dvmrpSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 62, 2, 2, 6)
)
dvmrpSecurityGroup.setObjects(
      *(("DVMRP-MIB", "dvmrpInterfaceMasterKey"),
        ("DVMRP-MIB", "dvmrpInterfaceMasterKeyVersion"))
)
if mibBuilder.loadTexts:
    dvmrpSecurityGroup.setStatus("current")


# Notification objects

dvmrpNeighborLoss = NotificationType(
    (1, 3, 6, 1, 3, 62, 1, 1, 11, 1)
)
dvmrpNeighborLoss.setObjects(
      *(("DVMRP-MIB", "dvmrpInterfaceLocalAddress"),
        ("DVMRP-MIB", "dvmrpNeighborIfIndex"),
        ("DVMRP-MIB", "dvmrpNeighborAddress"),
        ("DVMRP-MIB", "dvmrpNeighborState"))
)
if mibBuilder.loadTexts:
    dvmrpNeighborLoss.setStatus(
        "current"
    )

dvmrpNeighborNotPruning = NotificationType(
    (1, 3, 6, 1, 3, 62, 1, 1, 11, 2)
)
dvmrpNeighborNotPruning.setObjects(
      *(("DVMRP-MIB", "dvmrpInterfaceLocalAddress"),
        ("DVMRP-MIB", "dvmrpNeighborIfIndex"),
        ("DVMRP-MIB", "dvmrpNeighborAddress"))
)
if mibBuilder.loadTexts:
    dvmrpNeighborNotPruning.setStatus(
        "current"
    )


# Notifications groups


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
    "DVMRP-MIB",
    **{"dvmrpMIB": dvmrpMIB,
       "dvmrpMIBObjects": dvmrpMIBObjects,
       "dvmrp": dvmrp,
       "dvmrpVersionString": dvmrpVersionString,
       "dvmrpGenerationId": dvmrpGenerationId,
       "dvmrpInterfaceTable": dvmrpInterfaceTable,
       "dvmrpInterfaceEntry": dvmrpInterfaceEntry,
       "dvmrpInterfaceIfIndex": dvmrpInterfaceIfIndex,
       "dvmrpInterfaceType": dvmrpInterfaceType,
       "dvmrpInterfaceOperState": dvmrpInterfaceOperState,
       "dvmrpInterfaceLocalAddress": dvmrpInterfaceLocalAddress,
       "dvmrpInterfaceRemoteAddress": dvmrpInterfaceRemoteAddress,
       "dvmrpInterfaceRemoteSubnetMask": dvmrpInterfaceRemoteSubnetMask,
       "dvmrpInterfaceMetric": dvmrpInterfaceMetric,
       "dvmrpInterfaceRateLimit": dvmrpInterfaceRateLimit,
       "dvmrpInterfaceInPkts": dvmrpInterfaceInPkts,
       "dvmrpInterfaceOutPkts": dvmrpInterfaceOutPkts,
       "dvmrpInterfaceInOctets": dvmrpInterfaceInOctets,
       "dvmrpInterfaceOutOctets": dvmrpInterfaceOutOctets,
       "dvmrpInterfaceStatus": dvmrpInterfaceStatus,
       "dvmrpInterfaceRcvBadPkts": dvmrpInterfaceRcvBadPkts,
       "dvmrpInterfaceRcvBadRoutes": dvmrpInterfaceRcvBadRoutes,
       "dvmrpInterfaceSentRoutes": dvmrpInterfaceSentRoutes,
       "dvmrpInterfaceMasterKey": dvmrpInterfaceMasterKey,
       "dvmrpInterfaceMasterKeyVersion": dvmrpInterfaceMasterKeyVersion,
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
       "dvmrpAltNetTable": dvmrpAltNetTable,
       "dvmrpAltNetEntry": dvmrpAltNetEntry,
       "dvmrpAltNetIfIndex": dvmrpAltNetIfIndex,
       "dvmrpAltNetAddress": dvmrpAltNetAddress,
       "dvmrpAltNetMask": dvmrpAltNetMask,
       "dvmrpAltNetStatus": dvmrpAltNetStatus,
       "dvmrpNumRoutes": dvmrpNumRoutes,
       "dvmrpReachableRoutes": dvmrpReachableRoutes,
       "dvmrpTraps": dvmrpTraps,
       "dvmrpNeighborLoss": dvmrpNeighborLoss,
       "dvmrpNeighborNotPruning": dvmrpNeighborNotPruning,
       "dvmrpMIBConformance": dvmrpMIBConformance,
       "dvmrpMIBCompliances": dvmrpMIBCompliances,
       "dvmrpMIBCompliance": dvmrpMIBCompliance,
       "dvmrpMIBGroups": dvmrpMIBGroups,
       "dvmrpMIBGroup": dvmrpMIBGroup,
       "dvmrpGeneralGroup": dvmrpGeneralGroup,
       "dvmrpInterfaceGroup": dvmrpInterfaceGroup,
       "dvmrpNeighborGroup": dvmrpNeighborGroup,
       "dvmrpRoutingGroup": dvmrpRoutingGroup,
       "dvmrpSecurityGroup": dvmrpSecurityGroup}
)
