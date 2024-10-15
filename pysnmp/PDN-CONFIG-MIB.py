# SNMP MIB module (PDN-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:22 2024
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

(pdn_devConfig,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-devConfig")

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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DevConfigArea_ObjectIdentity = ObjectIdentity
devConfigArea = _DevConfigArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 1)
)


class _DevConfigAreaCopy_Type(Integer32):
    """Custom type devConfigAreaCopy based on Integer32"""
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
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("active-to-customer1", 2),
          ("active-to-customer2", 3),
          ("customer1-to-active", 4),
          ("customer1-to-customer2", 5),
          ("customer2-to-active", 6),
          ("customer2-to-customer1", 7),
          ("factory1-to-active", 8),
          ("factory1-to-customer1", 9),
          ("factory1-to-customer2", 10),
          ("factory2-to-active", 11),
          ("factory2-to-customer1", 12),
          ("factory2-to-customer2", 13),
          ("factory3-to-active", 14),
          ("factory3-to-customer1", 15),
          ("factory3-to-customer2", 16),
          ("factory4-to-active", 17),
          ("factory4-to-customer1", 18),
          ("factory4-to-customer2", 19),
          ("factory5-to-active", 20),
          ("factory5-to-customer1", 21),
          ("factory5-to-customer2", 22),
          ("factory6-to-active", 23),
          ("factory6-to-customer1", 24),
          ("factory6-to-customer2", 25),
          ("factory7-to-active", 26),
          ("factory7-to-customer1", 27),
          ("factory7-to-customer2", 28),
          ("factory8-to-active", 29),
          ("factory8-to-customer1", 30),
          ("factory8-to-customer2", 31),
          ("factory9-to-active", 32),
          ("factory9-to-customer1", 33),
          ("factory9-to-customer2", 34),
          ("noOp", 1))
    )


_DevConfigAreaCopy_Type.__name__ = "Integer32"
_DevConfigAreaCopy_Object = MibScalar
devConfigAreaCopy = _DevConfigAreaCopy_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 1, 1),
    _DevConfigAreaCopy_Type()
)
devConfigAreaCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devConfigAreaCopy.setStatus("mandatory")
_DevConfigTestTimer_ObjectIdentity = ObjectIdentity
devConfigTestTimer = _DevConfigTestTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 2)
)


class _DevConfigTestTimeout_Type(Integer32):
    """Custom type devConfigTestTimeout based on Integer32"""
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


_DevConfigTestTimeout_Type.__name__ = "Integer32"
_DevConfigTestTimeout_Object = MibScalar
devConfigTestTimeout = _DevConfigTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 2, 1),
    _DevConfigTestTimeout_Type()
)
devConfigTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devConfigTestTimeout.setStatus("mandatory")
_DevConfigTestDuration_Type = Integer32
_DevConfigTestDuration_Object = MibScalar
devConfigTestDuration = _DevConfigTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 2, 2),
    _DevConfigTestDuration_Type()
)
devConfigTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devConfigTestDuration.setStatus("mandatory")
_DevConfigClockSrc_ObjectIdentity = ObjectIdentity
devConfigClockSrc = _DevConfigClockSrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3)
)
_DevConfigClockSrcTable_Object = MibTable
devConfigClockSrcTable = _DevConfigClockSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1)
)
if mibBuilder.loadTexts:
    devConfigClockSrcTable.setStatus("mandatory")
_DevConfigClockSrcEntry_Object = MibTableRow
devConfigClockSrcEntry = _DevConfigClockSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1)
)
devConfigClockSrcEntry.setIndexNames(
    (0, "PDN-CONFIG-MIB", "devCfgClkWhichSrc"),
)
if mibBuilder.loadTexts:
    devConfigClockSrcEntry.setStatus("mandatory")


class _DevCfgClkWhichSrc_Type(Integer32):
    """Custom type devCfgClkWhichSrc based on Integer32"""
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


_DevCfgClkWhichSrc_Type.__name__ = "Integer32"
_DevCfgClkWhichSrc_Object = MibTableColumn
devCfgClkWhichSrc = _DevCfgClkWhichSrc_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1, 1),
    _DevCfgClkWhichSrc_Type()
)
devCfgClkWhichSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devCfgClkWhichSrc.setStatus("mandatory")


class _DevCfgClkSource_Type(Integer32):
    """Custom type devCfgClkSource based on Integer32"""
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
        *(("dbm", 4),
          ("external", 2),
          ("external2", 5),
          ("interface", 3),
          ("internal", 1))
    )


