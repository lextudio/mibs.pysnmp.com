# SNMP MIB module (EQL-DCB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQL-DCB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:55 2024
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

(eqlGroupId,) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "eqlGroupId")

(eqlMemberIndex,) = mibBuilder.importSymbols(
    "EQLMEMBER-MIB",
    "eqlMemberIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

eqlDcbMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 19)
)
eqlDcbMib.setRevisions(
        ("2011-01-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EqlDcbxTrafficClassGroupValue(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class EqlDcbxAppSelector(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("asEthertype", 0),
          ("asNotTCPUDPPortNumber", 4),
          ("asTCPPortNumber", 1),
          ("asTCPUDPPortNumber", 3),
          ("asUDPPortNumber", 2))
    )



class EqlDcbxAppProtocol(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class EqlDcbxSupportedCapacity(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )



class EqlVlanIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )



class EqlIEEE8021PriorityValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class EqlIEEEDraftSubtypeValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class EqlDcbxState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("off", 0),
          ("on", 1))
    )



class EqlDcbxVlanState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("off", 0),
          ("static", 1))
    )



class EqlDcbxTransmissionSelectionAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tsaCreditBasedShaper", 1),
          ("tsaEnhancedTransmission", 2),
          ("tsaStrictPriority", 0),
          ("tsaVendorSpecific", 255))
    )



class EqlDcbxMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dcbx101Baseline", 1),
          ("dcbxIeeeStandard", 2),
          ("off", 0))
    )



# MIB Managed Objects in the order of their OIDs

_EqlDcbMIBObjects_ObjectIdentity = ObjectIdentity
eqlDcbMIBObjects = _EqlDcbMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1)
)
_EqlDcbStaticIfTable_Object = MibTable
eqlDcbStaticIfTable = _EqlDcbStaticIfTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1)
)
if mibBuilder.loadTexts:
    eqlDcbStaticIfTable.setStatus("current")
_EqlDcbStaticIfEntry_Object = MibTableRow
eqlDcbStaticIfEntry = _EqlDcbStaticIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1)
)
eqlDcbStaticIfEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eqlDcbStaticIfEntry.setStatus("current")
_EqlDcbxConfigTCSupportedTxEnable_Type = TruthValue
_EqlDcbxConfigTCSupportedTxEnable_Object = MibTableColumn
eqlDcbxConfigTCSupportedTxEnable = _EqlDcbxConfigTCSupportedTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 1),
    _EqlDcbxConfigTCSupportedTxEnable_Type()
)
eqlDcbxConfigTCSupportedTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigTCSupportedTxEnable.setStatus("deprecated")


class _EqlDcbxConfigETSConfigurationTxEnable_Type(TruthValue):
    """Custom type eqlDcbxConfigETSConfigurationTxEnable based on TruthValue"""


_EqlDcbxConfigETSConfigurationTxEnable_Object = MibTableColumn
eqlDcbxConfigETSConfigurationTxEnable = _EqlDcbxConfigETSConfigurationTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 2),
    _EqlDcbxConfigETSConfigurationTxEnable_Type()
)
eqlDcbxConfigETSConfigurationTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigETSConfigurationTxEnable.setStatus("current")


class _EqlDcbxConfigETSRecommendationTxEnable_Type(TruthValue):
    """Custom type eqlDcbxConfigETSRecommendationTxEnable based on TruthValue"""


_EqlDcbxConfigETSRecommendationTxEnable_Object = MibTableColumn
eqlDcbxConfigETSRecommendationTxEnable = _EqlDcbxConfigETSRecommendationTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 3),
    _EqlDcbxConfigETSRecommendationTxEnable_Type()
)
eqlDcbxConfigETSRecommendationTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigETSRecommendationTxEnable.setStatus("current")


class _EqlDcbxConfigPFCTxEnable_Type(TruthValue):
    """Custom type eqlDcbxConfigPFCTxEnable based on TruthValue"""


_EqlDcbxConfigPFCTxEnable_Object = MibTableColumn
eqlDcbxConfigPFCTxEnable = _EqlDcbxConfigPFCTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 4),
    _EqlDcbxConfigPFCTxEnable_Type()
)
eqlDcbxConfigPFCTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigPFCTxEnable.setStatus("current")


class _EqlDcbxConfigAppPriorityTxEnable_Type(TruthValue):
    """Custom type eqlDcbxConfigAppPriorityTxEnable based on TruthValue"""


_EqlDcbxConfigAppPriorityTxEnable_Object = MibTableColumn
eqlDcbxConfigAppPriorityTxEnable = _EqlDcbxConfigAppPriorityTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 5),
    _EqlDcbxConfigAppPriorityTxEnable_Type()
)
eqlDcbxConfigAppPriorityTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigAppPriorityTxEnable.setStatus("current")


class _EqlDcbxConfigQcnTxEnable_Type(TruthValue):
    """Custom type eqlDcbxConfigQcnTxEnable based on TruthValue"""


_EqlDcbxConfigQcnTxEnable_Object = MibTableColumn
eqlDcbxConfigQcnTxEnable = _EqlDcbxConfigQcnTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 6),
    _EqlDcbxConfigQcnTxEnable_Type()
)
eqlDcbxConfigQcnTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigQcnTxEnable.setStatus("current")
_EqlDcbxAdminTCSupported_Type = EqlDcbxSupportedCapacity
_EqlDcbxAdminTCSupported_Object = MibTableColumn
eqlDcbxAdminTCSupported = _EqlDcbxAdminTCSupported_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 7),
    _EqlDcbxAdminTCSupported_Type()
)
eqlDcbxAdminTCSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminTCSupported.setStatus("deprecated")


class _EqlDcbxAdminETSConMaxTCG_Type(EqlDcbxSupportedCapacity):
    """Custom type eqlDcbxAdminETSConMaxTCG based on EqlDcbxSupportedCapacity"""
    defaultValue = 0


_EqlDcbxAdminETSConMaxTCG_Object = MibTableColumn
eqlDcbxAdminETSConMaxTCG = _EqlDcbxAdminETSConMaxTCG_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 8),
    _EqlDcbxAdminETSConMaxTCG_Type()
)
eqlDcbxAdminETSConMaxTCG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConMaxTCG.setStatus("current")


class _EqlDcbxAdminETSConWilling_Type(TruthValue):
    """Custom type eqlDcbxAdminETSConWilling based on TruthValue"""


_EqlDcbxAdminETSConWilling_Object = MibTableColumn
eqlDcbxAdminETSConWilling = _EqlDcbxAdminETSConWilling_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 9),
    _EqlDcbxAdminETSConWilling_Type()
)
eqlDcbxAdminETSConWilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConWilling.setStatus("current")


class _EqlDcbxAdminETSConTrafficClassGroupBandwidthTable_Type(OctetString):
    """Custom type eqlDcbxAdminETSConTrafficClassGroupBandwidthTable based on OctetString"""
    defaultHexValue = "6400000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EqlDcbxAdminETSConTrafficClassGroupBandwidthTable_Type.__name__ = "OctetString"
_EqlDcbxAdminETSConTrafficClassGroupBandwidthTable_Object = MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupBandwidthTable = _EqlDcbxAdminETSConTrafficClassGroupBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 10),
    _EqlDcbxAdminETSConTrafficClassGroupBandwidthTable_Type()
)
eqlDcbxAdminETSConTrafficClassGroupBandwidthTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTrafficClassGroupBandwidthTable.setStatus("current")


class _EqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable_Type(OctetString):
    """Custom type eqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable based on OctetString"""
    defaultHexValue = "6400000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable_Type.__name__ = "OctetString"
_EqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable_Object = MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable = _EqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 11),
    _EqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable_Type()
)
eqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable.setStatus("current")


class _EqlDcbxAdminPFCWilling_Type(TruthValue):
    """Custom type eqlDcbxAdminPFCWilling based on TruthValue"""


_EqlDcbxAdminPFCWilling_Object = MibTableColumn
eqlDcbxAdminPFCWilling = _EqlDcbxAdminPFCWilling_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 12),
    _EqlDcbxAdminPFCWilling_Type()
)
eqlDcbxAdminPFCWilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminPFCWilling.setStatus("current")


class _EqlDcbxAdminPFCMBC_Type(TruthValue):
    """Custom type eqlDcbxAdminPFCMBC based on TruthValue"""


_EqlDcbxAdminPFCMBC_Object = MibTableColumn
eqlDcbxAdminPFCMBC = _EqlDcbxAdminPFCMBC_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 13),
    _EqlDcbxAdminPFCMBC_Type()
)
eqlDcbxAdminPFCMBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminPFCMBC.setStatus("current")


class _EqlDcbxAdminPFCCap_Type(EqlDcbxSupportedCapacity):
    """Custom type eqlDcbxAdminPFCCap based on EqlDcbxSupportedCapacity"""
    defaultValue = 8


_EqlDcbxAdminPFCCap_Object = MibTableColumn
eqlDcbxAdminPFCCap = _EqlDcbxAdminPFCCap_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 14),
    _EqlDcbxAdminPFCCap_Type()
)
eqlDcbxAdminPFCCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminPFCCap.setStatus("current")


class _EqlDcbxAdminAppPriorityWilling_Type(TruthValue):
    """Custom type eqlDcbxAdminAppPriorityWilling based on TruthValue"""


_EqlDcbxAdminAppPriorityWilling_Object = MibTableColumn
eqlDcbxAdminAppPriorityWilling = _EqlDcbxAdminAppPriorityWilling_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 15),
    _EqlDcbxAdminAppPriorityWilling_Type()
)
eqlDcbxAdminAppPriorityWilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminAppPriorityWilling.setStatus("current")


class _EqlDcbxConfigAutoDetectVLANEnable_Type(TruthValue):
    """Custom type eqlDcbxConfigAutoDetectVLANEnable based on TruthValue"""


_EqlDcbxConfigAutoDetectVLANEnable_Object = MibTableColumn
eqlDcbxConfigAutoDetectVLANEnable = _EqlDcbxConfigAutoDetectVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 16),
    _EqlDcbxConfigAutoDetectVLANEnable_Type()
)
eqlDcbxConfigAutoDetectVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigAutoDetectVLANEnable.setStatus("current")


class _EqlDcbxConfigVLANId_Type(EqlVlanIdentifier):
    """Custom type eqlDcbxConfigVLANId based on EqlVlanIdentifier"""
    defaultValue = 4095


_EqlDcbxConfigVLANId_Object = MibTableColumn
eqlDcbxConfigVLANId = _EqlDcbxConfigVLANId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 17),
    _EqlDcbxConfigVLANId_Type()
)
eqlDcbxConfigVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigVLANId.setStatus("current")


class _EqlDcbxAdminETSConTrafficClassGroupPri0_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSConTrafficClassGroupPri0 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSConTrafficClassGroupPri0_Object = MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri0 = _EqlDcbxAdminETSConTrafficClassGroupPri0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 18),
    _EqlDcbxAdminETSConTrafficClassGroupPri0_Type()
)
eqlDcbxAdminETSConTrafficClassGroupPri0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTrafficClassGroupPri0.setStatus("current")


class _EqlDcbxAdminETSConTrafficClassGroupPri1_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSConTrafficClassGroupPri1 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSConTrafficClassGroupPri1_Object = MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri1 = _EqlDcbxAdminETSConTrafficClassGroupPri1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 19),
    _EqlDcbxAdminETSConTrafficClassGroupPri1_Type()
)
eqlDcbxAdminETSConTrafficClassGroupPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTrafficClassGroupPri1.setStatus("current")


class _EqlDcbxAdminETSConTrafficClassGroupPri2_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSConTrafficClassGroupPri2 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSConTrafficClassGroupPri2_Object = MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri2 = _EqlDcbxAdminETSConTrafficClassGroupPri2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 20),
    _EqlDcbxAdminETSConTrafficClassGroupPri2_Type()
)
eqlDcbxAdminETSConTrafficClassGroupPri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTrafficClassGroupPri2.setStatus("current")


class _EqlDcbxAdminETSConTrafficClassGroupPri3_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSConTrafficClassGroupPri3 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSConTrafficClassGroupPri3_Object = MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri3 = _EqlDcbxAdminETSConTrafficClassGroupPri3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 21),
    _EqlDcbxAdminETSConTrafficClassGroupPri3_Type()
)
eqlDcbxAdminETSConTrafficClassGroupPri3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTrafficClassGroupPri3.setStatus("current")


class _EqlDcbxAdminETSConTrafficClassGroupPri4_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSConTrafficClassGroupPri4 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSConTrafficClassGroupPri4_Object = MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri4 = _EqlDcbxAdminETSConTrafficClassGroupPri4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 22),
    _EqlDcbxAdminETSConTrafficClassGroupPri4_Type()
)
eqlDcbxAdminETSConTrafficClassGroupPri4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTrafficClassGroupPri4.setStatus("current")


class _EqlDcbxAdminETSConTrafficClassGroupPri5_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSConTrafficClassGroupPri5 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSConTrafficClassGroupPri5_Object = MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri5 = _EqlDcbxAdminETSConTrafficClassGroupPri5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 23),
    _EqlDcbxAdminETSConTrafficClassGroupPri5_Type()
)
eqlDcbxAdminETSConTrafficClassGroupPri5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTrafficClassGroupPri5.setStatus("current")


class _EqlDcbxAdminETSConTrafficClassGroupPri6_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSConTrafficClassGroupPri6 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSConTrafficClassGroupPri6_Object = MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri6 = _EqlDcbxAdminETSConTrafficClassGroupPri6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 24),
    _EqlDcbxAdminETSConTrafficClassGroupPri6_Type()
)
eqlDcbxAdminETSConTrafficClassGroupPri6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTrafficClassGroupPri6.setStatus("current")


class _EqlDcbxAdminETSConTrafficClassGroupPri7_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSConTrafficClassGroupPri7 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSConTrafficClassGroupPri7_Object = MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri7 = _EqlDcbxAdminETSConTrafficClassGroupPri7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 25),
    _EqlDcbxAdminETSConTrafficClassGroupPri7_Type()
)
eqlDcbxAdminETSConTrafficClassGroupPri7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTrafficClassGroupPri7.setStatus("current")


class _EqlDcbxAdminPFCEnableEnabledPri0_Type(TruthValue):
    """Custom type eqlDcbxAdminPFCEnableEnabledPri0 based on TruthValue"""


_EqlDcbxAdminPFCEnableEnabledPri0_Object = MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri0 = _EqlDcbxAdminPFCEnableEnabledPri0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 26),
    _EqlDcbxAdminPFCEnableEnabledPri0_Type()
)
eqlDcbxAdminPFCEnableEnabledPri0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminPFCEnableEnabledPri0.setStatus("current")


class _EqlDcbxAdminPFCEnableEnabledPri1_Type(TruthValue):
    """Custom type eqlDcbxAdminPFCEnableEnabledPri1 based on TruthValue"""


_EqlDcbxAdminPFCEnableEnabledPri1_Object = MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri1 = _EqlDcbxAdminPFCEnableEnabledPri1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 27),
    _EqlDcbxAdminPFCEnableEnabledPri1_Type()
)
eqlDcbxAdminPFCEnableEnabledPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminPFCEnableEnabledPri1.setStatus("current")


class _EqlDcbxAdminPFCEnableEnabledPri2_Type(TruthValue):
    """Custom type eqlDcbxAdminPFCEnableEnabledPri2 based on TruthValue"""


_EqlDcbxAdminPFCEnableEnabledPri2_Object = MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri2 = _EqlDcbxAdminPFCEnableEnabledPri2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 28),
    _EqlDcbxAdminPFCEnableEnabledPri2_Type()
)
eqlDcbxAdminPFCEnableEnabledPri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminPFCEnableEnabledPri2.setStatus("current")


