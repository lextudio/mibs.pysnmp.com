# SNMP MIB module (HUAWEI-VO-ANALOG-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VO-ANALOG-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:27 2024
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

(voice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "voice")

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

hwVoiceAnalogInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3)
)
hwVoiceAnalogInterfaceMIB.setRevisions(
        ("2004-04-08 13:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVoAnalogIfCommonObjects_ObjectIdentity = ObjectIdentity
hwVoAnalogIfCommonObjects = _HwVoAnalogIfCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1)
)
_HwVoAnalogIfCommonConfigTable_Object = MibTable
hwVoAnalogIfCommonConfigTable = _HwVoAnalogIfCommonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwVoAnalogIfCommonConfigTable.setStatus("current")
_HwVoAnalogIfCommonConfigEntry_Object = MibTableRow
hwVoAnalogIfCommonConfigEntry = _HwVoAnalogIfCommonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1)
)
hwVoAnalogIfCommonConfigEntry.setIndexNames(
    (0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfConfigPortNumber"),
)
if mibBuilder.loadTexts:
    hwVoAnalogIfCommonConfigEntry.setStatus("current")
_HwVoAnalogIfConfigPortNumber_Type = Integer32
_HwVoAnalogIfConfigPortNumber_Object = MibTableColumn
hwVoAnalogIfConfigPortNumber = _HwVoAnalogIfConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1, 1),
    _HwVoAnalogIfConfigPortNumber_Type()
)
hwVoAnalogIfConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfConfigPortNumber.setStatus("current")


class _HwVoAnalogIfConfigPortType_Type(Integer32):
    """Custom type hwVoAnalogIfConfigPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("em", 3),
          ("fxo", 2),
          ("fxs", 1))
    )


_HwVoAnalogIfConfigPortType_Type.__name__ = "Integer32"
_HwVoAnalogIfConfigPortType_Object = MibTableColumn
hwVoAnalogIfConfigPortType = _HwVoAnalogIfConfigPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1, 2),
    _HwVoAnalogIfConfigPortType_Type()
)
hwVoAnalogIfConfigPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfConfigPortType.setStatus("current")


class _HwVoAnaloglfConfigPortImpedance_Type(Integer32):
    """Custom type hwVoAnaloglfConfigPortImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("impedance600Real", 1),
          ("impedanceComplex", 2))
    )


_HwVoAnaloglfConfigPortImpedance_Type.__name__ = "Integer32"
_HwVoAnaloglfConfigPortImpedance_Object = MibTableColumn
hwVoAnaloglfConfigPortImpedance = _HwVoAnaloglfConfigPortImpedance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1, 3),
    _HwVoAnaloglfConfigPortImpedance_Type()
)
hwVoAnaloglfConfigPortImpedance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnaloglfConfigPortImpedance.setStatus("current")


class _HwVoAnalogIfConfigInitialDigitTimeOut_Type(Integer32):
    """Custom type hwVoAnalogIfConfigInitialDigitTimeOut based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_HwVoAnalogIfConfigInitialDigitTimeOut_Type.__name__ = "Integer32"
_HwVoAnalogIfConfigInitialDigitTimeOut_Object = MibTableColumn
hwVoAnalogIfConfigInitialDigitTimeOut = _HwVoAnalogIfConfigInitialDigitTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1, 4),
    _HwVoAnalogIfConfigInitialDigitTimeOut_Type()
)
hwVoAnalogIfConfigInitialDigitTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfConfigInitialDigitTimeOut.setStatus("current")


class _HwVoAnalogIfConfigInterDigitTimeOut_Type(Integer32):
    """Custom type hwVoAnalogIfConfigInterDigitTimeOut based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_HwVoAnalogIfConfigInterDigitTimeOut_Type.__name__ = "Integer32"
_HwVoAnalogIfConfigInterDigitTimeOut_Object = MibTableColumn
hwVoAnalogIfConfigInterDigitTimeOut = _HwVoAnalogIfConfigInterDigitTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1, 5),
    _HwVoAnalogIfConfigInterDigitTimeOut_Type()
)
hwVoAnalogIfConfigInterDigitTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfConfigInterDigitTimeOut.setStatus("current")


