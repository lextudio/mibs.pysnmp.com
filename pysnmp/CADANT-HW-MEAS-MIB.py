# SNMP MIB module (CADANT-HW-MEAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-HW-MEAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:59 2024
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

(cadIf3CmtsCmUsStatusChIfIndex,) = mibBuilder.importSymbols(
    "CADANT-CMTS-IF3-MIB",
    "cadIf3CmtsCmUsStatusChIfIndex")

(cadIfMacDomainIfIndex,) = mibBuilder.importSymbols(
    "CADANT-CMTS-LAYER2CMTS-MIB",
    "cadIfMacDomainIfIndex")

(cadIfCmtsCmStatusMacAddress,) = mibBuilder.importSymbols(
    "CADANT-CMTS-MAC-MIB",
    "cadIfCmtsCmStatusMacAddress")

(cadEquipment,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadEquipment")

(CadIfDirection,
 CardId,
 PortId) = mibBuilder.importSymbols(
    "CADANT-TC",
    "CadIfDirection",
    "CardId",
    "PortId")

(TenthdB,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB")

(IfDirection,) = mibBuilder.importSymbols(
    "DOCS-QOS3-MIB",
    "IfDirection")

(docsSubmgt3FilterGrpEntry,) = mibBuilder.importSymbols(
    "DOCS-SUBMGT3-MIB",
    "docsSubmgt3FilterGrpEntry")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(pktcEScTapMediationContentId,
 pktcEScTapStreamIndex) = mibBuilder.importSymbols(
    "PKTC-ES-TAP-MIB",
    "pktcEScTapMediationContentId",
    "pktcEScTapStreamIndex")

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
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cadHardwareMeasMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2)
)
cadHardwareMeasMib.setRevisions(
        ("2015-08-27 00:00",
         "2015-07-13 00:00",
         "2015-06-03 00:00",
         "2014-10-14 00:00",
         "2014-06-13 00:00",
         "2014-06-04 00:00",
         "2013-11-22 00:00",
         "2012-10-30 00:00",
         "2012-05-09 00:00",
         "2011-08-31 00:00",
         "2011-06-29 00:00",
         "2011-02-28 00:00",
         "2011-02-24 00:00",
         "2011-02-18 00:00",
         "2010-11-22 00:00",
         "2010-03-09 00:00",
         "2008-11-24 00:00",
         "2008-11-21 00:00",
         "2008-11-05 00:00",
         "2008-04-24 00:00",
         "2006-09-14 00:00",
         "2006-04-14 00:00",
         "2005-07-13 00:00",
         "2004-12-10 00:00",
         "2004-08-31 00:00",
         "2004-04-09 00:00",
         "2004-03-09 00:00",
         "2004-02-23 00:00",
         "2004-02-18 00:00",
         "2004-02-15 00:00",
         "2004-01-24 00:00",
         "2003-12-18 00:00",
         "2003-12-10 00:00",
         "2003-09-19 00:00",
         "2003-08-26 00:00",
         "2003-07-30 00:00",
         "2002-05-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DFIDIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class PktClassId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class SFIDIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class UFIDIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )



class SIDValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )



class TMSide(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tma", 1),
          ("tmb", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CadantHWMeasGeneral_ObjectIdentity = ObjectIdentity
cadantHWMeasGeneral = _CadantHWMeasGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 1)
)
_CadantFabActualDepth_Type = Integer32
_CadantFabActualDepth_Object = MibScalar
cadantFabActualDepth = _CadantFabActualDepth_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 1, 1),
    _CadantFabActualDepth_Type()
)
cadantFabActualDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantFabActualDepth.setStatus("current")
_CadantFabAvgDepth_Type = Integer32
_CadantFabAvgDepth_Object = MibScalar
cadantFabAvgDepth = _CadantFabAvgDepth_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 1, 2),
    _CadantFabAvgDepth_Type()
)
cadantFabAvgDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantFabAvgDepth.setStatus("current")
_CadantUPortMeasTable_Object = MibTable
cadantUPortMeasTable = _CadantUPortMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3)
)
if mibBuilder.loadTexts:
    cadantUPortMeasTable.setStatus("current")
_CadantUPortMeasEntry_Object = MibTableRow
cadantUPortMeasEntry = _CadantUPortMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1)
)
cadantUPortMeasEntry.setIndexNames(
    (0, "CADANT-HW-MEAS-MIB", "cadantUPortMeasCardId"),
    (0, "CADANT-HW-MEAS-MIB", "cadantUPortMeasPortId"),
)
if mibBuilder.loadTexts:
    cadantUPortMeasEntry.setStatus("current")
_CadantUPortMeasCardId_Type = CardId
_CadantUPortMeasCardId_Object = MibTableColumn
cadantUPortMeasCardId = _CadantUPortMeasCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 1),
    _CadantUPortMeasCardId_Type()
)
cadantUPortMeasCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadantUPortMeasCardId.setStatus("current")
_CadantUPortMeasPortId_Type = PortId
_CadantUPortMeasPortId_Object = MibTableColumn
cadantUPortMeasPortId = _CadantUPortMeasPortId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 2),
    _CadantUPortMeasPortId_Type()
)
cadantUPortMeasPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadantUPortMeasPortId.setStatus("current")
_CadantUPortMeasUcastFrms_Type = Counter64
_CadantUPortMeasUcastFrms_Object = MibTableColumn
cadantUPortMeasUcastFrms = _CadantUPortMeasUcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 3),
    _CadantUPortMeasUcastFrms_Type()
)
cadantUPortMeasUcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasUcastFrms.setStatus("current")
_CadantUPortMeasMcastFrms_Type = Counter64
_CadantUPortMeasMcastFrms_Object = MibTableColumn
cadantUPortMeasMcastFrms = _CadantUPortMeasMcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 4),
    _CadantUPortMeasMcastFrms_Type()
)
cadantUPortMeasMcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasMcastFrms.setStatus("current")
_CadantUPortMeasBcastFrms_Type = Counter64
_CadantUPortMeasBcastFrms_Object = MibTableColumn
cadantUPortMeasBcastFrms = _CadantUPortMeasBcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 5),
    _CadantUPortMeasBcastFrms_Type()
)
cadantUPortMeasBcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasBcastFrms.setStatus("current")
_CadantUPortMeasUcastDataFrms_Type = Counter64
_CadantUPortMeasUcastDataFrms_Object = MibTableColumn
cadantUPortMeasUcastDataFrms = _CadantUPortMeasUcastDataFrms_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 6),
    _CadantUPortMeasUcastDataFrms_Type()
)
cadantUPortMeasUcastDataFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasUcastDataFrms.setStatus("current")
_CadantUPortMeasMcastDataFrms_Type = Counter64
_CadantUPortMeasMcastDataFrms_Object = MibTableColumn
cadantUPortMeasMcastDataFrms = _CadantUPortMeasMcastDataFrms_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 7),
    _CadantUPortMeasMcastDataFrms_Type()
)
cadantUPortMeasMcastDataFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasMcastDataFrms.setStatus("current")
_CadantUPortMeasBcastDataFrms_Type = Counter64
_CadantUPortMeasBcastDataFrms_Object = MibTableColumn
cadantUPortMeasBcastDataFrms = _CadantUPortMeasBcastDataFrms_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 8),
    _CadantUPortMeasBcastDataFrms_Type()
)
cadantUPortMeasBcastDataFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasBcastDataFrms.setStatus("current")
_CadantUPortMeasDiscardFrms_Type = Counter64
_CadantUPortMeasDiscardFrms_Object = MibTableColumn
cadantUPortMeasDiscardFrms = _CadantUPortMeasDiscardFrms_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 9),
    _CadantUPortMeasDiscardFrms_Type()
)
cadantUPortMeasDiscardFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasDiscardFrms.setStatus("current")
_CadantUPortMeasIfInOctets_Type = Counter64
_CadantUPortMeasIfInOctets_Object = MibTableColumn
cadantUPortMeasIfInOctets = _CadantUPortMeasIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 10),
    _CadantUPortMeasIfInOctets_Type()
)
cadantUPortMeasIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasIfInOctets.setStatus("current")
_CadantUPortMeasIfInDataOctets_Type = Counter64
_CadantUPortMeasIfInDataOctets_Object = MibTableColumn
cadantUPortMeasIfInDataOctets = _CadantUPortMeasIfInDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 11),
    _CadantUPortMeasIfInDataOctets_Type()
)
cadantUPortMeasIfInDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasIfInDataOctets.setStatus("current")
_CadantUPortMeasIfInUnknownProtos_Type = Counter64
_CadantUPortMeasIfInUnknownProtos_Object = MibTableColumn
cadantUPortMeasIfInUnknownProtos = _CadantUPortMeasIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 12),
    _CadantUPortMeasIfInUnknownProtos_Type()
)
cadantUPortMeasIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasIfInUnknownProtos.setStatus("current")
_CadantUPortMeasAppMinusBWReqFrms_Type = Counter64
_CadantUPortMeasAppMinusBWReqFrms_Object = MibTableColumn
cadantUPortMeasAppMinusBWReqFrms = _CadantUPortMeasAppMinusBWReqFrms_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 13),
    _CadantUPortMeasAppMinusBWReqFrms_Type()
)
cadantUPortMeasAppMinusBWReqFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasAppMinusBWReqFrms.setStatus("current")
_CadantUPortMeasErroredFrms_Type = Counter64
_CadantUPortMeasErroredFrms_Object = MibTableColumn
cadantUPortMeasErroredFrms = _CadantUPortMeasErroredFrms_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 15),
    _CadantUPortMeasErroredFrms_Type()
)
cadantUPortMeasErroredFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasErroredFrms.setStatus("current")
_CadantUPortMeasFilteredFrms_Type = Counter64
_CadantUPortMeasFilteredFrms_Object = MibTableColumn
cadantUPortMeasFilteredFrms = _CadantUPortMeasFilteredFrms_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 16),
    _CadantUPortMeasFilteredFrms_Type()
)
cadantUPortMeasFilteredFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasFilteredFrms.setStatus("current")
_CadantUPortMeasBcastReqOpps_Type = Counter64
_CadantUPortMeasBcastReqOpps_Object = MibTableColumn
cadantUPortMeasBcastReqOpps = _CadantUPortMeasBcastReqOpps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 17),
    _CadantUPortMeasBcastReqOpps_Type()
)
cadantUPortMeasBcastReqOpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasBcastReqOpps.setStatus("current")
_CadantUPortMeasBcastReqColls_Type = Counter64
_CadantUPortMeasBcastReqColls_Object = MibTableColumn
cadantUPortMeasBcastReqColls = _CadantUPortMeasBcastReqColls_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 18),
    _CadantUPortMeasBcastReqColls_Type()
)
cadantUPortMeasBcastReqColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasBcastReqColls.setStatus("current")
_CadantUPortMeasBcastReqNoEnergies_Type = Counter64
_CadantUPortMeasBcastReqNoEnergies_Object = MibTableColumn
cadantUPortMeasBcastReqNoEnergies = _CadantUPortMeasBcastReqNoEnergies_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 19),
    _CadantUPortMeasBcastReqNoEnergies_Type()
)
cadantUPortMeasBcastReqNoEnergies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasBcastReqNoEnergies.setStatus("current")
_CadantUPortMeasBcastReqRxPwr1s_Type = Counter64
_CadantUPortMeasBcastReqRxPwr1s_Object = MibTableColumn
cadantUPortMeasBcastReqRxPwr1s = _CadantUPortMeasBcastReqRxPwr1s_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 20),
    _CadantUPortMeasBcastReqRxPwr1s_Type()
)
cadantUPortMeasBcastReqRxPwr1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasBcastReqRxPwr1s.setStatus("current")
_CadantUPortMeasBcastReqRxPwr2s_Type = Counter64
_CadantUPortMeasBcastReqRxPwr2s_Object = MibTableColumn
cadantUPortMeasBcastReqRxPwr2s = _CadantUPortMeasBcastReqRxPwr2s_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 21),
    _CadantUPortMeasBcastReqRxPwr2s_Type()
)
cadantUPortMeasBcastReqRxPwr2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasBcastReqRxPwr2s.setStatus("current")
_CadantUPortMeasInitMaintOpps_Type = Counter64
_CadantUPortMeasInitMaintOpps_Object = MibTableColumn
cadantUPortMeasInitMaintOpps = _CadantUPortMeasInitMaintOpps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 22),
    _CadantUPortMeasInitMaintOpps_Type()
)
cadantUPortMeasInitMaintOpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasInitMaintOpps.setStatus("current")
_CadantUPortMeasInitMaintColls_Type = Counter64
_CadantUPortMeasInitMaintColls_Object = MibTableColumn
cadantUPortMeasInitMaintColls = _CadantUPortMeasInitMaintColls_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 23),
    _CadantUPortMeasInitMaintColls_Type()
)
cadantUPortMeasInitMaintColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasInitMaintColls.setStatus("current")
_CadantUPortMeasInitMaintNoEnergies_Type = Counter64
_CadantUPortMeasInitMaintNoEnergies_Object = MibTableColumn
cadantUPortMeasInitMaintNoEnergies = _CadantUPortMeasInitMaintNoEnergies_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 24),
    _CadantUPortMeasInitMaintNoEnergies_Type()
)
cadantUPortMeasInitMaintNoEnergies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasInitMaintNoEnergies.setStatus("current")
_CadantUPortMeasInitMaintRxPwr1s_Type = Counter64
_CadantUPortMeasInitMaintRxPwr1s_Object = MibTableColumn
cadantUPortMeasInitMaintRxPwr1s = _CadantUPortMeasInitMaintRxPwr1s_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 25),
    _CadantUPortMeasInitMaintRxPwr1s_Type()
)
cadantUPortMeasInitMaintRxPwr1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasInitMaintRxPwr1s.setStatus("current")
_CadantUPortMeasInitMaintRxPwr2s_Type = Counter64
_CadantUPortMeasInitMaintRxPwr2s_Object = MibTableColumn
cadantUPortMeasInitMaintRxPwr2s = _CadantUPortMeasInitMaintRxPwr2s_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 3, 1, 26),
    _CadantUPortMeasInitMaintRxPwr2s_Type()
)
cadantUPortMeasInitMaintRxPwr2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUPortMeasInitMaintRxPwr2s.setStatus("current")
_CadantDPortMeasTable_Object = MibTable
cadantDPortMeasTable = _CadantDPortMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4)
)
if mibBuilder.loadTexts:
    cadantDPortMeasTable.setStatus("current")
