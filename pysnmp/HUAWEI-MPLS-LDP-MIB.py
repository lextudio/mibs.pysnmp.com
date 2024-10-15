# SNMP MIB module (HUAWEI-MPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MPLS-LDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:07 2024
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

(huaweiMgmt,
 hwMpls) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "huaweiMgmt",
    "hwMpls")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

hwMplsLdp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2)
)
hwMplsLdp.setRevisions(
        ("1996-11-08 21:55",)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class BitRate(Integer32):
    """Custom type BitRate based on Integer32"""




class BurstSize(Integer32):
    """Custom type BurstSize based on Integer32"""



# TEXTUAL-CONVENTIONS



class MplsLsrIdentifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class MplsLdpGenAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class MplsLdpIdentifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class AtmVpIdentifier(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class AtmVcIdentifier(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class AddressFamilyNumbers(Integer32, TextualConvention):
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 12),
          ("banyanVines", 14),
          ("bbn1822", 5),
          ("decnetIV", 13),
          ("e163", 7),
          ("e164", 8),
          ("e164WithNsap", 15),
          ("f69", 9),
          ("hdlc", 4),
          ("ieee802", 6),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipx", 11),
          ("nsap", 3),
          ("other", 0),
          ("x121", 10))
    )



class MplsLabel(Integer32, TextualConvention):
    status = "current"


class MplsTunnelIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_HwMplsLdpObjects_ObjectIdentity = ObjectIdentity
hwMplsLdpObjects = _HwMplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1)
)
_HwMplsLdpLsrObjects_ObjectIdentity = ObjectIdentity
hwMplsLdpLsrObjects = _HwMplsLdpLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1)
)
_HwMplsLdpLsrIncarnTable_Object = MibTable
hwMplsLdpLsrIncarnTable = _HwMplsLdpLsrIncarnTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwMplsLdpLsrIncarnTable.setStatus("current")
_HwMplsLdpLsrIncarnEntry_Object = MibTableRow
hwMplsLdpLsrIncarnEntry = _HwMplsLdpLsrIncarnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1)
)
hwMplsLdpLsrIncarnEntry.setIndexNames(
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
)
if mibBuilder.loadTexts:
    hwMplsLdpLsrIncarnEntry.setStatus("current")
_HwMplsLdpLsrID_Type = MplsLsrIdentifier
_HwMplsLdpLsrID_Object = MibTableColumn
hwMplsLdpLsrID = _HwMplsLdpLsrID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 1),
    _HwMplsLdpLsrID_Type()
)
hwMplsLdpLsrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrID.setStatus("current")


class _HwMplsLdpLsrLoopDetectionPresent_Type(TruthValue):
    """Custom type hwMplsLdpLsrLoopDetectionPresent based on TruthValue"""


_HwMplsLdpLsrLoopDetectionPresent_Object = MibTableColumn
hwMplsLdpLsrLoopDetectionPresent = _HwMplsLdpLsrLoopDetectionPresent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 2),
    _HwMplsLdpLsrLoopDetectionPresent_Type()
)
hwMplsLdpLsrLoopDetectionPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpLsrLoopDetectionPresent.setStatus("current")


class _HwMplsLdpLsrLoopDetectionAdminStatus_Type(Integer32):
    """Custom type hwMplsLdpLsrLoopDetectionAdminStatus based on Integer32"""
    defaultValue = 1

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


_HwMplsLdpLsrLoopDetectionAdminStatus_Type.__name__ = "Integer32"
_HwMplsLdpLsrLoopDetectionAdminStatus_Object = MibTableColumn
hwMplsLdpLsrLoopDetectionAdminStatus = _HwMplsLdpLsrLoopDetectionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 3),
    _HwMplsLdpLsrLoopDetectionAdminStatus_Type()
)
hwMplsLdpLsrLoopDetectionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrLoopDetectionAdminStatus.setStatus("current")


class _HwMplsLdpLsrPathVectorLimit_Type(Integer32):
    """Custom type hwMplsLdpLsrPathVectorLimit based on Integer32"""
    defaultValue = 32


_HwMplsLdpLsrPathVectorLimit_Object = MibTableColumn
hwMplsLdpLsrPathVectorLimit = _HwMplsLdpLsrPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 4),
    _HwMplsLdpLsrPathVectorLimit_Type()
)
hwMplsLdpLsrPathVectorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrPathVectorLimit.setStatus("current")


class _HwMplsLdpLsrHopCountLimit_Type(Integer32):
    """Custom type hwMplsLdpLsrHopCountLimit based on Integer32"""
    defaultValue = 32


_HwMplsLdpLsrHopCountLimit_Object = MibTableColumn
hwMplsLdpLsrHopCountLimit = _HwMplsLdpLsrHopCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 5),
    _HwMplsLdpLsrHopCountLimit_Type()
)
hwMplsLdpLsrHopCountLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrHopCountLimit.setStatus("current")


class _HwMplsLdpLsrLoopPreventionPresent_Type(TruthValue):
    """Custom type hwMplsLdpLsrLoopPreventionPresent based on TruthValue"""


_HwMplsLdpLsrLoopPreventionPresent_Object = MibTableColumn
hwMplsLdpLsrLoopPreventionPresent = _HwMplsLdpLsrLoopPreventionPresent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 6),
    _HwMplsLdpLsrLoopPreventionPresent_Type()
)
hwMplsLdpLsrLoopPreventionPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpLsrLoopPreventionPresent.setStatus("current")


class _HwMplsLdpLsrLoopPreventionAdminStatus_Type(Integer32):
    """Custom type hwMplsLdpLsrLoopPreventionAdminStatus based on Integer32"""
    defaultValue = 2

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


_HwMplsLdpLsrLoopPreventionAdminStatus_Type.__name__ = "Integer32"
_HwMplsLdpLsrLoopPreventionAdminStatus_Object = MibTableColumn
hwMplsLdpLsrLoopPreventionAdminStatus = _HwMplsLdpLsrLoopPreventionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 7),
    _HwMplsLdpLsrLoopPreventionAdminStatus_Type()
)
hwMplsLdpLsrLoopPreventionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrLoopPreventionAdminStatus.setStatus("current")


class _HwMplsLdpLsrLabelRetentionMode_Type(Integer32):
    """Custom type hwMplsLdpLsrLabelRetentionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conservative", 1),
          ("liberal", 2))
    )


_HwMplsLdpLsrLabelRetentionMode_Type.__name__ = "Integer32"
_HwMplsLdpLsrLabelRetentionMode_Object = MibTableColumn
hwMplsLdpLsrLabelRetentionMode = _HwMplsLdpLsrLabelRetentionMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 8),
    _HwMplsLdpLsrLabelRetentionMode_Type()
)
hwMplsLdpLsrLabelRetentionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrLabelRetentionMode.setStatus("current")
_HwMplsLdpLsrIncarnID_Type = Integer32
_HwMplsLdpLsrIncarnID_Object = MibTableColumn
hwMplsLdpLsrIncarnID = _HwMplsLdpLsrIncarnID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 9),
    _HwMplsLdpLsrIncarnID_Type()
)
hwMplsLdpLsrIncarnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpLsrIncarnID.setStatus("current")


class _HwMplsLdpLsrMaxLdpEntities_Type(Integer32):
    """Custom type hwMplsLdpLsrMaxLdpEntities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwMplsLdpLsrMaxLdpEntities_Type.__name__ = "Integer32"
_HwMplsLdpLsrMaxLdpEntities_Object = MibTableColumn
hwMplsLdpLsrMaxLdpEntities = _HwMplsLdpLsrMaxLdpEntities_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 10),
    _HwMplsLdpLsrMaxLdpEntities_Type()
)
hwMplsLdpLsrMaxLdpEntities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrMaxLdpEntities.setStatus("current")


class _HwMplsLdpLsrMaxLocalPeers_Type(Integer32):
    """Custom type hwMplsLdpLsrMaxLocalPeers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwMplsLdpLsrMaxLocalPeers_Type.__name__ = "Integer32"
_HwMplsLdpLsrMaxLocalPeers_Object = MibTableColumn
hwMplsLdpLsrMaxLocalPeers = _HwMplsLdpLsrMaxLocalPeers_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 11),
    _HwMplsLdpLsrMaxLocalPeers_Type()
)
hwMplsLdpLsrMaxLocalPeers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrMaxLocalPeers.setStatus("current")


class _HwMplsLdpLsrMaxRemotePeers_Type(Integer32):
    """Custom type hwMplsLdpLsrMaxRemotePeers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwMplsLdpLsrMaxRemotePeers_Type.__name__ = "Integer32"
