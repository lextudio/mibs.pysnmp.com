# SNMP MIB module (NTNTECH-NMS-TRAPS-V1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTNTECH-NMS-TRAPS-V1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:45 2024
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

(mumStaFanState,) = mibBuilder.importSymbols(
    "NTNTECH-CHASSIS-STATUS-MIB",
    "mumStaFanState")

(ifStaSlotIndex,
 ifStaType) = mibBuilder.importSymbols(
    "NTNTECH-INTERFACE-MODULE-STATUS-MIB",
    "ifStaSlotIndex",
    "ifStaType")

(ntntechNMSTraps,) = mibBuilder.importSymbols(
    "NTNTECH-ROOT-MIB",
    "ntntechNMSTraps")

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

envFanTrap_v1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3, 0, 1001)
)
envFanTrap_v1.setObjects(
    ("NTNTECH-CHASSIS-STATUS-MIB", "mumStaFanState")
)
if mibBuilder.loadTexts:
    envFanTrap_v1.setStatus(
        ""
    )

envTempNormal_v1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3, 0, 1002)
)
if mibBuilder.loadTexts:
    envTempNormal_v1.setStatus(
        ""
    )

envTempExceeded_v1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3, 0, 1003)
)
if mibBuilder.loadTexts:
    envTempExceeded_v1.setStatus(
        ""
    )

invIfModPresentTrap_v1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3, 0, 2001)
)
invIfModPresentTrap_v1.setObjects(
      *(("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"),
        ("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType"))
)
if mibBuilder.loadTexts:
    invIfModPresentTrap_v1.setStatus(
        ""
    )

invIfModRemovedTrap_v1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3, 0, 2002)
)
invIfModRemovedTrap_v1.setObjects(
      *(("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"),
        ("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType"))
)
if mibBuilder.loadTexts:
    invIfModRemovedTrap_v1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTNTECH-NMS-TRAPS-V1-MIB",
    **{"envFanTrap-v1": envFanTrap_v1,
       "envTempNormal-v1": envTempNormal_v1,
       "envTempExceeded-v1": envTempExceeded_v1,
       "invIfModPresentTrap-v1": invIfModPresentTrap_v1,
       "invIfModRemovedTrap-v1": invIfModRemovedTrap_v1}
)
