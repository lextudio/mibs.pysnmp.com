# SNMP MIB module (LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:19 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(TimeFilter,
 ZeroBasedCounter32) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter",
    "ZeroBasedCounter32")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

lldpMIB = ModuleIdentity(
    (1, 0, 8802, 1, 1, 2)
)
lldpMIB.setRevisions(
        ("2005-05-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LldpChassisIdSubtype(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("interfaceName", 6),
          ("local", 7),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("portComponent", 3))
    )



class LldpChassisId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class LldpPortIdSubtype(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("agentCircuitId", 6),
          ("interfaceAlias", 1),
          ("interfaceName", 5),
          ("local", 7),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("portComponent", 2))
    )



class LldpPortId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class LldpManAddrIfSubtype(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ifIndex", 2),
          ("systemPortNumber", 3),
          ("unknown", 1))
    )



class LldpManAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class LldpSystemCapabilitiesMap(Bits, TextualConvention):
    status = "current"


class LldpPortNumber(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class LldpPortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



# MIB Managed Objects in the order of their OIDs

_LldpNotifications_ObjectIdentity = ObjectIdentity
lldpNotifications = _LldpNotifications_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 0)
)
_LldpNotificationPrefix_ObjectIdentity = ObjectIdentity
lldpNotificationPrefix = _LldpNotificationPrefix_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 0, 0)
)
_LldpObjects_ObjectIdentity = ObjectIdentity
lldpObjects = _LldpObjects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1)
)
_LldpConfiguration_ObjectIdentity = ObjectIdentity
lldpConfiguration = _LldpConfiguration_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 1)
)


class _LldpMessageTxInterval_Type(Integer32):
    """Custom type lldpMessageTxInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_LldpMessageTxInterval_Type.__name__ = "Integer32"
_LldpMessageTxInterval_Object = MibScalar
lldpMessageTxInterval = _LldpMessageTxInterval_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 1),
    _LldpMessageTxInterval_Type()
)
lldpMessageTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMessageTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    lldpMessageTxInterval.setUnits("seconds")


class _LldpMessageTxHoldMultiplier_Type(Integer32):
    """Custom type lldpMessageTxHoldMultiplier based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_LldpMessageTxHoldMultiplier_Type.__name__ = "Integer32"
_LldpMessageTxHoldMultiplier_Object = MibScalar
lldpMessageTxHoldMultiplier = _LldpMessageTxHoldMultiplier_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 2),
    _LldpMessageTxHoldMultiplier_Type()
)
lldpMessageTxHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMessageTxHoldMultiplier.setStatus("current")


class _LldpReinitDelay_Type(Integer32):
    """Custom type lldpReinitDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LldpReinitDelay_Type.__name__ = "Integer32"
_LldpReinitDelay_Object = MibScalar
lldpReinitDelay = _LldpReinitDelay_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 3),
    _LldpReinitDelay_Type()
)
lldpReinitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpReinitDelay.setStatus("current")
if mibBuilder.loadTexts:
    lldpReinitDelay.setUnits("seconds")


class _LldpTxDelay_Type(Integer32):
    """Custom type lldpTxDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_LldpTxDelay_Type.__name__ = "Integer32"
_LldpTxDelay_Object = MibScalar
lldpTxDelay = _LldpTxDelay_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 4),
    _LldpTxDelay_Type()
)
lldpTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    lldpTxDelay.setUnits("seconds")


class _LldpNotificationInterval_Type(Integer32):
    """Custom type lldpNotificationInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_LldpNotificationInterval_Type.__name__ = "Integer32"
_LldpNotificationInterval_Object = MibScalar
lldpNotificationInterval = _LldpNotificationInterval_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 5),
    _LldpNotificationInterval_Type()
)
lldpNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    lldpNotificationInterval.setUnits("seconds")
_LldpPortConfigTable_Object = MibTable
lldpPortConfigTable = _LldpPortConfigTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    lldpPortConfigTable.setStatus("current")
_LldpPortConfigEntry_Object = MibTableRow
lldpPortConfigEntry = _LldpPortConfigEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 6, 1)
)
lldpPortConfigEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    lldpPortConfigEntry.setStatus("current")
_LldpPortConfigPortNum_Type = LldpPortNumber
_LldpPortConfigPortNum_Object = MibTableColumn
lldpPortConfigPortNum = _LldpPortConfigPortNum_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 1),
    _LldpPortConfigPortNum_Type()
)
lldpPortConfigPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpPortConfigPortNum.setStatus("current")


class _LldpPortConfigAdminStatus_Type(Integer32):
    """Custom type lldpPortConfigAdminStatus based on Integer32"""
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
        *(("disabled", 4),
          ("rxOnly", 2),
          ("txAndRx", 3),
          ("txOnly", 1))
    )


_LldpPortConfigAdminStatus_Type.__name__ = "Integer32"
_LldpPortConfigAdminStatus_Object = MibTableColumn
lldpPortConfigAdminStatus = _LldpPortConfigAdminStatus_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 2),
    _LldpPortConfigAdminStatus_Type()
)
lldpPortConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigAdminStatus.setStatus("current")


class _LldpPortConfigNotificationEnable_Type(TruthValue):
    """Custom type lldpPortConfigNotificationEnable based on TruthValue"""


_LldpPortConfigNotificationEnable_Object = MibTableColumn
lldpPortConfigNotificationEnable = _LldpPortConfigNotificationEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 3),
    _LldpPortConfigNotificationEnable_Type()
)
lldpPortConfigNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigNotificationEnable.setStatus("current")


class _LldpPortConfigTLVsTxEnable_Type(Bits):
    """Custom type lldpPortConfigTLVsTxEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("portDesc", 0),
          ("sysCap", 3),
          ("sysDesc", 2),
          ("sysName", 1))
    )

