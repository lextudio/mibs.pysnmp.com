# SNMP MIB module (BASIS-SHELF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BASIS-SHELF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:45 2024
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

(axisRedundancy,
 basisShelf) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "axisRedundancy",
    "basisShelf")

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

_ShelfTable_Object = MibTable
shelfTable = _ShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1)
)
if mibBuilder.loadTexts:
    shelfTable.setStatus("mandatory")
_ShelfEntry_Object = MibTableRow
shelfEntry = _ShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1)
)
shelfEntry.setIndexNames(
    (0, "BASIS-SHELF-MIB", "shelfNum"),
    (0, "BASIS-SHELF-MIB", "shelfSlotNum"),
)
if mibBuilder.loadTexts:
    shelfEntry.setStatus("mandatory")


class _ShelfNum_Type(Integer32):
    """Custom type shelfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ShelfNum_Type.__name__ = "Integer32"
_ShelfNum_Object = MibTableColumn
shelfNum = _ShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1, 1),
    _ShelfNum_Type()
)
shelfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfNum.setStatus("mandatory")


class _ShelfSlotNum_Type(Integer32):
    """Custom type shelfSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_ShelfSlotNum_Type.__name__ = "Integer32"
_ShelfSlotNum_Object = MibTableColumn
shelfSlotNum = _ShelfSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1, 2),
    _ShelfSlotNum_Type()
)
shelfSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfSlotNum.setStatus("mandatory")


class _ShelfBkplnSerialNumDeprecated_Type(Integer32):
    """Custom type shelfBkplnSerialNumDeprecated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ShelfBkplnSerialNumDeprecated_Type.__name__ = "Integer32"
_ShelfBkplnSerialNumDeprecated_Object = MibTableColumn
shelfBkplnSerialNumDeprecated = _ShelfBkplnSerialNumDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1, 3),
    _ShelfBkplnSerialNumDeprecated_Type()
)
shelfBkplnSerialNumDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBkplnSerialNumDeprecated.setStatus("mandatory")


class _ShelfFunctionModuleState_Type(Integer32):
    """Custom type shelfFunctionModuleState based on Integer32"""
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
          ("coreCardMismatch", 10),
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


_ShelfFunctionModuleState_Type.__name__ = "Integer32"
_ShelfFunctionModuleState_Object = MibTableColumn
shelfFunctionModuleState = _ShelfFunctionModuleState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1, 4),
    _ShelfFunctionModuleState_Type()
)
shelfFunctionModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfFunctionModuleState.setStatus("mandatory")


class _ShelfFunctionModuleType_Type(Integer32):
    """Custom type shelfFunctionModuleType based on Integer32"""
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
          ("imatmB-E1", 73),
          ("imatmB-T1", 72),
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


_ShelfFunctionModuleType_Type.__name__ = "Integer32"
_ShelfFunctionModuleType_Object = MibTableColumn
shelfFunctionModuleType = _ShelfFunctionModuleType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1, 5),
    _ShelfFunctionModuleType_Type()
)
shelfFunctionModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfFunctionModuleType.setStatus("mandatory")


class _ShelfFunctionModuleHoldReset_Type(Integer32):
    """Custom type shelfFunctionModuleHoldReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotHold", 1),
          ("holdInReset", 2))
    )


_ShelfFunctionModuleHoldReset_Type.__name__ = "Integer32"
_ShelfFunctionModuleHoldReset_Object = MibTableColumn
shelfFunctionModuleHoldReset = _ShelfFunctionModuleHoldReset_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1, 6),
    _ShelfFunctionModuleHoldReset_Type()
)
shelfFunctionModuleHoldReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfFunctionModuleHoldReset.setStatus("mandatory")


class _ShelfNumOfValidEntries_Type(Integer32):
    """Custom type shelfNumOfValidEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ShelfNumOfValidEntries_Type.__name__ = "Integer32"
_ShelfNumOfValidEntries_Object = MibScalar
shelfNumOfValidEntries = _ShelfNumOfValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 2),
    _ShelfNumOfValidEntries_Type()
)
shelfNumOfValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfNumOfValidEntries.setStatus("mandatory")


class _ShelfNodeName_Type(DisplayString):
    """Custom type shelfNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ShelfNodeName_Type.__name__ = "DisplayString"
