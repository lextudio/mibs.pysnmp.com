# SNMP MIB module (HH3C-TRANSCEIVER-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-TRANSCEIVER-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:06 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cTransceiver = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70)
)
hh3cTransceiver.setRevisions(
        ("2014-08-11 10:50",
         "2013-06-06 00:00",
         "2012-06-06 00:00",
         "2009-12-29 00:00",
         "2006-06-08 00:00",
         "2006-01-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cTransceiverInfoAdm_ObjectIdentity = ObjectIdentity
hh3cTransceiverInfoAdm = _Hh3cTransceiverInfoAdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1)
)
_Hh3cTransceiverInfoTable_Object = MibTable
hh3cTransceiverInfoTable = _Hh3cTransceiverInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cTransceiverInfoTable.setStatus("current")
_Hh3cTransceiverInfoEntry_Object = MibTableRow
hh3cTransceiverInfoEntry = _Hh3cTransceiverInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1)
)
hh3cTransceiverInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cTransceiverInfoEntry.setStatus("current")
_Hh3cTransceiverHardwareType_Type = OctetString
_Hh3cTransceiverHardwareType_Object = MibTableColumn
hh3cTransceiverHardwareType = _Hh3cTransceiverHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 1),
    _Hh3cTransceiverHardwareType_Type()
)
hh3cTransceiverHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverHardwareType.setStatus("current")
_Hh3cTransceiverType_Type = OctetString
_Hh3cTransceiverType_Object = MibTableColumn
hh3cTransceiverType = _Hh3cTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 2),
    _Hh3cTransceiverType_Type()
)
hh3cTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverType.setStatus("current")
_Hh3cTransceiverWaveLength_Type = Integer32
_Hh3cTransceiverWaveLength_Object = MibTableColumn
hh3cTransceiverWaveLength = _Hh3cTransceiverWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 3),
    _Hh3cTransceiverWaveLength_Type()
)
hh3cTransceiverWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverWaveLength.setStatus("current")
_Hh3cTransceiverVendorName_Type = OctetString
_Hh3cTransceiverVendorName_Object = MibTableColumn
hh3cTransceiverVendorName = _Hh3cTransceiverVendorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 4),
    _Hh3cTransceiverVendorName_Type()
)
hh3cTransceiverVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverVendorName.setStatus("current")
_Hh3cTransceiverSerialNumber_Type = OctetString
_Hh3cTransceiverSerialNumber_Object = MibTableColumn
hh3cTransceiverSerialNumber = _Hh3cTransceiverSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 5),
    _Hh3cTransceiverSerialNumber_Type()
)
hh3cTransceiverSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverSerialNumber.setStatus("current")


class _Hh3cTransceiverFiberDiameterType_Type(Integer32):
    """Custom type hh3cTransceiverFiberDiameterType based on Integer32"""
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


