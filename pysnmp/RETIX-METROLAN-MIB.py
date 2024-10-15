# SNMP MIB module (RETIX-METROLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RETIX-METROLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:58 2024
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

(DisplayString,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "DisplayString")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MetroLanDS3ATM_ObjectIdentity = ObjectIdentity
metroLanDS3ATM = _MetroLanDS3ATM_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37)
)
_AtmBandwithGroup_ObjectIdentity = ObjectIdentity
atmBandwithGroup = _AtmBandwithGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1)
)


class _AtmBWGBandwidth_Type(Integer32):
    """Custom type atmBWGBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtmBWGBandwidth_Type.__name__ = "Integer32"
_AtmBWGBandwidth_Object = MibScalar
atmBWGBandwidth = _AtmBWGBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 1),
    _AtmBWGBandwidth_Type()
)
atmBWGBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmBWGBandwidth.setStatus("mandatory")


class _AtmBWGConfig_Type(Integer32):
    """Custom type atmBWGConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("go", 1)
    )


_AtmBWGConfig_Type.__name__ = "Integer32"
_AtmBWGConfig_Object = MibScalar
atmBWGConfig = _AtmBWGConfig_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2),
    _AtmBWGConfig_Type()
)
atmBWGConfig.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    atmBWGConfig.setStatus("mandatory")
_AtmLogicalPort_ObjectIdentity = ObjectIdentity
atmLogicalPort = _AtmLogicalPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 2)
)


class _AtmRX_VCI_Type(Integer32):
    """Custom type atmRX_VCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35, 1023),
    )


_AtmRX_VCI_Type.__name__ = "Integer32"
_AtmRX_VCI_Object = MibScalar
atmRX_VCI = _AtmRX_VCI_Object(
    (1, 3, 6, 1, 2, 1, 37, 2, 1),
    _AtmRX_VCI_Type()
)
atmRX_VCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRX_VCI.setStatus("mandatory")


class _AtmRX_VPI_Type(Integer32):
    """Custom type atmRX_VPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmRX_VPI_Type.__name__ = "Integer32"
_AtmRX_VPI_Object = MibScalar
atmRX_VPI = _AtmRX_VPI_Object(
    (1, 3, 6, 1, 2, 1, 37, 2, 2),
    _AtmRX_VPI_Type()
)
atmRX_VPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmRX_VPI.setStatus("mandatory")


class _AtmTX_VCI_Type(Integer32):
    """Custom type atmTX_VCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35, 1023),
    )


_AtmTX_VCI_Type.__name__ = "Integer32"
_AtmTX_VCI_Object = MibScalar
atmTX_VCI = _AtmTX_VCI_Object(
    (1, 3, 6, 1, 2, 1, 37, 2, 3),
    _AtmTX_VCI_Type()
)
atmTX_VCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTX_VCI.setStatus("mandatory")


class _AtmTX_VPI_Type(Integer32):
    """Custom type atmTX_VPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmTX_VPI_Type.__name__ = "Integer32"
_AtmTX_VPI_Object = MibScalar
atmTX_VPI = _AtmTX_VPI_Object(
    (1, 3, 6, 1, 2, 1, 37, 2, 4),
    _AtmTX_VPI_Type()
)
atmTX_VPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmTX_VPI.setStatus("mandatory")


class _AtmBWG_Type(Integer32):
    """Custom type atmBWG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtmBWG_Type.__name__ = "Integer32"
_AtmBWG_Object = MibScalar
atmBWG = _AtmBWG_Object(
    (1, 3, 6, 1, 2, 1, 37, 2, 5),
    _AtmBWG_Type()
)
atmBWG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmBWG.setStatus("mandatory")


class _AtmEncaps_Type(Integer32):
    """Custom type atmEncaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              7)
        )
    )
    namedValues = NamedValues(
        *(("llcEncaps", 7),
          ("vcBridged8023", 2))
    )


_AtmEncaps_Type.__name__ = "Integer32"
_AtmEncaps_Object = MibScalar
atmEncaps = _AtmEncaps_Object(
    (1, 3, 6, 1, 2, 1, 37, 2, 6),
    _AtmEncaps_Type()
)
atmEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmEncaps.setStatus("mandatory")


