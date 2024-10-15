# SNMP MIB module (HP-ICF-TRANSCEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-TRANSCEIVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:19 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfTransceiverMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82)
)
hpicfTransceiverMIB.setRevisions(
        ("2016-02-23 00:00",
         "2016-02-01 00:00",
         "2015-02-17 00:00",
         "2012-02-22 00:00",
         "2011-07-25 00:00",
         "2011-06-08 00:00",
         "2011-03-14 00:00",
         "2011-03-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfXcvrObjects_ObjectIdentity = ObjectIdentity
hpicfXcvrObjects = _HpicfXcvrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1)
)
_HpicfXcvrInfo_ObjectIdentity = ObjectIdentity
hpicfXcvrInfo = _HpicfXcvrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1)
)
_HpicfXcvrInfoTable_Object = MibTable
hpicfXcvrInfoTable = _HpicfXcvrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfXcvrInfoTable.setStatus("current")
_HpicfXcvrInfoEntry_Object = MibTableRow
hpicfXcvrInfoEntry = _HpicfXcvrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1)
)
hpicfXcvrInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfXcvrInfoEntry.setStatus("current")


class _HpicfXcvrPortIndex_Type(Integer32):
    """Custom type hpicfXcvrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfXcvrPortIndex_Type.__name__ = "Integer32"
_HpicfXcvrPortIndex_Object = MibTableColumn
hpicfXcvrPortIndex = _HpicfXcvrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 1),
    _HpicfXcvrPortIndex_Type()
)
hpicfXcvrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrPortIndex.setStatus("current")


class _HpicfXcvrPortDesc_Type(SnmpAdminString):
    """Custom type hpicfXcvrPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HpicfXcvrPortDesc_Type.__name__ = "SnmpAdminString"
_HpicfXcvrPortDesc_Object = MibTableColumn
hpicfXcvrPortDesc = _HpicfXcvrPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 2),
    _HpicfXcvrPortDesc_Type()
)
hpicfXcvrPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrPortDesc.setStatus("current")


class _HpicfXcvrModel_Type(SnmpAdminString):
    """Custom type hpicfXcvrModel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfXcvrModel_Type.__name__ = "SnmpAdminString"
_HpicfXcvrModel_Object = MibTableColumn
hpicfXcvrModel = _HpicfXcvrModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 3),
    _HpicfXcvrModel_Type()
)
hpicfXcvrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrModel.setStatus("current")


class _HpicfXcvrSerial_Type(SnmpAdminString):
    """Custom type hpicfXcvrSerial based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfXcvrSerial_Type.__name__ = "SnmpAdminString"
_HpicfXcvrSerial_Object = MibTableColumn
hpicfXcvrSerial = _HpicfXcvrSerial_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 4),
    _HpicfXcvrSerial_Type()
)
hpicfXcvrSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrSerial.setStatus("current")


class _HpicfXcvrType_Type(SnmpAdminString):
    """Custom type hpicfXcvrType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfXcvrType_Type.__name__ = "SnmpAdminString"
_HpicfXcvrType_Object = MibTableColumn
hpicfXcvrType = _HpicfXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 5),
    _HpicfXcvrType_Type()
)
hpicfXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrType.setStatus("current")


class _HpicfXcvrConnectorType_Type(SnmpAdminString):
    """Custom type hpicfXcvrConnectorType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpicfXcvrConnectorType_Type.__name__ = "SnmpAdminString"
_HpicfXcvrConnectorType_Object = MibTableColumn
hpicfXcvrConnectorType = _HpicfXcvrConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 6),
    _HpicfXcvrConnectorType_Type()
)
hpicfXcvrConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrConnectorType.setStatus("current")


class _HpicfXcvrWavelength_Type(SnmpAdminString):
    """Custom type hpicfXcvrWavelength based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 96),
    )


_HpicfXcvrWavelength_Type.__name__ = "SnmpAdminString"
_HpicfXcvrWavelength_Object = MibTableColumn
hpicfXcvrWavelength = _HpicfXcvrWavelength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 7),
    _HpicfXcvrWavelength_Type()
)
hpicfXcvrWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrWavelength.setStatus("current")


class _HpicfXcvrTxDist_Type(SnmpAdminString):
    """Custom type hpicfXcvrTxDist based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpicfXcvrTxDist_Type.__name__ = "SnmpAdminString"
_HpicfXcvrTxDist_Object = MibTableColumn
hpicfXcvrTxDist = _HpicfXcvrTxDist_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 8),
    _HpicfXcvrTxDist_Type()
)
hpicfXcvrTxDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrTxDist.setStatus("current")


class _HpicfXcvrDiagnostics_Type(Integer32):
    """Custom type hpicfXcvrDiagnostics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dom", 1),
          ("none", 0),
          ("other", 3),
          ("vct", 2))
    )


_HpicfXcvrDiagnostics_Type.__name__ = "Integer32"
_HpicfXcvrDiagnostics_Object = MibTableColumn
hpicfXcvrDiagnostics = _HpicfXcvrDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 9),
    _HpicfXcvrDiagnostics_Type()
)
hpicfXcvrDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrDiagnostics.setStatus("current")
_HpicfXcvrDiagnosticsUpdate_Type = TruthValue
_HpicfXcvrDiagnosticsUpdate_Object = MibTableColumn
hpicfXcvrDiagnosticsUpdate = _HpicfXcvrDiagnosticsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 10),
    _HpicfXcvrDiagnosticsUpdate_Type()
)
hpicfXcvrDiagnosticsUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXcvrDiagnosticsUpdate.setStatus("current")
_HpicfXcvrTemp_Type = Integer32
_HpicfXcvrTemp_Object = MibTableColumn
hpicfXcvrTemp = _HpicfXcvrTemp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 11),
    _HpicfXcvrTemp_Type()
)
hpicfXcvrTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrTemp.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrTemp.setUnits("thousandths of degrees Celsius")


class _HpicfXcvrVoltage_Type(Unsigned32):
    """Custom type hpicfXcvrVoltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrVoltage_Type.__name__ = "Unsigned32"
_HpicfXcvrVoltage_Object = MibTableColumn
hpicfXcvrVoltage = _HpicfXcvrVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 12),
    _HpicfXcvrVoltage_Type()
)
hpicfXcvrVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrVoltage.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrVoltage.setUnits("hundreds of microvolts")


