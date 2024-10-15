# SNMP MIB module (WWP-ENVIRON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-ENVIRON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:39 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpEnvironMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13)
)
wwpEnvironMIB.setRevisions(
        ("2003-04-28 00:00",
         "2003-03-11 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_WwpEnvironMIBObjects_ObjectIdentity = ObjectIdentity
wwpEnvironMIBObjects = _WwpEnvironMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1)
)
_WwpEnviron_ObjectIdentity = ObjectIdentity
wwpEnviron = _WwpEnviron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1)
)
_WwpEnvBatteryModule_ObjectIdentity = ObjectIdentity
wwpEnvBatteryModule = _WwpEnvBatteryModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 1)
)


class _WwpEnvBattStatus_Type(Integer32):
    """Custom type wwpEnvBattStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 3),
          ("presentAndWorking", 1),
          ("presentButNotWorking", 2))
    )


_WwpEnvBattStatus_Type.__name__ = "Integer32"
_WwpEnvBattStatus_Object = MibScalar
wwpEnvBattStatus = _WwpEnvBattStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 1, 1),
    _WwpEnvBattStatus_Type()
)
wwpEnvBattStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvBattStatus.setStatus("current")
_WwpEnvPowerSupplyModule_ObjectIdentity = ObjectIdentity
wwpEnvPowerSupplyModule = _WwpEnvPowerSupplyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 2)
)
_WwpEnvPowerTable_Object = MibTable
wwpEnvPowerTable = _WwpEnvPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpEnvPowerTable.setStatus("current")
_WwpEnvPowerEntry_Object = MibTableRow
wwpEnvPowerEntry = _WwpEnvPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 2, 1, 1)
)
wwpEnvPowerEntry.setIndexNames(
    (0, "WWP-ENVIRON-MIB", "wwpEnvPowerSupplyNum"),
)
if mibBuilder.loadTexts:
    wwpEnvPowerEntry.setStatus("current")


class _WwpEnvPowerSupplyNum_Type(Integer32):
    """Custom type wwpEnvPowerSupplyNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpEnvPowerSupplyNum_Type.__name__ = "Integer32"
_WwpEnvPowerSupplyNum_Object = MibTableColumn
wwpEnvPowerSupplyNum = _WwpEnvPowerSupplyNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 2, 1, 1, 1),
    _WwpEnvPowerSupplyNum_Type()
)
wwpEnvPowerSupplyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvPowerSupplyNum.setStatus("current")


class _WwpEnvPowerSupplyState_Type(Integer32):
    """Custom type wwpEnvPowerSupplyState based on Integer32"""
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
        *(("infoNotAvailable", 1),
          ("installedAndNotOperating", 4),
          ("installedAndOperating", 3),
          ("notInstalled", 2))
    )


_WwpEnvPowerSupplyState_Type.__name__ = "Integer32"
_WwpEnvPowerSupplyState_Object = MibTableColumn
wwpEnvPowerSupplyState = _WwpEnvPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 2, 1, 1, 2),
    _WwpEnvPowerSupplyState_Type()
)
wwpEnvPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvPowerSupplyState.setStatus("current")


class _WwpEnvPowerSupplyType_Type(Integer32):
    """Custom type wwpEnvPowerSupplyType based on Integer32"""
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
        *(("ac-dc", 1),
          ("dc-dc", 2),
          ("external", 5),
          ("highOutput", 4),
          ("notSupported", 3))
    )


_WwpEnvPowerSupplyType_Type.__name__ = "Integer32"
_WwpEnvPowerSupplyType_Object = MibTableColumn
wwpEnvPowerSupplyType = _WwpEnvPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 2, 1, 1, 3),
    _WwpEnvPowerSupplyType_Type()
)
wwpEnvPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvPowerSupplyType.setStatus("current")


class _WwpEnvPowerSupplyRedundancy_Type(Integer32):
    """Custom type wwpEnvPowerSupplyRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRedundant", 2),
          ("notSupported", 3),
          ("redundant", 1))
    )


_WwpEnvPowerSupplyRedundancy_Type.__name__ = "Integer32"
_WwpEnvPowerSupplyRedundancy_Object = MibTableColumn
wwpEnvPowerSupplyRedundancy = _WwpEnvPowerSupplyRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 2, 1, 1, 4),
    _WwpEnvPowerSupplyRedundancy_Type()
)
wwpEnvPowerSupplyRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvPowerSupplyRedundancy.setStatus("current")


class _WwpEnvRedPowerSupplyNotifEnabled_Type(TruthValue):
    """Custom type wwpEnvRedPowerSupplyNotifEnabled based on TruthValue"""


_WwpEnvRedPowerSupplyNotifEnabled_Object = MibScalar
wwpEnvRedPowerSupplyNotifEnabled = _WwpEnvRedPowerSupplyNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 2, 2),
    _WwpEnvRedPowerSupplyNotifEnabled_Type()
)
wwpEnvRedPowerSupplyNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvRedPowerSupplyNotifEnabled.setStatus("deprecated")
_WwpEnvFanModule_ObjectIdentity = ObjectIdentity
wwpEnvFanModule = _WwpEnvFanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 3)
)
_WwpEnvFanModuleTable_Object = MibTable
wwpEnvFanModuleTable = _WwpEnvFanModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wwpEnvFanModuleTable.setStatus("current")
_WwpEnvFanModuleEntry_Object = MibTableRow
wwpEnvFanModuleEntry = _WwpEnvFanModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 3, 1, 1)
)
wwpEnvFanModuleEntry.setIndexNames(
    (0, "WWP-ENVIRON-MIB", "wwpEnvFanModuleNum"),
)
if mibBuilder.loadTexts:
    wwpEnvFanModuleEntry.setStatus("current")


class _WwpEnvFanModuleNum_Type(Integer32):
    """Custom type wwpEnvFanModuleNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpEnvFanModuleNum_Type.__name__ = "Integer32"
