# SNMP MIB module (CISCO-ATM-RM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-RM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:49 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

ciscoAtmRmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10)
)
ciscoAtmRmMIB.setRevisions(
        ("2002-06-03 00:00",
         "2001-01-29 00:00",
         "1999-12-22 00:00",
         "1999-07-27 00:00",
         "1999-04-30 00:00",
         "1999-04-14 00:00",
         "1999-03-11 00:00",
         "1998-11-24 00:00",
         "1998-11-03 00:00",
         "1998-07-26 00:00",
         "1997-12-03 00:00",
         "1997-05-26 00:00",
         "1996-11-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ForceValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceChange", 1),
          ("noForceChange", 2))
    )



class FineQueueThreshold(Integer32, TextualConvention):
    status = "current"
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
        *(("percent100", 8),
          ("percent12", 1),
          ("percent25", 2),
          ("percent37", 3),
          ("percent50", 4),
          ("percent62", 5),
          ("percent75", 6),
          ("percent87", 7))
    )



class LsPerVcqServiceClass(Integer32, TextualConvention):
    status = "current"
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
        *(("c1", 1),
          ("c2", 2),
          ("c3", 3),
          ("c4", 4),
          ("c5", 5),
          ("c6", 6),
          ("c7", 7),
          ("c8", 8))
    )



class LsPerVcqServiceClassNoC1(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("c2", 2),
          ("c3", 3),
          ("c4", 4),
          ("c5", 5),
          ("c6", 6),
          ("c7", 7),
          ("c8", 8))
    )



class LsPerVcqThresholdGroup(Integer32, TextualConvention):
    status = "current"
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("tg1", 1),
          ("tg10", 10),
          ("tg11", 11),
          ("tg12", 12),
          ("tg13", 13),
          ("tg14", 14),
          ("tg15", 15),
          ("tg16", 16),
          ("tg2", 2),
          ("tg3", 3),
          ("tg4", 4),
          ("tg5", 5),
          ("tg6", 6),
          ("tg7", 7),
          ("tg8", 8),
          ("tg9", 9))
    )



class LsPerVcqThresholdGroupService(Integer32, TextualConvention):
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
        *(("abr", 4),
          ("cbr", 1),
          ("ubr", 5),
          ("vbrNrt", 3),
          ("vbrRt", 2))
    )



class CgrPerVcqModuleId(Integer32, TextualConvention):
    status = "current"
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
        *(("module1", 1),
          ("module2", 2),
          ("module3", 3),
          ("module4", 4),
          ("module5", 5),
          ("module6", 6),
          ("module7", 7),
          ("module8", 8))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmRmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmRmMIBObjects = _CiscoAtmRmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1)
)
_CiscoAtmRmSwitchCfg_ObjectIdentity = ObjectIdentity
ciscoAtmRmSwitchCfg = _CiscoAtmRmSwitchCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1)
)


class _RmSwitchOverSubFactor_Type(Integer32):
    """Custom type rmSwitchOverSubFactor based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RmSwitchOverSubFactor_Type.__name__ = "Integer32"
_RmSwitchOverSubFactor_Object = MibScalar
rmSwitchOverSubFactor = _RmSwitchOverSubFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 1),
    _RmSwitchOverSubFactor_Type()
)
rmSwitchOverSubFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmSwitchOverSubFactor.setStatus("current")


class _RmSwitchScrMarginFactor_Type(Integer32):
    """Custom type rmSwitchScrMarginFactor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RmSwitchScrMarginFactor_Type.__name__ = "Integer32"
_RmSwitchScrMarginFactor_Object = MibScalar
rmSwitchScrMarginFactor = _RmSwitchScrMarginFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 2),
    _RmSwitchScrMarginFactor_Type()
)
rmSwitchScrMarginFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmSwitchScrMarginFactor.setStatus("current")


class _RmSwitchAbrCongNotify_Type(Integer32):
    """Custom type rmSwitchAbrCongNotify based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("efci", 2),
          ("efciAndRelativeRate", 3),
          ("relativeRate", 1))
    )


_RmSwitchAbrCongNotify_Type.__name__ = "Integer32"
_RmSwitchAbrCongNotify_Object = MibScalar
rmSwitchAbrCongNotify = _RmSwitchAbrCongNotify_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 3),
    _RmSwitchAbrCongNotify_Type()
)
rmSwitchAbrCongNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmSwitchAbrCongNotify.setStatus("current")
_RmDefaultQosObjectiveTable_Object = MibTable
rmDefaultQosObjectiveTable = _RmDefaultQosObjectiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rmDefaultQosObjectiveTable.setStatus("current")
_RmDefaultQosObjectiveEntry_Object = MibTableRow
rmDefaultQosObjectiveEntry = _RmDefaultQosObjectiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4, 1)
)
rmDefaultQosObjectiveEntry.setIndexNames(
    (0, "CISCO-ATM-RM-MIB", "rmDefaultQosServiceCategory"),
)
if mibBuilder.loadTexts:
    rmDefaultQosObjectiveEntry.setStatus("current")


class _RmDefaultQosServiceCategory_Type(Integer32):
    """Custom type rmDefaultQosServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("vbrNrt", 3),
          ("vbrRt", 2))
    )


_RmDefaultQosServiceCategory_Type.__name__ = "Integer32"
_RmDefaultQosServiceCategory_Object = MibTableColumn
rmDefaultQosServiceCategory = _RmDefaultQosServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4, 1, 1),
    _RmDefaultQosServiceCategory_Type()
)
rmDefaultQosServiceCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rmDefaultQosServiceCategory.setStatus("current")


class _RmScDefaultQosMaxCtd_Type(Integer32):
    """Custom type rmScDefaultQosMaxCtd based on Integer32"""
    defaultValue = 16777215

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RmScDefaultQosMaxCtd_Type.__name__ = "Integer32"
_RmScDefaultQosMaxCtd_Object = MibTableColumn
rmScDefaultQosMaxCtd = _RmScDefaultQosMaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4, 1, 2),
    _RmScDefaultQosMaxCtd_Type()
)
rmScDefaultQosMaxCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmScDefaultQosMaxCtd.setStatus("current")
if mibBuilder.loadTexts:
    rmScDefaultQosMaxCtd.setUnits("microseconds")


class _RmScDefaultQosPeakToPeakCdv_Type(Integer32):
    """Custom type rmScDefaultQosPeakToPeakCdv based on Integer32"""
    defaultValue = 16777215

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RmScDefaultQosPeakToPeakCdv_Type.__name__ = "Integer32"
_RmScDefaultQosPeakToPeakCdv_Object = MibTableColumn
rmScDefaultQosPeakToPeakCdv = _RmScDefaultQosPeakToPeakCdv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4, 1, 3),
    _RmScDefaultQosPeakToPeakCdv_Type()
)
rmScDefaultQosPeakToPeakCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmScDefaultQosPeakToPeakCdv.setStatus("current")
if mibBuilder.loadTexts:
    rmScDefaultQosPeakToPeakCdv.setUnits("microseconds")


class _RmScDefaultQosClr_Type(Integer32):
    """Custom type rmScDefaultQosClr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RmScDefaultQosClr_Type.__name__ = "Integer32"
_RmScDefaultQosClr_Object = MibTableColumn
rmScDefaultQosClr = _RmScDefaultQosClr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4, 1, 4),
    _RmScDefaultQosClr_Type()
)
rmScDefaultQosClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmScDefaultQosClr.setStatus("current")


class _RmScDefaultQosClrClp01_Type(Integer32):
    """Custom type rmScDefaultQosClrClp01 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RmScDefaultQosClrClp01_Type.__name__ = "Integer32"
_RmScDefaultQosClrClp01_Object = MibTableColumn
rmScDefaultQosClrClp01 = _RmScDefaultQosClrClp01_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4, 1, 5),
    _RmScDefaultQosClrClp01_Type()
)
rmScDefaultQosClrClp01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmScDefaultQosClrClp01.setStatus("current")
_CiscoAtmRmSwitchSharedMem_ObjectIdentity = ObjectIdentity
ciscoAtmRmSwitchSharedMem = _CiscoAtmRmSwitchSharedMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 2)
)
_SharedMemRmSwitchQueuedCellTable_Object = MibTable
sharedMemRmSwitchQueuedCellTable = _SharedMemRmSwitchQueuedCellTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sharedMemRmSwitchQueuedCellTable.setStatus("current")
_SharedMemRmSwitchQueuedCellEntry_Object = MibTableRow
sharedMemRmSwitchQueuedCellEntry = _SharedMemRmSwitchQueuedCellEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 2, 1, 1)
)
sharedMemRmSwitchQueuedCellEntry.setIndexNames(
    (0, "CISCO-ATM-RM-MIB", "sharedMemRmCellPriority"),
)
if mibBuilder.loadTexts:
    sharedMemRmSwitchQueuedCellEntry.setStatus("current")


class _SharedMemRmCellPriority_Type(Integer32):
    """Custom type sharedMemRmCellPriority based on Integer32"""
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
        *(("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4))
    )


_SharedMemRmCellPriority_Type.__name__ = "Integer32"
_SharedMemRmCellPriority_Object = MibTableColumn
sharedMemRmCellPriority = _SharedMemRmCellPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 2, 1, 1, 1),
    _SharedMemRmCellPriority_Type()
)
sharedMemRmCellPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sharedMemRmCellPriority.setStatus("current")


class _SharedMemRmSwitchQueuedCellLimit_Type(Integer32):
    """Custom type sharedMemRmSwitchQueuedCellLimit based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SharedMemRmSwitchQueuedCellLimit_Type.__name__ = "Integer32"
_SharedMemRmSwitchQueuedCellLimit_Object = MibTableColumn
sharedMemRmSwitchQueuedCellLimit = _SharedMemRmSwitchQueuedCellLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 2, 1, 1, 2),
    _SharedMemRmSwitchQueuedCellLimit_Type()
)
sharedMemRmSwitchQueuedCellLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sharedMemRmSwitchQueuedCellLimit.setStatus("current")
if mibBuilder.loadTexts:
    sharedMemRmSwitchQueuedCellLimit.setUnits("cells")
_SharedMemRmSwitchQueuedCellCount_Type = Gauge32
_SharedMemRmSwitchQueuedCellCount_Object = MibTableColumn
sharedMemRmSwitchQueuedCellCount = _SharedMemRmSwitchQueuedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 2, 1, 1, 3),
    _SharedMemRmSwitchQueuedCellCount_Type()
)
sharedMemRmSwitchQueuedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedMemRmSwitchQueuedCellCount.setStatus("current")
if mibBuilder.loadTexts:
    sharedMemRmSwitchQueuedCellCount.setUnits("cells")
_CiscoAtmRmIfCfg_ObjectIdentity = ObjectIdentity
ciscoAtmRmIfCfg = _CiscoAtmRmIfCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3)
)
_RmIfCfgTable_Object = MibTable
rmIfCfgTable = _RmIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3)
)
if mibBuilder.loadTexts:
    rmIfCfgTable.setStatus("current")
_RmIfCfgEntry_Object = MibTableRow
rmIfCfgEntry = _RmIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1)
)
rmIfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rmIfCfgEntry.setStatus("current")


class _RmIfOutPacingRateRequested_Type(Unsigned32):
    """Custom type rmIfOutPacingRateRequested based on Unsigned32"""
    defaultValue = 0


_RmIfOutPacingRateRequested_Object = MibTableColumn
rmIfOutPacingRateRequested = _RmIfOutPacingRateRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 1),
    _RmIfOutPacingRateRequested_Type()
)
rmIfOutPacingRateRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfOutPacingRateRequested.setStatus("current")
if mibBuilder.loadTexts:
    rmIfOutPacingRateRequested.setUnits("kilobits-per-second")


class _RmIfOutPacingRateInstalled_Type(Unsigned32):
    """Custom type rmIfOutPacingRateInstalled based on Unsigned32"""
    defaultValue = 0


_RmIfOutPacingRateInstalled_Object = MibTableColumn
rmIfOutPacingRateInstalled = _RmIfOutPacingRateInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 2),
    _RmIfOutPacingRateInstalled_Type()
)
rmIfOutPacingRateInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfOutPacingRateInstalled.setStatus("current")
if mibBuilder.loadTexts:
    rmIfOutPacingRateInstalled.setUnits("kilobits-per-second")


class _RmIfOutPacingForce_Type(ForceValue):
    """Custom type rmIfOutPacingForce based on ForceValue"""


_RmIfOutPacingForce_Object = MibTableColumn
rmIfOutPacingForce = _RmIfOutPacingForce_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 3),
    _RmIfOutPacingForce_Type()
)
rmIfOutPacingForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfOutPacingForce.setStatus("current")


class _RmIfLinkDistance_Type(Unsigned32):
    """Custom type rmIfLinkDistance based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmIfLinkDistance_Type.__name__ = "Unsigned32"
_RmIfLinkDistance_Object = MibTableColumn
rmIfLinkDistance = _RmIfLinkDistance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 4),
    _RmIfLinkDistance_Type()
)
rmIfLinkDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfLinkDistance.setStatus("current")
if mibBuilder.loadTexts:
    rmIfLinkDistance.setUnits("kilometers")


class _RmIfBestEffortLimit_Type(Unsigned32):
    """Custom type rmIfBestEffortLimit based on Unsigned32"""
    defaultValue = 4294967295


_RmIfBestEffortLimit_Object = MibTableColumn
rmIfBestEffortLimit = _RmIfBestEffortLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 5),
    _RmIfBestEffortLimit_Type()
)
rmIfBestEffortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfBestEffortLimit.setStatus("current")


class _RmIfCbrDefaultRxUpcTolerance_Type(Unsigned32):
    """Custom type rmIfCbrDefaultRxUpcTolerance based on Unsigned32"""
    defaultValue = 1024


_RmIfCbrDefaultRxUpcTolerance_Object = MibTableColumn
rmIfCbrDefaultRxUpcTolerance = _RmIfCbrDefaultRxUpcTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 6),
    _RmIfCbrDefaultRxUpcTolerance_Type()
)
rmIfCbrDefaultRxUpcTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfCbrDefaultRxUpcTolerance.setStatus("current")
if mibBuilder.loadTexts:
    rmIfCbrDefaultRxUpcTolerance.setUnits("cell-times")


class _RmIfVbrRtDefaultRxUpcTolerance_Type(Unsigned32):
    """Custom type rmIfVbrRtDefaultRxUpcTolerance based on Unsigned32"""
    defaultValue = 1024


_RmIfVbrRtDefaultRxUpcTolerance_Object = MibTableColumn
rmIfVbrRtDefaultRxUpcTolerance = _RmIfVbrRtDefaultRxUpcTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 7),
    _RmIfVbrRtDefaultRxUpcTolerance_Type()
)
rmIfVbrRtDefaultRxUpcTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfVbrRtDefaultRxUpcTolerance.setStatus("current")
if mibBuilder.loadTexts:
    rmIfVbrRtDefaultRxUpcTolerance.setUnits("cell-times")


