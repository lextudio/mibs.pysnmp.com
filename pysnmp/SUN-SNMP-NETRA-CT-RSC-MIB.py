# SNMP MIB module (SUN-SNMP-NETRA-CT-RSC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUN-SNMP-NETRA-CT-RSC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:38 2024
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

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

netraCtRscMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2)
)
netraCtRscMIB.setRevisions(
        ("1900-04-18 12:00",)
)


# Types definitions



class DateAndTime(OctetString):
    """Custom type DateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetraCtRscObjs_ObjectIdentity = ObjectIdentity
netraCtRscObjs = _NetraCtRscObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1)
)
_NetraCtRscAdminObjs_ObjectIdentity = ObjectIdentity
netraCtRscAdminObjs = _NetraCtRscAdminObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 1)
)


class _NetraCtRscAdminRscReset_Type(Integer32):
    """Custom type netraCtRscAdminRscReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("notimpl", 2147483647),
          ("set", 1))
    )


_NetraCtRscAdminRscReset_Type.__name__ = "Integer32"
_NetraCtRscAdminRscReset_Object = MibScalar
netraCtRscAdminRscReset = _NetraCtRscAdminRscReset_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 1, 1),
    _NetraCtRscAdminRscReset_Type()
)
netraCtRscAdminRscReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscAdminRscReset.setStatus("current")


class _NetraCtRscAdminHostReset_Type(Integer32):
    """Custom type netraCtRscAdminHostReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("notimpl", 2147483647),
          ("set", 1))
    )


_NetraCtRscAdminHostReset_Type.__name__ = "Integer32"
_NetraCtRscAdminHostReset_Object = MibScalar
netraCtRscAdminHostReset = _NetraCtRscAdminHostReset_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 1, 2),
    _NetraCtRscAdminHostReset_Type()
)
netraCtRscAdminHostReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscAdminHostReset.setStatus("current")


class _NetraCtRscAdminXir_Type(Integer32):
    """Custom type netraCtRscAdminXir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("notimpl", 2147483647),
          ("set", 1))
    )


_NetraCtRscAdminXir_Type.__name__ = "Integer32"
_NetraCtRscAdminXir_Object = MibScalar
netraCtRscAdminXir = _NetraCtRscAdminXir_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 1, 3),
    _NetraCtRscAdminXir_Type()
)
netraCtRscAdminXir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscAdminXir.setStatus("current")


class _NetraCtRscAdminNmi_Type(Integer32):
    """Custom type netraCtRscAdminNmi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("notimpl", 2147483647),
          ("set", 1))
    )


_NetraCtRscAdminNmi_Type.__name__ = "Integer32"
_NetraCtRscAdminNmi_Object = MibScalar
netraCtRscAdminNmi = _NetraCtRscAdminNmi_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 1, 4),
    _NetraCtRscAdminNmi_Type()
)
netraCtRscAdminNmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscAdminNmi.setStatus("current")


class _NetraCtRscAdminBreak_Type(Integer32):
    """Custom type netraCtRscAdminBreak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("notimpl", 2147483647),
          ("set", 1))
    )


_NetraCtRscAdminBreak_Type.__name__ = "Integer32"
_NetraCtRscAdminBreak_Object = MibScalar
netraCtRscAdminBreak = _NetraCtRscAdminBreak_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 1, 5),
    _NetraCtRscAdminBreak_Type()
)
netraCtRscAdminBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscAdminBreak.setStatus("current")
_NetraCtRscConfigObjs_ObjectIdentity = ObjectIdentity
netraCtRscConfigObjs = _NetraCtRscConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2)
)


class _NetraCtRscGlobalPageFlag_Type(Integer32):
    """Custom type netraCtRscGlobalPageFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscGlobalPageFlag_Type.__name__ = "Integer32"
_NetraCtRscGlobalPageFlag_Object = MibScalar
netraCtRscGlobalPageFlag = _NetraCtRscGlobalPageFlag_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 1),
    _NetraCtRscGlobalPageFlag_Type()
)
netraCtRscGlobalPageFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscGlobalPageFlag.setStatus("current")


class _NetraCtRscGlobalEmailFlag_Type(Integer32):
    """Custom type netraCtRscGlobalEmailFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscGlobalEmailFlag_Type.__name__ = "Integer32"
_NetraCtRscGlobalEmailFlag_Object = MibScalar
netraCtRscGlobalEmailFlag = _NetraCtRscGlobalEmailFlag_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 2),
    _NetraCtRscGlobalEmailFlag_Type()
)
netraCtRscGlobalEmailFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscGlobalEmailFlag.setStatus("current")


class _NetraCtRscGlobalIPModeFlag_Type(Integer32):
    """Custom type netraCtRscGlobalIPModeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("dhcp", 3),
          ("disabled", 1),
          ("notimpl", 2147483647))
    )


_NetraCtRscGlobalIPModeFlag_Type.__name__ = "Integer32"
_NetraCtRscGlobalIPModeFlag_Object = MibScalar
netraCtRscGlobalIPModeFlag = _NetraCtRscGlobalIPModeFlag_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 3),
    _NetraCtRscGlobalIPModeFlag_Type()
)
netraCtRscGlobalIPModeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscGlobalIPModeFlag.setStatus("current")


class _NetraCtRscGlobalPPPFlag_Type(Integer32):
    """Custom type netraCtRscGlobalPPPFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscGlobalPPPFlag_Type.__name__ = "Integer32"
_NetraCtRscGlobalPPPFlag_Object = MibScalar
netraCtRscGlobalPPPFlag = _NetraCtRscGlobalPPPFlag_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 4),
    _NetraCtRscGlobalPPPFlag_Type()
)
netraCtRscGlobalPPPFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscGlobalPPPFlag.setStatus("current")


class _NetraCtRscHostname_Type(DisplayString):
    """Custom type netraCtRscHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NetraCtRscHostname_Type.__name__ = "DisplayString"
_NetraCtRscHostname_Object = MibScalar
netraCtRscHostname = _NetraCtRscHostname_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 5),
    _NetraCtRscHostname_Type()
)
netraCtRscHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscHostname.setStatus("current")


class _NetraCtRscCustomerInfo_Type(DisplayString):
    """Custom type netraCtRscCustomerInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NetraCtRscCustomerInfo_Type.__name__ = "DisplayString"
_NetraCtRscCustomerInfo_Object = MibScalar
netraCtRscCustomerInfo = _NetraCtRscCustomerInfo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 6),
    _NetraCtRscCustomerInfo_Type()
)
netraCtRscCustomerInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscCustomerInfo.setStatus("current")


class _NetraCtRscVersionBootMajor_Type(Integer32):
    """Custom type netraCtRscVersionBootMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetraCtRscVersionBootMajor_Type.__name__ = "Integer32"
_NetraCtRscVersionBootMajor_Object = MibScalar
netraCtRscVersionBootMajor = _NetraCtRscVersionBootMajor_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 7),
    _NetraCtRscVersionBootMajor_Type()
)
netraCtRscVersionBootMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscVersionBootMajor.setStatus("current")


class _NetraCtRscVersionBootMinor_Type(Integer32):
    """Custom type netraCtRscVersionBootMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetraCtRscVersionBootMinor_Type.__name__ = "Integer32"
_NetraCtRscVersionBootMinor_Object = MibScalar
netraCtRscVersionBootMinor = _NetraCtRscVersionBootMinor_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 8),
    _NetraCtRscVersionBootMinor_Type()
)
netraCtRscVersionBootMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscVersionBootMinor.setStatus("current")


class _NetraCtRscVersionBootMicro_Type(Integer32):
    """Custom type netraCtRscVersionBootMicro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetraCtRscVersionBootMicro_Type.__name__ = "Integer32"
_NetraCtRscVersionBootMicro_Object = MibScalar
netraCtRscVersionBootMicro = _NetraCtRscVersionBootMicro_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 9),
    _NetraCtRscVersionBootMicro_Type()
)
netraCtRscVersionBootMicro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscVersionBootMicro.setStatus("current")


class _NetraCtRscVersionMainMajor_Type(Integer32):
    """Custom type netraCtRscVersionMainMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetraCtRscVersionMainMajor_Type.__name__ = "Integer32"
_NetraCtRscVersionMainMajor_Object = MibScalar
netraCtRscVersionMainMajor = _NetraCtRscVersionMainMajor_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 10),
    _NetraCtRscVersionMainMajor_Type()
)
netraCtRscVersionMainMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscVersionMainMajor.setStatus("current")


