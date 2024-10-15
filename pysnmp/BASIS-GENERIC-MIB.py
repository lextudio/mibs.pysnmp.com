# SNMP MIB module (BASIS-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BASIS-GENERIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:41 2024
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

(cardGeneric,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "cardGeneric")

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

_CardInformation_ObjectIdentity = ObjectIdentity
cardInformation = _CardInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1)
)


class _ModuleSlotNumber_Type(Integer32):
    """Custom type moduleSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ModuleSlotNumber_Type.__name__ = "Integer32"
_ModuleSlotNumber_Object = MibScalar
moduleSlotNumber = _ModuleSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 1),
    _ModuleSlotNumber_Type()
)
moduleSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSlotNumber.setStatus("mandatory")


class _FunctionModuleType_Type(Integer32):
    """Custom type functionModuleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              11,
              12,
              20,
              21,
              22,
              23,
              24,
              25,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              40,
              41,
              50,
              51,
              52,
              53,
              60,
              61,
              70,
              71,
              72,
              73,
              80,
              90,
              91,
              100,
              101,
              110,
              111,
              120,
              121,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              140,
              141,
              150,
              151,
              563,
              564,
              787,
              1000,
              1001,
              1002,
              1003,
              2000,
              2001)
        )
    )
    namedValues = NamedValues(
        *(("asc", 2),
          ("atmt-8E1", 111),
          ("atmt-8T1", 110),
          ("ausm-4E1", 41),
          ("ausm-4T1", 40),
          ("ausm-8E1", 51),
          ("ausm-8T1", 50),
          ("ausmB-8E1", 53),
          ("ausmB-8T1", 52),
          ("bnm-155", 12),
          ("bnm-E3", 11),
          ("bnm-T3", 10),
          ("bscsm-2", 100),
          ("bscsm-4", 101),
          ("cesm-4E1", 61),
          ("cesm-4T1", 60),
          ("cesm-8E1", 91),
          ("cesm-8T1", 90),
          ("cesm-E3", 141),
          ("cesm-T3", 140),
          ("cesmB-8T1", 787),
          ("frasm-8T1", 80),
          ("frsm-2ct3", 130),
          ("frsm-2e3", 132),
          ("frsm-2e3b", 135),
          ("frsm-2t3", 131),
          ("frsm-2t3b", 134),
          ("frsm-4E1", 31),
          ("frsm-4E1-C", 33),
          ("frsm-4T1", 30),
          ("frsm-4T1-C", 32),
          ("frsm-8E1", 36),
          ("frsm-8T1", 35),
          ("frsm-hs1", 34),
          ("frsm-hs1b", 37),
          ("frsm-hs2", 133),
          ("frsm-hs2b-12In1", 137),
          ("frsm-hs2b-hssi", 136),
          ("frt-8E1", 121),
          ("frt-8T1", 120),
          ("imatm-E3E1", 71),
          ("imatm-T3T1", 70),
          ("imatmB-8E1", 73),
          ("imatmB-8T1", 72),
          ("other", 1),
          ("pxm1", 1000),
          ("pxm1-2t3e3", 1001),
          ("pxm1-4oc3", 1002),
          ("pxm1-oc12", 1003),
          ("rpm", 2000),
          ("rpm-pr", 2001),
          ("srm-3T3", 21),
          ("srm-3T3-NOBC", 25),
          ("srm-4T1E1", 20),
          ("srme-1OC3", 22),
          ("srme-1STS3", 23),
          ("srme-NOBC", 24),
          ("vism-8E1", 151),
          ("vism-8T1", 150),
          ("vism-pr-8E1", 564),
          ("vism-pr-8T1", 563))
    )


_FunctionModuleType_Type.__name__ = "Integer32"
_FunctionModuleType_Object = MibScalar
functionModuleType = _FunctionModuleType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 2),
    _FunctionModuleType_Type()
)
functionModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    functionModuleType.setStatus("mandatory")


class _FunctionModuleDescription_Type(DisplayString):
    """Custom type functionModuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FunctionModuleDescription_Type.__name__ = "DisplayString"
_FunctionModuleDescription_Object = MibScalar
functionModuleDescription = _FunctionModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 3),
    _FunctionModuleDescription_Type()
)
functionModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    functionModuleDescription.setStatus("mandatory")


class _FunctionModuleSerialNum_Type(DisplayString):
    """Custom type functionModuleSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_FunctionModuleSerialNum_Type.__name__ = "DisplayString"
_FunctionModuleSerialNum_Object = MibScalar
functionModuleSerialNum = _FunctionModuleSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 4),
    _FunctionModuleSerialNum_Type()
)
functionModuleSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    functionModuleSerialNum.setStatus("mandatory")


class _FunctionModuleHWRev_Type(DisplayString):
    """Custom type functionModuleHWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_FunctionModuleHWRev_Type.__name__ = "DisplayString"
_FunctionModuleHWRev_Object = MibScalar
functionModuleHWRev = _FunctionModuleHWRev_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 5),
    _FunctionModuleHWRev_Type()
)
functionModuleHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    functionModuleHWRev.setStatus("mandatory")


class _FunctionModuleFWRev_Type(DisplayString):
    """Custom type functionModuleFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FunctionModuleFWRev_Type.__name__ = "DisplayString"
_FunctionModuleFWRev_Object = MibScalar
functionModuleFWRev = _FunctionModuleFWRev_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 6),
    _FunctionModuleFWRev_Type()
)
functionModuleFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    functionModuleFWRev.setStatus("mandatory")


