# SNMP MIB module (WLSX-SNR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-SNR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:11 2024
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")

(monPhyAddress,
 monRadioNumber,
 monitoredApBSSID,
 monitoredStaPhyAddress) = mibBuilder.importSymbols(
    "WLSX-MON-MIB",
    "monPhyAddress",
    "monRadioNumber",
    "monitoredApBSSID",
    "monitoredStaPhyAddress")


# MODULE-IDENTITY

wlsxSNRMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7)
)
wlsxSNRMIB.setRevisions(
        ("1906-11-27 20:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxSNRGroup_ObjectIdentity = ObjectIdentity
wlsxSNRGroup = _WlsxSNRGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1)
)
_WlsxAPSnrTable_Object = MibTable
wlsxAPSnrTable = _WlsxAPSnrTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxAPSnrTable.setStatus("current")
_WlsxAPSnrEntry_Object = MibTableRow
wlsxAPSnrEntry = _WlsxAPSnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 1, 1)
)
wlsxAPSnrEntry.setIndexNames(
    (0, "WLSX-MON-MIB", "monPhyAddress"),
    (0, "WLSX-MON-MIB", "monRadioNumber"),
    (0, "WLSX-MON-MIB", "monitoredApBSSID"),
)
if mibBuilder.loadTexts:
    wlsxAPSnrEntry.setStatus("current")
_ApSnrAverageSignalStrength_Type = Integer32
_ApSnrAverageSignalStrength_Object = MibTableColumn
apSnrAverageSignalStrength = _ApSnrAverageSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 1, 1, 1),
    _ApSnrAverageSignalStrength_Type()
)
apSnrAverageSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnrAverageSignalStrength.setStatus("current")
_ApSnrSignalPkts_Type = Integer32
_ApSnrSignalPkts_Object = MibTableColumn
apSnrSignalPkts = _ApSnrSignalPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 1, 1, 2),
    _ApSnrSignalPkts_Type()
)
apSnrSignalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnrSignalPkts.setStatus("current")
_ApSnrHighestRxSignalStrength_Type = Integer32
_ApSnrHighestRxSignalStrength_Object = MibTableColumn
apSnrHighestRxSignalStrength = _ApSnrHighestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 1, 1, 3),
    _ApSnrHighestRxSignalStrength_Type()
)
apSnrHighestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnrHighestRxSignalStrength.setStatus("current")
_ApSnrLowestRxSignalStrength_Type = Integer32
_ApSnrLowestRxSignalStrength_Object = MibTableColumn
apSnrLowestRxSignalStrength = _ApSnrLowestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 1, 1, 4),
    _ApSnrLowestRxSignalStrength_Type()
)
apSnrLowestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnrLowestRxSignalStrength.setStatus("current")
_ApSnrSampleTime_Type = Integer32
_ApSnrSampleTime_Object = MibTableColumn
apSnrSampleTime = _ApSnrSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 1, 1, 5),
    _ApSnrSampleTime_Type()
)
apSnrSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnrSampleTime.setStatus("current")
_WlsxStaSnrTable_Object = MibTable
wlsxStaSnrTable = _WlsxStaSnrTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxStaSnrTable.setStatus("current")
_WlsxStaSnrEntry_Object = MibTableRow
wlsxStaSnrEntry = _WlsxStaSnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 2, 1)
)
wlsxStaSnrEntry.setIndexNames(
    (0, "WLSX-MON-MIB", "monPhyAddress"),
    (0, "WLSX-MON-MIB", "monRadioNumber"),
    (0, "WLSX-MON-MIB", "monitoredStaPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxStaSnrEntry.setStatus("current")
_StaSnrAverageSignalStrength_Type = Integer32
_StaSnrAverageSignalStrength_Object = MibTableColumn
staSnrAverageSignalStrength = _StaSnrAverageSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 2, 1, 1),
    _StaSnrAverageSignalStrength_Type()
)
staSnrAverageSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSnrAverageSignalStrength.setStatus("current")
_StaSnrSignalPkts_Type = Integer32
_StaSnrSignalPkts_Object = MibTableColumn
staSnrSignalPkts = _StaSnrSignalPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 2, 1, 2),
    _StaSnrSignalPkts_Type()
)
staSnrSignalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSnrSignalPkts.setStatus("current")
_StaSnrHighestRxSignalStrength_Type = Integer32
_StaSnrHighestRxSignalStrength_Object = MibTableColumn
staSnrHighestRxSignalStrength = _StaSnrHighestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 2, 1, 3),
    _StaSnrHighestRxSignalStrength_Type()
)
staSnrHighestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSnrHighestRxSignalStrength.setStatus("current")
_StaSnrLowestRxSignalStrength_Type = Integer32
_StaSnrLowestRxSignalStrength_Object = MibTableColumn
staSnrLowestRxSignalStrength = _StaSnrLowestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 2, 1, 4),
    _StaSnrLowestRxSignalStrength_Type()
)
staSnrLowestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSnrLowestRxSignalStrength.setStatus("current")
_StaSnrSampleTime_Type = Integer32
_StaSnrSampleTime_Object = MibTableColumn
staSnrSampleTime = _StaSnrSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 2, 1, 5),
    _StaSnrSampleTime_Type()
)
staSnrSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSnrSampleTime.setStatus("current")
_WlsxAPSnrBSSIDTable_Object = MibTable
wlsxAPSnrBSSIDTable = _WlsxAPSnrBSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 3)
)
if mibBuilder.loadTexts:
    wlsxAPSnrBSSIDTable.setStatus("current")