class _HpicfXcvrBias_Type(Unsigned32):
    """Custom type hpicfXcvrBias based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrBias_Type.__name__ = "Unsigned32"
_HpicfXcvrBias_Object = MibTableColumn
hpicfXcvrBias = _HpicfXcvrBias_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 13),
    _HpicfXcvrBias_Type()
)
hpicfXcvrBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrBias.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrBias.setUnits("microamps")
_HpicfXcvrTxPower_Type = Integer32
_HpicfXcvrTxPower_Object = MibTableColumn
hpicfXcvrTxPower = _HpicfXcvrTxPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 14),
    _HpicfXcvrTxPower_Type()
)
hpicfXcvrTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrTxPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrTxPower.setUnits("thousandths of dBm")
_HpicfXcvrRxPower_Type = Integer32
_HpicfXcvrRxPower_Object = MibTableColumn
hpicfXcvrRxPower = _HpicfXcvrRxPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 15),
    _HpicfXcvrRxPower_Type()
)
hpicfXcvrRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrRxPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrRxPower.setUnits("thousandths of dBm")


class _HpicfXcvrAlarms_Type(Bits):
    """Custom type hpicfXcvrAlarms based on Bits"""
    namedValues = NamedValues(
        *(("rxPowerHighAlarm", 11),
          ("rxPowerHighWarning", 1),
          ("rxPowerLowAlarm", 10),
          ("rxPowerLowWarning", 0),
          ("tempHighAlarm", 19),
          ("tempHighWarning", 9),
          ("tempLowAlarm", 18),
          ("tempLowWarning", 8),
          ("txBiasHighAlarm", 15),
          ("txBiasHighWarning", 5),
          ("txBiasLowAlarm", 14),
          ("txBiasLowWarning", 4),
          ("txPowerHighAlarm", 13),
          ("txPowerHighWarning", 3),
          ("txPowerLowAlarm", 12),
          ("txPowerLowWarning", 2),
          ("vccHighAlarm", 17),
          ("vccHighWarning", 7),
          ("vccLowAlarm", 16),
          ("vccLowWarning", 6))
    )

_HpicfXcvrAlarms_Type.__name__ = "Bits"
_HpicfXcvrAlarms_Object = MibTableColumn
hpicfXcvrAlarms = _HpicfXcvrAlarms_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 16),
    _HpicfXcvrAlarms_Type()
)
hpicfXcvrAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrAlarms.setStatus("current")


class _HpicfXcvrErrors_Type(Bits):
    """Custom type hpicfXcvrErrors based on Bits"""
    namedValues = NamedValues(
        *(("laserBiasCurrentFault", 9),
          ("laserOutputPowerFault", 11),
          ("laserTemperatureFault", 10),
          ("pcsReceiveLocalFault", 7),
          ("pcsTransmitLocalFault", 14),
          ("phyXSReceiveLocalFault", 8),
          ("phyXSTransmitLocalFault", 15),
          ("pmapmdReceiverLocalFault", 6),
          ("pmapmdTransmitterLocalFault", 13),
          ("rcvOpticalPowerFault", 5),
          ("rxLossOfSignal", 16),
          ("txFault", 12),
          ("wisLocalFault", 4),
          ("xcvrChecksum", 1),
          ("xcvrIOError", 0),
          ("xcvrTypeAndPortConfigMismatch", 2),
          ("xcvrTypeNotSupported", 3))
    )

_HpicfXcvrErrors_Type.__name__ = "Bits"
_HpicfXcvrErrors_Object = MibTableColumn
hpicfXcvrErrors = _HpicfXcvrErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 17),
    _HpicfXcvrErrors_Type()
)
hpicfXcvrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrErrors.setStatus("current")
_HpicfXcvrTempHiAlarm_Type = Integer32
_HpicfXcvrTempHiAlarm_Object = MibTableColumn
hpicfXcvrTempHiAlarm = _HpicfXcvrTempHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 18),
    _HpicfXcvrTempHiAlarm_Type()
)
hpicfXcvrTempHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrTempHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrTempHiAlarm.setUnits("thousandths of degrees Celsius")
_HpicfXcvrTempLoAlarm_Type = Integer32
_HpicfXcvrTempLoAlarm_Object = MibTableColumn
hpicfXcvrTempLoAlarm = _HpicfXcvrTempLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 19),
    _HpicfXcvrTempLoAlarm_Type()
)
hpicfXcvrTempLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrTempLoAlarm.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrTempLoAlarm.setUnits("thousandths of degrees Celsius")
_HpicfXcvrTempHiWarn_Type = Integer32
_HpicfXcvrTempHiWarn_Object = MibTableColumn
hpicfXcvrTempHiWarn = _HpicfXcvrTempHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 20),
    _HpicfXcvrTempHiWarn_Type()
)
hpicfXcvrTempHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrTempHiWarn.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrTempHiWarn.setUnits("thousandths of degrees Celsius")
_HpicfXcvrTempLoWarn_Type = Integer32
_HpicfXcvrTempLoWarn_Object = MibTableColumn
hpicfXcvrTempLoWarn = _HpicfXcvrTempLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 21),
    _HpicfXcvrTempLoWarn_Type()
)
hpicfXcvrTempLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrTempLoWarn.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrTempLoWarn.setUnits("thousandths of degrees Celsius")


class _HpicfXcvrVccHiAlarm_Type(Unsigned32):
    """Custom type hpicfXcvrVccHiAlarm based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrVccHiAlarm_Type.__name__ = "Unsigned32"
_HpicfXcvrVccHiAlarm_Object = MibTableColumn
hpicfXcvrVccHiAlarm = _HpicfXcvrVccHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 22),
    _HpicfXcvrVccHiAlarm_Type()
)
hpicfXcvrVccHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrVccHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrVccHiAlarm.setUnits("hundreds of microvolts")


class _HpicfXcvrVccLoAlarm_Type(Unsigned32):
    """Custom type hpicfXcvrVccLoAlarm based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrVccLoAlarm_Type.__name__ = "Unsigned32"
_HpicfXcvrVccLoAlarm_Object = MibTableColumn
hpicfXcvrVccLoAlarm = _HpicfXcvrVccLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 23),
    _HpicfXcvrVccLoAlarm_Type()
)
hpicfXcvrVccLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrVccLoAlarm.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrVccLoAlarm.setUnits("hundreds of microvolts")


class _HpicfXcvrVccHiWarn_Type(Unsigned32):
    """Custom type hpicfXcvrVccHiWarn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrVccHiWarn_Type.__name__ = "Unsigned32"
_HpicfXcvrVccHiWarn_Object = MibTableColumn
hpicfXcvrVccHiWarn = _HpicfXcvrVccHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 24),
    _HpicfXcvrVccHiWarn_Type()
)
hpicfXcvrVccHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrVccHiWarn.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrVccHiWarn.setUnits("hundreds of microvolts")


class _HpicfXcvrVccLoWarn_Type(Unsigned32):
    """Custom type hpicfXcvrVccLoWarn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrVccLoWarn_Type.__name__ = "Unsigned32"
_HpicfXcvrVccLoWarn_Object = MibTableColumn
hpicfXcvrVccLoWarn = _HpicfXcvrVccLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 25),
    _HpicfXcvrVccLoWarn_Type()
)
hpicfXcvrVccLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrVccLoWarn.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrVccLoWarn.setUnits("hundreds of microvolts")


class _HpicfXcvrBiasHiAlarm_Type(Unsigned32):
    """Custom type hpicfXcvrBiasHiAlarm based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrBiasHiAlarm_Type.__name__ = "Unsigned32"
