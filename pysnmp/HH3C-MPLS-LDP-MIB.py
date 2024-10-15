# SNMP MIB module (HH3C-MPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MPLS-LDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:10 2024
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

(hh3cMpls,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cMpls")

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

hh3cMplsLdp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2)
)
hh3cMplsLdp.setRevisions(
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

_Hh3cMplsLdpObjects_ObjectIdentity = ObjectIdentity
hh3cMplsLdpObjects = _Hh3cMplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1)
)
_Hh3cMplsLdpLsrObjects_ObjectIdentity = ObjectIdentity
hh3cMplsLdpLsrObjects = _Hh3cMplsLdpLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1)
)
_Hh3cMplsLdpLsrIncarnTable_Object = MibTable
hh3cMplsLdpLsrIncarnTable = _Hh3cMplsLdpLsrIncarnTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrIncarnTable.setStatus("current")
_Hh3cMplsLdpLsrIncarnEntry_Object = MibTableRow
hh3cMplsLdpLsrIncarnEntry = _Hh3cMplsLdpLsrIncarnEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1)
)
hh3cMplsLdpLsrIncarnEntry.setIndexNames(
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
)
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrIncarnEntry.setStatus("current")
_Hh3cMplsLdpLsrID_Type = MplsLsrIdentifier
_Hh3cMplsLdpLsrID_Object = MibTableColumn
hh3cMplsLdpLsrID = _Hh3cMplsLdpLsrID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 1),
    _Hh3cMplsLdpLsrID_Type()
)
hh3cMplsLdpLsrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrID.setStatus("current")


class _Hh3cMplsLdpLsrLoopDetectionPresent_Type(TruthValue):
    """Custom type hh3cMplsLdpLsrLoopDetectionPresent based on TruthValue"""


_Hh3cMplsLdpLsrLoopDetectionPresent_Object = MibTableColumn
hh3cMplsLdpLsrLoopDetectionPresent = _Hh3cMplsLdpLsrLoopDetectionPresent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 2),
    _Hh3cMplsLdpLsrLoopDetectionPresent_Type()
)
hh3cMplsLdpLsrLoopDetectionPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrLoopDetectionPresent.setStatus("current")


class _Hh3cMplsLdpLsrLoopDetectionAdminStatus_Type(Integer32):
    """Custom type hh3cMplsLdpLsrLoopDetectionAdminStatus based on Integer32"""
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


_Hh3cMplsLdpLsrLoopDetectionAdminStatus_Type.__name__ = "Integer32"
_Hh3cMplsLdpLsrLoopDetectionAdminStatus_Object = MibTableColumn
hh3cMplsLdpLsrLoopDetectionAdminStatus = _Hh3cMplsLdpLsrLoopDetectionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 3),
    _Hh3cMplsLdpLsrLoopDetectionAdminStatus_Type()
)
hh3cMplsLdpLsrLoopDetectionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrLoopDetectionAdminStatus.setStatus("current")


class _Hh3cMplsLdpLsrPathVectorLimit_Type(Integer32):
    """Custom type hh3cMplsLdpLsrPathVectorLimit based on Integer32"""
    defaultValue = 32


_Hh3cMplsLdpLsrPathVectorLimit_Object = MibTableColumn
hh3cMplsLdpLsrPathVectorLimit = _Hh3cMplsLdpLsrPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 4),
    _Hh3cMplsLdpLsrPathVectorLimit_Type()
)
hh3cMplsLdpLsrPathVectorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrPathVectorLimit.setStatus("current")


class _Hh3cMplsLdpLsrHopCountLimit_Type(Integer32):
    """Custom type hh3cMplsLdpLsrHopCountLimit based on Integer32"""
    defaultValue = 32


_Hh3cMplsLdpLsrHopCountLimit_Object = MibTableColumn
hh3cMplsLdpLsrHopCountLimit = _Hh3cMplsLdpLsrHopCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 5),
    _Hh3cMplsLdpLsrHopCountLimit_Type()
)
hh3cMplsLdpLsrHopCountLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrHopCountLimit.setStatus("current")


class _Hh3cMplsLdpLsrLoopPreventionPresent_Type(TruthValue):
    """Custom type hh3cMplsLdpLsrLoopPreventionPresent based on TruthValue"""


_Hh3cMplsLdpLsrLoopPreventionPresent_Object = MibTableColumn
hh3cMplsLdpLsrLoopPreventionPresent = _Hh3cMplsLdpLsrLoopPreventionPresent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 6),
    _Hh3cMplsLdpLsrLoopPreventionPresent_Type()
)
hh3cMplsLdpLsrLoopPreventionPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrLoopPreventionPresent.setStatus("current")


class _Hh3cMplsLdpLsrLoopPreventionAdminStatus_Type(Integer32):
    """Custom type hh3cMplsLdpLsrLoopPreventionAdminStatus based on Integer32"""
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


_Hh3cMplsLdpLsrLoopPreventionAdminStatus_Type.__name__ = "Integer32"
_Hh3cMplsLdpLsrLoopPreventionAdminStatus_Object = MibTableColumn
hh3cMplsLdpLsrLoopPreventionAdminStatus = _Hh3cMplsLdpLsrLoopPreventionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 7),
    _Hh3cMplsLdpLsrLoopPreventionAdminStatus_Type()
)
hh3cMplsLdpLsrLoopPreventionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrLoopPreventionAdminStatus.setStatus("current")


class _Hh3cMplsLdpLsrLabelRetentionMode_Type(Integer32):
    """Custom type hh3cMplsLdpLsrLabelRetentionMode based on Integer32"""
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


_Hh3cMplsLdpLsrLabelRetentionMode_Type.__name__ = "Integer32"
_Hh3cMplsLdpLsrLabelRetentionMode_Object = MibTableColumn
hh3cMplsLdpLsrLabelRetentionMode = _Hh3cMplsLdpLsrLabelRetentionMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 8),
    _Hh3cMplsLdpLsrLabelRetentionMode_Type()
)
hh3cMplsLdpLsrLabelRetentionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrLabelRetentionMode.setStatus("current")
_Hh3cMplsLdpLsrIncarnID_Type = Integer32
_Hh3cMplsLdpLsrIncarnID_Object = MibTableColumn
hh3cMplsLdpLsrIncarnID = _Hh3cMplsLdpLsrIncarnID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 9),
    _Hh3cMplsLdpLsrIncarnID_Type()
)
hh3cMplsLdpLsrIncarnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrIncarnID.setStatus("current")


class _Hh3cMplsLdpLsrMaxLdpEntities_Type(Integer32):
    """Custom type hh3cMplsLdpLsrMaxLdpEntities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cMplsLdpLsrMaxLdpEntities_Type.__name__ = "Integer32"
_Hh3cMplsLdpLsrMaxLdpEntities_Object = MibTableColumn
hh3cMplsLdpLsrMaxLdpEntities = _Hh3cMplsLdpLsrMaxLdpEntities_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 10),
    _Hh3cMplsLdpLsrMaxLdpEntities_Type()
)
hh3cMplsLdpLsrMaxLdpEntities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrMaxLdpEntities.setStatus("current")


class _Hh3cMplsLdpLsrMaxLocalPeers_Type(Integer32):
    """Custom type hh3cMplsLdpLsrMaxLocalPeers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cMplsLdpLsrMaxLocalPeers_Type.__name__ = "Integer32"
_Hh3cMplsLdpLsrMaxLocalPeers_Object = MibTableColumn
hh3cMplsLdpLsrMaxLocalPeers = _Hh3cMplsLdpLsrMaxLocalPeers_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 11),
    _Hh3cMplsLdpLsrMaxLocalPeers_Type()
)
hh3cMplsLdpLsrMaxLocalPeers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrMaxLocalPeers.setStatus("current")


