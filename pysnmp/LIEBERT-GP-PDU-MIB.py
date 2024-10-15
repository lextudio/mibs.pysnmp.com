# SNMP MIB module (LIEBERT-GP-PDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIEBERT-GP-PDU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:57 2024
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

(lgpPdu,
 liebertPduModuleReg) = mibBuilder.importSymbols(
    "LIEBERT-GP-REGISTRATION-MIB",
    "lgpPdu",
    "liebertPduModuleReg")

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

liebertGlobalProductsPduModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 9, 1)
)
liebertGlobalProductsPduModule.setRevisions(
        ("2008-07-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LgpPduCluster_ObjectIdentity = ObjectIdentity
lgpPduCluster = _LgpPduCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 10)
)
if mibBuilder.loadTexts:
    lgpPduCluster.setStatus("current")
_LgpPduGrpSysStatus_Type = Unsigned32
_LgpPduGrpSysStatus_Object = MibScalar
lgpPduGrpSysStatus = _LgpPduGrpSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 10, 5),
    _LgpPduGrpSysStatus_Type()
)
lgpPduGrpSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduGrpSysStatus.setStatus("current")
_LgpPduTableCount_Type = Unsigned32
_LgpPduTableCount_Object = MibScalar
lgpPduTableCount = _LgpPduTableCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 19),
    _LgpPduTableCount_Type()
)
lgpPduTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduTableCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduTableCount.setUnits("Count")
_LgpPduTable_Object = MibTable
lgpPduTable = _LgpPduTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20)
)
if mibBuilder.loadTexts:
    lgpPduTable.setStatus("current")
_LgpPduEntry_Object = MibTableRow
lgpPduEntry = _LgpPduEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1)
)
lgpPduEntry.setIndexNames(
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpPduEntry.setStatus("current")
_LgpPduEntryIndex_Type = Unsigned32
_LgpPduEntryIndex_Object = MibTableColumn
lgpPduEntryIndex = _LgpPduEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 1),
    _LgpPduEntryIndex_Type()
)
lgpPduEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduEntryIndex.setStatus("current")
_LgpPduEntryId_Type = Unsigned32
_LgpPduEntryId_Object = MibTableColumn
lgpPduEntryId = _LgpPduEntryId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 5),
    _LgpPduEntryId_Type()
)
lgpPduEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduEntryId.setStatus("current")
_LgpPduEntryUsrLabel_Type = DisplayString
_LgpPduEntryUsrLabel_Object = MibTableColumn
lgpPduEntryUsrLabel = _LgpPduEntryUsrLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 10),
    _LgpPduEntryUsrLabel_Type()
)
lgpPduEntryUsrLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduEntryUsrLabel.setStatus("current")
_LgpPduEntrySysAssignLabel_Type = DisplayString
_LgpPduEntrySysAssignLabel_Object = MibTableColumn
lgpPduEntrySysAssignLabel = _LgpPduEntrySysAssignLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 15),
    _LgpPduEntrySysAssignLabel_Type()
)
lgpPduEntrySysAssignLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduEntrySysAssignLabel.setStatus("current")
_LgpPduEntryPositionRelative_Type = Unsigned32
_LgpPduEntryPositionRelative_Object = MibTableColumn
lgpPduEntryPositionRelative = _LgpPduEntryPositionRelative_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 20),
    _LgpPduEntryPositionRelative_Type()
)
lgpPduEntryPositionRelative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduEntryPositionRelative.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduEntryPositionRelative.setUnits("Count")
_LgpPduEntrySysStatus_Type = Unsigned32
_LgpPduEntrySysStatus_Object = MibTableColumn
lgpPduEntrySysStatus = _LgpPduEntrySysStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 25),
    _LgpPduEntrySysStatus_Type()
)
lgpPduEntrySysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduEntrySysStatus.setStatus("current")
_LgpPduEntryUsrTag1_Type = DisplayString
_LgpPduEntryUsrTag1_Object = MibTableColumn
lgpPduEntryUsrTag1 = _LgpPduEntryUsrTag1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 35),
    _LgpPduEntryUsrTag1_Type()
)
lgpPduEntryUsrTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduEntryUsrTag1.setStatus("current")
_LgpPduEntryUsrTag2_Type = DisplayString
_LgpPduEntryUsrTag2_Object = MibTableColumn
lgpPduEntryUsrTag2 = _LgpPduEntryUsrTag2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 40),
    _LgpPduEntryUsrTag2_Type()
)
lgpPduEntryUsrTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduEntryUsrTag2.setStatus("current")
_LgpPduEntrySerialNumber_Type = DisplayString
_LgpPduEntrySerialNumber_Object = MibTableColumn
lgpPduEntrySerialNumber = _LgpPduEntrySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 45),
    _LgpPduEntrySerialNumber_Type()
)
lgpPduEntrySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduEntrySerialNumber.setStatus("current")
_LgpPduEntryRbCount_Type = Unsigned32
_LgpPduEntryRbCount_Object = MibTableColumn
lgpPduEntryRbCount = _LgpPduEntryRbCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 50),
    _LgpPduEntryRbCount_Type()
)
lgpPduEntryRbCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduEntryRbCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduEntryRbCount.setUnits("Count")
_LgpPduPowerSource_ObjectIdentity = ObjectIdentity
lgpPduPowerSource = _LgpPduPowerSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30)
)
if mibBuilder.loadTexts:
    lgpPduPowerSource.setStatus("current")
_LgpPduPsTableCount_Type = Unsigned32
_LgpPduPsTableCount_Object = MibScalar
lgpPduPsTableCount = _LgpPduPsTableCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 19),
    _LgpPduPsTableCount_Type()
)
lgpPduPsTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsTableCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsTableCount.setUnits("Count")
_LgpPduPsTable_Object = MibTable
lgpPduPsTable = _LgpPduPsTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20)
)
if mibBuilder.loadTexts:
    lgpPduPsTable.setStatus("current")
_LgpPduPsEntry_Object = MibTableRow
lgpPduPsEntry = _LgpPduPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1)
)
lgpPduPsEntry.setIndexNames(
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduPsEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpPduPsEntry.setStatus("current")
_LgpPduPsEntryIndex_Type = Unsigned32
_LgpPduPsEntryIndex_Object = MibTableColumn
lgpPduPsEntryIndex = _LgpPduPsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 5),
    _LgpPduPsEntryIndex_Type()
)
lgpPduPsEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduPsEntryIndex.setStatus("current")
_LgpPduPsEntryId_Type = Unsigned32
_LgpPduPsEntryId_Object = MibTableColumn
lgpPduPsEntryId = _LgpPduPsEntryId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 10),
    _LgpPduPsEntryId_Type()
)
lgpPduPsEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryId.setStatus("current")
_LgpPduPsEntrySysAssignLabel_Type = DisplayString
_LgpPduPsEntrySysAssignLabel_Object = MibTableColumn
lgpPduPsEntrySysAssignLabel = _LgpPduPsEntrySysAssignLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 15),
    _LgpPduPsEntrySysAssignLabel_Type()
)
lgpPduPsEntrySysAssignLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntrySysAssignLabel.setStatus("current")
_LgpPduPsEntryModel_Type = DisplayString
_LgpPduPsEntryModel_Object = MibTableColumn
lgpPduPsEntryModel = _LgpPduPsEntryModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 20),
    _LgpPduPsEntryModel_Type()
)
lgpPduPsEntryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryModel.setStatus("current")


class _LgpPduPsEntryWiringType_Type(Integer32):
    """Custom type lgpPduPsEntryWiringType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("single-phase-3-wire-L1-N-PE", 1),
          ("three-phase-4-wire-L1-L2-L3-PE", 3),
          ("three-phase-5-wire-L1-L2-L3-N-PE", 4),
          ("two-phase-3-wire-L1-L2-PE", 2),
          ("two-phase-4-wire-L1-L2-N-PE", 5))
    )


_LgpPduPsEntryWiringType_Type.__name__ = "Integer32"
_LgpPduPsEntryWiringType_Object = MibTableColumn
lgpPduPsEntryWiringType = _LgpPduPsEntryWiringType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 25),
    _LgpPduPsEntryWiringType_Type()
)
lgpPduPsEntryWiringType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsEntryWiringType.setStatus("current")
_LgpPduPsEntryEpInputRated_Type = Unsigned32
_LgpPduPsEntryEpInputRated_Object = MibTableColumn
lgpPduPsEntryEpInputRated = _LgpPduPsEntryEpInputRated_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 30),
    _LgpPduPsEntryEpInputRated_Type()
)
lgpPduPsEntryEpInputRated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryEpInputRated.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryEpInputRated.setUnits("VoltRMS")
_LgpPduPsEntryEcInputRated_Type = Unsigned32
_LgpPduPsEntryEcInputRated_Object = MibTableColumn
lgpPduPsEntryEcInputRated = _LgpPduPsEntryEcInputRated_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 35),
    _LgpPduPsEntryEcInputRated_Type()
)
lgpPduPsEntryEcInputRated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcInputRated.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcInputRated.setUnits("0.1 Amp-AC-RMS")
_LgpPduPsEntryFreqRated_Type = Unsigned32
_LgpPduPsEntryFreqRated_Object = MibTableColumn
lgpPduPsEntryFreqRated = _LgpPduPsEntryFreqRated_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 40),
    _LgpPduPsEntryFreqRated_Type()
)
lgpPduPsEntryFreqRated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryFreqRated.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryFreqRated.setUnits("Hertz")
_LgpPduPsEntryEnergyAccum_Type = Unsigned32
_LgpPduPsEntryEnergyAccum_Object = MibTableColumn
lgpPduPsEntryEnergyAccum = _LgpPduPsEntryEnergyAccum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 50),
    _LgpPduPsEntryEnergyAccum_Type()
)
lgpPduPsEntryEnergyAccum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsEntryEnergyAccum.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryEnergyAccum.setUnits("0.1 Kilowatt-Hour")
_LgpPduPsEntrySerialNum_Type = DisplayString
_LgpPduPsEntrySerialNum_Object = MibTableColumn
lgpPduPsEntrySerialNum = _LgpPduPsEntrySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 55),
    _LgpPduPsEntrySerialNum_Type()
)
lgpPduPsEntrySerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntrySerialNum.setStatus("current")
_LgpPduPsEntryFirmwareVersion_Type = DisplayString
_LgpPduPsEntryFirmwareVersion_Object = MibTableColumn
lgpPduPsEntryFirmwareVersion = _LgpPduPsEntryFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 60),
    _LgpPduPsEntryFirmwareVersion_Type()
)
lgpPduPsEntryFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryFirmwareVersion.setStatus("current")
_LgpPduPsEntryPwrTotal_Type = Unsigned32
_LgpPduPsEntryPwrTotal_Object = MibTableColumn
lgpPduPsEntryPwrTotal = _LgpPduPsEntryPwrTotal_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 65),
    _LgpPduPsEntryPwrTotal_Type()
)
lgpPduPsEntryPwrTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryPwrTotal.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryPwrTotal.setUnits("Watt")
_LgpPduPsEntryEcNeutral_Type = Unsigned32
_LgpPduPsEntryEcNeutral_Object = MibTableColumn
lgpPduPsEntryEcNeutral = _LgpPduPsEntryEcNeutral_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 70),
    _LgpPduPsEntryEcNeutral_Type()
)
lgpPduPsEntryEcNeutral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcNeutral.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcNeutral.setUnits("0.1 Amp-AC-RMS")
_LgpPduPsEntryEcNeutralThrshldOvrWarn_Type = Unsigned32
_LgpPduPsEntryEcNeutralThrshldOvrWarn_Object = MibTableColumn
lgpPduPsEntryEcNeutralThrshldOvrWarn = _LgpPduPsEntryEcNeutralThrshldOvrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 75),
    _LgpPduPsEntryEcNeutralThrshldOvrWarn_Type()
)
lgpPduPsEntryEcNeutralThrshldOvrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcNeutralThrshldOvrWarn.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcNeutralThrshldOvrWarn.setUnits("Percent")
_LgpPduPsEntryEcNeutralThrshldOvrAlarm_Type = Unsigned32
_LgpPduPsEntryEcNeutralThrshldOvrAlarm_Object = MibTableColumn
lgpPduPsEntryEcNeutralThrshldOvrAlarm = _LgpPduPsEntryEcNeutralThrshldOvrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 80),
    _LgpPduPsEntryEcNeutralThrshldOvrAlarm_Type()
)
lgpPduPsEntryEcNeutralThrshldOvrAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcNeutralThrshldOvrAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcNeutralThrshldOvrAlarm.setUnits("Percent")
_LgpPduPsLineTable_Object = MibTable
lgpPduPsLineTable = _LgpPduPsLineTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40)
)
if mibBuilder.loadTexts:
    lgpPduPsLineTable.setStatus("current")
_LgpPduPsLineEntry_Object = MibTableRow
lgpPduPsLineEntry = _LgpPduPsLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1)
)
lgpPduPsLineEntry.setIndexNames(
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduPsEntryIndex"),
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduPsLineEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpPduPsLineEntry.setStatus("current")
_LgpPduPsLineEntryIndex_Type = Unsigned32
_LgpPduPsLineEntryIndex_Object = MibTableColumn
lgpPduPsLineEntryIndex = _LgpPduPsLineEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 5),
    _LgpPduPsLineEntryIndex_Type()
)
lgpPduPsLineEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryIndex.setStatus("current")
_LgpPduPsLineEntryId_Type = Unsigned32
_LgpPduPsLineEntryId_Object = MibTableColumn
lgpPduPsLineEntryId = _LgpPduPsLineEntryId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 10),
    _LgpPduPsLineEntryId_Type()
)
lgpPduPsLineEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryId.setStatus("current")


class _LgpPduPsLineEntryLine_Type(Integer32):
    """Custom type lgpPduPsLineEntryLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3))
    )


