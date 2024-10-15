# SNMP MIB module (RAPID-SYSTEM-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAPID-SYSTEM-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:41 2024
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

(rapidstream,) = mibBuilder.importSymbols(
    "RAPID-MIB",
    "rapidstream")

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


# MODULE-IDENTITY

rsSystemConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 2)
)
rsSystemConfigMIB.setRevisions(
        ("1999-06-26 12:00",
         "2002-11-01 12:00",
         "2004-06-01 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsSysTraps_ObjectIdentity = ObjectIdentity
rsSysTraps = _RsSysTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 2, 3)
)
if mibBuilder.loadTexts:
    rsSysTraps.setStatus("current")
_RsSysTrapsPrefix_ObjectIdentity = ObjectIdentity
rsSysTrapsPrefix = _RsSysTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 2, 3, 0)
)
if mibBuilder.loadTexts:
    rsSysTrapsPrefix.setStatus("current")
_RsSysTrapObjects_ObjectIdentity = ObjectIdentity
rsSysTrapObjects = _RsSysTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 2, 4)
)
if mibBuilder.loadTexts:
    rsSysTrapObjects.setStatus("current")
_RsAlarmId_Type = Integer32
_RsAlarmId_Object = MibScalar
rsAlarmId = _RsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 2, 4, 1),
    _RsAlarmId_Type()
)
rsAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAlarmId.setStatus("current")


class _RsAlarmLabel_Type(OctetString):
    """Custom type rsAlarmLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsAlarmLabel_Type.__name__ = "OctetString"
_RsAlarmLabel_Object = MibScalar
rsAlarmLabel = _RsAlarmLabel_Object(
    (1, 3, 6, 1, 4, 1, 4355, 2, 4, 2),
    _RsAlarmLabel_Type()
)
rsAlarmLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAlarmLabel.setStatus("current")
_RsAlarmTime_Type = OctetString
_RsAlarmTime_Object = MibScalar
rsAlarmTime = _RsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 4355, 2, 4, 3),
    _RsAlarmTime_Type()
)
rsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAlarmTime.setStatus("current")


class _RsAlarmLevel_Type(Integer32):
    """Custom type rsAlarmLevel based on Integer32"""
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


_RsAlarmLevel_Type.__name__ = "Integer32"
_RsAlarmLevel_Object = MibScalar
rsAlarmLevel = _RsAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 4355, 2, 4, 4),
    _RsAlarmLevel_Type()
)
rsAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAlarmLevel.setStatus("current")


class _RsAlarmHostname_Type(OctetString):
    """Custom type rsAlarmHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsAlarmHostname_Type.__name__ = "OctetString"
_RsAlarmHostname_Object = MibScalar
rsAlarmHostname = _RsAlarmHostname_Object(
    (1, 3, 6, 1, 4, 1, 4355, 2, 4, 5),
    _RsAlarmHostname_Type()
)
rsAlarmHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAlarmHostname.setStatus("current")
_RsAlarmMsg_Type = OctetString
_RsAlarmMsg_Object = MibScalar
rsAlarmMsg = _RsAlarmMsg_Object(
    (1, 3, 6, 1, 4, 1, 4355, 2, 4, 6),
    _RsAlarmMsg_Type()
)
rsAlarmMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAlarmMsg.setStatus("current")
_RsSysTrapControl_ObjectIdentity = ObjectIdentity
rsSysTrapControl = _RsSysTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 2, 5)
)
if mibBuilder.loadTexts:
    rsSysTrapControl.setStatus("current")


class _RsAlarmTrapEnable_Type(Integer32):
    """Custom type rsAlarmTrapEnable based on Integer32"""
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


_RsAlarmTrapEnable_Type.__name__ = "Integer32"
_RsAlarmTrapEnable_Object = MibScalar
rsAlarmTrapEnable = _RsAlarmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 2, 5, 1),
    _RsAlarmTrapEnable_Type()
)
rsAlarmTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAlarmTrapEnable.setStatus("current")

# Managed Objects groups


# Notification objects

rsAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4355, 2, 3, 0, 1)
)
rsAlarmTrap.setObjects(
      *(("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmId"),
        ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmLabel"),
        ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmTime"),
        ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmLevel"),
        ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmHostname"),
        ("RAPID-SYSTEM-CONFIG-MIB", "rsAlarmMsg"))
)
if mibBuilder.loadTexts:
    rsAlarmTrap.setStatus(
        "current"
    )

rsSnmpStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 4355, 2, 3, 0, 2)
)
if mibBuilder.loadTexts:
    rsSnmpStart.setStatus(
        "current"
    )

rsSnmpShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4355, 2, 3, 0, 3)
)
if mibBuilder.loadTexts:
    rsSnmpShutdown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAPID-SYSTEM-CONFIG-MIB",
    **{"rsSystemConfigMIB": rsSystemConfigMIB,
       "rsSysTraps": rsSysTraps,
       "rsSysTrapsPrefix": rsSysTrapsPrefix,
       "rsAlarmTrap": rsAlarmTrap,
       "rsSnmpStart": rsSnmpStart,
       "rsSnmpShutdown": rsSnmpShutdown,
       "rsSysTrapObjects": rsSysTrapObjects,
       "rsAlarmId": rsAlarmId,
       "rsAlarmLabel": rsAlarmLabel,
       "rsAlarmTime": rsAlarmTime,
       "rsAlarmLevel": rsAlarmLevel,
       "rsAlarmHostname": rsAlarmHostname,
       "rsAlarmMsg": rsAlarmMsg,
       "rsSysTrapControl": rsSysTrapControl,
       "rsAlarmTrapEnable": rsAlarmTrapEnable}
)