_WwpEnvFanModuleNum_Object = MibTableColumn
wwpEnvFanModuleNum = _WwpEnvFanModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 3, 1, 1, 1),
    _WwpEnvFanModuleNum_Type()
)
wwpEnvFanModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvFanModuleNum.setStatus("current")


class _WwpEnvFanModuleState_Type(Integer32):
    """Custom type wwpEnvFanModuleState based on Integer32"""
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
        *(("infoNotAvailable", 1),
          ("installedAndNotOperating", 4),
          ("installedAndOperating", 3),
          ("notInstalled", 2))
    )


_WwpEnvFanModuleState_Type.__name__ = "Integer32"
_WwpEnvFanModuleState_Object = MibTableColumn
wwpEnvFanModuleState = _WwpEnvFanModuleState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 3, 1, 1, 2),
    _WwpEnvFanModuleState_Type()
)
wwpEnvFanModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvFanModuleState.setStatus("current")


class _WwpEnvFanAvgSpeed_Type(Integer32):
    """Custom type wwpEnvFanAvgSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpEnvFanAvgSpeed_Type.__name__ = "Integer32"
_WwpEnvFanAvgSpeed_Object = MibTableColumn
wwpEnvFanAvgSpeed = _WwpEnvFanAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 3, 1, 1, 3),
    _WwpEnvFanAvgSpeed_Type()
)
wwpEnvFanAvgSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvFanAvgSpeed.setStatus("current")
if mibBuilder.loadTexts:
    wwpEnvFanAvgSpeed.setUnits("rpm")


class _WwpEnvFanCurrentSpeed_Type(Integer32):
    """Custom type wwpEnvFanCurrentSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpEnvFanCurrentSpeed_Type.__name__ = "Integer32"
_WwpEnvFanCurrentSpeed_Object = MibTableColumn
wwpEnvFanCurrentSpeed = _WwpEnvFanCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 3, 1, 1, 4),
    _WwpEnvFanCurrentSpeed_Type()
)
wwpEnvFanCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvFanCurrentSpeed.setStatus("current")
if mibBuilder.loadTexts:
    wwpEnvFanCurrentSpeed.setUnits("rpm")


class _WwpEnvFanMinSpeed_Type(Integer32):
    """Custom type wwpEnvFanMinSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpEnvFanMinSpeed_Type.__name__ = "Integer32"
_WwpEnvFanMinSpeed_Object = MibTableColumn
wwpEnvFanMinSpeed = _WwpEnvFanMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 3, 1, 1, 5),
    _WwpEnvFanMinSpeed_Type()
)
wwpEnvFanMinSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvFanMinSpeed.setStatus("current")
if mibBuilder.loadTexts:
    wwpEnvFanMinSpeed.setUnits("rpm")


class _WwpEnvFanModuleNotifEnabled_Type(TruthValue):
    """Custom type wwpEnvFanModuleNotifEnabled based on TruthValue"""


_WwpEnvFanModuleNotifEnabled_Object = MibScalar
wwpEnvFanModuleNotifEnabled = _WwpEnvFanModuleNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 3, 2),
    _WwpEnvFanModuleNotifEnabled_Type()
)
wwpEnvFanModuleNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvFanModuleNotifEnabled.setStatus("current")
_WwpEnvTempSensor_ObjectIdentity = ObjectIdentity
wwpEnvTempSensor = _WwpEnvTempSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 4)
)
_WwpEnvTempSensorTable_Object = MibTable
wwpEnvTempSensorTable = _WwpEnvTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wwpEnvTempSensorTable.setStatus("current")
_WwpEnvTempSensorEntry_Object = MibTableRow
wwpEnvTempSensorEntry = _WwpEnvTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 4, 1, 1)
)
wwpEnvTempSensorEntry.setIndexNames(
    (0, "WWP-ENVIRON-MIB", "wwpEnvTempSensorNum"),
)
if mibBuilder.loadTexts:
    wwpEnvTempSensorEntry.setStatus("current")


class _WwpEnvTempSensorNum_Type(Integer32):
    """Custom type wwpEnvTempSensorNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpEnvTempSensorNum_Type.__name__ = "Integer32"
_WwpEnvTempSensorNum_Object = MibTableColumn
wwpEnvTempSensorNum = _WwpEnvTempSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 4, 1, 1, 1),
    _WwpEnvTempSensorNum_Type()
)
wwpEnvTempSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvTempSensorNum.setStatus("current")
_WwpEnvTempSensorValue_Type = Integer32
_WwpEnvTempSensorValue_Object = MibTableColumn
wwpEnvTempSensorValue = _WwpEnvTempSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 4, 1, 1, 2),
    _WwpEnvTempSensorValue_Type()
)
wwpEnvTempSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvTempSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    wwpEnvTempSensorValue.setUnits("degrees Celsius")
_WwpEnvTempSensorHighThreshold_Type = Integer32
_WwpEnvTempSensorHighThreshold_Object = MibTableColumn
wwpEnvTempSensorHighThreshold = _WwpEnvTempSensorHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 4, 1, 1, 3),
    _WwpEnvTempSensorHighThreshold_Type()
)
wwpEnvTempSensorHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvTempSensorHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpEnvTempSensorHighThreshold.setUnits("degrees Celsius")
_WwpEnvTempSensorLowThreshold_Type = Integer32
_WwpEnvTempSensorLowThreshold_Object = MibTableColumn
wwpEnvTempSensorLowThreshold = _WwpEnvTempSensorLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 4, 1, 1, 4),
    _WwpEnvTempSensorLowThreshold_Type()
)
wwpEnvTempSensorLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvTempSensorLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpEnvTempSensorLowThreshold.setUnits("degrees Celsius")


