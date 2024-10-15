# SNMP MIB module (DAVID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DAVID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:19 2024
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
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "enterprises",
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

_David_ObjectIdentity = ObjectIdentity
david = _David_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 66)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 66, 1)
)
_DavidExpressNet_ObjectIdentity = ObjectIdentity
davidExpressNet = _DavidExpressNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 66, 1, 3)
)
_ExNetChassis_ObjectIdentity = ObjectIdentity
exNetChassis = _ExNetChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1)
)


class _ExNetChassisType_Type(Integer32):
    """Custom type exNetChassisType based on Integer32"""
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
        *(("m6102", 2),
          ("m6103", 3),
          ("m6310rj", 5),
          ("m6310tel", 4),
          ("m6318sma", 7),
          ("m6318st", 6),
          ("other", 1),
          ("reserved", 8))
    )


_ExNetChassisType_Type.__name__ = "Integer32"
_ExNetChassisType_Object = MibScalar
exNetChassisType = _ExNetChassisType_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 1),
    _ExNetChassisType_Type()
)
exNetChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetChassisType.setStatus("mandatory")


class _ExNetChassisBkplType_Type(Integer32):
    """Custom type exNetChassisBkplType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("expressNet", 2),
          ("other", 1),
          ("reserved", 3))
    )


_ExNetChassisBkplType_Type.__name__ = "Integer32"
_ExNetChassisBkplType_Object = MibScalar
exNetChassisBkplType = _ExNetChassisBkplType_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 2),
    _ExNetChassisBkplType_Type()
)
exNetChassisBkplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetChassisBkplType.setStatus("mandatory")
_ExNetChassisBkplRev_Type = Integer32
_ExNetChassisBkplRev_Object = MibScalar
exNetChassisBkplRev = _ExNetChassisBkplRev_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 3),
    _ExNetChassisBkplRev_Type()
)
exNetChassisBkplRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetChassisBkplRev.setStatus("mandatory")


class _ExNetChassisPsType_Type(Integer32):
    """Custom type exNetChassisPsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("standardXfmr", 2))
    )


_ExNetChassisPsType_Type.__name__ = "Integer32"
_ExNetChassisPsType_Object = MibScalar
exNetChassisPsType = _ExNetChassisPsType_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 4),
    _ExNetChassisPsType_Type()
)
exNetChassisPsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetChassisPsType.setStatus("mandatory")


class _ExNetChassisPsStatus_Type(Integer32):
    """Custom type exNetChassisPsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_ExNetChassisPsStatus_Type.__name__ = "Integer32"
_ExNetChassisPsStatus_Object = MibScalar
exNetChassisPsStatus = _ExNetChassisPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 5),
    _ExNetChassisPsStatus_Type()
)
exNetChassisPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetChassisPsStatus.setStatus("mandatory")
_ExNetSlotConfigTable_Object = MibTable
exNetSlotConfigTable = _ExNetSlotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 7)
)
if mibBuilder.loadTexts:
    exNetSlotConfigTable.setStatus("mandatory")
_ExNetSlotConfigEntry_Object = MibTableRow
exNetSlotConfigEntry = _ExNetSlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 7, 1)
)
exNetSlotConfigEntry.setIndexNames(
    (0, "DAVID-MIB", "exNetSlotIndex"),
)
if mibBuilder.loadTexts:
    exNetSlotConfigEntry.setStatus("mandatory")
_ExNetSlotIndex_Type = Integer32
_ExNetSlotIndex_Object = MibTableColumn
exNetSlotIndex = _ExNetSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 7, 1, 1),
    _ExNetSlotIndex_Type()
)
exNetSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetSlotIndex.setStatus("mandatory")
_ExNetBoardId_Type = Integer32
_ExNetBoardId_Object = MibTableColumn
exNetBoardId = _ExNetBoardId_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 7, 1, 2),
    _ExNetBoardId_Type()
)
exNetBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetBoardId.setStatus("mandatory")


class _ExNetBoardType_Type(Integer32):
    """Custom type exNetBoardType based on Integer32"""
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
        *(("empty", 1),
          ("m6006", 9),
          ("m6201", 4),
          ("m6203", 3),
          ("m6311", 5),
          ("m6312", 6),
          ("m6313sma", 8),
          ("m6313st", 7),
          ("other", 2),
          ("reserved", 10))
    )


_ExNetBoardType_Type.__name__ = "Integer32"
_ExNetBoardType_Object = MibTableColumn
exNetBoardType = _ExNetBoardType_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 7, 1, 3),
    _ExNetBoardType_Type()
)
exNetBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetBoardType.setStatus("mandatory")


class _ExNetBoardDescr_Type(DisplayString):
    """Custom type exNetBoardDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ExNetBoardDescr_Type.__name__ = "DisplayString"
_ExNetBoardDescr_Object = MibTableColumn
exNetBoardDescr = _ExNetBoardDescr_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 7, 1, 4),
    _ExNetBoardDescr_Type()
)
exNetBoardDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetBoardDescr.setStatus("mandatory")
_ExNetBoardNumOfPorts_Type = Integer32
_ExNetBoardNumOfPorts_Object = MibTableColumn
exNetBoardNumOfPorts = _ExNetBoardNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 7, 1, 40),
    _ExNetBoardNumOfPorts_Type()
)
exNetBoardNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetBoardNumOfPorts.setStatus("mandatory")
_ExNetChassisCapacity_Type = Integer32
_ExNetChassisCapacity_Object = MibScalar
exNetChassisCapacity = _ExNetChassisCapacity_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 1, 8),
    _ExNetChassisCapacity_Type()
)
exNetChassisCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetChassisCapacity.setStatus("mandatory")
_ExNetEthernet_ObjectIdentity = ObjectIdentity
exNetEthernet = _ExNetEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2)
)
_ExNetConcentrator_ObjectIdentity = ObjectIdentity
exNetConcentrator = _ExNetConcentrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1)
)


