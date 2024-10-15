# SNMP MIB module (WWP-LEOS-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-LLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:56 2024
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

(wwpModules,
 wwpModulesLeos) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosLldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26)
)
wwpLeosLldpMIB.setRevisions(
        ("2004-04-18 00:00",
         "2003-04-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TimeFilter(TimeTicks, TextualConvention):
    status = "deprecated"


class SnmpAdminString(OctetString, TextualConvention):
    status = "deprecated"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class WwpLeosLldpChassisIdType(Integer32, TextualConvention):
    status = "deprecated"
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
        *(("backplaneEntPhysicalAlias", 4),
          ("entPhysicalAlias", 1),
          ("ifAlias", 2),
          ("local", 7),
          ("macAddress", 5),
          ("networkAddress", 6),
          ("portEntPhysicalAlias", 3))
    )



class WwpLeosLldpChassisId(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class WwpLeosLldpPortIdType(Integer32, TextualConvention):
    status = "deprecated"
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
        *(("backplaneEntPhysicalAlias", 3),
          ("ifAlias", 1),
          ("local", 6),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("portEntPhysicalAlias", 2))
    )



class WwpLeosLldpPortId(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class WwpLeosLldpManAddrIfSubtype(Integer32, TextualConvention):
    status = "deprecated"
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



class WwpLeosLldpManAddress(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class WwpLeosLldpSystemCapabilitiesMap(Bits, TextualConvention):
    status = "deprecated"


class WwpLeosLldpPortNumber(Integer32, TextualConvention):
    status = "deprecated"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



class WwpLeosLldpPortList(OctetString, TextualConvention):
    status = "deprecated"


# MIB Managed Objects in the order of their OIDs

_WwpLeosLldpMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosLldpMIBObjects = _WwpLeosLldpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1)
)
_WwpLeosLldpConfiguration_ObjectIdentity = ObjectIdentity
wwpLeosLldpConfiguration = _WwpLeosLldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1)
)


class _WwpLeosLldpMessageTxInterval_Type(Integer32):
    """Custom type wwpLeosLldpMessageTxInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_WwpLeosLldpMessageTxInterval_Type.__name__ = "Integer32"
_WwpLeosLldpMessageTxInterval_Object = MibScalar
wwpLeosLldpMessageTxInterval = _WwpLeosLldpMessageTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 1),
    _WwpLeosLldpMessageTxInterval_Type()
)
wwpLeosLldpMessageTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLldpMessageTxInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    wwpLeosLldpMessageTxInterval.setUnits("seconds")


class _WwpLeosLldpMessageTxHoldMultiplier_Type(Integer32):
    """Custom type wwpLeosLldpMessageTxHoldMultiplier based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_WwpLeosLldpMessageTxHoldMultiplier_Type.__name__ = "Integer32"
_WwpLeosLldpMessageTxHoldMultiplier_Object = MibScalar
wwpLeosLldpMessageTxHoldMultiplier = _WwpLeosLldpMessageTxHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 2),
    _WwpLeosLldpMessageTxHoldMultiplier_Type()
)
wwpLeosLldpMessageTxHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLldpMessageTxHoldMultiplier.setStatus("deprecated")


class _WwpLeosLldpReinitDelay_Type(Integer32):
    """Custom type wwpLeosLldpReinitDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosLldpReinitDelay_Type.__name__ = "Integer32"
_WwpLeosLldpReinitDelay_Object = MibScalar
wwpLeosLldpReinitDelay = _WwpLeosLldpReinitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 3),
    _WwpLeosLldpReinitDelay_Type()
)
wwpLeosLldpReinitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLldpReinitDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    wwpLeosLldpReinitDelay.setUnits("seconds")


class _WwpLeosLldpTxDelay_Type(Integer32):
    """Custom type wwpLeosLldpTxDelay based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_WwpLeosLldpTxDelay_Type.__name__ = "Integer32"
_WwpLeosLldpTxDelay_Object = MibScalar
wwpLeosLldpTxDelay = _WwpLeosLldpTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 4),
    _WwpLeosLldpTxDelay_Type()
)
wwpLeosLldpTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLldpTxDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    wwpLeosLldpTxDelay.setUnits("seconds")
_WwpLeosLldpPortConfigTable_Object = MibTable
wwpLeosLldpPortConfigTable = _WwpLeosLldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosLldpPortConfigTable.setStatus("deprecated")
_WwpLeosLldpPortConfigEntry_Object = MibTableRow
wwpLeosLldpPortConfigEntry = _WwpLeosLldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1)
)
wwpLeosLldpPortConfigEntry.setIndexNames(
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    wwpLeosLldpPortConfigEntry.setStatus("deprecated")
_WwpLeosLldpPortConfigPortNum_Type = WwpLeosLldpPortNumber
_WwpLeosLldpPortConfigPortNum_Object = MibTableColumn
wwpLeosLldpPortConfigPortNum = _WwpLeosLldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1, 1),
    _WwpLeosLldpPortConfigPortNum_Type()
)
wwpLeosLldpPortConfigPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosLldpPortConfigPortNum.setStatus("deprecated")


class _WwpLeosLldpPortConfigAdminStatus_Type(Integer32):
    """Custom type wwpLeosLldpPortConfigAdminStatus based on Integer32"""
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


_WwpLeosLldpPortConfigAdminStatus_Type.__name__ = "Integer32"
_WwpLeosLldpPortConfigAdminStatus_Object = MibTableColumn
wwpLeosLldpPortConfigAdminStatus = _WwpLeosLldpPortConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1, 2),
    _WwpLeosLldpPortConfigAdminStatus_Type()
)
wwpLeosLldpPortConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLldpPortConfigAdminStatus.setStatus("deprecated")


class _WwpLeosLldpPortConfigTLVsTxEnable_Type(Bits):
    """Custom type wwpLeosLldpPortConfigTLVsTxEnable based on Bits"""
    defaultBinValue = "00001111"

    namedValues = NamedValues(
        *(("portDesc", 4),
          ("sysCap", 7),
          ("sysDesc", 6),
          ("sysName", 5))
    )