class _FunctionModuleState_Type(Integer32):
    """Custom type functionModuleState based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("blocked", 11),
          ("boot", 7),
          ("cardinit", 17),
          ("coreCardMisMatch", 10),
          ("failed", 4),
          ("heldInReset", 6),
          ("hold", 13),
          ("mismatch", 8),
          ("nocard", 1),
          ("notResponding", 14),
          ("reserved", 12),
          ("selfTest", 5),
          ("standby", 2),
          ("unknown", 9))
    )


_FunctionModuleState_Type.__name__ = "Integer32"
_FunctionModuleState_Object = MibScalar
functionModuleState = _FunctionModuleState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 7),
    _FunctionModuleState_Type()
)
functionModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    functionModuleState.setStatus("mandatory")


class _FunctionModuleResetReason_Type(Integer32):
    """Custom type functionModuleResetReason based on Integer32"""
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
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("clrAllCnf", 5),
          ("driverError", 18),
          ("missingTask", 6),
          ("parityError", 2),
          ("powerUp", 1),
          ("pxmLowVoltage", 7),
          ("resetByEventLogTask", 8),
          ("resetFromPXM", 11),
          ("resetFromShell", 9),
          ("resetSys", 12),
          ("resourceOverflow", 4),
          ("restoreAllCnf", 17),
          ("sCacheError", 14),
          ("swError", 15),
          ("switchCC", 13),
          ("unknown", 10),
          ("upgrade", 16),
          ("watchDog", 3))
    )


_FunctionModuleResetReason_Type.__name__ = "Integer32"
_FunctionModuleResetReason_Object = MibScalar
functionModuleResetReason = _FunctionModuleResetReason_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 8),
    _FunctionModuleResetReason_Type()
)
functionModuleResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    functionModuleResetReason.setStatus("mandatory")


class _LineModuleType_Type(Integer32):
    """Custom type lineModuleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              32,
              33,
              34,
              35,
              48,
              49,
              50,
              51,
              60,
              61,
              62,
              63,
              70,
              71,
              80,
              81,
              500,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              511,
              512,
              513,
              514,
              515,
              1006,
              1050,
              1051,
              1052)
        )
    )
    namedValues = NamedValues(
        *(("lm-12In1-8s", 63),
          ("lm-155-SMF", 34),
          ("lm-155-UTP", 35),
          ("lm-3T3-B", 51),
          ("lm-ASC", 2),
          ("lm-BNC-2E3", 81),
          ("lm-BNC-2T3", 80),
          ("lm-BNC-4E1", 18),
          ("lm-BNC-4E1-R", 21),
          ("lm-BSCSM-2", 70),
          ("lm-BSCSM-4", 71),
          ("lm-DB15-4E1", 17),
          ("lm-DB15-4E1-R", 20),
          ("lm-DB15-4T1", 16),
          ("lm-DB15-4T1-R", 19),
          ("lm-HS1-3HSSI", 61),
          ("lm-HS1-4V35", 62),
          ("lm-HS1-4X21", 60),
          ("lm-RJ48-8E1", 23),
          ("lm-RJ48-8E1-R", 49),
          ("lm-RJ48-8T1", 22),
          ("lm-RJ48-8T1-R", 48),
          ("lm-RJ48-E3E1", 26),
          ("lm-RJ48-E3T1", 29),
          ("lm-RJ48-T3E1", 27),
          ("lm-RJ48-T3T1", 25),
          ("lm-SMB-8E1", 24),
          ("lm-SMB-8E1-R", 50),
          ("lm-SMB-E3E1", 28),
          ("lm-SMB-T3E1", 30),
          ("lm-T3E3-B", 33),
          ("lm-T3E3-D", 32),
          ("lm-srme-1OC3-smb", 1052),
          ("lm-srme-1OC3-smir", 1051),
          ("lm-srme-1OC3-smlr", 1050),
          ("mmf-4-155", 505),
          ("mmf-fddi", 513),
          ("mmf-fe", 512),
          ("other", 1),
          ("pxm-ui", 500),
          ("pxm-ui-s3", 1006),
          ("rj45-4e", 515),
          ("rj45-fe", 511),
          ("smf-fddi", 514),
          ("smfir-1-622", 501),
          ("smfir-4-155", 506),
          ("smfir15-1-622", 503),
          ("smflr-1-622", 502),
          ("smflr-4-155", 507),
          ("smflr15-1-622", 504))
    )


_LineModuleType_Type.__name__ = "Integer32"
_LineModuleType_Object = MibScalar
lineModuleType = _LineModuleType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 9),
    _LineModuleType_Type()
)
lineModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleType.setStatus("mandatory")


class _LineModuleDescription_Type(DisplayString):
    """Custom type lineModuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LineModuleDescription_Type.__name__ = "DisplayString"
_LineModuleDescription_Object = MibScalar
lineModuleDescription = _LineModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 10),
    _LineModuleDescription_Type()
)
lineModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleDescription.setStatus("mandatory")


class _LineModuleSerialNum_Type(DisplayString):
    """Custom type lineModuleSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_LineModuleSerialNum_Type.__name__ = "DisplayString"
_LineModuleSerialNum_Object = MibScalar
lineModuleSerialNum = _LineModuleSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 11),
    _LineModuleSerialNum_Type()
)
lineModuleSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleSerialNum.setStatus("mandatory")


class _LineModuleHWRev_Type(DisplayString):
    """Custom type lineModuleHWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_LineModuleHWRev_Type.__name__ = "DisplayString"
_LineModuleHWRev_Object = MibScalar
lineModuleHWRev = _LineModuleHWRev_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 12),
    _LineModuleHWRev_Type()
)
lineModuleHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleHWRev.setStatus("mandatory")


class _LineModuleFWRev_Type(DisplayString):
    """Custom type lineModuleFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LineModuleFWRev_Type.__name__ = "DisplayString"