_CadantDPortMeasEntry_Object = MibTableRow
cadantDPortMeasEntry = _CadantDPortMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1)
)
cadantDPortMeasEntry.setIndexNames(
    (0, "CADANT-HW-MEAS-MIB", "cadantDPortMeasCardId"),
    (0, "CADANT-HW-MEAS-MIB", "cadantDPortMeasPortId"),
)
if mibBuilder.loadTexts:
    cadantDPortMeasEntry.setStatus("current")
_CadantDPortMeasCardId_Type = CardId
_CadantDPortMeasCardId_Object = MibTableColumn
cadantDPortMeasCardId = _CadantDPortMeasCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 1),
    _CadantDPortMeasCardId_Type()
)
cadantDPortMeasCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadantDPortMeasCardId.setStatus("current")
_CadantDPortMeasPortId_Type = PortId
_CadantDPortMeasPortId_Object = MibTableColumn
cadantDPortMeasPortId = _CadantDPortMeasPortId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 2),
    _CadantDPortMeasPortId_Type()
)
cadantDPortMeasPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadantDPortMeasPortId.setStatus("current")
_CadantDPortMeasIfOutOctets_Type = Counter64
_CadantDPortMeasIfOutOctets_Object = MibTableColumn
cadantDPortMeasIfOutOctets = _CadantDPortMeasIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 3),
    _CadantDPortMeasIfOutOctets_Type()
)
cadantDPortMeasIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasIfOutOctets.setStatus("current")
_CadantDPortMeasIfOutUcastPkts_Type = Counter64
_CadantDPortMeasIfOutUcastPkts_Object = MibTableColumn
cadantDPortMeasIfOutUcastPkts = _CadantDPortMeasIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 4),
    _CadantDPortMeasIfOutUcastPkts_Type()
)
cadantDPortMeasIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasIfOutUcastPkts.setStatus("current")
_CadantDPortMeasIfOutMcastPkts_Type = Counter64
_CadantDPortMeasIfOutMcastPkts_Object = MibTableColumn
cadantDPortMeasIfOutMcastPkts = _CadantDPortMeasIfOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 5),
    _CadantDPortMeasIfOutMcastPkts_Type()
)
cadantDPortMeasIfOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasIfOutMcastPkts.setStatus("current")
_CadantDPortMeasIfOutBcastPkts_Type = Counter64
_CadantDPortMeasIfOutBcastPkts_Object = MibTableColumn
cadantDPortMeasIfOutBcastPkts = _CadantDPortMeasIfOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 6),
    _CadantDPortMeasIfOutBcastPkts_Type()
)
cadantDPortMeasIfOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasIfOutBcastPkts.setStatus("current")
_CadantDPortMeasIfOutDataOctets_Type = Counter64
_CadantDPortMeasIfOutDataOctets_Object = MibTableColumn
cadantDPortMeasIfOutDataOctets = _CadantDPortMeasIfOutDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 7),
    _CadantDPortMeasIfOutDataOctets_Type()
)
cadantDPortMeasIfOutDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasIfOutDataOctets.setStatus("current")
_CadantDPortMeasIfOutUcastDataPkts_Type = Counter64
_CadantDPortMeasIfOutUcastDataPkts_Object = MibTableColumn
cadantDPortMeasIfOutUcastDataPkts = _CadantDPortMeasIfOutUcastDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 8),
    _CadantDPortMeasIfOutUcastDataPkts_Type()
)
cadantDPortMeasIfOutUcastDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasIfOutUcastDataPkts.setStatus("current")
_CadantDPortMeasIfOutMcastDataPkts_Type = Counter64
_CadantDPortMeasIfOutMcastDataPkts_Object = MibTableColumn
cadantDPortMeasIfOutMcastDataPkts = _CadantDPortMeasIfOutMcastDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 9),
    _CadantDPortMeasIfOutMcastDataPkts_Type()
)
cadantDPortMeasIfOutMcastDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasIfOutMcastDataPkts.setStatus("current")
_CadantDPortMeasIfOutBcastDataPkts_Type = Counter64
_CadantDPortMeasIfOutBcastDataPkts_Object = MibTableColumn
cadantDPortMeasIfOutBcastDataPkts = _CadantDPortMeasIfOutBcastDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 10),
    _CadantDPortMeasIfOutBcastDataPkts_Type()
)
cadantDPortMeasIfOutBcastDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasIfOutBcastDataPkts.setStatus("current")
_CadantDPortMeasGotNoDMACs_Type = Counter64
_CadantDPortMeasGotNoDMACs_Object = MibTableColumn
cadantDPortMeasGotNoDMACs = _CadantDPortMeasGotNoDMACs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 11),
    _CadantDPortMeasGotNoDMACs_Type()
)
cadantDPortMeasGotNoDMACs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasGotNoDMACs.setStatus("current")
_CadantDPortMeasGotNoClasses_Type = Counter64
_CadantDPortMeasGotNoClasses_Object = MibTableColumn
cadantDPortMeasGotNoClasses = _CadantDPortMeasGotNoClasses_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 12),
    _CadantDPortMeasGotNoClasses_Type()
)
cadantDPortMeasGotNoClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasGotNoClasses.setStatus("current")
_CadantDPortMeasSyncPkts_Type = Counter64
_CadantDPortMeasSyncPkts_Object = MibTableColumn
cadantDPortMeasSyncPkts = _CadantDPortMeasSyncPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 13),
    _CadantDPortMeasSyncPkts_Type()
)
cadantDPortMeasSyncPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasSyncPkts.setStatus("current")
_CadantDPortMeasAppUcastPkts_Type = Counter64
_CadantDPortMeasAppUcastPkts_Object = MibTableColumn
cadantDPortMeasAppUcastPkts = _CadantDPortMeasAppUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 14),
    _CadantDPortMeasAppUcastPkts_Type()
)
cadantDPortMeasAppUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasAppUcastPkts.setStatus("current")
_CadantDPortMeasAppMcastPkts_Type = Counter64
_CadantDPortMeasAppMcastPkts_Object = MibTableColumn
cadantDPortMeasAppMcastPkts = _CadantDPortMeasAppMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 15),
    _CadantDPortMeasAppMcastPkts_Type()
)
cadantDPortMeasAppMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasAppMcastPkts.setStatus("current")
_CadantDPortMeasIfOutTotalOctets_Type = Counter64
_CadantDPortMeasIfOutTotalOctets_Object = MibTableColumn
cadantDPortMeasIfOutTotalOctets = _CadantDPortMeasIfOutTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 16),
    _CadantDPortMeasIfOutTotalOctets_Type()
)
cadantDPortMeasIfOutTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasIfOutTotalOctets.setStatus("current")
_CadantDPortMeasOfdmIfSpeed_Type = Gauge32
_CadantDPortMeasOfdmIfSpeed_Object = MibTableColumn
cadantDPortMeasOfdmIfSpeed = _CadantDPortMeasOfdmIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 17),
    _CadantDPortMeasOfdmIfSpeed_Type()
)
cadantDPortMeasOfdmIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasOfdmIfSpeed.setStatus("current")
_CadantDPortMeasOfdmHighestAvgBitsPerSubc_Type = Unsigned32
_CadantDPortMeasOfdmHighestAvgBitsPerSubc_Object = MibTableColumn
cadantDPortMeasOfdmHighestAvgBitsPerSubc = _CadantDPortMeasOfdmHighestAvgBitsPerSubc_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 18),
    _CadantDPortMeasOfdmHighestAvgBitsPerSubc_Type()
)
cadantDPortMeasOfdmHighestAvgBitsPerSubc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasOfdmHighestAvgBitsPerSubc.setStatus("current")
_CadantDPortMeasOfdmNumDataSubc_Type = Unsigned32
_CadantDPortMeasOfdmNumDataSubc_Object = MibTableColumn
cadantDPortMeasOfdmNumDataSubc = _CadantDPortMeasOfdmNumDataSubc_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 19),
    _CadantDPortMeasOfdmNumDataSubc_Type()
)
cadantDPortMeasOfdmNumDataSubc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasOfdmNumDataSubc.setStatus("current")


