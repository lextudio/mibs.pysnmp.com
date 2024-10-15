# SNMP MIB module (STN-VEI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-VEI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:19 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(stnNotification,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification")

(stnRouterVEI,) = mibBuilder.importSymbols(
    "STN-ROUTER-MIB",
    "stnRouterVEI")


# MODULE-IDENTITY

stnVei = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnVeiObjects_ObjectIdentity = ObjectIdentity
stnVeiObjects = _StnVeiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1)
)
_StnVeiL2Table_Object = MibTable
stnVeiL2Table = _StnVeiL2Table_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnVeiL2Table.setStatus("current")
_StnVeiL2Entry_Object = MibTableRow
stnVeiL2Entry = _StnVeiL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1)
)
stnVeiL2Entry.setIndexNames(
    (0, "STN-VEI-MIB", "stnVeiL2IfIndex"),
)
if mibBuilder.loadTexts:
    stnVeiL2Entry.setStatus("current")
_StnVeiL2IfIndex_Type = InterfaceIndex
_StnVeiL2IfIndex_Object = MibTableColumn
stnVeiL2IfIndex = _StnVeiL2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 1),
    _StnVeiL2IfIndex_Type()
)
stnVeiL2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2IfIndex.setStatus("current")
_StnVeiL2ViId_Type = Integer32
_StnVeiL2ViId_Object = MibTableColumn
stnVeiL2ViId = _StnVeiL2ViId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 2),
    _StnVeiL2ViId_Type()
)
stnVeiL2ViId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2ViId.setStatus("current")


class _StnVeiL2Name_Type(DisplayString):
    """Custom type stnVeiL2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StnVeiL2Name_Type.__name__ = "DisplayString"
_StnVeiL2Name_Object = MibTableColumn
stnVeiL2Name = _StnVeiL2Name_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 3),
    _StnVeiL2Name_Type()
)
stnVeiL2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2Name.setStatus("current")


class _StnVeiL2Type_Type(Integer32):
    """Custom type stnVeiL2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atmBridgeEnet8023", 2),
          ("atmBridgeEnetV2", 1))
    )


_StnVeiL2Type_Type.__name__ = "Integer32"
_StnVeiL2Type_Object = MibTableColumn
stnVeiL2Type = _StnVeiL2Type_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 4),
    _StnVeiL2Type_Type()
)
stnVeiL2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2Type.setStatus("current")
_StnVeiL2MacTtl_Type = Gauge32
_StnVeiL2MacTtl_Object = MibTableColumn
stnVeiL2MacTtl = _StnVeiL2MacTtl_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 5),
    _StnVeiL2MacTtl_Type()
)
stnVeiL2MacTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2MacTtl.setStatus("current")


