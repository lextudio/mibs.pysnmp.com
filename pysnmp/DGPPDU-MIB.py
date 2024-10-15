# SNMP MIB module (DGPPDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGPPDU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:22 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dgp_ObjectIdentity = ObjectIdentity
dgp = _Dgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1)
)
_DevTable_ObjectIdentity = ObjectIdentity
devTable = _DevTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2)
)


class _DevID_Type(Integer32):
    """Custom type devID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DevID_Type.__name__ = "Integer32"
_DevID_Object = MibScalar
devID = _DevID_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 1),
    _DevID_Type()
)
devID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devID.setStatus("mandatory")


class _DevIP_Type(DisplayString):
    """Custom type devIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DevIP_Type.__name__ = "DisplayString"
_DevIP_Object = MibScalar
devIP = _DevIP_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 2),
    _DevIP_Type()
)
devIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devIP.setStatus("mandatory")


class _DevMAC_Type(DisplayString):
    """Custom type devMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DevMAC_Type.__name__ = "DisplayString"
_DevMAC_Object = MibScalar
devMAC = _DevMAC_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 3),
    _DevMAC_Type()
)
devMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devMAC.setStatus("mandatory")


class _DevVersion_Type(DisplayString):
    """Custom type devVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DevVersion_Type.__name__ = "DisplayString"
_DevVersion_Object = MibScalar
devVersion = _DevVersion_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 4),
    _DevVersion_Type()
)
devVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devVersion.setStatus("mandatory")


class _DevInfo_Type(DisplayString):
    """Custom type devInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DevInfo_Type.__name__ = "DisplayString"
_DevInfo_Object = MibScalar
devInfo = _DevInfo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 5),
    _DevInfo_Type()
)
devInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devInfo.setStatus("mandatory")


class _DevValues_Type(DisplayString):
    """Custom type devValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DevValues_Type.__name__ = "DisplayString"
_DevValues_Object = MibScalar
devValues = _DevValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 6),
    _DevValues_Type()
)
devValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devValues.setStatus("mandatory")


class _DevTemperature_Type(Integer32):
    """Custom type devTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_DevTemperature_Type.__name__ = "Integer32"
_DevTemperature_Object = MibScalar
devTemperature = _DevTemperature_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 7),
    _DevTemperature_Type()
)
devTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTemperature.setStatus("mandatory")


class _DevHumidity_Type(Integer32):
    """Custom type devHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DevHumidity_Type.__name__ = "Integer32"
_DevHumidity_Object = MibScalar
devHumidity = _DevHumidity_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 8),
    _DevHumidity_Type()
)
devHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devHumidity.setStatus("mandatory")
_PduTable_ObjectIdentity = ObjectIdentity
pduTable = _PduTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9)
)
_Pdu01Entry_ObjectIdentity = ObjectIdentity
pdu01Entry = _Pdu01Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1)
)
_Pdu01Value_Type = Integer32
_Pdu01Value_Object = MibScalar
pdu01Value = _Pdu01Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 11),
    _Pdu01Value_Type()
)
pdu01Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Value.setStatus("mandatory")


class _Pdu01SubValues_Type(DisplayString):
    """Custom type pdu01SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01SubValues_Type.__name__ = "DisplayString"
_Pdu01SubValues_Object = MibScalar
pdu01SubValues = _Pdu01SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 12),
    _Pdu01SubValues_Type()
)
pdu01SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01SubValues.setStatus("mandatory")


class _Pdu01OutletStatus_Type(DisplayString):
    """Custom type pdu01OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu01OutletStatus_Type.__name__ = "DisplayString"
_Pdu01OutletStatus_Object = MibScalar
pdu01OutletStatus = _Pdu01OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 13),
    _Pdu01OutletStatus_Type()
)
pdu01OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01OutletStatus.setStatus("mandatory")
_Pdu01OutletConfigs_ObjectIdentity = ObjectIdentity
pdu01OutletConfigs = _Pdu01OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14)
)


class _Pdu01Outlet1Config_Type(DisplayString):
    """Custom type pdu01Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet1Config_Type.__name__ = "DisplayString"
_Pdu01Outlet1Config_Object = MibScalar
pdu01Outlet1Config = _Pdu01Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 1),
    _Pdu01Outlet1Config_Type()
)
pdu01Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet1Config.setStatus("mandatory")


class _Pdu01Outlet2Config_Type(DisplayString):
    """Custom type pdu01Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet2Config_Type.__name__ = "DisplayString"
_Pdu01Outlet2Config_Object = MibScalar
pdu01Outlet2Config = _Pdu01Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 2),
    _Pdu01Outlet2Config_Type()
)
pdu01Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet2Config.setStatus("mandatory")


class _Pdu01Outlet3Config_Type(DisplayString):
    """Custom type pdu01Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet3Config_Type.__name__ = "DisplayString"
_Pdu01Outlet3Config_Object = MibScalar
pdu01Outlet3Config = _Pdu01Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 3),
    _Pdu01Outlet3Config_Type()
)
pdu01Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet3Config.setStatus("mandatory")


class _Pdu01Outlet4Config_Type(DisplayString):
    """Custom type pdu01Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet4Config_Type.__name__ = "DisplayString"
_Pdu01Outlet4Config_Object = MibScalar
pdu01Outlet4Config = _Pdu01Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 4),
    _Pdu01Outlet4Config_Type()
)
pdu01Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet4Config.setStatus("mandatory")


class _Pdu01Outlet5Config_Type(DisplayString):
    """Custom type pdu01Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet5Config_Type.__name__ = "DisplayString"
_Pdu01Outlet5Config_Object = MibScalar
pdu01Outlet5Config = _Pdu01Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 5),
    _Pdu01Outlet5Config_Type()
)
pdu01Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet5Config.setStatus("mandatory")


class _Pdu01Outlet6Config_Type(DisplayString):
    """Custom type pdu01Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet6Config_Type.__name__ = "DisplayString"
_Pdu01Outlet6Config_Object = MibScalar
pdu01Outlet6Config = _Pdu01Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 6),
    _Pdu01Outlet6Config_Type()
)
pdu01Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet6Config.setStatus("mandatory")


class _Pdu01Outlet7Config_Type(DisplayString):
    """Custom type pdu01Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet7Config_Type.__name__ = "DisplayString"
_Pdu01Outlet7Config_Object = MibScalar
pdu01Outlet7Config = _Pdu01Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 7),
    _Pdu01Outlet7Config_Type()
)
pdu01Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet7Config.setStatus("mandatory")


class _Pdu01Outlet8Config_Type(DisplayString):
    """Custom type pdu01Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet8Config_Type.__name__ = "DisplayString"
_Pdu01Outlet8Config_Object = MibScalar
pdu01Outlet8Config = _Pdu01Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 8),
    _Pdu01Outlet8Config_Type()
)
pdu01Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet8Config.setStatus("mandatory")


class _Pdu01Outlet9Config_Type(DisplayString):
    """Custom type pdu01Outlet9Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet9Config_Type.__name__ = "DisplayString"
_Pdu01Outlet9Config_Object = MibScalar
pdu01Outlet9Config = _Pdu01Outlet9Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 9),
    _Pdu01Outlet9Config_Type()
)
pdu01Outlet9Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet9Config.setStatus("mandatory")


class _Pdu01Outlet10Config_Type(DisplayString):
    """Custom type pdu01Outlet10Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet10Config_Type.__name__ = "DisplayString"
_Pdu01Outlet10Config_Object = MibScalar
pdu01Outlet10Config = _Pdu01Outlet10Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 10),
    _Pdu01Outlet10Config_Type()
)
pdu01Outlet10Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet10Config.setStatus("mandatory")


class _Pdu01Outlet11Config_Type(DisplayString):
    """Custom type pdu01Outlet11Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet11Config_Type.__name__ = "DisplayString"
_Pdu01Outlet11Config_Object = MibScalar
pdu01Outlet11Config = _Pdu01Outlet11Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 11),
    _Pdu01Outlet11Config_Type()
)
pdu01Outlet11Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet11Config.setStatus("mandatory")


class _Pdu01Outlet12Config_Type(DisplayString):
    """Custom type pdu01Outlet12Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet12Config_Type.__name__ = "DisplayString"
_Pdu01Outlet12Config_Object = MibScalar
pdu01Outlet12Config = _Pdu01Outlet12Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 12),
    _Pdu01Outlet12Config_Type()
)
pdu01Outlet12Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet12Config.setStatus("mandatory")


class _Pdu01Outlet13Config_Type(DisplayString):
    """Custom type pdu01Outlet13Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet13Config_Type.__name__ = "DisplayString"
_Pdu01Outlet13Config_Object = MibScalar
pdu01Outlet13Config = _Pdu01Outlet13Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 13),
    _Pdu01Outlet13Config_Type()
)
pdu01Outlet13Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet13Config.setStatus("mandatory")


class _Pdu01Outlet14Config_Type(DisplayString):
    """Custom type pdu01Outlet14Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet14Config_Type.__name__ = "DisplayString"
_Pdu01Outlet14Config_Object = MibScalar
pdu01Outlet14Config = _Pdu01Outlet14Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 14),
    _Pdu01Outlet14Config_Type()
)
pdu01Outlet14Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet14Config.setStatus("mandatory")


class _Pdu01Outlet15Config_Type(DisplayString):
    """Custom type pdu01Outlet15Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet15Config_Type.__name__ = "DisplayString"
_Pdu01Outlet15Config_Object = MibScalar
pdu01Outlet15Config = _Pdu01Outlet15Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 15),
    _Pdu01Outlet15Config_Type()
)
pdu01Outlet15Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet15Config.setStatus("mandatory")


class _Pdu01Outlet16Config_Type(DisplayString):
    """Custom type pdu01Outlet16Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet16Config_Type.__name__ = "DisplayString"
_Pdu01Outlet16Config_Object = MibScalar
pdu01Outlet16Config = _Pdu01Outlet16Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 16),
    _Pdu01Outlet16Config_Type()
)
pdu01Outlet16Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet16Config.setStatus("mandatory")


class _Pdu01Outlet17Config_Type(DisplayString):
    """Custom type pdu01Outlet17Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet17Config_Type.__name__ = "DisplayString"
_Pdu01Outlet17Config_Object = MibScalar
pdu01Outlet17Config = _Pdu01Outlet17Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 17),
    _Pdu01Outlet17Config_Type()
)
pdu01Outlet17Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet17Config.setStatus("mandatory")


class _Pdu01Outlet18Config_Type(DisplayString):
    """Custom type pdu01Outlet18Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet18Config_Type.__name__ = "DisplayString"
_Pdu01Outlet18Config_Object = MibScalar
pdu01Outlet18Config = _Pdu01Outlet18Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 18),
    _Pdu01Outlet18Config_Type()
)
pdu01Outlet18Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet18Config.setStatus("mandatory")


class _Pdu01Outlet19Config_Type(DisplayString):
    """Custom type pdu01Outlet19Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet19Config_Type.__name__ = "DisplayString"
_Pdu01Outlet19Config_Object = MibScalar
pdu01Outlet19Config = _Pdu01Outlet19Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 19),
    _Pdu01Outlet19Config_Type()
)
pdu01Outlet19Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet19Config.setStatus("mandatory")


class _Pdu01Outlet20Config_Type(DisplayString):
    """Custom type pdu01Outlet20Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet20Config_Type.__name__ = "DisplayString"
_Pdu01Outlet20Config_Object = MibScalar
pdu01Outlet20Config = _Pdu01Outlet20Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 20),
    _Pdu01Outlet20Config_Type()
)
pdu01Outlet20Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet20Config.setStatus("mandatory")


class _Pdu01Outlet21Config_Type(DisplayString):
    """Custom type pdu01Outlet21Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet21Config_Type.__name__ = "DisplayString"
_Pdu01Outlet21Config_Object = MibScalar
pdu01Outlet21Config = _Pdu01Outlet21Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 21),
    _Pdu01Outlet21Config_Type()
)
pdu01Outlet21Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet21Config.setStatus("mandatory")


class _Pdu01Outlet22Config_Type(DisplayString):
    """Custom type pdu01Outlet22Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet22Config_Type.__name__ = "DisplayString"
_Pdu01Outlet22Config_Object = MibScalar
pdu01Outlet22Config = _Pdu01Outlet22Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 22),
    _Pdu01Outlet22Config_Type()
)
pdu01Outlet22Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet22Config.setStatus("mandatory")


class _Pdu01Outlet23Config_Type(DisplayString):
    """Custom type pdu01Outlet23Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet23Config_Type.__name__ = "DisplayString"
_Pdu01Outlet23Config_Object = MibScalar
pdu01Outlet23Config = _Pdu01Outlet23Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 23),
    _Pdu01Outlet23Config_Type()
)
pdu01Outlet23Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet23Config.setStatus("mandatory")


class _Pdu01Outlet24Config_Type(DisplayString):
    """Custom type pdu01Outlet24Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu01Outlet24Config_Type.__name__ = "DisplayString"
_Pdu01Outlet24Config_Object = MibScalar
pdu01Outlet24Config = _Pdu01Outlet24Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 14, 24),
    _Pdu01Outlet24Config_Type()
)
pdu01Outlet24Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Outlet24Config.setStatus("mandatory")


class _Pdu01Threshold1_Type(Integer32):
    """Custom type pdu01Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu01Threshold1_Type.__name__ = "Integer32"
_Pdu01Threshold1_Object = MibScalar
pdu01Threshold1 = _Pdu01Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 15),
    _Pdu01Threshold1_Type()
)
pdu01Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu01Threshold1.setStatus("mandatory")


class _Pdu01Threshold2_Type(Integer32):
    """Custom type pdu01Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu01Threshold2_Type.__name__ = "Integer32"
_Pdu01Threshold2_Object = MibScalar
pdu01Threshold2 = _Pdu01Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 16),
    _Pdu01Threshold2_Type()
)
pdu01Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu01Threshold2.setStatus("mandatory")


class _Pdu01Voltage_Type(Integer32):
    """Custom type pdu01Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu01Voltage_Type.__name__ = "Integer32"
_Pdu01Voltage_Object = MibScalar
pdu01Voltage = _Pdu01Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 17),
    _Pdu01Voltage_Type()
)
pdu01Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Voltage.setStatus("mandatory")


class _Pdu01ModelName_Type(DisplayString):
    """Custom type pdu01ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu01ModelName_Type.__name__ = "DisplayString"
_Pdu01ModelName_Object = MibScalar
pdu01ModelName = _Pdu01ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 18),
    _Pdu01ModelName_Type()
)
pdu01ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01ModelName.setStatus("mandatory")


class _Pdu01ModelNo_Type(DisplayString):
    """Custom type pdu01ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu01ModelNo_Type.__name__ = "DisplayString"
_Pdu01ModelNo_Object = MibScalar
pdu01ModelNo = _Pdu01ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 19),
    _Pdu01ModelNo_Type()
)
pdu01ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01ModelNo.setStatus("mandatory")


class _Pdu01Identify_Type(DisplayString):
    """Custom type pdu01Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu01Identify_Type.__name__ = "DisplayString"
_Pdu01Identify_Object = MibScalar
pdu01Identify = _Pdu01Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 1, 20),
    _Pdu01Identify_Type()
)
pdu01Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu01Identify.setStatus("mandatory")
_Pdu02Entry_ObjectIdentity = ObjectIdentity
pdu02Entry = _Pdu02Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2)
)
_Pdu02Value_Type = Integer32
_Pdu02Value_Object = MibScalar
pdu02Value = _Pdu02Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 11),
    _Pdu02Value_Type()
)
pdu02Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02Value.setStatus("mandatory")


class _Pdu02SubValues_Type(DisplayString):
    """Custom type pdu02SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu02SubValues_Type.__name__ = "DisplayString"
_Pdu02SubValues_Object = MibScalar
pdu02SubValues = _Pdu02SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 12),
    _Pdu02SubValues_Type()
)
pdu02SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02SubValues.setStatus("mandatory")


class _Pdu02OutletStatus_Type(DisplayString):
    """Custom type pdu02OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu02OutletStatus_Type.__name__ = "DisplayString"
_Pdu02OutletStatus_Object = MibScalar
pdu02OutletStatus = _Pdu02OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 13),
    _Pdu02OutletStatus_Type()
)
pdu02OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02OutletStatus.setStatus("mandatory")
_Pdu02OutletConfigs_ObjectIdentity = ObjectIdentity
pdu02OutletConfigs = _Pdu02OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 14)
)