class _EqlDcbxAdminPFCEnableEnabledPri3_Type(TruthValue):
    """Custom type eqlDcbxAdminPFCEnableEnabledPri3 based on TruthValue"""


_EqlDcbxAdminPFCEnableEnabledPri3_Object = MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri3 = _EqlDcbxAdminPFCEnableEnabledPri3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 29),
    _EqlDcbxAdminPFCEnableEnabledPri3_Type()
)
eqlDcbxAdminPFCEnableEnabledPri3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminPFCEnableEnabledPri3.setStatus("current")


class _EqlDcbxAdminPFCEnableEnabledPri4_Type(TruthValue):
    """Custom type eqlDcbxAdminPFCEnableEnabledPri4 based on TruthValue"""


_EqlDcbxAdminPFCEnableEnabledPri4_Object = MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri4 = _EqlDcbxAdminPFCEnableEnabledPri4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 30),
    _EqlDcbxAdminPFCEnableEnabledPri4_Type()
)
eqlDcbxAdminPFCEnableEnabledPri4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminPFCEnableEnabledPri4.setStatus("current")


class _EqlDcbxAdminPFCEnableEnabledPri5_Type(TruthValue):
    """Custom type eqlDcbxAdminPFCEnableEnabledPri5 based on TruthValue"""


_EqlDcbxAdminPFCEnableEnabledPri5_Object = MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri5 = _EqlDcbxAdminPFCEnableEnabledPri5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 31),
    _EqlDcbxAdminPFCEnableEnabledPri5_Type()
)
eqlDcbxAdminPFCEnableEnabledPri5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminPFCEnableEnabledPri5.setStatus("current")


class _EqlDcbxAdminPFCEnableEnabledPri6_Type(TruthValue):
    """Custom type eqlDcbxAdminPFCEnableEnabledPri6 based on TruthValue"""


_EqlDcbxAdminPFCEnableEnabledPri6_Object = MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri6 = _EqlDcbxAdminPFCEnableEnabledPri6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 32),
    _EqlDcbxAdminPFCEnableEnabledPri6_Type()
)
eqlDcbxAdminPFCEnableEnabledPri6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminPFCEnableEnabledPri6.setStatus("current")


class _EqlDcbxAdminPFCEnableEnabledPri7_Type(TruthValue):
    """Custom type eqlDcbxAdminPFCEnableEnabledPri7 based on TruthValue"""


_EqlDcbxAdminPFCEnableEnabledPri7_Object = MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri7 = _EqlDcbxAdminPFCEnableEnabledPri7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 33),
    _EqlDcbxAdminPFCEnableEnabledPri7_Type()
)
eqlDcbxAdminPFCEnableEnabledPri7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminPFCEnableEnabledPri7.setStatus("current")


class _EqlDcbxAdminAppPriorityiSCSITxEnable_Type(TruthValue):
    """Custom type eqlDcbxAdminAppPriorityiSCSITxEnable based on TruthValue"""


_EqlDcbxAdminAppPriorityiSCSITxEnable_Object = MibTableColumn
eqlDcbxAdminAppPriorityiSCSITxEnable = _EqlDcbxAdminAppPriorityiSCSITxEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 34),
    _EqlDcbxAdminAppPriorityiSCSITxEnable_Type()
)
eqlDcbxAdminAppPriorityiSCSITxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminAppPriorityiSCSITxEnable.setStatus("current")


class _EqlDcbxAdminAppPriorityiSCSIProtocol_Type(EqlDcbxAppProtocol):
    """Custom type eqlDcbxAdminAppPriorityiSCSIProtocol based on EqlDcbxAppProtocol"""
    defaultValue = 3260


_EqlDcbxAdminAppPriorityiSCSIProtocol_Object = MibTableColumn
eqlDcbxAdminAppPriorityiSCSIProtocol = _EqlDcbxAdminAppPriorityiSCSIProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 35),
    _EqlDcbxAdminAppPriorityiSCSIProtocol_Type()
)
eqlDcbxAdminAppPriorityiSCSIProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminAppPriorityiSCSIProtocol.setStatus("current")


class _EqlDcbxAdminAppPriorityiSCSIPriority_Type(EqlIEEE8021PriorityValue):
    """Custom type eqlDcbxAdminAppPriorityiSCSIPriority based on EqlIEEE8021PriorityValue"""
    defaultValue = 4


_EqlDcbxAdminAppPriorityiSCSIPriority_Object = MibTableColumn
eqlDcbxAdminAppPriorityiSCSIPriority = _EqlDcbxAdminAppPriorityiSCSIPriority_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 36),
    _EqlDcbxAdminAppPriorityiSCSIPriority_Type()
)
eqlDcbxAdminAppPriorityiSCSIPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminAppPriorityiSCSIPriority.setStatus("current")


class _EqlDcbxAdminAppPriorityFCoETxEnable_Type(TruthValue):
    """Custom type eqlDcbxAdminAppPriorityFCoETxEnable based on TruthValue"""


_EqlDcbxAdminAppPriorityFCoETxEnable_Object = MibTableColumn
eqlDcbxAdminAppPriorityFCoETxEnable = _EqlDcbxAdminAppPriorityFCoETxEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 37),
    _EqlDcbxAdminAppPriorityFCoETxEnable_Type()
)
eqlDcbxAdminAppPriorityFCoETxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminAppPriorityFCoETxEnable.setStatus("current")


class _EqlDcbxAdminAppPriorityFCoEProtocol_Type(EqlDcbxAppProtocol):
    """Custom type eqlDcbxAdminAppPriorityFCoEProtocol based on EqlDcbxAppProtocol"""
    defaultValue = 35078


_EqlDcbxAdminAppPriorityFCoEProtocol_Object = MibTableColumn
eqlDcbxAdminAppPriorityFCoEProtocol = _EqlDcbxAdminAppPriorityFCoEProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 38),
    _EqlDcbxAdminAppPriorityFCoEProtocol_Type()
)
eqlDcbxAdminAppPriorityFCoEProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminAppPriorityFCoEProtocol.setStatus("current")


class _EqlDcbxAdminAppPriorityFCoEPriority_Type(EqlIEEE8021PriorityValue):
    """Custom type eqlDcbxAdminAppPriorityFCoEPriority based on EqlIEEE8021PriorityValue"""
    defaultValue = 3


_EqlDcbxAdminAppPriorityFCoEPriority_Object = MibTableColumn
eqlDcbxAdminAppPriorityFCoEPriority = _EqlDcbxAdminAppPriorityFCoEPriority_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 39),
    _EqlDcbxAdminAppPriorityFCoEPriority_Type()
)
eqlDcbxAdminAppPriorityFCoEPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminAppPriorityFCoEPriority.setStatus("current")


class _EqlDcbxConfigDCBEnable_Type(TruthValue):
    """Custom type eqlDcbxConfigDCBEnable based on TruthValue"""


_EqlDcbxConfigDCBEnable_Object = MibTableColumn
eqlDcbxConfigDCBEnable = _EqlDcbxConfigDCBEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 40),
    _EqlDcbxConfigDCBEnable_Type()
)
eqlDcbxConfigDCBEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigDCBEnable.setStatus("current")


class _EqlDcbxConfigDCBX101Enable_Type(TruthValue):
    """Custom type eqlDcbxConfigDCBX101Enable based on TruthValue"""


_EqlDcbxConfigDCBX101Enable_Object = MibTableColumn
eqlDcbxConfigDCBX101Enable = _EqlDcbxConfigDCBX101Enable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 41),
    _EqlDcbxConfigDCBX101Enable_Type()
)
eqlDcbxConfigDCBX101Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigDCBX101Enable.setStatus("current")


class _EqlDcbxConfigDCBXIEEEDraftEnable_Type(TruthValue):
    """Custom type eqlDcbxConfigDCBXIEEEDraftEnable based on TruthValue"""


_EqlDcbxConfigDCBXIEEEDraftEnable_Object = MibTableColumn
eqlDcbxConfigDCBXIEEEDraftEnable = _EqlDcbxConfigDCBXIEEEDraftEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 42),
    _EqlDcbxConfigDCBXIEEEDraftEnable_Type()
)
eqlDcbxConfigDCBXIEEEDraftEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigDCBXIEEEDraftEnable.setStatus("current")


class _EqlDcbxConfigQcnSubtype_Type(EqlIEEEDraftSubtypeValue):
    """Custom type eqlDcbxConfigQcnSubtype based on EqlIEEEDraftSubtypeValue"""
    defaultValue = 8


_EqlDcbxConfigQcnSubtype_Object = MibTableColumn
eqlDcbxConfigQcnSubtype = _EqlDcbxConfigQcnSubtype_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 43),
    _EqlDcbxConfigQcnSubtype_Type()
)
eqlDcbxConfigQcnSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigQcnSubtype.setStatus("deprecated")


class _EqlDcbxConfigETSConSubtype_Type(EqlIEEEDraftSubtypeValue):
    """Custom type eqlDcbxConfigETSConSubtype based on EqlIEEEDraftSubtypeValue"""
    defaultValue = 9


_EqlDcbxConfigETSConSubtype_Object = MibTableColumn
eqlDcbxConfigETSConSubtype = _EqlDcbxConfigETSConSubtype_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 44),
    _EqlDcbxConfigETSConSubtype_Type()
)
eqlDcbxConfigETSConSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigETSConSubtype.setStatus("deprecated")


class _EqlDcbxConfigETSRecoSubtype_Type(EqlIEEEDraftSubtypeValue):
    """Custom type eqlDcbxConfigETSRecoSubtype based on EqlIEEEDraftSubtypeValue"""
    defaultValue = 10


_EqlDcbxConfigETSRecoSubtype_Object = MibTableColumn
eqlDcbxConfigETSRecoSubtype = _EqlDcbxConfigETSRecoSubtype_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 45),
    _EqlDcbxConfigETSRecoSubtype_Type()
)
eqlDcbxConfigETSRecoSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigETSRecoSubtype.setStatus("deprecated")


class _EqlDcbxConfigPFCSubtype_Type(EqlIEEEDraftSubtypeValue):
    """Custom type eqlDcbxConfigPFCSubtype based on EqlIEEEDraftSubtypeValue"""
    defaultValue = 11


_EqlDcbxConfigPFCSubtype_Object = MibTableColumn
eqlDcbxConfigPFCSubtype = _EqlDcbxConfigPFCSubtype_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 46),
    _EqlDcbxConfigPFCSubtype_Type()
)
eqlDcbxConfigPFCSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigPFCSubtype.setStatus("deprecated")


class _EqlDcbxConfigAppPrioritySubtype_Type(EqlIEEEDraftSubtypeValue):
    """Custom type eqlDcbxConfigAppPrioritySubtype based on EqlIEEEDraftSubtypeValue"""
    defaultValue = 12


_EqlDcbxConfigAppPrioritySubtype_Object = MibTableColumn
eqlDcbxConfigAppPrioritySubtype = _EqlDcbxConfigAppPrioritySubtype_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 47),
    _EqlDcbxConfigAppPrioritySubtype_Type()
)
eqlDcbxConfigAppPrioritySubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigAppPrioritySubtype.setStatus("deprecated")
_EqlDcbxConfigTCSupportedSubtype_Type = EqlIEEEDraftSubtypeValue
_EqlDcbxConfigTCSupportedSubtype_Object = MibTableColumn
eqlDcbxConfigTCSupportedSubtype = _EqlDcbxConfigTCSupportedSubtype_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 48),
    _EqlDcbxConfigTCSupportedSubtype_Type()
)
eqlDcbxConfigTCSupportedSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxConfigTCSupportedSubtype.setStatus("deprecated")


class _EqlDcbxAdminETSRecoTrafficClassGroupPri0_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSRecoTrafficClassGroupPri0 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSRecoTrafficClassGroupPri0_Object = MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri0 = _EqlDcbxAdminETSRecoTrafficClassGroupPri0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 49),
    _EqlDcbxAdminETSRecoTrafficClassGroupPri0_Type()
)
eqlDcbxAdminETSRecoTrafficClassGroupPri0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTrafficClassGroupPri0.setStatus("current")


class _EqlDcbxAdminETSRecoTrafficClassGroupPri1_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSRecoTrafficClassGroupPri1 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSRecoTrafficClassGroupPri1_Object = MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri1 = _EqlDcbxAdminETSRecoTrafficClassGroupPri1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 50),
    _EqlDcbxAdminETSRecoTrafficClassGroupPri1_Type()
)
eqlDcbxAdminETSRecoTrafficClassGroupPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTrafficClassGroupPri1.setStatus("current")


class _EqlDcbxAdminETSRecoTrafficClassGroupPri2_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSRecoTrafficClassGroupPri2 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSRecoTrafficClassGroupPri2_Object = MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri2 = _EqlDcbxAdminETSRecoTrafficClassGroupPri2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 51),
    _EqlDcbxAdminETSRecoTrafficClassGroupPri2_Type()
)
eqlDcbxAdminETSRecoTrafficClassGroupPri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTrafficClassGroupPri2.setStatus("current")


class _EqlDcbxAdminETSRecoTrafficClassGroupPri3_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSRecoTrafficClassGroupPri3 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSRecoTrafficClassGroupPri3_Object = MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri3 = _EqlDcbxAdminETSRecoTrafficClassGroupPri3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 52),
    _EqlDcbxAdminETSRecoTrafficClassGroupPri3_Type()
)
eqlDcbxAdminETSRecoTrafficClassGroupPri3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTrafficClassGroupPri3.setStatus("current")


class _EqlDcbxAdminETSRecoTrafficClassGroupPri4_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSRecoTrafficClassGroupPri4 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSRecoTrafficClassGroupPri4_Object = MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri4 = _EqlDcbxAdminETSRecoTrafficClassGroupPri4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 53),
    _EqlDcbxAdminETSRecoTrafficClassGroupPri4_Type()
)
eqlDcbxAdminETSRecoTrafficClassGroupPri4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTrafficClassGroupPri4.setStatus("current")


class _EqlDcbxAdminETSRecoTrafficClassGroupPri5_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSRecoTrafficClassGroupPri5 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSRecoTrafficClassGroupPri5_Object = MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri5 = _EqlDcbxAdminETSRecoTrafficClassGroupPri5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 54),
    _EqlDcbxAdminETSRecoTrafficClassGroupPri5_Type()
)
eqlDcbxAdminETSRecoTrafficClassGroupPri5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTrafficClassGroupPri5.setStatus("current")


class _EqlDcbxAdminETSRecoTrafficClassGroupPri6_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSRecoTrafficClassGroupPri6 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSRecoTrafficClassGroupPri6_Object = MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri6 = _EqlDcbxAdminETSRecoTrafficClassGroupPri6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 55),
    _EqlDcbxAdminETSRecoTrafficClassGroupPri6_Type()
)
eqlDcbxAdminETSRecoTrafficClassGroupPri6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTrafficClassGroupPri6.setStatus("current")


class _EqlDcbxAdminETSRecoTrafficClassGroupPri7_Type(EqlDcbxTrafficClassGroupValue):
    """Custom type eqlDcbxAdminETSRecoTrafficClassGroupPri7 based on EqlDcbxTrafficClassGroupValue"""
    defaultValue = 0


_EqlDcbxAdminETSRecoTrafficClassGroupPri7_Object = MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri7 = _EqlDcbxAdminETSRecoTrafficClassGroupPri7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 56),
    _EqlDcbxAdminETSRecoTrafficClassGroupPri7_Type()
)
eqlDcbxAdminETSRecoTrafficClassGroupPri7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTrafficClassGroupPri7.setStatus("current")


