# SNMP MIB module (ALVARION-VSC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-VSC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:49 2024
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

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

(AlvarionSSID,) = mibBuilder.importSymbols(
    "ALVARION-TC",
    "AlvarionSSID")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alvarionVscMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionVscMIBObjects_ObjectIdentity = ObjectIdentity
alvarionVscMIBObjects = _AlvarionVscMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1)
)
_CoVscConfigGroup_ObjectIdentity = ObjectIdentity
coVscConfigGroup = _CoVscConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1)
)
_CoVscConfigTable_Object = MibTable
coVscConfigTable = _CoVscConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coVscConfigTable.setStatus("current")
_CoVscConfigEntry_Object = MibTableRow
coVscConfigEntry = _CoVscConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1)
)
coVscConfigEntry.setIndexNames(
    (0, "ALVARION-VSC-MIB", "coVscCfgIndex"),
)
if mibBuilder.loadTexts:
    coVscConfigEntry.setStatus("current")


class _CoVscCfgIndex_Type(Integer32):
    """Custom type coVscCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoVscCfgIndex_Type.__name__ = "Integer32"
_CoVscCfgIndex_Object = MibTableColumn
coVscCfgIndex = _CoVscCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 1),
    _CoVscCfgIndex_Type()
)
coVscCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coVscCfgIndex.setStatus("current")
_CoVscCfgFriendlyVscName_Type = DisplayString
_CoVscCfgFriendlyVscName_Object = MibTableColumn
coVscCfgFriendlyVscName = _CoVscCfgFriendlyVscName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 2),
    _CoVscCfgFriendlyVscName_Type()
)
coVscCfgFriendlyVscName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVscCfgFriendlyVscName.setStatus("current")
_CoVscCfgSSID_Type = AlvarionSSID
_CoVscCfgSSID_Object = MibTableColumn
coVscCfgSSID = _CoVscCfgSSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 3),
    _CoVscCfgSSID_Type()
)
coVscCfgSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVscCfgSSID.setStatus("current")
_CoVscCfgAccessControlled_Type = TruthValue
_CoVscCfgAccessControlled_Object = MibTableColumn
coVscCfgAccessControlled = _CoVscCfgAccessControlled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 4),
    _CoVscCfgAccessControlled_Type()
)
coVscCfgAccessControlled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVscCfgAccessControlled.setStatus("current")


class _CoVscCfgSecurity_Type(Integer32):
    """Custom type coVscCfgSecurity based on Integer32"""
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
        *(("ieee802dot1x", 2),
          ("open", 1),
          ("wpa", 3),
          ("wpa2", 4),
          ("wpaAndWpa2", 5))
    )


_CoVscCfgSecurity_Type.__name__ = "Integer32"
_CoVscCfgSecurity_Object = MibTableColumn
coVscCfgSecurity = _CoVscCfgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 5),
    _CoVscCfgSecurity_Type()
)
coVscCfgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVscCfgSecurity.setStatus("current")


class _CoVscCfgEncryption_Type(Integer32):
    """Custom type coVscCfgEncryption based on Integer32"""
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
        *(("aes", 4),
          ("none", 1),
          ("tkip", 3),
          ("tkipAndAes", 5),
          ("wep", 2))
    )


_CoVscCfgEncryption_Type.__name__ = "Integer32"
_CoVscCfgEncryption_Object = MibTableColumn
coVscCfgEncryption = _CoVscCfgEncryption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 6),
    _CoVscCfgEncryption_Type()
)
coVscCfgEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVscCfgEncryption.setStatus("current")


class _CoVscCfg8021xAuthentication_Type(Integer32):
    """Custom type coVscCfg8021xAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("psk", 3),
          ("radius", 2))
    )


_CoVscCfg8021xAuthentication_Type.__name__ = "Integer32"
_CoVscCfg8021xAuthentication_Object = MibTableColumn
coVscCfg8021xAuthentication = _CoVscCfg8021xAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 7),
    _CoVscCfg8021xAuthentication_Type()
)
coVscCfg8021xAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVscCfg8021xAuthentication.setStatus("current")
_CoVscCfgMACAuthentication_Type = TruthValue
_CoVscCfgMACAuthentication_Object = MibTableColumn
coVscCfgMACAuthentication = _CoVscCfgMACAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 8),
    _CoVscCfgMACAuthentication_Type()
)
coVscCfgMACAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVscCfgMACAuthentication.setStatus("current")
_CoVscCfgHTMLAuthentication_Type = TruthValue
_CoVscCfgHTMLAuthentication_Object = MibTableColumn
coVscCfgHTMLAuthentication = _CoVscCfgHTMLAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 9),
    _CoVscCfgHTMLAuthentication_Type()
)
coVscCfgHTMLAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVscCfgHTMLAuthentication.setStatus("current")
_AlvarionVscMIBConformance_ObjectIdentity = ObjectIdentity
alvarionVscMIBConformance = _AlvarionVscMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2)
)
_AlvarionVscMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionVscMIBCompliances = _AlvarionVscMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2, 1)
)
_AlvarionVscMIBGroups_ObjectIdentity = ObjectIdentity
alvarionVscMIBGroups = _AlvarionVscMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2, 2)
)

# Managed Objects groups

alvarionVscMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2, 2, 1)
)
alvarionVscMIBGroup.setObjects(
      *(("ALVARION-VSC-MIB", "coVscCfgFriendlyVscName"),
        ("ALVARION-VSC-MIB", "coVscCfgSSID"),
        ("ALVARION-VSC-MIB", "coVscCfgAccessControlled"),
        ("ALVARION-VSC-MIB", "coVscCfgSecurity"),
        ("ALVARION-VSC-MIB", "coVscCfgEncryption"),
        ("ALVARION-VSC-MIB", "coVscCfg8021xAuthentication"),
        ("ALVARION-VSC-MIB", "coVscCfgMACAuthentication"),
        ("ALVARION-VSC-MIB", "coVscCfgHTMLAuthentication"))
)
if mibBuilder.loadTexts:
    alvarionVscMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alvarionVscMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionVscMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-VSC-MIB",
    **{"alvarionVscMIB": alvarionVscMIB,
       "alvarionVscMIBObjects": alvarionVscMIBObjects,
       "coVscConfigGroup": coVscConfigGroup,
       "coVscConfigTable": coVscConfigTable,
       "coVscConfigEntry": coVscConfigEntry,
       "coVscCfgIndex": coVscCfgIndex,
       "coVscCfgFriendlyVscName": coVscCfgFriendlyVscName,
       "coVscCfgSSID": coVscCfgSSID,
       "coVscCfgAccessControlled": coVscCfgAccessControlled,
       "coVscCfgSecurity": coVscCfgSecurity,
       "coVscCfgEncryption": coVscCfgEncryption,
       "coVscCfg8021xAuthentication": coVscCfg8021xAuthentication,
       "coVscCfgMACAuthentication": coVscCfgMACAuthentication,
       "coVscCfgHTMLAuthentication": coVscCfgHTMLAuthentication,
       "alvarionVscMIBConformance": alvarionVscMIBConformance,
       "alvarionVscMIBCompliances": alvarionVscMIBCompliances,
       "alvarionVscMIBCompliance": alvarionVscMIBCompliance,
       "alvarionVscMIBGroups": alvarionVscMIBGroups,
       "alvarionVscMIBGroup": alvarionVscMIBGroup}
)