_WwpLeosLldpPortConfigTLVsTxEnable_Type.__name__ = "Bits"
_WwpLeosLldpPortConfigTLVsTxEnable_Object = MibTableColumn
wwpLeosLldpPortConfigTLVsTxEnable = _WwpLeosLldpPortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1, 3),
    _WwpLeosLldpPortConfigTLVsTxEnable_Type()
)
wwpLeosLldpPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLldpPortConfigTLVsTxEnable.setStatus("deprecated")
_WwpLeosLldpPortConfigStatsClear_Type = TruthValue
_WwpLeosLldpPortConfigStatsClear_Object = MibTableColumn
wwpLeosLldpPortConfigStatsClear = _WwpLeosLldpPortConfigStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1, 4),
    _WwpLeosLldpPortConfigStatsClear_Type()
)
wwpLeosLldpPortConfigStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLldpPortConfigStatsClear.setStatus("current")
_WwpLeosLldpPortConfigOperPortSpeed_Type = Unsigned32
_WwpLeosLldpPortConfigOperPortSpeed_Object = MibTableColumn
wwpLeosLldpPortConfigOperPortSpeed = _WwpLeosLldpPortConfigOperPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1, 5),
    _WwpLeosLldpPortConfigOperPortSpeed_Type()
)
wwpLeosLldpPortConfigOperPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpPortConfigOperPortSpeed.setStatus("current")
_WwpLeosLldpPortConfigReqPortSpeed_Type = Unsigned32
_WwpLeosLldpPortConfigReqPortSpeed_Object = MibTableColumn
wwpLeosLldpPortConfigReqPortSpeed = _WwpLeosLldpPortConfigReqPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1, 6),
    _WwpLeosLldpPortConfigReqPortSpeed_Type()
)
wwpLeosLldpPortConfigReqPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpPortConfigReqPortSpeed.setStatus("current")
_WwpLeosLldpConfigManAddrTable_Object = MibTable
wwpLeosLldpConfigManAddrTable = _WwpLeosLldpConfigManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpLeosLldpConfigManAddrTable.setStatus("deprecated")
_WwpLeosLldpConfigManAddrEntry_Object = MibTableRow
wwpLeosLldpConfigManAddrEntry = _WwpLeosLldpConfigManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    wwpLeosLldpConfigManAddrEntry.setStatus("deprecated")
_WwpLeosLldpManAddrPortsTxEnable_Type = WwpLeosLldpPortList
_WwpLeosLldpManAddrPortsTxEnable_Object = MibTableColumn
wwpLeosLldpManAddrPortsTxEnable = _WwpLeosLldpManAddrPortsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 6, 1, 1),
    _WwpLeosLldpManAddrPortsTxEnable_Type()
)
wwpLeosLldpManAddrPortsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLldpManAddrPortsTxEnable.setStatus("deprecated")
_WwpLeosLldpStatistics_ObjectIdentity = ObjectIdentity
wwpLeosLldpStatistics = _WwpLeosLldpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2)
)
_WwpLeosLldpStatsTable_Object = MibTable
wwpLeosLldpStatsTable = _WwpLeosLldpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosLldpStatsTable.setStatus("deprecated")
_WwpLeosLldpStatsEntry_Object = MibTableRow
wwpLeosLldpStatsEntry = _WwpLeosLldpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1)
)
wwpLeosLldpStatsEntry.setIndexNames(
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsPortNum"),
)
if mibBuilder.loadTexts:
    wwpLeosLldpStatsEntry.setStatus("deprecated")
_WwpLeosLldpStatsPortNum_Type = WwpLeosLldpPortNumber
_WwpLeosLldpStatsPortNum_Object = MibTableColumn
wwpLeosLldpStatsPortNum = _WwpLeosLldpStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 1),
    _WwpLeosLldpStatsPortNum_Type()
)
wwpLeosLldpStatsPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpStatsPortNum.setStatus("deprecated")
_WwpLeosLldpStatsFramesDiscardedTotal_Type = Counter32
_WwpLeosLldpStatsFramesDiscardedTotal_Object = MibTableColumn
wwpLeosLldpStatsFramesDiscardedTotal = _WwpLeosLldpStatsFramesDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 2),
    _WwpLeosLldpStatsFramesDiscardedTotal_Type()
)
wwpLeosLldpStatsFramesDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpStatsFramesDiscardedTotal.setStatus("deprecated")
_WwpLeosLldpStatsFramesInErrors_Type = Counter32
_WwpLeosLldpStatsFramesInErrors_Object = MibTableColumn
wwpLeosLldpStatsFramesInErrors = _WwpLeosLldpStatsFramesInErrors_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 3),
    _WwpLeosLldpStatsFramesInErrors_Type()
)
wwpLeosLldpStatsFramesInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpStatsFramesInErrors.setStatus("deprecated")
_WwpLeosLldpStatsFramesInTotal_Type = Counter32
_WwpLeosLldpStatsFramesInTotal_Object = MibTableColumn
wwpLeosLldpStatsFramesInTotal = _WwpLeosLldpStatsFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 4),
    _WwpLeosLldpStatsFramesInTotal_Type()
)
wwpLeosLldpStatsFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpStatsFramesInTotal.setStatus("deprecated")
_WwpLeosLldpStatsFramesOutTotal_Type = Counter32
_WwpLeosLldpStatsFramesOutTotal_Object = MibTableColumn
wwpLeosLldpStatsFramesOutTotal = _WwpLeosLldpStatsFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 5),
    _WwpLeosLldpStatsFramesOutTotal_Type()
)
wwpLeosLldpStatsFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpStatsFramesOutTotal.setStatus("deprecated")
_WwpLeosLldpStatsTLVsInErrors_Type = Counter32
_WwpLeosLldpStatsTLVsInErrors_Object = MibTableColumn
wwpLeosLldpStatsTLVsInErrors = _WwpLeosLldpStatsTLVsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 6),
    _WwpLeosLldpStatsTLVsInErrors_Type()
)
wwpLeosLldpStatsTLVsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpStatsTLVsInErrors.setStatus("deprecated")
_WwpLeosLldpStatsTLVsDiscardedTotal_Type = Counter32
_WwpLeosLldpStatsTLVsDiscardedTotal_Object = MibTableColumn
wwpLeosLldpStatsTLVsDiscardedTotal = _WwpLeosLldpStatsTLVsDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 7),
    _WwpLeosLldpStatsTLVsDiscardedTotal_Type()
)
wwpLeosLldpStatsTLVsDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpStatsTLVsDiscardedTotal.setStatus("deprecated")
_WwpLeosLldpStatsTLVsUnrecognizedTotal_Type = Counter32
_WwpLeosLldpStatsTLVsUnrecognizedTotal_Object = MibTableColumn
wwpLeosLldpStatsTLVsUnrecognizedTotal = _WwpLeosLldpStatsTLVsUnrecognizedTotal_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 8),
    _WwpLeosLldpStatsTLVsUnrecognizedTotal_Type()
)
wwpLeosLldpStatsTLVsUnrecognizedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpStatsTLVsUnrecognizedTotal.setStatus("deprecated")
_WwpLeosLldpCounterDiscontinuityTime_Type = TimeStamp
_WwpLeosLldpCounterDiscontinuityTime_Object = MibTableColumn
wwpLeosLldpCounterDiscontinuityTime = _WwpLeosLldpCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 9),
    _WwpLeosLldpCounterDiscontinuityTime_Type()
)
wwpLeosLldpCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpCounterDiscontinuityTime.setStatus("deprecated")
_WwpLeosLldpLocalSystemData_ObjectIdentity = ObjectIdentity
wwpLeosLldpLocalSystemData = _WwpLeosLldpLocalSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3)
)
_WwpLeosLldpLocChassisType_Type = WwpLeosLldpChassisIdType
_WwpLeosLldpLocChassisType_Object = MibScalar
wwpLeosLldpLocChassisType = _WwpLeosLldpLocChassisType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 1),
    _WwpLeosLldpLocChassisType_Type()
)
wwpLeosLldpLocChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpLocChassisType.setStatus("deprecated")
_WwpLeosLldpLocChassisId_Type = WwpLeosLldpChassisId
_WwpLeosLldpLocChassisId_Object = MibScalar
wwpLeosLldpLocChassisId = _WwpLeosLldpLocChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 2),
    _WwpLeosLldpLocChassisId_Type()
)
wwpLeosLldpLocChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpLocChassisId.setStatus("deprecated")


