# SNMP MIB module (Fore-PNNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-PNNI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:09 2024
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

(NsapAddr,
 NsapPrefix,
 software) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "NsapAddr",
    "NsapPrefix",
    "software")

(portNumber,) = mibBuilder.importSymbols(
    "Fore-Switch-MIB",
    "portNumber")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(AtmAddrPrefix,
 PnniMetricsTag,
 PnniNodeId,
 PnniNodeIndex,
 PnniPortId,
 PnniPrefixLength,
 ServiceCategory,
 TnsPlan,
 TnsType,
 pnniDTLIndex,
 pnniMapAddrAdvertisedPortId,
 pnniMapAddrAdvertisingNodeId,
 pnniMapAddrIndex,
 pnniMapIndex,
 pnniMapOriginatingNodeId,
 pnniMapOriginatingPortId,
 pnniNodeIndex) = mibBuilder.importSymbols(
    "PNNI-MIB",
    "AtmAddrPrefix",
    "PnniMetricsTag",
    "PnniNodeId",
    "PnniNodeIndex",
    "PnniPortId",
    "PnniPrefixLength",
    "ServiceCategory",
    "TnsPlan",
    "TnsType",
    "pnniDTLIndex",
    "pnniMapAddrAdvertisedPortId",
    "pnniMapAddrAdvertisingNodeId",
    "pnniMapAddrIndex",
    "pnniMapIndex",
    "pnniMapOriginatingNodeId",
    "pnniMapOriginatingPortId",
    "pnniNodeIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

forePnniGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4)
)


# Types definitions



class PnniPcProfileIndex(Integer32):
    """Custom type PnniPcProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )





class InterfaceLabel(OctetString):
    """Custom type InterfaceLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PnniGroup_ObjectIdentity = ObjectIdentity
pnniGroup = _PnniGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1)
)
_PnniPcProfileTable_Object = MibTable
pnniPcProfileTable = _PnniPcProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    pnniPcProfileTable.setStatus("current")
_PnniPcProfileEntry_Object = MibTableRow
pnniPcProfileEntry = _PnniPcProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1)
)
pnniPcProfileEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "Fore-PNNI-MIB", "pnniPcProfileIndex"),
)
if mibBuilder.loadTexts:
    pnniPcProfileEntry.setStatus("current")
_PnniPcProfileIndex_Type = PnniPcProfileIndex
_PnniPcProfileIndex_Object = MibTableColumn
pnniPcProfileIndex = _PnniPcProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 1),
    _PnniPcProfileIndex_Type()
)
pnniPcProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniPcProfileIndex.setStatus("current")


class _PnniPcProfileType_Type(Integer32):
    """Custom type pnniPcProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cacheEntry", 2),
          ("mgmtEntry", 1))
    )


_PnniPcProfileType_Type.__name__ = "Integer32"
_PnniPcProfileType_Object = MibTableColumn
pnniPcProfileType = _PnniPcProfileType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 2),
    _PnniPcProfileType_Type()
)
pnniPcProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileType.setStatus("current")


class _PnniPcProfileServiceCategory_Type(ServiceCategory):
    """Custom type pnniPcProfileServiceCategory based on ServiceCategory"""


_PnniPcProfileServiceCategory_Object = MibTableColumn
pnniPcProfileServiceCategory = _PnniPcProfileServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 3),
    _PnniPcProfileServiceCategory_Type()
)
pnniPcProfileServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileServiceCategory.setStatus("current")
_PnniPcProfileMinFwdCR_Type = Unsigned32
_PnniPcProfileMinFwdCR_Object = MibTableColumn
pnniPcProfileMinFwdCR = _PnniPcProfileMinFwdCR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 4),
    _PnniPcProfileMinFwdCR_Type()
)
pnniPcProfileMinFwdCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileMinFwdCR.setStatus("current")
_PnniPcProfileMinRevCR_Type = Unsigned32
_PnniPcProfileMinRevCR_Object = MibTableColumn
pnniPcProfileMinRevCR = _PnniPcProfileMinRevCR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 5),
    _PnniPcProfileMinRevCR_Type()
)
pnniPcProfileMinRevCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileMinRevCR.setStatus("current")


class _PnniPcProfileFwdClpType_Type(Integer32):
    """Custom type pnniPcProfileFwdClpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clpEqual0", 1),
          ("clpEqual0Or1", 2))
    )


_PnniPcProfileFwdClpType_Type.__name__ = "Integer32"
_PnniPcProfileFwdClpType_Object = MibTableColumn
pnniPcProfileFwdClpType = _PnniPcProfileFwdClpType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 6),
    _PnniPcProfileFwdClpType_Type()
)
pnniPcProfileFwdClpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileFwdClpType.setStatus("current")


class _PnniPcProfileRevClpType_Type(Integer32):
    """Custom type pnniPcProfileRevClpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clpEqual0", 1),
          ("clpEqual0Or1", 2))
    )


_PnniPcProfileRevClpType_Type.__name__ = "Integer32"
_PnniPcProfileRevClpType_Object = MibTableColumn
pnniPcProfileRevClpType = _PnniPcProfileRevClpType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 7),
    _PnniPcProfileRevClpType_Type()
)
pnniPcProfileRevClpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileRevClpType.setStatus("current")
_PnniPcProfileFwdCLR_Type = Unsigned32
_PnniPcProfileFwdCLR_Object = MibTableColumn
pnniPcProfileFwdCLR = _PnniPcProfileFwdCLR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 8),
    _PnniPcProfileFwdCLR_Type()
)
pnniPcProfileFwdCLR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileFwdCLR.setStatus("current")
_PnniPcProfileRevCLR_Type = Unsigned32
_PnniPcProfileRevCLR_Object = MibTableColumn
pnniPcProfileRevCLR = _PnniPcProfileRevCLR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 9),
    _PnniPcProfileRevCLR_Type()
)
pnniPcProfileRevCLR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileRevCLR.setStatus("current")


class _PnniPcProfileOptCTD_Type(TruthValue):
    """Custom type pnniPcProfileOptCTD based on TruthValue"""


_PnniPcProfileOptCTD_Object = MibTableColumn
pnniPcProfileOptCTD = _PnniPcProfileOptCTD_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 10),
    _PnniPcProfileOptCTD_Type()
)
pnniPcProfileOptCTD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileOptCTD.setStatus("current")


class _PnniPcProfileOptCDV_Type(TruthValue):
    """Custom type pnniPcProfileOptCDV based on TruthValue"""


_PnniPcProfileOptCDV_Object = MibTableColumn
pnniPcProfileOptCDV = _PnniPcProfileOptCDV_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 11),
    _PnniPcProfileOptCDV_Type()
)
pnniPcProfileOptCDV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileOptCDV.setStatus("current")


class _PnniPcProfileOptAdminWeight_Type(Integer32):
    """Custom type pnniPcProfileOptAdminWeight based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aw", 2),
          ("caw", 3),
          ("none", 1))
    )


_PnniPcProfileOptAdminWeight_Type.__name__ = "Integer32"
_PnniPcProfileOptAdminWeight_Object = MibTableColumn
pnniPcProfileOptAdminWeight = _PnniPcProfileOptAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 12),
    _PnniPcProfileOptAdminWeight_Type()
)
pnniPcProfileOptAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileOptAdminWeight.setStatus("current")


class _PnniPcProfileRstrVPOnly_Type(TruthValue):
    """Custom type pnniPcProfileRstrVPOnly based on TruthValue"""


_PnniPcProfileRstrVPOnly_Object = MibTableColumn
pnniPcProfileRstrVPOnly = _PnniPcProfileRstrVPOnly_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 13),
    _PnniPcProfileRstrVPOnly_Type()
)
pnniPcProfileRstrVPOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileRstrVPOnly.setStatus("current")


class _PnniPcProfileRstrLoadBalance_Type(TruthValue):
    """Custom type pnniPcProfileRstrLoadBalance based on TruthValue"""


_PnniPcProfileRstrLoadBalance_Object = MibTableColumn
pnniPcProfileRstrLoadBalance = _PnniPcProfileRstrLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 14),
    _PnniPcProfileRstrLoadBalance_Type()
)
pnniPcProfileRstrLoadBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileRstrLoadBalance.setStatus("current")
_PnniPcProfileNumberOfAvoidLinks_Type = Unsigned32
_PnniPcProfileNumberOfAvoidLinks_Object = MibTableColumn
pnniPcProfileNumberOfAvoidLinks = _PnniPcProfileNumberOfAvoidLinks_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 15),
    _PnniPcProfileNumberOfAvoidLinks_Type()
)
pnniPcProfileNumberOfAvoidLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileNumberOfAvoidLinks.setStatus("current")
_PnniPcProfileNumberOfPreferLinks_Type = Unsigned32
_PnniPcProfileNumberOfPreferLinks_Object = MibTableColumn
pnniPcProfileNumberOfPreferLinks = _PnniPcProfileNumberOfPreferLinks_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 16),
    _PnniPcProfileNumberOfPreferLinks_Type()
)
pnniPcProfileNumberOfPreferLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileNumberOfPreferLinks.setStatus("current")
_PnniPcProfileNumberOfHits_Type = Unsigned32
_PnniPcProfileNumberOfHits_Object = MibTableColumn
pnniPcProfileNumberOfHits = _PnniPcProfileNumberOfHits_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 17),
    _PnniPcProfileNumberOfHits_Type()
)
pnniPcProfileNumberOfHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileNumberOfHits.setStatus("current")
_PnniPcProfileTimeStamp_Type = TimeStamp
_PnniPcProfileTimeStamp_Object = MibTableColumn
pnniPcProfileTimeStamp = _PnniPcProfileTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 18),
    _PnniPcProfileTimeStamp_Type()
)
pnniPcProfileTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileTimeStamp.setStatus("current")


class _PnniPcProfileState_Type(Integer32):
    """Custom type pnniPcProfileState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("computed", 2),
          ("computing", 3),
          ("inactive", 1),
          ("touched", 4))
    )


_PnniPcProfileState_Type.__name__ = "Integer32"
_PnniPcProfileState_Object = MibTableColumn
pnniPcProfileState = _PnniPcProfileState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 19),
    _PnniPcProfileState_Type()
)
pnniPcProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileState.setStatus("current")
_PnniPcProfileRowStatus_Type = RowStatus
_PnniPcProfileRowStatus_Object = MibTableColumn
pnniPcProfileRowStatus = _PnniPcProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 20),
    _PnniPcProfileRowStatus_Type()
)
pnniPcProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileRowStatus.setStatus("current")
_PnniPcProfileCongestionBased_Type = TruthValue
_PnniPcProfileCongestionBased_Object = MibTableColumn
pnniPcProfileCongestionBased = _PnniPcProfileCongestionBased_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 1, 1, 21),
    _PnniPcProfileCongestionBased_Type()
)
pnniPcProfileCongestionBased.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniPcProfileCongestionBased.setStatus("current")
_PnniExportPolicyTable_Object = MibTable
pnniExportPolicyTable = _PnniExportPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    pnniExportPolicyTable.setStatus("current")
_PnniExportPolicyEntry_Object = MibTableRow
pnniExportPolicyEntry = _PnniExportPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 2, 1)
)
pnniExportPolicyEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "Fore-PNNI-MIB", "pnniExportPolicyAddress"),
    (0, "Fore-PNNI-MIB", "pnniExportPolicyPrefixLength"),
)
if mibBuilder.loadTexts:
    pnniExportPolicyEntry.setStatus("current")
_PnniExportPolicyAddress_Type = AtmAddrPrefix
_PnniExportPolicyAddress_Object = MibTableColumn
pnniExportPolicyAddress = _PnniExportPolicyAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 2, 1, 1),
    _PnniExportPolicyAddress_Type()
)
pnniExportPolicyAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniExportPolicyAddress.setStatus("current")
_PnniExportPolicyPrefixLength_Type = PnniPrefixLength
_PnniExportPolicyPrefixLength_Object = MibTableColumn
pnniExportPolicyPrefixLength = _PnniExportPolicyPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 2, 1, 2),
    _PnniExportPolicyPrefixLength_Type()
)
pnniExportPolicyPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniExportPolicyPrefixLength.setStatus("current")


class _PnniExportPolicyType_Type(Integer32):
    """Custom type pnniExportPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("exterior", 2),
          ("internal", 1))
    )


_PnniExportPolicyType_Type.__name__ = "Integer32"
_PnniExportPolicyType_Object = MibTableColumn
pnniExportPolicyType = _PnniExportPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 2, 1, 3),
    _PnniExportPolicyType_Type()
)
pnniExportPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniExportPolicyType.setStatus("current")