class _RmIfVbrNrtDefaultRxUpcTolerance_Type(Unsigned32):
    """Custom type rmIfVbrNrtDefaultRxUpcTolerance based on Unsigned32"""
    defaultValue = 1024


_RmIfVbrNrtDefaultRxUpcTolerance_Object = MibTableColumn
rmIfVbrNrtDefaultRxUpcTolerance = _RmIfVbrNrtDefaultRxUpcTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 8),
    _RmIfVbrNrtDefaultRxUpcTolerance_Type()
)
rmIfVbrNrtDefaultRxUpcTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfVbrNrtDefaultRxUpcTolerance.setStatus("current")
if mibBuilder.loadTexts:
    rmIfVbrNrtDefaultRxUpcTolerance.setUnits("cell-times")


class _RmIfAbrDefaultRxUpcTolerance_Type(Unsigned32):
    """Custom type rmIfAbrDefaultRxUpcTolerance based on Unsigned32"""
    defaultValue = 1024


_RmIfAbrDefaultRxUpcTolerance_Object = MibTableColumn
rmIfAbrDefaultRxUpcTolerance = _RmIfAbrDefaultRxUpcTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 9),
    _RmIfAbrDefaultRxUpcTolerance_Type()
)
rmIfAbrDefaultRxUpcTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfAbrDefaultRxUpcTolerance.setStatus("current")
if mibBuilder.loadTexts:
    rmIfAbrDefaultRxUpcTolerance.setUnits("cell-times")


class _RmIfUbrDefaultRxUpcTolerance_Type(Unsigned32):
    """Custom type rmIfUbrDefaultRxUpcTolerance based on Unsigned32"""
    defaultValue = 1024


_RmIfUbrDefaultRxUpcTolerance_Object = MibTableColumn
rmIfUbrDefaultRxUpcTolerance = _RmIfUbrDefaultRxUpcTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 10),
    _RmIfUbrDefaultRxUpcTolerance_Type()
)
rmIfUbrDefaultRxUpcTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfUbrDefaultRxUpcTolerance.setStatus("current")
if mibBuilder.loadTexts:
    rmIfUbrDefaultRxUpcTolerance.setUnits("cell-times")


class _RmIfVbrRtDefaultRxUpcCdvt_Type(Unsigned32):
    """Custom type rmIfVbrRtDefaultRxUpcCdvt based on Unsigned32"""
    defaultValue = 1024


_RmIfVbrRtDefaultRxUpcCdvt_Object = MibTableColumn
rmIfVbrRtDefaultRxUpcCdvt = _RmIfVbrRtDefaultRxUpcCdvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 11),
    _RmIfVbrRtDefaultRxUpcCdvt_Type()
)
rmIfVbrRtDefaultRxUpcCdvt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfVbrRtDefaultRxUpcCdvt.setStatus("current")
if mibBuilder.loadTexts:
    rmIfVbrRtDefaultRxUpcCdvt.setUnits("cell-times")


class _RmIfVbrNrtDefaultRxUpcCdvt_Type(Unsigned32):
    """Custom type rmIfVbrNrtDefaultRxUpcCdvt based on Unsigned32"""
    defaultValue = 1024


_RmIfVbrNrtDefaultRxUpcCdvt_Object = MibTableColumn
rmIfVbrNrtDefaultRxUpcCdvt = _RmIfVbrNrtDefaultRxUpcCdvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 12),
    _RmIfVbrNrtDefaultRxUpcCdvt_Type()
)
rmIfVbrNrtDefaultRxUpcCdvt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfVbrNrtDefaultRxUpcCdvt.setStatus("current")
if mibBuilder.loadTexts:
    rmIfVbrNrtDefaultRxUpcCdvt.setUnits("cell-times")


class _RmIfServCategorySupport_Type(Integer32):
    """Custom type rmIfServCategorySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_RmIfServCategorySupport_Type.__name__ = "Integer32"
_RmIfServCategorySupport_Object = MibTableColumn
rmIfServCategorySupport = _RmIfServCategorySupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 13),
    _RmIfServCategorySupport_Type()
)
rmIfServCategorySupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfServCategorySupport.setStatus("current")


class _RmIfFramingOverhead_Type(TruthValue):
    """Custom type rmIfFramingOverhead based on TruthValue"""


_RmIfFramingOverhead_Object = MibTableColumn
rmIfFramingOverhead = _RmIfFramingOverhead_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 14),
    _RmIfFramingOverhead_Type()
)
rmIfFramingOverhead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfFramingOverhead.setStatus("current")


class _RmIfFramingOverheadForce_Type(ForceValue):
    """Custom type rmIfFramingOverheadForce based on ForceValue"""


_RmIfFramingOverheadForce_Object = MibTableColumn
rmIfFramingOverheadForce = _RmIfFramingOverheadForce_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 15),
    _RmIfFramingOverheadForce_Type()
)
rmIfFramingOverheadForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfFramingOverheadForce.setStatus("current")


class _RmIfOverBooking_Type(Integer32):
    """Custom type rmIfOverBooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_RmIfOverBooking_Type.__name__ = "Integer32"
_RmIfOverBooking_Object = MibTableColumn
rmIfOverBooking = _RmIfOverBooking_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 16),
    _RmIfOverBooking_Type()
)
rmIfOverBooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfOverBooking.setStatus("current")
if mibBuilder.loadTexts:
    rmIfOverBooking.setUnits("percent")


class _RmIfVbrRtPerClassOverbooking_Type(Integer32):
    """Custom type rmIfVbrRtPerClassOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3200),
    )


_RmIfVbrRtPerClassOverbooking_Type.__name__ = "Integer32"
_RmIfVbrRtPerClassOverbooking_Object = MibTableColumn
rmIfVbrRtPerClassOverbooking = _RmIfVbrRtPerClassOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 17),
    _RmIfVbrRtPerClassOverbooking_Type()
)
rmIfVbrRtPerClassOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfVbrRtPerClassOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    rmIfVbrRtPerClassOverbooking.setUnits("percent")


class _RmIfVbrNrtPerClassOverbooking_Type(Integer32):
    """Custom type rmIfVbrNrtPerClassOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3200),
    )


_RmIfVbrNrtPerClassOverbooking_Type.__name__ = "Integer32"
_RmIfVbrNrtPerClassOverbooking_Object = MibTableColumn
rmIfVbrNrtPerClassOverbooking = _RmIfVbrNrtPerClassOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 18),
    _RmIfVbrNrtPerClassOverbooking_Type()
)
rmIfVbrNrtPerClassOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfVbrNrtPerClassOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    rmIfVbrNrtPerClassOverbooking.setUnits("percent")


class _RmIfAbrPerClassOverbooking_Type(Integer32):
    """Custom type rmIfAbrPerClassOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3200),
    )


_RmIfAbrPerClassOverbooking_Type.__name__ = "Integer32"
_RmIfAbrPerClassOverbooking_Object = MibTableColumn
rmIfAbrPerClassOverbooking = _RmIfAbrPerClassOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 19),
    _RmIfAbrPerClassOverbooking_Type()
)
rmIfAbrPerClassOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfAbrPerClassOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    rmIfAbrPerClassOverbooking.setUnits("percent")


class _RmIfUbrPerClassOverbooking_Type(Integer32):
    """Custom type rmIfUbrPerClassOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3200),
    )


_RmIfUbrPerClassOverbooking_Type.__name__ = "Integer32"
_RmIfUbrPerClassOverbooking_Object = MibTableColumn
rmIfUbrPerClassOverbooking = _RmIfUbrPerClassOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 20),
    _RmIfUbrPerClassOverbooking_Type()
)
rmIfUbrPerClassOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfUbrPerClassOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    rmIfUbrPerClassOverbooking.setUnits("percent")
_RmIfDirectionCfgTable_Object = MibTable
rmIfDirectionCfgTable = _RmIfDirectionCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4)
)
if mibBuilder.loadTexts:
    rmIfDirectionCfgTable.setStatus("current")
_RmIfDirectionCfgEntry_Object = MibTableRow
rmIfDirectionCfgEntry = _RmIfDirectionCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1)
)
rmIfDirectionCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-RM-MIB", "rmIfDirection"),
)
if mibBuilder.loadTexts:
    rmIfDirectionCfgEntry.setStatus("current")


class _RmIfDirection_Type(Integer32):
    """Custom type rmIfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 1),
          ("transmit", 2))
    )


_RmIfDirection_Type.__name__ = "Integer32"
_RmIfDirection_Object = MibTableColumn
rmIfDirection = _RmIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 1),
    _RmIfDirection_Type()
)
rmIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rmIfDirection.setStatus("current")


class _RmIfDirControlLinkShareMaxAgg_Type(Integer32):
    """Custom type rmIfDirControlLinkShareMaxAgg based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 95),
    )


_RmIfDirControlLinkShareMaxAgg_Type.__name__ = "Integer32"
_RmIfDirControlLinkShareMaxAgg_Object = MibTableColumn
rmIfDirControlLinkShareMaxAgg = _RmIfDirControlLinkShareMaxAgg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 2),
    _RmIfDirControlLinkShareMaxAgg_Type()
)
rmIfDirControlLinkShareMaxAgg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirControlLinkShareMaxAgg.setStatus("current")


class _RmIfDirControlLinkShareMinCbr_Type(Integer32):
    """Custom type rmIfDirControlLinkShareMinCbr based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 95),
    )


_RmIfDirControlLinkShareMinCbr_Type.__name__ = "Integer32"
_RmIfDirControlLinkShareMinCbr_Object = MibTableColumn
rmIfDirControlLinkShareMinCbr = _RmIfDirControlLinkShareMinCbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 3),
    _RmIfDirControlLinkShareMinCbr_Type()
)
rmIfDirControlLinkShareMinCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirControlLinkShareMinCbr.setStatus("current")


class _RmIfDirControlLinkShareMaxCbr_Type(Integer32):
    """Custom type rmIfDirControlLinkShareMaxCbr based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 95),
    )


_RmIfDirControlLinkShareMaxCbr_Type.__name__ = "Integer32"
_RmIfDirControlLinkShareMaxCbr_Object = MibTableColumn
rmIfDirControlLinkShareMaxCbr = _RmIfDirControlLinkShareMaxCbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 4),
    _RmIfDirControlLinkShareMaxCbr_Type()
)
rmIfDirControlLinkShareMaxCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirControlLinkShareMaxCbr.setStatus("current")


class _RmIfDirControlLinkShareMinVbr_Type(Integer32):
    """Custom type rmIfDirControlLinkShareMinVbr based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 95),
    )


_RmIfDirControlLinkShareMinVbr_Type.__name__ = "Integer32"
_RmIfDirControlLinkShareMinVbr_Object = MibTableColumn
rmIfDirControlLinkShareMinVbr = _RmIfDirControlLinkShareMinVbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 5),
    _RmIfDirControlLinkShareMinVbr_Type()
)
rmIfDirControlLinkShareMinVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirControlLinkShareMinVbr.setStatus("current")


class _RmIfDirControlLinkShareMaxVbr_Type(Integer32):
    """Custom type rmIfDirControlLinkShareMaxVbr based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 95),
    )


_RmIfDirControlLinkShareMaxVbr_Type.__name__ = "Integer32"
_RmIfDirControlLinkShareMaxVbr_Object = MibTableColumn
rmIfDirControlLinkShareMaxVbr = _RmIfDirControlLinkShareMaxVbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 6),
    _RmIfDirControlLinkShareMaxVbr_Type()
)
rmIfDirControlLinkShareMaxVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirControlLinkShareMaxVbr.setStatus("current")


class _RmIfDirMaxCbrPcr_Type(Unsigned32):
    """Custom type rmIfDirMaxCbrPcr based on Unsigned32"""
    defaultValue = 4294967295


_RmIfDirMaxCbrPcr_Object = MibTableColumn
rmIfDirMaxCbrPcr = _RmIfDirMaxCbrPcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 7),
    _RmIfDirMaxCbrPcr_Type()
)
rmIfDirMaxCbrPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirMaxCbrPcr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfDirMaxCbrPcr.setUnits("cells-per-second")


class _RmIfDirMaxCbrTolerance_Type(Unsigned32):
    """Custom type rmIfDirMaxCbrTolerance based on Unsigned32"""
    defaultValue = 4294967295


_RmIfDirMaxCbrTolerance_Object = MibTableColumn
rmIfDirMaxCbrTolerance = _RmIfDirMaxCbrTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 8),
    _RmIfDirMaxCbrTolerance_Type()
)
rmIfDirMaxCbrTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirMaxCbrTolerance.setStatus("current")
if mibBuilder.loadTexts:
    rmIfDirMaxCbrTolerance.setUnits("cell-times")


class _RmIfDirMaxVbrPcr_Type(Unsigned32):
    """Custom type rmIfDirMaxVbrPcr based on Unsigned32"""
    defaultValue = 4294967295


_RmIfDirMaxVbrPcr_Object = MibTableColumn
rmIfDirMaxVbrPcr = _RmIfDirMaxVbrPcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 9),
    _RmIfDirMaxVbrPcr_Type()
)
rmIfDirMaxVbrPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirMaxVbrPcr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfDirMaxVbrPcr.setUnits("cells-per-second")


class _RmIfDirMaxVbrScr_Type(Unsigned32):
    """Custom type rmIfDirMaxVbrScr based on Unsigned32"""
    defaultValue = 4294967295


_RmIfDirMaxVbrScr_Object = MibTableColumn
rmIfDirMaxVbrScr = _RmIfDirMaxVbrScr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 10),
    _RmIfDirMaxVbrScr_Type()
)
rmIfDirMaxVbrScr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirMaxVbrScr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfDirMaxVbrScr.setUnits("cells-per-second")


class _RmIfDirMaxVbrTolerance_Type(Unsigned32):
    """Custom type rmIfDirMaxVbrTolerance based on Unsigned32"""
    defaultValue = 4294967295


_RmIfDirMaxVbrTolerance_Object = MibTableColumn
rmIfDirMaxVbrTolerance = _RmIfDirMaxVbrTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 11),
    _RmIfDirMaxVbrTolerance_Type()
)
rmIfDirMaxVbrTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirMaxVbrTolerance.setStatus("current")
if mibBuilder.loadTexts:
    rmIfDirMaxVbrTolerance.setUnits("cell-times")


class _RmIfDirMaxAbrPcr_Type(Unsigned32):
    """Custom type rmIfDirMaxAbrPcr based on Unsigned32"""
    defaultValue = 4294967295


_RmIfDirMaxAbrPcr_Object = MibTableColumn
rmIfDirMaxAbrPcr = _RmIfDirMaxAbrPcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 12),
    _RmIfDirMaxAbrPcr_Type()
)
rmIfDirMaxAbrPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirMaxAbrPcr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfDirMaxAbrPcr.setUnits("cells-per-second")


