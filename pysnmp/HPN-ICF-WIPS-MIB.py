# SNMP MIB module (HPN-ICF-WIPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-WIPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:17 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfWIPS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118)
)
hpnicfWIPS.setRevisions(
        ("2011-12-29 14:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfWIPSRadioType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11an", 32),
          ("dot11b", 2),
          ("dot11g", 4),
          ("dot11gn", 16),
          ("dot11n", 8))
    )



class HpnicfWIPSDevStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )



class HpnicfWIPSDevCategoryWay(Integer32, TextualConvention):
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
        *(("autoByDev", 3),
          ("autoByNMS", 2),
          ("manual", 1))
    )



class HpnicfWIPSDeviceCategoryType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("adhoc", 7),
          ("authorizedAP", 1),
          ("authorizedClient", 2),
          ("bridge", 8),
          ("externalAP", 6),
          ("misassociatedClient", 9),
          ("misconfiguredAP", 3),
          ("none", 0),
          ("potentialAuthorizedAP", 10),
          ("potentialExternalAP", 12),
          ("potentialRogueAP", 11),
          ("rogueAP", 4),
          ("unauthorizedClient", 5),
          ("uncategorizedAP", 13),
          ("uncategorizedClient", 14))
    )



class HpnicfWIPSAPCategoryType(Integer32, TextualConvention):
    status = "current"
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
        *(("adhoc", 1),
          ("authorized", 2),
          ("external", 5),
          ("misconfigured", 4),
          ("potentialAuthorized", 6),
          ("potentialExternal", 8),
          ("potentialRogue", 7),
          ("rogue", 3),
          ("uncategorized", 9))
    )



class HpnicfWIPSClientCategoryType(Integer32, TextualConvention):
    status = "current"
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
        *(("authorized", 1),
          ("misassociated", 3),
          ("unauthorized", 2),
          ("uncategorized", 4))
    )



class HpnicfWIPSChannel(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 224),
    )



class HpnicfWIPSEncryptMethod(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class HpnicfWIPSAuthMethod(Integer32, TextualConvention):
    status = "current"
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
        *(("dot1x", 3),
          ("none", 1),
          ("other", 4),
          ("psk", 2))
    )



class HpnicfWIPSAPClassifyType(Integer32, TextualConvention):
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
        *(("authorized", 2),
          ("external", 3),
          ("misconfigured", 4),
          ("other", 1),
          ("rogue", 5))
    )



class HpnicfWIPSAPSecurityType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_HpnicfWIPSConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfWIPSConfigGroup = _HpnicfWIPSConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1)
)
_HpnicfWIPSGlobalConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfWIPSGlobalConfigGroup = _HpnicfWIPSGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1)
)
_HpnicfWIPSEnable_Type = TruthValue
_HpnicfWIPSEnable_Object = MibScalar
hpnicfWIPSEnable = _HpnicfWIPSEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 1),
    _HpnicfWIPSEnable_Type()
)
hpnicfWIPSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSEnable.setStatus("current")
_HpnicfWIPSSensorLicenseNum_Type = Unsigned32
_HpnicfWIPSSensorLicenseNum_Object = MibScalar
hpnicfWIPSSensorLicenseNum = _HpnicfWIPSSensorLicenseNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 2),
    _HpnicfWIPSSensorLicenseNum_Type()
)
hpnicfWIPSSensorLicenseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSSensorLicenseNum.setStatus("current")


class _HpnicfWIPSBlocklistAction_Type(Integer32):
    """Custom type hpnicfWIPSBlocklistAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("unblock", 2))
    )


_HpnicfWIPSBlocklistAction_Type.__name__ = "Integer32"
_HpnicfWIPSBlocklistAction_Object = MibScalar
hpnicfWIPSBlocklistAction = _HpnicfWIPSBlocklistAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 3),
    _HpnicfWIPSBlocklistAction_Type()
)
hpnicfWIPSBlocklistAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSBlocklistAction.setStatus("current")


class _HpnicfWIPSAPInactiveTime_Type(Integer32):
    """Custom type hpnicfWIPSAPInactiveTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_HpnicfWIPSAPInactiveTime_Type.__name__ = "Integer32"
_HpnicfWIPSAPInactiveTime_Object = MibScalar
hpnicfWIPSAPInactiveTime = _HpnicfWIPSAPInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 4),
    _HpnicfWIPSAPInactiveTime_Type()
)
hpnicfWIPSAPInactiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSAPInactiveTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfWIPSAPInactiveTime.setUnits("second")


class _HpnicfWIPSSTAInactiveTime_Type(Integer32):
    """Custom type hpnicfWIPSSTAInactiveTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 1200),
    )


_HpnicfWIPSSTAInactiveTime_Type.__name__ = "Integer32"
_HpnicfWIPSSTAInactiveTime_Object = MibScalar
hpnicfWIPSSTAInactiveTime = _HpnicfWIPSSTAInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 5),
    _HpnicfWIPSSTAInactiveTime_Type()
)
hpnicfWIPSSTAInactiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSSTAInactiveTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfWIPSSTAInactiveTime.setUnits("second")


class _HpnicfWIPSDevAgingTime_Type(Integer32):
    """Custom type hpnicfWIPSDevAgingTime based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2592000),
    )


_HpnicfWIPSDevAgingTime_Type.__name__ = "Integer32"
_HpnicfWIPSDevAgingTime_Object = MibScalar
hpnicfWIPSDevAgingTime = _HpnicfWIPSDevAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 6),
    _HpnicfWIPSDevAgingTime_Type()
)
hpnicfWIPSDevAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDevAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfWIPSDevAgingTime.setUnits("second")


class _HpnicfWIPSStatisticPeriod_Type(Integer32):
    """Custom type hpnicfWIPSStatisticPeriod based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_HpnicfWIPSStatisticPeriod_Type.__name__ = "Integer32"
_HpnicfWIPSStatisticPeriod_Object = MibScalar
hpnicfWIPSStatisticPeriod = _HpnicfWIPSStatisticPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 7),
    _HpnicfWIPSStatisticPeriod_Type()
)
hpnicfWIPSStatisticPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSStatisticPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfWIPSStatisticPeriod.setUnits("second")


class _HpnicfWIPSReclassificationPeriod_Type(Integer32):
    """Custom type hpnicfWIPSReclassificationPeriod based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_HpnicfWIPSReclassificationPeriod_Type.__name__ = "Integer32"
_HpnicfWIPSReclassificationPeriod_Object = MibScalar
hpnicfWIPSReclassificationPeriod = _HpnicfWIPSReclassificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 8),
    _HpnicfWIPSReclassificationPeriod_Type()
)
hpnicfWIPSReclassificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSReclassificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfWIPSReclassificationPeriod.setUnits("second")
_HpnicfWIPSResetAllTrustList_Type = TruthValue
_HpnicfWIPSResetAllTrustList_Object = MibScalar
hpnicfWIPSResetAllTrustList = _HpnicfWIPSResetAllTrustList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 9),
    _HpnicfWIPSResetAllTrustList_Type()
)
hpnicfWIPSResetAllTrustList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSResetAllTrustList.setStatus("current")
_HpnicfWIPSResetAllBlockList_Type = TruthValue
_HpnicfWIPSResetAllBlockList_Object = MibScalar
hpnicfWIPSResetAllBlockList = _HpnicfWIPSResetAllBlockList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 10),
    _HpnicfWIPSResetAllBlockList_Type()
)
hpnicfWIPSResetAllBlockList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSResetAllBlockList.setStatus("current")
_HpnicfWIPSResetAllIgnoreList_Type = TruthValue
_HpnicfWIPSResetAllIgnoreList_Object = MibScalar
hpnicfWIPSResetAllIgnoreList = _HpnicfWIPSResetAllIgnoreList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 11),
    _HpnicfWIPSResetAllIgnoreList_Type()
)
hpnicfWIPSResetAllIgnoreList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSResetAllIgnoreList.setStatus("current")
_HpnicfWIPSResetAllCtmList_Type = TruthValue
_HpnicfWIPSResetAllCtmList_Object = MibScalar
hpnicfWIPSResetAllCtmList = _HpnicfWIPSResetAllCtmList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 12),
    _HpnicfWIPSResetAllCtmList_Type()
)
hpnicfWIPSResetAllCtmList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSResetAllCtmList.setStatus("current")


class _HpnicfWIPSPermitChlBitMap_Type(OctetString):
    """Custom type hpnicfWIPSPermitChlBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HpnicfWIPSPermitChlBitMap_Type.__name__ = "OctetString"
_HpnicfWIPSPermitChlBitMap_Object = MibScalar
hpnicfWIPSPermitChlBitMap = _HpnicfWIPSPermitChlBitMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 13),
    _HpnicfWIPSPermitChlBitMap_Type()
)
hpnicfWIPSPermitChlBitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSPermitChlBitMap.setStatus("current")


class _HpnicfWIPSDynamicTrustListAgingTime_Type(Integer32):
    """Custom type hpnicfWIPSDynamicTrustListAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_HpnicfWIPSDynamicTrustListAgingTime_Type.__name__ = "Integer32"
_HpnicfWIPSDynamicTrustListAgingTime_Object = MibScalar
hpnicfWIPSDynamicTrustListAgingTime = _HpnicfWIPSDynamicTrustListAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 14),
    _HpnicfWIPSDynamicTrustListAgingTime_Type()
)
hpnicfWIPSDynamicTrustListAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDynamicTrustListAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfWIPSDynamicTrustListAgingTime.setUnits("second")


class _HpnicfWIPSDevUpdateTime_Type(Integer32):
    """Custom type hpnicfWIPSDevUpdateTime based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_HpnicfWIPSDevUpdateTime_Type.__name__ = "Integer32"
_HpnicfWIPSDevUpdateTime_Object = MibScalar
hpnicfWIPSDevUpdateTime = _HpnicfWIPSDevUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 15),
    _HpnicfWIPSDevUpdateTime_Type()
)
hpnicfWIPSDevUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDevUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfWIPSDevUpdateTime.setUnits("second")


class _HpnicfWIPSADOSEnable_Type(TruthValue):
    """Custom type hpnicfWIPSADOSEnable based on TruthValue"""


_HpnicfWIPSADOSEnable_Object = MibScalar
hpnicfWIPSADOSEnable = _HpnicfWIPSADOSEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 16),
    _HpnicfWIPSADOSEnable_Type()
)
hpnicfWIPSADOSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSADOSEnable.setStatus("current")


class _HpnicfWIPSAccessFlowScanEnable_Type(TruthValue):
    """Custom type hpnicfWIPSAccessFlowScanEnable based on TruthValue"""


_HpnicfWIPSAccessFlowScanEnable_Object = MibScalar
hpnicfWIPSAccessFlowScanEnable = _HpnicfWIPSAccessFlowScanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 1, 17),
    _HpnicfWIPSAccessFlowScanEnable_Type()
)
hpnicfWIPSAccessFlowScanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSAccessFlowScanEnable.setStatus("current")
_HpnicfWIPSVsdConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfWIPSVsdConfigGroup = _HpnicfWIPSVsdConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2)
)
_HpnicfWIPSVsdTable_Object = MibTable
hpnicfWIPSVsdTable = _HpnicfWIPSVsdTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfWIPSVsdTable.setStatus("current")
_HpnicfWIPSVsdEntry_Object = MibTableRow
hpnicfWIPSVsdEntry = _HpnicfWIPSVsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 1, 1)
)
hpnicfWIPSVsdEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSVsdNameCfg"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSVsdEntry.setStatus("current")


class _HpnicfWIPSVsdNameCfg_Type(OctetString):
    """Custom type hpnicfWIPSVsdNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSVsdNameCfg_Type.__name__ = "OctetString"
_HpnicfWIPSVsdNameCfg_Object = MibTableColumn
hpnicfWIPSVsdNameCfg = _HpnicfWIPSVsdNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 1, 1, 1),
    _HpnicfWIPSVsdNameCfg_Type()
)
hpnicfWIPSVsdNameCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSVsdNameCfg.setStatus("current")
_HpnicfWIPSVsdRowStatus_Type = RowStatus
_HpnicfWIPSVsdRowStatus_Object = MibTableColumn
hpnicfWIPSVsdRowStatus = _HpnicfWIPSVsdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 1, 1, 2),
    _HpnicfWIPSVsdRowStatus_Type()
)
hpnicfWIPSVsdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSVsdRowStatus.setStatus("current")


class _HpnicfWIPSVsdAtkDctPolicyNameCfg_Type(OctetString):
    """Custom type hpnicfWIPSVsdAtkDctPolicyNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfWIPSVsdAtkDctPolicyNameCfg_Type.__name__ = "OctetString"
_HpnicfWIPSVsdAtkDctPolicyNameCfg_Object = MibTableColumn
hpnicfWIPSVsdAtkDctPolicyNameCfg = _HpnicfWIPSVsdAtkDctPolicyNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 1, 1, 3),
    _HpnicfWIPSVsdAtkDctPolicyNameCfg_Type()
)
hpnicfWIPSVsdAtkDctPolicyNameCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSVsdAtkDctPolicyNameCfg.setStatus("current")


class _HpnicfWIPSVsdCtmPolicyNameCfg_Type(OctetString):
    """Custom type hpnicfWIPSVsdCtmPolicyNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfWIPSVsdCtmPolicyNameCfg_Type.__name__ = "OctetString"
_HpnicfWIPSVsdCtmPolicyNameCfg_Object = MibTableColumn
hpnicfWIPSVsdCtmPolicyNameCfg = _HpnicfWIPSVsdCtmPolicyNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 1, 1, 4),
    _HpnicfWIPSVsdCtmPolicyNameCfg_Type()
)
hpnicfWIPSVsdCtmPolicyNameCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSVsdCtmPolicyNameCfg.setStatus("current")


class _HpnicfWIPSVsdSigPolicyNameCfg_Type(OctetString):
    """Custom type hpnicfWIPSVsdSigPolicyNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfWIPSVsdSigPolicyNameCfg_Type.__name__ = "OctetString"
_HpnicfWIPSVsdSigPolicyNameCfg_Object = MibTableColumn
hpnicfWIPSVsdSigPolicyNameCfg = _HpnicfWIPSVsdSigPolicyNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 1, 1, 5),
    _HpnicfWIPSVsdSigPolicyNameCfg_Type()
)
hpnicfWIPSVsdSigPolicyNameCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSVsdSigPolicyNameCfg.setStatus("current")


class _HpnicfWIPSVsdMalPktPolicyNameCfg_Type(OctetString):
    """Custom type hpnicfWIPSVsdMalPktPolicyNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfWIPSVsdMalPktPolicyNameCfg_Type.__name__ = "OctetString"
_HpnicfWIPSVsdMalPktPolicyNameCfg_Object = MibTableColumn
hpnicfWIPSVsdMalPktPolicyNameCfg = _HpnicfWIPSVsdMalPktPolicyNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 1, 1, 6),
    _HpnicfWIPSVsdMalPktPolicyNameCfg_Type()
)
hpnicfWIPSVsdMalPktPolicyNameCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSVsdMalPktPolicyNameCfg.setStatus("current")
_HpnicfWIPSRule2VsdTable_Object = MibTable
hpnicfWIPSRule2VsdTable = _HpnicfWIPSRule2VsdTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfWIPSRule2VsdTable.setStatus("current")
_HpnicfWIPSRule2VsdEntry_Object = MibTableRow
hpnicfWIPSRule2VsdEntry = _HpnicfWIPSRule2VsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 2, 1)
)
hpnicfWIPSRule2VsdEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSVsdNameCfg"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSRule2VsdAPClaRuleNameCfg"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSRule2VsdEntry.setStatus("current")


class _HpnicfWIPSRule2VsdAPClaRuleNameCfg_Type(OctetString):
    """Custom type hpnicfWIPSRule2VsdAPClaRuleNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSRule2VsdAPClaRuleNameCfg_Type.__name__ = "OctetString"
_HpnicfWIPSRule2VsdAPClaRuleNameCfg_Object = MibTableColumn
hpnicfWIPSRule2VsdAPClaRuleNameCfg = _HpnicfWIPSRule2VsdAPClaRuleNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 2, 1, 1),
    _HpnicfWIPSRule2VsdAPClaRuleNameCfg_Type()
)
hpnicfWIPSRule2VsdAPClaRuleNameCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSRule2VsdAPClaRuleNameCfg.setStatus("current")
_HpnicfWIPSRule2VsdRowStatus_Type = RowStatus
_HpnicfWIPSRule2VsdRowStatus_Object = MibTableColumn
hpnicfWIPSRule2VsdRowStatus = _HpnicfWIPSRule2VsdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 2, 1, 2),
    _HpnicfWIPSRule2VsdRowStatus_Type()
)
hpnicfWIPSRule2VsdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSRule2VsdRowStatus.setStatus("current")


class _HpnicfWIPSRule2VsdPrecedence_Type(Integer32):
    """Custom type hpnicfWIPSRule2VsdPrecedence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfWIPSRule2VsdPrecedence_Type.__name__ = "Integer32"
_HpnicfWIPSRule2VsdPrecedence_Object = MibTableColumn
hpnicfWIPSRule2VsdPrecedence = _HpnicfWIPSRule2VsdPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 2, 1, 3),
    _HpnicfWIPSRule2VsdPrecedence_Type()
)
hpnicfWIPSRule2VsdPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSRule2VsdPrecedence.setStatus("current")
_HpnicfWIPSSensor2VsdTable_Object = MibTable
hpnicfWIPSSensor2VsdTable = _HpnicfWIPSSensor2VsdTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfWIPSSensor2VsdTable.setStatus("current")
_HpnicfWIPSSensor2VsdEntry_Object = MibTableRow
hpnicfWIPSSensor2VsdEntry = _HpnicfWIPSSensor2VsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 3, 1)
)
hpnicfWIPSSensor2VsdEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSVsdNameCfg"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSSensorNameCfg"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSSensor2VsdEntry.setStatus("current")


class _HpnicfWIPSSensorNameCfg_Type(OctetString):
    """Custom type hpnicfWIPSSensorNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfWIPSSensorNameCfg_Type.__name__ = "OctetString"
_HpnicfWIPSSensorNameCfg_Object = MibTableColumn
hpnicfWIPSSensorNameCfg = _HpnicfWIPSSensorNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 3, 1, 1),
    _HpnicfWIPSSensorNameCfg_Type()
)
hpnicfWIPSSensorNameCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSSensorNameCfg.setStatus("current")
_HpnicfWIPSSensor2VsdRowStatus_Type = RowStatus
_HpnicfWIPSSensor2VsdRowStatus_Object = MibTableColumn
hpnicfWIPSSensor2VsdRowStatus = _HpnicfWIPSSensor2VsdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 3, 1, 2),
    _HpnicfWIPSSensor2VsdRowStatus_Type()
)
hpnicfWIPSSensor2VsdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSensor2VsdRowStatus.setStatus("current")


class _HpnicfWIPSSensorState_Type(Integer32):
    """Custom type hpnicfWIPSSensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("running", 1))
    )


_HpnicfWIPSSensorState_Type.__name__ = "Integer32"
_HpnicfWIPSSensorState_Object = MibTableColumn
hpnicfWIPSSensorState = _HpnicfWIPSSensorState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 3, 1, 3),
    _HpnicfWIPSSensorState_Type()
)
hpnicfWIPSSensorState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSensorState.setStatus("current")
_HpnicfWIPSSensorRadioTable_Object = MibTable
hpnicfWIPSSensorRadioTable = _HpnicfWIPSSensorRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfWIPSSensorRadioTable.setStatus("current")
_HpnicfWIPSSensorRadioEntry_Object = MibTableRow
hpnicfWIPSSensorRadioEntry = _HpnicfWIPSSensorRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 4, 1)
)
hpnicfWIPSSensorRadioEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSVsdNameCfg"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSSensorNameCfg"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSSensorRadioRadioId"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSSensorRadioEntry.setStatus("current")


class _HpnicfWIPSSensorRadioRadioId_Type(Integer32):
    """Custom type hpnicfWIPSSensorRadioRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HpnicfWIPSSensorRadioRadioId_Type.__name__ = "Integer32"
_HpnicfWIPSSensorRadioRadioId_Object = MibTableColumn
hpnicfWIPSSensorRadioRadioId = _HpnicfWIPSSensorRadioRadioId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 4, 1, 1),
    _HpnicfWIPSSensorRadioRadioId_Type()
)
hpnicfWIPSSensorRadioRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSSensorRadioRadioId.setStatus("current")


class _HpnicfWIPSSensorRadioScanMode_Type(Integer32):
    """Custom type hpnicfWIPSSensorRadioScanMode based on Integer32"""
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
        *(("accessFirst", 1),
          ("detectFirst", 2),
          ("detectOnly", 4),
          ("middle", 3))
    )


_HpnicfWIPSSensorRadioScanMode_Type.__name__ = "Integer32"
_HpnicfWIPSSensorRadioScanMode_Object = MibTableColumn
hpnicfWIPSSensorRadioScanMode = _HpnicfWIPSSensorRadioScanMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 2, 4, 1, 2),
    _HpnicfWIPSSensorRadioScanMode_Type()
)
hpnicfWIPSSensorRadioScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSSensorRadioScanMode.setStatus("current")
_HpnicfWIPSAPClaRuleTable_Object = MibTable
hpnicfWIPSAPClaRuleTable = _HpnicfWIPSAPClaRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfWIPSAPClaRuleTable.setStatus("current")
_HpnicfWIPSAPClaRuleEntry_Object = MibTableRow
hpnicfWIPSAPClaRuleEntry = _HpnicfWIPSAPClaRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1)
)
hpnicfWIPSAPClaRuleEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSAPClaRuleName"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSAPClaRuleEntry.setStatus("current")


class _HpnicfWIPSAPClaRuleName_Type(OctetString):
    """Custom type hpnicfWIPSAPClaRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSAPClaRuleName_Type.__name__ = "OctetString"
_HpnicfWIPSAPClaRuleName_Object = MibTableColumn
hpnicfWIPSAPClaRuleName = _HpnicfWIPSAPClaRuleName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 1),
    _HpnicfWIPSAPClaRuleName_Type()
)
hpnicfWIPSAPClaRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSAPClaRuleName.setStatus("current")
_HpnicfWIPSAPClaRowStatus_Type = RowStatus
_HpnicfWIPSAPClaRowStatus_Object = MibTableColumn
hpnicfWIPSAPClaRowStatus = _HpnicfWIPSAPClaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 2),
    _HpnicfWIPSAPClaRowStatus_Type()
)
hpnicfWIPSAPClaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAPClaRowStatus.setStatus("current")


class _HpnicfWIPSAPClaSeverityLevel_Type(Unsigned32):
    """Custom type hpnicfWIPSAPClaSeverityLevel based on Unsigned32"""
    defaultHexValue = 4294967295


_HpnicfWIPSAPClaSeverityLevel_Object = MibTableColumn
hpnicfWIPSAPClaSeverityLevel = _HpnicfWIPSAPClaSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 3),
    _HpnicfWIPSAPClaSeverityLevel_Type()
)
hpnicfWIPSAPClaSeverityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAPClaSeverityLevel.setStatus("current")


class _HpnicfWIPSAPClaRuleMatchAll_Type(TruthValue):
    """Custom type hpnicfWIPSAPClaRuleMatchAll based on TruthValue"""


_HpnicfWIPSAPClaRuleMatchAll_Object = MibTableColumn
hpnicfWIPSAPClaRuleMatchAll = _HpnicfWIPSAPClaRuleMatchAll_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 4),
    _HpnicfWIPSAPClaRuleMatchAll_Type()
)
hpnicfWIPSAPClaRuleMatchAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAPClaRuleMatchAll.setStatus("current")
_HpnicfWIPSAPClaType_Type = HpnicfWIPSAPClassifyType
_HpnicfWIPSAPClaType_Object = MibTableColumn
hpnicfWIPSAPClaType = _HpnicfWIPSAPClaType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 5),
    _HpnicfWIPSAPClaType_Type()
)
hpnicfWIPSAPClaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAPClaType.setStatus("current")


class _HpnicfWIPSAPClaSubRuleSSIDOperator_Type(Integer32):
    """Custom type hpnicfWIPSAPClaSubRuleSSIDOperator based on Integer32"""
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
        *(("equal", 3),
          ("include", 1),
          ("notequal", 4),
          ("notinclude", 2))
    )


_HpnicfWIPSAPClaSubRuleSSIDOperator_Type.__name__ = "Integer32"
_HpnicfWIPSAPClaSubRuleSSIDOperator_Object = MibTableColumn
hpnicfWIPSAPClaSubRuleSSIDOperator = _HpnicfWIPSAPClaSubRuleSSIDOperator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 6),
    _HpnicfWIPSAPClaSubRuleSSIDOperator_Type()
)
hpnicfWIPSAPClaSubRuleSSIDOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAPClaSubRuleSSIDOperator.setStatus("current")


class _HpnicfWIPSAPClaSubRuleSSIDCase_Type(TruthValue):
    """Custom type hpnicfWIPSAPClaSubRuleSSIDCase based on TruthValue"""


_HpnicfWIPSAPClaSubRuleSSIDCase_Object = MibTableColumn
hpnicfWIPSAPClaSubRuleSSIDCase = _HpnicfWIPSAPClaSubRuleSSIDCase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 7),
    _HpnicfWIPSAPClaSubRuleSSIDCase_Type()
)
hpnicfWIPSAPClaSubRuleSSIDCase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAPClaSubRuleSSIDCase.setStatus("current")


class _HpnicfWIPSAPClaSubRuleSSID_Type(OctetString):
    """Custom type hpnicfWIPSAPClaSubRuleSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfWIPSAPClaSubRuleSSID_Type.__name__ = "OctetString"
_HpnicfWIPSAPClaSubRuleSSID_Object = MibTableColumn
hpnicfWIPSAPClaSubRuleSSID = _HpnicfWIPSAPClaSubRuleSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 8),
    _HpnicfWIPSAPClaSubRuleSSID_Type()
)
hpnicfWIPSAPClaSubRuleSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAPClaSubRuleSSID.setStatus("current")


class _HpnicfWIPSSecurityType_Type(HpnicfWIPSAPSecurityType):
    """Custom type hpnicfWIPSSecurityType based on HpnicfWIPSAPSecurityType"""
    defaultHexValue = 4294967295


_HpnicfWIPSSecurityType_Object = MibTableColumn
hpnicfWIPSSecurityType = _HpnicfWIPSSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 9),
    _HpnicfWIPSSecurityType_Type()
)
hpnicfWIPSSecurityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSecurityType.setStatus("current")


class _HpnicfWIPSSecurityTypeMatch_Type(Integer32):
    """Custom type hpnicfWIPSSecurityTypeMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("include", 2))
    )


_HpnicfWIPSSecurityTypeMatch_Type.__name__ = "Integer32"
_HpnicfWIPSSecurityTypeMatch_Object = MibTableColumn
hpnicfWIPSSecurityTypeMatch = _HpnicfWIPSSecurityTypeMatch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 10),
    _HpnicfWIPSSecurityTypeMatch_Type()
)
hpnicfWIPSSecurityTypeMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSecurityTypeMatch.setStatus("current")


class _HpnicfWIPSAPAuthType_Type(Integer32):
    """Custom type hpnicfWIPSAPAuthType based on Integer32"""
    defaultValue = 5

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
        *(("dot1x", 3),
          ("none", 1),
          ("other", 4),
          ("psk", 2),
          ("undo", 5))
    )


_HpnicfWIPSAPAuthType_Type.__name__ = "Integer32"
_HpnicfWIPSAPAuthType_Object = MibTableColumn
hpnicfWIPSAPAuthType = _HpnicfWIPSAPAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 11),
    _HpnicfWIPSAPAuthType_Type()
)
hpnicfWIPSAPAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAPAuthType.setStatus("current")


class _HpnicfWIPSMaxRSSIValue_Type(Unsigned32):
    """Custom type hpnicfWIPSMaxRSSIValue based on Unsigned32"""
    defaultHexValue = 4294967295


_HpnicfWIPSMaxRSSIValue_Object = MibTableColumn
hpnicfWIPSMaxRSSIValue = _HpnicfWIPSMaxRSSIValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 12),
    _HpnicfWIPSMaxRSSIValue_Type()
)
hpnicfWIPSMaxRSSIValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMaxRSSIValue.setStatus("current")


class _HpnicfWIPSMinRSSIValue_Type(Unsigned32):
    """Custom type hpnicfWIPSMinRSSIValue based on Unsigned32"""
    defaultHexValue = 4294967295


_HpnicfWIPSMinRSSIValue_Object = MibTableColumn
hpnicfWIPSMinRSSIValue = _HpnicfWIPSMinRSSIValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 13),
    _HpnicfWIPSMinRSSIValue_Type()
)
hpnicfWIPSMinRSSIValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMinRSSIValue.setStatus("current")


