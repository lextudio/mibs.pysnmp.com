# SNMP MIB module (ZYXEL-L2PT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-L2PT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:09 2024
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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelL2pt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 39)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelL2ptSetup_ObjectIdentity = ObjectIdentity
zyxelL2ptSetup = _ZyxelL2ptSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 39, 1)
)
_ZyL2ptState_Type = EnabledStatus
_ZyL2ptState_Object = MibScalar
zyL2ptState = _ZyL2ptState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 39, 1, 1),
    _ZyL2ptState_Type()
)
zyL2ptState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyL2ptState.setStatus("current")
_ZyL2ptMacAddress_Type = MacAddress
_ZyL2ptMacAddress_Object = MibScalar
zyL2ptMacAddress = _ZyL2ptMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 39, 1, 2),
    _ZyL2ptMacAddress_Type()
)
zyL2ptMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyL2ptMacAddress.setStatus("current")
_ZyxelL2ptTable_Object = MibTable
zyxelL2ptTable = _ZyxelL2ptTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 39, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelL2ptTable.setStatus("current")
_ZyxelL2ptEntry_Object = MibTableRow
zyxelL2ptEntry = _ZyxelL2ptEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 39, 1, 3, 1)
)
zyxelL2ptEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelL2ptEntry.setStatus("current")


class _ZyL2ptProtocolGroup_Type(Bits):
    """Custom type zyL2ptProtocolGroup based on Bits"""
    namedValues = NamedValues(
        *(("cdp", 0),
          ("stp", 1),
          ("vtp", 2))
    )

_ZyL2ptProtocolGroup_Type.__name__ = "Bits"
_ZyL2ptProtocolGroup_Object = MibTableColumn
zyL2ptProtocolGroup = _ZyL2ptProtocolGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 39, 1, 3, 1, 1),
    _ZyL2ptProtocolGroup_Type()
)
zyL2ptProtocolGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyL2ptProtocolGroup.setStatus("current")


class _ZyL2ptPointToPointProtocolGroup_Type(Bits):
    """Custom type zyL2ptPointToPointProtocolGroup based on Bits"""
    namedValues = NamedValues(
        *(("lacp", 1),
          ("pagp", 0),
          ("udld", 2))
    )

_ZyL2ptPointToPointProtocolGroup_Type.__name__ = "Bits"
_ZyL2ptPointToPointProtocolGroup_Object = MibTableColumn
zyL2ptPointToPointProtocolGroup = _ZyL2ptPointToPointProtocolGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 39, 1, 3, 1, 2),
    _ZyL2ptPointToPointProtocolGroup_Type()
)
zyL2ptPointToPointProtocolGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyL2ptPointToPointProtocolGroup.setStatus("current")


class _ZyL2ptMode_Type(Integer32):
    """Custom type zyL2ptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("tunnel", 2))
    )


_ZyL2ptMode_Type.__name__ = "Integer32"
_ZyL2ptMode_Object = MibTableColumn
zyL2ptMode = _ZyL2ptMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 39, 1, 3, 1, 3),
    _ZyL2ptMode_Type()
)
zyL2ptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyL2ptMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-L2PT-MIB",
    **{"zyxelL2pt": zyxelL2pt,
       "zyxelL2ptSetup": zyxelL2ptSetup,
       "zyL2ptState": zyL2ptState,
       "zyL2ptMacAddress": zyL2ptMacAddress,
       "zyxelL2ptTable": zyxelL2ptTable,
       "zyxelL2ptEntry": zyxelL2ptEntry,
       "zyL2ptProtocolGroup": zyL2ptProtocolGroup,
       "zyL2ptPointToPointProtocolGroup": zyL2ptPointToPointProtocolGroup,
       "zyL2ptMode": zyL2ptMode}
)
