# SNMP MIB module (ACC-ASPORT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-ASPORT
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:45 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccAsPort_ObjectIdentity = ObjectIdentity
accAsPort = _AccAsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10)
)
_AccConsole_ObjectIdentity = ObjectIdentity
accConsole = _AccConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10, 2)
)
_AccConsoleParms_ObjectIdentity = ObjectIdentity
accConsoleParms = _AccConsoleParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10, 2, 1)
)
_AccConsoleSpeed_Type = Integer32
_AccConsoleSpeed_Object = MibScalar
accConsoleSpeed = _AccConsoleSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10, 2, 1, 5),
    _AccConsoleSpeed_Type()
)
accConsoleSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accConsoleSpeed.setStatus("mandatory")
_AccNaTraps_ObjectIdentity = ObjectIdentity
accNaTraps = _AccNaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10, 2, 1, 6)
)
_AccNaTrapMsg_Type = DisplayString
_AccNaTrapMsg_Object = MibScalar
accNaTrapMsg = _AccNaTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10, 2, 1, 6, 1),
    _AccNaTrapMsg_Type()
)
accNaTrapMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accNaTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accSwLevlTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10, 2, 1, 6, 0, 1)
)
accSwLevlTrap.setObjects(
      *(("ACC-ASPORT", "accNaTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accSwLevlTrap.setStatus(
        ""
    )

accNaInvKeyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10, 2, 1, 6, 0, 2)
)
accNaInvKeyTrap.setObjects(
      *(("ACC-ASPORT", "accNaTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accNaInvKeyTrap.setStatus(
        ""
    )

accNaLogBufTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10, 2, 1, 6, 0, 3)
)
accNaLogBufTrap.setObjects(
      *(("ACC-ASPORT", "accNaTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accNaLogBufTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-ASPORT",
    **{"accAsPort": accAsPort,
       "accConsole": accConsole,
       "accConsoleParms": accConsoleParms,
       "accConsoleSpeed": accConsoleSpeed,
       "accNaTraps": accNaTraps,
       "accSwLevlTrap": accSwLevlTrap,
       "accNaInvKeyTrap": accNaInvKeyTrap,
       "accNaLogBufTrap": accNaLogBufTrap,
       "accNaTrapMsg": accNaTrapMsg}
)