# SNMP MIB module (ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:27 2024
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

zyxelBridgeControlProtocolTransparency = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelBridgeControlProtocolTransparencySetup_ObjectIdentity = ObjectIdentity
zyxelBridgeControlProtocolTransparencySetup = _ZyxelBridgeControlProtocolTransparencySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1)
)
_ZyBridgeControlProtocolTransparencyState_Type = EnabledStatus
_ZyBridgeControlProtocolTransparencyState_Object = MibScalar
zyBridgeControlProtocolTransparencyState = _ZyBridgeControlProtocolTransparencyState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 1),
    _ZyBridgeControlProtocolTransparencyState_Type()
)
zyBridgeControlProtocolTransparencyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyBridgeControlProtocolTransparencyState.setStatus("current")
_ZyxelBridgeControlProtocolTransparencyPortTable_Object = MibTable
zyxelBridgeControlProtocolTransparencyPortTable = _ZyxelBridgeControlProtocolTransparencyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelBridgeControlProtocolTransparencyPortTable.setStatus("current")
_ZyxelBridgeControlProtocolTransparencyPortEntry_Object = MibTableRow
zyxelBridgeControlProtocolTransparencyPortEntry = _ZyxelBridgeControlProtocolTransparencyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 2, 1)
)
zyxelBridgeControlProtocolTransparencyPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelBridgeControlProtocolTransparencyPortEntry.setStatus("current")


class _ZyBridgeControlProtocolTransparencyPortMode_Type(Integer32):
    """Custom type zyBridgeControlProtocolTransparencyPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("network", 3),
          ("peer", 0),
          ("tunnel", 1))
    )


_ZyBridgeControlProtocolTransparencyPortMode_Type.__name__ = "Integer32"
_ZyBridgeControlProtocolTransparencyPortMode_Object = MibTableColumn
zyBridgeControlProtocolTransparencyPortMode = _ZyBridgeControlProtocolTransparencyPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 15, 1, 2, 1, 1),
    _ZyBridgeControlProtocolTransparencyPortMode_Type()
)
zyBridgeControlProtocolTransparencyPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyBridgeControlProtocolTransparencyPortMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB",
    **{"zyxelBridgeControlProtocolTransparency": zyxelBridgeControlProtocolTransparency,
       "zyxelBridgeControlProtocolTransparencySetup": zyxelBridgeControlProtocolTransparencySetup,
       "zyBridgeControlProtocolTransparencyState": zyBridgeControlProtocolTransparencyState,
       "zyxelBridgeControlProtocolTransparencyPortTable": zyxelBridgeControlProtocolTransparencyPortTable,
       "zyxelBridgeControlProtocolTransparencyPortEntry": zyxelBridgeControlProtocolTransparencyPortEntry,
       "zyBridgeControlProtocolTransparencyPortMode": zyBridgeControlProtocolTransparencyPortMode}
)
