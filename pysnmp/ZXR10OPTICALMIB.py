# SNMP MIB module (ZXR10OPTICALMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10OPTICALMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:14 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(zxr10interfaces,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10interfaces")


# MODULE-IDENTITY

zxr10OpticalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class OpticalOnline(Integer32):
    """Custom type OpticalOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", 0),
          ("online", 1))
    )





class SonetComplianceCodesType(Integer32):
    """Custom type SonetComplianceCodesType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("intermediate-reach", 2),
          ("long-reach", 4),
          ("null", 0),
          ("short-reach", 1),
          ("very-Long-reach", 8))
    )





class SonetComplianceCodesSpeed(Integer32):
    """Custom type SonetComplianceCodesSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("oc12", 2),
          ("oc192", 8),
          ("oc3", 1),
          ("oc48", 4))
    )





class GigabitEthernetComplianceCodesType(Integer32):
    """Custom type GigabitEthernetComplianceCodesType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("base-cx-1000", 4),
          ("base-fx-100", 5),
          ("base-lx-100", 3),
          ("base-lx-1000", 2),
          ("base-sx-1000", 1),
          ("base-t-100", 9),
          ("base-t-1000", 8),
          ("base_bx", 6),
          ("base_px", 7),
          ("null", 0))
    )





class InfinibandComplianceCodesType(Integer32):
    """Custom type InfinibandComplianceCodesType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("copper-Active", 2),
          ("copper-Passiv", 1),
          ("lx", 4),
          ("null", 0),
          ("sx", 8))
    )





class GigabitEthernetComplianceCodesSpeed(Integer32):
    """Custom type GigabitEthernetComplianceCodesSpeed based on Integer32"""
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
        *(("g-10", 2),
          ("g-100", 4),
          ("g-40", 3),
          ("m-1000", 1))
    )





class InfinibandComplianceCodesSpeed(Integer32):
    """Custom type InfinibandComplianceCodesSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g-10", 2),
          ("m-1000", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zxr10OpticalTable_Object = MibTable
zxr10OpticalTable = _Zxr10OpticalTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1)
)
if mibBuilder.loadTexts:
    zxr10OpticalTable.setStatus("current")
_Zxr10OpticalEntry_Object = MibTableRow
zxr10OpticalEntry = _Zxr10OpticalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1)
)
zxr10OpticalEntry.setIndexNames(
    (0, "ZXR10OPTICALMIB", "zxr10OpticalIfIndex"),
)
if mibBuilder.loadTexts:
    zxr10OpticalEntry.setStatus("current")
_Zxr10OpticalIfIndex_Type = Integer32
_Zxr10OpticalIfIndex_Object = MibTableColumn
zxr10OpticalIfIndex = _Zxr10OpticalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 1),
    _Zxr10OpticalIfIndex_Type()
)
zxr10OpticalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalIfIndex.setStatus("current")


class _Zxr10OpticalIfName_Type(DisplayString):
    """Custom type zxr10OpticalIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalIfName_Type.__name__ = "DisplayString"
_Zxr10OpticalIfName_Object = MibTableColumn
zxr10OpticalIfName = _Zxr10OpticalIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 2),
    _Zxr10OpticalIfName_Type()
)
zxr10OpticalIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalIfName.setStatus("current")
_Zxr10OpticalOnline_Type = OpticalOnline
_Zxr10OpticalOnline_Object = MibTableColumn
zxr10OpticalOnline = _Zxr10OpticalOnline_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 3),
    _Zxr10OpticalOnline_Type()
)
zxr10OpticalOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalOnline.setStatus("current")


class _Zxr10OpticalFpType_Type(DisplayString):
    """Custom type zxr10OpticalFpType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalFpType_Type.__name__ = "DisplayString"
