# SNMP MIB module (CISCO-MGX82XX-DSX3-BERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MGX82XX-DSX3-BERT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:32 2024
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

(axisDiagnostics,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "axisDiagnostics")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoMgx82xxDsx3BertMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 39)
)
ciscoMgx82xxDsx3BertMIB.setRevisions(
        ("2003-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dsx3bert_ObjectIdentity = ObjectIdentity
dsx3bert = _Dsx3bert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2)
)


class _Dsx3bertControl_Type(Integer32):
    """Custom type dsx3bertControl based on Integer32"""
    defaultValue = 0

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
        *(("acquireBert", 1),
          ("cnfBert", 3),
          ("delBert", 6),
          ("modBert", 5),
          ("noAction", 0),
          ("releaseBert", 2),
          ("startBert", 4))
    )


_Dsx3bertControl_Type.__name__ = "Integer32"
_Dsx3bertControl_Object = MibScalar
dsx3bertControl = _Dsx3bertControl_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 1),
    _Dsx3bertControl_Type()
)
dsx3bertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3bertControl.setStatus("current")


class _Dsx3bertResourceStatus_Type(Integer32):
    """Custom type dsx3bertResourceStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("free", 1),
          ("inUse", 2))
    )


_Dsx3bertResourceStatus_Type.__name__ = "Integer32"
_Dsx3bertResourceStatus_Object = MibScalar
dsx3bertResourceStatus = _Dsx3bertResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 2),
    _Dsx3bertResourceStatus_Type()
)
dsx3bertResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3bertResourceStatus.setStatus("current")
_Dsx3bertOwner_Type = DisplayString
_Dsx3bertOwner_Object = MibScalar
dsx3bertOwner = _Dsx3bertOwner_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 3),
    _Dsx3bertOwner_Type()
)
dsx3bertOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3bertOwner.setStatus("current")
_Dsx3bertUserId_Type = DisplayString
_Dsx3bertUserId_Object = MibScalar
dsx3bertUserId = _Dsx3bertUserId_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 4),
    _Dsx3bertUserId_Type()
)
dsx3bertUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3bertUserId.setStatus("current")


class _Dsx3bertStatus_Type(Integer32):
    """Custom type dsx3bertStatus based on Integer32"""
    defaultValue = 1

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
        *(("bertFailed", 6),
          ("bertInSync", 2),
          ("bertOutOfSync", 3),
          ("farEndInLoop", 4),
          ("inactive", 1),
          ("metallicInLoop", 5))
    )


_Dsx3bertStatus_Type.__name__ = "Integer32"
_Dsx3bertStatus_Object = MibScalar
dsx3bertStatus = _Dsx3bertStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 5),
    _Dsx3bertStatus_Type()
)
dsx3bertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3bertStatus.setStatus("current")


class _Dsx3bertTestMedium_Type(Integer32):
    """Custom type dsx3bertTestMedium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line", 2),
          ("port", 1))
    )


_Dsx3bertTestMedium_Type.__name__ = "Integer32"
_Dsx3bertTestMedium_Object = MibScalar
dsx3bertTestMedium = _Dsx3bertTestMedium_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 6),
    _Dsx3bertTestMedium_Type()
)
dsx3bertTestMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3bertTestMedium.setStatus("current")


class _Dsx3bertPort_Type(Integer32):
    """Custom type dsx3bertPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx3bertPort_Type.__name__ = "Integer32"
_Dsx3bertPort_Object = MibScalar
dsx3bertPort = _Dsx3bertPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 7),
    _Dsx3bertPort_Type()
)
dsx3bertPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3bertPort.setStatus("current")


class _Dsx3bertLine_Type(Integer32):
    """Custom type dsx3bertLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx3bertLine_Type.__name__ = "Integer32"
_Dsx3bertLine_Object = MibScalar
dsx3bertLine = _Dsx3bertLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 8),
    _Dsx3bertLine_Type()
)
dsx3bertLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3bertLine.setStatus("current")