_ShelfNodeName_Object = MibScalar
shelfNodeName = _ShelfNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 3),
    _ShelfNodeName_Type()
)
shelfNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfNodeName.setStatus("mandatory")


class _ShelfDate_Type(DisplayString):
    """Custom type shelfDate based on DisplayString"""
    defaultValue = OctetString("01/01/1994")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_ShelfDate_Type.__name__ = "DisplayString"
_ShelfDate_Object = MibScalar
shelfDate = _ShelfDate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 4),
    _ShelfDate_Type()
)
shelfDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfDate.setStatus("mandatory")


class _ShelfTime_Type(DisplayString):
    """Custom type shelfTime based on DisplayString"""
    defaultValue = OctetString("12:00:00")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ShelfTime_Type.__name__ = "DisplayString"
_ShelfTime_Object = MibScalar
shelfTime = _ShelfTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 5),
    _ShelfTime_Type()
)
shelfTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfTime.setStatus("mandatory")


class _ShelfTmZn_Type(Integer32):
    """Custom type shelfTmZn based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("cdt", 7),
          ("cst", 3),
          ("edt", 6),
          ("est", 2),
          ("gmt", 1),
          ("mdt", 8),
          ("mst", 4),
          ("pdt", 9),
          ("pst", 5))
    )


_ShelfTmZn_Type.__name__ = "Integer32"
_ShelfTmZn_Object = MibScalar
shelfTmZn = _ShelfTmZn_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 6),
    _ShelfTmZn_Type()
)
shelfTmZn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfTmZn.setStatus("mandatory")


class _ShelfTmZnGMTOff_Type(Integer32):
    """Custom type shelfTmZnGMTOff based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_ShelfTmZnGMTOff_Type.__name__ = "Integer32"
_ShelfTmZnGMTOff_Object = MibScalar
shelfTmZnGMTOff = _ShelfTmZnGMTOff_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 7),
    _ShelfTmZnGMTOff_Type()
)
shelfTmZnGMTOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfTmZnGMTOff.setStatus("mandatory")


class _ShelfBkPlnType_Type(Integer32):
    """Custom type shelfBkPlnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ShelfBkPlnType_Type.__name__ = "Integer32"
_ShelfBkPlnType_Object = MibScalar
shelfBkPlnType = _ShelfBkPlnType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 8),
    _ShelfBkPlnType_Type()
)
shelfBkPlnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBkPlnType.setStatus("mandatory")


class _ShelfBkplnSerialNum_Type(DisplayString):
    """Custom type shelfBkplnSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ShelfBkplnSerialNum_Type.__name__ = "DisplayString"
_ShelfBkplnSerialNum_Object = MibScalar
shelfBkplnSerialNum = _ShelfBkplnSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 9),
    _ShelfBkplnSerialNum_Type()
)
shelfBkplnSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBkplnSerialNum.setStatus("mandatory")
_StatsMasterIpAddress_Type = IpAddress
_StatsMasterIpAddress_Object = MibScalar
statsMasterIpAddress = _StatsMasterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 10),
    _StatsMasterIpAddress_Type()
)
statsMasterIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsMasterIpAddress.setStatus("mandatory")


class _StatsCollectionInterval_Type(Integer32):
    """Custom type statsCollectionInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StatsCollectionInterval_Type.__name__ = "Integer32"
_StatsCollectionInterval_Object = MibScalar
statsCollectionInterval = _StatsCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 11),
    _StatsCollectionInterval_Type()
)
statsCollectionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsCollectionInterval.setStatus("mandatory")


class _StatsBucketInterval_Type(Integer32):
    """Custom type statsBucketInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StatsBucketInterval_Type.__name__ = "Integer32"
