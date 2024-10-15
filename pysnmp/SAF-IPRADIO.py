# SNMP MIB module (SAF-IPRADIO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAF-IPRADIO
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:19 2024
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

(ifEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry")

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
 enterprises,
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
    "enterprises",
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

_Saf_ObjectIdentity = ObjectIdentity
saf = _Saf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571)
)
_Tehnika_ObjectIdentity = ObjectIdentity
tehnika = _Tehnika_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100)
)
_MicrowaveRadio_ObjectIdentity = ObjectIdentity
microwaveRadio = _MicrowaveRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1)
)
_PointToPoint_ObjectIdentity = ObjectIdentity
pointToPoint = _PointToPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1)
)
_Safip_ObjectIdentity = ObjectIdentity
safip = _Safip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5)
)
_IpRadio_ObjectIdentity = ObjectIdentity
ipRadio = _IpRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1)
)
_IpRadioCfg_ObjectIdentity = ObjectIdentity
ipRadioCfg = _IpRadioCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1)
)
_IpRadioCfgGeneral_ObjectIdentity = ObjectIdentity
ipRadioCfgGeneral = _IpRadioCfgGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1)
)


class _Product_Type(DisplayString):
    """Custom type product based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Product_Type.__name__ = "DisplayString"
_Product_Object = MibScalar
product = _Product_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 1),
    _Product_Type()
)
product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product.setStatus("mandatory")


class _Description_Type(DisplayString):
    """Custom type description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Description_Type.__name__ = "DisplayString"
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 2),
    _Description_Type()
)
description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    description.setStatus("mandatory")


class _RadioName_Type(DisplayString):
    """Custom type radioName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RadioName_Type.__name__ = "DisplayString"
_RadioName_Object = MibScalar
radioName = _RadioName_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 3),
    _RadioName_Type()
)
radioName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioName.setStatus("mandatory")
_SysDateAndTime_Type = DateAndTime
_SysDateAndTime_Object = MibScalar
sysDateAndTime = _SysDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 4),
    _SysDateAndTime_Type()
)
sysDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateAndTime.setStatus("mandatory")
_SysTemperature_Type = Integer32
_SysTemperature_Object = MibScalar
sysTemperature = _SysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 5),
    _SysTemperature_Type()
)
sysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTemperature.setStatus("mandatory")


class _License_Type(DisplayString):
    """Custom type license based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_License_Type.__name__ = "DisplayString"
_License_Object = MibScalar
license = _License_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 6),
    _License_Type()
)
license.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    license.setStatus("mandatory")
_LicenseMask_Type = Integer32
_LicenseMask_Object = MibScalar
licenseMask = _LicenseMask_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 7),
    _LicenseMask_Type()
)
licenseMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseMask.setStatus("mandatory")
_RadioTable_Object = MibTable
radioTable = _RadioTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    radioTable.setStatus("mandatory")
_RadioEntry_Object = MibTableRow
radioEntry = _RadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 10, 1)
)
radioEntry.setIndexNames(
    (0, "SAF-IPRADIO", "radioIndex"),
)
if mibBuilder.loadTexts:
    radioEntry.setStatus("mandatory")


class _RadioIndex_Type(Integer32):
    """Custom type radioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_RadioIndex_Type.__name__ = "Integer32"
_RadioIndex_Object = MibTableColumn
radioIndex = _RadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 10, 1, 1),
    _RadioIndex_Type()
)
radioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioIndex.setStatus("mandatory")
_RadioGenStatus_Type = Integer32
_RadioGenStatus_Object = MibTableColumn
radioGenStatus = _RadioGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 10, 1, 2),
    _RadioGenStatus_Type()
)
radioGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioGenStatus.setStatus("mandatory")


class _RadioSide_Type(Integer32):
    """Custom type radioSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_RadioSide_Type.__name__ = "Integer32"
_RadioSide_Object = MibTableColumn
radioSide = _RadioSide_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 10, 1, 3),
    _RadioSide_Type()
)
radioSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioSide.setStatus("mandatory")
_RadioTxPower_Type = Integer32
_RadioTxPower_Object = MibTableColumn
radioTxPower = _RadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 10, 1, 4),
    _RadioTxPower_Type()
)
radioTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioTxPower.setStatus("mandatory")
_RadioRxLevel_Type = Integer32
_RadioRxLevel_Object = MibTableColumn
radioRxLevel = _RadioRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 10, 1, 5),
    _RadioRxLevel_Type()
)
radioRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRxLevel.setStatus("mandatory")
_RadioDuplexShift_Type = Integer32
_RadioDuplexShift_Object = MibTableColumn
radioDuplexShift = _RadioDuplexShift_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 10, 1, 6),
    _RadioDuplexShift_Type()
)
radioDuplexShift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioDuplexShift.setStatus("mandatory")


class _RadioLoopback_Type(Integer32):
    """Custom type radioLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_RadioLoopback_Type.__name__ = "Integer32"
_RadioLoopback_Object = MibTableColumn
radioLoopback = _RadioLoopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 10, 1, 7),
    _RadioLoopback_Type()
)
radioLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLoopback.setStatus("mandatory")


class _RadioTxMute_Type(Integer32):
    """Custom type radioTxMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_RadioTxMute_Type.__name__ = "Integer32"
_RadioTxMute_Object = MibTableColumn
radioTxMute = _RadioTxMute_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 10, 1, 8),
    _RadioTxMute_Type()
)
radioTxMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioTxMute.setStatus("mandatory")
_RadioTxFrequency_Type = Integer32
_RadioTxFrequency_Object = MibTableColumn
radioTxFrequency = _RadioTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 10, 1, 9),
    _RadioTxFrequency_Type()
)
radioTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioTxFrequency.setStatus("mandatory")
_RadioRxFrequency_Type = Integer32
_RadioRxFrequency_Object = MibTableColumn
radioRxFrequency = _RadioRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 10, 1, 10),
    _RadioRxFrequency_Type()
)
radioRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRxFrequency.setStatus("mandatory")
_ATPCTable_Object = MibTable
aTPCTable = _ATPCTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    aTPCTable.setStatus("mandatory")
_ATPCEntry_Object = MibTableRow
aTPCEntry = _ATPCEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 11, 1)
)
aTPCEntry.setIndexNames(
    (0, "SAF-IPRADIO", "atpcIndex"),
)
if mibBuilder.loadTexts:
    aTPCEntry.setStatus("mandatory")