class _HwVoAnalogIfConfigCallDisconnect_Type(Integer32):
    """Custom type hwVoAnalogIfConfigCallDisconnect based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HwVoAnalogIfConfigCallDisconnect_Type.__name__ = "Integer32"
_HwVoAnalogIfConfigCallDisconnect_Object = MibTableColumn
hwVoAnalogIfConfigCallDisconnect = _HwVoAnalogIfConfigCallDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1, 6),
    _HwVoAnalogIfConfigCallDisconnect_Type()
)
hwVoAnalogIfConfigCallDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfConfigCallDisconnect.setStatus("current")
_HwVoAnalogIfFXSObjects_ObjectIdentity = ObjectIdentity
hwVoAnalogIfFXSObjects = _HwVoAnalogIfFXSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2)
)
_HwVoAnalogIfFXSConfigTable_Object = MibTable
hwVoAnalogIfFXSConfigTable = _HwVoAnalogIfFXSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwVoAnalogIfFXSConfigTable.setStatus("current")
_HwVoAnalogIfFXSConfigEntry_Object = MibTableRow
hwVoAnalogIfFXSConfigEntry = _HwVoAnalogIfFXSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 1, 1)
)
hwVoAnalogIfFXSConfigEntry.setIndexNames(
    (0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfFXSConfigPortNumber"),
)
if mibBuilder.loadTexts:
    hwVoAnalogIfFXSConfigEntry.setStatus("current")
_HwVoAnalogIfFXSConfigPortNumber_Type = Integer32
_HwVoAnalogIfFXSConfigPortNumber_Object = MibTableColumn
hwVoAnalogIfFXSConfigPortNumber = _HwVoAnalogIfFXSConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 1, 1, 1),
    _HwVoAnalogIfFXSConfigPortNumber_Type()
)
hwVoAnalogIfFXSConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXSConfigPortNumber.setStatus("current")


class _HwVoAnalogIfFXSConfigStartMode_Type(Integer32):
    """Custom type hwVoAnalogIfFXSConfigStartMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("groundStart", 2),
          ("loopStart", 1))
    )


_HwVoAnalogIfFXSConfigStartMode_Type.__name__ = "Integer32"
_HwVoAnalogIfFXSConfigStartMode_Object = MibTableColumn
hwVoAnalogIfFXSConfigStartMode = _HwVoAnalogIfFXSConfigStartMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 1, 1, 2),
    _HwVoAnalogIfFXSConfigStartMode_Type()
)
hwVoAnalogIfFXSConfigStartMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXSConfigStartMode.setStatus("current")
_HwVoAnalogIfFXSTimerTable_Object = MibTable
hwVoAnalogIfFXSTimerTable = _HwVoAnalogIfFXSTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hwVoAnalogIfFXSTimerTable.setStatus("current")
_HwVoAnalogIfFXSTimerEntry_Object = MibTableRow
hwVoAnalogIfFXSTimerEntry = _HwVoAnalogIfFXSTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 3, 1)
)
hwVoAnalogIfFXSTimerEntry.setIndexNames(
    (0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfFXSTimerPortNumber"),
)
if mibBuilder.loadTexts:
    hwVoAnalogIfFXSTimerEntry.setStatus("current")
_HwVoAnalogIfFXSTimerPortNumber_Type = Integer32
_HwVoAnalogIfFXSTimerPortNumber_Object = MibTableColumn
hwVoAnalogIfFXSTimerPortNumber = _HwVoAnalogIfFXSTimerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 3, 1, 1),
    _HwVoAnalogIfFXSTimerPortNumber_Type()
)
hwVoAnalogIfFXSTimerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXSTimerPortNumber.setStatus("current")


class _HwVoAnalogIfFXSTimerDtmf_Type(Integer32):
    """Custom type hwVoAnalogIfFXSTimerDtmf based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_HwVoAnalogIfFXSTimerDtmf_Type.__name__ = "Integer32"
_HwVoAnalogIfFXSTimerDtmf_Object = MibTableColumn
hwVoAnalogIfFXSTimerDtmf = _HwVoAnalogIfFXSTimerDtmf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 3, 1, 2),
    _HwVoAnalogIfFXSTimerDtmf_Type()
)
hwVoAnalogIfFXSTimerDtmf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXSTimerDtmf.setStatus("current")


class _HwVoAnalogIfFXSTimerDtmfInterval_Type(Integer32):
    """Custom type hwVoAnalogIfFXSTimerDtmfInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_HwVoAnalogIfFXSTimerDtmfInterval_Type.__name__ = "Integer32"