_StatsBucketInterval_Object = MibScalar
statsBucketInterval = _StatsBucketInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 12),
    _StatsBucketInterval_Type()
)
statsBucketInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsBucketInterval.setStatus("mandatory")


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 13),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("mandatory")


class _ShelfIntegratedAlarm_Type(Integer32):
    """Custom type shelfIntegratedAlarm based on Integer32"""
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
        *(("clear", 1),
          ("critical", 4),
          ("major", 3),
          ("minor", 2))
    )


_ShelfIntegratedAlarm_Type.__name__ = "Integer32"
_ShelfIntegratedAlarm_Object = MibScalar
shelfIntegratedAlarm = _ShelfIntegratedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 14),
    _ShelfIntegratedAlarm_Type()
)
shelfIntegratedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfIntegratedAlarm.setStatus("mandatory")


class _ShelfAlarmCardBitMap_Type(Integer32):
    """Custom type shelfAlarmCardBitMap based on Integer32"""
    defaultValue = 0


_ShelfAlarmCardBitMap_Object = MibScalar
shelfAlarmCardBitMap = _ShelfAlarmCardBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 15),
    _ShelfAlarmCardBitMap_Type()
)
shelfAlarmCardBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfAlarmCardBitMap.setStatus("mandatory")


class _AxisFeederTkNo_Type(Integer32):
    """Custom type axisFeederTkNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AxisFeederTkNo_Type.__name__ = "Integer32"
_AxisFeederTkNo_Object = MibScalar
axisFeederTkNo = _AxisFeederTkNo_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 16),
    _AxisFeederTkNo_Type()
)
axisFeederTkNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    axisFeederTkNo.setStatus("mandatory")


class _AxisSvcBillingColInterval_Type(Integer32):
    """Custom type axisSvcBillingColInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("a0minutes", 1),
          ("a15minutes", 2),
          ("a30minutes", 3))
    )


_AxisSvcBillingColInterval_Type.__name__ = "Integer32"
_AxisSvcBillingColInterval_Object = MibScalar
axisSvcBillingColInterval = _AxisSvcBillingColInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 17),
    _AxisSvcBillingColInterval_Type()
)
axisSvcBillingColInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    axisSvcBillingColInterval.setStatus("mandatory")


class _AxisSvcBillingBucketInterval_Type(Integer32):
    """Custom type axisSvcBillingBucketInterval based on Integer32"""
    defaultValue = 3

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
        *(("a0minutes", 1),
          ("a15minutes", 3),
          ("a30minutes", 4),
          ("a5minutes", 2))
    )


_AxisSvcBillingBucketInterval_Type.__name__ = "Integer32"
_AxisSvcBillingBucketInterval_Object = MibScalar
axisSvcBillingBucketInterval = _AxisSvcBillingBucketInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 18),
    _AxisSvcBillingBucketInterval_Type()
)
axisSvcBillingBucketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    axisSvcBillingBucketInterval.setStatus("mandatory")
_ApsIpAddress_Type = IpAddress
_ApsIpAddress_Object = MibScalar
apsIpAddress = _ApsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 19),
    _ApsIpAddress_Type()
)
apsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsIpAddress.setStatus("mandatory")
_RedundantApsIpAddress_Type = IpAddress
_RedundantApsIpAddress_Object = MibScalar
redundantApsIpAddress = _RedundantApsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 20),
    _RedundantApsIpAddress_Type()
)
redundantApsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantApsIpAddress.setStatus("mandatory")


class _AxisSvcBilling_Type(Integer32):
    """Custom type axisSvcBilling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AxisSvcBilling_Type.__name__ = "Integer32"
_AxisSvcBilling_Object = MibScalar
axisSvcBilling = _AxisSvcBilling_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 21),
    _AxisSvcBilling_Type()
)
axisSvcBilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    axisSvcBilling.setStatus("mandatory")
_ShelfCBClkRateTable_Object = MibTable
shelfCBClkRateTable = _ShelfCBClkRateTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 22)
)
if mibBuilder.loadTexts:
    shelfCBClkRateTable.setStatus("mandatory")
_ShelfCBClkRateEntry_Object = MibTableRow
shelfCBClkRateEntry = _ShelfCBClkRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 22, 1)
)
shelfCBClkRateEntry.setIndexNames(
    (0, "BASIS-SHELF-MIB", "cBNum"),
)
if mibBuilder.loadTexts:
    shelfCBClkRateEntry.setStatus("mandatory")


class _CBNum_Type(Integer32):
    """Custom type cBNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CBNum_Type.__name__ = "Integer32"
