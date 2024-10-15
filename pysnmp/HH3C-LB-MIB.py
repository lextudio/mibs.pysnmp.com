# SNMP MIB module (HH3C-LB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:46 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cLB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116)
)
hh3cLB.setRevisions(
        ("2010-12-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cLBTables_ObjectIdentity = ObjectIdentity
hh3cLBTables = _Hh3cLBTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116, 1)
)
_Hh3cLBRealServerGroupTable_Object = MibTable
hh3cLBRealServerGroupTable = _Hh3cLBRealServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cLBRealServerGroupTable.setStatus("current")
_Hh3cLBRealServerGroupEntry_Object = MibTableRow
hh3cLBRealServerGroupEntry = _Hh3cLBRealServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 1, 1)
)
hh3cLBRealServerGroupEntry.setIndexNames(
    (0, "HH3C-LB-MIB", "hh3cLBRealServerGroupName"),
)
if mibBuilder.loadTexts:
    hh3cLBRealServerGroupEntry.setStatus("current")


class _Hh3cLBRealServerGroupName_Type(DisplayString):
    """Custom type hh3cLBRealServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cLBRealServerGroupName_Type.__name__ = "DisplayString"
_Hh3cLBRealServerGroupName_Object = MibTableColumn
hh3cLBRealServerGroupName = _Hh3cLBRealServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 1, 1, 1),
    _Hh3cLBRealServerGroupName_Type()
)
hh3cLBRealServerGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLBRealServerGroupName.setStatus("current")
_Hh3cLBRealServerTable_Object = MibTable
hh3cLBRealServerTable = _Hh3cLBRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cLBRealServerTable.setStatus("current")
_Hh3cLBRealServerEntry_Object = MibTableRow
hh3cLBRealServerEntry = _Hh3cLBRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 2, 1)
)
hh3cLBRealServerEntry.setIndexNames(
    (0, "HH3C-LB-MIB", "hh3cLBRealServerGroupName"),
    (0, "HH3C-LB-MIB", "hh3cLBRealServerName"),
)
if mibBuilder.loadTexts:
    hh3cLBRealServerEntry.setStatus("current")


class _Hh3cLBRealServerName_Type(DisplayString):
    """Custom type hh3cLBRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cLBRealServerName_Type.__name__ = "DisplayString"
_Hh3cLBRealServerName_Object = MibTableColumn
hh3cLBRealServerName = _Hh3cLBRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 2, 1, 1),
    _Hh3cLBRealServerName_Type()
)
hh3cLBRealServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLBRealServerName.setStatus("current")


class _Hh3cLBRealServerStatus_Type(Integer32):
    """Custom type hh3cLBRealServerStatus based on Integer32"""
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


_Hh3cLBRealServerStatus_Type.__name__ = "Integer32"
_Hh3cLBRealServerStatus_Object = MibTableColumn
hh3cLBRealServerStatus = _Hh3cLBRealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 2, 1, 2),
    _Hh3cLBRealServerStatus_Type()
)
hh3cLBRealServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLBRealServerStatus.setStatus("current")
_Hh3cLBRealServerConnectNumber_Type = Integer32
_Hh3cLBRealServerConnectNumber_Object = MibTableColumn
hh3cLBRealServerConnectNumber = _Hh3cLBRealServerConnectNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 2, 1, 3),
    _Hh3cLBRealServerConnectNumber_Type()
)
hh3cLBRealServerConnectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLBRealServerConnectNumber.setStatus("current")
_Hh3cLBTrap_ObjectIdentity = ObjectIdentity
hh3cLBTrap = _Hh3cLBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116, 2)
)
_Hh3cLBTrapPrex_ObjectIdentity = ObjectIdentity
hh3cLBTrapPrex = _Hh3cLBTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cLBRealServerOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116, 2, 0, 1)
)
hh3cLBRealServerOverLoad.setObjects(
      *(("HH3C-LB-MIB", "hh3cLBRealServerGroupName"),
        ("HH3C-LB-MIB", "hh3cLBRealServerName"),
        ("HH3C-LB-MIB", "hh3cLBRealServerConnectNumber"))
)
if mibBuilder.loadTexts:
    hh3cLBRealServerOverLoad.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LB-MIB",
    **{"hh3cLB": hh3cLB,
       "hh3cLBTables": hh3cLBTables,
       "hh3cLBRealServerGroupTable": hh3cLBRealServerGroupTable,
       "hh3cLBRealServerGroupEntry": hh3cLBRealServerGroupEntry,
       "hh3cLBRealServerGroupName": hh3cLBRealServerGroupName,
       "hh3cLBRealServerTable": hh3cLBRealServerTable,
       "hh3cLBRealServerEntry": hh3cLBRealServerEntry,
       "hh3cLBRealServerName": hh3cLBRealServerName,
       "hh3cLBRealServerStatus": hh3cLBRealServerStatus,
       "hh3cLBRealServerConnectNumber": hh3cLBRealServerConnectNumber,
       "hh3cLBTrap": hh3cLBTrap,
       "hh3cLBTrapPrex": hh3cLBTrapPrex,
       "hh3cLBRealServerOverLoad": hh3cLBRealServerOverLoad}
)