class _Hh3cMplsLdpLsrMaxRemotePeers_Type(Integer32):
    """Custom type hh3cMplsLdpLsrMaxRemotePeers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cMplsLdpLsrMaxRemotePeers_Type.__name__ = "Integer32"
_Hh3cMplsLdpLsrMaxRemotePeers_Object = MibTableColumn
hh3cMplsLdpLsrMaxRemotePeers = _Hh3cMplsLdpLsrMaxRemotePeers_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 12),
    _Hh3cMplsLdpLsrMaxRemotePeers_Type()
)
hh3cMplsLdpLsrMaxRemotePeers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrMaxRemotePeers.setStatus("current")
_Hh3cMplsLdpLsrMaxIfaces_Type = Integer32
_Hh3cMplsLdpLsrMaxIfaces_Object = MibTableColumn
hh3cMplsLdpLsrMaxIfaces = _Hh3cMplsLdpLsrMaxIfaces_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 13),
    _Hh3cMplsLdpLsrMaxIfaces_Type()
)
hh3cMplsLdpLsrMaxIfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrMaxIfaces.setStatus("current")
_Hh3cMplsLdpLsrMaxLsps_Type = Integer32
_Hh3cMplsLdpLsrMaxLsps_Object = MibTableColumn
hh3cMplsLdpLsrMaxLsps = _Hh3cMplsLdpLsrMaxLsps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 14),
    _Hh3cMplsLdpLsrMaxLsps_Type()
)
hh3cMplsLdpLsrMaxLsps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrMaxLsps.setStatus("current")
_Hh3cMplsLdpLsrMaxCrlspTnls_Type = Integer32
_Hh3cMplsLdpLsrMaxCrlspTnls_Object = MibTableColumn
hh3cMplsLdpLsrMaxCrlspTnls = _Hh3cMplsLdpLsrMaxCrlspTnls_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 15),
    _Hh3cMplsLdpLsrMaxCrlspTnls_Type()
)
hh3cMplsLdpLsrMaxCrlspTnls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrMaxCrlspTnls.setStatus("current")
_Hh3cMplsLdpLsrMaxErhopPerCrlspTnl_Type = Integer32
_Hh3cMplsLdpLsrMaxErhopPerCrlspTnl_Object = MibTableColumn
hh3cMplsLdpLsrMaxErhopPerCrlspTnl = _Hh3cMplsLdpLsrMaxErhopPerCrlspTnl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 16),
    _Hh3cMplsLdpLsrMaxErhopPerCrlspTnl_Type()
)
hh3cMplsLdpLsrMaxErhopPerCrlspTnl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrMaxErhopPerCrlspTnl.setStatus("current")
_Hh3cMplsLdpLsrRowStatus_Type = RowStatus
_Hh3cMplsLdpLsrRowStatus_Object = MibTableColumn
hh3cMplsLdpLsrRowStatus = _Hh3cMplsLdpLsrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 17),
    _Hh3cMplsLdpLsrRowStatus_Type()
)
hh3cMplsLdpLsrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrRowStatus.setStatus("current")
_Hh3cMplsLdpLsrMaxVcmCapability_Type = Integer32
_Hh3cMplsLdpLsrMaxVcmCapability_Object = MibTableColumn
hh3cMplsLdpLsrMaxVcmCapability = _Hh3cMplsLdpLsrMaxVcmCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 18),
    _Hh3cMplsLdpLsrMaxVcmCapability_Type()
)
hh3cMplsLdpLsrMaxVcmCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrMaxVcmCapability.setStatus("current")
_Hh3cMplsLdpLsrVcmPathVecInAllLblMapPresent_Type = TruthValue
_Hh3cMplsLdpLsrVcmPathVecInAllLblMapPresent_Object = MibTableColumn
hh3cMplsLdpLsrVcmPathVecInAllLblMapPresent = _Hh3cMplsLdpLsrVcmPathVecInAllLblMapPresent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 19),
    _Hh3cMplsLdpLsrVcmPathVecInAllLblMapPresent_Type()
)
hh3cMplsLdpLsrVcmPathVecInAllLblMapPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrVcmPathVecInAllLblMapPresent.setStatus("current")
_Hh3cMplsLdpLsrRequestRetrytimerValue_Type = Integer32
_Hh3cMplsLdpLsrRequestRetrytimerValue_Object = MibTableColumn
hh3cMplsLdpLsrRequestRetrytimerValue = _Hh3cMplsLdpLsrRequestRetrytimerValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 20),
    _Hh3cMplsLdpLsrRequestRetrytimerValue_Type()
)
hh3cMplsLdpLsrRequestRetrytimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrRequestRetrytimerValue.setStatus("current")
_Hh3cMplsLdpLsrNumOfRequestRetryAttempts_Type = Integer32
_Hh3cMplsLdpLsrNumOfRequestRetryAttempts_Object = MibTableColumn
hh3cMplsLdpLsrNumOfRequestRetryAttempts = _Hh3cMplsLdpLsrNumOfRequestRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 1, 1, 1, 21),
    _Hh3cMplsLdpLsrNumOfRequestRetryAttempts_Type()
)
hh3cMplsLdpLsrNumOfRequestRetryAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsLdpLsrNumOfRequestRetryAttempts.setStatus("current")
_Hh3cMplsLdpEntityObjects_ObjectIdentity = ObjectIdentity
hh3cMplsLdpEntityObjects = _Hh3cMplsLdpEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2)
)
_Hh3cMplsLdpEntityTable_Object = MibTable
hh3cMplsLdpEntityTable = _Hh3cMplsLdpEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityTable.setStatus("current")
_Hh3cMplsLdpEntityEntry_Object = MibTableRow
hh3cMplsLdpEntityEntry = _Hh3cMplsLdpEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1)
)
hh3cMplsLdpEntityEntry.setIndexNames(
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityEntry.setStatus("current")
_Hh3cMplsLdpEntityID_Type = MplsLdpIdentifier
_Hh3cMplsLdpEntityID_Object = MibTableColumn
hh3cMplsLdpEntityID = _Hh3cMplsLdpEntityID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 1),
    _Hh3cMplsLdpEntityID_Type()
)
hh3cMplsLdpEntityID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityID.setStatus("current")


class _Hh3cMplsLdpEntityLabelSpaceType_Type(Integer32):
    """Custom type hh3cMplsLdpEntityLabelSpaceType based on Integer32"""
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


_Hh3cMplsLdpEntityLabelSpaceType_Type.__name__ = "Integer32"
_Hh3cMplsLdpEntityLabelSpaceType_Object = MibTableColumn
hh3cMplsLdpEntityLabelSpaceType = _Hh3cMplsLdpEntityLabelSpaceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 2),
    _Hh3cMplsLdpEntityLabelSpaceType_Type()
)
hh3cMplsLdpEntityLabelSpaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityLabelSpaceType.setStatus("current")
_Hh3cMplsLdpEntityDefVpi_Type = AtmVpIdentifier
_Hh3cMplsLdpEntityDefVpi_Object = MibTableColumn
hh3cMplsLdpEntityDefVpi = _Hh3cMplsLdpEntityDefVpi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 3),
    _Hh3cMplsLdpEntityDefVpi_Type()
)
hh3cMplsLdpEntityDefVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityDefVpi.setStatus("current")
_Hh3cMplsLdpEntityDefVci_Type = AtmVcIdentifier
_Hh3cMplsLdpEntityDefVci_Object = MibTableColumn
hh3cMplsLdpEntityDefVci = _Hh3cMplsLdpEntityDefVci_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 4),
    _Hh3cMplsLdpEntityDefVci_Type()
)
hh3cMplsLdpEntityDefVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityDefVci.setStatus("current")


class _Hh3cMplsLdpEntityUnlabTrafVpi_Type(AtmVpIdentifier):
    """Custom type hh3cMplsLdpEntityUnlabTrafVpi based on AtmVpIdentifier"""
    defaultValue = 0


_Hh3cMplsLdpEntityUnlabTrafVpi_Object = MibTableColumn
hh3cMplsLdpEntityUnlabTrafVpi = _Hh3cMplsLdpEntityUnlabTrafVpi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 5),
    _Hh3cMplsLdpEntityUnlabTrafVpi_Type()
)
hh3cMplsLdpEntityUnlabTrafVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityUnlabTrafVpi.setStatus("current")


class _Hh3cMplsLdpEntityUnlabTrafVci_Type(AtmVcIdentifier):
    """Custom type hh3cMplsLdpEntityUnlabTrafVci based on AtmVcIdentifier"""
    defaultValue = 32


_Hh3cMplsLdpEntityUnlabTrafVci_Object = MibTableColumn
hh3cMplsLdpEntityUnlabTrafVci = _Hh3cMplsLdpEntityUnlabTrafVci_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 6),
    _Hh3cMplsLdpEntityUnlabTrafVci_Type()
)
hh3cMplsLdpEntityUnlabTrafVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityUnlabTrafVci.setStatus("current")


class _Hh3cMplsLdpEntityMergeCapability_Type(Integer32):
    """Custom type hh3cMplsLdpEntityMergeCapability based on Integer32"""
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


_Hh3cMplsLdpEntityMergeCapability_Type.__name__ = "Integer32"
_Hh3cMplsLdpEntityMergeCapability_Object = MibTableColumn
hh3cMplsLdpEntityMergeCapability = _Hh3cMplsLdpEntityMergeCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 7),
    _Hh3cMplsLdpEntityMergeCapability_Type()
)
hh3cMplsLdpEntityMergeCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityMergeCapability.setStatus("current")


class _Hh3cMplsLdpEntityVcDirectionality_Type(Integer32):
    """Custom type hh3cMplsLdpEntityVcDirectionality based on Integer32"""
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


_Hh3cMplsLdpEntityVcDirectionality_Type.__name__ = "Integer32"
_Hh3cMplsLdpEntityVcDirectionality_Object = MibTableColumn
hh3cMplsLdpEntityVcDirectionality = _Hh3cMplsLdpEntityVcDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 8),
    _Hh3cMplsLdpEntityVcDirectionality_Type()
)
hh3cMplsLdpEntityVcDirectionality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityVcDirectionality.setStatus("current")
_Hh3cMplsLdpEntityWellKnownDiscoveryPort_Type = Integer32
_Hh3cMplsLdpEntityWellKnownDiscoveryPort_Object = MibTableColumn
hh3cMplsLdpEntityWellKnownDiscoveryPort = _Hh3cMplsLdpEntityWellKnownDiscoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 9),
    _Hh3cMplsLdpEntityWellKnownDiscoveryPort_Type()
)
hh3cMplsLdpEntityWellKnownDiscoveryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityWellKnownDiscoveryPort.setStatus("current")


class _Hh3cMplsLdpEntityMtu_Type(Integer32):
    """Custom type hh3cMplsLdpEntityMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cMplsLdpEntityMtu_Type.__name__ = "Integer32"
_Hh3cMplsLdpEntityMtu_Object = MibTableColumn
hh3cMplsLdpEntityMtu = _Hh3cMplsLdpEntityMtu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 10),
    _Hh3cMplsLdpEntityMtu_Type()
)
hh3cMplsLdpEntityMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityMtu.setStatus("current")