class _WwpLeosLldpLocSysName_Type(SnmpAdminString):
    """Custom type wwpLeosLldpLocSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpLeosLldpLocSysName_Type.__name__ = "SnmpAdminString"
_WwpLeosLldpLocSysName_Object = MibScalar
wwpLeosLldpLocSysName = _WwpLeosLldpLocSysName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 3),
    _WwpLeosLldpLocSysName_Type()
)
wwpLeosLldpLocSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpLocSysName.setStatus("deprecated")


class _WwpLeosLldpLocSysDesc_Type(SnmpAdminString):
    """Custom type wwpLeosLldpLocSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpLeosLldpLocSysDesc_Type.__name__ = "SnmpAdminString"
_WwpLeosLldpLocSysDesc_Object = MibScalar
wwpLeosLldpLocSysDesc = _WwpLeosLldpLocSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 4),
    _WwpLeosLldpLocSysDesc_Type()
)
wwpLeosLldpLocSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpLocSysDesc.setStatus("deprecated")
_WwpLeosLldpLocSysCapSupported_Type = WwpLeosLldpSystemCapabilitiesMap
_WwpLeosLldpLocSysCapSupported_Object = MibScalar
wwpLeosLldpLocSysCapSupported = _WwpLeosLldpLocSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 5),
    _WwpLeosLldpLocSysCapSupported_Type()
)
wwpLeosLldpLocSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpLocSysCapSupported.setStatus("deprecated")
_WwpLeosLldpLocSysCapEnabled_Type = WwpLeosLldpSystemCapabilitiesMap
_WwpLeosLldpLocSysCapEnabled_Object = MibScalar
wwpLeosLldpLocSysCapEnabled = _WwpLeosLldpLocSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 6),
    _WwpLeosLldpLocSysCapEnabled_Type()
)
wwpLeosLldpLocSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpLocSysCapEnabled.setStatus("deprecated")
_WwpLeosLldpLocPortTable_Object = MibTable
wwpLeosLldpLocPortTable = _WwpLeosLldpLocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 7)
)
if mibBuilder.loadTexts:
    wwpLeosLldpLocPortTable.setStatus("deprecated")
_WwpLeosLldpLocPortEntry_Object = MibTableRow
wwpLeosLldpLocPortEntry = _WwpLeosLldpLocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 7, 1)
)
wwpLeosLldpLocPortEntry.setIndexNames(
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocPortNum"),
)
if mibBuilder.loadTexts:
    wwpLeosLldpLocPortEntry.setStatus("deprecated")
_WwpLeosLldpLocPortNum_Type = WwpLeosLldpPortNumber
_WwpLeosLldpLocPortNum_Object = MibTableColumn
wwpLeosLldpLocPortNum = _WwpLeosLldpLocPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 7, 1, 1),
    _WwpLeosLldpLocPortNum_Type()
)
wwpLeosLldpLocPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpLocPortNum.setStatus("deprecated")
_WwpLeosLldpLocPortType_Type = WwpLeosLldpPortIdType
_WwpLeosLldpLocPortType_Object = MibTableColumn
wwpLeosLldpLocPortType = _WwpLeosLldpLocPortType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 7, 1, 2),
    _WwpLeosLldpLocPortType_Type()
)
wwpLeosLldpLocPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpLocPortType.setStatus("deprecated")
_WwpLeosLldpLocPortId_Type = WwpLeosLldpPortId
_WwpLeosLldpLocPortId_Object = MibTableColumn
wwpLeosLldpLocPortId = _WwpLeosLldpLocPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 7, 1, 3),
    _WwpLeosLldpLocPortId_Type()
)
wwpLeosLldpLocPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpLocPortId.setStatus("deprecated")