_WlsxAPSnrBSSIDEntry_Object = MibTableRow
wlsxAPSnrBSSIDEntry = _WlsxAPSnrBSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 3, 1)
)
wlsxAPSnrBSSIDEntry.setIndexNames(
    (0, "WLSX-MON-MIB", "monitoredApBSSID"),
    (0, "WLSX-MON-MIB", "monPhyAddress"),
    (0, "WLSX-MON-MIB", "monRadioNumber"),
)
if mibBuilder.loadTexts:
    wlsxAPSnrBSSIDEntry.setStatus("current")
_ApSnrBSSIDAverageSignalStrength_Type = Integer32
_ApSnrBSSIDAverageSignalStrength_Object = MibTableColumn
apSnrBSSIDAverageSignalStrength = _ApSnrBSSIDAverageSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 3, 1, 1),
    _ApSnrBSSIDAverageSignalStrength_Type()
)
apSnrBSSIDAverageSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnrBSSIDAverageSignalStrength.setStatus("current")
_ApSnrBSSIDSignalPkts_Type = Integer32
_ApSnrBSSIDSignalPkts_Object = MibTableColumn
apSnrBSSIDSignalPkts = _ApSnrBSSIDSignalPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 3, 1, 2),
    _ApSnrBSSIDSignalPkts_Type()
)
apSnrBSSIDSignalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnrBSSIDSignalPkts.setStatus("current")
_ApSnrBSSIDHighestRxSignalStrength_Type = Integer32
_ApSnrBSSIDHighestRxSignalStrength_Object = MibTableColumn
apSnrBSSIDHighestRxSignalStrength = _ApSnrBSSIDHighestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 3, 1, 3),
    _ApSnrBSSIDHighestRxSignalStrength_Type()
)
apSnrBSSIDHighestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnrBSSIDHighestRxSignalStrength.setStatus("current")
_ApSnrBSSIDLowestRxSignalStrength_Type = Integer32
_ApSnrBSSIDLowestRxSignalStrength_Object = MibTableColumn
apSnrBSSIDLowestRxSignalStrength = _ApSnrBSSIDLowestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 3, 1, 4),
    _ApSnrBSSIDLowestRxSignalStrength_Type()
)
apSnrBSSIDLowestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnrBSSIDLowestRxSignalStrength.setStatus("current")
_ApSnrBSSIDSampleTime_Type = Integer32
_ApSnrBSSIDSampleTime_Object = MibTableColumn
apSnrBSSIDSampleTime = _ApSnrBSSIDSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 3, 1, 5),
    _ApSnrBSSIDSampleTime_Type()
)
apSnrBSSIDSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnrBSSIDSampleTime.setStatus("current")
_WlsxStaSnrPhyTable_Object = MibTable
wlsxStaSnrPhyTable = _WlsxStaSnrPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 4)
)
if mibBuilder.loadTexts:
    wlsxStaSnrPhyTable.setStatus("current")
_WlsxStaSnrPhyEntry_Object = MibTableRow
wlsxStaSnrPhyEntry = _WlsxStaSnrPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 4, 1)
)
wlsxStaSnrPhyEntry.setIndexNames(
    (0, "WLSX-MON-MIB", "monitoredStaPhyAddress"),
    (0, "WLSX-MON-MIB", "monPhyAddress"),
    (0, "WLSX-MON-MIB", "monRadioNumber"),
)
if mibBuilder.loadTexts:
    wlsxStaSnrPhyEntry.setStatus("current")
