# SNMP MIB module (ATM-FORUM-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-FORUM-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:50 2024
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class TruthValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )



class ClnpAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 21),
    )



class AtmServiceCategory(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abr", 5),
          ("cbr", 2),
          ("nrtVbr", 4),
          ("other", 1),
          ("rtVbr", 3),
          ("ubr", 6))
    )



class AtmAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(20, 20),
    )



class NetPrefix(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(13, 13),
    )



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumAdmin_ObjectIdentity = ObjectIdentity
atmForumAdmin = _AtmForumAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1)
)
_AtmfTransmissionTypes_ObjectIdentity = ObjectIdentity
atmfTransmissionTypes = _AtmfTransmissionTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2)
)
_AtmfUnknownType_ObjectIdentity = ObjectIdentity
atmfUnknownType = _AtmfUnknownType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 1)
)
_AtmfSonetSTS3c_ObjectIdentity = ObjectIdentity
atmfSonetSTS3c = _AtmfSonetSTS3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 2)
)
_AtmfDs3_ObjectIdentity = ObjectIdentity
atmfDs3 = _AtmfDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 3)
)
_Atmf4B5B_ObjectIdentity = ObjectIdentity
atmf4B5B = _Atmf4B5B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 4)
)
_Atmf8B10B_ObjectIdentity = ObjectIdentity
atmf8B10B = _Atmf8B10B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 5)
)
_AtmfSonetSTS12c_ObjectIdentity = ObjectIdentity
atmfSonetSTS12c = _AtmfSonetSTS12c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 6)
)
_AtmfE3_ObjectIdentity = ObjectIdentity
atmfE3 = _AtmfE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 7)
)
_AtmfT1_ObjectIdentity = ObjectIdentity
atmfT1 = _AtmfT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 8)
)
_AtmfE1_ObjectIdentity = ObjectIdentity
atmfE1 = _AtmfE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 9)
)
_AtmfMediaTypes_ObjectIdentity = ObjectIdentity
atmfMediaTypes = _AtmfMediaTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3)
)
_AtmfMediaUnknownType_ObjectIdentity = ObjectIdentity
atmfMediaUnknownType = _AtmfMediaUnknownType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3, 1)
)
_AtmfMediaCoaxCable_ObjectIdentity = ObjectIdentity
atmfMediaCoaxCable = _AtmfMediaCoaxCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3, 2)
)
_AtmfMediaSingleMode_ObjectIdentity = ObjectIdentity
atmfMediaSingleMode = _AtmfMediaSingleMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3, 3)
)
_AtmfMediaMultiMode_ObjectIdentity = ObjectIdentity
atmfMediaMultiMode = _AtmfMediaMultiMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3, 4)
)
_AtmfMediaStp_ObjectIdentity = ObjectIdentity
atmfMediaStp = _AtmfMediaStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3, 5)
)
_AtmfMediaUtp_ObjectIdentity = ObjectIdentity
atmfMediaUtp = _AtmfMediaUtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3, 6)
)
_AtmfTrafficDescrTypes_ObjectIdentity = ObjectIdentity
atmfTrafficDescrTypes = _AtmfTrafficDescrTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4)
)
_AtmfNoDescriptor_ObjectIdentity = ObjectIdentity
atmfNoDescriptor = _AtmfNoDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 1)
)
_AtmfPeakRate_ObjectIdentity = ObjectIdentity
atmfPeakRate = _AtmfPeakRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 2)
)
_AtmfNoClpNoScr_ObjectIdentity = ObjectIdentity
atmfNoClpNoScr = _AtmfNoClpNoScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 3)
)
_AtmfClpNoTaggingNoScr_ObjectIdentity = ObjectIdentity
atmfClpNoTaggingNoScr = _AtmfClpNoTaggingNoScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 4)
)
_AtmfClpTaggingNoScr_ObjectIdentity = ObjectIdentity
atmfClpTaggingNoScr = _AtmfClpTaggingNoScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 5)
)
_AtmfNoClpScr_ObjectIdentity = ObjectIdentity
atmfNoClpScr = _AtmfNoClpScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 6)
)
_AtmfClpNoTaggingScr_ObjectIdentity = ObjectIdentity
atmfClpNoTaggingScr = _AtmfClpNoTaggingScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 7)
)
_AtmfClpTaggingScr_ObjectIdentity = ObjectIdentity
atmfClpTaggingScr = _AtmfClpTaggingScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 8)
)
_AtmfClpNoTaggingMcr_ObjectIdentity = ObjectIdentity
atmfClpNoTaggingMcr = _AtmfClpNoTaggingMcr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 9)
)
_AtmfSrvcRegTypes_ObjectIdentity = ObjectIdentity
atmfSrvcRegTypes = _AtmfSrvcRegTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 5)
)
_AtmForumUni_ObjectIdentity = ObjectIdentity
atmForumUni = _AtmForumUni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2)
)
_AtmfPhysicalGroup_ObjectIdentity = ObjectIdentity
atmfPhysicalGroup = _AtmfPhysicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 1)
)
_AtmfAtmLayerGroup_ObjectIdentity = ObjectIdentity
atmfAtmLayerGroup = _AtmfAtmLayerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 2)
)
_AtmfAtmStatsGroup_ObjectIdentity = ObjectIdentity
atmfAtmStatsGroup = _AtmfAtmStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 3)
)
_AtmfVpcGroup_ObjectIdentity = ObjectIdentity
atmfVpcGroup = _AtmfVpcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 4)
)
_AtmfVccGroup_ObjectIdentity = ObjectIdentity
atmfVccGroup = _AtmfVccGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 5)
)
_AtmfAddressGroup_ObjectIdentity = ObjectIdentity
atmfAddressGroup = _AtmfAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 6)
)
_AtmfNetPrefixGroup_ObjectIdentity = ObjectIdentity
atmfNetPrefixGroup = _AtmfNetPrefixGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 7)
)
_AtmfSrvcRegistryGroup_ObjectIdentity = ObjectIdentity
atmfSrvcRegistryGroup = _AtmfSrvcRegistryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 8)
)
_AtmfVpcAbrGroup_ObjectIdentity = ObjectIdentity
atmfVpcAbrGroup = _AtmfVpcAbrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 9)
)
_AtmfVccAbrGroup_ObjectIdentity = ObjectIdentity
atmfVccAbrGroup = _AtmfVccAbrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 10)
)
_AtmfAddressRegistrationAdminGroup_ObjectIdentity = ObjectIdentity
atmfAddressRegistrationAdminGroup = _AtmfAddressRegistrationAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-FORUM-TC-MIB",
    **{"TruthValue": TruthValue,
       "ClnpAddress": ClnpAddress,
       "AtmServiceCategory": AtmServiceCategory,
       "AtmAddress": AtmAddress,
       "NetPrefix": NetPrefix,
       "atmForum": atmForum,
       "atmForumAdmin": atmForumAdmin,
       "atmfTransmissionTypes": atmfTransmissionTypes,
       "atmfUnknownType": atmfUnknownType,
       "atmfSonetSTS3c": atmfSonetSTS3c,
       "atmfDs3": atmfDs3,
       "atmf4B5B": atmf4B5B,
       "atmf8B10B": atmf8B10B,
       "atmfSonetSTS12c": atmfSonetSTS12c,
       "atmfE3": atmfE3,
       "atmfT1": atmfT1,
       "atmfE1": atmfE1,
       "atmfMediaTypes": atmfMediaTypes,
       "atmfMediaUnknownType": atmfMediaUnknownType,
       "atmfMediaCoaxCable": atmfMediaCoaxCable,
       "atmfMediaSingleMode": atmfMediaSingleMode,
       "atmfMediaMultiMode": atmfMediaMultiMode,
       "atmfMediaStp": atmfMediaStp,
       "atmfMediaUtp": atmfMediaUtp,
       "atmfTrafficDescrTypes": atmfTrafficDescrTypes,
       "atmfNoDescriptor": atmfNoDescriptor,
       "atmfPeakRate": atmfPeakRate,
       "atmfNoClpNoScr": atmfNoClpNoScr,
       "atmfClpNoTaggingNoScr": atmfClpNoTaggingNoScr,
       "atmfClpTaggingNoScr": atmfClpTaggingNoScr,
       "atmfNoClpScr": atmfNoClpScr,
       "atmfClpNoTaggingScr": atmfClpNoTaggingScr,
       "atmfClpTaggingScr": atmfClpTaggingScr,
       "atmfClpNoTaggingMcr": atmfClpNoTaggingMcr,
       "atmfSrvcRegTypes": atmfSrvcRegTypes,
       "atmForumUni": atmForumUni,
       "atmfPhysicalGroup": atmfPhysicalGroup,
       "atmfAtmLayerGroup": atmfAtmLayerGroup,
       "atmfAtmStatsGroup": atmfAtmStatsGroup,
       "atmfVpcGroup": atmfVpcGroup,
       "atmfVccGroup": atmfVccGroup,
       "atmfAddressGroup": atmfAddressGroup,
       "atmfNetPrefixGroup": atmfNetPrefixGroup,
       "atmfSrvcRegistryGroup": atmfSrvcRegistryGroup,
       "atmfVpcAbrGroup": atmfVpcAbrGroup,
       "atmfVccAbrGroup": atmfVccAbrGroup,
       "atmfAddressRegistrationAdminGroup": atmfAddressRegistrationAdminGroup}
)
