# SNMP MIB module (SC5520-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SC5520-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:49 2024
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

(dsu,) = mibBuilder.importSymbols(
    "DDS-MIB",
    "dsu")

(SCinstance,) = mibBuilder.importSymbols(
    "GDCMACRO-MIB",
    "SCinstance")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sc5520_ObjectIdentity = ObjectIdentity
sc5520 = _Sc5520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3)
)


class _Sc5520MIBversion_Type(DisplayString):
    """Custom type sc5520MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Sc5520MIBversion_Type.__name__ = "DisplayString"
_Sc5520MIBversion_Object = MibScalar
sc5520MIBversion = _Sc5520MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 1),
    _Sc5520MIBversion_Type()
)
sc5520MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520MIBversion.setStatus("mandatory")
_Sc5520UnitCfgTable_Object = MibTable
sc5520UnitCfgTable = _Sc5520UnitCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2)
)
if mibBuilder.loadTexts:
    sc5520UnitCfgTable.setStatus("mandatory")
_Sc5520UnitCfgEntry_Object = MibTableRow
sc5520UnitCfgEntry = _Sc5520UnitCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1)
)
sc5520UnitCfgEntry.setIndexNames(
    (0, "SC5520-MIB", "sc5520UnitCfgIndex"),
)
if mibBuilder.loadTexts:
    sc5520UnitCfgEntry.setStatus("mandatory")
_Sc5520UnitCfgIndex_Type = SCinstance
_Sc5520UnitCfgIndex_Object = MibTableColumn
sc5520UnitCfgIndex = _Sc5520UnitCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 1),
    _Sc5520UnitCfgIndex_Type()
)
sc5520UnitCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520UnitCfgIndex.setStatus("mandatory")


class _Sc5520Nms510CompatibilityMode_Type(Integer32):
    """Custom type sc5520Nms510CompatibilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Sc5520Nms510CompatibilityMode_Type.__name__ = "Integer32"
_Sc5520Nms510CompatibilityMode_Object = MibTableColumn
sc5520Nms510CompatibilityMode = _Sc5520Nms510CompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 2),
    _Sc5520Nms510CompatibilityMode_Type()
)
sc5520Nms510CompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520Nms510CompatibilityMode.setStatus("mandatory")


class _Sc5520PtToPtSentryTime_Type(Integer32):
    """Custom type sc5520PtToPtSentryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Sc5520PtToPtSentryTime_Type.__name__ = "Integer32"
_Sc5520PtToPtSentryTime_Object = MibTableColumn
sc5520PtToPtSentryTime = _Sc5520PtToPtSentryTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 3),
    _Sc5520PtToPtSentryTime_Type()
)
sc5520PtToPtSentryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520PtToPtSentryTime.setStatus("mandatory")


class _Sc5520AlarmHystTime_Type(Integer32):
    """Custom type sc5520AlarmHystTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Sc5520AlarmHystTime_Type.__name__ = "Integer32"
_Sc5520AlarmHystTime_Object = MibTableColumn
sc5520AlarmHystTime = _Sc5520AlarmHystTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 4),
    _Sc5520AlarmHystTime_Type()
)
sc5520AlarmHystTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520AlarmHystTime.setStatus("mandatory")


class _Sc5520MtpointRmRspIntrvl_Type(Integer32):
    """Custom type sc5520MtpointRmRspIntrvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Sc5520MtpointRmRspIntrvl_Type.__name__ = "Integer32"
_Sc5520MtpointRmRspIntrvl_Object = MibTableColumn
sc5520MtpointRmRspIntrvl = _Sc5520MtpointRmRspIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 5),
    _Sc5520MtpointRmRspIntrvl_Type()
)
sc5520MtpointRmRspIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520MtpointRmRspIntrvl.setStatus("mandatory")


class _Sc5520DtePortType_Type(Integer32):
    """Custom type sc5520DtePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("rs232", 1),
          ("v35", 2))
    )


_Sc5520DtePortType_Type.__name__ = "Integer32"
_Sc5520DtePortType_Object = MibTableColumn
sc5520DtePortType = _Sc5520DtePortType_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 6),
    _Sc5520DtePortType_Type()
)
sc5520DtePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DtePortType.setStatus("mandatory")


class _Sc5520DteCtsDelay_Type(Integer32):
    """Custom type sc5520DteCtsDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cts0mSec", 2),
          ("ctsFixed3Char", 3),
          ("ctsOn", 1))
    )


_Sc5520DteCtsDelay_Type.__name__ = "Integer32"
_Sc5520DteCtsDelay_Object = MibTableColumn
sc5520DteCtsDelay = _Sc5520DteCtsDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 7),
    _Sc5520DteCtsDelay_Type()
)
sc5520DteCtsDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DteCtsDelay.setStatus("mandatory")


class _Sc5520DteCtsDelayExt_Type(Integer32):
    """Custom type sc5520DteCtsDelayExt based on Integer32"""
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
        *(("ext0mSec", 1),
          ("ext30mSec", 2),
          ("ext60mSec", 3),
          ("ext90mSec", 4))
    )


_Sc5520DteCtsDelayExt_Type.__name__ = "Integer32"
_Sc5520DteCtsDelayExt_Object = MibTableColumn
sc5520DteCtsDelayExt = _Sc5520DteCtsDelayExt_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 8),
    _Sc5520DteCtsDelayExt_Type()
)
sc5520DteCtsDelayExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DteCtsDelayExt.setStatus("mandatory")


class _Sc5520BkPlaneFracNum_Type(Integer32):
    """Custom type sc5520BkPlaneFracNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Sc5520BkPlaneFracNum_Type.__name__ = "Integer32"
