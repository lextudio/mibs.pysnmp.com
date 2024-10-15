# SNMP MIB module (HM2-PLATFORM-DVMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-DVMRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:12 2024
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

(hm2PlatformMulticast,) = mibBuilder.importSymbols(
    "HM2-PLATFORM-MULTICAST-MIB",
    "hm2PlatformMulticast")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

hm2AgentDvmrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249)
)
hm2AgentDvmrp.setRevisions(
        ("2013-07-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2AgentDvmrpMIBNotifications_ObjectIdentity = ObjectIdentity
hm2AgentDvmrpMIBNotifications = _Hm2AgentDvmrpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 0)
)
_Hm2AgentDvmrpMIBObjects_ObjectIdentity = ObjectIdentity
hm2AgentDvmrpMIBObjects = _Hm2AgentDvmrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1)
)
_Hm2AgentDvmrpGroup_ObjectIdentity = ObjectIdentity
hm2AgentDvmrpGroup = _Hm2AgentDvmrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1)
)
_Hm2AgentDvmrpScalar_ObjectIdentity = ObjectIdentity
hm2AgentDvmrpScalar = _Hm2AgentDvmrpScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 1)
)
_Hm2AgentDvmrpVersionString_Type = DisplayString
_Hm2AgentDvmrpVersionString_Object = MibScalar
hm2AgentDvmrpVersionString = _Hm2AgentDvmrpVersionString_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 1, 1),
    _Hm2AgentDvmrpVersionString_Type()
)
hm2AgentDvmrpVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpVersionString.setStatus("current")
_Hm2AgentDvmrpGenerationId_Type = Integer32
_Hm2AgentDvmrpGenerationId_Object = MibScalar
hm2AgentDvmrpGenerationId = _Hm2AgentDvmrpGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 1, 2),
    _Hm2AgentDvmrpGenerationId_Type()
)
hm2AgentDvmrpGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpGenerationId.setStatus("current")
_Hm2AgentDvmrpNumRoutes_Type = Gauge32
_Hm2AgentDvmrpNumRoutes_Object = MibScalar
hm2AgentDvmrpNumRoutes = _Hm2AgentDvmrpNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 1, 3),
    _Hm2AgentDvmrpNumRoutes_Type()
)
hm2AgentDvmrpNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNumRoutes.setStatus("current")
_Hm2AgentDvmrpReachableRoutes_Type = Gauge32
_Hm2AgentDvmrpReachableRoutes_Object = MibScalar
hm2AgentDvmrpReachableRoutes = _Hm2AgentDvmrpReachableRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 1, 4),
    _Hm2AgentDvmrpReachableRoutes_Type()
)
hm2AgentDvmrpReachableRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpReachableRoutes.setStatus("current")
_Hm2AgentDvmrpInterfaceTable_Object = MibTable
hm2AgentDvmrpInterfaceTable = _Hm2AgentDvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hm2AgentDvmrpInterfaceTable.setStatus("current")
_Hm2AgentDvmrpInterfaceEntry_Object = MibTableRow
hm2AgentDvmrpInterfaceEntry = _Hm2AgentDvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1)
)
hm2AgentDvmrpInterfaceEntry.setIndexNames(
    (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDvmrpInterfaceEntry.setStatus("current")
_Hm2AgentDvmrpInterfaceIfIndex_Type = InterfaceIndex
_Hm2AgentDvmrpInterfaceIfIndex_Object = MibTableColumn
hm2AgentDvmrpInterfaceIfIndex = _Hm2AgentDvmrpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 1),
    _Hm2AgentDvmrpInterfaceIfIndex_Type()
)
hm2AgentDvmrpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDvmrpInterfaceIfIndex.setStatus("current")
_Hm2AgentDvmrpInterfaceLocalAddress_Type = IpAddress
_Hm2AgentDvmrpInterfaceLocalAddress_Object = MibTableColumn
hm2AgentDvmrpInterfaceLocalAddress = _Hm2AgentDvmrpInterfaceLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 2),
    _Hm2AgentDvmrpInterfaceLocalAddress_Type()
)
hm2AgentDvmrpInterfaceLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpInterfaceLocalAddress.setStatus("current")


