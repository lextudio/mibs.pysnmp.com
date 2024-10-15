# SNMP MIB module (BIANCA-X8000-MIBSYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-X8000-MIBSYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:55 2024
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
_X8_ObjectIdentity = ObjectIdentity
x8 = _X8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3)
)
_SysX8Config_ObjectIdentity = ObjectIdentity
sysX8Config = _SysX8Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1)
)


class _SysX8ConfigPowerSupply1State_Type(Integer32):
    """Custom type sysX8ConfigPowerSupply1State based on Integer32"""
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
        *(("fail", 4),
          ("missing", 1),
          ("off", 2),
          ("running", 3))
    )


_SysX8ConfigPowerSupply1State_Type.__name__ = "Integer32"
_SysX8ConfigPowerSupply1State_Object = MibScalar
sysX8ConfigPowerSupply1State = _SysX8ConfigPowerSupply1State_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 1),
    _SysX8ConfigPowerSupply1State_Type()
)
sysX8ConfigPowerSupply1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX8ConfigPowerSupply1State.setStatus("mandatory")


class _SysX8ConfigPowerSupply1Temp_Type(Integer32):
    """Custom type sysX8ConfigPowerSupply1Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_SysX8ConfigPowerSupply1Temp_Type.__name__ = "Integer32"
_SysX8ConfigPowerSupply1Temp_Object = MibScalar
sysX8ConfigPowerSupply1Temp = _SysX8ConfigPowerSupply1Temp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 2),
    _SysX8ConfigPowerSupply1Temp_Type()
)
sysX8ConfigPowerSupply1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX8ConfigPowerSupply1Temp.setStatus("mandatory")


class _SysX8ConfigPowerSupply1TempAlarmThreshold_Type(Integer32):
    """Custom type sysX8ConfigPowerSupply1TempAlarmThreshold based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_SysX8ConfigPowerSupply1TempAlarmThreshold_Type.__name__ = "Integer32"
_SysX8ConfigPowerSupply1TempAlarmThreshold_Object = MibScalar
sysX8ConfigPowerSupply1TempAlarmThreshold = _SysX8ConfigPowerSupply1TempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 3),
    _SysX8ConfigPowerSupply1TempAlarmThreshold_Type()
)
sysX8ConfigPowerSupply1TempAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX8ConfigPowerSupply1TempAlarmThreshold.setStatus("mandatory")


class _SysX8ConfigPowerSupply1TempAlarmTrap_Type(Integer32):
    """Custom type sysX8ConfigPowerSupply1TempAlarmTrap based on Integer32"""
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


_SysX8ConfigPowerSupply1TempAlarmTrap_Type.__name__ = "Integer32"
_SysX8ConfigPowerSupply1TempAlarmTrap_Object = MibScalar
sysX8ConfigPowerSupply1TempAlarmTrap = _SysX8ConfigPowerSupply1TempAlarmTrap_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 4),
    _SysX8ConfigPowerSupply1TempAlarmTrap_Type()
)
sysX8ConfigPowerSupply1TempAlarmTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX8ConfigPowerSupply1TempAlarmTrap.setStatus("mandatory")


class _SysX8ConfigPowerSupply2State_Type(Integer32):
    """Custom type sysX8ConfigPowerSupply2State based on Integer32"""
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
        *(("fail", 4),
          ("missing", 1),
          ("off", 2),
          ("running", 3))
    )


_SysX8ConfigPowerSupply2State_Type.__name__ = "Integer32"
_SysX8ConfigPowerSupply2State_Object = MibScalar
sysX8ConfigPowerSupply2State = _SysX8ConfigPowerSupply2State_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 5),
    _SysX8ConfigPowerSupply2State_Type()
)
sysX8ConfigPowerSupply2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX8ConfigPowerSupply2State.setStatus("mandatory")


class _SysX8ConfigPowerSupply2Temp_Type(Integer32):
    """Custom type sysX8ConfigPowerSupply2Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_SysX8ConfigPowerSupply2Temp_Type.__name__ = "Integer32"
_SysX8ConfigPowerSupply2Temp_Object = MibScalar
sysX8ConfigPowerSupply2Temp = _SysX8ConfigPowerSupply2Temp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 6),
    _SysX8ConfigPowerSupply2Temp_Type()
)
sysX8ConfigPowerSupply2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX8ConfigPowerSupply2Temp.setStatus("mandatory")


class _SysX8ConfigPowerSupply2TempAlarmThreshold_Type(Integer32):
    """Custom type sysX8ConfigPowerSupply2TempAlarmThreshold based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_SysX8ConfigPowerSupply2TempAlarmThreshold_Type.__name__ = "Integer32"