_DevCfgClkSource_Type.__name__ = "Integer32"
_DevCfgClkSource_Object = MibTableColumn
devCfgClkSource = _DevCfgClkSource_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1, 2),
    _DevCfgClkSource_Type()
)
devCfgClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devCfgClkSource.setStatus("mandatory")
_DevCfgClkIfIndex_Type = Integer32
_DevCfgClkIfIndex_Object = MibTableColumn
devCfgClkIfIndex = _DevCfgClkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1, 3),
    _DevCfgClkIfIndex_Type()
)
devCfgClkIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devCfgClkIfIndex.setStatus("mandatory")


class _DevCfgClkRate_Type(Integer32):
    """Custom type devCfgClkRate based on Integer32"""
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
        *(("rate1544KHz", 4),
          ("rate2048KHz", 5),
          ("rate400Hz", 1),
          ("rate64KHz", 3),
          ("rate8KHz", 2))
    )


_DevCfgClkRate_Type.__name__ = "Integer32"
_DevCfgClkRate_Object = MibTableColumn
devCfgClkRate = _DevCfgClkRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1, 4),
    _DevCfgClkRate_Type()
)
devCfgClkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devCfgClkRate.setStatus("mandatory")
_DevConfigTrap_ObjectIdentity = ObjectIdentity
devConfigTrap = _DevConfigTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 4)
)
_DevConfigTrapEnable_Type = Integer32
_DevConfigTrapEnable_Object = MibScalar
devConfigTrapEnable = _DevConfigTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 4, 1),
    _DevConfigTrapEnable_Type()
)
devConfigTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devConfigTrapEnable.setStatus("mandatory")
_CCNTrapEnable_Type = Integer32
_CCNTrapEnable_Object = MibScalar
cCNTrapEnable = _CCNTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 4, 2),
    _CCNTrapEnable_Type()
)
cCNTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCNTrapEnable.setStatus("mandatory")
_DevConfigAlarm_ObjectIdentity = ObjectIdentity
devConfigAlarm = _DevConfigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 5)
)


class _DevConfigAlarmRelayCutoff_Type(Integer32):
    """Custom type devConfigAlarmRelayCutoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("off", 2))
    )


_DevConfigAlarmRelayCutoff_Type.__name__ = "Integer32"
_DevConfigAlarmRelayCutoff_Object = MibScalar
devConfigAlarmRelayCutoff = _DevConfigAlarmRelayCutoff_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 5, 6),
    _DevConfigAlarmRelayCutoff_Type()
)
devConfigAlarmRelayCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devConfigAlarmRelayCutoff.setStatus("mandatory")
_DevConfigCardType_ObjectIdentity = ObjectIdentity
devConfigCardType = _DevConfigCardType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6)
)
_DevConfigCardTypeTable_Object = MibTable
devConfigCardTypeTable = _DevConfigCardTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7)
)
if mibBuilder.loadTexts:
    devConfigCardTypeTable.setStatus("mandatory")
_DevConfigCardTypeEntry_Object = MibTableRow
devConfigCardTypeEntry = _DevConfigCardTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1)
)
devConfigCardTypeEntry.setIndexNames(
    (0, "PDN-CONFIG-MIB", "devCfgCardSlot"),
)
if mibBuilder.loadTexts:
    devConfigCardTypeEntry.setStatus("mandatory")
_DevCfgCardSlot_Type = Integer32
_DevCfgCardSlot_Object = MibTableColumn
devCfgCardSlot = _DevCfgCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1, 1),
    _DevCfgCardSlot_Type()
)
devCfgCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devCfgCardSlot.setStatus("mandatory")


class _DevCfgCardConfig_Type(Integer32):
    """Custom type devCfgCardConfig based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("acceptingAPM", 17),
          ("dce6APM", 13),
          ("ddsNAM", 21),
          ("dpNAM", 19),
          ("dslNAM", 25),
          ("dsxAPM", 8),
          ("dualDsxNniNAM", 22),
          ("emptySlot", 1),
          ("failedAPM", 18),
          ("misconfiguredAPM", 10),
          ("ocu2APM", 11),
          ("ocu4APM", 15),
          ("ocu6APM", 12),
          ("pktVoiceAPM", 16),
          ("sruAPM", 14),
          ("stNAM", 20),
          ("syncDataAPM", 4),
          ("t1NAM", 3),
          ("t1NoDsxNAM", 9),
          ("t3NAM", 24),
          ("t3NniNAM", 23),
          ("unsupportedAPM", 2),
          ("voiceEmAPM", 6),
          ("voiceFxoAPM", 7),
          ("voiceFxsAPM", 5))
    )


_DevCfgCardConfig_Type.__name__ = "Integer32"
_DevCfgCardConfig_Object = MibTableColumn
devCfgCardConfig = _DevCfgCardConfig_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1, 2),
    _DevCfgCardConfig_Type()
)
devCfgCardConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devCfgCardConfig.setStatus("mandatory")