class _ExNetConcRetimingStatus_Type(Integer32):
    """Custom type exNetConcRetimingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ExNetConcRetimingStatus_Type.__name__ = "Integer32"
_ExNetConcRetimingStatus_Object = MibScalar
exNetConcRetimingStatus = _ExNetConcRetimingStatus_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 1),
    _ExNetConcRetimingStatus_Type()
)
exNetConcRetimingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcRetimingStatus.setStatus("mandatory")
_ExNetConcFrmsRxOk_Type = Counter32
_ExNetConcFrmsRxOk_Object = MibScalar
exNetConcFrmsRxOk = _ExNetConcFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 2),
    _ExNetConcFrmsRxOk_Type()
)
exNetConcFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcFrmsRxOk.setStatus("mandatory")
_ExNetConcOctetsRxOk_Type = Counter32
_ExNetConcOctetsRxOk_Object = MibScalar
exNetConcOctetsRxOk = _ExNetConcOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 3),
    _ExNetConcOctetsRxOk_Type()
)
exNetConcOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcOctetsRxOk.setStatus("mandatory")
_ExNetConcMcastFrmsRxOk_Type = Counter32
_ExNetConcMcastFrmsRxOk_Object = MibScalar
exNetConcMcastFrmsRxOk = _ExNetConcMcastFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 4),
    _ExNetConcMcastFrmsRxOk_Type()
)
exNetConcMcastFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcMcastFrmsRxOk.setStatus("mandatory")
_ExNetConcBcastFrmsRxOk_Type = Counter32
_ExNetConcBcastFrmsRxOk_Object = MibScalar
exNetConcBcastFrmsRxOk = _ExNetConcBcastFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 5),
    _ExNetConcBcastFrmsRxOk_Type()
)
exNetConcBcastFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcBcastFrmsRxOk.setStatus("mandatory")
_ExNetConcColls_Type = Counter32
_ExNetConcColls_Object = MibScalar
exNetConcColls = _ExNetConcColls_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 6),
    _ExNetConcColls_Type()
)
exNetConcColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcColls.setStatus("mandatory")
_ExNetConcTooLongErrors_Type = Counter32
_ExNetConcTooLongErrors_Object = MibScalar
exNetConcTooLongErrors = _ExNetConcTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 7),
    _ExNetConcTooLongErrors_Type()
)
exNetConcTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcTooLongErrors.setStatus("mandatory")
_ExNetConcRuntErrors_Type = Counter32
_ExNetConcRuntErrors_Object = MibScalar
exNetConcRuntErrors = _ExNetConcRuntErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 8),
    _ExNetConcRuntErrors_Type()
)
exNetConcRuntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcRuntErrors.setStatus("mandatory")
_ExNetConcFragErrors_Type = Counter32
_ExNetConcFragErrors_Object = MibScalar
exNetConcFragErrors = _ExNetConcFragErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 9),
    _ExNetConcFragErrors_Type()
)
exNetConcFragErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcFragErrors.setStatus("mandatory")
_ExNetConcAlignErrors_Type = Counter32
_ExNetConcAlignErrors_Object = MibScalar
exNetConcAlignErrors = _ExNetConcAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 10),
    _ExNetConcAlignErrors_Type()
)
exNetConcAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcAlignErrors.setStatus("mandatory")
_ExNetConcFcsErrors_Type = Counter32
_ExNetConcFcsErrors_Object = MibScalar
exNetConcFcsErrors = _ExNetConcFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 11),
    _ExNetConcFcsErrors_Type()
)
exNetConcFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcFcsErrors.setStatus("mandatory")
_ExNetConcLateCollErrors_Type = Counter32
_ExNetConcLateCollErrors_Object = MibScalar
exNetConcLateCollErrors = _ExNetConcLateCollErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 12),
    _ExNetConcLateCollErrors_Type()
)
exNetConcLateCollErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcLateCollErrors.setStatus("mandatory")


class _ExNetConcName_Type(DisplayString):
    """Custom type exNetConcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ExNetConcName_Type.__name__ = "DisplayString"
_ExNetConcName_Object = MibScalar
exNetConcName = _ExNetConcName_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 40),
    _ExNetConcName_Type()
)
exNetConcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetConcName.setStatus("mandatory")
_ExNetConcJabbers_Type = Counter32
_ExNetConcJabbers_Object = MibScalar
exNetConcJabbers = _ExNetConcJabbers_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 41),
    _ExNetConcJabbers_Type()
)
exNetConcJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcJabbers.setStatus("mandatory")
_ExNetConcSfdErrors_Type = Counter32
_ExNetConcSfdErrors_Object = MibScalar
exNetConcSfdErrors = _ExNetConcSfdErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 42),
    _ExNetConcSfdErrors_Type()
)
exNetConcSfdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcSfdErrors.setStatus("mandatory")
_ExNetConcAutoPartitions_Type = Counter32
_ExNetConcAutoPartitions_Object = MibScalar
exNetConcAutoPartitions = _ExNetConcAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 43),
    _ExNetConcAutoPartitions_Type()
)
exNetConcAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcAutoPartitions.setStatus("mandatory")
_ExNetConcOosBitRate_Type = Counter32
_ExNetConcOosBitRate_Object = MibScalar
exNetConcOosBitRate = _ExNetConcOosBitRate_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 44),
    _ExNetConcOosBitRate_Type()
)
exNetConcOosBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcOosBitRate.setStatus("mandatory")
_ExNetConcLinkErrors_Type = Counter32
_ExNetConcLinkErrors_Object = MibScalar
exNetConcLinkErrors = _ExNetConcLinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 45),
    _ExNetConcLinkErrors_Type()
)
exNetConcLinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcLinkErrors.setStatus("mandatory")
_ExNetConcFrameErrors_Type = Counter32
_ExNetConcFrameErrors_Object = MibScalar
exNetConcFrameErrors = _ExNetConcFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 46),
    _ExNetConcFrameErrors_Type()
)
exNetConcFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcFrameErrors.setStatus("mandatory")


class _ExNetConcNetUtilization_Type(OctetString):
    """Custom type exNetConcNetUtilization based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ExNetConcNetUtilization_Type.__name__ = "OctetString"
_ExNetConcNetUtilization_Object = MibScalar
exNetConcNetUtilization = _ExNetConcNetUtilization_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 47),
    _ExNetConcNetUtilization_Type()
)
exNetConcNetUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcNetUtilization.setStatus("mandatory")
_ExNetConcResetTimeStamp_Type = Gauge32
_ExNetConcResetTimeStamp_Object = MibScalar
exNetConcResetTimeStamp = _ExNetConcResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 48),
    _ExNetConcResetTimeStamp_Type()
)
exNetConcResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetConcResetTimeStamp.setStatus("mandatory")


class _ExNetConcReset_Type(Integer32):
    """Custom type exNetConcReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2),
          ("resetToDefault", 3))
    )