class _HpnicfWIPSMaxDuration_Type(Unsigned32):
    """Custom type hpnicfWIPSMaxDuration based on Unsigned32"""
    defaultHexValue = 4294967295


_HpnicfWIPSMaxDuration_Object = MibTableColumn
hpnicfWIPSMaxDuration = _HpnicfWIPSMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 14),
    _HpnicfWIPSMaxDuration_Type()
)
hpnicfWIPSMaxDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfWIPSMaxDuration.setUnits("second")


class _HpnicfWIPSMinDuration_Type(Unsigned32):
    """Custom type hpnicfWIPSMinDuration based on Unsigned32"""
    defaultHexValue = 4294967295


_HpnicfWIPSMinDuration_Object = MibTableColumn
hpnicfWIPSMinDuration = _HpnicfWIPSMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 15),
    _HpnicfWIPSMinDuration_Type()
)
hpnicfWIPSMinDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMinDuration.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfWIPSMinDuration.setUnits("second")


class _HpnicfWIPSMaxAPNum_Type(Unsigned32):
    """Custom type hpnicfWIPSMaxAPNum based on Unsigned32"""
    defaultHexValue = 4294967295


_HpnicfWIPSMaxAPNum_Object = MibTableColumn
hpnicfWIPSMaxAPNum = _HpnicfWIPSMaxAPNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 16),
    _HpnicfWIPSMaxAPNum_Type()
)
hpnicfWIPSMaxAPNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMaxAPNum.setStatus("current")


class _HpnicfWIPSMinAPNum_Type(Unsigned32):
    """Custom type hpnicfWIPSMinAPNum based on Unsigned32"""
    defaultHexValue = 4294967295


_HpnicfWIPSMinAPNum_Object = MibTableColumn
hpnicfWIPSMinAPNum = _HpnicfWIPSMinAPNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 17),
    _HpnicfWIPSMinAPNum_Type()
)
hpnicfWIPSMinAPNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMinAPNum.setStatus("current")


class _HpnicfWIPSMaxClientNum_Type(Unsigned32):
    """Custom type hpnicfWIPSMaxClientNum based on Unsigned32"""
    defaultHexValue = 4294967295


_HpnicfWIPSMaxClientNum_Object = MibTableColumn
hpnicfWIPSMaxClientNum = _HpnicfWIPSMaxClientNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 18),
    _HpnicfWIPSMaxClientNum_Type()
)
hpnicfWIPSMaxClientNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMaxClientNum.setStatus("current")


class _HpnicfWIPSMinClientNum_Type(Unsigned32):
    """Custom type hpnicfWIPSMinClientNum based on Unsigned32"""
    defaultHexValue = 4294967295


_HpnicfWIPSMinClientNum_Object = MibTableColumn
hpnicfWIPSMinClientNum = _HpnicfWIPSMinClientNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 19),
    _HpnicfWIPSMinClientNum_Type()
)
hpnicfWIPSMinClientNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMinClientNum.setStatus("current")


class _HpnicfWIPSOUIInfo_Type(OctetString):
    """Custom type hpnicfWIPSOUIInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HpnicfWIPSOUIInfo_Type.__name__ = "OctetString"
_HpnicfWIPSOUIInfo_Object = MibTableColumn
hpnicfWIPSOUIInfo = _HpnicfWIPSOUIInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 20),
    _HpnicfWIPSOUIInfo_Type()
)
hpnicfWIPSOUIInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSOUIInfo.setStatus("current")


class _HpnicfWIPSVendorInfo_Type(OctetString):
    """Custom type hpnicfWIPSVendorInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfWIPSVendorInfo_Type.__name__ = "OctetString"
_HpnicfWIPSVendorInfo_Object = MibTableColumn
hpnicfWIPSVendorInfo = _HpnicfWIPSVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 3, 1, 21),
    _HpnicfWIPSVendorInfo_Type()
)
hpnicfWIPSVendorInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSVendorInfo.setStatus("current")
_HpnicfWIPSAtkDctPolicyCfgGroup_ObjectIdentity = ObjectIdentity
hpnicfWIPSAtkDctPolicyCfgGroup = _HpnicfWIPSAtkDctPolicyCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4)
)


class _HpnicfWIPSAtkDctPolicyCfgSupportSet_Type(OctetString):
    """Custom type hpnicfWIPSAtkDctPolicyCfgSupportSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HpnicfWIPSAtkDctPolicyCfgSupportSet_Type.__name__ = "OctetString"
_HpnicfWIPSAtkDctPolicyCfgSupportSet_Object = MibScalar
hpnicfWIPSAtkDctPolicyCfgSupportSet = _HpnicfWIPSAtkDctPolicyCfgSupportSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 1),
    _HpnicfWIPSAtkDctPolicyCfgSupportSet_Type()
)
hpnicfWIPSAtkDctPolicyCfgSupportSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyCfgSupportSet.setStatus("current")
_HpnicfWIPSAtkDctPolicyCfgTable_Object = MibTable
hpnicfWIPSAtkDctPolicyCfgTable = _HpnicfWIPSAtkDctPolicyCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyCfgTable.setStatus("current")
_HpnicfWIPSAtkDctPolicyCfgEntry_Object = MibTableRow
hpnicfWIPSAtkDctPolicyCfgEntry = _HpnicfWIPSAtkDctPolicyCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1)
)
hpnicfWIPSAtkDctPolicyCfgEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSAtkDctPolicyName"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyCfgEntry.setStatus("current")


class _HpnicfWIPSAtkDctPolicyName_Type(OctetString):
    """Custom type hpnicfWIPSAtkDctPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSAtkDctPolicyName_Type.__name__ = "OctetString"
_HpnicfWIPSAtkDctPolicyName_Object = MibTableColumn
hpnicfWIPSAtkDctPolicyName = _HpnicfWIPSAtkDctPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1, 1),
    _HpnicfWIPSAtkDctPolicyName_Type()
)
hpnicfWIPSAtkDctPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyName.setStatus("current")
_HpnicfWIPSAtkDctPolicyCfgRowStatus_Type = RowStatus
_HpnicfWIPSAtkDctPolicyCfgRowStatus_Object = MibTableColumn
hpnicfWIPSAtkDctPolicyCfgRowStatus = _HpnicfWIPSAtkDctPolicyCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1, 2),
    _HpnicfWIPSAtkDctPolicyCfgRowStatus_Type()
)
hpnicfWIPSAtkDctPolicyCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyCfgRowStatus.setStatus("current")


class _HpnicfWIPSAtkDctPolicyBitString_Type(OctetString):
    """Custom type hpnicfWIPSAtkDctPolicyBitString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HpnicfWIPSAtkDctPolicyBitString_Type.__name__ = "OctetString"
_HpnicfWIPSAtkDctPolicyBitString_Object = MibTableColumn
hpnicfWIPSAtkDctPolicyBitString = _HpnicfWIPSAtkDctPolicyBitString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1, 3),
    _HpnicfWIPSAtkDctPolicyBitString_Type()
)
hpnicfWIPSAtkDctPolicyBitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyBitString.setStatus("current")


class _HpnicfWIPSAtkDctPolicyAPFloodQT_Type(Integer32):
    """Custom type hpnicfWIPSAtkDctPolicyAPFloodQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_HpnicfWIPSAtkDctPolicyAPFloodQT_Type.__name__ = "Integer32"
_HpnicfWIPSAtkDctPolicyAPFloodQT_Object = MibTableColumn
hpnicfWIPSAtkDctPolicyAPFloodQT = _HpnicfWIPSAtkDctPolicyAPFloodQT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1, 4),
    _HpnicfWIPSAtkDctPolicyAPFloodQT_Type()
)
hpnicfWIPSAtkDctPolicyAPFloodQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyAPFloodQT.setStatus("current")


class _HpnicfWIPSAtkDctPolicyAPSpoofQT_Type(Integer32):
    """Custom type hpnicfWIPSAtkDctPolicyAPSpoofQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_HpnicfWIPSAtkDctPolicyAPSpoofQT_Type.__name__ = "Integer32"
_HpnicfWIPSAtkDctPolicyAPSpoofQT_Object = MibTableColumn
hpnicfWIPSAtkDctPolicyAPSpoofQT = _HpnicfWIPSAtkDctPolicyAPSpoofQT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1, 5),
    _HpnicfWIPSAtkDctPolicyAPSpoofQT_Type()
)
hpnicfWIPSAtkDctPolicyAPSpoofQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyAPSpoofQT.setStatus("current")


class _HpnicfWIPSAtkDctPolicyCliSpoofQT_Type(Integer32):
    """Custom type hpnicfWIPSAtkDctPolicyCliSpoofQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_HpnicfWIPSAtkDctPolicyCliSpoofQT_Type.__name__ = "Integer32"
_HpnicfWIPSAtkDctPolicyCliSpoofQT_Object = MibTableColumn
hpnicfWIPSAtkDctPolicyCliSpoofQT = _HpnicfWIPSAtkDctPolicyCliSpoofQT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1, 6),
    _HpnicfWIPSAtkDctPolicyCliSpoofQT_Type()
)
hpnicfWIPSAtkDctPolicyCliSpoofQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyCliSpoofQT.setStatus("current")


class _HpnicfWIPSAtkDctPolicyDosAssoQT_Type(Integer32):
    """Custom type hpnicfWIPSAtkDctPolicyDosAssoQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_HpnicfWIPSAtkDctPolicyDosAssoQT_Type.__name__ = "Integer32"
_HpnicfWIPSAtkDctPolicyDosAssoQT_Object = MibTableColumn
hpnicfWIPSAtkDctPolicyDosAssoQT = _HpnicfWIPSAtkDctPolicyDosAssoQT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1, 7),
    _HpnicfWIPSAtkDctPolicyDosAssoQT_Type()
)
hpnicfWIPSAtkDctPolicyDosAssoQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyDosAssoQT.setStatus("current")


class _HpnicfWIPSAtkDctPolicyDosAuthQT_Type(Integer32):
    """Custom type hpnicfWIPSAtkDctPolicyDosAuthQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_HpnicfWIPSAtkDctPolicyDosAuthQT_Type.__name__ = "Integer32"
_HpnicfWIPSAtkDctPolicyDosAuthQT_Object = MibTableColumn
hpnicfWIPSAtkDctPolicyDosAuthQT = _HpnicfWIPSAtkDctPolicyDosAuthQT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1, 8),
    _HpnicfWIPSAtkDctPolicyDosAuthQT_Type()
)
hpnicfWIPSAtkDctPolicyDosAuthQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyDosAuthQT.setStatus("current")


class _HpnicfWIPSAtkDctPolicyDosEAPOLStartQT_Type(Integer32):
    """Custom type hpnicfWIPSAtkDctPolicyDosEAPOLStartQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_HpnicfWIPSAtkDctPolicyDosEAPOLStartQT_Type.__name__ = "Integer32"
_HpnicfWIPSAtkDctPolicyDosEAPOLStartQT_Object = MibTableColumn
hpnicfWIPSAtkDctPolicyDosEAPOLStartQT = _HpnicfWIPSAtkDctPolicyDosEAPOLStartQT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1, 9),
    _HpnicfWIPSAtkDctPolicyDosEAPOLStartQT_Type()
)
hpnicfWIPSAtkDctPolicyDosEAPOLStartQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyDosEAPOLStartQT.setStatus("current")


class _HpnicfWIPSAtkDctPolicyDosReAssoQT_Type(Integer32):
    """Custom type hpnicfWIPSAtkDctPolicyDosReAssoQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_HpnicfWIPSAtkDctPolicyDosReAssoQT_Type.__name__ = "Integer32"
_HpnicfWIPSAtkDctPolicyDosReAssoQT_Object = MibTableColumn
hpnicfWIPSAtkDctPolicyDosReAssoQT = _HpnicfWIPSAtkDctPolicyDosReAssoQT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1, 10),
    _HpnicfWIPSAtkDctPolicyDosReAssoQT_Type()
)
hpnicfWIPSAtkDctPolicyDosReAssoQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyDosReAssoQT.setStatus("current")


class _HpnicfWIPSAtkDctPolicyWeakIVQT_Type(Integer32):
    """Custom type hpnicfWIPSAtkDctPolicyWeakIVQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_HpnicfWIPSAtkDctPolicyWeakIVQT_Type.__name__ = "Integer32"
_HpnicfWIPSAtkDctPolicyWeakIVQT_Object = MibTableColumn
hpnicfWIPSAtkDctPolicyWeakIVQT = _HpnicfWIPSAtkDctPolicyWeakIVQT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1, 11),
    _HpnicfWIPSAtkDctPolicyWeakIVQT_Type()
)
hpnicfWIPSAtkDctPolicyWeakIVQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyWeakIVQT.setStatus("current")


class _HpnicfWIPSAtkDctPolicyInvalidOUIAction_Type(Integer32):
    """Custom type hpnicfWIPSAtkDctPolicyInvalidOUIAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rogue", 1))
    )


_HpnicfWIPSAtkDctPolicyInvalidOUIAction_Type.__name__ = "Integer32"
_HpnicfWIPSAtkDctPolicyInvalidOUIAction_Object = MibTableColumn
hpnicfWIPSAtkDctPolicyInvalidOUIAction = _HpnicfWIPSAtkDctPolicyInvalidOUIAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 4, 2, 1, 12),
    _HpnicfWIPSAtkDctPolicyInvalidOUIAction_Type()
)
hpnicfWIPSAtkDctPolicyInvalidOUIAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSAtkDctPolicyInvalidOUIAction.setStatus("current")
_HpnicfWIPSStaticCtmListCfgTable_Object = MibTable
hpnicfWIPSStaticCtmListCfgTable = _HpnicfWIPSStaticCtmListCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfWIPSStaticCtmListCfgTable.setStatus("current")
_HpnicfWIPSStaticCtmListCfgEntry_Object = MibTableRow
hpnicfWIPSStaticCtmListCfgEntry = _HpnicfWIPSStaticCtmListCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 5, 1)
)
hpnicfWIPSStaticCtmListCfgEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSStaticCtmListMAC"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSStaticCtmListCfgEntry.setStatus("current")
_HpnicfWIPSStaticCtmListMAC_Type = MacAddress
_HpnicfWIPSStaticCtmListMAC_Object = MibTableColumn
hpnicfWIPSStaticCtmListMAC = _HpnicfWIPSStaticCtmListMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 5, 1, 1),
    _HpnicfWIPSStaticCtmListMAC_Type()
)
hpnicfWIPSStaticCtmListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSStaticCtmListMAC.setStatus("current")
_HpnicfWIPSStaticCtmListRowStatus_Type = RowStatus
_HpnicfWIPSStaticCtmListRowStatus_Object = MibTableColumn
hpnicfWIPSStaticCtmListRowStatus = _HpnicfWIPSStaticCtmListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 5, 1, 2),
    _HpnicfWIPSStaticCtmListRowStatus_Type()
)
hpnicfWIPSStaticCtmListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSStaticCtmListRowStatus.setStatus("current")
_HpnicfWIPSStaticBlockListCfgTable_Object = MibTable
hpnicfWIPSStaticBlockListCfgTable = _HpnicfWIPSStaticBlockListCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfWIPSStaticBlockListCfgTable.setStatus("current")
_HpnicfWIPSStaticBlockListCfgEntry_Object = MibTableRow
hpnicfWIPSStaticBlockListCfgEntry = _HpnicfWIPSStaticBlockListCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 6, 1)
)
hpnicfWIPSStaticBlockListCfgEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSStaticBlockListMAC"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSStaticBlockListCfgEntry.setStatus("current")
_HpnicfWIPSStaticBlockListMAC_Type = MacAddress
_HpnicfWIPSStaticBlockListMAC_Object = MibTableColumn
hpnicfWIPSStaticBlockListMAC = _HpnicfWIPSStaticBlockListMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 6, 1, 1),
    _HpnicfWIPSStaticBlockListMAC_Type()
)
hpnicfWIPSStaticBlockListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSStaticBlockListMAC.setStatus("current")
_HpnicfWIPSStaticBlockListRowStatus_Type = RowStatus
_HpnicfWIPSStaticBlockListRowStatus_Object = MibTableColumn
hpnicfWIPSStaticBlockListRowStatus = _HpnicfWIPSStaticBlockListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 6, 1, 2),
    _HpnicfWIPSStaticBlockListRowStatus_Type()
)
hpnicfWIPSStaticBlockListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSStaticBlockListRowStatus.setStatus("current")
_HpnicfWIPSStaticTrustListCfgTable_Object = MibTable
hpnicfWIPSStaticTrustListCfgTable = _HpnicfWIPSStaticTrustListCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfWIPSStaticTrustListCfgTable.setStatus("current")
_HpnicfWIPSStaticTrustListCfgEntry_Object = MibTableRow
hpnicfWIPSStaticTrustListCfgEntry = _HpnicfWIPSStaticTrustListCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 7, 1)
)
hpnicfWIPSStaticTrustListCfgEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSStaticTrustListMAC"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSStaticTrustListCfgEntry.setStatus("current")
_HpnicfWIPSStaticTrustListMAC_Type = MacAddress
_HpnicfWIPSStaticTrustListMAC_Object = MibTableColumn
hpnicfWIPSStaticTrustListMAC = _HpnicfWIPSStaticTrustListMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 7, 1, 1),
    _HpnicfWIPSStaticTrustListMAC_Type()
)
hpnicfWIPSStaticTrustListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSStaticTrustListMAC.setStatus("current")
_HpnicfWIPSStaticTrustListRowStatus_Type = RowStatus
_HpnicfWIPSStaticTrustListRowStatus_Object = MibTableColumn
hpnicfWIPSStaticTrustListRowStatus = _HpnicfWIPSStaticTrustListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 7, 1, 2),
    _HpnicfWIPSStaticTrustListRowStatus_Type()
)
hpnicfWIPSStaticTrustListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSStaticTrustListRowStatus.setStatus("current")
_HpnicfWIPSIgnoreListCfgTable_Object = MibTable
hpnicfWIPSIgnoreListCfgTable = _HpnicfWIPSIgnoreListCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 8)
)
if mibBuilder.loadTexts:
    hpnicfWIPSIgnoreListCfgTable.setStatus("current")
_HpnicfWIPSIgnoreListCfgEntry_Object = MibTableRow
hpnicfWIPSIgnoreListCfgEntry = _HpnicfWIPSIgnoreListCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 8, 1)
)
hpnicfWIPSIgnoreListCfgEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSIgnoreListMAC"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSIgnoreListCfgEntry.setStatus("current")
_HpnicfWIPSIgnoreListMAC_Type = MacAddress
_HpnicfWIPSIgnoreListMAC_Object = MibTableColumn
hpnicfWIPSIgnoreListMAC = _HpnicfWIPSIgnoreListMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 8, 1, 1),
    _HpnicfWIPSIgnoreListMAC_Type()
)
hpnicfWIPSIgnoreListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSIgnoreListMAC.setStatus("current")
_HpnicfWIPSIgnoreListRowStatus_Type = RowStatus
_HpnicfWIPSIgnoreListRowStatus_Object = MibTableColumn
hpnicfWIPSIgnoreListRowStatus = _HpnicfWIPSIgnoreListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 8, 1, 2),
    _HpnicfWIPSIgnoreListRowStatus_Type()
)
hpnicfWIPSIgnoreListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSIgnoreListRowStatus.setStatus("current")
_HpnicfWIPSDctModeTable_Object = MibTable
hpnicfWIPSDctModeTable = _HpnicfWIPSDctModeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 9)
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctModeTable.setStatus("current")
_HpnicfWIPSDctModeEntry_Object = MibTableRow
hpnicfWIPSDctModeEntry = _HpnicfWIPSDctModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 9, 1)
)
hpnicfWIPSDctModeEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctModeAPName"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctModeRadio"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctModeEntry.setStatus("current")


class _HpnicfWIPSDctModeAPName_Type(OctetString):
    """Custom type hpnicfWIPSDctModeAPName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfWIPSDctModeAPName_Type.__name__ = "OctetString"
_HpnicfWIPSDctModeAPName_Object = MibTableColumn
hpnicfWIPSDctModeAPName = _HpnicfWIPSDctModeAPName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 9, 1, 1),
    _HpnicfWIPSDctModeAPName_Type()
)
hpnicfWIPSDctModeAPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctModeAPName.setStatus("current")


class _HpnicfWIPSDctModeRadio_Type(Integer32):
    """Custom type hpnicfWIPSDctModeRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HpnicfWIPSDctModeRadio_Type.__name__ = "Integer32"
_HpnicfWIPSDctModeRadio_Object = MibTableColumn
hpnicfWIPSDctModeRadio = _HpnicfWIPSDctModeRadio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 9, 1, 2),
    _HpnicfWIPSDctModeRadio_Type()
)
hpnicfWIPSDctModeRadio.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctModeRadio.setStatus("current")


class _HpnicfWIPSDctModeScanMode_Type(Integer32):
    """Custom type hpnicfWIPSDctModeScanMode based on Integer32"""
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
        *(("accessFirst", 1),
          ("detectFirst", 2),
          ("detectOnly", 4),
          ("middle", 3))
    )


_HpnicfWIPSDctModeScanMode_Type.__name__ = "Integer32"
_HpnicfWIPSDctModeScanMode_Object = MibTableColumn
hpnicfWIPSDctModeScanMode = _HpnicfWIPSDctModeScanMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 9, 1, 3),
    _HpnicfWIPSDctModeScanMode_Type()
)
hpnicfWIPSDctModeScanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSDctModeScanMode.setStatus("current")
_HpnicfWIPSDctModeRowStatus_Type = RowStatus
_HpnicfWIPSDctModeRowStatus_Object = MibTableColumn
hpnicfWIPSDctModeRowStatus = _HpnicfWIPSDctModeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 9, 1, 4),
    _HpnicfWIPSDctModeRowStatus_Type()
)
hpnicfWIPSDctModeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSDctModeRowStatus.setStatus("current")
_HpnicfWIPSSigConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfWIPSSigConfigGroup = _HpnicfWIPSSigConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10)
)
_HpnicfWIPSSigPolicyTable_Object = MibTable
hpnicfWIPSSigPolicyTable = _HpnicfWIPSSigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 1)
)
if mibBuilder.loadTexts:
    hpnicfWIPSSigPolicyTable.setStatus("current")
_HpnicfWIPSSigPolicyEntry_Object = MibTableRow
hpnicfWIPSSigPolicyEntry = _HpnicfWIPSSigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 1, 1)
)
hpnicfWIPSSigPolicyEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSSigPolicyNameCfg"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSSigPolicyEntry.setStatus("current")


class _HpnicfWIPSSigPolicyNameCfg_Type(OctetString):
    """Custom type hpnicfWIPSSigPolicyNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSSigPolicyNameCfg_Type.__name__ = "OctetString"
_HpnicfWIPSSigPolicyNameCfg_Object = MibTableColumn
hpnicfWIPSSigPolicyNameCfg = _HpnicfWIPSSigPolicyNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 1, 1, 1),
    _HpnicfWIPSSigPolicyNameCfg_Type()
)
hpnicfWIPSSigPolicyNameCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSSigPolicyNameCfg.setStatus("current")
_HpnicfWIPSSigPolicyRowStatus_Type = RowStatus
_HpnicfWIPSSigPolicyRowStatus_Object = MibTableColumn
hpnicfWIPSSigPolicyRowStatus = _HpnicfWIPSSigPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 1, 1, 2),
    _HpnicfWIPSSigPolicyRowStatus_Type()
)
hpnicfWIPSSigPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigPolicyRowStatus.setStatus("current")
_HpnicfWIPSSigRule2PolicyTable_Object = MibTable
hpnicfWIPSSigRule2PolicyTable = _HpnicfWIPSSigRule2PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 2)
)
if mibBuilder.loadTexts:
    hpnicfWIPSSigRule2PolicyTable.setStatus("current")
_HpnicfWIPSSigRule2PolicyEntry_Object = MibTableRow
hpnicfWIPSSigRule2PolicyEntry = _HpnicfWIPSSigRule2PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 2, 1)
)
hpnicfWIPSSigRule2PolicyEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSSigPolicyNameCfg"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSSigRule2PolicySigRuleIDCfg"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSSigRule2PolicyEntry.setStatus("current")


class _HpnicfWIPSSigRule2PolicySigRuleIDCfg_Type(Unsigned32):
    """Custom type hpnicfWIPSSigRule2PolicySigRuleIDCfg based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfWIPSSigRule2PolicySigRuleIDCfg_Type.__name__ = "Unsigned32"
_HpnicfWIPSSigRule2PolicySigRuleIDCfg_Object = MibTableColumn
hpnicfWIPSSigRule2PolicySigRuleIDCfg = _HpnicfWIPSSigRule2PolicySigRuleIDCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 2, 1, 1),
    _HpnicfWIPSSigRule2PolicySigRuleIDCfg_Type()
)
hpnicfWIPSSigRule2PolicySigRuleIDCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRule2PolicySigRuleIDCfg.setStatus("current")
_HpnicfWIPSSigRule2PolicyRowStatus_Type = RowStatus
_HpnicfWIPSSigRule2PolicyRowStatus_Object = MibTableColumn
hpnicfWIPSSigRule2PolicyRowStatus = _HpnicfWIPSSigRule2PolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 2, 1, 2),
    _HpnicfWIPSSigRule2PolicyRowStatus_Type()
)
hpnicfWIPSSigRule2PolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRule2PolicyRowStatus.setStatus("current")


class _HpnicfWIPSSigRule2PolicyPrecedence_Type(Unsigned32):
    """Custom type hpnicfWIPSSigRule2PolicyPrecedence based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfWIPSSigRule2PolicyPrecedence_Type.__name__ = "Unsigned32"
_HpnicfWIPSSigRule2PolicyPrecedence_Object = MibTableColumn
hpnicfWIPSSigRule2PolicyPrecedence = _HpnicfWIPSSigRule2PolicyPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 2, 1, 3),
    _HpnicfWIPSSigRule2PolicyPrecedence_Type()
)
hpnicfWIPSSigRule2PolicyPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRule2PolicyPrecedence.setStatus("current")
_HpnicfWIPSSigRuleTable_Object = MibTable
hpnicfWIPSSigRuleTable = _HpnicfWIPSSigRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3)
)
if mibBuilder.loadTexts:
    hpnicfWIPSSigRuleTable.setStatus("current")
_HpnicfWIPSSigRuleEntry_Object = MibTableRow
hpnicfWIPSSigRuleEntry = _HpnicfWIPSSigRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1)
)
hpnicfWIPSSigRuleEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSSigRuleName"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSSigRuleEntry.setStatus("current")


class _HpnicfWIPSSigRuleName_Type(OctetString):
    """Custom type hpnicfWIPSSigRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSSigRuleName_Type.__name__ = "OctetString"
_HpnicfWIPSSigRuleName_Object = MibTableColumn
hpnicfWIPSSigRuleName = _HpnicfWIPSSigRuleName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 1),
    _HpnicfWIPSSigRuleName_Type()
)
hpnicfWIPSSigRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRuleName.setStatus("current")