class _WwpEnvTempSensorState_Type(Integer32):
    """Custom type wwpEnvTempSensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("higherThanThreshold", 0),
          ("lowerThanThreshold", 2),
          ("normal", 1))
    )


_WwpEnvTempSensorState_Type.__name__ = "Integer32"
_WwpEnvTempSensorState_Object = MibTableColumn
wwpEnvTempSensorState = _WwpEnvTempSensorState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 4, 1, 1, 5),
    _WwpEnvTempSensorState_Type()
)
wwpEnvTempSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvTempSensorState.setStatus("current")


class _WwpEnvTempNotifEnabled_Type(TruthValue):
    """Custom type wwpEnvTempNotifEnabled based on TruthValue"""


_WwpEnvTempNotifEnabled_Object = MibScalar
wwpEnvTempNotifEnabled = _WwpEnvTempNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 4, 2),
    _WwpEnvTempNotifEnabled_Type()
)
wwpEnvTempNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvTempNotifEnabled.setStatus("current")
_WwpEnvPortPowerMgmt_ObjectIdentity = ObjectIdentity
wwpEnvPortPowerMgmt = _WwpEnvPortPowerMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 5)
)
_WwpPortPowerMgmtTable_Object = MibTable
wwpPortPowerMgmtTable = _WwpPortPowerMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    wwpPortPowerMgmtTable.setStatus("current")
_WwpPortPowerMgmtEntry_Object = MibTableRow
wwpPortPowerMgmtEntry = _WwpPortPowerMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 5, 1, 1)
)
wwpPortPowerMgmtEntry.setIndexNames(
    (0, "WWP-ENVIRON-MIB", "wwpEnvPortBankId"),
)
if mibBuilder.loadTexts:
    wwpPortPowerMgmtEntry.setStatus("current")


class _WwpEnvPortBankId_Type(Integer32):
    """Custom type wwpEnvPortBankId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpEnvPortBankId_Type.__name__ = "Integer32"
_WwpEnvPortBankId_Object = MibTableColumn
wwpEnvPortBankId = _WwpEnvPortBankId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 5, 1, 1, 1),
    _WwpEnvPortBankId_Type()
)
wwpEnvPortBankId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvPortBankId.setStatus("current")
_WwpEnvPortMap_Type = PortList
_WwpEnvPortMap_Object = MibTableColumn
wwpEnvPortMap = _WwpEnvPortMap_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 5, 1, 1, 2),
    _WwpEnvPortMap_Type()
)
wwpEnvPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvPortMap.setStatus("current")


class _WwpEnvPortBankOn_Type(Integer32):
    """Custom type wwpEnvPortBankOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_WwpEnvPortBankOn_Type.__name__ = "Integer32"
_WwpEnvPortBankOn_Object = MibTableColumn
wwpEnvPortBankOn = _WwpEnvPortBankOn_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 5, 1, 1, 3),
    _WwpEnvPortBankOn_Type()
)
wwpEnvPortBankOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvPortBankOn.setStatus("current")
_WwpEnvNotif_ObjectIdentity = ObjectIdentity
wwpEnvNotif = _WwpEnvNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 6)
)


class _WwpPowerSwitchingOp_Type(Integer32):
    """Custom type wwpPowerSwitchingOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acToBattery", 1),
          ("bateryToAC", 2),
          ("none", 0))
    )


_WwpPowerSwitchingOp_Type.__name__ = "Integer32"
_WwpPowerSwitchingOp_Object = MibScalar
wwpPowerSwitchingOp = _WwpPowerSwitchingOp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 6, 1),
    _WwpPowerSwitchingOp_Type()
)
wwpPowerSwitchingOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPowerSwitchingOp.setStatus("current")
_WwpEnvPortalBatteryModule_ObjectIdentity = ObjectIdentity
wwpEnvPortalBatteryModule = _WwpEnvPortalBatteryModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7)
)


class _WwpEnvPortalBatteryStatus_Type(Integer32):
    """Custom type wwpEnvPortalBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 2),
          ("present", 1))
    )


_WwpEnvPortalBatteryStatus_Type.__name__ = "Integer32"
_WwpEnvPortalBatteryStatus_Object = MibScalar
wwpEnvPortalBatteryStatus = _WwpEnvPortalBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 1),
    _WwpEnvPortalBatteryStatus_Type()
)
wwpEnvPortalBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvPortalBatteryStatus.setStatus("current")


class _WwpEnvPortalBatteryVoltageLevel_Type(Integer32):
    """Custom type wwpEnvPortalBatteryVoltageLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_WwpEnvPortalBatteryVoltageLevel_Type.__name__ = "Integer32"
_WwpEnvPortalBatteryVoltageLevel_Object = MibScalar
wwpEnvPortalBatteryVoltageLevel = _WwpEnvPortalBatteryVoltageLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 2),
    _WwpEnvPortalBatteryVoltageLevel_Type()
)
wwpEnvPortalBatteryVoltageLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvPortalBatteryVoltageLevel.setStatus("current")