_HwMplsLdpLsrMaxRemotePeers_Object = MibTableColumn
hwMplsLdpLsrMaxRemotePeers = _HwMplsLdpLsrMaxRemotePeers_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 12),
    _HwMplsLdpLsrMaxRemotePeers_Type()
)
hwMplsLdpLsrMaxRemotePeers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrMaxRemotePeers.setStatus("current")
_HwMplsLdpLsrMaxIfaces_Type = Integer32
_HwMplsLdpLsrMaxIfaces_Object = MibTableColumn
hwMplsLdpLsrMaxIfaces = _HwMplsLdpLsrMaxIfaces_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 13),
    _HwMplsLdpLsrMaxIfaces_Type()
)
hwMplsLdpLsrMaxIfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrMaxIfaces.setStatus("current")
_HwMplsLdpLsrMaxLsps_Type = Integer32
_HwMplsLdpLsrMaxLsps_Object = MibTableColumn
hwMplsLdpLsrMaxLsps = _HwMplsLdpLsrMaxLsps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 14),
    _HwMplsLdpLsrMaxLsps_Type()
)
hwMplsLdpLsrMaxLsps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrMaxLsps.setStatus("current")
_HwMplsLdpLsrMaxCrlspTnls_Type = Integer32
_HwMplsLdpLsrMaxCrlspTnls_Object = MibTableColumn
hwMplsLdpLsrMaxCrlspTnls = _HwMplsLdpLsrMaxCrlspTnls_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 15),
    _HwMplsLdpLsrMaxCrlspTnls_Type()
)
hwMplsLdpLsrMaxCrlspTnls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrMaxCrlspTnls.setStatus("current")
_HwMplsLdpLsrMaxErhopPerCrlspTnl_Type = Integer32
_HwMplsLdpLsrMaxErhopPerCrlspTnl_Object = MibTableColumn
hwMplsLdpLsrMaxErhopPerCrlspTnl = _HwMplsLdpLsrMaxErhopPerCrlspTnl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 16),
    _HwMplsLdpLsrMaxErhopPerCrlspTnl_Type()
)
hwMplsLdpLsrMaxErhopPerCrlspTnl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrMaxErhopPerCrlspTnl.setStatus("current")
_HwMplsLdpLsrRowStatus_Type = RowStatus
_HwMplsLdpLsrRowStatus_Object = MibTableColumn
hwMplsLdpLsrRowStatus = _HwMplsLdpLsrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 17),
    _HwMplsLdpLsrRowStatus_Type()
)
hwMplsLdpLsrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpLsrRowStatus.setStatus("current")
_HwMplsLdpLsrMaxVcmCapability_Type = Integer32
_HwMplsLdpLsrMaxVcmCapability_Object = MibTableColumn
hwMplsLdpLsrMaxVcmCapability = _HwMplsLdpLsrMaxVcmCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 18),
    _HwMplsLdpLsrMaxVcmCapability_Type()
)
hwMplsLdpLsrMaxVcmCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrMaxVcmCapability.setStatus("current")
_HwMplsLdpLsrVcmPathVecInAllLblMapPresent_Type = TruthValue
_HwMplsLdpLsrVcmPathVecInAllLblMapPresent_Object = MibTableColumn
hwMplsLdpLsrVcmPathVecInAllLblMapPresent = _HwMplsLdpLsrVcmPathVecInAllLblMapPresent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 19),
    _HwMplsLdpLsrVcmPathVecInAllLblMapPresent_Type()
)
hwMplsLdpLsrVcmPathVecInAllLblMapPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrVcmPathVecInAllLblMapPresent.setStatus("current")
_HwMplsLdpLsrRequestRetrytimerValue_Type = Integer32
_HwMplsLdpLsrRequestRetrytimerValue_Object = MibTableColumn
hwMplsLdpLsrRequestRetrytimerValue = _HwMplsLdpLsrRequestRetrytimerValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 20),
    _HwMplsLdpLsrRequestRetrytimerValue_Type()
)
hwMplsLdpLsrRequestRetrytimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrRequestRetrytimerValue.setStatus("current")
_HwMplsLdpLsrNumOfRequestRetryAttempts_Type = Integer32
_HwMplsLdpLsrNumOfRequestRetryAttempts_Object = MibTableColumn
hwMplsLdpLsrNumOfRequestRetryAttempts = _HwMplsLdpLsrNumOfRequestRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 1, 1, 1, 21),
    _HwMplsLdpLsrNumOfRequestRetryAttempts_Type()
)
hwMplsLdpLsrNumOfRequestRetryAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLdpLsrNumOfRequestRetryAttempts.setStatus("current")
_HwMplsLdpEntityObjects_ObjectIdentity = ObjectIdentity
hwMplsLdpEntityObjects = _HwMplsLdpEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2)
)
_HwMplsLdpEntityTable_Object = MibTable
hwMplsLdpEntityTable = _HwMplsLdpEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwMplsLdpEntityTable.setStatus("current")
_HwMplsLdpEntityEntry_Object = MibTableRow
hwMplsLdpEntityEntry = _HwMplsLdpEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1)
)
hwMplsLdpEntityEntry.setIndexNames(
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityIfIndex"),
)
if mibBuilder.loadTexts:
    hwMplsLdpEntityEntry.setStatus("current")
_HwMplsLdpEntityID_Type = MplsLdpIdentifier
_HwMplsLdpEntityID_Object = MibTableColumn
hwMplsLdpEntityID = _HwMplsLdpEntityID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 1),
    _HwMplsLdpEntityID_Type()
)
hwMplsLdpEntityID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLdpEntityID.setStatus("current")


class _HwMplsLdpEntityLabelSpaceType_Type(Integer32):
    """Custom type hwMplsLdpEntityLabelSpaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("perInterface", 2),
          ("perPlatform", 3),
          ("unknown", 1))
    )


_HwMplsLdpEntityLabelSpaceType_Type.__name__ = "Integer32"
_HwMplsLdpEntityLabelSpaceType_Object = MibTableColumn
hwMplsLdpEntityLabelSpaceType = _HwMplsLdpEntityLabelSpaceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 2),
    _HwMplsLdpEntityLabelSpaceType_Type()
)
hwMplsLdpEntityLabelSpaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityLabelSpaceType.setStatus("current")
_HwMplsLdpEntityDefVpi_Type = AtmVpIdentifier
_HwMplsLdpEntityDefVpi_Object = MibTableColumn
hwMplsLdpEntityDefVpi = _HwMplsLdpEntityDefVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 3),
    _HwMplsLdpEntityDefVpi_Type()
)
hwMplsLdpEntityDefVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityDefVpi.setStatus("current")
_HwMplsLdpEntityDefVci_Type = AtmVcIdentifier
_HwMplsLdpEntityDefVci_Object = MibTableColumn
hwMplsLdpEntityDefVci = _HwMplsLdpEntityDefVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 4),
    _HwMplsLdpEntityDefVci_Type()
)
hwMplsLdpEntityDefVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityDefVci.setStatus("current")


class _HwMplsLdpEntityUnlabTrafVpi_Type(AtmVpIdentifier):
    """Custom type hwMplsLdpEntityUnlabTrafVpi based on AtmVpIdentifier"""
    defaultValue = 0


_HwMplsLdpEntityUnlabTrafVpi_Object = MibTableColumn
hwMplsLdpEntityUnlabTrafVpi = _HwMplsLdpEntityUnlabTrafVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 5),
    _HwMplsLdpEntityUnlabTrafVpi_Type()
)
hwMplsLdpEntityUnlabTrafVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityUnlabTrafVpi.setStatus("current")


class _HwMplsLdpEntityUnlabTrafVci_Type(AtmVcIdentifier):
    """Custom type hwMplsLdpEntityUnlabTrafVci based on AtmVcIdentifier"""
    defaultValue = 32


_HwMplsLdpEntityUnlabTrafVci_Object = MibTableColumn
hwMplsLdpEntityUnlabTrafVci = _HwMplsLdpEntityUnlabTrafVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 6),
    _HwMplsLdpEntityUnlabTrafVci_Type()
)
hwMplsLdpEntityUnlabTrafVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityUnlabTrafVci.setStatus("current")


class _HwMplsLdpEntityMergeCapability_Type(Integer32):
    """Custom type hwMplsLdpEntityMergeCapability based on Integer32"""
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
        *(("noMerge", 0),
          ("vcMerge", 2),
          ("vpMerge", 1),
          ("vpVcMerge", 3))
    )


_HwMplsLdpEntityMergeCapability_Type.__name__ = "Integer32"
_HwMplsLdpEntityMergeCapability_Object = MibTableColumn
hwMplsLdpEntityMergeCapability = _HwMplsLdpEntityMergeCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 7),
    _HwMplsLdpEntityMergeCapability_Type()
)
hwMplsLdpEntityMergeCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityMergeCapability.setStatus("current")


class _HwMplsLdpEntityVcDirectionality_Type(Integer32):
    """Custom type hwMplsLdpEntityVcDirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("unidirectional", 2))
    )


_HwMplsLdpEntityVcDirectionality_Type.__name__ = "Integer32"
_HwMplsLdpEntityVcDirectionality_Object = MibTableColumn
hwMplsLdpEntityVcDirectionality = _HwMplsLdpEntityVcDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 8),
    _HwMplsLdpEntityVcDirectionality_Type()
)
hwMplsLdpEntityVcDirectionality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityVcDirectionality.setStatus("current")
_HwMplsLdpEntityWellKnownDiscoveryPort_Type = Integer32
_HwMplsLdpEntityWellKnownDiscoveryPort_Object = MibTableColumn
hwMplsLdpEntityWellKnownDiscoveryPort = _HwMplsLdpEntityWellKnownDiscoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 9),
    _HwMplsLdpEntityWellKnownDiscoveryPort_Type()
)
hwMplsLdpEntityWellKnownDiscoveryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityWellKnownDiscoveryPort.setStatus("current")


