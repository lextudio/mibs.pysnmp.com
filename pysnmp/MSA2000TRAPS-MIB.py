# SNMP MIB module (MSA2000TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSA2000TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:52 2024
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

(connUnitEventDescr,
 connUnitEventId,
 connUnitEventType) = mibBuilder.importSymbols(
    "FCMGMT-MIB",
    "connUnitEventDescr",
    "connUnitEventId",
    "connUnitEventType")

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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_HpMSA_ObjectIdentity = ObjectIdentity
hpMSA = _HpMSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 51)
)
_MibName_Type = Integer32
_MibName_Object = MibScalar
mibName = _MibName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 51, 1),
    _MibName_Type()
)
mibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

msaEventInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 51, 0, 3001)
)
msaEventInfoTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    msaEventInfoTrap.setStatus(
        ""
    )

msaEventWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 51, 0, 3002)
)
msaEventWarningTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    msaEventWarningTrap.setStatus(
        ""
    )

msaEventErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 51, 0, 3003)
)
msaEventErrorTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    msaEventErrorTrap.setStatus(
        ""
    )

msaEventCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 51, 0, 3004)
)
msaEventCriticalTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    msaEventCriticalTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSA2000TRAPS-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpMSA": hpMSA,
       "msaEventInfoTrap": msaEventInfoTrap,
       "msaEventWarningTrap": msaEventWarningTrap,
       "msaEventErrorTrap": msaEventErrorTrap,
       "msaEventCriticalTrap": msaEventCriticalTrap,
       "mibName": mibName}
)
