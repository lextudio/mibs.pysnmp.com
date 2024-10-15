# SNMP MIB module (ZHNHPNA) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHNHPNA
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:59 2024
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
 enterprises,
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
    "enterprises",
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

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")


# MODULE-IDENTITY

zhnHpna = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47)
)
zhnHpna.setRevisions(
        ("2012-04-25 12:00",
         "2012-01-30 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhnHpnaObjects_ObjectIdentity = ObjectIdentity
zhnHpnaObjects = _ZhnHpnaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1)
)
_HpnaDeviceTable_Object = MibTable
hpnaDeviceTable = _HpnaDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 1)
)
if mibBuilder.loadTexts:
    hpnaDeviceTable.setStatus("current")
_HpnaDeviceEntry_Object = MibTableRow
hpnaDeviceEntry = _HpnaDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 1, 1)
)
hpnaDeviceEntry.setIndexNames(
    (0, "ZHNHPNA", "hpnaDeviceIndex"),
)
if mibBuilder.loadTexts:
    hpnaDeviceEntry.setStatus("current")
_HpnaDeviceIndex_Type = Unsigned32
_HpnaDeviceIndex_Object = MibTableColumn
hpnaDeviceIndex = _HpnaDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 1, 1, 1),
    _HpnaDeviceIndex_Type()
)
hpnaDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnaDeviceIndex.setStatus("current")
_HpnaDeviceMAC_Type = MacAddress
_HpnaDeviceMAC_Object = MibTableColumn
hpnaDeviceMAC = _HpnaDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 1, 1, 2),
    _HpnaDeviceMAC_Type()
)
hpnaDeviceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnaDeviceMAC.setStatus("current")
_HpnaDeviceHWVersion_Type = OctetString
_HpnaDeviceHWVersion_Object = MibTableColumn
hpnaDeviceHWVersion = _HpnaDeviceHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 1, 1, 3),
    _HpnaDeviceHWVersion_Type()
)
hpnaDeviceHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnaDeviceHWVersion.setStatus("current")
_HpnaDeviceFWVersion_Type = OctetString
_HpnaDeviceFWVersion_Object = MibTableColumn
hpnaDeviceFWVersion = _HpnaDeviceFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 1, 1, 4),
    _HpnaDeviceFWVersion_Type()
)
hpnaDeviceFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnaDeviceFWVersion.setStatus("current")
_HcnaDeviceTable_Object = MibTable
hcnaDeviceTable = _HcnaDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 2)
)
if mibBuilder.loadTexts:
    hcnaDeviceTable.setStatus("current")
_HcnaDeviceEntry_Object = MibTableRow
hcnaDeviceEntry = _HcnaDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 2, 1)
)
hcnaDeviceEntry.setIndexNames(
    (0, "ZHNHPNA", "hcnaDeviceIndex"),
)
if mibBuilder.loadTexts:
    hcnaDeviceEntry.setStatus("current")
_HcnaDeviceIndex_Type = Unsigned32
_HcnaDeviceIndex_Object = MibTableColumn
hcnaDeviceIndex = _HcnaDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 2, 1, 1),
    _HcnaDeviceIndex_Type()
)
hcnaDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hcnaDeviceIndex.setStatus("current")
_HcnaDeviceMAC_Type = MacAddress
_HcnaDeviceMAC_Object = MibTableColumn
hcnaDeviceMAC = _HcnaDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 2, 1, 2),
    _HcnaDeviceMAC_Type()
)
hcnaDeviceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcnaDeviceMAC.setStatus("current")
_HcnaDeviceHWVersion_Type = OctetString
_HcnaDeviceHWVersion_Object = MibTableColumn
hcnaDeviceHWVersion = _HcnaDeviceHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 2, 1, 3),
    _HcnaDeviceHWVersion_Type()
)
hcnaDeviceHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcnaDeviceHWVersion.setStatus("current")
_HcnaDeviceFWVersion_Type = OctetString
_HcnaDeviceFWVersion_Object = MibTableColumn
hcnaDeviceFWVersion = _HcnaDeviceFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 2, 1, 4),
    _HcnaDeviceFWVersion_Type()
)
hcnaDeviceFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcnaDeviceFWVersion.setStatus("current")
_HpnaStationsTable_Object = MibTable
hpnaStationsTable = _HpnaStationsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 3)
)
if mibBuilder.loadTexts:
    hpnaStationsTable.setStatus("current")
_HpnaStationsEntry_Object = MibTableRow
hpnaStationsEntry = _HpnaStationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 3, 1)
)
hpnaStationsEntry.setIndexNames(
    (0, "ZHNHPNA", "hpnaStationIndex"),
)
if mibBuilder.loadTexts:
    hpnaStationsEntry.setStatus("current")