class _WwpLeosLldpLocPortDesc_Type(SnmpAdminString):
    """Custom type wwpLeosLldpLocPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpLeosLldpLocPortDesc_Type.__name__ = "SnmpAdminString"
_WwpLeosLldpLocPortDesc_Object = MibTableColumn
wwpLeosLldpLocPortDesc = _WwpLeosLldpLocPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 7, 1, 4),
    _WwpLeosLldpLocPortDesc_Type()
)
wwpLeosLldpLocPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpLocPortDesc.setStatus("deprecated")
_WwpLeosLldpLocManAddrTable_Object = MibTable
wwpLeosLldpLocManAddrTable = _WwpLeosLldpLocManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8)
)
if mibBuilder.loadTexts:
    wwpLeosLldpLocManAddrTable.setStatus("deprecated")
_WwpLeosLldpLocManAddrEntry_Object = MibTableRow
wwpLeosLldpLocManAddrEntry = _WwpLeosLldpLocManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1)
)
wwpLeosLldpLocManAddrEntry.setIndexNames(
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocManAddrType"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocManAddr"),
)
if mibBuilder.loadTexts:
    wwpLeosLldpLocManAddrEntry.setStatus("deprecated")
_WwpLeosLldpLocManAddrType_Type = AddressFamilyNumbers
_WwpLeosLldpLocManAddrType_Object = MibTableColumn
wwpLeosLldpLocManAddrType = _WwpLeosLldpLocManAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1, 1),
    _WwpLeosLldpLocManAddrType_Type()
)
wwpLeosLldpLocManAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpLocManAddrType.setStatus("deprecated")
_WwpLeosLldpLocManAddr_Type = WwpLeosLldpManAddress
_WwpLeosLldpLocManAddr_Object = MibTableColumn
wwpLeosLldpLocManAddr = _WwpLeosLldpLocManAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1, 2),
    _WwpLeosLldpLocManAddr_Type()
)
wwpLeosLldpLocManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpLocManAddr.setStatus("deprecated")
_WwpLeosLldpLocManAddrLen_Type = Integer32
_WwpLeosLldpLocManAddrLen_Object = MibTableColumn
wwpLeosLldpLocManAddrLen = _WwpLeosLldpLocManAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1, 3),
    _WwpLeosLldpLocManAddrLen_Type()
)
wwpLeosLldpLocManAddrLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpLocManAddrLen.setStatus("deprecated")
_WwpLeosLldpLocManAddrIfSubtype_Type = WwpLeosLldpManAddrIfSubtype
_WwpLeosLldpLocManAddrIfSubtype_Object = MibTableColumn
wwpLeosLldpLocManAddrIfSubtype = _WwpLeosLldpLocManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1, 4),
    _WwpLeosLldpLocManAddrIfSubtype_Type()
)
wwpLeosLldpLocManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpLocManAddrIfSubtype.setStatus("deprecated")
_WwpLeosLldpLocManAddrIfId_Type = Integer32
_WwpLeosLldpLocManAddrIfId_Object = MibTableColumn
wwpLeosLldpLocManAddrIfId = _WwpLeosLldpLocManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1, 5),
    _WwpLeosLldpLocManAddrIfId_Type()
)
wwpLeosLldpLocManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpLocManAddrIfId.setStatus("deprecated")
_WwpLeosLldpLocManAddrOID_Type = ObjectIdentifier
_WwpLeosLldpLocManAddrOID_Object = MibTableColumn
wwpLeosLldpLocManAddrOID = _WwpLeosLldpLocManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1, 6),
    _WwpLeosLldpLocManAddrOID_Type()
)
wwpLeosLldpLocManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpLocManAddrOID.setStatus("deprecated")
_WwpLeosLldpRemoteSystemsData_ObjectIdentity = ObjectIdentity
wwpLeosLldpRemoteSystemsData = _WwpLeosLldpRemoteSystemsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4)
)
_WwpLeosLldpRemTable_Object = MibTable
wwpLeosLldpRemTable = _WwpLeosLldpRemTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wwpLeosLldpRemTable.setStatus("deprecated")
_WwpLeosLldpRemEntry_Object = MibTableRow
wwpLeosLldpRemEntry = _WwpLeosLldpRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1)
)
wwpLeosLldpRemEntry.setIndexNames(
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemTimeMark"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemLocalPortNum"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosLldpRemEntry.setStatus("deprecated")
_WwpLeosLldpRemTimeMark_Type = TimeFilter
_WwpLeosLldpRemTimeMark_Object = MibTableColumn
wwpLeosLldpRemTimeMark = _WwpLeosLldpRemTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 1),
    _WwpLeosLldpRemTimeMark_Type()
)
wwpLeosLldpRemTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpRemTimeMark.setStatus("deprecated")
_WwpLeosLldpRemLocalPortNum_Type = WwpLeosLldpPortNumber
_WwpLeosLldpRemLocalPortNum_Object = MibTableColumn
wwpLeosLldpRemLocalPortNum = _WwpLeosLldpRemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 2),
    _WwpLeosLldpRemLocalPortNum_Type()
)
wwpLeosLldpRemLocalPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpRemLocalPortNum.setStatus("deprecated")


class _WwpLeosLldpRemIndex_Type(Integer32):
    """Custom type wwpLeosLldpRemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpLeosLldpRemIndex_Type.__name__ = "Integer32"
_WwpLeosLldpRemIndex_Object = MibTableColumn
wwpLeosLldpRemIndex = _WwpLeosLldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 3),
    _WwpLeosLldpRemIndex_Type()
)
wwpLeosLldpRemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpRemIndex.setStatus("deprecated")
_WwpLeosLldpRemRemoteChassisType_Type = WwpLeosLldpChassisIdType
_WwpLeosLldpRemRemoteChassisType_Object = MibTableColumn
wwpLeosLldpRemRemoteChassisType = _WwpLeosLldpRemRemoteChassisType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 4),
    _WwpLeosLldpRemRemoteChassisType_Type()
)
wwpLeosLldpRemRemoteChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemRemoteChassisType.setStatus("deprecated")
_WwpLeosLldpRemRemoteChassis_Type = WwpLeosLldpChassisId
_WwpLeosLldpRemRemoteChassis_Object = MibTableColumn
wwpLeosLldpRemRemoteChassis = _WwpLeosLldpRemRemoteChassis_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 5),
    _WwpLeosLldpRemRemoteChassis_Type()
)
wwpLeosLldpRemRemoteChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemRemoteChassis.setStatus("deprecated")
_WwpLeosLldpRemRemotePortType_Type = WwpLeosLldpPortIdType
_WwpLeosLldpRemRemotePortType_Object = MibTableColumn
wwpLeosLldpRemRemotePortType = _WwpLeosLldpRemRemotePortType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 6),
    _WwpLeosLldpRemRemotePortType_Type()
)
wwpLeosLldpRemRemotePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemRemotePortType.setStatus("deprecated")
_WwpLeosLldpRemRemotePort_Type = WwpLeosLldpPortId
_WwpLeosLldpRemRemotePort_Object = MibTableColumn
wwpLeosLldpRemRemotePort = _WwpLeosLldpRemRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 7),
    _WwpLeosLldpRemRemotePort_Type()
)
wwpLeosLldpRemRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemRemotePort.setStatus("deprecated")


