# SNMP MIB module (SNMP-PROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP-PROXY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:57 2024
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

(SnmpAdminString,
 SnmpEngineID) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID")

(SnmpTagValue,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagValue")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

snmpProxyMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 14)
)
snmpProxyMIB.setRevisions(
        ("2002-10-14 00:00",
         "1998-08-04 00:00",
         "1997-07-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpProxyObjects_ObjectIdentity = ObjectIdentity
snmpProxyObjects = _SnmpProxyObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 14, 1)
)
_SnmpProxyTable_Object = MibTable
snmpProxyTable = _SnmpProxyTable_Object(
    (1, 3, 6, 1, 6, 3, 14, 1, 2)
)
if mibBuilder.loadTexts:
    snmpProxyTable.setStatus("current")
_SnmpProxyEntry_Object = MibTableRow
snmpProxyEntry = _SnmpProxyEntry_Object(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1)
)
snmpProxyEntry.setIndexNames(
    (1, "SNMP-PROXY-MIB", "snmpProxyName"),
)
if mibBuilder.loadTexts:
    snmpProxyEntry.setStatus("current")


class _SnmpProxyName_Type(SnmpAdminString):
    """Custom type snmpProxyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpProxyName_Type.__name__ = "SnmpAdminString"
_SnmpProxyName_Object = MibTableColumn
snmpProxyName = _SnmpProxyName_Object(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 1),
    _SnmpProxyName_Type()
)
snmpProxyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpProxyName.setStatus("current")


class _SnmpProxyType_Type(Integer32):
    """Custom type snmpProxyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inform", 4),
          ("read", 1),
          ("trap", 3),
          ("write", 2))
    )


_SnmpProxyType_Type.__name__ = "Integer32"
_SnmpProxyType_Object = MibTableColumn
snmpProxyType = _SnmpProxyType_Object(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 2),
    _SnmpProxyType_Type()
)
snmpProxyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyType.setStatus("current")
_SnmpProxyContextEngineID_Type = SnmpEngineID
_SnmpProxyContextEngineID_Object = MibTableColumn
snmpProxyContextEngineID = _SnmpProxyContextEngineID_Object(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 3),
    _SnmpProxyContextEngineID_Type()
)
snmpProxyContextEngineID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyContextEngineID.setStatus("current")
_SnmpProxyContextName_Type = SnmpAdminString
_SnmpProxyContextName_Object = MibTableColumn
snmpProxyContextName = _SnmpProxyContextName_Object(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 4),
    _SnmpProxyContextName_Type()
)
snmpProxyContextName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyContextName.setStatus("current")
_SnmpProxyTargetParamsIn_Type = SnmpAdminString
_SnmpProxyTargetParamsIn_Object = MibTableColumn
snmpProxyTargetParamsIn = _SnmpProxyTargetParamsIn_Object(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 5),
    _SnmpProxyTargetParamsIn_Type()
)
snmpProxyTargetParamsIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyTargetParamsIn.setStatus("current")
_SnmpProxySingleTargetOut_Type = SnmpAdminString
_SnmpProxySingleTargetOut_Object = MibTableColumn
snmpProxySingleTargetOut = _SnmpProxySingleTargetOut_Object(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 6),
    _SnmpProxySingleTargetOut_Type()
)
snmpProxySingleTargetOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxySingleTargetOut.setStatus("current")
_SnmpProxyMultipleTargetOut_Type = SnmpTagValue
_SnmpProxyMultipleTargetOut_Object = MibTableColumn
snmpProxyMultipleTargetOut = _SnmpProxyMultipleTargetOut_Object(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 7),
    _SnmpProxyMultipleTargetOut_Type()
)
snmpProxyMultipleTargetOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyMultipleTargetOut.setStatus("current")


class _SnmpProxyStorageType_Type(StorageType):
    """Custom type snmpProxyStorageType based on StorageType"""


_SnmpProxyStorageType_Object = MibTableColumn
snmpProxyStorageType = _SnmpProxyStorageType_Object(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 8),
    _SnmpProxyStorageType_Type()
)
snmpProxyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyStorageType.setStatus("current")
_SnmpProxyRowStatus_Type = RowStatus
_SnmpProxyRowStatus_Object = MibTableColumn
snmpProxyRowStatus = _SnmpProxyRowStatus_Object(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 9),
    _SnmpProxyRowStatus_Type()
)
snmpProxyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyRowStatus.setStatus("current")
_SnmpProxyConformance_ObjectIdentity = ObjectIdentity
snmpProxyConformance = _SnmpProxyConformance_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 14, 3)
)
_SnmpProxyCompliances_ObjectIdentity = ObjectIdentity
snmpProxyCompliances = _SnmpProxyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 14, 3, 1)
)
_SnmpProxyGroups_ObjectIdentity = ObjectIdentity
snmpProxyGroups = _SnmpProxyGroups_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 14, 3, 2)
)

# Managed Objects groups

snmpProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 14, 3, 2, 3)
)
snmpProxyGroup.setObjects(
      *(("SNMP-PROXY-MIB", "snmpProxyType"),
        ("SNMP-PROXY-MIB", "snmpProxyContextEngineID"),
        ("SNMP-PROXY-MIB", "snmpProxyContextName"),
        ("SNMP-PROXY-MIB", "snmpProxyTargetParamsIn"),
        ("SNMP-PROXY-MIB", "snmpProxySingleTargetOut"),
        ("SNMP-PROXY-MIB", "snmpProxyMultipleTargetOut"),
        ("SNMP-PROXY-MIB", "snmpProxyStorageType"),
        ("SNMP-PROXY-MIB", "snmpProxyRowStatus"))
)
if mibBuilder.loadTexts:
    snmpProxyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpProxyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 14, 3, 1, 1)
)
if mibBuilder.loadTexts:
    snmpProxyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-PROXY-MIB",
    **{"snmpProxyMIB": snmpProxyMIB,
       "snmpProxyObjects": snmpProxyObjects,
       "snmpProxyTable": snmpProxyTable,
       "snmpProxyEntry": snmpProxyEntry,
       "snmpProxyName": snmpProxyName,
       "snmpProxyType": snmpProxyType,
       "snmpProxyContextEngineID": snmpProxyContextEngineID,
       "snmpProxyContextName": snmpProxyContextName,
       "snmpProxyTargetParamsIn": snmpProxyTargetParamsIn,
       "snmpProxySingleTargetOut": snmpProxySingleTargetOut,
       "snmpProxyMultipleTargetOut": snmpProxyMultipleTargetOut,
       "snmpProxyStorageType": snmpProxyStorageType,
       "snmpProxyRowStatus": snmpProxyRowStatus,
       "snmpProxyConformance": snmpProxyConformance,
       "snmpProxyCompliances": snmpProxyCompliances,
       "snmpProxyCompliance": snmpProxyCompliance,
       "snmpProxyGroups": snmpProxyGroups,
       "snmpProxyGroup": snmpProxyGroup}
)
