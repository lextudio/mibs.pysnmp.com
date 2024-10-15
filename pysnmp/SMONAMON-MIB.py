# SNMP MIB module (SMONAMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SMONAMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:38 2024
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

(smon,) = mibBuilder.importSymbols(
    "APPLIC-MIB",
    "smon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Smonamon_ObjectIdentity = ObjectIdentity
smonamon = _Smonamon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 5)
)
_AmonSlotStatistics_ObjectIdentity = ObjectIdentity
amonSlotStatistics = _AmonSlotStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1)
)
_AmonSlotStatsTable_Object = MibTable
amonSlotStatsTable = _AmonSlotStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1)
)
if mibBuilder.loadTexts:
    amonSlotStatsTable.setStatus("mandatory")
_AmonSlotStatsEntry_Object = MibTableRow
amonSlotStatsEntry = _AmonSlotStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1)
)
amonSlotStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    amonSlotStatsEntry.setStatus("mandatory")
_AmonSlotInCells_Type = Counter32
_AmonSlotInCells_Object = MibTableColumn
amonSlotInCells = _AmonSlotInCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 1),
    _AmonSlotInCells_Type()
)
amonSlotInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotInCells.setStatus("mandatory")
_AmonSlotBadHecCells_Type = Counter32
_AmonSlotBadHecCells_Object = MibTableColumn
amonSlotBadHecCells = _AmonSlotBadHecCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 2),
    _AmonSlotBadHecCells_Type()
)
amonSlotBadHecCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotBadHecCells.setStatus("mandatory")
_AmonSlotDroppedCells_Type = Counter32
_AmonSlotDroppedCells_Object = MibTableColumn
amonSlotDroppedCells = _AmonSlotDroppedCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 3),
    _AmonSlotDroppedCells_Type()
)
amonSlotDroppedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotDroppedCells.setStatus("mandatory")
_AmonSlotUbrCells_Type = Counter32
_AmonSlotUbrCells_Object = MibTableColumn
amonSlotUbrCells = _AmonSlotUbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 4),
    _AmonSlotUbrCells_Type()
)
amonSlotUbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotUbrCells.setStatus("mandatory")
_AmonSlotAbrCells_Type = Counter32
_AmonSlotAbrCells_Object = MibTableColumn
amonSlotAbrCells = _AmonSlotAbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 5),
    _AmonSlotAbrCells_Type()
)
amonSlotAbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotAbrCells.setStatus("mandatory")
_AmonSlotNrtVbrCells_Type = Counter32
_AmonSlotNrtVbrCells_Object = MibTableColumn
amonSlotNrtVbrCells = _AmonSlotNrtVbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 6),
    _AmonSlotNrtVbrCells_Type()
)
amonSlotNrtVbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotNrtVbrCells.setStatus("mandatory")
_AmonSlotRtVbrCells_Type = Counter32
_AmonSlotRtVbrCells_Object = MibTableColumn
amonSlotRtVbrCells = _AmonSlotRtVbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 7),
    _AmonSlotRtVbrCells_Type()
)
amonSlotRtVbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotRtVbrCells.setStatus("mandatory")
_AmonSlotCbrCells_Type = Counter32
_AmonSlotCbrCells_Object = MibTableColumn
amonSlotCbrCells = _AmonSlotCbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 8),
    _AmonSlotCbrCells_Type()
)
amonSlotCbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotCbrCells.setStatus("mandatory")
_AmonSlotPnniCells_Type = Counter32
_AmonSlotPnniCells_Object = MibTableColumn
amonSlotPnniCells = _AmonSlotPnniCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 9),
    _AmonSlotPnniCells_Type()
)
amonSlotPnniCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotPnniCells.setStatus("mandatory")
_AmonSlotSignalingCells_Type = Counter32
_AmonSlotSignalingCells_Object = MibTableColumn
amonSlotSignalingCells = _AmonSlotSignalingCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 10),
    _AmonSlotSignalingCells_Type()
)
amonSlotSignalingCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotSignalingCells.setStatus("mandatory")
_AmonSlotLaneCells_Type = Counter32
_AmonSlotLaneCells_Object = MibTableColumn
amonSlotLaneCells = _AmonSlotLaneCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 11),
    _AmonSlotLaneCells_Type()
)
amonSlotLaneCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotLaneCells.setStatus("mandatory")
_AmonSlotLaneDataDirectCells_Type = Counter32
_AmonSlotLaneDataDirectCells_Object = MibTableColumn
amonSlotLaneDataDirectCells = _AmonSlotLaneDataDirectCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 12),
    _AmonSlotLaneDataDirectCells_Type()
)
amonSlotLaneDataDirectCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotLaneDataDirectCells.setStatus("mandatory")
_AmonSlotLaneMulticastCells_Type = Counter32
_AmonSlotLaneMulticastCells_Object = MibTableColumn
amonSlotLaneMulticastCells = _AmonSlotLaneMulticastCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 13),
    _AmonSlotLaneMulticastCells_Type()
)
amonSlotLaneMulticastCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotLaneMulticastCells.setStatus("mandatory")
_AmonSlotLaneConfigControlCells_Type = Counter32
_AmonSlotLaneConfigControlCells_Object = MibTableColumn
amonSlotLaneConfigControlCells = _AmonSlotLaneConfigControlCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 14),
    _AmonSlotLaneConfigControlCells_Type()
)
amonSlotLaneConfigControlCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotLaneConfigControlCells.setStatus("mandatory")
_AmonSlotDefinityCells_Type = Counter32
_AmonSlotDefinityCells_Object = MibTableColumn
amonSlotDefinityCells = _AmonSlotDefinityCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 15),
    _AmonSlotDefinityCells_Type()
)
amonSlotDefinityCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotDefinityCells.setStatus("mandatory")
_AmonSlotTotalBwAllocated_Type = Counter32
_AmonSlotTotalBwAllocated_Object = MibTableColumn
amonSlotTotalBwAllocated = _AmonSlotTotalBwAllocated_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 16),
    _AmonSlotTotalBwAllocated_Type()
)
amonSlotTotalBwAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotTotalBwAllocated.setStatus("mandatory")
_AmonSlotAbrBwAllocated_Type = Counter32
_AmonSlotAbrBwAllocated_Object = MibTableColumn
amonSlotAbrBwAllocated = _AmonSlotAbrBwAllocated_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 17),
    _AmonSlotAbrBwAllocated_Type()
)
amonSlotAbrBwAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotAbrBwAllocated.setStatus("mandatory")
_AmonSlotNrtVbrBwAllocated_Type = Counter32
_AmonSlotNrtVbrBwAllocated_Object = MibTableColumn
amonSlotNrtVbrBwAllocated = _AmonSlotNrtVbrBwAllocated_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 18),
    _AmonSlotNrtVbrBwAllocated_Type()
)
amonSlotNrtVbrBwAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotNrtVbrBwAllocated.setStatus("mandatory")
_AmonSlotRtVbrBwAllocated_Type = Counter32
_AmonSlotRtVbrBwAllocated_Object = MibTableColumn
amonSlotRtVbrBwAllocated = _AmonSlotRtVbrBwAllocated_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 19),
    _AmonSlotRtVbrBwAllocated_Type()
)
amonSlotRtVbrBwAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotRtVbrBwAllocated.setStatus("mandatory")
_AmonSlotCbrBwAllocated_Type = Counter32
_AmonSlotCbrBwAllocated_Object = MibTableColumn
amonSlotCbrBwAllocated = _AmonSlotCbrBwAllocated_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 1, 1, 1, 20),
    _AmonSlotCbrBwAllocated_Type()
)
amonSlotCbrBwAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonSlotCbrBwAllocated.setStatus("mandatory")
_AmonPortStatistics_ObjectIdentity = ObjectIdentity
amonPortStatistics = _AmonPortStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2)
)
_AmonPortStatsTable_Object = MibTable
amonPortStatsTable = _AmonPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1)
)
if mibBuilder.loadTexts:
    amonPortStatsTable.setStatus("mandatory")