class _RmIfDirMaxAbrTolerance_Type(Unsigned32):
    """Custom type rmIfDirMaxAbrTolerance based on Unsigned32"""
    defaultValue = 4294967295


_RmIfDirMaxAbrTolerance_Object = MibTableColumn
rmIfDirMaxAbrTolerance = _RmIfDirMaxAbrTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 13),
    _RmIfDirMaxAbrTolerance_Type()
)
rmIfDirMaxAbrTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirMaxAbrTolerance.setStatus("current")
if mibBuilder.loadTexts:
    rmIfDirMaxAbrTolerance.setUnits("cell-times")


class _RmIfDirMaxUbrPcr_Type(Unsigned32):
    """Custom type rmIfDirMaxUbrPcr based on Unsigned32"""
    defaultValue = 4294967295


_RmIfDirMaxUbrPcr_Object = MibTableColumn
rmIfDirMaxUbrPcr = _RmIfDirMaxUbrPcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 14),
    _RmIfDirMaxUbrPcr_Type()
)
rmIfDirMaxUbrPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirMaxUbrPcr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfDirMaxUbrPcr.setUnits("cells-per-second")


class _RmIfDirMaxUbrTolerance_Type(Unsigned32):
    """Custom type rmIfDirMaxUbrTolerance based on Unsigned32"""
    defaultValue = 4294967295


_RmIfDirMaxUbrTolerance_Object = MibTableColumn
rmIfDirMaxUbrTolerance = _RmIfDirMaxUbrTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 15),
    _RmIfDirMaxUbrTolerance_Type()
)
rmIfDirMaxUbrTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirMaxUbrTolerance.setStatus("current")
if mibBuilder.loadTexts:
    rmIfDirMaxUbrTolerance.setUnits("cell-times")


class _RmIfDirMaxAbrMcr_Type(Unsigned32):
    """Custom type rmIfDirMaxAbrMcr based on Unsigned32"""
    defaultValue = 4294967295


_RmIfDirMaxAbrMcr_Object = MibTableColumn
rmIfDirMaxAbrMcr = _RmIfDirMaxAbrMcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 16),
    _RmIfDirMaxAbrMcr_Type()
)
rmIfDirMaxAbrMcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirMaxAbrMcr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfDirMaxAbrMcr.setUnits("cells-per-second")


class _RmIfDirMaxUbrMcr_Type(Unsigned32):
    """Custom type rmIfDirMaxUbrMcr based on Unsigned32"""
    defaultValue = 4294967295


_RmIfDirMaxUbrMcr_Object = MibTableColumn
rmIfDirMaxUbrMcr = _RmIfDirMaxUbrMcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 17),
    _RmIfDirMaxUbrMcr_Type()
)
rmIfDirMaxUbrMcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirMaxUbrMcr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfDirMaxUbrMcr.setUnits("cells-per-second")


class _RmIfDirMaxVbrCdvt_Type(Unsigned32):
    """Custom type rmIfDirMaxVbrCdvt based on Unsigned32"""
    defaultValue = 4294967295


_RmIfDirMaxVbrCdvt_Object = MibTableColumn
rmIfDirMaxVbrCdvt = _RmIfDirMaxVbrCdvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 18),
    _RmIfDirMaxVbrCdvt_Type()
)
rmIfDirMaxVbrCdvt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirMaxVbrCdvt.setStatus("current")
if mibBuilder.loadTexts:
    rmIfDirMaxVbrCdvt.setUnits("cell-times")


class _RmIfDirControlLinkShareMinAbr_Type(Integer32):
    """Custom type rmIfDirControlLinkShareMinAbr based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 95),
    )


_RmIfDirControlLinkShareMinAbr_Type.__name__ = "Integer32"
_RmIfDirControlLinkShareMinAbr_Object = MibTableColumn
rmIfDirControlLinkShareMinAbr = _RmIfDirControlLinkShareMinAbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 19),
    _RmIfDirControlLinkShareMinAbr_Type()
)
rmIfDirControlLinkShareMinAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirControlLinkShareMinAbr.setStatus("current")


class _RmIfDirControlLinkShareMaxAbr_Type(Integer32):
    """Custom type rmIfDirControlLinkShareMaxAbr based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 95),
    )


_RmIfDirControlLinkShareMaxAbr_Type.__name__ = "Integer32"
_RmIfDirControlLinkShareMaxAbr_Object = MibTableColumn
rmIfDirControlLinkShareMaxAbr = _RmIfDirControlLinkShareMaxAbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 20),
    _RmIfDirControlLinkShareMaxAbr_Type()
)
rmIfDirControlLinkShareMaxAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirControlLinkShareMaxAbr.setStatus("current")


class _RmIfDirControlLinkShareMinUbr_Type(Integer32):
    """Custom type rmIfDirControlLinkShareMinUbr based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 95),
    )


_RmIfDirControlLinkShareMinUbr_Type.__name__ = "Integer32"
_RmIfDirControlLinkShareMinUbr_Object = MibTableColumn
rmIfDirControlLinkShareMinUbr = _RmIfDirControlLinkShareMinUbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 21),
    _RmIfDirControlLinkShareMinUbr_Type()
)
rmIfDirControlLinkShareMinUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirControlLinkShareMinUbr.setStatus("current")


class _RmIfDirControlLinkShareMaxUbr_Type(Integer32):
    """Custom type rmIfDirControlLinkShareMaxUbr based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 95),
    )


_RmIfDirControlLinkShareMaxUbr_Type.__name__ = "Integer32"
_RmIfDirControlLinkShareMaxUbr_Object = MibTableColumn
rmIfDirControlLinkShareMaxUbr = _RmIfDirControlLinkShareMaxUbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 22),
    _RmIfDirControlLinkShareMaxUbr_Type()
)
rmIfDirControlLinkShareMaxUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmIfDirControlLinkShareMaxUbr.setStatus("current")
_CiscoAtmRmIfState_ObjectIdentity = ObjectIdentity
ciscoAtmRmIfState = _CiscoAtmRmIfState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4)
)
_RmIfServiceCategoryStateTable_Object = MibTable
rmIfServiceCategoryStateTable = _RmIfServiceCategoryStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rmIfServiceCategoryStateTable.setStatus("current")
_RmIfServiceCategoryStateEntry_Object = MibTableRow
rmIfServiceCategoryStateEntry = _RmIfServiceCategoryStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1)
)
rmIfServiceCategoryStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-RM-MIB", "rmIfSc"),
)
if mibBuilder.loadTexts:
    rmIfServiceCategoryStateEntry.setStatus("current")


class _RmIfSc_Type(Integer32):
    """Custom type rmIfSc based on Integer32"""
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
        *(("abr", 4),
          ("cbr", 1),
          ("ubr", 5),
          ("vbrNrt", 3),
          ("vbrRt", 2))
    )


_RmIfSc_Type.__name__ = "Integer32"
_RmIfSc_Object = MibTableColumn
rmIfSc = _RmIfSc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 1),
    _RmIfSc_Type()
)
rmIfSc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rmIfSc.setStatus("current")
_RmIfScRxAcr_Type = Gauge32
_RmIfScRxAcr_Object = MibTableColumn
rmIfScRxAcr = _RmIfScRxAcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 2),
    _RmIfScRxAcr_Type()
)
rmIfScRxAcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRxAcr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfScRxAcr.setUnits("cells-per-second")
_RmIfScTxAcr_Type = Gauge32
_RmIfScTxAcr_Object = MibTableColumn
rmIfScTxAcr = _RmIfScTxAcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 3),
    _RmIfScTxAcr_Type()
)
rmIfScTxAcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScTxAcr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfScTxAcr.setUnits("cells-per-second")
_RmIfScRxAlcr_Type = Gauge32
_RmIfScRxAlcr_Object = MibTableColumn
rmIfScRxAlcr = _RmIfScRxAlcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 4),
    _RmIfScRxAlcr_Type()
)
rmIfScRxAlcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRxAlcr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfScRxAlcr.setUnits("cells-per-second")
_RmIfScTxAlcr_Type = Gauge32
_RmIfScTxAlcr_Object = MibTableColumn
rmIfScTxAlcr = _RmIfScTxAlcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 5),
    _RmIfScTxAlcr_Type()
)
rmIfScTxAlcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScTxAlcr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfScTxAlcr.setUnits("cells-per-second")
_RmIfScNumSvxConns_Type = Gauge32
_RmIfScNumSvxConns_Object = MibTableColumn
rmIfScNumSvxConns = _RmIfScNumSvxConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 6),
    _RmIfScNumSvxConns_Type()
)
rmIfScNumSvxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScNumSvxConns.setStatus("current")
if mibBuilder.loadTexts:
    rmIfScNumSvxConns.setUnits("number of connections")
_RmIfScNumPvxConns_Type = Gauge32
_RmIfScNumPvxConns_Object = MibTableColumn
rmIfScNumPvxConns = _RmIfScNumPvxConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 7),
    _RmIfScNumPvxConns_Type()
)
rmIfScNumPvxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScNumPvxConns.setStatus("current")
if mibBuilder.loadTexts:
    rmIfScNumPvxConns.setUnits("number of connections")
_RmIfScTxMaxCtd_Type = Gauge32
_RmIfScTxMaxCtd_Object = MibTableColumn
rmIfScTxMaxCtd = _RmIfScTxMaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 8),
    _RmIfScTxMaxCtd_Type()
)
rmIfScTxMaxCtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScTxMaxCtd.setStatus("current")
if mibBuilder.loadTexts:
    rmIfScTxMaxCtd.setUnits("microseconds")
_RmIfScTxP2PeakCdv_Type = Gauge32
_RmIfScTxP2PeakCdv_Object = MibTableColumn
rmIfScTxP2PeakCdv = _RmIfScTxP2PeakCdv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 9),
    _RmIfScTxP2PeakCdv_Type()
)
rmIfScTxP2PeakCdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScTxP2PeakCdv.setStatus("current")
if mibBuilder.loadTexts:
    rmIfScTxP2PeakCdv.setUnits("microseconds")
_RmIfScTxClr_Type = Gauge32
_RmIfScTxClr_Object = MibTableColumn
rmIfScTxClr = _RmIfScTxClr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 10),
    _RmIfScTxClr_Type()
)
rmIfScTxClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScTxClr.setStatus("current")
_RmIfScTxClrClp01_Type = Gauge32
_RmIfScTxClrClp01_Object = MibTableColumn
rmIfScTxClrClp01 = _RmIfScTxClrClp01_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 11),
    _RmIfScTxClrClp01_Type()
)
rmIfScTxClrClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScTxClrClp01.setStatus("current")
_RmIfScRxDynBwSvcAcr_Type = Gauge32
_RmIfScRxDynBwSvcAcr_Object = MibTableColumn
rmIfScRxDynBwSvcAcr = _RmIfScRxDynBwSvcAcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 12),
    _RmIfScRxDynBwSvcAcr_Type()
)
rmIfScRxDynBwSvcAcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRxDynBwSvcAcr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfScRxDynBwSvcAcr.setUnits("cells-per-second")
_RmIfScTxDynBwSvcAcr_Type = Gauge32
_RmIfScTxDynBwSvcAcr_Object = MibTableColumn
rmIfScTxDynBwSvcAcr = _RmIfScTxDynBwSvcAcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 13),
    _RmIfScTxDynBwSvcAcr_Type()
)
rmIfScTxDynBwSvcAcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScTxDynBwSvcAcr.setStatus("current")
if mibBuilder.loadTexts:
    rmIfScTxDynBwSvcAcr.setUnits("cells-per-second")
_CiscoAtmRmIfStatistics_ObjectIdentity = ObjectIdentity
ciscoAtmRmIfStatistics = _CiscoAtmRmIfStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5)
)
_RmIfServiceCategoryStatisticsTable_Object = MibTable
rmIfServiceCategoryStatisticsTable = _RmIfServiceCategoryStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rmIfServiceCategoryStatisticsTable.setStatus("current")
_RmIfServiceCategoryStatisticsEntry_Object = MibTableRow
rmIfServiceCategoryStatisticsEntry = _RmIfServiceCategoryStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1)
)
rmIfServiceCategoryStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-RM-MIB", "rmIfSc"),
)
if mibBuilder.loadTexts:
    rmIfServiceCategoryStatisticsEntry.setStatus("current")
_RmIfScRcacResultNumAdmit_Type = Counter32
_RmIfScRcacResultNumAdmit_Object = MibTableColumn
rmIfScRcacResultNumAdmit = _RmIfScRcacResultNumAdmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 1),
    _RmIfScRcacResultNumAdmit_Type()
)
rmIfScRcacResultNumAdmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRcacResultNumAdmit.setStatus("current")
_RmIfScRcacResultNumTotalRequests_Type = Counter32
_RmIfScRcacResultNumTotalRequests_Object = MibTableColumn
rmIfScRcacResultNumTotalRequests = _RmIfScRcacResultNumTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 2),
    _RmIfScRcacResultNumTotalRequests_Type()
)
rmIfScRcacResultNumTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRcacResultNumTotalRequests.setStatus("current")
_RmIfScRcacResultNumFailTraffComb_Type = Counter32
_RmIfScRcacResultNumFailTraffComb_Object = MibTableColumn
rmIfScRcacResultNumFailTraffComb = _RmIfScRcacResultNumFailTraffComb_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 3),
    _RmIfScRcacResultNumFailTraffComb_Type()
)
rmIfScRcacResultNumFailTraffComb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRcacResultNumFailTraffComb.setStatus("current")
_RmIfScRcacResultNumFailBw_Type = Counter32
_RmIfScRcacResultNumFailBw_Object = MibTableColumn
rmIfScRcacResultNumFailBw = _RmIfScRcacResultNumFailBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 4),
    _RmIfScRcacResultNumFailBw_Type()
)
rmIfScRcacResultNumFailBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRcacResultNumFailBw.setStatus("current")
_RmIfScRcacResultNumFailLoss_Type = Counter32
_RmIfScRcacResultNumFailLoss_Object = MibTableColumn
rmIfScRcacResultNumFailLoss = _RmIfScRcacResultNumFailLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 5),
    _RmIfScRcacResultNumFailLoss_Type()
)
rmIfScRcacResultNumFailLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRcacResultNumFailLoss.setStatus("current")
_RmIfScRcacResultNumFailDelay_Type = Counter32
_RmIfScRcacResultNumFailDelay_Object = MibTableColumn
rmIfScRcacResultNumFailDelay = _RmIfScRcacResultNumFailDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 6),
    _RmIfScRcacResultNumFailDelay_Type()
)
rmIfScRcacResultNumFailDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRcacResultNumFailDelay.setStatus("current")
_RmIfScRcacResultNumFailCdv_Type = Counter32
_RmIfScRcacResultNumFailCdv_Object = MibTableColumn
rmIfScRcacResultNumFailCdv = _RmIfScRcacResultNumFailCdv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 7),
    _RmIfScRcacResultNumFailCdv_Type()
)
rmIfScRcacResultNumFailCdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRcacResultNumFailCdv.setStatus("current")
_RmIfScRcacResultNumFailBeLimit_Type = Counter32
_RmIfScRcacResultNumFailBeLimit_Object = MibTableColumn
rmIfScRcacResultNumFailBeLimit = _RmIfScRcacResultNumFailBeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 8),
    _RmIfScRcacResultNumFailBeLimit_Type()
)
rmIfScRcacResultNumFailBeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRcacResultNumFailBeLimit.setStatus("current")
_RmIfScRcacResultNumFailParmLimit_Type = Counter32
_RmIfScRcacResultNumFailParmLimit_Object = MibTableColumn
rmIfScRcacResultNumFailParmLimit = _RmIfScRcacResultNumFailParmLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 9),
    _RmIfScRcacResultNumFailParmLimit_Type()
)
rmIfScRcacResultNumFailParmLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRcacResultNumFailParmLimit.setStatus("current")
_RmIfScRcacResultNumFailOther_Type = Counter32
_RmIfScRcacResultNumFailOther_Object = MibTableColumn
rmIfScRcacResultNumFailOther = _RmIfScRcacResultNumFailOther_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 10),
    _RmIfScRcacResultNumFailOther_Type()
)
rmIfScRcacResultNumFailOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIfScRcacResultNumFailOther.setStatus("current")
_CiscoAtmRmIfSharedMem_ObjectIdentity = ObjectIdentity
ciscoAtmRmIfSharedMem = _CiscoAtmRmIfSharedMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6)
)
_SharedMemRmIfOutputQCfgTable_Object = MibTable
sharedMemRmIfOutputQCfgTable = _SharedMemRmIfOutputQCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sharedMemRmIfOutputQCfgTable.setStatus("current")
_SharedMemRmIfOutputQCfgEntry_Object = MibTableRow
sharedMemRmIfOutputQCfgEntry = _SharedMemRmIfOutputQCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1)
)
sharedMemRmIfOutputQCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-RM-MIB", "sharedMemRmIfOutputQ"),
)
if mibBuilder.loadTexts:
    sharedMemRmIfOutputQCfgEntry.setStatus("current")