_LldpPortConfigTLVsTxEnable_Type.__name__ = "Bits"
_LldpPortConfigTLVsTxEnable_Object = MibTableColumn
lldpPortConfigTLVsTxEnable = _LldpPortConfigTLVsTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 4),
    _LldpPortConfigTLVsTxEnable_Type()
)
lldpPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigTLVsTxEnable.setStatus("current")
_LldpConfigManAddrTable_Object = MibTable
lldpConfigManAddrTable = _LldpConfigManAddrTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    lldpConfigManAddrTable.setStatus("current")
_LldpConfigManAddrEntry_Object = MibTableRow
lldpConfigManAddrEntry = _LldpConfigManAddrEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    lldpConfigManAddrEntry.setStatus("current")


class _LldpConfigManAddrPortsTxEnable_Type(LldpPortList):
    """Custom type lldpConfigManAddrPortsTxEnable based on LldpPortList"""
    defaultHexValue = ""


_LldpConfigManAddrPortsTxEnable_Object = MibTableColumn
lldpConfigManAddrPortsTxEnable = _LldpConfigManAddrPortsTxEnable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 1, 7, 1, 1),
    _LldpConfigManAddrPortsTxEnable_Type()
)
lldpConfigManAddrPortsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigManAddrPortsTxEnable.setStatus("current")
_LldpStatistics_ObjectIdentity = ObjectIdentity
lldpStatistics = _LldpStatistics_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 2)
)
_LldpStatsRemTablesLastChangeTime_Type = TimeStamp
_LldpStatsRemTablesLastChangeTime_Object = MibScalar
lldpStatsRemTablesLastChangeTime = _LldpStatsRemTablesLastChangeTime_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 1),
    _LldpStatsRemTablesLastChangeTime_Type()
)
lldpStatsRemTablesLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesLastChangeTime.setStatus("current")
_LldpStatsRemTablesInserts_Type = ZeroBasedCounter32
_LldpStatsRemTablesInserts_Object = MibScalar
lldpStatsRemTablesInserts = _LldpStatsRemTablesInserts_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 2),
    _LldpStatsRemTablesInserts_Type()
)
lldpStatsRemTablesInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesInserts.setStatus("current")
if mibBuilder.loadTexts:
    lldpStatsRemTablesInserts.setUnits("table entries")
_LldpStatsRemTablesDeletes_Type = ZeroBasedCounter32
_LldpStatsRemTablesDeletes_Object = MibScalar
lldpStatsRemTablesDeletes = _LldpStatsRemTablesDeletes_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 3),
    _LldpStatsRemTablesDeletes_Type()
)
lldpStatsRemTablesDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesDeletes.setStatus("current")
if mibBuilder.loadTexts:
    lldpStatsRemTablesDeletes.setUnits("table entries")
_LldpStatsRemTablesDrops_Type = ZeroBasedCounter32
_LldpStatsRemTablesDrops_Object = MibScalar
lldpStatsRemTablesDrops = _LldpStatsRemTablesDrops_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 4),
    _LldpStatsRemTablesDrops_Type()
)
lldpStatsRemTablesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesDrops.setStatus("current")
if mibBuilder.loadTexts:
    lldpStatsRemTablesDrops.setUnits("table entries")
_LldpStatsRemTablesAgeouts_Type = ZeroBasedCounter32
_LldpStatsRemTablesAgeouts_Object = MibScalar
lldpStatsRemTablesAgeouts = _LldpStatsRemTablesAgeouts_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 5),
    _LldpStatsRemTablesAgeouts_Type()
)
lldpStatsRemTablesAgeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesAgeouts.setStatus("current")
_LldpStatsTxPortTable_Object = MibTable
lldpStatsTxPortTable = _LldpStatsTxPortTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    lldpStatsTxPortTable.setStatus("current")
_LldpStatsTxPortEntry_Object = MibTableRow
lldpStatsTxPortEntry = _LldpStatsTxPortEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 6, 1)
)
lldpStatsTxPortEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpStatsTxPortNum"),
)
if mibBuilder.loadTexts:
    lldpStatsTxPortEntry.setStatus("current")
_LldpStatsTxPortNum_Type = LldpPortNumber
_LldpStatsTxPortNum_Object = MibTableColumn
lldpStatsTxPortNum = _LldpStatsTxPortNum_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 6, 1, 1),
    _LldpStatsTxPortNum_Type()
)
lldpStatsTxPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpStatsTxPortNum.setStatus("current")
_LldpStatsTxPortFramesTotal_Type = Counter32
_LldpStatsTxPortFramesTotal_Object = MibTableColumn
lldpStatsTxPortFramesTotal = _LldpStatsTxPortFramesTotal_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 6, 1, 2),
    _LldpStatsTxPortFramesTotal_Type()
)
lldpStatsTxPortFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsTxPortFramesTotal.setStatus("current")
_LldpStatsRxPortTable_Object = MibTable
lldpStatsRxPortTable = _LldpStatsRxPortTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    lldpStatsRxPortTable.setStatus("current")
_LldpStatsRxPortEntry_Object = MibTableRow
lldpStatsRxPortEntry = _LldpStatsRxPortEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 7, 1)
)
lldpStatsRxPortEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpStatsRxPortNum"),
)
if mibBuilder.loadTexts:
    lldpStatsRxPortEntry.setStatus("current")
