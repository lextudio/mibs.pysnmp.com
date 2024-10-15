# SNMP MIB module (PET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:32 2024
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

_Wired_for_management_ObjectIdentity = ObjectIdentity
wired_for_management = _Wired_for_management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183)
)
_PET_ObjectIdentity = ObjectIdentity
pET = _PET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1)
)
_PET_version_1_ObjectIdentity = ObjectIdentity
pET_version_1 = _PET_version_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1)
)


class _PETTrap_Type(OctetString):
    """Custom type pETTrap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(110, 110),
    )


_PETTrap_Type.__name__ = "OctetString"
_PETTrap_Object = MibScalar
pETTrap = _PETTrap_Object(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 1),
    _PETTrap_Type()
)
pETTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pETTrap.setStatus("current")

# Managed Objects groups


# Notification objects

pET_Temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 93952)
)
if mibBuilder.loadTexts:
    pET_Temperature.setStatus(
        ""
    )

pET_Voltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 159488)
)
if mibBuilder.loadTexts:
    pET_Voltage.setStatus(
        ""
    )

pET_Fan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 290560)
)
if mibBuilder.loadTexts:
    pET_Fan.setStatus(
        ""
    )

pET_CoverTamper = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 356096)
)
if mibBuilder.loadTexts:
    pET_CoverTamper.setStatus(
        ""
    )

pET_ProcessorMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 356099)
)
if mibBuilder.loadTexts:
    pET_ProcessorMissing.setStatus(
        ""
    )

pET_LANLeash = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 356100)
)
if mibBuilder.loadTexts:
    pET_LANLeash.setStatus(
        ""
    )

pET_Undock = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 356101)
)
if mibBuilder.loadTexts:
    pET_Undock.setStatus(
        ""
    )

pET_ProcessorTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487169)
)
if mibBuilder.loadTexts:
    pET_ProcessorTemperature.setStatus(
        ""
    )

pET_Voltage_Fan_Temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552706)
)
if mibBuilder.loadTexts:
    pET_Voltage_Fan_Temperature.setStatus(
        ""
    )

pET_Fan_Temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 683778)
)
if mibBuilder.loadTexts:
    pET_Fan_Temperature.setStatus(
        ""
    )

pET_P_O_S_T = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1011456)
)
if mibBuilder.loadTexts:
    pET_P_O_S_T.setStatus(
        ""
    )

pET_EventClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1076994)
)
if mibBuilder.loadTexts:
    pET_EventClear.setStatus(
        ""
    )

pET_Watchdog = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1142534)
)
if mibBuilder.loadTexts:
    pET_Watchdog.setStatus(
        ""
    )

pET_AlertOnLAN = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2277391)
)
if mibBuilder.loadTexts:
    pET_AlertOnLAN.setStatus(
        ""
    )

pET_PresenceHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2584320)
)
if mibBuilder.loadTexts:
    pET_PresenceHeartbeat.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PET-MIB",
    **{"wired-for-management": wired_for_management,
       "pET": pET,
       "pET-version-1": pET_version_1,
       "pET-Temperature": pET_Temperature,
       "pET-Voltage": pET_Voltage,
       "pET-Fan": pET_Fan,
       "pET-CoverTamper": pET_CoverTamper,
       "pET-ProcessorMissing": pET_ProcessorMissing,
       "pET-LANLeash": pET_LANLeash,
       "pET-Undock": pET_Undock,
       "pET-ProcessorTemperature": pET_ProcessorTemperature,
       "pET-Voltage-Fan-Temperature": pET_Voltage_Fan_Temperature,
       "pET-Fan-Temperature": pET_Fan_Temperature,
       "pET-P-O-S-T": pET_P_O_S_T,
       "pET-EventClear": pET_EventClear,
       "pET-Watchdog": pET_Watchdog,
       "pET-AlertOnLAN": pET_AlertOnLAN,
       "pET-PresenceHeartbeat": pET_PresenceHeartbeat,
       "pETTrap": pETTrap}
)
