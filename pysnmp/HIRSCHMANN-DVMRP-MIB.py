# SNMP MIB module (HIRSCHMANN-DVMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIRSCHMANN-DVMRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:35 2024
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

(hmPlatform4Multicast,) = mibBuilder.importSymbols(
    "HIRSCHMANN-MULTICAST-MIB",
    "hmPlatform4Multicast")

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

hmDVMRPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100)
)
hmDVMRPMIB.setRevisions(
        ("2010-04-12 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmDVMRPMIBObjects_ObjectIdentity = ObjectIdentity
hmDVMRPMIBObjects = _HmDVMRPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1)
)
_HmDVMRP_ObjectIdentity = ObjectIdentity
hmDVMRP = _HmDVMRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1)
)
_HmDVMRPScalar_ObjectIdentity = ObjectIdentity
hmDVMRPScalar = _HmDVMRPScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1)
)
_HmDVMRPVersionString_Type = DisplayString
_HmDVMRPVersionString_Object = MibScalar
hmDVMRPVersionString = _HmDVMRPVersionString_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 1),
    _HmDVMRPVersionString_Type()
)
hmDVMRPVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPVersionString.setStatus("current")
_HmDVMRPGenerationId_Type = Integer32
_HmDVMRPGenerationId_Object = MibScalar
hmDVMRPGenerationId = _HmDVMRPGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 2),
    _HmDVMRPGenerationId_Type()
)
hmDVMRPGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPGenerationId.setStatus("obsolete")
_HmDVMRPNumRoutes_Type = Gauge32
_HmDVMRPNumRoutes_Object = MibScalar
hmDVMRPNumRoutes = _HmDVMRPNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 3),
    _HmDVMRPNumRoutes_Type()
)
hmDVMRPNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPNumRoutes.setStatus("current")
_HmDVMRPReachableRoutes_Type = Gauge32
_HmDVMRPReachableRoutes_Object = MibScalar
hmDVMRPReachableRoutes = _HmDVMRPReachableRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 4),
    _HmDVMRPReachableRoutes_Type()
)
hmDVMRPReachableRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPReachableRoutes.setStatus("current")


class _HmDVMRPUpdateInterval_Type(Integer32):
    """Custom type hmDVMRPUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 240),
    )


_HmDVMRPUpdateInterval_Type.__name__ = "Integer32"
_HmDVMRPUpdateInterval_Object = MibScalar
hmDVMRPUpdateInterval = _HmDVMRPUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 10),
    _HmDVMRPUpdateInterval_Type()
)
hmDVMRPUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDVMRPUpdateInterval.setStatus("current")


class _HmDVMRPPruneLifetime_Type(Integer32):
    """Custom type hmDVMRPPruneLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 64800),
    )


_HmDVMRPPruneLifetime_Type.__name__ = "Integer32"
_HmDVMRPPruneLifetime_Object = MibScalar
hmDVMRPPruneLifetime = _HmDVMRPPruneLifetime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 1, 11),
    _HmDVMRPPruneLifetime_Type()
)
hmDVMRPPruneLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDVMRPPruneLifetime.setStatus("current")
_HmDVMRPInterfaceTable_Object = MibTable
hmDVMRPInterfaceTable = _HmDVMRPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hmDVMRPInterfaceTable.setStatus("current")
_HmDVMRPInterfaceEntry_Object = MibTableRow
hmDVMRPInterfaceEntry = _HmDVMRPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1)
)
hmDVMRPInterfaceEntry.setIndexNames(
    (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    hmDVMRPInterfaceEntry.setStatus("current")
_HmDVMRPInterfaceIfIndex_Type = InterfaceIndex
_HmDVMRPInterfaceIfIndex_Object = MibTableColumn
hmDVMRPInterfaceIfIndex = _HmDVMRPInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 1),
    _HmDVMRPInterfaceIfIndex_Type()
)
hmDVMRPInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmDVMRPInterfaceIfIndex.setStatus("current")
_HmDVMRPInterfaceLocalAddress_Type = IpAddress
_HmDVMRPInterfaceLocalAddress_Object = MibTableColumn
hmDVMRPInterfaceLocalAddress = _HmDVMRPInterfaceLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 2),
    _HmDVMRPInterfaceLocalAddress_Type()
)
hmDVMRPInterfaceLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPInterfaceLocalAddress.setStatus("current")


