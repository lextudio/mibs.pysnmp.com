# SNMP MIB module (SNMP-VACM-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP-VACM-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:10 2024
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
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpSecurityModel")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

vacmAaaMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 199)
)
vacmAaaMIB.setRevisions(
        ("2010-12-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VacmAaaMIBObjects_ObjectIdentity = ObjectIdentity
vacmAaaMIBObjects = _VacmAaaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 199, 1)
)
_VacmAaaSecurityToGroupTable_Object = MibTable
vacmAaaSecurityToGroupTable = _VacmAaaSecurityToGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 199, 1, 1)
)
if mibBuilder.loadTexts:
    vacmAaaSecurityToGroupTable.setStatus("current")
_VacmAaaSecurityToGroupEntry_Object = MibTableRow
vacmAaaSecurityToGroupEntry = _VacmAaaSecurityToGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 199, 1, 1, 1)
)
vacmAaaSecurityToGroupEntry.setIndexNames(
    (0, "SNMP-VACM-AAA-MIB", "vacmAaaSecurityModel"),
    (0, "SNMP-VACM-AAA-MIB", "vacmAaaSecurityName"),
    (0, "SNMP-VACM-AAA-MIB", "vacmAaaSessionID"),
)
if mibBuilder.loadTexts:
    vacmAaaSecurityToGroupEntry.setStatus("current")


class _VacmAaaSecurityModel_Type(SnmpSecurityModel):
    """Custom type vacmAaaSecurityModel based on SnmpSecurityModel"""
    subtypeSpec = SnmpSecurityModel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VacmAaaSecurityModel_Type.__name__ = "SnmpSecurityModel"
_VacmAaaSecurityModel_Object = MibTableColumn
vacmAaaSecurityModel = _VacmAaaSecurityModel_Object(
    (1, 3, 6, 1, 2, 1, 199, 1, 1, 1, 1),
    _VacmAaaSecurityModel_Type()
)
vacmAaaSecurityModel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vacmAaaSecurityModel.setStatus("current")


class _VacmAaaSecurityName_Type(SnmpAdminString):
    """Custom type vacmAaaSecurityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VacmAaaSecurityName_Type.__name__ = "SnmpAdminString"
_VacmAaaSecurityName_Object = MibTableColumn
vacmAaaSecurityName = _VacmAaaSecurityName_Object(
    (1, 3, 6, 1, 2, 1, 199, 1, 1, 1, 2),
    _VacmAaaSecurityName_Type()
)
vacmAaaSecurityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vacmAaaSecurityName.setStatus("current")
_VacmAaaSessionID_Type = Unsigned32
_VacmAaaSessionID_Object = MibTableColumn
vacmAaaSessionID = _VacmAaaSessionID_Object(
    (1, 3, 6, 1, 2, 1, 199, 1, 1, 1, 3),
    _VacmAaaSessionID_Type()
)
vacmAaaSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vacmAaaSessionID.setStatus("current")


class _VacmAaaGroupName_Type(SnmpAdminString):
    """Custom type vacmAaaGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VacmAaaGroupName_Type.__name__ = "SnmpAdminString"
_VacmAaaGroupName_Object = MibTableColumn
vacmAaaGroupName = _VacmAaaGroupName_Object(
    (1, 3, 6, 1, 2, 1, 199, 1, 1, 1, 4),
    _VacmAaaGroupName_Type()
)
vacmAaaGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vacmAaaGroupName.setStatus("current")
_VacmAaaMIBConformance_ObjectIdentity = ObjectIdentity
vacmAaaMIBConformance = _VacmAaaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 199, 2)
)
_VacmAaaMIBCompliances_ObjectIdentity = ObjectIdentity
vacmAaaMIBCompliances = _VacmAaaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 199, 2, 1)
)
_VacmAaaMIBGroups_ObjectIdentity = ObjectIdentity
vacmAaaMIBGroups = _VacmAaaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 199, 2, 2)
)

# Managed Objects groups

vacmAaaGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 199, 2, 2, 1)
)
vacmAaaGroup.setObjects(
    ("SNMP-VACM-AAA-MIB", "vacmAaaGroupName")
)
if mibBuilder.loadTexts:
    vacmAaaGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vacmAaaMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 199, 2, 1, 1)
)
if mibBuilder.loadTexts:
    vacmAaaMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-VACM-AAA-MIB",
    **{"vacmAaaMIB": vacmAaaMIB,
       "vacmAaaMIBObjects": vacmAaaMIBObjects,
       "vacmAaaSecurityToGroupTable": vacmAaaSecurityToGroupTable,
       "vacmAaaSecurityToGroupEntry": vacmAaaSecurityToGroupEntry,
       "vacmAaaSecurityModel": vacmAaaSecurityModel,
       "vacmAaaSecurityName": vacmAaaSecurityName,
       "vacmAaaSessionID": vacmAaaSessionID,
       "vacmAaaGroupName": vacmAaaGroupName,
       "vacmAaaMIBConformance": vacmAaaMIBConformance,
       "vacmAaaMIBCompliances": vacmAaaMIBCompliances,
       "vacmAaaMIBBasicCompliance": vacmAaaMIBBasicCompliance,
       "vacmAaaMIBGroups": vacmAaaMIBGroups,
       "vacmAaaGroup": vacmAaaGroup}
)
