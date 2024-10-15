# SNMP MIB module (CISCO-COPS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-COPS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:48 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCopsClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 140)
)
ciscoCopsClientMIB.setRevisions(
        ("2005-11-14 00:00",
         "2000-06-11 00:00",
         "1999-09-16 00:40")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CopsRole(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class CopsRoleCombination(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CopsDomainName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class CopsClientType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("provisioning", 2),
          ("rsvp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CcopsMIBObjects_ObjectIdentity = ObjectIdentity
ccopsMIBObjects = _CcopsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1)
)
_CcopsGlobalObjects_ObjectIdentity = ObjectIdentity
ccopsGlobalObjects = _CcopsGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1)
)


class _CcopsServerMax_Type(Unsigned32):
    """Custom type ccopsServerMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcopsServerMax_Type.__name__ = "Unsigned32"
_CcopsServerMax_Object = MibScalar
ccopsServerMax = _CcopsServerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 1),
    _CcopsServerMax_Type()
)
ccopsServerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccopsServerMax.setStatus("current")
if mibBuilder.loadTexts:
    ccopsServerMax.setUnits("servers")
_CcopsMaxRole_Type = Unsigned32
_CcopsMaxRole_Object = MibScalar
ccopsMaxRole = _CcopsMaxRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 2),
    _CcopsMaxRole_Type()
)
ccopsMaxRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccopsMaxRole.setStatus("current")
if mibBuilder.loadTexts:
    ccopsMaxRole.setUnits("roles")
_CcopsMaxRoleCombination_Type = Unsigned32
_CcopsMaxRoleCombination_Object = MibScalar
ccopsMaxRoleCombination = _CcopsMaxRoleCombination_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 3),
    _CcopsMaxRoleCombination_Type()
)
ccopsMaxRoleCombination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccopsMaxRoleCombination.setStatus("current")
if mibBuilder.loadTexts:
    ccopsMaxRoleCombination.setUnits("role-combinations")
_CcopsServerConfigTable_Object = MibTable
ccopsServerConfigTable = _CcopsServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ccopsServerConfigTable.setStatus("current")
_CcopsServerConfigEntry_Object = MibTableRow
ccopsServerConfigEntry = _CcopsServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1)
)
ccopsServerConfigEntry.setIndexNames(
    (0, "CISCO-COPS-CLIENT-MIB", "ccopsServerConfigClientType"),
    (1, "CISCO-COPS-CLIENT-MIB", "ccopsServerConfigName"),
)
if mibBuilder.loadTexts:
    ccopsServerConfigEntry.setStatus("current")
_CcopsServerConfigClientType_Type = CopsClientType
_CcopsServerConfigClientType_Object = MibTableColumn
ccopsServerConfigClientType = _CcopsServerConfigClientType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 1),
    _CcopsServerConfigClientType_Type()
)
ccopsServerConfigClientType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccopsServerConfigClientType.setStatus("current")


class _CcopsServerConfigName_Type(DisplayString):
    """Custom type ccopsServerConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcopsServerConfigName_Type.__name__ = "DisplayString"
_CcopsServerConfigName_Object = MibTableColumn
ccopsServerConfigName = _CcopsServerConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 2),
    _CcopsServerConfigName_Type()
)
ccopsServerConfigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccopsServerConfigName.setStatus("current")


class _CcopsServerConfigPriority_Type(Unsigned32):
    """Custom type ccopsServerConfigPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CcopsServerConfigPriority_Type.__name__ = "Unsigned32"
_CcopsServerConfigPriority_Object = MibTableColumn
ccopsServerConfigPriority = _CcopsServerConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 3),
    _CcopsServerConfigPriority_Type()
)
ccopsServerConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccopsServerConfigPriority.setStatus("current")


class _CcopsServerConfigPort_Type(Unsigned32):
    """Custom type ccopsServerConfigPort based on Unsigned32"""
    defaultValue = 3288

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcopsServerConfigPort_Type.__name__ = "Unsigned32"
_CcopsServerConfigPort_Object = MibTableColumn
ccopsServerConfigPort = _CcopsServerConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 4),
    _CcopsServerConfigPort_Type()
)
ccopsServerConfigPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccopsServerConfigPort.setStatus("current")
_CcopsServerConfigStatus_Type = RowStatus
_CcopsServerConfigStatus_Object = MibTableColumn
ccopsServerConfigStatus = _CcopsServerConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 5),
    _CcopsServerConfigStatus_Type()
)
ccopsServerConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccopsServerConfigStatus.setStatus("current")


class _CcopsInitialTimeout_Type(Unsigned32):
    """Custom type ccopsInitialTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcopsInitialTimeout_Type.__name__ = "Unsigned32"