class _HmDVMRPInterfaceMetric_Type(Integer32):
    """Custom type hmDVMRPInterfaceMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_HmDVMRPInterfaceMetric_Type.__name__ = "Integer32"
_HmDVMRPInterfaceMetric_Object = MibTableColumn
hmDVMRPInterfaceMetric = _HmDVMRPInterfaceMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 3),
    _HmDVMRPInterfaceMetric_Type()
)
hmDVMRPInterfaceMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDVMRPInterfaceMetric.setStatus("current")


class _HmDVMRPInterfaceStatus_Type(Integer32):
    """Custom type hmDVMRPInterfaceStatus based on Integer32"""
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


_HmDVMRPInterfaceStatus_Type.__name__ = "Integer32"
_HmDVMRPInterfaceStatus_Object = MibTableColumn
hmDVMRPInterfaceStatus = _HmDVMRPInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 4),
    _HmDVMRPInterfaceStatus_Type()
)
hmDVMRPInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDVMRPInterfaceStatus.setStatus("current")
_HmDVMRPInterfaceRcvBadPkts_Type = Counter32
_HmDVMRPInterfaceRcvBadPkts_Object = MibTableColumn
hmDVMRPInterfaceRcvBadPkts = _HmDVMRPInterfaceRcvBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 5),
    _HmDVMRPInterfaceRcvBadPkts_Type()
)
hmDVMRPInterfaceRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPInterfaceRcvBadPkts.setStatus("current")
_HmDVMRPInterfaceRcvBadRoutes_Type = Counter32
_HmDVMRPInterfaceRcvBadRoutes_Object = MibTableColumn
hmDVMRPInterfaceRcvBadRoutes = _HmDVMRPInterfaceRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 6),
    _HmDVMRPInterfaceRcvBadRoutes_Type()
)
hmDVMRPInterfaceRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPInterfaceRcvBadRoutes.setStatus("current")
_HmDVMRPInterfaceSentRoutes_Type = Counter32
_HmDVMRPInterfaceSentRoutes_Object = MibTableColumn
hmDVMRPInterfaceSentRoutes = _HmDVMRPInterfaceSentRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 7),
    _HmDVMRPInterfaceSentRoutes_Type()
)
hmDVMRPInterfaceSentRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPInterfaceSentRoutes.setStatus("current")
_HmDVMRPInterfaceInterfaceKey_Type = SnmpAdminString
_HmDVMRPInterfaceInterfaceKey_Object = MibTableColumn
hmDVMRPInterfaceInterfaceKey = _HmDVMRPInterfaceInterfaceKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 8),
    _HmDVMRPInterfaceInterfaceKey_Type()
)
hmDVMRPInterfaceInterfaceKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDVMRPInterfaceInterfaceKey.setStatus("current")
_HmDVMRPInterfaceInterfaceKeyVersion_Type = Integer32
_HmDVMRPInterfaceInterfaceKeyVersion_Object = MibTableColumn
hmDVMRPInterfaceInterfaceKeyVersion = _HmDVMRPInterfaceInterfaceKeyVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 9),
    _HmDVMRPInterfaceInterfaceKeyVersion_Type()
)
hmDVMRPInterfaceInterfaceKeyVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDVMRPInterfaceInterfaceKeyVersion.setStatus("current")
_HmDVMRPInterfaceGenerationId_Type = Unsigned32
_HmDVMRPInterfaceGenerationId_Object = MibTableColumn
hmDVMRPInterfaceGenerationId = _HmDVMRPInterfaceGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 2, 1, 20),
    _HmDVMRPInterfaceGenerationId_Type()
)
hmDVMRPInterfaceGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPInterfaceGenerationId.setStatus("current")
_HmDVMRPNeighborTable_Object = MibTable
hmDVMRPNeighborTable = _HmDVMRPNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hmDVMRPNeighborTable.setStatus("current")
_HmDVMRPNeighborEntry_Object = MibTableRow
hmDVMRPNeighborEntry = _HmDVMRPNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1)
)
hmDVMRPNeighborEntry.setIndexNames(
    (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborIfIndex"),
    (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborAddress"),
)
if mibBuilder.loadTexts:
    hmDVMRPNeighborEntry.setStatus("current")
_HmDVMRPNeighborIfIndex_Type = InterfaceIndex
_HmDVMRPNeighborIfIndex_Object = MibTableColumn
hmDVMRPNeighborIfIndex = _HmDVMRPNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 1),
    _HmDVMRPNeighborIfIndex_Type()
)
hmDVMRPNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmDVMRPNeighborIfIndex.setStatus("current")
_HmDVMRPNeighborAddress_Type = IpAddress
_HmDVMRPNeighborAddress_Object = MibTableColumn
hmDVMRPNeighborAddress = _HmDVMRPNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 2),
    _HmDVMRPNeighborAddress_Type()
)
hmDVMRPNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmDVMRPNeighborAddress.setStatus("current")
_HmDVMRPNeighborUpTime_Type = TimeTicks
_HmDVMRPNeighborUpTime_Object = MibTableColumn
hmDVMRPNeighborUpTime = _HmDVMRPNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 3),
    _HmDVMRPNeighborUpTime_Type()
)
hmDVMRPNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPNeighborUpTime.setStatus("current")
_HmDVMRPNeighborExpiryTime_Type = TimeTicks
_HmDVMRPNeighborExpiryTime_Object = MibTableColumn
hmDVMRPNeighborExpiryTime = _HmDVMRPNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 4),
    _HmDVMRPNeighborExpiryTime_Type()
)
hmDVMRPNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPNeighborExpiryTime.setStatus("current")
_HmDVMRPNeighborGenerationId_Type = Integer32
_HmDVMRPNeighborGenerationId_Object = MibTableColumn
hmDVMRPNeighborGenerationId = _HmDVMRPNeighborGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 5),
    _HmDVMRPNeighborGenerationId_Type()
)
hmDVMRPNeighborGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPNeighborGenerationId.setStatus("current")


class _HmDVMRPNeighborMajorVersion_Type(Integer32):
    """Custom type hmDVMRPNeighborMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmDVMRPNeighborMajorVersion_Type.__name__ = "Integer32"