class _PnniExportPolicyAction_Type(Integer32):
    """Custom type pnniExportPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 3),
          ("summary", 1),
          ("suppress", 2))
    )


_PnniExportPolicyAction_Type.__name__ = "Integer32"
_PnniExportPolicyAction_Object = MibTableColumn
pnniExportPolicyAction = _PnniExportPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 2, 1, 4),
    _PnniExportPolicyAction_Type()
)
pnniExportPolicyAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniExportPolicyAction.setStatus("current")


class _PnniExportPolicyState_Type(Integer32):
    """Custom type pnniExportPolicyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("advertising", 3),
          ("inactive", 4),
          ("summarizing", 1),
          ("suppressing", 2))
    )


_PnniExportPolicyState_Type.__name__ = "Integer32"
_PnniExportPolicyState_Object = MibTableColumn
pnniExportPolicyState = _PnniExportPolicyState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 2, 1, 5),
    _PnniExportPolicyState_Type()
)
pnniExportPolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniExportPolicyState.setStatus("current")
_PnniExportPolicyTnsType_Type = TnsType
_PnniExportPolicyTnsType_Object = MibTableColumn
pnniExportPolicyTnsType = _PnniExportPolicyTnsType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 2, 1, 6),
    _PnniExportPolicyTnsType_Type()
)
pnniExportPolicyTnsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniExportPolicyTnsType.setStatus("current")
_PnniExportPolicyTnsPlan_Type = TnsPlan
_PnniExportPolicyTnsPlan_Object = MibTableColumn
pnniExportPolicyTnsPlan = _PnniExportPolicyTnsPlan_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 2, 1, 7),
    _PnniExportPolicyTnsPlan_Type()
)
pnniExportPolicyTnsPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniExportPolicyTnsPlan.setStatus("current")
_PnniExportPolicyTnsId_Type = DisplayString
_PnniExportPolicyTnsId_Object = MibTableColumn
pnniExportPolicyTnsId = _PnniExportPolicyTnsId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 2, 1, 8),
    _PnniExportPolicyTnsId_Type()
)
pnniExportPolicyTnsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniExportPolicyTnsId.setStatus("current")
_PnniExportPolicyMetricsTag_Type = PnniMetricsTag
_PnniExportPolicyMetricsTag_Object = MibTableColumn
pnniExportPolicyMetricsTag = _PnniExportPolicyMetricsTag_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 2, 1, 9),
    _PnniExportPolicyMetricsTag_Type()
)
pnniExportPolicyMetricsTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniExportPolicyMetricsTag.setStatus("current")
_PnniExportPolicyRowStatus_Type = RowStatus
_PnniExportPolicyRowStatus_Object = MibTableColumn
pnniExportPolicyRowStatus = _PnniExportPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 2, 1, 10),
    _PnniExportPolicyRowStatus_Type()
)
pnniExportPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniExportPolicyRowStatus.setStatus("current")
_PnniNodeExtnTable_Object = MibTable
pnniNodeExtnTable = _PnniNodeExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    pnniNodeExtnTable.setStatus("current")
_PnniNodeExtnEntry_Object = MibTableRow
pnniNodeExtnEntry = _PnniNodeExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 3, 1)
)
pnniNodeExtnEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
)
if mibBuilder.loadTexts:
    pnniNodeExtnEntry.setStatus("current")
_PnniNodeExtnDomainID_Type = Integer32
_PnniNodeExtnDomainID_Object = MibTableColumn
pnniNodeExtnDomainID = _PnniNodeExtnDomainID_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 3, 1, 1),
    _PnniNodeExtnDomainID_Type()
)
pnniNodeExtnDomainID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeExtnDomainID.setStatus("current")
_PnniNodeExtnForeLevel_Type = Integer32
_PnniNodeExtnForeLevel_Object = MibTableColumn
pnniNodeExtnForeLevel = _PnniNodeExtnForeLevel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 3, 1, 2),
    _PnniNodeExtnForeLevel_Type()
)
pnniNodeExtnForeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeExtnForeLevel.setStatus("current")
_PnniNodeExtnForeArea_Type = Integer32
_PnniNodeExtnForeArea_Object = MibTableColumn
pnniNodeExtnForeArea = _PnniNodeExtnForeArea_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 3, 1, 3),
    _PnniNodeExtnForeArea_Type()
)
pnniNodeExtnForeArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeExtnForeArea.setStatus("current")
_PnniNodeExtnShutdown_Type = TruthValue
_PnniNodeExtnShutdown_Object = MibTableColumn
pnniNodeExtnShutdown = _PnniNodeExtnShutdown_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 3, 1, 4),
    _PnniNodeExtnShutdown_Type()
)
pnniNodeExtnShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeExtnShutdown.setStatus("current")
_PnniNodeExtnLoadBalancing_Type = TruthValue
_PnniNodeExtnLoadBalancing_Object = MibTableColumn
pnniNodeExtnLoadBalancing = _PnniNodeExtnLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 3, 1, 5),
    _PnniNodeExtnLoadBalancing_Type()
)
pnniNodeExtnLoadBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeExtnLoadBalancing.setStatus("current")


class _PnniNodeExtnAdvertisedPglPriority_Type(Integer32):
    """Custom type pnniNodeExtnAdvertisedPglPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PnniNodeExtnAdvertisedPglPriority_Type.__name__ = "Integer32"
_PnniNodeExtnAdvertisedPglPriority_Object = MibTableColumn
pnniNodeExtnAdvertisedPglPriority = _PnniNodeExtnAdvertisedPglPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 3, 1, 6),
    _PnniNodeExtnAdvertisedPglPriority_Type()
)
pnniNodeExtnAdvertisedPglPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeExtnAdvertisedPglPriority.setStatus("current")
_PnniNodeExtnPcCongestionRange_Type = Integer32
_PnniNodeExtnPcCongestionRange_Object = MibTableColumn
pnniNodeExtnPcCongestionRange = _PnniNodeExtnPcCongestionRange_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 3, 1, 7),
    _PnniNodeExtnPcCongestionRange_Type()
)
pnniNodeExtnPcCongestionRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniNodeExtnPcCongestionRange.setStatus("current")
_PnniMapRaigTable_Object = MibTable
pnniMapRaigTable = _PnniMapRaigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    pnniMapRaigTable.setStatus("current")
_PnniMapRaigEntry_Object = MibTableRow
pnniMapRaigEntry = _PnniMapRaigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1)
)
pnniMapRaigEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniMapOriginatingNodeId"),
    (0, "PNNI-MIB", "pnniMapOriginatingPortId"),
    (0, "PNNI-MIB", "pnniMapIndex"),
    (0, "Fore-PNNI-MIB", "pnniMapRaigIndex"),
)
if mibBuilder.loadTexts:
    pnniMapRaigEntry.setStatus("current")


class _PnniMapRaigIndex_Type(Integer32):
    """Custom type pnniMapRaigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_PnniMapRaigIndex_Type.__name__ = "Integer32"
_PnniMapRaigIndex_Object = MibTableColumn
pnniMapRaigIndex = _PnniMapRaigIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1, 1),
    _PnniMapRaigIndex_Type()
)
pnniMapRaigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapRaigIndex.setStatus("current")


class _PnniMapRaigDirection_Type(Integer32):
    """Custom type pnniMapRaigDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 2),
          ("outgoing", 1))
    )


_PnniMapRaigDirection_Type.__name__ = "Integer32"
_PnniMapRaigDirection_Object = MibTableColumn
pnniMapRaigDirection = _PnniMapRaigDirection_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1, 2),
    _PnniMapRaigDirection_Type()
)
pnniMapRaigDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRaigDirection.setStatus("current")
_PnniMapRaigFlags_Type = Integer32
_PnniMapRaigFlags_Object = MibTableColumn
pnniMapRaigFlags = _PnniMapRaigFlags_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1, 3),
    _PnniMapRaigFlags_Type()
)
pnniMapRaigFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRaigFlags.setStatus("current")
_PnniMapRaigAdminWt_Type = Unsigned32
_PnniMapRaigAdminWt_Object = MibTableColumn
pnniMapRaigAdminWt = _PnniMapRaigAdminWt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1, 4),
    _PnniMapRaigAdminWt_Type()
)
pnniMapRaigAdminWt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRaigAdminWt.setStatus("current")
_PnniMapRaigMaximumCellRate_Type = Unsigned32
_PnniMapRaigMaximumCellRate_Object = MibTableColumn
pnniMapRaigMaximumCellRate = _PnniMapRaigMaximumCellRate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1, 5),
    _PnniMapRaigMaximumCellRate_Type()
)
pnniMapRaigMaximumCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRaigMaximumCellRate.setStatus("current")
_PnniMapRaigAvailableCellRate_Type = Unsigned32
_PnniMapRaigAvailableCellRate_Object = MibTableColumn
pnniMapRaigAvailableCellRate = _PnniMapRaigAvailableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1, 6),
    _PnniMapRaigAvailableCellRate_Type()
)
pnniMapRaigAvailableCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRaigAvailableCellRate.setStatus("current")
_PnniMapRaigCellTransferDelay_Type = Unsigned32
_PnniMapRaigCellTransferDelay_Object = MibTableColumn
pnniMapRaigCellTransferDelay = _PnniMapRaigCellTransferDelay_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1, 7),
    _PnniMapRaigCellTransferDelay_Type()
)
pnniMapRaigCellTransferDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRaigCellTransferDelay.setStatus("current")
_PnniMapRaigCellDelayVariation_Type = Unsigned32
_PnniMapRaigCellDelayVariation_Object = MibTableColumn
pnniMapRaigCellDelayVariation = _PnniMapRaigCellDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1, 8),
    _PnniMapRaigCellDelayVariation_Type()
)
pnniMapRaigCellDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRaigCellDelayVariation.setStatus("current")
_PnniMapRaigCellLossRatio_Type = Integer32
_PnniMapRaigCellLossRatio_Object = MibTableColumn
pnniMapRaigCellLossRatio = _PnniMapRaigCellLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1, 9),
    _PnniMapRaigCellLossRatio_Type()
)
pnniMapRaigCellLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRaigCellLossRatio.setStatus("current")
_PnniMapRaigCellLossRatio1_Type = Integer32
_PnniMapRaigCellLossRatio1_Object = MibTableColumn
pnniMapRaigCellLossRatio1 = _PnniMapRaigCellLossRatio1_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1, 10),
    _PnniMapRaigCellLossRatio1_Type()
)
pnniMapRaigCellLossRatio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRaigCellLossRatio1.setStatus("current")
_PnniMapRaigCellRateMargin_Type = Integer32
_PnniMapRaigCellRateMargin_Object = MibTableColumn
pnniMapRaigCellRateMargin = _PnniMapRaigCellRateMargin_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1, 11),
    _PnniMapRaigCellRateMargin_Type()
)
pnniMapRaigCellRateMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRaigCellRateMargin.setStatus("current")
_PnniMapRaigVarianceFactor_Type = Integer32
_PnniMapRaigVarianceFactor_Object = MibTableColumn
pnniMapRaigVarianceFactor = _PnniMapRaigVarianceFactor_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 4, 1, 12),
    _PnniMapRaigVarianceFactor_Type()
)
pnniMapRaigVarianceFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRaigVarianceFactor.setStatus("current")
_PnniMapAddrRaigTable_Object = MibTable
pnniMapAddrRaigTable = _PnniMapAddrRaigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    pnniMapAddrRaigTable.setStatus("current")
_PnniMapAddrRaigEntry_Object = MibTableRow
pnniMapAddrRaigEntry = _PnniMapAddrRaigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1)
)
pnniMapAddrRaigEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniMapAddrAdvertisingNodeId"),
    (0, "PNNI-MIB", "pnniMapAddrAdvertisedPortId"),
    (0, "PNNI-MIB", "pnniMapAddrIndex"),
    (0, "Fore-PNNI-MIB", "pnniMapAddrRaigIndex"),
)
if mibBuilder.loadTexts:
    pnniMapAddrRaigEntry.setStatus("current")


class _PnniMapAddrRaigIndex_Type(Integer32):
    """Custom type pnniMapAddrRaigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_PnniMapAddrRaigIndex_Type.__name__ = "Integer32"
_PnniMapAddrRaigIndex_Object = MibTableColumn
pnniMapAddrRaigIndex = _PnniMapAddrRaigIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1, 1),
    _PnniMapAddrRaigIndex_Type()
)
pnniMapAddrRaigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapAddrRaigIndex.setStatus("current")


