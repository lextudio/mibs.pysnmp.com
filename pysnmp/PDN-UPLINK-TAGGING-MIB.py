# SNMP MIB module (PDN-UPLINK-TAGGING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-UPLINK-TAGGING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:13 2024
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

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

pdnUplinkTagging = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37)
)
pdnUplinkTagging.setRevisions(
        ("2003-03-12 00:00",
         "2002-05-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnUplinkTaggingObjects_ObjectIdentity = ObjectIdentity
pdnUplinkTaggingObjects = _PdnUplinkTaggingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 1)
)


class _UltBaseVlanTag_Type(Integer32):
    """Custom type ultBaseVlanTag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ultBase1024", 3),
          ("ultBase1536", 4),
          ("ultBase16", 1),
          ("ultBase2048", 5),
          ("ultBase2560", 6),
          ("ultBase3072", 7),
          ("ultBase3584", 8),
          ("ultBase512", 2))
    )


_UltBaseVlanTag_Type.__name__ = "Integer32"
_UltBaseVlanTag_Object = MibScalar
ultBaseVlanTag = _UltBaseVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 1, 1),
    _UltBaseVlanTag_Type()
)
ultBaseVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ultBaseVlanTag.setStatus("deprecated")


class _UltIndex_Type(Integer32):
    """Custom type ultIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_UltIndex_Type.__name__ = "Integer32"
_UltIndex_Object = MibScalar
ultIndex = _UltIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 1, 2),
    _UltIndex_Type()
)
ultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ultIndex.setStatus("deprecated")
_PdnUplinkTaggingConformance_ObjectIdentity = ObjectIdentity
pdnUplinkTaggingConformance = _PdnUplinkTaggingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2)
)
_PdnUplinkTaggingGroups_ObjectIdentity = ObjectIdentity
pdnUplinkTaggingGroups = _PdnUplinkTaggingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2, 1)
)
_PdnUplinkTaggingCompliances_ObjectIdentity = ObjectIdentity
pdnUplinkTaggingCompliances = _PdnUplinkTaggingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2, 2)
)
_PdnUplinkTaggingDeprecatedGroup_ObjectIdentity = ObjectIdentity
pdnUplinkTaggingDeprecatedGroup = _PdnUplinkTaggingDeprecatedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2, 3)
)
_PdnUplinkTaggingObjectsR2_ObjectIdentity = ObjectIdentity
pdnUplinkTaggingObjectsR2 = _PdnUplinkTaggingObjectsR2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 3)
)


class _PdnUltIndex_Type(Unsigned32):
    """Custom type pdnUltIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PdnUltIndex_Type.__name__ = "Unsigned32"
_PdnUltIndex_Object = MibScalar
pdnUltIndex = _PdnUltIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 3, 1),
    _PdnUltIndex_Type()
)
pdnUltIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnUltIndex.setStatus("current")


class _PdnGenUltBaseVlanTag_Type(VlanId):
    """Custom type pdnGenUltBaseVlanTag based on VlanId"""
    defaultValue = 16


_PdnGenUltBaseVlanTag_Object = MibScalar
pdnGenUltBaseVlanTag = _PdnGenUltBaseVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 3, 2),
    _PdnGenUltBaseVlanTag_Type()
)
pdnGenUltBaseVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnGenUltBaseVlanTag.setStatus("current")


class _Pdn48UltBaseVlanTag_Type(Integer32):
    """Custom type pdn48UltBaseVlanTag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ultBase1024", 3),
          ("ultBase1536", 4),
          ("ultBase16", 1),
          ("ultBase2048", 5),
          ("ultBase2560", 6),
          ("ultBase3072", 7),
          ("ultBase3584", 8),
          ("ultBase512", 2))
    )


_Pdn48UltBaseVlanTag_Type.__name__ = "Integer32"
_Pdn48UltBaseVlanTag_Object = MibScalar
pdn48UltBaseVlanTag = _Pdn48UltBaseVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 3, 3),
    _Pdn48UltBaseVlanTag_Type()
)
pdn48UltBaseVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdn48UltBaseVlanTag.setStatus("current")