class _EqlDcbCnGlobalMasterEnable_Type(TruthValue):
    """Custom type eqlDcbCnGlobalMasterEnable based on TruthValue"""


_EqlDcbCnGlobalMasterEnable_Object = MibTableColumn
eqlDcbCnGlobalMasterEnable = _EqlDcbCnGlobalMasterEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 57),
    _EqlDcbCnGlobalMasterEnable_Type()
)
eqlDcbCnGlobalMasterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnGlobalMasterEnable.setStatus("current")


class _EqlDcbCnRpPortPriMaxRps_Type(Unsigned32):
    """Custom type eqlDcbCnRpPortPriMaxRps based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqlDcbCnRpPortPriMaxRps_Type.__name__ = "Unsigned32"
_EqlDcbCnRpPortPriMaxRps_Object = MibTableColumn
eqlDcbCnRpPortPriMaxRps = _EqlDcbCnRpPortPriMaxRps_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 58),
    _EqlDcbCnRpPortPriMaxRps_Type()
)
eqlDcbCnRpPortPriMaxRps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriMaxRps.setStatus("current")


class _EqlDcbCnRpgEnablePri0_Type(TruthValue):
    """Custom type eqlDcbCnRpgEnablePri0 based on TruthValue"""


_EqlDcbCnRpgEnablePri0_Object = MibTableColumn
eqlDcbCnRpgEnablePri0 = _EqlDcbCnRpgEnablePri0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 59),
    _EqlDcbCnRpgEnablePri0_Type()
)
eqlDcbCnRpgEnablePri0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgEnablePri0.setStatus("current")


class _EqlDcbCnRpgEnablePri1_Type(TruthValue):
    """Custom type eqlDcbCnRpgEnablePri1 based on TruthValue"""


_EqlDcbCnRpgEnablePri1_Object = MibTableColumn
eqlDcbCnRpgEnablePri1 = _EqlDcbCnRpgEnablePri1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 60),
    _EqlDcbCnRpgEnablePri1_Type()
)
eqlDcbCnRpgEnablePri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgEnablePri1.setStatus("current")


class _EqlDcbCnRpgEnablePri2_Type(TruthValue):
    """Custom type eqlDcbCnRpgEnablePri2 based on TruthValue"""


_EqlDcbCnRpgEnablePri2_Object = MibTableColumn
eqlDcbCnRpgEnablePri2 = _EqlDcbCnRpgEnablePri2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 61),
    _EqlDcbCnRpgEnablePri2_Type()
)
eqlDcbCnRpgEnablePri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgEnablePri2.setStatus("current")


class _EqlDcbCnRpgEnablePri3_Type(TruthValue):
    """Custom type eqlDcbCnRpgEnablePri3 based on TruthValue"""


_EqlDcbCnRpgEnablePri3_Object = MibTableColumn
eqlDcbCnRpgEnablePri3 = _EqlDcbCnRpgEnablePri3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 62),
    _EqlDcbCnRpgEnablePri3_Type()
)
eqlDcbCnRpgEnablePri3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgEnablePri3.setStatus("current")


class _EqlDcbCnRpgEnablePri4_Type(TruthValue):
    """Custom type eqlDcbCnRpgEnablePri4 based on TruthValue"""


_EqlDcbCnRpgEnablePri4_Object = MibTableColumn
eqlDcbCnRpgEnablePri4 = _EqlDcbCnRpgEnablePri4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 63),
    _EqlDcbCnRpgEnablePri4_Type()
)
eqlDcbCnRpgEnablePri4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgEnablePri4.setStatus("current")


class _EqlDcbCnRpgEnablePri5_Type(TruthValue):
    """Custom type eqlDcbCnRpgEnablePri5 based on TruthValue"""


_EqlDcbCnRpgEnablePri5_Object = MibTableColumn
eqlDcbCnRpgEnablePri5 = _EqlDcbCnRpgEnablePri5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 64),
    _EqlDcbCnRpgEnablePri5_Type()
)
eqlDcbCnRpgEnablePri5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgEnablePri5.setStatus("current")


class _EqlDcbCnRpgEnablePri6_Type(TruthValue):
    """Custom type eqlDcbCnRpgEnablePri6 based on TruthValue"""


_EqlDcbCnRpgEnablePri6_Object = MibTableColumn
eqlDcbCnRpgEnablePri6 = _EqlDcbCnRpgEnablePri6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 65),
    _EqlDcbCnRpgEnablePri6_Type()
)
eqlDcbCnRpgEnablePri6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgEnablePri6.setStatus("current")


class _EqlDcbCnRpgEnablePri7_Type(TruthValue):
    """Custom type eqlDcbCnRpgEnablePri7 based on TruthValue"""


_EqlDcbCnRpgEnablePri7_Object = MibTableColumn
eqlDcbCnRpgEnablePri7 = _EqlDcbCnRpgEnablePri7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 66),
    _EqlDcbCnRpgEnablePri7_Type()
)
eqlDcbCnRpgEnablePri7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgEnablePri7.setStatus("current")


class _EqlDcbCnRpgTimeReset_Type(TimeInterval):
    """Custom type eqlDcbCnRpgTimeReset based on TimeInterval"""
    defaultValue = 15


_EqlDcbCnRpgTimeReset_Object = MibTableColumn
eqlDcbCnRpgTimeReset = _EqlDcbCnRpgTimeReset_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 67),
    _EqlDcbCnRpgTimeReset_Type()
)
eqlDcbCnRpgTimeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgTimeReset.setStatus("current")
if mibBuilder.loadTexts:
    eqlDcbCnRpgTimeReset.setUnits("milliseconds")


class _EqlDcbCnRpgByteReset_Type(Unsigned32):
    """Custom type eqlDcbCnRpgByteReset based on Unsigned32"""
    defaultValue = 150000


_EqlDcbCnRpgByteReset_Object = MibTableColumn
eqlDcbCnRpgByteReset = _EqlDcbCnRpgByteReset_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 68),
    _EqlDcbCnRpgByteReset_Type()
)
eqlDcbCnRpgByteReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgByteReset.setStatus("current")
if mibBuilder.loadTexts:
    eqlDcbCnRpgByteReset.setUnits("octets")


class _EqlDcbCnRpgThreshold_Type(Unsigned32):
    """Custom type eqlDcbCnRpgThreshold based on Unsigned32"""
    defaultValue = 5


_EqlDcbCnRpgThreshold_Object = MibTableColumn
eqlDcbCnRpgThreshold = _EqlDcbCnRpgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 69),
    _EqlDcbCnRpgThreshold_Type()
)
eqlDcbCnRpgThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgThreshold.setStatus("current")


class _EqlDcbCnRpgMaxRate_Type(Unsigned32):
    """Custom type eqlDcbCnRpgMaxRate based on Unsigned32"""
    defaultValue = 10000


_EqlDcbCnRpgMaxRate_Object = MibTableColumn
eqlDcbCnRpgMaxRate = _EqlDcbCnRpgMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 70),
    _EqlDcbCnRpgMaxRate_Type()
)
eqlDcbCnRpgMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    eqlDcbCnRpgMaxRate.setUnits("Mbit/s")


class _EqlDcbCnRpgAiRate_Type(Unsigned32):
    """Custom type eqlDcbCnRpgAiRate based on Unsigned32"""
    defaultValue = 5


_EqlDcbCnRpgAiRate_Object = MibTableColumn
eqlDcbCnRpgAiRate = _EqlDcbCnRpgAiRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 71),
    _EqlDcbCnRpgAiRate_Type()
)
eqlDcbCnRpgAiRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgAiRate.setStatus("current")
if mibBuilder.loadTexts:
    eqlDcbCnRpgAiRate.setUnits("Mbit/s")


class _EqlDcbCnRpgHaiRate_Type(Unsigned32):
    """Custom type eqlDcbCnRpgHaiRate based on Unsigned32"""
    defaultValue = 50


_EqlDcbCnRpgHaiRate_Object = MibTableColumn
eqlDcbCnRpgHaiRate = _EqlDcbCnRpgHaiRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 72),
    _EqlDcbCnRpgHaiRate_Type()
)
eqlDcbCnRpgHaiRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgHaiRate.setStatus("current")
if mibBuilder.loadTexts:
    eqlDcbCnRpgHaiRate.setUnits("Mbit/s")


class _EqlDcbCnRpgGd_Type(Integer32):
    """Custom type eqlDcbCnRpgGd based on Integer32"""
    defaultValue = 7


_EqlDcbCnRpgGd_Object = MibTableColumn
eqlDcbCnRpgGd = _EqlDcbCnRpgGd_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 73),
    _EqlDcbCnRpgGd_Type()
)
eqlDcbCnRpgGd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgGd.setStatus("current")


class _EqlDcbCnRpgMinDecFac_Type(Unsigned32):
    """Custom type eqlDcbCnRpgMinDecFac based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqlDcbCnRpgMinDecFac_Type.__name__ = "Unsigned32"
_EqlDcbCnRpgMinDecFac_Object = MibTableColumn
eqlDcbCnRpgMinDecFac = _EqlDcbCnRpgMinDecFac_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 74),
    _EqlDcbCnRpgMinDecFac_Type()
)
eqlDcbCnRpgMinDecFac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgMinDecFac.setStatus("current")
if mibBuilder.loadTexts:
    eqlDcbCnRpgMinDecFac.setUnits("percent")


class _EqlDcbCnRpgMinRate_Type(Unsigned32):
    """Custom type eqlDcbCnRpgMinRate based on Unsigned32"""
    defaultValue = 5


_EqlDcbCnRpgMinRate_Object = MibTableColumn
eqlDcbCnRpgMinRate = _EqlDcbCnRpgMinRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 75),
    _EqlDcbCnRpgMinRate_Type()
)
eqlDcbCnRpgMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbCnRpgMinRate.setStatus("current")
if mibBuilder.loadTexts:
    eqlDcbCnRpgMinRate.setUnits("Mbit/s")


class _EqlDcbDefaultiSCSIPriority_Type(EqlIEEE8021PriorityValue):
    """Custom type eqlDcbDefaultiSCSIPriority based on EqlIEEE8021PriorityValue"""
    defaultValue = 0


_EqlDcbDefaultiSCSIPriority_Object = MibTableColumn
eqlDcbDefaultiSCSIPriority = _EqlDcbDefaultiSCSIPriority_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 76),
    _EqlDcbDefaultiSCSIPriority_Type()
)
eqlDcbDefaultiSCSIPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbDefaultiSCSIPriority.setStatus("current")


class _EqlDcbDefaultFCoEPriority_Type(EqlIEEE8021PriorityValue):
    """Custom type eqlDcbDefaultFCoEPriority based on EqlIEEE8021PriorityValue"""
    defaultValue = 0


_EqlDcbDefaultFCoEPriority_Object = MibTableColumn
eqlDcbDefaultFCoEPriority = _EqlDcbDefaultFCoEPriority_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 77),
    _EqlDcbDefaultFCoEPriority_Type()
)
eqlDcbDefaultFCoEPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbDefaultFCoEPriority.setStatus("current")


class _EqlDcbxAdminETSConTsaTc0_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSConTsaTc0 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSConTsaTc0_Object = MibTableColumn
eqlDcbxAdminETSConTsaTc0 = _EqlDcbxAdminETSConTsaTc0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 78),
    _EqlDcbxAdminETSConTsaTc0_Type()
)
eqlDcbxAdminETSConTsaTc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTsaTc0.setStatus("current")


class _EqlDcbxAdminETSConTsaTc1_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSConTsaTc1 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSConTsaTc1_Object = MibTableColumn
eqlDcbxAdminETSConTsaTc1 = _EqlDcbxAdminETSConTsaTc1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 79),
    _EqlDcbxAdminETSConTsaTc1_Type()
)
eqlDcbxAdminETSConTsaTc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTsaTc1.setStatus("current")


class _EqlDcbxAdminETSConTsaTc2_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSConTsaTc2 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSConTsaTc2_Object = MibTableColumn
eqlDcbxAdminETSConTsaTc2 = _EqlDcbxAdminETSConTsaTc2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 80),
    _EqlDcbxAdminETSConTsaTc2_Type()
)
eqlDcbxAdminETSConTsaTc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTsaTc2.setStatus("current")


class _EqlDcbxAdminETSConTsaTc3_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSConTsaTc3 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSConTsaTc3_Object = MibTableColumn
eqlDcbxAdminETSConTsaTc3 = _EqlDcbxAdminETSConTsaTc3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 81),
    _EqlDcbxAdminETSConTsaTc3_Type()
)
eqlDcbxAdminETSConTsaTc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTsaTc3.setStatus("current")


class _EqlDcbxAdminETSConTsaTc4_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSConTsaTc4 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSConTsaTc4_Object = MibTableColumn
eqlDcbxAdminETSConTsaTc4 = _EqlDcbxAdminETSConTsaTc4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 82),
    _EqlDcbxAdminETSConTsaTc4_Type()
)
eqlDcbxAdminETSConTsaTc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTsaTc4.setStatus("current")


class _EqlDcbxAdminETSConTsaTc5_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSConTsaTc5 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSConTsaTc5_Object = MibTableColumn
eqlDcbxAdminETSConTsaTc5 = _EqlDcbxAdminETSConTsaTc5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 83),
    _EqlDcbxAdminETSConTsaTc5_Type()
)
eqlDcbxAdminETSConTsaTc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTsaTc5.setStatus("current")


class _EqlDcbxAdminETSConTsaTc6_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSConTsaTc6 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSConTsaTc6_Object = MibTableColumn
eqlDcbxAdminETSConTsaTc6 = _EqlDcbxAdminETSConTsaTc6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 84),
    _EqlDcbxAdminETSConTsaTc6_Type()
)
eqlDcbxAdminETSConTsaTc6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTsaTc6.setStatus("current")


class _EqlDcbxAdminETSConTsaTc7_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSConTsaTc7 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSConTsaTc7_Object = MibTableColumn
eqlDcbxAdminETSConTsaTc7 = _EqlDcbxAdminETSConTsaTc7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 85),
    _EqlDcbxAdminETSConTsaTc7_Type()
)
eqlDcbxAdminETSConTsaTc7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSConTsaTc7.setStatus("current")


class _EqlDcbxAdminETSRecoTsaTc0_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSRecoTsaTc0 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSRecoTsaTc0_Object = MibTableColumn
eqlDcbxAdminETSRecoTsaTc0 = _EqlDcbxAdminETSRecoTsaTc0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 86),
    _EqlDcbxAdminETSRecoTsaTc0_Type()
)
eqlDcbxAdminETSRecoTsaTc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTsaTc0.setStatus("current")


class _EqlDcbxAdminETSRecoTsaTc1_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSRecoTsaTc1 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSRecoTsaTc1_Object = MibTableColumn
eqlDcbxAdminETSRecoTsaTc1 = _EqlDcbxAdminETSRecoTsaTc1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 87),
    _EqlDcbxAdminETSRecoTsaTc1_Type()
)
eqlDcbxAdminETSRecoTsaTc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTsaTc1.setStatus("current")


class _EqlDcbxAdminETSRecoTsaTc2_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSRecoTsaTc2 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSRecoTsaTc2_Object = MibTableColumn
eqlDcbxAdminETSRecoTsaTc2 = _EqlDcbxAdminETSRecoTsaTc2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 88),
    _EqlDcbxAdminETSRecoTsaTc2_Type()
)
eqlDcbxAdminETSRecoTsaTc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTsaTc2.setStatus("current")