_HpicfXcvrBiasHiAlarm_Object = MibTableColumn
hpicfXcvrBiasHiAlarm = _HpicfXcvrBiasHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 26),
    _HpicfXcvrBiasHiAlarm_Type()
)
hpicfXcvrBiasHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrBiasHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrBiasHiAlarm.setUnits("microamps")


class _HpicfXcvrBiasLoAlarm_Type(Unsigned32):
    """Custom type hpicfXcvrBiasLoAlarm based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrBiasLoAlarm_Type.__name__ = "Unsigned32"
_HpicfXcvrBiasLoAlarm_Object = MibTableColumn
hpicfXcvrBiasLoAlarm = _HpicfXcvrBiasLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 27),
    _HpicfXcvrBiasLoAlarm_Type()
)
hpicfXcvrBiasLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrBiasLoAlarm.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrBiasLoAlarm.setUnits("microamps")


class _HpicfXcvrBiasHiWarn_Type(Unsigned32):
    """Custom type hpicfXcvrBiasHiWarn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrBiasHiWarn_Type.__name__ = "Unsigned32"
_HpicfXcvrBiasHiWarn_Object = MibTableColumn
hpicfXcvrBiasHiWarn = _HpicfXcvrBiasHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 28),
    _HpicfXcvrBiasHiWarn_Type()
)
hpicfXcvrBiasHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrBiasHiWarn.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrBiasHiWarn.setUnits("microamps")


class _HpicfXcvrBiasLoWarn_Type(Unsigned32):
    """Custom type hpicfXcvrBiasLoWarn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrBiasLoWarn_Type.__name__ = "Unsigned32"
_HpicfXcvrBiasLoWarn_Object = MibTableColumn
hpicfXcvrBiasLoWarn = _HpicfXcvrBiasLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 29),
    _HpicfXcvrBiasLoWarn_Type()
)
hpicfXcvrBiasLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrBiasLoWarn.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrBiasLoWarn.setUnits("microamps")


class _HpicfXcvrPwrOutHiAlarm_Type(Unsigned32):
    """Custom type hpicfXcvrPwrOutHiAlarm based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrPwrOutHiAlarm_Type.__name__ = "Unsigned32"
_HpicfXcvrPwrOutHiAlarm_Object = MibTableColumn
hpicfXcvrPwrOutHiAlarm = _HpicfXcvrPwrOutHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 30),
    _HpicfXcvrPwrOutHiAlarm_Type()
)
hpicfXcvrPwrOutHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrPwrOutHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrPwrOutHiAlarm.setUnits("tenths of microwatts")


class _HpicfXcvrPwrOutLoAlarm_Type(Unsigned32):
    """Custom type hpicfXcvrPwrOutLoAlarm based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrPwrOutLoAlarm_Type.__name__ = "Unsigned32"
_HpicfXcvrPwrOutLoAlarm_Object = MibTableColumn
hpicfXcvrPwrOutLoAlarm = _HpicfXcvrPwrOutLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 31),
    _HpicfXcvrPwrOutLoAlarm_Type()
)
hpicfXcvrPwrOutLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrPwrOutLoAlarm.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrPwrOutLoAlarm.setUnits("tenths of microwatts")


class _HpicfXcvrPwrOutHiWarn_Type(Unsigned32):
    """Custom type hpicfXcvrPwrOutHiWarn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrPwrOutHiWarn_Type.__name__ = "Unsigned32"
_HpicfXcvrPwrOutHiWarn_Object = MibTableColumn
hpicfXcvrPwrOutHiWarn = _HpicfXcvrPwrOutHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 32),
    _HpicfXcvrPwrOutHiWarn_Type()
)
hpicfXcvrPwrOutHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrPwrOutHiWarn.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrPwrOutHiWarn.setUnits("tenths of microwatts")


class _HpicfXcvrPwrOutLoWarn_Type(Unsigned32):
    """Custom type hpicfXcvrPwrOutLoWarn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrPwrOutLoWarn_Type.__name__ = "Unsigned32"
_HpicfXcvrPwrOutLoWarn_Object = MibTableColumn
hpicfXcvrPwrOutLoWarn = _HpicfXcvrPwrOutLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 33),
    _HpicfXcvrPwrOutLoWarn_Type()
)
hpicfXcvrPwrOutLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrPwrOutLoWarn.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrPwrOutLoWarn.setUnits("tenths of microwatts")


class _HpicfXcvrRcvPwrHiAlarm_Type(Unsigned32):
    """Custom type hpicfXcvrRcvPwrHiAlarm based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrRcvPwrHiAlarm_Type.__name__ = "Unsigned32"
_HpicfXcvrRcvPwrHiAlarm_Object = MibTableColumn
hpicfXcvrRcvPwrHiAlarm = _HpicfXcvrRcvPwrHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 34),
    _HpicfXcvrRcvPwrHiAlarm_Type()
)
hpicfXcvrRcvPwrHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrRcvPwrHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrRcvPwrHiAlarm.setUnits("tenths of microwatts")


class _HpicfXcvrRcvPwrLoAlarm_Type(Unsigned32):
    """Custom type hpicfXcvrRcvPwrLoAlarm based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrRcvPwrLoAlarm_Type.__name__ = "Unsigned32"
_HpicfXcvrRcvPwrLoAlarm_Object = MibTableColumn
hpicfXcvrRcvPwrLoAlarm = _HpicfXcvrRcvPwrLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 35),
    _HpicfXcvrRcvPwrLoAlarm_Type()
)
hpicfXcvrRcvPwrLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrRcvPwrLoAlarm.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrRcvPwrLoAlarm.setUnits("tenths of microwatts")


class _HpicfXcvrRcvPwrHiWarn_Type(Unsigned32):
    """Custom type hpicfXcvrRcvPwrHiWarn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrRcvPwrHiWarn_Type.__name__ = "Unsigned32"
_HpicfXcvrRcvPwrHiWarn_Object = MibTableColumn
hpicfXcvrRcvPwrHiWarn = _HpicfXcvrRcvPwrHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 36),
    _HpicfXcvrRcvPwrHiWarn_Type()
)
hpicfXcvrRcvPwrHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrRcvPwrHiWarn.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrRcvPwrHiWarn.setUnits("tenths of microwatts")