class _NetraCtRscVersionMainMinor_Type(Integer32):
    """Custom type netraCtRscVersionMainMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetraCtRscVersionMainMinor_Type.__name__ = "Integer32"
_NetraCtRscVersionMainMinor_Object = MibScalar
netraCtRscVersionMainMinor = _NetraCtRscVersionMainMinor_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 11),
    _NetraCtRscVersionMainMinor_Type()
)
netraCtRscVersionMainMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscVersionMainMinor.setStatus("current")


class _NetraCtRscVersionMainMicro_Type(Integer32):
    """Custom type netraCtRscVersionMainMicro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetraCtRscVersionMainMicro_Type.__name__ = "Integer32"
_NetraCtRscVersionMainMicro_Object = MibScalar
netraCtRscVersionMainMicro = _NetraCtRscVersionMainMicro_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 12),
    _NetraCtRscVersionMainMicro_Type()
)
netraCtRscVersionMainMicro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscVersionMainMicro.setStatus("current")


class _NetraCtRscVersionFirmwareMajor_Type(Integer32):
    """Custom type netraCtRscVersionFirmwareMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetraCtRscVersionFirmwareMajor_Type.__name__ = "Integer32"
_NetraCtRscVersionFirmwareMajor_Object = MibScalar
netraCtRscVersionFirmwareMajor = _NetraCtRscVersionFirmwareMajor_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 13),
    _NetraCtRscVersionFirmwareMajor_Type()
)
netraCtRscVersionFirmwareMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscVersionFirmwareMajor.setStatus("current")


class _NetraCtRscVersionFirmwareMinor_Type(Integer32):
    """Custom type netraCtRscVersionFirmwareMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetraCtRscVersionFirmwareMinor_Type.__name__ = "Integer32"
_NetraCtRscVersionFirmwareMinor_Object = MibScalar
netraCtRscVersionFirmwareMinor = _NetraCtRscVersionFirmwareMinor_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 14),
    _NetraCtRscVersionFirmwareMinor_Type()
)
netraCtRscVersionFirmwareMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscVersionFirmwareMinor.setStatus("current")


class _NetraCtRscVersionFirmwareMicro_Type(Integer32):
    """Custom type netraCtRscVersionFirmwareMicro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetraCtRscVersionFirmwareMicro_Type.__name__ = "Integer32"
_NetraCtRscVersionFirmwareMicro_Object = MibScalar
netraCtRscVersionFirmwareMicro = _NetraCtRscVersionFirmwareMicro_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 15),
    _NetraCtRscVersionFirmwareMicro_Type()
)
netraCtRscVersionFirmwareMicro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscVersionFirmwareMicro.setStatus("current")
_NetraCtRscTOD_Type = DateAndTime
_NetraCtRscTOD_Object = MibScalar
netraCtRscTOD = _NetraCtRscTOD_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 16),
    _NetraCtRscTOD_Type()
)
netraCtRscTOD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscTOD.setStatus("current")


class _NetraCtRscEscape_Type(DisplayString):
    """Custom type netraCtRscEscape based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NetraCtRscEscape_Type.__name__ = "DisplayString"
_NetraCtRscEscape_Object = MibScalar
netraCtRscEscape = _NetraCtRscEscape_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 17),
    _NetraCtRscEscape_Type()
)
netraCtRscEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscEscape.setStatus("current")


class _NetraCtRscHostWatchDogReboot_Type(Integer32):
    """Custom type netraCtRscHostWatchDogReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscHostWatchDogReboot_Type.__name__ = "Integer32"
_NetraCtRscHostWatchDogReboot_Object = MibScalar
netraCtRscHostWatchDogReboot = _NetraCtRscHostWatchDogReboot_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 18),
    _NetraCtRscHostWatchDogReboot_Type()
)
netraCtRscHostWatchDogReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscHostWatchDogReboot.setStatus("current")


class _NetraCtRscHostWatchDogTimeout_Type(Integer32):
    """Custom type netraCtRscHostWatchDogTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetraCtRscHostWatchDogTimeout_Type.__name__ = "Integer32"
_NetraCtRscHostWatchDogTimeout_Object = MibScalar
netraCtRscHostWatchDogTimeout = _NetraCtRscHostWatchDogTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 19),
    _NetraCtRscHostWatchDogTimeout_Type()
)
netraCtRscHostWatchDogTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscHostWatchDogTimeout.setStatus("current")


class _NetraCtRscPanicDump_Type(Integer32):
    """Custom type netraCtRscPanicDump based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscPanicDump_Type.__name__ = "Integer32"
_NetraCtRscPanicDump_Object = MibScalar
netraCtRscPanicDump = _NetraCtRscPanicDump_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 2, 20),
    _NetraCtRscPanicDump_Type()
)
netraCtRscPanicDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscPanicDump.setStatus("current")
_NetraCtRscSerial2Objs_ObjectIdentity = ObjectIdentity
netraCtRscSerial2Objs = _NetraCtRscSerial2Objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3)
)


class _NetraCtRscSerial2Mode_Type(Integer32):
    """Custom type netraCtRscSerial2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("modem", 2),
          ("notimpl", 2147483647),
          ("rcc", 1),
          ("tty", 3))
    )


_NetraCtRscSerial2Mode_Type.__name__ = "Integer32"
_NetraCtRscSerial2Mode_Object = MibScalar
netraCtRscSerial2Mode = _NetraCtRscSerial2Mode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 1),
    _NetraCtRscSerial2Mode_Type()
)
netraCtRscSerial2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2Mode.setStatus("current")


class _NetraCtRscSerial2Parity_Type(Integer32):
    """Custom type netraCtRscSerial2Parity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("notimpl", 2147483647),
          ("odd", 2))
    )


_NetraCtRscSerial2Parity_Type.__name__ = "Integer32"
_NetraCtRscSerial2Parity_Object = MibScalar
netraCtRscSerial2Parity = _NetraCtRscSerial2Parity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 2),
    _NetraCtRscSerial2Parity_Type()
)
netraCtRscSerial2Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2Parity.setStatus("current")


class _NetraCtRscSerial2Stop_Type(Integer32):
    """Custom type netraCtRscSerial2Stop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("one", 1),
          ("two", 2))
    )


_NetraCtRscSerial2Stop_Type.__name__ = "Integer32"
_NetraCtRscSerial2Stop_Object = MibScalar
netraCtRscSerial2Stop = _NetraCtRscSerial2Stop_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 3),
    _NetraCtRscSerial2Stop_Type()
)
netraCtRscSerial2Stop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2Stop.setStatus("current")


class _NetraCtRscSerial2Data_Type(Integer32):
    """Custom type netraCtRscSerial2Data based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("eight", 2),
          ("notimpl", 2147483647),
          ("seven", 1))
    )


_NetraCtRscSerial2Data_Type.__name__ = "Integer32"
_NetraCtRscSerial2Data_Object = MibScalar
netraCtRscSerial2Data = _NetraCtRscSerial2Data_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 4),
    _NetraCtRscSerial2Data_Type()
)
netraCtRscSerial2Data.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2Data.setStatus("current")


class _NetraCtRscSerial2Baud_Type(Integer32):
    """Custom type netraCtRscSerial2Baud based on Integer32"""
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
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("b115200", 10),
          ("b1200", 2),
          ("b1800", 3),
          ("b19200", 7),
          ("b2400", 4),
          ("b300", 1),
          ("b38400", 8),
          ("b4800", 5),
          ("b57600", 9),
          ("b9600", 6),
          ("notimpl", 2147483647))
    )


_NetraCtRscSerial2Baud_Type.__name__ = "Integer32"
_NetraCtRscSerial2Baud_Object = MibScalar
netraCtRscSerial2Baud = _NetraCtRscSerial2Baud_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 5),
    _NetraCtRscSerial2Baud_Type()
)
netraCtRscSerial2Baud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2Baud.setStatus("current")


class _NetraCtRscSerial2HwFlowcontrol_Type(Integer32):
    """Custom type netraCtRscSerial2HwFlowcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscSerial2HwFlowcontrol_Type.__name__ = "Integer32"
_NetraCtRscSerial2HwFlowcontrol_Object = MibScalar
netraCtRscSerial2HwFlowcontrol = _NetraCtRscSerial2HwFlowcontrol_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 6),
    _NetraCtRscSerial2HwFlowcontrol_Type()
)
netraCtRscSerial2HwFlowcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2HwFlowcontrol.setStatus("current")