_LgpPduPsLineEntryLine_Type.__name__ = "Integer32"
_LgpPduPsLineEntryLine_Object = MibTableColumn
lgpPduPsLineEntryLine = _LgpPduPsLineEntryLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 15),
    _LgpPduPsLineEntryLine_Type()
)
lgpPduPsLineEntryLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryLine.setStatus("current")
_LgpPduPsLineEntryEpLNTenths_Type = Unsigned32
_LgpPduPsLineEntryEpLNTenths_Object = MibTableColumn
lgpPduPsLineEntryEpLNTenths = _LgpPduPsLineEntryEpLNTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 19),
    _LgpPduPsLineEntryEpLNTenths_Type()
)
lgpPduPsLineEntryEpLNTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLNTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLNTenths.setUnits("0.1 Volts-AC-RMS")
_LgpPduPsLineEntryEpLN_Type = Unsigned32
_LgpPduPsLineEntryEpLN_Object = MibTableColumn
lgpPduPsLineEntryEpLN = _LgpPduPsLineEntryEpLN_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 20),
    _LgpPduPsLineEntryEpLN_Type()
)
lgpPduPsLineEntryEpLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLN.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLN.setUnits("Volts-AC-RMS")
_LgpPduPsLineEntryEc_Type = Unsigned32
_LgpPduPsLineEntryEc_Object = MibTableColumn
lgpPduPsLineEntryEc = _LgpPduPsLineEntryEc_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 21),
    _LgpPduPsLineEntryEc_Type()
)
lgpPduPsLineEntryEc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEc.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEc.setUnits("0.1 Amps-AC-RMS")
_LgpPduPsLineEntryEcHundredths_Type = Unsigned32
_LgpPduPsLineEntryEcHundredths_Object = MibTableColumn
lgpPduPsLineEntryEcHundredths = _LgpPduPsLineEntryEcHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 22),
    _LgpPduPsLineEntryEcHundredths_Type()
)
lgpPduPsLineEntryEcHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcHundredths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcHundredths.setUnits("0.01 Amps-AC-RMS")
_LgpPduPsLineEntryEcThrshldUndrAlarm_Type = Unsigned32
_LgpPduPsLineEntryEcThrshldUndrAlarm_Object = MibTableColumn
lgpPduPsLineEntryEcThrshldUndrAlarm = _LgpPduPsLineEntryEcThrshldUndrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 35),
    _LgpPduPsLineEntryEcThrshldUndrAlarm_Type()
)
lgpPduPsLineEntryEcThrshldUndrAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcThrshldUndrAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcThrshldUndrAlarm.setUnits("Percent")
_LgpPduPsLineEntryEcThrshldOvrWarn_Type = Unsigned32
_LgpPduPsLineEntryEcThrshldOvrWarn_Object = MibTableColumn
lgpPduPsLineEntryEcThrshldOvrWarn = _LgpPduPsLineEntryEcThrshldOvrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 36),
    _LgpPduPsLineEntryEcThrshldOvrWarn_Type()
)
lgpPduPsLineEntryEcThrshldOvrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcThrshldOvrWarn.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcThrshldOvrWarn.setUnits("Percent")
_LgpPduPsLineEntryEcThrshldOvrAlarm_Type = Unsigned32
_LgpPduPsLineEntryEcThrshldOvrAlarm_Object = MibTableColumn
lgpPduPsLineEntryEcThrshldOvrAlarm = _LgpPduPsLineEntryEcThrshldOvrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 37),
    _LgpPduPsLineEntryEcThrshldOvrAlarm_Type()
)
lgpPduPsLineEntryEcThrshldOvrAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcThrshldOvrAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcThrshldOvrAlarm.setUnits("Percent")
_LgpPduPsLineEntryEcAvailBeforeAlarm_Type = Unsigned32
_LgpPduPsLineEntryEcAvailBeforeAlarm_Object = MibTableColumn
lgpPduPsLineEntryEcAvailBeforeAlarm = _LgpPduPsLineEntryEcAvailBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 38),
    _LgpPduPsLineEntryEcAvailBeforeAlarm_Type()
)
lgpPduPsLineEntryEcAvailBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcAvailBeforeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcAvailBeforeAlarm.setUnits("0.1 Amps-AC-RMS")
_LgpPduPsLineEntryEcUsedBeforeAlarm_Type = Unsigned32
_LgpPduPsLineEntryEcUsedBeforeAlarm_Object = MibTableColumn
lgpPduPsLineEntryEcUsedBeforeAlarm = _LgpPduPsLineEntryEcUsedBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 39),
    _LgpPduPsLineEntryEcUsedBeforeAlarm_Type()
)
lgpPduPsLineEntryEcUsedBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcUsedBeforeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcUsedBeforeAlarm.setUnits("0.1 Percent")
_LgpPduPsLineEntryEpLL_Type = Unsigned32
_LgpPduPsLineEntryEpLL_Object = MibTableColumn
lgpPduPsLineEntryEpLL = _LgpPduPsLineEntryEpLL_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 60),
    _LgpPduPsLineEntryEpLL_Type()
)
lgpPduPsLineEntryEpLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLL.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLL.setUnits("Volts-AC-RMS")
_LgpPduPsLineEntryEpLLTenths_Type = Unsigned32
_LgpPduPsLineEntryEpLLTenths_Object = MibTableColumn
lgpPduPsLineEntryEpLLTenths = _LgpPduPsLineEntryEpLLTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 61),
    _LgpPduPsLineEntryEpLLTenths_Type()
)
lgpPduPsLineEntryEpLLTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLLTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLLTenths.setUnits("0.1 Volts-AC-RMS")
_LgpPduPsLineEntryEcAvailBeforeAlarmHundredths_Type = Unsigned32
_LgpPduPsLineEntryEcAvailBeforeAlarmHundredths_Object = MibTableColumn
lgpPduPsLineEntryEcAvailBeforeAlarmHundredths = _LgpPduPsLineEntryEcAvailBeforeAlarmHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 62),
    _LgpPduPsLineEntryEcAvailBeforeAlarmHundredths_Type()
)
lgpPduPsLineEntryEcAvailBeforeAlarmHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcAvailBeforeAlarmHundredths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcAvailBeforeAlarmHundredths.setUnits("0.01 Amps-AC-RMS")
_LgpPduReceptacleBranch_ObjectIdentity = ObjectIdentity
lgpPduReceptacleBranch = _LgpPduReceptacleBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40)
)
if mibBuilder.loadTexts:
    lgpPduReceptacleBranch.setStatus("current")
_LgpPduRbTableCount_Type = Unsigned32
_LgpPduRbTableCount_Object = MibScalar
lgpPduRbTableCount = _LgpPduRbTableCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 19),
    _LgpPduRbTableCount_Type()
)
lgpPduRbTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbTableCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbTableCount.setUnits("Count")
_LgpPduRbTable_Object = MibTable
lgpPduRbTable = _LgpPduRbTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20)
)
if mibBuilder.loadTexts:
    lgpPduRbTable.setStatus("current")
_LgpPduRbEntry_Object = MibTableRow
lgpPduRbEntry = _LgpPduRbEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1)
)
lgpPduRbEntry.setIndexNames(
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduRbEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpPduRbEntry.setStatus("current")
_LgpPduRbEntryIndex_Type = Unsigned32
_LgpPduRbEntryIndex_Object = MibTableColumn
lgpPduRbEntryIndex = _LgpPduRbEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 1),
    _LgpPduRbEntryIndex_Type()
)
lgpPduRbEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduRbEntryIndex.setStatus("current")
_LgpPduRbEntryId_Type = Unsigned32
_LgpPduRbEntryId_Object = MibTableColumn
lgpPduRbEntryId = _LgpPduRbEntryId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 5),
    _LgpPduRbEntryId_Type()
)
lgpPduRbEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryId.setStatus("current")
_LgpPduRbEntryUsrLabel_Type = DisplayString
_LgpPduRbEntryUsrLabel_Object = MibTableColumn
lgpPduRbEntryUsrLabel = _LgpPduRbEntryUsrLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 8),
    _LgpPduRbEntryUsrLabel_Type()
)
lgpPduRbEntryUsrLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryUsrLabel.setStatus("current")
_LgpPduRbEntrySysAssignLabel_Type = DisplayString
_LgpPduRbEntrySysAssignLabel_Object = MibTableColumn
lgpPduRbEntrySysAssignLabel = _LgpPduRbEntrySysAssignLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 20),
    _LgpPduRbEntrySysAssignLabel_Type()
)
lgpPduRbEntrySysAssignLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntrySysAssignLabel.setStatus("current")
_LgpPduRbEntryPositionRelative_Type = Unsigned32
_LgpPduRbEntryPositionRelative_Object = MibTableColumn
lgpPduRbEntryPositionRelative = _LgpPduRbEntryPositionRelative_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 25),
    _LgpPduRbEntryPositionRelative_Type()
)
lgpPduRbEntryPositionRelative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryPositionRelative.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryPositionRelative.setUnits("Count")
_LgpPduRbEntrySerialNum_Type = DisplayString
_LgpPduRbEntrySerialNum_Object = MibTableColumn
lgpPduRbEntrySerialNum = _LgpPduRbEntrySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 30),
    _LgpPduRbEntrySerialNum_Type()
)
lgpPduRbEntrySerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntrySerialNum.setStatus("current")
_LgpPduRbEntryModel_Type = DisplayString
_LgpPduRbEntryModel_Object = MibTableColumn
lgpPduRbEntryModel = _LgpPduRbEntryModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 35),
    _LgpPduRbEntryModel_Type()
)
lgpPduRbEntryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryModel.setStatus("current")
_LgpPduRbEntryFirmwareVersion_Type = DisplayString
_LgpPduRbEntryFirmwareVersion_Object = MibTableColumn
lgpPduRbEntryFirmwareVersion = _LgpPduRbEntryFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 40),
    _LgpPduRbEntryFirmwareVersion_Type()
)
lgpPduRbEntryFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryFirmwareVersion.setStatus("current")
_LgpPduRbEntryUsrTag1_Type = DisplayString
_LgpPduRbEntryUsrTag1_Object = MibTableColumn
lgpPduRbEntryUsrTag1 = _LgpPduRbEntryUsrTag1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 41),
    _LgpPduRbEntryUsrTag1_Type()
)
lgpPduRbEntryUsrTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryUsrTag1.setStatus("current")
_LgpPduRbEntryUsrTag2_Type = DisplayString
_LgpPduRbEntryUsrTag2_Object = MibTableColumn
lgpPduRbEntryUsrTag2 = _LgpPduRbEntryUsrTag2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 42),
    _LgpPduRbEntryUsrTag2_Type()
)
lgpPduRbEntryUsrTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryUsrTag2.setStatus("current")


class _LgpPduRbEntryReceptacleType_Type(Integer32):
    """Custom type lgpPduRbEntryReceptacleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cee-7-type-E-schuko", 7),
          ("iec-C13-sheet-F-10-Amp", 2),
          ("iec-C13-sheet-F-10-Amp-and-iec-C19-sheet-J-16-Amp", 4),
          ("iec-C19-sheet-J-16-Amp", 3),
          ("nema-5-20R-20-Amp", 1),
          ("nema-5-20R-20-Amp-and-iec-C13-sheet-F-10-Amp", 5),
          ("nema-5-20R-20-Amp-and-iec-C19-sheet-J-16-Amp", 6),
          ("not-specified", 0))
    )


_LgpPduRbEntryReceptacleType_Type.__name__ = "Integer32"
_LgpPduRbEntryReceptacleType_Object = MibTableColumn
lgpPduRbEntryReceptacleType = _LgpPduRbEntryReceptacleType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 45),
    _LgpPduRbEntryReceptacleType_Type()
)
lgpPduRbEntryReceptacleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryReceptacleType.setStatus("current")


class _LgpPduRbEntryCapabilities_Type(Integer32):
    """Custom type lgpPduRbEntryCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("control-only", 4),
          ("current-measurement-and-control", 6),
          ("current-measurement-only", 5),
          ("measurement-and-control", 3),
          ("measurement-only", 2),
          ("no-optional-capabilities", 1),
          ("not-specified", 0))
    )