_HwVoAnalogIfFXSTimerDtmfInterval_Object = MibTableColumn
hwVoAnalogIfFXSTimerDtmfInterval = _HwVoAnalogIfFXSTimerDtmfInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 3, 1, 3),
    _HwVoAnalogIfFXSTimerDtmfInterval_Type()
)
hwVoAnalogIfFXSTimerDtmfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXSTimerDtmfInterval.setStatus("current")
_HwVoAnalogIfFXOObjects_ObjectIdentity = ObjectIdentity
hwVoAnalogIfFXOObjects = _HwVoAnalogIfFXOObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3)
)
_HwVoAnalogIfFXOConfigTable_Object = MibTable
hwVoAnalogIfFXOConfigTable = _HwVoAnalogIfFXOConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    hwVoAnalogIfFXOConfigTable.setStatus("current")
_HwVoAnalogIfFXOConfigEntry_Object = MibTableRow
hwVoAnalogIfFXOConfigEntry = _HwVoAnalogIfFXOConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1)
)
hwVoAnalogIfFXOConfigEntry.setIndexNames(
    (0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfFXOConfigPortNumber"),
)
if mibBuilder.loadTexts:
    hwVoAnalogIfFXOConfigEntry.setStatus("current")
_HwVoAnalogIfFXOConfigPortNumber_Type = Integer32
_HwVoAnalogIfFXOConfigPortNumber_Object = MibTableColumn
hwVoAnalogIfFXOConfigPortNumber = _HwVoAnalogIfFXOConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1, 1),
    _HwVoAnalogIfFXOConfigPortNumber_Type()
)
hwVoAnalogIfFXOConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXOConfigPortNumber.setStatus("current")


class _HwVoAnalogIfFXOConfigStartMode_Type(Integer32):
    """Custom type hwVoAnalogIfFXOConfigStartMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("groundStart", 2),
          ("loopStart", 1))
    )


_HwVoAnalogIfFXOConfigStartMode_Type.__name__ = "Integer32"
_HwVoAnalogIfFXOConfigStartMode_Object = MibTableColumn
hwVoAnalogIfFXOConfigStartMode = _HwVoAnalogIfFXOConfigStartMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1, 2),
    _HwVoAnalogIfFXOConfigStartMode_Type()
)
hwVoAnalogIfFXOConfigStartMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXOConfigStartMode.setStatus("current")


class _HwVoAnalogIfFXOConfigAlertNumber_Type(Integer32):
    """Custom type hwVoAnalogIfFXOConfigAlertNumber based on Integer32"""
    defaultValue = 2


_HwVoAnalogIfFXOConfigAlertNumber_Object = MibTableColumn
hwVoAnalogIfFXOConfigAlertNumber = _HwVoAnalogIfFXOConfigAlertNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1, 3),
    _HwVoAnalogIfFXOConfigAlertNumber_Type()
)
hwVoAnalogIfFXOConfigAlertNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXOConfigAlertNumber.setStatus("current")


class _HwVoAnalogIfFXOConfigArea_Type(Integer32):
    """Custom type hwVoAnalogIfFXOConfigArea based on Integer32"""
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
        *(("custom", 2),
          ("europe", 1),
          ("north-america", 3))
    )


_HwVoAnalogIfFXOConfigArea_Type.__name__ = "Integer32"
_HwVoAnalogIfFXOConfigArea_Object = MibTableColumn
hwVoAnalogIfFXOConfigArea = _HwVoAnalogIfFXOConfigArea_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1, 4),
    _HwVoAnalogIfFXOConfigArea_Type()
)
hwVoAnalogIfFXOConfigArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXOConfigArea.setStatus("current")


class _HwVoAnalogIfFXOPreDialDelay_Type(Integer32):
    """Custom type hwVoAnalogIfFXOPreDialDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HwVoAnalogIfFXOPreDialDelay_Type.__name__ = "Integer32"