class _NetraCtRscSerial2Inactivity_Type(Integer32):
    """Custom type netraCtRscSerial2Inactivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscSerial2Inactivity_Type.__name__ = "Integer32"
_NetraCtRscSerial2Inactivity_Object = MibScalar
netraCtRscSerial2Inactivity = _NetraCtRscSerial2Inactivity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 7),
    _NetraCtRscSerial2Inactivity_Type()
)
netraCtRscSerial2Inactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2Inactivity.setStatus("current")


class _NetraCtRscSerial2PagerOneConfig_Type(DisplayString):
    """Custom type netraCtRscSerial2PagerOneConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NetraCtRscSerial2PagerOneConfig_Type.__name__ = "DisplayString"
_NetraCtRscSerial2PagerOneConfig_Object = MibScalar
netraCtRscSerial2PagerOneConfig = _NetraCtRscSerial2PagerOneConfig_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 8),
    _NetraCtRscSerial2PagerOneConfig_Type()
)
netraCtRscSerial2PagerOneConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerOneConfig.setStatus("current")


class _NetraCtRscSerial2PagerTwoConfig_Type(DisplayString):
    """Custom type netraCtRscSerial2PagerTwoConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NetraCtRscSerial2PagerTwoConfig_Type.__name__ = "DisplayString"
_NetraCtRscSerial2PagerTwoConfig_Object = MibScalar
netraCtRscSerial2PagerTwoConfig = _NetraCtRscSerial2PagerTwoConfig_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 9),
    _NetraCtRscSerial2PagerTwoConfig_Type()
)
netraCtRscSerial2PagerTwoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerTwoConfig.setStatus("current")


class _NetraCtRscSerial2PagerOneBaud_Type(Integer32):
    """Custom type netraCtRscSerial2PagerOneBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 2),
          ("b2400", 3),
          ("b300", 1),
          ("b4800", 4),
          ("b9600", 5),
          ("notimpl", 2147483647))
    )


_NetraCtRscSerial2PagerOneBaud_Type.__name__ = "Integer32"
_NetraCtRscSerial2PagerOneBaud_Object = MibScalar
netraCtRscSerial2PagerOneBaud = _NetraCtRscSerial2PagerOneBaud_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 10),
    _NetraCtRscSerial2PagerOneBaud_Type()
)
netraCtRscSerial2PagerOneBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerOneBaud.setStatus("current")


class _NetraCtRscSerial2PagerTwoBaud_Type(Integer32):
    """Custom type netraCtRscSerial2PagerTwoBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 2),
          ("b2400", 3),
          ("b300", 1),
          ("b4800", 4),
          ("b9600", 5),
          ("notimpl", 2147483647))
    )


_NetraCtRscSerial2PagerTwoBaud_Type.__name__ = "Integer32"
_NetraCtRscSerial2PagerTwoBaud_Object = MibScalar
netraCtRscSerial2PagerTwoBaud = _NetraCtRscSerial2PagerTwoBaud_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 11),
    _NetraCtRscSerial2PagerTwoBaud_Type()
)
netraCtRscSerial2PagerTwoBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerTwoBaud.setStatus("current")


class _NetraCtRscSerial2PagerOneParity_Type(Integer32):
    """Custom type netraCtRscSerial2PagerOneParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("notimpl", 2147483647),
          ("odd", 2))
    )


_NetraCtRscSerial2PagerOneParity_Type.__name__ = "Integer32"
_NetraCtRscSerial2PagerOneParity_Object = MibScalar
netraCtRscSerial2PagerOneParity = _NetraCtRscSerial2PagerOneParity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 12),
    _NetraCtRscSerial2PagerOneParity_Type()
)
netraCtRscSerial2PagerOneParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerOneParity.setStatus("current")


class _NetraCtRscSerial2PagerTwoParity_Type(Integer32):
    """Custom type netraCtRscSerial2PagerTwoParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("notimpl", 2147483647),
          ("odd", 2))
    )


_NetraCtRscSerial2PagerTwoParity_Type.__name__ = "Integer32"
_NetraCtRscSerial2PagerTwoParity_Object = MibScalar
netraCtRscSerial2PagerTwoParity = _NetraCtRscSerial2PagerTwoParity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 13),
    _NetraCtRscSerial2PagerTwoParity_Type()
)
netraCtRscSerial2PagerTwoParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerTwoParity.setStatus("current")


class _NetraCtRscSerial2PagerOneStop_Type(Integer32):
    """Custom type netraCtRscSerial2PagerOneStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("one", 1),
          ("two", 2))
    )


_NetraCtRscSerial2PagerOneStop_Type.__name__ = "Integer32"
_NetraCtRscSerial2PagerOneStop_Object = MibScalar
netraCtRscSerial2PagerOneStop = _NetraCtRscSerial2PagerOneStop_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 14),
    _NetraCtRscSerial2PagerOneStop_Type()
)
netraCtRscSerial2PagerOneStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerOneStop.setStatus("current")


class _NetraCtRscSerial2PagerTwoStop_Type(Integer32):
    """Custom type netraCtRscSerial2PagerTwoStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("one", 1),
          ("two", 2))
    )


_NetraCtRscSerial2PagerTwoStop_Type.__name__ = "Integer32"
_NetraCtRscSerial2PagerTwoStop_Object = MibScalar
netraCtRscSerial2PagerTwoStop = _NetraCtRscSerial2PagerTwoStop_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 15),
    _NetraCtRscSerial2PagerTwoStop_Type()
)
netraCtRscSerial2PagerTwoStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerTwoStop.setStatus("current")


class _NetraCtRscSerial2PagerOneData_Type(Integer32):
    """Custom type netraCtRscSerial2PagerOneData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("eight", 2),
          ("notimpl", 2147483647),
          ("seven", 1))
    )


_NetraCtRscSerial2PagerOneData_Type.__name__ = "Integer32"
_NetraCtRscSerial2PagerOneData_Object = MibScalar
netraCtRscSerial2PagerOneData = _NetraCtRscSerial2PagerOneData_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 16),
    _NetraCtRscSerial2PagerOneData_Type()
)
netraCtRscSerial2PagerOneData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerOneData.setStatus("current")


class _NetraCtRscSerial2PagerTwoData_Type(Integer32):
    """Custom type netraCtRscSerial2PagerTwoData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("eight", 2),
          ("notimpl", 2147483647),
          ("seven", 1))
    )


_NetraCtRscSerial2PagerTwoData_Type.__name__ = "Integer32"
_NetraCtRscSerial2PagerTwoData_Object = MibScalar
netraCtRscSerial2PagerTwoData = _NetraCtRscSerial2PagerTwoData_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 17),
    _NetraCtRscSerial2PagerTwoData_Type()
)
netraCtRscSerial2PagerTwoData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerTwoData.setStatus("current")


class _NetraCtRscSerial2PagerOneInit_Type(DisplayString):
    """Custom type netraCtRscSerial2PagerOneInit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_NetraCtRscSerial2PagerOneInit_Type.__name__ = "DisplayString"
_NetraCtRscSerial2PagerOneInit_Object = MibScalar
netraCtRscSerial2PagerOneInit = _NetraCtRscSerial2PagerOneInit_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 18),
    _NetraCtRscSerial2PagerOneInit_Type()
)
netraCtRscSerial2PagerOneInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerOneInit.setStatus("current")


class _NetraCtRscSerial2PagerTwoInit_Type(DisplayString):
    """Custom type netraCtRscSerial2PagerTwoInit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_NetraCtRscSerial2PagerTwoInit_Type.__name__ = "DisplayString"
_NetraCtRscSerial2PagerTwoInit_Object = MibScalar
netraCtRscSerial2PagerTwoInit = _NetraCtRscSerial2PagerTwoInit_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 19),
    _NetraCtRscSerial2PagerTwoInit_Type()
)
netraCtRscSerial2PagerTwoInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerTwoInit.setStatus("current")


class _NetraCtRscSerial2PagerOnePassword_Type(DisplayString):
    """Custom type netraCtRscSerial2PagerOnePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NetraCtRscSerial2PagerOnePassword_Type.__name__ = "DisplayString"
_NetraCtRscSerial2PagerOnePassword_Object = MibScalar
netraCtRscSerial2PagerOnePassword = _NetraCtRscSerial2PagerOnePassword_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 20),
    _NetraCtRscSerial2PagerOnePassword_Type()
)
netraCtRscSerial2PagerOnePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerOnePassword.setStatus("current")