_LgpPduRbEntryCapabilities_Type.__name__ = "Integer32"
_LgpPduRbEntryCapabilities_Object = MibTableColumn
lgpPduRbEntryCapabilities = _LgpPduRbEntryCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 50),
    _LgpPduRbEntryCapabilities_Type()
)
lgpPduRbEntryCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryCapabilities.setStatus("current")


class _LgpPduRbEntryLineSource_Type(Integer32):
    """Custom type lgpPduRbEntryLineSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("line-1-line-2", 4),
          ("line-1-line-2-and-line-1-neutral", 7),
          ("line-1-neutral", 1),
          ("line-2-line-3", 5),
          ("line-2-line-3-and-line-2-neutral", 8),
          ("line-2-neutral", 2),
          ("line-3-line-1", 6),
          ("line-3-line-1-and-line-3-neutral", 9),
          ("line-3-neutral", 3),
          ("not-specified", 0),
          ("unknown-line-line", 11),
          ("unknown-line-neutral", 10))
    )


_LgpPduRbEntryLineSource_Type.__name__ = "Integer32"
_LgpPduRbEntryLineSource_Object = MibTableColumn
lgpPduRbEntryLineSource = _LgpPduRbEntryLineSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 55),
    _LgpPduRbEntryLineSource_Type()
)
lgpPduRbEntryLineSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryLineSource.setStatus("current")
_LgpPduRbEntryRcpCount_Type = Unsigned32
_LgpPduRbEntryRcpCount_Object = MibTableColumn
lgpPduRbEntryRcpCount = _LgpPduRbEntryRcpCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 60),
    _LgpPduRbEntryRcpCount_Type()
)
lgpPduRbEntryRcpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryRcpCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryRcpCount.setUnits("Count")
_LgpPduRbEntryEpRated_Type = Unsigned32
_LgpPduRbEntryEpRated_Object = MibTableColumn
lgpPduRbEntryEpRated = _LgpPduRbEntryEpRated_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 70),
    _LgpPduRbEntryEpRated_Type()
)
lgpPduRbEntryEpRated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEpRated.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEpRated.setUnits("VoltRMS")
_LgpPduRbEntryEcRated_Type = Unsigned32
_LgpPduRbEntryEcRated_Object = MibTableColumn
lgpPduRbEntryEcRated = _LgpPduRbEntryEcRated_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 75),
    _LgpPduRbEntryEcRated_Type()
)
lgpPduRbEntryEcRated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcRated.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcRated.setUnits("0.1 Amp-AC-RMS")
_LgpPduRbEntryFreqRated_Type = Unsigned32
_LgpPduRbEntryFreqRated_Object = MibTableColumn
lgpPduRbEntryFreqRated = _LgpPduRbEntryFreqRated_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 80),
    _LgpPduRbEntryFreqRated_Type()
)
lgpPduRbEntryFreqRated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryFreqRated.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryFreqRated.setUnits("Hertz")
_LgpPduRbEntryEnergyAccum_Type = Unsigned32
_LgpPduRbEntryEnergyAccum_Object = MibTableColumn
lgpPduRbEntryEnergyAccum = _LgpPduRbEntryEnergyAccum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 85),
    _LgpPduRbEntryEnergyAccum_Type()
)
lgpPduRbEntryEnergyAccum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryEnergyAccum.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEnergyAccum.setUnits("0.1 Kilowatt-Hour")
_LgpPduRbEntryEpLNTenths_Type = Unsigned32
_LgpPduRbEntryEpLNTenths_Object = MibTableColumn
lgpPduRbEntryEpLNTenths = _LgpPduRbEntryEpLNTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 100),
    _LgpPduRbEntryEpLNTenths_Type()
)
lgpPduRbEntryEpLNTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEpLNTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEpLNTenths.setUnits("0.1 VoltRMS")
_LgpPduRbEntryPwr_Type = Unsigned32
_LgpPduRbEntryPwr_Object = MibTableColumn
lgpPduRbEntryPwr = _LgpPduRbEntryPwr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 115),
    _LgpPduRbEntryPwr_Type()
)
lgpPduRbEntryPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryPwr.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryPwr.setUnits("Watt")
_LgpPduRbEntryAp_Type = Unsigned32
_LgpPduRbEntryAp_Object = MibTableColumn
lgpPduRbEntryAp = _LgpPduRbEntryAp_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 120),
    _LgpPduRbEntryAp_Type()
)
lgpPduRbEntryAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryAp.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryAp.setUnits("VoltAmp")
_LgpPduRbEntryPf_Type = Integer32
_LgpPduRbEntryPf_Object = MibTableColumn
lgpPduRbEntryPf = _LgpPduRbEntryPf_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 125),
    _LgpPduRbEntryPf_Type()
)
lgpPduRbEntryPf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryPf.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryPf.setUnits("0.01 Power Factor")
_LgpPduRbEntryEcHundredths_Type = Unsigned32
_LgpPduRbEntryEcHundredths_Object = MibTableColumn
lgpPduRbEntryEcHundredths = _LgpPduRbEntryEcHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 130),
    _LgpPduRbEntryEcHundredths_Type()
)
lgpPduRbEntryEcHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcHundredths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcHundredths.setUnits("0.01 Amp-AC-RMS")
_LgpPduRbEntryEcThrshldUndrAlm_Type = Unsigned32
_LgpPduRbEntryEcThrshldUndrAlm_Object = MibTableColumn
lgpPduRbEntryEcThrshldUndrAlm = _LgpPduRbEntryEcThrshldUndrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 135),
    _LgpPduRbEntryEcThrshldUndrAlm_Type()
)
lgpPduRbEntryEcThrshldUndrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcThrshldUndrAlm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcThrshldUndrAlm.setUnits("Percent")
_LgpPduRbEntryEcThrshldOvrWarn_Type = Unsigned32
_LgpPduRbEntryEcThrshldOvrWarn_Object = MibTableColumn
lgpPduRbEntryEcThrshldOvrWarn = _LgpPduRbEntryEcThrshldOvrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 140),
    _LgpPduRbEntryEcThrshldOvrWarn_Type()
)
lgpPduRbEntryEcThrshldOvrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcThrshldOvrWarn.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcThrshldOvrWarn.setUnits("Percent")
_LgpPduRbEntryEcThrshldOvrAlm_Type = Unsigned32
_LgpPduRbEntryEcThrshldOvrAlm_Object = MibTableColumn
lgpPduRbEntryEcThrshldOvrAlm = _LgpPduRbEntryEcThrshldOvrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 145),
    _LgpPduRbEntryEcThrshldOvrAlm_Type()
)
lgpPduRbEntryEcThrshldOvrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcThrshldOvrAlm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcThrshldOvrAlm.setUnits("Percent")
_LgpPduRbEntryEcAvailBeforeAlarmHundredths_Type = Unsigned32
_LgpPduRbEntryEcAvailBeforeAlarmHundredths_Object = MibTableColumn
lgpPduRbEntryEcAvailBeforeAlarmHundredths = _LgpPduRbEntryEcAvailBeforeAlarmHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 150),
    _LgpPduRbEntryEcAvailBeforeAlarmHundredths_Type()
)
lgpPduRbEntryEcAvailBeforeAlarmHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcAvailBeforeAlarmHundredths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcAvailBeforeAlarmHundredths.setUnits("0.01 Amps-AC-RMS")
_LgpPduRbEntryEcUsedBeforeAlarm_Type = Unsigned32
_LgpPduRbEntryEcUsedBeforeAlarm_Object = MibTableColumn
lgpPduRbEntryEcUsedBeforeAlarm = _LgpPduRbEntryEcUsedBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 160),
    _LgpPduRbEntryEcUsedBeforeAlarm_Type()
)
lgpPduRbEntryEcUsedBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcUsedBeforeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcUsedBeforeAlarm.setUnits("0.1 Percent")
_LgpPduRbEntryEpLLTenths_Type = Unsigned32
_LgpPduRbEntryEpLLTenths_Object = MibTableColumn
lgpPduRbEntryEpLLTenths = _LgpPduRbEntryEpLLTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 170),
    _LgpPduRbEntryEpLLTenths_Type()
)
lgpPduRbEntryEpLLTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEpLLTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEpLLTenths.setUnits("0.1 VoltRMS")
_LgpPduRbLineTable_Object = MibTable
lgpPduRbLineTable = _LgpPduRbLineTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40)
)
if mibBuilder.loadTexts:
    lgpPduRbLineTable.setStatus("deprecated")
_LgpPduRbLineEntry_Object = MibTableRow
lgpPduRbLineEntry = _LgpPduRbLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1)
)
lgpPduRbLineEntry.setIndexNames(
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduRbEntryIndex"),
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduRbLineEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpPduRbLineEntry.setStatus("deprecated")
_LgpPduRbLineEntryIndex_Type = Unsigned32
_LgpPduRbLineEntryIndex_Object = MibTableColumn
lgpPduRbLineEntryIndex = _LgpPduRbLineEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 1),
    _LgpPduRbLineEntryIndex_Type()
)
lgpPduRbLineEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryIndex.setStatus("deprecated")
_LgpPduRbLineEntryId_Type = Unsigned32
_LgpPduRbLineEntryId_Object = MibTableColumn
lgpPduRbLineEntryId = _LgpPduRbLineEntryId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 5),
    _LgpPduRbLineEntryId_Type()
)
lgpPduRbLineEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryId.setStatus("deprecated")


class _LgpPduRbLineEntryLine_Type(Integer32):
    """Custom type lgpPduRbLineEntryLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3))
    )