class _Hh3cMplsLdpEntityKeepAliveHoldTimer_Type(Integer32):
    """Custom type hh3cMplsLdpEntityKeepAliveHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cMplsLdpEntityKeepAliveHoldTimer_Type.__name__ = "Integer32"
_Hh3cMplsLdpEntityKeepAliveHoldTimer_Object = MibTableColumn
hh3cMplsLdpEntityKeepAliveHoldTimer = _Hh3cMplsLdpEntityKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 11),
    _Hh3cMplsLdpEntityKeepAliveHoldTimer_Type()
)
hh3cMplsLdpEntityKeepAliveHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityKeepAliveHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityKeepAliveHoldTimer.setUnits("seconds")
_Hh3cMplsLdpEntityFailedInitSessionThreshold_Type = Integer32
_Hh3cMplsLdpEntityFailedInitSessionThreshold_Object = MibTableColumn
hh3cMplsLdpEntityFailedInitSessionThreshold = _Hh3cMplsLdpEntityFailedInitSessionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 12),
    _Hh3cMplsLdpEntityFailedInitSessionThreshold_Type()
)
hh3cMplsLdpEntityFailedInitSessionThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityFailedInitSessionThreshold.setStatus("current")


class _Hh3cMplsLdpEntityLabelDistributionMethod_Type(Integer32):
    """Custom type hh3cMplsLdpEntityLabelDistributionMethod based on Integer32"""
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


_Hh3cMplsLdpEntityLabelDistributionMethod_Type.__name__ = "Integer32"
_Hh3cMplsLdpEntityLabelDistributionMethod_Object = MibTableColumn
hh3cMplsLdpEntityLabelDistributionMethod = _Hh3cMplsLdpEntityLabelDistributionMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 13),
    _Hh3cMplsLdpEntityLabelDistributionMethod_Type()
)
hh3cMplsLdpEntityLabelDistributionMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityLabelDistributionMethod.setStatus("current")


class _Hh3cMplsLdpEntityLabelAllocationMethod_Type(Integer32):
    """Custom type hh3cMplsLdpEntityLabelAllocationMethod based on Integer32"""
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


_Hh3cMplsLdpEntityLabelAllocationMethod_Type.__name__ = "Integer32"
_Hh3cMplsLdpEntityLabelAllocationMethod_Object = MibTableColumn
hh3cMplsLdpEntityLabelAllocationMethod = _Hh3cMplsLdpEntityLabelAllocationMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 14),
    _Hh3cMplsLdpEntityLabelAllocationMethod_Type()
)
hh3cMplsLdpEntityLabelAllocationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityLabelAllocationMethod.setStatus("current")


class _Hh3cMplsLdpEntityHelloHoldTimer_Type(Integer32):
    """Custom type hh3cMplsLdpEntityHelloHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cMplsLdpEntityHelloHoldTimer_Type.__name__ = "Integer32"
_Hh3cMplsLdpEntityHelloHoldTimer_Object = MibTableColumn
hh3cMplsLdpEntityHelloHoldTimer = _Hh3cMplsLdpEntityHelloHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 15),
    _Hh3cMplsLdpEntityHelloHoldTimer_Type()
)
hh3cMplsLdpEntityHelloHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityHelloHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityHelloHoldTimer.setUnits("seconds")
_Hh3cMplsLdpEntityRowStatus_Type = RowStatus
_Hh3cMplsLdpEntityRowStatus_Object = MibTableColumn
hh3cMplsLdpEntityRowStatus = _Hh3cMplsLdpEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 1, 1, 16),
    _Hh3cMplsLdpEntityRowStatus_Type()
)
hh3cMplsLdpEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityRowStatus.setStatus("current")
_Hh3cMplsLdpEntityIfTable_Object = MibTable
hh3cMplsLdpEntityIfTable = _Hh3cMplsLdpEntityIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityIfTable.setStatus("current")
_Hh3cMplsLdpEntityIfEntry_Object = MibTableRow
hh3cMplsLdpEntityIfEntry = _Hh3cMplsLdpEntityIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 2, 1)
)
hh3cMplsLdpEntityIfEntry.setIndexNames(
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityIfEntry.setStatus("current")


class _Hh3cMplsLdpEntityIfIndex_Type(Unsigned32):
    """Custom type hh3cMplsLdpEntityIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsLdpEntityIfIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsLdpEntityIfIndex_Object = MibTableColumn
hh3cMplsLdpEntityIfIndex = _Hh3cMplsLdpEntityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 2, 1, 1),
    _Hh3cMplsLdpEntityIfIndex_Type()
)
hh3cMplsLdpEntityIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityIfIndex.setStatus("current")
_Hh3cMplsLdpEntityIfIpv4Address_Type = IpAddress
_Hh3cMplsLdpEntityIfIpv4Address_Object = MibTableColumn
hh3cMplsLdpEntityIfIpv4Address = _Hh3cMplsLdpEntityIfIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 2, 1, 2),
    _Hh3cMplsLdpEntityIfIpv4Address_Type()
)
hh3cMplsLdpEntityIfIpv4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityIfIpv4Address.setStatus("current")
_Hh3cMplsLdpEntityIfRowStatus_Type = RowStatus
_Hh3cMplsLdpEntityIfRowStatus_Object = MibTableColumn
hh3cMplsLdpEntityIfRowStatus = _Hh3cMplsLdpEntityIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 2, 1, 3),
    _Hh3cMplsLdpEntityIfRowStatus_Type()
)
hh3cMplsLdpEntityIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityIfRowStatus.setStatus("current")
_Hh3cMplsLdpEntityConfAtmLabelRangeTable_Object = MibTable
hh3cMplsLdpEntityConfAtmLabelRangeTable = _Hh3cMplsLdpEntityConfAtmLabelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityConfAtmLabelRangeTable.setStatus("current")
_Hh3cMplsLdpEntityConfAtmLabelRangeEntry_Object = MibTableRow
hh3cMplsLdpEntityConfAtmLabelRangeEntry = _Hh3cMplsLdpEntityConfAtmLabelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 3, 1)
)
hh3cMplsLdpEntityConfAtmLabelRangeEntry.setIndexNames(
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityIfIndex"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVPI"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVCI"),
)
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityConfAtmLabelRangeEntry.setStatus("current")
_Hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Type = AtmVpIdentifier
_Hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Object = MibTableColumn
hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVPI = _Hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 3, 1, 1),
    _Hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVPI_Type()
)
hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVPI.setStatus("current")
_Hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Type = AtmVcIdentifier
_Hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Object = MibTableColumn
hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVCI = _Hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 3, 1, 2),
    _Hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVCI_Type()
)
hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVCI.setStatus("current")
_Hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Type = AtmVpIdentifier
_Hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Object = MibTableColumn
hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVPI = _Hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 3, 1, 3),
    _Hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVPI_Type()
)
hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVPI.setStatus("current")
_Hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Type = AtmVcIdentifier
_Hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Object = MibTableColumn
hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVCI = _Hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 3, 1, 4),
    _Hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVCI_Type()
)
hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVCI.setStatus("current")
_Hh3cMplsLdpEntityConfAtmLabelRangeRowStatus_Type = RowStatus
_Hh3cMplsLdpEntityConfAtmLabelRangeRowStatus_Object = MibTableColumn
hh3cMplsLdpEntityConfAtmLabelRangeRowStatus = _Hh3cMplsLdpEntityConfAtmLabelRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 3, 1, 5),
    _Hh3cMplsLdpEntityConfAtmLabelRangeRowStatus_Type()
)
hh3cMplsLdpEntityConfAtmLabelRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityConfAtmLabelRangeRowStatus.setStatus("current")
_Hh3cMplsLdpEntityStatsTable_Object = MibTable
hh3cMplsLdpEntityStatsTable = _Hh3cMplsLdpEntityStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityStatsTable.setStatus("current")
_Hh3cMplsLdpEntityStatsEntry_Object = MibTableRow
hh3cMplsLdpEntityStatsEntry = _Hh3cMplsLdpEntityStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityStatsEntry.setStatus("current")
_Hh3cMplsLdpAttemptedSessions_Type = Counter32
_Hh3cMplsLdpAttemptedSessions_Object = MibTableColumn
hh3cMplsLdpAttemptedSessions = _Hh3cMplsLdpAttemptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 2, 4, 1, 1),
    _Hh3cMplsLdpAttemptedSessions_Type()
)
hh3cMplsLdpAttemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpAttemptedSessions.setStatus("current")
_Hh3cMplsLdpPeerObjects_ObjectIdentity = ObjectIdentity
hh3cMplsLdpPeerObjects = _Hh3cMplsLdpPeerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3)
)
_Hh3cMplsLdpPeerTable_Object = MibTable
hh3cMplsLdpPeerTable = _Hh3cMplsLdpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerTable.setStatus("current")
_Hh3cMplsLdpPeerEntry_Object = MibTableRow
hh3cMplsLdpPeerEntry = _Hh3cMplsLdpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 1, 1)
)
hh3cMplsLdpPeerEntry.setIndexNames(
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityIfIndex"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpPeerIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerEntry.setStatus("current")


class _Hh3cMplsLdpPeerIndex_Type(Unsigned32):
    """Custom type hh3cMplsLdpPeerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsLdpPeerIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsLdpPeerIndex_Object = MibTableColumn
hh3cMplsLdpPeerIndex = _Hh3cMplsLdpPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 1, 1, 1),
    _Hh3cMplsLdpPeerIndex_Type()
)
hh3cMplsLdpPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerIndex.setStatus("current")
_Hh3cMplsLdpPeerID_Type = MplsLdpIdentifier
_Hh3cMplsLdpPeerID_Object = MibTableColumn
hh3cMplsLdpPeerID = _Hh3cMplsLdpPeerID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 1, 1, 2),
    _Hh3cMplsLdpPeerID_Type()
)
hh3cMplsLdpPeerID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerID.setStatus("current")
_Hh3cMplsLdpPeerInternetworkAddrType_Type = AddressFamilyNumbers
_Hh3cMplsLdpPeerInternetworkAddrType_Object = MibTableColumn
hh3cMplsLdpPeerInternetworkAddrType = _Hh3cMplsLdpPeerInternetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 1, 1, 3),
    _Hh3cMplsLdpPeerInternetworkAddrType_Type()
)
hh3cMplsLdpPeerInternetworkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerInternetworkAddrType.setStatus("current")
_Hh3cMplsLdpPeerInternetworkAddr_Type = MplsLdpGenAddr
_Hh3cMplsLdpPeerInternetworkAddr_Object = MibTableColumn
hh3cMplsLdpPeerInternetworkAddr = _Hh3cMplsLdpPeerInternetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 1, 1, 4),
    _Hh3cMplsLdpPeerInternetworkAddr_Type()
)
hh3cMplsLdpPeerInternetworkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerInternetworkAddr.setStatus("current")