_HpnaStationIndex_Type = Unsigned32
_HpnaStationIndex_Object = MibTableColumn
hpnaStationIndex = _HpnaStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 3, 1, 1),
    _HpnaStationIndex_Type()
)
hpnaStationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnaStationIndex.setStatus("current")
_HpnaStationSource_Type = MacAddress
_HpnaStationSource_Object = MibTableColumn
hpnaStationSource = _HpnaStationSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 3, 1, 2),
    _HpnaStationSource_Type()
)
hpnaStationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnaStationSource.setStatus("current")
_HpnaStationDestination_Type = MacAddress
_HpnaStationDestination_Object = MibTableColumn
hpnaStationDestination = _HpnaStationDestination_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 3, 1, 3),
    _HpnaStationDestination_Type()
)
hpnaStationDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnaStationDestination.setStatus("current")
_HpnaStationRate_Type = Unsigned32
_HpnaStationRate_Object = MibTableColumn
hpnaStationRate = _HpnaStationRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 3, 1, 4),
    _HpnaStationRate_Type()
)
hpnaStationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnaStationRate.setStatus("current")
_HpnaStationSymbolRate_Type = Unsigned32
_HpnaStationSymbolRate_Object = MibTableColumn
hpnaStationSymbolRate = _HpnaStationSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 3, 1, 5),
    _HpnaStationSymbolRate_Type()
)
hpnaStationSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnaStationSymbolRate.setStatus("current")
_HpnaStationBitsPerSymbol_Type = Unsigned32
_HpnaStationBitsPerSymbol_Object = MibTableColumn
hpnaStationBitsPerSymbol = _HpnaStationBitsPerSymbol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 3, 1, 6),
    _HpnaStationBitsPerSymbol_Type()
)
hpnaStationBitsPerSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnaStationBitsPerSymbol.setStatus("current")
_HpnaStationRxPower_Type = Integer32
_HpnaStationRxPower_Object = MibTableColumn
hpnaStationRxPower = _HpnaStationRxPower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 3, 1, 7),
    _HpnaStationRxPower_Type()
)
hpnaStationRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnaStationRxPower.setStatus("current")
_HcnaStationsTable_Object = MibTable
hcnaStationsTable = _HcnaStationsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 4)
)
if mibBuilder.loadTexts:
    hcnaStationsTable.setStatus("current")
_HcnaStationsEntry_Object = MibTableRow
hcnaStationsEntry = _HcnaStationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 4, 1)
)
hcnaStationsEntry.setIndexNames(
    (0, "ZHNHPNA", "hcnaStationIndex"),
)
if mibBuilder.loadTexts:
    hcnaStationsEntry.setStatus("current")
_HcnaStationIndex_Type = Unsigned32
_HcnaStationIndex_Object = MibTableColumn
hcnaStationIndex = _HcnaStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 4, 1, 1),
    _HcnaStationIndex_Type()
)
hcnaStationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hcnaStationIndex.setStatus("current")
_HcnaStationSource_Type = MacAddress
_HcnaStationSource_Object = MibTableColumn
hcnaStationSource = _HcnaStationSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 4, 1, 2),
    _HcnaStationSource_Type()
)
hcnaStationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcnaStationSource.setStatus("current")
_HcnaStationDestination_Type = MacAddress
_HcnaStationDestination_Object = MibTableColumn
hcnaStationDestination = _HcnaStationDestination_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 4, 1, 3),
    _HcnaStationDestination_Type()
)
hcnaStationDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcnaStationDestination.setStatus("current")
_HcnaStationRate_Type = Unsigned32
_HcnaStationRate_Object = MibTableColumn
hcnaStationRate = _HcnaStationRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 4, 1, 4),
    _HcnaStationRate_Type()
)
hcnaStationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcnaStationRate.setStatus("current")
_HcnaStationSymbolRate_Type = Unsigned32
_HcnaStationSymbolRate_Object = MibTableColumn
hcnaStationSymbolRate = _HcnaStationSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 4, 1, 5),
    _HcnaStationSymbolRate_Type()
)
hcnaStationSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcnaStationSymbolRate.setStatus("current")
_HcnaStationBitsPerSymbol_Type = Unsigned32
_HcnaStationBitsPerSymbol_Object = MibTableColumn
hcnaStationBitsPerSymbol = _HcnaStationBitsPerSymbol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 4, 1, 6),
    _HcnaStationBitsPerSymbol_Type()
)
hcnaStationBitsPerSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcnaStationBitsPerSymbol.setStatus("current")
_HcnaStationRxPower_Type = Integer32
_HcnaStationRxPower_Object = MibTableColumn
hcnaStationRxPower = _HcnaStationRxPower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 1, 4, 1, 7),
    _HcnaStationRxPower_Type()
)
hcnaStationRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcnaStationRxPower.setStatus("current")
_ZhnHpnaConformance_ObjectIdentity = ObjectIdentity
zhnHpnaConformance = _ZhnHpnaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 2)
)
_ZhnHpnaGroups_ObjectIdentity = ObjectIdentity
zhnHpnaGroups = _ZhnHpnaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 2, 1)
)
_ZhnHpnaCompliances_ObjectIdentity = ObjectIdentity
zhnHpnaCompliances = _ZhnHpnaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 2, 2)
)