class _Pdu02Outlet1Config_Type(DisplayString):
    """Custom type pdu02Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu02Outlet1Config_Type.__name__ = "DisplayString"
_Pdu02Outlet1Config_Object = MibScalar
pdu02Outlet1Config = _Pdu02Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 14, 1),
    _Pdu02Outlet1Config_Type()
)
pdu02Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02Outlet1Config.setStatus("mandatory")


class _Pdu02Outlet2Config_Type(DisplayString):
    """Custom type pdu02Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu02Outlet2Config_Type.__name__ = "DisplayString"
_Pdu02Outlet2Config_Object = MibScalar
pdu02Outlet2Config = _Pdu02Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 14, 2),
    _Pdu02Outlet2Config_Type()
)
pdu02Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02Outlet2Config.setStatus("mandatory")


class _Pdu02Outlet3Config_Type(DisplayString):
    """Custom type pdu02Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu02Outlet3Config_Type.__name__ = "DisplayString"
_Pdu02Outlet3Config_Object = MibScalar
pdu02Outlet3Config = _Pdu02Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 14, 3),
    _Pdu02Outlet3Config_Type()
)
pdu02Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02Outlet3Config.setStatus("mandatory")


class _Pdu02Outlet4Config_Type(DisplayString):
    """Custom type pdu02Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu02Outlet4Config_Type.__name__ = "DisplayString"
_Pdu02Outlet4Config_Object = MibScalar
pdu02Outlet4Config = _Pdu02Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 14, 4),
    _Pdu02Outlet4Config_Type()
)
pdu02Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02Outlet4Config.setStatus("mandatory")


class _Pdu02Outlet5Config_Type(DisplayString):
    """Custom type pdu02Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu02Outlet5Config_Type.__name__ = "DisplayString"
_Pdu02Outlet5Config_Object = MibScalar
pdu02Outlet5Config = _Pdu02Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 14, 5),
    _Pdu02Outlet5Config_Type()
)
pdu02Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02Outlet5Config.setStatus("mandatory")


class _Pdu02Outlet6Config_Type(DisplayString):
    """Custom type pdu02Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu02Outlet6Config_Type.__name__ = "DisplayString"
_Pdu02Outlet6Config_Object = MibScalar
pdu02Outlet6Config = _Pdu02Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 14, 6),
    _Pdu02Outlet6Config_Type()
)
pdu02Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02Outlet6Config.setStatus("mandatory")


class _Pdu02Outlet7Config_Type(DisplayString):
    """Custom type pdu02Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu02Outlet7Config_Type.__name__ = "DisplayString"
_Pdu02Outlet7Config_Object = MibScalar
pdu02Outlet7Config = _Pdu02Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 14, 7),
    _Pdu02Outlet7Config_Type()
)
pdu02Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02Outlet7Config.setStatus("mandatory")


class _Pdu02Outlet8Config_Type(DisplayString):
    """Custom type pdu02Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu02Outlet8Config_Type.__name__ = "DisplayString"
_Pdu02Outlet8Config_Object = MibScalar
pdu02Outlet8Config = _Pdu02Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 14, 8),
    _Pdu02Outlet8Config_Type()
)
pdu02Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02Outlet8Config.setStatus("mandatory")


class _Pdu02Threshold1_Type(Integer32):
    """Custom type pdu02Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu02Threshold1_Type.__name__ = "Integer32"
_Pdu02Threshold1_Object = MibScalar
pdu02Threshold1 = _Pdu02Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 15),
    _Pdu02Threshold1_Type()
)
pdu02Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu02Threshold1.setStatus("mandatory")


class _Pdu02Threshold2_Type(Integer32):
    """Custom type pdu02Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu02Threshold2_Type.__name__ = "Integer32"
_Pdu02Threshold2_Object = MibScalar
pdu02Threshold2 = _Pdu02Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 16),
    _Pdu02Threshold2_Type()
)
pdu02Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu02Threshold2.setStatus("mandatory")


class _Pdu02Voltage_Type(Integer32):
    """Custom type pdu02Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu02Voltage_Type.__name__ = "Integer32"
_Pdu02Voltage_Object = MibScalar
pdu02Voltage = _Pdu02Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 17),
    _Pdu02Voltage_Type()
)
pdu02Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02Voltage.setStatus("mandatory")


class _Pdu02ModelName_Type(DisplayString):
    """Custom type pdu02ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu02ModelName_Type.__name__ = "DisplayString"
_Pdu02ModelName_Object = MibScalar
pdu02ModelName = _Pdu02ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 18),
    _Pdu02ModelName_Type()
)
pdu02ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02ModelName.setStatus("mandatory")


class _Pdu02ModelNo_Type(DisplayString):
    """Custom type pdu02ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu02ModelNo_Type.__name__ = "DisplayString"
_Pdu02ModelNo_Object = MibScalar
pdu02ModelNo = _Pdu02ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 19),
    _Pdu02ModelNo_Type()
)
pdu02ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02ModelNo.setStatus("mandatory")


class _Pdu02Identify_Type(DisplayString):
    """Custom type pdu02Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu02Identify_Type.__name__ = "DisplayString"
_Pdu02Identify_Object = MibScalar
pdu02Identify = _Pdu02Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 2, 20),
    _Pdu02Identify_Type()
)
pdu02Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu02Identify.setStatus("mandatory")
_Pdu03Entry_ObjectIdentity = ObjectIdentity
pdu03Entry = _Pdu03Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3)
)
_Pdu03Value_Type = Integer32
_Pdu03Value_Object = MibScalar
pdu03Value = _Pdu03Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 11),
    _Pdu03Value_Type()
)
pdu03Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03Value.setStatus("mandatory")


class _Pdu03SubValues_Type(DisplayString):
    """Custom type pdu03SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu03SubValues_Type.__name__ = "DisplayString"
_Pdu03SubValues_Object = MibScalar
pdu03SubValues = _Pdu03SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 12),
    _Pdu03SubValues_Type()
)
pdu03SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03SubValues.setStatus("mandatory")


class _Pdu03OutletStatus_Type(DisplayString):
    """Custom type pdu03OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu03OutletStatus_Type.__name__ = "DisplayString"
_Pdu03OutletStatus_Object = MibScalar
pdu03OutletStatus = _Pdu03OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 13),
    _Pdu03OutletStatus_Type()
)
pdu03OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03OutletStatus.setStatus("mandatory")
_Pdu03OutletConfigs_ObjectIdentity = ObjectIdentity
pdu03OutletConfigs = _Pdu03OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 14)
)


class _Pdu03Outlet1Config_Type(DisplayString):
    """Custom type pdu03Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu03Outlet1Config_Type.__name__ = "DisplayString"
_Pdu03Outlet1Config_Object = MibScalar
pdu03Outlet1Config = _Pdu03Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 14, 1),
    _Pdu03Outlet1Config_Type()
)
pdu03Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03Outlet1Config.setStatus("mandatory")


class _Pdu03Outlet2Config_Type(DisplayString):
    """Custom type pdu03Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu03Outlet2Config_Type.__name__ = "DisplayString"
_Pdu03Outlet2Config_Object = MibScalar
pdu03Outlet2Config = _Pdu03Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 14, 2),
    _Pdu03Outlet2Config_Type()
)
pdu03Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03Outlet2Config.setStatus("mandatory")


class _Pdu03Outlet3Config_Type(DisplayString):
    """Custom type pdu03Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu03Outlet3Config_Type.__name__ = "DisplayString"
_Pdu03Outlet3Config_Object = MibScalar
pdu03Outlet3Config = _Pdu03Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 14, 3),
    _Pdu03Outlet3Config_Type()
)
pdu03Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03Outlet3Config.setStatus("mandatory")


class _Pdu03Outlet4Config_Type(DisplayString):
    """Custom type pdu03Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu03Outlet4Config_Type.__name__ = "DisplayString"
_Pdu03Outlet4Config_Object = MibScalar
pdu03Outlet4Config = _Pdu03Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 14, 4),
    _Pdu03Outlet4Config_Type()
)
pdu03Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03Outlet4Config.setStatus("mandatory")


class _Pdu03Outlet5Config_Type(DisplayString):
    """Custom type pdu03Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu03Outlet5Config_Type.__name__ = "DisplayString"
_Pdu03Outlet5Config_Object = MibScalar
pdu03Outlet5Config = _Pdu03Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 14, 5),
    _Pdu03Outlet5Config_Type()
)
pdu03Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03Outlet5Config.setStatus("mandatory")


class _Pdu03Outlet6Config_Type(DisplayString):
    """Custom type pdu03Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu03Outlet6Config_Type.__name__ = "DisplayString"
_Pdu03Outlet6Config_Object = MibScalar
pdu03Outlet6Config = _Pdu03Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 14, 6),
    _Pdu03Outlet6Config_Type()
)
pdu03Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03Outlet6Config.setStatus("mandatory")


class _Pdu03Outlet7Config_Type(DisplayString):
    """Custom type pdu03Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu03Outlet7Config_Type.__name__ = "DisplayString"
_Pdu03Outlet7Config_Object = MibScalar
pdu03Outlet7Config = _Pdu03Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 14, 7),
    _Pdu03Outlet7Config_Type()
)
pdu03Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03Outlet7Config.setStatus("mandatory")


class _Pdu03Outlet8Config_Type(DisplayString):
    """Custom type pdu03Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu03Outlet8Config_Type.__name__ = "DisplayString"
_Pdu03Outlet8Config_Object = MibScalar
pdu03Outlet8Config = _Pdu03Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 14, 8),
    _Pdu03Outlet8Config_Type()
)
pdu03Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03Outlet8Config.setStatus("mandatory")


class _Pdu03Threshold1_Type(Integer32):
    """Custom type pdu03Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu03Threshold1_Type.__name__ = "Integer32"
_Pdu03Threshold1_Object = MibScalar
pdu03Threshold1 = _Pdu03Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 15),
    _Pdu03Threshold1_Type()
)
pdu03Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu03Threshold1.setStatus("mandatory")


class _Pdu03Threshold2_Type(Integer32):
    """Custom type pdu03Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu03Threshold2_Type.__name__ = "Integer32"
_Pdu03Threshold2_Object = MibScalar
pdu03Threshold2 = _Pdu03Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 16),
    _Pdu03Threshold2_Type()
)
pdu03Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu03Threshold2.setStatus("mandatory")


class _Pdu03Voltage_Type(Integer32):
    """Custom type pdu03Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu03Voltage_Type.__name__ = "Integer32"
_Pdu03Voltage_Object = MibScalar
pdu03Voltage = _Pdu03Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 17),
    _Pdu03Voltage_Type()
)
pdu03Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03Voltage.setStatus("mandatory")


class _Pdu03ModelName_Type(DisplayString):
    """Custom type pdu03ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu03ModelName_Type.__name__ = "DisplayString"
_Pdu03ModelName_Object = MibScalar
pdu03ModelName = _Pdu03ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 18),
    _Pdu03ModelName_Type()
)
pdu03ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03ModelName.setStatus("mandatory")


class _Pdu03ModelNo_Type(DisplayString):
    """Custom type pdu03ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu03ModelNo_Type.__name__ = "DisplayString"
_Pdu03ModelNo_Object = MibScalar
pdu03ModelNo = _Pdu03ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 19),
    _Pdu03ModelNo_Type()
)
pdu03ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03ModelNo.setStatus("mandatory")


class _Pdu03Identify_Type(DisplayString):
    """Custom type pdu03Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu03Identify_Type.__name__ = "DisplayString"
_Pdu03Identify_Object = MibScalar
pdu03Identify = _Pdu03Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 3, 20),
    _Pdu03Identify_Type()
)
pdu03Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu03Identify.setStatus("mandatory")
_Pdu04Entry_ObjectIdentity = ObjectIdentity
pdu04Entry = _Pdu04Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4)
)
_Pdu04Value_Type = Integer32
_Pdu04Value_Object = MibScalar
pdu04Value = _Pdu04Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 11),
    _Pdu04Value_Type()
)
pdu04Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04Value.setStatus("mandatory")


class _Pdu04SubValues_Type(DisplayString):
    """Custom type pdu04SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu04SubValues_Type.__name__ = "DisplayString"
_Pdu04SubValues_Object = MibScalar
pdu04SubValues = _Pdu04SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 12),
    _Pdu04SubValues_Type()
)
pdu04SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04SubValues.setStatus("mandatory")


class _Pdu04OutletStatus_Type(DisplayString):
    """Custom type pdu04OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu04OutletStatus_Type.__name__ = "DisplayString"
_Pdu04OutletStatus_Object = MibScalar
pdu04OutletStatus = _Pdu04OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 13),
    _Pdu04OutletStatus_Type()
)
pdu04OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04OutletStatus.setStatus("mandatory")
_Pdu04OutletConfigs_ObjectIdentity = ObjectIdentity
pdu04OutletConfigs = _Pdu04OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 14)
)


class _Pdu04Outlet1Config_Type(DisplayString):
    """Custom type pdu04Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu04Outlet1Config_Type.__name__ = "DisplayString"
_Pdu04Outlet1Config_Object = MibScalar
pdu04Outlet1Config = _Pdu04Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 14, 1),
    _Pdu04Outlet1Config_Type()
)
pdu04Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04Outlet1Config.setStatus("mandatory")


class _Pdu04Outlet2Config_Type(DisplayString):
    """Custom type pdu04Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu04Outlet2Config_Type.__name__ = "DisplayString"
_Pdu04Outlet2Config_Object = MibScalar
pdu04Outlet2Config = _Pdu04Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 14, 2),
    _Pdu04Outlet2Config_Type()
)
pdu04Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04Outlet2Config.setStatus("mandatory")


class _Pdu04Outlet3Config_Type(DisplayString):
    """Custom type pdu04Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu04Outlet3Config_Type.__name__ = "DisplayString"
_Pdu04Outlet3Config_Object = MibScalar
pdu04Outlet3Config = _Pdu04Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 14, 3),
    _Pdu04Outlet3Config_Type()
)
pdu04Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04Outlet3Config.setStatus("mandatory")


class _Pdu04Outlet4Config_Type(DisplayString):
    """Custom type pdu04Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu04Outlet4Config_Type.__name__ = "DisplayString"
_Pdu04Outlet4Config_Object = MibScalar
pdu04Outlet4Config = _Pdu04Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 14, 4),
    _Pdu04Outlet4Config_Type()
)
pdu04Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04Outlet4Config.setStatus("mandatory")


class _Pdu04Outlet5Config_Type(DisplayString):
    """Custom type pdu04Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu04Outlet5Config_Type.__name__ = "DisplayString"
_Pdu04Outlet5Config_Object = MibScalar
pdu04Outlet5Config = _Pdu04Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 14, 5),
    _Pdu04Outlet5Config_Type()
)
pdu04Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04Outlet5Config.setStatus("mandatory")


class _Pdu04Outlet6Config_Type(DisplayString):
    """Custom type pdu04Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu04Outlet6Config_Type.__name__ = "DisplayString"
_Pdu04Outlet6Config_Object = MibScalar
pdu04Outlet6Config = _Pdu04Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 14, 6),
    _Pdu04Outlet6Config_Type()
)
pdu04Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04Outlet6Config.setStatus("mandatory")


class _Pdu04Outlet7Config_Type(DisplayString):
    """Custom type pdu04Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu04Outlet7Config_Type.__name__ = "DisplayString"
_Pdu04Outlet7Config_Object = MibScalar
pdu04Outlet7Config = _Pdu04Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 14, 7),
    _Pdu04Outlet7Config_Type()
)
pdu04Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04Outlet7Config.setStatus("mandatory")


class _Pdu04Outlet8Config_Type(DisplayString):
    """Custom type pdu04Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu04Outlet8Config_Type.__name__ = "DisplayString"
_Pdu04Outlet8Config_Object = MibScalar
pdu04Outlet8Config = _Pdu04Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 14, 8),
    _Pdu04Outlet8Config_Type()
)
pdu04Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04Outlet8Config.setStatus("mandatory")


class _Pdu04Threshold1_Type(Integer32):
    """Custom type pdu04Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu04Threshold1_Type.__name__ = "Integer32"
_Pdu04Threshold1_Object = MibScalar
pdu04Threshold1 = _Pdu04Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 15),
    _Pdu04Threshold1_Type()
)
pdu04Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu04Threshold1.setStatus("mandatory")


class _Pdu04Threshold2_Type(Integer32):
    """Custom type pdu04Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu04Threshold2_Type.__name__ = "Integer32"
_Pdu04Threshold2_Object = MibScalar
pdu04Threshold2 = _Pdu04Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 16),
    _Pdu04Threshold2_Type()
)
pdu04Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu04Threshold2.setStatus("mandatory")