_Zxr10OpticalFpType_Object = MibTableColumn
zxr10OpticalFpType = _Zxr10OpticalFpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 4),
    _Zxr10OpticalFpType_Type()
)
zxr10OpticalFpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalFpType.setStatus("current")
_Zxr10OpticalSonetComplianceCodesType_Type = SonetComplianceCodesType
_Zxr10OpticalSonetComplianceCodesType_Object = MibTableColumn
zxr10OpticalSonetComplianceCodesType = _Zxr10OpticalSonetComplianceCodesType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 5),
    _Zxr10OpticalSonetComplianceCodesType_Type()
)
zxr10OpticalSonetComplianceCodesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSonetComplianceCodesType.setStatus("current")
_Zxr10OpticalSonetComplianceCodesSpeed_Type = SonetComplianceCodesSpeed
_Zxr10OpticalSonetComplianceCodesSpeed_Object = MibTableColumn
zxr10OpticalSonetComplianceCodesSpeed = _Zxr10OpticalSonetComplianceCodesSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 6),
    _Zxr10OpticalSonetComplianceCodesSpeed_Type()
)
zxr10OpticalSonetComplianceCodesSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSonetComplianceCodesSpeed.setStatus("current")
_Zxr10OpticalGigabitEthernetComplianceCodesType_Type = DisplayString
_Zxr10OpticalGigabitEthernetComplianceCodesType_Object = MibTableColumn
zxr10OpticalGigabitEthernetComplianceCodesType = _Zxr10OpticalGigabitEthernetComplianceCodesType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 7),
    _Zxr10OpticalGigabitEthernetComplianceCodesType_Type()
)
zxr10OpticalGigabitEthernetComplianceCodesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalGigabitEthernetComplianceCodesType.setStatus("current")
_Zxr10OpticalGigabitEthernetComplianceCodesSpeed_Type = GigabitEthernetComplianceCodesSpeed
_Zxr10OpticalGigabitEthernetComplianceCodesSpeed_Object = MibTableColumn
zxr10OpticalGigabitEthernetComplianceCodesSpeed = _Zxr10OpticalGigabitEthernetComplianceCodesSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 8),
    _Zxr10OpticalGigabitEthernetComplianceCodesSpeed_Type()
)
zxr10OpticalGigabitEthernetComplianceCodesSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalGigabitEthernetComplianceCodesSpeed.setStatus("current")
_Zxr10OpticalInfinibandComplianceCodesType_Type = InfinibandComplianceCodesType
_Zxr10OpticalInfinibandComplianceCodesType_Object = MibTableColumn
zxr10OpticalInfinibandComplianceCodesType = _Zxr10OpticalInfinibandComplianceCodesType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 9),
    _Zxr10OpticalInfinibandComplianceCodesType_Type()
)
zxr10OpticalInfinibandComplianceCodesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalInfinibandComplianceCodesType.setStatus("current")
_Zxr10OpticalInfinibandComplianceCodesSpeed_Type = InfinibandComplianceCodesSpeed
_Zxr10OpticalInfinibandComplianceCodesSpeed_Object = MibTableColumn
zxr10OpticalInfinibandComplianceCodesSpeed = _Zxr10OpticalInfinibandComplianceCodesSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 10),
    _Zxr10OpticalInfinibandComplianceCodesSpeed_Type()
)
zxr10OpticalInfinibandComplianceCodesSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalInfinibandComplianceCodesSpeed.setStatus("current")
_Zxr10OpticalDisSMFkm_Type = Integer32
_Zxr10OpticalDisSMFkm_Object = MibTableColumn
zxr10OpticalDisSMFkm = _Zxr10OpticalDisSMFkm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 11),
    _Zxr10OpticalDisSMFkm_Type()
)
zxr10OpticalDisSMFkm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalDisSMFkm.setStatus("current")
_Zxr10OpticalDis9um_Type = Integer32
_Zxr10OpticalDis9um_Object = MibTableColumn
zxr10OpticalDis9um = _Zxr10OpticalDis9um_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 12),
    _Zxr10OpticalDis9um_Type()
)
zxr10OpticalDis9um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalDis9um.setStatus("current")
_Zxr10OpticalDis50um_Type = Integer32
_Zxr10OpticalDis50um_Object = MibTableColumn
zxr10OpticalDis50um = _Zxr10OpticalDis50um_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 13),
    _Zxr10OpticalDis50um_Type()
)
zxr10OpticalDis50um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalDis50um.setStatus("current")
_Zxr10OpticalDis62um_Type = Integer32
_Zxr10OpticalDis62um_Object = MibTableColumn
zxr10OpticalDis62um = _Zxr10OpticalDis62um_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 14),
    _Zxr10OpticalDis62um_Type()
)
zxr10OpticalDis62um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalDis62um.setStatus("current")
_Zxr10OpticalDiscopperLine_Type = Integer32
_Zxr10OpticalDiscopperLine_Object = MibTableColumn
zxr10OpticalDiscopperLine = _Zxr10OpticalDiscopperLine_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 15),
    _Zxr10OpticalDiscopperLine_Type()
)
zxr10OpticalDiscopperLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalDiscopperLine.setStatus("current")
_Zxr10OpticalSWaveLenth_Type = DisplayString
_Zxr10OpticalSWaveLenth_Object = MibTableColumn
zxr10OpticalSWaveLenth = _Zxr10OpticalSWaveLenth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 16),
    _Zxr10OpticalSWaveLenth_Type()
)
zxr10OpticalSWaveLenth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSWaveLenth.setStatus("current")
_Zxr10OpticalSWaveLenthValid_Type = Integer32
_Zxr10OpticalSWaveLenthValid_Object = MibTableColumn
zxr10OpticalSWaveLenthValid = _Zxr10OpticalSWaveLenthValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 17),
    _Zxr10OpticalSWaveLenthValid_Type()
)
zxr10OpticalSWaveLenthValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSWaveLenthValid.setStatus("current")


