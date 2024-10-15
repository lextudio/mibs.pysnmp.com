# SNMP MIB module (H3C-LB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-LB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:48 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cLB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116)
)
h3cLB.setRevisions(
        ("2010-12-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cLBTables_ObjectIdentity = ObjectIdentity
h3cLBTables = _H3cLBTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1)
)
_H3cLBRealServerGroupTable_Object = MibTable
h3cLBRealServerGroupTable = _H3cLBRealServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 1)
)
if mibBuilder.loadTexts:
    h3cLBRealServerGroupTable.setStatus("current")
_H3cLBRealServerGroupEntry_Object = MibTableRow
h3cLBRealServerGroupEntry = _H3cLBRealServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 1, 1)
)
h3cLBRealServerGroupEntry.setIndexNames(
    (0, "H3C-LB-MIB", "h3cLBRealServerGroupName"),
)
if mibBuilder.loadTexts:
    h3cLBRealServerGroupEntry.setStatus("current")


class _H3cLBRealServerGroupName_Type(DisplayString):
    """Custom type h3cLBRealServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cLBRealServerGroupName_Type.__name__ = "DisplayString"
_H3cLBRealServerGroupName_Object = MibTableColumn
h3cLBRealServerGroupName = _H3cLBRealServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 1, 1, 1),
    _H3cLBRealServerGroupName_Type()
)
h3cLBRealServerGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBRealServerGroupName.setStatus("current")
_H3cLBRealServerTable_Object = MibTable
h3cLBRealServerTable = _H3cLBRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 2)
)
if mibBuilder.loadTexts:
    h3cLBRealServerTable.setStatus("current")
_H3cLBRealServerEntry_Object = MibTableRow
h3cLBRealServerEntry = _H3cLBRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 2, 1)
)
h3cLBRealServerEntry.setIndexNames(
    (0, "H3C-LB-MIB", "h3cLBRealServerGroupName"),
    (0, "H3C-LB-MIB", "h3cLBRealServerName"),
)
if mibBuilder.loadTexts:
    h3cLBRealServerEntry.setStatus("current")


class _H3cLBRealServerName_Type(DisplayString):
    """Custom type h3cLBRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cLBRealServerName_Type.__name__ = "DisplayString"
_H3cLBRealServerName_Object = MibTableColumn
h3cLBRealServerName = _H3cLBRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 2, 1, 1),
    _H3cLBRealServerName_Type()
)
h3cLBRealServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBRealServerName.setStatus("current")


class _H3cLBRealServerStatus_Type(Integer32):
    """Custom type h3cLBRealServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("slowdown", 3))
    )


_H3cLBRealServerStatus_Type.__name__ = "Integer32"
_H3cLBRealServerStatus_Object = MibTableColumn
h3cLBRealServerStatus = _H3cLBRealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 2, 1, 2),
    _H3cLBRealServerStatus_Type()
)
h3cLBRealServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLBRealServerStatus.setStatus("current")
_H3cLBRealServerConnectNumber_Type = Integer32
_H3cLBRealServerConnectNumber_Object = MibTableColumn
h3cLBRealServerConnectNumber = _H3cLBRealServerConnectNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 1, 2, 1, 3),
    _H3cLBRealServerConnectNumber_Type()
)
h3cLBRealServerConnectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBRealServerConnectNumber.setStatus("current")
_H3cLBTrap_ObjectIdentity = ObjectIdentity
h3cLBTrap = _H3cLBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 2)
)
_H3cLBTrapPrex_ObjectIdentity = ObjectIdentity
h3cLBTrapPrex = _H3cLBTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cLBRealServerOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 116, 2, 0, 1)
)
h3cLBRealServerOverLoad.setObjects(
      *(("H3C-LB-MIB", "h3cLBRealServerGroupName"),
        ("H3C-LB-MIB", "h3cLBRealServerName"),
        ("H3C-LB-MIB", "h3cLBRealServerConnectNumber"))
)
if mibBuilder.loadTexts:
    h3cLBRealServerOverLoad.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-LB-MIB",
    **{"h3cLB": h3cLB,
       "h3cLBTables": h3cLBTables,
       "h3cLBRealServerGroupTable": h3cLBRealServerGroupTable,
       "h3cLBRealServerGroupEntry": h3cLBRealServerGroupEntry,
       "h3cLBRealServerGroupName": h3cLBRealServerGroupName,
       "h3cLBRealServerTable": h3cLBRealServerTable,
       "h3cLBRealServerEntry": h3cLBRealServerEntry,
       "h3cLBRealServerName": h3cLBRealServerName,
       "h3cLBRealServerStatus": h3cLBRealServerStatus,
       "h3cLBRealServerConnectNumber": h3cLBRealServerConnectNumber,
       "h3cLBTrap": h3cLBTrap,
       "h3cLBTrapPrex": h3cLBTrapPrex,
       "h3cLBRealServerOverLoad": h3cLBRealServerOverLoad}
)