_LgpPduRbLineEntryLine_Type.__name__ = "Integer32"
_LgpPduRbLineEntryLine_Object = MibTableColumn
lgpPduRbLineEntryLine = _LgpPduRbLineEntryLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 10),
    _LgpPduRbLineEntryLine_Type()
)
lgpPduRbLineEntryLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryLine.setStatus("deprecated")
_LgpPduRbLineEntryEpLNTenths_Type = Unsigned32
_LgpPduRbLineEntryEpLNTenths_Object = MibTableColumn
lgpPduRbLineEntryEpLNTenths = _LgpPduRbLineEntryEpLNTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 19),
    _LgpPduRbLineEntryEpLNTenths_Type()
)
lgpPduRbLineEntryEpLNTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLNTenths.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLNTenths.setUnits("0.1 VoltRMS")
_LgpPduRbLineEntryEpLN_Type = Unsigned32
_LgpPduRbLineEntryEpLN_Object = MibTableColumn
lgpPduRbLineEntryEpLN = _LgpPduRbLineEntryEpLN_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 20),
    _LgpPduRbLineEntryEpLN_Type()
)
lgpPduRbLineEntryEpLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLN.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLN.setUnits("VoltRMS")
_LgpPduRbLineEntryEc_Type = Unsigned32
_LgpPduRbLineEntryEc_Object = MibTableColumn
lgpPduRbLineEntryEc = _LgpPduRbLineEntryEc_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 21),
    _LgpPduRbLineEntryEc_Type()
)
lgpPduRbLineEntryEc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEc.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEc.setUnits("0.1 Amp-AC-RMS")
_LgpPduRbLineEntryPwr_Type = Unsigned32
_LgpPduRbLineEntryPwr_Object = MibTableColumn
lgpPduRbLineEntryPwr = _LgpPduRbLineEntryPwr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 22),
    _LgpPduRbLineEntryPwr_Type()
)
lgpPduRbLineEntryPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryPwr.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryPwr.setUnits("Watt")
_LgpPduRbLineEntryAp_Type = Unsigned32
_LgpPduRbLineEntryAp_Object = MibTableColumn
lgpPduRbLineEntryAp = _LgpPduRbLineEntryAp_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 23),
    _LgpPduRbLineEntryAp_Type()
)
lgpPduRbLineEntryAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryAp.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryAp.setUnits("VoltAmp")
_LgpPduRbLineEntryPf_Type = Integer32
_LgpPduRbLineEntryPf_Object = MibTableColumn
lgpPduRbLineEntryPf = _LgpPduRbLineEntryPf_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 24),
    _LgpPduRbLineEntryPf_Type()
)
lgpPduRbLineEntryPf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryPf.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryPf.setUnits("0.01 Power Factor")
_LgpPduRbLineEntryEcHundredths_Type = Unsigned32
_LgpPduRbLineEntryEcHundredths_Object = MibTableColumn
lgpPduRbLineEntryEcHundredths = _LgpPduRbLineEntryEcHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 25),
    _LgpPduRbLineEntryEcHundredths_Type()
)
lgpPduRbLineEntryEcHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcHundredths.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcHundredths.setUnits("0.01 Amp-AC-RMS")
_LgpPduRbLineEntryEcThrshldUndrAlm_Type = Unsigned32
_LgpPduRbLineEntryEcThrshldUndrAlm_Object = MibTableColumn
lgpPduRbLineEntryEcThrshldUndrAlm = _LgpPduRbLineEntryEcThrshldUndrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 35),
    _LgpPduRbLineEntryEcThrshldUndrAlm_Type()
)
lgpPduRbLineEntryEcThrshldUndrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcThrshldUndrAlm.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcThrshldUndrAlm.setUnits("Percent")
_LgpPduRbLineEntryEcThrshldOvrWarn_Type = Unsigned32
_LgpPduRbLineEntryEcThrshldOvrWarn_Object = MibTableColumn
lgpPduRbLineEntryEcThrshldOvrWarn = _LgpPduRbLineEntryEcThrshldOvrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 36),
    _LgpPduRbLineEntryEcThrshldOvrWarn_Type()
)
lgpPduRbLineEntryEcThrshldOvrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcThrshldOvrWarn.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcThrshldOvrWarn.setUnits("Percent")
_LgpPduRbLineEntryEcThrshldOvrAlm_Type = Unsigned32
_LgpPduRbLineEntryEcThrshldOvrAlm_Object = MibTableColumn
lgpPduRbLineEntryEcThrshldOvrAlm = _LgpPduRbLineEntryEcThrshldOvrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 37),
    _LgpPduRbLineEntryEcThrshldOvrAlm_Type()
)
lgpPduRbLineEntryEcThrshldOvrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcThrshldOvrAlm.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcThrshldOvrAlm.setUnits("Percent")
_LgpPduRbLineEntryEcAvailBeforeAlarmHundredths_Type = Unsigned32
_LgpPduRbLineEntryEcAvailBeforeAlarmHundredths_Object = MibTableColumn
lgpPduRbLineEntryEcAvailBeforeAlarmHundredths = _LgpPduRbLineEntryEcAvailBeforeAlarmHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 39),
    _LgpPduRbLineEntryEcAvailBeforeAlarmHundredths_Type()
)
lgpPduRbLineEntryEcAvailBeforeAlarmHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcAvailBeforeAlarmHundredths.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcAvailBeforeAlarmHundredths.setUnits("0.01 Amps-AC-RMS")
_LgpPduRbLineEntryEcAvailBeforeAlarm_Type = Unsigned32
_LgpPduRbLineEntryEcAvailBeforeAlarm_Object = MibTableColumn
lgpPduRbLineEntryEcAvailBeforeAlarm = _LgpPduRbLineEntryEcAvailBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 40),
    _LgpPduRbLineEntryEcAvailBeforeAlarm_Type()
)
lgpPduRbLineEntryEcAvailBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcAvailBeforeAlarm.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcAvailBeforeAlarm.setUnits("0.1 Amps-AC-RMS")
_LgpPduRbLineEntryEcUsedBeforeAlarm_Type = Unsigned32
_LgpPduRbLineEntryEcUsedBeforeAlarm_Object = MibTableColumn
lgpPduRbLineEntryEcUsedBeforeAlarm = _LgpPduRbLineEntryEcUsedBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 41),
    _LgpPduRbLineEntryEcUsedBeforeAlarm_Type()
)
lgpPduRbLineEntryEcUsedBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcUsedBeforeAlarm.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcUsedBeforeAlarm.setUnits("0.1 Percent")
_LgpPduRbLineEntryEpLL_Type = Unsigned32
_LgpPduRbLineEntryEpLL_Object = MibTableColumn
lgpPduRbLineEntryEpLL = _LgpPduRbLineEntryEpLL_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 60),
    _LgpPduRbLineEntryEpLL_Type()
)
lgpPduRbLineEntryEpLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLL.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLL.setUnits("VoltRMS")
_LgpPduRbLineEntryEpLLTenths_Type = Unsigned32
_LgpPduRbLineEntryEpLLTenths_Object = MibTableColumn
lgpPduRbLineEntryEpLLTenths = _LgpPduRbLineEntryEpLLTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 61),
    _LgpPduRbLineEntryEpLLTenths_Type()
)
lgpPduRbLineEntryEpLLTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLLTenths.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLLTenths.setUnits("0.1 VoltRMS")
_LgpPduReceptacle_ObjectIdentity = ObjectIdentity
lgpPduReceptacle = _LgpPduReceptacle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50)
)
if mibBuilder.loadTexts:
    lgpPduReceptacle.setStatus("current")
_LgpPduRcpTableCount_Type = Unsigned32
_LgpPduRcpTableCount_Object = MibScalar
lgpPduRcpTableCount = _LgpPduRcpTableCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 19),
    _LgpPduRcpTableCount_Type()
)
lgpPduRcpTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpTableCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpTableCount.setUnits("Count")
_LgpPduRcpTable_Object = MibTable
lgpPduRcpTable = _LgpPduRcpTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20)
)
if mibBuilder.loadTexts:
    lgpPduRcpTable.setStatus("current")
_LgpPduRcpEntry_Object = MibTableRow
lgpPduRcpEntry = _LgpPduRcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1)
)
lgpPduRcpEntry.setIndexNames(
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduRbEntryIndex"),
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduRcpEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpPduRcpEntry.setStatus("current")
_LgpPduRcpEntryIndex_Type = Unsigned32
_LgpPduRcpEntryIndex_Object = MibTableColumn
lgpPduRcpEntryIndex = _LgpPduRcpEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 1),
    _LgpPduRcpEntryIndex_Type()
)
lgpPduRcpEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduRcpEntryIndex.setStatus("current")
_LgpPduRcpEntryId_Type = Unsigned32
_LgpPduRcpEntryId_Object = MibTableColumn
lgpPduRcpEntryId = _LgpPduRcpEntryId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 5),
    _LgpPduRcpEntryId_Type()
)
lgpPduRcpEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryId.setStatus("current")
_LgpPduRcpEntryUsrLabel_Type = DisplayString
_LgpPduRcpEntryUsrLabel_Object = MibTableColumn
lgpPduRcpEntryUsrLabel = _LgpPduRcpEntryUsrLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 10),
    _LgpPduRcpEntryUsrLabel_Type()
)
lgpPduRcpEntryUsrLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryUsrLabel.setStatus("current")
_LgpPduRcpEntryUsrTag1_Type = DisplayString
_LgpPduRcpEntryUsrTag1_Object = MibTableColumn
lgpPduRcpEntryUsrTag1 = _LgpPduRcpEntryUsrTag1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 15),
    _LgpPduRcpEntryUsrTag1_Type()
)
lgpPduRcpEntryUsrTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryUsrTag1.setStatus("current")
_LgpPduRcpEntryUsrTag2_Type = DisplayString
_LgpPduRcpEntryUsrTag2_Object = MibTableColumn
lgpPduRcpEntryUsrTag2 = _LgpPduRcpEntryUsrTag2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 20),
    _LgpPduRcpEntryUsrTag2_Type()
)
lgpPduRcpEntryUsrTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryUsrTag2.setStatus("current")
_LgpPduRcpEntrySysAssignLabel_Type = DisplayString
_LgpPduRcpEntrySysAssignLabel_Object = MibTableColumn
lgpPduRcpEntrySysAssignLabel = _LgpPduRcpEntrySysAssignLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 25),
    _LgpPduRcpEntrySysAssignLabel_Type()
)
lgpPduRcpEntrySysAssignLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntrySysAssignLabel.setStatus("current")
_LgpPduRcpEntryPosition_Type = Unsigned32
_LgpPduRcpEntryPosition_Object = MibTableColumn
lgpPduRcpEntryPosition = _LgpPduRcpEntryPosition_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 30),
    _LgpPduRcpEntryPosition_Type()
)
lgpPduRcpEntryPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPosition.setStatus("current")


class _LgpPduRcpEntryType_Type(Integer32):
    """Custom type lgpPduRcpEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cee-7-type-E-schuko", 7),
          ("iec-C13-sheet-F-10-Amp", 2),
          ("iec-C19-sheet-J-16-Amp", 3),
          ("nema-5-20R-20-Amp", 1),
          ("not-specified", 0))
    )


_LgpPduRcpEntryType_Type.__name__ = "Integer32"
_LgpPduRcpEntryType_Object = MibTableColumn
lgpPduRcpEntryType = _LgpPduRcpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 40),
    _LgpPduRcpEntryType_Type()
)
lgpPduRcpEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryType.setStatus("current")


class _LgpPduRcpEntryLineSource_Type(Integer32):
    """Custom type lgpPduRcpEntryLineSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("line-1-N", 1),
          ("line-1-line-2", 4),
          ("line-2-N", 2),
          ("line-2-line-3", 5),
          ("line-3-N", 3),
          ("line-3-line-1", 6),
          ("not-specified", 0),
          ("unknown-line-line", 8),
          ("unknown-line-neutral", 7))
    )


_LgpPduRcpEntryLineSource_Type.__name__ = "Integer32"
_LgpPduRcpEntryLineSource_Object = MibTableColumn
lgpPduRcpEntryLineSource = _LgpPduRcpEntryLineSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 45),
    _LgpPduRcpEntryLineSource_Type()
)
lgpPduRcpEntryLineSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryLineSource.setStatus("current")


class _LgpPduRcpEntryCapabilities_Type(Integer32):
    """Custom type lgpPduRcpEntryCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("control-only", 4),
          ("current-measurement-and-control", 6),
          ("current-measurement-only", 5),
          ("measurement-and-control", 3),
          ("measurement-only", 2),
          ("no-optional-capabilities", 1),
          ("not-specified", 0))
    )


_LgpPduRcpEntryCapabilities_Type.__name__ = "Integer32"
_LgpPduRcpEntryCapabilities_Object = MibTableColumn
lgpPduRcpEntryCapabilities = _LgpPduRcpEntryCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 50),
    _LgpPduRcpEntryCapabilities_Type()
)
lgpPduRcpEntryCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryCapabilities.setStatus("current")
_LgpPduRcpEntryEp_Type = Unsigned32
_LgpPduRcpEntryEp_Object = MibTableColumn
lgpPduRcpEntryEp = _LgpPduRcpEntryEp_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 55),
    _LgpPduRcpEntryEp_Type()
)
lgpPduRcpEntryEp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEp.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEp.setUnits("Volts-AC-RMS")
_LgpPduRcpEntryEpTenths_Type = Unsigned32
_LgpPduRcpEntryEpTenths_Object = MibTableColumn
lgpPduRcpEntryEpTenths = _LgpPduRcpEntryEpTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 56),
    _LgpPduRcpEntryEpTenths_Type()
)
lgpPduRcpEntryEpTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEpTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEpTenths.setUnits("0.1 Volts-AC-RMS")
_LgpPduRcpEntryEc_Type = Unsigned32
_LgpPduRcpEntryEc_Object = MibTableColumn
lgpPduRcpEntryEc = _LgpPduRcpEntryEc_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 60),
    _LgpPduRcpEntryEc_Type()
)
lgpPduRcpEntryEc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEc.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEc.setUnits("0.1 Amp-AC-RMS")
_LgpPduRcpEntryEcHundredths_Type = Unsigned32
_LgpPduRcpEntryEcHundredths_Object = MibTableColumn
lgpPduRcpEntryEcHundredths = _LgpPduRcpEntryEcHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 61),
    _LgpPduRcpEntryEcHundredths_Type()
)
lgpPduRcpEntryEcHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcHundredths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcHundredths.setUnits("0.01 Amp-AC-RMS")
_LgpPduRcpEntryPwrOut_Type = Unsigned32
_LgpPduRcpEntryPwrOut_Object = MibTableColumn
lgpPduRcpEntryPwrOut = _LgpPduRcpEntryPwrOut_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 65),
    _LgpPduRcpEntryPwrOut_Type()
)
lgpPduRcpEntryPwrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPwrOut.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPwrOut.setUnits("Watt")
_LgpPduRcpEntryApOut_Type = Unsigned32
_LgpPduRcpEntryApOut_Object = MibTableColumn
lgpPduRcpEntryApOut = _LgpPduRcpEntryApOut_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 70),
    _LgpPduRcpEntryApOut_Type()
)
lgpPduRcpEntryApOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryApOut.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryApOut.setUnits("Volt-Amp-RMS")
_LgpPduRcpEntryPf_Type = Unsigned32
_LgpPduRcpEntryPf_Object = MibTableColumn
lgpPduRcpEntryPf = _LgpPduRcpEntryPf_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 75),
    _LgpPduRcpEntryPf_Type()
)
lgpPduRcpEntryPf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPf.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPf.setUnits(".01 Power Factor")
_LgpPduRcpEntryFreq_Type = Unsigned32
_LgpPduRcpEntryFreq_Object = MibTableColumn
lgpPduRcpEntryFreq = _LgpPduRcpEntryFreq_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 80),
    _LgpPduRcpEntryFreq_Type()
)
lgpPduRcpEntryFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryFreq.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryFreq.setUnits("0.1 Hertz")
_LgpPduRcpEntryEnergyAccum_Type = Unsigned32
_LgpPduRcpEntryEnergyAccum_Object = MibTableColumn
lgpPduRcpEntryEnergyAccum = _LgpPduRcpEntryEnergyAccum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 85),
    _LgpPduRcpEntryEnergyAccum_Type()
)
lgpPduRcpEntryEnergyAccum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEnergyAccum.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEnergyAccum.setUnits("0.1 Kilowatt-Hour")
_LgpPduRcpEntryPwrOnDelay_Type = Unsigned32
_LgpPduRcpEntryPwrOnDelay_Object = MibTableColumn
lgpPduRcpEntryPwrOnDelay = _LgpPduRcpEntryPwrOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 90),
    _LgpPduRcpEntryPwrOnDelay_Type()
)
lgpPduRcpEntryPwrOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPwrOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPwrOnDelay.setUnits("Seconds")


class _LgpPduRcpEntryPwrState_Type(Integer32):
    """Custom type lgpPduRcpEntryPwrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("off-pending-on-delay", 3),
          ("on", 2),
          ("unknown", 0))
    )


