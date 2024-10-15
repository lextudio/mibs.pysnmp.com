# SNMP MIB module (HPN-ICF-MPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MPLS-LDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:10 2024
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

(hpnicfMpls,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfMpls")

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

hpnicfMplsLdp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2)
)
hpnicfMplsLdp.setRevisions(
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

_HpnicfMplsLdpObjects_ObjectIdentity = ObjectIdentity
hpnicfMplsLdpObjects = _HpnicfMplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1)
)
_HpnicfMplsLdpLsrObjects_ObjectIdentity = ObjectIdentity
hpnicfMplsLdpLsrObjects = _HpnicfMplsLdpLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1)
)
_HpnicfMplsLdpLsrIncarnTable_Object = MibTable
hpnicfMplsLdpLsrIncarnTable = _HpnicfMplsLdpLsrIncarnTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrIncarnTable.setStatus("current")
_HpnicfMplsLdpLsrIncarnEntry_Object = MibTableRow
hpnicfMplsLdpLsrIncarnEntry = _HpnicfMplsLdpLsrIncarnEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1)
)
hpnicfMplsLdpLsrIncarnEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrIncarnEntry.setStatus("current")
_HpnicfMplsLdpLsrID_Type = MplsLsrIdentifier
_HpnicfMplsLdpLsrID_Object = MibTableColumn
hpnicfMplsLdpLsrID = _HpnicfMplsLdpLsrID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 1),
    _HpnicfMplsLdpLsrID_Type()
)
hpnicfMplsLdpLsrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrID.setStatus("current")


class _HpnicfMplsLdpLsrLoopDetectionPresent_Type(TruthValue):
    """Custom type hpnicfMplsLdpLsrLoopDetectionPresent based on TruthValue"""


_HpnicfMplsLdpLsrLoopDetectionPresent_Object = MibTableColumn
hpnicfMplsLdpLsrLoopDetectionPresent = _HpnicfMplsLdpLsrLoopDetectionPresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 2),
    _HpnicfMplsLdpLsrLoopDetectionPresent_Type()
)
hpnicfMplsLdpLsrLoopDetectionPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrLoopDetectionPresent.setStatus("current")


class _HpnicfMplsLdpLsrLoopDetectionAdminStatus_Type(Integer32):
    """Custom type hpnicfMplsLdpLsrLoopDetectionAdminStatus based on Integer32"""
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


_HpnicfMplsLdpLsrLoopDetectionAdminStatus_Type.__name__ = "Integer32"
_HpnicfMplsLdpLsrLoopDetectionAdminStatus_Object = MibTableColumn
hpnicfMplsLdpLsrLoopDetectionAdminStatus = _HpnicfMplsLdpLsrLoopDetectionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 3),
    _HpnicfMplsLdpLsrLoopDetectionAdminStatus_Type()
)
hpnicfMplsLdpLsrLoopDetectionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrLoopDetectionAdminStatus.setStatus("current")


class _HpnicfMplsLdpLsrPathVectorLimit_Type(Integer32):
    """Custom type hpnicfMplsLdpLsrPathVectorLimit based on Integer32"""
    defaultValue = 32


_HpnicfMplsLdpLsrPathVectorLimit_Object = MibTableColumn
hpnicfMplsLdpLsrPathVectorLimit = _HpnicfMplsLdpLsrPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 4),
    _HpnicfMplsLdpLsrPathVectorLimit_Type()
)
hpnicfMplsLdpLsrPathVectorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrPathVectorLimit.setStatus("current")


class _HpnicfMplsLdpLsrHopCountLimit_Type(Integer32):
    """Custom type hpnicfMplsLdpLsrHopCountLimit based on Integer32"""
    defaultValue = 32


_HpnicfMplsLdpLsrHopCountLimit_Object = MibTableColumn
hpnicfMplsLdpLsrHopCountLimit = _HpnicfMplsLdpLsrHopCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 5),
    _HpnicfMplsLdpLsrHopCountLimit_Type()
)
hpnicfMplsLdpLsrHopCountLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrHopCountLimit.setStatus("current")


class _HpnicfMplsLdpLsrLoopPreventionPresent_Type(TruthValue):
    """Custom type hpnicfMplsLdpLsrLoopPreventionPresent based on TruthValue"""


_HpnicfMplsLdpLsrLoopPreventionPresent_Object = MibTableColumn
hpnicfMplsLdpLsrLoopPreventionPresent = _HpnicfMplsLdpLsrLoopPreventionPresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 6),
    _HpnicfMplsLdpLsrLoopPreventionPresent_Type()
)
hpnicfMplsLdpLsrLoopPreventionPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrLoopPreventionPresent.setStatus("current")


class _HpnicfMplsLdpLsrLoopPreventionAdminStatus_Type(Integer32):
    """Custom type hpnicfMplsLdpLsrLoopPreventionAdminStatus based on Integer32"""
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


_HpnicfMplsLdpLsrLoopPreventionAdminStatus_Type.__name__ = "Integer32"
_HpnicfMplsLdpLsrLoopPreventionAdminStatus_Object = MibTableColumn
hpnicfMplsLdpLsrLoopPreventionAdminStatus = _HpnicfMplsLdpLsrLoopPreventionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 7),
    _HpnicfMplsLdpLsrLoopPreventionAdminStatus_Type()
)
hpnicfMplsLdpLsrLoopPreventionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrLoopPreventionAdminStatus.setStatus("current")


class _HpnicfMplsLdpLsrLabelRetentionMode_Type(Integer32):
    """Custom type hpnicfMplsLdpLsrLabelRetentionMode based on Integer32"""
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


_HpnicfMplsLdpLsrLabelRetentionMode_Type.__name__ = "Integer32"
_HpnicfMplsLdpLsrLabelRetentionMode_Object = MibTableColumn
hpnicfMplsLdpLsrLabelRetentionMode = _HpnicfMplsLdpLsrLabelRetentionMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 8),
    _HpnicfMplsLdpLsrLabelRetentionMode_Type()
)
hpnicfMplsLdpLsrLabelRetentionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrLabelRetentionMode.setStatus("current")
_HpnicfMplsLdpLsrIncarnID_Type = Integer32
_HpnicfMplsLdpLsrIncarnID_Object = MibTableColumn
hpnicfMplsLdpLsrIncarnID = _HpnicfMplsLdpLsrIncarnID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 9),
    _HpnicfMplsLdpLsrIncarnID_Type()
)
hpnicfMplsLdpLsrIncarnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrIncarnID.setStatus("current")


class _HpnicfMplsLdpLsrMaxLdpEntities_Type(Integer32):
    """Custom type hpnicfMplsLdpLsrMaxLdpEntities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfMplsLdpLsrMaxLdpEntities_Type.__name__ = "Integer32"
_HpnicfMplsLdpLsrMaxLdpEntities_Object = MibTableColumn
hpnicfMplsLdpLsrMaxLdpEntities = _HpnicfMplsLdpLsrMaxLdpEntities_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 10),
    _HpnicfMplsLdpLsrMaxLdpEntities_Type()
)
hpnicfMplsLdpLsrMaxLdpEntities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrMaxLdpEntities.setStatus("current")


class _HpnicfMplsLdpLsrMaxLocalPeers_Type(Integer32):
    """Custom type hpnicfMplsLdpLsrMaxLocalPeers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfMplsLdpLsrMaxLocalPeers_Type.__name__ = "Integer32"
_HpnicfMplsLdpLsrMaxLocalPeers_Object = MibTableColumn
hpnicfMplsLdpLsrMaxLocalPeers = _HpnicfMplsLdpLsrMaxLocalPeers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 11),
    _HpnicfMplsLdpLsrMaxLocalPeers_Type()
)
hpnicfMplsLdpLsrMaxLocalPeers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrMaxLocalPeers.setStatus("current")