class _Zxr10OpticalSRxPower_Type(DisplayString):
    """Custom type zxr10OpticalSRxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSRxPower_Type.__name__ = "DisplayString"
_Zxr10OpticalSRxPower_Object = MibTableColumn
zxr10OpticalSRxPower = _Zxr10OpticalSRxPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 18),
    _Zxr10OpticalSRxPower_Type()
)
zxr10OpticalSRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSRxPower.setStatus("current")
_Zxr10OpticalSRxPowerValid_Type = Integer32
_Zxr10OpticalSRxPowerValid_Object = MibTableColumn
zxr10OpticalSRxPowerValid = _Zxr10OpticalSRxPowerValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 19),
    _Zxr10OpticalSRxPowerValid_Type()
)
zxr10OpticalSRxPowerValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSRxPowerValid.setStatus("current")


class _Zxr10OpticalSTxPower_Type(DisplayString):
    """Custom type zxr10OpticalSTxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTxPower_Type.__name__ = "DisplayString"
_Zxr10OpticalSTxPower_Object = MibTableColumn
zxr10OpticalSTxPower = _Zxr10OpticalSTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 20),
    _Zxr10OpticalSTxPower_Type()
)
zxr10OpticalSTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxPower.setStatus("current")
_Zxr10OpticalSTxPowerValid_Type = Integer32
_Zxr10OpticalSTxPowerValid_Object = MibTableColumn
zxr10OpticalSTxPowerValid = _Zxr10OpticalSTxPowerValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 21),
    _Zxr10OpticalSTxPowerValid_Type()
)
zxr10OpticalSTxPowerValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxPowerValid.setStatus("current")


class _Zxr10OpticalSTxCurrent_Type(DisplayString):
    """Custom type zxr10OpticalSTxCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTxCurrent_Type.__name__ = "DisplayString"
_Zxr10OpticalSTxCurrent_Object = MibTableColumn
zxr10OpticalSTxCurrent = _Zxr10OpticalSTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 22),
    _Zxr10OpticalSTxCurrent_Type()
)
zxr10OpticalSTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxCurrent.setStatus("current")
_Zxr10OpticalSTxCurrentValid_Type = Integer32
_Zxr10OpticalSTxCurrentValid_Object = MibTableColumn
zxr10OpticalSTxCurrentValid = _Zxr10OpticalSTxCurrentValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 23),
    _Zxr10OpticalSTxCurrentValid_Type()
)
zxr10OpticalSTxCurrentValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxCurrentValid.setStatus("current")


class _Zxr10OpticalSTemperature_Type(DisplayString):
    """Custom type zxr10OpticalSTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTemperature_Type.__name__ = "DisplayString"
_Zxr10OpticalSTemperature_Object = MibTableColumn
zxr10OpticalSTemperature = _Zxr10OpticalSTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 24),
    _Zxr10OpticalSTemperature_Type()
)
zxr10OpticalSTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTemperature.setStatus("current")
_Zxr10OpticalSTemperatureValid_Type = Integer32
_Zxr10OpticalSTemperatureValid_Object = MibTableColumn
zxr10OpticalSTemperatureValid = _Zxr10OpticalSTemperatureValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 25),
    _Zxr10OpticalSTemperatureValid_Type()
)
zxr10OpticalSTemperatureValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTemperatureValid.setStatus("current")


class _Zxr10Optical33SVoltage_Type(DisplayString):
    """Custom type zxr10Optical33SVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10Optical33SVoltage_Type.__name__ = "DisplayString"
_Zxr10Optical33SVoltage_Object = MibTableColumn
zxr10Optical33SVoltage = _Zxr10Optical33SVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 26),
    _Zxr10Optical33SVoltage_Type()
)
zxr10Optical33SVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10Optical33SVoltage.setStatus("current")
_Zxr10Optical33SVoltageValid_Type = Integer32
_Zxr10Optical33SVoltageValid_Object = MibTableColumn
zxr10Optical33SVoltageValid = _Zxr10Optical33SVoltageValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 27),
    _Zxr10Optical33SVoltageValid_Type()
)
zxr10Optical33SVoltageValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10Optical33SVoltageValid.setStatus("current")


class _Zxr10Optical5SVoltage_Type(DisplayString):
    """Custom type zxr10Optical5SVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10Optical5SVoltage_Type.__name__ = "DisplayString"
_Zxr10Optical5SVoltage_Object = MibTableColumn
zxr10Optical5SVoltage = _Zxr10Optical5SVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 28),
    _Zxr10Optical5SVoltage_Type()
)
zxr10Optical5SVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10Optical5SVoltage.setStatus("current")
_Zxr10Optical5SVoltageValid_Type = Integer32
_Zxr10Optical5SVoltageValid_Object = MibTableColumn
zxr10Optical5SVoltageValid = _Zxr10Optical5SVoltageValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 29),
    _Zxr10Optical5SVoltageValid_Type()
)
zxr10Optical5SVoltageValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10Optical5SVoltageValid.setStatus("current")


class _Zxr10OpticalVName_Type(DisplayString):
    """Custom type zxr10OpticalVName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalVName_Type.__name__ = "DisplayString"
_Zxr10OpticalVName_Object = MibTableColumn
zxr10OpticalVName = _Zxr10OpticalVName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 30),
    _Zxr10OpticalVName_Type()
)
zxr10OpticalVName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalVName.setStatus("current")


class _Zxr10OpticalVPn_Type(DisplayString):
    """Custom type zxr10OpticalVPn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalVPn_Type.__name__ = "DisplayString"