_LgpPduRcpEntryPwrState_Type.__name__ = "Integer32"
_LgpPduRcpEntryPwrState_Object = MibTableColumn
lgpPduRcpEntryPwrState = _LgpPduRcpEntryPwrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 95),
    _LgpPduRcpEntryPwrState_Type()
)
lgpPduRcpEntryPwrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPwrState.setStatus("current")


class _LgpPduRcpEntryControl_Type(Integer32):
    """Custom type lgpPduRcpEntryControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cycle-power", 2),
          ("off", 0),
          ("on", 1))
    )


_LgpPduRcpEntryControl_Type.__name__ = "Integer32"
_LgpPduRcpEntryControl_Object = MibTableColumn
lgpPduRcpEntryControl = _LgpPduRcpEntryControl_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 100),
    _LgpPduRcpEntryControl_Type()
)
lgpPduRcpEntryControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryControl.setStatus("current")


class _LgpPduRcpEntryControlLock_Type(Integer32):
    """Custom type lgpPduRcpEntryControlLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unknown", 0),
          ("unlocked", 1))
    )


_LgpPduRcpEntryControlLock_Type.__name__ = "Integer32"
_LgpPduRcpEntryControlLock_Object = MibTableColumn
lgpPduRcpEntryControlLock = _LgpPduRcpEntryControlLock_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 105),
    _LgpPduRcpEntryControlLock_Type()
)
lgpPduRcpEntryControlLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryControlLock.setStatus("current")
_LgpPduRcpEntryEcThrshldUnderAlarm_Type = Unsigned32
_LgpPduRcpEntryEcThrshldUnderAlarm_Object = MibTableColumn
lgpPduRcpEntryEcThrshldUnderAlarm = _LgpPduRcpEntryEcThrshldUnderAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 150),
    _LgpPduRcpEntryEcThrshldUnderAlarm_Type()
)
lgpPduRcpEntryEcThrshldUnderAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcThrshldUnderAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcThrshldUnderAlarm.setUnits("Percent")
_LgpPduRcpEntryEcThrshldOverWarn_Type = Unsigned32
_LgpPduRcpEntryEcThrshldOverWarn_Object = MibTableColumn
lgpPduRcpEntryEcThrshldOverWarn = _LgpPduRcpEntryEcThrshldOverWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 151),
    _LgpPduRcpEntryEcThrshldOverWarn_Type()
)
lgpPduRcpEntryEcThrshldOverWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcThrshldOverWarn.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcThrshldOverWarn.setUnits("Percent")
_LgpPduRcpEntryEcThrshldOverAlarm_Type = Unsigned32
_LgpPduRcpEntryEcThrshldOverAlarm_Object = MibTableColumn
lgpPduRcpEntryEcThrshldOverAlarm = _LgpPduRcpEntryEcThrshldOverAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 152),
    _LgpPduRcpEntryEcThrshldOverAlarm_Type()
)
lgpPduRcpEntryEcThrshldOverAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcThrshldOverAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcThrshldOverAlarm.setUnits("Percent")
_LgpPduRcpEntryEcAvailBeforeAlarmHundredths_Type = Unsigned32
_LgpPduRcpEntryEcAvailBeforeAlarmHundredths_Object = MibTableColumn
lgpPduRcpEntryEcAvailBeforeAlarmHundredths = _LgpPduRcpEntryEcAvailBeforeAlarmHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 159),
    _LgpPduRcpEntryEcAvailBeforeAlarmHundredths_Type()
)
lgpPduRcpEntryEcAvailBeforeAlarmHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcAvailBeforeAlarmHundredths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcAvailBeforeAlarmHundredths.setUnits("0.01 Amps-AC-RMS")
_LgpPduRcpEntryEcAvailBeforeAlarm_Type = Unsigned32
_LgpPduRcpEntryEcAvailBeforeAlarm_Object = MibTableColumn
lgpPduRcpEntryEcAvailBeforeAlarm = _LgpPduRcpEntryEcAvailBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 160),
    _LgpPduRcpEntryEcAvailBeforeAlarm_Type()
)
lgpPduRcpEntryEcAvailBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcAvailBeforeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcAvailBeforeAlarm.setUnits("0.1 Amps-AC-RMS")
_LgpPduRcpEntryEcUsedBeforeAlarm_Type = Unsigned32
_LgpPduRcpEntryEcUsedBeforeAlarm_Object = MibTableColumn
lgpPduRcpEntryEcUsedBeforeAlarm = _LgpPduRcpEntryEcUsedBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 161),
    _LgpPduRcpEntryEcUsedBeforeAlarm_Type()
)
lgpPduRcpEntryEcUsedBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcUsedBeforeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcUsedBeforeAlarm.setUnits("0.1 Percent")
_LgpPduRcpEntryEcCrestFactor_Type = Unsigned32
_LgpPduRcpEntryEcCrestFactor_Object = MibTableColumn
lgpPduRcpEntryEcCrestFactor = _LgpPduRcpEntryEcCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 162),
    _LgpPduRcpEntryEcCrestFactor_Type()
)
lgpPduRcpEntryEcCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcCrestFactor.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcCrestFactor.setUnits("0.01")


class _LgpPduRcpEntryBlinkLED_Type(Integer32):
    """Custom type lgpPduRcpEntryBlinkLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blinkLED", 2),
          ("noAction", 1))
    )


_LgpPduRcpEntryBlinkLED_Type.__name__ = "Integer32"
_LgpPduRcpEntryBlinkLED_Object = MibTableColumn
lgpPduRcpEntryBlinkLED = _LgpPduRcpEntryBlinkLED_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 200),
    _LgpPduRcpEntryBlinkLED_Type()
)
lgpPduRcpEntryBlinkLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryBlinkLED.setStatus("current")
_LgpPduAuxiliarySensors_ObjectIdentity = ObjectIdentity
lgpPduAuxiliarySensors = _LgpPduAuxiliarySensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60)
)
if mibBuilder.loadTexts:
    lgpPduAuxiliarySensors.setStatus("current")
_LgpPduAuxSensorCount_Type = Unsigned32
_LgpPduAuxSensorCount_Object = MibScalar
lgpPduAuxSensorCount = _LgpPduAuxSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 5),
    _LgpPduAuxSensorCount_Type()
)
lgpPduAuxSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxSensorCount.setUnits("Count")
_LgpPduAuxSensorTable_Object = MibTable
lgpPduAuxSensorTable = _LgpPduAuxSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10)
)
if mibBuilder.loadTexts:
    lgpPduAuxSensorTable.setStatus("deprecated")
_LgpPduAuxSensorEntry_Object = MibTableRow
lgpPduAuxSensorEntry = _LgpPduAuxSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1)
)
lgpPduAuxSensorEntry.setIndexNames(
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduAuxSensorIndex"),
)
if mibBuilder.loadTexts:
    lgpPduAuxSensorEntry.setStatus("deprecated")
_LgpPduAuxSensorIndex_Type = Unsigned32
_LgpPduAuxSensorIndex_Object = MibTableColumn
lgpPduAuxSensorIndex = _LgpPduAuxSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 1),
    _LgpPduAuxSensorIndex_Type()
)
lgpPduAuxSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduAuxSensorIndex.setStatus("deprecated")


class _LgpPduAuxSensorMeasType_Type(Integer32):
    """Custom type lgpPduAuxSensorMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("humidity", 2),
          ("not-specified", 0),
          ("temperature", 1),
          ("temperature-and-humidity", 3))
    )