class _HpnicfWIPSSigRuleID_Type(Integer32):
    """Custom type hpnicfWIPSSigRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfWIPSSigRuleID_Type.__name__ = "Integer32"
_HpnicfWIPSSigRuleID_Object = MibTableColumn
hpnicfWIPSSigRuleID = _HpnicfWIPSSigRuleID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 2),
    _HpnicfWIPSSigRuleID_Type()
)
hpnicfWIPSSigRuleID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRuleID.setStatus("current")
_HpnicfWIPSSigRuleRowStatus_Type = RowStatus
_HpnicfWIPSSigRuleRowStatus_Object = MibTableColumn
hpnicfWIPSSigRuleRowStatus = _HpnicfWIPSSigRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 3),
    _HpnicfWIPSSigRuleRowStatus_Type()
)
hpnicfWIPSSigRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRuleRowStatus.setStatus("current")
_HpnicfWIPSSigSubRuleMatchAll_Type = TruthValue
_HpnicfWIPSSigSubRuleMatchAll_Object = MibTableColumn
hpnicfWIPSSigSubRuleMatchAll = _HpnicfWIPSSigSubRuleMatchAll_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 4),
    _HpnicfWIPSSigSubRuleMatchAll_Type()
)
hpnicfWIPSSigSubRuleMatchAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleMatchAll.setStatus("current")
_HpnicfWIPSSigRuleDctPeriod_Type = Unsigned32
_HpnicfWIPSSigRuleDctPeriod_Object = MibTableColumn
hpnicfWIPSSigRuleDctPeriod = _HpnicfWIPSSigRuleDctPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 5),
    _HpnicfWIPSSigRuleDctPeriod_Type()
)
hpnicfWIPSSigRuleDctPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRuleDctPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRuleDctPeriod.setUnits("second")


class _HpnicfWIPSSigRuleTrackMethod_Type(Integer32):
    """Custom type hpnicfWIPSSigRuleTrackMethod based on Integer32"""
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
          ("perMAC", 2),
          ("perSig", 1))
    )


_HpnicfWIPSSigRuleTrackMethod_Type.__name__ = "Integer32"
_HpnicfWIPSSigRuleTrackMethod_Object = MibTableColumn
hpnicfWIPSSigRuleTrackMethod = _HpnicfWIPSSigRuleTrackMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 6),
    _HpnicfWIPSSigRuleTrackMethod_Type()
)
hpnicfWIPSSigRuleTrackMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRuleTrackMethod.setStatus("current")
_HpnicfWIPSSigRuleDctThresholdPerMAC_Type = Unsigned32
_HpnicfWIPSSigRuleDctThresholdPerMAC_Object = MibTableColumn
hpnicfWIPSSigRuleDctThresholdPerMAC = _HpnicfWIPSSigRuleDctThresholdPerMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 7),
    _HpnicfWIPSSigRuleDctThresholdPerMAC_Type()
)
hpnicfWIPSSigRuleDctThresholdPerMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRuleDctThresholdPerMAC.setStatus("current")
_HpnicfWIPSSigRuleDctThresholdPerSig_Type = Unsigned32
_HpnicfWIPSSigRuleDctThresholdPerSig_Object = MibTableColumn
hpnicfWIPSSigRuleDctThresholdPerSig = _HpnicfWIPSSigRuleDctThresholdPerSig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 8),
    _HpnicfWIPSSigRuleDctThresholdPerSig_Type()
)
hpnicfWIPSSigRuleDctThresholdPerSig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRuleDctThresholdPerSig.setStatus("current")
_HpnicfWIPSSigRuleActionEvtLevel_Type = Unsigned32
_HpnicfWIPSSigRuleActionEvtLevel_Object = MibTableColumn
hpnicfWIPSSigRuleActionEvtLevel = _HpnicfWIPSSigRuleActionEvtLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 9),
    _HpnicfWIPSSigRuleActionEvtLevel_Type()
)
hpnicfWIPSSigRuleActionEvtLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRuleActionEvtLevel.setStatus("current")
_HpnicfWIPSSigRuleQuietTime_Type = Unsigned32
_HpnicfWIPSSigRuleQuietTime_Object = MibTableColumn
hpnicfWIPSSigRuleQuietTime = _HpnicfWIPSSigRuleQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 10),
    _HpnicfWIPSSigRuleQuietTime_Type()
)
hpnicfWIPSSigRuleQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigRuleQuietTime.setStatus("current")


class _HpnicfWIPSSigSubRuleFrameType_Type(Integer32):
    """Custom type hpnicfWIPSSigSubRuleFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("control", 1),
          ("data", 2),
          ("manage", 0),
          ("undo", 3))
    )


_HpnicfWIPSSigSubRuleFrameType_Type.__name__ = "Integer32"
_HpnicfWIPSSigSubRuleFrameType_Object = MibTableColumn
hpnicfWIPSSigSubRuleFrameType = _HpnicfWIPSSigSubRuleFrameType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 11),
    _HpnicfWIPSSigSubRuleFrameType_Type()
)
hpnicfWIPSSigSubRuleFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleFrameType.setStatus("current")


class _HpnicfWIPSSigSubRuleFrameSubType_Type(Integer32):
    """Custom type hpnicfWIPSSigSubRuleFrameSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("assocReq", 1),
          ("assocRes", 2),
          ("auth", 6),
          ("beacon", 4),
          ("deauth", 7),
          ("disasso", 5),
          ("none", 0),
          ("probeReq", 3))
    )


_HpnicfWIPSSigSubRuleFrameSubType_Type.__name__ = "Integer32"
_HpnicfWIPSSigSubRuleFrameSubType_Object = MibTableColumn
hpnicfWIPSSigSubRuleFrameSubType = _HpnicfWIPSSigSubRuleFrameSubType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 12),
    _HpnicfWIPSSigSubRuleFrameSubType_Type()
)
hpnicfWIPSSigSubRuleFrameSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleFrameSubType.setStatus("current")


class _HpnicfWIPSSigSubRuleMac_Type(OctetString):
    """Custom type hpnicfWIPSSigSubRuleMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_HpnicfWIPSSigSubRuleMac_Type.__name__ = "OctetString"
_HpnicfWIPSSigSubRuleMac_Object = MibTableColumn
hpnicfWIPSSigSubRuleMac = _HpnicfWIPSSigSubRuleMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 13),
    _HpnicfWIPSSigSubRuleMac_Type()
)
hpnicfWIPSSigSubRuleMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleMac.setStatus("current")


class _HpnicfWIPSSigSubRuleMacType_Type(Integer32):
    """Custom type hpnicfWIPSSigSubRuleMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bssid", 2),
          ("dest", 1),
          ("source", 0))
    )


_HpnicfWIPSSigSubRuleMacType_Type.__name__ = "Integer32"
_HpnicfWIPSSigSubRuleMacType_Object = MibTableColumn
hpnicfWIPSSigSubRuleMacType = _HpnicfWIPSSigSubRuleMacType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 14),
    _HpnicfWIPSSigSubRuleMacType_Type()
)
hpnicfWIPSSigSubRuleMacType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleMacType.setStatus("current")
_HpnicfWIPSSigSubRuleSeqNumMin_Type = Unsigned32
_HpnicfWIPSSigSubRuleSeqNumMin_Object = MibTableColumn
hpnicfWIPSSigSubRuleSeqNumMin = _HpnicfWIPSSigSubRuleSeqNumMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 15),
    _HpnicfWIPSSigSubRuleSeqNumMin_Type()
)
hpnicfWIPSSigSubRuleSeqNumMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleSeqNumMin.setStatus("current")
_HpnicfWIPSSigSubRuleSeqNumMax_Type = Unsigned32
_HpnicfWIPSSigSubRuleSeqNumMax_Object = MibTableColumn
hpnicfWIPSSigSubRuleSeqNumMax = _HpnicfWIPSSigSubRuleSeqNumMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 16),
    _HpnicfWIPSSigSubRuleSeqNumMax_Type()
)
hpnicfWIPSSigSubRuleSeqNumMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleSeqNumMax.setStatus("current")
_HpnicfWIPSSigSubRuleSSIDLenMin_Type = Unsigned32
_HpnicfWIPSSigSubRuleSSIDLenMin_Object = MibTableColumn
hpnicfWIPSSigSubRuleSSIDLenMin = _HpnicfWIPSSigSubRuleSSIDLenMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 17),
    _HpnicfWIPSSigSubRuleSSIDLenMin_Type()
)
hpnicfWIPSSigSubRuleSSIDLenMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleSSIDLenMin.setStatus("current")
_HpnicfWIPSSigSubRuleSSIDLenMax_Type = Unsigned32
_HpnicfWIPSSigSubRuleSSIDLenMax_Object = MibTableColumn
hpnicfWIPSSigSubRuleSSIDLenMax = _HpnicfWIPSSigSubRuleSSIDLenMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 18),
    _HpnicfWIPSSigSubRuleSSIDLenMax_Type()
)
hpnicfWIPSSigSubRuleSSIDLenMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleSSIDLenMax.setStatus("current")


class _HpnicfWIPSSigSubRuleSSID_Type(OctetString):
    """Custom type hpnicfWIPSSigSubRuleSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfWIPSSigSubRuleSSID_Type.__name__ = "OctetString"
_HpnicfWIPSSigSubRuleSSID_Object = MibTableColumn
hpnicfWIPSSigSubRuleSSID = _HpnicfWIPSSigSubRuleSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 19),
    _HpnicfWIPSSigSubRuleSSID_Type()
)
hpnicfWIPSSigSubRuleSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleSSID.setStatus("current")


class _HpnicfWIPSSigSubRuleSSIDOpe_Type(Integer32):
    """Custom type hpnicfWIPSSigSubRuleSSIDOpe based on Integer32"""
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
        *(("equal", 3),
          ("include", 1),
          ("notequal", 4),
          ("notinclude", 2))
    )


_HpnicfWIPSSigSubRuleSSIDOpe_Type.__name__ = "Integer32"
_HpnicfWIPSSigSubRuleSSIDOpe_Object = MibTableColumn
hpnicfWIPSSigSubRuleSSIDOpe = _HpnicfWIPSSigSubRuleSSIDOpe_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 20),
    _HpnicfWIPSSigSubRuleSSIDOpe_Type()
)
hpnicfWIPSSigSubRuleSSIDOpe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleSSIDOpe.setStatus("current")


class _HpnicfWIPSSigSubRuleSSIDCase_Type(TruthValue):
    """Custom type hpnicfWIPSSigSubRuleSSIDCase based on TruthValue"""


_HpnicfWIPSSigSubRuleSSIDCase_Object = MibTableColumn
hpnicfWIPSSigSubRuleSSIDCase = _HpnicfWIPSSigSubRuleSSIDCase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 3, 1, 21),
    _HpnicfWIPSSigSubRuleSSIDCase_Type()
)
hpnicfWIPSSigSubRuleSSIDCase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleSSIDCase.setStatus("current")
_HpnicfWIPSSigSubRulePatternTable_Object = MibTable
hpnicfWIPSSigSubRulePatternTable = _HpnicfWIPSSigSubRulePatternTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 4)
)
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRulePatternTable.setStatus("current")
_HpnicfWIPSSigSubRulePatternEntry_Object = MibTableRow
hpnicfWIPSSigSubRulePatternEntry = _HpnicfWIPSSigSubRulePatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 4, 1)
)
hpnicfWIPSSigSubRulePatternEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSSigRuleName"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSSigSubRulePatternID"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRulePatternEntry.setStatus("current")


class _HpnicfWIPSSigSubRulePatternID_Type(Unsigned32):
    """Custom type hpnicfWIPSSigSubRulePatternID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 27),
    )


_HpnicfWIPSSigSubRulePatternID_Type.__name__ = "Unsigned32"
_HpnicfWIPSSigSubRulePatternID_Object = MibTableColumn
hpnicfWIPSSigSubRulePatternID = _HpnicfWIPSSigSubRulePatternID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 4, 1, 1),
    _HpnicfWIPSSigSubRulePatternID_Type()
)
hpnicfWIPSSigSubRulePatternID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRulePatternID.setStatus("current")
_HpnicfWIPSSigSubRuleRowStatus_Type = RowStatus
_HpnicfWIPSSigSubRuleRowStatus_Object = MibTableColumn
hpnicfWIPSSigSubRuleRowStatus = _HpnicfWIPSSigSubRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 4, 1, 2),
    _HpnicfWIPSSigSubRuleRowStatus_Type()
)
hpnicfWIPSSigSubRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRuleRowStatus.setStatus("current")


class _HpnicfWIPSSigSubRulePatternName_Type(OctetString):
    """Custom type hpnicfWIPSSigSubRulePatternName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfWIPSSigSubRulePatternName_Type.__name__ = "OctetString"
_HpnicfWIPSSigSubRulePatternName_Object = MibTableColumn
hpnicfWIPSSigSubRulePatternName = _HpnicfWIPSSigSubRulePatternName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 4, 1, 3),
    _HpnicfWIPSSigSubRulePatternName_Type()
)
hpnicfWIPSSigSubRulePatternName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRulePatternName.setStatus("current")


class _HpnicfWIPSSigSubRulePatternOffset_Type(Integer32):
    """Custom type hpnicfWIPSSigSubRulePatternOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2346),
    )


_HpnicfWIPSSigSubRulePatternOffset_Type.__name__ = "Integer32"
_HpnicfWIPSSigSubRulePatternOffset_Object = MibTableColumn
hpnicfWIPSSigSubRulePatternOffset = _HpnicfWIPSSigSubRulePatternOffset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 4, 1, 4),
    _HpnicfWIPSSigSubRulePatternOffset_Type()
)
hpnicfWIPSSigSubRulePatternOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRulePatternOffset.setStatus("current")


class _HpnicfWIPSSigSubRulePatternMask_Type(Integer32):
    """Custom type hpnicfWIPSSigSubRulePatternMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfWIPSSigSubRulePatternMask_Type.__name__ = "Integer32"
_HpnicfWIPSSigSubRulePatternMask_Object = MibTableColumn
hpnicfWIPSSigSubRulePatternMask = _HpnicfWIPSSigSubRulePatternMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 4, 1, 5),
    _HpnicfWIPSSigSubRulePatternMask_Type()
)
hpnicfWIPSSigSubRulePatternMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRulePatternMask.setStatus("current")


class _HpnicfWIPSSigSubRulePatternValueMin_Type(Unsigned32):
    """Custom type hpnicfWIPSSigSubRulePatternValueMin based on Unsigned32"""
    defaultHexValue = 4294967295


_HpnicfWIPSSigSubRulePatternValueMin_Object = MibTableColumn
hpnicfWIPSSigSubRulePatternValueMin = _HpnicfWIPSSigSubRulePatternValueMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 4, 1, 6),
    _HpnicfWIPSSigSubRulePatternValueMin_Type()
)
hpnicfWIPSSigSubRulePatternValueMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRulePatternValueMin.setStatus("current")


class _HpnicfWIPSSigSubRulePatternValueMax_Type(Unsigned32):
    """Custom type hpnicfWIPSSigSubRulePatternValueMax based on Unsigned32"""
    defaultHexValue = 4294967295


_HpnicfWIPSSigSubRulePatternValueMax_Object = MibTableColumn
hpnicfWIPSSigSubRulePatternValueMax = _HpnicfWIPSSigSubRulePatternValueMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 4, 1, 7),
    _HpnicfWIPSSigSubRulePatternValueMax_Type()
)
hpnicfWIPSSigSubRulePatternValueMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRulePatternValueMax.setStatus("current")


class _HpnicfWIPSSigSubRulePatternFromPayload_Type(TruthValue):
    """Custom type hpnicfWIPSSigSubRulePatternFromPayload based on TruthValue"""


_HpnicfWIPSSigSubRulePatternFromPayload_Object = MibTableColumn
hpnicfWIPSSigSubRulePatternFromPayload = _HpnicfWIPSSigSubRulePatternFromPayload_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 10, 4, 1, 8),
    _HpnicfWIPSSigSubRulePatternFromPayload_Type()
)
hpnicfWIPSSigSubRulePatternFromPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSSigSubRulePatternFromPayload.setStatus("current")
_HpnicfWIPSCtmConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfWIPSCtmConfigGroup = _HpnicfWIPSCtmConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11)
)


class _HpnicfWIPSCtmPolicyCfgSupportSet_Type(OctetString):
    """Custom type hpnicfWIPSCtmPolicyCfgSupportSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HpnicfWIPSCtmPolicyCfgSupportSet_Type.__name__ = "OctetString"
_HpnicfWIPSCtmPolicyCfgSupportSet_Object = MibScalar
hpnicfWIPSCtmPolicyCfgSupportSet = _HpnicfWIPSCtmPolicyCfgSupportSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 1),
    _HpnicfWIPSCtmPolicyCfgSupportSet_Type()
)
hpnicfWIPSCtmPolicyCfgSupportSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyCfgSupportSet.setStatus("current")
_HpnicfWIPSCtmPolicyTable_Object = MibTable
hpnicfWIPSCtmPolicyTable = _HpnicfWIPSCtmPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2)
)
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyTable.setStatus("current")
_HpnicfWIPSCtmPolicyEntry_Object = MibTableRow
hpnicfWIPSCtmPolicyEntry = _HpnicfWIPSCtmPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1)
)
hpnicfWIPSCtmPolicyEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSCtmPolicyName"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyEntry.setStatus("current")


class _HpnicfWIPSCtmPolicyName_Type(OctetString):
    """Custom type hpnicfWIPSCtmPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSCtmPolicyName_Type.__name__ = "OctetString"
_HpnicfWIPSCtmPolicyName_Object = MibTableColumn
hpnicfWIPSCtmPolicyName = _HpnicfWIPSCtmPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 1),
    _HpnicfWIPSCtmPolicyName_Type()
)
hpnicfWIPSCtmPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyName.setStatus("current")
_HpnicfWIPSCtmPolicyCfgRowStatus_Type = RowStatus
_HpnicfWIPSCtmPolicyCfgRowStatus_Object = MibTableColumn
hpnicfWIPSCtmPolicyCfgRowStatus = _HpnicfWIPSCtmPolicyCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 2),
    _HpnicfWIPSCtmPolicyCfgRowStatus_Type()
)
hpnicfWIPSCtmPolicyCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyCfgRowStatus.setStatus("current")


class _HpnicfWIPSCtmPolicyBitString_Type(OctetString):
    """Custom type hpnicfWIPSCtmPolicyBitString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HpnicfWIPSCtmPolicyBitString_Type.__name__ = "OctetString"
_HpnicfWIPSCtmPolicyBitString_Object = MibTableColumn
hpnicfWIPSCtmPolicyBitString = _HpnicfWIPSCtmPolicyBitString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 3),
    _HpnicfWIPSCtmPolicyBitString_Type()
)
hpnicfWIPSCtmPolicyBitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyBitString.setStatus("current")


class _HpnicfWIPSCtmPolicyFixedChl_Type(TruthValue):
    """Custom type hpnicfWIPSCtmPolicyFixedChl based on TruthValue"""


_HpnicfWIPSCtmPolicyFixedChl_Object = MibTableColumn
hpnicfWIPSCtmPolicyFixedChl = _HpnicfWIPSCtmPolicyFixedChl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 4),
    _HpnicfWIPSCtmPolicyFixedChl_Type()
)
hpnicfWIPSCtmPolicyFixedChl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyFixedChl.setStatus("current")


class _HpnicfWIPSCtmPolicyRogueAPPre_Type(Unsigned32):
    """Custom type hpnicfWIPSCtmPolicyRogueAPPre based on Unsigned32"""
    defaultValue = 9


_HpnicfWIPSCtmPolicyRogueAPPre_Object = MibTableColumn
hpnicfWIPSCtmPolicyRogueAPPre = _HpnicfWIPSCtmPolicyRogueAPPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 5),
    _HpnicfWIPSCtmPolicyRogueAPPre_Type()
)
hpnicfWIPSCtmPolicyRogueAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyRogueAPPre.setStatus("current")


class _HpnicfWIPSCtmPolicyPtRogueAPPre_Type(Unsigned32):
    """Custom type hpnicfWIPSCtmPolicyPtRogueAPPre based on Unsigned32"""
    defaultValue = 7


_HpnicfWIPSCtmPolicyPtRogueAPPre_Object = MibTableColumn
hpnicfWIPSCtmPolicyPtRogueAPPre = _HpnicfWIPSCtmPolicyPtRogueAPPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 6),
    _HpnicfWIPSCtmPolicyPtRogueAPPre_Type()
)
hpnicfWIPSCtmPolicyPtRogueAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyPtRogueAPPre.setStatus("current")


class _HpnicfWIPSCtmPolicyMisconfAPPre_Type(Unsigned32):
    """Custom type hpnicfWIPSCtmPolicyMisconfAPPre based on Unsigned32"""
    defaultValue = 3


_HpnicfWIPSCtmPolicyMisconfAPPre_Object = MibTableColumn
hpnicfWIPSCtmPolicyMisconfAPPre = _HpnicfWIPSCtmPolicyMisconfAPPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 7),
    _HpnicfWIPSCtmPolicyMisconfAPPre_Type()
)
hpnicfWIPSCtmPolicyMisconfAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyMisconfAPPre.setStatus("current")


class _HpnicfWIPSCtmPolicyExternalAPPre_Type(Unsigned32):
    """Custom type hpnicfWIPSCtmPolicyExternalAPPre based on Unsigned32"""
    defaultValue = 1


_HpnicfWIPSCtmPolicyExternalAPPre_Object = MibTableColumn
hpnicfWIPSCtmPolicyExternalAPPre = _HpnicfWIPSCtmPolicyExternalAPPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 8),
    _HpnicfWIPSCtmPolicyExternalAPPre_Type()
)
hpnicfWIPSCtmPolicyExternalAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyExternalAPPre.setStatus("current")


class _HpnicfWIPSCtmPolicyPtExternalAPPre_Type(Unsigned32):
    """Custom type hpnicfWIPSCtmPolicyPtExternalAPPre based on Unsigned32"""
    defaultValue = 2


_HpnicfWIPSCtmPolicyPtExternalAPPre_Object = MibTableColumn
hpnicfWIPSCtmPolicyPtExternalAPPre = _HpnicfWIPSCtmPolicyPtExternalAPPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 9),
    _HpnicfWIPSCtmPolicyPtExternalAPPre_Type()
)
hpnicfWIPSCtmPolicyPtExternalAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyPtExternalAPPre.setStatus("current")


class _HpnicfWIPSCtmPolicyUncateAPPre_Type(Unsigned32):
    """Custom type hpnicfWIPSCtmPolicyUncateAPPre based on Unsigned32"""
    defaultValue = 5


_HpnicfWIPSCtmPolicyUncateAPPre_Object = MibTableColumn
hpnicfWIPSCtmPolicyUncateAPPre = _HpnicfWIPSCtmPolicyUncateAPPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 10),
    _HpnicfWIPSCtmPolicyUncateAPPre_Type()
)
hpnicfWIPSCtmPolicyUncateAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyUncateAPPre.setStatus("current")


class _HpnicfWIPSCtmPolicyPtAuthAPPre_Type(Unsigned32):
    """Custom type hpnicfWIPSCtmPolicyPtAuthAPPre based on Unsigned32"""
    defaultValue = 0


_HpnicfWIPSCtmPolicyPtAuthAPPre_Object = MibTableColumn
hpnicfWIPSCtmPolicyPtAuthAPPre = _HpnicfWIPSCtmPolicyPtAuthAPPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 11),
    _HpnicfWIPSCtmPolicyPtAuthAPPre_Type()
)
hpnicfWIPSCtmPolicyPtAuthAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyPtAuthAPPre.setStatus("current")


class _HpnicfWIPSCtmPolicyMisassoStaPre_Type(Unsigned32):
    """Custom type hpnicfWIPSCtmPolicyMisassoStaPre based on Unsigned32"""
    defaultValue = 6


_HpnicfWIPSCtmPolicyMisassoStaPre_Object = MibTableColumn
hpnicfWIPSCtmPolicyMisassoStaPre = _HpnicfWIPSCtmPolicyMisassoStaPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 12),
    _HpnicfWIPSCtmPolicyMisassoStaPre_Type()
)
hpnicfWIPSCtmPolicyMisassoStaPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyMisassoStaPre.setStatus("current")


class _HpnicfWIPSCtmPolicyUncateStaPre_Type(Unsigned32):
    """Custom type hpnicfWIPSCtmPolicyUncateStaPre based on Unsigned32"""
    defaultValue = 4


_HpnicfWIPSCtmPolicyUncateStaPre_Object = MibTableColumn
hpnicfWIPSCtmPolicyUncateStaPre = _HpnicfWIPSCtmPolicyUncateStaPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 13),
    _HpnicfWIPSCtmPolicyUncateStaPre_Type()
)
hpnicfWIPSCtmPolicyUncateStaPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyUncateStaPre.setStatus("current")


class _HpnicfWIPSCtmPolicyUnauthStaPre_Type(Unsigned32):
    """Custom type hpnicfWIPSCtmPolicyUnauthStaPre based on Unsigned32"""
    defaultValue = 8


_HpnicfWIPSCtmPolicyUnauthStaPre_Object = MibTableColumn
hpnicfWIPSCtmPolicyUnauthStaPre = _HpnicfWIPSCtmPolicyUnauthStaPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 2, 1, 14),
    _HpnicfWIPSCtmPolicyUnauthStaPre_Type()
)
hpnicfWIPSCtmPolicyUnauthStaPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyUnauthStaPre.setStatus("current")
_HpnicfWIPSCtmPolicyDevListTable_Object = MibTable
hpnicfWIPSCtmPolicyDevListTable = _HpnicfWIPSCtmPolicyDevListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 3)
)
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyDevListTable.setStatus("current")
_HpnicfWIPSCtmPolicyDevListEntry_Object = MibTableRow
hpnicfWIPSCtmPolicyDevListEntry = _HpnicfWIPSCtmPolicyDevListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 3, 1)
)
hpnicfWIPSCtmPolicyDevListEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSCtmPolicyName"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSCtmPolicyDevMAC"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyDevListEntry.setStatus("current")
_HpnicfWIPSCtmPolicyDevMAC_Type = MacAddress
_HpnicfWIPSCtmPolicyDevMAC_Object = MibTableColumn
hpnicfWIPSCtmPolicyDevMAC = _HpnicfWIPSCtmPolicyDevMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 3, 1, 1),
    _HpnicfWIPSCtmPolicyDevMAC_Type()
)
hpnicfWIPSCtmPolicyDevMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyDevMAC.setStatus("current")
_HpnicfWIPSCtmPolicyDevRowStatus_Type = RowStatus
_HpnicfWIPSCtmPolicyDevRowStatus_Object = MibTableColumn
hpnicfWIPSCtmPolicyDevRowStatus = _HpnicfWIPSCtmPolicyDevRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 11, 3, 1, 2),
    _HpnicfWIPSCtmPolicyDevRowStatus_Type()
)
hpnicfWIPSCtmPolicyDevRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmPolicyDevRowStatus.setStatus("current")
_HpnicfWIPSMalPktDctConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfWIPSMalPktDctConfigGroup = _HpnicfWIPSMalPktDctConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 12)
)


class _HpnicfWIPSMalPktDctCfgLogSupportSet_Type(OctetString):
    """Custom type hpnicfWIPSMalPktDctCfgLogSupportSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HpnicfWIPSMalPktDctCfgLogSupportSet_Type.__name__ = "OctetString"
_HpnicfWIPSMalPktDctCfgLogSupportSet_Object = MibScalar
hpnicfWIPSMalPktDctCfgLogSupportSet = _HpnicfWIPSMalPktDctCfgLogSupportSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 12, 1),
    _HpnicfWIPSMalPktDctCfgLogSupportSet_Type()
)
hpnicfWIPSMalPktDctCfgLogSupportSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktDctCfgLogSupportSet.setStatus("current")


class _HpnicfWIPSMalPktDctCfgTrapSupportSet_Type(OctetString):
    """Custom type hpnicfWIPSMalPktDctCfgTrapSupportSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HpnicfWIPSMalPktDctCfgTrapSupportSet_Type.__name__ = "OctetString"
_HpnicfWIPSMalPktDctCfgTrapSupportSet_Object = MibScalar
hpnicfWIPSMalPktDctCfgTrapSupportSet = _HpnicfWIPSMalPktDctCfgTrapSupportSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 12, 2),
    _HpnicfWIPSMalPktDctCfgTrapSupportSet_Type()
)
hpnicfWIPSMalPktDctCfgTrapSupportSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktDctCfgTrapSupportSet.setStatus("current")
_HpnicfWIPSMalPktDctPolicyTable_Object = MibTable
hpnicfWIPSMalPktDctPolicyTable = _HpnicfWIPSMalPktDctPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 12, 3)
)
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktDctPolicyTable.setStatus("current")
_HpnicfWIPSMalPktDctPolicyEntry_Object = MibTableRow
hpnicfWIPSMalPktDctPolicyEntry = _HpnicfWIPSMalPktDctPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 12, 3, 1)
)
hpnicfWIPSMalPktDctPolicyEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSMalPktDctPolicyName"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktDctPolicyEntry.setStatus("current")


class _HpnicfWIPSMalPktDctPolicyName_Type(OctetString):
    """Custom type hpnicfWIPSMalPktDctPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSMalPktDctPolicyName_Type.__name__ = "OctetString"
_HpnicfWIPSMalPktDctPolicyName_Object = MibTableColumn
hpnicfWIPSMalPktDctPolicyName = _HpnicfWIPSMalPktDctPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 12, 3, 1, 1),
    _HpnicfWIPSMalPktDctPolicyName_Type()
)
hpnicfWIPSMalPktDctPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktDctPolicyName.setStatus("current")
_HpnicfWIPSMalPktDctPolicyCfgRowStatus_Type = RowStatus
_HpnicfWIPSMalPktDctPolicyCfgRowStatus_Object = MibTableColumn
hpnicfWIPSMalPktDctPolicyCfgRowStatus = _HpnicfWIPSMalPktDctPolicyCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 12, 3, 1, 2),
    _HpnicfWIPSMalPktDctPolicyCfgRowStatus_Type()
)
hpnicfWIPSMalPktDctPolicyCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktDctPolicyCfgRowStatus.setStatus("current")