_Zxr10OpticalVPn_Object = MibTableColumn
zxr10OpticalVPn = _Zxr10OpticalVPn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 31),
    _Zxr10OpticalVPn_Type()
)
zxr10OpticalVPn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalVPn.setStatus("current")


class _Zxr10OpticalRev_Type(DisplayString):
    """Custom type zxr10OpticalRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalRev_Type.__name__ = "DisplayString"
_Zxr10OpticalRev_Object = MibTableColumn
zxr10OpticalRev = _Zxr10OpticalRev_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 32),
    _Zxr10OpticalRev_Type()
)
zxr10OpticalRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalRev.setStatus("current")


class _Zxr10OpticalVSn_Type(DisplayString):
    """Custom type zxr10OpticalVSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalVSn_Type.__name__ = "DisplayString"
_Zxr10OpticalVSn_Object = MibTableColumn
zxr10OpticalVSn = _Zxr10OpticalVSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 33),
    _Zxr10OpticalVSn_Type()
)
zxr10OpticalVSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalVSn.setStatus("current")


class _Zxr10OpticalSRxPowerChannel1_Type(DisplayString):
    """Custom type zxr10OpticalSRxPowerChannel1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSRxPowerChannel1_Type.__name__ = "DisplayString"
_Zxr10OpticalSRxPowerChannel1_Object = MibTableColumn
zxr10OpticalSRxPowerChannel1 = _Zxr10OpticalSRxPowerChannel1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 34),
    _Zxr10OpticalSRxPowerChannel1_Type()
)
zxr10OpticalSRxPowerChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSRxPowerChannel1.setStatus("current")
_Zxr10OpticalSRxPowerChannel1Valid_Type = Integer32
_Zxr10OpticalSRxPowerChannel1Valid_Object = MibTableColumn
zxr10OpticalSRxPowerChannel1Valid = _Zxr10OpticalSRxPowerChannel1Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 35),
    _Zxr10OpticalSRxPowerChannel1Valid_Type()
)
zxr10OpticalSRxPowerChannel1Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSRxPowerChannel1Valid.setStatus("current")


class _Zxr10OpticalSRxPowerChannel2_Type(DisplayString):
    """Custom type zxr10OpticalSRxPowerChannel2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSRxPowerChannel2_Type.__name__ = "DisplayString"
_Zxr10OpticalSRxPowerChannel2_Object = MibTableColumn
zxr10OpticalSRxPowerChannel2 = _Zxr10OpticalSRxPowerChannel2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 36),
    _Zxr10OpticalSRxPowerChannel2_Type()
)
zxr10OpticalSRxPowerChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSRxPowerChannel2.setStatus("current")
_Zxr10OpticalSRxPowerChannel2Valid_Type = Integer32
_Zxr10OpticalSRxPowerChannel2Valid_Object = MibTableColumn
zxr10OpticalSRxPowerChannel2Valid = _Zxr10OpticalSRxPowerChannel2Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 37),
    _Zxr10OpticalSRxPowerChannel2Valid_Type()
)
zxr10OpticalSRxPowerChannel2Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSRxPowerChannel2Valid.setStatus("current")


class _Zxr10OpticalSRxPowerChannel3_Type(DisplayString):
    """Custom type zxr10OpticalSRxPowerChannel3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSRxPowerChannel3_Type.__name__ = "DisplayString"
_Zxr10OpticalSRxPowerChannel3_Object = MibTableColumn
zxr10OpticalSRxPowerChannel3 = _Zxr10OpticalSRxPowerChannel3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 38),
    _Zxr10OpticalSRxPowerChannel3_Type()
)
zxr10OpticalSRxPowerChannel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSRxPowerChannel3.setStatus("current")
_Zxr10OpticalSRxPowerChannel3Valid_Type = Integer32
_Zxr10OpticalSRxPowerChannel3Valid_Object = MibTableColumn
zxr10OpticalSRxPowerChannel3Valid = _Zxr10OpticalSRxPowerChannel3Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 39),
    _Zxr10OpticalSRxPowerChannel3Valid_Type()
)
zxr10OpticalSRxPowerChannel3Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSRxPowerChannel3Valid.setStatus("current")


class _Zxr10OpticalSRxPowerChannel4_Type(DisplayString):
    """Custom type zxr10OpticalSRxPowerChannel4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSRxPowerChannel4_Type.__name__ = "DisplayString"
_Zxr10OpticalSRxPowerChannel4_Object = MibTableColumn
zxr10OpticalSRxPowerChannel4 = _Zxr10OpticalSRxPowerChannel4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 40),
    _Zxr10OpticalSRxPowerChannel4_Type()
)
zxr10OpticalSRxPowerChannel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSRxPowerChannel4.setStatus("current")
_Zxr10OpticalSRxPowerChannel4Valid_Type = Integer32
_Zxr10OpticalSRxPowerChannel4Valid_Object = MibTableColumn
zxr10OpticalSRxPowerChannel4Valid = _Zxr10OpticalSRxPowerChannel4Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 41),
    _Zxr10OpticalSRxPowerChannel4Valid_Type()
)
zxr10OpticalSRxPowerChannel4Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSRxPowerChannel4Valid.setStatus("current")


