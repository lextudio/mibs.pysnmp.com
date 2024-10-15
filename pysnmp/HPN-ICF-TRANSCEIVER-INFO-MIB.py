# SNMP MIB module (HPN-ICF-TRANSCEIVER-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-TRANSCEIVER-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:00 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# MODULE-IDENTITY

hpnicfTransceiver = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70)
)
hpnicfTransceiver.setRevisions(
        ("2013-07-23 16:50",
         "2009-12-29 16:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfTransceiverInfoAdm_ObjectIdentity = ObjectIdentity
hpnicfTransceiverInfoAdm = _HpnicfTransceiverInfoAdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1)
)
_HpnicfTransceiverInfoTable_Object = MibTable
hpnicfTransceiverInfoTable = _HpnicfTransceiverInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfTransceiverInfoTable.setStatus("current")
_HpnicfTransceiverInfoEntry_Object = MibTableRow
hpnicfTransceiverInfoEntry = _HpnicfTransceiverInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1)
)
hpnicfTransceiverInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfTransceiverInfoEntry.setStatus("current")
_HpnicfTransceiverHardwareType_Type = OctetString
_HpnicfTransceiverHardwareType_Object = MibTableColumn
hpnicfTransceiverHardwareType = _HpnicfTransceiverHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 1),
    _HpnicfTransceiverHardwareType_Type()
)
hpnicfTransceiverHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverHardwareType.setStatus("current")
_HpnicfTransceiverType_Type = OctetString
_HpnicfTransceiverType_Object = MibTableColumn
hpnicfTransceiverType = _HpnicfTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 2),
    _HpnicfTransceiverType_Type()
)
hpnicfTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverType.setStatus("current")
_HpnicfTransceiverWaveLength_Type = Integer32
_HpnicfTransceiverWaveLength_Object = MibTableColumn
hpnicfTransceiverWaveLength = _HpnicfTransceiverWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 3),
    _HpnicfTransceiverWaveLength_Type()
)
hpnicfTransceiverWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverWaveLength.setStatus("current")
_HpnicfTransceiverVendorName_Type = OctetString
_HpnicfTransceiverVendorName_Object = MibTableColumn
hpnicfTransceiverVendorName = _HpnicfTransceiverVendorName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 4),
    _HpnicfTransceiverVendorName_Type()
)
hpnicfTransceiverVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverVendorName.setStatus("current")
_HpnicfTransceiverSerialNumber_Type = OctetString
_HpnicfTransceiverSerialNumber_Object = MibTableColumn
hpnicfTransceiverSerialNumber = _HpnicfTransceiverSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 5),
    _HpnicfTransceiverSerialNumber_Type()
)
hpnicfTransceiverSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverSerialNumber.setStatus("current")