class _CadantDPortMeasOfdmChanUtilization_Type(Integer32):
    """Custom type cadantDPortMeasOfdmChanUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadantDPortMeasOfdmChanUtilization_Type.__name__ = "Integer32"
_CadantDPortMeasOfdmChanUtilization_Object = MibTableColumn
cadantDPortMeasOfdmChanUtilization = _CadantDPortMeasOfdmChanUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 4, 1, 20),
    _CadantDPortMeasOfdmChanUtilization_Type()
)
cadantDPortMeasOfdmChanUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantDPortMeasOfdmChanUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cadantDPortMeasOfdmChanUtilization.setUnits("percent")
_CadantUFIDMeasTable_Object = MibTable
cadantUFIDMeasTable = _CadantUFIDMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6)
)
if mibBuilder.loadTexts:
    cadantUFIDMeasTable.setStatus("current")
_CadantUFIDMeasEntry_Object = MibTableRow
cadantUFIDMeasEntry = _CadantUFIDMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1)
)
cadantUFIDMeasEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CADANT-HW-MEAS-MIB", "cadantUFIDMeasSID"),
)
if mibBuilder.loadTexts:
    cadantUFIDMeasEntry.setStatus("current")
_CadantUFIDMeasSID_Type = SIDValue
_CadantUFIDMeasSID_Object = MibTableColumn
cadantUFIDMeasSID = _CadantUFIDMeasSID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 3),
    _CadantUFIDMeasSID_Type()
)
cadantUFIDMeasSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadantUFIDMeasSID.setStatus("current")
_CadantUFIDMeasPktsSGreedyDrop_Type = Counter64
_CadantUFIDMeasPktsSGreedyDrop_Object = MibTableColumn
cadantUFIDMeasPktsSGreedyDrop = _CadantUFIDMeasPktsSGreedyDrop_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 4),
    _CadantUFIDMeasPktsSGreedyDrop_Type()
)
cadantUFIDMeasPktsSGreedyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasPktsSGreedyDrop.setStatus("current")
_CadantUFIDMeasBytsOtherDrop_Type = Counter64
_CadantUFIDMeasBytsOtherDrop_Object = MibTableColumn
cadantUFIDMeasBytsOtherDrop = _CadantUFIDMeasBytsOtherDrop_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 5),
    _CadantUFIDMeasBytsOtherDrop_Type()
)
cadantUFIDMeasBytsOtherDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasBytsOtherDrop.setStatus("current")
_CadantUFIDMeasBytsArrived_Type = Counter64
_CadantUFIDMeasBytsArrived_Object = MibTableColumn
cadantUFIDMeasBytsArrived = _CadantUFIDMeasBytsArrived_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 6),
    _CadantUFIDMeasBytsArrived_Type()
)
cadantUFIDMeasBytsArrived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasBytsArrived.setStatus("current")
_CadantUFIDMeasPktsArrived_Type = Counter64
_CadantUFIDMeasPktsArrived_Object = MibTableColumn
cadantUFIDMeasPktsArrived = _CadantUFIDMeasPktsArrived_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 7),
    _CadantUFIDMeasPktsArrived_Type()
)
cadantUFIDMeasPktsArrived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasPktsArrived.setStatus("current")
_CadantUFIDMeasSIDCorrecteds_Type = Counter64
_CadantUFIDMeasSIDCorrecteds_Object = MibTableColumn
cadantUFIDMeasSIDCorrecteds = _CadantUFIDMeasSIDCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 8),
    _CadantUFIDMeasSIDCorrecteds_Type()
)
cadantUFIDMeasSIDCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDCorrecteds.setStatus("current")
_CadantUFIDMeasSIDUnerroreds_Type = Counter64
_CadantUFIDMeasSIDUnerroreds_Object = MibTableColumn
cadantUFIDMeasSIDUnerroreds = _CadantUFIDMeasSIDUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 9),
    _CadantUFIDMeasSIDUnerroreds_Type()
)
cadantUFIDMeasSIDUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDUnerroreds.setStatus("current")
_CadantUFIDMeasSIDUnCorrecteds_Type = Counter64
_CadantUFIDMeasSIDUnCorrecteds_Object = MibTableColumn
cadantUFIDMeasSIDUnCorrecteds = _CadantUFIDMeasSIDUnCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 10),
    _CadantUFIDMeasSIDUnCorrecteds_Type()
)
cadantUFIDMeasSIDUnCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDUnCorrecteds.setStatus("current")
_CadantUFIDMeasSIDNoUniqueWordDetecteds_Type = Counter64
_CadantUFIDMeasSIDNoUniqueWordDetecteds_Object = MibTableColumn
cadantUFIDMeasSIDNoUniqueWordDetecteds = _CadantUFIDMeasSIDNoUniqueWordDetecteds_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 11),
    _CadantUFIDMeasSIDNoUniqueWordDetecteds_Type()
)
cadantUFIDMeasSIDNoUniqueWordDetecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDNoUniqueWordDetecteds.setStatus("current")
_CadantUFIDMeasSIDCollidedBursts_Type = Counter64
_CadantUFIDMeasSIDCollidedBursts_Object = MibTableColumn
cadantUFIDMeasSIDCollidedBursts = _CadantUFIDMeasSIDCollidedBursts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 12),
    _CadantUFIDMeasSIDCollidedBursts_Type()
)
cadantUFIDMeasSIDCollidedBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDCollidedBursts.setStatus("current")
_CadantUFIDMeasSIDNoEnergyDetecteds_Type = Counter64
_CadantUFIDMeasSIDNoEnergyDetecteds_Object = MibTableColumn
cadantUFIDMeasSIDNoEnergyDetecteds = _CadantUFIDMeasSIDNoEnergyDetecteds_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 13),
    _CadantUFIDMeasSIDNoEnergyDetecteds_Type()
)
cadantUFIDMeasSIDNoEnergyDetecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDNoEnergyDetecteds.setStatus("current")
_CadantUFIDMeasSIDLengthErrors_Type = Counter64
_CadantUFIDMeasSIDLengthErrors_Object = MibTableColumn
cadantUFIDMeasSIDLengthErrors = _CadantUFIDMeasSIDLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 14),
    _CadantUFIDMeasSIDLengthErrors_Type()
)
cadantUFIDMeasSIDLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDLengthErrors.setStatus("current")
_CadantUFIDMeasSIDMACErrors_Type = Counter64
_CadantUFIDMeasSIDMACErrors_Object = MibTableColumn
cadantUFIDMeasSIDMACErrors = _CadantUFIDMeasSIDMACErrors_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 15),
    _CadantUFIDMeasSIDMACErrors_Type()
)
cadantUFIDMeasSIDMACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDMACErrors.setStatus("current")
_CadantUFIDMeasMacAddress_Type = MacAddress
_CadantUFIDMeasMacAddress_Object = MibTableColumn
cadantUFIDMeasMacAddress = _CadantUFIDMeasMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 17),
    _CadantUFIDMeasMacAddress_Type()
)
cadantUFIDMeasMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasMacAddress.setStatus("current")
_CadantUFIDMeasSCN_Type = DisplayString
_CadantUFIDMeasSCN_Object = MibTableColumn
cadantUFIDMeasSCN = _CadantUFIDMeasSCN_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 18),
    _CadantUFIDMeasSCN_Type()
)
cadantUFIDMeasSCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSCN.setStatus("current")
_CadantUFIDMeasSFID_Type = SFIDIndex
_CadantUFIDMeasSFID_Object = MibTableColumn
cadantUFIDMeasSFID = _CadantUFIDMeasSFID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 19),
    _CadantUFIDMeasSFID_Type()
)
cadantUFIDMeasSFID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSFID.setStatus("current")
_CadantUFIDMeasPHSUnknowns_Type = Counter64
_CadantUFIDMeasPHSUnknowns_Object = MibTableColumn
cadantUFIDMeasPHSUnknowns = _CadantUFIDMeasPHSUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 20),
    _CadantUFIDMeasPHSUnknowns_Type()
)
cadantUFIDMeasPHSUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasPHSUnknowns.setStatus("current")
_CadantUFIDMeasFragPkts_Type = Counter64
_CadantUFIDMeasFragPkts_Object = MibTableColumn
cadantUFIDMeasFragPkts = _CadantUFIDMeasFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 21),
    _CadantUFIDMeasFragPkts_Type()
)
cadantUFIDMeasFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasFragPkts.setStatus("current")
_CadantUFIDMeasIncompletePkts_Type = Counter64
_CadantUFIDMeasIncompletePkts_Object = MibTableColumn
cadantUFIDMeasIncompletePkts = _CadantUFIDMeasIncompletePkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 22),
    _CadantUFIDMeasIncompletePkts_Type()
)
cadantUFIDMeasIncompletePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasIncompletePkts.setStatus("current")
_CadantUFIDMeasConcatBursts_Type = Counter64
_CadantUFIDMeasConcatBursts_Object = MibTableColumn
cadantUFIDMeasConcatBursts = _CadantUFIDMeasConcatBursts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 23),
    _CadantUFIDMeasConcatBursts_Type()
)
cadantUFIDMeasConcatBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasConcatBursts.setStatus("current")
_CadantUFIDMeasSIDSignalNoise_Type = TenthdB
_CadantUFIDMeasSIDSignalNoise_Object = MibTableColumn
cadantUFIDMeasSIDSignalNoise = _CadantUFIDMeasSIDSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 24),
    _CadantUFIDMeasSIDSignalNoise_Type()
)
cadantUFIDMeasSIDSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDSignalNoise.setStatus("current")
_CadantUFIDMeasSIDMicroreflections_Type = Integer32
_CadantUFIDMeasSIDMicroreflections_Object = MibTableColumn
cadantUFIDMeasSIDMicroreflections = _CadantUFIDMeasSIDMicroreflections_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 25),
    _CadantUFIDMeasSIDMicroreflections_Type()
)
cadantUFIDMeasSIDMicroreflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDMicroreflections.setStatus("current")
_CadantUFIDMeasSIDHCSErrors_Type = Counter64
_CadantUFIDMeasSIDHCSErrors_Object = MibTableColumn
cadantUFIDMeasSIDHCSErrors = _CadantUFIDMeasSIDHCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 26),
    _CadantUFIDMeasSIDHCSErrors_Type()
)
cadantUFIDMeasSIDHCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDHCSErrors.setStatus("current")
_CadantUFIDMeasSIDCRCErrors_Type = Counter64
_CadantUFIDMeasSIDCRCErrors_Object = MibTableColumn
cadantUFIDMeasSIDCRCErrors = _CadantUFIDMeasSIDCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 27),
    _CadantUFIDMeasSIDCRCErrors_Type()
)
cadantUFIDMeasSIDCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDCRCErrors.setStatus("current")
_CadantUFIDMeasUFIDIndex_Type = UFIDIndex
_CadantUFIDMeasUFIDIndex_Object = MibTableColumn
cadantUFIDMeasUFIDIndex = _CadantUFIDMeasUFIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 28),
    _CadantUFIDMeasUFIDIndex_Type()
)
cadantUFIDMeasUFIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasUFIDIndex.setStatus("current")
_CadantUFIDMeasGateID_Type = Unsigned32
_CadantUFIDMeasGateID_Object = MibTableColumn
cadantUFIDMeasGateID = _CadantUFIDMeasGateID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 29),
    _CadantUFIDMeasGateID_Type()
)
cadantUFIDMeasGateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasGateID.setStatus("current")
_CadantUFIDMeasSIDMacIfIndex_Type = InterfaceIndex
_CadantUFIDMeasSIDMacIfIndex_Object = MibTableColumn
cadantUFIDMeasSIDMacIfIndex = _CadantUFIDMeasSIDMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 30),
    _CadantUFIDMeasSIDMacIfIndex_Type()
)
cadantUFIDMeasSIDMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDMacIfIndex.setStatus("current")
_CadantUFIDMeasSIDBonded_Type = TruthValue
_CadantUFIDMeasSIDBonded_Object = MibTableColumn
cadantUFIDMeasSIDBonded = _CadantUFIDMeasSIDBonded_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 31),
    _CadantUFIDMeasSIDBonded_Type()
)
cadantUFIDMeasSIDBonded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasSIDBonded.setStatus("current")
_CadantUFIDMeasCcfStatsSgmtValids_Type = Counter32
_CadantUFIDMeasCcfStatsSgmtValids_Object = MibTableColumn
cadantUFIDMeasCcfStatsSgmtValids = _CadantUFIDMeasCcfStatsSgmtValids_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 32),
    _CadantUFIDMeasCcfStatsSgmtValids_Type()
)
cadantUFIDMeasCcfStatsSgmtValids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasCcfStatsSgmtValids.setStatus("current")
if mibBuilder.loadTexts:
    cadantUFIDMeasCcfStatsSgmtValids.setUnits("segments")
_CadantUFIDMeasCcfStatsSgmtLost_Type = Counter32
_CadantUFIDMeasCcfStatsSgmtLost_Object = MibTableColumn
cadantUFIDMeasCcfStatsSgmtLost = _CadantUFIDMeasCcfStatsSgmtLost_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 33),
    _CadantUFIDMeasCcfStatsSgmtLost_Type()
)
cadantUFIDMeasCcfStatsSgmtLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasCcfStatsSgmtLost.setStatus("current")
if mibBuilder.loadTexts:
    cadantUFIDMeasCcfStatsSgmtLost.setUnits("segments")
_CadantUFIDMeasCcfStatsSgmtDrop_Type = Counter32
_CadantUFIDMeasCcfStatsSgmtDrop_Object = MibTableColumn
cadantUFIDMeasCcfStatsSgmtDrop = _CadantUFIDMeasCcfStatsSgmtDrop_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 6, 1, 34),
    _CadantUFIDMeasCcfStatsSgmtDrop_Type()
)
cadantUFIDMeasCcfStatsSgmtDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantUFIDMeasCcfStatsSgmtDrop.setStatus("current")
if mibBuilder.loadTexts:
    cadantUFIDMeasCcfStatsSgmtDrop.setUnits("segments")
_CadantEtherPhyMeasTable_Object = MibTable
cadantEtherPhyMeasTable = _CadantEtherPhyMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10)
)
if mibBuilder.loadTexts:
    cadantEtherPhyMeasTable.setStatus("current")
_CadantEtherPhyMeasEntry_Object = MibTableRow
cadantEtherPhyMeasEntry = _CadantEtherPhyMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1)
)
cadantEtherPhyMeasEntry.setIndexNames(
    (0, "CADANT-HW-MEAS-MIB", "cadantEtherPhyMeasCardId"),
    (0, "CADANT-HW-MEAS-MIB", "cadantEtherPhyMeasPortId"),
)
if mibBuilder.loadTexts:
    cadantEtherPhyMeasEntry.setStatus("current")
_CadantEtherPhyMeasCardId_Type = CardId
_CadantEtherPhyMeasCardId_Object = MibTableColumn
cadantEtherPhyMeasCardId = _CadantEtherPhyMeasCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 1),
    _CadantEtherPhyMeasCardId_Type()
)
cadantEtherPhyMeasCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasCardId.setStatus("current")
_CadantEtherPhyMeasPortId_Type = PortId
_CadantEtherPhyMeasPortId_Object = MibTableColumn
cadantEtherPhyMeasPortId = _CadantEtherPhyMeasPortId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 2),
    _CadantEtherPhyMeasPortId_Type()
)
cadantEtherPhyMeasPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasPortId.setStatus("current")
_CadantEtherPhyMeasRxOctOK_Type = Counter64
_CadantEtherPhyMeasRxOctOK_Object = MibTableColumn
cadantEtherPhyMeasRxOctOK = _CadantEtherPhyMeasRxOctOK_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 3),
    _CadantEtherPhyMeasRxOctOK_Type()
)
cadantEtherPhyMeasRxOctOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxOctOK.setStatus("current")
_CadantEtherPhyMeasRxUniOK_Type = Counter64
_CadantEtherPhyMeasRxUniOK_Object = MibTableColumn
cadantEtherPhyMeasRxUniOK = _CadantEtherPhyMeasRxUniOK_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 4),
    _CadantEtherPhyMeasRxUniOK_Type()
)
cadantEtherPhyMeasRxUniOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxUniOK.setStatus("current")
_CadantEtherPhyMeasRxMultiOK_Type = Counter64
_CadantEtherPhyMeasRxMultiOK_Object = MibTableColumn
cadantEtherPhyMeasRxMultiOK = _CadantEtherPhyMeasRxMultiOK_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 5),
    _CadantEtherPhyMeasRxMultiOK_Type()
)
cadantEtherPhyMeasRxMultiOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxMultiOK.setStatus("current")
_CadantEtherPhyMeasRxBroadOK_Type = Counter64
_CadantEtherPhyMeasRxBroadOK_Object = MibTableColumn
cadantEtherPhyMeasRxBroadOK = _CadantEtherPhyMeasRxBroadOK_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 6),
    _CadantEtherPhyMeasRxBroadOK_Type()
)
cadantEtherPhyMeasRxBroadOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxBroadOK.setStatus("current")
_CadantEtherPhyMeasRxOverflow_Type = Counter64
_CadantEtherPhyMeasRxOverflow_Object = MibTableColumn
cadantEtherPhyMeasRxOverflow = _CadantEtherPhyMeasRxOverflow_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 7),
    _CadantEtherPhyMeasRxOverflow_Type()
)
cadantEtherPhyMeasRxOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxOverflow.setStatus("current")
_CadantEtherPhyMeasRxNormAlign_Type = Counter64
_CadantEtherPhyMeasRxNormAlign_Object = MibTableColumn
cadantEtherPhyMeasRxNormAlign = _CadantEtherPhyMeasRxNormAlign_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 8),
    _CadantEtherPhyMeasRxNormAlign_Type()
)
cadantEtherPhyMeasRxNormAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxNormAlign.setStatus("current")
_CadantEtherPhyMeasRxNormCRC_Type = Counter64
_CadantEtherPhyMeasRxNormCRC_Object = MibTableColumn
cadantEtherPhyMeasRxNormCRC = _CadantEtherPhyMeasRxNormCRC_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 9),
    _CadantEtherPhyMeasRxNormCRC_Type()
)
cadantEtherPhyMeasRxNormCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxNormCRC.setStatus("current")
_CadantEtherPhyMeasRxLongOK_Type = Counter64
_CadantEtherPhyMeasRxLongOK_Object = MibTableColumn
cadantEtherPhyMeasRxLongOK = _CadantEtherPhyMeasRxLongOK_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 10),
    _CadantEtherPhyMeasRxLongOK_Type()
)
cadantEtherPhyMeasRxLongOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxLongOK.setStatus("current")
_CadantEtherPhyMeasRxLongCRC_Type = Counter64
_CadantEtherPhyMeasRxLongCRC_Object = MibTableColumn
cadantEtherPhyMeasRxLongCRC = _CadantEtherPhyMeasRxLongCRC_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 11),
    _CadantEtherPhyMeasRxLongCRC_Type()
)
cadantEtherPhyMeasRxLongCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxLongCRC.setStatus("current")
_CadantEtherPhyMeasRxFalsCRS_Type = Counter64
_CadantEtherPhyMeasRxFalsCRS_Object = MibTableColumn
cadantEtherPhyMeasRxFalsCRS = _CadantEtherPhyMeasRxFalsCRS_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 12),
    _CadantEtherPhyMeasRxFalsCRS_Type()
)
cadantEtherPhyMeasRxFalsCRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxFalsCRS.setStatus("current")
_CadantEtherPhyMeasRxSymbolErrors_Type = Counter64
_CadantEtherPhyMeasRxSymbolErrors_Object = MibTableColumn
cadantEtherPhyMeasRxSymbolErrors = _CadantEtherPhyMeasRxSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 13),
    _CadantEtherPhyMeasRxSymbolErrors_Type()
)
cadantEtherPhyMeasRxSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxSymbolErrors.setStatus("current")
_CadantEtherPhyMeasRxPause_Type = Counter64
_CadantEtherPhyMeasRxPause_Object = MibTableColumn
cadantEtherPhyMeasRxPause = _CadantEtherPhyMeasRxPause_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 14),
    _CadantEtherPhyMeasRxPause_Type()
)
cadantEtherPhyMeasRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxPause.setStatus("current")
_CadantEtherPhyMeasTxOctOK_Type = Counter64
_CadantEtherPhyMeasTxOctOK_Object = MibTableColumn
cadantEtherPhyMeasTxOctOK = _CadantEtherPhyMeasTxOctOK_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 15),
    _CadantEtherPhyMeasTxOctOK_Type()
)
cadantEtherPhyMeasTxOctOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasTxOctOK.setStatus("current")
_CadantEtherPhyMeasTxUniOK_Type = Counter64
_CadantEtherPhyMeasTxUniOK_Object = MibTableColumn
cadantEtherPhyMeasTxUniOK = _CadantEtherPhyMeasTxUniOK_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 16),
    _CadantEtherPhyMeasTxUniOK_Type()
)
cadantEtherPhyMeasTxUniOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasTxUniOK.setStatus("current")
_CadantEtherPhyMeasTxMultiOK_Type = Counter64
_CadantEtherPhyMeasTxMultiOK_Object = MibTableColumn
cadantEtherPhyMeasTxMultiOK = _CadantEtherPhyMeasTxMultiOK_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 17),
    _CadantEtherPhyMeasTxMultiOK_Type()
)
cadantEtherPhyMeasTxMultiOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasTxMultiOK.setStatus("current")
_CadantEtherPhyMeasTxBroadOK_Type = Counter64
_CadantEtherPhyMeasTxBroadOK_Object = MibTableColumn
cadantEtherPhyMeasTxBroadOK = _CadantEtherPhyMeasTxBroadOK_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 18),
    _CadantEtherPhyMeasTxBroadOK_Type()
)
cadantEtherPhyMeasTxBroadOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasTxBroadOK.setStatus("current")
_CadantEtherPhyMeasTxScol_Type = Counter64
_CadantEtherPhyMeasTxScol_Object = MibTableColumn
cadantEtherPhyMeasTxScol = _CadantEtherPhyMeasTxScol_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 19),
    _CadantEtherPhyMeasTxScol_Type()
)
cadantEtherPhyMeasTxScol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasTxScol.setStatus("current")
_CadantEtherPhyMeasTxMcol_Type = Counter64
_CadantEtherPhyMeasTxMcol_Object = MibTableColumn
cadantEtherPhyMeasTxMcol = _CadantEtherPhyMeasTxMcol_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 20),
    _CadantEtherPhyMeasTxMcol_Type()
)
cadantEtherPhyMeasTxMcol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasTxMcol.setStatus("current")
_CadantEtherPhyMeasTxDeferred_Type = Counter64
_CadantEtherPhyMeasTxDeferred_Object = MibTableColumn
cadantEtherPhyMeasTxDeferred = _CadantEtherPhyMeasTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 21),
    _CadantEtherPhyMeasTxDeferred_Type()
)
cadantEtherPhyMeasTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasTxDeferred.setStatus("current")
_CadantEtherPhyMeasTxLcol_Type = Counter64
_CadantEtherPhyMeasTxLcol_Object = MibTableColumn
cadantEtherPhyMeasTxLcol = _CadantEtherPhyMeasTxLcol_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 22),
    _CadantEtherPhyMeasTxLcol_Type()
)
cadantEtherPhyMeasTxLcol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasTxLcol.setStatus("current")
_CadantEtherPhyMeasTxCcol_Type = Counter64
_CadantEtherPhyMeasTxCcol_Object = MibTableColumn
cadantEtherPhyMeasTxCcol = _CadantEtherPhyMeasTxCcol_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 23),
    _CadantEtherPhyMeasTxCcol_Type()
)
cadantEtherPhyMeasTxCcol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasTxCcol.setStatus("current")
_CadantEtherPhyMeasTxErr_Type = Counter64
_CadantEtherPhyMeasTxErr_Object = MibTableColumn
cadantEtherPhyMeasTxErr = _CadantEtherPhyMeasTxErr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 24),
    _CadantEtherPhyMeasTxErr_Type()
)
cadantEtherPhyMeasTxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasTxErr.setStatus("current")
_CadantEtherPhyMeasTxPause_Type = Counter64
_CadantEtherPhyMeasTxPause_Object = MibTableColumn
cadantEtherPhyMeasTxPause = _CadantEtherPhyMeasTxPause_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 25),
    _CadantEtherPhyMeasTxPause_Type()
)
cadantEtherPhyMeasTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasTxPause.setStatus("current")
_CadantEtherPhyMeasRxShortOK_Type = Counter64
_CadantEtherPhyMeasRxShortOK_Object = MibTableColumn
cadantEtherPhyMeasRxShortOK = _CadantEtherPhyMeasRxShortOK_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 26),
    _CadantEtherPhyMeasRxShortOK_Type()
)
cadantEtherPhyMeasRxShortOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxShortOK.setStatus("current")
_CadantEtherPhyMeasRxShortCRC_Type = Counter64
_CadantEtherPhyMeasRxShortCRC_Object = MibTableColumn
cadantEtherPhyMeasRxShortCRC = _CadantEtherPhyMeasRxShortCRC_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 27),
    _CadantEtherPhyMeasRxShortCRC_Type()
)
cadantEtherPhyMeasRxShortCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxShortCRC.setStatus("current")
_CadantEtherPhyMeasRxRunt_Type = Counter64
_CadantEtherPhyMeasRxRunt_Object = MibTableColumn
cadantEtherPhyMeasRxRunt = _CadantEtherPhyMeasRxRunt_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 28),
    _CadantEtherPhyMeasRxRunt_Type()
)
cadantEtherPhyMeasRxRunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxRunt.setStatus("current")
_CadantEtherPhyMeasRxOctBad_Type = Counter64
_CadantEtherPhyMeasRxOctBad_Object = MibTableColumn
cadantEtherPhyMeasRxOctBad = _CadantEtherPhyMeasRxOctBad_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 10, 1, 29),
    _CadantEtherPhyMeasRxOctBad_Type()
)
cadantEtherPhyMeasRxOctBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadantEtherPhyMeasRxOctBad.setStatus("current")
_CadDFIDMeasTable_Object = MibTable
cadDFIDMeasTable = _CadDFIDMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14)
)
if mibBuilder.loadTexts:
    cadDFIDMeasTable.setStatus("current")
_CadDFIDMeasEntry_Object = MibTableRow
cadDFIDMeasEntry = _CadDFIDMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1)
)
cadDFIDMeasEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CADANT-HW-MEAS-MIB", "cadDFIDMeasIndex"),
)
if mibBuilder.loadTexts:
    cadDFIDMeasEntry.setStatus("current")
_CadDFIDMeasIndex_Type = SFIDIndex
_CadDFIDMeasIndex_Object = MibTableColumn
cadDFIDMeasIndex = _CadDFIDMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1, 3),
    _CadDFIDMeasIndex_Type()
)
cadDFIDMeasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDFIDMeasIndex.setStatus("current")
_CadDFIDMeasBytsArrived_Type = Counter64
_CadDFIDMeasBytsArrived_Object = MibTableColumn
cadDFIDMeasBytsArrived = _CadDFIDMeasBytsArrived_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1, 4),
    _CadDFIDMeasBytsArrived_Type()
)
cadDFIDMeasBytsArrived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDFIDMeasBytsArrived.setStatus("current")
_CadDFIDMeasPktsArrived_Type = Counter64
_CadDFIDMeasPktsArrived_Object = MibTableColumn
cadDFIDMeasPktsArrived = _CadDFIDMeasPktsArrived_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1, 5),
    _CadDFIDMeasPktsArrived_Type()
)
cadDFIDMeasPktsArrived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDFIDMeasPktsArrived.setStatus("current")
_CadDFIDMeasBytsDropped_Type = Counter64
_CadDFIDMeasBytsDropped_Object = MibTableColumn
cadDFIDMeasBytsDropped = _CadDFIDMeasBytsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1, 6),
    _CadDFIDMeasBytsDropped_Type()
)
cadDFIDMeasBytsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDFIDMeasBytsDropped.setStatus("current")
_CadDFIDMeasPktsDropped_Type = Counter64
_CadDFIDMeasPktsDropped_Object = MibTableColumn
cadDFIDMeasPktsDropped = _CadDFIDMeasPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1, 7),
    _CadDFIDMeasPktsDropped_Type()
)
cadDFIDMeasPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDFIDMeasPktsDropped.setStatus("current")
_CadDFIDMeasBytsUnkDropped_Type = Counter64
_CadDFIDMeasBytsUnkDropped_Object = MibTableColumn
cadDFIDMeasBytsUnkDropped = _CadDFIDMeasBytsUnkDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1, 8),
    _CadDFIDMeasBytsUnkDropped_Type()
)
cadDFIDMeasBytsUnkDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDFIDMeasBytsUnkDropped.setStatus("current")
_CadDFIDMeasDFID_Type = DFIDIndex
_CadDFIDMeasDFID_Object = MibTableColumn
cadDFIDMeasDFID = _CadDFIDMeasDFID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1, 9),
    _CadDFIDMeasDFID_Type()
)
cadDFIDMeasDFID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDFIDMeasDFID.setStatus("current")
_CadDFIDMeasPHSUnknowns_Type = Counter64
_CadDFIDMeasPHSUnknowns_Object = MibTableColumn
cadDFIDMeasPHSUnknowns = _CadDFIDMeasPHSUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1, 10),
    _CadDFIDMeasPHSUnknowns_Type()
)
cadDFIDMeasPHSUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDFIDMeasPHSUnknowns.setStatus("current")
_CadDFIDMeasMacAddress_Type = MacAddress
_CadDFIDMeasMacAddress_Object = MibTableColumn
cadDFIDMeasMacAddress = _CadDFIDMeasMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1, 11),
    _CadDFIDMeasMacAddress_Type()
)
cadDFIDMeasMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDFIDMeasMacAddress.setStatus("current")
_CadDFIDMeasSCN_Type = DisplayString
_CadDFIDMeasSCN_Object = MibTableColumn
cadDFIDMeasSCN = _CadDFIDMeasSCN_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1, 12),
    _CadDFIDMeasSCN_Type()
)
cadDFIDMeasSCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDFIDMeasSCN.setStatus("current")
_CadDFIDMeasPolicedDelayPkts_Type = Counter64
_CadDFIDMeasPolicedDelayPkts_Object = MibTableColumn
cadDFIDMeasPolicedDelayPkts = _CadDFIDMeasPolicedDelayPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1, 13),
    _CadDFIDMeasPolicedDelayPkts_Type()
)
cadDFIDMeasPolicedDelayPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDFIDMeasPolicedDelayPkts.setStatus("current")
_CadDFIDMeasGateID_Type = Unsigned32
_CadDFIDMeasGateID_Object = MibTableColumn
cadDFIDMeasGateID = _CadDFIDMeasGateID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 14, 1, 14),
    _CadDFIDMeasGateID_Type()
)
cadDFIDMeasGateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDFIDMeasGateID.setStatus("current")
_CadQosPktClassMeasTable_Object = MibTable
cadQosPktClassMeasTable = _CadQosPktClassMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 16)
)
if mibBuilder.loadTexts:
    cadQosPktClassMeasTable.setStatus("current")
_CadQosPktClassMeasEntry_Object = MibTableRow
cadQosPktClassMeasEntry = _CadQosPktClassMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 16, 1)
)
cadQosPktClassMeasEntry.setIndexNames(
    (0, "CADANT-HW-MEAS-MIB", "cadQosPktClassMeasIfIndex"),
    (0, "CADANT-HW-MEAS-MIB", "cadQosPktClassMeasSFID"),
    (0, "CADANT-HW-MEAS-MIB", "cadQosPktClassMeasPktClassId"),
)
if mibBuilder.loadTexts:
    cadQosPktClassMeasEntry.setStatus("current")
_CadQosPktClassMeasIfIndex_Type = InterfaceIndex
_CadQosPktClassMeasIfIndex_Object = MibTableColumn
cadQosPktClassMeasIfIndex = _CadQosPktClassMeasIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 16, 1, 1),
    _CadQosPktClassMeasIfIndex_Type()
)
cadQosPktClassMeasIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadQosPktClassMeasIfIndex.setStatus("current")
_CadQosPktClassMeasSFID_Type = SFIDIndex
_CadQosPktClassMeasSFID_Object = MibTableColumn
cadQosPktClassMeasSFID = _CadQosPktClassMeasSFID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 16, 1, 2),
    _CadQosPktClassMeasSFID_Type()
)
cadQosPktClassMeasSFID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadQosPktClassMeasSFID.setStatus("current")
_CadQosPktClassMeasPktClassId_Type = PktClassId
_CadQosPktClassMeasPktClassId_Object = MibTableColumn
cadQosPktClassMeasPktClassId = _CadQosPktClassMeasPktClassId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 16, 1, 3),
    _CadQosPktClassMeasPktClassId_Type()
)
cadQosPktClassMeasPktClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadQosPktClassMeasPktClassId.setStatus("current")
_CadQosPktClassMeasPkts_Type = Counter64
_CadQosPktClassMeasPkts_Object = MibTableColumn
cadQosPktClassMeasPkts = _CadQosPktClassMeasPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 16, 1, 4),
    _CadQosPktClassMeasPkts_Type()
)
cadQosPktClassMeasPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadQosPktClassMeasPkts.setStatus("current")
_CadIfMeasTable_Object = MibTable
cadIfMeasTable = _CadIfMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18)
)
if mibBuilder.loadTexts:
    cadIfMeasTable.setStatus("current")
_CadIfMeasEntry_Object = MibTableRow
cadIfMeasEntry = _CadIfMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1)
)
cadIfMeasEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cadIfMeasEntry.setStatus("current")
_CadIfInOctets_Type = Counter64
_CadIfInOctets_Object = MibTableColumn
cadIfInOctets = _CadIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 1),
    _CadIfInOctets_Type()
)
cadIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfInOctets.setStatus("current")
_CadIfInUcastPkts_Type = Counter64
_CadIfInUcastPkts_Object = MibTableColumn
cadIfInUcastPkts = _CadIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 2),
    _CadIfInUcastPkts_Type()
)
cadIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfInUcastPkts.setStatus("current")
_CadIfInMulticastPkts_Type = Counter64
_CadIfInMulticastPkts_Object = MibTableColumn
cadIfInMulticastPkts = _CadIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 3),
    _CadIfInMulticastPkts_Type()
)
cadIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfInMulticastPkts.setStatus("current")
_CadIfInBroadcastPkts_Type = Counter64
_CadIfInBroadcastPkts_Object = MibTableColumn
cadIfInBroadcastPkts = _CadIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 4),
    _CadIfInBroadcastPkts_Type()
)
cadIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfInBroadcastPkts.setStatus("current")
_CadIfInDiscards_Type = Counter64
_CadIfInDiscards_Object = MibTableColumn
cadIfInDiscards = _CadIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 5),
    _CadIfInDiscards_Type()
)
cadIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfInDiscards.setStatus("current")
_CadIfInErrors_Type = Counter64
_CadIfInErrors_Object = MibTableColumn
cadIfInErrors = _CadIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 6),
    _CadIfInErrors_Type()
)
cadIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfInErrors.setStatus("current")
_CadIfInUnknownProtos_Type = Counter64
_CadIfInUnknownProtos_Object = MibTableColumn
cadIfInUnknownProtos = _CadIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 7),
    _CadIfInUnknownProtos_Type()
)
cadIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfInUnknownProtos.setStatus("current")
_CadIfOutOctets_Type = Counter64
_CadIfOutOctets_Object = MibTableColumn
cadIfOutOctets = _CadIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 8),
    _CadIfOutOctets_Type()
)
cadIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfOutOctets.setStatus("current")
_CadIfOutUcastPkts_Type = Counter64
_CadIfOutUcastPkts_Object = MibTableColumn
cadIfOutUcastPkts = _CadIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 9),
    _CadIfOutUcastPkts_Type()
)
cadIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfOutUcastPkts.setStatus("current")
_CadIfOutMulticastPkts_Type = Counter64
_CadIfOutMulticastPkts_Object = MibTableColumn
cadIfOutMulticastPkts = _CadIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 10),
    _CadIfOutMulticastPkts_Type()
)
cadIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfOutMulticastPkts.setStatus("current")
_CadIfOutBroadcastPkts_Type = Counter64
_CadIfOutBroadcastPkts_Object = MibTableColumn
cadIfOutBroadcastPkts = _CadIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 11),
    _CadIfOutBroadcastPkts_Type()
)
cadIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfOutBroadcastPkts.setStatus("current")
_CadIfOutDiscards_Type = Counter64
_CadIfOutDiscards_Object = MibTableColumn
cadIfOutDiscards = _CadIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 12),
    _CadIfOutDiscards_Type()
)
cadIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfOutDiscards.setStatus("current")
_CadIfOutErrors_Type = Counter64
_CadIfOutErrors_Object = MibTableColumn
cadIfOutErrors = _CadIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 18, 1, 13),
    _CadIfOutErrors_Type()
)
cadIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfOutErrors.setStatus("current")
_CadDCardMeasTable_Object = MibTable
cadDCardMeasTable = _CadDCardMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 20)
)
if mibBuilder.loadTexts:
    cadDCardMeasTable.setStatus("current")
_CadDCardMeasEntry_Object = MibTableRow
cadDCardMeasEntry = _CadDCardMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 20, 1)
)
cadDCardMeasEntry.setIndexNames(
    (0, "CADANT-HW-MEAS-MIB", "cadDCardMeasCardId"),
)
if mibBuilder.loadTexts:
    cadDCardMeasEntry.setStatus("current")
_CadDCardMeasCardId_Type = CardId
_CadDCardMeasCardId_Object = MibTableColumn
cadDCardMeasCardId = _CadDCardMeasCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 20, 1, 1),
    _CadDCardMeasCardId_Type()
)
cadDCardMeasCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDCardMeasCardId.setStatus("current")
_CadDCardIpInReceives_Type = Counter64
_CadDCardIpInReceives_Object = MibTableColumn
cadDCardIpInReceives = _CadDCardIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 20, 1, 2),
    _CadDCardIpInReceives_Type()
)
cadDCardIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDCardIpInReceives.setStatus("current")
_CadDCardIpInHdrErrors_Type = Counter64
_CadDCardIpInHdrErrors_Object = MibTableColumn
cadDCardIpInHdrErrors = _CadDCardIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 20, 1, 3),
    _CadDCardIpInHdrErrors_Type()
)
cadDCardIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDCardIpInHdrErrors.setStatus("current")
_CadDCardIpInAddrErrors_Type = Counter64
_CadDCardIpInAddrErrors_Object = MibTableColumn
cadDCardIpInAddrErrors = _CadDCardIpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 20, 1, 4),
    _CadDCardIpInAddrErrors_Type()
)
cadDCardIpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDCardIpInAddrErrors.setStatus("current")
_CadDCardDhcpThrottleDropPkts_Type = Counter64
_CadDCardDhcpThrottleDropPkts_Object = MibTableColumn
cadDCardDhcpThrottleDropPkts = _CadDCardDhcpThrottleDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 20, 1, 5),
    _CadDCardDhcpThrottleDropPkts_Type()
)
cadDCardDhcpThrottleDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDCardDhcpThrottleDropPkts.setStatus("current")
_CadDCardArpThrottleDropPkts_Type = Counter64
_CadDCardArpThrottleDropPkts_Object = MibTableColumn
cadDCardArpThrottleDropPkts = _CadDCardArpThrottleDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 20, 1, 6),
    _CadDCardArpThrottleDropPkts_Type()
)
cadDCardArpThrottleDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDCardArpThrottleDropPkts.setStatus("current")
_CadDCardDhcpV6ThrottleDropPkts_Type = Counter64
_CadDCardDhcpV6ThrottleDropPkts_Object = MibTableColumn
cadDCardDhcpV6ThrottleDropPkts = _CadDCardDhcpV6ThrottleDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 20, 1, 7),
    _CadDCardDhcpV6ThrottleDropPkts_Type()
)
cadDCardDhcpV6ThrottleDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDCardDhcpV6ThrottleDropPkts.setStatus("current")
_CadDCardNdThrottleDropPkts_Type = Counter64
_CadDCardNdThrottleDropPkts_Object = MibTableColumn
cadDCardNdThrottleDropPkts = _CadDCardNdThrottleDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 20, 1, 8),
    _CadDCardNdThrottleDropPkts_Type()
)
cadDCardNdThrottleDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDCardNdThrottleDropPkts.setStatus("current")
_CadDCardIgmpThrottleDropPkts_Type = Counter64
_CadDCardIgmpThrottleDropPkts_Object = MibTableColumn
cadDCardIgmpThrottleDropPkts = _CadDCardIgmpThrottleDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 20, 1, 9),
    _CadDCardIgmpThrottleDropPkts_Type()
)
cadDCardIgmpThrottleDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDCardIgmpThrottleDropPkts.setStatus("current")
_CadInterfaceUtilizationTable_Object = MibTable
cadInterfaceUtilizationTable = _CadInterfaceUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 23)
)
if mibBuilder.loadTexts:
    cadInterfaceUtilizationTable.setStatus("current")
_CadInterfaceUtilizationEntry_Object = MibTableRow
cadInterfaceUtilizationEntry = _CadInterfaceUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 23, 1)
)
cadInterfaceUtilizationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CADANT-HW-MEAS-MIB", "cadInterfaceUtilizationDirection"),
)
if mibBuilder.loadTexts:
    cadInterfaceUtilizationEntry.setStatus("current")
_CadInterfaceUtilizationDirection_Type = CadIfDirection
_CadInterfaceUtilizationDirection_Object = MibTableColumn
cadInterfaceUtilizationDirection = _CadInterfaceUtilizationDirection_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 23, 1, 1),
    _CadInterfaceUtilizationDirection_Type()
)
cadInterfaceUtilizationDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadInterfaceUtilizationDirection.setStatus("current")


class _CadInterfaceUtilizationPercentage_Type(Integer32):
    """Custom type cadInterfaceUtilizationPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadInterfaceUtilizationPercentage_Type.__name__ = "Integer32"