class _Pdu04Voltage_Type(Integer32):
    """Custom type pdu04Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu04Voltage_Type.__name__ = "Integer32"
_Pdu04Voltage_Object = MibScalar
pdu04Voltage = _Pdu04Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 17),
    _Pdu04Voltage_Type()
)
pdu04Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04Voltage.setStatus("mandatory")


class _Pdu04ModelName_Type(DisplayString):
    """Custom type pdu04ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu04ModelName_Type.__name__ = "DisplayString"
_Pdu04ModelName_Object = MibScalar
pdu04ModelName = _Pdu04ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 18),
    _Pdu04ModelName_Type()
)
pdu04ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04ModelName.setStatus("mandatory")


class _Pdu04ModelNo_Type(DisplayString):
    """Custom type pdu04ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu04ModelNo_Type.__name__ = "DisplayString"
_Pdu04ModelNo_Object = MibScalar
pdu04ModelNo = _Pdu04ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 19),
    _Pdu04ModelNo_Type()
)
pdu04ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04ModelNo.setStatus("mandatory")


class _Pdu04Identify_Type(DisplayString):
    """Custom type pdu04Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu04Identify_Type.__name__ = "DisplayString"
_Pdu04Identify_Object = MibScalar
pdu04Identify = _Pdu04Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 4, 20),
    _Pdu04Identify_Type()
)
pdu04Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu04Identify.setStatus("mandatory")
_Pdu05Entry_ObjectIdentity = ObjectIdentity
pdu05Entry = _Pdu05Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5)
)
_Pdu05Value_Type = Integer32
_Pdu05Value_Object = MibScalar
pdu05Value = _Pdu05Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 11),
    _Pdu05Value_Type()
)
pdu05Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05Value.setStatus("mandatory")


class _Pdu05SubValues_Type(DisplayString):
    """Custom type pdu05SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu05SubValues_Type.__name__ = "DisplayString"
_Pdu05SubValues_Object = MibScalar
pdu05SubValues = _Pdu05SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 12),
    _Pdu05SubValues_Type()
)
pdu05SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05SubValues.setStatus("mandatory")


class _Pdu05OutletStatus_Type(DisplayString):
    """Custom type pdu05OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu05OutletStatus_Type.__name__ = "DisplayString"
_Pdu05OutletStatus_Object = MibScalar
pdu05OutletStatus = _Pdu05OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 13),
    _Pdu05OutletStatus_Type()
)
pdu05OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05OutletStatus.setStatus("mandatory")
_Pdu05OutletConfigs_ObjectIdentity = ObjectIdentity
pdu05OutletConfigs = _Pdu05OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 14)
)


class _Pdu05Outlet1Config_Type(DisplayString):
    """Custom type pdu05Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu05Outlet1Config_Type.__name__ = "DisplayString"
_Pdu05Outlet1Config_Object = MibScalar
pdu05Outlet1Config = _Pdu05Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 14, 1),
    _Pdu05Outlet1Config_Type()
)
pdu05Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05Outlet1Config.setStatus("mandatory")


class _Pdu05Outlet2Config_Type(DisplayString):
    """Custom type pdu05Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu05Outlet2Config_Type.__name__ = "DisplayString"
_Pdu05Outlet2Config_Object = MibScalar
pdu05Outlet2Config = _Pdu05Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 14, 2),
    _Pdu05Outlet2Config_Type()
)
pdu05Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05Outlet2Config.setStatus("mandatory")


class _Pdu05Outlet3Config_Type(DisplayString):
    """Custom type pdu05Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu05Outlet3Config_Type.__name__ = "DisplayString"
_Pdu05Outlet3Config_Object = MibScalar
pdu05Outlet3Config = _Pdu05Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 14, 3),
    _Pdu05Outlet3Config_Type()
)
pdu05Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05Outlet3Config.setStatus("mandatory")


class _Pdu05Outlet4Config_Type(DisplayString):
    """Custom type pdu05Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu05Outlet4Config_Type.__name__ = "DisplayString"
_Pdu05Outlet4Config_Object = MibScalar
pdu05Outlet4Config = _Pdu05Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 14, 4),
    _Pdu05Outlet4Config_Type()
)
pdu05Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05Outlet4Config.setStatus("mandatory")


class _Pdu05Outlet5Config_Type(DisplayString):
    """Custom type pdu05Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu05Outlet5Config_Type.__name__ = "DisplayString"
_Pdu05Outlet5Config_Object = MibScalar
pdu05Outlet5Config = _Pdu05Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 14, 5),
    _Pdu05Outlet5Config_Type()
)
pdu05Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05Outlet5Config.setStatus("mandatory")


class _Pdu05Outlet6Config_Type(DisplayString):
    """Custom type pdu05Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu05Outlet6Config_Type.__name__ = "DisplayString"
_Pdu05Outlet6Config_Object = MibScalar
pdu05Outlet6Config = _Pdu05Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 14, 6),
    _Pdu05Outlet6Config_Type()
)
pdu05Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05Outlet6Config.setStatus("mandatory")


class _Pdu05Outlet7Config_Type(DisplayString):
    """Custom type pdu05Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu05Outlet7Config_Type.__name__ = "DisplayString"
_Pdu05Outlet7Config_Object = MibScalar
pdu05Outlet7Config = _Pdu05Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 14, 7),
    _Pdu05Outlet7Config_Type()
)
pdu05Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05Outlet7Config.setStatus("mandatory")


class _Pdu05Outlet8Config_Type(DisplayString):
    """Custom type pdu05Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu05Outlet8Config_Type.__name__ = "DisplayString"
_Pdu05Outlet8Config_Object = MibScalar
pdu05Outlet8Config = _Pdu05Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 14, 8),
    _Pdu05Outlet8Config_Type()
)
pdu05Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05Outlet8Config.setStatus("mandatory")


class _Pdu05Threshold1_Type(Integer32):
    """Custom type pdu05Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu05Threshold1_Type.__name__ = "Integer32"
_Pdu05Threshold1_Object = MibScalar
pdu05Threshold1 = _Pdu05Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 15),
    _Pdu05Threshold1_Type()
)
pdu05Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu05Threshold1.setStatus("mandatory")


class _Pdu05Threshold2_Type(Integer32):
    """Custom type pdu05Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu05Threshold2_Type.__name__ = "Integer32"
_Pdu05Threshold2_Object = MibScalar
pdu05Threshold2 = _Pdu05Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 16),
    _Pdu05Threshold2_Type()
)
pdu05Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu05Threshold2.setStatus("mandatory")


class _Pdu05Voltage_Type(Integer32):
    """Custom type pdu05Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu05Voltage_Type.__name__ = "Integer32"
_Pdu05Voltage_Object = MibScalar
pdu05Voltage = _Pdu05Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 17),
    _Pdu05Voltage_Type()
)
pdu05Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05Voltage.setStatus("mandatory")


class _Pdu05ModelName_Type(DisplayString):
    """Custom type pdu05ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu05ModelName_Type.__name__ = "DisplayString"
_Pdu05ModelName_Object = MibScalar
pdu05ModelName = _Pdu05ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 18),
    _Pdu05ModelName_Type()
)
pdu05ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05ModelName.setStatus("mandatory")


class _Pdu05ModelNo_Type(DisplayString):
    """Custom type pdu05ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu05ModelNo_Type.__name__ = "DisplayString"
_Pdu05ModelNo_Object = MibScalar
pdu05ModelNo = _Pdu05ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 19),
    _Pdu05ModelNo_Type()
)
pdu05ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05ModelNo.setStatus("mandatory")


class _Pdu05Identify_Type(DisplayString):
    """Custom type pdu05Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu05Identify_Type.__name__ = "DisplayString"
_Pdu05Identify_Object = MibScalar
pdu05Identify = _Pdu05Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 5, 20),
    _Pdu05Identify_Type()
)
pdu05Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu05Identify.setStatus("mandatory")
_Pdu06Entry_ObjectIdentity = ObjectIdentity
pdu06Entry = _Pdu06Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6)
)
_Pdu06Value_Type = Integer32
_Pdu06Value_Object = MibScalar
pdu06Value = _Pdu06Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 11),
    _Pdu06Value_Type()
)
pdu06Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06Value.setStatus("mandatory")


class _Pdu06SubValues_Type(DisplayString):
    """Custom type pdu06SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu06SubValues_Type.__name__ = "DisplayString"
_Pdu06SubValues_Object = MibScalar
pdu06SubValues = _Pdu06SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 12),
    _Pdu06SubValues_Type()
)
pdu06SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06SubValues.setStatus("mandatory")


class _Pdu06OutletStatus_Type(DisplayString):
    """Custom type pdu06OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu06OutletStatus_Type.__name__ = "DisplayString"
_Pdu06OutletStatus_Object = MibScalar
pdu06OutletStatus = _Pdu06OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 13),
    _Pdu06OutletStatus_Type()
)
pdu06OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06OutletStatus.setStatus("mandatory")
_Pdu06OutletConfigs_ObjectIdentity = ObjectIdentity
pdu06OutletConfigs = _Pdu06OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 14)
)


class _Pdu06Outlet1Config_Type(DisplayString):
    """Custom type pdu06Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu06Outlet1Config_Type.__name__ = "DisplayString"
_Pdu06Outlet1Config_Object = MibScalar
pdu06Outlet1Config = _Pdu06Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 14, 1),
    _Pdu06Outlet1Config_Type()
)
pdu06Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06Outlet1Config.setStatus("mandatory")


class _Pdu06Outlet2Config_Type(DisplayString):
    """Custom type pdu06Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu06Outlet2Config_Type.__name__ = "DisplayString"
_Pdu06Outlet2Config_Object = MibScalar
pdu06Outlet2Config = _Pdu06Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 14, 2),
    _Pdu06Outlet2Config_Type()
)
pdu06Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06Outlet2Config.setStatus("mandatory")


class _Pdu06Outlet3Config_Type(DisplayString):
    """Custom type pdu06Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu06Outlet3Config_Type.__name__ = "DisplayString"
_Pdu06Outlet3Config_Object = MibScalar
pdu06Outlet3Config = _Pdu06Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 14, 3),
    _Pdu06Outlet3Config_Type()
)
pdu06Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06Outlet3Config.setStatus("mandatory")


class _Pdu06Outlet4Config_Type(DisplayString):
    """Custom type pdu06Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu06Outlet4Config_Type.__name__ = "DisplayString"
_Pdu06Outlet4Config_Object = MibScalar
pdu06Outlet4Config = _Pdu06Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 14, 4),
    _Pdu06Outlet4Config_Type()
)
pdu06Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06Outlet4Config.setStatus("mandatory")


class _Pdu06Outlet5Config_Type(DisplayString):
    """Custom type pdu06Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu06Outlet5Config_Type.__name__ = "DisplayString"
_Pdu06Outlet5Config_Object = MibScalar
pdu06Outlet5Config = _Pdu06Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 14, 5),
    _Pdu06Outlet5Config_Type()
)
pdu06Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06Outlet5Config.setStatus("mandatory")


class _Pdu06Outlet6Config_Type(DisplayString):
    """Custom type pdu06Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu06Outlet6Config_Type.__name__ = "DisplayString"
_Pdu06Outlet6Config_Object = MibScalar
pdu06Outlet6Config = _Pdu06Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 14, 6),
    _Pdu06Outlet6Config_Type()
)
pdu06Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06Outlet6Config.setStatus("mandatory")


class _Pdu06Outlet7Config_Type(DisplayString):
    """Custom type pdu06Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu06Outlet7Config_Type.__name__ = "DisplayString"
_Pdu06Outlet7Config_Object = MibScalar
pdu06Outlet7Config = _Pdu06Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 14, 7),
    _Pdu06Outlet7Config_Type()
)
pdu06Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06Outlet7Config.setStatus("mandatory")


class _Pdu06Outlet8Config_Type(DisplayString):
    """Custom type pdu06Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu06Outlet8Config_Type.__name__ = "DisplayString"
_Pdu06Outlet8Config_Object = MibScalar
pdu06Outlet8Config = _Pdu06Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 14, 8),
    _Pdu06Outlet8Config_Type()
)
pdu06Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06Outlet8Config.setStatus("mandatory")


class _Pdu06Threshold1_Type(Integer32):
    """Custom type pdu06Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu06Threshold1_Type.__name__ = "Integer32"
_Pdu06Threshold1_Object = MibScalar
pdu06Threshold1 = _Pdu06Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 15),
    _Pdu06Threshold1_Type()
)
pdu06Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu06Threshold1.setStatus("mandatory")


class _Pdu06Threshold2_Type(Integer32):
    """Custom type pdu06Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu06Threshold2_Type.__name__ = "Integer32"
_Pdu06Threshold2_Object = MibScalar
pdu06Threshold2 = _Pdu06Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 16),
    _Pdu06Threshold2_Type()
)
pdu06Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu06Threshold2.setStatus("mandatory")


class _Pdu06Voltage_Type(Integer32):
    """Custom type pdu06Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu06Voltage_Type.__name__ = "Integer32"
_Pdu06Voltage_Object = MibScalar
pdu06Voltage = _Pdu06Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 17),
    _Pdu06Voltage_Type()
)
pdu06Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06Voltage.setStatus("mandatory")


class _Pdu06ModelName_Type(DisplayString):
    """Custom type pdu06ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu06ModelName_Type.__name__ = "DisplayString"
_Pdu06ModelName_Object = MibScalar
pdu06ModelName = _Pdu06ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 18),
    _Pdu06ModelName_Type()
)
pdu06ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06ModelName.setStatus("mandatory")


class _Pdu06ModelNo_Type(DisplayString):
    """Custom type pdu06ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu06ModelNo_Type.__name__ = "DisplayString"
_Pdu06ModelNo_Object = MibScalar
pdu06ModelNo = _Pdu06ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 19),
    _Pdu06ModelNo_Type()
)
pdu06ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06ModelNo.setStatus("mandatory")


class _Pdu06Identify_Type(DisplayString):
    """Custom type pdu06Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu06Identify_Type.__name__ = "DisplayString"
_Pdu06Identify_Object = MibScalar
pdu06Identify = _Pdu06Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 6, 20),
    _Pdu06Identify_Type()
)
pdu06Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu06Identify.setStatus("mandatory")
_Pdu07Entry_ObjectIdentity = ObjectIdentity
pdu07Entry = _Pdu07Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7)
)
_Pdu07Value_Type = Integer32
_Pdu07Value_Object = MibScalar
pdu07Value = _Pdu07Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 11),
    _Pdu07Value_Type()
)
pdu07Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07Value.setStatus("mandatory")


class _Pdu07SubValues_Type(DisplayString):
    """Custom type pdu07SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu07SubValues_Type.__name__ = "DisplayString"
_Pdu07SubValues_Object = MibScalar
pdu07SubValues = _Pdu07SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 12),
    _Pdu07SubValues_Type()
)
pdu07SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07SubValues.setStatus("mandatory")


class _Pdu07OutletStatus_Type(DisplayString):
    """Custom type pdu07OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu07OutletStatus_Type.__name__ = "DisplayString"
_Pdu07OutletStatus_Object = MibScalar
pdu07OutletStatus = _Pdu07OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 13),
    _Pdu07OutletStatus_Type()
)
pdu07OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07OutletStatus.setStatus("mandatory")
_Pdu07OutletConfigs_ObjectIdentity = ObjectIdentity
pdu07OutletConfigs = _Pdu07OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 14)
)


class _Pdu07Outlet1Config_Type(DisplayString):
    """Custom type pdu07Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu07Outlet1Config_Type.__name__ = "DisplayString"
_Pdu07Outlet1Config_Object = MibScalar
pdu07Outlet1Config = _Pdu07Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 14, 1),
    _Pdu07Outlet1Config_Type()
)
pdu07Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07Outlet1Config.setStatus("mandatory")


class _Pdu07Outlet2Config_Type(DisplayString):
    """Custom type pdu07Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu07Outlet2Config_Type.__name__ = "DisplayString"
_Pdu07Outlet2Config_Object = MibScalar
pdu07Outlet2Config = _Pdu07Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 14, 2),
    _Pdu07Outlet2Config_Type()
)
pdu07Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07Outlet2Config.setStatus("mandatory")