_ExNetConcReset_Type.__name__ = "Integer32"
_ExNetConcReset_Object = MibScalar
exNetConcReset = _ExNetConcReset_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 1, 49),
    _ExNetConcReset_Type()
)
exNetConcReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetConcReset.setStatus("mandatory")
_ExNetModule_ObjectIdentity = ObjectIdentity
exNetModule = _ExNetModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2)
)
_ExNetModuleTable_Object = MibTable
exNetModuleTable = _ExNetModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    exNetModuleTable.setStatus("mandatory")
_ExNetModuleEntry_Object = MibTableRow
exNetModuleEntry = _ExNetModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1)
)
exNetModuleEntry.setIndexNames(
    (0, "DAVID-MIB", "exNetModuleIndex"),
)
if mibBuilder.loadTexts:
    exNetModuleEntry.setStatus("mandatory")
_ExNetModuleIndex_Type = Integer32
_ExNetModuleIndex_Object = MibTableColumn
exNetModuleIndex = _ExNetModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 1),
    _ExNetModuleIndex_Type()
)
exNetModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleIndex.setStatus("mandatory")


class _ExNetModuleType_Type(Integer32):
    """Custom type exNetModuleType based on Integer32"""
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
        *(("empty", 1),
          ("m6006", 9),
          ("m6201", 4),
          ("m6203", 3),
          ("m6311", 5),
          ("m6312", 6),
          ("m6313sma", 8),
          ("m6313st", 7),
          ("other", 2),
          ("reserved", 10))
    )


_ExNetModuleType_Type.__name__ = "Integer32"
_ExNetModuleType_Object = MibTableColumn
exNetModuleType = _ExNetModuleType_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 2),
    _ExNetModuleType_Type()
)
exNetModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleType.setStatus("mandatory")
_ExNetModuleHwVer_Type = Integer32
_ExNetModuleHwVer_Object = MibTableColumn
exNetModuleHwVer = _ExNetModuleHwVer_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 3),
    _ExNetModuleHwVer_Type()
)
exNetModuleHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleHwVer.setStatus("mandatory")


class _ExNetModuleStatus_Type(Integer32):
    """Custom type exNetModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noComms", 2),
          ("ok", 1),
          ("selfTestFail", 3))
    )


_ExNetModuleStatus_Type.__name__ = "Integer32"
_ExNetModuleStatus_Object = MibTableColumn
exNetModuleStatus = _ExNetModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 4),
    _ExNetModuleStatus_Type()
)
exNetModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleStatus.setStatus("mandatory")


class _ExNetModuleReset_Type(Integer32):
    """Custom type exNetModuleReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2),
          ("resetToDefault", 3))
    )


_ExNetModuleReset_Type.__name__ = "Integer32"
_ExNetModuleReset_Object = MibTableColumn
exNetModuleReset = _ExNetModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 5),
    _ExNetModuleReset_Type()
)
exNetModuleReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetModuleReset.setStatus("mandatory")


class _ExNetModulePartStatus_Type(Integer32):
    """Custom type exNetModulePartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("partition", 2))
    )


_ExNetModulePartStatus_Type.__name__ = "Integer32"
_ExNetModulePartStatus_Object = MibTableColumn
exNetModulePartStatus = _ExNetModulePartStatus_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 6),
    _ExNetModulePartStatus_Type()
)
exNetModulePartStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetModulePartStatus.setStatus("mandatory")


class _ExNetModuleNmCntlStatus_Type(Integer32):
    """Custom type exNetModuleNmCntlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmControl", 2),
          ("notNmControl", 1))
    )


_ExNetModuleNmCntlStatus_Type.__name__ = "Integer32"
_ExNetModuleNmCntlStatus_Object = MibTableColumn
exNetModuleNmCntlStatus = _ExNetModuleNmCntlStatus_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 7),
    _ExNetModuleNmCntlStatus_Type()
)
exNetModuleNmCntlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleNmCntlStatus.setStatus("mandatory")


class _ExNetModulePsStatus_Type(Integer32):
    """Custom type exNetModulePsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_ExNetModulePsStatus_Type.__name__ = "Integer32"
_ExNetModulePsStatus_Object = MibTableColumn
exNetModulePsStatus = _ExNetModulePsStatus_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 8),
    _ExNetModulePsStatus_Type()
)
exNetModulePsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModulePsStatus.setStatus("mandatory")
_ExNetModuleFrmsRxOk_Type = Counter32
_ExNetModuleFrmsRxOk_Object = MibTableColumn
exNetModuleFrmsRxOk = _ExNetModuleFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 9),
    _ExNetModuleFrmsRxOk_Type()
)
exNetModuleFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleFrmsRxOk.setStatus("mandatory")
_ExNetModuleOctetsRxOk_Type = Counter32
_ExNetModuleOctetsRxOk_Object = MibTableColumn
exNetModuleOctetsRxOk = _ExNetModuleOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 10),
    _ExNetModuleOctetsRxOk_Type()
)
exNetModuleOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleOctetsRxOk.setStatus("mandatory")
_ExNetModuleColls_Type = Counter32
_ExNetModuleColls_Object = MibTableColumn
exNetModuleColls = _ExNetModuleColls_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 13),
    _ExNetModuleColls_Type()
)
exNetModuleColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleColls.setStatus("mandatory")
_ExNetModuleTooLongErrors_Type = Counter32
_ExNetModuleTooLongErrors_Object = MibTableColumn
exNetModuleTooLongErrors = _ExNetModuleTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 14),
    _ExNetModuleTooLongErrors_Type()
)
exNetModuleTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleTooLongErrors.setStatus("mandatory")
_ExNetModuleRuntErrors_Type = Counter32
_ExNetModuleRuntErrors_Object = MibTableColumn
exNetModuleRuntErrors = _ExNetModuleRuntErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 15),
    _ExNetModuleRuntErrors_Type()
)
exNetModuleRuntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleRuntErrors.setStatus("mandatory")
_ExNetModuleAlignErrors_Type = Counter32
_ExNetModuleAlignErrors_Object = MibTableColumn
exNetModuleAlignErrors = _ExNetModuleAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 16),
    _ExNetModuleAlignErrors_Type()
)
exNetModuleAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleAlignErrors.setStatus("mandatory")
_ExNetModuleFcsErrors_Type = Counter32
_ExNetModuleFcsErrors_Object = MibTableColumn
exNetModuleFcsErrors = _ExNetModuleFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 17),
    _ExNetModuleFcsErrors_Type()
)
exNetModuleFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleFcsErrors.setStatus("mandatory")
_ExNetModuleLateCollErrors_Type = Counter32
_ExNetModuleLateCollErrors_Object = MibTableColumn
exNetModuleLateCollErrors = _ExNetModuleLateCollErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 18),
    _ExNetModuleLateCollErrors_Type()
)
exNetModuleLateCollErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleLateCollErrors.setStatus("mandatory")


class _ExNetModuleName_Type(DisplayString):
    """Custom type exNetModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ExNetModuleName_Type.__name__ = "DisplayString"
