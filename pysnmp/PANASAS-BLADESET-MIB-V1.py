# SNMP MIB module (PANASAS-BLADESET-MIB-V1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANASAS-BLADESET-MIB-V1
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:35 2024
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

(panFs,) = mibBuilder.importSymbols(
    "PANASAS-PANFS-MIB-V1",
    "panFs")

(PanSerialNumber,) = mibBuilder.importSymbols(
    "PANASAS-TC-MIB",
    "PanSerialNumber")

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

panBSet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3)
)
panBSet.setRevisions(
        ("2011-04-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PanBSetTable_Object = MibTable
panBSetTable = _PanBSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    panBSetTable.setStatus("current")
_PanBSetEntry_Object = MibTableRow
panBSetEntry = _PanBSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 1, 1)
)
panBSetEntry.setIndexNames(
    (0, "PANASAS-BLADESET-MIB-V1", "panBSetName"),
)
if mibBuilder.loadTexts:
    panBSetEntry.setStatus("current")
_PanBSetName_Type = DisplayString
_PanBSetName_Object = MibTableColumn
panBSetName = _PanBSetName_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 1, 1, 1),
    _PanBSetName_Type()
)
panBSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panBSetName.setStatus("current")
_PanBSetNumBlades_Type = DisplayString
_PanBSetNumBlades_Object = MibTableColumn
panBSetNumBlades = _PanBSetNumBlades_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 1, 1, 2),
    _PanBSetNumBlades_Type()
)
panBSetNumBlades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panBSetNumBlades.setStatus("current")
_PanBSetAvailSpares_Type = DisplayString
_PanBSetAvailSpares_Object = MibTableColumn
panBSetAvailSpares = _PanBSetAvailSpares_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 1, 1, 3),
    _PanBSetAvailSpares_Type()
)
panBSetAvailSpares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panBSetAvailSpares.setStatus("current")
_PanBSetRequestedSpares_Type = DisplayString
_PanBSetRequestedSpares_Object = MibTableColumn
panBSetRequestedSpares = _PanBSetRequestedSpares_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 1, 1, 4),
    _PanBSetRequestedSpares_Type()
)
panBSetRequestedSpares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panBSetRequestedSpares.setStatus("current")
_PanBSetTotalCapacity_Type = Unsigned32
_PanBSetTotalCapacity_Object = MibTableColumn
panBSetTotalCapacity = _PanBSetTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 1, 1, 5),
    _PanBSetTotalCapacity_Type()
)
panBSetTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panBSetTotalCapacity.setStatus("current")
_PanBSetReservedCapacity_Type = Unsigned32
_PanBSetReservedCapacity_Object = MibTableColumn
panBSetReservedCapacity = _PanBSetReservedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 1, 1, 6),
    _PanBSetReservedCapacity_Type()
)
panBSetReservedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panBSetReservedCapacity.setStatus("current")
_PanBSetUsedCapacity_Type = Unsigned32
_PanBSetUsedCapacity_Object = MibTableColumn
panBSetUsedCapacity = _PanBSetUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 1, 1, 7),
    _PanBSetUsedCapacity_Type()
)
panBSetUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panBSetUsedCapacity.setStatus("current")
_PanBSetAvailableCapacity_Type = Unsigned32
_PanBSetAvailableCapacity_Object = MibTableColumn
panBSetAvailableCapacity = _PanBSetAvailableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 1, 1, 8),
    _PanBSetAvailableCapacity_Type()
)
panBSetAvailableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panBSetAvailableCapacity.setStatus("current")
_PanBSetInfo_Type = DisplayString
_PanBSetInfo_Object = MibTableColumn
panBSetInfo = _PanBSetInfo_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 1, 1, 9),
    _PanBSetInfo_Type()
)
panBSetInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panBSetInfo.setStatus("current")
_PanBSetBladesTable_Object = MibTable
panBSetBladesTable = _PanBSetBladesTable_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    panBSetBladesTable.setStatus("obsolete")
_PanBSetBladesEntry_Object = MibTableRow
panBSetBladesEntry = _PanBSetBladesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 2, 1)
)
panBSetBladesEntry.setIndexNames(
    (0, "PANASAS-BLADESET-MIB-V1", "panBSetName"),
    (0, "PANASAS-BLADESET-MIB-V1", "panBSetBladeIndex"),
)
if mibBuilder.loadTexts:
    panBSetBladesEntry.setStatus("obsolete")
_PanBSetBladeIndex_Type = Unsigned32
_PanBSetBladeIndex_Object = MibTableColumn
panBSetBladeIndex = _PanBSetBladeIndex_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 2, 1, 1),
    _PanBSetBladeIndex_Type()
)
panBSetBladeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panBSetBladeIndex.setStatus("obsolete")
_PanBSetBladeHwSn_Type = PanSerialNumber
_PanBSetBladeHwSn_Object = MibTableColumn
panBSetBladeHwSn = _PanBSetBladeHwSn_Object(
    (1, 3, 6, 1, 4, 1, 10159, 1, 3, 3, 2, 1, 2),
    _PanBSetBladeHwSn_Type()
)
panBSetBladeHwSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panBSetBladeHwSn.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANASAS-BLADESET-MIB-V1",
    **{"panBSet": panBSet,
       "panBSetTable": panBSetTable,
       "panBSetEntry": panBSetEntry,
       "panBSetName": panBSetName,
       "panBSetNumBlades": panBSetNumBlades,
       "panBSetAvailSpares": panBSetAvailSpares,
       "panBSetRequestedSpares": panBSetRequestedSpares,
       "panBSetTotalCapacity": panBSetTotalCapacity,
       "panBSetReservedCapacity": panBSetReservedCapacity,
       "panBSetUsedCapacity": panBSetUsedCapacity,
       "panBSetAvailableCapacity": panBSetAvailableCapacity,
       "panBSetInfo": panBSetInfo,
       "panBSetBladesTable": panBSetBladesTable,
       "panBSetBladesEntry": panBSetBladesEntry,
       "panBSetBladeIndex": panBSetBladeIndex,
       "panBSetBladeHwSn": panBSetBladeHwSn}
)