class _AtmPortConfig_Type(Integer32):
    """Custom type atmPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AtmPortConfig_Type.__name__ = "Integer32"
_AtmPortConfig_Object = MibScalar
atmPortConfig = _AtmPortConfig_Object(
    (1, 3, 6, 1, 2, 1, 37, 2, 7),
    _AtmPortConfig_Type()
)
atmPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPortConfig.setStatus("mandatory")
_Ds3FrameDevice_ObjectIdentity = ObjectIdentity
ds3FrameDevice = _Ds3FrameDevice_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 3)
)
_Ds3NoSignalCntr_Type = Integer32
_Ds3NoSignalCntr_Object = MibScalar
ds3NoSignalCntr = _Ds3NoSignalCntr_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 1),
    _Ds3NoSignalCntr_Type()
)
ds3NoSignalCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3NoSignalCntr.setStatus("mandatory")
_Ds3NoDS3FrameCntr_Type = Integer32
_Ds3NoDS3FrameCntr_Object = MibScalar
ds3NoDS3FrameCntr = _Ds3NoDS3FrameCntr_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 2),
    _Ds3NoDS3FrameCntr_Type()
)
ds3NoDS3FrameCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3NoDS3FrameCntr.setStatus("mandatory")
_Ds3AISDetectCntr_Type = Integer32
_Ds3AISDetectCntr_Object = MibScalar
ds3AISDetectCntr = _Ds3AISDetectCntr_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 3),
    _Ds3AISDetectCntr_Type()
)
ds3AISDetectCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AISDetectCntr.setStatus("mandatory")
_Ds3YellowAlarmCntr_Type = Integer32
_Ds3YellowAlarmCntr_Object = MibScalar
ds3YellowAlarmCntr = _Ds3YellowAlarmCntr_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 4),
    _Ds3YellowAlarmCntr_Type()
)
ds3YellowAlarmCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3YellowAlarmCntr.setStatus("mandatory")
_Ds3FErrCntr_Type = Integer32
_Ds3FErrCntr_Object = MibScalar
ds3FErrCntr = _Ds3FErrCntr_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 5),
    _Ds3FErrCntr_Type()
)
ds3FErrCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FErrCntr.setStatus("mandatory")
_Ds3PErrCntr_Type = Integer32
_Ds3PErrCntr_Object = MibScalar
ds3PErrCntr = _Ds3PErrCntr_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 6),
    _Ds3PErrCntr_Type()
)
ds3PErrCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3PErrCntr.setStatus("mandatory")
_Ds3CPErrCntr_Type = Integer32
_Ds3CPErrCntr_Object = MibScalar
ds3CPErrCntr = _Ds3CPErrCntr_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 7),
    _Ds3CPErrCntr_Type()
)
ds3CPErrCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CPErrCntr.setStatus("mandatory")
_Ds3FEBlockErrCntr_Type = Integer32
_Ds3FEBlockErrCntr_Object = MibScalar
ds3FEBlockErrCntr = _Ds3FEBlockErrCntr_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 8),
    _Ds3FEBlockErrCntr_Type()
)
ds3FEBlockErrCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FEBlockErrCntr.setStatus("mandatory")
_Ds3BPVErrCntr_Type = Integer32
_Ds3BPVErrCntr_Object = MibScalar
ds3BPVErrCntr = _Ds3BPVErrCntr_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 9),
    _Ds3BPVErrCntr_Type()
)
ds3BPVErrCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3BPVErrCntr.setStatus("mandatory")
_Ds3ATMOCD_Type = Integer32
_Ds3ATMOCD_Object = MibScalar
ds3ATMOCD = _Ds3ATMOCD_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 10),
    _Ds3ATMOCD_Type()
)
ds3ATMOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3ATMOCD.setStatus("mandatory")
_Ds3FIFOOverflow_Type = Integer32
_Ds3FIFOOverflow_Object = MibScalar
ds3FIFOOverflow = _Ds3FIFOOverflow_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 11),
    _Ds3FIFOOverflow_Type()
)
ds3FIFOOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FIFOOverflow.setStatus("mandatory")
_Ds3RAI_Type = Integer32
_Ds3RAI_Object = MibScalar
ds3RAI = _Ds3RAI_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 12),
    _Ds3RAI_Type()
)
ds3RAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3RAI.setStatus("mandatory")
_Ds3RAICntr_Type = Integer32
_Ds3RAICntr_Object = MibScalar
ds3RAICntr = _Ds3RAICntr_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 13),
    _Ds3RAICntr_Type()
)
ds3RAICntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3RAICntr.setStatus("mandatory")
_Ds3SignalLoss_Type = Integer32
_Ds3SignalLoss_Object = MibScalar
ds3SignalLoss = _Ds3SignalLoss_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 14),
    _Ds3SignalLoss_Type()
)
ds3SignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3SignalLoss.setStatus("mandatory")
_Ds3FrameLoss_Type = Integer32
_Ds3FrameLoss_Object = MibScalar
ds3FrameLoss = _Ds3FrameLoss_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 15),
    _Ds3FrameLoss_Type()
)
ds3FrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FrameLoss.setStatus("mandatory")
_Ds3SyncLoss_Type = Integer32
_Ds3SyncLoss_Object = MibScalar
ds3SyncLoss = _Ds3SyncLoss_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 16),
    _Ds3SyncLoss_Type()
)
ds3SyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3SyncLoss.setStatus("mandatory")
_Ds3YellowAlarm_Type = Integer32
_Ds3YellowAlarm_Object = MibScalar
ds3YellowAlarm = _Ds3YellowAlarm_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 17),
    _Ds3YellowAlarm_Type()
)
ds3YellowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3YellowAlarm.setStatus("mandatory")
_Ds3AISDetect_Type = Integer32
_Ds3AISDetect_Object = MibScalar
ds3AISDetect = _Ds3AISDetect_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 18),
    _Ds3AISDetect_Type()
)
ds3AISDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AISDetect.setStatus("mandatory")


class _Ds3ClearErrorCntr_Type(Integer32):
    """Custom type ds3ClearErrorCntr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("set", 1)
    )