class _HpicfXcvrRcvPwrLoWarn_Type(Unsigned32):
    """Custom type hpicfXcvrRcvPwrLoWarn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrRcvPwrLoWarn_Type.__name__ = "Unsigned32"
_HpicfXcvrRcvPwrLoWarn_Object = MibTableColumn
hpicfXcvrRcvPwrLoWarn = _HpicfXcvrRcvPwrLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 37),
    _HpicfXcvrRcvPwrLoWarn_Type()
)
hpicfXcvrRcvPwrLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrRcvPwrLoWarn.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrRcvPwrLoWarn.setUnits("tenths of microwatts")


class _HpicfXcvrDiagnosticsTimeStamp_Type(SnmpAdminString):
    """Custom type hpicfXcvrDiagnosticsTimeStamp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpicfXcvrDiagnosticsTimeStamp_Type.__name__ = "SnmpAdminString"
_HpicfXcvrDiagnosticsTimeStamp_Object = MibTableColumn
hpicfXcvrDiagnosticsTimeStamp = _HpicfXcvrDiagnosticsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 38),
    _HpicfXcvrDiagnosticsTimeStamp_Type()
)
hpicfXcvrDiagnosticsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrDiagnosticsTimeStamp.setStatus("deprecated")


class _HpicfXcvrPhyLinkStatus_Type(Integer32):
    """Custom type hpicfXcvrPhyLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_HpicfXcvrPhyLinkStatus_Type.__name__ = "Integer32"
_HpicfXcvrPhyLinkStatus_Object = MibTableColumn
hpicfXcvrPhyLinkStatus = _HpicfXcvrPhyLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 39),
    _HpicfXcvrPhyLinkStatus_Type()
)
hpicfXcvrPhyLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrPhyLinkStatus.setStatus("current")


class _HpicfXcvrPhySpeed_Type(Unsigned32):
    """Custom type hpicfXcvrPhySpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrPhySpeed_Type.__name__ = "Unsigned32"
_HpicfXcvrPhySpeed_Object = MibTableColumn
hpicfXcvrPhySpeed = _HpicfXcvrPhySpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 40),
    _HpicfXcvrPhySpeed_Type()
)
hpicfXcvrPhySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrPhySpeed.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrPhySpeed.setUnits("megabits per second")


class _HpicfXcvrPhyDuplex_Type(Integer32):
    """Custom type hpicfXcvrPhyDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 0),
          ("unspecified", 2))
    )


_HpicfXcvrPhyDuplex_Type.__name__ = "Integer32"
_HpicfXcvrPhyDuplex_Object = MibTableColumn
hpicfXcvrPhyDuplex = _HpicfXcvrPhyDuplex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 41),
    _HpicfXcvrPhyDuplex_Type()
)
hpicfXcvrPhyDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrPhyDuplex.setStatus("current")


class _HpicfXcvrMdiPairACableStatus_Type(Integer32):
    """Custom type hpicfXcvrMdiPairACableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("impedanceMismatch", 4),
          ("normal", 0),
          ("open", 2),
          ("short", 1),
          ("unspecified", 5))
    )


_HpicfXcvrMdiPairACableStatus_Type.__name__ = "Integer32"
_HpicfXcvrMdiPairACableStatus_Object = MibTableColumn
hpicfXcvrMdiPairACableStatus = _HpicfXcvrMdiPairACableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 42),
    _HpicfXcvrMdiPairACableStatus_Type()
)
hpicfXcvrMdiPairACableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairACableStatus.setStatus("current")


class _HpicfXcvrMdiPairACableLength_Type(Unsigned32):
    """Custom type hpicfXcvrMdiPairACableLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrMdiPairACableLength_Type.__name__ = "Unsigned32"
_HpicfXcvrMdiPairACableLength_Object = MibTableColumn
hpicfXcvrMdiPairACableLength = _HpicfXcvrMdiPairACableLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 43),
    _HpicfXcvrMdiPairACableLength_Type()
)
hpicfXcvrMdiPairACableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairACableLength.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairACableLength.setUnits("meters")


class _HpicfXcvrMdiPairADistanceToFault_Type(Unsigned32):
    """Custom type hpicfXcvrMdiPairADistanceToFault based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrMdiPairADistanceToFault_Type.__name__ = "Unsigned32"
_HpicfXcvrMdiPairADistanceToFault_Object = MibTableColumn
hpicfXcvrMdiPairADistanceToFault = _HpicfXcvrMdiPairADistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 44),
    _HpicfXcvrMdiPairADistanceToFault_Type()
)
hpicfXcvrMdiPairADistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairADistanceToFault.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairADistanceToFault.setUnits("meters")


class _HpicfXcvrMdiPairAPolaritySwap_Type(Integer32):
    """Custom type hpicfXcvrMdiPairAPolaritySwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reversed", 1),
          ("unspecified", 2))
    )


_HpicfXcvrMdiPairAPolaritySwap_Type.__name__ = "Integer32"
_HpicfXcvrMdiPairAPolaritySwap_Object = MibTableColumn
hpicfXcvrMdiPairAPolaritySwap = _HpicfXcvrMdiPairAPolaritySwap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 45),
    _HpicfXcvrMdiPairAPolaritySwap_Type()
)
hpicfXcvrMdiPairAPolaritySwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairAPolaritySwap.setStatus("current")


class _HpicfXcvrMdiPairASkew_Type(Unsigned32):
    """Custom type hpicfXcvrMdiPairASkew based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrMdiPairASkew_Type.__name__ = "Unsigned32"
_HpicfXcvrMdiPairASkew_Object = MibTableColumn
hpicfXcvrMdiPairASkew = _HpicfXcvrMdiPairASkew_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 46),
    _HpicfXcvrMdiPairASkew_Type()
)
hpicfXcvrMdiPairASkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairASkew.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairASkew.setUnits("nanoseconds")


class _HpicfXcvrMdiPairBCableStatus_Type(Integer32):
    """Custom type hpicfXcvrMdiPairBCableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("impedanceMismatch", 4),
          ("normal", 0),
          ("open", 2),
          ("short", 1),
          ("unspecified", 5))
    )


_HpicfXcvrMdiPairBCableStatus_Type.__name__ = "Integer32"
_HpicfXcvrMdiPairBCableStatus_Object = MibTableColumn
hpicfXcvrMdiPairBCableStatus = _HpicfXcvrMdiPairBCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 47),
    _HpicfXcvrMdiPairBCableStatus_Type()
)
hpicfXcvrMdiPairBCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairBCableStatus.setStatus("current")


class _HpicfXcvrMdiPairBCableLength_Type(Unsigned32):
    """Custom type hpicfXcvrMdiPairBCableLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrMdiPairBCableLength_Type.__name__ = "Unsigned32"
_HpicfXcvrMdiPairBCableLength_Object = MibTableColumn
hpicfXcvrMdiPairBCableLength = _HpicfXcvrMdiPairBCableLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 48),
    _HpicfXcvrMdiPairBCableLength_Type()
)
hpicfXcvrMdiPairBCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairBCableLength.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairBCableLength.setUnits("meters")