_StaSnrPhyAverageSignalStrength_Type = Integer32
_StaSnrPhyAverageSignalStrength_Object = MibTableColumn
staSnrPhyAverageSignalStrength = _StaSnrPhyAverageSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 4, 1, 1),
    _StaSnrPhyAverageSignalStrength_Type()
)
staSnrPhyAverageSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSnrPhyAverageSignalStrength.setStatus("current")
_StaSnrPhySignalPkts_Type = Integer32
_StaSnrPhySignalPkts_Object = MibTableColumn
staSnrPhySignalPkts = _StaSnrPhySignalPkts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 4, 1, 2),
    _StaSnrPhySignalPkts_Type()
)
staSnrPhySignalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSnrPhySignalPkts.setStatus("current")
_StaSnrPhyHighestRxSignalStrength_Type = Integer32
_StaSnrPhyHighestRxSignalStrength_Object = MibTableColumn
staSnrPhyHighestRxSignalStrength = _StaSnrPhyHighestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 4, 1, 3),
    _StaSnrPhyHighestRxSignalStrength_Type()
)
staSnrPhyHighestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSnrPhyHighestRxSignalStrength.setStatus("current")
_StaSnrPhyLowestRxSignalStrength_Type = Integer32
_StaSnrPhyLowestRxSignalStrength_Object = MibTableColumn
staSnrPhyLowestRxSignalStrength = _StaSnrPhyLowestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 4, 1, 4),
    _StaSnrPhyLowestRxSignalStrength_Type()
)
staSnrPhyLowestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSnrPhyLowestRxSignalStrength.setStatus("current")
_StaSnrPhySampleTime_Type = Integer32
_StaSnrPhySampleTime_Object = MibTableColumn
staSnrPhySampleTime = _StaSnrPhySampleTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 7, 1, 4, 1, 5),
    _StaSnrPhySampleTime_Type()
)
staSnrPhySampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSnrPhySampleTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-SNR-MIB",
    **{"wlsxSNRMIB": wlsxSNRMIB,
       "wlsxSNRGroup": wlsxSNRGroup,
       "wlsxAPSnrTable": wlsxAPSnrTable,
       "wlsxAPSnrEntry": wlsxAPSnrEntry,
       "apSnrAverageSignalStrength": apSnrAverageSignalStrength,
       "apSnrSignalPkts": apSnrSignalPkts,
       "apSnrHighestRxSignalStrength": apSnrHighestRxSignalStrength,
       "apSnrLowestRxSignalStrength": apSnrLowestRxSignalStrength,
       "apSnrSampleTime": apSnrSampleTime,
       "wlsxStaSnrTable": wlsxStaSnrTable,
       "wlsxStaSnrEntry": wlsxStaSnrEntry,
       "staSnrAverageSignalStrength": staSnrAverageSignalStrength,
       "staSnrSignalPkts": staSnrSignalPkts,
       "staSnrHighestRxSignalStrength": staSnrHighestRxSignalStrength,
       "staSnrLowestRxSignalStrength": staSnrLowestRxSignalStrength,
       "staSnrSampleTime": staSnrSampleTime,
       "wlsxAPSnrBSSIDTable": wlsxAPSnrBSSIDTable,
       "wlsxAPSnrBSSIDEntry": wlsxAPSnrBSSIDEntry,
       "apSnrBSSIDAverageSignalStrength": apSnrBSSIDAverageSignalStrength,
       "apSnrBSSIDSignalPkts": apSnrBSSIDSignalPkts,
       "apSnrBSSIDHighestRxSignalStrength": apSnrBSSIDHighestRxSignalStrength,
       "apSnrBSSIDLowestRxSignalStrength": apSnrBSSIDLowestRxSignalStrength,
       "apSnrBSSIDSampleTime": apSnrBSSIDSampleTime,
       "wlsxStaSnrPhyTable": wlsxStaSnrPhyTable,
       "wlsxStaSnrPhyEntry": wlsxStaSnrPhyEntry,
       "staSnrPhyAverageSignalStrength": staSnrPhyAverageSignalStrength,
       "staSnrPhySignalPkts": staSnrPhySignalPkts,
       "staSnrPhyHighestRxSignalStrength": staSnrPhyHighestRxSignalStrength,
       "staSnrPhyLowestRxSignalStrength": staSnrPhyLowestRxSignalStrength,
       "staSnrPhySampleTime": staSnrPhySampleTime}
)