_LineModuleFWRev_Object = MibScalar
lineModuleFWRev = _LineModuleFWRev_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 13),
    _LineModuleFWRev_Type()
)
lineModuleFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleFWRev.setStatus("mandatory")


class _LineModuleState_Type(Integer32):
    """Custom type lineModuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("notPresent", 1),
          ("present", 2))
    )


_LineModuleState_Type.__name__ = "Integer32"
_LineModuleState_Object = MibScalar
lineModuleState = _LineModuleState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 14),
    _LineModuleState_Type()
)
lineModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineModuleState.setStatus("mandatory")


class _ModuleTrapAlarmSeverity_Type(Integer32):
    """Custom type moduleTrapAlarmSeverity based on Integer32"""
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
        *(("critical", 4),
          ("dontCare", 3),
          ("error", 5),
          ("info", 8),
          ("major", 2),
          ("minor", 1),
          ("notice", 7),
          ("warning", 6))
    )


_ModuleTrapAlarmSeverity_Type.__name__ = "Integer32"
_ModuleTrapAlarmSeverity_Object = MibScalar
moduleTrapAlarmSeverity = _ModuleTrapAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 15),
    _ModuleTrapAlarmSeverity_Type()
)
moduleTrapAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTrapAlarmSeverity.setStatus("mandatory")


class _MibVersionNumber_Type(Integer32):
    """Custom type mibVersionNumber based on Integer32"""
    defaultValue = 2


_MibVersionNumber_Object = MibScalar
mibVersionNumber = _MibVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 16),
    _MibVersionNumber_Type()
)
mibVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibVersionNumber.setStatus("mandatory")


class _ConfigChangeTypeBitMap_Type(Integer32):
    """Custom type configChangeTypeBitMap based on Integer32"""
    defaultValue = 0


_ConfigChangeTypeBitMap_Object = MibScalar
configChangeTypeBitMap = _ConfigChangeTypeBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 17),
    _ConfigChangeTypeBitMap_Type()
)
configChangeTypeBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configChangeTypeBitMap.setStatus("mandatory")


class _ConfigChangeObjectIndex_Type(Integer32):
    """Custom type configChangeObjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ConfigChangeObjectIndex_Type.__name__ = "Integer32"
_ConfigChangeObjectIndex_Object = MibScalar
configChangeObjectIndex = _ConfigChangeObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 18),
    _ConfigChangeObjectIndex_Type()
)
configChangeObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configChangeObjectIndex.setStatus("mandatory")


class _ConfigChangeStatus_Type(Integer32):
    """Custom type configChangeStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ConfigChangeStatus_Type.__name__ = "Integer32"
_ConfigChangeStatus_Object = MibScalar
configChangeStatus = _ConfigChangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 19),
    _ConfigChangeStatus_Type()
)
configChangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configChangeStatus.setStatus("mandatory")


class _CardIntegratedAlarmBitMap_Type(Integer32):
    """Custom type cardIntegratedAlarmBitMap based on Integer32"""
    defaultValue = 0


_CardIntegratedAlarmBitMap_Object = MibScalar
cardIntegratedAlarmBitMap = _CardIntegratedAlarmBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 20),
    _CardIntegratedAlarmBitMap_Type()
)
cardIntegratedAlarmBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIntegratedAlarmBitMap.setStatus("mandatory")


class _CleiCode_Type(DisplayString):
    """Custom type cleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CleiCode_Type.__name__ = "DisplayString"
_CleiCode_Object = MibScalar
cleiCode = _CleiCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 21),
    _CleiCode_Type()
)
cleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cleiCode.setStatus("mandatory")
_MacAddress_Type = DisplayString
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 22),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("mandatory")
_MacAddrBlkSize_Type = Integer32
_MacAddrBlkSize_Object = MibScalar
macAddrBlkSize = _MacAddrBlkSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 23),
    _MacAddrBlkSize_Type()
)
macAddrBlkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddrBlkSize.setStatus("mandatory")