class _WwpEnvPortalBatteryCondition_Type(Integer32):
    """Custom type wwpEnvPortalBatteryCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1))
    )


_WwpEnvPortalBatteryCondition_Type.__name__ = "Integer32"
_WwpEnvPortalBatteryCondition_Object = MibScalar
wwpEnvPortalBatteryCondition = _WwpEnvPortalBatteryCondition_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 3),
    _WwpEnvPortalBatteryCondition_Type()
)
wwpEnvPortalBatteryCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvPortalBatteryCondition.setStatus("current")


class _WwpEnvPortalPowerSource_Type(Integer32):
    """Custom type wwpEnvPortalPowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("battery", 2),
          ("primaryPower", 1))
    )


_WwpEnvPortalPowerSource_Type.__name__ = "Integer32"
_WwpEnvPortalPowerSource_Object = MibScalar
wwpEnvPortalPowerSource = _WwpEnvPortalPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 4),
    _WwpEnvPortalPowerSource_Type()
)
wwpEnvPortalPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvPortalPowerSource.setStatus("current")


class _WwpEnvBatteryNormalStateName_Type(DisplayString):
    """Custom type wwpEnvBatteryNormalStateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpEnvBatteryNormalStateName_Type.__name__ = "DisplayString"
_WwpEnvBatteryNormalStateName_Object = MibScalar
wwpEnvBatteryNormalStateName = _WwpEnvBatteryNormalStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 5),
    _WwpEnvBatteryNormalStateName_Type()
)
wwpEnvBatteryNormalStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryNormalStateName.setStatus("current")


class _WwpEnvBatteryLowStateName_Type(DisplayString):
    """Custom type wwpEnvBatteryLowStateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpEnvBatteryLowStateName_Type.__name__ = "DisplayString"
_WwpEnvBatteryLowStateName_Object = MibScalar
wwpEnvBatteryLowStateName = _WwpEnvBatteryLowStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 6),
    _WwpEnvBatteryLowStateName_Type()
)
wwpEnvBatteryLowStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryLowStateName.setStatus("current")


class _WwpEnvBatteryGoodStateName_Type(DisplayString):
    """Custom type wwpEnvBatteryGoodStateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpEnvBatteryGoodStateName_Type.__name__ = "DisplayString"
_WwpEnvBatteryGoodStateName_Object = MibScalar
wwpEnvBatteryGoodStateName = _WwpEnvBatteryGoodStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 7),
    _WwpEnvBatteryGoodStateName_Type()
)
wwpEnvBatteryGoodStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryGoodStateName.setStatus("current")


class _WwpEnvBatteryBadStateName_Type(DisplayString):
    """Custom type wwpEnvBatteryBadStateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpEnvBatteryBadStateName_Type.__name__ = "DisplayString"
_WwpEnvBatteryBadStateName_Object = MibScalar
wwpEnvBatteryBadStateName = _WwpEnvBatteryBadStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 8),
    _WwpEnvBatteryBadStateName_Type()
)
wwpEnvBatteryBadStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryBadStateName.setStatus("current")


class _WwpEnvBatteryPresentStateName_Type(DisplayString):
    """Custom type wwpEnvBatteryPresentStateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpEnvBatteryPresentStateName_Type.__name__ = "DisplayString"
_WwpEnvBatteryPresentStateName_Object = MibScalar
wwpEnvBatteryPresentStateName = _WwpEnvBatteryPresentStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 9),
    _WwpEnvBatteryPresentStateName_Type()
)
wwpEnvBatteryPresentStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryPresentStateName.setStatus("current")


class _WwpEnvBatteryMissingStateName_Type(DisplayString):
    """Custom type wwpEnvBatteryMissingStateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpEnvBatteryMissingStateName_Type.__name__ = "DisplayString"
_WwpEnvBatteryMissingStateName_Object = MibScalar
wwpEnvBatteryMissingStateName = _WwpEnvBatteryMissingStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 10),
    _WwpEnvBatteryMissingStateName_Type()
)
wwpEnvBatteryMissingStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryMissingStateName.setStatus("current")


class _WwpEnvBatteryPowerPrimaryStateName_Type(DisplayString):
    """Custom type wwpEnvBatteryPowerPrimaryStateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpEnvBatteryPowerPrimaryStateName_Type.__name__ = "DisplayString"
_WwpEnvBatteryPowerPrimaryStateName_Object = MibScalar
wwpEnvBatteryPowerPrimaryStateName = _WwpEnvBatteryPowerPrimaryStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 11),
    _WwpEnvBatteryPowerPrimaryStateName_Type()
)
wwpEnvBatteryPowerPrimaryStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryPowerPrimaryStateName.setStatus("current")


class _WwpEnvBatteryPowerBatteryStateName_Type(DisplayString):
    """Custom type wwpEnvBatteryPowerBatteryStateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpEnvBatteryPowerBatteryStateName_Type.__name__ = "DisplayString"
_WwpEnvBatteryPowerBatteryStateName_Object = MibScalar
wwpEnvBatteryPowerBatteryStateName = _WwpEnvBatteryPowerBatteryStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 12),
    _WwpEnvBatteryPowerBatteryStateName_Type()
)
wwpEnvBatteryPowerBatteryStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryPowerBatteryStateName.setStatus("current")


class _WwpEnvBatteryLowStateNotifEnabled_Type(TruthValue):
    """Custom type wwpEnvBatteryLowStateNotifEnabled based on TruthValue"""


_WwpEnvBatteryLowStateNotifEnabled_Object = MibScalar
wwpEnvBatteryLowStateNotifEnabled = _WwpEnvBatteryLowStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 13),
    _WwpEnvBatteryLowStateNotifEnabled_Type()
)
wwpEnvBatteryLowStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryLowStateNotifEnabled.setStatus("current")


class _WwpEnvBatteryBadStateNotifEnabled_Type(TruthValue):
    """Custom type wwpEnvBatteryBadStateNotifEnabled based on TruthValue"""