class _PnniMapAddrRaigDirection_Type(Integer32):
    """Custom type pnniMapAddrRaigDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 2),
          ("outgoing", 1))
    )


_PnniMapAddrRaigDirection_Type.__name__ = "Integer32"
_PnniMapAddrRaigDirection_Object = MibTableColumn
pnniMapAddrRaigDirection = _PnniMapAddrRaigDirection_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1, 2),
    _PnniMapAddrRaigDirection_Type()
)
pnniMapAddrRaigDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrRaigDirection.setStatus("current")
_PnniMapAddrRaigFlags_Type = Integer32
_PnniMapAddrRaigFlags_Object = MibTableColumn
pnniMapAddrRaigFlags = _PnniMapAddrRaigFlags_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1, 3),
    _PnniMapAddrRaigFlags_Type()
)
pnniMapAddrRaigFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrRaigFlags.setStatus("current")
_PnniMapAddrRaigAdminWt_Type = Unsigned32
_PnniMapAddrRaigAdminWt_Object = MibTableColumn
pnniMapAddrRaigAdminWt = _PnniMapAddrRaigAdminWt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1, 4),
    _PnniMapAddrRaigAdminWt_Type()
)
pnniMapAddrRaigAdminWt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrRaigAdminWt.setStatus("current")
_PnniMapAddrRaigMaximumCellRate_Type = Unsigned32
_PnniMapAddrRaigMaximumCellRate_Object = MibTableColumn
pnniMapAddrRaigMaximumCellRate = _PnniMapAddrRaigMaximumCellRate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1, 5),
    _PnniMapAddrRaigMaximumCellRate_Type()
)
pnniMapAddrRaigMaximumCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrRaigMaximumCellRate.setStatus("current")
_PnniMapAddrRaigAvailableCellRate_Type = Unsigned32
_PnniMapAddrRaigAvailableCellRate_Object = MibTableColumn
pnniMapAddrRaigAvailableCellRate = _PnniMapAddrRaigAvailableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1, 6),
    _PnniMapAddrRaigAvailableCellRate_Type()
)
pnniMapAddrRaigAvailableCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrRaigAvailableCellRate.setStatus("current")
_PnniMapAddrRaigCellTransferDelay_Type = Unsigned32
_PnniMapAddrRaigCellTransferDelay_Object = MibTableColumn
pnniMapAddrRaigCellTransferDelay = _PnniMapAddrRaigCellTransferDelay_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1, 7),
    _PnniMapAddrRaigCellTransferDelay_Type()
)
pnniMapAddrRaigCellTransferDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrRaigCellTransferDelay.setStatus("current")
_PnniMapAddrRaigCellDelayVariation_Type = Unsigned32
_PnniMapAddrRaigCellDelayVariation_Object = MibTableColumn
pnniMapAddrRaigCellDelayVariation = _PnniMapAddrRaigCellDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1, 8),
    _PnniMapAddrRaigCellDelayVariation_Type()
)
pnniMapAddrRaigCellDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrRaigCellDelayVariation.setStatus("current")
_PnniMapAddrRaigCellLossRatio_Type = Integer32
_PnniMapAddrRaigCellLossRatio_Object = MibTableColumn
pnniMapAddrRaigCellLossRatio = _PnniMapAddrRaigCellLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1, 9),
    _PnniMapAddrRaigCellLossRatio_Type()
)
pnniMapAddrRaigCellLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrRaigCellLossRatio.setStatus("current")
_PnniMapAddrRaigCellLossRatio1_Type = Integer32
_PnniMapAddrRaigCellLossRatio1_Object = MibTableColumn
pnniMapAddrRaigCellLossRatio1 = _PnniMapAddrRaigCellLossRatio1_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1, 10),
    _PnniMapAddrRaigCellLossRatio1_Type()
)
pnniMapAddrRaigCellLossRatio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrRaigCellLossRatio1.setStatus("current")
_PnniMapAddrRaigCellRateMargin_Type = Integer32
_PnniMapAddrRaigCellRateMargin_Object = MibTableColumn
pnniMapAddrRaigCellRateMargin = _PnniMapAddrRaigCellRateMargin_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1, 11),
    _PnniMapAddrRaigCellRateMargin_Type()
)
pnniMapAddrRaigCellRateMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrRaigCellRateMargin.setStatus("current")
_PnniMapAddrRaigVarianceFactor_Type = Integer32
_PnniMapAddrRaigVarianceFactor_Object = MibTableColumn
pnniMapAddrRaigVarianceFactor = _PnniMapAddrRaigVarianceFactor_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 5, 1, 12),
    _PnniMapAddrRaigVarianceFactor_Type()
)
pnniMapAddrRaigVarianceFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrRaigVarianceFactor.setStatus("current")
_PnniPcProfileMapTable_Object = MibTable
pnniPcProfileMapTable = _PnniPcProfileMapTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6)
)
if mibBuilder.loadTexts:
    pnniPcProfileMapTable.setStatus("current")
_PnniPcProfileMapEntry_Object = MibTableRow
pnniPcProfileMapEntry = _PnniPcProfileMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1)
)
pnniPcProfileMapEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "Fore-PNNI-MIB", "pnniPcProfileIndex"),
    (0, "Fore-PNNI-MIB", "pnniPcProfileMapOptIndex"),
    (0, "Fore-PNNI-MIB", "pnniPcProfileMapNodeId"),
)
if mibBuilder.loadTexts:
    pnniPcProfileMapEntry.setStatus("current")
_PnniPcProfileMapOptIndex_Type = Integer32
_PnniPcProfileMapOptIndex_Object = MibTableColumn
pnniPcProfileMapOptIndex = _PnniPcProfileMapOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 1),
    _PnniPcProfileMapOptIndex_Type()
)
pnniPcProfileMapOptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniPcProfileMapOptIndex.setStatus("current")
_PnniPcProfileMapNodeId_Type = PnniNodeId
_PnniPcProfileMapNodeId_Object = MibTableColumn
pnniPcProfileMapNodeId = _PnniPcProfileMapNodeId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 2),
    _PnniPcProfileMapNodeId_Type()
)
pnniPcProfileMapNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniPcProfileMapNodeId.setStatus("current")
_PnniPcProfileMapLocalPort_Type = PnniPortId
_PnniPcProfileMapLocalPort_Object = MibTableColumn
pnniPcProfileMapLocalPort = _PnniPcProfileMapLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 3),
    _PnniPcProfileMapLocalPort_Type()
)
pnniPcProfileMapLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileMapLocalPort.setStatus("current")
_PnniPcProfileMapParentNode_Type = PnniNodeId
_PnniPcProfileMapParentNode_Object = MibTableColumn
pnniPcProfileMapParentNode = _PnniPcProfileMapParentNode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 4),
    _PnniPcProfileMapParentNode_Type()
)
pnniPcProfileMapParentNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileMapParentNode.setStatus("current")
_PnniPcProfileMapAdminWt_Type = Unsigned32
_PnniPcProfileMapAdminWt_Object = MibTableColumn
pnniPcProfileMapAdminWt = _PnniPcProfileMapAdminWt_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 5),
    _PnniPcProfileMapAdminWt_Type()
)
pnniPcProfileMapAdminWt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileMapAdminWt.setStatus("current")
_PnniPcProfileMapMaximumCellRate_Type = Unsigned32
_PnniPcProfileMapMaximumCellRate_Object = MibTableColumn
pnniPcProfileMapMaximumCellRate = _PnniPcProfileMapMaximumCellRate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 6),
    _PnniPcProfileMapMaximumCellRate_Type()
)
pnniPcProfileMapMaximumCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileMapMaximumCellRate.setStatus("current")
_PnniPcProfileMapAvailableCellRate_Type = Unsigned32
_PnniPcProfileMapAvailableCellRate_Object = MibTableColumn
pnniPcProfileMapAvailableCellRate = _PnniPcProfileMapAvailableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 7),
    _PnniPcProfileMapAvailableCellRate_Type()
)
pnniPcProfileMapAvailableCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileMapAvailableCellRate.setStatus("current")
_PnniPcProfileMapCellTransferDelay_Type = Unsigned32
_PnniPcProfileMapCellTransferDelay_Object = MibTableColumn
pnniPcProfileMapCellTransferDelay = _PnniPcProfileMapCellTransferDelay_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 8),
    _PnniPcProfileMapCellTransferDelay_Type()
)
pnniPcProfileMapCellTransferDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileMapCellTransferDelay.setStatus("current")
_PnniPcProfileMapCellDelayVariation_Type = Unsigned32
_PnniPcProfileMapCellDelayVariation_Object = MibTableColumn
pnniPcProfileMapCellDelayVariation = _PnniPcProfileMapCellDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 9),
    _PnniPcProfileMapCellDelayVariation_Type()
)
pnniPcProfileMapCellDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileMapCellDelayVariation.setStatus("current")
_PnniPcProfileMapCellLossRatio_Type = Integer32
_PnniPcProfileMapCellLossRatio_Object = MibTableColumn
pnniPcProfileMapCellLossRatio = _PnniPcProfileMapCellLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 10),
    _PnniPcProfileMapCellLossRatio_Type()
)
pnniPcProfileMapCellLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileMapCellLossRatio.setStatus("current")
_PnniPcProfileMapCellLossRatio1_Type = Integer32
_PnniPcProfileMapCellLossRatio1_Object = MibTableColumn
pnniPcProfileMapCellLossRatio1 = _PnniPcProfileMapCellLossRatio1_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 11),
    _PnniPcProfileMapCellLossRatio1_Type()
)
pnniPcProfileMapCellLossRatio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileMapCellLossRatio1.setStatus("current")
_PnniPcProfileMapCellRateMargin_Type = Integer32
_PnniPcProfileMapCellRateMargin_Object = MibTableColumn
pnniPcProfileMapCellRateMargin = _PnniPcProfileMapCellRateMargin_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 12),
    _PnniPcProfileMapCellRateMargin_Type()
)
pnniPcProfileMapCellRateMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileMapCellRateMargin.setStatus("current")
_PnniPcProfileMapVarianceFactor_Type = Integer32
_PnniPcProfileMapVarianceFactor_Object = MibTableColumn
pnniPcProfileMapVarianceFactor = _PnniPcProfileMapVarianceFactor_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 6, 1, 13),
    _PnniPcProfileMapVarianceFactor_Type()
)
pnniPcProfileMapVarianceFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileMapVarianceFactor.setStatus("current")
_PnniSpanningTreeMapTable_Object = MibTable
pnniSpanningTreeMapTable = _PnniSpanningTreeMapTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 7)
)
if mibBuilder.loadTexts:
    pnniSpanningTreeMapTable.setStatus("current")
_PnniSpanningTreeMapEntry_Object = MibTableRow
pnniSpanningTreeMapEntry = _PnniSpanningTreeMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 7, 1)
)
pnniSpanningTreeMapEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "Fore-PNNI-MIB", "pnniSpanningTreeMapNodeId"),
)
if mibBuilder.loadTexts:
    pnniSpanningTreeMapEntry.setStatus("current")
_PnniSpanningTreeMapNodeId_Type = PnniNodeId
_PnniSpanningTreeMapNodeId_Object = MibTableColumn
pnniSpanningTreeMapNodeId = _PnniSpanningTreeMapNodeId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 7, 1, 1),
    _PnniSpanningTreeMapNodeId_Type()
)
pnniSpanningTreeMapNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniSpanningTreeMapNodeId.setStatus("current")


class _PnniSpanningTreeMapStatus_Type(Integer32):
    """Custom type pnniSpanningTreeMapStatus based on Integer32"""
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
        *(("linkadded", 2),
          ("linkdeleted", 3),
          ("pglchanged", 5),
          ("treeclean", 4),
          ("uptodate", 1))
    )


_PnniSpanningTreeMapStatus_Type.__name__ = "Integer32"
_PnniSpanningTreeMapStatus_Object = MibTableColumn
pnniSpanningTreeMapStatus = _PnniSpanningTreeMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 7, 1, 2),
    _PnniSpanningTreeMapStatus_Type()
)
pnniSpanningTreeMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpanningTreeMapStatus.setStatus("current")
_PnniSpanningTreeMapParentNode_Type = PnniNodeId
_PnniSpanningTreeMapParentNode_Object = MibTableColumn
pnniSpanningTreeMapParentNode = _PnniSpanningTreeMapParentNode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 7, 1, 3),
    _PnniSpanningTreeMapParentNode_Type()
)
pnniSpanningTreeMapParentNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpanningTreeMapParentNode.setStatus("current")
_PnniSpanningTreeMapPort_Type = PnniPortId
_PnniSpanningTreeMapPort_Object = MibTableColumn
pnniSpanningTreeMapPort = _PnniSpanningTreeMapPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 7, 1, 4),
    _PnniSpanningTreeMapPort_Type()
)
pnniSpanningTreeMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpanningTreeMapPort.setStatus("current")


class _PnniSpanningTreeMapLinkType_Type(Integer32):
    """Custom type pnniSpanningTreeMapLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hlink", 1),
          ("uplink", 2))
    )