class _HpnicfMplsLdpLsrMaxRemotePeers_Type(Integer32):
    """Custom type hpnicfMplsLdpLsrMaxRemotePeers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfMplsLdpLsrMaxRemotePeers_Type.__name__ = "Integer32"
_HpnicfMplsLdpLsrMaxRemotePeers_Object = MibTableColumn
hpnicfMplsLdpLsrMaxRemotePeers = _HpnicfMplsLdpLsrMaxRemotePeers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 12),
    _HpnicfMplsLdpLsrMaxRemotePeers_Type()
)
hpnicfMplsLdpLsrMaxRemotePeers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrMaxRemotePeers.setStatus("current")
_HpnicfMplsLdpLsrMaxIfaces_Type = Integer32
_HpnicfMplsLdpLsrMaxIfaces_Object = MibTableColumn
hpnicfMplsLdpLsrMaxIfaces = _HpnicfMplsLdpLsrMaxIfaces_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 13),
    _HpnicfMplsLdpLsrMaxIfaces_Type()
)
hpnicfMplsLdpLsrMaxIfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrMaxIfaces.setStatus("current")
_HpnicfMplsLdpLsrMaxLsps_Type = Integer32
_HpnicfMplsLdpLsrMaxLsps_Object = MibTableColumn
hpnicfMplsLdpLsrMaxLsps = _HpnicfMplsLdpLsrMaxLsps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 14),
    _HpnicfMplsLdpLsrMaxLsps_Type()
)
hpnicfMplsLdpLsrMaxLsps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrMaxLsps.setStatus("current")
_HpnicfMplsLdpLsrMaxCrlspTnls_Type = Integer32
_HpnicfMplsLdpLsrMaxCrlspTnls_Object = MibTableColumn
hpnicfMplsLdpLsrMaxCrlspTnls = _HpnicfMplsLdpLsrMaxCrlspTnls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 15),
    _HpnicfMplsLdpLsrMaxCrlspTnls_Type()
)
hpnicfMplsLdpLsrMaxCrlspTnls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrMaxCrlspTnls.setStatus("current")
_HpnicfMplsLdpLsrMaxErhopPerCrlspTnl_Type = Integer32
_HpnicfMplsLdpLsrMaxErhopPerCrlspTnl_Object = MibTableColumn
hpnicfMplsLdpLsrMaxErhopPerCrlspTnl = _HpnicfMplsLdpLsrMaxErhopPerCrlspTnl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 16),
    _HpnicfMplsLdpLsrMaxErhopPerCrlspTnl_Type()
)
hpnicfMplsLdpLsrMaxErhopPerCrlspTnl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrMaxErhopPerCrlspTnl.setStatus("current")
_HpnicfMplsLdpLsrRowStatus_Type = RowStatus
_HpnicfMplsLdpLsrRowStatus_Object = MibTableColumn
hpnicfMplsLdpLsrRowStatus = _HpnicfMplsLdpLsrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 17),
    _HpnicfMplsLdpLsrRowStatus_Type()
)
hpnicfMplsLdpLsrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrRowStatus.setStatus("current")
_HpnicfMplsLdpLsrMaxVcmCapability_Type = Integer32
_HpnicfMplsLdpLsrMaxVcmCapability_Object = MibTableColumn
hpnicfMplsLdpLsrMaxVcmCapability = _HpnicfMplsLdpLsrMaxVcmCapability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 18),
    _HpnicfMplsLdpLsrMaxVcmCapability_Type()
)
hpnicfMplsLdpLsrMaxVcmCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrMaxVcmCapability.setStatus("current")
_HpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent_Type = TruthValue
_HpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent_Object = MibTableColumn
hpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent = _HpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 19),
    _HpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent_Type()
)
hpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent.setStatus("current")
_HpnicfMplsLdpLsrRequestRetrytimerValue_Type = Integer32
_HpnicfMplsLdpLsrRequestRetrytimerValue_Object = MibTableColumn
hpnicfMplsLdpLsrRequestRetrytimerValue = _HpnicfMplsLdpLsrRequestRetrytimerValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 20),
    _HpnicfMplsLdpLsrRequestRetrytimerValue_Type()
)
hpnicfMplsLdpLsrRequestRetrytimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrRequestRetrytimerValue.setStatus("current")
_HpnicfMplsLdpLsrNumOfRequestRetryAttempts_Type = Integer32
_HpnicfMplsLdpLsrNumOfRequestRetryAttempts_Object = MibTableColumn
hpnicfMplsLdpLsrNumOfRequestRetryAttempts = _HpnicfMplsLdpLsrNumOfRequestRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 1, 1, 1, 21),
    _HpnicfMplsLdpLsrNumOfRequestRetryAttempts_Type()
)
hpnicfMplsLdpLsrNumOfRequestRetryAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsLdpLsrNumOfRequestRetryAttempts.setStatus("current")
_HpnicfMplsLdpEntityObjects_ObjectIdentity = ObjectIdentity
hpnicfMplsLdpEntityObjects = _HpnicfMplsLdpEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2)
)
_HpnicfMplsLdpEntityTable_Object = MibTable
hpnicfMplsLdpEntityTable = _HpnicfMplsLdpEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityTable.setStatus("current")
_HpnicfMplsLdpEntityEntry_Object = MibTableRow
hpnicfMplsLdpEntityEntry = _HpnicfMplsLdpEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1)
)
hpnicfMplsLdpEntityEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityEntry.setStatus("current")
_HpnicfMplsLdpEntityID_Type = MplsLdpIdentifier
_HpnicfMplsLdpEntityID_Object = MibTableColumn
hpnicfMplsLdpEntityID = _HpnicfMplsLdpEntityID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 1),
    _HpnicfMplsLdpEntityID_Type()
)
hpnicfMplsLdpEntityID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityID.setStatus("current")


class _HpnicfMplsLdpEntityLabelSpaceType_Type(Integer32):
    """Custom type hpnicfMplsLdpEntityLabelSpaceType based on Integer32"""
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


_HpnicfMplsLdpEntityLabelSpaceType_Type.__name__ = "Integer32"
_HpnicfMplsLdpEntityLabelSpaceType_Object = MibTableColumn
hpnicfMplsLdpEntityLabelSpaceType = _HpnicfMplsLdpEntityLabelSpaceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 2),
    _HpnicfMplsLdpEntityLabelSpaceType_Type()
)
hpnicfMplsLdpEntityLabelSpaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityLabelSpaceType.setStatus("current")
_HpnicfMplsLdpEntityDefVpi_Type = AtmVpIdentifier
_HpnicfMplsLdpEntityDefVpi_Object = MibTableColumn
hpnicfMplsLdpEntityDefVpi = _HpnicfMplsLdpEntityDefVpi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 3),
    _HpnicfMplsLdpEntityDefVpi_Type()
)
hpnicfMplsLdpEntityDefVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityDefVpi.setStatus("current")
_HpnicfMplsLdpEntityDefVci_Type = AtmVcIdentifier
_HpnicfMplsLdpEntityDefVci_Object = MibTableColumn
hpnicfMplsLdpEntityDefVci = _HpnicfMplsLdpEntityDefVci_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 4),
    _HpnicfMplsLdpEntityDefVci_Type()
)
hpnicfMplsLdpEntityDefVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityDefVci.setStatus("current")


class _HpnicfMplsLdpEntityUnlabTrafVpi_Type(AtmVpIdentifier):
    """Custom type hpnicfMplsLdpEntityUnlabTrafVpi based on AtmVpIdentifier"""
    defaultValue = 0


_HpnicfMplsLdpEntityUnlabTrafVpi_Object = MibTableColumn
hpnicfMplsLdpEntityUnlabTrafVpi = _HpnicfMplsLdpEntityUnlabTrafVpi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 5),
    _HpnicfMplsLdpEntityUnlabTrafVpi_Type()
)
hpnicfMplsLdpEntityUnlabTrafVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityUnlabTrafVpi.setStatus("current")


class _HpnicfMplsLdpEntityUnlabTrafVci_Type(AtmVcIdentifier):
    """Custom type hpnicfMplsLdpEntityUnlabTrafVci based on AtmVcIdentifier"""
    defaultValue = 32


_HpnicfMplsLdpEntityUnlabTrafVci_Object = MibTableColumn
hpnicfMplsLdpEntityUnlabTrafVci = _HpnicfMplsLdpEntityUnlabTrafVci_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 6),
    _HpnicfMplsLdpEntityUnlabTrafVci_Type()
)
hpnicfMplsLdpEntityUnlabTrafVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityUnlabTrafVci.setStatus("current")


class _HpnicfMplsLdpEntityMergeCapability_Type(Integer32):
    """Custom type hpnicfMplsLdpEntityMergeCapability based on Integer32"""
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


_HpnicfMplsLdpEntityMergeCapability_Type.__name__ = "Integer32"
_HpnicfMplsLdpEntityMergeCapability_Object = MibTableColumn
hpnicfMplsLdpEntityMergeCapability = _HpnicfMplsLdpEntityMergeCapability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 7),
    _HpnicfMplsLdpEntityMergeCapability_Type()
)
hpnicfMplsLdpEntityMergeCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityMergeCapability.setStatus("current")


class _HpnicfMplsLdpEntityVcDirectionality_Type(Integer32):
    """Custom type hpnicfMplsLdpEntityVcDirectionality based on Integer32"""
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


_HpnicfMplsLdpEntityVcDirectionality_Type.__name__ = "Integer32"
_HpnicfMplsLdpEntityVcDirectionality_Object = MibTableColumn
hpnicfMplsLdpEntityVcDirectionality = _HpnicfMplsLdpEntityVcDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 8),
    _HpnicfMplsLdpEntityVcDirectionality_Type()
)
hpnicfMplsLdpEntityVcDirectionality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityVcDirectionality.setStatus("current")
_HpnicfMplsLdpEntityWellKnownDiscoveryPort_Type = Integer32
_HpnicfMplsLdpEntityWellKnownDiscoveryPort_Object = MibTableColumn
hpnicfMplsLdpEntityWellKnownDiscoveryPort = _HpnicfMplsLdpEntityWellKnownDiscoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 9),
    _HpnicfMplsLdpEntityWellKnownDiscoveryPort_Type()
)
hpnicfMplsLdpEntityWellKnownDiscoveryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityWellKnownDiscoveryPort.setStatus("current")


class _HpnicfMplsLdpEntityMtu_Type(Integer32):
    """Custom type hpnicfMplsLdpEntityMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfMplsLdpEntityMtu_Type.__name__ = "Integer32"