class _StnVeiL2State_Type(Integer32):
    """Custom type stnVeiL2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_StnVeiL2State_Type.__name__ = "Integer32"
_StnVeiL2State_Object = MibTableColumn
stnVeiL2State = _StnVeiL2State_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 6),
    _StnVeiL2State_Type()
)
stnVeiL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2State.setStatus("current")
_StnVeiL2RegisteredLowerLinks_Type = Gauge32
_StnVeiL2RegisteredLowerLinks_Object = MibTableColumn
stnVeiL2RegisteredLowerLinks = _StnVeiL2RegisteredLowerLinks_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 7),
    _StnVeiL2RegisteredLowerLinks_Type()
)
stnVeiL2RegisteredLowerLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2RegisteredLowerLinks.setStatus("current")
_StnVeiL2ActiveLowerLinks_Type = Gauge32
_StnVeiL2ActiveLowerLinks_Object = MibTableColumn
stnVeiL2ActiveLowerLinks = _StnVeiL2ActiveLowerLinks_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 8),
    _StnVeiL2ActiveLowerLinks_Type()
)
stnVeiL2ActiveLowerLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2ActiveLowerLinks.setStatus("current")
_StnVeiL2NoFreeEndStations_Type = Counter32
_StnVeiL2NoFreeEndStations_Object = MibTableColumn
stnVeiL2NoFreeEndStations = _StnVeiL2NoFreeEndStations_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 9),
    _StnVeiL2NoFreeEndStations_Type()
)
stnVeiL2NoFreeEndStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2NoFreeEndStations.setStatus("current")
_StnVeiL2TxDestNotFound_Type = Counter32
_StnVeiL2TxDestNotFound_Object = MibTableColumn
stnVeiL2TxDestNotFound = _StnVeiL2TxDestNotFound_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 10),
    _StnVeiL2TxDestNotFound_Type()
)
stnVeiL2TxDestNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2TxDestNotFound.setStatus("current")
_StnVeiL2TxArpRspDropNoEndStation_Type = Counter32
_StnVeiL2TxArpRspDropNoEndStation_Object = MibTableColumn
stnVeiL2TxArpRspDropNoEndStation = _StnVeiL2TxArpRspDropNoEndStation_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 11),
    _StnVeiL2TxArpRspDropNoEndStation_Type()
)
stnVeiL2TxArpRspDropNoEndStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2TxArpRspDropNoEndStation.setStatus("current")
_StnVeiL2ActiveMultiCasts_Type = Counter32
_StnVeiL2ActiveMultiCasts_Object = MibTableColumn
stnVeiL2ActiveMultiCasts = _StnVeiL2ActiveMultiCasts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 12),
    _StnVeiL2ActiveMultiCasts_Type()
)
stnVeiL2ActiveMultiCasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2ActiveMultiCasts.setStatus("current")
_StnVeiL2MultiCastsDrop_Type = Counter32
_StnVeiL2MultiCastsDrop_Object = MibTableColumn
stnVeiL2MultiCastsDrop = _StnVeiL2MultiCastsDrop_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 1, 1, 13),
    _StnVeiL2MultiCastsDrop_Type()
)
stnVeiL2MultiCastsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiL2MultiCastsDrop.setStatus("current")
_StnVeiLinkTable_Object = MibTable
stnVeiLinkTable = _StnVeiLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    stnVeiLinkTable.setStatus("current")
_StnVeiLinkEntry_Object = MibTableRow
stnVeiLinkEntry = _StnVeiLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1)
)
stnVeiLinkEntry.setIndexNames(
    (0, "STN-VEI-MIB", "stnVeiLinkVeiIfIndex"),
    (0, "STN-VEI-MIB", "stnVeiLinkIfIndex"),
)
if mibBuilder.loadTexts:
    stnVeiLinkEntry.setStatus("current")
_StnVeiLinkVeiIfIndex_Type = InterfaceIndex
_StnVeiLinkVeiIfIndex_Object = MibTableColumn
stnVeiLinkVeiIfIndex = _StnVeiLinkVeiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1, 1),
    _StnVeiLinkVeiIfIndex_Type()
)
stnVeiLinkVeiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkVeiIfIndex.setStatus("current")
_StnVeiLinkIfIndex_Type = InterfaceIndex
_StnVeiLinkIfIndex_Object = MibTableColumn
stnVeiLinkIfIndex = _StnVeiLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1, 2),
    _StnVeiLinkIfIndex_Type()
)
stnVeiLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkIfIndex.setStatus("current")
_StnVeiLinkMaxEndStations_Type = Gauge32
_StnVeiLinkMaxEndStations_Object = MibTableColumn
stnVeiLinkMaxEndStations = _StnVeiLinkMaxEndStations_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1, 3),
    _StnVeiLinkMaxEndStations_Type()
)
stnVeiLinkMaxEndStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkMaxEndStations.setStatus("current")
_StnVeiLinkCurrentEndStations_Type = Gauge32
_StnVeiLinkCurrentEndStations_Object = MibTableColumn
stnVeiLinkCurrentEndStations = _StnVeiLinkCurrentEndStations_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1, 4),
    _StnVeiLinkCurrentEndStations_Type()
)
stnVeiLinkCurrentEndStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkCurrentEndStations.setStatus("current")
_StnVeiLinkLearnFailures_Type = Counter32
_StnVeiLinkLearnFailures_Object = MibTableColumn
stnVeiLinkLearnFailures = _StnVeiLinkLearnFailures_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1, 5),
    _StnVeiLinkLearnFailures_Type()
)
stnVeiLinkLearnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkLearnFailures.setStatus("current")
_StnVeiLinkMacRecycledLocal_Type = Counter32
_StnVeiLinkMacRecycledLocal_Object = MibTableColumn
stnVeiLinkMacRecycledLocal = _StnVeiLinkMacRecycledLocal_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1, 6),
    _StnVeiLinkMacRecycledLocal_Type()
)
stnVeiLinkMacRecycledLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkMacRecycledLocal.setStatus("current")
_StnVeiLinkMacRecycledGlobal_Type = Counter32
_StnVeiLinkMacRecycledGlobal_Object = MibTableColumn
stnVeiLinkMacRecycledGlobal = _StnVeiLinkMacRecycledGlobal_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1, 7),
    _StnVeiLinkMacRecycledGlobal_Type()
)
stnVeiLinkMacRecycledGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkMacRecycledGlobal.setStatus("current")
_StnVeiLinkArpRspDropSameIface_Type = Counter32
_StnVeiLinkArpRspDropSameIface_Object = MibTableColumn
stnVeiLinkArpRspDropSameIface = _StnVeiLinkArpRspDropSameIface_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1, 8),
    _StnVeiLinkArpRspDropSameIface_Type()
)
stnVeiLinkArpRspDropSameIface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkArpRspDropSameIface.setStatus("current")
_StnVeiLinkEndStationMoved_Type = Counter32
_StnVeiLinkEndStationMoved_Object = MibTableColumn
stnVeiLinkEndStationMoved = _StnVeiLinkEndStationMoved_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1, 9),
    _StnVeiLinkEndStationMoved_Type()
)
stnVeiLinkEndStationMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkEndStationMoved.setStatus("current")
_StnVeiLinkPhysIfIndex_Type = InterfaceIndex
_StnVeiLinkPhysIfIndex_Object = MibTableColumn
stnVeiLinkPhysIfIndex = _StnVeiLinkPhysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1, 10),
    _StnVeiLinkPhysIfIndex_Type()
)
stnVeiLinkPhysIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkPhysIfIndex.setStatus("current")
_StnVeiLinkVpi_Type = Integer32
_StnVeiLinkVpi_Object = MibTableColumn
stnVeiLinkVpi = _StnVeiLinkVpi_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1, 11),
    _StnVeiLinkVpi_Type()
)
stnVeiLinkVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkVpi.setStatus("current")
_StnVeiLinkVci_Type = Integer32
_StnVeiLinkVci_Object = MibTableColumn
stnVeiLinkVci = _StnVeiLinkVci_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 2, 1, 12),
    _StnVeiLinkVci_Type()
)
stnVeiLinkVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkVci.setStatus("current")
_StnVeiLinkMacTable_Object = MibTable
stnVeiLinkMacTable = _StnVeiLinkMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    stnVeiLinkMacTable.setStatus("current")
_StnVeiLinkMacEntry_Object = MibTableRow
stnVeiLinkMacEntry = _StnVeiLinkMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 3, 1)
)
stnVeiLinkMacEntry.setIndexNames(
    (0, "STN-VEI-MIB", "stnVeiLinkMacVeiIfIndex"),
    (0, "STN-VEI-MIB", "stnVeiLinkMacLinkIfIndex"),
    (0, "STN-VEI-MIB", "stnVeiLinkMacAddress"),
)
if mibBuilder.loadTexts:
    stnVeiLinkMacEntry.setStatus("current")
_StnVeiLinkMacVeiIfIndex_Type = InterfaceIndex
_StnVeiLinkMacVeiIfIndex_Object = MibTableColumn
stnVeiLinkMacVeiIfIndex = _StnVeiLinkMacVeiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 3, 1, 1),
    _StnVeiLinkMacVeiIfIndex_Type()
)
stnVeiLinkMacVeiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkMacVeiIfIndex.setStatus("current")
_StnVeiLinkMacLinkIfIndex_Type = InterfaceIndex
_StnVeiLinkMacLinkIfIndex_Object = MibTableColumn
stnVeiLinkMacLinkIfIndex = _StnVeiLinkMacLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 3, 1, 2),
    _StnVeiLinkMacLinkIfIndex_Type()
)
stnVeiLinkMacLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkMacLinkIfIndex.setStatus("current")
_StnVeiLinkMacAddress_Type = PhysAddress
_StnVeiLinkMacAddress_Object = MibTableColumn
stnVeiLinkMacAddress = _StnVeiLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 3, 1, 3),
    _StnVeiLinkMacAddress_Type()
)
stnVeiLinkMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkMacAddress.setStatus("current")
_StnVeiLinkMacAge_Type = Gauge32
_StnVeiLinkMacAge_Object = MibTableColumn
stnVeiLinkMacAge = _StnVeiLinkMacAge_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 3, 1, 4),
    _StnVeiLinkMacAge_Type()
)
stnVeiLinkMacAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkMacAge.setStatus("current")


class _StnVeiLinkMacType_Type(Integer32):
    """Custom type stnVeiLinkMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("veiLinkMacLearned", 1),
          ("veiLinkMacStatic", 2))
    )