# Managed Objects groups

zhnHpnaDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 2, 1, 1)
)
zhnHpnaDeviceGroup.setObjects(
      *(("ZHNHPNA", "hpnaDeviceMAC"),
        ("ZHNHPNA", "hpnaDeviceHWVersion"),
        ("ZHNHPNA", "hpnaDeviceFWVersion"))
)
if mibBuilder.loadTexts:
    zhnHpnaDeviceGroup.setStatus("current")

zhnHcnaDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 2, 1, 2)
)
zhnHcnaDeviceGroup.setObjects(
      *(("ZHNHPNA", "hcnaDeviceMAC"),
        ("ZHNHPNA", "hcnaDeviceHWVersion"),
        ("ZHNHPNA", "hcnaDeviceFWVersion"))
)
if mibBuilder.loadTexts:
    zhnHcnaDeviceGroup.setStatus("current")

zhnHpnaStationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 2, 1, 3)
)
zhnHpnaStationsGroup.setObjects(
      *(("ZHNHPNA", "hpnaStationSource"),
        ("ZHNHPNA", "hpnaStationDestination"),
        ("ZHNHPNA", "hpnaStationRate"),
        ("ZHNHPNA", "hpnaStationSymbolRate"),
        ("ZHNHPNA", "hpnaStationBitsPerSymbol"),
        ("ZHNHPNA", "hpnaStationRxPower"))
)
if mibBuilder.loadTexts:
    zhnHpnaStationsGroup.setStatus("current")

zhnHcnaStationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 2, 1, 4)
)
zhnHcnaStationsGroup.setObjects(
      *(("ZHNHPNA", "hcnaStationSource"),
        ("ZHNHPNA", "hcnaStationDestination"),
        ("ZHNHPNA", "hcnaStationRate"),
        ("ZHNHPNA", "hcnaStationSymbolRate"),
        ("ZHNHPNA", "hcnaStationBitsPerSymbol"),
        ("ZHNHPNA", "hcnaStationRxPower"))
)
if mibBuilder.loadTexts:
    zhnHcnaStationsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

zhnHpnaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 47, 2, 2, 1)
)
if mibBuilder.loadTexts:
    zhnHpnaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHNHPNA",
    **{"zhnHpna": zhnHpna,
       "zhnHpnaObjects": zhnHpnaObjects,
       "hpnaDeviceTable": hpnaDeviceTable,
       "hpnaDeviceEntry": hpnaDeviceEntry,
       "hpnaDeviceIndex": hpnaDeviceIndex,
       "hpnaDeviceMAC": hpnaDeviceMAC,
       "hpnaDeviceHWVersion": hpnaDeviceHWVersion,
       "hpnaDeviceFWVersion": hpnaDeviceFWVersion,
       "hcnaDeviceTable": hcnaDeviceTable,
       "hcnaDeviceEntry": hcnaDeviceEntry,
       "hcnaDeviceIndex": hcnaDeviceIndex,
       "hcnaDeviceMAC": hcnaDeviceMAC,
       "hcnaDeviceHWVersion": hcnaDeviceHWVersion,
       "hcnaDeviceFWVersion": hcnaDeviceFWVersion,
       "hpnaStationsTable": hpnaStationsTable,
       "hpnaStationsEntry": hpnaStationsEntry,
       "hpnaStationIndex": hpnaStationIndex,
       "hpnaStationSource": hpnaStationSource,
       "hpnaStationDestination": hpnaStationDestination,
       "hpnaStationRate": hpnaStationRate,
       "hpnaStationSymbolRate": hpnaStationSymbolRate,
       "hpnaStationBitsPerSymbol": hpnaStationBitsPerSymbol,
       "hpnaStationRxPower": hpnaStationRxPower,
       "hcnaStationsTable": hcnaStationsTable,
       "hcnaStationsEntry": hcnaStationsEntry,
       "hcnaStationIndex": hcnaStationIndex,
       "hcnaStationSource": hcnaStationSource,
       "hcnaStationDestination": hcnaStationDestination,
       "hcnaStationRate": hcnaStationRate,
       "hcnaStationSymbolRate": hcnaStationSymbolRate,
       "hcnaStationBitsPerSymbol": hcnaStationBitsPerSymbol,
       "hcnaStationRxPower": hcnaStationRxPower,
       "zhnHpnaConformance": zhnHpnaConformance,
       "zhnHpnaGroups": zhnHpnaGroups,
       "zhnHpnaDeviceGroup": zhnHpnaDeviceGroup,
       "zhnHcnaDeviceGroup": zhnHcnaDeviceGroup,
       "zhnHpnaStationsGroup": zhnHpnaStationsGroup,
       "zhnHcnaStationsGroup": zhnHcnaStationsGroup,
       "zhnHpnaCompliances": zhnHpnaCompliances,
       "zhnHpnaCompliance": zhnHpnaCompliance}
)
