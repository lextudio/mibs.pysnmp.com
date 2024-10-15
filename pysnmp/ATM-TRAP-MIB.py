# SNMP MIB module (ATM-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:05 2024
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

(atmPortCardIndex,
 atmPortPortIndex,
 atmPortSscopStatus) = mibBuilder.importSymbols(
    "CENTILLION-ATMCFG-MIB",
    "atmPortCardIndex",
    "atmPortPortIndex",
    "atmPortSscopStatus")

(atmTraps,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "atmTraps")

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


# Managed Objects groups


# Notification objects

s5CtrSscopDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 7, 0, 1)
)
s5CtrSscopDown.setObjects(
      *(("CENTILLION-ATMCFG-MIB", "atmPortCardIndex"),
        ("CENTILLION-ATMCFG-MIB", "atmPortPortIndex"),
        ("CENTILLION-ATMCFG-MIB", "atmPortSscopStatus"))
)
if mibBuilder.loadTexts:
    s5CtrSscopDown.setStatus(
        ""
    )

s5CtrAdmaLockup = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 7, 0, 2)
)
s5CtrAdmaLockup.setObjects(
      *(("CENTILLION-ATMCFG-MIB", "atmPortCardIndex"),
        ("CENTILLION-ATMCFG-MIB", "atmPortPortIndex"))
)
if mibBuilder.loadTexts:
    s5CtrAdmaLockup.setStatus(
        ""
    )

s5CtrAcmaLockup = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 7, 0, 3)
)
s5CtrAcmaLockup.setObjects(
    ("CENTILLION-ATMCFG-MIB", "atmPortCardIndex")
)
if mibBuilder.loadTexts:
    s5CtrAcmaLockup.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-TRAP-MIB",
    **{"s5CtrSscopDown": s5CtrSscopDown,
       "s5CtrAdmaLockup": s5CtrAdmaLockup,
       "s5CtrAcmaLockup": s5CtrAcmaLockup}
)