_CadInterfaceUtilizationPercentage_Object = MibTableColumn
cadInterfaceUtilizationPercentage = _CadInterfaceUtilizationPercentage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 23, 1, 2),
    _CadInterfaceUtilizationPercentage_Type()
)
cadInterfaceUtilizationPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadInterfaceUtilizationPercentage.setStatus("current")
if mibBuilder.loadTexts:
    cadInterfaceUtilizationPercentage.setUnits("percent")


class _CadInterfaceUtilizationAvgContSlots_Type(Integer32):
    """Custom type cadInterfaceUtilizationAvgContSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadInterfaceUtilizationAvgContSlots_Type.__name__ = "Integer32"
_CadInterfaceUtilizationAvgContSlots_Object = MibTableColumn
cadInterfaceUtilizationAvgContSlots = _CadInterfaceUtilizationAvgContSlots_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 23, 1, 3),
    _CadInterfaceUtilizationAvgContSlots_Type()
)
cadInterfaceUtilizationAvgContSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadInterfaceUtilizationAvgContSlots.setStatus("current")
if mibBuilder.loadTexts:
    cadInterfaceUtilizationAvgContSlots.setUnits("percent")


class _CadInterfaceHighResUtilizationPercentage_Type(Integer32):
    """Custom type cadInterfaceHighResUtilizationPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CadInterfaceHighResUtilizationPercentage_Type.__name__ = "Integer32"