_Sc5520BkPlaneFracNum_Object = MibTableColumn
sc5520BkPlaneFracNum = _Sc5520BkPlaneFracNum_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 9),
    _Sc5520BkPlaneFracNum_Type()
)
sc5520BkPlaneFracNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520BkPlaneFracNum.setStatus("mandatory")


class _Sc5520BkPlaneFracIfIndex_Type(Integer32):
    """Custom type sc5520BkPlaneFracIfIndex based on Integer32"""
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
        *(("highway1", 2),
          ("highway2", 3),
          ("highway3", 4),
          ("highway4", 5),
          ("none", 1))
    )


_Sc5520BkPlaneFracIfIndex_Type.__name__ = "Integer32"
_Sc5520BkPlaneFracIfIndex_Object = MibTableColumn
sc5520BkPlaneFracIfIndex = _Sc5520BkPlaneFracIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 10),
    _Sc5520BkPlaneFracIfIndex_Type()
)
sc5520BkPlaneFracIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520BkPlaneFracIfIndex.setStatus("mandatory")


class _Sc5520FirmwareLevel_Type(DisplayString):
    """Custom type sc5520FirmwareLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Sc5520FirmwareLevel_Type.__name__ = "DisplayString"
_Sc5520FirmwareLevel_Object = MibTableColumn
sc5520FirmwareLevel = _Sc5520FirmwareLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 11),
    _Sc5520FirmwareLevel_Type()
)
sc5520FirmwareLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520FirmwareLevel.setStatus("mandatory")


class _Sc5520FrontPanelInhibit_Type(Integer32):
    """Custom type sc5520FrontPanelInhibit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("execute", 3),
          ("fpEnabled", 2),
          ("fpInhibited", 1))
    )


_Sc5520FrontPanelInhibit_Type.__name__ = "Integer32"
_Sc5520FrontPanelInhibit_Object = MibTableColumn
sc5520FrontPanelInhibit = _Sc5520FrontPanelInhibit_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 12),
    _Sc5520FrontPanelInhibit_Type()
)
sc5520FrontPanelInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520FrontPanelInhibit.setStatus("mandatory")


class _Sc5520FrontPanelEnable_Type(Integer32):
    """Custom type sc5520FrontPanelEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("execute", 3),
          ("fpEnabled", 2),
          ("fpInhibited", 1))
    )


_Sc5520FrontPanelEnable_Type.__name__ = "Integer32"
_Sc5520FrontPanelEnable_Object = MibTableColumn
sc5520FrontPanelEnable = _Sc5520FrontPanelEnable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 13),
    _Sc5520FrontPanelEnable_Type()
)
sc5520FrontPanelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520FrontPanelEnable.setStatus("mandatory")


class _Sc5520RemLoopAllowed_Type(Integer32):
    """Custom type sc5520RemLoopAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("inhibit", 2))
    )


_Sc5520RemLoopAllowed_Type.__name__ = "Integer32"
_Sc5520RemLoopAllowed_Object = MibTableColumn
sc5520RemLoopAllowed = _Sc5520RemLoopAllowed_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 14),
    _Sc5520RemLoopAllowed_Type()
)
sc5520RemLoopAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520RemLoopAllowed.setStatus("mandatory")


class _Sc5520RemLoopPattern_Type(Integer32):
    """Custom type sc5520RemLoopPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("patternGDC", 3),
          ("patternPn127", 2),
          ("patternV54", 1))
    )


_Sc5520RemLoopPattern_Type.__name__ = "Integer32"
_Sc5520RemLoopPattern_Object = MibTableColumn
sc5520RemLoopPattern = _Sc5520RemLoopPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 15),
    _Sc5520RemLoopPattern_Type()
)
sc5520RemLoopPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520RemLoopPattern.setStatus("mandatory")


class _Sc5520RemLoopTimeout_Type(Integer32):
    """Custom type sc5520RemLoopTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("inhibit", 1))
    )


_Sc5520RemLoopTimeout_Type.__name__ = "Integer32"
_Sc5520RemLoopTimeout_Object = MibTableColumn
sc5520RemLoopTimeout = _Sc5520RemLoopTimeout_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 16),
    _Sc5520RemLoopTimeout_Type()
)
sc5520RemLoopTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520RemLoopTimeout.setStatus("mandatory")


class _Sc5520HdlcInvert_Type(Integer32):
    """Custom type sc5520HdlcInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invert", 2),
          ("normal", 1))
    )


_Sc5520HdlcInvert_Type.__name__ = "Integer32"
_Sc5520HdlcInvert_Object = MibTableColumn
sc5520HdlcInvert = _Sc5520HdlcInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 17),
    _Sc5520HdlcInvert_Type()
)
sc5520HdlcInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520HdlcInvert.setStatus("mandatory")


class _Sc5520EIARemLoop_Type(Integer32):
    """Custom type sc5520EIARemLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Sc5520EIARemLoop_Type.__name__ = "Integer32"
_Sc5520EIARemLoop_Object = MibTableColumn
sc5520EIARemLoop = _Sc5520EIARemLoop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 18),
    _Sc5520EIARemLoop_Type()
)
sc5520EIARemLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520EIARemLoop.setStatus("mandatory")


class _Sc5520EIALineLoop_Type(Integer32):
    """Custom type sc5520EIALineLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Sc5520EIALineLoop_Type.__name__ = "Integer32"
_Sc5520EIALineLoop_Object = MibTableColumn
sc5520EIALineLoop = _Sc5520EIALineLoop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 19),
    _Sc5520EIALineLoop_Type()
)
sc5520EIALineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520EIALineLoop.setStatus("mandatory")


class _Sc5520PiggyBackDetect_Type(Integer32):
    """Custom type sc5520PiggyBackDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("not-installed", 1))
    )


