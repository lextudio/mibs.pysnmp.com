# SNMP MIB module (ZHONE-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:35 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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

(zhonePhysical,
 zhoneTrapModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhonePhysical",
    "zhoneTrapModules")


# MODULE-IDENTITY

zhoneIsdn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7)
)
zhoneIsdn.setRevisions(
        ("2003-03-03 11:58",
         "2003-02-04 18:04",
         "2000-09-27 10:57",
         "2000-09-27 19:42")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneIsdnTrap_ObjectIdentity = ObjectIdentity
zhoneIsdnTrap = _ZhoneIsdnTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 3)
)
if mibBuilder.loadTexts:
    zhoneIsdnTrap.setStatus("current")
_IsdnMibV2Traps_ObjectIdentity = ObjectIdentity
isdnMibV2Traps = _IsdnMibV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 3, 1)
)
if mibBuilder.loadTexts:
    isdnMibV2Traps.setStatus("current")
_ZhoneIsdnMib_ObjectIdentity = ObjectIdentity
zhoneIsdnMib = _ZhoneIsdnMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1)
)
_IsdnConfigTable_Object = MibTable
isdnConfigTable = _IsdnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 1)
)
if mibBuilder.loadTexts:
    isdnConfigTable.setStatus("current")
_IsdnConfigEntry_Object = MibTableRow
isdnConfigEntry = _IsdnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 1, 1)
)
isdnConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    isdnConfigEntry.setStatus("current")


class _IsdnLineTermClass_Type(Integer32):
    """Custom type isdnLineTermClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("class1", 1),
          ("class2", 2))
    )


_IsdnLineTermClass_Type.__name__ = "Integer32"
_IsdnLineTermClass_Object = MibTableColumn
isdnLineTermClass = _IsdnLineTermClass_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 1, 1, 1),
    _IsdnLineTermClass_Type()
)
isdnLineTermClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnLineTermClass.setStatus("current")


class _IsdnActivationTimer2_Type(Integer32):
    """Custom type isdnActivationTimer2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t2-100ms", 2),
          ("t2-50ms", 1))
    )


_IsdnActivationTimer2_Type.__name__ = "Integer32"
_IsdnActivationTimer2_Object = MibTableColumn
isdnActivationTimer2 = _IsdnActivationTimer2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 1, 1, 2),
    _IsdnActivationTimer2_Type()
)
isdnActivationTimer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnActivationTimer2.setStatus("current")


class _IsdnLineLoopBack_Type(Integer32):
    """Custom type isdnLineLoopBack based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("loop-back-2bd-external-analog", 14),
          ("loop-back-2bd-idl2-nt", 11),
          ("loop-back-2bd-idl2-tr", 10),
          ("loop-back-2bd-u-interface-nt", 13),
          ("loop-back-2bd-u-interface-tr", 12),
          ("loop-back-b1-idl2-nt", 7),
          ("loop-back-b1-idl2-tr", 6),
          ("loop-back-b1-st-nt", 3),
          ("loop-back-b1-st-tr", 2),
          ("loop-back-b2-idl2-nt", 9),
          ("loop-back-b2-idl2-tr", 8),
          ("loop-back-b2-st-nt", 5),
          ("loop-back-b2-st-tr", 4),
          ("loop-back-none", 1))
    )


_IsdnLineLoopBack_Type.__name__ = "Integer32"
_IsdnLineLoopBack_Object = MibTableColumn
isdnLineLoopBack = _IsdnLineLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 1, 1, 3),
    _IsdnLineLoopBack_Type()
)
isdnLineLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnLineLoopBack.setStatus("current")


class _IsdnLinePower_Type(Integer32):
    """Custom type isdnLinePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("powering", 3),
          ("sealing", 2))
    )


_IsdnLinePower_Type.__name__ = "Integer32"
_IsdnLinePower_Object = MibTableColumn
isdnLinePower = _IsdnLinePower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 1, 1, 4),
    _IsdnLinePower_Type()
)
isdnLinePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnLinePower.setStatus("current")
_IsdnPerfDataCurrentTable_Object = MibTable
isdnPerfDataCurrentTable = _IsdnPerfDataCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2)
)
if mibBuilder.loadTexts:
    isdnPerfDataCurrentTable.setStatus("current")