_AmonPortStatsEntry_Object = MibTableRow
amonPortStatsEntry = _AmonPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1)
)
amonPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    amonPortStatsEntry.setStatus("mandatory")
_AmonPortInCells_Type = Counter32
_AmonPortInCells_Object = MibTableColumn
amonPortInCells = _AmonPortInCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 2),
    _AmonPortInCells_Type()
)
amonPortInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInCells.setStatus("mandatory")
_AmonPortOutCells_Type = Counter32
_AmonPortOutCells_Object = MibTableColumn
amonPortOutCells = _AmonPortOutCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 3),
    _AmonPortOutCells_Type()
)
amonPortOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortOutCells.setStatus("mandatory")
_AmonPortInBadHecCells_Type = Counter32
_AmonPortInBadHecCells_Object = MibTableColumn
amonPortInBadHecCells = _AmonPortInBadHecCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 4),
    _AmonPortInBadHecCells_Type()
)
amonPortInBadHecCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInBadHecCells.setStatus("mandatory")
_AmonPortInUbrCells_Type = Counter32
_AmonPortInUbrCells_Object = MibTableColumn
amonPortInUbrCells = _AmonPortInUbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 5),
    _AmonPortInUbrCells_Type()
)
amonPortInUbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInUbrCells.setStatus("mandatory")
_AmonPortInAbrCells_Type = Counter32
_AmonPortInAbrCells_Object = MibTableColumn
amonPortInAbrCells = _AmonPortInAbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 6),
    _AmonPortInAbrCells_Type()
)
amonPortInAbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInAbrCells.setStatus("mandatory")
_AmonPortInNrtVbrCells_Type = Counter32
_AmonPortInNrtVbrCells_Object = MibTableColumn
amonPortInNrtVbrCells = _AmonPortInNrtVbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 7),
    _AmonPortInNrtVbrCells_Type()
)
amonPortInNrtVbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInNrtVbrCells.setStatus("mandatory")
_AmonPortInRtVbrCells_Type = Counter32
_AmonPortInRtVbrCells_Object = MibTableColumn
amonPortInRtVbrCells = _AmonPortInRtVbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 8),
    _AmonPortInRtVbrCells_Type()
)
amonPortInRtVbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInRtVbrCells.setStatus("mandatory")
_AmonPortInCbrCells_Type = Counter32
_AmonPortInCbrCells_Object = MibTableColumn
amonPortInCbrCells = _AmonPortInCbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 9),
    _AmonPortInCbrCells_Type()
)
amonPortInCbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInCbrCells.setStatus("mandatory")
_AmonPortInPointToPointCells_Type = Counter32
_AmonPortInPointToPointCells_Object = MibTableColumn
amonPortInPointToPointCells = _AmonPortInPointToPointCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 10),
    _AmonPortInPointToPointCells_Type()
)
amonPortInPointToPointCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInPointToPointCells.setStatus("mandatory")
_AmonPortInPointToMultipointCells_Type = Counter32
_AmonPortInPointToMultipointCells_Object = MibTableColumn
amonPortInPointToMultipointCells = _AmonPortInPointToMultipointCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 11),
    _AmonPortInPointToMultipointCells_Type()
)
amonPortInPointToMultipointCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInPointToMultipointCells.setStatus("mandatory")
_AmonPortInPnniCells_Type = Counter32
_AmonPortInPnniCells_Object = MibTableColumn
amonPortInPnniCells = _AmonPortInPnniCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 12),
    _AmonPortInPnniCells_Type()
)
amonPortInPnniCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInPnniCells.setStatus("mandatory")
_AmonPortInSignalingCells_Type = Counter32
_AmonPortInSignalingCells_Object = MibTableColumn
amonPortInSignalingCells = _AmonPortInSignalingCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 13),
    _AmonPortInSignalingCells_Type()
)
amonPortInSignalingCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInSignalingCells.setStatus("mandatory")
_AmonPortInLaneDataDirectCells_Type = Counter32
_AmonPortInLaneDataDirectCells_Object = MibTableColumn
amonPortInLaneDataDirectCells = _AmonPortInLaneDataDirectCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 14),
    _AmonPortInLaneDataDirectCells_Type()
)
amonPortInLaneDataDirectCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInLaneDataDirectCells.setStatus("mandatory")
_AmonPortInLaneMulticastCells_Type = Counter32
_AmonPortInLaneMulticastCells_Object = MibTableColumn
amonPortInLaneMulticastCells = _AmonPortInLaneMulticastCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 15),
    _AmonPortInLaneMulticastCells_Type()
)
amonPortInLaneMulticastCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortInLaneMulticastCells.setStatus("mandatory")
_AmonPortLaneConfigControlCells_Type = Counter32
_AmonPortLaneConfigControlCells_Object = MibTableColumn
amonPortLaneConfigControlCells = _AmonPortLaneConfigControlCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 16),
    _AmonPortLaneConfigControlCells_Type()
)
amonPortLaneConfigControlCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortLaneConfigControlCells.setStatus("mandatory")
_AmonPortDefinityCells_Type = Counter32
_AmonPortDefinityCells_Object = MibTableColumn
amonPortDefinityCells = _AmonPortDefinityCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 2, 1, 1, 17),
    _AmonPortDefinityCells_Type()
)
amonPortDefinityCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonPortDefinityCells.setStatus("mandatory")
_AmonHostStatistics_ObjectIdentity = ObjectIdentity
amonHostStatistics = _AmonHostStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3)
)
_AmonHostTimeTable_Object = MibTable
amonHostTimeTable = _AmonHostTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1)
)
if mibBuilder.loadTexts:
    amonHostTimeTable.setStatus("mandatory")