_HwVoAnalogIfFXOPreDialDelay_Object = MibTableColumn
hwVoAnalogIfFXOPreDialDelay = _HwVoAnalogIfFXOPreDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1, 5),
    _HwVoAnalogIfFXOPreDialDelay_Type()
)
hwVoAnalogIfFXOPreDialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXOPreDialDelay.setStatus("current")


class _HwVoAnaloglfFXOConfigPortImpedance_Type(Integer32):
    """Custom type hwVoAnaloglfFXOConfigPortImpedance based on Integer32"""
    defaultValue = 2

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
        *(("impedance550r", 0),
          ("impedance600c", 2),
          ("impedance600r", 1),
          ("impedancecomplex", 3))
    )


_HwVoAnaloglfFXOConfigPortImpedance_Type.__name__ = "Integer32"
_HwVoAnaloglfFXOConfigPortImpedance_Object = MibTableColumn
hwVoAnaloglfFXOConfigPortImpedance = _HwVoAnaloglfFXOConfigPortImpedance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1, 6),
    _HwVoAnaloglfFXOConfigPortImpedance_Type()
)
hwVoAnaloglfFXOConfigPortImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnaloglfFXOConfigPortImpedance.setStatus("current")
_HwVoAnalogIfFXOTimerTable_Object = MibTable
hwVoAnalogIfFXOTimerTable = _HwVoAnalogIfFXOTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    hwVoAnalogIfFXOTimerTable.setStatus("current")
_HwVoAnalogIfFXOTimerEntry_Object = MibTableRow
hwVoAnalogIfFXOTimerEntry = _HwVoAnalogIfFXOTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 3, 1)
)
hwVoAnalogIfFXOTimerEntry.setIndexNames(
    (0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfFXOTimerPortNumber"),
)
if mibBuilder.loadTexts:
    hwVoAnalogIfFXOTimerEntry.setStatus("current")
_HwVoAnalogIfFXOTimerPortNumber_Type = Integer32
_HwVoAnalogIfFXOTimerPortNumber_Object = MibTableColumn
hwVoAnalogIfFXOTimerPortNumber = _HwVoAnalogIfFXOTimerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 3, 1, 1),
    _HwVoAnalogIfFXOTimerPortNumber_Type()
)
hwVoAnalogIfFXOTimerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXOTimerPortNumber.setStatus("current")


class _HwVoAnalogIfFXOTimerDtmf_Type(Integer32):
    """Custom type hwVoAnalogIfFXOTimerDtmf based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_HwVoAnalogIfFXOTimerDtmf_Type.__name__ = "Integer32"
_HwVoAnalogIfFXOTimerDtmf_Object = MibTableColumn
hwVoAnalogIfFXOTimerDtmf = _HwVoAnalogIfFXOTimerDtmf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 3, 1, 2),
    _HwVoAnalogIfFXOTimerDtmf_Type()
)
hwVoAnalogIfFXOTimerDtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXOTimerDtmf.setStatus("current")


class _HwVoAnalogIfFXOTimerDtmfInterval_Type(Integer32):
    """Custom type hwVoAnalogIfFXOTimerDtmfInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_HwVoAnalogIfFXOTimerDtmfInterval_Type.__name__ = "Integer32"
_HwVoAnalogIfFXOTimerDtmfInterval_Object = MibTableColumn
hwVoAnalogIfFXOTimerDtmfInterval = _HwVoAnalogIfFXOTimerDtmfInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 3, 1, 3),
    _HwVoAnalogIfFXOTimerDtmfInterval_Type()
)
hwVoAnalogIfFXOTimerDtmfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfFXOTimerDtmfInterval.setStatus("current")
_HwVoAnalogIfEMObjects_ObjectIdentity = ObjectIdentity
hwVoAnalogIfEMObjects = _HwVoAnalogIfEMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4)
)
_HwVoAnalogIfEMConfigTable_Object = MibTable
hwVoAnalogIfEMConfigTable = _HwVoAnalogIfEMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    hwVoAnalogIfEMConfigTable.setStatus("current")
_HwVoAnalogIfEMConfigEntry_Object = MibTableRow
hwVoAnalogIfEMConfigEntry = _HwVoAnalogIfEMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1)
)
hwVoAnalogIfEMConfigEntry.setIndexNames(
    (0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfEMConfigPortNumber"),
)
if mibBuilder.loadTexts:
    hwVoAnalogIfEMConfigEntry.setStatus("current")
_HwVoAnalogIfEMConfigPortNumber_Type = Integer32
_HwVoAnalogIfEMConfigPortNumber_Object = MibTableColumn
hwVoAnalogIfEMConfigPortNumber = _HwVoAnalogIfEMConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1, 1),
    _HwVoAnalogIfEMConfigPortNumber_Type()
)
hwVoAnalogIfEMConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMConfigPortNumber.setStatus("current")