_CcopsInitialTimeout_Object = MibScalar
ccopsInitialTimeout = _CcopsInitialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 5),
    _CcopsInitialTimeout_Type()
)
ccopsInitialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccopsInitialTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ccopsInitialTimeout.setUnits("seconds")


class _CcopsTimeoutIncrement_Type(Unsigned32):
    """Custom type ccopsTimeoutIncrement based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcopsTimeoutIncrement_Type.__name__ = "Unsigned32"
_CcopsTimeoutIncrement_Object = MibScalar
ccopsTimeoutIncrement = _CcopsTimeoutIncrement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 6),
    _CcopsTimeoutIncrement_Type()
)
ccopsTimeoutIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccopsTimeoutIncrement.setStatus("current")
if mibBuilder.loadTexts:
    ccopsTimeoutIncrement.setUnits("seconds")


class _CcopsTimeoutMax_Type(Unsigned32):
    """Custom type ccopsTimeoutMax based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcopsTimeoutMax_Type.__name__ = "Unsigned32"
_CcopsTimeoutMax_Object = MibScalar
ccopsTimeoutMax = _CcopsTimeoutMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 7),
    _CcopsTimeoutMax_Type()
)
ccopsTimeoutMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccopsTimeoutMax.setStatus("current")
if mibBuilder.loadTexts:
    ccopsTimeoutMax.setUnits("seconds")
_CcopsDomainTable_Object = MibTable
ccopsDomainTable = _CcopsDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ccopsDomainTable.setStatus("current")
_CcopsDomainEntry_Object = MibTableRow
ccopsDomainEntry = _CcopsDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8, 1)
)
ccopsDomainEntry.setIndexNames(
    (0, "CISCO-COPS-CLIENT-MIB", "ccopsDomainClientType"),
)
if mibBuilder.loadTexts:
    ccopsDomainEntry.setStatus("current")
_CcopsDomainClientType_Type = CopsClientType
_CcopsDomainClientType_Object = MibTableColumn
ccopsDomainClientType = _CcopsDomainClientType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8, 1, 1),
    _CcopsDomainClientType_Type()
)
ccopsDomainClientType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccopsDomainClientType.setStatus("current")


class _CcopsDomainName_Type(CopsDomainName):
    """Custom type ccopsDomainName based on CopsDomainName"""
    defaultHexValue = ""


_CcopsDomainName_Object = MibTableColumn
ccopsDomainName = _CcopsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8, 1, 2),
    _CcopsDomainName_Type()
)
ccopsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccopsDomainName.setStatus("current")
_CcopsRoleTable_Object = MibTable
ccopsRoleTable = _CcopsRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9)
)
if mibBuilder.loadTexts:
    ccopsRoleTable.setStatus("current")
_CcopsRoleEntry_Object = MibTableRow
ccopsRoleEntry = _CcopsRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9, 1)
)
ccopsRoleEntry.setIndexNames(
    (1, "CISCO-COPS-CLIENT-MIB", "ccopsRoleName"),
)
if mibBuilder.loadTexts:
    ccopsRoleEntry.setStatus("current")
_CcopsRoleName_Type = CopsRole
_CcopsRoleName_Object = MibTableColumn
ccopsRoleName = _CcopsRoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9, 1, 1),
    _CcopsRoleName_Type()
)
ccopsRoleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccopsRoleName.setStatus("current")
_CcopsRoleStatus_Type = RowStatus
_CcopsRoleStatus_Object = MibTableColumn
ccopsRoleStatus = _CcopsRoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9, 1, 2),
    _CcopsRoleStatus_Type()
)
ccopsRoleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccopsRoleStatus.setStatus("current")
_CcopsIfTable_Object = MibTable
ccopsIfTable = _CcopsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 10)
)
if mibBuilder.loadTexts:
    ccopsIfTable.setStatus("current")
_CcopsIfEntry_Object = MibTableRow
ccopsIfEntry = _CcopsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 10, 1)
)
ccopsIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ccopsIfEntry.setStatus("current")
_CcopsIfRoleCombination_Type = CopsRoleCombination
_CcopsIfRoleCombination_Object = MibTableColumn
ccopsIfRoleCombination = _CcopsIfRoleCombination_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 10, 1, 1),
    _CcopsIfRoleCombination_Type()
)
ccopsIfRoleCombination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccopsIfRoleCombination.setStatus("current")
_CcopsRoleConfigSupported_Type = TruthValue
_CcopsRoleConfigSupported_Object = MibScalar
ccopsRoleConfigSupported = _CcopsRoleConfigSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 11),
    _CcopsRoleConfigSupported_Type()
)
ccopsRoleConfigSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccopsRoleConfigSupported.setStatus("current")
_CcopsMIBNotifications_ObjectIdentity = ObjectIdentity
ccopsMIBNotifications = _CcopsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 2)
)
_CcopsMIBConformance_ObjectIdentity = ObjectIdentity
ccopsMIBConformance = _CcopsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 3)
)
_CcopsMIBCompliances_ObjectIdentity = ObjectIdentity
ccopsMIBCompliances = _CcopsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 1)
)
_CcopsMIBGroups_ObjectIdentity = ObjectIdentity
ccopsMIBGroups = _CcopsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2)
)

