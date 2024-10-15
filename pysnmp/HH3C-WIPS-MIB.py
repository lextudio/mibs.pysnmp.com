# SNMP MIB module (HH3C-WIPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-WIPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:25 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cWIPS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118)
)
hh3cWIPS.setRevisions(
        ("2011-12-29 14:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cWIPSRadioType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class Hh3cWIPSDevStatus(Integer32, TextualConvention):
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



class Hh3cWIPSDevCategoryWay(Integer32, TextualConvention):
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



class Hh3cWIPSDeviceCategoryType(Integer32, TextualConvention):
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



class Hh3cWIPSAPCategoryType(Integer32, TextualConvention):
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



class Hh3cWIPSClientCategoryType(Integer32, TextualConvention):
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
        *(("authorized", 1),
          ("misassociated", 3),
          ("unassociated", 5),
          ("unauthorized", 2),
          ("uncategorized", 4))
    )



class Hh3cWIPSChannel(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 224),
    )



class Hh3cWIPSEncryptMethod(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class Hh3cWIPSAuthMethod(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 3),
          ("dot1xANDother", 7),
          ("none", 1),
          ("other", 4),
          ("psk", 2),
          ("pskANDdot1x", 5),
          ("pskANDdot1xANDother", 8),
          ("pskANDother", 6))
    )



class Hh3cWIPSAPClassifyType(Integer32, TextualConvention):
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



class Hh3cWIPSAPSecurityType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_Hh3cWIPSConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWIPSConfigGroup = _Hh3cWIPSConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1)
)
_Hh3cWIPSGlobalConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWIPSGlobalConfigGroup = _Hh3cWIPSGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1)
)
_Hh3cWIPSEnable_Type = TruthValue
_Hh3cWIPSEnable_Object = MibScalar
hh3cWIPSEnable = _Hh3cWIPSEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 1),
    _Hh3cWIPSEnable_Type()
)
hh3cWIPSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSEnable.setStatus("current")
_Hh3cWIPSSensorLicenseNum_Type = Unsigned32
_Hh3cWIPSSensorLicenseNum_Object = MibScalar
hh3cWIPSSensorLicenseNum = _Hh3cWIPSSensorLicenseNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 2),
    _Hh3cWIPSSensorLicenseNum_Type()
)
hh3cWIPSSensorLicenseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSSensorLicenseNum.setStatus("current")


class _Hh3cWIPSBlocklistAction_Type(Integer32):
    """Custom type hh3cWIPSBlocklistAction based on Integer32"""
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


_Hh3cWIPSBlocklistAction_Type.__name__ = "Integer32"
_Hh3cWIPSBlocklistAction_Object = MibScalar
hh3cWIPSBlocklistAction = _Hh3cWIPSBlocklistAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 3),
    _Hh3cWIPSBlocklistAction_Type()
)
hh3cWIPSBlocklistAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSBlocklistAction.setStatus("current")


class _Hh3cWIPSAPInactiveTime_Type(Integer32):
    """Custom type hh3cWIPSAPInactiveTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_Hh3cWIPSAPInactiveTime_Type.__name__ = "Integer32"
_Hh3cWIPSAPInactiveTime_Object = MibScalar
hh3cWIPSAPInactiveTime = _Hh3cWIPSAPInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 4),
    _Hh3cWIPSAPInactiveTime_Type()
)
hh3cWIPSAPInactiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSAPInactiveTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWIPSAPInactiveTime.setUnits("second")


class _Hh3cWIPSSTAInactiveTime_Type(Integer32):
    """Custom type hh3cWIPSSTAInactiveTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 1200),
    )


_Hh3cWIPSSTAInactiveTime_Type.__name__ = "Integer32"
_Hh3cWIPSSTAInactiveTime_Object = MibScalar
hh3cWIPSSTAInactiveTime = _Hh3cWIPSSTAInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 5),
    _Hh3cWIPSSTAInactiveTime_Type()
)
hh3cWIPSSTAInactiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSSTAInactiveTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWIPSSTAInactiveTime.setUnits("second")


class _Hh3cWIPSDevAgingTime_Type(Integer32):
    """Custom type hh3cWIPSDevAgingTime based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2592000),
    )


_Hh3cWIPSDevAgingTime_Type.__name__ = "Integer32"
_Hh3cWIPSDevAgingTime_Object = MibScalar
hh3cWIPSDevAgingTime = _Hh3cWIPSDevAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 6),
    _Hh3cWIPSDevAgingTime_Type()
)
hh3cWIPSDevAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDevAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWIPSDevAgingTime.setUnits("second")


class _Hh3cWIPSStatisticPeriod_Type(Integer32):
    """Custom type hh3cWIPSStatisticPeriod based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_Hh3cWIPSStatisticPeriod_Type.__name__ = "Integer32"
_Hh3cWIPSStatisticPeriod_Object = MibScalar
hh3cWIPSStatisticPeriod = _Hh3cWIPSStatisticPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 7),
    _Hh3cWIPSStatisticPeriod_Type()
)
hh3cWIPSStatisticPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSStatisticPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWIPSStatisticPeriod.setUnits("second")


class _Hh3cWIPSReclassificationPeriod_Type(Integer32):
    """Custom type hh3cWIPSReclassificationPeriod based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_Hh3cWIPSReclassificationPeriod_Type.__name__ = "Integer32"
_Hh3cWIPSReclassificationPeriod_Object = MibScalar
hh3cWIPSReclassificationPeriod = _Hh3cWIPSReclassificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 8),
    _Hh3cWIPSReclassificationPeriod_Type()
)
hh3cWIPSReclassificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSReclassificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWIPSReclassificationPeriod.setUnits("second")
_Hh3cWIPSResetAllTrustList_Type = TruthValue
_Hh3cWIPSResetAllTrustList_Object = MibScalar
hh3cWIPSResetAllTrustList = _Hh3cWIPSResetAllTrustList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 9),
    _Hh3cWIPSResetAllTrustList_Type()
)
hh3cWIPSResetAllTrustList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSResetAllTrustList.setStatus("current")
_Hh3cWIPSResetAllBlockList_Type = TruthValue
_Hh3cWIPSResetAllBlockList_Object = MibScalar
hh3cWIPSResetAllBlockList = _Hh3cWIPSResetAllBlockList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 10),
    _Hh3cWIPSResetAllBlockList_Type()
)
hh3cWIPSResetAllBlockList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSResetAllBlockList.setStatus("current")
_Hh3cWIPSResetAllIgnoreList_Type = TruthValue
_Hh3cWIPSResetAllIgnoreList_Object = MibScalar
hh3cWIPSResetAllIgnoreList = _Hh3cWIPSResetAllIgnoreList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 11),
    _Hh3cWIPSResetAllIgnoreList_Type()
)
hh3cWIPSResetAllIgnoreList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSResetAllIgnoreList.setStatus("current")
_Hh3cWIPSResetAllCtmList_Type = TruthValue
_Hh3cWIPSResetAllCtmList_Object = MibScalar
hh3cWIPSResetAllCtmList = _Hh3cWIPSResetAllCtmList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 12),
    _Hh3cWIPSResetAllCtmList_Type()
)
hh3cWIPSResetAllCtmList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSResetAllCtmList.setStatus("current")


class _Hh3cWIPSPermitChlBitMap_Type(OctetString):
    """Custom type hh3cWIPSPermitChlBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Hh3cWIPSPermitChlBitMap_Type.__name__ = "OctetString"
_Hh3cWIPSPermitChlBitMap_Object = MibScalar
hh3cWIPSPermitChlBitMap = _Hh3cWIPSPermitChlBitMap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 13),
    _Hh3cWIPSPermitChlBitMap_Type()
)
hh3cWIPSPermitChlBitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSPermitChlBitMap.setStatus("current")


class _Hh3cWIPSDynamicTrustListAgingTime_Type(Integer32):
    """Custom type hh3cWIPSDynamicTrustListAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_Hh3cWIPSDynamicTrustListAgingTime_Type.__name__ = "Integer32"
_Hh3cWIPSDynamicTrustListAgingTime_Object = MibScalar
hh3cWIPSDynamicTrustListAgingTime = _Hh3cWIPSDynamicTrustListAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 14),
    _Hh3cWIPSDynamicTrustListAgingTime_Type()
)
hh3cWIPSDynamicTrustListAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDynamicTrustListAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWIPSDynamicTrustListAgingTime.setUnits("second")


class _Hh3cWIPSDevUpdateTime_Type(Integer32):
    """Custom type hh3cWIPSDevUpdateTime based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_Hh3cWIPSDevUpdateTime_Type.__name__ = "Integer32"
_Hh3cWIPSDevUpdateTime_Object = MibScalar
hh3cWIPSDevUpdateTime = _Hh3cWIPSDevUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 15),
    _Hh3cWIPSDevUpdateTime_Type()
)
hh3cWIPSDevUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDevUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWIPSDevUpdateTime.setUnits("second")


class _Hh3cWIPSADOSEnable_Type(TruthValue):
    """Custom type hh3cWIPSADOSEnable based on TruthValue"""


_Hh3cWIPSADOSEnable_Object = MibScalar
hh3cWIPSADOSEnable = _Hh3cWIPSADOSEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 16),
    _Hh3cWIPSADOSEnable_Type()
)
hh3cWIPSADOSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSADOSEnable.setStatus("current")


class _Hh3cWIPSAccessFlowScanEnable_Type(TruthValue):
    """Custom type hh3cWIPSAccessFlowScanEnable based on TruthValue"""


_Hh3cWIPSAccessFlowScanEnable_Object = MibScalar
hh3cWIPSAccessFlowScanEnable = _Hh3cWIPSAccessFlowScanEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 1, 17),
    _Hh3cWIPSAccessFlowScanEnable_Type()
)
hh3cWIPSAccessFlowScanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSAccessFlowScanEnable.setStatus("current")
_Hh3cWIPSVsdConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWIPSVsdConfigGroup = _Hh3cWIPSVsdConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2)
)
_Hh3cWIPSVsdTable_Object = MibTable
hh3cWIPSVsdTable = _Hh3cWIPSVsdTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cWIPSVsdTable.setStatus("current")
_Hh3cWIPSVsdEntry_Object = MibTableRow
hh3cWIPSVsdEntry = _Hh3cWIPSVsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 1, 1)
)
hh3cWIPSVsdEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSVsdNameCfg"),
)
if mibBuilder.loadTexts:
    hh3cWIPSVsdEntry.setStatus("current")


class _Hh3cWIPSVsdNameCfg_Type(OctetString):
    """Custom type hh3cWIPSVsdNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSVsdNameCfg_Type.__name__ = "OctetString"
_Hh3cWIPSVsdNameCfg_Object = MibTableColumn
hh3cWIPSVsdNameCfg = _Hh3cWIPSVsdNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 1, 1, 1),
    _Hh3cWIPSVsdNameCfg_Type()
)
hh3cWIPSVsdNameCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSVsdNameCfg.setStatus("current")
_Hh3cWIPSVsdRowStatus_Type = RowStatus
_Hh3cWIPSVsdRowStatus_Object = MibTableColumn
hh3cWIPSVsdRowStatus = _Hh3cWIPSVsdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 1, 1, 2),
    _Hh3cWIPSVsdRowStatus_Type()
)
hh3cWIPSVsdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSVsdRowStatus.setStatus("current")


class _Hh3cWIPSVsdAtkDctPolicyNameCfg_Type(OctetString):
    """Custom type hh3cWIPSVsdAtkDctPolicyNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cWIPSVsdAtkDctPolicyNameCfg_Type.__name__ = "OctetString"
_Hh3cWIPSVsdAtkDctPolicyNameCfg_Object = MibTableColumn
hh3cWIPSVsdAtkDctPolicyNameCfg = _Hh3cWIPSVsdAtkDctPolicyNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 1, 1, 3),
    _Hh3cWIPSVsdAtkDctPolicyNameCfg_Type()
)
hh3cWIPSVsdAtkDctPolicyNameCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSVsdAtkDctPolicyNameCfg.setStatus("current")


class _Hh3cWIPSVsdCtmPolicyNameCfg_Type(OctetString):
    """Custom type hh3cWIPSVsdCtmPolicyNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cWIPSVsdCtmPolicyNameCfg_Type.__name__ = "OctetString"
_Hh3cWIPSVsdCtmPolicyNameCfg_Object = MibTableColumn
hh3cWIPSVsdCtmPolicyNameCfg = _Hh3cWIPSVsdCtmPolicyNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 1, 1, 4),
    _Hh3cWIPSVsdCtmPolicyNameCfg_Type()
)
hh3cWIPSVsdCtmPolicyNameCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSVsdCtmPolicyNameCfg.setStatus("current")


class _Hh3cWIPSVsdSigPolicyNameCfg_Type(OctetString):
    """Custom type hh3cWIPSVsdSigPolicyNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cWIPSVsdSigPolicyNameCfg_Type.__name__ = "OctetString"
_Hh3cWIPSVsdSigPolicyNameCfg_Object = MibTableColumn
hh3cWIPSVsdSigPolicyNameCfg = _Hh3cWIPSVsdSigPolicyNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 1, 1, 5),
    _Hh3cWIPSVsdSigPolicyNameCfg_Type()
)
hh3cWIPSVsdSigPolicyNameCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSVsdSigPolicyNameCfg.setStatus("current")


class _Hh3cWIPSVsdMalPktPolicyNameCfg_Type(OctetString):
    """Custom type hh3cWIPSVsdMalPktPolicyNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cWIPSVsdMalPktPolicyNameCfg_Type.__name__ = "OctetString"
_Hh3cWIPSVsdMalPktPolicyNameCfg_Object = MibTableColumn
hh3cWIPSVsdMalPktPolicyNameCfg = _Hh3cWIPSVsdMalPktPolicyNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 1, 1, 6),
    _Hh3cWIPSVsdMalPktPolicyNameCfg_Type()
)
hh3cWIPSVsdMalPktPolicyNameCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSVsdMalPktPolicyNameCfg.setStatus("current")
_Hh3cWIPSRule2VsdTable_Object = MibTable
hh3cWIPSRule2VsdTable = _Hh3cWIPSRule2VsdTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cWIPSRule2VsdTable.setStatus("current")
_Hh3cWIPSRule2VsdEntry_Object = MibTableRow
hh3cWIPSRule2VsdEntry = _Hh3cWIPSRule2VsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 2, 1)
)
hh3cWIPSRule2VsdEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSVsdNameCfg"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSRule2VsdAPClaRuleNameCfg"),
)
if mibBuilder.loadTexts:
    hh3cWIPSRule2VsdEntry.setStatus("current")


class _Hh3cWIPSRule2VsdAPClaRuleNameCfg_Type(OctetString):
    """Custom type hh3cWIPSRule2VsdAPClaRuleNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSRule2VsdAPClaRuleNameCfg_Type.__name__ = "OctetString"
_Hh3cWIPSRule2VsdAPClaRuleNameCfg_Object = MibTableColumn
hh3cWIPSRule2VsdAPClaRuleNameCfg = _Hh3cWIPSRule2VsdAPClaRuleNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 2, 1, 1),
    _Hh3cWIPSRule2VsdAPClaRuleNameCfg_Type()
)
hh3cWIPSRule2VsdAPClaRuleNameCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSRule2VsdAPClaRuleNameCfg.setStatus("current")
_Hh3cWIPSRule2VsdRowStatus_Type = RowStatus
_Hh3cWIPSRule2VsdRowStatus_Object = MibTableColumn
hh3cWIPSRule2VsdRowStatus = _Hh3cWIPSRule2VsdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 2, 1, 2),
    _Hh3cWIPSRule2VsdRowStatus_Type()
)
hh3cWIPSRule2VsdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSRule2VsdRowStatus.setStatus("current")


class _Hh3cWIPSRule2VsdPrecedence_Type(Integer32):
    """Custom type hh3cWIPSRule2VsdPrecedence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cWIPSRule2VsdPrecedence_Type.__name__ = "Integer32"
_Hh3cWIPSRule2VsdPrecedence_Object = MibTableColumn
hh3cWIPSRule2VsdPrecedence = _Hh3cWIPSRule2VsdPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 2, 1, 3),
    _Hh3cWIPSRule2VsdPrecedence_Type()
)
hh3cWIPSRule2VsdPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSRule2VsdPrecedence.setStatus("current")
_Hh3cWIPSSensor2VsdTable_Object = MibTable
hh3cWIPSSensor2VsdTable = _Hh3cWIPSSensor2VsdTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cWIPSSensor2VsdTable.setStatus("current")
_Hh3cWIPSSensor2VsdEntry_Object = MibTableRow
hh3cWIPSSensor2VsdEntry = _Hh3cWIPSSensor2VsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 3, 1)
)
hh3cWIPSSensor2VsdEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSVsdNameCfg"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSSensorNameCfg"),
)
if mibBuilder.loadTexts:
    hh3cWIPSSensor2VsdEntry.setStatus("current")


class _Hh3cWIPSSensorNameCfg_Type(OctetString):
    """Custom type hh3cWIPSSensorNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cWIPSSensorNameCfg_Type.__name__ = "OctetString"
_Hh3cWIPSSensorNameCfg_Object = MibTableColumn
hh3cWIPSSensorNameCfg = _Hh3cWIPSSensorNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 3, 1, 1),
    _Hh3cWIPSSensorNameCfg_Type()
)
hh3cWIPSSensorNameCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSSensorNameCfg.setStatus("current")
_Hh3cWIPSSensor2VsdRowStatus_Type = RowStatus
_Hh3cWIPSSensor2VsdRowStatus_Object = MibTableColumn
hh3cWIPSSensor2VsdRowStatus = _Hh3cWIPSSensor2VsdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 3, 1, 2),
    _Hh3cWIPSSensor2VsdRowStatus_Type()
)
hh3cWIPSSensor2VsdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSensor2VsdRowStatus.setStatus("current")


class _Hh3cWIPSSensorState_Type(Integer32):
    """Custom type hh3cWIPSSensorState based on Integer32"""
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


_Hh3cWIPSSensorState_Type.__name__ = "Integer32"
_Hh3cWIPSSensorState_Object = MibTableColumn
hh3cWIPSSensorState = _Hh3cWIPSSensorState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 3, 1, 3),
    _Hh3cWIPSSensorState_Type()
)
hh3cWIPSSensorState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSensorState.setStatus("current")
_Hh3cWIPSSensorRadioTable_Object = MibTable
hh3cWIPSSensorRadioTable = _Hh3cWIPSSensorRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cWIPSSensorRadioTable.setStatus("current")
_Hh3cWIPSSensorRadioEntry_Object = MibTableRow
hh3cWIPSSensorRadioEntry = _Hh3cWIPSSensorRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 4, 1)
)
hh3cWIPSSensorRadioEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSVsdNameCfg"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSSensorNameCfg"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSSensorRadioRadioId"),
)
if mibBuilder.loadTexts:
    hh3cWIPSSensorRadioEntry.setStatus("current")


class _Hh3cWIPSSensorRadioRadioId_Type(Integer32):
    """Custom type hh3cWIPSSensorRadioRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cWIPSSensorRadioRadioId_Type.__name__ = "Integer32"
_Hh3cWIPSSensorRadioRadioId_Object = MibTableColumn
hh3cWIPSSensorRadioRadioId = _Hh3cWIPSSensorRadioRadioId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 4, 1, 1),
    _Hh3cWIPSSensorRadioRadioId_Type()
)
hh3cWIPSSensorRadioRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSSensorRadioRadioId.setStatus("current")


class _Hh3cWIPSSensorRadioScanMode_Type(Integer32):
    """Custom type hh3cWIPSSensorRadioScanMode based on Integer32"""
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


_Hh3cWIPSSensorRadioScanMode_Type.__name__ = "Integer32"
_Hh3cWIPSSensorRadioScanMode_Object = MibTableColumn
hh3cWIPSSensorRadioScanMode = _Hh3cWIPSSensorRadioScanMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 2, 4, 1, 2),
    _Hh3cWIPSSensorRadioScanMode_Type()
)
hh3cWIPSSensorRadioScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSSensorRadioScanMode.setStatus("current")
_Hh3cWIPSAPClaRuleTable_Object = MibTable
hh3cWIPSAPClaRuleTable = _Hh3cWIPSAPClaRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cWIPSAPClaRuleTable.setStatus("current")
_Hh3cWIPSAPClaRuleEntry_Object = MibTableRow
hh3cWIPSAPClaRuleEntry = _Hh3cWIPSAPClaRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1)
)
hh3cWIPSAPClaRuleEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSAPClaRuleName"),
)
if mibBuilder.loadTexts:
    hh3cWIPSAPClaRuleEntry.setStatus("current")


class _Hh3cWIPSAPClaRuleName_Type(OctetString):
    """Custom type hh3cWIPSAPClaRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSAPClaRuleName_Type.__name__ = "OctetString"
_Hh3cWIPSAPClaRuleName_Object = MibTableColumn
hh3cWIPSAPClaRuleName = _Hh3cWIPSAPClaRuleName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 1),
    _Hh3cWIPSAPClaRuleName_Type()
)
hh3cWIPSAPClaRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSAPClaRuleName.setStatus("current")
_Hh3cWIPSAPClaRowStatus_Type = RowStatus
_Hh3cWIPSAPClaRowStatus_Object = MibTableColumn
hh3cWIPSAPClaRowStatus = _Hh3cWIPSAPClaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 2),
    _Hh3cWIPSAPClaRowStatus_Type()
)
hh3cWIPSAPClaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAPClaRowStatus.setStatus("current")


class _Hh3cWIPSAPClaSeverityLevel_Type(Unsigned32):
    """Custom type hh3cWIPSAPClaSeverityLevel based on Unsigned32"""
    defaultHexValue = 4294967295


_Hh3cWIPSAPClaSeverityLevel_Object = MibTableColumn
hh3cWIPSAPClaSeverityLevel = _Hh3cWIPSAPClaSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 3),
    _Hh3cWIPSAPClaSeverityLevel_Type()
)
hh3cWIPSAPClaSeverityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAPClaSeverityLevel.setStatus("current")


class _Hh3cWIPSAPClaRuleMatchAll_Type(TruthValue):
    """Custom type hh3cWIPSAPClaRuleMatchAll based on TruthValue"""


_Hh3cWIPSAPClaRuleMatchAll_Object = MibTableColumn
hh3cWIPSAPClaRuleMatchAll = _Hh3cWIPSAPClaRuleMatchAll_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 4),
    _Hh3cWIPSAPClaRuleMatchAll_Type()
)
hh3cWIPSAPClaRuleMatchAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAPClaRuleMatchAll.setStatus("current")
_Hh3cWIPSAPClaType_Type = Hh3cWIPSAPClassifyType
_Hh3cWIPSAPClaType_Object = MibTableColumn
hh3cWIPSAPClaType = _Hh3cWIPSAPClaType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 5),
    _Hh3cWIPSAPClaType_Type()
)
hh3cWIPSAPClaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAPClaType.setStatus("current")


class _Hh3cWIPSAPClaSubRuleSSIDOperator_Type(Integer32):
    """Custom type hh3cWIPSAPClaSubRuleSSIDOperator based on Integer32"""
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


_Hh3cWIPSAPClaSubRuleSSIDOperator_Type.__name__ = "Integer32"
_Hh3cWIPSAPClaSubRuleSSIDOperator_Object = MibTableColumn
hh3cWIPSAPClaSubRuleSSIDOperator = _Hh3cWIPSAPClaSubRuleSSIDOperator_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 6),
    _Hh3cWIPSAPClaSubRuleSSIDOperator_Type()
)
hh3cWIPSAPClaSubRuleSSIDOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAPClaSubRuleSSIDOperator.setStatus("current")


class _Hh3cWIPSAPClaSubRuleSSIDCase_Type(TruthValue):
    """Custom type hh3cWIPSAPClaSubRuleSSIDCase based on TruthValue"""


_Hh3cWIPSAPClaSubRuleSSIDCase_Object = MibTableColumn
hh3cWIPSAPClaSubRuleSSIDCase = _Hh3cWIPSAPClaSubRuleSSIDCase_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 7),
    _Hh3cWIPSAPClaSubRuleSSIDCase_Type()
)
hh3cWIPSAPClaSubRuleSSIDCase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAPClaSubRuleSSIDCase.setStatus("current")


class _Hh3cWIPSAPClaSubRuleSSID_Type(OctetString):
    """Custom type hh3cWIPSAPClaSubRuleSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cWIPSAPClaSubRuleSSID_Type.__name__ = "OctetString"
_Hh3cWIPSAPClaSubRuleSSID_Object = MibTableColumn
hh3cWIPSAPClaSubRuleSSID = _Hh3cWIPSAPClaSubRuleSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 8),
    _Hh3cWIPSAPClaSubRuleSSID_Type()
)
hh3cWIPSAPClaSubRuleSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAPClaSubRuleSSID.setStatus("current")


class _Hh3cWIPSSecurityType_Type(Hh3cWIPSAPSecurityType):
    """Custom type hh3cWIPSSecurityType based on Hh3cWIPSAPSecurityType"""
    defaultHexValue = 4294967295


_Hh3cWIPSSecurityType_Object = MibTableColumn
hh3cWIPSSecurityType = _Hh3cWIPSSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 9),
    _Hh3cWIPSSecurityType_Type()
)
hh3cWIPSSecurityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSecurityType.setStatus("current")


class _Hh3cWIPSSecurityTypeMatch_Type(Integer32):
    """Custom type hh3cWIPSSecurityTypeMatch based on Integer32"""
    defaultValue = 2

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


_Hh3cWIPSSecurityTypeMatch_Type.__name__ = "Integer32"
_Hh3cWIPSSecurityTypeMatch_Object = MibTableColumn
hh3cWIPSSecurityTypeMatch = _Hh3cWIPSSecurityTypeMatch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 10),
    _Hh3cWIPSSecurityTypeMatch_Type()
)
hh3cWIPSSecurityTypeMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSecurityTypeMatch.setStatus("current")


class _Hh3cWIPSAPAuthType_Type(Integer32):
    """Custom type hh3cWIPSAPAuthType based on Integer32"""
    defaultValue = 5

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
        *(("dot1x", 3),
          ("dot1xANDother", 8),
          ("none", 1),
          ("noneANDdot1x", 11),
          ("noneANDdot1xANDother", 15),
          ("noneANDother", 12),
          ("noneANDpsk", 10),
          ("noneANDpskANDdot1x", 13),
          ("noneANDpskANDdot1xANDother", 16),
          ("noneANDpskANDother", 14),
          ("other", 4),
          ("psk", 2),
          ("pskANDdot1x", 6),
          ("pskANDdot1xANDother", 9),
          ("pskANDother", 7),
          ("undo", 5))
    )


_Hh3cWIPSAPAuthType_Type.__name__ = "Integer32"
_Hh3cWIPSAPAuthType_Object = MibTableColumn
hh3cWIPSAPAuthType = _Hh3cWIPSAPAuthType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 11),
    _Hh3cWIPSAPAuthType_Type()
)
hh3cWIPSAPAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAPAuthType.setStatus("current")


class _Hh3cWIPSMaxRSSIValue_Type(Unsigned32):
    """Custom type hh3cWIPSMaxRSSIValue based on Unsigned32"""
    defaultHexValue = 4294967295


_Hh3cWIPSMaxRSSIValue_Object = MibTableColumn
hh3cWIPSMaxRSSIValue = _Hh3cWIPSMaxRSSIValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 12),
    _Hh3cWIPSMaxRSSIValue_Type()
)
hh3cWIPSMaxRSSIValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMaxRSSIValue.setStatus("current")


class _Hh3cWIPSMinRSSIValue_Type(Unsigned32):
    """Custom type hh3cWIPSMinRSSIValue based on Unsigned32"""
    defaultHexValue = 4294967295


_Hh3cWIPSMinRSSIValue_Object = MibTableColumn
hh3cWIPSMinRSSIValue = _Hh3cWIPSMinRSSIValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 13),
    _Hh3cWIPSMinRSSIValue_Type()
)
hh3cWIPSMinRSSIValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMinRSSIValue.setStatus("current")


class _Hh3cWIPSMaxDuration_Type(Unsigned32):
    """Custom type hh3cWIPSMaxDuration based on Unsigned32"""
    defaultHexValue = 4294967295


_Hh3cWIPSMaxDuration_Object = MibTableColumn
hh3cWIPSMaxDuration = _Hh3cWIPSMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 14),
    _Hh3cWIPSMaxDuration_Type()
)
hh3cWIPSMaxDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWIPSMaxDuration.setUnits("second")


class _Hh3cWIPSMinDuration_Type(Unsigned32):
    """Custom type hh3cWIPSMinDuration based on Unsigned32"""
    defaultHexValue = 4294967295


_Hh3cWIPSMinDuration_Object = MibTableColumn
hh3cWIPSMinDuration = _Hh3cWIPSMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 15),
    _Hh3cWIPSMinDuration_Type()
)
hh3cWIPSMinDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMinDuration.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWIPSMinDuration.setUnits("second")


class _Hh3cWIPSMaxAPNum_Type(Unsigned32):
    """Custom type hh3cWIPSMaxAPNum based on Unsigned32"""
    defaultHexValue = 4294967295


_Hh3cWIPSMaxAPNum_Object = MibTableColumn
hh3cWIPSMaxAPNum = _Hh3cWIPSMaxAPNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 16),
    _Hh3cWIPSMaxAPNum_Type()
)
hh3cWIPSMaxAPNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMaxAPNum.setStatus("current")


class _Hh3cWIPSMinAPNum_Type(Unsigned32):
    """Custom type hh3cWIPSMinAPNum based on Unsigned32"""
    defaultHexValue = 4294967295


_Hh3cWIPSMinAPNum_Object = MibTableColumn
hh3cWIPSMinAPNum = _Hh3cWIPSMinAPNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 17),
    _Hh3cWIPSMinAPNum_Type()
)
hh3cWIPSMinAPNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMinAPNum.setStatus("current")


class _Hh3cWIPSMaxClientNum_Type(Unsigned32):
    """Custom type hh3cWIPSMaxClientNum based on Unsigned32"""
    defaultHexValue = 4294967295


_Hh3cWIPSMaxClientNum_Object = MibTableColumn
hh3cWIPSMaxClientNum = _Hh3cWIPSMaxClientNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 18),
    _Hh3cWIPSMaxClientNum_Type()
)
hh3cWIPSMaxClientNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMaxClientNum.setStatus("current")


class _Hh3cWIPSMinClientNum_Type(Unsigned32):
    """Custom type hh3cWIPSMinClientNum based on Unsigned32"""
    defaultHexValue = 4294967295


_Hh3cWIPSMinClientNum_Object = MibTableColumn
hh3cWIPSMinClientNum = _Hh3cWIPSMinClientNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 19),
    _Hh3cWIPSMinClientNum_Type()
)
hh3cWIPSMinClientNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMinClientNum.setStatus("current")


class _Hh3cWIPSOUIInfo_Type(OctetString):
    """Custom type hh3cWIPSOUIInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Hh3cWIPSOUIInfo_Type.__name__ = "OctetString"