class _HwMplsLdpEntityMtu_Type(Integer32):
    """Custom type hwMplsLdpEntityMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMplsLdpEntityMtu_Type.__name__ = "Integer32"
_HwMplsLdpEntityMtu_Object = MibTableColumn
hwMplsLdpEntityMtu = _HwMplsLdpEntityMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 10),
    _HwMplsLdpEntityMtu_Type()
)
hwMplsLdpEntityMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityMtu.setStatus("current")


class _HwMplsLdpEntityKeepAliveHoldTimer_Type(Integer32):
    """Custom type hwMplsLdpEntityKeepAliveHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMplsLdpEntityKeepAliveHoldTimer_Type.__name__ = "Integer32"
_HwMplsLdpEntityKeepAliveHoldTimer_Object = MibTableColumn
hwMplsLdpEntityKeepAliveHoldTimer = _HwMplsLdpEntityKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 11),
    _HwMplsLdpEntityKeepAliveHoldTimer_Type()
)
hwMplsLdpEntityKeepAliveHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityKeepAliveHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsLdpEntityKeepAliveHoldTimer.setUnits("seconds")
_HwMplsLdpEntityFailedInitSessionThreshold_Type = Integer32
_HwMplsLdpEntityFailedInitSessionThreshold_Object = MibTableColumn
hwMplsLdpEntityFailedInitSessionThreshold = _HwMplsLdpEntityFailedInitSessionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 12),
    _HwMplsLdpEntityFailedInitSessionThreshold_Type()
)
hwMplsLdpEntityFailedInitSessionThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityFailedInitSessionThreshold.setStatus("current")


class _HwMplsLdpEntityLabelDistributionMethod_Type(Integer32):
    """Custom type hwMplsLdpEntityLabelDistributionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstreamOnDemand", 1),
          ("downstreamUnsolicited", 2))
    )


_HwMplsLdpEntityLabelDistributionMethod_Type.__name__ = "Integer32"
_HwMplsLdpEntityLabelDistributionMethod_Object = MibTableColumn
hwMplsLdpEntityLabelDistributionMethod = _HwMplsLdpEntityLabelDistributionMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 13),
    _HwMplsLdpEntityLabelDistributionMethod_Type()
)
hwMplsLdpEntityLabelDistributionMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityLabelDistributionMethod.setStatus("current")


class _HwMplsLdpEntityLabelAllocationMethod_Type(Integer32):
    """Custom type hwMplsLdpEntityLabelAllocationMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 2),
          ("ordered", 1))
    )


_HwMplsLdpEntityLabelAllocationMethod_Type.__name__ = "Integer32"
_HwMplsLdpEntityLabelAllocationMethod_Object = MibTableColumn
hwMplsLdpEntityLabelAllocationMethod = _HwMplsLdpEntityLabelAllocationMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 14),
    _HwMplsLdpEntityLabelAllocationMethod_Type()
)
hwMplsLdpEntityLabelAllocationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityLabelAllocationMethod.setStatus("current")


class _HwMplsLdpEntityHelloHoldTimer_Type(Integer32):
    """Custom type hwMplsLdpEntityHelloHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMplsLdpEntityHelloHoldTimer_Type.__name__ = "Integer32"
_HwMplsLdpEntityHelloHoldTimer_Object = MibTableColumn
hwMplsLdpEntityHelloHoldTimer = _HwMplsLdpEntityHelloHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 15),
    _HwMplsLdpEntityHelloHoldTimer_Type()
)
hwMplsLdpEntityHelloHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityHelloHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsLdpEntityHelloHoldTimer.setUnits("seconds")
_HwMplsLdpEntityRowStatus_Type = RowStatus
_HwMplsLdpEntityRowStatus_Object = MibTableColumn
hwMplsLdpEntityRowStatus = _HwMplsLdpEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 1, 1, 16),
    _HwMplsLdpEntityRowStatus_Type()
)
hwMplsLdpEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityRowStatus.setStatus("current")
_HwMplsLdpEntityIfTable_Object = MibTable
hwMplsLdpEntityIfTable = _HwMplsLdpEntityIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwMplsLdpEntityIfTable.setStatus("current")
_HwMplsLdpEntityIfEntry_Object = MibTableRow
hwMplsLdpEntityIfEntry = _HwMplsLdpEntityIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 2, 1)
)
hwMplsLdpEntityIfEntry.setIndexNames(
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityIfIndex"),
)
if mibBuilder.loadTexts:
    hwMplsLdpEntityIfEntry.setStatus("current")


class _HwMplsLdpEntityIfIndex_Type(Unsigned32):
    """Custom type hwMplsLdpEntityIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwMplsLdpEntityIfIndex_Type.__name__ = "Unsigned32"
_HwMplsLdpEntityIfIndex_Object = MibTableColumn
hwMplsLdpEntityIfIndex = _HwMplsLdpEntityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 2, 1, 1),
    _HwMplsLdpEntityIfIndex_Type()
)
hwMplsLdpEntityIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsLdpEntityIfIndex.setStatus("current")
_HwMplsLdpEntityIfIpv4Address_Type = IpAddress
_HwMplsLdpEntityIfIpv4Address_Object = MibTableColumn
hwMplsLdpEntityIfIpv4Address = _HwMplsLdpEntityIfIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 2, 1, 2),
    _HwMplsLdpEntityIfIpv4Address_Type()
)
hwMplsLdpEntityIfIpv4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityIfIpv4Address.setStatus("current")
_HwMplsLdpEntityIfRowStatus_Type = RowStatus
_HwMplsLdpEntityIfRowStatus_Object = MibTableColumn
hwMplsLdpEntityIfRowStatus = _HwMplsLdpEntityIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 2, 1, 3),
    _HwMplsLdpEntityIfRowStatus_Type()
)
hwMplsLdpEntityIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityIfRowStatus.setStatus("current")
_HwMplsLdpEntityConfAtmLabelRangeTable_Object = MibTable
hwMplsLdpEntityConfAtmLabelRangeTable = _HwMplsLdpEntityConfAtmLabelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwMplsLdpEntityConfAtmLabelRangeTable.setStatus("current")
_HwMplsLdpEntityConfAtmLabelRangeEntry_Object = MibTableRow
hwMplsLdpEntityConfAtmLabelRangeEntry = _HwMplsLdpEntityConfAtmLabelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 3, 1)
)
hwMplsLdpEntityConfAtmLabelRangeEntry.setIndexNames(
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityIfIndex"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI"),
)
if mibBuilder.loadTexts:
    hwMplsLdpEntityConfAtmLabelRangeEntry.setStatus("current")
_HwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Type = AtmVpIdentifier
_HwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Object = MibTableColumn
hwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI = _HwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 3, 1, 1),
    _HwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Type()
)
hwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI.setStatus("current")
_HwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Type = AtmVcIdentifier
_HwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Object = MibTableColumn
hwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI = _HwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 3, 1, 2),
    _HwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Type()
)
hwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI.setStatus("current")
_HwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Type = AtmVpIdentifier
_HwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Object = MibTableColumn
hwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI = _HwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 3, 1, 3),
    _HwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Type()
)
hwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI.setStatus("current")
_HwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Type = AtmVcIdentifier
_HwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Object = MibTableColumn
hwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI = _HwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 3, 1, 4),
    _HwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Type()
)
hwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI.setStatus("current")
_HwMplsLdpEntityConfAtmLabelRangeRowStatus_Type = RowStatus
_HwMplsLdpEntityConfAtmLabelRangeRowStatus_Object = MibTableColumn
hwMplsLdpEntityConfAtmLabelRangeRowStatus = _HwMplsLdpEntityConfAtmLabelRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 3, 1, 5),
    _HwMplsLdpEntityConfAtmLabelRangeRowStatus_Type()
)
hwMplsLdpEntityConfAtmLabelRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpEntityConfAtmLabelRangeRowStatus.setStatus("current")
_HwMplsLdpEntityStatsTable_Object = MibTable
hwMplsLdpEntityStatsTable = _HwMplsLdpEntityStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hwMplsLdpEntityStatsTable.setStatus("current")
_HwMplsLdpEntityStatsEntry_Object = MibTableRow
hwMplsLdpEntityStatsEntry = _HwMplsLdpEntityStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    hwMplsLdpEntityStatsEntry.setStatus("current")
_HwMplsLdpAttemptedSessions_Type = Counter32
_HwMplsLdpAttemptedSessions_Object = MibTableColumn
hwMplsLdpAttemptedSessions = _HwMplsLdpAttemptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 2, 4, 1, 1),
    _HwMplsLdpAttemptedSessions_Type()
)
hwMplsLdpAttemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpAttemptedSessions.setStatus("current")
_HwMplsLdpPeerObjects_ObjectIdentity = ObjectIdentity
hwMplsLdpPeerObjects = _HwMplsLdpPeerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3)
)
_HwMplsLdpPeerTable_Object = MibTable
hwMplsLdpPeerTable = _HwMplsLdpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwMplsLdpPeerTable.setStatus("current")
_HwMplsLdpPeerEntry_Object = MibTableRow
hwMplsLdpPeerEntry = _HwMplsLdpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 1, 1)
)
hwMplsLdpPeerEntry.setIndexNames(
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityIfIndex"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpPeerIndex"),
)
if mibBuilder.loadTexts:
    hwMplsLdpPeerEntry.setStatus("current")


