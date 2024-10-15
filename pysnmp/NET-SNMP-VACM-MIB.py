# SNMP MIB module (NET-SNMP-VACM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NET-SNMP-VACM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:27 2024
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

(netSnmpGroups,
 netSnmpObjects) = mibBuilder.importSymbols(
    "NET-SNMP-MIB",
    "netSnmpGroups",
    "netSnmpObjects")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(vacmAccessContextPrefix,
 vacmAccessSecurityLevel,
 vacmAccessSecurityModel,
 vacmGroupName) = mibBuilder.importSymbols(
    "SNMP-VIEW-BASED-ACM-MIB",
    "vacmAccessContextPrefix",
    "vacmAccessSecurityLevel",
    "vacmAccessSecurityModel",
    "vacmGroupName")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

netSnmpVacmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 9)
)
netSnmpVacmMIB.setRevisions(
        ("2006-08-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVacmAccessTable_Object = MibTable
nsVacmAccessTable = _NsVacmAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 9, 1)
)
if mibBuilder.loadTexts:
    nsVacmAccessTable.setStatus("current")
_NsVacmAccessEntry_Object = MibTableRow
nsVacmAccessEntry = _NsVacmAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 9, 1, 1)
)
nsVacmAccessEntry.setIndexNames(
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmGroupName"),
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessContextPrefix"),
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessSecurityModel"),
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessSecurityLevel"),
    (0, "NET-SNMP-VACM-MIB", "nsVacmAuthType"),
)
if mibBuilder.loadTexts:
    nsVacmAccessEntry.setStatus("current")


class _NsVacmAuthType_Type(SnmpAdminString):
    """Custom type nsVacmAuthType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVacmAuthType_Type.__name__ = "SnmpAdminString"
_NsVacmAuthType_Object = MibTableColumn
nsVacmAuthType = _NsVacmAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 9, 1, 1, 1),
    _NsVacmAuthType_Type()
)
nsVacmAuthType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsVacmAuthType.setStatus("current")


class _NsVacmContextMatch_Type(Integer32):
    """Custom type nsVacmContextMatch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exact", 1),
          ("prefix", 2))
    )


_NsVacmContextMatch_Type.__name__ = "Integer32"
_NsVacmContextMatch_Object = MibTableColumn
nsVacmContextMatch = _NsVacmContextMatch_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 9, 1, 1, 2),
    _NsVacmContextMatch_Type()
)
nsVacmContextMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVacmContextMatch.setStatus("current")


class _NsVacmViewName_Type(SnmpAdminString):
    """Custom type nsVacmViewName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVacmViewName_Type.__name__ = "SnmpAdminString"
_NsVacmViewName_Object = MibTableColumn
nsVacmViewName = _NsVacmViewName_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 9, 1, 1, 3),
    _NsVacmViewName_Type()
)
nsVacmViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVacmViewName.setStatus("current")


class _NsVacmStorageType_Type(StorageType):
    """Custom type nsVacmStorageType based on StorageType"""


_NsVacmStorageType_Object = MibTableColumn
nsVacmStorageType = _NsVacmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 9, 1, 1, 4),
    _NsVacmStorageType_Type()
)
nsVacmStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVacmStorageType.setStatus("current")
_NsVacmStatus_Type = RowStatus
_NsVacmStatus_Object = MibTableColumn
nsVacmStatus = _NsVacmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8072, 1, 9, 1, 1, 5),
    _NsVacmStatus_Type()
)
nsVacmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVacmStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NET-SNMP-VACM-MIB",
    **{"netSnmpVacmMIB": netSnmpVacmMIB,
       "nsVacmAccessTable": nsVacmAccessTable,
       "nsVacmAccessEntry": nsVacmAccessEntry,
       "nsVacmAuthType": nsVacmAuthType,
       "nsVacmContextMatch": nsVacmContextMatch,
       "nsVacmViewName": nsVacmViewName,
       "nsVacmStorageType": nsVacmStorageType,
       "nsVacmStatus": nsVacmStatus}
)