_LldpStatsRxPortNum_Type = LldpPortNumber
_LldpStatsRxPortNum_Object = MibTableColumn
lldpStatsRxPortNum = _LldpStatsRxPortNum_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 1),
    _LldpStatsRxPortNum_Type()
)
lldpStatsRxPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpStatsRxPortNum.setStatus("current")
_LldpStatsRxPortFramesDiscardedTotal_Type = Counter32
_LldpStatsRxPortFramesDiscardedTotal_Object = MibTableColumn
lldpStatsRxPortFramesDiscardedTotal = _LldpStatsRxPortFramesDiscardedTotal_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 2),
    _LldpStatsRxPortFramesDiscardedTotal_Type()
)
lldpStatsRxPortFramesDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortFramesDiscardedTotal.setStatus("current")
_LldpStatsRxPortFramesErrors_Type = Counter32
_LldpStatsRxPortFramesErrors_Object = MibTableColumn
lldpStatsRxPortFramesErrors = _LldpStatsRxPortFramesErrors_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 3),
    _LldpStatsRxPortFramesErrors_Type()
)
lldpStatsRxPortFramesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortFramesErrors.setStatus("current")
_LldpStatsRxPortFramesTotal_Type = Counter32
_LldpStatsRxPortFramesTotal_Object = MibTableColumn
lldpStatsRxPortFramesTotal = _LldpStatsRxPortFramesTotal_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 4),
    _LldpStatsRxPortFramesTotal_Type()
)
lldpStatsRxPortFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortFramesTotal.setStatus("current")
_LldpStatsRxPortTLVsDiscardedTotal_Type = Counter32
_LldpStatsRxPortTLVsDiscardedTotal_Object = MibTableColumn
lldpStatsRxPortTLVsDiscardedTotal = _LldpStatsRxPortTLVsDiscardedTotal_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 5),
    _LldpStatsRxPortTLVsDiscardedTotal_Type()
)
lldpStatsRxPortTLVsDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortTLVsDiscardedTotal.setStatus("current")
_LldpStatsRxPortTLVsUnrecognizedTotal_Type = Counter32
_LldpStatsRxPortTLVsUnrecognizedTotal_Object = MibTableColumn
lldpStatsRxPortTLVsUnrecognizedTotal = _LldpStatsRxPortTLVsUnrecognizedTotal_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 6),
    _LldpStatsRxPortTLVsUnrecognizedTotal_Type()
)
lldpStatsRxPortTLVsUnrecognizedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortTLVsUnrecognizedTotal.setStatus("current")
_LldpStatsRxPortAgeoutsTotal_Type = ZeroBasedCounter32
_LldpStatsRxPortAgeoutsTotal_Object = MibTableColumn
lldpStatsRxPortAgeoutsTotal = _LldpStatsRxPortAgeoutsTotal_Object(
    (1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 7),
    _LldpStatsRxPortAgeoutsTotal_Type()
)
lldpStatsRxPortAgeoutsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortAgeoutsTotal.setStatus("current")
_LldpLocalSystemData_ObjectIdentity = ObjectIdentity
lldpLocalSystemData = _LldpLocalSystemData_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 3)
)
_LldpLocChassisIdSubtype_Type = LldpChassisIdSubtype
_LldpLocChassisIdSubtype_Object = MibScalar
lldpLocChassisIdSubtype = _LldpLocChassisIdSubtype_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 1),
    _LldpLocChassisIdSubtype_Type()
)
lldpLocChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocChassisIdSubtype.setStatus("current")
_LldpLocChassisId_Type = LldpChassisId
_LldpLocChassisId_Object = MibScalar
lldpLocChassisId = _LldpLocChassisId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 2),
    _LldpLocChassisId_Type()
)
lldpLocChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocChassisId.setStatus("current")


class _LldpLocSysName_Type(SnmpAdminString):
    """Custom type lldpLocSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocSysName_Type.__name__ = "SnmpAdminString"
_LldpLocSysName_Object = MibScalar
lldpLocSysName = _LldpLocSysName_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 3),
    _LldpLocSysName_Type()
)
lldpLocSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocSysName.setStatus("current")


class _LldpLocSysDesc_Type(SnmpAdminString):
    """Custom type lldpLocSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocSysDesc_Type.__name__ = "SnmpAdminString"
_LldpLocSysDesc_Object = MibScalar
lldpLocSysDesc = _LldpLocSysDesc_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 4),
    _LldpLocSysDesc_Type()
)
lldpLocSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocSysDesc.setStatus("current")
_LldpLocSysCapSupported_Type = LldpSystemCapabilitiesMap
_LldpLocSysCapSupported_Object = MibScalar
lldpLocSysCapSupported = _LldpLocSysCapSupported_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 5),
    _LldpLocSysCapSupported_Type()
)
lldpLocSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocSysCapSupported.setStatus("current")
_LldpLocSysCapEnabled_Type = LldpSystemCapabilitiesMap
_LldpLocSysCapEnabled_Object = MibScalar
lldpLocSysCapEnabled = _LldpLocSysCapEnabled_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 6),
    _LldpLocSysCapEnabled_Type()
)
lldpLocSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocSysCapEnabled.setStatus("current")
_LldpLocPortTable_Object = MibTable
lldpLocPortTable = _LldpLocPortTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    lldpLocPortTable.setStatus("current")
_LldpLocPortEntry_Object = MibTableRow
lldpLocPortEntry = _LldpLocPortEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 7, 1)
)
lldpLocPortEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpLocPortEntry.setStatus("current")
_LldpLocPortNum_Type = LldpPortNumber
_LldpLocPortNum_Object = MibTableColumn
lldpLocPortNum = _LldpLocPortNum_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 1),
    _LldpLocPortNum_Type()
)
lldpLocPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpLocPortNum.setStatus("current")
_LldpLocPortIdSubtype_Type = LldpPortIdSubtype
_LldpLocPortIdSubtype_Object = MibTableColumn
lldpLocPortIdSubtype = _LldpLocPortIdSubtype_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 2),
    _LldpLocPortIdSubtype_Type()
)
lldpLocPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocPortIdSubtype.setStatus("current")
_LldpLocPortId_Type = LldpPortId
_LldpLocPortId_Object = MibTableColumn
lldpLocPortId = _LldpLocPortId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 3),
    _LldpLocPortId_Type()
)
lldpLocPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocPortId.setStatus("current")