class _HpnicfWIPSMalPktDctPolicyLogBitString_Type(OctetString):
    """Custom type hpnicfWIPSMalPktDctPolicyLogBitString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HpnicfWIPSMalPktDctPolicyLogBitString_Type.__name__ = "OctetString"
_HpnicfWIPSMalPktDctPolicyLogBitString_Object = MibTableColumn
hpnicfWIPSMalPktDctPolicyLogBitString = _HpnicfWIPSMalPktDctPolicyLogBitString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 12, 3, 1, 3),
    _HpnicfWIPSMalPktDctPolicyLogBitString_Type()
)
hpnicfWIPSMalPktDctPolicyLogBitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktDctPolicyLogBitString.setStatus("current")


class _HpnicfWIPSMalPktDctPolicyTrapBitString_Type(OctetString):
    """Custom type hpnicfWIPSMalPktDctPolicyTrapBitString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HpnicfWIPSMalPktDctPolicyTrapBitString_Type.__name__ = "OctetString"
_HpnicfWIPSMalPktDctPolicyTrapBitString_Object = MibTableColumn
hpnicfWIPSMalPktDctPolicyTrapBitString = _HpnicfWIPSMalPktDctPolicyTrapBitString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 12, 3, 1, 4),
    _HpnicfWIPSMalPktDctPolicyTrapBitString_Type()
)
hpnicfWIPSMalPktDctPolicyTrapBitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktDctPolicyTrapBitString.setStatus("current")


class _HpnicfWIPSMalPktDctPolicyDurationThreshold_Type(Integer32):
    """Custom type hpnicfWIPSMalPktDctPolicyDurationThreshold based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_HpnicfWIPSMalPktDctPolicyDurationThreshold_Type.__name__ = "Integer32"
_HpnicfWIPSMalPktDctPolicyDurationThreshold_Object = MibTableColumn
hpnicfWIPSMalPktDctPolicyDurationThreshold = _HpnicfWIPSMalPktDctPolicyDurationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 12, 3, 1, 5),
    _HpnicfWIPSMalPktDctPolicyDurationThreshold_Type()
)
hpnicfWIPSMalPktDctPolicyDurationThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktDctPolicyDurationThreshold.setStatus("current")


class _HpnicfWIPSMalPktDctPolicyQuietTime_Type(Integer32):
    """Custom type hpnicfWIPSMalPktDctPolicyQuietTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_HpnicfWIPSMalPktDctPolicyQuietTime_Type.__name__ = "Integer32"
_HpnicfWIPSMalPktDctPolicyQuietTime_Object = MibTableColumn
hpnicfWIPSMalPktDctPolicyQuietTime = _HpnicfWIPSMalPktDctPolicyQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 12, 3, 1, 6),
    _HpnicfWIPSMalPktDctPolicyQuietTime_Type()
)
hpnicfWIPSMalPktDctPolicyQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktDctPolicyQuietTime.setStatus("current")
_HpnicfWIPSStaticTrustOUIListCfgTable_Object = MibTable
hpnicfWIPSStaticTrustOUIListCfgTable = _HpnicfWIPSStaticTrustOUIListCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 13)
)
if mibBuilder.loadTexts:
    hpnicfWIPSStaticTrustOUIListCfgTable.setStatus("current")
_HpnicfWIPSStaticTrustOUIListCfgEntry_Object = MibTableRow
hpnicfWIPSStaticTrustOUIListCfgEntry = _HpnicfWIPSStaticTrustOUIListCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 13, 1)
)
hpnicfWIPSStaticTrustOUIListCfgEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSStaticTrustOUIListOUI"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSStaticTrustOUIListCfgEntry.setStatus("current")


class _HpnicfWIPSStaticTrustOUIListOUI_Type(OctetString):
    """Custom type hpnicfWIPSStaticTrustOUIListOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpnicfWIPSStaticTrustOUIListOUI_Type.__name__ = "OctetString"
_HpnicfWIPSStaticTrustOUIListOUI_Object = MibTableColumn
hpnicfWIPSStaticTrustOUIListOUI = _HpnicfWIPSStaticTrustOUIListOUI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 13, 1, 1),
    _HpnicfWIPSStaticTrustOUIListOUI_Type()
)
hpnicfWIPSStaticTrustOUIListOUI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSStaticTrustOUIListOUI.setStatus("current")
_HpnicfWIPSStaticTrustOUIListRowStatus_Type = RowStatus
_HpnicfWIPSStaticTrustOUIListRowStatus_Object = MibTableColumn
hpnicfWIPSStaticTrustOUIListRowStatus = _HpnicfWIPSStaticTrustOUIListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 13, 1, 2),
    _HpnicfWIPSStaticTrustOUIListRowStatus_Type()
)
hpnicfWIPSStaticTrustOUIListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSStaticTrustOUIListRowStatus.setStatus("current")
_HpnicfWIPSStaticTrustVendorListCfgTable_Object = MibTable
hpnicfWIPSStaticTrustVendorListCfgTable = _HpnicfWIPSStaticTrustVendorListCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 14)
)
if mibBuilder.loadTexts:
    hpnicfWIPSStaticTrustVendorListCfgTable.setStatus("current")
_HpnicfWIPSStaticTrustVendorListCfgEntry_Object = MibTableRow
hpnicfWIPSStaticTrustVendorListCfgEntry = _HpnicfWIPSStaticTrustVendorListCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 14, 1)
)
hpnicfWIPSStaticTrustVendorListCfgEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSStaticTrustVendorListVendor"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSStaticTrustVendorListCfgEntry.setStatus("current")


class _HpnicfWIPSStaticTrustVendorListVendor_Type(OctetString):
    """Custom type hpnicfWIPSStaticTrustVendorListVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfWIPSStaticTrustVendorListVendor_Type.__name__ = "OctetString"
_HpnicfWIPSStaticTrustVendorListVendor_Object = MibTableColumn
hpnicfWIPSStaticTrustVendorListVendor = _HpnicfWIPSStaticTrustVendorListVendor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 14, 1, 1),
    _HpnicfWIPSStaticTrustVendorListVendor_Type()
)
hpnicfWIPSStaticTrustVendorListVendor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSStaticTrustVendorListVendor.setStatus("current")
_HpnicfWIPSStaticTrustVendorListRowStatus_Type = RowStatus
_HpnicfWIPSStaticTrustVendorListRowStatus_Object = MibTableColumn
hpnicfWIPSStaticTrustVendorListRowStatus = _HpnicfWIPSStaticTrustVendorListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 1, 14, 1, 2),
    _HpnicfWIPSStaticTrustVendorListRowStatus_Type()
)
hpnicfWIPSStaticTrustVendorListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfWIPSStaticTrustVendorListRowStatus.setStatus("current")
_HpnicfWIPSDetectGroup_ObjectIdentity = ObjectIdentity
hpnicfWIPSDetectGroup = _HpnicfWIPSDetectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2)
)
_HpnicfWIPSDctAPTable_Object = MibTable
hpnicfWIPSDctAPTable = _HpnicfWIPSDctAPTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPTable.setStatus("current")
_HpnicfWIPSDctAPEntry_Object = MibTableRow
hpnicfWIPSDctAPEntry = _HpnicfWIPSDctAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1)
)
hpnicfWIPSDctAPEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctAPVSD"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctAPBSSID"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPEntry.setStatus("current")


class _HpnicfWIPSDctAPVSD_Type(OctetString):
    """Custom type hpnicfWIPSDctAPVSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSDctAPVSD_Type.__name__ = "OctetString"
_HpnicfWIPSDctAPVSD_Object = MibTableColumn
hpnicfWIPSDctAPVSD = _HpnicfWIPSDctAPVSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 1),
    _HpnicfWIPSDctAPVSD_Type()
)
hpnicfWIPSDctAPVSD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPVSD.setStatus("current")
_HpnicfWIPSDctAPBSSID_Type = MacAddress
_HpnicfWIPSDctAPBSSID_Object = MibTableColumn
hpnicfWIPSDctAPBSSID = _HpnicfWIPSDctAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 2),
    _HpnicfWIPSDctAPBSSID_Type()
)
hpnicfWIPSDctAPBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPBSSID.setStatus("current")
_HpnicfWIPSDctAPRunningTime_Type = TimeTicks
_HpnicfWIPSDctAPRunningTime_Object = MibTableColumn
hpnicfWIPSDctAPRunningTime = _HpnicfWIPSDctAPRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 3),
    _HpnicfWIPSDctAPRunningTime_Type()
)
hpnicfWIPSDctAPRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPRunningTime.setStatus("current")
_HpnicfWIPSDctAPRunTmLastUpdateTm_Type = TimeTicks
_HpnicfWIPSDctAPRunTmLastUpdateTm_Object = MibTableColumn
hpnicfWIPSDctAPRunTmLastUpdateTm = _HpnicfWIPSDctAPRunTmLastUpdateTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 4),
    _HpnicfWIPSDctAPRunTmLastUpdateTm_Type()
)
hpnicfWIPSDctAPRunTmLastUpdateTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPRunTmLastUpdateTm.setStatus("current")
_HpnicfWIPSDctAPIsCountered_Type = TruthValue
_HpnicfWIPSDctAPIsCountered_Object = MibTableColumn
hpnicfWIPSDctAPIsCountered = _HpnicfWIPSDctAPIsCountered_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 5),
    _HpnicfWIPSDctAPIsCountered_Type()
)
hpnicfWIPSDctAPIsCountered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPIsCountered.setStatus("current")
_HpnicfWIPSDctAPWorkChannel_Type = HpnicfWIPSChannel
_HpnicfWIPSDctAPWorkChannel_Object = MibTableColumn
hpnicfWIPSDctAPWorkChannel = _HpnicfWIPSDctAPWorkChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 6),
    _HpnicfWIPSDctAPWorkChannel_Type()
)
hpnicfWIPSDctAPWorkChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPWorkChannel.setStatus("current")
_HpnicfWIPSDctAPRadioType_Type = HpnicfWIPSRadioType
_HpnicfWIPSDctAPRadioType_Object = MibTableColumn
hpnicfWIPSDctAPRadioType = _HpnicfWIPSDctAPRadioType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 7),
    _HpnicfWIPSDctAPRadioType_Type()
)
hpnicfWIPSDctAPRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPRadioType.setStatus("current")
_HpnicfWIPSDctAPAuthMethod_Type = HpnicfWIPSAuthMethod
_HpnicfWIPSDctAPAuthMethod_Object = MibTableColumn
hpnicfWIPSDctAPAuthMethod = _HpnicfWIPSDctAPAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 8),
    _HpnicfWIPSDctAPAuthMethod_Type()
)
hpnicfWIPSDctAPAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPAuthMethod.setStatus("current")
_HpnicfWIPSDctAPEncryptMethod_Type = HpnicfWIPSEncryptMethod
_HpnicfWIPSDctAPEncryptMethod_Object = MibTableColumn
hpnicfWIPSDctAPEncryptMethod = _HpnicfWIPSDctAPEncryptMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 9),
    _HpnicfWIPSDctAPEncryptMethod_Type()
)
hpnicfWIPSDctAPEncryptMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPEncryptMethod.setStatus("current")
_HpnicfWIPSDctAPSecurity_Type = HpnicfWIPSAPSecurityType
_HpnicfWIPSDctAPSecurity_Object = MibTableColumn
hpnicfWIPSDctAPSecurity = _HpnicfWIPSDctAPSecurity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 10),
    _HpnicfWIPSDctAPSecurity_Type()
)
hpnicfWIPSDctAPSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPSecurity.setStatus("current")


class _HpnicfWIPSDctAPSeverityLevel_Type(Unsigned32):
    """Custom type hpnicfWIPSDctAPSeverityLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfWIPSDctAPSeverityLevel_Type.__name__ = "Unsigned32"
_HpnicfWIPSDctAPSeverityLevel_Object = MibTableColumn
hpnicfWIPSDctAPSeverityLevel = _HpnicfWIPSDctAPSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 11),
    _HpnicfWIPSDctAPSeverityLevel_Type()
)
hpnicfWIPSDctAPSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPSeverityLevel.setStatus("current")
_HpnicfWIPSDctAPLastDctTm_Type = TimeTicks
_HpnicfWIPSDctAPLastDctTm_Object = MibTableColumn
hpnicfWIPSDctAPLastDctTm = _HpnicfWIPSDctAPLastDctTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 12),
    _HpnicfWIPSDctAPLastDctTm_Type()
)
hpnicfWIPSDctAPLastDctTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPLastDctTm.setStatus("current")
_HpnicfWIPSDctAPFirstDctTm_Type = TimeTicks
_HpnicfWIPSDctAPFirstDctTm_Object = MibTableColumn
hpnicfWIPSDctAPFirstDctTm = _HpnicfWIPSDctAPFirstDctTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 13),
    _HpnicfWIPSDctAPFirstDctTm_Type()
)
hpnicfWIPSDctAPFirstDctTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPFirstDctTm.setStatus("current")


class _HpnicfWIPSDctAPAdd2BlackList_Type(TruthValue):
    """Custom type hpnicfWIPSDctAPAdd2BlackList based on TruthValue"""


_HpnicfWIPSDctAPAdd2BlackList_Object = MibTableColumn
hpnicfWIPSDctAPAdd2BlackList = _HpnicfWIPSDctAPAdd2BlackList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 14),
    _HpnicfWIPSDctAPAdd2BlackList_Type()
)
hpnicfWIPSDctAPAdd2BlackList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPAdd2BlackList.setStatus("current")


class _HpnicfWIPSDctAPAdd2WhiteList_Type(TruthValue):
    """Custom type hpnicfWIPSDctAPAdd2WhiteList based on TruthValue"""


_HpnicfWIPSDctAPAdd2WhiteList_Object = MibTableColumn
hpnicfWIPSDctAPAdd2WhiteList = _HpnicfWIPSDctAPAdd2WhiteList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 15),
    _HpnicfWIPSDctAPAdd2WhiteList_Type()
)
hpnicfWIPSDctAPAdd2WhiteList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPAdd2WhiteList.setStatus("current")


class _HpnicfWIPSDctAPAdd2IgnoreList_Type(TruthValue):
    """Custom type hpnicfWIPSDctAPAdd2IgnoreList based on TruthValue"""


_HpnicfWIPSDctAPAdd2IgnoreList_Object = MibTableColumn
hpnicfWIPSDctAPAdd2IgnoreList = _HpnicfWIPSDctAPAdd2IgnoreList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 16),
    _HpnicfWIPSDctAPAdd2IgnoreList_Type()
)
hpnicfWIPSDctAPAdd2IgnoreList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPAdd2IgnoreList.setStatus("current")


class _HpnicfWIPSDctAPAdd2CtmList_Type(TruthValue):
    """Custom type hpnicfWIPSDctAPAdd2CtmList based on TruthValue"""


_HpnicfWIPSDctAPAdd2CtmList_Object = MibTableColumn
hpnicfWIPSDctAPAdd2CtmList = _HpnicfWIPSDctAPAdd2CtmList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 17),
    _HpnicfWIPSDctAPAdd2CtmList_Type()
)
hpnicfWIPSDctAPAdd2CtmList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPAdd2CtmList.setStatus("current")
_HpnicfWIPSDctAPCategory_Type = HpnicfWIPSAPCategoryType
_HpnicfWIPSDctAPCategory_Object = MibTableColumn
hpnicfWIPSDctAPCategory = _HpnicfWIPSDctAPCategory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 18),
    _HpnicfWIPSDctAPCategory_Type()
)
hpnicfWIPSDctAPCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPCategory.setStatus("current")


class _HpnicfWIPSDctAPCategoryWay_Type(HpnicfWIPSDevCategoryWay):
    """Custom type hpnicfWIPSDctAPCategoryWay based on HpnicfWIPSDevCategoryWay"""


_HpnicfWIPSDctAPCategoryWay_Object = MibTableColumn
hpnicfWIPSDctAPCategoryWay = _HpnicfWIPSDctAPCategoryWay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 19),
    _HpnicfWIPSDctAPCategoryWay_Type()
)
hpnicfWIPSDctAPCategoryWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPCategoryWay.setStatus("current")
_HpnicfWIPSDctAPStatus_Type = HpnicfWIPSDevStatus
_HpnicfWIPSDctAPStatus_Object = MibTableColumn
hpnicfWIPSDctAPStatus = _HpnicfWIPSDctAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 20),
    _HpnicfWIPSDctAPStatus_Type()
)
hpnicfWIPSDctAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPStatus.setStatus("current")


class _HpnicfWIPSDctAPSSID_Type(OctetString):
    """Custom type hpnicfWIPSDctAPSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfWIPSDctAPSSID_Type.__name__ = "OctetString"
_HpnicfWIPSDctAPSSID_Object = MibTableColumn
hpnicfWIPSDctAPSSID = _HpnicfWIPSDctAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 21),
    _HpnicfWIPSDctAPSSID_Type()
)
hpnicfWIPSDctAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPSSID.setStatus("current")
_HpnicfWIPSDctAPAttachStaNum_Type = Integer32
_HpnicfWIPSDctAPAttachStaNum_Object = MibTableColumn
hpnicfWIPSDctAPAttachStaNum = _HpnicfWIPSDctAPAttachStaNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 22),
    _HpnicfWIPSDctAPAttachStaNum_Type()
)
hpnicfWIPSDctAPAttachStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPAttachStaNum.setStatus("current")
_HpnicfWIPSDctAPRptSensorNum_Type = Integer32
_HpnicfWIPSDctAPRptSensorNum_Object = MibTableColumn
hpnicfWIPSDctAPRptSensorNum = _HpnicfWIPSDctAPRptSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 23),
    _HpnicfWIPSDctAPRptSensorNum_Type()
)
hpnicfWIPSDctAPRptSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPRptSensorNum.setStatus("current")


class _HpnicfWIPSDctAPVendor_Type(OctetString):
    """Custom type hpnicfWIPSDctAPVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfWIPSDctAPVendor_Type.__name__ = "OctetString"
_HpnicfWIPSDctAPVendor_Object = MibTableColumn
hpnicfWIPSDctAPVendor = _HpnicfWIPSDctAPVendor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 1, 1, 24),
    _HpnicfWIPSDctAPVendor_Type()
)
hpnicfWIPSDctAPVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPVendor.setStatus("current")
_HpnicfWIPSDctAPAttachStaTable_Object = MibTable
hpnicfWIPSDctAPAttachStaTable = _HpnicfWIPSDctAPAttachStaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPAttachStaTable.setStatus("current")
_HpnicfWIPSDctAPAttachStaEntry_Object = MibTableRow
hpnicfWIPSDctAPAttachStaEntry = _HpnicfWIPSDctAPAttachStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 2, 1)
)
hpnicfWIPSDctAPAttachStaEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctAPVSD"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctAPBSSID"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctAPAttachStaMac"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPAttachStaEntry.setStatus("current")
_HpnicfWIPSDctAPAttachStaMac_Type = MacAddress
_HpnicfWIPSDctAPAttachStaMac_Object = MibTableColumn
hpnicfWIPSDctAPAttachStaMac = _HpnicfWIPSDctAPAttachStaMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 2, 1, 1),
    _HpnicfWIPSDctAPAttachStaMac_Type()
)
hpnicfWIPSDctAPAttachStaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPAttachStaMac.setStatus("current")
_HpnicfWIPSDctAPAttachStaRowStatus_Type = RowStatus
_HpnicfWIPSDctAPAttachStaRowStatus_Object = MibTableColumn
hpnicfWIPSDctAPAttachStaRowStatus = _HpnicfWIPSDctAPAttachStaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 2, 1, 2),
    _HpnicfWIPSDctAPAttachStaRowStatus_Type()
)
hpnicfWIPSDctAPAttachStaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPAttachStaRowStatus.setStatus("current")
_HpnicfWIPSDctAPRptSensorTable_Object = MibTable
hpnicfWIPSDctAPRptSensorTable = _HpnicfWIPSDctAPRptSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPRptSensorTable.setStatus("current")
_HpnicfWIPSDctAPRptSensorEntry_Object = MibTableRow
hpnicfWIPSDctAPRptSensorEntry = _HpnicfWIPSDctAPRptSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 3, 1)
)
hpnicfWIPSDctAPRptSensorEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctAPVSD"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctAPBSSID"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctAPRptSensorName"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPRptSensorEntry.setStatus("current")


class _HpnicfWIPSDctAPRptSensorName_Type(OctetString):
    """Custom type hpnicfWIPSDctAPRptSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfWIPSDctAPRptSensorName_Type.__name__ = "OctetString"
_HpnicfWIPSDctAPRptSensorName_Object = MibTableColumn
hpnicfWIPSDctAPRptSensorName = _HpnicfWIPSDctAPRptSensorName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 3, 1, 1),
    _HpnicfWIPSDctAPRptSensorName_Type()
)
hpnicfWIPSDctAPRptSensorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPRptSensorName.setStatus("current")


class _HpnicfWIPSDctAPRptSensorRadioId_Type(Integer32):
    """Custom type hpnicfWIPSDctAPRptSensorRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HpnicfWIPSDctAPRptSensorRadioId_Type.__name__ = "Integer32"
_HpnicfWIPSDctAPRptSensorRadioId_Object = MibTableColumn
hpnicfWIPSDctAPRptSensorRadioId = _HpnicfWIPSDctAPRptSensorRadioId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 3, 1, 2),
    _HpnicfWIPSDctAPRptSensorRadioId_Type()
)
hpnicfWIPSDctAPRptSensorRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPRptSensorRadioId.setStatus("current")


class _HpnicfWIPSDctAPRptRSSI_Type(Integer32):
    """Custom type hpnicfWIPSDctAPRptRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_HpnicfWIPSDctAPRptRSSI_Type.__name__ = "Integer32"
_HpnicfWIPSDctAPRptRSSI_Object = MibTableColumn
hpnicfWIPSDctAPRptRSSI = _HpnicfWIPSDctAPRptRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 3, 1, 3),
    _HpnicfWIPSDctAPRptRSSI_Type()
)
hpnicfWIPSDctAPRptRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPRptRSSI.setStatus("current")
_HpnicfWIPSDctAPLastRptTm_Type = TimeTicks
_HpnicfWIPSDctAPLastRptTm_Object = MibTableColumn
hpnicfWIPSDctAPLastRptTm = _HpnicfWIPSDctAPLastRptTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 3, 1, 4),
    _HpnicfWIPSDctAPLastRptTm_Type()
)
hpnicfWIPSDctAPLastRptTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctAPLastRptTm.setStatus("current")
_HpnicfWIPSDctStaTable_Object = MibTable
hpnicfWIPSDctStaTable = _HpnicfWIPSDctStaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaTable.setStatus("current")
_HpnicfWIPSDctStaEntry_Object = MibTableRow
hpnicfWIPSDctStaEntry = _HpnicfWIPSDctStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1)
)
hpnicfWIPSDctStaEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctStaVSD"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctStaMac"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaEntry.setStatus("current")


class _HpnicfWIPSDctStaVSD_Type(OctetString):
    """Custom type hpnicfWIPSDctStaVSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSDctStaVSD_Type.__name__ = "OctetString"
_HpnicfWIPSDctStaVSD_Object = MibTableColumn
hpnicfWIPSDctStaVSD = _HpnicfWIPSDctStaVSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 1),
    _HpnicfWIPSDctStaVSD_Type()
)
hpnicfWIPSDctStaVSD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaVSD.setStatus("current")
_HpnicfWIPSDctStaMac_Type = MacAddress
_HpnicfWIPSDctStaMac_Object = MibTableColumn
hpnicfWIPSDctStaMac = _HpnicfWIPSDctStaMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 2),
    _HpnicfWIPSDctStaMac_Type()
)
hpnicfWIPSDctStaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaMac.setStatus("current")
_HpnicfWIPSDctStaAssocBSSID_Type = MacAddress
_HpnicfWIPSDctStaAssocBSSID_Object = MibTableColumn
hpnicfWIPSDctStaAssocBSSID = _HpnicfWIPSDctStaAssocBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 3),
    _HpnicfWIPSDctStaAssocBSSID_Type()
)
hpnicfWIPSDctStaAssocBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaAssocBSSID.setStatus("current")
_HpnicfWIPSDctStaStatus_Type = HpnicfWIPSDevStatus
_HpnicfWIPSDctStaStatus_Object = MibTableColumn
hpnicfWIPSDctStaStatus = _HpnicfWIPSDctStaStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 4),
    _HpnicfWIPSDctStaStatus_Type()
)
hpnicfWIPSDctStaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaStatus.setStatus("current")
_HpnicfWIPSDctStaCategory_Type = HpnicfWIPSClientCategoryType
_HpnicfWIPSDctStaCategory_Object = MibTableColumn
hpnicfWIPSDctStaCategory = _HpnicfWIPSDctStaCategory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 5),
    _HpnicfWIPSDctStaCategory_Type()
)
hpnicfWIPSDctStaCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaCategory.setStatus("current")
_HpnicfWIPSDctStaRadioType_Type = HpnicfWIPSRadioType
_HpnicfWIPSDctStaRadioType_Object = MibTableColumn
hpnicfWIPSDctStaRadioType = _HpnicfWIPSDctStaRadioType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 6),
    _HpnicfWIPSDctStaRadioType_Type()
)
hpnicfWIPSDctStaRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaRadioType.setStatus("current")
_HpnicfWIPSDctStaWorkChannel_Type = HpnicfWIPSChannel
_HpnicfWIPSDctStaWorkChannel_Object = MibTableColumn
hpnicfWIPSDctStaWorkChannel = _HpnicfWIPSDctStaWorkChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 7),
    _HpnicfWIPSDctStaWorkChannel_Type()
)
hpnicfWIPSDctStaWorkChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaWorkChannel.setStatus("current")
_HpnicfWIPSDctStaIsCountered_Type = TruthValue
_HpnicfWIPSDctStaIsCountered_Object = MibTableColumn
hpnicfWIPSDctStaIsCountered = _HpnicfWIPSDctStaIsCountered_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 8),
    _HpnicfWIPSDctStaIsCountered_Type()
)
hpnicfWIPSDctStaIsCountered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaIsCountered.setStatus("current")


class _HpnicfWIPSDctStaAdd2BlackList_Type(TruthValue):
    """Custom type hpnicfWIPSDctStaAdd2BlackList based on TruthValue"""


_HpnicfWIPSDctStaAdd2BlackList_Object = MibTableColumn
hpnicfWIPSDctStaAdd2BlackList = _HpnicfWIPSDctStaAdd2BlackList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 9),
    _HpnicfWIPSDctStaAdd2BlackList_Type()
)
hpnicfWIPSDctStaAdd2BlackList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaAdd2BlackList.setStatus("current")


class _HpnicfWIPSDctStaAdd2WhiteList_Type(TruthValue):
    """Custom type hpnicfWIPSDctStaAdd2WhiteList based on TruthValue"""


_HpnicfWIPSDctStaAdd2WhiteList_Object = MibTableColumn
hpnicfWIPSDctStaAdd2WhiteList = _HpnicfWIPSDctStaAdd2WhiteList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 10),
    _HpnicfWIPSDctStaAdd2WhiteList_Type()
)
hpnicfWIPSDctStaAdd2WhiteList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaAdd2WhiteList.setStatus("current")


class _HpnicfWIPSDctStaAdd2IgnoreList_Type(TruthValue):
    """Custom type hpnicfWIPSDctStaAdd2IgnoreList based on TruthValue"""


_HpnicfWIPSDctStaAdd2IgnoreList_Object = MibTableColumn
hpnicfWIPSDctStaAdd2IgnoreList = _HpnicfWIPSDctStaAdd2IgnoreList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 11),
    _HpnicfWIPSDctStaAdd2IgnoreList_Type()
)
hpnicfWIPSDctStaAdd2IgnoreList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaAdd2IgnoreList.setStatus("current")


class _HpnicfWIPSDctStaAdd2CtmList_Type(TruthValue):
    """Custom type hpnicfWIPSDctStaAdd2CtmList based on TruthValue"""


_HpnicfWIPSDctStaAdd2CtmList_Object = MibTableColumn
hpnicfWIPSDctStaAdd2CtmList = _HpnicfWIPSDctStaAdd2CtmList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 12),
    _HpnicfWIPSDctStaAdd2CtmList_Type()
)
hpnicfWIPSDctStaAdd2CtmList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaAdd2CtmList.setStatus("current")
_HpnicfWIPSDctStaFirstDctTm_Type = TimeTicks
_HpnicfWIPSDctStaFirstDctTm_Object = MibTableColumn
hpnicfWIPSDctStaFirstDctTm = _HpnicfWIPSDctStaFirstDctTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 13),
    _HpnicfWIPSDctStaFirstDctTm_Type()
)
hpnicfWIPSDctStaFirstDctTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaFirstDctTm.setStatus("current")
_HpnicfWIPSDctStaLastDctTm_Type = TimeTicks
_HpnicfWIPSDctStaLastDctTm_Object = MibTableColumn
hpnicfWIPSDctStaLastDctTm = _HpnicfWIPSDctStaLastDctTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 14),
    _HpnicfWIPSDctStaLastDctTm_Type()
)
hpnicfWIPSDctStaLastDctTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaLastDctTm.setStatus("current")
_HpnicfWIPSDctStaRptSensorNum_Type = Integer32
_HpnicfWIPSDctStaRptSensorNum_Object = MibTableColumn
hpnicfWIPSDctStaRptSensorNum = _HpnicfWIPSDctStaRptSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 15),
    _HpnicfWIPSDctStaRptSensorNum_Type()
)
hpnicfWIPSDctStaRptSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaRptSensorNum.setStatus("current")


