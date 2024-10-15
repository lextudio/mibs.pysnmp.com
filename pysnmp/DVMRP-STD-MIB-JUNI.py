# SNMP MIB module (DVMRP-STD-MIB-JUNI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DVMRP-STD-MIB-JUNI
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:58 2024
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

(juniDvmrpExperiment,) = mibBuilder.importSymbols(
    "Juniper-Experiment",
    "juniDvmrpExperiment")

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

junidDvmrpStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1)
)
junidDvmrpStdMIB.setRevisions(
        ("1999-10-19 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JunidDvmrpMIBObjects_ObjectIdentity = ObjectIdentity
junidDvmrpMIBObjects = _JunidDvmrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1)
)
_JunidDvmrp_ObjectIdentity = ObjectIdentity
junidDvmrp = _JunidDvmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1)
)
_JunidDvmrpTraps_ObjectIdentity = ObjectIdentity
junidDvmrpTraps = _JunidDvmrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 0)
)
_JunidDvmrpScalar_ObjectIdentity = ObjectIdentity
junidDvmrpScalar = _JunidDvmrpScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1)
)
_JunidDvmrpVersionString_Type = DisplayString
_JunidDvmrpVersionString_Object = MibScalar
junidDvmrpVersionString = _JunidDvmrpVersionString_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1, 1),
    _JunidDvmrpVersionString_Type()
)
junidDvmrpVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpVersionString.setStatus("current")
_JunidDvmrpGenerationId_Type = Integer32
_JunidDvmrpGenerationId_Object = MibScalar
junidDvmrpGenerationId = _JunidDvmrpGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1, 2),
    _JunidDvmrpGenerationId_Type()
)
junidDvmrpGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpGenerationId.setStatus("current")
_JunidDvmrpNumRoutes_Type = Gauge32
_JunidDvmrpNumRoutes_Object = MibScalar
junidDvmrpNumRoutes = _JunidDvmrpNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1, 3),
    _JunidDvmrpNumRoutes_Type()
)
junidDvmrpNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpNumRoutes.setStatus("current")
_JunidDvmrpReachableRoutes_Type = Gauge32
_JunidDvmrpReachableRoutes_Object = MibScalar
junidDvmrpReachableRoutes = _JunidDvmrpReachableRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1, 4),
    _JunidDvmrpReachableRoutes_Type()
)
junidDvmrpReachableRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpReachableRoutes.setStatus("current")
_JunidDvmrpInterfaceTable_Object = MibTable
junidDvmrpInterfaceTable = _JunidDvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    junidDvmrpInterfaceTable.setStatus("current")
_JunidDvmrpInterfaceEntry_Object = MibTableRow
junidDvmrpInterfaceEntry = _JunidDvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1)
)
junidDvmrpInterfaceEntry.setIndexNames(
    (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    junidDvmrpInterfaceEntry.setStatus("current")
_JunidDvmrpInterfaceIfIndex_Type = InterfaceIndex
_JunidDvmrpInterfaceIfIndex_Object = MibTableColumn
junidDvmrpInterfaceIfIndex = _JunidDvmrpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 1),
    _JunidDvmrpInterfaceIfIndex_Type()
)
junidDvmrpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidDvmrpInterfaceIfIndex.setStatus("current")
_JunidDvmrpInterfaceLocalAddress_Type = IpAddress
_JunidDvmrpInterfaceLocalAddress_Object = MibTableColumn
junidDvmrpInterfaceLocalAddress = _JunidDvmrpInterfaceLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 2),
    _JunidDvmrpInterfaceLocalAddress_Type()
)
junidDvmrpInterfaceLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidDvmrpInterfaceLocalAddress.setStatus("current")