class _NetraCtRscSerial2PagerTwoPassword_Type(DisplayString):
    """Custom type netraCtRscSerial2PagerTwoPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NetraCtRscSerial2PagerTwoPassword_Type.__name__ = "DisplayString"
_NetraCtRscSerial2PagerTwoPassword_Object = MibScalar
netraCtRscSerial2PagerTwoPassword = _NetraCtRscSerial2PagerTwoPassword_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 3, 21),
    _NetraCtRscSerial2PagerTwoPassword_Type()
)
netraCtRscSerial2PagerTwoPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSerial2PagerTwoPassword.setStatus("current")
_NetraCtRscModemObjs_ObjectIdentity = ObjectIdentity
netraCtRscModemObjs = _NetraCtRscModemObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 4)
)


class _NetraCtRscModemParity_Type(Integer32):
    """Custom type netraCtRscModemParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("notimpl", 2147483647),
          ("odd", 2))
    )


_NetraCtRscModemParity_Type.__name__ = "Integer32"
_NetraCtRscModemParity_Object = MibScalar
netraCtRscModemParity = _NetraCtRscModemParity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 4, 1),
    _NetraCtRscModemParity_Type()
)
netraCtRscModemParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscModemParity.setStatus("current")


class _NetraCtRscModemStop_Type(Integer32):
    """Custom type netraCtRscModemStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("one", 1),
          ("two", 2))
    )


_NetraCtRscModemStop_Type.__name__ = "Integer32"
_NetraCtRscModemStop_Object = MibScalar
netraCtRscModemStop = _NetraCtRscModemStop_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 4, 2),
    _NetraCtRscModemStop_Type()
)
netraCtRscModemStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscModemStop.setStatus("current")


class _NetraCtRscModemData_Type(Integer32):
    """Custom type netraCtRscModemData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("eight", 2),
          ("notimpl", 2147483647),
          ("seven", 1))
    )


_NetraCtRscModemData_Type.__name__ = "Integer32"
_NetraCtRscModemData_Object = MibScalar
netraCtRscModemData = _NetraCtRscModemData_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 4, 3),
    _NetraCtRscModemData_Type()
)
netraCtRscModemData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscModemData.setStatus("current")


class _NetraCtRscCountryCode_Type(Integer32):
    """Custom type netraCtRscCountryCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetraCtRscCountryCode_Type.__name__ = "Integer32"
_NetraCtRscCountryCode_Object = MibScalar
netraCtRscCountryCode = _NetraCtRscCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 4, 4),
    _NetraCtRscCountryCode_Type()
)
netraCtRscCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscCountryCode.setStatus("current")


class _NetraCtRscModemModel_Type(DisplayString):
    """Custom type netraCtRscModemModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NetraCtRscModemModel_Type.__name__ = "DisplayString"
_NetraCtRscModemModel_Object = MibScalar
netraCtRscModemModel = _NetraCtRscModemModel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 4, 5),
    _NetraCtRscModemModel_Type()
)
netraCtRscModemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscModemModel.setStatus("current")
_NetraCtRscEnetObjs_ObjectIdentity = ObjectIdentity
netraCtRscEnetObjs = _NetraCtRscEnetObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 5)
)
_NetraCtRscMacAddress_Type = MacAddress
_NetraCtRscMacAddress_Object = MibScalar
netraCtRscMacAddress = _NetraCtRscMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 5, 1),
    _NetraCtRscMacAddress_Type()
)
netraCtRscMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscMacAddress.setStatus("current")


class _NetraCtRscEnetTpeLinkTest_Type(Integer32):
    """Custom type netraCtRscEnetTpeLinkTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscEnetTpeLinkTest_Type.__name__ = "Integer32"
_NetraCtRscEnetTpeLinkTest_Object = MibScalar
netraCtRscEnetTpeLinkTest = _NetraCtRscEnetTpeLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 5, 2),
    _NetraCtRscEnetTpeLinkTest_Type()
)
netraCtRscEnetTpeLinkTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscEnetTpeLinkTest.setStatus("current")
_NetraCtRscIPAddress_Type = IpAddress
_NetraCtRscIPAddress_Object = MibScalar
netraCtRscIPAddress = _NetraCtRscIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 5, 3),
    _NetraCtRscIPAddress_Type()
)
netraCtRscIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscIPAddress.setStatus("current")
_NetraCtRscIpMask_Type = IpAddress
_NetraCtRscIpMask_Object = MibScalar
netraCtRscIpMask = _NetraCtRscIpMask_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 5, 4),
    _NetraCtRscIpMask_Type()
)
netraCtRscIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscIpMask.setStatus("current")
_NetraCtRscIpGateway_Type = IpAddress
_NetraCtRscIpGateway_Object = MibScalar
netraCtRscIpGateway = _NetraCtRscIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 5, 5),
    _NetraCtRscIpGateway_Type()
)
netraCtRscIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscIpGateway.setStatus("current")
_NetraCtRscSNMPHostAddress_Type = IpAddress
_NetraCtRscSNMPHostAddress_Object = MibScalar
netraCtRscSNMPHostAddress = _NetraCtRscSNMPHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 5, 6),
    _NetraCtRscSNMPHostAddress_Type()
)
netraCtRscSNMPHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscSNMPHostAddress.setStatus("current")
_NetraCtRscMailHostAddress_Type = IpAddress
_NetraCtRscMailHostAddress_Object = MibScalar
netraCtRscMailHostAddress = _NetraCtRscMailHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 5, 7),
    _NetraCtRscMailHostAddress_Type()
)
netraCtRscMailHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscMailHostAddress.setStatus("current")


class _NetraCtRscMailUser_Type(DisplayString):
    """Custom type netraCtRscMailUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NetraCtRscMailUser_Type.__name__ = "DisplayString"
_NetraCtRscMailUser_Object = MibScalar
netraCtRscMailUser = _NetraCtRscMailUser_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 5, 8),
    _NetraCtRscMailUser_Type()
)
netraCtRscMailUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscMailUser.setStatus("current")
_NetraCtRscPPPLocalIP_Type = IpAddress
_NetraCtRscPPPLocalIP_Object = MibScalar
netraCtRscPPPLocalIP = _NetraCtRscPPPLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 5, 9),
    _NetraCtRscPPPLocalIP_Type()
)
netraCtRscPPPLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscPPPLocalIP.setStatus("current")
_NetraCtRscPPPRemoteIP_Type = IpAddress
_NetraCtRscPPPRemoteIP_Object = MibScalar
netraCtRscPPPRemoteIP = _NetraCtRscPPPRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 5, 10),
    _NetraCtRscPPPRemoteIP_Type()
)
netraCtRscPPPRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscPPPRemoteIP.setStatus("current")
_NetraCtRscMailHostAddressBackup_Type = IpAddress
_NetraCtRscMailHostAddressBackup_Object = MibScalar
netraCtRscMailHostAddressBackup = _NetraCtRscMailHostAddressBackup_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 5, 11),
    _NetraCtRscMailHostAddressBackup_Type()
)
netraCtRscMailHostAddressBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscMailHostAddressBackup.setStatus("current")
_NetraCtRscEnvObjs_ObjectIdentity = ObjectIdentity
netraCtRscEnvObjs = _NetraCtRscEnvObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6)
)


class _NetraCtRscSystemType_Type(DisplayString):
    """Custom type netraCtRscSystemType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_NetraCtRscSystemType_Type.__name__ = "DisplayString"
_NetraCtRscSystemType_Object = MibScalar
netraCtRscSystemType = _NetraCtRscSystemType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 1),
    _NetraCtRscSystemType_Type()
)
netraCtRscSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscSystemType.setStatus("current")


class _NetraCtRscPowerSupplyCount_Type(Integer32):
    """Custom type netraCtRscPowerSupplyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NetraCtRscPowerSupplyCount_Type.__name__ = "Integer32"
_NetraCtRscPowerSupplyCount_Object = MibScalar
netraCtRscPowerSupplyCount = _NetraCtRscPowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 2),
    _NetraCtRscPowerSupplyCount_Type()
)
netraCtRscPowerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscPowerSupplyCount.setStatus("current")
_NetraCtRscPowerSupplyTable_Object = MibTable
netraCtRscPowerSupplyTable = _NetraCtRscPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    netraCtRscPowerSupplyTable.setStatus("current")
_NetraCtRscPowerSupplyEntry_Object = MibTableRow
netraCtRscPowerSupplyEntry = _NetraCtRscPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 3, 1)
)
netraCtRscPowerSupplyEntry.setIndexNames(
    (0, "SUN-SNMP-NETRA-CT-RSC-MIB", "netraCtRscPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    netraCtRscPowerSupplyEntry.setStatus("current")


class _NetraCtRscPowerSupplyIndex_Type(Integer32):
    """Custom type netraCtRscPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_NetraCtRscPowerSupplyIndex_Type.__name__ = "Integer32"
_NetraCtRscPowerSupplyIndex_Object = MibTableColumn
netraCtRscPowerSupplyIndex = _NetraCtRscPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 3, 1, 1),
    _NetraCtRscPowerSupplyIndex_Type()
)
netraCtRscPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscPowerSupplyIndex.setStatus("current")


class _NetraCtRscPowerSupplyPresent_Type(Integer32):
    """Custom type netraCtRscPowerSupplyPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notimpl", 2147483647),
          ("true", 1),
          ("unknown", 3))
    )