class _HpnicfWIPSDctStaState_Type(Integer32):
    """Custom type hpnicfWIPSDctStaState based on Integer32"""
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
        *(("association", 2),
          ("authentication", 1),
          ("deauthentication", 6),
          ("disassociation", 5),
          ("eapLogoff", 4),
          ("eapSuccess", 3))
    )


_HpnicfWIPSDctStaState_Type.__name__ = "Integer32"
_HpnicfWIPSDctStaState_Object = MibTableColumn
hpnicfWIPSDctStaState = _HpnicfWIPSDctStaState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 16),
    _HpnicfWIPSDctStaState_Type()
)
hpnicfWIPSDctStaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaState.setStatus("current")


class _HpnicfWIPSDctStaVendor_Type(OctetString):
    """Custom type hpnicfWIPSDctStaVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfWIPSDctStaVendor_Type.__name__ = "OctetString"
_HpnicfWIPSDctStaVendor_Object = MibTableColumn
hpnicfWIPSDctStaVendor = _HpnicfWIPSDctStaVendor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 4, 1, 17),
    _HpnicfWIPSDctStaVendor_Type()
)
hpnicfWIPSDctStaVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaVendor.setStatus("current")
_HpnicfWIPSDctStaRptSensorTable_Object = MibTable
hpnicfWIPSDctStaRptSensorTable = _HpnicfWIPSDctStaRptSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaRptSensorTable.setStatus("current")
_HpnicfWIPSDctStaRptSensorEntry_Object = MibTableRow
hpnicfWIPSDctStaRptSensorEntry = _HpnicfWIPSDctStaRptSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 5, 1)
)
hpnicfWIPSDctStaRptSensorEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctStaVSD"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctStaMac"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctStaRtpSensorName"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaRptSensorEntry.setStatus("current")


class _HpnicfWIPSDctStaRtpSensorName_Type(OctetString):
    """Custom type hpnicfWIPSDctStaRtpSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfWIPSDctStaRtpSensorName_Type.__name__ = "OctetString"
_HpnicfWIPSDctStaRtpSensorName_Object = MibTableColumn
hpnicfWIPSDctStaRtpSensorName = _HpnicfWIPSDctStaRtpSensorName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 5, 1, 1),
    _HpnicfWIPSDctStaRtpSensorName_Type()
)
hpnicfWIPSDctStaRtpSensorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaRtpSensorName.setStatus("current")


class _HpnicfWIPSDctStaRptSensorRadioId_Type(Integer32):
    """Custom type hpnicfWIPSDctStaRptSensorRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HpnicfWIPSDctStaRptSensorRadioId_Type.__name__ = "Integer32"
_HpnicfWIPSDctStaRptSensorRadioId_Object = MibTableColumn
hpnicfWIPSDctStaRptSensorRadioId = _HpnicfWIPSDctStaRptSensorRadioId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 5, 1, 2),
    _HpnicfWIPSDctStaRptSensorRadioId_Type()
)
hpnicfWIPSDctStaRptSensorRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaRptSensorRadioId.setStatus("current")
_HpnicfWIPSDctStaRptRSSI_Type = Integer32
_HpnicfWIPSDctStaRptRSSI_Object = MibTableColumn
hpnicfWIPSDctStaRptRSSI = _HpnicfWIPSDctStaRptRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 5, 1, 3),
    _HpnicfWIPSDctStaRptRSSI_Type()
)
hpnicfWIPSDctStaRptRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaRptRSSI.setStatus("current")
_HpnicfWIPSDctStaLastRptTm_Type = TimeTicks
_HpnicfWIPSDctStaLastRptTm_Object = MibTableColumn
hpnicfWIPSDctStaLastRptTm = _HpnicfWIPSDctStaLastRptTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 5, 1, 4),
    _HpnicfWIPSDctStaLastRptTm_Type()
)
hpnicfWIPSDctStaLastRptTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctStaLastRptTm.setStatus("current")
_HpnicfWIPSDctSSIDTable_Object = MibTable
hpnicfWIPSDctSSIDTable = _HpnicfWIPSDctSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctSSIDTable.setStatus("current")
_HpnicfWIPSDctSSIDEntry_Object = MibTableRow
hpnicfWIPSDctSSIDEntry = _HpnicfWIPSDctSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 6, 1)
)
hpnicfWIPSDctSSIDEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctNetworkVSD"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctNetworkSSID"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctNetworkCfg"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctSSIDEntry.setStatus("current")


class _HpnicfWIPSDctNetworkVSD_Type(OctetString):
    """Custom type hpnicfWIPSDctNetworkVSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSDctNetworkVSD_Type.__name__ = "OctetString"
_HpnicfWIPSDctNetworkVSD_Object = MibTableColumn
hpnicfWIPSDctNetworkVSD = _HpnicfWIPSDctNetworkVSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 6, 1, 1),
    _HpnicfWIPSDctNetworkVSD_Type()
)
hpnicfWIPSDctNetworkVSD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctNetworkVSD.setStatus("current")


class _HpnicfWIPSDctNetworkSSID_Type(OctetString):
    """Custom type hpnicfWIPSDctNetworkSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSDctNetworkSSID_Type.__name__ = "OctetString"
_HpnicfWIPSDctNetworkSSID_Object = MibTableColumn
hpnicfWIPSDctNetworkSSID = _HpnicfWIPSDctNetworkSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 6, 1, 2),
    _HpnicfWIPSDctNetworkSSID_Type()
)
hpnicfWIPSDctNetworkSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctNetworkSSID.setStatus("current")
_HpnicfWIPSDctNetworkCfg_Type = Unsigned32
_HpnicfWIPSDctNetworkCfg_Object = MibTableColumn
hpnicfWIPSDctNetworkCfg = _HpnicfWIPSDctNetworkCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 6, 1, 3),
    _HpnicfWIPSDctNetworkCfg_Type()
)
hpnicfWIPSDctNetworkCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctNetworkCfg.setStatus("current")
_HpnicfWIPSDctNetworkFirstRptTm_Type = TimeTicks
_HpnicfWIPSDctNetworkFirstRptTm_Object = MibTableColumn
hpnicfWIPSDctNetworkFirstRptTm = _HpnicfWIPSDctNetworkFirstRptTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 6, 1, 4),
    _HpnicfWIPSDctNetworkFirstRptTm_Type()
)
hpnicfWIPSDctNetworkFirstRptTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctNetworkFirstRptTm.setStatus("current")
_HpnicfWIPSDctNetworkLastRptTm_Type = TimeTicks
_HpnicfWIPSDctNetworkLastRptTm_Object = MibTableColumn
hpnicfWIPSDctNetworkLastRptTm = _HpnicfWIPSDctNetworkLastRptTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 6, 1, 5),
    _HpnicfWIPSDctNetworkLastRptTm_Type()
)
hpnicfWIPSDctNetworkLastRptTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctNetworkLastRptTm.setStatus("current")
_HpnicfWIPSDctNetworkStatus_Type = HpnicfWIPSDevStatus
_HpnicfWIPSDctNetworkStatus_Object = MibTableColumn
hpnicfWIPSDctNetworkStatus = _HpnicfWIPSDctNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 6, 1, 6),
    _HpnicfWIPSDctNetworkStatus_Type()
)
hpnicfWIPSDctNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctNetworkStatus.setStatus("current")


class _HpnicfWIPSDctNetworkSSIDHide_Type(TruthValue):
    """Custom type hpnicfWIPSDctNetworkSSIDHide based on TruthValue"""


_HpnicfWIPSDctNetworkSSIDHide_Object = MibTableColumn
hpnicfWIPSDctNetworkSSIDHide = _HpnicfWIPSDctNetworkSSIDHide_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 6, 1, 7),
    _HpnicfWIPSDctNetworkSSIDHide_Type()
)
hpnicfWIPSDctNetworkSSIDHide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctNetworkSSIDHide.setStatus("current")
_HpnicfWIPSDctNetworkBSSNum_Type = Integer32
_HpnicfWIPSDctNetworkBSSNum_Object = MibTableColumn
hpnicfWIPSDctNetworkBSSNum = _HpnicfWIPSDctNetworkBSSNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 6, 1, 8),
    _HpnicfWIPSDctNetworkBSSNum_Type()
)
hpnicfWIPSDctNetworkBSSNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctNetworkBSSNum.setStatus("current")
_HpnicfWIPSDctSSIDBSSTable_Object = MibTable
hpnicfWIPSDctSSIDBSSTable = _HpnicfWIPSDctSSIDBSSTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctSSIDBSSTable.setStatus("current")
_HpnicfWIPSDctSSIDBSSEntry_Object = MibTableRow
hpnicfWIPSDctSSIDBSSEntry = _HpnicfWIPSDctSSIDBSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 7, 1)
)
hpnicfWIPSDctSSIDBSSEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctNetworkVSD"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctNetworkSSID"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctNetworkCfg"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDctNetworkBSSID"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSDctSSIDBSSEntry.setStatus("current")
_HpnicfWIPSDctNetworkBSSID_Type = MacAddress
_HpnicfWIPSDctNetworkBSSID_Object = MibTableColumn
hpnicfWIPSDctNetworkBSSID = _HpnicfWIPSDctNetworkBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 7, 1, 1),
    _HpnicfWIPSDctNetworkBSSID_Type()
)
hpnicfWIPSDctNetworkBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDctNetworkBSSID.setStatus("current")
_HpnicfWIPSDctNetworkBSSWorkChl_Type = HpnicfWIPSChannel
_HpnicfWIPSDctNetworkBSSWorkChl_Object = MibTableColumn
hpnicfWIPSDctNetworkBSSWorkChl = _HpnicfWIPSDctNetworkBSSWorkChl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 7, 1, 2),
    _HpnicfWIPSDctNetworkBSSWorkChl_Type()
)
hpnicfWIPSDctNetworkBSSWorkChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctNetworkBSSWorkChl.setStatus("current")
_HpnicfWIPSDctNetworkBSSStaNum_Type = Integer32
_HpnicfWIPSDctNetworkBSSStaNum_Object = MibTableColumn
hpnicfWIPSDctNetworkBSSStaNum = _HpnicfWIPSDctNetworkBSSStaNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 7, 1, 3),
    _HpnicfWIPSDctNetworkBSSStaNum_Type()
)
hpnicfWIPSDctNetworkBSSStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDctNetworkBSSStaNum.setStatus("current")
_HpnicfWIPSBlockListTable_Object = MibTable
hpnicfWIPSBlockListTable = _HpnicfWIPSBlockListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfWIPSBlockListTable.setStatus("current")
_HpnicfWIPSBlockListEntry_Object = MibTableRow
hpnicfWIPSBlockListEntry = _HpnicfWIPSBlockListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 8, 1)
)
hpnicfWIPSBlockListEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSBlockListMacAddress"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSBlockListEntry.setStatus("current")
_HpnicfWIPSBlockListMacAddress_Type = MacAddress
_HpnicfWIPSBlockListMacAddress_Object = MibTableColumn
hpnicfWIPSBlockListMacAddress = _HpnicfWIPSBlockListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 8, 1, 1),
    _HpnicfWIPSBlockListMacAddress_Type()
)
hpnicfWIPSBlockListMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSBlockListMacAddress.setStatus("current")


class _HpnicfWIPSBlockListStatus_Type(Integer32):
    """Custom type hpnicfWIPSBlockListStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1),
          ("staticAndDynamic", 3))
    )


_HpnicfWIPSBlockListStatus_Type.__name__ = "Integer32"
_HpnicfWIPSBlockListStatus_Object = MibTableColumn
hpnicfWIPSBlockListStatus = _HpnicfWIPSBlockListStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 8, 1, 2),
    _HpnicfWIPSBlockListStatus_Type()
)
hpnicfWIPSBlockListStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSBlockListStatus.setStatus("current")
_HpnicfWIPSChannelTable_Object = MibTable
hpnicfWIPSChannelTable = _HpnicfWIPSChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 9)
)
if mibBuilder.loadTexts:
    hpnicfWIPSChannelTable.setStatus("current")
_HpnicfWIPSChannelEntry_Object = MibTableRow
hpnicfWIPSChannelEntry = _HpnicfWIPSChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 9, 1)
)
hpnicfWIPSChannelEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSChannelNum"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSChannelEntry.setStatus("current")
_HpnicfWIPSChannelNum_Type = HpnicfWIPSChannel
_HpnicfWIPSChannelNum_Object = MibTableColumn
hpnicfWIPSChannelNum = _HpnicfWIPSChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 9, 1, 1),
    _HpnicfWIPSChannelNum_Type()
)
hpnicfWIPSChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSChannelNum.setStatus("current")
_HpnicfWIPSChannelRadioType_Type = HpnicfWIPSRadioType
_HpnicfWIPSChannelRadioType_Object = MibTableColumn
hpnicfWIPSChannelRadioType = _HpnicfWIPSChannelRadioType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 9, 1, 2),
    _HpnicfWIPSChannelRadioType_Type()
)
hpnicfWIPSChannelRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChannelRadioType.setStatus("current")
_HpnicfWIPSChannelIsPermitted_Type = TruthValue
_HpnicfWIPSChannelIsPermitted_Object = MibTableColumn
hpnicfWIPSChannelIsPermitted = _HpnicfWIPSChannelIsPermitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 9, 1, 3),
    _HpnicfWIPSChannelIsPermitted_Type()
)
hpnicfWIPSChannelIsPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChannelIsPermitted.setStatus("current")
_HpnicfWIPSChannelLastRptTm_Type = TimeTicks
_HpnicfWIPSChannelLastRptTm_Object = MibTableColumn
hpnicfWIPSChannelLastRptTm = _HpnicfWIPSChannelLastRptTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 9, 1, 4),
    _HpnicfWIPSChannelLastRptTm_Type()
)
hpnicfWIPSChannelLastRptTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChannelLastRptTm.setStatus("current")
_HpnicfWIPSCountermeasureListTable_Object = MibTable
hpnicfWIPSCountermeasureListTable = _HpnicfWIPSCountermeasureListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 10)
)
if mibBuilder.loadTexts:
    hpnicfWIPSCountermeasureListTable.setStatus("current")
_HpnicfWIPSCountermeasureListEntry_Object = MibTableRow
hpnicfWIPSCountermeasureListEntry = _HpnicfWIPSCountermeasureListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 10, 1)
)
hpnicfWIPSCountermeasureListEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSCtmListMacAddress"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSCountermeasureListEntry.setStatus("current")
_HpnicfWIPSCtmListMacAddress_Type = MacAddress
_HpnicfWIPSCtmListMacAddress_Object = MibTableColumn
hpnicfWIPSCtmListMacAddress = _HpnicfWIPSCtmListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 10, 1, 1),
    _HpnicfWIPSCtmListMacAddress_Type()
)
hpnicfWIPSCtmListMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmListMacAddress.setStatus("current")
_HpnicfWIPSCtmListLastestWorkChl_Type = HpnicfWIPSChannel
_HpnicfWIPSCtmListLastestWorkChl_Object = MibTableColumn
hpnicfWIPSCtmListLastestWorkChl = _HpnicfWIPSCtmListLastestWorkChl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 10, 1, 2),
    _HpnicfWIPSCtmListLastestWorkChl_Type()
)
hpnicfWIPSCtmListLastestWorkChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmListLastestWorkChl.setStatus("current")
_HpnicfWIPSCtmListFirstTm_Type = TimeTicks
_HpnicfWIPSCtmListFirstTm_Object = MibTableColumn
hpnicfWIPSCtmListFirstTm = _HpnicfWIPSCtmListFirstTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 10, 1, 3),
    _HpnicfWIPSCtmListFirstTm_Type()
)
hpnicfWIPSCtmListFirstTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmListFirstTm.setStatus("current")
_HpnicfWIPSCtmListLastTm_Type = TimeTicks
_HpnicfWIPSCtmListLastTm_Object = MibTableColumn
hpnicfWIPSCtmListLastTm = _HpnicfWIPSCtmListLastTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 10, 1, 4),
    _HpnicfWIPSCtmListLastTm_Type()
)
hpnicfWIPSCtmListLastTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmListLastTm.setStatus("current")
_HpnicfWIPSCtmListQurCnt_Type = Integer32
_HpnicfWIPSCtmListQurCnt_Object = MibTableColumn
hpnicfWIPSCtmListQurCnt = _HpnicfWIPSCtmListQurCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 10, 1, 5),
    _HpnicfWIPSCtmListQurCnt_Type()
)
hpnicfWIPSCtmListQurCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmListQurCnt.setStatus("current")
_HpnicfWIPSCtmListSensorNum_Type = Integer32
_HpnicfWIPSCtmListSensorNum_Object = MibTableColumn
hpnicfWIPSCtmListSensorNum = _HpnicfWIPSCtmListSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 10, 1, 6),
    _HpnicfWIPSCtmListSensorNum_Type()
)
hpnicfWIPSCtmListSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmListSensorNum.setStatus("current")
_HpnicfWIPSIgnoreListTable_Object = MibTable
hpnicfWIPSIgnoreListTable = _HpnicfWIPSIgnoreListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 11)
)
if mibBuilder.loadTexts:
    hpnicfWIPSIgnoreListTable.setStatus("current")
_HpnicfWIPSIgnoreListEntry_Object = MibTableRow
hpnicfWIPSIgnoreListEntry = _HpnicfWIPSIgnoreListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 11, 1)
)
hpnicfWIPSIgnoreListEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSIgnoreListMacAddress"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSIgnoreListEntry.setStatus("current")
_HpnicfWIPSIgnoreListMacAddress_Type = MacAddress
_HpnicfWIPSIgnoreListMacAddress_Object = MibTableColumn
hpnicfWIPSIgnoreListMacAddress = _HpnicfWIPSIgnoreListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 11, 1, 1),
    _HpnicfWIPSIgnoreListMacAddress_Type()
)
hpnicfWIPSIgnoreListMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSIgnoreListMacAddress.setStatus("current")
_HpnicfWIPSIgnoreListFirstIgnoreTm_Type = TimeTicks
_HpnicfWIPSIgnoreListFirstIgnoreTm_Object = MibTableColumn
hpnicfWIPSIgnoreListFirstIgnoreTm = _HpnicfWIPSIgnoreListFirstIgnoreTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 11, 1, 2),
    _HpnicfWIPSIgnoreListFirstIgnoreTm_Type()
)
hpnicfWIPSIgnoreListFirstIgnoreTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSIgnoreListFirstIgnoreTm.setStatus("current")
_HpnicfWIPSIgnoreListLastIgnoreTm_Type = TimeTicks
_HpnicfWIPSIgnoreListLastIgnoreTm_Object = MibTableColumn
hpnicfWIPSIgnoreListLastIgnoreTm = _HpnicfWIPSIgnoreListLastIgnoreTm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 11, 1, 3),
    _HpnicfWIPSIgnoreListLastIgnoreTm_Type()
)
hpnicfWIPSIgnoreListLastIgnoreTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSIgnoreListLastIgnoreTm.setStatus("current")
_HpnicfWIPSIgnoreListIgnoreCnt_Type = Integer32
_HpnicfWIPSIgnoreListIgnoreCnt_Object = MibTableColumn
hpnicfWIPSIgnoreListIgnoreCnt = _HpnicfWIPSIgnoreListIgnoreCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 11, 1, 4),
    _HpnicfWIPSIgnoreListIgnoreCnt_Type()
)
hpnicfWIPSIgnoreListIgnoreCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSIgnoreListIgnoreCnt.setStatus("current")
_HpnicfWIPSTrustListTable_Object = MibTable
hpnicfWIPSTrustListTable = _HpnicfWIPSTrustListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 12)
)
if mibBuilder.loadTexts:
    hpnicfWIPSTrustListTable.setStatus("current")
_HpnicfWIPSTrustListEntry_Object = MibTableRow
hpnicfWIPSTrustListEntry = _HpnicfWIPSTrustListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 12, 1)
)
hpnicfWIPSTrustListEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSTrustListMacAddress"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSTrustListEntry.setStatus("current")
_HpnicfWIPSTrustListMacAddress_Type = MacAddress
_HpnicfWIPSTrustListMacAddress_Object = MibTableColumn
hpnicfWIPSTrustListMacAddress = _HpnicfWIPSTrustListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 12, 1, 1),
    _HpnicfWIPSTrustListMacAddress_Type()
)
hpnicfWIPSTrustListMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSTrustListMacAddress.setStatus("current")


class _HpnicfWIPSTrustListStatus_Type(Integer32):
    """Custom type hpnicfWIPSTrustListStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1),
          ("staticAndDynamic", 3))
    )


_HpnicfWIPSTrustListStatus_Type.__name__ = "Integer32"
_HpnicfWIPSTrustListStatus_Object = MibTableColumn
hpnicfWIPSTrustListStatus = _HpnicfWIPSTrustListStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 12, 1, 2),
    _HpnicfWIPSTrustListStatus_Type()
)
hpnicfWIPSTrustListStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSTrustListStatus.setStatus("current")
_HpnicfWIPSChlStatTable_Object = MibTable
hpnicfWIPSChlStatTable = _HpnicfWIPSChlStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13)
)
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatTable.setStatus("current")
_HpnicfWIPSChlStatEntry_Object = MibTableRow
hpnicfWIPSChlStatEntry = _HpnicfWIPSChlStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1)
)
hpnicfWIPSChlStatEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSChlStatSensorMacAddr"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSChlStatChannel"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatEntry.setStatus("current")
_HpnicfWIPSChlStatSensorMacAddr_Type = MacAddress
_HpnicfWIPSChlStatSensorMacAddr_Object = MibTableColumn
hpnicfWIPSChlStatSensorMacAddr = _HpnicfWIPSChlStatSensorMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 1),
    _HpnicfWIPSChlStatSensorMacAddr_Type()
)
hpnicfWIPSChlStatSensorMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatSensorMacAddr.setStatus("current")
_HpnicfWIPSChlStatChannel_Type = HpnicfWIPSChannel
_HpnicfWIPSChlStatChannel_Object = MibTableColumn
hpnicfWIPSChlStatChannel = _HpnicfWIPSChlStatChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 2),
    _HpnicfWIPSChlStatChannel_Type()
)
hpnicfWIPSChlStatChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatChannel.setStatus("current")


class _HpnicfWIPSChlStatTotalPkt_Type(Counter64):
    """Custom type hpnicfWIPSChlStatTotalPkt based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatTotalPkt_Object = MibTableColumn
hpnicfWIPSChlStatTotalPkt = _HpnicfWIPSChlStatTotalPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 3),
    _HpnicfWIPSChlStatTotalPkt_Type()
)
hpnicfWIPSChlStatTotalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatTotalPkt.setStatus("current")


class _HpnicfWIPSChlStatTotalByte_Type(Counter64):
    """Custom type hpnicfWIPSChlStatTotalByte based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatTotalByte_Object = MibTableColumn
hpnicfWIPSChlStatTotalByte = _HpnicfWIPSChlStatTotalByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 4),
    _HpnicfWIPSChlStatTotalByte_Type()
)
hpnicfWIPSChlStatTotalByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatTotalByte.setStatus("current")


class _HpnicfWIPSChlStatBmcastPkt_Type(Counter64):
    """Custom type hpnicfWIPSChlStatBmcastPkt based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatBmcastPkt_Object = MibTableColumn
hpnicfWIPSChlStatBmcastPkt = _HpnicfWIPSChlStatBmcastPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 5),
    _HpnicfWIPSChlStatBmcastPkt_Type()
)
hpnicfWIPSChlStatBmcastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatBmcastPkt.setStatus("current")


class _HpnicfWIPSChlStatBmcastByte_Type(Counter64):
    """Custom type hpnicfWIPSChlStatBmcastByte based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatBmcastByte_Object = MibTableColumn
hpnicfWIPSChlStatBmcastByte = _HpnicfWIPSChlStatBmcastByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 6),
    _HpnicfWIPSChlStatBmcastByte_Type()
)
hpnicfWIPSChlStatBmcastByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatBmcastByte.setStatus("current")


class _HpnicfWIPSChlStatUnicastPkt_Type(Counter64):
    """Custom type hpnicfWIPSChlStatUnicastPkt based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatUnicastPkt_Object = MibTableColumn
hpnicfWIPSChlStatUnicastPkt = _HpnicfWIPSChlStatUnicastPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 7),
    _HpnicfWIPSChlStatUnicastPkt_Type()
)
hpnicfWIPSChlStatUnicastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatUnicastPkt.setStatus("current")


class _HpnicfWIPSChlStatUnicastByte_Type(Counter64):
    """Custom type hpnicfWIPSChlStatUnicastByte based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatUnicastByte_Object = MibTableColumn
hpnicfWIPSChlStatUnicastByte = _HpnicfWIPSChlStatUnicastByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 8),
    _HpnicfWIPSChlStatUnicastByte_Type()
)
hpnicfWIPSChlStatUnicastByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatUnicastByte.setStatus("current")


class _HpnicfWIPSChlStatManagement_Type(Counter64):
    """Custom type hpnicfWIPSChlStatManagement based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatManagement_Object = MibTableColumn
hpnicfWIPSChlStatManagement = _HpnicfWIPSChlStatManagement_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 9),
    _HpnicfWIPSChlStatManagement_Type()
)
hpnicfWIPSChlStatManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatManagement.setStatus("current")


class _HpnicfWIPSChlStatControl_Type(Counter64):
    """Custom type hpnicfWIPSChlStatControl based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatControl_Object = MibTableColumn
hpnicfWIPSChlStatControl = _HpnicfWIPSChlStatControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 10),
    _HpnicfWIPSChlStatControl_Type()
)
hpnicfWIPSChlStatControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatControl.setStatus("current")


class _HpnicfWIPSChlStatData_Type(Counter64):
    """Custom type hpnicfWIPSChlStatData based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatData_Object = MibTableColumn
hpnicfWIPSChlStatData = _HpnicfWIPSChlStatData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 11),
    _HpnicfWIPSChlStatData_Type()
)
hpnicfWIPSChlStatData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatData.setStatus("current")


class _HpnicfWIPSChlStatBeacon_Type(Counter64):
    """Custom type hpnicfWIPSChlStatBeacon based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatBeacon_Object = MibTableColumn
hpnicfWIPSChlStatBeacon = _HpnicfWIPSChlStatBeacon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 12),
    _HpnicfWIPSChlStatBeacon_Type()
)
hpnicfWIPSChlStatBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatBeacon.setStatus("current")


class _HpnicfWIPSChlStatRTS_Type(Counter64):
    """Custom type hpnicfWIPSChlStatRTS based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatRTS_Object = MibTableColumn
hpnicfWIPSChlStatRTS = _HpnicfWIPSChlStatRTS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 13),
    _HpnicfWIPSChlStatRTS_Type()
)
hpnicfWIPSChlStatRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatRTS.setStatus("current")


class _HpnicfWIPSChlStatCTS_Type(Counter64):
    """Custom type hpnicfWIPSChlStatCTS based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatCTS_Object = MibTableColumn
hpnicfWIPSChlStatCTS = _HpnicfWIPSChlStatCTS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 14),
    _HpnicfWIPSChlStatCTS_Type()
)
hpnicfWIPSChlStatCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatCTS.setStatus("current")


class _HpnicfWIPSChlStatProbeRequest_Type(Counter64):
    """Custom type hpnicfWIPSChlStatProbeRequest based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatProbeRequest_Object = MibTableColumn
hpnicfWIPSChlStatProbeRequest = _HpnicfWIPSChlStatProbeRequest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 15),
    _HpnicfWIPSChlStatProbeRequest_Type()
)
hpnicfWIPSChlStatProbeRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatProbeRequest.setStatus("current")


class _HpnicfWIPSChlStatProbeResponse_Type(Counter64):
    """Custom type hpnicfWIPSChlStatProbeResponse based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatProbeResponse_Object = MibTableColumn
hpnicfWIPSChlStatProbeResponse = _HpnicfWIPSChlStatProbeResponse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 16),
    _HpnicfWIPSChlStatProbeResponse_Type()
)
hpnicfWIPSChlStatProbeResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatProbeResponse.setStatus("current")


class _HpnicfWIPSChlStatFragment_Type(Counter64):
    """Custom type hpnicfWIPSChlStatFragment based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatFragment_Object = MibTableColumn
