# SNMP MIB module (BIANCA-X4000-MIBSYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-X4000-MIBSYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:54 2024
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

(sysDescr,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysName")

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

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 17)
)
_X4_ObjectIdentity = ObjectIdentity
x4 = _X4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2)
)
_SysX4Config_ObjectIdentity = ObjectIdentity
sysX4Config = _SysX4Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1)
)


class _SysX4ConfigLcdBrightness_Type(Integer32):
    """Custom type sysX4ConfigLcdBrightness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SysX4ConfigLcdBrightness_Type.__name__ = "Integer32"
_SysX4ConfigLcdBrightness_Object = MibScalar
sysX4ConfigLcdBrightness = _SysX4ConfigLcdBrightness_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 1),
    _SysX4ConfigLcdBrightness_Type()
)
sysX4ConfigLcdBrightness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX4ConfigLcdBrightness.setStatus("mandatory")


class _SysX4ConfigLcdContrast_Type(Integer32):
    """Custom type sysX4ConfigLcdContrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SysX4ConfigLcdContrast_Type.__name__ = "Integer32"
_SysX4ConfigLcdContrast_Object = MibScalar
sysX4ConfigLcdContrast = _SysX4ConfigLcdContrast_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 2),
    _SysX4ConfigLcdContrast_Type()
)
sysX4ConfigLcdContrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX4ConfigLcdContrast.setStatus("mandatory")


class _SysX4ConfigLcdConfigure_Type(Integer32):
    """Custom type sysX4ConfigLcdConfigure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SysX4ConfigLcdConfigure_Type.__name__ = "Integer32"
_SysX4ConfigLcdConfigure_Object = MibScalar
sysX4ConfigLcdConfigure = _SysX4ConfigLcdConfigure_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 3),
    _SysX4ConfigLcdConfigure_Type()
)
sysX4ConfigLcdConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX4ConfigLcdConfigure.setStatus("mandatory")


class _SysX4ConfigLcdPin_Type(DisplayString):
    """Custom type sysX4ConfigLcdPin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SysX4ConfigLcdPin_Type.__name__ = "DisplayString"
_SysX4ConfigLcdPin_Object = MibScalar
sysX4ConfigLcdPin = _SysX4ConfigLcdPin_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 4),
    _SysX4ConfigLcdPin_Type()
)
sysX4ConfigLcdPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX4ConfigLcdPin.setStatus("mandatory")


class _SysX4ConfigLcdIdleTimer_Type(Integer32):
    """Custom type sysX4ConfigLcdIdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SysX4ConfigLcdIdleTimer_Type.__name__ = "Integer32"
_SysX4ConfigLcdIdleTimer_Object = MibScalar
sysX4ConfigLcdIdleTimer = _SysX4ConfigLcdIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 5),
    _SysX4ConfigLcdIdleTimer_Type()
)
sysX4ConfigLcdIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX4ConfigLcdIdleTimer.setStatus("mandatory")


class _SysX4ConfigLcdDefaultScreen_Type(DisplayString):
    """Custom type sysX4ConfigLcdDefaultScreen based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SysX4ConfigLcdDefaultScreen_Type.__name__ = "DisplayString"
_SysX4ConfigLcdDefaultScreen_Object = MibScalar
sysX4ConfigLcdDefaultScreen = _SysX4ConfigLcdDefaultScreen_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 6),
    _SysX4ConfigLcdDefaultScreen_Type()
)
sysX4ConfigLcdDefaultScreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX4ConfigLcdDefaultScreen.setStatus("mandatory")


class _SysX4ConfigLcdLanguage_Type(DisplayString):
    """Custom type sysX4ConfigLcdLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SysX4ConfigLcdLanguage_Type.__name__ = "DisplayString"
_SysX4ConfigLcdLanguage_Object = MibScalar
sysX4ConfigLcdLanguage = _SysX4ConfigLcdLanguage_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 7),
    _SysX4ConfigLcdLanguage_Type()
)
sysX4ConfigLcdLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX4ConfigLcdLanguage.setStatus("mandatory")


class _SysX4ConfigTempUnit_Type(Integer32):
    """Custom type sysX4ConfigTempUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )


_SysX4ConfigTempUnit_Type.__name__ = "Integer32"
_SysX4ConfigTempUnit_Object = MibScalar
sysX4ConfigTempUnit = _SysX4ConfigTempUnit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 8),
    _SysX4ConfigTempUnit_Type()
)
sysX4ConfigTempUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX4ConfigTempUnit.setStatus("mandatory")