_CadInterfaceHighResUtilizationPercentage_Object = MibTableColumn
cadInterfaceHighResUtilizationPercentage = _CadInterfaceHighResUtilizationPercentage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 23, 1, 4),
    _CadInterfaceHighResUtilizationPercentage_Type()
)
cadInterfaceHighResUtilizationPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadInterfaceHighResUtilizationPercentage.setStatus("current")
if mibBuilder.loadTexts:
    cadInterfaceHighResUtilizationPercentage.setUnits("Hundredth of a percent")
_CadInterfaceIntervalOctetsForwarded_Type = Counter64
_CadInterfaceIntervalOctetsForwarded_Object = MibTableColumn
cadInterfaceIntervalOctetsForwarded = _CadInterfaceIntervalOctetsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 23, 1, 5),
    _CadInterfaceIntervalOctetsForwarded_Type()
)
cadInterfaceIntervalOctetsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadInterfaceIntervalOctetsForwarded.setStatus("current")
_CadFftUpstreamChannelTable_Object = MibTable
cadFftUpstreamChannelTable = _CadFftUpstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 24)
)
if mibBuilder.loadTexts:
    cadFftUpstreamChannelTable.setStatus("current")
_CadFftUpstreamChannelEntry_Object = MibTableRow
cadFftUpstreamChannelEntry = _CadFftUpstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 24, 1)
)
cadFftUpstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cadFftUpstreamChannelEntry.setStatus("current")
_CadFftInProgress_Type = TruthValue
_CadFftInProgress_Object = MibTableColumn
cadFftInProgress = _CadFftInProgress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 24, 1, 1),
    _CadFftInProgress_Type()
)
cadFftInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFftInProgress.setStatus("current")
_CadFftCurrentTriggers_Type = Unsigned32
_CadFftCurrentTriggers_Object = MibTableColumn
cadFftCurrentTriggers = _CadFftCurrentTriggers_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 24, 1, 2),
    _CadFftCurrentTriggers_Type()
)
cadFftCurrentTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFftCurrentTriggers.setStatus("current")
_CadSubMgtPktFilterExtTable_Object = MibTable
cadSubMgtPktFilterExtTable = _CadSubMgtPktFilterExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 25)
)
if mibBuilder.loadTexts:
    cadSubMgtPktFilterExtTable.setStatus("current")