class _Zxr10OpticalSTxPowerChannel1_Type(DisplayString):
    """Custom type zxr10OpticalSTxPowerChannel1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTxPowerChannel1_Type.__name__ = "DisplayString"
_Zxr10OpticalSTxPowerChannel1_Object = MibTableColumn
zxr10OpticalSTxPowerChannel1 = _Zxr10OpticalSTxPowerChannel1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 42),
    _Zxr10OpticalSTxPowerChannel1_Type()
)
zxr10OpticalSTxPowerChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxPowerChannel1.setStatus("current")
_Zxr10OpticalSTxPowerChannel1Valid_Type = Integer32
_Zxr10OpticalSTxPowerChannel1Valid_Object = MibTableColumn
zxr10OpticalSTxPowerChannel1Valid = _Zxr10OpticalSTxPowerChannel1Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 43),
    _Zxr10OpticalSTxPowerChannel1Valid_Type()
)
zxr10OpticalSTxPowerChannel1Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxPowerChannel1Valid.setStatus("current")


class _Zxr10OpticalSTxPowerChannel2_Type(DisplayString):
    """Custom type zxr10OpticalSTxPowerChannel2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTxPowerChannel2_Type.__name__ = "DisplayString"
_Zxr10OpticalSTxPowerChannel2_Object = MibTableColumn
zxr10OpticalSTxPowerChannel2 = _Zxr10OpticalSTxPowerChannel2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 44),
    _Zxr10OpticalSTxPowerChannel2_Type()
)
zxr10OpticalSTxPowerChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxPowerChannel2.setStatus("current")
_Zxr10OpticalSTxPowerChannel2Valid_Type = Integer32
_Zxr10OpticalSTxPowerChannel2Valid_Object = MibTableColumn
zxr10OpticalSTxPowerChannel2Valid = _Zxr10OpticalSTxPowerChannel2Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 45),
    _Zxr10OpticalSTxPowerChannel2Valid_Type()
)
zxr10OpticalSTxPowerChannel2Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxPowerChannel2Valid.setStatus("current")


class _Zxr10OpticalSTxPowerChannel3_Type(DisplayString):
    """Custom type zxr10OpticalSTxPowerChannel3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTxPowerChannel3_Type.__name__ = "DisplayString"
_Zxr10OpticalSTxPowerChannel3_Object = MibTableColumn
zxr10OpticalSTxPowerChannel3 = _Zxr10OpticalSTxPowerChannel3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 46),
    _Zxr10OpticalSTxPowerChannel3_Type()
)
zxr10OpticalSTxPowerChannel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxPowerChannel3.setStatus("current")
_Zxr10OpticalSTxPowerChannel3Valid_Type = Integer32
_Zxr10OpticalSTxPowerChannel3Valid_Object = MibTableColumn
zxr10OpticalSTxPowerChannel3Valid = _Zxr10OpticalSTxPowerChannel3Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 47),
    _Zxr10OpticalSTxPowerChannel3Valid_Type()
)
zxr10OpticalSTxPowerChannel3Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxPowerChannel3Valid.setStatus("current")


class _Zxr10OpticalSTxPowerChannel4_Type(DisplayString):
    """Custom type zxr10OpticalSTxPowerChannel4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTxPowerChannel4_Type.__name__ = "DisplayString"
_Zxr10OpticalSTxPowerChannel4_Object = MibTableColumn
zxr10OpticalSTxPowerChannel4 = _Zxr10OpticalSTxPowerChannel4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 48),
    _Zxr10OpticalSTxPowerChannel4_Type()
)
zxr10OpticalSTxPowerChannel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxPowerChannel4.setStatus("current")
_Zxr10OpticalSTxPowerChannel4Valid_Type = Integer32
_Zxr10OpticalSTxPowerChannel4Valid_Object = MibTableColumn
zxr10OpticalSTxPowerChannel4Valid = _Zxr10OpticalSTxPowerChannel4Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 49),
    _Zxr10OpticalSTxPowerChannel4Valid_Type()
)
zxr10OpticalSTxPowerChannel4Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxPowerChannel4Valid.setStatus("current")