_Hh3cWIPSOUIInfo_Object = MibTableColumn
hh3cWIPSOUIInfo = _Hh3cWIPSOUIInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 20),
    _Hh3cWIPSOUIInfo_Type()
)
hh3cWIPSOUIInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSOUIInfo.setStatus("current")


class _Hh3cWIPSVendorInfo_Type(OctetString):
    """Custom type hh3cWIPSVendorInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cWIPSVendorInfo_Type.__name__ = "OctetString"
_Hh3cWIPSVendorInfo_Object = MibTableColumn
hh3cWIPSVendorInfo = _Hh3cWIPSVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 21),
    _Hh3cWIPSVendorInfo_Type()
)
hh3cWIPSVendorInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSVendorInfo.setStatus("current")


class _Hh3cWIPSAPAuthTypeMatch_Type(Integer32):
    """Custom type hh3cWIPSAPAuthTypeMatch based on Integer32"""
    defaultValue = 2

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


_Hh3cWIPSAPAuthTypeMatch_Type.__name__ = "Integer32"
_Hh3cWIPSAPAuthTypeMatch_Object = MibTableColumn
hh3cWIPSAPAuthTypeMatch = _Hh3cWIPSAPAuthTypeMatch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 3, 1, 22),
    _Hh3cWIPSAPAuthTypeMatch_Type()
)
hh3cWIPSAPAuthTypeMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAPAuthTypeMatch.setStatus("current")
_Hh3cWIPSAtkDctPolicyCfgGroup_ObjectIdentity = ObjectIdentity
hh3cWIPSAtkDctPolicyCfgGroup = _Hh3cWIPSAtkDctPolicyCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4)
)


class _Hh3cWIPSAtkDctPolicyCfgSupportSet_Type(OctetString):
    """Custom type hh3cWIPSAtkDctPolicyCfgSupportSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Hh3cWIPSAtkDctPolicyCfgSupportSet_Type.__name__ = "OctetString"
_Hh3cWIPSAtkDctPolicyCfgSupportSet_Object = MibScalar
hh3cWIPSAtkDctPolicyCfgSupportSet = _Hh3cWIPSAtkDctPolicyCfgSupportSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 1),
    _Hh3cWIPSAtkDctPolicyCfgSupportSet_Type()
)
hh3cWIPSAtkDctPolicyCfgSupportSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyCfgSupportSet.setStatus("current")
_Hh3cWIPSAtkDctPolicyCfgTable_Object = MibTable
hh3cWIPSAtkDctPolicyCfgTable = _Hh3cWIPSAtkDctPolicyCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyCfgTable.setStatus("current")
_Hh3cWIPSAtkDctPolicyCfgEntry_Object = MibTableRow
hh3cWIPSAtkDctPolicyCfgEntry = _Hh3cWIPSAtkDctPolicyCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1)
)
hh3cWIPSAtkDctPolicyCfgEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSAtkDctPolicyName"),
)
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyCfgEntry.setStatus("current")


class _Hh3cWIPSAtkDctPolicyName_Type(OctetString):
    """Custom type hh3cWIPSAtkDctPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSAtkDctPolicyName_Type.__name__ = "OctetString"
_Hh3cWIPSAtkDctPolicyName_Object = MibTableColumn
hh3cWIPSAtkDctPolicyName = _Hh3cWIPSAtkDctPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 1),
    _Hh3cWIPSAtkDctPolicyName_Type()
)
hh3cWIPSAtkDctPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyName.setStatus("current")
_Hh3cWIPSAtkDctPolicyCfgRowStatus_Type = RowStatus
_Hh3cWIPSAtkDctPolicyCfgRowStatus_Object = MibTableColumn
hh3cWIPSAtkDctPolicyCfgRowStatus = _Hh3cWIPSAtkDctPolicyCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 2),
    _Hh3cWIPSAtkDctPolicyCfgRowStatus_Type()
)
hh3cWIPSAtkDctPolicyCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyCfgRowStatus.setStatus("current")


class _Hh3cWIPSAtkDctPolicyBitString_Type(OctetString):
    """Custom type hh3cWIPSAtkDctPolicyBitString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Hh3cWIPSAtkDctPolicyBitString_Type.__name__ = "OctetString"
_Hh3cWIPSAtkDctPolicyBitString_Object = MibTableColumn
hh3cWIPSAtkDctPolicyBitString = _Hh3cWIPSAtkDctPolicyBitString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 3),
    _Hh3cWIPSAtkDctPolicyBitString_Type()
)
hh3cWIPSAtkDctPolicyBitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyBitString.setStatus("current")


class _Hh3cWIPSAtkDctPolicyAPFloodQT_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyAPFloodQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSAtkDctPolicyAPFloodQT_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyAPFloodQT_Object = MibTableColumn
hh3cWIPSAtkDctPolicyAPFloodQT = _Hh3cWIPSAtkDctPolicyAPFloodQT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 4),
    _Hh3cWIPSAtkDctPolicyAPFloodQT_Type()
)
hh3cWIPSAtkDctPolicyAPFloodQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyAPFloodQT.setStatus("current")


class _Hh3cWIPSAtkDctPolicyAPSpoofQT_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyAPSpoofQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSAtkDctPolicyAPSpoofQT_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyAPSpoofQT_Object = MibTableColumn
hh3cWIPSAtkDctPolicyAPSpoofQT = _Hh3cWIPSAtkDctPolicyAPSpoofQT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 5),
    _Hh3cWIPSAtkDctPolicyAPSpoofQT_Type()
)
hh3cWIPSAtkDctPolicyAPSpoofQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyAPSpoofQT.setStatus("current")


class _Hh3cWIPSAtkDctPolicyCliSpoofQT_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyCliSpoofQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSAtkDctPolicyCliSpoofQT_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyCliSpoofQT_Object = MibTableColumn
hh3cWIPSAtkDctPolicyCliSpoofQT = _Hh3cWIPSAtkDctPolicyCliSpoofQT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 6),
    _Hh3cWIPSAtkDctPolicyCliSpoofQT_Type()
)
hh3cWIPSAtkDctPolicyCliSpoofQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyCliSpoofQT.setStatus("current")


class _Hh3cWIPSAtkDctPolicyDosAssoQT_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyDosAssoQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSAtkDctPolicyDosAssoQT_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyDosAssoQT_Object = MibTableColumn
hh3cWIPSAtkDctPolicyDosAssoQT = _Hh3cWIPSAtkDctPolicyDosAssoQT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 7),
    _Hh3cWIPSAtkDctPolicyDosAssoQT_Type()
)
hh3cWIPSAtkDctPolicyDosAssoQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyDosAssoQT.setStatus("current")


class _Hh3cWIPSAtkDctPolicyDosAuthQT_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyDosAuthQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSAtkDctPolicyDosAuthQT_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyDosAuthQT_Object = MibTableColumn
hh3cWIPSAtkDctPolicyDosAuthQT = _Hh3cWIPSAtkDctPolicyDosAuthQT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 8),
    _Hh3cWIPSAtkDctPolicyDosAuthQT_Type()
)
hh3cWIPSAtkDctPolicyDosAuthQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyDosAuthQT.setStatus("current")


class _Hh3cWIPSAtkDctPolicyDosEAPOLStartQT_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyDosEAPOLStartQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSAtkDctPolicyDosEAPOLStartQT_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyDosEAPOLStartQT_Object = MibTableColumn
hh3cWIPSAtkDctPolicyDosEAPOLStartQT = _Hh3cWIPSAtkDctPolicyDosEAPOLStartQT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 9),
    _Hh3cWIPSAtkDctPolicyDosEAPOLStartQT_Type()
)
hh3cWIPSAtkDctPolicyDosEAPOLStartQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyDosEAPOLStartQT.setStatus("current")


class _Hh3cWIPSAtkDctPolicyDosReAssoQT_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyDosReAssoQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSAtkDctPolicyDosReAssoQT_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyDosReAssoQT_Object = MibTableColumn
hh3cWIPSAtkDctPolicyDosReAssoQT = _Hh3cWIPSAtkDctPolicyDosReAssoQT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 10),
    _Hh3cWIPSAtkDctPolicyDosReAssoQT_Type()
)
hh3cWIPSAtkDctPolicyDosReAssoQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyDosReAssoQT.setStatus("current")


class _Hh3cWIPSAtkDctPolicyWeakIVQT_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyWeakIVQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSAtkDctPolicyWeakIVQT_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyWeakIVQT_Object = MibTableColumn
hh3cWIPSAtkDctPolicyWeakIVQT = _Hh3cWIPSAtkDctPolicyWeakIVQT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 11),
    _Hh3cWIPSAtkDctPolicyWeakIVQT_Type()
)
hh3cWIPSAtkDctPolicyWeakIVQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyWeakIVQT.setStatus("current")


class _Hh3cWIPSAtkDctPolicyInvalidOUIAction_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyInvalidOUIAction based on Integer32"""
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


_Hh3cWIPSAtkDctPolicyInvalidOUIAction_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyInvalidOUIAction_Object = MibTableColumn
hh3cWIPSAtkDctPolicyInvalidOUIAction = _Hh3cWIPSAtkDctPolicyInvalidOUIAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 12),
    _Hh3cWIPSAtkDctPolicyInvalidOUIAction_Type()
)
hh3cWIPSAtkDctPolicyInvalidOUIAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyInvalidOUIAction.setStatus("current")


class _Hh3cWIPSAtkDctPolicyUnencryptedAuthApQT_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyUnencryptedAuthApQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSAtkDctPolicyUnencryptedAuthApQT_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyUnencryptedAuthApQT_Object = MibTableColumn
hh3cWIPSAtkDctPolicyUnencryptedAuthApQT = _Hh3cWIPSAtkDctPolicyUnencryptedAuthApQT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 13),
    _Hh3cWIPSAtkDctPolicyUnencryptedAuthApQT_Type()
)
hh3cWIPSAtkDctPolicyUnencryptedAuthApQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyUnencryptedAuthApQT.setStatus("current")


class _Hh3cWIPSAtkDctPolicyUnencryptedAuthClientQT_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyUnencryptedAuthClientQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSAtkDctPolicyUnencryptedAuthClientQT_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyUnencryptedAuthClientQT_Object = MibTableColumn
hh3cWIPSAtkDctPolicyUnencryptedAuthClientQT = _Hh3cWIPSAtkDctPolicyUnencryptedAuthClientQT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 14),
    _Hh3cWIPSAtkDctPolicyUnencryptedAuthClientQT_Type()
)
hh3cWIPSAtkDctPolicyUnencryptedAuthClientQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyUnencryptedAuthClientQT.setStatus("current")


class _Hh3cWIPSAtkDctPolicyPSAttackQT_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyPSAttackQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSAtkDctPolicyPSAttackQT_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyPSAttackQT_Object = MibTableColumn
hh3cWIPSAtkDctPolicyPSAttackQT = _Hh3cWIPSAtkDctPolicyPSAttackQT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 15),
    _Hh3cWIPSAtkDctPolicyPSAttackQT_Type()
)
hh3cWIPSAtkDctPolicyPSAttackQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyPSAttackQT.setStatus("current")


class _Hh3cWIPSAtkDctPolicyPSAttackMinOffPacket_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyPSAttackMinOffPacket based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 150),
    )


_Hh3cWIPSAtkDctPolicyPSAttackMinOffPacket_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyPSAttackMinOffPacket_Object = MibTableColumn
hh3cWIPSAtkDctPolicyPSAttackMinOffPacket = _Hh3cWIPSAtkDctPolicyPSAttackMinOffPacket_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 16),
    _Hh3cWIPSAtkDctPolicyPSAttackMinOffPacket_Type()
)
hh3cWIPSAtkDctPolicyPSAttackMinOffPacket.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyPSAttackMinOffPacket.setStatus("current")


class _Hh3cWIPSAtkDctPolicyPSAttackOnOffPercent_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyPSAttackOnOffPercent based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cWIPSAtkDctPolicyPSAttackOnOffPercent_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyPSAttackOnOffPercent_Object = MibTableColumn
hh3cWIPSAtkDctPolicyPSAttackOnOffPercent = _Hh3cWIPSAtkDctPolicyPSAttackOnOffPercent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 17),
    _Hh3cWIPSAtkDctPolicyPSAttackOnOffPercent_Type()
)
hh3cWIPSAtkDctPolicyPSAttackOnOffPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyPSAttackOnOffPercent.setStatus("current")


class _Hh3cWIPSAtkDctPolicyApImpersonationQT_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyApImpersonationQT based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSAtkDctPolicyApImpersonationQT_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyApImpersonationQT_Object = MibTableColumn
hh3cWIPSAtkDctPolicyApImpersonationQT = _Hh3cWIPSAtkDctPolicyApImpersonationQT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 18),
    _Hh3cWIPSAtkDctPolicyApImpersonationQT_Type()
)
hh3cWIPSAtkDctPolicyApImpersonationQT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyApImpersonationQT.setStatus("current")


class _Hh3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Object = MibTableColumn
hh3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold = _Hh3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 19),
    _Hh3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Type()
)
hh3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold.setStatus("current")


class _Hh3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360000),
    )


_Hh3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Object = MibTableColumn
hh3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime = _Hh3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 20),
    _Hh3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Type()
)
hh3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime.setStatus("current")


class _Hh3cWIPSAtkDctPolicySoftApConvertTime_Type(Integer32):
    """Custom type hh3cWIPSAtkDctPolicySoftApConvertTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_Hh3cWIPSAtkDctPolicySoftApConvertTime_Type.__name__ = "Integer32"
_Hh3cWIPSAtkDctPolicySoftApConvertTime_Object = MibTableColumn
hh3cWIPSAtkDctPolicySoftApConvertTime = _Hh3cWIPSAtkDctPolicySoftApConvertTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 4, 2, 1, 21),
    _Hh3cWIPSAtkDctPolicySoftApConvertTime_Type()
)
hh3cWIPSAtkDctPolicySoftApConvertTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSAtkDctPolicySoftApConvertTime.setStatus("current")
_Hh3cWIPSStaticCtmListCfgTable_Object = MibTable
hh3cWIPSStaticCtmListCfgTable = _Hh3cWIPSStaticCtmListCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cWIPSStaticCtmListCfgTable.setStatus("current")
_Hh3cWIPSStaticCtmListCfgEntry_Object = MibTableRow
hh3cWIPSStaticCtmListCfgEntry = _Hh3cWIPSStaticCtmListCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 5, 1)
)
hh3cWIPSStaticCtmListCfgEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSStaticCtmListMAC"),
)
if mibBuilder.loadTexts:
    hh3cWIPSStaticCtmListCfgEntry.setStatus("current")
_Hh3cWIPSStaticCtmListMAC_Type = MacAddress
_Hh3cWIPSStaticCtmListMAC_Object = MibTableColumn
hh3cWIPSStaticCtmListMAC = _Hh3cWIPSStaticCtmListMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 5, 1, 1),
    _Hh3cWIPSStaticCtmListMAC_Type()
)
hh3cWIPSStaticCtmListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSStaticCtmListMAC.setStatus("current")
_Hh3cWIPSStaticCtmListRowStatus_Type = RowStatus
_Hh3cWIPSStaticCtmListRowStatus_Object = MibTableColumn
hh3cWIPSStaticCtmListRowStatus = _Hh3cWIPSStaticCtmListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 5, 1, 2),
    _Hh3cWIPSStaticCtmListRowStatus_Type()
)
hh3cWIPSStaticCtmListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSStaticCtmListRowStatus.setStatus("current")
_Hh3cWIPSStaticBlockListCfgTable_Object = MibTable
hh3cWIPSStaticBlockListCfgTable = _Hh3cWIPSStaticBlockListCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cWIPSStaticBlockListCfgTable.setStatus("current")
_Hh3cWIPSStaticBlockListCfgEntry_Object = MibTableRow
hh3cWIPSStaticBlockListCfgEntry = _Hh3cWIPSStaticBlockListCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 6, 1)
)
hh3cWIPSStaticBlockListCfgEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSStaticBlockListMAC"),
)
if mibBuilder.loadTexts:
    hh3cWIPSStaticBlockListCfgEntry.setStatus("current")
_Hh3cWIPSStaticBlockListMAC_Type = MacAddress
_Hh3cWIPSStaticBlockListMAC_Object = MibTableColumn
hh3cWIPSStaticBlockListMAC = _Hh3cWIPSStaticBlockListMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 6, 1, 1),
    _Hh3cWIPSStaticBlockListMAC_Type()
)
hh3cWIPSStaticBlockListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSStaticBlockListMAC.setStatus("current")
_Hh3cWIPSStaticBlockListRowStatus_Type = RowStatus
_Hh3cWIPSStaticBlockListRowStatus_Object = MibTableColumn
hh3cWIPSStaticBlockListRowStatus = _Hh3cWIPSStaticBlockListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 6, 1, 2),
    _Hh3cWIPSStaticBlockListRowStatus_Type()
)
hh3cWIPSStaticBlockListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSStaticBlockListRowStatus.setStatus("current")
_Hh3cWIPSStaticTrustListCfgTable_Object = MibTable
hh3cWIPSStaticTrustListCfgTable = _Hh3cWIPSStaticTrustListCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cWIPSStaticTrustListCfgTable.setStatus("current")
_Hh3cWIPSStaticTrustListCfgEntry_Object = MibTableRow
hh3cWIPSStaticTrustListCfgEntry = _Hh3cWIPSStaticTrustListCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 7, 1)
)
hh3cWIPSStaticTrustListCfgEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSStaticTrustListMAC"),
)
if mibBuilder.loadTexts:
    hh3cWIPSStaticTrustListCfgEntry.setStatus("current")
_Hh3cWIPSStaticTrustListMAC_Type = MacAddress
_Hh3cWIPSStaticTrustListMAC_Object = MibTableColumn
hh3cWIPSStaticTrustListMAC = _Hh3cWIPSStaticTrustListMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 7, 1, 1),
    _Hh3cWIPSStaticTrustListMAC_Type()
)
hh3cWIPSStaticTrustListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSStaticTrustListMAC.setStatus("current")
_Hh3cWIPSStaticTrustListRowStatus_Type = RowStatus
_Hh3cWIPSStaticTrustListRowStatus_Object = MibTableColumn
hh3cWIPSStaticTrustListRowStatus = _Hh3cWIPSStaticTrustListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 7, 1, 2),
    _Hh3cWIPSStaticTrustListRowStatus_Type()
)
hh3cWIPSStaticTrustListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSStaticTrustListRowStatus.setStatus("current")
_Hh3cWIPSIgnoreListCfgTable_Object = MibTable
hh3cWIPSIgnoreListCfgTable = _Hh3cWIPSIgnoreListCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cWIPSIgnoreListCfgTable.setStatus("current")
_Hh3cWIPSIgnoreListCfgEntry_Object = MibTableRow
hh3cWIPSIgnoreListCfgEntry = _Hh3cWIPSIgnoreListCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 8, 1)
)
hh3cWIPSIgnoreListCfgEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSIgnoreListMAC"),
)
if mibBuilder.loadTexts:
    hh3cWIPSIgnoreListCfgEntry.setStatus("current")
_Hh3cWIPSIgnoreListMAC_Type = MacAddress
_Hh3cWIPSIgnoreListMAC_Object = MibTableColumn
hh3cWIPSIgnoreListMAC = _Hh3cWIPSIgnoreListMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 8, 1, 1),
    _Hh3cWIPSIgnoreListMAC_Type()
)
hh3cWIPSIgnoreListMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSIgnoreListMAC.setStatus("current")
_Hh3cWIPSIgnoreListRowStatus_Type = RowStatus
_Hh3cWIPSIgnoreListRowStatus_Object = MibTableColumn
hh3cWIPSIgnoreListRowStatus = _Hh3cWIPSIgnoreListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 8, 1, 2),
    _Hh3cWIPSIgnoreListRowStatus_Type()
)
hh3cWIPSIgnoreListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSIgnoreListRowStatus.setStatus("current")
_Hh3cWIPSDctModeTable_Object = MibTable
hh3cWIPSDctModeTable = _Hh3cWIPSDctModeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cWIPSDctModeTable.setStatus("current")
_Hh3cWIPSDctModeEntry_Object = MibTableRow
hh3cWIPSDctModeEntry = _Hh3cWIPSDctModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 9, 1)
)
hh3cWIPSDctModeEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctModeAPName"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctModeRadio"),
)
if mibBuilder.loadTexts:
    hh3cWIPSDctModeEntry.setStatus("current")


class _Hh3cWIPSDctModeAPName_Type(OctetString):
    """Custom type hh3cWIPSDctModeAPName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cWIPSDctModeAPName_Type.__name__ = "OctetString"
_Hh3cWIPSDctModeAPName_Object = MibTableColumn
hh3cWIPSDctModeAPName = _Hh3cWIPSDctModeAPName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 9, 1, 1),
    _Hh3cWIPSDctModeAPName_Type()
)
hh3cWIPSDctModeAPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctModeAPName.setStatus("current")


class _Hh3cWIPSDctModeRadio_Type(Integer32):
    """Custom type hh3cWIPSDctModeRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cWIPSDctModeRadio_Type.__name__ = "Integer32"
_Hh3cWIPSDctModeRadio_Object = MibTableColumn
hh3cWIPSDctModeRadio = _Hh3cWIPSDctModeRadio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 9, 1, 2),
    _Hh3cWIPSDctModeRadio_Type()
)
hh3cWIPSDctModeRadio.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctModeRadio.setStatus("current")


class _Hh3cWIPSDctModeScanMode_Type(Integer32):
    """Custom type hh3cWIPSDctModeScanMode based on Integer32"""
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


_Hh3cWIPSDctModeScanMode_Type.__name__ = "Integer32"
_Hh3cWIPSDctModeScanMode_Object = MibTableColumn
hh3cWIPSDctModeScanMode = _Hh3cWIPSDctModeScanMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 9, 1, 3),
    _Hh3cWIPSDctModeScanMode_Type()
)
hh3cWIPSDctModeScanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSDctModeScanMode.setStatus("current")
_Hh3cWIPSDctModeRowStatus_Type = RowStatus
_Hh3cWIPSDctModeRowStatus_Object = MibTableColumn
hh3cWIPSDctModeRowStatus = _Hh3cWIPSDctModeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 9, 1, 4),
    _Hh3cWIPSDctModeRowStatus_Type()
)
hh3cWIPSDctModeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSDctModeRowStatus.setStatus("current")
_Hh3cWIPSSigConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWIPSSigConfigGroup = _Hh3cWIPSSigConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10)
)
_Hh3cWIPSSigPolicyTable_Object = MibTable
hh3cWIPSSigPolicyTable = _Hh3cWIPSSigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 1)
)
if mibBuilder.loadTexts:
    hh3cWIPSSigPolicyTable.setStatus("current")
_Hh3cWIPSSigPolicyEntry_Object = MibTableRow
hh3cWIPSSigPolicyEntry = _Hh3cWIPSSigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 1, 1)
)
hh3cWIPSSigPolicyEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSSigPolicyNameCfg"),
)
if mibBuilder.loadTexts:
    hh3cWIPSSigPolicyEntry.setStatus("current")


class _Hh3cWIPSSigPolicyNameCfg_Type(OctetString):
    """Custom type hh3cWIPSSigPolicyNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSSigPolicyNameCfg_Type.__name__ = "OctetString"
_Hh3cWIPSSigPolicyNameCfg_Object = MibTableColumn
hh3cWIPSSigPolicyNameCfg = _Hh3cWIPSSigPolicyNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 1, 1, 1),
    _Hh3cWIPSSigPolicyNameCfg_Type()
)
hh3cWIPSSigPolicyNameCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSSigPolicyNameCfg.setStatus("current")
_Hh3cWIPSSigPolicyRowStatus_Type = RowStatus
_Hh3cWIPSSigPolicyRowStatus_Object = MibTableColumn
hh3cWIPSSigPolicyRowStatus = _Hh3cWIPSSigPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 1, 1, 2),
    _Hh3cWIPSSigPolicyRowStatus_Type()
)
hh3cWIPSSigPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigPolicyRowStatus.setStatus("current")
_Hh3cWIPSSigRule2PolicyTable_Object = MibTable
hh3cWIPSSigRule2PolicyTable = _Hh3cWIPSSigRule2PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 2)
)
if mibBuilder.loadTexts:
    hh3cWIPSSigRule2PolicyTable.setStatus("current")
_Hh3cWIPSSigRule2PolicyEntry_Object = MibTableRow
hh3cWIPSSigRule2PolicyEntry = _Hh3cWIPSSigRule2PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 2, 1)
)
hh3cWIPSSigRule2PolicyEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSSigPolicyNameCfg"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSSigRule2PolicySigRuleIDCfg"),
)
if mibBuilder.loadTexts:
    hh3cWIPSSigRule2PolicyEntry.setStatus("current")


class _Hh3cWIPSSigRule2PolicySigRuleIDCfg_Type(Unsigned32):
    """Custom type hh3cWIPSSigRule2PolicySigRuleIDCfg based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cWIPSSigRule2PolicySigRuleIDCfg_Type.__name__ = "Unsigned32"
_Hh3cWIPSSigRule2PolicySigRuleIDCfg_Object = MibTableColumn
hh3cWIPSSigRule2PolicySigRuleIDCfg = _Hh3cWIPSSigRule2PolicySigRuleIDCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 2, 1, 1),
    _Hh3cWIPSSigRule2PolicySigRuleIDCfg_Type()
)
hh3cWIPSSigRule2PolicySigRuleIDCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSSigRule2PolicySigRuleIDCfg.setStatus("current")
_Hh3cWIPSSigRule2PolicyRowStatus_Type = RowStatus
_Hh3cWIPSSigRule2PolicyRowStatus_Object = MibTableColumn
hh3cWIPSSigRule2PolicyRowStatus = _Hh3cWIPSSigRule2PolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 2, 1, 2),
    _Hh3cWIPSSigRule2PolicyRowStatus_Type()
)
hh3cWIPSSigRule2PolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigRule2PolicyRowStatus.setStatus("current")


class _Hh3cWIPSSigRule2PolicyPrecedence_Type(Unsigned32):
    """Custom type hh3cWIPSSigRule2PolicyPrecedence based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cWIPSSigRule2PolicyPrecedence_Type.__name__ = "Unsigned32"
_Hh3cWIPSSigRule2PolicyPrecedence_Object = MibTableColumn
hh3cWIPSSigRule2PolicyPrecedence = _Hh3cWIPSSigRule2PolicyPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 2, 1, 3),
    _Hh3cWIPSSigRule2PolicyPrecedence_Type()
)
hh3cWIPSSigRule2PolicyPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigRule2PolicyPrecedence.setStatus("current")
_Hh3cWIPSSigRuleTable_Object = MibTable
hh3cWIPSSigRuleTable = _Hh3cWIPSSigRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3)
)
if mibBuilder.loadTexts:
    hh3cWIPSSigRuleTable.setStatus("current")
_Hh3cWIPSSigRuleEntry_Object = MibTableRow
hh3cWIPSSigRuleEntry = _Hh3cWIPSSigRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1)
)
hh3cWIPSSigRuleEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSSigRuleName"),
)
if mibBuilder.loadTexts:
    hh3cWIPSSigRuleEntry.setStatus("current")


class _Hh3cWIPSSigRuleName_Type(OctetString):
    """Custom type hh3cWIPSSigRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSSigRuleName_Type.__name__ = "OctetString"
_Hh3cWIPSSigRuleName_Object = MibTableColumn
hh3cWIPSSigRuleName = _Hh3cWIPSSigRuleName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 1),
    _Hh3cWIPSSigRuleName_Type()
)
hh3cWIPSSigRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSSigRuleName.setStatus("current")