_Sc5520PiggyBackDetect_Type.__name__ = "Integer32"
_Sc5520PiggyBackDetect_Object = MibTableColumn
sc5520PiggyBackDetect = _Sc5520PiggyBackDetect_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 20),
    _Sc5520PiggyBackDetect_Type()
)
sc5520PiggyBackDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520PiggyBackDetect.setStatus("mandatory")


class _Sc5520RateBroadcast_Type(Integer32):
    """Custom type sc5520RateBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("normal", 1))
    )


_Sc5520RateBroadcast_Type.__name__ = "Integer32"
_Sc5520RateBroadcast_Object = MibTableColumn
sc5520RateBroadcast = _Sc5520RateBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 21),
    _Sc5520RateBroadcast_Type()
)
sc5520RateBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520RateBroadcast.setStatus("mandatory")


class _Sc5520CircuitType_Type(Integer32):
    """Custom type sc5520CircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipoint", 2),
          ("point-to-point", 1))
    )


_Sc5520CircuitType_Type.__name__ = "Integer32"
_Sc5520CircuitType_Object = MibTableColumn
sc5520CircuitType = _Sc5520CircuitType_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 22),
    _Sc5520CircuitType_Type()
)
sc5520CircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520CircuitType.setStatus("mandatory")


class _Sc5520WakeUpRemote_Type(DisplayString):
    """Custom type sc5520WakeUpRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Sc5520WakeUpRemote_Type.__name__ = "DisplayString"
_Sc5520WakeUpRemote_Object = MibTableColumn
sc5520WakeUpRemote = _Sc5520WakeUpRemote_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 23),
    _Sc5520WakeUpRemote_Type()
)
sc5520WakeUpRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520WakeUpRemote.setStatus("mandatory")


class _Sc5520ListOfRemotes_Type(OctetString):
    """Custom type sc5520ListOfRemotes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Sc5520ListOfRemotes_Type.__name__ = "OctetString"
_Sc5520ListOfRemotes_Object = MibTableColumn
sc5520ListOfRemotes = _Sc5520ListOfRemotes_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 24),
    _Sc5520ListOfRemotes_Type()
)
sc5520ListOfRemotes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520ListOfRemotes.setStatus("mandatory")


class _Sc5520TelcoLatchingLoop_Type(Integer32):
    """Custom type sc5520TelcoLatchingLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("inhibit", 2))
    )


_Sc5520TelcoLatchingLoop_Type.__name__ = "Integer32"
_Sc5520TelcoLatchingLoop_Object = MibTableColumn
sc5520TelcoLatchingLoop = _Sc5520TelcoLatchingLoop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 25),
    _Sc5520TelcoLatchingLoop_Type()
)
sc5520TelcoLatchingLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520TelcoLatchingLoop.setStatus("mandatory")
_Sc5520MasterTable_Object = MibTable
sc5520MasterTable = _Sc5520MasterTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 3)
)
if mibBuilder.loadTexts:
    sc5520MasterTable.setStatus("mandatory")
_Sc5520MasterTableEntry_Object = MibTableRow
sc5520MasterTableEntry = _Sc5520MasterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1)
)
sc5520MasterTableEntry.setIndexNames(
    (0, "SC5520-MIB", "sc5520MasterIndex"),
)
if mibBuilder.loadTexts:
    sc5520MasterTableEntry.setStatus("mandatory")
_Sc5520MasterIndex_Type = SCinstance
_Sc5520MasterIndex_Object = MibTableColumn
sc5520MasterIndex = _Sc5520MasterIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 1),
    _Sc5520MasterIndex_Type()
)
sc5520MasterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520MasterIndex.setStatus("mandatory")


class _Sc5520AddRemoteAddress_Type(OctetString):
    """Custom type sc5520AddRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_Sc5520AddRemoteAddress_Type.__name__ = "OctetString"
_Sc5520AddRemoteAddress_Object = MibTableColumn
sc5520AddRemoteAddress = _Sc5520AddRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 2),
    _Sc5520AddRemoteAddress_Type()
)
sc5520AddRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520AddRemoteAddress.setStatus("mandatory")


class _Sc5520DelRemoteAddress_Type(OctetString):
    """Custom type sc5520DelRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_Sc5520DelRemoteAddress_Type.__name__ = "OctetString"
_Sc5520DelRemoteAddress_Object = MibTableColumn
sc5520DelRemoteAddress = _Sc5520DelRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 3),
    _Sc5520DelRemoteAddress_Type()
)
sc5520DelRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DelRemoteAddress.setStatus("mandatory")


class _Sc5520EnableRemoteAlarm_Type(Integer32):
    """Custom type sc5520EnableRemoteAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Sc5520EnableRemoteAlarm_Type.__name__ = "Integer32"
_Sc5520EnableRemoteAlarm_Object = MibTableColumn
sc5520EnableRemoteAlarm = _Sc5520EnableRemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 4),
    _Sc5520EnableRemoteAlarm_Type()
)
sc5520EnableRemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520EnableRemoteAlarm.setStatus("mandatory")


class _Sc5520DisableRemoteAlarm_Type(Integer32):
    """Custom type sc5520DisableRemoteAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Sc5520DisableRemoteAlarm_Type.__name__ = "Integer32"
_Sc5520DisableRemoteAlarm_Object = MibTableColumn
sc5520DisableRemoteAlarm = _Sc5520DisableRemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 5),
    _Sc5520DisableRemoteAlarm_Type()
)
sc5520DisableRemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DisableRemoteAlarm.setStatus("mandatory")


class _Sc5520EnableAllRemoteAlarms_Type(Integer32):
    """Custom type sc5520EnableAllRemoteAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("normal", 1))
    )


_Sc5520EnableAllRemoteAlarms_Type.__name__ = "Integer32"
_Sc5520EnableAllRemoteAlarms_Object = MibTableColumn
sc5520EnableAllRemoteAlarms = _Sc5520EnableAllRemoteAlarms_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 6),
    _Sc5520EnableAllRemoteAlarms_Type()
)
sc5520EnableAllRemoteAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520EnableAllRemoteAlarms.setStatus("obsolete")