_Hh3cTransceiverFiberDiameterType_Type.__name__ = "Integer32"
_Hh3cTransceiverFiberDiameterType_Object = MibTableColumn
hh3cTransceiverFiberDiameterType = _Hh3cTransceiverFiberDiameterType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 6),
    _Hh3cTransceiverFiberDiameterType_Type()
)
hh3cTransceiverFiberDiameterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverFiberDiameterType.setStatus("current")
_Hh3cTransceiverTransferDistance_Type = Integer32
_Hh3cTransceiverTransferDistance_Object = MibTableColumn
hh3cTransceiverTransferDistance = _Hh3cTransceiverTransferDistance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 7),
    _Hh3cTransceiverTransferDistance_Type()
)
hh3cTransceiverTransferDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverTransferDistance.setStatus("current")
_Hh3cTransceiverDiagnostic_Type = TruthValue
_Hh3cTransceiverDiagnostic_Object = MibTableColumn
hh3cTransceiverDiagnostic = _Hh3cTransceiverDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 8),
    _Hh3cTransceiverDiagnostic_Type()
)
hh3cTransceiverDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverDiagnostic.setStatus("current")
_Hh3cTransceiverCurTXPower_Type = Integer32
_Hh3cTransceiverCurTXPower_Object = MibTableColumn
hh3cTransceiverCurTXPower = _Hh3cTransceiverCurTXPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 9),
    _Hh3cTransceiverCurTXPower_Type()
)
hh3cTransceiverCurTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverCurTXPower.setStatus("current")
_Hh3cTransceiverMaxTXPower_Type = Integer32
_Hh3cTransceiverMaxTXPower_Object = MibTableColumn
hh3cTransceiverMaxTXPower = _Hh3cTransceiverMaxTXPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 10),
    _Hh3cTransceiverMaxTXPower_Type()
)
hh3cTransceiverMaxTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverMaxTXPower.setStatus("current")
_Hh3cTransceiverMinTXPower_Type = Integer32
_Hh3cTransceiverMinTXPower_Object = MibTableColumn
hh3cTransceiverMinTXPower = _Hh3cTransceiverMinTXPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 11),
    _Hh3cTransceiverMinTXPower_Type()
)
hh3cTransceiverMinTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverMinTXPower.setStatus("current")
_Hh3cTransceiverCurRXPower_Type = Integer32
_Hh3cTransceiverCurRXPower_Object = MibTableColumn
hh3cTransceiverCurRXPower = _Hh3cTransceiverCurRXPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 12),
    _Hh3cTransceiverCurRXPower_Type()
)
hh3cTransceiverCurRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverCurRXPower.setStatus("current")
_Hh3cTransceiverMaxRXPower_Type = Integer32
_Hh3cTransceiverMaxRXPower_Object = MibTableColumn
hh3cTransceiverMaxRXPower = _Hh3cTransceiverMaxRXPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 13),
    _Hh3cTransceiverMaxRXPower_Type()
)
hh3cTransceiverMaxRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverMaxRXPower.setStatus("current")
_Hh3cTransceiverMinRXPower_Type = Integer32
_Hh3cTransceiverMinRXPower_Object = MibTableColumn
hh3cTransceiverMinRXPower = _Hh3cTransceiverMinRXPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 14),
    _Hh3cTransceiverMinRXPower_Type()
)
hh3cTransceiverMinRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverMinRXPower.setStatus("current")
_Hh3cTransceiverTemperature_Type = Integer32
_Hh3cTransceiverTemperature_Object = MibTableColumn
hh3cTransceiverTemperature = _Hh3cTransceiverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 15),
    _Hh3cTransceiverTemperature_Type()
)
hh3cTransceiverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverTemperature.setStatus("current")
_Hh3cTransceiverVoltage_Type = Integer32
_Hh3cTransceiverVoltage_Object = MibTableColumn
hh3cTransceiverVoltage = _Hh3cTransceiverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 16),
    _Hh3cTransceiverVoltage_Type()
)
hh3cTransceiverVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverVoltage.setStatus("current")
_Hh3cTransceiverBiasCurrent_Type = Integer32
_Hh3cTransceiverBiasCurrent_Object = MibTableColumn
hh3cTransceiverBiasCurrent = _Hh3cTransceiverBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 17),
    _Hh3cTransceiverBiasCurrent_Type()
)
hh3cTransceiverBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverBiasCurrent.setStatus("current")
_Hh3cTransceiverTempHiAlarm_Type = Integer32
_Hh3cTransceiverTempHiAlarm_Object = MibTableColumn
hh3cTransceiverTempHiAlarm = _Hh3cTransceiverTempHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 18),
    _Hh3cTransceiverTempHiAlarm_Type()
)
hh3cTransceiverTempHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverTempHiAlarm.setStatus("current")
_Hh3cTransceiverTempLoAlarm_Type = Integer32
_Hh3cTransceiverTempLoAlarm_Object = MibTableColumn
hh3cTransceiverTempLoAlarm = _Hh3cTransceiverTempLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 19),
    _Hh3cTransceiverTempLoAlarm_Type()
)
hh3cTransceiverTempLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverTempLoAlarm.setStatus("current")
_Hh3cTransceiverTempHiWarn_Type = Integer32
_Hh3cTransceiverTempHiWarn_Object = MibTableColumn
hh3cTransceiverTempHiWarn = _Hh3cTransceiverTempHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 20),
    _Hh3cTransceiverTempHiWarn_Type()
)
hh3cTransceiverTempHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverTempHiWarn.setStatus("current")
_Hh3cTransceiverTempLoWarn_Type = Integer32
_Hh3cTransceiverTempLoWarn_Object = MibTableColumn
hh3cTransceiverTempLoWarn = _Hh3cTransceiverTempLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 21),
    _Hh3cTransceiverTempLoWarn_Type()
)
hh3cTransceiverTempLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverTempLoWarn.setStatus("current")
_Hh3cTransceiverVccHiAlarm_Type = Integer32
_Hh3cTransceiverVccHiAlarm_Object = MibTableColumn
hh3cTransceiverVccHiAlarm = _Hh3cTransceiverVccHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 22),
    _Hh3cTransceiverVccHiAlarm_Type()
)
hh3cTransceiverVccHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverVccHiAlarm.setStatus("current")
_Hh3cTransceiverVccLoAlarm_Type = Integer32
_Hh3cTransceiverVccLoAlarm_Object = MibTableColumn
hh3cTransceiverVccLoAlarm = _Hh3cTransceiverVccLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 23),
    _Hh3cTransceiverVccLoAlarm_Type()
)
hh3cTransceiverVccLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverVccLoAlarm.setStatus("current")
_Hh3cTransceiverVccHiWarn_Type = Integer32
_Hh3cTransceiverVccHiWarn_Object = MibTableColumn
hh3cTransceiverVccHiWarn = _Hh3cTransceiverVccHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 24),
    _Hh3cTransceiverVccHiWarn_Type()
)
hh3cTransceiverVccHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverVccHiWarn.setStatus("current")
_Hh3cTransceiverVccLoWarn_Type = Integer32
_Hh3cTransceiverVccLoWarn_Object = MibTableColumn
hh3cTransceiverVccLoWarn = _Hh3cTransceiverVccLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 25),
    _Hh3cTransceiverVccLoWarn_Type()
)
hh3cTransceiverVccLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverVccLoWarn.setStatus("current")
_Hh3cTransceiverBiasHiAlarm_Type = Integer32
_Hh3cTransceiverBiasHiAlarm_Object = MibTableColumn
hh3cTransceiverBiasHiAlarm = _Hh3cTransceiverBiasHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 26),
    _Hh3cTransceiverBiasHiAlarm_Type()
)
hh3cTransceiverBiasHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverBiasHiAlarm.setStatus("current")
_Hh3cTransceiverBiasLoAlarm_Type = Integer32
_Hh3cTransceiverBiasLoAlarm_Object = MibTableColumn
hh3cTransceiverBiasLoAlarm = _Hh3cTransceiverBiasLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 27),
    _Hh3cTransceiverBiasLoAlarm_Type()
)
hh3cTransceiverBiasLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverBiasLoAlarm.setStatus("current")
_Hh3cTransceiverBiasHiWarn_Type = Integer32
_Hh3cTransceiverBiasHiWarn_Object = MibTableColumn
hh3cTransceiverBiasHiWarn = _Hh3cTransceiverBiasHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 28),
    _Hh3cTransceiverBiasHiWarn_Type()
)
hh3cTransceiverBiasHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverBiasHiWarn.setStatus("current")
_Hh3cTransceiverBiasLoWarn_Type = Integer32
_Hh3cTransceiverBiasLoWarn_Object = MibTableColumn
hh3cTransceiverBiasLoWarn = _Hh3cTransceiverBiasLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 29),
    _Hh3cTransceiverBiasLoWarn_Type()
)
hh3cTransceiverBiasLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverBiasLoWarn.setStatus("current")
_Hh3cTransceiverPwrOutHiAlarm_Type = Integer32
_Hh3cTransceiverPwrOutHiAlarm_Object = MibTableColumn
hh3cTransceiverPwrOutHiAlarm = _Hh3cTransceiverPwrOutHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 30),
    _Hh3cTransceiverPwrOutHiAlarm_Type()
)
hh3cTransceiverPwrOutHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverPwrOutHiAlarm.setStatus("current")
_Hh3cTransceiverPwrOutLoAlarm_Type = Integer32
_Hh3cTransceiverPwrOutLoAlarm_Object = MibTableColumn
hh3cTransceiverPwrOutLoAlarm = _Hh3cTransceiverPwrOutLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 31),
    _Hh3cTransceiverPwrOutLoAlarm_Type()
)
hh3cTransceiverPwrOutLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverPwrOutLoAlarm.setStatus("current")
_Hh3cTransceiverPwrOutHiWarn_Type = Integer32
_Hh3cTransceiverPwrOutHiWarn_Object = MibTableColumn
hh3cTransceiverPwrOutHiWarn = _Hh3cTransceiverPwrOutHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 32),
    _Hh3cTransceiverPwrOutHiWarn_Type()
)
hh3cTransceiverPwrOutHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverPwrOutHiWarn.setStatus("current")
_Hh3cTransceiverPwrOutLoWarn_Type = Integer32
_Hh3cTransceiverPwrOutLoWarn_Object = MibTableColumn
hh3cTransceiverPwrOutLoWarn = _Hh3cTransceiverPwrOutLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 33),
    _Hh3cTransceiverPwrOutLoWarn_Type()
)
hh3cTransceiverPwrOutLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverPwrOutLoWarn.setStatus("current")
_Hh3cTransceiverRcvPwrHiAlarm_Type = Integer32
_Hh3cTransceiverRcvPwrHiAlarm_Object = MibTableColumn
hh3cTransceiverRcvPwrHiAlarm = _Hh3cTransceiverRcvPwrHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 34),
    _Hh3cTransceiverRcvPwrHiAlarm_Type()
)
hh3cTransceiverRcvPwrHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverRcvPwrHiAlarm.setStatus("current")
_Hh3cTransceiverRcvPwrLoAlarm_Type = Integer32
_Hh3cTransceiverRcvPwrLoAlarm_Object = MibTableColumn
hh3cTransceiverRcvPwrLoAlarm = _Hh3cTransceiverRcvPwrLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 35),
    _Hh3cTransceiverRcvPwrLoAlarm_Type()
)
hh3cTransceiverRcvPwrLoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverRcvPwrLoAlarm.setStatus("current")
_Hh3cTransceiverRcvPwrHiWarn_Type = Integer32
_Hh3cTransceiverRcvPwrHiWarn_Object = MibTableColumn
hh3cTransceiverRcvPwrHiWarn = _Hh3cTransceiverRcvPwrHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 36),
    _Hh3cTransceiverRcvPwrHiWarn_Type()
)
hh3cTransceiverRcvPwrHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverRcvPwrHiWarn.setStatus("current")
_Hh3cTransceiverRcvPwrLoWarn_Type = Integer32
_Hh3cTransceiverRcvPwrLoWarn_Object = MibTableColumn
hh3cTransceiverRcvPwrLoWarn = _Hh3cTransceiverRcvPwrLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 37),
    _Hh3cTransceiverRcvPwrLoWarn_Type()
)
hh3cTransceiverRcvPwrLoWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverRcvPwrLoWarn.setStatus("current")