class _Hm2AgentDvmrpInterfaceMetric_Type(Integer32):
    """Custom type hm2AgentDvmrpInterfaceMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Hm2AgentDvmrpInterfaceMetric_Type.__name__ = "Integer32"
_Hm2AgentDvmrpInterfaceMetric_Object = MibTableColumn
hm2AgentDvmrpInterfaceMetric = _Hm2AgentDvmrpInterfaceMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 3),
    _Hm2AgentDvmrpInterfaceMetric_Type()
)
hm2AgentDvmrpInterfaceMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDvmrpInterfaceMetric.setStatus("current")
_Hm2AgentDvmrpInterfaceStatus_Type = RowStatus
_Hm2AgentDvmrpInterfaceStatus_Object = MibTableColumn
hm2AgentDvmrpInterfaceStatus = _Hm2AgentDvmrpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 4),
    _Hm2AgentDvmrpInterfaceStatus_Type()
)
hm2AgentDvmrpInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDvmrpInterfaceStatus.setStatus("current")
_Hm2AgentDvmrpInterfaceRcvBadPkts_Type = Counter32
_Hm2AgentDvmrpInterfaceRcvBadPkts_Object = MibTableColumn
hm2AgentDvmrpInterfaceRcvBadPkts = _Hm2AgentDvmrpInterfaceRcvBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 5),
    _Hm2AgentDvmrpInterfaceRcvBadPkts_Type()
)
hm2AgentDvmrpInterfaceRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpInterfaceRcvBadPkts.setStatus("current")
_Hm2AgentDvmrpInterfaceRcvBadRoutes_Type = Counter32
_Hm2AgentDvmrpInterfaceRcvBadRoutes_Object = MibTableColumn
hm2AgentDvmrpInterfaceRcvBadRoutes = _Hm2AgentDvmrpInterfaceRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 6),
    _Hm2AgentDvmrpInterfaceRcvBadRoutes_Type()
)
hm2AgentDvmrpInterfaceRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpInterfaceRcvBadRoutes.setStatus("current")
_Hm2AgentDvmrpInterfaceSentRoutes_Type = Counter32
_Hm2AgentDvmrpInterfaceSentRoutes_Object = MibTableColumn
hm2AgentDvmrpInterfaceSentRoutes = _Hm2AgentDvmrpInterfaceSentRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 7),
    _Hm2AgentDvmrpInterfaceSentRoutes_Type()
)
hm2AgentDvmrpInterfaceSentRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpInterfaceSentRoutes.setStatus("current")
_Hm2AgentDvmrpInterfaceInterfaceKey_Type = SnmpAdminString
_Hm2AgentDvmrpInterfaceInterfaceKey_Object = MibTableColumn
hm2AgentDvmrpInterfaceInterfaceKey = _Hm2AgentDvmrpInterfaceInterfaceKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 8),
    _Hm2AgentDvmrpInterfaceInterfaceKey_Type()
)
hm2AgentDvmrpInterfaceInterfaceKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDvmrpInterfaceInterfaceKey.setStatus("current")
_Hm2AgentDvmrpInterfaceInterfaceKeyVersion_Type = Integer32
_Hm2AgentDvmrpInterfaceInterfaceKeyVersion_Object = MibTableColumn
hm2AgentDvmrpInterfaceInterfaceKeyVersion = _Hm2AgentDvmrpInterfaceInterfaceKeyVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 9),
    _Hm2AgentDvmrpInterfaceInterfaceKeyVersion_Type()
)
hm2AgentDvmrpInterfaceInterfaceKeyVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDvmrpInterfaceInterfaceKeyVersion.setStatus("current")
_Hm2AgentDvmrpInterfaceGenerationId_Type = Integer32
_Hm2AgentDvmrpInterfaceGenerationId_Object = MibTableColumn
hm2AgentDvmrpInterfaceGenerationId = _Hm2AgentDvmrpInterfaceGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 248),
    _Hm2AgentDvmrpInterfaceGenerationId_Type()
)
hm2AgentDvmrpInterfaceGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpInterfaceGenerationId.setStatus("current")
_Hm2AgentDvmrpNeighborTable_Object = MibTable
hm2AgentDvmrpNeighborTable = _Hm2AgentDvmrpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborTable.setStatus("current")
_Hm2AgentDvmrpNeighborEntry_Object = MibTableRow
hm2AgentDvmrpNeighborEntry = _Hm2AgentDvmrpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1)
)
hm2AgentDvmrpNeighborEntry.setIndexNames(
    (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpNeighborIfIndex"),
    (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpNeighborAddress"),
)
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborEntry.setStatus("current")
_Hm2AgentDvmrpNeighborIfIndex_Type = InterfaceIndex
_Hm2AgentDvmrpNeighborIfIndex_Object = MibTableColumn
hm2AgentDvmrpNeighborIfIndex = _Hm2AgentDvmrpNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 1),
    _Hm2AgentDvmrpNeighborIfIndex_Type()
)
hm2AgentDvmrpNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborIfIndex.setStatus("current")
_Hm2AgentDvmrpNeighborAddress_Type = IpAddress
_Hm2AgentDvmrpNeighborAddress_Object = MibTableColumn
hm2AgentDvmrpNeighborAddress = _Hm2AgentDvmrpNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 2),
    _Hm2AgentDvmrpNeighborAddress_Type()
)
hm2AgentDvmrpNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborAddress.setStatus("current")
_Hm2AgentDvmrpNeighborUpTime_Type = TimeTicks
_Hm2AgentDvmrpNeighborUpTime_Object = MibTableColumn
hm2AgentDvmrpNeighborUpTime = _Hm2AgentDvmrpNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 3),
    _Hm2AgentDvmrpNeighborUpTime_Type()
)
hm2AgentDvmrpNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborUpTime.setStatus("current")
_Hm2AgentDvmrpNeighborExpiryTime_Type = TimeTicks
_Hm2AgentDvmrpNeighborExpiryTime_Object = MibTableColumn
hm2AgentDvmrpNeighborExpiryTime = _Hm2AgentDvmrpNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 4),
    _Hm2AgentDvmrpNeighborExpiryTime_Type()
)
hm2AgentDvmrpNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborExpiryTime.setStatus("current")
_Hm2AgentDvmrpNeighborGenerationId_Type = Integer32
_Hm2AgentDvmrpNeighborGenerationId_Object = MibTableColumn
hm2AgentDvmrpNeighborGenerationId = _Hm2AgentDvmrpNeighborGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 5),
    _Hm2AgentDvmrpNeighborGenerationId_Type()
)
hm2AgentDvmrpNeighborGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborGenerationId.setStatus("current")


class _Hm2AgentDvmrpNeighborMajorVersion_Type(Integer32):
    """Custom type hm2AgentDvmrpNeighborMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hm2AgentDvmrpNeighborMajorVersion_Type.__name__ = "Integer32"