class _Sc5520DisableAllRemoteAlarms_Type(Integer32):
    """Custom type sc5520DisableAllRemoteAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("normal", 1))
    )


_Sc5520DisableAllRemoteAlarms_Type.__name__ = "Integer32"
_Sc5520DisableAllRemoteAlarms_Object = MibTableColumn
sc5520DisableAllRemoteAlarms = _Sc5520DisableAllRemoteAlarms_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 7),
    _Sc5520DisableAllRemoteAlarms_Type()
)
sc5520DisableAllRemoteAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DisableAllRemoteAlarms.setStatus("obsolete")
_Sc5520AlarmData_ObjectIdentity = ObjectIdentity
sc5520AlarmData = _Sc5520AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4)
)
_Sc5520NoResponseAlm_ObjectIdentity = ObjectIdentity
sc5520NoResponseAlm = _Sc5520NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 1)
)
_Sc5520DiagRxErrAlm_ObjectIdentity = ObjectIdentity
sc5520DiagRxErrAlm = _Sc5520DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 2)
)
_Sc5520PowerUpAlm_ObjectIdentity = ObjectIdentity
sc5520PowerUpAlm = _Sc5520PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 3)
)
_Sc5520EEChkSumErrAlm_ObjectIdentity = ObjectIdentity
sc5520EEChkSumErrAlm = _Sc5520EEChkSumErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 4)
)
_Sc5520FpTestAlm_ObjectIdentity = ObjectIdentity
sc5520FpTestAlm = _Sc5520FpTestAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 5)
)
_Sc5520DSRLossAlm_ObjectIdentity = ObjectIdentity
sc5520DSRLossAlm = _Sc5520DSRLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 7)
)
_Sc5520DTRLossAlm_ObjectIdentity = ObjectIdentity
sc5520DTRLossAlm = _Sc5520DTRLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 8)
)
_Sc5520DTPLossAlm_ObjectIdentity = ObjectIdentity
sc5520DTPLossAlm = _Sc5520DTPLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 9)
)
_Sc5520DCDLossAlm_ObjectIdentity = ObjectIdentity
sc5520DCDLossAlm = _Sc5520DCDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 10)
)
_Sc5520RXDLossAlm_ObjectIdentity = ObjectIdentity
sc5520RXDLossAlm = _Sc5520RXDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 11)
)
_Sc5520TXDLossAlm_ObjectIdentity = ObjectIdentity
sc5520TXDLossAlm = _Sc5520TXDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 12)
)
_Sc5520TmShortedAlm_ObjectIdentity = ObjectIdentity
sc5520TmShortedAlm = _Sc5520TmShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 13)
)
_Sc5520DcdShortedAlm_ObjectIdentity = ObjectIdentity
sc5520DcdShortedAlm = _Sc5520DcdShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 14)
)
_Sc5520DsrShortedAlm_ObjectIdentity = ObjectIdentity
sc5520DsrShortedAlm = _Sc5520DsrShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 15)
)
_Sc5520CtsShortedAlm_ObjectIdentity = ObjectIdentity
sc5520CtsShortedAlm = _Sc5520CtsShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 16)
)
_Sc5520RxdShortedAlm_ObjectIdentity = ObjectIdentity
sc5520RxdShortedAlm = _Sc5520RxdShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 17)
)
_Sc5520RxcShortedAlm_ObjectIdentity = ObjectIdentity
sc5520RxcShortedAlm = _Sc5520RxcShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 18)
)
_Sc5520TxcShortedAlm_ObjectIdentity = ObjectIdentity
sc5520TxcShortedAlm = _Sc5520TxcShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 19)
)
_Sc5520DBURequestForScanAlm_ObjectIdentity = ObjectIdentity
sc5520DBURequestForScanAlm = _Sc5520DBURequestForScanAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 20)
)
_Sc5520DBUOnAlm_ObjectIdentity = ObjectIdentity
sc5520DBUOnAlm = _Sc5520DBUOnAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 21)
)
_Sc5520DBUFailedAlm_ObjectIdentity = ObjectIdentity
sc5520DBUFailedAlm = _Sc5520DBUFailedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 22)
)
_Sc5520CSULoopbackAlm_ObjectIdentity = ObjectIdentity
sc5520CSULoopbackAlm = _Sc5520CSULoopbackAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 23)
)
_Sc5520MaintTable_Object = MibTable
sc5520MaintTable = _Sc5520MaintTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 5)
)
if mibBuilder.loadTexts:
    sc5520MaintTable.setStatus("mandatory")
_Sc5520MaintEntry_Object = MibTableRow
sc5520MaintEntry = _Sc5520MaintEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1)
)
sc5520MaintEntry.setIndexNames(
    (0, "SC5520-MIB", "sc5520MaintIndex"),
)
if mibBuilder.loadTexts:
    sc5520MaintEntry.setStatus("mandatory")
_Sc5520MaintIndex_Type = SCinstance
_Sc5520MaintIndex_Object = MibTableColumn
sc5520MaintIndex = _Sc5520MaintIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 1),
    _Sc5520MaintIndex_Type()
)
sc5520MaintIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520MaintIndex.setStatus("mandatory")


class _Sc5520LedStatus_Type(OctetString):
    """Custom type sc5520LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Sc5520LedStatus_Type.__name__ = "OctetString"
_Sc5520LedStatus_Object = MibTableColumn
sc5520LedStatus = _Sc5520LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 2),
    _Sc5520LedStatus_Type()
)
sc5520LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520LedStatus.setStatus("mandatory")


