# SNMP MIB module (CISCO-FABRIC-C12K-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FABRIC-C12K-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:04 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

(PhysicalIndex,
 entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex",
    "entPhysicalName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoFabricC12kMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281)
)
ciscoFabricC12kMIB.setRevisions(
        ("2002-09-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CfcFabricConfigMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fullBwNonRedundant", 4),
          ("fullBwRedundant", 5),
          ("invalidMode", 1),
          ("quarterBwNonRedundant", 2),
          ("quarterBwRedundant", 3))
    )



class CfcFabricFiaState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("halted", 2))
    )



class CfcScaInterrupts(Bits, TextualConvention):
    status = "current"


class CfcSlotMask(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFabricC12kMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFabricC12kMIBNotifs = _CiscoFabricC12kMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 0)
)
_CiscoFabricC12kMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFabricC12kMIBObjects = _CiscoFabricC12kMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1)
)
_CfcGeneric_ObjectIdentity = ObjectIdentity
cfcGeneric = _CfcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1)
)
_CfcGenericGlobal_ObjectIdentity = ObjectIdentity
cfcGenericGlobal = _CfcGenericGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 1)
)
_CfcGenericGlobalFabConfigMode_Type = CfcFabricConfigMode
_CfcGenericGlobalFabConfigMode_Object = MibScalar
cfcGenericGlobalFabConfigMode = _CfcGenericGlobalFabConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 1, 1),
    _CfcGenericGlobalFabConfigMode_Type()
)
cfcGenericGlobalFabConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericGlobalFabConfigMode.setStatus("current")
_CfcGenericGlobalFabMasterSched_Type = EntPhysicalIndexOrZero
_CfcGenericGlobalFabMasterSched_Object = MibScalar
cfcGenericGlobalFabMasterSched = _CfcGenericGlobalFabMasterSched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 1, 2),
    _CfcGenericGlobalFabMasterSched_Type()
)
cfcGenericGlobalFabMasterSched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericGlobalFabMasterSched.setStatus("current")
_CfcGenericFab_ObjectIdentity = ObjectIdentity
cfcGenericFab = _CfcGenericFab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2)
)
_CfcGenericFabToFabTable_Object = MibTable
cfcGenericFabToFabTable = _CfcGenericFabToFabTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfcGenericFabToFabTable.setStatus("current")
_CfcGenericFabToFabEntry_Object = MibTableRow
cfcGenericFabToFabEntry = _CfcGenericFabToFabEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 1, 1)
)
cfcGenericFabToFabEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfcGenericFabToFabEntry.setStatus("current")
_CfcGenericFabToFabState_Type = CfcFabricFiaState
_CfcGenericFabToFabState_Object = MibTableColumn
cfcGenericFabToFabState = _CfcGenericFabToFabState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 1, 1, 1),
    _CfcGenericFabToFabState_Type()
)
cfcGenericFabToFabState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericFabToFabState.setStatus("current")
_CfcGenericFabToFabGrantPEs_Type = Counter32
_CfcGenericFabToFabGrantPEs_Object = MibTableColumn
cfcGenericFabToFabGrantPEs = _CfcGenericFabToFabGrantPEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 1, 1, 2),
    _CfcGenericFabToFabGrantPEs_Type()
)
cfcGenericFabToFabGrantPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericFabToFabGrantPEs.setStatus("current")
_CfcGenericFabToFabRequestPEs_Type = Counter32
_CfcGenericFabToFabRequestPEs_Object = MibTableColumn
cfcGenericFabToFabRequestPEs = _CfcGenericFabToFabRequestPEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 1, 1, 3),
    _CfcGenericFabToFabRequestPEs_Type()
)
cfcGenericFabToFabRequestPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericFabToFabRequestPEs.setStatus("current")
_CfcGenericFabToFabCellFifoPEs_Type = Counter32
_CfcGenericFabToFabCellFifoPEs_Object = MibTableColumn
cfcGenericFabToFabCellFifoPEs = _CfcGenericFabToFabCellFifoPEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 1, 1, 4),
    _CfcGenericFabToFabCellFifoPEs_Type()
)
cfcGenericFabToFabCellFifoPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericFabToFabCellFifoPEs.setStatus("current")
_CfcGenericFabFrFabTable_Object = MibTable
cfcGenericFabFrFabTable = _CfcGenericFabFrFabTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cfcGenericFabFrFabTable.setStatus("current")
_CfcGenericFabFrFabEntry_Object = MibTableRow
cfcGenericFabFrFabEntry = _CfcGenericFabFrFabEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 2, 1)
)
cfcGenericFabFrFabEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfcGenericFabFrFabEntry.setStatus("current")
_CfcGenericFabFrFabState_Type = CfcFabricFiaState
_CfcGenericFabFrFabState_Object = MibTableColumn
cfcGenericFabFrFabState = _CfcGenericFabFrFabState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 2, 1, 1),
    _CfcGenericFabFrFabState_Type()
)
cfcGenericFabFrFabState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericFabFrFabState.setStatus("current")
_CfcGenericFabFrFabSliTable_Object = MibTable
cfcGenericFabFrFabSliTable = _CfcGenericFabFrFabSliTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cfcGenericFabFrFabSliTable.setStatus("current")
_CfcGenericFabFrFabSliEntry_Object = MibTableRow
cfcGenericFabFrFabSliEntry = _CfcGenericFabFrFabSliEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 3, 1)
)
cfcGenericFabFrFabSliEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-FABRIC-C12K-MIB", "cfcGenericFabFrFabSliFabIndex"),
)
if mibBuilder.loadTexts:
    cfcGenericFabFrFabSliEntry.setStatus("current")
_CfcGenericFabFrFabSliFabIndex_Type = PhysicalIndex
_CfcGenericFabFrFabSliFabIndex_Object = MibTableColumn
cfcGenericFabFrFabSliFabIndex = _CfcGenericFabFrFabSliFabIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 3, 1, 1),
    _CfcGenericFabFrFabSliFabIndex_Type()
)
cfcGenericFabFrFabSliFabIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcGenericFabFrFabSliFabIndex.setStatus("current")
_CfcGenericFabFrFabSliLOSErrors_Type = Counter32
_CfcGenericFabFrFabSliLOSErrors_Object = MibTableColumn
cfcGenericFabFrFabSliLOSErrors = _CfcGenericFabFrFabSliLOSErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 3, 1, 2),
    _CfcGenericFabFrFabSliLOSErrors_Type()
)
cfcGenericFabFrFabSliLOSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericFabFrFabSliLOSErrors.setStatus("current")
_CfcGenericFabFrFabSliCRCErrors_Type = Counter32
_CfcGenericFabFrFabSliCRCErrors_Object = MibTableColumn
cfcGenericFabFrFabSliCRCErrors = _CfcGenericFabFrFabSliCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 3, 1, 3),
    _CfcGenericFabFrFabSliCRCErrors_Type()
)
cfcGenericFabFrFabSliCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericFabFrFabSliCRCErrors.setStatus("current")


