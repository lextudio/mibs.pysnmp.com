# SNMP MIB module (CISCO-DOT11-HT-MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-HT-MAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:51 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoDot11HtMacMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 626)
)
ciscoDot11HtMacMIB.setRevisions(
        ("2007-05-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDot11HtMacMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDot11HtMacMIBNotifs = _CiscoDot11HtMacMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 0)
)
_CiscoDot11HtMacMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDot11HtMacMIBObjects = _CiscoDot11HtMacMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1)
)
_CD11HtMacStationConfig_ObjectIdentity = ObjectIdentity
cD11HtMacStationConfig = _CD11HtMacStationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1)
)
_CD11HtMacStationConfigTable_Object = MibTable
cD11HtMacStationConfigTable = _CD11HtMacStationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cD11HtMacStationConfigTable.setStatus("current")
_CD11HtMacStationConfigEntry_Object = MibTableRow
cD11HtMacStationConfigEntry = _CD11HtMacStationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1)
)
cD11HtMacStationConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cD11HtMacStationConfigEntry.setStatus("current")


class _CD11HtMacOperationalMCSSet_Type(OctetString):
    """Custom type cD11HtMacOperationalMCSSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CD11HtMacOperationalMCSSet_Type.__name__ = "OctetString"
_CD11HtMacOperationalMCSSet_Object = MibTableColumn
cD11HtMacOperationalMCSSet = _CD11HtMacOperationalMCSSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 1),
    _CD11HtMacOperationalMCSSet_Type()
)
cD11HtMacOperationalMCSSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacOperationalMCSSet.setStatus("current")


class _CD11HtMacMIMOPowerSave_Type(Integer32):
    """Custom type cD11HtMacMIMOPowerSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("mimo", 3),
          ("static", 1))
    )


_CD11HtMacMIMOPowerSave_Type.__name__ = "Integer32"
_CD11HtMacMIMOPowerSave_Object = MibTableColumn
cD11HtMacMIMOPowerSave = _CD11HtMacMIMOPowerSave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 2),
    _CD11HtMacMIMOPowerSave_Type()
)
cD11HtMacMIMOPowerSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtMacMIMOPowerSave.setStatus("current")


class _CD11HtMacNDelayedBlockAckImplemented_Type(TruthValue):
    """Custom type cD11HtMacNDelayedBlockAckImplemented based on TruthValue"""


_CD11HtMacNDelayedBlockAckImplemented_Object = MibTableColumn
cD11HtMacNDelayedBlockAckImplemented = _CD11HtMacNDelayedBlockAckImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 3),
    _CD11HtMacNDelayedBlockAckImplemented_Type()
)
cD11HtMacNDelayedBlockAckImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtMacNDelayedBlockAckImplemented.setStatus("current")


class _CD11HtMacMaxAMSDULength_Type(Integer32):
    """Custom type cD11HtMacMaxAMSDULength based on Integer32"""
    defaultValue = 3839

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3839,
              7935)
        )
    )
    namedValues = NamedValues(
        *(("amsduSize3839", 3839),
          ("amsduSize7935", 7935))
    )


_CD11HtMacMaxAMSDULength_Type.__name__ = "Integer32"
_CD11HtMacMaxAMSDULength_Object = MibTableColumn
cD11HtMacMaxAMSDULength = _CD11HtMacMaxAMSDULength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 4),
    _CD11HtMacMaxAMSDULength_Type()
)
cD11HtMacMaxAMSDULength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtMacMaxAMSDULength.setStatus("current")


class _CD11HtMacPSMPImplemented_Type(TruthValue):
    """Custom type cD11HtMacPSMPImplemented based on TruthValue"""


_CD11HtMacPSMPImplemented_Object = MibTableColumn
cD11HtMacPSMPImplemented = _CD11HtMacPSMPImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 5),
    _CD11HtMacPSMPImplemented_Type()
)
cD11HtMacPSMPImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtMacPSMPImplemented.setStatus("current")


class _CD11HtMacSTBCControlFrameImplemented_Type(TruthValue):
    """Custom type cD11HtMacSTBCControlFrameImplemented based on TruthValue"""


_CD11HtMacSTBCControlFrameImplemented_Object = MibTableColumn
cD11HtMacSTBCControlFrameImplemented = _CD11HtMacSTBCControlFrameImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 6),
    _CD11HtMacSTBCControlFrameImplemented_Type()
)
cD11HtMacSTBCControlFrameImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtMacSTBCControlFrameImplemented.setStatus("current")