class _WwpLeosLldpRemPortDesc_Type(SnmpAdminString):
    """Custom type wwpLeosLldpRemPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpLeosLldpRemPortDesc_Type.__name__ = "SnmpAdminString"
_WwpLeosLldpRemPortDesc_Object = MibTableColumn
wwpLeosLldpRemPortDesc = _WwpLeosLldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 8),
    _WwpLeosLldpRemPortDesc_Type()
)
wwpLeosLldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemPortDesc.setStatus("deprecated")


class _WwpLeosLldpRemSysName_Type(SnmpAdminString):
    """Custom type wwpLeosLldpRemSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpLeosLldpRemSysName_Type.__name__ = "SnmpAdminString"
_WwpLeosLldpRemSysName_Object = MibTableColumn
wwpLeosLldpRemSysName = _WwpLeosLldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 9),
    _WwpLeosLldpRemSysName_Type()
)
wwpLeosLldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemSysName.setStatus("deprecated")


class _WwpLeosLldpRemSysDesc_Type(SnmpAdminString):
    """Custom type wwpLeosLldpRemSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpLeosLldpRemSysDesc_Type.__name__ = "SnmpAdminString"
_WwpLeosLldpRemSysDesc_Object = MibTableColumn
wwpLeosLldpRemSysDesc = _WwpLeosLldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 10),
    _WwpLeosLldpRemSysDesc_Type()
)
wwpLeosLldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemSysDesc.setStatus("deprecated")
_WwpLeosLldpRemSysCapSupported_Type = WwpLeosLldpSystemCapabilitiesMap
_WwpLeosLldpRemSysCapSupported_Object = MibTableColumn
wwpLeosLldpRemSysCapSupported = _WwpLeosLldpRemSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 11),
    _WwpLeosLldpRemSysCapSupported_Type()
)
wwpLeosLldpRemSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemSysCapSupported.setStatus("deprecated")
_WwpLeosLldpRemSysCapEnabled_Type = WwpLeosLldpSystemCapabilitiesMap
_WwpLeosLldpRemSysCapEnabled_Object = MibTableColumn
wwpLeosLldpRemSysCapEnabled = _WwpLeosLldpRemSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 12),
    _WwpLeosLldpRemSysCapEnabled_Type()
)
wwpLeosLldpRemSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemSysCapEnabled.setStatus("deprecated")
_WwpLeosLldpRemManAddrTable_Object = MibTable
wwpLeosLldpRemManAddrTable = _WwpLeosLldpRemManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wwpLeosLldpRemManAddrTable.setStatus("deprecated")
_WwpLeosLldpRemManAddrEntry_Object = MibTableRow
wwpLeosLldpRemManAddrEntry = _WwpLeosLldpRemManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2, 1)
)
wwpLeosLldpRemManAddrEntry.setIndexNames(
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemTimeMark"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemLocalPortNum"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemIndex"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemManAddrType"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemManAddr"),
)
if mibBuilder.loadTexts:
    wwpLeosLldpRemManAddrEntry.setStatus("deprecated")
_WwpLeosLldpRemManAddrType_Type = AddressFamilyNumbers
_WwpLeosLldpRemManAddrType_Object = MibTableColumn
wwpLeosLldpRemManAddrType = _WwpLeosLldpRemManAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2, 1, 1),
    _WwpLeosLldpRemManAddrType_Type()
)
wwpLeosLldpRemManAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpRemManAddrType.setStatus("deprecated")
_WwpLeosLldpRemManAddr_Type = WwpLeosLldpManAddress
_WwpLeosLldpRemManAddr_Object = MibTableColumn
wwpLeosLldpRemManAddr = _WwpLeosLldpRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2, 1, 2),
    _WwpLeosLldpRemManAddr_Type()
)
wwpLeosLldpRemManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpRemManAddr.setStatus("deprecated")
_WwpLeosLldpRemManAddrIfSubtype_Type = WwpLeosLldpManAddrIfSubtype
_WwpLeosLldpRemManAddrIfSubtype_Object = MibTableColumn
wwpLeosLldpRemManAddrIfSubtype = _WwpLeosLldpRemManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2, 1, 3),
    _WwpLeosLldpRemManAddrIfSubtype_Type()
)
wwpLeosLldpRemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemManAddrIfSubtype.setStatus("deprecated")
_WwpLeosLldpRemManAddrIfId_Type = Integer32
_WwpLeosLldpRemManAddrIfId_Object = MibTableColumn
wwpLeosLldpRemManAddrIfId = _WwpLeosLldpRemManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2, 1, 4),
    _WwpLeosLldpRemManAddrIfId_Type()
)
wwpLeosLldpRemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemManAddrIfId.setStatus("deprecated")
_WwpLeosLldpRemManAddrOID_Type = ObjectIdentifier
_WwpLeosLldpRemManAddrOID_Object = MibTableColumn
wwpLeosLldpRemManAddrOID = _WwpLeosLldpRemManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2, 1, 5),
    _WwpLeosLldpRemManAddrOID_Type()
)
wwpLeosLldpRemManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemManAddrOID.setStatus("deprecated")
_WwpLeosLldpRemUnknownTLVTable_Object = MibTable
wwpLeosLldpRemUnknownTLVTable = _WwpLeosLldpRemUnknownTLVTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 3)
)
if mibBuilder.loadTexts:
    wwpLeosLldpRemUnknownTLVTable.setStatus("deprecated")
_WwpLeosLldpRemUnknownTLVEntry_Object = MibTableRow
wwpLeosLldpRemUnknownTLVEntry = _WwpLeosLldpRemUnknownTLVEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 3, 1)
)
wwpLeosLldpRemUnknownTLVEntry.setIndexNames(
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemTimeMark"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemLocalPortNum"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosLldpRemUnknownTLVEntry.setStatus("deprecated")


class _WwpLeosLldpRemUnknownTLVType_Type(Integer32):
    """Custom type wwpLeosLldpRemUnknownTLVType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 126),
    )


_WwpLeosLldpRemUnknownTLVType_Type.__name__ = "Integer32"
_WwpLeosLldpRemUnknownTLVType_Object = MibTableColumn
wwpLeosLldpRemUnknownTLVType = _WwpLeosLldpRemUnknownTLVType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 3, 1, 1),
    _WwpLeosLldpRemUnknownTLVType_Type()
)
wwpLeosLldpRemUnknownTLVType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpRemUnknownTLVType.setStatus("deprecated")


