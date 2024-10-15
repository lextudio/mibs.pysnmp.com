# SNMP MIB module (CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:48 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

ciscoDot11CsMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228)
)
ciscoDot11CsMgrMIB.setRevisions(
        ("2003-11-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Cdot11CsModuleIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDot11CsMgrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDot11CsMgrMIBObjects = _CiscoDot11CsMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 1)
)
_CiscoDot11CsMgrClientConfig_ObjectIdentity = ObjectIdentity
ciscoDot11CsMgrClientConfig = _CiscoDot11CsMgrClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1)
)
_CDot11CsMgrClientTable_Object = MibTable
cDot11CsMgrClientTable = _CDot11CsMgrClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cDot11CsMgrClientTable.setStatus("current")
_CDot11CsMgrClientEntry_Object = MibTableRow
cDot11CsMgrClientEntry = _CDot11CsMgrClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1)
)
cDot11CsMgrClientEntry.setIndexNames(
    (0, "CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntModuleIndex"),
)
if mibBuilder.loadTexts:
    cDot11CsMgrClientEntry.setStatus("current")
_CDot11CsMgrClntModuleIndex_Type = Cdot11CsModuleIndex
_CDot11CsMgrClntModuleIndex_Object = MibTableColumn
cDot11CsMgrClntModuleIndex = _CDot11CsMgrClntModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 1),
    _CDot11CsMgrClntModuleIndex_Type()
)
cDot11CsMgrClntModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11CsMgrClntModuleIndex.setStatus("current")
_CDot11CsMgrClntAddressType_Type = InetAddressType
_CDot11CsMgrClntAddressType_Object = MibTableColumn
cDot11CsMgrClntAddressType = _CDot11CsMgrClntAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 2),
    _CDot11CsMgrClntAddressType_Type()
)
cDot11CsMgrClntAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CsMgrClntAddressType.setStatus("current")
_CDot11CsMgrClntParentWdsAddr_Type = InetAddress
_CDot11CsMgrClntParentWdsAddr_Object = MibTableColumn
cDot11CsMgrClntParentWdsAddr = _CDot11CsMgrClntParentWdsAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 3),
    _CDot11CsMgrClntParentWdsAddr_Type()
)
cDot11CsMgrClntParentWdsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CsMgrClntParentWdsAddr.setStatus("current")
_CDot11CsMgrClntRootNodeAddr_Type = InetAddress
_CDot11CsMgrClntRootNodeAddr_Object = MibTableColumn
cDot11CsMgrClntRootNodeAddr = _CDot11CsMgrClntRootNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 4),
    _CDot11CsMgrClntRootNodeAddr_Type()
)
cDot11CsMgrClntRootNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CsMgrClntRootNodeAddr.setStatus("current")
_CDot11CsMgrClntMnAuthenAddr_Type = InetAddress
_CDot11CsMgrClntMnAuthenAddr_Object = MibTableColumn
cDot11CsMgrClntMnAuthenAddr = _CDot11CsMgrClntMnAuthenAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 5),
    _CDot11CsMgrClntMnAuthenAddr_Type()
)
cDot11CsMgrClntMnAuthenAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CsMgrClntMnAuthenAddr.setStatus("current")


class _CDot11CsMgrClntOperMode_Type(Integer32):
    """Custom type cDot11CsMgrClntOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("distributed", 2),
          ("infrastructure", 1))
    )


_CDot11CsMgrClntOperMode_Type.__name__ = "Integer32"
_CDot11CsMgrClntOperMode_Object = MibTableColumn
cDot11CsMgrClntOperMode = _CDot11CsMgrClntOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 6),
    _CDot11CsMgrClntOperMode_Type()
)
cDot11CsMgrClntOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CsMgrClntOperMode.setStatus("current")
_CDot11CsMgrClntRegistLifeTime_Type = TimeInterval
_CDot11CsMgrClntRegistLifeTime_Object = MibTableColumn
cDot11CsMgrClntRegistLifeTime = _CDot11CsMgrClntRegistLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 7),
    _CDot11CsMgrClntRegistLifeTime_Type()
)
cDot11CsMgrClntRegistLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CsMgrClntRegistLifeTime.setStatus("current")
_CDot11CsMgrClntStateTransitions_Type = Counter32
_CDot11CsMgrClntStateTransitions_Object = MibTableColumn
cDot11CsMgrClntStateTransitions = _CDot11CsMgrClntStateTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 8),
    _CDot11CsMgrClntStateTransitions_Type()
)
cDot11CsMgrClntStateTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CsMgrClntStateTransitions.setStatus("current")
_CiscoDot11CsMgrMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDot11CsMgrMIBConformance = _CiscoDot11CsMgrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 2)
)
_CiscoDot11CsMgrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDot11CsMgrMIBCompliances = _CiscoDot11CsMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 2, 1)
)
_CiscoDot11CsMgrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDot11CsMgrMIBGroups = _CiscoDot11CsMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 2, 2)
)

# Managed Objects groups

ciscoDot11CsMgrClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 2, 2, 1)
)
ciscoDot11CsMgrClientGroup.setObjects(
      *(("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntAddressType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntParentWdsAddr"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntRootNodeAddr"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntMnAuthenAddr"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntOperMode"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntRegistLifeTime"),
        ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntStateTransitions"))
)
if mibBuilder.loadTexts:
    ciscoDot11CsMgrClientGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDot11CsMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 3228, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDot11CsMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB",
    **{"Cdot11CsModuleIndex": Cdot11CsModuleIndex,
       "ciscoDot11CsMgrMIB": ciscoDot11CsMgrMIB,
       "ciscoDot11CsMgrMIBObjects": ciscoDot11CsMgrMIBObjects,
       "ciscoDot11CsMgrClientConfig": ciscoDot11CsMgrClientConfig,
       "cDot11CsMgrClientTable": cDot11CsMgrClientTable,
       "cDot11CsMgrClientEntry": cDot11CsMgrClientEntry,
       "cDot11CsMgrClntModuleIndex": cDot11CsMgrClntModuleIndex,
       "cDot11CsMgrClntAddressType": cDot11CsMgrClntAddressType,
       "cDot11CsMgrClntParentWdsAddr": cDot11CsMgrClntParentWdsAddr,
       "cDot11CsMgrClntRootNodeAddr": cDot11CsMgrClntRootNodeAddr,
       "cDot11CsMgrClntMnAuthenAddr": cDot11CsMgrClntMnAuthenAddr,
       "cDot11CsMgrClntOperMode": cDot11CsMgrClntOperMode,
       "cDot11CsMgrClntRegistLifeTime": cDot11CsMgrClntRegistLifeTime,
       "cDot11CsMgrClntStateTransitions": cDot11CsMgrClntStateTransitions,
       "ciscoDot11CsMgrMIBConformance": ciscoDot11CsMgrMIBConformance,
       "ciscoDot11CsMgrMIBCompliances": ciscoDot11CsMgrMIBCompliances,
       "ciscoDot11CsMgrMIBCompliance": ciscoDot11CsMgrMIBCompliance,
       "ciscoDot11CsMgrMIBGroups": ciscoDot11CsMgrMIBGroups,
       "ciscoDot11CsMgrClientGroup": ciscoDot11CsMgrClientGroup}
)