class _Hh3cWIPSSigRuleID_Type(Integer32):
    """Custom type hh3cWIPSSigRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cWIPSSigRuleID_Type.__name__ = "Integer32"
_Hh3cWIPSSigRuleID_Object = MibTableColumn
hh3cWIPSSigRuleID = _Hh3cWIPSSigRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 2),
    _Hh3cWIPSSigRuleID_Type()
)
hh3cWIPSSigRuleID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigRuleID.setStatus("current")
_Hh3cWIPSSigRuleRowStatus_Type = RowStatus
_Hh3cWIPSSigRuleRowStatus_Object = MibTableColumn
hh3cWIPSSigRuleRowStatus = _Hh3cWIPSSigRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 3),
    _Hh3cWIPSSigRuleRowStatus_Type()
)
hh3cWIPSSigRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigRuleRowStatus.setStatus("current")
_Hh3cWIPSSigSubRuleMatchAll_Type = TruthValue
_Hh3cWIPSSigSubRuleMatchAll_Object = MibTableColumn
hh3cWIPSSigSubRuleMatchAll = _Hh3cWIPSSigSubRuleMatchAll_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 4),
    _Hh3cWIPSSigSubRuleMatchAll_Type()
)
hh3cWIPSSigSubRuleMatchAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleMatchAll.setStatus("current")
_Hh3cWIPSSigRuleDctPeriod_Type = Unsigned32
_Hh3cWIPSSigRuleDctPeriod_Object = MibTableColumn
hh3cWIPSSigRuleDctPeriod = _Hh3cWIPSSigRuleDctPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 5),
    _Hh3cWIPSSigRuleDctPeriod_Type()
)
hh3cWIPSSigRuleDctPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigRuleDctPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWIPSSigRuleDctPeriod.setUnits("second")


class _Hh3cWIPSSigRuleTrackMethod_Type(Integer32):
    """Custom type hh3cWIPSSigRuleTrackMethod based on Integer32"""
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


_Hh3cWIPSSigRuleTrackMethod_Type.__name__ = "Integer32"
_Hh3cWIPSSigRuleTrackMethod_Object = MibTableColumn
hh3cWIPSSigRuleTrackMethod = _Hh3cWIPSSigRuleTrackMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 6),
    _Hh3cWIPSSigRuleTrackMethod_Type()
)
hh3cWIPSSigRuleTrackMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigRuleTrackMethod.setStatus("current")
_Hh3cWIPSSigRuleDctThresholdPerMAC_Type = Unsigned32
_Hh3cWIPSSigRuleDctThresholdPerMAC_Object = MibTableColumn
hh3cWIPSSigRuleDctThresholdPerMAC = _Hh3cWIPSSigRuleDctThresholdPerMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 7),
    _Hh3cWIPSSigRuleDctThresholdPerMAC_Type()
)
hh3cWIPSSigRuleDctThresholdPerMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigRuleDctThresholdPerMAC.setStatus("current")
_Hh3cWIPSSigRuleDctThresholdPerSig_Type = Unsigned32
_Hh3cWIPSSigRuleDctThresholdPerSig_Object = MibTableColumn
hh3cWIPSSigRuleDctThresholdPerSig = _Hh3cWIPSSigRuleDctThresholdPerSig_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 8),
    _Hh3cWIPSSigRuleDctThresholdPerSig_Type()
)
hh3cWIPSSigRuleDctThresholdPerSig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigRuleDctThresholdPerSig.setStatus("current")
_Hh3cWIPSSigRuleActionEvtLevel_Type = Unsigned32
_Hh3cWIPSSigRuleActionEvtLevel_Object = MibTableColumn
hh3cWIPSSigRuleActionEvtLevel = _Hh3cWIPSSigRuleActionEvtLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 9),
    _Hh3cWIPSSigRuleActionEvtLevel_Type()
)
hh3cWIPSSigRuleActionEvtLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigRuleActionEvtLevel.setStatus("current")
_Hh3cWIPSSigRuleQuietTime_Type = Unsigned32
_Hh3cWIPSSigRuleQuietTime_Object = MibTableColumn
hh3cWIPSSigRuleQuietTime = _Hh3cWIPSSigRuleQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 10),
    _Hh3cWIPSSigRuleQuietTime_Type()
)
hh3cWIPSSigRuleQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigRuleQuietTime.setStatus("current")


class _Hh3cWIPSSigSubRuleFrameType_Type(Integer32):
    """Custom type hh3cWIPSSigSubRuleFrameType based on Integer32"""
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


_Hh3cWIPSSigSubRuleFrameType_Type.__name__ = "Integer32"
_Hh3cWIPSSigSubRuleFrameType_Object = MibTableColumn
hh3cWIPSSigSubRuleFrameType = _Hh3cWIPSSigSubRuleFrameType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 11),
    _Hh3cWIPSSigSubRuleFrameType_Type()
)
hh3cWIPSSigSubRuleFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleFrameType.setStatus("current")


class _Hh3cWIPSSigSubRuleFrameSubType_Type(Integer32):
    """Custom type hh3cWIPSSigSubRuleFrameSubType based on Integer32"""
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


_Hh3cWIPSSigSubRuleFrameSubType_Type.__name__ = "Integer32"
_Hh3cWIPSSigSubRuleFrameSubType_Object = MibTableColumn
hh3cWIPSSigSubRuleFrameSubType = _Hh3cWIPSSigSubRuleFrameSubType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 12),
    _Hh3cWIPSSigSubRuleFrameSubType_Type()
)
hh3cWIPSSigSubRuleFrameSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleFrameSubType.setStatus("current")


class _Hh3cWIPSSigSubRuleMac_Type(OctetString):
    """Custom type hh3cWIPSSigSubRuleMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Hh3cWIPSSigSubRuleMac_Type.__name__ = "OctetString"
_Hh3cWIPSSigSubRuleMac_Object = MibTableColumn
hh3cWIPSSigSubRuleMac = _Hh3cWIPSSigSubRuleMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 13),
    _Hh3cWIPSSigSubRuleMac_Type()
)
hh3cWIPSSigSubRuleMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleMac.setStatus("current")


class _Hh3cWIPSSigSubRuleMacType_Type(Integer32):
    """Custom type hh3cWIPSSigSubRuleMacType based on Integer32"""
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


_Hh3cWIPSSigSubRuleMacType_Type.__name__ = "Integer32"
_Hh3cWIPSSigSubRuleMacType_Object = MibTableColumn
hh3cWIPSSigSubRuleMacType = _Hh3cWIPSSigSubRuleMacType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 14),
    _Hh3cWIPSSigSubRuleMacType_Type()
)
hh3cWIPSSigSubRuleMacType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleMacType.setStatus("current")
_Hh3cWIPSSigSubRuleSeqNumMin_Type = Unsigned32
_Hh3cWIPSSigSubRuleSeqNumMin_Object = MibTableColumn
hh3cWIPSSigSubRuleSeqNumMin = _Hh3cWIPSSigSubRuleSeqNumMin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 15),
    _Hh3cWIPSSigSubRuleSeqNumMin_Type()
)
hh3cWIPSSigSubRuleSeqNumMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleSeqNumMin.setStatus("current")
_Hh3cWIPSSigSubRuleSeqNumMax_Type = Unsigned32
_Hh3cWIPSSigSubRuleSeqNumMax_Object = MibTableColumn
hh3cWIPSSigSubRuleSeqNumMax = _Hh3cWIPSSigSubRuleSeqNumMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 16),
    _Hh3cWIPSSigSubRuleSeqNumMax_Type()
)
hh3cWIPSSigSubRuleSeqNumMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleSeqNumMax.setStatus("current")
_Hh3cWIPSSigSubRuleSSIDLenMin_Type = Unsigned32
_Hh3cWIPSSigSubRuleSSIDLenMin_Object = MibTableColumn
hh3cWIPSSigSubRuleSSIDLenMin = _Hh3cWIPSSigSubRuleSSIDLenMin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 17),
    _Hh3cWIPSSigSubRuleSSIDLenMin_Type()
)
hh3cWIPSSigSubRuleSSIDLenMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleSSIDLenMin.setStatus("current")
_Hh3cWIPSSigSubRuleSSIDLenMax_Type = Unsigned32
_Hh3cWIPSSigSubRuleSSIDLenMax_Object = MibTableColumn
hh3cWIPSSigSubRuleSSIDLenMax = _Hh3cWIPSSigSubRuleSSIDLenMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 18),
    _Hh3cWIPSSigSubRuleSSIDLenMax_Type()
)
hh3cWIPSSigSubRuleSSIDLenMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleSSIDLenMax.setStatus("current")


class _Hh3cWIPSSigSubRuleSSID_Type(OctetString):
    """Custom type hh3cWIPSSigSubRuleSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cWIPSSigSubRuleSSID_Type.__name__ = "OctetString"
_Hh3cWIPSSigSubRuleSSID_Object = MibTableColumn
hh3cWIPSSigSubRuleSSID = _Hh3cWIPSSigSubRuleSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 19),
    _Hh3cWIPSSigSubRuleSSID_Type()
)
hh3cWIPSSigSubRuleSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleSSID.setStatus("current")


class _Hh3cWIPSSigSubRuleSSIDOpe_Type(Integer32):
    """Custom type hh3cWIPSSigSubRuleSSIDOpe based on Integer32"""
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


_Hh3cWIPSSigSubRuleSSIDOpe_Type.__name__ = "Integer32"
_Hh3cWIPSSigSubRuleSSIDOpe_Object = MibTableColumn
hh3cWIPSSigSubRuleSSIDOpe = _Hh3cWIPSSigSubRuleSSIDOpe_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 20),
    _Hh3cWIPSSigSubRuleSSIDOpe_Type()
)
hh3cWIPSSigSubRuleSSIDOpe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleSSIDOpe.setStatus("current")


class _Hh3cWIPSSigSubRuleSSIDCase_Type(TruthValue):
    """Custom type hh3cWIPSSigSubRuleSSIDCase based on TruthValue"""


_Hh3cWIPSSigSubRuleSSIDCase_Object = MibTableColumn
hh3cWIPSSigSubRuleSSIDCase = _Hh3cWIPSSigSubRuleSSIDCase_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 3, 1, 21),
    _Hh3cWIPSSigSubRuleSSIDCase_Type()
)
hh3cWIPSSigSubRuleSSIDCase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleSSIDCase.setStatus("current")
_Hh3cWIPSSigSubRulePatternTable_Object = MibTable
hh3cWIPSSigSubRulePatternTable = _Hh3cWIPSSigSubRulePatternTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 4)
)
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRulePatternTable.setStatus("current")
_Hh3cWIPSSigSubRulePatternEntry_Object = MibTableRow
hh3cWIPSSigSubRulePatternEntry = _Hh3cWIPSSigSubRulePatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 4, 1)
)
hh3cWIPSSigSubRulePatternEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSSigRuleName"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSSigSubRulePatternID"),
)
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRulePatternEntry.setStatus("current")


class _Hh3cWIPSSigSubRulePatternID_Type(Unsigned32):
    """Custom type hh3cWIPSSigSubRulePatternID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 27),
    )


_Hh3cWIPSSigSubRulePatternID_Type.__name__ = "Unsigned32"
_Hh3cWIPSSigSubRulePatternID_Object = MibTableColumn
hh3cWIPSSigSubRulePatternID = _Hh3cWIPSSigSubRulePatternID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 4, 1, 1),
    _Hh3cWIPSSigSubRulePatternID_Type()
)
hh3cWIPSSigSubRulePatternID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRulePatternID.setStatus("current")
_Hh3cWIPSSigSubRuleRowStatus_Type = RowStatus
_Hh3cWIPSSigSubRuleRowStatus_Object = MibTableColumn
hh3cWIPSSigSubRuleRowStatus = _Hh3cWIPSSigSubRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 4, 1, 2),
    _Hh3cWIPSSigSubRuleRowStatus_Type()
)
hh3cWIPSSigSubRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRuleRowStatus.setStatus("current")


class _Hh3cWIPSSigSubRulePatternName_Type(OctetString):
    """Custom type hh3cWIPSSigSubRulePatternName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cWIPSSigSubRulePatternName_Type.__name__ = "OctetString"
_Hh3cWIPSSigSubRulePatternName_Object = MibTableColumn
hh3cWIPSSigSubRulePatternName = _Hh3cWIPSSigSubRulePatternName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 4, 1, 3),
    _Hh3cWIPSSigSubRulePatternName_Type()
)
hh3cWIPSSigSubRulePatternName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRulePatternName.setStatus("current")


class _Hh3cWIPSSigSubRulePatternOffset_Type(Integer32):
    """Custom type hh3cWIPSSigSubRulePatternOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2346),
    )


_Hh3cWIPSSigSubRulePatternOffset_Type.__name__ = "Integer32"
_Hh3cWIPSSigSubRulePatternOffset_Object = MibTableColumn
hh3cWIPSSigSubRulePatternOffset = _Hh3cWIPSSigSubRulePatternOffset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 4, 1, 4),
    _Hh3cWIPSSigSubRulePatternOffset_Type()
)
hh3cWIPSSigSubRulePatternOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRulePatternOffset.setStatus("current")


class _Hh3cWIPSSigSubRulePatternMask_Type(Integer32):
    """Custom type hh3cWIPSSigSubRulePatternMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWIPSSigSubRulePatternMask_Type.__name__ = "Integer32"
_Hh3cWIPSSigSubRulePatternMask_Object = MibTableColumn
hh3cWIPSSigSubRulePatternMask = _Hh3cWIPSSigSubRulePatternMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 4, 1, 5),
    _Hh3cWIPSSigSubRulePatternMask_Type()
)
hh3cWIPSSigSubRulePatternMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRulePatternMask.setStatus("current")


class _Hh3cWIPSSigSubRulePatternValueMin_Type(Unsigned32):
    """Custom type hh3cWIPSSigSubRulePatternValueMin based on Unsigned32"""
    defaultHexValue = 4294967295


_Hh3cWIPSSigSubRulePatternValueMin_Object = MibTableColumn
hh3cWIPSSigSubRulePatternValueMin = _Hh3cWIPSSigSubRulePatternValueMin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 4, 1, 6),
    _Hh3cWIPSSigSubRulePatternValueMin_Type()
)
hh3cWIPSSigSubRulePatternValueMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRulePatternValueMin.setStatus("current")


class _Hh3cWIPSSigSubRulePatternValueMax_Type(Unsigned32):
    """Custom type hh3cWIPSSigSubRulePatternValueMax based on Unsigned32"""
    defaultHexValue = 4294967295


_Hh3cWIPSSigSubRulePatternValueMax_Object = MibTableColumn
hh3cWIPSSigSubRulePatternValueMax = _Hh3cWIPSSigSubRulePatternValueMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 4, 1, 7),
    _Hh3cWIPSSigSubRulePatternValueMax_Type()
)
hh3cWIPSSigSubRulePatternValueMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRulePatternValueMax.setStatus("current")


class _Hh3cWIPSSigSubRulePatternFromPayload_Type(TruthValue):
    """Custom type hh3cWIPSSigSubRulePatternFromPayload based on TruthValue"""


_Hh3cWIPSSigSubRulePatternFromPayload_Object = MibTableColumn
hh3cWIPSSigSubRulePatternFromPayload = _Hh3cWIPSSigSubRulePatternFromPayload_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 10, 4, 1, 8),
    _Hh3cWIPSSigSubRulePatternFromPayload_Type()
)
hh3cWIPSSigSubRulePatternFromPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSSigSubRulePatternFromPayload.setStatus("current")
_Hh3cWIPSCtmConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWIPSCtmConfigGroup = _Hh3cWIPSCtmConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11)
)


class _Hh3cWIPSCtmPolicyCfgSupportSet_Type(OctetString):
    """Custom type hh3cWIPSCtmPolicyCfgSupportSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Hh3cWIPSCtmPolicyCfgSupportSet_Type.__name__ = "OctetString"
_Hh3cWIPSCtmPolicyCfgSupportSet_Object = MibScalar
hh3cWIPSCtmPolicyCfgSupportSet = _Hh3cWIPSCtmPolicyCfgSupportSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 1),
    _Hh3cWIPSCtmPolicyCfgSupportSet_Type()
)
hh3cWIPSCtmPolicyCfgSupportSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyCfgSupportSet.setStatus("current")
_Hh3cWIPSCtmPolicyTable_Object = MibTable
hh3cWIPSCtmPolicyTable = _Hh3cWIPSCtmPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2)
)
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyTable.setStatus("current")
_Hh3cWIPSCtmPolicyEntry_Object = MibTableRow
hh3cWIPSCtmPolicyEntry = _Hh3cWIPSCtmPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1)
)
hh3cWIPSCtmPolicyEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSCtmPolicyName"),
)
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyEntry.setStatus("current")


class _Hh3cWIPSCtmPolicyName_Type(OctetString):
    """Custom type hh3cWIPSCtmPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSCtmPolicyName_Type.__name__ = "OctetString"
_Hh3cWIPSCtmPolicyName_Object = MibTableColumn
hh3cWIPSCtmPolicyName = _Hh3cWIPSCtmPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 1),
    _Hh3cWIPSCtmPolicyName_Type()
)
hh3cWIPSCtmPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyName.setStatus("current")
_Hh3cWIPSCtmPolicyCfgRowStatus_Type = RowStatus
_Hh3cWIPSCtmPolicyCfgRowStatus_Object = MibTableColumn
hh3cWIPSCtmPolicyCfgRowStatus = _Hh3cWIPSCtmPolicyCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 2),
    _Hh3cWIPSCtmPolicyCfgRowStatus_Type()
)
hh3cWIPSCtmPolicyCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyCfgRowStatus.setStatus("current")


class _Hh3cWIPSCtmPolicyBitString_Type(OctetString):
    """Custom type hh3cWIPSCtmPolicyBitString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Hh3cWIPSCtmPolicyBitString_Type.__name__ = "OctetString"
_Hh3cWIPSCtmPolicyBitString_Object = MibTableColumn
hh3cWIPSCtmPolicyBitString = _Hh3cWIPSCtmPolicyBitString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 3),
    _Hh3cWIPSCtmPolicyBitString_Type()
)
hh3cWIPSCtmPolicyBitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyBitString.setStatus("current")


class _Hh3cWIPSCtmPolicyFixedChl_Type(TruthValue):
    """Custom type hh3cWIPSCtmPolicyFixedChl based on TruthValue"""


_Hh3cWIPSCtmPolicyFixedChl_Object = MibTableColumn
hh3cWIPSCtmPolicyFixedChl = _Hh3cWIPSCtmPolicyFixedChl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 4),
    _Hh3cWIPSCtmPolicyFixedChl_Type()
)
hh3cWIPSCtmPolicyFixedChl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyFixedChl.setStatus("current")


class _Hh3cWIPSCtmPolicyRogueAPPre_Type(Unsigned32):
    """Custom type hh3cWIPSCtmPolicyRogueAPPre based on Unsigned32"""
    defaultValue = 9


_Hh3cWIPSCtmPolicyRogueAPPre_Object = MibTableColumn
hh3cWIPSCtmPolicyRogueAPPre = _Hh3cWIPSCtmPolicyRogueAPPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 5),
    _Hh3cWIPSCtmPolicyRogueAPPre_Type()
)
hh3cWIPSCtmPolicyRogueAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyRogueAPPre.setStatus("current")


class _Hh3cWIPSCtmPolicyPtRogueAPPre_Type(Unsigned32):
    """Custom type hh3cWIPSCtmPolicyPtRogueAPPre based on Unsigned32"""
    defaultValue = 7


_Hh3cWIPSCtmPolicyPtRogueAPPre_Object = MibTableColumn
hh3cWIPSCtmPolicyPtRogueAPPre = _Hh3cWIPSCtmPolicyPtRogueAPPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 6),
    _Hh3cWIPSCtmPolicyPtRogueAPPre_Type()
)
hh3cWIPSCtmPolicyPtRogueAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyPtRogueAPPre.setStatus("current")


class _Hh3cWIPSCtmPolicyMisconfAPPre_Type(Unsigned32):
    """Custom type hh3cWIPSCtmPolicyMisconfAPPre based on Unsigned32"""
    defaultValue = 3


_Hh3cWIPSCtmPolicyMisconfAPPre_Object = MibTableColumn
hh3cWIPSCtmPolicyMisconfAPPre = _Hh3cWIPSCtmPolicyMisconfAPPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 7),
    _Hh3cWIPSCtmPolicyMisconfAPPre_Type()
)
hh3cWIPSCtmPolicyMisconfAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyMisconfAPPre.setStatus("current")


class _Hh3cWIPSCtmPolicyExternalAPPre_Type(Unsigned32):
    """Custom type hh3cWIPSCtmPolicyExternalAPPre based on Unsigned32"""
    defaultValue = 1


_Hh3cWIPSCtmPolicyExternalAPPre_Object = MibTableColumn
hh3cWIPSCtmPolicyExternalAPPre = _Hh3cWIPSCtmPolicyExternalAPPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 8),
    _Hh3cWIPSCtmPolicyExternalAPPre_Type()
)
hh3cWIPSCtmPolicyExternalAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyExternalAPPre.setStatus("current")


class _Hh3cWIPSCtmPolicyPtExternalAPPre_Type(Unsigned32):
    """Custom type hh3cWIPSCtmPolicyPtExternalAPPre based on Unsigned32"""
    defaultValue = 2


_Hh3cWIPSCtmPolicyPtExternalAPPre_Object = MibTableColumn
hh3cWIPSCtmPolicyPtExternalAPPre = _Hh3cWIPSCtmPolicyPtExternalAPPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 9),
    _Hh3cWIPSCtmPolicyPtExternalAPPre_Type()
)
hh3cWIPSCtmPolicyPtExternalAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyPtExternalAPPre.setStatus("current")


class _Hh3cWIPSCtmPolicyUncateAPPre_Type(Unsigned32):
    """Custom type hh3cWIPSCtmPolicyUncateAPPre based on Unsigned32"""
    defaultValue = 5


_Hh3cWIPSCtmPolicyUncateAPPre_Object = MibTableColumn
hh3cWIPSCtmPolicyUncateAPPre = _Hh3cWIPSCtmPolicyUncateAPPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 10),
    _Hh3cWIPSCtmPolicyUncateAPPre_Type()
)
hh3cWIPSCtmPolicyUncateAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyUncateAPPre.setStatus("current")


class _Hh3cWIPSCtmPolicyPtAuthAPPre_Type(Unsigned32):
    """Custom type hh3cWIPSCtmPolicyPtAuthAPPre based on Unsigned32"""
    defaultValue = 0


_Hh3cWIPSCtmPolicyPtAuthAPPre_Object = MibTableColumn
hh3cWIPSCtmPolicyPtAuthAPPre = _Hh3cWIPSCtmPolicyPtAuthAPPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 11),
    _Hh3cWIPSCtmPolicyPtAuthAPPre_Type()
)
hh3cWIPSCtmPolicyPtAuthAPPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyPtAuthAPPre.setStatus("current")


class _Hh3cWIPSCtmPolicyMisassoStaPre_Type(Unsigned32):
    """Custom type hh3cWIPSCtmPolicyMisassoStaPre based on Unsigned32"""
    defaultValue = 6


_Hh3cWIPSCtmPolicyMisassoStaPre_Object = MibTableColumn
hh3cWIPSCtmPolicyMisassoStaPre = _Hh3cWIPSCtmPolicyMisassoStaPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 12),
    _Hh3cWIPSCtmPolicyMisassoStaPre_Type()
)
hh3cWIPSCtmPolicyMisassoStaPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyMisassoStaPre.setStatus("current")


class _Hh3cWIPSCtmPolicyUncateStaPre_Type(Unsigned32):
    """Custom type hh3cWIPSCtmPolicyUncateStaPre based on Unsigned32"""
    defaultValue = 4


_Hh3cWIPSCtmPolicyUncateStaPre_Object = MibTableColumn
hh3cWIPSCtmPolicyUncateStaPre = _Hh3cWIPSCtmPolicyUncateStaPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 13),
    _Hh3cWIPSCtmPolicyUncateStaPre_Type()
)
hh3cWIPSCtmPolicyUncateStaPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyUncateStaPre.setStatus("current")


class _Hh3cWIPSCtmPolicyUnauthStaPre_Type(Unsigned32):
    """Custom type hh3cWIPSCtmPolicyUnauthStaPre based on Unsigned32"""
    defaultValue = 8


_Hh3cWIPSCtmPolicyUnauthStaPre_Object = MibTableColumn
hh3cWIPSCtmPolicyUnauthStaPre = _Hh3cWIPSCtmPolicyUnauthStaPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 2, 1, 14),
    _Hh3cWIPSCtmPolicyUnauthStaPre_Type()
)
hh3cWIPSCtmPolicyUnauthStaPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyUnauthStaPre.setStatus("current")
_Hh3cWIPSCtmPolicyDevListTable_Object = MibTable
hh3cWIPSCtmPolicyDevListTable = _Hh3cWIPSCtmPolicyDevListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 3)
)
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyDevListTable.setStatus("current")
_Hh3cWIPSCtmPolicyDevListEntry_Object = MibTableRow
hh3cWIPSCtmPolicyDevListEntry = _Hh3cWIPSCtmPolicyDevListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 3, 1)
)
hh3cWIPSCtmPolicyDevListEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSCtmPolicyName"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSCtmPolicyDevMAC"),
)
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyDevListEntry.setStatus("current")
_Hh3cWIPSCtmPolicyDevMAC_Type = MacAddress
_Hh3cWIPSCtmPolicyDevMAC_Object = MibTableColumn
hh3cWIPSCtmPolicyDevMAC = _Hh3cWIPSCtmPolicyDevMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 3, 1, 1),
    _Hh3cWIPSCtmPolicyDevMAC_Type()
)
hh3cWIPSCtmPolicyDevMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyDevMAC.setStatus("current")
_Hh3cWIPSCtmPolicyDevRowStatus_Type = RowStatus
_Hh3cWIPSCtmPolicyDevRowStatus_Object = MibTableColumn
hh3cWIPSCtmPolicyDevRowStatus = _Hh3cWIPSCtmPolicyDevRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 11, 3, 1, 2),
    _Hh3cWIPSCtmPolicyDevRowStatus_Type()
)
hh3cWIPSCtmPolicyDevRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSCtmPolicyDevRowStatus.setStatus("current")
_Hh3cWIPSMalPktDctConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWIPSMalPktDctConfigGroup = _Hh3cWIPSMalPktDctConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 12)
)


class _Hh3cWIPSMalPktDctCfgLogSupportSet_Type(OctetString):
    """Custom type hh3cWIPSMalPktDctCfgLogSupportSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Hh3cWIPSMalPktDctCfgLogSupportSet_Type.__name__ = "OctetString"
_Hh3cWIPSMalPktDctCfgLogSupportSet_Object = MibScalar
hh3cWIPSMalPktDctCfgLogSupportSet = _Hh3cWIPSMalPktDctCfgLogSupportSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 12, 1),
    _Hh3cWIPSMalPktDctCfgLogSupportSet_Type()
)
hh3cWIPSMalPktDctCfgLogSupportSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktDctCfgLogSupportSet.setStatus("current")


class _Hh3cWIPSMalPktDctCfgTrapSupportSet_Type(OctetString):
    """Custom type hh3cWIPSMalPktDctCfgTrapSupportSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Hh3cWIPSMalPktDctCfgTrapSupportSet_Type.__name__ = "OctetString"
_Hh3cWIPSMalPktDctCfgTrapSupportSet_Object = MibScalar
hh3cWIPSMalPktDctCfgTrapSupportSet = _Hh3cWIPSMalPktDctCfgTrapSupportSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 12, 2),
    _Hh3cWIPSMalPktDctCfgTrapSupportSet_Type()
)
hh3cWIPSMalPktDctCfgTrapSupportSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktDctCfgTrapSupportSet.setStatus("current")
_Hh3cWIPSMalPktDctPolicyTable_Object = MibTable
hh3cWIPSMalPktDctPolicyTable = _Hh3cWIPSMalPktDctPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 12, 3)
)
if mibBuilder.loadTexts:
    hh3cWIPSMalPktDctPolicyTable.setStatus("current")
_Hh3cWIPSMalPktDctPolicyEntry_Object = MibTableRow
hh3cWIPSMalPktDctPolicyEntry = _Hh3cWIPSMalPktDctPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 12, 3, 1)
)
hh3cWIPSMalPktDctPolicyEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSMalPktDctPolicyName"),
)
if mibBuilder.loadTexts:
    hh3cWIPSMalPktDctPolicyEntry.setStatus("current")


class _Hh3cWIPSMalPktDctPolicyName_Type(OctetString):
    """Custom type hh3cWIPSMalPktDctPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSMalPktDctPolicyName_Type.__name__ = "OctetString"
_Hh3cWIPSMalPktDctPolicyName_Object = MibTableColumn
hh3cWIPSMalPktDctPolicyName = _Hh3cWIPSMalPktDctPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 12, 3, 1, 1),
    _Hh3cWIPSMalPktDctPolicyName_Type()
)
hh3cWIPSMalPktDctPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktDctPolicyName.setStatus("current")
_Hh3cWIPSMalPktDctPolicyCfgRowStatus_Type = RowStatus
_Hh3cWIPSMalPktDctPolicyCfgRowStatus_Object = MibTableColumn
hh3cWIPSMalPktDctPolicyCfgRowStatus = _Hh3cWIPSMalPktDctPolicyCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 12, 3, 1, 2),
    _Hh3cWIPSMalPktDctPolicyCfgRowStatus_Type()
)
hh3cWIPSMalPktDctPolicyCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktDctPolicyCfgRowStatus.setStatus("current")


class _Hh3cWIPSMalPktDctPolicyLogBitString_Type(OctetString):
    """Custom type hh3cWIPSMalPktDctPolicyLogBitString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Hh3cWIPSMalPktDctPolicyLogBitString_Type.__name__ = "OctetString"
_Hh3cWIPSMalPktDctPolicyLogBitString_Object = MibTableColumn
hh3cWIPSMalPktDctPolicyLogBitString = _Hh3cWIPSMalPktDctPolicyLogBitString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 12, 3, 1, 3),
    _Hh3cWIPSMalPktDctPolicyLogBitString_Type()
)
hh3cWIPSMalPktDctPolicyLogBitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktDctPolicyLogBitString.setStatus("current")


class _Hh3cWIPSMalPktDctPolicyTrapBitString_Type(OctetString):
    """Custom type hh3cWIPSMalPktDctPolicyTrapBitString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Hh3cWIPSMalPktDctPolicyTrapBitString_Type.__name__ = "OctetString"
_Hh3cWIPSMalPktDctPolicyTrapBitString_Object = MibTableColumn
hh3cWIPSMalPktDctPolicyTrapBitString = _Hh3cWIPSMalPktDctPolicyTrapBitString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 12, 3, 1, 4),
    _Hh3cWIPSMalPktDctPolicyTrapBitString_Type()
)
hh3cWIPSMalPktDctPolicyTrapBitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktDctPolicyTrapBitString.setStatus("current")


class _Hh3cWIPSMalPktDctPolicyDurationThreshold_Type(Integer32):
    """Custom type hh3cWIPSMalPktDctPolicyDurationThreshold based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Hh3cWIPSMalPktDctPolicyDurationThreshold_Type.__name__ = "Integer32"
_Hh3cWIPSMalPktDctPolicyDurationThreshold_Object = MibTableColumn
hh3cWIPSMalPktDctPolicyDurationThreshold = _Hh3cWIPSMalPktDctPolicyDurationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 12, 3, 1, 5),
    _Hh3cWIPSMalPktDctPolicyDurationThreshold_Type()
)
hh3cWIPSMalPktDctPolicyDurationThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktDctPolicyDurationThreshold.setStatus("current")


class _Hh3cWIPSMalPktDctPolicyQuietTime_Type(Integer32):
    """Custom type hh3cWIPSMalPktDctPolicyQuietTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cWIPSMalPktDctPolicyQuietTime_Type.__name__ = "Integer32"
_Hh3cWIPSMalPktDctPolicyQuietTime_Object = MibTableColumn
hh3cWIPSMalPktDctPolicyQuietTime = _Hh3cWIPSMalPktDctPolicyQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 12, 3, 1, 6),
    _Hh3cWIPSMalPktDctPolicyQuietTime_Type()
)
hh3cWIPSMalPktDctPolicyQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktDctPolicyQuietTime.setStatus("current")
_Hh3cWIPSStaticTrustOUIListCfgTable_Object = MibTable
hh3cWIPSStaticTrustOUIListCfgTable = _Hh3cWIPSStaticTrustOUIListCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 13)
)
if mibBuilder.loadTexts:
    hh3cWIPSStaticTrustOUIListCfgTable.setStatus("current")
_Hh3cWIPSStaticTrustOUIListCfgEntry_Object = MibTableRow
hh3cWIPSStaticTrustOUIListCfgEntry = _Hh3cWIPSStaticTrustOUIListCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 13, 1)
)
hh3cWIPSStaticTrustOUIListCfgEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSStaticTrustOUIListOUI"),
)
if mibBuilder.loadTexts:
    hh3cWIPSStaticTrustOUIListCfgEntry.setStatus("current")


class _Hh3cWIPSStaticTrustOUIListOUI_Type(OctetString):
    """Custom type hh3cWIPSStaticTrustOUIListOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Hh3cWIPSStaticTrustOUIListOUI_Type.__name__ = "OctetString"