class _HwMplsLdpPeerIndex_Type(Unsigned32):
    """Custom type hwMplsLdpPeerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwMplsLdpPeerIndex_Type.__name__ = "Unsigned32"
_HwMplsLdpPeerIndex_Object = MibTableColumn
hwMplsLdpPeerIndex = _HwMplsLdpPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 1, 1, 1),
    _HwMplsLdpPeerIndex_Type()
)
hwMplsLdpPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsLdpPeerIndex.setStatus("current")
_HwMplsLdpPeerID_Type = MplsLdpIdentifier
_HwMplsLdpPeerID_Object = MibTableColumn
hwMplsLdpPeerID = _HwMplsLdpPeerID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 1, 1, 2),
    _HwMplsLdpPeerID_Type()
)
hwMplsLdpPeerID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpPeerID.setStatus("current")
_HwMplsLdpPeerInternetworkAddrType_Type = AddressFamilyNumbers
_HwMplsLdpPeerInternetworkAddrType_Object = MibTableColumn
hwMplsLdpPeerInternetworkAddrType = _HwMplsLdpPeerInternetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 1, 1, 3),
    _HwMplsLdpPeerInternetworkAddrType_Type()
)
hwMplsLdpPeerInternetworkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpPeerInternetworkAddrType.setStatus("current")
_HwMplsLdpPeerInternetworkAddr_Type = MplsLdpGenAddr
_HwMplsLdpPeerInternetworkAddr_Object = MibTableColumn
hwMplsLdpPeerInternetworkAddr = _HwMplsLdpPeerInternetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 1, 1, 4),
    _HwMplsLdpPeerInternetworkAddr_Type()
)
hwMplsLdpPeerInternetworkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpPeerInternetworkAddr.setStatus("current")


class _HwMplsLdpPeerDefaultMtu_Type(Integer32):
    """Custom type hwMplsLdpPeerDefaultMtu based on Integer32"""
    defaultValue = 9180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMplsLdpPeerDefaultMtu_Type.__name__ = "Integer32"
_HwMplsLdpPeerDefaultMtu_Object = MibTableColumn
hwMplsLdpPeerDefaultMtu = _HwMplsLdpPeerDefaultMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 1, 1, 5),
    _HwMplsLdpPeerDefaultMtu_Type()
)
hwMplsLdpPeerDefaultMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpPeerDefaultMtu.setStatus("current")


class _HwMplsLdpPeerKeepAliveHoldTimer_Type(Integer32):
    """Custom type hwMplsLdpPeerKeepAliveHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMplsLdpPeerKeepAliveHoldTimer_Type.__name__ = "Integer32"
_HwMplsLdpPeerKeepAliveHoldTimer_Object = MibTableColumn
hwMplsLdpPeerKeepAliveHoldTimer = _HwMplsLdpPeerKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 1, 1, 6),
    _HwMplsLdpPeerKeepAliveHoldTimer_Type()
)
hwMplsLdpPeerKeepAliveHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpPeerKeepAliveHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsLdpPeerKeepAliveHoldTimer.setUnits("seconds")


class _HwMplsLdpPeerLabelDistributionMethod_Type(Integer32):
    """Custom type hwMplsLdpPeerLabelDistributionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstreamOnDemand", 1),
          ("downstreamUnsolicited", 2))
    )


_HwMplsLdpPeerLabelDistributionMethod_Type.__name__ = "Integer32"
_HwMplsLdpPeerLabelDistributionMethod_Object = MibTableColumn
hwMplsLdpPeerLabelDistributionMethod = _HwMplsLdpPeerLabelDistributionMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 1, 1, 7),
    _HwMplsLdpPeerLabelDistributionMethod_Type()
)
hwMplsLdpPeerLabelDistributionMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpPeerLabelDistributionMethod.setStatus("current")


class _HwMplsLdpPeerType_Type(Integer32):
    """Custom type hwMplsLdpPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_HwMplsLdpPeerType_Type.__name__ = "Integer32"
_HwMplsLdpPeerType_Object = MibTableColumn
hwMplsLdpPeerType = _HwMplsLdpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 1, 1, 8),
    _HwMplsLdpPeerType_Type()
)
hwMplsLdpPeerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpPeerType.setStatus("current")
_HwMplsLdpPeerRowStatus_Type = RowStatus
_HwMplsLdpPeerRowStatus_Object = MibTableColumn
hwMplsLdpPeerRowStatus = _HwMplsLdpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 1, 1, 9),
    _HwMplsLdpPeerRowStatus_Type()
)
hwMplsLdpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpPeerRowStatus.setStatus("current")
_HwMplsLdpPeerConfAtmLabelRangeTable_Object = MibTable
hwMplsLdpPeerConfAtmLabelRangeTable = _HwMplsLdpPeerConfAtmLabelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwMplsLdpPeerConfAtmLabelRangeTable.setStatus("current")
_HwMplsLdpPeerConfAtmLabelRangeEntry_Object = MibTableRow
hwMplsLdpPeerConfAtmLabelRangeEntry = _HwMplsLdpPeerConfAtmLabelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 2, 1)
)
hwMplsLdpPeerConfAtmLabelRangeEntry.setIndexNames(
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityIfIndex"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpPeerIndex"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI"),
)
if mibBuilder.loadTexts:
    hwMplsLdpPeerConfAtmLabelRangeEntry.setStatus("current")
_HwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Type = AtmVpIdentifier
_HwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Object = MibTableColumn
hwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI = _HwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 2, 1, 1),
    _HwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Type()
)
hwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI.setStatus("current")
_HwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Type = AtmVcIdentifier
_HwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Object = MibTableColumn
hwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI = _HwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 2, 1, 2),
    _HwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Type()
)
hwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI.setStatus("current")
_HwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Type = AtmVpIdentifier
_HwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Object = MibTableColumn
hwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI = _HwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 2, 1, 3),
    _HwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Type()
)
hwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI.setStatus("current")
_HwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Type = AtmVcIdentifier
_HwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Object = MibTableColumn
hwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI = _HwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 3, 2, 1, 4),
    _HwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Type()
)
hwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI.setStatus("current")
_HwMplsLdpSessionObjects_ObjectIdentity = ObjectIdentity
hwMplsLdpSessionObjects = _HwMplsLdpSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4)
)
_HwMplsLdpSessionTable_Object = MibTable
hwMplsLdpSessionTable = _HwMplsLdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwMplsLdpSessionTable.setStatus("current")
_HwMplsLdpSessionEntry_Object = MibTableRow
hwMplsLdpSessionEntry = _HwMplsLdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4, 1, 1)
)
hwMplsLdpSessionEntry.setIndexNames(
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityIfIndex"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpPeerIndex"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpSessionIndex"),
)
if mibBuilder.loadTexts:
    hwMplsLdpSessionEntry.setStatus("current")


class _HwMplsLdpSessionIndex_Type(Unsigned32):
    """Custom type hwMplsLdpSessionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwMplsLdpSessionIndex_Type.__name__ = "Unsigned32"
_HwMplsLdpSessionIndex_Object = MibTableColumn
hwMplsLdpSessionIndex = _HwMplsLdpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4, 1, 1, 1),
    _HwMplsLdpSessionIndex_Type()
)
hwMplsLdpSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsLdpSessionIndex.setStatus("current")
_HwMplsLdpSessionID_Type = MplsLdpIdentifier
_HwMplsLdpSessionID_Object = MibTableColumn
hwMplsLdpSessionID = _HwMplsLdpSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4, 1, 1, 2),
    _HwMplsLdpSessionID_Type()
)
hwMplsLdpSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionID.setStatus("current")


class _HwMplsLdpSessionProtocolVersion_Type(Integer32):
    """Custom type hwMplsLdpSessionProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMplsLdpSessionProtocolVersion_Type.__name__ = "Integer32"
_HwMplsLdpSessionProtocolVersion_Object = MibTableColumn
hwMplsLdpSessionProtocolVersion = _HwMplsLdpSessionProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4, 1, 1, 3),
    _HwMplsLdpSessionProtocolVersion_Type()
)
hwMplsLdpSessionProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionProtocolVersion.setStatus("current")
_HwMplsLdpSessionKeepAliveHoldTimeRemaining_Type = TimeInterval
_HwMplsLdpSessionKeepAliveHoldTimeRemaining_Object = MibTableColumn
hwMplsLdpSessionKeepAliveHoldTimeRemaining = _HwMplsLdpSessionKeepAliveHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4, 1, 1, 4),
    _HwMplsLdpSessionKeepAliveHoldTimeRemaining_Type()
)
hwMplsLdpSessionKeepAliveHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionKeepAliveHoldTimeRemaining.setStatus("current")


