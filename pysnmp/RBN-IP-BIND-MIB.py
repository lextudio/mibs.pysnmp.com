# SNMP MIB module (RBN-IP-BIND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-IP-BIND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:11 2024
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnCircuitHandle,) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnCircuitHandle")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

rbnIpBindMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26)
)
rbnIpBindMib.setRevisions(
        ("2002-08-20 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnIpBindMibNotifications_ObjectIdentity = ObjectIdentity
rbnIpBindMibNotifications = _RbnIpBindMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 0)
)
_RbnIpBindMibObjects_ObjectIdentity = ObjectIdentity
rbnIpBindMibObjects = _RbnIpBindMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 1)
)
_RbnIpBindTable_Object = MibTable
rbnIpBindTable = _RbnIpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1)
)
if mibBuilder.loadTexts:
    rbnIpBindTable.setStatus("current")
_RbnIpBindEntry_Object = MibTableRow
rbnIpBindEntry = _RbnIpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1)
)
rbnIpBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RBN-IP-BIND-MIB", "rbnIpBindCircuitHandle"),
)
if mibBuilder.loadTexts:
    rbnIpBindEntry.setStatus("current")
_RbnIpBindCircuitHandle_Type = RbnCircuitHandle
_RbnIpBindCircuitHandle_Object = MibTableColumn
rbnIpBindCircuitHandle = _RbnIpBindCircuitHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 1),
    _RbnIpBindCircuitHandle_Type()
)
rbnIpBindCircuitHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnIpBindCircuitHandle.setStatus("current")
_RbnIpBindIfIndex_Type = InterfaceIndexOrZero
_RbnIpBindIfIndex_Object = MibTableColumn
rbnIpBindIfIndex = _RbnIpBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 2),
    _RbnIpBindIfIndex_Type()
)
rbnIpBindIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpBindIfIndex.setStatus("current")
_RbnIpBindHierarchicalIfIndex_Type = InterfaceIndexOrZero
_RbnIpBindHierarchicalIfIndex_Object = MibTableColumn
rbnIpBindHierarchicalIfIndex = _RbnIpBindHierarchicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 3),
    _RbnIpBindHierarchicalIfIndex_Type()
)
rbnIpBindHierarchicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpBindHierarchicalIfIndex.setStatus("current")


class _RbnIpBindCircuitDescr_Type(SnmpAdminString):
    """Custom type rbnIpBindCircuitDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 192),
    )


_RbnIpBindCircuitDescr_Type.__name__ = "SnmpAdminString"
_RbnIpBindCircuitDescr_Object = MibTableColumn
rbnIpBindCircuitDescr = _RbnIpBindCircuitDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 4),
    _RbnIpBindCircuitDescr_Type()
)
rbnIpBindCircuitDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpBindCircuitDescr.setStatus("current")


class _RbnIpBindContextName_Type(SnmpAdminString):
    """Custom type rbnIpBindContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RbnIpBindContextName_Type.__name__ = "SnmpAdminString"
_RbnIpBindContextName_Object = MibTableColumn
rbnIpBindContextName = _RbnIpBindContextName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 5),
    _RbnIpBindContextName_Type()
)
rbnIpBindContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIpBindContextName.setStatus("current")
_RbnIpBindMibConformance_ObjectIdentity = ObjectIdentity
rbnIpBindMibConformance = _RbnIpBindMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 2)
)
_RbnIpBindCompliances_ObjectIdentity = ObjectIdentity
rbnIpBindCompliances = _RbnIpBindCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 2, 1)
)
_RbnIpBindGroups_ObjectIdentity = ObjectIdentity
rbnIpBindGroups = _RbnIpBindGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 2, 2)
)

# Managed Objects groups

rbnIpBindDisplayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 2, 2, 1)
)
rbnIpBindDisplayGroup.setObjects(
      *(("RBN-IP-BIND-MIB", "rbnIpBindIfIndex"),
        ("RBN-IP-BIND-MIB", "rbnIpBindHierarchicalIfIndex"),
        ("RBN-IP-BIND-MIB", "rbnIpBindCircuitDescr"),
        ("RBN-IP-BIND-MIB", "rbnIpBindContextName"))
)
if mibBuilder.loadTexts:
    rbnIpBindDisplayGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnIpBindCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 26, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnIpBindCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-IP-BIND-MIB",
    **{"rbnIpBindMib": rbnIpBindMib,
       "rbnIpBindMibNotifications": rbnIpBindMibNotifications,
       "rbnIpBindMibObjects": rbnIpBindMibObjects,
       "rbnIpBindTable": rbnIpBindTable,
       "rbnIpBindEntry": rbnIpBindEntry,
       "rbnIpBindCircuitHandle": rbnIpBindCircuitHandle,
       "rbnIpBindIfIndex": rbnIpBindIfIndex,
       "rbnIpBindHierarchicalIfIndex": rbnIpBindHierarchicalIfIndex,
       "rbnIpBindCircuitDescr": rbnIpBindCircuitDescr,
       "rbnIpBindContextName": rbnIpBindContextName,
       "rbnIpBindMibConformance": rbnIpBindMibConformance,
       "rbnIpBindCompliances": rbnIpBindCompliances,
       "rbnIpBindCompliance": rbnIpBindCompliance,
       "rbnIpBindGroups": rbnIpBindGroups,
       "rbnIpBindDisplayGroup": rbnIpBindDisplayGroup}
)