_Hh3cWIPSStaticTrustOUIListOUI_Object = MibTableColumn
hh3cWIPSStaticTrustOUIListOUI = _Hh3cWIPSStaticTrustOUIListOUI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 13, 1, 1),
    _Hh3cWIPSStaticTrustOUIListOUI_Type()
)
hh3cWIPSStaticTrustOUIListOUI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSStaticTrustOUIListOUI.setStatus("current")
_Hh3cWIPSStaticTrustOUIListRowStatus_Type = RowStatus
_Hh3cWIPSStaticTrustOUIListRowStatus_Object = MibTableColumn
hh3cWIPSStaticTrustOUIListRowStatus = _Hh3cWIPSStaticTrustOUIListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 13, 1, 2),
    _Hh3cWIPSStaticTrustOUIListRowStatus_Type()
)
hh3cWIPSStaticTrustOUIListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSStaticTrustOUIListRowStatus.setStatus("current")
_Hh3cWIPSStaticTrustVendorListCfgTable_Object = MibTable
hh3cWIPSStaticTrustVendorListCfgTable = _Hh3cWIPSStaticTrustVendorListCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 14)
)
if mibBuilder.loadTexts:
    hh3cWIPSStaticTrustVendorListCfgTable.setStatus("current")
_Hh3cWIPSStaticTrustVendorListCfgEntry_Object = MibTableRow
hh3cWIPSStaticTrustVendorListCfgEntry = _Hh3cWIPSStaticTrustVendorListCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 14, 1)
)
hh3cWIPSStaticTrustVendorListCfgEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSStaticTrustVendorListVendor"),
)
if mibBuilder.loadTexts:
    hh3cWIPSStaticTrustVendorListCfgEntry.setStatus("current")


class _Hh3cWIPSStaticTrustVendorListVendor_Type(OctetString):
    """Custom type hh3cWIPSStaticTrustVendorListVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cWIPSStaticTrustVendorListVendor_Type.__name__ = "OctetString"
_Hh3cWIPSStaticTrustVendorListVendor_Object = MibTableColumn
hh3cWIPSStaticTrustVendorListVendor = _Hh3cWIPSStaticTrustVendorListVendor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 14, 1, 1),
    _Hh3cWIPSStaticTrustVendorListVendor_Type()
)
hh3cWIPSStaticTrustVendorListVendor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSStaticTrustVendorListVendor.setStatus("current")
_Hh3cWIPSStaticTrustVendorListRowStatus_Type = RowStatus
_Hh3cWIPSStaticTrustVendorListRowStatus_Object = MibTableColumn
hh3cWIPSStaticTrustVendorListRowStatus = _Hh3cWIPSStaticTrustVendorListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 1, 14, 1, 2),
    _Hh3cWIPSStaticTrustVendorListRowStatus_Type()
)
hh3cWIPSStaticTrustVendorListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cWIPSStaticTrustVendorListRowStatus.setStatus("current")
_Hh3cWIPSDetectGroup_ObjectIdentity = ObjectIdentity
hh3cWIPSDetectGroup = _Hh3cWIPSDetectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2)
)
_Hh3cWIPSDctAPTable_Object = MibTable
hh3cWIPSDctAPTable = _Hh3cWIPSDctAPTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cWIPSDctAPTable.setStatus("current")
_Hh3cWIPSDctAPEntry_Object = MibTableRow
hh3cWIPSDctAPEntry = _Hh3cWIPSDctAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1)
)
hh3cWIPSDctAPEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctAPVSD"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctAPBSSID"),
)
if mibBuilder.loadTexts:
    hh3cWIPSDctAPEntry.setStatus("current")


class _Hh3cWIPSDctAPVSD_Type(OctetString):
    """Custom type hh3cWIPSDctAPVSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSDctAPVSD_Type.__name__ = "OctetString"
_Hh3cWIPSDctAPVSD_Object = MibTableColumn
hh3cWIPSDctAPVSD = _Hh3cWIPSDctAPVSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 1),
    _Hh3cWIPSDctAPVSD_Type()
)
hh3cWIPSDctAPVSD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPVSD.setStatus("current")
_Hh3cWIPSDctAPBSSID_Type = MacAddress
_Hh3cWIPSDctAPBSSID_Object = MibTableColumn
hh3cWIPSDctAPBSSID = _Hh3cWIPSDctAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 2),
    _Hh3cWIPSDctAPBSSID_Type()
)
hh3cWIPSDctAPBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPBSSID.setStatus("current")
_Hh3cWIPSDctAPRunningTime_Type = TimeTicks
_Hh3cWIPSDctAPRunningTime_Object = MibTableColumn
hh3cWIPSDctAPRunningTime = _Hh3cWIPSDctAPRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 3),
    _Hh3cWIPSDctAPRunningTime_Type()
)
hh3cWIPSDctAPRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPRunningTime.setStatus("current")
_Hh3cWIPSDctAPRunTmLastUpdateTm_Type = TimeTicks
_Hh3cWIPSDctAPRunTmLastUpdateTm_Object = MibTableColumn
hh3cWIPSDctAPRunTmLastUpdateTm = _Hh3cWIPSDctAPRunTmLastUpdateTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 4),
    _Hh3cWIPSDctAPRunTmLastUpdateTm_Type()
)
hh3cWIPSDctAPRunTmLastUpdateTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPRunTmLastUpdateTm.setStatus("current")
_Hh3cWIPSDctAPIsCountered_Type = TruthValue
_Hh3cWIPSDctAPIsCountered_Object = MibTableColumn
hh3cWIPSDctAPIsCountered = _Hh3cWIPSDctAPIsCountered_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 5),
    _Hh3cWIPSDctAPIsCountered_Type()
)
hh3cWIPSDctAPIsCountered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPIsCountered.setStatus("current")
_Hh3cWIPSDctAPWorkChannel_Type = Hh3cWIPSChannel
_Hh3cWIPSDctAPWorkChannel_Object = MibTableColumn
hh3cWIPSDctAPWorkChannel = _Hh3cWIPSDctAPWorkChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 6),
    _Hh3cWIPSDctAPWorkChannel_Type()
)
hh3cWIPSDctAPWorkChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPWorkChannel.setStatus("current")
_Hh3cWIPSDctAPRadioType_Type = Hh3cWIPSRadioType
_Hh3cWIPSDctAPRadioType_Object = MibTableColumn
hh3cWIPSDctAPRadioType = _Hh3cWIPSDctAPRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 7),
    _Hh3cWIPSDctAPRadioType_Type()
)
hh3cWIPSDctAPRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPRadioType.setStatus("current")
_Hh3cWIPSDctAPAuthMethod_Type = Hh3cWIPSAuthMethod
_Hh3cWIPSDctAPAuthMethod_Object = MibTableColumn
hh3cWIPSDctAPAuthMethod = _Hh3cWIPSDctAPAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 8),
    _Hh3cWIPSDctAPAuthMethod_Type()
)
hh3cWIPSDctAPAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPAuthMethod.setStatus("current")
_Hh3cWIPSDctAPEncryptMethod_Type = Hh3cWIPSEncryptMethod
_Hh3cWIPSDctAPEncryptMethod_Object = MibTableColumn
hh3cWIPSDctAPEncryptMethod = _Hh3cWIPSDctAPEncryptMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 9),
    _Hh3cWIPSDctAPEncryptMethod_Type()
)
hh3cWIPSDctAPEncryptMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPEncryptMethod.setStatus("current")
_Hh3cWIPSDctAPSecurity_Type = Hh3cWIPSAPSecurityType
_Hh3cWIPSDctAPSecurity_Object = MibTableColumn
hh3cWIPSDctAPSecurity = _Hh3cWIPSDctAPSecurity_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 10),
    _Hh3cWIPSDctAPSecurity_Type()
)
hh3cWIPSDctAPSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPSecurity.setStatus("current")


class _Hh3cWIPSDctAPSeverityLevel_Type(Unsigned32):
    """Custom type hh3cWIPSDctAPSeverityLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cWIPSDctAPSeverityLevel_Type.__name__ = "Unsigned32"
_Hh3cWIPSDctAPSeverityLevel_Object = MibTableColumn
hh3cWIPSDctAPSeverityLevel = _Hh3cWIPSDctAPSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 11),
    _Hh3cWIPSDctAPSeverityLevel_Type()
)
hh3cWIPSDctAPSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPSeverityLevel.setStatus("current")
_Hh3cWIPSDctAPLastDctTm_Type = TimeTicks
_Hh3cWIPSDctAPLastDctTm_Object = MibTableColumn
hh3cWIPSDctAPLastDctTm = _Hh3cWIPSDctAPLastDctTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 12),
    _Hh3cWIPSDctAPLastDctTm_Type()
)
hh3cWIPSDctAPLastDctTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPLastDctTm.setStatus("current")
_Hh3cWIPSDctAPFirstDctTm_Type = TimeTicks
_Hh3cWIPSDctAPFirstDctTm_Object = MibTableColumn
hh3cWIPSDctAPFirstDctTm = _Hh3cWIPSDctAPFirstDctTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 13),
    _Hh3cWIPSDctAPFirstDctTm_Type()
)
hh3cWIPSDctAPFirstDctTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPFirstDctTm.setStatus("current")


class _Hh3cWIPSDctAPAdd2BlackList_Type(TruthValue):
    """Custom type hh3cWIPSDctAPAdd2BlackList based on TruthValue"""


_Hh3cWIPSDctAPAdd2BlackList_Object = MibTableColumn
hh3cWIPSDctAPAdd2BlackList = _Hh3cWIPSDctAPAdd2BlackList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 14),
    _Hh3cWIPSDctAPAdd2BlackList_Type()
)
hh3cWIPSDctAPAdd2BlackList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPAdd2BlackList.setStatus("current")


class _Hh3cWIPSDctAPAdd2WhiteList_Type(TruthValue):
    """Custom type hh3cWIPSDctAPAdd2WhiteList based on TruthValue"""


_Hh3cWIPSDctAPAdd2WhiteList_Object = MibTableColumn
hh3cWIPSDctAPAdd2WhiteList = _Hh3cWIPSDctAPAdd2WhiteList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 15),
    _Hh3cWIPSDctAPAdd2WhiteList_Type()
)
hh3cWIPSDctAPAdd2WhiteList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPAdd2WhiteList.setStatus("current")


class _Hh3cWIPSDctAPAdd2IgnoreList_Type(TruthValue):
    """Custom type hh3cWIPSDctAPAdd2IgnoreList based on TruthValue"""


_Hh3cWIPSDctAPAdd2IgnoreList_Object = MibTableColumn
hh3cWIPSDctAPAdd2IgnoreList = _Hh3cWIPSDctAPAdd2IgnoreList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 16),
    _Hh3cWIPSDctAPAdd2IgnoreList_Type()
)
hh3cWIPSDctAPAdd2IgnoreList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPAdd2IgnoreList.setStatus("current")


class _Hh3cWIPSDctAPAdd2CtmList_Type(TruthValue):
    """Custom type hh3cWIPSDctAPAdd2CtmList based on TruthValue"""


_Hh3cWIPSDctAPAdd2CtmList_Object = MibTableColumn
hh3cWIPSDctAPAdd2CtmList = _Hh3cWIPSDctAPAdd2CtmList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 17),
    _Hh3cWIPSDctAPAdd2CtmList_Type()
)
hh3cWIPSDctAPAdd2CtmList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPAdd2CtmList.setStatus("current")
_Hh3cWIPSDctAPCategory_Type = Hh3cWIPSAPCategoryType
_Hh3cWIPSDctAPCategory_Object = MibTableColumn
hh3cWIPSDctAPCategory = _Hh3cWIPSDctAPCategory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 18),
    _Hh3cWIPSDctAPCategory_Type()
)
hh3cWIPSDctAPCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPCategory.setStatus("current")


class _Hh3cWIPSDctAPCategoryWay_Type(Hh3cWIPSDevCategoryWay):
    """Custom type hh3cWIPSDctAPCategoryWay based on Hh3cWIPSDevCategoryWay"""


_Hh3cWIPSDctAPCategoryWay_Object = MibTableColumn
hh3cWIPSDctAPCategoryWay = _Hh3cWIPSDctAPCategoryWay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 19),
    _Hh3cWIPSDctAPCategoryWay_Type()
)
hh3cWIPSDctAPCategoryWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPCategoryWay.setStatus("current")
_Hh3cWIPSDctAPStatus_Type = Hh3cWIPSDevStatus
_Hh3cWIPSDctAPStatus_Object = MibTableColumn
hh3cWIPSDctAPStatus = _Hh3cWIPSDctAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 20),
    _Hh3cWIPSDctAPStatus_Type()
)
hh3cWIPSDctAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPStatus.setStatus("current")


class _Hh3cWIPSDctAPSSID_Type(OctetString):
    """Custom type hh3cWIPSDctAPSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cWIPSDctAPSSID_Type.__name__ = "OctetString"
_Hh3cWIPSDctAPSSID_Object = MibTableColumn
hh3cWIPSDctAPSSID = _Hh3cWIPSDctAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 21),
    _Hh3cWIPSDctAPSSID_Type()
)
hh3cWIPSDctAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPSSID.setStatus("current")
_Hh3cWIPSDctAPAttachStaNum_Type = Integer32
_Hh3cWIPSDctAPAttachStaNum_Object = MibTableColumn
hh3cWIPSDctAPAttachStaNum = _Hh3cWIPSDctAPAttachStaNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 22),
    _Hh3cWIPSDctAPAttachStaNum_Type()
)
hh3cWIPSDctAPAttachStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPAttachStaNum.setStatus("current")
_Hh3cWIPSDctAPRptSensorNum_Type = Integer32
_Hh3cWIPSDctAPRptSensorNum_Object = MibTableColumn
hh3cWIPSDctAPRptSensorNum = _Hh3cWIPSDctAPRptSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 23),
    _Hh3cWIPSDctAPRptSensorNum_Type()
)
hh3cWIPSDctAPRptSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPRptSensorNum.setStatus("current")


class _Hh3cWIPSDctAPVendor_Type(OctetString):
    """Custom type hh3cWIPSDctAPVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cWIPSDctAPVendor_Type.__name__ = "OctetString"
_Hh3cWIPSDctAPVendor_Object = MibTableColumn
hh3cWIPSDctAPVendor = _Hh3cWIPSDctAPVendor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 1, 1, 24),
    _Hh3cWIPSDctAPVendor_Type()
)
hh3cWIPSDctAPVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPVendor.setStatus("current")
_Hh3cWIPSDctAPAttachStaTable_Object = MibTable
hh3cWIPSDctAPAttachStaTable = _Hh3cWIPSDctAPAttachStaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cWIPSDctAPAttachStaTable.setStatus("current")
_Hh3cWIPSDctAPAttachStaEntry_Object = MibTableRow
hh3cWIPSDctAPAttachStaEntry = _Hh3cWIPSDctAPAttachStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 2, 1)
)
hh3cWIPSDctAPAttachStaEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctAPVSD"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctAPBSSID"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctAPAttachStaMac"),
)
if mibBuilder.loadTexts:
    hh3cWIPSDctAPAttachStaEntry.setStatus("current")
_Hh3cWIPSDctAPAttachStaMac_Type = MacAddress
_Hh3cWIPSDctAPAttachStaMac_Object = MibTableColumn
hh3cWIPSDctAPAttachStaMac = _Hh3cWIPSDctAPAttachStaMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 2, 1, 1),
    _Hh3cWIPSDctAPAttachStaMac_Type()
)
hh3cWIPSDctAPAttachStaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPAttachStaMac.setStatus("current")
_Hh3cWIPSDctAPAttachStaRowStatus_Type = RowStatus
_Hh3cWIPSDctAPAttachStaRowStatus_Object = MibTableColumn
hh3cWIPSDctAPAttachStaRowStatus = _Hh3cWIPSDctAPAttachStaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 2, 1, 2),
    _Hh3cWIPSDctAPAttachStaRowStatus_Type()
)
hh3cWIPSDctAPAttachStaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPAttachStaRowStatus.setStatus("current")
_Hh3cWIPSDctAPRptSensorTable_Object = MibTable
hh3cWIPSDctAPRptSensorTable = _Hh3cWIPSDctAPRptSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cWIPSDctAPRptSensorTable.setStatus("current")
_Hh3cWIPSDctAPRptSensorEntry_Object = MibTableRow
hh3cWIPSDctAPRptSensorEntry = _Hh3cWIPSDctAPRptSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 3, 1)
)
hh3cWIPSDctAPRptSensorEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctAPVSD"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctAPBSSID"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctAPRptSensorName"),
)
if mibBuilder.loadTexts:
    hh3cWIPSDctAPRptSensorEntry.setStatus("current")


class _Hh3cWIPSDctAPRptSensorName_Type(OctetString):
    """Custom type hh3cWIPSDctAPRptSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cWIPSDctAPRptSensorName_Type.__name__ = "OctetString"
_Hh3cWIPSDctAPRptSensorName_Object = MibTableColumn
hh3cWIPSDctAPRptSensorName = _Hh3cWIPSDctAPRptSensorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 3, 1, 1),
    _Hh3cWIPSDctAPRptSensorName_Type()
)
hh3cWIPSDctAPRptSensorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPRptSensorName.setStatus("current")


class _Hh3cWIPSDctAPRptSensorRadioId_Type(Integer32):
    """Custom type hh3cWIPSDctAPRptSensorRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cWIPSDctAPRptSensorRadioId_Type.__name__ = "Integer32"
_Hh3cWIPSDctAPRptSensorRadioId_Object = MibTableColumn
hh3cWIPSDctAPRptSensorRadioId = _Hh3cWIPSDctAPRptSensorRadioId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 3, 1, 2),
    _Hh3cWIPSDctAPRptSensorRadioId_Type()
)
hh3cWIPSDctAPRptSensorRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPRptSensorRadioId.setStatus("current")


class _Hh3cWIPSDctAPRptRSSI_Type(Integer32):
    """Custom type hh3cWIPSDctAPRptRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_Hh3cWIPSDctAPRptRSSI_Type.__name__ = "Integer32"
_Hh3cWIPSDctAPRptRSSI_Object = MibTableColumn
hh3cWIPSDctAPRptRSSI = _Hh3cWIPSDctAPRptRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 3, 1, 3),
    _Hh3cWIPSDctAPRptRSSI_Type()
)
hh3cWIPSDctAPRptRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPRptRSSI.setStatus("current")
_Hh3cWIPSDctAPLastRptTm_Type = TimeTicks
_Hh3cWIPSDctAPLastRptTm_Object = MibTableColumn
hh3cWIPSDctAPLastRptTm = _Hh3cWIPSDctAPLastRptTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 3, 1, 4),
    _Hh3cWIPSDctAPLastRptTm_Type()
)
hh3cWIPSDctAPLastRptTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctAPLastRptTm.setStatus("current")
_Hh3cWIPSDctStaTable_Object = MibTable
hh3cWIPSDctStaTable = _Hh3cWIPSDctStaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cWIPSDctStaTable.setStatus("current")
_Hh3cWIPSDctStaEntry_Object = MibTableRow
hh3cWIPSDctStaEntry = _Hh3cWIPSDctStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1)
)
hh3cWIPSDctStaEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctStaVSD"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctStaMac"),
)
if mibBuilder.loadTexts:
    hh3cWIPSDctStaEntry.setStatus("current")


class _Hh3cWIPSDctStaVSD_Type(OctetString):
    """Custom type hh3cWIPSDctStaVSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSDctStaVSD_Type.__name__ = "OctetString"
_Hh3cWIPSDctStaVSD_Object = MibTableColumn
hh3cWIPSDctStaVSD = _Hh3cWIPSDctStaVSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 1),
    _Hh3cWIPSDctStaVSD_Type()
)
hh3cWIPSDctStaVSD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaVSD.setStatus("current")
_Hh3cWIPSDctStaMac_Type = MacAddress
_Hh3cWIPSDctStaMac_Object = MibTableColumn
hh3cWIPSDctStaMac = _Hh3cWIPSDctStaMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 2),
    _Hh3cWIPSDctStaMac_Type()
)
hh3cWIPSDctStaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaMac.setStatus("current")
_Hh3cWIPSDctStaAssocBSSID_Type = MacAddress
_Hh3cWIPSDctStaAssocBSSID_Object = MibTableColumn
hh3cWIPSDctStaAssocBSSID = _Hh3cWIPSDctStaAssocBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 3),
    _Hh3cWIPSDctStaAssocBSSID_Type()
)
hh3cWIPSDctStaAssocBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaAssocBSSID.setStatus("current")
_Hh3cWIPSDctStaStatus_Type = Hh3cWIPSDevStatus
_Hh3cWIPSDctStaStatus_Object = MibTableColumn
hh3cWIPSDctStaStatus = _Hh3cWIPSDctStaStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 4),
    _Hh3cWIPSDctStaStatus_Type()
)
hh3cWIPSDctStaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaStatus.setStatus("current")
_Hh3cWIPSDctStaCategory_Type = Hh3cWIPSClientCategoryType
_Hh3cWIPSDctStaCategory_Object = MibTableColumn
hh3cWIPSDctStaCategory = _Hh3cWIPSDctStaCategory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 5),
    _Hh3cWIPSDctStaCategory_Type()
)
hh3cWIPSDctStaCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaCategory.setStatus("current")
_Hh3cWIPSDctStaRadioType_Type = Hh3cWIPSRadioType
_Hh3cWIPSDctStaRadioType_Object = MibTableColumn
hh3cWIPSDctStaRadioType = _Hh3cWIPSDctStaRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 6),
    _Hh3cWIPSDctStaRadioType_Type()
)
hh3cWIPSDctStaRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaRadioType.setStatus("current")
_Hh3cWIPSDctStaWorkChannel_Type = Hh3cWIPSChannel
_Hh3cWIPSDctStaWorkChannel_Object = MibTableColumn
hh3cWIPSDctStaWorkChannel = _Hh3cWIPSDctStaWorkChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 7),
    _Hh3cWIPSDctStaWorkChannel_Type()
)
hh3cWIPSDctStaWorkChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaWorkChannel.setStatus("current")
_Hh3cWIPSDctStaIsCountered_Type = TruthValue
_Hh3cWIPSDctStaIsCountered_Object = MibTableColumn
hh3cWIPSDctStaIsCountered = _Hh3cWIPSDctStaIsCountered_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 8),
    _Hh3cWIPSDctStaIsCountered_Type()
)
hh3cWIPSDctStaIsCountered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaIsCountered.setStatus("current")


class _Hh3cWIPSDctStaAdd2BlackList_Type(TruthValue):
    """Custom type hh3cWIPSDctStaAdd2BlackList based on TruthValue"""


_Hh3cWIPSDctStaAdd2BlackList_Object = MibTableColumn
hh3cWIPSDctStaAdd2BlackList = _Hh3cWIPSDctStaAdd2BlackList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 9),
    _Hh3cWIPSDctStaAdd2BlackList_Type()
)
hh3cWIPSDctStaAdd2BlackList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaAdd2BlackList.setStatus("current")


class _Hh3cWIPSDctStaAdd2WhiteList_Type(TruthValue):
    """Custom type hh3cWIPSDctStaAdd2WhiteList based on TruthValue"""


_Hh3cWIPSDctStaAdd2WhiteList_Object = MibTableColumn
hh3cWIPSDctStaAdd2WhiteList = _Hh3cWIPSDctStaAdd2WhiteList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 10),
    _Hh3cWIPSDctStaAdd2WhiteList_Type()
)
hh3cWIPSDctStaAdd2WhiteList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaAdd2WhiteList.setStatus("current")


class _Hh3cWIPSDctStaAdd2IgnoreList_Type(TruthValue):
    """Custom type hh3cWIPSDctStaAdd2IgnoreList based on TruthValue"""


_Hh3cWIPSDctStaAdd2IgnoreList_Object = MibTableColumn
hh3cWIPSDctStaAdd2IgnoreList = _Hh3cWIPSDctStaAdd2IgnoreList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 11),
    _Hh3cWIPSDctStaAdd2IgnoreList_Type()
)
hh3cWIPSDctStaAdd2IgnoreList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaAdd2IgnoreList.setStatus("current")


class _Hh3cWIPSDctStaAdd2CtmList_Type(TruthValue):
    """Custom type hh3cWIPSDctStaAdd2CtmList based on TruthValue"""


_Hh3cWIPSDctStaAdd2CtmList_Object = MibTableColumn
hh3cWIPSDctStaAdd2CtmList = _Hh3cWIPSDctStaAdd2CtmList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 12),
    _Hh3cWIPSDctStaAdd2CtmList_Type()
)
hh3cWIPSDctStaAdd2CtmList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaAdd2CtmList.setStatus("current")
_Hh3cWIPSDctStaFirstDctTm_Type = TimeTicks
_Hh3cWIPSDctStaFirstDctTm_Object = MibTableColumn
hh3cWIPSDctStaFirstDctTm = _Hh3cWIPSDctStaFirstDctTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 13),
    _Hh3cWIPSDctStaFirstDctTm_Type()
)
hh3cWIPSDctStaFirstDctTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaFirstDctTm.setStatus("current")
_Hh3cWIPSDctStaLastDctTm_Type = TimeTicks
_Hh3cWIPSDctStaLastDctTm_Object = MibTableColumn
hh3cWIPSDctStaLastDctTm = _Hh3cWIPSDctStaLastDctTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 14),
    _Hh3cWIPSDctStaLastDctTm_Type()
)
hh3cWIPSDctStaLastDctTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaLastDctTm.setStatus("current")
_Hh3cWIPSDctStaRptSensorNum_Type = Integer32
_Hh3cWIPSDctStaRptSensorNum_Object = MibTableColumn
hh3cWIPSDctStaRptSensorNum = _Hh3cWIPSDctStaRptSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 15),
    _Hh3cWIPSDctStaRptSensorNum_Type()
)
hh3cWIPSDctStaRptSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaRptSensorNum.setStatus("current")


class _Hh3cWIPSDctStaState_Type(Integer32):
    """Custom type hh3cWIPSDctStaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("association", 2),
          ("authentication", 1),
          ("deauthentication", 6),
          ("disassociation", 5),
          ("eapLogoff", 4),
          ("eapSuccess", 3),
          ("unassociation", 7))
    )


_Hh3cWIPSDctStaState_Type.__name__ = "Integer32"
_Hh3cWIPSDctStaState_Object = MibTableColumn
hh3cWIPSDctStaState = _Hh3cWIPSDctStaState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 16),
    _Hh3cWIPSDctStaState_Type()
)
hh3cWIPSDctStaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaState.setStatus("current")


class _Hh3cWIPSDctStaVendor_Type(OctetString):
    """Custom type hh3cWIPSDctStaVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cWIPSDctStaVendor_Type.__name__ = "OctetString"
_Hh3cWIPSDctStaVendor_Object = MibTableColumn
hh3cWIPSDctStaVendor = _Hh3cWIPSDctStaVendor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 4, 1, 17),
    _Hh3cWIPSDctStaVendor_Type()
)
hh3cWIPSDctStaVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaVendor.setStatus("current")
_Hh3cWIPSDctStaRptSensorTable_Object = MibTable
hh3cWIPSDctStaRptSensorTable = _Hh3cWIPSDctStaRptSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cWIPSDctStaRptSensorTable.setStatus("current")
_Hh3cWIPSDctStaRptSensorEntry_Object = MibTableRow
hh3cWIPSDctStaRptSensorEntry = _Hh3cWIPSDctStaRptSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 5, 1)
)
hh3cWIPSDctStaRptSensorEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctStaVSD"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctStaMac"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctStaRtpSensorName"),
)
if mibBuilder.loadTexts:
    hh3cWIPSDctStaRptSensorEntry.setStatus("current")


class _Hh3cWIPSDctStaRtpSensorName_Type(OctetString):
    """Custom type hh3cWIPSDctStaRtpSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cWIPSDctStaRtpSensorName_Type.__name__ = "OctetString"
_Hh3cWIPSDctStaRtpSensorName_Object = MibTableColumn
hh3cWIPSDctStaRtpSensorName = _Hh3cWIPSDctStaRtpSensorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 5, 1, 1),
    _Hh3cWIPSDctStaRtpSensorName_Type()
)
hh3cWIPSDctStaRtpSensorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaRtpSensorName.setStatus("current")


class _Hh3cWIPSDctStaRptSensorRadioId_Type(Integer32):
    """Custom type hh3cWIPSDctStaRptSensorRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cWIPSDctStaRptSensorRadioId_Type.__name__ = "Integer32"
_Hh3cWIPSDctStaRptSensorRadioId_Object = MibTableColumn
hh3cWIPSDctStaRptSensorRadioId = _Hh3cWIPSDctStaRptSensorRadioId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 5, 1, 2),
    _Hh3cWIPSDctStaRptSensorRadioId_Type()
)
hh3cWIPSDctStaRptSensorRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaRptSensorRadioId.setStatus("current")
_Hh3cWIPSDctStaRptRSSI_Type = Integer32
_Hh3cWIPSDctStaRptRSSI_Object = MibTableColumn
hh3cWIPSDctStaRptRSSI = _Hh3cWIPSDctStaRptRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 5, 1, 3),
    _Hh3cWIPSDctStaRptRSSI_Type()
)
hh3cWIPSDctStaRptRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaRptRSSI.setStatus("current")
_Hh3cWIPSDctStaLastRptTm_Type = TimeTicks
_Hh3cWIPSDctStaLastRptTm_Object = MibTableColumn
hh3cWIPSDctStaLastRptTm = _Hh3cWIPSDctStaLastRptTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 5, 1, 4),
    _Hh3cWIPSDctStaLastRptTm_Type()
)
hh3cWIPSDctStaLastRptTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctStaLastRptTm.setStatus("current")
_Hh3cWIPSDctSSIDTable_Object = MibTable
hh3cWIPSDctSSIDTable = _Hh3cWIPSDctSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cWIPSDctSSIDTable.setStatus("current")
_Hh3cWIPSDctSSIDEntry_Object = MibTableRow
hh3cWIPSDctSSIDEntry = _Hh3cWIPSDctSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 6, 1)
)
hh3cWIPSDctSSIDEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctNetworkVSD"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctNetworkSSID"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctNetworkCfg"),
)
if mibBuilder.loadTexts:
    hh3cWIPSDctSSIDEntry.setStatus("current")


class _Hh3cWIPSDctNetworkVSD_Type(OctetString):
    """Custom type hh3cWIPSDctNetworkVSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSDctNetworkVSD_Type.__name__ = "OctetString"