class _HwMplsLdpSessionRole_Type(Integer32):
    """Custom type hwMplsLdpSessionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_HwMplsLdpSessionRole_Type.__name__ = "Integer32"
_HwMplsLdpSessionRole_Object = MibTableColumn
hwMplsLdpSessionRole = _HwMplsLdpSessionRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4, 1, 1, 5),
    _HwMplsLdpSessionRole_Type()
)
hwMplsLdpSessionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionRole.setStatus("current")


class _HwMplsLdpSessionState_Type(Integer32):
    """Custom type hwMplsLdpSessionState based on Integer32"""
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
        *(("initialized", 2),
          ("nonexistent", 1),
          ("openrec", 3),
          ("opensent", 4),
          ("operational", 5))
    )


_HwMplsLdpSessionState_Type.__name__ = "Integer32"
_HwMplsLdpSessionState_Object = MibTableColumn
hwMplsLdpSessionState = _HwMplsLdpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4, 1, 1, 6),
    _HwMplsLdpSessionState_Type()
)
hwMplsLdpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionState.setStatus("current")
_HwMplsLdpSessionAtmLabelRangeLowerBoundVPI_Type = AtmVpIdentifier
_HwMplsLdpSessionAtmLabelRangeLowerBoundVPI_Object = MibTableColumn
hwMplsLdpSessionAtmLabelRangeLowerBoundVPI = _HwMplsLdpSessionAtmLabelRangeLowerBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4, 1, 1, 7),
    _HwMplsLdpSessionAtmLabelRangeLowerBoundVPI_Type()
)
hwMplsLdpSessionAtmLabelRangeLowerBoundVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionAtmLabelRangeLowerBoundVPI.setStatus("current")
_HwMplsLdpSessionAtmLabelRangeLowerBoundVCI_Type = AtmVcIdentifier
_HwMplsLdpSessionAtmLabelRangeLowerBoundVCI_Object = MibTableColumn
hwMplsLdpSessionAtmLabelRangeLowerBoundVCI = _HwMplsLdpSessionAtmLabelRangeLowerBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4, 1, 1, 8),
    _HwMplsLdpSessionAtmLabelRangeLowerBoundVCI_Type()
)
hwMplsLdpSessionAtmLabelRangeLowerBoundVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionAtmLabelRangeLowerBoundVCI.setStatus("current")
_HwMplsLdpSessionAtmLabelRangeUpperBoundVPI_Type = AtmVpIdentifier
_HwMplsLdpSessionAtmLabelRangeUpperBoundVPI_Object = MibTableColumn
hwMplsLdpSessionAtmLabelRangeUpperBoundVPI = _HwMplsLdpSessionAtmLabelRangeUpperBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4, 1, 1, 9),
    _HwMplsLdpSessionAtmLabelRangeUpperBoundVPI_Type()
)
hwMplsLdpSessionAtmLabelRangeUpperBoundVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionAtmLabelRangeUpperBoundVPI.setStatus("current")
_HwMplsLdpSessionAtmLabelRangeUpperBoundVCI_Type = AtmVcIdentifier
_HwMplsLdpSessionAtmLabelRangeUpperBoundVCI_Object = MibTableColumn
hwMplsLdpSessionAtmLabelRangeUpperBoundVCI = _HwMplsLdpSessionAtmLabelRangeUpperBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 4, 1, 1, 10),
    _HwMplsLdpSessionAtmLabelRangeUpperBoundVCI_Type()
)
hwMplsLdpSessionAtmLabelRangeUpperBoundVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionAtmLabelRangeUpperBoundVCI.setStatus("current")
_HwMplsLdpHelloAdjacencyObjects_ObjectIdentity = ObjectIdentity
hwMplsLdpHelloAdjacencyObjects = _HwMplsLdpHelloAdjacencyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 5)
)
_HwMplsLdpHelloAdjacencyTable_Object = MibTable
hwMplsLdpHelloAdjacencyTable = _HwMplsLdpHelloAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hwMplsLdpHelloAdjacencyTable.setStatus("current")
_HwMplsLdpHelloAdjacencyEntry_Object = MibTableRow
hwMplsLdpHelloAdjacencyEntry = _HwMplsLdpHelloAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 5, 1, 1)
)
hwMplsLdpHelloAdjacencyEntry.setIndexNames(
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityIfIndex"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpPeerIndex"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpSessionIndex"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpHelloAdjacencyIndex"),
)
if mibBuilder.loadTexts:
    hwMplsLdpHelloAdjacencyEntry.setStatus("current")


class _HwMplsLdpHelloAdjacencyIndex_Type(Unsigned32):
    """Custom type hwMplsLdpHelloAdjacencyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwMplsLdpHelloAdjacencyIndex_Type.__name__ = "Unsigned32"
_HwMplsLdpHelloAdjacencyIndex_Object = MibTableColumn
hwMplsLdpHelloAdjacencyIndex = _HwMplsLdpHelloAdjacencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 5, 1, 1, 1),
    _HwMplsLdpHelloAdjacencyIndex_Type()
)
hwMplsLdpHelloAdjacencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsLdpHelloAdjacencyIndex.setStatus("current")
_HwMplsLdpHelloAdjacencyHoldTimeRemaining_Type = TimeInterval
_HwMplsLdpHelloAdjacencyHoldTimeRemaining_Object = MibTableColumn
hwMplsLdpHelloAdjacencyHoldTimeRemaining = _HwMplsLdpHelloAdjacencyHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 5, 1, 1, 2),
    _HwMplsLdpHelloAdjacencyHoldTimeRemaining_Type()
)
hwMplsLdpHelloAdjacencyHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpHelloAdjacencyHoldTimeRemaining.setStatus("current")
_HwMplsLdpCrlspTnlObjects_ObjectIdentity = ObjectIdentity
hwMplsLdpCrlspTnlObjects = _HwMplsLdpCrlspTnlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6)
)
_HwMplsLdpCrlspTnlTable_Object = MibTable
hwMplsLdpCrlspTnlTable = _HwMplsLdpCrlspTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlTable.setStatus("current")
_HwMplsLdpCrlspTnlEntry_Object = MibTableRow
hwMplsLdpCrlspTnlEntry = _HwMplsLdpCrlspTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1)
)
hwMplsLdpCrlspTnlEntry.setIndexNames(
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpCrlspTnlIndex"),
)
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlEntry.setStatus("current")
_HwMplsLdpCrlspTnlIndex_Type = MplsTunnelIndex
_HwMplsLdpCrlspTnlIndex_Object = MibTableColumn
hwMplsLdpCrlspTnlIndex = _HwMplsLdpCrlspTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 1),
    _HwMplsLdpCrlspTnlIndex_Type()
)
hwMplsLdpCrlspTnlIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlIndex.setStatus("current")
_HwMplsLdpCrlspTnlName_Type = DisplayString
_HwMplsLdpCrlspTnlName_Object = MibTableColumn
hwMplsLdpCrlspTnlName = _HwMplsLdpCrlspTnlName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 2),
    _HwMplsLdpCrlspTnlName_Type()
)
hwMplsLdpCrlspTnlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlName.setStatus("current")


class _HwMplsLdpCrlspTnlDirection_Type(Integer32):
    """Custom type hwMplsLdpCrlspTnlDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("inOut", 3),
          ("out", 2))
    )


_HwMplsLdpCrlspTnlDirection_Type.__name__ = "Integer32"
_HwMplsLdpCrlspTnlDirection_Object = MibTableColumn
hwMplsLdpCrlspTnlDirection = _HwMplsLdpCrlspTnlDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 3),
    _HwMplsLdpCrlspTnlDirection_Type()
)
hwMplsLdpCrlspTnlDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlDirection.setStatus("current")


class _HwMplsLdpCrlspTnlSignallingProto_Type(Integer32):
    """Custom type hwMplsLdpCrlspTnlSignallingProto based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ldp", 2),
          ("none", 1),
          ("rsvp", 3))
    )


_HwMplsLdpCrlspTnlSignallingProto_Type.__name__ = "Integer32"
_HwMplsLdpCrlspTnlSignallingProto_Object = MibTableColumn
hwMplsLdpCrlspTnlSignallingProto = _HwMplsLdpCrlspTnlSignallingProto_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 4),
    _HwMplsLdpCrlspTnlSignallingProto_Type()
)
hwMplsLdpCrlspTnlSignallingProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlSignallingProto.setStatus("current")


class _HwMplsLdpCrlspTnlSetupPrio_Type(Integer32):
    """Custom type hwMplsLdpCrlspTnlSetupPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwMplsLdpCrlspTnlSetupPrio_Type.__name__ = "Integer32"
_HwMplsLdpCrlspTnlSetupPrio_Object = MibTableColumn
hwMplsLdpCrlspTnlSetupPrio = _HwMplsLdpCrlspTnlSetupPrio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 5),
    _HwMplsLdpCrlspTnlSetupPrio_Type()
)
hwMplsLdpCrlspTnlSetupPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlSetupPrio.setStatus("current")


class _HwMplsLdpCrlspTnlHoldingPrio_Type(Integer32):
    """Custom type hwMplsLdpCrlspTnlHoldingPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwMplsLdpCrlspTnlHoldingPrio_Type.__name__ = "Integer32"
_HwMplsLdpCrlspTnlHoldingPrio_Object = MibTableColumn
hwMplsLdpCrlspTnlHoldingPrio = _HwMplsLdpCrlspTnlHoldingPrio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 6),
    _HwMplsLdpCrlspTnlHoldingPrio_Type()
)
hwMplsLdpCrlspTnlHoldingPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlHoldingPrio.setStatus("current")