class _CD11HtMacLsigTxOpProtectImplemented_Type(TruthValue):
    """Custom type cD11HtMacLsigTxOpProtectImplemented based on TruthValue"""


_CD11HtMacLsigTxOpProtectImplemented_Object = MibTableColumn
cD11HtMacLsigTxOpProtectImplemented = _CD11HtMacLsigTxOpProtectImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 7),
    _CD11HtMacLsigTxOpProtectImplemented_Type()
)
cD11HtMacLsigTxOpProtectImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtMacLsigTxOpProtectImplemented.setStatus("current")


class _CD11HtMacMaxRxAMPDUFactor_Type(Integer32):
    """Custom type cD11HtMacMaxRxAMPDUFactor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CD11HtMacMaxRxAMPDUFactor_Type.__name__ = "Integer32"
_CD11HtMacMaxRxAMPDUFactor_Object = MibTableColumn
cD11HtMacMaxRxAMPDUFactor = _CD11HtMacMaxRxAMPDUFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 8),
    _CD11HtMacMaxRxAMPDUFactor_Type()
)
cD11HtMacMaxRxAMPDUFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtMacMaxRxAMPDUFactor.setStatus("current")


class _CD11HtMacMPDUDensity_Type(Integer32):
    """Custom type cD11HtMacMPDUDensity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("four", 7),
          ("half", 4),
          ("noTimeRestriction", 1),
          ("one", 5),
          ("oneEighth", 2),
          ("oneFourth", 3),
          ("two", 6))
    )


_CD11HtMacMPDUDensity_Type.__name__ = "Integer32"
_CD11HtMacMPDUDensity_Object = MibTableColumn
cD11HtMacMPDUDensity = _CD11HtMacMPDUDensity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 9),
    _CD11HtMacMPDUDensity_Type()
)
cD11HtMacMPDUDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtMacMPDUDensity.setStatus("current")


class _CD11HtMacPCOImplemented_Type(TruthValue):
    """Custom type cD11HtMacPCOImplemented based on TruthValue"""


_CD11HtMacPCOImplemented_Object = MibTableColumn
cD11HtMacPCOImplemented = _CD11HtMacPCOImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 10),
    _CD11HtMacPCOImplemented_Type()
)
cD11HtMacPCOImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtMacPCOImplemented.setStatus("current")


class _CD11HtMacTransitionTime_Type(Integer32):
    """Custom type cD11HtMacTransitionTime based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(400,
              1500,
              5000)
        )
    )
    namedValues = NamedValues(
        *(("fiveThousand", 5000),
          ("fourHundred", 400),
          ("oneThousandFiveHundred", 1500))
    )


_CD11HtMacTransitionTime_Type.__name__ = "Integer32"
_CD11HtMacTransitionTime_Object = MibTableColumn
cD11HtMacTransitionTime = _CD11HtMacTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 11),
    _CD11HtMacTransitionTime_Type()
)
cD11HtMacTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtMacTransitionTime.setStatus("current")
if mibBuilder.loadTexts:
    cD11HtMacTransitionTime.setUnits("microseconds")


class _CD11HtMacMCSFeedbackImplemented_Type(Integer32):
    """Custom type cD11HtMacMCSFeedbackImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("none", 1),
          ("unsolicited", 2))
    )


_CD11HtMacMCSFeedbackImplemented_Type.__name__ = "Integer32"
_CD11HtMacMCSFeedbackImplemented_Object = MibTableColumn
cD11HtMacMCSFeedbackImplemented = _CD11HtMacMCSFeedbackImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 12),
    _CD11HtMacMCSFeedbackImplemented_Type()
)
cD11HtMacMCSFeedbackImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtMacMCSFeedbackImplemented.setStatus("current")


class _CD11HtMacAMSDUEnable_Type(TruthValue):
    """Custom type cD11HtMacAMSDUEnable based on TruthValue"""


_CD11HtMacAMSDUEnable_Object = MibTableColumn
cD11HtMacAMSDUEnable = _CD11HtMacAMSDUEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 13),
    _CD11HtMacAMSDUEnable_Type()
)
cD11HtMacAMSDUEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacAMSDUEnable.setStatus("current")


class _CD11HtMacAMPDUEnable_Type(TruthValue):
    """Custom type cD11HtMacAMPDUEnable based on TruthValue"""


