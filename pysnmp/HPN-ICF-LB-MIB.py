# SNMP MIB module (HPN-ICF-LB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:45 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfLB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116)
)
hpnicfLB.setRevisions(
        ("2010-12-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfLBTables_ObjectIdentity = ObjectIdentity
hpnicfLBTables = _HpnicfLBTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116, 1)
)
_HpnicfLBRealServerGroupTable_Object = MibTable
hpnicfLBRealServerGroupTable = _HpnicfLBRealServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfLBRealServerGroupTable.setStatus("current")
_HpnicfLBRealServerGroupEntry_Object = MibTableRow
hpnicfLBRealServerGroupEntry = _HpnicfLBRealServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116, 1, 1, 1)
)
hpnicfLBRealServerGroupEntry.setIndexNames(
    (0, "HPN-ICF-LB-MIB", "hpnicfLBRealServerGroupName"),
)
if mibBuilder.loadTexts:
    hpnicfLBRealServerGroupEntry.setStatus("current")


class _HpnicfLBRealServerGroupName_Type(DisplayString):
    """Custom type hpnicfLBRealServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfLBRealServerGroupName_Type.__name__ = "DisplayString"
_HpnicfLBRealServerGroupName_Object = MibTableColumn
hpnicfLBRealServerGroupName = _HpnicfLBRealServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116, 1, 1, 1, 1),
    _HpnicfLBRealServerGroupName_Type()
)
hpnicfLBRealServerGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLBRealServerGroupName.setStatus("current")
_HpnicfLBRealServerTable_Object = MibTable
hpnicfLBRealServerTable = _HpnicfLBRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfLBRealServerTable.setStatus("current")
_HpnicfLBRealServerEntry_Object = MibTableRow
hpnicfLBRealServerEntry = _HpnicfLBRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116, 1, 2, 1)
)
hpnicfLBRealServerEntry.setIndexNames(
    (0, "HPN-ICF-LB-MIB", "hpnicfLBRealServerGroupName"),
    (0, "HPN-ICF-LB-MIB", "hpnicfLBRealServerName"),
)
if mibBuilder.loadTexts:
    hpnicfLBRealServerEntry.setStatus("current")


class _HpnicfLBRealServerName_Type(DisplayString):
    """Custom type hpnicfLBRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfLBRealServerName_Type.__name__ = "DisplayString"
_HpnicfLBRealServerName_Object = MibTableColumn
hpnicfLBRealServerName = _HpnicfLBRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116, 1, 2, 1, 1),
    _HpnicfLBRealServerName_Type()
)
hpnicfLBRealServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLBRealServerName.setStatus("current")


class _HpnicfLBRealServerStatus_Type(Integer32):
    """Custom type hpnicfLBRealServerStatus based on Integer32"""
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


_HpnicfLBRealServerStatus_Type.__name__ = "Integer32"
_HpnicfLBRealServerStatus_Object = MibTableColumn
hpnicfLBRealServerStatus = _HpnicfLBRealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116, 1, 2, 1, 2),
    _HpnicfLBRealServerStatus_Type()
)
hpnicfLBRealServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLBRealServerStatus.setStatus("current")
_HpnicfLBRealServerConnectNumber_Type = Integer32
_HpnicfLBRealServerConnectNumber_Object = MibTableColumn
hpnicfLBRealServerConnectNumber = _HpnicfLBRealServerConnectNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116, 1, 2, 1, 3),
    _HpnicfLBRealServerConnectNumber_Type()
)
hpnicfLBRealServerConnectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLBRealServerConnectNumber.setStatus("current")
_HpnicfLBTrap_ObjectIdentity = ObjectIdentity
hpnicfLBTrap = _HpnicfLBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116, 2)
)
_HpnicfLBTrapPrex_ObjectIdentity = ObjectIdentity
hpnicfLBTrapPrex = _HpnicfLBTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116, 2, 0)
)

# Managed Objects groups


# Notification objects

hpnicfLBRealServerOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116, 2, 0, 1)
)
hpnicfLBRealServerOverLoad.setObjects(
      *(("HPN-ICF-LB-MIB", "hpnicfLBRealServerGroupName"),
        ("HPN-ICF-LB-MIB", "hpnicfLBRealServerName"),
        ("HPN-ICF-LB-MIB", "hpnicfLBRealServerConnectNumber"))
)
if mibBuilder.loadTexts:
    hpnicfLBRealServerOverLoad.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LB-MIB",
    **{"hpnicfLB": hpnicfLB,
       "hpnicfLBTables": hpnicfLBTables,
       "hpnicfLBRealServerGroupTable": hpnicfLBRealServerGroupTable,
       "hpnicfLBRealServerGroupEntry": hpnicfLBRealServerGroupEntry,
       "hpnicfLBRealServerGroupName": hpnicfLBRealServerGroupName,
       "hpnicfLBRealServerTable": hpnicfLBRealServerTable,
       "hpnicfLBRealServerEntry": hpnicfLBRealServerEntry,
       "hpnicfLBRealServerName": hpnicfLBRealServerName,
       "hpnicfLBRealServerStatus": hpnicfLBRealServerStatus,
       "hpnicfLBRealServerConnectNumber": hpnicfLBRealServerConnectNumber,
       "hpnicfLBTrap": hpnicfLBTrap,
       "hpnicfLBTrapPrex": hpnicfLBTrapPrex,
       "hpnicfLBRealServerOverLoad": hpnicfLBRealServerOverLoad}
)