class _JunidDvmrpInterfaceMetric_Type(Integer32):
    """Custom type junidDvmrpInterfaceMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_JunidDvmrpInterfaceMetric_Type.__name__ = "Integer32"
_JunidDvmrpInterfaceMetric_Object = MibTableColumn
junidDvmrpInterfaceMetric = _JunidDvmrpInterfaceMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 3),
    _JunidDvmrpInterfaceMetric_Type()
)
junidDvmrpInterfaceMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidDvmrpInterfaceMetric.setStatus("current")
_JunidDvmrpInterfaceStatus_Type = RowStatus
_JunidDvmrpInterfaceStatus_Object = MibTableColumn
junidDvmrpInterfaceStatus = _JunidDvmrpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 4),
    _JunidDvmrpInterfaceStatus_Type()
)
junidDvmrpInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidDvmrpInterfaceStatus.setStatus("current")
_JunidDvmrpInterfaceRcvBadPkts_Type = Counter32
_JunidDvmrpInterfaceRcvBadPkts_Object = MibTableColumn
junidDvmrpInterfaceRcvBadPkts = _JunidDvmrpInterfaceRcvBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 5),
    _JunidDvmrpInterfaceRcvBadPkts_Type()
)
junidDvmrpInterfaceRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpInterfaceRcvBadPkts.setStatus("current")
_JunidDvmrpInterfaceRcvBadRoutes_Type = Counter32
_JunidDvmrpInterfaceRcvBadRoutes_Object = MibTableColumn
junidDvmrpInterfaceRcvBadRoutes = _JunidDvmrpInterfaceRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 6),
    _JunidDvmrpInterfaceRcvBadRoutes_Type()
)
junidDvmrpInterfaceRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpInterfaceRcvBadRoutes.setStatus("current")
_JunidDvmrpInterfaceSentRoutes_Type = Counter32
_JunidDvmrpInterfaceSentRoutes_Object = MibTableColumn
junidDvmrpInterfaceSentRoutes = _JunidDvmrpInterfaceSentRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 7),
    _JunidDvmrpInterfaceSentRoutes_Type()
)
junidDvmrpInterfaceSentRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpInterfaceSentRoutes.setStatus("current")
_JunidDvmrpInterfaceInterfaceKey_Type = SnmpAdminString
_JunidDvmrpInterfaceInterfaceKey_Object = MibTableColumn
junidDvmrpInterfaceInterfaceKey = _JunidDvmrpInterfaceInterfaceKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 8),
    _JunidDvmrpInterfaceInterfaceKey_Type()
)
junidDvmrpInterfaceInterfaceKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidDvmrpInterfaceInterfaceKey.setStatus("current")
_JunidDvmrpInterfaceInterfaceKeyVersion_Type = Integer32
_JunidDvmrpInterfaceInterfaceKeyVersion_Object = MibTableColumn
junidDvmrpInterfaceInterfaceKeyVersion = _JunidDvmrpInterfaceInterfaceKeyVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 9),
    _JunidDvmrpInterfaceInterfaceKeyVersion_Type()
)
junidDvmrpInterfaceInterfaceKeyVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidDvmrpInterfaceInterfaceKeyVersion.setStatus("current")
_JunidDvmrpNeighborTable_Object = MibTable
junidDvmrpNeighborTable = _JunidDvmrpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    junidDvmrpNeighborTable.setStatus("current")
_JunidDvmrpNeighborEntry_Object = MibTableRow
junidDvmrpNeighborEntry = _JunidDvmrpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1)
)
junidDvmrpNeighborEntry.setIndexNames(
    (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborIfIndex"),
    (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborAddress"),
)
if mibBuilder.loadTexts:
    junidDvmrpNeighborEntry.setStatus("current")
_JunidDvmrpNeighborIfIndex_Type = InterfaceIndex
_JunidDvmrpNeighborIfIndex_Object = MibTableColumn
junidDvmrpNeighborIfIndex = _JunidDvmrpNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 1),
    _JunidDvmrpNeighborIfIndex_Type()
)
junidDvmrpNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidDvmrpNeighborIfIndex.setStatus("current")
_JunidDvmrpNeighborAddress_Type = IpAddress
_JunidDvmrpNeighborAddress_Object = MibTableColumn
junidDvmrpNeighborAddress = _JunidDvmrpNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 2),
    _JunidDvmrpNeighborAddress_Type()
)
junidDvmrpNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidDvmrpNeighborAddress.setStatus("current")
_JunidDvmrpNeighborUpTime_Type = TimeTicks
_JunidDvmrpNeighborUpTime_Object = MibTableColumn
junidDvmrpNeighborUpTime = _JunidDvmrpNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 3),
    _JunidDvmrpNeighborUpTime_Type()
)
junidDvmrpNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpNeighborUpTime.setStatus("current")
_JunidDvmrpNeighborExpiryTime_Type = TimeTicks
_JunidDvmrpNeighborExpiryTime_Object = MibTableColumn
junidDvmrpNeighborExpiryTime = _JunidDvmrpNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 4),
    _JunidDvmrpNeighborExpiryTime_Type()
)
junidDvmrpNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpNeighborExpiryTime.setStatus("current")
_JunidDvmrpNeighborGenerationId_Type = Integer32
_JunidDvmrpNeighborGenerationId_Object = MibTableColumn
junidDvmrpNeighborGenerationId = _JunidDvmrpNeighborGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 5),
    _JunidDvmrpNeighborGenerationId_Type()
)
junidDvmrpNeighborGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpNeighborGenerationId.setStatus("current")


class _JunidDvmrpNeighborMajorVersion_Type(Integer32):
    """Custom type junidDvmrpNeighborMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JunidDvmrpNeighborMajorVersion_Type.__name__ = "Integer32"