class _LldpLocPortDesc_Type(SnmpAdminString):
    """Custom type lldpLocPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocPortDesc_Type.__name__ = "SnmpAdminString"
_LldpLocPortDesc_Object = MibTableColumn
lldpLocPortDesc = _LldpLocPortDesc_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 4),
    _LldpLocPortDesc_Type()
)
lldpLocPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocPortDesc.setStatus("current")
_LldpLocManAddrTable_Object = MibTable
lldpLocManAddrTable = _LldpLocManAddrTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 8)
)
if mibBuilder.loadTexts:
    lldpLocManAddrTable.setStatus("current")
_LldpLocManAddrEntry_Object = MibTableRow
lldpLocManAddrEntry = _LldpLocManAddrEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 8, 1)
)
lldpLocManAddrEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpLocManAddrSubtype"),
    (0, "LLDP-MIB", "lldpLocManAddr"),
)
if mibBuilder.loadTexts:
    lldpLocManAddrEntry.setStatus("current")
_LldpLocManAddrSubtype_Type = AddressFamilyNumbers
_LldpLocManAddrSubtype_Object = MibTableColumn
lldpLocManAddrSubtype = _LldpLocManAddrSubtype_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 1),
    _LldpLocManAddrSubtype_Type()
)
lldpLocManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpLocManAddrSubtype.setStatus("current")
_LldpLocManAddr_Type = LldpManAddress
_LldpLocManAddr_Object = MibTableColumn
lldpLocManAddr = _LldpLocManAddr_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 2),
    _LldpLocManAddr_Type()
)
lldpLocManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpLocManAddr.setStatus("current")
_LldpLocManAddrLen_Type = Integer32
_LldpLocManAddrLen_Object = MibTableColumn
lldpLocManAddrLen = _LldpLocManAddrLen_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 3),
    _LldpLocManAddrLen_Type()
)
lldpLocManAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrLen.setStatus("current")
_LldpLocManAddrIfSubtype_Type = LldpManAddrIfSubtype
_LldpLocManAddrIfSubtype_Object = MibTableColumn
lldpLocManAddrIfSubtype = _LldpLocManAddrIfSubtype_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 4),
    _LldpLocManAddrIfSubtype_Type()
)
lldpLocManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrIfSubtype.setStatus("current")
_LldpLocManAddrIfId_Type = Integer32
_LldpLocManAddrIfId_Object = MibTableColumn
lldpLocManAddrIfId = _LldpLocManAddrIfId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 5),
    _LldpLocManAddrIfId_Type()
)
lldpLocManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrIfId.setStatus("current")
_LldpLocManAddrOID_Type = ObjectIdentifier
_LldpLocManAddrOID_Object = MibTableColumn
lldpLocManAddrOID = _LldpLocManAddrOID_Object(
    (1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 6),
    _LldpLocManAddrOID_Type()
)
lldpLocManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrOID.setStatus("current")
_LldpRemoteSystemsData_ObjectIdentity = ObjectIdentity
lldpRemoteSystemsData = _LldpRemoteSystemsData_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 4)
)
_LldpRemTable_Object = MibTable
lldpRemTable = _LldpRemTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lldpRemTable.setStatus("current")
_LldpRemEntry_Object = MibTableRow
lldpRemEntry = _LldpRemEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1)
)
lldpRemEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpRemEntry.setStatus("current")
_LldpRemTimeMark_Type = TimeFilter
_LldpRemTimeMark_Object = MibTableColumn
lldpRemTimeMark = _LldpRemTimeMark_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 1),
    _LldpRemTimeMark_Type()
)
lldpRemTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemTimeMark.setStatus("current")
_LldpRemLocalPortNum_Type = LldpPortNumber
_LldpRemLocalPortNum_Object = MibTableColumn
lldpRemLocalPortNum = _LldpRemLocalPortNum_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 2),
    _LldpRemLocalPortNum_Type()
)
lldpRemLocalPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemLocalPortNum.setStatus("current")


class _LldpRemIndex_Type(Integer32):
    """Custom type lldpRemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpRemIndex_Type.__name__ = "Integer32"
_LldpRemIndex_Object = MibTableColumn
lldpRemIndex = _LldpRemIndex_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 3),
    _LldpRemIndex_Type()
)
lldpRemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemIndex.setStatus("current")
_LldpRemChassisIdSubtype_Type = LldpChassisIdSubtype
_LldpRemChassisIdSubtype_Object = MibTableColumn
lldpRemChassisIdSubtype = _LldpRemChassisIdSubtype_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 4),
    _LldpRemChassisIdSubtype_Type()
)
lldpRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemChassisIdSubtype.setStatus("current")
_LldpRemChassisId_Type = LldpChassisId
_LldpRemChassisId_Object = MibTableColumn
lldpRemChassisId = _LldpRemChassisId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 5),
    _LldpRemChassisId_Type()
)
lldpRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemChassisId.setStatus("current")
_LldpRemPortIdSubtype_Type = LldpPortIdSubtype
_LldpRemPortIdSubtype_Object = MibTableColumn
lldpRemPortIdSubtype = _LldpRemPortIdSubtype_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 6),
    _LldpRemPortIdSubtype_Type()
)
lldpRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemPortIdSubtype.setStatus("current")
_LldpRemPortId_Type = LldpPortId
_LldpRemPortId_Object = MibTableColumn
lldpRemPortId = _LldpRemPortId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 7),
    _LldpRemPortId_Type()
)
lldpRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemPortId.setStatus("current")