_CadSubMgtPktFilterExtEntry_Object = MibTableRow
cadSubMgtPktFilterExtEntry = _CadSubMgtPktFilterExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 25, 1)
)
if mibBuilder.loadTexts:
    cadSubMgtPktFilterExtEntry.setStatus("current")


class _CadSubMgtPktFilterMatchesReset_Type(TruthValue):
    """Custom type cadSubMgtPktFilterMatchesReset based on TruthValue"""


_CadSubMgtPktFilterMatchesReset_Object = MibTableColumn
cadSubMgtPktFilterMatchesReset = _CadSubMgtPktFilterMatchesReset_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 25, 1, 1),
    _CadSubMgtPktFilterMatchesReset_Type()
)
cadSubMgtPktFilterMatchesReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSubMgtPktFilterMatchesReset.setStatus("current")
_CadSubMgtPktFilterLastChanged_Type = TimeStamp
_CadSubMgtPktFilterLastChanged_Object = MibTableColumn
cadSubMgtPktFilterLastChanged = _CadSubMgtPktFilterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 25, 1, 2),
    _CadSubMgtPktFilterLastChanged_Type()
)
cadSubMgtPktFilterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadSubMgtPktFilterLastChanged.setStatus("current")


class _CadSubMgtPktFilterCaptureEnabled_Type(TruthValue):
    """Custom type cadSubMgtPktFilterCaptureEnabled based on TruthValue"""