_Hm2AgentDvmrpNeighborMajorVersion_Object = MibTableColumn
hm2AgentDvmrpNeighborMajorVersion = _Hm2AgentDvmrpNeighborMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 6),
    _Hm2AgentDvmrpNeighborMajorVersion_Type()
)
hm2AgentDvmrpNeighborMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborMajorVersion.setStatus("current")


class _Hm2AgentDvmrpNeighborMinorVersion_Type(Integer32):
    """Custom type hm2AgentDvmrpNeighborMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hm2AgentDvmrpNeighborMinorVersion_Type.__name__ = "Integer32"
_Hm2AgentDvmrpNeighborMinorVersion_Object = MibTableColumn
hm2AgentDvmrpNeighborMinorVersion = _Hm2AgentDvmrpNeighborMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 7),
    _Hm2AgentDvmrpNeighborMinorVersion_Type()
)
hm2AgentDvmrpNeighborMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborMinorVersion.setStatus("current")


class _Hm2AgentDvmrpNeighborCapabilities_Type(Bits):
    """Custom type hm2AgentDvmrpNeighborCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("generationID", 2),
          ("leaf", 0),
          ("mtrace", 3),
          ("prune", 1))
    )

_Hm2AgentDvmrpNeighborCapabilities_Type.__name__ = "Bits"
_Hm2AgentDvmrpNeighborCapabilities_Object = MibTableColumn
hm2AgentDvmrpNeighborCapabilities = _Hm2AgentDvmrpNeighborCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 8),
    _Hm2AgentDvmrpNeighborCapabilities_Type()
)
hm2AgentDvmrpNeighborCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborCapabilities.setStatus("current")
_Hm2AgentDvmrpNeighborRcvRoutes_Type = Counter32
_Hm2AgentDvmrpNeighborRcvRoutes_Object = MibTableColumn
hm2AgentDvmrpNeighborRcvRoutes = _Hm2AgentDvmrpNeighborRcvRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 9),
    _Hm2AgentDvmrpNeighborRcvRoutes_Type()
)
hm2AgentDvmrpNeighborRcvRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborRcvRoutes.setStatus("current")
_Hm2AgentDvmrpNeighborRcvBadPkts_Type = Counter32
_Hm2AgentDvmrpNeighborRcvBadPkts_Object = MibTableColumn
hm2AgentDvmrpNeighborRcvBadPkts = _Hm2AgentDvmrpNeighborRcvBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 10),
    _Hm2AgentDvmrpNeighborRcvBadPkts_Type()
)
hm2AgentDvmrpNeighborRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborRcvBadPkts.setStatus("current")
_Hm2AgentDvmrpNeighborRcvBadRoutes_Type = Counter32
_Hm2AgentDvmrpNeighborRcvBadRoutes_Object = MibTableColumn
hm2AgentDvmrpNeighborRcvBadRoutes = _Hm2AgentDvmrpNeighborRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 11),
    _Hm2AgentDvmrpNeighborRcvBadRoutes_Type()
)
hm2AgentDvmrpNeighborRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborRcvBadRoutes.setStatus("current")