class _FinalTestTechnician_Type(DisplayString):
    """Custom type finalTestTechnician based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_FinalTestTechnician_Type.__name__ = "DisplayString"
_FinalTestTechnician_Object = MibScalar
finalTestTechnician = _FinalTestTechnician_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 24),
    _FinalTestTechnician_Type()
)
finalTestTechnician.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    finalTestTechnician.setStatus("mandatory")
_HwFailures_Type = Integer32
_HwFailures_Object = MibScalar
hwFailures = _HwFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 25),
    _HwFailures_Type()
)
hwFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFailures.setStatus("mandatory")
_HwHistory_Type = Integer32
_HwHistory_Object = MibScalar
hwHistory = _HwHistory_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 26),
    _HwHistory_Type()
)
hwHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHistory.setStatus("mandatory")


class _SecLineModuleType_Type(Integer32):
    """Custom type secLineModuleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              32,
              33,
              34,
              35,
              48,
              49,
              50,
              51,
              60,
              61,
              62,
              63,
              70,
              71,
              80,
              81,
              500,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              511,
              512,
              513,
              514,
              515,
              1006)
        )
    )
    namedValues = NamedValues(
        *(("lm-12In1-8s", 63),
          ("lm-155-SMF", 34),
          ("lm-155-UTP", 35),
          ("lm-3T3-B", 51),
          ("lm-ASC", 2),
          ("lm-BNC-2E3", 81),
          ("lm-BNC-2T3", 80),
          ("lm-BNC-4E1", 18),
          ("lm-BNC-4E1-R", 21),
          ("lm-BSCSM-2", 70),
          ("lm-BSCSM-4", 71),
          ("lm-DB15-4E1", 17),
          ("lm-DB15-4E1-R", 20),
          ("lm-DB15-4T1", 16),
          ("lm-DB15-4T1-R", 19),
          ("lm-HS1-3HSSI", 61),
          ("lm-HS1-4V35", 62),
          ("lm-HS1-4X21", 60),
          ("lm-RJ48-8E1", 23),
          ("lm-RJ48-8E1-R", 49),
          ("lm-RJ48-8T1", 22),
          ("lm-RJ48-8T1-R", 48),
          ("lm-RJ48-E3E1", 26),
          ("lm-RJ48-E3T1", 29),
          ("lm-RJ48-T3E1", 27),
          ("lm-RJ48-T3T1", 25),
          ("lm-SMB-8E1", 24),
          ("lm-SMB-8E1-R", 50),
          ("lm-SMB-E3E1", 28),
          ("lm-SMB-T3E1", 30),
          ("lm-T3E3-B", 33),
          ("lm-T3E3-D", 32),
          ("mmf-4-155", 505),
          ("mmf-fddi", 513),
          ("mmf-fe", 512),
          ("other", 1),
          ("pxm-ui", 500),
          ("pxm-ui-s3", 1006),
          ("rj45-4e", 515),
          ("rj45-fe", 511),
          ("smf-fddi", 514),
          ("smfir-1-622", 501),
          ("smfir-4-155", 506),
          ("smfir15-1-622", 503),
          ("smflr-1-622", 502),
          ("smflr-4-155", 507),
          ("smflr15-1-622", 504))
    )


_SecLineModuleType_Type.__name__ = "Integer32"
_SecLineModuleType_Object = MibScalar
secLineModuleType = _SecLineModuleType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 27),
    _SecLineModuleType_Type()
)
secLineModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secLineModuleType.setStatus("mandatory")


class _SecLineModuleDescription_Type(DisplayString):
    """Custom type secLineModuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SecLineModuleDescription_Type.__name__ = "DisplayString"
_SecLineModuleDescription_Object = MibScalar
secLineModuleDescription = _SecLineModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 28),
    _SecLineModuleDescription_Type()
)
secLineModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secLineModuleDescription.setStatus("mandatory")


class _SecLineModuleSerialNum_Type(DisplayString):
    """Custom type secLineModuleSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_SecLineModuleSerialNum_Type.__name__ = "DisplayString"
_SecLineModuleSerialNum_Object = MibScalar
secLineModuleSerialNum = _SecLineModuleSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 29),
    _SecLineModuleSerialNum_Type()
)
secLineModuleSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secLineModuleSerialNum.setStatus("mandatory")


class _SecLineModuleHWRev_Type(DisplayString):
    """Custom type secLineModuleHWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_SecLineModuleHWRev_Type.__name__ = "DisplayString"
_SecLineModuleHWRev_Object = MibScalar
secLineModuleHWRev = _SecLineModuleHWRev_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 30),
    _SecLineModuleHWRev_Type()
)
secLineModuleHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secLineModuleHWRev.setStatus("mandatory")


class _SecLineModuleFWRev_Type(DisplayString):
    """Custom type secLineModuleFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SecLineModuleFWRev_Type.__name__ = "DisplayString"
_SecLineModuleFWRev_Object = MibScalar
secLineModuleFWRev = _SecLineModuleFWRev_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 31),
    _SecLineModuleFWRev_Type()
)
secLineModuleFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secLineModuleFWRev.setStatus("mandatory")


class _SecLineModuleState_Type(Integer32):
    """Custom type secLineModuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("notPresent", 1),
          ("present", 2))
    )


_SecLineModuleState_Type.__name__ = "Integer32"
_SecLineModuleState_Object = MibScalar
secLineModuleState = _SecLineModuleState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 32),
    _SecLineModuleState_Type()
)
secLineModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secLineModuleState.setStatus("mandatory")


class _ConfigChangeParentObjectIndex_Type(Integer32):
    """Custom type configChangeParentObjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ConfigChangeParentObjectIndex_Type.__name__ = "Integer32"
_ConfigChangeParentObjectIndex_Object = MibScalar
configChangeParentObjectIndex = _ConfigChangeParentObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 33),
    _ConfigChangeParentObjectIndex_Type()
)
configChangeParentObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configChangeParentObjectIndex.setStatus("mandatory")


class _ConfigChangeGrandParentObjectIndex_Type(Integer32):
    """Custom type configChangeGrandParentObjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ConfigChangeGrandParentObjectIndex_Type.__name__ = "Integer32"
_ConfigChangeGrandParentObjectIndex_Object = MibScalar
configChangeGrandParentObjectIndex = _ConfigChangeGrandParentObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 34),
    _ConfigChangeGrandParentObjectIndex_Type()
)
configChangeGrandParentObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configChangeGrandParentObjectIndex.setStatus("mandatory")


class _ConfigChangeSMSpecificObject_Type(Integer32):
    """Custom type configChangeSMSpecificObject based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ConfigChangeSMSpecificObject_Type.__name__ = "Integer32"
_ConfigChangeSMSpecificObject_Object = MibScalar
configChangeSMSpecificObject = _ConfigChangeSMSpecificObject_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 35),
    _ConfigChangeSMSpecificObject_Type()
)
configChangeSMSpecificObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configChangeSMSpecificObject.setStatus("mandatory")