_ExNetModuleName_Object = MibTableColumn
exNetModuleName = _ExNetModuleName_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 40),
    _ExNetModuleName_Type()
)
exNetModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetModuleName.setStatus("mandatory")
_ExNetModuleJabbers_Type = Counter32
_ExNetModuleJabbers_Object = MibTableColumn
exNetModuleJabbers = _ExNetModuleJabbers_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 41),
    _ExNetModuleJabbers_Type()
)
exNetModuleJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleJabbers.setStatus("mandatory")
_ExNetModuleSfdErrors_Type = Counter32
_ExNetModuleSfdErrors_Object = MibTableColumn
exNetModuleSfdErrors = _ExNetModuleSfdErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 42),
    _ExNetModuleSfdErrors_Type()
)
exNetModuleSfdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleSfdErrors.setStatus("mandatory")
_ExNetModuleAutoPartitions_Type = Counter32
_ExNetModuleAutoPartitions_Object = MibTableColumn
exNetModuleAutoPartitions = _ExNetModuleAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 43),
    _ExNetModuleAutoPartitions_Type()
)
exNetModuleAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleAutoPartitions.setStatus("mandatory")
_ExNetModuleOosBitRate_Type = Counter32
_ExNetModuleOosBitRate_Object = MibTableColumn
exNetModuleOosBitRate = _ExNetModuleOosBitRate_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 44),
    _ExNetModuleOosBitRate_Type()
)
exNetModuleOosBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleOosBitRate.setStatus("mandatory")
_ExNetModuleLinkErrors_Type = Counter32
_ExNetModuleLinkErrors_Object = MibTableColumn
exNetModuleLinkErrors = _ExNetModuleLinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 45),
    _ExNetModuleLinkErrors_Type()
)
exNetModuleLinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleLinkErrors.setStatus("mandatory")
_ExNetModuleFrameErrors_Type = Counter32
_ExNetModuleFrameErrors_Object = MibTableColumn
exNetModuleFrameErrors = _ExNetModuleFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 46),
    _ExNetModuleFrameErrors_Type()
)
exNetModuleFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleFrameErrors.setStatus("mandatory")
_ExNetModuleFragErrors_Type = Counter32
_ExNetModuleFragErrors_Object = MibTableColumn
exNetModuleFragErrors = _ExNetModuleFragErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 47),
    _ExNetModuleFragErrors_Type()
)
exNetModuleFragErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleFragErrors.setStatus("mandatory")
_ExNetModulePortConfig_Type = Integer32
_ExNetModulePortConfig_Object = MibTableColumn
exNetModulePortConfig = _ExNetModulePortConfig_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 48),
    _ExNetModulePortConfig_Type()
)
exNetModulePortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetModulePortConfig.setStatus("mandatory")
_ExNetModuleLinkStatConfig_Type = Integer32
_ExNetModuleLinkStatConfig_Object = MibTableColumn
exNetModuleLinkStatConfig = _ExNetModuleLinkStatConfig_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 49),
    _ExNetModuleLinkStatConfig_Type()
)
exNetModuleLinkStatConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetModuleLinkStatConfig.setStatus("mandatory")
_ExNetModuleResetTimeStamp_Type = Gauge32
_ExNetModuleResetTimeStamp_Object = MibTableColumn
exNetModuleResetTimeStamp = _ExNetModuleResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 50),
    _ExNetModuleResetTimeStamp_Type()
)
exNetModuleResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleResetTimeStamp.setStatus("mandatory")
_ExNetModuleLinkStatus_Type = Integer32
_ExNetModuleLinkStatus_Object = MibTableColumn
exNetModuleLinkStatus = _ExNetModuleLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 51),
    _ExNetModuleLinkStatus_Type()
)
exNetModuleLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleLinkStatus.setStatus("mandatory")
_ExNetModuleFwVer_Type = Integer32
_ExNetModuleFwVer_Object = MibTableColumn
exNetModuleFwVer = _ExNetModuleFwVer_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 52),
    _ExNetModuleFwVer_Type()
)
exNetModuleFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleFwVer.setStatus("mandatory")
_ExNetModuleFwFeaturePkg_Type = Integer32
_ExNetModuleFwFeaturePkg_Object = MibTableColumn
exNetModuleFwFeaturePkg = _ExNetModuleFwFeaturePkg_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 53),
    _ExNetModuleFwFeaturePkg_Type()
)
exNetModuleFwFeaturePkg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleFwFeaturePkg.setStatus("mandatory")
_ExNetModuleSelfTestResult_Type = Integer32
_ExNetModuleSelfTestResult_Object = MibTableColumn
exNetModuleSelfTestResult = _ExNetModuleSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 2, 1, 1, 54),
    _ExNetModuleSelfTestResult_Type()
)
exNetModuleSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetModuleSelfTestResult.setStatus("mandatory")
_ExNetPort_ObjectIdentity = ObjectIdentity
exNetPort = _ExNetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3)
)
_ExNetPortTable_Object = MibTable
exNetPortTable = _ExNetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    exNetPortTable.setStatus("mandatory")
_ExNetPortEntry_Object = MibTableRow
exNetPortEntry = _ExNetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1)
)
exNetPortEntry.setIndexNames(
    (0, "DAVID-MIB", "exNetPortModuleIndex"),
    (0, "DAVID-MIB", "exNetPortIndex"),
)
if mibBuilder.loadTexts:
    exNetPortEntry.setStatus("mandatory")
_ExNetPortModuleIndex_Type = Integer32
_ExNetPortModuleIndex_Object = MibTableColumn
exNetPortModuleIndex = _ExNetPortModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 1),
    _ExNetPortModuleIndex_Type()
)
exNetPortModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortModuleIndex.setStatus("mandatory")
_ExNetPortIndex_Type = Integer32
_ExNetPortIndex_Object = MibTableColumn
exNetPortIndex = _ExNetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 2),
    _ExNetPortIndex_Type()
)
exNetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortIndex.setStatus("mandatory")