_NetraCtRscPowerSupplyPresent_Type.__name__ = "Integer32"
_NetraCtRscPowerSupplyPresent_Object = MibTableColumn
netraCtRscPowerSupplyPresent = _NetraCtRscPowerSupplyPresent_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 3, 1, 2),
    _NetraCtRscPowerSupplyPresent_Type()
)
netraCtRscPowerSupplyPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscPowerSupplyPresent.setStatus("current")


class _NetraCtRscPowerSupplyOperState_Type(Integer32):
    """Custom type netraCtRscPowerSupplyOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("notimpl", 2147483647),
          ("offline", 4),
          ("okay", 1),
          ("unknown", 3))
    )


_NetraCtRscPowerSupplyOperState_Type.__name__ = "Integer32"
_NetraCtRscPowerSupplyOperState_Object = MibTableColumn
netraCtRscPowerSupplyOperState = _NetraCtRscPowerSupplyOperState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 3, 1, 3),
    _NetraCtRscPowerSupplyOperState_Type()
)
netraCtRscPowerSupplyOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscPowerSupplyOperState.setStatus("current")


class _NetraCtRscPowerSupplyAdminState_Type(Integer32):
    """Custom type netraCtRscPowerSupplyAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscPowerSupplyAdminState_Type.__name__ = "Integer32"
_NetraCtRscPowerSupplyAdminState_Object = MibTableColumn
netraCtRscPowerSupplyAdminState = _NetraCtRscPowerSupplyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 3, 1, 4),
    _NetraCtRscPowerSupplyAdminState_Type()
)
netraCtRscPowerSupplyAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscPowerSupplyAdminState.setStatus("current")


class _NetraCtRscAlarmCount_Type(Integer32):
    """Custom type netraCtRscAlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NetraCtRscAlarmCount_Type.__name__ = "Integer32"
_NetraCtRscAlarmCount_Object = MibScalar
netraCtRscAlarmCount = _NetraCtRscAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 4),
    _NetraCtRscAlarmCount_Type()
)
netraCtRscAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscAlarmCount.setStatus("current")
_NetraCtRscAlarmTable_Object = MibTable
netraCtRscAlarmTable = _NetraCtRscAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 5)
)
if mibBuilder.loadTexts:
    netraCtRscAlarmTable.setStatus("current")
_NetraCtRscAlarmEntry_Object = MibTableRow
netraCtRscAlarmEntry = _NetraCtRscAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 5, 1)
)
netraCtRscAlarmEntry.setIndexNames(
    (0, "SUN-SNMP-NETRA-CT-RSC-MIB", "netraCtRscAlarmIndex"),
)
if mibBuilder.loadTexts:
    netraCtRscAlarmEntry.setStatus("current")


class _NetraCtRscAlarmIndex_Type(Integer32):
    """Custom type netraCtRscAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_NetraCtRscAlarmIndex_Type.__name__ = "Integer32"
_NetraCtRscAlarmIndex_Object = MibTableColumn
netraCtRscAlarmIndex = _NetraCtRscAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 5, 1, 1),
    _NetraCtRscAlarmIndex_Type()
)
netraCtRscAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netraCtRscAlarmIndex.setStatus("current")


class _NetraCtRscAlarmID_Type(Integer32):
    """Custom type netraCtRscAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NetraCtRscAlarmID_Type.__name__ = "Integer32"
_NetraCtRscAlarmID_Object = MibTableColumn
netraCtRscAlarmID = _NetraCtRscAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 5, 1, 2),
    _NetraCtRscAlarmID_Type()
)
netraCtRscAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscAlarmID.setStatus("current")


class _NetraCtRscAlarmOperState_Type(Integer32):
    """Custom type netraCtRscAlarmOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscAlarmOperState_Type.__name__ = "Integer32"
_NetraCtRscAlarmOperState_Object = MibTableColumn
netraCtRscAlarmOperState = _NetraCtRscAlarmOperState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 5, 1, 3),
    _NetraCtRscAlarmOperState_Type()
)
netraCtRscAlarmOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscAlarmOperState.setStatus("current")


class _NetraCtRscAlarmAdminState_Type(Integer32):
    """Custom type netraCtRscAlarmAdminState based on Integer32"""
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


_NetraCtRscAlarmAdminState_Type.__name__ = "Integer32"
_NetraCtRscAlarmAdminState_Object = MibTableColumn
netraCtRscAlarmAdminState = _NetraCtRscAlarmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 5, 1, 4),
    _NetraCtRscAlarmAdminState_Type()
)
netraCtRscAlarmAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscAlarmAdminState.setStatus("current")


class _NetraCtRscAlarmPrefix_Type(Integer32):
    """Custom type netraCtRscAlarmPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetraCtRscAlarmPrefix_Type.__name__ = "Integer32"
_NetraCtRscAlarmPrefix_Object = MibTableColumn
netraCtRscAlarmPrefix = _NetraCtRscAlarmPrefix_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 5, 1, 5),
    _NetraCtRscAlarmPrefix_Type()
)
netraCtRscAlarmPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscAlarmPrefix.setStatus("current")


class _NetraCtRscFanCount_Type(Integer32):
    """Custom type netraCtRscFanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NetraCtRscFanCount_Type.__name__ = "Integer32"
_NetraCtRscFanCount_Object = MibScalar
netraCtRscFanCount = _NetraCtRscFanCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 6),
    _NetraCtRscFanCount_Type()
)
netraCtRscFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscFanCount.setStatus("current")
_NetraCtRscFanTable_Object = MibTable
netraCtRscFanTable = _NetraCtRscFanTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 7)
)
if mibBuilder.loadTexts:
    netraCtRscFanTable.setStatus("current")
_NetraCtRscFanEntry_Object = MibTableRow
netraCtRscFanEntry = _NetraCtRscFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 7, 1)
)
netraCtRscFanEntry.setIndexNames(
    (0, "SUN-SNMP-NETRA-CT-RSC-MIB", "netraCtRscFanIndex"),
)
if mibBuilder.loadTexts:
    netraCtRscFanEntry.setStatus("current")


class _NetraCtRscFanIndex_Type(Integer32):
    """Custom type netraCtRscFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_NetraCtRscFanIndex_Type.__name__ = "Integer32"
_NetraCtRscFanIndex_Object = MibTableColumn
netraCtRscFanIndex = _NetraCtRscFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 7, 1, 1),
    _NetraCtRscFanIndex_Type()
)
netraCtRscFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscFanIndex.setStatus("current")


class _NetraCtRscFanPresent_Type(Integer32):
    """Custom type netraCtRscFanPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notimpl", 2147483647),
          ("true", 1),
          ("unknown", 3))
    )


_NetraCtRscFanPresent_Type.__name__ = "Integer32"
_NetraCtRscFanPresent_Object = MibTableColumn
netraCtRscFanPresent = _NetraCtRscFanPresent_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 7, 1, 2),
    _NetraCtRscFanPresent_Type()
)
netraCtRscFanPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscFanPresent.setStatus("current")


class _NetraCtRscFanStatus_Type(Integer32):
    """Custom type netraCtRscFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("notimpl", 2147483647),
          ("okay", 1),
          ("unknown", 3))
    )


_NetraCtRscFanStatus_Type.__name__ = "Integer32"
_NetraCtRscFanStatus_Object = MibTableColumn
netraCtRscFanStatus = _NetraCtRscFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 7, 1, 3),
    _NetraCtRscFanStatus_Type()
)
netraCtRscFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscFanStatus.setStatus("current")


class _NetraCtRscTemperatureCount_Type(Integer32):
    """Custom type netraCtRscTemperatureCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NetraCtRscTemperatureCount_Type.__name__ = "Integer32"
_NetraCtRscTemperatureCount_Object = MibScalar
netraCtRscTemperatureCount = _NetraCtRscTemperatureCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 8),
    _NetraCtRscTemperatureCount_Type()
)
netraCtRscTemperatureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscTemperatureCount.setStatus("current")
_NetraCtRscTemperatureTable_Object = MibTable
netraCtRscTemperatureTable = _NetraCtRscTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 9)
)
if mibBuilder.loadTexts:
    netraCtRscTemperatureTable.setStatus("current")