_PnniSpanningTreeMapLinkType_Type.__name__ = "Integer32"
_PnniSpanningTreeMapLinkType_Object = MibTableColumn
pnniSpanningTreeMapLinkType = _PnniSpanningTreeMapLinkType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 7, 1, 5),
    _PnniSpanningTreeMapLinkType_Type()
)
pnniSpanningTreeMapLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSpanningTreeMapLinkType.setStatus("current")
_PnniNodeScStatsTable_Object = MibTable
pnniNodeScStatsTable = _PnniNodeScStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 8)
)
if mibBuilder.loadTexts:
    pnniNodeScStatsTable.setStatus("current")
_PnniNodeScStatsEntry_Object = MibTableRow
pnniNodeScStatsEntry = _PnniNodeScStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 8, 1)
)
pnniNodeScStatsEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
)
if mibBuilder.loadTexts:
    pnniNodeScStatsEntry.setStatus("current")
_PnniNodeScStatsNrOfEvents_Type = Unsigned32
_PnniNodeScStatsNrOfEvents_Object = MibTableColumn
pnniNodeScStatsNrOfEvents = _PnniNodeScStatsNrOfEvents_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 8, 1, 2),
    _PnniNodeScStatsNrOfEvents_Type()
)
pnniNodeScStatsNrOfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeScStatsNrOfEvents.setStatus("current")
_PnniNodeScStatsNrOfPurges_Type = Unsigned32
_PnniNodeScStatsNrOfPurges_Object = MibTableColumn
pnniNodeScStatsNrOfPurges = _PnniNodeScStatsNrOfPurges_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 8, 1, 3),
    _PnniNodeScStatsNrOfPurges_Type()
)
pnniNodeScStatsNrOfPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeScStatsNrOfPurges.setStatus("current")
_PnniNodeScStatsNrOfTimeoutPurges_Type = Unsigned32
_PnniNodeScStatsNrOfTimeoutPurges_Object = MibTableColumn
pnniNodeScStatsNrOfTimeoutPurges = _PnniNodeScStatsNrOfTimeoutPurges_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 8, 1, 4),
    _PnniNodeScStatsNrOfTimeoutPurges_Type()
)
pnniNodeScStatsNrOfTimeoutPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeScStatsNrOfTimeoutPurges.setStatus("current")
_PnniNodeScStatsNrOfPacketsDropped_Type = Unsigned32
_PnniNodeScStatsNrOfPacketsDropped_Object = MibTableColumn
pnniNodeScStatsNrOfPacketsDropped = _PnniNodeScStatsNrOfPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 8, 1, 5),
    _PnniNodeScStatsNrOfPacketsDropped_Type()
)
pnniNodeScStatsNrOfPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeScStatsNrOfPacketsDropped.setStatus("current")
_PnniNodeScStatsNrOfHiPriPktsDropped_Type = Unsigned32
_PnniNodeScStatsNrOfHiPriPktsDropped_Object = MibTableColumn
pnniNodeScStatsNrOfHiPriPktsDropped = _PnniNodeScStatsNrOfHiPriPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 8, 1, 6),
    _PnniNodeScStatsNrOfHiPriPktsDropped_Type()
)
pnniNodeScStatsNrOfHiPriPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeScStatsNrOfHiPriPktsDropped.setStatus("current")
_PnniNodeScStatsNrOfLowPriPktsDropped_Type = Unsigned32
_PnniNodeScStatsNrOfLowPriPktsDropped_Object = MibTableColumn
pnniNodeScStatsNrOfLowPriPktsDropped = _PnniNodeScStatsNrOfLowPriPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 8, 1, 7),
    _PnniNodeScStatsNrOfLowPriPktsDropped_Type()
)
pnniNodeScStatsNrOfLowPriPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeScStatsNrOfLowPriPktsDropped.setStatus("current")
_PnniNodeScStatsNrOfNodalInfoEvents_Type = Unsigned32
_PnniNodeScStatsNrOfNodalInfoEvents_Object = MibTableColumn
pnniNodeScStatsNrOfNodalInfoEvents = _PnniNodeScStatsNrOfNodalInfoEvents_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 8, 1, 8),
    _PnniNodeScStatsNrOfNodalInfoEvents_Type()
)
pnniNodeScStatsNrOfNodalInfoEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeScStatsNrOfNodalInfoEvents.setStatus("current")
_PnniNodeScStatsNrOfHorizLinkEvents_Type = Unsigned32
_PnniNodeScStatsNrOfHorizLinkEvents_Object = MibTableColumn
pnniNodeScStatsNrOfHorizLinkEvents = _PnniNodeScStatsNrOfHorizLinkEvents_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 8, 1, 9),
    _PnniNodeScStatsNrOfHorizLinkEvents_Type()
)
pnniNodeScStatsNrOfHorizLinkEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeScStatsNrOfHorizLinkEvents.setStatus("current")
_PnniNodeScStatsNrOfUpLinkEvents_Type = Unsigned32
_PnniNodeScStatsNrOfUpLinkEvents_Object = MibTableColumn
pnniNodeScStatsNrOfUpLinkEvents = _PnniNodeScStatsNrOfUpLinkEvents_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 8, 1, 10),
    _PnniNodeScStatsNrOfUpLinkEvents_Type()
)
pnniNodeScStatsNrOfUpLinkEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeScStatsNrOfUpLinkEvents.setStatus("current")
_PnniNodeScStatsNrOfNodalStateEvents_Type = Unsigned32
_PnniNodeScStatsNrOfNodalStateEvents_Object = MibTableColumn
pnniNodeScStatsNrOfNodalStateEvents = _PnniNodeScStatsNrOfNodalStateEvents_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 8, 1, 11),
    _PnniNodeScStatsNrOfNodalStateEvents_Type()
)
pnniNodeScStatsNrOfNodalStateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeScStatsNrOfNodalStateEvents.setStatus("current")
_PnniCrankbackGroup_ObjectIdentity = ObjectIdentity
pnniCrankbackGroup = _PnniCrankbackGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 9)
)
_PnniMaxCrankbackTries_Type = Integer32
_PnniMaxCrankbackTries_Object = MibScalar
pnniMaxCrankbackTries = _PnniMaxCrankbackTries_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 9, 1),
    _PnniMaxCrankbackTries_Type()
)
pnniMaxCrankbackTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMaxCrankbackTries.setStatus("current")
_PnniPcProfileAvoidLinkTable_Object = MibTable
pnniPcProfileAvoidLinkTable = _PnniPcProfileAvoidLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 10)
)
if mibBuilder.loadTexts:
    pnniPcProfileAvoidLinkTable.setStatus("current")
_PnniPcProfileAvoidLinkEntry_Object = MibTableRow
pnniPcProfileAvoidLinkEntry = _PnniPcProfileAvoidLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 10, 1)
)
pnniPcProfileAvoidLinkEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "Fore-PNNI-MIB", "pnniPcProfileIndex"),
    (0, "Fore-PNNI-MIB", "pnniPcProfileAvoidLinkIndex"),
)
if mibBuilder.loadTexts:
    pnniPcProfileAvoidLinkEntry.setStatus("current")
_PnniPcProfileAvoidLinkIndex_Type = Integer32
_PnniPcProfileAvoidLinkIndex_Object = MibTableColumn
pnniPcProfileAvoidLinkIndex = _PnniPcProfileAvoidLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 10, 1, 1),
    _PnniPcProfileAvoidLinkIndex_Type()
)
pnniPcProfileAvoidLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniPcProfileAvoidLinkIndex.setStatus("current")
_PnniPcProfileAvoidLinkNodeId_Type = PnniNodeId
_PnniPcProfileAvoidLinkNodeId_Object = MibTableColumn
pnniPcProfileAvoidLinkNodeId = _PnniPcProfileAvoidLinkNodeId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 10, 1, 2),
    _PnniPcProfileAvoidLinkNodeId_Type()
)
pnniPcProfileAvoidLinkNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileAvoidLinkNodeId.setStatus("current")
_PnniPcProfileAvoidLinkPortId_Type = PnniPortId
_PnniPcProfileAvoidLinkPortId_Object = MibTableColumn
pnniPcProfileAvoidLinkPortId = _PnniPcProfileAvoidLinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 10, 1, 3),
    _PnniPcProfileAvoidLinkPortId_Type()
)
pnniPcProfileAvoidLinkPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileAvoidLinkPortId.setStatus("current")


class _PnniPcProfileAvoidLinkType_Type(Integer32):
    """Custom type pnniPcProfileAvoidLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalLink", 1),
          ("reverseLink", 2))
    )


_PnniPcProfileAvoidLinkType_Type.__name__ = "Integer32"
_PnniPcProfileAvoidLinkType_Object = MibTableColumn
pnniPcProfileAvoidLinkType = _PnniPcProfileAvoidLinkType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 10, 1, 4),
    _PnniPcProfileAvoidLinkType_Type()
)
pnniPcProfileAvoidLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileAvoidLinkType.setStatus("current")
_PnniPcProfileAvoidLinkRemoteNodeId_Type = PnniNodeId
_PnniPcProfileAvoidLinkRemoteNodeId_Object = MibTableColumn
pnniPcProfileAvoidLinkRemoteNodeId = _PnniPcProfileAvoidLinkRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 10, 1, 5),
    _PnniPcProfileAvoidLinkRemoteNodeId_Type()
)
pnniPcProfileAvoidLinkRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfileAvoidLinkRemoteNodeId.setStatus("current")
_PnniPcProfilePreferLinkTable_Object = MibTable
pnniPcProfilePreferLinkTable = _PnniPcProfilePreferLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 11)
)
if mibBuilder.loadTexts:
    pnniPcProfilePreferLinkTable.setStatus("current")
_PnniPcProfilePreferLinkEntry_Object = MibTableRow
pnniPcProfilePreferLinkEntry = _PnniPcProfilePreferLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 11, 1)
)
pnniPcProfilePreferLinkEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "Fore-PNNI-MIB", "pnniPcProfileIndex"),
    (0, "Fore-PNNI-MIB", "pnniPcProfilePreferLinkIndex"),
)
if mibBuilder.loadTexts:
    pnniPcProfilePreferLinkEntry.setStatus("current")
_PnniPcProfilePreferLinkIndex_Type = Integer32
_PnniPcProfilePreferLinkIndex_Object = MibTableColumn
pnniPcProfilePreferLinkIndex = _PnniPcProfilePreferLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 11, 1, 1),
    _PnniPcProfilePreferLinkIndex_Type()
)
pnniPcProfilePreferLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniPcProfilePreferLinkIndex.setStatus("current")
_PnniPcProfilePreferLinkNodeId_Type = PnniNodeId
_PnniPcProfilePreferLinkNodeId_Object = MibTableColumn
pnniPcProfilePreferLinkNodeId = _PnniPcProfilePreferLinkNodeId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 11, 1, 2),
    _PnniPcProfilePreferLinkNodeId_Type()
)
pnniPcProfilePreferLinkNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfilePreferLinkNodeId.setStatus("current")
_PnniPcProfilePreferLinkPortId_Type = PnniPortId
_PnniPcProfilePreferLinkPortId_Object = MibTableColumn
pnniPcProfilePreferLinkPortId = _PnniPcProfilePreferLinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 11, 1, 3),
    _PnniPcProfilePreferLinkPortId_Type()
)
pnniPcProfilePreferLinkPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfilePreferLinkPortId.setStatus("current")


class _PnniPcProfilePreferLinkType_Type(Integer32):
    """Custom type pnniPcProfilePreferLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalLink", 1),
          ("reverseLink", 2))
    )


_PnniPcProfilePreferLinkType_Type.__name__ = "Integer32"
_PnniPcProfilePreferLinkType_Object = MibTableColumn
pnniPcProfilePreferLinkType = _PnniPcProfilePreferLinkType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 11, 1, 4),
    _PnniPcProfilePreferLinkType_Type()
)
pnniPcProfilePreferLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfilePreferLinkType.setStatus("current")
_PnniPcProfilePreferLinkRemoteNodeId_Type = PnniNodeId
_PnniPcProfilePreferLinkRemoteNodeId_Object = MibTableColumn
pnniPcProfilePreferLinkRemoteNodeId = _PnniPcProfilePreferLinkRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 11, 1, 5),
    _PnniPcProfilePreferLinkRemoteNodeId_Type()
)
pnniPcProfilePreferLinkRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPcProfilePreferLinkRemoteNodeId.setStatus("current")
_PnniParametersGroup_ObjectIdentity = ObjectIdentity
pnniParametersGroup = _PnniParametersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 12)
)