class _TransId_Type(Integer32):
    """Custom type transId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TransId_Type.__name__ = "Integer32"
_TransId_Object = MibScalar
transId = _TransId_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 36),
    _TransId_Type()
)
transId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transId.setStatus("mandatory")
_CardInterface_ObjectIdentity = ObjectIdentity
cardInterface = _CardInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 2)
)
_InterfaceLineTable_Object = MibTable
interfaceLineTable = _InterfaceLineTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1)
)
if mibBuilder.loadTexts:
    interfaceLineTable.setStatus("mandatory")
_InterfaceLineEntry_Object = MibTableRow
interfaceLineEntry = _InterfaceLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1)
)
interfaceLineEntry.setIndexNames(
    (0, "BASIS-GENERIC-MIB", "interfaceLineNum"),
)
if mibBuilder.loadTexts:
    interfaceLineEntry.setStatus("mandatory")


class _InterfaceLineNum_Type(Integer32):
    """Custom type interfaceLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_InterfaceLineNum_Type.__name__ = "Integer32"
_InterfaceLineNum_Object = MibTableColumn
interfaceLineNum = _InterfaceLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1, 1),
    _InterfaceLineNum_Type()
)
interfaceLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceLineNum.setStatus("mandatory")


class _InterfaceLineType_Type(Integer32):
    """Custom type interfaceLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              18,
              19,
              26,
              30,
              33,
              45,
              46)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("ethernet-3Mbit", 26),
          ("hssi", 46),
          ("other", 1),
          ("rs232", 33),
          ("v35", 45))
    )


_InterfaceLineType_Type.__name__ = "Integer32"
_InterfaceLineType_Object = MibTableColumn
interfaceLineType = _InterfaceLineType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1, 2),
    _InterfaceLineType_Type()
)
interfaceLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceLineType.setStatus("mandatory")


class _InterfaceNumOfPortsPerLine_Type(Integer32):
    """Custom type interfaceNumOfPortsPerLine based on Integer32"""
    defaultValue = 672

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InterfaceNumOfPortsPerLine_Type.__name__ = "Integer32"
_InterfaceNumOfPortsPerLine_Object = MibTableColumn
interfaceNumOfPortsPerLine = _InterfaceNumOfPortsPerLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1, 3),
    _InterfaceNumOfPortsPerLine_Type()
)
interfaceNumOfPortsPerLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceNumOfPortsPerLine.setStatus("mandatory")


class _InterfaceServiceType_Type(Integer32):
    """Custom type interfaceServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              26,
              28,
              32,
              37,
              42)
        )
    )
    namedValues = NamedValues(
        *(("atm", 37),
          ("ethernet-3Mbit", 26),
          ("frameRelay", 32),
          ("other", 1),
          ("slip", 28),
          ("voice", 42))
    )


_InterfaceServiceType_Type.__name__ = "Integer32"
_InterfaceServiceType_Object = MibTableColumn
interfaceServiceType = _InterfaceServiceType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1, 4),
    _InterfaceServiceType_Type()
)
interfaceServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceServiceType.setStatus("mandatory")
_InterfaceNumOfPVC_Type = Integer32
_InterfaceNumOfPVC_Object = MibTableColumn
interfaceNumOfPVC = _InterfaceNumOfPVC_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1, 5),
    _InterfaceNumOfPVC_Type()
)
interfaceNumOfPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceNumOfPVC.setStatus("mandatory")
_InterfaceNumOfEgressQueue_Type = Integer32
_InterfaceNumOfEgressQueue_Object = MibTableColumn
interfaceNumOfEgressQueue = _InterfaceNumOfEgressQueue_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1, 6),
    _InterfaceNumOfEgressQueue_Type()
)
interfaceNumOfEgressQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceNumOfEgressQueue.setStatus("mandatory")
_InterfaceNumOfValidEntries_Type = Integer32
_InterfaceNumOfValidEntries_Object = MibScalar
interfaceNumOfValidEntries = _InterfaceNumOfValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 2),
    _InterfaceNumOfValidEntries_Type()
)
interfaceNumOfValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceNumOfValidEntries.setStatus("mandatory")
_CardSelfTest_ObjectIdentity = ObjectIdentity
cardSelfTest = _CardSelfTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 3)
)


class _SelfTestEnable_Type(Integer32):
    """Custom type selfTestEnable based on Integer32"""
    defaultValue = 1

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


_SelfTestEnable_Type.__name__ = "Integer32"
_SelfTestEnable_Object = MibScalar
selfTestEnable = _SelfTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 3, 1),
    _SelfTestEnable_Type()
)
selfTestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selfTestEnable.setStatus("mandatory")


class _SelfTestPeriod_Type(Integer32):
    """Custom type selfTestPeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SelfTestPeriod_Type.__name__ = "Integer32"
_SelfTestPeriod_Object = MibScalar
selfTestPeriod = _SelfTestPeriod_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 3, 2),
    _SelfTestPeriod_Type()
)
selfTestPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selfTestPeriod.setStatus("mandatory")


class _SelfTestState_Type(Integer32):
    """Custom type selfTestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("passed", 1))
    )


_SelfTestState_Type.__name__ = "Integer32"
_SelfTestState_Object = MibScalar
selfTestState = _SelfTestState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 3, 3),
    _SelfTestState_Type()
)
selfTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfTestState.setStatus("mandatory")


class _SelfTestResultDescription_Type(DisplayString):
    """Custom type selfTestResultDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SelfTestResultDescription_Type.__name__ = "DisplayString"
_SelfTestResultDescription_Object = MibScalar
selfTestResultDescription = _SelfTestResultDescription_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 3, 4),
    _SelfTestResultDescription_Type()
)
selfTestResultDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfTestResultDescription.setStatus("mandatory")


class _SelfTestClrResultButton_Type(Integer32):
    """Custom type selfTestClrResultButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("other", 1))
    )