_LgpPduAuxSensorMeasType_Type.__name__ = "Integer32"
_LgpPduAuxSensorMeasType_Object = MibTableColumn
lgpPduAuxSensorMeasType = _LgpPduAuxSensorMeasType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 5),
    _LgpPduAuxSensorMeasType_Type()
)
lgpPduAuxSensorMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorMeasType.setStatus("deprecated")
_LgpPduAuxSensorId_Type = Unsigned32
_LgpPduAuxSensorId_Object = MibTableColumn
lgpPduAuxSensorId = _LgpPduAuxSensorId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 10),
    _LgpPduAuxSensorId_Type()
)
lgpPduAuxSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorId.setStatus("deprecated")
_LgpPduAuxSensorSysAssignLabel_Type = DisplayString
_LgpPduAuxSensorSysAssignLabel_Object = MibTableColumn
lgpPduAuxSensorSysAssignLabel = _LgpPduAuxSensorSysAssignLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 15),
    _LgpPduAuxSensorSysAssignLabel_Type()
)
lgpPduAuxSensorSysAssignLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorSysAssignLabel.setStatus("deprecated")
_LgpPduAuxSensorPositionRelative_Type = Unsigned32
_LgpPduAuxSensorPositionRelative_Object = MibTableColumn
lgpPduAuxSensorPositionRelative = _LgpPduAuxSensorPositionRelative_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 20),
    _LgpPduAuxSensorPositionRelative_Type()
)
lgpPduAuxSensorPositionRelative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorPositionRelative.setStatus("deprecated")
_LgpPduAuxSensorUsrLabel_Type = DisplayString
_LgpPduAuxSensorUsrLabel_Object = MibTableColumn
lgpPduAuxSensorUsrLabel = _LgpPduAuxSensorUsrLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 25),
    _LgpPduAuxSensorUsrLabel_Type()
)
lgpPduAuxSensorUsrLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorUsrLabel.setStatus("deprecated")
_LgpPduAuxSensorUsrTag1_Type = DisplayString
_LgpPduAuxSensorUsrTag1_Object = MibTableColumn
lgpPduAuxSensorUsrTag1 = _LgpPduAuxSensorUsrTag1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 30),
    _LgpPduAuxSensorUsrTag1_Type()
)
lgpPduAuxSensorUsrTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorUsrTag1.setStatus("deprecated")
_LgpPduAuxSensorUsrTag2_Type = DisplayString
_LgpPduAuxSensorUsrTag2_Object = MibTableColumn
lgpPduAuxSensorUsrTag2 = _LgpPduAuxSensorUsrTag2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 35),
    _LgpPduAuxSensorUsrTag2_Type()
)
lgpPduAuxSensorUsrTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorUsrTag2.setStatus("deprecated")
_LgpPduAuxSensorTempSerialNum_Type = DisplayString
_LgpPduAuxSensorTempSerialNum_Object = MibTableColumn
lgpPduAuxSensorTempSerialNum = _LgpPduAuxSensorTempSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 40),
    _LgpPduAuxSensorTempSerialNum_Type()
)
lgpPduAuxSensorTempSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempSerialNum.setStatus("deprecated")
_LgpPduAuxSensorHumSerialNum_Type = DisplayString
_LgpPduAuxSensorHumSerialNum_Object = MibTableColumn
lgpPduAuxSensorHumSerialNum = _LgpPduAuxSensorHumSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 45),
    _LgpPduAuxSensorHumSerialNum_Type()
)
lgpPduAuxSensorHumSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumSerialNum.setStatus("deprecated")
_LgpPduAuxSensorTempMeasurementDegF_Type = Integer32
_LgpPduAuxSensorTempMeasurementDegF_Object = MibTableColumn
lgpPduAuxSensorTempMeasurementDegF = _LgpPduAuxSensorTempMeasurementDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 50),
    _LgpPduAuxSensorTempMeasurementDegF_Type()
)
lgpPduAuxSensorTempMeasurementDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempMeasurementDegF.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempMeasurementDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxSensorTempThrshldUndrAlmDegF_Type = Integer32
_LgpPduAuxSensorTempThrshldUndrAlmDegF_Object = MibTableColumn
lgpPduAuxSensorTempThrshldUndrAlmDegF = _LgpPduAuxSensorTempThrshldUndrAlmDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 55),
    _LgpPduAuxSensorTempThrshldUndrAlmDegF_Type()
)
lgpPduAuxSensorTempThrshldUndrAlmDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrAlmDegF.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrAlmDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxSensorTempThrshldOvrAlmDegF_Type = Integer32
_LgpPduAuxSensorTempThrshldOvrAlmDegF_Object = MibTableColumn
lgpPduAuxSensorTempThrshldOvrAlmDegF = _LgpPduAuxSensorTempThrshldOvrAlmDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 60),
    _LgpPduAuxSensorTempThrshldOvrAlmDegF_Type()
)
lgpPduAuxSensorTempThrshldOvrAlmDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrAlmDegF.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrAlmDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxSensorTempThrshldUndrWarnDegF_Type = Integer32
_LgpPduAuxSensorTempThrshldUndrWarnDegF_Object = MibTableColumn
lgpPduAuxSensorTempThrshldUndrWarnDegF = _LgpPduAuxSensorTempThrshldUndrWarnDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 65),
    _LgpPduAuxSensorTempThrshldUndrWarnDegF_Type()
)
lgpPduAuxSensorTempThrshldUndrWarnDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrWarnDegF.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrWarnDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxSensorTempThrshldOvrWarnDegF_Type = Integer32
_LgpPduAuxSensorTempThrshldOvrWarnDegF_Object = MibTableColumn
lgpPduAuxSensorTempThrshldOvrWarnDegF = _LgpPduAuxSensorTempThrshldOvrWarnDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 70),
    _LgpPduAuxSensorTempThrshldOvrWarnDegF_Type()
)
lgpPduAuxSensorTempThrshldOvrWarnDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrWarnDegF.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrWarnDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxSensorTempMeasurementDegC_Type = Integer32
_LgpPduAuxSensorTempMeasurementDegC_Object = MibTableColumn
lgpPduAuxSensorTempMeasurementDegC = _LgpPduAuxSensorTempMeasurementDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 75),
    _LgpPduAuxSensorTempMeasurementDegC_Type()
)
lgpPduAuxSensorTempMeasurementDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempMeasurementDegC.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempMeasurementDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxSensorTempThrshldUndrAlmDegC_Type = Integer32
_LgpPduAuxSensorTempThrshldUndrAlmDegC_Object = MibTableColumn
lgpPduAuxSensorTempThrshldUndrAlmDegC = _LgpPduAuxSensorTempThrshldUndrAlmDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 80),
    _LgpPduAuxSensorTempThrshldUndrAlmDegC_Type()
)
lgpPduAuxSensorTempThrshldUndrAlmDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrAlmDegC.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrAlmDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxSensorTempThrshldOvrAlmDegC_Type = Integer32
_LgpPduAuxSensorTempThrshldOvrAlmDegC_Object = MibTableColumn
lgpPduAuxSensorTempThrshldOvrAlmDegC = _LgpPduAuxSensorTempThrshldOvrAlmDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 85),
    _LgpPduAuxSensorTempThrshldOvrAlmDegC_Type()
)
lgpPduAuxSensorTempThrshldOvrAlmDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrAlmDegC.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrAlmDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxSensorTempThrshldUndrWarnDegC_Type = Integer32
_LgpPduAuxSensorTempThrshldUndrWarnDegC_Object = MibTableColumn
lgpPduAuxSensorTempThrshldUndrWarnDegC = _LgpPduAuxSensorTempThrshldUndrWarnDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 90),
    _LgpPduAuxSensorTempThrshldUndrWarnDegC_Type()
)
lgpPduAuxSensorTempThrshldUndrWarnDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrWarnDegC.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrWarnDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxSensorTempThrshldOvrWarnDegC_Type = Integer32
_LgpPduAuxSensorTempThrshldOvrWarnDegC_Object = MibTableColumn
lgpPduAuxSensorTempThrshldOvrWarnDegC = _LgpPduAuxSensorTempThrshldOvrWarnDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 95),
    _LgpPduAuxSensorTempThrshldOvrWarnDegC_Type()
)
lgpPduAuxSensorTempThrshldOvrWarnDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrWarnDegC.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrWarnDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxSensorHumMeasurement_Type = Unsigned32
_LgpPduAuxSensorHumMeasurement_Object = MibTableColumn
lgpPduAuxSensorHumMeasurement = _LgpPduAuxSensorHumMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 100),
    _LgpPduAuxSensorHumMeasurement_Type()
)
lgpPduAuxSensorHumMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumMeasurement.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumMeasurement.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxSensorHumThrshldUndrAlm_Type = Unsigned32
_LgpPduAuxSensorHumThrshldUndrAlm_Object = MibTableColumn
lgpPduAuxSensorHumThrshldUndrAlm = _LgpPduAuxSensorHumThrshldUndrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 105),
    _LgpPduAuxSensorHumThrshldUndrAlm_Type()
)
lgpPduAuxSensorHumThrshldUndrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldUndrAlm.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldUndrAlm.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxSensorHumThrshldOvrAlm_Type = Unsigned32
_LgpPduAuxSensorHumThrshldOvrAlm_Object = MibTableColumn
lgpPduAuxSensorHumThrshldOvrAlm = _LgpPduAuxSensorHumThrshldOvrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 110),
    _LgpPduAuxSensorHumThrshldOvrAlm_Type()
)
lgpPduAuxSensorHumThrshldOvrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldOvrAlm.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldOvrAlm.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxSensorHumThrshldUndrWarn_Type = Unsigned32
_LgpPduAuxSensorHumThrshldUndrWarn_Object = MibTableColumn
lgpPduAuxSensorHumThrshldUndrWarn = _LgpPduAuxSensorHumThrshldUndrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 115),
    _LgpPduAuxSensorHumThrshldUndrWarn_Type()
)
lgpPduAuxSensorHumThrshldUndrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldUndrWarn.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldUndrWarn.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxSensorHumThrshldOvrWarn_Type = Unsigned32
_LgpPduAuxSensorHumThrshldOvrWarn_Object = MibTableColumn
lgpPduAuxSensorHumThrshldOvrWarn = _LgpPduAuxSensorHumThrshldOvrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 120),
    _LgpPduAuxSensorHumThrshldOvrWarn_Type()
)
lgpPduAuxSensorHumThrshldOvrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldOvrWarn.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldOvrWarn.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxMeasTable_Object = MibTable
lgpPduAuxMeasTable = _LgpPduAuxMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15)
)
if mibBuilder.loadTexts:
    lgpPduAuxMeasTable.setStatus("current")
_LgpPduAuxMeasEntry_Object = MibTableRow
lgpPduAuxMeasEntry = _LgpPduAuxMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1)
)
lgpPduAuxMeasEntry.setIndexNames(
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduAuxMeasSensorIndex"),
    (0, "LIEBERT-GP-PDU-MIB", "lgpPduAuxMeasSensorMeasurementIndex"),
)
if mibBuilder.loadTexts:
    lgpPduAuxMeasEntry.setStatus("current")
_LgpPduAuxMeasSensorIndex_Type = Unsigned32
_LgpPduAuxMeasSensorIndex_Object = MibTableColumn
lgpPduAuxMeasSensorIndex = _LgpPduAuxMeasSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 1),
    _LgpPduAuxMeasSensorIndex_Type()
)
lgpPduAuxMeasSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduAuxMeasSensorIndex.setStatus("current")
_LgpPduAuxMeasSensorMeasurementIndex_Type = Unsigned32
_LgpPduAuxMeasSensorMeasurementIndex_Object = MibTableColumn
lgpPduAuxMeasSensorMeasurementIndex = _LgpPduAuxMeasSensorMeasurementIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 5),
    _LgpPduAuxMeasSensorMeasurementIndex_Type()
)
lgpPduAuxMeasSensorMeasurementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduAuxMeasSensorMeasurementIndex.setStatus("current")


class _LgpPduAuxMeasType_Type(Integer32):
    """Custom type lgpPduAuxMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("contact-closure", 4),
          ("door-closure", 3),
          ("humidity", 2),
          ("not-specified", 0),
          ("temperature", 1))
    )


_LgpPduAuxMeasType_Type.__name__ = "Integer32"
_LgpPduAuxMeasType_Object = MibTableColumn
lgpPduAuxMeasType = _LgpPduAuxMeasType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 10),
    _LgpPduAuxMeasType_Type()
)
lgpPduAuxMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasType.setStatus("current")
_LgpPduAuxMeasSensorSysAssignLabel_Type = DisplayString
_LgpPduAuxMeasSensorSysAssignLabel_Object = MibTableColumn
lgpPduAuxMeasSensorSysAssignLabel = _LgpPduAuxMeasSensorSysAssignLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 15),
    _LgpPduAuxMeasSensorSysAssignLabel_Type()
)
lgpPduAuxMeasSensorSysAssignLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasSensorSysAssignLabel.setStatus("current")
_LgpPduAuxMeasUsrLabel_Type = DisplayString
_LgpPduAuxMeasUsrLabel_Object = MibTableColumn
lgpPduAuxMeasUsrLabel = _LgpPduAuxMeasUsrLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 20),
    _LgpPduAuxMeasUsrLabel_Type()
)
lgpPduAuxMeasUsrLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasUsrLabel.setStatus("current")
_LgpPduAuxMeasUsrTag1_Type = DisplayString
_LgpPduAuxMeasUsrTag1_Object = MibTableColumn
lgpPduAuxMeasUsrTag1 = _LgpPduAuxMeasUsrTag1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 25),
    _LgpPduAuxMeasUsrTag1_Type()
)
lgpPduAuxMeasUsrTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasUsrTag1.setStatus("current")
_LgpPduAuxMeasUsrTag2_Type = DisplayString
_LgpPduAuxMeasUsrTag2_Object = MibTableColumn
lgpPduAuxMeasUsrTag2 = _LgpPduAuxMeasUsrTag2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 30),
    _LgpPduAuxMeasUsrTag2_Type()
)
lgpPduAuxMeasUsrTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasUsrTag2.setStatus("current")
_LgpPduAuxMeasSensorSerialNum_Type = DisplayString
_LgpPduAuxMeasSensorSerialNum_Object = MibTableColumn
lgpPduAuxMeasSensorSerialNum = _LgpPduAuxMeasSensorSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 35),
    _LgpPduAuxMeasSensorSerialNum_Type()
)
lgpPduAuxMeasSensorSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasSensorSerialNum.setStatus("current")
_LgpPduAuxMeasTempDegF_Type = Integer32
_LgpPduAuxMeasTempDegF_Object = MibTableColumn
lgpPduAuxMeasTempDegF = _LgpPduAuxMeasTempDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 40),
    _LgpPduAuxMeasTempDegF_Type()
)
lgpPduAuxMeasTempDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxMeasTempThrshldUndrAlmDegF_Type = Integer32
_LgpPduAuxMeasTempThrshldUndrAlmDegF_Object = MibTableColumn
lgpPduAuxMeasTempThrshldUndrAlmDegF = _LgpPduAuxMeasTempThrshldUndrAlmDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 50),
    _LgpPduAuxMeasTempThrshldUndrAlmDegF_Type()
)
lgpPduAuxMeasTempThrshldUndrAlmDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrAlmDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrAlmDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxMeasTempThrshldOvrAlmDegF_Type = Integer32
_LgpPduAuxMeasTempThrshldOvrAlmDegF_Object = MibTableColumn
lgpPduAuxMeasTempThrshldOvrAlmDegF = _LgpPduAuxMeasTempThrshldOvrAlmDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 55),
    _LgpPduAuxMeasTempThrshldOvrAlmDegF_Type()
)
lgpPduAuxMeasTempThrshldOvrAlmDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrAlmDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrAlmDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxMeasTempThrshldUndrWarnDegF_Type = Integer32
_LgpPduAuxMeasTempThrshldUndrWarnDegF_Object = MibTableColumn
lgpPduAuxMeasTempThrshldUndrWarnDegF = _LgpPduAuxMeasTempThrshldUndrWarnDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 60),
    _LgpPduAuxMeasTempThrshldUndrWarnDegF_Type()
)
lgpPduAuxMeasTempThrshldUndrWarnDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrWarnDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrWarnDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxMeasTempThrshldOvrWarnDegF_Type = Integer32
_LgpPduAuxMeasTempThrshldOvrWarnDegF_Object = MibTableColumn
lgpPduAuxMeasTempThrshldOvrWarnDegF = _LgpPduAuxMeasTempThrshldOvrWarnDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 65),
    _LgpPduAuxMeasTempThrshldOvrWarnDegF_Type()
)
lgpPduAuxMeasTempThrshldOvrWarnDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrWarnDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrWarnDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxMeasTempDegC_Type = Integer32
_LgpPduAuxMeasTempDegC_Object = MibTableColumn
lgpPduAuxMeasTempDegC = _LgpPduAuxMeasTempDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 70),
    _LgpPduAuxMeasTempDegC_Type()
)
lgpPduAuxMeasTempDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxMeasTempThrshldUndrAlmDegC_Type = Integer32
_LgpPduAuxMeasTempThrshldUndrAlmDegC_Object = MibTableColumn
lgpPduAuxMeasTempThrshldUndrAlmDegC = _LgpPduAuxMeasTempThrshldUndrAlmDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 75),
    _LgpPduAuxMeasTempThrshldUndrAlmDegC_Type()
)
lgpPduAuxMeasTempThrshldUndrAlmDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrAlmDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrAlmDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxMeasTempThrshldOvrAlmDegC_Type = Integer32
_LgpPduAuxMeasTempThrshldOvrAlmDegC_Object = MibTableColumn
lgpPduAuxMeasTempThrshldOvrAlmDegC = _LgpPduAuxMeasTempThrshldOvrAlmDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 80),
    _LgpPduAuxMeasTempThrshldOvrAlmDegC_Type()
)
lgpPduAuxMeasTempThrshldOvrAlmDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrAlmDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrAlmDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxMeasTempThrshldUndrWarnDegC_Type = Integer32
_LgpPduAuxMeasTempThrshldUndrWarnDegC_Object = MibTableColumn
lgpPduAuxMeasTempThrshldUndrWarnDegC = _LgpPduAuxMeasTempThrshldUndrWarnDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 85),
    _LgpPduAuxMeasTempThrshldUndrWarnDegC_Type()
)
lgpPduAuxMeasTempThrshldUndrWarnDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrWarnDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrWarnDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxMeasTempThrshldOvrWarnDegC_Type = Integer32
_LgpPduAuxMeasTempThrshldOvrWarnDegC_Object = MibTableColumn
lgpPduAuxMeasTempThrshldOvrWarnDegC = _LgpPduAuxMeasTempThrshldOvrWarnDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 90),
    _LgpPduAuxMeasTempThrshldOvrWarnDegC_Type()
)
lgpPduAuxMeasTempThrshldOvrWarnDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrWarnDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrWarnDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxMeasHum_Type = Unsigned32
_LgpPduAuxMeasHum_Object = MibTableColumn
lgpPduAuxMeasHum = _LgpPduAuxMeasHum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 95),
    _LgpPduAuxMeasHum_Type()
)
lgpPduAuxMeasHum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHum.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHum.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxMeasHumThrshldUndrAlm_Type = Unsigned32
_LgpPduAuxMeasHumThrshldUndrAlm_Object = MibTableColumn
lgpPduAuxMeasHumThrshldUndrAlm = _LgpPduAuxMeasHumThrshldUndrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 100),
    _LgpPduAuxMeasHumThrshldUndrAlm_Type()
)
lgpPduAuxMeasHumThrshldUndrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldUndrAlm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldUndrAlm.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxMeasHumThrshldOvrAlm_Type = Unsigned32
_LgpPduAuxMeasHumThrshldOvrAlm_Object = MibTableColumn
lgpPduAuxMeasHumThrshldOvrAlm = _LgpPduAuxMeasHumThrshldOvrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 105),
    _LgpPduAuxMeasHumThrshldOvrAlm_Type()
)
lgpPduAuxMeasHumThrshldOvrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldOvrAlm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldOvrAlm.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxMeasHumThrshldUndrWarn_Type = Unsigned32
_LgpPduAuxMeasHumThrshldUndrWarn_Object = MibTableColumn
lgpPduAuxMeasHumThrshldUndrWarn = _LgpPduAuxMeasHumThrshldUndrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 110),
    _LgpPduAuxMeasHumThrshldUndrWarn_Type()
)
lgpPduAuxMeasHumThrshldUndrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldUndrWarn.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldUndrWarn.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxMeasHumThrshldOvrWarn_Type = Unsigned32
_LgpPduAuxMeasHumThrshldOvrWarn_Object = MibTableColumn
lgpPduAuxMeasHumThrshldOvrWarn = _LgpPduAuxMeasHumThrshldOvrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 115),
    _LgpPduAuxMeasHumThrshldOvrWarn_Type()
)
lgpPduAuxMeasHumThrshldOvrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldOvrWarn.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldOvrWarn.setUnits("0.1 percent Relative Humidity")


class _LgpPduAuxMeasDrClosureState_Type(Integer32):
    """Custom type lgpPduAuxMeasDrClosureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("not-specified", 0),
          ("open", 1))
    )