_HpnicfMplsLdpEntityMtu_Object = MibTableColumn
hpnicfMplsLdpEntityMtu = _HpnicfMplsLdpEntityMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 10),
    _HpnicfMplsLdpEntityMtu_Type()
)
hpnicfMplsLdpEntityMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityMtu.setStatus("current")


class _HpnicfMplsLdpEntityKeepAliveHoldTimer_Type(Integer32):
    """Custom type hpnicfMplsLdpEntityKeepAliveHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfMplsLdpEntityKeepAliveHoldTimer_Type.__name__ = "Integer32"
_HpnicfMplsLdpEntityKeepAliveHoldTimer_Object = MibTableColumn
hpnicfMplsLdpEntityKeepAliveHoldTimer = _HpnicfMplsLdpEntityKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 11),
    _HpnicfMplsLdpEntityKeepAliveHoldTimer_Type()
)
hpnicfMplsLdpEntityKeepAliveHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityKeepAliveHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityKeepAliveHoldTimer.setUnits("seconds")
_HpnicfMplsLdpEntityFailedInitSessionThreshold_Type = Integer32
_HpnicfMplsLdpEntityFailedInitSessionThreshold_Object = MibTableColumn
hpnicfMplsLdpEntityFailedInitSessionThreshold = _HpnicfMplsLdpEntityFailedInitSessionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 12),
    _HpnicfMplsLdpEntityFailedInitSessionThreshold_Type()
)
hpnicfMplsLdpEntityFailedInitSessionThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityFailedInitSessionThreshold.setStatus("current")


class _HpnicfMplsLdpEntityLabelDistributionMethod_Type(Integer32):
    """Custom type hpnicfMplsLdpEntityLabelDistributionMethod based on Integer32"""
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


_HpnicfMplsLdpEntityLabelDistributionMethod_Type.__name__ = "Integer32"
_HpnicfMplsLdpEntityLabelDistributionMethod_Object = MibTableColumn
hpnicfMplsLdpEntityLabelDistributionMethod = _HpnicfMplsLdpEntityLabelDistributionMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 13),
    _HpnicfMplsLdpEntityLabelDistributionMethod_Type()
)
hpnicfMplsLdpEntityLabelDistributionMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityLabelDistributionMethod.setStatus("current")


class _HpnicfMplsLdpEntityLabelAllocationMethod_Type(Integer32):
    """Custom type hpnicfMplsLdpEntityLabelAllocationMethod based on Integer32"""
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


_HpnicfMplsLdpEntityLabelAllocationMethod_Type.__name__ = "Integer32"
_HpnicfMplsLdpEntityLabelAllocationMethod_Object = MibTableColumn
hpnicfMplsLdpEntityLabelAllocationMethod = _HpnicfMplsLdpEntityLabelAllocationMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 14),
    _HpnicfMplsLdpEntityLabelAllocationMethod_Type()
)
hpnicfMplsLdpEntityLabelAllocationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityLabelAllocationMethod.setStatus("current")


class _HpnicfMplsLdpEntityHelloHoldTimer_Type(Integer32):
    """Custom type hpnicfMplsLdpEntityHelloHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfMplsLdpEntityHelloHoldTimer_Type.__name__ = "Integer32"
_HpnicfMplsLdpEntityHelloHoldTimer_Object = MibTableColumn
hpnicfMplsLdpEntityHelloHoldTimer = _HpnicfMplsLdpEntityHelloHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 15),
    _HpnicfMplsLdpEntityHelloHoldTimer_Type()
)
hpnicfMplsLdpEntityHelloHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityHelloHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityHelloHoldTimer.setUnits("seconds")
_HpnicfMplsLdpEntityRowStatus_Type = RowStatus
_HpnicfMplsLdpEntityRowStatus_Object = MibTableColumn
hpnicfMplsLdpEntityRowStatus = _HpnicfMplsLdpEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 1, 1, 16),
    _HpnicfMplsLdpEntityRowStatus_Type()
)
hpnicfMplsLdpEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityRowStatus.setStatus("current")
_HpnicfMplsLdpEntityIfTable_Object = MibTable
hpnicfMplsLdpEntityIfTable = _HpnicfMplsLdpEntityIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityIfTable.setStatus("current")
_HpnicfMplsLdpEntityIfEntry_Object = MibTableRow
hpnicfMplsLdpEntityIfEntry = _HpnicfMplsLdpEntityIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 2, 1)
)
hpnicfMplsLdpEntityIfEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityIfEntry.setStatus("current")


class _HpnicfMplsLdpEntityIfIndex_Type(Unsigned32):
    """Custom type hpnicfMplsLdpEntityIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfMplsLdpEntityIfIndex_Type.__name__ = "Unsigned32"
_HpnicfMplsLdpEntityIfIndex_Object = MibTableColumn
hpnicfMplsLdpEntityIfIndex = _HpnicfMplsLdpEntityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 2, 1, 1),
    _HpnicfMplsLdpEntityIfIndex_Type()
)
hpnicfMplsLdpEntityIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityIfIndex.setStatus("current")
_HpnicfMplsLdpEntityIfIpv4Address_Type = IpAddress
_HpnicfMplsLdpEntityIfIpv4Address_Object = MibTableColumn
hpnicfMplsLdpEntityIfIpv4Address = _HpnicfMplsLdpEntityIfIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 2, 1, 2),
    _HpnicfMplsLdpEntityIfIpv4Address_Type()
)
hpnicfMplsLdpEntityIfIpv4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityIfIpv4Address.setStatus("current")
_HpnicfMplsLdpEntityIfRowStatus_Type = RowStatus
_HpnicfMplsLdpEntityIfRowStatus_Object = MibTableColumn
hpnicfMplsLdpEntityIfRowStatus = _HpnicfMplsLdpEntityIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 2, 1, 3),
    _HpnicfMplsLdpEntityIfRowStatus_Type()
)
hpnicfMplsLdpEntityIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityIfRowStatus.setStatus("current")
_HpnicfMplsLdpEntityConfAtmLabelRangeTable_Object = MibTable
hpnicfMplsLdpEntityConfAtmLabelRangeTable = _HpnicfMplsLdpEntityConfAtmLabelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityConfAtmLabelRangeTable.setStatus("current")
_HpnicfMplsLdpEntityConfAtmLabelRangeEntry_Object = MibTableRow
hpnicfMplsLdpEntityConfAtmLabelRangeEntry = _HpnicfMplsLdpEntityConfAtmLabelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 3, 1)
)
hpnicfMplsLdpEntityConfAtmLabelRangeEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityIfIndex"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI"),
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityConfAtmLabelRangeEntry.setStatus("current")
_HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Type = AtmVpIdentifier
_HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Object = MibTableColumn
hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI = _HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 3, 1, 1),
    _HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Type()
)
hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI.setStatus("current")
_HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Type = AtmVcIdentifier
_HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Object = MibTableColumn
hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI = _HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 3, 1, 2),
    _HpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Type()
)
hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI.setStatus("current")
_HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Type = AtmVpIdentifier
_HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Object = MibTableColumn
hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI = _HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 3, 1, 3),
    _HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Type()
)
hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI.setStatus("current")
_HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Type = AtmVcIdentifier
_HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Object = MibTableColumn
hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI = _HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 3, 1, 4),
    _HpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Type()
)
hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI.setStatus("current")
_HpnicfMplsLdpEntityConfAtmLabelRangeRowStatus_Type = RowStatus
_HpnicfMplsLdpEntityConfAtmLabelRangeRowStatus_Object = MibTableColumn
hpnicfMplsLdpEntityConfAtmLabelRangeRowStatus = _HpnicfMplsLdpEntityConfAtmLabelRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 3, 1, 5),
    _HpnicfMplsLdpEntityConfAtmLabelRangeRowStatus_Type()
)
hpnicfMplsLdpEntityConfAtmLabelRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityConfAtmLabelRangeRowStatus.setStatus("current")
_HpnicfMplsLdpEntityStatsTable_Object = MibTable
hpnicfMplsLdpEntityStatsTable = _HpnicfMplsLdpEntityStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityStatsTable.setStatus("current")
_HpnicfMplsLdpEntityStatsEntry_Object = MibTableRow
hpnicfMplsLdpEntityStatsEntry = _HpnicfMplsLdpEntityStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityStatsEntry.setStatus("current")
_HpnicfMplsLdpAttemptedSessions_Type = Counter32
_HpnicfMplsLdpAttemptedSessions_Object = MibTableColumn
hpnicfMplsLdpAttemptedSessions = _HpnicfMplsLdpAttemptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 2, 4, 1, 1),
    _HpnicfMplsLdpAttemptedSessions_Type()
)
hpnicfMplsLdpAttemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpAttemptedSessions.setStatus("current")
_HpnicfMplsLdpPeerObjects_ObjectIdentity = ObjectIdentity
hpnicfMplsLdpPeerObjects = _HpnicfMplsLdpPeerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3)
)
_HpnicfMplsLdpPeerTable_Object = MibTable
hpnicfMplsLdpPeerTable = _HpnicfMplsLdpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerTable.setStatus("current")
_HpnicfMplsLdpPeerEntry_Object = MibTableRow
hpnicfMplsLdpPeerEntry = _HpnicfMplsLdpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 1, 1)
)
hpnicfMplsLdpPeerEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityIfIndex"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpPeerIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerEntry.setStatus("current")


class _HpnicfMplsLdpPeerIndex_Type(Unsigned32):
    """Custom type hpnicfMplsLdpPeerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfMplsLdpPeerIndex_Type.__name__ = "Unsigned32"