class _PnniMaxDtlSize_Type(Integer32):
    """Custom type pnniMaxDtlSize based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_PnniMaxDtlSize_Type.__name__ = "Integer32"
_PnniMaxDtlSize_Object = MibScalar
pnniMaxDtlSize = _PnniMaxDtlSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 12, 1),
    _PnniMaxDtlSize_Type()
)
pnniMaxDtlSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMaxDtlSize.setStatus("current")
_PnniLoadBalancedUbrEnable_Type = Integer32
_PnniLoadBalancedUbrEnable_Object = MibScalar
pnniLoadBalancedUbrEnable = _PnniLoadBalancedUbrEnable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 12, 2),
    _PnniLoadBalancedUbrEnable_Type()
)
pnniLoadBalancedUbrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniLoadBalancedUbrEnable.setStatus("current")
_ForePnniDTLTable_Object = MibTable
forePnniDTLTable = _ForePnniDTLTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 13)
)
if mibBuilder.loadTexts:
    forePnniDTLTable.setStatus("current")
_ForePnniDTLEntry_Object = MibTableRow
forePnniDTLEntry = _ForePnniDTLEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 13, 1)
)
forePnniDTLEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniDTLIndex"),
)
if mibBuilder.loadTexts:
    forePnniDTLEntry.setStatus("current")


class _ForePnniDTLName_Type(DisplayString):
    """Custom type forePnniDTLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ForePnniDTLName_Type.__name__ = "DisplayString"
_ForePnniDTLName_Object = MibTableColumn
forePnniDTLName = _ForePnniDTLName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 13, 1, 1),
    _ForePnniDTLName_Type()
)
forePnniDTLName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forePnniDTLName.setStatus("current")


class _ForePnniDTLValidity_Type(DisplayString):
    """Custom type forePnniDTLValidity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ForePnniDTLValidity_Type.__name__ = "DisplayString"
_ForePnniDTLValidity_Object = MibTableColumn
forePnniDTLValidity = _ForePnniDTLValidity_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 13, 1, 2),
    _ForePnniDTLValidity_Type()
)
forePnniDTLValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePnniDTLValidity.setStatus("current")
_PnniDtlComputationTable_Object = MibTable
pnniDtlComputationTable = _PnniDtlComputationTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 14)
)
if mibBuilder.loadTexts:
    pnniDtlComputationTable.setStatus("current")
_PnniDtlComputationEntry_Object = MibTableRow
pnniDtlComputationEntry = _PnniDtlComputationEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 14, 1)
)
pnniDtlComputationEntry.setIndexNames(
    (0, "Fore-PNNI-MIB", "pnniDtlComputationNodeIndex"),
    (0, "Fore-PNNI-MIB", "pnniDtlComputationDtlIndex"),
)
if mibBuilder.loadTexts:
    pnniDtlComputationEntry.setStatus("current")
_PnniDtlComputationNodeIndex_Type = PnniNodeIndex
_PnniDtlComputationNodeIndex_Object = MibTableColumn
pnniDtlComputationNodeIndex = _PnniDtlComputationNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 14, 1, 1),
    _PnniDtlComputationNodeIndex_Type()
)
pnniDtlComputationNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniDtlComputationNodeIndex.setStatus("current")
_PnniDtlComputationDtlIndex_Type = Integer32
_PnniDtlComputationDtlIndex_Object = MibTableColumn
pnniDtlComputationDtlIndex = _PnniDtlComputationDtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 14, 1, 2),
    _PnniDtlComputationDtlIndex_Type()
)
pnniDtlComputationDtlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniDtlComputationDtlIndex.setStatus("current")
_PnniDtlComputationDestNsapAddress_Type = NsapAddr
_PnniDtlComputationDestNsapAddress_Object = MibTableColumn
pnniDtlComputationDestNsapAddress = _PnniDtlComputationDestNsapAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 14, 1, 3),
    _PnniDtlComputationDestNsapAddress_Type()
)
pnniDtlComputationDestNsapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniDtlComputationDestNsapAddress.setStatus("current")
_PnniDtlComputationCompute_Type = Integer32
_PnniDtlComputationCompute_Object = MibTableColumn
pnniDtlComputationCompute = _PnniDtlComputationCompute_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 14, 1, 4),
    _PnniDtlComputationCompute_Type()
)
pnniDtlComputationCompute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniDtlComputationCompute.setStatus("current")
_PnniDtlListTable_Object = MibTable
pnniDtlListTable = _PnniDtlListTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 15)
)
if mibBuilder.loadTexts:
    pnniDtlListTable.setStatus("current")
_PnniDtlListEntry_Object = MibTableRow
pnniDtlListEntry = _PnniDtlListEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 15, 1)
)
pnniDtlListEntry.setIndexNames(
    (0, "Fore-PNNI-MIB", "pnniDtlListTag"),
    (0, "Fore-PNNI-MIB", "pnniDtlListNodeIndex"),
    (0, "Fore-PNNI-MIB", "pnniDtlListDtlIndex"),
)
if mibBuilder.loadTexts:
    pnniDtlListEntry.setStatus("current")


class _PnniDtlListTag_Type(Integer32):
    """Custom type pnniDtlListTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnniDtlListTag_Type.__name__ = "Integer32"
_PnniDtlListTag_Object = MibTableColumn
pnniDtlListTag = _PnniDtlListTag_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 15, 1, 1),
    _PnniDtlListTag_Type()
)
pnniDtlListTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniDtlListTag.setStatus("current")


class _PnniDtlListNodeIndex_Type(Integer32):
    """Custom type pnniDtlListNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnniDtlListNodeIndex_Type.__name__ = "Integer32"
_PnniDtlListNodeIndex_Object = MibTableColumn
pnniDtlListNodeIndex = _PnniDtlListNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 15, 1, 2),
    _PnniDtlListNodeIndex_Type()
)
pnniDtlListNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniDtlListNodeIndex.setStatus("current")


class _PnniDtlListDtlIndex_Type(Integer32):
    """Custom type pnniDtlListDtlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnniDtlListDtlIndex_Type.__name__ = "Integer32"
_PnniDtlListDtlIndex_Object = MibTableColumn
pnniDtlListDtlIndex = _PnniDtlListDtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 15, 1, 3),
    _PnniDtlListDtlIndex_Type()
)
pnniDtlListDtlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniDtlListDtlIndex.setStatus("current")


class _PnniDtlListWeight_Type(Integer32):
    """Custom type pnniDtlListWeight based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnniDtlListWeight_Type.__name__ = "Integer32"
_PnniDtlListWeight_Object = MibTableColumn
pnniDtlListWeight = _PnniDtlListWeight_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 15, 1, 4),
    _PnniDtlListWeight_Type()
)
pnniDtlListWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniDtlListWeight.setStatus("current")
_PnniDtlListStatus_Type = RowStatus
_PnniDtlListStatus_Object = MibTableColumn
pnniDtlListStatus = _PnniDtlListStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 15, 1, 5),
    _PnniDtlListStatus_Type()
)
pnniDtlListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniDtlListStatus.setStatus("current")
_PnniMapNodeExtTable_Object = MibTable
pnniMapNodeExtTable = _PnniMapNodeExtTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 16)
)
if mibBuilder.loadTexts:
    pnniMapNodeExtTable.setStatus("current")
_PnniMapNodeExtEntry_Object = MibTableRow
pnniMapNodeExtEntry = _PnniMapNodeExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 16, 1)
)
pnniMapNodeExtEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "Fore-PNNI-MIB", "pnniMapNodeExtRemoteNodeId"),
)
if mibBuilder.loadTexts:
    pnniMapNodeExtEntry.setStatus("current")
_PnniMapNodeExtRemoteNodeId_Type = PnniNodeId
_PnniMapNodeExtRemoteNodeId_Object = MibTableColumn
pnniMapNodeExtRemoteNodeId = _PnniMapNodeExtRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 16, 1, 1),
    _PnniMapNodeExtRemoteNodeId_Type()
)
pnniMapNodeExtRemoteNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapNodeExtRemoteNodeId.setStatus("current")
_PnniMapNodeExtSoftwareVersion_Type = Unsigned32
_PnniMapNodeExtSoftwareVersion_Object = MibTableColumn
pnniMapNodeExtSoftwareVersion = _PnniMapNodeExtSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 16, 1, 2),
    _PnniMapNodeExtSoftwareVersion_Type()
)
pnniMapNodeExtSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeExtSoftwareVersion.setStatus("current")
_PnniMapNodeExtHardwareVersion_Type = Unsigned32
_PnniMapNodeExtHardwareVersion_Object = MibTableColumn
pnniMapNodeExtHardwareVersion = _PnniMapNodeExtHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 16, 1, 3),
    _PnniMapNodeExtHardwareVersion_Type()
)
pnniMapNodeExtHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeExtHardwareVersion.setStatus("current")
_PnniMapNodeExtHardwareId_Type = Unsigned32
_PnniMapNodeExtHardwareId_Object = MibTableColumn
pnniMapNodeExtHardwareId = _PnniMapNodeExtHardwareId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 16, 1, 4),
    _PnniMapNodeExtHardwareId_Type()
)
pnniMapNodeExtHardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeExtHardwareId.setStatus("current")
_PnniMapNodeExtSwitchName_Type = DisplayString
_PnniMapNodeExtSwitchName_Object = MibTableColumn
pnniMapNodeExtSwitchName = _PnniMapNodeExtSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 16, 1, 5),
    _PnniMapNodeExtSwitchName_Type()
)
pnniMapNodeExtSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeExtSwitchName.setStatus("current")
_PnniMapNodeExtRemoteNodeIndex_Type = Integer32
_PnniMapNodeExtRemoteNodeIndex_Object = MibTableColumn
pnniMapNodeExtRemoteNodeIndex = _PnniMapNodeExtRemoteNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 16, 1, 6),
    _PnniMapNodeExtRemoteNodeIndex_Type()
)
pnniMapNodeExtRemoteNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeExtRemoteNodeIndex.setStatus("current")
_PnniMapNodeExtForeNodalFlags_Type = Unsigned32
_PnniMapNodeExtForeNodalFlags_Object = MibTableColumn
pnniMapNodeExtForeNodalFlags = _PnniMapNodeExtForeNodalFlags_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 16, 1, 7),
    _PnniMapNodeExtForeNodalFlags_Type()
)
pnniMapNodeExtForeNodalFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeExtForeNodalFlags.setStatus("current")
_PnniMapNodeIpAddrTable_Object = MibTable
pnniMapNodeIpAddrTable = _PnniMapNodeIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 17)
)
if mibBuilder.loadTexts:
    pnniMapNodeIpAddrTable.setStatus("current")
_PnniMapNodeIpAddrEntry_Object = MibTableRow
pnniMapNodeIpAddrEntry = _PnniMapNodeIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 17, 1)
)
pnniMapNodeIpAddrEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "Fore-PNNI-MIB", "pnniMapNodeExtRemoteNodeId"),
    (0, "Fore-PNNI-MIB", "pnniMapNodeIpAddr"),
)
if mibBuilder.loadTexts:
    pnniMapNodeIpAddrEntry.setStatus("current")
_PnniMapNodeIpAddr_Type = IpAddress
_PnniMapNodeIpAddr_Object = MibTableColumn
pnniMapNodeIpAddr = _PnniMapNodeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 17, 1, 1),
    _PnniMapNodeIpAddr_Type()
)
pnniMapNodeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeIpAddr.setStatus("current")
_PnniMapNodeIpAddrIfName_Type = InterfaceLabel
_PnniMapNodeIpAddrIfName_Object = MibTableColumn
pnniMapNodeIpAddrIfName = _PnniMapNodeIpAddrIfName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 17, 1, 2),
    _PnniMapNodeIpAddrIfName_Type()
)
pnniMapNodeIpAddrIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeIpAddrIfName.setStatus("current")
_PnniConnTreeMapTable_Object = MibTable
pnniConnTreeMapTable = _PnniConnTreeMapTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 18)
)
if mibBuilder.loadTexts:
    pnniConnTreeMapTable.setStatus("current")
_PnniConnTreeMapEntry_Object = MibTableRow
pnniConnTreeMapEntry = _PnniConnTreeMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 18, 1)
)
pnniConnTreeMapEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "Fore-PNNI-MIB", "pnniConnTreeMapNodeId"),
)
if mibBuilder.loadTexts:
    pnniConnTreeMapEntry.setStatus("current")
_PnniConnTreeMapNodeId_Type = PnniNodeId
_PnniConnTreeMapNodeId_Object = MibTableColumn
pnniConnTreeMapNodeId = _PnniConnTreeMapNodeId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 18, 1, 1),
    _PnniConnTreeMapNodeId_Type()
)
pnniConnTreeMapNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniConnTreeMapNodeId.setStatus("current")


class _PnniConnTreeMapStatus_Type(Integer32):
    """Custom type pnniConnTreeMapStatus based on Integer32"""
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
        *(("linkadded", 2),
          ("linkdeleted", 3),
          ("pglchanged", 5),
          ("treeclean", 4),
          ("uptodate", 1))
    )


_PnniConnTreeMapStatus_Type.__name__ = "Integer32"
_PnniConnTreeMapStatus_Object = MibTableColumn
pnniConnTreeMapStatus = _PnniConnTreeMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 18, 1, 2),
    _PnniConnTreeMapStatus_Type()
)
pnniConnTreeMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniConnTreeMapStatus.setStatus("current")
_PnniConnTreeMapParentNode_Type = PnniNodeId
_PnniConnTreeMapParentNode_Object = MibTableColumn
pnniConnTreeMapParentNode = _PnniConnTreeMapParentNode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 18, 1, 3),
    _PnniConnTreeMapParentNode_Type()
)
pnniConnTreeMapParentNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniConnTreeMapParentNode.setStatus("current")
_PnniConnTreeMapPort_Type = PnniPortId
_PnniConnTreeMapPort_Object = MibTableColumn
pnniConnTreeMapPort = _PnniConnTreeMapPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 18, 1, 4),
    _PnniConnTreeMapPort_Type()
)
pnniConnTreeMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniConnTreeMapPort.setStatus("current")


class _PnniConnTreeMapLinkType_Type(Integer32):
    """Custom type pnniConnTreeMapLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hlink", 1),
          ("uplink", 2))
    )