class _HwMplsLdpCrlspTnlPeakDataRate_Type(BitRate):
    """Custom type hwMplsLdpCrlspTnlPeakDataRate based on BitRate"""
    defaultValue = 0


_HwMplsLdpCrlspTnlPeakDataRate_Object = MibTableColumn
hwMplsLdpCrlspTnlPeakDataRate = _HwMplsLdpCrlspTnlPeakDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 7),
    _HwMplsLdpCrlspTnlPeakDataRate_Type()
)
hwMplsLdpCrlspTnlPeakDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlPeakDataRate.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlPeakDataRate.setUnits("bits per second")


class _HwMplsLdpCrlspTnlPeakBurstSize_Type(BurstSize):
    """Custom type hwMplsLdpCrlspTnlPeakBurstSize based on BurstSize"""
    defaultValue = 0


_HwMplsLdpCrlspTnlPeakBurstSize_Object = MibTableColumn
hwMplsLdpCrlspTnlPeakBurstSize = _HwMplsLdpCrlspTnlPeakBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 8),
    _HwMplsLdpCrlspTnlPeakBurstSize_Type()
)
hwMplsLdpCrlspTnlPeakBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlPeakBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlPeakBurstSize.setUnits("bytes")


class _HwMplsLdpCrlspTnlCommittedDataRate_Type(BitRate):
    """Custom type hwMplsLdpCrlspTnlCommittedDataRate based on BitRate"""
    defaultValue = 0


_HwMplsLdpCrlspTnlCommittedDataRate_Object = MibTableColumn
hwMplsLdpCrlspTnlCommittedDataRate = _HwMplsLdpCrlspTnlCommittedDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 9),
    _HwMplsLdpCrlspTnlCommittedDataRate_Type()
)
hwMplsLdpCrlspTnlCommittedDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlCommittedDataRate.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlCommittedDataRate.setUnits("bits per second")


class _HwMplsLdpCrlspTnlCommittedBurstSize_Type(BurstSize):
    """Custom type hwMplsLdpCrlspTnlCommittedBurstSize based on BurstSize"""
    defaultValue = 0


_HwMplsLdpCrlspTnlCommittedBurstSize_Object = MibTableColumn
hwMplsLdpCrlspTnlCommittedBurstSize = _HwMplsLdpCrlspTnlCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 10),
    _HwMplsLdpCrlspTnlCommittedBurstSize_Type()
)
hwMplsLdpCrlspTnlCommittedBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlCommittedBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlCommittedBurstSize.setUnits("bytes")


class _HwMplsLdpCrlspTnlExcessBurstSize_Type(BurstSize):
    """Custom type hwMplsLdpCrlspTnlExcessBurstSize based on BurstSize"""
    defaultValue = 0


_HwMplsLdpCrlspTnlExcessBurstSize_Object = MibTableColumn
hwMplsLdpCrlspTnlExcessBurstSize = _HwMplsLdpCrlspTnlExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 11),
    _HwMplsLdpCrlspTnlExcessBurstSize_Type()
)
hwMplsLdpCrlspTnlExcessBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlExcessBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlExcessBurstSize.setUnits("bytes")


class _HwMplsLdpCrlspTnlIsPinned_Type(TruthValue):
    """Custom type hwMplsLdpCrlspTnlIsPinned based on TruthValue"""


_HwMplsLdpCrlspTnlIsPinned_Object = MibTableColumn
hwMplsLdpCrlspTnlIsPinned = _HwMplsLdpCrlspTnlIsPinned_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 12),
    _HwMplsLdpCrlspTnlIsPinned_Type()
)
hwMplsLdpCrlspTnlIsPinned.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlIsPinned.setStatus("current")


class _HwMplsLdpCrlspTnlFrequency_Type(Integer32):
    """Custom type hwMplsLdpCrlspTnlFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwMplsLdpCrlspTnlFrequency_Type.__name__ = "Integer32"
_HwMplsLdpCrlspTnlFrequency_Object = MibTableColumn
hwMplsLdpCrlspTnlFrequency = _HwMplsLdpCrlspTnlFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 13),
    _HwMplsLdpCrlspTnlFrequency_Type()
)
hwMplsLdpCrlspTnlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlFrequency.setStatus("current")


class _HwMplsLdpCrlspTnlWeight_Type(Integer32):
    """Custom type hwMplsLdpCrlspTnlWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwMplsLdpCrlspTnlWeight_Type.__name__ = "Integer32"
_HwMplsLdpCrlspTnlWeight_Object = MibTableColumn
hwMplsLdpCrlspTnlWeight = _HwMplsLdpCrlspTnlWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 14),
    _HwMplsLdpCrlspTnlWeight_Type()
)
hwMplsLdpCrlspTnlWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlWeight.setStatus("current")
_HwMplsLdpCrlspTnlRowStatus_Type = RowStatus
_HwMplsLdpCrlspTnlRowStatus_Object = MibTableColumn
hwMplsLdpCrlspTnlRowStatus = _HwMplsLdpCrlspTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 1, 1, 15),
    _HwMplsLdpCrlspTnlRowStatus_Type()
)
hwMplsLdpCrlspTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTnlRowStatus.setStatus("current")
_HwMplsLdpCrlspErHopTable_Object = MibTable
hwMplsLdpCrlspErHopTable = _HwMplsLdpCrlspErHopTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hwMplsLdpCrlspErHopTable.setStatus("current")
_HwMplsLdpCrlspErHopEntry_Object = MibTableRow
hwMplsLdpCrlspErHopEntry = _HwMplsLdpCrlspErHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 2, 1)
)
hwMplsLdpCrlspErHopEntry.setIndexNames(
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpCrlspTnlIndex"),
    (0, "HUAWEI-MPLS-LDP-MIB", "hwMplsLdpCrlspErHopIndex"),
)
if mibBuilder.loadTexts:
    hwMplsLdpCrlspErHopEntry.setStatus("current")
_HwMplsLdpCrlspErHopIndex_Type = Integer32
_HwMplsLdpCrlspErHopIndex_Object = MibTableColumn
hwMplsLdpCrlspErHopIndex = _HwMplsLdpCrlspErHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 2, 1, 1),
    _HwMplsLdpCrlspErHopIndex_Type()
)
hwMplsLdpCrlspErHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspErHopIndex.setStatus("current")


class _HwMplsLdpCrlspErHopAddrType_Type(Integer32):
    """Custom type hwMplsLdpCrlspErHopAddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipV4", 1)
    )


_HwMplsLdpCrlspErHopAddrType_Type.__name__ = "Integer32"
_HwMplsLdpCrlspErHopAddrType_Object = MibTableColumn
hwMplsLdpCrlspErHopAddrType = _HwMplsLdpCrlspErHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 2, 1, 2),
    _HwMplsLdpCrlspErHopAddrType_Type()
)
hwMplsLdpCrlspErHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspErHopAddrType.setStatus("current")
_HwMplsLdpCrlspErHopIpv4Addr_Type = IpAddress
_HwMplsLdpCrlspErHopIpv4Addr_Object = MibTableColumn
hwMplsLdpCrlspErHopIpv4Addr = _HwMplsLdpCrlspErHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 2, 1, 3),
    _HwMplsLdpCrlspErHopIpv4Addr_Type()
)
hwMplsLdpCrlspErHopIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspErHopIpv4Addr.setStatus("current")


class _HwMplsLdpCrlspErHopIpv4PrefixLen_Type(Integer32):
    """Custom type hwMplsLdpCrlspErHopIpv4PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwMplsLdpCrlspErHopIpv4PrefixLen_Type.__name__ = "Integer32"
_HwMplsLdpCrlspErHopIpv4PrefixLen_Object = MibTableColumn
hwMplsLdpCrlspErHopIpv4PrefixLen = _HwMplsLdpCrlspErHopIpv4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 2, 1, 4),
    _HwMplsLdpCrlspErHopIpv4PrefixLen_Type()
)
hwMplsLdpCrlspErHopIpv4PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspErHopIpv4PrefixLen.setStatus("current")