class _AtpcIndex_Type(Integer32):
    """Custom type atpcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_AtpcIndex_Type.__name__ = "Integer32"
_AtpcIndex_Object = MibTableColumn
atpcIndex = _AtpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 11, 1, 1),
    _AtpcIndex_Type()
)
atpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atpcIndex.setStatus("mandatory")


class _AtpcEnabled_Type(Integer32):
    """Custom type atpcEnabled based on Integer32"""
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


_AtpcEnabled_Type.__name__ = "Integer32"
_AtpcEnabled_Object = MibTableColumn
atpcEnabled = _AtpcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 11, 1, 2),
    _AtpcEnabled_Type()
)
atpcEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atpcEnabled.setStatus("mandatory")
_AtpcTxPowerCorrection_Type = Integer32
_AtpcTxPowerCorrection_Object = MibTableColumn
atpcTxPowerCorrection = _AtpcTxPowerCorrection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 11, 1, 3),
    _AtpcTxPowerCorrection_Type()
)
atpcTxPowerCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atpcTxPowerCorrection.setStatus("mandatory")
_ModemTable_Object = MibTable
modemTable = _ModemTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    modemTable.setStatus("mandatory")
_ModemEntry_Object = MibTableRow
modemEntry = _ModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1)
)
modemEntry.setIndexNames(
    (0, "SAF-IPRADIO", "modemIndex"),
)
if mibBuilder.loadTexts:
    modemEntry.setStatus("mandatory")


class _ModemIndex_Type(Integer32):
    """Custom type modemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_ModemIndex_Type.__name__ = "Integer32"
_ModemIndex_Object = MibTableColumn
modemIndex = _ModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 1),
    _ModemIndex_Type()
)
modemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIndex.setStatus("mandatory")
_ModemGeneralStatus_Type = Integer32
_ModemGeneralStatus_Object = MibTableColumn
modemGeneralStatus = _ModemGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 2),
    _ModemGeneralStatus_Type()
)
modemGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemGeneralStatus.setStatus("mandatory")
_ModemBandwith_Type = Integer32
_ModemBandwith_Object = MibTableColumn
modemBandwith = _ModemBandwith_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 3),
    _ModemBandwith_Type()
)
modemBandwith.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemBandwith.setStatus("mandatory")
_ModemE1T1Channels_Type = Integer32
_ModemE1T1Channels_Object = MibTableColumn
modemE1T1Channels = _ModemE1T1Channels_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 4),
    _ModemE1T1Channels_Type()
)
modemE1T1Channels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemE1T1Channels.setStatus("mandatory")


class _ModemModulation_Type(Integer32):
    """Custom type modemModulation based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              33,
              34,
              40,
              41,
              42,
              49,
              50,
              57,
              58)
        )
    )
    namedValues = NamedValues(
        *(("acmpsk8", 18),
          ("acmqam128", 22),
          ("acmqam16", 19),
          ("acmqam256", 23),
          ("acmqam32", 20),
          ("acmqam4", 49),
          ("acmqam64", 21),
          ("acmqam8", 50),
          ("acmqpsk", 17),
          ("acmwpsk8", 26),
          ("acmwqam128", 30),
          ("acmwqam16", 27),
          ("acmwqam256", 31),
          ("acmwqam32", 28),
          ("acmwqam4", 57),
          ("acmwqam64", 29),
          ("acmwqam8", 58),
          ("acmwqpsk", 25),
          ("psk8", 2),
          ("qam128", 6),
          ("qam16", 3),
          ("qam256", 7),
          ("qam32", 4),
          ("qam4", 33),
          ("qam4limited", 40),
          ("qam64", 5),
          ("qam8", 34),
          ("qpsk", 1),
          ("qpsklimited", 8),
          ("wpsk8", 10),
          ("wqam128", 14),
          ("wqam16", 11),
          ("wqam256", 15),
          ("wqam32", 12),
          ("wqam4", 41),
          ("wqam64", 13),
          ("wqam8", 42),
          ("wqpsk", 9))
    )


_ModemModulation_Type.__name__ = "Integer32"
_ModemModulation_Object = MibTableColumn
modemModulation = _ModemModulation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 5),
    _ModemModulation_Type()
)
modemModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemModulation.setStatus("mandatory")
_ModemTotalCapacity_Type = Integer32
_ModemTotalCapacity_Object = MibTableColumn
modemTotalCapacity = _ModemTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 6),
    _ModemTotalCapacity_Type()
)
modemTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemTotalCapacity.setStatus("mandatory")
_ModemEthernetCapacity_Type = Integer32
_ModemEthernetCapacity_Object = MibTableColumn
modemEthernetCapacity = _ModemEthernetCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 7),
    _ModemEthernetCapacity_Type()
)
modemEthernetCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemEthernetCapacity.setStatus("mandatory")
_ModemAcqStatus_Type = Integer32
_ModemAcqStatus_Object = MibTableColumn
modemAcqStatus = _ModemAcqStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 8),
    _ModemAcqStatus_Type()
)
modemAcqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemAcqStatus.setStatus("mandatory")


class _ModemLastAcqError_Type(Integer32):
    """Custom type modemLastAcqError based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("erragc", 2),
          ("errbit", 6),
          ("errblind", 8),
          ("errfatal", 11),
          ("errfreqsweep", 4),
          ("errmse", 5),
          ("errservice", 7),
          ("errstopped", 10),
          ("errtimeout", 9),
          ("errtiming", 3),
          ("success", 1))
    )


_ModemLastAcqError_Type.__name__ = "Integer32"
_ModemLastAcqError_Object = MibTableColumn
modemLastAcqError = _ModemLastAcqError_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 9),
    _ModemLastAcqError_Type()
)
modemLastAcqError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemLastAcqError.setStatus("mandatory")
_ModemRadialMSE_Type = Integer32
_ModemRadialMSE_Object = MibTableColumn
modemRadialMSE = _ModemRadialMSE_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 10),
    _ModemRadialMSE_Type()
)
modemRadialMSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemRadialMSE.setStatus("mandatory")
_ModemInternalAGCgain_Type = Integer32
_ModemInternalAGCgain_Object = MibTableColumn
modemInternalAGCgain = _ModemInternalAGCgain_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 11),
    _ModemInternalAGCgain_Type()
)
modemInternalAGCgain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemInternalAGCgain.setStatus("mandatory")
_ModemCarrierOffset_Type = Integer32
_ModemCarrierOffset_Object = MibTableColumn
modemCarrierOffset = _ModemCarrierOffset_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 12),
    _ModemCarrierOffset_Type()
)
modemCarrierOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCarrierOffset.setStatus("mandatory")
_ModemSymbolRateTx_Type = Integer32
_ModemSymbolRateTx_Object = MibTableColumn
modemSymbolRateTx = _ModemSymbolRateTx_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 13),
    _ModemSymbolRateTx_Type()
)
modemSymbolRateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSymbolRateTx.setStatus("mandatory")
_ModemSymbolRateRx_Type = Integer32
_ModemSymbolRateRx_Object = MibTableColumn
modemSymbolRateRx = _ModemSymbolRateRx_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 14),
    _ModemSymbolRateRx_Type()
)
modemSymbolRateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSymbolRateRx.setStatus("mandatory")