_PnniConnTreeMapLinkType_Type.__name__ = "Integer32"
_PnniConnTreeMapLinkType_Object = MibTableColumn
pnniConnTreeMapLinkType = _PnniConnTreeMapLinkType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 1, 18, 1, 5),
    _PnniConnTreeMapLinkType_Type()
)
pnniConnTreeMapLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniConnTreeMapLinkType.setStatus("current")
_AtmRoutingGroup_ObjectIdentity = ObjectIdentity
atmRoutingGroup = _AtmRoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2)
)
_RtDomainTable_Object = MibTable
rtDomainTable = _RtDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    rtDomainTable.setStatus("current")
_RtDomainEntry_Object = MibTableRow
rtDomainEntry = _RtDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 1, 1)
)
rtDomainEntry.setIndexNames(
    (0, "Fore-PNNI-MIB", "rtDomainID"),
)
if mibBuilder.loadTexts:
    rtDomainEntry.setStatus("current")
_RtDomainID_Type = Integer32
_RtDomainID_Object = MibTableColumn
rtDomainID = _RtDomainID_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 1, 1, 1),
    _RtDomainID_Type()
)
rtDomainID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtDomainID.setStatus("current")


class _RtDomainDefaultProto_Type(Integer32):
    """Custom type rtDomainDefaultProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftpnni", 1),
          ("gateway", 3),
          ("pnni", 2))
    )


_RtDomainDefaultProto_Type.__name__ = "Integer32"
_RtDomainDefaultProto_Object = MibTableColumn
rtDomainDefaultProto = _RtDomainDefaultProto_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 1, 1, 2),
    _RtDomainDefaultProto_Type()
)
rtDomainDefaultProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtDomainDefaultProto.setStatus("current")
_RtDomainPrefix_Type = NsapPrefix
_RtDomainPrefix_Object = MibTableColumn
rtDomainPrefix = _RtDomainPrefix_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 1, 1, 3),
    _RtDomainPrefix_Type()
)
rtDomainPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtDomainPrefix.setStatus("current")


class _RtDomainName_Type(DisplayString):
    """Custom type rtDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RtDomainName_Type.__name__ = "DisplayString"
_RtDomainName_Object = MibTableColumn
rtDomainName = _RtDomainName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 1, 1, 4),
    _RtDomainName_Type()
)
rtDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtDomainName.setStatus("current")


class _RtDomainDefSumState_Type(Integer32):
    """Custom type rtDomainDefSumState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RtDomainDefSumState_Type.__name__ = "Integer32"
_RtDomainDefSumState_Object = MibTableColumn
rtDomainDefSumState = _RtDomainDefSumState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 1, 1, 5),
    _RtDomainDefSumState_Type()
)
rtDomainDefSumState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtDomainDefSumState.setStatus("current")
_RtDomainStatus_Type = RowStatus
_RtDomainStatus_Object = MibTableColumn
rtDomainStatus = _RtDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 1, 1, 6),
    _RtDomainStatus_Type()
)
rtDomainStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtDomainStatus.setStatus("current")
_RtDomainDefaultPrefix_Type = NsapPrefix
_RtDomainDefaultPrefix_Object = MibTableColumn
rtDomainDefaultPrefix = _RtDomainDefaultPrefix_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 1, 1, 7),
    _RtDomainDefaultPrefix_Type()
)
rtDomainDefaultPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtDomainDefaultPrefix.setStatus("current")
_AtmrPrefixTable_Object = MibTable
atmrPrefixTable = _AtmrPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    atmrPrefixTable.setStatus("current")
_AtmrPrefixEntry_Object = MibTableRow
atmrPrefixEntry = _AtmrPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 2, 1)
)
atmrPrefixEntry.setIndexNames(
    (0, "Fore-PNNI-MIB", "rtDomainID"),
    (0, "Fore-PNNI-MIB", "atmrPrefixAddr"),
    (0, "Fore-PNNI-MIB", "atmrPrefixLength"),
)
if mibBuilder.loadTexts:
    atmrPrefixEntry.setStatus("current")
_AtmrPrefixAddr_Type = AtmAddrPrefix
_AtmrPrefixAddr_Object = MibTableColumn
atmrPrefixAddr = _AtmrPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 2, 1, 1),
    _AtmrPrefixAddr_Type()
)
atmrPrefixAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmrPrefixAddr.setStatus("current")
_AtmrPrefixLength_Type = PnniPrefixLength
_AtmrPrefixLength_Object = MibTableColumn
atmrPrefixLength = _AtmrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 2, 1, 2),
    _AtmrPrefixLength_Type()
)
atmrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmrPrefixLength.setStatus("current")
_AtmrPrefixFlags_Type = Integer32
_AtmrPrefixFlags_Object = MibTableColumn
atmrPrefixFlags = _AtmrPrefixFlags_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 2, 1, 3),
    _AtmrPrefixFlags_Type()
)
atmrPrefixFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPrefixFlags.setStatus("current")
_AtmrPrefixOwnerLevel_Type = Integer32
_AtmrPrefixOwnerLevel_Object = MibTableColumn
atmrPrefixOwnerLevel = _AtmrPrefixOwnerLevel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 2, 1, 4),
    _AtmrPrefixOwnerLevel_Type()
)
atmrPrefixOwnerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPrefixOwnerLevel.setStatus("current")


class _AtmrPrefixOwnerProtocol_Type(Integer32):
    """Custom type atmrPrefixOwnerProtocol based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("admin", 2),
          ("atmfext", 8),
          ("atmfint", 7),
          ("bogus", 1),
          ("ftpnni", 3),
          ("ilmi", 5),
          ("interdom", 9),
          ("pnni", 4),
          ("static", 6))
    )


_AtmrPrefixOwnerProtocol_Type.__name__ = "Integer32"
_AtmrPrefixOwnerProtocol_Object = MibTableColumn
atmrPrefixOwnerProtocol = _AtmrPrefixOwnerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 2, 1, 5),
    _AtmrPrefixOwnerProtocol_Type()
)
atmrPrefixOwnerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPrefixOwnerProtocol.setStatus("current")
_AtmrPrefixOwnerPathFlags_Type = Integer32
_AtmrPrefixOwnerPathFlags_Object = MibTableColumn
atmrPrefixOwnerPathFlags = _AtmrPrefixOwnerPathFlags_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 2, 1, 6),
    _AtmrPrefixOwnerPathFlags_Type()
)
atmrPrefixOwnerPathFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPrefixOwnerPathFlags.setStatus("current")
_AtmrPrefixTimeStamp_Type = Unsigned32
_AtmrPrefixTimeStamp_Object = MibTableColumn
atmrPrefixTimeStamp = _AtmrPrefixTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 2, 1, 7),
    _AtmrPrefixTimeStamp_Type()
)
atmrPrefixTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPrefixTimeStamp.setStatus("current")
_AtmrPteTable_Object = MibTable
atmrPteTable = _AtmrPteTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    atmrPteTable.setStatus("current")
_AtmrPteEntry_Object = MibTableRow
atmrPteEntry = _AtmrPteEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1)
)
atmrPteEntry.setIndexNames(
    (0, "Fore-PNNI-MIB", "rtDomainID"),
    (0, "Fore-PNNI-MIB", "atmrPrefixAddr"),
    (0, "Fore-PNNI-MIB", "atmrPrefixLength"),
    (0, "Fore-PNNI-MIB", "atmrPteIndex"),
)
if mibBuilder.loadTexts:
    atmrPteEntry.setStatus("current")
_AtmrPteIndex_Type = Integer32
_AtmrPteIndex_Object = MibTableColumn
atmrPteIndex = _AtmrPteIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 1),
    _AtmrPteIndex_Type()
)
atmrPteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmrPteIndex.setStatus("current")
_AtmrPteProtocolId_Type = Integer32
_AtmrPteProtocolId_Object = MibTableColumn
atmrPteProtocolId = _AtmrPteProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 2),
    _AtmrPteProtocolId_Type()
)
atmrPteProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPteProtocolId.setStatus("current")
_AtmrPteProtocolHandle_Type = Unsigned32
_AtmrPteProtocolHandle_Object = MibTableColumn
atmrPteProtocolHandle = _AtmrPteProtocolHandle_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 3),
    _AtmrPteProtocolHandle_Type()
)
atmrPteProtocolHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPteProtocolHandle.setStatus("current")