_LgpPduAuxMeasDrClosureState_Type.__name__ = "Integer32"
_LgpPduAuxMeasDrClosureState_Object = MibTableColumn
lgpPduAuxMeasDrClosureState = _LgpPduAuxMeasDrClosureState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 120),
    _LgpPduAuxMeasDrClosureState_Type()
)
lgpPduAuxMeasDrClosureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasDrClosureState.setStatus("current")


class _LgpPduAuxMeasDrClosureConfig_Type(Integer32):
    """Custom type lgpPduAuxMeasDrClosureConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm-when-open", 1),
          ("disabled", 0))
    )


_LgpPduAuxMeasDrClosureConfig_Type.__name__ = "Integer32"
_LgpPduAuxMeasDrClosureConfig_Object = MibTableColumn
lgpPduAuxMeasDrClosureConfig = _LgpPduAuxMeasDrClosureConfig_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 125),
    _LgpPduAuxMeasDrClosureConfig_Type()
)
lgpPduAuxMeasDrClosureConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasDrClosureConfig.setStatus("current")


class _LgpPduAuxMeasCntctClosureState_Type(Integer32):
    """Custom type lgpPduAuxMeasCntctClosureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("not-specified", 0),
          ("open", 1))
    )


_LgpPduAuxMeasCntctClosureState_Type.__name__ = "Integer32"
_LgpPduAuxMeasCntctClosureState_Object = MibTableColumn
lgpPduAuxMeasCntctClosureState = _LgpPduAuxMeasCntctClosureState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 130),
    _LgpPduAuxMeasCntctClosureState_Type()
)
lgpPduAuxMeasCntctClosureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasCntctClosureState.setStatus("current")