class _HpnicfTransceiverFiberDiameterType_Type(Integer32):
    """Custom type hpnicfTransceiverFiberDiameterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("copper", 4),
          ("fiber50", 2),
          ("fiber625", 3),
          ("fiber9", 1),
          ("unknown", 65535))
    )


_HpnicfTransceiverFiberDiameterType_Type.__name__ = "Integer32"
_HpnicfTransceiverFiberDiameterType_Object = MibTableColumn
hpnicfTransceiverFiberDiameterType = _HpnicfTransceiverFiberDiameterType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 6),
    _HpnicfTransceiverFiberDiameterType_Type()
)
hpnicfTransceiverFiberDiameterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverFiberDiameterType.setStatus("current")
_HpnicfTransceiverTransferDistance_Type = Integer32
_HpnicfTransceiverTransferDistance_Object = MibTableColumn
hpnicfTransceiverTransferDistance = _HpnicfTransceiverTransferDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 7),
    _HpnicfTransceiverTransferDistance_Type()
)
hpnicfTransceiverTransferDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverTransferDistance.setStatus("current")
_HpnicfTransceiverDiagnostic_Type = TruthValue
_HpnicfTransceiverDiagnostic_Object = MibTableColumn
hpnicfTransceiverDiagnostic = _HpnicfTransceiverDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 8),
    _HpnicfTransceiverDiagnostic_Type()
)
hpnicfTransceiverDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverDiagnostic.setStatus("current")
_HpnicfTransceiverCurTXPower_Type = Integer32
_HpnicfTransceiverCurTXPower_Object = MibTableColumn
hpnicfTransceiverCurTXPower = _HpnicfTransceiverCurTXPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 9),
    _HpnicfTransceiverCurTXPower_Type()
)
hpnicfTransceiverCurTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverCurTXPower.setStatus("current")
_HpnicfTransceiverMaxTXPower_Type = Integer32
_HpnicfTransceiverMaxTXPower_Object = MibTableColumn
hpnicfTransceiverMaxTXPower = _HpnicfTransceiverMaxTXPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 10),
    _HpnicfTransceiverMaxTXPower_Type()
)
hpnicfTransceiverMaxTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverMaxTXPower.setStatus("current")
_HpnicfTransceiverMinTXPower_Type = Integer32
_HpnicfTransceiverMinTXPower_Object = MibTableColumn
hpnicfTransceiverMinTXPower = _HpnicfTransceiverMinTXPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 11),
    _HpnicfTransceiverMinTXPower_Type()
)
hpnicfTransceiverMinTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverMinTXPower.setStatus("current")
_HpnicfTransceiverCurRXPower_Type = Integer32
_HpnicfTransceiverCurRXPower_Object = MibTableColumn
hpnicfTransceiverCurRXPower = _HpnicfTransceiverCurRXPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 12),
    _HpnicfTransceiverCurRXPower_Type()
)
hpnicfTransceiverCurRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverCurRXPower.setStatus("current")
_HpnicfTransceiverMaxRXPower_Type = Integer32
_HpnicfTransceiverMaxRXPower_Object = MibTableColumn
hpnicfTransceiverMaxRXPower = _HpnicfTransceiverMaxRXPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 13),
    _HpnicfTransceiverMaxRXPower_Type()
)
hpnicfTransceiverMaxRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverMaxRXPower.setStatus("current")
_HpnicfTransceiverMinRXPower_Type = Integer32
_HpnicfTransceiverMinRXPower_Object = MibTableColumn
hpnicfTransceiverMinRXPower = _HpnicfTransceiverMinRXPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 14),
    _HpnicfTransceiverMinRXPower_Type()
)
hpnicfTransceiverMinRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverMinRXPower.setStatus("current")
_HpnicfTransceiverTemperature_Type = Integer32
_HpnicfTransceiverTemperature_Object = MibTableColumn
hpnicfTransceiverTemperature = _HpnicfTransceiverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 15),
    _HpnicfTransceiverTemperature_Type()
)
hpnicfTransceiverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverTemperature.setStatus("current")
_HpnicfTransceiverVoltage_Type = Integer32
_HpnicfTransceiverVoltage_Object = MibTableColumn
hpnicfTransceiverVoltage = _HpnicfTransceiverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 16),
    _HpnicfTransceiverVoltage_Type()
)
hpnicfTransceiverVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverVoltage.setStatus("current")
_HpnicfTransceiverBiasCurrent_Type = Integer32
_HpnicfTransceiverBiasCurrent_Object = MibTableColumn
hpnicfTransceiverBiasCurrent = _HpnicfTransceiverBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 17),
    _HpnicfTransceiverBiasCurrent_Type()
)
hpnicfTransceiverBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverBiasCurrent.setStatus("current")
_HpnicfTransceiverTempHiAlarm_Type = Integer32
_HpnicfTransceiverTempHiAlarm_Object = MibTableColumn
hpnicfTransceiverTempHiAlarm = _HpnicfTransceiverTempHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 18),
    _HpnicfTransceiverTempHiAlarm_Type()
)
hpnicfTransceiverTempHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverTempHiAlarm.setStatus("current")
_HpnicfTransceiverTempLoAlarm_Type = Integer32
_HpnicfTransceiverTempLoAlarm_Object = MibTableColumn
hpnicfTransceiverTempLoAlarm = _HpnicfTransceiverTempLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 19),
    _HpnicfTransceiverTempLoAlarm_Type()
)
hpnicfTransceiverTempLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverTempLoAlarm.setStatus("current")
_HpnicfTransceiverTempHiWarn_Type = Integer32
_HpnicfTransceiverTempHiWarn_Object = MibTableColumn
hpnicfTransceiverTempHiWarn = _HpnicfTransceiverTempHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 20),
    _HpnicfTransceiverTempHiWarn_Type()
)
hpnicfTransceiverTempHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverTempHiWarn.setStatus("current")
_HpnicfTransceiverTempLoWarn_Type = Integer32
_HpnicfTransceiverTempLoWarn_Object = MibTableColumn
hpnicfTransceiverTempLoWarn = _HpnicfTransceiverTempLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 21),
    _HpnicfTransceiverTempLoWarn_Type()
)
hpnicfTransceiverTempLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverTempLoWarn.setStatus("current")
_HpnicfTransceiverVccHiAlarm_Type = Integer32
_HpnicfTransceiverVccHiAlarm_Object = MibTableColumn
hpnicfTransceiverVccHiAlarm = _HpnicfTransceiverVccHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 22),
    _HpnicfTransceiverVccHiAlarm_Type()
)
hpnicfTransceiverVccHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverVccHiAlarm.setStatus("current")
_HpnicfTransceiverVccLoAlarm_Type = Integer32
_HpnicfTransceiverVccLoAlarm_Object = MibTableColumn
hpnicfTransceiverVccLoAlarm = _HpnicfTransceiverVccLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 23),
    _HpnicfTransceiverVccLoAlarm_Type()
)
hpnicfTransceiverVccLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverVccLoAlarm.setStatus("current")
_HpnicfTransceiverVccHiWarn_Type = Integer32
_HpnicfTransceiverVccHiWarn_Object = MibTableColumn
hpnicfTransceiverVccHiWarn = _HpnicfTransceiverVccHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 24),
    _HpnicfTransceiverVccHiWarn_Type()
)
hpnicfTransceiverVccHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverVccHiWarn.setStatus("current")
_HpnicfTransceiverVccLoWarn_Type = Integer32
_HpnicfTransceiverVccLoWarn_Object = MibTableColumn
hpnicfTransceiverVccLoWarn = _HpnicfTransceiverVccLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 25),
    _HpnicfTransceiverVccLoWarn_Type()
)
hpnicfTransceiverVccLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverVccLoWarn.setStatus("current")
_HpnicfTransceiverBiasHiAlarm_Type = Integer32
_HpnicfTransceiverBiasHiAlarm_Object = MibTableColumn
hpnicfTransceiverBiasHiAlarm = _HpnicfTransceiverBiasHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 26),
    _HpnicfTransceiverBiasHiAlarm_Type()
)
hpnicfTransceiverBiasHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverBiasHiAlarm.setStatus("current")
_HpnicfTransceiverBiasLoAlarm_Type = Integer32
_HpnicfTransceiverBiasLoAlarm_Object = MibTableColumn
hpnicfTransceiverBiasLoAlarm = _HpnicfTransceiverBiasLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 27),
    _HpnicfTransceiverBiasLoAlarm_Type()
)
hpnicfTransceiverBiasLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverBiasLoAlarm.setStatus("current")
_HpnicfTransceiverBiasHiWarn_Type = Integer32
_HpnicfTransceiverBiasHiWarn_Object = MibTableColumn
hpnicfTransceiverBiasHiWarn = _HpnicfTransceiverBiasHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 28),
    _HpnicfTransceiverBiasHiWarn_Type()
)
hpnicfTransceiverBiasHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverBiasHiWarn.setStatus("current")
_HpnicfTransceiverBiasLoWarn_Type = Integer32
_HpnicfTransceiverBiasLoWarn_Object = MibTableColumn
hpnicfTransceiverBiasLoWarn = _HpnicfTransceiverBiasLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 29),
    _HpnicfTransceiverBiasLoWarn_Type()
)
hpnicfTransceiverBiasLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverBiasLoWarn.setStatus("current")
_HpnicfTransceiverPwrOutHiAlarm_Type = Integer32
_HpnicfTransceiverPwrOutHiAlarm_Object = MibTableColumn
hpnicfTransceiverPwrOutHiAlarm = _HpnicfTransceiverPwrOutHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 30),
    _HpnicfTransceiverPwrOutHiAlarm_Type()
)
hpnicfTransceiverPwrOutHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverPwrOutHiAlarm.setStatus("current")
_HpnicfTransceiverPwrOutLoAlarm_Type = Integer32
_HpnicfTransceiverPwrOutLoAlarm_Object = MibTableColumn
hpnicfTransceiverPwrOutLoAlarm = _HpnicfTransceiverPwrOutLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 31),
    _HpnicfTransceiverPwrOutLoAlarm_Type()
)
hpnicfTransceiverPwrOutLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverPwrOutLoAlarm.setStatus("current")
_HpnicfTransceiverPwrOutHiWarn_Type = Integer32
_HpnicfTransceiverPwrOutHiWarn_Object = MibTableColumn
hpnicfTransceiverPwrOutHiWarn = _HpnicfTransceiverPwrOutHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 32),
    _HpnicfTransceiverPwrOutHiWarn_Type()
)
hpnicfTransceiverPwrOutHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverPwrOutHiWarn.setStatus("current")
_HpnicfTransceiverPwrOutLoWarn_Type = Integer32
_HpnicfTransceiverPwrOutLoWarn_Object = MibTableColumn
hpnicfTransceiverPwrOutLoWarn = _HpnicfTransceiverPwrOutLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 33),
    _HpnicfTransceiverPwrOutLoWarn_Type()
)
hpnicfTransceiverPwrOutLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverPwrOutLoWarn.setStatus("current")
_HpnicfTransceiverRcvPwrHiAlarm_Type = Integer32
_HpnicfTransceiverRcvPwrHiAlarm_Object = MibTableColumn
hpnicfTransceiverRcvPwrHiAlarm = _HpnicfTransceiverRcvPwrHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 34),
    _HpnicfTransceiverRcvPwrHiAlarm_Type()
)
hpnicfTransceiverRcvPwrHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverRcvPwrHiAlarm.setStatus("current")
_HpnicfTransceiverRcvPwrLoAlarm_Type = Integer32
_HpnicfTransceiverRcvPwrLoAlarm_Object = MibTableColumn
hpnicfTransceiverRcvPwrLoAlarm = _HpnicfTransceiverRcvPwrLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 35),
    _HpnicfTransceiverRcvPwrLoAlarm_Type()
)
hpnicfTransceiverRcvPwrLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverRcvPwrLoAlarm.setStatus("current")
_HpnicfTransceiverRcvPwrHiWarn_Type = Integer32
_HpnicfTransceiverRcvPwrHiWarn_Object = MibTableColumn
hpnicfTransceiverRcvPwrHiWarn = _HpnicfTransceiverRcvPwrHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 36),
    _HpnicfTransceiverRcvPwrHiWarn_Type()
)
hpnicfTransceiverRcvPwrHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverRcvPwrHiWarn.setStatus("current")
_HpnicfTransceiverRcvPwrLoWarn_Type = Integer32
_HpnicfTransceiverRcvPwrLoWarn_Object = MibTableColumn
hpnicfTransceiverRcvPwrLoWarn = _HpnicfTransceiverRcvPwrLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 37),
    _HpnicfTransceiverRcvPwrLoWarn_Type()
)
hpnicfTransceiverRcvPwrLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverRcvPwrLoWarn.setStatus("current")


class _HpnicfTransceiverErrors_Type(Bits):
    """Custom type hpnicfTransceiverErrors based on Bits"""
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

_HpnicfTransceiverErrors_Type.__name__ = "Bits"
_HpnicfTransceiverErrors_Object = MibTableColumn
hpnicfTransceiverErrors = _HpnicfTransceiverErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 38),
    _HpnicfTransceiverErrors_Type()
)
hpnicfTransceiverErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverErrors.setStatus("current")
_HpnicfTransceiverChannelTable_Object = MibTable
hpnicfTransceiverChannelTable = _HpnicfTransceiverChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfTransceiverChannelTable.setStatus("current")
_HpnicfTransceiverChannelEntry_Object = MibTableRow
hpnicfTransceiverChannelEntry = _HpnicfTransceiverChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2, 1)
)
hpnicfTransceiverChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-TRANSCEIVER-INFO-MIB", "hpnicfTransceiverChannelIndex"),
)
if mibBuilder.loadTexts:
    hpnicfTransceiverChannelEntry.setStatus("current")


class _HpnicfTransceiverChannelIndex_Type(Integer32):
    """Custom type hpnicfTransceiverChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfTransceiverChannelIndex_Type.__name__ = "Integer32"