_AmonHostTimeEntry_Object = MibTableRow
amonHostTimeEntry = _AmonHostTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1)
)
amonHostTimeEntry.setIndexNames(
    (0, "SMONAMON-MIB", "amonHostTimeIndex"),
    (0, "SMONAMON-MIB", "amonHostTimeCreationOrder"),
)
if mibBuilder.loadTexts:
    amonHostTimeEntry.setStatus("mandatory")


class _AmonHostTimeAddress_Type(OctetString):
    """Custom type amonHostTimeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AmonHostTimeAddress_Type.__name__ = "OctetString"
_AmonHostTimeAddress_Object = MibTableColumn
amonHostTimeAddress = _AmonHostTimeAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 1),
    _AmonHostTimeAddress_Type()
)
amonHostTimeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeAddress.setStatus("mandatory")


class _AmonHostTimeIndex_Type(Integer32):
    """Custom type amonHostTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AmonHostTimeIndex_Type.__name__ = "Integer32"
_AmonHostTimeIndex_Object = MibTableColumn
amonHostTimeIndex = _AmonHostTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 2),
    _AmonHostTimeIndex_Type()
)
amonHostTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeIndex.setStatus("mandatory")


class _AmonHostTimeCreationOrder_Type(Integer32):
    """Custom type amonHostTimeCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AmonHostTimeCreationOrder_Type.__name__ = "Integer32"
_AmonHostTimeCreationOrder_Object = MibTableColumn
amonHostTimeCreationOrder = _AmonHostTimeCreationOrder_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 3),
    _AmonHostTimeCreationOrder_Type()
)
amonHostTimeCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeCreationOrder.setStatus("mandatory")
_AmonHostTimeOutCells_Type = Counter32
_AmonHostTimeOutCells_Object = MibTableColumn
amonHostTimeOutCells = _AmonHostTimeOutCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 4),
    _AmonHostTimeOutCells_Type()
)
amonHostTimeOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeOutCells.setStatus("mandatory")
_AmonHostTimeOutUbrCells_Type = Counter32
_AmonHostTimeOutUbrCells_Object = MibTableColumn
amonHostTimeOutUbrCells = _AmonHostTimeOutUbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 5),
    _AmonHostTimeOutUbrCells_Type()
)
amonHostTimeOutUbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeOutUbrCells.setStatus("mandatory")
_AmonHostTimeOutAbrCells_Type = Counter32
_AmonHostTimeOutAbrCells_Object = MibTableColumn
amonHostTimeOutAbrCells = _AmonHostTimeOutAbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 6),
    _AmonHostTimeOutAbrCells_Type()
)
amonHostTimeOutAbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeOutAbrCells.setStatus("mandatory")
_AmonHostTimeOutNrtVbrCells_Type = Counter32
_AmonHostTimeOutNrtVbrCells_Object = MibTableColumn
amonHostTimeOutNrtVbrCells = _AmonHostTimeOutNrtVbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 7),
    _AmonHostTimeOutNrtVbrCells_Type()
)
amonHostTimeOutNrtVbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeOutNrtVbrCells.setStatus("mandatory")
_AmonHostTimeOutRtVbrCells_Type = Counter32
_AmonHostTimeOutRtVbrCells_Object = MibTableColumn
amonHostTimeOutRtVbrCells = _AmonHostTimeOutRtVbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 8),
    _AmonHostTimeOutRtVbrCells_Type()
)
amonHostTimeOutRtVbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeOutRtVbrCells.setStatus("mandatory")
_AmonHostTimeOutCbrCells_Type = Counter32
_AmonHostTimeOutCbrCells_Object = MibTableColumn
amonHostTimeOutCbrCells = _AmonHostTimeOutCbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 9),
    _AmonHostTimeOutCbrCells_Type()
)
amonHostTimeOutCbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeOutCbrCells.setStatus("mandatory")
_AmonHostTimeOutLaneCells_Type = Counter32
_AmonHostTimeOutLaneCells_Object = MibTableColumn
amonHostTimeOutLaneCells = _AmonHostTimeOutLaneCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 10),
    _AmonHostTimeOutLaneCells_Type()
)
amonHostTimeOutLaneCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeOutLaneCells.setStatus("mandatory")
_AmonHostTimeOutLaneDataDirectCells_Type = Counter32
_AmonHostTimeOutLaneDataDirectCells_Object = MibTableColumn
amonHostTimeOutLaneDataDirectCells = _AmonHostTimeOutLaneDataDirectCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 11),
    _AmonHostTimeOutLaneDataDirectCells_Type()
)
amonHostTimeOutLaneDataDirectCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeOutLaneDataDirectCells.setStatus("mandatory")
_AmonHostTimeOutLaneMulticastCells_Type = Counter32
_AmonHostTimeOutLaneMulticastCells_Object = MibTableColumn
amonHostTimeOutLaneMulticastCells = _AmonHostTimeOutLaneMulticastCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 12),
    _AmonHostTimeOutLaneMulticastCells_Type()
)
amonHostTimeOutLaneMulticastCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeOutLaneMulticastCells.setStatus("mandatory")
_AmonHostTimeOutLaneConfigControlCells_Type = Counter32
_AmonHostTimeOutLaneConfigControlCells_Object = MibTableColumn
amonHostTimeOutLaneConfigControlCells = _AmonHostTimeOutLaneConfigControlCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 13),
    _AmonHostTimeOutLaneConfigControlCells_Type()
)
amonHostTimeOutLaneConfigControlCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeOutLaneConfigControlCells.setStatus("mandatory")
_AmonHostTimeOutDefinityCells_Type = Counter32
_AmonHostTimeOutDefinityCells_Object = MibTableColumn
amonHostTimeOutDefinityCells = _AmonHostTimeOutDefinityCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 3, 1, 1, 14),
    _AmonHostTimeOutDefinityCells_Type()
)
amonHostTimeOutDefinityCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonHostTimeOutDefinityCells.setStatus("mandatory")
_AmonHostMatrix_ObjectIdentity = ObjectIdentity
amonHostMatrix = _AmonHostMatrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4)
)
_AmonMatrixTimeTable_Object = MibTable
amonMatrixTimeTable = _AmonMatrixTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4, 1)
)
if mibBuilder.loadTexts:
    amonMatrixTimeTable.setStatus("mandatory")
_AmonMatrixTimeEntry_Object = MibTableRow
amonMatrixTimeEntry = _AmonMatrixTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4, 1, 1)
)
amonMatrixTimeEntry.setIndexNames(
    (0, "SMONAMON-MIB", "amonMatrixTimeIndex"),
    (0, "SMONAMON-MIB", "amonMatrixTimeCreationOrder"),
)
if mibBuilder.loadTexts:
    amonMatrixTimeEntry.setStatus("mandatory")


class _AmonMatrixTimeIndex_Type(Integer32):
    """Custom type amonMatrixTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AmonMatrixTimeIndex_Type.__name__ = "Integer32"