class _SharedMemRmIfOutputQ_Type(Integer32):
    """Custom type sharedMemRmIfOutputQ based on Integer32"""
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
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4))
    )


_SharedMemRmIfOutputQ_Type.__name__ = "Integer32"
_SharedMemRmIfOutputQ_Object = MibTableColumn
sharedMemRmIfOutputQ = _SharedMemRmIfOutputQ_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1, 1),
    _SharedMemRmIfOutputQ_Type()
)
sharedMemRmIfOutputQ.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sharedMemRmIfOutputQ.setStatus("current")


class _SharedMemRmIfOutputQServCategory_Type(Integer32):
    """Custom type sharedMemRmIfOutputQServCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SharedMemRmIfOutputQServCategory_Type.__name__ = "Integer32"
_SharedMemRmIfOutputQServCategory_Object = MibTableColumn
sharedMemRmIfOutputQServCategory = _SharedMemRmIfOutputQServCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1, 2),
    _SharedMemRmIfOutputQServCategory_Type()
)
sharedMemRmIfOutputQServCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedMemRmIfOutputQServCategory.setStatus("current")


class _SharedMemRmIfOutputQRequestedMaxSize_Type(Integer32):
    """Custom type sharedMemRmIfOutputQRequestedMaxSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65504),
    )


_SharedMemRmIfOutputQRequestedMaxSize_Type.__name__ = "Integer32"
_SharedMemRmIfOutputQRequestedMaxSize_Object = MibTableColumn
sharedMemRmIfOutputQRequestedMaxSize = _SharedMemRmIfOutputQRequestedMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1, 3),
    _SharedMemRmIfOutputQRequestedMaxSize_Type()
)
sharedMemRmIfOutputQRequestedMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sharedMemRmIfOutputQRequestedMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    sharedMemRmIfOutputQRequestedMaxSize.setUnits("cells")


class _SharedMemRmIfOutputQInstalledMaxSize_Type(Integer32):
    """Custom type sharedMemRmIfOutputQInstalledMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65504),
    )


_SharedMemRmIfOutputQInstalledMaxSize_Type.__name__ = "Integer32"
_SharedMemRmIfOutputQInstalledMaxSize_Object = MibTableColumn
sharedMemRmIfOutputQInstalledMaxSize = _SharedMemRmIfOutputQInstalledMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1, 4),
    _SharedMemRmIfOutputQInstalledMaxSize_Type()
)
sharedMemRmIfOutputQInstalledMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedMemRmIfOutputQInstalledMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    sharedMemRmIfOutputQInstalledMaxSize.setUnits("cells")


class _SharedMemRmIfOutputQMaxSizeForce_Type(ForceValue):
    """Custom type sharedMemRmIfOutputQMaxSizeForce based on ForceValue"""


_SharedMemRmIfOutputQMaxSizeForce_Object = MibTableColumn
sharedMemRmIfOutputQMaxSizeForce = _SharedMemRmIfOutputQMaxSizeForce_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1, 5),
    _SharedMemRmIfOutputQMaxSizeForce_Type()
)
sharedMemRmIfOutputQMaxSizeForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sharedMemRmIfOutputQMaxSizeForce.setStatus("current")
_SharedMemRmIfOutputQCellCount_Type = Gauge32
_SharedMemRmIfOutputQCellCount_Object = MibTableColumn
sharedMemRmIfOutputQCellCount = _SharedMemRmIfOutputQCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1, 6),
    _SharedMemRmIfOutputQCellCount_Type()
)
sharedMemRmIfOutputQCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedMemRmIfOutputQCellCount.setStatus("current")
if mibBuilder.loadTexts:
    sharedMemRmIfOutputQCellCount.setUnits("cells")
_SharedMemRmIfThresholdCfgTable_Object = MibTable
sharedMemRmIfThresholdCfgTable = _SharedMemRmIfThresholdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 2)
)
if mibBuilder.loadTexts:
    sharedMemRmIfThresholdCfgTable.setStatus("current")
_SharedMemRmIfThresholdCfgEntry_Object = MibTableRow
sharedMemRmIfThresholdCfgEntry = _SharedMemRmIfThresholdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 2, 1)
)
sharedMemRmIfThresholdCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-RM-MIB", "rmIfSc"),
)
if mibBuilder.loadTexts:
    sharedMemRmIfThresholdCfgEntry.setStatus("current")


class _SharedMemRmIfDiscardThreshold_Type(FineQueueThreshold):
    """Custom type sharedMemRmIfDiscardThreshold based on FineQueueThreshold"""


_SharedMemRmIfDiscardThreshold_Object = MibTableColumn
sharedMemRmIfDiscardThreshold = _SharedMemRmIfDiscardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 2, 1, 1),
    _SharedMemRmIfDiscardThreshold_Type()
)
sharedMemRmIfDiscardThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sharedMemRmIfDiscardThreshold.setStatus("current")


class _SharedMemRmIfEfciThreshold_Type(Integer32):
    """Custom type sharedMemRmIfEfciThreshold based on Integer32"""
    defaultValue = 2

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
        *(("percent100", 4),
          ("percent12", 1),
          ("percent25", 2),
          ("percent50", 3))
    )


_SharedMemRmIfEfciThreshold_Type.__name__ = "Integer32"
_SharedMemRmIfEfciThreshold_Object = MibTableColumn
sharedMemRmIfEfciThreshold = _SharedMemRmIfEfciThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 2, 1, 2),
    _SharedMemRmIfEfciThreshold_Type()
)
sharedMemRmIfEfciThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sharedMemRmIfEfciThreshold.setStatus("current")


class _SharedMemRmIfAbrRelativeRateThreshold_Type(FineQueueThreshold):
    """Custom type sharedMemRmIfAbrRelativeRateThreshold based on FineQueueThreshold"""


_SharedMemRmIfAbrRelativeRateThreshold_Object = MibTableColumn
sharedMemRmIfAbrRelativeRateThreshold = _SharedMemRmIfAbrRelativeRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 2, 1, 3),
    _SharedMemRmIfAbrRelativeRateThreshold_Type()
)
sharedMemRmIfAbrRelativeRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sharedMemRmIfAbrRelativeRateThreshold.setStatus("current")
_CiscoLsPerVcqAtmRmSwitch_ObjectIdentity = ObjectIdentity
ciscoLsPerVcqAtmRmSwitch = _CiscoLsPerVcqAtmRmSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7)
)
_LsPerVcqRmThreshGrpTable_Object = MibTable
lsPerVcqRmThreshGrpTable = _LsPerVcqRmThreshGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1)
)
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpTable.setStatus("current")
_LsPerVcqRmThreshGrpEntry_Object = MibTableRow
lsPerVcqRmThreshGrpEntry = _LsPerVcqRmThreshGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1)
)
lsPerVcqRmThreshGrpEntry.setIndexNames(
    (0, "CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrp"),
)
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpEntry.setStatus("current")
_LsPerVcqRmThreshGrp_Type = LsPerVcqThresholdGroup
_LsPerVcqRmThreshGrp_Object = MibTableColumn
lsPerVcqRmThreshGrp = _LsPerVcqRmThreshGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 1),
    _LsPerVcqRmThreshGrp_Type()
)
lsPerVcqRmThreshGrp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrp.setStatus("current")


class _LsPerVcqRmThreshGrpMaxSize_Type(Integer32):
    """Custom type lsPerVcqRmThreshGrpMaxSize based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_LsPerVcqRmThreshGrpMaxSize_Type.__name__ = "Integer32"
_LsPerVcqRmThreshGrpMaxSize_Object = MibTableColumn
lsPerVcqRmThreshGrpMaxSize = _LsPerVcqRmThreshGrpMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 2),
    _LsPerVcqRmThreshGrpMaxSize_Type()
)
lsPerVcqRmThreshGrpMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpMaxSize.setUnits("cells")


class _LsPerVcqRmThreshGrpQMaxSize_Type(Integer32):
    """Custom type lsPerVcqRmThreshGrpQMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(31, 16383),
    )


_LsPerVcqRmThreshGrpQMaxSize_Type.__name__ = "Integer32"
_LsPerVcqRmThreshGrpQMaxSize_Object = MibTableColumn
lsPerVcqRmThreshGrpQMaxSize = _LsPerVcqRmThreshGrpQMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 3),
    _LsPerVcqRmThreshGrpQMaxSize_Type()
)
lsPerVcqRmThreshGrpQMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpQMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpQMaxSize.setUnits("cells")


class _LsPerVcqRmThreshGrpQMinSize_Type(Integer32):
    """Custom type lsPerVcqRmThreshGrpQMinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_LsPerVcqRmThreshGrpQMinSize_Type.__name__ = "Integer32"
_LsPerVcqRmThreshGrpQMinSize_Object = MibTableColumn
lsPerVcqRmThreshGrpQMinSize = _LsPerVcqRmThreshGrpQMinSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 4),
    _LsPerVcqRmThreshGrpQMinSize_Type()
)
lsPerVcqRmThreshGrpQMinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpQMinSize.setStatus("current")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpQMinSize.setUnits("cells")


class _LsPerVcqRmThreshGrpDiscThreshold_Type(Integer32):
    """Custom type lsPerVcqRmThreshGrpDiscThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_LsPerVcqRmThreshGrpDiscThreshold_Type.__name__ = "Integer32"
_LsPerVcqRmThreshGrpDiscThreshold_Object = MibTableColumn
lsPerVcqRmThreshGrpDiscThreshold = _LsPerVcqRmThreshGrpDiscThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 5),
    _LsPerVcqRmThreshGrpDiscThreshold_Type()
)
lsPerVcqRmThreshGrpDiscThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpDiscThreshold.setStatus("current")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpDiscThreshold.setUnits("percentage")


class _LsPerVcqRmThreshGrpMarkThreshold_Type(Integer32):
    """Custom type lsPerVcqRmThreshGrpMarkThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_LsPerVcqRmThreshGrpMarkThreshold_Type.__name__ = "Integer32"
_LsPerVcqRmThreshGrpMarkThreshold_Object = MibTableColumn
lsPerVcqRmThreshGrpMarkThreshold = _LsPerVcqRmThreshGrpMarkThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 6),
    _LsPerVcqRmThreshGrpMarkThreshold_Type()
)
lsPerVcqRmThreshGrpMarkThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpMarkThreshold.setStatus("current")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpMarkThreshold.setUnits("percentage")


class _LsPerVcqRmThreshGrpName_Type(DisplayString):
    """Custom type lsPerVcqRmThreshGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LsPerVcqRmThreshGrpName_Type.__name__ = "DisplayString"
_LsPerVcqRmThreshGrpName_Object = MibTableColumn
lsPerVcqRmThreshGrpName = _LsPerVcqRmThreshGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 7),
    _LsPerVcqRmThreshGrpName_Type()
)
lsPerVcqRmThreshGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpName.setStatus("current")
_LsPerVcqRmThreshGrpCellCount_Type = Gauge32
_LsPerVcqRmThreshGrpCellCount_Object = MibTableColumn
lsPerVcqRmThreshGrpCellCount = _LsPerVcqRmThreshGrpCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 8),
    _LsPerVcqRmThreshGrpCellCount_Type()
)
lsPerVcqRmThreshGrpCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpCellCount.setStatus("current")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpCellCount.setUnits("cells")
_LsPerVcqRmThreshGrpServiceTable_Object = MibTable
lsPerVcqRmThreshGrpServiceTable = _LsPerVcqRmThreshGrpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 2)
)
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpServiceTable.setStatus("current")
_LsPerVcqRmThreshGrpServiceEntry_Object = MibTableRow
lsPerVcqRmThreshGrpServiceEntry = _LsPerVcqRmThreshGrpServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 2, 1)
)
lsPerVcqRmThreshGrpServiceEntry.setIndexNames(
    (0, "CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpService"),
)
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpServiceEntry.setStatus("current")
_LsPerVcqRmThreshGrpService_Type = LsPerVcqThresholdGroupService
_LsPerVcqRmThreshGrpService_Object = MibTableColumn
lsPerVcqRmThreshGrpService = _LsPerVcqRmThreshGrpService_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 2, 1, 1),
    _LsPerVcqRmThreshGrpService_Type()
)
lsPerVcqRmThreshGrpService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpService.setStatus("current")
_LsPerVcqRmThreshGrpServGroup_Type = LsPerVcqThresholdGroup
_LsPerVcqRmThreshGrpServGroup_Object = MibTableColumn
lsPerVcqRmThreshGrpServGroup = _LsPerVcqRmThreshGrpServGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 2, 1, 2),
    _LsPerVcqRmThreshGrpServGroup_Type()
)
lsPerVcqRmThreshGrpServGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPerVcqRmThreshGrpServGroup.setStatus("current")


class _LsPerVcqRmHierarchicalSchedulingMode_Type(Integer32):
    """Custom type lsPerVcqRmHierarchicalSchedulingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_LsPerVcqRmHierarchicalSchedulingMode_Type.__name__ = "Integer32"