class _ExNetPortLinkStatus_Type(Integer32):
    """Custom type exNetPortLinkStatus based on Integer32"""
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
          ("on", 2),
          ("other", 3))
    )


_ExNetPortLinkStatus_Type.__name__ = "Integer32"
_ExNetPortLinkStatus_Object = MibTableColumn
exNetPortLinkStatus = _ExNetPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 3),
    _ExNetPortLinkStatus_Type()
)
exNetPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortLinkStatus.setStatus("mandatory")


class _ExNetPortPartStatus_Type(Integer32):
    """Custom type exNetPortPartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoPartition", 3),
          ("enabled", 1),
          ("partition", 2))
    )


_ExNetPortPartStatus_Type.__name__ = "Integer32"
_ExNetPortPartStatus_Object = MibTableColumn
exNetPortPartStatus = _ExNetPortPartStatus_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 4),
    _ExNetPortPartStatus_Type()
)
exNetPortPartStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetPortPartStatus.setStatus("mandatory")


class _ExNetPortJabberStatus_Type(Integer32):
    """Custom type exNetPortJabberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jabbering", 2),
          ("ok", 1))
    )


_ExNetPortJabberStatus_Type.__name__ = "Integer32"
_ExNetPortJabberStatus_Object = MibTableColumn
exNetPortJabberStatus = _ExNetPortJabberStatus_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 5),
    _ExNetPortJabberStatus_Type()
)
exNetPortJabberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortJabberStatus.setStatus("mandatory")
_ExNetPortFrmsRxOk_Type = Counter32
_ExNetPortFrmsRxOk_Object = MibTableColumn
exNetPortFrmsRxOk = _ExNetPortFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 6),
    _ExNetPortFrmsRxOk_Type()
)
exNetPortFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortFrmsRxOk.setStatus("mandatory")
_ExNetPortOctetsRxOk_Type = Counter32
_ExNetPortOctetsRxOk_Object = MibTableColumn
exNetPortOctetsRxOk = _ExNetPortOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 7),
    _ExNetPortOctetsRxOk_Type()
)
exNetPortOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortOctetsRxOk.setStatus("mandatory")
_ExNetPortColls_Type = Counter32
_ExNetPortColls_Object = MibTableColumn
exNetPortColls = _ExNetPortColls_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 10),
    _ExNetPortColls_Type()
)
exNetPortColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortColls.setStatus("mandatory")
_ExNetPortTooLongErrors_Type = Counter32
_ExNetPortTooLongErrors_Object = MibTableColumn
exNetPortTooLongErrors = _ExNetPortTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 11),
    _ExNetPortTooLongErrors_Type()
)
exNetPortTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortTooLongErrors.setStatus("mandatory")
_ExNetPortRuntErrors_Type = Counter32
_ExNetPortRuntErrors_Object = MibTableColumn
exNetPortRuntErrors = _ExNetPortRuntErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 12),
    _ExNetPortRuntErrors_Type()
)
exNetPortRuntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortRuntErrors.setStatus("mandatory")
_ExNetPortAlignErrors_Type = Counter32
_ExNetPortAlignErrors_Object = MibTableColumn
exNetPortAlignErrors = _ExNetPortAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 13),
    _ExNetPortAlignErrors_Type()
)
exNetPortAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortAlignErrors.setStatus("mandatory")
_ExNetPortFcsErrors_Type = Counter32
_ExNetPortFcsErrors_Object = MibTableColumn
exNetPortFcsErrors = _ExNetPortFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 14),
    _ExNetPortFcsErrors_Type()
)
exNetPortFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortFcsErrors.setStatus("mandatory")
_ExNetPortLateCollErrors_Type = Counter32
_ExNetPortLateCollErrors_Object = MibTableColumn
exNetPortLateCollErrors = _ExNetPortLateCollErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 15),
    _ExNetPortLateCollErrors_Type()
)
exNetPortLateCollErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortLateCollErrors.setStatus("mandatory")


class _ExNetPortName_Type(DisplayString):
    """Custom type exNetPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ExNetPortName_Type.__name__ = "DisplayString"
_ExNetPortName_Object = MibTableColumn
exNetPortName = _ExNetPortName_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 40),
    _ExNetPortName_Type()
)
exNetPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetPortName.setStatus("mandatory")
_ExNetPortJabbers_Type = Counter32
_ExNetPortJabbers_Object = MibTableColumn
exNetPortJabbers = _ExNetPortJabbers_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 41),
    _ExNetPortJabbers_Type()
)
exNetPortJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortJabbers.setStatus("mandatory")
_ExNetPortSfdErrors_Type = Counter32
_ExNetPortSfdErrors_Object = MibTableColumn
exNetPortSfdErrors = _ExNetPortSfdErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 42),
    _ExNetPortSfdErrors_Type()
)
exNetPortSfdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortSfdErrors.setStatus("mandatory")
_ExNetPortAutoPartitions_Type = Counter32
_ExNetPortAutoPartitions_Object = MibTableColumn
exNetPortAutoPartitions = _ExNetPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 43),
    _ExNetPortAutoPartitions_Type()
)
exNetPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortAutoPartitions.setStatus("mandatory")
_ExNetPortOosBitRate_Type = Counter32
_ExNetPortOosBitRate_Object = MibTableColumn
exNetPortOosBitRate = _ExNetPortOosBitRate_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 44),
    _ExNetPortOosBitRate_Type()
)
exNetPortOosBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortOosBitRate.setStatus("mandatory")
_ExNetPortLinkErrors_Type = Counter32
_ExNetPortLinkErrors_Object = MibTableColumn
exNetPortLinkErrors = _ExNetPortLinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 45),
    _ExNetPortLinkErrors_Type()
)
exNetPortLinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortLinkErrors.setStatus("mandatory")
_ExNetPortFrameErrors_Type = Counter32
_ExNetPortFrameErrors_Object = MibTableColumn
exNetPortFrameErrors = _ExNetPortFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 46),
    _ExNetPortFrameErrors_Type()
)
exNetPortFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortFrameErrors.setStatus("mandatory")
_ExNetPortFragErrors_Type = Counter32
_ExNetPortFragErrors_Object = MibTableColumn
exNetPortFragErrors = _ExNetPortFragErrors_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 47),
    _ExNetPortFragErrors_Type()
)
exNetPortFragErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortFragErrors.setStatus("mandatory")


class _ExNetPortType_Type(Integer32):
    """Custom type exNetPortType based on Integer32"""
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
        *(("other", 1),
          ("repeater", 2),
          ("tenBasefAsync", 3),
          ("tenBasefSync", 4))
    )


_ExNetPortType_Type.__name__ = "Integer32"
_ExNetPortType_Object = MibTableColumn
exNetPortType = _ExNetPortType_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 48),
    _ExNetPortType_Type()
)
exNetPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortType.setStatus("mandatory")


class _ExNetPortMauType_Type(Integer32):
    """Custom type exNetPortMauType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fOIRL", 4),
          ("other", 1),
          ("tenBase2", 5),
          ("tenBase5", 2),
          ("tenBaseFA", 6),
          ("tenBaseT", 3))
    )