class _Hh3cTransceiverErrors_Type(Bits):
    """Custom type hh3cTransceiverErrors based on Bits"""
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

_Hh3cTransceiverErrors_Type.__name__ = "Bits"
_Hh3cTransceiverErrors_Object = MibTableColumn
hh3cTransceiverErrors = _Hh3cTransceiverErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 38),
    _Hh3cTransceiverErrors_Type()
)
hh3cTransceiverErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverErrors.setStatus("current")


class _Hh3cTransceiverVendorOUI_Type(OctetString):
    """Custom type hh3cTransceiverVendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cTransceiverVendorOUI_Type.__name__ = "OctetString"
_Hh3cTransceiverVendorOUI_Object = MibTableColumn
hh3cTransceiverVendorOUI = _Hh3cTransceiverVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 39),
    _Hh3cTransceiverVendorOUI_Type()
)
hh3cTransceiverVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverVendorOUI.setStatus("current")


class _Hh3cTransceiverRevisionNumber_Type(OctetString):
    """Custom type hh3cTransceiverRevisionNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cTransceiverRevisionNumber_Type.__name__ = "OctetString"
_Hh3cTransceiverRevisionNumber_Object = MibTableColumn
hh3cTransceiverRevisionNumber = _Hh3cTransceiverRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 1, 1, 40),
    _Hh3cTransceiverRevisionNumber_Type()
)
hh3cTransceiverRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverRevisionNumber.setStatus("current")
_Hh3cTransceiverChannelTable_Object = MibTable
hh3cTransceiverChannelTable = _Hh3cTransceiverChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cTransceiverChannelTable.setStatus("current")
_Hh3cTransceiverChannelEntry_Object = MibTableRow
hh3cTransceiverChannelEntry = _Hh3cTransceiverChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 2, 1)
)
hh3cTransceiverChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-TRANSCEIVER-INFO-MIB", "hh3cTransceiverChannelIndex"),
)
if mibBuilder.loadTexts:
    hh3cTransceiverChannelEntry.setStatus("current")