_LsPerVcqRmHierarchicalSchedulingMode_Object = MibScalar
lsPerVcqRmHierarchicalSchedulingMode = _LsPerVcqRmHierarchicalSchedulingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 3),
    _LsPerVcqRmHierarchicalSchedulingMode_Type()
)
lsPerVcqRmHierarchicalSchedulingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPerVcqRmHierarchicalSchedulingMode.setStatus("current")
_CiscoLsPerVcqAtmRmIf_ObjectIdentity = ObjectIdentity
ciscoLsPerVcqAtmRmIf = _CiscoLsPerVcqAtmRmIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8)
)
_LsPerVcqRmIfTable_Object = MibTable
lsPerVcqRmIfTable = _LsPerVcqRmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 1)
)
if mibBuilder.loadTexts:
    lsPerVcqRmIfTable.setStatus("current")
_LsPerVcqRmIfEntry_Object = MibTableRow
lsPerVcqRmIfEntry = _LsPerVcqRmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 1, 1)
)
lsPerVcqRmIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lsPerVcqRmIfEntry.setStatus("current")
_LsPerVcqRmIfMinWrrServiceClass_Type = LsPerVcqServiceClass
_LsPerVcqRmIfMinWrrServiceClass_Object = MibTableColumn
lsPerVcqRmIfMinWrrServiceClass = _LsPerVcqRmIfMinWrrServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 1, 1, 1),
    _LsPerVcqRmIfMinWrrServiceClass_Type()
)
lsPerVcqRmIfMinWrrServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPerVcqRmIfMinWrrServiceClass.setStatus("current")
if mibBuilder.loadTexts:
    lsPerVcqRmIfMinWrrServiceClass.setUnits("service class")
_LsPerVcqRmIfServiceClassTable_Object = MibTable
lsPerVcqRmIfServiceClassTable = _LsPerVcqRmIfServiceClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 2)
)
if mibBuilder.loadTexts:
    lsPerVcqRmIfServiceClassTable.setStatus("current")
_LsPerVcqRmIfServiceClassEntry_Object = MibTableRow
lsPerVcqRmIfServiceClassEntry = _LsPerVcqRmIfServiceClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 2, 1)
)
lsPerVcqRmIfServiceClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-RM-MIB", "lsPerVcqRmIfServiceClass"),
)
if mibBuilder.loadTexts:
    lsPerVcqRmIfServiceClassEntry.setStatus("current")
_LsPerVcqRmIfServiceClass_Type = LsPerVcqServiceClass
_LsPerVcqRmIfServiceClass_Object = MibTableColumn
lsPerVcqRmIfServiceClass = _LsPerVcqRmIfServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 2, 1, 1),
    _LsPerVcqRmIfServiceClass_Type()
)
lsPerVcqRmIfServiceClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lsPerVcqRmIfServiceClass.setStatus("current")


class _LsPerVcqRmIfServClassConnType_Type(Integer32):
    """Custom type lsPerVcqRmIfServClassConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_LsPerVcqRmIfServClassConnType_Type.__name__ = "Integer32"
_LsPerVcqRmIfServClassConnType_Object = MibTableColumn
lsPerVcqRmIfServClassConnType = _LsPerVcqRmIfServClassConnType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 2, 1, 2),
    _LsPerVcqRmIfServClassConnType_Type()
)
lsPerVcqRmIfServClassConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsPerVcqRmIfServClassConnType.setStatus("current")


class _LsPerVcqRmIfServClassWrrWeight_Type(Integer32):
    """Custom type lsPerVcqRmIfServClassWrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_LsPerVcqRmIfServClassWrrWeight_Type.__name__ = "Integer32"
_LsPerVcqRmIfServClassWrrWeight_Object = MibTableColumn
lsPerVcqRmIfServClassWrrWeight = _LsPerVcqRmIfServClassWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 2, 1, 3),
    _LsPerVcqRmIfServClassWrrWeight_Type()
)
lsPerVcqRmIfServClassWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsPerVcqRmIfServClassWrrWeight.setStatus("current")
if mibBuilder.loadTexts:
    lsPerVcqRmIfServClassWrrWeight.setUnits("weight")
_CiscoCgrPerVcqAtmRmSwitch_ObjectIdentity = ObjectIdentity
ciscoCgrPerVcqAtmRmSwitch = _CiscoCgrPerVcqAtmRmSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9)
)
_CgrPerVcqRmThreshGrpTable_Object = MibTable
cgrPerVcqRmThreshGrpTable = _CgrPerVcqRmThreshGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpTable.setStatus("current")
_CgrPerVcqRmThreshGrpEntry_Object = MibTableRow
cgrPerVcqRmThreshGrpEntry = _CgrPerVcqRmThreshGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 1, 1)
)
cgrPerVcqRmThreshGrpEntry.setIndexNames(
    (0, "CISCO-ATM-RM-MIB", "cgrPerVcqModuleId"),
    (0, "CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrp"),
)
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpEntry.setStatus("current")
_CgrPerVcqModuleId_Type = CgrPerVcqModuleId
_CgrPerVcqModuleId_Object = MibTableColumn
cgrPerVcqModuleId = _CgrPerVcqModuleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 1, 1, 1),
    _CgrPerVcqModuleId_Type()
)
cgrPerVcqModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgrPerVcqModuleId.setStatus("current")
_CgrPerVcqRmThreshGrp_Type = LsPerVcqThresholdGroup
_CgrPerVcqRmThreshGrp_Object = MibTableColumn
cgrPerVcqRmThreshGrp = _CgrPerVcqRmThreshGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 1, 1, 2),
    _CgrPerVcqRmThreshGrp_Type()
)
cgrPerVcqRmThreshGrp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrp.setStatus("current")


class _CgrPerVcqRmThreshGrpMaxSize_Type(Integer32):
    """Custom type cgrPerVcqRmThreshGrpMaxSize based on Integer32"""
    defaultValue = 131071

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 131071),
    )


_CgrPerVcqRmThreshGrpMaxSize_Type.__name__ = "Integer32"
_CgrPerVcqRmThreshGrpMaxSize_Object = MibTableColumn
cgrPerVcqRmThreshGrpMaxSize = _CgrPerVcqRmThreshGrpMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 1, 1, 3),
    _CgrPerVcqRmThreshGrpMaxSize_Type()
)
cgrPerVcqRmThreshGrpMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpMaxSize.setUnits("cells")


class _CgrPerVcqRmThreshGrpQMaxSize_Type(Integer32):
    """Custom type cgrPerVcqRmThreshGrpQMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(31, 16383),
    )


_CgrPerVcqRmThreshGrpQMaxSize_Type.__name__ = "Integer32"
_CgrPerVcqRmThreshGrpQMaxSize_Object = MibTableColumn
cgrPerVcqRmThreshGrpQMaxSize = _CgrPerVcqRmThreshGrpQMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 1, 1, 4),
    _CgrPerVcqRmThreshGrpQMaxSize_Type()
)
cgrPerVcqRmThreshGrpQMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpQMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpQMaxSize.setUnits("cells")


class _CgrPerVcqRmThreshGrpQMinSize_Type(Integer32):
    """Custom type cgrPerVcqRmThreshGrpQMinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_CgrPerVcqRmThreshGrpQMinSize_Type.__name__ = "Integer32"
_CgrPerVcqRmThreshGrpQMinSize_Object = MibTableColumn
cgrPerVcqRmThreshGrpQMinSize = _CgrPerVcqRmThreshGrpQMinSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 1, 1, 5),
    _CgrPerVcqRmThreshGrpQMinSize_Type()
)
cgrPerVcqRmThreshGrpQMinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpQMinSize.setStatus("current")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpQMinSize.setUnits("cells")


class _CgrPerVcqRmThreshGrpDiscThreshold_Type(Integer32):
    """Custom type cgrPerVcqRmThreshGrpDiscThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_CgrPerVcqRmThreshGrpDiscThreshold_Type.__name__ = "Integer32"
_CgrPerVcqRmThreshGrpDiscThreshold_Object = MibTableColumn
cgrPerVcqRmThreshGrpDiscThreshold = _CgrPerVcqRmThreshGrpDiscThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 1, 1, 6),
    _CgrPerVcqRmThreshGrpDiscThreshold_Type()
)
cgrPerVcqRmThreshGrpDiscThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpDiscThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpDiscThreshold.setUnits("percentage")


class _CgrPerVcqRmThreshGrpMarkThreshold_Type(Integer32):
    """Custom type cgrPerVcqRmThreshGrpMarkThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_CgrPerVcqRmThreshGrpMarkThreshold_Type.__name__ = "Integer32"
_CgrPerVcqRmThreshGrpMarkThreshold_Object = MibTableColumn
cgrPerVcqRmThreshGrpMarkThreshold = _CgrPerVcqRmThreshGrpMarkThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 1, 1, 7),
    _CgrPerVcqRmThreshGrpMarkThreshold_Type()
)
cgrPerVcqRmThreshGrpMarkThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpMarkThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpMarkThreshold.setUnits("percentage")


class _CgrPerVcqRmThreshGrpName_Type(DisplayString):
    """Custom type cgrPerVcqRmThreshGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CgrPerVcqRmThreshGrpName_Type.__name__ = "DisplayString"
_CgrPerVcqRmThreshGrpName_Object = MibTableColumn
cgrPerVcqRmThreshGrpName = _CgrPerVcqRmThreshGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 1, 1, 8),
    _CgrPerVcqRmThreshGrpName_Type()
)
cgrPerVcqRmThreshGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpName.setStatus("current")
_CgrPerVcqRmThreshGrpCellCount_Type = Gauge32
_CgrPerVcqRmThreshGrpCellCount_Object = MibTableColumn
cgrPerVcqRmThreshGrpCellCount = _CgrPerVcqRmThreshGrpCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 1, 1, 9),
    _CgrPerVcqRmThreshGrpCellCount_Type()
)
cgrPerVcqRmThreshGrpCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpCellCount.setStatus("current")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpCellCount.setUnits("cells")
_CgrPerVcqRmThreshGrpServiceTable_Object = MibTable
cgrPerVcqRmThreshGrpServiceTable = _CgrPerVcqRmThreshGrpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 2)
)
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpServiceTable.setStatus("current")
_CgrPerVcqRmThreshGrpServiceEntry_Object = MibTableRow
cgrPerVcqRmThreshGrpServiceEntry = _CgrPerVcqRmThreshGrpServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 2, 1)
)
cgrPerVcqRmThreshGrpServiceEntry.setIndexNames(
    (0, "CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpService"),
)
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpServiceEntry.setStatus("current")
_CgrPerVcqRmThreshGrpService_Type = LsPerVcqThresholdGroupService
_CgrPerVcqRmThreshGrpService_Object = MibTableColumn
cgrPerVcqRmThreshGrpService = _CgrPerVcqRmThreshGrpService_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 2, 1, 1),
    _CgrPerVcqRmThreshGrpService_Type()
)
cgrPerVcqRmThreshGrpService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpService.setStatus("current")
_CgrPerVcqRmThreshGrpServGroup_Type = LsPerVcqThresholdGroup
_CgrPerVcqRmThreshGrpServGroup_Object = MibTableColumn
cgrPerVcqRmThreshGrpServGroup = _CgrPerVcqRmThreshGrpServGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 2, 1, 2),
    _CgrPerVcqRmThreshGrpServGroup_Type()
)
cgrPerVcqRmThreshGrpServGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrPerVcqRmThreshGrpServGroup.setStatus("current")


class _CgrPerVcqRmHierarchicalSchedulingMode_Type(Integer32):
    """Custom type cgrPerVcqRmHierarchicalSchedulingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CgrPerVcqRmHierarchicalSchedulingMode_Type.__name__ = "Integer32"
_CgrPerVcqRmHierarchicalSchedulingMode_Object = MibScalar
cgrPerVcqRmHierarchicalSchedulingMode = _CgrPerVcqRmHierarchicalSchedulingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 9, 3),
    _CgrPerVcqRmHierarchicalSchedulingMode_Type()
)
cgrPerVcqRmHierarchicalSchedulingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgrPerVcqRmHierarchicalSchedulingMode.setStatus("current")
_CiscoAtmRmTrafShaperIf_ObjectIdentity = ObjectIdentity
ciscoAtmRmTrafShaperIf = _CiscoAtmRmTrafShaperIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10)
)
_RmTrafficShaperIfTable_Object = MibTable
rmTrafficShaperIfTable = _RmTrafficShaperIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1)
)
if mibBuilder.loadTexts:
    rmTrafficShaperIfTable.setStatus("current")
_RmTrafficShaperIfEntry_Object = MibTableRow
rmTrafficShaperIfEntry = _RmTrafficShaperIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1)
)
rmTrafficShaperIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rmTrafficShaperIfEntry.setStatus("current")


class _RtsIfMaxThreshold_Type(Unsigned32):
    """Custom type rtsIfMaxThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtsIfMaxThreshold_Type.__name__ = "Unsigned32"
_RtsIfMaxThreshold_Object = MibTableColumn
rtsIfMaxThreshold = _RtsIfMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 1),
    _RtsIfMaxThreshold_Type()
)
rtsIfMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsIfMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rtsIfMaxThreshold.setUnits("cells")
_RtsIfCellCount_Type = Gauge32
_RtsIfCellCount_Object = MibTableColumn
rtsIfCellCount = _RtsIfCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 2),
    _RtsIfCellCount_Type()
)
rtsIfCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsIfCellCount.setStatus("current")
if mibBuilder.loadTexts:
    rtsIfCellCount.setUnits("cells")


class _RtsIfVbrCfgRequested_Type(Integer32):
    """Custom type rtsIfVbrCfgRequested based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("shapeToPcr", 2),
          ("shapeToScrAndPcr", 3),
          ("shapingDisable", 1))
    )


_RtsIfVbrCfgRequested_Type.__name__ = "Integer32"
_RtsIfVbrCfgRequested_Object = MibTableColumn
rtsIfVbrCfgRequested = _RtsIfVbrCfgRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 3),
    _RtsIfVbrCfgRequested_Type()
)
rtsIfVbrCfgRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsIfVbrCfgRequested.setStatus("current")


class _RtsIfVbrCfgInstalled_Type(Integer32):
    """Custom type rtsIfVbrCfgInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("shapeToPcr", 2),
          ("shapeToScrAndPcr", 3),
          ("shapingDisable", 1))
    )


_RtsIfVbrCfgInstalled_Type.__name__ = "Integer32"
_RtsIfVbrCfgInstalled_Object = MibTableColumn
rtsIfVbrCfgInstalled = _RtsIfVbrCfgInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 4),
    _RtsIfVbrCfgInstalled_Type()
)
rtsIfVbrCfgInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsIfVbrCfgInstalled.setStatus("current")


class _RtsIfBeCfgRequested_Type(Integer32):
    """Custom type rtsIfBeCfgRequested based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shapeToPcr", 2),
          ("shapingDisable", 1))
    )