_Ds3ClearErrorCntr_Type.__name__ = "Integer32"
_Ds3ClearErrorCntr_Object = MibScalar
ds3ClearErrorCntr = _Ds3ClearErrorCntr_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 19),
    _Ds3ClearErrorCntr_Type()
)
ds3ClearErrorCntr.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ds3ClearErrorCntr.setStatus("mandatory")
_Ds3GFCInsertion_Type = Integer32
_Ds3GFCInsertion_Object = MibScalar
ds3GFCInsertion = _Ds3GFCInsertion_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 20),
    _Ds3GFCInsertion_Type()
)
ds3GFCInsertion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3GFCInsertion.setStatus("mandatory")
_Ds3BipolarSerialIO_Type = Integer32
_Ds3BipolarSerialIO_Object = MibScalar
ds3BipolarSerialIO = _Ds3BipolarSerialIO_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 21),
    _Ds3BipolarSerialIO_Type()
)
ds3BipolarSerialIO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3BipolarSerialIO.setStatus("mandatory")
_Ds3PayloadScrambling_Type = Integer32
_Ds3PayloadScrambling_Object = MibScalar
ds3PayloadScrambling = _Ds3PayloadScrambling_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 22),
    _Ds3PayloadScrambling_Type()
)
ds3PayloadScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PayloadScrambling.setStatus("mandatory")
_Ds3PLCPOverheadProc_Type = Integer32
_Ds3PLCPOverheadProc_Object = MibScalar
ds3PLCPOverheadProc = _Ds3PLCPOverheadProc_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 23),
    _Ds3PLCPOverheadProc_Type()
)
ds3PLCPOverheadProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PLCPOverheadProc.setStatus("mandatory")
_Ds3FEBEGeneration_Type = Integer32
_Ds3FEBEGeneration_Object = MibScalar
ds3FEBEGeneration = _Ds3FEBEGeneration_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 24),
    _Ds3FEBEGeneration_Type()
)
ds3FEBEGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3FEBEGeneration.setStatus("mandatory")
_Ds3LoopBack_Type = Integer32
_Ds3LoopBack_Object = MibScalar
ds3LoopBack = _Ds3LoopBack_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 25),
    _Ds3LoopBack_Type()
)
ds3LoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3LoopBack.setStatus("mandatory")
_Ds3FEACGenNDetect_Type = Integer32
_Ds3FEACGenNDetect_Object = MibScalar
ds3FEACGenNDetect = _Ds3FEACGenNDetect_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 26),
    _Ds3FEACGenNDetect_Type()
)
ds3FEACGenNDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3FEACGenNDetect.setStatus("mandatory")
_Ds3RcvEQ_Type = Integer32
_Ds3RcvEQ_Object = MibScalar
ds3RcvEQ = _Ds3RcvEQ_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 27),
    _Ds3RcvEQ_Type()
)
ds3RcvEQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3RcvEQ.setStatus("mandatory")
_Ds3XmitLevel_Type = Integer32
_Ds3XmitLevel_Object = MibScalar
ds3XmitLevel = _Ds3XmitLevel_Object(
    (1, 3, 6, 1, 2, 1, 37, 3, 28),
    _Ds3XmitLevel_Type()
)
ds3XmitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3XmitLevel.setStatus("mandatory")
_Retix_ObjectIdentity = ObjectIdentity
retix = _Retix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72)
)
_MetroLanSS_ObjectIdentity = ObjectIdentity
metroLanSS = _MetroLanSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 20)
)
_SsUnitProfile_ObjectIdentity = ObjectIdentity
ssUnitProfile = _SsUnitProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 20, 1)
)
_SsBaseModule_Type = Integer32
_SsBaseModule_Object = MibScalar
ssBaseModule = _SsBaseModule_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 1, 1),
    _SsBaseModule_Type()
)
ssBaseModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssBaseModule.setStatus("mandatory")