class _Hh3cMplsLdpPeerDefaultMtu_Type(Integer32):
    """Custom type hh3cMplsLdpPeerDefaultMtu based on Integer32"""
    defaultValue = 9180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cMplsLdpPeerDefaultMtu_Type.__name__ = "Integer32"
_Hh3cMplsLdpPeerDefaultMtu_Object = MibTableColumn
hh3cMplsLdpPeerDefaultMtu = _Hh3cMplsLdpPeerDefaultMtu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 1, 1, 5),
    _Hh3cMplsLdpPeerDefaultMtu_Type()
)
hh3cMplsLdpPeerDefaultMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerDefaultMtu.setStatus("current")


class _Hh3cMplsLdpPeerKeepAliveHoldTimer_Type(Integer32):
    """Custom type hh3cMplsLdpPeerKeepAliveHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cMplsLdpPeerKeepAliveHoldTimer_Type.__name__ = "Integer32"
_Hh3cMplsLdpPeerKeepAliveHoldTimer_Object = MibTableColumn
hh3cMplsLdpPeerKeepAliveHoldTimer = _Hh3cMplsLdpPeerKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 1, 1, 6),
    _Hh3cMplsLdpPeerKeepAliveHoldTimer_Type()
)
hh3cMplsLdpPeerKeepAliveHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerKeepAliveHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerKeepAliveHoldTimer.setUnits("seconds")


class _Hh3cMplsLdpPeerLabelDistributionMethod_Type(Integer32):
    """Custom type hh3cMplsLdpPeerLabelDistributionMethod based on Integer32"""
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


_Hh3cMplsLdpPeerLabelDistributionMethod_Type.__name__ = "Integer32"
_Hh3cMplsLdpPeerLabelDistributionMethod_Object = MibTableColumn
hh3cMplsLdpPeerLabelDistributionMethod = _Hh3cMplsLdpPeerLabelDistributionMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 1, 1, 7),
    _Hh3cMplsLdpPeerLabelDistributionMethod_Type()
)
hh3cMplsLdpPeerLabelDistributionMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerLabelDistributionMethod.setStatus("current")


class _Hh3cMplsLdpPeerType_Type(Integer32):
    """Custom type hh3cMplsLdpPeerType based on Integer32"""
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


_Hh3cMplsLdpPeerType_Type.__name__ = "Integer32"
_Hh3cMplsLdpPeerType_Object = MibTableColumn
hh3cMplsLdpPeerType = _Hh3cMplsLdpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 1, 1, 8),
    _Hh3cMplsLdpPeerType_Type()
)
hh3cMplsLdpPeerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerType.setStatus("current")
_Hh3cMplsLdpPeerRowStatus_Type = RowStatus
_Hh3cMplsLdpPeerRowStatus_Object = MibTableColumn
hh3cMplsLdpPeerRowStatus = _Hh3cMplsLdpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 1, 1, 9),
    _Hh3cMplsLdpPeerRowStatus_Type()
)
hh3cMplsLdpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerRowStatus.setStatus("current")
_Hh3cMplsLdpPeerConfAtmLabelRangeTable_Object = MibTable
hh3cMplsLdpPeerConfAtmLabelRangeTable = _Hh3cMplsLdpPeerConfAtmLabelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerConfAtmLabelRangeTable.setStatus("current")
_Hh3cMplsLdpPeerConfAtmLabelRangeEntry_Object = MibTableRow
hh3cMplsLdpPeerConfAtmLabelRangeEntry = _Hh3cMplsLdpPeerConfAtmLabelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 2, 1)
)
hh3cMplsLdpPeerConfAtmLabelRangeEntry.setIndexNames(
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityIfIndex"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpPeerIndex"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVPI"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVCI"),
)
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerConfAtmLabelRangeEntry.setStatus("current")
_Hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Type = AtmVpIdentifier
_Hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Object = MibTableColumn
hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVPI = _Hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 2, 1, 1),
    _Hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVPI_Type()
)
hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVPI.setStatus("current")
_Hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Type = AtmVcIdentifier
_Hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Object = MibTableColumn
hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVCI = _Hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 2, 1, 2),
    _Hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVCI_Type()
)
hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVCI.setStatus("current")
_Hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Type = AtmVpIdentifier
_Hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Object = MibTableColumn
hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVPI = _Hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 2, 1, 3),
    _Hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVPI_Type()
)
hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVPI.setStatus("current")
_Hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Type = AtmVcIdentifier
_Hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Object = MibTableColumn
hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVCI = _Hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 3, 2, 1, 4),
    _Hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVCI_Type()
)
hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVCI.setStatus("current")
_Hh3cMplsLdpSessionObjects_ObjectIdentity = ObjectIdentity
hh3cMplsLdpSessionObjects = _Hh3cMplsLdpSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4)
)
_Hh3cMplsLdpSessionTable_Object = MibTable
hh3cMplsLdpSessionTable = _Hh3cMplsLdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionTable.setStatus("current")
_Hh3cMplsLdpSessionEntry_Object = MibTableRow
hh3cMplsLdpSessionEntry = _Hh3cMplsLdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4, 1, 1)
)
hh3cMplsLdpSessionEntry.setIndexNames(
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityIfIndex"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpPeerIndex"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpSessionIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionEntry.setStatus("current")


class _Hh3cMplsLdpSessionIndex_Type(Unsigned32):
    """Custom type hh3cMplsLdpSessionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsLdpSessionIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsLdpSessionIndex_Object = MibTableColumn
hh3cMplsLdpSessionIndex = _Hh3cMplsLdpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4, 1, 1, 1),
    _Hh3cMplsLdpSessionIndex_Type()
)
hh3cMplsLdpSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionIndex.setStatus("current")
_Hh3cMplsLdpSessionID_Type = MplsLdpIdentifier
_Hh3cMplsLdpSessionID_Object = MibTableColumn
hh3cMplsLdpSessionID = _Hh3cMplsLdpSessionID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4, 1, 1, 2),
    _Hh3cMplsLdpSessionID_Type()
)
hh3cMplsLdpSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionID.setStatus("current")


