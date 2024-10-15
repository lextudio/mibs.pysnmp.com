# SNMP MIB module (A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:55 2024
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_SwitchingSystemsMibs_ObjectIdentity = ObjectIdentity
switchingSystemsMibs = _SwitchingSystemsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29)
)
_A3ComSwitchingSystemsMib_ObjectIdentity = ObjectIdentity
a3ComSwitchingSystemsMib = _A3ComSwitchingSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4)
)
_A3ComWebConfig_ObjectIdentity = ObjectIdentity
a3ComWebConfig = _A3ComWebConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 24)
)


class _A3ComWebConfigHelpServer_Type(DisplayString):
    """Custom type a3ComWebConfigHelpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 85),
    )


_A3ComWebConfigHelpServer_Type.__name__ = "DisplayString"
_A3ComWebConfigHelpServer_Object = MibScalar
a3ComWebConfigHelpServer = _A3ComWebConfigHelpServer_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 24, 1),
    _A3ComWebConfigHelpServer_Type()
)
a3ComWebConfigHelpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComWebConfigHelpServer.setStatus("mandatory")


class _A3ComWebConfigEmailServerAddress_Type(DisplayString):
    """Custom type a3ComWebConfigEmailServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 85),
    )


_A3ComWebConfigEmailServerAddress_Type.__name__ = "DisplayString"
_A3ComWebConfigEmailServerAddress_Object = MibScalar
a3ComWebConfigEmailServerAddress = _A3ComWebConfigEmailServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 24, 2),
    _A3ComWebConfigEmailServerAddress_Type()
)
a3ComWebConfigEmailServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComWebConfigEmailServerAddress.setStatus("mandatory")


class _A3ComWebConfigEmailAddresses_Type(DisplayString):
    """Custom type a3ComWebConfigEmailAddresses based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_A3ComWebConfigEmailAddresses_Type.__name__ = "DisplayString"
_A3ComWebConfigEmailAddresses_Object = MibScalar
a3ComWebConfigEmailAddresses = _A3ComWebConfigEmailAddresses_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 24, 3),
    _A3ComWebConfigEmailAddresses_Type()
)
a3ComWebConfigEmailAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComWebConfigEmailAddresses.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB",
    **{"a3Com": a3Com,
       "switchingSystemsMibs": switchingSystemsMibs,
       "a3ComSwitchingSystemsMib": a3ComSwitchingSystemsMib,
       "a3ComWebConfig": a3ComWebConfig,
       "a3ComWebConfigHelpServer": a3ComWebConfigHelpServer,
       "a3ComWebConfigEmailServerAddress": a3ComWebConfigEmailServerAddress,
       "a3ComWebConfigEmailAddresses": a3ComWebConfigEmailAddresses}
)