class _HwVoAnalogIfEMConfigSignalMode_Type(Integer32):
    """Custom type hwVoAnalogIfEMConfigSignalMode based on Integer32"""
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
        *(("delayDial", 1),
          ("immediateDial", 2),
          ("winkStart", 3))
    )


_HwVoAnalogIfEMConfigSignalMode_Type.__name__ = "Integer32"
_HwVoAnalogIfEMConfigSignalMode_Object = MibTableColumn
hwVoAnalogIfEMConfigSignalMode = _HwVoAnalogIfEMConfigSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1, 2),
    _HwVoAnalogIfEMConfigSignalMode_Type()
)
hwVoAnalogIfEMConfigSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMConfigSignalMode.setStatus("current")


class _HwVoAnalogIfEMConfigPhyParm_Type(Integer32):
    """Custom type hwVoAnalogIfEMConfigPhyParm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourWiresOperation", 2),
          ("twoWiresOperation", 1))
    )


_HwVoAnalogIfEMConfigPhyParm_Type.__name__ = "Integer32"
_HwVoAnalogIfEMConfigPhyParm_Object = MibTableColumn
hwVoAnalogIfEMConfigPhyParm = _HwVoAnalogIfEMConfigPhyParm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1, 3),
    _HwVoAnalogIfEMConfigPhyParm_Type()
)
hwVoAnalogIfEMConfigPhyParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMConfigPhyParm.setStatus("current")


class _HwVoAnalogIfEMConfigPhyType_Type(Integer32):
    """Custom type hwVoAnalogIfEMConfigPhyType based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2),
          ("type3", 3),
          ("type5", 5))
    )


_HwVoAnalogIfEMConfigPhyType_Type.__name__ = "Integer32"
_HwVoAnalogIfEMConfigPhyType_Object = MibTableColumn
hwVoAnalogIfEMConfigPhyType = _HwVoAnalogIfEMConfigPhyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1, 4),
    _HwVoAnalogIfEMConfigPhyType_Type()
)
hwVoAnalogIfEMConfigPhyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMConfigPhyType.setStatus("current")


class _HwVoAnalogIfEMConfigTimeoutRinging_Type(Integer32):
    """Custom type hwVoAnalogIfEMConfigTimeoutRinging based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
        ValueRangeConstraint(65535, 65535),
    )


_HwVoAnalogIfEMConfigTimeoutRinging_Type.__name__ = "Integer32"
_HwVoAnalogIfEMConfigTimeoutRinging_Object = MibTableColumn
hwVoAnalogIfEMConfigTimeoutRinging = _HwVoAnalogIfEMConfigTimeoutRinging_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1, 5),
    _HwVoAnalogIfEMConfigTimeoutRinging_Type()
)
hwVoAnalogIfEMConfigTimeoutRinging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMConfigTimeoutRinging.setStatus("current")


class _HwVoAnalogIfEMConfigTimeoutWaitDigit_Type(Integer32):
    """Custom type hwVoAnalogIfEMConfigTimeoutWaitDigit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 600),
        ValueRangeConstraint(65535, 65535),
    )