_StnVeiLinkMacType_Type.__name__ = "Integer32"
_StnVeiLinkMacType_Object = MibTableColumn
stnVeiLinkMacType = _StnVeiLinkMacType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6, 1, 1, 3, 1, 5),
    _StnVeiLinkMacType_Type()
)
stnVeiLinkMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnVeiLinkMacType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-VEI-MIB",
    **{"stnVei": stnVei,
       "stnVeiObjects": stnVeiObjects,
       "stnVeiL2Table": stnVeiL2Table,
       "stnVeiL2Entry": stnVeiL2Entry,
       "stnVeiL2IfIndex": stnVeiL2IfIndex,
       "stnVeiL2ViId": stnVeiL2ViId,
       "stnVeiL2Name": stnVeiL2Name,
       "stnVeiL2Type": stnVeiL2Type,
       "stnVeiL2MacTtl": stnVeiL2MacTtl,
       "stnVeiL2State": stnVeiL2State,
       "stnVeiL2RegisteredLowerLinks": stnVeiL2RegisteredLowerLinks,
       "stnVeiL2ActiveLowerLinks": stnVeiL2ActiveLowerLinks,
       "stnVeiL2NoFreeEndStations": stnVeiL2NoFreeEndStations,
       "stnVeiL2TxDestNotFound": stnVeiL2TxDestNotFound,
       "stnVeiL2TxArpRspDropNoEndStation": stnVeiL2TxArpRspDropNoEndStation,
       "stnVeiL2ActiveMultiCasts": stnVeiL2ActiveMultiCasts,
       "stnVeiL2MultiCastsDrop": stnVeiL2MultiCastsDrop,
       "stnVeiLinkTable": stnVeiLinkTable,
       "stnVeiLinkEntry": stnVeiLinkEntry,
       "stnVeiLinkVeiIfIndex": stnVeiLinkVeiIfIndex,
       "stnVeiLinkIfIndex": stnVeiLinkIfIndex,
       "stnVeiLinkMaxEndStations": stnVeiLinkMaxEndStations,
       "stnVeiLinkCurrentEndStations": stnVeiLinkCurrentEndStations,
       "stnVeiLinkLearnFailures": stnVeiLinkLearnFailures,
       "stnVeiLinkMacRecycledLocal": stnVeiLinkMacRecycledLocal,
       "stnVeiLinkMacRecycledGlobal": stnVeiLinkMacRecycledGlobal,
       "stnVeiLinkArpRspDropSameIface": stnVeiLinkArpRspDropSameIface,
       "stnVeiLinkEndStationMoved": stnVeiLinkEndStationMoved,
       "stnVeiLinkPhysIfIndex": stnVeiLinkPhysIfIndex,
       "stnVeiLinkVpi": stnVeiLinkVpi,
       "stnVeiLinkVci": stnVeiLinkVci,
       "stnVeiLinkMacTable": stnVeiLinkMacTable,
       "stnVeiLinkMacEntry": stnVeiLinkMacEntry,
       "stnVeiLinkMacVeiIfIndex": stnVeiLinkMacVeiIfIndex,
       "stnVeiLinkMacLinkIfIndex": stnVeiLinkMacLinkIfIndex,
       "stnVeiLinkMacAddress": stnVeiLinkMacAddress,
       "stnVeiLinkMacAge": stnVeiLinkMacAge,
       "stnVeiLinkMacType": stnVeiLinkMacType}
)