class _SsIO1Module_Type(Integer32):
    """Custom type ssIO1Module based on Integer32"""
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
        *(("atm-card-id", 5),
          ("feast-card-id", 3),
          ("pcnet-6-card-id", 2),
          ("stakBus-card-id", 4),
          ("vacant", 1))
    )


_SsIO1Module_Type.__name__ = "Integer32"
_SsIO1Module_Object = MibScalar
ssIO1Module = _SsIO1Module_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 1, 2),
    _SsIO1Module_Type()
)
ssIO1Module.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIO1Module.setStatus("mandatory")


class _SsIO2Module_Type(Integer32):
    """Custom type ssIO2Module based on Integer32"""
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
        *(("atm-card-id", 5),
          ("feast-card-id", 3),
          ("pcnet-6-card-id", 2),
          ("stakBus-card-id", 4),
          ("vacant", 1))
    )


_SsIO2Module_Type.__name__ = "Integer32"
_SsIO2Module_Object = MibScalar
ssIO2Module = _SsIO2Module_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 1, 3),
    _SsIO2Module_Type()
)
ssIO2Module.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIO2Module.setStatus("mandatory")
_SsBaseUnit_ObjectIdentity = ObjectIdentity
ssBaseUnit = _SsBaseUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 20, 2)
)
_SsBaseBootFWVer_Type = Integer32
_SsBaseBootFWVer_Object = MibScalar
ssBaseBootFWVer = _SsBaseBootFWVer_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 2, 1),
    _SsBaseBootFWVer_Type()
)
ssBaseBootFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssBaseBootFWVer.setStatus("mandatory")
_SsBaseSoftVer_Type = Integer32
_SsBaseSoftVer_Object = MibScalar
ssBaseSoftVer = _SsBaseSoftVer_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 2, 2),
    _SsBaseSoftVer_Type()
)
ssBaseSoftVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssBaseSoftVer.setStatus("mandatory")
_SsErrorLog_Type = Integer32
_SsErrorLog_Object = MibScalar
ssErrorLog = _SsErrorLog_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 2, 3),
    _SsErrorLog_Type()
)
ssErrorLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssErrorLog.setStatus("mandatory")
_SsStakBus_ObjectIdentity = ObjectIdentity
ssStakBus = _SsStakBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 20, 3)
)