class _Hh3cTransceiverChannelIndex_Type(Integer32):
    """Custom type hh3cTransceiverChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cTransceiverChannelIndex_Type.__name__ = "Integer32"
_Hh3cTransceiverChannelIndex_Object = MibTableColumn
hh3cTransceiverChannelIndex = _Hh3cTransceiverChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 2, 1, 1),
    _Hh3cTransceiverChannelIndex_Type()
)
hh3cTransceiverChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTransceiverChannelIndex.setStatus("current")
_Hh3cTransceiverChannelCurTXPower_Type = Integer32
_Hh3cTransceiverChannelCurTXPower_Object = MibTableColumn
hh3cTransceiverChannelCurTXPower = _Hh3cTransceiverChannelCurTXPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 2, 1, 2),
    _Hh3cTransceiverChannelCurTXPower_Type()
)
hh3cTransceiverChannelCurTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverChannelCurTXPower.setStatus("current")
_Hh3cTransceiverChannelCurRXPower_Type = Integer32
_Hh3cTransceiverChannelCurRXPower_Object = MibTableColumn
hh3cTransceiverChannelCurRXPower = _Hh3cTransceiverChannelCurRXPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 2, 1, 3),
    _Hh3cTransceiverChannelCurRXPower_Type()
)
hh3cTransceiverChannelCurRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverChannelCurRXPower.setStatus("current")
_Hh3cTransceiverChannelTemperature_Type = Integer32
_Hh3cTransceiverChannelTemperature_Object = MibTableColumn
hh3cTransceiverChannelTemperature = _Hh3cTransceiverChannelTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 2, 1, 4),
    _Hh3cTransceiverChannelTemperature_Type()
)
hh3cTransceiverChannelTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverChannelTemperature.setStatus("current")
_Hh3cTransceiverChannelBiasCurrent_Type = Integer32
_Hh3cTransceiverChannelBiasCurrent_Object = MibTableColumn
hh3cTransceiverChannelBiasCurrent = _Hh3cTransceiverChannelBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70, 1, 2, 1, 5),
    _Hh3cTransceiverChannelBiasCurrent_Type()
)
hh3cTransceiverChannelBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTransceiverChannelBiasCurrent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-TRANSCEIVER-INFO-MIB",
    **{"hh3cTransceiver": hh3cTransceiver,
       "hh3cTransceiverInfoAdm": hh3cTransceiverInfoAdm,
       "hh3cTransceiverInfoTable": hh3cTransceiverInfoTable,
       "hh3cTransceiverInfoEntry": hh3cTransceiverInfoEntry,
       "hh3cTransceiverHardwareType": hh3cTransceiverHardwareType,
       "hh3cTransceiverType": hh3cTransceiverType,
       "hh3cTransceiverWaveLength": hh3cTransceiverWaveLength,
       "hh3cTransceiverVendorName": hh3cTransceiverVendorName,
       "hh3cTransceiverSerialNumber": hh3cTransceiverSerialNumber,
       "hh3cTransceiverFiberDiameterType": hh3cTransceiverFiberDiameterType,
       "hh3cTransceiverTransferDistance": hh3cTransceiverTransferDistance,
       "hh3cTransceiverDiagnostic": hh3cTransceiverDiagnostic,
       "hh3cTransceiverCurTXPower": hh3cTransceiverCurTXPower,
       "hh3cTransceiverMaxTXPower": hh3cTransceiverMaxTXPower,
       "hh3cTransceiverMinTXPower": hh3cTransceiverMinTXPower,
       "hh3cTransceiverCurRXPower": hh3cTransceiverCurRXPower,
       "hh3cTransceiverMaxRXPower": hh3cTransceiverMaxRXPower,
       "hh3cTransceiverMinRXPower": hh3cTransceiverMinRXPower,
       "hh3cTransceiverTemperature": hh3cTransceiverTemperature,
       "hh3cTransceiverVoltage": hh3cTransceiverVoltage,
       "hh3cTransceiverBiasCurrent": hh3cTransceiverBiasCurrent,
       "hh3cTransceiverTempHiAlarm": hh3cTransceiverTempHiAlarm,
       "hh3cTransceiverTempLoAlarm": hh3cTransceiverTempLoAlarm,
       "hh3cTransceiverTempHiWarn": hh3cTransceiverTempHiWarn,
       "hh3cTransceiverTempLoWarn": hh3cTransceiverTempLoWarn,
       "hh3cTransceiverVccHiAlarm": hh3cTransceiverVccHiAlarm,
       "hh3cTransceiverVccLoAlarm": hh3cTransceiverVccLoAlarm,
       "hh3cTransceiverVccHiWarn": hh3cTransceiverVccHiWarn,
       "hh3cTransceiverVccLoWarn": hh3cTransceiverVccLoWarn,
       "hh3cTransceiverBiasHiAlarm": hh3cTransceiverBiasHiAlarm,
       "hh3cTransceiverBiasLoAlarm": hh3cTransceiverBiasLoAlarm,
       "hh3cTransceiverBiasHiWarn": hh3cTransceiverBiasHiWarn,
       "hh3cTransceiverBiasLoWarn": hh3cTransceiverBiasLoWarn,
       "hh3cTransceiverPwrOutHiAlarm": hh3cTransceiverPwrOutHiAlarm,
       "hh3cTransceiverPwrOutLoAlarm": hh3cTransceiverPwrOutLoAlarm,
       "hh3cTransceiverPwrOutHiWarn": hh3cTransceiverPwrOutHiWarn,
       "hh3cTransceiverPwrOutLoWarn": hh3cTransceiverPwrOutLoWarn,
       "hh3cTransceiverRcvPwrHiAlarm": hh3cTransceiverRcvPwrHiAlarm,
       "hh3cTransceiverRcvPwrLoAlarm": hh3cTransceiverRcvPwrLoAlarm,
       "hh3cTransceiverRcvPwrHiWarn": hh3cTransceiverRcvPwrHiWarn,
       "hh3cTransceiverRcvPwrLoWarn": hh3cTransceiverRcvPwrLoWarn,
       "hh3cTransceiverErrors": hh3cTransceiverErrors,
       "hh3cTransceiverVendorOUI": hh3cTransceiverVendorOUI,
       "hh3cTransceiverRevisionNumber": hh3cTransceiverRevisionNumber,
       "hh3cTransceiverChannelTable": hh3cTransceiverChannelTable,
       "hh3cTransceiverChannelEntry": hh3cTransceiverChannelEntry,
       "hh3cTransceiverChannelIndex": hh3cTransceiverChannelIndex,
       "hh3cTransceiverChannelCurTXPower": hh3cTransceiverChannelCurTXPower,
       "hh3cTransceiverChannelCurRXPower": hh3cTransceiverChannelCurRXPower,
       "hh3cTransceiverChannelTemperature": hh3cTransceiverChannelTemperature,
       "hh3cTransceiverChannelBiasCurrent": hh3cTransceiverChannelBiasCurrent}
)