_ExNetPortMauType_Type.__name__ = "Integer32"
_ExNetPortMauType_Object = MibTableColumn
exNetPortMauType = _ExNetPortMauType_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 49),
    _ExNetPortMauType_Type()
)
exNetPortMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetPortMauType.setStatus("mandatory")


class _ExNetPortConfig_Type(Integer32):
    """Custom type exNetPortConfig based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1),
          ("rxDisabled", 5),
          ("txDisabled", 4))
    )


_ExNetPortConfig_Type.__name__ = "Integer32"
_ExNetPortConfig_Object = MibTableColumn
exNetPortConfig = _ExNetPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 50),
    _ExNetPortConfig_Type()
)
exNetPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetPortConfig.setStatus("mandatory")


class _ExNetPortLinkStatConfig_Type(Integer32):
    """Custom type exNetPortLinkStatConfig based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1),
          ("rxDisabled", 5),
          ("txDisabled", 4))
    )


_ExNetPortLinkStatConfig_Type.__name__ = "Integer32"
_ExNetPortLinkStatConfig_Object = MibTableColumn
exNetPortLinkStatConfig = _ExNetPortLinkStatConfig_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 51),
    _ExNetPortLinkStatConfig_Type()
)
exNetPortLinkStatConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetPortLinkStatConfig.setStatus("mandatory")


class _ExNetPortPolarity_Type(Integer32):
    """Custom type exNetPortPolarity based on Integer32"""
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
        *(("negative", 3),
          ("other", 1),
          ("positive", 2),
          ("rxNegative", 5),
          ("txNegative", 4))
    )


_ExNetPortPolarity_Type.__name__ = "Integer32"
_ExNetPortPolarity_Object = MibTableColumn
exNetPortPolarity = _ExNetPortPolarity_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 52),
    _ExNetPortPolarity_Type()
)
exNetPortPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetPortPolarity.setStatus("mandatory")


class _ExNetPortTransmitTest_Type(Integer32):
    """Custom type exNetPortTransmitTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_ExNetPortTransmitTest_Type.__name__ = "Integer32"
_ExNetPortTransmitTest_Object = MibTableColumn
exNetPortTransmitTest = _ExNetPortTransmitTest_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 3, 1, 1, 53),
    _ExNetPortTransmitTest_Type()
)
exNetPortTransmitTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetPortTransmitTest.setStatus("mandatory")
_ExNetMgmt_ObjectIdentity = ObjectIdentity
exNetMgmt = _ExNetMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4)
)


class _ExNetMgmtType_Type(Integer32):
    """Custom type exNetMgmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tbd", 2))
    )


_ExNetMgmtType_Type.__name__ = "Integer32"
_ExNetMgmtType_Object = MibScalar
exNetMgmtType = _ExNetMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 1),
    _ExNetMgmtType_Type()
)
exNetMgmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetMgmtType.setStatus("mandatory")
_ExNetMgmtHwVer_Type = Integer32
_ExNetMgmtHwVer_Object = MibScalar
exNetMgmtHwVer = _ExNetMgmtHwVer_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 2),
    _ExNetMgmtHwVer_Type()
)
exNetMgmtHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetMgmtHwVer.setStatus("mandatory")
_ExNetMgmtFwVer_Type = Integer32
_ExNetMgmtFwVer_Object = MibScalar
exNetMgmtFwVer = _ExNetMgmtFwVer_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 3),
    _ExNetMgmtFwVer_Type()
)
exNetMgmtFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetMgmtFwVer.setStatus("mandatory")
_ExNetMgmtSwMajorVer_Type = Integer32
_ExNetMgmtSwMajorVer_Object = MibScalar
exNetMgmtSwMajorVer = _ExNetMgmtSwMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 4),
    _ExNetMgmtSwMajorVer_Type()
)
exNetMgmtSwMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetMgmtSwMajorVer.setStatus("mandatory")
_ExNetMgmtSwMinorVer_Type = Integer32
_ExNetMgmtSwMinorVer_Object = MibScalar
exNetMgmtSwMinorVer = _ExNetMgmtSwMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 5),
    _ExNetMgmtSwMinorVer_Type()
)
exNetMgmtSwMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetMgmtSwMinorVer.setStatus("mandatory")


class _ExNetMgmtStatus_Type(Integer32):
    """Custom type exNetMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )


_ExNetMgmtStatus_Type.__name__ = "Integer32"
_ExNetMgmtStatus_Object = MibScalar
exNetMgmtStatus = _ExNetMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 6),
    _ExNetMgmtStatus_Type()
)
exNetMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetMgmtStatus.setStatus("mandatory")


class _ExNetMgmtMode_Type(Integer32):
    """Custom type exNetMgmtMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ExNetMgmtMode_Type.__name__ = "Integer32"
_ExNetMgmtMode_Object = MibScalar
exNetMgmtMode = _ExNetMgmtMode_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 7),
    _ExNetMgmtMode_Type()
)
exNetMgmtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetMgmtMode.setStatus("mandatory")


class _ExNetMgmtReset_Type(Integer32):
    """Custom type exNetMgmtReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notReset", 1),
          ("reset", 2))
    )


_ExNetMgmtReset_Type.__name__ = "Integer32"
_ExNetMgmtReset_Object = MibScalar
exNetMgmtReset = _ExNetMgmtReset_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 8),
    _ExNetMgmtReset_Type()
)
exNetMgmtReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetMgmtReset.setStatus("mandatory")


class _ExNetMgmtRestart_Type(Integer32):
    """Custom type exNetMgmtRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRestart", 1),
          ("restart", 2))
    )