class _SysX4ConfigMainTemp_Type(Integer32):
    """Custom type sysX4ConfigMainTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_SysX4ConfigMainTemp_Type.__name__ = "Integer32"
_SysX4ConfigMainTemp_Object = MibScalar
sysX4ConfigMainTemp = _SysX4ConfigMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 9),
    _SysX4ConfigMainTemp_Type()
)
sysX4ConfigMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX4ConfigMainTemp.setStatus("mandatory")


class _SysX4ConfigMainTempAlarmThreshold_Type(Integer32):
    """Custom type sysX4ConfigMainTempAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_SysX4ConfigMainTempAlarmThreshold_Type.__name__ = "Integer32"
_SysX4ConfigMainTempAlarmThreshold_Object = MibScalar
sysX4ConfigMainTempAlarmThreshold = _SysX4ConfigMainTempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 10),
    _SysX4ConfigMainTempAlarmThreshold_Type()
)
sysX4ConfigMainTempAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX4ConfigMainTempAlarmThreshold.setStatus("mandatory")


class _SysX4ConfigMainTempAlarmTrap_Type(Integer32):
    """Custom type sysX4ConfigMainTempAlarmTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("normal", 1))
    )


_SysX4ConfigMainTempAlarmTrap_Type.__name__ = "Integer32"
_SysX4ConfigMainTempAlarmTrap_Object = MibScalar
sysX4ConfigMainTempAlarmTrap = _SysX4ConfigMainTempAlarmTrap_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 11),
    _SysX4ConfigMainTempAlarmTrap_Type()
)
sysX4ConfigMainTempAlarmTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX4ConfigMainTempAlarmTrap.setStatus("mandatory")


class _SysX4ConfigMod1Temp_Type(Integer32):
    """Custom type sysX4ConfigMod1Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_SysX4ConfigMod1Temp_Type.__name__ = "Integer32"
_SysX4ConfigMod1Temp_Object = MibScalar
sysX4ConfigMod1Temp = _SysX4ConfigMod1Temp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 12),
    _SysX4ConfigMod1Temp_Type()
)
sysX4ConfigMod1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX4ConfigMod1Temp.setStatus("mandatory")


class _SysX4ConfigMod1TempAlarmThreshold_Type(Integer32):
    """Custom type sysX4ConfigMod1TempAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_SysX4ConfigMod1TempAlarmThreshold_Type.__name__ = "Integer32"
_SysX4ConfigMod1TempAlarmThreshold_Object = MibScalar
sysX4ConfigMod1TempAlarmThreshold = _SysX4ConfigMod1TempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 13),
    _SysX4ConfigMod1TempAlarmThreshold_Type()
)
sysX4ConfigMod1TempAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX4ConfigMod1TempAlarmThreshold.setStatus("mandatory")


class _SysX4ConfigMod1TempAlarmTrap_Type(Integer32):
    """Custom type sysX4ConfigMod1TempAlarmTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("normal", 1))
    )


_SysX4ConfigMod1TempAlarmTrap_Type.__name__ = "Integer32"
_SysX4ConfigMod1TempAlarmTrap_Object = MibScalar
sysX4ConfigMod1TempAlarmTrap = _SysX4ConfigMod1TempAlarmTrap_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 14),
    _SysX4ConfigMod1TempAlarmTrap_Type()
)
sysX4ConfigMod1TempAlarmTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX4ConfigMod1TempAlarmTrap.setStatus("mandatory")


class _SysX4ConfigMod2Temp_Type(Integer32):
    """Custom type sysX4ConfigMod2Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_SysX4ConfigMod2Temp_Type.__name__ = "Integer32"
_SysX4ConfigMod2Temp_Object = MibScalar
sysX4ConfigMod2Temp = _SysX4ConfigMod2Temp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 15),
    _SysX4ConfigMod2Temp_Type()
)
sysX4ConfigMod2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX4ConfigMod2Temp.setStatus("mandatory")


class _SysX4ConfigMod2TempAlarmThreshold_Type(Integer32):
    """Custom type sysX4ConfigMod2TempAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_SysX4ConfigMod2TempAlarmThreshold_Type.__name__ = "Integer32"
_SysX4ConfigMod2TempAlarmThreshold_Object = MibScalar
sysX4ConfigMod2TempAlarmThreshold = _SysX4ConfigMod2TempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 16),
    _SysX4ConfigMod2TempAlarmThreshold_Type()
)
sysX4ConfigMod2TempAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX4ConfigMod2TempAlarmThreshold.setStatus("mandatory")


