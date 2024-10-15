# SNMP MIB module (CISCO-IPSEC-POLICY-MAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSEC-POLICY-MAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:52 2024
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


# MODULE-IDENTITY

ciscoIpSecPolMapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 172)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpSecPolMapMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpSecPolMapMIBObjects = _CiscoIpSecPolMapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1)
)
_IpSecPhaseOnePolMap_ObjectIdentity = ObjectIdentity
ipSecPhaseOnePolMap = _IpSecPhaseOnePolMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 1)
)
_IkePolMapTable_Object = MibTable
ikePolMapTable = _IkePolMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ikePolMapTable.setStatus("current")
_IkePolMapEntry_Object = MibTableRow
ikePolMapEntry = _IkePolMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 1, 1, 1)
)
ikePolMapEntry.setIndexNames(
    (0, "CISCO-IPSEC-POLICY-MAP-MIB", "ikePolMapTunIndex"),
)
if mibBuilder.loadTexts:
    ikePolMapEntry.setStatus("current")


class _IkePolMapTunIndex_Type(Integer32):
    """Custom type ikePolMapTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IkePolMapTunIndex_Type.__name__ = "Integer32"
_IkePolMapTunIndex_Object = MibTableColumn
ikePolMapTunIndex = _IkePolMapTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 1, 1, 1, 1),
    _IkePolMapTunIndex_Type()
)
ikePolMapTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ikePolMapTunIndex.setStatus("current")


class _IkePolMapPolicyNum_Type(Integer32):
    """Custom type ikePolMapPolicyNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IkePolMapPolicyNum_Type.__name__ = "Integer32"
_IkePolMapPolicyNum_Object = MibTableColumn
ikePolMapPolicyNum = _IkePolMapPolicyNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 1, 1, 1, 2),
    _IkePolMapPolicyNum_Type()
)
ikePolMapPolicyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ikePolMapPolicyNum.setStatus("current")
_IpSecPhaseTwoPolMap_ObjectIdentity = ObjectIdentity
ipSecPhaseTwoPolMap = _IpSecPhaseTwoPolMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2)
)
_IpSecPolMapTable_Object = MibTable
ipSecPolMapTable = _IpSecPolMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipSecPolMapTable.setStatus("current")
_IpSecPolMapEntry_Object = MibTableRow
ipSecPolMapEntry = _IpSecPolMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1, 1)
)
ipSecPolMapEntry.setIndexNames(
    (0, "CISCO-IPSEC-POLICY-MAP-MIB", "ipSecPolMapTunIndex"),
)
if mibBuilder.loadTexts:
    ipSecPolMapEntry.setStatus("current")


class _IpSecPolMapTunIndex_Type(Integer32):
    """Custom type ipSecPolMapTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpSecPolMapTunIndex_Type.__name__ = "Integer32"
_IpSecPolMapTunIndex_Object = MibTableColumn
ipSecPolMapTunIndex = _IpSecPolMapTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1, 1, 1),
    _IpSecPolMapTunIndex_Type()
)
ipSecPolMapTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSecPolMapTunIndex.setStatus("current")
_IpSecPolMapCryptoMapName_Type = DisplayString
_IpSecPolMapCryptoMapName_Object = MibTableColumn
ipSecPolMapCryptoMapName = _IpSecPolMapCryptoMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1, 1, 2),
    _IpSecPolMapCryptoMapName_Type()
)
ipSecPolMapCryptoMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecPolMapCryptoMapName.setStatus("current")


class _IpSecPolMapCryptoMapNum_Type(Integer32):
    """Custom type ipSecPolMapCryptoMapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpSecPolMapCryptoMapNum_Type.__name__ = "Integer32"