_ExNetMgmtRestart_Type.__name__ = "Integer32"
_ExNetMgmtRestart_Object = MibScalar
exNetMgmtRestart = _ExNetMgmtRestart_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 9),
    _ExNetMgmtRestart_Type()
)
exNetMgmtRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetMgmtRestart.setStatus("mandatory")
_ExNetMgmtIpAddr_Type = IpAddress
_ExNetMgmtIpAddr_Object = MibScalar
exNetMgmtIpAddr = _ExNetMgmtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 10),
    _ExNetMgmtIpAddr_Type()
)
exNetMgmtIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetMgmtIpAddr.setStatus("mandatory")
_ExNetMgmtNetMask_Type = IpAddress
_ExNetMgmtNetMask_Object = MibScalar
exNetMgmtNetMask = _ExNetMgmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 11),
    _ExNetMgmtNetMask_Type()
)
exNetMgmtNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetMgmtNetMask.setStatus("mandatory")
_ExNetMgmtDefaultGateway_Type = IpAddress
_ExNetMgmtDefaultGateway_Object = MibScalar
exNetMgmtDefaultGateway = _ExNetMgmtDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 12),
    _ExNetMgmtDefaultGateway_Type()
)
exNetMgmtDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetMgmtDefaultGateway.setStatus("mandatory")
_ExNetMgmtBaudRate_Type = Gauge32
_ExNetMgmtBaudRate_Object = MibScalar
exNetMgmtBaudRate = _ExNetMgmtBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 17),
    _ExNetMgmtBaudRate_Type()
)
exNetMgmtBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exNetMgmtBaudRate.setStatus("mandatory")
_ExNetMgmtLocation_Type = DisplayString
_ExNetMgmtLocation_Object = MibScalar
exNetMgmtLocation = _ExNetMgmtLocation_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 19),
    _ExNetMgmtLocation_Type()
)
exNetMgmtLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetMgmtLocation.setStatus("mandatory")
_ExNetMgmtTrapReceiverTable_Object = MibTable
exNetMgmtTrapReceiverTable = _ExNetMgmtTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 20)
)
if mibBuilder.loadTexts:
    exNetMgmtTrapReceiverTable.setStatus("mandatory")
_ExNetMgmtTrapReceiverEntry_Object = MibTableRow
exNetMgmtTrapReceiverEntry = _ExNetMgmtTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 20, 1)
)
exNetMgmtTrapReceiverEntry.setIndexNames(
    (0, "DAVID-MIB", "exNetMgmtTrapReceiverAddr"),
)
if mibBuilder.loadTexts:
    exNetMgmtTrapReceiverEntry.setStatus("mandatory")


class _ExNetMgmtTrapType_Type(Integer32):
    """Custom type exNetMgmtTrapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_ExNetMgmtTrapType_Type.__name__ = "Integer32"
_ExNetMgmtTrapType_Object = MibTableColumn
exNetMgmtTrapType = _ExNetMgmtTrapType_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 20, 1, 1),
    _ExNetMgmtTrapType_Type()
)
exNetMgmtTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetMgmtTrapType.setStatus("mandatory")
_ExNetMgmtTrapReceiverAddr_Type = IpAddress
_ExNetMgmtTrapReceiverAddr_Object = MibTableColumn
exNetMgmtTrapReceiverAddr = _ExNetMgmtTrapReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 20, 1, 2),
    _ExNetMgmtTrapReceiverAddr_Type()
)
exNetMgmtTrapReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetMgmtTrapReceiverAddr.setStatus("mandatory")


class _ExNetMgmtTrapReceiverComm_Type(OctetString):
    """Custom type exNetMgmtTrapReceiverComm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_ExNetMgmtTrapReceiverComm_Type.__name__ = "OctetString"
_ExNetMgmtTrapReceiverComm_Object = MibTableColumn
exNetMgmtTrapReceiverComm = _ExNetMgmtTrapReceiverComm_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 20, 1, 3),
    _ExNetMgmtTrapReceiverComm_Type()
)
exNetMgmtTrapReceiverComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetMgmtTrapReceiverComm.setStatus("mandatory")


class _ExNetMgmtAuthTrap_Type(Integer32):
    """Custom type exNetMgmtAuthTrap based on Integer32"""
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