class _Dsx3bertMode_Type(Integer32):
    """Custom type dsx3bertMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bertPatternTest", 1),
          ("loopback", 2))
    )


_Dsx3bertMode_Type.__name__ = "Integer32"
_Dsx3bertMode_Object = MibScalar
dsx3bertMode = _Dsx3bertMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 9),
    _Dsx3bertMode_Type()
)
dsx3bertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3bertMode.setStatus("current")


class _Dsx3bertPattern_Type(Integer32):
    """Custom type dsx3bertPattern based on Integer32"""
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
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 1),
          ("allZeros", 2),
          ("alternateOneZero", 3),
          ("doubleOneZero", 4),
          ("eighteenBit", 23),
          ("elevenBit", 20),
          ("fifteenBit", 21),
          ("fiveBit", 13),
          ("fourBit", 12),
          ("fracT1LoopDown", 17),
          ("fracT1LoopUp", 16),
          ("nineBit", 18),
          ("oneInEight", 7),
          ("oneInFour", 8),
          ("oneInSixteen", 6),
          ("sevenBit", 15),
          ("seventeenBit", 22),
          ("sfLoopDown", 10),
          ("sfLoopUp", 9),
          ("sixBit", 14),
          ("tenBit", 19),
          ("thirtyOneBit", 32),
          ("thirtyTwo", 33),
          ("threeBit", 11),
          ("threeInTwentyFour", 5),
          ("twentyBit", 24),
          ("twentyBitQRSS", 25),
          ("twentyEightBit", 30),
          ("twentyFiveBit", 29),
          ("twentyNineBit", 31),
          ("twentyOneBit", 26),
          ("twentyThreeBit", 28),
          ("twentyTwoBit", 27))
    )


_Dsx3bertPattern_Type.__name__ = "Integer32"
_Dsx3bertPattern_Object = MibScalar
dsx3bertPattern = _Dsx3bertPattern_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 10),
    _Dsx3bertPattern_Type()
)
dsx3bertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3bertPattern.setStatus("current")


class _Dsx3bertLoopback_Type(Integer32):
    """Custom type dsx3bertLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("farEndLoopback", 1),
          ("metallicLoopback", 2))
    )


_Dsx3bertLoopback_Type.__name__ = "Integer32"
_Dsx3bertLoopback_Object = MibScalar
dsx3bertLoopback = _Dsx3bertLoopback_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 11),
    _Dsx3bertLoopback_Type()
)
dsx3bertLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3bertLoopback.setStatus("current")


class _Dsx3bertStartTime_Type(DisplayString):
    """Custom type dsx3bertStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_Dsx3bertStartTime_Type.__name__ = "DisplayString"
_Dsx3bertStartTime_Object = MibScalar
dsx3bertStartTime = _Dsx3bertStartTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 12),
    _Dsx3bertStartTime_Type()
)
dsx3bertStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3bertStartTime.setStatus("current")


class _Dsx3bertStartDate_Type(DisplayString):
    """Custom type dsx3bertStartDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_Dsx3bertStartDate_Type.__name__ = "DisplayString"
_Dsx3bertStartDate_Object = MibScalar
dsx3bertStartDate = _Dsx3bertStartDate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 13),
    _Dsx3bertStartDate_Type()
)
dsx3bertStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3bertStartDate.setStatus("current")


class _Dsx3bertBitCountUpper_Type(Integer32):
    """Custom type dsx3bertBitCountUpper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3bertBitCountUpper_Type.__name__ = "Integer32"
_Dsx3bertBitCountUpper_Object = MibScalar
dsx3bertBitCountUpper = _Dsx3bertBitCountUpper_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 14),
    _Dsx3bertBitCountUpper_Type()
)
dsx3bertBitCountUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3bertBitCountUpper.setStatus("current")


class _Dsx3bertBitCountLower_Type(Integer32):
    """Custom type dsx3bertBitCountLower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3bertBitCountLower_Type.__name__ = "Integer32"
_Dsx3bertBitCountLower_Object = MibScalar
dsx3bertBitCountLower = _Dsx3bertBitCountLower_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 15),
    _Dsx3bertBitCountLower_Type()
)
dsx3bertBitCountLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3bertBitCountLower.setStatus("current")


class _Dsx3bertBitErrorCountUpper_Type(Integer32):
    """Custom type dsx3bertBitErrorCountUpper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3bertBitErrorCountUpper_Type.__name__ = "Integer32"
_Dsx3bertBitErrorCountUpper_Object = MibScalar
dsx3bertBitErrorCountUpper = _Dsx3bertBitErrorCountUpper_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 16),
    _Dsx3bertBitErrorCountUpper_Type()
)
dsx3bertBitErrorCountUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3bertBitErrorCountUpper.setStatus("current")


class _Dsx3bertBitErrorCountLower_Type(Integer32):
    """Custom type dsx3bertBitErrorCountLower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3bertBitErrorCountLower_Type.__name__ = "Integer32"
_Dsx3bertBitErrorCountLower_Object = MibScalar
dsx3bertBitErrorCountLower = _Dsx3bertBitErrorCountLower_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 17),
    _Dsx3bertBitErrorCountLower_Type()
)
dsx3bertBitErrorCountLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3bertBitErrorCountLower.setStatus("current")


class _Dsx3bertErrorInsertionRate_Type(Integer32):
    """Custom type dsx3bertErrorInsertionRate based on Integer32"""
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
        *(("errorInsertionDisabled", 1),
          ("oneInTen", 2),
          ("oneInTenPowerFive", 6),
          ("oneInTenPowerFour", 5),
          ("oneInTenPowerSeven", 8),
          ("oneInTenPowerSix", 7),
          ("oneInTenPowerThree", 4),
          ("oneInTenPowerTwo", 3))
    )