_Hh3cWIPSDctNetworkVSD_Object = MibTableColumn
hh3cWIPSDctNetworkVSD = _Hh3cWIPSDctNetworkVSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 6, 1, 1),
    _Hh3cWIPSDctNetworkVSD_Type()
)
hh3cWIPSDctNetworkVSD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctNetworkVSD.setStatus("current")


class _Hh3cWIPSDctNetworkSSID_Type(OctetString):
    """Custom type hh3cWIPSDctNetworkSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSDctNetworkSSID_Type.__name__ = "OctetString"
_Hh3cWIPSDctNetworkSSID_Object = MibTableColumn
hh3cWIPSDctNetworkSSID = _Hh3cWIPSDctNetworkSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 6, 1, 2),
    _Hh3cWIPSDctNetworkSSID_Type()
)
hh3cWIPSDctNetworkSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctNetworkSSID.setStatus("current")
_Hh3cWIPSDctNetworkCfg_Type = Unsigned32
_Hh3cWIPSDctNetworkCfg_Object = MibTableColumn
hh3cWIPSDctNetworkCfg = _Hh3cWIPSDctNetworkCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 6, 1, 3),
    _Hh3cWIPSDctNetworkCfg_Type()
)
hh3cWIPSDctNetworkCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctNetworkCfg.setStatus("current")
_Hh3cWIPSDctNetworkFirstRptTm_Type = TimeTicks
_Hh3cWIPSDctNetworkFirstRptTm_Object = MibTableColumn
hh3cWIPSDctNetworkFirstRptTm = _Hh3cWIPSDctNetworkFirstRptTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 6, 1, 4),
    _Hh3cWIPSDctNetworkFirstRptTm_Type()
)
hh3cWIPSDctNetworkFirstRptTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctNetworkFirstRptTm.setStatus("current")
_Hh3cWIPSDctNetworkLastRptTm_Type = TimeTicks
_Hh3cWIPSDctNetworkLastRptTm_Object = MibTableColumn
hh3cWIPSDctNetworkLastRptTm = _Hh3cWIPSDctNetworkLastRptTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 6, 1, 5),
    _Hh3cWIPSDctNetworkLastRptTm_Type()
)
hh3cWIPSDctNetworkLastRptTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctNetworkLastRptTm.setStatus("current")
_Hh3cWIPSDctNetworkStatus_Type = Hh3cWIPSDevStatus
_Hh3cWIPSDctNetworkStatus_Object = MibTableColumn
hh3cWIPSDctNetworkStatus = _Hh3cWIPSDctNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 6, 1, 6),
    _Hh3cWIPSDctNetworkStatus_Type()
)
hh3cWIPSDctNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctNetworkStatus.setStatus("current")


class _Hh3cWIPSDctNetworkSSIDHide_Type(TruthValue):
    """Custom type hh3cWIPSDctNetworkSSIDHide based on TruthValue"""


_Hh3cWIPSDctNetworkSSIDHide_Object = MibTableColumn
hh3cWIPSDctNetworkSSIDHide = _Hh3cWIPSDctNetworkSSIDHide_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 6, 1, 7),
    _Hh3cWIPSDctNetworkSSIDHide_Type()
)
hh3cWIPSDctNetworkSSIDHide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctNetworkSSIDHide.setStatus("current")
_Hh3cWIPSDctNetworkBSSNum_Type = Integer32
_Hh3cWIPSDctNetworkBSSNum_Object = MibTableColumn
hh3cWIPSDctNetworkBSSNum = _Hh3cWIPSDctNetworkBSSNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 6, 1, 8),
    _Hh3cWIPSDctNetworkBSSNum_Type()
)
hh3cWIPSDctNetworkBSSNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctNetworkBSSNum.setStatus("current")
_Hh3cWIPSDctSSIDBSSTable_Object = MibTable
hh3cWIPSDctSSIDBSSTable = _Hh3cWIPSDctSSIDBSSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cWIPSDctSSIDBSSTable.setStatus("current")
_Hh3cWIPSDctSSIDBSSEntry_Object = MibTableRow
hh3cWIPSDctSSIDBSSEntry = _Hh3cWIPSDctSSIDBSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 7, 1)
)
hh3cWIPSDctSSIDBSSEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctNetworkVSD"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctNetworkSSID"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctNetworkCfg"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctNetworkBSSID"),
)
if mibBuilder.loadTexts:
    hh3cWIPSDctSSIDBSSEntry.setStatus("current")
_Hh3cWIPSDctNetworkBSSID_Type = MacAddress
_Hh3cWIPSDctNetworkBSSID_Object = MibTableColumn
hh3cWIPSDctNetworkBSSID = _Hh3cWIPSDctNetworkBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 7, 1, 1),
    _Hh3cWIPSDctNetworkBSSID_Type()
)
hh3cWIPSDctNetworkBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctNetworkBSSID.setStatus("current")
_Hh3cWIPSDctNetworkBSSWorkChl_Type = Hh3cWIPSChannel
_Hh3cWIPSDctNetworkBSSWorkChl_Object = MibTableColumn
hh3cWIPSDctNetworkBSSWorkChl = _Hh3cWIPSDctNetworkBSSWorkChl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 7, 1, 2),
    _Hh3cWIPSDctNetworkBSSWorkChl_Type()
)
hh3cWIPSDctNetworkBSSWorkChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctNetworkBSSWorkChl.setStatus("current")
_Hh3cWIPSDctNetworkBSSStaNum_Type = Integer32
_Hh3cWIPSDctNetworkBSSStaNum_Object = MibTableColumn
hh3cWIPSDctNetworkBSSStaNum = _Hh3cWIPSDctNetworkBSSStaNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 7, 1, 3),
    _Hh3cWIPSDctNetworkBSSStaNum_Type()
)
hh3cWIPSDctNetworkBSSStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctNetworkBSSStaNum.setStatus("current")
_Hh3cWIPSBlockListTable_Object = MibTable
hh3cWIPSBlockListTable = _Hh3cWIPSBlockListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cWIPSBlockListTable.setStatus("current")
_Hh3cWIPSBlockListEntry_Object = MibTableRow
hh3cWIPSBlockListEntry = _Hh3cWIPSBlockListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 8, 1)
)
hh3cWIPSBlockListEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSBlockListMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cWIPSBlockListEntry.setStatus("current")
_Hh3cWIPSBlockListMacAddress_Type = MacAddress
_Hh3cWIPSBlockListMacAddress_Object = MibTableColumn
hh3cWIPSBlockListMacAddress = _Hh3cWIPSBlockListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 8, 1, 1),
    _Hh3cWIPSBlockListMacAddress_Type()
)
hh3cWIPSBlockListMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSBlockListMacAddress.setStatus("current")


class _Hh3cWIPSBlockListStatus_Type(Integer32):
    """Custom type hh3cWIPSBlockListStatus based on Integer32"""
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


_Hh3cWIPSBlockListStatus_Type.__name__ = "Integer32"
_Hh3cWIPSBlockListStatus_Object = MibTableColumn
hh3cWIPSBlockListStatus = _Hh3cWIPSBlockListStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 8, 1, 2),
    _Hh3cWIPSBlockListStatus_Type()
)
hh3cWIPSBlockListStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSBlockListStatus.setStatus("current")
_Hh3cWIPSChannelTable_Object = MibTable
hh3cWIPSChannelTable = _Hh3cWIPSChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 9)
)
if mibBuilder.loadTexts:
    hh3cWIPSChannelTable.setStatus("current")
_Hh3cWIPSChannelEntry_Object = MibTableRow
hh3cWIPSChannelEntry = _Hh3cWIPSChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 9, 1)
)
hh3cWIPSChannelEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSChannelNum"),
)
if mibBuilder.loadTexts:
    hh3cWIPSChannelEntry.setStatus("current")
_Hh3cWIPSChannelNum_Type = Hh3cWIPSChannel
_Hh3cWIPSChannelNum_Object = MibTableColumn
hh3cWIPSChannelNum = _Hh3cWIPSChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 9, 1, 1),
    _Hh3cWIPSChannelNum_Type()
)
hh3cWIPSChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSChannelNum.setStatus("current")
_Hh3cWIPSChannelRadioType_Type = Hh3cWIPSRadioType
_Hh3cWIPSChannelRadioType_Object = MibTableColumn
hh3cWIPSChannelRadioType = _Hh3cWIPSChannelRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 9, 1, 2),
    _Hh3cWIPSChannelRadioType_Type()
)
hh3cWIPSChannelRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChannelRadioType.setStatus("current")
_Hh3cWIPSChannelIsPermitted_Type = TruthValue
_Hh3cWIPSChannelIsPermitted_Object = MibTableColumn
hh3cWIPSChannelIsPermitted = _Hh3cWIPSChannelIsPermitted_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 9, 1, 3),
    _Hh3cWIPSChannelIsPermitted_Type()
)
hh3cWIPSChannelIsPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChannelIsPermitted.setStatus("current")
_Hh3cWIPSChannelLastRptTm_Type = TimeTicks
_Hh3cWIPSChannelLastRptTm_Object = MibTableColumn
hh3cWIPSChannelLastRptTm = _Hh3cWIPSChannelLastRptTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 9, 1, 4),
    _Hh3cWIPSChannelLastRptTm_Type()
)
hh3cWIPSChannelLastRptTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChannelLastRptTm.setStatus("current")
_Hh3cWIPSCountermeasureListTable_Object = MibTable
hh3cWIPSCountermeasureListTable = _Hh3cWIPSCountermeasureListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 10)
)
if mibBuilder.loadTexts:
    hh3cWIPSCountermeasureListTable.setStatus("current")
_Hh3cWIPSCountermeasureListEntry_Object = MibTableRow
hh3cWIPSCountermeasureListEntry = _Hh3cWIPSCountermeasureListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 10, 1)
)
hh3cWIPSCountermeasureListEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSCtmListMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cWIPSCountermeasureListEntry.setStatus("current")
_Hh3cWIPSCtmListMacAddress_Type = MacAddress
_Hh3cWIPSCtmListMacAddress_Object = MibTableColumn
hh3cWIPSCtmListMacAddress = _Hh3cWIPSCtmListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 10, 1, 1),
    _Hh3cWIPSCtmListMacAddress_Type()
)
hh3cWIPSCtmListMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSCtmListMacAddress.setStatus("current")
_Hh3cWIPSCtmListLastestWorkChl_Type = Hh3cWIPSChannel
_Hh3cWIPSCtmListLastestWorkChl_Object = MibTableColumn
hh3cWIPSCtmListLastestWorkChl = _Hh3cWIPSCtmListLastestWorkChl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 10, 1, 2),
    _Hh3cWIPSCtmListLastestWorkChl_Type()
)
hh3cWIPSCtmListLastestWorkChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSCtmListLastestWorkChl.setStatus("current")
_Hh3cWIPSCtmListFirstTm_Type = TimeTicks
_Hh3cWIPSCtmListFirstTm_Object = MibTableColumn
hh3cWIPSCtmListFirstTm = _Hh3cWIPSCtmListFirstTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 10, 1, 3),
    _Hh3cWIPSCtmListFirstTm_Type()
)
hh3cWIPSCtmListFirstTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSCtmListFirstTm.setStatus("current")
_Hh3cWIPSCtmListLastTm_Type = TimeTicks
_Hh3cWIPSCtmListLastTm_Object = MibTableColumn
hh3cWIPSCtmListLastTm = _Hh3cWIPSCtmListLastTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 10, 1, 4),
    _Hh3cWIPSCtmListLastTm_Type()
)
hh3cWIPSCtmListLastTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSCtmListLastTm.setStatus("current")
_Hh3cWIPSCtmListQurCnt_Type = Integer32
_Hh3cWIPSCtmListQurCnt_Object = MibTableColumn
hh3cWIPSCtmListQurCnt = _Hh3cWIPSCtmListQurCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 10, 1, 5),
    _Hh3cWIPSCtmListQurCnt_Type()
)
hh3cWIPSCtmListQurCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSCtmListQurCnt.setStatus("current")
_Hh3cWIPSCtmListSensorNum_Type = Integer32
_Hh3cWIPSCtmListSensorNum_Object = MibTableColumn
hh3cWIPSCtmListSensorNum = _Hh3cWIPSCtmListSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 10, 1, 6),
    _Hh3cWIPSCtmListSensorNum_Type()
)
hh3cWIPSCtmListSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSCtmListSensorNum.setStatus("current")
_Hh3cWIPSIgnoreListTable_Object = MibTable
hh3cWIPSIgnoreListTable = _Hh3cWIPSIgnoreListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 11)
)
if mibBuilder.loadTexts:
    hh3cWIPSIgnoreListTable.setStatus("current")
_Hh3cWIPSIgnoreListEntry_Object = MibTableRow
hh3cWIPSIgnoreListEntry = _Hh3cWIPSIgnoreListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 11, 1)
)
hh3cWIPSIgnoreListEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSIgnoreListMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cWIPSIgnoreListEntry.setStatus("current")
_Hh3cWIPSIgnoreListMacAddress_Type = MacAddress
_Hh3cWIPSIgnoreListMacAddress_Object = MibTableColumn
hh3cWIPSIgnoreListMacAddress = _Hh3cWIPSIgnoreListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 11, 1, 1),
    _Hh3cWIPSIgnoreListMacAddress_Type()
)
hh3cWIPSIgnoreListMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSIgnoreListMacAddress.setStatus("current")
_Hh3cWIPSIgnoreListFirstIgnoreTm_Type = TimeTicks
_Hh3cWIPSIgnoreListFirstIgnoreTm_Object = MibTableColumn
hh3cWIPSIgnoreListFirstIgnoreTm = _Hh3cWIPSIgnoreListFirstIgnoreTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 11, 1, 2),
    _Hh3cWIPSIgnoreListFirstIgnoreTm_Type()
)
hh3cWIPSIgnoreListFirstIgnoreTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSIgnoreListFirstIgnoreTm.setStatus("current")
_Hh3cWIPSIgnoreListLastIgnoreTm_Type = TimeTicks
_Hh3cWIPSIgnoreListLastIgnoreTm_Object = MibTableColumn
hh3cWIPSIgnoreListLastIgnoreTm = _Hh3cWIPSIgnoreListLastIgnoreTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 11, 1, 3),
    _Hh3cWIPSIgnoreListLastIgnoreTm_Type()
)
hh3cWIPSIgnoreListLastIgnoreTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSIgnoreListLastIgnoreTm.setStatus("current")
_Hh3cWIPSIgnoreListIgnoreCnt_Type = Integer32
_Hh3cWIPSIgnoreListIgnoreCnt_Object = MibTableColumn
hh3cWIPSIgnoreListIgnoreCnt = _Hh3cWIPSIgnoreListIgnoreCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 11, 1, 4),
    _Hh3cWIPSIgnoreListIgnoreCnt_Type()
)
hh3cWIPSIgnoreListIgnoreCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSIgnoreListIgnoreCnt.setStatus("current")
_Hh3cWIPSTrustListTable_Object = MibTable
hh3cWIPSTrustListTable = _Hh3cWIPSTrustListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 12)
)
if mibBuilder.loadTexts:
    hh3cWIPSTrustListTable.setStatus("current")
_Hh3cWIPSTrustListEntry_Object = MibTableRow
hh3cWIPSTrustListEntry = _Hh3cWIPSTrustListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 12, 1)
)
hh3cWIPSTrustListEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSTrustListMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cWIPSTrustListEntry.setStatus("current")
_Hh3cWIPSTrustListMacAddress_Type = MacAddress
_Hh3cWIPSTrustListMacAddress_Object = MibTableColumn
hh3cWIPSTrustListMacAddress = _Hh3cWIPSTrustListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 12, 1, 1),
    _Hh3cWIPSTrustListMacAddress_Type()
)
hh3cWIPSTrustListMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSTrustListMacAddress.setStatus("current")


class _Hh3cWIPSTrustListStatus_Type(Integer32):
    """Custom type hh3cWIPSTrustListStatus based on Integer32"""
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


_Hh3cWIPSTrustListStatus_Type.__name__ = "Integer32"
_Hh3cWIPSTrustListStatus_Object = MibTableColumn
hh3cWIPSTrustListStatus = _Hh3cWIPSTrustListStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 12, 1, 2),
    _Hh3cWIPSTrustListStatus_Type()
)
hh3cWIPSTrustListStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSTrustListStatus.setStatus("current")
_Hh3cWIPSChlStatTable_Object = MibTable
hh3cWIPSChlStatTable = _Hh3cWIPSChlStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13)
)
if mibBuilder.loadTexts:
    hh3cWIPSChlStatTable.setStatus("current")
_Hh3cWIPSChlStatEntry_Object = MibTableRow
hh3cWIPSChlStatEntry = _Hh3cWIPSChlStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1)
)
hh3cWIPSChlStatEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSChlStatSensorMacAddr"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSChlStatChannel"),
)
if mibBuilder.loadTexts:
    hh3cWIPSChlStatEntry.setStatus("current")
_Hh3cWIPSChlStatSensorMacAddr_Type = MacAddress
_Hh3cWIPSChlStatSensorMacAddr_Object = MibTableColumn
hh3cWIPSChlStatSensorMacAddr = _Hh3cWIPSChlStatSensorMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 1),
    _Hh3cWIPSChlStatSensorMacAddr_Type()
)
hh3cWIPSChlStatSensorMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatSensorMacAddr.setStatus("current")
_Hh3cWIPSChlStatChannel_Type = Hh3cWIPSChannel
_Hh3cWIPSChlStatChannel_Object = MibTableColumn
hh3cWIPSChlStatChannel = _Hh3cWIPSChlStatChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 2),
    _Hh3cWIPSChlStatChannel_Type()
)
hh3cWIPSChlStatChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatChannel.setStatus("current")


class _Hh3cWIPSChlStatTotalPkt_Type(Counter64):
    """Custom type hh3cWIPSChlStatTotalPkt based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatTotalPkt_Object = MibTableColumn
hh3cWIPSChlStatTotalPkt = _Hh3cWIPSChlStatTotalPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 3),
    _Hh3cWIPSChlStatTotalPkt_Type()
)
hh3cWIPSChlStatTotalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatTotalPkt.setStatus("current")


class _Hh3cWIPSChlStatTotalByte_Type(Counter64):
    """Custom type hh3cWIPSChlStatTotalByte based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatTotalByte_Object = MibTableColumn
hh3cWIPSChlStatTotalByte = _Hh3cWIPSChlStatTotalByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 4),
    _Hh3cWIPSChlStatTotalByte_Type()
)
hh3cWIPSChlStatTotalByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatTotalByte.setStatus("current")


class _Hh3cWIPSChlStatBmcastPkt_Type(Counter64):
    """Custom type hh3cWIPSChlStatBmcastPkt based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatBmcastPkt_Object = MibTableColumn
hh3cWIPSChlStatBmcastPkt = _Hh3cWIPSChlStatBmcastPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 5),
    _Hh3cWIPSChlStatBmcastPkt_Type()
)
hh3cWIPSChlStatBmcastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatBmcastPkt.setStatus("current")


class _Hh3cWIPSChlStatBmcastByte_Type(Counter64):
    """Custom type hh3cWIPSChlStatBmcastByte based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatBmcastByte_Object = MibTableColumn
hh3cWIPSChlStatBmcastByte = _Hh3cWIPSChlStatBmcastByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 6),
    _Hh3cWIPSChlStatBmcastByte_Type()
)
hh3cWIPSChlStatBmcastByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatBmcastByte.setStatus("current")


class _Hh3cWIPSChlStatUnicastPkt_Type(Counter64):
    """Custom type hh3cWIPSChlStatUnicastPkt based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatUnicastPkt_Object = MibTableColumn
hh3cWIPSChlStatUnicastPkt = _Hh3cWIPSChlStatUnicastPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 7),
    _Hh3cWIPSChlStatUnicastPkt_Type()
)
hh3cWIPSChlStatUnicastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatUnicastPkt.setStatus("current")


class _Hh3cWIPSChlStatUnicastByte_Type(Counter64):
    """Custom type hh3cWIPSChlStatUnicastByte based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatUnicastByte_Object = MibTableColumn
hh3cWIPSChlStatUnicastByte = _Hh3cWIPSChlStatUnicastByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 8),
    _Hh3cWIPSChlStatUnicastByte_Type()
)
hh3cWIPSChlStatUnicastByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatUnicastByte.setStatus("current")


class _Hh3cWIPSChlStatManagement_Type(Counter64):
    """Custom type hh3cWIPSChlStatManagement based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatManagement_Object = MibTableColumn
hh3cWIPSChlStatManagement = _Hh3cWIPSChlStatManagement_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 9),
    _Hh3cWIPSChlStatManagement_Type()
)
hh3cWIPSChlStatManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatManagement.setStatus("current")


class _Hh3cWIPSChlStatControl_Type(Counter64):
    """Custom type hh3cWIPSChlStatControl based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatControl_Object = MibTableColumn
hh3cWIPSChlStatControl = _Hh3cWIPSChlStatControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 10),
    _Hh3cWIPSChlStatControl_Type()
)
hh3cWIPSChlStatControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatControl.setStatus("current")


class _Hh3cWIPSChlStatData_Type(Counter64):
    """Custom type hh3cWIPSChlStatData based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatData_Object = MibTableColumn
hh3cWIPSChlStatData = _Hh3cWIPSChlStatData_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 11),
    _Hh3cWIPSChlStatData_Type()
)
hh3cWIPSChlStatData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatData.setStatus("current")


class _Hh3cWIPSChlStatBeacon_Type(Counter64):
    """Custom type hh3cWIPSChlStatBeacon based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatBeacon_Object = MibTableColumn
hh3cWIPSChlStatBeacon = _Hh3cWIPSChlStatBeacon_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 12),
    _Hh3cWIPSChlStatBeacon_Type()
)
hh3cWIPSChlStatBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatBeacon.setStatus("current")


class _Hh3cWIPSChlStatRTS_Type(Counter64):
    """Custom type hh3cWIPSChlStatRTS based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatRTS_Object = MibTableColumn
hh3cWIPSChlStatRTS = _Hh3cWIPSChlStatRTS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 13),
    _Hh3cWIPSChlStatRTS_Type()
)
hh3cWIPSChlStatRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatRTS.setStatus("current")


class _Hh3cWIPSChlStatCTS_Type(Counter64):
    """Custom type hh3cWIPSChlStatCTS based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatCTS_Object = MibTableColumn
hh3cWIPSChlStatCTS = _Hh3cWIPSChlStatCTS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 14),
    _Hh3cWIPSChlStatCTS_Type()
)
hh3cWIPSChlStatCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatCTS.setStatus("current")


class _Hh3cWIPSChlStatProbeRequest_Type(Counter64):
    """Custom type hh3cWIPSChlStatProbeRequest based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatProbeRequest_Object = MibTableColumn
hh3cWIPSChlStatProbeRequest = _Hh3cWIPSChlStatProbeRequest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 15),
    _Hh3cWIPSChlStatProbeRequest_Type()
)
hh3cWIPSChlStatProbeRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatProbeRequest.setStatus("current")


class _Hh3cWIPSChlStatProbeResponse_Type(Counter64):
    """Custom type hh3cWIPSChlStatProbeResponse based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatProbeResponse_Object = MibTableColumn
hh3cWIPSChlStatProbeResponse = _Hh3cWIPSChlStatProbeResponse_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 16),
    _Hh3cWIPSChlStatProbeResponse_Type()
)
hh3cWIPSChlStatProbeResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatProbeResponse.setStatus("current")


class _Hh3cWIPSChlStatFragment_Type(Counter64):
    """Custom type hh3cWIPSChlStatFragment based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatFragment_Object = MibTableColumn
hh3cWIPSChlStatFragment = _Hh3cWIPSChlStatFragment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 17),
    _Hh3cWIPSChlStatFragment_Type()
)
hh3cWIPSChlStatFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatFragment.setStatus("current")


class _Hh3cWIPSChlStatRetry_Type(Counter64):
    """Custom type hh3cWIPSChlStatRetry based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatRetry_Object = MibTableColumn
hh3cWIPSChlStatRetry = _Hh3cWIPSChlStatRetry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 18),
    _Hh3cWIPSChlStatRetry_Type()
)
hh3cWIPSChlStatRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatRetry.setStatus("current")


class _Hh3cWIPSChlStatEapSuccess_Type(Counter64):
    """Custom type hh3cWIPSChlStatEapSuccess based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatEapSuccess_Object = MibTableColumn
hh3cWIPSChlStatEapSuccess = _Hh3cWIPSChlStatEapSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 19),
    _Hh3cWIPSChlStatEapSuccess_Type()
)
hh3cWIPSChlStatEapSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatEapSuccess.setStatus("current")


class _Hh3cWIPSChlStatEapFailure_Type(Counter64):
    """Custom type hh3cWIPSChlStatEapFailure based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatEapFailure_Object = MibTableColumn
hh3cWIPSChlStatEapFailure = _Hh3cWIPSChlStatEapFailure_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 20),
    _Hh3cWIPSChlStatEapFailure_Type()
)
hh3cWIPSChlStatEapFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatEapFailure.setStatus("current")


class _Hh3cWIPSChlStatEapolStart_Type(Counter64):
    """Custom type hh3cWIPSChlStatEapolStart based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatEapolStart_Object = MibTableColumn
hh3cWIPSChlStatEapolStart = _Hh3cWIPSChlStatEapolStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 21),
    _Hh3cWIPSChlStatEapolStart_Type()
)
hh3cWIPSChlStatEapolStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatEapolStart.setStatus("current")


class _Hh3cWIPSChlStatEapolLogoff_Type(Counter64):
    """Custom type hh3cWIPSChlStatEapolLogoff based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatEapolLogoff_Object = MibTableColumn
hh3cWIPSChlStatEapolLogoff = _Hh3cWIPSChlStatEapolLogoff_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 22),
    _Hh3cWIPSChlStatEapolLogoff_Type()
)
hh3cWIPSChlStatEapolLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatEapolLogoff.setStatus("current")


class _Hh3cWIPSChlStatAssocRequest_Type(Counter64):
    """Custom type hh3cWIPSChlStatAssocRequest based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatAssocRequest_Object = MibTableColumn
hh3cWIPSChlStatAssocRequest = _Hh3cWIPSChlStatAssocRequest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 23),
    _Hh3cWIPSChlStatAssocRequest_Type()
)
hh3cWIPSChlStatAssocRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatAssocRequest.setStatus("current")


class _Hh3cWIPSChlStatAssocResponse_Type(Counter64):
    """Custom type hh3cWIPSChlStatAssocResponse based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatAssocResponse_Object = MibTableColumn
hh3cWIPSChlStatAssocResponse = _Hh3cWIPSChlStatAssocResponse_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 24),
    _Hh3cWIPSChlStatAssocResponse_Type()
)
hh3cWIPSChlStatAssocResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatAssocResponse.setStatus("current")


class _Hh3cWIPSChlStatUnicastDisassoc_Type(Counter64):
    """Custom type hh3cWIPSChlStatUnicastDisassoc based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatUnicastDisassoc_Object = MibTableColumn
hh3cWIPSChlStatUnicastDisassoc = _Hh3cWIPSChlStatUnicastDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 25),
    _Hh3cWIPSChlStatUnicastDisassoc_Type()
)
hh3cWIPSChlStatUnicastDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatUnicastDisassoc.setStatus("current")


class _Hh3cWIPSChlStatBroadcastDisassoc_Type(Counter64):
    """Custom type hh3cWIPSChlStatBroadcastDisassoc based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatBroadcastDisassoc_Object = MibTableColumn
hh3cWIPSChlStatBroadcastDisassoc = _Hh3cWIPSChlStatBroadcastDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 26),
    _Hh3cWIPSChlStatBroadcastDisassoc_Type()
)
hh3cWIPSChlStatBroadcastDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatBroadcastDisassoc.setStatus("current")


class _Hh3cWIPSChlStatAuthentication_Type(Counter64):
    """Custom type hh3cWIPSChlStatAuthentication based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatAuthentication_Object = MibTableColumn
hh3cWIPSChlStatAuthentication = _Hh3cWIPSChlStatAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 27),
    _Hh3cWIPSChlStatAuthentication_Type()
)
hh3cWIPSChlStatAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatAuthentication.setStatus("current")


class _Hh3cWIPSChlStatUnicastDeauthen_Type(Counter64):
    """Custom type hh3cWIPSChlStatUnicastDeauthen based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatUnicastDeauthen_Object = MibTableColumn
hh3cWIPSChlStatUnicastDeauthen = _Hh3cWIPSChlStatUnicastDeauthen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 28),
    _Hh3cWIPSChlStatUnicastDeauthen_Type()
)
hh3cWIPSChlStatUnicastDeauthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatUnicastDeauthen.setStatus("current")


class _Hh3cWIPSChlStatBroadcastDeauthen_Type(Counter64):
    """Custom type hh3cWIPSChlStatBroadcastDeauthen based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatBroadcastDeauthen_Object = MibTableColumn
hh3cWIPSChlStatBroadcastDeauthen = _Hh3cWIPSChlStatBroadcastDeauthen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 29),
    _Hh3cWIPSChlStatBroadcastDeauthen_Type()
)
hh3cWIPSChlStatBroadcastDeauthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatBroadcastDeauthen.setStatus("current")


class _Hh3cWIPSChlStatMalformed_Type(Counter64):
    """Custom type hh3cWIPSChlStatMalformed based on Counter64"""
    defaultValue = 0


_Hh3cWIPSChlStatMalformed_Object = MibTableColumn
hh3cWIPSChlStatMalformed = _Hh3cWIPSChlStatMalformed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 13, 1, 30),
    _Hh3cWIPSChlStatMalformed_Type()
)
hh3cWIPSChlStatMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSChlStatMalformed.setStatus("current")
_Hh3cWIPSDevStatTable_Object = MibTable
hh3cWIPSDevStatTable = _Hh3cWIPSDevStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14)
)
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTable.setStatus("current")
_Hh3cWIPSDevStatEntry_Object = MibTableRow
hh3cWIPSDevStatEntry = _Hh3cWIPSDevStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1)
)
hh3cWIPSDevStatEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDevStatSensorMacAddr"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDevStatDevMacAddress"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDevStatChannel"),
)
if mibBuilder.loadTexts:
    hh3cWIPSDevStatEntry.setStatus("current")