class _Hh3cMplsLdpSessionProtocolVersion_Type(Integer32):
    """Custom type hh3cMplsLdpSessionProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cMplsLdpSessionProtocolVersion_Type.__name__ = "Integer32"
_Hh3cMplsLdpSessionProtocolVersion_Object = MibTableColumn
hh3cMplsLdpSessionProtocolVersion = _Hh3cMplsLdpSessionProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4, 1, 1, 3),
    _Hh3cMplsLdpSessionProtocolVersion_Type()
)
hh3cMplsLdpSessionProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionProtocolVersion.setStatus("current")
_Hh3cMplsLdpSessionKeepAliveHoldTimeRemaining_Type = TimeInterval
_Hh3cMplsLdpSessionKeepAliveHoldTimeRemaining_Object = MibTableColumn
hh3cMplsLdpSessionKeepAliveHoldTimeRemaining = _Hh3cMplsLdpSessionKeepAliveHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4, 1, 1, 4),
    _Hh3cMplsLdpSessionKeepAliveHoldTimeRemaining_Type()
)
hh3cMplsLdpSessionKeepAliveHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionKeepAliveHoldTimeRemaining.setStatus("current")


class _Hh3cMplsLdpSessionRole_Type(Integer32):
    """Custom type hh3cMplsLdpSessionRole based on Integer32"""
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


_Hh3cMplsLdpSessionRole_Type.__name__ = "Integer32"
_Hh3cMplsLdpSessionRole_Object = MibTableColumn
hh3cMplsLdpSessionRole = _Hh3cMplsLdpSessionRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4, 1, 1, 5),
    _Hh3cMplsLdpSessionRole_Type()
)
hh3cMplsLdpSessionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionRole.setStatus("current")


class _Hh3cMplsLdpSessionState_Type(Integer32):
    """Custom type hh3cMplsLdpSessionState based on Integer32"""
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


_Hh3cMplsLdpSessionState_Type.__name__ = "Integer32"
_Hh3cMplsLdpSessionState_Object = MibTableColumn
hh3cMplsLdpSessionState = _Hh3cMplsLdpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4, 1, 1, 6),
    _Hh3cMplsLdpSessionState_Type()
)
hh3cMplsLdpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionState.setStatus("current")
_Hh3cMplsLdpSessionAtmLabelRangeLowerBoundVPI_Type = AtmVpIdentifier
_Hh3cMplsLdpSessionAtmLabelRangeLowerBoundVPI_Object = MibTableColumn
hh3cMplsLdpSessionAtmLabelRangeLowerBoundVPI = _Hh3cMplsLdpSessionAtmLabelRangeLowerBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4, 1, 1, 7),
    _Hh3cMplsLdpSessionAtmLabelRangeLowerBoundVPI_Type()
)
hh3cMplsLdpSessionAtmLabelRangeLowerBoundVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionAtmLabelRangeLowerBoundVPI.setStatus("current")
_Hh3cMplsLdpSessionAtmLabelRangeLowerBoundVCI_Type = AtmVcIdentifier
_Hh3cMplsLdpSessionAtmLabelRangeLowerBoundVCI_Object = MibTableColumn
hh3cMplsLdpSessionAtmLabelRangeLowerBoundVCI = _Hh3cMplsLdpSessionAtmLabelRangeLowerBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4, 1, 1, 8),
    _Hh3cMplsLdpSessionAtmLabelRangeLowerBoundVCI_Type()
)
hh3cMplsLdpSessionAtmLabelRangeLowerBoundVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionAtmLabelRangeLowerBoundVCI.setStatus("current")
_Hh3cMplsLdpSessionAtmLabelRangeUpperBoundVPI_Type = AtmVpIdentifier
_Hh3cMplsLdpSessionAtmLabelRangeUpperBoundVPI_Object = MibTableColumn
hh3cMplsLdpSessionAtmLabelRangeUpperBoundVPI = _Hh3cMplsLdpSessionAtmLabelRangeUpperBoundVPI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4, 1, 1, 9),
    _Hh3cMplsLdpSessionAtmLabelRangeUpperBoundVPI_Type()
)
hh3cMplsLdpSessionAtmLabelRangeUpperBoundVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionAtmLabelRangeUpperBoundVPI.setStatus("current")
_Hh3cMplsLdpSessionAtmLabelRangeUpperBoundVCI_Type = AtmVcIdentifier
_Hh3cMplsLdpSessionAtmLabelRangeUpperBoundVCI_Object = MibTableColumn
hh3cMplsLdpSessionAtmLabelRangeUpperBoundVCI = _Hh3cMplsLdpSessionAtmLabelRangeUpperBoundVCI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 4, 1, 1, 10),
    _Hh3cMplsLdpSessionAtmLabelRangeUpperBoundVCI_Type()
)
hh3cMplsLdpSessionAtmLabelRangeUpperBoundVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionAtmLabelRangeUpperBoundVCI.setStatus("current")
_Hh3cMplsLdpHelloAdjacencyObjects_ObjectIdentity = ObjectIdentity
hh3cMplsLdpHelloAdjacencyObjects = _Hh3cMplsLdpHelloAdjacencyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 5)
)
_Hh3cMplsLdpHelloAdjacencyTable_Object = MibTable
hh3cMplsLdpHelloAdjacencyTable = _Hh3cMplsLdpHelloAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cMplsLdpHelloAdjacencyTable.setStatus("current")
_Hh3cMplsLdpHelloAdjacencyEntry_Object = MibTableRow
hh3cMplsLdpHelloAdjacencyEntry = _Hh3cMplsLdpHelloAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 5, 1, 1)
)
hh3cMplsLdpHelloAdjacencyEntry.setIndexNames(
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityIfIndex"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpPeerIndex"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpSessionIndex"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpHelloAdjacencyIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsLdpHelloAdjacencyEntry.setStatus("current")


class _Hh3cMplsLdpHelloAdjacencyIndex_Type(Unsigned32):
    """Custom type hh3cMplsLdpHelloAdjacencyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cMplsLdpHelloAdjacencyIndex_Type.__name__ = "Unsigned32"
_Hh3cMplsLdpHelloAdjacencyIndex_Object = MibTableColumn
hh3cMplsLdpHelloAdjacencyIndex = _Hh3cMplsLdpHelloAdjacencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 5, 1, 1, 1),
    _Hh3cMplsLdpHelloAdjacencyIndex_Type()
)
hh3cMplsLdpHelloAdjacencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsLdpHelloAdjacencyIndex.setStatus("current")
_Hh3cMplsLdpHelloAdjacencyHoldTimeRemaining_Type = TimeInterval
_Hh3cMplsLdpHelloAdjacencyHoldTimeRemaining_Object = MibTableColumn
hh3cMplsLdpHelloAdjacencyHoldTimeRemaining = _Hh3cMplsLdpHelloAdjacencyHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 5, 1, 1, 2),
    _Hh3cMplsLdpHelloAdjacencyHoldTimeRemaining_Type()
)
hh3cMplsLdpHelloAdjacencyHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsLdpHelloAdjacencyHoldTimeRemaining.setStatus("current")
_Hh3cMplsLdpCrlspTnlObjects_ObjectIdentity = ObjectIdentity
hh3cMplsLdpCrlspTnlObjects = _Hh3cMplsLdpCrlspTnlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6)
)
_Hh3cMplsLdpCrlspTnlTable_Object = MibTable
hh3cMplsLdpCrlspTnlTable = _Hh3cMplsLdpCrlspTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlTable.setStatus("current")
_Hh3cMplsLdpCrlspTnlEntry_Object = MibTableRow
hh3cMplsLdpCrlspTnlEntry = _Hh3cMplsLdpCrlspTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1)
)
hh3cMplsLdpCrlspTnlEntry.setIndexNames(
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpCrlspTnlIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlEntry.setStatus("current")
_Hh3cMplsLdpCrlspTnlIndex_Type = MplsTunnelIndex
_Hh3cMplsLdpCrlspTnlIndex_Object = MibTableColumn
hh3cMplsLdpCrlspTnlIndex = _Hh3cMplsLdpCrlspTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 1),
    _Hh3cMplsLdpCrlspTnlIndex_Type()
)
hh3cMplsLdpCrlspTnlIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlIndex.setStatus("current")
_Hh3cMplsLdpCrlspTnlName_Type = DisplayString
_Hh3cMplsLdpCrlspTnlName_Object = MibTableColumn
hh3cMplsLdpCrlspTnlName = _Hh3cMplsLdpCrlspTnlName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 2),
    _Hh3cMplsLdpCrlspTnlName_Type()
)
hh3cMplsLdpCrlspTnlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlName.setStatus("current")


class _Hh3cMplsLdpCrlspTnlDirection_Type(Integer32):
    """Custom type hh3cMplsLdpCrlspTnlDirection based on Integer32"""
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


_Hh3cMplsLdpCrlspTnlDirection_Type.__name__ = "Integer32"
_Hh3cMplsLdpCrlspTnlDirection_Object = MibTableColumn
hh3cMplsLdpCrlspTnlDirection = _Hh3cMplsLdpCrlspTnlDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 3),
    _Hh3cMplsLdpCrlspTnlDirection_Type()
)
hh3cMplsLdpCrlspTnlDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlDirection.setStatus("current")


class _Hh3cMplsLdpCrlspTnlSignallingProto_Type(Integer32):
    """Custom type hh3cMplsLdpCrlspTnlSignallingProto based on Integer32"""
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


_Hh3cMplsLdpCrlspTnlSignallingProto_Type.__name__ = "Integer32"
_Hh3cMplsLdpCrlspTnlSignallingProto_Object = MibTableColumn
hh3cMplsLdpCrlspTnlSignallingProto = _Hh3cMplsLdpCrlspTnlSignallingProto_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 4),
    _Hh3cMplsLdpCrlspTnlSignallingProto_Type()
)
hh3cMplsLdpCrlspTnlSignallingProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlSignallingProto.setStatus("current")


class _Hh3cMplsLdpCrlspTnlSetupPrio_Type(Integer32):
    """Custom type hh3cMplsLdpCrlspTnlSetupPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cMplsLdpCrlspTnlSetupPrio_Type.__name__ = "Integer32"
_Hh3cMplsLdpCrlspTnlSetupPrio_Object = MibTableColumn
hh3cMplsLdpCrlspTnlSetupPrio = _Hh3cMplsLdpCrlspTnlSetupPrio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 5),
    _Hh3cMplsLdpCrlspTnlSetupPrio_Type()
)
hh3cMplsLdpCrlspTnlSetupPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlSetupPrio.setStatus("current")


class _Hh3cMplsLdpCrlspTnlHoldingPrio_Type(Integer32):
    """Custom type hh3cMplsLdpCrlspTnlHoldingPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cMplsLdpCrlspTnlHoldingPrio_Type.__name__ = "Integer32"
_Hh3cMplsLdpCrlspTnlHoldingPrio_Object = MibTableColumn
hh3cMplsLdpCrlspTnlHoldingPrio = _Hh3cMplsLdpCrlspTnlHoldingPrio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 6),
    _Hh3cMplsLdpCrlspTnlHoldingPrio_Type()
)
hh3cMplsLdpCrlspTnlHoldingPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlHoldingPrio.setStatus("current")


class _Hh3cMplsLdpCrlspTnlPeakDataRate_Type(BitRate):
    """Custom type hh3cMplsLdpCrlspTnlPeakDataRate based on BitRate"""
    defaultValue = 0