class _ModemLDPCdecoderStress_Type(DisplayString):
    """Custom type modemLDPCdecoderStress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModemLDPCdecoderStress_Type.__name__ = "DisplayString"
_ModemLDPCdecoderStress_Object = MibTableColumn
modemLDPCdecoderStress = _ModemLDPCdecoderStress_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 15),
    _ModemLDPCdecoderStress_Type()
)
modemLDPCdecoderStress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemLDPCdecoderStress.setStatus("mandatory")


class _ModemACMengine_Type(Integer32):
    """Custom type modemACMengine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ModemACMengine_Type.__name__ = "Integer32"
_ModemACMengine_Object = MibTableColumn
modemACMengine = _ModemACMengine_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 16),
    _ModemACMengine_Type()
)
modemACMengine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemACMengine.setStatus("mandatory")


class _ModemACMmodulationMin_Type(Integer32):
    """Custom type modemACMmodulationMin based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              33,
              34,
              40,
              41,
              42,
              49,
              50,
              57,
              58)
        )
    )
    namedValues = NamedValues(
        *(("acmpsk8", 18),
          ("acmqam128", 22),
          ("acmqam16", 19),
          ("acmqam256", 23),
          ("acmqam32", 20),
          ("acmqam4", 49),
          ("acmqam64", 21),
          ("acmqam8", 50),
          ("acmqpsk", 17),
          ("acmwpsk8", 26),
          ("acmwqam128", 30),
          ("acmwqam16", 27),
          ("acmwqam256", 31),
          ("acmwqam32", 28),
          ("acmwqam4", 57),
          ("acmwqam64", 29),
          ("acmwqam8", 58),
          ("acmwqpsk", 25),
          ("psk8", 2),
          ("qam128", 6),
          ("qam16", 3),
          ("qam256", 7),
          ("qam32", 4),
          ("qam4", 33),
          ("qam4limited", 40),
          ("qam64", 5),
          ("qam8", 34),
          ("qpsk", 1),
          ("qpsklimited", 8),
          ("wpsk8", 10),
          ("wqam128", 14),
          ("wqam16", 11),
          ("wqam256", 15),
          ("wqam32", 12),
          ("wqam4", 41),
          ("wqam64", 13),
          ("wqam8", 42),
          ("wqpsk", 9))
    )


_ModemACMmodulationMin_Type.__name__ = "Integer32"
_ModemACMmodulationMin_Object = MibTableColumn
modemACMmodulationMin = _ModemACMmodulationMin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 17),
    _ModemACMmodulationMin_Type()
)
modemACMmodulationMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMmodulationMin.setStatus("mandatory")
_ModemACMtotalCapacity_Type = Integer32
_ModemACMtotalCapacity_Object = MibTableColumn
modemACMtotalCapacity = _ModemACMtotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 18),
    _ModemACMtotalCapacity_Type()
)
modemACMtotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemACMtotalCapacity.setStatus("mandatory")
_ModemACMethernetCapacity_Type = Integer32
_ModemACMethernetCapacity_Object = MibTableColumn
modemACMethernetCapacity = _ModemACMethernetCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 19),
    _ModemACMethernetCapacity_Type()
)
modemACMethernetCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemACMethernetCapacity.setStatus("mandatory")


class _ModemStandard_Type(Integer32):
    """Custom type modemStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 2),
          ("etsi", 1))
    )


_ModemStandard_Type.__name__ = "Integer32"
_ModemStandard_Object = MibTableColumn
modemStandard = _ModemStandard_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 20),
    _ModemStandard_Type()
)
modemStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemStandard.setStatus("mandatory")
_ModemE1T1ChannelMask_Type = Integer32
_ModemE1T1ChannelMask_Object = MibTableColumn
modemE1T1ChannelMask = _ModemE1T1ChannelMask_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 21),
    _ModemE1T1ChannelMask_Type()
)
modemE1T1ChannelMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemE1T1ChannelMask.setStatus("mandatory")


class _ModemACMmodulationMax_Type(Integer32):
    """Custom type modemACMmodulationMax based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              33,
              34,
              40,
              41,
              42,
              49,
              50,
              57,
              58)
        )
    )
    namedValues = NamedValues(
        *(("acmpsk8", 18),
          ("acmqam128", 22),
          ("acmqam16", 19),
          ("acmqam256", 23),
          ("acmqam32", 20),
          ("acmqam4", 49),
          ("acmqam64", 21),
          ("acmqam8", 50),
          ("acmqpsk", 17),
          ("acmwpsk8", 26),
          ("acmwqam128", 30),
          ("acmwqam16", 27),
          ("acmwqam256", 31),
          ("acmwqam32", 28),
          ("acmwqam4", 57),
          ("acmwqam64", 29),
          ("acmwqam8", 58),
          ("acmwqpsk", 25),
          ("psk8", 2),
          ("qam128", 6),
          ("qam16", 3),
          ("qam256", 7),
          ("qam32", 4),
          ("qam4", 33),
          ("qam4limited", 40),
          ("qam64", 5),
          ("qam8", 34),
          ("qpsk", 1),
          ("qpsklimited", 8),
          ("wpsk8", 10),
          ("wqam128", 14),
          ("wqam16", 11),
          ("wqam256", 15),
          ("wqam32", 12),
          ("wqam4", 41),
          ("wqam64", 13),
          ("wqam8", 42),
          ("wqpsk", 9))
    )


_ModemACMmodulationMax_Type.__name__ = "Integer32"
_ModemACMmodulationMax_Object = MibTableColumn
modemACMmodulationMax = _ModemACMmodulationMax_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 22),
    _ModemACMmodulationMax_Type()
)
modemACMmodulationMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMmodulationMax.setStatus("mandatory")


class _ModemRowStatus_Type(Integer32):
    """Custom type modemRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notReady", 3),
          ("undo", 4))
    )