class _HwMplsLdpCrlspErHopStrictOrLoose_Type(Integer32):
    """Custom type hwMplsLdpCrlspErHopStrictOrLoose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 2),
          ("strict", 1))
    )


_HwMplsLdpCrlspErHopStrictOrLoose_Type.__name__ = "Integer32"
_HwMplsLdpCrlspErHopStrictOrLoose_Object = MibTableColumn
hwMplsLdpCrlspErHopStrictOrLoose = _HwMplsLdpCrlspErHopStrictOrLoose_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 2, 1, 5),
    _HwMplsLdpCrlspErHopStrictOrLoose_Type()
)
hwMplsLdpCrlspErHopStrictOrLoose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspErHopStrictOrLoose.setStatus("current")
_HwMplsLdpCrlspErHopRowStatus_Type = RowStatus
_HwMplsLdpCrlspErHopRowStatus_Object = MibTableColumn
hwMplsLdpCrlspErHopRowStatus = _HwMplsLdpCrlspErHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 1, 6, 2, 1, 6),
    _HwMplsLdpCrlspErHopRowStatus_Type()
)
hwMplsLdpCrlspErHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsLdpCrlspErHopRowStatus.setStatus("current")
_HwMplsLdpNotifications_ObjectIdentity = ObjectIdentity
hwMplsLdpNotifications = _HwMplsLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 2)
)
_HwMplsLdpNotificationPrefix_ObjectIdentity = ObjectIdentity
hwMplsLdpNotificationPrefix = _HwMplsLdpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 2, 0)
)
hwMplsLdpEntityEntry.registerAugmentions(
    ("HUAWEI-MPLS-LDP-MIB",
     "hwMplsLdpEntityStatsEntry")
)
hwMplsLdpEntityStatsEntry.setIndexNames(*hwMplsLdpEntityEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hwMplsLdpFailedInitSessionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 2, 0, 1)
)
hwMplsLdpFailedInitSessionThresholdExceeded.setObjects(
      *(("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
        ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityID"),
        ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityFailedInitSessionThreshold"))
)
if mibBuilder.loadTexts:
    hwMplsLdpFailedInitSessionThresholdExceeded.setStatus(
        "current"
    )

hwMplsLdpCrlspTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 2, 0, 2)
)
hwMplsLdpCrlspTunnelUp.setObjects(
      *(("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
        ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityID"),
        ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpCrlspTnlIndex"))
)
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTunnelUp.setStatus(
        "current"
    )

hwMplsLdpCrlspTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 2, 0, 3)
)
hwMplsLdpCrlspTunnelDown.setObjects(
      *(("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
        ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityID"),
        ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpCrlspTnlIndex"))
)
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTunnelDown.setStatus(
        "current"
    )

hwMplsLdpCrlspTunnelSetupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 2, 0, 4)
)
hwMplsLdpCrlspTunnelSetupFailure.setObjects(
      *(("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
        ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityID"),
        ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpCrlspTnlIndex"))
)
if mibBuilder.loadTexts:
    hwMplsLdpCrlspTunnelSetupFailure.setStatus(
        "current"
    )

hwMplsLdpIncarnUpEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 2, 0, 11)
)
hwMplsLdpIncarnUpEventFailure.setObjects(
    ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID")
)
if mibBuilder.loadTexts:
    hwMplsLdpIncarnUpEventFailure.setStatus(
        "current"
    )

hwMplsLdpIncarnDownEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 2, 0, 12)
)
hwMplsLdpIncarnDownEventFailure.setObjects(
    ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID")
)
if mibBuilder.loadTexts:
    hwMplsLdpIncarnDownEventFailure.setStatus(
        "current"
    )

hwMplsLdpEntityUpEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 2, 0, 13)
)
hwMplsLdpEntityUpEventFailure.setObjects(
      *(("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
        ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityID"))
)
if mibBuilder.loadTexts:
    hwMplsLdpEntityUpEventFailure.setStatus(
        "current"
    )

hwMplsLdpEntityDownEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 2, 0, 14)
)
hwMplsLdpEntityDownEventFailure.setObjects(
      *(("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpLsrIncarnID"),
        ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpEntityID"))
)
if mibBuilder.loadTexts:
    hwMplsLdpEntityDownEventFailure.setStatus(
        "current"
    )

hwMplsLdpSessionUpEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 2, 0, 15)
)
hwMplsLdpSessionUpEventFailure.setObjects(
      *(("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpSessionID"),
        ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpSessionState"))
)
if mibBuilder.loadTexts:
    hwMplsLdpSessionUpEventFailure.setStatus(
        "current"
    )

hwMplsLdpSessionDownEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 2, 2, 0, 16)
)
hwMplsLdpSessionDownEventFailure.setObjects(
      *(("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpSessionID"),
        ("HUAWEI-MPLS-LDP-MIB", "hwMplsLdpSessionState"))
)
if mibBuilder.loadTexts:
    hwMplsLdpSessionDownEventFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MPLS-LDP-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "BitRate": BitRate,
       "BurstSize": BurstSize,
       "MplsLsrIdentifier": MplsLsrIdentifier,
       "MplsLdpGenAddr": MplsLdpGenAddr,
       "MplsLdpIdentifier": MplsLdpIdentifier,
       "AtmVpIdentifier": AtmVpIdentifier,
       "AtmVcIdentifier": AtmVcIdentifier,
       "AddressFamilyNumbers": AddressFamilyNumbers,
       "MplsLabel": MplsLabel,
       "MplsTunnelIndex": MplsTunnelIndex,
       "hwMplsLdp": hwMplsLdp,
       "hwMplsLdpObjects": hwMplsLdpObjects,
       "hwMplsLdpLsrObjects": hwMplsLdpLsrObjects,
       "hwMplsLdpLsrIncarnTable": hwMplsLdpLsrIncarnTable,
       "hwMplsLdpLsrIncarnEntry": hwMplsLdpLsrIncarnEntry,
       "hwMplsLdpLsrID": hwMplsLdpLsrID,
       "hwMplsLdpLsrLoopDetectionPresent": hwMplsLdpLsrLoopDetectionPresent,
       "hwMplsLdpLsrLoopDetectionAdminStatus": hwMplsLdpLsrLoopDetectionAdminStatus,
       "hwMplsLdpLsrPathVectorLimit": hwMplsLdpLsrPathVectorLimit,
       "hwMplsLdpLsrHopCountLimit": hwMplsLdpLsrHopCountLimit,
       "hwMplsLdpLsrLoopPreventionPresent": hwMplsLdpLsrLoopPreventionPresent,
       "hwMplsLdpLsrLoopPreventionAdminStatus": hwMplsLdpLsrLoopPreventionAdminStatus,
       "hwMplsLdpLsrLabelRetentionMode": hwMplsLdpLsrLabelRetentionMode,
       "hwMplsLdpLsrIncarnID": hwMplsLdpLsrIncarnID,
       "hwMplsLdpLsrMaxLdpEntities": hwMplsLdpLsrMaxLdpEntities,
       "hwMplsLdpLsrMaxLocalPeers": hwMplsLdpLsrMaxLocalPeers,
       "hwMplsLdpLsrMaxRemotePeers": hwMplsLdpLsrMaxRemotePeers,
       "hwMplsLdpLsrMaxIfaces": hwMplsLdpLsrMaxIfaces,
       "hwMplsLdpLsrMaxLsps": hwMplsLdpLsrMaxLsps,
       "hwMplsLdpLsrMaxCrlspTnls": hwMplsLdpLsrMaxCrlspTnls,
       "hwMplsLdpLsrMaxErhopPerCrlspTnl": hwMplsLdpLsrMaxErhopPerCrlspTnl,
       "hwMplsLdpLsrRowStatus": hwMplsLdpLsrRowStatus,
       "hwMplsLdpLsrMaxVcmCapability": hwMplsLdpLsrMaxVcmCapability,
       "hwMplsLdpLsrVcmPathVecInAllLblMapPresent": hwMplsLdpLsrVcmPathVecInAllLblMapPresent,
       "hwMplsLdpLsrRequestRetrytimerValue": hwMplsLdpLsrRequestRetrytimerValue,
       "hwMplsLdpLsrNumOfRequestRetryAttempts": hwMplsLdpLsrNumOfRequestRetryAttempts,
       "hwMplsLdpEntityObjects": hwMplsLdpEntityObjects,
       "hwMplsLdpEntityTable": hwMplsLdpEntityTable,
       "hwMplsLdpEntityEntry": hwMplsLdpEntityEntry,
       "hwMplsLdpEntityID": hwMplsLdpEntityID,
       "hwMplsLdpEntityLabelSpaceType": hwMplsLdpEntityLabelSpaceType,
       "hwMplsLdpEntityDefVpi": hwMplsLdpEntityDefVpi,
       "hwMplsLdpEntityDefVci": hwMplsLdpEntityDefVci,
       "hwMplsLdpEntityUnlabTrafVpi": hwMplsLdpEntityUnlabTrafVpi,
       "hwMplsLdpEntityUnlabTrafVci": hwMplsLdpEntityUnlabTrafVci,
       "hwMplsLdpEntityMergeCapability": hwMplsLdpEntityMergeCapability,
       "hwMplsLdpEntityVcDirectionality": hwMplsLdpEntityVcDirectionality,
       "hwMplsLdpEntityWellKnownDiscoveryPort": hwMplsLdpEntityWellKnownDiscoveryPort,
       "hwMplsLdpEntityMtu": hwMplsLdpEntityMtu,
       "hwMplsLdpEntityKeepAliveHoldTimer": hwMplsLdpEntityKeepAliveHoldTimer,
       "hwMplsLdpEntityFailedInitSessionThreshold": hwMplsLdpEntityFailedInitSessionThreshold,
       "hwMplsLdpEntityLabelDistributionMethod": hwMplsLdpEntityLabelDistributionMethod,
       "hwMplsLdpEntityLabelAllocationMethod": hwMplsLdpEntityLabelAllocationMethod,
       "hwMplsLdpEntityHelloHoldTimer": hwMplsLdpEntityHelloHoldTimer,
       "hwMplsLdpEntityRowStatus": hwMplsLdpEntityRowStatus,
       "hwMplsLdpEntityIfTable": hwMplsLdpEntityIfTable,
       "hwMplsLdpEntityIfEntry": hwMplsLdpEntityIfEntry,
       "hwMplsLdpEntityIfIndex": hwMplsLdpEntityIfIndex,
       "hwMplsLdpEntityIfIpv4Address": hwMplsLdpEntityIfIpv4Address,
       "hwMplsLdpEntityIfRowStatus": hwMplsLdpEntityIfRowStatus,
       "hwMplsLdpEntityConfAtmLabelRangeTable": hwMplsLdpEntityConfAtmLabelRangeTable,
       "hwMplsLdpEntityConfAtmLabelRangeEntry": hwMplsLdpEntityConfAtmLabelRangeEntry,
       "hwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI": hwMplsLdpEntityConfAtmLabelRangeLowerBoundVPI,
       "hwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI": hwMplsLdpEntityConfAtmLabelRangeLowerBoundVCI,
       "hwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI": hwMplsLdpEntityConfAtmLabelRangeUpperBoundVPI,
       "hwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI": hwMplsLdpEntityConfAtmLabelRangeUpperBoundVCI,
       "hwMplsLdpEntityConfAtmLabelRangeRowStatus": hwMplsLdpEntityConfAtmLabelRangeRowStatus,
       "hwMplsLdpEntityStatsTable": hwMplsLdpEntityStatsTable,
       "hwMplsLdpEntityStatsEntry": hwMplsLdpEntityStatsEntry,
       "hwMplsLdpAttemptedSessions": hwMplsLdpAttemptedSessions,
       "hwMplsLdpPeerObjects": hwMplsLdpPeerObjects,
       "hwMplsLdpPeerTable": hwMplsLdpPeerTable,
       "hwMplsLdpPeerEntry": hwMplsLdpPeerEntry,
       "hwMplsLdpPeerIndex": hwMplsLdpPeerIndex,
       "hwMplsLdpPeerID": hwMplsLdpPeerID,
       "hwMplsLdpPeerInternetworkAddrType": hwMplsLdpPeerInternetworkAddrType,
       "hwMplsLdpPeerInternetworkAddr": hwMplsLdpPeerInternetworkAddr,
       "hwMplsLdpPeerDefaultMtu": hwMplsLdpPeerDefaultMtu,
       "hwMplsLdpPeerKeepAliveHoldTimer": hwMplsLdpPeerKeepAliveHoldTimer,
       "hwMplsLdpPeerLabelDistributionMethod": hwMplsLdpPeerLabelDistributionMethod,
       "hwMplsLdpPeerType": hwMplsLdpPeerType,
       "hwMplsLdpPeerRowStatus": hwMplsLdpPeerRowStatus,
       "hwMplsLdpPeerConfAtmLabelRangeTable": hwMplsLdpPeerConfAtmLabelRangeTable,
       "hwMplsLdpPeerConfAtmLabelRangeEntry": hwMplsLdpPeerConfAtmLabelRangeEntry,
       "hwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI": hwMplsLdpPeerConfAtmLabelRangeLowerBoundVPI,
       "hwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI": hwMplsLdpPeerConfAtmLabelRangeLowerBoundVCI,
       "hwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI": hwMplsLdpPeerConfAtmLabelRangeUpperBoundVPI,
       "hwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI": hwMplsLdpPeerConfAtmLabelRangeUpperBoundVCI,
       "hwMplsLdpSessionObjects": hwMplsLdpSessionObjects,
       "hwMplsLdpSessionTable": hwMplsLdpSessionTable,
       "hwMplsLdpSessionEntry": hwMplsLdpSessionEntry,
       "hwMplsLdpSessionIndex": hwMplsLdpSessionIndex,
       "hwMplsLdpSessionID": hwMplsLdpSessionID,
       "hwMplsLdpSessionProtocolVersion": hwMplsLdpSessionProtocolVersion,
       "hwMplsLdpSessionKeepAliveHoldTimeRemaining": hwMplsLdpSessionKeepAliveHoldTimeRemaining,
       "hwMplsLdpSessionRole": hwMplsLdpSessionRole,
       "hwMplsLdpSessionState": hwMplsLdpSessionState,
       "hwMplsLdpSessionAtmLabelRangeLowerBoundVPI": hwMplsLdpSessionAtmLabelRangeLowerBoundVPI,
       "hwMplsLdpSessionAtmLabelRangeLowerBoundVCI": hwMplsLdpSessionAtmLabelRangeLowerBoundVCI,
       "hwMplsLdpSessionAtmLabelRangeUpperBoundVPI": hwMplsLdpSessionAtmLabelRangeUpperBoundVPI,
       "hwMplsLdpSessionAtmLabelRangeUpperBoundVCI": hwMplsLdpSessionAtmLabelRangeUpperBoundVCI,
       "hwMplsLdpHelloAdjacencyObjects": hwMplsLdpHelloAdjacencyObjects,
       "hwMplsLdpHelloAdjacencyTable": hwMplsLdpHelloAdjacencyTable,
       "hwMplsLdpHelloAdjacencyEntry": hwMplsLdpHelloAdjacencyEntry,
       "hwMplsLdpHelloAdjacencyIndex": hwMplsLdpHelloAdjacencyIndex,
       "hwMplsLdpHelloAdjacencyHoldTimeRemaining": hwMplsLdpHelloAdjacencyHoldTimeRemaining,
       "hwMplsLdpCrlspTnlObjects": hwMplsLdpCrlspTnlObjects,
       "hwMplsLdpCrlspTnlTable": hwMplsLdpCrlspTnlTable,
       "hwMplsLdpCrlspTnlEntry": hwMplsLdpCrlspTnlEntry,
       "hwMplsLdpCrlspTnlIndex": hwMplsLdpCrlspTnlIndex,
       "hwMplsLdpCrlspTnlName": hwMplsLdpCrlspTnlName,
       "hwMplsLdpCrlspTnlDirection": hwMplsLdpCrlspTnlDirection,
       "hwMplsLdpCrlspTnlSignallingProto": hwMplsLdpCrlspTnlSignallingProto,
       "hwMplsLdpCrlspTnlSetupPrio": hwMplsLdpCrlspTnlSetupPrio,
       "hwMplsLdpCrlspTnlHoldingPrio": hwMplsLdpCrlspTnlHoldingPrio,
       "hwMplsLdpCrlspTnlPeakDataRate": hwMplsLdpCrlspTnlPeakDataRate,
       "hwMplsLdpCrlspTnlPeakBurstSize": hwMplsLdpCrlspTnlPeakBurstSize,
       "hwMplsLdpCrlspTnlCommittedDataRate": hwMplsLdpCrlspTnlCommittedDataRate,
       "hwMplsLdpCrlspTnlCommittedBurstSize": hwMplsLdpCrlspTnlCommittedBurstSize,
       "hwMplsLdpCrlspTnlExcessBurstSize": hwMplsLdpCrlspTnlExcessBurstSize,
       "hwMplsLdpCrlspTnlIsPinned": hwMplsLdpCrlspTnlIsPinned,
       "hwMplsLdpCrlspTnlFrequency": hwMplsLdpCrlspTnlFrequency,
       "hwMplsLdpCrlspTnlWeight": hwMplsLdpCrlspTnlWeight,
       "hwMplsLdpCrlspTnlRowStatus": hwMplsLdpCrlspTnlRowStatus,
       "hwMplsLdpCrlspErHopTable": hwMplsLdpCrlspErHopTable,
       "hwMplsLdpCrlspErHopEntry": hwMplsLdpCrlspErHopEntry,
       "hwMplsLdpCrlspErHopIndex": hwMplsLdpCrlspErHopIndex,
       "hwMplsLdpCrlspErHopAddrType": hwMplsLdpCrlspErHopAddrType,
       "hwMplsLdpCrlspErHopIpv4Addr": hwMplsLdpCrlspErHopIpv4Addr,
       "hwMplsLdpCrlspErHopIpv4PrefixLen": hwMplsLdpCrlspErHopIpv4PrefixLen,
       "hwMplsLdpCrlspErHopStrictOrLoose": hwMplsLdpCrlspErHopStrictOrLoose,
       "hwMplsLdpCrlspErHopRowStatus": hwMplsLdpCrlspErHopRowStatus,
       "hwMplsLdpNotifications": hwMplsLdpNotifications,
       "hwMplsLdpNotificationPrefix": hwMplsLdpNotificationPrefix,
       "hwMplsLdpFailedInitSessionThresholdExceeded": hwMplsLdpFailedInitSessionThresholdExceeded,
       "hwMplsLdpCrlspTunnelUp": hwMplsLdpCrlspTunnelUp,
       "hwMplsLdpCrlspTunnelDown": hwMplsLdpCrlspTunnelDown,
       "hwMplsLdpCrlspTunnelSetupFailure": hwMplsLdpCrlspTunnelSetupFailure,
       "hwMplsLdpIncarnUpEventFailure": hwMplsLdpIncarnUpEventFailure,
       "hwMplsLdpIncarnDownEventFailure": hwMplsLdpIncarnDownEventFailure,
       "hwMplsLdpEntityUpEventFailure": hwMplsLdpEntityUpEventFailure,
       "hwMplsLdpEntityDownEventFailure": hwMplsLdpEntityDownEventFailure,
       "hwMplsLdpSessionUpEventFailure": hwMplsLdpSessionUpEventFailure,
       "hwMplsLdpSessionDownEventFailure": hwMplsLdpSessionDownEventFailure}
)