_CBNum_Object = MibTableColumn
cBNum = _CBNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 22, 1, 1),
    _CBNum_Type()
)
cBNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBNum.setStatus("mandatory")


class _ClkRate_Type(Integer32):
    """Custom type clkRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fortyTwo-Mhz", 2),
          ("twentyOne-Mhz", 1))
    )


_ClkRate_Type.__name__ = "Integer32"
_ClkRate_Object = MibTableColumn
clkRate = _ClkRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 22, 1, 2),
    _ClkRate_Type()
)
clkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clkRate.setStatus("mandatory")


class _ShelfPowerSupplyVoltage_Type(Integer32):
    """Custom type shelfPowerSupplyVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one-ten", 2),
          ("two-twenty", 1))
    )


_ShelfPowerSupplyVoltage_Type.__name__ = "Integer32"
_ShelfPowerSupplyVoltage_Object = MibScalar
shelfPowerSupplyVoltage = _ShelfPowerSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 23),
    _ShelfPowerSupplyVoltage_Type()
)
shelfPowerSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfPowerSupplyVoltage.setStatus("mandatory")


class _ShelfFilteredAlarm_Type(Integer32):
    """Custom type shelfFilteredAlarm based on Integer32"""
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
        *(("clear", 1),
          ("critical", 4),
          ("major", 3),
          ("minor", 2))
    )


_ShelfFilteredAlarm_Type.__name__ = "Integer32"
_ShelfFilteredAlarm_Object = MibScalar
shelfFilteredAlarm = _ShelfFilteredAlarm_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 24),
    _ShelfFilteredAlarm_Type()
)
shelfFilteredAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfFilteredAlarm.setStatus("mandatory")
_SmRedMapTable_Object = MibTable
smRedMapTable = _SmRedMapTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1)
)
if mibBuilder.loadTexts:
    smRedMapTable.setStatus("mandatory")
_SmRedMapEntry_Object = MibTableRow
smRedMapEntry = _SmRedMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1)
)
smRedMapEntry.setIndexNames(
    (0, "BASIS-SHELF-MIB", "redPrimarySlotNum"),
)
if mibBuilder.loadTexts:
    smRedMapEntry.setStatus("mandatory")


class _RedPrimarySlotNum_Type(Integer32):
    """Custom type redPrimarySlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RedPrimarySlotNum_Type.__name__ = "Integer32"
_RedPrimarySlotNum_Object = MibTableColumn
redPrimarySlotNum = _RedPrimarySlotNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 1),
    _RedPrimarySlotNum_Type()
)
redPrimarySlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redPrimarySlotNum.setStatus("mandatory")


class _RedRowStatus_Type(Integer32):
    """Custom type redRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2),
          ("mod", 3))
    )


_RedRowStatus_Type.__name__ = "Integer32"
_RedRowStatus_Object = MibTableColumn
redRowStatus = _RedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 2),
    _RedRowStatus_Type()
)
redRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redRowStatus.setStatus("mandatory")