_Hh3cWIPSDevStatSensorMacAddr_Type = MacAddress
_Hh3cWIPSDevStatSensorMacAddr_Object = MibTableColumn
hh3cWIPSDevStatSensorMacAddr = _Hh3cWIPSDevStatSensorMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 1),
    _Hh3cWIPSDevStatSensorMacAddr_Type()
)
hh3cWIPSDevStatSensorMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatSensorMacAddr.setStatus("current")
_Hh3cWIPSDevStatDevMacAddress_Type = MacAddress
_Hh3cWIPSDevStatDevMacAddress_Object = MibTableColumn
hh3cWIPSDevStatDevMacAddress = _Hh3cWIPSDevStatDevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 2),
    _Hh3cWIPSDevStatDevMacAddress_Type()
)
hh3cWIPSDevStatDevMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatDevMacAddress.setStatus("current")
_Hh3cWIPSDevStatChannel_Type = Hh3cWIPSChannel
_Hh3cWIPSDevStatChannel_Object = MibTableColumn
hh3cWIPSDevStatChannel = _Hh3cWIPSDevStatChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 3),
    _Hh3cWIPSDevStatChannel_Type()
)
hh3cWIPSDevStatChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatChannel.setStatus("current")


class _Hh3cWIPSDevStatTxTotalPkt_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxTotalPkt based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxTotalPkt_Object = MibTableColumn
hh3cWIPSDevStatTxTotalPkt = _Hh3cWIPSDevStatTxTotalPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 4),
    _Hh3cWIPSDevStatTxTotalPkt_Type()
)
hh3cWIPSDevStatTxTotalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxTotalPkt.setStatus("current")


class _Hh3cWIPSDevStatTxTotalByte_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxTotalByte based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxTotalByte_Object = MibTableColumn
hh3cWIPSDevStatTxTotalByte = _Hh3cWIPSDevStatTxTotalByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 5),
    _Hh3cWIPSDevStatTxTotalByte_Type()
)
hh3cWIPSDevStatTxTotalByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxTotalByte.setStatus("current")


class _Hh3cWIPSDevStatTxBMcastPkt_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxBMcastPkt based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxBMcastPkt_Object = MibTableColumn
hh3cWIPSDevStatTxBMcastPkt = _Hh3cWIPSDevStatTxBMcastPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 6),
    _Hh3cWIPSDevStatTxBMcastPkt_Type()
)
hh3cWIPSDevStatTxBMcastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxBMcastPkt.setStatus("current")


class _Hh3cWIPSDevStatTxBMcastByte_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxBMcastByte based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxBMcastByte_Object = MibTableColumn
hh3cWIPSDevStatTxBMcastByte = _Hh3cWIPSDevStatTxBMcastByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 7),
    _Hh3cWIPSDevStatTxBMcastByte_Type()
)
hh3cWIPSDevStatTxBMcastByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxBMcastByte.setStatus("current")


class _Hh3cWIPSDevStatTxUnicastPkt_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxUnicastPkt based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxUnicastPkt_Object = MibTableColumn
hh3cWIPSDevStatTxUnicastPkt = _Hh3cWIPSDevStatTxUnicastPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 8),
    _Hh3cWIPSDevStatTxUnicastPkt_Type()
)
hh3cWIPSDevStatTxUnicastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxUnicastPkt.setStatus("current")


class _Hh3cWIPSDevStatTxUnicastByte_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxUnicastByte based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxUnicastByte_Object = MibTableColumn
hh3cWIPSDevStatTxUnicastByte = _Hh3cWIPSDevStatTxUnicastByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 9),
    _Hh3cWIPSDevStatTxUnicastByte_Type()
)
hh3cWIPSDevStatTxUnicastByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxUnicastByte.setStatus("current")


class _Hh3cWIPSDevStatTxMgmt_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxMgmt based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxMgmt_Object = MibTableColumn
hh3cWIPSDevStatTxMgmt = _Hh3cWIPSDevStatTxMgmt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 10),
    _Hh3cWIPSDevStatTxMgmt_Type()
)
hh3cWIPSDevStatTxMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxMgmt.setStatus("current")


class _Hh3cWIPSDevStatTxCtrl_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxCtrl based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxCtrl_Object = MibTableColumn
hh3cWIPSDevStatTxCtrl = _Hh3cWIPSDevStatTxCtrl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 11),
    _Hh3cWIPSDevStatTxCtrl_Type()
)
hh3cWIPSDevStatTxCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxCtrl.setStatus("current")


class _Hh3cWIPSDevStatTxData_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxData based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxData_Object = MibTableColumn
hh3cWIPSDevStatTxData = _Hh3cWIPSDevStatTxData_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 12),
    _Hh3cWIPSDevStatTxData_Type()
)
hh3cWIPSDevStatTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxData.setStatus("current")


class _Hh3cWIPSDevStatTxBeacon_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxBeacon based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxBeacon_Object = MibTableColumn
hh3cWIPSDevStatTxBeacon = _Hh3cWIPSDevStatTxBeacon_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 13),
    _Hh3cWIPSDevStatTxBeacon_Type()
)
hh3cWIPSDevStatTxBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxBeacon.setStatus("current")


class _Hh3cWIPSDevStatTxRTS_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxRTS based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxRTS_Object = MibTableColumn
hh3cWIPSDevStatTxRTS = _Hh3cWIPSDevStatTxRTS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 14),
    _Hh3cWIPSDevStatTxRTS_Type()
)
hh3cWIPSDevStatTxRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxRTS.setStatus("current")


class _Hh3cWIPSDevStatTxProbeRequest_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxProbeRequest based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxProbeRequest_Object = MibTableColumn
hh3cWIPSDevStatTxProbeRequest = _Hh3cWIPSDevStatTxProbeRequest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 15),
    _Hh3cWIPSDevStatTxProbeRequest_Type()
)
hh3cWIPSDevStatTxProbeRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxProbeRequest.setStatus("current")


class _Hh3cWIPSDevStatTxProbeResponse_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxProbeResponse based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxProbeResponse_Object = MibTableColumn
hh3cWIPSDevStatTxProbeResponse = _Hh3cWIPSDevStatTxProbeResponse_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 16),
    _Hh3cWIPSDevStatTxProbeResponse_Type()
)
hh3cWIPSDevStatTxProbeResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxProbeResponse.setStatus("current")


class _Hh3cWIPSDevStatTxFragment_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxFragment based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxFragment_Object = MibTableColumn
hh3cWIPSDevStatTxFragment = _Hh3cWIPSDevStatTxFragment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 17),
    _Hh3cWIPSDevStatTxFragment_Type()
)
hh3cWIPSDevStatTxFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxFragment.setStatus("current")


class _Hh3cWIPSDevStatTxRetry_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxRetry based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxRetry_Object = MibTableColumn
hh3cWIPSDevStatTxRetry = _Hh3cWIPSDevStatTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 18),
    _Hh3cWIPSDevStatTxRetry_Type()
)
hh3cWIPSDevStatTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxRetry.setStatus("current")


class _Hh3cWIPSDevStatTxAssocRequest_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxAssocRequest based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxAssocRequest_Object = MibTableColumn
hh3cWIPSDevStatTxAssocRequest = _Hh3cWIPSDevStatTxAssocRequest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 19),
    _Hh3cWIPSDevStatTxAssocRequest_Type()
)
hh3cWIPSDevStatTxAssocRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxAssocRequest.setStatus("current")


class _Hh3cWIPSDevStatTxAssocResponse_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxAssocResponse based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxAssocResponse_Object = MibTableColumn
hh3cWIPSDevStatTxAssocResponse = _Hh3cWIPSDevStatTxAssocResponse_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 20),
    _Hh3cWIPSDevStatTxAssocResponse_Type()
)
hh3cWIPSDevStatTxAssocResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxAssocResponse.setStatus("current")


class _Hh3cWIPSDevStatTxUnicastDisassoc_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxUnicastDisassoc based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxUnicastDisassoc_Object = MibTableColumn
hh3cWIPSDevStatTxUnicastDisassoc = _Hh3cWIPSDevStatTxUnicastDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 21),
    _Hh3cWIPSDevStatTxUnicastDisassoc_Type()
)
hh3cWIPSDevStatTxUnicastDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxUnicastDisassoc.setStatus("current")


class _Hh3cWIPSDevStatTxBcastDisassoc_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxBcastDisassoc based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxBcastDisassoc_Object = MibTableColumn
hh3cWIPSDevStatTxBcastDisassoc = _Hh3cWIPSDevStatTxBcastDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 22),
    _Hh3cWIPSDevStatTxBcastDisassoc_Type()
)
hh3cWIPSDevStatTxBcastDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxBcastDisassoc.setStatus("current")


class _Hh3cWIPSDevStatTxAuth_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxAuth based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxAuth_Object = MibTableColumn
hh3cWIPSDevStatTxAuth = _Hh3cWIPSDevStatTxAuth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 23),
    _Hh3cWIPSDevStatTxAuth_Type()
)
hh3cWIPSDevStatTxAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxAuth.setStatus("current")


class _Hh3cWIPSDevStatTxUnicastDeauth_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxUnicastDeauth based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxUnicastDeauth_Object = MibTableColumn
hh3cWIPSDevStatTxUnicastDeauth = _Hh3cWIPSDevStatTxUnicastDeauth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 24),
    _Hh3cWIPSDevStatTxUnicastDeauth_Type()
)
hh3cWIPSDevStatTxUnicastDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxUnicastDeauth.setStatus("current")


class _Hh3cWIPSDevStatTxBcastDeauth_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxBcastDeauth based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxBcastDeauth_Object = MibTableColumn
hh3cWIPSDevStatTxBcastDeauth = _Hh3cWIPSDevStatTxBcastDeauth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 25),
    _Hh3cWIPSDevStatTxBcastDeauth_Type()
)
hh3cWIPSDevStatTxBcastDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxBcastDeauth.setStatus("current")


class _Hh3cWIPSDevStatTxEAPSuccess_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxEAPSuccess based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxEAPSuccess_Object = MibTableColumn
hh3cWIPSDevStatTxEAPSuccess = _Hh3cWIPSDevStatTxEAPSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 26),
    _Hh3cWIPSDevStatTxEAPSuccess_Type()
)
hh3cWIPSDevStatTxEAPSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxEAPSuccess.setStatus("current")


class _Hh3cWIPSDevStatTxEAPFailure_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxEAPFailure based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxEAPFailure_Object = MibTableColumn
hh3cWIPSDevStatTxEAPFailure = _Hh3cWIPSDevStatTxEAPFailure_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 27),
    _Hh3cWIPSDevStatTxEAPFailure_Type()
)
hh3cWIPSDevStatTxEAPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxEAPFailure.setStatus("current")


class _Hh3cWIPSDevStatTxEAPOLStart_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxEAPOLStart based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxEAPOLStart_Object = MibTableColumn
hh3cWIPSDevStatTxEAPOLStart = _Hh3cWIPSDevStatTxEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 28),
    _Hh3cWIPSDevStatTxEAPOLStart_Type()
)
hh3cWIPSDevStatTxEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxEAPOLStart.setStatus("current")


class _Hh3cWIPSDevStatTxEAPOLLogOff_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxEAPOLLogOff based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxEAPOLLogOff_Object = MibTableColumn
hh3cWIPSDevStatTxEAPOLLogOff = _Hh3cWIPSDevStatTxEAPOLLogOff_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 29),
    _Hh3cWIPSDevStatTxEAPOLLogOff_Type()
)
hh3cWIPSDevStatTxEAPOLLogOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxEAPOLLogOff.setStatus("current")


class _Hh3cWIPSDevStatTxMalformed_Type(Counter64):
    """Custom type hh3cWIPSDevStatTxMalformed based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatTxMalformed_Object = MibTableColumn
hh3cWIPSDevStatTxMalformed = _Hh3cWIPSDevStatTxMalformed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 30),
    _Hh3cWIPSDevStatTxMalformed_Type()
)
hh3cWIPSDevStatTxMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatTxMalformed.setStatus("current")


class _Hh3cWIPSDevStatRxTotalPkt_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxTotalPkt based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxTotalPkt_Object = MibTableColumn
hh3cWIPSDevStatRxTotalPkt = _Hh3cWIPSDevStatRxTotalPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 31),
    _Hh3cWIPSDevStatRxTotalPkt_Type()
)
hh3cWIPSDevStatRxTotalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxTotalPkt.setStatus("current")


class _Hh3cWIPSDevStatRxTotalByte_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxTotalByte based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxTotalByte_Object = MibTableColumn
hh3cWIPSDevStatRxTotalByte = _Hh3cWIPSDevStatRxTotalByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 32),
    _Hh3cWIPSDevStatRxTotalByte_Type()
)
hh3cWIPSDevStatRxTotalByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxTotalByte.setStatus("current")


class _Hh3cWIPSDevStatRxUnicastPkt_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxUnicastPkt based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxUnicastPkt_Object = MibTableColumn
hh3cWIPSDevStatRxUnicastPkt = _Hh3cWIPSDevStatRxUnicastPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 33),
    _Hh3cWIPSDevStatRxUnicastPkt_Type()
)
hh3cWIPSDevStatRxUnicastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxUnicastPkt.setStatus("current")


class _Hh3cWIPSDevStatRxUnicastByte_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxUnicastByte based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxUnicastByte_Object = MibTableColumn
hh3cWIPSDevStatRxUnicastByte = _Hh3cWIPSDevStatRxUnicastByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 34),
    _Hh3cWIPSDevStatRxUnicastByte_Type()
)
hh3cWIPSDevStatRxUnicastByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxUnicastByte.setStatus("current")


class _Hh3cWIPSDevStatRxMgmt_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxMgmt based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxMgmt_Object = MibTableColumn
hh3cWIPSDevStatRxMgmt = _Hh3cWIPSDevStatRxMgmt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 35),
    _Hh3cWIPSDevStatRxMgmt_Type()
)
hh3cWIPSDevStatRxMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxMgmt.setStatus("current")


class _Hh3cWIPSDevStatRxCtrl_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxCtrl based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxCtrl_Object = MibTableColumn
hh3cWIPSDevStatRxCtrl = _Hh3cWIPSDevStatRxCtrl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 36),
    _Hh3cWIPSDevStatRxCtrl_Type()
)
hh3cWIPSDevStatRxCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxCtrl.setStatus("current")


class _Hh3cWIPSDevStatRxData_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxData based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxData_Object = MibTableColumn
hh3cWIPSDevStatRxData = _Hh3cWIPSDevStatRxData_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 37),
    _Hh3cWIPSDevStatRxData_Type()
)
hh3cWIPSDevStatRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxData.setStatus("current")


class _Hh3cWIPSDevStatRxRTS_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxRTS based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxRTS_Object = MibTableColumn
hh3cWIPSDevStatRxRTS = _Hh3cWIPSDevStatRxRTS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 38),
    _Hh3cWIPSDevStatRxRTS_Type()
)
hh3cWIPSDevStatRxRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxRTS.setStatus("current")


class _Hh3cWIPSDevStatRxCTS_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxCTS based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxCTS_Object = MibTableColumn
hh3cWIPSDevStatRxCTS = _Hh3cWIPSDevStatRxCTS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 39),
    _Hh3cWIPSDevStatRxCTS_Type()
)
hh3cWIPSDevStatRxCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxCTS.setStatus("current")


class _Hh3cWIPSDevStatRxProbeRequest_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxProbeRequest based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxProbeRequest_Object = MibTableColumn
hh3cWIPSDevStatRxProbeRequest = _Hh3cWIPSDevStatRxProbeRequest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 40),
    _Hh3cWIPSDevStatRxProbeRequest_Type()
)
hh3cWIPSDevStatRxProbeRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxProbeRequest.setStatus("current")


class _Hh3cWIPSDevStatRxProbeResponse_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxProbeResponse based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxProbeResponse_Object = MibTableColumn
hh3cWIPSDevStatRxProbeResponse = _Hh3cWIPSDevStatRxProbeResponse_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 41),
    _Hh3cWIPSDevStatRxProbeResponse_Type()
)
hh3cWIPSDevStatRxProbeResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxProbeResponse.setStatus("current")


class _Hh3cWIPSDevStatRxFragment_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxFragment based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxFragment_Object = MibTableColumn
hh3cWIPSDevStatRxFragment = _Hh3cWIPSDevStatRxFragment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 42),
    _Hh3cWIPSDevStatRxFragment_Type()
)
hh3cWIPSDevStatRxFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxFragment.setStatus("current")


class _Hh3cWIPSDevStatRxRetry_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxRetry based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxRetry_Object = MibTableColumn
hh3cWIPSDevStatRxRetry = _Hh3cWIPSDevStatRxRetry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 43),
    _Hh3cWIPSDevStatRxRetry_Type()
)
hh3cWIPSDevStatRxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxRetry.setStatus("current")


class _Hh3cWIPSDevStatRxAssoRequest_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxAssoRequest based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxAssoRequest_Object = MibTableColumn
hh3cWIPSDevStatRxAssoRequest = _Hh3cWIPSDevStatRxAssoRequest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 44),
    _Hh3cWIPSDevStatRxAssoRequest_Type()
)
hh3cWIPSDevStatRxAssoRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxAssoRequest.setStatus("current")


class _Hh3cWIPSDevStatRxAssoResponse_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxAssoResponse based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxAssoResponse_Object = MibTableColumn
hh3cWIPSDevStatRxAssoResponse = _Hh3cWIPSDevStatRxAssoResponse_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 45),
    _Hh3cWIPSDevStatRxAssoResponse_Type()
)
hh3cWIPSDevStatRxAssoResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxAssoResponse.setStatus("current")


class _Hh3cWIPSDevStatRxDisassoc_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxDisassoc based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxDisassoc_Object = MibTableColumn
hh3cWIPSDevStatRxDisassoc = _Hh3cWIPSDevStatRxDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 46),
    _Hh3cWIPSDevStatRxDisassoc_Type()
)
hh3cWIPSDevStatRxDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxDisassoc.setStatus("current")


class _Hh3cWIPSDevStatRxAuth_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxAuth based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxAuth_Object = MibTableColumn
hh3cWIPSDevStatRxAuth = _Hh3cWIPSDevStatRxAuth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 47),
    _Hh3cWIPSDevStatRxAuth_Type()
)
hh3cWIPSDevStatRxAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxAuth.setStatus("current")


class _Hh3cWIPSDevStatRxDeauth_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxDeauth based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxDeauth_Object = MibTableColumn
hh3cWIPSDevStatRxDeauth = _Hh3cWIPSDevStatRxDeauth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 48),
    _Hh3cWIPSDevStatRxDeauth_Type()
)
hh3cWIPSDevStatRxDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxDeauth.setStatus("current")


class _Hh3cWIPSDevStatRxEAPSuccess_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxEAPSuccess based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxEAPSuccess_Object = MibTableColumn
hh3cWIPSDevStatRxEAPSuccess = _Hh3cWIPSDevStatRxEAPSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 49),
    _Hh3cWIPSDevStatRxEAPSuccess_Type()
)
hh3cWIPSDevStatRxEAPSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxEAPSuccess.setStatus("current")


class _Hh3cWIPSDevStatRxEAPFailure_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxEAPFailure based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxEAPFailure_Object = MibTableColumn
hh3cWIPSDevStatRxEAPFailure = _Hh3cWIPSDevStatRxEAPFailure_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 50),
    _Hh3cWIPSDevStatRxEAPFailure_Type()
)
hh3cWIPSDevStatRxEAPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxEAPFailure.setStatus("current")


class _Hh3cWIPSDevStatRxEAPOLStart_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxEAPOLStart based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxEAPOLStart_Object = MibTableColumn
hh3cWIPSDevStatRxEAPOLStart = _Hh3cWIPSDevStatRxEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 51),
    _Hh3cWIPSDevStatRxEAPOLStart_Type()
)
hh3cWIPSDevStatRxEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxEAPOLStart.setStatus("current")


class _Hh3cWIPSDevStatRxEAPOLLogoff_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxEAPOLLogoff based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxEAPOLLogoff_Object = MibTableColumn
hh3cWIPSDevStatRxEAPOLLogoff = _Hh3cWIPSDevStatRxEAPOLLogoff_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 52),
    _Hh3cWIPSDevStatRxEAPOLLogoff_Type()
)
hh3cWIPSDevStatRxEAPOLLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxEAPOLLogoff.setStatus("current")


class _Hh3cWIPSDevStatRxMalformed_Type(Counter64):
    """Custom type hh3cWIPSDevStatRxMalformed based on Counter64"""
    defaultValue = 0


_Hh3cWIPSDevStatRxMalformed_Object = MibTableColumn
hh3cWIPSDevStatRxMalformed = _Hh3cWIPSDevStatRxMalformed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 14, 1, 53),
    _Hh3cWIPSDevStatRxMalformed_Type()
)
hh3cWIPSDevStatRxMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDevStatRxMalformed.setStatus("current")
_Hh3cWIPSCtmDeviceTable_Object = MibTable
hh3cWIPSCtmDeviceTable = _Hh3cWIPSCtmDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 15)
)
if mibBuilder.loadTexts:
    hh3cWIPSCtmDeviceTable.setStatus("current")
_Hh3cWIPSCtmDeviceEntry_Object = MibTableRow
hh3cWIPSCtmDeviceEntry = _Hh3cWIPSCtmDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 15, 1)
)
hh3cWIPSCtmDeviceEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSCtmDeviceVSD"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSCtmDeviceMAC"),
)
if mibBuilder.loadTexts:
    hh3cWIPSCtmDeviceEntry.setStatus("current")


class _Hh3cWIPSCtmDeviceVSD_Type(OctetString):
    """Custom type hh3cWIPSCtmDeviceVSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSCtmDeviceVSD_Type.__name__ = "OctetString"
_Hh3cWIPSCtmDeviceVSD_Object = MibTableColumn
hh3cWIPSCtmDeviceVSD = _Hh3cWIPSCtmDeviceVSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 15, 1, 1),
    _Hh3cWIPSCtmDeviceVSD_Type()
)
hh3cWIPSCtmDeviceVSD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSCtmDeviceVSD.setStatus("current")
_Hh3cWIPSCtmDeviceMAC_Type = MacAddress
_Hh3cWIPSCtmDeviceMAC_Object = MibTableColumn
hh3cWIPSCtmDeviceMAC = _Hh3cWIPSCtmDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 15, 1, 2),
    _Hh3cWIPSCtmDeviceMAC_Type()
)
hh3cWIPSCtmDeviceMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSCtmDeviceMAC.setStatus("current")


class _Hh3cWIPSCtmDeviceType_Type(Integer32):
    """Custom type hh3cWIPSCtmDeviceType based on Integer32"""
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


_Hh3cWIPSCtmDeviceType_Type.__name__ = "Integer32"
_Hh3cWIPSCtmDeviceType_Object = MibTableColumn
hh3cWIPSCtmDeviceType = _Hh3cWIPSCtmDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 15, 1, 3),
    _Hh3cWIPSCtmDeviceType_Type()
)
hh3cWIPSCtmDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSCtmDeviceType.setStatus("current")


class _Hh3cWIPSCtmDeviceState_Type(Integer32):
    """Custom type hh3cWIPSCtmDeviceState based on Integer32"""
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


_Hh3cWIPSCtmDeviceState_Type.__name__ = "Integer32"
_Hh3cWIPSCtmDeviceState_Object = MibTableColumn
hh3cWIPSCtmDeviceState = _Hh3cWIPSCtmDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 15, 1, 4),
    _Hh3cWIPSCtmDeviceState_Type()
)
hh3cWIPSCtmDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSCtmDeviceState.setStatus("current")
_Hh3cWIPSCtmDeviceStartTime_Type = TimeTicks
_Hh3cWIPSCtmDeviceStartTime_Object = MibTableColumn
hh3cWIPSCtmDeviceStartTime = _Hh3cWIPSCtmDeviceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 15, 1, 5),
    _Hh3cWIPSCtmDeviceStartTime_Type()
)
hh3cWIPSCtmDeviceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSCtmDeviceStartTime.setStatus("current")
_Hh3cWIPSCtmDeviceCategory_Type = Hh3cWIPSDeviceCategoryType
_Hh3cWIPSCtmDeviceCategory_Object = MibTableColumn
hh3cWIPSCtmDeviceCategory = _Hh3cWIPSCtmDeviceCategory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 15, 1, 6),
    _Hh3cWIPSCtmDeviceCategory_Type()
)
hh3cWIPSCtmDeviceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSCtmDeviceCategory.setStatus("current")
_Hh3cWIPSCtmDeviceChl_Type = Unsigned32
_Hh3cWIPSCtmDeviceChl_Object = MibTableColumn
hh3cWIPSCtmDeviceChl = _Hh3cWIPSCtmDeviceChl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 15, 1, 7),
    _Hh3cWIPSCtmDeviceChl_Type()
)
hh3cWIPSCtmDeviceChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSCtmDeviceChl.setStatus("current")


class _Hh3cWIPSCtmDevicePrecedence_Type(Integer32):
    """Custom type hh3cWIPSCtmDevicePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Hh3cWIPSCtmDevicePrecedence_Type.__name__ = "Integer32"
_Hh3cWIPSCtmDevicePrecedence_Object = MibTableColumn
hh3cWIPSCtmDevicePrecedence = _Hh3cWIPSCtmDevicePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 15, 1, 8),
    _Hh3cWIPSCtmDevicePrecedence_Type()
)
hh3cWIPSCtmDevicePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSCtmDevicePrecedence.setStatus("current")
_Hh3cWIPSMalPktStatTable_Object = MibTable
hh3cWIPSMalPktStatTable = _Hh3cWIPSMalPktStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16)
)
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatTable.setStatus("current")
_Hh3cWIPSMalPktStatEntry_Object = MibTableRow
hh3cWIPSMalPktStatEntry = _Hh3cWIPSMalPktStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1)
)
hh3cWIPSMalPktStatEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSMalPktStatSensorName"),
)
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatEntry.setStatus("current")


class _Hh3cWIPSMalPktStatSensorName_Type(OctetString):
    """Custom type hh3cWIPSMalPktStatSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cWIPSMalPktStatSensorName_Type.__name__ = "OctetString"
_Hh3cWIPSMalPktStatSensorName_Object = MibTableColumn
hh3cWIPSMalPktStatSensorName = _Hh3cWIPSMalPktStatSensorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 1),
    _Hh3cWIPSMalPktStatSensorName_Type()
)
hh3cWIPSMalPktStatSensorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatSensorName.setStatus("current")


class _Hh3cWIPSMalPktStatInvalidIELength_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatInvalidIELength based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatInvalidIELength_Object = MibTableColumn
hh3cWIPSMalPktStatInvalidIELength = _Hh3cWIPSMalPktStatInvalidIELength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 2),
    _Hh3cWIPSMalPktStatInvalidIELength_Type()
)
hh3cWIPSMalPktStatInvalidIELength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatInvalidIELength.setStatus("current")


class _Hh3cWIPSMalPktStatDuplicatedIE_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatDuplicatedIE based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatDuplicatedIE_Object = MibTableColumn
hh3cWIPSMalPktStatDuplicatedIE = _Hh3cWIPSMalPktStatDuplicatedIE_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 3),
    _Hh3cWIPSMalPktStatDuplicatedIE_Type()
)
hh3cWIPSMalPktStatDuplicatedIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatDuplicatedIE.setStatus("current")


class _Hh3cWIPSMalPktStatRedundantIE_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatRedundantIE based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatRedundantIE_Object = MibTableColumn
hh3cWIPSMalPktStatRedundantIE = _Hh3cWIPSMalPktStatRedundantIE_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 4),
    _Hh3cWIPSMalPktStatRedundantIE_Type()
)
hh3cWIPSMalPktStatRedundantIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatRedundantIE.setStatus("current")


class _Hh3cWIPSMalPktStatInvalidPktLength_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatInvalidPktLength based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatInvalidPktLength_Object = MibTableColumn
hh3cWIPSMalPktStatInvalidPktLength = _Hh3cWIPSMalPktStatInvalidPktLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 5),
    _Hh3cWIPSMalPktStatInvalidPktLength_Type()
)
hh3cWIPSMalPktStatInvalidPktLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatInvalidPktLength.setStatus("current")


class _Hh3cWIPSMalPktStatIllegalIBSSESS_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatIllegalIBSSESS based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatIllegalIBSSESS_Object = MibTableColumn
hh3cWIPSMalPktStatIllegalIBSSESS = _Hh3cWIPSMalPktStatIllegalIBSSESS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 6),
    _Hh3cWIPSMalPktStatIllegalIBSSESS_Type()
)
hh3cWIPSMalPktStatIllegalIBSSESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatIllegalIBSSESS.setStatus("current")


class _Hh3cWIPSMalPktStatInvalidSourceAddr_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatInvalidSourceAddr based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatInvalidSourceAddr_Object = MibTableColumn
hh3cWIPSMalPktStatInvalidSourceAddr = _Hh3cWIPSMalPktStatInvalidSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 7),
    _Hh3cWIPSMalPktStatInvalidSourceAddr_Type()
)
hh3cWIPSMalPktStatInvalidSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatInvalidSourceAddr.setStatus("current")


class _Hh3cWIPSMalPktStatOverflowEAPOLKey_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatOverflowEAPOLKey based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatOverflowEAPOLKey_Object = MibTableColumn
hh3cWIPSMalPktStatOverflowEAPOLKey = _Hh3cWIPSMalPktStatOverflowEAPOLKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 8),
    _Hh3cWIPSMalPktStatOverflowEAPOLKey_Type()
)
hh3cWIPSMalPktStatOverflowEAPOLKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatOverflowEAPOLKey.setStatus("current")


class _Hh3cWIPSMalPktStatMalAuth_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatMalAuth based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatMalAuth_Object = MibTableColumn
hh3cWIPSMalPktStatMalAuth = _Hh3cWIPSMalPktStatMalAuth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 9),
    _Hh3cWIPSMalPktStatMalAuth_Type()
)
hh3cWIPSMalPktStatMalAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatMalAuth.setStatus("current")


class _Hh3cWIPSMalPktStatMalAssoReq_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatMalAssoReq based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatMalAssoReq_Object = MibTableColumn
hh3cWIPSMalPktStatMalAssoReq = _Hh3cWIPSMalPktStatMalAssoReq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 10),
    _Hh3cWIPSMalPktStatMalAssoReq_Type()
)
hh3cWIPSMalPktStatMalAssoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatMalAssoReq.setStatus("current")


class _Hh3cWIPSMalPktStatMalHTIE_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatMalHTIE based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatMalHTIE_Object = MibTableColumn
hh3cWIPSMalPktStatMalHTIE = _Hh3cWIPSMalPktStatMalHTIE_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 11),
    _Hh3cWIPSMalPktStatMalHTIE_Type()
)
hh3cWIPSMalPktStatMalHTIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatMalHTIE.setStatus("current")


class _Hh3cWIPSMalPktStatLargeDuration_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatLargeDuration based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatLargeDuration_Object = MibTableColumn
hh3cWIPSMalPktStatLargeDuration = _Hh3cWIPSMalPktStatLargeDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 12),
    _Hh3cWIPSMalPktStatLargeDuration_Type()
)
hh3cWIPSMalPktStatLargeDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatLargeDuration.setStatus("current")


