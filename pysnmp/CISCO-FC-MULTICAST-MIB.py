# SNMP MIB module (CISCO-FC-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FC-MULTICAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:15 2024
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

(DomainIdOrZero,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "DomainIdOrZero")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

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

ciscoFcMulticastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 435)
)
ciscoFcMulticastMIB.setRevisions(
        ("2004-10-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CfmMulticastRootMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowestDomainSwitch", 2),
          ("principalSwitch", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFcMulticastNotifications_ObjectIdentity = ObjectIdentity
ciscoFcMulticastNotifications = _CiscoFcMulticastNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 0)
)
_CiscoFcMulticastMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFcMulticastMIBObjects = _CiscoFcMulticastMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 1)
)
_CfmConfiguration_ObjectIdentity = ObjectIdentity
cfmConfiguration = _CfmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1)
)
_CfmMulticastRootTable_Object = MibTable
cfmMulticastRootTable = _CfmMulticastRootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfmMulticastRootTable.setStatus("current")
_CfmMulticastRootEntry_Object = MibTableRow
cfmMulticastRootEntry = _CfmMulticastRootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1)
)
cfmMulticastRootEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    cfmMulticastRootEntry.setStatus("current")


class _CfmMulticastRootConfigMode_Type(CfmMulticastRootMode):
    """Custom type cfmMulticastRootConfigMode based on CfmMulticastRootMode"""


_CfmMulticastRootConfigMode_Object = MibTableColumn
cfmMulticastRootConfigMode = _CfmMulticastRootConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 1),
    _CfmMulticastRootConfigMode_Type()
)
cfmMulticastRootConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMulticastRootConfigMode.setStatus("current")
_CfmMulticastRootOperMode_Type = CfmMulticastRootMode
_CfmMulticastRootOperMode_Object = MibTableColumn
cfmMulticastRootOperMode = _CfmMulticastRootOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 2),
    _CfmMulticastRootOperMode_Type()
)
cfmMulticastRootOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMulticastRootOperMode.setStatus("current")
_CfmMulticastRootDomainId_Type = DomainIdOrZero
_CfmMulticastRootDomainId_Object = MibTableColumn
cfmMulticastRootDomainId = _CfmMulticastRootDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 3),
    _CfmMulticastRootDomainId_Type()
)
cfmMulticastRootDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMulticastRootDomainId.setStatus("current")
_CfmMulticastRootRowStatus_Type = RowStatus
_CfmMulticastRootRowStatus_Object = MibTableColumn
cfmMulticastRootRowStatus = _CfmMulticastRootRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 4),
    _CfmMulticastRootRowStatus_Type()
)
cfmMulticastRootRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMulticastRootRowStatus.setStatus("current")
_CiscoFcMulticaseConformance_ObjectIdentity = ObjectIdentity
ciscoFcMulticaseConformance = _CiscoFcMulticaseConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 2)
)
_CiscoFcMulticastMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFcMulticastMIBCompliances = _CiscoFcMulticastMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 1)
)
_CiscoFcMulticastMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFcMulticastMIBGroups = _CiscoFcMulticastMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 2)
)

# Managed Objects groups

cfmConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 2, 1)
)
cfmConfigurationGroup.setObjects(
      *(("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootConfigMode"),
        ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootOperMode"),
        ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootDomainId"),
        ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootRowStatus"))
)
if mibBuilder.loadTexts:
    cfmConfigurationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoFcMulticastMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFcMulticastMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FC-MULTICAST-MIB",
    **{"CfmMulticastRootMode": CfmMulticastRootMode,
       "ciscoFcMulticastMIB": ciscoFcMulticastMIB,
       "ciscoFcMulticastNotifications": ciscoFcMulticastNotifications,
       "ciscoFcMulticastMIBObjects": ciscoFcMulticastMIBObjects,
       "cfmConfiguration": cfmConfiguration,
       "cfmMulticastRootTable": cfmMulticastRootTable,
       "cfmMulticastRootEntry": cfmMulticastRootEntry,
       "cfmMulticastRootConfigMode": cfmMulticastRootConfigMode,
       "cfmMulticastRootOperMode": cfmMulticastRootOperMode,
       "cfmMulticastRootDomainId": cfmMulticastRootDomainId,
       "cfmMulticastRootRowStatus": cfmMulticastRootRowStatus,
       "ciscoFcMulticaseConformance": ciscoFcMulticaseConformance,
       "ciscoFcMulticastMIBCompliances": ciscoFcMulticastMIBCompliances,
       "ciscoFcMulticastMIBCompliance": ciscoFcMulticastMIBCompliance,
       "ciscoFcMulticastMIBGroups": ciscoFcMulticastMIBGroups,
       "cfmConfigurationGroup": cfmConfigurationGroup}
)