_ModemRowStatus_Type.__name__ = "Integer32"
_ModemRowStatus_Object = MibTableColumn
modemRowStatus = _ModemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 12, 1, 23),
    _ModemRowStatus_Type()
)
modemRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemRowStatus.setStatus("mandatory")


class _VlansEnabled_Type(Integer32):
    """Custom type vlansEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("reset", 3))
    )


_VlansEnabled_Type.__name__ = "Integer32"
_VlansEnabled_Object = MibScalar
vlansEnabled = _VlansEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 13),
    _VlansEnabled_Type()
)
vlansEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlansEnabled.setStatus("mandatory")
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("mandatory")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("mandatory")
_VlanNumber_Type = Integer32
_VlanNumber_Object = MibTableColumn
vlanNumber = _VlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 14, 1, 1),
    _VlanNumber_Type()
)
vlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNumber.setStatus("mandatory")


class _VlanPortType_Type(Integer32):
    """Custom type vlanPortType based on Integer32"""
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
        *(("endpoint", 4),
          ("management", 1),
          ("none", 2),
          ("traffic", 3))
    )


_VlanPortType_Type.__name__ = "Integer32"
_VlanPortType_Object = MibTableColumn
vlanPortType = _VlanPortType_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 14, 1, 2),
    _VlanPortType_Type()
)
vlanPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortType.setStatus("mandatory")
_VlanPortmap_Type = Integer32
_VlanPortmap_Object = MibTableColumn
vlanPortmap = _VlanPortmap_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 14, 1, 3),
    _VlanPortmap_Type()
)
vlanPortmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortmap.setStatus("mandatory")
_VlanFid_Type = Integer32
_VlanFid_Object = MibTableColumn
vlanFid = _VlanFid_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 14, 1, 4),
    _VlanFid_Type()
)
vlanFid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanFid.setStatus("optional")


class _VlanCfgStat_Type(Integer32):
    """Custom type vlanCfgStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("disable", 2),
          ("enable", 1))
    )


_VlanCfgStat_Type.__name__ = "Integer32"
_VlanCfgStat_Object = MibTableColumn
vlanCfgStat = _VlanCfgStat_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 14, 1, 5),
    _VlanCfgStat_Type()
)
vlanCfgStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanCfgStat.setStatus("mandatory")


class _VlanRowStatus_Type(Integer32):
    """Custom type vlanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notReady", 3),
          ("undo", 4))
    )


_VlanRowStatus_Type.__name__ = "Integer32"
_VlanRowStatus_Object = MibTableColumn
vlanRowStatus = _VlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 1, 14, 1, 6),
    _VlanRowStatus_Type()
)
vlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanRowStatus.setStatus("mandatory")
_IpRadioCfgNetwork_ObjectIdentity = ObjectIdentity
ipRadioCfgNetwork = _IpRadioCfgNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 2)
)
_LocalIp_Type = IpAddress
_LocalIp_Object = MibScalar
localIp = _LocalIp_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 2, 1),
    _LocalIp_Type()
)
localIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localIp.setStatus("mandatory")
_LocalIpMask_Type = IpAddress
_LocalIpMask_Object = MibScalar
localIpMask = _LocalIpMask_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 2, 2),
    _LocalIpMask_Type()
)
localIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localIpMask.setStatus("mandatory")
_RemoteIp_Type = IpAddress
_RemoteIp_Object = MibScalar
remoteIp = _RemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 1, 2, 3),
    _RemoteIp_Type()
)
remoteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteIp.setStatus("mandatory")
_IpRadioMgmt_ObjectIdentity = ObjectIdentity
ipRadioMgmt = _IpRadioMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 2)
)
_WriteConfig_Type = Integer32
_WriteConfig_Object = MibScalar
writeConfig = _WriteConfig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 2, 1),
    _WriteConfig_Type()
)
writeConfig.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    writeConfig.setStatus("mandatory")
_Restartcpu_Type = Integer32
_Restartcpu_Object = MibScalar
restartcpu = _Restartcpu_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 2, 2),
    _Restartcpu_Type()
)
restartcpu.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    restartcpu.setStatus("mandatory")


class _Loopbacks_Type(Integer32):
    """Custom type loopbacks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              12)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("if", 4),
          ("modem", 5),
          ("multi", 12),
          ("off", 2))
    )