_JunidDvmrpNeighborMajorVersion_Object = MibTableColumn
junidDvmrpNeighborMajorVersion = _JunidDvmrpNeighborMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 6),
    _JunidDvmrpNeighborMajorVersion_Type()
)
junidDvmrpNeighborMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpNeighborMajorVersion.setStatus("current")


class _JunidDvmrpNeighborMinorVersion_Type(Integer32):
    """Custom type junidDvmrpNeighborMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JunidDvmrpNeighborMinorVersion_Type.__name__ = "Integer32"
_JunidDvmrpNeighborMinorVersion_Object = MibTableColumn
junidDvmrpNeighborMinorVersion = _JunidDvmrpNeighborMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 7),
    _JunidDvmrpNeighborMinorVersion_Type()
)
junidDvmrpNeighborMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpNeighborMinorVersion.setStatus("current")


class _JunidDvmrpNeighborCapabilities_Type(Bits):
    """Custom type junidDvmrpNeighborCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("generationID", 2),
          ("leaf", 0),
          ("mtrace", 3),
          ("prune", 1))
    )

_JunidDvmrpNeighborCapabilities_Type.__name__ = "Bits"
_JunidDvmrpNeighborCapabilities_Object = MibTableColumn
junidDvmrpNeighborCapabilities = _JunidDvmrpNeighborCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 8),
    _JunidDvmrpNeighborCapabilities_Type()
)
junidDvmrpNeighborCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpNeighborCapabilities.setStatus("current")
_JunidDvmrpNeighborRcvRoutes_Type = Counter32
_JunidDvmrpNeighborRcvRoutes_Object = MibTableColumn
junidDvmrpNeighborRcvRoutes = _JunidDvmrpNeighborRcvRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 9),
    _JunidDvmrpNeighborRcvRoutes_Type()
)
junidDvmrpNeighborRcvRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpNeighborRcvRoutes.setStatus("current")
_JunidDvmrpNeighborRcvBadPkts_Type = Counter32
_JunidDvmrpNeighborRcvBadPkts_Object = MibTableColumn
junidDvmrpNeighborRcvBadPkts = _JunidDvmrpNeighborRcvBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 10),
    _JunidDvmrpNeighborRcvBadPkts_Type()
)
junidDvmrpNeighborRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpNeighborRcvBadPkts.setStatus("current")
_JunidDvmrpNeighborRcvBadRoutes_Type = Counter32
_JunidDvmrpNeighborRcvBadRoutes_Object = MibTableColumn
junidDvmrpNeighborRcvBadRoutes = _JunidDvmrpNeighborRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 11),
    _JunidDvmrpNeighborRcvBadRoutes_Type()
)
junidDvmrpNeighborRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpNeighborRcvBadRoutes.setStatus("current")


class _JunidDvmrpNeighborState_Type(Integer32):
    """Custom type junidDvmrpNeighborState based on Integer32"""
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


