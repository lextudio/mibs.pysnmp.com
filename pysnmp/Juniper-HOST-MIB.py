# SNMP MIB module (Juniper-HOST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-HOST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:22 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

juniHostMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33)
)
juniHostMIB.setRevisions(
        ("2004-11-26 00:00",
         "2002-09-16 21:44",
         "2001-05-07 17:02",
         "2000-01-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniHostObjects_ObjectIdentity = ObjectIdentity
juniHostObjects = _JuniHostObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1)
)
_JuniHost_ObjectIdentity = ObjectIdentity
juniHost = _JuniHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1)
)
_JuniHostTable_Object = MibTable
juniHostTable = _JuniHostTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniHostTable.setStatus("current")
_JuniHostEntry_Object = MibTableRow
juniHostEntry = _JuniHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1)
)
juniHostEntry.setIndexNames(
    (1, "Juniper-HOST-MIB", "juniHostName"),
)
if mibBuilder.loadTexts:
    juniHostEntry.setStatus("current")


class _JuniHostName_Type(DisplayString):
    """Custom type juniHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_JuniHostName_Type.__name__ = "DisplayString"
_JuniHostName_Object = MibTableColumn
juniHostName = _JuniHostName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1, 1),
    _JuniHostName_Type()
)
juniHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHostName.setStatus("current")
_JuniHostIpAddress_Type = IpAddress
_JuniHostIpAddress_Object = MibTableColumn
juniHostIpAddress = _JuniHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1, 2),
    _JuniHostIpAddress_Type()
)
juniHostIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHostIpAddress.setStatus("current")


class _JuniHostProtocol_Type(Integer32):
    """Custom type juniHostProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("juniHostFtp", 1),
          ("juniHostTftp", 2))
    )


_JuniHostProtocol_Type.__name__ = "Integer32"
_JuniHostProtocol_Object = MibTableColumn
juniHostProtocol = _JuniHostProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1, 3),
    _JuniHostProtocol_Type()
)
juniHostProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHostProtocol.setStatus("current")


class _JuniHostUserName_Type(DisplayString):
    """Custom type juniHostUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniHostUserName_Type.__name__ = "DisplayString"
_JuniHostUserName_Object = MibTableColumn
juniHostUserName = _JuniHostUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1, 4),
    _JuniHostUserName_Type()
)
juniHostUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHostUserName.setStatus("current")


class _JuniHostUserPassword_Type(DisplayString):
    """Custom type juniHostUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_JuniHostUserPassword_Type.__name__ = "DisplayString"
_JuniHostUserPassword_Object = MibTableColumn
juniHostUserPassword = _JuniHostUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1, 5),
    _JuniHostUserPassword_Type()
)
juniHostUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHostUserPassword.setStatus("current")
_JuniHostRowStatus_Type = RowStatus
_JuniHostRowStatus_Object = MibTableColumn
juniHostRowStatus = _JuniHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1, 6),
    _JuniHostRowStatus_Type()
)
juniHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHostRowStatus.setStatus("current")
_JuniHostMIBConformance_ObjectIdentity = ObjectIdentity
juniHostMIBConformance = _JuniHostMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 4)
)
_JuniHostMIBCompliances_ObjectIdentity = ObjectIdentity
juniHostMIBCompliances = _JuniHostMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 4, 1)
)
_JuniHostMIBGroups_ObjectIdentity = ObjectIdentity
juniHostMIBGroups = _JuniHostMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 4, 2)
)

# Managed Objects groups

juniHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 4, 2, 1)
)
juniHostGroup.setObjects(
      *(("Juniper-HOST-MIB", "juniHostName"),
        ("Juniper-HOST-MIB", "juniHostIpAddress"),
        ("Juniper-HOST-MIB", "juniHostProtocol"),
        ("Juniper-HOST-MIB", "juniHostUserName"),
        ("Juniper-HOST-MIB", "juniHostUserPassword"),
        ("Juniper-HOST-MIB", "juniHostRowStatus"))
)
if mibBuilder.loadTexts:
    juniHostGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniHostCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniHostCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-HOST-MIB",
    **{"juniHostMIB": juniHostMIB,
       "juniHostObjects": juniHostObjects,
       "juniHost": juniHost,
       "juniHostTable": juniHostTable,
       "juniHostEntry": juniHostEntry,
       "juniHostName": juniHostName,
       "juniHostIpAddress": juniHostIpAddress,
       "juniHostProtocol": juniHostProtocol,
       "juniHostUserName": juniHostUserName,
       "juniHostUserPassword": juniHostUserPassword,
       "juniHostRowStatus": juniHostRowStatus,
       "juniHostMIBConformance": juniHostMIBConformance,
       "juniHostMIBCompliances": juniHostMIBCompliances,
       "juniHostCompliance": juniHostCompliance,
       "juniHostMIBGroups": juniHostMIBGroups,
       "juniHostGroup": juniHostGroup}
)