class _WwpLeosLldpRemUnknownTLVInfo_Type(OctetString):
    """Custom type wwpLeosLldpRemUnknownTLVInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_WwpLeosLldpRemUnknownTLVInfo_Type.__name__ = "OctetString"
_WwpLeosLldpRemUnknownTLVInfo_Object = MibTableColumn
wwpLeosLldpRemUnknownTLVInfo = _WwpLeosLldpRemUnknownTLVInfo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 3, 1, 2),
    _WwpLeosLldpRemUnknownTLVInfo_Type()
)
wwpLeosLldpRemUnknownTLVInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemUnknownTLVInfo.setStatus("deprecated")
_WwpLeosLldpRemOrgDefInfoTable_Object = MibTable
wwpLeosLldpRemOrgDefInfoTable = _WwpLeosLldpRemOrgDefInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wwpLeosLldpRemOrgDefInfoTable.setStatus("deprecated")
_WwpLeosLldpRemOrgDefInfoEntry_Object = MibTableRow
wwpLeosLldpRemOrgDefInfoEntry = _WwpLeosLldpRemOrgDefInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 4, 1)
)
wwpLeosLldpRemOrgDefInfoEntry.setIndexNames(
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemTimeMark"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemLocalPortNum"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemIndex"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemOrgDefInfoOUI"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemOrgDefInfoSubtype"),
    (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemOrgDefInfoIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosLldpRemOrgDefInfoEntry.setStatus("deprecated")


class _WwpLeosLldpRemOrgDefInfoOUI_Type(OctetString):
    """Custom type wwpLeosLldpRemOrgDefInfoOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WwpLeosLldpRemOrgDefInfoOUI_Type.__name__ = "OctetString"
_WwpLeosLldpRemOrgDefInfoOUI_Object = MibTableColumn
wwpLeosLldpRemOrgDefInfoOUI = _WwpLeosLldpRemOrgDefInfoOUI_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 4, 1, 1),
    _WwpLeosLldpRemOrgDefInfoOUI_Type()
)
wwpLeosLldpRemOrgDefInfoOUI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpRemOrgDefInfoOUI.setStatus("deprecated")


class _WwpLeosLldpRemOrgDefInfoSubtype_Type(Integer32):
    """Custom type wwpLeosLldpRemOrgDefInfoSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WwpLeosLldpRemOrgDefInfoSubtype_Type.__name__ = "Integer32"
_WwpLeosLldpRemOrgDefInfoSubtype_Object = MibTableColumn
wwpLeosLldpRemOrgDefInfoSubtype = _WwpLeosLldpRemOrgDefInfoSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 4, 1, 2),
    _WwpLeosLldpRemOrgDefInfoSubtype_Type()
)
wwpLeosLldpRemOrgDefInfoSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpRemOrgDefInfoSubtype.setStatus("deprecated")


class _WwpLeosLldpRemOrgDefInfoIndex_Type(Integer32):
    """Custom type wwpLeosLldpRemOrgDefInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpLeosLldpRemOrgDefInfoIndex_Type.__name__ = "Integer32"
_WwpLeosLldpRemOrgDefInfoIndex_Object = MibTableColumn
wwpLeosLldpRemOrgDefInfoIndex = _WwpLeosLldpRemOrgDefInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 4, 1, 3),
    _WwpLeosLldpRemOrgDefInfoIndex_Type()
)
wwpLeosLldpRemOrgDefInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosLldpRemOrgDefInfoIndex.setStatus("deprecated")