_HpnicfMplsLdpPeerIndex_Object = MibTableColumn
hpnicfMplsLdpPeerIndex = _HpnicfMplsLdpPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 1, 1, 1),
    _HpnicfMplsLdpPeerIndex_Type()
)
hpnicfMplsLdpPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerIndex.setStatus("current")
_HpnicfMplsLdpPeerID_Type = MplsLdpIdentifier
_HpnicfMplsLdpPeerID_Object = MibTableColumn
hpnicfMplsLdpPeerID = _HpnicfMplsLdpPeerID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 1, 1, 2),
    _HpnicfMplsLdpPeerID_Type()
)
hpnicfMplsLdpPeerID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerID.setStatus("current")
_HpnicfMplsLdpPeerInternetworkAddrType_Type = AddressFamilyNumbers
_HpnicfMplsLdpPeerInternetworkAddrType_Object = MibTableColumn
hpnicfMplsLdpPeerInternetworkAddrType = _HpnicfMplsLdpPeerInternetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 1, 1, 3),
    _HpnicfMplsLdpPeerInternetworkAddrType_Type()
)
hpnicfMplsLdpPeerInternetworkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerInternetworkAddrType.setStatus("current")
_HpnicfMplsLdpPeerInternetworkAddr_Type = MplsLdpGenAddr
_HpnicfMplsLdpPeerInternetworkAddr_Object = MibTableColumn
hpnicfMplsLdpPeerInternetworkAddr = _HpnicfMplsLdpPeerInternetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 1, 1, 4),
    _HpnicfMplsLdpPeerInternetworkAddr_Type()
)
hpnicfMplsLdpPeerInternetworkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerInternetworkAddr.setStatus("current")


class _HpnicfMplsLdpPeerDefaultMtu_Type(Integer32):
    """Custom type hpnicfMplsLdpPeerDefaultMtu based on Integer32"""
    defaultValue = 9180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfMplsLdpPeerDefaultMtu_Type.__name__ = "Integer32"
_HpnicfMplsLdpPeerDefaultMtu_Object = MibTableColumn
hpnicfMplsLdpPeerDefaultMtu = _HpnicfMplsLdpPeerDefaultMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 1, 1, 5),
    _HpnicfMplsLdpPeerDefaultMtu_Type()
)
hpnicfMplsLdpPeerDefaultMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerDefaultMtu.setStatus("current")


class _HpnicfMplsLdpPeerKeepAliveHoldTimer_Type(Integer32):
    """Custom type hpnicfMplsLdpPeerKeepAliveHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfMplsLdpPeerKeepAliveHoldTimer_Type.__name__ = "Integer32"
_HpnicfMplsLdpPeerKeepAliveHoldTimer_Object = MibTableColumn
hpnicfMplsLdpPeerKeepAliveHoldTimer = _HpnicfMplsLdpPeerKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 1, 1, 6),
    _HpnicfMplsLdpPeerKeepAliveHoldTimer_Type()
)
hpnicfMplsLdpPeerKeepAliveHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerKeepAliveHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerKeepAliveHoldTimer.setUnits("seconds")


class _HpnicfMplsLdpPeerLabelDistributionMethod_Type(Integer32):
    """Custom type hpnicfMplsLdpPeerLabelDistributionMethod based on Integer32"""
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


_HpnicfMplsLdpPeerLabelDistributionMethod_Type.__name__ = "Integer32"
_HpnicfMplsLdpPeerLabelDistributionMethod_Object = MibTableColumn
hpnicfMplsLdpPeerLabelDistributionMethod = _HpnicfMplsLdpPeerLabelDistributionMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 1, 1, 7),
    _HpnicfMplsLdpPeerLabelDistributionMethod_Type()
)
hpnicfMplsLdpPeerLabelDistributionMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerLabelDistributionMethod.setStatus("current")


class _HpnicfMplsLdpPeerType_Type(Integer32):
    """Custom type hpnicfMplsLdpPeerType based on Integer32"""
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


_HpnicfMplsLdpPeerType_Type.__name__ = "Integer32"
_HpnicfMplsLdpPeerType_Object = MibTableColumn
hpnicfMplsLdpPeerType = _HpnicfMplsLdpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 1, 1, 8),
    _HpnicfMplsLdpPeerType_Type()
)
hpnicfMplsLdpPeerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerType.setStatus("current")
_HpnicfMplsLdpPeerRowStatus_Type = RowStatus
_HpnicfMplsLdpPeerRowStatus_Object = MibTableColumn
hpnicfMplsLdpPeerRowStatus = _HpnicfMplsLdpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 1, 1, 9),
    _HpnicfMplsLdpPeerRowStatus_Type()
)
hpnicfMplsLdpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerRowStatus.setStatus("current")
_HpnicfMplsLdpPeerConfAtmLabelRangeTable_Object = MibTable
hpnicfMplsLdpPeerConfAtmLabelRangeTable = _HpnicfMplsLdpPeerConfAtmLabelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerConfAtmLabelRangeTable.setStatus("current")
_HpnicfMplsLdpPeerConfAtmLabelRangeEntry_Object = MibTableRow
hpnicfMplsLdpPeerConfAtmLabelRangeEntry = _HpnicfMplsLdpPeerConfAtmLabelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 2, 1)
)
hpnicfMplsLdpPeerConfAtmLabelRangeEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityIfIndex"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpPeerIndex"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI"),
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerConfAtmLabelRangeEntry.setStatus("current")
_HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Type = AtmVpIdentifier
_HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Object = MibTableColumn
hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI = _HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 2, 1, 1),
    _HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Type()
)
hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI.setStatus("current")
_HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Type = AtmVcIdentifier
_HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Object = MibTableColumn
hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI = _HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 2, 1, 2),
    _HpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Type()
)
hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI.setStatus("current")
_HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Type = AtmVpIdentifier
_HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Object = MibTableColumn
hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI = _HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 2, 1, 3),
    _HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Type()
)
hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI.setStatus("current")
_HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Type = AtmVcIdentifier
_HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Object = MibTableColumn
hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI = _HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 3, 2, 1, 4),
    _HpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Type()
)
hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI.setStatus("current")
_HpnicfMplsLdpSessionObjects_ObjectIdentity = ObjectIdentity
hpnicfMplsLdpSessionObjects = _HpnicfMplsLdpSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4)
)
_HpnicfMplsLdpSessionTable_Object = MibTable
hpnicfMplsLdpSessionTable = _HpnicfMplsLdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionTable.setStatus("current")
_HpnicfMplsLdpSessionEntry_Object = MibTableRow
hpnicfMplsLdpSessionEntry = _HpnicfMplsLdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4, 1, 1)
)
hpnicfMplsLdpSessionEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityIfIndex"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpPeerIndex"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpSessionIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionEntry.setStatus("current")


class _HpnicfMplsLdpSessionIndex_Type(Unsigned32):
    """Custom type hpnicfMplsLdpSessionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfMplsLdpSessionIndex_Type.__name__ = "Unsigned32"
_HpnicfMplsLdpSessionIndex_Object = MibTableColumn
hpnicfMplsLdpSessionIndex = _HpnicfMplsLdpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4, 1, 1, 1),
    _HpnicfMplsLdpSessionIndex_Type()
)
hpnicfMplsLdpSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionIndex.setStatus("current")
_HpnicfMplsLdpSessionID_Type = MplsLdpIdentifier
_HpnicfMplsLdpSessionID_Object = MibTableColumn
hpnicfMplsLdpSessionID = _HpnicfMplsLdpSessionID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4, 1, 1, 2),
    _HpnicfMplsLdpSessionID_Type()
)
hpnicfMplsLdpSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionID.setStatus("current")