hpnicfWIPSChlStatFragment = _HpnicfWIPSChlStatFragment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 17),
    _HpnicfWIPSChlStatFragment_Type()
)
hpnicfWIPSChlStatFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatFragment.setStatus("current")


class _HpnicfWIPSChlStatRetry_Type(Counter64):
    """Custom type hpnicfWIPSChlStatRetry based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatRetry_Object = MibTableColumn
hpnicfWIPSChlStatRetry = _HpnicfWIPSChlStatRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 18),
    _HpnicfWIPSChlStatRetry_Type()
)
hpnicfWIPSChlStatRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatRetry.setStatus("current")


class _HpnicfWIPSChlStatEapSuccess_Type(Counter64):
    """Custom type hpnicfWIPSChlStatEapSuccess based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatEapSuccess_Object = MibTableColumn
hpnicfWIPSChlStatEapSuccess = _HpnicfWIPSChlStatEapSuccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 19),
    _HpnicfWIPSChlStatEapSuccess_Type()
)
hpnicfWIPSChlStatEapSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatEapSuccess.setStatus("current")


class _HpnicfWIPSChlStatEapFailure_Type(Counter64):
    """Custom type hpnicfWIPSChlStatEapFailure based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatEapFailure_Object = MibTableColumn
hpnicfWIPSChlStatEapFailure = _HpnicfWIPSChlStatEapFailure_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 20),
    _HpnicfWIPSChlStatEapFailure_Type()
)
hpnicfWIPSChlStatEapFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatEapFailure.setStatus("current")


class _HpnicfWIPSChlStatEapolStart_Type(Counter64):
    """Custom type hpnicfWIPSChlStatEapolStart based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatEapolStart_Object = MibTableColumn
hpnicfWIPSChlStatEapolStart = _HpnicfWIPSChlStatEapolStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 21),
    _HpnicfWIPSChlStatEapolStart_Type()
)
hpnicfWIPSChlStatEapolStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatEapolStart.setStatus("current")


class _HpnicfWIPSChlStatEapolLogoff_Type(Counter64):
    """Custom type hpnicfWIPSChlStatEapolLogoff based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatEapolLogoff_Object = MibTableColumn
hpnicfWIPSChlStatEapolLogoff = _HpnicfWIPSChlStatEapolLogoff_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 22),
    _HpnicfWIPSChlStatEapolLogoff_Type()
)
hpnicfWIPSChlStatEapolLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatEapolLogoff.setStatus("current")


class _HpnicfWIPSChlStatAssocRequest_Type(Counter64):
    """Custom type hpnicfWIPSChlStatAssocRequest based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatAssocRequest_Object = MibTableColumn
hpnicfWIPSChlStatAssocRequest = _HpnicfWIPSChlStatAssocRequest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 23),
    _HpnicfWIPSChlStatAssocRequest_Type()
)
hpnicfWIPSChlStatAssocRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatAssocRequest.setStatus("current")


class _HpnicfWIPSChlStatAssocResponse_Type(Counter64):
    """Custom type hpnicfWIPSChlStatAssocResponse based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatAssocResponse_Object = MibTableColumn
hpnicfWIPSChlStatAssocResponse = _HpnicfWIPSChlStatAssocResponse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 24),
    _HpnicfWIPSChlStatAssocResponse_Type()
)
hpnicfWIPSChlStatAssocResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatAssocResponse.setStatus("current")


class _HpnicfWIPSChlStatUnicastDisassoc_Type(Counter64):
    """Custom type hpnicfWIPSChlStatUnicastDisassoc based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatUnicastDisassoc_Object = MibTableColumn
hpnicfWIPSChlStatUnicastDisassoc = _HpnicfWIPSChlStatUnicastDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 25),
    _HpnicfWIPSChlStatUnicastDisassoc_Type()
)
hpnicfWIPSChlStatUnicastDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatUnicastDisassoc.setStatus("current")


class _HpnicfWIPSChlStatBroadcastDisassoc_Type(Counter64):
    """Custom type hpnicfWIPSChlStatBroadcastDisassoc based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatBroadcastDisassoc_Object = MibTableColumn
hpnicfWIPSChlStatBroadcastDisassoc = _HpnicfWIPSChlStatBroadcastDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 26),
    _HpnicfWIPSChlStatBroadcastDisassoc_Type()
)
hpnicfWIPSChlStatBroadcastDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatBroadcastDisassoc.setStatus("current")


class _HpnicfWIPSChlStatAuthentication_Type(Counter64):
    """Custom type hpnicfWIPSChlStatAuthentication based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatAuthentication_Object = MibTableColumn
hpnicfWIPSChlStatAuthentication = _HpnicfWIPSChlStatAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 27),
    _HpnicfWIPSChlStatAuthentication_Type()
)
hpnicfWIPSChlStatAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatAuthentication.setStatus("current")


class _HpnicfWIPSChlStatUnicastDeauthen_Type(Counter64):
    """Custom type hpnicfWIPSChlStatUnicastDeauthen based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatUnicastDeauthen_Object = MibTableColumn
hpnicfWIPSChlStatUnicastDeauthen = _HpnicfWIPSChlStatUnicastDeauthen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 28),
    _HpnicfWIPSChlStatUnicastDeauthen_Type()
)
hpnicfWIPSChlStatUnicastDeauthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatUnicastDeauthen.setStatus("current")


class _HpnicfWIPSChlStatBroadcastDeauthen_Type(Counter64):
    """Custom type hpnicfWIPSChlStatBroadcastDeauthen based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatBroadcastDeauthen_Object = MibTableColumn
hpnicfWIPSChlStatBroadcastDeauthen = _HpnicfWIPSChlStatBroadcastDeauthen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 29),
    _HpnicfWIPSChlStatBroadcastDeauthen_Type()
)
hpnicfWIPSChlStatBroadcastDeauthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatBroadcastDeauthen.setStatus("current")


class _HpnicfWIPSChlStatMalformed_Type(Counter64):
    """Custom type hpnicfWIPSChlStatMalformed based on Counter64"""
    defaultValue = 0


_HpnicfWIPSChlStatMalformed_Object = MibTableColumn
hpnicfWIPSChlStatMalformed = _HpnicfWIPSChlStatMalformed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 13, 1, 30),
    _HpnicfWIPSChlStatMalformed_Type()
)
hpnicfWIPSChlStatMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSChlStatMalformed.setStatus("current")
_HpnicfWIPSDevStatTable_Object = MibTable
hpnicfWIPSDevStatTable = _HpnicfWIPSDevStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14)
)
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTable.setStatus("current")
_HpnicfWIPSDevStatEntry_Object = MibTableRow
hpnicfWIPSDevStatEntry = _HpnicfWIPSDevStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1)
)
hpnicfWIPSDevStatEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDevStatSensorMacAddr"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDevStatDevMacAddress"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSDevStatChannel"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatEntry.setStatus("current")
_HpnicfWIPSDevStatSensorMacAddr_Type = MacAddress
_HpnicfWIPSDevStatSensorMacAddr_Object = MibTableColumn
hpnicfWIPSDevStatSensorMacAddr = _HpnicfWIPSDevStatSensorMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 1),
    _HpnicfWIPSDevStatSensorMacAddr_Type()
)
hpnicfWIPSDevStatSensorMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatSensorMacAddr.setStatus("current")
_HpnicfWIPSDevStatDevMacAddress_Type = MacAddress
_HpnicfWIPSDevStatDevMacAddress_Object = MibTableColumn
hpnicfWIPSDevStatDevMacAddress = _HpnicfWIPSDevStatDevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 2),
    _HpnicfWIPSDevStatDevMacAddress_Type()
)
hpnicfWIPSDevStatDevMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatDevMacAddress.setStatus("current")
_HpnicfWIPSDevStatChannel_Type = HpnicfWIPSChannel
_HpnicfWIPSDevStatChannel_Object = MibTableColumn
hpnicfWIPSDevStatChannel = _HpnicfWIPSDevStatChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 3),
    _HpnicfWIPSDevStatChannel_Type()
)
hpnicfWIPSDevStatChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatChannel.setStatus("current")


class _HpnicfWIPSDevStatTxTotalPkt_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxTotalPkt based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxTotalPkt_Object = MibTableColumn
hpnicfWIPSDevStatTxTotalPkt = _HpnicfWIPSDevStatTxTotalPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 4),
    _HpnicfWIPSDevStatTxTotalPkt_Type()
)
hpnicfWIPSDevStatTxTotalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxTotalPkt.setStatus("current")


class _HpnicfWIPSDevStatTxTotalByte_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxTotalByte based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxTotalByte_Object = MibTableColumn
hpnicfWIPSDevStatTxTotalByte = _HpnicfWIPSDevStatTxTotalByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 5),
    _HpnicfWIPSDevStatTxTotalByte_Type()
)
hpnicfWIPSDevStatTxTotalByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxTotalByte.setStatus("current")


class _HpnicfWIPSDevStatTxBMcastPkt_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxBMcastPkt based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxBMcastPkt_Object = MibTableColumn
hpnicfWIPSDevStatTxBMcastPkt = _HpnicfWIPSDevStatTxBMcastPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 6),
    _HpnicfWIPSDevStatTxBMcastPkt_Type()
)
hpnicfWIPSDevStatTxBMcastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxBMcastPkt.setStatus("current")


class _HpnicfWIPSDevStatTxBMcastByte_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxBMcastByte based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxBMcastByte_Object = MibTableColumn
hpnicfWIPSDevStatTxBMcastByte = _HpnicfWIPSDevStatTxBMcastByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 7),
    _HpnicfWIPSDevStatTxBMcastByte_Type()
)
hpnicfWIPSDevStatTxBMcastByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxBMcastByte.setStatus("current")


class _HpnicfWIPSDevStatTxUnicastPkt_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxUnicastPkt based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxUnicastPkt_Object = MibTableColumn
hpnicfWIPSDevStatTxUnicastPkt = _HpnicfWIPSDevStatTxUnicastPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 8),
    _HpnicfWIPSDevStatTxUnicastPkt_Type()
)
hpnicfWIPSDevStatTxUnicastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxUnicastPkt.setStatus("current")


class _HpnicfWIPSDevStatTxUnicastByte_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxUnicastByte based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxUnicastByte_Object = MibTableColumn
hpnicfWIPSDevStatTxUnicastByte = _HpnicfWIPSDevStatTxUnicastByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 9),
    _HpnicfWIPSDevStatTxUnicastByte_Type()
)
hpnicfWIPSDevStatTxUnicastByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxUnicastByte.setStatus("current")


class _HpnicfWIPSDevStatTxMgmt_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxMgmt based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxMgmt_Object = MibTableColumn
hpnicfWIPSDevStatTxMgmt = _HpnicfWIPSDevStatTxMgmt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 10),
    _HpnicfWIPSDevStatTxMgmt_Type()
)
hpnicfWIPSDevStatTxMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxMgmt.setStatus("current")


class _HpnicfWIPSDevStatTxCtrl_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxCtrl based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxCtrl_Object = MibTableColumn
hpnicfWIPSDevStatTxCtrl = _HpnicfWIPSDevStatTxCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 11),
    _HpnicfWIPSDevStatTxCtrl_Type()
)
hpnicfWIPSDevStatTxCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxCtrl.setStatus("current")


class _HpnicfWIPSDevStatTxData_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxData based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxData_Object = MibTableColumn
hpnicfWIPSDevStatTxData = _HpnicfWIPSDevStatTxData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 12),
    _HpnicfWIPSDevStatTxData_Type()
)
hpnicfWIPSDevStatTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxData.setStatus("current")


class _HpnicfWIPSDevStatTxBeacon_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxBeacon based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxBeacon_Object = MibTableColumn
hpnicfWIPSDevStatTxBeacon = _HpnicfWIPSDevStatTxBeacon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 13),
    _HpnicfWIPSDevStatTxBeacon_Type()
)
hpnicfWIPSDevStatTxBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxBeacon.setStatus("current")


class _HpnicfWIPSDevStatTxRTS_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxRTS based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxRTS_Object = MibTableColumn
hpnicfWIPSDevStatTxRTS = _HpnicfWIPSDevStatTxRTS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 14),
    _HpnicfWIPSDevStatTxRTS_Type()
)
hpnicfWIPSDevStatTxRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxRTS.setStatus("current")


class _HpnicfWIPSDevStatTxProbeRequest_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxProbeRequest based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxProbeRequest_Object = MibTableColumn
hpnicfWIPSDevStatTxProbeRequest = _HpnicfWIPSDevStatTxProbeRequest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 15),
    _HpnicfWIPSDevStatTxProbeRequest_Type()
)
hpnicfWIPSDevStatTxProbeRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxProbeRequest.setStatus("current")


class _HpnicfWIPSDevStatTxProbeResponse_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxProbeResponse based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxProbeResponse_Object = MibTableColumn
hpnicfWIPSDevStatTxProbeResponse = _HpnicfWIPSDevStatTxProbeResponse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 16),
    _HpnicfWIPSDevStatTxProbeResponse_Type()
)
hpnicfWIPSDevStatTxProbeResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxProbeResponse.setStatus("current")


class _HpnicfWIPSDevStatTxFragment_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxFragment based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxFragment_Object = MibTableColumn
hpnicfWIPSDevStatTxFragment = _HpnicfWIPSDevStatTxFragment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 17),
    _HpnicfWIPSDevStatTxFragment_Type()
)
hpnicfWIPSDevStatTxFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxFragment.setStatus("current")


class _HpnicfWIPSDevStatTxRetry_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxRetry based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxRetry_Object = MibTableColumn
hpnicfWIPSDevStatTxRetry = _HpnicfWIPSDevStatTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 18),
    _HpnicfWIPSDevStatTxRetry_Type()
)
hpnicfWIPSDevStatTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxRetry.setStatus("current")


class _HpnicfWIPSDevStatTxAssocRequest_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxAssocRequest based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxAssocRequest_Object = MibTableColumn
hpnicfWIPSDevStatTxAssocRequest = _HpnicfWIPSDevStatTxAssocRequest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 19),
    _HpnicfWIPSDevStatTxAssocRequest_Type()
)
hpnicfWIPSDevStatTxAssocRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxAssocRequest.setStatus("current")


class _HpnicfWIPSDevStatTxAssocResponse_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxAssocResponse based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxAssocResponse_Object = MibTableColumn
hpnicfWIPSDevStatTxAssocResponse = _HpnicfWIPSDevStatTxAssocResponse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 20),
    _HpnicfWIPSDevStatTxAssocResponse_Type()
)
hpnicfWIPSDevStatTxAssocResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxAssocResponse.setStatus("current")


class _HpnicfWIPSDevStatTxUnicastDisassoc_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxUnicastDisassoc based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxUnicastDisassoc_Object = MibTableColumn
hpnicfWIPSDevStatTxUnicastDisassoc = _HpnicfWIPSDevStatTxUnicastDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 21),
    _HpnicfWIPSDevStatTxUnicastDisassoc_Type()
)
hpnicfWIPSDevStatTxUnicastDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxUnicastDisassoc.setStatus("current")


class _HpnicfWIPSDevStatTxBcastDisassoc_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxBcastDisassoc based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxBcastDisassoc_Object = MibTableColumn
hpnicfWIPSDevStatTxBcastDisassoc = _HpnicfWIPSDevStatTxBcastDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 22),
    _HpnicfWIPSDevStatTxBcastDisassoc_Type()
)
hpnicfWIPSDevStatTxBcastDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxBcastDisassoc.setStatus("current")


class _HpnicfWIPSDevStatTxAuth_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxAuth based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxAuth_Object = MibTableColumn
hpnicfWIPSDevStatTxAuth = _HpnicfWIPSDevStatTxAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 23),
    _HpnicfWIPSDevStatTxAuth_Type()
)
hpnicfWIPSDevStatTxAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxAuth.setStatus("current")


class _HpnicfWIPSDevStatTxUnicastDeauth_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxUnicastDeauth based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxUnicastDeauth_Object = MibTableColumn
hpnicfWIPSDevStatTxUnicastDeauth = _HpnicfWIPSDevStatTxUnicastDeauth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 24),
    _HpnicfWIPSDevStatTxUnicastDeauth_Type()
)
hpnicfWIPSDevStatTxUnicastDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxUnicastDeauth.setStatus("current")


class _HpnicfWIPSDevStatTxBcastDeauth_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxBcastDeauth based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxBcastDeauth_Object = MibTableColumn
hpnicfWIPSDevStatTxBcastDeauth = _HpnicfWIPSDevStatTxBcastDeauth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 25),
    _HpnicfWIPSDevStatTxBcastDeauth_Type()
)
hpnicfWIPSDevStatTxBcastDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxBcastDeauth.setStatus("current")


class _HpnicfWIPSDevStatTxEAPSuccess_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxEAPSuccess based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxEAPSuccess_Object = MibTableColumn
hpnicfWIPSDevStatTxEAPSuccess = _HpnicfWIPSDevStatTxEAPSuccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 26),
    _HpnicfWIPSDevStatTxEAPSuccess_Type()
)
hpnicfWIPSDevStatTxEAPSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxEAPSuccess.setStatus("current")


class _HpnicfWIPSDevStatTxEAPFailure_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxEAPFailure based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxEAPFailure_Object = MibTableColumn
hpnicfWIPSDevStatTxEAPFailure = _HpnicfWIPSDevStatTxEAPFailure_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 27),
    _HpnicfWIPSDevStatTxEAPFailure_Type()
)
hpnicfWIPSDevStatTxEAPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxEAPFailure.setStatus("current")


class _HpnicfWIPSDevStatTxEAPOLStart_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxEAPOLStart based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxEAPOLStart_Object = MibTableColumn
hpnicfWIPSDevStatTxEAPOLStart = _HpnicfWIPSDevStatTxEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 28),
    _HpnicfWIPSDevStatTxEAPOLStart_Type()
)
hpnicfWIPSDevStatTxEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxEAPOLStart.setStatus("current")


class _HpnicfWIPSDevStatTxEAPOLLogOff_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxEAPOLLogOff based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxEAPOLLogOff_Object = MibTableColumn
hpnicfWIPSDevStatTxEAPOLLogOff = _HpnicfWIPSDevStatTxEAPOLLogOff_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 29),
    _HpnicfWIPSDevStatTxEAPOLLogOff_Type()
)
hpnicfWIPSDevStatTxEAPOLLogOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxEAPOLLogOff.setStatus("current")


class _HpnicfWIPSDevStatTxMalformed_Type(Counter64):
    """Custom type hpnicfWIPSDevStatTxMalformed based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatTxMalformed_Object = MibTableColumn
hpnicfWIPSDevStatTxMalformed = _HpnicfWIPSDevStatTxMalformed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 30),
    _HpnicfWIPSDevStatTxMalformed_Type()
)
hpnicfWIPSDevStatTxMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatTxMalformed.setStatus("current")


class _HpnicfWIPSDevStatRxTotalPkt_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxTotalPkt based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxTotalPkt_Object = MibTableColumn
hpnicfWIPSDevStatRxTotalPkt = _HpnicfWIPSDevStatRxTotalPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 31),
    _HpnicfWIPSDevStatRxTotalPkt_Type()
)
hpnicfWIPSDevStatRxTotalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxTotalPkt.setStatus("current")


class _HpnicfWIPSDevStatRxTotalByte_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxTotalByte based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxTotalByte_Object = MibTableColumn
hpnicfWIPSDevStatRxTotalByte = _HpnicfWIPSDevStatRxTotalByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 32),
    _HpnicfWIPSDevStatRxTotalByte_Type()
)
hpnicfWIPSDevStatRxTotalByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxTotalByte.setStatus("current")


class _HpnicfWIPSDevStatRxUnicastPkt_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxUnicastPkt based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxUnicastPkt_Object = MibTableColumn
hpnicfWIPSDevStatRxUnicastPkt = _HpnicfWIPSDevStatRxUnicastPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 33),
    _HpnicfWIPSDevStatRxUnicastPkt_Type()
)
hpnicfWIPSDevStatRxUnicastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxUnicastPkt.setStatus("current")


class _HpnicfWIPSDevStatRxUnicastByte_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxUnicastByte based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxUnicastByte_Object = MibTableColumn
hpnicfWIPSDevStatRxUnicastByte = _HpnicfWIPSDevStatRxUnicastByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 34),
    _HpnicfWIPSDevStatRxUnicastByte_Type()
)
hpnicfWIPSDevStatRxUnicastByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxUnicastByte.setStatus("current")


class _HpnicfWIPSDevStatRxMgmt_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxMgmt based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxMgmt_Object = MibTableColumn
hpnicfWIPSDevStatRxMgmt = _HpnicfWIPSDevStatRxMgmt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 35),
    _HpnicfWIPSDevStatRxMgmt_Type()
)
hpnicfWIPSDevStatRxMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxMgmt.setStatus("current")


class _HpnicfWIPSDevStatRxCtrl_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxCtrl based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxCtrl_Object = MibTableColumn
hpnicfWIPSDevStatRxCtrl = _HpnicfWIPSDevStatRxCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 36),
    _HpnicfWIPSDevStatRxCtrl_Type()
)
hpnicfWIPSDevStatRxCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxCtrl.setStatus("current")


class _HpnicfWIPSDevStatRxData_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxData based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxData_Object = MibTableColumn
hpnicfWIPSDevStatRxData = _HpnicfWIPSDevStatRxData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 37),
    _HpnicfWIPSDevStatRxData_Type()
)
hpnicfWIPSDevStatRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxData.setStatus("current")


class _HpnicfWIPSDevStatRxRTS_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxRTS based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxRTS_Object = MibTableColumn
hpnicfWIPSDevStatRxRTS = _HpnicfWIPSDevStatRxRTS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 38),
    _HpnicfWIPSDevStatRxRTS_Type()
)
hpnicfWIPSDevStatRxRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxRTS.setStatus("current")


class _HpnicfWIPSDevStatRxCTS_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxCTS based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxCTS_Object = MibTableColumn
hpnicfWIPSDevStatRxCTS = _HpnicfWIPSDevStatRxCTS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 39),
    _HpnicfWIPSDevStatRxCTS_Type()
)
hpnicfWIPSDevStatRxCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxCTS.setStatus("current")


class _HpnicfWIPSDevStatRxProbeRequest_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxProbeRequest based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxProbeRequest_Object = MibTableColumn
hpnicfWIPSDevStatRxProbeRequest = _HpnicfWIPSDevStatRxProbeRequest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 40),
    _HpnicfWIPSDevStatRxProbeRequest_Type()
)
hpnicfWIPSDevStatRxProbeRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxProbeRequest.setStatus("current")


class _HpnicfWIPSDevStatRxProbeResponse_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxProbeResponse based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxProbeResponse_Object = MibTableColumn
hpnicfWIPSDevStatRxProbeResponse = _HpnicfWIPSDevStatRxProbeResponse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 41),
    _HpnicfWIPSDevStatRxProbeResponse_Type()
)
hpnicfWIPSDevStatRxProbeResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxProbeResponse.setStatus("current")


class _HpnicfWIPSDevStatRxFragment_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxFragment based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxFragment_Object = MibTableColumn
hpnicfWIPSDevStatRxFragment = _HpnicfWIPSDevStatRxFragment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 42),
    _HpnicfWIPSDevStatRxFragment_Type()
)
hpnicfWIPSDevStatRxFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxFragment.setStatus("current")


class _HpnicfWIPSDevStatRxRetry_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxRetry based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxRetry_Object = MibTableColumn
hpnicfWIPSDevStatRxRetry = _HpnicfWIPSDevStatRxRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 43),
    _HpnicfWIPSDevStatRxRetry_Type()
)
hpnicfWIPSDevStatRxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxRetry.setStatus("current")


class _HpnicfWIPSDevStatRxAssoRequest_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxAssoRequest based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxAssoRequest_Object = MibTableColumn
hpnicfWIPSDevStatRxAssoRequest = _HpnicfWIPSDevStatRxAssoRequest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 44),
    _HpnicfWIPSDevStatRxAssoRequest_Type()
)
hpnicfWIPSDevStatRxAssoRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxAssoRequest.setStatus("current")


class _HpnicfWIPSDevStatRxAssoResponse_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxAssoResponse based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxAssoResponse_Object = MibTableColumn
hpnicfWIPSDevStatRxAssoResponse = _HpnicfWIPSDevStatRxAssoResponse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 45),
    _HpnicfWIPSDevStatRxAssoResponse_Type()
)
hpnicfWIPSDevStatRxAssoResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxAssoResponse.setStatus("current")


class _HpnicfWIPSDevStatRxDisassoc_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxDisassoc based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxDisassoc_Object = MibTableColumn
hpnicfWIPSDevStatRxDisassoc = _HpnicfWIPSDevStatRxDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 46),
    _HpnicfWIPSDevStatRxDisassoc_Type()
)
hpnicfWIPSDevStatRxDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxDisassoc.setStatus("current")


class _HpnicfWIPSDevStatRxAuth_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxAuth based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxAuth_Object = MibTableColumn
hpnicfWIPSDevStatRxAuth = _HpnicfWIPSDevStatRxAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 47),
    _HpnicfWIPSDevStatRxAuth_Type()
)
hpnicfWIPSDevStatRxAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxAuth.setStatus("current")


class _HpnicfWIPSDevStatRxDeauth_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxDeauth based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxDeauth_Object = MibTableColumn
hpnicfWIPSDevStatRxDeauth = _HpnicfWIPSDevStatRxDeauth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 48),
    _HpnicfWIPSDevStatRxDeauth_Type()
)
hpnicfWIPSDevStatRxDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxDeauth.setStatus("current")


class _HpnicfWIPSDevStatRxEAPSuccess_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxEAPSuccess based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxEAPSuccess_Object = MibTableColumn
hpnicfWIPSDevStatRxEAPSuccess = _HpnicfWIPSDevStatRxEAPSuccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 49),
    _HpnicfWIPSDevStatRxEAPSuccess_Type()
)
hpnicfWIPSDevStatRxEAPSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxEAPSuccess.setStatus("current")


class _HpnicfWIPSDevStatRxEAPFailure_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxEAPFailure based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxEAPFailure_Object = MibTableColumn
hpnicfWIPSDevStatRxEAPFailure = _HpnicfWIPSDevStatRxEAPFailure_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 50),
    _HpnicfWIPSDevStatRxEAPFailure_Type()
)
hpnicfWIPSDevStatRxEAPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxEAPFailure.setStatus("current")


class _HpnicfWIPSDevStatRxEAPOLStart_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxEAPOLStart based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxEAPOLStart_Object = MibTableColumn
hpnicfWIPSDevStatRxEAPOLStart = _HpnicfWIPSDevStatRxEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 51),
    _HpnicfWIPSDevStatRxEAPOLStart_Type()
)
hpnicfWIPSDevStatRxEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxEAPOLStart.setStatus("current")


class _HpnicfWIPSDevStatRxEAPOLLogoff_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxEAPOLLogoff based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxEAPOLLogoff_Object = MibTableColumn
hpnicfWIPSDevStatRxEAPOLLogoff = _HpnicfWIPSDevStatRxEAPOLLogoff_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 52),
    _HpnicfWIPSDevStatRxEAPOLLogoff_Type()
)
hpnicfWIPSDevStatRxEAPOLLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxEAPOLLogoff.setStatus("current")


class _HpnicfWIPSDevStatRxMalformed_Type(Counter64):
    """Custom type hpnicfWIPSDevStatRxMalformed based on Counter64"""
    defaultValue = 0


_HpnicfWIPSDevStatRxMalformed_Object = MibTableColumn
hpnicfWIPSDevStatRxMalformed = _HpnicfWIPSDevStatRxMalformed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 14, 1, 53),
    _HpnicfWIPSDevStatRxMalformed_Type()
)
hpnicfWIPSDevStatRxMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSDevStatRxMalformed.setStatus("current")
_HpnicfWIPSCtmDeviceTable_Object = MibTable
hpnicfWIPSCtmDeviceTable = _HpnicfWIPSCtmDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 15)
)
if mibBuilder.loadTexts:
    hpnicfWIPSCtmDeviceTable.setStatus("current")
_HpnicfWIPSCtmDeviceEntry_Object = MibTableRow
hpnicfWIPSCtmDeviceEntry = _HpnicfWIPSCtmDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 15, 1)
)
hpnicfWIPSCtmDeviceEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSCtmDeviceVSD"),
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSCtmDeviceMAC"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSCtmDeviceEntry.setStatus("current")


class _HpnicfWIPSCtmDeviceVSD_Type(OctetString):
    """Custom type hpnicfWIPSCtmDeviceVSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfWIPSCtmDeviceVSD_Type.__name__ = "OctetString"