class _Pdn24UltBaseVlanTag_Type(Integer32):
    """Custom type pdn24UltBaseVlanTag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ultBase1024", 5),
          ("ultBase1280", 6),
          ("ultBase1536", 7),
          ("ultBase16", 1),
          ("ultBase1792", 8),
          ("ultBase2048", 9),
          ("ultBase2304", 10),
          ("ultBase256", 2),
          ("ultBase2560", 11),
          ("ultBase2816", 12),
          ("ultBase3072", 13),
          ("ultBase3328", 14),
          ("ultBase3584", 15),
          ("ultBase3840", 16),
          ("ultBase512", 3),
          ("ultBase768", 4))
    )


_Pdn24UltBaseVlanTag_Type.__name__ = "Integer32"
_Pdn24UltBaseVlanTag_Object = MibScalar
pdn24UltBaseVlanTag = _Pdn24UltBaseVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 3, 4),
    _Pdn24UltBaseVlanTag_Type()
)
pdn24UltBaseVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdn24UltBaseVlanTag.setStatus("current")

# Managed Objects groups

pdn48PortUpLinkTaggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2, 1, 1)
)
pdn48PortUpLinkTaggingGroup.setObjects(
      *(("PDN-UPLINK-TAGGING-MIB", "pdnUltIndex"),
        ("PDN-UPLINK-TAGGING-MIB", "pdnGenUltBaseVlanTag"),
        ("PDN-UPLINK-TAGGING-MIB", "pdn48UltBaseVlanTag"))
)
if mibBuilder.loadTexts:
    pdn48PortUpLinkTaggingGroup.setStatus("current")

pdn24PortUpLinkTaggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2, 1, 2)
)
pdn24PortUpLinkTaggingGroup.setObjects(
      *(("PDN-UPLINK-TAGGING-MIB", "pdnUltIndex"),
        ("PDN-UPLINK-TAGGING-MIB", "pdnGenUltBaseVlanTag"),
        ("PDN-UPLINK-TAGGING-MIB", "pdn24UltBaseVlanTag"))
)
if mibBuilder.loadTexts:
    pdn24PortUpLinkTaggingGroup.setStatus("current")

upLinkTaggingDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2, 3, 1)
)
upLinkTaggingDeprecatedGroup.setObjects(
      *(("PDN-UPLINK-TAGGING-MIB", "ultBaseVlanTag"),
        ("PDN-UPLINK-TAGGING-MIB", "ultIndex"))
)
if mibBuilder.loadTexts:
    upLinkTaggingDeprecatedGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-UPLINK-TAGGING-MIB",
    **{"pdnUplinkTagging": pdnUplinkTagging,
       "pdnUplinkTaggingObjects": pdnUplinkTaggingObjects,
       "ultBaseVlanTag": ultBaseVlanTag,
       "ultIndex": ultIndex,
       "pdnUplinkTaggingConformance": pdnUplinkTaggingConformance,
       "pdnUplinkTaggingGroups": pdnUplinkTaggingGroups,
       "pdn48PortUpLinkTaggingGroup": pdn48PortUpLinkTaggingGroup,
       "pdn24PortUpLinkTaggingGroup": pdn24PortUpLinkTaggingGroup,
       "pdnUplinkTaggingCompliances": pdnUplinkTaggingCompliances,
       "pdnUplinkTaggingDeprecatedGroup": pdnUplinkTaggingDeprecatedGroup,
       "upLinkTaggingDeprecatedGroup": upLinkTaggingDeprecatedGroup,
       "pdnUplinkTaggingObjectsR2": pdnUplinkTaggingObjectsR2,
       "pdnUltIndex": pdnUltIndex,
       "pdnGenUltBaseVlanTag": pdnGenUltBaseVlanTag,
       "pdn48UltBaseVlanTag": pdn48UltBaseVlanTag,
       "pdn24UltBaseVlanTag": pdn24UltBaseVlanTag}
)