# Managed Objects groups

ccopsGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2, 1)
)
ccopsGlobalGroup.setObjects(
      *(("CISCO-COPS-CLIENT-MIB", "ccopsServerMax"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPriority"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPort"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigStatus"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsInitialTimeout"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutIncrement"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutMax"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsDomainName"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsMaxRole"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsMaxRoleCombination"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsRoleStatus"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsIfRoleCombination"))
)
if mibBuilder.loadTexts:
    ccopsGlobalGroup.setStatus("deprecated")

ccopsGlobalGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2, 2)
)
ccopsGlobalGroupRev2.setObjects(
      *(("CISCO-COPS-CLIENT-MIB", "ccopsServerMax"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPriority"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPort"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigStatus"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsInitialTimeout"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutIncrement"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutMax"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsDomainName"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsMaxRoleCombination"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsIfRoleCombination"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsRoleConfigSupported"))
)
if mibBuilder.loadTexts:
    ccopsGlobalGroupRev2.setStatus("current")

ccopsRoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2, 3)
)
ccopsRoleGroup.setObjects(
      *(("CISCO-COPS-CLIENT-MIB", "ccopsMaxRole"),
        ("CISCO-COPS-CLIENT-MIB", "ccopsRoleStatus"))
)
if mibBuilder.loadTexts:
    ccopsRoleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ccopsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ccopsMIBCompliance.setStatus(
        "deprecated"
    )

ccopsMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ccopsMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-COPS-CLIENT-MIB",
    **{"CopsRole": CopsRole,
       "CopsRoleCombination": CopsRoleCombination,
       "CopsDomainName": CopsDomainName,
       "CopsClientType": CopsClientType,
       "ciscoCopsClientMIB": ciscoCopsClientMIB,
       "ccopsMIBObjects": ccopsMIBObjects,
       "ccopsGlobalObjects": ccopsGlobalObjects,
       "ccopsServerMax": ccopsServerMax,
       "ccopsMaxRole": ccopsMaxRole,
       "ccopsMaxRoleCombination": ccopsMaxRoleCombination,
       "ccopsServerConfigTable": ccopsServerConfigTable,
       "ccopsServerConfigEntry": ccopsServerConfigEntry,
       "ccopsServerConfigClientType": ccopsServerConfigClientType,
       "ccopsServerConfigName": ccopsServerConfigName,
       "ccopsServerConfigPriority": ccopsServerConfigPriority,
       "ccopsServerConfigPort": ccopsServerConfigPort,
       "ccopsServerConfigStatus": ccopsServerConfigStatus,
       "ccopsInitialTimeout": ccopsInitialTimeout,
       "ccopsTimeoutIncrement": ccopsTimeoutIncrement,
       "ccopsTimeoutMax": ccopsTimeoutMax,
       "ccopsDomainTable": ccopsDomainTable,
       "ccopsDomainEntry": ccopsDomainEntry,
       "ccopsDomainClientType": ccopsDomainClientType,
       "ccopsDomainName": ccopsDomainName,
       "ccopsRoleTable": ccopsRoleTable,
       "ccopsRoleEntry": ccopsRoleEntry,
       "ccopsRoleName": ccopsRoleName,
       "ccopsRoleStatus": ccopsRoleStatus,
       "ccopsIfTable": ccopsIfTable,
       "ccopsIfEntry": ccopsIfEntry,
       "ccopsIfRoleCombination": ccopsIfRoleCombination,
       "ccopsRoleConfigSupported": ccopsRoleConfigSupported,
       "ccopsMIBNotifications": ccopsMIBNotifications,
       "ccopsMIBConformance": ccopsMIBConformance,
       "ccopsMIBCompliances": ccopsMIBCompliances,
       "ccopsMIBCompliance": ccopsMIBCompliance,
       "ccopsMIBComplianceRev2": ccopsMIBComplianceRev2,
       "ccopsMIBGroups": ccopsMIBGroups,
       "ccopsGlobalGroup": ccopsGlobalGroup,
       "ccopsGlobalGroupRev2": ccopsGlobalGroupRev2,
       "ccopsRoleGroup": ccopsRoleGroup}
)