_HpnicfWIPSCtmDeviceVSD_Object = MibTableColumn
hpnicfWIPSCtmDeviceVSD = _HpnicfWIPSCtmDeviceVSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 15, 1, 1),
    _HpnicfWIPSCtmDeviceVSD_Type()
)
hpnicfWIPSCtmDeviceVSD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmDeviceVSD.setStatus("current")
_HpnicfWIPSCtmDeviceMAC_Type = MacAddress
_HpnicfWIPSCtmDeviceMAC_Object = MibTableColumn
hpnicfWIPSCtmDeviceMAC = _HpnicfWIPSCtmDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 15, 1, 2),
    _HpnicfWIPSCtmDeviceMAC_Type()
)
hpnicfWIPSCtmDeviceMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmDeviceMAC.setStatus("current")


class _HpnicfWIPSCtmDeviceType_Type(Integer32):
    """Custom type hpnicfWIPSCtmDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1),
          ("staticAnddynamic", 3))
    )


_HpnicfWIPSCtmDeviceType_Type.__name__ = "Integer32"
_HpnicfWIPSCtmDeviceType_Object = MibTableColumn
hpnicfWIPSCtmDeviceType = _HpnicfWIPSCtmDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 15, 1, 3),
    _HpnicfWIPSCtmDeviceType_Type()
)
hpnicfWIPSCtmDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmDeviceType.setStatus("current")


class _HpnicfWIPSCtmDeviceState_Type(Integer32):
    """Custom type hpnicfWIPSCtmDeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("action", 3),
          ("idle", 1),
          ("none", 0),
          ("pending", 2))
    )


_HpnicfWIPSCtmDeviceState_Type.__name__ = "Integer32"
_HpnicfWIPSCtmDeviceState_Object = MibTableColumn
hpnicfWIPSCtmDeviceState = _HpnicfWIPSCtmDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 15, 1, 4),
    _HpnicfWIPSCtmDeviceState_Type()
)
hpnicfWIPSCtmDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmDeviceState.setStatus("current")
_HpnicfWIPSCtmDeviceStartTime_Type = TimeTicks
_HpnicfWIPSCtmDeviceStartTime_Object = MibTableColumn
hpnicfWIPSCtmDeviceStartTime = _HpnicfWIPSCtmDeviceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 15, 1, 5),
    _HpnicfWIPSCtmDeviceStartTime_Type()
)
hpnicfWIPSCtmDeviceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmDeviceStartTime.setStatus("current")
_HpnicfWIPSCtmDeviceCategory_Type = HpnicfWIPSDeviceCategoryType
_HpnicfWIPSCtmDeviceCategory_Object = MibTableColumn
hpnicfWIPSCtmDeviceCategory = _HpnicfWIPSCtmDeviceCategory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 15, 1, 6),
    _HpnicfWIPSCtmDeviceCategory_Type()
)
hpnicfWIPSCtmDeviceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmDeviceCategory.setStatus("current")
_HpnicfWIPSCtmDeviceChl_Type = Unsigned32
_HpnicfWIPSCtmDeviceChl_Object = MibTableColumn
hpnicfWIPSCtmDeviceChl = _HpnicfWIPSCtmDeviceChl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 15, 1, 7),
    _HpnicfWIPSCtmDeviceChl_Type()
)
hpnicfWIPSCtmDeviceChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmDeviceChl.setStatus("current")