_HmDVMRPNeighborMajorVersion_Object = MibTableColumn
hmDVMRPNeighborMajorVersion = _HmDVMRPNeighborMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 6),
    _HmDVMRPNeighborMajorVersion_Type()
)
hmDVMRPNeighborMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPNeighborMajorVersion.setStatus("current")


class _HmDVMRPNeighborMinorVersion_Type(Integer32):
    """Custom type hmDVMRPNeighborMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmDVMRPNeighborMinorVersion_Type.__name__ = "Integer32"
_HmDVMRPNeighborMinorVersion_Object = MibTableColumn
hmDVMRPNeighborMinorVersion = _HmDVMRPNeighborMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 7),
    _HmDVMRPNeighborMinorVersion_Type()
)
hmDVMRPNeighborMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPNeighborMinorVersion.setStatus("current")


class _HmDVMRPNeighborCapabilities_Type(Bits):
    """Custom type hmDVMRPNeighborCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("generationID", 2),
          ("leaf", 0),
          ("mtrace", 3),
          ("prune", 1))
    )

_HmDVMRPNeighborCapabilities_Type.__name__ = "Bits"
_HmDVMRPNeighborCapabilities_Object = MibTableColumn
hmDVMRPNeighborCapabilities = _HmDVMRPNeighborCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 8),
    _HmDVMRPNeighborCapabilities_Type()
)
hmDVMRPNeighborCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPNeighborCapabilities.setStatus("current")
_HmDVMRPNeighborRcvRoutes_Type = Counter32
_HmDVMRPNeighborRcvRoutes_Object = MibTableColumn
hmDVMRPNeighborRcvRoutes = _HmDVMRPNeighborRcvRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 9),
    _HmDVMRPNeighborRcvRoutes_Type()
)
hmDVMRPNeighborRcvRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPNeighborRcvRoutes.setStatus("current")
_HmDVMRPNeighborRcvBadPkts_Type = Counter32
_HmDVMRPNeighborRcvBadPkts_Object = MibTableColumn
hmDVMRPNeighborRcvBadPkts = _HmDVMRPNeighborRcvBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 10),
    _HmDVMRPNeighborRcvBadPkts_Type()
)
hmDVMRPNeighborRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPNeighborRcvBadPkts.setStatus("current")
_HmDVMRPNeighborRcvBadRoutes_Type = Counter32
_HmDVMRPNeighborRcvBadRoutes_Object = MibTableColumn
hmDVMRPNeighborRcvBadRoutes = _HmDVMRPNeighborRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 11),
    _HmDVMRPNeighborRcvBadRoutes_Type()
)
hmDVMRPNeighborRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPNeighborRcvBadRoutes.setStatus("current")