class _Sc5520SoftReset_Type(Integer32):
    """Custom type sc5520SoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_Sc5520SoftReset_Type.__name__ = "Integer32"
_Sc5520SoftReset_Object = MibTableColumn
sc5520SoftReset = _Sc5520SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 3),
    _Sc5520SoftReset_Type()
)
sc5520SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520SoftReset.setStatus("mandatory")
_Sc5520SysUpTime_Type = TimeTicks
_Sc5520SysUpTime_Object = MibTableColumn
sc5520SysUpTime = _Sc5520SysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 4),
    _Sc5520SysUpTime_Type()
)
sc5520SysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520SysUpTime.setStatus("mandatory")


class _Sc5520PrivateStorage1_Type(DisplayString):
    """Custom type sc5520PrivateStorage1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Sc5520PrivateStorage1_Type.__name__ = "DisplayString"
_Sc5520PrivateStorage1_Object = MibTableColumn
sc5520PrivateStorage1 = _Sc5520PrivateStorage1_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 5),
    _Sc5520PrivateStorage1_Type()
)
sc5520PrivateStorage1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520PrivateStorage1.setStatus("mandatory")


class _Sc5520PrivateStorage2_Type(DisplayString):
    """Custom type sc5520PrivateStorage2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Sc5520PrivateStorage2_Type.__name__ = "DisplayString"
_Sc5520PrivateStorage2_Object = MibTableColumn
sc5520PrivateStorage2 = _Sc5520PrivateStorage2_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 6),
    _Sc5520PrivateStorage2_Type()
)
sc5520PrivateStorage2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520PrivateStorage2.setStatus("mandatory")


class _Sc5520PrivateStorage3_Type(DisplayString):
    """Custom type sc5520PrivateStorage3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Sc5520PrivateStorage3_Type.__name__ = "DisplayString"
_Sc5520PrivateStorage3_Object = MibTableColumn
sc5520PrivateStorage3 = _Sc5520PrivateStorage3_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 7),
    _Sc5520PrivateStorage3_Type()
)
sc5520PrivateStorage3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520PrivateStorage3.setStatus("mandatory")


class _Sc5520BlinkINS_Type(Integer32):
    """Custom type sc5520BlinkINS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blinking", 2),
          ("notBlinking", 1))
    )


_Sc5520BlinkINS_Type.__name__ = "Integer32"
_Sc5520BlinkINS_Object = MibTableColumn
sc5520BlinkINS = _Sc5520BlinkINS_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 8),
    _Sc5520BlinkINS_Type()
)
sc5520BlinkINS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520BlinkINS.setStatus("mandatory")
_Sc5520DiagCfgTable_Object = MibTable
sc5520DiagCfgTable = _Sc5520DiagCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 6)
)
if mibBuilder.loadTexts:
    sc5520DiagCfgTable.setStatus("mandatory")
_Sc5520DiagCfgEntry_Object = MibTableRow
sc5520DiagCfgEntry = _Sc5520DiagCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1)
)
sc5520DiagCfgEntry.setIndexNames(
    (0, "SC5520-MIB", "sc5520DiagCfgIndex"),
)
if mibBuilder.loadTexts:
    sc5520DiagCfgEntry.setStatus("mandatory")
_Sc5520DiagCfgIndex_Type = SCinstance
_Sc5520DiagCfgIndex_Object = MibTableColumn
sc5520DiagCfgIndex = _Sc5520DiagCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 1),
    _Sc5520DiagCfgIndex_Type()
)
sc5520DiagCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520DiagCfgIndex.setStatus("mandatory")


class _Sc5520DiagSendCode_Type(Integer32):
    """Custom type sc5520DiagSendCode based on Integer32"""
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
        *(("sc5520Send15BitPattern", 4),
          ("sc5520Send2047Pattern", 3),
          ("sc5520Send511Pattern", 2),
          ("sc5520SendOtherPattern", 1))
    )


_Sc5520DiagSendCode_Type.__name__ = "Integer32"
_Sc5520DiagSendCode_Object = MibTableColumn
sc5520DiagSendCode = _Sc5520DiagSendCode_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 2),
    _Sc5520DiagSendCode_Type()
)
sc5520DiagSendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DiagSendCode.setStatus("mandatory")


class _Sc5520DiagTestExceptions_Type(Integer32):
    """Custom type sc5520DiagTestExceptions based on Integer32"""
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
        *(("bitsOutOfRange", 3),
          ("blocksAndBitsOutOfRange", 4),
          ("blocksOutOfRange", 2),
          ("noExceptions", 1))
    )


_Sc5520DiagTestExceptions_Type.__name__ = "Integer32"
_Sc5520DiagTestExceptions_Object = MibTableColumn
sc5520DiagTestExceptions = _Sc5520DiagTestExceptions_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 3),
    _Sc5520DiagTestExceptions_Type()
)
sc5520DiagTestExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520DiagTestExceptions.setStatus("mandatory")


class _Sc5520DiagBitErrors_Type(Integer32):
    """Custom type sc5520DiagBitErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Sc5520DiagBitErrors_Type.__name__ = "Integer32"
_Sc5520DiagBitErrors_Object = MibTableColumn
sc5520DiagBitErrors = _Sc5520DiagBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 4),
    _Sc5520DiagBitErrors_Type()
)
sc5520DiagBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520DiagBitErrors.setStatus("mandatory")


class _Sc5520DiagBlockErrors_Type(Integer32):
    """Custom type sc5520DiagBlockErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Sc5520DiagBlockErrors_Type.__name__ = "Integer32"
_Sc5520DiagBlockErrors_Object = MibTableColumn
sc5520DiagBlockErrors = _Sc5520DiagBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 5),
    _Sc5520DiagBlockErrors_Type()
)
sc5520DiagBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520DiagBlockErrors.setStatus("mandatory")


class _Sc5520DiagTestReset_Type(Integer32):
    """Custom type sc5520DiagTestReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTestActive", 1),
          ("resetTest", 3),
          ("testActive", 2))
    )