class _EqlDcbxAdminETSRecoTsaTc3_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSRecoTsaTc3 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSRecoTsaTc3_Object = MibTableColumn
eqlDcbxAdminETSRecoTsaTc3 = _EqlDcbxAdminETSRecoTsaTc3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 89),
    _EqlDcbxAdminETSRecoTsaTc3_Type()
)
eqlDcbxAdminETSRecoTsaTc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTsaTc3.setStatus("current")


class _EqlDcbxAdminETSRecoTsaTc4_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSRecoTsaTc4 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSRecoTsaTc4_Object = MibTableColumn
eqlDcbxAdminETSRecoTsaTc4 = _EqlDcbxAdminETSRecoTsaTc4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 90),
    _EqlDcbxAdminETSRecoTsaTc4_Type()
)
eqlDcbxAdminETSRecoTsaTc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTsaTc4.setStatus("current")


class _EqlDcbxAdminETSRecoTsaTc5_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSRecoTsaTc5 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSRecoTsaTc5_Object = MibTableColumn
eqlDcbxAdminETSRecoTsaTc5 = _EqlDcbxAdminETSRecoTsaTc5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 91),
    _EqlDcbxAdminETSRecoTsaTc5_Type()
)
eqlDcbxAdminETSRecoTsaTc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTsaTc5.setStatus("current")


class _EqlDcbxAdminETSRecoTsaTc6_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSRecoTsaTc6 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSRecoTsaTc6_Object = MibTableColumn
eqlDcbxAdminETSRecoTsaTc6 = _EqlDcbxAdminETSRecoTsaTc6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 92),
    _EqlDcbxAdminETSRecoTsaTc6_Type()
)
eqlDcbxAdminETSRecoTsaTc6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTsaTc6.setStatus("current")


class _EqlDcbxAdminETSRecoTsaTc7_Type(EqlDcbxTransmissionSelectionAlgorithm):
    """Custom type eqlDcbxAdminETSRecoTsaTc7 based on EqlDcbxTransmissionSelectionAlgorithm"""


_EqlDcbxAdminETSRecoTsaTc7_Object = MibTableColumn
eqlDcbxAdminETSRecoTsaTc7 = _EqlDcbxAdminETSRecoTsaTc7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 1, 1, 93),
    _EqlDcbxAdminETSRecoTsaTc7_Type()
)
eqlDcbxAdminETSRecoTsaTc7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDcbxAdminETSRecoTsaTc7.setStatus("current")
_EqlDcbDynamicIfTable_Object = MibTable
eqlDcbDynamicIfTable = _EqlDcbDynamicIfTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2)
)
if mibBuilder.loadTexts:
    eqlDcbDynamicIfTable.setStatus("current")
_EqlDcbDynamicIfEntry_Object = MibTableRow
eqlDcbDynamicIfEntry = _EqlDcbDynamicIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1)
)
eqlDcbDynamicIfEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eqlDcbDynamicIfEntry.setStatus("current")
_EqlDcbPfcRequestsSent_Type = Counter32
_EqlDcbPfcRequestsSent_Object = MibTableColumn
eqlDcbPfcRequestsSent = _EqlDcbPfcRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 1),
    _EqlDcbPfcRequestsSent_Type()
)
eqlDcbPfcRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbPfcRequestsSent.setStatus("current")
_EqlDcbPfcIndicationsReceived_Type = Counter32
_EqlDcbPfcIndicationsReceived_Object = MibTableColumn
eqlDcbPfcIndicationsReceived = _EqlDcbPfcIndicationsReceived_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 2),
    _EqlDcbPfcIndicationsReceived_Type()
)
eqlDcbPfcIndicationsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbPfcIndicationsReceived.setStatus("current")
_EqlDcbxLocTCSupported_Type = EqlDcbxSupportedCapacity
_EqlDcbxLocTCSupported_Object = MibTableColumn
eqlDcbxLocTCSupported = _EqlDcbxLocTCSupported_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 3),
    _EqlDcbxLocTCSupported_Type()
)
eqlDcbxLocTCSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocTCSupported.setStatus("deprecated")
_EqlDcbxLocETSConMaxTCG_Type = EqlDcbxSupportedCapacity
_EqlDcbxLocETSConMaxTCG_Object = MibTableColumn
eqlDcbxLocETSConMaxTCG = _EqlDcbxLocETSConMaxTCG_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 4),
    _EqlDcbxLocETSConMaxTCG_Type()
)
eqlDcbxLocETSConMaxTCG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConMaxTCG.setStatus("current")
_EqlDcbxLocETSConWilling_Type = TruthValue
_EqlDcbxLocETSConWilling_Object = MibTableColumn
eqlDcbxLocETSConWilling = _EqlDcbxLocETSConWilling_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 5),
    _EqlDcbxLocETSConWilling_Type()
)
eqlDcbxLocETSConWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConWilling.setStatus("current")


class _EqlDcbxLocETSConTrafficClassGroupBandwidthTable_Type(OctetString):
    """Custom type eqlDcbxLocETSConTrafficClassGroupBandwidthTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EqlDcbxLocETSConTrafficClassGroupBandwidthTable_Type.__name__ = "OctetString"
_EqlDcbxLocETSConTrafficClassGroupBandwidthTable_Object = MibTableColumn
eqlDcbxLocETSConTrafficClassGroupBandwidthTable = _EqlDcbxLocETSConTrafficClassGroupBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 6),
    _EqlDcbxLocETSConTrafficClassGroupBandwidthTable_Type()
)
eqlDcbxLocETSConTrafficClassGroupBandwidthTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTrafficClassGroupBandwidthTable.setStatus("current")


class _EqlDcbxLocETSRecoTrafficClassGroupBandwidthTable_Type(OctetString):
    """Custom type eqlDcbxLocETSRecoTrafficClassGroupBandwidthTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EqlDcbxLocETSRecoTrafficClassGroupBandwidthTable_Type.__name__ = "OctetString"
_EqlDcbxLocETSRecoTrafficClassGroupBandwidthTable_Object = MibTableColumn
eqlDcbxLocETSRecoTrafficClassGroupBandwidthTable = _EqlDcbxLocETSRecoTrafficClassGroupBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 7),
    _EqlDcbxLocETSRecoTrafficClassGroupBandwidthTable_Type()
)
eqlDcbxLocETSRecoTrafficClassGroupBandwidthTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSRecoTrafficClassGroupBandwidthTable.setStatus("current")
_EqlDcbxLocPFCWilling_Type = TruthValue
_EqlDcbxLocPFCWilling_Object = MibTableColumn
eqlDcbxLocPFCWilling = _EqlDcbxLocPFCWilling_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 8),
    _EqlDcbxLocPFCWilling_Type()
)
eqlDcbxLocPFCWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPFCWilling.setStatus("current")
_EqlDcbxLocPFCMBC_Type = TruthValue
_EqlDcbxLocPFCMBC_Object = MibTableColumn
eqlDcbxLocPFCMBC = _EqlDcbxLocPFCMBC_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 9),
    _EqlDcbxLocPFCMBC_Type()
)
eqlDcbxLocPFCMBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPFCMBC.setStatus("current")
_EqlDcbxLocPFCCap_Type = EqlDcbxSupportedCapacity
_EqlDcbxLocPFCCap_Object = MibTableColumn
eqlDcbxLocPFCCap = _EqlDcbxLocPFCCap_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 10),
    _EqlDcbxLocPFCCap_Type()
)
eqlDcbxLocPFCCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPFCCap.setStatus("current")
_EqlDcbxLocAppPriorityWilling_Type = TruthValue
_EqlDcbxLocAppPriorityWilling_Object = MibTableColumn
eqlDcbxLocAppPriorityWilling = _EqlDcbxLocAppPriorityWilling_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 11),
    _EqlDcbxLocAppPriorityWilling_Type()
)
eqlDcbxLocAppPriorityWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocAppPriorityWilling.setStatus("current")
_EqlDcbxRemTCSupported_Type = EqlDcbxSupportedCapacity
_EqlDcbxRemTCSupported_Object = MibTableColumn
eqlDcbxRemTCSupported = _EqlDcbxRemTCSupported_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 12),
    _EqlDcbxRemTCSupported_Type()
)
eqlDcbxRemTCSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemTCSupported.setStatus("deprecated")
_EqlDcbxRemETSConMaxTCG_Type = EqlDcbxSupportedCapacity
_EqlDcbxRemETSConMaxTCG_Object = MibTableColumn
eqlDcbxRemETSConMaxTCG = _EqlDcbxRemETSConMaxTCG_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 13),
    _EqlDcbxRemETSConMaxTCG_Type()
)
eqlDcbxRemETSConMaxTCG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSConMaxTCG.setStatus("current")
_EqlDcbxRemETSConWilling_Type = TruthValue
_EqlDcbxRemETSConWilling_Object = MibTableColumn
eqlDcbxRemETSConWilling = _EqlDcbxRemETSConWilling_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 14),
    _EqlDcbxRemETSConWilling_Type()
)
eqlDcbxRemETSConWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSConWilling.setStatus("current")


class _EqlDcbxRemETSConTrafficClassGroupBandwidthTable_Type(OctetString):
    """Custom type eqlDcbxRemETSConTrafficClassGroupBandwidthTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EqlDcbxRemETSConTrafficClassGroupBandwidthTable_Type.__name__ = "OctetString"
_EqlDcbxRemETSConTrafficClassGroupBandwidthTable_Object = MibTableColumn
eqlDcbxRemETSConTrafficClassGroupBandwidthTable = _EqlDcbxRemETSConTrafficClassGroupBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 15),
    _EqlDcbxRemETSConTrafficClassGroupBandwidthTable_Type()
)
eqlDcbxRemETSConTrafficClassGroupBandwidthTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSConTrafficClassGroupBandwidthTable.setStatus("current")


class _EqlDcbxRemETSRecoTrafficClassGroupBandwidthTable_Type(OctetString):
    """Custom type eqlDcbxRemETSRecoTrafficClassGroupBandwidthTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EqlDcbxRemETSRecoTrafficClassGroupBandwidthTable_Type.__name__ = "OctetString"