class _HmDVMRPNeighborState_Type(Integer32):
    """Custom type hmDVMRPNeighborState based on Integer32"""
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


_HmDVMRPNeighborState_Type.__name__ = "Integer32"
_HmDVMRPNeighborState_Object = MibTableColumn
hmDVMRPNeighborState = _HmDVMRPNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 3, 1, 12),
    _HmDVMRPNeighborState_Type()
)
hmDVMRPNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPNeighborState.setStatus("current")
_HmDVMRPRouteTable_Object = MibTable
hmDVMRPRouteTable = _HmDVMRPRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hmDVMRPRouteTable.setStatus("current")
_HmDVMRPRouteEntry_Object = MibTableRow
hmDVMRPRouteEntry = _HmDVMRPRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1)
)
hmDVMRPRouteEntry.setIndexNames(
    (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteSource"),
    (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteSourceMask"),
)
if mibBuilder.loadTexts:
    hmDVMRPRouteEntry.setStatus("current")
_HmDVMRPRouteSource_Type = IpAddress
_HmDVMRPRouteSource_Object = MibTableColumn
hmDVMRPRouteSource = _HmDVMRPRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 1),
    _HmDVMRPRouteSource_Type()
)
hmDVMRPRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmDVMRPRouteSource.setStatus("current")
_HmDVMRPRouteSourceMask_Type = IpAddress
_HmDVMRPRouteSourceMask_Object = MibTableColumn
hmDVMRPRouteSourceMask = _HmDVMRPRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 2),
    _HmDVMRPRouteSourceMask_Type()
)
hmDVMRPRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmDVMRPRouteSourceMask.setStatus("current")
_HmDVMRPRouteUpstreamNeighbor_Type = IpAddress
_HmDVMRPRouteUpstreamNeighbor_Object = MibTableColumn
hmDVMRPRouteUpstreamNeighbor = _HmDVMRPRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 3),
    _HmDVMRPRouteUpstreamNeighbor_Type()
)
hmDVMRPRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPRouteUpstreamNeighbor.setStatus("current")
_HmDVMRPRouteIfIndex_Type = InterfaceIndexOrZero
_HmDVMRPRouteIfIndex_Object = MibTableColumn
hmDVMRPRouteIfIndex = _HmDVMRPRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 4),
    _HmDVMRPRouteIfIndex_Type()
)
hmDVMRPRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPRouteIfIndex.setStatus("current")