class _HpnicfMplsLdpSessionProtocolVersion_Type(Integer32):
    """Custom type hpnicfMplsLdpSessionProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfMplsLdpSessionProtocolVersion_Type.__name__ = "Integer32"
_HpnicfMplsLdpSessionProtocolVersion_Object = MibTableColumn
hpnicfMplsLdpSessionProtocolVersion = _HpnicfMplsLdpSessionProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4, 1, 1, 3),
    _HpnicfMplsLdpSessionProtocolVersion_Type()
)
hpnicfMplsLdpSessionProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionProtocolVersion.setStatus("current")
_HpnicfMplsLdpSessionKeepAliveHoldTimeRemaining_Type = TimeInterval
_HpnicfMplsLdpSessionKeepAliveHoldTimeRemaining_Object = MibTableColumn
hpnicfMplsLdpSessionKeepAliveHoldTimeRemaining = _HpnicfMplsLdpSessionKeepAliveHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4, 1, 1, 4),
    _HpnicfMplsLdpSessionKeepAliveHoldTimeRemaining_Type()
)
hpnicfMplsLdpSessionKeepAliveHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionKeepAliveHoldTimeRemaining.setStatus("current")


class _HpnicfMplsLdpSessionRole_Type(Integer32):
    """Custom type hpnicfMplsLdpSessionRole based on Integer32"""
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


_HpnicfMplsLdpSessionRole_Type.__name__ = "Integer32"
_HpnicfMplsLdpSessionRole_Object = MibTableColumn
hpnicfMplsLdpSessionRole = _HpnicfMplsLdpSessionRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4, 1, 1, 5),
    _HpnicfMplsLdpSessionRole_Type()
)
hpnicfMplsLdpSessionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionRole.setStatus("current")


class _HpnicfMplsLdpSessionState_Type(Integer32):
    """Custom type hpnicfMplsLdpSessionState based on Integer32"""
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


_HpnicfMplsLdpSessionState_Type.__name__ = "Integer32"
_HpnicfMplsLdpSessionState_Object = MibTableColumn
hpnicfMplsLdpSessionState = _HpnicfMplsLdpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4, 1, 1, 6),
    _HpnicfMplsLdpSessionState_Type()
)
hpnicfMplsLdpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionState.setStatus("current")
_HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI_Type = AtmVpIdentifier
_HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI_Object = MibTableColumn
hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI = _HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4, 1, 1, 7),
    _HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI_Type()
)
hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI.setStatus("current")
_HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI_Type = AtmVcIdentifier
_HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI_Object = MibTableColumn
hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI = _HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4, 1, 1, 8),
    _HpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI_Type()
)
hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI.setStatus("current")
_HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI_Type = AtmVpIdentifier
_HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI_Object = MibTableColumn
hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI = _HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4, 1, 1, 9),
    _HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI_Type()
)
hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI.setStatus("current")
_HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI_Type = AtmVcIdentifier
_HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI_Object = MibTableColumn
hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI = _HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 4, 1, 1, 10),
    _HpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI_Type()
)
hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI.setStatus("current")
_HpnicfMplsLdpHelloAdjacencyObjects_ObjectIdentity = ObjectIdentity
hpnicfMplsLdpHelloAdjacencyObjects = _HpnicfMplsLdpHelloAdjacencyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 5)
)
_HpnicfMplsLdpHelloAdjacencyTable_Object = MibTable
hpnicfMplsLdpHelloAdjacencyTable = _HpnicfMplsLdpHelloAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpHelloAdjacencyTable.setStatus("current")
_HpnicfMplsLdpHelloAdjacencyEntry_Object = MibTableRow
hpnicfMplsLdpHelloAdjacencyEntry = _HpnicfMplsLdpHelloAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 5, 1, 1)
)
hpnicfMplsLdpHelloAdjacencyEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityIfIndex"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpPeerIndex"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpSessionIndex"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpHelloAdjacencyIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpHelloAdjacencyEntry.setStatus("current")


class _HpnicfMplsLdpHelloAdjacencyIndex_Type(Unsigned32):
    """Custom type hpnicfMplsLdpHelloAdjacencyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfMplsLdpHelloAdjacencyIndex_Type.__name__ = "Unsigned32"
_HpnicfMplsLdpHelloAdjacencyIndex_Object = MibTableColumn
hpnicfMplsLdpHelloAdjacencyIndex = _HpnicfMplsLdpHelloAdjacencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 5, 1, 1, 1),
    _HpnicfMplsLdpHelloAdjacencyIndex_Type()
)
hpnicfMplsLdpHelloAdjacencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsLdpHelloAdjacencyIndex.setStatus("current")
_HpnicfMplsLdpHelloAdjacencyHoldTimeRemaining_Type = TimeInterval
_HpnicfMplsLdpHelloAdjacencyHoldTimeRemaining_Object = MibTableColumn
hpnicfMplsLdpHelloAdjacencyHoldTimeRemaining = _HpnicfMplsLdpHelloAdjacencyHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 5, 1, 1, 2),
    _HpnicfMplsLdpHelloAdjacencyHoldTimeRemaining_Type()
)
hpnicfMplsLdpHelloAdjacencyHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsLdpHelloAdjacencyHoldTimeRemaining.setStatus("current")
_HpnicfMplsLdpCrlspTnlObjects_ObjectIdentity = ObjectIdentity
hpnicfMplsLdpCrlspTnlObjects = _HpnicfMplsLdpCrlspTnlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6)
)
_HpnicfMplsLdpCrlspTnlTable_Object = MibTable
hpnicfMplsLdpCrlspTnlTable = _HpnicfMplsLdpCrlspTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlTable.setStatus("current")
_HpnicfMplsLdpCrlspTnlEntry_Object = MibTableRow
hpnicfMplsLdpCrlspTnlEntry = _HpnicfMplsLdpCrlspTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1)
)
hpnicfMplsLdpCrlspTnlEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpCrlspTnlIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlEntry.setStatus("current")
_HpnicfMplsLdpCrlspTnlIndex_Type = MplsTunnelIndex
_HpnicfMplsLdpCrlspTnlIndex_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlIndex = _HpnicfMplsLdpCrlspTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 1),
    _HpnicfMplsLdpCrlspTnlIndex_Type()
)
hpnicfMplsLdpCrlspTnlIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlIndex.setStatus("current")
_HpnicfMplsLdpCrlspTnlName_Type = DisplayString
_HpnicfMplsLdpCrlspTnlName_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlName = _HpnicfMplsLdpCrlspTnlName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 2),
    _HpnicfMplsLdpCrlspTnlName_Type()
)
hpnicfMplsLdpCrlspTnlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlName.setStatus("current")


class _HpnicfMplsLdpCrlspTnlDirection_Type(Integer32):
    """Custom type hpnicfMplsLdpCrlspTnlDirection based on Integer32"""
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


_HpnicfMplsLdpCrlspTnlDirection_Type.__name__ = "Integer32"
_HpnicfMplsLdpCrlspTnlDirection_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlDirection = _HpnicfMplsLdpCrlspTnlDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 3),
    _HpnicfMplsLdpCrlspTnlDirection_Type()
)
hpnicfMplsLdpCrlspTnlDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlDirection.setStatus("current")


class _HpnicfMplsLdpCrlspTnlSignallingProto_Type(Integer32):
    """Custom type hpnicfMplsLdpCrlspTnlSignallingProto based on Integer32"""
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


_HpnicfMplsLdpCrlspTnlSignallingProto_Type.__name__ = "Integer32"
_HpnicfMplsLdpCrlspTnlSignallingProto_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlSignallingProto = _HpnicfMplsLdpCrlspTnlSignallingProto_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 4),
    _HpnicfMplsLdpCrlspTnlSignallingProto_Type()
)
hpnicfMplsLdpCrlspTnlSignallingProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlSignallingProto.setStatus("current")


class _HpnicfMplsLdpCrlspTnlSetupPrio_Type(Integer32):
    """Custom type hpnicfMplsLdpCrlspTnlSetupPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfMplsLdpCrlspTnlSetupPrio_Type.__name__ = "Integer32"
_HpnicfMplsLdpCrlspTnlSetupPrio_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlSetupPrio = _HpnicfMplsLdpCrlspTnlSetupPrio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 5),
    _HpnicfMplsLdpCrlspTnlSetupPrio_Type()
)
hpnicfMplsLdpCrlspTnlSetupPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlSetupPrio.setStatus("current")


class _HpnicfMplsLdpCrlspTnlHoldingPrio_Type(Integer32):
    """Custom type hpnicfMplsLdpCrlspTnlHoldingPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfMplsLdpCrlspTnlHoldingPrio_Type.__name__ = "Integer32"
_HpnicfMplsLdpCrlspTnlHoldingPrio_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlHoldingPrio = _HpnicfMplsLdpCrlspTnlHoldingPrio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 6),
    _HpnicfMplsLdpCrlspTnlHoldingPrio_Type()
)
hpnicfMplsLdpCrlspTnlHoldingPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlHoldingPrio.setStatus("current")


class _HpnicfMplsLdpCrlspTnlPeakDataRate_Type(BitRate):
    """Custom type hpnicfMplsLdpCrlspTnlPeakDataRate based on BitRate"""
    defaultValue = 0


_HpnicfMplsLdpCrlspTnlPeakDataRate_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlPeakDataRate = _HpnicfMplsLdpCrlspTnlPeakDataRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 7),
    _HpnicfMplsLdpCrlspTnlPeakDataRate_Type()
)
hpnicfMplsLdpCrlspTnlPeakDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlPeakDataRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlPeakDataRate.setUnits("bits per second")


class _HpnicfMplsLdpCrlspTnlPeakBurstSize_Type(BurstSize):
    """Custom type hpnicfMplsLdpCrlspTnlPeakBurstSize based on BurstSize"""
    defaultValue = 0