_Hh3cMplsLdpCrlspTnlPeakDataRate_Object = MibTableColumn
hh3cMplsLdpCrlspTnlPeakDataRate = _Hh3cMplsLdpCrlspTnlPeakDataRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 7),
    _Hh3cMplsLdpCrlspTnlPeakDataRate_Type()
)
hh3cMplsLdpCrlspTnlPeakDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlPeakDataRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlPeakDataRate.setUnits("bits per second")


class _Hh3cMplsLdpCrlspTnlPeakBurstSize_Type(BurstSize):
    """Custom type hh3cMplsLdpCrlspTnlPeakBurstSize based on BurstSize"""
    defaultValue = 0


_Hh3cMplsLdpCrlspTnlPeakBurstSize_Object = MibTableColumn
hh3cMplsLdpCrlspTnlPeakBurstSize = _Hh3cMplsLdpCrlspTnlPeakBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 8),
    _Hh3cMplsLdpCrlspTnlPeakBurstSize_Type()
)
hh3cMplsLdpCrlspTnlPeakBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlPeakBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlPeakBurstSize.setUnits("bytes")


class _Hh3cMplsLdpCrlspTnlCommittedDataRate_Type(BitRate):
    """Custom type hh3cMplsLdpCrlspTnlCommittedDataRate based on BitRate"""
    defaultValue = 0


_Hh3cMplsLdpCrlspTnlCommittedDataRate_Object = MibTableColumn
hh3cMplsLdpCrlspTnlCommittedDataRate = _Hh3cMplsLdpCrlspTnlCommittedDataRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 9),
    _Hh3cMplsLdpCrlspTnlCommittedDataRate_Type()
)
hh3cMplsLdpCrlspTnlCommittedDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlCommittedDataRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlCommittedDataRate.setUnits("bits per second")


class _Hh3cMplsLdpCrlspTnlCommittedBurstSize_Type(BurstSize):
    """Custom type hh3cMplsLdpCrlspTnlCommittedBurstSize based on BurstSize"""
    defaultValue = 0


_Hh3cMplsLdpCrlspTnlCommittedBurstSize_Object = MibTableColumn
hh3cMplsLdpCrlspTnlCommittedBurstSize = _Hh3cMplsLdpCrlspTnlCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 10),
    _Hh3cMplsLdpCrlspTnlCommittedBurstSize_Type()
)
hh3cMplsLdpCrlspTnlCommittedBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlCommittedBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlCommittedBurstSize.setUnits("bytes")


class _Hh3cMplsLdpCrlspTnlExcessBurstSize_Type(BurstSize):
    """Custom type hh3cMplsLdpCrlspTnlExcessBurstSize based on BurstSize"""
    defaultValue = 0


_Hh3cMplsLdpCrlspTnlExcessBurstSize_Object = MibTableColumn
hh3cMplsLdpCrlspTnlExcessBurstSize = _Hh3cMplsLdpCrlspTnlExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 11),
    _Hh3cMplsLdpCrlspTnlExcessBurstSize_Type()
)
hh3cMplsLdpCrlspTnlExcessBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlExcessBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlExcessBurstSize.setUnits("bytes")


class _Hh3cMplsLdpCrlspTnlIsPinned_Type(TruthValue):
    """Custom type hh3cMplsLdpCrlspTnlIsPinned based on TruthValue"""


_Hh3cMplsLdpCrlspTnlIsPinned_Object = MibTableColumn
hh3cMplsLdpCrlspTnlIsPinned = _Hh3cMplsLdpCrlspTnlIsPinned_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 12),
    _Hh3cMplsLdpCrlspTnlIsPinned_Type()
)
hh3cMplsLdpCrlspTnlIsPinned.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlIsPinned.setStatus("current")


class _Hh3cMplsLdpCrlspTnlFrequency_Type(Integer32):
    """Custom type hh3cMplsLdpCrlspTnlFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Hh3cMplsLdpCrlspTnlFrequency_Type.__name__ = "Integer32"
_Hh3cMplsLdpCrlspTnlFrequency_Object = MibTableColumn
hh3cMplsLdpCrlspTnlFrequency = _Hh3cMplsLdpCrlspTnlFrequency_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 13),
    _Hh3cMplsLdpCrlspTnlFrequency_Type()
)
hh3cMplsLdpCrlspTnlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlFrequency.setStatus("current")


class _Hh3cMplsLdpCrlspTnlWeight_Type(Integer32):
    """Custom type hh3cMplsLdpCrlspTnlWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cMplsLdpCrlspTnlWeight_Type.__name__ = "Integer32"
_Hh3cMplsLdpCrlspTnlWeight_Object = MibTableColumn
hh3cMplsLdpCrlspTnlWeight = _Hh3cMplsLdpCrlspTnlWeight_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 14),
    _Hh3cMplsLdpCrlspTnlWeight_Type()
)
hh3cMplsLdpCrlspTnlWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlWeight.setStatus("current")
_Hh3cMplsLdpCrlspTnlRowStatus_Type = RowStatus
_Hh3cMplsLdpCrlspTnlRowStatus_Object = MibTableColumn
hh3cMplsLdpCrlspTnlRowStatus = _Hh3cMplsLdpCrlspTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 1, 1, 15),
    _Hh3cMplsLdpCrlspTnlRowStatus_Type()
)
hh3cMplsLdpCrlspTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTnlRowStatus.setStatus("current")
_Hh3cMplsLdpCrlspErHopTable_Object = MibTable
hh3cMplsLdpCrlspErHopTable = _Hh3cMplsLdpCrlspErHopTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspErHopTable.setStatus("current")
_Hh3cMplsLdpCrlspErHopEntry_Object = MibTableRow
hh3cMplsLdpCrlspErHopEntry = _Hh3cMplsLdpCrlspErHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 2, 1)
)
hh3cMplsLdpCrlspErHopEntry.setIndexNames(
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpCrlspTnlIndex"),
    (0, "HH3C-MPLS-LDP-MIB", "hh3cMplsLdpCrlspErHopIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspErHopEntry.setStatus("current")
_Hh3cMplsLdpCrlspErHopIndex_Type = Integer32
_Hh3cMplsLdpCrlspErHopIndex_Object = MibTableColumn
hh3cMplsLdpCrlspErHopIndex = _Hh3cMplsLdpCrlspErHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 2, 1, 1),
    _Hh3cMplsLdpCrlspErHopIndex_Type()
)
hh3cMplsLdpCrlspErHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspErHopIndex.setStatus("current")


class _Hh3cMplsLdpCrlspErHopAddrType_Type(Integer32):
    """Custom type hh3cMplsLdpCrlspErHopAddrType based on Integer32"""
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


_Hh3cMplsLdpCrlspErHopAddrType_Type.__name__ = "Integer32"
_Hh3cMplsLdpCrlspErHopAddrType_Object = MibTableColumn
hh3cMplsLdpCrlspErHopAddrType = _Hh3cMplsLdpCrlspErHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 2, 1, 2),
    _Hh3cMplsLdpCrlspErHopAddrType_Type()
)
hh3cMplsLdpCrlspErHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspErHopAddrType.setStatus("current")
_Hh3cMplsLdpCrlspErHopIpv4Addr_Type = IpAddress
_Hh3cMplsLdpCrlspErHopIpv4Addr_Object = MibTableColumn
hh3cMplsLdpCrlspErHopIpv4Addr = _Hh3cMplsLdpCrlspErHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 2, 1, 3),
    _Hh3cMplsLdpCrlspErHopIpv4Addr_Type()
)
hh3cMplsLdpCrlspErHopIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspErHopIpv4Addr.setStatus("current")