_Loopbacks_Type.__name__ = "Integer32"
_Loopbacks_Object = MibScalar
loopbacks = _Loopbacks_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 2, 3),
    _Loopbacks_Type()
)
loopbacks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbacks.setStatus("mandatory")
_Loopback_tributary_mask_Type = Integer32
_Loopback_tributary_mask_Object = MibScalar
loopback_tributary_mask = _Loopback_tributary_mask_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 2, 4),
    _Loopback_tributary_mask_Type()
)
loopback_tributary_mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopback_tributary_mask.setStatus("mandatory")
_IpRadioStat_ObjectIdentity = ObjectIdentity
ipRadioStat = _IpRadioStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3)
)
_IpRadioStatEth_ObjectIdentity = ObjectIdentity
ipRadioStatEth = _IpRadioStatEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2)
)
_EthRXTruncatedFrames_Type = Counter32
_EthRXTruncatedFrames_Object = MibScalar
ethRXTruncatedFrames = _EthRXTruncatedFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 1),
    _EthRXTruncatedFrames_Type()
)
ethRXTruncatedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXTruncatedFrames.setStatus("mandatory")
_EthRXLongEvents_Type = Counter32
_EthRXLongEvents_Object = MibScalar
ethRXLongEvents = _EthRXLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 2),
    _EthRXLongEvents_Type()
)
ethRXLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXLongEvents.setStatus("mandatory")
_EthRXVlanTagsDetected_Type = Counter32
_EthRXVlanTagsDetected_Object = MibScalar
ethRXVlanTagsDetected = _EthRXVlanTagsDetected_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 3),
    _EthRXVlanTagsDetected_Type()
)
ethRXVlanTagsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXVlanTagsDetected.setStatus("mandatory")
_EthRXUnsupOpcodes_Type = Counter32
_EthRXUnsupOpcodes_Object = MibScalar
ethRXUnsupOpcodes = _EthRXUnsupOpcodes_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 4),
    _EthRXUnsupOpcodes_Type()
)
ethRXUnsupOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXUnsupOpcodes.setStatus("mandatory")
_EthRXPauseFrames_Type = Counter32
_EthRXPauseFrames_Object = MibScalar
ethRXPauseFrames = _EthRXPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 5),
    _EthRXPauseFrames_Type()
)
ethRXPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXPauseFrames.setStatus("mandatory")
_EthRXControlFrames_Type = Counter32
_EthRXControlFrames_Object = MibScalar
ethRXControlFrames = _EthRXControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 6),
    _EthRXControlFrames_Type()
)
ethRXControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXControlFrames.setStatus("mandatory")
_EthRXDribleNibbles_Type = Counter32
_EthRXDribleNibbles_Object = MibScalar
ethRXDribleNibbles = _EthRXDribleNibbles_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 7),
    _EthRXDribleNibbles_Type()
)
ethRXDribleNibbles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXDribleNibbles.setStatus("mandatory")
_EthRXBroadcasts_Type = Counter32
_EthRXBroadcasts_Object = MibScalar
ethRXBroadcasts = _EthRXBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 8),
    _EthRXBroadcasts_Type()
)
ethRXBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXBroadcasts.setStatus("mandatory")
_EthRXMulticasts_Type = Counter32
_EthRXMulticasts_Object = MibScalar
ethRXMulticasts = _EthRXMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 9),
    _EthRXMulticasts_Type()
)
ethRXMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXMulticasts.setStatus("mandatory")
_EthRXDones_Type = Counter32
_EthRXDones_Object = MibScalar
ethRXDones = _EthRXDones_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 10),
    _EthRXDones_Type()
)
ethRXDones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXDones.setStatus("mandatory")
_EthRXOutOfRangeErrors_Type = Counter32
_EthRXOutOfRangeErrors_Object = MibScalar
ethRXOutOfRangeErrors = _EthRXOutOfRangeErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 11),
    _EthRXOutOfRangeErrors_Type()
)
ethRXOutOfRangeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXOutOfRangeErrors.setStatus("mandatory")
_EthRXLengthCheckerrorsErrors_Type = Counter32
_EthRXLengthCheckerrorsErrors_Object = MibScalar
ethRXLengthCheckerrorsErrors = _EthRXLengthCheckerrorsErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 12),
    _EthRXLengthCheckerrorsErrors_Type()
)
ethRXLengthCheckerrorsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXLengthCheckerrorsErrors.setStatus("mandatory")
_EthRXCRCErrors_Type = Counter32
_EthRXCRCErrors_Object = MibScalar
ethRXCRCErrors = _EthRXCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 13),
    _EthRXCRCErrors_Type()
)
ethRXCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXCRCErrors.setStatus("mandatory")
_EthRXCodeErrors_Type = Counter32
_EthRXCodeErrors_Object = MibScalar
ethRXCodeErrors = _EthRXCodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 14),
    _EthRXCodeErrors_Type()
)
ethRXCodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXCodeErrors.setStatus("mandatory")
_EthRXFalseCarrierErrors_Type = Counter32
_EthRXFalseCarrierErrors_Object = MibScalar
ethRXFalseCarrierErrors = _EthRXFalseCarrierErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 15),
    _EthRXFalseCarrierErrors_Type()
)
ethRXFalseCarrierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXFalseCarrierErrors.setStatus("mandatory")
_EthRXDvEvent_Type = Counter32
_EthRXDvEvent_Object = MibScalar
ethRXDvEvent = _EthRXDvEvent_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 16),
    _EthRXDvEvent_Type()
)
ethRXDvEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXDvEvent.setStatus("mandatory")
_EthRXPrevPktDropped_Type = Counter32
_EthRXPrevPktDropped_Object = MibScalar
ethRXPrevPktDropped = _EthRXPrevPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 17),
    _EthRXPrevPktDropped_Type()
)
ethRXPrevPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXPrevPktDropped.setStatus("mandatory")
_EthRXByteCounterHi_Type = Counter32
_EthRXByteCounterHi_Object = MibScalar
ethRXByteCounterHi = _EthRXByteCounterHi_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 18),
    _EthRXByteCounterHi_Type()
)
ethRXByteCounterHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXByteCounterHi.setStatus("mandatory")
_EthRXByteCounterLow_Type = Counter32
_EthRXByteCounterLow_Object = MibScalar
ethRXByteCounterLow = _EthRXByteCounterLow_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 19),
    _EthRXByteCounterLow_Type()
)
ethRXByteCounterLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethRXByteCounterLow.setStatus("mandatory")
_EthTXVlanTags_Type = Counter32
_EthTXVlanTags_Object = MibScalar
ethTXVlanTags = _EthTXVlanTags_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 21),
    _EthTXVlanTags_Type()
)
ethTXVlanTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXVlanTags.setStatus("mandatory")
_EthTXBackpresEvents_Type = Counter32
_EthTXBackpresEvents_Object = MibScalar
ethTXBackpresEvents = _EthTXBackpresEvents_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 22),
    _EthTXBackpresEvents_Type()
)
ethTXBackpresEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXBackpresEvents.setStatus("mandatory")
_EthTXPauseFrames_Type = Counter32
_EthTXPauseFrames_Object = MibScalar
ethTXPauseFrames = _EthTXPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 23),
    _EthTXPauseFrames_Type()
)
ethTXPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXPauseFrames.setStatus("mandatory")
_EthTXControlFrames_Type = Counter32
_EthTXControlFrames_Object = MibScalar
ethTXControlFrames = _EthTXControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 24),
    _EthTXControlFrames_Type()
)
ethTXControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXControlFrames.setStatus("mandatory")
_EthTXWireByteCounterHi_Type = Counter32
_EthTXWireByteCounterHi_Object = MibScalar
ethTXWireByteCounterHi = _EthTXWireByteCounterHi_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 25),
    _EthTXWireByteCounterHi_Type()
)
ethTXWireByteCounterHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXWireByteCounterHi.setStatus("mandatory")
_EthTXWireByteCounterLow_Type = Counter32
_EthTXWireByteCounterLow_Object = MibScalar
ethTXWireByteCounterLow = _EthTXWireByteCounterLow_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 26),
    _EthTXWireByteCounterLow_Type()
)
ethTXWireByteCounterLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXWireByteCounterLow.setStatus("mandatory")
_EthTXUnderruns_Type = Counter32
_EthTXUnderruns_Object = MibScalar
ethTXUnderruns = _EthTXUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 28),
    _EthTXUnderruns_Type()
)
ethTXUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXUnderruns.setStatus("mandatory")
_EthTXGiants_Type = Counter32
_EthTXGiants_Object = MibScalar
ethTXGiants = _EthTXGiants_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 29),
    _EthTXGiants_Type()
)
ethTXGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXGiants.setStatus("mandatory")
_EthTXLateCollisions_Type = Counter32
_EthTXLateCollisions_Object = MibScalar
ethTXLateCollisions = _EthTXLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 30),
    _EthTXLateCollisions_Type()
)
ethTXLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXLateCollisions.setStatus("mandatory")
_EthTXMaxCollisions_Type = Counter32
_EthTXMaxCollisions_Object = MibScalar
ethTXMaxCollisions = _EthTXMaxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 31),
    _EthTXMaxCollisions_Type()
)
ethTXMaxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXMaxCollisions.setStatus("mandatory")
_EthTXExcessiveDefers_Type = Counter32
_EthTXExcessiveDefers_Object = MibScalar
ethTXExcessiveDefers = _EthTXExcessiveDefers_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 32),
    _EthTXExcessiveDefers_Type()
)
ethTXExcessiveDefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXExcessiveDefers.setStatus("mandatory")
_EthTXNonExcessiveDefers_Type = Counter32
_EthTXNonExcessiveDefers_Object = MibScalar
ethTXNonExcessiveDefers = _EthTXNonExcessiveDefers_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 33),
    _EthTXNonExcessiveDefers_Type()
)
ethTXNonExcessiveDefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXNonExcessiveDefers.setStatus("mandatory")
_EthTXBroadcasts_Type = Counter32
_EthTXBroadcasts_Object = MibScalar
ethTXBroadcasts = _EthTXBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 34),
    _EthTXBroadcasts_Type()
)
ethTXBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXBroadcasts.setStatus("mandatory")
_EthTXMulticasts_Type = Counter32
_EthTXMulticasts_Object = MibScalar
ethTXMulticasts = _EthTXMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 35),
    _EthTXMulticasts_Type()
)
ethTXMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXMulticasts.setStatus("mandatory")
_EthTXDones_Type = Counter32
_EthTXDones_Object = MibScalar
ethTXDones = _EthTXDones_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 36),
    _EthTXDones_Type()
)
ethTXDones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXDones.setStatus("mandatory")
_EthTXLengthCheckErrors_Type = Counter32
_EthTXLengthCheckErrors_Object = MibScalar
ethTXLengthCheckErrors = _EthTXLengthCheckErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 38),
    _EthTXLengthCheckErrors_Type()
)
ethTXLengthCheckErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXLengthCheckErrors.setStatus("mandatory")
_EthTXCRCErrors_Type = Counter32
_EthTXCRCErrors_Object = MibScalar
ethTXCRCErrors = _EthTXCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 39),
    _EthTXCRCErrors_Type()
)
ethTXCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXCRCErrors.setStatus("mandatory")
_EthTXCollisions_Type = Counter32
_EthTXCollisions_Object = MibScalar
ethTXCollisions = _EthTXCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 40),
    _EthTXCollisions_Type()
)
ethTXCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXCollisions.setStatus("mandatory")
_EthTXByteCounterHi_Type = Counter32
_EthTXByteCounterHi_Object = MibScalar
ethTXByteCounterHi = _EthTXByteCounterHi_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 41),
    _EthTXByteCounterHi_Type()
)
ethTXByteCounterHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXByteCounterHi.setStatus("mandatory")
_EthTXByteCounterLow_Type = Counter32
_EthTXByteCounterLow_Object = MibScalar
ethTXByteCounterLow = _EthTXByteCounterLow_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 42),
    _EthTXByteCounterLow_Type()
)
ethTXByteCounterLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTXByteCounterLow.setStatus("mandatory")
_EthGFPFCSErrors_Type = Counter32
_EthGFPFCSErrors_Object = MibScalar
ethGFPFCSErrors = _EthGFPFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 44),
    _EthGFPFCSErrors_Type()
)
ethGFPFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGFPFCSErrors.setStatus("mandatory")
_EthGFPCHECErrors_Type = Counter32
_EthGFPCHECErrors_Object = MibScalar
ethGFPCHECErrors = _EthGFPCHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 45),
    _EthGFPCHECErrors_Type()
)
ethGFPCHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGFPCHECErrors.setStatus("mandatory")
_EthGFPDropedFrames_Type = Counter32
_EthGFPDropedFrames_Object = MibScalar
ethGFPDropedFrames = _EthGFPDropedFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 46),
    _EthGFPDropedFrames_Type()
)
ethGFPDropedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGFPDropedFrames.setStatus("mandatory")
_EthGFPDelineationErrors_Type = Counter32
_EthGFPDelineationErrors_Object = MibScalar
ethGFPDelineationErrors = _EthGFPDelineationErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 47),
    _EthGFPDelineationErrors_Type()
)
ethGFPDelineationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGFPDelineationErrors.setStatus("mandatory")
_EthQOSRXQ1Frames_Type = Counter32
_EthQOSRXQ1Frames_Object = MibScalar
ethQOSRXQ1Frames = _EthQOSRXQ1Frames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 48),
    _EthQOSRXQ1Frames_Type()
)
ethQOSRXQ1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethQOSRXQ1Frames.setStatus("mandatory")
_EthQOSRXQ1Dropped_Type = Counter32
_EthQOSRXQ1Dropped_Object = MibScalar
ethQOSRXQ1Dropped = _EthQOSRXQ1Dropped_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 49),
    _EthQOSRXQ1Dropped_Type()
)
ethQOSRXQ1Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethQOSRXQ1Dropped.setStatus("mandatory")
_EthQOSRXQ2Frames_Type = Counter32
_EthQOSRXQ2Frames_Object = MibScalar
ethQOSRXQ2Frames = _EthQOSRXQ2Frames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 50),
    _EthQOSRXQ2Frames_Type()
)
ethQOSRXQ2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethQOSRXQ2Frames.setStatus("mandatory")
_EthQOSRXQ2Dropped_Type = Counter32
_EthQOSRXQ2Dropped_Object = MibScalar
ethQOSRXQ2Dropped = _EthQOSRXQ2Dropped_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 51),
    _EthQOSRXQ2Dropped_Type()
)
ethQOSRXQ2Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethQOSRXQ2Dropped.setStatus("mandatory")
_EthQOSTXFrames_Type = Counter32
_EthQOSTXFrames_Object = MibScalar
ethQOSTXFrames = _EthQOSTXFrames_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 52),
    _EthQOSTXFrames_Type()
)
ethQOSTXFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethQOSTXFrames.setStatus("mandatory")
_EthQOSTXDropped_Type = Counter32
_EthQOSTXDropped_Object = MibScalar
ethQOSTXDropped = _EthQOSTXDropped_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 2, 53),
    _EthQOSTXDropped_Type()
)
ethQOSTXDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethQOSTXDropped.setStatus("mandatory")
_E1t1StatTable_Object = MibTable
e1t1StatTable = _E1t1StatTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    e1t1StatTable.setStatus("mandatory")
_E1t1StatEntry_Object = MibTableRow
e1t1StatEntry = _E1t1StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    e1t1StatEntry.setStatus("mandatory")