class _Hm2AgentDvmrpNeighborState_Type(Integer32):
    """Custom type hm2AgentDvmrpNeighborState based on Integer32"""
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


_Hm2AgentDvmrpNeighborState_Type.__name__ = "Integer32"
_Hm2AgentDvmrpNeighborState_Object = MibTableColumn
hm2AgentDvmrpNeighborState = _Hm2AgentDvmrpNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 12),
    _Hm2AgentDvmrpNeighborState_Type()
)
hm2AgentDvmrpNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborState.setStatus("current")
_Hm2AgentDvmrpRouteTable_Object = MibTable
hm2AgentDvmrpRouteTable = _Hm2AgentDvmrpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteTable.setStatus("current")
_Hm2AgentDvmrpRouteEntry_Object = MibTableRow
hm2AgentDvmrpRouteEntry = _Hm2AgentDvmrpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1)
)
hm2AgentDvmrpRouteEntry.setIndexNames(
    (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpRouteSource"),
    (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpRouteSourceMask"),
)
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteEntry.setStatus("current")
_Hm2AgentDvmrpRouteSource_Type = IpAddress
_Hm2AgentDvmrpRouteSource_Object = MibTableColumn
hm2AgentDvmrpRouteSource = _Hm2AgentDvmrpRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 1),
    _Hm2AgentDvmrpRouteSource_Type()
)
hm2AgentDvmrpRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteSource.setStatus("current")
_Hm2AgentDvmrpRouteSourceMask_Type = IpAddress
_Hm2AgentDvmrpRouteSourceMask_Object = MibTableColumn
hm2AgentDvmrpRouteSourceMask = _Hm2AgentDvmrpRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 2),
    _Hm2AgentDvmrpRouteSourceMask_Type()
)
hm2AgentDvmrpRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteSourceMask.setStatus("current")
_Hm2AgentDvmrpRouteUpstreamNeighbor_Type = IpAddress
_Hm2AgentDvmrpRouteUpstreamNeighbor_Object = MibTableColumn
hm2AgentDvmrpRouteUpstreamNeighbor = _Hm2AgentDvmrpRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 3),
    _Hm2AgentDvmrpRouteUpstreamNeighbor_Type()
)
hm2AgentDvmrpRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteUpstreamNeighbor.setStatus("current")
_Hm2AgentDvmrpRouteIfIndex_Type = InterfaceIndexOrZero
_Hm2AgentDvmrpRouteIfIndex_Object = MibTableColumn
hm2AgentDvmrpRouteIfIndex = _Hm2AgentDvmrpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 4),
    _Hm2AgentDvmrpRouteIfIndex_Type()
)
hm2AgentDvmrpRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteIfIndex.setStatus("current")