_CD11HtMacAMPDUEnable_Object = MibTableColumn
cD11HtMacAMPDUEnable = _CD11HtMacAMPDUEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 14),
    _CD11HtMacAMPDUEnable_Type()
)
cD11HtMacAMPDUEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacAMPDUEnable.setStatus("current")
_CD11HtMacOperations_ObjectIdentity = ObjectIdentity
cD11HtMacOperations = _CD11HtMacOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2)
)
_CD11HtMacOperationTable_Object = MibTable
cD11HtMacOperationTable = _CD11HtMacOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cD11HtMacOperationTable.setStatus("current")
_CD11HtMacOperationEntry_Object = MibTableRow
cD11HtMacOperationEntry = _CD11HtMacOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1)
)
cD11HtMacOperationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cD11HtMacOperationEntry.setStatus("current")


class _CD11HtMacOperatingMode_Type(Integer32):
    """Custom type cD11HtMacOperatingMode based on Integer32"""
    defaultValue = 1

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
        *(("mandatoryAllProtection", 4),
          ("mandatoryFortyProtection", 3),
          ("optionalProtection", 2),
          ("pureHt", 1))
    )


_CD11HtMacOperatingMode_Type.__name__ = "Integer32"
_CD11HtMacOperatingMode_Object = MibTableColumn
cD11HtMacOperatingMode = _CD11HtMacOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 1),
    _CD11HtMacOperatingMode_Type()
)
cD11HtMacOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacOperatingMode.setStatus("current")


class _CD11HtMacRIFSMode_Type(TruthValue):
    """Custom type cD11HtMacRIFSMode based on TruthValue"""


_CD11HtMacRIFSMode_Object = MibTableColumn
cD11HtMacRIFSMode = _CD11HtMacRIFSMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 2),
    _CD11HtMacRIFSMode_Type()
)
cD11HtMacRIFSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacRIFSMode.setStatus("current")


class _CD11HtMacPSMPControlledAccess_Type(TruthValue):
    """Custom type cD11HtMacPSMPControlledAccess based on TruthValue"""


_CD11HtMacPSMPControlledAccess_Object = MibTableColumn
cD11HtMacPSMPControlledAccess = _CD11HtMacPSMPControlledAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 3),
    _CD11HtMacPSMPControlledAccess_Type()
)
cD11HtMacPSMPControlledAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacPSMPControlledAccess.setStatus("current")


class _CD11HtMacServiceIntervalGranularity_Type(Integer32):
    """Custom type cD11HtMacServiceIntervalGranularity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CD11HtMacServiceIntervalGranularity_Type.__name__ = "Integer32"
_CD11HtMacServiceIntervalGranularity_Object = MibTableColumn
cD11HtMacServiceIntervalGranularity = _CD11HtMacServiceIntervalGranularity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 4),
    _CD11HtMacServiceIntervalGranularity_Type()
)
cD11HtMacServiceIntervalGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacServiceIntervalGranularity.setStatus("current")
if mibBuilder.loadTexts:
    cD11HtMacServiceIntervalGranularity.setUnits("milliseconds")


class _CD11HtMacDualCTSProtection_Type(TruthValue):
    """Custom type cD11HtMacDualCTSProtection based on TruthValue"""


_CD11HtMacDualCTSProtection_Object = MibTableColumn
cD11HtMacDualCTSProtection = _CD11HtMacDualCTSProtection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 5),
    _CD11HtMacDualCTSProtection_Type()
)
cD11HtMacDualCTSProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacDualCTSProtection.setStatus("current")


class _CD11HtMacLSigTxOpFullProtectionEnabled_Type(TruthValue):
    """Custom type cD11HtMacLSigTxOpFullProtectionEnabled based on TruthValue"""


_CD11HtMacLSigTxOpFullProtectionEnabled_Object = MibTableColumn
cD11HtMacLSigTxOpFullProtectionEnabled = _CD11HtMacLSigTxOpFullProtectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 6),
    _CD11HtMacLSigTxOpFullProtectionEnabled_Type()
)
cD11HtMacLSigTxOpFullProtectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacLSigTxOpFullProtectionEnabled.setStatus("current")


class _CD11HtMacNonGFEntitiesPresent_Type(TruthValue):
    """Custom type cD11HtMacNonGFEntitiesPresent based on TruthValue"""


_CD11HtMacNonGFEntitiesPresent_Object = MibTableColumn
cD11HtMacNonGFEntitiesPresent = _CD11HtMacNonGFEntitiesPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 7),
    _CD11HtMacNonGFEntitiesPresent_Type()
)
cD11HtMacNonGFEntitiesPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacNonGFEntitiesPresent.setStatus("current")


class _CD11HtMacPCOActivated_Type(TruthValue):
    """Custom type cD11HtMacPCOActivated based on TruthValue"""


_CD11HtMacPCOActivated_Object = MibTableColumn
cD11HtMacPCOActivated = _CD11HtMacPCOActivated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 8),
    _CD11HtMacPCOActivated_Type()
)
cD11HtMacPCOActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacPCOActivated.setStatus("current")


class _CD11HtMacPCO20MaxDuration_Type(Integer32):
    """Custom type cD11HtMacPCO20MaxDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CD11HtMacPCO20MaxDuration_Type.__name__ = "Integer32"