_SelfTestClrResultButton_Type.__name__ = "Integer32"
_SelfTestClrResultButton_Object = MibScalar
selfTestClrResultButton = _SelfTestClrResultButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 3, 5),
    _SelfTestClrResultButton_Type()
)
selfTestClrResultButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selfTestClrResultButton.setStatus("mandatory")
_ControlMsgCounter_ObjectIdentity = ObjectIdentity
controlMsgCounter = _ControlMsgCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 4)
)
_RiscXmtCtrlMsg_Type = Counter32
_RiscXmtCtrlMsg_Object = MibScalar
riscXmtCtrlMsg = _RiscXmtCtrlMsg_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 1),
    _RiscXmtCtrlMsg_Type()
)
riscXmtCtrlMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riscXmtCtrlMsg.setStatus("mandatory")
_RiscRcvCtrlMsg_Type = Counter32
_RiscRcvCtrlMsg_Object = MibScalar
riscRcvCtrlMsg = _RiscRcvCtrlMsg_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 2),
    _RiscRcvCtrlMsg_Type()
)
riscRcvCtrlMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riscRcvCtrlMsg.setStatus("mandatory")
_SarXmtCtrlMsg_Type = Counter32
_SarXmtCtrlMsg_Object = MibScalar
sarXmtCtrlMsg = _SarXmtCtrlMsg_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 3),
    _SarXmtCtrlMsg_Type()
)
sarXmtCtrlMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sarXmtCtrlMsg.setStatus("mandatory")
_SarRcvCtrlMsg_Type = Counter32
_SarRcvCtrlMsg_Object = MibScalar
sarRcvCtrlMsg = _SarRcvCtrlMsg_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 4),
    _SarRcvCtrlMsg_Type()
)
sarRcvCtrlMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sarRcvCtrlMsg.setStatus("mandatory")
_SarCtrlMsgDiscLenErr_Type = Counter32
_SarCtrlMsgDiscLenErr_Object = MibScalar
sarCtrlMsgDiscLenErr = _SarCtrlMsgDiscLenErr_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 5),
    _SarCtrlMsgDiscLenErr_Type()
)
sarCtrlMsgDiscLenErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sarCtrlMsgDiscLenErr.setStatus("mandatory")
_SarCtrlMsgDiscCRCErr_Type = Counter32
_SarCtrlMsgDiscCRCErr_Object = MibScalar
sarCtrlMsgDiscCRCErr = _SarCtrlMsgDiscCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 6),
    _SarCtrlMsgDiscCRCErr_Type()
)
sarCtrlMsgDiscCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sarCtrlMsgDiscCRCErr.setStatus("mandatory")
_SarCtrlMsgDiscUnknownChan_Type = Counter32
_SarCtrlMsgDiscUnknownChan_Object = MibScalar
sarCtrlMsgDiscUnknownChan = _SarCtrlMsgDiscUnknownChan_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 7),
    _SarCtrlMsgDiscUnknownChan_Type()
)
sarCtrlMsgDiscUnknownChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sarCtrlMsgDiscUnknownChan.setStatus("mandatory")
_SarCtrlMsgLastUnkownChan_Type = Integer32
_SarCtrlMsgLastUnkownChan_Object = MibScalar
sarCtrlMsgLastUnkownChan = _SarCtrlMsgLastUnkownChan_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 8),
    _SarCtrlMsgLastUnkownChan_Type()
)
sarCtrlMsgLastUnkownChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sarCtrlMsgLastUnkownChan.setStatus("mandatory")


class _CtrlMsgClrButton_Type(Integer32):
    """Custom type ctrlMsgClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("other", 1))
    )


_CtrlMsgClrButton_Type.__name__ = "Integer32"
_CtrlMsgClrButton_Object = MibScalar
ctrlMsgClrButton = _CtrlMsgClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 9),
    _CtrlMsgClrButton_Type()
)
ctrlMsgClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlMsgClrButton.setStatus("mandatory")
_SarChannelCounter_ObjectIdentity = ObjectIdentity
sarChannelCounter = _SarChannelCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5)
)
_SarChannelCounterTable_Object = MibTable
sarChannelCounterTable = _SarChannelCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1)
)
if mibBuilder.loadTexts:
    sarChannelCounterTable.setStatus("mandatory")
_SarChannelCounterEntry_Object = MibTableRow
sarChannelCounterEntry = _SarChannelCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1)
)
sarChannelCounterEntry.setIndexNames(
    (0, "BASIS-GENERIC-MIB", "sarShelfNum"),
    (0, "BASIS-GENERIC-MIB", "sarSlotNum"),
    (0, "BASIS-GENERIC-MIB", "sarChanNum"),
)
if mibBuilder.loadTexts:
    sarChannelCounterEntry.setStatus("mandatory")


class _SarShelfNum_Type(Integer32):
    """Custom type sarShelfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SarShelfNum_Type.__name__ = "Integer32"
_SarShelfNum_Object = MibTableColumn
sarShelfNum = _SarShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 1),
    _SarShelfNum_Type()
)
sarShelfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sarShelfNum.setStatus("mandatory")


class _SarSlotNum_Type(Integer32):
    """Custom type sarSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SarSlotNum_Type.__name__ = "Integer32"
_SarSlotNum_Object = MibTableColumn
sarSlotNum = _SarSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 2),
    _SarSlotNum_Type()
)
sarSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sarSlotNum.setStatus("mandatory")


class _SarChanNum_Type(Integer32):
    """Custom type sarChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4015),
    )