class _LldpRemPortDesc_Type(SnmpAdminString):
    """Custom type lldpRemPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemPortDesc_Type.__name__ = "SnmpAdminString"
_LldpRemPortDesc_Object = MibTableColumn
lldpRemPortDesc = _LldpRemPortDesc_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 8),
    _LldpRemPortDesc_Type()
)
lldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemPortDesc.setStatus("current")


class _LldpRemSysName_Type(SnmpAdminString):
    """Custom type lldpRemSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemSysName_Type.__name__ = "SnmpAdminString"
_LldpRemSysName_Object = MibTableColumn
lldpRemSysName = _LldpRemSysName_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 9),
    _LldpRemSysName_Type()
)
lldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysName.setStatus("current")


class _LldpRemSysDesc_Type(SnmpAdminString):
    """Custom type lldpRemSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemSysDesc_Type.__name__ = "SnmpAdminString"
_LldpRemSysDesc_Object = MibTableColumn
lldpRemSysDesc = _LldpRemSysDesc_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 10),
    _LldpRemSysDesc_Type()
)
lldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysDesc.setStatus("current")
_LldpRemSysCapSupported_Type = LldpSystemCapabilitiesMap
_LldpRemSysCapSupported_Object = MibTableColumn
lldpRemSysCapSupported = _LldpRemSysCapSupported_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 11),
    _LldpRemSysCapSupported_Type()
)
lldpRemSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysCapSupported.setStatus("current")
_LldpRemSysCapEnabled_Type = LldpSystemCapabilitiesMap
_LldpRemSysCapEnabled_Object = MibTableColumn
lldpRemSysCapEnabled = _LldpRemSysCapEnabled_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 12),
    _LldpRemSysCapEnabled_Type()
)
lldpRemSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysCapEnabled.setStatus("current")
_LldpRemManAddrTable_Object = MibTable
lldpRemManAddrTable = _LldpRemManAddrTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    lldpRemManAddrTable.setStatus("current")
_LldpRemManAddrEntry_Object = MibTableRow
lldpRemManAddrEntry = _LldpRemManAddrEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 2, 1)
)
lldpRemManAddrEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
    (0, "LLDP-MIB", "lldpRemManAddrSubtype"),
    (0, "LLDP-MIB", "lldpRemManAddr"),
)
if mibBuilder.loadTexts:
    lldpRemManAddrEntry.setStatus("current")
_LldpRemManAddrSubtype_Type = AddressFamilyNumbers
_LldpRemManAddrSubtype_Object = MibTableColumn
lldpRemManAddrSubtype = _LldpRemManAddrSubtype_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 1),
    _LldpRemManAddrSubtype_Type()
)
lldpRemManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemManAddrSubtype.setStatus("current")
_LldpRemManAddr_Type = LldpManAddress
_LldpRemManAddr_Object = MibTableColumn
lldpRemManAddr = _LldpRemManAddr_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 2),
    _LldpRemManAddr_Type()
)
lldpRemManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemManAddr.setStatus("current")
_LldpRemManAddrIfSubtype_Type = LldpManAddrIfSubtype
_LldpRemManAddrIfSubtype_Object = MibTableColumn
lldpRemManAddrIfSubtype = _LldpRemManAddrIfSubtype_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 3),
    _LldpRemManAddrIfSubtype_Type()
)
lldpRemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddrIfSubtype.setStatus("current")
_LldpRemManAddrIfId_Type = Integer32
_LldpRemManAddrIfId_Object = MibTableColumn
lldpRemManAddrIfId = _LldpRemManAddrIfId_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 4),
    _LldpRemManAddrIfId_Type()
)
lldpRemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddrIfId.setStatus("current")
_LldpRemManAddrOID_Type = ObjectIdentifier
_LldpRemManAddrOID_Object = MibTableColumn
lldpRemManAddrOID = _LldpRemManAddrOID_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 5),
    _LldpRemManAddrOID_Type()
)
lldpRemManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddrOID.setStatus("current")
_LldpRemUnknownTLVTable_Object = MibTable
lldpRemUnknownTLVTable = _LldpRemUnknownTLVTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    lldpRemUnknownTLVTable.setStatus("current")
_LldpRemUnknownTLVEntry_Object = MibTableRow
lldpRemUnknownTLVEntry = _LldpRemUnknownTLVEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 3, 1)
)
lldpRemUnknownTLVEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
    (0, "LLDP-MIB", "lldpRemUnknownTLVType"),
)
if mibBuilder.loadTexts:
    lldpRemUnknownTLVEntry.setStatus("current")


class _LldpRemUnknownTLVType_Type(Integer32):
    """Custom type lldpRemUnknownTLVType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 126),
    )


_LldpRemUnknownTLVType_Type.__name__ = "Integer32"
_LldpRemUnknownTLVType_Object = MibTableColumn
lldpRemUnknownTLVType = _LldpRemUnknownTLVType_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 3, 1, 1),
    _LldpRemUnknownTLVType_Type()
)
lldpRemUnknownTLVType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemUnknownTLVType.setStatus("current")


class _LldpRemUnknownTLVInfo_Type(OctetString):
    """Custom type lldpRemUnknownTLVInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_LldpRemUnknownTLVInfo_Type.__name__ = "OctetString"
_LldpRemUnknownTLVInfo_Object = MibTableColumn
lldpRemUnknownTLVInfo = _LldpRemUnknownTLVInfo_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 3, 1, 2),
    _LldpRemUnknownTLVInfo_Type()
)
lldpRemUnknownTLVInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemUnknownTLVInfo.setStatus("current")
_LldpRemOrgDefInfoTable_Object = MibTable
lldpRemOrgDefInfoTable = _LldpRemOrgDefInfoTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    lldpRemOrgDefInfoTable.setStatus("current")
_LldpRemOrgDefInfoEntry_Object = MibTableRow
lldpRemOrgDefInfoEntry = _LldpRemOrgDefInfoEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 4, 1)
)
lldpRemOrgDefInfoEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
    (0, "LLDP-MIB", "lldpRemOrgDefInfoOUI"),
    (0, "LLDP-MIB", "lldpRemOrgDefInfoSubtype"),
    (0, "LLDP-MIB", "lldpRemOrgDefInfoIndex"),
)
if mibBuilder.loadTexts:
    lldpRemOrgDefInfoEntry.setStatus("current")


class _LldpRemOrgDefInfoOUI_Type(OctetString):
    """Custom type lldpRemOrgDefInfoOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_LldpRemOrgDefInfoOUI_Type.__name__ = "OctetString"