class _RedPrimaryType_Type(Integer32):
    """Custom type redPrimaryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              20,
              30,
              31,
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
        *(("atmt-8E1", 111),
          ("atmt-8T1", 110),
          ("aum-T3", 10),
          ("ausm-4E1", 41),
          ("ausm-4T1", 40),
          ("ausm-8E1", 51),
          ("ausm-8T1", 50),
          ("ausmB-8E1", 53),
          ("ausmB-8T1", 52),
          ("bsc", 2),
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
          ("frsm-4T1", 30),
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
          ("imatmB-E1", 73),
          ("imatmB-T1", 72),
          ("other", 1),
          ("pxm1", 1000),
          ("pxm1-2t3e3", 1001),
          ("pxm1-4oc3", 1002),
          ("pxm1-oc12", 1003),
          ("rpm", 2000),
          ("rpm-pr", 2001),
          ("tim", 20),
          ("vism-8E1", 151),
          ("vism-8T1", 150),
          ("vism-pr-8E1", 564),
          ("vism-pr-8T1", 563))
    )


_RedPrimaryType_Type.__name__ = "Integer32"
_RedPrimaryType_Object = MibTableColumn
redPrimaryType = _RedPrimaryType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 3),
    _RedPrimaryType_Type()
)
redPrimaryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redPrimaryType.setStatus("mandatory")


class _RedPrimaryState_Type(Integer32):
    """Custom type redPrimaryState based on Integer32"""
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
          ("failed", 4),
          ("heldInReset", 6),
          ("mismatch", 8),
          ("nocard", 1),
          ("notResponding", 14),
          ("reserved", 12),
          ("selfTest", 5),
          ("standby", 2),
          ("unknown", 9),
          ("unusedCoreCardMisMatch", 10),
          ("unusedHold", 13))
    )


_RedPrimaryState_Type.__name__ = "Integer32"
_RedPrimaryState_Object = MibTableColumn
redPrimaryState = _RedPrimaryState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 4),
    _RedPrimaryState_Type()
)
redPrimaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redPrimaryState.setStatus("mandatory")


class _RedSecondarySlotNum_Type(Integer32):
    """Custom type redSecondarySlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RedSecondarySlotNum_Type.__name__ = "Integer32"
_RedSecondarySlotNum_Object = MibTableColumn
redSecondarySlotNum = _RedSecondarySlotNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 5),
    _RedSecondarySlotNum_Type()
)
redSecondarySlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redSecondarySlotNum.setStatus("mandatory")


class _RedSecondaryType_Type(Integer32):
    """Custom type redSecondaryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              20,
              30,
              31,
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
        *(("atmt-8E1", 111),
          ("atmt-8T1", 110),
          ("aum-T3", 10),
          ("ausm-4E1", 41),
          ("ausm-4T1", 40),
          ("ausm-8E1", 51),
          ("ausm-8T1", 50),
          ("ausmB-8E1", 53),
          ("ausmB-8T1", 52),
          ("bsc", 2),
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
          ("frsm-4T1", 30),
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
          ("imatmB-E1", 73),
          ("imatmB-T1", 72),
          ("other", 1),
          ("pxm1", 1000),
          ("pxm1-2t3e3", 1001),
          ("pxm1-4oc3", 1002),
          ("pxm1-oc12", 1003),
          ("rpm", 2000),
          ("rpm-pr", 2001),
          ("tim", 20),
          ("vism-8E1", 151),
          ("vism-8T1", 150),
          ("vism-pr-8E1", 564),
          ("vism-pr-8T1", 563))
    )


_RedSecondaryType_Type.__name__ = "Integer32"
_RedSecondaryType_Object = MibTableColumn
redSecondaryType = _RedSecondaryType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 6),
    _RedSecondaryType_Type()
)
redSecondaryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redSecondaryType.setStatus("mandatory")


class _RedSecondaryState_Type(Integer32):
    """Custom type redSecondaryState based on Integer32"""
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
          ("failed", 4),
          ("heldInReset", 6),
          ("mismatch", 8),
          ("nocard", 1),
          ("notResponding", 14),
          ("reserved", 12),
          ("selfTest", 5),
          ("standby", 2),
          ("unknown", 9),
          ("unusedCoreCardMisMatch", 10),
          ("unusedHold", 13))
    )


_RedSecondaryState_Type.__name__ = "Integer32"
_RedSecondaryState_Object = MibTableColumn
redSecondaryState = _RedSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 7),
    _RedSecondaryState_Type()
)
redSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redSecondaryState.setStatus("mandatory")


class _RedType_Type(Integer32):
    """Custom type redType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneToN", 2),
          ("yCable", 1))
    )


