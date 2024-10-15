# SNMP MIB module (BSUSUSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BSUSUSTATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:48 2024
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

(aniBsuSuGroup,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "aniBsuSuGroup")

(aniBsuSuMacAddr,) = mibBuilder.importSymbols(
    "BSUSUINV-MIB",
    "aniBsuSuMacAddr")

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

aniBsuSuStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniBsuSuServStatsTable_Object = MibTable
aniBsuSuServStatsTable = _AniBsuSuServStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 1)
)
if mibBuilder.loadTexts:
    aniBsuSuServStatsTable.setStatus("current")
_AniBsuSuServStatsEntry_Object = MibTableRow
aniBsuSuServStatsEntry = _AniBsuSuServStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 1, 1)
)
aniBsuSuServStatsEntry.setIndexNames(
    (0, "BSUSUINV-MIB", "aniBsuSuMacAddr"),
    (0, "BSUSUSTATS-MIB", "aniBsuSuServStatsFlowId"),
)
if mibBuilder.loadTexts:
    aniBsuSuServStatsEntry.setStatus("current")
_AniBsuSuServStatsFlowId_Type = Integer32
_AniBsuSuServStatsFlowId_Object = MibTableColumn
aniBsuSuServStatsFlowId = _AniBsuSuServStatsFlowId_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 1, 1, 1),
    _AniBsuSuServStatsFlowId_Type()
)
aniBsuSuServStatsFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuServStatsFlowId.setStatus("current")
_AniBsuSuServStatsDSEthernetPkts_Type = Counter32
_AniBsuSuServStatsDSEthernetPkts_Object = MibTableColumn
aniBsuSuServStatsDSEthernetPkts = _AniBsuSuServStatsDSEthernetPkts_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 1, 1, 2),
    _AniBsuSuServStatsDSEthernetPkts_Type()
)
aniBsuSuServStatsDSEthernetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuServStatsDSEthernetPkts.setStatus("current")
_AniBsuSuServStatsDSDropEthernetPkts_Type = Counter32
_AniBsuSuServStatsDSDropEthernetPkts_Object = MibTableColumn
aniBsuSuServStatsDSDropEthernetPkts = _AniBsuSuServStatsDSDropEthernetPkts_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 1, 1, 3),
    _AniBsuSuServStatsDSDropEthernetPkts_Type()
)
aniBsuSuServStatsDSDropEthernetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuServStatsDSDropEthernetPkts.setStatus("current")
_AniBsuSuServStatsDSBytes_Type = Counter32
_AniBsuSuServStatsDSBytes_Object = MibTableColumn
aniBsuSuServStatsDSBytes = _AniBsuSuServStatsDSBytes_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 1, 1, 4),
    _AniBsuSuServStatsDSBytes_Type()
)
aniBsuSuServStatsDSBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuServStatsDSBytes.setStatus("current")
_AniBsuSuServStatsDSWirelessPkts_Type = Counter32
_AniBsuSuServStatsDSWirelessPkts_Object = MibTableColumn
aniBsuSuServStatsDSWirelessPkts = _AniBsuSuServStatsDSWirelessPkts_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 1, 1, 5),
    _AniBsuSuServStatsDSWirelessPkts_Type()
)
aniBsuSuServStatsDSWirelessPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuServStatsDSWirelessPkts.setStatus("current")
_AniBsuSuServStatsDSWirelessPktsRetrans_Type = Counter32
_AniBsuSuServStatsDSWirelessPktsRetrans_Object = MibTableColumn
aniBsuSuServStatsDSWirelessPktsRetrans = _AniBsuSuServStatsDSWirelessPktsRetrans_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 1, 1, 6),
    _AniBsuSuServStatsDSWirelessPktsRetrans_Type()
)
aniBsuSuServStatsDSWirelessPktsRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuServStatsDSWirelessPktsRetrans.setStatus("current")
_AniBsuSuServStatsUSEthernetPkts_Type = Counter32
_AniBsuSuServStatsUSEthernetPkts_Object = MibTableColumn
aniBsuSuServStatsUSEthernetPkts = _AniBsuSuServStatsUSEthernetPkts_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 1, 1, 7),
    _AniBsuSuServStatsUSEthernetPkts_Type()
)
aniBsuSuServStatsUSEthernetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuServStatsUSEthernetPkts.setStatus("current")
_AniBsuSuServStatsUSDropEthernetPkts_Type = Counter32
_AniBsuSuServStatsUSDropEthernetPkts_Object = MibTableColumn
aniBsuSuServStatsUSDropEthernetPkts = _AniBsuSuServStatsUSDropEthernetPkts_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 1, 1, 8),
    _AniBsuSuServStatsUSDropEthernetPkts_Type()
)
aniBsuSuServStatsUSDropEthernetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuServStatsUSDropEthernetPkts.setStatus("current")
_AniBsuSuServStatsUSBytes_Type = Counter32
_AniBsuSuServStatsUSBytes_Object = MibTableColumn
aniBsuSuServStatsUSBytes = _AniBsuSuServStatsUSBytes_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 1, 1, 9),
    _AniBsuSuServStatsUSBytes_Type()
)
aniBsuSuServStatsUSBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuServStatsUSBytes.setStatus("current")
_AniBsuSuServStatsUSWirelessPkts_Type = Counter32
_AniBsuSuServStatsUSWirelessPkts_Object = MibTableColumn
aniBsuSuServStatsUSWirelessPkts = _AniBsuSuServStatsUSWirelessPkts_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 1, 1, 10),
    _AniBsuSuServStatsUSWirelessPkts_Type()
)
aniBsuSuServStatsUSWirelessPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuServStatsUSWirelessPkts.setStatus("current")
_AniBsuSuSignalQualityTable_Object = MibTable
aniBsuSuSignalQualityTable = _AniBsuSuSignalQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 2)
)
if mibBuilder.loadTexts:
    aniBsuSuSignalQualityTable.setStatus("current")