_RtsIfBeCfgRequested_Type.__name__ = "Integer32"
_RtsIfBeCfgRequested_Object = MibTableColumn
rtsIfBeCfgRequested = _RtsIfBeCfgRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 5),
    _RtsIfBeCfgRequested_Type()
)
rtsIfBeCfgRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsIfBeCfgRequested.setStatus("current")


class _RtsIfBeCfgInstalled_Type(Integer32):
    """Custom type rtsIfBeCfgInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shapeToPcr", 2),
          ("shapingDisable", 1))
    )


_RtsIfBeCfgInstalled_Type.__name__ = "Integer32"
_RtsIfBeCfgInstalled_Object = MibTableColumn
rtsIfBeCfgInstalled = _RtsIfBeCfgInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 6),
    _RtsIfBeCfgInstalled_Type()
)
rtsIfBeCfgInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsIfBeCfgInstalled.setStatus("current")


class _RtsIfVbrClassMaxThrshRequested_Type(Integer32):
    """Custom type rtsIfVbrClassMaxThrshRequested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 95),
    )


_RtsIfVbrClassMaxThrshRequested_Type.__name__ = "Integer32"
_RtsIfVbrClassMaxThrshRequested_Object = MibTableColumn
rtsIfVbrClassMaxThrshRequested = _RtsIfVbrClassMaxThrshRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 7),
    _RtsIfVbrClassMaxThrshRequested_Type()
)
rtsIfVbrClassMaxThrshRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsIfVbrClassMaxThrshRequested.setStatus("current")
if mibBuilder.loadTexts:
    rtsIfVbrClassMaxThrshRequested.setUnits("percent")


class _RtsIfVbrClassMaxThrshInstalled_Type(Unsigned32):
    """Custom type rtsIfVbrClassMaxThrshInstalled based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtsIfVbrClassMaxThrshInstalled_Type.__name__ = "Unsigned32"
_RtsIfVbrClassMaxThrshInstalled_Object = MibTableColumn
rtsIfVbrClassMaxThrshInstalled = _RtsIfVbrClassMaxThrshInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 8),
    _RtsIfVbrClassMaxThrshInstalled_Type()
)
rtsIfVbrClassMaxThrshInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsIfVbrClassMaxThrshInstalled.setStatus("current")
if mibBuilder.loadTexts:
    rtsIfVbrClassMaxThrshInstalled.setUnits("cells")


class _RtsIfBeClassMaxThrshRequested_Type(Integer32):
    """Custom type rtsIfBeClassMaxThrshRequested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 95),
    )


_RtsIfBeClassMaxThrshRequested_Type.__name__ = "Integer32"
_RtsIfBeClassMaxThrshRequested_Object = MibTableColumn
rtsIfBeClassMaxThrshRequested = _RtsIfBeClassMaxThrshRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 9),
    _RtsIfBeClassMaxThrshRequested_Type()
)
rtsIfBeClassMaxThrshRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsIfBeClassMaxThrshRequested.setStatus("current")
if mibBuilder.loadTexts:
    rtsIfBeClassMaxThrshRequested.setUnits("percent")


class _RtsIfBeClassMaxThrshInstalled_Type(Unsigned32):
    """Custom type rtsIfBeClassMaxThrshInstalled based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtsIfBeClassMaxThrshInstalled_Type.__name__ = "Unsigned32"
_RtsIfBeClassMaxThrshInstalled_Object = MibTableColumn
rtsIfBeClassMaxThrshInstalled = _RtsIfBeClassMaxThrshInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 10),
    _RtsIfBeClassMaxThrshInstalled_Type()
)
rtsIfBeClassMaxThrshInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsIfBeClassMaxThrshInstalled.setStatus("current")
if mibBuilder.loadTexts:
    rtsIfBeClassMaxThrshInstalled.setUnits("cells")


class _RtsIfVbrVcMaxThrshRequested_Type(Unsigned32):
    """Custom type rtsIfVbrVcMaxThrshRequested based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtsIfVbrVcMaxThrshRequested_Type.__name__ = "Unsigned32"
_RtsIfVbrVcMaxThrshRequested_Object = MibTableColumn
rtsIfVbrVcMaxThrshRequested = _RtsIfVbrVcMaxThrshRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 11),
    _RtsIfVbrVcMaxThrshRequested_Type()
)
rtsIfVbrVcMaxThrshRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsIfVbrVcMaxThrshRequested.setStatus("current")
if mibBuilder.loadTexts:
    rtsIfVbrVcMaxThrshRequested.setUnits("cells")


class _RtsIfVbrVcMaxThrshInstalled_Type(Unsigned32):
    """Custom type rtsIfVbrVcMaxThrshInstalled based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtsIfVbrVcMaxThrshInstalled_Type.__name__ = "Unsigned32"
_RtsIfVbrVcMaxThrshInstalled_Object = MibTableColumn
rtsIfVbrVcMaxThrshInstalled = _RtsIfVbrVcMaxThrshInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 12),
    _RtsIfVbrVcMaxThrshInstalled_Type()
)
rtsIfVbrVcMaxThrshInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsIfVbrVcMaxThrshInstalled.setStatus("current")
if mibBuilder.loadTexts:
    rtsIfVbrVcMaxThrshInstalled.setUnits("cells")


class _RtsIfBeVcMaxThrshRequested_Type(Unsigned32):
    """Custom type rtsIfBeVcMaxThrshRequested based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtsIfBeVcMaxThrshRequested_Type.__name__ = "Unsigned32"
_RtsIfBeVcMaxThrshRequested_Object = MibTableColumn
rtsIfBeVcMaxThrshRequested = _RtsIfBeVcMaxThrshRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 13),
    _RtsIfBeVcMaxThrshRequested_Type()
)
rtsIfBeVcMaxThrshRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsIfBeVcMaxThrshRequested.setStatus("current")
if mibBuilder.loadTexts:
    rtsIfBeVcMaxThrshRequested.setUnits("cells")