_JunidDvmrpNeighborState_Type.__name__ = "Integer32"
_JunidDvmrpNeighborState_Object = MibTableColumn
junidDvmrpNeighborState = _JunidDvmrpNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 12),
    _JunidDvmrpNeighborState_Type()
)
junidDvmrpNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpNeighborState.setStatus("current")
_JunidDvmrpRouteTable_Object = MibTable
junidDvmrpRouteTable = _JunidDvmrpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    junidDvmrpRouteTable.setStatus("current")
_JunidDvmrpRouteEntry_Object = MibTableRow
junidDvmrpRouteEntry = _JunidDvmrpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1)
)
junidDvmrpRouteEntry.setIndexNames(
    (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpRouteSource"),
    (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpRouteSourceMask"),
)
if mibBuilder.loadTexts:
    junidDvmrpRouteEntry.setStatus("current")
_JunidDvmrpRouteSource_Type = IpAddress
_JunidDvmrpRouteSource_Object = MibTableColumn
junidDvmrpRouteSource = _JunidDvmrpRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 1),
    _JunidDvmrpRouteSource_Type()
)
junidDvmrpRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidDvmrpRouteSource.setStatus("current")
_JunidDvmrpRouteSourceMask_Type = IpAddress
_JunidDvmrpRouteSourceMask_Object = MibTableColumn
junidDvmrpRouteSourceMask = _JunidDvmrpRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 2),
    _JunidDvmrpRouteSourceMask_Type()
)
junidDvmrpRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidDvmrpRouteSourceMask.setStatus("current")
_JunidDvmrpRouteUpstreamNeighbor_Type = IpAddress
_JunidDvmrpRouteUpstreamNeighbor_Object = MibTableColumn
junidDvmrpRouteUpstreamNeighbor = _JunidDvmrpRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 3),
    _JunidDvmrpRouteUpstreamNeighbor_Type()
)
junidDvmrpRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpRouteUpstreamNeighbor.setStatus("current")
_JunidDvmrpRouteIfIndex_Type = InterfaceIndexOrZero
_JunidDvmrpRouteIfIndex_Object = MibTableColumn
junidDvmrpRouteIfIndex = _JunidDvmrpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 4),
    _JunidDvmrpRouteIfIndex_Type()
)
junidDvmrpRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpRouteIfIndex.setStatus("current")


