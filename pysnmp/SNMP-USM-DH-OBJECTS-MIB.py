# SNMP MIB module (SNMP-USM-DH-OBJECTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP-USM-DH-OBJECTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:09 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(usmUserEntry,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "usmUserEntry")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

snmpUsmDHObjectsMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 101)
)
snmpUsmDHObjectsMIB.setRevisions(
        ("2000-03-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DHKeyChange(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_UsmDHKeyObjects_ObjectIdentity = ObjectIdentity
usmDHKeyObjects = _UsmDHKeyObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 101, 1)
)
_UsmDHPublicObjects_ObjectIdentity = ObjectIdentity
usmDHPublicObjects = _UsmDHPublicObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 101, 1, 1)
)
_UsmDHParameters_Type = OctetString
_UsmDHParameters_Object = MibScalar
usmDHParameters = _UsmDHParameters_Object(
    (1, 3, 6, 1, 3, 101, 1, 1, 1),
    _UsmDHParameters_Type()
)
usmDHParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmDHParameters.setStatus("current")
_UsmDHUserKeyTable_Object = MibTable
usmDHUserKeyTable = _UsmDHUserKeyTable_Object(
    (1, 3, 6, 1, 3, 101, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usmDHUserKeyTable.setStatus("current")
_UsmDHUserKeyEntry_Object = MibTableRow
usmDHUserKeyEntry = _UsmDHUserKeyEntry_Object(
    (1, 3, 6, 1, 3, 101, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usmDHUserKeyEntry.setStatus("current")
_UsmDHUserAuthKeyChange_Type = DHKeyChange
_UsmDHUserAuthKeyChange_Object = MibTableColumn
usmDHUserAuthKeyChange = _UsmDHUserAuthKeyChange_Object(
    (1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 1),
    _UsmDHUserAuthKeyChange_Type()
)
usmDHUserAuthKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmDHUserAuthKeyChange.setStatus("current")
_UsmDHUserOwnAuthKeyChange_Type = DHKeyChange
_UsmDHUserOwnAuthKeyChange_Object = MibTableColumn
usmDHUserOwnAuthKeyChange = _UsmDHUserOwnAuthKeyChange_Object(
    (1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 2),
    _UsmDHUserOwnAuthKeyChange_Type()
)
usmDHUserOwnAuthKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmDHUserOwnAuthKeyChange.setStatus("current")
_UsmDHUserPrivKeyChange_Type = DHKeyChange
_UsmDHUserPrivKeyChange_Object = MibTableColumn
usmDHUserPrivKeyChange = _UsmDHUserPrivKeyChange_Object(
    (1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 3),
    _UsmDHUserPrivKeyChange_Type()
)
usmDHUserPrivKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmDHUserPrivKeyChange.setStatus("current")
_UsmDHUserOwnPrivKeyChange_Type = DHKeyChange
_UsmDHUserOwnPrivKeyChange_Object = MibTableColumn
usmDHUserOwnPrivKeyChange = _UsmDHUserOwnPrivKeyChange_Object(
    (1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 4),
    _UsmDHUserOwnPrivKeyChange_Type()
)
usmDHUserOwnPrivKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmDHUserOwnPrivKeyChange.setStatus("current")
_UsmDHKickstartGroup_ObjectIdentity = ObjectIdentity
usmDHKickstartGroup = _UsmDHKickstartGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 101, 1, 2)
)
_UsmDHKickstartTable_Object = MibTable
usmDHKickstartTable = _UsmDHKickstartTable_Object(
    (1, 3, 6, 1, 3, 101, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usmDHKickstartTable.setStatus("current")
_UsmDHKickstartEntry_Object = MibTableRow
usmDHKickstartEntry = _UsmDHKickstartEntry_Object(
    (1, 3, 6, 1, 3, 101, 1, 2, 1, 1)
)
usmDHKickstartEntry.setIndexNames(
    (0, "SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartIndex"),
)
if mibBuilder.loadTexts:
    usmDHKickstartEntry.setStatus("current")


class _UsmDHKickstartIndex_Type(Integer32):
    """Custom type usmDHKickstartIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsmDHKickstartIndex_Type.__name__ = "Integer32"
_UsmDHKickstartIndex_Object = MibTableColumn
usmDHKickstartIndex = _UsmDHKickstartIndex_Object(
    (1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 1),
    _UsmDHKickstartIndex_Type()
)
usmDHKickstartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usmDHKickstartIndex.setStatus("current")
_UsmDHKickstartMyPublic_Type = OctetString
_UsmDHKickstartMyPublic_Object = MibTableColumn
usmDHKickstartMyPublic = _UsmDHKickstartMyPublic_Object(
    (1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 2),
    _UsmDHKickstartMyPublic_Type()
)
usmDHKickstartMyPublic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmDHKickstartMyPublic.setStatus("current")
_UsmDHKickstartMgrPublic_Type = OctetString
_UsmDHKickstartMgrPublic_Object = MibTableColumn
usmDHKickstartMgrPublic = _UsmDHKickstartMgrPublic_Object(
    (1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 3),
    _UsmDHKickstartMgrPublic_Type()
)
usmDHKickstartMgrPublic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmDHKickstartMgrPublic.setStatus("current")
_UsmDHKickstartSecurityName_Type = SnmpAdminString
_UsmDHKickstartSecurityName_Object = MibTableColumn
usmDHKickstartSecurityName = _UsmDHKickstartSecurityName_Object(
    (1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 4),
    _UsmDHKickstartSecurityName_Type()
)
usmDHKickstartSecurityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmDHKickstartSecurityName.setStatus("current")
_UsmDHKeyConformance_ObjectIdentity = ObjectIdentity
usmDHKeyConformance = _UsmDHKeyConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 101, 2)
)
_UsmDHKeyMIBCompliances_ObjectIdentity = ObjectIdentity
usmDHKeyMIBCompliances = _UsmDHKeyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 101, 2, 1)
)
_UsmDHKeyMIBGroups_ObjectIdentity = ObjectIdentity
usmDHKeyMIBGroups = _UsmDHKeyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 101, 2, 2)
)
usmUserEntry.registerAugmentions(
    ("SNMP-USM-DH-OBJECTS-MIB",
     "usmDHUserKeyEntry")
)
usmDHUserKeyEntry.setIndexNames(*usmUserEntry.getIndexNames())

# Managed Objects groups

usmDHKeyMIBBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 101, 2, 2, 1)
)
usmDHKeyMIBBasicGroup.setObjects(
      *(("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserAuthKeyChange"),
        ("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserOwnAuthKeyChange"),
        ("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserPrivKeyChange"),
        ("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserOwnPrivKeyChange"))
)
if mibBuilder.loadTexts:
    usmDHKeyMIBBasicGroup.setStatus("current")

usmDHKeyParamGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 101, 2, 2, 2)
)
usmDHKeyParamGroup.setObjects(
    ("SNMP-USM-DH-OBJECTS-MIB", "usmDHParameters")
)
if mibBuilder.loadTexts:
    usmDHKeyParamGroup.setStatus("current")

usmDHKeyKickstartGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 101, 2, 2, 3)
)
usmDHKeyKickstartGroup.setObjects(
      *(("SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartMyPublic"),
        ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartMgrPublic"),
        ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartSecurityName"))
)
if mibBuilder.loadTexts:
    usmDHKeyKickstartGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usmDHKeyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 101, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usmDHKeyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-USM-DH-OBJECTS-MIB",
    **{"DHKeyChange": DHKeyChange,
       "snmpUsmDHObjectsMIB": snmpUsmDHObjectsMIB,
       "usmDHKeyObjects": usmDHKeyObjects,
       "usmDHPublicObjects": usmDHPublicObjects,
       "usmDHParameters": usmDHParameters,
       "usmDHUserKeyTable": usmDHUserKeyTable,
       "usmDHUserKeyEntry": usmDHUserKeyEntry,
       "usmDHUserAuthKeyChange": usmDHUserAuthKeyChange,
       "usmDHUserOwnAuthKeyChange": usmDHUserOwnAuthKeyChange,
       "usmDHUserPrivKeyChange": usmDHUserPrivKeyChange,
       "usmDHUserOwnPrivKeyChange": usmDHUserOwnPrivKeyChange,
       "usmDHKickstartGroup": usmDHKickstartGroup,
       "usmDHKickstartTable": usmDHKickstartTable,
       "usmDHKickstartEntry": usmDHKickstartEntry,
       "usmDHKickstartIndex": usmDHKickstartIndex,
       "usmDHKickstartMyPublic": usmDHKickstartMyPublic,
       "usmDHKickstartMgrPublic": usmDHKickstartMgrPublic,
       "usmDHKickstartSecurityName": usmDHKickstartSecurityName,
       "usmDHKeyConformance": usmDHKeyConformance,
       "usmDHKeyMIBCompliances": usmDHKeyMIBCompliances,
       "usmDHKeyMIBCompliance": usmDHKeyMIBCompliance,
       "usmDHKeyMIBGroups": usmDHKeyMIBGroups,
       "usmDHKeyMIBBasicGroup": usmDHKeyMIBBasicGroup,
       "usmDHKeyParamGroup": usmDHKeyParamGroup,
       "usmDHKeyKickstartGroup": usmDHKeyKickstartGroup}
)