class _RtsIfBeVcMaxThrshInstalled_Type(Unsigned32):
    """Custom type rtsIfBeVcMaxThrshInstalled based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtsIfBeVcMaxThrshInstalled_Type.__name__ = "Unsigned32"
_RtsIfBeVcMaxThrshInstalled_Object = MibTableColumn
rtsIfBeVcMaxThrshInstalled = _RtsIfBeVcMaxThrshInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 10, 1, 1, 14),
    _RtsIfBeVcMaxThrshInstalled_Type()
)
rtsIfBeVcMaxThrshInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsIfBeVcMaxThrshInstalled.setStatus("current")
if mibBuilder.loadTexts:
    rtsIfBeVcMaxThrshInstalled.setUnits("cells")
_CiscoAtmRmMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmRmMIBConformance = _CiscoAtmRmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3)
)
_CiscoAtmRmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmRmMIBCompliances = _CiscoAtmRmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1)
)
_CiscoAtmRmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmRmMIBGroups = _CiscoAtmRmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2)
)

# Managed Objects groups

atmRmSwitchCfgMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 1)
)
atmRmSwitchCfgMIBGroup.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmSwitchOverSubFactor"),
        ("CISCO-ATM-RM-MIB", "rmSwitchScrMarginFactor"),
        ("CISCO-ATM-RM-MIB", "rmSwitchAbrCongNotify"),
        ("CISCO-ATM-RM-MIB", "rmScDefaultQosMaxCtd"),
        ("CISCO-ATM-RM-MIB", "rmScDefaultQosPeakToPeakCdv"),
        ("CISCO-ATM-RM-MIB", "rmScDefaultQosClr"))
)
if mibBuilder.loadTexts:
    atmRmSwitchCfgMIBGroup.setStatus("obsolete")

sharedMemAtmRmSwitchMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 2)
)
sharedMemAtmRmSwitchMIBGroup.setObjects(
      *(("CISCO-ATM-RM-MIB", "sharedMemRmSwitchQueuedCellLimit"),
        ("CISCO-ATM-RM-MIB", "sharedMemRmSwitchQueuedCellCount"))
)
if mibBuilder.loadTexts:
    sharedMemAtmRmSwitchMIBGroup.setStatus("current")

atmRmPhyIfCfgMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 3)
)
atmRmPhyIfCfgMIBGroup.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfOutPacingRateRequested"),
        ("CISCO-ATM-RM-MIB", "rmIfOutPacingRateInstalled"),
        ("CISCO-ATM-RM-MIB", "rmIfOutPacingForce"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxAgg"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinCbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxCbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinVbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxVbr"))
)
if mibBuilder.loadTexts:
    atmRmPhyIfCfgMIBGroup.setStatus("obsolete")

atmRmAllIfCfgMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 4)
)
atmRmAllIfCfgMIBGroup.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfLinkDistance"),
        ("CISCO-ATM-RM-MIB", "rmIfBestEffortLimit"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxCbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxCbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrScr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrTolerance"))
)
if mibBuilder.loadTexts:
    atmRmAllIfCfgMIBGroup.setStatus("obsolete")

atmRmIfAllStateMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 5)
)
atmRmIfAllStateMIBGroup.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfScRxAcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxAcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScRxAlcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxAlcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScNumSvxConns"),
        ("CISCO-ATM-RM-MIB", "rmIfScNumPvxConns"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxMaxCtd"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxP2PeakCdv"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxClr"))
)
if mibBuilder.loadTexts:
    atmRmIfAllStateMIBGroup.setStatus("obsolete")

atmRmIfStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 6)
)
atmRmIfStatsMIBGroup.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfScRcacResultNumAdmit"),
        ("CISCO-ATM-RM-MIB", "rmIfScRcacResultNumTotalRequests"),
        ("CISCO-ATM-RM-MIB", "rmIfScRcacResultNumFailTraffComb"),
        ("CISCO-ATM-RM-MIB", "rmIfScRcacResultNumFailBw"),
        ("CISCO-ATM-RM-MIB", "rmIfScRcacResultNumFailLoss"),
        ("CISCO-ATM-RM-MIB", "rmIfScRcacResultNumFailDelay"),
        ("CISCO-ATM-RM-MIB", "rmIfScRcacResultNumFailCdv"),
        ("CISCO-ATM-RM-MIB", "rmIfScRcacResultNumFailBeLimit"),
        ("CISCO-ATM-RM-MIB", "rmIfScRcacResultNumFailParmLimit"),
        ("CISCO-ATM-RM-MIB", "rmIfScRcacResultNumFailOther"))
)
if mibBuilder.loadTexts:
    atmRmIfStatsMIBGroup.setStatus("current")

sharedMemAtmRmPhyIfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 7)
)
sharedMemAtmRmPhyIfMIBGroup.setObjects(
      *(("CISCO-ATM-RM-MIB", "sharedMemRmIfOutputQServCategory"),
        ("CISCO-ATM-RM-MIB", "sharedMemRmIfOutputQRequestedMaxSize"),
        ("CISCO-ATM-RM-MIB", "sharedMemRmIfOutputQInstalledMaxSize"),
        ("CISCO-ATM-RM-MIB", "sharedMemRmIfOutputQMaxSizeForce"),
        ("CISCO-ATM-RM-MIB", "sharedMemRmIfOutputQCellCount"),
        ("CISCO-ATM-RM-MIB", "sharedMemRmIfDiscardThreshold"),
        ("CISCO-ATM-RM-MIB", "sharedMemRmIfEfciThreshold"),
        ("CISCO-ATM-RM-MIB", "sharedMemRmIfAbrRelativeRateThreshold"))
)
if mibBuilder.loadTexts:
    sharedMemAtmRmPhyIfMIBGroup.setStatus("current")

atmRmSwitchCfgMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 8)
)
atmRmSwitchCfgMIBGroup2.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmSwitchOverSubFactor"),
        ("CISCO-ATM-RM-MIB", "rmSwitchScrMarginFactor"),
        ("CISCO-ATM-RM-MIB", "rmSwitchAbrCongNotify"),
        ("CISCO-ATM-RM-MIB", "rmScDefaultQosMaxCtd"),
        ("CISCO-ATM-RM-MIB", "rmScDefaultQosPeakToPeakCdv"),
        ("CISCO-ATM-RM-MIB", "rmScDefaultQosClr"),
        ("CISCO-ATM-RM-MIB", "rmScDefaultQosClrClp01"))
)
if mibBuilder.loadTexts:
    atmRmSwitchCfgMIBGroup2.setStatus("current")

atmRmPhyIfCfgMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 9)
)
atmRmPhyIfCfgMIBGroup2.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfOutPacingRateRequested"),
        ("CISCO-ATM-RM-MIB", "rmIfOutPacingRateInstalled"),
        ("CISCO-ATM-RM-MIB", "rmIfOutPacingForce"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxAgg"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinCbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxCbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinVbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxVbr"),
        ("CISCO-ATM-RM-MIB", "rmIfCbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrRtDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrNrtDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfAbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfUbrDefaultRxUpcTolerance"))
)
if mibBuilder.loadTexts:
    atmRmPhyIfCfgMIBGroup2.setStatus("obsolete")

atmRmIfAllStateMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 10)
)
atmRmIfAllStateMIBGroup2.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfScRxAcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxAcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScRxAlcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxAlcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScNumSvxConns"),
        ("CISCO-ATM-RM-MIB", "rmIfScNumPvxConns"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxMaxCtd"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxP2PeakCdv"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxClr"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxClrClp01"))
)
if mibBuilder.loadTexts:
    atmRmIfAllStateMIBGroup2.setStatus("obsolete")

lsPerVcqAtmRmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 11)
)
lsPerVcqAtmRmGroup.setObjects(
      *(("CISCO-ATM-RM-MIB", "lsPerVcqRmIfMinWrrServiceClass"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmIfServClassConnType"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmIfServClassWrrWeight"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpMaxSize"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpQMaxSize"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpQMinSize"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpDiscThreshold"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpMarkThreshold"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpName"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpCellCount"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpServGroup"))
)
if mibBuilder.loadTexts:
    lsPerVcqAtmRmGroup.setStatus("obsolete")

atmRmPhyIfCfgMIBGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 12)
)
atmRmPhyIfCfgMIBGroup3.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfOutPacingRateRequested"),
        ("CISCO-ATM-RM-MIB", "rmIfOutPacingRateInstalled"),
        ("CISCO-ATM-RM-MIB", "rmIfOutPacingForce"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxAgg"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinCbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxCbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinVbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxVbr"),
        ("CISCO-ATM-RM-MIB", "rmIfCbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrRtDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrNrtDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfAbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfUbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrRtDefaultRxUpcCdvt"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrNrtDefaultRxUpcCdvt"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinAbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxAbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinUbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxUbr"))
)
if mibBuilder.loadTexts:
    atmRmPhyIfCfgMIBGroup3.setStatus("obsolete")

atmRmAllIfCfgMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 13)
)
atmRmAllIfCfgMIBGroup2.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfLinkDistance"),
        ("CISCO-ATM-RM-MIB", "rmIfBestEffortLimit"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxCbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxCbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrScr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrMcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrMcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrCdvt"))
)
if mibBuilder.loadTexts:
    atmRmAllIfCfgMIBGroup2.setStatus("obsolete")

atmRmAllIfCfgMIBGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 14)
)
atmRmAllIfCfgMIBGroup3.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfLinkDistance"),
        ("CISCO-ATM-RM-MIB", "rmIfBestEffortLimit"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxCbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxCbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrScr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrMcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrMcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrCdvt"),
        ("CISCO-ATM-RM-MIB", "rmIfServCategorySupport"))
)
if mibBuilder.loadTexts:
    atmRmAllIfCfgMIBGroup3.setStatus("obsolete")

lsPerVcqAtmRmGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 15)
)
lsPerVcqAtmRmGroup2.setObjects(
      *(("CISCO-ATM-RM-MIB", "lsPerVcqRmIfMinWrrServiceClass"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmIfServClassConnType"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmIfServClassWrrWeight"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpMaxSize"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpQMaxSize"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpQMinSize"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpDiscThreshold"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpMarkThreshold"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpName"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpCellCount"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmThreshGrpServGroup"),
        ("CISCO-ATM-RM-MIB", "lsPerVcqRmHierarchicalSchedulingMode"))
)
if mibBuilder.loadTexts:
    lsPerVcqAtmRmGroup2.setStatus("current")

cgrPerVcqAtmRmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 16)
)
cgrPerVcqAtmRmGroup.setObjects(
      *(("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpQMaxSize"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpQMinSize"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpDiscThreshold"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpMarkThreshold"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpName"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpCellCount"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpServGroup"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmHierarchicalSchedulingMode"))
)
if mibBuilder.loadTexts:
    cgrPerVcqAtmRmGroup.setStatus("obsolete")

atmRmAllIfCfgMIBGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 17)
)
atmRmAllIfCfgMIBGroup4.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfLinkDistance"),
        ("CISCO-ATM-RM-MIB", "rmIfBestEffortLimit"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxCbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxCbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrScr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrMcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrMcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrCdvt"),
        ("CISCO-ATM-RM-MIB", "rmIfServCategorySupport"),
        ("CISCO-ATM-RM-MIB", "rmIfCbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrRtDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrNrtDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfAbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfUbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrRtDefaultRxUpcCdvt"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrNrtDefaultRxUpcCdvt"))
)
if mibBuilder.loadTexts:
    atmRmAllIfCfgMIBGroup4.setStatus("obsolete")

atmRmPhyIfCfgMIBGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 18)
)
atmRmPhyIfCfgMIBGroup4.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfOutPacingRateRequested"),
        ("CISCO-ATM-RM-MIB", "rmIfOutPacingRateInstalled"),
        ("CISCO-ATM-RM-MIB", "rmIfOutPacingForce"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxAgg"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinCbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxCbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinVbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxVbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinAbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxAbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinUbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxUbr"))
)
if mibBuilder.loadTexts:
    atmRmPhyIfCfgMIBGroup4.setStatus("obsolete")

atmRmPhyIfCfgMIBGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 19)
)
atmRmPhyIfCfgMIBGroup5.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfOutPacingRateRequested"),
        ("CISCO-ATM-RM-MIB", "rmIfOutPacingRateInstalled"),
        ("CISCO-ATM-RM-MIB", "rmIfOutPacingForce"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxAgg"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinCbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxCbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinVbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxVbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinAbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxAbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMinUbr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirControlLinkShareMaxUbr"),
        ("CISCO-ATM-RM-MIB", "rmIfFramingOverhead"),
        ("CISCO-ATM-RM-MIB", "rmIfFramingOverheadForce"))
)
if mibBuilder.loadTexts:
    atmRmPhyIfCfgMIBGroup5.setStatus("current")

atmRmIfAllStateMIBGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 20)
)
atmRmIfAllStateMIBGroup3.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfScRxAcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxAcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScRxAlcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxAlcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScNumSvxConns"),
        ("CISCO-ATM-RM-MIB", "rmIfScNumPvxConns"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxMaxCtd"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxP2PeakCdv"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxClr"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxClrClp01"),
        ("CISCO-ATM-RM-MIB", "rmIfScRxDynBwSvcAcr"),
        ("CISCO-ATM-RM-MIB", "rmIfScTxDynBwSvcAcr"))
)
if mibBuilder.loadTexts:
    atmRmIfAllStateMIBGroup3.setStatus("current")

atmRmAllIfCfgMIBGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 21)
)
atmRmAllIfCfgMIBGroup5.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfLinkDistance"),
        ("CISCO-ATM-RM-MIB", "rmIfBestEffortLimit"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxCbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxCbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrScr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrMcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrMcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrCdvt"),
        ("CISCO-ATM-RM-MIB", "rmIfServCategorySupport"),
        ("CISCO-ATM-RM-MIB", "rmIfCbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrRtDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrNrtDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfAbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfUbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrRtDefaultRxUpcCdvt"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrNrtDefaultRxUpcCdvt"),
        ("CISCO-ATM-RM-MIB", "rmIfOverBooking"))
)
if mibBuilder.loadTexts:
    atmRmAllIfCfgMIBGroup5.setStatus("deprecated")

cgrPerVcqAtmRmGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 22)
)
cgrPerVcqAtmRmGroup2.setObjects(
      *(("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpQMaxSize"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpQMinSize"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpDiscThreshold"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpMaxSize"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpMarkThreshold"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpName"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpCellCount"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmThreshGrpServGroup"),
        ("CISCO-ATM-RM-MIB", "cgrPerVcqRmHierarchicalSchedulingMode"))
)
if mibBuilder.loadTexts:
    cgrPerVcqAtmRmGroup2.setStatus("current")

atmRmTrafficShaperIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 23)
)
atmRmTrafficShaperIfGroup.setObjects(
      *(("CISCO-ATM-RM-MIB", "rtsIfMaxThreshold"),
        ("CISCO-ATM-RM-MIB", "rtsIfCellCount"),
        ("CISCO-ATM-RM-MIB", "rtsIfVbrCfgRequested"),
        ("CISCO-ATM-RM-MIB", "rtsIfVbrCfgInstalled"),
        ("CISCO-ATM-RM-MIB", "rtsIfBeCfgRequested"),
        ("CISCO-ATM-RM-MIB", "rtsIfBeCfgInstalled"),
        ("CISCO-ATM-RM-MIB", "rtsIfVbrClassMaxThrshRequested"),
        ("CISCO-ATM-RM-MIB", "rtsIfVbrClassMaxThrshInstalled"),
        ("CISCO-ATM-RM-MIB", "rtsIfBeClassMaxThrshRequested"),
        ("CISCO-ATM-RM-MIB", "rtsIfBeClassMaxThrshInstalled"),
        ("CISCO-ATM-RM-MIB", "rtsIfVbrVcMaxThrshRequested"),
        ("CISCO-ATM-RM-MIB", "rtsIfVbrVcMaxThrshInstalled"),
        ("CISCO-ATM-RM-MIB", "rtsIfBeVcMaxThrshRequested"),
        ("CISCO-ATM-RM-MIB", "rtsIfBeVcMaxThrshInstalled"))
)
if mibBuilder.loadTexts:
    atmRmTrafficShaperIfGroup.setStatus("current")

atmRmAllIfCfgMIBGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 24)
)
atmRmAllIfCfgMIBGroup6.setObjects(
      *(("CISCO-ATM-RM-MIB", "rmIfLinkDistance"),
        ("CISCO-ATM-RM-MIB", "rmIfBestEffortLimit"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxCbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxCbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrScr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrPcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxAbrMcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxUbrMcr"),
        ("CISCO-ATM-RM-MIB", "rmIfDirMaxVbrCdvt"),
        ("CISCO-ATM-RM-MIB", "rmIfServCategorySupport"),
        ("CISCO-ATM-RM-MIB", "rmIfCbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrRtDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrNrtDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfAbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfUbrDefaultRxUpcTolerance"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrRtDefaultRxUpcCdvt"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrNrtDefaultRxUpcCdvt"),
        ("CISCO-ATM-RM-MIB", "rmIfOverBooking"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrRtPerClassOverbooking"),
        ("CISCO-ATM-RM-MIB", "rmIfVbrNrtPerClassOverbooking"),
        ("CISCO-ATM-RM-MIB", "rmIfAbrPerClassOverbooking"),
        ("CISCO-ATM-RM-MIB", "rmIfUbrPerClassOverbooking"))
)
if mibBuilder.loadTexts:
    atmRmAllIfCfgMIBGroup6.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmRmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance.setStatus(
        "obsolete"
    )

ciscoAtmRmMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance2.setStatus(
        "obsolete"
    )

ciscoAtmRmMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance3.setStatus(
        "obsolete"
    )

ciscoAtmRmMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance4.setStatus(
        "obsolete"
    )

ciscoAtmRmMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance5.setStatus(
        "obsolete"
    )

ciscoAtmRmMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance6.setStatus(
        "obsolete"
    )

ciscoAtmRmMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance7.setStatus(
        "obsolete"
    )

ciscoAtmRmMIBCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance8.setStatus(
        "obsolete"
    )

ciscoAtmRmMIBCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 9)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance9.setStatus(
        "obsolete"
    )

ciscoAtmRmMIBCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 10)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance10.setStatus(
        "obsolete"
    )

ciscoAtmRmMIBCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 11)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance11.setStatus(
        "obsolete"
    )

ciscoAtmRmMIBCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 12)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance12.setStatus(
        "deprecated"
    )

ciscoAtmRmMIBCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1, 13)
)
if mibBuilder.loadTexts:
    ciscoAtmRmMIBCompliance13.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-RM-MIB",
    **{"ForceValue": ForceValue,
       "FineQueueThreshold": FineQueueThreshold,
       "LsPerVcqServiceClass": LsPerVcqServiceClass,
       "LsPerVcqServiceClassNoC1": LsPerVcqServiceClassNoC1,
       "LsPerVcqThresholdGroup": LsPerVcqThresholdGroup,
       "LsPerVcqThresholdGroupService": LsPerVcqThresholdGroupService,
       "CgrPerVcqModuleId": CgrPerVcqModuleId,
       "ciscoAtmRmMIB": ciscoAtmRmMIB,
       "ciscoAtmRmMIBObjects": ciscoAtmRmMIBObjects,
       "ciscoAtmRmSwitchCfg": ciscoAtmRmSwitchCfg,
       "rmSwitchOverSubFactor": rmSwitchOverSubFactor,
       "rmSwitchScrMarginFactor": rmSwitchScrMarginFactor,
       "rmSwitchAbrCongNotify": rmSwitchAbrCongNotify,
       "rmDefaultQosObjectiveTable": rmDefaultQosObjectiveTable,
       "rmDefaultQosObjectiveEntry": rmDefaultQosObjectiveEntry,
       "rmDefaultQosServiceCategory": rmDefaultQosServiceCategory,
       "rmScDefaultQosMaxCtd": rmScDefaultQosMaxCtd,
       "rmScDefaultQosPeakToPeakCdv": rmScDefaultQosPeakToPeakCdv,
       "rmScDefaultQosClr": rmScDefaultQosClr,
       "rmScDefaultQosClrClp01": rmScDefaultQosClrClp01,
       "ciscoAtmRmSwitchSharedMem": ciscoAtmRmSwitchSharedMem,
       "sharedMemRmSwitchQueuedCellTable": sharedMemRmSwitchQueuedCellTable,
       "sharedMemRmSwitchQueuedCellEntry": sharedMemRmSwitchQueuedCellEntry,
       "sharedMemRmCellPriority": sharedMemRmCellPriority,
       "sharedMemRmSwitchQueuedCellLimit": sharedMemRmSwitchQueuedCellLimit,
       "sharedMemRmSwitchQueuedCellCount": sharedMemRmSwitchQueuedCellCount,
       "ciscoAtmRmIfCfg": ciscoAtmRmIfCfg,
       "rmIfCfgTable": rmIfCfgTable,
       "rmIfCfgEntry": rmIfCfgEntry,
       "rmIfOutPacingRateRequested": rmIfOutPacingRateRequested,
       "rmIfOutPacingRateInstalled": rmIfOutPacingRateInstalled,
       "rmIfOutPacingForce": rmIfOutPacingForce,
       "rmIfLinkDistance": rmIfLinkDistance,
       "rmIfBestEffortLimit": rmIfBestEffortLimit,
       "rmIfCbrDefaultRxUpcTolerance": rmIfCbrDefaultRxUpcTolerance,
       "rmIfVbrRtDefaultRxUpcTolerance": rmIfVbrRtDefaultRxUpcTolerance,
       "rmIfVbrNrtDefaultRxUpcTolerance": rmIfVbrNrtDefaultRxUpcTolerance,
       "rmIfAbrDefaultRxUpcTolerance": rmIfAbrDefaultRxUpcTolerance,
       "rmIfUbrDefaultRxUpcTolerance": rmIfUbrDefaultRxUpcTolerance,
       "rmIfVbrRtDefaultRxUpcCdvt": rmIfVbrRtDefaultRxUpcCdvt,
       "rmIfVbrNrtDefaultRxUpcCdvt": rmIfVbrNrtDefaultRxUpcCdvt,
       "rmIfServCategorySupport": rmIfServCategorySupport,
       "rmIfFramingOverhead": rmIfFramingOverhead,
       "rmIfFramingOverheadForce": rmIfFramingOverheadForce,
       "rmIfOverBooking": rmIfOverBooking,
       "rmIfVbrRtPerClassOverbooking": rmIfVbrRtPerClassOverbooking,
       "rmIfVbrNrtPerClassOverbooking": rmIfVbrNrtPerClassOverbooking,
       "rmIfAbrPerClassOverbooking": rmIfAbrPerClassOverbooking,
       "rmIfUbrPerClassOverbooking": rmIfUbrPerClassOverbooking,
       "rmIfDirectionCfgTable": rmIfDirectionCfgTable,
       "rmIfDirectionCfgEntry": rmIfDirectionCfgEntry,
       "rmIfDirection": rmIfDirection,
       "rmIfDirControlLinkShareMaxAgg": rmIfDirControlLinkShareMaxAgg,
       "rmIfDirControlLinkShareMinCbr": rmIfDirControlLinkShareMinCbr,
       "rmIfDirControlLinkShareMaxCbr": rmIfDirControlLinkShareMaxCbr,
       "rmIfDirControlLinkShareMinVbr": rmIfDirControlLinkShareMinVbr,
       "rmIfDirControlLinkShareMaxVbr": rmIfDirControlLinkShareMaxVbr,
       "rmIfDirMaxCbrPcr": rmIfDirMaxCbrPcr,
       "rmIfDirMaxCbrTolerance": rmIfDirMaxCbrTolerance,
       "rmIfDirMaxVbrPcr": rmIfDirMaxVbrPcr,
       "rmIfDirMaxVbrScr": rmIfDirMaxVbrScr,
       "rmIfDirMaxVbrTolerance": rmIfDirMaxVbrTolerance,
       "rmIfDirMaxAbrPcr": rmIfDirMaxAbrPcr,
       "rmIfDirMaxAbrTolerance": rmIfDirMaxAbrTolerance,
       "rmIfDirMaxUbrPcr": rmIfDirMaxUbrPcr,
       "rmIfDirMaxUbrTolerance": rmIfDirMaxUbrTolerance,
       "rmIfDirMaxAbrMcr": rmIfDirMaxAbrMcr,
       "rmIfDirMaxUbrMcr": rmIfDirMaxUbrMcr,
       "rmIfDirMaxVbrCdvt": rmIfDirMaxVbrCdvt,
       "rmIfDirControlLinkShareMinAbr": rmIfDirControlLinkShareMinAbr,
       "rmIfDirControlLinkShareMaxAbr": rmIfDirControlLinkShareMaxAbr,
       "rmIfDirControlLinkShareMinUbr": rmIfDirControlLinkShareMinUbr,
       "rmIfDirControlLinkShareMaxUbr": rmIfDirControlLinkShareMaxUbr,
       "ciscoAtmRmIfState": ciscoAtmRmIfState,
       "rmIfServiceCategoryStateTable": rmIfServiceCategoryStateTable,
       "rmIfServiceCategoryStateEntry": rmIfServiceCategoryStateEntry,
       "rmIfSc": rmIfSc,
       "rmIfScRxAcr": rmIfScRxAcr,
       "rmIfScTxAcr": rmIfScTxAcr,
       "rmIfScRxAlcr": rmIfScRxAlcr,
       "rmIfScTxAlcr": rmIfScTxAlcr,
       "rmIfScNumSvxConns": rmIfScNumSvxConns,
       "rmIfScNumPvxConns": rmIfScNumPvxConns,
       "rmIfScTxMaxCtd": rmIfScTxMaxCtd,
       "rmIfScTxP2PeakCdv": rmIfScTxP2PeakCdv,
       "rmIfScTxClr": rmIfScTxClr,
       "rmIfScTxClrClp01": rmIfScTxClrClp01,
       "rmIfScRxDynBwSvcAcr": rmIfScRxDynBwSvcAcr,
       "rmIfScTxDynBwSvcAcr": rmIfScTxDynBwSvcAcr,
       "ciscoAtmRmIfStatistics": ciscoAtmRmIfStatistics,
       "rmIfServiceCategoryStatisticsTable": rmIfServiceCategoryStatisticsTable,
       "rmIfServiceCategoryStatisticsEntry": rmIfServiceCategoryStatisticsEntry,
       "rmIfScRcacResultNumAdmit": rmIfScRcacResultNumAdmit,
       "rmIfScRcacResultNumTotalRequests": rmIfScRcacResultNumTotalRequests,
       "rmIfScRcacResultNumFailTraffComb": rmIfScRcacResultNumFailTraffComb,
       "rmIfScRcacResultNumFailBw": rmIfScRcacResultNumFailBw,
       "rmIfScRcacResultNumFailLoss": rmIfScRcacResultNumFailLoss,
       "rmIfScRcacResultNumFailDelay": rmIfScRcacResultNumFailDelay,
       "rmIfScRcacResultNumFailCdv": rmIfScRcacResultNumFailCdv,
       "rmIfScRcacResultNumFailBeLimit": rmIfScRcacResultNumFailBeLimit,
       "rmIfScRcacResultNumFailParmLimit": rmIfScRcacResultNumFailParmLimit,
       "rmIfScRcacResultNumFailOther": rmIfScRcacResultNumFailOther,
       "ciscoAtmRmIfSharedMem": ciscoAtmRmIfSharedMem,
       "sharedMemRmIfOutputQCfgTable": sharedMemRmIfOutputQCfgTable,
       "sharedMemRmIfOutputQCfgEntry": sharedMemRmIfOutputQCfgEntry,
       "sharedMemRmIfOutputQ": sharedMemRmIfOutputQ,
       "sharedMemRmIfOutputQServCategory": sharedMemRmIfOutputQServCategory,
       "sharedMemRmIfOutputQRequestedMaxSize": sharedMemRmIfOutputQRequestedMaxSize,
       "sharedMemRmIfOutputQInstalledMaxSize": sharedMemRmIfOutputQInstalledMaxSize,
       "sharedMemRmIfOutputQMaxSizeForce": sharedMemRmIfOutputQMaxSizeForce,
       "sharedMemRmIfOutputQCellCount": sharedMemRmIfOutputQCellCount,
       "sharedMemRmIfThresholdCfgTable": sharedMemRmIfThresholdCfgTable,
       "sharedMemRmIfThresholdCfgEntry": sharedMemRmIfThresholdCfgEntry,
       "sharedMemRmIfDiscardThreshold": sharedMemRmIfDiscardThreshold,
       "sharedMemRmIfEfciThreshold": sharedMemRmIfEfciThreshold,
       "sharedMemRmIfAbrRelativeRateThreshold": sharedMemRmIfAbrRelativeRateThreshold,
       "ciscoLsPerVcqAtmRmSwitch": ciscoLsPerVcqAtmRmSwitch,
       "lsPerVcqRmThreshGrpTable": lsPerVcqRmThreshGrpTable,
       "lsPerVcqRmThreshGrpEntry": lsPerVcqRmThreshGrpEntry,
       "lsPerVcqRmThreshGrp": lsPerVcqRmThreshGrp,
       "lsPerVcqRmThreshGrpMaxSize": lsPerVcqRmThreshGrpMaxSize,
       "lsPerVcqRmThreshGrpQMaxSize": lsPerVcqRmThreshGrpQMaxSize,
       "lsPerVcqRmThreshGrpQMinSize": lsPerVcqRmThreshGrpQMinSize,
       "lsPerVcqRmThreshGrpDiscThreshold": lsPerVcqRmThreshGrpDiscThreshold,
       "lsPerVcqRmThreshGrpMarkThreshold": lsPerVcqRmThreshGrpMarkThreshold,
       "lsPerVcqRmThreshGrpName": lsPerVcqRmThreshGrpName,
       "lsPerVcqRmThreshGrpCellCount": lsPerVcqRmThreshGrpCellCount,
       "lsPerVcqRmThreshGrpServiceTable": lsPerVcqRmThreshGrpServiceTable,
       "lsPerVcqRmThreshGrpServiceEntry": lsPerVcqRmThreshGrpServiceEntry,
       "lsPerVcqRmThreshGrpService": lsPerVcqRmThreshGrpService,
       "lsPerVcqRmThreshGrpServGroup": lsPerVcqRmThreshGrpServGroup,
       "lsPerVcqRmHierarchicalSchedulingMode": lsPerVcqRmHierarchicalSchedulingMode,
       "ciscoLsPerVcqAtmRmIf": ciscoLsPerVcqAtmRmIf,
       "lsPerVcqRmIfTable": lsPerVcqRmIfTable,
       "lsPerVcqRmIfEntry": lsPerVcqRmIfEntry,
       "lsPerVcqRmIfMinWrrServiceClass": lsPerVcqRmIfMinWrrServiceClass,
       "lsPerVcqRmIfServiceClassTable": lsPerVcqRmIfServiceClassTable,
       "lsPerVcqRmIfServiceClassEntry": lsPerVcqRmIfServiceClassEntry,
       "lsPerVcqRmIfServiceClass": lsPerVcqRmIfServiceClass,
       "lsPerVcqRmIfServClassConnType": lsPerVcqRmIfServClassConnType,
       "lsPerVcqRmIfServClassWrrWeight": lsPerVcqRmIfServClassWrrWeight,
       "ciscoCgrPerVcqAtmRmSwitch": ciscoCgrPerVcqAtmRmSwitch,
       "cgrPerVcqRmThreshGrpTable": cgrPerVcqRmThreshGrpTable,
       "cgrPerVcqRmThreshGrpEntry": cgrPerVcqRmThreshGrpEntry,
       "cgrPerVcqModuleId": cgrPerVcqModuleId,
       "cgrPerVcqRmThreshGrp": cgrPerVcqRmThreshGrp,
       "cgrPerVcqRmThreshGrpMaxSize": cgrPerVcqRmThreshGrpMaxSize,
       "cgrPerVcqRmThreshGrpQMaxSize": cgrPerVcqRmThreshGrpQMaxSize,
       "cgrPerVcqRmThreshGrpQMinSize": cgrPerVcqRmThreshGrpQMinSize,
       "cgrPerVcqRmThreshGrpDiscThreshold": cgrPerVcqRmThreshGrpDiscThreshold,
       "cgrPerVcqRmThreshGrpMarkThreshold": cgrPerVcqRmThreshGrpMarkThreshold,
       "cgrPerVcqRmThreshGrpName": cgrPerVcqRmThreshGrpName,
       "cgrPerVcqRmThreshGrpCellCount": cgrPerVcqRmThreshGrpCellCount,
       "cgrPerVcqRmThreshGrpServiceTable": cgrPerVcqRmThreshGrpServiceTable,
       "cgrPerVcqRmThreshGrpServiceEntry": cgrPerVcqRmThreshGrpServiceEntry,
       "cgrPerVcqRmThreshGrpService": cgrPerVcqRmThreshGrpService,
       "cgrPerVcqRmThreshGrpServGroup": cgrPerVcqRmThreshGrpServGroup,
       "cgrPerVcqRmHierarchicalSchedulingMode": cgrPerVcqRmHierarchicalSchedulingMode,
       "ciscoAtmRmTrafShaperIf": ciscoAtmRmTrafShaperIf,
       "rmTrafficShaperIfTable": rmTrafficShaperIfTable,
       "rmTrafficShaperIfEntry": rmTrafficShaperIfEntry,
       "rtsIfMaxThreshold": rtsIfMaxThreshold,
       "rtsIfCellCount": rtsIfCellCount,
       "rtsIfVbrCfgRequested": rtsIfVbrCfgRequested,
       "rtsIfVbrCfgInstalled": rtsIfVbrCfgInstalled,
       "rtsIfBeCfgRequested": rtsIfBeCfgRequested,
       "rtsIfBeCfgInstalled": rtsIfBeCfgInstalled,
       "rtsIfVbrClassMaxThrshRequested": rtsIfVbrClassMaxThrshRequested,
       "rtsIfVbrClassMaxThrshInstalled": rtsIfVbrClassMaxThrshInstalled,
       "rtsIfBeClassMaxThrshRequested": rtsIfBeClassMaxThrshRequested,
       "rtsIfBeClassMaxThrshInstalled": rtsIfBeClassMaxThrshInstalled,
       "rtsIfVbrVcMaxThrshRequested": rtsIfVbrVcMaxThrshRequested,
       "rtsIfVbrVcMaxThrshInstalled": rtsIfVbrVcMaxThrshInstalled,
       "rtsIfBeVcMaxThrshRequested": rtsIfBeVcMaxThrshRequested,
       "rtsIfBeVcMaxThrshInstalled": rtsIfBeVcMaxThrshInstalled,
       "ciscoAtmRmMIBConformance": ciscoAtmRmMIBConformance,
       "ciscoAtmRmMIBCompliances": ciscoAtmRmMIBCompliances,
       "ciscoAtmRmMIBCompliance": ciscoAtmRmMIBCompliance,
       "ciscoAtmRmMIBCompliance2": ciscoAtmRmMIBCompliance2,
       "ciscoAtmRmMIBCompliance3": ciscoAtmRmMIBCompliance3,
       "ciscoAtmRmMIBCompliance4": ciscoAtmRmMIBCompliance4,
       "ciscoAtmRmMIBCompliance5": ciscoAtmRmMIBCompliance5,
       "ciscoAtmRmMIBCompliance6": ciscoAtmRmMIBCompliance6,
       "ciscoAtmRmMIBCompliance7": ciscoAtmRmMIBCompliance7,
       "ciscoAtmRmMIBCompliance8": ciscoAtmRmMIBCompliance8,
       "ciscoAtmRmMIBCompliance9": ciscoAtmRmMIBCompliance9,
       "ciscoAtmRmMIBCompliance10": ciscoAtmRmMIBCompliance10,
       "ciscoAtmRmMIBCompliance11": ciscoAtmRmMIBCompliance11,
       "ciscoAtmRmMIBCompliance12": ciscoAtmRmMIBCompliance12,
       "ciscoAtmRmMIBCompliance13": ciscoAtmRmMIBCompliance13,
       "ciscoAtmRmMIBGroups": ciscoAtmRmMIBGroups,
       "atmRmSwitchCfgMIBGroup": atmRmSwitchCfgMIBGroup,
       "sharedMemAtmRmSwitchMIBGroup": sharedMemAtmRmSwitchMIBGroup,
       "atmRmPhyIfCfgMIBGroup": atmRmPhyIfCfgMIBGroup,
       "atmRmAllIfCfgMIBGroup": atmRmAllIfCfgMIBGroup,
       "atmRmIfAllStateMIBGroup": atmRmIfAllStateMIBGroup,
       "atmRmIfStatsMIBGroup": atmRmIfStatsMIBGroup,
       "sharedMemAtmRmPhyIfMIBGroup": sharedMemAtmRmPhyIfMIBGroup,
       "atmRmSwitchCfgMIBGroup2": atmRmSwitchCfgMIBGroup2,
       "atmRmPhyIfCfgMIBGroup2": atmRmPhyIfCfgMIBGroup2,
       "atmRmIfAllStateMIBGroup2": atmRmIfAllStateMIBGroup2,
       "lsPerVcqAtmRmGroup": lsPerVcqAtmRmGroup,
       "atmRmPhyIfCfgMIBGroup3": atmRmPhyIfCfgMIBGroup3,
       "atmRmAllIfCfgMIBGroup2": atmRmAllIfCfgMIBGroup2,
       "atmRmAllIfCfgMIBGroup3": atmRmAllIfCfgMIBGroup3,
       "lsPerVcqAtmRmGroup2": lsPerVcqAtmRmGroup2,
       "cgrPerVcqAtmRmGroup": cgrPerVcqAtmRmGroup,
       "atmRmAllIfCfgMIBGroup4": atmRmAllIfCfgMIBGroup4,
       "atmRmPhyIfCfgMIBGroup4": atmRmPhyIfCfgMIBGroup4,
       "atmRmPhyIfCfgMIBGroup5": atmRmPhyIfCfgMIBGroup5,
       "atmRmIfAllStateMIBGroup3": atmRmIfAllStateMIBGroup3,
       "atmRmAllIfCfgMIBGroup5": atmRmAllIfCfgMIBGroup5,
       "cgrPerVcqAtmRmGroup2": cgrPerVcqAtmRmGroup2,
       "atmRmTrafficShaperIfGroup": atmRmTrafficShaperIfGroup,
       "atmRmAllIfCfgMIBGroup6": atmRmAllIfCfgMIBGroup6}
)