class _CfcGenericFabFrFabSliLOSState_Type(Integer32):
    """Custom type cfcGenericFabFrFabSliLOSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("losOff", 1),
          ("losOn", 2))
    )


_CfcGenericFabFrFabSliLOSState_Type.__name__ = "Integer32"
_CfcGenericFabFrFabSliLOSState_Object = MibTableColumn
cfcGenericFabFrFabSliLOSState = _CfcGenericFabFrFabSliLOSState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 2, 3, 1, 4),
    _CfcGenericFabFrFabSliLOSState_Type()
)
cfcGenericFabFrFabSliLOSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericFabFrFabSliLOSState.setStatus("current")
_CfcGenericSca_ObjectIdentity = ObjectIdentity
cfcGenericSca = _CfcGenericSca_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3)
)
_CfcGenericScaTable_Object = MibTable
cfcGenericScaTable = _CfcGenericScaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cfcGenericScaTable.setStatus("current")
_CfcGenericScaEntry_Object = MibTableRow
cfcGenericScaEntry = _CfcGenericScaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3, 1, 1)
)
cfcGenericScaEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfcGenericScaEntry.setStatus("current")
_CfcGenericScaIdentifier_Type = SnmpAdminString
_CfcGenericScaIdentifier_Object = MibTableColumn
cfcGenericScaIdentifier = _CfcGenericScaIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3, 1, 1, 1),
    _CfcGenericScaIdentifier_Type()
)
cfcGenericScaIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericScaIdentifier.setStatus("current")
_CfcGenericScaIntrStatus_Type = CfcScaInterrupts
_CfcGenericScaIntrStatus_Object = MibTableColumn
cfcGenericScaIntrStatus = _CfcGenericScaIntrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3, 1, 1, 2),
    _CfcGenericScaIntrStatus_Type()
)
cfcGenericScaIntrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericScaIntrStatus.setStatus("current")
_CfcGenericScaIntrsEnabled_Type = CfcScaInterrupts
_CfcGenericScaIntrsEnabled_Object = MibTableColumn
cfcGenericScaIntrsEnabled = _CfcGenericScaIntrsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3, 1, 1, 3),
    _CfcGenericScaIntrsEnabled_Type()
)
cfcGenericScaIntrsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericScaIntrsEnabled.setStatus("current")


class _CfcGenericScaConfig_Type(Bits):
    """Custom type cfcGenericScaConfig based on Bits"""
    namedValues = NamedValues(
        *(("earlyIntrOnLOS", 7),
          ("enableParity", 3),
          ("forceGrantParityXer", 10),
          ("forceXbarCrcOnCtlLink0", 12),
          ("forceXbarCrcOnCtlLink1", 13),
          ("forceXbarCrcOnCtlLink2", 14),
          ("forceXbarCrcOnCtlLink3", 15),
          ("forceXbarParityXer", 9),
          ("fullBandwidth", 2),
          ("halfBandwidth", 1),
          ("noEarlyIntrOnLOS", 8),
          ("priAlternating", 6),
          ("priMcast", 4),
          ("priUnicast", 5),
          ("quarterBandwidth", 0),
          ("unicastAcceptMode", 11))
    )

_CfcGenericScaConfig_Type.__name__ = "Bits"
_CfcGenericScaConfig_Object = MibTableColumn
cfcGenericScaConfig = _CfcGenericScaConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3, 1, 1, 4),
    _CfcGenericScaConfig_Type()
)
cfcGenericScaConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericScaConfig.setStatus("current")
_CfcGenericScaPELog_Type = CfcSlotMask
_CfcGenericScaPELog_Object = MibTableColumn
cfcGenericScaPELog = _CfcGenericScaPELog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3, 1, 1, 5),
    _CfcGenericScaPELog_Type()
)
cfcGenericScaPELog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericScaPELog.setStatus("current")
_CfcGenericScaFifoOverflowLog_Type = CfcSlotMask
_CfcGenericScaFifoOverflowLog_Object = MibTableColumn
cfcGenericScaFifoOverflowLog = _CfcGenericScaFifoOverflowLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3, 1, 1, 6),
    _CfcGenericScaFifoOverflowLog_Type()
)
cfcGenericScaFifoOverflowLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericScaFifoOverflowLog.setStatus("current")
_CfcGenericScaLCsEnabled_Type = CfcSlotMask
_CfcGenericScaLCsEnabled_Object = MibTableColumn
cfcGenericScaLCsEnabled = _CfcGenericScaLCsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3, 1, 1, 7),
    _CfcGenericScaLCsEnabled_Type()
)
cfcGenericScaLCsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericScaLCsEnabled.setStatus("current")
_CfcGenericScaForcedBackPressure_Type = CfcSlotMask
_CfcGenericScaForcedBackPressure_Object = MibTableColumn
cfcGenericScaForcedBackPressure = _CfcGenericScaForcedBackPressure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3, 1, 1, 8),
    _CfcGenericScaForcedBackPressure_Type()
)
cfcGenericScaForcedBackPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericScaForcedBackPressure.setStatus("current")
_CfcGenericScaOc192LCsPresent_Type = CfcSlotMask
_CfcGenericScaOc192LCsPresent_Object = MibTableColumn
cfcGenericScaOc192LCsPresent = _CfcGenericScaOc192LCsPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3, 1, 1, 9),
    _CfcGenericScaOc192LCsPresent_Type()
)
cfcGenericScaOc192LCsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericScaOc192LCsPresent.setStatus("current")
_CfcGenericScaPreOc192LCsPresent_Type = CfcSlotMask
_CfcGenericScaPreOc192LCsPresent_Object = MibTableColumn
cfcGenericScaPreOc192LCsPresent = _CfcGenericScaPreOc192LCsPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 3, 1, 1, 10),
    _CfcGenericScaPreOc192LCsPresent_Type()
)
cfcGenericScaPreOc192LCsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericScaPreOc192LCsPresent.setStatus("current")
_CfcGenericXbar_ObjectIdentity = ObjectIdentity
cfcGenericXbar = _CfcGenericXbar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 4)
)
_CfcGenericXbarTable_Object = MibTable
cfcGenericXbarTable = _CfcGenericXbarTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cfcGenericXbarTable.setStatus("current")
_CfcGenericXbarEntry_Object = MibTableRow
cfcGenericXbarEntry = _CfcGenericXbarEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 4, 1, 1)
)
cfcGenericXbarEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfcGenericXbarEntry.setStatus("current")
_CfcGenericXbarIdentifier_Type = SnmpAdminString
_CfcGenericXbarIdentifier_Object = MibTableColumn
cfcGenericXbarIdentifier = _CfcGenericXbarIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 1, 4, 1, 1, 1),
    _CfcGenericXbarIdentifier_Type()
)
cfcGenericXbarIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcGenericXbarIdentifier.setStatus("current")
_CfcPreOc192_ObjectIdentity = ObjectIdentity
cfcPreOc192 = _CfcPreOc192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2)
)
_CfcPreOc192Fab_ObjectIdentity = ObjectIdentity
cfcPreOc192Fab = _CfcPreOc192Fab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1)
)
_CfcPreOc192FabToFabTable_Object = MibTable
cfcPreOc192FabToFabTable = _CfcPreOc192FabToFabTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cfcPreOc192FabToFabTable.setStatus("current")
_CfcPreOc192FabToFabEntry_Object = MibTableRow
cfcPreOc192FabToFabEntry = _CfcPreOc192FabToFabEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 1, 1)
)
cfcPreOc192FabToFabEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfcPreOc192FabToFabEntry.setStatus("current")
_CfcPreOc192FabToFabScaLosts_Type = Counter32
_CfcPreOc192FabToFabScaLosts_Object = MibTableColumn
cfcPreOc192FabToFabScaLosts = _CfcPreOc192FabToFabScaLosts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 1, 1, 1),
    _CfcPreOc192FabToFabScaLosts_Type()
)
cfcPreOc192FabToFabScaLosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabToFabScaLosts.setStatus("current")
_CfcPreOc192FabToFabUCFifoOvFlws_Type = Counter32
_CfcPreOc192FabToFabUCFifoOvFlws_Object = MibTableColumn
cfcPreOc192FabToFabUCFifoOvFlws = _CfcPreOc192FabToFabUCFifoOvFlws_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 1, 1, 2),
    _CfcPreOc192FabToFabUCFifoOvFlws_Type()
)
cfcPreOc192FabToFabUCFifoOvFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabToFabUCFifoOvFlws.setStatus("current")
_CfcPreOc192FabToFabUCFifoUnFlws_Type = Counter32
_CfcPreOc192FabToFabUCFifoUnFlws_Object = MibTableColumn
cfcPreOc192FabToFabUCFifoUnFlws = _CfcPreOc192FabToFabUCFifoUnFlws_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 1, 1, 3),
    _CfcPreOc192FabToFabUCFifoUnFlws_Type()
)
cfcPreOc192FabToFabUCFifoUnFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabToFabUCFifoUnFlws.setStatus("current")
_CfcPreOc192FabToFabMCFifoErrs_Type = Counter32
_CfcPreOc192FabToFabMCFifoErrs_Object = MibTableColumn
cfcPreOc192FabToFabMCFifoErrs = _CfcPreOc192FabToFabMCFifoErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 1, 1, 4),
    _CfcPreOc192FabToFabMCFifoErrs_Type()
)
cfcPreOc192FabToFabMCFifoErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabToFabMCFifoErrs.setStatus("current")
_CfcPreOc192FabToFabBmaPEs_Type = Counter32
_CfcPreOc192FabToFabBmaPEs_Object = MibTableColumn
cfcPreOc192FabToFabBmaPEs = _CfcPreOc192FabToFabBmaPEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 1, 1, 5),
    _CfcPreOc192FabToFabBmaPEs_Type()
)
cfcPreOc192FabToFabBmaPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabToFabBmaPEs.setStatus("current")
_CfcPreOc192FabToFabBmaHskErrs_Type = Counter32
_CfcPreOc192FabToFabBmaHskErrs_Object = MibTableColumn
cfcPreOc192FabToFabBmaHskErrs = _CfcPreOc192FabToFabBmaHskErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 1, 1, 6),
    _CfcPreOc192FabToFabBmaHskErrs_Type()
)
cfcPreOc192FabToFabBmaHskErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabToFabBmaHskErrs.setStatus("current")
_CfcPreOc192FabToFabUniDestMCRqs_Type = Counter32
_CfcPreOc192FabToFabUniDestMCRqs_Object = MibTableColumn
cfcPreOc192FabToFabUniDestMCRqs = _CfcPreOc192FabToFabUniDestMCRqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 1, 1, 7),
    _CfcPreOc192FabToFabUniDestMCRqs_Type()
)
cfcPreOc192FabToFabUniDestMCRqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabToFabUniDestMCRqs.setStatus("current")
_CfcPreOc192FabToFabMultiDstUCRqs_Type = Counter32
_CfcPreOc192FabToFabMultiDstUCRqs_Object = MibTableColumn
cfcPreOc192FabToFabMultiDstUCRqs = _CfcPreOc192FabToFabMultiDstUCRqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 1, 1, 8),
    _CfcPreOc192FabToFabMultiDstUCRqs_Type()
)
cfcPreOc192FabToFabMultiDstUCRqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabToFabMultiDstUCRqs.setStatus("current")
_CfcPreOc192FabToFabEmptyDestRqs_Type = Counter32
_CfcPreOc192FabToFabEmptyDestRqs_Object = MibTableColumn
cfcPreOc192FabToFabEmptyDestRqs = _CfcPreOc192FabToFabEmptyDestRqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 1, 1, 9),
    _CfcPreOc192FabToFabEmptyDestRqs_Type()
)
cfcPreOc192FabToFabEmptyDestRqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabToFabEmptyDestRqs.setStatus("current")
_CfcPreOc192FabFrFabTable_Object = MibTable
cfcPreOc192FabFrFabTable = _CfcPreOc192FabFrFabTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cfcPreOc192FabFrFabTable.setStatus("current")
_CfcPreOc192FabFrFabEntry_Object = MibTableRow
cfcPreOc192FabFrFabEntry = _CfcPreOc192FabFrFabEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 2, 1)
)
cfcPreOc192FabFrFabEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfcPreOc192FabFrFabEntry.setStatus("current")
_CfcPreOc192FabFrFabCellFifoPEs_Type = Counter32
_CfcPreOc192FabFrFabCellFifoPEs_Object = MibTableColumn
cfcPreOc192FabFrFabCellFifoPEs = _CfcPreOc192FabFrFabCellFifoPEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 2, 1, 1),
    _CfcPreOc192FabFrFabCellFifoPEs_Type()
)
cfcPreOc192FabFrFabCellFifoPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabFrFabCellFifoPEs.setStatus("current")
_CfcPreOc192FabFrFabRedFifoPEs_Type = Counter32
_CfcPreOc192FabFrFabRedFifoPEs_Object = MibTableColumn
cfcPreOc192FabFrFabRedFifoPEs = _CfcPreOc192FabFrFabRedFifoPEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 2, 1, 2),
    _CfcPreOc192FabFrFabRedFifoPEs_Type()
)
cfcPreOc192FabFrFabRedFifoPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabFrFabRedFifoPEs.setStatus("current")
_CfcPreOc192FabFrFabRedFifoOvflws_Type = Counter32
_CfcPreOc192FabFrFabRedFifoOvflws_Object = MibTableColumn
cfcPreOc192FabFrFabRedFifoOvflws = _CfcPreOc192FabFrFabRedFifoOvflws_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 2, 1, 3),
    _CfcPreOc192FabFrFabRedFifoOvflws_Type()
)
cfcPreOc192FabFrFabRedFifoOvflws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabFrFabRedFifoOvflws.setStatus("current")
_CfcPreOc192FabFrFabCellDrops_Type = Counter32
_CfcPreOc192FabFrFabCellDrops_Object = MibTableColumn
cfcPreOc192FabFrFabCellDrops = _CfcPreOc192FabFrFabCellDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 1, 2, 1, 4),
    _CfcPreOc192FabFrFabCellDrops_Type()
)
cfcPreOc192FabFrFabCellDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192FabFrFabCellDrops.setStatus("current")
_CfcPreOc192Sca_ObjectIdentity = ObjectIdentity
cfcPreOc192Sca = _CfcPreOc192Sca_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 2)
)
_CfcPreOc192ScaTable_Object = MibTable
cfcPreOc192ScaTable = _CfcPreOc192ScaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cfcPreOc192ScaTable.setStatus("current")
_CfcPreOc192ScaEntry_Object = MibTableRow
cfcPreOc192ScaEntry = _CfcPreOc192ScaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 2, 1, 1)
)
cfcPreOc192ScaEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfcPreOc192ScaEntry.setStatus("current")
_CfcPreOc192ScaReSyncDelay_Type = Unsigned32
_CfcPreOc192ScaReSyncDelay_Object = MibTableColumn
cfcPreOc192ScaReSyncDelay = _CfcPreOc192ScaReSyncDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 2, 1, 1, 1),
    _CfcPreOc192ScaReSyncDelay_Type()
)
cfcPreOc192ScaReSyncDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192ScaReSyncDelay.setStatus("current")
_CfcPreOc192ScaLOSLog_Type = CfcSlotMask
_CfcPreOc192ScaLOSLog_Object = MibTableColumn
cfcPreOc192ScaLOSLog = _CfcPreOc192ScaLOSLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 2, 1, 1, 2),
    _CfcPreOc192ScaLOSLog_Type()
)
cfcPreOc192ScaLOSLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192ScaLOSLog.setStatus("current")
_CfcPreOc192Xbar_ObjectIdentity = ObjectIdentity
cfcPreOc192Xbar = _CfcPreOc192Xbar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 3)
)
_CfcPreOc192XbarTable_Object = MibTable
cfcPreOc192XbarTable = _CfcPreOc192XbarTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cfcPreOc192XbarTable.setStatus("current")
_CfcPreOc192XbarEntry_Object = MibTableRow
cfcPreOc192XbarEntry = _CfcPreOc192XbarEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 3, 1, 1)
)
cfcPreOc192XbarEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfcPreOc192XbarEntry.setStatus("current")


class _CfcPreOc192XbarIntrStatus_Type(Bits):
    """Custom type cfcPreOc192XbarIntrStatus based on Bits"""
    namedValues = NamedValues(
        *(("frameLossOfSync", 0),
          ("parityErrorFromSca", 1))
    )

_CfcPreOc192XbarIntrStatus_Type.__name__ = "Bits"
_CfcPreOc192XbarIntrStatus_Object = MibTableColumn
cfcPreOc192XbarIntrStatus = _CfcPreOc192XbarIntrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 3, 1, 1, 1),
    _CfcPreOc192XbarIntrStatus_Type()
)
cfcPreOc192XbarIntrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192XbarIntrStatus.setStatus("current")
_CfcPreOc192XbarParityChkStatus_Type = TruthValue
_CfcPreOc192XbarParityChkStatus_Object = MibTableColumn
cfcPreOc192XbarParityChkStatus = _CfcPreOc192XbarParityChkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 2, 3, 1, 1, 2),
    _CfcPreOc192XbarParityChkStatus_Type()
)
cfcPreOc192XbarParityChkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcPreOc192XbarParityChkStatus.setStatus("current")
_CfcOc192_ObjectIdentity = ObjectIdentity
cfcOc192 = _CfcOc192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3)
)
_CfcOc192Fab_ObjectIdentity = ObjectIdentity
cfcOc192Fab = _CfcOc192Fab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1)
)
_CfcOc192FabToFabTable_Object = MibTable
cfcOc192FabToFabTable = _CfcOc192FabToFabTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cfcOc192FabToFabTable.setStatus("current")
_CfcOc192FabToFabEntry_Object = MibTableRow
cfcOc192FabToFabEntry = _CfcOc192FabToFabEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 1, 1)
)
cfcOc192FabToFabEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfcOc192FabToFabEntry.setStatus("current")
_CfcOc192FabToFabMccDataPEs_Type = Counter32
_CfcOc192FabToFabMccDataPEs_Object = MibTableColumn
cfcOc192FabToFabMccDataPEs = _CfcOc192FabToFabMccDataPEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 1, 1, 1),
    _CfcOc192FabToFabMccDataPEs_Type()
)
cfcOc192FabToFabMccDataPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabToFabMccDataPEs.setStatus("current")
_CfcOc192FabToFabMccCmdPEs_Type = Counter32
_CfcOc192FabToFabMccCmdPEs_Object = MibTableColumn
cfcOc192FabToFabMccCmdPEs = _CfcOc192FabToFabMccCmdPEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 1, 1, 2),
    _CfcOc192FabToFabMccCmdPEs_Type()
)
cfcOc192FabToFabMccCmdPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabToFabMccCmdPEs.setStatus("current")
_CfcOc192FabToFabBackPressurePEs_Type = Counter32
_CfcOc192FabToFabBackPressurePEs_Object = MibTableColumn
cfcOc192FabToFabBackPressurePEs = _CfcOc192FabToFabBackPressurePEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 1, 1, 3),
    _CfcOc192FabToFabBackPressurePEs_Type()
)
cfcOc192FabToFabBackPressurePEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabToFabBackPressurePEs.setStatus("current")
_CfcOc192FabToFabCellFifoOvFlws_Type = Counter32
_CfcOc192FabToFabCellFifoOvFlws_Object = MibTableColumn
cfcOc192FabToFabCellFifoOvFlws = _CfcOc192FabToFabCellFifoOvFlws_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 1, 1, 4),
    _CfcOc192FabToFabCellFifoOvFlws_Type()
)
cfcOc192FabToFabCellFifoOvFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabToFabCellFifoOvFlws.setStatus("current")
_CfcOc192FabToFabCellFifoUnFlws_Type = Counter32
_CfcOc192FabToFabCellFifoUnFlws_Object = MibTableColumn
cfcOc192FabToFabCellFifoUnFlws = _CfcOc192FabToFabCellFifoUnFlws_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 1, 1, 5),
    _CfcOc192FabToFabCellFifoUnFlws_Type()
)
cfcOc192FabToFabCellFifoUnFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabToFabCellFifoUnFlws.setStatus("current")
_CfcOc192FabToFabMccCmdSeqEndErrs_Type = Counter32
_CfcOc192FabToFabMccCmdSeqEndErrs_Object = MibTableColumn
cfcOc192FabToFabMccCmdSeqEndErrs = _CfcOc192FabToFabMccCmdSeqEndErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 1, 1, 6),
    _CfcOc192FabToFabMccCmdSeqEndErrs_Type()
)
cfcOc192FabToFabMccCmdSeqEndErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabToFabMccCmdSeqEndErrs.setStatus("current")
_CfcOc192FabToFabMccCmdSeqStrErrs_Type = Counter32
_CfcOc192FabToFabMccCmdSeqStrErrs_Object = MibTableColumn
cfcOc192FabToFabMccCmdSeqStrErrs = _CfcOc192FabToFabMccCmdSeqStrErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 1, 1, 7),
    _CfcOc192FabToFabMccCmdSeqStrErrs_Type()
)
cfcOc192FabToFabMccCmdSeqStrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabToFabMccCmdSeqStrErrs.setStatus("current")
_CfcOc192FabFrFabTable_Object = MibTable
cfcOc192FabFrFabTable = _CfcOc192FabFrFabTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cfcOc192FabFrFabTable.setStatus("current")
_CfcOc192FabFrFabEntry_Object = MibTableRow
cfcOc192FabFrFabEntry = _CfcOc192FabFrFabEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 2, 1)
)
cfcOc192FabFrFabEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfcOc192FabFrFabEntry.setStatus("current")
_CfcOc192FabFrFabPktLenErrs_Type = Counter32
_CfcOc192FabFrFabPktLenErrs_Object = MibTableColumn
cfcOc192FabFrFabPktLenErrs = _CfcOc192FabFrFabPktLenErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 2, 1, 1),
    _CfcOc192FabFrFabPktLenErrs_Type()
)
cfcOc192FabFrFabPktLenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabPktLenErrs.setStatus("current")
_CfcOc192FabFrFabExtRamPEs_Type = Counter32
_CfcOc192FabFrFabExtRamPEs_Object = MibTableColumn
cfcOc192FabFrFabExtRamPEs = _CfcOc192FabFrFabExtRamPEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 2, 1, 2),
    _CfcOc192FabFrFabExtRamPEs_Type()
)
cfcOc192FabFrFabExtRamPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabExtRamPEs.setStatus("current")
_CfcOc192FabFrFabPktLenPEs_Type = Counter32
_CfcOc192FabFrFabPktLenPEs_Object = MibTableColumn
cfcOc192FabFrFabPktLenPEs = _CfcOc192FabFrFabPktLenPEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 2, 1, 3),
    _CfcOc192FabFrFabPktLenPEs_Type()
)
cfcOc192FabFrFabPktLenPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabPktLenPEs.setStatus("current")
_CfcOc192FabFrFabHdrSramPEs_Type = Counter32
_CfcOc192FabFrFabHdrSramPEs_Object = MibTableColumn
cfcOc192FabFrFabHdrSramPEs = _CfcOc192FabFrFabHdrSramPEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 2, 1, 4),
    _CfcOc192FabFrFabHdrSramPEs_Type()
)
cfcOc192FabFrFabHdrSramPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabHdrSramPEs.setStatus("current")
_CfcOc192FabFrFabTxCtrlPEs_Type = Counter32
_CfcOc192FabFrFabTxCtrlPEs_Object = MibTableColumn
cfcOc192FabFrFabTxCtrlPEs = _CfcOc192FabFrFabTxCtrlPEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 2, 1, 5),
    _CfcOc192FabFrFabTxCtrlPEs_Type()
)
cfcOc192FabFrFabTxCtrlPEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabTxCtrlPEs.setStatus("current")
_CfcOc192FabFrFabHdrFifoOvFlws_Type = Counter32
_CfcOc192FabFrFabHdrFifoOvFlws_Object = MibTableColumn
cfcOc192FabFrFabHdrFifoOvFlws = _CfcOc192FabFrFabHdrFifoOvFlws_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 2, 1, 6),
    _CfcOc192FabFrFabHdrFifoOvFlws_Type()
)
cfcOc192FabFrFabHdrFifoOvFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabHdrFifoOvFlws.setStatus("current")
_CfcOc192FabFrFabExtSramOvFlws_Type = Counter32
_CfcOc192FabFrFabExtSramOvFlws_Object = MibTableColumn
cfcOc192FabFrFabExtSramOvFlws = _CfcOc192FabFrFabExtSramOvFlws_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 2, 1, 7),
    _CfcOc192FabFrFabExtSramOvFlws_Type()
)
cfcOc192FabFrFabExtSramOvFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabExtSramOvFlws.setStatus("current")
_CfcOc192FabFrFabFirstLastErrs_Type = Counter32
_CfcOc192FabFrFabFirstLastErrs_Object = MibTableColumn
cfcOc192FabFrFabFirstLastErrs = _CfcOc192FabFrFabFirstLastErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 2, 1, 8),
    _CfcOc192FabFrFabFirstLastErrs_Type()
)
cfcOc192FabFrFabFirstLastErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabFirstLastErrs.setStatus("current")
_CfcOc192FabFrFabSeqErrs_Type = Counter32
_CfcOc192FabFrFabSeqErrs_Object = MibTableColumn
cfcOc192FabFrFabSeqErrs = _CfcOc192FabFrFabSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 2, 1, 9),
    _CfcOc192FabFrFabSeqErrs_Type()
)
cfcOc192FabFrFabSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabSeqErrs.setStatus("current")
_CfcOc192FabFrFabSliTable_Object = MibTable
cfcOc192FabFrFabSliTable = _CfcOc192FabFrFabSliTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cfcOc192FabFrFabSliTable.setStatus("current")
_CfcOc192FabFrFabSliEntry_Object = MibTableRow
cfcOc192FabFrFabSliEntry = _CfcOc192FabFrFabSliEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 3, 1)
)
cfcOc192FabFrFabSliEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabSliSwitchIndex"),
)
if mibBuilder.loadTexts:
    cfcOc192FabFrFabSliEntry.setStatus("current")
_CfcOc192FabFrFabSliSwitchIndex_Type = PhysicalIndex
_CfcOc192FabFrFabSliSwitchIndex_Object = MibTableColumn
cfcOc192FabFrFabSliSwitchIndex = _CfcOc192FabFrFabSliSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 3, 1, 1),
    _CfcOc192FabFrFabSliSwitchIndex_Type()
)
cfcOc192FabFrFabSliSwitchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabSliSwitchIndex.setStatus("current")
_CfcOc192FabFrFabSliXorErrs_Type = Counter32
_CfcOc192FabFrFabSliXorErrs_Object = MibTableColumn
cfcOc192FabFrFabSliXorErrs = _CfcOc192FabFrFabSliXorErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 3, 1, 2),
    _CfcOc192FabFrFabSliXorErrs_Type()
)
cfcOc192FabFrFabSliXorErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabSliXorErrs.setStatus("current")
_CfcOc192FabFrFabSliCellDrops_Type = Counter32
_CfcOc192FabFrFabSliCellDrops_Object = MibTableColumn
cfcOc192FabFrFabSliCellDrops = _CfcOc192FabFrFabSliCellDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 3, 1, 3),
    _CfcOc192FabFrFabSliCellDrops_Type()
)
cfcOc192FabFrFabSliCellDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabSliCellDrops.setStatus("current")
_CfcOc192FabFrFabStatTable_Object = MibTable
cfcOc192FabFrFabStatTable = _CfcOc192FabFrFabStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cfcOc192FabFrFabStatTable.setStatus("current")
_CfcOc192FabFrFabStatEntry_Object = MibTableRow
cfcOc192FabFrFabStatEntry = _CfcOc192FabFrFabStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 4, 1)
)
cfcOc192FabFrFabStatEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabStatLCIndex"),
)
if mibBuilder.loadTexts:
    cfcOc192FabFrFabStatEntry.setStatus("current")
_CfcOc192FabFrFabStatLCIndex_Type = PhysicalIndex
_CfcOc192FabFrFabStatLCIndex_Object = MibTableColumn
cfcOc192FabFrFabStatLCIndex = _CfcOc192FabFrFabStatLCIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 4, 1, 1),
    _CfcOc192FabFrFabStatLCIndex_Type()
)
cfcOc192FabFrFabStatLCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabStatLCIndex.setStatus("current")
_CfcOc192FabFrFabStatUCHiPktDrops_Type = Counter32
_CfcOc192FabFrFabStatUCHiPktDrops_Object = MibTableColumn
cfcOc192FabFrFabStatUCHiPktDrops = _CfcOc192FabFrFabStatUCHiPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 4, 1, 2),
    _CfcOc192FabFrFabStatUCHiPktDrops_Type()
)
cfcOc192FabFrFabStatUCHiPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabStatUCHiPktDrops.setStatus("current")
_CfcOc192FabFrFabStatUCLoPktDrops_Type = Counter32
_CfcOc192FabFrFabStatUCLoPktDrops_Object = MibTableColumn
cfcOc192FabFrFabStatUCLoPktDrops = _CfcOc192FabFrFabStatUCLoPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 4, 1, 3),
    _CfcOc192FabFrFabStatUCLoPktDrops_Type()
)
cfcOc192FabFrFabStatUCLoPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabStatUCLoPktDrops.setStatus("current")
_CfcOc192FabFrFabStatMCHiPktDrops_Type = Counter32
_CfcOc192FabFrFabStatMCHiPktDrops_Object = MibTableColumn
cfcOc192FabFrFabStatMCHiPktDrops = _CfcOc192FabFrFabStatMCHiPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 4, 1, 4),
    _CfcOc192FabFrFabStatMCHiPktDrops_Type()
)
cfcOc192FabFrFabStatMCHiPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabStatMCHiPktDrops.setStatus("current")
_CfcOc192FabFrFabStatMCLoPktDrops_Type = Counter32
_CfcOc192FabFrFabStatMCLoPktDrops_Object = MibTableColumn
cfcOc192FabFrFabStatMCLoPktDrops = _CfcOc192FabFrFabStatMCLoPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 1, 4, 1, 5),
    _CfcOc192FabFrFabStatMCLoPktDrops_Type()
)
cfcOc192FabFrFabStatMCLoPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192FabFrFabStatMCLoPktDrops.setStatus("current")
_CfcOc192Sca_ObjectIdentity = ObjectIdentity
cfcOc192Sca = _CfcOc192Sca_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 2)
)
_CfcOc192ScaTable_Object = MibTable
cfcOc192ScaTable = _CfcOc192ScaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cfcOc192ScaTable.setStatus("current")
_CfcOc192ScaEntry_Object = MibTableRow
cfcOc192ScaEntry = _CfcOc192ScaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 2, 1, 1)
)
cfcOc192ScaEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfcOc192ScaEntry.setStatus("current")
_CfcOc192ScaRotationPeriod_Type = Unsigned32
_CfcOc192ScaRotationPeriod_Object = MibTableColumn
cfcOc192ScaRotationPeriod = _CfcOc192ScaRotationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 2, 1, 1, 1),
    _CfcOc192ScaRotationPeriod_Type()
)
cfcOc192ScaRotationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192ScaRotationPeriod.setStatus("current")
_CfcOc192ScaDisableGrants_Type = CfcSlotMask
_CfcOc192ScaDisableGrants_Object = MibTableColumn
cfcOc192ScaDisableGrants = _CfcOc192ScaDisableGrants_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 2, 1, 1, 2),
    _CfcOc192ScaDisableGrants_Type()
)
cfcOc192ScaDisableGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192ScaDisableGrants.setStatus("current")
_CfcOc192Xbar_ObjectIdentity = ObjectIdentity
cfcOc192Xbar = _CfcOc192Xbar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 3)
)
_CfcOc192XbarTable_Object = MibTable
cfcOc192XbarTable = _CfcOc192XbarTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cfcOc192XbarTable.setStatus("current")
_CfcOc192XbarEntry_Object = MibTableRow
cfcOc192XbarEntry = _CfcOc192XbarEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 3, 1, 1)
)
cfcOc192XbarEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cfcOc192XbarEntry.setStatus("current")


class _CfcOc192XbarCtrlLOSStatus_Type(Bits):
    """Custom type cfcOc192XbarCtrlLOSStatus based on Bits"""
    namedValues = NamedValues(
        *(("frameLosErr", 0),
          ("sliErrorOnControlLink0", 1),
          ("sliErrorOnControlLink1", 2),
          ("sliErrorOnControlLink2", 3),
          ("sliErrorOnControlLink3", 4))
    )

_CfcOc192XbarCtrlLOSStatus_Type.__name__ = "Bits"
_CfcOc192XbarCtrlLOSStatus_Object = MibTableColumn
cfcOc192XbarCtrlLOSStatus = _CfcOc192XbarCtrlLOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 3, 1, 1, 1),
    _CfcOc192XbarCtrlLOSStatus_Type()
)
cfcOc192XbarCtrlLOSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192XbarCtrlLOSStatus.setStatus("current")


class _CfcOc192XbarCtrlCRCErr_Type(Bits):
    """Custom type cfcOc192XbarCtrlCRCErr based on Bits"""
    namedValues = NamedValues(
        *(("ctlCrcErrorLink0", 0),
          ("ctlCrcErrorLink1", 1),
          ("ctlCrcErrorLink2", 2),
          ("ctlCrcErrorLink3", 3))
    )

_CfcOc192XbarCtrlCRCErr_Type.__name__ = "Bits"
_CfcOc192XbarCtrlCRCErr_Object = MibTableColumn
cfcOc192XbarCtrlCRCErr = _CfcOc192XbarCtrlCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 3, 3, 1, 1, 2),
    _CfcOc192XbarCtrlCRCErr_Type()
)
cfcOc192XbarCtrlCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcOc192XbarCtrlCRCErr.setStatus("current")
_CfcNotif_ObjectIdentity = ObjectIdentity
cfcNotif = _CfcNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 4)
)


class _CfcNotifEnable_Type(TruthValue):
    """Custom type cfcNotifEnable based on TruthValue"""


_CfcNotifEnable_Object = MibScalar
cfcNotifEnable = _CfcNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 1, 4, 1),
    _CfcNotifEnable_Type()
)
cfcNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcNotifEnable.setStatus("current")
_CiscoFabricC12kMIBConform_ObjectIdentity = ObjectIdentity
ciscoFabricC12kMIBConform = _CiscoFabricC12kMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2)
)
_CiscoFabricC12kMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFabricC12kMIBCompliances = _CiscoFabricC12kMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 1)
)
_CiscoFabricC12kMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFabricC12kMIBGroups = _CiscoFabricC12kMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2)
)

# Managed Objects groups

ciscoFabricC12kGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 1)
)
ciscoFabricC12kGlobalGroup.setObjects(
      *(("CISCO-FABRIC-C12K-MIB", "cfcGenericGlobalFabConfigMode"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericGlobalFabMasterSched"))
)
if mibBuilder.loadTexts:
    ciscoFabricC12kGlobalGroup.setStatus("current")

ciscoFabricC12kFiaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 2)
)
ciscoFabricC12kFiaGroup.setObjects(
      *(("CISCO-FABRIC-C12K-MIB", "cfcGenericFabToFabState"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericFabToFabGrantPEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericFabToFabRequestPEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericFabToFabCellFifoPEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericFabFrFabState"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericFabFrFabSliLOSErrors"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericFabFrFabSliCRCErrors"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericFabFrFabSliLOSState"))
)
if mibBuilder.loadTexts:
    ciscoFabricC12kFiaGroup.setStatus("current")

ciscoFabricC12kScaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 3)
)
ciscoFabricC12kScaGroup.setObjects(
      *(("CISCO-FABRIC-C12K-MIB", "cfcGenericScaIdentifier"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericScaIntrStatus"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericScaIntrsEnabled"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericScaConfig"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericScaPELog"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericScaFifoOverflowLog"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericScaLCsEnabled"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericScaForcedBackPressure"),
        ("CISCO-FABRIC-C12K-MIB", "cfcGenericScaPreOc192LCsPresent"))
)
if mibBuilder.loadTexts:
    ciscoFabricC12kScaGroup.setStatus("current")

ciscoFabricC12kXbarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 4)
)
ciscoFabricC12kXbarGroup.setObjects(
    ("CISCO-FABRIC-C12K-MIB", "cfcGenericXbarIdentifier")
)
if mibBuilder.loadTexts:
    ciscoFabricC12kXbarGroup.setStatus("current")

ciscoFabricC12kPreOc192FiaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 5)
)
ciscoFabricC12kPreOc192FiaGroup.setObjects(
      *(("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabToFabScaLosts"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabToFabUCFifoOvFlws"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabToFabUCFifoUnFlws"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabToFabMCFifoErrs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabToFabBmaPEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabToFabBmaHskErrs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabToFabUniDestMCRqs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabToFabMultiDstUCRqs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabToFabEmptyDestRqs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabFrFabCellFifoPEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabFrFabRedFifoPEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabFrFabRedFifoOvflws"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192FabFrFabCellDrops"))
)
if mibBuilder.loadTexts:
    ciscoFabricC12kPreOc192FiaGroup.setStatus("current")

ciscoFabricC12kPreOc192ScaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 6)
)
ciscoFabricC12kPreOc192ScaGroup.setObjects(
      *(("CISCO-FABRIC-C12K-MIB", "cfcPreOc192ScaReSyncDelay"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192ScaLOSLog"))
)
if mibBuilder.loadTexts:
    ciscoFabricC12kPreOc192ScaGroup.setStatus("current")

ciscoFabricC12kPreOc192XbarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 7)
)
ciscoFabricC12kPreOc192XbarGroup.setObjects(
      *(("CISCO-FABRIC-C12K-MIB", "cfcPreOc192XbarIntrStatus"),
        ("CISCO-FABRIC-C12K-MIB", "cfcPreOc192XbarParityChkStatus"))
)
if mibBuilder.loadTexts:
    ciscoFabricC12kPreOc192XbarGroup.setStatus("current")

ciscoFabricC12kOc192FiaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 8)
)
ciscoFabricC12kOc192FiaGroup.setObjects(
      *(("CISCO-FABRIC-C12K-MIB", "cfcOc192FabToFabMccDataPEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabToFabMccCmdPEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabToFabBackPressurePEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabToFabCellFifoOvFlws"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabToFabCellFifoUnFlws"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabToFabMccCmdSeqEndErrs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabToFabMccCmdSeqStrErrs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabPktLenErrs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabExtRamPEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabPktLenPEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabHdrSramPEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabTxCtrlPEs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabHdrFifoOvFlws"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabExtSramOvFlws"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabFirstLastErrs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabSeqErrs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabSliXorErrs"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabSliCellDrops"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabStatUCHiPktDrops"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabStatUCLoPktDrops"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabStatMCHiPktDrops"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192FabFrFabStatMCLoPktDrops"))
)
if mibBuilder.loadTexts:
    ciscoFabricC12kOc192FiaGroup.setStatus("current")

ciscoFabricC12kOc192LCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 9)
)
ciscoFabricC12kOc192LCGroup.setObjects(
    ("CISCO-FABRIC-C12K-MIB", "cfcGenericScaOc192LCsPresent")
)
if mibBuilder.loadTexts:
    ciscoFabricC12kOc192LCGroup.setStatus("current")

ciscoFabricC12kOc192ScaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 10)
)
ciscoFabricC12kOc192ScaGroup.setObjects(
      *(("CISCO-FABRIC-C12K-MIB", "cfcOc192ScaRotationPeriod"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192ScaDisableGrants"))
)
if mibBuilder.loadTexts:
    ciscoFabricC12kOc192ScaGroup.setStatus("current")

ciscoFabricC12kOc192XbarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 11)
)
ciscoFabricC12kOc192XbarGroup.setObjects(
      *(("CISCO-FABRIC-C12K-MIB", "cfcOc192XbarCtrlLOSStatus"),
        ("CISCO-FABRIC-C12K-MIB", "cfcOc192XbarCtrlCRCErr"))
)
if mibBuilder.loadTexts:
    ciscoFabricC12kOc192XbarGroup.setStatus("current")

ciscoFabricC12kNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 12)
)
ciscoFabricC12kNotifEnableGroup.setObjects(
    ("CISCO-FABRIC-C12K-MIB", "cfcNotifEnable")
)
if mibBuilder.loadTexts:
    ciscoFabricC12kNotifEnableGroup.setStatus("current")


# Notification objects

ciscoFabricC12kMIBFabMasterSchCh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 0, 1)
)
ciscoFabricC12kMIBFabMasterSchCh.setObjects(
      *(("CISCO-FABRIC-C12K-MIB", "cfcGenericGlobalFabMasterSched"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    ciscoFabricC12kMIBFabMasterSchCh.setStatus(
        "current"
    )


# Notifications groups

ciscoFabricC12kNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 2, 13)
)
ciscoFabricC12kNotifGroup.setObjects(
    ("CISCO-FABRIC-C12K-MIB", "ciscoFabricC12kMIBFabMasterSchCh")
)
if mibBuilder.loadTexts:
    ciscoFabricC12kNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoFabricC12kMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 281, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFabricC12kMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FABRIC-C12K-MIB",
    **{"CfcFabricConfigMode": CfcFabricConfigMode,
       "CfcFabricFiaState": CfcFabricFiaState,
       "CfcScaInterrupts": CfcScaInterrupts,
       "CfcSlotMask": CfcSlotMask,
       "ciscoFabricC12kMIB": ciscoFabricC12kMIB,
       "ciscoFabricC12kMIBNotifs": ciscoFabricC12kMIBNotifs,
       "ciscoFabricC12kMIBFabMasterSchCh": ciscoFabricC12kMIBFabMasterSchCh,
       "ciscoFabricC12kMIBObjects": ciscoFabricC12kMIBObjects,
       "cfcGeneric": cfcGeneric,
       "cfcGenericGlobal": cfcGenericGlobal,
       "cfcGenericGlobalFabConfigMode": cfcGenericGlobalFabConfigMode,
       "cfcGenericGlobalFabMasterSched": cfcGenericGlobalFabMasterSched,
       "cfcGenericFab": cfcGenericFab,
       "cfcGenericFabToFabTable": cfcGenericFabToFabTable,
       "cfcGenericFabToFabEntry": cfcGenericFabToFabEntry,
       "cfcGenericFabToFabState": cfcGenericFabToFabState,
       "cfcGenericFabToFabGrantPEs": cfcGenericFabToFabGrantPEs,
       "cfcGenericFabToFabRequestPEs": cfcGenericFabToFabRequestPEs,
       "cfcGenericFabToFabCellFifoPEs": cfcGenericFabToFabCellFifoPEs,
       "cfcGenericFabFrFabTable": cfcGenericFabFrFabTable,
       "cfcGenericFabFrFabEntry": cfcGenericFabFrFabEntry,
       "cfcGenericFabFrFabState": cfcGenericFabFrFabState,
       "cfcGenericFabFrFabSliTable": cfcGenericFabFrFabSliTable,
       "cfcGenericFabFrFabSliEntry": cfcGenericFabFrFabSliEntry,
       "cfcGenericFabFrFabSliFabIndex": cfcGenericFabFrFabSliFabIndex,
       "cfcGenericFabFrFabSliLOSErrors": cfcGenericFabFrFabSliLOSErrors,
       "cfcGenericFabFrFabSliCRCErrors": cfcGenericFabFrFabSliCRCErrors,
       "cfcGenericFabFrFabSliLOSState": cfcGenericFabFrFabSliLOSState,
       "cfcGenericSca": cfcGenericSca,
       "cfcGenericScaTable": cfcGenericScaTable,
       "cfcGenericScaEntry": cfcGenericScaEntry,
       "cfcGenericScaIdentifier": cfcGenericScaIdentifier,
       "cfcGenericScaIntrStatus": cfcGenericScaIntrStatus,
       "cfcGenericScaIntrsEnabled": cfcGenericScaIntrsEnabled,
       "cfcGenericScaConfig": cfcGenericScaConfig,
       "cfcGenericScaPELog": cfcGenericScaPELog,
       "cfcGenericScaFifoOverflowLog": cfcGenericScaFifoOverflowLog,
       "cfcGenericScaLCsEnabled": cfcGenericScaLCsEnabled,
       "cfcGenericScaForcedBackPressure": cfcGenericScaForcedBackPressure,
       "cfcGenericScaOc192LCsPresent": cfcGenericScaOc192LCsPresent,
       "cfcGenericScaPreOc192LCsPresent": cfcGenericScaPreOc192LCsPresent,
       "cfcGenericXbar": cfcGenericXbar,
       "cfcGenericXbarTable": cfcGenericXbarTable,
       "cfcGenericXbarEntry": cfcGenericXbarEntry,
       "cfcGenericXbarIdentifier": cfcGenericXbarIdentifier,
       "cfcPreOc192": cfcPreOc192,
       "cfcPreOc192Fab": cfcPreOc192Fab,
       "cfcPreOc192FabToFabTable": cfcPreOc192FabToFabTable,
       "cfcPreOc192FabToFabEntry": cfcPreOc192FabToFabEntry,
       "cfcPreOc192FabToFabScaLosts": cfcPreOc192FabToFabScaLosts,
       "cfcPreOc192FabToFabUCFifoOvFlws": cfcPreOc192FabToFabUCFifoOvFlws,
       "cfcPreOc192FabToFabUCFifoUnFlws": cfcPreOc192FabToFabUCFifoUnFlws,
       "cfcPreOc192FabToFabMCFifoErrs": cfcPreOc192FabToFabMCFifoErrs,
       "cfcPreOc192FabToFabBmaPEs": cfcPreOc192FabToFabBmaPEs,
       "cfcPreOc192FabToFabBmaHskErrs": cfcPreOc192FabToFabBmaHskErrs,
       "cfcPreOc192FabToFabUniDestMCRqs": cfcPreOc192FabToFabUniDestMCRqs,
       "cfcPreOc192FabToFabMultiDstUCRqs": cfcPreOc192FabToFabMultiDstUCRqs,
       "cfcPreOc192FabToFabEmptyDestRqs": cfcPreOc192FabToFabEmptyDestRqs,
       "cfcPreOc192FabFrFabTable": cfcPreOc192FabFrFabTable,
       "cfcPreOc192FabFrFabEntry": cfcPreOc192FabFrFabEntry,
       "cfcPreOc192FabFrFabCellFifoPEs": cfcPreOc192FabFrFabCellFifoPEs,
       "cfcPreOc192FabFrFabRedFifoPEs": cfcPreOc192FabFrFabRedFifoPEs,
       "cfcPreOc192FabFrFabRedFifoOvflws": cfcPreOc192FabFrFabRedFifoOvflws,
       "cfcPreOc192FabFrFabCellDrops": cfcPreOc192FabFrFabCellDrops,
       "cfcPreOc192Sca": cfcPreOc192Sca,
       "cfcPreOc192ScaTable": cfcPreOc192ScaTable,
       "cfcPreOc192ScaEntry": cfcPreOc192ScaEntry,
       "cfcPreOc192ScaReSyncDelay": cfcPreOc192ScaReSyncDelay,
       "cfcPreOc192ScaLOSLog": cfcPreOc192ScaLOSLog,
       "cfcPreOc192Xbar": cfcPreOc192Xbar,
       "cfcPreOc192XbarTable": cfcPreOc192XbarTable,
       "cfcPreOc192XbarEntry": cfcPreOc192XbarEntry,
       "cfcPreOc192XbarIntrStatus": cfcPreOc192XbarIntrStatus,
       "cfcPreOc192XbarParityChkStatus": cfcPreOc192XbarParityChkStatus,
       "cfcOc192": cfcOc192,
       "cfcOc192Fab": cfcOc192Fab,
       "cfcOc192FabToFabTable": cfcOc192FabToFabTable,
       "cfcOc192FabToFabEntry": cfcOc192FabToFabEntry,
       "cfcOc192FabToFabMccDataPEs": cfcOc192FabToFabMccDataPEs,
       "cfcOc192FabToFabMccCmdPEs": cfcOc192FabToFabMccCmdPEs,
       "cfcOc192FabToFabBackPressurePEs": cfcOc192FabToFabBackPressurePEs,
       "cfcOc192FabToFabCellFifoOvFlws": cfcOc192FabToFabCellFifoOvFlws,
       "cfcOc192FabToFabCellFifoUnFlws": cfcOc192FabToFabCellFifoUnFlws,
       "cfcOc192FabToFabMccCmdSeqEndErrs": cfcOc192FabToFabMccCmdSeqEndErrs,
       "cfcOc192FabToFabMccCmdSeqStrErrs": cfcOc192FabToFabMccCmdSeqStrErrs,
       "cfcOc192FabFrFabTable": cfcOc192FabFrFabTable,
       "cfcOc192FabFrFabEntry": cfcOc192FabFrFabEntry,
       "cfcOc192FabFrFabPktLenErrs": cfcOc192FabFrFabPktLenErrs,
       "cfcOc192FabFrFabExtRamPEs": cfcOc192FabFrFabExtRamPEs,
       "cfcOc192FabFrFabPktLenPEs": cfcOc192FabFrFabPktLenPEs,
       "cfcOc192FabFrFabHdrSramPEs": cfcOc192FabFrFabHdrSramPEs,
       "cfcOc192FabFrFabTxCtrlPEs": cfcOc192FabFrFabTxCtrlPEs,
       "cfcOc192FabFrFabHdrFifoOvFlws": cfcOc192FabFrFabHdrFifoOvFlws,
       "cfcOc192FabFrFabExtSramOvFlws": cfcOc192FabFrFabExtSramOvFlws,
       "cfcOc192FabFrFabFirstLastErrs": cfcOc192FabFrFabFirstLastErrs,
       "cfcOc192FabFrFabSeqErrs": cfcOc192FabFrFabSeqErrs,
       "cfcOc192FabFrFabSliTable": cfcOc192FabFrFabSliTable,
       "cfcOc192FabFrFabSliEntry": cfcOc192FabFrFabSliEntry,
       "cfcOc192FabFrFabSliSwitchIndex": cfcOc192FabFrFabSliSwitchIndex,
       "cfcOc192FabFrFabSliXorErrs": cfcOc192FabFrFabSliXorErrs,
       "cfcOc192FabFrFabSliCellDrops": cfcOc192FabFrFabSliCellDrops,
       "cfcOc192FabFrFabStatTable": cfcOc192FabFrFabStatTable,
       "cfcOc192FabFrFabStatEntry": cfcOc192FabFrFabStatEntry,
       "cfcOc192FabFrFabStatLCIndex": cfcOc192FabFrFabStatLCIndex,
       "cfcOc192FabFrFabStatUCHiPktDrops": cfcOc192FabFrFabStatUCHiPktDrops,
       "cfcOc192FabFrFabStatUCLoPktDrops": cfcOc192FabFrFabStatUCLoPktDrops,
       "cfcOc192FabFrFabStatMCHiPktDrops": cfcOc192FabFrFabStatMCHiPktDrops,
       "cfcOc192FabFrFabStatMCLoPktDrops": cfcOc192FabFrFabStatMCLoPktDrops,
       "cfcOc192Sca": cfcOc192Sca,
       "cfcOc192ScaTable": cfcOc192ScaTable,
       "cfcOc192ScaEntry": cfcOc192ScaEntry,
       "cfcOc192ScaRotationPeriod": cfcOc192ScaRotationPeriod,
       "cfcOc192ScaDisableGrants": cfcOc192ScaDisableGrants,
       "cfcOc192Xbar": cfcOc192Xbar,
       "cfcOc192XbarTable": cfcOc192XbarTable,
       "cfcOc192XbarEntry": cfcOc192XbarEntry,
       "cfcOc192XbarCtrlLOSStatus": cfcOc192XbarCtrlLOSStatus,
       "cfcOc192XbarCtrlCRCErr": cfcOc192XbarCtrlCRCErr,
       "cfcNotif": cfcNotif,
       "cfcNotifEnable": cfcNotifEnable,
       "ciscoFabricC12kMIBConform": ciscoFabricC12kMIBConform,
       "ciscoFabricC12kMIBCompliances": ciscoFabricC12kMIBCompliances,
       "ciscoFabricC12kMIBCompliance": ciscoFabricC12kMIBCompliance,
       "ciscoFabricC12kMIBGroups": ciscoFabricC12kMIBGroups,
       "ciscoFabricC12kGlobalGroup": ciscoFabricC12kGlobalGroup,
       "ciscoFabricC12kFiaGroup": ciscoFabricC12kFiaGroup,
       "ciscoFabricC12kScaGroup": ciscoFabricC12kScaGroup,
       "ciscoFabricC12kXbarGroup": ciscoFabricC12kXbarGroup,
       "ciscoFabricC12kPreOc192FiaGroup": ciscoFabricC12kPreOc192FiaGroup,
       "ciscoFabricC12kPreOc192ScaGroup": ciscoFabricC12kPreOc192ScaGroup,
       "ciscoFabricC12kPreOc192XbarGroup": ciscoFabricC12kPreOc192XbarGroup,
       "ciscoFabricC12kOc192FiaGroup": ciscoFabricC12kOc192FiaGroup,
       "ciscoFabricC12kOc192LCGroup": ciscoFabricC12kOc192LCGroup,
       "ciscoFabricC12kOc192ScaGroup": ciscoFabricC12kOc192ScaGroup,
       "ciscoFabricC12kOc192XbarGroup": ciscoFabricC12kOc192XbarGroup,
       "ciscoFabricC12kNotifEnableGroup": ciscoFabricC12kNotifEnableGroup,
       "ciscoFabricC12kNotifGroup": ciscoFabricC12kNotifGroup}
)