class _Zxr10OpticalSTxCurrentChannel1_Type(DisplayString):
    """Custom type zxr10OpticalSTxCurrentChannel1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTxCurrentChannel1_Type.__name__ = "DisplayString"
_Zxr10OpticalSTxCurrentChannel1_Object = MibTableColumn
zxr10OpticalSTxCurrentChannel1 = _Zxr10OpticalSTxCurrentChannel1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 50),
    _Zxr10OpticalSTxCurrentChannel1_Type()
)
zxr10OpticalSTxCurrentChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxCurrentChannel1.setStatus("current")
_Zxr10OpticalSTxCurrentChannel1Valid_Type = Integer32
_Zxr10OpticalSTxCurrentChannel1Valid_Object = MibTableColumn
zxr10OpticalSTxCurrentChannel1Valid = _Zxr10OpticalSTxCurrentChannel1Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 51),
    _Zxr10OpticalSTxCurrentChannel1Valid_Type()
)
zxr10OpticalSTxCurrentChannel1Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxCurrentChannel1Valid.setStatus("current")


class _Zxr10OpticalSTxCurrentChannel2_Type(DisplayString):
    """Custom type zxr10OpticalSTxCurrentChannel2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTxCurrentChannel2_Type.__name__ = "DisplayString"
_Zxr10OpticalSTxCurrentChannel2_Object = MibTableColumn
zxr10OpticalSTxCurrentChannel2 = _Zxr10OpticalSTxCurrentChannel2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 52),
    _Zxr10OpticalSTxCurrentChannel2_Type()
)
zxr10OpticalSTxCurrentChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxCurrentChannel2.setStatus("current")
_Zxr10OpticalSTxCurrentChannel2Valid_Type = Integer32
_Zxr10OpticalSTxCurrentChannel2Valid_Object = MibTableColumn
zxr10OpticalSTxCurrentChannel2Valid = _Zxr10OpticalSTxCurrentChannel2Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 53),
    _Zxr10OpticalSTxCurrentChannel2Valid_Type()
)
zxr10OpticalSTxCurrentChannel2Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxCurrentChannel2Valid.setStatus("current")


class _Zxr10OpticalSTxCurrentChannel3_Type(DisplayString):
    """Custom type zxr10OpticalSTxCurrentChannel3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTxCurrentChannel3_Type.__name__ = "DisplayString"
_Zxr10OpticalSTxCurrentChannel3_Object = MibTableColumn
zxr10OpticalSTxCurrentChannel3 = _Zxr10OpticalSTxCurrentChannel3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 54),
    _Zxr10OpticalSTxCurrentChannel3_Type()
)
zxr10OpticalSTxCurrentChannel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxCurrentChannel3.setStatus("current")
_Zxr10OpticalSTxCurrentChannel3Valid_Type = Integer32
_Zxr10OpticalSTxCurrentChannel3Valid_Object = MibTableColumn
zxr10OpticalSTxCurrentChannel3Valid = _Zxr10OpticalSTxCurrentChannel3Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 55),
    _Zxr10OpticalSTxCurrentChannel3Valid_Type()
)
zxr10OpticalSTxCurrentChannel3Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxCurrentChannel3Valid.setStatus("current")


class _Zxr10OpticalSTxCurrentChannel4_Type(DisplayString):
    """Custom type zxr10OpticalSTxCurrentChannel4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTxCurrentChannel4_Type.__name__ = "DisplayString"
_Zxr10OpticalSTxCurrentChannel4_Object = MibTableColumn
zxr10OpticalSTxCurrentChannel4 = _Zxr10OpticalSTxCurrentChannel4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 56),
    _Zxr10OpticalSTxCurrentChannel4_Type()
)
zxr10OpticalSTxCurrentChannel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxCurrentChannel4.setStatus("current")
_Zxr10OpticalSTxCurrentChannel4Valid_Type = Integer32
_Zxr10OpticalSTxCurrentChannel4Valid_Object = MibTableColumn
zxr10OpticalSTxCurrentChannel4Valid = _Zxr10OpticalSTxCurrentChannel4Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 57),
    _Zxr10OpticalSTxCurrentChannel4Valid_Type()
)
zxr10OpticalSTxCurrentChannel4Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTxCurrentChannel4Valid.setStatus("current")


class _Zxr10OpticalSTemperatureChannel1_Type(DisplayString):
    """Custom type zxr10OpticalSTemperatureChannel1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTemperatureChannel1_Type.__name__ = "DisplayString"
_Zxr10OpticalSTemperatureChannel1_Object = MibTableColumn
zxr10OpticalSTemperatureChannel1 = _Zxr10OpticalSTemperatureChannel1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 58),
    _Zxr10OpticalSTemperatureChannel1_Type()
)
zxr10OpticalSTemperatureChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTemperatureChannel1.setStatus("current")
_Zxr10OpticalSTemperatureChannel1Valid_Type = Integer32
_Zxr10OpticalSTemperatureChannel1Valid_Object = MibTableColumn
zxr10OpticalSTemperatureChannel1Valid = _Zxr10OpticalSTemperatureChannel1Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 59),
    _Zxr10OpticalSTemperatureChannel1Valid_Type()
)
zxr10OpticalSTemperatureChannel1Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTemperatureChannel1Valid.setStatus("current")


class _Zxr10OpticalSTemperatureChannel2_Type(DisplayString):
    """Custom type zxr10OpticalSTemperatureChannel2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTemperatureChannel2_Type.__name__ = "DisplayString"