_HpnicfTransceiverChannelIndex_Object = MibTableColumn
hpnicfTransceiverChannelIndex = _HpnicfTransceiverChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2, 1, 1),
    _HpnicfTransceiverChannelIndex_Type()
)
hpnicfTransceiverChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTransceiverChannelIndex.setStatus("current")
_HpnicfTransceiverChannelCurTXPower_Type = Integer32
_HpnicfTransceiverChannelCurTXPower_Object = MibTableColumn
hpnicfTransceiverChannelCurTXPower = _HpnicfTransceiverChannelCurTXPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2, 1, 2),
    _HpnicfTransceiverChannelCurTXPower_Type()
)
hpnicfTransceiverChannelCurTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverChannelCurTXPower.setStatus("current")
_HpnicfTransceiverChannelCurRXPower_Type = Integer32
_HpnicfTransceiverChannelCurRXPower_Object = MibTableColumn
hpnicfTransceiverChannelCurRXPower = _HpnicfTransceiverChannelCurRXPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2, 1, 3),
    _HpnicfTransceiverChannelCurRXPower_Type()
)
hpnicfTransceiverChannelCurRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverChannelCurRXPower.setStatus("current")
_HpnicfTransceiverChannelTemperature_Type = Integer32
_HpnicfTransceiverChannelTemperature_Object = MibTableColumn
hpnicfTransceiverChannelTemperature = _HpnicfTransceiverChannelTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2, 1, 4),
    _HpnicfTransceiverChannelTemperature_Type()
)
hpnicfTransceiverChannelTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverChannelTemperature.setStatus("current")
_HpnicfTransceiverChannelBiasCurrent_Type = Integer32
_HpnicfTransceiverChannelBiasCurrent_Object = MibTableColumn
hpnicfTransceiverChannelBiasCurrent = _HpnicfTransceiverChannelBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2, 1, 5),
    _HpnicfTransceiverChannelBiasCurrent_Type()
)
hpnicfTransceiverChannelBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTransceiverChannelBiasCurrent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-TRANSCEIVER-INFO-MIB",
    **{"hpnicfTransceiver": hpnicfTransceiver,
       "hpnicfTransceiverInfoAdm": hpnicfTransceiverInfoAdm,
       "hpnicfTransceiverInfoTable": hpnicfTransceiverInfoTable,
       "hpnicfTransceiverInfoEntry": hpnicfTransceiverInfoEntry,
       "hpnicfTransceiverHardwareType": hpnicfTransceiverHardwareType,
       "hpnicfTransceiverType": hpnicfTransceiverType,
       "hpnicfTransceiverWaveLength": hpnicfTransceiverWaveLength,
       "hpnicfTransceiverVendorName": hpnicfTransceiverVendorName,
       "hpnicfTransceiverSerialNumber": hpnicfTransceiverSerialNumber,
       "hpnicfTransceiverFiberDiameterType": hpnicfTransceiverFiberDiameterType,
       "hpnicfTransceiverTransferDistance": hpnicfTransceiverTransferDistance,
       "hpnicfTransceiverDiagnostic": hpnicfTransceiverDiagnostic,
       "hpnicfTransceiverCurTXPower": hpnicfTransceiverCurTXPower,
       "hpnicfTransceiverMaxTXPower": hpnicfTransceiverMaxTXPower,
       "hpnicfTransceiverMinTXPower": hpnicfTransceiverMinTXPower,
       "hpnicfTransceiverCurRXPower": hpnicfTransceiverCurRXPower,
       "hpnicfTransceiverMaxRXPower": hpnicfTransceiverMaxRXPower,
       "hpnicfTransceiverMinRXPower": hpnicfTransceiverMinRXPower,
       "hpnicfTransceiverTemperature": hpnicfTransceiverTemperature,
       "hpnicfTransceiverVoltage": hpnicfTransceiverVoltage,
       "hpnicfTransceiverBiasCurrent": hpnicfTransceiverBiasCurrent,
       "hpnicfTransceiverTempHiAlarm": hpnicfTransceiverTempHiAlarm,
       "hpnicfTransceiverTempLoAlarm": hpnicfTransceiverTempLoAlarm,
       "hpnicfTransceiverTempHiWarn": hpnicfTransceiverTempHiWarn,
       "hpnicfTransceiverTempLoWarn": hpnicfTransceiverTempLoWarn,
       "hpnicfTransceiverVccHiAlarm": hpnicfTransceiverVccHiAlarm,
       "hpnicfTransceiverVccLoAlarm": hpnicfTransceiverVccLoAlarm,
       "hpnicfTransceiverVccHiWarn": hpnicfTransceiverVccHiWarn,
       "hpnicfTransceiverVccLoWarn": hpnicfTransceiverVccLoWarn,
       "hpnicfTransceiverBiasHiAlarm": hpnicfTransceiverBiasHiAlarm,
       "hpnicfTransceiverBiasLoAlarm": hpnicfTransceiverBiasLoAlarm,
       "hpnicfTransceiverBiasHiWarn": hpnicfTransceiverBiasHiWarn,
       "hpnicfTransceiverBiasLoWarn": hpnicfTransceiverBiasLoWarn,
       "hpnicfTransceiverPwrOutHiAlarm": hpnicfTransceiverPwrOutHiAlarm,
       "hpnicfTransceiverPwrOutLoAlarm": hpnicfTransceiverPwrOutLoAlarm,
       "hpnicfTransceiverPwrOutHiWarn": hpnicfTransceiverPwrOutHiWarn,
       "hpnicfTransceiverPwrOutLoWarn": hpnicfTransceiverPwrOutLoWarn,
       "hpnicfTransceiverRcvPwrHiAlarm": hpnicfTransceiverRcvPwrHiAlarm,
       "hpnicfTransceiverRcvPwrLoAlarm": hpnicfTransceiverRcvPwrLoAlarm,
       "hpnicfTransceiverRcvPwrHiWarn": hpnicfTransceiverRcvPwrHiWarn,
       "hpnicfTransceiverRcvPwrLoWarn": hpnicfTransceiverRcvPwrLoWarn,
       "hpnicfTransceiverErrors": hpnicfTransceiverErrors,
       "hpnicfTransceiverChannelTable": hpnicfTransceiverChannelTable,
       "hpnicfTransceiverChannelEntry": hpnicfTransceiverChannelEntry,
       "hpnicfTransceiverChannelIndex": hpnicfTransceiverChannelIndex,
       "hpnicfTransceiverChannelCurTXPower": hpnicfTransceiverChannelCurTXPower,
       "hpnicfTransceiverChannelCurRXPower": hpnicfTransceiverChannelCurRXPower,
       "hpnicfTransceiverChannelTemperature": hpnicfTransceiverChannelTemperature,
       "hpnicfTransceiverChannelBiasCurrent": hpnicfTransceiverChannelBiasCurrent}
)