class _SsStkBusIOPort_Type(Integer32):
    """Custom type ssStkBusIOPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-installed", 3),
          ("on-IO1", 1),
          ("on-IO2", 2))
    )


_SsStkBusIOPort_Type.__name__ = "Integer32"
_SsStkBusIOPort_Object = MibScalar
ssStkBusIOPort = _SsStkBusIOPort_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 3, 1),
    _SsStkBusIOPort_Type()
)
ssStkBusIOPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssStkBusIOPort.setStatus("mandatory")
_SsStkBusSpeed_Type = Integer32
_SsStkBusSpeed_Object = MibScalar
ssStkBusSpeed = _SsStkBusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 3, 2),
    _SsStkBusSpeed_Type()
)
ssStkBusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssStkBusSpeed.setStatus("mandatory")


class _SsStkBusNodeAddr_Type(Integer32):
    """Custom type ssStkBusNodeAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SsStkBusNodeAddr_Type.__name__ = "Integer32"
_SsStkBusNodeAddr_Object = MibScalar
ssStkBusNodeAddr = _SsStkBusNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 3, 3),
    _SsStkBusNodeAddr_Type()
)
ssStkBusNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssStkBusNodeAddr.setStatus("mandatory")


class _SsStkBusRingOp_Type(Integer32):
    """Custom type ssStkBusRingOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 3),
          ("ringNotOperational", 2),
          ("ringOperational", 1))
    )


_SsStkBusRingOp_Type.__name__ = "Integer32"
_SsStkBusRingOp_Object = MibScalar
ssStkBusRingOp = _SsStkBusRingOp_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 3, 4),
    _SsStkBusRingOp_Type()
)
ssStkBusRingOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssStkBusRingOp.setStatus("mandatory")
_SsVirtualLan_ObjectIdentity = ObjectIdentity
ssVirtualLan = _SsVirtualLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 20, 4)
)
_SsVLANEnDisable_Type = Integer32
_SsVLANEnDisable_Object = MibScalar
ssVLANEnDisable = _SsVLANEnDisable_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 4, 1),
    _SsVLANEnDisable_Type()
)
ssVLANEnDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssVLANEnDisable.setStatus("mandatory")
_PortVLANTable_Object = MibTable
portVLANTable = _PortVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 4, 2)
)
if mibBuilder.loadTexts:
    portVLANTable.setStatus("mandatory")
_PortVLANEntry_Object = MibTableRow
portVLANEntry = _PortVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 4, 2, 1)
)
portVLANEntry.setIndexNames(
    (0, "RETIX-METROLAN-MIB", "ssVLANEntryPortID"),
    (0, "RETIX-METROLAN-MIB", "ssVLANEntryVLANID"),
)
if mibBuilder.loadTexts:
    portVLANEntry.setStatus("mandatory")
_SsVLANEntryPortID_Type = Integer32
_SsVLANEntryPortID_Object = MibTableColumn
ssVLANEntryPortID = _SsVLANEntryPortID_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 4, 2, 1, 1),
    _SsVLANEntryPortID_Type()
)
ssVLANEntryPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssVLANEntryPortID.setStatus("mandatory")
_SsVLANEntryVLANID_Type = Integer32
_SsVLANEntryVLANID_Object = MibTableColumn
ssVLANEntryVLANID = _SsVLANEntryVLANID_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 4, 2, 1, 2),
    _SsVLANEntryVLANID_Type()
)
ssVLANEntryVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssVLANEntryVLANID.setStatus("mandatory")


class _SsVLANEntryEdit_Type(Integer32):
    """Custom type ssVLANEntryEdit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable-add", 1))
    )


