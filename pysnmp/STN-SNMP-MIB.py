# SNMP MIB module (STN-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:17 2024
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

(stnSystems,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnSystems")


# MODULE-IDENTITY

stnSnmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnSnmp_ObjectIdentity = ObjectIdentity
stnSnmp = _StnSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1)
)
_StnSnmpVirtualRouterTable_Object = MibTable
stnSnmpVirtualRouterTable = _StnSnmpVirtualRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    stnSnmpVirtualRouterTable.setStatus("current")
_StnSnmpVirtualRouterEntry_Object = MibTableRow
stnSnmpVirtualRouterEntry = _StnSnmpVirtualRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1)
)
stnSnmpVirtualRouterEntry.setIndexNames(
    (0, "STN-SNMP-MIB", "stnSnmpRouterInstance"),
)
if mibBuilder.loadTexts:
    stnSnmpVirtualRouterEntry.setStatus("current")
_StnSnmpRouterInstance_Type = Integer32
_StnSnmpRouterInstance_Object = MibTableColumn
stnSnmpRouterInstance = _StnSnmpRouterInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1, 1),
    _StnSnmpRouterInstance_Type()
)
stnSnmpRouterInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSnmpRouterInstance.setStatus("current")


class _StnSnmpEnabled_Type(Integer32):
    """Custom type stnSnmpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StnSnmpEnabled_Type.__name__ = "Integer32"
_StnSnmpEnabled_Object = MibTableColumn
stnSnmpEnabled = _StnSnmpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1, 2),
    _StnSnmpEnabled_Type()
)
stnSnmpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSnmpEnabled.setStatus("current")
_StnSnmpReadCommunity_Type = DisplayString
_StnSnmpReadCommunity_Object = MibTableColumn
stnSnmpReadCommunity = _StnSnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1, 3),
    _StnSnmpReadCommunity_Type()
)
stnSnmpReadCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSnmpReadCommunity.setStatus("current")
_StnSnmpReadView_Type = DisplayString
_StnSnmpReadView_Object = MibTableColumn
stnSnmpReadView = _StnSnmpReadView_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1, 4),
    _StnSnmpReadView_Type()
)
stnSnmpReadView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSnmpReadView.setStatus("current")
_StnSnmpContextName_Type = DisplayString
_StnSnmpContextName_Object = MibTableColumn
stnSnmpContextName = _StnSnmpContextName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1, 5),
    _StnSnmpContextName_Type()
)
stnSnmpContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSnmpContextName.setStatus("current")
_StnSnmpWriteCommunity_Type = DisplayString
_StnSnmpWriteCommunity_Object = MibTableColumn
stnSnmpWriteCommunity = _StnSnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1, 6),
    _StnSnmpWriteCommunity_Type()
)
stnSnmpWriteCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSnmpWriteCommunity.setStatus("current")
_StnSnmpTrapHostTable_Object = MibTable
stnSnmpTrapHostTable = _StnSnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    stnSnmpTrapHostTable.setStatus("current")
_StnSnmpTrapHostEntry_Object = MibTableRow
stnSnmpTrapHostEntry = _StnSnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 2, 1)
)
stnSnmpTrapHostEntry.setIndexNames(
    (0, "STN-SNMP-MIB", "stnSnmpTrapHostIndex"),
)
if mibBuilder.loadTexts:
    stnSnmpTrapHostEntry.setStatus("current")
_StnSnmpTrapHostIndex_Type = Integer32
_StnSnmpTrapHostIndex_Object = MibTableColumn
stnSnmpTrapHostIndex = _StnSnmpTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 2, 1, 1),
    _StnSnmpTrapHostIndex_Type()
)
stnSnmpTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSnmpTrapHostIndex.setStatus("current")
_StnSnmpTrapHostIpAddress_Type = IpAddress
_StnSnmpTrapHostIpAddress_Object = MibTableColumn
stnSnmpTrapHostIpAddress = _StnSnmpTrapHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 2, 1, 2),
    _StnSnmpTrapHostIpAddress_Type()
)
stnSnmpTrapHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSnmpTrapHostIpAddress.setStatus("current")
_StnSnmpTrapHostPort_Type = Integer32
_StnSnmpTrapHostPort_Object = MibTableColumn
stnSnmpTrapHostPort = _StnSnmpTrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 2, 1, 3),
    _StnSnmpTrapHostPort_Type()
)
stnSnmpTrapHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSnmpTrapHostPort.setStatus("current")
_StnSnmpMibConformance_ObjectIdentity = ObjectIdentity
stnSnmpMibConformance = _StnSnmpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 2)
)
_StnSnmpMIBConformance_ObjectIdentity = ObjectIdentity
stnSnmpMIBConformance = _StnSnmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 3)
)
_StnSnmpMIBCompliances_ObjectIdentity = ObjectIdentity
stnSnmpMIBCompliances = _StnSnmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 3, 1)
)
_StnSnmpMIBGroups_ObjectIdentity = ObjectIdentity
stnSnmpMIBGroups = _StnSnmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 3, 2)
)

# Managed Objects groups

stnSnmpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 3, 2, 1)
)
stnSnmpMIBGroup.setObjects(
      *(("STN-SNMP-MIB", "stnSnmpRouterInstance"),
        ("STN-SNMP-MIB", "stnSnmpEnabled"),
        ("STN-SNMP-MIB", "stnSnmpReadCommunity"),
        ("STN-SNMP-MIB", "stnSnmpReadView"),
        ("STN-SNMP-MIB", "stnSnmpContextName"))
)
if mibBuilder.loadTexts:
    stnSnmpMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

stnSnmpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3551, 2, 14, 3, 1, 1)
)
if mibBuilder.loadTexts:
    stnSnmpMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-SNMP-MIB",
    **{"stnSnmpMIB": stnSnmpMIB,
       "stnSnmp": stnSnmp,
       "stnSnmpVirtualRouterTable": stnSnmpVirtualRouterTable,
       "stnSnmpVirtualRouterEntry": stnSnmpVirtualRouterEntry,
       "stnSnmpRouterInstance": stnSnmpRouterInstance,
       "stnSnmpEnabled": stnSnmpEnabled,
       "stnSnmpReadCommunity": stnSnmpReadCommunity,
       "stnSnmpReadView": stnSnmpReadView,
       "stnSnmpContextName": stnSnmpContextName,
       "stnSnmpWriteCommunity": stnSnmpWriteCommunity,
       "stnSnmpTrapHostTable": stnSnmpTrapHostTable,
       "stnSnmpTrapHostEntry": stnSnmpTrapHostEntry,
       "stnSnmpTrapHostIndex": stnSnmpTrapHostIndex,
       "stnSnmpTrapHostIpAddress": stnSnmpTrapHostIpAddress,
       "stnSnmpTrapHostPort": stnSnmpTrapHostPort,
       "stnSnmpMibConformance": stnSnmpMibConformance,
       "stnSnmpMIBConformance": stnSnmpMIBConformance,
       "stnSnmpMIBCompliances": stnSnmpMIBCompliances,
       "stnSnmpMIBComplianceRev1": stnSnmpMIBComplianceRev1,
       "stnSnmpMIBGroups": stnSnmpMIBGroups,
       "stnSnmpMIBGroup": stnSnmpMIBGroup}
)