_HwVoAnalogIfEMConfigTimeoutWaitDigit_Type.__name__ = "Integer32"
_HwVoAnalogIfEMConfigTimeoutWaitDigit_Object = MibTableColumn
hwVoAnalogIfEMConfigTimeoutWaitDigit = _HwVoAnalogIfEMConfigTimeoutWaitDigit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1, 6),
    _HwVoAnalogIfEMConfigTimeoutWaitDigit_Type()
)
hwVoAnalogIfEMConfigTimeoutWaitDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMConfigTimeoutWaitDigit.setStatus("current")
_HwVoAnalogIfEMTimerTable_Object = MibTable
hwVoAnalogIfEMTimerTable = _HwVoAnalogIfEMTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    hwVoAnalogIfEMTimerTable.setStatus("current")
_HwVoAnalogIfEMTimerEntry_Object = MibTableRow
hwVoAnalogIfEMTimerEntry = _HwVoAnalogIfEMTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1)
)
hwVoAnalogIfEMTimerEntry.setIndexNames(
    (0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfEMTimerPortNumber"),
)
if mibBuilder.loadTexts:
    hwVoAnalogIfEMTimerEntry.setStatus("current")
_HwVoAnalogIfEMTimerPortNumber_Type = Integer32
_HwVoAnalogIfEMTimerPortNumber_Object = MibTableColumn
hwVoAnalogIfEMTimerPortNumber = _HwVoAnalogIfEMTimerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 1),
    _HwVoAnalogIfEMTimerPortNumber_Type()
)
hwVoAnalogIfEMTimerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMTimerPortNumber.setStatus("current")


class _HwVoAnalogIfEMTimerDtmf_Type(Integer32):
    """Custom type hwVoAnalogIfEMTimerDtmf based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_HwVoAnalogIfEMTimerDtmf_Type.__name__ = "Integer32"
_HwVoAnalogIfEMTimerDtmf_Object = MibTableColumn
hwVoAnalogIfEMTimerDtmf = _HwVoAnalogIfEMTimerDtmf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 2),
    _HwVoAnalogIfEMTimerDtmf_Type()
)
hwVoAnalogIfEMTimerDtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMTimerDtmf.setStatus("current")


class _HwVoAnalogIfEMTimerDtmfInterval_Type(Integer32):
    """Custom type hwVoAnalogIfEMTimerDtmfInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_HwVoAnalogIfEMTimerDtmfInterval_Type.__name__ = "Integer32"
_HwVoAnalogIfEMTimerDtmfInterval_Object = MibTableColumn
hwVoAnalogIfEMTimerDtmfInterval = _HwVoAnalogIfEMTimerDtmfInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 3),
    _HwVoAnalogIfEMTimerDtmfInterval_Type()
)
hwVoAnalogIfEMTimerDtmfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMTimerDtmfInterval.setStatus("current")


class _HwVoAnalogIfEMTimerCallInterval_Type(Integer32):
    """Custom type hwVoAnalogIfEMTimerCallInterval based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 2000),
    )


_HwVoAnalogIfEMTimerCallInterval_Type.__name__ = "Integer32"
_HwVoAnalogIfEMTimerCallInterval_Object = MibTableColumn
hwVoAnalogIfEMTimerCallInterval = _HwVoAnalogIfEMTimerCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 4),
    _HwVoAnalogIfEMTimerCallInterval_Type()
)
hwVoAnalogIfEMTimerCallInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMTimerCallInterval.setStatus("current")


class _HwVoAnalogIfEMTimerSendWink_Type(Integer32):
    """Custom type hwVoAnalogIfEMTimerSendWink based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_HwVoAnalogIfEMTimerSendWink_Type.__name__ = "Integer32"
_HwVoAnalogIfEMTimerSendWink_Object = MibTableColumn
hwVoAnalogIfEMTimerSendWink = _HwVoAnalogIfEMTimerSendWink_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 5),
    _HwVoAnalogIfEMTimerSendWink_Type()
)
hwVoAnalogIfEMTimerSendWink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMTimerSendWink.setStatus("current")


class _HwVoAnalogIfEMTimerWinkRising_Type(Integer32):
    """Custom type hwVoAnalogIfEMTimerWinkRising based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_HwVoAnalogIfEMTimerWinkRising_Type.__name__ = "Integer32"
_HwVoAnalogIfEMTimerWinkRising_Object = MibTableColumn
hwVoAnalogIfEMTimerWinkRising = _HwVoAnalogIfEMTimerWinkRising_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 6),
    _HwVoAnalogIfEMTimerWinkRising_Type()
)
hwVoAnalogIfEMTimerWinkRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMTimerWinkRising.setStatus("current")


class _HwVoAnalogIfEMTimerWinkHold_Type(Integer32):
    """Custom type hwVoAnalogIfEMTimerWinkHold based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3000),
    )