class _Hm2AgentDvmrpRouteMetric_Type(Integer32):
    """Custom type hm2AgentDvmrpRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Hm2AgentDvmrpRouteMetric_Type.__name__ = "Integer32"
_Hm2AgentDvmrpRouteMetric_Object = MibTableColumn
hm2AgentDvmrpRouteMetric = _Hm2AgentDvmrpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 5),
    _Hm2AgentDvmrpRouteMetric_Type()
)
hm2AgentDvmrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteMetric.setStatus("current")
_Hm2AgentDvmrpRouteExpiryTime_Type = TimeTicks
_Hm2AgentDvmrpRouteExpiryTime_Object = MibTableColumn
hm2AgentDvmrpRouteExpiryTime = _Hm2AgentDvmrpRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 6),
    _Hm2AgentDvmrpRouteExpiryTime_Type()
)
hm2AgentDvmrpRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteExpiryTime.setStatus("current")
_Hm2AgentDvmrpRouteUpTime_Type = TimeTicks
_Hm2AgentDvmrpRouteUpTime_Object = MibTableColumn
hm2AgentDvmrpRouteUpTime = _Hm2AgentDvmrpRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 7),
    _Hm2AgentDvmrpRouteUpTime_Type()
)
hm2AgentDvmrpRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteUpTime.setStatus("current")
_Hm2AgentDvmrpRouteNextHopTable_Object = MibTable
hm2AgentDvmrpRouteNextHopTable = _Hm2AgentDvmrpRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteNextHopTable.setStatus("current")
_Hm2AgentDvmrpRouteNextHopEntry_Object = MibTableRow
hm2AgentDvmrpRouteNextHopEntry = _Hm2AgentDvmrpRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 5, 1)
)
hm2AgentDvmrpRouteNextHopEntry.setIndexNames(
    (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpRouteNextHopSource"),
    (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpRouteNextHopSourceMask"),
    (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpRouteNextHopIfIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteNextHopEntry.setStatus("current")
_Hm2AgentDvmrpRouteNextHopSource_Type = IpAddress
_Hm2AgentDvmrpRouteNextHopSource_Object = MibTableColumn
hm2AgentDvmrpRouteNextHopSource = _Hm2AgentDvmrpRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 5, 1, 1),
    _Hm2AgentDvmrpRouteNextHopSource_Type()
)
hm2AgentDvmrpRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteNextHopSource.setStatus("current")
_Hm2AgentDvmrpRouteNextHopSourceMask_Type = IpAddress
_Hm2AgentDvmrpRouteNextHopSourceMask_Object = MibTableColumn
hm2AgentDvmrpRouteNextHopSourceMask = _Hm2AgentDvmrpRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 5, 1, 2),
    _Hm2AgentDvmrpRouteNextHopSourceMask_Type()
)
hm2AgentDvmrpRouteNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteNextHopSourceMask.setStatus("current")
_Hm2AgentDvmrpRouteNextHopIfIndex_Type = InterfaceIndex
_Hm2AgentDvmrpRouteNextHopIfIndex_Object = MibTableColumn
hm2AgentDvmrpRouteNextHopIfIndex = _Hm2AgentDvmrpRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 5, 1, 3),
    _Hm2AgentDvmrpRouteNextHopIfIndex_Type()
)
hm2AgentDvmrpRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteNextHopIfIndex.setStatus("current")


class _Hm2AgentDvmrpRouteNextHopType_Type(Integer32):
    """Custom type hm2AgentDvmrpRouteNextHopType based on Integer32"""
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


_Hm2AgentDvmrpRouteNextHopType_Type.__name__ = "Integer32"
_Hm2AgentDvmrpRouteNextHopType_Object = MibTableColumn
hm2AgentDvmrpRouteNextHopType = _Hm2AgentDvmrpRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 5, 1, 4),
    _Hm2AgentDvmrpRouteNextHopType_Type()
)
hm2AgentDvmrpRouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpRouteNextHopType.setStatus("current")
_Hm2AgentDvmrpPruneTable_Object = MibTable
hm2AgentDvmrpPruneTable = _Hm2AgentDvmrpPruneTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hm2AgentDvmrpPruneTable.setStatus("current")
_Hm2AgentDvmrpPruneEntry_Object = MibTableRow
hm2AgentDvmrpPruneEntry = _Hm2AgentDvmrpPruneEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 6, 1)
)
hm2AgentDvmrpPruneEntry.setIndexNames(
    (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpPruneGroup"),
    (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpPruneSource"),
    (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpPruneSourceMask"),
)
if mibBuilder.loadTexts:
    hm2AgentDvmrpPruneEntry.setStatus("current")
_Hm2AgentDvmrpPruneGroup_Type = IpAddress
_Hm2AgentDvmrpPruneGroup_Object = MibTableColumn
hm2AgentDvmrpPruneGroup = _Hm2AgentDvmrpPruneGroup_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 6, 1, 1),
    _Hm2AgentDvmrpPruneGroup_Type()
)
hm2AgentDvmrpPruneGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDvmrpPruneGroup.setStatus("current")
_Hm2AgentDvmrpPruneSource_Type = IpAddress
_Hm2AgentDvmrpPruneSource_Object = MibTableColumn
hm2AgentDvmrpPruneSource = _Hm2AgentDvmrpPruneSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 6, 1, 2),
    _Hm2AgentDvmrpPruneSource_Type()
)
hm2AgentDvmrpPruneSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDvmrpPruneSource.setStatus("current")
_Hm2AgentDvmrpPruneSourceMask_Type = IpAddress
_Hm2AgentDvmrpPruneSourceMask_Object = MibTableColumn
hm2AgentDvmrpPruneSourceMask = _Hm2AgentDvmrpPruneSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 6, 1, 3),
    _Hm2AgentDvmrpPruneSourceMask_Type()
)
hm2AgentDvmrpPruneSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDvmrpPruneSourceMask.setStatus("current")
_Hm2AgentDvmrpPruneExpiryTime_Type = TimeTicks
_Hm2AgentDvmrpPruneExpiryTime_Object = MibTableColumn
hm2AgentDvmrpPruneExpiryTime = _Hm2AgentDvmrpPruneExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 6, 1, 4),
    _Hm2AgentDvmrpPruneExpiryTime_Type()
)
hm2AgentDvmrpPruneExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDvmrpPruneExpiryTime.setStatus("current")

# Managed Objects groups


# Notification objects

hm2AgentDvmrpNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 0, 1)
)
hm2AgentDvmrpNeighborLoss.setObjects(
      *(("HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpInterfaceLocalAddress"),
        ("HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpNeighborState"))
)
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborLoss.setStatus(
        "current"
    )

hm2AgentDvmrpNeighborNotPruning = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 0, 2)
)
hm2AgentDvmrpNeighborNotPruning.setObjects(
      *(("HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpInterfaceLocalAddress"),
        ("HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpNeighborCapabilities"))
)
if mibBuilder.loadTexts:
    hm2AgentDvmrpNeighborNotPruning.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-DVMRP-MIB",
    **{"hm2AgentDvmrp": hm2AgentDvmrp,
       "hm2AgentDvmrpMIBNotifications": hm2AgentDvmrpMIBNotifications,
       "hm2AgentDvmrpNeighborLoss": hm2AgentDvmrpNeighborLoss,
       "hm2AgentDvmrpNeighborNotPruning": hm2AgentDvmrpNeighborNotPruning,
       "hm2AgentDvmrpMIBObjects": hm2AgentDvmrpMIBObjects,
       "hm2AgentDvmrpGroup": hm2AgentDvmrpGroup,
       "hm2AgentDvmrpScalar": hm2AgentDvmrpScalar,
       "hm2AgentDvmrpVersionString": hm2AgentDvmrpVersionString,
       "hm2AgentDvmrpGenerationId": hm2AgentDvmrpGenerationId,
       "hm2AgentDvmrpNumRoutes": hm2AgentDvmrpNumRoutes,
       "hm2AgentDvmrpReachableRoutes": hm2AgentDvmrpReachableRoutes,
       "hm2AgentDvmrpInterfaceTable": hm2AgentDvmrpInterfaceTable,
       "hm2AgentDvmrpInterfaceEntry": hm2AgentDvmrpInterfaceEntry,
       "hm2AgentDvmrpInterfaceIfIndex": hm2AgentDvmrpInterfaceIfIndex,
       "hm2AgentDvmrpInterfaceLocalAddress": hm2AgentDvmrpInterfaceLocalAddress,
       "hm2AgentDvmrpInterfaceMetric": hm2AgentDvmrpInterfaceMetric,
       "hm2AgentDvmrpInterfaceStatus": hm2AgentDvmrpInterfaceStatus,
       "hm2AgentDvmrpInterfaceRcvBadPkts": hm2AgentDvmrpInterfaceRcvBadPkts,
       "hm2AgentDvmrpInterfaceRcvBadRoutes": hm2AgentDvmrpInterfaceRcvBadRoutes,
       "hm2AgentDvmrpInterfaceSentRoutes": hm2AgentDvmrpInterfaceSentRoutes,
       "hm2AgentDvmrpInterfaceInterfaceKey": hm2AgentDvmrpInterfaceInterfaceKey,
       "hm2AgentDvmrpInterfaceInterfaceKeyVersion": hm2AgentDvmrpInterfaceInterfaceKeyVersion,
       "hm2AgentDvmrpInterfaceGenerationId": hm2AgentDvmrpInterfaceGenerationId,
       "hm2AgentDvmrpNeighborTable": hm2AgentDvmrpNeighborTable,
       "hm2AgentDvmrpNeighborEntry": hm2AgentDvmrpNeighborEntry,
       "hm2AgentDvmrpNeighborIfIndex": hm2AgentDvmrpNeighborIfIndex,
       "hm2AgentDvmrpNeighborAddress": hm2AgentDvmrpNeighborAddress,
       "hm2AgentDvmrpNeighborUpTime": hm2AgentDvmrpNeighborUpTime,
       "hm2AgentDvmrpNeighborExpiryTime": hm2AgentDvmrpNeighborExpiryTime,
       "hm2AgentDvmrpNeighborGenerationId": hm2AgentDvmrpNeighborGenerationId,
       "hm2AgentDvmrpNeighborMajorVersion": hm2AgentDvmrpNeighborMajorVersion,
       "hm2AgentDvmrpNeighborMinorVersion": hm2AgentDvmrpNeighborMinorVersion,
       "hm2AgentDvmrpNeighborCapabilities": hm2AgentDvmrpNeighborCapabilities,
       "hm2AgentDvmrpNeighborRcvRoutes": hm2AgentDvmrpNeighborRcvRoutes,
       "hm2AgentDvmrpNeighborRcvBadPkts": hm2AgentDvmrpNeighborRcvBadPkts,
       "hm2AgentDvmrpNeighborRcvBadRoutes": hm2AgentDvmrpNeighborRcvBadRoutes,
       "hm2AgentDvmrpNeighborState": hm2AgentDvmrpNeighborState,
       "hm2AgentDvmrpRouteTable": hm2AgentDvmrpRouteTable,
       "hm2AgentDvmrpRouteEntry": hm2AgentDvmrpRouteEntry,
       "hm2AgentDvmrpRouteSource": hm2AgentDvmrpRouteSource,
       "hm2AgentDvmrpRouteSourceMask": hm2AgentDvmrpRouteSourceMask,
       "hm2AgentDvmrpRouteUpstreamNeighbor": hm2AgentDvmrpRouteUpstreamNeighbor,
       "hm2AgentDvmrpRouteIfIndex": hm2AgentDvmrpRouteIfIndex,
       "hm2AgentDvmrpRouteMetric": hm2AgentDvmrpRouteMetric,
       "hm2AgentDvmrpRouteExpiryTime": hm2AgentDvmrpRouteExpiryTime,
       "hm2AgentDvmrpRouteUpTime": hm2AgentDvmrpRouteUpTime,
       "hm2AgentDvmrpRouteNextHopTable": hm2AgentDvmrpRouteNextHopTable,
       "hm2AgentDvmrpRouteNextHopEntry": hm2AgentDvmrpRouteNextHopEntry,
       "hm2AgentDvmrpRouteNextHopSource": hm2AgentDvmrpRouteNextHopSource,
       "hm2AgentDvmrpRouteNextHopSourceMask": hm2AgentDvmrpRouteNextHopSourceMask,
       "hm2AgentDvmrpRouteNextHopIfIndex": hm2AgentDvmrpRouteNextHopIfIndex,
       "hm2AgentDvmrpRouteNextHopType": hm2AgentDvmrpRouteNextHopType,
       "hm2AgentDvmrpPruneTable": hm2AgentDvmrpPruneTable,
       "hm2AgentDvmrpPruneEntry": hm2AgentDvmrpPruneEntry,
       "hm2AgentDvmrpPruneGroup": hm2AgentDvmrpPruneGroup,
       "hm2AgentDvmrpPruneSource": hm2AgentDvmrpPruneSource,
       "hm2AgentDvmrpPruneSourceMask": hm2AgentDvmrpPruneSourceMask,
       "hm2AgentDvmrpPruneExpiryTime": hm2AgentDvmrpPruneExpiryTime}
)