class _JunidDvmrpRouteMetric_Type(Integer32):
    """Custom type junidDvmrpRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_JunidDvmrpRouteMetric_Type.__name__ = "Integer32"
_JunidDvmrpRouteMetric_Object = MibTableColumn
junidDvmrpRouteMetric = _JunidDvmrpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 5),
    _JunidDvmrpRouteMetric_Type()
)
junidDvmrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpRouteMetric.setStatus("current")
_JunidDvmrpRouteExpiryTime_Type = TimeTicks
_JunidDvmrpRouteExpiryTime_Object = MibTableColumn
junidDvmrpRouteExpiryTime = _JunidDvmrpRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 6),
    _JunidDvmrpRouteExpiryTime_Type()
)
junidDvmrpRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpRouteExpiryTime.setStatus("current")
_JunidDvmrpRouteUpTime_Type = TimeTicks
_JunidDvmrpRouteUpTime_Object = MibTableColumn
junidDvmrpRouteUpTime = _JunidDvmrpRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 7),
    _JunidDvmrpRouteUpTime_Type()
)
junidDvmrpRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpRouteUpTime.setStatus("current")
_JunidDvmrpRouteNextHopTable_Object = MibTable
junidDvmrpRouteNextHopTable = _JunidDvmrpRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    junidDvmrpRouteNextHopTable.setStatus("current")
_JunidDvmrpRouteNextHopEntry_Object = MibTableRow
junidDvmrpRouteNextHopEntry = _JunidDvmrpRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1)
)
junidDvmrpRouteNextHopEntry.setIndexNames(
    (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpRouteNextHopSource"),
    (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpRouteNextHopSourceMask"),
    (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpRouteNextHopIfIndex"),
)
if mibBuilder.loadTexts:
    junidDvmrpRouteNextHopEntry.setStatus("current")
_JunidDvmrpRouteNextHopSource_Type = IpAddress
_JunidDvmrpRouteNextHopSource_Object = MibTableColumn
junidDvmrpRouteNextHopSource = _JunidDvmrpRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1, 1),
    _JunidDvmrpRouteNextHopSource_Type()
)
junidDvmrpRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidDvmrpRouteNextHopSource.setStatus("current")
_JunidDvmrpRouteNextHopSourceMask_Type = IpAddress
_JunidDvmrpRouteNextHopSourceMask_Object = MibTableColumn
junidDvmrpRouteNextHopSourceMask = _JunidDvmrpRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1, 2),
    _JunidDvmrpRouteNextHopSourceMask_Type()
)
junidDvmrpRouteNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidDvmrpRouteNextHopSourceMask.setStatus("current")
_JunidDvmrpRouteNextHopIfIndex_Type = InterfaceIndex
_JunidDvmrpRouteNextHopIfIndex_Object = MibTableColumn
junidDvmrpRouteNextHopIfIndex = _JunidDvmrpRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1, 3),
    _JunidDvmrpRouteNextHopIfIndex_Type()
)
junidDvmrpRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidDvmrpRouteNextHopIfIndex.setStatus("current")


class _JunidDvmrpRouteNextHopType_Type(Integer32):
    """Custom type junidDvmrpRouteNextHopType based on Integer32"""
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


_JunidDvmrpRouteNextHopType_Type.__name__ = "Integer32"
_JunidDvmrpRouteNextHopType_Object = MibTableColumn
junidDvmrpRouteNextHopType = _JunidDvmrpRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1, 4),
    _JunidDvmrpRouteNextHopType_Type()
)
junidDvmrpRouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpRouteNextHopType.setStatus("current")
_JunidDvmrpPruneTable_Object = MibTable
junidDvmrpPruneTable = _JunidDvmrpPruneTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    junidDvmrpPruneTable.setStatus("current")
_JunidDvmrpPruneEntry_Object = MibTableRow
junidDvmrpPruneEntry = _JunidDvmrpPruneEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1)
)
junidDvmrpPruneEntry.setIndexNames(
    (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpPruneGroup"),
    (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpPruneSource"),
    (0, "DVMRP-STD-MIB-JUNI", "junidDvmrpPruneSourceMask"),
)
if mibBuilder.loadTexts:
    junidDvmrpPruneEntry.setStatus("current")
_JunidDvmrpPruneGroup_Type = IpAddress
_JunidDvmrpPruneGroup_Object = MibTableColumn
junidDvmrpPruneGroup = _JunidDvmrpPruneGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1, 1),
    _JunidDvmrpPruneGroup_Type()
)
junidDvmrpPruneGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidDvmrpPruneGroup.setStatus("current")
_JunidDvmrpPruneSource_Type = IpAddress
_JunidDvmrpPruneSource_Object = MibTableColumn
junidDvmrpPruneSource = _JunidDvmrpPruneSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1, 2),
    _JunidDvmrpPruneSource_Type()
)
junidDvmrpPruneSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidDvmrpPruneSource.setStatus("current")
_JunidDvmrpPruneSourceMask_Type = IpAddress
_JunidDvmrpPruneSourceMask_Object = MibTableColumn
junidDvmrpPruneSourceMask = _JunidDvmrpPruneSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1, 3),
    _JunidDvmrpPruneSourceMask_Type()
)
junidDvmrpPruneSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidDvmrpPruneSourceMask.setStatus("current")
_JunidDvmrpPruneExpiryTime_Type = TimeTicks
_JunidDvmrpPruneExpiryTime_Object = MibTableColumn
junidDvmrpPruneExpiryTime = _JunidDvmrpPruneExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1, 4),
    _JunidDvmrpPruneExpiryTime_Type()
)
junidDvmrpPruneExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidDvmrpPruneExpiryTime.setStatus("current")
_JunidDvmrpMIBConformance_ObjectIdentity = ObjectIdentity
junidDvmrpMIBConformance = _JunidDvmrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2)
)
_JunidDvmrpMIBCompliances_ObjectIdentity = ObjectIdentity
junidDvmrpMIBCompliances = _JunidDvmrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 1)
)
_JunidDvmrpMIBGroups_ObjectIdentity = ObjectIdentity
junidDvmrpMIBGroups = _JunidDvmrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2)
)

# Managed Objects groups

junidDvmrpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 2)
)
junidDvmrpGeneralGroup.setObjects(
      *(("DVMRP-STD-MIB-JUNI", "junidDvmrpVersionString"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpGenerationId"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNumRoutes"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpReachableRoutes"))
)
if mibBuilder.loadTexts:
    junidDvmrpGeneralGroup.setStatus("current")

junidDvmrpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 3)
)
junidDvmrpInterfaceGroup.setObjects(
      *(("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceLocalAddress"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceMetric"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceStatus"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceRcvBadPkts"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceRcvBadRoutes"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceSentRoutes"))
)
if mibBuilder.loadTexts:
    junidDvmrpInterfaceGroup.setStatus("current")

junidDvmrpNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 4)
)
junidDvmrpNeighborGroup.setObjects(
      *(("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborUpTime"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborExpiryTime"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborGenerationId"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborMajorVersion"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborMinorVersion"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborCapabilities"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborRcvRoutes"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborRcvBadPkts"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborRcvBadRoutes"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborState"))
)
if mibBuilder.loadTexts:
    junidDvmrpNeighborGroup.setStatus("current")

junidDvmrpRoutingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 5)
)
junidDvmrpRoutingGroup.setObjects(
      *(("DVMRP-STD-MIB-JUNI", "junidDvmrpRouteUpstreamNeighbor"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpRouteIfIndex"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpRouteMetric"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpRouteExpiryTime"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpRouteUpTime"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpRouteNextHopType"))
)
if mibBuilder.loadTexts:
    junidDvmrpRoutingGroup.setStatus("current")

junidDvmrpSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 6)
)
junidDvmrpSecurityGroup.setObjects(
      *(("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceInterfaceKey"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceInterfaceKeyVersion"))
)
if mibBuilder.loadTexts:
    junidDvmrpSecurityGroup.setStatus("current")

junidDvmrpTreeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 7)
)
junidDvmrpTreeGroup.setObjects(
    ("DVMRP-STD-MIB-JUNI", "junidDvmrpPruneExpiryTime")
)
if mibBuilder.loadTexts:
    junidDvmrpTreeGroup.setStatus("current")


# Notification objects

junidDvmrpNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 0, 1)
)
junidDvmrpNeighborLoss.setObjects(
      *(("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceLocalAddress"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborState"))
)
if mibBuilder.loadTexts:
    junidDvmrpNeighborLoss.setStatus(
        "current"
    )

junidDvmrpNeighborNotPruning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 0, 2)
)
junidDvmrpNeighborNotPruning.setObjects(
      *(("DVMRP-STD-MIB-JUNI", "junidDvmrpInterfaceLocalAddress"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborCapabilities"))
)
if mibBuilder.loadTexts:
    junidDvmrpNeighborNotPruning.setStatus(
        "current"
    )


# Notifications groups

junidDvmrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 8)
)
junidDvmrpNotificationGroup.setObjects(
      *(("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborLoss"),
        ("DVMRP-STD-MIB-JUNI", "junidDvmrpNeighborNotPruning"))
)
if mibBuilder.loadTexts:
    junidDvmrpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

junidDvmrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    junidDvmrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DVMRP-STD-MIB-JUNI",
    **{"junidDvmrpStdMIB": junidDvmrpStdMIB,
       "junidDvmrpMIBObjects": junidDvmrpMIBObjects,
       "junidDvmrp": junidDvmrp,
       "junidDvmrpTraps": junidDvmrpTraps,
       "junidDvmrpNeighborLoss": junidDvmrpNeighborLoss,
       "junidDvmrpNeighborNotPruning": junidDvmrpNeighborNotPruning,
       "junidDvmrpScalar": junidDvmrpScalar,
       "junidDvmrpVersionString": junidDvmrpVersionString,
       "junidDvmrpGenerationId": junidDvmrpGenerationId,
       "junidDvmrpNumRoutes": junidDvmrpNumRoutes,
       "junidDvmrpReachableRoutes": junidDvmrpReachableRoutes,
       "junidDvmrpInterfaceTable": junidDvmrpInterfaceTable,
       "junidDvmrpInterfaceEntry": junidDvmrpInterfaceEntry,
       "junidDvmrpInterfaceIfIndex": junidDvmrpInterfaceIfIndex,
       "junidDvmrpInterfaceLocalAddress": junidDvmrpInterfaceLocalAddress,
       "junidDvmrpInterfaceMetric": junidDvmrpInterfaceMetric,
       "junidDvmrpInterfaceStatus": junidDvmrpInterfaceStatus,
       "junidDvmrpInterfaceRcvBadPkts": junidDvmrpInterfaceRcvBadPkts,
       "junidDvmrpInterfaceRcvBadRoutes": junidDvmrpInterfaceRcvBadRoutes,
       "junidDvmrpInterfaceSentRoutes": junidDvmrpInterfaceSentRoutes,
       "junidDvmrpInterfaceInterfaceKey": junidDvmrpInterfaceInterfaceKey,
       "junidDvmrpInterfaceInterfaceKeyVersion": junidDvmrpInterfaceInterfaceKeyVersion,
       "junidDvmrpNeighborTable": junidDvmrpNeighborTable,
       "junidDvmrpNeighborEntry": junidDvmrpNeighborEntry,
       "junidDvmrpNeighborIfIndex": junidDvmrpNeighborIfIndex,
       "junidDvmrpNeighborAddress": junidDvmrpNeighborAddress,
       "junidDvmrpNeighborUpTime": junidDvmrpNeighborUpTime,
       "junidDvmrpNeighborExpiryTime": junidDvmrpNeighborExpiryTime,
       "junidDvmrpNeighborGenerationId": junidDvmrpNeighborGenerationId,
       "junidDvmrpNeighborMajorVersion": junidDvmrpNeighborMajorVersion,
       "junidDvmrpNeighborMinorVersion": junidDvmrpNeighborMinorVersion,
       "junidDvmrpNeighborCapabilities": junidDvmrpNeighborCapabilities,
       "junidDvmrpNeighborRcvRoutes": junidDvmrpNeighborRcvRoutes,
       "junidDvmrpNeighborRcvBadPkts": junidDvmrpNeighborRcvBadPkts,
       "junidDvmrpNeighborRcvBadRoutes": junidDvmrpNeighborRcvBadRoutes,
       "junidDvmrpNeighborState": junidDvmrpNeighborState,
       "junidDvmrpRouteTable": junidDvmrpRouteTable,
       "junidDvmrpRouteEntry": junidDvmrpRouteEntry,
       "junidDvmrpRouteSource": junidDvmrpRouteSource,
       "junidDvmrpRouteSourceMask": junidDvmrpRouteSourceMask,
       "junidDvmrpRouteUpstreamNeighbor": junidDvmrpRouteUpstreamNeighbor,
       "junidDvmrpRouteIfIndex": junidDvmrpRouteIfIndex,
       "junidDvmrpRouteMetric": junidDvmrpRouteMetric,
       "junidDvmrpRouteExpiryTime": junidDvmrpRouteExpiryTime,
       "junidDvmrpRouteUpTime": junidDvmrpRouteUpTime,
       "junidDvmrpRouteNextHopTable": junidDvmrpRouteNextHopTable,
       "junidDvmrpRouteNextHopEntry": junidDvmrpRouteNextHopEntry,
       "junidDvmrpRouteNextHopSource": junidDvmrpRouteNextHopSource,
       "junidDvmrpRouteNextHopSourceMask": junidDvmrpRouteNextHopSourceMask,
       "junidDvmrpRouteNextHopIfIndex": junidDvmrpRouteNextHopIfIndex,
       "junidDvmrpRouteNextHopType": junidDvmrpRouteNextHopType,
       "junidDvmrpPruneTable": junidDvmrpPruneTable,
       "junidDvmrpPruneEntry": junidDvmrpPruneEntry,
       "junidDvmrpPruneGroup": junidDvmrpPruneGroup,
       "junidDvmrpPruneSource": junidDvmrpPruneSource,
       "junidDvmrpPruneSourceMask": junidDvmrpPruneSourceMask,
       "junidDvmrpPruneExpiryTime": junidDvmrpPruneExpiryTime,
       "junidDvmrpMIBConformance": junidDvmrpMIBConformance,
       "junidDvmrpMIBCompliances": junidDvmrpMIBCompliances,
       "junidDvmrpMIBCompliance": junidDvmrpMIBCompliance,
       "junidDvmrpMIBGroups": junidDvmrpMIBGroups,
       "junidDvmrpGeneralGroup": junidDvmrpGeneralGroup,
       "junidDvmrpInterfaceGroup": junidDvmrpInterfaceGroup,
       "junidDvmrpNeighborGroup": junidDvmrpNeighborGroup,
       "junidDvmrpRoutingGroup": junidDvmrpRoutingGroup,
       "junidDvmrpSecurityGroup": junidDvmrpSecurityGroup,
       "junidDvmrpTreeGroup": junidDvmrpTreeGroup,
       "junidDvmrpNotificationGroup": junidDvmrpNotificationGroup}
)