_NetraCtRscTemperatureEntry_Object = MibTableRow
netraCtRscTemperatureEntry = _NetraCtRscTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 9, 1)
)
netraCtRscTemperatureEntry.setIndexNames(
    (0, "SUN-SNMP-NETRA-CT-RSC-MIB", "netraCtRscTemperatureIndex"),
)
if mibBuilder.loadTexts:
    netraCtRscTemperatureEntry.setStatus("current")


class _NetraCtRscTemperatureIndex_Type(Integer32):
    """Custom type netraCtRscTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_NetraCtRscTemperatureIndex_Type.__name__ = "Integer32"
_NetraCtRscTemperatureIndex_Object = MibTableColumn
netraCtRscTemperatureIndex = _NetraCtRscTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 9, 1, 1),
    _NetraCtRscTemperatureIndex_Type()
)
netraCtRscTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscTemperatureIndex.setStatus("current")


class _NetraCtRscTemperatureValid_Type(Integer32):
    """Custom type netraCtRscTemperatureValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_NetraCtRscTemperatureValid_Type.__name__ = "Integer32"
_NetraCtRscTemperatureValid_Object = MibTableColumn
netraCtRscTemperatureValid = _NetraCtRscTemperatureValid_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 9, 1, 2),
    _NetraCtRscTemperatureValid_Type()
)
netraCtRscTemperatureValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscTemperatureValid.setStatus("current")


class _NetraCtRscTemperatureValue_Type(Integer32):
    """Custom type netraCtRscTemperatureValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NetraCtRscTemperatureValue_Type.__name__ = "Integer32"
_NetraCtRscTemperatureValue_Object = MibTableColumn
netraCtRscTemperatureValue = _NetraCtRscTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 9, 1, 3),
    _NetraCtRscTemperatureValue_Type()
)
netraCtRscTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscTemperatureValue.setStatus("current")


class _NetraCtRscTemperatureLowWarn_Type(Integer32):
    """Custom type netraCtRscTemperatureLowWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NetraCtRscTemperatureLowWarn_Type.__name__ = "Integer32"
_NetraCtRscTemperatureLowWarn_Object = MibTableColumn
netraCtRscTemperatureLowWarn = _NetraCtRscTemperatureLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 9, 1, 4),
    _NetraCtRscTemperatureLowWarn_Type()
)
netraCtRscTemperatureLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscTemperatureLowWarn.setStatus("current")


class _NetraCtRscTemperatureHighWarn_Type(Integer32):
    """Custom type netraCtRscTemperatureHighWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NetraCtRscTemperatureHighWarn_Type.__name__ = "Integer32"
_NetraCtRscTemperatureHighWarn_Object = MibTableColumn
netraCtRscTemperatureHighWarn = _NetraCtRscTemperatureHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 9, 1, 5),
    _NetraCtRscTemperatureHighWarn_Type()
)
netraCtRscTemperatureHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscTemperatureHighWarn.setStatus("current")


class _NetraCtRscTemperatureDesc_Type(DisplayString):
    """Custom type netraCtRscTemperatureDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NetraCtRscTemperatureDesc_Type.__name__ = "DisplayString"
_NetraCtRscTemperatureDesc_Object = MibTableColumn
netraCtRscTemperatureDesc = _NetraCtRscTemperatureDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 6, 9, 1, 6),
    _NetraCtRscTemperatureDesc_Type()
)
netraCtRscTemperatureDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscTemperatureDesc.setStatus("current")
_NetraCtRscLogObjs_ObjectIdentity = ObjectIdentity
netraCtRscLogObjs = _NetraCtRscLogObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7)
)


class _NetraCtRscEventLogCount_Type(Integer32):
    """Custom type netraCtRscEventLogCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetraCtRscEventLogCount_Type.__name__ = "Integer32"
_NetraCtRscEventLogCount_Object = MibScalar
netraCtRscEventLogCount = _NetraCtRscEventLogCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 1),
    _NetraCtRscEventLogCount_Type()
)
netraCtRscEventLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscEventLogCount.setStatus("current")
_NetraCtRscEventLogTable_Object = MibTable
netraCtRscEventLogTable = _NetraCtRscEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    netraCtRscEventLogTable.setStatus("current")
_NetraCtRscEventLogEntry_Object = MibTableRow
netraCtRscEventLogEntry = _NetraCtRscEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 2, 1)
)
netraCtRscEventLogEntry.setIndexNames(
    (0, "SUN-SNMP-NETRA-CT-RSC-MIB", "netraCtRscEventLogIndex"),
)
if mibBuilder.loadTexts:
    netraCtRscEventLogEntry.setStatus("current")


class _NetraCtRscEventLogIndex_Type(Integer32):
    """Custom type netraCtRscEventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetraCtRscEventLogIndex_Type.__name__ = "Integer32"
_NetraCtRscEventLogIndex_Object = MibTableColumn
netraCtRscEventLogIndex = _NetraCtRscEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 2, 1, 1),
    _NetraCtRscEventLogIndex_Type()
)
netraCtRscEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscEventLogIndex.setStatus("current")
_NetraCtRscEventLogTimeStamp_Type = DateAndTime
_NetraCtRscEventLogTimeStamp_Object = MibTableColumn
netraCtRscEventLogTimeStamp = _NetraCtRscEventLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 2, 1, 2),
    _NetraCtRscEventLogTimeStamp_Type()
)
netraCtRscEventLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscEventLogTimeStamp.setStatus("current")


class _NetraCtRscEventLogMessage_Type(DisplayString):
    """Custom type netraCtRscEventLogMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NetraCtRscEventLogMessage_Type.__name__ = "DisplayString"
_NetraCtRscEventLogMessage_Object = MibTableColumn
netraCtRscEventLogMessage = _NetraCtRscEventLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 2, 1, 3),
    _NetraCtRscEventLogMessage_Type()
)
netraCtRscEventLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscEventLogMessage.setStatus("current")


class _NetraCtRscOrigConsoleLogCount_Type(Integer32):
    """Custom type netraCtRscOrigConsoleLogCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetraCtRscOrigConsoleLogCount_Type.__name__ = "Integer32"
_NetraCtRscOrigConsoleLogCount_Object = MibScalar
netraCtRscOrigConsoleLogCount = _NetraCtRscOrigConsoleLogCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 3),
    _NetraCtRscOrigConsoleLogCount_Type()
)
netraCtRscOrigConsoleLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscOrigConsoleLogCount.setStatus("current")
_NetraCtRscOrigConsoleLogTable_Object = MibTable
netraCtRscOrigConsoleLogTable = _NetraCtRscOrigConsoleLogTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    netraCtRscOrigConsoleLogTable.setStatus("current")
_NetraCtRscOrigConsoleLogEntry_Object = MibTableRow
netraCtRscOrigConsoleLogEntry = _NetraCtRscOrigConsoleLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 4, 1)
)
netraCtRscOrigConsoleLogEntry.setIndexNames(
    (0, "SUN-SNMP-NETRA-CT-RSC-MIB", "netraCtRscOrigConsoleLogIndex"),
)
if mibBuilder.loadTexts:
    netraCtRscOrigConsoleLogEntry.setStatus("current")


class _NetraCtRscOrigConsoleLogIndex_Type(Integer32):
    """Custom type netraCtRscOrigConsoleLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetraCtRscOrigConsoleLogIndex_Type.__name__ = "Integer32"
_NetraCtRscOrigConsoleLogIndex_Object = MibTableColumn
netraCtRscOrigConsoleLogIndex = _NetraCtRscOrigConsoleLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 4, 1, 1),
    _NetraCtRscOrigConsoleLogIndex_Type()
)
netraCtRscOrigConsoleLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscOrigConsoleLogIndex.setStatus("current")
_NetraCtRscOrigConsoleLogTimeStamp_Type = DateAndTime
_NetraCtRscOrigConsoleLogTimeStamp_Object = MibTableColumn
netraCtRscOrigConsoleLogTimeStamp = _NetraCtRscOrigConsoleLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 4, 1, 2),
    _NetraCtRscOrigConsoleLogTimeStamp_Type()
)
netraCtRscOrigConsoleLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscOrigConsoleLogTimeStamp.setStatus("current")


class _NetraCtRscOrigConsoleLogMessage_Type(DisplayString):
    """Custom type netraCtRscOrigConsoleLogMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NetraCtRscOrigConsoleLogMessage_Type.__name__ = "DisplayString"
_NetraCtRscOrigConsoleLogMessage_Object = MibTableColumn
netraCtRscOrigConsoleLogMessage = _NetraCtRscOrigConsoleLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 4, 1, 3),
    _NetraCtRscOrigConsoleLogMessage_Type()
)
netraCtRscOrigConsoleLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscOrigConsoleLogMessage.setStatus("current")