class _HpicfXcvrMdiPairBDistanceToFault_Type(Unsigned32):
    """Custom type hpicfXcvrMdiPairBDistanceToFault based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrMdiPairBDistanceToFault_Type.__name__ = "Unsigned32"
_HpicfXcvrMdiPairBDistanceToFault_Object = MibTableColumn
hpicfXcvrMdiPairBDistanceToFault = _HpicfXcvrMdiPairBDistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 49),
    _HpicfXcvrMdiPairBDistanceToFault_Type()
)
hpicfXcvrMdiPairBDistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairBDistanceToFault.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairBDistanceToFault.setUnits("meters")


class _HpicfXcvrMdiPairBPolaritySwap_Type(Integer32):
    """Custom type hpicfXcvrMdiPairBPolaritySwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reversed", 1),
          ("unspecified", 2))
    )


_HpicfXcvrMdiPairBPolaritySwap_Type.__name__ = "Integer32"
_HpicfXcvrMdiPairBPolaritySwap_Object = MibTableColumn
hpicfXcvrMdiPairBPolaritySwap = _HpicfXcvrMdiPairBPolaritySwap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 50),
    _HpicfXcvrMdiPairBPolaritySwap_Type()
)
hpicfXcvrMdiPairBPolaritySwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairBPolaritySwap.setStatus("current")


class _HpicfXcvrMdiPairBSkew_Type(Unsigned32):
    """Custom type hpicfXcvrMdiPairBSkew based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrMdiPairBSkew_Type.__name__ = "Unsigned32"
_HpicfXcvrMdiPairBSkew_Object = MibTableColumn
hpicfXcvrMdiPairBSkew = _HpicfXcvrMdiPairBSkew_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 51),
    _HpicfXcvrMdiPairBSkew_Type()
)
hpicfXcvrMdiPairBSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairBSkew.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairBSkew.setUnits("nanoseconds")


class _HpicfXcvrMdiPairCCableStatus_Type(Integer32):
    """Custom type hpicfXcvrMdiPairCCableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("impedanceMismatch", 4),
          ("normal", 0),
          ("open", 2),
          ("short", 1),
          ("unspecified", 5))
    )


_HpicfXcvrMdiPairCCableStatus_Type.__name__ = "Integer32"
_HpicfXcvrMdiPairCCableStatus_Object = MibTableColumn
hpicfXcvrMdiPairCCableStatus = _HpicfXcvrMdiPairCCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 52),
    _HpicfXcvrMdiPairCCableStatus_Type()
)
hpicfXcvrMdiPairCCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairCCableStatus.setStatus("current")


class _HpicfXcvrMdiPairCCableLength_Type(Unsigned32):
    """Custom type hpicfXcvrMdiPairCCableLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrMdiPairCCableLength_Type.__name__ = "Unsigned32"
_HpicfXcvrMdiPairCCableLength_Object = MibTableColumn
hpicfXcvrMdiPairCCableLength = _HpicfXcvrMdiPairCCableLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 53),
    _HpicfXcvrMdiPairCCableLength_Type()
)
hpicfXcvrMdiPairCCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairCCableLength.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairCCableLength.setUnits("meters")


class _HpicfXcvrMdiPairCDistanceToFault_Type(Unsigned32):
    """Custom type hpicfXcvrMdiPairCDistanceToFault based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrMdiPairCDistanceToFault_Type.__name__ = "Unsigned32"
_HpicfXcvrMdiPairCDistanceToFault_Object = MibTableColumn
hpicfXcvrMdiPairCDistanceToFault = _HpicfXcvrMdiPairCDistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 54),
    _HpicfXcvrMdiPairCDistanceToFault_Type()
)
hpicfXcvrMdiPairCDistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairCDistanceToFault.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairCDistanceToFault.setUnits("meters")


class _HpicfXcvrMdiPairCPolaritySwap_Type(Integer32):
    """Custom type hpicfXcvrMdiPairCPolaritySwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reversed", 1),
          ("unspecified", 2))
    )


_HpicfXcvrMdiPairCPolaritySwap_Type.__name__ = "Integer32"
_HpicfXcvrMdiPairCPolaritySwap_Object = MibTableColumn
hpicfXcvrMdiPairCPolaritySwap = _HpicfXcvrMdiPairCPolaritySwap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 55),
    _HpicfXcvrMdiPairCPolaritySwap_Type()
)
hpicfXcvrMdiPairCPolaritySwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairCPolaritySwap.setStatus("current")


class _HpicfXcvrMdiPairCSkew_Type(Unsigned32):
    """Custom type hpicfXcvrMdiPairCSkew based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrMdiPairCSkew_Type.__name__ = "Unsigned32"
_HpicfXcvrMdiPairCSkew_Object = MibTableColumn
hpicfXcvrMdiPairCSkew = _HpicfXcvrMdiPairCSkew_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 56),
    _HpicfXcvrMdiPairCSkew_Type()
)
hpicfXcvrMdiPairCSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairCSkew.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairCSkew.setUnits("nanoseconds")


class _HpicfXcvrMdiPairDCableStatus_Type(Integer32):
    """Custom type hpicfXcvrMdiPairDCableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("impedanceMismatch", 4),
          ("normal", 0),
          ("open", 2),
          ("short", 1),
          ("unspecified", 5))
    )


_HpicfXcvrMdiPairDCableStatus_Type.__name__ = "Integer32"
_HpicfXcvrMdiPairDCableStatus_Object = MibTableColumn
hpicfXcvrMdiPairDCableStatus = _HpicfXcvrMdiPairDCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 57),
    _HpicfXcvrMdiPairDCableStatus_Type()
)
hpicfXcvrMdiPairDCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairDCableStatus.setStatus("current")


class _HpicfXcvrMdiPairDCableLength_Type(Unsigned32):
    """Custom type hpicfXcvrMdiPairDCableLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrMdiPairDCableLength_Type.__name__ = "Unsigned32"
_HpicfXcvrMdiPairDCableLength_Object = MibTableColumn
hpicfXcvrMdiPairDCableLength = _HpicfXcvrMdiPairDCableLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 58),
    _HpicfXcvrMdiPairDCableLength_Type()
)
hpicfXcvrMdiPairDCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairDCableLength.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairDCableLength.setUnits("meters")


class _HpicfXcvrMdiPairDDistanceToFault_Type(Unsigned32):
    """Custom type hpicfXcvrMdiPairDDistanceToFault based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrMdiPairDDistanceToFault_Type.__name__ = "Unsigned32"
_HpicfXcvrMdiPairDDistanceToFault_Object = MibTableColumn
hpicfXcvrMdiPairDDistanceToFault = _HpicfXcvrMdiPairDDistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 59),
    _HpicfXcvrMdiPairDDistanceToFault_Type()
)
hpicfXcvrMdiPairDDistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairDDistanceToFault.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairDDistanceToFault.setUnits("meters")


class _HpicfXcvrMdiPairDPolaritySwap_Type(Integer32):
    """Custom type hpicfXcvrMdiPairDPolaritySwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reversed", 1),
          ("unspecified", 2))
    )


