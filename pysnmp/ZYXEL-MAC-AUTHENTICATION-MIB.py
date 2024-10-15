# SNMP MIB module (ZYXEL-MAC-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-MAC-AUTHENTICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:16 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelMacAuthentication = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMacAuthenticationSetup_ObjectIdentity = ObjectIdentity
zyxelMacAuthenticationSetup = _ZyxelMacAuthenticationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1)
)
_ZyMacAuthenticationState_Type = EnabledStatus
_ZyMacAuthenticationState_Object = MibScalar
zyMacAuthenticationState = _ZyMacAuthenticationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 1),
    _ZyMacAuthenticationState_Type()
)
zyMacAuthenticationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationState.setStatus("current")
_ZyMacAuthenticationNamePrefix_Type = DisplayString
_ZyMacAuthenticationNamePrefix_Object = MibScalar
zyMacAuthenticationNamePrefix = _ZyMacAuthenticationNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 2),
    _ZyMacAuthenticationNamePrefix_Type()
)
zyMacAuthenticationNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationNamePrefix.setStatus("current")
_ZyMacAuthenticationPassword_Type = DisplayString
_ZyMacAuthenticationPassword_Object = MibScalar
zyMacAuthenticationPassword = _ZyMacAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 3),
    _ZyMacAuthenticationPassword_Type()
)
zyMacAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationPassword.setStatus("current")
_ZyMacAuthenticationTimeout_Type = Integer32
_ZyMacAuthenticationTimeout_Object = MibScalar
zyMacAuthenticationTimeout = _ZyMacAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 4),
    _ZyMacAuthenticationTimeout_Type()
)
zyMacAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationTimeout.setStatus("current")
_ZyxelMacAuthenticationPortTable_Object = MibTable
zyxelMacAuthenticationPortTable = _ZyxelMacAuthenticationPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelMacAuthenticationPortTable.setStatus("current")
_ZyxelMacAuthenticationPortEntry_Object = MibTableRow
zyxelMacAuthenticationPortEntry = _ZyxelMacAuthenticationPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 5, 1)
)
zyxelMacAuthenticationPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMacAuthenticationPortEntry.setStatus("current")
_ZyMacAuthenticationPortState_Type = EnabledStatus
_ZyMacAuthenticationPortState_Object = MibTableColumn
zyMacAuthenticationPortState = _ZyMacAuthenticationPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 46, 1, 5, 1, 1),
    _ZyMacAuthenticationPortState_Type()
)
zyMacAuthenticationPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacAuthenticationPortState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MAC-AUTHENTICATION-MIB",
    **{"zyxelMacAuthentication": zyxelMacAuthentication,
       "zyxelMacAuthenticationSetup": zyxelMacAuthenticationSetup,
       "zyMacAuthenticationState": zyMacAuthenticationState,
       "zyMacAuthenticationNamePrefix": zyMacAuthenticationNamePrefix,
       "zyMacAuthenticationPassword": zyMacAuthenticationPassword,
       "zyMacAuthenticationTimeout": zyMacAuthenticationTimeout,
       "zyxelMacAuthenticationPortTable": zyxelMacAuthenticationPortTable,
       "zyxelMacAuthenticationPortEntry": zyxelMacAuthenticationPortEntry,
       "zyMacAuthenticationPortState": zyMacAuthenticationPortState}
)