class _DevCfgCardActual_Type(Integer32):
    """Custom type devCfgCardActual based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("acceptingAPM", 17),
          ("dce6APM", 13),
          ("ddsNAM", 21),
          ("dpNAM", 19),
          ("dslNAM", 25),
          ("dualDsxNniNAM", 22),
          ("emptySlot", 1),
          ("failedAPM", 18),
          ("misconfigured", 10),
          ("ocu2APM", 11),
          ("ocu4APM", 15),
          ("ocu6APM", 12),
          ("pktVoiceAPM", 16),
          ("sruAPM", 14),
          ("stNAM", 20),
          ("syncDataAPM", 4),
          ("t1NAM", 3),
          ("t1NoDsxNAM", 9),
          ("t3NAM", 24),
          ("t3NniNAM", 23),
          ("unsupportedAPM", 2),
          ("voiceDsxAPM", 8),
          ("voiceEmAPM", 6),
          ("voiceFxoAPM", 7),
          ("voiceFxsAPM", 5))
    )


_DevCfgCardActual_Type.__name__ = "Integer32"
_DevCfgCardActual_Object = MibTableColumn
devCfgCardActual = _DevCfgCardActual_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1, 3),
    _DevCfgCardActual_Type()
)
devCfgCardActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devCfgCardActual.setStatus("mandatory")


class _DevCfgCardAction_Type(Integer32):
    """Custom type devCfgCardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("noOp", 1))
    )


_DevCfgCardAction_Type.__name__ = "Integer32"
_DevCfgCardAction_Object = MibTableColumn
devCfgCardAction = _DevCfgCardAction_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1, 4),
    _DevCfgCardAction_Type()
)
devCfgCardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devCfgCardAction.setStatus("mandatory")
_DevConfigNetSync_ObjectIdentity = ObjectIdentity
devConfigNetSync = _DevConfigNetSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 7)
)


class _DevConfigNetSyncRole_Type(Integer32):
    """Custom type devConfigNetSyncRole based on Integer32"""
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
        *(("controller", 3),
          ("none", 1),
          ("tributary", 2))
    )


_DevConfigNetSyncRole_Type.__name__ = "Integer32"
_DevConfigNetSyncRole_Object = MibScalar
devConfigNetSyncRole = _DevConfigNetSyncRole_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 7, 1),
    _DevConfigNetSyncRole_Type()
)
devConfigNetSyncRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devConfigNetSyncRole.setStatus("mandatory")
_DevConfigTime_ObjectIdentity = ObjectIdentity
devConfigTime = _DevConfigTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 8)
)
_DevConfigTimeOfDay_Type = DateAndTime
_DevConfigTimeOfDay_Object = MibScalar
devConfigTimeOfDay = _DevConfigTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 8, 1),
    _DevConfigTimeOfDay_Type()
)
devConfigTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devConfigTimeOfDay.setStatus("mandatory")
_DevConfigChangeKeys_ObjectIdentity = ObjectIdentity
devConfigChangeKeys = _DevConfigChangeKeys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9)
)
_DevConfigChangeKeysTable_Object = MibTable
devConfigChangeKeysTable = _DevConfigChangeKeysTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9, 1)
)
if mibBuilder.loadTexts:
    devConfigChangeKeysTable.setStatus("mandatory")
_DevConfigChangeKeysEntry_Object = MibTableRow
devConfigChangeKeysEntry = _DevConfigChangeKeysEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9, 1, 1)
)
devConfigChangeKeysEntry.setIndexNames(
    (0, "PDN-CONFIG-MIB", "devConfigChangeKeysDbType"),
)
if mibBuilder.loadTexts:
    devConfigChangeKeysEntry.setStatus("mandatory")


class _DevConfigChangeKeysDbType_Type(Integer32):
    """Custom type devConfigChangeKeysDbType based on Integer32"""
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
        *(("generalConfig", 1),
          ("rmonAlarm", 2),
          ("rmonUserHistory", 3),
          ("routerConfig", 4))
    )


_DevConfigChangeKeysDbType_Type.__name__ = "Integer32"
_DevConfigChangeKeysDbType_Object = MibTableColumn
devConfigChangeKeysDbType = _DevConfigChangeKeysDbType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9, 1, 1, 1),
    _DevConfigChangeKeysDbType_Type()
)
devConfigChangeKeysDbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devConfigChangeKeysDbType.setStatus("mandatory")
_DevConfigChangeKeysDbKey_Type = Gauge32
_DevConfigChangeKeysDbKey_Object = MibTableColumn
devConfigChangeKeysDbKey = _DevConfigChangeKeysDbKey_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9, 1, 1, 2),
    _DevConfigChangeKeysDbKey_Type()
)
devConfigChangeKeysDbKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devConfigChangeKeysDbKey.setStatus("mandatory")
_DevConfiguration_ObjectIdentity = ObjectIdentity
devConfiguration = _DevConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10)
)
_DevConfigComDiscTime_Type = Integer32
_DevConfigComDiscTime_Object = MibScalar
devConfigComDiscTime = _DevConfigComDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10, 1),
    _DevConfigComDiscTime_Type()
)
devConfigComDiscTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devConfigComDiscTime.setStatus("mandatory")