_AmonMatrixTimeIndex_Object = MibTableColumn
amonMatrixTimeIndex = _AmonMatrixTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4, 1, 1, 1),
    _AmonMatrixTimeIndex_Type()
)
amonMatrixTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonMatrixTimeIndex.setStatus("mandatory")


class _AmonMatrixTimeCreationOrder_Type(Integer32):
    """Custom type amonMatrixTimeCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AmonMatrixTimeCreationOrder_Type.__name__ = "Integer32"
_AmonMatrixTimeCreationOrder_Object = MibTableColumn
amonMatrixTimeCreationOrder = _AmonMatrixTimeCreationOrder_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4, 1, 1, 2),
    _AmonMatrixTimeCreationOrder_Type()
)
amonMatrixTimeCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonMatrixTimeCreationOrder.setStatus("mandatory")


class _AmonMatrixTimeSourceAddress_Type(OctetString):
    """Custom type amonMatrixTimeSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AmonMatrixTimeSourceAddress_Type.__name__ = "OctetString"
_AmonMatrixTimeSourceAddress_Object = MibTableColumn
amonMatrixTimeSourceAddress = _AmonMatrixTimeSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4, 1, 1, 3),
    _AmonMatrixTimeSourceAddress_Type()
)
amonMatrixTimeSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonMatrixTimeSourceAddress.setStatus("mandatory")