_IsdnPerfDataCurrentEntry_Object = MibTableRow
isdnPerfDataCurrentEntry = _IsdnPerfDataCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    isdnPerfDataCurrentEntry.setStatus("current")
_IsdnPerfCurBadAmiViolation_Type = PerfCurrentCount
_IsdnPerfCurBadAmiViolation_Object = MibTableColumn
isdnPerfCurBadAmiViolation = _IsdnPerfCurBadAmiViolation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2, 1, 1),
    _IsdnPerfCurBadAmiViolation_Type()
)
isdnPerfCurBadAmiViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerfCurBadAmiViolation.setStatus("current")
_IsdnPerfCurUnbalancedFrame_Type = PerfCurrentCount
_IsdnPerfCurUnbalancedFrame_Object = MibTableColumn
isdnPerfCurUnbalancedFrame = _IsdnPerfCurUnbalancedFrame_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2, 1, 2),
    _IsdnPerfCurUnbalancedFrame_Type()
)
isdnPerfCurUnbalancedFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerfCurUnbalancedFrame.setStatus("current")
_IsdnPerCurErrorSeconds_Type = PerfCurrentCount
_IsdnPerCurErrorSeconds_Object = MibTableColumn
isdnPerCurErrorSeconds = _IsdnPerCurErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2, 1, 3),
    _IsdnPerCurErrorSeconds_Type()
)
isdnPerCurErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerCurErrorSeconds.setStatus("current")
if mibBuilder.loadTexts:
    isdnPerCurErrorSeconds.setUnits("seconds")
_IsdnPerCurFsyncSeconds_Type = PerfCurrentCount
_IsdnPerCurFsyncSeconds_Object = MibTableColumn
isdnPerCurFsyncSeconds = _IsdnPerCurFsyncSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2, 1, 4),
    _IsdnPerCurFsyncSeconds_Type()
)
isdnPerCurFsyncSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerCurFsyncSeconds.setStatus("current")
if mibBuilder.loadTexts:
    isdnPerCurFsyncSeconds.setUnits("seconds")
_IsdnPerfCurTimeElapsed_Type = TimeTicks
_IsdnPerfCurTimeElapsed_Object = MibTableColumn
isdnPerfCurTimeElapsed = _IsdnPerfCurTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 2, 1, 5),
    _IsdnPerfCurTimeElapsed_Type()
)
isdnPerfCurTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerfCurTimeElapsed.setStatus("current")
_IsdnPerfDataPreviousTable_Object = MibTable
isdnPerfDataPreviousTable = _IsdnPerfDataPreviousTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 3)
)
if mibBuilder.loadTexts:
    isdnPerfDataPreviousTable.setStatus("current")
_IsdnPerfDataPreviousEntry_Object = MibTableRow
isdnPerfDataPreviousEntry = _IsdnPerfDataPreviousEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    isdnPerfDataPreviousEntry.setStatus("current")
_IsdnPerfPrevBadAmiViolation_Type = PerfIntervalCount
_IsdnPerfPrevBadAmiViolation_Object = MibTableColumn
isdnPerfPrevBadAmiViolation = _IsdnPerfPrevBadAmiViolation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 3, 1, 1),
    _IsdnPerfPrevBadAmiViolation_Type()
)
isdnPerfPrevBadAmiViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerfPrevBadAmiViolation.setStatus("current")
_IsdnPerfPrevUnbalancedFrame_Type = PerfIntervalCount
_IsdnPerfPrevUnbalancedFrame_Object = MibTableColumn
isdnPerfPrevUnbalancedFrame = _IsdnPerfPrevUnbalancedFrame_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 3, 1, 2),
    _IsdnPerfPrevUnbalancedFrame_Type()
)
isdnPerfPrevUnbalancedFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerfPrevUnbalancedFrame.setStatus("current")
_IsdnPerPrevFsyncSeconds_Type = PerfIntervalCount
_IsdnPerPrevFsyncSeconds_Object = MibTableColumn
isdnPerPrevFsyncSeconds = _IsdnPerPrevFsyncSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 3, 1, 3),
    _IsdnPerPrevFsyncSeconds_Type()
)
isdnPerPrevFsyncSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerPrevFsyncSeconds.setStatus("current")
if mibBuilder.loadTexts:
    isdnPerPrevFsyncSeconds.setUnits("seconds")
_IsdnPerfPrevErrorSeconds_Type = PerfIntervalCount
_IsdnPerfPrevErrorSeconds_Object = MibTableColumn
isdnPerfPrevErrorSeconds = _IsdnPerfPrevErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 3, 1, 4),
    _IsdnPerfPrevErrorSeconds_Type()
)
isdnPerfPrevErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerfPrevErrorSeconds.setStatus("current")
if mibBuilder.loadTexts:
    isdnPerfPrevErrorSeconds.setUnits("seconds")