_SarChanNum_Type.__name__ = "Integer32"
_SarChanNum_Object = MibTableColumn
sarChanNum = _SarChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 3),
    _SarChanNum_Type()
)
sarChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sarChanNum.setStatus("mandatory")
_XmtCells_Type = Counter32
_XmtCells_Object = MibTableColumn
xmtCells = _XmtCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 4),
    _XmtCells_Type()
)
xmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtCells.setStatus("mandatory")
_XmtCellsCLP_Type = Counter32
_XmtCellsCLP_Object = MibTableColumn
xmtCellsCLP = _XmtCellsCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 5),
    _XmtCellsCLP_Type()
)
xmtCellsCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtCellsCLP.setStatus("mandatory")
_XmtCellsAIS_Type = Counter32
_XmtCellsAIS_Object = MibTableColumn
xmtCellsAIS = _XmtCellsAIS_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 6),
    _XmtCellsAIS_Type()
)
xmtCellsAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtCellsAIS.setStatus("mandatory")
_XmtCellsFERF_Type = Counter32
_XmtCellsFERF_Object = MibTableColumn
xmtCellsFERF = _XmtCellsFERF_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 7),
    _XmtCellsFERF_Type()
)
xmtCellsFERF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtCellsFERF.setStatus("mandatory")
_XmtCellsBCM_Type = Counter32
_XmtCellsBCM_Object = MibTableColumn
xmtCellsBCM = _XmtCellsBCM_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 8),
    _XmtCellsBCM_Type()
)
xmtCellsBCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtCellsBCM.setStatus("mandatory")
_XmtCellsEnd2EndLpBk_Type = Counter32
_XmtCellsEnd2EndLpBk_Object = MibTableColumn
xmtCellsEnd2EndLpBk = _XmtCellsEnd2EndLpBk_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 9),
    _XmtCellsEnd2EndLpBk_Type()
)
xmtCellsEnd2EndLpBk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtCellsEnd2EndLpBk.setStatus("mandatory")
_XmtCellsSegmentLpBk_Type = Counter32
_XmtCellsSegmentLpBk_Object = MibTableColumn
xmtCellsSegmentLpBk = _XmtCellsSegmentLpBk_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 10),
    _XmtCellsSegmentLpBk_Type()
)
xmtCellsSegmentLpBk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtCellsSegmentLpBk.setStatus("mandatory")
_XmtCellsDiscShelfAlarm_Type = Counter32
_XmtCellsDiscShelfAlarm_Object = MibTableColumn
xmtCellsDiscShelfAlarm = _XmtCellsDiscShelfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 11),
    _XmtCellsDiscShelfAlarm_Type()
)
xmtCellsDiscShelfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtCellsDiscShelfAlarm.setStatus("mandatory")
_RcvCells_Type = Counter32
_RcvCells_Object = MibTableColumn
rcvCells = _RcvCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 12),
    _RcvCells_Type()
)
rcvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvCells.setStatus("mandatory")
_RcvCellsCLP_Type = Counter32
_RcvCellsCLP_Object = MibTableColumn
rcvCellsCLP = _RcvCellsCLP_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 13),
    _RcvCellsCLP_Type()
)
rcvCellsCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvCellsCLP.setStatus("mandatory")
_RcvCellsAIS_Type = Counter32
_RcvCellsAIS_Object = MibTableColumn
rcvCellsAIS = _RcvCellsAIS_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 14),
    _RcvCellsAIS_Type()
)
rcvCellsAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvCellsAIS.setStatus("mandatory")
_RcvCellsFERF_Type = Counter32
_RcvCellsFERF_Object = MibTableColumn
rcvCellsFERF = _RcvCellsFERF_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 15),
    _RcvCellsFERF_Type()
)
rcvCellsFERF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvCellsFERF.setStatus("mandatory")
_RcvCellsBCM_Type = Counter32
_RcvCellsBCM_Object = MibTableColumn
rcvCellsBCM = _RcvCellsBCM_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 16),
    _RcvCellsBCM_Type()
)
rcvCellsBCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvCellsBCM.setStatus("mandatory")
_RcvCellsEnd2EndLpBk_Type = Counter32
_RcvCellsEnd2EndLpBk_Object = MibTableColumn
rcvCellsEnd2EndLpBk = _RcvCellsEnd2EndLpBk_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 17),
    _RcvCellsEnd2EndLpBk_Type()
)
rcvCellsEnd2EndLpBk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvCellsEnd2EndLpBk.setStatus("mandatory")
_RcvCellsSegmentLpBk_Type = Counter32
_RcvCellsSegmentLpBk_Object = MibTableColumn
rcvCellsSegmentLpBk = _RcvCellsSegmentLpBk_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 18),
    _RcvCellsSegmentLpBk_Type()
)
rcvCellsSegmentLpBk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvCellsSegmentLpBk.setStatus("mandatory")
_RcvCellsDiscOAM_Type = Counter32
_RcvCellsDiscOAM_Object = MibTableColumn
rcvCellsDiscOAM = _RcvCellsDiscOAM_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 19),
    _RcvCellsDiscOAM_Type()
)
rcvCellsDiscOAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvCellsDiscOAM.setStatus("mandatory")