_ExNetMgmtAuthTrap_Type.__name__ = "Integer32"
_ExNetMgmtAuthTrap_Object = MibScalar
exNetMgmtAuthTrap = _ExNetMgmtAuthTrap_Object(
    (1, 3, 6, 1, 4, 1, 66, 1, 3, 2, 4, 21),
    _ExNetMgmtAuthTrap_Type()
)
exNetMgmtAuthTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exNetMgmtAuthTrap.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DAVID-MIB",
    **{"david": david,
       "products": products,
       "davidExpressNet": davidExpressNet,
       "exNetChassis": exNetChassis,
       "exNetChassisType": exNetChassisType,
       "exNetChassisBkplType": exNetChassisBkplType,
       "exNetChassisBkplRev": exNetChassisBkplRev,
       "exNetChassisPsType": exNetChassisPsType,
       "exNetChassisPsStatus": exNetChassisPsStatus,
       "exNetSlotConfigTable": exNetSlotConfigTable,
       "exNetSlotConfigEntry": exNetSlotConfigEntry,
       "exNetSlotIndex": exNetSlotIndex,
       "exNetBoardId": exNetBoardId,
       "exNetBoardType": exNetBoardType,
       "exNetBoardDescr": exNetBoardDescr,
       "exNetBoardNumOfPorts": exNetBoardNumOfPorts,
       "exNetChassisCapacity": exNetChassisCapacity,
       "exNetEthernet": exNetEthernet,
       "exNetConcentrator": exNetConcentrator,
       "exNetConcRetimingStatus": exNetConcRetimingStatus,
       "exNetConcFrmsRxOk": exNetConcFrmsRxOk,
       "exNetConcOctetsRxOk": exNetConcOctetsRxOk,
       "exNetConcMcastFrmsRxOk": exNetConcMcastFrmsRxOk,
       "exNetConcBcastFrmsRxOk": exNetConcBcastFrmsRxOk,
       "exNetConcColls": exNetConcColls,
       "exNetConcTooLongErrors": exNetConcTooLongErrors,
       "exNetConcRuntErrors": exNetConcRuntErrors,
       "exNetConcFragErrors": exNetConcFragErrors,
       "exNetConcAlignErrors": exNetConcAlignErrors,
       "exNetConcFcsErrors": exNetConcFcsErrors,
       "exNetConcLateCollErrors": exNetConcLateCollErrors,
       "exNetConcName": exNetConcName,
       "exNetConcJabbers": exNetConcJabbers,
       "exNetConcSfdErrors": exNetConcSfdErrors,
       "exNetConcAutoPartitions": exNetConcAutoPartitions,
       "exNetConcOosBitRate": exNetConcOosBitRate,
       "exNetConcLinkErrors": exNetConcLinkErrors,
       "exNetConcFrameErrors": exNetConcFrameErrors,
       "exNetConcNetUtilization": exNetConcNetUtilization,
       "exNetConcResetTimeStamp": exNetConcResetTimeStamp,
       "exNetConcReset": exNetConcReset,
       "exNetModule": exNetModule,
       "exNetModuleTable": exNetModuleTable,
       "exNetModuleEntry": exNetModuleEntry,
       "exNetModuleIndex": exNetModuleIndex,
       "exNetModuleType": exNetModuleType,
       "exNetModuleHwVer": exNetModuleHwVer,
       "exNetModuleStatus": exNetModuleStatus,
       "exNetModuleReset": exNetModuleReset,
       "exNetModulePartStatus": exNetModulePartStatus,
       "exNetModuleNmCntlStatus": exNetModuleNmCntlStatus,
       "exNetModulePsStatus": exNetModulePsStatus,
       "exNetModuleFrmsRxOk": exNetModuleFrmsRxOk,
       "exNetModuleOctetsRxOk": exNetModuleOctetsRxOk,
       "exNetModuleColls": exNetModuleColls,
       "exNetModuleTooLongErrors": exNetModuleTooLongErrors,
       "exNetModuleRuntErrors": exNetModuleRuntErrors,
       "exNetModuleAlignErrors": exNetModuleAlignErrors,
       "exNetModuleFcsErrors": exNetModuleFcsErrors,
       "exNetModuleLateCollErrors": exNetModuleLateCollErrors,
       "exNetModuleName": exNetModuleName,
       "exNetModuleJabbers": exNetModuleJabbers,
       "exNetModuleSfdErrors": exNetModuleSfdErrors,
       "exNetModuleAutoPartitions": exNetModuleAutoPartitions,
       "exNetModuleOosBitRate": exNetModuleOosBitRate,
       "exNetModuleLinkErrors": exNetModuleLinkErrors,
       "exNetModuleFrameErrors": exNetModuleFrameErrors,
       "exNetModuleFragErrors": exNetModuleFragErrors,
       "exNetModulePortConfig": exNetModulePortConfig,
       "exNetModuleLinkStatConfig": exNetModuleLinkStatConfig,
       "exNetModuleResetTimeStamp": exNetModuleResetTimeStamp,
       "exNetModuleLinkStatus": exNetModuleLinkStatus,
       "exNetModuleFwVer": exNetModuleFwVer,
       "exNetModuleFwFeaturePkg": exNetModuleFwFeaturePkg,
       "exNetModuleSelfTestResult": exNetModuleSelfTestResult,
       "exNetPort": exNetPort,
       "exNetPortTable": exNetPortTable,
       "exNetPortEntry": exNetPortEntry,
       "exNetPortModuleIndex": exNetPortModuleIndex,
       "exNetPortIndex": exNetPortIndex,
       "exNetPortLinkStatus": exNetPortLinkStatus,
       "exNetPortPartStatus": exNetPortPartStatus,
       "exNetPortJabberStatus": exNetPortJabberStatus,
       "exNetPortFrmsRxOk": exNetPortFrmsRxOk,
       "exNetPortOctetsRxOk": exNetPortOctetsRxOk,
       "exNetPortColls": exNetPortColls,
       "exNetPortTooLongErrors": exNetPortTooLongErrors,
       "exNetPortRuntErrors": exNetPortRuntErrors,
       "exNetPortAlignErrors": exNetPortAlignErrors,
       "exNetPortFcsErrors": exNetPortFcsErrors,
       "exNetPortLateCollErrors": exNetPortLateCollErrors,
       "exNetPortName": exNetPortName,
       "exNetPortJabbers": exNetPortJabbers,
       "exNetPortSfdErrors": exNetPortSfdErrors,
       "exNetPortAutoPartitions": exNetPortAutoPartitions,
       "exNetPortOosBitRate": exNetPortOosBitRate,
       "exNetPortLinkErrors": exNetPortLinkErrors,
       "exNetPortFrameErrors": exNetPortFrameErrors,
       "exNetPortFragErrors": exNetPortFragErrors,
       "exNetPortType": exNetPortType,
       "exNetPortMauType": exNetPortMauType,
       "exNetPortConfig": exNetPortConfig,
       "exNetPortLinkStatConfig": exNetPortLinkStatConfig,
       "exNetPortPolarity": exNetPortPolarity,
       "exNetPortTransmitTest": exNetPortTransmitTest,
       "exNetMgmt": exNetMgmt,
       "exNetMgmtType": exNetMgmtType,
       "exNetMgmtHwVer": exNetMgmtHwVer,
       "exNetMgmtFwVer": exNetMgmtFwVer,
       "exNetMgmtSwMajorVer": exNetMgmtSwMajorVer,
       "exNetMgmtSwMinorVer": exNetMgmtSwMinorVer,
       "exNetMgmtStatus": exNetMgmtStatus,
       "exNetMgmtMode": exNetMgmtMode,
       "exNetMgmtReset": exNetMgmtReset,
       "exNetMgmtRestart": exNetMgmtRestart,
       "exNetMgmtIpAddr": exNetMgmtIpAddr,
       "exNetMgmtNetMask": exNetMgmtNetMask,
       "exNetMgmtDefaultGateway": exNetMgmtDefaultGateway,
       "exNetMgmtBaudRate": exNetMgmtBaudRate,
       "exNetMgmtLocation": exNetMgmtLocation,
       "exNetMgmtTrapReceiverTable": exNetMgmtTrapReceiverTable,
       "exNetMgmtTrapReceiverEntry": exNetMgmtTrapReceiverEntry,
       "exNetMgmtTrapType": exNetMgmtTrapType,
       "exNetMgmtTrapReceiverAddr": exNetMgmtTrapReceiverAddr,
       "exNetMgmtTrapReceiverComm": exNetMgmtTrapReceiverComm,
       "exNetMgmtAuthTrap": exNetMgmtAuthTrap}
)