_Sc5520DiagTestReset_Type.__name__ = "Integer32"
_Sc5520DiagTestReset_Object = MibTableColumn
sc5520DiagTestReset = _Sc5520DiagTestReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 6),
    _Sc5520DiagTestReset_Type()
)
sc5520DiagTestReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DiagTestReset.setStatus("mandatory")


class _Sc5520DiagTimeDelay_Type(Integer32):
    """Custom type sc5520DiagTimeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Sc5520DiagTimeDelay_Type.__name__ = "Integer32"
_Sc5520DiagTimeDelay_Object = MibTableColumn
sc5520DiagTimeDelay = _Sc5520DiagTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 7),
    _Sc5520DiagTimeDelay_Type()
)
sc5520DiagTimeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520DiagTimeDelay.setStatus("mandatory")
_Sc5520ExcDiagTable_Object = MibTable
sc5520ExcDiagTable = _Sc5520ExcDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 7)
)
if mibBuilder.loadTexts:
    sc5520ExcDiagTable.setStatus("mandatory")
_Sc5520ExcDiagEntry_Object = MibTableRow
sc5520ExcDiagEntry = _Sc5520ExcDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1)
)
sc5520ExcDiagEntry.setIndexNames(
    (0, "SC5520-MIB", "sc5520ExcDiagIndex"),
)
if mibBuilder.loadTexts:
    sc5520ExcDiagEntry.setStatus("mandatory")
_Sc5520ExcDiagIndex_Type = SCinstance
_Sc5520ExcDiagIndex_Object = MibTableColumn
sc5520ExcDiagIndex = _Sc5520ExcDiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 1),
    _Sc5520ExcDiagIndex_Type()
)
sc5520ExcDiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520ExcDiagIndex.setStatus("mandatory")


class _Sc5520DiagExtLineloop_Type(Integer32):
    """Custom type sc5520DiagExtLineloop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("lineloopOff", 1),
          ("lineloopOn", 2))
    )


_Sc5520DiagExtLineloop_Type.__name__ = "Integer32"
_Sc5520DiagExtLineloop_Object = MibTableColumn
sc5520DiagExtLineloop = _Sc5520DiagExtLineloop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 2),
    _Sc5520DiagExtLineloop_Type()
)
sc5520DiagExtLineloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DiagExtLineloop.setStatus("mandatory")


class _Sc5520DiagIntLineloop_Type(Integer32):
    """Custom type sc5520DiagIntLineloop based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("blocks1", 3),
          ("blocks10", 4),
          ("blocks100", 5),
          ("blocks1000", 7),
          ("blocks10000", 9),
          ("blocks500", 6),
          ("blocks5000", 8),
          ("blocks50000", 10),
          ("lineloopOff", 1),
          ("lineloopOn", 2))
    )


_Sc5520DiagIntLineloop_Type.__name__ = "Integer32"
_Sc5520DiagIntLineloop_Object = MibTableColumn
sc5520DiagIntLineloop = _Sc5520DiagIntLineloop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 3),
    _Sc5520DiagIntLineloop_Type()
)
sc5520DiagIntLineloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DiagIntLineloop.setStatus("mandatory")


class _Sc5520DiagExtDataloop_Type(Integer32):
    """Custom type sc5520DiagExtDataloop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dataloopOff", 1),
          ("dataloopOn", 2),
          ("external", 3))
    )


_Sc5520DiagExtDataloop_Type.__name__ = "Integer32"
_Sc5520DiagExtDataloop_Object = MibTableColumn
sc5520DiagExtDataloop = _Sc5520DiagExtDataloop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 4),
    _Sc5520DiagExtDataloop_Type()
)
sc5520DiagExtDataloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DiagExtDataloop.setStatus("mandatory")


class _Sc5520DiagTestStatus_Type(Integer32):
    """Custom type sc5520DiagTestStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("endToend", 6),
          ("externalDataloop", 4),
          ("externalLineloop", 2),
          ("internalLineloop", 3),
          ("networkDelay", 9),
          ("noTest", 1),
          ("remoteLoop", 7),
          ("remoteLoopWithSelfTest", 8),
          ("serviceTestCenterLoop", 5))
    )


_Sc5520DiagTestStatus_Type.__name__ = "Integer32"
_Sc5520DiagTestStatus_Object = MibTableColumn
sc5520DiagTestStatus = _Sc5520DiagTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 5),
    _Sc5520DiagTestStatus_Type()
)
sc5520DiagTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520DiagTestStatus.setStatus("mandatory")


class _Sc5520DiagExtRemoteLoop_Type(Integer32):
    """Custom type sc5520DiagExtRemoteLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("remoteloopOff", 1),
          ("remoteloopOn", 2))
    )


_Sc5520DiagExtRemoteLoop_Type.__name__ = "Integer32"
_Sc5520DiagExtRemoteLoop_Object = MibTableColumn
sc5520DiagExtRemoteLoop = _Sc5520DiagExtRemoteLoop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 6),
    _Sc5520DiagExtRemoteLoop_Type()
)
sc5520DiagExtRemoteLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DiagExtRemoteLoop.setStatus("mandatory")