class _SysX4ConfigMod2TempAlarmTrap_Type(Integer32):
    """Custom type sysX4ConfigMod2TempAlarmTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("normal", 1))
    )


_SysX4ConfigMod2TempAlarmTrap_Type.__name__ = "Integer32"
_SysX4ConfigMod2TempAlarmTrap_Object = MibScalar
sysX4ConfigMod2TempAlarmTrap = _SysX4ConfigMod2TempAlarmTrap_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 1, 17),
    _SysX4ConfigMod2TempAlarmTrap_Type()
)
sysX4ConfigMod2TempAlarmTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX4ConfigMod2TempAlarmTrap.setStatus("mandatory")
_SysX4Traps_ObjectIdentity = ObjectIdentity
sysX4Traps = _SysX4Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 2)
)

# Managed Objects groups


# Notification objects

sysX4TrapMainTempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 2, 0, 1)
)
sysX4TrapMainTempCritical.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigTempUnit"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMainTemp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMainTempAlarmThreshold"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod1Temp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod2Temp"))
)
if mibBuilder.loadTexts:
    sysX4TrapMainTempCritical.setStatus(
        ""
    )

sysX4TrapMainTempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 2, 0, 2)
)
sysX4TrapMainTempOk.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigTempUnit"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMainTemp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMainTempAlarmThreshold"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod1Temp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod2Temp"))
)
if mibBuilder.loadTexts:
    sysX4TrapMainTempOk.setStatus(
        ""
    )

sysX4TrapMod1TempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 2, 0, 3)
)
sysX4TrapMod1TempCritical.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigTempUnit"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMainTemp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod1Temp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod1TempAlarmThreshold"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod2Temp"))
)
if mibBuilder.loadTexts:
    sysX4TrapMod1TempCritical.setStatus(
        ""
    )

sysX4TrapMod1Temp1Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 2, 0, 4)
)
sysX4TrapMod1Temp1Ok.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigTempUnit"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMainTemp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod1Temp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod1TempAlarmThreshold"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod2Temp"))
)
if mibBuilder.loadTexts:
    sysX4TrapMod1Temp1Ok.setStatus(
        ""
    )

sysX4TrapMod2TempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 2, 0, 5)
)
sysX4TrapMod2TempCritical.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigTempUnit"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMainTemp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod1Temp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod2Temp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod2TempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    sysX4TrapMod2TempCritical.setStatus(
        ""
    )

sysX4TrapMod2TempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 2, 2, 0, 6)
)
sysX4TrapMod2TempOk.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigTempUnit"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMainTemp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod1Temp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod2Temp"),
        ("BIANCA-X4000-MIBSYS-MIB", "sysX4ConfigMod2TempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    sysX4TrapMod2TempOk.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-X4000-MIBSYS-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "sys": sys,
       "x4": x4,
       "sysX4Config": sysX4Config,
       "sysX4ConfigLcdBrightness": sysX4ConfigLcdBrightness,
       "sysX4ConfigLcdContrast": sysX4ConfigLcdContrast,
       "sysX4ConfigLcdConfigure": sysX4ConfigLcdConfigure,
       "sysX4ConfigLcdPin": sysX4ConfigLcdPin,
       "sysX4ConfigLcdIdleTimer": sysX4ConfigLcdIdleTimer,
       "sysX4ConfigLcdDefaultScreen": sysX4ConfigLcdDefaultScreen,
       "sysX4ConfigLcdLanguage": sysX4ConfigLcdLanguage,
       "sysX4ConfigTempUnit": sysX4ConfigTempUnit,
       "sysX4ConfigMainTemp": sysX4ConfigMainTemp,
       "sysX4ConfigMainTempAlarmThreshold": sysX4ConfigMainTempAlarmThreshold,
       "sysX4ConfigMainTempAlarmTrap": sysX4ConfigMainTempAlarmTrap,
       "sysX4ConfigMod1Temp": sysX4ConfigMod1Temp,
       "sysX4ConfigMod1TempAlarmThreshold": sysX4ConfigMod1TempAlarmThreshold,
       "sysX4ConfigMod1TempAlarmTrap": sysX4ConfigMod1TempAlarmTrap,
       "sysX4ConfigMod2Temp": sysX4ConfigMod2Temp,
       "sysX4ConfigMod2TempAlarmThreshold": sysX4ConfigMod2TempAlarmThreshold,
       "sysX4ConfigMod2TempAlarmTrap": sysX4ConfigMod2TempAlarmTrap,
       "sysX4Traps": sysX4Traps,
       "sysX4TrapMainTempCritical": sysX4TrapMainTempCritical,
       "sysX4TrapMainTempOk": sysX4TrapMainTempOk,
       "sysX4TrapMod1TempCritical": sysX4TrapMod1TempCritical,
       "sysX4TrapMod1Temp1Ok": sysX4TrapMod1Temp1Ok,
       "sysX4TrapMod2TempCritical": sysX4TrapMod2TempCritical,
       "sysX4TrapMod2TempOk": sysX4TrapMod2TempOk}
)