_SsVLANEntryEdit_Type.__name__ = "Integer32"
_SsVLANEntryEdit_Object = MibTableColumn
ssVLANEntryEdit = _SsVLANEntryEdit_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 4, 2, 1, 3),
    _SsVLANEntryEdit_Type()
)
ssVLANEntryEdit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssVLANEntryEdit.setStatus("mandatory")
_SsSlip_ObjectIdentity = ObjectIdentity
ssSlip = _SsSlip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 20, 5)
)
_SlipEnable_Type = Integer32
_SlipEnable_Object = MibScalar
slipEnable = _SlipEnable_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 5, 1),
    _SlipEnable_Type()
)
slipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipEnable.setStatus("mandatory")
_SlipHostIP_Type = IpAddress
_SlipHostIP_Object = MibScalar
slipHostIP = _SlipHostIP_Object(
    (1, 3, 6, 1, 4, 1, 72, 20, 5, 2),
    _SlipHostIP_Type()
)
slipHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipHostIP.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RETIX-METROLAN-MIB",
    **{"metroLanDS3ATM": metroLanDS3ATM,
       "atmBandwithGroup": atmBandwithGroup,
       "atmBWGBandwidth": atmBWGBandwidth,
       "atmBWGConfig": atmBWGConfig,
       "atmLogicalPort": atmLogicalPort,
       "atmRX-VCI": atmRX_VCI,
       "atmRX-VPI": atmRX_VPI,
       "atmTX-VCI": atmTX_VCI,
       "atmTX-VPI": atmTX_VPI,
       "atmBWG": atmBWG,
       "atmEncaps": atmEncaps,
       "atmPortConfig": atmPortConfig,
       "ds3FrameDevice": ds3FrameDevice,
       "ds3NoSignalCntr": ds3NoSignalCntr,
       "ds3NoDS3FrameCntr": ds3NoDS3FrameCntr,
       "ds3AISDetectCntr": ds3AISDetectCntr,
       "ds3YellowAlarmCntr": ds3YellowAlarmCntr,
       "ds3FErrCntr": ds3FErrCntr,
       "ds3PErrCntr": ds3PErrCntr,
       "ds3CPErrCntr": ds3CPErrCntr,
       "ds3FEBlockErrCntr": ds3FEBlockErrCntr,
       "ds3BPVErrCntr": ds3BPVErrCntr,
       "ds3ATMOCD": ds3ATMOCD,
       "ds3FIFOOverflow": ds3FIFOOverflow,
       "ds3RAI": ds3RAI,
       "ds3RAICntr": ds3RAICntr,
       "ds3SignalLoss": ds3SignalLoss,
       "ds3FrameLoss": ds3FrameLoss,
       "ds3SyncLoss": ds3SyncLoss,
       "ds3YellowAlarm": ds3YellowAlarm,
       "ds3AISDetect": ds3AISDetect,
       "ds3ClearErrorCntr": ds3ClearErrorCntr,
       "ds3GFCInsertion": ds3GFCInsertion,
       "ds3BipolarSerialIO": ds3BipolarSerialIO,
       "ds3PayloadScrambling": ds3PayloadScrambling,
       "ds3PLCPOverheadProc": ds3PLCPOverheadProc,
       "ds3FEBEGeneration": ds3FEBEGeneration,
       "ds3LoopBack": ds3LoopBack,
       "ds3FEACGenNDetect": ds3FEACGenNDetect,
       "ds3RcvEQ": ds3RcvEQ,
       "ds3XmitLevel": ds3XmitLevel,
       "retix": retix,
       "metroLanSS": metroLanSS,
       "ssUnitProfile": ssUnitProfile,
       "ssBaseModule": ssBaseModule,
       "ssIO1Module": ssIO1Module,
       "ssIO2Module": ssIO2Module,
       "ssBaseUnit": ssBaseUnit,
       "ssBaseBootFWVer": ssBaseBootFWVer,
       "ssBaseSoftVer": ssBaseSoftVer,
       "ssErrorLog": ssErrorLog,
       "ssStakBus": ssStakBus,
       "ssStkBusIOPort": ssStkBusIOPort,
       "ssStkBusSpeed": ssStkBusSpeed,
       "ssStkBusNodeAddr": ssStkBusNodeAddr,
       "ssStkBusRingOp": ssStkBusRingOp,
       "ssVirtualLan": ssVirtualLan,
       "ssVLANEnDisable": ssVLANEnDisable,
       "portVLANTable": portVLANTable,
       "portVLANEntry": portVLANEntry,
       "ssVLANEntryPortID": ssVLANEntryPortID,
       "ssVLANEntryVLANID": ssVLANEntryVLANID,
       "ssVLANEntryEdit": ssVLANEntryEdit,
       "ssSlip": ssSlip,
       "slipEnable": slipEnable,
       "slipHostIP": slipHostIP}
)