_IsdnPerfDataTotalTable_Object = MibTable
isdnPerfDataTotalTable = _IsdnPerfDataTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4)
)
if mibBuilder.loadTexts:
    isdnPerfDataTotalTable.setStatus("current")
_IsdnPerfDataTotalEntry_Object = MibTableRow
isdnPerfDataTotalEntry = _IsdnPerfDataTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    isdnPerfDataTotalEntry.setStatus("current")
_IsdnPerfTotalBadAmiViolation_Type = PerfTotalCount
_IsdnPerfTotalBadAmiViolation_Object = MibTableColumn
isdnPerfTotalBadAmiViolation = _IsdnPerfTotalBadAmiViolation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4, 1, 1),
    _IsdnPerfTotalBadAmiViolation_Type()
)
isdnPerfTotalBadAmiViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerfTotalBadAmiViolation.setStatus("current")
_IsdnPerfTotalUnbalancedFrame_Type = PerfTotalCount
_IsdnPerfTotalUnbalancedFrame_Object = MibTableColumn
isdnPerfTotalUnbalancedFrame = _IsdnPerfTotalUnbalancedFrame_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4, 1, 2),
    _IsdnPerfTotalUnbalancedFrame_Type()
)
isdnPerfTotalUnbalancedFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerfTotalUnbalancedFrame.setStatus("current")
_IsdnPerTotalFsyncSeconds_Type = PerfTotalCount
_IsdnPerTotalFsyncSeconds_Object = MibTableColumn
isdnPerTotalFsyncSeconds = _IsdnPerTotalFsyncSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4, 1, 3),
    _IsdnPerTotalFsyncSeconds_Type()
)
isdnPerTotalFsyncSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerTotalFsyncSeconds.setStatus("current")
if mibBuilder.loadTexts:
    isdnPerTotalFsyncSeconds.setUnits("seconds")
_IsdnPerfTotalErrorSeconds_Type = PerfTotalCount
_IsdnPerfTotalErrorSeconds_Object = MibTableColumn
isdnPerfTotalErrorSeconds = _IsdnPerfTotalErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4, 1, 4),
    _IsdnPerfTotalErrorSeconds_Type()
)
isdnPerfTotalErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerfTotalErrorSeconds.setStatus("current")
if mibBuilder.loadTexts:
    isdnPerfTotalErrorSeconds.setUnits("seconds")