_Zxr10OpticalSTemperatureChannel2_Object = MibTableColumn
zxr10OpticalSTemperatureChannel2 = _Zxr10OpticalSTemperatureChannel2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 60),
    _Zxr10OpticalSTemperatureChannel2_Type()
)
zxr10OpticalSTemperatureChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTemperatureChannel2.setStatus("current")
_Zxr10OpticalSTemperatureChannel2Valid_Type = Integer32
_Zxr10OpticalSTemperatureChannel2Valid_Object = MibTableColumn
zxr10OpticalSTemperatureChannel2Valid = _Zxr10OpticalSTemperatureChannel2Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 61),
    _Zxr10OpticalSTemperatureChannel2Valid_Type()
)
zxr10OpticalSTemperatureChannel2Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTemperatureChannel2Valid.setStatus("current")


class _Zxr10OpticalSTemperatureChannel3_Type(DisplayString):
    """Custom type zxr10OpticalSTemperatureChannel3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTemperatureChannel3_Type.__name__ = "DisplayString"
_Zxr10OpticalSTemperatureChannel3_Object = MibTableColumn
zxr10OpticalSTemperatureChannel3 = _Zxr10OpticalSTemperatureChannel3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 62),
    _Zxr10OpticalSTemperatureChannel3_Type()
)
zxr10OpticalSTemperatureChannel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTemperatureChannel3.setStatus("current")
_Zxr10OpticalSTemperatureChannel3Valid_Type = Integer32
_Zxr10OpticalSTemperatureChannel3Valid_Object = MibTableColumn
zxr10OpticalSTemperatureChannel3Valid = _Zxr10OpticalSTemperatureChannel3Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 63),
    _Zxr10OpticalSTemperatureChannel3Valid_Type()
)
zxr10OpticalSTemperatureChannel3Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTemperatureChannel3Valid.setStatus("current")


class _Zxr10OpticalSTemperatureChannel4_Type(DisplayString):
    """Custom type zxr10OpticalSTemperatureChannel4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10OpticalSTemperatureChannel4_Type.__name__ = "DisplayString"