_HwVoAnalogIfEMTimerWinkHold_Type.__name__ = "Integer32"
_HwVoAnalogIfEMTimerWinkHold_Object = MibTableColumn
hwVoAnalogIfEMTimerWinkHold = _HwVoAnalogIfEMTimerWinkHold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 7),
    _HwVoAnalogIfEMTimerWinkHold_Type()
)
hwVoAnalogIfEMTimerWinkHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMTimerWinkHold.setStatus("current")


class _HwVoAnalogIfEMTimerDialoutDelay_Type(Integer32):
    """Custom type hwVoAnalogIfEMTimerDialoutDelay based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 5000),
    )


_HwVoAnalogIfEMTimerDialoutDelay_Type.__name__ = "Integer32"
_HwVoAnalogIfEMTimerDialoutDelay_Object = MibTableColumn
hwVoAnalogIfEMTimerDialoutDelay = _HwVoAnalogIfEMTimerDialoutDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 8),
    _HwVoAnalogIfEMTimerDialoutDelay_Type()
)
hwVoAnalogIfEMTimerDialoutDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMTimerDialoutDelay.setStatus("current")


class _HwVoAnalogIfEMTimerRising_Type(Integer32):
    """Custom type hwVoAnalogIfEMTimerRising based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_HwVoAnalogIfEMTimerRising_Type.__name__ = "Integer32"
_HwVoAnalogIfEMTimerRising_Object = MibTableColumn
hwVoAnalogIfEMTimerRising = _HwVoAnalogIfEMTimerRising_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 9),
    _HwVoAnalogIfEMTimerRising_Type()
)
hwVoAnalogIfEMTimerRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMTimerRising.setStatus("current")