class _Hh3cWIPSMalPktStatNULLProbeRes_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatNULLProbeRes based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatNULLProbeRes_Object = MibTableColumn
hh3cWIPSMalPktStatNULLProbeRes = _Hh3cWIPSMalPktStatNULLProbeRes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 13),
    _Hh3cWIPSMalPktStatNULLProbeRes_Type()
)
hh3cWIPSMalPktStatNULLProbeRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatNULLProbeRes.setStatus("current")


class _Hh3cWIPSMalPktStatInvalidDeAuthCode_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatInvalidDeAuthCode based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatInvalidDeAuthCode_Object = MibTableColumn
hh3cWIPSMalPktStatInvalidDeAuthCode = _Hh3cWIPSMalPktStatInvalidDeAuthCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 14),
    _Hh3cWIPSMalPktStatInvalidDeAuthCode_Type()
)
hh3cWIPSMalPktStatInvalidDeAuthCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatInvalidDeAuthCode.setStatus("current")


class _Hh3cWIPSMalPktStatInvalidDisAssoCode_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatInvalidDisAssoCode based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatInvalidDisAssoCode_Object = MibTableColumn
hh3cWIPSMalPktStatInvalidDisAssoCode = _Hh3cWIPSMalPktStatInvalidDisAssoCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 15),
    _Hh3cWIPSMalPktStatInvalidDisAssoCode_Type()
)
hh3cWIPSMalPktStatInvalidDisAssoCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatInvalidDisAssoCode.setStatus("current")


class _Hh3cWIPSMalPktStatOverflowSSID_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatOverflowSSID based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatOverflowSSID_Object = MibTableColumn
hh3cWIPSMalPktStatOverflowSSID = _Hh3cWIPSMalPktStatOverflowSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 16),
    _Hh3cWIPSMalPktStatOverflowSSID_Type()
)
hh3cWIPSMalPktStatOverflowSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatOverflowSSID.setStatus("current")


class _Hh3cWIPSMalPktStatFatajack_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatFatajack based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatFatajack_Object = MibTableColumn
hh3cWIPSMalPktStatFatajack = _Hh3cWIPSMalPktStatFatajack_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 17),
    _Hh3cWIPSMalPktStatFatajack_Type()
)
hh3cWIPSMalPktStatFatajack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatFatajack.setStatus("current")


class _Hh3cWIPSMalPktStatInvalidChannel_Type(Counter64):
    """Custom type hh3cWIPSMalPktStatInvalidChannel based on Counter64"""
    defaultValue = 0


_Hh3cWIPSMalPktStatInvalidChannel_Object = MibTableColumn
hh3cWIPSMalPktStatInvalidChannel = _Hh3cWIPSMalPktStatInvalidChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 16, 1, 18),
    _Hh3cWIPSMalPktStatInvalidChannel_Type()
)
hh3cWIPSMalPktStatInvalidChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSMalPktStatInvalidChannel.setStatus("current")
_Hh3cWIPSDctUnassocStaTable_Object = MibTable
hh3cWIPSDctUnassocStaTable = _Hh3cWIPSDctUnassocStaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17)
)
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaTable.setStatus("current")
_Hh3cWIPSDctUnassocStaEntry_Object = MibTableRow
hh3cWIPSDctUnassocStaEntry = _Hh3cWIPSDctUnassocStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1)
)
hh3cWIPSDctUnassocStaEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctUnassocStaVSD"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctUnassocStaMac"),
)
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaEntry.setStatus("current")


class _Hh3cWIPSDctUnassocStaVSD_Type(OctetString):
    """Custom type hh3cWIPSDctUnassocStaVSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cWIPSDctUnassocStaVSD_Type.__name__ = "OctetString"
_Hh3cWIPSDctUnassocStaVSD_Object = MibTableColumn
hh3cWIPSDctUnassocStaVSD = _Hh3cWIPSDctUnassocStaVSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 1),
    _Hh3cWIPSDctUnassocStaVSD_Type()
)
hh3cWIPSDctUnassocStaVSD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaVSD.setStatus("current")
_Hh3cWIPSDctUnassocStaMac_Type = MacAddress
_Hh3cWIPSDctUnassocStaMac_Object = MibTableColumn
hh3cWIPSDctUnassocStaMac = _Hh3cWIPSDctUnassocStaMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 2),
    _Hh3cWIPSDctUnassocStaMac_Type()
)
hh3cWIPSDctUnassocStaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaMac.setStatus("current")
_Hh3cWIPSDctUnassocStaCategory_Type = Hh3cWIPSClientCategoryType
_Hh3cWIPSDctUnassocStaCategory_Object = MibTableColumn
hh3cWIPSDctUnassocStaCategory = _Hh3cWIPSDctUnassocStaCategory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 3),
    _Hh3cWIPSDctUnassocStaCategory_Type()
)
hh3cWIPSDctUnassocStaCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaCategory.setStatus("current")
_Hh3cWIPSDctUnassocStaRadioType_Type = Unsigned32
_Hh3cWIPSDctUnassocStaRadioType_Object = MibTableColumn
hh3cWIPSDctUnassocStaRadioType = _Hh3cWIPSDctUnassocStaRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 4),
    _Hh3cWIPSDctUnassocStaRadioType_Type()
)
hh3cWIPSDctUnassocStaRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaRadioType.setStatus("current")
_Hh3cWIPSDctUnassocStaIsCountered_Type = TruthValue
_Hh3cWIPSDctUnassocStaIsCountered_Object = MibTableColumn
hh3cWIPSDctUnassocStaIsCountered = _Hh3cWIPSDctUnassocStaIsCountered_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 5),
    _Hh3cWIPSDctUnassocStaIsCountered_Type()
)
hh3cWIPSDctUnassocStaIsCountered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaIsCountered.setStatus("current")


class _Hh3cWIPSDctUnassocStaAdd2BlackList_Type(TruthValue):
    """Custom type hh3cWIPSDctUnassocStaAdd2BlackList based on TruthValue"""


_Hh3cWIPSDctUnassocStaAdd2BlackList_Object = MibTableColumn
hh3cWIPSDctUnassocStaAdd2BlackList = _Hh3cWIPSDctUnassocStaAdd2BlackList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 6),
    _Hh3cWIPSDctUnassocStaAdd2BlackList_Type()
)
hh3cWIPSDctUnassocStaAdd2BlackList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaAdd2BlackList.setStatus("current")


class _Hh3cWIPSDctUnassocStaAdd2WhiteList_Type(TruthValue):
    """Custom type hh3cWIPSDctUnassocStaAdd2WhiteList based on TruthValue"""


_Hh3cWIPSDctUnassocStaAdd2WhiteList_Object = MibTableColumn
hh3cWIPSDctUnassocStaAdd2WhiteList = _Hh3cWIPSDctUnassocStaAdd2WhiteList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 7),
    _Hh3cWIPSDctUnassocStaAdd2WhiteList_Type()
)
hh3cWIPSDctUnassocStaAdd2WhiteList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaAdd2WhiteList.setStatus("current")


class _Hh3cWIPSDctUnassocStaAdd2IgnoreList_Type(TruthValue):
    """Custom type hh3cWIPSDctUnassocStaAdd2IgnoreList based on TruthValue"""


_Hh3cWIPSDctUnassocStaAdd2IgnoreList_Object = MibTableColumn
hh3cWIPSDctUnassocStaAdd2IgnoreList = _Hh3cWIPSDctUnassocStaAdd2IgnoreList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 8),
    _Hh3cWIPSDctUnassocStaAdd2IgnoreList_Type()
)
hh3cWIPSDctUnassocStaAdd2IgnoreList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaAdd2IgnoreList.setStatus("current")


class _Hh3cWIPSDctUnassocStaAdd2CtmList_Type(TruthValue):
    """Custom type hh3cWIPSDctUnassocStaAdd2CtmList based on TruthValue"""


_Hh3cWIPSDctUnassocStaAdd2CtmList_Object = MibTableColumn
hh3cWIPSDctUnassocStaAdd2CtmList = _Hh3cWIPSDctUnassocStaAdd2CtmList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 9),
    _Hh3cWIPSDctUnassocStaAdd2CtmList_Type()
)
hh3cWIPSDctUnassocStaAdd2CtmList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaAdd2CtmList.setStatus("current")
_Hh3cWIPSDctUnassocStaFirstDctTm_Type = TimeTicks
_Hh3cWIPSDctUnassocStaFirstDctTm_Object = MibTableColumn
hh3cWIPSDctUnassocStaFirstDctTm = _Hh3cWIPSDctUnassocStaFirstDctTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 10),
    _Hh3cWIPSDctUnassocStaFirstDctTm_Type()
)
hh3cWIPSDctUnassocStaFirstDctTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaFirstDctTm.setStatus("current")
_Hh3cWIPSDctUnassocStaLastDctTm_Type = TimeTicks
_Hh3cWIPSDctUnassocStaLastDctTm_Object = MibTableColumn
hh3cWIPSDctUnassocStaLastDctTm = _Hh3cWIPSDctUnassocStaLastDctTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 11),
    _Hh3cWIPSDctUnassocStaLastDctTm_Type()
)
hh3cWIPSDctUnassocStaLastDctTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaLastDctTm.setStatus("current")
_Hh3cWIPSDctUnassocStaRptSensorNum_Type = Integer32
_Hh3cWIPSDctUnassocStaRptSensorNum_Object = MibTableColumn
hh3cWIPSDctUnassocStaRptSensorNum = _Hh3cWIPSDctUnassocStaRptSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 12),
    _Hh3cWIPSDctUnassocStaRptSensorNum_Type()
)
hh3cWIPSDctUnassocStaRptSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaRptSensorNum.setStatus("current")


class _Hh3cWIPSDctUnassocStaState_Type(Integer32):
    """Custom type hh3cWIPSDctUnassocStaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("association", 2),
          ("authentication", 1),
          ("deauthentication", 6),
          ("disassociation", 5),
          ("eapLogoff", 4),
          ("eapSuccess", 3),
          ("unassociation", 7))
    )


_Hh3cWIPSDctUnassocStaState_Type.__name__ = "Integer32"
_Hh3cWIPSDctUnassocStaState_Object = MibTableColumn
hh3cWIPSDctUnassocStaState = _Hh3cWIPSDctUnassocStaState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 13),
    _Hh3cWIPSDctUnassocStaState_Type()
)
hh3cWIPSDctUnassocStaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaState.setStatus("current")


class _Hh3cWIPSDctUnassocStaVendor_Type(OctetString):
    """Custom type hh3cWIPSDctUnassocStaVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cWIPSDctUnassocStaVendor_Type.__name__ = "OctetString"
_Hh3cWIPSDctUnassocStaVendor_Object = MibTableColumn
hh3cWIPSDctUnassocStaVendor = _Hh3cWIPSDctUnassocStaVendor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 17, 1, 14),
    _Hh3cWIPSDctUnassocStaVendor_Type()
)
hh3cWIPSDctUnassocStaVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaVendor.setStatus("current")
_Hh3cWIPSDctUnassocStaRptSensorTable_Object = MibTable
hh3cWIPSDctUnassocStaRptSensorTable = _Hh3cWIPSDctUnassocStaRptSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 18)
)
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaRptSensorTable.setStatus("current")
_Hh3cWIPSDctUnassocStaRptSensorEntry_Object = MibTableRow
hh3cWIPSDctUnassocStaRptSensorEntry = _Hh3cWIPSDctUnassocStaRptSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 18, 1)
)
hh3cWIPSDctUnassocStaRptSensorEntry.setIndexNames(
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctUnassocStaVSD"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctUnassocStaMac"),
    (0, "HH3C-WIPS-MIB", "hh3cWIPSDctUnassocStaRtpSensorName"),
)
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaRptSensorEntry.setStatus("current")


class _Hh3cWIPSDctUnassocStaRtpSensorName_Type(OctetString):
    """Custom type hh3cWIPSDctUnassocStaRtpSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cWIPSDctUnassocStaRtpSensorName_Type.__name__ = "OctetString"
_Hh3cWIPSDctUnassocStaRtpSensorName_Object = MibTableColumn
hh3cWIPSDctUnassocStaRtpSensorName = _Hh3cWIPSDctUnassocStaRtpSensorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 18, 1, 1),
    _Hh3cWIPSDctUnassocStaRtpSensorName_Type()
)
hh3cWIPSDctUnassocStaRtpSensorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaRtpSensorName.setStatus("current")