class _Sc5520DiagRemLoopWithSelf_Type(Integer32):
    """Custom type sc5520DiagRemLoopWithSelf based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("blocks1", 3),
          ("blocks10", 4),
          ("blocks100", 5),
          ("blocks1000", 7),
          ("blocks10000", 9),
          ("blocks500", 6),
          ("blocks5000", 8),
          ("blocks50000", 10),
          ("remoteloopOff", 1),
          ("remoteloopOn", 2))
    )


_Sc5520DiagRemLoopWithSelf_Type.__name__ = "Integer32"
_Sc5520DiagRemLoopWithSelf_Object = MibTableColumn
sc5520DiagRemLoopWithSelf = _Sc5520DiagRemLoopWithSelf_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 7),
    _Sc5520DiagRemLoopWithSelf_Type()
)
sc5520DiagRemLoopWithSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DiagRemLoopWithSelf.setStatus("mandatory")
_Sc5520VersionTable_Object = MibTable
sc5520VersionTable = _Sc5520VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 8)
)
if mibBuilder.loadTexts:
    sc5520VersionTable.setStatus("mandatory")
_Sc5520VersionEntry_Object = MibTableRow
sc5520VersionEntry = _Sc5520VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1)
)
sc5520VersionEntry.setIndexNames(
    (0, "SC5520-MIB", "sc5520VersionIndex"),
)
if mibBuilder.loadTexts:
    sc5520VersionEntry.setStatus("mandatory")
_Sc5520VersionIndex_Type = SCinstance
_Sc5520VersionIndex_Object = MibTableColumn
sc5520VersionIndex = _Sc5520VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 1),
    _Sc5520VersionIndex_Type()
)
sc5520VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520VersionIndex.setStatus("mandatory")


class _Sc5520ActiveFirmwareRev_Type(DisplayString):
    """Custom type sc5520ActiveFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sc5520ActiveFirmwareRev_Type.__name__ = "DisplayString"
_Sc5520ActiveFirmwareRev_Object = MibTableColumn
sc5520ActiveFirmwareRev = _Sc5520ActiveFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 2),
    _Sc5520ActiveFirmwareRev_Type()
)
sc5520ActiveFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520ActiveFirmwareRev.setStatus("mandatory")


class _Sc5520StoredFirmwareRev_Type(DisplayString):
    """Custom type sc5520StoredFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sc5520StoredFirmwareRev_Type.__name__ = "DisplayString"
_Sc5520StoredFirmwareRev_Object = MibTableColumn
sc5520StoredFirmwareRev = _Sc5520StoredFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 3),
    _Sc5520StoredFirmwareRev_Type()
)
sc5520StoredFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520StoredFirmwareRev.setStatus("mandatory")


class _Sc5520BootRev_Type(DisplayString):
    """Custom type sc5520BootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Sc5520BootRev_Type.__name__ = "DisplayString"
_Sc5520BootRev_Object = MibTableColumn
sc5520BootRev = _Sc5520BootRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 4),
    _Sc5520BootRev_Type()
)
sc5520BootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520BootRev.setStatus("mandatory")


class _Sc5520StoredFirmwareStatus_Type(Integer32):
    """Custom type sc5520StoredFirmwareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("statBadUnZip", 6),
          ("statBlank", 1),
          ("statCheckSumBad", 4),
          ("statDownLoading", 2),
          ("statDownloadAborted", 7),
          ("statOK", 3),
          ("statUnZipping", 5))
    )


_Sc5520StoredFirmwareStatus_Type.__name__ = "Integer32"
_Sc5520StoredFirmwareStatus_Object = MibTableColumn
sc5520StoredFirmwareStatus = _Sc5520StoredFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 5),
    _Sc5520StoredFirmwareStatus_Type()
)
sc5520StoredFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5520StoredFirmwareStatus.setStatus("mandatory")


class _Sc5520SwitchActiveFirmware_Type(Integer32):
    """Custom type sc5520SwitchActiveFirmware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchActive", 2),
          ("switchNorm", 1))
    )


_Sc5520SwitchActiveFirmware_Type.__name__ = "Integer32"
_Sc5520SwitchActiveFirmware_Object = MibTableColumn
sc5520SwitchActiveFirmware = _Sc5520SwitchActiveFirmware_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 6),
    _Sc5520SwitchActiveFirmware_Type()
)
sc5520SwitchActiveFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520SwitchActiveFirmware.setStatus("mandatory")