_HpnicfMplsLdpCrlspTnlPeakBurstSize_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlPeakBurstSize = _HpnicfMplsLdpCrlspTnlPeakBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 8),
    _HpnicfMplsLdpCrlspTnlPeakBurstSize_Type()
)
hpnicfMplsLdpCrlspTnlPeakBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlPeakBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlPeakBurstSize.setUnits("bytes")


class _HpnicfMplsLdpCrlspTnlCommittedDataRate_Type(BitRate):
    """Custom type hpnicfMplsLdpCrlspTnlCommittedDataRate based on BitRate"""
    defaultValue = 0


_HpnicfMplsLdpCrlspTnlCommittedDataRate_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlCommittedDataRate = _HpnicfMplsLdpCrlspTnlCommittedDataRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 9),
    _HpnicfMplsLdpCrlspTnlCommittedDataRate_Type()
)
hpnicfMplsLdpCrlspTnlCommittedDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlCommittedDataRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlCommittedDataRate.setUnits("bits per second")


class _HpnicfMplsLdpCrlspTnlCommittedBurstSize_Type(BurstSize):
    """Custom type hpnicfMplsLdpCrlspTnlCommittedBurstSize based on BurstSize"""
    defaultValue = 0


_HpnicfMplsLdpCrlspTnlCommittedBurstSize_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlCommittedBurstSize = _HpnicfMplsLdpCrlspTnlCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 10),
    _HpnicfMplsLdpCrlspTnlCommittedBurstSize_Type()
)
hpnicfMplsLdpCrlspTnlCommittedBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlCommittedBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlCommittedBurstSize.setUnits("bytes")


class _HpnicfMplsLdpCrlspTnlExcessBurstSize_Type(BurstSize):
    """Custom type hpnicfMplsLdpCrlspTnlExcessBurstSize based on BurstSize"""
    defaultValue = 0


_HpnicfMplsLdpCrlspTnlExcessBurstSize_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlExcessBurstSize = _HpnicfMplsLdpCrlspTnlExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 11),
    _HpnicfMplsLdpCrlspTnlExcessBurstSize_Type()
)
hpnicfMplsLdpCrlspTnlExcessBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlExcessBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlExcessBurstSize.setUnits("bytes")


class _HpnicfMplsLdpCrlspTnlIsPinned_Type(TruthValue):
    """Custom type hpnicfMplsLdpCrlspTnlIsPinned based on TruthValue"""


_HpnicfMplsLdpCrlspTnlIsPinned_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlIsPinned = _HpnicfMplsLdpCrlspTnlIsPinned_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 12),
    _HpnicfMplsLdpCrlspTnlIsPinned_Type()
)
hpnicfMplsLdpCrlspTnlIsPinned.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlIsPinned.setStatus("current")


class _HpnicfMplsLdpCrlspTnlFrequency_Type(Integer32):
    """Custom type hpnicfMplsLdpCrlspTnlFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HpnicfMplsLdpCrlspTnlFrequency_Type.__name__ = "Integer32"
_HpnicfMplsLdpCrlspTnlFrequency_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlFrequency = _HpnicfMplsLdpCrlspTnlFrequency_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 13),
    _HpnicfMplsLdpCrlspTnlFrequency_Type()
)
hpnicfMplsLdpCrlspTnlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlFrequency.setStatus("current")


class _HpnicfMplsLdpCrlspTnlWeight_Type(Integer32):
    """Custom type hpnicfMplsLdpCrlspTnlWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfMplsLdpCrlspTnlWeight_Type.__name__ = "Integer32"
_HpnicfMplsLdpCrlspTnlWeight_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlWeight = _HpnicfMplsLdpCrlspTnlWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 14),
    _HpnicfMplsLdpCrlspTnlWeight_Type()
)
hpnicfMplsLdpCrlspTnlWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlWeight.setStatus("current")
_HpnicfMplsLdpCrlspTnlRowStatus_Type = RowStatus
_HpnicfMplsLdpCrlspTnlRowStatus_Object = MibTableColumn
hpnicfMplsLdpCrlspTnlRowStatus = _HpnicfMplsLdpCrlspTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 1, 1, 15),
    _HpnicfMplsLdpCrlspTnlRowStatus_Type()
)
hpnicfMplsLdpCrlspTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTnlRowStatus.setStatus("current")
_HpnicfMplsLdpCrlspErHopTable_Object = MibTable
hpnicfMplsLdpCrlspErHopTable = _HpnicfMplsLdpCrlspErHopTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspErHopTable.setStatus("current")
_HpnicfMplsLdpCrlspErHopEntry_Object = MibTableRow
hpnicfMplsLdpCrlspErHopEntry = _HpnicfMplsLdpCrlspErHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 2, 1)
)
hpnicfMplsLdpCrlspErHopEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpCrlspTnlIndex"),
    (0, "HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpCrlspErHopIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspErHopEntry.setStatus("current")
_HpnicfMplsLdpCrlspErHopIndex_Type = Integer32
_HpnicfMplsLdpCrlspErHopIndex_Object = MibTableColumn
hpnicfMplsLdpCrlspErHopIndex = _HpnicfMplsLdpCrlspErHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 2, 1, 1),
    _HpnicfMplsLdpCrlspErHopIndex_Type()
)
hpnicfMplsLdpCrlspErHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspErHopIndex.setStatus("current")


class _HpnicfMplsLdpCrlspErHopAddrType_Type(Integer32):
    """Custom type hpnicfMplsLdpCrlspErHopAddrType based on Integer32"""
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


_HpnicfMplsLdpCrlspErHopAddrType_Type.__name__ = "Integer32"
_HpnicfMplsLdpCrlspErHopAddrType_Object = MibTableColumn
hpnicfMplsLdpCrlspErHopAddrType = _HpnicfMplsLdpCrlspErHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 2, 1, 2),
    _HpnicfMplsLdpCrlspErHopAddrType_Type()
)
hpnicfMplsLdpCrlspErHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspErHopAddrType.setStatus("current")
_HpnicfMplsLdpCrlspErHopIpv4Addr_Type = IpAddress
_HpnicfMplsLdpCrlspErHopIpv4Addr_Object = MibTableColumn
hpnicfMplsLdpCrlspErHopIpv4Addr = _HpnicfMplsLdpCrlspErHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 2, 1, 3),
    _HpnicfMplsLdpCrlspErHopIpv4Addr_Type()
)
hpnicfMplsLdpCrlspErHopIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspErHopIpv4Addr.setStatus("current")