_LldpRemOrgDefInfoOUI_Object = MibTableColumn
lldpRemOrgDefInfoOUI = _LldpRemOrgDefInfoOUI_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 1),
    _LldpRemOrgDefInfoOUI_Type()
)
lldpRemOrgDefInfoOUI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemOrgDefInfoOUI.setStatus("current")


class _LldpRemOrgDefInfoSubtype_Type(Integer32):
    """Custom type lldpRemOrgDefInfoSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LldpRemOrgDefInfoSubtype_Type.__name__ = "Integer32"
_LldpRemOrgDefInfoSubtype_Object = MibTableColumn
lldpRemOrgDefInfoSubtype = _LldpRemOrgDefInfoSubtype_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 2),
    _LldpRemOrgDefInfoSubtype_Type()
)
lldpRemOrgDefInfoSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemOrgDefInfoSubtype.setStatus("current")


class _LldpRemOrgDefInfoIndex_Type(Integer32):
    """Custom type lldpRemOrgDefInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpRemOrgDefInfoIndex_Type.__name__ = "Integer32"
_LldpRemOrgDefInfoIndex_Object = MibTableColumn
lldpRemOrgDefInfoIndex = _LldpRemOrgDefInfoIndex_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 3),
    _LldpRemOrgDefInfoIndex_Type()
)
lldpRemOrgDefInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpRemOrgDefInfoIndex.setStatus("current")