class _DevConfigPortNumDisplayFormat_Type(Integer32):
    """Custom type devConfigPortNumDisplayFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("name", 3),
          ("sle", 1),
          ("unitport", 2))
    )


_DevConfigPortNumDisplayFormat_Type.__name__ = "Integer32"
_DevConfigPortNumDisplayFormat_Object = MibScalar
devConfigPortNumDisplayFormat = _DevConfigPortNumDisplayFormat_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10, 2),
    _DevConfigPortNumDisplayFormat_Type()
)
devConfigPortNumDisplayFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devConfigPortNumDisplayFormat.setStatus("mandatory")


class _DevConfigDateDisplayFormat_Type(Integer32):
    """Custom type devConfigDateDisplayFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ddmmyy", 1),
          ("mmddyy", 2))
    )


_DevConfigDateDisplayFormat_Type.__name__ = "Integer32"
_DevConfigDateDisplayFormat_Object = MibScalar
devConfigDateDisplayFormat = _DevConfigDateDisplayFormat_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10, 3),
    _DevConfigDateDisplayFormat_Type()
)
devConfigDateDisplayFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devConfigDateDisplayFormat.setStatus("mandatory")


class _DevAcceptRemoteResetFrame_Type(Integer32):
    """Custom type devAcceptRemoteResetFrame based on Integer32"""
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


_DevAcceptRemoteResetFrame_Type.__name__ = "Integer32"
_DevAcceptRemoteResetFrame_Object = MibScalar
devAcceptRemoteResetFrame = _DevAcceptRemoteResetFrame_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10, 4),
    _DevAcceptRemoteResetFrame_Type()
)
devAcceptRemoteResetFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devAcceptRemoteResetFrame.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cCN = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 4, 0, 7)
)
cCN.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    cCN.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-CONFIG-MIB",
    **{"devConfigArea": devConfigArea,
       "devConfigAreaCopy": devConfigAreaCopy,
       "devConfigTestTimer": devConfigTestTimer,
       "devConfigTestTimeout": devConfigTestTimeout,
       "devConfigTestDuration": devConfigTestDuration,
       "devConfigClockSrc": devConfigClockSrc,
       "devConfigClockSrcTable": devConfigClockSrcTable,
       "devConfigClockSrcEntry": devConfigClockSrcEntry,
       "devCfgClkWhichSrc": devCfgClkWhichSrc,
       "devCfgClkSource": devCfgClkSource,
       "devCfgClkIfIndex": devCfgClkIfIndex,
       "devCfgClkRate": devCfgClkRate,
       "devConfigTrap": devConfigTrap,
       "cCN": cCN,
       "devConfigTrapEnable": devConfigTrapEnable,
       "cCNTrapEnable": cCNTrapEnable,
       "devConfigAlarm": devConfigAlarm,
       "devConfigAlarmRelayCutoff": devConfigAlarmRelayCutoff,
       "devConfigCardType": devConfigCardType,
       "devConfigCardTypeTable": devConfigCardTypeTable,
       "devConfigCardTypeEntry": devConfigCardTypeEntry,
       "devCfgCardSlot": devCfgCardSlot,
       "devCfgCardConfig": devCfgCardConfig,
       "devCfgCardActual": devCfgCardActual,
       "devCfgCardAction": devCfgCardAction,
       "devConfigNetSync": devConfigNetSync,
       "devConfigNetSyncRole": devConfigNetSyncRole,
       "devConfigTime": devConfigTime,
       "devConfigTimeOfDay": devConfigTimeOfDay,
       "devConfigChangeKeys": devConfigChangeKeys,
       "devConfigChangeKeysTable": devConfigChangeKeysTable,
       "devConfigChangeKeysEntry": devConfigChangeKeysEntry,
       "devConfigChangeKeysDbType": devConfigChangeKeysDbType,
       "devConfigChangeKeysDbKey": devConfigChangeKeysDbKey,
       "devConfiguration": devConfiguration,
       "devConfigComDiscTime": devConfigComDiscTime,
       "devConfigPortNumDisplayFormat": devConfigPortNumDisplayFormat,
       "devConfigDateDisplayFormat": devConfigDateDisplayFormat,
       "devAcceptRemoteResetFrame": devAcceptRemoteResetFrame}
)
