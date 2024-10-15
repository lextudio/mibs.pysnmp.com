# SNMP MIB module (S5-CHASSIS-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-CHASSIS-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:03 2024
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

(s5ChasComOperState,
 s5ChasComType,
 s5ChasNotifyFanDirection) = mibBuilder.importSymbols(
    "S5-CHASSIS-MIB",
    "s5ChasComOperState",
    "s5ChasComType",
    "s5ChasNotifyFanDirection")

(s5ChaTrap,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5ChaTrap")

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

s5ChassisTrapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0)
)
s5ChassisTrapMib.setRevisions(
        ("2011-04-15 00:00",
         "2011-03-29 00:00",
         "2009-07-29 00:00",
         "2004-07-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

s5CtrNewHotSwap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 1)
)
s5CtrNewHotSwap.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrNewHotSwap.setStatus(
        "current"
    )

s5CtrNewProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 2)
)
s5CtrNewProblem.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrNewProblem.setStatus(
        "current"
    )

s5CtrNewUnitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 3)
)
s5CtrNewUnitUp.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrNewUnitUp.setStatus(
        "current"
    )

s5CtrNewUnitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 4)
)
s5CtrNewUnitDown.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrNewUnitDown.setStatus(
        "current"
    )

s5CtrFanRotationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 5)
)
s5CtrFanRotationError.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrFanRotationError.setStatus(
        "current"
    )

s5CtrFanDirectionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 6)
)
s5CtrFanDirectionError.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"),
        ("S5-CHASSIS-MIB", "s5ChasNotifyFanDirection"))
)
if mibBuilder.loadTexts:
    s5CtrFanDirectionError.setStatus(
        "current"
    )

s5CtrHighTemperatureError = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 7)
)
s5CtrHighTemperatureError.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrHighTemperatureError.setStatus(
        "current"
    )

s5CtrHotSwap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 1)
)
s5CtrHotSwap.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrHotSwap.setStatus(
        "current"
    )

s5CtrProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 2)
)
s5CtrProblem.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrProblem.setStatus(
        "current"
    )

s5CtrUnitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 3)
)
s5CtrUnitUp.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrUnitUp.setStatus(
        "current"
    )

s5CtrUnitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 4)
)
s5CtrUnitDown.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrUnitDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-CHASSIS-TRAP-MIB",
    **{"s5ChassisTrapMib": s5ChassisTrapMib,
       "s5CtrNewHotSwap": s5CtrNewHotSwap,
       "s5CtrNewProblem": s5CtrNewProblem,
       "s5CtrNewUnitUp": s5CtrNewUnitUp,
       "s5CtrNewUnitDown": s5CtrNewUnitDown,
       "s5CtrFanRotationError": s5CtrFanRotationError,
       "s5CtrFanDirectionError": s5CtrFanDirectionError,
       "s5CtrHighTemperatureError": s5CtrHighTemperatureError,
       "s5CtrHotSwap": s5CtrHotSwap,
       "s5CtrProblem": s5CtrProblem,
       "s5CtrUnitUp": s5CtrUnitUp,
       "s5CtrUnitDown": s5CtrUnitDown}
)