_EqlDcbxRemETSRecoTrafficClassGroupBandwidthTable_Object = MibTableColumn
eqlDcbxRemETSRecoTrafficClassGroupBandwidthTable = _EqlDcbxRemETSRecoTrafficClassGroupBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 16),
    _EqlDcbxRemETSRecoTrafficClassGroupBandwidthTable_Type()
)
eqlDcbxRemETSRecoTrafficClassGroupBandwidthTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSRecoTrafficClassGroupBandwidthTable.setStatus("current")
_EqlDcbxRemPFCWilling_Type = TruthValue
_EqlDcbxRemPFCWilling_Object = MibTableColumn
eqlDcbxRemPFCWilling = _EqlDcbxRemPFCWilling_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 17),
    _EqlDcbxRemPFCWilling_Type()
)
eqlDcbxRemPFCWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemPFCWilling.setStatus("current")
_EqlDcbxRemPFCMBC_Type = TruthValue
_EqlDcbxRemPFCMBC_Object = MibTableColumn
eqlDcbxRemPFCMBC = _EqlDcbxRemPFCMBC_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 18),
    _EqlDcbxRemPFCMBC_Type()
)
eqlDcbxRemPFCMBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemPFCMBC.setStatus("current")
_EqlDcbxRemPFCCap_Type = EqlDcbxSupportedCapacity
_EqlDcbxRemPFCCap_Object = MibTableColumn
eqlDcbxRemPFCCap = _EqlDcbxRemPFCCap_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 19),
    _EqlDcbxRemPFCCap_Type()
)
eqlDcbxRemPFCCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemPFCCap.setStatus("current")
_EqlDcbxRemAppPriorityWilling_Type = TruthValue
_EqlDcbxRemAppPriorityWilling_Object = MibTableColumn
eqlDcbxRemAppPriorityWilling = _EqlDcbxRemAppPriorityWilling_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 20),
    _EqlDcbxRemAppPriorityWilling_Type()
)
eqlDcbxRemAppPriorityWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemAppPriorityWilling.setStatus("current")
_EqlDcbxLocETSConTrafficClassGroupPri0_Type = EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri0_Object = MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri0 = _EqlDcbxLocETSConTrafficClassGroupPri0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 21),
    _EqlDcbxLocETSConTrafficClassGroupPri0_Type()
)
eqlDcbxLocETSConTrafficClassGroupPri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTrafficClassGroupPri0.setStatus("current")
_EqlDcbxLocETSConTrafficClassGroupPri1_Type = EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri1_Object = MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri1 = _EqlDcbxLocETSConTrafficClassGroupPri1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 22),
    _EqlDcbxLocETSConTrafficClassGroupPri1_Type()
)
eqlDcbxLocETSConTrafficClassGroupPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTrafficClassGroupPri1.setStatus("current")
_EqlDcbxLocETSConTrafficClassGroupPri2_Type = EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri2_Object = MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri2 = _EqlDcbxLocETSConTrafficClassGroupPri2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 23),
    _EqlDcbxLocETSConTrafficClassGroupPri2_Type()
)
eqlDcbxLocETSConTrafficClassGroupPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTrafficClassGroupPri2.setStatus("current")
_EqlDcbxLocETSConTrafficClassGroupPri3_Type = EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri3_Object = MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri3 = _EqlDcbxLocETSConTrafficClassGroupPri3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 24),
    _EqlDcbxLocETSConTrafficClassGroupPri3_Type()
)
eqlDcbxLocETSConTrafficClassGroupPri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTrafficClassGroupPri3.setStatus("current")
_EqlDcbxLocETSConTrafficClassGroupPri4_Type = EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri4_Object = MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri4 = _EqlDcbxLocETSConTrafficClassGroupPri4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 25),
    _EqlDcbxLocETSConTrafficClassGroupPri4_Type()
)
eqlDcbxLocETSConTrafficClassGroupPri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTrafficClassGroupPri4.setStatus("current")
_EqlDcbxLocETSConTrafficClassGroupPri5_Type = EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri5_Object = MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri5 = _EqlDcbxLocETSConTrafficClassGroupPri5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 26),
    _EqlDcbxLocETSConTrafficClassGroupPri5_Type()
)
eqlDcbxLocETSConTrafficClassGroupPri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTrafficClassGroupPri5.setStatus("current")
_EqlDcbxLocETSConTrafficClassGroupPri6_Type = EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri6_Object = MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri6 = _EqlDcbxLocETSConTrafficClassGroupPri6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 27),
    _EqlDcbxLocETSConTrafficClassGroupPri6_Type()
)
eqlDcbxLocETSConTrafficClassGroupPri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTrafficClassGroupPri6.setStatus("current")
_EqlDcbxLocETSConTrafficClassGroupPri7_Type = EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri7_Object = MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri7 = _EqlDcbxLocETSConTrafficClassGroupPri7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 28),
    _EqlDcbxLocETSConTrafficClassGroupPri7_Type()
)
eqlDcbxLocETSConTrafficClassGroupPri7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTrafficClassGroupPri7.setStatus("current")
_EqlDcbxLocPFCEnableEnabledPri0_Type = TruthValue
_EqlDcbxLocPFCEnableEnabledPri0_Object = MibTableColumn
eqlDcbxLocPFCEnableEnabledPri0 = _EqlDcbxLocPFCEnableEnabledPri0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 29),
    _EqlDcbxLocPFCEnableEnabledPri0_Type()
)
eqlDcbxLocPFCEnableEnabledPri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPFCEnableEnabledPri0.setStatus("current")
_EqlDcbxLocPFCEnableEnabledPri1_Type = TruthValue
_EqlDcbxLocPFCEnableEnabledPri1_Object = MibTableColumn
eqlDcbxLocPFCEnableEnabledPri1 = _EqlDcbxLocPFCEnableEnabledPri1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 30),
    _EqlDcbxLocPFCEnableEnabledPri1_Type()
)
eqlDcbxLocPFCEnableEnabledPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPFCEnableEnabledPri1.setStatus("current")
_EqlDcbxLocPFCEnableEnabledPri2_Type = TruthValue
_EqlDcbxLocPFCEnableEnabledPri2_Object = MibTableColumn
eqlDcbxLocPFCEnableEnabledPri2 = _EqlDcbxLocPFCEnableEnabledPri2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 31),
    _EqlDcbxLocPFCEnableEnabledPri2_Type()
)
eqlDcbxLocPFCEnableEnabledPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPFCEnableEnabledPri2.setStatus("current")
_EqlDcbxLocPFCEnableEnabledPri3_Type = TruthValue
_EqlDcbxLocPFCEnableEnabledPri3_Object = MibTableColumn
eqlDcbxLocPFCEnableEnabledPri3 = _EqlDcbxLocPFCEnableEnabledPri3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 32),
    _EqlDcbxLocPFCEnableEnabledPri3_Type()
)
eqlDcbxLocPFCEnableEnabledPri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPFCEnableEnabledPri3.setStatus("current")
_EqlDcbxLocPFCEnableEnabledPri4_Type = TruthValue
_EqlDcbxLocPFCEnableEnabledPri4_Object = MibTableColumn
eqlDcbxLocPFCEnableEnabledPri4 = _EqlDcbxLocPFCEnableEnabledPri4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 33),
    _EqlDcbxLocPFCEnableEnabledPri4_Type()
)
eqlDcbxLocPFCEnableEnabledPri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPFCEnableEnabledPri4.setStatus("current")
_EqlDcbxLocPFCEnableEnabledPri5_Type = TruthValue
_EqlDcbxLocPFCEnableEnabledPri5_Object = MibTableColumn
eqlDcbxLocPFCEnableEnabledPri5 = _EqlDcbxLocPFCEnableEnabledPri5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 34),
    _EqlDcbxLocPFCEnableEnabledPri5_Type()
)
eqlDcbxLocPFCEnableEnabledPri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPFCEnableEnabledPri5.setStatus("current")
_EqlDcbxLocPFCEnableEnabledPri6_Type = TruthValue
_EqlDcbxLocPFCEnableEnabledPri6_Object = MibTableColumn
eqlDcbxLocPFCEnableEnabledPri6 = _EqlDcbxLocPFCEnableEnabledPri6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 35),
    _EqlDcbxLocPFCEnableEnabledPri6_Type()
)
eqlDcbxLocPFCEnableEnabledPri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPFCEnableEnabledPri6.setStatus("current")
_EqlDcbxLocPFCEnableEnabledPri7_Type = TruthValue
_EqlDcbxLocPFCEnableEnabledPri7_Object = MibTableColumn
eqlDcbxLocPFCEnableEnabledPri7 = _EqlDcbxLocPFCEnableEnabledPri7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 36),
    _EqlDcbxLocPFCEnableEnabledPri7_Type()
)
eqlDcbxLocPFCEnableEnabledPri7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPFCEnableEnabledPri7.setStatus("current")
_EqlDcbxLocVLANId_Type = EqlVlanIdentifier
_EqlDcbxLocVLANId_Object = MibTableColumn
eqlDcbxLocVLANId = _EqlDcbxLocVLANId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 37),
    _EqlDcbxLocVLANId_Type()
)
eqlDcbxLocVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocVLANId.setStatus("current")
_EqlDcbxLocVLANState_Type = EqlDcbxVlanState
_EqlDcbxLocVLANState_Object = MibTableColumn
eqlDcbxLocVLANState = _EqlDcbxLocVLANState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 38),
    _EqlDcbxLocVLANState_Type()
)
eqlDcbxLocVLANState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocVLANState.setStatus("current")
_EqlDcbxLocDCBState_Type = EqlDcbxState
_EqlDcbxLocDCBState_Object = MibTableColumn
eqlDcbxLocDCBState = _EqlDcbxLocDCBState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 39),
    _EqlDcbxLocDCBState_Type()
)
eqlDcbxLocDCBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocDCBState.setStatus("current")
_EqlDcbxLocPFCState_Type = EqlDcbxState
_EqlDcbxLocPFCState_Object = MibTableColumn
eqlDcbxLocPFCState = _EqlDcbxLocPFCState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 40),
    _EqlDcbxLocPFCState_Type()
)
eqlDcbxLocPFCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPFCState.setStatus("current")
_EqlDcbxLocETSState_Type = EqlDcbxState
_EqlDcbxLocETSState_Object = MibTableColumn
eqlDcbxLocETSState = _EqlDcbxLocETSState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 41),
    _EqlDcbxLocETSState_Type()
)
eqlDcbxLocETSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSState.setStatus("current")
_EqlDcbxLocQCNState_Type = EqlDcbxState
_EqlDcbxLocQCNState_Object = MibTableColumn
eqlDcbxLocQCNState = _EqlDcbxLocQCNState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 42),
    _EqlDcbxLocQCNState_Type()
)
eqlDcbxLocQCNState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocQCNState.setStatus("current")
_EqlDcbxLociSCSIPriority_Type = EqlIEEE8021PriorityValue
_EqlDcbxLociSCSIPriority_Object = MibTableColumn
eqlDcbxLociSCSIPriority = _EqlDcbxLociSCSIPriority_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 43),
    _EqlDcbxLociSCSIPriority_Type()
)
eqlDcbxLociSCSIPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLociSCSIPriority.setStatus("current")
_EqlDcbxLocFCoEPriority_Type = EqlIEEE8021PriorityValue
_EqlDcbxLocFCoEPriority_Object = MibTableColumn
eqlDcbxLocFCoEPriority = _EqlDcbxLocFCoEPriority_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 44),
    _EqlDcbxLocFCoEPriority_Type()
)
eqlDcbxLocFCoEPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocFCoEPriority.setStatus("current")
_EqlDcbxLocBytesRxPri0_Type = Counter64
_EqlDcbxLocBytesRxPri0_Object = MibTableColumn
eqlDcbxLocBytesRxPri0 = _EqlDcbxLocBytesRxPri0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 45),
    _EqlDcbxLocBytesRxPri0_Type()
)
eqlDcbxLocBytesRxPri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesRxPri0.setStatus("current")
_EqlDcbxLocBytesRxPri1_Type = Counter64
_EqlDcbxLocBytesRxPri1_Object = MibTableColumn
eqlDcbxLocBytesRxPri1 = _EqlDcbxLocBytesRxPri1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 46),
    _EqlDcbxLocBytesRxPri1_Type()
)
eqlDcbxLocBytesRxPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesRxPri1.setStatus("current")
_EqlDcbxLocBytesRxPri2_Type = Counter64
_EqlDcbxLocBytesRxPri2_Object = MibTableColumn
eqlDcbxLocBytesRxPri2 = _EqlDcbxLocBytesRxPri2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 47),
    _EqlDcbxLocBytesRxPri2_Type()
)
eqlDcbxLocBytesRxPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesRxPri2.setStatus("current")
_EqlDcbxLocBytesRxPri3_Type = Counter64
_EqlDcbxLocBytesRxPri3_Object = MibTableColumn
eqlDcbxLocBytesRxPri3 = _EqlDcbxLocBytesRxPri3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 48),
    _EqlDcbxLocBytesRxPri3_Type()
)
eqlDcbxLocBytesRxPri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesRxPri3.setStatus("current")
_EqlDcbxLocBytesRxPri4_Type = Counter64
_EqlDcbxLocBytesRxPri4_Object = MibTableColumn
eqlDcbxLocBytesRxPri4 = _EqlDcbxLocBytesRxPri4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 49),
    _EqlDcbxLocBytesRxPri4_Type()
)
eqlDcbxLocBytesRxPri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesRxPri4.setStatus("current")
_EqlDcbxLocBytesRxPri5_Type = Counter64
_EqlDcbxLocBytesRxPri5_Object = MibTableColumn
eqlDcbxLocBytesRxPri5 = _EqlDcbxLocBytesRxPri5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 50),
    _EqlDcbxLocBytesRxPri5_Type()
)
eqlDcbxLocBytesRxPri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesRxPri5.setStatus("current")
_EqlDcbxLocBytesRxPri6_Type = Counter64
_EqlDcbxLocBytesRxPri6_Object = MibTableColumn
eqlDcbxLocBytesRxPri6 = _EqlDcbxLocBytesRxPri6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 51),
    _EqlDcbxLocBytesRxPri6_Type()
)
eqlDcbxLocBytesRxPri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesRxPri6.setStatus("current")
_EqlDcbxLocBytesRxPri7_Type = Counter64
_EqlDcbxLocBytesRxPri7_Object = MibTableColumn
eqlDcbxLocBytesRxPri7 = _EqlDcbxLocBytesRxPri7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 52),
    _EqlDcbxLocBytesRxPri7_Type()
)
eqlDcbxLocBytesRxPri7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesRxPri7.setStatus("current")
_EqlDcbxLocBytesTxPri0_Type = Counter64
_EqlDcbxLocBytesTxPri0_Object = MibTableColumn
eqlDcbxLocBytesTxPri0 = _EqlDcbxLocBytesTxPri0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 53),
    _EqlDcbxLocBytesTxPri0_Type()
)
eqlDcbxLocBytesTxPri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesTxPri0.setStatus("current")
_EqlDcbxLocBytesTxPri1_Type = Counter64
_EqlDcbxLocBytesTxPri1_Object = MibTableColumn
eqlDcbxLocBytesTxPri1 = _EqlDcbxLocBytesTxPri1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 54),
    _EqlDcbxLocBytesTxPri1_Type()
)
eqlDcbxLocBytesTxPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesTxPri1.setStatus("current")
_EqlDcbxLocBytesTxPri2_Type = Counter64
_EqlDcbxLocBytesTxPri2_Object = MibTableColumn
eqlDcbxLocBytesTxPri2 = _EqlDcbxLocBytesTxPri2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 55),
    _EqlDcbxLocBytesTxPri2_Type()
)
eqlDcbxLocBytesTxPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesTxPri2.setStatus("current")
_EqlDcbxLocBytesTxPri3_Type = Counter64
_EqlDcbxLocBytesTxPri3_Object = MibTableColumn
eqlDcbxLocBytesTxPri3 = _EqlDcbxLocBytesTxPri3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 56),
    _EqlDcbxLocBytesTxPri3_Type()
)
eqlDcbxLocBytesTxPri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesTxPri3.setStatus("current")
_EqlDcbxLocBytesTxPri4_Type = Counter64
_EqlDcbxLocBytesTxPri4_Object = MibTableColumn
eqlDcbxLocBytesTxPri4 = _EqlDcbxLocBytesTxPri4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 57),
    _EqlDcbxLocBytesTxPri4_Type()
)
eqlDcbxLocBytesTxPri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesTxPri4.setStatus("current")
_EqlDcbxLocBytesTxPri5_Type = Counter64
_EqlDcbxLocBytesTxPri5_Object = MibTableColumn
eqlDcbxLocBytesTxPri5 = _EqlDcbxLocBytesTxPri5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 58),
    _EqlDcbxLocBytesTxPri5_Type()
)
eqlDcbxLocBytesTxPri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesTxPri5.setStatus("current")
_EqlDcbxLocBytesTxPri6_Type = Counter64
_EqlDcbxLocBytesTxPri6_Object = MibTableColumn
eqlDcbxLocBytesTxPri6 = _EqlDcbxLocBytesTxPri6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 59),
    _EqlDcbxLocBytesTxPri6_Type()
)
eqlDcbxLocBytesTxPri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesTxPri6.setStatus("current")
_EqlDcbxLocBytesTxPri7_Type = Counter64
_EqlDcbxLocBytesTxPri7_Object = MibTableColumn
eqlDcbxLocBytesTxPri7 = _EqlDcbxLocBytesTxPri7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 60),
    _EqlDcbxLocBytesTxPri7_Type()
)
eqlDcbxLocBytesTxPri7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocBytesTxPri7.setStatus("current")
_EqlDcbCnRpPortPriCreatedRpsPri0_Type = Counter64
_EqlDcbCnRpPortPriCreatedRpsPri0_Object = MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri0 = _EqlDcbCnRpPortPriCreatedRpsPri0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 61),
    _EqlDcbCnRpPortPriCreatedRpsPri0_Type()
)
eqlDcbCnRpPortPriCreatedRpsPri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCreatedRpsPri0.setStatus("current")
_EqlDcbCnRpPortPriCreatedRpsPri1_Type = Counter64
_EqlDcbCnRpPortPriCreatedRpsPri1_Object = MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri1 = _EqlDcbCnRpPortPriCreatedRpsPri1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 62),
    _EqlDcbCnRpPortPriCreatedRpsPri1_Type()
)
eqlDcbCnRpPortPriCreatedRpsPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCreatedRpsPri1.setStatus("current")
_EqlDcbCnRpPortPriCreatedRpsPri2_Type = Counter64
_EqlDcbCnRpPortPriCreatedRpsPri2_Object = MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri2 = _EqlDcbCnRpPortPriCreatedRpsPri2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 63),
    _EqlDcbCnRpPortPriCreatedRpsPri2_Type()
)
eqlDcbCnRpPortPriCreatedRpsPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCreatedRpsPri2.setStatus("current")
_EqlDcbCnRpPortPriCreatedRpsPri3_Type = Counter64
_EqlDcbCnRpPortPriCreatedRpsPri3_Object = MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri3 = _EqlDcbCnRpPortPriCreatedRpsPri3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 64),
    _EqlDcbCnRpPortPriCreatedRpsPri3_Type()
)
eqlDcbCnRpPortPriCreatedRpsPri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCreatedRpsPri3.setStatus("current")
_EqlDcbCnRpPortPriCreatedRpsPri4_Type = Counter64
_EqlDcbCnRpPortPriCreatedRpsPri4_Object = MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri4 = _EqlDcbCnRpPortPriCreatedRpsPri4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 65),
    _EqlDcbCnRpPortPriCreatedRpsPri4_Type()
)
eqlDcbCnRpPortPriCreatedRpsPri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCreatedRpsPri4.setStatus("current")
_EqlDcbCnRpPortPriCreatedRpsPri5_Type = Counter64
_EqlDcbCnRpPortPriCreatedRpsPri5_Object = MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri5 = _EqlDcbCnRpPortPriCreatedRpsPri5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 66),
    _EqlDcbCnRpPortPriCreatedRpsPri5_Type()
)
eqlDcbCnRpPortPriCreatedRpsPri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCreatedRpsPri5.setStatus("current")
_EqlDcbCnRpPortPriCreatedRpsPri6_Type = Counter64
_EqlDcbCnRpPortPriCreatedRpsPri6_Object = MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri6 = _EqlDcbCnRpPortPriCreatedRpsPri6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 67),
    _EqlDcbCnRpPortPriCreatedRpsPri6_Type()
)
eqlDcbCnRpPortPriCreatedRpsPri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCreatedRpsPri6.setStatus("current")
_EqlDcbCnRpPortPriCreatedRpsPri7_Type = Counter64
_EqlDcbCnRpPortPriCreatedRpsPri7_Object = MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri7 = _EqlDcbCnRpPortPriCreatedRpsPri7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 68),
    _EqlDcbCnRpPortPriCreatedRpsPri7_Type()
)
eqlDcbCnRpPortPriCreatedRpsPri7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCreatedRpsPri7.setStatus("current")
_EqlDcbCnRpPortPriCentisecondsPri0_Type = Counter64
_EqlDcbCnRpPortPriCentisecondsPri0_Object = MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri0 = _EqlDcbCnRpPortPriCentisecondsPri0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 69),
    _EqlDcbCnRpPortPriCentisecondsPri0_Type()
)
eqlDcbCnRpPortPriCentisecondsPri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCentisecondsPri0.setStatus("current")
_EqlDcbCnRpPortPriCentisecondsPri1_Type = Counter64
_EqlDcbCnRpPortPriCentisecondsPri1_Object = MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri1 = _EqlDcbCnRpPortPriCentisecondsPri1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 70),
    _EqlDcbCnRpPortPriCentisecondsPri1_Type()
)
eqlDcbCnRpPortPriCentisecondsPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCentisecondsPri1.setStatus("current")
_EqlDcbCnRpPortPriCentisecondsPri2_Type = Counter64
_EqlDcbCnRpPortPriCentisecondsPri2_Object = MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri2 = _EqlDcbCnRpPortPriCentisecondsPri2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 71),
    _EqlDcbCnRpPortPriCentisecondsPri2_Type()
)
eqlDcbCnRpPortPriCentisecondsPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCentisecondsPri2.setStatus("current")
_EqlDcbCnRpPortPriCentisecondsPri3_Type = Counter64
_EqlDcbCnRpPortPriCentisecondsPri3_Object = MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri3 = _EqlDcbCnRpPortPriCentisecondsPri3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 72),
    _EqlDcbCnRpPortPriCentisecondsPri3_Type()
)
eqlDcbCnRpPortPriCentisecondsPri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCentisecondsPri3.setStatus("current")
_EqlDcbCnRpPortPriCentisecondsPri4_Type = Counter64
_EqlDcbCnRpPortPriCentisecondsPri4_Object = MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri4 = _EqlDcbCnRpPortPriCentisecondsPri4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 73),
    _EqlDcbCnRpPortPriCentisecondsPri4_Type()
)
eqlDcbCnRpPortPriCentisecondsPri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCentisecondsPri4.setStatus("current")
_EqlDcbCnRpPortPriCentisecondsPri5_Type = Counter64
_EqlDcbCnRpPortPriCentisecondsPri5_Object = MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri5 = _EqlDcbCnRpPortPriCentisecondsPri5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 74),
    _EqlDcbCnRpPortPriCentisecondsPri5_Type()
)
eqlDcbCnRpPortPriCentisecondsPri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCentisecondsPri5.setStatus("current")
_EqlDcbCnRpPortPriCentisecondsPri6_Type = Counter64
_EqlDcbCnRpPortPriCentisecondsPri6_Object = MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri6 = _EqlDcbCnRpPortPriCentisecondsPri6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 75),
    _EqlDcbCnRpPortPriCentisecondsPri6_Type()
)
eqlDcbCnRpPortPriCentisecondsPri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCentisecondsPri6.setStatus("current")
_EqlDcbCnRpPortPriCentisecondsPri7_Type = Counter64
_EqlDcbCnRpPortPriCentisecondsPri7_Object = MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri7 = _EqlDcbCnRpPortPriCentisecondsPri7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 76),
    _EqlDcbCnRpPortPriCentisecondsPri7_Type()
)
eqlDcbCnRpPortPriCentisecondsPri7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbCnRpPortPriCentisecondsPri7.setStatus("current")
_EqlDcbxLocPfcPausePri0_Type = Counter64
_EqlDcbxLocPfcPausePri0_Object = MibTableColumn
eqlDcbxLocPfcPausePri0 = _EqlDcbxLocPfcPausePri0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 77),
    _EqlDcbxLocPfcPausePri0_Type()
)
eqlDcbxLocPfcPausePri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcPausePri0.setStatus("current")
_EqlDcbxLocPfcPausePri1_Type = Counter64
_EqlDcbxLocPfcPausePri1_Object = MibTableColumn
eqlDcbxLocPfcPausePri1 = _EqlDcbxLocPfcPausePri1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 78),
    _EqlDcbxLocPfcPausePri1_Type()
)
eqlDcbxLocPfcPausePri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcPausePri1.setStatus("current")
_EqlDcbxLocPfcPausePri2_Type = Counter64
_EqlDcbxLocPfcPausePri2_Object = MibTableColumn
eqlDcbxLocPfcPausePri2 = _EqlDcbxLocPfcPausePri2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 79),
    _EqlDcbxLocPfcPausePri2_Type()
)
eqlDcbxLocPfcPausePri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcPausePri2.setStatus("current")
_EqlDcbxLocPfcPausePri3_Type = Counter64
_EqlDcbxLocPfcPausePri3_Object = MibTableColumn
eqlDcbxLocPfcPausePri3 = _EqlDcbxLocPfcPausePri3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 80),
    _EqlDcbxLocPfcPausePri3_Type()
)
eqlDcbxLocPfcPausePri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcPausePri3.setStatus("current")
_EqlDcbxLocPfcPausePri4_Type = Counter64
_EqlDcbxLocPfcPausePri4_Object = MibTableColumn
eqlDcbxLocPfcPausePri4 = _EqlDcbxLocPfcPausePri4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 81),
    _EqlDcbxLocPfcPausePri4_Type()
)
eqlDcbxLocPfcPausePri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcPausePri4.setStatus("current")
_EqlDcbxLocPfcPausePri5_Type = Counter64
_EqlDcbxLocPfcPausePri5_Object = MibTableColumn
eqlDcbxLocPfcPausePri5 = _EqlDcbxLocPfcPausePri5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 82),
    _EqlDcbxLocPfcPausePri5_Type()
)
eqlDcbxLocPfcPausePri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcPausePri5.setStatus("current")
_EqlDcbxLocPfcPausePri6_Type = Counter64
_EqlDcbxLocPfcPausePri6_Object = MibTableColumn
eqlDcbxLocPfcPausePri6 = _EqlDcbxLocPfcPausePri6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 83),
    _EqlDcbxLocPfcPausePri6_Type()
)
eqlDcbxLocPfcPausePri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcPausePri6.setStatus("current")
_EqlDcbxLocPfcPausePri7_Type = Counter64
_EqlDcbxLocPfcPausePri7_Object = MibTableColumn
eqlDcbxLocPfcPausePri7 = _EqlDcbxLocPfcPausePri7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 84),
    _EqlDcbxLocPfcPausePri7_Type()
)
eqlDcbxLocPfcPausePri7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcPausePri7.setStatus("current")
_EqlDcbxLocPfcUnpausePri0_Type = Counter64
_EqlDcbxLocPfcUnpausePri0_Object = MibTableColumn
eqlDcbxLocPfcUnpausePri0 = _EqlDcbxLocPfcUnpausePri0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 85),
    _EqlDcbxLocPfcUnpausePri0_Type()
)
eqlDcbxLocPfcUnpausePri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcUnpausePri0.setStatus("current")
_EqlDcbxLocPfcUnpausePri1_Type = Counter64
_EqlDcbxLocPfcUnpausePri1_Object = MibTableColumn
eqlDcbxLocPfcUnpausePri1 = _EqlDcbxLocPfcUnpausePri1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 86),
    _EqlDcbxLocPfcUnpausePri1_Type()
)
eqlDcbxLocPfcUnpausePri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcUnpausePri1.setStatus("current")
_EqlDcbxLocPfcUnpausePri2_Type = Counter64
_EqlDcbxLocPfcUnpausePri2_Object = MibTableColumn
eqlDcbxLocPfcUnpausePri2 = _EqlDcbxLocPfcUnpausePri2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 87),
    _EqlDcbxLocPfcUnpausePri2_Type()
)
eqlDcbxLocPfcUnpausePri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcUnpausePri2.setStatus("current")
_EqlDcbxLocPfcUnpausePri3_Type = Counter64
_EqlDcbxLocPfcUnpausePri3_Object = MibTableColumn
eqlDcbxLocPfcUnpausePri3 = _EqlDcbxLocPfcUnpausePri3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 88),
    _EqlDcbxLocPfcUnpausePri3_Type()
)
eqlDcbxLocPfcUnpausePri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcUnpausePri3.setStatus("current")
_EqlDcbxLocPfcUnpausePri4_Type = Counter64
_EqlDcbxLocPfcUnpausePri4_Object = MibTableColumn
eqlDcbxLocPfcUnpausePri4 = _EqlDcbxLocPfcUnpausePri4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 89),
    _EqlDcbxLocPfcUnpausePri4_Type()
)
eqlDcbxLocPfcUnpausePri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcUnpausePri4.setStatus("current")
_EqlDcbxLocPfcUnpausePri5_Type = Counter64
_EqlDcbxLocPfcUnpausePri5_Object = MibTableColumn
eqlDcbxLocPfcUnpausePri5 = _EqlDcbxLocPfcUnpausePri5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 90),
    _EqlDcbxLocPfcUnpausePri5_Type()
)
eqlDcbxLocPfcUnpausePri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcUnpausePri5.setStatus("current")
_EqlDcbxLocPfcUnpausePri6_Type = Counter64
_EqlDcbxLocPfcUnpausePri6_Object = MibTableColumn
eqlDcbxLocPfcUnpausePri6 = _EqlDcbxLocPfcUnpausePri6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 91),
    _EqlDcbxLocPfcUnpausePri6_Type()
)
eqlDcbxLocPfcUnpausePri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcUnpausePri6.setStatus("current")
_EqlDcbxLocPfcUnpausePri7_Type = Counter64
_EqlDcbxLocPfcUnpausePri7_Object = MibTableColumn
eqlDcbxLocPfcUnpausePri7 = _EqlDcbxLocPfcUnpausePri7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 92),
    _EqlDcbxLocPfcUnpausePri7_Type()
)
eqlDcbxLocPfcUnpausePri7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocPfcUnpausePri7.setStatus("current")
_EqlDcbxLocETSConTsaTc0_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc0_Object = MibTableColumn
eqlDcbxLocETSConTsaTc0 = _EqlDcbxLocETSConTsaTc0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 93),
    _EqlDcbxLocETSConTsaTc0_Type()
)
eqlDcbxLocETSConTsaTc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTsaTc0.setStatus("current")
_EqlDcbxLocETSConTsaTc1_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc1_Object = MibTableColumn
eqlDcbxLocETSConTsaTc1 = _EqlDcbxLocETSConTsaTc1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 94),
    _EqlDcbxLocETSConTsaTc1_Type()
)
eqlDcbxLocETSConTsaTc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTsaTc1.setStatus("current")
_EqlDcbxLocETSConTsaTc2_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc2_Object = MibTableColumn
eqlDcbxLocETSConTsaTc2 = _EqlDcbxLocETSConTsaTc2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 95),
    _EqlDcbxLocETSConTsaTc2_Type()
)
eqlDcbxLocETSConTsaTc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTsaTc2.setStatus("current")
_EqlDcbxLocETSConTsaTc3_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc3_Object = MibTableColumn
eqlDcbxLocETSConTsaTc3 = _EqlDcbxLocETSConTsaTc3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 96),
    _EqlDcbxLocETSConTsaTc3_Type()
)
eqlDcbxLocETSConTsaTc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTsaTc3.setStatus("current")
_EqlDcbxLocETSConTsaTc4_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc4_Object = MibTableColumn
eqlDcbxLocETSConTsaTc4 = _EqlDcbxLocETSConTsaTc4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 97),
    _EqlDcbxLocETSConTsaTc4_Type()
)
eqlDcbxLocETSConTsaTc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTsaTc4.setStatus("current")
_EqlDcbxLocETSConTsaTc5_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc5_Object = MibTableColumn
eqlDcbxLocETSConTsaTc5 = _EqlDcbxLocETSConTsaTc5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 98),
    _EqlDcbxLocETSConTsaTc5_Type()
)
eqlDcbxLocETSConTsaTc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTsaTc5.setStatus("current")
_EqlDcbxLocETSConTsaTc6_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc6_Object = MibTableColumn
eqlDcbxLocETSConTsaTc6 = _EqlDcbxLocETSConTsaTc6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 99),
    _EqlDcbxLocETSConTsaTc6_Type()
)
eqlDcbxLocETSConTsaTc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTsaTc6.setStatus("current")
_EqlDcbxLocETSConTsaTc7_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc7_Object = MibTableColumn
eqlDcbxLocETSConTsaTc7 = _EqlDcbxLocETSConTsaTc7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 100),
    _EqlDcbxLocETSConTsaTc7_Type()
)
eqlDcbxLocETSConTsaTc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSConTsaTc7.setStatus("current")
_EqlDcbxLocETSRecoTsaTc0_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc0_Object = MibTableColumn
eqlDcbxLocETSRecoTsaTc0 = _EqlDcbxLocETSRecoTsaTc0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 101),
    _EqlDcbxLocETSRecoTsaTc0_Type()
)
eqlDcbxLocETSRecoTsaTc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSRecoTsaTc0.setStatus("current")
_EqlDcbxLocETSRecoTsaTc1_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc1_Object = MibTableColumn
eqlDcbxLocETSRecoTsaTc1 = _EqlDcbxLocETSRecoTsaTc1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 102),
    _EqlDcbxLocETSRecoTsaTc1_Type()
)
eqlDcbxLocETSRecoTsaTc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSRecoTsaTc1.setStatus("current")
_EqlDcbxLocETSRecoTsaTc2_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc2_Object = MibTableColumn
eqlDcbxLocETSRecoTsaTc2 = _EqlDcbxLocETSRecoTsaTc2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 103),
    _EqlDcbxLocETSRecoTsaTc2_Type()
)
eqlDcbxLocETSRecoTsaTc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSRecoTsaTc2.setStatus("current")
_EqlDcbxLocETSRecoTsaTc3_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc3_Object = MibTableColumn
eqlDcbxLocETSRecoTsaTc3 = _EqlDcbxLocETSRecoTsaTc3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 104),
    _EqlDcbxLocETSRecoTsaTc3_Type()
)
eqlDcbxLocETSRecoTsaTc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSRecoTsaTc3.setStatus("current")
_EqlDcbxLocETSRecoTsaTc4_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc4_Object = MibTableColumn
eqlDcbxLocETSRecoTsaTc4 = _EqlDcbxLocETSRecoTsaTc4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 105),
    _EqlDcbxLocETSRecoTsaTc4_Type()
)
eqlDcbxLocETSRecoTsaTc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSRecoTsaTc4.setStatus("current")
_EqlDcbxLocETSRecoTsaTc5_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc5_Object = MibTableColumn
eqlDcbxLocETSRecoTsaTc5 = _EqlDcbxLocETSRecoTsaTc5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 106),
    _EqlDcbxLocETSRecoTsaTc5_Type()
)
eqlDcbxLocETSRecoTsaTc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSRecoTsaTc5.setStatus("current")
_EqlDcbxLocETSRecoTsaTc6_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc6_Object = MibTableColumn
eqlDcbxLocETSRecoTsaTc6 = _EqlDcbxLocETSRecoTsaTc6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 107),
    _EqlDcbxLocETSRecoTsaTc6_Type()
)
eqlDcbxLocETSRecoTsaTc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSRecoTsaTc6.setStatus("current")
_EqlDcbxLocETSRecoTsaTc7_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc7_Object = MibTableColumn
eqlDcbxLocETSRecoTsaTc7 = _EqlDcbxLocETSRecoTsaTc7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 108),
    _EqlDcbxLocETSRecoTsaTc7_Type()
)
eqlDcbxLocETSRecoTsaTc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocETSRecoTsaTc7.setStatus("current")
_EqlDcbxRemETSConTsaTc0_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc0_Object = MibTableColumn
eqlDcbxRemETSConTsaTc0 = _EqlDcbxRemETSConTsaTc0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 109),
    _EqlDcbxRemETSConTsaTc0_Type()
)
eqlDcbxRemETSConTsaTc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSConTsaTc0.setStatus("current")
_EqlDcbxRemETSConTsaTc1_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc1_Object = MibTableColumn
eqlDcbxRemETSConTsaTc1 = _EqlDcbxRemETSConTsaTc1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 110),
    _EqlDcbxRemETSConTsaTc1_Type()
)
eqlDcbxRemETSConTsaTc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSConTsaTc1.setStatus("current")
_EqlDcbxRemETSConTsaTc2_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc2_Object = MibTableColumn
eqlDcbxRemETSConTsaTc2 = _EqlDcbxRemETSConTsaTc2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 111),
    _EqlDcbxRemETSConTsaTc2_Type()
)
eqlDcbxRemETSConTsaTc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSConTsaTc2.setStatus("current")
_EqlDcbxRemETSConTsaTc3_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc3_Object = MibTableColumn
eqlDcbxRemETSConTsaTc3 = _EqlDcbxRemETSConTsaTc3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 112),
    _EqlDcbxRemETSConTsaTc3_Type()
)
eqlDcbxRemETSConTsaTc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSConTsaTc3.setStatus("current")
_EqlDcbxRemETSConTsaTc4_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc4_Object = MibTableColumn
eqlDcbxRemETSConTsaTc4 = _EqlDcbxRemETSConTsaTc4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 113),
    _EqlDcbxRemETSConTsaTc4_Type()
)
eqlDcbxRemETSConTsaTc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSConTsaTc4.setStatus("current")
_EqlDcbxRemETSConTsaTc5_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc5_Object = MibTableColumn
eqlDcbxRemETSConTsaTc5 = _EqlDcbxRemETSConTsaTc5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 114),
    _EqlDcbxRemETSConTsaTc5_Type()
)
eqlDcbxRemETSConTsaTc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSConTsaTc5.setStatus("current")
_EqlDcbxRemETSConTsaTc6_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc6_Object = MibTableColumn
eqlDcbxRemETSConTsaTc6 = _EqlDcbxRemETSConTsaTc6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 115),
    _EqlDcbxRemETSConTsaTc6_Type()
)
eqlDcbxRemETSConTsaTc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSConTsaTc6.setStatus("current")
_EqlDcbxRemETSConTsaTc7_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc7_Object = MibTableColumn
eqlDcbxRemETSConTsaTc7 = _EqlDcbxRemETSConTsaTc7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 116),
    _EqlDcbxRemETSConTsaTc7_Type()
)
eqlDcbxRemETSConTsaTc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSConTsaTc7.setStatus("current")
_EqlDcbxRemETSRecoTsaTc0_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc0_Object = MibTableColumn
eqlDcbxRemETSRecoTsaTc0 = _EqlDcbxRemETSRecoTsaTc0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 117),
    _EqlDcbxRemETSRecoTsaTc0_Type()
)
eqlDcbxRemETSRecoTsaTc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSRecoTsaTc0.setStatus("current")
_EqlDcbxRemETSRecoTsaTc1_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc1_Object = MibTableColumn
eqlDcbxRemETSRecoTsaTc1 = _EqlDcbxRemETSRecoTsaTc1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 118),
    _EqlDcbxRemETSRecoTsaTc1_Type()
)
eqlDcbxRemETSRecoTsaTc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSRecoTsaTc1.setStatus("current")
_EqlDcbxRemETSRecoTsaTc2_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc2_Object = MibTableColumn
eqlDcbxRemETSRecoTsaTc2 = _EqlDcbxRemETSRecoTsaTc2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 119),
    _EqlDcbxRemETSRecoTsaTc2_Type()
)
eqlDcbxRemETSRecoTsaTc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSRecoTsaTc2.setStatus("current")
_EqlDcbxRemETSRecoTsaTc3_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc3_Object = MibTableColumn
eqlDcbxRemETSRecoTsaTc3 = _EqlDcbxRemETSRecoTsaTc3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 120),
    _EqlDcbxRemETSRecoTsaTc3_Type()
)
eqlDcbxRemETSRecoTsaTc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSRecoTsaTc3.setStatus("current")
_EqlDcbxRemETSRecoTsaTc4_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc4_Object = MibTableColumn
eqlDcbxRemETSRecoTsaTc4 = _EqlDcbxRemETSRecoTsaTc4_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 121),
    _EqlDcbxRemETSRecoTsaTc4_Type()
)
eqlDcbxRemETSRecoTsaTc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSRecoTsaTc4.setStatus("current")
_EqlDcbxRemETSRecoTsaTc5_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc5_Object = MibTableColumn
eqlDcbxRemETSRecoTsaTc5 = _EqlDcbxRemETSRecoTsaTc5_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 122),
    _EqlDcbxRemETSRecoTsaTc5_Type()
)
eqlDcbxRemETSRecoTsaTc5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSRecoTsaTc5.setStatus("current")
_EqlDcbxRemETSRecoTsaTc6_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc6_Object = MibTableColumn
eqlDcbxRemETSRecoTsaTc6 = _EqlDcbxRemETSRecoTsaTc6_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 123),
    _EqlDcbxRemETSRecoTsaTc6_Type()
)
eqlDcbxRemETSRecoTsaTc6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSRecoTsaTc6.setStatus("current")
_EqlDcbxRemETSRecoTsaTc7_Type = EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc7_Object = MibTableColumn
eqlDcbxRemETSRecoTsaTc7 = _EqlDcbxRemETSRecoTsaTc7_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 124),
    _EqlDcbxRemETSRecoTsaTc7_Type()
)
eqlDcbxRemETSRecoTsaTc7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxRemETSRecoTsaTc7.setStatus("current")
_EqlDcbxLocDCBMode_Type = EqlDcbxMode
_EqlDcbxLocDCBMode_Object = MibTableColumn
eqlDcbxLocDCBMode = _EqlDcbxLocDCBMode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 19, 1, 2, 1, 125),
    _EqlDcbxLocDCBMode_Type()
)
eqlDcbxLocDCBMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDcbxLocDCBMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQL-DCB-MIB",
    **{"EqlDcbxTrafficClassGroupValue": EqlDcbxTrafficClassGroupValue,
       "EqlDcbxAppSelector": EqlDcbxAppSelector,
       "EqlDcbxAppProtocol": EqlDcbxAppProtocol,
       "EqlDcbxSupportedCapacity": EqlDcbxSupportedCapacity,
       "EqlVlanIdentifier": EqlVlanIdentifier,
       "EqlIEEE8021PriorityValue": EqlIEEE8021PriorityValue,
       "EqlIEEEDraftSubtypeValue": EqlIEEEDraftSubtypeValue,
       "EqlDcbxState": EqlDcbxState,
       "EqlDcbxVlanState": EqlDcbxVlanState,
       "EqlDcbxTransmissionSelectionAlgorithm": EqlDcbxTransmissionSelectionAlgorithm,
       "EqlDcbxMode": EqlDcbxMode,
       "eqlDcbMib": eqlDcbMib,
       "eqlDcbMIBObjects": eqlDcbMIBObjects,
       "eqlDcbStaticIfTable": eqlDcbStaticIfTable,
       "eqlDcbStaticIfEntry": eqlDcbStaticIfEntry,
       "eqlDcbxConfigTCSupportedTxEnable": eqlDcbxConfigTCSupportedTxEnable,
       "eqlDcbxConfigETSConfigurationTxEnable": eqlDcbxConfigETSConfigurationTxEnable,
       "eqlDcbxConfigETSRecommendationTxEnable": eqlDcbxConfigETSRecommendationTxEnable,
       "eqlDcbxConfigPFCTxEnable": eqlDcbxConfigPFCTxEnable,
       "eqlDcbxConfigAppPriorityTxEnable": eqlDcbxConfigAppPriorityTxEnable,
       "eqlDcbxConfigQcnTxEnable": eqlDcbxConfigQcnTxEnable,
       "eqlDcbxAdminTCSupported": eqlDcbxAdminTCSupported,
       "eqlDcbxAdminETSConMaxTCG": eqlDcbxAdminETSConMaxTCG,
       "eqlDcbxAdminETSConWilling": eqlDcbxAdminETSConWilling,
       "eqlDcbxAdminETSConTrafficClassGroupBandwidthTable": eqlDcbxAdminETSConTrafficClassGroupBandwidthTable,
       "eqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable": eqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable,
       "eqlDcbxAdminPFCWilling": eqlDcbxAdminPFCWilling,
       "eqlDcbxAdminPFCMBC": eqlDcbxAdminPFCMBC,
       "eqlDcbxAdminPFCCap": eqlDcbxAdminPFCCap,
       "eqlDcbxAdminAppPriorityWilling": eqlDcbxAdminAppPriorityWilling,
       "eqlDcbxConfigAutoDetectVLANEnable": eqlDcbxConfigAutoDetectVLANEnable,
       "eqlDcbxConfigVLANId": eqlDcbxConfigVLANId,
       "eqlDcbxAdminETSConTrafficClassGroupPri0": eqlDcbxAdminETSConTrafficClassGroupPri0,
       "eqlDcbxAdminETSConTrafficClassGroupPri1": eqlDcbxAdminETSConTrafficClassGroupPri1,
       "eqlDcbxAdminETSConTrafficClassGroupPri2": eqlDcbxAdminETSConTrafficClassGroupPri2,
       "eqlDcbxAdminETSConTrafficClassGroupPri3": eqlDcbxAdminETSConTrafficClassGroupPri3,
       "eqlDcbxAdminETSConTrafficClassGroupPri4": eqlDcbxAdminETSConTrafficClassGroupPri4,
       "eqlDcbxAdminETSConTrafficClassGroupPri5": eqlDcbxAdminETSConTrafficClassGroupPri5,
       "eqlDcbxAdminETSConTrafficClassGroupPri6": eqlDcbxAdminETSConTrafficClassGroupPri6,
       "eqlDcbxAdminETSConTrafficClassGroupPri7": eqlDcbxAdminETSConTrafficClassGroupPri7,
       "eqlDcbxAdminPFCEnableEnabledPri0": eqlDcbxAdminPFCEnableEnabledPri0,
       "eqlDcbxAdminPFCEnableEnabledPri1": eqlDcbxAdminPFCEnableEnabledPri1,
       "eqlDcbxAdminPFCEnableEnabledPri2": eqlDcbxAdminPFCEnableEnabledPri2,
       "eqlDcbxAdminPFCEnableEnabledPri3": eqlDcbxAdminPFCEnableEnabledPri3,
       "eqlDcbxAdminPFCEnableEnabledPri4": eqlDcbxAdminPFCEnableEnabledPri4,
       "eqlDcbxAdminPFCEnableEnabledPri5": eqlDcbxAdminPFCEnableEnabledPri5,
       "eqlDcbxAdminPFCEnableEnabledPri6": eqlDcbxAdminPFCEnableEnabledPri6,
       "eqlDcbxAdminPFCEnableEnabledPri7": eqlDcbxAdminPFCEnableEnabledPri7,
       "eqlDcbxAdminAppPriorityiSCSITxEnable": eqlDcbxAdminAppPriorityiSCSITxEnable,
       "eqlDcbxAdminAppPriorityiSCSIProtocol": eqlDcbxAdminAppPriorityiSCSIProtocol,
       "eqlDcbxAdminAppPriorityiSCSIPriority": eqlDcbxAdminAppPriorityiSCSIPriority,
       "eqlDcbxAdminAppPriorityFCoETxEnable": eqlDcbxAdminAppPriorityFCoETxEnable,
       "eqlDcbxAdminAppPriorityFCoEProtocol": eqlDcbxAdminAppPriorityFCoEProtocol,
       "eqlDcbxAdminAppPriorityFCoEPriority": eqlDcbxAdminAppPriorityFCoEPriority,
       "eqlDcbxConfigDCBEnable": eqlDcbxConfigDCBEnable,
       "eqlDcbxConfigDCBX101Enable": eqlDcbxConfigDCBX101Enable,
       "eqlDcbxConfigDCBXIEEEDraftEnable": eqlDcbxConfigDCBXIEEEDraftEnable,
       "eqlDcbxConfigQcnSubtype": eqlDcbxConfigQcnSubtype,
       "eqlDcbxConfigETSConSubtype": eqlDcbxConfigETSConSubtype,
       "eqlDcbxConfigETSRecoSubtype": eqlDcbxConfigETSRecoSubtype,
       "eqlDcbxConfigPFCSubtype": eqlDcbxConfigPFCSubtype,
       "eqlDcbxConfigAppPrioritySubtype": eqlDcbxConfigAppPrioritySubtype,
       "eqlDcbxConfigTCSupportedSubtype": eqlDcbxConfigTCSupportedSubtype,
       "eqlDcbxAdminETSRecoTrafficClassGroupPri0": eqlDcbxAdminETSRecoTrafficClassGroupPri0,
       "eqlDcbxAdminETSRecoTrafficClassGroupPri1": eqlDcbxAdminETSRecoTrafficClassGroupPri1,
       "eqlDcbxAdminETSRecoTrafficClassGroupPri2": eqlDcbxAdminETSRecoTrafficClassGroupPri2,
       "eqlDcbxAdminETSRecoTrafficClassGroupPri3": eqlDcbxAdminETSRecoTrafficClassGroupPri3,
       "eqlDcbxAdminETSRecoTrafficClassGroupPri4": eqlDcbxAdminETSRecoTrafficClassGroupPri4,
       "eqlDcbxAdminETSRecoTrafficClassGroupPri5": eqlDcbxAdminETSRecoTrafficClassGroupPri5,
       "eqlDcbxAdminETSRecoTrafficClassGroupPri6": eqlDcbxAdminETSRecoTrafficClassGroupPri6,
       "eqlDcbxAdminETSRecoTrafficClassGroupPri7": eqlDcbxAdminETSRecoTrafficClassGroupPri7,
       "eqlDcbCnGlobalMasterEnable": eqlDcbCnGlobalMasterEnable,
       "eqlDcbCnRpPortPriMaxRps": eqlDcbCnRpPortPriMaxRps,
       "eqlDcbCnRpgEnablePri0": eqlDcbCnRpgEnablePri0,
       "eqlDcbCnRpgEnablePri1": eqlDcbCnRpgEnablePri1,
       "eqlDcbCnRpgEnablePri2": eqlDcbCnRpgEnablePri2,
       "eqlDcbCnRpgEnablePri3": eqlDcbCnRpgEnablePri3,
       "eqlDcbCnRpgEnablePri4": eqlDcbCnRpgEnablePri4,
       "eqlDcbCnRpgEnablePri5": eqlDcbCnRpgEnablePri5,
       "eqlDcbCnRpgEnablePri6": eqlDcbCnRpgEnablePri6,
       "eqlDcbCnRpgEnablePri7": eqlDcbCnRpgEnablePri7,
       "eqlDcbCnRpgTimeReset": eqlDcbCnRpgTimeReset,
       "eqlDcbCnRpgByteReset": eqlDcbCnRpgByteReset,
       "eqlDcbCnRpgThreshold": eqlDcbCnRpgThreshold,
       "eqlDcbCnRpgMaxRate": eqlDcbCnRpgMaxRate,
       "eqlDcbCnRpgAiRate": eqlDcbCnRpgAiRate,
       "eqlDcbCnRpgHaiRate": eqlDcbCnRpgHaiRate,
       "eqlDcbCnRpgGd": eqlDcbCnRpgGd,
       "eqlDcbCnRpgMinDecFac": eqlDcbCnRpgMinDecFac,
       "eqlDcbCnRpgMinRate": eqlDcbCnRpgMinRate,
       "eqlDcbDefaultiSCSIPriority": eqlDcbDefaultiSCSIPriority,
       "eqlDcbDefaultFCoEPriority": eqlDcbDefaultFCoEPriority,
       "eqlDcbxAdminETSConTsaTc0": eqlDcbxAdminETSConTsaTc0,
       "eqlDcbxAdminETSConTsaTc1": eqlDcbxAdminETSConTsaTc1,
       "eqlDcbxAdminETSConTsaTc2": eqlDcbxAdminETSConTsaTc2,
       "eqlDcbxAdminETSConTsaTc3": eqlDcbxAdminETSConTsaTc3,
       "eqlDcbxAdminETSConTsaTc4": eqlDcbxAdminETSConTsaTc4,
       "eqlDcbxAdminETSConTsaTc5": eqlDcbxAdminETSConTsaTc5,
       "eqlDcbxAdminETSConTsaTc6": eqlDcbxAdminETSConTsaTc6,
       "eqlDcbxAdminETSConTsaTc7": eqlDcbxAdminETSConTsaTc7,
       "eqlDcbxAdminETSRecoTsaTc0": eqlDcbxAdminETSRecoTsaTc0,
       "eqlDcbxAdminETSRecoTsaTc1": eqlDcbxAdminETSRecoTsaTc1,
       "eqlDcbxAdminETSRecoTsaTc2": eqlDcbxAdminETSRecoTsaTc2,
       "eqlDcbxAdminETSRecoTsaTc3": eqlDcbxAdminETSRecoTsaTc3,
       "eqlDcbxAdminETSRecoTsaTc4": eqlDcbxAdminETSRecoTsaTc4,
       "eqlDcbxAdminETSRecoTsaTc5": eqlDcbxAdminETSRecoTsaTc5,
       "eqlDcbxAdminETSRecoTsaTc6": eqlDcbxAdminETSRecoTsaTc6,
       "eqlDcbxAdminETSRecoTsaTc7": eqlDcbxAdminETSRecoTsaTc7,
       "eqlDcbDynamicIfTable": eqlDcbDynamicIfTable,
       "eqlDcbDynamicIfEntry": eqlDcbDynamicIfEntry,
       "eqlDcbPfcRequestsSent": eqlDcbPfcRequestsSent,
       "eqlDcbPfcIndicationsReceived": eqlDcbPfcIndicationsReceived,
       "eqlDcbxLocTCSupported": eqlDcbxLocTCSupported,
       "eqlDcbxLocETSConMaxTCG": eqlDcbxLocETSConMaxTCG,
       "eqlDcbxLocETSConWilling": eqlDcbxLocETSConWilling,
       "eqlDcbxLocETSConTrafficClassGroupBandwidthTable": eqlDcbxLocETSConTrafficClassGroupBandwidthTable,
       "eqlDcbxLocETSRecoTrafficClassGroupBandwidthTable": eqlDcbxLocETSRecoTrafficClassGroupBandwidthTable,
       "eqlDcbxLocPFCWilling": eqlDcbxLocPFCWilling,
       "eqlDcbxLocPFCMBC": eqlDcbxLocPFCMBC,
       "eqlDcbxLocPFCCap": eqlDcbxLocPFCCap,
       "eqlDcbxLocAppPriorityWilling": eqlDcbxLocAppPriorityWilling,
       "eqlDcbxRemTCSupported": eqlDcbxRemTCSupported,
       "eqlDcbxRemETSConMaxTCG": eqlDcbxRemETSConMaxTCG,
       "eqlDcbxRemETSConWilling": eqlDcbxRemETSConWilling,
       "eqlDcbxRemETSConTrafficClassGroupBandwidthTable": eqlDcbxRemETSConTrafficClassGroupBandwidthTable,
       "eqlDcbxRemETSRecoTrafficClassGroupBandwidthTable": eqlDcbxRemETSRecoTrafficClassGroupBandwidthTable,
       "eqlDcbxRemPFCWilling": eqlDcbxRemPFCWilling,
       "eqlDcbxRemPFCMBC": eqlDcbxRemPFCMBC,
       "eqlDcbxRemPFCCap": eqlDcbxRemPFCCap,
       "eqlDcbxRemAppPriorityWilling": eqlDcbxRemAppPriorityWilling,
       "eqlDcbxLocETSConTrafficClassGroupPri0": eqlDcbxLocETSConTrafficClassGroupPri0,
       "eqlDcbxLocETSConTrafficClassGroupPri1": eqlDcbxLocETSConTrafficClassGroupPri1,
       "eqlDcbxLocETSConTrafficClassGroupPri2": eqlDcbxLocETSConTrafficClassGroupPri2,
       "eqlDcbxLocETSConTrafficClassGroupPri3": eqlDcbxLocETSConTrafficClassGroupPri3,
       "eqlDcbxLocETSConTrafficClassGroupPri4": eqlDcbxLocETSConTrafficClassGroupPri4,
       "eqlDcbxLocETSConTrafficClassGroupPri5": eqlDcbxLocETSConTrafficClassGroupPri5,
       "eqlDcbxLocETSConTrafficClassGroupPri6": eqlDcbxLocETSConTrafficClassGroupPri6,
       "eqlDcbxLocETSConTrafficClassGroupPri7": eqlDcbxLocETSConTrafficClassGroupPri7,
       "eqlDcbxLocPFCEnableEnabledPri0": eqlDcbxLocPFCEnableEnabledPri0,
       "eqlDcbxLocPFCEnableEnabledPri1": eqlDcbxLocPFCEnableEnabledPri1,
       "eqlDcbxLocPFCEnableEnabledPri2": eqlDcbxLocPFCEnableEnabledPri2,
       "eqlDcbxLocPFCEnableEnabledPri3": eqlDcbxLocPFCEnableEnabledPri3,
       "eqlDcbxLocPFCEnableEnabledPri4": eqlDcbxLocPFCEnableEnabledPri4,
       "eqlDcbxLocPFCEnableEnabledPri5": eqlDcbxLocPFCEnableEnabledPri5,
       "eqlDcbxLocPFCEnableEnabledPri6": eqlDcbxLocPFCEnableEnabledPri6,
       "eqlDcbxLocPFCEnableEnabledPri7": eqlDcbxLocPFCEnableEnabledPri7,
       "eqlDcbxLocVLANId": eqlDcbxLocVLANId,
       "eqlDcbxLocVLANState": eqlDcbxLocVLANState,
       "eqlDcbxLocDCBState": eqlDcbxLocDCBState,
       "eqlDcbxLocPFCState": eqlDcbxLocPFCState,
       "eqlDcbxLocETSState": eqlDcbxLocETSState,
       "eqlDcbxLocQCNState": eqlDcbxLocQCNState,
       "eqlDcbxLociSCSIPriority": eqlDcbxLociSCSIPriority,
       "eqlDcbxLocFCoEPriority": eqlDcbxLocFCoEPriority,
       "eqlDcbxLocBytesRxPri0": eqlDcbxLocBytesRxPri0,
       "eqlDcbxLocBytesRxPri1": eqlDcbxLocBytesRxPri1,
       "eqlDcbxLocBytesRxPri2": eqlDcbxLocBytesRxPri2,
       "eqlDcbxLocBytesRxPri3": eqlDcbxLocBytesRxPri3,
       "eqlDcbxLocBytesRxPri4": eqlDcbxLocBytesRxPri4,
       "eqlDcbxLocBytesRxPri5": eqlDcbxLocBytesRxPri5,
       "eqlDcbxLocBytesRxPri6": eqlDcbxLocBytesRxPri6,
       "eqlDcbxLocBytesRxPri7": eqlDcbxLocBytesRxPri7,
       "eqlDcbxLocBytesTxPri0": eqlDcbxLocBytesTxPri0,
       "eqlDcbxLocBytesTxPri1": eqlDcbxLocBytesTxPri1,
       "eqlDcbxLocBytesTxPri2": eqlDcbxLocBytesTxPri2,
       "eqlDcbxLocBytesTxPri3": eqlDcbxLocBytesTxPri3,
       "eqlDcbxLocBytesTxPri4": eqlDcbxLocBytesTxPri4,
       "eqlDcbxLocBytesTxPri5": eqlDcbxLocBytesTxPri5,
       "eqlDcbxLocBytesTxPri6": eqlDcbxLocBytesTxPri6,
       "eqlDcbxLocBytesTxPri7": eqlDcbxLocBytesTxPri7,
       "eqlDcbCnRpPortPriCreatedRpsPri0": eqlDcbCnRpPortPriCreatedRpsPri0,
       "eqlDcbCnRpPortPriCreatedRpsPri1": eqlDcbCnRpPortPriCreatedRpsPri1,
       "eqlDcbCnRpPortPriCreatedRpsPri2": eqlDcbCnRpPortPriCreatedRpsPri2,
       "eqlDcbCnRpPortPriCreatedRpsPri3": eqlDcbCnRpPortPriCreatedRpsPri3,
       "eqlDcbCnRpPortPriCreatedRpsPri4": eqlDcbCnRpPortPriCreatedRpsPri4,
       "eqlDcbCnRpPortPriCreatedRpsPri5": eqlDcbCnRpPortPriCreatedRpsPri5,
       "eqlDcbCnRpPortPriCreatedRpsPri6": eqlDcbCnRpPortPriCreatedRpsPri6,
       "eqlDcbCnRpPortPriCreatedRpsPri7": eqlDcbCnRpPortPriCreatedRpsPri7,
       "eqlDcbCnRpPortPriCentisecondsPri0": eqlDcbCnRpPortPriCentisecondsPri0,
       "eqlDcbCnRpPortPriCentisecondsPri1": eqlDcbCnRpPortPriCentisecondsPri1,
       "eqlDcbCnRpPortPriCentisecondsPri2": eqlDcbCnRpPortPriCentisecondsPri2,
       "eqlDcbCnRpPortPriCentisecondsPri3": eqlDcbCnRpPortPriCentisecondsPri3,
       "eqlDcbCnRpPortPriCentisecondsPri4": eqlDcbCnRpPortPriCentisecondsPri4,
       "eqlDcbCnRpPortPriCentisecondsPri5": eqlDcbCnRpPortPriCentisecondsPri5,
       "eqlDcbCnRpPortPriCentisecondsPri6": eqlDcbCnRpPortPriCentisecondsPri6,
       "eqlDcbCnRpPortPriCentisecondsPri7": eqlDcbCnRpPortPriCentisecondsPri7,
       "eqlDcbxLocPfcPausePri0": eqlDcbxLocPfcPausePri0,
       "eqlDcbxLocPfcPausePri1": eqlDcbxLocPfcPausePri1,
       "eqlDcbxLocPfcPausePri2": eqlDcbxLocPfcPausePri2,
       "eqlDcbxLocPfcPausePri3": eqlDcbxLocPfcPausePri3,
       "eqlDcbxLocPfcPausePri4": eqlDcbxLocPfcPausePri4,
       "eqlDcbxLocPfcPausePri5": eqlDcbxLocPfcPausePri5,
       "eqlDcbxLocPfcPausePri6": eqlDcbxLocPfcPausePri6,
       "eqlDcbxLocPfcPausePri7": eqlDcbxLocPfcPausePri7,
       "eqlDcbxLocPfcUnpausePri0": eqlDcbxLocPfcUnpausePri0,
       "eqlDcbxLocPfcUnpausePri1": eqlDcbxLocPfcUnpausePri1,
       "eqlDcbxLocPfcUnpausePri2": eqlDcbxLocPfcUnpausePri2,
       "eqlDcbxLocPfcUnpausePri3": eqlDcbxLocPfcUnpausePri3,
       "eqlDcbxLocPfcUnpausePri4": eqlDcbxLocPfcUnpausePri4,
       "eqlDcbxLocPfcUnpausePri5": eqlDcbxLocPfcUnpausePri5,
       "eqlDcbxLocPfcUnpausePri6": eqlDcbxLocPfcUnpausePri6,
       "eqlDcbxLocPfcUnpausePri7": eqlDcbxLocPfcUnpausePri7,
       "eqlDcbxLocETSConTsaTc0": eqlDcbxLocETSConTsaTc0,
       "eqlDcbxLocETSConTsaTc1": eqlDcbxLocETSConTsaTc1,
       "eqlDcbxLocETSConTsaTc2": eqlDcbxLocETSConTsaTc2,
       "eqlDcbxLocETSConTsaTc3": eqlDcbxLocETSConTsaTc3,
       "eqlDcbxLocETSConTsaTc4": eqlDcbxLocETSConTsaTc4,
       "eqlDcbxLocETSConTsaTc5": eqlDcbxLocETSConTsaTc5,
       "eqlDcbxLocETSConTsaTc6": eqlDcbxLocETSConTsaTc6,
       "eqlDcbxLocETSConTsaTc7": eqlDcbxLocETSConTsaTc7,
       "eqlDcbxLocETSRecoTsaTc0": eqlDcbxLocETSRecoTsaTc0,
       "eqlDcbxLocETSRecoTsaTc1": eqlDcbxLocETSRecoTsaTc1,
       "eqlDcbxLocETSRecoTsaTc2": eqlDcbxLocETSRecoTsaTc2,
       "eqlDcbxLocETSRecoTsaTc3": eqlDcbxLocETSRecoTsaTc3,
       "eqlDcbxLocETSRecoTsaTc4": eqlDcbxLocETSRecoTsaTc4,
       "eqlDcbxLocETSRecoTsaTc5": eqlDcbxLocETSRecoTsaTc5,
       "eqlDcbxLocETSRecoTsaTc6": eqlDcbxLocETSRecoTsaTc6,
       "eqlDcbxLocETSRecoTsaTc7": eqlDcbxLocETSRecoTsaTc7,
       "eqlDcbxRemETSConTsaTc0": eqlDcbxRemETSConTsaTc0,
       "eqlDcbxRemETSConTsaTc1": eqlDcbxRemETSConTsaTc1,
       "eqlDcbxRemETSConTsaTc2": eqlDcbxRemETSConTsaTc2,
       "eqlDcbxRemETSConTsaTc3": eqlDcbxRemETSConTsaTc3,
       "eqlDcbxRemETSConTsaTc4": eqlDcbxRemETSConTsaTc4,
       "eqlDcbxRemETSConTsaTc5": eqlDcbxRemETSConTsaTc5,
       "eqlDcbxRemETSConTsaTc6": eqlDcbxRemETSConTsaTc6,
       "eqlDcbxRemETSConTsaTc7": eqlDcbxRemETSConTsaTc7,
       "eqlDcbxRemETSRecoTsaTc0": eqlDcbxRemETSRecoTsaTc0,
       "eqlDcbxRemETSRecoTsaTc1": eqlDcbxRemETSRecoTsaTc1,
       "eqlDcbxRemETSRecoTsaTc2": eqlDcbxRemETSRecoTsaTc2,
       "eqlDcbxRemETSRecoTsaTc3": eqlDcbxRemETSRecoTsaTc3,
       "eqlDcbxRemETSRecoTsaTc4": eqlDcbxRemETSRecoTsaTc4,
       "eqlDcbxRemETSRecoTsaTc5": eqlDcbxRemETSRecoTsaTc5,
       "eqlDcbxRemETSRecoTsaTc6": eqlDcbxRemETSRecoTsaTc6,
       "eqlDcbxRemETSRecoTsaTc7": eqlDcbxRemETSRecoTsaTc7,
       "eqlDcbxLocDCBMode": eqlDcbxLocDCBMode}
)