class _HpnicfWIPSCtmDevicePrecedence_Type(Integer32):
    """Custom type hpnicfWIPSCtmDevicePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HpnicfWIPSCtmDevicePrecedence_Type.__name__ = "Integer32"
_HpnicfWIPSCtmDevicePrecedence_Object = MibTableColumn
hpnicfWIPSCtmDevicePrecedence = _HpnicfWIPSCtmDevicePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 15, 1, 8),
    _HpnicfWIPSCtmDevicePrecedence_Type()
)
hpnicfWIPSCtmDevicePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSCtmDevicePrecedence.setStatus("current")
_HpnicfWIPSMalPktStatTable_Object = MibTable
hpnicfWIPSMalPktStatTable = _HpnicfWIPSMalPktStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16)
)
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatTable.setStatus("current")
_HpnicfWIPSMalPktStatEntry_Object = MibTableRow
hpnicfWIPSMalPktStatEntry = _HpnicfWIPSMalPktStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1)
)
hpnicfWIPSMalPktStatEntry.setIndexNames(
    (0, "HPN-ICF-WIPS-MIB", "hpnicfWIPSMalPktStatSensorMAC"),
)
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatEntry.setStatus("current")
_HpnicfWIPSMalPktStatSensorMAC_Type = MacAddress
_HpnicfWIPSMalPktStatSensorMAC_Object = MibTableColumn
hpnicfWIPSMalPktStatSensorMAC = _HpnicfWIPSMalPktStatSensorMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 1),
    _HpnicfWIPSMalPktStatSensorMAC_Type()
)
hpnicfWIPSMalPktStatSensorMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatSensorMAC.setStatus("current")


class _HpnicfWIPSMalPktStatInvalidIELength_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatInvalidIELength based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatInvalidIELength_Object = MibTableColumn
hpnicfWIPSMalPktStatInvalidIELength = _HpnicfWIPSMalPktStatInvalidIELength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 2),
    _HpnicfWIPSMalPktStatInvalidIELength_Type()
)
hpnicfWIPSMalPktStatInvalidIELength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatInvalidIELength.setStatus("current")


class _HpnicfWIPSMalPktStatDuplicatedIE_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatDuplicatedIE based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatDuplicatedIE_Object = MibTableColumn
hpnicfWIPSMalPktStatDuplicatedIE = _HpnicfWIPSMalPktStatDuplicatedIE_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 3),
    _HpnicfWIPSMalPktStatDuplicatedIE_Type()
)
hpnicfWIPSMalPktStatDuplicatedIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatDuplicatedIE.setStatus("current")


class _HpnicfWIPSMalPktStatRedundantIE_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatRedundantIE based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatRedundantIE_Object = MibTableColumn
hpnicfWIPSMalPktStatRedundantIE = _HpnicfWIPSMalPktStatRedundantIE_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 4),
    _HpnicfWIPSMalPktStatRedundantIE_Type()
)
hpnicfWIPSMalPktStatRedundantIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatRedundantIE.setStatus("current")


class _HpnicfWIPSMalPktStatInvalidPktLength_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatInvalidPktLength based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatInvalidPktLength_Object = MibTableColumn
hpnicfWIPSMalPktStatInvalidPktLength = _HpnicfWIPSMalPktStatInvalidPktLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 5),
    _HpnicfWIPSMalPktStatInvalidPktLength_Type()
)
hpnicfWIPSMalPktStatInvalidPktLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatInvalidPktLength.setStatus("current")


class _HpnicfWIPSMalPktStatIllegalIBSSESS_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatIllegalIBSSESS based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatIllegalIBSSESS_Object = MibTableColumn
hpnicfWIPSMalPktStatIllegalIBSSESS = _HpnicfWIPSMalPktStatIllegalIBSSESS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 6),
    _HpnicfWIPSMalPktStatIllegalIBSSESS_Type()
)
hpnicfWIPSMalPktStatIllegalIBSSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatIllegalIBSSESS.setStatus("current")


class _HpnicfWIPSMalPktStatInvalidSourceAddr_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatInvalidSourceAddr based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatInvalidSourceAddr_Object = MibTableColumn
hpnicfWIPSMalPktStatInvalidSourceAddr = _HpnicfWIPSMalPktStatInvalidSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 7),
    _HpnicfWIPSMalPktStatInvalidSourceAddr_Type()
)
hpnicfWIPSMalPktStatInvalidSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatInvalidSourceAddr.setStatus("current")


class _HpnicfWIPSMalPktStatOverflowEAPOLKey_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatOverflowEAPOLKey based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatOverflowEAPOLKey_Object = MibTableColumn
hpnicfWIPSMalPktStatOverflowEAPOLKey = _HpnicfWIPSMalPktStatOverflowEAPOLKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 8),
    _HpnicfWIPSMalPktStatOverflowEAPOLKey_Type()
)
hpnicfWIPSMalPktStatOverflowEAPOLKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatOverflowEAPOLKey.setStatus("current")


class _HpnicfWIPSMalPktStatMalAuth_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatMalAuth based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatMalAuth_Object = MibTableColumn
hpnicfWIPSMalPktStatMalAuth = _HpnicfWIPSMalPktStatMalAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 9),
    _HpnicfWIPSMalPktStatMalAuth_Type()
)
hpnicfWIPSMalPktStatMalAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatMalAuth.setStatus("current")


class _HpnicfWIPSMalPktStatMalAssoReq_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatMalAssoReq based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatMalAssoReq_Object = MibTableColumn
hpnicfWIPSMalPktStatMalAssoReq = _HpnicfWIPSMalPktStatMalAssoReq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 10),
    _HpnicfWIPSMalPktStatMalAssoReq_Type()
)
hpnicfWIPSMalPktStatMalAssoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatMalAssoReq.setStatus("current")


class _HpnicfWIPSMalPktStatMalHTIE_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatMalHTIE based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatMalHTIE_Object = MibTableColumn
hpnicfWIPSMalPktStatMalHTIE = _HpnicfWIPSMalPktStatMalHTIE_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 11),
    _HpnicfWIPSMalPktStatMalHTIE_Type()
)
hpnicfWIPSMalPktStatMalHTIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatMalHTIE.setStatus("current")


class _HpnicfWIPSMalPktStatLargeDuration_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatLargeDuration based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatLargeDuration_Object = MibTableColumn
hpnicfWIPSMalPktStatLargeDuration = _HpnicfWIPSMalPktStatLargeDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 12),
    _HpnicfWIPSMalPktStatLargeDuration_Type()
)
hpnicfWIPSMalPktStatLargeDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatLargeDuration.setStatus("current")


class _HpnicfWIPSMalPktStatNULLProbeRes_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatNULLProbeRes based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatNULLProbeRes_Object = MibTableColumn
hpnicfWIPSMalPktStatNULLProbeRes = _HpnicfWIPSMalPktStatNULLProbeRes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 13),
    _HpnicfWIPSMalPktStatNULLProbeRes_Type()
)
hpnicfWIPSMalPktStatNULLProbeRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatNULLProbeRes.setStatus("current")


class _HpnicfWIPSMalPktStatInvalidDeAuthCode_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatInvalidDeAuthCode based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatInvalidDeAuthCode_Object = MibTableColumn
hpnicfWIPSMalPktStatInvalidDeAuthCode = _HpnicfWIPSMalPktStatInvalidDeAuthCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 14),
    _HpnicfWIPSMalPktStatInvalidDeAuthCode_Type()
)
hpnicfWIPSMalPktStatInvalidDeAuthCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatInvalidDeAuthCode.setStatus("current")


class _HpnicfWIPSMalPktStatInvalidDisAssoCode_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatInvalidDisAssoCode based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatInvalidDisAssoCode_Object = MibTableColumn
hpnicfWIPSMalPktStatInvalidDisAssoCode = _HpnicfWIPSMalPktStatInvalidDisAssoCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 15),
    _HpnicfWIPSMalPktStatInvalidDisAssoCode_Type()
)
hpnicfWIPSMalPktStatInvalidDisAssoCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatInvalidDisAssoCode.setStatus("current")


class _HpnicfWIPSMalPktStatOverflowSSID_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatOverflowSSID based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatOverflowSSID_Object = MibTableColumn
hpnicfWIPSMalPktStatOverflowSSID = _HpnicfWIPSMalPktStatOverflowSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 16),
    _HpnicfWIPSMalPktStatOverflowSSID_Type()
)
hpnicfWIPSMalPktStatOverflowSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatOverflowSSID.setStatus("current")


class _HpnicfWIPSMalPktStatFatajack_Type(Counter64):
    """Custom type hpnicfWIPSMalPktStatFatajack based on Counter64"""
    defaultValue = 0


_HpnicfWIPSMalPktStatFatajack_Object = MibTableColumn
hpnicfWIPSMalPktStatFatajack = _HpnicfWIPSMalPktStatFatajack_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 2, 16, 1, 17),
    _HpnicfWIPSMalPktStatFatajack_Type()
)
hpnicfWIPSMalPktStatFatajack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWIPSMalPktStatFatajack.setStatus("current")
_HpnicfWIPSNotifyGroup_ObjectIdentity = ObjectIdentity
hpnicfWIPSNotifyGroup = _HpnicfWIPSNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-WIPS-MIB",
    **{"HpnicfWIPSRadioType": HpnicfWIPSRadioType,
       "HpnicfWIPSDevStatus": HpnicfWIPSDevStatus,
       "HpnicfWIPSDevCategoryWay": HpnicfWIPSDevCategoryWay,
       "HpnicfWIPSDeviceCategoryType": HpnicfWIPSDeviceCategoryType,
       "HpnicfWIPSAPCategoryType": HpnicfWIPSAPCategoryType,
       "HpnicfWIPSClientCategoryType": HpnicfWIPSClientCategoryType,
       "HpnicfWIPSChannel": HpnicfWIPSChannel,
       "HpnicfWIPSEncryptMethod": HpnicfWIPSEncryptMethod,
       "HpnicfWIPSAuthMethod": HpnicfWIPSAuthMethod,
       "HpnicfWIPSAPClassifyType": HpnicfWIPSAPClassifyType,
       "HpnicfWIPSAPSecurityType": HpnicfWIPSAPSecurityType,
       "hpnicfWIPS": hpnicfWIPS,
       "hpnicfWIPSConfigGroup": hpnicfWIPSConfigGroup,
       "hpnicfWIPSGlobalConfigGroup": hpnicfWIPSGlobalConfigGroup,
       "hpnicfWIPSEnable": hpnicfWIPSEnable,
       "hpnicfWIPSSensorLicenseNum": hpnicfWIPSSensorLicenseNum,
       "hpnicfWIPSBlocklistAction": hpnicfWIPSBlocklistAction,
       "hpnicfWIPSAPInactiveTime": hpnicfWIPSAPInactiveTime,
       "hpnicfWIPSSTAInactiveTime": hpnicfWIPSSTAInactiveTime,
       "hpnicfWIPSDevAgingTime": hpnicfWIPSDevAgingTime,
       "hpnicfWIPSStatisticPeriod": hpnicfWIPSStatisticPeriod,
       "hpnicfWIPSReclassificationPeriod": hpnicfWIPSReclassificationPeriod,
       "hpnicfWIPSResetAllTrustList": hpnicfWIPSResetAllTrustList,
       "hpnicfWIPSResetAllBlockList": hpnicfWIPSResetAllBlockList,
       "hpnicfWIPSResetAllIgnoreList": hpnicfWIPSResetAllIgnoreList,
       "hpnicfWIPSResetAllCtmList": hpnicfWIPSResetAllCtmList,
       "hpnicfWIPSPermitChlBitMap": hpnicfWIPSPermitChlBitMap,
       "hpnicfWIPSDynamicTrustListAgingTime": hpnicfWIPSDynamicTrustListAgingTime,
       "hpnicfWIPSDevUpdateTime": hpnicfWIPSDevUpdateTime,
       "hpnicfWIPSADOSEnable": hpnicfWIPSADOSEnable,
       "hpnicfWIPSAccessFlowScanEnable": hpnicfWIPSAccessFlowScanEnable,
       "hpnicfWIPSVsdConfigGroup": hpnicfWIPSVsdConfigGroup,
       "hpnicfWIPSVsdTable": hpnicfWIPSVsdTable,
       "hpnicfWIPSVsdEntry": hpnicfWIPSVsdEntry,
       "hpnicfWIPSVsdNameCfg": hpnicfWIPSVsdNameCfg,
       "hpnicfWIPSVsdRowStatus": hpnicfWIPSVsdRowStatus,
       "hpnicfWIPSVsdAtkDctPolicyNameCfg": hpnicfWIPSVsdAtkDctPolicyNameCfg,
       "hpnicfWIPSVsdCtmPolicyNameCfg": hpnicfWIPSVsdCtmPolicyNameCfg,
       "hpnicfWIPSVsdSigPolicyNameCfg": hpnicfWIPSVsdSigPolicyNameCfg,
       "hpnicfWIPSVsdMalPktPolicyNameCfg": hpnicfWIPSVsdMalPktPolicyNameCfg,
       "hpnicfWIPSRule2VsdTable": hpnicfWIPSRule2VsdTable,
       "hpnicfWIPSRule2VsdEntry": hpnicfWIPSRule2VsdEntry,
       "hpnicfWIPSRule2VsdAPClaRuleNameCfg": hpnicfWIPSRule2VsdAPClaRuleNameCfg,
       "hpnicfWIPSRule2VsdRowStatus": hpnicfWIPSRule2VsdRowStatus,
       "hpnicfWIPSRule2VsdPrecedence": hpnicfWIPSRule2VsdPrecedence,
       "hpnicfWIPSSensor2VsdTable": hpnicfWIPSSensor2VsdTable,
       "hpnicfWIPSSensor2VsdEntry": hpnicfWIPSSensor2VsdEntry,
       "hpnicfWIPSSensorNameCfg": hpnicfWIPSSensorNameCfg,
       "hpnicfWIPSSensor2VsdRowStatus": hpnicfWIPSSensor2VsdRowStatus,
       "hpnicfWIPSSensorState": hpnicfWIPSSensorState,
       "hpnicfWIPSSensorRadioTable": hpnicfWIPSSensorRadioTable,
       "hpnicfWIPSSensorRadioEntry": hpnicfWIPSSensorRadioEntry,
       "hpnicfWIPSSensorRadioRadioId": hpnicfWIPSSensorRadioRadioId,
       "hpnicfWIPSSensorRadioScanMode": hpnicfWIPSSensorRadioScanMode,
       "hpnicfWIPSAPClaRuleTable": hpnicfWIPSAPClaRuleTable,
       "hpnicfWIPSAPClaRuleEntry": hpnicfWIPSAPClaRuleEntry,
       "hpnicfWIPSAPClaRuleName": hpnicfWIPSAPClaRuleName,
       "hpnicfWIPSAPClaRowStatus": hpnicfWIPSAPClaRowStatus,
       "hpnicfWIPSAPClaSeverityLevel": hpnicfWIPSAPClaSeverityLevel,
       "hpnicfWIPSAPClaRuleMatchAll": hpnicfWIPSAPClaRuleMatchAll,
       "hpnicfWIPSAPClaType": hpnicfWIPSAPClaType,
       "hpnicfWIPSAPClaSubRuleSSIDOperator": hpnicfWIPSAPClaSubRuleSSIDOperator,
       "hpnicfWIPSAPClaSubRuleSSIDCase": hpnicfWIPSAPClaSubRuleSSIDCase,
       "hpnicfWIPSAPClaSubRuleSSID": hpnicfWIPSAPClaSubRuleSSID,
       "hpnicfWIPSSecurityType": hpnicfWIPSSecurityType,
       "hpnicfWIPSSecurityTypeMatch": hpnicfWIPSSecurityTypeMatch,
       "hpnicfWIPSAPAuthType": hpnicfWIPSAPAuthType,
       "hpnicfWIPSMaxRSSIValue": hpnicfWIPSMaxRSSIValue,
       "hpnicfWIPSMinRSSIValue": hpnicfWIPSMinRSSIValue,
       "hpnicfWIPSMaxDuration": hpnicfWIPSMaxDuration,
       "hpnicfWIPSMinDuration": hpnicfWIPSMinDuration,
       "hpnicfWIPSMaxAPNum": hpnicfWIPSMaxAPNum,
       "hpnicfWIPSMinAPNum": hpnicfWIPSMinAPNum,
       "hpnicfWIPSMaxClientNum": hpnicfWIPSMaxClientNum,
       "hpnicfWIPSMinClientNum": hpnicfWIPSMinClientNum,
       "hpnicfWIPSOUIInfo": hpnicfWIPSOUIInfo,
       "hpnicfWIPSVendorInfo": hpnicfWIPSVendorInfo,
       "hpnicfWIPSAtkDctPolicyCfgGroup": hpnicfWIPSAtkDctPolicyCfgGroup,
       "hpnicfWIPSAtkDctPolicyCfgSupportSet": hpnicfWIPSAtkDctPolicyCfgSupportSet,
       "hpnicfWIPSAtkDctPolicyCfgTable": hpnicfWIPSAtkDctPolicyCfgTable,
       "hpnicfWIPSAtkDctPolicyCfgEntry": hpnicfWIPSAtkDctPolicyCfgEntry,
       "hpnicfWIPSAtkDctPolicyName": hpnicfWIPSAtkDctPolicyName,
       "hpnicfWIPSAtkDctPolicyCfgRowStatus": hpnicfWIPSAtkDctPolicyCfgRowStatus,
       "hpnicfWIPSAtkDctPolicyBitString": hpnicfWIPSAtkDctPolicyBitString,
       "hpnicfWIPSAtkDctPolicyAPFloodQT": hpnicfWIPSAtkDctPolicyAPFloodQT,
       "hpnicfWIPSAtkDctPolicyAPSpoofQT": hpnicfWIPSAtkDctPolicyAPSpoofQT,
       "hpnicfWIPSAtkDctPolicyCliSpoofQT": hpnicfWIPSAtkDctPolicyCliSpoofQT,
       "hpnicfWIPSAtkDctPolicyDosAssoQT": hpnicfWIPSAtkDctPolicyDosAssoQT,
       "hpnicfWIPSAtkDctPolicyDosAuthQT": hpnicfWIPSAtkDctPolicyDosAuthQT,
       "hpnicfWIPSAtkDctPolicyDosEAPOLStartQT": hpnicfWIPSAtkDctPolicyDosEAPOLStartQT,
       "hpnicfWIPSAtkDctPolicyDosReAssoQT": hpnicfWIPSAtkDctPolicyDosReAssoQT,
       "hpnicfWIPSAtkDctPolicyWeakIVQT": hpnicfWIPSAtkDctPolicyWeakIVQT,
       "hpnicfWIPSAtkDctPolicyInvalidOUIAction": hpnicfWIPSAtkDctPolicyInvalidOUIAction,
       "hpnicfWIPSStaticCtmListCfgTable": hpnicfWIPSStaticCtmListCfgTable,
       "hpnicfWIPSStaticCtmListCfgEntry": hpnicfWIPSStaticCtmListCfgEntry,
       "hpnicfWIPSStaticCtmListMAC": hpnicfWIPSStaticCtmListMAC,
       "hpnicfWIPSStaticCtmListRowStatus": hpnicfWIPSStaticCtmListRowStatus,
       "hpnicfWIPSStaticBlockListCfgTable": hpnicfWIPSStaticBlockListCfgTable,
       "hpnicfWIPSStaticBlockListCfgEntry": hpnicfWIPSStaticBlockListCfgEntry,
       "hpnicfWIPSStaticBlockListMAC": hpnicfWIPSStaticBlockListMAC,
       "hpnicfWIPSStaticBlockListRowStatus": hpnicfWIPSStaticBlockListRowStatus,
       "hpnicfWIPSStaticTrustListCfgTable": hpnicfWIPSStaticTrustListCfgTable,
       "hpnicfWIPSStaticTrustListCfgEntry": hpnicfWIPSStaticTrustListCfgEntry,
       "hpnicfWIPSStaticTrustListMAC": hpnicfWIPSStaticTrustListMAC,
       "hpnicfWIPSStaticTrustListRowStatus": hpnicfWIPSStaticTrustListRowStatus,
       "hpnicfWIPSIgnoreListCfgTable": hpnicfWIPSIgnoreListCfgTable,
       "hpnicfWIPSIgnoreListCfgEntry": hpnicfWIPSIgnoreListCfgEntry,
       "hpnicfWIPSIgnoreListMAC": hpnicfWIPSIgnoreListMAC,
       "hpnicfWIPSIgnoreListRowStatus": hpnicfWIPSIgnoreListRowStatus,
       "hpnicfWIPSDctModeTable": hpnicfWIPSDctModeTable,
       "hpnicfWIPSDctModeEntry": hpnicfWIPSDctModeEntry,
       "hpnicfWIPSDctModeAPName": hpnicfWIPSDctModeAPName,
       "hpnicfWIPSDctModeRadio": hpnicfWIPSDctModeRadio,
       "hpnicfWIPSDctModeScanMode": hpnicfWIPSDctModeScanMode,
       "hpnicfWIPSDctModeRowStatus": hpnicfWIPSDctModeRowStatus,
       "hpnicfWIPSSigConfigGroup": hpnicfWIPSSigConfigGroup,
       "hpnicfWIPSSigPolicyTable": hpnicfWIPSSigPolicyTable,
       "hpnicfWIPSSigPolicyEntry": hpnicfWIPSSigPolicyEntry,
       "hpnicfWIPSSigPolicyNameCfg": hpnicfWIPSSigPolicyNameCfg,
       "hpnicfWIPSSigPolicyRowStatus": hpnicfWIPSSigPolicyRowStatus,
       "hpnicfWIPSSigRule2PolicyTable": hpnicfWIPSSigRule2PolicyTable,
       "hpnicfWIPSSigRule2PolicyEntry": hpnicfWIPSSigRule2PolicyEntry,
       "hpnicfWIPSSigRule2PolicySigRuleIDCfg": hpnicfWIPSSigRule2PolicySigRuleIDCfg,
       "hpnicfWIPSSigRule2PolicyRowStatus": hpnicfWIPSSigRule2PolicyRowStatus,
       "hpnicfWIPSSigRule2PolicyPrecedence": hpnicfWIPSSigRule2PolicyPrecedence,
       "hpnicfWIPSSigRuleTable": hpnicfWIPSSigRuleTable,
       "hpnicfWIPSSigRuleEntry": hpnicfWIPSSigRuleEntry,
       "hpnicfWIPSSigRuleName": hpnicfWIPSSigRuleName,
       "hpnicfWIPSSigRuleID": hpnicfWIPSSigRuleID,
       "hpnicfWIPSSigRuleRowStatus": hpnicfWIPSSigRuleRowStatus,
       "hpnicfWIPSSigSubRuleMatchAll": hpnicfWIPSSigSubRuleMatchAll,
       "hpnicfWIPSSigRuleDctPeriod": hpnicfWIPSSigRuleDctPeriod,
       "hpnicfWIPSSigRuleTrackMethod": hpnicfWIPSSigRuleTrackMethod,
       "hpnicfWIPSSigRuleDctThresholdPerMAC": hpnicfWIPSSigRuleDctThresholdPerMAC,
       "hpnicfWIPSSigRuleDctThresholdPerSig": hpnicfWIPSSigRuleDctThresholdPerSig,
       "hpnicfWIPSSigRuleActionEvtLevel": hpnicfWIPSSigRuleActionEvtLevel,
       "hpnicfWIPSSigRuleQuietTime": hpnicfWIPSSigRuleQuietTime,
       "hpnicfWIPSSigSubRuleFrameType": hpnicfWIPSSigSubRuleFrameType,
       "hpnicfWIPSSigSubRuleFrameSubType": hpnicfWIPSSigSubRuleFrameSubType,
       "hpnicfWIPSSigSubRuleMac": hpnicfWIPSSigSubRuleMac,
       "hpnicfWIPSSigSubRuleMacType": hpnicfWIPSSigSubRuleMacType,
       "hpnicfWIPSSigSubRuleSeqNumMin": hpnicfWIPSSigSubRuleSeqNumMin,
       "hpnicfWIPSSigSubRuleSeqNumMax": hpnicfWIPSSigSubRuleSeqNumMax,
       "hpnicfWIPSSigSubRuleSSIDLenMin": hpnicfWIPSSigSubRuleSSIDLenMin,
       "hpnicfWIPSSigSubRuleSSIDLenMax": hpnicfWIPSSigSubRuleSSIDLenMax,
       "hpnicfWIPSSigSubRuleSSID": hpnicfWIPSSigSubRuleSSID,
       "hpnicfWIPSSigSubRuleSSIDOpe": hpnicfWIPSSigSubRuleSSIDOpe,
       "hpnicfWIPSSigSubRuleSSIDCase": hpnicfWIPSSigSubRuleSSIDCase,
       "hpnicfWIPSSigSubRulePatternTable": hpnicfWIPSSigSubRulePatternTable,
       "hpnicfWIPSSigSubRulePatternEntry": hpnicfWIPSSigSubRulePatternEntry,
       "hpnicfWIPSSigSubRulePatternID": hpnicfWIPSSigSubRulePatternID,
       "hpnicfWIPSSigSubRuleRowStatus": hpnicfWIPSSigSubRuleRowStatus,
       "hpnicfWIPSSigSubRulePatternName": hpnicfWIPSSigSubRulePatternName,
       "hpnicfWIPSSigSubRulePatternOffset": hpnicfWIPSSigSubRulePatternOffset,
       "hpnicfWIPSSigSubRulePatternMask": hpnicfWIPSSigSubRulePatternMask,
       "hpnicfWIPSSigSubRulePatternValueMin": hpnicfWIPSSigSubRulePatternValueMin,
       "hpnicfWIPSSigSubRulePatternValueMax": hpnicfWIPSSigSubRulePatternValueMax,
       "hpnicfWIPSSigSubRulePatternFromPayload": hpnicfWIPSSigSubRulePatternFromPayload,
       "hpnicfWIPSCtmConfigGroup": hpnicfWIPSCtmConfigGroup,
       "hpnicfWIPSCtmPolicyCfgSupportSet": hpnicfWIPSCtmPolicyCfgSupportSet,
       "hpnicfWIPSCtmPolicyTable": hpnicfWIPSCtmPolicyTable,
       "hpnicfWIPSCtmPolicyEntry": hpnicfWIPSCtmPolicyEntry,
       "hpnicfWIPSCtmPolicyName": hpnicfWIPSCtmPolicyName,
       "hpnicfWIPSCtmPolicyCfgRowStatus": hpnicfWIPSCtmPolicyCfgRowStatus,
       "hpnicfWIPSCtmPolicyBitString": hpnicfWIPSCtmPolicyBitString,
       "hpnicfWIPSCtmPolicyFixedChl": hpnicfWIPSCtmPolicyFixedChl,
       "hpnicfWIPSCtmPolicyRogueAPPre": hpnicfWIPSCtmPolicyRogueAPPre,
       "hpnicfWIPSCtmPolicyPtRogueAPPre": hpnicfWIPSCtmPolicyPtRogueAPPre,
       "hpnicfWIPSCtmPolicyMisconfAPPre": hpnicfWIPSCtmPolicyMisconfAPPre,
       "hpnicfWIPSCtmPolicyExternalAPPre": hpnicfWIPSCtmPolicyExternalAPPre,
       "hpnicfWIPSCtmPolicyPtExternalAPPre": hpnicfWIPSCtmPolicyPtExternalAPPre,
       "hpnicfWIPSCtmPolicyUncateAPPre": hpnicfWIPSCtmPolicyUncateAPPre,
       "hpnicfWIPSCtmPolicyPtAuthAPPre": hpnicfWIPSCtmPolicyPtAuthAPPre,
       "hpnicfWIPSCtmPolicyMisassoStaPre": hpnicfWIPSCtmPolicyMisassoStaPre,
       "hpnicfWIPSCtmPolicyUncateStaPre": hpnicfWIPSCtmPolicyUncateStaPre,
       "hpnicfWIPSCtmPolicyUnauthStaPre": hpnicfWIPSCtmPolicyUnauthStaPre,
       "hpnicfWIPSCtmPolicyDevListTable": hpnicfWIPSCtmPolicyDevListTable,
       "hpnicfWIPSCtmPolicyDevListEntry": hpnicfWIPSCtmPolicyDevListEntry,
       "hpnicfWIPSCtmPolicyDevMAC": hpnicfWIPSCtmPolicyDevMAC,
       "hpnicfWIPSCtmPolicyDevRowStatus": hpnicfWIPSCtmPolicyDevRowStatus,
       "hpnicfWIPSMalPktDctConfigGroup": hpnicfWIPSMalPktDctConfigGroup,
       "hpnicfWIPSMalPktDctCfgLogSupportSet": hpnicfWIPSMalPktDctCfgLogSupportSet,
       "hpnicfWIPSMalPktDctCfgTrapSupportSet": hpnicfWIPSMalPktDctCfgTrapSupportSet,
       "hpnicfWIPSMalPktDctPolicyTable": hpnicfWIPSMalPktDctPolicyTable,
       "hpnicfWIPSMalPktDctPolicyEntry": hpnicfWIPSMalPktDctPolicyEntry,
       "hpnicfWIPSMalPktDctPolicyName": hpnicfWIPSMalPktDctPolicyName,
       "hpnicfWIPSMalPktDctPolicyCfgRowStatus": hpnicfWIPSMalPktDctPolicyCfgRowStatus,
       "hpnicfWIPSMalPktDctPolicyLogBitString": hpnicfWIPSMalPktDctPolicyLogBitString,
       "hpnicfWIPSMalPktDctPolicyTrapBitString": hpnicfWIPSMalPktDctPolicyTrapBitString,
       "hpnicfWIPSMalPktDctPolicyDurationThreshold": hpnicfWIPSMalPktDctPolicyDurationThreshold,
       "hpnicfWIPSMalPktDctPolicyQuietTime": hpnicfWIPSMalPktDctPolicyQuietTime,
       "hpnicfWIPSStaticTrustOUIListCfgTable": hpnicfWIPSStaticTrustOUIListCfgTable,
       "hpnicfWIPSStaticTrustOUIListCfgEntry": hpnicfWIPSStaticTrustOUIListCfgEntry,
       "hpnicfWIPSStaticTrustOUIListOUI": hpnicfWIPSStaticTrustOUIListOUI,
       "hpnicfWIPSStaticTrustOUIListRowStatus": hpnicfWIPSStaticTrustOUIListRowStatus,
       "hpnicfWIPSStaticTrustVendorListCfgTable": hpnicfWIPSStaticTrustVendorListCfgTable,
       "hpnicfWIPSStaticTrustVendorListCfgEntry": hpnicfWIPSStaticTrustVendorListCfgEntry,
       "hpnicfWIPSStaticTrustVendorListVendor": hpnicfWIPSStaticTrustVendorListVendor,
       "hpnicfWIPSStaticTrustVendorListRowStatus": hpnicfWIPSStaticTrustVendorListRowStatus,
       "hpnicfWIPSDetectGroup": hpnicfWIPSDetectGroup,
       "hpnicfWIPSDctAPTable": hpnicfWIPSDctAPTable,
       "hpnicfWIPSDctAPEntry": hpnicfWIPSDctAPEntry,
       "hpnicfWIPSDctAPVSD": hpnicfWIPSDctAPVSD,
       "hpnicfWIPSDctAPBSSID": hpnicfWIPSDctAPBSSID,
       "hpnicfWIPSDctAPRunningTime": hpnicfWIPSDctAPRunningTime,
       "hpnicfWIPSDctAPRunTmLastUpdateTm": hpnicfWIPSDctAPRunTmLastUpdateTm,
       "hpnicfWIPSDctAPIsCountered": hpnicfWIPSDctAPIsCountered,
       "hpnicfWIPSDctAPWorkChannel": hpnicfWIPSDctAPWorkChannel,
       "hpnicfWIPSDctAPRadioType": hpnicfWIPSDctAPRadioType,
       "hpnicfWIPSDctAPAuthMethod": hpnicfWIPSDctAPAuthMethod,
       "hpnicfWIPSDctAPEncryptMethod": hpnicfWIPSDctAPEncryptMethod,
       "hpnicfWIPSDctAPSecurity": hpnicfWIPSDctAPSecurity,
       "hpnicfWIPSDctAPSeverityLevel": hpnicfWIPSDctAPSeverityLevel,
       "hpnicfWIPSDctAPLastDctTm": hpnicfWIPSDctAPLastDctTm,
       "hpnicfWIPSDctAPFirstDctTm": hpnicfWIPSDctAPFirstDctTm,
       "hpnicfWIPSDctAPAdd2BlackList": hpnicfWIPSDctAPAdd2BlackList,
       "hpnicfWIPSDctAPAdd2WhiteList": hpnicfWIPSDctAPAdd2WhiteList,
       "hpnicfWIPSDctAPAdd2IgnoreList": hpnicfWIPSDctAPAdd2IgnoreList,
       "hpnicfWIPSDctAPAdd2CtmList": hpnicfWIPSDctAPAdd2CtmList,
       "hpnicfWIPSDctAPCategory": hpnicfWIPSDctAPCategory,
       "hpnicfWIPSDctAPCategoryWay": hpnicfWIPSDctAPCategoryWay,
       "hpnicfWIPSDctAPStatus": hpnicfWIPSDctAPStatus,
       "hpnicfWIPSDctAPSSID": hpnicfWIPSDctAPSSID,
       "hpnicfWIPSDctAPAttachStaNum": hpnicfWIPSDctAPAttachStaNum,
       "hpnicfWIPSDctAPRptSensorNum": hpnicfWIPSDctAPRptSensorNum,
       "hpnicfWIPSDctAPVendor": hpnicfWIPSDctAPVendor,
       "hpnicfWIPSDctAPAttachStaTable": hpnicfWIPSDctAPAttachStaTable,
       "hpnicfWIPSDctAPAttachStaEntry": hpnicfWIPSDctAPAttachStaEntry,
       "hpnicfWIPSDctAPAttachStaMac": hpnicfWIPSDctAPAttachStaMac,
       "hpnicfWIPSDctAPAttachStaRowStatus": hpnicfWIPSDctAPAttachStaRowStatus,
       "hpnicfWIPSDctAPRptSensorTable": hpnicfWIPSDctAPRptSensorTable,
       "hpnicfWIPSDctAPRptSensorEntry": hpnicfWIPSDctAPRptSensorEntry,
       "hpnicfWIPSDctAPRptSensorName": hpnicfWIPSDctAPRptSensorName,
       "hpnicfWIPSDctAPRptSensorRadioId": hpnicfWIPSDctAPRptSensorRadioId,
       "hpnicfWIPSDctAPRptRSSI": hpnicfWIPSDctAPRptRSSI,
       "hpnicfWIPSDctAPLastRptTm": hpnicfWIPSDctAPLastRptTm,
       "hpnicfWIPSDctStaTable": hpnicfWIPSDctStaTable,
       "hpnicfWIPSDctStaEntry": hpnicfWIPSDctStaEntry,
       "hpnicfWIPSDctStaVSD": hpnicfWIPSDctStaVSD,
       "hpnicfWIPSDctStaMac": hpnicfWIPSDctStaMac,
       "hpnicfWIPSDctStaAssocBSSID": hpnicfWIPSDctStaAssocBSSID,
       "hpnicfWIPSDctStaStatus": hpnicfWIPSDctStaStatus,
       "hpnicfWIPSDctStaCategory": hpnicfWIPSDctStaCategory,
       "hpnicfWIPSDctStaRadioType": hpnicfWIPSDctStaRadioType,
       "hpnicfWIPSDctStaWorkChannel": hpnicfWIPSDctStaWorkChannel,
       "hpnicfWIPSDctStaIsCountered": hpnicfWIPSDctStaIsCountered,
       "hpnicfWIPSDctStaAdd2BlackList": hpnicfWIPSDctStaAdd2BlackList,
       "hpnicfWIPSDctStaAdd2WhiteList": hpnicfWIPSDctStaAdd2WhiteList,
       "hpnicfWIPSDctStaAdd2IgnoreList": hpnicfWIPSDctStaAdd2IgnoreList,
       "hpnicfWIPSDctStaAdd2CtmList": hpnicfWIPSDctStaAdd2CtmList,
       "hpnicfWIPSDctStaFirstDctTm": hpnicfWIPSDctStaFirstDctTm,
       "hpnicfWIPSDctStaLastDctTm": hpnicfWIPSDctStaLastDctTm,
       "hpnicfWIPSDctStaRptSensorNum": hpnicfWIPSDctStaRptSensorNum,
       "hpnicfWIPSDctStaState": hpnicfWIPSDctStaState,
       "hpnicfWIPSDctStaVendor": hpnicfWIPSDctStaVendor,
       "hpnicfWIPSDctStaRptSensorTable": hpnicfWIPSDctStaRptSensorTable,
       "hpnicfWIPSDctStaRptSensorEntry": hpnicfWIPSDctStaRptSensorEntry,
       "hpnicfWIPSDctStaRtpSensorName": hpnicfWIPSDctStaRtpSensorName,
       "hpnicfWIPSDctStaRptSensorRadioId": hpnicfWIPSDctStaRptSensorRadioId,
       "hpnicfWIPSDctStaRptRSSI": hpnicfWIPSDctStaRptRSSI,
       "hpnicfWIPSDctStaLastRptTm": hpnicfWIPSDctStaLastRptTm,
       "hpnicfWIPSDctSSIDTable": hpnicfWIPSDctSSIDTable,
       "hpnicfWIPSDctSSIDEntry": hpnicfWIPSDctSSIDEntry,
       "hpnicfWIPSDctNetworkVSD": hpnicfWIPSDctNetworkVSD,
       "hpnicfWIPSDctNetworkSSID": hpnicfWIPSDctNetworkSSID,
       "hpnicfWIPSDctNetworkCfg": hpnicfWIPSDctNetworkCfg,
       "hpnicfWIPSDctNetworkFirstRptTm": hpnicfWIPSDctNetworkFirstRptTm,
       "hpnicfWIPSDctNetworkLastRptTm": hpnicfWIPSDctNetworkLastRptTm,
       "hpnicfWIPSDctNetworkStatus": hpnicfWIPSDctNetworkStatus,
       "hpnicfWIPSDctNetworkSSIDHide": hpnicfWIPSDctNetworkSSIDHide,
       "hpnicfWIPSDctNetworkBSSNum": hpnicfWIPSDctNetworkBSSNum,
       "hpnicfWIPSDctSSIDBSSTable": hpnicfWIPSDctSSIDBSSTable,
       "hpnicfWIPSDctSSIDBSSEntry": hpnicfWIPSDctSSIDBSSEntry,
       "hpnicfWIPSDctNetworkBSSID": hpnicfWIPSDctNetworkBSSID,
       "hpnicfWIPSDctNetworkBSSWorkChl": hpnicfWIPSDctNetworkBSSWorkChl,
       "hpnicfWIPSDctNetworkBSSStaNum": hpnicfWIPSDctNetworkBSSStaNum,
       "hpnicfWIPSBlockListTable": hpnicfWIPSBlockListTable,
       "hpnicfWIPSBlockListEntry": hpnicfWIPSBlockListEntry,
       "hpnicfWIPSBlockListMacAddress": hpnicfWIPSBlockListMacAddress,
       "hpnicfWIPSBlockListStatus": hpnicfWIPSBlockListStatus,
       "hpnicfWIPSChannelTable": hpnicfWIPSChannelTable,
       "hpnicfWIPSChannelEntry": hpnicfWIPSChannelEntry,
       "hpnicfWIPSChannelNum": hpnicfWIPSChannelNum,
       "hpnicfWIPSChannelRadioType": hpnicfWIPSChannelRadioType,
       "hpnicfWIPSChannelIsPermitted": hpnicfWIPSChannelIsPermitted,
       "hpnicfWIPSChannelLastRptTm": hpnicfWIPSChannelLastRptTm,
       "hpnicfWIPSCountermeasureListTable": hpnicfWIPSCountermeasureListTable,
       "hpnicfWIPSCountermeasureListEntry": hpnicfWIPSCountermeasureListEntry,
       "hpnicfWIPSCtmListMacAddress": hpnicfWIPSCtmListMacAddress,
       "hpnicfWIPSCtmListLastestWorkChl": hpnicfWIPSCtmListLastestWorkChl,
       "hpnicfWIPSCtmListFirstTm": hpnicfWIPSCtmListFirstTm,
       "hpnicfWIPSCtmListLastTm": hpnicfWIPSCtmListLastTm,
       "hpnicfWIPSCtmListQurCnt": hpnicfWIPSCtmListQurCnt,
       "hpnicfWIPSCtmListSensorNum": hpnicfWIPSCtmListSensorNum,
       "hpnicfWIPSIgnoreListTable": hpnicfWIPSIgnoreListTable,
       "hpnicfWIPSIgnoreListEntry": hpnicfWIPSIgnoreListEntry,
       "hpnicfWIPSIgnoreListMacAddress": hpnicfWIPSIgnoreListMacAddress,
       "hpnicfWIPSIgnoreListFirstIgnoreTm": hpnicfWIPSIgnoreListFirstIgnoreTm,
       "hpnicfWIPSIgnoreListLastIgnoreTm": hpnicfWIPSIgnoreListLastIgnoreTm,
       "hpnicfWIPSIgnoreListIgnoreCnt": hpnicfWIPSIgnoreListIgnoreCnt,
       "hpnicfWIPSTrustListTable": hpnicfWIPSTrustListTable,
       "hpnicfWIPSTrustListEntry": hpnicfWIPSTrustListEntry,
       "hpnicfWIPSTrustListMacAddress": hpnicfWIPSTrustListMacAddress,
       "hpnicfWIPSTrustListStatus": hpnicfWIPSTrustListStatus,
       "hpnicfWIPSChlStatTable": hpnicfWIPSChlStatTable,
       "hpnicfWIPSChlStatEntry": hpnicfWIPSChlStatEntry,
       "hpnicfWIPSChlStatSensorMacAddr": hpnicfWIPSChlStatSensorMacAddr,
       "hpnicfWIPSChlStatChannel": hpnicfWIPSChlStatChannel,
       "hpnicfWIPSChlStatTotalPkt": hpnicfWIPSChlStatTotalPkt,
       "hpnicfWIPSChlStatTotalByte": hpnicfWIPSChlStatTotalByte,
       "hpnicfWIPSChlStatBmcastPkt": hpnicfWIPSChlStatBmcastPkt,
       "hpnicfWIPSChlStatBmcastByte": hpnicfWIPSChlStatBmcastByte,
       "hpnicfWIPSChlStatUnicastPkt": hpnicfWIPSChlStatUnicastPkt,
       "hpnicfWIPSChlStatUnicastByte": hpnicfWIPSChlStatUnicastByte,
       "hpnicfWIPSChlStatManagement": hpnicfWIPSChlStatManagement,
       "hpnicfWIPSChlStatControl": hpnicfWIPSChlStatControl,
       "hpnicfWIPSChlStatData": hpnicfWIPSChlStatData,
       "hpnicfWIPSChlStatBeacon": hpnicfWIPSChlStatBeacon,
       "hpnicfWIPSChlStatRTS": hpnicfWIPSChlStatRTS,
       "hpnicfWIPSChlStatCTS": hpnicfWIPSChlStatCTS,
       "hpnicfWIPSChlStatProbeRequest": hpnicfWIPSChlStatProbeRequest,
       "hpnicfWIPSChlStatProbeResponse": hpnicfWIPSChlStatProbeResponse,
       "hpnicfWIPSChlStatFragment": hpnicfWIPSChlStatFragment,
       "hpnicfWIPSChlStatRetry": hpnicfWIPSChlStatRetry,
       "hpnicfWIPSChlStatEapSuccess": hpnicfWIPSChlStatEapSuccess,
       "hpnicfWIPSChlStatEapFailure": hpnicfWIPSChlStatEapFailure,
       "hpnicfWIPSChlStatEapolStart": hpnicfWIPSChlStatEapolStart,
       "hpnicfWIPSChlStatEapolLogoff": hpnicfWIPSChlStatEapolLogoff,
       "hpnicfWIPSChlStatAssocRequest": hpnicfWIPSChlStatAssocRequest,
       "hpnicfWIPSChlStatAssocResponse": hpnicfWIPSChlStatAssocResponse,
       "hpnicfWIPSChlStatUnicastDisassoc": hpnicfWIPSChlStatUnicastDisassoc,
       "hpnicfWIPSChlStatBroadcastDisassoc": hpnicfWIPSChlStatBroadcastDisassoc,
       "hpnicfWIPSChlStatAuthentication": hpnicfWIPSChlStatAuthentication,
       "hpnicfWIPSChlStatUnicastDeauthen": hpnicfWIPSChlStatUnicastDeauthen,
       "hpnicfWIPSChlStatBroadcastDeauthen": hpnicfWIPSChlStatBroadcastDeauthen,
       "hpnicfWIPSChlStatMalformed": hpnicfWIPSChlStatMalformed,
       "hpnicfWIPSDevStatTable": hpnicfWIPSDevStatTable,
       "hpnicfWIPSDevStatEntry": hpnicfWIPSDevStatEntry,
       "hpnicfWIPSDevStatSensorMacAddr": hpnicfWIPSDevStatSensorMacAddr,
       "hpnicfWIPSDevStatDevMacAddress": hpnicfWIPSDevStatDevMacAddress,
       "hpnicfWIPSDevStatChannel": hpnicfWIPSDevStatChannel,
       "hpnicfWIPSDevStatTxTotalPkt": hpnicfWIPSDevStatTxTotalPkt,
       "hpnicfWIPSDevStatTxTotalByte": hpnicfWIPSDevStatTxTotalByte,
       "hpnicfWIPSDevStatTxBMcastPkt": hpnicfWIPSDevStatTxBMcastPkt,
       "hpnicfWIPSDevStatTxBMcastByte": hpnicfWIPSDevStatTxBMcastByte,
       "hpnicfWIPSDevStatTxUnicastPkt": hpnicfWIPSDevStatTxUnicastPkt,
       "hpnicfWIPSDevStatTxUnicastByte": hpnicfWIPSDevStatTxUnicastByte,
       "hpnicfWIPSDevStatTxMgmt": hpnicfWIPSDevStatTxMgmt,
       "hpnicfWIPSDevStatTxCtrl": hpnicfWIPSDevStatTxCtrl,
       "hpnicfWIPSDevStatTxData": hpnicfWIPSDevStatTxData,
       "hpnicfWIPSDevStatTxBeacon": hpnicfWIPSDevStatTxBeacon,
       "hpnicfWIPSDevStatTxRTS": hpnicfWIPSDevStatTxRTS,
       "hpnicfWIPSDevStatTxProbeRequest": hpnicfWIPSDevStatTxProbeRequest,
       "hpnicfWIPSDevStatTxProbeResponse": hpnicfWIPSDevStatTxProbeResponse,
       "hpnicfWIPSDevStatTxFragment": hpnicfWIPSDevStatTxFragment,
       "hpnicfWIPSDevStatTxRetry": hpnicfWIPSDevStatTxRetry,
       "hpnicfWIPSDevStatTxAssocRequest": hpnicfWIPSDevStatTxAssocRequest,
       "hpnicfWIPSDevStatTxAssocResponse": hpnicfWIPSDevStatTxAssocResponse,
       "hpnicfWIPSDevStatTxUnicastDisassoc": hpnicfWIPSDevStatTxUnicastDisassoc,
       "hpnicfWIPSDevStatTxBcastDisassoc": hpnicfWIPSDevStatTxBcastDisassoc,
       "hpnicfWIPSDevStatTxAuth": hpnicfWIPSDevStatTxAuth,
       "hpnicfWIPSDevStatTxUnicastDeauth": hpnicfWIPSDevStatTxUnicastDeauth,
       "hpnicfWIPSDevStatTxBcastDeauth": hpnicfWIPSDevStatTxBcastDeauth,
       "hpnicfWIPSDevStatTxEAPSuccess": hpnicfWIPSDevStatTxEAPSuccess,
       "hpnicfWIPSDevStatTxEAPFailure": hpnicfWIPSDevStatTxEAPFailure,
       "hpnicfWIPSDevStatTxEAPOLStart": hpnicfWIPSDevStatTxEAPOLStart,
       "hpnicfWIPSDevStatTxEAPOLLogOff": hpnicfWIPSDevStatTxEAPOLLogOff,
       "hpnicfWIPSDevStatTxMalformed": hpnicfWIPSDevStatTxMalformed,
       "hpnicfWIPSDevStatRxTotalPkt": hpnicfWIPSDevStatRxTotalPkt,
       "hpnicfWIPSDevStatRxTotalByte": hpnicfWIPSDevStatRxTotalByte,
       "hpnicfWIPSDevStatRxUnicastPkt": hpnicfWIPSDevStatRxUnicastPkt,
       "hpnicfWIPSDevStatRxUnicastByte": hpnicfWIPSDevStatRxUnicastByte,
       "hpnicfWIPSDevStatRxMgmt": hpnicfWIPSDevStatRxMgmt,
       "hpnicfWIPSDevStatRxCtrl": hpnicfWIPSDevStatRxCtrl,
       "hpnicfWIPSDevStatRxData": hpnicfWIPSDevStatRxData,
       "hpnicfWIPSDevStatRxRTS": hpnicfWIPSDevStatRxRTS,
       "hpnicfWIPSDevStatRxCTS": hpnicfWIPSDevStatRxCTS,
       "hpnicfWIPSDevStatRxProbeRequest": hpnicfWIPSDevStatRxProbeRequest,
       "hpnicfWIPSDevStatRxProbeResponse": hpnicfWIPSDevStatRxProbeResponse,
       "hpnicfWIPSDevStatRxFragment": hpnicfWIPSDevStatRxFragment,
       "hpnicfWIPSDevStatRxRetry": hpnicfWIPSDevStatRxRetry,
       "hpnicfWIPSDevStatRxAssoRequest": hpnicfWIPSDevStatRxAssoRequest,
       "hpnicfWIPSDevStatRxAssoResponse": hpnicfWIPSDevStatRxAssoResponse,
       "hpnicfWIPSDevStatRxDisassoc": hpnicfWIPSDevStatRxDisassoc,
       "hpnicfWIPSDevStatRxAuth": hpnicfWIPSDevStatRxAuth,
       "hpnicfWIPSDevStatRxDeauth": hpnicfWIPSDevStatRxDeauth,
       "hpnicfWIPSDevStatRxEAPSuccess": hpnicfWIPSDevStatRxEAPSuccess,
       "hpnicfWIPSDevStatRxEAPFailure": hpnicfWIPSDevStatRxEAPFailure,
       "hpnicfWIPSDevStatRxEAPOLStart": hpnicfWIPSDevStatRxEAPOLStart,
       "hpnicfWIPSDevStatRxEAPOLLogoff": hpnicfWIPSDevStatRxEAPOLLogoff,
       "hpnicfWIPSDevStatRxMalformed": hpnicfWIPSDevStatRxMalformed,
       "hpnicfWIPSCtmDeviceTable": hpnicfWIPSCtmDeviceTable,
       "hpnicfWIPSCtmDeviceEntry": hpnicfWIPSCtmDeviceEntry,
       "hpnicfWIPSCtmDeviceVSD": hpnicfWIPSCtmDeviceVSD,
       "hpnicfWIPSCtmDeviceMAC": hpnicfWIPSCtmDeviceMAC,
       "hpnicfWIPSCtmDeviceType": hpnicfWIPSCtmDeviceType,
       "hpnicfWIPSCtmDeviceState": hpnicfWIPSCtmDeviceState,
       "hpnicfWIPSCtmDeviceStartTime": hpnicfWIPSCtmDeviceStartTime,
       "hpnicfWIPSCtmDeviceCategory": hpnicfWIPSCtmDeviceCategory,
       "hpnicfWIPSCtmDeviceChl": hpnicfWIPSCtmDeviceChl,
       "hpnicfWIPSCtmDevicePrecedence": hpnicfWIPSCtmDevicePrecedence,
       "hpnicfWIPSMalPktStatTable": hpnicfWIPSMalPktStatTable,
       "hpnicfWIPSMalPktStatEntry": hpnicfWIPSMalPktStatEntry,
       "hpnicfWIPSMalPktStatSensorMAC": hpnicfWIPSMalPktStatSensorMAC,
       "hpnicfWIPSMalPktStatInvalidIELength": hpnicfWIPSMalPktStatInvalidIELength,
       "hpnicfWIPSMalPktStatDuplicatedIE": hpnicfWIPSMalPktStatDuplicatedIE,
       "hpnicfWIPSMalPktStatRedundantIE": hpnicfWIPSMalPktStatRedundantIE,
       "hpnicfWIPSMalPktStatInvalidPktLength": hpnicfWIPSMalPktStatInvalidPktLength,
       "hpnicfWIPSMalPktStatIllegalIBSSESS": hpnicfWIPSMalPktStatIllegalIBSSESS,
       "hpnicfWIPSMalPktStatInvalidSourceAddr": hpnicfWIPSMalPktStatInvalidSourceAddr,
       "hpnicfWIPSMalPktStatOverflowEAPOLKey": hpnicfWIPSMalPktStatOverflowEAPOLKey,
       "hpnicfWIPSMalPktStatMalAuth": hpnicfWIPSMalPktStatMalAuth,
       "hpnicfWIPSMalPktStatMalAssoReq": hpnicfWIPSMalPktStatMalAssoReq,
       "hpnicfWIPSMalPktStatMalHTIE": hpnicfWIPSMalPktStatMalHTIE,
       "hpnicfWIPSMalPktStatLargeDuration": hpnicfWIPSMalPktStatLargeDuration,
       "hpnicfWIPSMalPktStatNULLProbeRes": hpnicfWIPSMalPktStatNULLProbeRes,
       "hpnicfWIPSMalPktStatInvalidDeAuthCode": hpnicfWIPSMalPktStatInvalidDeAuthCode,
       "hpnicfWIPSMalPktStatInvalidDisAssoCode": hpnicfWIPSMalPktStatInvalidDisAssoCode,
       "hpnicfWIPSMalPktStatOverflowSSID": hpnicfWIPSMalPktStatOverflowSSID,
       "hpnicfWIPSMalPktStatFatajack": hpnicfWIPSMalPktStatFatajack,
       "hpnicfWIPSNotifyGroup": hpnicfWIPSNotifyGroup}
)