class _Pdu07Outlet3Config_Type(DisplayString):
    """Custom type pdu07Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu07Outlet3Config_Type.__name__ = "DisplayString"
_Pdu07Outlet3Config_Object = MibScalar
pdu07Outlet3Config = _Pdu07Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 14, 3),
    _Pdu07Outlet3Config_Type()
)
pdu07Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07Outlet3Config.setStatus("mandatory")


class _Pdu07Outlet4Config_Type(DisplayString):
    """Custom type pdu07Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu07Outlet4Config_Type.__name__ = "DisplayString"
_Pdu07Outlet4Config_Object = MibScalar
pdu07Outlet4Config = _Pdu07Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 14, 4),
    _Pdu07Outlet4Config_Type()
)
pdu07Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07Outlet4Config.setStatus("mandatory")


class _Pdu07Outlet5Config_Type(DisplayString):
    """Custom type pdu07Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu07Outlet5Config_Type.__name__ = "DisplayString"
_Pdu07Outlet5Config_Object = MibScalar
pdu07Outlet5Config = _Pdu07Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 14, 5),
    _Pdu07Outlet5Config_Type()
)
pdu07Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07Outlet5Config.setStatus("mandatory")


class _Pdu07Outlet6Config_Type(DisplayString):
    """Custom type pdu07Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu07Outlet6Config_Type.__name__ = "DisplayString"
_Pdu07Outlet6Config_Object = MibScalar
pdu07Outlet6Config = _Pdu07Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 14, 6),
    _Pdu07Outlet6Config_Type()
)
pdu07Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07Outlet6Config.setStatus("mandatory")


class _Pdu07Outlet7Config_Type(DisplayString):
    """Custom type pdu07Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu07Outlet7Config_Type.__name__ = "DisplayString"
_Pdu07Outlet7Config_Object = MibScalar
pdu07Outlet7Config = _Pdu07Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 14, 7),
    _Pdu07Outlet7Config_Type()
)
pdu07Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07Outlet7Config.setStatus("mandatory")


class _Pdu07Outlet8Config_Type(DisplayString):
    """Custom type pdu07Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu07Outlet8Config_Type.__name__ = "DisplayString"
_Pdu07Outlet8Config_Object = MibScalar
pdu07Outlet8Config = _Pdu07Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 14, 8),
    _Pdu07Outlet8Config_Type()
)
pdu07Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07Outlet8Config.setStatus("mandatory")


class _Pdu07Threshold1_Type(Integer32):
    """Custom type pdu07Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu07Threshold1_Type.__name__ = "Integer32"
_Pdu07Threshold1_Object = MibScalar
pdu07Threshold1 = _Pdu07Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 15),
    _Pdu07Threshold1_Type()
)
pdu07Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu07Threshold1.setStatus("mandatory")


class _Pdu07Threshold2_Type(Integer32):
    """Custom type pdu07Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu07Threshold2_Type.__name__ = "Integer32"
_Pdu07Threshold2_Object = MibScalar
pdu07Threshold2 = _Pdu07Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 16),
    _Pdu07Threshold2_Type()
)
pdu07Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu07Threshold2.setStatus("mandatory")


class _Pdu07Voltage_Type(Integer32):
    """Custom type pdu07Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu07Voltage_Type.__name__ = "Integer32"
_Pdu07Voltage_Object = MibScalar
pdu07Voltage = _Pdu07Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 17),
    _Pdu07Voltage_Type()
)
pdu07Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07Voltage.setStatus("mandatory")


class _Pdu07ModelName_Type(DisplayString):
    """Custom type pdu07ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu07ModelName_Type.__name__ = "DisplayString"
_Pdu07ModelName_Object = MibScalar
pdu07ModelName = _Pdu07ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 18),
    _Pdu07ModelName_Type()
)
pdu07ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07ModelName.setStatus("mandatory")


class _Pdu07ModelNo_Type(DisplayString):
    """Custom type pdu07ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu07ModelNo_Type.__name__ = "DisplayString"
_Pdu07ModelNo_Object = MibScalar
pdu07ModelNo = _Pdu07ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 19),
    _Pdu07ModelNo_Type()
)
pdu07ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07ModelNo.setStatus("mandatory")


class _Pdu07Identify_Type(DisplayString):
    """Custom type pdu07Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu07Identify_Type.__name__ = "DisplayString"
_Pdu07Identify_Object = MibScalar
pdu07Identify = _Pdu07Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 7, 20),
    _Pdu07Identify_Type()
)
pdu07Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu07Identify.setStatus("mandatory")
_Pdu08Entry_ObjectIdentity = ObjectIdentity
pdu08Entry = _Pdu08Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8)
)
_Pdu08Value_Type = Integer32
_Pdu08Value_Object = MibScalar
pdu08Value = _Pdu08Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 11),
    _Pdu08Value_Type()
)
pdu08Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08Value.setStatus("mandatory")


class _Pdu08SubValues_Type(DisplayString):
    """Custom type pdu08SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu08SubValues_Type.__name__ = "DisplayString"
_Pdu08SubValues_Object = MibScalar
pdu08SubValues = _Pdu08SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 12),
    _Pdu08SubValues_Type()
)
pdu08SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08SubValues.setStatus("mandatory")


class _Pdu08OutletStatus_Type(DisplayString):
    """Custom type pdu08OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu08OutletStatus_Type.__name__ = "DisplayString"
_Pdu08OutletStatus_Object = MibScalar
pdu08OutletStatus = _Pdu08OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 13),
    _Pdu08OutletStatus_Type()
)
pdu08OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08OutletStatus.setStatus("mandatory")
_Pdu08OutletConfigs_ObjectIdentity = ObjectIdentity
pdu08OutletConfigs = _Pdu08OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 14)
)


class _Pdu08Outlet1Config_Type(DisplayString):
    """Custom type pdu08Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu08Outlet1Config_Type.__name__ = "DisplayString"
_Pdu08Outlet1Config_Object = MibScalar
pdu08Outlet1Config = _Pdu08Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 14, 1),
    _Pdu08Outlet1Config_Type()
)
pdu08Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08Outlet1Config.setStatus("mandatory")


class _Pdu08Outlet2Config_Type(DisplayString):
    """Custom type pdu08Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu08Outlet2Config_Type.__name__ = "DisplayString"
_Pdu08Outlet2Config_Object = MibScalar
pdu08Outlet2Config = _Pdu08Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 14, 2),
    _Pdu08Outlet2Config_Type()
)
pdu08Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08Outlet2Config.setStatus("mandatory")


class _Pdu08Outlet3Config_Type(DisplayString):
    """Custom type pdu08Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu08Outlet3Config_Type.__name__ = "DisplayString"
_Pdu08Outlet3Config_Object = MibScalar
pdu08Outlet3Config = _Pdu08Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 14, 3),
    _Pdu08Outlet3Config_Type()
)
pdu08Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08Outlet3Config.setStatus("mandatory")


class _Pdu08Outlet4Config_Type(DisplayString):
    """Custom type pdu08Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu08Outlet4Config_Type.__name__ = "DisplayString"
_Pdu08Outlet4Config_Object = MibScalar
pdu08Outlet4Config = _Pdu08Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 14, 4),
    _Pdu08Outlet4Config_Type()
)
pdu08Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08Outlet4Config.setStatus("mandatory")


class _Pdu08Outlet5Config_Type(DisplayString):
    """Custom type pdu08Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu08Outlet5Config_Type.__name__ = "DisplayString"
_Pdu08Outlet5Config_Object = MibScalar
pdu08Outlet5Config = _Pdu08Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 14, 5),
    _Pdu08Outlet5Config_Type()
)
pdu08Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08Outlet5Config.setStatus("mandatory")


class _Pdu08Outlet6Config_Type(DisplayString):
    """Custom type pdu08Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu08Outlet6Config_Type.__name__ = "DisplayString"
_Pdu08Outlet6Config_Object = MibScalar
pdu08Outlet6Config = _Pdu08Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 14, 6),
    _Pdu08Outlet6Config_Type()
)
pdu08Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08Outlet6Config.setStatus("mandatory")


class _Pdu08Outlet7Config_Type(DisplayString):
    """Custom type pdu08Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu08Outlet7Config_Type.__name__ = "DisplayString"
_Pdu08Outlet7Config_Object = MibScalar
pdu08Outlet7Config = _Pdu08Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 14, 7),
    _Pdu08Outlet7Config_Type()
)
pdu08Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08Outlet7Config.setStatus("mandatory")


class _Pdu08Outlet8Config_Type(DisplayString):
    """Custom type pdu08Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu08Outlet8Config_Type.__name__ = "DisplayString"
_Pdu08Outlet8Config_Object = MibScalar
pdu08Outlet8Config = _Pdu08Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 14, 8),
    _Pdu08Outlet8Config_Type()
)
pdu08Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08Outlet8Config.setStatus("mandatory")


class _Pdu08Threshold1_Type(Integer32):
    """Custom type pdu08Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu08Threshold1_Type.__name__ = "Integer32"
_Pdu08Threshold1_Object = MibScalar
pdu08Threshold1 = _Pdu08Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 15),
    _Pdu08Threshold1_Type()
)
pdu08Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu08Threshold1.setStatus("mandatory")


class _Pdu08Threshold2_Type(Integer32):
    """Custom type pdu08Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu08Threshold2_Type.__name__ = "Integer32"
_Pdu08Threshold2_Object = MibScalar
pdu08Threshold2 = _Pdu08Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 16),
    _Pdu08Threshold2_Type()
)
pdu08Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu08Threshold2.setStatus("mandatory")


class _Pdu08Voltage_Type(Integer32):
    """Custom type pdu08Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu08Voltage_Type.__name__ = "Integer32"
_Pdu08Voltage_Object = MibScalar
pdu08Voltage = _Pdu08Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 17),
    _Pdu08Voltage_Type()
)
pdu08Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08Voltage.setStatus("mandatory")


class _Pdu08ModelName_Type(DisplayString):
    """Custom type pdu08ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu08ModelName_Type.__name__ = "DisplayString"
_Pdu08ModelName_Object = MibScalar
pdu08ModelName = _Pdu08ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 18),
    _Pdu08ModelName_Type()
)
pdu08ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08ModelName.setStatus("mandatory")


class _Pdu08ModelNo_Type(DisplayString):
    """Custom type pdu08ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu08ModelNo_Type.__name__ = "DisplayString"
_Pdu08ModelNo_Object = MibScalar
pdu08ModelNo = _Pdu08ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 19),
    _Pdu08ModelNo_Type()
)
pdu08ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08ModelNo.setStatus("mandatory")


class _Pdu08Identify_Type(DisplayString):
    """Custom type pdu08Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu08Identify_Type.__name__ = "DisplayString"
_Pdu08Identify_Object = MibScalar
pdu08Identify = _Pdu08Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 8, 20),
    _Pdu08Identify_Type()
)
pdu08Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu08Identify.setStatus("mandatory")
_Pdu09Entry_ObjectIdentity = ObjectIdentity
pdu09Entry = _Pdu09Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9)
)
_Pdu09Value_Type = Integer32
_Pdu09Value_Object = MibScalar
pdu09Value = _Pdu09Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 11),
    _Pdu09Value_Type()
)
pdu09Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09Value.setStatus("mandatory")


class _Pdu09SubValues_Type(DisplayString):
    """Custom type pdu09SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu09SubValues_Type.__name__ = "DisplayString"
_Pdu09SubValues_Object = MibScalar
pdu09SubValues = _Pdu09SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 12),
    _Pdu09SubValues_Type()
)
pdu09SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09SubValues.setStatus("mandatory")


class _Pdu09OutletStatus_Type(DisplayString):
    """Custom type pdu09OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu09OutletStatus_Type.__name__ = "DisplayString"
_Pdu09OutletStatus_Object = MibScalar
pdu09OutletStatus = _Pdu09OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 13),
    _Pdu09OutletStatus_Type()
)
pdu09OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09OutletStatus.setStatus("mandatory")
_Pdu09OutletConfigs_ObjectIdentity = ObjectIdentity
pdu09OutletConfigs = _Pdu09OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 14)
)


class _Pdu09Outlet1Config_Type(DisplayString):
    """Custom type pdu09Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu09Outlet1Config_Type.__name__ = "DisplayString"
_Pdu09Outlet1Config_Object = MibScalar
pdu09Outlet1Config = _Pdu09Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 14, 1),
    _Pdu09Outlet1Config_Type()
)
pdu09Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09Outlet1Config.setStatus("mandatory")


class _Pdu09Outlet2Config_Type(DisplayString):
    """Custom type pdu09Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu09Outlet2Config_Type.__name__ = "DisplayString"
_Pdu09Outlet2Config_Object = MibScalar
pdu09Outlet2Config = _Pdu09Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 14, 2),
    _Pdu09Outlet2Config_Type()
)
pdu09Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09Outlet2Config.setStatus("mandatory")


class _Pdu09Outlet3Config_Type(DisplayString):
    """Custom type pdu09Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu09Outlet3Config_Type.__name__ = "DisplayString"
_Pdu09Outlet3Config_Object = MibScalar
pdu09Outlet3Config = _Pdu09Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 14, 3),
    _Pdu09Outlet3Config_Type()
)
pdu09Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09Outlet3Config.setStatus("mandatory")


class _Pdu09Outlet4Config_Type(DisplayString):
    """Custom type pdu09Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu09Outlet4Config_Type.__name__ = "DisplayString"
_Pdu09Outlet4Config_Object = MibScalar
pdu09Outlet4Config = _Pdu09Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 14, 4),
    _Pdu09Outlet4Config_Type()
)
pdu09Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09Outlet4Config.setStatus("mandatory")


class _Pdu09Outlet5Config_Type(DisplayString):
    """Custom type pdu09Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu09Outlet5Config_Type.__name__ = "DisplayString"
_Pdu09Outlet5Config_Object = MibScalar
pdu09Outlet5Config = _Pdu09Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 14, 5),
    _Pdu09Outlet5Config_Type()
)
pdu09Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09Outlet5Config.setStatus("mandatory")


class _Pdu09Outlet6Config_Type(DisplayString):
    """Custom type pdu09Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu09Outlet6Config_Type.__name__ = "DisplayString"
_Pdu09Outlet6Config_Object = MibScalar
pdu09Outlet6Config = _Pdu09Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 14, 6),
    _Pdu09Outlet6Config_Type()
)
pdu09Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09Outlet6Config.setStatus("mandatory")


class _Pdu09Outlet7Config_Type(DisplayString):
    """Custom type pdu09Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu09Outlet7Config_Type.__name__ = "DisplayString"
_Pdu09Outlet7Config_Object = MibScalar
pdu09Outlet7Config = _Pdu09Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 14, 7),
    _Pdu09Outlet7Config_Type()
)
pdu09Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09Outlet7Config.setStatus("mandatory")


class _Pdu09Outlet8Config_Type(DisplayString):
    """Custom type pdu09Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu09Outlet8Config_Type.__name__ = "DisplayString"
_Pdu09Outlet8Config_Object = MibScalar
pdu09Outlet8Config = _Pdu09Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 14, 8),
    _Pdu09Outlet8Config_Type()
)
pdu09Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09Outlet8Config.setStatus("mandatory")


class _Pdu09Threshold1_Type(Integer32):
    """Custom type pdu09Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu09Threshold1_Type.__name__ = "Integer32"
_Pdu09Threshold1_Object = MibScalar
pdu09Threshold1 = _Pdu09Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 15),
    _Pdu09Threshold1_Type()
)
pdu09Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu09Threshold1.setStatus("mandatory")


class _Pdu09Threshold2_Type(Integer32):
    """Custom type pdu09Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu09Threshold2_Type.__name__ = "Integer32"
_Pdu09Threshold2_Object = MibScalar
pdu09Threshold2 = _Pdu09Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 16),
    _Pdu09Threshold2_Type()
)
pdu09Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu09Threshold2.setStatus("mandatory")


class _Pdu09Voltage_Type(Integer32):
    """Custom type pdu09Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu09Voltage_Type.__name__ = "Integer32"
_Pdu09Voltage_Object = MibScalar
pdu09Voltage = _Pdu09Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 17),
    _Pdu09Voltage_Type()
)
pdu09Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09Voltage.setStatus("mandatory")


class _Pdu09ModelName_Type(DisplayString):
    """Custom type pdu09ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu09ModelName_Type.__name__ = "DisplayString"
_Pdu09ModelName_Object = MibScalar
pdu09ModelName = _Pdu09ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 18),
    _Pdu09ModelName_Type()
)
pdu09ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09ModelName.setStatus("mandatory")