_CadSubMgtPktFilterCaptureEnabled_Object = MibTableColumn
cadSubMgtPktFilterCaptureEnabled = _CadSubMgtPktFilterCaptureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 25, 1, 3),
    _CadSubMgtPktFilterCaptureEnabled_Type()
)
cadSubMgtPktFilterCaptureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSubMgtPktFilterCaptureEnabled.setStatus("current")
_CadLaesCountTable_Object = MibTable
cadLaesCountTable = _CadLaesCountTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 26)
)
if mibBuilder.loadTexts:
    cadLaesCountTable.setStatus("current")
_CadLaesCountEntry_Object = MibTableRow
cadLaesCountEntry = _CadLaesCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 26, 1)
)
cadLaesCountEntry.setIndexNames(
    (0, "PKTC-ES-TAP-MIB", "pktcEScTapMediationContentId"),
    (0, "PKTC-ES-TAP-MIB", "pktcEScTapStreamIndex"),
)
if mibBuilder.loadTexts:
    cadLaesCountEntry.setStatus("current")
_CadLaesCountMacDomainIfIndex_Type = InterfaceIndex
_CadLaesCountMacDomainIfIndex_Object = MibTableColumn
cadLaesCountMacDomainIfIndex = _CadLaesCountMacDomainIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 26, 1, 1),
    _CadLaesCountMacDomainIfIndex_Type()
)
cadLaesCountMacDomainIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLaesCountMacDomainIfIndex.setStatus("current")
_CadLaesCountStreamDirection_Type = IfDirection
_CadLaesCountStreamDirection_Object = MibTableColumn
cadLaesCountStreamDirection = _CadLaesCountStreamDirection_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 26, 1, 2),
    _CadLaesCountStreamDirection_Type()
)
cadLaesCountStreamDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLaesCountStreamDirection.setStatus("current")
_CadLaesCountInterceptedPackets_Type = Counter32
_CadLaesCountInterceptedPackets_Object = MibTableColumn
cadLaesCountInterceptedPackets = _CadLaesCountInterceptedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 26, 1, 3),
    _CadLaesCountInterceptedPackets_Type()
)
cadLaesCountInterceptedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLaesCountInterceptedPackets.setStatus("current")
_CadLaesCountInterceptDrops_Type = Counter32
_CadLaesCountInterceptDrops_Object = MibTableColumn
cadLaesCountInterceptDrops = _CadLaesCountInterceptDrops_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 2, 26, 1, 4),
    _CadLaesCountInterceptDrops_Type()
)
cadLaesCountInterceptDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLaesCountInterceptDrops.setStatus("current")
docsSubmgt3FilterGrpEntry.registerAugmentions(
    ("CADANT-HW-MEAS-MIB",
     "cadSubMgtPktFilterExtEntry")
)
cadSubMgtPktFilterExtEntry.setIndexNames(*docsSubmgt3FilterGrpEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-HW-MEAS-MIB",
    **{"DFIDIndex": DFIDIndex,
       "PktClassId": PktClassId,
       "SFIDIndex": SFIDIndex,
       "UFIDIndex": UFIDIndex,
       "SIDValue": SIDValue,
       "TMSide": TMSide,
       "cadHardwareMeasMib": cadHardwareMeasMib,
       "cadantHWMeasGeneral": cadantHWMeasGeneral,
       "cadantFabActualDepth": cadantFabActualDepth,
       "cadantFabAvgDepth": cadantFabAvgDepth,
       "cadantUPortMeasTable": cadantUPortMeasTable,
       "cadantUPortMeasEntry": cadantUPortMeasEntry,
       "cadantUPortMeasCardId": cadantUPortMeasCardId,
       "cadantUPortMeasPortId": cadantUPortMeasPortId,
       "cadantUPortMeasUcastFrms": cadantUPortMeasUcastFrms,
       "cadantUPortMeasMcastFrms": cadantUPortMeasMcastFrms,
       "cadantUPortMeasBcastFrms": cadantUPortMeasBcastFrms,
       "cadantUPortMeasUcastDataFrms": cadantUPortMeasUcastDataFrms,
       "cadantUPortMeasMcastDataFrms": cadantUPortMeasMcastDataFrms,
       "cadantUPortMeasBcastDataFrms": cadantUPortMeasBcastDataFrms,
       "cadantUPortMeasDiscardFrms": cadantUPortMeasDiscardFrms,
       "cadantUPortMeasIfInOctets": cadantUPortMeasIfInOctets,
       "cadantUPortMeasIfInDataOctets": cadantUPortMeasIfInDataOctets,
       "cadantUPortMeasIfInUnknownProtos": cadantUPortMeasIfInUnknownProtos,
       "cadantUPortMeasAppMinusBWReqFrms": cadantUPortMeasAppMinusBWReqFrms,
       "cadantUPortMeasErroredFrms": cadantUPortMeasErroredFrms,
       "cadantUPortMeasFilteredFrms": cadantUPortMeasFilteredFrms,
       "cadantUPortMeasBcastReqOpps": cadantUPortMeasBcastReqOpps,
       "cadantUPortMeasBcastReqColls": cadantUPortMeasBcastReqColls,
       "cadantUPortMeasBcastReqNoEnergies": cadantUPortMeasBcastReqNoEnergies,
       "cadantUPortMeasBcastReqRxPwr1s": cadantUPortMeasBcastReqRxPwr1s,
       "cadantUPortMeasBcastReqRxPwr2s": cadantUPortMeasBcastReqRxPwr2s,
       "cadantUPortMeasInitMaintOpps": cadantUPortMeasInitMaintOpps,
       "cadantUPortMeasInitMaintColls": cadantUPortMeasInitMaintColls,
       "cadantUPortMeasInitMaintNoEnergies": cadantUPortMeasInitMaintNoEnergies,
       "cadantUPortMeasInitMaintRxPwr1s": cadantUPortMeasInitMaintRxPwr1s,
       "cadantUPortMeasInitMaintRxPwr2s": cadantUPortMeasInitMaintRxPwr2s,
       "cadantDPortMeasTable": cadantDPortMeasTable,
       "cadantDPortMeasEntry": cadantDPortMeasEntry,
       "cadantDPortMeasCardId": cadantDPortMeasCardId,
       "cadantDPortMeasPortId": cadantDPortMeasPortId,
       "cadantDPortMeasIfOutOctets": cadantDPortMeasIfOutOctets,
       "cadantDPortMeasIfOutUcastPkts": cadantDPortMeasIfOutUcastPkts,
       "cadantDPortMeasIfOutMcastPkts": cadantDPortMeasIfOutMcastPkts,
       "cadantDPortMeasIfOutBcastPkts": cadantDPortMeasIfOutBcastPkts,
       "cadantDPortMeasIfOutDataOctets": cadantDPortMeasIfOutDataOctets,
       "cadantDPortMeasIfOutUcastDataPkts": cadantDPortMeasIfOutUcastDataPkts,
       "cadantDPortMeasIfOutMcastDataPkts": cadantDPortMeasIfOutMcastDataPkts,
       "cadantDPortMeasIfOutBcastDataPkts": cadantDPortMeasIfOutBcastDataPkts,
       "cadantDPortMeasGotNoDMACs": cadantDPortMeasGotNoDMACs,
       "cadantDPortMeasGotNoClasses": cadantDPortMeasGotNoClasses,
       "cadantDPortMeasSyncPkts": cadantDPortMeasSyncPkts,
       "cadantDPortMeasAppUcastPkts": cadantDPortMeasAppUcastPkts,
       "cadantDPortMeasAppMcastPkts": cadantDPortMeasAppMcastPkts,
       "cadantDPortMeasIfOutTotalOctets": cadantDPortMeasIfOutTotalOctets,
       "cadantDPortMeasOfdmIfSpeed": cadantDPortMeasOfdmIfSpeed,
       "cadantDPortMeasOfdmHighestAvgBitsPerSubc": cadantDPortMeasOfdmHighestAvgBitsPerSubc,
       "cadantDPortMeasOfdmNumDataSubc": cadantDPortMeasOfdmNumDataSubc,
       "cadantDPortMeasOfdmChanUtilization": cadantDPortMeasOfdmChanUtilization,
       "cadantUFIDMeasTable": cadantUFIDMeasTable,
       "cadantUFIDMeasEntry": cadantUFIDMeasEntry,
       "cadantUFIDMeasSID": cadantUFIDMeasSID,
       "cadantUFIDMeasPktsSGreedyDrop": cadantUFIDMeasPktsSGreedyDrop,
       "cadantUFIDMeasBytsOtherDrop": cadantUFIDMeasBytsOtherDrop,
       "cadantUFIDMeasBytsArrived": cadantUFIDMeasBytsArrived,
       "cadantUFIDMeasPktsArrived": cadantUFIDMeasPktsArrived,
       "cadantUFIDMeasSIDCorrecteds": cadantUFIDMeasSIDCorrecteds,
       "cadantUFIDMeasSIDUnerroreds": cadantUFIDMeasSIDUnerroreds,
       "cadantUFIDMeasSIDUnCorrecteds": cadantUFIDMeasSIDUnCorrecteds,
       "cadantUFIDMeasSIDNoUniqueWordDetecteds": cadantUFIDMeasSIDNoUniqueWordDetecteds,
       "cadantUFIDMeasSIDCollidedBursts": cadantUFIDMeasSIDCollidedBursts,
       "cadantUFIDMeasSIDNoEnergyDetecteds": cadantUFIDMeasSIDNoEnergyDetecteds,
       "cadantUFIDMeasSIDLengthErrors": cadantUFIDMeasSIDLengthErrors,
       "cadantUFIDMeasSIDMACErrors": cadantUFIDMeasSIDMACErrors,
       "cadantUFIDMeasMacAddress": cadantUFIDMeasMacAddress,
       "cadantUFIDMeasSCN": cadantUFIDMeasSCN,
       "cadantUFIDMeasSFID": cadantUFIDMeasSFID,
       "cadantUFIDMeasPHSUnknowns": cadantUFIDMeasPHSUnknowns,
       "cadantUFIDMeasFragPkts": cadantUFIDMeasFragPkts,
       "cadantUFIDMeasIncompletePkts": cadantUFIDMeasIncompletePkts,
       "cadantUFIDMeasConcatBursts": cadantUFIDMeasConcatBursts,
       "cadantUFIDMeasSIDSignalNoise": cadantUFIDMeasSIDSignalNoise,
       "cadantUFIDMeasSIDMicroreflections": cadantUFIDMeasSIDMicroreflections,
       "cadantUFIDMeasSIDHCSErrors": cadantUFIDMeasSIDHCSErrors,
       "cadantUFIDMeasSIDCRCErrors": cadantUFIDMeasSIDCRCErrors,
       "cadantUFIDMeasUFIDIndex": cadantUFIDMeasUFIDIndex,
       "cadantUFIDMeasGateID": cadantUFIDMeasGateID,
       "cadantUFIDMeasSIDMacIfIndex": cadantUFIDMeasSIDMacIfIndex,
       "cadantUFIDMeasSIDBonded": cadantUFIDMeasSIDBonded,
       "cadantUFIDMeasCcfStatsSgmtValids": cadantUFIDMeasCcfStatsSgmtValids,
       "cadantUFIDMeasCcfStatsSgmtLost": cadantUFIDMeasCcfStatsSgmtLost,
       "cadantUFIDMeasCcfStatsSgmtDrop": cadantUFIDMeasCcfStatsSgmtDrop,
       "cadantEtherPhyMeasTable": cadantEtherPhyMeasTable,
       "cadantEtherPhyMeasEntry": cadantEtherPhyMeasEntry,
       "cadantEtherPhyMeasCardId": cadantEtherPhyMeasCardId,
       "cadantEtherPhyMeasPortId": cadantEtherPhyMeasPortId,
       "cadantEtherPhyMeasRxOctOK": cadantEtherPhyMeasRxOctOK,
       "cadantEtherPhyMeasRxUniOK": cadantEtherPhyMeasRxUniOK,
       "cadantEtherPhyMeasRxMultiOK": cadantEtherPhyMeasRxMultiOK,
       "cadantEtherPhyMeasRxBroadOK": cadantEtherPhyMeasRxBroadOK,
       "cadantEtherPhyMeasRxOverflow": cadantEtherPhyMeasRxOverflow,
       "cadantEtherPhyMeasRxNormAlign": cadantEtherPhyMeasRxNormAlign,
       "cadantEtherPhyMeasRxNormCRC": cadantEtherPhyMeasRxNormCRC,
       "cadantEtherPhyMeasRxLongOK": cadantEtherPhyMeasRxLongOK,
       "cadantEtherPhyMeasRxLongCRC": cadantEtherPhyMeasRxLongCRC,
       "cadantEtherPhyMeasRxFalsCRS": cadantEtherPhyMeasRxFalsCRS,
       "cadantEtherPhyMeasRxSymbolErrors": cadantEtherPhyMeasRxSymbolErrors,
       "cadantEtherPhyMeasRxPause": cadantEtherPhyMeasRxPause,
       "cadantEtherPhyMeasTxOctOK": cadantEtherPhyMeasTxOctOK,
       "cadantEtherPhyMeasTxUniOK": cadantEtherPhyMeasTxUniOK,
       "cadantEtherPhyMeasTxMultiOK": cadantEtherPhyMeasTxMultiOK,
       "cadantEtherPhyMeasTxBroadOK": cadantEtherPhyMeasTxBroadOK,
       "cadantEtherPhyMeasTxScol": cadantEtherPhyMeasTxScol,
       "cadantEtherPhyMeasTxMcol": cadantEtherPhyMeasTxMcol,
       "cadantEtherPhyMeasTxDeferred": cadantEtherPhyMeasTxDeferred,
       "cadantEtherPhyMeasTxLcol": cadantEtherPhyMeasTxLcol,
       "cadantEtherPhyMeasTxCcol": cadantEtherPhyMeasTxCcol,
       "cadantEtherPhyMeasTxErr": cadantEtherPhyMeasTxErr,
       "cadantEtherPhyMeasTxPause": cadantEtherPhyMeasTxPause,
       "cadantEtherPhyMeasRxShortOK": cadantEtherPhyMeasRxShortOK,
       "cadantEtherPhyMeasRxShortCRC": cadantEtherPhyMeasRxShortCRC,
       "cadantEtherPhyMeasRxRunt": cadantEtherPhyMeasRxRunt,
       "cadantEtherPhyMeasRxOctBad": cadantEtherPhyMeasRxOctBad,
       "cadDFIDMeasTable": cadDFIDMeasTable,
       "cadDFIDMeasEntry": cadDFIDMeasEntry,
       "cadDFIDMeasIndex": cadDFIDMeasIndex,
       "cadDFIDMeasBytsArrived": cadDFIDMeasBytsArrived,
       "cadDFIDMeasPktsArrived": cadDFIDMeasPktsArrived,
       "cadDFIDMeasBytsDropped": cadDFIDMeasBytsDropped,
       "cadDFIDMeasPktsDropped": cadDFIDMeasPktsDropped,
       "cadDFIDMeasBytsUnkDropped": cadDFIDMeasBytsUnkDropped,
       "cadDFIDMeasDFID": cadDFIDMeasDFID,
       "cadDFIDMeasPHSUnknowns": cadDFIDMeasPHSUnknowns,
       "cadDFIDMeasMacAddress": cadDFIDMeasMacAddress,
       "cadDFIDMeasSCN": cadDFIDMeasSCN,
       "cadDFIDMeasPolicedDelayPkts": cadDFIDMeasPolicedDelayPkts,
       "cadDFIDMeasGateID": cadDFIDMeasGateID,
       "cadQosPktClassMeasTable": cadQosPktClassMeasTable,
       "cadQosPktClassMeasEntry": cadQosPktClassMeasEntry,
       "cadQosPktClassMeasIfIndex": cadQosPktClassMeasIfIndex,
       "cadQosPktClassMeasSFID": cadQosPktClassMeasSFID,
       "cadQosPktClassMeasPktClassId": cadQosPktClassMeasPktClassId,
       "cadQosPktClassMeasPkts": cadQosPktClassMeasPkts,
       "cadIfMeasTable": cadIfMeasTable,
       "cadIfMeasEntry": cadIfMeasEntry,
       "cadIfInOctets": cadIfInOctets,
       "cadIfInUcastPkts": cadIfInUcastPkts,
       "cadIfInMulticastPkts": cadIfInMulticastPkts,
       "cadIfInBroadcastPkts": cadIfInBroadcastPkts,
       "cadIfInDiscards": cadIfInDiscards,
       "cadIfInErrors": cadIfInErrors,
       "cadIfInUnknownProtos": cadIfInUnknownProtos,
       "cadIfOutOctets": cadIfOutOctets,
       "cadIfOutUcastPkts": cadIfOutUcastPkts,
       "cadIfOutMulticastPkts": cadIfOutMulticastPkts,
       "cadIfOutBroadcastPkts": cadIfOutBroadcastPkts,
       "cadIfOutDiscards": cadIfOutDiscards,
       "cadIfOutErrors": cadIfOutErrors,
       "cadDCardMeasTable": cadDCardMeasTable,
       "cadDCardMeasEntry": cadDCardMeasEntry,
       "cadDCardMeasCardId": cadDCardMeasCardId,
       "cadDCardIpInReceives": cadDCardIpInReceives,
       "cadDCardIpInHdrErrors": cadDCardIpInHdrErrors,
       "cadDCardIpInAddrErrors": cadDCardIpInAddrErrors,
       "cadDCardDhcpThrottleDropPkts": cadDCardDhcpThrottleDropPkts,
       "cadDCardArpThrottleDropPkts": cadDCardArpThrottleDropPkts,
       "cadDCardDhcpV6ThrottleDropPkts": cadDCardDhcpV6ThrottleDropPkts,
       "cadDCardNdThrottleDropPkts": cadDCardNdThrottleDropPkts,
       "cadDCardIgmpThrottleDropPkts": cadDCardIgmpThrottleDropPkts,
       "cadInterfaceUtilizationTable": cadInterfaceUtilizationTable,
       "cadInterfaceUtilizationEntry": cadInterfaceUtilizationEntry,
       "cadInterfaceUtilizationDirection": cadInterfaceUtilizationDirection,
       "cadInterfaceUtilizationPercentage": cadInterfaceUtilizationPercentage,
       "cadInterfaceUtilizationAvgContSlots": cadInterfaceUtilizationAvgContSlots,
       "cadInterfaceHighResUtilizationPercentage": cadInterfaceHighResUtilizationPercentage,
       "cadInterfaceIntervalOctetsForwarded": cadInterfaceIntervalOctetsForwarded,
       "cadFftUpstreamChannelTable": cadFftUpstreamChannelTable,
       "cadFftUpstreamChannelEntry": cadFftUpstreamChannelEntry,
       "cadFftInProgress": cadFftInProgress,
       "cadFftCurrentTriggers": cadFftCurrentTriggers,
       "cadSubMgtPktFilterExtTable": cadSubMgtPktFilterExtTable,
       "cadSubMgtPktFilterExtEntry": cadSubMgtPktFilterExtEntry,
       "cadSubMgtPktFilterMatchesReset": cadSubMgtPktFilterMatchesReset,
       "cadSubMgtPktFilterLastChanged": cadSubMgtPktFilterLastChanged,
       "cadSubMgtPktFilterCaptureEnabled": cadSubMgtPktFilterCaptureEnabled,
       "cadLaesCountTable": cadLaesCountTable,
       "cadLaesCountEntry": cadLaesCountEntry,
       "cadLaesCountMacDomainIfIndex": cadLaesCountMacDomainIfIndex,
       "cadLaesCountStreamDirection": cadLaesCountStreamDirection,
       "cadLaesCountInterceptedPackets": cadLaesCountInterceptedPackets,
       "cadLaesCountInterceptDrops": cadLaesCountInterceptDrops}
)