class _WwpLeosLldpRemOrgDefInfo_Type(OctetString):
    """Custom type wwpLeosLldpRemOrgDefInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 507),
    )


_WwpLeosLldpRemOrgDefInfo_Type.__name__ = "OctetString"
_WwpLeosLldpRemOrgDefInfo_Object = MibTableColumn
wwpLeosLldpRemOrgDefInfo = _WwpLeosLldpRemOrgDefInfo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 4, 1, 4),
    _WwpLeosLldpRemOrgDefInfo_Type()
)
wwpLeosLldpRemOrgDefInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLldpRemOrgDefInfo.setStatus("deprecated")
_WwpLeosLldpExtentions_ObjectIdentity = ObjectIdentity
wwpLeosLldpExtentions = _WwpLeosLldpExtentions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 5)
)
_WwpLeosLldpGlobalAtts_ObjectIdentity = ObjectIdentity
wwpLeosLldpGlobalAtts = _WwpLeosLldpGlobalAtts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 6)
)
_WwpLeosLldpStatsClear_Type = TruthValue
_WwpLeosLldpStatsClear_Object = MibScalar
wwpLeosLldpStatsClear = _WwpLeosLldpStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 6, 1),
    _WwpLeosLldpStatsClear_Type()
)
wwpLeosLldpStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLldpStatsClear.setStatus("current")
_WwpLeosLldpConformance_ObjectIdentity = ObjectIdentity
wwpLeosLldpConformance = _WwpLeosLldpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2)
)
_WwpLeosLldpCompliances_ObjectIdentity = ObjectIdentity
wwpLeosLldpCompliances = _WwpLeosLldpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 1)
)
_WwpLeosLldpGroups_ObjectIdentity = ObjectIdentity
wwpLeosLldpGroups = _WwpLeosLldpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 2)
)
_WwpLeosLldpNotifMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosLldpNotifMIBNotificationPrefix = _WwpLeosLldpNotifMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 3)
)
_WwpLeosLldpNotifMIBNotification_ObjectIdentity = ObjectIdentity
wwpLeosLldpNotifMIBNotification = _WwpLeosLldpNotifMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 3, 0)
)
wwpLeosLldpLocManAddrEntry.registerAugmentions(
    ("WWP-LEOS-LLDP-MIB",
     "wwpLeosLldpConfigManAddrEntry")
)
wwpLeosLldpConfigManAddrEntry.setIndexNames(*wwpLeosLldpLocManAddrEntry.getIndexNames())

# Managed Objects groups

wwpLeosLldpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 2, 1)
)
wwpLeosLldpConfigGroup.setObjects(
      *(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpMessageTxInterval"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpMessageTxHoldMultiplier"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpReinitDelay"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpTxDelay"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpPortConfigAdminStatus"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpPortConfigTLVsTxEnable"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpManAddrPortsTxEnable"))
)
if mibBuilder.loadTexts:
    wwpLeosLldpConfigGroup.setStatus("deprecated")

wwpLeosLldpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 2, 2)
)
wwpLeosLldpStatsGroup.setObjects(
      *(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsFramesDiscardedTotal"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsFramesInErrors"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsFramesInTotal"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsFramesOutTotal"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsTLVsInErrors"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsTLVsDiscardedTotal"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsTLVsUnrecognizedTotal"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpCounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    wwpLeosLldpStatsGroup.setStatus("deprecated")

wwpLeosLldpLocSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 2, 3)
)
wwpLeosLldpLocSysGroup.setObjects(
      *(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocChassisType"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocChassisId"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocPortType"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocPortId"))
)
if mibBuilder.loadTexts:
    wwpLeosLldpLocSysGroup.setStatus("deprecated")

wwpLeosLldpOptLocSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 2, 4)
)
wwpLeosLldpOptLocSysGroup.setObjects(
      *(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocPortDesc"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocSysDesc"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocSysName"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocSysCapSupported"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocSysCapEnabled"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocManAddrIfSubtype"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocManAddrIfId"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocManAddrOID"))
)
if mibBuilder.loadTexts:
    wwpLeosLldpOptLocSysGroup.setStatus("deprecated")

wwpLeosLldpRemSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 2, 5)
)
wwpLeosLldpRemSysGroup.setObjects(
      *(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemRemoteChassisType"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemRemoteChassis"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemRemotePortType"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemRemotePort"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemPortDesc"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemSysName"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemSysDesc"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemSysCapSupported"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemSysCapEnabled"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemManAddrIfSubtype"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemManAddrIfId"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemManAddrOID"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemUnknownTLVInfo"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemOrgDefInfo"))
)
if mibBuilder.loadTexts:
    wwpLeosLldpRemSysGroup.setStatus("deprecated")


# Notification objects

wwpLeosLldpPortSpeedChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 3, 0, 1)
)
wwpLeosLldpPortSpeedChangeTrap.setObjects(
      *(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpPortConfigPortNum"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpPortConfigOperPortSpeed"),
        ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpPortConfigReqPortSpeed"))
)
if mibBuilder.loadTexts:
    wwpLeosLldpPortSpeedChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

wwpLeosLldpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosLldpCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-LLDP-MIB",
    **{"TimeFilter": TimeFilter,
       "SnmpAdminString": SnmpAdminString,
       "WwpLeosLldpChassisIdType": WwpLeosLldpChassisIdType,
       "WwpLeosLldpChassisId": WwpLeosLldpChassisId,
       "WwpLeosLldpPortIdType": WwpLeosLldpPortIdType,
       "WwpLeosLldpPortId": WwpLeosLldpPortId,
       "WwpLeosLldpManAddrIfSubtype": WwpLeosLldpManAddrIfSubtype,
       "WwpLeosLldpManAddress": WwpLeosLldpManAddress,
       "WwpLeosLldpSystemCapabilitiesMap": WwpLeosLldpSystemCapabilitiesMap,
       "WwpLeosLldpPortNumber": WwpLeosLldpPortNumber,
       "WwpLeosLldpPortList": WwpLeosLldpPortList,
       "wwpLeosLldpMIB": wwpLeosLldpMIB,
       "wwpLeosLldpMIBObjects": wwpLeosLldpMIBObjects,
       "wwpLeosLldpConfiguration": wwpLeosLldpConfiguration,
       "wwpLeosLldpMessageTxInterval": wwpLeosLldpMessageTxInterval,
       "wwpLeosLldpMessageTxHoldMultiplier": wwpLeosLldpMessageTxHoldMultiplier,
       "wwpLeosLldpReinitDelay": wwpLeosLldpReinitDelay,
       "wwpLeosLldpTxDelay": wwpLeosLldpTxDelay,
       "wwpLeosLldpPortConfigTable": wwpLeosLldpPortConfigTable,
       "wwpLeosLldpPortConfigEntry": wwpLeosLldpPortConfigEntry,
       "wwpLeosLldpPortConfigPortNum": wwpLeosLldpPortConfigPortNum,
       "wwpLeosLldpPortConfigAdminStatus": wwpLeosLldpPortConfigAdminStatus,
       "wwpLeosLldpPortConfigTLVsTxEnable": wwpLeosLldpPortConfigTLVsTxEnable,
       "wwpLeosLldpPortConfigStatsClear": wwpLeosLldpPortConfigStatsClear,
       "wwpLeosLldpPortConfigOperPortSpeed": wwpLeosLldpPortConfigOperPortSpeed,
       "wwpLeosLldpPortConfigReqPortSpeed": wwpLeosLldpPortConfigReqPortSpeed,
       "wwpLeosLldpConfigManAddrTable": wwpLeosLldpConfigManAddrTable,
       "wwpLeosLldpConfigManAddrEntry": wwpLeosLldpConfigManAddrEntry,
       "wwpLeosLldpManAddrPortsTxEnable": wwpLeosLldpManAddrPortsTxEnable,
       "wwpLeosLldpStatistics": wwpLeosLldpStatistics,
       "wwpLeosLldpStatsTable": wwpLeosLldpStatsTable,
       "wwpLeosLldpStatsEntry": wwpLeosLldpStatsEntry,
       "wwpLeosLldpStatsPortNum": wwpLeosLldpStatsPortNum,
       "wwpLeosLldpStatsFramesDiscardedTotal": wwpLeosLldpStatsFramesDiscardedTotal,
       "wwpLeosLldpStatsFramesInErrors": wwpLeosLldpStatsFramesInErrors,
       "wwpLeosLldpStatsFramesInTotal": wwpLeosLldpStatsFramesInTotal,
       "wwpLeosLldpStatsFramesOutTotal": wwpLeosLldpStatsFramesOutTotal,
       "wwpLeosLldpStatsTLVsInErrors": wwpLeosLldpStatsTLVsInErrors,
       "wwpLeosLldpStatsTLVsDiscardedTotal": wwpLeosLldpStatsTLVsDiscardedTotal,
       "wwpLeosLldpStatsTLVsUnrecognizedTotal": wwpLeosLldpStatsTLVsUnrecognizedTotal,
       "wwpLeosLldpCounterDiscontinuityTime": wwpLeosLldpCounterDiscontinuityTime,
       "wwpLeosLldpLocalSystemData": wwpLeosLldpLocalSystemData,
       "wwpLeosLldpLocChassisType": wwpLeosLldpLocChassisType,
       "wwpLeosLldpLocChassisId": wwpLeosLldpLocChassisId,
       "wwpLeosLldpLocSysName": wwpLeosLldpLocSysName,
       "wwpLeosLldpLocSysDesc": wwpLeosLldpLocSysDesc,
       "wwpLeosLldpLocSysCapSupported": wwpLeosLldpLocSysCapSupported,
       "wwpLeosLldpLocSysCapEnabled": wwpLeosLldpLocSysCapEnabled,
       "wwpLeosLldpLocPortTable": wwpLeosLldpLocPortTable,
       "wwpLeosLldpLocPortEntry": wwpLeosLldpLocPortEntry,
       "wwpLeosLldpLocPortNum": wwpLeosLldpLocPortNum,
       "wwpLeosLldpLocPortType": wwpLeosLldpLocPortType,
       "wwpLeosLldpLocPortId": wwpLeosLldpLocPortId,
       "wwpLeosLldpLocPortDesc": wwpLeosLldpLocPortDesc,
       "wwpLeosLldpLocManAddrTable": wwpLeosLldpLocManAddrTable,
       "wwpLeosLldpLocManAddrEntry": wwpLeosLldpLocManAddrEntry,
       "wwpLeosLldpLocManAddrType": wwpLeosLldpLocManAddrType,
       "wwpLeosLldpLocManAddr": wwpLeosLldpLocManAddr,
       "wwpLeosLldpLocManAddrLen": wwpLeosLldpLocManAddrLen,
       "wwpLeosLldpLocManAddrIfSubtype": wwpLeosLldpLocManAddrIfSubtype,
       "wwpLeosLldpLocManAddrIfId": wwpLeosLldpLocManAddrIfId,
       "wwpLeosLldpLocManAddrOID": wwpLeosLldpLocManAddrOID,
       "wwpLeosLldpRemoteSystemsData": wwpLeosLldpRemoteSystemsData,
       "wwpLeosLldpRemTable": wwpLeosLldpRemTable,
       "wwpLeosLldpRemEntry": wwpLeosLldpRemEntry,
       "wwpLeosLldpRemTimeMark": wwpLeosLldpRemTimeMark,
       "wwpLeosLldpRemLocalPortNum": wwpLeosLldpRemLocalPortNum,
       "wwpLeosLldpRemIndex": wwpLeosLldpRemIndex,
       "wwpLeosLldpRemRemoteChassisType": wwpLeosLldpRemRemoteChassisType,
       "wwpLeosLldpRemRemoteChassis": wwpLeosLldpRemRemoteChassis,
       "wwpLeosLldpRemRemotePortType": wwpLeosLldpRemRemotePortType,
       "wwpLeosLldpRemRemotePort": wwpLeosLldpRemRemotePort,
       "wwpLeosLldpRemPortDesc": wwpLeosLldpRemPortDesc,
       "wwpLeosLldpRemSysName": wwpLeosLldpRemSysName,
       "wwpLeosLldpRemSysDesc": wwpLeosLldpRemSysDesc,
       "wwpLeosLldpRemSysCapSupported": wwpLeosLldpRemSysCapSupported,
       "wwpLeosLldpRemSysCapEnabled": wwpLeosLldpRemSysCapEnabled,
       "wwpLeosLldpRemManAddrTable": wwpLeosLldpRemManAddrTable,
       "wwpLeosLldpRemManAddrEntry": wwpLeosLldpRemManAddrEntry,
       "wwpLeosLldpRemManAddrType": wwpLeosLldpRemManAddrType,
       "wwpLeosLldpRemManAddr": wwpLeosLldpRemManAddr,
       "wwpLeosLldpRemManAddrIfSubtype": wwpLeosLldpRemManAddrIfSubtype,
       "wwpLeosLldpRemManAddrIfId": wwpLeosLldpRemManAddrIfId,
       "wwpLeosLldpRemManAddrOID": wwpLeosLldpRemManAddrOID,
       "wwpLeosLldpRemUnknownTLVTable": wwpLeosLldpRemUnknownTLVTable,
       "wwpLeosLldpRemUnknownTLVEntry": wwpLeosLldpRemUnknownTLVEntry,
       "wwpLeosLldpRemUnknownTLVType": wwpLeosLldpRemUnknownTLVType,
       "wwpLeosLldpRemUnknownTLVInfo": wwpLeosLldpRemUnknownTLVInfo,
       "wwpLeosLldpRemOrgDefInfoTable": wwpLeosLldpRemOrgDefInfoTable,
       "wwpLeosLldpRemOrgDefInfoEntry": wwpLeosLldpRemOrgDefInfoEntry,
       "wwpLeosLldpRemOrgDefInfoOUI": wwpLeosLldpRemOrgDefInfoOUI,
       "wwpLeosLldpRemOrgDefInfoSubtype": wwpLeosLldpRemOrgDefInfoSubtype,
       "wwpLeosLldpRemOrgDefInfoIndex": wwpLeosLldpRemOrgDefInfoIndex,
       "wwpLeosLldpRemOrgDefInfo": wwpLeosLldpRemOrgDefInfo,
       "wwpLeosLldpExtentions": wwpLeosLldpExtentions,
       "wwpLeosLldpGlobalAtts": wwpLeosLldpGlobalAtts,
       "wwpLeosLldpStatsClear": wwpLeosLldpStatsClear,
       "wwpLeosLldpConformance": wwpLeosLldpConformance,
       "wwpLeosLldpCompliances": wwpLeosLldpCompliances,
       "wwpLeosLldpCompliance": wwpLeosLldpCompliance,
       "wwpLeosLldpGroups": wwpLeosLldpGroups,
       "wwpLeosLldpConfigGroup": wwpLeosLldpConfigGroup,
       "wwpLeosLldpStatsGroup": wwpLeosLldpStatsGroup,
       "wwpLeosLldpLocSysGroup": wwpLeosLldpLocSysGroup,
       "wwpLeosLldpOptLocSysGroup": wwpLeosLldpOptLocSysGroup,
       "wwpLeosLldpRemSysGroup": wwpLeosLldpRemSysGroup,
       "wwpLeosLldpNotifMIBNotificationPrefix": wwpLeosLldpNotifMIBNotificationPrefix,
       "wwpLeosLldpNotifMIBNotification": wwpLeosLldpNotifMIBNotification,
       "wwpLeosLldpPortSpeedChangeTrap": wwpLeosLldpPortSpeedChangeTrap}
)