class _Pdu09ModelNo_Type(DisplayString):
    """Custom type pdu09ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu09ModelNo_Type.__name__ = "DisplayString"
_Pdu09ModelNo_Object = MibScalar
pdu09ModelNo = _Pdu09ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 19),
    _Pdu09ModelNo_Type()
)
pdu09ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09ModelNo.setStatus("mandatory")


class _Pdu09Identify_Type(DisplayString):
    """Custom type pdu09Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu09Identify_Type.__name__ = "DisplayString"
_Pdu09Identify_Object = MibScalar
pdu09Identify = _Pdu09Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 9, 20),
    _Pdu09Identify_Type()
)
pdu09Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu09Identify.setStatus("mandatory")
_Pdu10Entry_ObjectIdentity = ObjectIdentity
pdu10Entry = _Pdu10Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10)
)
_Pdu10Value_Type = Integer32
_Pdu10Value_Object = MibScalar
pdu10Value = _Pdu10Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 11),
    _Pdu10Value_Type()
)
pdu10Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10Value.setStatus("mandatory")


class _Pdu10SubValues_Type(DisplayString):
    """Custom type pdu10SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu10SubValues_Type.__name__ = "DisplayString"
_Pdu10SubValues_Object = MibScalar
pdu10SubValues = _Pdu10SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 12),
    _Pdu10SubValues_Type()
)
pdu10SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10SubValues.setStatus("mandatory")


class _Pdu10OutletStatus_Type(DisplayString):
    """Custom type pdu10OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu10OutletStatus_Type.__name__ = "DisplayString"
_Pdu10OutletStatus_Object = MibScalar
pdu10OutletStatus = _Pdu10OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 13),
    _Pdu10OutletStatus_Type()
)
pdu10OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10OutletStatus.setStatus("mandatory")
_Pdu10OutletConfigs_ObjectIdentity = ObjectIdentity
pdu10OutletConfigs = _Pdu10OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 14)
)


class _Pdu10Outlet1Config_Type(DisplayString):
    """Custom type pdu10Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu10Outlet1Config_Type.__name__ = "DisplayString"
_Pdu10Outlet1Config_Object = MibScalar
pdu10Outlet1Config = _Pdu10Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 14, 1),
    _Pdu10Outlet1Config_Type()
)
pdu10Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10Outlet1Config.setStatus("mandatory")


class _Pdu10Outlet2Config_Type(DisplayString):
    """Custom type pdu10Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu10Outlet2Config_Type.__name__ = "DisplayString"
_Pdu10Outlet2Config_Object = MibScalar
pdu10Outlet2Config = _Pdu10Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 14, 2),
    _Pdu10Outlet2Config_Type()
)
pdu10Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10Outlet2Config.setStatus("mandatory")


class _Pdu10Outlet3Config_Type(DisplayString):
    """Custom type pdu10Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu10Outlet3Config_Type.__name__ = "DisplayString"
_Pdu10Outlet3Config_Object = MibScalar
pdu10Outlet3Config = _Pdu10Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 14, 3),
    _Pdu10Outlet3Config_Type()
)
pdu10Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10Outlet3Config.setStatus("mandatory")


class _Pdu10Outlet4Config_Type(DisplayString):
    """Custom type pdu10Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu10Outlet4Config_Type.__name__ = "DisplayString"
_Pdu10Outlet4Config_Object = MibScalar
pdu10Outlet4Config = _Pdu10Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 14, 4),
    _Pdu10Outlet4Config_Type()
)
pdu10Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10Outlet4Config.setStatus("mandatory")


class _Pdu10Outlet5Config_Type(DisplayString):
    """Custom type pdu10Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu10Outlet5Config_Type.__name__ = "DisplayString"
_Pdu10Outlet5Config_Object = MibScalar
pdu10Outlet5Config = _Pdu10Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 14, 5),
    _Pdu10Outlet5Config_Type()
)
pdu10Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10Outlet5Config.setStatus("mandatory")


class _Pdu10Outlet6Config_Type(DisplayString):
    """Custom type pdu10Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu10Outlet6Config_Type.__name__ = "DisplayString"
_Pdu10Outlet6Config_Object = MibScalar
pdu10Outlet6Config = _Pdu10Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 14, 6),
    _Pdu10Outlet6Config_Type()
)
pdu10Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10Outlet6Config.setStatus("mandatory")


class _Pdu10Outlet7Config_Type(DisplayString):
    """Custom type pdu10Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu10Outlet7Config_Type.__name__ = "DisplayString"
_Pdu10Outlet7Config_Object = MibScalar
pdu10Outlet7Config = _Pdu10Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 14, 7),
    _Pdu10Outlet7Config_Type()
)
pdu10Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10Outlet7Config.setStatus("mandatory")


class _Pdu10Outlet8Config_Type(DisplayString):
    """Custom type pdu10Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu10Outlet8Config_Type.__name__ = "DisplayString"
_Pdu10Outlet8Config_Object = MibScalar
pdu10Outlet8Config = _Pdu10Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 14, 8),
    _Pdu10Outlet8Config_Type()
)
pdu10Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10Outlet8Config.setStatus("mandatory")


class _Pdu10Threshold1_Type(Integer32):
    """Custom type pdu10Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu10Threshold1_Type.__name__ = "Integer32"
_Pdu10Threshold1_Object = MibScalar
pdu10Threshold1 = _Pdu10Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 15),
    _Pdu10Threshold1_Type()
)
pdu10Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu10Threshold1.setStatus("mandatory")


class _Pdu10Threshold2_Type(Integer32):
    """Custom type pdu10Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu10Threshold2_Type.__name__ = "Integer32"
_Pdu10Threshold2_Object = MibScalar
pdu10Threshold2 = _Pdu10Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 16),
    _Pdu10Threshold2_Type()
)
pdu10Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu10Threshold2.setStatus("mandatory")


class _Pdu10Voltage_Type(Integer32):
    """Custom type pdu10Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu10Voltage_Type.__name__ = "Integer32"
_Pdu10Voltage_Object = MibScalar
pdu10Voltage = _Pdu10Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 17),
    _Pdu10Voltage_Type()
)
pdu10Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10Voltage.setStatus("mandatory")


class _Pdu10ModelName_Type(DisplayString):
    """Custom type pdu10ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu10ModelName_Type.__name__ = "DisplayString"
_Pdu10ModelName_Object = MibScalar
pdu10ModelName = _Pdu10ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 18),
    _Pdu10ModelName_Type()
)
pdu10ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10ModelName.setStatus("mandatory")


class _Pdu10ModelNo_Type(DisplayString):
    """Custom type pdu10ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu10ModelNo_Type.__name__ = "DisplayString"
_Pdu10ModelNo_Object = MibScalar
pdu10ModelNo = _Pdu10ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 19),
    _Pdu10ModelNo_Type()
)
pdu10ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10ModelNo.setStatus("mandatory")


class _Pdu10Identify_Type(DisplayString):
    """Custom type pdu10Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu10Identify_Type.__name__ = "DisplayString"
_Pdu10Identify_Object = MibScalar
pdu10Identify = _Pdu10Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 10, 20),
    _Pdu10Identify_Type()
)
pdu10Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu10Identify.setStatus("mandatory")
_Pdu11Entry_ObjectIdentity = ObjectIdentity
pdu11Entry = _Pdu11Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11)
)
_Pdu11Value_Type = Integer32
_Pdu11Value_Object = MibScalar
pdu11Value = _Pdu11Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 11),
    _Pdu11Value_Type()
)
pdu11Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11Value.setStatus("mandatory")


class _Pdu11SubValues_Type(DisplayString):
    """Custom type pdu11SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu11SubValues_Type.__name__ = "DisplayString"
_Pdu11SubValues_Object = MibScalar
pdu11SubValues = _Pdu11SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 12),
    _Pdu11SubValues_Type()
)
pdu11SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11SubValues.setStatus("mandatory")


class _Pdu11OutletStatus_Type(DisplayString):
    """Custom type pdu11OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu11OutletStatus_Type.__name__ = "DisplayString"
_Pdu11OutletStatus_Object = MibScalar
pdu11OutletStatus = _Pdu11OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 13),
    _Pdu11OutletStatus_Type()
)
pdu11OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11OutletStatus.setStatus("mandatory")
_Pdu11OutletConfigs_ObjectIdentity = ObjectIdentity
pdu11OutletConfigs = _Pdu11OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 14)
)


class _Pdu11Outlet1Config_Type(DisplayString):
    """Custom type pdu11Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu11Outlet1Config_Type.__name__ = "DisplayString"
_Pdu11Outlet1Config_Object = MibScalar
pdu11Outlet1Config = _Pdu11Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 14, 1),
    _Pdu11Outlet1Config_Type()
)
pdu11Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11Outlet1Config.setStatus("mandatory")


class _Pdu11Outlet2Config_Type(DisplayString):
    """Custom type pdu11Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu11Outlet2Config_Type.__name__ = "DisplayString"
_Pdu11Outlet2Config_Object = MibScalar
pdu11Outlet2Config = _Pdu11Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 14, 2),
    _Pdu11Outlet2Config_Type()
)
pdu11Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11Outlet2Config.setStatus("mandatory")


class _Pdu11Outlet3Config_Type(DisplayString):
    """Custom type pdu11Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu11Outlet3Config_Type.__name__ = "DisplayString"
_Pdu11Outlet3Config_Object = MibScalar
pdu11Outlet3Config = _Pdu11Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 14, 3),
    _Pdu11Outlet3Config_Type()
)
pdu11Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11Outlet3Config.setStatus("mandatory")


class _Pdu11Outlet4Config_Type(DisplayString):
    """Custom type pdu11Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu11Outlet4Config_Type.__name__ = "DisplayString"
_Pdu11Outlet4Config_Object = MibScalar
pdu11Outlet4Config = _Pdu11Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 14, 4),
    _Pdu11Outlet4Config_Type()
)
pdu11Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11Outlet4Config.setStatus("mandatory")


class _Pdu11Outlet5Config_Type(DisplayString):
    """Custom type pdu11Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu11Outlet5Config_Type.__name__ = "DisplayString"
_Pdu11Outlet5Config_Object = MibScalar
pdu11Outlet5Config = _Pdu11Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 14, 5),
    _Pdu11Outlet5Config_Type()
)
pdu11Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11Outlet5Config.setStatus("mandatory")


class _Pdu11Outlet6Config_Type(DisplayString):
    """Custom type pdu11Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu11Outlet6Config_Type.__name__ = "DisplayString"
_Pdu11Outlet6Config_Object = MibScalar
pdu11Outlet6Config = _Pdu11Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 14, 6),
    _Pdu11Outlet6Config_Type()
)
pdu11Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11Outlet6Config.setStatus("mandatory")


class _Pdu11Outlet7Config_Type(DisplayString):
    """Custom type pdu11Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu11Outlet7Config_Type.__name__ = "DisplayString"
_Pdu11Outlet7Config_Object = MibScalar
pdu11Outlet7Config = _Pdu11Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 14, 7),
    _Pdu11Outlet7Config_Type()
)
pdu11Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11Outlet7Config.setStatus("mandatory")


class _Pdu11Outlet8Config_Type(DisplayString):
    """Custom type pdu11Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu11Outlet8Config_Type.__name__ = "DisplayString"
_Pdu11Outlet8Config_Object = MibScalar
pdu11Outlet8Config = _Pdu11Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 14, 8),
    _Pdu11Outlet8Config_Type()
)
pdu11Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11Outlet8Config.setStatus("mandatory")


class _Pdu11Threshold1_Type(Integer32):
    """Custom type pdu11Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu11Threshold1_Type.__name__ = "Integer32"
_Pdu11Threshold1_Object = MibScalar
pdu11Threshold1 = _Pdu11Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 15),
    _Pdu11Threshold1_Type()
)
pdu11Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu11Threshold1.setStatus("mandatory")


class _Pdu11Threshold2_Type(Integer32):
    """Custom type pdu11Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu11Threshold2_Type.__name__ = "Integer32"
_Pdu11Threshold2_Object = MibScalar
pdu11Threshold2 = _Pdu11Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 16),
    _Pdu11Threshold2_Type()
)
pdu11Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu11Threshold2.setStatus("mandatory")


class _Pdu11Voltage_Type(Integer32):
    """Custom type pdu11Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu11Voltage_Type.__name__ = "Integer32"
_Pdu11Voltage_Object = MibScalar
pdu11Voltage = _Pdu11Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 17),
    _Pdu11Voltage_Type()
)
pdu11Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11Voltage.setStatus("mandatory")


class _Pdu11ModelName_Type(DisplayString):
    """Custom type pdu11ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu11ModelName_Type.__name__ = "DisplayString"
_Pdu11ModelName_Object = MibScalar
pdu11ModelName = _Pdu11ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 18),
    _Pdu11ModelName_Type()
)
pdu11ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11ModelName.setStatus("mandatory")


class _Pdu11ModelNo_Type(DisplayString):
    """Custom type pdu11ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu11ModelNo_Type.__name__ = "DisplayString"
_Pdu11ModelNo_Object = MibScalar
pdu11ModelNo = _Pdu11ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 19),
    _Pdu11ModelNo_Type()
)
pdu11ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11ModelNo.setStatus("mandatory")


class _Pdu11Identify_Type(DisplayString):
    """Custom type pdu11Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu11Identify_Type.__name__ = "DisplayString"
_Pdu11Identify_Object = MibScalar
pdu11Identify = _Pdu11Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 11, 20),
    _Pdu11Identify_Type()
)
pdu11Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu11Identify.setStatus("mandatory")
_Pdu12Entry_ObjectIdentity = ObjectIdentity
pdu12Entry = _Pdu12Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12)
)
_Pdu12Value_Type = Integer32
_Pdu12Value_Object = MibScalar
pdu12Value = _Pdu12Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 11),
    _Pdu12Value_Type()
)
pdu12Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12Value.setStatus("mandatory")


class _Pdu12SubValues_Type(DisplayString):
    """Custom type pdu12SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu12SubValues_Type.__name__ = "DisplayString"
_Pdu12SubValues_Object = MibScalar
pdu12SubValues = _Pdu12SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 12),
    _Pdu12SubValues_Type()
)
pdu12SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12SubValues.setStatus("mandatory")


class _Pdu12OutletStatus_Type(DisplayString):
    """Custom type pdu12OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu12OutletStatus_Type.__name__ = "DisplayString"
_Pdu12OutletStatus_Object = MibScalar
pdu12OutletStatus = _Pdu12OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 13),
    _Pdu12OutletStatus_Type()
)
pdu12OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12OutletStatus.setStatus("mandatory")
_Pdu12OutletConfigs_ObjectIdentity = ObjectIdentity
pdu12OutletConfigs = _Pdu12OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 14)
)


class _Pdu12Outlet1Config_Type(DisplayString):
    """Custom type pdu12Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu12Outlet1Config_Type.__name__ = "DisplayString"
_Pdu12Outlet1Config_Object = MibScalar
pdu12Outlet1Config = _Pdu12Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 14, 1),
    _Pdu12Outlet1Config_Type()
)
pdu12Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12Outlet1Config.setStatus("mandatory")


class _Pdu12Outlet2Config_Type(DisplayString):
    """Custom type pdu12Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu12Outlet2Config_Type.__name__ = "DisplayString"
_Pdu12Outlet2Config_Object = MibScalar
pdu12Outlet2Config = _Pdu12Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 14, 2),
    _Pdu12Outlet2Config_Type()
)
pdu12Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12Outlet2Config.setStatus("mandatory")


class _Pdu12Outlet3Config_Type(DisplayString):
    """Custom type pdu12Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu12Outlet3Config_Type.__name__ = "DisplayString"
_Pdu12Outlet3Config_Object = MibScalar
pdu12Outlet3Config = _Pdu12Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 14, 3),
    _Pdu12Outlet3Config_Type()
)
pdu12Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12Outlet3Config.setStatus("mandatory")


class _Pdu12Outlet4Config_Type(DisplayString):
    """Custom type pdu12Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu12Outlet4Config_Type.__name__ = "DisplayString"
_Pdu12Outlet4Config_Object = MibScalar
pdu12Outlet4Config = _Pdu12Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 14, 4),
    _Pdu12Outlet4Config_Type()
)
pdu12Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12Outlet4Config.setStatus("mandatory")


class _Pdu12Outlet5Config_Type(DisplayString):
    """Custom type pdu12Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu12Outlet5Config_Type.__name__ = "DisplayString"
_Pdu12Outlet5Config_Object = MibScalar
pdu12Outlet5Config = _Pdu12Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 14, 5),
    _Pdu12Outlet5Config_Type()
)
pdu12Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12Outlet5Config.setStatus("mandatory")


class _Pdu12Outlet6Config_Type(DisplayString):
    """Custom type pdu12Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu12Outlet6Config_Type.__name__ = "DisplayString"