_AniBsuSuSignalQualityEntry_Object = MibTableRow
aniBsuSuSignalQualityEntry = _AniBsuSuSignalQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 2, 1)
)
aniBsuSuSignalQualityEntry.setIndexNames(
    (0, "BSUSUINV-MIB", "aniBsuSuMacAddr"),
    (0, "BSUSUSTATS-MIB", "aniBsuSuServStatsFlowId"),
)
if mibBuilder.loadTexts:
    aniBsuSuSignalQualityEntry.setStatus("current")
_AniBsuSuSigQCollidedBurstsCount_Type = Counter32
_AniBsuSuSigQCollidedBurstsCount_Object = MibTableColumn
aniBsuSuSigQCollidedBurstsCount = _AniBsuSuSigQCollidedBurstsCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 2, 1, 1),
    _AniBsuSuSigQCollidedBurstsCount_Type()
)
aniBsuSuSigQCollidedBurstsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuSigQCollidedBurstsCount.setStatus("current")
_AniBsuSuSigQCorrFecErrorCount_Type = Counter32
_AniBsuSuSigQCorrFecErrorCount_Object = MibTableColumn
aniBsuSuSigQCorrFecErrorCount = _AniBsuSuSigQCorrFecErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 2, 1, 2),
    _AniBsuSuSigQCorrFecErrorCount_Type()
)
aniBsuSuSigQCorrFecErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuSigQCorrFecErrorCount.setStatus("current")
_AniBsuSuSigQUnCorrFecErrorCount_Type = Counter32
_AniBsuSuSigQUnCorrFecErrorCount_Object = MibTableColumn
aniBsuSuSigQUnCorrFecErrorCount = _AniBsuSuSigQUnCorrFecErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 2, 1, 3),
    _AniBsuSuSigQUnCorrFecErrorCount_Type()
)
aniBsuSuSigQUnCorrFecErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuSigQUnCorrFecErrorCount.setStatus("current")
_AniBsuSuSigQNoFecErrorCount_Type = Counter32
_AniBsuSuSigQNoFecErrorCount_Object = MibTableColumn
aniBsuSuSigQNoFecErrorCount = _AniBsuSuSigQNoFecErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 2, 1, 4),
    _AniBsuSuSigQNoFecErrorCount_Type()
)
aniBsuSuSigQNoFecErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuSigQNoFecErrorCount.setStatus("current")
_AniBsuSuSigQNoUniqWordDetectedCount_Type = Counter32
_AniBsuSuSigQNoUniqWordDetectedCount_Object = MibTableColumn
aniBsuSuSigQNoUniqWordDetectedCount = _AniBsuSuSigQNoUniqWordDetectedCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 2, 1, 5),
    _AniBsuSuSigQNoUniqWordDetectedCount_Type()
)
aniBsuSuSigQNoUniqWordDetectedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuSigQNoUniqWordDetectedCount.setStatus("current")
_AniBsuSuSigQNoEnergyDetectedCount_Type = Counter32
_AniBsuSuSigQNoEnergyDetectedCount_Object = MibTableColumn
aniBsuSuSigQNoEnergyDetectedCount = _AniBsuSuSigQNoEnergyDetectedCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 4, 2, 1, 6),
    _AniBsuSuSigQNoEnergyDetectedCount_Type()
)
aniBsuSuSigQNoEnergyDetectedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuSigQNoEnergyDetectedCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSUSUSTATS-MIB",
    **{"aniBsuSuStatistics": aniBsuSuStatistics,
       "aniBsuSuServStatsTable": aniBsuSuServStatsTable,
       "aniBsuSuServStatsEntry": aniBsuSuServStatsEntry,
       "aniBsuSuServStatsFlowId": aniBsuSuServStatsFlowId,
       "aniBsuSuServStatsDSEthernetPkts": aniBsuSuServStatsDSEthernetPkts,
       "aniBsuSuServStatsDSDropEthernetPkts": aniBsuSuServStatsDSDropEthernetPkts,
       "aniBsuSuServStatsDSBytes": aniBsuSuServStatsDSBytes,
       "aniBsuSuServStatsDSWirelessPkts": aniBsuSuServStatsDSWirelessPkts,
       "aniBsuSuServStatsDSWirelessPktsRetrans": aniBsuSuServStatsDSWirelessPktsRetrans,
       "aniBsuSuServStatsUSEthernetPkts": aniBsuSuServStatsUSEthernetPkts,
       "aniBsuSuServStatsUSDropEthernetPkts": aniBsuSuServStatsUSDropEthernetPkts,
       "aniBsuSuServStatsUSBytes": aniBsuSuServStatsUSBytes,
       "aniBsuSuServStatsUSWirelessPkts": aniBsuSuServStatsUSWirelessPkts,
       "aniBsuSuSignalQualityTable": aniBsuSuSignalQualityTable,
       "aniBsuSuSignalQualityEntry": aniBsuSuSignalQualityEntry,
       "aniBsuSuSigQCollidedBurstsCount": aniBsuSuSigQCollidedBurstsCount,
       "aniBsuSuSigQCorrFecErrorCount": aniBsuSuSigQCorrFecErrorCount,
       "aniBsuSuSigQUnCorrFecErrorCount": aniBsuSuSigQUnCorrFecErrorCount,
       "aniBsuSuSigQNoFecErrorCount": aniBsuSuSigQNoFecErrorCount,
       "aniBsuSuSigQNoUniqWordDetectedCount": aniBsuSuSigQNoUniqWordDetectedCount,
       "aniBsuSuSigQNoEnergyDetectedCount": aniBsuSuSigQNoEnergyDetectedCount}
)