_HpicfXcvrMdiPairDPolaritySwap_Type.__name__ = "Integer32"
_HpicfXcvrMdiPairDPolaritySwap_Object = MibTableColumn
hpicfXcvrMdiPairDPolaritySwap = _HpicfXcvrMdiPairDPolaritySwap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 60),
    _HpicfXcvrMdiPairDPolaritySwap_Type()
)
hpicfXcvrMdiPairDPolaritySwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairDPolaritySwap.setStatus("current")


class _HpicfXcvrMdiPairDSkew_Type(Unsigned32):
    """Custom type hpicfXcvrMdiPairDSkew based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfXcvrMdiPairDSkew_Type.__name__ = "Unsigned32"
_HpicfXcvrMdiPairDSkew_Object = MibTableColumn
hpicfXcvrMdiPairDSkew = _HpicfXcvrMdiPairDSkew_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 61),
    _HpicfXcvrMdiPairDSkew_Type()
)
hpicfXcvrMdiPairDSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairDSkew.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairDSkew.setUnits("nanoseconds")


class _HpicfXcvrMdiPairABSwap_Type(Integer32):
    """Custom type hpicfXcvrMdiPairABSwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 0),
          ("mdix", 1),
          ("unspecified", 2))
    )


_HpicfXcvrMdiPairABSwap_Type.__name__ = "Integer32"
_HpicfXcvrMdiPairABSwap_Object = MibTableColumn
hpicfXcvrMdiPairABSwap = _HpicfXcvrMdiPairABSwap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 62),
    _HpicfXcvrMdiPairABSwap_Type()
)
hpicfXcvrMdiPairABSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairABSwap.setStatus("current")


class _HpicfXcvrMdiPairCDSwap_Type(Integer32):
    """Custom type hpicfXcvrMdiPairCDSwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 0),
          ("mdix", 1),
          ("unspecified", 2))
    )


_HpicfXcvrMdiPairCDSwap_Type.__name__ = "Integer32"
_HpicfXcvrMdiPairCDSwap_Object = MibTableColumn
hpicfXcvrMdiPairCDSwap = _HpicfXcvrMdiPairCDSwap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 63),
    _HpicfXcvrMdiPairCDSwap_Type()
)
hpicfXcvrMdiPairCDSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrMdiPairCDSwap.setStatus("current")
_HpicfXcvrDiagnosticsTimeTicks_Type = TimeTicks
_HpicfXcvrDiagnosticsTimeTicks_Object = MibTableColumn
hpicfXcvrDiagnosticsTimeTicks = _HpicfXcvrDiagnosticsTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 64),
    _HpicfXcvrDiagnosticsTimeTicks_Type()
)
hpicfXcvrDiagnosticsTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrDiagnosticsTimeTicks.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrDiagnosticsTimeTicks.setUnits("centi-seconds")


class _HpicfXcvrManufacDate_Type(SnmpAdminString):
    """Custom type hpicfXcvrManufacDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HpicfXcvrManufacDate_Type.__name__ = "SnmpAdminString"
_HpicfXcvrManufacDate_Object = MibTableColumn
hpicfXcvrManufacDate = _HpicfXcvrManufacDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 1, 1, 65),
    _HpicfXcvrManufacDate_Type()
)
hpicfXcvrManufacDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrManufacDate.setStatus("current")
_HpicfXcvrChannelInfoTable_Object = MibTable
hpicfXcvrChannelInfoTable = _HpicfXcvrChannelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfXcvrChannelInfoTable.setStatus("current")
_HpicfXcvrChannelInfoEntry_Object = MibTableRow
hpicfXcvrChannelInfoEntry = _HpicfXcvrChannelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 2, 1)
)
hpicfXcvrChannelInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrChannel"),
)
if mibBuilder.loadTexts:
    hpicfXcvrChannelInfoEntry.setStatus("current")
_HpicfXcvrChannel_Type = Unsigned32
_HpicfXcvrChannel_Object = MibTableColumn
hpicfXcvrChannel = _HpicfXcvrChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 2, 1, 1),
    _HpicfXcvrChannel_Type()
)
hpicfXcvrChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfXcvrChannel.setStatus("current")