class _NetraCtRscConsoleLogCount_Type(Integer32):
    """Custom type netraCtRscConsoleLogCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetraCtRscConsoleLogCount_Type.__name__ = "Integer32"
_NetraCtRscConsoleLogCount_Object = MibScalar
netraCtRscConsoleLogCount = _NetraCtRscConsoleLogCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 5),
    _NetraCtRscConsoleLogCount_Type()
)
netraCtRscConsoleLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscConsoleLogCount.setStatus("current")
_NetraCtRscConsoleLogTable_Object = MibTable
netraCtRscConsoleLogTable = _NetraCtRscConsoleLogTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 6)
)
if mibBuilder.loadTexts:
    netraCtRscConsoleLogTable.setStatus("current")
_NetraCtRscConsoleLogEntry_Object = MibTableRow
netraCtRscConsoleLogEntry = _NetraCtRscConsoleLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 6, 1)
)
netraCtRscConsoleLogEntry.setIndexNames(
    (0, "SUN-SNMP-NETRA-CT-RSC-MIB", "netraCtRscConsoleLogIndex"),
)
if mibBuilder.loadTexts:
    netraCtRscConsoleLogEntry.setStatus("current")


class _NetraCtRscConsoleLogIndex_Type(Integer32):
    """Custom type netraCtRscConsoleLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NetraCtRscConsoleLogIndex_Type.__name__ = "Integer32"
_NetraCtRscConsoleLogIndex_Object = MibTableColumn
netraCtRscConsoleLogIndex = _NetraCtRscConsoleLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 6, 1, 1),
    _NetraCtRscConsoleLogIndex_Type()
)
netraCtRscConsoleLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscConsoleLogIndex.setStatus("current")
_NetraCtRscConsoleLogTimeStamp_Type = DateAndTime
_NetraCtRscConsoleLogTimeStamp_Object = MibTableColumn
netraCtRscConsoleLogTimeStamp = _NetraCtRscConsoleLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 6, 1, 2),
    _NetraCtRscConsoleLogTimeStamp_Type()
)
netraCtRscConsoleLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscConsoleLogTimeStamp.setStatus("current")


class _NetraCtRscConsoleLogMessage_Type(DisplayString):
    """Custom type netraCtRscConsoleLogMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NetraCtRscConsoleLogMessage_Type.__name__ = "DisplayString"
_NetraCtRscConsoleLogMessage_Object = MibTableColumn
netraCtRscConsoleLogMessage = _NetraCtRscConsoleLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 6, 1, 3),
    _NetraCtRscConsoleLogMessage_Type()
)
netraCtRscConsoleLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netraCtRscConsoleLogMessage.setStatus("current")


class _NetraCtRscConsoleReset_Type(Integer32):
    """Custom type netraCtRscConsoleReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("set", 1))
    )


_NetraCtRscConsoleReset_Type.__name__ = "Integer32"
_NetraCtRscConsoleReset_Object = MibScalar
netraCtRscConsoleReset = _NetraCtRscConsoleReset_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 1, 7, 7),
    _NetraCtRscConsoleReset_Type()
)
netraCtRscConsoleReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscConsoleReset.setStatus("current")
_NetraCtRscEvents_ObjectIdentity = ObjectIdentity
netraCtRscEvents = _NetraCtRscEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 2)
)
_NetraCtRscTrapPrefix_ObjectIdentity = ObjectIdentity
netraCtRscTrapPrefix = _NetraCtRscTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 2, 0)
)
_NetraCtRscExpmnt_ObjectIdentity = ObjectIdentity
netraCtRscExpmnt = _NetraCtRscExpmnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 3)
)
_NetraCtRscRccConfig_ObjectIdentity = ObjectIdentity
netraCtRscRccConfig = _NetraCtRscRccConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 3, 1)
)


class _NetraCtRscRCCPowerOnEnable_Type(Integer32):
    """Custom type netraCtRscRCCPowerOnEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscRCCPowerOnEnable_Type.__name__ = "Integer32"
_NetraCtRscRCCPowerOnEnable_Object = MibScalar
netraCtRscRCCPowerOnEnable = _NetraCtRscRCCPowerOnEnable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 3, 1, 1),
    _NetraCtRscRCCPowerOnEnable_Type()
)
netraCtRscRCCPowerOnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscRCCPowerOnEnable.setStatus("current")


class _NetraCtRscRCCPowerOffEnable_Type(Integer32):
    """Custom type netraCtRscRCCPowerOffEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscRCCPowerOffEnable_Type.__name__ = "Integer32"
_NetraCtRscRCCPowerOffEnable_Object = MibScalar
netraCtRscRCCPowerOffEnable = _NetraCtRscRCCPowerOffEnable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 3, 1, 2),
    _NetraCtRscRCCPowerOffEnable_Type()
)
netraCtRscRCCPowerOffEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscRCCPowerOffEnable.setStatus("current")


class _NetraCtRscRCCResetEnable_Type(Integer32):
    """Custom type netraCtRscRCCResetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notimpl", 2147483647),
          ("off", 2),
          ("on", 1))
    )


_NetraCtRscRCCResetEnable_Type.__name__ = "Integer32"
_NetraCtRscRCCResetEnable_Object = MibScalar
netraCtRscRCCResetEnable = _NetraCtRscRCCResetEnable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 3, 1, 3),
    _NetraCtRscRCCResetEnable_Type()
)
netraCtRscRCCResetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscRCCResetEnable.setStatus("current")


class _NetraCtRscRCCLinkNum_Type(DisplayString):
    """Custom type netraCtRscRCCLinkNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NetraCtRscRCCLinkNum_Type.__name__ = "DisplayString"
_NetraCtRscRCCLinkNum_Object = MibScalar
netraCtRscRCCLinkNum = _NetraCtRscRCCLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 3, 1, 4),
    _NetraCtRscRCCLinkNum_Type()
)
netraCtRscRCCLinkNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netraCtRscRCCLinkNum.setStatus("current")

# Managed Objects groups


# Notification objects

netraCtRscEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 65, 2, 2, 0, 1)
)
netraCtRscEvent.setObjects(
      *(("SUN-SNMP-NETRA-CT-RSC-MIB", "netraCtRscAlarmID"),
        ("SUN-SNMP-NETRA-CT-RSC-MIB", "netraCtRscAlarmOperState"),
        ("SUN-SNMP-NETRA-CT-RSC-MIB", "netraCtRscAlarmPrefix"))
)
if mibBuilder.loadTexts:
    netraCtRscEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUN-SNMP-NETRA-CT-RSC-MIB",
    **{"DateAndTime": DateAndTime,
       "netraCtRscMIB": netraCtRscMIB,
       "netraCtRscObjs": netraCtRscObjs,
       "netraCtRscAdminObjs": netraCtRscAdminObjs,
       "netraCtRscAdminRscReset": netraCtRscAdminRscReset,
       "netraCtRscAdminHostReset": netraCtRscAdminHostReset,
       "netraCtRscAdminXir": netraCtRscAdminXir,
       "netraCtRscAdminNmi": netraCtRscAdminNmi,
       "netraCtRscAdminBreak": netraCtRscAdminBreak,
       "netraCtRscConfigObjs": netraCtRscConfigObjs,
       "netraCtRscGlobalPageFlag": netraCtRscGlobalPageFlag,
       "netraCtRscGlobalEmailFlag": netraCtRscGlobalEmailFlag,
       "netraCtRscGlobalIPModeFlag": netraCtRscGlobalIPModeFlag,
       "netraCtRscGlobalPPPFlag": netraCtRscGlobalPPPFlag,
       "netraCtRscHostname": netraCtRscHostname,
       "netraCtRscCustomerInfo": netraCtRscCustomerInfo,
       "netraCtRscVersionBootMajor": netraCtRscVersionBootMajor,
       "netraCtRscVersionBootMinor": netraCtRscVersionBootMinor,
       "netraCtRscVersionBootMicro": netraCtRscVersionBootMicro,
       "netraCtRscVersionMainMajor": netraCtRscVersionMainMajor,
       "netraCtRscVersionMainMinor": netraCtRscVersionMainMinor,
       "netraCtRscVersionMainMicro": netraCtRscVersionMainMicro,
       "netraCtRscVersionFirmwareMajor": netraCtRscVersionFirmwareMajor,
       "netraCtRscVersionFirmwareMinor": netraCtRscVersionFirmwareMinor,
       "netraCtRscVersionFirmwareMicro": netraCtRscVersionFirmwareMicro,
       "netraCtRscTOD": netraCtRscTOD,
       "netraCtRscEscape": netraCtRscEscape,
       "netraCtRscHostWatchDogReboot": netraCtRscHostWatchDogReboot,
       "netraCtRscHostWatchDogTimeout": netraCtRscHostWatchDogTimeout,
       "netraCtRscPanicDump": netraCtRscPanicDump,
       "netraCtRscSerial2Objs": netraCtRscSerial2Objs,
       "netraCtRscSerial2Mode": netraCtRscSerial2Mode,
       "netraCtRscSerial2Parity": netraCtRscSerial2Parity,
       "netraCtRscSerial2Stop": netraCtRscSerial2Stop,
       "netraCtRscSerial2Data": netraCtRscSerial2Data,
       "netraCtRscSerial2Baud": netraCtRscSerial2Baud,
       "netraCtRscSerial2HwFlowcontrol": netraCtRscSerial2HwFlowcontrol,
       "netraCtRscSerial2Inactivity": netraCtRscSerial2Inactivity,
       "netraCtRscSerial2PagerOneConfig": netraCtRscSerial2PagerOneConfig,
       "netraCtRscSerial2PagerTwoConfig": netraCtRscSerial2PagerTwoConfig,
       "netraCtRscSerial2PagerOneBaud": netraCtRscSerial2PagerOneBaud,
       "netraCtRscSerial2PagerTwoBaud": netraCtRscSerial2PagerTwoBaud,
       "netraCtRscSerial2PagerOneParity": netraCtRscSerial2PagerOneParity,
       "netraCtRscSerial2PagerTwoParity": netraCtRscSerial2PagerTwoParity,
       "netraCtRscSerial2PagerOneStop": netraCtRscSerial2PagerOneStop,
       "netraCtRscSerial2PagerTwoStop": netraCtRscSerial2PagerTwoStop,
       "netraCtRscSerial2PagerOneData": netraCtRscSerial2PagerOneData,
       "netraCtRscSerial2PagerTwoData": netraCtRscSerial2PagerTwoData,
       "netraCtRscSerial2PagerOneInit": netraCtRscSerial2PagerOneInit,
       "netraCtRscSerial2PagerTwoInit": netraCtRscSerial2PagerTwoInit,
       "netraCtRscSerial2PagerOnePassword": netraCtRscSerial2PagerOnePassword,
       "netraCtRscSerial2PagerTwoPassword": netraCtRscSerial2PagerTwoPassword,
       "netraCtRscModemObjs": netraCtRscModemObjs,
       "netraCtRscModemParity": netraCtRscModemParity,
       "netraCtRscModemStop": netraCtRscModemStop,
       "netraCtRscModemData": netraCtRscModemData,
       "netraCtRscCountryCode": netraCtRscCountryCode,
       "netraCtRscModemModel": netraCtRscModemModel,
       "netraCtRscEnetObjs": netraCtRscEnetObjs,
       "netraCtRscMacAddress": netraCtRscMacAddress,
       "netraCtRscEnetTpeLinkTest": netraCtRscEnetTpeLinkTest,
       "netraCtRscIPAddress": netraCtRscIPAddress,
       "netraCtRscIpMask": netraCtRscIpMask,
       "netraCtRscIpGateway": netraCtRscIpGateway,
       "netraCtRscSNMPHostAddress": netraCtRscSNMPHostAddress,
       "netraCtRscMailHostAddress": netraCtRscMailHostAddress,
       "netraCtRscMailUser": netraCtRscMailUser,
       "netraCtRscPPPLocalIP": netraCtRscPPPLocalIP,
       "netraCtRscPPPRemoteIP": netraCtRscPPPRemoteIP,
       "netraCtRscMailHostAddressBackup": netraCtRscMailHostAddressBackup,
       "netraCtRscEnvObjs": netraCtRscEnvObjs,
       "netraCtRscSystemType": netraCtRscSystemType,
       "netraCtRscPowerSupplyCount": netraCtRscPowerSupplyCount,
       "netraCtRscPowerSupplyTable": netraCtRscPowerSupplyTable,
       "netraCtRscPowerSupplyEntry": netraCtRscPowerSupplyEntry,
       "netraCtRscPowerSupplyIndex": netraCtRscPowerSupplyIndex,
       "netraCtRscPowerSupplyPresent": netraCtRscPowerSupplyPresent,
       "netraCtRscPowerSupplyOperState": netraCtRscPowerSupplyOperState,
       "netraCtRscPowerSupplyAdminState": netraCtRscPowerSupplyAdminState,
       "netraCtRscAlarmCount": netraCtRscAlarmCount,
       "netraCtRscAlarmTable": netraCtRscAlarmTable,
       "netraCtRscAlarmEntry": netraCtRscAlarmEntry,
       "netraCtRscAlarmIndex": netraCtRscAlarmIndex,
       "netraCtRscAlarmID": netraCtRscAlarmID,
       "netraCtRscAlarmOperState": netraCtRscAlarmOperState,
       "netraCtRscAlarmAdminState": netraCtRscAlarmAdminState,
       "netraCtRscAlarmPrefix": netraCtRscAlarmPrefix,
       "netraCtRscFanCount": netraCtRscFanCount,
       "netraCtRscFanTable": netraCtRscFanTable,
       "netraCtRscFanEntry": netraCtRscFanEntry,
       "netraCtRscFanIndex": netraCtRscFanIndex,
       "netraCtRscFanPresent": netraCtRscFanPresent,
       "netraCtRscFanStatus": netraCtRscFanStatus,
       "netraCtRscTemperatureCount": netraCtRscTemperatureCount,
       "netraCtRscTemperatureTable": netraCtRscTemperatureTable,
       "netraCtRscTemperatureEntry": netraCtRscTemperatureEntry,
       "netraCtRscTemperatureIndex": netraCtRscTemperatureIndex,
       "netraCtRscTemperatureValid": netraCtRscTemperatureValid,
       "netraCtRscTemperatureValue": netraCtRscTemperatureValue,
       "netraCtRscTemperatureLowWarn": netraCtRscTemperatureLowWarn,
       "netraCtRscTemperatureHighWarn": netraCtRscTemperatureHighWarn,
       "netraCtRscTemperatureDesc": netraCtRscTemperatureDesc,
       "netraCtRscLogObjs": netraCtRscLogObjs,
       "netraCtRscEventLogCount": netraCtRscEventLogCount,
       "netraCtRscEventLogTable": netraCtRscEventLogTable,
       "netraCtRscEventLogEntry": netraCtRscEventLogEntry,
       "netraCtRscEventLogIndex": netraCtRscEventLogIndex,
       "netraCtRscEventLogTimeStamp": netraCtRscEventLogTimeStamp,
       "netraCtRscEventLogMessage": netraCtRscEventLogMessage,
       "netraCtRscOrigConsoleLogCount": netraCtRscOrigConsoleLogCount,
       "netraCtRscOrigConsoleLogTable": netraCtRscOrigConsoleLogTable,
       "netraCtRscOrigConsoleLogEntry": netraCtRscOrigConsoleLogEntry,
       "netraCtRscOrigConsoleLogIndex": netraCtRscOrigConsoleLogIndex,
       "netraCtRscOrigConsoleLogTimeStamp": netraCtRscOrigConsoleLogTimeStamp,
       "netraCtRscOrigConsoleLogMessage": netraCtRscOrigConsoleLogMessage,
       "netraCtRscConsoleLogCount": netraCtRscConsoleLogCount,
       "netraCtRscConsoleLogTable": netraCtRscConsoleLogTable,
       "netraCtRscConsoleLogEntry": netraCtRscConsoleLogEntry,
       "netraCtRscConsoleLogIndex": netraCtRscConsoleLogIndex,
       "netraCtRscConsoleLogTimeStamp": netraCtRscConsoleLogTimeStamp,
       "netraCtRscConsoleLogMessage": netraCtRscConsoleLogMessage,
       "netraCtRscConsoleReset": netraCtRscConsoleReset,
       "netraCtRscEvents": netraCtRscEvents,
       "netraCtRscTrapPrefix": netraCtRscTrapPrefix,
       "netraCtRscEvent": netraCtRscEvent,
       "netraCtRscExpmnt": netraCtRscExpmnt,
       "netraCtRscRccConfig": netraCtRscRccConfig,
       "netraCtRscRCCPowerOnEnable": netraCtRscRCCPowerOnEnable,
       "netraCtRscRCCPowerOffEnable": netraCtRscRCCPowerOffEnable,
       "netraCtRscRCCResetEnable": netraCtRscRCCResetEnable,
       "netraCtRscRCCLinkNum": netraCtRscRCCLinkNum}
)