_Dsx3bertErrorInsertionRate_Type.__name__ = "Integer32"
_Dsx3bertErrorInsertionRate_Object = MibScalar
dsx3bertErrorInsertionRate = _Dsx3bertErrorInsertionRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 18),
    _Dsx3bertErrorInsertionRate_Type()
)
dsx3bertErrorInsertionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3bertErrorInsertionRate.setStatus("current")


class _Dsx3bertErrorInjectCount_Type(Integer32):
    """Custom type dsx3bertErrorInjectCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3bertErrorInjectCount_Type.__name__ = "Integer32"
_Dsx3bertErrorInjectCount_Object = MibScalar
dsx3bertErrorInjectCount = _Dsx3bertErrorInjectCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 19),
    _Dsx3bertErrorInjectCount_Type()
)
dsx3bertErrorInjectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3bertErrorInjectCount.setStatus("current")


class _Dsx3bertCleanupAction_Type(Integer32):
    """Custom type dsx3bertCleanupAction based on Integer32"""
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
        *(("metallicLoopdown", 3),
          ("noAction", 1),
          ("smCleanup", 2))
    )


_Dsx3bertCleanupAction_Type.__name__ = "Integer32"
_Dsx3bertCleanupAction_Object = MibScalar
dsx3bertCleanupAction = _Dsx3bertCleanupAction_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 20),
    _Dsx3bertCleanupAction_Type()
)
dsx3bertCleanupAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3bertCleanupAction.setStatus("current")
_CmDsx3BertMIBConformance_ObjectIdentity = ObjectIdentity
cmDsx3BertMIBConformance = _CmDsx3BertMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 39, 2)
)
_CmDsx3BertMIBGroups_ObjectIdentity = ObjectIdentity
cmDsx3BertMIBGroups = _CmDsx3BertMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 39, 2, 1)
)
_CmDsx3BertMIBCompliances_ObjectIdentity = ObjectIdentity
cmDsx3BertMIBCompliances = _CmDsx3BertMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 39, 2, 2)
)

# Managed Objects groups

cmDsx3BertConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 39, 2, 1, 1)
)
cmDsx3BertConfGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertControl"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertResourceStatus"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertOwner"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertUserId"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertStatus"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertTestMedium"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertPort"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertLine"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertMode"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertPattern"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertLoopback"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertStartTime"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertStartDate"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertBitCountUpper"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertBitCountLower"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertBitErrorCountUpper"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertBitErrorCountLower"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertErrorInsertionRate"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertErrorInjectCount"),
        ("CISCO-MGX82XX-DSX3-BERT-MIB", "dsx3bertCleanupAction"))
)
if mibBuilder.loadTexts:
    cmDsx3BertConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmDsx3BertCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 39, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cmDsx3BertCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-DSX3-BERT-MIB",
    **{"dsx3bert": dsx3bert,
       "dsx3bertControl": dsx3bertControl,
       "dsx3bertResourceStatus": dsx3bertResourceStatus,
       "dsx3bertOwner": dsx3bertOwner,
       "dsx3bertUserId": dsx3bertUserId,
       "dsx3bertStatus": dsx3bertStatus,
       "dsx3bertTestMedium": dsx3bertTestMedium,
       "dsx3bertPort": dsx3bertPort,
       "dsx3bertLine": dsx3bertLine,
       "dsx3bertMode": dsx3bertMode,
       "dsx3bertPattern": dsx3bertPattern,
       "dsx3bertLoopback": dsx3bertLoopback,
       "dsx3bertStartTime": dsx3bertStartTime,
       "dsx3bertStartDate": dsx3bertStartDate,
       "dsx3bertBitCountUpper": dsx3bertBitCountUpper,
       "dsx3bertBitCountLower": dsx3bertBitCountLower,
       "dsx3bertBitErrorCountUpper": dsx3bertBitErrorCountUpper,
       "dsx3bertBitErrorCountLower": dsx3bertBitErrorCountLower,
       "dsx3bertErrorInsertionRate": dsx3bertErrorInsertionRate,
       "dsx3bertErrorInjectCount": dsx3bertErrorInjectCount,
       "dsx3bertCleanupAction": dsx3bertCleanupAction,
       "ciscoMgx82xxDsx3BertMIB": ciscoMgx82xxDsx3BertMIB,
       "cmDsx3BertMIBConformance": cmDsx3BertMIBConformance,
       "cmDsx3BertMIBGroups": cmDsx3BertMIBGroups,
       "cmDsx3BertConfGroup": cmDsx3BertConfGroup,
       "cmDsx3BertMIBCompliances": cmDsx3BertMIBCompliances,
       "cmDsx3BertCompliance": cmDsx3BertCompliance}
)