class _HmDVMRPRouteMetric_Type(Integer32):
    """Custom type hmDVMRPRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HmDVMRPRouteMetric_Type.__name__ = "Integer32"
_HmDVMRPRouteMetric_Object = MibTableColumn
hmDVMRPRouteMetric = _HmDVMRPRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 5),
    _HmDVMRPRouteMetric_Type()
)
hmDVMRPRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPRouteMetric.setStatus("current")
_HmDVMRPRouteExpiryTime_Type = TimeTicks
_HmDVMRPRouteExpiryTime_Object = MibTableColumn
hmDVMRPRouteExpiryTime = _HmDVMRPRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 6),
    _HmDVMRPRouteExpiryTime_Type()
)
hmDVMRPRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPRouteExpiryTime.setStatus("current")
_HmDVMRPRouteUpTime_Type = TimeTicks
_HmDVMRPRouteUpTime_Object = MibTableColumn
hmDVMRPRouteUpTime = _HmDVMRPRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 4, 1, 7),
    _HmDVMRPRouteUpTime_Type()
)
hmDVMRPRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPRouteUpTime.setStatus("current")
_HmDVMRPRouteNextHopTable_Object = MibTable
hmDVMRPRouteNextHopTable = _HmDVMRPRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hmDVMRPRouteNextHopTable.setStatus("current")
_HmDVMRPRouteNextHopEntry_Object = MibTableRow
hmDVMRPRouteNextHopEntry = _HmDVMRPRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1)
)
hmDVMRPRouteNextHopEntry.setIndexNames(
    (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteNextHopSource"),
    (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteNextHopSourceMask"),
    (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteNextHopIfIndex"),
)
if mibBuilder.loadTexts:
    hmDVMRPRouteNextHopEntry.setStatus("current")
_HmDVMRPRouteNextHopSource_Type = IpAddress
_HmDVMRPRouteNextHopSource_Object = MibTableColumn
hmDVMRPRouteNextHopSource = _HmDVMRPRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1, 1),
    _HmDVMRPRouteNextHopSource_Type()
)
hmDVMRPRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmDVMRPRouteNextHopSource.setStatus("current")
_HmDVMRPRouteNextHopSourceMask_Type = IpAddress
_HmDVMRPRouteNextHopSourceMask_Object = MibTableColumn
hmDVMRPRouteNextHopSourceMask = _HmDVMRPRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1, 2),
    _HmDVMRPRouteNextHopSourceMask_Type()
)
hmDVMRPRouteNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmDVMRPRouteNextHopSourceMask.setStatus("current")
_HmDVMRPRouteNextHopIfIndex_Type = InterfaceIndex
_HmDVMRPRouteNextHopIfIndex_Object = MibTableColumn
hmDVMRPRouteNextHopIfIndex = _HmDVMRPRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1, 3),
    _HmDVMRPRouteNextHopIfIndex_Type()
)
hmDVMRPRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmDVMRPRouteNextHopIfIndex.setStatus("current")


class _HmDVMRPRouteNextHopType_Type(Integer32):
    """Custom type hmDVMRPRouteNextHopType based on Integer32"""
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


_HmDVMRPRouteNextHopType_Type.__name__ = "Integer32"
_HmDVMRPRouteNextHopType_Object = MibTableColumn
hmDVMRPRouteNextHopType = _HmDVMRPRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 5, 1, 4),
    _HmDVMRPRouteNextHopType_Type()
)
hmDVMRPRouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPRouteNextHopType.setStatus("current")
_HmDVMRPPruneTable_Object = MibTable
hmDVMRPPruneTable = _HmDVMRPPruneTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hmDVMRPPruneTable.setStatus("current")
_HmDVMRPPruneEntry_Object = MibTableRow
hmDVMRPPruneEntry = _HmDVMRPPruneEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1)
)
hmDVMRPPruneEntry.setIndexNames(
    (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPPruneGroup"),
    (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPPruneSource"),
    (0, "HIRSCHMANN-DVMRP-MIB", "hmDVMRPPruneSourceMask"),
)
if mibBuilder.loadTexts:
    hmDVMRPPruneEntry.setStatus("current")
_HmDVMRPPruneGroup_Type = IpAddress
_HmDVMRPPruneGroup_Object = MibTableColumn
hmDVMRPPruneGroup = _HmDVMRPPruneGroup_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1, 1),
    _HmDVMRPPruneGroup_Type()
)
hmDVMRPPruneGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmDVMRPPruneGroup.setStatus("current")
_HmDVMRPPruneSource_Type = IpAddress
_HmDVMRPPruneSource_Object = MibTableColumn
hmDVMRPPruneSource = _HmDVMRPPruneSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1, 2),
    _HmDVMRPPruneSource_Type()
)
hmDVMRPPruneSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmDVMRPPruneSource.setStatus("current")
_HmDVMRPPruneSourceMask_Type = IpAddress
_HmDVMRPPruneSourceMask_Object = MibTableColumn
hmDVMRPPruneSourceMask = _HmDVMRPPruneSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1, 3),
    _HmDVMRPPruneSourceMask_Type()
)
hmDVMRPPruneSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmDVMRPPruneSourceMask.setStatus("current")
_HmDVMRPPruneExpiryTime_Type = TimeTicks
_HmDVMRPPruneExpiryTime_Object = MibTableColumn
hmDVMRPPruneExpiryTime = _HmDVMRPPruneExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 6, 1, 4),
    _HmDVMRPPruneExpiryTime_Type()
)
hmDVMRPPruneExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDVMRPPruneExpiryTime.setStatus("current")
_HmDVMRPTraps_ObjectIdentity = ObjectIdentity
hmDVMRPTraps = _HmDVMRPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 7)
)
_HmDVMRPMIBConformance_ObjectIdentity = ObjectIdentity
hmDVMRPMIBConformance = _HmDVMRPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2)
)
_HmDVMRPMIBCompliances_ObjectIdentity = ObjectIdentity
hmDVMRPMIBCompliances = _HmDVMRPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 1)
)
_HmDVMRPMIBGroups_ObjectIdentity = ObjectIdentity
hmDVMRPMIBGroups = _HmDVMRPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2)
)

# Managed Objects groups

hmDVMRPGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 2)
)
hmDVMRPGeneralGroup.setObjects(
      *(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPVersionString"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPGenerationId"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNumRoutes"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPReachableRoutes"))
)
if mibBuilder.loadTexts:
    hmDVMRPGeneralGroup.setStatus("current")

hmDVMRPInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 3)
)
hmDVMRPInterfaceGroup.setObjects(
      *(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceLocalAddress"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceMetric"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceStatus"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceRcvBadPkts"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceRcvBadRoutes"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceSentRoutes"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceGenerationId"))
)
if mibBuilder.loadTexts:
    hmDVMRPInterfaceGroup.setStatus("current")

hmDVMRPNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 4)
)
hmDVMRPNeighborGroup.setObjects(
      *(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborUpTime"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborExpiryTime"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborGenerationId"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborMajorVersion"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborMinorVersion"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborCapabilities"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborRcvRoutes"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborRcvBadPkts"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborRcvBadRoutes"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborState"))
)
if mibBuilder.loadTexts:
    hmDVMRPNeighborGroup.setStatus("current")

hmDVMRPRoutingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 5)
)
hmDVMRPRoutingGroup.setObjects(
      *(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteUpstreamNeighbor"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteIfIndex"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteMetric"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteExpiryTime"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteUpTime"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPRouteNextHopType"))
)
if mibBuilder.loadTexts:
    hmDVMRPRoutingGroup.setStatus("current")

hmDVMRPSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 6)
)
hmDVMRPSecurityGroup.setObjects(
      *(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceInterfaceKey"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceInterfaceKeyVersion"))
)
if mibBuilder.loadTexts:
    hmDVMRPSecurityGroup.setStatus("current")

hmDVMRPTreeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 7)
)
hmDVMRPTreeGroup.setObjects(
    ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPPruneExpiryTime")
)
if mibBuilder.loadTexts:
    hmDVMRPTreeGroup.setStatus("current")


# Notification objects

hmDVMRPNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 7, 1)
)
hmDVMRPNeighborLoss.setObjects(
      *(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceLocalAddress"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborState"))
)
if mibBuilder.loadTexts:
    hmDVMRPNeighborLoss.setStatus(
        "current"
    )

hmDVMRPNeighborNotPruning = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 1, 1, 7, 2)
)
hmDVMRPNeighborNotPruning.setObjects(
      *(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPInterfaceLocalAddress"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborCapabilities"))
)
if mibBuilder.loadTexts:
    hmDVMRPNeighborNotPruning.setStatus(
        "current"
    )


# Notifications groups

hmDVMRPNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 2, 8)
)
hmDVMRPNotificationGroup.setObjects(
      *(("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborLoss"),
        ("HIRSCHMANN-DVMRP-MIB", "hmDVMRPNeighborNotPruning"))
)
if mibBuilder.loadTexts:
    hmDVMRPNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hmDVMRPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 100, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hmDVMRPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-DVMRP-MIB",
    **{"hmDVMRPMIB": hmDVMRPMIB,
       "hmDVMRPMIBObjects": hmDVMRPMIBObjects,
       "hmDVMRP": hmDVMRP,
       "hmDVMRPScalar": hmDVMRPScalar,
       "hmDVMRPVersionString": hmDVMRPVersionString,
       "hmDVMRPGenerationId": hmDVMRPGenerationId,
       "hmDVMRPNumRoutes": hmDVMRPNumRoutes,
       "hmDVMRPReachableRoutes": hmDVMRPReachableRoutes,
       "hmDVMRPUpdateInterval": hmDVMRPUpdateInterval,
       "hmDVMRPPruneLifetime": hmDVMRPPruneLifetime,
       "hmDVMRPInterfaceTable": hmDVMRPInterfaceTable,
       "hmDVMRPInterfaceEntry": hmDVMRPInterfaceEntry,
       "hmDVMRPInterfaceIfIndex": hmDVMRPInterfaceIfIndex,
       "hmDVMRPInterfaceLocalAddress": hmDVMRPInterfaceLocalAddress,
       "hmDVMRPInterfaceMetric": hmDVMRPInterfaceMetric,
       "hmDVMRPInterfaceStatus": hmDVMRPInterfaceStatus,
       "hmDVMRPInterfaceRcvBadPkts": hmDVMRPInterfaceRcvBadPkts,
       "hmDVMRPInterfaceRcvBadRoutes": hmDVMRPInterfaceRcvBadRoutes,
       "hmDVMRPInterfaceSentRoutes": hmDVMRPInterfaceSentRoutes,
       "hmDVMRPInterfaceInterfaceKey": hmDVMRPInterfaceInterfaceKey,
       "hmDVMRPInterfaceInterfaceKeyVersion": hmDVMRPInterfaceInterfaceKeyVersion,
       "hmDVMRPInterfaceGenerationId": hmDVMRPInterfaceGenerationId,
       "hmDVMRPNeighborTable": hmDVMRPNeighborTable,
       "hmDVMRPNeighborEntry": hmDVMRPNeighborEntry,
       "hmDVMRPNeighborIfIndex": hmDVMRPNeighborIfIndex,
       "hmDVMRPNeighborAddress": hmDVMRPNeighborAddress,
       "hmDVMRPNeighborUpTime": hmDVMRPNeighborUpTime,
       "hmDVMRPNeighborExpiryTime": hmDVMRPNeighborExpiryTime,
       "hmDVMRPNeighborGenerationId": hmDVMRPNeighborGenerationId,
       "hmDVMRPNeighborMajorVersion": hmDVMRPNeighborMajorVersion,
       "hmDVMRPNeighborMinorVersion": hmDVMRPNeighborMinorVersion,
       "hmDVMRPNeighborCapabilities": hmDVMRPNeighborCapabilities,
       "hmDVMRPNeighborRcvRoutes": hmDVMRPNeighborRcvRoutes,
       "hmDVMRPNeighborRcvBadPkts": hmDVMRPNeighborRcvBadPkts,
       "hmDVMRPNeighborRcvBadRoutes": hmDVMRPNeighborRcvBadRoutes,
       "hmDVMRPNeighborState": hmDVMRPNeighborState,
       "hmDVMRPRouteTable": hmDVMRPRouteTable,
       "hmDVMRPRouteEntry": hmDVMRPRouteEntry,
       "hmDVMRPRouteSource": hmDVMRPRouteSource,
       "hmDVMRPRouteSourceMask": hmDVMRPRouteSourceMask,
       "hmDVMRPRouteUpstreamNeighbor": hmDVMRPRouteUpstreamNeighbor,
       "hmDVMRPRouteIfIndex": hmDVMRPRouteIfIndex,
       "hmDVMRPRouteMetric": hmDVMRPRouteMetric,
       "hmDVMRPRouteExpiryTime": hmDVMRPRouteExpiryTime,
       "hmDVMRPRouteUpTime": hmDVMRPRouteUpTime,
       "hmDVMRPRouteNextHopTable": hmDVMRPRouteNextHopTable,
       "hmDVMRPRouteNextHopEntry": hmDVMRPRouteNextHopEntry,
       "hmDVMRPRouteNextHopSource": hmDVMRPRouteNextHopSource,
       "hmDVMRPRouteNextHopSourceMask": hmDVMRPRouteNextHopSourceMask,
       "hmDVMRPRouteNextHopIfIndex": hmDVMRPRouteNextHopIfIndex,
       "hmDVMRPRouteNextHopType": hmDVMRPRouteNextHopType,
       "hmDVMRPPruneTable": hmDVMRPPruneTable,
       "hmDVMRPPruneEntry": hmDVMRPPruneEntry,
       "hmDVMRPPruneGroup": hmDVMRPPruneGroup,
       "hmDVMRPPruneSource": hmDVMRPPruneSource,
       "hmDVMRPPruneSourceMask": hmDVMRPPruneSourceMask,
       "hmDVMRPPruneExpiryTime": hmDVMRPPruneExpiryTime,
       "hmDVMRPTraps": hmDVMRPTraps,
       "hmDVMRPNeighborLoss": hmDVMRPNeighborLoss,
       "hmDVMRPNeighborNotPruning": hmDVMRPNeighborNotPruning,
       "hmDVMRPMIBConformance": hmDVMRPMIBConformance,
       "hmDVMRPMIBCompliances": hmDVMRPMIBCompliances,
       "hmDVMRPMIBCompliance": hmDVMRPMIBCompliance,
       "hmDVMRPMIBGroups": hmDVMRPMIBGroups,
       "hmDVMRPGeneralGroup": hmDVMRPGeneralGroup,
       "hmDVMRPInterfaceGroup": hmDVMRPInterfaceGroup,
       "hmDVMRPNeighborGroup": hmDVMRPNeighborGroup,
       "hmDVMRPRoutingGroup": hmDVMRPRoutingGroup,
       "hmDVMRPSecurityGroup": hmDVMRPSecurityGroup,
       "hmDVMRPTreeGroup": hmDVMRPTreeGroup,
       "hmDVMRPNotificationGroup": hmDVMRPNotificationGroup}
)