_CD11HtMacPCO20MaxDuration_Object = MibTableColumn
cD11HtMacPCO20MaxDuration = _CD11HtMacPCO20MaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 9),
    _CD11HtMacPCO20MaxDuration_Type()
)
cD11HtMacPCO20MaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacPCO20MaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cD11HtMacPCO20MaxDuration.setUnits("TU")


class _CD11HtMacPCO40MaxDuration_Type(Integer32):
    """Custom type cD11HtMacPCO40MaxDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CD11HtMacPCO40MaxDuration_Type.__name__ = "Integer32"
_CD11HtMacPCO40MaxDuration_Object = MibTableColumn
cD11HtMacPCO40MaxDuration = _CD11HtMacPCO40MaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 10),
    _CD11HtMacPCO40MaxDuration_Type()
)
cD11HtMacPCO40MaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacPCO40MaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cD11HtMacPCO40MaxDuration.setUnits("TU")


class _CD11HtMacPCO20MinDuration_Type(Integer32):
    """Custom type cD11HtMacPCO20MinDuration based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CD11HtMacPCO20MinDuration_Type.__name__ = "Integer32"
_CD11HtMacPCO20MinDuration_Object = MibTableColumn
cD11HtMacPCO20MinDuration = _CD11HtMacPCO20MinDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 11),
    _CD11HtMacPCO20MinDuration_Type()
)
cD11HtMacPCO20MinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacPCO20MinDuration.setStatus("current")
if mibBuilder.loadTexts:
    cD11HtMacPCO20MinDuration.setUnits("TU")