class _LldpRemOrgDefInfo_Type(OctetString):
    """Custom type lldpRemOrgDefInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 507),
    )


_LldpRemOrgDefInfo_Type.__name__ = "OctetString"
_LldpRemOrgDefInfo_Object = MibTableColumn
lldpRemOrgDefInfo = _LldpRemOrgDefInfo_Object(
    (1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 4),
    _LldpRemOrgDefInfo_Type()
)
lldpRemOrgDefInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemOrgDefInfo.setStatus("current")
_LldpExtensions_ObjectIdentity = ObjectIdentity
lldpExtensions = _LldpExtensions_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5)
)
_LldpConformance_ObjectIdentity = ObjectIdentity
lldpConformance = _LldpConformance_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 2)
)
_LldpCompliances_ObjectIdentity = ObjectIdentity
lldpCompliances = _LldpCompliances_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 2, 1)
)
_LldpGroups_ObjectIdentity = ObjectIdentity
lldpGroups = _LldpGroups_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 2, 2)
)
lldpLocManAddrEntry.registerAugmentions(
    ("LLDP-MIB",
     "lldpConfigManAddrEntry")
)
lldpConfigManAddrEntry.setIndexNames(*lldpLocManAddrEntry.getIndexNames())

# Managed Objects groups

lldpConfigGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 2, 2, 1)
)
lldpConfigGroup.setObjects(
    ("LLDP-MIB", "lldpPortConfigAdminStatus")
)
if mibBuilder.loadTexts:
    lldpConfigGroup.setStatus("current")

lldpConfigRxGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 2, 2, 2)
)
lldpConfigRxGroup.setObjects(
      *(("LLDP-MIB", "lldpNotificationInterval"),
        ("LLDP-MIB", "lldpPortConfigNotificationEnable"))
)
if mibBuilder.loadTexts:
    lldpConfigRxGroup.setStatus("current")

lldpConfigTxGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 2, 2, 3)
)
lldpConfigTxGroup.setObjects(
      *(("LLDP-MIB", "lldpMessageTxInterval"),
        ("LLDP-MIB", "lldpMessageTxHoldMultiplier"),
        ("LLDP-MIB", "lldpReinitDelay"),
        ("LLDP-MIB", "lldpTxDelay"),
        ("LLDP-MIB", "lldpPortConfigTLVsTxEnable"),
        ("LLDP-MIB", "lldpConfigManAddrPortsTxEnable"))
)
if mibBuilder.loadTexts:
    lldpConfigTxGroup.setStatus("current")

lldpStatsRxGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 2, 2, 4)
)
lldpStatsRxGroup.setObjects(
      *(("LLDP-MIB", "lldpStatsRemTablesLastChangeTime"),
        ("LLDP-MIB", "lldpStatsRemTablesInserts"),
        ("LLDP-MIB", "lldpStatsRemTablesDeletes"),
        ("LLDP-MIB", "lldpStatsRemTablesDrops"),
        ("LLDP-MIB", "lldpStatsRemTablesAgeouts"),
        ("LLDP-MIB", "lldpStatsRxPortFramesDiscardedTotal"),
        ("LLDP-MIB", "lldpStatsRxPortFramesErrors"),
        ("LLDP-MIB", "lldpStatsRxPortFramesTotal"),
        ("LLDP-MIB", "lldpStatsRxPortTLVsDiscardedTotal"),
        ("LLDP-MIB", "lldpStatsRxPortTLVsUnrecognizedTotal"),
        ("LLDP-MIB", "lldpStatsRxPortAgeoutsTotal"))
)
if mibBuilder.loadTexts:
    lldpStatsRxGroup.setStatus("current")

lldpStatsTxGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 2, 2, 5)
)
lldpStatsTxGroup.setObjects(
    ("LLDP-MIB", "lldpStatsTxPortFramesTotal")
)
if mibBuilder.loadTexts:
    lldpStatsTxGroup.setStatus("current")

lldpLocSysGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 2, 2, 6)
)
lldpLocSysGroup.setObjects(
      *(("LLDP-MIB", "lldpLocChassisIdSubtype"),
        ("LLDP-MIB", "lldpLocChassisId"),
        ("LLDP-MIB", "lldpLocPortIdSubtype"),
        ("LLDP-MIB", "lldpLocPortId"),
        ("LLDP-MIB", "lldpLocPortDesc"),
        ("LLDP-MIB", "lldpLocSysDesc"),
        ("LLDP-MIB", "lldpLocSysName"),
        ("LLDP-MIB", "lldpLocSysCapSupported"),
        ("LLDP-MIB", "lldpLocSysCapEnabled"),
        ("LLDP-MIB", "lldpLocManAddrLen"),
        ("LLDP-MIB", "lldpLocManAddrIfSubtype"),
        ("LLDP-MIB", "lldpLocManAddrIfId"),
        ("LLDP-MIB", "lldpLocManAddrOID"))
)
if mibBuilder.loadTexts:
    lldpLocSysGroup.setStatus("current")

lldpRemSysGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 2, 2, 2, 7)
)
lldpRemSysGroup.setObjects(
      *(("LLDP-MIB", "lldpRemChassisIdSubtype"),
        ("LLDP-MIB", "lldpRemChassisId"),
        ("LLDP-MIB", "lldpRemPortIdSubtype"),
        ("LLDP-MIB", "lldpRemPortId"),
        ("LLDP-MIB", "lldpRemPortDesc"),
        ("LLDP-MIB", "lldpRemSysName"),
        ("LLDP-MIB", "lldpRemSysDesc"),
        ("LLDP-MIB", "lldpRemSysCapSupported"),
        ("LLDP-MIB", "lldpRemSysCapEnabled"),
        ("LLDP-MIB", "lldpRemManAddrIfSubtype"),
        ("LLDP-MIB", "lldpRemManAddrIfId"),
        ("LLDP-MIB", "lldpRemManAddrOID"),
        ("LLDP-MIB", "lldpRemUnknownTLVInfo"),
        ("LLDP-MIB", "lldpRemOrgDefInfo"))
)
if mibBuilder.loadTexts:
    lldpRemSysGroup.setStatus("current")


# Notification objects

lldpRemTablesChange = NotificationType(
    (1, 0, 8802, 1, 1, 2, 0, 0, 1)
)
lldpRemTablesChange.setObjects(
      *(("LLDP-MIB", "lldpStatsRemTablesInserts"),
        ("LLDP-MIB", "lldpStatsRemTablesDeletes"),
        ("LLDP-MIB", "lldpStatsRemTablesDrops"),
        ("LLDP-MIB", "lldpStatsRemTablesAgeouts"))
)
if mibBuilder.loadTexts:
    lldpRemTablesChange.setStatus(
        "current"
    )


# Notifications groups

lldpNotificationsGroup = NotificationGroup(
    (1, 0, 8802, 1, 1, 2, 2, 2, 8)
)
lldpNotificationsGroup.setObjects(
    ("LLDP-MIB", "lldpRemTablesChange")
)
if mibBuilder.loadTexts:
    lldpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lldpCompliance = ModuleCompliance(
    (1, 0, 8802, 1, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lldpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-MIB",
    **{"LldpChassisIdSubtype": LldpChassisIdSubtype,
       "LldpChassisId": LldpChassisId,
       "LldpPortIdSubtype": LldpPortIdSubtype,
       "LldpPortId": LldpPortId,
       "LldpManAddrIfSubtype": LldpManAddrIfSubtype,
       "LldpManAddress": LldpManAddress,
       "LldpSystemCapabilitiesMap": LldpSystemCapabilitiesMap,
       "LldpPortNumber": LldpPortNumber,
       "LldpPortList": LldpPortList,
       "lldpMIB": lldpMIB,
       "lldpNotifications": lldpNotifications,
       "lldpNotificationPrefix": lldpNotificationPrefix,
       "lldpRemTablesChange": lldpRemTablesChange,
       "lldpObjects": lldpObjects,
       "lldpConfiguration": lldpConfiguration,
       "lldpMessageTxInterval": lldpMessageTxInterval,
       "lldpMessageTxHoldMultiplier": lldpMessageTxHoldMultiplier,
       "lldpReinitDelay": lldpReinitDelay,
       "lldpTxDelay": lldpTxDelay,
       "lldpNotificationInterval": lldpNotificationInterval,
       "lldpPortConfigTable": lldpPortConfigTable,
       "lldpPortConfigEntry": lldpPortConfigEntry,
       "lldpPortConfigPortNum": lldpPortConfigPortNum,
       "lldpPortConfigAdminStatus": lldpPortConfigAdminStatus,
       "lldpPortConfigNotificationEnable": lldpPortConfigNotificationEnable,
       "lldpPortConfigTLVsTxEnable": lldpPortConfigTLVsTxEnable,
       "lldpConfigManAddrTable": lldpConfigManAddrTable,
       "lldpConfigManAddrEntry": lldpConfigManAddrEntry,
       "lldpConfigManAddrPortsTxEnable": lldpConfigManAddrPortsTxEnable,
       "lldpStatistics": lldpStatistics,
       "lldpStatsRemTablesLastChangeTime": lldpStatsRemTablesLastChangeTime,
       "lldpStatsRemTablesInserts": lldpStatsRemTablesInserts,
       "lldpStatsRemTablesDeletes": lldpStatsRemTablesDeletes,
       "lldpStatsRemTablesDrops": lldpStatsRemTablesDrops,
       "lldpStatsRemTablesAgeouts": lldpStatsRemTablesAgeouts,
       "lldpStatsTxPortTable": lldpStatsTxPortTable,
       "lldpStatsTxPortEntry": lldpStatsTxPortEntry,
       "lldpStatsTxPortNum": lldpStatsTxPortNum,
       "lldpStatsTxPortFramesTotal": lldpStatsTxPortFramesTotal,
       "lldpStatsRxPortTable": lldpStatsRxPortTable,
       "lldpStatsRxPortEntry": lldpStatsRxPortEntry,
       "lldpStatsRxPortNum": lldpStatsRxPortNum,
       "lldpStatsRxPortFramesDiscardedTotal": lldpStatsRxPortFramesDiscardedTotal,
       "lldpStatsRxPortFramesErrors": lldpStatsRxPortFramesErrors,
       "lldpStatsRxPortFramesTotal": lldpStatsRxPortFramesTotal,
       "lldpStatsRxPortTLVsDiscardedTotal": lldpStatsRxPortTLVsDiscardedTotal,
       "lldpStatsRxPortTLVsUnrecognizedTotal": lldpStatsRxPortTLVsUnrecognizedTotal,
       "lldpStatsRxPortAgeoutsTotal": lldpStatsRxPortAgeoutsTotal,
       "lldpLocalSystemData": lldpLocalSystemData,
       "lldpLocChassisIdSubtype": lldpLocChassisIdSubtype,
       "lldpLocChassisId": lldpLocChassisId,
       "lldpLocSysName": lldpLocSysName,
       "lldpLocSysDesc": lldpLocSysDesc,
       "lldpLocSysCapSupported": lldpLocSysCapSupported,
       "lldpLocSysCapEnabled": lldpLocSysCapEnabled,
       "lldpLocPortTable": lldpLocPortTable,
       "lldpLocPortEntry": lldpLocPortEntry,
       "lldpLocPortNum": lldpLocPortNum,
       "lldpLocPortIdSubtype": lldpLocPortIdSubtype,
       "lldpLocPortId": lldpLocPortId,
       "lldpLocPortDesc": lldpLocPortDesc,
       "lldpLocManAddrTable": lldpLocManAddrTable,
       "lldpLocManAddrEntry": lldpLocManAddrEntry,
       "lldpLocManAddrSubtype": lldpLocManAddrSubtype,
       "lldpLocManAddr": lldpLocManAddr,
       "lldpLocManAddrLen": lldpLocManAddrLen,
       "lldpLocManAddrIfSubtype": lldpLocManAddrIfSubtype,
       "lldpLocManAddrIfId": lldpLocManAddrIfId,
       "lldpLocManAddrOID": lldpLocManAddrOID,
       "lldpRemoteSystemsData": lldpRemoteSystemsData,
       "lldpRemTable": lldpRemTable,
       "lldpRemEntry": lldpRemEntry,
       "lldpRemTimeMark": lldpRemTimeMark,
       "lldpRemLocalPortNum": lldpRemLocalPortNum,
       "lldpRemIndex": lldpRemIndex,
       "lldpRemChassisIdSubtype": lldpRemChassisIdSubtype,
       "lldpRemChassisId": lldpRemChassisId,
       "lldpRemPortIdSubtype": lldpRemPortIdSubtype,
       "lldpRemPortId": lldpRemPortId,
       "lldpRemPortDesc": lldpRemPortDesc,
       "lldpRemSysName": lldpRemSysName,
       "lldpRemSysDesc": lldpRemSysDesc,
       "lldpRemSysCapSupported": lldpRemSysCapSupported,
       "lldpRemSysCapEnabled": lldpRemSysCapEnabled,
       "lldpRemManAddrTable": lldpRemManAddrTable,
       "lldpRemManAddrEntry": lldpRemManAddrEntry,
       "lldpRemManAddrSubtype": lldpRemManAddrSubtype,
       "lldpRemManAddr": lldpRemManAddr,
       "lldpRemManAddrIfSubtype": lldpRemManAddrIfSubtype,
       "lldpRemManAddrIfId": lldpRemManAddrIfId,
       "lldpRemManAddrOID": lldpRemManAddrOID,
       "lldpRemUnknownTLVTable": lldpRemUnknownTLVTable,
       "lldpRemUnknownTLVEntry": lldpRemUnknownTLVEntry,
       "lldpRemUnknownTLVType": lldpRemUnknownTLVType,
       "lldpRemUnknownTLVInfo": lldpRemUnknownTLVInfo,
       "lldpRemOrgDefInfoTable": lldpRemOrgDefInfoTable,
       "lldpRemOrgDefInfoEntry": lldpRemOrgDefInfoEntry,
       "lldpRemOrgDefInfoOUI": lldpRemOrgDefInfoOUI,
       "lldpRemOrgDefInfoSubtype": lldpRemOrgDefInfoSubtype,
       "lldpRemOrgDefInfoIndex": lldpRemOrgDefInfoIndex,
       "lldpRemOrgDefInfo": lldpRemOrgDefInfo,
       "lldpExtensions": lldpExtensions,
       "lldpConformance": lldpConformance,
       "lldpCompliances": lldpCompliances,
       "lldpCompliance": lldpCompliance,
       "lldpGroups": lldpGroups,
       "lldpConfigGroup": lldpConfigGroup,
       "lldpConfigRxGroup": lldpConfigRxGroup,
       "lldpConfigTxGroup": lldpConfigTxGroup,
       "lldpStatsRxGroup": lldpStatsRxGroup,
       "lldpStatsTxGroup": lldpStatsTxGroup,
       "lldpLocSysGroup": lldpLocSysGroup,
       "lldpRemSysGroup": lldpRemSysGroup,
       "lldpNotificationsGroup": lldpNotificationsGroup}
)