_WwpEnvBatteryBadStateNotifEnabled_Object = MibScalar
wwpEnvBatteryBadStateNotifEnabled = _WwpEnvBatteryBadStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 14),
    _WwpEnvBatteryBadStateNotifEnabled_Type()
)
wwpEnvBatteryBadStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryBadStateNotifEnabled.setStatus("current")


class _WwpEnvBatteryMissingStateNotifEnabled_Type(TruthValue):
    """Custom type wwpEnvBatteryMissingStateNotifEnabled based on TruthValue"""


_WwpEnvBatteryMissingStateNotifEnabled_Object = MibScalar
wwpEnvBatteryMissingStateNotifEnabled = _WwpEnvBatteryMissingStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 15),
    _WwpEnvBatteryMissingStateNotifEnabled_Type()
)
wwpEnvBatteryMissingStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryMissingStateNotifEnabled.setStatus("current")


class _WwpEnvBatteryPowerNotifEnabled_Type(TruthValue):
    """Custom type wwpEnvBatteryPowerNotifEnabled based on TruthValue"""


_WwpEnvBatteryPowerNotifEnabled_Object = MibScalar
wwpEnvBatteryPowerNotifEnabled = _WwpEnvBatteryPowerNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 16),
    _WwpEnvBatteryPowerNotifEnabled_Type()
)
wwpEnvBatteryPowerNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryPowerNotifEnabled.setStatus("current")


class _WwpEnvBatteryPeriodicTrapsTimer_Type(Integer32):
    """Custom type wwpEnvBatteryPeriodicTrapsTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8760),
    )


_WwpEnvBatteryPeriodicTrapsTimer_Type.__name__ = "Integer32"
_WwpEnvBatteryPeriodicTrapsTimer_Object = MibScalar
wwpEnvBatteryPeriodicTrapsTimer = _WwpEnvBatteryPeriodicTrapsTimer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 17),
    _WwpEnvBatteryPeriodicTrapsTimer_Type()
)
wwpEnvBatteryPeriodicTrapsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryPeriodicTrapsTimer.setStatus("current")


class _WwpEnvBatteryPowerUpTrapsEnable_Type(TruthValue):
    """Custom type wwpEnvBatteryPowerUpTrapsEnable based on TruthValue"""


_WwpEnvBatteryPowerUpTrapsEnable_Object = MibScalar
wwpEnvBatteryPowerUpTrapsEnable = _WwpEnvBatteryPowerUpTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 7, 18),
    _WwpEnvBatteryPowerUpTrapsEnable_Type()
)
wwpEnvBatteryPowerUpTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvBatteryPowerUpTrapsEnable.setStatus("current")
_WwpEnvDoorModule_ObjectIdentity = ObjectIdentity
wwpEnvDoorModule = _WwpEnvDoorModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 8)
)


class _WwpEnvDoorState_Type(Integer32):
    """Custom type wwpEnvDoorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_WwpEnvDoorState_Type.__name__ = "Integer32"
_WwpEnvDoorState_Object = MibScalar
wwpEnvDoorState = _WwpEnvDoorState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 8, 1),
    _WwpEnvDoorState_Type()
)
wwpEnvDoorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvDoorState.setStatus("current")


class _WwpEnvDoorNotifEnabled_Type(TruthValue):
    """Custom type wwpEnvDoorNotifEnabled based on TruthValue"""


_WwpEnvDoorNotifEnabled_Object = MibScalar
wwpEnvDoorNotifEnabled = _WwpEnvDoorNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 8, 2),
    _WwpEnvDoorNotifEnabled_Type()
)
wwpEnvDoorNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvDoorNotifEnabled.setStatus("current")
_WwpEnvDryContactModule_ObjectIdentity = ObjectIdentity
wwpEnvDryContactModule = _WwpEnvDryContactModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 9)
)


class _WwpEnvDryContactOpenStateName_Type(DisplayString):
    """Custom type wwpEnvDryContactOpenStateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpEnvDryContactOpenStateName_Type.__name__ = "DisplayString"
_WwpEnvDryContactOpenStateName_Object = MibScalar
wwpEnvDryContactOpenStateName = _WwpEnvDryContactOpenStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 9, 1),
    _WwpEnvDryContactOpenStateName_Type()
)
wwpEnvDryContactOpenStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvDryContactOpenStateName.setStatus("current")


class _WwpEnvDryContactOpenStateChgAccumulate_Type(Integer32):
    """Custom type wwpEnvDryContactOpenStateChgAccumulate based on Integer32"""
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


_WwpEnvDryContactOpenStateChgAccumulate_Type.__name__ = "Integer32"
_WwpEnvDryContactOpenStateChgAccumulate_Object = MibScalar
wwpEnvDryContactOpenStateChgAccumulate = _WwpEnvDryContactOpenStateChgAccumulate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 9, 2),
    _WwpEnvDryContactOpenStateChgAccumulate_Type()
)
wwpEnvDryContactOpenStateChgAccumulate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvDryContactOpenStateChgAccumulate.setStatus("current")
_WwpEnvDryContactOpenStateCount_Type = Counter32
_WwpEnvDryContactOpenStateCount_Object = MibScalar
wwpEnvDryContactOpenStateCount = _WwpEnvDryContactOpenStateCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 9, 3),
    _WwpEnvDryContactOpenStateCount_Type()
)
wwpEnvDryContactOpenStateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvDryContactOpenStateCount.setStatus("current")


class _WwpEnvDryContactOpenStateNotifEnabled_Type(TruthValue):
    """Custom type wwpEnvDryContactOpenStateNotifEnabled based on TruthValue"""


_WwpEnvDryContactOpenStateNotifEnabled_Object = MibScalar
wwpEnvDryContactOpenStateNotifEnabled = _WwpEnvDryContactOpenStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 9, 4),
    _WwpEnvDryContactOpenStateNotifEnabled_Type()
)
wwpEnvDryContactOpenStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvDryContactOpenStateNotifEnabled.setStatus("current")


class _WwpEnvDryContactCloseStateName_Type(DisplayString):
    """Custom type wwpEnvDryContactCloseStateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpEnvDryContactCloseStateName_Type.__name__ = "DisplayString"
