# SNMP MIB module (BEKARTS-v1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BEKARTS-v1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:49 2024
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

_Bekarts_ObjectIdentity = ObjectIdentity
bekarts = _Bekarts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18514)
)
_Bekarts_software_ObjectIdentity = ObjectIdentity
bekarts_software = _Bekarts_software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18514, 20)
)
_Bekarts_mailshappy_ObjectIdentity = ObjectIdentity
bekarts_mailshappy = _Bekarts_mailshappy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18514, 20, 1)
)
_Bekarts_hardware_ObjectIdentity = ObjectIdentity
bekarts_hardware = _Bekarts_hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18514, 100)
)

# Managed Objects groups


# Notification objects

bekarts_mailshappy_on = NotificationType(
    (1, 3, 6, 1, 4, 1, 18514, 20, 1, 0, 1)
)
if mibBuilder.loadTexts:
    bekarts_mailshappy_on.setStatus(
        ""
    )

bekarts_mailshappy_off = NotificationType(
    (1, 3, 6, 1, 4, 1, 18514, 20, 1, 0, 2)
)
if mibBuilder.loadTexts:
    bekarts_mailshappy_off.setStatus(
        ""
    )

bekarts_mailshappy_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 18514, 20, 1, 0, 3)
)
if mibBuilder.loadTexts:
    bekarts_mailshappy_active.setStatus(
        ""
    )

bekarts_mailshappy_deactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 18514, 20, 1, 0, 4)
)
if mibBuilder.loadTexts:
    bekarts_mailshappy_deactive.setStatus(
        ""
    )

bekarts_mailshappy_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 18514, 20, 1, 0, 5)
)
if mibBuilder.loadTexts:
    bekarts_mailshappy_warning.setStatus(
        ""
    )

bekarts_mailshappy_clear_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 18514, 20, 1, 0, 6)
)
if mibBuilder.loadTexts:
    bekarts_mailshappy_clear_warning.setStatus(
        ""
    )

bekarts_mailshappy_critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 18514, 20, 1, 0, 7)
)
if mibBuilder.loadTexts:
    bekarts_mailshappy_critical.setStatus(
        ""
    )

bekarts_mailshappy_clear_critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 18514, 20, 1, 0, 8)
)
if mibBuilder.loadTexts:
    bekarts_mailshappy_clear_critical.setStatus(
        ""
    )

bekarts_mailshappy_test = NotificationType(
    (1, 3, 6, 1, 4, 1, 18514, 20, 1, 0, 9)
)
if mibBuilder.loadTexts:
    bekarts_mailshappy_test.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEKARTS-v1-MIB",
    **{"bekarts": bekarts,
       "bekarts-software": bekarts_software,
       "bekarts-mailshappy": bekarts_mailshappy,
       "bekarts-mailshappy-on": bekarts_mailshappy_on,
       "bekarts-mailshappy-off": bekarts_mailshappy_off,
       "bekarts-mailshappy-active": bekarts_mailshappy_active,
       "bekarts-mailshappy-deactive": bekarts_mailshappy_deactive,
       "bekarts-mailshappy-warning": bekarts_mailshappy_warning,
       "bekarts-mailshappy-clear-warning": bekarts_mailshappy_clear_warning,
       "bekarts-mailshappy-critical": bekarts_mailshappy_critical,
       "bekarts-mailshappy-clear-critical": bekarts_mailshappy_clear_critical,
       "bekarts-mailshappy-test": bekarts_mailshappy_test,
       "bekarts-hardware": bekarts_hardware}
)