class _HwVoAnalogIfEMTimerHold_Type(Integer32):
    """Custom type hwVoAnalogIfEMTimerHold based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_HwVoAnalogIfEMTimerHold_Type.__name__ = "Integer32"
_HwVoAnalogIfEMTimerHold_Object = MibTableColumn
hwVoAnalogIfEMTimerHold = _HwVoAnalogIfEMTimerHold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 10),
    _HwVoAnalogIfEMTimerHold_Type()
)
hwVoAnalogIfEMTimerHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoAnalogIfEMTimerHold.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VO-ANALOG-IF-MIB",
    **{"hwVoiceAnalogInterfaceMIB": hwVoiceAnalogInterfaceMIB,
       "hwVoAnalogIfCommonObjects": hwVoAnalogIfCommonObjects,
       "hwVoAnalogIfCommonConfigTable": hwVoAnalogIfCommonConfigTable,
       "hwVoAnalogIfCommonConfigEntry": hwVoAnalogIfCommonConfigEntry,
       "hwVoAnalogIfConfigPortNumber": hwVoAnalogIfConfigPortNumber,
       "hwVoAnalogIfConfigPortType": hwVoAnalogIfConfigPortType,
       "hwVoAnaloglfConfigPortImpedance": hwVoAnaloglfConfigPortImpedance,
       "hwVoAnalogIfConfigInitialDigitTimeOut": hwVoAnalogIfConfigInitialDigitTimeOut,
       "hwVoAnalogIfConfigInterDigitTimeOut": hwVoAnalogIfConfigInterDigitTimeOut,
       "hwVoAnalogIfConfigCallDisconnect": hwVoAnalogIfConfigCallDisconnect,
       "hwVoAnalogIfFXSObjects": hwVoAnalogIfFXSObjects,
       "hwVoAnalogIfFXSConfigTable": hwVoAnalogIfFXSConfigTable,
       "hwVoAnalogIfFXSConfigEntry": hwVoAnalogIfFXSConfigEntry,
       "hwVoAnalogIfFXSConfigPortNumber": hwVoAnalogIfFXSConfigPortNumber,
       "hwVoAnalogIfFXSConfigStartMode": hwVoAnalogIfFXSConfigStartMode,
       "hwVoAnalogIfFXSTimerTable": hwVoAnalogIfFXSTimerTable,
       "hwVoAnalogIfFXSTimerEntry": hwVoAnalogIfFXSTimerEntry,
       "hwVoAnalogIfFXSTimerPortNumber": hwVoAnalogIfFXSTimerPortNumber,
       "hwVoAnalogIfFXSTimerDtmf": hwVoAnalogIfFXSTimerDtmf,
       "hwVoAnalogIfFXSTimerDtmfInterval": hwVoAnalogIfFXSTimerDtmfInterval,
       "hwVoAnalogIfFXOObjects": hwVoAnalogIfFXOObjects,
       "hwVoAnalogIfFXOConfigTable": hwVoAnalogIfFXOConfigTable,
       "hwVoAnalogIfFXOConfigEntry": hwVoAnalogIfFXOConfigEntry,
       "hwVoAnalogIfFXOConfigPortNumber": hwVoAnalogIfFXOConfigPortNumber,
       "hwVoAnalogIfFXOConfigStartMode": hwVoAnalogIfFXOConfigStartMode,
       "hwVoAnalogIfFXOConfigAlertNumber": hwVoAnalogIfFXOConfigAlertNumber,
       "hwVoAnalogIfFXOConfigArea": hwVoAnalogIfFXOConfigArea,
       "hwVoAnalogIfFXOPreDialDelay": hwVoAnalogIfFXOPreDialDelay,
       "hwVoAnaloglfFXOConfigPortImpedance": hwVoAnaloglfFXOConfigPortImpedance,
       "hwVoAnalogIfFXOTimerTable": hwVoAnalogIfFXOTimerTable,
       "hwVoAnalogIfFXOTimerEntry": hwVoAnalogIfFXOTimerEntry,
       "hwVoAnalogIfFXOTimerPortNumber": hwVoAnalogIfFXOTimerPortNumber,
       "hwVoAnalogIfFXOTimerDtmf": hwVoAnalogIfFXOTimerDtmf,
       "hwVoAnalogIfFXOTimerDtmfInterval": hwVoAnalogIfFXOTimerDtmfInterval,
       "hwVoAnalogIfEMObjects": hwVoAnalogIfEMObjects,
       "hwVoAnalogIfEMConfigTable": hwVoAnalogIfEMConfigTable,
       "hwVoAnalogIfEMConfigEntry": hwVoAnalogIfEMConfigEntry,
       "hwVoAnalogIfEMConfigPortNumber": hwVoAnalogIfEMConfigPortNumber,
       "hwVoAnalogIfEMConfigSignalMode": hwVoAnalogIfEMConfigSignalMode,
       "hwVoAnalogIfEMConfigPhyParm": hwVoAnalogIfEMConfigPhyParm,
       "hwVoAnalogIfEMConfigPhyType": hwVoAnalogIfEMConfigPhyType,
       "hwVoAnalogIfEMConfigTimeoutRinging": hwVoAnalogIfEMConfigTimeoutRinging,
       "hwVoAnalogIfEMConfigTimeoutWaitDigit": hwVoAnalogIfEMConfigTimeoutWaitDigit,
       "hwVoAnalogIfEMTimerTable": hwVoAnalogIfEMTimerTable,
       "hwVoAnalogIfEMTimerEntry": hwVoAnalogIfEMTimerEntry,
       "hwVoAnalogIfEMTimerPortNumber": hwVoAnalogIfEMTimerPortNumber,
       "hwVoAnalogIfEMTimerDtmf": hwVoAnalogIfEMTimerDtmf,
       "hwVoAnalogIfEMTimerDtmfInterval": hwVoAnalogIfEMTimerDtmfInterval,
       "hwVoAnalogIfEMTimerCallInterval": hwVoAnalogIfEMTimerCallInterval,
       "hwVoAnalogIfEMTimerSendWink": hwVoAnalogIfEMTimerSendWink,
       "hwVoAnalogIfEMTimerWinkRising": hwVoAnalogIfEMTimerWinkRising,
       "hwVoAnalogIfEMTimerWinkHold": hwVoAnalogIfEMTimerWinkHold,
       "hwVoAnalogIfEMTimerDialoutDelay": hwVoAnalogIfEMTimerDialoutDelay,
       "hwVoAnalogIfEMTimerRising": hwVoAnalogIfEMTimerRising,
       "hwVoAnalogIfEMTimerHold": hwVoAnalogIfEMTimerHold}
)