class _Hh3cWIPSDctUnassocStaRptSensorRadioId_Type(Integer32):
    """Custom type hh3cWIPSDctUnassocStaRptSensorRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cWIPSDctUnassocStaRptSensorRadioId_Type.__name__ = "Integer32"
_Hh3cWIPSDctUnassocStaRptSensorRadioId_Object = MibTableColumn
hh3cWIPSDctUnassocStaRptSensorRadioId = _Hh3cWIPSDctUnassocStaRptSensorRadioId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 18, 1, 2),
    _Hh3cWIPSDctUnassocStaRptSensorRadioId_Type()
)
hh3cWIPSDctUnassocStaRptSensorRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaRptSensorRadioId.setStatus("current")
_Hh3cWIPSDctUnassocStaRptRSSI_Type = Integer32
_Hh3cWIPSDctUnassocStaRptRSSI_Object = MibTableColumn
hh3cWIPSDctUnassocStaRptRSSI = _Hh3cWIPSDctUnassocStaRptRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 18, 1, 3),
    _Hh3cWIPSDctUnassocStaRptRSSI_Type()
)
hh3cWIPSDctUnassocStaRptRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaRptRSSI.setStatus("current")
_Hh3cWIPSDctUnassocStaLastRptTm_Type = TimeTicks
_Hh3cWIPSDctUnassocStaLastRptTm_Object = MibTableColumn
hh3cWIPSDctUnassocStaLastRptTm = _Hh3cWIPSDctUnassocStaLastRptTm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 2, 18, 1, 4),
    _Hh3cWIPSDctUnassocStaLastRptTm_Type()
)
hh3cWIPSDctUnassocStaLastRptTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWIPSDctUnassocStaLastRptTm.setStatus("current")
_Hh3cWIPSNotifyGroup_ObjectIdentity = ObjectIdentity
hh3cWIPSNotifyGroup = _Hh3cWIPSNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-WIPS-MIB",
    **{"Hh3cWIPSRadioType": Hh3cWIPSRadioType,
       "Hh3cWIPSDevStatus": Hh3cWIPSDevStatus,
       "Hh3cWIPSDevCategoryWay": Hh3cWIPSDevCategoryWay,
       "Hh3cWIPSDeviceCategoryType": Hh3cWIPSDeviceCategoryType,
       "Hh3cWIPSAPCategoryType": Hh3cWIPSAPCategoryType,
       "Hh3cWIPSClientCategoryType": Hh3cWIPSClientCategoryType,
       "Hh3cWIPSChannel": Hh3cWIPSChannel,
       "Hh3cWIPSEncryptMethod": Hh3cWIPSEncryptMethod,
       "Hh3cWIPSAuthMethod": Hh3cWIPSAuthMethod,
       "Hh3cWIPSAPClassifyType": Hh3cWIPSAPClassifyType,
       "Hh3cWIPSAPSecurityType": Hh3cWIPSAPSecurityType,
       "hh3cWIPS": hh3cWIPS,
       "hh3cWIPSConfigGroup": hh3cWIPSConfigGroup,
       "hh3cWIPSGlobalConfigGroup": hh3cWIPSGlobalConfigGroup,
       "hh3cWIPSEnable": hh3cWIPSEnable,
       "hh3cWIPSSensorLicenseNum": hh3cWIPSSensorLicenseNum,
       "hh3cWIPSBlocklistAction": hh3cWIPSBlocklistAction,
       "hh3cWIPSAPInactiveTime": hh3cWIPSAPInactiveTime,
       "hh3cWIPSSTAInactiveTime": hh3cWIPSSTAInactiveTime,
       "hh3cWIPSDevAgingTime": hh3cWIPSDevAgingTime,
       "hh3cWIPSStatisticPeriod": hh3cWIPSStatisticPeriod,
       "hh3cWIPSReclassificationPeriod": hh3cWIPSReclassificationPeriod,
       "hh3cWIPSResetAllTrustList": hh3cWIPSResetAllTrustList,
       "hh3cWIPSResetAllBlockList": hh3cWIPSResetAllBlockList,
       "hh3cWIPSResetAllIgnoreList": hh3cWIPSResetAllIgnoreList,
       "hh3cWIPSResetAllCtmList": hh3cWIPSResetAllCtmList,
       "hh3cWIPSPermitChlBitMap": hh3cWIPSPermitChlBitMap,
       "hh3cWIPSDynamicTrustListAgingTime": hh3cWIPSDynamicTrustListAgingTime,
       "hh3cWIPSDevUpdateTime": hh3cWIPSDevUpdateTime,
       "hh3cWIPSADOSEnable": hh3cWIPSADOSEnable,
       "hh3cWIPSAccessFlowScanEnable": hh3cWIPSAccessFlowScanEnable,
       "hh3cWIPSVsdConfigGroup": hh3cWIPSVsdConfigGroup,
       "hh3cWIPSVsdTable": hh3cWIPSVsdTable,
       "hh3cWIPSVsdEntry": hh3cWIPSVsdEntry,
       "hh3cWIPSVsdNameCfg": hh3cWIPSVsdNameCfg,
       "hh3cWIPSVsdRowStatus": hh3cWIPSVsdRowStatus,
       "hh3cWIPSVsdAtkDctPolicyNameCfg": hh3cWIPSVsdAtkDctPolicyNameCfg,
       "hh3cWIPSVsdCtmPolicyNameCfg": hh3cWIPSVsdCtmPolicyNameCfg,
       "hh3cWIPSVsdSigPolicyNameCfg": hh3cWIPSVsdSigPolicyNameCfg,
       "hh3cWIPSVsdMalPktPolicyNameCfg": hh3cWIPSVsdMalPktPolicyNameCfg,
       "hh3cWIPSRule2VsdTable": hh3cWIPSRule2VsdTable,
       "hh3cWIPSRule2VsdEntry": hh3cWIPSRule2VsdEntry,
       "hh3cWIPSRule2VsdAPClaRuleNameCfg": hh3cWIPSRule2VsdAPClaRuleNameCfg,
       "hh3cWIPSRule2VsdRowStatus": hh3cWIPSRule2VsdRowStatus,
       "hh3cWIPSRule2VsdPrecedence": hh3cWIPSRule2VsdPrecedence,
       "hh3cWIPSSensor2VsdTable": hh3cWIPSSensor2VsdTable,
       "hh3cWIPSSensor2VsdEntry": hh3cWIPSSensor2VsdEntry,
       "hh3cWIPSSensorNameCfg": hh3cWIPSSensorNameCfg,
       "hh3cWIPSSensor2VsdRowStatus": hh3cWIPSSensor2VsdRowStatus,
       "hh3cWIPSSensorState": hh3cWIPSSensorState,
       "hh3cWIPSSensorRadioTable": hh3cWIPSSensorRadioTable,
       "hh3cWIPSSensorRadioEntry": hh3cWIPSSensorRadioEntry,
       "hh3cWIPSSensorRadioRadioId": hh3cWIPSSensorRadioRadioId,
       "hh3cWIPSSensorRadioScanMode": hh3cWIPSSensorRadioScanMode,
       "hh3cWIPSAPClaRuleTable": hh3cWIPSAPClaRuleTable,
       "hh3cWIPSAPClaRuleEntry": hh3cWIPSAPClaRuleEntry,
       "hh3cWIPSAPClaRuleName": hh3cWIPSAPClaRuleName,
       "hh3cWIPSAPClaRowStatus": hh3cWIPSAPClaRowStatus,
       "hh3cWIPSAPClaSeverityLevel": hh3cWIPSAPClaSeverityLevel,
       "hh3cWIPSAPClaRuleMatchAll": hh3cWIPSAPClaRuleMatchAll,
       "hh3cWIPSAPClaType": hh3cWIPSAPClaType,
       "hh3cWIPSAPClaSubRuleSSIDOperator": hh3cWIPSAPClaSubRuleSSIDOperator,
       "hh3cWIPSAPClaSubRuleSSIDCase": hh3cWIPSAPClaSubRuleSSIDCase,
       "hh3cWIPSAPClaSubRuleSSID": hh3cWIPSAPClaSubRuleSSID,
       "hh3cWIPSSecurityType": hh3cWIPSSecurityType,
       "hh3cWIPSSecurityTypeMatch": hh3cWIPSSecurityTypeMatch,
       "hh3cWIPSAPAuthType": hh3cWIPSAPAuthType,
       "hh3cWIPSMaxRSSIValue": hh3cWIPSMaxRSSIValue,
       "hh3cWIPSMinRSSIValue": hh3cWIPSMinRSSIValue,
       "hh3cWIPSMaxDuration": hh3cWIPSMaxDuration,
       "hh3cWIPSMinDuration": hh3cWIPSMinDuration,
       "hh3cWIPSMaxAPNum": hh3cWIPSMaxAPNum,
       "hh3cWIPSMinAPNum": hh3cWIPSMinAPNum,
       "hh3cWIPSMaxClientNum": hh3cWIPSMaxClientNum,
       "hh3cWIPSMinClientNum": hh3cWIPSMinClientNum,
       "hh3cWIPSOUIInfo": hh3cWIPSOUIInfo,
       "hh3cWIPSVendorInfo": hh3cWIPSVendorInfo,
       "hh3cWIPSAPAuthTypeMatch": hh3cWIPSAPAuthTypeMatch,
       "hh3cWIPSAtkDctPolicyCfgGroup": hh3cWIPSAtkDctPolicyCfgGroup,
       "hh3cWIPSAtkDctPolicyCfgSupportSet": hh3cWIPSAtkDctPolicyCfgSupportSet,
       "hh3cWIPSAtkDctPolicyCfgTable": hh3cWIPSAtkDctPolicyCfgTable,
       "hh3cWIPSAtkDctPolicyCfgEntry": hh3cWIPSAtkDctPolicyCfgEntry,
       "hh3cWIPSAtkDctPolicyName": hh3cWIPSAtkDctPolicyName,
       "hh3cWIPSAtkDctPolicyCfgRowStatus": hh3cWIPSAtkDctPolicyCfgRowStatus,
       "hh3cWIPSAtkDctPolicyBitString": hh3cWIPSAtkDctPolicyBitString,
       "hh3cWIPSAtkDctPolicyAPFloodQT": hh3cWIPSAtkDctPolicyAPFloodQT,
       "hh3cWIPSAtkDctPolicyAPSpoofQT": hh3cWIPSAtkDctPolicyAPSpoofQT,
       "hh3cWIPSAtkDctPolicyCliSpoofQT": hh3cWIPSAtkDctPolicyCliSpoofQT,
       "hh3cWIPSAtkDctPolicyDosAssoQT": hh3cWIPSAtkDctPolicyDosAssoQT,
       "hh3cWIPSAtkDctPolicyDosAuthQT": hh3cWIPSAtkDctPolicyDosAuthQT,
       "hh3cWIPSAtkDctPolicyDosEAPOLStartQT": hh3cWIPSAtkDctPolicyDosEAPOLStartQT,
       "hh3cWIPSAtkDctPolicyDosReAssoQT": hh3cWIPSAtkDctPolicyDosReAssoQT,
       "hh3cWIPSAtkDctPolicyWeakIVQT": hh3cWIPSAtkDctPolicyWeakIVQT,
       "hh3cWIPSAtkDctPolicyInvalidOUIAction": hh3cWIPSAtkDctPolicyInvalidOUIAction,
       "hh3cWIPSAtkDctPolicyUnencryptedAuthApQT": hh3cWIPSAtkDctPolicyUnencryptedAuthApQT,
       "hh3cWIPSAtkDctPolicyUnencryptedAuthClientQT": hh3cWIPSAtkDctPolicyUnencryptedAuthClientQT,
       "hh3cWIPSAtkDctPolicyPSAttackQT": hh3cWIPSAtkDctPolicyPSAttackQT,
       "hh3cWIPSAtkDctPolicyPSAttackMinOffPacket": hh3cWIPSAtkDctPolicyPSAttackMinOffPacket,
       "hh3cWIPSAtkDctPolicyPSAttackOnOffPercent": hh3cWIPSAtkDctPolicyPSAttackOnOffPercent,
       "hh3cWIPSAtkDctPolicyApImpersonationQT": hh3cWIPSAtkDctPolicyApImpersonationQT,
       "hh3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold": hh3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold,
       "hh3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime": hh3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime,
       "hh3cWIPSAtkDctPolicySoftApConvertTime": hh3cWIPSAtkDctPolicySoftApConvertTime,
       "hh3cWIPSStaticCtmListCfgTable": hh3cWIPSStaticCtmListCfgTable,
       "hh3cWIPSStaticCtmListCfgEntry": hh3cWIPSStaticCtmListCfgEntry,
       "hh3cWIPSStaticCtmListMAC": hh3cWIPSStaticCtmListMAC,
       "hh3cWIPSStaticCtmListRowStatus": hh3cWIPSStaticCtmListRowStatus,
       "hh3cWIPSStaticBlockListCfgTable": hh3cWIPSStaticBlockListCfgTable,
       "hh3cWIPSStaticBlockListCfgEntry": hh3cWIPSStaticBlockListCfgEntry,
       "hh3cWIPSStaticBlockListMAC": hh3cWIPSStaticBlockListMAC,
       "hh3cWIPSStaticBlockListRowStatus": hh3cWIPSStaticBlockListRowStatus,
       "hh3cWIPSStaticTrustListCfgTable": hh3cWIPSStaticTrustListCfgTable,
       "hh3cWIPSStaticTrustListCfgEntry": hh3cWIPSStaticTrustListCfgEntry,
       "hh3cWIPSStaticTrustListMAC": hh3cWIPSStaticTrustListMAC,
       "hh3cWIPSStaticTrustListRowStatus": hh3cWIPSStaticTrustListRowStatus,
       "hh3cWIPSIgnoreListCfgTable": hh3cWIPSIgnoreListCfgTable,
       "hh3cWIPSIgnoreListCfgEntry": hh3cWIPSIgnoreListCfgEntry,
       "hh3cWIPSIgnoreListMAC": hh3cWIPSIgnoreListMAC,
       "hh3cWIPSIgnoreListRowStatus": hh3cWIPSIgnoreListRowStatus,
       "hh3cWIPSDctModeTable": hh3cWIPSDctModeTable,
       "hh3cWIPSDctModeEntry": hh3cWIPSDctModeEntry,
       "hh3cWIPSDctModeAPName": hh3cWIPSDctModeAPName,
       "hh3cWIPSDctModeRadio": hh3cWIPSDctModeRadio,
       "hh3cWIPSDctModeScanMode": hh3cWIPSDctModeScanMode,
       "hh3cWIPSDctModeRowStatus": hh3cWIPSDctModeRowStatus,
       "hh3cWIPSSigConfigGroup": hh3cWIPSSigConfigGroup,
       "hh3cWIPSSigPolicyTable": hh3cWIPSSigPolicyTable,
       "hh3cWIPSSigPolicyEntry": hh3cWIPSSigPolicyEntry,
       "hh3cWIPSSigPolicyNameCfg": hh3cWIPSSigPolicyNameCfg,
       "hh3cWIPSSigPolicyRowStatus": hh3cWIPSSigPolicyRowStatus,
       "hh3cWIPSSigRule2PolicyTable": hh3cWIPSSigRule2PolicyTable,
       "hh3cWIPSSigRule2PolicyEntry": hh3cWIPSSigRule2PolicyEntry,
       "hh3cWIPSSigRule2PolicySigRuleIDCfg": hh3cWIPSSigRule2PolicySigRuleIDCfg,
       "hh3cWIPSSigRule2PolicyRowStatus": hh3cWIPSSigRule2PolicyRowStatus,
       "hh3cWIPSSigRule2PolicyPrecedence": hh3cWIPSSigRule2PolicyPrecedence,
       "hh3cWIPSSigRuleTable": hh3cWIPSSigRuleTable,
       "hh3cWIPSSigRuleEntry": hh3cWIPSSigRuleEntry,
       "hh3cWIPSSigRuleName": hh3cWIPSSigRuleName,
       "hh3cWIPSSigRuleID": hh3cWIPSSigRuleID,
       "hh3cWIPSSigRuleRowStatus": hh3cWIPSSigRuleRowStatus,
       "hh3cWIPSSigSubRuleMatchAll": hh3cWIPSSigSubRuleMatchAll,
       "hh3cWIPSSigRuleDctPeriod": hh3cWIPSSigRuleDctPeriod,
       "hh3cWIPSSigRuleTrackMethod": hh3cWIPSSigRuleTrackMethod,
       "hh3cWIPSSigRuleDctThresholdPerMAC": hh3cWIPSSigRuleDctThresholdPerMAC,
       "hh3cWIPSSigRuleDctThresholdPerSig": hh3cWIPSSigRuleDctThresholdPerSig,
       "hh3cWIPSSigRuleActionEvtLevel": hh3cWIPSSigRuleActionEvtLevel,
       "hh3cWIPSSigRuleQuietTime": hh3cWIPSSigRuleQuietTime,
       "hh3cWIPSSigSubRuleFrameType": hh3cWIPSSigSubRuleFrameType,
       "hh3cWIPSSigSubRuleFrameSubType": hh3cWIPSSigSubRuleFrameSubType,
       "hh3cWIPSSigSubRuleMac": hh3cWIPSSigSubRuleMac,
       "hh3cWIPSSigSubRuleMacType": hh3cWIPSSigSubRuleMacType,
       "hh3cWIPSSigSubRuleSeqNumMin": hh3cWIPSSigSubRuleSeqNumMin,
       "hh3cWIPSSigSubRuleSeqNumMax": hh3cWIPSSigSubRuleSeqNumMax,
       "hh3cWIPSSigSubRuleSSIDLenMin": hh3cWIPSSigSubRuleSSIDLenMin,
       "hh3cWIPSSigSubRuleSSIDLenMax": hh3cWIPSSigSubRuleSSIDLenMax,
       "hh3cWIPSSigSubRuleSSID": hh3cWIPSSigSubRuleSSID,
       "hh3cWIPSSigSubRuleSSIDOpe": hh3cWIPSSigSubRuleSSIDOpe,
       "hh3cWIPSSigSubRuleSSIDCase": hh3cWIPSSigSubRuleSSIDCase,
       "hh3cWIPSSigSubRulePatternTable": hh3cWIPSSigSubRulePatternTable,
       "hh3cWIPSSigSubRulePatternEntry": hh3cWIPSSigSubRulePatternEntry,
       "hh3cWIPSSigSubRulePatternID": hh3cWIPSSigSubRulePatternID,
       "hh3cWIPSSigSubRuleRowStatus": hh3cWIPSSigSubRuleRowStatus,
       "hh3cWIPSSigSubRulePatternName": hh3cWIPSSigSubRulePatternName,
       "hh3cWIPSSigSubRulePatternOffset": hh3cWIPSSigSubRulePatternOffset,
       "hh3cWIPSSigSubRulePatternMask": hh3cWIPSSigSubRulePatternMask,
       "hh3cWIPSSigSubRulePatternValueMin": hh3cWIPSSigSubRulePatternValueMin,
       "hh3cWIPSSigSubRulePatternValueMax": hh3cWIPSSigSubRulePatternValueMax,
       "hh3cWIPSSigSubRulePatternFromPayload": hh3cWIPSSigSubRulePatternFromPayload,
       "hh3cWIPSCtmConfigGroup": hh3cWIPSCtmConfigGroup,
       "hh3cWIPSCtmPolicyCfgSupportSet": hh3cWIPSCtmPolicyCfgSupportSet,
       "hh3cWIPSCtmPolicyTable": hh3cWIPSCtmPolicyTable,
       "hh3cWIPSCtmPolicyEntry": hh3cWIPSCtmPolicyEntry,
       "hh3cWIPSCtmPolicyName": hh3cWIPSCtmPolicyName,
       "hh3cWIPSCtmPolicyCfgRowStatus": hh3cWIPSCtmPolicyCfgRowStatus,
       "hh3cWIPSCtmPolicyBitString": hh3cWIPSCtmPolicyBitString,
       "hh3cWIPSCtmPolicyFixedChl": hh3cWIPSCtmPolicyFixedChl,
       "hh3cWIPSCtmPolicyRogueAPPre": hh3cWIPSCtmPolicyRogueAPPre,
       "hh3cWIPSCtmPolicyPtRogueAPPre": hh3cWIPSCtmPolicyPtRogueAPPre,
       "hh3cWIPSCtmPolicyMisconfAPPre": hh3cWIPSCtmPolicyMisconfAPPre,
       "hh3cWIPSCtmPolicyExternalAPPre": hh3cWIPSCtmPolicyExternalAPPre,
       "hh3cWIPSCtmPolicyPtExternalAPPre": hh3cWIPSCtmPolicyPtExternalAPPre,
       "hh3cWIPSCtmPolicyUncateAPPre": hh3cWIPSCtmPolicyUncateAPPre,
       "hh3cWIPSCtmPolicyPtAuthAPPre": hh3cWIPSCtmPolicyPtAuthAPPre,
       "hh3cWIPSCtmPolicyMisassoStaPre": hh3cWIPSCtmPolicyMisassoStaPre,
       "hh3cWIPSCtmPolicyUncateStaPre": hh3cWIPSCtmPolicyUncateStaPre,
       "hh3cWIPSCtmPolicyUnauthStaPre": hh3cWIPSCtmPolicyUnauthStaPre,
       "hh3cWIPSCtmPolicyDevListTable": hh3cWIPSCtmPolicyDevListTable,
       "hh3cWIPSCtmPolicyDevListEntry": hh3cWIPSCtmPolicyDevListEntry,
       "hh3cWIPSCtmPolicyDevMAC": hh3cWIPSCtmPolicyDevMAC,
       "hh3cWIPSCtmPolicyDevRowStatus": hh3cWIPSCtmPolicyDevRowStatus,
       "hh3cWIPSMalPktDctConfigGroup": hh3cWIPSMalPktDctConfigGroup,
       "hh3cWIPSMalPktDctCfgLogSupportSet": hh3cWIPSMalPktDctCfgLogSupportSet,
       "hh3cWIPSMalPktDctCfgTrapSupportSet": hh3cWIPSMalPktDctCfgTrapSupportSet,
       "hh3cWIPSMalPktDctPolicyTable": hh3cWIPSMalPktDctPolicyTable,
       "hh3cWIPSMalPktDctPolicyEntry": hh3cWIPSMalPktDctPolicyEntry,
       "hh3cWIPSMalPktDctPolicyName": hh3cWIPSMalPktDctPolicyName,
       "hh3cWIPSMalPktDctPolicyCfgRowStatus": hh3cWIPSMalPktDctPolicyCfgRowStatus,
       "hh3cWIPSMalPktDctPolicyLogBitString": hh3cWIPSMalPktDctPolicyLogBitString,
       "hh3cWIPSMalPktDctPolicyTrapBitString": hh3cWIPSMalPktDctPolicyTrapBitString,
       "hh3cWIPSMalPktDctPolicyDurationThreshold": hh3cWIPSMalPktDctPolicyDurationThreshold,
       "hh3cWIPSMalPktDctPolicyQuietTime": hh3cWIPSMalPktDctPolicyQuietTime,
       "hh3cWIPSStaticTrustOUIListCfgTable": hh3cWIPSStaticTrustOUIListCfgTable,
       "hh3cWIPSStaticTrustOUIListCfgEntry": hh3cWIPSStaticTrustOUIListCfgEntry,
       "hh3cWIPSStaticTrustOUIListOUI": hh3cWIPSStaticTrustOUIListOUI,
       "hh3cWIPSStaticTrustOUIListRowStatus": hh3cWIPSStaticTrustOUIListRowStatus,
       "hh3cWIPSStaticTrustVendorListCfgTable": hh3cWIPSStaticTrustVendorListCfgTable,
       "hh3cWIPSStaticTrustVendorListCfgEntry": hh3cWIPSStaticTrustVendorListCfgEntry,
       "hh3cWIPSStaticTrustVendorListVendor": hh3cWIPSStaticTrustVendorListVendor,
       "hh3cWIPSStaticTrustVendorListRowStatus": hh3cWIPSStaticTrustVendorListRowStatus,
       "hh3cWIPSDetectGroup": hh3cWIPSDetectGroup,
       "hh3cWIPSDctAPTable": hh3cWIPSDctAPTable,
       "hh3cWIPSDctAPEntry": hh3cWIPSDctAPEntry,
       "hh3cWIPSDctAPVSD": hh3cWIPSDctAPVSD,
       "hh3cWIPSDctAPBSSID": hh3cWIPSDctAPBSSID,
       "hh3cWIPSDctAPRunningTime": hh3cWIPSDctAPRunningTime,
       "hh3cWIPSDctAPRunTmLastUpdateTm": hh3cWIPSDctAPRunTmLastUpdateTm,
       "hh3cWIPSDctAPIsCountered": hh3cWIPSDctAPIsCountered,
       "hh3cWIPSDctAPWorkChannel": hh3cWIPSDctAPWorkChannel,
       "hh3cWIPSDctAPRadioType": hh3cWIPSDctAPRadioType,
       "hh3cWIPSDctAPAuthMethod": hh3cWIPSDctAPAuthMethod,
       "hh3cWIPSDctAPEncryptMethod": hh3cWIPSDctAPEncryptMethod,
       "hh3cWIPSDctAPSecurity": hh3cWIPSDctAPSecurity,
       "hh3cWIPSDctAPSeverityLevel": hh3cWIPSDctAPSeverityLevel,
       "hh3cWIPSDctAPLastDctTm": hh3cWIPSDctAPLastDctTm,
       "hh3cWIPSDctAPFirstDctTm": hh3cWIPSDctAPFirstDctTm,
       "hh3cWIPSDctAPAdd2BlackList": hh3cWIPSDctAPAdd2BlackList,
       "hh3cWIPSDctAPAdd2WhiteList": hh3cWIPSDctAPAdd2WhiteList,
       "hh3cWIPSDctAPAdd2IgnoreList": hh3cWIPSDctAPAdd2IgnoreList,
       "hh3cWIPSDctAPAdd2CtmList": hh3cWIPSDctAPAdd2CtmList,
       "hh3cWIPSDctAPCategory": hh3cWIPSDctAPCategory,
       "hh3cWIPSDctAPCategoryWay": hh3cWIPSDctAPCategoryWay,
       "hh3cWIPSDctAPStatus": hh3cWIPSDctAPStatus,
       "hh3cWIPSDctAPSSID": hh3cWIPSDctAPSSID,
       "hh3cWIPSDctAPAttachStaNum": hh3cWIPSDctAPAttachStaNum,
       "hh3cWIPSDctAPRptSensorNum": hh3cWIPSDctAPRptSensorNum,
       "hh3cWIPSDctAPVendor": hh3cWIPSDctAPVendor,
       "hh3cWIPSDctAPAttachStaTable": hh3cWIPSDctAPAttachStaTable,
       "hh3cWIPSDctAPAttachStaEntry": hh3cWIPSDctAPAttachStaEntry,
       "hh3cWIPSDctAPAttachStaMac": hh3cWIPSDctAPAttachStaMac,
       "hh3cWIPSDctAPAttachStaRowStatus": hh3cWIPSDctAPAttachStaRowStatus,
       "hh3cWIPSDctAPRptSensorTable": hh3cWIPSDctAPRptSensorTable,
       "hh3cWIPSDctAPRptSensorEntry": hh3cWIPSDctAPRptSensorEntry,
       "hh3cWIPSDctAPRptSensorName": hh3cWIPSDctAPRptSensorName,
       "hh3cWIPSDctAPRptSensorRadioId": hh3cWIPSDctAPRptSensorRadioId,
       "hh3cWIPSDctAPRptRSSI": hh3cWIPSDctAPRptRSSI,
       "hh3cWIPSDctAPLastRptTm": hh3cWIPSDctAPLastRptTm,
       "hh3cWIPSDctStaTable": hh3cWIPSDctStaTable,
       "hh3cWIPSDctStaEntry": hh3cWIPSDctStaEntry,
       "hh3cWIPSDctStaVSD": hh3cWIPSDctStaVSD,
       "hh3cWIPSDctStaMac": hh3cWIPSDctStaMac,
       "hh3cWIPSDctStaAssocBSSID": hh3cWIPSDctStaAssocBSSID,
       "hh3cWIPSDctStaStatus": hh3cWIPSDctStaStatus,
       "hh3cWIPSDctStaCategory": hh3cWIPSDctStaCategory,
       "hh3cWIPSDctStaRadioType": hh3cWIPSDctStaRadioType,
       "hh3cWIPSDctStaWorkChannel": hh3cWIPSDctStaWorkChannel,
       "hh3cWIPSDctStaIsCountered": hh3cWIPSDctStaIsCountered,
       "hh3cWIPSDctStaAdd2BlackList": hh3cWIPSDctStaAdd2BlackList,
       "hh3cWIPSDctStaAdd2WhiteList": hh3cWIPSDctStaAdd2WhiteList,
       "hh3cWIPSDctStaAdd2IgnoreList": hh3cWIPSDctStaAdd2IgnoreList,
       "hh3cWIPSDctStaAdd2CtmList": hh3cWIPSDctStaAdd2CtmList,
       "hh3cWIPSDctStaFirstDctTm": hh3cWIPSDctStaFirstDctTm,
       "hh3cWIPSDctStaLastDctTm": hh3cWIPSDctStaLastDctTm,
       "hh3cWIPSDctStaRptSensorNum": hh3cWIPSDctStaRptSensorNum,
       "hh3cWIPSDctStaState": hh3cWIPSDctStaState,
       "hh3cWIPSDctStaVendor": hh3cWIPSDctStaVendor,
       "hh3cWIPSDctStaRptSensorTable": hh3cWIPSDctStaRptSensorTable,
       "hh3cWIPSDctStaRptSensorEntry": hh3cWIPSDctStaRptSensorEntry,
       "hh3cWIPSDctStaRtpSensorName": hh3cWIPSDctStaRtpSensorName,
       "hh3cWIPSDctStaRptSensorRadioId": hh3cWIPSDctStaRptSensorRadioId,
       "hh3cWIPSDctStaRptRSSI": hh3cWIPSDctStaRptRSSI,
       "hh3cWIPSDctStaLastRptTm": hh3cWIPSDctStaLastRptTm,
       "hh3cWIPSDctSSIDTable": hh3cWIPSDctSSIDTable,
       "hh3cWIPSDctSSIDEntry": hh3cWIPSDctSSIDEntry,
       "hh3cWIPSDctNetworkVSD": hh3cWIPSDctNetworkVSD,
       "hh3cWIPSDctNetworkSSID": hh3cWIPSDctNetworkSSID,
       "hh3cWIPSDctNetworkCfg": hh3cWIPSDctNetworkCfg,
       "hh3cWIPSDctNetworkFirstRptTm": hh3cWIPSDctNetworkFirstRptTm,
       "hh3cWIPSDctNetworkLastRptTm": hh3cWIPSDctNetworkLastRptTm,
       "hh3cWIPSDctNetworkStatus": hh3cWIPSDctNetworkStatus,
       "hh3cWIPSDctNetworkSSIDHide": hh3cWIPSDctNetworkSSIDHide,
       "hh3cWIPSDctNetworkBSSNum": hh3cWIPSDctNetworkBSSNum,
       "hh3cWIPSDctSSIDBSSTable": hh3cWIPSDctSSIDBSSTable,
       "hh3cWIPSDctSSIDBSSEntry": hh3cWIPSDctSSIDBSSEntry,
       "hh3cWIPSDctNetworkBSSID": hh3cWIPSDctNetworkBSSID,
       "hh3cWIPSDctNetworkBSSWorkChl": hh3cWIPSDctNetworkBSSWorkChl,
       "hh3cWIPSDctNetworkBSSStaNum": hh3cWIPSDctNetworkBSSStaNum,
       "hh3cWIPSBlockListTable": hh3cWIPSBlockListTable,
       "hh3cWIPSBlockListEntry": hh3cWIPSBlockListEntry,
       "hh3cWIPSBlockListMacAddress": hh3cWIPSBlockListMacAddress,
       "hh3cWIPSBlockListStatus": hh3cWIPSBlockListStatus,
       "hh3cWIPSChannelTable": hh3cWIPSChannelTable,
       "hh3cWIPSChannelEntry": hh3cWIPSChannelEntry,
       "hh3cWIPSChannelNum": hh3cWIPSChannelNum,
       "hh3cWIPSChannelRadioType": hh3cWIPSChannelRadioType,
       "hh3cWIPSChannelIsPermitted": hh3cWIPSChannelIsPermitted,
       "hh3cWIPSChannelLastRptTm": hh3cWIPSChannelLastRptTm,
       "hh3cWIPSCountermeasureListTable": hh3cWIPSCountermeasureListTable,
       "hh3cWIPSCountermeasureListEntry": hh3cWIPSCountermeasureListEntry,
       "hh3cWIPSCtmListMacAddress": hh3cWIPSCtmListMacAddress,
       "hh3cWIPSCtmListLastestWorkChl": hh3cWIPSCtmListLastestWorkChl,
       "hh3cWIPSCtmListFirstTm": hh3cWIPSCtmListFirstTm,
       "hh3cWIPSCtmListLastTm": hh3cWIPSCtmListLastTm,
       "hh3cWIPSCtmListQurCnt": hh3cWIPSCtmListQurCnt,
       "hh3cWIPSCtmListSensorNum": hh3cWIPSCtmListSensorNum,
       "hh3cWIPSIgnoreListTable": hh3cWIPSIgnoreListTable,
       "hh3cWIPSIgnoreListEntry": hh3cWIPSIgnoreListEntry,
       "hh3cWIPSIgnoreListMacAddress": hh3cWIPSIgnoreListMacAddress,
       "hh3cWIPSIgnoreListFirstIgnoreTm": hh3cWIPSIgnoreListFirstIgnoreTm,
       "hh3cWIPSIgnoreListLastIgnoreTm": hh3cWIPSIgnoreListLastIgnoreTm,
       "hh3cWIPSIgnoreListIgnoreCnt": hh3cWIPSIgnoreListIgnoreCnt,
       "hh3cWIPSTrustListTable": hh3cWIPSTrustListTable,
       "hh3cWIPSTrustListEntry": hh3cWIPSTrustListEntry,
       "hh3cWIPSTrustListMacAddress": hh3cWIPSTrustListMacAddress,
       "hh3cWIPSTrustListStatus": hh3cWIPSTrustListStatus,
       "hh3cWIPSChlStatTable": hh3cWIPSChlStatTable,
       "hh3cWIPSChlStatEntry": hh3cWIPSChlStatEntry,
       "hh3cWIPSChlStatSensorMacAddr": hh3cWIPSChlStatSensorMacAddr,
       "hh3cWIPSChlStatChannel": hh3cWIPSChlStatChannel,
       "hh3cWIPSChlStatTotalPkt": hh3cWIPSChlStatTotalPkt,
       "hh3cWIPSChlStatTotalByte": hh3cWIPSChlStatTotalByte,
       "hh3cWIPSChlStatBmcastPkt": hh3cWIPSChlStatBmcastPkt,
       "hh3cWIPSChlStatBmcastByte": hh3cWIPSChlStatBmcastByte,
       "hh3cWIPSChlStatUnicastPkt": hh3cWIPSChlStatUnicastPkt,
       "hh3cWIPSChlStatUnicastByte": hh3cWIPSChlStatUnicastByte,
       "hh3cWIPSChlStatManagement": hh3cWIPSChlStatManagement,
       "hh3cWIPSChlStatControl": hh3cWIPSChlStatControl,
       "hh3cWIPSChlStatData": hh3cWIPSChlStatData,
       "hh3cWIPSChlStatBeacon": hh3cWIPSChlStatBeacon,
       "hh3cWIPSChlStatRTS": hh3cWIPSChlStatRTS,
       "hh3cWIPSChlStatCTS": hh3cWIPSChlStatCTS,
       "hh3cWIPSChlStatProbeRequest": hh3cWIPSChlStatProbeRequest,
       "hh3cWIPSChlStatProbeResponse": hh3cWIPSChlStatProbeResponse,
       "hh3cWIPSChlStatFragment": hh3cWIPSChlStatFragment,
       "hh3cWIPSChlStatRetry": hh3cWIPSChlStatRetry,
       "hh3cWIPSChlStatEapSuccess": hh3cWIPSChlStatEapSuccess,
       "hh3cWIPSChlStatEapFailure": hh3cWIPSChlStatEapFailure,
       "hh3cWIPSChlStatEapolStart": hh3cWIPSChlStatEapolStart,
       "hh3cWIPSChlStatEapolLogoff": hh3cWIPSChlStatEapolLogoff,
       "hh3cWIPSChlStatAssocRequest": hh3cWIPSChlStatAssocRequest,
       "hh3cWIPSChlStatAssocResponse": hh3cWIPSChlStatAssocResponse,
       "hh3cWIPSChlStatUnicastDisassoc": hh3cWIPSChlStatUnicastDisassoc,
       "hh3cWIPSChlStatBroadcastDisassoc": hh3cWIPSChlStatBroadcastDisassoc,
       "hh3cWIPSChlStatAuthentication": hh3cWIPSChlStatAuthentication,
       "hh3cWIPSChlStatUnicastDeauthen": hh3cWIPSChlStatUnicastDeauthen,
       "hh3cWIPSChlStatBroadcastDeauthen": hh3cWIPSChlStatBroadcastDeauthen,
       "hh3cWIPSChlStatMalformed": hh3cWIPSChlStatMalformed,
       "hh3cWIPSDevStatTable": hh3cWIPSDevStatTable,
       "hh3cWIPSDevStatEntry": hh3cWIPSDevStatEntry,
       "hh3cWIPSDevStatSensorMacAddr": hh3cWIPSDevStatSensorMacAddr,
       "hh3cWIPSDevStatDevMacAddress": hh3cWIPSDevStatDevMacAddress,
       "hh3cWIPSDevStatChannel": hh3cWIPSDevStatChannel,
       "hh3cWIPSDevStatTxTotalPkt": hh3cWIPSDevStatTxTotalPkt,
       "hh3cWIPSDevStatTxTotalByte": hh3cWIPSDevStatTxTotalByte,
       "hh3cWIPSDevStatTxBMcastPkt": hh3cWIPSDevStatTxBMcastPkt,
       "hh3cWIPSDevStatTxBMcastByte": hh3cWIPSDevStatTxBMcastByte,
       "hh3cWIPSDevStatTxUnicastPkt": hh3cWIPSDevStatTxUnicastPkt,
       "hh3cWIPSDevStatTxUnicastByte": hh3cWIPSDevStatTxUnicastByte,
       "hh3cWIPSDevStatTxMgmt": hh3cWIPSDevStatTxMgmt,
       "hh3cWIPSDevStatTxCtrl": hh3cWIPSDevStatTxCtrl,
       "hh3cWIPSDevStatTxData": hh3cWIPSDevStatTxData,
       "hh3cWIPSDevStatTxBeacon": hh3cWIPSDevStatTxBeacon,
       "hh3cWIPSDevStatTxRTS": hh3cWIPSDevStatTxRTS,
       "hh3cWIPSDevStatTxProbeRequest": hh3cWIPSDevStatTxProbeRequest,
       "hh3cWIPSDevStatTxProbeResponse": hh3cWIPSDevStatTxProbeResponse,
       "hh3cWIPSDevStatTxFragment": hh3cWIPSDevStatTxFragment,
       "hh3cWIPSDevStatTxRetry": hh3cWIPSDevStatTxRetry,
       "hh3cWIPSDevStatTxAssocRequest": hh3cWIPSDevStatTxAssocRequest,
       "hh3cWIPSDevStatTxAssocResponse": hh3cWIPSDevStatTxAssocResponse,
       "hh3cWIPSDevStatTxUnicastDisassoc": hh3cWIPSDevStatTxUnicastDisassoc,
       "hh3cWIPSDevStatTxBcastDisassoc": hh3cWIPSDevStatTxBcastDisassoc,
       "hh3cWIPSDevStatTxAuth": hh3cWIPSDevStatTxAuth,
       "hh3cWIPSDevStatTxUnicastDeauth": hh3cWIPSDevStatTxUnicastDeauth,
       "hh3cWIPSDevStatTxBcastDeauth": hh3cWIPSDevStatTxBcastDeauth,
       "hh3cWIPSDevStatTxEAPSuccess": hh3cWIPSDevStatTxEAPSuccess,
       "hh3cWIPSDevStatTxEAPFailure": hh3cWIPSDevStatTxEAPFailure,
       "hh3cWIPSDevStatTxEAPOLStart": hh3cWIPSDevStatTxEAPOLStart,
       "hh3cWIPSDevStatTxEAPOLLogOff": hh3cWIPSDevStatTxEAPOLLogOff,
       "hh3cWIPSDevStatTxMalformed": hh3cWIPSDevStatTxMalformed,
       "hh3cWIPSDevStatRxTotalPkt": hh3cWIPSDevStatRxTotalPkt,
       "hh3cWIPSDevStatRxTotalByte": hh3cWIPSDevStatRxTotalByte,
       "hh3cWIPSDevStatRxUnicastPkt": hh3cWIPSDevStatRxUnicastPkt,
       "hh3cWIPSDevStatRxUnicastByte": hh3cWIPSDevStatRxUnicastByte,
       "hh3cWIPSDevStatRxMgmt": hh3cWIPSDevStatRxMgmt,
       "hh3cWIPSDevStatRxCtrl": hh3cWIPSDevStatRxCtrl,
       "hh3cWIPSDevStatRxData": hh3cWIPSDevStatRxData,
       "hh3cWIPSDevStatRxRTS": hh3cWIPSDevStatRxRTS,
       "hh3cWIPSDevStatRxCTS": hh3cWIPSDevStatRxCTS,
       "hh3cWIPSDevStatRxProbeRequest": hh3cWIPSDevStatRxProbeRequest,
       "hh3cWIPSDevStatRxProbeResponse": hh3cWIPSDevStatRxProbeResponse,
       "hh3cWIPSDevStatRxFragment": hh3cWIPSDevStatRxFragment,
       "hh3cWIPSDevStatRxRetry": hh3cWIPSDevStatRxRetry,
       "hh3cWIPSDevStatRxAssoRequest": hh3cWIPSDevStatRxAssoRequest,
       "hh3cWIPSDevStatRxAssoResponse": hh3cWIPSDevStatRxAssoResponse,
       "hh3cWIPSDevStatRxDisassoc": hh3cWIPSDevStatRxDisassoc,
       "hh3cWIPSDevStatRxAuth": hh3cWIPSDevStatRxAuth,
       "hh3cWIPSDevStatRxDeauth": hh3cWIPSDevStatRxDeauth,
       "hh3cWIPSDevStatRxEAPSuccess": hh3cWIPSDevStatRxEAPSuccess,
       "hh3cWIPSDevStatRxEAPFailure": hh3cWIPSDevStatRxEAPFailure,
       "hh3cWIPSDevStatRxEAPOLStart": hh3cWIPSDevStatRxEAPOLStart,
       "hh3cWIPSDevStatRxEAPOLLogoff": hh3cWIPSDevStatRxEAPOLLogoff,
       "hh3cWIPSDevStatRxMalformed": hh3cWIPSDevStatRxMalformed,
       "hh3cWIPSCtmDeviceTable": hh3cWIPSCtmDeviceTable,
       "hh3cWIPSCtmDeviceEntry": hh3cWIPSCtmDeviceEntry,
       "hh3cWIPSCtmDeviceVSD": hh3cWIPSCtmDeviceVSD,
       "hh3cWIPSCtmDeviceMAC": hh3cWIPSCtmDeviceMAC,
       "hh3cWIPSCtmDeviceType": hh3cWIPSCtmDeviceType,
       "hh3cWIPSCtmDeviceState": hh3cWIPSCtmDeviceState,
       "hh3cWIPSCtmDeviceStartTime": hh3cWIPSCtmDeviceStartTime,
       "hh3cWIPSCtmDeviceCategory": hh3cWIPSCtmDeviceCategory,
       "hh3cWIPSCtmDeviceChl": hh3cWIPSCtmDeviceChl,
       "hh3cWIPSCtmDevicePrecedence": hh3cWIPSCtmDevicePrecedence,
       "hh3cWIPSMalPktStatTable": hh3cWIPSMalPktStatTable,
       "hh3cWIPSMalPktStatEntry": hh3cWIPSMalPktStatEntry,
       "hh3cWIPSMalPktStatSensorName": hh3cWIPSMalPktStatSensorName,
       "hh3cWIPSMalPktStatInvalidIELength": hh3cWIPSMalPktStatInvalidIELength,
       "hh3cWIPSMalPktStatDuplicatedIE": hh3cWIPSMalPktStatDuplicatedIE,
       "hh3cWIPSMalPktStatRedundantIE": hh3cWIPSMalPktStatRedundantIE,
       "hh3cWIPSMalPktStatInvalidPktLength": hh3cWIPSMalPktStatInvalidPktLength,
       "hh3cWIPSMalPktStatIllegalIBSSESS": hh3cWIPSMalPktStatIllegalIBSSESS,
       "hh3cWIPSMalPktStatInvalidSourceAddr": hh3cWIPSMalPktStatInvalidSourceAddr,
       "hh3cWIPSMalPktStatOverflowEAPOLKey": hh3cWIPSMalPktStatOverflowEAPOLKey,
       "hh3cWIPSMalPktStatMalAuth": hh3cWIPSMalPktStatMalAuth,
       "hh3cWIPSMalPktStatMalAssoReq": hh3cWIPSMalPktStatMalAssoReq,
       "hh3cWIPSMalPktStatMalHTIE": hh3cWIPSMalPktStatMalHTIE,
       "hh3cWIPSMalPktStatLargeDuration": hh3cWIPSMalPktStatLargeDuration,
       "hh3cWIPSMalPktStatNULLProbeRes": hh3cWIPSMalPktStatNULLProbeRes,
       "hh3cWIPSMalPktStatInvalidDeAuthCode": hh3cWIPSMalPktStatInvalidDeAuthCode,
       "hh3cWIPSMalPktStatInvalidDisAssoCode": hh3cWIPSMalPktStatInvalidDisAssoCode,
       "hh3cWIPSMalPktStatOverflowSSID": hh3cWIPSMalPktStatOverflowSSID,
       "hh3cWIPSMalPktStatFatajack": hh3cWIPSMalPktStatFatajack,
       "hh3cWIPSMalPktStatInvalidChannel": hh3cWIPSMalPktStatInvalidChannel,
       "hh3cWIPSDctUnassocStaTable": hh3cWIPSDctUnassocStaTable,
       "hh3cWIPSDctUnassocStaEntry": hh3cWIPSDctUnassocStaEntry,
       "hh3cWIPSDctUnassocStaVSD": hh3cWIPSDctUnassocStaVSD,
       "hh3cWIPSDctUnassocStaMac": hh3cWIPSDctUnassocStaMac,
       "hh3cWIPSDctUnassocStaCategory": hh3cWIPSDctUnassocStaCategory,
       "hh3cWIPSDctUnassocStaRadioType": hh3cWIPSDctUnassocStaRadioType,
       "hh3cWIPSDctUnassocStaIsCountered": hh3cWIPSDctUnassocStaIsCountered,
       "hh3cWIPSDctUnassocStaAdd2BlackList": hh3cWIPSDctUnassocStaAdd2BlackList,
       "hh3cWIPSDctUnassocStaAdd2WhiteList": hh3cWIPSDctUnassocStaAdd2WhiteList,
       "hh3cWIPSDctUnassocStaAdd2IgnoreList": hh3cWIPSDctUnassocStaAdd2IgnoreList,
       "hh3cWIPSDctUnassocStaAdd2CtmList": hh3cWIPSDctUnassocStaAdd2CtmList,
       "hh3cWIPSDctUnassocStaFirstDctTm": hh3cWIPSDctUnassocStaFirstDctTm,
       "hh3cWIPSDctUnassocStaLastDctTm": hh3cWIPSDctUnassocStaLastDctTm,
       "hh3cWIPSDctUnassocStaRptSensorNum": hh3cWIPSDctUnassocStaRptSensorNum,
       "hh3cWIPSDctUnassocStaState": hh3cWIPSDctUnassocStaState,
       "hh3cWIPSDctUnassocStaVendor": hh3cWIPSDctUnassocStaVendor,
       "hh3cWIPSDctUnassocStaRptSensorTable": hh3cWIPSDctUnassocStaRptSensorTable,
       "hh3cWIPSDctUnassocStaRptSensorEntry": hh3cWIPSDctUnassocStaRptSensorEntry,
       "hh3cWIPSDctUnassocStaRtpSensorName": hh3cWIPSDctUnassocStaRtpSensorName,
       "hh3cWIPSDctUnassocStaRptSensorRadioId": hh3cWIPSDctUnassocStaRptSensorRadioId,
       "hh3cWIPSDctUnassocStaRptRSSI": hh3cWIPSDctUnassocStaRptRSSI,
       "hh3cWIPSDctUnassocStaLastRptTm": hh3cWIPSDctUnassocStaLastRptTm,
       "hh3cWIPSNotifyGroup": hh3cWIPSNotifyGroup}
)