class _HpnicfMplsLdpCrlspErHopIpv4PrefixLen_Type(Integer32):
    """Custom type hpnicfMplsLdpCrlspErHopIpv4PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HpnicfMplsLdpCrlspErHopIpv4PrefixLen_Type.__name__ = "Integer32"
_HpnicfMplsLdpCrlspErHopIpv4PrefixLen_Object = MibTableColumn
hpnicfMplsLdpCrlspErHopIpv4PrefixLen = _HpnicfMplsLdpCrlspErHopIpv4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 2, 1, 4),
    _HpnicfMplsLdpCrlspErHopIpv4PrefixLen_Type()
)
hpnicfMplsLdpCrlspErHopIpv4PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspErHopIpv4PrefixLen.setStatus("current")


class _HpnicfMplsLdpCrlspErHopStrictOrLoose_Type(Integer32):
    """Custom type hpnicfMplsLdpCrlspErHopStrictOrLoose based on Integer32"""
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


_HpnicfMplsLdpCrlspErHopStrictOrLoose_Type.__name__ = "Integer32"
_HpnicfMplsLdpCrlspErHopStrictOrLoose_Object = MibTableColumn
hpnicfMplsLdpCrlspErHopStrictOrLoose = _HpnicfMplsLdpCrlspErHopStrictOrLoose_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 2, 1, 5),
    _HpnicfMplsLdpCrlspErHopStrictOrLoose_Type()
)
hpnicfMplsLdpCrlspErHopStrictOrLoose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspErHopStrictOrLoose.setStatus("current")
_HpnicfMplsLdpCrlspErHopRowStatus_Type = RowStatus
_HpnicfMplsLdpCrlspErHopRowStatus_Object = MibTableColumn
hpnicfMplsLdpCrlspErHopRowStatus = _HpnicfMplsLdpCrlspErHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 1, 6, 2, 1, 6),
    _HpnicfMplsLdpCrlspErHopRowStatus_Type()
)
hpnicfMplsLdpCrlspErHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspErHopRowStatus.setStatus("current")
_HpnicfMplsLdpNotifications_ObjectIdentity = ObjectIdentity
hpnicfMplsLdpNotifications = _HpnicfMplsLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 2)
)
_HpnicfMplsLdpNotificationPrefix_ObjectIdentity = ObjectIdentity
hpnicfMplsLdpNotificationPrefix = _HpnicfMplsLdpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 2, 0)
)
hpnicfMplsLdpEntityEntry.registerAugmentions(
    ("HPN-ICF-MPLS-LDP-MIB",
     "hpnicfMplsLdpEntityStatsEntry")
)
hpnicfMplsLdpEntityStatsEntry.setIndexNames(*hpnicfMplsLdpEntityEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hpnicfMplsLdpFailedInitSessionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 2, 0, 1)
)
hpnicfMplsLdpFailedInitSessionThresholdExceeded.setObjects(
      *(("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
        ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityID"),
        ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityFailedInitSessionThreshold"))
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpFailedInitSessionThresholdExceeded.setStatus(
        "current"
    )

hpnicfMplsLdpCrlspTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 2, 0, 2)
)
hpnicfMplsLdpCrlspTunnelUp.setObjects(
      *(("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
        ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityID"),
        ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpCrlspTnlIndex"))
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTunnelUp.setStatus(
        "current"
    )

hpnicfMplsLdpCrlspTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 2, 0, 3)
)
hpnicfMplsLdpCrlspTunnelDown.setObjects(
      *(("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
        ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityID"),
        ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpCrlspTnlIndex"))
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTunnelDown.setStatus(
        "current"
    )

hpnicfMplsLdpCrlspTunnelSetupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 2, 0, 4)
)
hpnicfMplsLdpCrlspTunnelSetupFailure.setObjects(
      *(("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
        ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityID"),
        ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpCrlspTnlIndex"))
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpCrlspTunnelSetupFailure.setStatus(
        "current"
    )

hpnicfMplsLdpIncarnUpEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 2, 0, 11)
)
hpnicfMplsLdpIncarnUpEventFailure.setObjects(
    ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID")
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpIncarnUpEventFailure.setStatus(
        "current"
    )

hpnicfMplsLdpIncarnDownEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 2, 0, 12)
)
hpnicfMplsLdpIncarnDownEventFailure.setObjects(
    ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID")
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpIncarnDownEventFailure.setStatus(
        "current"
    )

hpnicfMplsLdpEntityUpEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 2, 0, 13)
)
hpnicfMplsLdpEntityUpEventFailure.setObjects(
      *(("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
        ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityID"))
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityUpEventFailure.setStatus(
        "current"
    )

hpnicfMplsLdpEntityDownEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 2, 0, 14)
)
hpnicfMplsLdpEntityDownEventFailure.setObjects(
      *(("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpLsrIncarnID"),
        ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpEntityID"))
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpEntityDownEventFailure.setStatus(
        "current"
    )

hpnicfMplsLdpSessionUpEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 2, 0, 15)
)
hpnicfMplsLdpSessionUpEventFailure.setObjects(
      *(("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpSessionID"),
        ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpSessionState"))
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionUpEventFailure.setStatus(
        "current"
    )

hpnicfMplsLdpSessionDownEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2, 2, 0, 16)
)
hpnicfMplsLdpSessionDownEventFailure.setObjects(
      *(("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpSessionID"),
        ("HPN-ICF-MPLS-LDP-MIB", "hpnicfMplsLdpSessionState"))
)
if mibBuilder.loadTexts:
    hpnicfMplsLdpSessionDownEventFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MPLS-LDP-MIB",
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
       "hpnicfMplsLdp": hpnicfMplsLdp,
       "hpnicfMplsLdpObjects": hpnicfMplsLdpObjects,
       "hpnicfMplsLdpLsrObjects": hpnicfMplsLdpLsrObjects,
       "hpnicfMplsLdpLsrIncarnTable": hpnicfMplsLdpLsrIncarnTable,
       "hpnicfMplsLdpLsrIncarnEntry": hpnicfMplsLdpLsrIncarnEntry,
       "hpnicfMplsLdpLsrID": hpnicfMplsLdpLsrID,
       "hpnicfMplsLdpLsrLoopDetectionPresent": hpnicfMplsLdpLsrLoopDetectionPresent,
       "hpnicfMplsLdpLsrLoopDetectionAdminStatus": hpnicfMplsLdpLsrLoopDetectionAdminStatus,
       "hpnicfMplsLdpLsrPathVectorLimit": hpnicfMplsLdpLsrPathVectorLimit,
       "hpnicfMplsLdpLsrHopCountLimit": hpnicfMplsLdpLsrHopCountLimit,
       "hpnicfMplsLdpLsrLoopPreventionPresent": hpnicfMplsLdpLsrLoopPreventionPresent,
       "hpnicfMplsLdpLsrLoopPreventionAdminStatus": hpnicfMplsLdpLsrLoopPreventionAdminStatus,
       "hpnicfMplsLdpLsrLabelRetentionMode": hpnicfMplsLdpLsrLabelRetentionMode,
       "hpnicfMplsLdpLsrIncarnID": hpnicfMplsLdpLsrIncarnID,
       "hpnicfMplsLdpLsrMaxLdpEntities": hpnicfMplsLdpLsrMaxLdpEntities,
       "hpnicfMplsLdpLsrMaxLocalPeers": hpnicfMplsLdpLsrMaxLocalPeers,
       "hpnicfMplsLdpLsrMaxRemotePeers": hpnicfMplsLdpLsrMaxRemotePeers,
       "hpnicfMplsLdpLsrMaxIfaces": hpnicfMplsLdpLsrMaxIfaces,
       "hpnicfMplsLdpLsrMaxLsps": hpnicfMplsLdpLsrMaxLsps,
       "hpnicfMplsLdpLsrMaxCrlspTnls": hpnicfMplsLdpLsrMaxCrlspTnls,
       "hpnicfMplsLdpLsrMaxErhopPerCrlspTnl": hpnicfMplsLdpLsrMaxErhopPerCrlspTnl,
       "hpnicfMplsLdpLsrRowStatus": hpnicfMplsLdpLsrRowStatus,
       "hpnicfMplsLdpLsrMaxVcmCapability": hpnicfMplsLdpLsrMaxVcmCapability,
       "hpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent": hpnicfMplsLdpLsrVcmPathVecInAllLblMapPresent,
       "hpnicfMplsLdpLsrRequestRetrytimerValue": hpnicfMplsLdpLsrRequestRetrytimerValue,
       "hpnicfMplsLdpLsrNumOfRequestRetryAttempts": hpnicfMplsLdpLsrNumOfRequestRetryAttempts,
       "hpnicfMplsLdpEntityObjects": hpnicfMplsLdpEntityObjects,
       "hpnicfMplsLdpEntityTable": hpnicfMplsLdpEntityTable,
       "hpnicfMplsLdpEntityEntry": hpnicfMplsLdpEntityEntry,
       "hpnicfMplsLdpEntityID": hpnicfMplsLdpEntityID,
       "hpnicfMplsLdpEntityLabelSpaceType": hpnicfMplsLdpEntityLabelSpaceType,
       "hpnicfMplsLdpEntityDefVpi": hpnicfMplsLdpEntityDefVpi,
       "hpnicfMplsLdpEntityDefVci": hpnicfMplsLdpEntityDefVci,
       "hpnicfMplsLdpEntityUnlabTrafVpi": hpnicfMplsLdpEntityUnlabTrafVpi,
       "hpnicfMplsLdpEntityUnlabTrafVci": hpnicfMplsLdpEntityUnlabTrafVci,
       "hpnicfMplsLdpEntityMergeCapability": hpnicfMplsLdpEntityMergeCapability,
       "hpnicfMplsLdpEntityVcDirectionality": hpnicfMplsLdpEntityVcDirectionality,
       "hpnicfMplsLdpEntityWellKnownDiscoveryPort": hpnicfMplsLdpEntityWellKnownDiscoveryPort,
       "hpnicfMplsLdpEntityMtu": hpnicfMplsLdpEntityMtu,
       "hpnicfMplsLdpEntityKeepAliveHoldTimer": hpnicfMplsLdpEntityKeepAliveHoldTimer,
       "hpnicfMplsLdpEntityFailedInitSessionThreshold": hpnicfMplsLdpEntityFailedInitSessionThreshold,
       "hpnicfMplsLdpEntityLabelDistributionMethod": hpnicfMplsLdpEntityLabelDistributionMethod,
       "hpnicfMplsLdpEntityLabelAllocationMethod": hpnicfMplsLdpEntityLabelAllocationMethod,
       "hpnicfMplsLdpEntityHelloHoldTimer": hpnicfMplsLdpEntityHelloHoldTimer,
       "hpnicfMplsLdpEntityRowStatus": hpnicfMplsLdpEntityRowStatus,
       "hpnicfMplsLdpEntityIfTable": hpnicfMplsLdpEntityIfTable,
       "hpnicfMplsLdpEntityIfEntry": hpnicfMplsLdpEntityIfEntry,
       "hpnicfMplsLdpEntityIfIndex": hpnicfMplsLdpEntityIfIndex,
       "hpnicfMplsLdpEntityIfIpv4Address": hpnicfMplsLdpEntityIfIpv4Address,
       "hpnicfMplsLdpEntityIfRowStatus": hpnicfMplsLdpEntityIfRowStatus,
       "hpnicfMplsLdpEntityConfAtmLabelRangeTable": hpnicfMplsLdpEntityConfAtmLabelRangeTable,
       "hpnicfMplsLdpEntityConfAtmLabelRangeEntry": hpnicfMplsLdpEntityConfAtmLabelRangeEntry,
       "hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI": hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVPI,
       "hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI": hpnicfMplsLdpEntityConfAtmLabelRangeLowerBoundVCI,
       "hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI": hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVPI,
       "hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI": hpnicfMplsLdpEntityConfAtmLabelRangeUpperBoundVCI,
       "hpnicfMplsLdpEntityConfAtmLabelRangeRowStatus": hpnicfMplsLdpEntityConfAtmLabelRangeRowStatus,
       "hpnicfMplsLdpEntityStatsTable": hpnicfMplsLdpEntityStatsTable,
       "hpnicfMplsLdpEntityStatsEntry": hpnicfMplsLdpEntityStatsEntry,
       "hpnicfMplsLdpAttemptedSessions": hpnicfMplsLdpAttemptedSessions,
       "hpnicfMplsLdpPeerObjects": hpnicfMplsLdpPeerObjects,
       "hpnicfMplsLdpPeerTable": hpnicfMplsLdpPeerTable,
       "hpnicfMplsLdpPeerEntry": hpnicfMplsLdpPeerEntry,
       "hpnicfMplsLdpPeerIndex": hpnicfMplsLdpPeerIndex,
       "hpnicfMplsLdpPeerID": hpnicfMplsLdpPeerID,
       "hpnicfMplsLdpPeerInternetworkAddrType": hpnicfMplsLdpPeerInternetworkAddrType,
       "hpnicfMplsLdpPeerInternetworkAddr": hpnicfMplsLdpPeerInternetworkAddr,
       "hpnicfMplsLdpPeerDefaultMtu": hpnicfMplsLdpPeerDefaultMtu,
       "hpnicfMplsLdpPeerKeepAliveHoldTimer": hpnicfMplsLdpPeerKeepAliveHoldTimer,
       "hpnicfMplsLdpPeerLabelDistributionMethod": hpnicfMplsLdpPeerLabelDistributionMethod,
       "hpnicfMplsLdpPeerType": hpnicfMplsLdpPeerType,
       "hpnicfMplsLdpPeerRowStatus": hpnicfMplsLdpPeerRowStatus,
       "hpnicfMplsLdpPeerConfAtmLabelRangeTable": hpnicfMplsLdpPeerConfAtmLabelRangeTable,
       "hpnicfMplsLdpPeerConfAtmLabelRangeEntry": hpnicfMplsLdpPeerConfAtmLabelRangeEntry,
       "hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI": hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVPI,
       "hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI": hpnicfMplsLdpPeerConfAtmLabelRangeLowerBoundVCI,
       "hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI": hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVPI,
       "hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI": hpnicfMplsLdpPeerConfAtmLabelRangeUpperBoundVCI,
       "hpnicfMplsLdpSessionObjects": hpnicfMplsLdpSessionObjects,
       "hpnicfMplsLdpSessionTable": hpnicfMplsLdpSessionTable,
       "hpnicfMplsLdpSessionEntry": hpnicfMplsLdpSessionEntry,
       "hpnicfMplsLdpSessionIndex": hpnicfMplsLdpSessionIndex,
       "hpnicfMplsLdpSessionID": hpnicfMplsLdpSessionID,
       "hpnicfMplsLdpSessionProtocolVersion": hpnicfMplsLdpSessionProtocolVersion,
       "hpnicfMplsLdpSessionKeepAliveHoldTimeRemaining": hpnicfMplsLdpSessionKeepAliveHoldTimeRemaining,
       "hpnicfMplsLdpSessionRole": hpnicfMplsLdpSessionRole,
       "hpnicfMplsLdpSessionState": hpnicfMplsLdpSessionState,
       "hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI": hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVPI,
       "hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI": hpnicfMplsLdpSessionAtmLabelRangeLowerBoundVCI,
       "hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI": hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVPI,
       "hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI": hpnicfMplsLdpSessionAtmLabelRangeUpperBoundVCI,
       "hpnicfMplsLdpHelloAdjacencyObjects": hpnicfMplsLdpHelloAdjacencyObjects,
       "hpnicfMplsLdpHelloAdjacencyTable": hpnicfMplsLdpHelloAdjacencyTable,
       "hpnicfMplsLdpHelloAdjacencyEntry": hpnicfMplsLdpHelloAdjacencyEntry,
       "hpnicfMplsLdpHelloAdjacencyIndex": hpnicfMplsLdpHelloAdjacencyIndex,
       "hpnicfMplsLdpHelloAdjacencyHoldTimeRemaining": hpnicfMplsLdpHelloAdjacencyHoldTimeRemaining,
       "hpnicfMplsLdpCrlspTnlObjects": hpnicfMplsLdpCrlspTnlObjects,
       "hpnicfMplsLdpCrlspTnlTable": hpnicfMplsLdpCrlspTnlTable,
       "hpnicfMplsLdpCrlspTnlEntry": hpnicfMplsLdpCrlspTnlEntry,
       "hpnicfMplsLdpCrlspTnlIndex": hpnicfMplsLdpCrlspTnlIndex,
       "hpnicfMplsLdpCrlspTnlName": hpnicfMplsLdpCrlspTnlName,
       "hpnicfMplsLdpCrlspTnlDirection": hpnicfMplsLdpCrlspTnlDirection,
       "hpnicfMplsLdpCrlspTnlSignallingProto": hpnicfMplsLdpCrlspTnlSignallingProto,
       "hpnicfMplsLdpCrlspTnlSetupPrio": hpnicfMplsLdpCrlspTnlSetupPrio,
       "hpnicfMplsLdpCrlspTnlHoldingPrio": hpnicfMplsLdpCrlspTnlHoldingPrio,
       "hpnicfMplsLdpCrlspTnlPeakDataRate": hpnicfMplsLdpCrlspTnlPeakDataRate,
       "hpnicfMplsLdpCrlspTnlPeakBurstSize": hpnicfMplsLdpCrlspTnlPeakBurstSize,
       "hpnicfMplsLdpCrlspTnlCommittedDataRate": hpnicfMplsLdpCrlspTnlCommittedDataRate,
       "hpnicfMplsLdpCrlspTnlCommittedBurstSize": hpnicfMplsLdpCrlspTnlCommittedBurstSize,
       "hpnicfMplsLdpCrlspTnlExcessBurstSize": hpnicfMplsLdpCrlspTnlExcessBurstSize,
       "hpnicfMplsLdpCrlspTnlIsPinned": hpnicfMplsLdpCrlspTnlIsPinned,
       "hpnicfMplsLdpCrlspTnlFrequency": hpnicfMplsLdpCrlspTnlFrequency,
       "hpnicfMplsLdpCrlspTnlWeight": hpnicfMplsLdpCrlspTnlWeight,
       "hpnicfMplsLdpCrlspTnlRowStatus": hpnicfMplsLdpCrlspTnlRowStatus,
       "hpnicfMplsLdpCrlspErHopTable": hpnicfMplsLdpCrlspErHopTable,
       "hpnicfMplsLdpCrlspErHopEntry": hpnicfMplsLdpCrlspErHopEntry,
       "hpnicfMplsLdpCrlspErHopIndex": hpnicfMplsLdpCrlspErHopIndex,
       "hpnicfMplsLdpCrlspErHopAddrType": hpnicfMplsLdpCrlspErHopAddrType,
       "hpnicfMplsLdpCrlspErHopIpv4Addr": hpnicfMplsLdpCrlspErHopIpv4Addr,
       "hpnicfMplsLdpCrlspErHopIpv4PrefixLen": hpnicfMplsLdpCrlspErHopIpv4PrefixLen,
       "hpnicfMplsLdpCrlspErHopStrictOrLoose": hpnicfMplsLdpCrlspErHopStrictOrLoose,
       "hpnicfMplsLdpCrlspErHopRowStatus": hpnicfMplsLdpCrlspErHopRowStatus,
       "hpnicfMplsLdpNotifications": hpnicfMplsLdpNotifications,
       "hpnicfMplsLdpNotificationPrefix": hpnicfMplsLdpNotificationPrefix,
       "hpnicfMplsLdpFailedInitSessionThresholdExceeded": hpnicfMplsLdpFailedInitSessionThresholdExceeded,
       "hpnicfMplsLdpCrlspTunnelUp": hpnicfMplsLdpCrlspTunnelUp,
       "hpnicfMplsLdpCrlspTunnelDown": hpnicfMplsLdpCrlspTunnelDown,
       "hpnicfMplsLdpCrlspTunnelSetupFailure": hpnicfMplsLdpCrlspTunnelSetupFailure,
       "hpnicfMplsLdpIncarnUpEventFailure": hpnicfMplsLdpIncarnUpEventFailure,
       "hpnicfMplsLdpIncarnDownEventFailure": hpnicfMplsLdpIncarnDownEventFailure,
       "hpnicfMplsLdpEntityUpEventFailure": hpnicfMplsLdpEntityUpEventFailure,
       "hpnicfMplsLdpEntityDownEventFailure": hpnicfMplsLdpEntityDownEventFailure,
       "hpnicfMplsLdpSessionUpEventFailure": hpnicfMplsLdpSessionUpEventFailure,
       "hpnicfMplsLdpSessionDownEventFailure": hpnicfMplsLdpSessionDownEventFailure}
)