_Pdu12Outlet6Config_Object = MibScalar
pdu12Outlet6Config = _Pdu12Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 14, 6),
    _Pdu12Outlet6Config_Type()
)
pdu12Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12Outlet6Config.setStatus("mandatory")


class _Pdu12Outlet7Config_Type(DisplayString):
    """Custom type pdu12Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu12Outlet7Config_Type.__name__ = "DisplayString"
_Pdu12Outlet7Config_Object = MibScalar
pdu12Outlet7Config = _Pdu12Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 14, 7),
    _Pdu12Outlet7Config_Type()
)
pdu12Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12Outlet7Config.setStatus("mandatory")


class _Pdu12Outlet8Config_Type(DisplayString):
    """Custom type pdu12Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu12Outlet8Config_Type.__name__ = "DisplayString"
_Pdu12Outlet8Config_Object = MibScalar
pdu12Outlet8Config = _Pdu12Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 14, 8),
    _Pdu12Outlet8Config_Type()
)
pdu12Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12Outlet8Config.setStatus("mandatory")


class _Pdu12Threshold1_Type(Integer32):
    """Custom type pdu12Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu12Threshold1_Type.__name__ = "Integer32"
_Pdu12Threshold1_Object = MibScalar
pdu12Threshold1 = _Pdu12Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 15),
    _Pdu12Threshold1_Type()
)
pdu12Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu12Threshold1.setStatus("mandatory")


class _Pdu12Threshold2_Type(Integer32):
    """Custom type pdu12Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu12Threshold2_Type.__name__ = "Integer32"
_Pdu12Threshold2_Object = MibScalar
pdu12Threshold2 = _Pdu12Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 16),
    _Pdu12Threshold2_Type()
)
pdu12Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu12Threshold2.setStatus("mandatory")


class _Pdu12Voltage_Type(Integer32):
    """Custom type pdu12Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu12Voltage_Type.__name__ = "Integer32"
_Pdu12Voltage_Object = MibScalar
pdu12Voltage = _Pdu12Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 17),
    _Pdu12Voltage_Type()
)
pdu12Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12Voltage.setStatus("mandatory")


class _Pdu12ModelName_Type(DisplayString):
    """Custom type pdu12ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu12ModelName_Type.__name__ = "DisplayString"
_Pdu12ModelName_Object = MibScalar
pdu12ModelName = _Pdu12ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 18),
    _Pdu12ModelName_Type()
)
pdu12ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12ModelName.setStatus("mandatory")


class _Pdu12ModelNo_Type(DisplayString):
    """Custom type pdu12ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu12ModelNo_Type.__name__ = "DisplayString"
_Pdu12ModelNo_Object = MibScalar
pdu12ModelNo = _Pdu12ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 19),
    _Pdu12ModelNo_Type()
)
pdu12ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12ModelNo.setStatus("mandatory")


class _Pdu12Identify_Type(DisplayString):
    """Custom type pdu12Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu12Identify_Type.__name__ = "DisplayString"
_Pdu12Identify_Object = MibScalar
pdu12Identify = _Pdu12Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 12, 20),
    _Pdu12Identify_Type()
)
pdu12Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu12Identify.setStatus("mandatory")
_Pdu13Entry_ObjectIdentity = ObjectIdentity
pdu13Entry = _Pdu13Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13)
)
_Pdu13Value_Type = Integer32
_Pdu13Value_Object = MibScalar
pdu13Value = _Pdu13Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 11),
    _Pdu13Value_Type()
)
pdu13Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13Value.setStatus("mandatory")


class _Pdu13SubValues_Type(DisplayString):
    """Custom type pdu13SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu13SubValues_Type.__name__ = "DisplayString"
_Pdu13SubValues_Object = MibScalar
pdu13SubValues = _Pdu13SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 12),
    _Pdu13SubValues_Type()
)
pdu13SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13SubValues.setStatus("mandatory")


class _Pdu13OutletStatus_Type(DisplayString):
    """Custom type pdu13OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu13OutletStatus_Type.__name__ = "DisplayString"
_Pdu13OutletStatus_Object = MibScalar
pdu13OutletStatus = _Pdu13OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 13),
    _Pdu13OutletStatus_Type()
)
pdu13OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13OutletStatus.setStatus("mandatory")
_Pdu13OutletConfigs_ObjectIdentity = ObjectIdentity
pdu13OutletConfigs = _Pdu13OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 14)
)


class _Pdu13Outlet1Config_Type(DisplayString):
    """Custom type pdu13Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu13Outlet1Config_Type.__name__ = "DisplayString"
_Pdu13Outlet1Config_Object = MibScalar
pdu13Outlet1Config = _Pdu13Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 14, 1),
    _Pdu13Outlet1Config_Type()
)
pdu13Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13Outlet1Config.setStatus("mandatory")


class _Pdu13Outlet2Config_Type(DisplayString):
    """Custom type pdu13Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu13Outlet2Config_Type.__name__ = "DisplayString"
_Pdu13Outlet2Config_Object = MibScalar
pdu13Outlet2Config = _Pdu13Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 14, 2),
    _Pdu13Outlet2Config_Type()
)
pdu13Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13Outlet2Config.setStatus("mandatory")


class _Pdu13Outlet3Config_Type(DisplayString):
    """Custom type pdu13Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu13Outlet3Config_Type.__name__ = "DisplayString"
_Pdu13Outlet3Config_Object = MibScalar
pdu13Outlet3Config = _Pdu13Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 14, 3),
    _Pdu13Outlet3Config_Type()
)
pdu13Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13Outlet3Config.setStatus("mandatory")


class _Pdu13Outlet4Config_Type(DisplayString):
    """Custom type pdu13Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu13Outlet4Config_Type.__name__ = "DisplayString"
_Pdu13Outlet4Config_Object = MibScalar
pdu13Outlet4Config = _Pdu13Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 14, 4),
    _Pdu13Outlet4Config_Type()
)
pdu13Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13Outlet4Config.setStatus("mandatory")


class _Pdu13Outlet5Config_Type(DisplayString):
    """Custom type pdu13Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu13Outlet5Config_Type.__name__ = "DisplayString"
_Pdu13Outlet5Config_Object = MibScalar
pdu13Outlet5Config = _Pdu13Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 14, 5),
    _Pdu13Outlet5Config_Type()
)
pdu13Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13Outlet5Config.setStatus("mandatory")


class _Pdu13Outlet6Config_Type(DisplayString):
    """Custom type pdu13Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu13Outlet6Config_Type.__name__ = "DisplayString"
_Pdu13Outlet6Config_Object = MibScalar
pdu13Outlet6Config = _Pdu13Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 14, 6),
    _Pdu13Outlet6Config_Type()
)
pdu13Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13Outlet6Config.setStatus("mandatory")


class _Pdu13Outlet7Config_Type(DisplayString):
    """Custom type pdu13Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu13Outlet7Config_Type.__name__ = "DisplayString"
_Pdu13Outlet7Config_Object = MibScalar
pdu13Outlet7Config = _Pdu13Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 14, 7),
    _Pdu13Outlet7Config_Type()
)
pdu13Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13Outlet7Config.setStatus("mandatory")


class _Pdu13Outlet8Config_Type(DisplayString):
    """Custom type pdu13Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu13Outlet8Config_Type.__name__ = "DisplayString"
_Pdu13Outlet8Config_Object = MibScalar
pdu13Outlet8Config = _Pdu13Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 14, 8),
    _Pdu13Outlet8Config_Type()
)
pdu13Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13Outlet8Config.setStatus("mandatory")


class _Pdu13Threshold1_Type(Integer32):
    """Custom type pdu13Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu13Threshold1_Type.__name__ = "Integer32"
_Pdu13Threshold1_Object = MibScalar
pdu13Threshold1 = _Pdu13Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 15),
    _Pdu13Threshold1_Type()
)
pdu13Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu13Threshold1.setStatus("mandatory")


class _Pdu13Threshold2_Type(Integer32):
    """Custom type pdu13Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu13Threshold2_Type.__name__ = "Integer32"
_Pdu13Threshold2_Object = MibScalar
pdu13Threshold2 = _Pdu13Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 16),
    _Pdu13Threshold2_Type()
)
pdu13Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu13Threshold2.setStatus("mandatory")


class _Pdu13Voltage_Type(Integer32):
    """Custom type pdu13Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu13Voltage_Type.__name__ = "Integer32"
_Pdu13Voltage_Object = MibScalar
pdu13Voltage = _Pdu13Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 17),
    _Pdu13Voltage_Type()
)
pdu13Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13Voltage.setStatus("mandatory")


class _Pdu13ModelName_Type(DisplayString):
    """Custom type pdu13ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu13ModelName_Type.__name__ = "DisplayString"
_Pdu13ModelName_Object = MibScalar
pdu13ModelName = _Pdu13ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 18),
    _Pdu13ModelName_Type()
)
pdu13ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13ModelName.setStatus("mandatory")


class _Pdu13ModelNo_Type(DisplayString):
    """Custom type pdu13ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu13ModelNo_Type.__name__ = "DisplayString"
_Pdu13ModelNo_Object = MibScalar
pdu13ModelNo = _Pdu13ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 19),
    _Pdu13ModelNo_Type()
)
pdu13ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13ModelNo.setStatus("mandatory")


class _Pdu13Identify_Type(DisplayString):
    """Custom type pdu13Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu13Identify_Type.__name__ = "DisplayString"
_Pdu13Identify_Object = MibScalar
pdu13Identify = _Pdu13Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 13, 20),
    _Pdu13Identify_Type()
)
pdu13Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu13Identify.setStatus("mandatory")
_Pdu14Entry_ObjectIdentity = ObjectIdentity
pdu14Entry = _Pdu14Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14)
)
_Pdu14Value_Type = Integer32
_Pdu14Value_Object = MibScalar
pdu14Value = _Pdu14Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 11),
    _Pdu14Value_Type()
)
pdu14Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14Value.setStatus("mandatory")


class _Pdu14SubValues_Type(DisplayString):
    """Custom type pdu14SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu14SubValues_Type.__name__ = "DisplayString"
_Pdu14SubValues_Object = MibScalar
pdu14SubValues = _Pdu14SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 12),
    _Pdu14SubValues_Type()
)
pdu14SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14SubValues.setStatus("mandatory")


class _Pdu14OutletStatus_Type(DisplayString):
    """Custom type pdu14OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu14OutletStatus_Type.__name__ = "DisplayString"
_Pdu14OutletStatus_Object = MibScalar
pdu14OutletStatus = _Pdu14OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 13),
    _Pdu14OutletStatus_Type()
)
pdu14OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14OutletStatus.setStatus("mandatory")
_Pdu14OutletConfigs_ObjectIdentity = ObjectIdentity
pdu14OutletConfigs = _Pdu14OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 14)
)


class _Pdu14Outlet1Config_Type(DisplayString):
    """Custom type pdu14Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu14Outlet1Config_Type.__name__ = "DisplayString"
_Pdu14Outlet1Config_Object = MibScalar
pdu14Outlet1Config = _Pdu14Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 14, 1),
    _Pdu14Outlet1Config_Type()
)
pdu14Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14Outlet1Config.setStatus("mandatory")


class _Pdu14Outlet2Config_Type(DisplayString):
    """Custom type pdu14Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu14Outlet2Config_Type.__name__ = "DisplayString"
_Pdu14Outlet2Config_Object = MibScalar
pdu14Outlet2Config = _Pdu14Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 14, 2),
    _Pdu14Outlet2Config_Type()
)
pdu14Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14Outlet2Config.setStatus("mandatory")


class _Pdu14Outlet3Config_Type(DisplayString):
    """Custom type pdu14Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu14Outlet3Config_Type.__name__ = "DisplayString"
_Pdu14Outlet3Config_Object = MibScalar
pdu14Outlet3Config = _Pdu14Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 14, 3),
    _Pdu14Outlet3Config_Type()
)
pdu14Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14Outlet3Config.setStatus("mandatory")


class _Pdu14Outlet4Config_Type(DisplayString):
    """Custom type pdu14Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu14Outlet4Config_Type.__name__ = "DisplayString"
_Pdu14Outlet4Config_Object = MibScalar
pdu14Outlet4Config = _Pdu14Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 14, 4),
    _Pdu14Outlet4Config_Type()
)
pdu14Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14Outlet4Config.setStatus("mandatory")


class _Pdu14Outlet5Config_Type(DisplayString):
    """Custom type pdu14Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu14Outlet5Config_Type.__name__ = "DisplayString"
_Pdu14Outlet5Config_Object = MibScalar
pdu14Outlet5Config = _Pdu14Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 14, 5),
    _Pdu14Outlet5Config_Type()
)
pdu14Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14Outlet5Config.setStatus("mandatory")


class _Pdu14Outlet6Config_Type(DisplayString):
    """Custom type pdu14Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu14Outlet6Config_Type.__name__ = "DisplayString"
_Pdu14Outlet6Config_Object = MibScalar
pdu14Outlet6Config = _Pdu14Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 14, 6),
    _Pdu14Outlet6Config_Type()
)
pdu14Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14Outlet6Config.setStatus("mandatory")


class _Pdu14Outlet7Config_Type(DisplayString):
    """Custom type pdu14Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu14Outlet7Config_Type.__name__ = "DisplayString"
_Pdu14Outlet7Config_Object = MibScalar
pdu14Outlet7Config = _Pdu14Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 14, 7),
    _Pdu14Outlet7Config_Type()
)
pdu14Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14Outlet7Config.setStatus("mandatory")


class _Pdu14Outlet8Config_Type(DisplayString):
    """Custom type pdu14Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu14Outlet8Config_Type.__name__ = "DisplayString"
_Pdu14Outlet8Config_Object = MibScalar
pdu14Outlet8Config = _Pdu14Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 14, 8),
    _Pdu14Outlet8Config_Type()
)
pdu14Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14Outlet8Config.setStatus("mandatory")


class _Pdu14Threshold1_Type(Integer32):
    """Custom type pdu14Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu14Threshold1_Type.__name__ = "Integer32"
_Pdu14Threshold1_Object = MibScalar
pdu14Threshold1 = _Pdu14Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 15),
    _Pdu14Threshold1_Type()
)
pdu14Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu14Threshold1.setStatus("mandatory")


class _Pdu14Threshold2_Type(Integer32):
    """Custom type pdu14Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu14Threshold2_Type.__name__ = "Integer32"
_Pdu14Threshold2_Object = MibScalar
pdu14Threshold2 = _Pdu14Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 16),
    _Pdu14Threshold2_Type()
)
pdu14Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu14Threshold2.setStatus("mandatory")


class _Pdu14Voltage_Type(Integer32):
    """Custom type pdu14Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu14Voltage_Type.__name__ = "Integer32"
_Pdu14Voltage_Object = MibScalar
pdu14Voltage = _Pdu14Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 17),
    _Pdu14Voltage_Type()
)
pdu14Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14Voltage.setStatus("mandatory")


class _Pdu14ModelName_Type(DisplayString):
    """Custom type pdu14ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu14ModelName_Type.__name__ = "DisplayString"
_Pdu14ModelName_Object = MibScalar
pdu14ModelName = _Pdu14ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 18),
    _Pdu14ModelName_Type()
)
pdu14ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14ModelName.setStatus("mandatory")


class _Pdu14ModelNo_Type(DisplayString):
    """Custom type pdu14ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu14ModelNo_Type.__name__ = "DisplayString"
_Pdu14ModelNo_Object = MibScalar
pdu14ModelNo = _Pdu14ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 19),
    _Pdu14ModelNo_Type()
)
pdu14ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14ModelNo.setStatus("mandatory")


class _Pdu14Identify_Type(DisplayString):
    """Custom type pdu14Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu14Identify_Type.__name__ = "DisplayString"
_Pdu14Identify_Object = MibScalar
pdu14Identify = _Pdu14Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 14, 20),
    _Pdu14Identify_Type()
)
pdu14Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu14Identify.setStatus("mandatory")
_Pdu15Entry_ObjectIdentity = ObjectIdentity
pdu15Entry = _Pdu15Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15)
)
_Pdu15Value_Type = Integer32
_Pdu15Value_Object = MibScalar
pdu15Value = _Pdu15Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 11),
    _Pdu15Value_Type()
)
pdu15Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15Value.setStatus("mandatory")