class _Hh3cMplsLdpCrlspErHopIpv4PrefixLen_Type(Integer32):
    """Custom type hh3cMplsLdpCrlspErHopIpv4PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Hh3cMplsLdpCrlspErHopIpv4PrefixLen_Type.__name__ = "Integer32"
_Hh3cMplsLdpCrlspErHopIpv4PrefixLen_Object = MibTableColumn
hh3cMplsLdpCrlspErHopIpv4PrefixLen = _Hh3cMplsLdpCrlspErHopIpv4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 2, 1, 4),
    _Hh3cMplsLdpCrlspErHopIpv4PrefixLen_Type()
)
hh3cMplsLdpCrlspErHopIpv4PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspErHopIpv4PrefixLen.setStatus("current")


class _Hh3cMplsLdpCrlspErHopStrictOrLoose_Type(Integer32):
    """Custom type hh3cMplsLdpCrlspErHopStrictOrLoose based on Integer32"""
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


_Hh3cMplsLdpCrlspErHopStrictOrLoose_Type.__name__ = "Integer32"
_Hh3cMplsLdpCrlspErHopStrictOrLoose_Object = MibTableColumn
hh3cMplsLdpCrlspErHopStrictOrLoose = _Hh3cMplsLdpCrlspErHopStrictOrLoose_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 2, 1, 5),
    _Hh3cMplsLdpCrlspErHopStrictOrLoose_Type()
)
hh3cMplsLdpCrlspErHopStrictOrLoose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspErHopStrictOrLoose.setStatus("current")
_Hh3cMplsLdpCrlspErHopRowStatus_Type = RowStatus
_Hh3cMplsLdpCrlspErHopRowStatus_Object = MibTableColumn
hh3cMplsLdpCrlspErHopRowStatus = _Hh3cMplsLdpCrlspErHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 1, 6, 2, 1, 6),
    _Hh3cMplsLdpCrlspErHopRowStatus_Type()
)
hh3cMplsLdpCrlspErHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspErHopRowStatus.setStatus("current")
_Hh3cMplsLdpNotifications_ObjectIdentity = ObjectIdentity
hh3cMplsLdpNotifications = _Hh3cMplsLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 2)
)
_Hh3cMplsLdpNotificationPrefix_ObjectIdentity = ObjectIdentity
hh3cMplsLdpNotificationPrefix = _Hh3cMplsLdpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 2, 0)
)
hh3cMplsLdpEntityEntry.registerAugmentions(
    ("HH3C-MPLS-LDP-MIB",
     "hh3cMplsLdpEntityStatsEntry")
)
hh3cMplsLdpEntityStatsEntry.setIndexNames(*hh3cMplsLdpEntityEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hh3cMplsLdpFailedInitSessionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 2, 0, 1)
)
hh3cMplsLdpFailedInitSessionThresholdExceeded.setObjects(
      *(("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
        ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityID"),
        ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityFailedInitSessionThreshold"))
)
if mibBuilder.loadTexts:
    hh3cMplsLdpFailedInitSessionThresholdExceeded.setStatus(
        "current"
    )

hh3cMplsLdpCrlspTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 2, 0, 2)
)
hh3cMplsLdpCrlspTunnelUp.setObjects(
      *(("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
        ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityID"),
        ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpCrlspTnlIndex"))
)
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTunnelUp.setStatus(
        "current"
    )

hh3cMplsLdpCrlspTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 2, 0, 3)
)
hh3cMplsLdpCrlspTunnelDown.setObjects(
      *(("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
        ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityID"),
        ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpCrlspTnlIndex"))
)
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTunnelDown.setStatus(
        "current"
    )

hh3cMplsLdpCrlspTunnelSetupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 2, 0, 4)
)
hh3cMplsLdpCrlspTunnelSetupFailure.setObjects(
      *(("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
        ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityID"),
        ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpCrlspTnlIndex"))
)
if mibBuilder.loadTexts:
    hh3cMplsLdpCrlspTunnelSetupFailure.setStatus(
        "current"
    )

hh3cMplsLdpIncarnUpEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 2, 0, 11)
)
hh3cMplsLdpIncarnUpEventFailure.setObjects(
    ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID")
)
if mibBuilder.loadTexts:
    hh3cMplsLdpIncarnUpEventFailure.setStatus(
        "current"
    )

hh3cMplsLdpIncarnDownEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 2, 0, 12)
)
hh3cMplsLdpIncarnDownEventFailure.setObjects(
    ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID")
)
if mibBuilder.loadTexts:
    hh3cMplsLdpIncarnDownEventFailure.setStatus(
        "current"
    )

hh3cMplsLdpEntityUpEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 2, 0, 13)
)
hh3cMplsLdpEntityUpEventFailure.setObjects(
      *(("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
        ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityID"))
)
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityUpEventFailure.setStatus(
        "current"
    )

hh3cMplsLdpEntityDownEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 2, 0, 14)
)
hh3cMplsLdpEntityDownEventFailure.setObjects(
      *(("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpLsrIncarnID"),
        ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpEntityID"))
)
if mibBuilder.loadTexts:
    hh3cMplsLdpEntityDownEventFailure.setStatus(
        "current"
    )

hh3cMplsLdpSessionUpEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 2, 0, 15)
)
hh3cMplsLdpSessionUpEventFailure.setObjects(
      *(("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpSessionID"),
        ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpSessionState"))
)
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionUpEventFailure.setStatus(
        "current"
    )

hh3cMplsLdpSessionDownEventFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2, 2, 0, 16)
)
hh3cMplsLdpSessionDownEventFailure.setObjects(
      *(("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpSessionID"),
        ("HH3C-MPLS-LDP-MIB", "hh3cMplsLdpSessionState"))
)
if mibBuilder.loadTexts:
    hh3cMplsLdpSessionDownEventFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MPLS-LDP-MIB",
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
       "hh3cMplsLdp": hh3cMplsLdp,
       "hh3cMplsLdpObjects": hh3cMplsLdpObjects,
       "hh3cMplsLdpLsrObjects": hh3cMplsLdpLsrObjects,
       "hh3cMplsLdpLsrIncarnTable": hh3cMplsLdpLsrIncarnTable,
       "hh3cMplsLdpLsrIncarnEntry": hh3cMplsLdpLsrIncarnEntry,
       "hh3cMplsLdpLsrID": hh3cMplsLdpLsrID,
       "hh3cMplsLdpLsrLoopDetectionPresent": hh3cMplsLdpLsrLoopDetectionPresent,
       "hh3cMplsLdpLsrLoopDetectionAdminStatus": hh3cMplsLdpLsrLoopDetectionAdminStatus,
       "hh3cMplsLdpLsrPathVectorLimit": hh3cMplsLdpLsrPathVectorLimit,
       "hh3cMplsLdpLsrHopCountLimit": hh3cMplsLdpLsrHopCountLimit,
       "hh3cMplsLdpLsrLoopPreventionPresent": hh3cMplsLdpLsrLoopPreventionPresent,
       "hh3cMplsLdpLsrLoopPreventionAdminStatus": hh3cMplsLdpLsrLoopPreventionAdminStatus,
       "hh3cMplsLdpLsrLabelRetentionMode": hh3cMplsLdpLsrLabelRetentionMode,
       "hh3cMplsLdpLsrIncarnID": hh3cMplsLdpLsrIncarnID,
       "hh3cMplsLdpLsrMaxLdpEntities": hh3cMplsLdpLsrMaxLdpEntities,
       "hh3cMplsLdpLsrMaxLocalPeers": hh3cMplsLdpLsrMaxLocalPeers,
       "hh3cMplsLdpLsrMaxRemotePeers": hh3cMplsLdpLsrMaxRemotePeers,
       "hh3cMplsLdpLsrMaxIfaces": hh3cMplsLdpLsrMaxIfaces,
       "hh3cMplsLdpLsrMaxLsps": hh3cMplsLdpLsrMaxLsps,
       "hh3cMplsLdpLsrMaxCrlspTnls": hh3cMplsLdpLsrMaxCrlspTnls,
       "hh3cMplsLdpLsrMaxErhopPerCrlspTnl": hh3cMplsLdpLsrMaxErhopPerCrlspTnl,
       "hh3cMplsLdpLsrRowStatus": hh3cMplsLdpLsrRowStatus,
       "hh3cMplsLdpLsrMaxVcmCapability": hh3cMplsLdpLsrMaxVcmCapability,
       "hh3cMplsLdpLsrVcmPathVecInAllLblMapPresent": hh3cMplsLdpLsrVcmPathVecInAllLblMapPresent,
       "hh3cMplsLdpLsrRequestRetrytimerValue": hh3cMplsLdpLsrRequestRetrytimerValue,
       "hh3cMplsLdpLsrNumOfRequestRetryAttempts": hh3cMplsLdpLsrNumOfRequestRetryAttempts,
       "hh3cMplsLdpEntityObjects": hh3cMplsLdpEntityObjects,
       "hh3cMplsLdpEntityTable": hh3cMplsLdpEntityTable,
       "hh3cMplsLdpEntityEntry": hh3cMplsLdpEntityEntry,
       "hh3cMplsLdpEntityID": hh3cMplsLdpEntityID,
       "hh3cMplsLdpEntityLabelSpaceType": hh3cMplsLdpEntityLabelSpaceType,
       "hh3cMplsLdpEntityDefVpi": hh3cMplsLdpEntityDefVpi,
       "hh3cMplsLdpEntityDefVci": hh3cMplsLdpEntityDefVci,
       "hh3cMplsLdpEntityUnlabTrafVpi": hh3cMplsLdpEntityUnlabTrafVpi,
       "hh3cMplsLdpEntityUnlabTrafVci": hh3cMplsLdpEntityUnlabTrafVci,
       "hh3cMplsLdpEntityMergeCapability": hh3cMplsLdpEntityMergeCapability,
       "hh3cMplsLdpEntityVcDirectionality": hh3cMplsLdpEntityVcDirectionality,
       "hh3cMplsLdpEntityWellKnownDiscoveryPort": hh3cMplsLdpEntityWellKnownDiscoveryPort,
       "hh3cMplsLdpEntityMtu": hh3cMplsLdpEntityMtu,
       "hh3cMplsLdpEntityKeepAliveHoldTimer": hh3cMplsLdpEntityKeepAliveHoldTimer,
       "hh3cMplsLdpEntityFailedInitSessionThreshold": hh3cMplsLdpEntityFailedInitSessionThreshold,
       "hh3cMplsLdpEntityLabelDistributionMethod": hh3cMplsLdpEntityLabelDistributionMethod,
       "hh3cMplsLdpEntityLabelAllocationMethod": hh3cMplsLdpEntityLabelAllocationMethod,
       "hh3cMplsLdpEntityHelloHoldTimer": hh3cMplsLdpEntityHelloHoldTimer,
       "hh3cMplsLdpEntityRowStatus": hh3cMplsLdpEntityRowStatus,
       "hh3cMplsLdpEntityIfTable": hh3cMplsLdpEntityIfTable,
       "hh3cMplsLdpEntityIfEntry": hh3cMplsLdpEntityIfEntry,
       "hh3cMplsLdpEntityIfIndex": hh3cMplsLdpEntityIfIndex,
       "hh3cMplsLdpEntityIfIpv4Address": hh3cMplsLdpEntityIfIpv4Address,
       "hh3cMplsLdpEntityIfRowStatus": hh3cMplsLdpEntityIfRowStatus,
       "hh3cMplsLdpEntityConfAtmLabelRangeTable": hh3cMplsLdpEntityConfAtmLabelRangeTable,
       "hh3cMplsLdpEntityConfAtmLabelRangeEntry": hh3cMplsLdpEntityConfAtmLabelRangeEntry,
       "hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVPI": hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVPI,
       "hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVCI": hh3cMplsLdpEntityConfAtmLabelRangeLowerBoundVCI,
       "hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVPI": hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVPI,
       "hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVCI": hh3cMplsLdpEntityConfAtmLabelRangeUpperBoundVCI,
       "hh3cMplsLdpEntityConfAtmLabelRangeRowStatus": hh3cMplsLdpEntityConfAtmLabelRangeRowStatus,
       "hh3cMplsLdpEntityStatsTable": hh3cMplsLdpEntityStatsTable,
       "hh3cMplsLdpEntityStatsEntry": hh3cMplsLdpEntityStatsEntry,
       "hh3cMplsLdpAttemptedSessions": hh3cMplsLdpAttemptedSessions,
       "hh3cMplsLdpPeerObjects": hh3cMplsLdpPeerObjects,
       "hh3cMplsLdpPeerTable": hh3cMplsLdpPeerTable,
       "hh3cMplsLdpPeerEntry": hh3cMplsLdpPeerEntry,
       "hh3cMplsLdpPeerIndex": hh3cMplsLdpPeerIndex,
       "hh3cMplsLdpPeerID": hh3cMplsLdpPeerID,
       "hh3cMplsLdpPeerInternetworkAddrType": hh3cMplsLdpPeerInternetworkAddrType,
       "hh3cMplsLdpPeerInternetworkAddr": hh3cMplsLdpPeerInternetworkAddr,
       "hh3cMplsLdpPeerDefaultMtu": hh3cMplsLdpPeerDefaultMtu,
       "hh3cMplsLdpPeerKeepAliveHoldTimer": hh3cMplsLdpPeerKeepAliveHoldTimer,
       "hh3cMplsLdpPeerLabelDistributionMethod": hh3cMplsLdpPeerLabelDistributionMethod,
       "hh3cMplsLdpPeerType": hh3cMplsLdpPeerType,
       "hh3cMplsLdpPeerRowStatus": hh3cMplsLdpPeerRowStatus,
       "hh3cMplsLdpPeerConfAtmLabelRangeTable": hh3cMplsLdpPeerConfAtmLabelRangeTable,
       "hh3cMplsLdpPeerConfAtmLabelRangeEntry": hh3cMplsLdpPeerConfAtmLabelRangeEntry,
       "hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVPI": hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVPI,
       "hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVCI": hh3cMplsLdpPeerConfAtmLabelRangeLowerBoundVCI,
       "hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVPI": hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVPI,
       "hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVCI": hh3cMplsLdpPeerConfAtmLabelRangeUpperBoundVCI,
       "hh3cMplsLdpSessionObjects": hh3cMplsLdpSessionObjects,
       "hh3cMplsLdpSessionTable": hh3cMplsLdpSessionTable,
       "hh3cMplsLdpSessionEntry": hh3cMplsLdpSessionEntry,
       "hh3cMplsLdpSessionIndex": hh3cMplsLdpSessionIndex,
       "hh3cMplsLdpSessionID": hh3cMplsLdpSessionID,
       "hh3cMplsLdpSessionProtocolVersion": hh3cMplsLdpSessionProtocolVersion,
       "hh3cMplsLdpSessionKeepAliveHoldTimeRemaining": hh3cMplsLdpSessionKeepAliveHoldTimeRemaining,
       "hh3cMplsLdpSessionRole": hh3cMplsLdpSessionRole,
       "hh3cMplsLdpSessionState": hh3cMplsLdpSessionState,
       "hh3cMplsLdpSessionAtmLabelRangeLowerBoundVPI": hh3cMplsLdpSessionAtmLabelRangeLowerBoundVPI,
       "hh3cMplsLdpSessionAtmLabelRangeLowerBoundVCI": hh3cMplsLdpSessionAtmLabelRangeLowerBoundVCI,
       "hh3cMplsLdpSessionAtmLabelRangeUpperBoundVPI": hh3cMplsLdpSessionAtmLabelRangeUpperBoundVPI,
       "hh3cMplsLdpSessionAtmLabelRangeUpperBoundVCI": hh3cMplsLdpSessionAtmLabelRangeUpperBoundVCI,
       "hh3cMplsLdpHelloAdjacencyObjects": hh3cMplsLdpHelloAdjacencyObjects,
       "hh3cMplsLdpHelloAdjacencyTable": hh3cMplsLdpHelloAdjacencyTable,
       "hh3cMplsLdpHelloAdjacencyEntry": hh3cMplsLdpHelloAdjacencyEntry,
       "hh3cMplsLdpHelloAdjacencyIndex": hh3cMplsLdpHelloAdjacencyIndex,
       "hh3cMplsLdpHelloAdjacencyHoldTimeRemaining": hh3cMplsLdpHelloAdjacencyHoldTimeRemaining,
       "hh3cMplsLdpCrlspTnlObjects": hh3cMplsLdpCrlspTnlObjects,
       "hh3cMplsLdpCrlspTnlTable": hh3cMplsLdpCrlspTnlTable,
       "hh3cMplsLdpCrlspTnlEntry": hh3cMplsLdpCrlspTnlEntry,
       "hh3cMplsLdpCrlspTnlIndex": hh3cMplsLdpCrlspTnlIndex,
       "hh3cMplsLdpCrlspTnlName": hh3cMplsLdpCrlspTnlName,
       "hh3cMplsLdpCrlspTnlDirection": hh3cMplsLdpCrlspTnlDirection,
       "hh3cMplsLdpCrlspTnlSignallingProto": hh3cMplsLdpCrlspTnlSignallingProto,
       "hh3cMplsLdpCrlspTnlSetupPrio": hh3cMplsLdpCrlspTnlSetupPrio,
       "hh3cMplsLdpCrlspTnlHoldingPrio": hh3cMplsLdpCrlspTnlHoldingPrio,
       "hh3cMplsLdpCrlspTnlPeakDataRate": hh3cMplsLdpCrlspTnlPeakDataRate,
       "hh3cMplsLdpCrlspTnlPeakBurstSize": hh3cMplsLdpCrlspTnlPeakBurstSize,
       "hh3cMplsLdpCrlspTnlCommittedDataRate": hh3cMplsLdpCrlspTnlCommittedDataRate,
       "hh3cMplsLdpCrlspTnlCommittedBurstSize": hh3cMplsLdpCrlspTnlCommittedBurstSize,
       "hh3cMplsLdpCrlspTnlExcessBurstSize": hh3cMplsLdpCrlspTnlExcessBurstSize,
       "hh3cMplsLdpCrlspTnlIsPinned": hh3cMplsLdpCrlspTnlIsPinned,
       "hh3cMplsLdpCrlspTnlFrequency": hh3cMplsLdpCrlspTnlFrequency,
       "hh3cMplsLdpCrlspTnlWeight": hh3cMplsLdpCrlspTnlWeight,
       "hh3cMplsLdpCrlspTnlRowStatus": hh3cMplsLdpCrlspTnlRowStatus,
       "hh3cMplsLdpCrlspErHopTable": hh3cMplsLdpCrlspErHopTable,
       "hh3cMplsLdpCrlspErHopEntry": hh3cMplsLdpCrlspErHopEntry,
       "hh3cMplsLdpCrlspErHopIndex": hh3cMplsLdpCrlspErHopIndex,
       "hh3cMplsLdpCrlspErHopAddrType": hh3cMplsLdpCrlspErHopAddrType,
       "hh3cMplsLdpCrlspErHopIpv4Addr": hh3cMplsLdpCrlspErHopIpv4Addr,
       "hh3cMplsLdpCrlspErHopIpv4PrefixLen": hh3cMplsLdpCrlspErHopIpv4PrefixLen,
       "hh3cMplsLdpCrlspErHopStrictOrLoose": hh3cMplsLdpCrlspErHopStrictOrLoose,
       "hh3cMplsLdpCrlspErHopRowStatus": hh3cMplsLdpCrlspErHopRowStatus,
       "hh3cMplsLdpNotifications": hh3cMplsLdpNotifications,
       "hh3cMplsLdpNotificationPrefix": hh3cMplsLdpNotificationPrefix,
       "hh3cMplsLdpFailedInitSessionThresholdExceeded": hh3cMplsLdpFailedInitSessionThresholdExceeded,
       "hh3cMplsLdpCrlspTunnelUp": hh3cMplsLdpCrlspTunnelUp,
       "hh3cMplsLdpCrlspTunnelDown": hh3cMplsLdpCrlspTunnelDown,
       "hh3cMplsLdpCrlspTunnelSetupFailure": hh3cMplsLdpCrlspTunnelSetupFailure,
       "hh3cMplsLdpIncarnUpEventFailure": hh3cMplsLdpIncarnUpEventFailure,
       "hh3cMplsLdpIncarnDownEventFailure": hh3cMplsLdpIncarnDownEventFailure,
       "hh3cMplsLdpEntityUpEventFailure": hh3cMplsLdpEntityUpEventFailure,
       "hh3cMplsLdpEntityDownEventFailure": hh3cMplsLdpEntityDownEventFailure,
       "hh3cMplsLdpSessionUpEventFailure": hh3cMplsLdpSessionUpEventFailure,
       "hh3cMplsLdpSessionDownEventFailure": hh3cMplsLdpSessionDownEventFailure}
)