_IpSecPolMapCryptoMapNum_Object = MibTableColumn
ipSecPolMapCryptoMapNum = _IpSecPolMapCryptoMapNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1, 1, 3),
    _IpSecPolMapCryptoMapNum_Type()
)
ipSecPolMapCryptoMapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecPolMapCryptoMapNum.setStatus("current")
_IpSecPolMapAclString_Type = DisplayString
_IpSecPolMapAclString_Object = MibTableColumn
ipSecPolMapAclString = _IpSecPolMapAclString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1, 1, 4),
    _IpSecPolMapAclString_Type()
)
ipSecPolMapAclString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecPolMapAclString.setStatus("current")
_IpSecPolMapAceString_Type = DisplayString
_IpSecPolMapAceString_Object = MibTableColumn
ipSecPolMapAceString = _IpSecPolMapAceString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1, 1, 5),
    _IpSecPolMapAceString_Type()
)
ipSecPolMapAceString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSecPolMapAceString.setStatus("current")
_CiscoIpSecPolMapMIBNotifPrefix_ObjectIdentity = ObjectIdentity
ciscoIpSecPolMapMIBNotifPrefix = _CiscoIpSecPolMapMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 2)
)
_CiscoIpSecPolMapMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIpSecPolMapMIBConformance = _CiscoIpSecPolMapMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 3)
)
_IpSecPolMapMIBGroups_ObjectIdentity = ObjectIdentity
ipSecPolMapMIBGroups = _IpSecPolMapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 3, 1)
)
_IpSecPolMapMIBCompliances_ObjectIdentity = ObjectIdentity
ipSecPolMapMIBCompliances = _IpSecPolMapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 3, 2)
)

# Managed Objects groups

ipSecPhaseOnePolMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 3, 1, 1)
)
ipSecPhaseOnePolMapGroup.setObjects(
    ("CISCO-IPSEC-POLICY-MAP-MIB", "ikePolMapPolicyNum")
)
if mibBuilder.loadTexts:
    ipSecPhaseOnePolMapGroup.setStatus("current")

ipSecPhaseTwoPolMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 3, 1, 2)
)
ipSecPhaseTwoPolMapGroup.setObjects(
      *(("CISCO-IPSEC-POLICY-MAP-MIB", "ipSecPolMapCryptoMapName"),
        ("CISCO-IPSEC-POLICY-MAP-MIB", "ipSecPolMapCryptoMapNum"),
        ("CISCO-IPSEC-POLICY-MAP-MIB", "ipSecPolMapAclString"),
        ("CISCO-IPSEC-POLICY-MAP-MIB", "ipSecPolMapAceString"))
)
if mibBuilder.loadTexts:
    ipSecPhaseTwoPolMapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipSecPolMapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 172, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ipSecPolMapMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSEC-POLICY-MAP-MIB",
    **{"ciscoIpSecPolMapMIB": ciscoIpSecPolMapMIB,
       "ciscoIpSecPolMapMIBObjects": ciscoIpSecPolMapMIBObjects,
       "ipSecPhaseOnePolMap": ipSecPhaseOnePolMap,
       "ikePolMapTable": ikePolMapTable,
       "ikePolMapEntry": ikePolMapEntry,
       "ikePolMapTunIndex": ikePolMapTunIndex,
       "ikePolMapPolicyNum": ikePolMapPolicyNum,
       "ipSecPhaseTwoPolMap": ipSecPhaseTwoPolMap,
       "ipSecPolMapTable": ipSecPolMapTable,
       "ipSecPolMapEntry": ipSecPolMapEntry,
       "ipSecPolMapTunIndex": ipSecPolMapTunIndex,
       "ipSecPolMapCryptoMapName": ipSecPolMapCryptoMapName,
       "ipSecPolMapCryptoMapNum": ipSecPolMapCryptoMapNum,
       "ipSecPolMapAclString": ipSecPolMapAclString,
       "ipSecPolMapAceString": ipSecPolMapAceString,
       "ciscoIpSecPolMapMIBNotifPrefix": ciscoIpSecPolMapMIBNotifPrefix,
       "ciscoIpSecPolMapMIBConformance": ciscoIpSecPolMapMIBConformance,
       "ipSecPolMapMIBGroups": ipSecPolMapMIBGroups,
       "ipSecPhaseOnePolMapGroup": ipSecPhaseOnePolMapGroup,
       "ipSecPhaseTwoPolMapGroup": ipSecPhaseTwoPolMapGroup,
       "ipSecPolMapMIBCompliances": ipSecPolMapMIBCompliances,
       "ipSecPolMapMIBCompliance": ipSecPolMapMIBCompliance}
)