class _Pdu15SubValues_Type(DisplayString):
    """Custom type pdu15SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu15SubValues_Type.__name__ = "DisplayString"
_Pdu15SubValues_Object = MibScalar
pdu15SubValues = _Pdu15SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 12),
    _Pdu15SubValues_Type()
)
pdu15SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15SubValues.setStatus("mandatory")


class _Pdu15OutletStatus_Type(DisplayString):
    """Custom type pdu15OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu15OutletStatus_Type.__name__ = "DisplayString"
_Pdu15OutletStatus_Object = MibScalar
pdu15OutletStatus = _Pdu15OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 13),
    _Pdu15OutletStatus_Type()
)
pdu15OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15OutletStatus.setStatus("mandatory")
_Pdu15OutletConfigs_ObjectIdentity = ObjectIdentity
pdu15OutletConfigs = _Pdu15OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 14)
)


class _Pdu15Outlet1Config_Type(DisplayString):
    """Custom type pdu15Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu15Outlet1Config_Type.__name__ = "DisplayString"
_Pdu15Outlet1Config_Object = MibScalar
pdu15Outlet1Config = _Pdu15Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 14, 1),
    _Pdu15Outlet1Config_Type()
)
pdu15Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15Outlet1Config.setStatus("mandatory")


class _Pdu15Outlet2Config_Type(DisplayString):
    """Custom type pdu15Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu15Outlet2Config_Type.__name__ = "DisplayString"
_Pdu15Outlet2Config_Object = MibScalar
pdu15Outlet2Config = _Pdu15Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 14, 2),
    _Pdu15Outlet2Config_Type()
)
pdu15Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15Outlet2Config.setStatus("mandatory")


class _Pdu15Outlet3Config_Type(DisplayString):
    """Custom type pdu15Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu15Outlet3Config_Type.__name__ = "DisplayString"
_Pdu15Outlet3Config_Object = MibScalar
pdu15Outlet3Config = _Pdu15Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 14, 3),
    _Pdu15Outlet3Config_Type()
)
pdu15Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15Outlet3Config.setStatus("mandatory")


class _Pdu15Outlet4Config_Type(DisplayString):
    """Custom type pdu15Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu15Outlet4Config_Type.__name__ = "DisplayString"
_Pdu15Outlet4Config_Object = MibScalar
pdu15Outlet4Config = _Pdu15Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 14, 4),
    _Pdu15Outlet4Config_Type()
)
pdu15Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15Outlet4Config.setStatus("mandatory")


class _Pdu15Outlet5Config_Type(DisplayString):
    """Custom type pdu15Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu15Outlet5Config_Type.__name__ = "DisplayString"
_Pdu15Outlet5Config_Object = MibScalar
pdu15Outlet5Config = _Pdu15Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 14, 5),
    _Pdu15Outlet5Config_Type()
)
pdu15Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15Outlet5Config.setStatus("mandatory")


class _Pdu15Outlet6Config_Type(DisplayString):
    """Custom type pdu15Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu15Outlet6Config_Type.__name__ = "DisplayString"
_Pdu15Outlet6Config_Object = MibScalar
pdu15Outlet6Config = _Pdu15Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 14, 6),
    _Pdu15Outlet6Config_Type()
)
pdu15Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15Outlet6Config.setStatus("mandatory")


class _Pdu15Outlet7Config_Type(DisplayString):
    """Custom type pdu15Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu15Outlet7Config_Type.__name__ = "DisplayString"
_Pdu15Outlet7Config_Object = MibScalar
pdu15Outlet7Config = _Pdu15Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 14, 7),
    _Pdu15Outlet7Config_Type()
)
pdu15Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15Outlet7Config.setStatus("mandatory")


class _Pdu15Outlet8Config_Type(DisplayString):
    """Custom type pdu15Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu15Outlet8Config_Type.__name__ = "DisplayString"
_Pdu15Outlet8Config_Object = MibScalar
pdu15Outlet8Config = _Pdu15Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 14, 8),
    _Pdu15Outlet8Config_Type()
)
pdu15Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15Outlet8Config.setStatus("mandatory")


class _Pdu15Threshold1_Type(Integer32):
    """Custom type pdu15Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu15Threshold1_Type.__name__ = "Integer32"
_Pdu15Threshold1_Object = MibScalar
pdu15Threshold1 = _Pdu15Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 15),
    _Pdu15Threshold1_Type()
)
pdu15Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu15Threshold1.setStatus("mandatory")


class _Pdu15Threshold2_Type(Integer32):
    """Custom type pdu15Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu15Threshold2_Type.__name__ = "Integer32"
_Pdu15Threshold2_Object = MibScalar
pdu15Threshold2 = _Pdu15Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 16),
    _Pdu15Threshold2_Type()
)
pdu15Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu15Threshold2.setStatus("mandatory")


class _Pdu15Voltage_Type(Integer32):
    """Custom type pdu15Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu15Voltage_Type.__name__ = "Integer32"
_Pdu15Voltage_Object = MibScalar
pdu15Voltage = _Pdu15Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 17),
    _Pdu15Voltage_Type()
)
pdu15Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15Voltage.setStatus("mandatory")


class _Pdu15ModelName_Type(DisplayString):
    """Custom type pdu15ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu15ModelName_Type.__name__ = "DisplayString"
_Pdu15ModelName_Object = MibScalar
pdu15ModelName = _Pdu15ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 18),
    _Pdu15ModelName_Type()
)
pdu15ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15ModelName.setStatus("mandatory")


class _Pdu15ModelNo_Type(DisplayString):
    """Custom type pdu15ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu15ModelNo_Type.__name__ = "DisplayString"
_Pdu15ModelNo_Object = MibScalar
pdu15ModelNo = _Pdu15ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 19),
    _Pdu15ModelNo_Type()
)
pdu15ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15ModelNo.setStatus("mandatory")


class _Pdu15Identify_Type(DisplayString):
    """Custom type pdu15Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu15Identify_Type.__name__ = "DisplayString"
_Pdu15Identify_Object = MibScalar
pdu15Identify = _Pdu15Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 15, 20),
    _Pdu15Identify_Type()
)
pdu15Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu15Identify.setStatus("mandatory")
_Pdu16Entry_ObjectIdentity = ObjectIdentity
pdu16Entry = _Pdu16Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16)
)
_Pdu16Value_Type = Integer32
_Pdu16Value_Object = MibScalar
pdu16Value = _Pdu16Value_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 11),
    _Pdu16Value_Type()
)
pdu16Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16Value.setStatus("mandatory")


class _Pdu16SubValues_Type(DisplayString):
    """Custom type pdu16SubValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu16SubValues_Type.__name__ = "DisplayString"
_Pdu16SubValues_Object = MibScalar
pdu16SubValues = _Pdu16SubValues_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 12),
    _Pdu16SubValues_Type()
)
pdu16SubValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16SubValues.setStatus("mandatory")


class _Pdu16OutletStatus_Type(DisplayString):
    """Custom type pdu16OutletStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu16OutletStatus_Type.__name__ = "DisplayString"
_Pdu16OutletStatus_Object = MibScalar
pdu16OutletStatus = _Pdu16OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 13),
    _Pdu16OutletStatus_Type()
)
pdu16OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16OutletStatus.setStatus("mandatory")
_Pdu16OutletConfigs_ObjectIdentity = ObjectIdentity
pdu16OutletConfigs = _Pdu16OutletConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 14)
)


class _Pdu16Outlet1Config_Type(DisplayString):
    """Custom type pdu16Outlet1Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu16Outlet1Config_Type.__name__ = "DisplayString"
_Pdu16Outlet1Config_Object = MibScalar
pdu16Outlet1Config = _Pdu16Outlet1Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 14, 1),
    _Pdu16Outlet1Config_Type()
)
pdu16Outlet1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16Outlet1Config.setStatus("mandatory")


class _Pdu16Outlet2Config_Type(DisplayString):
    """Custom type pdu16Outlet2Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu16Outlet2Config_Type.__name__ = "DisplayString"
_Pdu16Outlet2Config_Object = MibScalar
pdu16Outlet2Config = _Pdu16Outlet2Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 14, 2),
    _Pdu16Outlet2Config_Type()
)
pdu16Outlet2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16Outlet2Config.setStatus("mandatory")


class _Pdu16Outlet3Config_Type(DisplayString):
    """Custom type pdu16Outlet3Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu16Outlet3Config_Type.__name__ = "DisplayString"
_Pdu16Outlet3Config_Object = MibScalar
pdu16Outlet3Config = _Pdu16Outlet3Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 14, 3),
    _Pdu16Outlet3Config_Type()
)
pdu16Outlet3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16Outlet3Config.setStatus("mandatory")


class _Pdu16Outlet4Config_Type(DisplayString):
    """Custom type pdu16Outlet4Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu16Outlet4Config_Type.__name__ = "DisplayString"
_Pdu16Outlet4Config_Object = MibScalar
pdu16Outlet4Config = _Pdu16Outlet4Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 14, 4),
    _Pdu16Outlet4Config_Type()
)
pdu16Outlet4Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16Outlet4Config.setStatus("mandatory")


class _Pdu16Outlet5Config_Type(DisplayString):
    """Custom type pdu16Outlet5Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu16Outlet5Config_Type.__name__ = "DisplayString"
_Pdu16Outlet5Config_Object = MibScalar
pdu16Outlet5Config = _Pdu16Outlet5Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 14, 5),
    _Pdu16Outlet5Config_Type()
)
pdu16Outlet5Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16Outlet5Config.setStatus("mandatory")


class _Pdu16Outlet6Config_Type(DisplayString):
    """Custom type pdu16Outlet6Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu16Outlet6Config_Type.__name__ = "DisplayString"
_Pdu16Outlet6Config_Object = MibScalar
pdu16Outlet6Config = _Pdu16Outlet6Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 14, 6),
    _Pdu16Outlet6Config_Type()
)
pdu16Outlet6Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16Outlet6Config.setStatus("mandatory")


class _Pdu16Outlet7Config_Type(DisplayString):
    """Custom type pdu16Outlet7Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu16Outlet7Config_Type.__name__ = "DisplayString"
_Pdu16Outlet7Config_Object = MibScalar
pdu16Outlet7Config = _Pdu16Outlet7Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 14, 7),
    _Pdu16Outlet7Config_Type()
)
pdu16Outlet7Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16Outlet7Config.setStatus("mandatory")


class _Pdu16Outlet8Config_Type(DisplayString):
    """Custom type pdu16Outlet8Config based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pdu16Outlet8Config_Type.__name__ = "DisplayString"
_Pdu16Outlet8Config_Object = MibScalar
pdu16Outlet8Config = _Pdu16Outlet8Config_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 14, 8),
    _Pdu16Outlet8Config_Type()
)
pdu16Outlet8Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16Outlet8Config.setStatus("mandatory")


class _Pdu16Threshold1_Type(Integer32):
    """Custom type pdu16Threshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu16Threshold1_Type.__name__ = "Integer32"
_Pdu16Threshold1_Object = MibScalar
pdu16Threshold1 = _Pdu16Threshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 15),
    _Pdu16Threshold1_Type()
)
pdu16Threshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu16Threshold1.setStatus("mandatory")


class _Pdu16Threshold2_Type(Integer32):
    """Custom type pdu16Threshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu16Threshold2_Type.__name__ = "Integer32"
_Pdu16Threshold2_Object = MibScalar
pdu16Threshold2 = _Pdu16Threshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 16),
    _Pdu16Threshold2_Type()
)
pdu16Threshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu16Threshold2.setStatus("mandatory")


class _Pdu16Voltage_Type(Integer32):
    """Custom type pdu16Voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu16Voltage_Type.__name__ = "Integer32"
_Pdu16Voltage_Object = MibScalar
pdu16Voltage = _Pdu16Voltage_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 17),
    _Pdu16Voltage_Type()
)
pdu16Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16Voltage.setStatus("mandatory")


class _Pdu16ModelName_Type(DisplayString):
    """Custom type pdu16ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu16ModelName_Type.__name__ = "DisplayString"
_Pdu16ModelName_Object = MibScalar
pdu16ModelName = _Pdu16ModelName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 18),
    _Pdu16ModelName_Type()
)
pdu16ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16ModelName.setStatus("mandatory")


class _Pdu16ModelNo_Type(DisplayString):
    """Custom type pdu16ModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu16ModelNo_Type.__name__ = "DisplayString"
_Pdu16ModelNo_Object = MibScalar
pdu16ModelNo = _Pdu16ModelNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 19),
    _Pdu16ModelNo_Type()
)
pdu16ModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16ModelNo.setStatus("mandatory")


class _Pdu16Identify_Type(DisplayString):
    """Custom type pdu16Identify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pdu16Identify_Type.__name__ = "DisplayString"
_Pdu16Identify_Object = MibScalar
pdu16Identify = _Pdu16Identify_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 2, 9, 16, 20),
    _Pdu16Identify_Type()
)
pdu16Identify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu16Identify.setStatus("mandatory")

# Managed Objects groups


# Notification objects

devOutOfThreshold1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 17420, 0, 105)
)
if mibBuilder.loadTexts:
    devOutOfThreshold1.setStatus(
        ""
    )

devOutOfThreshold2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 17420, 0, 106)
)
if mibBuilder.loadTexts:
    devOutOfThreshold2.setStatus(
        ""
    )

devBackToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 17420, 0, 108)
)
if mibBuilder.loadTexts:
    devBackToNormal.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGPPDU-MIB",
    **{"dgp": dgp,
       "devOutOfThreshold1": devOutOfThreshold1,
       "devOutOfThreshold2": devOutOfThreshold2,
       "devBackToNormal": devBackToNormal,
       "products": products,
       "devTable": devTable,
       "devID": devID,
       "devIP": devIP,
       "devMAC": devMAC,
       "devVersion": devVersion,
       "devInfo": devInfo,
       "devValues": devValues,
       "devTemperature": devTemperature,
       "devHumidity": devHumidity,
       "pduTable": pduTable,
       "pdu01Entry": pdu01Entry,
       "pdu01Value": pdu01Value,
       "pdu01SubValues": pdu01SubValues,
       "pdu01OutletStatus": pdu01OutletStatus,
       "pdu01OutletConfigs": pdu01OutletConfigs,
       "pdu01Outlet1Config": pdu01Outlet1Config,
       "pdu01Outlet2Config": pdu01Outlet2Config,
       "pdu01Outlet3Config": pdu01Outlet3Config,
       "pdu01Outlet4Config": pdu01Outlet4Config,
       "pdu01Outlet5Config": pdu01Outlet5Config,
       "pdu01Outlet6Config": pdu01Outlet6Config,
       "pdu01Outlet7Config": pdu01Outlet7Config,
       "pdu01Outlet8Config": pdu01Outlet8Config,
       "pdu01Outlet9Config": pdu01Outlet9Config,
       "pdu01Outlet10Config": pdu01Outlet10Config,
       "pdu01Outlet11Config": pdu01Outlet11Config,
       "pdu01Outlet12Config": pdu01Outlet12Config,
       "pdu01Outlet13Config": pdu01Outlet13Config,
       "pdu01Outlet14Config": pdu01Outlet14Config,
       "pdu01Outlet15Config": pdu01Outlet15Config,
       "pdu01Outlet16Config": pdu01Outlet16Config,
       "pdu01Outlet17Config": pdu01Outlet17Config,
       "pdu01Outlet18Config": pdu01Outlet18Config,
       "pdu01Outlet19Config": pdu01Outlet19Config,
       "pdu01Outlet20Config": pdu01Outlet20Config,
       "pdu01Outlet21Config": pdu01Outlet21Config,
       "pdu01Outlet22Config": pdu01Outlet22Config,
       "pdu01Outlet23Config": pdu01Outlet23Config,
       "pdu01Outlet24Config": pdu01Outlet24Config,
       "pdu01Threshold1": pdu01Threshold1,
       "pdu01Threshold2": pdu01Threshold2,
       "pdu01Voltage": pdu01Voltage,
       "pdu01ModelName": pdu01ModelName,
       "pdu01ModelNo": pdu01ModelNo,
       "pdu01Identify": pdu01Identify,
       "pdu02Entry": pdu02Entry,
       "pdu02Value": pdu02Value,
       "pdu02SubValues": pdu02SubValues,
       "pdu02OutletStatus": pdu02OutletStatus,
       "pdu02OutletConfigs": pdu02OutletConfigs,
       "pdu02Outlet1Config": pdu02Outlet1Config,
       "pdu02Outlet2Config": pdu02Outlet2Config,
       "pdu02Outlet3Config": pdu02Outlet3Config,
       "pdu02Outlet4Config": pdu02Outlet4Config,
       "pdu02Outlet5Config": pdu02Outlet5Config,
       "pdu02Outlet6Config": pdu02Outlet6Config,
       "pdu02Outlet7Config": pdu02Outlet7Config,
       "pdu02Outlet8Config": pdu02Outlet8Config,
       "pdu02Threshold1": pdu02Threshold1,
       "pdu02Threshold2": pdu02Threshold2,
       "pdu02Voltage": pdu02Voltage,
       "pdu02ModelName": pdu02ModelName,
       "pdu02ModelNo": pdu02ModelNo,
       "pdu02Identify": pdu02Identify,
       "pdu03Entry": pdu03Entry,
       "pdu03Value": pdu03Value,
       "pdu03SubValues": pdu03SubValues,
       "pdu03OutletStatus": pdu03OutletStatus,
       "pdu03OutletConfigs": pdu03OutletConfigs,
       "pdu03Outlet1Config": pdu03Outlet1Config,
       "pdu03Outlet2Config": pdu03Outlet2Config,
       "pdu03Outlet3Config": pdu03Outlet3Config,
       "pdu03Outlet4Config": pdu03Outlet4Config,
       "pdu03Outlet5Config": pdu03Outlet5Config,
       "pdu03Outlet6Config": pdu03Outlet6Config,
       "pdu03Outlet7Config": pdu03Outlet7Config,
       "pdu03Outlet8Config": pdu03Outlet8Config,
       "pdu03Threshold1": pdu03Threshold1,
       "pdu03Threshold2": pdu03Threshold2,
       "pdu03Voltage": pdu03Voltage,
       "pdu03ModelName": pdu03ModelName,
       "pdu03ModelNo": pdu03ModelNo,
       "pdu03Identify": pdu03Identify,
       "pdu04Entry": pdu04Entry,
       "pdu04Value": pdu04Value,
       "pdu04SubValues": pdu04SubValues,
       "pdu04OutletStatus": pdu04OutletStatus,
       "pdu04OutletConfigs": pdu04OutletConfigs,
       "pdu04Outlet1Config": pdu04Outlet1Config,
       "pdu04Outlet2Config": pdu04Outlet2Config,
       "pdu04Outlet3Config": pdu04Outlet3Config,
       "pdu04Outlet4Config": pdu04Outlet4Config,
       "pdu04Outlet5Config": pdu04Outlet5Config,
       "pdu04Outlet6Config": pdu04Outlet6Config,
       "pdu04Outlet7Config": pdu04Outlet7Config,
       "pdu04Outlet8Config": pdu04Outlet8Config,
       "pdu04Threshold1": pdu04Threshold1,
       "pdu04Threshold2": pdu04Threshold2,
       "pdu04Voltage": pdu04Voltage,
       "pdu04ModelName": pdu04ModelName,
       "pdu04ModelNo": pdu04ModelNo,
       "pdu04Identify": pdu04Identify,
       "pdu05Entry": pdu05Entry,
       "pdu05Value": pdu05Value,
       "pdu05SubValues": pdu05SubValues,
       "pdu05OutletStatus": pdu05OutletStatus,
       "pdu05OutletConfigs": pdu05OutletConfigs,
       "pdu05Outlet1Config": pdu05Outlet1Config,
       "pdu05Outlet2Config": pdu05Outlet2Config,
       "pdu05Outlet3Config": pdu05Outlet3Config,
       "pdu05Outlet4Config": pdu05Outlet4Config,
       "pdu05Outlet5Config": pdu05Outlet5Config,
       "pdu05Outlet6Config": pdu05Outlet6Config,
       "pdu05Outlet7Config": pdu05Outlet7Config,
       "pdu05Outlet8Config": pdu05Outlet8Config,
       "pdu05Threshold1": pdu05Threshold1,
       "pdu05Threshold2": pdu05Threshold2,
       "pdu05Voltage": pdu05Voltage,
       "pdu05ModelName": pdu05ModelName,
       "pdu05ModelNo": pdu05ModelNo,
       "pdu05Identify": pdu05Identify,
       "pdu06Entry": pdu06Entry,
       "pdu06Value": pdu06Value,
       "pdu06SubValues": pdu06SubValues,
       "pdu06OutletStatus": pdu06OutletStatus,
       "pdu06OutletConfigs": pdu06OutletConfigs,
       "pdu06Outlet1Config": pdu06Outlet1Config,
       "pdu06Outlet2Config": pdu06Outlet2Config,
       "pdu06Outlet3Config": pdu06Outlet3Config,
       "pdu06Outlet4Config": pdu06Outlet4Config,
       "pdu06Outlet5Config": pdu06Outlet5Config,
       "pdu06Outlet6Config": pdu06Outlet6Config,
       "pdu06Outlet7Config": pdu06Outlet7Config,
       "pdu06Outlet8Config": pdu06Outlet8Config,
       "pdu06Threshold1": pdu06Threshold1,
       "pdu06Threshold2": pdu06Threshold2,
       "pdu06Voltage": pdu06Voltage,
       "pdu06ModelName": pdu06ModelName,
       "pdu06ModelNo": pdu06ModelNo,
       "pdu06Identify": pdu06Identify,
       "pdu07Entry": pdu07Entry,
       "pdu07Value": pdu07Value,
       "pdu07SubValues": pdu07SubValues,
       "pdu07OutletStatus": pdu07OutletStatus,
       "pdu07OutletConfigs": pdu07OutletConfigs,
       "pdu07Outlet1Config": pdu07Outlet1Config,
       "pdu07Outlet2Config": pdu07Outlet2Config,
       "pdu07Outlet3Config": pdu07Outlet3Config,
       "pdu07Outlet4Config": pdu07Outlet4Config,
       "pdu07Outlet5Config": pdu07Outlet5Config,
       "pdu07Outlet6Config": pdu07Outlet6Config,
       "pdu07Outlet7Config": pdu07Outlet7Config,
       "pdu07Outlet8Config": pdu07Outlet8Config,
       "pdu07Threshold1": pdu07Threshold1,
       "pdu07Threshold2": pdu07Threshold2,
       "pdu07Voltage": pdu07Voltage,
       "pdu07ModelName": pdu07ModelName,
       "pdu07ModelNo": pdu07ModelNo,
       "pdu07Identify": pdu07Identify,
       "pdu08Entry": pdu08Entry,
       "pdu08Value": pdu08Value,
       "pdu08SubValues": pdu08SubValues,
       "pdu08OutletStatus": pdu08OutletStatus,
       "pdu08OutletConfigs": pdu08OutletConfigs,
       "pdu08Outlet1Config": pdu08Outlet1Config,
       "pdu08Outlet2Config": pdu08Outlet2Config,
       "pdu08Outlet3Config": pdu08Outlet3Config,
       "pdu08Outlet4Config": pdu08Outlet4Config,
       "pdu08Outlet5Config": pdu08Outlet5Config,
       "pdu08Outlet6Config": pdu08Outlet6Config,
       "pdu08Outlet7Config": pdu08Outlet7Config,
       "pdu08Outlet8Config": pdu08Outlet8Config,
       "pdu08Threshold1": pdu08Threshold1,
       "pdu08Threshold2": pdu08Threshold2,
       "pdu08Voltage": pdu08Voltage,
       "pdu08ModelName": pdu08ModelName,
       "pdu08ModelNo": pdu08ModelNo,
       "pdu08Identify": pdu08Identify,
       "pdu09Entry": pdu09Entry,
       "pdu09Value": pdu09Value,
       "pdu09SubValues": pdu09SubValues,
       "pdu09OutletStatus": pdu09OutletStatus,
       "pdu09OutletConfigs": pdu09OutletConfigs,
       "pdu09Outlet1Config": pdu09Outlet1Config,
       "pdu09Outlet2Config": pdu09Outlet2Config,
       "pdu09Outlet3Config": pdu09Outlet3Config,
       "pdu09Outlet4Config": pdu09Outlet4Config,
       "pdu09Outlet5Config": pdu09Outlet5Config,
       "pdu09Outlet6Config": pdu09Outlet6Config,
       "pdu09Outlet7Config": pdu09Outlet7Config,
       "pdu09Outlet8Config": pdu09Outlet8Config,
       "pdu09Threshold1": pdu09Threshold1,
       "pdu09Threshold2": pdu09Threshold2,
       "pdu09Voltage": pdu09Voltage,
       "pdu09ModelName": pdu09ModelName,
       "pdu09ModelNo": pdu09ModelNo,
       "pdu09Identify": pdu09Identify,
       "pdu10Entry": pdu10Entry,
       "pdu10Value": pdu10Value,
       "pdu10SubValues": pdu10SubValues,
       "pdu10OutletStatus": pdu10OutletStatus,
       "pdu10OutletConfigs": pdu10OutletConfigs,
       "pdu10Outlet1Config": pdu10Outlet1Config,
       "pdu10Outlet2Config": pdu10Outlet2Config,
       "pdu10Outlet3Config": pdu10Outlet3Config,
       "pdu10Outlet4Config": pdu10Outlet4Config,
       "pdu10Outlet5Config": pdu10Outlet5Config,
       "pdu10Outlet6Config": pdu10Outlet6Config,
       "pdu10Outlet7Config": pdu10Outlet7Config,
       "pdu10Outlet8Config": pdu10Outlet8Config,
       "pdu10Threshold1": pdu10Threshold1,
       "pdu10Threshold2": pdu10Threshold2,
       "pdu10Voltage": pdu10Voltage,
       "pdu10ModelName": pdu10ModelName,
       "pdu10ModelNo": pdu10ModelNo,
       "pdu10Identify": pdu10Identify,
       "pdu11Entry": pdu11Entry,
       "pdu11Value": pdu11Value,
       "pdu11SubValues": pdu11SubValues,
       "pdu11OutletStatus": pdu11OutletStatus,
       "pdu11OutletConfigs": pdu11OutletConfigs,
       "pdu11Outlet1Config": pdu11Outlet1Config,
       "pdu11Outlet2Config": pdu11Outlet2Config,
       "pdu11Outlet3Config": pdu11Outlet3Config,
       "pdu11Outlet4Config": pdu11Outlet4Config,
       "pdu11Outlet5Config": pdu11Outlet5Config,
       "pdu11Outlet6Config": pdu11Outlet6Config,
       "pdu11Outlet7Config": pdu11Outlet7Config,
       "pdu11Outlet8Config": pdu11Outlet8Config,
       "pdu11Threshold1": pdu11Threshold1,
       "pdu11Threshold2": pdu11Threshold2,
       "pdu11Voltage": pdu11Voltage,
       "pdu11ModelName": pdu11ModelName,
       "pdu11ModelNo": pdu11ModelNo,
       "pdu11Identify": pdu11Identify,
       "pdu12Entry": pdu12Entry,
       "pdu12Value": pdu12Value,
       "pdu12SubValues": pdu12SubValues,
       "pdu12OutletStatus": pdu12OutletStatus,
       "pdu12OutletConfigs": pdu12OutletConfigs,
       "pdu12Outlet1Config": pdu12Outlet1Config,
       "pdu12Outlet2Config": pdu12Outlet2Config,
       "pdu12Outlet3Config": pdu12Outlet3Config,
       "pdu12Outlet4Config": pdu12Outlet4Config,
       "pdu12Outlet5Config": pdu12Outlet5Config,
       "pdu12Outlet6Config": pdu12Outlet6Config,
       "pdu12Outlet7Config": pdu12Outlet7Config,
       "pdu12Outlet8Config": pdu12Outlet8Config,
       "pdu12Threshold1": pdu12Threshold1,
       "pdu12Threshold2": pdu12Threshold2,
       "pdu12Voltage": pdu12Voltage,
       "pdu12ModelName": pdu12ModelName,
       "pdu12ModelNo": pdu12ModelNo,
       "pdu12Identify": pdu12Identify,
       "pdu13Entry": pdu13Entry,
       "pdu13Value": pdu13Value,
       "pdu13SubValues": pdu13SubValues,
       "pdu13OutletStatus": pdu13OutletStatus,
       "pdu13OutletConfigs": pdu13OutletConfigs,
       "pdu13Outlet1Config": pdu13Outlet1Config,
       "pdu13Outlet2Config": pdu13Outlet2Config,
       "pdu13Outlet3Config": pdu13Outlet3Config,
       "pdu13Outlet4Config": pdu13Outlet4Config,
       "pdu13Outlet5Config": pdu13Outlet5Config,
       "pdu13Outlet6Config": pdu13Outlet6Config,
       "pdu13Outlet7Config": pdu13Outlet7Config,
       "pdu13Outlet8Config": pdu13Outlet8Config,
       "pdu13Threshold1": pdu13Threshold1,
       "pdu13Threshold2": pdu13Threshold2,
       "pdu13Voltage": pdu13Voltage,
       "pdu13ModelName": pdu13ModelName,
       "pdu13ModelNo": pdu13ModelNo,
       "pdu13Identify": pdu13Identify,
       "pdu14Entry": pdu14Entry,
       "pdu14Value": pdu14Value,
       "pdu14SubValues": pdu14SubValues,
       "pdu14OutletStatus": pdu14OutletStatus,
       "pdu14OutletConfigs": pdu14OutletConfigs,
       "pdu14Outlet1Config": pdu14Outlet1Config,
       "pdu14Outlet2Config": pdu14Outlet2Config,
       "pdu14Outlet3Config": pdu14Outlet3Config,
       "pdu14Outlet4Config": pdu14Outlet4Config,
       "pdu14Outlet5Config": pdu14Outlet5Config,
       "pdu14Outlet6Config": pdu14Outlet6Config,
       "pdu14Outlet7Config": pdu14Outlet7Config,
       "pdu14Outlet8Config": pdu14Outlet8Config,
       "pdu14Threshold1": pdu14Threshold1,
       "pdu14Threshold2": pdu14Threshold2,
       "pdu14Voltage": pdu14Voltage,
       "pdu14ModelName": pdu14ModelName,
       "pdu14ModelNo": pdu14ModelNo,
       "pdu14Identify": pdu14Identify,
       "pdu15Entry": pdu15Entry,
       "pdu15Value": pdu15Value,
       "pdu15SubValues": pdu15SubValues,
       "pdu15OutletStatus": pdu15OutletStatus,
       "pdu15OutletConfigs": pdu15OutletConfigs,
       "pdu15Outlet1Config": pdu15Outlet1Config,
       "pdu15Outlet2Config": pdu15Outlet2Config,
       "pdu15Outlet3Config": pdu15Outlet3Config,
       "pdu15Outlet4Config": pdu15Outlet4Config,
       "pdu15Outlet5Config": pdu15Outlet5Config,
       "pdu15Outlet6Config": pdu15Outlet6Config,
       "pdu15Outlet7Config": pdu15Outlet7Config,
       "pdu15Outlet8Config": pdu15Outlet8Config,
       "pdu15Threshold1": pdu15Threshold1,
       "pdu15Threshold2": pdu15Threshold2,
       "pdu15Voltage": pdu15Voltage,
       "pdu15ModelName": pdu15ModelName,
       "pdu15ModelNo": pdu15ModelNo,
       "pdu15Identify": pdu15Identify,
       "pdu16Entry": pdu16Entry,
       "pdu16Value": pdu16Value,
       "pdu16SubValues": pdu16SubValues,
       "pdu16OutletStatus": pdu16OutletStatus,
       "pdu16OutletConfigs": pdu16OutletConfigs,
       "pdu16Outlet1Config": pdu16Outlet1Config,
       "pdu16Outlet2Config": pdu16Outlet2Config,
       "pdu16Outlet3Config": pdu16Outlet3Config,
       "pdu16Outlet4Config": pdu16Outlet4Config,
       "pdu16Outlet5Config": pdu16Outlet5Config,
       "pdu16Outlet6Config": pdu16Outlet6Config,
       "pdu16Outlet7Config": pdu16Outlet7Config,
       "pdu16Outlet8Config": pdu16Outlet8Config,
       "pdu16Threshold1": pdu16Threshold1,
       "pdu16Threshold2": pdu16Threshold2,
       "pdu16Voltage": pdu16Voltage,
       "pdu16ModelName": pdu16ModelName,
       "pdu16ModelNo": pdu16ModelNo,
       "pdu16Identify": pdu16Identify}
)