class _HpicfXcvrChannelTxBias_Type(Unsigned32):
    """Custom type hpicfXcvrChannelTxBias based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfXcvrChannelTxBias_Type.__name__ = "Unsigned32"
_HpicfXcvrChannelTxBias_Object = MibTableColumn
hpicfXcvrChannelTxBias = _HpicfXcvrChannelTxBias_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 2, 1, 2),
    _HpicfXcvrChannelTxBias_Type()
)
hpicfXcvrChannelTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrChannelTxBias.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrChannelTxBias.setUnits("microamps")
_HpicfXcvrChannelTxPower_Type = Integer32
_HpicfXcvrChannelTxPower_Object = MibTableColumn
hpicfXcvrChannelTxPower = _HpicfXcvrChannelTxPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 2, 1, 3),
    _HpicfXcvrChannelTxPower_Type()
)
hpicfXcvrChannelTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrChannelTxPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrChannelTxPower.setUnits("thousandths of dBm")
_HpicfXcvrChannelRxPower_Type = Integer32
_HpicfXcvrChannelRxPower_Object = MibTableColumn
hpicfXcvrChannelRxPower = _HpicfXcvrChannelRxPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 2, 1, 4),
    _HpicfXcvrChannelRxPower_Type()
)
hpicfXcvrChannelRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrChannelRxPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXcvrChannelRxPower.setUnits("thousandths of dBm")


class _HpicfXcvrChannelAlarms_Type(Bits):
    """Custom type hpicfXcvrChannelAlarms based on Bits"""
    namedValues = NamedValues(
        *(("rxPowerHighAlarm", 7),
          ("rxPowerHighWarning", 1),
          ("rxPowerLowAlarm", 6),
          ("rxPowerLowWarning", 0),
          ("txBiasHighAlarm", 11),
          ("txBiasHighWarning", 5),
          ("txBiasLowAlarm", 10),
          ("txBiasLowWarning", 4),
          ("txPowerHighAlarm", 9),
          ("txPowerHighWarning", 3),
          ("txPowerLowAlarm", 8),
          ("txPowerLowWarning", 2))
    )

_HpicfXcvrChannelAlarms_Type.__name__ = "Bits"
_HpicfXcvrChannelAlarms_Object = MibTableColumn
hpicfXcvrChannelAlarms = _HpicfXcvrChannelAlarms_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 2, 1, 5),
    _HpicfXcvrChannelAlarms_Type()
)
hpicfXcvrChannelAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrChannelAlarms.setStatus("current")


class _HpicfXcvrChannelErrors_Type(Bits):
    """Custom type hpicfXcvrChannelErrors based on Bits"""
    namedValues = NamedValues(
        *(("rxLossOfSignal", 2),
          ("txFault", 0),
          ("txLossOfSignal", 1))
    )

_HpicfXcvrChannelErrors_Type.__name__ = "Bits"
_HpicfXcvrChannelErrors_Object = MibTableColumn
hpicfXcvrChannelErrors = _HpicfXcvrChannelErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 1, 1, 2, 1, 6),
    _HpicfXcvrChannelErrors_Type()
)
hpicfXcvrChannelErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXcvrChannelErrors.setStatus("current")
_HpicfXcvrConformance_ObjectIdentity = ObjectIdentity
hpicfXcvrConformance = _HpicfXcvrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 2)
)
_HpicfXcvrGroups_ObjectIdentity = ObjectIdentity
hpicfXcvrGroups = _HpicfXcvrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 2, 1)
)
_HpicfXcvrCompliances_ObjectIdentity = ObjectIdentity
hpicfXcvrCompliances = _HpicfXcvrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 2, 2)
)

# Managed Objects groups

hpicfXcvrInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 2, 1, 1)
)
hpicfXcvrInfoGroup.setObjects(
      *(("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPortIndex"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPortDesc"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrModel"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrSerial"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrType"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrConnectorType"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrWavelength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTxDist"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrDiagnostics"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrDiagnosticsUpdate"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTemp"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVoltage"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBias"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRxPower"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTxPower"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrAlarms"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrErrors"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTempHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTempLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTempHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTempLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVccHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVccLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVccHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVccLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBiasHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBiasLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBiasHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBiasLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPwrOutHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPwrOutLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPwrOutHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPwrOutLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRcvPwrHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRcvPwrLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRcvPwrHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRcvPwrLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrDiagnosticsTimeStamp"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPhyLinkStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPhySpeed"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPhyDuplex"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairACableStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairACableLength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairADistanceToFault"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairAPolaritySwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairASkew"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBCableStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBCableLength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBDistanceToFault"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBPolaritySwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBSkew"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCCableStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCCableLength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCDistanceToFault"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCPolaritySwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCSkew"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDCableStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDCableLength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDDistanceToFault"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDPolaritySwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDSkew"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairABSwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCDSwap"))
)
if mibBuilder.loadTexts:
    hpicfXcvrInfoGroup.setStatus("deprecated")

hpicfXcvrInfoGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 2, 1, 2)
)
hpicfXcvrInfoGroup1.setObjects(
      *(("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPortIndex"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPortDesc"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrModel"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrSerial"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrType"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrConnectorType"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrWavelength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTxDist"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrDiagnostics"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrDiagnosticsUpdate"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTemp"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVoltage"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBias"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRxPower"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTxPower"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrAlarms"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrErrors"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTempHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTempLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTempHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTempLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVccHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVccLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVccHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVccLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBiasHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBiasLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBiasHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBiasLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPwrOutHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPwrOutLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPwrOutHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPwrOutLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRcvPwrHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRcvPwrLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRcvPwrHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRcvPwrLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPhyLinkStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPhySpeed"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPhyDuplex"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairACableStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairACableLength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairADistanceToFault"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairAPolaritySwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairASkew"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBCableStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBCableLength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBDistanceToFault"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBPolaritySwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBSkew"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCCableStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCCableLength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCDistanceToFault"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCPolaritySwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCSkew"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDCableStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDCableLength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDDistanceToFault"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDPolaritySwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDSkew"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairABSwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCDSwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrDiagnosticsTimeTicks"))
)
if mibBuilder.loadTexts:
    hpicfXcvrInfoGroup1.setStatus("deprecated")

hpicfXcvrInfoGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 2, 1, 3)
)
hpicfXcvrInfoGroup2.setObjects(
      *(("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPortIndex"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPortDesc"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrModel"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrSerial"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrType"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrConnectorType"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrWavelength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTxDist"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrDiagnostics"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrDiagnosticsUpdate"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTemp"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVoltage"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBias"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRxPower"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTxPower"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrAlarms"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrErrors"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTempHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTempLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTempHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrTempLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVccHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVccLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVccHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrVccLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBiasHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBiasLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBiasHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrBiasLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPwrOutHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPwrOutLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPwrOutHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPwrOutLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRcvPwrHiAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRcvPwrLoAlarm"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRcvPwrHiWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrRcvPwrLoWarn"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPhyLinkStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPhySpeed"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrPhyDuplex"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairACableStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairACableLength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairADistanceToFault"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairAPolaritySwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairASkew"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBCableStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBCableLength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBDistanceToFault"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBPolaritySwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairBSkew"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCCableStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCCableLength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCDistanceToFault"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCPolaritySwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCSkew"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDCableStatus"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDCableLength"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDDistanceToFault"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDPolaritySwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairDSkew"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairABSwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrMdiPairCDSwap"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrDiagnosticsTimeTicks"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrManufacDate"))
)
if mibBuilder.loadTexts:
    hpicfXcvrInfoGroup2.setStatus("current")

hpicfXcvrChannelInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 2, 1, 4)
)
hpicfXcvrChannelInfoGroup.setObjects(
      *(("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrChannelTxBias"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrChannelTxPower"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrChannelRxPower"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrChannelAlarms"),
        ("HP-ICF-TRANSCEIVER-MIB", "hpicfXcvrChannelErrors"))
)
if mibBuilder.loadTexts:
    hpicfXcvrChannelInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfXcvrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfXcvrCompliance.setStatus(
        "deprecated"
    )

hpicfXcvrCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfXcvrCompliance1.setStatus(
        "deprecated"
    )

hpicfXcvrCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfXcvrCompliance2.setStatus(
        "current"
    )

hpicfXcvrChannelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfXcvrChannelCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-TRANSCEIVER-MIB",
    **{"hpicfTransceiverMIB": hpicfTransceiverMIB,
       "hpicfXcvrObjects": hpicfXcvrObjects,
       "hpicfXcvrInfo": hpicfXcvrInfo,
       "hpicfXcvrInfoTable": hpicfXcvrInfoTable,
       "hpicfXcvrInfoEntry": hpicfXcvrInfoEntry,
       "hpicfXcvrPortIndex": hpicfXcvrPortIndex,
       "hpicfXcvrPortDesc": hpicfXcvrPortDesc,
       "hpicfXcvrModel": hpicfXcvrModel,
       "hpicfXcvrSerial": hpicfXcvrSerial,
       "hpicfXcvrType": hpicfXcvrType,
       "hpicfXcvrConnectorType": hpicfXcvrConnectorType,
       "hpicfXcvrWavelength": hpicfXcvrWavelength,
       "hpicfXcvrTxDist": hpicfXcvrTxDist,
       "hpicfXcvrDiagnostics": hpicfXcvrDiagnostics,
       "hpicfXcvrDiagnosticsUpdate": hpicfXcvrDiagnosticsUpdate,
       "hpicfXcvrTemp": hpicfXcvrTemp,
       "hpicfXcvrVoltage": hpicfXcvrVoltage,
       "hpicfXcvrBias": hpicfXcvrBias,
       "hpicfXcvrTxPower": hpicfXcvrTxPower,
       "hpicfXcvrRxPower": hpicfXcvrRxPower,
       "hpicfXcvrAlarms": hpicfXcvrAlarms,
       "hpicfXcvrErrors": hpicfXcvrErrors,
       "hpicfXcvrTempHiAlarm": hpicfXcvrTempHiAlarm,
       "hpicfXcvrTempLoAlarm": hpicfXcvrTempLoAlarm,
       "hpicfXcvrTempHiWarn": hpicfXcvrTempHiWarn,
       "hpicfXcvrTempLoWarn": hpicfXcvrTempLoWarn,
       "hpicfXcvrVccHiAlarm": hpicfXcvrVccHiAlarm,
       "hpicfXcvrVccLoAlarm": hpicfXcvrVccLoAlarm,
       "hpicfXcvrVccHiWarn": hpicfXcvrVccHiWarn,
       "hpicfXcvrVccLoWarn": hpicfXcvrVccLoWarn,
       "hpicfXcvrBiasHiAlarm": hpicfXcvrBiasHiAlarm,
       "hpicfXcvrBiasLoAlarm": hpicfXcvrBiasLoAlarm,
       "hpicfXcvrBiasHiWarn": hpicfXcvrBiasHiWarn,
       "hpicfXcvrBiasLoWarn": hpicfXcvrBiasLoWarn,
       "hpicfXcvrPwrOutHiAlarm": hpicfXcvrPwrOutHiAlarm,
       "hpicfXcvrPwrOutLoAlarm": hpicfXcvrPwrOutLoAlarm,
       "hpicfXcvrPwrOutHiWarn": hpicfXcvrPwrOutHiWarn,
       "hpicfXcvrPwrOutLoWarn": hpicfXcvrPwrOutLoWarn,
       "hpicfXcvrRcvPwrHiAlarm": hpicfXcvrRcvPwrHiAlarm,
       "hpicfXcvrRcvPwrLoAlarm": hpicfXcvrRcvPwrLoAlarm,
       "hpicfXcvrRcvPwrHiWarn": hpicfXcvrRcvPwrHiWarn,
       "hpicfXcvrRcvPwrLoWarn": hpicfXcvrRcvPwrLoWarn,
       "hpicfXcvrDiagnosticsTimeStamp": hpicfXcvrDiagnosticsTimeStamp,
       "hpicfXcvrPhyLinkStatus": hpicfXcvrPhyLinkStatus,
       "hpicfXcvrPhySpeed": hpicfXcvrPhySpeed,
       "hpicfXcvrPhyDuplex": hpicfXcvrPhyDuplex,
       "hpicfXcvrMdiPairACableStatus": hpicfXcvrMdiPairACableStatus,
       "hpicfXcvrMdiPairACableLength": hpicfXcvrMdiPairACableLength,
       "hpicfXcvrMdiPairADistanceToFault": hpicfXcvrMdiPairADistanceToFault,
       "hpicfXcvrMdiPairAPolaritySwap": hpicfXcvrMdiPairAPolaritySwap,
       "hpicfXcvrMdiPairASkew": hpicfXcvrMdiPairASkew,
       "hpicfXcvrMdiPairBCableStatus": hpicfXcvrMdiPairBCableStatus,
       "hpicfXcvrMdiPairBCableLength": hpicfXcvrMdiPairBCableLength,
       "hpicfXcvrMdiPairBDistanceToFault": hpicfXcvrMdiPairBDistanceToFault,
       "hpicfXcvrMdiPairBPolaritySwap": hpicfXcvrMdiPairBPolaritySwap,
       "hpicfXcvrMdiPairBSkew": hpicfXcvrMdiPairBSkew,
       "hpicfXcvrMdiPairCCableStatus": hpicfXcvrMdiPairCCableStatus,
       "hpicfXcvrMdiPairCCableLength": hpicfXcvrMdiPairCCableLength,
       "hpicfXcvrMdiPairCDistanceToFault": hpicfXcvrMdiPairCDistanceToFault,
       "hpicfXcvrMdiPairCPolaritySwap": hpicfXcvrMdiPairCPolaritySwap,
       "hpicfXcvrMdiPairCSkew": hpicfXcvrMdiPairCSkew,
       "hpicfXcvrMdiPairDCableStatus": hpicfXcvrMdiPairDCableStatus,
       "hpicfXcvrMdiPairDCableLength": hpicfXcvrMdiPairDCableLength,
       "hpicfXcvrMdiPairDDistanceToFault": hpicfXcvrMdiPairDDistanceToFault,
       "hpicfXcvrMdiPairDPolaritySwap": hpicfXcvrMdiPairDPolaritySwap,
       "hpicfXcvrMdiPairDSkew": hpicfXcvrMdiPairDSkew,
       "hpicfXcvrMdiPairABSwap": hpicfXcvrMdiPairABSwap,
       "hpicfXcvrMdiPairCDSwap": hpicfXcvrMdiPairCDSwap,
       "hpicfXcvrDiagnosticsTimeTicks": hpicfXcvrDiagnosticsTimeTicks,
       "hpicfXcvrManufacDate": hpicfXcvrManufacDate,
       "hpicfXcvrChannelInfoTable": hpicfXcvrChannelInfoTable,
       "hpicfXcvrChannelInfoEntry": hpicfXcvrChannelInfoEntry,
       "hpicfXcvrChannel": hpicfXcvrChannel,
       "hpicfXcvrChannelTxBias": hpicfXcvrChannelTxBias,
       "hpicfXcvrChannelTxPower": hpicfXcvrChannelTxPower,
       "hpicfXcvrChannelRxPower": hpicfXcvrChannelRxPower,
       "hpicfXcvrChannelAlarms": hpicfXcvrChannelAlarms,
       "hpicfXcvrChannelErrors": hpicfXcvrChannelErrors,
       "hpicfXcvrConformance": hpicfXcvrConformance,
       "hpicfXcvrGroups": hpicfXcvrGroups,
       "hpicfXcvrInfoGroup": hpicfXcvrInfoGroup,
       "hpicfXcvrInfoGroup1": hpicfXcvrInfoGroup1,
       "hpicfXcvrInfoGroup2": hpicfXcvrInfoGroup2,
       "hpicfXcvrChannelInfoGroup": hpicfXcvrChannelInfoGroup,
       "hpicfXcvrCompliances": hpicfXcvrCompliances,
       "hpicfXcvrCompliance": hpicfXcvrCompliance,
       "hpicfXcvrCompliance1": hpicfXcvrCompliance1,
       "hpicfXcvrCompliance2": hpicfXcvrCompliance2,
       "hpicfXcvrChannelCompliance": hpicfXcvrChannelCompliance}
)