class _Sc5520DownloadingMode_Type(Integer32):
    """Custom type sc5520DownloadingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableAll", 1),
          ("enableAndSwitch", 3),
          ("enableAndWait", 2))
    )


_Sc5520DownloadingMode_Type.__name__ = "Integer32"
_Sc5520DownloadingMode_Object = MibTableColumn
sc5520DownloadingMode = _Sc5520DownloadingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 7),
    _Sc5520DownloadingMode_Type()
)
sc5520DownloadingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5520DownloadingMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SC5520-MIB",
    **{"sc5520": sc5520,
       "sc5520MIBversion": sc5520MIBversion,
       "sc5520UnitCfgTable": sc5520UnitCfgTable,
       "sc5520UnitCfgEntry": sc5520UnitCfgEntry,
       "sc5520UnitCfgIndex": sc5520UnitCfgIndex,
       "sc5520Nms510CompatibilityMode": sc5520Nms510CompatibilityMode,
       "sc5520PtToPtSentryTime": sc5520PtToPtSentryTime,
       "sc5520AlarmHystTime": sc5520AlarmHystTime,
       "sc5520MtpointRmRspIntrvl": sc5520MtpointRmRspIntrvl,
       "sc5520DtePortType": sc5520DtePortType,
       "sc5520DteCtsDelay": sc5520DteCtsDelay,
       "sc5520DteCtsDelayExt": sc5520DteCtsDelayExt,
       "sc5520BkPlaneFracNum": sc5520BkPlaneFracNum,
       "sc5520BkPlaneFracIfIndex": sc5520BkPlaneFracIfIndex,
       "sc5520FirmwareLevel": sc5520FirmwareLevel,
       "sc5520FrontPanelInhibit": sc5520FrontPanelInhibit,
       "sc5520FrontPanelEnable": sc5520FrontPanelEnable,
       "sc5520RemLoopAllowed": sc5520RemLoopAllowed,
       "sc5520RemLoopPattern": sc5520RemLoopPattern,
       "sc5520RemLoopTimeout": sc5520RemLoopTimeout,
       "sc5520HdlcInvert": sc5520HdlcInvert,
       "sc5520EIARemLoop": sc5520EIARemLoop,
       "sc5520EIALineLoop": sc5520EIALineLoop,
       "sc5520PiggyBackDetect": sc5520PiggyBackDetect,
       "sc5520RateBroadcast": sc5520RateBroadcast,
       "sc5520CircuitType": sc5520CircuitType,
       "sc5520WakeUpRemote": sc5520WakeUpRemote,
       "sc5520ListOfRemotes": sc5520ListOfRemotes,
       "sc5520TelcoLatchingLoop": sc5520TelcoLatchingLoop,
       "sc5520MasterTable": sc5520MasterTable,
       "sc5520MasterTableEntry": sc5520MasterTableEntry,
       "sc5520MasterIndex": sc5520MasterIndex,
       "sc5520AddRemoteAddress": sc5520AddRemoteAddress,
       "sc5520DelRemoteAddress": sc5520DelRemoteAddress,
       "sc5520EnableRemoteAlarm": sc5520EnableRemoteAlarm,
       "sc5520DisableRemoteAlarm": sc5520DisableRemoteAlarm,
       "sc5520EnableAllRemoteAlarms": sc5520EnableAllRemoteAlarms,
       "sc5520DisableAllRemoteAlarms": sc5520DisableAllRemoteAlarms,
       "sc5520AlarmData": sc5520AlarmData,
       "sc5520NoResponseAlm": sc5520NoResponseAlm,
       "sc5520DiagRxErrAlm": sc5520DiagRxErrAlm,
       "sc5520PowerUpAlm": sc5520PowerUpAlm,
       "sc5520EEChkSumErrAlm": sc5520EEChkSumErrAlm,
       "sc5520FpTestAlm": sc5520FpTestAlm,
       "sc5520DSRLossAlm": sc5520DSRLossAlm,
       "sc5520DTRLossAlm": sc5520DTRLossAlm,
       "sc5520DTPLossAlm": sc5520DTPLossAlm,
       "sc5520DCDLossAlm": sc5520DCDLossAlm,
       "sc5520RXDLossAlm": sc5520RXDLossAlm,
       "sc5520TXDLossAlm": sc5520TXDLossAlm,
       "sc5520TmShortedAlm": sc5520TmShortedAlm,
       "sc5520DcdShortedAlm": sc5520DcdShortedAlm,
       "sc5520DsrShortedAlm": sc5520DsrShortedAlm,
       "sc5520CtsShortedAlm": sc5520CtsShortedAlm,
       "sc5520RxdShortedAlm": sc5520RxdShortedAlm,
       "sc5520RxcShortedAlm": sc5520RxcShortedAlm,
       "sc5520TxcShortedAlm": sc5520TxcShortedAlm,
       "sc5520DBURequestForScanAlm": sc5520DBURequestForScanAlm,
       "sc5520DBUOnAlm": sc5520DBUOnAlm,
       "sc5520DBUFailedAlm": sc5520DBUFailedAlm,
       "sc5520CSULoopbackAlm": sc5520CSULoopbackAlm,
       "sc5520MaintTable": sc5520MaintTable,
       "sc5520MaintEntry": sc5520MaintEntry,
       "sc5520MaintIndex": sc5520MaintIndex,
       "sc5520LedStatus": sc5520LedStatus,
       "sc5520SoftReset": sc5520SoftReset,
       "sc5520SysUpTime": sc5520SysUpTime,
       "sc5520PrivateStorage1": sc5520PrivateStorage1,
       "sc5520PrivateStorage2": sc5520PrivateStorage2,
       "sc5520PrivateStorage3": sc5520PrivateStorage3,
       "sc5520BlinkINS": sc5520BlinkINS,
       "sc5520DiagCfgTable": sc5520DiagCfgTable,
       "sc5520DiagCfgEntry": sc5520DiagCfgEntry,
       "sc5520DiagCfgIndex": sc5520DiagCfgIndex,
       "sc5520DiagSendCode": sc5520DiagSendCode,
       "sc5520DiagTestExceptions": sc5520DiagTestExceptions,
       "sc5520DiagBitErrors": sc5520DiagBitErrors,
       "sc5520DiagBlockErrors": sc5520DiagBlockErrors,
       "sc5520DiagTestReset": sc5520DiagTestReset,
       "sc5520DiagTimeDelay": sc5520DiagTimeDelay,
       "sc5520ExcDiagTable": sc5520ExcDiagTable,
       "sc5520ExcDiagEntry": sc5520ExcDiagEntry,
       "sc5520ExcDiagIndex": sc5520ExcDiagIndex,
       "sc5520DiagExtLineloop": sc5520DiagExtLineloop,
       "sc5520DiagIntLineloop": sc5520DiagIntLineloop,
       "sc5520DiagExtDataloop": sc5520DiagExtDataloop,
       "sc5520DiagTestStatus": sc5520DiagTestStatus,
       "sc5520DiagExtRemoteLoop": sc5520DiagExtRemoteLoop,
       "sc5520DiagRemLoopWithSelf": sc5520DiagRemLoopWithSelf,
       "sc5520VersionTable": sc5520VersionTable,
       "sc5520VersionEntry": sc5520VersionEntry,
       "sc5520VersionIndex": sc5520VersionIndex,
       "sc5520ActiveFirmwareRev": sc5520ActiveFirmwareRev,
       "sc5520StoredFirmwareRev": sc5520StoredFirmwareRev,
       "sc5520BootRev": sc5520BootRev,
       "sc5520StoredFirmwareStatus": sc5520StoredFirmwareStatus,
       "sc5520SwitchActiveFirmware": sc5520SwitchActiveFirmware,
       "sc5520DownloadingMode": sc5520DownloadingMode}
)