class _CD11HtMacPCO40MinDuration_Type(Integer32):
    """Custom type cD11HtMacPCO40MinDuration based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CD11HtMacPCO40MinDuration_Type.__name__ = "Integer32"
_CD11HtMacPCO40MinDuration_Object = MibTableColumn
cD11HtMacPCO40MinDuration = _CD11HtMacPCO40MinDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 12),
    _CD11HtMacPCO40MinDuration_Type()
)
cD11HtMacPCO40MinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtMacPCO40MinDuration.setStatus("current")
if mibBuilder.loadTexts:
    cD11HtMacPCO40MinDuration.setUnits("TU")
_CiscoDot11HtMacMIBConform_ObjectIdentity = ObjectIdentity
ciscoDot11HtMacMIBConform = _CiscoDot11HtMacMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 2)
)
_CiscoDot11HtMacMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDot11HtMacMIBCompliances = _CiscoDot11HtMacMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 1)
)
_CiscoDot11HtMacMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDot11HtMacMIBGroups = _CiscoDot11HtMacMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 2)
)

# Managed Objects groups

ciscoDot11HtMacStationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 2, 1)
)
ciscoDot11HtMacStationConfigGroup.setObjects(
      *(("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacOperationalMCSSet"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMIMOPowerSave"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacNDelayedBlockAckImplemented"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMaxAMSDULength"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPSMPImplemented"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacSTBCControlFrameImplemented"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacLsigTxOpProtectImplemented"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMaxRxAMPDUFactor"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMPDUDensity"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCOImplemented"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacTransitionTime"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMCSFeedbackImplemented"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacAMSDUEnable"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacAMPDUEnable"))
)
if mibBuilder.loadTexts:
    ciscoDot11HtMacStationConfigGroup.setStatus("current")

ciscoDot11HtMacOperationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 2, 2)
)
ciscoDot11HtMacOperationsGroup.setObjects(
      *(("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacOperatingMode"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacRIFSMode"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPSMPControlledAccess"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacServiceIntervalGranularity"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacDualCTSProtection"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacLSigTxOpFullProtectionEnabled"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacNonGFEntitiesPresent"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCOActivated"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCO40MaxDuration"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCO20MaxDuration"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCO40MinDuration"),
        ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCO20MinDuration"))
)
if mibBuilder.loadTexts:
    ciscoDot11HtMacOperationsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cD11HtMacCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cD11HtMacCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-HT-MAC-MIB",
    **{"ciscoDot11HtMacMIB": ciscoDot11HtMacMIB,
       "ciscoDot11HtMacMIBNotifs": ciscoDot11HtMacMIBNotifs,
       "ciscoDot11HtMacMIBObjects": ciscoDot11HtMacMIBObjects,
       "cD11HtMacStationConfig": cD11HtMacStationConfig,
       "cD11HtMacStationConfigTable": cD11HtMacStationConfigTable,
       "cD11HtMacStationConfigEntry": cD11HtMacStationConfigEntry,
       "cD11HtMacOperationalMCSSet": cD11HtMacOperationalMCSSet,
       "cD11HtMacMIMOPowerSave": cD11HtMacMIMOPowerSave,
       "cD11HtMacNDelayedBlockAckImplemented": cD11HtMacNDelayedBlockAckImplemented,
       "cD11HtMacMaxAMSDULength": cD11HtMacMaxAMSDULength,
       "cD11HtMacPSMPImplemented": cD11HtMacPSMPImplemented,
       "cD11HtMacSTBCControlFrameImplemented": cD11HtMacSTBCControlFrameImplemented,
       "cD11HtMacLsigTxOpProtectImplemented": cD11HtMacLsigTxOpProtectImplemented,
       "cD11HtMacMaxRxAMPDUFactor": cD11HtMacMaxRxAMPDUFactor,
       "cD11HtMacMPDUDensity": cD11HtMacMPDUDensity,
       "cD11HtMacPCOImplemented": cD11HtMacPCOImplemented,
       "cD11HtMacTransitionTime": cD11HtMacTransitionTime,
       "cD11HtMacMCSFeedbackImplemented": cD11HtMacMCSFeedbackImplemented,
       "cD11HtMacAMSDUEnable": cD11HtMacAMSDUEnable,
       "cD11HtMacAMPDUEnable": cD11HtMacAMPDUEnable,
       "cD11HtMacOperations": cD11HtMacOperations,
       "cD11HtMacOperationTable": cD11HtMacOperationTable,
       "cD11HtMacOperationEntry": cD11HtMacOperationEntry,
       "cD11HtMacOperatingMode": cD11HtMacOperatingMode,
       "cD11HtMacRIFSMode": cD11HtMacRIFSMode,
       "cD11HtMacPSMPControlledAccess": cD11HtMacPSMPControlledAccess,
       "cD11HtMacServiceIntervalGranularity": cD11HtMacServiceIntervalGranularity,
       "cD11HtMacDualCTSProtection": cD11HtMacDualCTSProtection,
       "cD11HtMacLSigTxOpFullProtectionEnabled": cD11HtMacLSigTxOpFullProtectionEnabled,
       "cD11HtMacNonGFEntitiesPresent": cD11HtMacNonGFEntitiesPresent,
       "cD11HtMacPCOActivated": cD11HtMacPCOActivated,
       "cD11HtMacPCO20MaxDuration": cD11HtMacPCO20MaxDuration,
       "cD11HtMacPCO40MaxDuration": cD11HtMacPCO40MaxDuration,
       "cD11HtMacPCO20MinDuration": cD11HtMacPCO20MinDuration,
       "cD11HtMacPCO40MinDuration": cD11HtMacPCO40MinDuration,
       "ciscoDot11HtMacMIBConform": ciscoDot11HtMacMIBConform,
       "ciscoDot11HtMacMIBCompliances": ciscoDot11HtMacMIBCompliances,
       "cD11HtMacCompliance": cD11HtMacCompliance,
       "ciscoDot11HtMacMIBGroups": ciscoDot11HtMacMIBGroups,
       "ciscoDot11HtMacStationConfigGroup": ciscoDot11HtMacStationConfigGroup,
       "ciscoDot11HtMacOperationsGroup": ciscoDot11HtMacOperationsGroup}
)