class _AmonMatrixTimeDestAddress_Type(OctetString):
    """Custom type amonMatrixTimeDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_AmonMatrixTimeDestAddress_Type.__name__ = "OctetString"
_AmonMatrixTimeDestAddress_Object = MibTableColumn
amonMatrixTimeDestAddress = _AmonMatrixTimeDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4, 1, 1, 4),
    _AmonMatrixTimeDestAddress_Type()
)
amonMatrixTimeDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonMatrixTimeDestAddress.setStatus("mandatory")
_AmonMatrixTimeCells_Type = Counter32
_AmonMatrixTimeCells_Object = MibTableColumn
amonMatrixTimeCells = _AmonMatrixTimeCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4, 1, 1, 5),
    _AmonMatrixTimeCells_Type()
)
amonMatrixTimeCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonMatrixTimeCells.setStatus("mandatory")
_AmonMatrixTimeUbrCells_Type = Counter32
_AmonMatrixTimeUbrCells_Object = MibTableColumn
amonMatrixTimeUbrCells = _AmonMatrixTimeUbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4, 1, 1, 6),
    _AmonMatrixTimeUbrCells_Type()
)
amonMatrixTimeUbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonMatrixTimeUbrCells.setStatus("mandatory")
_AmonMatrixTimeAbrCells_Type = Counter32
_AmonMatrixTimeAbrCells_Object = MibTableColumn
amonMatrixTimeAbrCells = _AmonMatrixTimeAbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4, 1, 1, 7),
    _AmonMatrixTimeAbrCells_Type()
)
amonMatrixTimeAbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonMatrixTimeAbrCells.setStatus("mandatory")
_AmonMatrixTimeNrtVbrCells_Type = Counter32
_AmonMatrixTimeNrtVbrCells_Object = MibTableColumn
amonMatrixTimeNrtVbrCells = _AmonMatrixTimeNrtVbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4, 1, 1, 8),
    _AmonMatrixTimeNrtVbrCells_Type()
)
amonMatrixTimeNrtVbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonMatrixTimeNrtVbrCells.setStatus("mandatory")
_AmonMatrixTimeRtVbrCells_Type = Counter32
_AmonMatrixTimeRtVbrCells_Object = MibTableColumn
amonMatrixTimeRtVbrCells = _AmonMatrixTimeRtVbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4, 1, 1, 9),
    _AmonMatrixTimeRtVbrCells_Type()
)
amonMatrixTimeRtVbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonMatrixTimeRtVbrCells.setStatus("mandatory")
_AmonMatrixTimeCbrCells_Type = Counter32
_AmonMatrixTimeCbrCells_Object = MibTableColumn
amonMatrixTimeCbrCells = _AmonMatrixTimeCbrCells_Object(
    (1, 3, 6, 1, 4, 1, 81, 30, 5, 4, 1, 1, 10),
    _AmonMatrixTimeCbrCells_Type()
)
amonMatrixTimeCbrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amonMatrixTimeCbrCells.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMONAMON-MIB",
    **{"smonamon": smonamon,
       "amonSlotStatistics": amonSlotStatistics,
       "amonSlotStatsTable": amonSlotStatsTable,
       "amonSlotStatsEntry": amonSlotStatsEntry,
       "amonSlotInCells": amonSlotInCells,
       "amonSlotBadHecCells": amonSlotBadHecCells,
       "amonSlotDroppedCells": amonSlotDroppedCells,
       "amonSlotUbrCells": amonSlotUbrCells,
       "amonSlotAbrCells": amonSlotAbrCells,
       "amonSlotNrtVbrCells": amonSlotNrtVbrCells,
       "amonSlotRtVbrCells": amonSlotRtVbrCells,
       "amonSlotCbrCells": amonSlotCbrCells,
       "amonSlotPnniCells": amonSlotPnniCells,
       "amonSlotSignalingCells": amonSlotSignalingCells,
       "amonSlotLaneCells": amonSlotLaneCells,
       "amonSlotLaneDataDirectCells": amonSlotLaneDataDirectCells,
       "amonSlotLaneMulticastCells": amonSlotLaneMulticastCells,
       "amonSlotLaneConfigControlCells": amonSlotLaneConfigControlCells,
       "amonSlotDefinityCells": amonSlotDefinityCells,
       "amonSlotTotalBwAllocated": amonSlotTotalBwAllocated,
       "amonSlotAbrBwAllocated": amonSlotAbrBwAllocated,
       "amonSlotNrtVbrBwAllocated": amonSlotNrtVbrBwAllocated,
       "amonSlotRtVbrBwAllocated": amonSlotRtVbrBwAllocated,
       "amonSlotCbrBwAllocated": amonSlotCbrBwAllocated,
       "amonPortStatistics": amonPortStatistics,
       "amonPortStatsTable": amonPortStatsTable,
       "amonPortStatsEntry": amonPortStatsEntry,
       "amonPortInCells": amonPortInCells,
       "amonPortOutCells": amonPortOutCells,
       "amonPortInBadHecCells": amonPortInBadHecCells,
       "amonPortInUbrCells": amonPortInUbrCells,
       "amonPortInAbrCells": amonPortInAbrCells,
       "amonPortInNrtVbrCells": amonPortInNrtVbrCells,
       "amonPortInRtVbrCells": amonPortInRtVbrCells,
       "amonPortInCbrCells": amonPortInCbrCells,
       "amonPortInPointToPointCells": amonPortInPointToPointCells,
       "amonPortInPointToMultipointCells": amonPortInPointToMultipointCells,
       "amonPortInPnniCells": amonPortInPnniCells,
       "amonPortInSignalingCells": amonPortInSignalingCells,
       "amonPortInLaneDataDirectCells": amonPortInLaneDataDirectCells,
       "amonPortInLaneMulticastCells": amonPortInLaneMulticastCells,
       "amonPortLaneConfigControlCells": amonPortLaneConfigControlCells,
       "amonPortDefinityCells": amonPortDefinityCells,
       "amonHostStatistics": amonHostStatistics,
       "amonHostTimeTable": amonHostTimeTable,
       "amonHostTimeEntry": amonHostTimeEntry,
       "amonHostTimeAddress": amonHostTimeAddress,
       "amonHostTimeIndex": amonHostTimeIndex,
       "amonHostTimeCreationOrder": amonHostTimeCreationOrder,
       "amonHostTimeOutCells": amonHostTimeOutCells,
       "amonHostTimeOutUbrCells": amonHostTimeOutUbrCells,
       "amonHostTimeOutAbrCells": amonHostTimeOutAbrCells,
       "amonHostTimeOutNrtVbrCells": amonHostTimeOutNrtVbrCells,
       "amonHostTimeOutRtVbrCells": amonHostTimeOutRtVbrCells,
       "amonHostTimeOutCbrCells": amonHostTimeOutCbrCells,
       "amonHostTimeOutLaneCells": amonHostTimeOutLaneCells,
       "amonHostTimeOutLaneDataDirectCells": amonHostTimeOutLaneDataDirectCells,
       "amonHostTimeOutLaneMulticastCells": amonHostTimeOutLaneMulticastCells,
       "amonHostTimeOutLaneConfigControlCells": amonHostTimeOutLaneConfigControlCells,
       "amonHostTimeOutDefinityCells": amonHostTimeOutDefinityCells,
       "amonHostMatrix": amonHostMatrix,
       "amonMatrixTimeTable": amonMatrixTimeTable,
       "amonMatrixTimeEntry": amonMatrixTimeEntry,
       "amonMatrixTimeIndex": amonMatrixTimeIndex,
       "amonMatrixTimeCreationOrder": amonMatrixTimeCreationOrder,
       "amonMatrixTimeSourceAddress": amonMatrixTimeSourceAddress,
       "amonMatrixTimeDestAddress": amonMatrixTimeDestAddress,
       "amonMatrixTimeCells": amonMatrixTimeCells,
       "amonMatrixTimeUbrCells": amonMatrixTimeUbrCells,
       "amonMatrixTimeAbrCells": amonMatrixTimeAbrCells,
       "amonMatrixTimeNrtVbrCells": amonMatrixTimeNrtVbrCells,
       "amonMatrixTimeRtVbrCells": amonMatrixTimeRtVbrCells,
       "amonMatrixTimeCbrCells": amonMatrixTimeCbrCells}
)