_Zxr10OpticalSTemperatureChannel4_Object = MibTableColumn
zxr10OpticalSTemperatureChannel4 = _Zxr10OpticalSTemperatureChannel4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 64),
    _Zxr10OpticalSTemperatureChannel4_Type()
)
zxr10OpticalSTemperatureChannel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTemperatureChannel4.setStatus("current")
_Zxr10OpticalSTemperatureChannel4Valid_Type = Integer32
_Zxr10OpticalSTemperatureChannel4Valid_Object = MibTableColumn
zxr10OpticalSTemperatureChannel4Valid = _Zxr10OpticalSTemperatureChannel4Valid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 65),
    _Zxr10OpticalSTemperatureChannel4Valid_Type()
)
zxr10OpticalSTemperatureChannel4Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OpticalSTemperatureChannel4Valid.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10OPTICALMIB",
    **{"DisplayString": DisplayString,
       "OpticalOnline": OpticalOnline,
       "SonetComplianceCodesType": SonetComplianceCodesType,
       "SonetComplianceCodesSpeed": SonetComplianceCodesSpeed,
       "GigabitEthernetComplianceCodesType": GigabitEthernetComplianceCodesType,
       "InfinibandComplianceCodesType": InfinibandComplianceCodesType,
       "GigabitEthernetComplianceCodesSpeed": GigabitEthernetComplianceCodesSpeed,
       "InfinibandComplianceCodesSpeed": InfinibandComplianceCodesSpeed,
       "zxr10OpticalMIB": zxr10OpticalMIB,
       "zxr10OpticalTable": zxr10OpticalTable,
       "zxr10OpticalEntry": zxr10OpticalEntry,
       "zxr10OpticalIfIndex": zxr10OpticalIfIndex,
       "zxr10OpticalIfName": zxr10OpticalIfName,
       "zxr10OpticalOnline": zxr10OpticalOnline,
       "zxr10OpticalFpType": zxr10OpticalFpType,
       "zxr10OpticalSonetComplianceCodesType": zxr10OpticalSonetComplianceCodesType,
       "zxr10OpticalSonetComplianceCodesSpeed": zxr10OpticalSonetComplianceCodesSpeed,
       "zxr10OpticalGigabitEthernetComplianceCodesType": zxr10OpticalGigabitEthernetComplianceCodesType,
       "zxr10OpticalGigabitEthernetComplianceCodesSpeed": zxr10OpticalGigabitEthernetComplianceCodesSpeed,
       "zxr10OpticalInfinibandComplianceCodesType": zxr10OpticalInfinibandComplianceCodesType,
       "zxr10OpticalInfinibandComplianceCodesSpeed": zxr10OpticalInfinibandComplianceCodesSpeed,
       "zxr10OpticalDisSMFkm": zxr10OpticalDisSMFkm,
       "zxr10OpticalDis9um": zxr10OpticalDis9um,
       "zxr10OpticalDis50um": zxr10OpticalDis50um,
       "zxr10OpticalDis62um": zxr10OpticalDis62um,
       "zxr10OpticalDiscopperLine": zxr10OpticalDiscopperLine,
       "zxr10OpticalSWaveLenth": zxr10OpticalSWaveLenth,
       "zxr10OpticalSWaveLenthValid": zxr10OpticalSWaveLenthValid,
       "zxr10OpticalSRxPower": zxr10OpticalSRxPower,
       "zxr10OpticalSRxPowerValid": zxr10OpticalSRxPowerValid,
       "zxr10OpticalSTxPower": zxr10OpticalSTxPower,
       "zxr10OpticalSTxPowerValid": zxr10OpticalSTxPowerValid,
       "zxr10OpticalSTxCurrent": zxr10OpticalSTxCurrent,
       "zxr10OpticalSTxCurrentValid": zxr10OpticalSTxCurrentValid,
       "zxr10OpticalSTemperature": zxr10OpticalSTemperature,
       "zxr10OpticalSTemperatureValid": zxr10OpticalSTemperatureValid,
       "zxr10Optical33SVoltage": zxr10Optical33SVoltage,
       "zxr10Optical33SVoltageValid": zxr10Optical33SVoltageValid,
       "zxr10Optical5SVoltage": zxr10Optical5SVoltage,
       "zxr10Optical5SVoltageValid": zxr10Optical5SVoltageValid,
       "zxr10OpticalVName": zxr10OpticalVName,
       "zxr10OpticalVPn": zxr10OpticalVPn,
       "zxr10OpticalRev": zxr10OpticalRev,
       "zxr10OpticalVSn": zxr10OpticalVSn,
       "zxr10OpticalSRxPowerChannel1": zxr10OpticalSRxPowerChannel1,
       "zxr10OpticalSRxPowerChannel1Valid": zxr10OpticalSRxPowerChannel1Valid,
       "zxr10OpticalSRxPowerChannel2": zxr10OpticalSRxPowerChannel2,
       "zxr10OpticalSRxPowerChannel2Valid": zxr10OpticalSRxPowerChannel2Valid,
       "zxr10OpticalSRxPowerChannel3": zxr10OpticalSRxPowerChannel3,
       "zxr10OpticalSRxPowerChannel3Valid": zxr10OpticalSRxPowerChannel3Valid,
       "zxr10OpticalSRxPowerChannel4": zxr10OpticalSRxPowerChannel4,
       "zxr10OpticalSRxPowerChannel4Valid": zxr10OpticalSRxPowerChannel4Valid,
       "zxr10OpticalSTxPowerChannel1": zxr10OpticalSTxPowerChannel1,
       "zxr10OpticalSTxPowerChannel1Valid": zxr10OpticalSTxPowerChannel1Valid,
       "zxr10OpticalSTxPowerChannel2": zxr10OpticalSTxPowerChannel2,
       "zxr10OpticalSTxPowerChannel2Valid": zxr10OpticalSTxPowerChannel2Valid,
       "zxr10OpticalSTxPowerChannel3": zxr10OpticalSTxPowerChannel3,
       "zxr10OpticalSTxPowerChannel3Valid": zxr10OpticalSTxPowerChannel3Valid,
       "zxr10OpticalSTxPowerChannel4": zxr10OpticalSTxPowerChannel4,
       "zxr10OpticalSTxPowerChannel4Valid": zxr10OpticalSTxPowerChannel4Valid,
       "zxr10OpticalSTxCurrentChannel1": zxr10OpticalSTxCurrentChannel1,
       "zxr10OpticalSTxCurrentChannel1Valid": zxr10OpticalSTxCurrentChannel1Valid,
       "zxr10OpticalSTxCurrentChannel2": zxr10OpticalSTxCurrentChannel2,
       "zxr10OpticalSTxCurrentChannel2Valid": zxr10OpticalSTxCurrentChannel2Valid,
       "zxr10OpticalSTxCurrentChannel3": zxr10OpticalSTxCurrentChannel3,
       "zxr10OpticalSTxCurrentChannel3Valid": zxr10OpticalSTxCurrentChannel3Valid,
       "zxr10OpticalSTxCurrentChannel4": zxr10OpticalSTxCurrentChannel4,
       "zxr10OpticalSTxCurrentChannel4Valid": zxr10OpticalSTxCurrentChannel4Valid,
       "zxr10OpticalSTemperatureChannel1": zxr10OpticalSTemperatureChannel1,
       "zxr10OpticalSTemperatureChannel1Valid": zxr10OpticalSTemperatureChannel1Valid,
       "zxr10OpticalSTemperatureChannel2": zxr10OpticalSTemperatureChannel2,
       "zxr10OpticalSTemperatureChannel2Valid": zxr10OpticalSTemperatureChannel2Valid,
       "zxr10OpticalSTemperatureChannel3": zxr10OpticalSTemperatureChannel3,
       "zxr10OpticalSTemperatureChannel3Valid": zxr10OpticalSTemperatureChannel3Valid,
       "zxr10OpticalSTemperatureChannel4": zxr10OpticalSTemperatureChannel4,
       "zxr10OpticalSTemperatureChannel4Valid": zxr10OpticalSTemperatureChannel4Valid}
)