class _SarClrButton_Type(Integer32):
    """Custom type sarClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("other", 1))
    )


_SarClrButton_Type.__name__ = "Integer32"
_SarClrButton_Object = MibTableColumn
sarClrButton = _SarClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 20),
    _SarClrButton_Type()
)
sarClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sarClrButton.setStatus("mandatory")
_ChanNumOfValidEntries_Type = Integer32
_ChanNumOfValidEntries_Object = MibScalar
chanNumOfValidEntries = _ChanNumOfValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 2),
    _ChanNumOfValidEntries_Type()
)
chanNumOfValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanNumOfValidEntries.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BASIS-GENERIC-MIB",
    **{"cardInformation": cardInformation,
       "moduleSlotNumber": moduleSlotNumber,
       "functionModuleType": functionModuleType,
       "functionModuleDescription": functionModuleDescription,
       "functionModuleSerialNum": functionModuleSerialNum,
       "functionModuleHWRev": functionModuleHWRev,
       "functionModuleFWRev": functionModuleFWRev,
       "functionModuleState": functionModuleState,
       "functionModuleResetReason": functionModuleResetReason,
       "lineModuleType": lineModuleType,
       "lineModuleDescription": lineModuleDescription,
       "lineModuleSerialNum": lineModuleSerialNum,
       "lineModuleHWRev": lineModuleHWRev,
       "lineModuleFWRev": lineModuleFWRev,
       "lineModuleState": lineModuleState,
       "moduleTrapAlarmSeverity": moduleTrapAlarmSeverity,
       "mibVersionNumber": mibVersionNumber,
       "configChangeTypeBitMap": configChangeTypeBitMap,
       "configChangeObjectIndex": configChangeObjectIndex,
       "configChangeStatus": configChangeStatus,
       "cardIntegratedAlarmBitMap": cardIntegratedAlarmBitMap,
       "cleiCode": cleiCode,
       "macAddress": macAddress,
       "macAddrBlkSize": macAddrBlkSize,
       "finalTestTechnician": finalTestTechnician,
       "hwFailures": hwFailures,
       "hwHistory": hwHistory,
       "secLineModuleType": secLineModuleType,
       "secLineModuleDescription": secLineModuleDescription,
       "secLineModuleSerialNum": secLineModuleSerialNum,
       "secLineModuleHWRev": secLineModuleHWRev,
       "secLineModuleFWRev": secLineModuleFWRev,
       "secLineModuleState": secLineModuleState,
       "configChangeParentObjectIndex": configChangeParentObjectIndex,
       "configChangeGrandParentObjectIndex": configChangeGrandParentObjectIndex,
       "configChangeSMSpecificObject": configChangeSMSpecificObject,
       "transId": transId,
       "cardInterface": cardInterface,
       "interfaceLineTable": interfaceLineTable,
       "interfaceLineEntry": interfaceLineEntry,
       "interfaceLineNum": interfaceLineNum,
       "interfaceLineType": interfaceLineType,
       "interfaceNumOfPortsPerLine": interfaceNumOfPortsPerLine,
       "interfaceServiceType": interfaceServiceType,
       "interfaceNumOfPVC": interfaceNumOfPVC,
       "interfaceNumOfEgressQueue": interfaceNumOfEgressQueue,
       "interfaceNumOfValidEntries": interfaceNumOfValidEntries,
       "cardSelfTest": cardSelfTest,
       "selfTestEnable": selfTestEnable,
       "selfTestPeriod": selfTestPeriod,
       "selfTestState": selfTestState,
       "selfTestResultDescription": selfTestResultDescription,
       "selfTestClrResultButton": selfTestClrResultButton,
       "controlMsgCounter": controlMsgCounter,
       "riscXmtCtrlMsg": riscXmtCtrlMsg,
       "riscRcvCtrlMsg": riscRcvCtrlMsg,
       "sarXmtCtrlMsg": sarXmtCtrlMsg,
       "sarRcvCtrlMsg": sarRcvCtrlMsg,
       "sarCtrlMsgDiscLenErr": sarCtrlMsgDiscLenErr,
       "sarCtrlMsgDiscCRCErr": sarCtrlMsgDiscCRCErr,
       "sarCtrlMsgDiscUnknownChan": sarCtrlMsgDiscUnknownChan,
       "sarCtrlMsgLastUnkownChan": sarCtrlMsgLastUnkownChan,
       "ctrlMsgClrButton": ctrlMsgClrButton,
       "sarChannelCounter": sarChannelCounter,
       "sarChannelCounterTable": sarChannelCounterTable,
       "sarChannelCounterEntry": sarChannelCounterEntry,
       "sarShelfNum": sarShelfNum,
       "sarSlotNum": sarSlotNum,
       "sarChanNum": sarChanNum,
       "xmtCells": xmtCells,
       "xmtCellsCLP": xmtCellsCLP,
       "xmtCellsAIS": xmtCellsAIS,
       "xmtCellsFERF": xmtCellsFERF,
       "xmtCellsBCM": xmtCellsBCM,
       "xmtCellsEnd2EndLpBk": xmtCellsEnd2EndLpBk,
       "xmtCellsSegmentLpBk": xmtCellsSegmentLpBk,
       "xmtCellsDiscShelfAlarm": xmtCellsDiscShelfAlarm,
       "rcvCells": rcvCells,
       "rcvCellsCLP": rcvCellsCLP,
       "rcvCellsAIS": rcvCellsAIS,
       "rcvCellsFERF": rcvCellsFERF,
       "rcvCellsBCM": rcvCellsBCM,
       "rcvCellsEnd2EndLpBk": rcvCellsEnd2EndLpBk,
       "rcvCellsSegmentLpBk": rcvCellsSegmentLpBk,
       "rcvCellsDiscOAM": rcvCellsDiscOAM,
       "sarClrButton": sarClrButton,
       "chanNumOfValidEntries": chanNumOfValidEntries}
)