class _LgpPduAuxMeasCntctClosureConfig_Type(Integer32):
    """Custom type lgpPduAuxMeasCntctClosureConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm-when-closed", 2),
          ("alarm-when-open", 1),
          ("disabled", 0))
    )


_LgpPduAuxMeasCntctClosureConfig_Type.__name__ = "Integer32"
_LgpPduAuxMeasCntctClosureConfig_Object = MibTableColumn
lgpPduAuxMeasCntctClosureConfig = _LgpPduAuxMeasCntctClosureConfig_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 135),
    _LgpPduAuxMeasCntctClosureConfig_Type()
)
lgpPduAuxMeasCntctClosureConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasCntctClosureConfig.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-PDU-MIB",
    **{"liebertGlobalProductsPduModule": liebertGlobalProductsPduModule,
       "lgpPduCluster": lgpPduCluster,
       "lgpPduGrpSysStatus": lgpPduGrpSysStatus,
       "lgpPduTableCount": lgpPduTableCount,
       "lgpPduTable": lgpPduTable,
       "lgpPduEntry": lgpPduEntry,
       "lgpPduEntryIndex": lgpPduEntryIndex,
       "lgpPduEntryId": lgpPduEntryId,
       "lgpPduEntryUsrLabel": lgpPduEntryUsrLabel,
       "lgpPduEntrySysAssignLabel": lgpPduEntrySysAssignLabel,
       "lgpPduEntryPositionRelative": lgpPduEntryPositionRelative,
       "lgpPduEntrySysStatus": lgpPduEntrySysStatus,
       "lgpPduEntryUsrTag1": lgpPduEntryUsrTag1,
       "lgpPduEntryUsrTag2": lgpPduEntryUsrTag2,
       "lgpPduEntrySerialNumber": lgpPduEntrySerialNumber,
       "lgpPduEntryRbCount": lgpPduEntryRbCount,
       "lgpPduPowerSource": lgpPduPowerSource,
       "lgpPduPsTableCount": lgpPduPsTableCount,
       "lgpPduPsTable": lgpPduPsTable,
       "lgpPduPsEntry": lgpPduPsEntry,
       "lgpPduPsEntryIndex": lgpPduPsEntryIndex,
       "lgpPduPsEntryId": lgpPduPsEntryId,
       "lgpPduPsEntrySysAssignLabel": lgpPduPsEntrySysAssignLabel,
       "lgpPduPsEntryModel": lgpPduPsEntryModel,
       "lgpPduPsEntryWiringType": lgpPduPsEntryWiringType,
       "lgpPduPsEntryEpInputRated": lgpPduPsEntryEpInputRated,
       "lgpPduPsEntryEcInputRated": lgpPduPsEntryEcInputRated,
       "lgpPduPsEntryFreqRated": lgpPduPsEntryFreqRated,
       "lgpPduPsEntryEnergyAccum": lgpPduPsEntryEnergyAccum,
       "lgpPduPsEntrySerialNum": lgpPduPsEntrySerialNum,
       "lgpPduPsEntryFirmwareVersion": lgpPduPsEntryFirmwareVersion,
       "lgpPduPsEntryPwrTotal": lgpPduPsEntryPwrTotal,
       "lgpPduPsEntryEcNeutral": lgpPduPsEntryEcNeutral,
       "lgpPduPsEntryEcNeutralThrshldOvrWarn": lgpPduPsEntryEcNeutralThrshldOvrWarn,
       "lgpPduPsEntryEcNeutralThrshldOvrAlarm": lgpPduPsEntryEcNeutralThrshldOvrAlarm,
       "lgpPduPsLineTable": lgpPduPsLineTable,
       "lgpPduPsLineEntry": lgpPduPsLineEntry,
       "lgpPduPsLineEntryIndex": lgpPduPsLineEntryIndex,
       "lgpPduPsLineEntryId": lgpPduPsLineEntryId,
       "lgpPduPsLineEntryLine": lgpPduPsLineEntryLine,
       "lgpPduPsLineEntryEpLNTenths": lgpPduPsLineEntryEpLNTenths,
       "lgpPduPsLineEntryEpLN": lgpPduPsLineEntryEpLN,
       "lgpPduPsLineEntryEc": lgpPduPsLineEntryEc,
       "lgpPduPsLineEntryEcHundredths": lgpPduPsLineEntryEcHundredths,
       "lgpPduPsLineEntryEcThrshldUndrAlarm": lgpPduPsLineEntryEcThrshldUndrAlarm,
       "lgpPduPsLineEntryEcThrshldOvrWarn": lgpPduPsLineEntryEcThrshldOvrWarn,
       "lgpPduPsLineEntryEcThrshldOvrAlarm": lgpPduPsLineEntryEcThrshldOvrAlarm,
       "lgpPduPsLineEntryEcAvailBeforeAlarm": lgpPduPsLineEntryEcAvailBeforeAlarm,
       "lgpPduPsLineEntryEcUsedBeforeAlarm": lgpPduPsLineEntryEcUsedBeforeAlarm,
       "lgpPduPsLineEntryEpLL": lgpPduPsLineEntryEpLL,
       "lgpPduPsLineEntryEpLLTenths": lgpPduPsLineEntryEpLLTenths,
       "lgpPduPsLineEntryEcAvailBeforeAlarmHundredths": lgpPduPsLineEntryEcAvailBeforeAlarmHundredths,
       "lgpPduReceptacleBranch": lgpPduReceptacleBranch,
       "lgpPduRbTableCount": lgpPduRbTableCount,
       "lgpPduRbTable": lgpPduRbTable,
       "lgpPduRbEntry": lgpPduRbEntry,
       "lgpPduRbEntryIndex": lgpPduRbEntryIndex,
       "lgpPduRbEntryId": lgpPduRbEntryId,
       "lgpPduRbEntryUsrLabel": lgpPduRbEntryUsrLabel,
       "lgpPduRbEntrySysAssignLabel": lgpPduRbEntrySysAssignLabel,
       "lgpPduRbEntryPositionRelative": lgpPduRbEntryPositionRelative,
       "lgpPduRbEntrySerialNum": lgpPduRbEntrySerialNum,
       "lgpPduRbEntryModel": lgpPduRbEntryModel,
       "lgpPduRbEntryFirmwareVersion": lgpPduRbEntryFirmwareVersion,
       "lgpPduRbEntryUsrTag1": lgpPduRbEntryUsrTag1,
       "lgpPduRbEntryUsrTag2": lgpPduRbEntryUsrTag2,
       "lgpPduRbEntryReceptacleType": lgpPduRbEntryReceptacleType,
       "lgpPduRbEntryCapabilities": lgpPduRbEntryCapabilities,
       "lgpPduRbEntryLineSource": lgpPduRbEntryLineSource,
       "lgpPduRbEntryRcpCount": lgpPduRbEntryRcpCount,
       "lgpPduRbEntryEpRated": lgpPduRbEntryEpRated,
       "lgpPduRbEntryEcRated": lgpPduRbEntryEcRated,
       "lgpPduRbEntryFreqRated": lgpPduRbEntryFreqRated,
       "lgpPduRbEntryEnergyAccum": lgpPduRbEntryEnergyAccum,
       "lgpPduRbEntryEpLNTenths": lgpPduRbEntryEpLNTenths,
       "lgpPduRbEntryPwr": lgpPduRbEntryPwr,
       "lgpPduRbEntryAp": lgpPduRbEntryAp,
       "lgpPduRbEntryPf": lgpPduRbEntryPf,
       "lgpPduRbEntryEcHundredths": lgpPduRbEntryEcHundredths,
       "lgpPduRbEntryEcThrshldUndrAlm": lgpPduRbEntryEcThrshldUndrAlm,
       "lgpPduRbEntryEcThrshldOvrWarn": lgpPduRbEntryEcThrshldOvrWarn,
       "lgpPduRbEntryEcThrshldOvrAlm": lgpPduRbEntryEcThrshldOvrAlm,
       "lgpPduRbEntryEcAvailBeforeAlarmHundredths": lgpPduRbEntryEcAvailBeforeAlarmHundredths,
       "lgpPduRbEntryEcUsedBeforeAlarm": lgpPduRbEntryEcUsedBeforeAlarm,
       "lgpPduRbEntryEpLLTenths": lgpPduRbEntryEpLLTenths,
       "lgpPduRbLineTable": lgpPduRbLineTable,
       "lgpPduRbLineEntry": lgpPduRbLineEntry,
       "lgpPduRbLineEntryIndex": lgpPduRbLineEntryIndex,
       "lgpPduRbLineEntryId": lgpPduRbLineEntryId,
       "lgpPduRbLineEntryLine": lgpPduRbLineEntryLine,
       "lgpPduRbLineEntryEpLNTenths": lgpPduRbLineEntryEpLNTenths,
       "lgpPduRbLineEntryEpLN": lgpPduRbLineEntryEpLN,
       "lgpPduRbLineEntryEc": lgpPduRbLineEntryEc,
       "lgpPduRbLineEntryPwr": lgpPduRbLineEntryPwr,
       "lgpPduRbLineEntryAp": lgpPduRbLineEntryAp,
       "lgpPduRbLineEntryPf": lgpPduRbLineEntryPf,
       "lgpPduRbLineEntryEcHundredths": lgpPduRbLineEntryEcHundredths,
       "lgpPduRbLineEntryEcThrshldUndrAlm": lgpPduRbLineEntryEcThrshldUndrAlm,
       "lgpPduRbLineEntryEcThrshldOvrWarn": lgpPduRbLineEntryEcThrshldOvrWarn,
       "lgpPduRbLineEntryEcThrshldOvrAlm": lgpPduRbLineEntryEcThrshldOvrAlm,
       "lgpPduRbLineEntryEcAvailBeforeAlarmHundredths": lgpPduRbLineEntryEcAvailBeforeAlarmHundredths,
       "lgpPduRbLineEntryEcAvailBeforeAlarm": lgpPduRbLineEntryEcAvailBeforeAlarm,
       "lgpPduRbLineEntryEcUsedBeforeAlarm": lgpPduRbLineEntryEcUsedBeforeAlarm,
       "lgpPduRbLineEntryEpLL": lgpPduRbLineEntryEpLL,
       "lgpPduRbLineEntryEpLLTenths": lgpPduRbLineEntryEpLLTenths,
       "lgpPduReceptacle": lgpPduReceptacle,
       "lgpPduRcpTableCount": lgpPduRcpTableCount,
       "lgpPduRcpTable": lgpPduRcpTable,
       "lgpPduRcpEntry": lgpPduRcpEntry,
       "lgpPduRcpEntryIndex": lgpPduRcpEntryIndex,
       "lgpPduRcpEntryId": lgpPduRcpEntryId,
       "lgpPduRcpEntryUsrLabel": lgpPduRcpEntryUsrLabel,
       "lgpPduRcpEntryUsrTag1": lgpPduRcpEntryUsrTag1,
       "lgpPduRcpEntryUsrTag2": lgpPduRcpEntryUsrTag2,
       "lgpPduRcpEntrySysAssignLabel": lgpPduRcpEntrySysAssignLabel,
       "lgpPduRcpEntryPosition": lgpPduRcpEntryPosition,
       "lgpPduRcpEntryType": lgpPduRcpEntryType,
       "lgpPduRcpEntryLineSource": lgpPduRcpEntryLineSource,
       "lgpPduRcpEntryCapabilities": lgpPduRcpEntryCapabilities,
       "lgpPduRcpEntryEp": lgpPduRcpEntryEp,
       "lgpPduRcpEntryEpTenths": lgpPduRcpEntryEpTenths,
       "lgpPduRcpEntryEc": lgpPduRcpEntryEc,
       "lgpPduRcpEntryEcHundredths": lgpPduRcpEntryEcHundredths,
       "lgpPduRcpEntryPwrOut": lgpPduRcpEntryPwrOut,
       "lgpPduRcpEntryApOut": lgpPduRcpEntryApOut,
       "lgpPduRcpEntryPf": lgpPduRcpEntryPf,
       "lgpPduRcpEntryFreq": lgpPduRcpEntryFreq,
       "lgpPduRcpEntryEnergyAccum": lgpPduRcpEntryEnergyAccum,
       "lgpPduRcpEntryPwrOnDelay": lgpPduRcpEntryPwrOnDelay,
       "lgpPduRcpEntryPwrState": lgpPduRcpEntryPwrState,
       "lgpPduRcpEntryControl": lgpPduRcpEntryControl,
       "lgpPduRcpEntryControlLock": lgpPduRcpEntryControlLock,
       "lgpPduRcpEntryEcThrshldUnderAlarm": lgpPduRcpEntryEcThrshldUnderAlarm,
       "lgpPduRcpEntryEcThrshldOverWarn": lgpPduRcpEntryEcThrshldOverWarn,
       "lgpPduRcpEntryEcThrshldOverAlarm": lgpPduRcpEntryEcThrshldOverAlarm,
       "lgpPduRcpEntryEcAvailBeforeAlarmHundredths": lgpPduRcpEntryEcAvailBeforeAlarmHundredths,
       "lgpPduRcpEntryEcAvailBeforeAlarm": lgpPduRcpEntryEcAvailBeforeAlarm,
       "lgpPduRcpEntryEcUsedBeforeAlarm": lgpPduRcpEntryEcUsedBeforeAlarm,
       "lgpPduRcpEntryEcCrestFactor": lgpPduRcpEntryEcCrestFactor,
       "lgpPduRcpEntryBlinkLED": lgpPduRcpEntryBlinkLED,
       "lgpPduAuxiliarySensors": lgpPduAuxiliarySensors,
       "lgpPduAuxSensorCount": lgpPduAuxSensorCount,
       "lgpPduAuxSensorTable": lgpPduAuxSensorTable,
       "lgpPduAuxSensorEntry": lgpPduAuxSensorEntry,
       "lgpPduAuxSensorIndex": lgpPduAuxSensorIndex,
       "lgpPduAuxSensorMeasType": lgpPduAuxSensorMeasType,
       "lgpPduAuxSensorId": lgpPduAuxSensorId,
       "lgpPduAuxSensorSysAssignLabel": lgpPduAuxSensorSysAssignLabel,
       "lgpPduAuxSensorPositionRelative": lgpPduAuxSensorPositionRelative,
       "lgpPduAuxSensorUsrLabel": lgpPduAuxSensorUsrLabel,
       "lgpPduAuxSensorUsrTag1": lgpPduAuxSensorUsrTag1,
       "lgpPduAuxSensorUsrTag2": lgpPduAuxSensorUsrTag2,
       "lgpPduAuxSensorTempSerialNum": lgpPduAuxSensorTempSerialNum,
       "lgpPduAuxSensorHumSerialNum": lgpPduAuxSensorHumSerialNum,
       "lgpPduAuxSensorTempMeasurementDegF": lgpPduAuxSensorTempMeasurementDegF,
       "lgpPduAuxSensorTempThrshldUndrAlmDegF": lgpPduAuxSensorTempThrshldUndrAlmDegF,
       "lgpPduAuxSensorTempThrshldOvrAlmDegF": lgpPduAuxSensorTempThrshldOvrAlmDegF,
       "lgpPduAuxSensorTempThrshldUndrWarnDegF": lgpPduAuxSensorTempThrshldUndrWarnDegF,
       "lgpPduAuxSensorTempThrshldOvrWarnDegF": lgpPduAuxSensorTempThrshldOvrWarnDegF,
       "lgpPduAuxSensorTempMeasurementDegC": lgpPduAuxSensorTempMeasurementDegC,
       "lgpPduAuxSensorTempThrshldUndrAlmDegC": lgpPduAuxSensorTempThrshldUndrAlmDegC,
       "lgpPduAuxSensorTempThrshldOvrAlmDegC": lgpPduAuxSensorTempThrshldOvrAlmDegC,
       "lgpPduAuxSensorTempThrshldUndrWarnDegC": lgpPduAuxSensorTempThrshldUndrWarnDegC,
       "lgpPduAuxSensorTempThrshldOvrWarnDegC": lgpPduAuxSensorTempThrshldOvrWarnDegC,
       "lgpPduAuxSensorHumMeasurement": lgpPduAuxSensorHumMeasurement,
       "lgpPduAuxSensorHumThrshldUndrAlm": lgpPduAuxSensorHumThrshldUndrAlm,
       "lgpPduAuxSensorHumThrshldOvrAlm": lgpPduAuxSensorHumThrshldOvrAlm,
       "lgpPduAuxSensorHumThrshldUndrWarn": lgpPduAuxSensorHumThrshldUndrWarn,
       "lgpPduAuxSensorHumThrshldOvrWarn": lgpPduAuxSensorHumThrshldOvrWarn,
       "lgpPduAuxMeasTable": lgpPduAuxMeasTable,
       "lgpPduAuxMeasEntry": lgpPduAuxMeasEntry,
       "lgpPduAuxMeasSensorIndex": lgpPduAuxMeasSensorIndex,
       "lgpPduAuxMeasSensorMeasurementIndex": lgpPduAuxMeasSensorMeasurementIndex,
       "lgpPduAuxMeasType": lgpPduAuxMeasType,
       "lgpPduAuxMeasSensorSysAssignLabel": lgpPduAuxMeasSensorSysAssignLabel,
       "lgpPduAuxMeasUsrLabel": lgpPduAuxMeasUsrLabel,
       "lgpPduAuxMeasUsrTag1": lgpPduAuxMeasUsrTag1,
       "lgpPduAuxMeasUsrTag2": lgpPduAuxMeasUsrTag2,
       "lgpPduAuxMeasSensorSerialNum": lgpPduAuxMeasSensorSerialNum,
       "lgpPduAuxMeasTempDegF": lgpPduAuxMeasTempDegF,
       "lgpPduAuxMeasTempThrshldUndrAlmDegF": lgpPduAuxMeasTempThrshldUndrAlmDegF,
       "lgpPduAuxMeasTempThrshldOvrAlmDegF": lgpPduAuxMeasTempThrshldOvrAlmDegF,
       "lgpPduAuxMeasTempThrshldUndrWarnDegF": lgpPduAuxMeasTempThrshldUndrWarnDegF,
       "lgpPduAuxMeasTempThrshldOvrWarnDegF": lgpPduAuxMeasTempThrshldOvrWarnDegF,
       "lgpPduAuxMeasTempDegC": lgpPduAuxMeasTempDegC,
       "lgpPduAuxMeasTempThrshldUndrAlmDegC": lgpPduAuxMeasTempThrshldUndrAlmDegC,
       "lgpPduAuxMeasTempThrshldOvrAlmDegC": lgpPduAuxMeasTempThrshldOvrAlmDegC,
       "lgpPduAuxMeasTempThrshldUndrWarnDegC": lgpPduAuxMeasTempThrshldUndrWarnDegC,
       "lgpPduAuxMeasTempThrshldOvrWarnDegC": lgpPduAuxMeasTempThrshldOvrWarnDegC,
       "lgpPduAuxMeasHum": lgpPduAuxMeasHum,
       "lgpPduAuxMeasHumThrshldUndrAlm": lgpPduAuxMeasHumThrshldUndrAlm,
       "lgpPduAuxMeasHumThrshldOvrAlm": lgpPduAuxMeasHumThrshldOvrAlm,
       "lgpPduAuxMeasHumThrshldUndrWarn": lgpPduAuxMeasHumThrshldUndrWarn,
       "lgpPduAuxMeasHumThrshldOvrWarn": lgpPduAuxMeasHumThrshldOvrWarn,
       "lgpPduAuxMeasDrClosureState": lgpPduAuxMeasDrClosureState,
       "lgpPduAuxMeasDrClosureConfig": lgpPduAuxMeasDrClosureConfig,
       "lgpPduAuxMeasCntctClosureState": lgpPduAuxMeasCntctClosureState,
       "lgpPduAuxMeasCntctClosureConfig": lgpPduAuxMeasCntctClosureConfig}
)