class _IsdnPerfTotalTimePeriodsElapsed_Type(Integer32):
    """Custom type isdnPerfTotalTimePeriodsElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_IsdnPerfTotalTimePeriodsElapsed_Type.__name__ = "Integer32"
_IsdnPerfTotalTimePeriodsElapsed_Object = MibTableColumn
isdnPerfTotalTimePeriodsElapsed = _IsdnPerfTotalTimePeriodsElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 4, 1, 5),
    _IsdnPerfTotalTimePeriodsElapsed_Type()
)
isdnPerfTotalTimePeriodsElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPerfTotalTimePeriodsElapsed.setStatus("current")
_IsdnAlarmProfileTable_Object = MibTable
isdnAlarmProfileTable = _IsdnAlarmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 5)
)
if mibBuilder.loadTexts:
    isdnAlarmProfileTable.setStatus("current")
_IsdnAlarmProfileEntry_Object = MibTableRow
isdnAlarmProfileEntry = _IsdnAlarmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 5, 1)
)
if mibBuilder.loadTexts:
    isdnAlarmProfileEntry.setStatus("current")
_IsdnThresholdAmiViolations_Type = Unsigned32
_IsdnThresholdAmiViolations_Object = MibTableColumn
isdnThresholdAmiViolations = _IsdnThresholdAmiViolations_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 5, 1, 1),
    _IsdnThresholdAmiViolations_Type()
)
isdnThresholdAmiViolations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnThresholdAmiViolations.setStatus("current")
_IsdnThresholdUnbalancedFrame_Type = Unsigned32
_IsdnThresholdUnbalancedFrame_Object = MibTableColumn
isdnThresholdUnbalancedFrame = _IsdnThresholdUnbalancedFrame_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 7, 1, 5, 1, 2),
    _IsdnThresholdUnbalancedFrame_Type()
)
isdnThresholdUnbalancedFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnThresholdUnbalancedFrame.setStatus("current")
isdnConfigEntry.registerAugmentions(
    ("ZHONE-ISDN-MIB",
     "isdnPerfDataCurrentEntry")
)
isdnPerfDataCurrentEntry.setIndexNames(*isdnConfigEntry.getIndexNames())
isdnConfigEntry.registerAugmentions(
    ("ZHONE-ISDN-MIB",
     "isdnPerfDataPreviousEntry")
)
isdnPerfDataPreviousEntry.setIndexNames(*isdnConfigEntry.getIndexNames())
isdnConfigEntry.registerAugmentions(
    ("ZHONE-ISDN-MIB",
     "isdnPerfDataTotalEntry")
)
isdnPerfDataTotalEntry.setIndexNames(*isdnConfigEntry.getIndexNames())
isdnConfigEntry.registerAugmentions(
    ("ZHONE-ISDN-MIB",
     "isdnAlarmProfileEntry")
)
isdnAlarmProfileEntry.setIndexNames(*isdnConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

isdnTrapFrameSynchLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 3, 1, 1)
)
isdnTrapFrameSynchLoss.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    isdnTrapFrameSynchLoss.setStatus(
        "current"
    )

isdnTrapFECV = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 3, 1, 2)
)
isdnTrapFECV.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    isdnTrapFECV.setStatus(
        "current"
    )

isdnTrapAmiViolations = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 3, 1, 3)
)
isdnTrapAmiViolations.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    isdnTrapAmiViolations.setStatus(
        "current"
    )

isdnTrapUnbalancedFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 8, 3, 1, 4)
)
if mibBuilder.loadTexts:
    isdnTrapUnbalancedFrame.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-ISDN-MIB",
    **{"zhoneIsdnTrap": zhoneIsdnTrap,
       "isdnMibV2Traps": isdnMibV2Traps,
       "isdnTrapFrameSynchLoss": isdnTrapFrameSynchLoss,
       "isdnTrapFECV": isdnTrapFECV,
       "isdnTrapAmiViolations": isdnTrapAmiViolations,
       "isdnTrapUnbalancedFrame": isdnTrapUnbalancedFrame,
       "zhoneIsdn": zhoneIsdn,
       "zhoneIsdnMib": zhoneIsdnMib,
       "isdnConfigTable": isdnConfigTable,
       "isdnConfigEntry": isdnConfigEntry,
       "isdnLineTermClass": isdnLineTermClass,
       "isdnActivationTimer2": isdnActivationTimer2,
       "isdnLineLoopBack": isdnLineLoopBack,
       "isdnLinePower": isdnLinePower,
       "isdnPerfDataCurrentTable": isdnPerfDataCurrentTable,
       "isdnPerfDataCurrentEntry": isdnPerfDataCurrentEntry,
       "isdnPerfCurBadAmiViolation": isdnPerfCurBadAmiViolation,
       "isdnPerfCurUnbalancedFrame": isdnPerfCurUnbalancedFrame,
       "isdnPerCurErrorSeconds": isdnPerCurErrorSeconds,
       "isdnPerCurFsyncSeconds": isdnPerCurFsyncSeconds,
       "isdnPerfCurTimeElapsed": isdnPerfCurTimeElapsed,
       "isdnPerfDataPreviousTable": isdnPerfDataPreviousTable,
       "isdnPerfDataPreviousEntry": isdnPerfDataPreviousEntry,
       "isdnPerfPrevBadAmiViolation": isdnPerfPrevBadAmiViolation,
       "isdnPerfPrevUnbalancedFrame": isdnPerfPrevUnbalancedFrame,
       "isdnPerPrevFsyncSeconds": isdnPerPrevFsyncSeconds,
       "isdnPerfPrevErrorSeconds": isdnPerfPrevErrorSeconds,
       "isdnPerfDataTotalTable": isdnPerfDataTotalTable,
       "isdnPerfDataTotalEntry": isdnPerfDataTotalEntry,
       "isdnPerfTotalBadAmiViolation": isdnPerfTotalBadAmiViolation,
       "isdnPerfTotalUnbalancedFrame": isdnPerfTotalUnbalancedFrame,
       "isdnPerTotalFsyncSeconds": isdnPerTotalFsyncSeconds,
       "isdnPerfTotalErrorSeconds": isdnPerfTotalErrorSeconds,
       "isdnPerfTotalTimePeriodsElapsed": isdnPerfTotalTimePeriodsElapsed,
       "isdnAlarmProfileTable": isdnAlarmProfileTable,
       "isdnAlarmProfileEntry": isdnAlarmProfileEntry,
       "isdnThresholdAmiViolations": isdnThresholdAmiViolations,
       "isdnThresholdUnbalancedFrame": isdnThresholdUnbalancedFrame}
)