_RedType_Type.__name__ = "Integer32"
_RedType_Object = MibTableColumn
redType = _RedType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 8),
    _RedType_Type()
)
redType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redType.setStatus("mandatory")


class _RedCoveringSlot_Type(Integer32):
    """Custom type redCoveringSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RedCoveringSlot_Type.__name__ = "Integer32"
_RedCoveringSlot_Object = MibTableColumn
redCoveringSlot = _RedCoveringSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 9),
    _RedCoveringSlot_Type()
)
redCoveringSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redCoveringSlot.setStatus("mandatory")
_RedFeature_Type = Integer32
_RedFeature_Object = MibTableColumn
redFeature = _RedFeature_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 10),
    _RedFeature_Type()
)
redFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redFeature.setStatus("mandatory")


class _RedLineModuleType_Type(Integer32):
    """Custom type redLineModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
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
              48,
              49,
              50,
              60,
              61,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("lm-12In1-8s", 63),
          ("lm-BNC-4E1", 18),
          ("lm-BNC-4E1-R", 21),
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
          ("lm-T3E3-D", 32))
    )


_RedLineModuleType_Type.__name__ = "Integer32"
_RedLineModuleType_Object = MibTableColumn
redLineModuleType = _RedLineModuleType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 11),
    _RedLineModuleType_Type()
)
redLineModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redLineModuleType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BASIS-SHELF-MIB",
    **{"shelfTable": shelfTable,
       "shelfEntry": shelfEntry,
       "shelfNum": shelfNum,
       "shelfSlotNum": shelfSlotNum,
       "shelfBkplnSerialNumDeprecated": shelfBkplnSerialNumDeprecated,
       "shelfFunctionModuleState": shelfFunctionModuleState,
       "shelfFunctionModuleType": shelfFunctionModuleType,
       "shelfFunctionModuleHoldReset": shelfFunctionModuleHoldReset,
       "shelfNumOfValidEntries": shelfNumOfValidEntries,
       "shelfNodeName": shelfNodeName,
       "shelfDate": shelfDate,
       "shelfTime": shelfTime,
       "shelfTmZn": shelfTmZn,
       "shelfTmZnGMTOff": shelfTmZnGMTOff,
       "shelfBkPlnType": shelfBkPlnType,
       "shelfBkplnSerialNum": shelfBkplnSerialNum,
       "statsMasterIpAddress": statsMasterIpAddress,
       "statsCollectionInterval": statsCollectionInterval,
       "statsBucketInterval": statsBucketInterval,
       "userName": userName,
       "shelfIntegratedAlarm": shelfIntegratedAlarm,
       "shelfAlarmCardBitMap": shelfAlarmCardBitMap,
       "axisFeederTkNo": axisFeederTkNo,
       "axisSvcBillingColInterval": axisSvcBillingColInterval,
       "axisSvcBillingBucketInterval": axisSvcBillingBucketInterval,
       "apsIpAddress": apsIpAddress,
       "redundantApsIpAddress": redundantApsIpAddress,
       "axisSvcBilling": axisSvcBilling,
       "shelfCBClkRateTable": shelfCBClkRateTable,
       "shelfCBClkRateEntry": shelfCBClkRateEntry,
       "cBNum": cBNum,
       "clkRate": clkRate,
       "shelfPowerSupplyVoltage": shelfPowerSupplyVoltage,
       "shelfFilteredAlarm": shelfFilteredAlarm,
       "smRedMapTable": smRedMapTable,
       "smRedMapEntry": smRedMapEntry,
       "redPrimarySlotNum": redPrimarySlotNum,
       "redRowStatus": redRowStatus,
       "redPrimaryType": redPrimaryType,
       "redPrimaryState": redPrimaryState,
       "redSecondarySlotNum": redSecondarySlotNum,
       "redSecondaryType": redSecondaryType,
       "redSecondaryState": redSecondaryState,
       "redType": redType,
       "redCoveringSlot": redCoveringSlot,
       "redFeature": redFeature,
       "redLineModuleType": redLineModuleType}
)