_SysX8ConfigPowerSupply2TempAlarmThreshold_Object = MibScalar
sysX8ConfigPowerSupply2TempAlarmThreshold = _SysX8ConfigPowerSupply2TempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 7),
    _SysX8ConfigPowerSupply2TempAlarmThreshold_Type()
)
sysX8ConfigPowerSupply2TempAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX8ConfigPowerSupply2TempAlarmThreshold.setStatus("mandatory")


class _SysX8ConfigPowerSupply2TempAlarmTrap_Type(Integer32):
    """Custom type sysX8ConfigPowerSupply2TempAlarmTrap based on Integer32"""
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


_SysX8ConfigPowerSupply2TempAlarmTrap_Type.__name__ = "Integer32"
_SysX8ConfigPowerSupply2TempAlarmTrap_Object = MibScalar
sysX8ConfigPowerSupply2TempAlarmTrap = _SysX8ConfigPowerSupply2TempAlarmTrap_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 8),
    _SysX8ConfigPowerSupply2TempAlarmTrap_Type()
)
sysX8ConfigPowerSupply2TempAlarmTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX8ConfigPowerSupply2TempAlarmTrap.setStatus("mandatory")


class _SysX8ConfigFanControl_Type(Integer32):
    """Custom type sysX8ConfigFanControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("high", 2))
    )


_SysX8ConfigFanControl_Type.__name__ = "Integer32"
_SysX8ConfigFanControl_Object = MibScalar
sysX8ConfigFanControl = _SysX8ConfigFanControl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 9),
    _SysX8ConfigFanControl_Type()
)
sysX8ConfigFanControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysX8ConfigFanControl.setStatus("mandatory")
_SysX8ConfigFanVersion_Type = DisplayString
_SysX8ConfigFanVersion_Object = MibScalar
sysX8ConfigFanVersion = _SysX8ConfigFanVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 10),
    _SysX8ConfigFanVersion_Type()
)
sysX8ConfigFanVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX8ConfigFanVersion.setStatus("mandatory")
_SysX8ConfigFan1_Type = Integer32
_SysX8ConfigFan1_Object = MibScalar
sysX8ConfigFan1 = _SysX8ConfigFan1_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 11),
    _SysX8ConfigFan1_Type()
)
sysX8ConfigFan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX8ConfigFan1.setStatus("mandatory")
_SysX8ConfigFan2_Type = Integer32
_SysX8ConfigFan2_Object = MibScalar
sysX8ConfigFan2 = _SysX8ConfigFan2_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 12),
    _SysX8ConfigFan2_Type()
)
sysX8ConfigFan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX8ConfigFan2.setStatus("mandatory")
_SysX8ConfigFan3_Type = Integer32
_SysX8ConfigFan3_Object = MibScalar
sysX8ConfigFan3 = _SysX8ConfigFan3_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 13),
    _SysX8ConfigFan3_Type()
)
sysX8ConfigFan3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX8ConfigFan3.setStatus("mandatory")
_SysX8ConfigFan4_Type = Integer32
_SysX8ConfigFan4_Object = MibScalar
sysX8ConfigFan4 = _SysX8ConfigFan4_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 14),
    _SysX8ConfigFan4_Type()
)
sysX8ConfigFan4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysX8ConfigFan4.setStatus("mandatory")
_SysX8Traps_ObjectIdentity = ObjectIdentity
sysX8Traps = _SysX8Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2)
)

# Managed Objects groups


# Notification objects

sysX8TrapPowerSupply1Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2, 0, 1)
)
sysX8TrapPowerSupply1Missing.setObjects(
      *(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysName"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1State"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1Temp"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1TempAlarmTrap"))
)
if mibBuilder.loadTexts:
    sysX8TrapPowerSupply1Missing.setStatus(
        ""
    )

sysX8TrapPowerSupply1PowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2, 0, 2)
)
sysX8TrapPowerSupply1PowerOff.setObjects(
      *(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysName"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1State"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1Temp"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1TempAlarmTrap"))
)
if mibBuilder.loadTexts:
    sysX8TrapPowerSupply1PowerOff.setStatus(
        ""
    )

sysX8TrapPowerSupply1PowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2, 0, 3)
)
sysX8TrapPowerSupply1PowerFail.setObjects(
      *(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysName"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1State"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1Temp"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1TempAlarmTrap"))
)
if mibBuilder.loadTexts:
    sysX8TrapPowerSupply1PowerFail.setStatus(
        ""
    )

sysX8TrapPowerSupply1PowerGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2, 0, 4)
)
sysX8TrapPowerSupply1PowerGood.setObjects(
      *(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysName"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1State"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1Temp"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1TempAlarmTrap"))
)
if mibBuilder.loadTexts:
    sysX8TrapPowerSupply1PowerGood.setStatus(
        ""
    )

sysX8TrapPowerSupply1TempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2, 0, 5)
)
sysX8TrapPowerSupply1TempCritical.setObjects(
      *(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysName"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1State"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1Temp"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1TempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    sysX8TrapPowerSupply1TempCritical.setStatus(
        ""
    )

sysX8TrapPowerSupply1TempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2, 0, 6)
)
sysX8TrapPowerSupply1TempOk.setObjects(
      *(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysName"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1State"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1Temp"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1TempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    sysX8TrapPowerSupply1TempOk.setStatus(
        ""
    )

sysX8TrapPowerSupply2Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2, 0, 7)
)
sysX8TrapPowerSupply2Missing.setObjects(
      *(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysName"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2State"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2Temp"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2TempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    sysX8TrapPowerSupply2Missing.setStatus(
        ""
    )

sysX8TrapPowerSupply2PowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2, 0, 8)
)
sysX8TrapPowerSupply2PowerOff.setObjects(
      *(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysName"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2State"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2Temp"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2TempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    sysX8TrapPowerSupply2PowerOff.setStatus(
        ""
    )

sysX8TrapPowerSupply2PowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2, 0, 9)
)
sysX8TrapPowerSupply2PowerFail.setObjects(
      *(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysName"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2State"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2Temp"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2TempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    sysX8TrapPowerSupply2PowerFail.setStatus(
        ""
    )

sysX8TrapPowerSupply2PowerGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2, 0, 10)
)
sysX8TrapPowerSupply2PowerGood.setObjects(
      *(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysName"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2State"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2Temp"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2TempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    sysX8TrapPowerSupply2PowerGood.setStatus(
        ""
    )

sysX8TrapPowerSupply2TempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2, 0, 11)
)
sysX8TrapPowerSupply2TempCritical.setObjects(
      *(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysName"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2State"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2Temp"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2TempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    sysX8TrapPowerSupply2TempCritical.setStatus(
        ""
    )

sysX8TrapPowerSupply2TempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2, 0, 12)
)
sysX8TrapPowerSupply2TempOk.setObjects(
      *(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysName"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2State"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2Temp"),
        ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2TempAlarmThreshold"))
)
if mibBuilder.loadTexts:
    sysX8TrapPowerSupply2TempOk.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-X8000-MIBSYS-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "sys": sys,
       "x8": x8,
       "sysX8Config": sysX8Config,
       "sysX8ConfigPowerSupply1State": sysX8ConfigPowerSupply1State,
       "sysX8ConfigPowerSupply1Temp": sysX8ConfigPowerSupply1Temp,
       "sysX8ConfigPowerSupply1TempAlarmThreshold": sysX8ConfigPowerSupply1TempAlarmThreshold,
       "sysX8ConfigPowerSupply1TempAlarmTrap": sysX8ConfigPowerSupply1TempAlarmTrap,
       "sysX8ConfigPowerSupply2State": sysX8ConfigPowerSupply2State,
       "sysX8ConfigPowerSupply2Temp": sysX8ConfigPowerSupply2Temp,
       "sysX8ConfigPowerSupply2TempAlarmThreshold": sysX8ConfigPowerSupply2TempAlarmThreshold,
       "sysX8ConfigPowerSupply2TempAlarmTrap": sysX8ConfigPowerSupply2TempAlarmTrap,
       "sysX8ConfigFanControl": sysX8ConfigFanControl,
       "sysX8ConfigFanVersion": sysX8ConfigFanVersion,
       "sysX8ConfigFan1": sysX8ConfigFan1,
       "sysX8ConfigFan2": sysX8ConfigFan2,
       "sysX8ConfigFan3": sysX8ConfigFan3,
       "sysX8ConfigFan4": sysX8ConfigFan4,
       "sysX8Traps": sysX8Traps,
       "sysX8TrapPowerSupply1Missing": sysX8TrapPowerSupply1Missing,
       "sysX8TrapPowerSupply1PowerOff": sysX8TrapPowerSupply1PowerOff,
       "sysX8TrapPowerSupply1PowerFail": sysX8TrapPowerSupply1PowerFail,
       "sysX8TrapPowerSupply1PowerGood": sysX8TrapPowerSupply1PowerGood,
       "sysX8TrapPowerSupply1TempCritical": sysX8TrapPowerSupply1TempCritical,
       "sysX8TrapPowerSupply1TempOk": sysX8TrapPowerSupply1TempOk,
       "sysX8TrapPowerSupply2Missing": sysX8TrapPowerSupply2Missing,
       "sysX8TrapPowerSupply2PowerOff": sysX8TrapPowerSupply2PowerOff,
       "sysX8TrapPowerSupply2PowerFail": sysX8TrapPowerSupply2PowerFail,
       "sysX8TrapPowerSupply2PowerGood": sysX8TrapPowerSupply2PowerGood,
       "sysX8TrapPowerSupply2TempCritical": sysX8TrapPowerSupply2TempCritical,
       "sysX8TrapPowerSupply2TempOk": sysX8TrapPowerSupply2TempOk}
)