_WwpEnvDryContactCloseStateName_Object = MibScalar
wwpEnvDryContactCloseStateName = _WwpEnvDryContactCloseStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 9, 5),
    _WwpEnvDryContactCloseStateName_Type()
)
wwpEnvDryContactCloseStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvDryContactCloseStateName.setStatus("current")


class _WwpEnvDryContactCloseStateChgAccumulate_Type(Integer32):
    """Custom type wwpEnvDryContactCloseStateChgAccumulate based on Integer32"""
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


_WwpEnvDryContactCloseStateChgAccumulate_Type.__name__ = "Integer32"
_WwpEnvDryContactCloseStateChgAccumulate_Object = MibScalar
wwpEnvDryContactCloseStateChgAccumulate = _WwpEnvDryContactCloseStateChgAccumulate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 9, 6),
    _WwpEnvDryContactCloseStateChgAccumulate_Type()
)
wwpEnvDryContactCloseStateChgAccumulate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvDryContactCloseStateChgAccumulate.setStatus("current")
_WwpEnvDryContactCloseStateCount_Type = Counter32
_WwpEnvDryContactCloseStateCount_Object = MibScalar
wwpEnvDryContactCloseStateCount = _WwpEnvDryContactCloseStateCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 9, 7),
    _WwpEnvDryContactCloseStateCount_Type()
)
wwpEnvDryContactCloseStateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvDryContactCloseStateCount.setStatus("current")


class _WwpEnvDryContactCloseStateNotifEnabled_Type(TruthValue):
    """Custom type wwpEnvDryContactCloseStateNotifEnabled based on TruthValue"""


_WwpEnvDryContactCloseStateNotifEnabled_Object = MibScalar
wwpEnvDryContactCloseStateNotifEnabled = _WwpEnvDryContactCloseStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 9, 8),
    _WwpEnvDryContactCloseStateNotifEnabled_Type()
)
wwpEnvDryContactCloseStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvDryContactCloseStateNotifEnabled.setStatus("current")
_WwpEnvRFModule_ObjectIdentity = ObjectIdentity
wwpEnvRFModule = _WwpEnvRFModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 10)
)


class _WwpEnvRFModuleState_Type(Integer32):
    """Custom type wwpEnvRFModuleState based on Integer32"""
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


_WwpEnvRFModuleState_Type.__name__ = "Integer32"
_WwpEnvRFModuleState_Object = MibScalar
wwpEnvRFModuleState = _WwpEnvRFModuleState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 10, 1),
    _WwpEnvRFModuleState_Type()
)
wwpEnvRFModuleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpEnvRFModuleState.setStatus("current")
_WwpEnvRFModuleSignalDetect_Type = TruthValue
_WwpEnvRFModuleSignalDetect_Object = MibScalar
wwpEnvRFModuleSignalDetect = _WwpEnvRFModuleSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 1, 1, 10, 2),
    _WwpEnvRFModuleSignalDetect_Type()
)
wwpEnvRFModuleSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpEnvRFModuleSignalDetect.setStatus("current")
_WwpEnvironMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpEnvironMIBNotificationPrefix = _WwpEnvironMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2)
)
_WwpEnvironMIBNotifications_ObjectIdentity = ObjectIdentity
wwpEnvironMIBNotifications = _WwpEnvironMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2, 0)
)
_WwpEnvironMIBConformance_ObjectIdentity = ObjectIdentity
wwpEnvironMIBConformance = _WwpEnvironMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 3)
)
_WwpEnvironMIBCompliances_ObjectIdentity = ObjectIdentity
wwpEnvironMIBCompliances = _WwpEnvironMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 3, 1)
)
_WwpEnvironMIBGroups_ObjectIdentity = ObjectIdentity
wwpEnvironMIBGroups = _WwpEnvironMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpEnvPowerSupplyStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2, 0, 1)
)
wwpEnvPowerSupplyStatusNotification.setObjects(
      *(("WWP-ENVIRON-MIB", "wwpEnvPowerSupplyNum"),
        ("WWP-ENVIRON-MIB", "wwpEnvPowerSupplyState"),
        ("WWP-ENVIRON-MIB", "wwpEnvPowerSupplyType"))
)
if mibBuilder.loadTexts:
    wwpEnvPowerSupplyStatusNotification.setStatus(
        "current"
    )

wwpEnvFanModuleNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2, 0, 2)
)
wwpEnvFanModuleNotification.setObjects(
      *(("WWP-ENVIRON-MIB", "wwpEnvFanModuleNum"),
        ("WWP-ENVIRON-MIB", "wwpEnvFanModuleState"))
)
if mibBuilder.loadTexts:
    wwpEnvFanModuleNotification.setStatus(
        "current"
    )

wwpEnvTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2, 0, 3)
)
wwpEnvTempNotification.setObjects(
      *(("WWP-ENVIRON-MIB", "wwpEnvTempSensorState"),
        ("WWP-ENVIRON-MIB", "wwpEnvTempSensorValue"),
        ("WWP-ENVIRON-MIB", "wwpEnvTempSensorHighThreshold"),
        ("WWP-ENVIRON-MIB", "wwpEnvTempSensorLowThreshold"))
)
if mibBuilder.loadTexts:
    wwpEnvTempNotification.setStatus(
        "current"
    )

wwpEnvPowerSwitchNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2, 0, 4)
)
wwpEnvPowerSwitchNotification.setObjects(
    ("WWP-ENVIRON-MIB", "wwpPowerSwitchingOp")
)
if mibBuilder.loadTexts:
    wwpEnvPowerSwitchNotification.setStatus(
        "current"
    )

wwpEnvPortalBatteryStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2, 0, 5)
)
wwpEnvPortalBatteryStatusNotification.setObjects(
    ("WWP-ENVIRON-MIB", "wwpEnvPortalBatteryStatus")
)
if mibBuilder.loadTexts:
    wwpEnvPortalBatteryStatusNotification.setStatus(
        "current"
    )

wwpEnvPortalBatteryVoltageLevelNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2, 0, 6)
)
wwpEnvPortalBatteryVoltageLevelNotification.setObjects(
    ("WWP-ENVIRON-MIB", "wwpEnvPortalBatteryVoltageLevel")
)
if mibBuilder.loadTexts:
    wwpEnvPortalBatteryVoltageLevelNotification.setStatus(
        "current"
    )

wwpEnvPortalBatteryConditionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2, 0, 7)
)
wwpEnvPortalBatteryConditionNotification.setObjects(
    ("WWP-ENVIRON-MIB", "wwpEnvPortalBatteryCondition")
)
if mibBuilder.loadTexts:
    wwpEnvPortalBatteryConditionNotification.setStatus(
        "current"
    )

wwpEnvPortalPowerSourceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2, 0, 8)
)
wwpEnvPortalPowerSourceNotification.setObjects(
    ("WWP-ENVIRON-MIB", "wwpEnvPortalPowerSource")
)
if mibBuilder.loadTexts:
    wwpEnvPortalPowerSourceNotification.setStatus(
        "current"
    )

wwpEnvDoorStateChgNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2, 0, 9)
)
wwpEnvDoorStateChgNotification.setObjects(
    ("WWP-ENVIRON-MIB", "wwpEnvDoorState")
)
if mibBuilder.loadTexts:
    wwpEnvDoorStateChgNotification.setStatus(
        "current"
    )

wwpEnvDryContactOpenStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2, 0, 10)
)
wwpEnvDryContactOpenStateNotification.setObjects(
      *(("WWP-ENVIRON-MIB", "wwpEnvDryContactOpenStateName"),
        ("WWP-ENVIRON-MIB", "wwpEnvDryContactOpenStateCount"))
)
if mibBuilder.loadTexts:
    wwpEnvDryContactOpenStateNotification.setStatus(
        "current"
    )

wwpEnvDryContactCloseStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 13, 2, 0, 11)
)
wwpEnvDryContactCloseStateNotification.setObjects(
      *(("WWP-ENVIRON-MIB", "wwpEnvDryContactCloseStateName"),
        ("WWP-ENVIRON-MIB", "wwpEnvDryContactCloseStateCount"))
)
if mibBuilder.loadTexts:
    wwpEnvDryContactCloseStateNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-ENVIRON-MIB",
    **{"PortList": PortList,
       "wwpEnvironMIB": wwpEnvironMIB,
       "wwpEnvironMIBObjects": wwpEnvironMIBObjects,
       "wwpEnviron": wwpEnviron,
       "wwpEnvBatteryModule": wwpEnvBatteryModule,
       "wwpEnvBattStatus": wwpEnvBattStatus,
       "wwpEnvPowerSupplyModule": wwpEnvPowerSupplyModule,
       "wwpEnvPowerTable": wwpEnvPowerTable,
       "wwpEnvPowerEntry": wwpEnvPowerEntry,
       "wwpEnvPowerSupplyNum": wwpEnvPowerSupplyNum,
       "wwpEnvPowerSupplyState": wwpEnvPowerSupplyState,
       "wwpEnvPowerSupplyType": wwpEnvPowerSupplyType,
       "wwpEnvPowerSupplyRedundancy": wwpEnvPowerSupplyRedundancy,
       "wwpEnvRedPowerSupplyNotifEnabled": wwpEnvRedPowerSupplyNotifEnabled,
       "wwpEnvFanModule": wwpEnvFanModule,
       "wwpEnvFanModuleTable": wwpEnvFanModuleTable,
       "wwpEnvFanModuleEntry": wwpEnvFanModuleEntry,
       "wwpEnvFanModuleNum": wwpEnvFanModuleNum,
       "wwpEnvFanModuleState": wwpEnvFanModuleState,
       "wwpEnvFanAvgSpeed": wwpEnvFanAvgSpeed,
       "wwpEnvFanCurrentSpeed": wwpEnvFanCurrentSpeed,
       "wwpEnvFanMinSpeed": wwpEnvFanMinSpeed,
       "wwpEnvFanModuleNotifEnabled": wwpEnvFanModuleNotifEnabled,
       "wwpEnvTempSensor": wwpEnvTempSensor,
       "wwpEnvTempSensorTable": wwpEnvTempSensorTable,
       "wwpEnvTempSensorEntry": wwpEnvTempSensorEntry,
       "wwpEnvTempSensorNum": wwpEnvTempSensorNum,
       "wwpEnvTempSensorValue": wwpEnvTempSensorValue,
       "wwpEnvTempSensorHighThreshold": wwpEnvTempSensorHighThreshold,
       "wwpEnvTempSensorLowThreshold": wwpEnvTempSensorLowThreshold,
       "wwpEnvTempSensorState": wwpEnvTempSensorState,
       "wwpEnvTempNotifEnabled": wwpEnvTempNotifEnabled,
       "wwpEnvPortPowerMgmt": wwpEnvPortPowerMgmt,
       "wwpPortPowerMgmtTable": wwpPortPowerMgmtTable,
       "wwpPortPowerMgmtEntry": wwpPortPowerMgmtEntry,
       "wwpEnvPortBankId": wwpEnvPortBankId,
       "wwpEnvPortMap": wwpEnvPortMap,
       "wwpEnvPortBankOn": wwpEnvPortBankOn,
       "wwpEnvNotif": wwpEnvNotif,
       "wwpPowerSwitchingOp": wwpPowerSwitchingOp,
       "wwpEnvPortalBatteryModule": wwpEnvPortalBatteryModule,
       "wwpEnvPortalBatteryStatus": wwpEnvPortalBatteryStatus,
       "wwpEnvPortalBatteryVoltageLevel": wwpEnvPortalBatteryVoltageLevel,
       "wwpEnvPortalBatteryCondition": wwpEnvPortalBatteryCondition,
       "wwpEnvPortalPowerSource": wwpEnvPortalPowerSource,
       "wwpEnvBatteryNormalStateName": wwpEnvBatteryNormalStateName,
       "wwpEnvBatteryLowStateName": wwpEnvBatteryLowStateName,
       "wwpEnvBatteryGoodStateName": wwpEnvBatteryGoodStateName,
       "wwpEnvBatteryBadStateName": wwpEnvBatteryBadStateName,
       "wwpEnvBatteryPresentStateName": wwpEnvBatteryPresentStateName,
       "wwpEnvBatteryMissingStateName": wwpEnvBatteryMissingStateName,
       "wwpEnvBatteryPowerPrimaryStateName": wwpEnvBatteryPowerPrimaryStateName,
       "wwpEnvBatteryPowerBatteryStateName": wwpEnvBatteryPowerBatteryStateName,
       "wwpEnvBatteryLowStateNotifEnabled": wwpEnvBatteryLowStateNotifEnabled,
       "wwpEnvBatteryBadStateNotifEnabled": wwpEnvBatteryBadStateNotifEnabled,
       "wwpEnvBatteryMissingStateNotifEnabled": wwpEnvBatteryMissingStateNotifEnabled,
       "wwpEnvBatteryPowerNotifEnabled": wwpEnvBatteryPowerNotifEnabled,
       "wwpEnvBatteryPeriodicTrapsTimer": wwpEnvBatteryPeriodicTrapsTimer,
       "wwpEnvBatteryPowerUpTrapsEnable": wwpEnvBatteryPowerUpTrapsEnable,
       "wwpEnvDoorModule": wwpEnvDoorModule,
       "wwpEnvDoorState": wwpEnvDoorState,
       "wwpEnvDoorNotifEnabled": wwpEnvDoorNotifEnabled,
       "wwpEnvDryContactModule": wwpEnvDryContactModule,
       "wwpEnvDryContactOpenStateName": wwpEnvDryContactOpenStateName,
       "wwpEnvDryContactOpenStateChgAccumulate": wwpEnvDryContactOpenStateChgAccumulate,
       "wwpEnvDryContactOpenStateCount": wwpEnvDryContactOpenStateCount,
       "wwpEnvDryContactOpenStateNotifEnabled": wwpEnvDryContactOpenStateNotifEnabled,
       "wwpEnvDryContactCloseStateName": wwpEnvDryContactCloseStateName,
       "wwpEnvDryContactCloseStateChgAccumulate": wwpEnvDryContactCloseStateChgAccumulate,
       "wwpEnvDryContactCloseStateCount": wwpEnvDryContactCloseStateCount,
       "wwpEnvDryContactCloseStateNotifEnabled": wwpEnvDryContactCloseStateNotifEnabled,
       "wwpEnvRFModule": wwpEnvRFModule,
       "wwpEnvRFModuleState": wwpEnvRFModuleState,
       "wwpEnvRFModuleSignalDetect": wwpEnvRFModuleSignalDetect,
       "wwpEnvironMIBNotificationPrefix": wwpEnvironMIBNotificationPrefix,
       "wwpEnvironMIBNotifications": wwpEnvironMIBNotifications,
       "wwpEnvPowerSupplyStatusNotification": wwpEnvPowerSupplyStatusNotification,
       "wwpEnvFanModuleNotification": wwpEnvFanModuleNotification,
       "wwpEnvTempNotification": wwpEnvTempNotification,
       "wwpEnvPowerSwitchNotification": wwpEnvPowerSwitchNotification,
       "wwpEnvPortalBatteryStatusNotification": wwpEnvPortalBatteryStatusNotification,
       "wwpEnvPortalBatteryVoltageLevelNotification": wwpEnvPortalBatteryVoltageLevelNotification,
       "wwpEnvPortalBatteryConditionNotification": wwpEnvPortalBatteryConditionNotification,
       "wwpEnvPortalPowerSourceNotification": wwpEnvPortalPowerSourceNotification,
       "wwpEnvDoorStateChgNotification": wwpEnvDoorStateChgNotification,
       "wwpEnvDryContactOpenStateNotification": wwpEnvDryContactOpenStateNotification,
       "wwpEnvDryContactCloseStateNotification": wwpEnvDryContactCloseStateNotification,
       "wwpEnvironMIBConformance": wwpEnvironMIBConformance,
       "wwpEnvironMIBCompliances": wwpEnvironMIBCompliances,
       "wwpEnvironMIBGroups": wwpEnvironMIBGroups}
)
