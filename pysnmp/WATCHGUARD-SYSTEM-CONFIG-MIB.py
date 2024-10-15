# SNMP MIB module (WATCHGUARD-SYSTEM-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WATCHGUARD-SYSTEM-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:38 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-MIB",
    "watchguard")


# MODULE-IDENTITY

wgSystemConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 2)
)
wgSystemConfigMIB.setRevisions(
        ("2007-01-25 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WgSysTraps_ObjectIdentity = ObjectIdentity
wgSysTraps = _WgSysTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 2, 3)
)
if mibBuilder.loadTexts:
    wgSysTraps.setStatus("current")
_WgSysTrapsPrefix_ObjectIdentity = ObjectIdentity
wgSysTrapsPrefix = _WgSysTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 2, 3, 0)
)
if mibBuilder.loadTexts:
    wgSysTrapsPrefix.setStatus("current")
_WgSysTrapObjects_ObjectIdentity = ObjectIdentity
wgSysTrapObjects = _WgSysTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 2, 4)
)
if mibBuilder.loadTexts:
    wgSysTrapObjects.setStatus("current")
_WgAlarmId_Type = Integer32
_WgAlarmId_Object = MibScalar
wgAlarmId = _WgAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 2, 4, 1),
    _WgAlarmId_Type()
)
wgAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgAlarmId.setStatus("current")


class _WgAlarmLabel_Type(OctetString):
    """Custom type wgAlarmLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WgAlarmLabel_Type.__name__ = "OctetString"
_WgAlarmLabel_Object = MibScalar
wgAlarmLabel = _WgAlarmLabel_Object(
    (1, 3, 6, 1, 4, 1, 3097, 2, 4, 2),
    _WgAlarmLabel_Type()
)
wgAlarmLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgAlarmLabel.setStatus("current")
_WgAlarmTime_Type = OctetString
_WgAlarmTime_Object = MibScalar
wgAlarmTime = _WgAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 3097, 2, 4, 3),
    _WgAlarmTime_Type()
)
wgAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgAlarmTime.setStatus("current")


class _WgAlarmLevel_Type(Integer32):
    """Custom type wgAlarmLevel based on Integer32"""
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
        *(("critical", 1),
          ("error", 2),
          ("normal", 4),
          ("warning", 3))
    )


_WgAlarmLevel_Type.__name__ = "Integer32"
_WgAlarmLevel_Object = MibScalar
wgAlarmLevel = _WgAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3097, 2, 4, 4),
    _WgAlarmLevel_Type()
)
wgAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgAlarmLevel.setStatus("current")


class _WgAlarmHostname_Type(OctetString):
    """Custom type wgAlarmHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WgAlarmHostname_Type.__name__ = "OctetString"
_WgAlarmHostname_Object = MibScalar
wgAlarmHostname = _WgAlarmHostname_Object(
    (1, 3, 6, 1, 4, 1, 3097, 2, 4, 5),
    _WgAlarmHostname_Type()
)
wgAlarmHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgAlarmHostname.setStatus("current")
_WgAlarmMsg_Type = OctetString
_WgAlarmMsg_Object = MibScalar
wgAlarmMsg = _WgAlarmMsg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 2, 4, 6),
    _WgAlarmMsg_Type()
)
wgAlarmMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgAlarmMsg.setStatus("current")
_WgSysTrapControl_ObjectIdentity = ObjectIdentity
wgSysTrapControl = _WgSysTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 2, 5)
)
if mibBuilder.loadTexts:
    wgSysTrapControl.setStatus("current")


class _WgAlarmTrapEnable_Type(Integer32):
    """Custom type wgAlarmTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_WgAlarmTrapEnable_Type.__name__ = "Integer32"
_WgAlarmTrapEnable_Object = MibScalar
wgAlarmTrapEnable = _WgAlarmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 2, 5, 1),
    _WgAlarmTrapEnable_Type()
)
wgAlarmTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgAlarmTrapEnable.setStatus("current")

# Managed Objects groups


# Notification objects

wgAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3097, 2, 3, 0, 1)
)
wgAlarmTrap.setObjects(
      *(("WATCHGUARD-SYSTEM-CONFIG-MIB", "wgAlarmId"),
        ("WATCHGUARD-SYSTEM-CONFIG-MIB", "wgAlarmLabel"),
        ("WATCHGUARD-SYSTEM-CONFIG-MIB", "wgAlarmTime"),
        ("WATCHGUARD-SYSTEM-CONFIG-MIB", "wgAlarmLevel"),
        ("WATCHGUARD-SYSTEM-CONFIG-MIB", "wgAlarmHostname"),
        ("WATCHGUARD-SYSTEM-CONFIG-MIB", "wgAlarmMsg"))
)
if mibBuilder.loadTexts:
    wgAlarmTrap.setStatus(
        "current"
    )

wgSnmpStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3097, 2, 3, 0, 2)
)
if mibBuilder.loadTexts:
    wgSnmpStart.setStatus(
        "current"
    )

wgSnmpShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3097, 2, 3, 0, 3)
)
if mibBuilder.loadTexts:
    wgSnmpShutdown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-SYSTEM-CONFIG-MIB",
    **{"wgSystemConfigMIB": wgSystemConfigMIB,
       "wgSysTraps": wgSysTraps,
       "wgSysTrapsPrefix": wgSysTrapsPrefix,
       "wgAlarmTrap": wgAlarmTrap,
       "wgSnmpStart": wgSnmpStart,
       "wgSnmpShutdown": wgSnmpShutdown,
       "wgSysTrapObjects": wgSysTrapObjects,
       "wgAlarmId": wgAlarmId,
       "wgAlarmLabel": wgAlarmLabel,
       "wgAlarmTime": wgAlarmTime,
       "wgAlarmLevel": wgAlarmLevel,
       "wgAlarmHostname": wgAlarmHostname,
       "wgAlarmMsg": wgAlarmMsg,
       "wgSysTrapControl": wgSysTrapControl,
       "wgAlarmTrapEnable": wgAlarmTrapEnable}
)