class _AtmrPteProtocol_Type(Integer32):
    """Custom type atmrPteProtocol based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("admin", 2),
          ("atmfext", 8),
          ("atmfint", 7),
          ("bogus", 1),
          ("ftpnni", 3),
          ("ilmi", 5),
          ("interdom", 9),
          ("pnni", 4),
          ("static", 6))
    )


_AtmrPteProtocol_Type.__name__ = "Integer32"
_AtmrPteProtocol_Object = MibTableColumn
atmrPteProtocol = _AtmrPteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 4),
    _AtmrPteProtocol_Type()
)
atmrPteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPteProtocol.setStatus("current")
_AtmrPtePathFlags_Type = Integer32
_AtmrPtePathFlags_Object = MibTableColumn
atmrPtePathFlags = _AtmrPtePathFlags_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 5),
    _AtmrPtePathFlags_Type()
)
atmrPtePathFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPtePathFlags.setStatus("current")
_AtmrPteLevel_Type = Integer32
_AtmrPteLevel_Object = MibTableColumn
atmrPteLevel = _AtmrPteLevel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 6),
    _AtmrPteLevel_Type()
)
atmrPteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPteLevel.setStatus("current")
_AtmrPteArea_Type = Unsigned32
_AtmrPteArea_Object = MibTableColumn
atmrPteArea = _AtmrPteArea_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 7),
    _AtmrPteArea_Type()
)
atmrPteArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPteArea.setStatus("current")
_AtmrPteScope_Type = Integer32
_AtmrPteScope_Object = MibTableColumn
atmrPteScope = _AtmrPteScope_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 8),
    _AtmrPteScope_Type()
)
atmrPteScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPteScope.setStatus("current")
_AtmrPteSourceArea_Type = Unsigned32
_AtmrPteSourceArea_Object = MibTableColumn
atmrPteSourceArea = _AtmrPteSourceArea_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 9),
    _AtmrPteSourceArea_Type()
)
atmrPteSourceArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPteSourceArea.setStatus("current")
_AtmrPteType_Type = Integer32
_AtmrPteType_Object = MibTableColumn
atmrPteType = _AtmrPteType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 10),
    _AtmrPteType_Type()
)
atmrPteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPteType.setStatus("current")
_AtmrPteTnsLen_Type = Integer32
_AtmrPteTnsLen_Object = MibTableColumn
atmrPteTnsLen = _AtmrPteTnsLen_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 11),
    _AtmrPteTnsLen_Type()
)
atmrPteTnsLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPteTnsLen.setStatus("current")
_AtmrPteTnsType_Type = TnsType
_AtmrPteTnsType_Object = MibTableColumn
atmrPteTnsType = _AtmrPteTnsType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 12),
    _AtmrPteTnsType_Type()
)
atmrPteTnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPteTnsType.setStatus("current")
_AtmrPteTnsPlan_Type = TnsPlan
_AtmrPteTnsPlan_Object = MibTableColumn
atmrPteTnsPlan = _AtmrPteTnsPlan_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 13),
    _AtmrPteTnsPlan_Type()
)
atmrPteTnsPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPteTnsPlan.setStatus("current")
_AtmrPteTnsId_Type = Integer32
_AtmrPteTnsId_Object = MibTableColumn
atmrPteTnsId = _AtmrPteTnsId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 3, 1, 14),
    _AtmrPteTnsId_Type()
)
atmrPteTnsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrPteTnsId.setStatus("current")
_AtmrInterDomainRouteTable_Object = MibTable
atmrInterDomainRouteTable = _AtmrInterDomainRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    atmrInterDomainRouteTable.setStatus("current")
_AtmrInterDomainRouteEntry_Object = MibTableRow
atmrInterDomainRouteEntry = _AtmrInterDomainRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 4, 1)
)
atmrInterDomainRouteEntry.setIndexNames(
    (0, "Fore-PNNI-MIB", "atmrIDRDomainID"),
    (0, "Fore-PNNI-MIB", "atmrIDRAddr"),
    (0, "Fore-PNNI-MIB", "atmrIDRAddrLen"),
    (0, "Fore-PNNI-MIB", "atmrIDRDestDomainID"),
)
if mibBuilder.loadTexts:
    atmrInterDomainRouteEntry.setStatus("current")
_AtmrIDRDomainID_Type = Integer32
_AtmrIDRDomainID_Object = MibTableColumn
atmrIDRDomainID = _AtmrIDRDomainID_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 4, 1, 1),
    _AtmrIDRDomainID_Type()
)
atmrIDRDomainID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmrIDRDomainID.setStatus("current")
_AtmrIDRAddr_Type = AtmAddrPrefix
_AtmrIDRAddr_Object = MibTableColumn
atmrIDRAddr = _AtmrIDRAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 4, 1, 2),
    _AtmrIDRAddr_Type()
)
atmrIDRAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmrIDRAddr.setStatus("current")
_AtmrIDRAddrLen_Type = PnniPrefixLength
_AtmrIDRAddrLen_Object = MibTableColumn
atmrIDRAddrLen = _AtmrIDRAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 4, 1, 3),
    _AtmrIDRAddrLen_Type()
)
atmrIDRAddrLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmrIDRAddrLen.setStatus("current")
_AtmrIDRDestDomainID_Type = Integer32
_AtmrIDRDestDomainID_Object = MibTableColumn
atmrIDRDestDomainID = _AtmrIDRDestDomainID_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 4, 1, 4),
    _AtmrIDRDestDomainID_Type()
)
atmrIDRDestDomainID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmrIDRDestDomainID.setStatus("current")
_AtmrIDRRowStatus_Type = RowStatus
_AtmrIDRRowStatus_Object = MibTableColumn
atmrIDRRowStatus = _AtmrIDRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 4, 1, 5),
    _AtmrIDRRowStatus_Type()
)
atmrIDRRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmrIDRRowStatus.setStatus("current")
_AtmrDestNsapTable_Object = MibTable
atmrDestNsapTable = _AtmrDestNsapTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 5)
)
if mibBuilder.loadTexts:
    atmrDestNsapTable.setStatus("current")
_AtmrDestNsapEntry_Object = MibTableRow
atmrDestNsapEntry = _AtmrDestNsapEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 5, 1)
)
atmrDestNsapEntry.setIndexNames(
    (0, "Fore-PNNI-MIB", "rtDomainID"),
    (0, "Fore-Switch-MIB", "portNumber"),
)
if mibBuilder.loadTexts:
    atmrDestNsapEntry.setStatus("current")
_AtmrDestNsapAddr_Type = NsapAddr
_AtmrDestNsapAddr_Object = MibTableColumn
atmrDestNsapAddr = _AtmrDestNsapAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 2, 5, 1, 1),
    _AtmrDestNsapAddr_Type()
)
atmrDestNsapAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmrDestNsapAddr.setStatus("current")
_PnniIfMapGroup_ObjectIdentity = ObjectIdentity
pnniIfMapGroup = _PnniIfMapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3)
)
_PnniPortVpiMapTable_Object = MibTable
pnniPortVpiMapTable = _PnniPortVpiMapTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    pnniPortVpiMapTable.setStatus("current")
_PnniPortVpiMapEntry_Object = MibTableRow
pnniPortVpiMapEntry = _PnniPortVpiMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3, 1, 1)
)
pnniPortVpiMapEntry.setIndexNames(
    (0, "Fore-PNNI-MIB", "pnniPortVpiMapPort"),
    (0, "Fore-PNNI-MIB", "pnniPortVpiMapVpi"),
)
if mibBuilder.loadTexts:
    pnniPortVpiMapEntry.setStatus("current")
_PnniPortVpiMapPort_Type = Integer32
_PnniPortVpiMapPort_Object = MibTableColumn
pnniPortVpiMapPort = _PnniPortVpiMapPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3, 1, 1, 1),
    _PnniPortVpiMapPort_Type()
)
pnniPortVpiMapPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniPortVpiMapPort.setStatus("current")
_PnniPortVpiMapVpi_Type = Integer32
_PnniPortVpiMapVpi_Object = MibTableColumn
pnniPortVpiMapVpi = _PnniPortVpiMapVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3, 1, 1, 2),
    _PnniPortVpiMapVpi_Type()
)
pnniPortVpiMapVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniPortVpiMapVpi.setStatus("current")
_PnniPortVpiMapIfIndex_Type = InterfaceIndex
_PnniPortVpiMapIfIndex_Object = MibTableColumn
pnniPortVpiMapIfIndex = _PnniPortVpiMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3, 1, 1, 3),
    _PnniPortVpiMapIfIndex_Type()
)
pnniPortVpiMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPortVpiMapIfIndex.setStatus("current")
_PnniPortVpiMapPortId_Type = PnniPortId
_PnniPortVpiMapPortId_Object = MibTableColumn
pnniPortVpiMapPortId = _PnniPortVpiMapPortId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3, 1, 1, 4),
    _PnniPortVpiMapPortId_Type()
)
pnniPortVpiMapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPortVpiMapPortId.setStatus("current")
_PnniPortIdMapTable_Object = MibTable
pnniPortIdMapTable = _PnniPortIdMapTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3, 2)
)
if mibBuilder.loadTexts:
    pnniPortIdMapTable.setStatus("current")
_PnniPortIdMapEntry_Object = MibTableRow
pnniPortIdMapEntry = _PnniPortIdMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3, 2, 1)
)
pnniPortIdMapEntry.setIndexNames(
    (0, "Fore-PNNI-MIB", "pnniPortIdMapPortId"),
)
if mibBuilder.loadTexts:
    pnniPortIdMapEntry.setStatus("current")
_PnniPortIdMapPortId_Type = PnniPortId
_PnniPortIdMapPortId_Object = MibTableColumn
pnniPortIdMapPortId = _PnniPortIdMapPortId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3, 2, 1, 1),
    _PnniPortIdMapPortId_Type()
)
pnniPortIdMapPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniPortIdMapPortId.setStatus("current")
_PnniPortIdMapPort_Type = Integer32
_PnniPortIdMapPort_Object = MibTableColumn
pnniPortIdMapPort = _PnniPortIdMapPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3, 2, 1, 2),
    _PnniPortIdMapPort_Type()
)
pnniPortIdMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPortIdMapPort.setStatus("current")
_PnniPortIdMapVpi_Type = Integer32
_PnniPortIdMapVpi_Object = MibTableColumn
pnniPortIdMapVpi = _PnniPortIdMapVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3, 2, 1, 3),
    _PnniPortIdMapVpi_Type()
)
pnniPortIdMapVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPortIdMapVpi.setStatus("current")
_PnniPortIdMapIfIndex_Type = InterfaceIndex
_PnniPortIdMapIfIndex_Object = MibTableColumn
pnniPortIdMapIfIndex = _PnniPortIdMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 4, 3, 2, 1, 4),
    _PnniPortIdMapIfIndex_Type()
)
pnniPortIdMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPortIdMapIfIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-PNNI-MIB",
    **{"PnniPcProfileIndex": PnniPcProfileIndex,
       "InterfaceLabel": InterfaceLabel,
       "forePnniGroup": forePnniGroup,
       "pnniGroup": pnniGroup,
       "pnniPcProfileTable": pnniPcProfileTable,
       "pnniPcProfileEntry": pnniPcProfileEntry,
       "pnniPcProfileIndex": pnniPcProfileIndex,
       "pnniPcProfileType": pnniPcProfileType,
       "pnniPcProfileServiceCategory": pnniPcProfileServiceCategory,
       "pnniPcProfileMinFwdCR": pnniPcProfileMinFwdCR,
       "pnniPcProfileMinRevCR": pnniPcProfileMinRevCR,
       "pnniPcProfileFwdClpType": pnniPcProfileFwdClpType,
       "pnniPcProfileRevClpType": pnniPcProfileRevClpType,
       "pnniPcProfileFwdCLR": pnniPcProfileFwdCLR,
       "pnniPcProfileRevCLR": pnniPcProfileRevCLR,
       "pnniPcProfileOptCTD": pnniPcProfileOptCTD,
       "pnniPcProfileOptCDV": pnniPcProfileOptCDV,
       "pnniPcProfileOptAdminWeight": pnniPcProfileOptAdminWeight,
       "pnniPcProfileRstrVPOnly": pnniPcProfileRstrVPOnly,
       "pnniPcProfileRstrLoadBalance": pnniPcProfileRstrLoadBalance,
       "pnniPcProfileNumberOfAvoidLinks": pnniPcProfileNumberOfAvoidLinks,
       "pnniPcProfileNumberOfPreferLinks": pnniPcProfileNumberOfPreferLinks,
       "pnniPcProfileNumberOfHits": pnniPcProfileNumberOfHits,
       "pnniPcProfileTimeStamp": pnniPcProfileTimeStamp,
       "pnniPcProfileState": pnniPcProfileState,
       "pnniPcProfileRowStatus": pnniPcProfileRowStatus,
       "pnniPcProfileCongestionBased": pnniPcProfileCongestionBased,
       "pnniExportPolicyTable": pnniExportPolicyTable,
       "pnniExportPolicyEntry": pnniExportPolicyEntry,
       "pnniExportPolicyAddress": pnniExportPolicyAddress,
       "pnniExportPolicyPrefixLength": pnniExportPolicyPrefixLength,
       "pnniExportPolicyType": pnniExportPolicyType,
       "pnniExportPolicyAction": pnniExportPolicyAction,
       "pnniExportPolicyState": pnniExportPolicyState,
       "pnniExportPolicyTnsType": pnniExportPolicyTnsType,
       "pnniExportPolicyTnsPlan": pnniExportPolicyTnsPlan,
       "pnniExportPolicyTnsId": pnniExportPolicyTnsId,
       "pnniExportPolicyMetricsTag": pnniExportPolicyMetricsTag,
       "pnniExportPolicyRowStatus": pnniExportPolicyRowStatus,
       "pnniNodeExtnTable": pnniNodeExtnTable,
       "pnniNodeExtnEntry": pnniNodeExtnEntry,
       "pnniNodeExtnDomainID": pnniNodeExtnDomainID,
       "pnniNodeExtnForeLevel": pnniNodeExtnForeLevel,
       "pnniNodeExtnForeArea": pnniNodeExtnForeArea,
       "pnniNodeExtnShutdown": pnniNodeExtnShutdown,
       "pnniNodeExtnLoadBalancing": pnniNodeExtnLoadBalancing,
       "pnniNodeExtnAdvertisedPglPriority": pnniNodeExtnAdvertisedPglPriority,
       "pnniNodeExtnPcCongestionRange": pnniNodeExtnPcCongestionRange,
       "pnniMapRaigTable": pnniMapRaigTable,
       "pnniMapRaigEntry": pnniMapRaigEntry,
       "pnniMapRaigIndex": pnniMapRaigIndex,
       "pnniMapRaigDirection": pnniMapRaigDirection,
       "pnniMapRaigFlags": pnniMapRaigFlags,
       "pnniMapRaigAdminWt": pnniMapRaigAdminWt,
       "pnniMapRaigMaximumCellRate": pnniMapRaigMaximumCellRate,
       "pnniMapRaigAvailableCellRate": pnniMapRaigAvailableCellRate,
       "pnniMapRaigCellTransferDelay": pnniMapRaigCellTransferDelay,
       "pnniMapRaigCellDelayVariation": pnniMapRaigCellDelayVariation,
       "pnniMapRaigCellLossRatio": pnniMapRaigCellLossRatio,
       "pnniMapRaigCellLossRatio1": pnniMapRaigCellLossRatio1,
       "pnniMapRaigCellRateMargin": pnniMapRaigCellRateMargin,
       "pnniMapRaigVarianceFactor": pnniMapRaigVarianceFactor,
       "pnniMapAddrRaigTable": pnniMapAddrRaigTable,
       "pnniMapAddrRaigEntry": pnniMapAddrRaigEntry,
       "pnniMapAddrRaigIndex": pnniMapAddrRaigIndex,
       "pnniMapAddrRaigDirection": pnniMapAddrRaigDirection,
       "pnniMapAddrRaigFlags": pnniMapAddrRaigFlags,
       "pnniMapAddrRaigAdminWt": pnniMapAddrRaigAdminWt,
       "pnniMapAddrRaigMaximumCellRate": pnniMapAddrRaigMaximumCellRate,
       "pnniMapAddrRaigAvailableCellRate": pnniMapAddrRaigAvailableCellRate,
       "pnniMapAddrRaigCellTransferDelay": pnniMapAddrRaigCellTransferDelay,
       "pnniMapAddrRaigCellDelayVariation": pnniMapAddrRaigCellDelayVariation,
       "pnniMapAddrRaigCellLossRatio": pnniMapAddrRaigCellLossRatio,
       "pnniMapAddrRaigCellLossRatio1": pnniMapAddrRaigCellLossRatio1,
       "pnniMapAddrRaigCellRateMargin": pnniMapAddrRaigCellRateMargin,
       "pnniMapAddrRaigVarianceFactor": pnniMapAddrRaigVarianceFactor,
       "pnniPcProfileMapTable": pnniPcProfileMapTable,
       "pnniPcProfileMapEntry": pnniPcProfileMapEntry,
       "pnniPcProfileMapOptIndex": pnniPcProfileMapOptIndex,
       "pnniPcProfileMapNodeId": pnniPcProfileMapNodeId,
       "pnniPcProfileMapLocalPort": pnniPcProfileMapLocalPort,
       "pnniPcProfileMapParentNode": pnniPcProfileMapParentNode,
       "pnniPcProfileMapAdminWt": pnniPcProfileMapAdminWt,
       "pnniPcProfileMapMaximumCellRate": pnniPcProfileMapMaximumCellRate,
       "pnniPcProfileMapAvailableCellRate": pnniPcProfileMapAvailableCellRate,
       "pnniPcProfileMapCellTransferDelay": pnniPcProfileMapCellTransferDelay,
       "pnniPcProfileMapCellDelayVariation": pnniPcProfileMapCellDelayVariation,
       "pnniPcProfileMapCellLossRatio": pnniPcProfileMapCellLossRatio,
       "pnniPcProfileMapCellLossRatio1": pnniPcProfileMapCellLossRatio1,
       "pnniPcProfileMapCellRateMargin": pnniPcProfileMapCellRateMargin,
       "pnniPcProfileMapVarianceFactor": pnniPcProfileMapVarianceFactor,
       "pnniSpanningTreeMapTable": pnniSpanningTreeMapTable,
       "pnniSpanningTreeMapEntry": pnniSpanningTreeMapEntry,
       "pnniSpanningTreeMapNodeId": pnniSpanningTreeMapNodeId,
       "pnniSpanningTreeMapStatus": pnniSpanningTreeMapStatus,
       "pnniSpanningTreeMapParentNode": pnniSpanningTreeMapParentNode,
       "pnniSpanningTreeMapPort": pnniSpanningTreeMapPort,
       "pnniSpanningTreeMapLinkType": pnniSpanningTreeMapLinkType,
       "pnniNodeScStatsTable": pnniNodeScStatsTable,
       "pnniNodeScStatsEntry": pnniNodeScStatsEntry,
       "pnniNodeScStatsNrOfEvents": pnniNodeScStatsNrOfEvents,
       "pnniNodeScStatsNrOfPurges": pnniNodeScStatsNrOfPurges,
       "pnniNodeScStatsNrOfTimeoutPurges": pnniNodeScStatsNrOfTimeoutPurges,
       "pnniNodeScStatsNrOfPacketsDropped": pnniNodeScStatsNrOfPacketsDropped,
       "pnniNodeScStatsNrOfHiPriPktsDropped": pnniNodeScStatsNrOfHiPriPktsDropped,
       "pnniNodeScStatsNrOfLowPriPktsDropped": pnniNodeScStatsNrOfLowPriPktsDropped,
       "pnniNodeScStatsNrOfNodalInfoEvents": pnniNodeScStatsNrOfNodalInfoEvents,
       "pnniNodeScStatsNrOfHorizLinkEvents": pnniNodeScStatsNrOfHorizLinkEvents,
       "pnniNodeScStatsNrOfUpLinkEvents": pnniNodeScStatsNrOfUpLinkEvents,
       "pnniNodeScStatsNrOfNodalStateEvents": pnniNodeScStatsNrOfNodalStateEvents,
       "pnniCrankbackGroup": pnniCrankbackGroup,
       "pnniMaxCrankbackTries": pnniMaxCrankbackTries,
       "pnniPcProfileAvoidLinkTable": pnniPcProfileAvoidLinkTable,
       "pnniPcProfileAvoidLinkEntry": pnniPcProfileAvoidLinkEntry,
       "pnniPcProfileAvoidLinkIndex": pnniPcProfileAvoidLinkIndex,
       "pnniPcProfileAvoidLinkNodeId": pnniPcProfileAvoidLinkNodeId,
       "pnniPcProfileAvoidLinkPortId": pnniPcProfileAvoidLinkPortId,
       "pnniPcProfileAvoidLinkType": pnniPcProfileAvoidLinkType,
       "pnniPcProfileAvoidLinkRemoteNodeId": pnniPcProfileAvoidLinkRemoteNodeId,
       "pnniPcProfilePreferLinkTable": pnniPcProfilePreferLinkTable,
       "pnniPcProfilePreferLinkEntry": pnniPcProfilePreferLinkEntry,
       "pnniPcProfilePreferLinkIndex": pnniPcProfilePreferLinkIndex,
       "pnniPcProfilePreferLinkNodeId": pnniPcProfilePreferLinkNodeId,
       "pnniPcProfilePreferLinkPortId": pnniPcProfilePreferLinkPortId,
       "pnniPcProfilePreferLinkType": pnniPcProfilePreferLinkType,
       "pnniPcProfilePreferLinkRemoteNodeId": pnniPcProfilePreferLinkRemoteNodeId,
       "pnniParametersGroup": pnniParametersGroup,
       "pnniMaxDtlSize": pnniMaxDtlSize,
       "pnniLoadBalancedUbrEnable": pnniLoadBalancedUbrEnable,
       "forePnniDTLTable": forePnniDTLTable,
       "forePnniDTLEntry": forePnniDTLEntry,
       "forePnniDTLName": forePnniDTLName,
       "forePnniDTLValidity": forePnniDTLValidity,
       "pnniDtlComputationTable": pnniDtlComputationTable,
       "pnniDtlComputationEntry": pnniDtlComputationEntry,
       "pnniDtlComputationNodeIndex": pnniDtlComputationNodeIndex,
       "pnniDtlComputationDtlIndex": pnniDtlComputationDtlIndex,
       "pnniDtlComputationDestNsapAddress": pnniDtlComputationDestNsapAddress,
       "pnniDtlComputationCompute": pnniDtlComputationCompute,
       "pnniDtlListTable": pnniDtlListTable,
       "pnniDtlListEntry": pnniDtlListEntry,
       "pnniDtlListTag": pnniDtlListTag,
       "pnniDtlListNodeIndex": pnniDtlListNodeIndex,
       "pnniDtlListDtlIndex": pnniDtlListDtlIndex,
       "pnniDtlListWeight": pnniDtlListWeight,
       "pnniDtlListStatus": pnniDtlListStatus,
       "pnniMapNodeExtTable": pnniMapNodeExtTable,
       "pnniMapNodeExtEntry": pnniMapNodeExtEntry,
       "pnniMapNodeExtRemoteNodeId": pnniMapNodeExtRemoteNodeId,
       "pnniMapNodeExtSoftwareVersion": pnniMapNodeExtSoftwareVersion,
       "pnniMapNodeExtHardwareVersion": pnniMapNodeExtHardwareVersion,
       "pnniMapNodeExtHardwareId": pnniMapNodeExtHardwareId,
       "pnniMapNodeExtSwitchName": pnniMapNodeExtSwitchName,
       "pnniMapNodeExtRemoteNodeIndex": pnniMapNodeExtRemoteNodeIndex,
       "pnniMapNodeExtForeNodalFlags": pnniMapNodeExtForeNodalFlags,
       "pnniMapNodeIpAddrTable": pnniMapNodeIpAddrTable,
       "pnniMapNodeIpAddrEntry": pnniMapNodeIpAddrEntry,
       "pnniMapNodeIpAddr": pnniMapNodeIpAddr,
       "pnniMapNodeIpAddrIfName": pnniMapNodeIpAddrIfName,
       "pnniConnTreeMapTable": pnniConnTreeMapTable,
       "pnniConnTreeMapEntry": pnniConnTreeMapEntry,
       "pnniConnTreeMapNodeId": pnniConnTreeMapNodeId,
       "pnniConnTreeMapStatus": pnniConnTreeMapStatus,
       "pnniConnTreeMapParentNode": pnniConnTreeMapParentNode,
       "pnniConnTreeMapPort": pnniConnTreeMapPort,
       "pnniConnTreeMapLinkType": pnniConnTreeMapLinkType,
       "atmRoutingGroup": atmRoutingGroup,
       "rtDomainTable": rtDomainTable,
       "rtDomainEntry": rtDomainEntry,
       "rtDomainID": rtDomainID,
       "rtDomainDefaultProto": rtDomainDefaultProto,
       "rtDomainPrefix": rtDomainPrefix,
       "rtDomainName": rtDomainName,
       "rtDomainDefSumState": rtDomainDefSumState,
       "rtDomainStatus": rtDomainStatus,
       "rtDomainDefaultPrefix": rtDomainDefaultPrefix,
       "atmrPrefixTable": atmrPrefixTable,
       "atmrPrefixEntry": atmrPrefixEntry,
       "atmrPrefixAddr": atmrPrefixAddr,
       "atmrPrefixLength": atmrPrefixLength,
       "atmrPrefixFlags": atmrPrefixFlags,
       "atmrPrefixOwnerLevel": atmrPrefixOwnerLevel,
       "atmrPrefixOwnerProtocol": atmrPrefixOwnerProtocol,
       "atmrPrefixOwnerPathFlags": atmrPrefixOwnerPathFlags,
       "atmrPrefixTimeStamp": atmrPrefixTimeStamp,
       "atmrPteTable": atmrPteTable,
       "atmrPteEntry": atmrPteEntry,
       "atmrPteIndex": atmrPteIndex,
       "atmrPteProtocolId": atmrPteProtocolId,
       "atmrPteProtocolHandle": atmrPteProtocolHandle,
       "atmrPteProtocol": atmrPteProtocol,
       "atmrPtePathFlags": atmrPtePathFlags,
       "atmrPteLevel": atmrPteLevel,
       "atmrPteArea": atmrPteArea,
       "atmrPteScope": atmrPteScope,
       "atmrPteSourceArea": atmrPteSourceArea,
       "atmrPteType": atmrPteType,
       "atmrPteTnsLen": atmrPteTnsLen,
       "atmrPteTnsType": atmrPteTnsType,
       "atmrPteTnsPlan": atmrPteTnsPlan,
       "atmrPteTnsId": atmrPteTnsId,
       "atmrInterDomainRouteTable": atmrInterDomainRouteTable,
       "atmrInterDomainRouteEntry": atmrInterDomainRouteEntry,
       "atmrIDRDomainID": atmrIDRDomainID,
       "atmrIDRAddr": atmrIDRAddr,
       "atmrIDRAddrLen": atmrIDRAddrLen,
       "atmrIDRDestDomainID": atmrIDRDestDomainID,
       "atmrIDRRowStatus": atmrIDRRowStatus,
       "atmrDestNsapTable": atmrDestNsapTable,
       "atmrDestNsapEntry": atmrDestNsapEntry,
       "atmrDestNsapAddr": atmrDestNsapAddr,
       "pnniIfMapGroup": pnniIfMapGroup,
       "pnniPortVpiMapTable": pnniPortVpiMapTable,
       "pnniPortVpiMapEntry": pnniPortVpiMapEntry,
       "pnniPortVpiMapPort": pnniPortVpiMapPort,
       "pnniPortVpiMapVpi": pnniPortVpiMapVpi,
       "pnniPortVpiMapIfIndex": pnniPortVpiMapIfIndex,
       "pnniPortVpiMapPortId": pnniPortVpiMapPortId,
       "pnniPortIdMapTable": pnniPortIdMapTable,
       "pnniPortIdMapEntry": pnniPortIdMapEntry,
       "pnniPortIdMapPortId": pnniPortIdMapPortId,
       "pnniPortIdMapPort": pnniPortIdMapPort,
       "pnniPortIdMapVpi": pnniPortIdMapVpi,
       "pnniPortIdMapIfIndex": pnniPortIdMapIfIndex}
)