class _E1t1LOS_Type(Integer32):
    """Custom type e1t1LOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_E1t1LOS_Type.__name__ = "Integer32"
_E1t1LOS_Object = MibTableColumn
e1t1LOS = _E1t1LOS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 3, 1, 1),
    _E1t1LOS_Type()
)
e1t1LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1LOS.setStatus("mandatory")


class _E1t1AIS_Type(Integer32):
    """Custom type e1t1AIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_E1t1AIS_Type.__name__ = "Integer32"
_E1t1AIS_Object = MibTableColumn
e1t1AIS = _E1t1AIS_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 3, 1, 2),
    _E1t1AIS_Type()
)
e1t1AIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1AIS.setStatus("mandatory")
_E1t1ChannelNr_Type = Integer32
_E1t1ChannelNr_Object = MibTableColumn
e1t1ChannelNr = _E1t1ChannelNr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 3, 1, 3),
    _E1t1ChannelNr_Type()
)
e1t1ChannelNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1ChannelNr.setStatus("mandatory")
_ModemStatistics_ObjectIdentity = ObjectIdentity
modemStatistics = _ModemStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 4)
)
_ModemCountTime_Type = Counter32
_ModemCountTime_Object = MibScalar
modemCountTime = _ModemCountTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 4, 1),
    _ModemCountTime_Type()
)
modemCountTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCountTime.setStatus("mandatory")
_ModemErroredBlock_Type = Counter32
_ModemErroredBlock_Object = MibScalar
modemErroredBlock = _ModemErroredBlock_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 4, 2),
    _ModemErroredBlock_Type()
)
modemErroredBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemErroredBlock.setStatus("mandatory")
_ModemErroredSecond_Type = Counter32
_ModemErroredSecond_Object = MibScalar
modemErroredSecond = _ModemErroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 4, 3),
    _ModemErroredSecond_Type()
)
modemErroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemErroredSecond.setStatus("mandatory")
_ModemSeverelyErroredSecond_Type = Counter32
_ModemSeverelyErroredSecond_Object = MibScalar
modemSeverelyErroredSecond = _ModemSeverelyErroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 4, 4),
    _ModemSeverelyErroredSecond_Type()
)
modemSeverelyErroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSeverelyErroredSecond.setStatus("mandatory")
_ModemBackgroundBlockErrror_Type = Counter32
_ModemBackgroundBlockErrror_Object = MibScalar
modemBackgroundBlockErrror = _ModemBackgroundBlockErrror_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 4, 5),
    _ModemBackgroundBlockErrror_Type()
)
modemBackgroundBlockErrror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemBackgroundBlockErrror.setStatus("mandatory")
_ModemTotalBlockNumber_Type = Counter32
_ModemTotalBlockNumber_Object = MibScalar
modemTotalBlockNumber = _ModemTotalBlockNumber_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 4, 6),
    _ModemTotalBlockNumber_Type()
)
modemTotalBlockNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemTotalBlockNumber.setStatus("mandatory")
_ModemErroredSecondRatio_Type = DisplayString
_ModemErroredSecondRatio_Object = MibScalar
modemErroredSecondRatio = _ModemErroredSecondRatio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 4, 7),
    _ModemErroredSecondRatio_Type()
)
modemErroredSecondRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemErroredSecondRatio.setStatus("mandatory")
_ModemSeverelyErroredSecondRatio_Type = DisplayString
_ModemSeverelyErroredSecondRatio_Object = MibScalar
modemSeverelyErroredSecondRatio = _ModemSeverelyErroredSecondRatio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 4, 8),
    _ModemSeverelyErroredSecondRatio_Type()
)
modemSeverelyErroredSecondRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemSeverelyErroredSecondRatio.setStatus("mandatory")
_ModemBackgroundBlockErrorRatio_Type = DisplayString
_ModemBackgroundBlockErrorRatio_Object = MibScalar
modemBackgroundBlockErrorRatio = _ModemBackgroundBlockErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 4, 9),
    _ModemBackgroundBlockErrorRatio_Type()
)
modemBackgroundBlockErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemBackgroundBlockErrorRatio.setStatus("mandatory")
_ModemUptime_Type = Counter32
_ModemUptime_Object = MibScalar
modemUptime = _ModemUptime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 4, 10),
    _ModemUptime_Type()
)
modemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemUptime.setStatus("mandatory")
_ModemUnavailtime_Type = Counter32
_ModemUnavailtime_Object = MibScalar
modemUnavailtime = _ModemUnavailtime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 1, 3, 4, 11),
    _ModemUnavailtime_Type()
)
modemUnavailtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemUnavailtime.setStatus("mandatory")
ifEntry.registerAugmentions(
    ("SAF-IPRADIO",
     "vlanEntry")
)
vlanEntry.setIndexNames(*ifEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("SAF-IPRADIO",
     "e1t1StatEntry")
)
e1t1StatEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAF-IPRADIO",
    **{"saf": saf,
       "tehnika": tehnika,
       "microwaveRadio": microwaveRadio,
       "pointToPoint": pointToPoint,
       "safip": safip,
       "ipRadio": ipRadio,
       "ipRadioCfg": ipRadioCfg,
       "ipRadioCfgGeneral": ipRadioCfgGeneral,
       "product": product,
       "description": description,
       "radioName": radioName,
       "sysDateAndTime": sysDateAndTime,
       "sysTemperature": sysTemperature,
       "license": license,
       "licenseMask": licenseMask,
       "radioTable": radioTable,
       "radioEntry": radioEntry,
       "radioIndex": radioIndex,
       "radioGenStatus": radioGenStatus,
       "radioSide": radioSide,
       "radioTxPower": radioTxPower,
       "radioRxLevel": radioRxLevel,
       "radioDuplexShift": radioDuplexShift,
       "radioLoopback": radioLoopback,
       "radioTxMute": radioTxMute,
       "radioTxFrequency": radioTxFrequency,
       "radioRxFrequency": radioRxFrequency,
       "aTPCTable": aTPCTable,
       "aTPCEntry": aTPCEntry,
       "atpcIndex": atpcIndex,
       "atpcEnabled": atpcEnabled,
       "atpcTxPowerCorrection": atpcTxPowerCorrection,
       "modemTable": modemTable,
       "modemEntry": modemEntry,
       "modemIndex": modemIndex,
       "modemGeneralStatus": modemGeneralStatus,
       "modemBandwith": modemBandwith,
       "modemE1T1Channels": modemE1T1Channels,
       "modemModulation": modemModulation,
       "modemTotalCapacity": modemTotalCapacity,
       "modemEthernetCapacity": modemEthernetCapacity,
       "modemAcqStatus": modemAcqStatus,
       "modemLastAcqError": modemLastAcqError,
       "modemRadialMSE": modemRadialMSE,
       "modemInternalAGCgain": modemInternalAGCgain,
       "modemCarrierOffset": modemCarrierOffset,
       "modemSymbolRateTx": modemSymbolRateTx,
       "modemSymbolRateRx": modemSymbolRateRx,
       "modemLDPCdecoderStress": modemLDPCdecoderStress,
       "modemACMengine": modemACMengine,
       "modemACMmodulationMin": modemACMmodulationMin,
       "modemACMtotalCapacity": modemACMtotalCapacity,
       "modemACMethernetCapacity": modemACMethernetCapacity,
       "modemStandard": modemStandard,
       "modemE1T1ChannelMask": modemE1T1ChannelMask,
       "modemACMmodulationMax": modemACMmodulationMax,
       "modemRowStatus": modemRowStatus,
       "vlansEnabled": vlansEnabled,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanNumber": vlanNumber,
       "vlanPortType": vlanPortType,
       "vlanPortmap": vlanPortmap,
       "vlanFid": vlanFid,
       "vlanCfgStat": vlanCfgStat,
       "vlanRowStatus": vlanRowStatus,
       "ipRadioCfgNetwork": ipRadioCfgNetwork,
       "localIp": localIp,
       "localIpMask": localIpMask,
       "remoteIp": remoteIp,
       "ipRadioMgmt": ipRadioMgmt,
       "writeConfig": writeConfig,
       "restartcpu": restartcpu,
       "loopbacks": loopbacks,
       "loopback-tributary-mask": loopback_tributary_mask,
       "ipRadioStat": ipRadioStat,
       "ipRadioStatEth": ipRadioStatEth,
       "ethRXTruncatedFrames": ethRXTruncatedFrames,
       "ethRXLongEvents": ethRXLongEvents,
       "ethRXVlanTagsDetected": ethRXVlanTagsDetected,
       "ethRXUnsupOpcodes": ethRXUnsupOpcodes,
       "ethRXPauseFrames": ethRXPauseFrames,
       "ethRXControlFrames": ethRXControlFrames,
       "ethRXDribleNibbles": ethRXDribleNibbles,
       "ethRXBroadcasts": ethRXBroadcasts,
       "ethRXMulticasts": ethRXMulticasts,
       "ethRXDones": ethRXDones,
       "ethRXOutOfRangeErrors": ethRXOutOfRangeErrors,
       "ethRXLengthCheckerrorsErrors": ethRXLengthCheckerrorsErrors,
       "ethRXCRCErrors": ethRXCRCErrors,
       "ethRXCodeErrors": ethRXCodeErrors,
       "ethRXFalseCarrierErrors": ethRXFalseCarrierErrors,
       "ethRXDvEvent": ethRXDvEvent,
       "ethRXPrevPktDropped": ethRXPrevPktDropped,
       "ethRXByteCounterHi": ethRXByteCounterHi,
       "ethRXByteCounterLow": ethRXByteCounterLow,
       "ethTXVlanTags": ethTXVlanTags,
       "ethTXBackpresEvents": ethTXBackpresEvents,
       "ethTXPauseFrames": ethTXPauseFrames,
       "ethTXControlFrames": ethTXControlFrames,
       "ethTXWireByteCounterHi": ethTXWireByteCounterHi,
       "ethTXWireByteCounterLow": ethTXWireByteCounterLow,
       "ethTXUnderruns": ethTXUnderruns,
       "ethTXGiants": ethTXGiants,
       "ethTXLateCollisions": ethTXLateCollisions,
       "ethTXMaxCollisions": ethTXMaxCollisions,
       "ethTXExcessiveDefers": ethTXExcessiveDefers,
       "ethTXNonExcessiveDefers": ethTXNonExcessiveDefers,
       "ethTXBroadcasts": ethTXBroadcasts,
       "ethTXMulticasts": ethTXMulticasts,
       "ethTXDones": ethTXDones,
       "ethTXLengthCheckErrors": ethTXLengthCheckErrors,
       "ethTXCRCErrors": ethTXCRCErrors,
       "ethTXCollisions": ethTXCollisions,
       "ethTXByteCounterHi": ethTXByteCounterHi,
       "ethTXByteCounterLow": ethTXByteCounterLow,
       "ethGFPFCSErrors": ethGFPFCSErrors,
       "ethGFPCHECErrors": ethGFPCHECErrors,
       "ethGFPDropedFrames": ethGFPDropedFrames,
       "ethGFPDelineationErrors": ethGFPDelineationErrors,
       "ethQOSRXQ1Frames": ethQOSRXQ1Frames,
       "ethQOSRXQ1Dropped": ethQOSRXQ1Dropped,
       "ethQOSRXQ2Frames": ethQOSRXQ2Frames,
       "ethQOSRXQ2Dropped": ethQOSRXQ2Dropped,
       "ethQOSTXFrames": ethQOSTXFrames,
       "ethQOSTXDropped": ethQOSTXDropped,
       "e1t1StatTable": e1t1StatTable,
       "e1t1StatEntry": e1t1StatEntry,
       "e1t1LOS": e1t1LOS,
       "e1t1AIS": e1t1AIS,
       "e1t1ChannelNr": e1t1ChannelNr,
       "modemStatistics": modemStatistics,
       "modemCountTime": modemCountTime,
       "modemErroredBlock": modemErroredBlock,
       "modemErroredSecond": modemErroredSecond,
       "modemSeverelyErroredSecond": modemSeverelyErroredSecond,
       "modemBackgroundBlockErrror": modemBackgroundBlockErrror,
       "modemTotalBlockNumber": modemTotalBlockNumber,
       "modemErroredSecondRatio": modemErroredSecondRatio,
       "modemSeverelyErroredSecondRatio": modemSeverelyErroredSecondRatio,
       "modemBackgroundBlockErrorRatio": modemBackgroundBlockErrorRatio,
       "modemUptime": modemUptime,
       "modemUnavailtime": modemUnavailtime}
)
