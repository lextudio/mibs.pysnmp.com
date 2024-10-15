# SNMP MIB module (HPVCMODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPVCMODULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:35 2024
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

(ifInErrors,
 ifIndex,
 ifOutErrors) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifInErrors",
    "ifIndex",
    "ifOutErrors")

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
 enterprises,
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mib-2",
    "zeroDotZero")

(DisplayString,
 RowPointer,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TruthValue")

(TransportAddress,
 TransportAddressType) = mibBuilder.importSymbols(
    "TRANSPORT-ADDRESS-MIB",
    "TransportAddress",
    "TransportAddressType")


# MODULE-IDENTITY

vcModuleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3)
)
vcModuleMIB.setRevisions(
        ("2008-10-08 00:00",
         "2009-02-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VcModuleRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 5),
          ("primaryProtected", 2),
          ("primaryUnprotected", 3),
          ("standby", 4),
          ("unintegrated", 1))
    )



class VcEnclosureRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 2),
          ("secondary", 3),
          ("unknown", 1))
    )



class VcModuleType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vcModuleEnet", 1),
          ("vcModuleFC", 2),
          ("vcModuleOther", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_HpSysMgt_ObjectIdentity = ObjectIdentity
hpSysMgt = _HpSysMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5)
)
_HpEmbeddedServerMgt_ObjectIdentity = ObjectIdentity
hpEmbeddedServerMgt = _HpEmbeddedServerMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7)
)
_HpModuleMgmtProc_ObjectIdentity = ObjectIdentity
hpModuleMgmtProc = _HpModuleMgmtProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5)
)
_VirtualConnect_ObjectIdentity = ObjectIdentity
virtualConnect = _VirtualConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2)
)
_VcModuleMIBObjects_ObjectIdentity = ObjectIdentity
vcModuleMIBObjects = _VcModuleMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1)
)
_VcModuleObjects_ObjectIdentity = ObjectIdentity
vcModuleObjects = _VcModuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1)
)
_VcModuleDomainName_Type = SnmpAdminString
_VcModuleDomainName_Object = MibScalar
vcModuleDomainName = _VcModuleDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 1),
    _VcModuleDomainName_Type()
)
vcModuleDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleDomainName.setStatus("current")
_VcModuleRole_Type = VcModuleRole
_VcModuleRole_Object = MibScalar
vcModuleRole = _VcModuleRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 2),
    _VcModuleRole_Type()
)
vcModuleRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleRole.setStatus("current")
_VcModuleDomainPrimaryAddressType_Type = TransportAddressType
_VcModuleDomainPrimaryAddressType_Object = MibScalar
vcModuleDomainPrimaryAddressType = _VcModuleDomainPrimaryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 3),
    _VcModuleDomainPrimaryAddressType_Type()
)
vcModuleDomainPrimaryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleDomainPrimaryAddressType.setStatus("current")
_VcModuleDomainPrimaryAddress_Type = TransportAddress
_VcModuleDomainPrimaryAddress_Object = MibScalar
vcModuleDomainPrimaryAddress = _VcModuleDomainPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 4),
    _VcModuleDomainPrimaryAddress_Type()
)
vcModuleDomainPrimaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleDomainPrimaryAddress.setStatus("current")
_VcModuleEnclosureRole_Type = VcEnclosureRole
_VcModuleEnclosureRole_Object = MibScalar
vcModuleEnclosureRole = _VcModuleEnclosureRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 5),
    _VcModuleEnclosureRole_Type()
)
vcModuleEnclosureRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcModuleEnclosureRole.setStatus("current")
_VcModuleMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
vcModuleMIBNotificationPrefix = _VcModuleMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2)
)
_VcModuleMIBNotifications_ObjectIdentity = ObjectIdentity
vcModuleMIBNotifications = _VcModuleMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0)
)
_VcModuleMIBNotificationObjects_ObjectIdentity = ObjectIdentity
vcModuleMIBNotificationObjects = _VcModuleMIBNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 1)
)
_VcModuleMIBConformance_ObjectIdentity = ObjectIdentity
vcModuleMIBConformance = _VcModuleMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3)
)
_VcModuleMIBCompliances_ObjectIdentity = ObjectIdentity
vcModuleMIBCompliances = _VcModuleMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 1)
)
_VcModuleMIBGroups_ObjectIdentity = ObjectIdentity
vcModuleMIBGroups = _VcModuleMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2)
)

# Managed Objects groups

vcModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 1)
)
vcModuleGroup.setObjects(
      *(("HPVCMODULE-MIB", "vcModuleDomainName"),
        ("HPVCMODULE-MIB", "vcModuleRole"),
        ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddressType"),
        ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddress"))
)
if mibBuilder.loadTexts:
    vcModuleGroup.setStatus("current")


# Notification objects

vcModuleDomainRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 1)
)
vcModuleDomainRoleChange.setObjects(
    ("HPVCMODULE-MIB", "vcModuleRole")
)
if mibBuilder.loadTexts:
    vcModuleDomainRoleChange.setStatus(
        "current"
    )

vcModPortInputUtilizationUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 11)
)
vcModPortInputUtilizationUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    vcModPortInputUtilizationUp.setStatus(
        "current"
    )

vcModPortInputUtilizationDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 12)
)
vcModPortInputUtilizationDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    vcModPortInputUtilizationDown.setStatus(
        "current"
    )

vcModPortOutputUtilizationUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 13)
)
vcModPortOutputUtilizationUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    vcModPortOutputUtilizationUp.setStatus(
        "current"
    )

vcModPortOutputUtilizationDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 14)
)
vcModPortOutputUtilizationDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    vcModPortOutputUtilizationDown.setStatus(
        "current"
    )

vcModPortInputErrorsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 15)
)
vcModPortInputErrorsUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifInErrors"))
)
if mibBuilder.loadTexts:
    vcModPortInputErrorsUp.setStatus(
        "current"
    )

vcModPortInputErrorsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 16)
)
vcModPortInputErrorsDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifInErrors"))
)
if mibBuilder.loadTexts:
    vcModPortInputErrorsDown.setStatus(
        "current"
    )

vcModPortOutputErrorsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 17)
)
vcModPortOutputErrorsUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifOutErrors"))
)
if mibBuilder.loadTexts:
    vcModPortOutputErrorsUp.setStatus(
        "current"
    )

vcModPortOutputErrorsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 18)
)
vcModPortOutputErrorsDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifOutErrors"))
)
if mibBuilder.loadTexts:
    vcModPortOutputErrorsDown.setStatus(
        "current"
    )


# Notifications groups

vcModPortThresholdNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 2)
)
vcModPortThresholdNotificationsGroup.setObjects(
      *(("HPVCMODULE-MIB", "vcModPortInputUtilizationUp"),
        ("HPVCMODULE-MIB", "vcModPortInputUtilizationDown"),
        ("HPVCMODULE-MIB", "vcModPortOutputUtilizationUp"),
        ("HPVCMODULE-MIB", "vcModPortOutputUtilizationDown"),
        ("HPVCMODULE-MIB", "vcModPortInputErrorsUp"),
        ("HPVCMODULE-MIB", "vcModPortInputErrorsDown"),
        ("HPVCMODULE-MIB", "vcModPortOutputErrorsUp"),
        ("HPVCMODULE-MIB", "vcModPortOutputErrorsDown"))
)
if mibBuilder.loadTexts:
    vcModPortThresholdNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vcModuleMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vcModuleMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPVCMODULE-MIB",
    **{"VcModuleRole": VcModuleRole,
       "VcEnclosureRole": VcEnclosureRole,
       "VcModuleType": VcModuleType,
       "hp": hp,
       "hpSysMgt": hpSysMgt,
       "hpEmbeddedServerMgt": hpEmbeddedServerMgt,
       "hpModuleMgmtProc": hpModuleMgmtProc,
       "virtualConnect": virtualConnect,
       "vcModuleMIB": vcModuleMIB,
       "vcModuleMIBObjects": vcModuleMIBObjects,
       "vcModuleObjects": vcModuleObjects,
       "vcModuleDomainName": vcModuleDomainName,
       "vcModuleRole": vcModuleRole,
       "vcModuleDomainPrimaryAddressType": vcModuleDomainPrimaryAddressType,
       "vcModuleDomainPrimaryAddress": vcModuleDomainPrimaryAddress,
       "vcModuleEnclosureRole": vcModuleEnclosureRole,
       "vcModuleMIBNotificationPrefix": vcModuleMIBNotificationPrefix,
       "vcModuleMIBNotifications": vcModuleMIBNotifications,
       "vcModuleDomainRoleChange": vcModuleDomainRoleChange,
       "vcModPortInputUtilizationUp": vcModPortInputUtilizationUp,
       "vcModPortInputUtilizationDown": vcModPortInputUtilizationDown,
       "vcModPortOutputUtilizationUp": vcModPortOutputUtilizationUp,
       "vcModPortOutputUtilizationDown": vcModPortOutputUtilizationDown,
       "vcModPortInputErrorsUp": vcModPortInputErrorsUp,
       "vcModPortInputErrorsDown": vcModPortInputErrorsDown,
       "vcModPortOutputErrorsUp": vcModPortOutputErrorsUp,
       "vcModPortOutputErrorsDown": vcModPortOutputErrorsDown,
       "vcModuleMIBNotificationObjects": vcModuleMIBNotificationObjects,
       "vcModuleMIBConformance": vcModuleMIBConformance,
       "vcModuleMIBCompliances": vcModuleMIBCompliances,
       "vcModuleMIBCompliance": vcModuleMIBCompliance,
       "vcModuleMIBGroups": vcModuleMIBGroups,
       "vcModuleGroup": vcModuleGroup,
       "vcModPortThresholdNotificationsGroup": vcModPortThresholdNotificationsGroup}
)
