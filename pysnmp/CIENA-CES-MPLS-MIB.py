# SNMP MIB module (CIENA-CES-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-MPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:02 2024
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(MplsBitRate,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsBitRate")

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
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cienaCesMplsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18)
)
cienaCesMplsMIB.setRevisions(
        ("2016-11-22 00:00",
         "2016-11-17 00:00",
         "2016-10-21 00:00",
         "2016-10-12 00:00",
         "2016-09-21 00:00",
         "2016-08-29 00:00",
         "2016-08-22 00:00",
         "2016-07-18 00:00",
         "2016-07-12 00:00",
         "2016-07-11 00:00",
         "2016-07-04 00:00",
         "2016-06-10 00:00",
         "2016-03-11 00:00",
         "2016-02-15 00:00",
         "2016-01-04 00:00",
         "2015-08-18 00:00",
         "2015-02-23 00:00",
         "2014-12-01 00:00",
         "2014-11-04 00:00",
         "2014-06-11 00:00",
         "2014-04-08 00:00",
         "2014-02-28 00:00",
         "2013-09-27 00:00",
         "2013-05-08 00:00",
         "2011-02-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TTLPolicy(Integer32, TextualConvention):
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
        *(("decrement", 0),
          ("fixed", 1),
          ("inherit", 2))
    )



class PseudoWireType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("raw", 1),
          ("tagged", 2))
    )



class RCosPolicy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exp-mapped", 2),
          ("fixed", 1))
    )



class FCosPolicy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("rcos-mapped", 2))
    )



class PrivateForwardGroup(Integer32, TextualConvention):
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
        *(("groupA", 1),
          ("groupB", 2),
          ("groupC", 3))
    )



class OperState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capable", 1),
          ("not-capable", 2))
    )



class VCFailReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 2),
          ("indeterminate", 1))
    )



class VCStatus(Bits, TextualConvention):
    status = "current"


class VCState(Integer32, TextualConvention):
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
          ("notActive", 2))
    )



class AttachGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )



class TunnelType(Integer32, TextualConvention):
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
        *(("gmplsAssociated", 8),
          ("gmplsDynamicEgressCorouted", 7),
          ("gmplsDynamicIngressCorouted", 5),
          ("gmplsStaticEgressCorouted", 6),
          ("gmplsStaticIngressCorouted", 4),
          ("mplsAssociated", 3),
          ("mplsDynamicIngress", 2),
          ("mplsStaticIngress", 1))
    )



class TunnelAisFault(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("nofault", 2))
    )



class TunnelOamFault(Integer32, TextualConvention):
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
        *(("aisbfdfault", 3),
          ("aisfault", 1),
          ("bfdfault", 2),
          ("nofault", 4))
    )



class AutoSizeFailHdlr(Integer32, TextualConvention):
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
        *(("alarm", 2),
          ("mbb", 3),
          ("none", 1),
          ("notApplicable", 4))
    )



class AutoSizeState(Integer32, TextualConvention):
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
        *(("downsizeFailed", 5),
          ("downsizeInProgress", 4),
          ("notApplicable", 6),
          ("ok", 1),
          ("upsizeFailed", 3),
          ("upsizeInProgress", 2))
    )



class AutoSizeMode(Integer32, TextualConvention):
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
        *(("cac", 2),
          ("none", 1),
          ("notApplicable", 4),
          ("utilization", 3))
    )



class CacPolicy(Integer32, TextualConvention):
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
        *(("invalid", 1),
          ("mam", 2),
          ("rdm", 3))
    )



class PathDisjointType(Integer32, TextualConvention):
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
        *(("link", 3),
          ("node", 5),
          ("none", 2),
          ("notApplicable", 8),
          ("srlg", 4),
          ("srlgAndNode", 6),
          ("srlgOrNode", 7),
          ("unknown", 1))
    )



class PathDisjointMode(Integer32, TextualConvention):
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
        *(("maximal", 3),
          ("none", 1),
          ("notApplicable", 4),
          ("strict", 2))
    )



class SRLGState(Integer32, TextualConvention):
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
          ("inActive", 2))
    )



class TEMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diffServ", 1),
          ("diffServ-Te", 2))
    )



class MplsGlobalState(Integer32, TextualConvention):
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
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesMplsMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesMplsMIBObjects = _CienaCesMplsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1)
)
_CienaCesMpls_ObjectIdentity = ObjectIdentity
cienaCesMpls = _CienaCesMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1)
)
_CienaCesMplsGlobalAttrs_ObjectIdentity = ObjectIdentity
cienaCesMplsGlobalAttrs = _CienaCesMplsGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 1)
)


class _CienaCesMplsStaticAdminLabelRangeStart_Type(Integer32):
    """Custom type cienaCesMplsStaticAdminLabelRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsStaticAdminLabelRangeStart_Type.__name__ = "Integer32"
_CienaCesMplsStaticAdminLabelRangeStart_Object = MibScalar
cienaCesMplsStaticAdminLabelRangeStart = _CienaCesMplsStaticAdminLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 1, 1),
    _CienaCesMplsStaticAdminLabelRangeStart_Type()
)
cienaCesMplsStaticAdminLabelRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticAdminLabelRangeStart.setStatus("deprecated")


class _CienaCesMplsStaticAdminLabelRangeEnd_Type(Integer32):
    """Custom type cienaCesMplsStaticAdminLabelRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsStaticAdminLabelRangeEnd_Type.__name__ = "Integer32"
_CienaCesMplsStaticAdminLabelRangeEnd_Object = MibScalar
cienaCesMplsStaticAdminLabelRangeEnd = _CienaCesMplsStaticAdminLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 1, 2),
    _CienaCesMplsStaticAdminLabelRangeEnd_Type()
)
cienaCesMplsStaticAdminLabelRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticAdminLabelRangeEnd.setStatus("deprecated")


class _CienaCesMplsStaticOperLabelRangeStart_Type(Integer32):
    """Custom type cienaCesMplsStaticOperLabelRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsStaticOperLabelRangeStart_Type.__name__ = "Integer32"
_CienaCesMplsStaticOperLabelRangeStart_Object = MibScalar
cienaCesMplsStaticOperLabelRangeStart = _CienaCesMplsStaticOperLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 1, 3),
    _CienaCesMplsStaticOperLabelRangeStart_Type()
)
cienaCesMplsStaticOperLabelRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticOperLabelRangeStart.setStatus("deprecated")


class _CienaCesMplsStaticOperLabelRangeEnd_Type(Integer32):
    """Custom type cienaCesMplsStaticOperLabelRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsStaticOperLabelRangeEnd_Type.__name__ = "Integer32"
_CienaCesMplsStaticOperLabelRangeEnd_Object = MibScalar
cienaCesMplsStaticOperLabelRangeEnd = _CienaCesMplsStaticOperLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 1, 4),
    _CienaCesMplsStaticOperLabelRangeEnd_Type()
)
cienaCesMplsStaticOperLabelRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticOperLabelRangeEnd.setStatus("deprecated")


class _CienaCesMplsDynamicAdminLabelRangeStart_Type(Integer32):
    """Custom type cienaCesMplsDynamicAdminLabelRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsDynamicAdminLabelRangeStart_Type.__name__ = "Integer32"
_CienaCesMplsDynamicAdminLabelRangeStart_Object = MibScalar
cienaCesMplsDynamicAdminLabelRangeStart = _CienaCesMplsDynamicAdminLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 1, 5),
    _CienaCesMplsDynamicAdminLabelRangeStart_Type()
)
cienaCesMplsDynamicAdminLabelRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicAdminLabelRangeStart.setStatus("deprecated")


class _CienaCesMplsDynamicAdminLabelRangeEnd_Type(Integer32):
    """Custom type cienaCesMplsDynamicAdminLabelRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsDynamicAdminLabelRangeEnd_Type.__name__ = "Integer32"
_CienaCesMplsDynamicAdminLabelRangeEnd_Object = MibScalar
cienaCesMplsDynamicAdminLabelRangeEnd = _CienaCesMplsDynamicAdminLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 1, 6),
    _CienaCesMplsDynamicAdminLabelRangeEnd_Type()
)
cienaCesMplsDynamicAdminLabelRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicAdminLabelRangeEnd.setStatus("deprecated")


class _CienaCesMplsDynamicOperLabelRangeStart_Type(Integer32):
    """Custom type cienaCesMplsDynamicOperLabelRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsDynamicOperLabelRangeStart_Type.__name__ = "Integer32"
_CienaCesMplsDynamicOperLabelRangeStart_Object = MibScalar
cienaCesMplsDynamicOperLabelRangeStart = _CienaCesMplsDynamicOperLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 1, 7),
    _CienaCesMplsDynamicOperLabelRangeStart_Type()
)
cienaCesMplsDynamicOperLabelRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicOperLabelRangeStart.setStatus("deprecated")


class _CienaCesMplsDynamicOperLabelRangeEnd_Type(Integer32):
    """Custom type cienaCesMplsDynamicOperLabelRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsDynamicOperLabelRangeEnd_Type.__name__ = "Integer32"
_CienaCesMplsDynamicOperLabelRangeEnd_Object = MibScalar
cienaCesMplsDynamicOperLabelRangeEnd = _CienaCesMplsDynamicOperLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 1, 8),
    _CienaCesMplsDynamicOperLabelRangeEnd_Type()
)
cienaCesMplsDynamicOperLabelRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicOperLabelRangeEnd.setStatus("deprecated")
_CienaCesMplsStaticIngressTunnelTable_Object = MibTable
cienaCesMplsStaticIngressTunnelTable = _CienaCesMplsStaticIngressTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelTable.setStatus("current")
_CienaCesMplsStaticIngressTunnelEntry_Object = MibTableRow
cienaCesMplsStaticIngressTunnelEntry = _CienaCesMplsStaticIngressTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1)
)
cienaCesMplsStaticIngressTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsStaticIngressTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelEntry.setStatus("current")


class _CienaCesMplsStaticIngressTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesMplsStaticIngressTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsStaticIngressTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsStaticIngressTunnelIndex_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelIndex = _CienaCesMplsStaticIngressTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 1),
    _CienaCesMplsStaticIngressTunnelIndex_Type()
)
cienaCesMplsStaticIngressTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelIndex.setStatus("current")


class _CienaCesMplsStaticIngressTunnelName_Type(DisplayString):
    """Custom type cienaCesMplsStaticIngressTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsStaticIngressTunnelName_Type.__name__ = "DisplayString"
_CienaCesMplsStaticIngressTunnelName_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelName = _CienaCesMplsStaticIngressTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 2),
    _CienaCesMplsStaticIngressTunnelName_Type()
)
cienaCesMplsStaticIngressTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelName.setStatus("current")


class _CienaCesMplsStaticIngressTunnelWeight_Type(Integer32):
    """Custom type cienaCesMplsStaticIngressTunnelWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesMplsStaticIngressTunnelWeight_Type.__name__ = "Integer32"
_CienaCesMplsStaticIngressTunnelWeight_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelWeight = _CienaCesMplsStaticIngressTunnelWeight_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 3),
    _CienaCesMplsStaticIngressTunnelWeight_Type()
)
cienaCesMplsStaticIngressTunnelWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelWeight.setStatus("current")
_CienaCesMplsStaticIngressTunnelNextHopIp_Type = IpAddress
_CienaCesMplsStaticIngressTunnelNextHopIp_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelNextHopIp = _CienaCesMplsStaticIngressTunnelNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 4),
    _CienaCesMplsStaticIngressTunnelNextHopIp_Type()
)
cienaCesMplsStaticIngressTunnelNextHopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelNextHopIp.setStatus("current")
_CienaCesMplsStaticIngressTunnelAdminState_Type = CienaGlobalState
_CienaCesMplsStaticIngressTunnelAdminState_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelAdminState = _CienaCesMplsStaticIngressTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 5),
    _CienaCesMplsStaticIngressTunnelAdminState_Type()
)
cienaCesMplsStaticIngressTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelAdminState.setStatus("current")
_CienaCesMplsStaticIngressTunnelOperState_Type = CienaGlobalState
_CienaCesMplsStaticIngressTunnelOperState_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelOperState = _CienaCesMplsStaticIngressTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 6),
    _CienaCesMplsStaticIngressTunnelOperState_Type()
)
cienaCesMplsStaticIngressTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelOperState.setStatus("current")
_CienaCesMplsStaticIngressTunnelDestIpAddr_Type = IpAddress
_CienaCesMplsStaticIngressTunnelDestIpAddr_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelDestIpAddr = _CienaCesMplsStaticIngressTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 7),
    _CienaCesMplsStaticIngressTunnelDestIpAddr_Type()
)
cienaCesMplsStaticIngressTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelDestIpAddr.setStatus("current")


class _CienaCesMplsStaticIngressTunnelLabel_Type(Integer32):
    """Custom type cienaCesMplsStaticIngressTunnelLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesMplsStaticIngressTunnelLabel_Type.__name__ = "Integer32"
_CienaCesMplsStaticIngressTunnelLabel_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelLabel = _CienaCesMplsStaticIngressTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 8),
    _CienaCesMplsStaticIngressTunnelLabel_Type()
)
cienaCesMplsStaticIngressTunnelLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelLabel.setStatus("current")


class _CienaCesMplsStaticIngressTunnelFrmCosPolicy_Type(FCosPolicy):
    """Custom type cienaCesMplsStaticIngressTunnelFrmCosPolicy based on FCosPolicy"""


_CienaCesMplsStaticIngressTunnelFrmCosPolicy_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelFrmCosPolicy = _CienaCesMplsStaticIngressTunnelFrmCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 9),
    _CienaCesMplsStaticIngressTunnelFrmCosPolicy_Type()
)
cienaCesMplsStaticIngressTunnelFrmCosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelFrmCosPolicy.setStatus("deprecated")


class _CienaCesMplsStaticIngressTunnelFrmCosMapId_Type(Integer32):
    """Custom type cienaCesMplsStaticIngressTunnelFrmCosMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsStaticIngressTunnelFrmCosMapId_Type.__name__ = "Integer32"
_CienaCesMplsStaticIngressTunnelFrmCosMapId_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelFrmCosMapId = _CienaCesMplsStaticIngressTunnelFrmCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 10),
    _CienaCesMplsStaticIngressTunnelFrmCosMapId_Type()
)
cienaCesMplsStaticIngressTunnelFrmCosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelFrmCosMapId.setStatus("deprecated")


class _CienaCesMplsStaticIngressTunnelFixedExp_Type(Unsigned32):
    """Custom type cienaCesMplsStaticIngressTunnelFixedExp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMplsStaticIngressTunnelFixedExp_Type.__name__ = "Unsigned32"
_CienaCesMplsStaticIngressTunnelFixedExp_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelFixedExp = _CienaCesMplsStaticIngressTunnelFixedExp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 11),
    _CienaCesMplsStaticIngressTunnelFixedExp_Type()
)
cienaCesMplsStaticIngressTunnelFixedExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelFixedExp.setStatus("deprecated")


class _CienaCesMplsStaticIngressTunnelTTLPolicy_Type(TTLPolicy):
    """Custom type cienaCesMplsStaticIngressTunnelTTLPolicy based on TTLPolicy"""


_CienaCesMplsStaticIngressTunnelTTLPolicy_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelTTLPolicy = _CienaCesMplsStaticIngressTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 12),
    _CienaCesMplsStaticIngressTunnelTTLPolicy_Type()
)
cienaCesMplsStaticIngressTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelTTLPolicy.setStatus("current")


class _CienaCesMplsStaticIngressTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesMplsStaticIngressTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesMplsStaticIngressTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesMplsStaticIngressTunnelFixedTTL_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelFixedTTL = _CienaCesMplsStaticIngressTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 13),
    _CienaCesMplsStaticIngressTunnelFixedTTL_Type()
)
cienaCesMplsStaticIngressTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelFixedTTL.setStatus("current")
_CienaCesMplsStaticIngressTunnelGrpIndex_Type = Unsigned32
_CienaCesMplsStaticIngressTunnelGrpIndex_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelGrpIndex = _CienaCesMplsStaticIngressTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 14),
    _CienaCesMplsStaticIngressTunnelGrpIndex_Type()
)
cienaCesMplsStaticIngressTunnelGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelGrpIndex.setStatus("current")


class _CienaCesMplsStaticIngressTunnelReversion_Type(Integer32):
    """Custom type cienaCesMplsStaticIngressTunnelReversion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesMplsStaticIngressTunnelReversion_Type.__name__ = "Integer32"
_CienaCesMplsStaticIngressTunnelReversion_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelReversion = _CienaCesMplsStaticIngressTunnelReversion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 16),
    _CienaCesMplsStaticIngressTunnelReversion_Type()
)
cienaCesMplsStaticIngressTunnelReversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelReversion.setStatus("current")


class _CienaCesMplsStaticIngressTunnelReversionTimeout_Type(Integer32):
    """Custom type cienaCesMplsStaticIngressTunnelReversionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsStaticIngressTunnelReversionTimeout_Type.__name__ = "Integer32"
_CienaCesMplsStaticIngressTunnelReversionTimeout_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelReversionTimeout = _CienaCesMplsStaticIngressTunnelReversionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 17),
    _CienaCesMplsStaticIngressTunnelReversionTimeout_Type()
)
cienaCesMplsStaticIngressTunnelReversionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelReversionTimeout.setStatus("current")
_CienaCesMplsStaticIngressTunnelPrimaryTunnelName_Type = DisplayString
_CienaCesMplsStaticIngressTunnelPrimaryTunnelName_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelPrimaryTunnelName = _CienaCesMplsStaticIngressTunnelPrimaryTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 18),
    _CienaCesMplsStaticIngressTunnelPrimaryTunnelName_Type()
)
cienaCesMplsStaticIngressTunnelPrimaryTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelPrimaryTunnelName.setStatus("deprecated")


class _CienaCesMplsStaticIngressTunnelFixedTC_Type(Unsigned32):
    """Custom type cienaCesMplsStaticIngressTunnelFixedTC based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMplsStaticIngressTunnelFixedTC_Type.__name__ = "Unsigned32"
_CienaCesMplsStaticIngressTunnelFixedTC_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelFixedTC = _CienaCesMplsStaticIngressTunnelFixedTC_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 19),
    _CienaCesMplsStaticIngressTunnelFixedTC_Type()
)
cienaCesMplsStaticIngressTunnelFixedTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelFixedTC.setStatus("deprecated")


class _CienaCesMplsStaticIngressTunnelProtectionRole_Type(Integer32):
    """Custom type cienaCesMplsStaticIngressTunnelProtectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 0),
          ("primary", 1))
    )


_CienaCesMplsStaticIngressTunnelProtectionRole_Type.__name__ = "Integer32"
_CienaCesMplsStaticIngressTunnelProtectionRole_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelProtectionRole = _CienaCesMplsStaticIngressTunnelProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 20),
    _CienaCesMplsStaticIngressTunnelProtectionRole_Type()
)
cienaCesMplsStaticIngressTunnelProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelProtectionRole.setStatus("current")


class _CienaCesMplsStaticIngressTunnelProtectionState_Type(Integer32):
    """Custom type cienaCesMplsStaticIngressTunnelProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 0))
    )


_CienaCesMplsStaticIngressTunnelProtectionState_Type.__name__ = "Integer32"
_CienaCesMplsStaticIngressTunnelProtectionState_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelProtectionState = _CienaCesMplsStaticIngressTunnelProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 21),
    _CienaCesMplsStaticIngressTunnelProtectionState_Type()
)
cienaCesMplsStaticIngressTunnelProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelProtectionState.setStatus("current")
_CienaCesMplsStaticIngressTunnelProtectionPartnerName_Type = DisplayString
_CienaCesMplsStaticIngressTunnelProtectionPartnerName_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelProtectionPartnerName = _CienaCesMplsStaticIngressTunnelProtectionPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 22),
    _CienaCesMplsStaticIngressTunnelProtectionPartnerName_Type()
)
cienaCesMplsStaticIngressTunnelProtectionPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelProtectionPartnerName.setStatus("current")


class _CienaCesMplsStaticIngressTunnelCosProfileIndex_Type(Integer32):
    """Custom type cienaCesMplsStaticIngressTunnelCosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsStaticIngressTunnelCosProfileIndex_Type.__name__ = "Integer32"
_CienaCesMplsStaticIngressTunnelCosProfileIndex_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelCosProfileIndex = _CienaCesMplsStaticIngressTunnelCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 23),
    _CienaCesMplsStaticIngressTunnelCosProfileIndex_Type()
)
cienaCesMplsStaticIngressTunnelCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelCosProfileIndex.setStatus("current")
_CienaCesMplsStaticIngressTunnelCosProfileName_Type = DisplayString
_CienaCesMplsStaticIngressTunnelCosProfileName_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelCosProfileName = _CienaCesMplsStaticIngressTunnelCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 24),
    _CienaCesMplsStaticIngressTunnelCosProfileName_Type()
)
cienaCesMplsStaticIngressTunnelCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelCosProfileName.setStatus("current")


class _CienaCesMplsStaticIngressTunnelRecoveryDisjoint_Type(Integer32):
    """Custom type cienaCesMplsStaticIngressTunnelRecoveryDisjoint based on Integer32"""
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
        *(("link", 2),
          ("node", 3),
          ("none", 1),
          ("srlg", 4),
          ("unknown", 5))
    )


_CienaCesMplsStaticIngressTunnelRecoveryDisjoint_Type.__name__ = "Integer32"
_CienaCesMplsStaticIngressTunnelRecoveryDisjoint_Object = MibTableColumn
cienaCesMplsStaticIngressTunnelRecoveryDisjoint = _CienaCesMplsStaticIngressTunnelRecoveryDisjoint_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 2, 1, 25),
    _CienaCesMplsStaticIngressTunnelRecoveryDisjoint_Type()
)
cienaCesMplsStaticIngressTunnelRecoveryDisjoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticIngressTunnelRecoveryDisjoint.setStatus("current")
_CienaCesMplsDynamicIngressTunnelTable_Object = MibTable
cienaCesMplsDynamicIngressTunnelTable = _CienaCesMplsDynamicIngressTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelTable.setStatus("current")
_CienaCesMplsDynamicIngressTunnelEntry_Object = MibTableRow
cienaCesMplsDynamicIngressTunnelEntry = _CienaCesMplsDynamicIngressTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1)
)
cienaCesMplsDynamicIngressTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsDynamicIngressTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelEntry.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesMplsDynamicIngressTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsDynamicIngressTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsDynamicIngressTunnelIndex_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelIndex = _CienaCesMplsDynamicIngressTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 1),
    _CienaCesMplsDynamicIngressTunnelIndex_Type()
)
cienaCesMplsDynamicIngressTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelIndex.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelName_Type(DisplayString):
    """Custom type cienaCesMplsDynamicIngressTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsDynamicIngressTunnelName_Type.__name__ = "DisplayString"
_CienaCesMplsDynamicIngressTunnelName_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelName = _CienaCesMplsDynamicIngressTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 2),
    _CienaCesMplsDynamicIngressTunnelName_Type()
)
cienaCesMplsDynamicIngressTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelName.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelWeight_Type(Integer32):
    """Custom type cienaCesMplsDynamicIngressTunnelWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesMplsDynamicIngressTunnelWeight_Type.__name__ = "Integer32"
_CienaCesMplsDynamicIngressTunnelWeight_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelWeight = _CienaCesMplsDynamicIngressTunnelWeight_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 3),
    _CienaCesMplsDynamicIngressTunnelWeight_Type()
)
cienaCesMplsDynamicIngressTunnelWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelWeight.setStatus("current")
_CienaCesMplsDynamicIngressTunnelLspId_Type = Unsigned32
_CienaCesMplsDynamicIngressTunnelLspId_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelLspId = _CienaCesMplsDynamicIngressTunnelLspId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 4),
    _CienaCesMplsDynamicIngressTunnelLspId_Type()
)
cienaCesMplsDynamicIngressTunnelLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelLspId.setStatus("current")
_CienaCesMplsDynamicIngressTunnelNextHopIp_Type = IpAddress
_CienaCesMplsDynamicIngressTunnelNextHopIp_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelNextHopIp = _CienaCesMplsDynamicIngressTunnelNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 5),
    _CienaCesMplsDynamicIngressTunnelNextHopIp_Type()
)
cienaCesMplsDynamicIngressTunnelNextHopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelNextHopIp.setStatus("current")
_CienaCesMplsDynamicIngressTunnelAdminState_Type = CienaGlobalState
_CienaCesMplsDynamicIngressTunnelAdminState_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelAdminState = _CienaCesMplsDynamicIngressTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 6),
    _CienaCesMplsDynamicIngressTunnelAdminState_Type()
)
cienaCesMplsDynamicIngressTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelAdminState.setStatus("current")
_CienaCesMplsDynamicIngressTunnelOperState_Type = CienaGlobalState
_CienaCesMplsDynamicIngressTunnelOperState_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelOperState = _CienaCesMplsDynamicIngressTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 7),
    _CienaCesMplsDynamicIngressTunnelOperState_Type()
)
cienaCesMplsDynamicIngressTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelOperState.setStatus("current")
_CienaCesMplsDynamicIngressTunnelDestIpAddr_Type = IpAddress
_CienaCesMplsDynamicIngressTunnelDestIpAddr_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelDestIpAddr = _CienaCesMplsDynamicIngressTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 8),
    _CienaCesMplsDynamicIngressTunnelDestIpAddr_Type()
)
cienaCesMplsDynamicIngressTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelDestIpAddr.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelLabel_Type(Integer32):
    """Custom type cienaCesMplsDynamicIngressTunnelLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1048575),
    )


_CienaCesMplsDynamicIngressTunnelLabel_Type.__name__ = "Integer32"
_CienaCesMplsDynamicIngressTunnelLabel_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelLabel = _CienaCesMplsDynamicIngressTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 9),
    _CienaCesMplsDynamicIngressTunnelLabel_Type()
)
cienaCesMplsDynamicIngressTunnelLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelLabel.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelFrmCosPolicy_Type(Integer32):
    """Custom type cienaCesMplsDynamicIngressTunnelFrmCosPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("rcos-mapped", 2))
    )


_CienaCesMplsDynamicIngressTunnelFrmCosPolicy_Type.__name__ = "Integer32"
_CienaCesMplsDynamicIngressTunnelFrmCosPolicy_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelFrmCosPolicy = _CienaCesMplsDynamicIngressTunnelFrmCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 10),
    _CienaCesMplsDynamicIngressTunnelFrmCosPolicy_Type()
)
cienaCesMplsDynamicIngressTunnelFrmCosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelFrmCosPolicy.setStatus("deprecated")


class _CienaCesMplsDynamicIngressTunnelFrmCosMapId_Type(Integer32):
    """Custom type cienaCesMplsDynamicIngressTunnelFrmCosMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsDynamicIngressTunnelFrmCosMapId_Type.__name__ = "Integer32"
_CienaCesMplsDynamicIngressTunnelFrmCosMapId_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelFrmCosMapId = _CienaCesMplsDynamicIngressTunnelFrmCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 11),
    _CienaCesMplsDynamicIngressTunnelFrmCosMapId_Type()
)
cienaCesMplsDynamicIngressTunnelFrmCosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelFrmCosMapId.setStatus("deprecated")


class _CienaCesMplsDynamicIngressTunnelFixedExp_Type(Unsigned32):
    """Custom type cienaCesMplsDynamicIngressTunnelFixedExp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMplsDynamicIngressTunnelFixedExp_Type.__name__ = "Unsigned32"
_CienaCesMplsDynamicIngressTunnelFixedExp_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelFixedExp = _CienaCesMplsDynamicIngressTunnelFixedExp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 12),
    _CienaCesMplsDynamicIngressTunnelFixedExp_Type()
)
cienaCesMplsDynamicIngressTunnelFixedExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelFixedExp.setStatus("deprecated")


class _CienaCesMplsDynamicIngressTunnelSetupPriority_Type(Unsigned32):
    """Custom type cienaCesMplsDynamicIngressTunnelSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMplsDynamicIngressTunnelSetupPriority_Type.__name__ = "Unsigned32"
_CienaCesMplsDynamicIngressTunnelSetupPriority_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelSetupPriority = _CienaCesMplsDynamicIngressTunnelSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 13),
    _CienaCesMplsDynamicIngressTunnelSetupPriority_Type()
)
cienaCesMplsDynamicIngressTunnelSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelSetupPriority.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelHoldPriority_Type(Unsigned32):
    """Custom type cienaCesMplsDynamicIngressTunnelHoldPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMplsDynamicIngressTunnelHoldPriority_Type.__name__ = "Unsigned32"
_CienaCesMplsDynamicIngressTunnelHoldPriority_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelHoldPriority = _CienaCesMplsDynamicIngressTunnelHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 14),
    _CienaCesMplsDynamicIngressTunnelHoldPriority_Type()
)
cienaCesMplsDynamicIngressTunnelHoldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelHoldPriority.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelRecordRoute_Type(Integer32):
    """Custom type cienaCesMplsDynamicIngressTunnelRecordRoute based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesMplsDynamicIngressTunnelRecordRoute_Type.__name__ = "Integer32"
_CienaCesMplsDynamicIngressTunnelRecordRoute_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelRecordRoute = _CienaCesMplsDynamicIngressTunnelRecordRoute_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 15),
    _CienaCesMplsDynamicIngressTunnelRecordRoute_Type()
)
cienaCesMplsDynamicIngressTunnelRecordRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelRecordRoute.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelFastRoute_Type(Integer32):
    """Custom type cienaCesMplsDynamicIngressTunnelFastRoute based on Integer32"""
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
        *(("link-protect", 2),
          ("node-protect", 3),
          ("none", 1))
    )


_CienaCesMplsDynamicIngressTunnelFastRoute_Type.__name__ = "Integer32"
_CienaCesMplsDynamicIngressTunnelFastRoute_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelFastRoute = _CienaCesMplsDynamicIngressTunnelFastRoute_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 16),
    _CienaCesMplsDynamicIngressTunnelFastRoute_Type()
)
cienaCesMplsDynamicIngressTunnelFastRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelFastRoute.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelTTLPolicy_Type(Integer32):
    """Custom type cienaCesMplsDynamicIngressTunnelTTLPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("inherit", 2))
    )


_CienaCesMplsDynamicIngressTunnelTTLPolicy_Type.__name__ = "Integer32"
_CienaCesMplsDynamicIngressTunnelTTLPolicy_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelTTLPolicy = _CienaCesMplsDynamicIngressTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 17),
    _CienaCesMplsDynamicIngressTunnelTTLPolicy_Type()
)
cienaCesMplsDynamicIngressTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelTTLPolicy.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesMplsDynamicIngressTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesMplsDynamicIngressTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesMplsDynamicIngressTunnelFixedTTL_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelFixedTTL = _CienaCesMplsDynamicIngressTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 18),
    _CienaCesMplsDynamicIngressTunnelFixedTTL_Type()
)
cienaCesMplsDynamicIngressTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelFixedTTL.setStatus("current")
_CienaCesMplsDynamicIngressTunnelPathIndex_Type = Unsigned32
_CienaCesMplsDynamicIngressTunnelPathIndex_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelPathIndex = _CienaCesMplsDynamicIngressTunnelPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 19),
    _CienaCesMplsDynamicIngressTunnelPathIndex_Type()
)
cienaCesMplsDynamicIngressTunnelPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelPathIndex.setStatus("current")
_CienaCesMplsDynamicIngressTunnelPathName_Type = DisplayString
_CienaCesMplsDynamicIngressTunnelPathName_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelPathName = _CienaCesMplsDynamicIngressTunnelPathName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 20),
    _CienaCesMplsDynamicIngressTunnelPathName_Type()
)
cienaCesMplsDynamicIngressTunnelPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelPathName.setStatus("current")
_CienaCesMplsDynamicIngressTunnelGrpIndex_Type = Unsigned32
_CienaCesMplsDynamicIngressTunnelGrpIndex_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelGrpIndex = _CienaCesMplsDynamicIngressTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 21),
    _CienaCesMplsDynamicIngressTunnelGrpIndex_Type()
)
cienaCesMplsDynamicIngressTunnelGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelGrpIndex.setStatus("current")
_CienaCesMplsDynamicIngressTunnelResourcePointer_Type = RowPointer
_CienaCesMplsDynamicIngressTunnelResourcePointer_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelResourcePointer = _CienaCesMplsDynamicIngressTunnelResourcePointer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 23),
    _CienaCesMplsDynamicIngressTunnelResourcePointer_Type()
)
cienaCesMplsDynamicIngressTunnelResourcePointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelResourcePointer.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelReversion_Type(Integer32):
    """Custom type cienaCesMplsDynamicIngressTunnelReversion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesMplsDynamicIngressTunnelReversion_Type.__name__ = "Integer32"
_CienaCesMplsDynamicIngressTunnelReversion_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelReversion = _CienaCesMplsDynamicIngressTunnelReversion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 24),
    _CienaCesMplsDynamicIngressTunnelReversion_Type()
)
cienaCesMplsDynamicIngressTunnelReversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelReversion.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelReversionTimeout_Type(Integer32):
    """Custom type cienaCesMplsDynamicIngressTunnelReversionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsDynamicIngressTunnelReversionTimeout_Type.__name__ = "Integer32"
_CienaCesMplsDynamicIngressTunnelReversionTimeout_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelReversionTimeout = _CienaCesMplsDynamicIngressTunnelReversionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 25),
    _CienaCesMplsDynamicIngressTunnelReversionTimeout_Type()
)
cienaCesMplsDynamicIngressTunnelReversionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelReversionTimeout.setStatus("current")
_CienaCesMplsDynamicIngressTunnelBandwidthProfile_Type = DisplayString
_CienaCesMplsDynamicIngressTunnelBandwidthProfile_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelBandwidthProfile = _CienaCesMplsDynamicIngressTunnelBandwidthProfile_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 26),
    _CienaCesMplsDynamicIngressTunnelBandwidthProfile_Type()
)
cienaCesMplsDynamicIngressTunnelBandwidthProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelBandwidthProfile.setStatus("current")
_CienaCesMplsDynamicIngressTunnelPrimaryTunnelName_Type = DisplayString
_CienaCesMplsDynamicIngressTunnelPrimaryTunnelName_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelPrimaryTunnelName = _CienaCesMplsDynamicIngressTunnelPrimaryTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 27),
    _CienaCesMplsDynamicIngressTunnelPrimaryTunnelName_Type()
)
cienaCesMplsDynamicIngressTunnelPrimaryTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelPrimaryTunnelName.setStatus("deprecated")


class _CienaCesMplsDynamicIngressTunnelFixedTC_Type(Unsigned32):
    """Custom type cienaCesMplsDynamicIngressTunnelFixedTC based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMplsDynamicIngressTunnelFixedTC_Type.__name__ = "Unsigned32"
_CienaCesMplsDynamicIngressTunnelFixedTC_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelFixedTC = _CienaCesMplsDynamicIngressTunnelFixedTC_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 28),
    _CienaCesMplsDynamicIngressTunnelFixedTC_Type()
)
cienaCesMplsDynamicIngressTunnelFixedTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelFixedTC.setStatus("deprecated")


class _CienaCesMplsDynamicIngressTunnelProtectionRole_Type(Integer32):
    """Custom type cienaCesMplsDynamicIngressTunnelProtectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 0),
          ("primary", 1))
    )


_CienaCesMplsDynamicIngressTunnelProtectionRole_Type.__name__ = "Integer32"
_CienaCesMplsDynamicIngressTunnelProtectionRole_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelProtectionRole = _CienaCesMplsDynamicIngressTunnelProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 29),
    _CienaCesMplsDynamicIngressTunnelProtectionRole_Type()
)
cienaCesMplsDynamicIngressTunnelProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelProtectionRole.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelProtectionState_Type(Integer32):
    """Custom type cienaCesMplsDynamicIngressTunnelProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 0))
    )


_CienaCesMplsDynamicIngressTunnelProtectionState_Type.__name__ = "Integer32"
_CienaCesMplsDynamicIngressTunnelProtectionState_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelProtectionState = _CienaCesMplsDynamicIngressTunnelProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 30),
    _CienaCesMplsDynamicIngressTunnelProtectionState_Type()
)
cienaCesMplsDynamicIngressTunnelProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelProtectionState.setStatus("current")
_CienaCesMplsDynamicIngressTunnelProtectionPartnerName_Type = DisplayString
_CienaCesMplsDynamicIngressTunnelProtectionPartnerName_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelProtectionPartnerName = _CienaCesMplsDynamicIngressTunnelProtectionPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 31),
    _CienaCesMplsDynamicIngressTunnelProtectionPartnerName_Type()
)
cienaCesMplsDynamicIngressTunnelProtectionPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelProtectionPartnerName.setStatus("current")


class _CienaCesMplsDynamicIngressTunnelCosProfileIndex_Type(Integer32):
    """Custom type cienaCesMplsDynamicIngressTunnelCosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsDynamicIngressTunnelCosProfileIndex_Type.__name__ = "Integer32"
_CienaCesMplsDynamicIngressTunnelCosProfileIndex_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelCosProfileIndex = _CienaCesMplsDynamicIngressTunnelCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 32),
    _CienaCesMplsDynamicIngressTunnelCosProfileIndex_Type()
)
cienaCesMplsDynamicIngressTunnelCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelCosProfileIndex.setStatus("current")
_CienaCesMplsDynamicIngressTunnelCosProfileName_Type = DisplayString
_CienaCesMplsDynamicIngressTunnelCosProfileName_Object = MibTableColumn
cienaCesMplsDynamicIngressTunnelCosProfileName = _CienaCesMplsDynamicIngressTunnelCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 3, 1, 33),
    _CienaCesMplsDynamicIngressTunnelCosProfileName_Type()
)
cienaCesMplsDynamicIngressTunnelCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressTunnelCosProfileName.setStatus("current")
_CienaCesMplsStaticEgressTunnelTable_Object = MibTable
cienaCesMplsStaticEgressTunnelTable = _CienaCesMplsStaticEgressTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cienaCesMplsStaticEgressTunnelTable.setStatus("current")
_CienaCesMplsStaticEgressTunnelEntry_Object = MibTableRow
cienaCesMplsStaticEgressTunnelEntry = _CienaCesMplsStaticEgressTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 4, 1)
)
cienaCesMplsStaticEgressTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsStaticEgressTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsStaticEgressTunnelEntry.setStatus("current")
_CienaCesMplsStaticEgressTunnelIndex_Type = Unsigned32
_CienaCesMplsStaticEgressTunnelIndex_Object = MibTableColumn
cienaCesMplsStaticEgressTunnelIndex = _CienaCesMplsStaticEgressTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 4, 1, 1),
    _CienaCesMplsStaticEgressTunnelIndex_Type()
)
cienaCesMplsStaticEgressTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsStaticEgressTunnelIndex.setStatus("current")


class _CienaCesMplsStaticEgressTunnelName_Type(DisplayString):
    """Custom type cienaCesMplsStaticEgressTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsStaticEgressTunnelName_Type.__name__ = "DisplayString"
_CienaCesMplsStaticEgressTunnelName_Object = MibTableColumn
cienaCesMplsStaticEgressTunnelName = _CienaCesMplsStaticEgressTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 4, 1, 2),
    _CienaCesMplsStaticEgressTunnelName_Type()
)
cienaCesMplsStaticEgressTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticEgressTunnelName.setStatus("current")


class _CienaCesMplsStaticEgressTunnelAdminState_Type(CienaGlobalState):
    """Custom type cienaCesMplsStaticEgressTunnelAdminState based on CienaGlobalState"""


_CienaCesMplsStaticEgressTunnelAdminState_Object = MibTableColumn
cienaCesMplsStaticEgressTunnelAdminState = _CienaCesMplsStaticEgressTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 4, 1, 3),
    _CienaCesMplsStaticEgressTunnelAdminState_Type()
)
cienaCesMplsStaticEgressTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticEgressTunnelAdminState.setStatus("current")
_CienaCesMplsStaticEgressTunnelOperState_Type = CienaGlobalState
_CienaCesMplsStaticEgressTunnelOperState_Object = MibTableColumn
cienaCesMplsStaticEgressTunnelOperState = _CienaCesMplsStaticEgressTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 4, 1, 4),
    _CienaCesMplsStaticEgressTunnelOperState_Type()
)
cienaCesMplsStaticEgressTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticEgressTunnelOperState.setStatus("current")
_CienaCesMplsStaticEgressTunnelSourceIpAddr_Type = IpAddress
_CienaCesMplsStaticEgressTunnelSourceIpAddr_Object = MibTableColumn
cienaCesMplsStaticEgressTunnelSourceIpAddr = _CienaCesMplsStaticEgressTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 4, 1, 5),
    _CienaCesMplsStaticEgressTunnelSourceIpAddr_Type()
)
cienaCesMplsStaticEgressTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticEgressTunnelSourceIpAddr.setStatus("current")


class _CienaCesMplsStaticEgressTunnelLabel_Type(Unsigned32):
    """Custom type cienaCesMplsStaticEgressTunnelLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesMplsStaticEgressTunnelLabel_Type.__name__ = "Unsigned32"
_CienaCesMplsStaticEgressTunnelLabel_Object = MibTableColumn
cienaCesMplsStaticEgressTunnelLabel = _CienaCesMplsStaticEgressTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 4, 1, 6),
    _CienaCesMplsStaticEgressTunnelLabel_Type()
)
cienaCesMplsStaticEgressTunnelLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticEgressTunnelLabel.setStatus("current")
_CienaCesMplsDynamicEgressTunnelTable_Object = MibTable
cienaCesMplsDynamicEgressTunnelTable = _CienaCesMplsDynamicEgressTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cienaCesMplsDynamicEgressTunnelTable.setStatus("current")
_CienaCesMplsDynamicEgressTunnelEntry_Object = MibTableRow
cienaCesMplsDynamicEgressTunnelEntry = _CienaCesMplsDynamicEgressTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 5, 1)
)
cienaCesMplsDynamicEgressTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsDynamicEgressTunnelIndex"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsDynamicEgressTunnelInstance"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsDynamicEgressTunnelSourceIpAddr"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsDynamicEgressTunnelDestIpAddr"),
)
if mibBuilder.loadTexts:
    cienaCesMplsDynamicEgressTunnelEntry.setStatus("current")
_CienaCesMplsDynamicEgressTunnelIndex_Type = Unsigned32
_CienaCesMplsDynamicEgressTunnelIndex_Object = MibTableColumn
cienaCesMplsDynamicEgressTunnelIndex = _CienaCesMplsDynamicEgressTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 5, 1, 1),
    _CienaCesMplsDynamicEgressTunnelIndex_Type()
)
cienaCesMplsDynamicEgressTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicEgressTunnelIndex.setStatus("current")


class _CienaCesMplsDynamicEgressTunnelName_Type(DisplayString):
    """Custom type cienaCesMplsDynamicEgressTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesMplsDynamicEgressTunnelName_Type.__name__ = "DisplayString"
_CienaCesMplsDynamicEgressTunnelName_Object = MibTableColumn
cienaCesMplsDynamicEgressTunnelName = _CienaCesMplsDynamicEgressTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 5, 1, 2),
    _CienaCesMplsDynamicEgressTunnelName_Type()
)
cienaCesMplsDynamicEgressTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicEgressTunnelName.setStatus("current")


class _CienaCesMplsDynamicEgressTunnelAdminState_Type(CienaGlobalState):
    """Custom type cienaCesMplsDynamicEgressTunnelAdminState based on CienaGlobalState"""


_CienaCesMplsDynamicEgressTunnelAdminState_Object = MibTableColumn
cienaCesMplsDynamicEgressTunnelAdminState = _CienaCesMplsDynamicEgressTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 5, 1, 3),
    _CienaCesMplsDynamicEgressTunnelAdminState_Type()
)
cienaCesMplsDynamicEgressTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicEgressTunnelAdminState.setStatus("current")
_CienaCesMplsDynamicEgressTunnelOperState_Type = CienaGlobalState
_CienaCesMplsDynamicEgressTunnelOperState_Object = MibTableColumn
cienaCesMplsDynamicEgressTunnelOperState = _CienaCesMplsDynamicEgressTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 5, 1, 4),
    _CienaCesMplsDynamicEgressTunnelOperState_Type()
)
cienaCesMplsDynamicEgressTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicEgressTunnelOperState.setStatus("current")
_CienaCesMplsDynamicEgressTunnelInstance_Type = Unsigned32
_CienaCesMplsDynamicEgressTunnelInstance_Object = MibTableColumn
cienaCesMplsDynamicEgressTunnelInstance = _CienaCesMplsDynamicEgressTunnelInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 5, 1, 5),
    _CienaCesMplsDynamicEgressTunnelInstance_Type()
)
cienaCesMplsDynamicEgressTunnelInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicEgressTunnelInstance.setStatus("current")
_CienaCesMplsDynamicEgressTunnelSourceIpAddr_Type = IpAddress
_CienaCesMplsDynamicEgressTunnelSourceIpAddr_Object = MibTableColumn
cienaCesMplsDynamicEgressTunnelSourceIpAddr = _CienaCesMplsDynamicEgressTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 5, 1, 6),
    _CienaCesMplsDynamicEgressTunnelSourceIpAddr_Type()
)
cienaCesMplsDynamicEgressTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicEgressTunnelSourceIpAddr.setStatus("current")
_CienaCesMplsDynamicEgressTunnelDestIpAddr_Type = IpAddress
_CienaCesMplsDynamicEgressTunnelDestIpAddr_Object = MibTableColumn
cienaCesMplsDynamicEgressTunnelDestIpAddr = _CienaCesMplsDynamicEgressTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 5, 1, 7),
    _CienaCesMplsDynamicEgressTunnelDestIpAddr_Type()
)
cienaCesMplsDynamicEgressTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicEgressTunnelDestIpAddr.setStatus("current")
_CienaCesMplsDynamicEgressTunnelLabel_Type = Unsigned32
_CienaCesMplsDynamicEgressTunnelLabel_Object = MibTableColumn
cienaCesMplsDynamicEgressTunnelLabel = _CienaCesMplsDynamicEgressTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 5, 1, 8),
    _CienaCesMplsDynamicEgressTunnelLabel_Type()
)
cienaCesMplsDynamicEgressTunnelLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicEgressTunnelLabel.setStatus("current")
_CienaCesMplsStaticTransitTunnelTable_Object = MibTable
cienaCesMplsStaticTransitTunnelTable = _CienaCesMplsStaticTransitTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelTable.setStatus("current")
_CienaCesMplsStaticTransitTunnelEntry_Object = MibTableRow
cienaCesMplsStaticTransitTunnelEntry = _CienaCesMplsStaticTransitTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1)
)
cienaCesMplsStaticTransitTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsStaticTransitTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelEntry.setStatus("current")
_CienaCesMplsStaticTransitTunnelIndex_Type = Unsigned32
_CienaCesMplsStaticTransitTunnelIndex_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelIndex = _CienaCesMplsStaticTransitTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 1),
    _CienaCesMplsStaticTransitTunnelIndex_Type()
)
cienaCesMplsStaticTransitTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelIndex.setStatus("current")


class _CienaCesMplsStaticTransitTunnelName_Type(DisplayString):
    """Custom type cienaCesMplsStaticTransitTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesMplsStaticTransitTunnelName_Type.__name__ = "DisplayString"
_CienaCesMplsStaticTransitTunnelName_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelName = _CienaCesMplsStaticTransitTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 2),
    _CienaCesMplsStaticTransitTunnelName_Type()
)
cienaCesMplsStaticTransitTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelName.setStatus("current")


class _CienaCesMplsStaticTransitTunnelAdminState_Type(CienaGlobalState):
    """Custom type cienaCesMplsStaticTransitTunnelAdminState based on CienaGlobalState"""


_CienaCesMplsStaticTransitTunnelAdminState_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelAdminState = _CienaCesMplsStaticTransitTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 3),
    _CienaCesMplsStaticTransitTunnelAdminState_Type()
)
cienaCesMplsStaticTransitTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelAdminState.setStatus("current")
_CienaCesMplsStaticTransitTunnelOperState_Type = CienaGlobalState
_CienaCesMplsStaticTransitTunnelOperState_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelOperState = _CienaCesMplsStaticTransitTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 4),
    _CienaCesMplsStaticTransitTunnelOperState_Type()
)
cienaCesMplsStaticTransitTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelOperState.setStatus("current")
_CienaCesMplsStaticTransitTunnelNextHopIpAddr_Type = IpAddress
_CienaCesMplsStaticTransitTunnelNextHopIpAddr_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelNextHopIpAddr = _CienaCesMplsStaticTransitTunnelNextHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 5),
    _CienaCesMplsStaticTransitTunnelNextHopIpAddr_Type()
)
cienaCesMplsStaticTransitTunnelNextHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelNextHopIpAddr.setStatus("current")


class _CienaCesMplsStaticTransitTunnelInLabel_Type(Integer32):
    """Custom type cienaCesMplsStaticTransitTunnelInLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesMplsStaticTransitTunnelInLabel_Type.__name__ = "Integer32"
_CienaCesMplsStaticTransitTunnelInLabel_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelInLabel = _CienaCesMplsStaticTransitTunnelInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 6),
    _CienaCesMplsStaticTransitTunnelInLabel_Type()
)
cienaCesMplsStaticTransitTunnelInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelInLabel.setStatus("current")


class _CienaCesMplsStaticTransitTunnelOutLabel_Type(Integer32):
    """Custom type cienaCesMplsStaticTransitTunnelOutLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesMplsStaticTransitTunnelOutLabel_Type.__name__ = "Integer32"
_CienaCesMplsStaticTransitTunnelOutLabel_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelOutLabel = _CienaCesMplsStaticTransitTunnelOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 7),
    _CienaCesMplsStaticTransitTunnelOutLabel_Type()
)
cienaCesMplsStaticTransitTunnelOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelOutLabel.setStatus("current")


class _CienaCesMplsStaticTransitTunnelFcosPolicy_Type(FCosPolicy):
    """Custom type cienaCesMplsStaticTransitTunnelFcosPolicy based on FCosPolicy"""


_CienaCesMplsStaticTransitTunnelFcosPolicy_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelFcosPolicy = _CienaCesMplsStaticTransitTunnelFcosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 8),
    _CienaCesMplsStaticTransitTunnelFcosPolicy_Type()
)
cienaCesMplsStaticTransitTunnelFcosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelFcosPolicy.setStatus("deprecated")


class _CienaCesMplsStaticTransitTunnelFixedTc_Type(Unsigned32):
    """Custom type cienaCesMplsStaticTransitTunnelFixedTc based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMplsStaticTransitTunnelFixedTc_Type.__name__ = "Unsigned32"
_CienaCesMplsStaticTransitTunnelFixedTc_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelFixedTc = _CienaCesMplsStaticTransitTunnelFixedTc_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 9),
    _CienaCesMplsStaticTransitTunnelFixedTc_Type()
)
cienaCesMplsStaticTransitTunnelFixedTc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelFixedTc.setStatus("deprecated")


class _CienaCesMplsStaticTransitTunnelFrmCosMapId_Type(Integer32):
    """Custom type cienaCesMplsStaticTransitTunnelFrmCosMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsStaticTransitTunnelFrmCosMapId_Type.__name__ = "Integer32"
_CienaCesMplsStaticTransitTunnelFrmCosMapId_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelFrmCosMapId = _CienaCesMplsStaticTransitTunnelFrmCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 10),
    _CienaCesMplsStaticTransitTunnelFrmCosMapId_Type()
)
cienaCesMplsStaticTransitTunnelFrmCosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelFrmCosMapId.setStatus("deprecated")


class _CienaCesMplsStaticTransitTunnelTTLPolicy_Type(TTLPolicy):
    """Custom type cienaCesMplsStaticTransitTunnelTTLPolicy based on TTLPolicy"""


_CienaCesMplsStaticTransitTunnelTTLPolicy_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelTTLPolicy = _CienaCesMplsStaticTransitTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 11),
    _CienaCesMplsStaticTransitTunnelTTLPolicy_Type()
)
cienaCesMplsStaticTransitTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelTTLPolicy.setStatus("current")


class _CienaCesMplsStaticTransitTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesMplsStaticTransitTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesMplsStaticTransitTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesMplsStaticTransitTunnelFixedTTL_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelFixedTTL = _CienaCesMplsStaticTransitTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 12),
    _CienaCesMplsStaticTransitTunnelFixedTTL_Type()
)
cienaCesMplsStaticTransitTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelFixedTTL.setStatus("current")


class _CienaCesMplsStaticTransitTunnelRcosPolicy_Type(FCosPolicy):
    """Custom type cienaCesMplsStaticTransitTunnelRcosPolicy based on FCosPolicy"""


_CienaCesMplsStaticTransitTunnelRcosPolicy_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelRcosPolicy = _CienaCesMplsStaticTransitTunnelRcosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 13),
    _CienaCesMplsStaticTransitTunnelRcosPolicy_Type()
)
cienaCesMplsStaticTransitTunnelRcosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelRcosPolicy.setStatus("deprecated")


class _CienaCesMplsStaticTransitTunnelRCosMapId_Type(Integer32):
    """Custom type cienaCesMplsStaticTransitTunnelRCosMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsStaticTransitTunnelRCosMapId_Type.__name__ = "Integer32"
_CienaCesMplsStaticTransitTunnelRCosMapId_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelRCosMapId = _CienaCesMplsStaticTransitTunnelRCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 14),
    _CienaCesMplsStaticTransitTunnelRCosMapId_Type()
)
cienaCesMplsStaticTransitTunnelRCosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelRCosMapId.setStatus("deprecated")


class _CienaCesMplsStaticTransitTunnelCosProfileIndex_Type(Integer32):
    """Custom type cienaCesMplsStaticTransitTunnelCosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsStaticTransitTunnelCosProfileIndex_Type.__name__ = "Integer32"
_CienaCesMplsStaticTransitTunnelCosProfileIndex_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelCosProfileIndex = _CienaCesMplsStaticTransitTunnelCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 15),
    _CienaCesMplsStaticTransitTunnelCosProfileIndex_Type()
)
cienaCesMplsStaticTransitTunnelCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelCosProfileIndex.setStatus("current")
_CienaCesMplsStaticTransitTunnelCosProfileName_Type = DisplayString
_CienaCesMplsStaticTransitTunnelCosProfileName_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelCosProfileName = _CienaCesMplsStaticTransitTunnelCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 16),
    _CienaCesMplsStaticTransitTunnelCosProfileName_Type()
)
cienaCesMplsStaticTransitTunnelCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelCosProfileName.setStatus("current")
_CienaCesMplsStaticTransitTunnelSourceIpAddr_Type = IpAddress
_CienaCesMplsStaticTransitTunnelSourceIpAddr_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelSourceIpAddr = _CienaCesMplsStaticTransitTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 17),
    _CienaCesMplsStaticTransitTunnelSourceIpAddr_Type()
)
cienaCesMplsStaticTransitTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelSourceIpAddr.setStatus("current")
_CienaCesMplsStaticTransitTunnelDestIpAddr_Type = IpAddress
_CienaCesMplsStaticTransitTunnelDestIpAddr_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelDestIpAddr = _CienaCesMplsStaticTransitTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 18),
    _CienaCesMplsStaticTransitTunnelDestIpAddr_Type()
)
cienaCesMplsStaticTransitTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelDestIpAddr.setStatus("current")
_CienaCesMplsStaticTransitTunnelIncomingPackets_Type = Unsigned32
_CienaCesMplsStaticTransitTunnelIncomingPackets_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelIncomingPackets = _CienaCesMplsStaticTransitTunnelIncomingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 19),
    _CienaCesMplsStaticTransitTunnelIncomingPackets_Type()
)
cienaCesMplsStaticTransitTunnelIncomingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelIncomingPackets.setStatus("current")
_CienaCesMplsStaticTransitTunnelOutgoingPackets_Type = Unsigned32
_CienaCesMplsStaticTransitTunnelOutgoingPackets_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelOutgoingPackets = _CienaCesMplsStaticTransitTunnelOutgoingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 20),
    _CienaCesMplsStaticTransitTunnelOutgoingPackets_Type()
)
cienaCesMplsStaticTransitTunnelOutgoingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelOutgoingPackets.setStatus("current")
_CienaCesMplsStaticTransitTunnelIncomingBytes_Type = Unsigned32
_CienaCesMplsStaticTransitTunnelIncomingBytes_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelIncomingBytes = _CienaCesMplsStaticTransitTunnelIncomingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 21),
    _CienaCesMplsStaticTransitTunnelIncomingBytes_Type()
)
cienaCesMplsStaticTransitTunnelIncomingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelIncomingBytes.setStatus("current")
_CienaCesMplsStaticTransitTunnelOutgoingBytes_Type = Unsigned32
_CienaCesMplsStaticTransitTunnelOutgoingBytes_Object = MibTableColumn
cienaCesMplsStaticTransitTunnelOutgoingBytes = _CienaCesMplsStaticTransitTunnelOutgoingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 6, 1, 22),
    _CienaCesMplsStaticTransitTunnelOutgoingBytes_Type()
)
cienaCesMplsStaticTransitTunnelOutgoingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsStaticTransitTunnelOutgoingBytes.setStatus("current")
_CienaCesMplsDynamicTransitTunnelTable_Object = MibTable
cienaCesMplsDynamicTransitTunnelTable = _CienaCesMplsDynamicTransitTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelTable.setStatus("current")
_CienaCesMplsDynamicTransitTunnelEntry_Object = MibTableRow
cienaCesMplsDynamicTransitTunnelEntry = _CienaCesMplsDynamicTransitTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1)
)
cienaCesMplsDynamicTransitTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsDynamicTransitTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelEntry.setStatus("current")
_CienaCesMplsDynamicTransitTunnelIndex_Type = Unsigned32
_CienaCesMplsDynamicTransitTunnelIndex_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelIndex = _CienaCesMplsDynamicTransitTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 1),
    _CienaCesMplsDynamicTransitTunnelIndex_Type()
)
cienaCesMplsDynamicTransitTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelIndex.setStatus("current")


class _CienaCesMplsDynamicTransitTunnelName_Type(DisplayString):
    """Custom type cienaCesMplsDynamicTransitTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesMplsDynamicTransitTunnelName_Type.__name__ = "DisplayString"
_CienaCesMplsDynamicTransitTunnelName_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelName = _CienaCesMplsDynamicTransitTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 2),
    _CienaCesMplsDynamicTransitTunnelName_Type()
)
cienaCesMplsDynamicTransitTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelName.setStatus("current")


class _CienaCesMplsDynamicTransitTunnelAdminState_Type(CienaGlobalState):
    """Custom type cienaCesMplsDynamicTransitTunnelAdminState based on CienaGlobalState"""


_CienaCesMplsDynamicTransitTunnelAdminState_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelAdminState = _CienaCesMplsDynamicTransitTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 3),
    _CienaCesMplsDynamicTransitTunnelAdminState_Type()
)
cienaCesMplsDynamicTransitTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelAdminState.setStatus("current")
_CienaCesMplsDynamicTransitTunnelOperState_Type = CienaGlobalState
_CienaCesMplsDynamicTransitTunnelOperState_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelOperState = _CienaCesMplsDynamicTransitTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 4),
    _CienaCesMplsDynamicTransitTunnelOperState_Type()
)
cienaCesMplsDynamicTransitTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelOperState.setStatus("current")


class _CienaCesMplsDynamicTransitTunnelInLabel_Type(Integer32):
    """Custom type cienaCesMplsDynamicTransitTunnelInLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesMplsDynamicTransitTunnelInLabel_Type.__name__ = "Integer32"
_CienaCesMplsDynamicTransitTunnelInLabel_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelInLabel = _CienaCesMplsDynamicTransitTunnelInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 5),
    _CienaCesMplsDynamicTransitTunnelInLabel_Type()
)
cienaCesMplsDynamicTransitTunnelInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelInLabel.setStatus("current")


class _CienaCesMplsDynamicTransitTunnelOutLabel_Type(Integer32):
    """Custom type cienaCesMplsDynamicTransitTunnelOutLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesMplsDynamicTransitTunnelOutLabel_Type.__name__ = "Integer32"
_CienaCesMplsDynamicTransitTunnelOutLabel_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelOutLabel = _CienaCesMplsDynamicTransitTunnelOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 6),
    _CienaCesMplsDynamicTransitTunnelOutLabel_Type()
)
cienaCesMplsDynamicTransitTunnelOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelOutLabel.setStatus("current")
_CienaCesMplsDynamicTransitTunnelNextHopIpAddr_Type = IpAddress
_CienaCesMplsDynamicTransitTunnelNextHopIpAddr_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelNextHopIpAddr = _CienaCesMplsDynamicTransitTunnelNextHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 7),
    _CienaCesMplsDynamicTransitTunnelNextHopIpAddr_Type()
)
cienaCesMplsDynamicTransitTunnelNextHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelNextHopIpAddr.setStatus("current")
_CienaCesMplsDynamicTransitTunnelSourceIpAddr_Type = IpAddress
_CienaCesMplsDynamicTransitTunnelSourceIpAddr_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelSourceIpAddr = _CienaCesMplsDynamicTransitTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 8),
    _CienaCesMplsDynamicTransitTunnelSourceIpAddr_Type()
)
cienaCesMplsDynamicTransitTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelSourceIpAddr.setStatus("current")
_CienaCesMplsDynamicTransitTunnelDestIpAddr_Type = IpAddress
_CienaCesMplsDynamicTransitTunnelDestIpAddr_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelDestIpAddr = _CienaCesMplsDynamicTransitTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 9),
    _CienaCesMplsDynamicTransitTunnelDestIpAddr_Type()
)
cienaCesMplsDynamicTransitTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelDestIpAddr.setStatus("current")
_CienaCesMplsDynamicTransitTunnelIncomingPackets_Type = Unsigned32
_CienaCesMplsDynamicTransitTunnelIncomingPackets_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelIncomingPackets = _CienaCesMplsDynamicTransitTunnelIncomingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 10),
    _CienaCesMplsDynamicTransitTunnelIncomingPackets_Type()
)
cienaCesMplsDynamicTransitTunnelIncomingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelIncomingPackets.setStatus("current")
_CienaCesMplsDynamicTransitTunnelOutgoingPackets_Type = Unsigned32
_CienaCesMplsDynamicTransitTunnelOutgoingPackets_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelOutgoingPackets = _CienaCesMplsDynamicTransitTunnelOutgoingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 11),
    _CienaCesMplsDynamicTransitTunnelOutgoingPackets_Type()
)
cienaCesMplsDynamicTransitTunnelOutgoingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelOutgoingPackets.setStatus("current")
_CienaCesMplsDynamicTransitTunnelIncomingBytes_Type = Unsigned32
_CienaCesMplsDynamicTransitTunnelIncomingBytes_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelIncomingBytes = _CienaCesMplsDynamicTransitTunnelIncomingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 12),
    _CienaCesMplsDynamicTransitTunnelIncomingBytes_Type()
)
cienaCesMplsDynamicTransitTunnelIncomingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelIncomingBytes.setStatus("current")
_CienaCesMplsDynamicTransitTunnelOutgoingBytes_Type = Unsigned32
_CienaCesMplsDynamicTransitTunnelOutgoingBytes_Object = MibTableColumn
cienaCesMplsDynamicTransitTunnelOutgoingBytes = _CienaCesMplsDynamicTransitTunnelOutgoingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 7, 1, 13),
    _CienaCesMplsDynamicTransitTunnelOutgoingBytes_Type()
)
cienaCesMplsDynamicTransitTunnelOutgoingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicTransitTunnelOutgoingBytes.setStatus("current")
_CienaCesMplsTunnelPath_ObjectIdentity = ObjectIdentity
cienaCesMplsTunnelPath = _CienaCesMplsTunnelPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 8)
)
_CienaCesMplsTunnelPathTable_Object = MibTable
cienaCesMplsTunnelPathTable = _CienaCesMplsTunnelPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cienaCesMplsTunnelPathTable.setStatus("current")
_CienaCesMplsTunnelPathEntry_Object = MibTableRow
cienaCesMplsTunnelPathEntry = _CienaCesMplsTunnelPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 8, 1, 1)
)
cienaCesMplsTunnelPathEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsTunnelPathIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsTunnelPathEntry.setStatus("current")
_CienaCesMplsTunnelPathIndex_Type = Unsigned32
_CienaCesMplsTunnelPathIndex_Object = MibTableColumn
cienaCesMplsTunnelPathIndex = _CienaCesMplsTunnelPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 8, 1, 1, 1),
    _CienaCesMplsTunnelPathIndex_Type()
)
cienaCesMplsTunnelPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelPathIndex.setStatus("current")


class _CienaCesMplsTunnelPathName_Type(DisplayString):
    """Custom type cienaCesMplsTunnelPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsTunnelPathName_Type.__name__ = "DisplayString"
_CienaCesMplsTunnelPathName_Object = MibTableColumn
cienaCesMplsTunnelPathName = _CienaCesMplsTunnelPathName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 8, 1, 1, 2),
    _CienaCesMplsTunnelPathName_Type()
)
cienaCesMplsTunnelPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelPathName.setStatus("current")
_CienaCesMplsTunnelPathUseCount_Type = Counter32
_CienaCesMplsTunnelPathUseCount_Object = MibTableColumn
cienaCesMplsTunnelPathUseCount = _CienaCesMplsTunnelPathUseCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 8, 1, 1, 3),
    _CienaCesMplsTunnelPathUseCount_Type()
)
cienaCesMplsTunnelPathUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelPathUseCount.setStatus("current")
_CienaCesMplsTunnelPathHopTable_Object = MibTable
cienaCesMplsTunnelPathHopTable = _CienaCesMplsTunnelPathHopTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cienaCesMplsTunnelPathHopTable.setStatus("current")
_CienaCesMplsTunnelPathHopEntry_Object = MibTableRow
cienaCesMplsTunnelPathHopEntry = _CienaCesMplsTunnelPathHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 8, 2, 1)
)
cienaCesMplsTunnelPathHopEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsTunnelPathIndex"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsTunnelPathHopIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsTunnelPathHopEntry.setStatus("current")
_CienaCesMplsTunnelPathHopIndex_Type = Unsigned32
_CienaCesMplsTunnelPathHopIndex_Object = MibTableColumn
cienaCesMplsTunnelPathHopIndex = _CienaCesMplsTunnelPathHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 8, 2, 1, 1),
    _CienaCesMplsTunnelPathHopIndex_Type()
)
cienaCesMplsTunnelPathHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelPathHopIndex.setStatus("current")
_CienaCesMplsTunnelPathHopIpAddr_Type = IpAddress
_CienaCesMplsTunnelPathHopIpAddr_Object = MibTableColumn
cienaCesMplsTunnelPathHopIpAddr = _CienaCesMplsTunnelPathHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 8, 2, 1, 2),
    _CienaCesMplsTunnelPathHopIpAddr_Type()
)
cienaCesMplsTunnelPathHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelPathHopIpAddr.setStatus("current")


class _CienaCesMplsTunnelPathHopType_Type(Integer32):
    """Custom type cienaCesMplsTunnelPathHopType based on Integer32"""
    defaultValue = 1

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


_CienaCesMplsTunnelPathHopType_Type.__name__ = "Integer32"
_CienaCesMplsTunnelPathHopType_Object = MibTableColumn
cienaCesMplsTunnelPathHopType = _CienaCesMplsTunnelPathHopType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 8, 2, 1, 3),
    _CienaCesMplsTunnelPathHopType_Type()
)
cienaCesMplsTunnelPathHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelPathHopType.setStatus("current")
_CienaCesMplsEncapTunnelNotif_ObjectIdentity = ObjectIdentity
cienaCesMplsEncapTunnelNotif = _CienaCesMplsEncapTunnelNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 9)
)
_CienaCesMplsNotifEncapTunnelTable_Object = MibTable
cienaCesMplsNotifEncapTunnelTable = _CienaCesMplsNotifEncapTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelTable.setStatus("current")
_CienaCesMplsNotifEncapTunnelEntry_Object = MibTableRow
cienaCesMplsNotifEncapTunnelEntry = _CienaCesMplsNotifEncapTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 9, 1, 1)
)
cienaCesMplsNotifEncapTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelType"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelEntry.setStatus("current")


class _CienaCesMplsNotifEncapTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesMplsNotifEncapTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsNotifEncapTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsNotifEncapTunnelIndex_Object = MibTableColumn
cienaCesMplsNotifEncapTunnelIndex = _CienaCesMplsNotifEncapTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 9, 1, 1, 1),
    _CienaCesMplsNotifEncapTunnelIndex_Type()
)
cienaCesMplsNotifEncapTunnelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelIndex.setStatus("current")


class _CienaCesMplsNotifEncapTunnelType_Type(Integer32):
    """Custom type cienaCesMplsNotifEncapTunnelType based on Integer32"""
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
          ("frr", 3),
          ("static", 1))
    )


_CienaCesMplsNotifEncapTunnelType_Type.__name__ = "Integer32"
_CienaCesMplsNotifEncapTunnelType_Object = MibTableColumn
cienaCesMplsNotifEncapTunnelType = _CienaCesMplsNotifEncapTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 9, 1, 1, 2),
    _CienaCesMplsNotifEncapTunnelType_Type()
)
cienaCesMplsNotifEncapTunnelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelType.setStatus("current")
_CienaCesMplsNotifEncapTunnelName_Type = DisplayString
_CienaCesMplsNotifEncapTunnelName_Object = MibTableColumn
cienaCesMplsNotifEncapTunnelName = _CienaCesMplsNotifEncapTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 9, 1, 1, 3),
    _CienaCesMplsNotifEncapTunnelName_Type()
)
cienaCesMplsNotifEncapTunnelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelName.setStatus("current")
_CienaCesMplsNotifEncapTunnelAdminState_Type = CienaGlobalState
_CienaCesMplsNotifEncapTunnelAdminState_Object = MibTableColumn
cienaCesMplsNotifEncapTunnelAdminState = _CienaCesMplsNotifEncapTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 9, 1, 1, 4),
    _CienaCesMplsNotifEncapTunnelAdminState_Type()
)
cienaCesMplsNotifEncapTunnelAdminState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelAdminState.setStatus("current")
_CienaCesMplsNotifEncapTunnelOperState_Type = CienaGlobalState
_CienaCesMplsNotifEncapTunnelOperState_Object = MibTableColumn
cienaCesMplsNotifEncapTunnelOperState = _CienaCesMplsNotifEncapTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 9, 1, 1, 5),
    _CienaCesMplsNotifEncapTunnelOperState_Type()
)
cienaCesMplsNotifEncapTunnelOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelOperState.setStatus("current")
_CienaCesMplsNotifEncapTunnelOamFaulted_Type = TunnelOamFault
_CienaCesMplsNotifEncapTunnelOamFaulted_Object = MibTableColumn
cienaCesMplsNotifEncapTunnelOamFaulted = _CienaCesMplsNotifEncapTunnelOamFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 9, 1, 1, 6),
    _CienaCesMplsNotifEncapTunnelOamFaulted_Type()
)
cienaCesMplsNotifEncapTunnelOamFaulted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelOamFaulted.setStatus("current")
_CienaCesMplsNotifEncapTunnelFaultedNodeId_Type = IpAddress
_CienaCesMplsNotifEncapTunnelFaultedNodeId_Object = MibTableColumn
cienaCesMplsNotifEncapTunnelFaultedNodeId = _CienaCesMplsNotifEncapTunnelFaultedNodeId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 9, 1, 1, 7),
    _CienaCesMplsNotifEncapTunnelFaultedNodeId_Type()
)
cienaCesMplsNotifEncapTunnelFaultedNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelFaultedNodeId.setStatus("current")
_CienaCesMplsTransitTunnelNotif_ObjectIdentity = ObjectIdentity
cienaCesMplsTransitTunnelNotif = _CienaCesMplsTransitTunnelNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 10)
)
_CienaCesMplsNotifTransitTunnelTable_Object = MibTable
cienaCesMplsNotifTransitTunnelTable = _CienaCesMplsNotifTransitTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cienaCesMplsNotifTransitTunnelTable.setStatus("current")
_CienaCesMplsNotifTransitTunnelEntry_Object = MibTableRow
cienaCesMplsNotifTransitTunnelEntry = _CienaCesMplsNotifTransitTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 10, 1, 1)
)
cienaCesMplsNotifTransitTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsNotifTransitTunnelType"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsNotifTransitTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsNotifTransitTunnelEntry.setStatus("current")


class _CienaCesMplsNotifTransitTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesMplsNotifTransitTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsNotifTransitTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsNotifTransitTunnelIndex_Object = MibTableColumn
cienaCesMplsNotifTransitTunnelIndex = _CienaCesMplsNotifTransitTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 10, 1, 1, 1),
    _CienaCesMplsNotifTransitTunnelIndex_Type()
)
cienaCesMplsNotifTransitTunnelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifTransitTunnelIndex.setStatus("current")


class _CienaCesMplsNotifTransitTunnelType_Type(Integer32):
    """Custom type cienaCesMplsNotifTransitTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CienaCesMplsNotifTransitTunnelType_Type.__name__ = "Integer32"
_CienaCesMplsNotifTransitTunnelType_Object = MibTableColumn
cienaCesMplsNotifTransitTunnelType = _CienaCesMplsNotifTransitTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 10, 1, 1, 2),
    _CienaCesMplsNotifTransitTunnelType_Type()
)
cienaCesMplsNotifTransitTunnelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifTransitTunnelType.setStatus("current")
_CienaCesMplsNotifTransitTunnelName_Type = DisplayString
_CienaCesMplsNotifTransitTunnelName_Object = MibTableColumn
cienaCesMplsNotifTransitTunnelName = _CienaCesMplsNotifTransitTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 10, 1, 1, 3),
    _CienaCesMplsNotifTransitTunnelName_Type()
)
cienaCesMplsNotifTransitTunnelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifTransitTunnelName.setStatus("current")
_CienaCesMplsNotifTransitTunnelAdminState_Type = CienaGlobalState
_CienaCesMplsNotifTransitTunnelAdminState_Object = MibTableColumn
cienaCesMplsNotifTransitTunnelAdminState = _CienaCesMplsNotifTransitTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 10, 1, 1, 4),
    _CienaCesMplsNotifTransitTunnelAdminState_Type()
)
cienaCesMplsNotifTransitTunnelAdminState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifTransitTunnelAdminState.setStatus("current")
_CienaCesMplsNotifTransitTunnelOperState_Type = CienaGlobalState
_CienaCesMplsNotifTransitTunnelOperState_Object = MibTableColumn
cienaCesMplsNotifTransitTunnelOperState = _CienaCesMplsNotifTransitTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 10, 1, 1, 5),
    _CienaCesMplsNotifTransitTunnelOperState_Type()
)
cienaCesMplsNotifTransitTunnelOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifTransitTunnelOperState.setStatus("current")
_CienaCesMplsNotifTransitTunnelOamFaulted_Type = TunnelOamFault
_CienaCesMplsNotifTransitTunnelOamFaulted_Object = MibTableColumn
cienaCesMplsNotifTransitTunnelOamFaulted = _CienaCesMplsNotifTransitTunnelOamFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 10, 1, 1, 6),
    _CienaCesMplsNotifTransitTunnelOamFaulted_Type()
)
cienaCesMplsNotifTransitTunnelOamFaulted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifTransitTunnelOamFaulted.setStatus("current")
_CienaCesMplsEncapTunnelGrpNotif_ObjectIdentity = ObjectIdentity
cienaCesMplsEncapTunnelGrpNotif = _CienaCesMplsEncapTunnelGrpNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 11)
)
_CienaCesMplsNotifEncapTunnelGrpTable_Object = MibTable
cienaCesMplsNotifEncapTunnelGrpTable = _CienaCesMplsNotifEncapTunnelGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelGrpTable.setStatus("current")
_CienaCesMplsNotifEncapTunnelGrpEntry_Object = MibTableRow
cienaCesMplsNotifEncapTunnelGrpEntry = _CienaCesMplsNotifEncapTunnelGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 11, 1, 1)
)
cienaCesMplsNotifEncapTunnelGrpEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelGrpIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelGrpEntry.setStatus("current")


class _CienaCesMplsNotifEncapTunnelGrpIndex_Type(Unsigned32):
    """Custom type cienaCesMplsNotifEncapTunnelGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsNotifEncapTunnelGrpIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsNotifEncapTunnelGrpIndex_Object = MibTableColumn
cienaCesMplsNotifEncapTunnelGrpIndex = _CienaCesMplsNotifEncapTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 11, 1, 1, 1),
    _CienaCesMplsNotifEncapTunnelGrpIndex_Type()
)
cienaCesMplsNotifEncapTunnelGrpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelGrpIndex.setStatus("current")
_CienaCesMplsNotifEncapTunnelGrpName_Type = DisplayString
_CienaCesMplsNotifEncapTunnelGrpName_Object = MibTableColumn
cienaCesMplsNotifEncapTunnelGrpName = _CienaCesMplsNotifEncapTunnelGrpName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 11, 1, 1, 2),
    _CienaCesMplsNotifEncapTunnelGrpName_Type()
)
cienaCesMplsNotifEncapTunnelGrpName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelGrpName.setStatus("current")


class _CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlIndex_Type(Unsigned32):
    """Custom type cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlIndex_Object = MibTableColumn
cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlIndex = _CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 11, 1, 1, 3),
    _CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlIndex_Type()
)
cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlIndex.setStatus("current")
_CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlName_Type = DisplayString
_CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlName_Object = MibTableColumn
cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlName = _CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 11, 1, 1, 4),
    _CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlName_Type()
)
cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlName.setStatus("current")


class _CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlType_Type(Integer32):
    """Custom type cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlType based on Integer32"""
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
          ("frr", 3),
          ("static", 1))
    )


_CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlType_Type.__name__ = "Integer32"
_CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlType_Object = MibTableColumn
cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlType = _CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 11, 1, 1, 5),
    _CienaCesMplsNotifEncapTunnelGrpActiveEncapTunlType_Type()
)
cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlType.setStatus("current")
_CienaCesMplsAssociatedTunnelTable_Object = MibTable
cienaCesMplsAssociatedTunnelTable = _CienaCesMplsAssociatedTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedTunnelTable.setStatus("current")
_CienaCesMplsAssociatedTunnelEntry_Object = MibTableRow
cienaCesMplsAssociatedTunnelEntry = _CienaCesMplsAssociatedTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1)
)
cienaCesMplsAssociatedTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsAssociatedTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedTunnelEntry.setStatus("current")


class _CienaCesMplsAssociatedTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesMplsAssociatedTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsAssociatedTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsAssociatedTunnelIndex_Object = MibTableColumn
cienaCesMplsAssociatedTunnelIndex = _CienaCesMplsAssociatedTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 1),
    _CienaCesMplsAssociatedTunnelIndex_Type()
)
cienaCesMplsAssociatedTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedTunnelIndex.setStatus("current")
_CienaCesMplsAssociatedTunnelName_Type = DisplayString
_CienaCesMplsAssociatedTunnelName_Object = MibTableColumn
cienaCesMplsAssociatedTunnelName = _CienaCesMplsAssociatedTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 2),
    _CienaCesMplsAssociatedTunnelName_Type()
)
cienaCesMplsAssociatedTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedTunnelName.setStatus("current")
_CienaCesMplsAssociatedForwardTunnelName_Type = DisplayString
_CienaCesMplsAssociatedForwardTunnelName_Object = MibTableColumn
cienaCesMplsAssociatedForwardTunnelName = _CienaCesMplsAssociatedForwardTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 3),
    _CienaCesMplsAssociatedForwardTunnelName_Type()
)
cienaCesMplsAssociatedForwardTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedForwardTunnelName.setStatus("current")
_CienaCesMplsAssociatedForwardTunnelType_Type = DisplayString
_CienaCesMplsAssociatedForwardTunnelType_Object = MibTableColumn
cienaCesMplsAssociatedForwardTunnelType = _CienaCesMplsAssociatedForwardTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 4),
    _CienaCesMplsAssociatedForwardTunnelType_Type()
)
cienaCesMplsAssociatedForwardTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedForwardTunnelType.setStatus("current")
_CienaCesMplsAssociatedReverseTunnelName_Type = DisplayString
_CienaCesMplsAssociatedReverseTunnelName_Object = MibTableColumn
cienaCesMplsAssociatedReverseTunnelName = _CienaCesMplsAssociatedReverseTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 5),
    _CienaCesMplsAssociatedReverseTunnelName_Type()
)
cienaCesMplsAssociatedReverseTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedReverseTunnelName.setStatus("current")
_CienaCesMplsAssociatedReverseTunnelType_Type = DisplayString
_CienaCesMplsAssociatedReverseTunnelType_Object = MibTableColumn
cienaCesMplsAssociatedReverseTunnelType = _CienaCesMplsAssociatedReverseTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 6),
    _CienaCesMplsAssociatedReverseTunnelType_Type()
)
cienaCesMplsAssociatedReverseTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedReverseTunnelType.setStatus("current")
_CienaCesMplsAssociatedForwardTunnelDestIpAddr_Type = IpAddress
_CienaCesMplsAssociatedForwardTunnelDestIpAddr_Object = MibTableColumn
cienaCesMplsAssociatedForwardTunnelDestIpAddr = _CienaCesMplsAssociatedForwardTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 7),
    _CienaCesMplsAssociatedForwardTunnelDestIpAddr_Type()
)
cienaCesMplsAssociatedForwardTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedForwardTunnelDestIpAddr.setStatus("current")
_CienaCesMplsAssociatedDynamicTunnelSrcIpAddr_Type = IpAddress
_CienaCesMplsAssociatedDynamicTunnelSrcIpAddr_Object = MibTableColumn
cienaCesMplsAssociatedDynamicTunnelSrcIpAddr = _CienaCesMplsAssociatedDynamicTunnelSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 8),
    _CienaCesMplsAssociatedDynamicTunnelSrcIpAddr_Type()
)
cienaCesMplsAssociatedDynamicTunnelSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedDynamicTunnelSrcIpAddr.setStatus("current")
_CienaCesMplsAssociatedTunnelAdminState_Type = CienaGlobalState
_CienaCesMplsAssociatedTunnelAdminState_Object = MibTableColumn
cienaCesMplsAssociatedTunnelAdminState = _CienaCesMplsAssociatedTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 9),
    _CienaCesMplsAssociatedTunnelAdminState_Type()
)
cienaCesMplsAssociatedTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedTunnelAdminState.setStatus("current")
_CienaCesMplsAssociatedTunnelOperState_Type = CienaGlobalState
_CienaCesMplsAssociatedTunnelOperState_Object = MibTableColumn
cienaCesMplsAssociatedTunnelOperState = _CienaCesMplsAssociatedTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 10),
    _CienaCesMplsAssociatedTunnelOperState_Type()
)
cienaCesMplsAssociatedTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedTunnelOperState.setStatus("current")
_CienaCesMplsAssociatedForwardTunnelOperState_Type = CienaGlobalState
_CienaCesMplsAssociatedForwardTunnelOperState_Object = MibTableColumn
cienaCesMplsAssociatedForwardTunnelOperState = _CienaCesMplsAssociatedForwardTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 11),
    _CienaCesMplsAssociatedForwardTunnelOperState_Type()
)
cienaCesMplsAssociatedForwardTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedForwardTunnelOperState.setStatus("current")
_CienaCesMplsAssociatedReverseTunnelOperState_Type = CienaGlobalState
_CienaCesMplsAssociatedReverseTunnelOperState_Object = MibTableColumn
cienaCesMplsAssociatedReverseTunnelOperState = _CienaCesMplsAssociatedReverseTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 12),
    _CienaCesMplsAssociatedReverseTunnelOperState_Type()
)
cienaCesMplsAssociatedReverseTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedReverseTunnelOperState.setStatus("current")


class _CienaCesMplsAssociatedProtectionRole_Type(Integer32):
    """Custom type cienaCesMplsAssociatedProtectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 0),
          ("primary", 1))
    )


_CienaCesMplsAssociatedProtectionRole_Type.__name__ = "Integer32"
_CienaCesMplsAssociatedProtectionRole_Object = MibTableColumn
cienaCesMplsAssociatedProtectionRole = _CienaCesMplsAssociatedProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 13),
    _CienaCesMplsAssociatedProtectionRole_Type()
)
cienaCesMplsAssociatedProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedProtectionRole.setStatus("current")


class _CienaCesMplsAssociatedProtectionState_Type(Integer32):
    """Custom type cienaCesMplsAssociatedProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 0))
    )


_CienaCesMplsAssociatedProtectionState_Type.__name__ = "Integer32"
_CienaCesMplsAssociatedProtectionState_Object = MibTableColumn
cienaCesMplsAssociatedProtectionState = _CienaCesMplsAssociatedProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 14),
    _CienaCesMplsAssociatedProtectionState_Type()
)
cienaCesMplsAssociatedProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedProtectionState.setStatus("current")
_CienaCesMplsAssociatedTunnelProtectionPartnerName_Type = DisplayString
_CienaCesMplsAssociatedTunnelProtectionPartnerName_Object = MibTableColumn
cienaCesMplsAssociatedTunnelProtectionPartnerName = _CienaCesMplsAssociatedTunnelProtectionPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 15),
    _CienaCesMplsAssociatedTunnelProtectionPartnerName_Type()
)
cienaCesMplsAssociatedTunnelProtectionPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedTunnelProtectionPartnerName.setStatus("current")
_CienaCesMplsAssociatedBfdMonitoring_Type = CienaGlobalState
_CienaCesMplsAssociatedBfdMonitoring_Object = MibTableColumn
cienaCesMplsAssociatedBfdMonitoring = _CienaCesMplsAssociatedBfdMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 16),
    _CienaCesMplsAssociatedBfdMonitoring_Type()
)
cienaCesMplsAssociatedBfdMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedBfdMonitoring.setStatus("current")
_CienaCesMplsAssociatedBfdProfileName_Type = DisplayString
_CienaCesMplsAssociatedBfdProfileName_Object = MibTableColumn
cienaCesMplsAssociatedBfdProfileName = _CienaCesMplsAssociatedBfdProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 17),
    _CienaCesMplsAssociatedBfdProfileName_Type()
)
cienaCesMplsAssociatedBfdProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedBfdProfileName.setStatus("current")
_CienaCesMplsAssociatedBfdSessionName_Type = DisplayString
_CienaCesMplsAssociatedBfdSessionName_Object = MibTableColumn
cienaCesMplsAssociatedBfdSessionName = _CienaCesMplsAssociatedBfdSessionName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 18),
    _CienaCesMplsAssociatedBfdSessionName_Type()
)
cienaCesMplsAssociatedBfdSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedBfdSessionName.setStatus("current")
_CienaCesMplsAssociatedBfdSessionFaulted_Type = Integer32
_CienaCesMplsAssociatedBfdSessionFaulted_Object = MibTableColumn
cienaCesMplsAssociatedBfdSessionFaulted = _CienaCesMplsAssociatedBfdSessionFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 19),
    _CienaCesMplsAssociatedBfdSessionFaulted_Type()
)
cienaCesMplsAssociatedBfdSessionFaulted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedBfdSessionFaulted.setStatus("current")


class _CienaCesMplsAssociatedBfdProfileIndex_Type(Unsigned32):
    """Custom type cienaCesMplsAssociatedBfdProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsAssociatedBfdProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsAssociatedBfdProfileIndex_Object = MibTableColumn
cienaCesMplsAssociatedBfdProfileIndex = _CienaCesMplsAssociatedBfdProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 12, 1, 20),
    _CienaCesMplsAssociatedBfdProfileIndex_Type()
)
cienaCesMplsAssociatedBfdProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedBfdProfileIndex.setStatus("current")
_CienaCesMplsTunnelARHopTable_Object = MibTable
cienaCesMplsTunnelARHopTable = _CienaCesMplsTunnelARHopTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cienaCesMplsTunnelARHopTable.setStatus("current")
_CienaCesMplsTunnelARHopEntry_Object = MibTableRow
cienaCesMplsTunnelARHopEntry = _CienaCesMplsTunnelARHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 13, 1)
)
cienaCesMplsTunnelARHopEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaMplsTunnelARHopListIndex"),
    (0, "CIENA-CES-MPLS-MIB", "cienaMplsTunnelARHopIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsTunnelARHopEntry.setStatus("current")
_CienaMplsTunnelARHopListIndex_Type = Unsigned32
_CienaMplsTunnelARHopListIndex_Object = MibTableColumn
cienaMplsTunnelARHopListIndex = _CienaMplsTunnelARHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 13, 1, 1),
    _CienaMplsTunnelARHopListIndex_Type()
)
cienaMplsTunnelARHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaMplsTunnelARHopListIndex.setStatus("current")
_CienaMplsTunnelARHopIndex_Type = Unsigned32
_CienaMplsTunnelARHopIndex_Object = MibTableColumn
cienaMplsTunnelARHopIndex = _CienaMplsTunnelARHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 13, 1, 2),
    _CienaMplsTunnelARHopIndex_Type()
)
cienaMplsTunnelARHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaMplsTunnelARHopIndex.setStatus("current")
_CienaMplsTunnelARHopAddrType_Type = Integer32
_CienaMplsTunnelARHopAddrType_Object = MibTableColumn
cienaMplsTunnelARHopAddrType = _CienaMplsTunnelARHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 13, 1, 3),
    _CienaMplsTunnelARHopAddrType_Type()
)
cienaMplsTunnelARHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaMplsTunnelARHopAddrType.setStatus("current")
_CienaMplsTunnelARHopIpAddr_Type = IpAddress
_CienaMplsTunnelARHopIpAddr_Object = MibTableColumn
cienaMplsTunnelARHopIpAddr = _CienaMplsTunnelARHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 13, 1, 4),
    _CienaMplsTunnelARHopIpAddr_Type()
)
cienaMplsTunnelARHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaMplsTunnelARHopIpAddr.setStatus("current")
_CienaMplsTunnelARHopAddrUnnum_Type = Unsigned32
_CienaMplsTunnelARHopAddrUnnum_Object = MibTableColumn
cienaMplsTunnelARHopAddrUnnum = _CienaMplsTunnelARHopAddrUnnum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 13, 1, 5),
    _CienaMplsTunnelARHopAddrUnnum_Type()
)
cienaMplsTunnelARHopAddrUnnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaMplsTunnelARHopAddrUnnum.setStatus("current")
_CienaMplsTunnelARHopLspId_Type = Unsigned32
_CienaMplsTunnelARHopLspId_Object = MibTableColumn
cienaMplsTunnelARHopLspId = _CienaMplsTunnelARHopLspId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 13, 1, 6),
    _CienaMplsTunnelARHopLspId_Type()
)
cienaMplsTunnelARHopLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaMplsTunnelARHopLspId.setStatus("current")
_CienaCesMplsAssociatedTunnelNotif_ObjectIdentity = ObjectIdentity
cienaCesMplsAssociatedTunnelNotif = _CienaCesMplsAssociatedTunnelNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 14)
)
_CienaCesMplsNotifAssociatedTunnelTable_Object = MibTable
cienaCesMplsNotifAssociatedTunnelTable = _CienaCesMplsNotifAssociatedTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    cienaCesMplsNotifAssociatedTunnelTable.setStatus("current")
_CienaCesMplsNotifAssociatedTunnelEntry_Object = MibTableRow
cienaCesMplsNotifAssociatedTunnelEntry = _CienaCesMplsNotifAssociatedTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 14, 1, 1)
)
cienaCesMplsNotifAssociatedTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsNotifAssociatedTunnelType"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsNotifAssociatedTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsNotifAssociatedTunnelEntry.setStatus("current")


class _CienaCesMplsNotifAssociatedTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesMplsNotifAssociatedTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsNotifAssociatedTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsNotifAssociatedTunnelIndex_Object = MibTableColumn
cienaCesMplsNotifAssociatedTunnelIndex = _CienaCesMplsNotifAssociatedTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 14, 1, 1, 1),
    _CienaCesMplsNotifAssociatedTunnelIndex_Type()
)
cienaCesMplsNotifAssociatedTunnelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifAssociatedTunnelIndex.setStatus("current")


class _CienaCesMplsNotifAssociatedTunnelType_Type(Integer32):
    """Custom type cienaCesMplsNotifAssociatedTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CienaCesMplsNotifAssociatedTunnelType_Type.__name__ = "Integer32"
_CienaCesMplsNotifAssociatedTunnelType_Object = MibTableColumn
cienaCesMplsNotifAssociatedTunnelType = _CienaCesMplsNotifAssociatedTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 14, 1, 1, 2),
    _CienaCesMplsNotifAssociatedTunnelType_Type()
)
cienaCesMplsNotifAssociatedTunnelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifAssociatedTunnelType.setStatus("current")
_CienaCesMplsNotifAssociatedTunnelName_Type = DisplayString
_CienaCesMplsNotifAssociatedTunnelName_Object = MibTableColumn
cienaCesMplsNotifAssociatedTunnelName = _CienaCesMplsNotifAssociatedTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 14, 1, 1, 3),
    _CienaCesMplsNotifAssociatedTunnelName_Type()
)
cienaCesMplsNotifAssociatedTunnelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifAssociatedTunnelName.setStatus("current")
_CienaCesMplsNotifAssociatedTunnelAdminState_Type = CienaGlobalState
_CienaCesMplsNotifAssociatedTunnelAdminState_Object = MibTableColumn
cienaCesMplsNotifAssociatedTunnelAdminState = _CienaCesMplsNotifAssociatedTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 14, 1, 1, 4),
    _CienaCesMplsNotifAssociatedTunnelAdminState_Type()
)
cienaCesMplsNotifAssociatedTunnelAdminState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifAssociatedTunnelAdminState.setStatus("current")
_CienaCesMplsNotifAssociatedTunnelOperState_Type = CienaGlobalState
_CienaCesMplsNotifAssociatedTunnelOperState_Object = MibTableColumn
cienaCesMplsNotifAssociatedTunnelOperState = _CienaCesMplsNotifAssociatedTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 14, 1, 1, 5),
    _CienaCesMplsNotifAssociatedTunnelOperState_Type()
)
cienaCesMplsNotifAssociatedTunnelOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifAssociatedTunnelOperState.setStatus("current")
_CienaCesMplsNotifAssociatedTunnelOamFaulted_Type = TunnelOamFault
_CienaCesMplsNotifAssociatedTunnelOamFaulted_Object = MibTableColumn
cienaCesMplsNotifAssociatedTunnelOamFaulted = _CienaCesMplsNotifAssociatedTunnelOamFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 14, 1, 1, 6),
    _CienaCesMplsNotifAssociatedTunnelOamFaulted_Type()
)
cienaCesMplsNotifAssociatedTunnelOamFaulted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifAssociatedTunnelOamFaulted.setStatus("current")
_CienaCesMplsNotifAssociatedTunnelFaultedNodeId_Type = IpAddress
_CienaCesMplsNotifAssociatedTunnelFaultedNodeId_Object = MibTableColumn
cienaCesMplsNotifAssociatedTunnelFaultedNodeId = _CienaCesMplsNotifAssociatedTunnelFaultedNodeId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 14, 1, 1, 7),
    _CienaCesMplsNotifAssociatedTunnelFaultedNodeId_Type()
)
cienaCesMplsNotifAssociatedTunnelFaultedNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifAssociatedTunnelFaultedNodeId.setStatus("current")
_CienaCesMplsCacInterfaceNotif_ObjectIdentity = ObjectIdentity
cienaCesMplsCacInterfaceNotif = _CienaCesMplsCacInterfaceNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 15)
)
_CienaCesMplsNotifCacInterfaceTable_Object = MibTable
cienaCesMplsNotifCacInterfaceTable = _CienaCesMplsNotifCacInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    cienaCesMplsNotifCacInterfaceTable.setStatus("current")
_CienaCesMplsNotifCacInterfaceEntry_Object = MibTableRow
cienaCesMplsNotifCacInterfaceEntry = _CienaCesMplsNotifCacInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 15, 1, 1)
)
cienaCesMplsNotifCacInterfaceEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsNotifCacInterfaceClassType"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsNotifCacInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsNotifCacInterfaceEntry.setStatus("current")


class _CienaCesMplsNotifCacInterfaceIndex_Type(Unsigned32):
    """Custom type cienaCesMplsNotifCacInterfaceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsNotifCacInterfaceIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsNotifCacInterfaceIndex_Object = MibTableColumn
cienaCesMplsNotifCacInterfaceIndex = _CienaCesMplsNotifCacInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 15, 1, 1, 1),
    _CienaCesMplsNotifCacInterfaceIndex_Type()
)
cienaCesMplsNotifCacInterfaceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifCacInterfaceIndex.setStatus("current")


class _CienaCesMplsNotifCacInterfaceClassType_Type(Unsigned32):
    """Custom type cienaCesMplsNotifCacInterfaceClassType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMplsNotifCacInterfaceClassType_Type.__name__ = "Unsigned32"
_CienaCesMplsNotifCacInterfaceClassType_Object = MibTableColumn
cienaCesMplsNotifCacInterfaceClassType = _CienaCesMplsNotifCacInterfaceClassType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 15, 1, 1, 2),
    _CienaCesMplsNotifCacInterfaceClassType_Type()
)
cienaCesMplsNotifCacInterfaceClassType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifCacInterfaceClassType.setStatus("current")
_CienaCesMplsNotifCacInterfaceName_Type = DisplayString
_CienaCesMplsNotifCacInterfaceName_Object = MibTableColumn
cienaCesMplsNotifCacInterfaceName = _CienaCesMplsNotifCacInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 15, 1, 1, 3),
    _CienaCesMplsNotifCacInterfaceName_Type()
)
cienaCesMplsNotifCacInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifCacInterfaceName.setStatus("current")


class _CienaCesMplsNotifCacInterfaceThreshold_Type(Unsigned32):
    """Custom type cienaCesMplsNotifCacInterfaceThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsNotifCacInterfaceThreshold_Type.__name__ = "Unsigned32"
_CienaCesMplsNotifCacInterfaceThreshold_Object = MibTableColumn
cienaCesMplsNotifCacInterfaceThreshold = _CienaCesMplsNotifCacInterfaceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 15, 1, 1, 4),
    _CienaCesMplsNotifCacInterfaceThreshold_Type()
)
cienaCesMplsNotifCacInterfaceThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsNotifCacInterfaceThreshold.setStatus("current")
_CienaCesMplsClassProfileTable_Object = MibTable
cienaCesMplsClassProfileTable = _CienaCesMplsClassProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 16)
)
if mibBuilder.loadTexts:
    cienaCesMplsClassProfileTable.setStatus("current")
_CienaCesMplsClassProfileEntry_Object = MibTableRow
cienaCesMplsClassProfileEntry = _CienaCesMplsClassProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 16, 1)
)
cienaCesMplsClassProfileEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsClassProfileIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsClassProfileEntry.setStatus("current")


class _CienaCesMplsClassProfileIndex_Type(Unsigned32):
    """Custom type cienaCesMplsClassProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_CienaCesMplsClassProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsClassProfileIndex_Object = MibTableColumn
cienaCesMplsClassProfileIndex = _CienaCesMplsClassProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 16, 1, 1),
    _CienaCesMplsClassProfileIndex_Type()
)
cienaCesMplsClassProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsClassProfileIndex.setStatus("current")


class _CienaCesMplsClassProfileName_Type(DisplayString):
    """Custom type cienaCesMplsClassProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsClassProfileName_Type.__name__ = "DisplayString"
_CienaCesMplsClassProfileName_Object = MibTableColumn
cienaCesMplsClassProfileName = _CienaCesMplsClassProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 16, 1, 2),
    _CienaCesMplsClassProfileName_Type()
)
cienaCesMplsClassProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsClassProfileName.setStatus("current")


class _CienaCesMplsClassProfileCacPolicy_Type(CacPolicy):
    """Custom type cienaCesMplsClassProfileCacPolicy based on CacPolicy"""


_CienaCesMplsClassProfileCacPolicy_Object = MibTableColumn
cienaCesMplsClassProfileCacPolicy = _CienaCesMplsClassProfileCacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 16, 1, 3),
    _CienaCesMplsClassProfileCacPolicy_Type()
)
cienaCesMplsClassProfileCacPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsClassProfileCacPolicy.setStatus("current")
_CienaCesMplsTEClassTypeTable_Object = MibTable
cienaCesMplsTEClassTypeTable = _CienaCesMplsTEClassTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 17)
)
if mibBuilder.loadTexts:
    cienaCesMplsTEClassTypeTable.setStatus("current")
_CienaCesMplsTEClassTypeEntry_Object = MibTableRow
cienaCesMplsTEClassTypeEntry = _CienaCesMplsTEClassTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 17, 1)
)
cienaCesMplsTEClassTypeEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsClassProfileIndex"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsClassType"),
)
if mibBuilder.loadTexts:
    cienaCesMplsTEClassTypeEntry.setStatus("current")


class _CienaCesMplsClassType_Type(Unsigned32):
    """Custom type cienaCesMplsClassType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMplsClassType_Type.__name__ = "Unsigned32"
_CienaCesMplsClassType_Object = MibTableColumn
cienaCesMplsClassType = _CienaCesMplsClassType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 17, 1, 1),
    _CienaCesMplsClassType_Type()
)
cienaCesMplsClassType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsClassType.setStatus("current")


class _CienaCesMplsClassTypeQueueGroupIndex_Type(Unsigned32):
    """Custom type cienaCesMplsClassTypeQueueGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_CienaCesMplsClassTypeQueueGroupIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsClassTypeQueueGroupIndex_Object = MibTableColumn
cienaCesMplsClassTypeQueueGroupIndex = _CienaCesMplsClassTypeQueueGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 17, 1, 2),
    _CienaCesMplsClassTypeQueueGroupIndex_Type()
)
cienaCesMplsClassTypeQueueGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsClassTypeQueueGroupIndex.setStatus("current")


class _CienaCesMplsClassTypeQueueGroupInstance_Type(Unsigned32):
    """Custom type cienaCesMplsClassTypeQueueGroupInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_CienaCesMplsClassTypeQueueGroupInstance_Type.__name__ = "Unsigned32"
_CienaCesMplsClassTypeQueueGroupInstance_Object = MibTableColumn
cienaCesMplsClassTypeQueueGroupInstance = _CienaCesMplsClassTypeQueueGroupInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 17, 1, 3),
    _CienaCesMplsClassTypeQueueGroupInstance_Type()
)
cienaCesMplsClassTypeQueueGroupInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsClassTypeQueueGroupInstance.setStatus("current")


class _CienaCesMplsClassTypeLom_Type(Unsigned32):
    """Custom type cienaCesMplsClassTypeLom based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CienaCesMplsClassTypeLom_Type.__name__ = "Unsigned32"
_CienaCesMplsClassTypeLom_Object = MibTableColumn
cienaCesMplsClassTypeLom = _CienaCesMplsClassTypeLom_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 17, 1, 4),
    _CienaCesMplsClassTypeLom_Type()
)
cienaCesMplsClassTypeLom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsClassTypeLom.setStatus("current")


class _CienaCesMplsClassTypeAlarmThreshold_Type(Unsigned32):
    """Custom type cienaCesMplsClassTypeAlarmThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CienaCesMplsClassTypeAlarmThreshold_Type.__name__ = "Unsigned32"
_CienaCesMplsClassTypeAlarmThreshold_Object = MibTableColumn
cienaCesMplsClassTypeAlarmThreshold = _CienaCesMplsClassTypeAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 1, 17, 1, 5),
    _CienaCesMplsClassTypeAlarmThreshold_Type()
)
cienaCesMplsClassTypeAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsClassTypeAlarmThreshold.setStatus("current")
_CienaCesGmpls_ObjectIdentity = ObjectIdentity
cienaCesGmpls = _CienaCesGmpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2)
)
_CienaCesGmplsStaticIngressUniDirTunnelTable_Object = MibTable
cienaCesGmplsStaticIngressUniDirTunnelTable = _CienaCesGmplsStaticIngressUniDirTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelTable.setStatus("current")
_CienaCesGmplsStaticIngressUniDirTunnelEntry_Object = MibTableRow
cienaCesGmplsStaticIngressUniDirTunnelEntry = _CienaCesGmplsStaticIngressUniDirTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1)
)
cienaCesGmplsStaticIngressUniDirTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsStaticIngressUniDirTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelEntry.setStatus("current")


class _CienaCesGmplsStaticIngressUniDirTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticIngressUniDirTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsStaticIngressUniDirTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticIngressUniDirTunnelIndex_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelIndex = _CienaCesGmplsStaticIngressUniDirTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 1),
    _CienaCesGmplsStaticIngressUniDirTunnelIndex_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelIndex.setStatus("current")


class _CienaCesGmplsStaticIngressUniDirTunnelName_Type(DisplayString):
    """Custom type cienaCesGmplsStaticIngressUniDirTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesGmplsStaticIngressUniDirTunnelName_Type.__name__ = "DisplayString"
_CienaCesGmplsStaticIngressUniDirTunnelName_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelName = _CienaCesGmplsStaticIngressUniDirTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 2),
    _CienaCesGmplsStaticIngressUniDirTunnelName_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelName.setStatus("current")
_CienaCesGmplsStaticIngressUniDirTunnelNextHopIp_Type = IpAddress
_CienaCesGmplsStaticIngressUniDirTunnelNextHopIp_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelNextHopIp = _CienaCesGmplsStaticIngressUniDirTunnelNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 3),
    _CienaCesGmplsStaticIngressUniDirTunnelNextHopIp_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelNextHopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelNextHopIp.setStatus("current")
_CienaCesGmplsStaticIngressUniDirTunnelSrcIpAddr_Type = IpAddress
_CienaCesGmplsStaticIngressUniDirTunnelSrcIpAddr_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelSrcIpAddr = _CienaCesGmplsStaticIngressUniDirTunnelSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 4),
    _CienaCesGmplsStaticIngressUniDirTunnelSrcIpAddr_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelSrcIpAddr.setStatus("current")
_CienaCesGmplsStaticIngressUniDirTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsStaticIngressUniDirTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelDestIpAddr = _CienaCesGmplsStaticIngressUniDirTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 5),
    _CienaCesGmplsStaticIngressUniDirTunnelDestIpAddr_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelDestIpAddr.setStatus("current")
_CienaCesGmplsStaticIngressUniDirTunnelAdminState_Type = CienaGlobalState
_CienaCesGmplsStaticIngressUniDirTunnelAdminState_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelAdminState = _CienaCesGmplsStaticIngressUniDirTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 6),
    _CienaCesGmplsStaticIngressUniDirTunnelAdminState_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelAdminState.setStatus("current")
_CienaCesGmplsStaticIngressUniDirTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsStaticIngressUniDirTunnelOperState_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelOperState = _CienaCesGmplsStaticIngressUniDirTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 7),
    _CienaCesGmplsStaticIngressUniDirTunnelOperState_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelOperState.setStatus("current")
_CienaCesGmplsStaticIngressUniDirTunnelForwardOutLabel_Type = Unsigned32
_CienaCesGmplsStaticIngressUniDirTunnelForwardOutLabel_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelForwardOutLabel = _CienaCesGmplsStaticIngressUniDirTunnelForwardOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 8),
    _CienaCesGmplsStaticIngressUniDirTunnelForwardOutLabel_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelForwardOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelForwardOutLabel.setStatus("current")


class _CienaCesGmplsStaticIngressUniDirTunnelProtectionRole_Type(Integer32):
    """Custom type cienaCesGmplsStaticIngressUniDirTunnelProtectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 0),
          ("primary", 1))
    )


_CienaCesGmplsStaticIngressUniDirTunnelProtectionRole_Type.__name__ = "Integer32"
_CienaCesGmplsStaticIngressUniDirTunnelProtectionRole_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelProtectionRole = _CienaCesGmplsStaticIngressUniDirTunnelProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 9),
    _CienaCesGmplsStaticIngressUniDirTunnelProtectionRole_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelProtectionRole.setStatus("current")
_CienaCesGmplsStaticIngressUniDirTunnelProtectionPartnerName_Type = DisplayString
_CienaCesGmplsStaticIngressUniDirTunnelProtectionPartnerName_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelProtectionPartnerName = _CienaCesGmplsStaticIngressUniDirTunnelProtectionPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 10),
    _CienaCesGmplsStaticIngressUniDirTunnelProtectionPartnerName_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelProtectionPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelProtectionPartnerName.setStatus("current")


class _CienaCesGmplsStaticIngressUniDirTunnelProtectionState_Type(Integer32):
    """Custom type cienaCesGmplsStaticIngressUniDirTunnelProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 0))
    )


_CienaCesGmplsStaticIngressUniDirTunnelProtectionState_Type.__name__ = "Integer32"
_CienaCesGmplsStaticIngressUniDirTunnelProtectionState_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelProtectionState = _CienaCesGmplsStaticIngressUniDirTunnelProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 11),
    _CienaCesGmplsStaticIngressUniDirTunnelProtectionState_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelProtectionState.setStatus("current")


class _CienaCesGmplsStaticIngressUniDirTunnelTTLPolicy_Type(TTLPolicy):
    """Custom type cienaCesGmplsStaticIngressUniDirTunnelTTLPolicy based on TTLPolicy"""


_CienaCesGmplsStaticIngressUniDirTunnelTTLPolicy_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelTTLPolicy = _CienaCesGmplsStaticIngressUniDirTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 12),
    _CienaCesGmplsStaticIngressUniDirTunnelTTLPolicy_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelTTLPolicy.setStatus("current")


class _CienaCesGmplsStaticIngressUniDirTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticIngressUniDirTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesGmplsStaticIngressUniDirTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticIngressUniDirTunnelFixedTTL_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelFixedTTL = _CienaCesGmplsStaticIngressUniDirTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 13),
    _CienaCesGmplsStaticIngressUniDirTunnelFixedTTL_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelFixedTTL.setStatus("current")
_CienaCesGmplsStaticIngressUniDirTunnelGrpIndex_Type = Unsigned32
_CienaCesGmplsStaticIngressUniDirTunnelGrpIndex_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelGrpIndex = _CienaCesGmplsStaticIngressUniDirTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 14),
    _CienaCesGmplsStaticIngressUniDirTunnelGrpIndex_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelGrpIndex.setStatus("current")


class _CienaCesGmplsStaticIngressUniDirTunnelReversion_Type(Integer32):
    """Custom type cienaCesGmplsStaticIngressUniDirTunnelReversion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesGmplsStaticIngressUniDirTunnelReversion_Type.__name__ = "Integer32"
_CienaCesGmplsStaticIngressUniDirTunnelReversion_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelReversion = _CienaCesGmplsStaticIngressUniDirTunnelReversion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 15),
    _CienaCesGmplsStaticIngressUniDirTunnelReversion_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelReversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelReversion.setStatus("current")
_CienaCesGmplsStaticIngressUniDirTunnelReversionTimeout_Type = Unsigned32
_CienaCesGmplsStaticIngressUniDirTunnelReversionTimeout_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelReversionTimeout = _CienaCesGmplsStaticIngressUniDirTunnelReversionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 16),
    _CienaCesGmplsStaticIngressUniDirTunnelReversionTimeout_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelReversionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelReversionTimeout.setStatus("current")


class _CienaCesGmplsStaticIngressUniDirTunnelCosProfileIndex_Type(Integer32):
    """Custom type cienaCesGmplsStaticIngressUniDirTunnelCosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsStaticIngressUniDirTunnelCosProfileIndex_Type.__name__ = "Integer32"
_CienaCesGmplsStaticIngressUniDirTunnelCosProfileIndex_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelCosProfileIndex = _CienaCesGmplsStaticIngressUniDirTunnelCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 17),
    _CienaCesGmplsStaticIngressUniDirTunnelCosProfileIndex_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelCosProfileIndex.setStatus("current")
_CienaCesGmplsStaticIngressUniDirTunnelCosProfileName_Type = DisplayString
_CienaCesGmplsStaticIngressUniDirTunnelCosProfileName_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelCosProfileName = _CienaCesGmplsStaticIngressUniDirTunnelCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 18),
    _CienaCesGmplsStaticIngressUniDirTunnelCosProfileName_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelCosProfileName.setStatus("current")


class _CienaCesGmplsStaticIngressUniDirTunnelRecoveryDisjoint_Type(Integer32):
    """Custom type cienaCesGmplsStaticIngressUniDirTunnelRecoveryDisjoint based on Integer32"""
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
        *(("link", 2),
          ("node", 3),
          ("none", 1),
          ("srlg", 4),
          ("unknown", 5))
    )


_CienaCesGmplsStaticIngressUniDirTunnelRecoveryDisjoint_Type.__name__ = "Integer32"
_CienaCesGmplsStaticIngressUniDirTunnelRecoveryDisjoint_Object = MibTableColumn
cienaCesGmplsStaticIngressUniDirTunnelRecoveryDisjoint = _CienaCesGmplsStaticIngressUniDirTunnelRecoveryDisjoint_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 1, 1, 19),
    _CienaCesGmplsStaticIngressUniDirTunnelRecoveryDisjoint_Type()
)
cienaCesGmplsStaticIngressUniDirTunnelRecoveryDisjoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressUniDirTunnelRecoveryDisjoint.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelTable_Object = MibTable
cienaCesGmplsStaticIngressCoroutedTunnelTable = _CienaCesGmplsStaticIngressCoroutedTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelTable.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelEntry_Object = MibTableRow
cienaCesGmplsStaticIngressCoroutedTunnelEntry = _CienaCesGmplsStaticIngressCoroutedTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1)
)
cienaCesGmplsStaticIngressCoroutedTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsStaticIngressCoroutedTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelEntry.setStatus("current")


class _CienaCesGmplsStaticIngressCoroutedTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticIngressCoroutedTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsStaticIngressCoroutedTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticIngressCoroutedTunnelIndex_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelIndex = _CienaCesGmplsStaticIngressCoroutedTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 1),
    _CienaCesGmplsStaticIngressCoroutedTunnelIndex_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelIndex.setStatus("current")


class _CienaCesGmplsStaticIngressCoroutedTunnelName_Type(DisplayString):
    """Custom type cienaCesGmplsStaticIngressCoroutedTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesGmplsStaticIngressCoroutedTunnelName_Type.__name__ = "DisplayString"
_CienaCesGmplsStaticIngressCoroutedTunnelName_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelName = _CienaCesGmplsStaticIngressCoroutedTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 2),
    _CienaCesGmplsStaticIngressCoroutedTunnelName_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelName.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelNextHopIp_Type = IpAddress
_CienaCesGmplsStaticIngressCoroutedTunnelNextHopIp_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelNextHopIp = _CienaCesGmplsStaticIngressCoroutedTunnelNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 3),
    _CienaCesGmplsStaticIngressCoroutedTunnelNextHopIp_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelNextHopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelNextHopIp.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelSrcIpAddr_Type = IpAddress
_CienaCesGmplsStaticIngressCoroutedTunnelSrcIpAddr_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelSrcIpAddr = _CienaCesGmplsStaticIngressCoroutedTunnelSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 4),
    _CienaCesGmplsStaticIngressCoroutedTunnelSrcIpAddr_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelSrcIpAddr.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsStaticIngressCoroutedTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelDestIpAddr = _CienaCesGmplsStaticIngressCoroutedTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 5),
    _CienaCesGmplsStaticIngressCoroutedTunnelDestIpAddr_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelDestIpAddr.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelAdminState_Type = CienaGlobalState
_CienaCesGmplsStaticIngressCoroutedTunnelAdminState_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelAdminState = _CienaCesGmplsStaticIngressCoroutedTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 6),
    _CienaCesGmplsStaticIngressCoroutedTunnelAdminState_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelAdminState.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsStaticIngressCoroutedTunnelOperState_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelOperState = _CienaCesGmplsStaticIngressCoroutedTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 7),
    _CienaCesGmplsStaticIngressCoroutedTunnelOperState_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelOperState.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelForwardOutLabel_Type = Unsigned32
_CienaCesGmplsStaticIngressCoroutedTunnelForwardOutLabel_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelForwardOutLabel = _CienaCesGmplsStaticIngressCoroutedTunnelForwardOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 8),
    _CienaCesGmplsStaticIngressCoroutedTunnelForwardOutLabel_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelForwardOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelForwardOutLabel.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelReverseInLabel_Type = Unsigned32
_CienaCesGmplsStaticIngressCoroutedTunnelReverseInLabel_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelReverseInLabel = _CienaCesGmplsStaticIngressCoroutedTunnelReverseInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 9),
    _CienaCesGmplsStaticIngressCoroutedTunnelReverseInLabel_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelReverseInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelReverseInLabel.setStatus("current")


class _CienaCesGmplsStaticIngressCoroutedTunnelProtectionRole_Type(Integer32):
    """Custom type cienaCesGmplsStaticIngressCoroutedTunnelProtectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 0),
          ("primary", 1))
    )


_CienaCesGmplsStaticIngressCoroutedTunnelProtectionRole_Type.__name__ = "Integer32"
_CienaCesGmplsStaticIngressCoroutedTunnelProtectionRole_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelProtectionRole = _CienaCesGmplsStaticIngressCoroutedTunnelProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 10),
    _CienaCesGmplsStaticIngressCoroutedTunnelProtectionRole_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelProtectionRole.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelProtectionPartnerName_Type = DisplayString
_CienaCesGmplsStaticIngressCoroutedTunnelProtectionPartnerName_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelProtectionPartnerName = _CienaCesGmplsStaticIngressCoroutedTunnelProtectionPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 11),
    _CienaCesGmplsStaticIngressCoroutedTunnelProtectionPartnerName_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelProtectionPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelProtectionPartnerName.setStatus("current")


class _CienaCesGmplsStaticIngressCoroutedTunnelProtectionState_Type(Integer32):
    """Custom type cienaCesGmplsStaticIngressCoroutedTunnelProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 0))
    )


_CienaCesGmplsStaticIngressCoroutedTunnelProtectionState_Type.__name__ = "Integer32"
_CienaCesGmplsStaticIngressCoroutedTunnelProtectionState_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelProtectionState = _CienaCesGmplsStaticIngressCoroutedTunnelProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 12),
    _CienaCesGmplsStaticIngressCoroutedTunnelProtectionState_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelProtectionState.setStatus("current")


class _CienaCesGmplsStaticIngressCoroutedTunnelTTLPolicy_Type(TTLPolicy):
    """Custom type cienaCesGmplsStaticIngressCoroutedTunnelTTLPolicy based on TTLPolicy"""


_CienaCesGmplsStaticIngressCoroutedTunnelTTLPolicy_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelTTLPolicy = _CienaCesGmplsStaticIngressCoroutedTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 13),
    _CienaCesGmplsStaticIngressCoroutedTunnelTTLPolicy_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelTTLPolicy.setStatus("current")


class _CienaCesGmplsStaticIngressCoroutedTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticIngressCoroutedTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesGmplsStaticIngressCoroutedTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticIngressCoroutedTunnelFixedTTL_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelFixedTTL = _CienaCesGmplsStaticIngressCoroutedTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 14),
    _CienaCesGmplsStaticIngressCoroutedTunnelFixedTTL_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelFixedTTL.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelGrpIndex_Type = Unsigned32
_CienaCesGmplsStaticIngressCoroutedTunnelGrpIndex_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelGrpIndex = _CienaCesGmplsStaticIngressCoroutedTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 15),
    _CienaCesGmplsStaticIngressCoroutedTunnelGrpIndex_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelGrpIndex.setStatus("current")


class _CienaCesGmplsStaticIngressCoroutedTunnelReversion_Type(Integer32):
    """Custom type cienaCesGmplsStaticIngressCoroutedTunnelReversion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesGmplsStaticIngressCoroutedTunnelReversion_Type.__name__ = "Integer32"
_CienaCesGmplsStaticIngressCoroutedTunnelReversion_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelReversion = _CienaCesGmplsStaticIngressCoroutedTunnelReversion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 16),
    _CienaCesGmplsStaticIngressCoroutedTunnelReversion_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelReversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelReversion.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelReversionTimeout_Type = Unsigned32
_CienaCesGmplsStaticIngressCoroutedTunnelReversionTimeout_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelReversionTimeout = _CienaCesGmplsStaticIngressCoroutedTunnelReversionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 17),
    _CienaCesGmplsStaticIngressCoroutedTunnelReversionTimeout_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelReversionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelReversionTimeout.setStatus("current")


class _CienaCesGmplsStaticIngressCoroutedTunnelCosProfileIndex_Type(Integer32):
    """Custom type cienaCesGmplsStaticIngressCoroutedTunnelCosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsStaticIngressCoroutedTunnelCosProfileIndex_Type.__name__ = "Integer32"
_CienaCesGmplsStaticIngressCoroutedTunnelCosProfileIndex_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelCosProfileIndex = _CienaCesGmplsStaticIngressCoroutedTunnelCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 18),
    _CienaCesGmplsStaticIngressCoroutedTunnelCosProfileIndex_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelCosProfileIndex.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelCosProfileName_Type = DisplayString
_CienaCesGmplsStaticIngressCoroutedTunnelCosProfileName_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelCosProfileName = _CienaCesGmplsStaticIngressCoroutedTunnelCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 19),
    _CienaCesGmplsStaticIngressCoroutedTunnelCosProfileName_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelCosProfileName.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelBfdMonitoring_Type = CienaGlobalState
_CienaCesGmplsStaticIngressCoroutedTunnelBfdMonitoring_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelBfdMonitoring = _CienaCesGmplsStaticIngressCoroutedTunnelBfdMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 20),
    _CienaCesGmplsStaticIngressCoroutedTunnelBfdMonitoring_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelBfdMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelBfdMonitoring.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelBfdProfileName_Type = DisplayString
_CienaCesGmplsStaticIngressCoroutedTunnelBfdProfileName_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelBfdProfileName = _CienaCesGmplsStaticIngressCoroutedTunnelBfdProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 21),
    _CienaCesGmplsStaticIngressCoroutedTunnelBfdProfileName_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelBfdProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelBfdProfileName.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelBfdSessionName_Type = DisplayString
_CienaCesGmplsStaticIngressCoroutedTunnelBfdSessionName_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelBfdSessionName = _CienaCesGmplsStaticIngressCoroutedTunnelBfdSessionName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 22),
    _CienaCesGmplsStaticIngressCoroutedTunnelBfdSessionName_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelBfdSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelBfdSessionName.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelAisMonitoring_Type = CienaGlobalState
_CienaCesGmplsStaticIngressCoroutedTunnelAisMonitoring_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelAisMonitoring = _CienaCesGmplsStaticIngressCoroutedTunnelAisMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 23),
    _CienaCesGmplsStaticIngressCoroutedTunnelAisMonitoring_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelAisMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelAisMonitoring.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelAisProfileName_Type = DisplayString
_CienaCesGmplsStaticIngressCoroutedTunnelAisProfileName_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelAisProfileName = _CienaCesGmplsStaticIngressCoroutedTunnelAisProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 24),
    _CienaCesGmplsStaticIngressCoroutedTunnelAisProfileName_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelAisProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelAisProfileName.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelBfdSessionFaulted_Type = Integer32
_CienaCesGmplsStaticIngressCoroutedTunnelBfdSessionFaulted_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelBfdSessionFaulted = _CienaCesGmplsStaticIngressCoroutedTunnelBfdSessionFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 25),
    _CienaCesGmplsStaticIngressCoroutedTunnelBfdSessionFaulted_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelBfdSessionFaulted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelBfdSessionFaulted.setStatus("current")


class _CienaCesGmplsStaticIngressCoroutedTunnelBfdProfileIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticIngressCoroutedTunnelBfdProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsStaticIngressCoroutedTunnelBfdProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticIngressCoroutedTunnelBfdProfileIndex_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelBfdProfileIndex = _CienaCesGmplsStaticIngressCoroutedTunnelBfdProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 26),
    _CienaCesGmplsStaticIngressCoroutedTunnelBfdProfileIndex_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelBfdProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelBfdProfileIndex.setStatus("current")


class _CienaCesGmplsStaticIngressCoroutedTunnelRecoveryDisjoint_Type(Integer32):
    """Custom type cienaCesGmplsStaticIngressCoroutedTunnelRecoveryDisjoint based on Integer32"""
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
        *(("link", 2),
          ("node", 3),
          ("none", 1),
          ("srlg", 4),
          ("unknown", 5))
    )


_CienaCesGmplsStaticIngressCoroutedTunnelRecoveryDisjoint_Type.__name__ = "Integer32"
_CienaCesGmplsStaticIngressCoroutedTunnelRecoveryDisjoint_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelRecoveryDisjoint = _CienaCesGmplsStaticIngressCoroutedTunnelRecoveryDisjoint_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 27),
    _CienaCesGmplsStaticIngressCoroutedTunnelRecoveryDisjoint_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelRecoveryDisjoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelRecoveryDisjoint.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelNextHopIfNum_Type = Unsigned32
_CienaCesGmplsStaticIngressCoroutedTunnelNextHopIfNum_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelNextHopIfNum = _CienaCesGmplsStaticIngressCoroutedTunnelNextHopIfNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 28),
    _CienaCesGmplsStaticIngressCoroutedTunnelNextHopIfNum_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelNextHopIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelNextHopIfNum.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelLspId_Type = Unsigned32
_CienaCesGmplsStaticIngressCoroutedTunnelLspId_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelLspId = _CienaCesGmplsStaticIngressCoroutedTunnelLspId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 29),
    _CienaCesGmplsStaticIngressCoroutedTunnelLspId_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelLspId.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelSrcTunnelId_Type = Unsigned32
_CienaCesGmplsStaticIngressCoroutedTunnelSrcTunnelId_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelSrcTunnelId = _CienaCesGmplsStaticIngressCoroutedTunnelSrcTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 30),
    _CienaCesGmplsStaticIngressCoroutedTunnelSrcTunnelId_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelSrcTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelSrcTunnelId.setStatus("current")
_CienaCesGmplsStaticIngressCoroutedTunnelDestTunnelId_Type = Unsigned32
_CienaCesGmplsStaticIngressCoroutedTunnelDestTunnelId_Object = MibTableColumn
cienaCesGmplsStaticIngressCoroutedTunnelDestTunnelId = _CienaCesGmplsStaticIngressCoroutedTunnelDestTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 2, 1, 31),
    _CienaCesGmplsStaticIngressCoroutedTunnelDestTunnelId_Type()
)
cienaCesGmplsStaticIngressCoroutedTunnelDestTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticIngressCoroutedTunnelDestTunnelId.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelTable_Object = MibTable
cienaCesGmplsDynamicIngressUniDirTunnelTable = _CienaCesGmplsDynamicIngressUniDirTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelTable.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelEntry_Object = MibTableRow
cienaCesGmplsDynamicIngressUniDirTunnelEntry = _CienaCesGmplsDynamicIngressUniDirTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1)
)
cienaCesGmplsDynamicIngressUniDirTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsDynamicIngressUniDirTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelEntry.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsDynamicIngressUniDirTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressUniDirTunnelIndex_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelIndex = _CienaCesGmplsDynamicIngressUniDirTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 1),
    _CienaCesGmplsDynamicIngressUniDirTunnelIndex_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelIndex.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelName_Type(DisplayString):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesGmplsDynamicIngressUniDirTunnelName_Type.__name__ = "DisplayString"
_CienaCesGmplsDynamicIngressUniDirTunnelName_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelName = _CienaCesGmplsDynamicIngressUniDirTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 2),
    _CienaCesGmplsDynamicIngressUniDirTunnelName_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelName.setStatus("current")
_CienaCesMplsDynamicIngressUniDirTunnelLspId_Type = Unsigned32
_CienaCesMplsDynamicIngressUniDirTunnelLspId_Object = MibTableColumn
cienaCesMplsDynamicIngressUniDirTunnelLspId = _CienaCesMplsDynamicIngressUniDirTunnelLspId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 3),
    _CienaCesMplsDynamicIngressUniDirTunnelLspId_Type()
)
cienaCesMplsDynamicIngressUniDirTunnelLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsDynamicIngressUniDirTunnelLspId.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelNextHopIp_Type = IpAddress
_CienaCesGmplsDynamicIngressUniDirTunnelNextHopIp_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelNextHopIp = _CienaCesGmplsDynamicIngressUniDirTunnelNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 4),
    _CienaCesGmplsDynamicIngressUniDirTunnelNextHopIp_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelNextHopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelNextHopIp.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelSrcIpAddr_Type = IpAddress
_CienaCesGmplsDynamicIngressUniDirTunnelSrcIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelSrcIpAddr = _CienaCesGmplsDynamicIngressUniDirTunnelSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 5),
    _CienaCesGmplsDynamicIngressUniDirTunnelSrcIpAddr_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelSrcIpAddr.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsDynamicIngressUniDirTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelDestIpAddr = _CienaCesGmplsDynamicIngressUniDirTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 6),
    _CienaCesGmplsDynamicIngressUniDirTunnelDestIpAddr_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelDestIpAddr.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelAdminState_Type = CienaGlobalState
_CienaCesGmplsDynamicIngressUniDirTunnelAdminState_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelAdminState = _CienaCesGmplsDynamicIngressUniDirTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 7),
    _CienaCesGmplsDynamicIngressUniDirTunnelAdminState_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelAdminState.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsDynamicIngressUniDirTunnelOperState_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelOperState = _CienaCesGmplsDynamicIngressUniDirTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 8),
    _CienaCesGmplsDynamicIngressUniDirTunnelOperState_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelOperState.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelForwardOutLabel_Type = Unsigned32
_CienaCesGmplsDynamicIngressUniDirTunnelForwardOutLabel_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelForwardOutLabel = _CienaCesGmplsDynamicIngressUniDirTunnelForwardOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 9),
    _CienaCesGmplsDynamicIngressUniDirTunnelForwardOutLabel_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelForwardOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelForwardOutLabel.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelProtectionRole_Type(Integer32):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelProtectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 0),
          ("primary", 1))
    )


_CienaCesGmplsDynamicIngressUniDirTunnelProtectionRole_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicIngressUniDirTunnelProtectionRole_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelProtectionRole = _CienaCesGmplsDynamicIngressUniDirTunnelProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 10),
    _CienaCesGmplsDynamicIngressUniDirTunnelProtectionRole_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelProtectionRole.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelProtectionPartnerName_Type = DisplayString
_CienaCesGmplsDynamicIngressUniDirTunnelProtectionPartnerName_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelProtectionPartnerName = _CienaCesGmplsDynamicIngressUniDirTunnelProtectionPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 11),
    _CienaCesGmplsDynamicIngressUniDirTunnelProtectionPartnerName_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelProtectionPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelProtectionPartnerName.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelProtectionState_Type(Integer32):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 0))
    )


_CienaCesGmplsDynamicIngressUniDirTunnelProtectionState_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicIngressUniDirTunnelProtectionState_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelProtectionState = _CienaCesGmplsDynamicIngressUniDirTunnelProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 12),
    _CienaCesGmplsDynamicIngressUniDirTunnelProtectionState_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelProtectionState.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelTTLPolicy_Type(TTLPolicy):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelTTLPolicy based on TTLPolicy"""


_CienaCesGmplsDynamicIngressUniDirTunnelTTLPolicy_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelTTLPolicy = _CienaCesGmplsDynamicIngressUniDirTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 13),
    _CienaCesGmplsDynamicIngressUniDirTunnelTTLPolicy_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelTTLPolicy.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesGmplsDynamicIngressUniDirTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressUniDirTunnelFixedTTL_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelFixedTTL = _CienaCesGmplsDynamicIngressUniDirTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 14),
    _CienaCesGmplsDynamicIngressUniDirTunnelFixedTTL_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelFixedTTL.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelGrpIndex_Type = Unsigned32
_CienaCesGmplsDynamicIngressUniDirTunnelGrpIndex_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelGrpIndex = _CienaCesGmplsDynamicIngressUniDirTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 15),
    _CienaCesGmplsDynamicIngressUniDirTunnelGrpIndex_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelGrpIndex.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelReversion_Type(Integer32):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelReversion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesGmplsDynamicIngressUniDirTunnelReversion_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicIngressUniDirTunnelReversion_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelReversion = _CienaCesGmplsDynamicIngressUniDirTunnelReversion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 16),
    _CienaCesGmplsDynamicIngressUniDirTunnelReversion_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelReversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelReversion.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelReversionTimeout_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelReversionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsDynamicIngressUniDirTunnelReversionTimeout_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressUniDirTunnelReversionTimeout_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelReversionTimeout = _CienaCesGmplsDynamicIngressUniDirTunnelReversionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 17),
    _CienaCesGmplsDynamicIngressUniDirTunnelReversionTimeout_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelReversionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelReversionTimeout.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelCosProfileIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelCosProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsDynamicIngressUniDirTunnelCosProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressUniDirTunnelCosProfileIndex_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelCosProfileIndex = _CienaCesGmplsDynamicIngressUniDirTunnelCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 18),
    _CienaCesGmplsDynamicIngressUniDirTunnelCosProfileIndex_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelCosProfileIndex.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelCosProfileName_Type = DisplayString
_CienaCesGmplsDynamicIngressUniDirTunnelCosProfileName_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelCosProfileName = _CienaCesGmplsDynamicIngressUniDirTunnelCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 19),
    _CienaCesGmplsDynamicIngressUniDirTunnelCosProfileName_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelCosProfileName.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelRecordRoute_Type(Integer32):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelRecordRoute based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesGmplsDynamicIngressUniDirTunnelRecordRoute_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicIngressUniDirTunnelRecordRoute_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelRecordRoute = _CienaCesGmplsDynamicIngressUniDirTunnelRecordRoute_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 20),
    _CienaCesGmplsDynamicIngressUniDirTunnelRecordRoute_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelRecordRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelRecordRoute.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelFastRoute_Type(Integer32):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelFastRoute based on Integer32"""
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
        *(("link-protect", 2),
          ("node-protect", 3),
          ("none", 1))
    )


_CienaCesGmplsDynamicIngressUniDirTunnelFastRoute_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicIngressUniDirTunnelFastRoute_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelFastRoute = _CienaCesGmplsDynamicIngressUniDirTunnelFastRoute_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 21),
    _CienaCesGmplsDynamicIngressUniDirTunnelFastRoute_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelFastRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelFastRoute.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelSetupPriority_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesGmplsDynamicIngressUniDirTunnelSetupPriority_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressUniDirTunnelSetupPriority_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelSetupPriority = _CienaCesGmplsDynamicIngressUniDirTunnelSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 22),
    _CienaCesGmplsDynamicIngressUniDirTunnelSetupPriority_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelSetupPriority.setStatus("current")


class _CienaCesGmplsDynamicIngressUniDirTunnelHoldPriority_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressUniDirTunnelHoldPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesGmplsDynamicIngressUniDirTunnelHoldPriority_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressUniDirTunnelHoldPriority_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelHoldPriority = _CienaCesGmplsDynamicIngressUniDirTunnelHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 23),
    _CienaCesGmplsDynamicIngressUniDirTunnelHoldPriority_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelHoldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelHoldPriority.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelPathIndex_Type = Unsigned32
_CienaCesGmplsDynamicIngressUniDirTunnelPathIndex_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelPathIndex = _CienaCesGmplsDynamicIngressUniDirTunnelPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 24),
    _CienaCesGmplsDynamicIngressUniDirTunnelPathIndex_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelPathIndex.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelPathName_Type = DisplayString
_CienaCesGmplsDynamicIngressUniDirTunnelPathName_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelPathName = _CienaCesGmplsDynamicIngressUniDirTunnelPathName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 25),
    _CienaCesGmplsDynamicIngressUniDirTunnelPathName_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelPathName.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelBandwidthProfile_Type = DisplayString
_CienaCesGmplsDynamicIngressUniDirTunnelBandwidthProfile_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelBandwidthProfile = _CienaCesGmplsDynamicIngressUniDirTunnelBandwidthProfile_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 26),
    _CienaCesGmplsDynamicIngressUniDirTunnelBandwidthProfile_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelBandwidthProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelBandwidthProfile.setStatus("current")
_CienaCesGmplsDynamicIngressUniDirTunnelResourcePointer_Type = RowPointer
_CienaCesGmplsDynamicIngressUniDirTunnelResourcePointer_Object = MibTableColumn
cienaCesGmplsDynamicIngressUniDirTunnelResourcePointer = _CienaCesGmplsDynamicIngressUniDirTunnelResourcePointer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 3, 1, 27),
    _CienaCesGmplsDynamicIngressUniDirTunnelResourcePointer_Type()
)
cienaCesGmplsDynamicIngressUniDirTunnelResourcePointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressUniDirTunnelResourcePointer.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelTable_Object = MibTable
cienaCesGmplsDynamicIngressCoroutedTunnelTable = _CienaCesGmplsDynamicIngressCoroutedTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelTable.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelEntry_Object = MibTableRow
cienaCesGmplsDynamicIngressCoroutedTunnelEntry = _CienaCesGmplsDynamicIngressCoroutedTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1)
)
cienaCesGmplsDynamicIngressCoroutedTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsDynamicIngressCoroutedTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelEntry.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressCoroutedTunnelIndex_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelIndex = _CienaCesGmplsDynamicIngressCoroutedTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 1),
    _CienaCesGmplsDynamicIngressCoroutedTunnelIndex_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelIndex.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelName_Type(DisplayString):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelName_Type.__name__ = "DisplayString"
_CienaCesGmplsDynamicIngressCoroutedTunnelName_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelName = _CienaCesGmplsDynamicIngressCoroutedTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 2),
    _CienaCesGmplsDynamicIngressCoroutedTunnelName_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelName.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelNextHopIp_Type = IpAddress
_CienaCesGmplsDynamicIngressCoroutedTunnelNextHopIp_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelNextHopIp = _CienaCesGmplsDynamicIngressCoroutedTunnelNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 3),
    _CienaCesGmplsDynamicIngressCoroutedTunnelNextHopIp_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelNextHopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelNextHopIp.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelSrcIpAddr_Type = IpAddress
_CienaCesGmplsDynamicIngressCoroutedTunnelSrcIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelSrcIpAddr = _CienaCesGmplsDynamicIngressCoroutedTunnelSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 4),
    _CienaCesGmplsDynamicIngressCoroutedTunnelSrcIpAddr_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelSrcIpAddr.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsDynamicIngressCoroutedTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelDestIpAddr = _CienaCesGmplsDynamicIngressCoroutedTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 5),
    _CienaCesGmplsDynamicIngressCoroutedTunnelDestIpAddr_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelDestIpAddr.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelAdminState_Type = CienaGlobalState
_CienaCesGmplsDynamicIngressCoroutedTunnelAdminState_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelAdminState = _CienaCesGmplsDynamicIngressCoroutedTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 6),
    _CienaCesGmplsDynamicIngressCoroutedTunnelAdminState_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelAdminState.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsDynamicIngressCoroutedTunnelOperState_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelOperState = _CienaCesGmplsDynamicIngressCoroutedTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 7),
    _CienaCesGmplsDynamicIngressCoroutedTunnelOperState_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelOperState.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelForwardOutLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelForwardOutLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelForwardOutLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressCoroutedTunnelForwardOutLabel_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelForwardOutLabel = _CienaCesGmplsDynamicIngressCoroutedTunnelForwardOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 8),
    _CienaCesGmplsDynamicIngressCoroutedTunnelForwardOutLabel_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelForwardOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelForwardOutLabel.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelReverseInLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelReverseInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelReverseInLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressCoroutedTunnelReverseInLabel_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelReverseInLabel = _CienaCesGmplsDynamicIngressCoroutedTunnelReverseInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 9),
    _CienaCesGmplsDynamicIngressCoroutedTunnelReverseInLabel_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelReverseInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelReverseInLabel.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelProtectionRole_Type(Integer32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelProtectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 0),
          ("primary", 1))
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelProtectionRole_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicIngressCoroutedTunnelProtectionRole_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelProtectionRole = _CienaCesGmplsDynamicIngressCoroutedTunnelProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 10),
    _CienaCesGmplsDynamicIngressCoroutedTunnelProtectionRole_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelProtectionRole.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelProtectionPartnerName_Type = DisplayString
_CienaCesGmplsDynamicIngressCoroutedTunnelProtectionPartnerName_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelProtectionPartnerName = _CienaCesGmplsDynamicIngressCoroutedTunnelProtectionPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 11),
    _CienaCesGmplsDynamicIngressCoroutedTunnelProtectionPartnerName_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelProtectionPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelProtectionPartnerName.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelProtectionState_Type(Integer32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 0))
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelProtectionState_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicIngressCoroutedTunnelProtectionState_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelProtectionState = _CienaCesGmplsDynamicIngressCoroutedTunnelProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 12),
    _CienaCesGmplsDynamicIngressCoroutedTunnelProtectionState_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelProtectionState.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelTTLPolicy_Type(TTLPolicy):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelTTLPolicy based on TTLPolicy"""


_CienaCesGmplsDynamicIngressCoroutedTunnelTTLPolicy_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelTTLPolicy = _CienaCesGmplsDynamicIngressCoroutedTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 13),
    _CienaCesGmplsDynamicIngressCoroutedTunnelTTLPolicy_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelTTLPolicy.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressCoroutedTunnelFixedTTL_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelFixedTTL = _CienaCesGmplsDynamicIngressCoroutedTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 14),
    _CienaCesGmplsDynamicIngressCoroutedTunnelFixedTTL_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelFixedTTL.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelGrpIndex_Type = Unsigned32
_CienaCesGmplsDynamicIngressCoroutedTunnelGrpIndex_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelGrpIndex = _CienaCesGmplsDynamicIngressCoroutedTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 15),
    _CienaCesGmplsDynamicIngressCoroutedTunnelGrpIndex_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelGrpIndex.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelReversion_Type(Integer32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelReversion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelReversion_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicIngressCoroutedTunnelReversion_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelReversion = _CienaCesGmplsDynamicIngressCoroutedTunnelReversion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 16),
    _CienaCesGmplsDynamicIngressCoroutedTunnelReversion_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelReversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelReversion.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelReversionTimeout_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelReversionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelReversionTimeout_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressCoroutedTunnelReversionTimeout_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelReversionTimeout = _CienaCesGmplsDynamicIngressCoroutedTunnelReversionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 17),
    _CienaCesGmplsDynamicIngressCoroutedTunnelReversionTimeout_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelReversionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelReversionTimeout.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelCosProfileIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelCosProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelCosProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressCoroutedTunnelCosProfileIndex_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelCosProfileIndex = _CienaCesGmplsDynamicIngressCoroutedTunnelCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 18),
    _CienaCesGmplsDynamicIngressCoroutedTunnelCosProfileIndex_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelCosProfileIndex.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelCosProfileName_Type = DisplayString
_CienaCesGmplsDynamicIngressCoroutedTunnelCosProfileName_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelCosProfileName = _CienaCesGmplsDynamicIngressCoroutedTunnelCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 19),
    _CienaCesGmplsDynamicIngressCoroutedTunnelCosProfileName_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelCosProfileName.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelRecordRoute_Type(Integer32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelRecordRoute based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelRecordRoute_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicIngressCoroutedTunnelRecordRoute_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelRecordRoute = _CienaCesGmplsDynamicIngressCoroutedTunnelRecordRoute_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 20),
    _CienaCesGmplsDynamicIngressCoroutedTunnelRecordRoute_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelRecordRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelRecordRoute.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelFastRoute_Type(Integer32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelFastRoute based on Integer32"""
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
        *(("link-protect", 2),
          ("node-protect", 3),
          ("none", 1))
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelFastRoute_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicIngressCoroutedTunnelFastRoute_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelFastRoute = _CienaCesGmplsDynamicIngressCoroutedTunnelFastRoute_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 21),
    _CienaCesGmplsDynamicIngressCoroutedTunnelFastRoute_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelFastRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelFastRoute.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelSetupPriority_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelSetupPriority_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressCoroutedTunnelSetupPriority_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelSetupPriority = _CienaCesGmplsDynamicIngressCoroutedTunnelSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 22),
    _CienaCesGmplsDynamicIngressCoroutedTunnelSetupPriority_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelSetupPriority.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelHoldPriority_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelHoldPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelHoldPriority_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressCoroutedTunnelHoldPriority_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelHoldPriority = _CienaCesGmplsDynamicIngressCoroutedTunnelHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 23),
    _CienaCesGmplsDynamicIngressCoroutedTunnelHoldPriority_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelHoldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelHoldPriority.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelPathIndex_Type = Unsigned32
_CienaCesGmplsDynamicIngressCoroutedTunnelPathIndex_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelPathIndex = _CienaCesGmplsDynamicIngressCoroutedTunnelPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 24),
    _CienaCesGmplsDynamicIngressCoroutedTunnelPathIndex_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelPathIndex.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelPathName_Type = DisplayString
_CienaCesGmplsDynamicIngressCoroutedTunnelPathName_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelPathName = _CienaCesGmplsDynamicIngressCoroutedTunnelPathName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 25),
    _CienaCesGmplsDynamicIngressCoroutedTunnelPathName_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelPathName.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelBandwidthProfile_Type = DisplayString
_CienaCesGmplsDynamicIngressCoroutedTunnelBandwidthProfile_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelBandwidthProfile = _CienaCesGmplsDynamicIngressCoroutedTunnelBandwidthProfile_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 26),
    _CienaCesGmplsDynamicIngressCoroutedTunnelBandwidthProfile_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelBandwidthProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelBandwidthProfile.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelResourcePointer_Type = RowPointer
_CienaCesGmplsDynamicIngressCoroutedTunnelResourcePointer_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelResourcePointer = _CienaCesGmplsDynamicIngressCoroutedTunnelResourcePointer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 27),
    _CienaCesGmplsDynamicIngressCoroutedTunnelResourcePointer_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelResourcePointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelResourcePointer.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelBfdMonitoring_Type = CienaGlobalState
_CienaCesGmplsDynamicIngressCoroutedTunnelBfdMonitoring_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelBfdMonitoring = _CienaCesGmplsDynamicIngressCoroutedTunnelBfdMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 28),
    _CienaCesGmplsDynamicIngressCoroutedTunnelBfdMonitoring_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelBfdMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelBfdMonitoring.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileName_Type = DisplayString
_CienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileName_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileName = _CienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 29),
    _CienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileName_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileName.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionName_Type = DisplayString
_CienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionName_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionName = _CienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 30),
    _CienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionName_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionName.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionFaulted_Type = Integer32
_CienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionFaulted_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionFaulted = _CienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 31),
    _CienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionFaulted_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionFaulted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionFaulted.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileIndex_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileIndex = _CienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 32),
    _CienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileIndex_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileIndex.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelAutoBackupEnable_Type = Integer32
_CienaCesGmplsDynamicIngressCoroutedTunnelAutoBackupEnable_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelAutoBackupEnable = _CienaCesGmplsDynamicIngressCoroutedTunnelAutoBackupEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 33),
    _CienaCesGmplsDynamicIngressCoroutedTunnelAutoBackupEnable_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelAutoBackupEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelAutoBackupEnable.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelLspReoptimization_Type = MplsGlobalState
_CienaCesGmplsDynamicIngressCoroutedTunnelLspReoptimization_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelLspReoptimization = _CienaCesGmplsDynamicIngressCoroutedTunnelLspReoptimization_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 34),
    _CienaCesGmplsDynamicIngressCoroutedTunnelLspReoptimization_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelLspReoptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelLspReoptimization.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelLspReOptTimeInterval_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelLspReOptTimeInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelLspReOptTimeInterval_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressCoroutedTunnelLspReOptTimeInterval_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelLspReOptTimeInterval = _CienaCesGmplsDynamicIngressCoroutedTunnelLspReOptTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 35),
    _CienaCesGmplsDynamicIngressCoroutedTunnelLspReOptTimeInterval_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelLspReOptTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelLspReOptTimeInterval.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointType_Type(PathDisjointType):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointType based on PathDisjointType"""


_CienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointType_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointType = _CienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 36),
    _CienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointType_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointType.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointMode_Type(PathDisjointMode):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointMode based on PathDisjointMode"""


_CienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointMode_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointMode = _CienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 37),
    _CienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointMode_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointMode.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeEnable_Type = MplsGlobalState
_CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeEnable_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeEnable = _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 38),
    _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeEnable_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeEnable.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeInterval_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeInterval_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeInterval_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeInterval = _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 39),
    _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeInterval_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeInterval.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeFailureHdlr_Type(AutoSizeFailHdlr):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeFailureHdlr based on AutoSizeFailHdlr"""


_CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeFailureHdlr_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeFailureHdlr = _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeFailureHdlr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 40),
    _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeFailureHdlr_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeFailureHdlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeFailureHdlr.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeState_Type = AutoSizeState
_CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeState_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeState = _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 41),
    _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeState_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeState.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeMode_Type(AutoSizeMode):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeMode based on AutoSizeMode"""


_CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeMode_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeMode = _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 42),
    _CienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeMode_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeMode.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelMinBandwidth_Type(MplsBitRate):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelMinBandwidth based on MplsBitRate"""
    defaultValue = 0


_CienaCesGmplsDynamicIngressCoroutedTunnelMinBandwidth_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelMinBandwidth = _CienaCesGmplsDynamicIngressCoroutedTunnelMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 43),
    _CienaCesGmplsDynamicIngressCoroutedTunnelMinBandwidth_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelMinBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelMinBandwidth.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelMaxBandwidth_Type(MplsBitRate):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelMaxBandwidth based on MplsBitRate"""
    defaultValue = 1000000000


_CienaCesGmplsDynamicIngressCoroutedTunnelMaxBandwidth_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelMaxBandwidth = _CienaCesGmplsDynamicIngressCoroutedTunnelMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 44),
    _CienaCesGmplsDynamicIngressCoroutedTunnelMaxBandwidth_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelMaxBandwidth.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelIncBandwidth_Type(MplsBitRate):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelIncBandwidth based on MplsBitRate"""
    defaultValue = 0


_CienaCesGmplsDynamicIngressCoroutedTunnelIncBandwidth_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelIncBandwidth = _CienaCesGmplsDynamicIngressCoroutedTunnelIncBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 45),
    _CienaCesGmplsDynamicIngressCoroutedTunnelIncBandwidth_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelIncBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelIncBandwidth.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelCurBandwidth_Type = MplsBitRate
_CienaCesGmplsDynamicIngressCoroutedTunnelCurBandwidth_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelCurBandwidth = _CienaCesGmplsDynamicIngressCoroutedTunnelCurBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 46),
    _CienaCesGmplsDynamicIngressCoroutedTunnelCurBandwidth_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelCurBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelCurBandwidth.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelReqBandwidth_Type = MplsBitRate
_CienaCesGmplsDynamicIngressCoroutedTunnelReqBandwidth_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelReqBandwidth = _CienaCesGmplsDynamicIngressCoroutedTunnelReqBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 47),
    _CienaCesGmplsDynamicIngressCoroutedTunnelReqBandwidth_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelReqBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelReqBandwidth.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelUsedBandwidth_Type = MplsBitRate
_CienaCesGmplsDynamicIngressCoroutedTunnelUsedBandwidth_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelUsedBandwidth = _CienaCesGmplsDynamicIngressCoroutedTunnelUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 48),
    _CienaCesGmplsDynamicIngressCoroutedTunnelUsedBandwidth_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelUsedBandwidth.setStatus("current")


class _CienaCesGmplsDynamicIngressCoroutedTunnelClassType_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicIngressCoroutedTunnelClassType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesGmplsDynamicIngressCoroutedTunnelClassType_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicIngressCoroutedTunnelClassType_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelClassType = _CienaCesGmplsDynamicIngressCoroutedTunnelClassType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 49),
    _CienaCesGmplsDynamicIngressCoroutedTunnelClassType_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelClassType.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAll_Type = Unsigned32
_CienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAll_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAll = _CienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAll_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 50),
    _CienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAll_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAll.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAny_Type = Unsigned32
_CienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAny_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAny = _CienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAny_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 51),
    _CienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAny_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAny.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedTunnelResourceExcludeAny_Type = Unsigned32
_CienaCesGmplsDynamicIngressCoroutedTunnelResourceExcludeAny_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedTunnelResourceExcludeAny = _CienaCesGmplsDynamicIngressCoroutedTunnelResourceExcludeAny_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 52),
    _CienaCesGmplsDynamicIngressCoroutedTunnelResourceExcludeAny_Type()
)
cienaCesGmplsDynamicIngressCoroutedTunnelResourceExcludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedTunnelResourceExcludeAny.setStatus("current")
_CienaCesGmplsDynamicIngressCoroutedLspId_Type = Unsigned32
_CienaCesGmplsDynamicIngressCoroutedLspId_Object = MibTableColumn
cienaCesGmplsDynamicIngressCoroutedLspId = _CienaCesGmplsDynamicIngressCoroutedLspId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 4, 1, 53),
    _CienaCesGmplsDynamicIngressCoroutedLspId_Type()
)
cienaCesGmplsDynamicIngressCoroutedLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicIngressCoroutedLspId.setStatus("current")
_CienaCesGmplsStaticEgressUniDirTunnelTable_Object = MibTable
cienaCesGmplsStaticEgressUniDirTunnelTable = _CienaCesGmplsStaticEgressUniDirTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressUniDirTunnelTable.setStatus("current")
_CienaCesGmplsStaticEgressUniDirTunnelEntry_Object = MibTableRow
cienaCesGmplsStaticEgressUniDirTunnelEntry = _CienaCesGmplsStaticEgressUniDirTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 5, 1)
)
cienaCesGmplsStaticEgressUniDirTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsStaticEgressUniDirTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressUniDirTunnelEntry.setStatus("current")
_CienaCesGmplsStaticEgressUniDirTunnelIndex_Type = Unsigned32
_CienaCesGmplsStaticEgressUniDirTunnelIndex_Object = MibTableColumn
cienaCesGmplsStaticEgressUniDirTunnelIndex = _CienaCesGmplsStaticEgressUniDirTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 5, 1, 1),
    _CienaCesGmplsStaticEgressUniDirTunnelIndex_Type()
)
cienaCesGmplsStaticEgressUniDirTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressUniDirTunnelIndex.setStatus("current")


class _CienaCesGmplsStaticEgressUniDirTunnelName_Type(DisplayString):
    """Custom type cienaCesGmplsStaticEgressUniDirTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesGmplsStaticEgressUniDirTunnelName_Type.__name__ = "DisplayString"
_CienaCesGmplsStaticEgressUniDirTunnelName_Object = MibTableColumn
cienaCesGmplsStaticEgressUniDirTunnelName = _CienaCesGmplsStaticEgressUniDirTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 5, 1, 2),
    _CienaCesGmplsStaticEgressUniDirTunnelName_Type()
)
cienaCesGmplsStaticEgressUniDirTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressUniDirTunnelName.setStatus("current")


class _CienaCesGmplsStaticEgressUniDirTunnelAdminState_Type(CienaGlobalState):
    """Custom type cienaCesGmplsStaticEgressUniDirTunnelAdminState based on CienaGlobalState"""


_CienaCesGmplsStaticEgressUniDirTunnelAdminState_Object = MibTableColumn
cienaCesGmplsStaticEgressUniDirTunnelAdminState = _CienaCesGmplsStaticEgressUniDirTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 5, 1, 3),
    _CienaCesGmplsStaticEgressUniDirTunnelAdminState_Type()
)
cienaCesGmplsStaticEgressUniDirTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressUniDirTunnelAdminState.setStatus("current")
_CienaCesGmplsStaticEgressUniDirTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsStaticEgressUniDirTunnelOperState_Object = MibTableColumn
cienaCesGmplsStaticEgressUniDirTunnelOperState = _CienaCesGmplsStaticEgressUniDirTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 5, 1, 4),
    _CienaCesGmplsStaticEgressUniDirTunnelOperState_Type()
)
cienaCesGmplsStaticEgressUniDirTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressUniDirTunnelOperState.setStatus("current")
_CienaCesGmplsStaticEgressUniDirTunnelPrevHopIpAddr_Type = IpAddress
_CienaCesGmplsStaticEgressUniDirTunnelPrevHopIpAddr_Object = MibTableColumn
cienaCesGmplsStaticEgressUniDirTunnelPrevHopIpAddr = _CienaCesGmplsStaticEgressUniDirTunnelPrevHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 5, 1, 5),
    _CienaCesGmplsStaticEgressUniDirTunnelPrevHopIpAddr_Type()
)
cienaCesGmplsStaticEgressUniDirTunnelPrevHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressUniDirTunnelPrevHopIpAddr.setStatus("current")
_CienaCesGmplsStaticEgressUniDirTunnelSourceIpAddr_Type = IpAddress
_CienaCesGmplsStaticEgressUniDirTunnelSourceIpAddr_Object = MibTableColumn
cienaCesGmplsStaticEgressUniDirTunnelSourceIpAddr = _CienaCesGmplsStaticEgressUniDirTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 5, 1, 6),
    _CienaCesGmplsStaticEgressUniDirTunnelSourceIpAddr_Type()
)
cienaCesGmplsStaticEgressUniDirTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressUniDirTunnelSourceIpAddr.setStatus("current")
_CienaCesGmplsStaticEgressUniDirTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsStaticEgressUniDirTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsStaticEgressUniDirTunnelDestIpAddr = _CienaCesGmplsStaticEgressUniDirTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 5, 1, 7),
    _CienaCesGmplsStaticEgressUniDirTunnelDestIpAddr_Type()
)
cienaCesGmplsStaticEgressUniDirTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressUniDirTunnelDestIpAddr.setStatus("current")


class _CienaCesGmplsStaticEgressUniDirTunnelForwardInLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticEgressUniDirTunnelForwardInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsStaticEgressUniDirTunnelForwardInLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticEgressUniDirTunnelForwardInLabel_Object = MibTableColumn
cienaCesGmplsStaticEgressUniDirTunnelForwardInLabel = _CienaCesGmplsStaticEgressUniDirTunnelForwardInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 5, 1, 8),
    _CienaCesGmplsStaticEgressUniDirTunnelForwardInLabel_Type()
)
cienaCesGmplsStaticEgressUniDirTunnelForwardInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressUniDirTunnelForwardInLabel.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelTable_Object = MibTable
cienaCesGmplsStaticEgressCoroutedTunnelTable = _CienaCesGmplsStaticEgressCoroutedTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelTable.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelEntry_Object = MibTableRow
cienaCesGmplsStaticEgressCoroutedTunnelEntry = _CienaCesGmplsStaticEgressCoroutedTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1)
)
cienaCesGmplsStaticEgressCoroutedTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsStaticEgressCoroutedTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelEntry.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelIndex_Type = Unsigned32
_CienaCesGmplsStaticEgressCoroutedTunnelIndex_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelIndex = _CienaCesGmplsStaticEgressCoroutedTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 1),
    _CienaCesGmplsStaticEgressCoroutedTunnelIndex_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelIndex.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelName_Type(DisplayString):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesGmplsStaticEgressCoroutedTunnelName_Type.__name__ = "DisplayString"
_CienaCesGmplsStaticEgressCoroutedTunnelName_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelName = _CienaCesGmplsStaticEgressCoroutedTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 2),
    _CienaCesGmplsStaticEgressCoroutedTunnelName_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelName.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelAdminState_Type(CienaGlobalState):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelAdminState based on CienaGlobalState"""


_CienaCesGmplsStaticEgressCoroutedTunnelAdminState_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelAdminState = _CienaCesGmplsStaticEgressCoroutedTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 3),
    _CienaCesGmplsStaticEgressCoroutedTunnelAdminState_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelAdminState.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsStaticEgressCoroutedTunnelOperState_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelOperState = _CienaCesGmplsStaticEgressCoroutedTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 4),
    _CienaCesGmplsStaticEgressCoroutedTunnelOperState_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelOperState.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelPrevHopIpAddr_Type = IpAddress
_CienaCesGmplsStaticEgressCoroutedTunnelPrevHopIpAddr_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelPrevHopIpAddr = _CienaCesGmplsStaticEgressCoroutedTunnelPrevHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 5),
    _CienaCesGmplsStaticEgressCoroutedTunnelPrevHopIpAddr_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelPrevHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelPrevHopIpAddr.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelSourceIpAddr_Type = IpAddress
_CienaCesGmplsStaticEgressCoroutedTunnelSourceIpAddr_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelSourceIpAddr = _CienaCesGmplsStaticEgressCoroutedTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 6),
    _CienaCesGmplsStaticEgressCoroutedTunnelSourceIpAddr_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelSourceIpAddr.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsStaticEgressCoroutedTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelDestIpAddr = _CienaCesGmplsStaticEgressCoroutedTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 7),
    _CienaCesGmplsStaticEgressCoroutedTunnelDestIpAddr_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelDestIpAddr.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelForwardInLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelForwardInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsStaticEgressCoroutedTunnelForwardInLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticEgressCoroutedTunnelForwardInLabel_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelForwardInLabel = _CienaCesGmplsStaticEgressCoroutedTunnelForwardInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 8),
    _CienaCesGmplsStaticEgressCoroutedTunnelForwardInLabel_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelForwardInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelForwardInLabel.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelReverseOutLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelReverseOutLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsStaticEgressCoroutedTunnelReverseOutLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticEgressCoroutedTunnelReverseOutLabel_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelReverseOutLabel = _CienaCesGmplsStaticEgressCoroutedTunnelReverseOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 9),
    _CienaCesGmplsStaticEgressCoroutedTunnelReverseOutLabel_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelReverseOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelReverseOutLabel.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelProtectionRole_Type(Integer32):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelProtectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 0),
          ("primary", 1))
    )


_CienaCesGmplsStaticEgressCoroutedTunnelProtectionRole_Type.__name__ = "Integer32"
_CienaCesGmplsStaticEgressCoroutedTunnelProtectionRole_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelProtectionRole = _CienaCesGmplsStaticEgressCoroutedTunnelProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 10),
    _CienaCesGmplsStaticEgressCoroutedTunnelProtectionRole_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelProtectionRole.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelProtectionPartnerName_Type = DisplayString
_CienaCesGmplsStaticEgressCoroutedTunnelProtectionPartnerName_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelProtectionPartnerName = _CienaCesGmplsStaticEgressCoroutedTunnelProtectionPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 11),
    _CienaCesGmplsStaticEgressCoroutedTunnelProtectionPartnerName_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelProtectionPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelProtectionPartnerName.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelProtectionState_Type(Integer32):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 0))
    )


_CienaCesGmplsStaticEgressCoroutedTunnelProtectionState_Type.__name__ = "Integer32"
_CienaCesGmplsStaticEgressCoroutedTunnelProtectionState_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelProtectionState = _CienaCesGmplsStaticEgressCoroutedTunnelProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 12),
    _CienaCesGmplsStaticEgressCoroutedTunnelProtectionState_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelProtectionState.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelGrpIndex_Type = Unsigned32
_CienaCesGmplsStaticEgressCoroutedTunnelGrpIndex_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelGrpIndex = _CienaCesGmplsStaticEgressCoroutedTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 13),
    _CienaCesGmplsStaticEgressCoroutedTunnelGrpIndex_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelGrpIndex.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelReversion_Type(Integer32):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelReversion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesGmplsStaticEgressCoroutedTunnelReversion_Type.__name__ = "Integer32"
_CienaCesGmplsStaticEgressCoroutedTunnelReversion_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelReversion = _CienaCesGmplsStaticEgressCoroutedTunnelReversion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 14),
    _CienaCesGmplsStaticEgressCoroutedTunnelReversion_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelReversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelReversion.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelReversionTimeout_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelReversionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsStaticEgressCoroutedTunnelReversionTimeout_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticEgressCoroutedTunnelReversionTimeout_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelReversionTimeout = _CienaCesGmplsStaticEgressCoroutedTunnelReversionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 15),
    _CienaCesGmplsStaticEgressCoroutedTunnelReversionTimeout_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelReversionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelReversionTimeout.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelCosProfileIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelCosProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsStaticEgressCoroutedTunnelCosProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticEgressCoroutedTunnelCosProfileIndex_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelCosProfileIndex = _CienaCesGmplsStaticEgressCoroutedTunnelCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 16),
    _CienaCesGmplsStaticEgressCoroutedTunnelCosProfileIndex_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelCosProfileIndex.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelCosProfileName_Type = DisplayString
_CienaCesGmplsStaticEgressCoroutedTunnelCosProfileName_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelCosProfileName = _CienaCesGmplsStaticEgressCoroutedTunnelCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 17),
    _CienaCesGmplsStaticEgressCoroutedTunnelCosProfileName_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelCosProfileName.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelBfdMonitoring_Type = CienaGlobalState
_CienaCesGmplsStaticEgressCoroutedTunnelBfdMonitoring_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelBfdMonitoring = _CienaCesGmplsStaticEgressCoroutedTunnelBfdMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 18),
    _CienaCesGmplsStaticEgressCoroutedTunnelBfdMonitoring_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelBfdMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelBfdMonitoring.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelBfdProfileName_Type = DisplayString
_CienaCesGmplsStaticEgressCoroutedTunnelBfdProfileName_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelBfdProfileName = _CienaCesGmplsStaticEgressCoroutedTunnelBfdProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 19),
    _CienaCesGmplsStaticEgressCoroutedTunnelBfdProfileName_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelBfdProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelBfdProfileName.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelBfdSessionName_Type = DisplayString
_CienaCesGmplsStaticEgressCoroutedTunnelBfdSessionName_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelBfdSessionName = _CienaCesGmplsStaticEgressCoroutedTunnelBfdSessionName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 20),
    _CienaCesGmplsStaticEgressCoroutedTunnelBfdSessionName_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelBfdSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelBfdSessionName.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelAisMonitoring_Type = CienaGlobalState
_CienaCesGmplsStaticEgressCoroutedTunnelAisMonitoring_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelAisMonitoring = _CienaCesGmplsStaticEgressCoroutedTunnelAisMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 21),
    _CienaCesGmplsStaticEgressCoroutedTunnelAisMonitoring_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelAisMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelAisMonitoring.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelAisProfileName_Type = DisplayString
_CienaCesGmplsStaticEgressCoroutedTunnelAisProfileName_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelAisProfileName = _CienaCesGmplsStaticEgressCoroutedTunnelAisProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 22),
    _CienaCesGmplsStaticEgressCoroutedTunnelAisProfileName_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelAisProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelAisProfileName.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelBfdSessionFaulted_Type = Integer32
_CienaCesGmplsStaticEgressCoroutedTunnelBfdSessionFaulted_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelBfdSessionFaulted = _CienaCesGmplsStaticEgressCoroutedTunnelBfdSessionFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 23),
    _CienaCesGmplsStaticEgressCoroutedTunnelBfdSessionFaulted_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelBfdSessionFaulted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelBfdSessionFaulted.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelBfdProfileIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelBfdProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsStaticEgressCoroutedTunnelBfdProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticEgressCoroutedTunnelBfdProfileIndex_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelBfdProfileIndex = _CienaCesGmplsStaticEgressCoroutedTunnelBfdProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 24),
    _CienaCesGmplsStaticEgressCoroutedTunnelBfdProfileIndex_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelBfdProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelBfdProfileIndex.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelRecoveryDisjoint_Type(Integer32):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelRecoveryDisjoint based on Integer32"""
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
        *(("link", 2),
          ("node", 3),
          ("none", 1),
          ("srlg", 4),
          ("unknown", 5))
    )


_CienaCesGmplsStaticEgressCoroutedTunnelRecoveryDisjoint_Type.__name__ = "Integer32"
_CienaCesGmplsStaticEgressCoroutedTunnelRecoveryDisjoint_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelRecoveryDisjoint = _CienaCesGmplsStaticEgressCoroutedTunnelRecoveryDisjoint_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 25),
    _CienaCesGmplsStaticEgressCoroutedTunnelRecoveryDisjoint_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelRecoveryDisjoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelRecoveryDisjoint.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelTTLPolicy_Type(TTLPolicy):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelTTLPolicy based on TTLPolicy"""


_CienaCesGmplsStaticEgressCoroutedTunnelTTLPolicy_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelTTLPolicy = _CienaCesGmplsStaticEgressCoroutedTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 26),
    _CienaCesGmplsStaticEgressCoroutedTunnelTTLPolicy_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelTTLPolicy.setStatus("current")


class _CienaCesGmplsStaticEgressCoroutedTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticEgressCoroutedTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesGmplsStaticEgressCoroutedTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticEgressCoroutedTunnelFixedTTL_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelFixedTTL = _CienaCesGmplsStaticEgressCoroutedTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 27),
    _CienaCesGmplsStaticEgressCoroutedTunnelFixedTTL_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelFixedTTL.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelPrevHopIfNum_Type = Unsigned32
_CienaCesGmplsStaticEgressCoroutedTunnelPrevHopIfNum_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelPrevHopIfNum = _CienaCesGmplsStaticEgressCoroutedTunnelPrevHopIfNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 28),
    _CienaCesGmplsStaticEgressCoroutedTunnelPrevHopIfNum_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelPrevHopIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelPrevHopIfNum.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelLspId_Type = Unsigned32
_CienaCesGmplsStaticEgressCoroutedTunnelLspId_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelLspId = _CienaCesGmplsStaticEgressCoroutedTunnelLspId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 29),
    _CienaCesGmplsStaticEgressCoroutedTunnelLspId_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelLspId.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelSrcTunnelId_Type = Unsigned32
_CienaCesGmplsStaticEgressCoroutedTunnelSrcTunnelId_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelSrcTunnelId = _CienaCesGmplsStaticEgressCoroutedTunnelSrcTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 30),
    _CienaCesGmplsStaticEgressCoroutedTunnelSrcTunnelId_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelSrcTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelSrcTunnelId.setStatus("current")
_CienaCesGmplsStaticEgressCoroutedTunnelDestTunnelId_Type = Unsigned32
_CienaCesGmplsStaticEgressCoroutedTunnelDestTunnelId_Object = MibTableColumn
cienaCesGmplsStaticEgressCoroutedTunnelDestTunnelId = _CienaCesGmplsStaticEgressCoroutedTunnelDestTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 6, 1, 31),
    _CienaCesGmplsStaticEgressCoroutedTunnelDestTunnelId_Type()
)
cienaCesGmplsStaticEgressCoroutedTunnelDestTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticEgressCoroutedTunnelDestTunnelId.setStatus("current")
_CienaCesGmplsDynamicEgressUniDirTunnelTable_Object = MibTable
cienaCesGmplsDynamicEgressUniDirTunnelTable = _CienaCesGmplsDynamicEgressUniDirTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressUniDirTunnelTable.setStatus("current")
_CienaCesGmplsDynamicEgressUniDirTunnelEntry_Object = MibTableRow
cienaCesGmplsDynamicEgressUniDirTunnelEntry = _CienaCesGmplsDynamicEgressUniDirTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 7, 1)
)
cienaCesGmplsDynamicEgressUniDirTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsDynamicEgressUniDirTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressUniDirTunnelEntry.setStatus("current")
_CienaCesGmplsDynamicEgressUniDirTunnelIndex_Type = Unsigned32
_CienaCesGmplsDynamicEgressUniDirTunnelIndex_Object = MibTableColumn
cienaCesGmplsDynamicEgressUniDirTunnelIndex = _CienaCesGmplsDynamicEgressUniDirTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 7, 1, 1),
    _CienaCesGmplsDynamicEgressUniDirTunnelIndex_Type()
)
cienaCesGmplsDynamicEgressUniDirTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressUniDirTunnelIndex.setStatus("current")


class _CienaCesGmplsDynamicEgressUniDirTunnelName_Type(DisplayString):
    """Custom type cienaCesGmplsDynamicEgressUniDirTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesGmplsDynamicEgressUniDirTunnelName_Type.__name__ = "DisplayString"
_CienaCesGmplsDynamicEgressUniDirTunnelName_Object = MibTableColumn
cienaCesGmplsDynamicEgressUniDirTunnelName = _CienaCesGmplsDynamicEgressUniDirTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 7, 1, 2),
    _CienaCesGmplsDynamicEgressUniDirTunnelName_Type()
)
cienaCesGmplsDynamicEgressUniDirTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressUniDirTunnelName.setStatus("current")


class _CienaCesGmplsDynamicEgressUniDirTunnelAdminState_Type(CienaGlobalState):
    """Custom type cienaCesGmplsDynamicEgressUniDirTunnelAdminState based on CienaGlobalState"""


_CienaCesGmplsDynamicEgressUniDirTunnelAdminState_Object = MibTableColumn
cienaCesGmplsDynamicEgressUniDirTunnelAdminState = _CienaCesGmplsDynamicEgressUniDirTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 7, 1, 3),
    _CienaCesGmplsDynamicEgressUniDirTunnelAdminState_Type()
)
cienaCesGmplsDynamicEgressUniDirTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressUniDirTunnelAdminState.setStatus("current")
_CienaCesGmplsDynamicEgressUniDirTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsDynamicEgressUniDirTunnelOperState_Object = MibTableColumn
cienaCesGmplsDynamicEgressUniDirTunnelOperState = _CienaCesGmplsDynamicEgressUniDirTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 7, 1, 4),
    _CienaCesGmplsDynamicEgressUniDirTunnelOperState_Type()
)
cienaCesGmplsDynamicEgressUniDirTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressUniDirTunnelOperState.setStatus("current")
_CienaCesGmplsDynamicEgressUniDirLspId_Type = Unsigned32
_CienaCesGmplsDynamicEgressUniDirLspId_Object = MibTableColumn
cienaCesGmplsDynamicEgressUniDirLspId = _CienaCesGmplsDynamicEgressUniDirLspId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 7, 1, 5),
    _CienaCesGmplsDynamicEgressUniDirLspId_Type()
)
cienaCesGmplsDynamicEgressUniDirLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressUniDirLspId.setStatus("current")
_CienaCesGmplsDynamicEgressUniDirTunnelPrevHopIpAddr_Type = IpAddress
_CienaCesGmplsDynamicEgressUniDirTunnelPrevHopIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicEgressUniDirTunnelPrevHopIpAddr = _CienaCesGmplsDynamicEgressUniDirTunnelPrevHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 7, 1, 6),
    _CienaCesGmplsDynamicEgressUniDirTunnelPrevHopIpAddr_Type()
)
cienaCesGmplsDynamicEgressUniDirTunnelPrevHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressUniDirTunnelPrevHopIpAddr.setStatus("current")
_CienaCesGmplsDynamicEgressUniDirTunnelSourceIpAddr_Type = IpAddress
_CienaCesGmplsDynamicEgressUniDirTunnelSourceIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicEgressUniDirTunnelSourceIpAddr = _CienaCesGmplsDynamicEgressUniDirTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 7, 1, 7),
    _CienaCesGmplsDynamicEgressUniDirTunnelSourceIpAddr_Type()
)
cienaCesGmplsDynamicEgressUniDirTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressUniDirTunnelSourceIpAddr.setStatus("current")
_CienaCesGmplsDynamicEgressUniDirTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsDynamicEgressUniDirTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicEgressUniDirTunnelDestIpAddr = _CienaCesGmplsDynamicEgressUniDirTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 7, 1, 8),
    _CienaCesGmplsDynamicEgressUniDirTunnelDestIpAddr_Type()
)
cienaCesGmplsDynamicEgressUniDirTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressUniDirTunnelDestIpAddr.setStatus("current")
_CienaCesGmplsDynamicEgressUniDirTunnelForwardInLabel_Type = Unsigned32
_CienaCesGmplsDynamicEgressUniDirTunnelForwardInLabel_Object = MibTableColumn
cienaCesGmplsDynamicEgressUniDirTunnelForwardInLabel = _CienaCesGmplsDynamicEgressUniDirTunnelForwardInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 7, 1, 9),
    _CienaCesGmplsDynamicEgressUniDirTunnelForwardInLabel_Type()
)
cienaCesGmplsDynamicEgressUniDirTunnelForwardInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressUniDirTunnelForwardInLabel.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelTable_Object = MibTable
cienaCesGmplsDynamicEgressCoroutedTunnelTable = _CienaCesGmplsDynamicEgressCoroutedTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelTable.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelEntry_Object = MibTableRow
cienaCesGmplsDynamicEgressCoroutedTunnelEntry = _CienaCesGmplsDynamicEgressCoroutedTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1)
)
cienaCesGmplsDynamicEgressCoroutedTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsDynamicEgressCoroutedTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelEntry.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelIndex_Type = Unsigned32
_CienaCesGmplsDynamicEgressCoroutedTunnelIndex_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelIndex = _CienaCesGmplsDynamicEgressCoroutedTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 1),
    _CienaCesGmplsDynamicEgressCoroutedTunnelIndex_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelIndex.setStatus("current")


class _CienaCesGmplsDynamicEgressCoroutedTunnelName_Type(DisplayString):
    """Custom type cienaCesGmplsDynamicEgressCoroutedTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesGmplsDynamicEgressCoroutedTunnelName_Type.__name__ = "DisplayString"
_CienaCesGmplsDynamicEgressCoroutedTunnelName_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelName = _CienaCesGmplsDynamicEgressCoroutedTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 2),
    _CienaCesGmplsDynamicEgressCoroutedTunnelName_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelName.setStatus("current")


class _CienaCesGmplsDynamicEgressCoroutedTunnelAdminState_Type(CienaGlobalState):
    """Custom type cienaCesGmplsDynamicEgressCoroutedTunnelAdminState based on CienaGlobalState"""


_CienaCesGmplsDynamicEgressCoroutedTunnelAdminState_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelAdminState = _CienaCesGmplsDynamicEgressCoroutedTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 3),
    _CienaCesGmplsDynamicEgressCoroutedTunnelAdminState_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelAdminState.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsDynamicEgressCoroutedTunnelOperState_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelOperState = _CienaCesGmplsDynamicEgressCoroutedTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 4),
    _CienaCesGmplsDynamicEgressCoroutedTunnelOperState_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelOperState.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedLspId_Type = Unsigned32
_CienaCesGmplsDynamicEgressCoroutedLspId_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedLspId = _CienaCesGmplsDynamicEgressCoroutedLspId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 5),
    _CienaCesGmplsDynamicEgressCoroutedLspId_Type()
)
cienaCesGmplsDynamicEgressCoroutedLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedLspId.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelPrevHopIpAddr_Type = IpAddress
_CienaCesGmplsDynamicEgressCoroutedTunnelPrevHopIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelPrevHopIpAddr = _CienaCesGmplsDynamicEgressCoroutedTunnelPrevHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 6),
    _CienaCesGmplsDynamicEgressCoroutedTunnelPrevHopIpAddr_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelPrevHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelPrevHopIpAddr.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelSourceIpAddr_Type = IpAddress
_CienaCesGmplsDynamicEgressCoroutedTunnelSourceIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelSourceIpAddr = _CienaCesGmplsDynamicEgressCoroutedTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 7),
    _CienaCesGmplsDynamicEgressCoroutedTunnelSourceIpAddr_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelSourceIpAddr.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsDynamicEgressCoroutedTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelDestIpAddr = _CienaCesGmplsDynamicEgressCoroutedTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 8),
    _CienaCesGmplsDynamicEgressCoroutedTunnelDestIpAddr_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelDestIpAddr.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelForwardInLabel_Type = Unsigned32
_CienaCesGmplsDynamicEgressCoroutedTunnelForwardInLabel_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelForwardInLabel = _CienaCesGmplsDynamicEgressCoroutedTunnelForwardInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 9),
    _CienaCesGmplsDynamicEgressCoroutedTunnelForwardInLabel_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelForwardInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelForwardInLabel.setStatus("current")


class _CienaCesGmplsDynamicEgressCoroutedTunnelReverseOutLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicEgressCoroutedTunnelReverseOutLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsDynamicEgressCoroutedTunnelReverseOutLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicEgressCoroutedTunnelReverseOutLabel_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelReverseOutLabel = _CienaCesGmplsDynamicEgressCoroutedTunnelReverseOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 10),
    _CienaCesGmplsDynamicEgressCoroutedTunnelReverseOutLabel_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelReverseOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelReverseOutLabel.setStatus("current")


class _CienaCesGmplsDynamicEgressCoroutedTunnelProtectionRole_Type(Integer32):
    """Custom type cienaCesGmplsDynamicEgressCoroutedTunnelProtectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 0),
          ("primary", 1))
    )


_CienaCesGmplsDynamicEgressCoroutedTunnelProtectionRole_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicEgressCoroutedTunnelProtectionRole_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelProtectionRole = _CienaCesGmplsDynamicEgressCoroutedTunnelProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 11),
    _CienaCesGmplsDynamicEgressCoroutedTunnelProtectionRole_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelProtectionRole.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelProtectionPartnerName_Type = DisplayString
_CienaCesGmplsDynamicEgressCoroutedTunnelProtectionPartnerName_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelProtectionPartnerName = _CienaCesGmplsDynamicEgressCoroutedTunnelProtectionPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 12),
    _CienaCesGmplsDynamicEgressCoroutedTunnelProtectionPartnerName_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelProtectionPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelProtectionPartnerName.setStatus("current")


class _CienaCesGmplsDynamicEgressCoroutedTunnelProtectionState_Type(Integer32):
    """Custom type cienaCesGmplsDynamicEgressCoroutedTunnelProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 0))
    )


_CienaCesGmplsDynamicEgressCoroutedTunnelProtectionState_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicEgressCoroutedTunnelProtectionState_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelProtectionState = _CienaCesGmplsDynamicEgressCoroutedTunnelProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 13),
    _CienaCesGmplsDynamicEgressCoroutedTunnelProtectionState_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelProtectionState.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelGrpIndex_Type = Unsigned32
_CienaCesGmplsDynamicEgressCoroutedTunnelGrpIndex_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelGrpIndex = _CienaCesGmplsDynamicEgressCoroutedTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 14),
    _CienaCesGmplsDynamicEgressCoroutedTunnelGrpIndex_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelGrpIndex.setStatus("current")


class _CienaCesGmplsDynamicEgressCoroutedTunnelReversion_Type(Integer32):
    """Custom type cienaCesGmplsDynamicEgressCoroutedTunnelReversion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesGmplsDynamicEgressCoroutedTunnelReversion_Type.__name__ = "Integer32"
_CienaCesGmplsDynamicEgressCoroutedTunnelReversion_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelReversion = _CienaCesGmplsDynamicEgressCoroutedTunnelReversion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 15),
    _CienaCesGmplsDynamicEgressCoroutedTunnelReversion_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelReversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelReversion.setStatus("current")


class _CienaCesGmplsDynamicEgressCoroutedTunnelReversionTimeout_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicEgressCoroutedTunnelReversionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsDynamicEgressCoroutedTunnelReversionTimeout_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicEgressCoroutedTunnelReversionTimeout_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelReversionTimeout = _CienaCesGmplsDynamicEgressCoroutedTunnelReversionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 16),
    _CienaCesGmplsDynamicEgressCoroutedTunnelReversionTimeout_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelReversionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelReversionTimeout.setStatus("current")


class _CienaCesGmplsDynamicEgressCoroutedTunnelCosProfileIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicEgressCoroutedTunnelCosProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsDynamicEgressCoroutedTunnelCosProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicEgressCoroutedTunnelCosProfileIndex_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelCosProfileIndex = _CienaCesGmplsDynamicEgressCoroutedTunnelCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 17),
    _CienaCesGmplsDynamicEgressCoroutedTunnelCosProfileIndex_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelCosProfileIndex.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelCosProfileName_Type = DisplayString
_CienaCesGmplsDynamicEgressCoroutedTunnelCosProfileName_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelCosProfileName = _CienaCesGmplsDynamicEgressCoroutedTunnelCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 18),
    _CienaCesGmplsDynamicEgressCoroutedTunnelCosProfileName_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelCosProfileName.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelBfdMonitoring_Type = CienaGlobalState
_CienaCesGmplsDynamicEgressCoroutedTunnelBfdMonitoring_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelBfdMonitoring = _CienaCesGmplsDynamicEgressCoroutedTunnelBfdMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 19),
    _CienaCesGmplsDynamicEgressCoroutedTunnelBfdMonitoring_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelBfdMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelBfdMonitoring.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileName_Type = DisplayString
_CienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileName_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileName = _CienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 20),
    _CienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileName_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileName.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionName_Type = DisplayString
_CienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionName_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionName = _CienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 21),
    _CienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionName_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionName.setStatus("current")
_CienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionFaulted_Type = Integer32
_CienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionFaulted_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionFaulted = _CienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 22),
    _CienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionFaulted_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionFaulted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionFaulted.setStatus("current")


class _CienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileIndex_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileIndex = _CienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 23),
    _CienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileIndex_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileIndex.setStatus("current")


class _CienaCesGmplsDynamicEgressCoroutedTunnelTTLPolicy_Type(TTLPolicy):
    """Custom type cienaCesGmplsDynamicEgressCoroutedTunnelTTLPolicy based on TTLPolicy"""


_CienaCesGmplsDynamicEgressCoroutedTunnelTTLPolicy_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelTTLPolicy = _CienaCesGmplsDynamicEgressCoroutedTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 24),
    _CienaCesGmplsDynamicEgressCoroutedTunnelTTLPolicy_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelTTLPolicy.setStatus("current")


class _CienaCesGmplsDynamicEgressCoroutedTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicEgressCoroutedTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesGmplsDynamicEgressCoroutedTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicEgressCoroutedTunnelFixedTTL_Object = MibTableColumn
cienaCesGmplsDynamicEgressCoroutedTunnelFixedTTL = _CienaCesGmplsDynamicEgressCoroutedTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 8, 1, 25),
    _CienaCesGmplsDynamicEgressCoroutedTunnelFixedTTL_Type()
)
cienaCesGmplsDynamicEgressCoroutedTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicEgressCoroutedTunnelFixedTTL.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelTable_Object = MibTable
cienaCesGmplsStaticTransitUniDirTunnelTable = _CienaCesGmplsStaticTransitUniDirTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelTable.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelEntry_Object = MibTableRow
cienaCesGmplsStaticTransitUniDirTunnelEntry = _CienaCesGmplsStaticTransitUniDirTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1)
)
cienaCesGmplsStaticTransitUniDirTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsStaticTransitUniDirTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelEntry.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelIndex_Type = Unsigned32
_CienaCesGmplsStaticTransitUniDirTunnelIndex_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelIndex = _CienaCesGmplsStaticTransitUniDirTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 1),
    _CienaCesGmplsStaticTransitUniDirTunnelIndex_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelIndex.setStatus("current")


class _CienaCesGmplsStaticTransitUniDirTunnelName_Type(DisplayString):
    """Custom type cienaCesGmplsStaticTransitUniDirTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesGmplsStaticTransitUniDirTunnelName_Type.__name__ = "DisplayString"
_CienaCesGmplsStaticTransitUniDirTunnelName_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelName = _CienaCesGmplsStaticTransitUniDirTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 2),
    _CienaCesGmplsStaticTransitUniDirTunnelName_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelName.setStatus("current")


class _CienaCesGmplsStaticTransitUniDirTunnelAdminState_Type(CienaGlobalState):
    """Custom type cienaCesGmplsStaticTransitUniDirTunnelAdminState based on CienaGlobalState"""


_CienaCesGmplsStaticTransitUniDirTunnelAdminState_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelAdminState = _CienaCesGmplsStaticTransitUniDirTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 3),
    _CienaCesGmplsStaticTransitUniDirTunnelAdminState_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelAdminState.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsStaticTransitUniDirTunnelOperState_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelOperState = _CienaCesGmplsStaticTransitUniDirTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 4),
    _CienaCesGmplsStaticTransitUniDirTunnelOperState_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelOperState.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelSourceIpAddr_Type = IpAddress
_CienaCesGmplsStaticTransitUniDirTunnelSourceIpAddr_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelSourceIpAddr = _CienaCesGmplsStaticTransitUniDirTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 5),
    _CienaCesGmplsStaticTransitUniDirTunnelSourceIpAddr_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelSourceIpAddr.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsStaticTransitUniDirTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelDestIpAddr = _CienaCesGmplsStaticTransitUniDirTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 6),
    _CienaCesGmplsStaticTransitUniDirTunnelDestIpAddr_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelDestIpAddr.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelNextHopIpAddr_Type = IpAddress
_CienaCesGmplsStaticTransitUniDirTunnelNextHopIpAddr_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelNextHopIpAddr = _CienaCesGmplsStaticTransitUniDirTunnelNextHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 7),
    _CienaCesGmplsStaticTransitUniDirTunnelNextHopIpAddr_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelNextHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelNextHopIpAddr.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelPrevHopIpAddr_Type = IpAddress
_CienaCesGmplsStaticTransitUniDirTunnelPrevHopIpAddr_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelPrevHopIpAddr = _CienaCesGmplsStaticTransitUniDirTunnelPrevHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 8),
    _CienaCesGmplsStaticTransitUniDirTunnelPrevHopIpAddr_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelPrevHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelPrevHopIpAddr.setStatus("current")


class _CienaCesGmplsStaticTransitUniDirTunnelForwardInLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticTransitUniDirTunnelForwardInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsStaticTransitUniDirTunnelForwardInLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticTransitUniDirTunnelForwardInLabel_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelForwardInLabel = _CienaCesGmplsStaticTransitUniDirTunnelForwardInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 9),
    _CienaCesGmplsStaticTransitUniDirTunnelForwardInLabel_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelForwardInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelForwardInLabel.setStatus("current")


class _CienaCesGmplsStaticTransitUniDirTunnelForwardOutLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticTransitUniDirTunnelForwardOutLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsStaticTransitUniDirTunnelForwardOutLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticTransitUniDirTunnelForwardOutLabel_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelForwardOutLabel = _CienaCesGmplsStaticTransitUniDirTunnelForwardOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 10),
    _CienaCesGmplsStaticTransitUniDirTunnelForwardOutLabel_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelForwardOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelForwardOutLabel.setStatus("current")


class _CienaCesGmplsStaticTransitUniDirTunnelTTLPolicy_Type(TTLPolicy):
    """Custom type cienaCesGmplsStaticTransitUniDirTunnelTTLPolicy based on TTLPolicy"""


_CienaCesGmplsStaticTransitUniDirTunnelTTLPolicy_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelTTLPolicy = _CienaCesGmplsStaticTransitUniDirTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 11),
    _CienaCesGmplsStaticTransitUniDirTunnelTTLPolicy_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelTTLPolicy.setStatus("current")


class _CienaCesGmplsStaticTransitUniDirTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticTransitUniDirTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesGmplsStaticTransitUniDirTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticTransitUniDirTunnelFixedTTL_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelFixedTTL = _CienaCesGmplsStaticTransitUniDirTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 12),
    _CienaCesGmplsStaticTransitUniDirTunnelFixedTTL_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelFixedTTL.setStatus("current")


class _CienaCesGmplsStaticTransitUniDirTunnelCosProfileIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticTransitUniDirTunnelCosProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsStaticTransitUniDirTunnelCosProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticTransitUniDirTunnelCosProfileIndex_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelCosProfileIndex = _CienaCesGmplsStaticTransitUniDirTunnelCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 13),
    _CienaCesGmplsStaticTransitUniDirTunnelCosProfileIndex_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelCosProfileIndex.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelCosProfileName_Type = DisplayString
_CienaCesGmplsStaticTransitUniDirTunnelCosProfileName_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelCosProfileName = _CienaCesGmplsStaticTransitUniDirTunnelCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 14),
    _CienaCesGmplsStaticTransitUniDirTunnelCosProfileName_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelCosProfileName.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelAisMonitoring_Type = CienaGlobalState
_CienaCesGmplsStaticTransitUniDirTunnelAisMonitoring_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelAisMonitoring = _CienaCesGmplsStaticTransitUniDirTunnelAisMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 15),
    _CienaCesGmplsStaticTransitUniDirTunnelAisMonitoring_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelAisMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelAisMonitoring.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelAisProfileName_Type = DisplayString
_CienaCesGmplsStaticTransitUniDirTunnelAisProfileName_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelAisProfileName = _CienaCesGmplsStaticTransitUniDirTunnelAisProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 16),
    _CienaCesGmplsStaticTransitUniDirTunnelAisProfileName_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelAisProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelAisProfileName.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelIncomingPackets_Type = Unsigned32
_CienaCesGmplsStaticTransitUniDirTunnelIncomingPackets_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelIncomingPackets = _CienaCesGmplsStaticTransitUniDirTunnelIncomingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 17),
    _CienaCesGmplsStaticTransitUniDirTunnelIncomingPackets_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelIncomingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelIncomingPackets.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelOutgoingPackets_Type = Unsigned32
_CienaCesGmplsStaticTransitUniDirTunnelOutgoingPackets_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelOutgoingPackets = _CienaCesGmplsStaticTransitUniDirTunnelOutgoingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 18),
    _CienaCesGmplsStaticTransitUniDirTunnelOutgoingPackets_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelOutgoingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelOutgoingPackets.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelIncomingBytes_Type = Unsigned32
_CienaCesGmplsStaticTransitUniDirTunnelIncomingBytes_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelIncomingBytes = _CienaCesGmplsStaticTransitUniDirTunnelIncomingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 19),
    _CienaCesGmplsStaticTransitUniDirTunnelIncomingBytes_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelIncomingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelIncomingBytes.setStatus("current")
_CienaCesGmplsStaticTransitUniDirTunnelOutgoingBytes_Type = Unsigned32
_CienaCesGmplsStaticTransitUniDirTunnelOutgoingBytes_Object = MibTableColumn
cienaCesGmplsStaticTransitUniDirTunnelOutgoingBytes = _CienaCesGmplsStaticTransitUniDirTunnelOutgoingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 9, 1, 20),
    _CienaCesGmplsStaticTransitUniDirTunnelOutgoingBytes_Type()
)
cienaCesGmplsStaticTransitUniDirTunnelOutgoingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitUniDirTunnelOutgoingBytes.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelTable_Object = MibTable
cienaCesGmplsStaticTransitCoroutedTunnelTable = _CienaCesGmplsStaticTransitCoroutedTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelTable.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelEntry_Object = MibTableRow
cienaCesGmplsStaticTransitCoroutedTunnelEntry = _CienaCesGmplsStaticTransitCoroutedTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1)
)
cienaCesGmplsStaticTransitCoroutedTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsStaticTransitCoroutedTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelEntry.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelIndex_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelIndex_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelIndex = _CienaCesGmplsStaticTransitCoroutedTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 1),
    _CienaCesGmplsStaticTransitCoroutedTunnelIndex_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelIndex.setStatus("current")


class _CienaCesGmplsStaticTransitCoroutedTunnelName_Type(DisplayString):
    """Custom type cienaCesGmplsStaticTransitCoroutedTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesGmplsStaticTransitCoroutedTunnelName_Type.__name__ = "DisplayString"
_CienaCesGmplsStaticTransitCoroutedTunnelName_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelName = _CienaCesGmplsStaticTransitCoroutedTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 2),
    _CienaCesGmplsStaticTransitCoroutedTunnelName_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelName.setStatus("current")


class _CienaCesGmplsStaticTransitCoroutedTunnelAdminState_Type(CienaGlobalState):
    """Custom type cienaCesGmplsStaticTransitCoroutedTunnelAdminState based on CienaGlobalState"""


_CienaCesGmplsStaticTransitCoroutedTunnelAdminState_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelAdminState = _CienaCesGmplsStaticTransitCoroutedTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 3),
    _CienaCesGmplsStaticTransitCoroutedTunnelAdminState_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelAdminState.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsStaticTransitCoroutedTunnelOperState_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelOperState = _CienaCesGmplsStaticTransitCoroutedTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 4),
    _CienaCesGmplsStaticTransitCoroutedTunnelOperState_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelOperState.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelSourceIpAddr_Type = IpAddress
_CienaCesGmplsStaticTransitCoroutedTunnelSourceIpAddr_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelSourceIpAddr = _CienaCesGmplsStaticTransitCoroutedTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 5),
    _CienaCesGmplsStaticTransitCoroutedTunnelSourceIpAddr_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelSourceIpAddr.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsStaticTransitCoroutedTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelDestIpAddr = _CienaCesGmplsStaticTransitCoroutedTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 6),
    _CienaCesGmplsStaticTransitCoroutedTunnelDestIpAddr_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelDestIpAddr.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelNextHopIpAddr_Type = IpAddress
_CienaCesGmplsStaticTransitCoroutedTunnelNextHopIpAddr_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelNextHopIpAddr = _CienaCesGmplsStaticTransitCoroutedTunnelNextHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 7),
    _CienaCesGmplsStaticTransitCoroutedTunnelNextHopIpAddr_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelNextHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelNextHopIpAddr.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelPrevHopIpAddr_Type = IpAddress
_CienaCesGmplsStaticTransitCoroutedTunnelPrevHopIpAddr_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelPrevHopIpAddr = _CienaCesGmplsStaticTransitCoroutedTunnelPrevHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 8),
    _CienaCesGmplsStaticTransitCoroutedTunnelPrevHopIpAddr_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelPrevHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelPrevHopIpAddr.setStatus("current")


class _CienaCesGmplsStaticTransitCoroutedTunnelForwardInLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticTransitCoroutedTunnelForwardInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsStaticTransitCoroutedTunnelForwardInLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticTransitCoroutedTunnelForwardInLabel_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelForwardInLabel = _CienaCesGmplsStaticTransitCoroutedTunnelForwardInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 9),
    _CienaCesGmplsStaticTransitCoroutedTunnelForwardInLabel_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelForwardInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelForwardInLabel.setStatus("current")


class _CienaCesGmplsStaticTransitCoroutedTunnelForwardOutLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticTransitCoroutedTunnelForwardOutLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsStaticTransitCoroutedTunnelForwardOutLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticTransitCoroutedTunnelForwardOutLabel_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelForwardOutLabel = _CienaCesGmplsStaticTransitCoroutedTunnelForwardOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 10),
    _CienaCesGmplsStaticTransitCoroutedTunnelForwardOutLabel_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelForwardOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelForwardOutLabel.setStatus("current")


class _CienaCesGmplsStaticTransitCoroutedTunnelReverseInLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticTransitCoroutedTunnelReverseInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsStaticTransitCoroutedTunnelReverseInLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticTransitCoroutedTunnelReverseInLabel_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelReverseInLabel = _CienaCesGmplsStaticTransitCoroutedTunnelReverseInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 11),
    _CienaCesGmplsStaticTransitCoroutedTunnelReverseInLabel_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelReverseInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelReverseInLabel.setStatus("current")


class _CienaCesGmplsStaticTransitCoroutedTunnelReverseOutLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticTransitCoroutedTunnelReverseOutLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsStaticTransitCoroutedTunnelReverseOutLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticTransitCoroutedTunnelReverseOutLabel_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelReverseOutLabel = _CienaCesGmplsStaticTransitCoroutedTunnelReverseOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 12),
    _CienaCesGmplsStaticTransitCoroutedTunnelReverseOutLabel_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelReverseOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelReverseOutLabel.setStatus("current")


class _CienaCesGmplsStaticTransitCoroutedTunnelTTLPolicy_Type(TTLPolicy):
    """Custom type cienaCesGmplsStaticTransitCoroutedTunnelTTLPolicy based on TTLPolicy"""


_CienaCesGmplsStaticTransitCoroutedTunnelTTLPolicy_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelTTLPolicy = _CienaCesGmplsStaticTransitCoroutedTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 13),
    _CienaCesGmplsStaticTransitCoroutedTunnelTTLPolicy_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelTTLPolicy.setStatus("current")


class _CienaCesGmplsStaticTransitCoroutedTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticTransitCoroutedTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesGmplsStaticTransitCoroutedTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticTransitCoroutedTunnelFixedTTL_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelFixedTTL = _CienaCesGmplsStaticTransitCoroutedTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 14),
    _CienaCesGmplsStaticTransitCoroutedTunnelFixedTTL_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelFixedTTL.setStatus("current")


class _CienaCesGmplsStaticTransitCoroutedTunnelCosProfileIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsStaticTransitCoroutedTunnelCosProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsStaticTransitCoroutedTunnelCosProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsStaticTransitCoroutedTunnelCosProfileIndex_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelCosProfileIndex = _CienaCesGmplsStaticTransitCoroutedTunnelCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 15),
    _CienaCesGmplsStaticTransitCoroutedTunnelCosProfileIndex_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelCosProfileIndex.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelCosProfileName_Type = DisplayString
_CienaCesGmplsStaticTransitCoroutedTunnelCosProfileName_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelCosProfileName = _CienaCesGmplsStaticTransitCoroutedTunnelCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 16),
    _CienaCesGmplsStaticTransitCoroutedTunnelCosProfileName_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelCosProfileName.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelAisMonitoring_Type = CienaGlobalState
_CienaCesGmplsStaticTransitCoroutedTunnelAisMonitoring_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelAisMonitoring = _CienaCesGmplsStaticTransitCoroutedTunnelAisMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 17),
    _CienaCesGmplsStaticTransitCoroutedTunnelAisMonitoring_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelAisMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelAisMonitoring.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelAisProfileName_Type = DisplayString
_CienaCesGmplsStaticTransitCoroutedTunnelAisProfileName_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelAisProfileName = _CienaCesGmplsStaticTransitCoroutedTunnelAisProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 18),
    _CienaCesGmplsStaticTransitCoroutedTunnelAisProfileName_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelAisProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelAisProfileName.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelPrevHopIfNum_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelPrevHopIfNum_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelPrevHopIfNum = _CienaCesGmplsStaticTransitCoroutedTunnelPrevHopIfNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 19),
    _CienaCesGmplsStaticTransitCoroutedTunnelPrevHopIfNum_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelPrevHopIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelPrevHopIfNum.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelNextHopIfNum_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelNextHopIfNum_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelNextHopIfNum = _CienaCesGmplsStaticTransitCoroutedTunnelNextHopIfNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 20),
    _CienaCesGmplsStaticTransitCoroutedTunnelNextHopIfNum_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelNextHopIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelNextHopIfNum.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelLspId_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelLspId_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelLspId = _CienaCesGmplsStaticTransitCoroutedTunnelLspId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 21),
    _CienaCesGmplsStaticTransitCoroutedTunnelLspId_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelLspId.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelSrcTunnelId_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelSrcTunnelId_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelSrcTunnelId = _CienaCesGmplsStaticTransitCoroutedTunnelSrcTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 22),
    _CienaCesGmplsStaticTransitCoroutedTunnelSrcTunnelId_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelSrcTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelSrcTunnelId.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelDestTunnelId_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelDestTunnelId_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelDestTunnelId = _CienaCesGmplsStaticTransitCoroutedTunnelDestTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 23),
    _CienaCesGmplsStaticTransitCoroutedTunnelDestTunnelId_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelDestTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelDestTunnelId.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelIncomingPackets_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelIncomingPackets_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelIncomingPackets = _CienaCesGmplsStaticTransitCoroutedTunnelIncomingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 24),
    _CienaCesGmplsStaticTransitCoroutedTunnelIncomingPackets_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelIncomingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelIncomingPackets.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelOutgoingPackets_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelOutgoingPackets_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelOutgoingPackets = _CienaCesGmplsStaticTransitCoroutedTunnelOutgoingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 25),
    _CienaCesGmplsStaticTransitCoroutedTunnelOutgoingPackets_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelOutgoingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelOutgoingPackets.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelIncomingBytes_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelIncomingBytes_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelIncomingBytes = _CienaCesGmplsStaticTransitCoroutedTunnelIncomingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 26),
    _CienaCesGmplsStaticTransitCoroutedTunnelIncomingBytes_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelIncomingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelIncomingBytes.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelOutgoingBytes_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelOutgoingBytes_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelOutgoingBytes = _CienaCesGmplsStaticTransitCoroutedTunnelOutgoingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 27),
    _CienaCesGmplsStaticTransitCoroutedTunnelOutgoingBytes_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelOutgoingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelOutgoingBytes.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingPackets_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingPackets_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingPackets = _CienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 28),
    _CienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingPackets_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingPackets.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingPackets_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingPackets_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingPackets = _CienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 29),
    _CienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingPackets_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingPackets.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingBytes_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingBytes_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingBytes = _CienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 30),
    _CienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingBytes_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingBytes.setStatus("current")
_CienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingBytes_Type = Unsigned32
_CienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingBytes_Object = MibTableColumn
cienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingBytes = _CienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 10, 1, 31),
    _CienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingBytes_Type()
)
cienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingBytes.setStatus("current")
_CienaCesGmplsDynamicTransitUniDirTunnelTable_Object = MibTable
cienaCesGmplsDynamicTransitUniDirTunnelTable = _CienaCesGmplsDynamicTransitUniDirTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelTable.setStatus("current")
_CienaCesGmplsDynamicTransitUniDirTunnelEntry_Object = MibTableRow
cienaCesGmplsDynamicTransitUniDirTunnelEntry = _CienaCesGmplsDynamicTransitUniDirTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1)
)
cienaCesGmplsDynamicTransitUniDirTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsDynamicTransitUniDirTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelEntry.setStatus("current")
_CienaCesGmplsDynamicTransitUniDirTunnelIndex_Type = Unsigned32
_CienaCesGmplsDynamicTransitUniDirTunnelIndex_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelIndex = _CienaCesGmplsDynamicTransitUniDirTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 1),
    _CienaCesGmplsDynamicTransitUniDirTunnelIndex_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelIndex.setStatus("current")


class _CienaCesGmplsDynamicTransitUniDirTunnelName_Type(DisplayString):
    """Custom type cienaCesGmplsDynamicTransitUniDirTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesGmplsDynamicTransitUniDirTunnelName_Type.__name__ = "DisplayString"
_CienaCesGmplsDynamicTransitUniDirTunnelName_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelName = _CienaCesGmplsDynamicTransitUniDirTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 2),
    _CienaCesGmplsDynamicTransitUniDirTunnelName_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelName.setStatus("current")


class _CienaCesGmplsDynamicTransitUniDirTunnelAdminState_Type(CienaGlobalState):
    """Custom type cienaCesGmplsDynamicTransitUniDirTunnelAdminState based on CienaGlobalState"""


_CienaCesGmplsDynamicTransitUniDirTunnelAdminState_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelAdminState = _CienaCesGmplsDynamicTransitUniDirTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 3),
    _CienaCesGmplsDynamicTransitUniDirTunnelAdminState_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelAdminState.setStatus("current")
_CienaCesGmplsDynamicTransitUniDirTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsDynamicTransitUniDirTunnelOperState_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelOperState = _CienaCesGmplsDynamicTransitUniDirTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 4),
    _CienaCesGmplsDynamicTransitUniDirTunnelOperState_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelOperState.setStatus("current")
_CienaCesGmplsDynamicTransitUniDirTunnelSourceIpAddr_Type = IpAddress
_CienaCesGmplsDynamicTransitUniDirTunnelSourceIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelSourceIpAddr = _CienaCesGmplsDynamicTransitUniDirTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 5),
    _CienaCesGmplsDynamicTransitUniDirTunnelSourceIpAddr_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelSourceIpAddr.setStatus("current")
_CienaCesGmplsDynamicTransitUniDirTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsDynamicTransitUniDirTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelDestIpAddr = _CienaCesGmplsDynamicTransitUniDirTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 6),
    _CienaCesGmplsDynamicTransitUniDirTunnelDestIpAddr_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelDestIpAddr.setStatus("current")
_CienaCesGmplsDynamicTransitUniDirTunnelNextHopIpAddr_Type = IpAddress
_CienaCesGmplsDynamicTransitUniDirTunnelNextHopIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelNextHopIpAddr = _CienaCesGmplsDynamicTransitUniDirTunnelNextHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 7),
    _CienaCesGmplsDynamicTransitUniDirTunnelNextHopIpAddr_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelNextHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelNextHopIpAddr.setStatus("current")


class _CienaCesGmplsDynamicTransitUniDirTunnelForwardInLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicTransitUniDirTunnelForwardInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsDynamicTransitUniDirTunnelForwardInLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicTransitUniDirTunnelForwardInLabel_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelForwardInLabel = _CienaCesGmplsDynamicTransitUniDirTunnelForwardInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 8),
    _CienaCesGmplsDynamicTransitUniDirTunnelForwardInLabel_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelForwardInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelForwardInLabel.setStatus("current")


class _CienaCesGmplsDynamicTransitUniDirTunnelForwardOutLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicTransitUniDirTunnelForwardOutLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsDynamicTransitUniDirTunnelForwardOutLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicTransitUniDirTunnelForwardOutLabel_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelForwardOutLabel = _CienaCesGmplsDynamicTransitUniDirTunnelForwardOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 9),
    _CienaCesGmplsDynamicTransitUniDirTunnelForwardOutLabel_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelForwardOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelForwardOutLabel.setStatus("current")


class _CienaCesGmplsDynamicTransitUniDirTunnelTTLPolicy_Type(TTLPolicy):
    """Custom type cienaCesGmplsDynamicTransitUniDirTunnelTTLPolicy based on TTLPolicy"""


_CienaCesGmplsDynamicTransitUniDirTunnelTTLPolicy_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelTTLPolicy = _CienaCesGmplsDynamicTransitUniDirTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 10),
    _CienaCesGmplsDynamicTransitUniDirTunnelTTLPolicy_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelTTLPolicy.setStatus("current")


class _CienaCesGmplsDynamicTransitUniDirTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicTransitUniDirTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesGmplsDynamicTransitUniDirTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicTransitUniDirTunnelFixedTTL_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelFixedTTL = _CienaCesGmplsDynamicTransitUniDirTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 11),
    _CienaCesGmplsDynamicTransitUniDirTunnelFixedTTL_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelFixedTTL.setStatus("current")
_CienaCesGmplsDynamicTransitUniDirTunnelIncomingPackets_Type = Unsigned32
_CienaCesGmplsDynamicTransitUniDirTunnelIncomingPackets_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelIncomingPackets = _CienaCesGmplsDynamicTransitUniDirTunnelIncomingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 12),
    _CienaCesGmplsDynamicTransitUniDirTunnelIncomingPackets_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelIncomingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelIncomingPackets.setStatus("current")
_CienaCesGmplsDynamicTransitUniDirTunnelOutgoingPackets_Type = Unsigned32
_CienaCesGmplsDynamicTransitUniDirTunnelOutgoingPackets_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelOutgoingPackets = _CienaCesGmplsDynamicTransitUniDirTunnelOutgoingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 13),
    _CienaCesGmplsDynamicTransitUniDirTunnelOutgoingPackets_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelOutgoingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelOutgoingPackets.setStatus("current")
_CienaCesGmplsDynamicTransitUniDirTunnelIncomingBytes_Type = Unsigned32
_CienaCesGmplsDynamicTransitUniDirTunnelIncomingBytes_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelIncomingBytes = _CienaCesGmplsDynamicTransitUniDirTunnelIncomingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 14),
    _CienaCesGmplsDynamicTransitUniDirTunnelIncomingBytes_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelIncomingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelIncomingBytes.setStatus("current")
_CienaCesGmplsDynamicTransitUniDirTunnelOutgoingBytes_Type = Unsigned32
_CienaCesGmplsDynamicTransitUniDirTunnelOutgoingBytes_Object = MibTableColumn
cienaCesGmplsDynamicTransitUniDirTunnelOutgoingBytes = _CienaCesGmplsDynamicTransitUniDirTunnelOutgoingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 11, 1, 15),
    _CienaCesGmplsDynamicTransitUniDirTunnelOutgoingBytes_Type()
)
cienaCesGmplsDynamicTransitUniDirTunnelOutgoingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitUniDirTunnelOutgoingBytes.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelTable_Object = MibTable
cienaCesGmplsDynamicTransitCoroutedTunnelTable = _CienaCesGmplsDynamicTransitCoroutedTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelTable.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelEntry_Object = MibTableRow
cienaCesGmplsDynamicTransitCoroutedTunnelEntry = _CienaCesGmplsDynamicTransitCoroutedTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1)
)
cienaCesGmplsDynamicTransitCoroutedTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsDynamicTransitCoroutedTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelEntry.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelIndex_Type = Unsigned32
_CienaCesGmplsDynamicTransitCoroutedTunnelIndex_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelIndex = _CienaCesGmplsDynamicTransitCoroutedTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 1),
    _CienaCesGmplsDynamicTransitCoroutedTunnelIndex_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelIndex.setStatus("current")


class _CienaCesGmplsDynamicTransitCoroutedTunnelName_Type(DisplayString):
    """Custom type cienaCesGmplsDynamicTransitCoroutedTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesGmplsDynamicTransitCoroutedTunnelName_Type.__name__ = "DisplayString"
_CienaCesGmplsDynamicTransitCoroutedTunnelName_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelName = _CienaCesGmplsDynamicTransitCoroutedTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 2),
    _CienaCesGmplsDynamicTransitCoroutedTunnelName_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelName.setStatus("current")


class _CienaCesGmplsDynamicTransitCoroutedTunnelAdminState_Type(CienaGlobalState):
    """Custom type cienaCesGmplsDynamicTransitCoroutedTunnelAdminState based on CienaGlobalState"""


_CienaCesGmplsDynamicTransitCoroutedTunnelAdminState_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelAdminState = _CienaCesGmplsDynamicTransitCoroutedTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 3),
    _CienaCesGmplsDynamicTransitCoroutedTunnelAdminState_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelAdminState.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsDynamicTransitCoroutedTunnelOperState_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelOperState = _CienaCesGmplsDynamicTransitCoroutedTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 4),
    _CienaCesGmplsDynamicTransitCoroutedTunnelOperState_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelOperState.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelSourceIpAddr_Type = IpAddress
_CienaCesGmplsDynamicTransitCoroutedTunnelSourceIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelSourceIpAddr = _CienaCesGmplsDynamicTransitCoroutedTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 5),
    _CienaCesGmplsDynamicTransitCoroutedTunnelSourceIpAddr_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelSourceIpAddr.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsDynamicTransitCoroutedTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelDestIpAddr = _CienaCesGmplsDynamicTransitCoroutedTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 6),
    _CienaCesGmplsDynamicTransitCoroutedTunnelDestIpAddr_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelDestIpAddr.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelNextHopIpAddr_Type = IpAddress
_CienaCesGmplsDynamicTransitCoroutedTunnelNextHopIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelNextHopIpAddr = _CienaCesGmplsDynamicTransitCoroutedTunnelNextHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 7),
    _CienaCesGmplsDynamicTransitCoroutedTunnelNextHopIpAddr_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelNextHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelNextHopIpAddr.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelPrevHopIpAddr_Type = IpAddress
_CienaCesGmplsDynamicTransitCoroutedTunnelPrevHopIpAddr_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelPrevHopIpAddr = _CienaCesGmplsDynamicTransitCoroutedTunnelPrevHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 8),
    _CienaCesGmplsDynamicTransitCoroutedTunnelPrevHopIpAddr_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelPrevHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelPrevHopIpAddr.setStatus("current")


class _CienaCesGmplsDynamicTransitCoroutedTunnelForwardInLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicTransitCoroutedTunnelForwardInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsDynamicTransitCoroutedTunnelForwardInLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicTransitCoroutedTunnelForwardInLabel_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelForwardInLabel = _CienaCesGmplsDynamicTransitCoroutedTunnelForwardInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 9),
    _CienaCesGmplsDynamicTransitCoroutedTunnelForwardInLabel_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelForwardInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelForwardInLabel.setStatus("current")


class _CienaCesGmplsDynamicTransitCoroutedTunnelForwardOutLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicTransitCoroutedTunnelForwardOutLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsDynamicTransitCoroutedTunnelForwardOutLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicTransitCoroutedTunnelForwardOutLabel_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelForwardOutLabel = _CienaCesGmplsDynamicTransitCoroutedTunnelForwardOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 10),
    _CienaCesGmplsDynamicTransitCoroutedTunnelForwardOutLabel_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelForwardOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelForwardOutLabel.setStatus("current")


class _CienaCesGmplsDynamicTransitCoroutedTunnelReverseInLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicTransitCoroutedTunnelReverseInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsDynamicTransitCoroutedTunnelReverseInLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicTransitCoroutedTunnelReverseInLabel_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelReverseInLabel = _CienaCesGmplsDynamicTransitCoroutedTunnelReverseInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 11),
    _CienaCesGmplsDynamicTransitCoroutedTunnelReverseInLabel_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelReverseInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelReverseInLabel.setStatus("current")


class _CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutLabel_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutLabel = _CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 12),
    _CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutLabel_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutLabel.setStatus("current")


class _CienaCesGmplsDynamicTransitCoroutedTunnelTTLPolicy_Type(TTLPolicy):
    """Custom type cienaCesGmplsDynamicTransitCoroutedTunnelTTLPolicy based on TTLPolicy"""


_CienaCesGmplsDynamicTransitCoroutedTunnelTTLPolicy_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelTTLPolicy = _CienaCesGmplsDynamicTransitCoroutedTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 13),
    _CienaCesGmplsDynamicTransitCoroutedTunnelTTLPolicy_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelTTLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelTTLPolicy.setStatus("current")


class _CienaCesGmplsDynamicTransitCoroutedTunnelFixedTTL_Type(Unsigned32):
    """Custom type cienaCesGmplsDynamicTransitCoroutedTunnelFixedTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesGmplsDynamicTransitCoroutedTunnelFixedTTL_Type.__name__ = "Unsigned32"
_CienaCesGmplsDynamicTransitCoroutedTunnelFixedTTL_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelFixedTTL = _CienaCesGmplsDynamicTransitCoroutedTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 14),
    _CienaCesGmplsDynamicTransitCoroutedTunnelFixedTTL_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelFixedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelFixedTTL.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelIncomingPackets_Type = Unsigned32
_CienaCesGmplsDynamicTransitCoroutedTunnelIncomingPackets_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelIncomingPackets = _CienaCesGmplsDynamicTransitCoroutedTunnelIncomingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 15),
    _CienaCesGmplsDynamicTransitCoroutedTunnelIncomingPackets_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelIncomingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelIncomingPackets.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelOutgoingPackets_Type = Unsigned32
_CienaCesGmplsDynamicTransitCoroutedTunnelOutgoingPackets_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelOutgoingPackets = _CienaCesGmplsDynamicTransitCoroutedTunnelOutgoingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 16),
    _CienaCesGmplsDynamicTransitCoroutedTunnelOutgoingPackets_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelOutgoingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelOutgoingPackets.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelIncomingBytes_Type = Unsigned32
_CienaCesGmplsDynamicTransitCoroutedTunnelIncomingBytes_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelIncomingBytes = _CienaCesGmplsDynamicTransitCoroutedTunnelIncomingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 17),
    _CienaCesGmplsDynamicTransitCoroutedTunnelIncomingBytes_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelIncomingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelIncomingBytes.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelOutgoingBytes_Type = Unsigned32
_CienaCesGmplsDynamicTransitCoroutedTunnelOutgoingBytes_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelOutgoingBytes = _CienaCesGmplsDynamicTransitCoroutedTunnelOutgoingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 18),
    _CienaCesGmplsDynamicTransitCoroutedTunnelOutgoingBytes_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelOutgoingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelOutgoingBytes.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingPackets_Type = Unsigned32
_CienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingPackets_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingPackets = _CienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 19),
    _CienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingPackets_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingPackets.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingPackets_Type = Unsigned32
_CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingPackets_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingPackets = _CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 20),
    _CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingPackets_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingPackets.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingBytes_Type = Unsigned32
_CienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingBytes_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingBytes = _CienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 21),
    _CienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingBytes_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingBytes.setStatus("current")
_CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingBytes_Type = Unsigned32
_CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingBytes_Object = MibTableColumn
cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingBytes = _CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 12, 1, 22),
    _CienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingBytes_Type()
)
cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingBytes.setStatus("current")
_CienaCesGmplsAssociatedTunnelTable_Object = MibTable
cienaCesGmplsAssociatedTunnelTable = _CienaCesGmplsAssociatedTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13)
)
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedTunnelTable.setStatus("current")
_CienaCesGmplsAssociatedTunnelEntry_Object = MibTableRow
cienaCesGmplsAssociatedTunnelEntry = _CienaCesGmplsAssociatedTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1)
)
cienaCesGmplsAssociatedTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsAssociatedTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedTunnelEntry.setStatus("current")


class _CienaCesGmplsAssociatedTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsAssociatedTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsAssociatedTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsAssociatedTunnelIndex_Object = MibTableColumn
cienaCesGmplsAssociatedTunnelIndex = _CienaCesGmplsAssociatedTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 1),
    _CienaCesGmplsAssociatedTunnelIndex_Type()
)
cienaCesGmplsAssociatedTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedTunnelIndex.setStatus("current")
_CienaCesGmplsAssociatedTunnelName_Type = DisplayString
_CienaCesGmplsAssociatedTunnelName_Object = MibTableColumn
cienaCesGmplsAssociatedTunnelName = _CienaCesGmplsAssociatedTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 2),
    _CienaCesGmplsAssociatedTunnelName_Type()
)
cienaCesGmplsAssociatedTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedTunnelName.setStatus("current")
_CienaCesGmplsAssociatedForwardTunnelName_Type = DisplayString
_CienaCesGmplsAssociatedForwardTunnelName_Object = MibTableColumn
cienaCesGmplsAssociatedForwardTunnelName = _CienaCesGmplsAssociatedForwardTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 3),
    _CienaCesGmplsAssociatedForwardTunnelName_Type()
)
cienaCesGmplsAssociatedForwardTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedForwardTunnelName.setStatus("current")
_CienaCesGmplsAssociatedForwardTunnelType_Type = DisplayString
_CienaCesGmplsAssociatedForwardTunnelType_Object = MibTableColumn
cienaCesGmplsAssociatedForwardTunnelType = _CienaCesGmplsAssociatedForwardTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 4),
    _CienaCesGmplsAssociatedForwardTunnelType_Type()
)
cienaCesGmplsAssociatedForwardTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedForwardTunnelType.setStatus("current")
_CienaCesGmplsAssociatedReverseTunnelName_Type = DisplayString
_CienaCesGmplsAssociatedReverseTunnelName_Object = MibTableColumn
cienaCesGmplsAssociatedReverseTunnelName = _CienaCesGmplsAssociatedReverseTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 5),
    _CienaCesGmplsAssociatedReverseTunnelName_Type()
)
cienaCesGmplsAssociatedReverseTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedReverseTunnelName.setStatus("current")
_CienaCesGmplsAssociatedReverseTunnelType_Type = DisplayString
_CienaCesGmplsAssociatedReverseTunnelType_Object = MibTableColumn
cienaCesGmplsAssociatedReverseTunnelType = _CienaCesGmplsAssociatedReverseTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 6),
    _CienaCesGmplsAssociatedReverseTunnelType_Type()
)
cienaCesGmplsAssociatedReverseTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedReverseTunnelType.setStatus("current")
_CienaCesGmplsAssociatedForwardTunnelDestIpAddr_Type = IpAddress
_CienaCesGmplsAssociatedForwardTunnelDestIpAddr_Object = MibTableColumn
cienaCesGmplsAssociatedForwardTunnelDestIpAddr = _CienaCesGmplsAssociatedForwardTunnelDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 7),
    _CienaCesGmplsAssociatedForwardTunnelDestIpAddr_Type()
)
cienaCesGmplsAssociatedForwardTunnelDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedForwardTunnelDestIpAddr.setStatus("current")
_CienaCesGmplsAssociatedDynamicTunnelSrcIpAddr_Type = IpAddress
_CienaCesGmplsAssociatedDynamicTunnelSrcIpAddr_Object = MibTableColumn
cienaCesGmplsAssociatedDynamicTunnelSrcIpAddr = _CienaCesGmplsAssociatedDynamicTunnelSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 8),
    _CienaCesGmplsAssociatedDynamicTunnelSrcIpAddr_Type()
)
cienaCesGmplsAssociatedDynamicTunnelSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedDynamicTunnelSrcIpAddr.setStatus("current")
_CienaCesGmplsAssociatedTunnelAdminState_Type = CienaGlobalState
_CienaCesGmplsAssociatedTunnelAdminState_Object = MibTableColumn
cienaCesGmplsAssociatedTunnelAdminState = _CienaCesGmplsAssociatedTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 9),
    _CienaCesGmplsAssociatedTunnelAdminState_Type()
)
cienaCesGmplsAssociatedTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedTunnelAdminState.setStatus("current")
_CienaCesGmplsAssociatedTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsAssociatedTunnelOperState_Object = MibTableColumn
cienaCesGmplsAssociatedTunnelOperState = _CienaCesGmplsAssociatedTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 10),
    _CienaCesGmplsAssociatedTunnelOperState_Type()
)
cienaCesGmplsAssociatedTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedTunnelOperState.setStatus("current")
_CienaCesGmplsAssociatedForwardTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsAssociatedForwardTunnelOperState_Object = MibTableColumn
cienaCesGmplsAssociatedForwardTunnelOperState = _CienaCesGmplsAssociatedForwardTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 11),
    _CienaCesGmplsAssociatedForwardTunnelOperState_Type()
)
cienaCesGmplsAssociatedForwardTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedForwardTunnelOperState.setStatus("current")
_CienaCesGmplsAssociatedReverseTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsAssociatedReverseTunnelOperState_Object = MibTableColumn
cienaCesGmplsAssociatedReverseTunnelOperState = _CienaCesGmplsAssociatedReverseTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 12),
    _CienaCesGmplsAssociatedReverseTunnelOperState_Type()
)
cienaCesGmplsAssociatedReverseTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedReverseTunnelOperState.setStatus("current")


class _CienaCesGmplsAssociatedProtectionRole_Type(Integer32):
    """Custom type cienaCesGmplsAssociatedProtectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 0),
          ("primary", 1))
    )


_CienaCesGmplsAssociatedProtectionRole_Type.__name__ = "Integer32"
_CienaCesGmplsAssociatedProtectionRole_Object = MibTableColumn
cienaCesGmplsAssociatedProtectionRole = _CienaCesGmplsAssociatedProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 13),
    _CienaCesGmplsAssociatedProtectionRole_Type()
)
cienaCesGmplsAssociatedProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedProtectionRole.setStatus("current")


class _CienaCesGmplsAssociatedProtectionState_Type(Integer32):
    """Custom type cienaCesGmplsAssociatedProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 0))
    )


_CienaCesGmplsAssociatedProtectionState_Type.__name__ = "Integer32"
_CienaCesGmplsAssociatedProtectionState_Object = MibTableColumn
cienaCesGmplsAssociatedProtectionState = _CienaCesGmplsAssociatedProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 14),
    _CienaCesGmplsAssociatedProtectionState_Type()
)
cienaCesGmplsAssociatedProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedProtectionState.setStatus("current")
_CienaCesGmplsAssociatedTunnelProtectionPartnerName_Type = DisplayString
_CienaCesGmplsAssociatedTunnelProtectionPartnerName_Object = MibTableColumn
cienaCesGmplsAssociatedTunnelProtectionPartnerName = _CienaCesGmplsAssociatedTunnelProtectionPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 15),
    _CienaCesGmplsAssociatedTunnelProtectionPartnerName_Type()
)
cienaCesGmplsAssociatedTunnelProtectionPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedTunnelProtectionPartnerName.setStatus("current")
_CienaCesGmplsAssociatedBfdMonitoring_Type = CienaGlobalState
_CienaCesGmplsAssociatedBfdMonitoring_Object = MibTableColumn
cienaCesGmplsAssociatedBfdMonitoring = _CienaCesGmplsAssociatedBfdMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 16),
    _CienaCesGmplsAssociatedBfdMonitoring_Type()
)
cienaCesGmplsAssociatedBfdMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedBfdMonitoring.setStatus("current")
_CienaCesGmplsAssociatedBfdProfileName_Type = DisplayString
_CienaCesGmplsAssociatedBfdProfileName_Object = MibTableColumn
cienaCesGmplsAssociatedBfdProfileName = _CienaCesGmplsAssociatedBfdProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 17),
    _CienaCesGmplsAssociatedBfdProfileName_Type()
)
cienaCesGmplsAssociatedBfdProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedBfdProfileName.setStatus("current")
_CienaCesGmplsAssociatedBfdSessionName_Type = DisplayString
_CienaCesGmplsAssociatedBfdSessionName_Object = MibTableColumn
cienaCesGmplsAssociatedBfdSessionName = _CienaCesGmplsAssociatedBfdSessionName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 18),
    _CienaCesGmplsAssociatedBfdSessionName_Type()
)
cienaCesGmplsAssociatedBfdSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedBfdSessionName.setStatus("current")
_CienaCesGmplsAssociatedAisMonitoring_Type = CienaGlobalState
_CienaCesGmplsAssociatedAisMonitoring_Object = MibTableColumn
cienaCesGmplsAssociatedAisMonitoring = _CienaCesGmplsAssociatedAisMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 19),
    _CienaCesGmplsAssociatedAisMonitoring_Type()
)
cienaCesGmplsAssociatedAisMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedAisMonitoring.setStatus("current")
_CienaCesGmplsAssociatedAisProfileName_Type = DisplayString
_CienaCesGmplsAssociatedAisProfileName_Object = MibTableColumn
cienaCesGmplsAssociatedAisProfileName = _CienaCesGmplsAssociatedAisProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 20),
    _CienaCesGmplsAssociatedAisProfileName_Type()
)
cienaCesGmplsAssociatedAisProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedAisProfileName.setStatus("current")
_CienaCesGmplsAssociatedBfdSessionFaulted_Type = Integer32
_CienaCesGmplsAssociatedBfdSessionFaulted_Object = MibTableColumn
cienaCesGmplsAssociatedBfdSessionFaulted = _CienaCesGmplsAssociatedBfdSessionFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 21),
    _CienaCesGmplsAssociatedBfdSessionFaulted_Type()
)
cienaCesGmplsAssociatedBfdSessionFaulted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedBfdSessionFaulted.setStatus("current")


class _CienaCesGmplsAssociatedBfdProfileIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsAssociatedBfdProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsAssociatedBfdProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsAssociatedBfdProfileIndex_Object = MibTableColumn
cienaCesGmplsAssociatedBfdProfileIndex = _CienaCesGmplsAssociatedBfdProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 13, 1, 22),
    _CienaCesGmplsAssociatedBfdProfileIndex_Type()
)
cienaCesGmplsAssociatedBfdProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedBfdProfileIndex.setStatus("current")
_CienaCesGmplsTunnelARHopTable_Object = MibTable
cienaCesGmplsTunnelARHopTable = _CienaCesGmplsTunnelARHopTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 14)
)
if mibBuilder.loadTexts:
    cienaCesGmplsTunnelARHopTable.setStatus("current")
_CienaCesGmplsTunnelARHopEntry_Object = MibTableRow
cienaCesGmplsTunnelARHopEntry = _CienaCesGmplsTunnelARHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 14, 1)
)
cienaCesGmplsTunnelARHopEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaGmplsTunnelARHopListIndex"),
    (0, "CIENA-CES-MPLS-MIB", "cienaGmplsTunnelARHopIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsTunnelARHopEntry.setStatus("current")
_CienaGmplsTunnelARHopListIndex_Type = Unsigned32
_CienaGmplsTunnelARHopListIndex_Object = MibTableColumn
cienaGmplsTunnelARHopListIndex = _CienaGmplsTunnelARHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 14, 1, 1),
    _CienaGmplsTunnelARHopListIndex_Type()
)
cienaGmplsTunnelARHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaGmplsTunnelARHopListIndex.setStatus("current")
_CienaGmplsTunnelARHopIndex_Type = Unsigned32
_CienaGmplsTunnelARHopIndex_Object = MibTableColumn
cienaGmplsTunnelARHopIndex = _CienaGmplsTunnelARHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 14, 1, 2),
    _CienaGmplsTunnelARHopIndex_Type()
)
cienaGmplsTunnelARHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaGmplsTunnelARHopIndex.setStatus("current")
_CienaGmplsTunnelARHopAddrType_Type = Integer32
_CienaGmplsTunnelARHopAddrType_Object = MibTableColumn
cienaGmplsTunnelARHopAddrType = _CienaGmplsTunnelARHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 14, 1, 3),
    _CienaGmplsTunnelARHopAddrType_Type()
)
cienaGmplsTunnelARHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaGmplsTunnelARHopAddrType.setStatus("current")
_CienaGmplsTunnelARHopIpAddr_Type = IpAddress
_CienaGmplsTunnelARHopIpAddr_Object = MibTableColumn
cienaGmplsTunnelARHopIpAddr = _CienaGmplsTunnelARHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 14, 1, 4),
    _CienaGmplsTunnelARHopIpAddr_Type()
)
cienaGmplsTunnelARHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaGmplsTunnelARHopIpAddr.setStatus("current")
_CienaGmplsTunnelARHopAddrUnnum_Type = Unsigned32
_CienaGmplsTunnelARHopAddrUnnum_Object = MibTableColumn
cienaGmplsTunnelARHopAddrUnnum = _CienaGmplsTunnelARHopAddrUnnum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 14, 1, 5),
    _CienaGmplsTunnelARHopAddrUnnum_Type()
)
cienaGmplsTunnelARHopAddrUnnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaGmplsTunnelARHopAddrUnnum.setStatus("current")
_CienaGmplsTunnelARHopLspId_Type = Unsigned32
_CienaGmplsTunnelARHopLspId_Object = MibTableColumn
cienaGmplsTunnelARHopLspId = _CienaGmplsTunnelARHopLspId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 14, 1, 6),
    _CienaGmplsTunnelARHopLspId_Type()
)
cienaGmplsTunnelARHopLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaGmplsTunnelARHopLspId.setStatus("current")
_CienaCesGmplsEncapTunnelNotif_ObjectIdentity = ObjectIdentity
cienaCesGmplsEncapTunnelNotif = _CienaCesGmplsEncapTunnelNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15)
)
_CienaCesGmplsNotifEncapTunnelTable_Object = MibTable
cienaCesGmplsNotifEncapTunnelTable = _CienaCesGmplsNotifEncapTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelTable.setStatus("current")
_CienaCesGmplsNotifEncapTunnelEntry_Object = MibTableRow
cienaCesGmplsNotifEncapTunnelEntry = _CienaCesGmplsNotifEncapTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1)
)
cienaCesGmplsNotifEncapTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelType"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelEntry.setStatus("current")


class _CienaCesGmplsNotifEncapTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsNotifEncapTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsNotifEncapTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsNotifEncapTunnelIndex_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelIndex = _CienaCesGmplsNotifEncapTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 1),
    _CienaCesGmplsNotifEncapTunnelIndex_Type()
)
cienaCesGmplsNotifEncapTunnelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelIndex.setStatus("current")


class _CienaCesGmplsNotifEncapTunnelType_Type(Integer32):
    """Custom type cienaCesGmplsNotifEncapTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CienaCesGmplsNotifEncapTunnelType_Type.__name__ = "Integer32"
_CienaCesGmplsNotifEncapTunnelType_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelType = _CienaCesGmplsNotifEncapTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 2),
    _CienaCesGmplsNotifEncapTunnelType_Type()
)
cienaCesGmplsNotifEncapTunnelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelType.setStatus("current")
_CienaCesGmplsNotifEncapTunnelName_Type = DisplayString
_CienaCesGmplsNotifEncapTunnelName_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelName = _CienaCesGmplsNotifEncapTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 3),
    _CienaCesGmplsNotifEncapTunnelName_Type()
)
cienaCesGmplsNotifEncapTunnelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelName.setStatus("current")
_CienaCesGmplsNotifEncapTunnelAdminState_Type = CienaGlobalState
_CienaCesGmplsNotifEncapTunnelAdminState_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelAdminState = _CienaCesGmplsNotifEncapTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 4),
    _CienaCesGmplsNotifEncapTunnelAdminState_Type()
)
cienaCesGmplsNotifEncapTunnelAdminState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelAdminState.setStatus("current")
_CienaCesGmplsNotifEncapTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsNotifEncapTunnelOperState_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelOperState = _CienaCesGmplsNotifEncapTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 5),
    _CienaCesGmplsNotifEncapTunnelOperState_Type()
)
cienaCesGmplsNotifEncapTunnelOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelOperState.setStatus("current")
_CienaCesGmplsNotifEncapTunnelAisFaulted_Type = TunnelAisFault
_CienaCesGmplsNotifEncapTunnelAisFaulted_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelAisFaulted = _CienaCesGmplsNotifEncapTunnelAisFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 6),
    _CienaCesGmplsNotifEncapTunnelAisFaulted_Type()
)
cienaCesGmplsNotifEncapTunnelAisFaulted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelAisFaulted.setStatus("obsolete")
_CienaCesGmplsNotifEncapTunnelFaultedNodeId_Type = IpAddress
_CienaCesGmplsNotifEncapTunnelFaultedNodeId_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelFaultedNodeId = _CienaCesGmplsNotifEncapTunnelFaultedNodeId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 7),
    _CienaCesGmplsNotifEncapTunnelFaultedNodeId_Type()
)
cienaCesGmplsNotifEncapTunnelFaultedNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelFaultedNodeId.setStatus("current")
_CienaCesGmplsNotifEncapTunnelFarEndLerId_Type = IpAddress
_CienaCesGmplsNotifEncapTunnelFarEndLerId_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelFarEndLerId = _CienaCesGmplsNotifEncapTunnelFarEndLerId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 8),
    _CienaCesGmplsNotifEncapTunnelFarEndLerId_Type()
)
cienaCesGmplsNotifEncapTunnelFarEndLerId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelFarEndLerId.setStatus("current")


class _CienaCesGmplsNotifEncapTunnelResult_Type(Integer32):
    """Custom type cienaCesGmplsNotifEncapTunnelResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("success", 1))
    )


_CienaCesGmplsNotifEncapTunnelResult_Type.__name__ = "Integer32"
_CienaCesGmplsNotifEncapTunnelResult_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelResult = _CienaCesGmplsNotifEncapTunnelResult_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 9),
    _CienaCesGmplsNotifEncapTunnelResult_Type()
)
cienaCesGmplsNotifEncapTunnelResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelResult.setStatus("current")


class _CienaCesGmplsNotifEncapTunnelProtectionRole_Type(Integer32):
    """Custom type cienaCesGmplsNotifEncapTunnelProtectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 0),
          ("primary", 1))
    )


_CienaCesGmplsNotifEncapTunnelProtectionRole_Type.__name__ = "Integer32"
_CienaCesGmplsNotifEncapTunnelProtectionRole_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelProtectionRole = _CienaCesGmplsNotifEncapTunnelProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 10),
    _CienaCesGmplsNotifEncapTunnelProtectionRole_Type()
)
cienaCesGmplsNotifEncapTunnelProtectionRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelProtectionRole.setStatus("current")


class _CienaCesGmplsNotifEncapTunnelRequestedBw_Type(Unsigned32):
    """Custom type cienaCesGmplsNotifEncapTunnelRequestedBw based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsNotifEncapTunnelRequestedBw_Type.__name__ = "Unsigned32"
_CienaCesGmplsNotifEncapTunnelRequestedBw_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelRequestedBw = _CienaCesGmplsNotifEncapTunnelRequestedBw_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 11),
    _CienaCesGmplsNotifEncapTunnelRequestedBw_Type()
)
cienaCesGmplsNotifEncapTunnelRequestedBw.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelRequestedBw.setStatus("current")


class _CienaCesGmplsNotifEncapTunnelOperationalBw_Type(Unsigned32):
    """Custom type cienaCesGmplsNotifEncapTunnelOperationalBw based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsNotifEncapTunnelOperationalBw_Type.__name__ = "Unsigned32"
_CienaCesGmplsNotifEncapTunnelOperationalBw_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelOperationalBw = _CienaCesGmplsNotifEncapTunnelOperationalBw_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 12),
    _CienaCesGmplsNotifEncapTunnelOperationalBw_Type()
)
cienaCesGmplsNotifEncapTunnelOperationalBw.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelOperationalBw.setStatus("current")


class _CienaCesGmplsNotifEncapTunnelMbbParentApp_Type(Integer32):
    """Custom type cienaCesGmplsNotifEncapTunnelMbbParentApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autosize", 2),
          ("lspreoptimization", 3),
          ("none", 1))
    )


_CienaCesGmplsNotifEncapTunnelMbbParentApp_Type.__name__ = "Integer32"
_CienaCesGmplsNotifEncapTunnelMbbParentApp_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelMbbParentApp = _CienaCesGmplsNotifEncapTunnelMbbParentApp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 13),
    _CienaCesGmplsNotifEncapTunnelMbbParentApp_Type()
)
cienaCesGmplsNotifEncapTunnelMbbParentApp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelMbbParentApp.setStatus("current")
_CienaCesGmplsNotifEncapTunnelOamFaulted_Type = TunnelOamFault
_CienaCesGmplsNotifEncapTunnelOamFaulted_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelOamFaulted = _CienaCesGmplsNotifEncapTunnelOamFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 15, 1, 1, 14),
    _CienaCesGmplsNotifEncapTunnelOamFaulted_Type()
)
cienaCesGmplsNotifEncapTunnelOamFaulted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelOamFaulted.setStatus("current")
_CienaCesGmplsDecapTunnelNotif_ObjectIdentity = ObjectIdentity
cienaCesGmplsDecapTunnelNotif = _CienaCesGmplsDecapTunnelNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 16)
)
_CienaCesGmplsNotifDecapTunnelTable_Object = MibTable
cienaCesGmplsNotifDecapTunnelTable = _CienaCesGmplsNotifDecapTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 16, 1)
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelTable.setStatus("current")
_CienaCesGmplsNotifDecapTunnelEntry_Object = MibTableRow
cienaCesGmplsNotifDecapTunnelEntry = _CienaCesGmplsNotifDecapTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 16, 1, 1)
)
cienaCesGmplsNotifDecapTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelType"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelEntry.setStatus("current")


class _CienaCesGmplsNotifDecapTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsNotifDecapTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsNotifDecapTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsNotifDecapTunnelIndex_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelIndex = _CienaCesGmplsNotifDecapTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 16, 1, 1, 1),
    _CienaCesGmplsNotifDecapTunnelIndex_Type()
)
cienaCesGmplsNotifDecapTunnelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelIndex.setStatus("current")


class _CienaCesGmplsNotifDecapTunnelType_Type(Integer32):
    """Custom type cienaCesGmplsNotifDecapTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CienaCesGmplsNotifDecapTunnelType_Type.__name__ = "Integer32"
_CienaCesGmplsNotifDecapTunnelType_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelType = _CienaCesGmplsNotifDecapTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 16, 1, 1, 2),
    _CienaCesGmplsNotifDecapTunnelType_Type()
)
cienaCesGmplsNotifDecapTunnelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelType.setStatus("current")
_CienaCesGmplsNotifDecapTunnelName_Type = DisplayString
_CienaCesGmplsNotifDecapTunnelName_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelName = _CienaCesGmplsNotifDecapTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 16, 1, 1, 3),
    _CienaCesGmplsNotifDecapTunnelName_Type()
)
cienaCesGmplsNotifDecapTunnelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelName.setStatus("current")
_CienaCesGmplsNotifDecapTunnelAdminState_Type = CienaGlobalState
_CienaCesGmplsNotifDecapTunnelAdminState_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelAdminState = _CienaCesGmplsNotifDecapTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 16, 1, 1, 4),
    _CienaCesGmplsNotifDecapTunnelAdminState_Type()
)
cienaCesGmplsNotifDecapTunnelAdminState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelAdminState.setStatus("current")
_CienaCesGmplsNotifDecapTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsNotifDecapTunnelOperState_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelOperState = _CienaCesGmplsNotifDecapTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 16, 1, 1, 5),
    _CienaCesGmplsNotifDecapTunnelOperState_Type()
)
cienaCesGmplsNotifDecapTunnelOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelOperState.setStatus("current")
_CienaCesGmplsNotifDecapTunnelAisFaulted_Type = TunnelAisFault
_CienaCesGmplsNotifDecapTunnelAisFaulted_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelAisFaulted = _CienaCesGmplsNotifDecapTunnelAisFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 16, 1, 1, 6),
    _CienaCesGmplsNotifDecapTunnelAisFaulted_Type()
)
cienaCesGmplsNotifDecapTunnelAisFaulted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelAisFaulted.setStatus("obsolete")
_CienaCesGmplsNotifDecapTunnelFaultedNodeId_Type = IpAddress
_CienaCesGmplsNotifDecapTunnelFaultedNodeId_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelFaultedNodeId = _CienaCesGmplsNotifDecapTunnelFaultedNodeId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 16, 1, 1, 7),
    _CienaCesGmplsNotifDecapTunnelFaultedNodeId_Type()
)
cienaCesGmplsNotifDecapTunnelFaultedNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelFaultedNodeId.setStatus("current")
_CienaCesGmplsNotifDecapTunnelFarEndLerId_Type = IpAddress
_CienaCesGmplsNotifDecapTunnelFarEndLerId_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelFarEndLerId = _CienaCesGmplsNotifDecapTunnelFarEndLerId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 16, 1, 1, 8),
    _CienaCesGmplsNotifDecapTunnelFarEndLerId_Type()
)
cienaCesGmplsNotifDecapTunnelFarEndLerId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelFarEndLerId.setStatus("current")
_CienaCesGmplsNotifDecapTunnelOamFaulted_Type = TunnelOamFault
_CienaCesGmplsNotifDecapTunnelOamFaulted_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelOamFaulted = _CienaCesGmplsNotifDecapTunnelOamFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 16, 1, 1, 9),
    _CienaCesGmplsNotifDecapTunnelOamFaulted_Type()
)
cienaCesGmplsNotifDecapTunnelOamFaulted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelOamFaulted.setStatus("current")
_CienaCesGmplsTransitTunnelNotif_ObjectIdentity = ObjectIdentity
cienaCesGmplsTransitTunnelNotif = _CienaCesGmplsTransitTunnelNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 17)
)
_CienaCesGmplsNotifTransitTunnelTable_Object = MibTable
cienaCesGmplsNotifTransitTunnelTable = _CienaCesGmplsNotifTransitTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifTransitTunnelTable.setStatus("current")
_CienaCesGmplsNotifTransitTunnelEntry_Object = MibTableRow
cienaCesGmplsNotifTransitTunnelEntry = _CienaCesGmplsNotifTransitTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 17, 1, 1)
)
cienaCesGmplsNotifTransitTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelType"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifTransitTunnelEntry.setStatus("current")


class _CienaCesGmplsNotifTransitTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsNotifTransitTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsNotifTransitTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsNotifTransitTunnelIndex_Object = MibTableColumn
cienaCesGmplsNotifTransitTunnelIndex = _CienaCesGmplsNotifTransitTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 17, 1, 1, 1),
    _CienaCesGmplsNotifTransitTunnelIndex_Type()
)
cienaCesGmplsNotifTransitTunnelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifTransitTunnelIndex.setStatus("current")


class _CienaCesGmplsNotifTransitTunnelType_Type(Integer32):
    """Custom type cienaCesGmplsNotifTransitTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CienaCesGmplsNotifTransitTunnelType_Type.__name__ = "Integer32"
_CienaCesGmplsNotifTransitTunnelType_Object = MibTableColumn
cienaCesGmplsNotifTransitTunnelType = _CienaCesGmplsNotifTransitTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 17, 1, 1, 2),
    _CienaCesGmplsNotifTransitTunnelType_Type()
)
cienaCesGmplsNotifTransitTunnelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifTransitTunnelType.setStatus("current")
_CienaCesGmplsNotifTransitTunnelName_Type = DisplayString
_CienaCesGmplsNotifTransitTunnelName_Object = MibTableColumn
cienaCesGmplsNotifTransitTunnelName = _CienaCesGmplsNotifTransitTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 17, 1, 1, 3),
    _CienaCesGmplsNotifTransitTunnelName_Type()
)
cienaCesGmplsNotifTransitTunnelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifTransitTunnelName.setStatus("current")
_CienaCesGmplsNotifTransitTunnelAdminState_Type = CienaGlobalState
_CienaCesGmplsNotifTransitTunnelAdminState_Object = MibTableColumn
cienaCesGmplsNotifTransitTunnelAdminState = _CienaCesGmplsNotifTransitTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 17, 1, 1, 4),
    _CienaCesGmplsNotifTransitTunnelAdminState_Type()
)
cienaCesGmplsNotifTransitTunnelAdminState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifTransitTunnelAdminState.setStatus("current")
_CienaCesGmplsNotifTransitTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsNotifTransitTunnelOperState_Object = MibTableColumn
cienaCesGmplsNotifTransitTunnelOperState = _CienaCesGmplsNotifTransitTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 17, 1, 1, 5),
    _CienaCesGmplsNotifTransitTunnelOperState_Type()
)
cienaCesGmplsNotifTransitTunnelOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifTransitTunnelOperState.setStatus("current")
_CienaCesGmplsNotifTransitTunnelOamFaulted_Type = TunnelOamFault
_CienaCesGmplsNotifTransitTunnelOamFaulted_Object = MibTableColumn
cienaCesGmplsNotifTransitTunnelOamFaulted = _CienaCesGmplsNotifTransitTunnelOamFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 17, 1, 1, 6),
    _CienaCesGmplsNotifTransitTunnelOamFaulted_Type()
)
cienaCesGmplsNotifTransitTunnelOamFaulted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifTransitTunnelOamFaulted.setStatus("current")
_CienaCesGmplsAssociatedTunnelNotif_ObjectIdentity = ObjectIdentity
cienaCesGmplsAssociatedTunnelNotif = _CienaCesGmplsAssociatedTunnelNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 18)
)
_CienaCesGmplsNotifAssociatedTunnelTable_Object = MibTable
cienaCesGmplsNotifAssociatedTunnelTable = _CienaCesGmplsNotifAssociatedTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 18, 1)
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifAssociatedTunnelTable.setStatus("current")
_CienaCesGmplsNotifAssociatedTunnelEntry_Object = MibTableRow
cienaCesGmplsNotifAssociatedTunnelEntry = _CienaCesGmplsNotifAssociatedTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 18, 1, 1)
)
cienaCesGmplsNotifAssociatedTunnelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelType"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifAssociatedTunnelEntry.setStatus("current")


class _CienaCesGmplsNotifAssociatedTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsNotifAssociatedTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsNotifAssociatedTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsNotifAssociatedTunnelIndex_Object = MibTableColumn
cienaCesGmplsNotifAssociatedTunnelIndex = _CienaCesGmplsNotifAssociatedTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 18, 1, 1, 1),
    _CienaCesGmplsNotifAssociatedTunnelIndex_Type()
)
cienaCesGmplsNotifAssociatedTunnelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifAssociatedTunnelIndex.setStatus("current")


class _CienaCesGmplsNotifAssociatedTunnelType_Type(Integer32):
    """Custom type cienaCesGmplsNotifAssociatedTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CienaCesGmplsNotifAssociatedTunnelType_Type.__name__ = "Integer32"
_CienaCesGmplsNotifAssociatedTunnelType_Object = MibTableColumn
cienaCesGmplsNotifAssociatedTunnelType = _CienaCesGmplsNotifAssociatedTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 18, 1, 1, 2),
    _CienaCesGmplsNotifAssociatedTunnelType_Type()
)
cienaCesGmplsNotifAssociatedTunnelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifAssociatedTunnelType.setStatus("current")
_CienaCesGmplsNotifAssociatedTunnelName_Type = DisplayString
_CienaCesGmplsNotifAssociatedTunnelName_Object = MibTableColumn
cienaCesGmplsNotifAssociatedTunnelName = _CienaCesGmplsNotifAssociatedTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 18, 1, 1, 3),
    _CienaCesGmplsNotifAssociatedTunnelName_Type()
)
cienaCesGmplsNotifAssociatedTunnelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifAssociatedTunnelName.setStatus("current")
_CienaCesGmplsNotifAssociatedTunnelAdminState_Type = CienaGlobalState
_CienaCesGmplsNotifAssociatedTunnelAdminState_Object = MibTableColumn
cienaCesGmplsNotifAssociatedTunnelAdminState = _CienaCesGmplsNotifAssociatedTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 18, 1, 1, 4),
    _CienaCesGmplsNotifAssociatedTunnelAdminState_Type()
)
cienaCesGmplsNotifAssociatedTunnelAdminState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifAssociatedTunnelAdminState.setStatus("current")
_CienaCesGmplsNotifAssociatedTunnelOperState_Type = CienaGlobalState
_CienaCesGmplsNotifAssociatedTunnelOperState_Object = MibTableColumn
cienaCesGmplsNotifAssociatedTunnelOperState = _CienaCesGmplsNotifAssociatedTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 18, 1, 1, 5),
    _CienaCesGmplsNotifAssociatedTunnelOperState_Type()
)
cienaCesGmplsNotifAssociatedTunnelOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifAssociatedTunnelOperState.setStatus("current")
_CienaCesGmplsNotifAssociatedTunnelAisFaulted_Type = TunnelAisFault
_CienaCesGmplsNotifAssociatedTunnelAisFaulted_Object = MibTableColumn
cienaCesGmplsNotifAssociatedTunnelAisFaulted = _CienaCesGmplsNotifAssociatedTunnelAisFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 18, 1, 1, 6),
    _CienaCesGmplsNotifAssociatedTunnelAisFaulted_Type()
)
cienaCesGmplsNotifAssociatedTunnelAisFaulted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifAssociatedTunnelAisFaulted.setStatus("obsolete")
_CienaCesGmplsNotifAssociatedTunnelFaultedNodeId_Type = IpAddress
_CienaCesGmplsNotifAssociatedTunnelFaultedNodeId_Object = MibTableColumn
cienaCesGmplsNotifAssociatedTunnelFaultedNodeId = _CienaCesGmplsNotifAssociatedTunnelFaultedNodeId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 18, 1, 1, 7),
    _CienaCesGmplsNotifAssociatedTunnelFaultedNodeId_Type()
)
cienaCesGmplsNotifAssociatedTunnelFaultedNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifAssociatedTunnelFaultedNodeId.setStatus("current")
_CienaCesGmplsNotifAssociatedTunnelFarEndLerId_Type = IpAddress
_CienaCesGmplsNotifAssociatedTunnelFarEndLerId_Object = MibTableColumn
cienaCesGmplsNotifAssociatedTunnelFarEndLerId = _CienaCesGmplsNotifAssociatedTunnelFarEndLerId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 18, 1, 1, 8),
    _CienaCesGmplsNotifAssociatedTunnelFarEndLerId_Type()
)
cienaCesGmplsNotifAssociatedTunnelFarEndLerId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifAssociatedTunnelFarEndLerId.setStatus("current")
_CienaCesGmplsNotifAssociatedTunnelOamFaulted_Type = TunnelOamFault
_CienaCesGmplsNotifAssociatedTunnelOamFaulted_Object = MibTableColumn
cienaCesGmplsNotifAssociatedTunnelOamFaulted = _CienaCesGmplsNotifAssociatedTunnelOamFaulted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 18, 1, 1, 9),
    _CienaCesGmplsNotifAssociatedTunnelOamFaulted_Type()
)
cienaCesGmplsNotifAssociatedTunnelOamFaulted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifAssociatedTunnelOamFaulted.setStatus("current")
_CienaCesGmplsEncapTunnelGrpNotif_ObjectIdentity = ObjectIdentity
cienaCesGmplsEncapTunnelGrpNotif = _CienaCesGmplsEncapTunnelGrpNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 19)
)
_CienaCesGmplsNotifEncapTunnelGrpTable_Object = MibTable
cienaCesGmplsNotifEncapTunnelGrpTable = _CienaCesGmplsNotifEncapTunnelGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 19, 1)
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelGrpTable.setStatus("current")
_CienaCesGmplsNotifEncapTunnelGrpEntry_Object = MibTableRow
cienaCesGmplsNotifEncapTunnelGrpEntry = _CienaCesGmplsNotifEncapTunnelGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 19, 1, 1)
)
cienaCesGmplsNotifEncapTunnelGrpEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelGrpIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelGrpEntry.setStatus("current")


class _CienaCesGmplsNotifEncapTunnelGrpIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsNotifEncapTunnelGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsNotifEncapTunnelGrpIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsNotifEncapTunnelGrpIndex_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelGrpIndex = _CienaCesGmplsNotifEncapTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 19, 1, 1, 1),
    _CienaCesGmplsNotifEncapTunnelGrpIndex_Type()
)
cienaCesGmplsNotifEncapTunnelGrpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelGrpIndex.setStatus("current")
_CienaCesGmplsNotifEncapTunnelGrpName_Type = DisplayString
_CienaCesGmplsNotifEncapTunnelGrpName_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelGrpName = _CienaCesGmplsNotifEncapTunnelGrpName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 19, 1, 1, 2),
    _CienaCesGmplsNotifEncapTunnelGrpName_Type()
)
cienaCesGmplsNotifEncapTunnelGrpName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelGrpName.setStatus("current")


class _CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex = _CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 19, 1, 1, 3),
    _CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex_Type()
)
cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex.setStatus("current")
_CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlName_Type = DisplayString
_CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlName_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlName = _CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 19, 1, 1, 4),
    _CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlName_Type()
)
cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlName.setStatus("current")


class _CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType_Type(Integer32):
    """Custom type cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType_Type.__name__ = "Integer32"
_CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType_Object = MibTableColumn
cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType = _CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 19, 1, 1, 5),
    _CienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType_Type()
)
cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType.setStatus("current")
_CienaCesGmplsDecapTunnelGrpNotif_ObjectIdentity = ObjectIdentity
cienaCesGmplsDecapTunnelGrpNotif = _CienaCesGmplsDecapTunnelGrpNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 20)
)
_CienaCesGmplsNotifDecapTunnelGrpTable_Object = MibTable
cienaCesGmplsNotifDecapTunnelGrpTable = _CienaCesGmplsNotifDecapTunnelGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 20, 1)
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelGrpTable.setStatus("current")
_CienaCesGmplsNotifDecapTunnelGrpEntry_Object = MibTableRow
cienaCesGmplsNotifDecapTunnelGrpEntry = _CienaCesGmplsNotifDecapTunnelGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 20, 1, 1)
)
cienaCesGmplsNotifDecapTunnelGrpEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelGrpIndex"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelGrpEntry.setStatus("current")


class _CienaCesGmplsNotifDecapTunnelGrpIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsNotifDecapTunnelGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsNotifDecapTunnelGrpIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsNotifDecapTunnelGrpIndex_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelGrpIndex = _CienaCesGmplsNotifDecapTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 20, 1, 1, 1),
    _CienaCesGmplsNotifDecapTunnelGrpIndex_Type()
)
cienaCesGmplsNotifDecapTunnelGrpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelGrpIndex.setStatus("current")
_CienaCesGmplsNotifDecapTunnelGrpName_Type = DisplayString
_CienaCesGmplsNotifDecapTunnelGrpName_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelGrpName = _CienaCesGmplsNotifDecapTunnelGrpName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 20, 1, 1, 2),
    _CienaCesGmplsNotifDecapTunnelGrpName_Type()
)
cienaCesGmplsNotifDecapTunnelGrpName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelGrpName.setStatus("current")


class _CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlIndex_Type(Unsigned32):
    """Custom type cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlIndex_Type.__name__ = "Unsigned32"
_CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlIndex_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlIndex = _CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 20, 1, 1, 3),
    _CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlIndex_Type()
)
cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlIndex.setStatus("current")
_CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlName_Type = DisplayString
_CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlName_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlName = _CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 20, 1, 1, 4),
    _CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlName_Type()
)
cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlName.setStatus("current")


class _CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlType_Type(Integer32):
    """Custom type cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlType_Type.__name__ = "Integer32"
_CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlType_Object = MibTableColumn
cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlType = _CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 20, 1, 1, 5),
    _CienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlType_Type()
)
cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlType.setStatus("current")
_CienaCesGmplsTunnelAisFaultErrorNotif_ObjectIdentity = ObjectIdentity
cienaCesGmplsTunnelAisFaultErrorNotif = _CienaCesGmplsTunnelAisFaultErrorNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 21)
)
_CienaCesGmplsNotifTunnelAisFaultErrorTable_Object = MibTable
cienaCesGmplsNotifTunnelAisFaultErrorTable = _CienaCesGmplsNotifTunnelAisFaultErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 21, 1)
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifTunnelAisFaultErrorTable.setStatus("current")
_CienaCesGmplsNotifTunnelAisFaultErrorEntry_Object = MibTableRow
cienaCesGmplsNotifTunnelAisFaultErrorEntry = _CienaCesGmplsNotifTunnelAisFaultErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 21, 1, 1)
)
cienaCesGmplsNotifTunnelAisFaultErrorEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTunnelDecapLabel"),
)
if mibBuilder.loadTexts:
    cienaCesGmplsNotifTunnelAisFaultErrorEntry.setStatus("current")


class _CienaCesGmplsNotifTunnelDecapLabel_Type(Unsigned32):
    """Custom type cienaCesGmplsNotifTunnelDecapLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesGmplsNotifTunnelDecapLabel_Type.__name__ = "Unsigned32"
_CienaCesGmplsNotifTunnelDecapLabel_Object = MibTableColumn
cienaCesGmplsNotifTunnelDecapLabel = _CienaCesGmplsNotifTunnelDecapLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 21, 1, 1, 1),
    _CienaCesGmplsNotifTunnelDecapLabel_Type()
)
cienaCesGmplsNotifTunnelDecapLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifTunnelDecapLabel.setStatus("current")
_CienaCesGmplsNotifTunnelErrorMsg_Type = DisplayString
_CienaCesGmplsNotifTunnelErrorMsg_Object = MibTableColumn
cienaCesGmplsNotifTunnelErrorMsg = _CienaCesGmplsNotifTunnelErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 2, 21, 1, 1, 2),
    _CienaCesGmplsNotifTunnelErrorMsg_Type()
)
cienaCesGmplsNotifTunnelErrorMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesGmplsNotifTunnelErrorMsg.setStatus("current")
_CienaCesMplsGlobal_ObjectIdentity = ObjectIdentity
cienaCesMplsGlobal = _CienaCesMplsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3)
)
_CienaCesMplsAttrs_ObjectIdentity = ObjectIdentity
cienaCesMplsAttrs = _CienaCesMplsAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1)
)


class _CienaCesMplsGlobalStaticAdminLabelRangeStart_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalStaticAdminLabelRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalStaticAdminLabelRangeStart_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalStaticAdminLabelRangeStart_Object = MibScalar
cienaCesMplsGlobalStaticAdminLabelRangeStart = _CienaCesMplsGlobalStaticAdminLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 1),
    _CienaCesMplsGlobalStaticAdminLabelRangeStart_Type()
)
cienaCesMplsGlobalStaticAdminLabelRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalStaticAdminLabelRangeStart.setStatus("current")


class _CienaCesMplsGlobalStaticAdminLabelRangeEnd_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalStaticAdminLabelRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalStaticAdminLabelRangeEnd_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalStaticAdminLabelRangeEnd_Object = MibScalar
cienaCesMplsGlobalStaticAdminLabelRangeEnd = _CienaCesMplsGlobalStaticAdminLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 2),
    _CienaCesMplsGlobalStaticAdminLabelRangeEnd_Type()
)
cienaCesMplsGlobalStaticAdminLabelRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalStaticAdminLabelRangeEnd.setStatus("current")


class _CienaCesMplsGlobalStaticOperLabelRangeStart_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalStaticOperLabelRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalStaticOperLabelRangeStart_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalStaticOperLabelRangeStart_Object = MibScalar
cienaCesMplsGlobalStaticOperLabelRangeStart = _CienaCesMplsGlobalStaticOperLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 3),
    _CienaCesMplsGlobalStaticOperLabelRangeStart_Type()
)
cienaCesMplsGlobalStaticOperLabelRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalStaticOperLabelRangeStart.setStatus("current")


class _CienaCesMplsGlobalStaticOperLabelRangeEnd_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalStaticOperLabelRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalStaticOperLabelRangeEnd_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalStaticOperLabelRangeEnd_Object = MibScalar
cienaCesMplsGlobalStaticOperLabelRangeEnd = _CienaCesMplsGlobalStaticOperLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 4),
    _CienaCesMplsGlobalStaticOperLabelRangeEnd_Type()
)
cienaCesMplsGlobalStaticOperLabelRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalStaticOperLabelRangeEnd.setStatus("current")


class _CienaCesMplsGlobalDynamicAdminLabelRangeStart_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalDynamicAdminLabelRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalDynamicAdminLabelRangeStart_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalDynamicAdminLabelRangeStart_Object = MibScalar
cienaCesMplsGlobalDynamicAdminLabelRangeStart = _CienaCesMplsGlobalDynamicAdminLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 5),
    _CienaCesMplsGlobalDynamicAdminLabelRangeStart_Type()
)
cienaCesMplsGlobalDynamicAdminLabelRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalDynamicAdminLabelRangeStart.setStatus("current")


class _CienaCesMplsGlobalDynamicAdminLabelRangeEnd_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalDynamicAdminLabelRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalDynamicAdminLabelRangeEnd_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalDynamicAdminLabelRangeEnd_Object = MibScalar
cienaCesMplsGlobalDynamicAdminLabelRangeEnd = _CienaCesMplsGlobalDynamicAdminLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 6),
    _CienaCesMplsGlobalDynamicAdminLabelRangeEnd_Type()
)
cienaCesMplsGlobalDynamicAdminLabelRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalDynamicAdminLabelRangeEnd.setStatus("current")


class _CienaCesMplsGlobalDynamicOperLabelRangeStart_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalDynamicOperLabelRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalDynamicOperLabelRangeStart_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalDynamicOperLabelRangeStart_Object = MibScalar
cienaCesMplsGlobalDynamicOperLabelRangeStart = _CienaCesMplsGlobalDynamicOperLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 7),
    _CienaCesMplsGlobalDynamicOperLabelRangeStart_Type()
)
cienaCesMplsGlobalDynamicOperLabelRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalDynamicOperLabelRangeStart.setStatus("current")


class _CienaCesMplsGlobalDynamicOperLabelRangeEnd_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalDynamicOperLabelRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalDynamicOperLabelRangeEnd_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalDynamicOperLabelRangeEnd_Object = MibScalar
cienaCesMplsGlobalDynamicOperLabelRangeEnd = _CienaCesMplsGlobalDynamicOperLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 8),
    _CienaCesMplsGlobalDynamicOperLabelRangeEnd_Type()
)
cienaCesMplsGlobalDynamicOperLabelRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalDynamicOperLabelRangeEnd.setStatus("current")


class _CienaCesMplsGlobalStaticAdminTunnelLabelRangeStart_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalStaticAdminTunnelLabelRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalStaticAdminTunnelLabelRangeStart_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalStaticAdminTunnelLabelRangeStart_Object = MibScalar
cienaCesMplsGlobalStaticAdminTunnelLabelRangeStart = _CienaCesMplsGlobalStaticAdminTunnelLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 9),
    _CienaCesMplsGlobalStaticAdminTunnelLabelRangeStart_Type()
)
cienaCesMplsGlobalStaticAdminTunnelLabelRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalStaticAdminTunnelLabelRangeStart.setStatus("current")


class _CienaCesMplsGlobalStaticAdminTunnelLabelRangeEnd_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalStaticAdminTunnelLabelRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalStaticAdminTunnelLabelRangeEnd_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalStaticAdminTunnelLabelRangeEnd_Object = MibScalar
cienaCesMplsGlobalStaticAdminTunnelLabelRangeEnd = _CienaCesMplsGlobalStaticAdminTunnelLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 10),
    _CienaCesMplsGlobalStaticAdminTunnelLabelRangeEnd_Type()
)
cienaCesMplsGlobalStaticAdminTunnelLabelRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalStaticAdminTunnelLabelRangeEnd.setStatus("current")


class _CienaCesMplsGlobalStaticOperTunnelLabelRangeStart_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalStaticOperTunnelLabelRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalStaticOperTunnelLabelRangeStart_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalStaticOperTunnelLabelRangeStart_Object = MibScalar
cienaCesMplsGlobalStaticOperTunnelLabelRangeStart = _CienaCesMplsGlobalStaticOperTunnelLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 11),
    _CienaCesMplsGlobalStaticOperTunnelLabelRangeStart_Type()
)
cienaCesMplsGlobalStaticOperTunnelLabelRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalStaticOperTunnelLabelRangeStart.setStatus("current")


class _CienaCesMplsGlobalStaticOperTunnelLabelRangeEnd_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalStaticOperTunnelLabelRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalStaticOperTunnelLabelRangeEnd_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalStaticOperTunnelLabelRangeEnd_Object = MibScalar
cienaCesMplsGlobalStaticOperTunnelLabelRangeEnd = _CienaCesMplsGlobalStaticOperTunnelLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 12),
    _CienaCesMplsGlobalStaticOperTunnelLabelRangeEnd_Type()
)
cienaCesMplsGlobalStaticOperTunnelLabelRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalStaticOperTunnelLabelRangeEnd.setStatus("current")


class _CienaCesMplsGlobalStaticAdminVcLabelRangeStart_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalStaticAdminVcLabelRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalStaticAdminVcLabelRangeStart_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalStaticAdminVcLabelRangeStart_Object = MibScalar
cienaCesMplsGlobalStaticAdminVcLabelRangeStart = _CienaCesMplsGlobalStaticAdminVcLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 13),
    _CienaCesMplsGlobalStaticAdminVcLabelRangeStart_Type()
)
cienaCesMplsGlobalStaticAdminVcLabelRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalStaticAdminVcLabelRangeStart.setStatus("current")


class _CienaCesMplsGlobalStaticAdminVcLabelRangeEnd_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalStaticAdminVcLabelRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalStaticAdminVcLabelRangeEnd_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalStaticAdminVcLabelRangeEnd_Object = MibScalar
cienaCesMplsGlobalStaticAdminVcLabelRangeEnd = _CienaCesMplsGlobalStaticAdminVcLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 14),
    _CienaCesMplsGlobalStaticAdminVcLabelRangeEnd_Type()
)
cienaCesMplsGlobalStaticAdminVcLabelRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalStaticAdminVcLabelRangeEnd.setStatus("current")


class _CienaCesMplsGlobalStaticOperVcLabelRangeStart_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalStaticOperVcLabelRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalStaticOperVcLabelRangeStart_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalStaticOperVcLabelRangeStart_Object = MibScalar
cienaCesMplsGlobalStaticOperVcLabelRangeStart = _CienaCesMplsGlobalStaticOperVcLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 15),
    _CienaCesMplsGlobalStaticOperVcLabelRangeStart_Type()
)
cienaCesMplsGlobalStaticOperVcLabelRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalStaticOperVcLabelRangeStart.setStatus("current")


class _CienaCesMplsGlobalStaticOperVcLabelRangeEnd_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalStaticOperVcLabelRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalStaticOperVcLabelRangeEnd_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalStaticOperVcLabelRangeEnd_Object = MibScalar
cienaCesMplsGlobalStaticOperVcLabelRangeEnd = _CienaCesMplsGlobalStaticOperVcLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 16),
    _CienaCesMplsGlobalStaticOperVcLabelRangeEnd_Type()
)
cienaCesMplsGlobalStaticOperVcLabelRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalStaticOperVcLabelRangeEnd.setStatus("current")


class _CienaCesMplsGlobalNextFreeStaticVcLabel_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalNextFreeStaticVcLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalNextFreeStaticVcLabel_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalNextFreeStaticVcLabel_Object = MibScalar
cienaCesMplsGlobalNextFreeStaticVcLabel = _CienaCesMplsGlobalNextFreeStaticVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 1, 17),
    _CienaCesMplsGlobalNextFreeStaticVcLabel_Type()
)
cienaCesMplsGlobalNextFreeStaticVcLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalNextFreeStaticVcLabel.setStatus("current")
_CienaCesMplsTunnelCosProfileTable_Object = MibTable
cienaCesMplsTunnelCosProfileTable = _CienaCesMplsTunnelCosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cienaCesMplsTunnelCosProfileTable.setStatus("current")
_CienaCesMplsTunnelCosProfileEntry_Object = MibTableRow
cienaCesMplsTunnelCosProfileEntry = _CienaCesMplsTunnelCosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2, 1)
)
cienaCesMplsTunnelCosProfileEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsTunnelCosProfileIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsTunnelCosProfileEntry.setStatus("current")
_CienaCesMplsTunnelCosProfileIndex_Type = Unsigned32
_CienaCesMplsTunnelCosProfileIndex_Object = MibTableColumn
cienaCesMplsTunnelCosProfileIndex = _CienaCesMplsTunnelCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2, 1, 1),
    _CienaCesMplsTunnelCosProfileIndex_Type()
)
cienaCesMplsTunnelCosProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelCosProfileIndex.setStatus("current")
_CienaCesMplsTunnelCosProfileName_Type = DisplayString
_CienaCesMplsTunnelCosProfileName_Object = MibTableColumn
cienaCesMplsTunnelCosProfileName = _CienaCesMplsTunnelCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2, 1, 2),
    _CienaCesMplsTunnelCosProfileName_Type()
)
cienaCesMplsTunnelCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelCosProfileName.setStatus("current")


class _CienaCesMplsTunnelFrmCosPolicy_Type(FCosPolicy):
    """Custom type cienaCesMplsTunnelFrmCosPolicy based on FCosPolicy"""


_CienaCesMplsTunnelFrmCosPolicy_Object = MibTableColumn
cienaCesMplsTunnelFrmCosPolicy = _CienaCesMplsTunnelFrmCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2, 1, 3),
    _CienaCesMplsTunnelFrmCosPolicy_Type()
)
cienaCesMplsTunnelFrmCosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelFrmCosPolicy.setStatus("current")


class _CienaCesMplsTunnelFrmCosMapId_Type(Integer32):
    """Custom type cienaCesMplsTunnelFrmCosMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsTunnelFrmCosMapId_Type.__name__ = "Integer32"
_CienaCesMplsTunnelFrmCosMapId_Object = MibTableColumn
cienaCesMplsTunnelFrmCosMapId = _CienaCesMplsTunnelFrmCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2, 1, 4),
    _CienaCesMplsTunnelFrmCosMapId_Type()
)
cienaCesMplsTunnelFrmCosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelFrmCosMapId.setStatus("current")
_CienaCesMplsTunnelFrmCosMapName_Type = DisplayString
_CienaCesMplsTunnelFrmCosMapName_Object = MibTableColumn
cienaCesMplsTunnelFrmCosMapName = _CienaCesMplsTunnelFrmCosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2, 1, 5),
    _CienaCesMplsTunnelFrmCosMapName_Type()
)
cienaCesMplsTunnelFrmCosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelFrmCosMapName.setStatus("current")


class _CienaCesMplsTunnelFixedTC_Type(Unsigned32):
    """Custom type cienaCesMplsTunnelFixedTC based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMplsTunnelFixedTC_Type.__name__ = "Unsigned32"
_CienaCesMplsTunnelFixedTC_Object = MibTableColumn
cienaCesMplsTunnelFixedTC = _CienaCesMplsTunnelFixedTC_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2, 1, 6),
    _CienaCesMplsTunnelFixedTC_Type()
)
cienaCesMplsTunnelFixedTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelFixedTC.setStatus("current")


class _CienaCesMplsTunnelRcosPolicy_Type(RCosPolicy):
    """Custom type cienaCesMplsTunnelRcosPolicy based on RCosPolicy"""


_CienaCesMplsTunnelRcosPolicy_Object = MibTableColumn
cienaCesMplsTunnelRcosPolicy = _CienaCesMplsTunnelRcosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2, 1, 7),
    _CienaCesMplsTunnelRcosPolicy_Type()
)
cienaCesMplsTunnelRcosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelRcosPolicy.setStatus("current")
_CienaCesMplsTunnelRcosMapName_Type = DisplayString
_CienaCesMplsTunnelRcosMapName_Object = MibTableColumn
cienaCesMplsTunnelRcosMapName = _CienaCesMplsTunnelRcosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2, 1, 8),
    _CienaCesMplsTunnelRcosMapName_Type()
)
cienaCesMplsTunnelRcosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelRcosMapName.setStatus("current")


class _CienaCesMplsTunnelRCosMapId_Type(Integer32):
    """Custom type cienaCesMplsTunnelRCosMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsTunnelRCosMapId_Type.__name__ = "Integer32"
_CienaCesMplsTunnelRCosMapId_Object = MibTableColumn
cienaCesMplsTunnelRCosMapId = _CienaCesMplsTunnelRCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2, 1, 9),
    _CienaCesMplsTunnelRCosMapId_Type()
)
cienaCesMplsTunnelRCosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelRCosMapId.setStatus("current")
_CienaCesMplsTunnelRcosProfileName_Type = DisplayString
_CienaCesMplsTunnelRcosProfileName_Object = MibTableColumn
cienaCesMplsTunnelRcosProfileName = _CienaCesMplsTunnelRcosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2, 1, 10),
    _CienaCesMplsTunnelRcosProfileName_Type()
)
cienaCesMplsTunnelRcosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelRcosProfileName.setStatus("current")


class _CienaCesMplsTunnelRCosProfileId_Type(Unsigned32):
    """Custom type cienaCesMplsTunnelRCosProfileId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsTunnelRCosProfileId_Type.__name__ = "Unsigned32"
_CienaCesMplsTunnelRCosProfileId_Object = MibTableColumn
cienaCesMplsTunnelRCosProfileId = _CienaCesMplsTunnelRCosProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 2, 1, 11),
    _CienaCesMplsTunnelRCosProfileId_Type()
)
cienaCesMplsTunnelRCosProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsTunnelRCosProfileId.setStatus("current")
_CienaCesMplsGlobalTunnelPath_ObjectIdentity = ObjectIdentity
cienaCesMplsGlobalTunnelPath = _CienaCesMplsGlobalTunnelPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 3)
)
_CienaCesMplsGlobalTunnelPathTable_Object = MibTable
cienaCesMplsGlobalTunnelPathTable = _CienaCesMplsGlobalTunnelPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cienaCesMplsGlobalTunnelPathTable.setStatus("current")
_CienaCesMplsGlobalTunnelPathEntry_Object = MibTableRow
cienaCesMplsGlobalTunnelPathEntry = _CienaCesMplsGlobalTunnelPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 3, 1, 1)
)
cienaCesMplsGlobalTunnelPathEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsGlobalTunnelPathIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsGlobalTunnelPathEntry.setStatus("current")
_CienaCesMplsGlobalTunnelPathIndex_Type = Unsigned32
_CienaCesMplsGlobalTunnelPathIndex_Object = MibTableColumn
cienaCesMplsGlobalTunnelPathIndex = _CienaCesMplsGlobalTunnelPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 3, 1, 1, 1),
    _CienaCesMplsGlobalTunnelPathIndex_Type()
)
cienaCesMplsGlobalTunnelPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalTunnelPathIndex.setStatus("current")


class _CienaCesMplsGlobalTunnelPathName_Type(DisplayString):
    """Custom type cienaCesMplsGlobalTunnelPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsGlobalTunnelPathName_Type.__name__ = "DisplayString"
_CienaCesMplsGlobalTunnelPathName_Object = MibTableColumn
cienaCesMplsGlobalTunnelPathName = _CienaCesMplsGlobalTunnelPathName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 3, 1, 1, 2),
    _CienaCesMplsGlobalTunnelPathName_Type()
)
cienaCesMplsGlobalTunnelPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalTunnelPathName.setStatus("current")
_CienaCesMplsGlobalTunnelPathUseCount_Type = Counter32
_CienaCesMplsGlobalTunnelPathUseCount_Object = MibTableColumn
cienaCesMplsGlobalTunnelPathUseCount = _CienaCesMplsGlobalTunnelPathUseCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 3, 1, 1, 3),
    _CienaCesMplsGlobalTunnelPathUseCount_Type()
)
cienaCesMplsGlobalTunnelPathUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalTunnelPathUseCount.setStatus("current")
_CienaCesMplsGlobalTunnelPathHopTable_Object = MibTable
cienaCesMplsGlobalTunnelPathHopTable = _CienaCesMplsGlobalTunnelPathHopTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    cienaCesMplsGlobalTunnelPathHopTable.setStatus("current")
_CienaCesMplsGlobalTunnelPathHopEntry_Object = MibTableRow
cienaCesMplsGlobalTunnelPathHopEntry = _CienaCesMplsGlobalTunnelPathHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 3, 2, 1)
)
cienaCesMplsGlobalTunnelPathHopEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsGlobalTunnelPathIndex"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsGlobalTunnelPathHopIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsGlobalTunnelPathHopEntry.setStatus("current")
_CienaCesMplsGlobalTunnelPathHopIndex_Type = Unsigned32
_CienaCesMplsGlobalTunnelPathHopIndex_Object = MibTableColumn
cienaCesMplsGlobalTunnelPathHopIndex = _CienaCesMplsGlobalTunnelPathHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 3, 2, 1, 1),
    _CienaCesMplsGlobalTunnelPathHopIndex_Type()
)
cienaCesMplsGlobalTunnelPathHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalTunnelPathHopIndex.setStatus("current")
_CienaCesMplsGlobalTunnelPathHopIpAddr_Type = IpAddress
_CienaCesMplsGlobalTunnelPathHopIpAddr_Object = MibTableColumn
cienaCesMplsGlobalTunnelPathHopIpAddr = _CienaCesMplsGlobalTunnelPathHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 3, 2, 1, 2),
    _CienaCesMplsGlobalTunnelPathHopIpAddr_Type()
)
cienaCesMplsGlobalTunnelPathHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalTunnelPathHopIpAddr.setStatus("current")


class _CienaCesMplsGlobalTunnelPathHopType_Type(Integer32):
    """Custom type cienaCesMplsGlobalTunnelPathHopType based on Integer32"""
    defaultValue = 1

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


_CienaCesMplsGlobalTunnelPathHopType_Type.__name__ = "Integer32"
_CienaCesMplsGlobalTunnelPathHopType_Object = MibTableColumn
cienaCesMplsGlobalTunnelPathHopType = _CienaCesMplsGlobalTunnelPathHopType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 3, 2, 1, 3),
    _CienaCesMplsGlobalTunnelPathHopType_Type()
)
cienaCesMplsGlobalTunnelPathHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalTunnelPathHopType.setStatus("current")
_CienaCesMplsGlobalFreeStaticTunnelLabelTable_Object = MibTable
cienaCesMplsGlobalFreeStaticTunnelLabelTable = _CienaCesMplsGlobalFreeStaticTunnelLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cienaCesMplsGlobalFreeStaticTunnelLabelTable.setStatus("current")
_CienaCesMplsGlobalFreeStaticTunnelLabelEntry_Object = MibTableRow
cienaCesMplsGlobalFreeStaticTunnelLabelEntry = _CienaCesMplsGlobalFreeStaticTunnelLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 4, 1)
)
cienaCesMplsGlobalFreeStaticTunnelLabelEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsGlobalFreeStaticTunnelLabelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsGlobalFreeStaticTunnelLabelEntry.setStatus("current")


class _CienaCesMplsGlobalFreeStaticTunnelLabelIndex_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalFreeStaticTunnelLabelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsGlobalFreeStaticTunnelLabelIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalFreeStaticTunnelLabelIndex_Object = MibTableColumn
cienaCesMplsGlobalFreeStaticTunnelLabelIndex = _CienaCesMplsGlobalFreeStaticTunnelLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 4, 1, 1),
    _CienaCesMplsGlobalFreeStaticTunnelLabelIndex_Type()
)
cienaCesMplsGlobalFreeStaticTunnelLabelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalFreeStaticTunnelLabelIndex.setStatus("current")


class _CienaCesMplsGlobalFreeStaticTunnelLabel_Type(Unsigned32):
    """Custom type cienaCesMplsGlobalFreeStaticTunnelLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_CienaCesMplsGlobalFreeStaticTunnelLabel_Type.__name__ = "Unsigned32"
_CienaCesMplsGlobalFreeStaticTunnelLabel_Object = MibTableColumn
cienaCesMplsGlobalFreeStaticTunnelLabel = _CienaCesMplsGlobalFreeStaticTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 3, 4, 1, 2),
    _CienaCesMplsGlobalFreeStaticTunnelLabel_Type()
)
cienaCesMplsGlobalFreeStaticTunnelLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsGlobalFreeStaticTunnelLabel.setStatus("current")
_CienaCesMplsPw_ObjectIdentity = ObjectIdentity
cienaCesMplsPw = _CienaCesMplsPw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4)
)
_CienaCesMplsPwTable_Object = MibTable
cienaCesMplsPwTable = _CienaCesMplsPwTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cienaCesMplsPwTable.setStatus("current")
_CienaCesMplsPwEntry_Object = MibTableRow
cienaCesMplsPwEntry = _CienaCesMplsPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1)
)
cienaCesMplsPwEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsPwIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsPwEntry.setStatus("current")


class _CienaCesMplsPwIndex_Type(Unsigned32):
    """Custom type cienaCesMplsPwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsPwIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsPwIndex_Object = MibTableColumn
cienaCesMplsPwIndex = _CienaCesMplsPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 1),
    _CienaCesMplsPwIndex_Type()
)
cienaCesMplsPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsPwIndex.setStatus("current")


class _CienaCesMplsPwSignallingType_Type(Integer32):
    """Custom type cienaCesMplsPwSignallingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CienaCesMplsPwSignallingType_Type.__name__ = "Integer32"
_CienaCesMplsPwSignallingType_Object = MibTableColumn
cienaCesMplsPwSignallingType = _CienaCesMplsPwSignallingType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 2),
    _CienaCesMplsPwSignallingType_Type()
)
cienaCesMplsPwSignallingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwSignallingType.setStatus("current")


class _CienaCesMplsPwId_Type(Unsigned32):
    """Custom type cienaCesMplsPwId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CienaCesMplsPwId_Type.__name__ = "Unsigned32"
_CienaCesMplsPwId_Object = MibTableColumn
cienaCesMplsPwId = _CienaCesMplsPwId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 3),
    _CienaCesMplsPwId_Type()
)
cienaCesMplsPwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwId.setStatus("current")


class _CienaCesMplsPwName_Type(DisplayString):
    """Custom type cienaCesMplsPwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsPwName_Type.__name__ = "DisplayString"
_CienaCesMplsPwName_Object = MibTableColumn
cienaCesMplsPwName = _CienaCesMplsPwName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 4),
    _CienaCesMplsPwName_Type()
)
cienaCesMplsPwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwName.setStatus("current")


class _CienaCesMplsPwCustomerName_Type(DisplayString):
    """Custom type cienaCesMplsPwCustomerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsPwCustomerName_Type.__name__ = "DisplayString"
_CienaCesMplsPwCustomerName_Object = MibTableColumn
cienaCesMplsPwCustomerName = _CienaCesMplsPwCustomerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 5),
    _CienaCesMplsPwCustomerName_Type()
)
cienaCesMplsPwCustomerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCustomerName.setStatus("current")
_CienaCesMplsPwAdminState_Type = CienaGlobalState
_CienaCesMplsPwAdminState_Object = MibTableColumn
cienaCesMplsPwAdminState = _CienaCesMplsPwAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 6),
    _CienaCesMplsPwAdminState_Type()
)
cienaCesMplsPwAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwAdminState.setStatus("current")
_CienaCesMplsPwOperState_Type = CienaGlobalState
_CienaCesMplsPwOperState_Object = MibTableColumn
cienaCesMplsPwOperState = _CienaCesMplsPwOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 7),
    _CienaCesMplsPwOperState_Type()
)
cienaCesMplsPwOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwOperState.setStatus("current")
_CienaCesMplsPwPeerIpAddr_Type = IpAddress
_CienaCesMplsPwPeerIpAddr_Object = MibTableColumn
cienaCesMplsPwPeerIpAddr = _CienaCesMplsPwPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 8),
    _CienaCesMplsPwPeerIpAddr_Type()
)
cienaCesMplsPwPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwPeerIpAddr.setStatus("current")


class _CienaCesMplsPwInLabel_Type(Integer32):
    """Custom type cienaCesMplsPwInLabel based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1048575),
    )


_CienaCesMplsPwInLabel_Type.__name__ = "Integer32"
_CienaCesMplsPwInLabel_Object = MibTableColumn
cienaCesMplsPwInLabel = _CienaCesMplsPwInLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 9),
    _CienaCesMplsPwInLabel_Type()
)
cienaCesMplsPwInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwInLabel.setStatus("current")


class _CienaCesMplsPwOutLabel_Type(Integer32):
    """Custom type cienaCesMplsPwOutLabel based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1048575),
    )


_CienaCesMplsPwOutLabel_Type.__name__ = "Integer32"
_CienaCesMplsPwOutLabel_Object = MibTableColumn
cienaCesMplsPwOutLabel = _CienaCesMplsPwOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 10),
    _CienaCesMplsPwOutLabel_Type()
)
cienaCesMplsPwOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwOutLabel.setStatus("current")


class _CienaCesMplsPwStatusTlv_Type(Integer32):
    """Custom type cienaCesMplsPwStatusTlv based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesMplsPwStatusTlv_Type.__name__ = "Integer32"
_CienaCesMplsPwStatusTlv_Object = MibTableColumn
cienaCesMplsPwStatusTlv = _CienaCesMplsPwStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 11),
    _CienaCesMplsPwStatusTlv_Type()
)
cienaCesMplsPwStatusTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwStatusTlv.setStatus("current")


class _CienaCesMplsPwRefreshStatusIntvl_Type(Unsigned32):
    """Custom type cienaCesMplsPwRefreshStatusIntvl based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CienaCesMplsPwRefreshStatusIntvl_Type.__name__ = "Unsigned32"
_CienaCesMplsPwRefreshStatusIntvl_Object = MibTableColumn
cienaCesMplsPwRefreshStatusIntvl = _CienaCesMplsPwRefreshStatusIntvl_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 12),
    _CienaCesMplsPwRefreshStatusIntvl_Type()
)
cienaCesMplsPwRefreshStatusIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwRefreshStatusIntvl.setStatus("current")
_CienaCesMplsPwLocalFault_Type = VCStatus
_CienaCesMplsPwLocalFault_Object = MibTableColumn
cienaCesMplsPwLocalFault = _CienaCesMplsPwLocalFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 13),
    _CienaCesMplsPwLocalFault_Type()
)
cienaCesMplsPwLocalFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwLocalFault.setStatus("current")
_CienaCesMplsPwRemoteFault_Type = VCStatus
_CienaCesMplsPwRemoteFault_Object = MibTableColumn
cienaCesMplsPwRemoteFault = _CienaCesMplsPwRemoteFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 14),
    _CienaCesMplsPwRemoteFault_Type()
)
cienaCesMplsPwRemoteFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwRemoteFault.setStatus("current")


class _CienaCesMplsPwMtu_Type(Unsigned32):
    """Custom type cienaCesMplsPwMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 9128),
    )


_CienaCesMplsPwMtu_Type.__name__ = "Unsigned32"
_CienaCesMplsPwMtu_Object = MibTableColumn
cienaCesMplsPwMtu = _CienaCesMplsPwMtu_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 15),
    _CienaCesMplsPwMtu_Type()
)
cienaCesMplsPwMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwMtu.setStatus("current")


class _CienaCesMplsPwType_Type(Integer32):
    """Custom type cienaCesMplsPwType based on Integer32"""
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
        *(("raw", 1),
          ("tagged", 2),
          ("tdm", 3))
    )


_CienaCesMplsPwType_Type.__name__ = "Integer32"
_CienaCesMplsPwType_Object = MibTableColumn
cienaCesMplsPwType = _CienaCesMplsPwType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 16),
    _CienaCesMplsPwType_Type()
)
cienaCesMplsPwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwType.setStatus("current")


class _CienaCesMplsPwMode_Type(Integer32):
    """Custom type cienaCesMplsPwMode based on Integer32"""
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
        *(("mesh", 1),
          ("spoke", 2),
          ("switching", 3))
    )


_CienaCesMplsPwMode_Type.__name__ = "Integer32"
_CienaCesMplsPwMode_Object = MibTableColumn
cienaCesMplsPwMode = _CienaCesMplsPwMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 17),
    _CienaCesMplsPwMode_Type()
)
cienaCesMplsPwMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwMode.setStatus("current")


class _CienaCesMplsPwCoSProfileName_Type(DisplayString):
    """Custom type cienaCesMplsPwCoSProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsPwCoSProfileName_Type.__name__ = "DisplayString"
_CienaCesMplsPwCoSProfileName_Object = MibTableColumn
cienaCesMplsPwCoSProfileName = _CienaCesMplsPwCoSProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 18),
    _CienaCesMplsPwCoSProfileName_Type()
)
cienaCesMplsPwCoSProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCoSProfileName.setStatus("current")


class _CienaCesMplsPwCoSProfileIndex_Type(Unsigned32):
    """Custom type cienaCesMplsPwCoSProfileIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsPwCoSProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsPwCoSProfileIndex_Object = MibTableColumn
cienaCesMplsPwCoSProfileIndex = _CienaCesMplsPwCoSProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 19),
    _CienaCesMplsPwCoSProfileIndex_Type()
)
cienaCesMplsPwCoSProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCoSProfileIndex.setStatus("current")
_CienaCesMplsPwEgressL2PtTransform_Type = CienaGlobalState
_CienaCesMplsPwEgressL2PtTransform_Object = MibTableColumn
cienaCesMplsPwEgressL2PtTransform = _CienaCesMplsPwEgressL2PtTransform_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 20),
    _CienaCesMplsPwEgressL2PtTransform_Type()
)
cienaCesMplsPwEgressL2PtTransform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwEgressL2PtTransform.setStatus("current")


class _CienaCesMplsPwVccVProfileName_Type(DisplayString):
    """Custom type cienaCesMplsPwVccVProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsPwVccVProfileName_Type.__name__ = "DisplayString"
_CienaCesMplsPwVccVProfileName_Object = MibTableColumn
cienaCesMplsPwVccVProfileName = _CienaCesMplsPwVccVProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 21),
    _CienaCesMplsPwVccVProfileName_Type()
)
cienaCesMplsPwVccVProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwVccVProfileName.setStatus("current")


class _CienaCesMplsPwVccVProfileIndex_Type(Unsigned32):
    """Custom type cienaCesMplsPwVccVProfileIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsPwVccVProfileIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsPwVccVProfileIndex_Object = MibTableColumn
cienaCesMplsPwVccVProfileIndex = _CienaCesMplsPwVccVProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 22),
    _CienaCesMplsPwVccVProfileIndex_Type()
)
cienaCesMplsPwVccVProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwVccVProfileIndex.setStatus("current")


class _CienaCesMplsPwLocalCcCv_Type(DisplayString):
    """Custom type cienaCesMplsPwLocalCcCv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsPwLocalCcCv_Type.__name__ = "DisplayString"
_CienaCesMplsPwLocalCcCv_Object = MibTableColumn
cienaCesMplsPwLocalCcCv = _CienaCesMplsPwLocalCcCv_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 23),
    _CienaCesMplsPwLocalCcCv_Type()
)
cienaCesMplsPwLocalCcCv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwLocalCcCv.setStatus("current")


class _CienaCesMplsPwRemoteCcCv_Type(DisplayString):
    """Custom type cienaCesMplsPwRemoteCcCv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsPwRemoteCcCv_Type.__name__ = "DisplayString"
_CienaCesMplsPwRemoteCcCv_Object = MibTableColumn
cienaCesMplsPwRemoteCcCv = _CienaCesMplsPwRemoteCcCv_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 24),
    _CienaCesMplsPwRemoteCcCv_Type()
)
cienaCesMplsPwRemoteCcCv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwRemoteCcCv.setStatus("current")


class _CienaCesMplsPwOperatingCcCv_Type(DisplayString):
    """Custom type cienaCesMplsPwOperatingCcCv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsPwOperatingCcCv_Type.__name__ = "DisplayString"
_CienaCesMplsPwOperatingCcCv_Object = MibTableColumn
cienaCesMplsPwOperatingCcCv = _CienaCesMplsPwOperatingCcCv_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 25),
    _CienaCesMplsPwOperatingCcCv_Type()
)
cienaCesMplsPwOperatingCcCv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwOperatingCcCv.setStatus("current")


class _CienaCesMplsPwBlocking_Type(Integer32):
    """Custom type cienaCesMplsPwBlocking based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CienaCesMplsPwBlocking_Type.__name__ = "Integer32"
_CienaCesMplsPwBlocking_Object = MibTableColumn
cienaCesMplsPwBlocking = _CienaCesMplsPwBlocking_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 26),
    _CienaCesMplsPwBlocking_Type()
)
cienaCesMplsPwBlocking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwBlocking.setStatus("current")


class _CienaCesMplsPwVifIndex_Type(Unsigned32):
    """Custom type cienaCesMplsPwVifIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32769, 2147483647),
    )


_CienaCesMplsPwVifIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsPwVifIndex_Object = MibTableColumn
cienaCesMplsPwVifIndex = _CienaCesMplsPwVifIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 27),
    _CienaCesMplsPwVifIndex_Type()
)
cienaCesMplsPwVifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwVifIndex.setStatus("current")


class _CienaCesMplsPwConfigTunnelName_Type(DisplayString):
    """Custom type cienaCesMplsPwConfigTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsPwConfigTunnelName_Type.__name__ = "DisplayString"
_CienaCesMplsPwConfigTunnelName_Object = MibTableColumn
cienaCesMplsPwConfigTunnelName = _CienaCesMplsPwConfigTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 28),
    _CienaCesMplsPwConfigTunnelName_Type()
)
cienaCesMplsPwConfigTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwConfigTunnelName.setStatus("current")
_CienaCesMplsPwConfigTunnelType_Type = TunnelType
_CienaCesMplsPwConfigTunnelType_Object = MibTableColumn
cienaCesMplsPwConfigTunnelType = _CienaCesMplsPwConfigTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 29),
    _CienaCesMplsPwConfigTunnelType_Type()
)
cienaCesMplsPwConfigTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwConfigTunnelType.setStatus("current")


class _CienaCesMplsPwConfigTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesMplsPwConfigTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsPwConfigTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsPwConfigTunnelIndex_Object = MibTableColumn
cienaCesMplsPwConfigTunnelIndex = _CienaCesMplsPwConfigTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 30),
    _CienaCesMplsPwConfigTunnelIndex_Type()
)
cienaCesMplsPwConfigTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwConfigTunnelIndex.setStatus("current")


class _CienaCesMplsPwActiveTunnelName_Type(DisplayString):
    """Custom type cienaCesMplsPwActiveTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsPwActiveTunnelName_Type.__name__ = "DisplayString"
_CienaCesMplsPwActiveTunnelName_Object = MibTableColumn
cienaCesMplsPwActiveTunnelName = _CienaCesMplsPwActiveTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 31),
    _CienaCesMplsPwActiveTunnelName_Type()
)
cienaCesMplsPwActiveTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwActiveTunnelName.setStatus("current")
_CienaCesMplsPwActiveTunnelType_Type = TunnelType
_CienaCesMplsPwActiveTunnelType_Object = MibTableColumn
cienaCesMplsPwActiveTunnelType = _CienaCesMplsPwActiveTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 32),
    _CienaCesMplsPwActiveTunnelType_Type()
)
cienaCesMplsPwActiveTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwActiveTunnelType.setStatus("current")


class _CienaCesMplsPwActiveTunnelIndex_Type(Unsigned32):
    """Custom type cienaCesMplsPwActiveTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsPwActiveTunnelIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsPwActiveTunnelIndex_Object = MibTableColumn
cienaCesMplsPwActiveTunnelIndex = _CienaCesMplsPwActiveTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 33),
    _CienaCesMplsPwActiveTunnelIndex_Type()
)
cienaCesMplsPwActiveTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwActiveTunnelIndex.setStatus("current")


class _CienaCesMplsPwRole_Type(Integer32):
    """Custom type cienaCesMplsPwRole based on Integer32"""
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
        *(("primary", 1),
          ("secondary", 2),
          ("stand-alone", 3))
    )


_CienaCesMplsPwRole_Type.__name__ = "Integer32"
_CienaCesMplsPwRole_Object = MibTableColumn
cienaCesMplsPwRole = _CienaCesMplsPwRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 34),
    _CienaCesMplsPwRole_Type()
)
cienaCesMplsPwRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwRole.setStatus("deprecated")


class _CienaCesMplsPwPrimaryPwName_Type(DisplayString):
    """Custom type cienaCesMplsPwPrimaryPwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsPwPrimaryPwName_Type.__name__ = "DisplayString"
_CienaCesMplsPwPrimaryPwName_Object = MibTableColumn
cienaCesMplsPwPrimaryPwName = _CienaCesMplsPwPrimaryPwName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 35),
    _CienaCesMplsPwPrimaryPwName_Type()
)
cienaCesMplsPwPrimaryPwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwPrimaryPwName.setStatus("current")


class _CienaCesMplsPwPrimaryPwIndex_Type(Unsigned32):
    """Custom type cienaCesMplsPwPrimaryPwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsPwPrimaryPwIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsPwPrimaryPwIndex_Object = MibTableColumn
cienaCesMplsPwPrimaryPwIndex = _CienaCesMplsPwPrimaryPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 36),
    _CienaCesMplsPwPrimaryPwIndex_Type()
)
cienaCesMplsPwPrimaryPwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwPrimaryPwIndex.setStatus("current")


class _CienaCesMplsPwVsIndex_Type(Unsigned32):
    """Custom type cienaCesMplsPwVsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsPwVsIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsPwVsIndex_Object = MibTableColumn
cienaCesMplsPwVsIndex = _CienaCesMplsPwVsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 37),
    _CienaCesMplsPwVsIndex_Type()
)
cienaCesMplsPwVsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwVsIndex.setStatus("current")


class _CienaCesServiceDelimiterVID_Type(Unsigned32):
    """Custom type cienaCesServiceDelimiterVID based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CienaCesServiceDelimiterVID_Type.__name__ = "Unsigned32"
_CienaCesServiceDelimiterVID_Object = MibTableColumn
cienaCesServiceDelimiterVID = _CienaCesServiceDelimiterVID_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 38),
    _CienaCesServiceDelimiterVID_Type()
)
cienaCesServiceDelimiterVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesServiceDelimiterVID.setStatus("deprecated")
_CienaCesServiceDelimiterTPID_Type = Unsigned32
_CienaCesServiceDelimiterTPID_Object = MibTableColumn
cienaCesServiceDelimiterTPID = _CienaCesServiceDelimiterTPID_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 39),
    _CienaCesServiceDelimiterTPID_Type()
)
cienaCesServiceDelimiterTPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesServiceDelimiterTPID.setStatus("deprecated")


class _CienaCesMplsPwReversion_Type(Integer32):
    """Custom type cienaCesMplsPwReversion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesMplsPwReversion_Type.__name__ = "Integer32"
_CienaCesMplsPwReversion_Object = MibTableColumn
cienaCesMplsPwReversion = _CienaCesMplsPwReversion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 40),
    _CienaCesMplsPwReversion_Type()
)
cienaCesMplsPwReversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwReversion.setStatus("current")


class _CienaCesMplsPwRevertTime_Type(Unsigned32):
    """Custom type cienaCesMplsPwRevertTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CienaCesMplsPwRevertTime_Type.__name__ = "Unsigned32"
_CienaCesMplsPwRevertTime_Object = MibTableColumn
cienaCesMplsPwRevertTime = _CienaCesMplsPwRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 41),
    _CienaCesMplsPwRevertTime_Type()
)
cienaCesMplsPwRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwRevertTime.setStatus("current")


class _CienaCesMplsPwProtectionRole_Type(Integer32):
    """Custom type cienaCesMplsPwProtectionRole based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup-pseudowire", 2),
          ("primary-pseudowire", 1),
          ("stand-alone-pseudowire", 3))
    )


_CienaCesMplsPwProtectionRole_Type.__name__ = "Integer32"
_CienaCesMplsPwProtectionRole_Object = MibTableColumn
cienaCesMplsPwProtectionRole = _CienaCesMplsPwProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 42),
    _CienaCesMplsPwProtectionRole_Type()
)
cienaCesMplsPwProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwProtectionRole.setStatus("current")


class _CienaCesMplsPwProtectionState_Type(Integer32):
    """Custom type cienaCesMplsPwProtectionState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("man-swo-active", 4),
          ("man-swo-standby", 5),
          ("not-applicable", 1),
          ("pw-activation-pending", 7),
          ("pw-reversion-pending", 6),
          ("standby", 3))
    )


_CienaCesMplsPwProtectionState_Type.__name__ = "Integer32"
_CienaCesMplsPwProtectionState_Object = MibTableColumn
cienaCesMplsPwProtectionState = _CienaCesMplsPwProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 43),
    _CienaCesMplsPwProtectionState_Type()
)
cienaCesMplsPwProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwProtectionState.setStatus("current")


class _CienaCesMplsPwVsName_Type(DisplayString):
    """Custom type cienaCesMplsPwVsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsPwVsName_Type.__name__ = "DisplayString"
_CienaCesMplsPwVsName_Object = MibTableColumn
cienaCesMplsPwVsName = _CienaCesMplsPwVsName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 44),
    _CienaCesMplsPwVsName_Type()
)
cienaCesMplsPwVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwVsName.setStatus("current")


class _CienaCesMplsPwStatusQuery_Type(Integer32):
    """Custom type cienaCesMplsPwStatusQuery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesMplsPwStatusQuery_Type.__name__ = "Integer32"
_CienaCesMplsPwStatusQuery_Object = MibTableColumn
cienaCesMplsPwStatusQuery = _CienaCesMplsPwStatusQuery_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 45),
    _CienaCesMplsPwStatusQuery_Type()
)
cienaCesMplsPwStatusQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwStatusQuery.setStatus("current")


class _CienaCesMplsMsPwPeerPwName_Type(DisplayString):
    """Custom type cienaCesMplsMsPwPeerPwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesMplsMsPwPeerPwName_Type.__name__ = "DisplayString"
_CienaCesMplsMsPwPeerPwName_Object = MibTableColumn
cienaCesMplsMsPwPeerPwName = _CienaCesMplsMsPwPeerPwName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 46),
    _CienaCesMplsMsPwPeerPwName_Type()
)
cienaCesMplsMsPwPeerPwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsMsPwPeerPwName.setStatus("current")


class _CienaCesMplsMsPwPeerPwIndex_Type(Unsigned32):
    """Custom type cienaCesMplsMsPwPeerPwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsMsPwPeerPwIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsMsPwPeerPwIndex_Object = MibTableColumn
cienaCesMplsMsPwPeerPwIndex = _CienaCesMplsMsPwPeerPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 47),
    _CienaCesMplsMsPwPeerPwIndex_Type()
)
cienaCesMplsMsPwPeerPwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsMsPwPeerPwIndex.setStatus("current")


class _CienaCesMplsPwIdInRemoteFault_Type(Unsigned32):
    """Custom type cienaCesMplsPwIdInRemoteFault based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CienaCesMplsPwIdInRemoteFault_Type.__name__ = "Unsigned32"
_CienaCesMplsPwIdInRemoteFault_Object = MibTableColumn
cienaCesMplsPwIdInRemoteFault = _CienaCesMplsPwIdInRemoteFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 48),
    _CienaCesMplsPwIdInRemoteFault_Type()
)
cienaCesMplsPwIdInRemoteFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwIdInRemoteFault.setStatus("current")
_CienaCesMplsLocalIpInRemoteFault_Type = IpAddress
_CienaCesMplsLocalIpInRemoteFault_Object = MibTableColumn
cienaCesMplsLocalIpInRemoteFault = _CienaCesMplsLocalIpInRemoteFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 49),
    _CienaCesMplsLocalIpInRemoteFault_Type()
)
cienaCesMplsLocalIpInRemoteFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsLocalIpInRemoteFault.setStatus("current")
_CienaCesMplsRemoteIpInRemoteFault_Type = IpAddress
_CienaCesMplsRemoteIpInRemoteFault_Object = MibTableColumn
cienaCesMplsRemoteIpInRemoteFault = _CienaCesMplsRemoteIpInRemoteFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 50),
    _CienaCesMplsRemoteIpInRemoteFault_Type()
)
cienaCesMplsRemoteIpInRemoteFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsRemoteIpInRemoteFault.setStatus("current")
_CienaCesMplsPwFaultToNextHop_Type = VCStatus
_CienaCesMplsPwFaultToNextHop_Object = MibTableColumn
cienaCesMplsPwFaultToNextHop = _CienaCesMplsPwFaultToNextHop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 51),
    _CienaCesMplsPwFaultToNextHop_Type()
)
cienaCesMplsPwFaultToNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwFaultToNextHop.setStatus("current")


class _CienaCesMplsPwIdInFaultToNextHop_Type(Unsigned32):
    """Custom type cienaCesMplsPwIdInFaultToNextHop based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CienaCesMplsPwIdInFaultToNextHop_Type.__name__ = "Unsigned32"
_CienaCesMplsPwIdInFaultToNextHop_Object = MibTableColumn
cienaCesMplsPwIdInFaultToNextHop = _CienaCesMplsPwIdInFaultToNextHop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 52),
    _CienaCesMplsPwIdInFaultToNextHop_Type()
)
cienaCesMplsPwIdInFaultToNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwIdInFaultToNextHop.setStatus("current")
_CienaCesMplsLocalIpInFaultToNextHop_Type = IpAddress
_CienaCesMplsLocalIpInFaultToNextHop_Object = MibTableColumn
cienaCesMplsLocalIpInFaultToNextHop = _CienaCesMplsLocalIpInFaultToNextHop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 53),
    _CienaCesMplsLocalIpInFaultToNextHop_Type()
)
cienaCesMplsLocalIpInFaultToNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsLocalIpInFaultToNextHop.setStatus("current")
_CienaCesMplsRemoteIpInFaultToNextHop_Type = IpAddress
_CienaCesMplsRemoteIpInFaultToNextHop_Object = MibTableColumn
cienaCesMplsRemoteIpInFaultToNextHop = _CienaCesMplsRemoteIpInFaultToNextHop_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 54),
    _CienaCesMplsRemoteIpInFaultToNextHop_Type()
)
cienaCesMplsRemoteIpInFaultToNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsRemoteIpInFaultToNextHop.setStatus("current")


class _CienaCesMplsPwConfigBandwidth_Type(MplsBitRate):
    """Custom type cienaCesMplsPwConfigBandwidth based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_CienaCesMplsPwConfigBandwidth_Type.__name__ = "MplsBitRate"
_CienaCesMplsPwConfigBandwidth_Object = MibTableColumn
cienaCesMplsPwConfigBandwidth = _CienaCesMplsPwConfigBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 55),
    _CienaCesMplsPwConfigBandwidth_Type()
)
cienaCesMplsPwConfigBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwConfigBandwidth.setStatus("current")


class _CienaCesMplsPwOperBandwidth_Type(MplsBitRate):
    """Custom type cienaCesMplsPwOperBandwidth based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_CienaCesMplsPwOperBandwidth_Type.__name__ = "MplsBitRate"
_CienaCesMplsPwOperBandwidth_Object = MibTableColumn
cienaCesMplsPwOperBandwidth = _CienaCesMplsPwOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 56),
    _CienaCesMplsPwOperBandwidth_Type()
)
cienaCesMplsPwOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwOperBandwidth.setStatus("current")


class _CienaCesMplsPwBandwidthState_Type(Integer32):
    """Custom type cienaCesMplsPwBandwidthState based on Integer32"""
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
        *(("acquired", 5),
          ("admitted", 4),
          ("configured", 2),
          ("none", 1),
          ("notRequired", 3),
          ("rejected", 6))
    )


_CienaCesMplsPwBandwidthState_Type.__name__ = "Integer32"
_CienaCesMplsPwBandwidthState_Object = MibTableColumn
cienaCesMplsPwBandwidthState = _CienaCesMplsPwBandwidthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 1, 1, 57),
    _CienaCesMplsPwBandwidthState_Type()
)
cienaCesMplsPwBandwidthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwBandwidthState.setStatus("current")
_CienaCesMplsPwCosProfileTable_Object = MibTable
cienaCesMplsPwCosProfileTable = _CienaCesMplsPwCosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileTable.setStatus("current")
_CienaCesMplsPwCosProfileEntry_Object = MibTableRow
cienaCesMplsPwCosProfileEntry = _CienaCesMplsPwCosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1)
)
cienaCesMplsPwCosProfileEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsPwCosProfileIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileEntry.setStatus("current")
_CienaCesMplsPwCosProfileIndex_Type = Unsigned32
_CienaCesMplsPwCosProfileIndex_Object = MibTableColumn
cienaCesMplsPwCosProfileIndex = _CienaCesMplsPwCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1, 1),
    _CienaCesMplsPwCosProfileIndex_Type()
)
cienaCesMplsPwCosProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileIndex.setStatus("current")
_CienaCesMplsPwCosProfileName_Type = DisplayString
_CienaCesMplsPwCosProfileName_Object = MibTableColumn
cienaCesMplsPwCosProfileName = _CienaCesMplsPwCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1, 2),
    _CienaCesMplsPwCosProfileName_Type()
)
cienaCesMplsPwCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileName.setStatus("current")


class _CienaCesMplsPwCosProfileFrmCosPolicy_Type(FCosPolicy):
    """Custom type cienaCesMplsPwCosProfileFrmCosPolicy based on FCosPolicy"""


_CienaCesMplsPwCosProfileFrmCosPolicy_Object = MibTableColumn
cienaCesMplsPwCosProfileFrmCosPolicy = _CienaCesMplsPwCosProfileFrmCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1, 3),
    _CienaCesMplsPwCosProfileFrmCosPolicy_Type()
)
cienaCesMplsPwCosProfileFrmCosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileFrmCosPolicy.setStatus("current")


class _CienaCesMplsPwCosProfileFrmCosMapId_Type(Unsigned32):
    """Custom type cienaCesMplsPwCosProfileFrmCosMapId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsPwCosProfileFrmCosMapId_Type.__name__ = "Unsigned32"
_CienaCesMplsPwCosProfileFrmCosMapId_Object = MibTableColumn
cienaCesMplsPwCosProfileFrmCosMapId = _CienaCesMplsPwCosProfileFrmCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1, 4),
    _CienaCesMplsPwCosProfileFrmCosMapId_Type()
)
cienaCesMplsPwCosProfileFrmCosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileFrmCosMapId.setStatus("current")
_CienaCesMplsPwCosProfileFrmCosMapName_Type = DisplayString
_CienaCesMplsPwCosProfileFrmCosMapName_Object = MibTableColumn
cienaCesMplsPwCosProfileFrmCosMapName = _CienaCesMplsPwCosProfileFrmCosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1, 5),
    _CienaCesMplsPwCosProfileFrmCosMapName_Type()
)
cienaCesMplsPwCosProfileFrmCosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileFrmCosMapName.setStatus("current")


class _CienaCesMplsPwCosProfileFixedTC_Type(Unsigned32):
    """Custom type cienaCesMplsPwCosProfileFixedTC based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMplsPwCosProfileFixedTC_Type.__name__ = "Unsigned32"
_CienaCesMplsPwCosProfileFixedTC_Object = MibTableColumn
cienaCesMplsPwCosProfileFixedTC = _CienaCesMplsPwCosProfileFixedTC_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1, 6),
    _CienaCesMplsPwCosProfileFixedTC_Type()
)
cienaCesMplsPwCosProfileFixedTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileFixedTC.setStatus("current")


class _CienaCesMplsPwCosProfileRcosPolicy_Type(RCosPolicy):
    """Custom type cienaCesMplsPwCosProfileRcosPolicy based on RCosPolicy"""


_CienaCesMplsPwCosProfileRcosPolicy_Object = MibTableColumn
cienaCesMplsPwCosProfileRcosPolicy = _CienaCesMplsPwCosProfileRcosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1, 7),
    _CienaCesMplsPwCosProfileRcosPolicy_Type()
)
cienaCesMplsPwCosProfileRcosPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileRcosPolicy.setStatus("current")
_CienaCesMplsPwCosProfileRcosMapName_Type = DisplayString
_CienaCesMplsPwCosProfileRcosMapName_Object = MibTableColumn
cienaCesMplsPwCosProfileRcosMapName = _CienaCesMplsPwCosProfileRcosMapName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1, 8),
    _CienaCesMplsPwCosProfileRcosMapName_Type()
)
cienaCesMplsPwCosProfileRcosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileRcosMapName.setStatus("current")


class _CienaCesMplsPwCosProfileRCosMapId_Type(Unsigned32):
    """Custom type cienaCesMplsPwCosProfileRCosMapId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsPwCosProfileRCosMapId_Type.__name__ = "Unsigned32"
_CienaCesMplsPwCosProfileRCosMapId_Object = MibTableColumn
cienaCesMplsPwCosProfileRCosMapId = _CienaCesMplsPwCosProfileRCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1, 9),
    _CienaCesMplsPwCosProfileRCosMapId_Type()
)
cienaCesMplsPwCosProfileRCosMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileRCosMapId.setStatus("current")
_CienaCesMplsPwCosProfileRcosProfileName_Type = DisplayString
_CienaCesMplsPwCosProfileRcosProfileName_Object = MibTableColumn
cienaCesMplsPwCosProfileRcosProfileName = _CienaCesMplsPwCosProfileRcosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1, 10),
    _CienaCesMplsPwCosProfileRcosProfileName_Type()
)
cienaCesMplsPwCosProfileRcosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileRcosProfileName.setStatus("current")


class _CienaCesMplsPwCosProfileRCosProfileId_Type(Integer32):
    """Custom type cienaCesMplsPwCosProfileRCosProfileId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesMplsPwCosProfileRCosProfileId_Type.__name__ = "Integer32"
_CienaCesMplsPwCosProfileRCosProfileId_Object = MibTableColumn
cienaCesMplsPwCosProfileRCosProfileId = _CienaCesMplsPwCosProfileRCosProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1, 11),
    _CienaCesMplsPwCosProfileRCosProfileId_Type()
)
cienaCesMplsPwCosProfileRCosProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileRCosProfileId.setStatus("current")


class _CienaCesMplsPwCosProfileRCosFixed_Type(Unsigned32):
    """Custom type cienaCesMplsPwCosProfileRCosFixed based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesMplsPwCosProfileRCosFixed_Type.__name__ = "Unsigned32"
_CienaCesMplsPwCosProfileRCosFixed_Object = MibTableColumn
cienaCesMplsPwCosProfileRCosFixed = _CienaCesMplsPwCosProfileRCosFixed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 2, 1, 12),
    _CienaCesMplsPwCosProfileRCosFixed_Type()
)
cienaCesMplsPwCosProfileRCosFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwCosProfileRCosFixed.setStatus("current")
_CienaCesMplsPwVccvProfileTable_Object = MibTable
cienaCesMplsPwVccvProfileTable = _CienaCesMplsPwVccvProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cienaCesMplsPwVccvProfileTable.setStatus("current")
_CienaCesMplsPwVccvProfileEntry_Object = MibTableRow
cienaCesMplsPwVccvProfileEntry = _CienaCesMplsPwVccvProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 3, 1)
)
cienaCesMplsPwVccvProfileEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsPwVccvProfileIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsPwVccvProfileEntry.setStatus("current")
_CienaCesMplsPwVccvProfileIndex_Type = Unsigned32
_CienaCesMplsPwVccvProfileIndex_Object = MibTableColumn
cienaCesMplsPwVccvProfileIndex = _CienaCesMplsPwVccvProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 3, 1, 1),
    _CienaCesMplsPwVccvProfileIndex_Type()
)
cienaCesMplsPwVccvProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsPwVccvProfileIndex.setStatus("current")
_CienaCesMplsPwVccvProfileName_Type = DisplayString
_CienaCesMplsPwVccvProfileName_Object = MibTableColumn
cienaCesMplsPwVccvProfileName = _CienaCesMplsPwVccvProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 3, 1, 2),
    _CienaCesMplsPwVccvProfileName_Type()
)
cienaCesMplsPwVccvProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwVccvProfileName.setStatus("current")


class _CienaCesMplsPwVccvProfileCcTtlExp_Type(Integer32):
    """Custom type cienaCesMplsPwVccvProfileCcTtlExp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesMplsPwVccvProfileCcTtlExp_Type.__name__ = "Integer32"
_CienaCesMplsPwVccvProfileCcTtlExp_Object = MibTableColumn
cienaCesMplsPwVccvProfileCcTtlExp = _CienaCesMplsPwVccvProfileCcTtlExp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 3, 1, 3),
    _CienaCesMplsPwVccvProfileCcTtlExp_Type()
)
cienaCesMplsPwVccvProfileCcTtlExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwVccvProfileCcTtlExp.setStatus("current")


class _CienaCesMplsPwVccvProfileCcCienaOob_Type(Integer32):
    """Custom type cienaCesMplsPwVccvProfileCcCienaOob based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CienaCesMplsPwVccvProfileCcCienaOob_Type.__name__ = "Integer32"
_CienaCesMplsPwVccvProfileCcCienaOob_Object = MibTableColumn
cienaCesMplsPwVccvProfileCcCienaOob = _CienaCesMplsPwVccvProfileCcCienaOob_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 3, 1, 4),
    _CienaCesMplsPwVccvProfileCcCienaOob_Type()
)
cienaCesMplsPwVccvProfileCcCienaOob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPwVccvProfileCcCienaOob.setStatus("current")
_CienaCesMplsPwNotif_ObjectIdentity = ObjectIdentity
cienaCesMplsPwNotif = _CienaCesMplsPwNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4)
)
_CienaCesMplsPwNotifTable_Object = MibTable
cienaCesMplsPwNotifTable = _CienaCesMplsPwNotifTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifTable.setStatus("current")
_CienaCesMplsPwNotifEntry_Object = MibTableRow
cienaCesMplsPwNotifEntry = _CienaCesMplsPwNotifEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1, 1)
)
cienaCesMplsPwNotifEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifPwIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifEntry.setStatus("current")


class _CienaCesMplsPwNotifPwIndex_Type(Unsigned32):
    """Custom type cienaCesMplsPwNotifPwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesMplsPwNotifPwIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsPwNotifPwIndex_Object = MibTableColumn
cienaCesMplsPwNotifPwIndex = _CienaCesMplsPwNotifPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1, 1, 1),
    _CienaCesMplsPwNotifPwIndex_Type()
)
cienaCesMplsPwNotifPwIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifPwIndex.setStatus("current")


class _CienaCesMplsPwNotifPwId_Type(Unsigned32):
    """Custom type cienaCesMplsPwNotifPwId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesMplsPwNotifPwId_Type.__name__ = "Unsigned32"
_CienaCesMplsPwNotifPwId_Object = MibTableColumn
cienaCesMplsPwNotifPwId = _CienaCesMplsPwNotifPwId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1, 1, 2),
    _CienaCesMplsPwNotifPwId_Type()
)
cienaCesMplsPwNotifPwId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifPwId.setStatus("current")
_CienaCesMplsPwNotifPwName_Type = DisplayString
_CienaCesMplsPwNotifPwName_Object = MibTableColumn
cienaCesMplsPwNotifPwName = _CienaCesMplsPwNotifPwName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1, 1, 3),
    _CienaCesMplsPwNotifPwName_Type()
)
cienaCesMplsPwNotifPwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifPwName.setStatus("current")
_CienaCesMplsPwNotifPwPeerIpAddr_Type = IpAddress
_CienaCesMplsPwNotifPwPeerIpAddr_Object = MibTableColumn
cienaCesMplsPwNotifPwPeerIpAddr = _CienaCesMplsPwNotifPwPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1, 1, 4),
    _CienaCesMplsPwNotifPwPeerIpAddr_Type()
)
cienaCesMplsPwNotifPwPeerIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifPwPeerIpAddr.setStatus("current")


class _CienaCesMplsPwNotifPriPwId_Type(Unsigned32):
    """Custom type cienaCesMplsPwNotifPriPwId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesMplsPwNotifPriPwId_Type.__name__ = "Unsigned32"
_CienaCesMplsPwNotifPriPwId_Object = MibTableColumn
cienaCesMplsPwNotifPriPwId = _CienaCesMplsPwNotifPriPwId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1, 1, 5),
    _CienaCesMplsPwNotifPriPwId_Type()
)
cienaCesMplsPwNotifPriPwId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifPriPwId.setStatus("current")
_CienaCesMplsPwNotifPriPwName_Type = DisplayString
_CienaCesMplsPwNotifPriPwName_Object = MibTableColumn
cienaCesMplsPwNotifPriPwName = _CienaCesMplsPwNotifPriPwName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1, 1, 6),
    _CienaCesMplsPwNotifPriPwName_Type()
)
cienaCesMplsPwNotifPriPwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifPriPwName.setStatus("current")
_CienaCesMplsPwNotifPriPwPeerIpAddr_Type = IpAddress
_CienaCesMplsPwNotifPriPwPeerIpAddr_Object = MibTableColumn
cienaCesMplsPwNotifPriPwPeerIpAddr = _CienaCesMplsPwNotifPriPwPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1, 1, 7),
    _CienaCesMplsPwNotifPriPwPeerIpAddr_Type()
)
cienaCesMplsPwNotifPriPwPeerIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifPriPwPeerIpAddr.setStatus("current")


class _CienaCesMplsPwNotifActPwIndex_Type(Unsigned32):
    """Custom type cienaCesMplsPwNotifActPwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesMplsPwNotifActPwIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsPwNotifActPwIndex_Object = MibTableColumn
cienaCesMplsPwNotifActPwIndex = _CienaCesMplsPwNotifActPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1, 1, 8),
    _CienaCesMplsPwNotifActPwIndex_Type()
)
cienaCesMplsPwNotifActPwIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifActPwIndex.setStatus("current")


class _CienaCesMplsPwNotifActPwId_Type(Unsigned32):
    """Custom type cienaCesMplsPwNotifActPwId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesMplsPwNotifActPwId_Type.__name__ = "Unsigned32"
_CienaCesMplsPwNotifActPwId_Object = MibTableColumn
cienaCesMplsPwNotifActPwId = _CienaCesMplsPwNotifActPwId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1, 1, 9),
    _CienaCesMplsPwNotifActPwId_Type()
)
cienaCesMplsPwNotifActPwId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifActPwId.setStatus("current")
_CienaCesMplsPwNotifActPwName_Type = DisplayString
_CienaCesMplsPwNotifActPwName_Object = MibTableColumn
cienaCesMplsPwNotifActPwName = _CienaCesMplsPwNotifActPwName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1, 1, 10),
    _CienaCesMplsPwNotifActPwName_Type()
)
cienaCesMplsPwNotifActPwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifActPwName.setStatus("current")
_CienaCesMplsPwNotifActPwPeerIpAddr_Type = IpAddress
_CienaCesMplsPwNotifActPwPeerIpAddr_Object = MibTableColumn
cienaCesMplsPwNotifActPwPeerIpAddr = _CienaCesMplsPwNotifActPwPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 4, 1, 1, 11),
    _CienaCesMplsPwNotifActPwPeerIpAddr_Type()
)
cienaCesMplsPwNotifActPwPeerIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesMplsPwNotifActPwPeerIpAddr.setStatus("current")
_CienaCesMplsPWTrafficStatsTable_Object = MibTable
cienaCesMplsPWTrafficStatsTable = _CienaCesMplsPWTrafficStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cienaCesMplsPWTrafficStatsTable.setStatus("current")
_CienaCesMplsPWTrafficStatsEntry_Object = MibTableRow
cienaCesMplsPWTrafficStatsEntry = _CienaCesMplsPWTrafficStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 5, 1)
)
cienaCesMplsPWTrafficStatsEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesMplsPWTrafficStatsPWIndex"),
)
if mibBuilder.loadTexts:
    cienaCesMplsPWTrafficStatsEntry.setStatus("current")
_CienaCesMplsPWTrafficStatsPWIndex_Type = Unsigned32
_CienaCesMplsPWTrafficStatsPWIndex_Object = MibTableColumn
cienaCesMplsPWTrafficStatsPWIndex = _CienaCesMplsPWTrafficStatsPWIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 5, 1, 1),
    _CienaCesMplsPWTrafficStatsPWIndex_Type()
)
cienaCesMplsPWTrafficStatsPWIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesMplsPWTrafficStatsPWIndex.setStatus("current")
_CienaCesMplsPWTrafficStatsIncomingPackets_Type = Unsigned32
_CienaCesMplsPWTrafficStatsIncomingPackets_Object = MibTableColumn
cienaCesMplsPWTrafficStatsIncomingPackets = _CienaCesMplsPWTrafficStatsIncomingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 5, 1, 2),
    _CienaCesMplsPWTrafficStatsIncomingPackets_Type()
)
cienaCesMplsPWTrafficStatsIncomingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPWTrafficStatsIncomingPackets.setStatus("current")
_CienaCesMplsPWTrafficStatsOutgoingPackets_Type = Unsigned32
_CienaCesMplsPWTrafficStatsOutgoingPackets_Object = MibTableColumn
cienaCesMplsPWTrafficStatsOutgoingPackets = _CienaCesMplsPWTrafficStatsOutgoingPackets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 5, 1, 3),
    _CienaCesMplsPWTrafficStatsOutgoingPackets_Type()
)
cienaCesMplsPWTrafficStatsOutgoingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPWTrafficStatsOutgoingPackets.setStatus("current")
_CienaCesMplsPWTrafficStatsIncomingBytes_Type = Unsigned32
_CienaCesMplsPWTrafficStatsIncomingBytes_Object = MibTableColumn
cienaCesMplsPWTrafficStatsIncomingBytes = _CienaCesMplsPWTrafficStatsIncomingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 5, 1, 4),
    _CienaCesMplsPWTrafficStatsIncomingBytes_Type()
)
cienaCesMplsPWTrafficStatsIncomingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPWTrafficStatsIncomingBytes.setStatus("current")
_CienaCesMplsPWTrafficStatsOutgoingBytes_Type = Unsigned32
_CienaCesMplsPWTrafficStatsOutgoingBytes_Object = MibTableColumn
cienaCesMplsPWTrafficStatsOutgoingBytes = _CienaCesMplsPWTrafficStatsOutgoingBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 4, 5, 1, 5),
    _CienaCesMplsPWTrafficStatsOutgoingBytes_Type()
)
cienaCesMplsPWTrafficStatsOutgoingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsPWTrafficStatsOutgoingBytes.setStatus("current")
_CienaCesMplsTe_ObjectIdentity = ObjectIdentity
cienaCesMplsTe = _CienaCesMplsTe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5)
)
_CienaCesTeLinkTable_Object = MibTable
cienaCesTeLinkTable = _CienaCesTeLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cienaCesTeLinkTable.setStatus("current")
_CienaCesTeLinkEntry_Object = MibTableRow
cienaCesTeLinkEntry = _CienaCesTeLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1)
)
cienaCesTeLinkEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesTeIfIndex"),
)
if mibBuilder.loadTexts:
    cienaCesTeLinkEntry.setStatus("current")


class _CienaCesTeIfIndex_Type(Unsigned32):
    """Custom type cienaCesTeIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesTeIfIndex_Type.__name__ = "Unsigned32"
_CienaCesTeIfIndex_Object = MibTableColumn
cienaCesTeIfIndex = _CienaCesTeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 1),
    _CienaCesTeIfIndex_Type()
)
cienaCesTeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesTeIfIndex.setStatus("current")


class _CienaCesTeInterfaceName_Type(DisplayString):
    """Custom type cienaCesTeInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesTeInterfaceName_Type.__name__ = "DisplayString"
_CienaCesTeInterfaceName_Object = MibTableColumn
cienaCesTeInterfaceName = _CienaCesTeInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 2),
    _CienaCesTeInterfaceName_Type()
)
cienaCesTeInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeInterfaceName.setStatus("current")


class _CienaCesTeLinkMetric_Type(Unsigned32):
    """Custom type cienaCesTeLinkMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesTeLinkMetric_Type.__name__ = "Unsigned32"
_CienaCesTeLinkMetric_Object = MibTableColumn
cienaCesTeLinkMetric = _CienaCesTeLinkMetric_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 3),
    _CienaCesTeLinkMetric_Type()
)
cienaCesTeLinkMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkMetric.setStatus("current")


class _CienaCesTeResourceColorGroupIndex_Type(Unsigned32):
    """Custom type cienaCesTeResourceColorGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CienaCesTeResourceColorGroupIndex_Type.__name__ = "Unsigned32"
_CienaCesTeResourceColorGroupIndex_Object = MibTableColumn
cienaCesTeResourceColorGroupIndex = _CienaCesTeResourceColorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 4),
    _CienaCesTeResourceColorGroupIndex_Type()
)
cienaCesTeResourceColorGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeResourceColorGroupIndex.setStatus("current")


class _CienaCesTeResourceColorBitMask_Type(OctetString):
    """Custom type cienaCesTeResourceColorBitMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CienaCesTeResourceColorBitMask_Type.__name__ = "OctetString"
_CienaCesTeResourceColorBitMask_Object = MibTableColumn
cienaCesTeResourceColorBitMask = _CienaCesTeResourceColorBitMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 5),
    _CienaCesTeResourceColorBitMask_Type()
)
cienaCesTeResourceColorBitMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeResourceColorBitMask.setStatus("current")


class _CienaCesMplsClassProfIndex_Type(Unsigned32):
    """Custom type cienaCesMplsClassProfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_CienaCesMplsClassProfIndex_Type.__name__ = "Unsigned32"
_CienaCesMplsClassProfIndex_Object = MibTableColumn
cienaCesMplsClassProfIndex = _CienaCesMplsClassProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 6),
    _CienaCesMplsClassProfIndex_Type()
)
cienaCesMplsClassProfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMplsClassProfIndex.setStatus("current")
_CienaCesTeLinkMode_Type = TEMode
_CienaCesTeLinkMode_Object = MibTableColumn
cienaCesTeLinkMode = _CienaCesTeLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 7),
    _CienaCesTeLinkMode_Type()
)
cienaCesTeLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkMode.setStatus("current")
_CienaCesTeLinkSrlgCount_Type = Unsigned32
_CienaCesTeLinkSrlgCount_Object = MibTableColumn
cienaCesTeLinkSrlgCount = _CienaCesTeLinkSrlgCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 8),
    _CienaCesTeLinkSrlgCount_Type()
)
cienaCesTeLinkSrlgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkSrlgCount.setStatus("current")


class _CienaCesTeLinkMaximumBandwidth_Type(MplsBitRate):
    """Custom type cienaCesTeLinkMaximumBandwidth based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkMaximumBandwidth_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkMaximumBandwidth_Object = MibTableColumn
cienaCesTeLinkMaximumBandwidth = _CienaCesTeLinkMaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 9),
    _CienaCesTeLinkMaximumBandwidth_Type()
)
cienaCesTeLinkMaximumBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkMaximumBandwidth.setStatus("current")


class _CienaCesTeLinkMaximumReservableBandwidth_Type(MplsBitRate):
    """Custom type cienaCesTeLinkMaximumReservableBandwidth based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkMaximumReservableBandwidth_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkMaximumReservableBandwidth_Object = MibTableColumn
cienaCesTeLinkMaximumReservableBandwidth = _CienaCesTeLinkMaximumReservableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 10),
    _CienaCesTeLinkMaximumReservableBandwidth_Type()
)
cienaCesTeLinkMaximumReservableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkMaximumReservableBandwidth.setStatus("current")


class _CienaCesTeLinkTotalBandwidthPrio0_Type(MplsBitRate):
    """Custom type cienaCesTeLinkTotalBandwidthPrio0 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkTotalBandwidthPrio0_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkTotalBandwidthPrio0_Object = MibTableColumn
cienaCesTeLinkTotalBandwidthPrio0 = _CienaCesTeLinkTotalBandwidthPrio0_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 11),
    _CienaCesTeLinkTotalBandwidthPrio0_Type()
)
cienaCesTeLinkTotalBandwidthPrio0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkTotalBandwidthPrio0.setStatus("current")


class _CienaCesTeLinkReservedBandwidthPrio0_Type(MplsBitRate):
    """Custom type cienaCesTeLinkReservedBandwidthPrio0 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkReservedBandwidthPrio0_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkReservedBandwidthPrio0_Object = MibTableColumn
cienaCesTeLinkReservedBandwidthPrio0 = _CienaCesTeLinkReservedBandwidthPrio0_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 12),
    _CienaCesTeLinkReservedBandwidthPrio0_Type()
)
cienaCesTeLinkReservedBandwidthPrio0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkReservedBandwidthPrio0.setStatus("current")


class _CienaCesTeLinkUnReservedBandwidthPrio0_Type(MplsBitRate):
    """Custom type cienaCesTeLinkUnReservedBandwidthPrio0 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkUnReservedBandwidthPrio0_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkUnReservedBandwidthPrio0_Object = MibTableColumn
cienaCesTeLinkUnReservedBandwidthPrio0 = _CienaCesTeLinkUnReservedBandwidthPrio0_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 13),
    _CienaCesTeLinkUnReservedBandwidthPrio0_Type()
)
cienaCesTeLinkUnReservedBandwidthPrio0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkUnReservedBandwidthPrio0.setStatus("current")


class _CienaCesTeLinkTotalBandwidthPrio1_Type(MplsBitRate):
    """Custom type cienaCesTeLinkTotalBandwidthPrio1 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkTotalBandwidthPrio1_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkTotalBandwidthPrio1_Object = MibTableColumn
cienaCesTeLinkTotalBandwidthPrio1 = _CienaCesTeLinkTotalBandwidthPrio1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 14),
    _CienaCesTeLinkTotalBandwidthPrio1_Type()
)
cienaCesTeLinkTotalBandwidthPrio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkTotalBandwidthPrio1.setStatus("current")


class _CienaCesTeLinkReservedBandwidthPrio1_Type(MplsBitRate):
    """Custom type cienaCesTeLinkReservedBandwidthPrio1 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkReservedBandwidthPrio1_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkReservedBandwidthPrio1_Object = MibTableColumn
cienaCesTeLinkReservedBandwidthPrio1 = _CienaCesTeLinkReservedBandwidthPrio1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 15),
    _CienaCesTeLinkReservedBandwidthPrio1_Type()
)
cienaCesTeLinkReservedBandwidthPrio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkReservedBandwidthPrio1.setStatus("current")


class _CienaCesTeLinkUnReservedBandwidthPrio1_Type(MplsBitRate):
    """Custom type cienaCesTeLinkUnReservedBandwidthPrio1 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkUnReservedBandwidthPrio1_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkUnReservedBandwidthPrio1_Object = MibTableColumn
cienaCesTeLinkUnReservedBandwidthPrio1 = _CienaCesTeLinkUnReservedBandwidthPrio1_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 16),
    _CienaCesTeLinkUnReservedBandwidthPrio1_Type()
)
cienaCesTeLinkUnReservedBandwidthPrio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkUnReservedBandwidthPrio1.setStatus("current")


class _CienaCesTeLinkTotalBandwidthPrio2_Type(MplsBitRate):
    """Custom type cienaCesTeLinkTotalBandwidthPrio2 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkTotalBandwidthPrio2_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkTotalBandwidthPrio2_Object = MibTableColumn
cienaCesTeLinkTotalBandwidthPrio2 = _CienaCesTeLinkTotalBandwidthPrio2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 17),
    _CienaCesTeLinkTotalBandwidthPrio2_Type()
)
cienaCesTeLinkTotalBandwidthPrio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkTotalBandwidthPrio2.setStatus("current")


class _CienaCesTeLinkReservedBandwidthPrio2_Type(MplsBitRate):
    """Custom type cienaCesTeLinkReservedBandwidthPrio2 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkReservedBandwidthPrio2_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkReservedBandwidthPrio2_Object = MibTableColumn
cienaCesTeLinkReservedBandwidthPrio2 = _CienaCesTeLinkReservedBandwidthPrio2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 18),
    _CienaCesTeLinkReservedBandwidthPrio2_Type()
)
cienaCesTeLinkReservedBandwidthPrio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkReservedBandwidthPrio2.setStatus("current")


class _CienaCesTeLinkUnReservedBandwidthPrio2_Type(MplsBitRate):
    """Custom type cienaCesTeLinkUnReservedBandwidthPrio2 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkUnReservedBandwidthPrio2_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkUnReservedBandwidthPrio2_Object = MibTableColumn
cienaCesTeLinkUnReservedBandwidthPrio2 = _CienaCesTeLinkUnReservedBandwidthPrio2_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 19),
    _CienaCesTeLinkUnReservedBandwidthPrio2_Type()
)
cienaCesTeLinkUnReservedBandwidthPrio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkUnReservedBandwidthPrio2.setStatus("current")


class _CienaCesTeLinkTotalBandwidthPrio3_Type(MplsBitRate):
    """Custom type cienaCesTeLinkTotalBandwidthPrio3 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkTotalBandwidthPrio3_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkTotalBandwidthPrio3_Object = MibTableColumn
cienaCesTeLinkTotalBandwidthPrio3 = _CienaCesTeLinkTotalBandwidthPrio3_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 20),
    _CienaCesTeLinkTotalBandwidthPrio3_Type()
)
cienaCesTeLinkTotalBandwidthPrio3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkTotalBandwidthPrio3.setStatus("current")


class _CienaCesTeLinkReservedBandwidthPrio3_Type(MplsBitRate):
    """Custom type cienaCesTeLinkReservedBandwidthPrio3 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkReservedBandwidthPrio3_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkReservedBandwidthPrio3_Object = MibTableColumn
cienaCesTeLinkReservedBandwidthPrio3 = _CienaCesTeLinkReservedBandwidthPrio3_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 21),
    _CienaCesTeLinkReservedBandwidthPrio3_Type()
)
cienaCesTeLinkReservedBandwidthPrio3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkReservedBandwidthPrio3.setStatus("current")


class _CienaCesTeLinkUnReservedBandwidthPrio3_Type(MplsBitRate):
    """Custom type cienaCesTeLinkUnReservedBandwidthPrio3 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkUnReservedBandwidthPrio3_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkUnReservedBandwidthPrio3_Object = MibTableColumn
cienaCesTeLinkUnReservedBandwidthPrio3 = _CienaCesTeLinkUnReservedBandwidthPrio3_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 22),
    _CienaCesTeLinkUnReservedBandwidthPrio3_Type()
)
cienaCesTeLinkUnReservedBandwidthPrio3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkUnReservedBandwidthPrio3.setStatus("current")


class _CienaCesTeLinkTotalBandwidthPrio4_Type(MplsBitRate):
    """Custom type cienaCesTeLinkTotalBandwidthPrio4 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkTotalBandwidthPrio4_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkTotalBandwidthPrio4_Object = MibTableColumn
cienaCesTeLinkTotalBandwidthPrio4 = _CienaCesTeLinkTotalBandwidthPrio4_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 23),
    _CienaCesTeLinkTotalBandwidthPrio4_Type()
)
cienaCesTeLinkTotalBandwidthPrio4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkTotalBandwidthPrio4.setStatus("current")


class _CienaCesTeLinkReservedBandwidthPrio4_Type(MplsBitRate):
    """Custom type cienaCesTeLinkReservedBandwidthPrio4 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkReservedBandwidthPrio4_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkReservedBandwidthPrio4_Object = MibTableColumn
cienaCesTeLinkReservedBandwidthPrio4 = _CienaCesTeLinkReservedBandwidthPrio4_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 24),
    _CienaCesTeLinkReservedBandwidthPrio4_Type()
)
cienaCesTeLinkReservedBandwidthPrio4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkReservedBandwidthPrio4.setStatus("current")


class _CienaCesTeLinkUnReservedBandwidthPrio4_Type(MplsBitRate):
    """Custom type cienaCesTeLinkUnReservedBandwidthPrio4 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkUnReservedBandwidthPrio4_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkUnReservedBandwidthPrio4_Object = MibTableColumn
cienaCesTeLinkUnReservedBandwidthPrio4 = _CienaCesTeLinkUnReservedBandwidthPrio4_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 25),
    _CienaCesTeLinkUnReservedBandwidthPrio4_Type()
)
cienaCesTeLinkUnReservedBandwidthPrio4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkUnReservedBandwidthPrio4.setStatus("current")


class _CienaCesTeLinkTotalBandwidthPrio5_Type(MplsBitRate):
    """Custom type cienaCesTeLinkTotalBandwidthPrio5 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkTotalBandwidthPrio5_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkTotalBandwidthPrio5_Object = MibTableColumn
cienaCesTeLinkTotalBandwidthPrio5 = _CienaCesTeLinkTotalBandwidthPrio5_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 26),
    _CienaCesTeLinkTotalBandwidthPrio5_Type()
)
cienaCesTeLinkTotalBandwidthPrio5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkTotalBandwidthPrio5.setStatus("current")


class _CienaCesTeLinkReservedBandwidthPrio5_Type(MplsBitRate):
    """Custom type cienaCesTeLinkReservedBandwidthPrio5 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkReservedBandwidthPrio5_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkReservedBandwidthPrio5_Object = MibTableColumn
cienaCesTeLinkReservedBandwidthPrio5 = _CienaCesTeLinkReservedBandwidthPrio5_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 27),
    _CienaCesTeLinkReservedBandwidthPrio5_Type()
)
cienaCesTeLinkReservedBandwidthPrio5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkReservedBandwidthPrio5.setStatus("current")


class _CienaCesTeLinkUnReservedBandwidthPrio5_Type(MplsBitRate):
    """Custom type cienaCesTeLinkUnReservedBandwidthPrio5 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkUnReservedBandwidthPrio5_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkUnReservedBandwidthPrio5_Object = MibTableColumn
cienaCesTeLinkUnReservedBandwidthPrio5 = _CienaCesTeLinkUnReservedBandwidthPrio5_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 28),
    _CienaCesTeLinkUnReservedBandwidthPrio5_Type()
)
cienaCesTeLinkUnReservedBandwidthPrio5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkUnReservedBandwidthPrio5.setStatus("current")


class _CienaCesTeLinkTotalBandwidthPrio6_Type(MplsBitRate):
    """Custom type cienaCesTeLinkTotalBandwidthPrio6 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkTotalBandwidthPrio6_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkTotalBandwidthPrio6_Object = MibTableColumn
cienaCesTeLinkTotalBandwidthPrio6 = _CienaCesTeLinkTotalBandwidthPrio6_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 29),
    _CienaCesTeLinkTotalBandwidthPrio6_Type()
)
cienaCesTeLinkTotalBandwidthPrio6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkTotalBandwidthPrio6.setStatus("current")


class _CienaCesTeLinkReservedBandwidthPrio6_Type(MplsBitRate):
    """Custom type cienaCesTeLinkReservedBandwidthPrio6 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkReservedBandwidthPrio6_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkReservedBandwidthPrio6_Object = MibTableColumn
cienaCesTeLinkReservedBandwidthPrio6 = _CienaCesTeLinkReservedBandwidthPrio6_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 30),
    _CienaCesTeLinkReservedBandwidthPrio6_Type()
)
cienaCesTeLinkReservedBandwidthPrio6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkReservedBandwidthPrio6.setStatus("current")


class _CienaCesTeLinkUnReservedBandwidthPrio6_Type(MplsBitRate):
    """Custom type cienaCesTeLinkUnReservedBandwidthPrio6 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkUnReservedBandwidthPrio6_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkUnReservedBandwidthPrio6_Object = MibTableColumn
cienaCesTeLinkUnReservedBandwidthPrio6 = _CienaCesTeLinkUnReservedBandwidthPrio6_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 31),
    _CienaCesTeLinkUnReservedBandwidthPrio6_Type()
)
cienaCesTeLinkUnReservedBandwidthPrio6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkUnReservedBandwidthPrio6.setStatus("current")


class _CienaCesTeLinkTotalBandwidthPrio7_Type(MplsBitRate):
    """Custom type cienaCesTeLinkTotalBandwidthPrio7 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkTotalBandwidthPrio7_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkTotalBandwidthPrio7_Object = MibTableColumn
cienaCesTeLinkTotalBandwidthPrio7 = _CienaCesTeLinkTotalBandwidthPrio7_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 32),
    _CienaCesTeLinkTotalBandwidthPrio7_Type()
)
cienaCesTeLinkTotalBandwidthPrio7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkTotalBandwidthPrio7.setStatus("current")


class _CienaCesTeLinkReservedBandwidthPrio7_Type(MplsBitRate):
    """Custom type cienaCesTeLinkReservedBandwidthPrio7 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkReservedBandwidthPrio7_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkReservedBandwidthPrio7_Object = MibTableColumn
cienaCesTeLinkReservedBandwidthPrio7 = _CienaCesTeLinkReservedBandwidthPrio7_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 33),
    _CienaCesTeLinkReservedBandwidthPrio7_Type()
)
cienaCesTeLinkReservedBandwidthPrio7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkReservedBandwidthPrio7.setStatus("current")


class _CienaCesTeLinkUnReservedBandwidthPrio7_Type(MplsBitRate):
    """Custom type cienaCesTeLinkUnReservedBandwidthPrio7 based on MplsBitRate"""
    subtypeSpec = MplsBitRate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CienaCesTeLinkUnReservedBandwidthPrio7_Type.__name__ = "MplsBitRate"
_CienaCesTeLinkUnReservedBandwidthPrio7_Object = MibTableColumn
cienaCesTeLinkUnReservedBandwidthPrio7 = _CienaCesTeLinkUnReservedBandwidthPrio7_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 1, 1, 34),
    _CienaCesTeLinkUnReservedBandwidthPrio7_Type()
)
cienaCesTeLinkUnReservedBandwidthPrio7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkUnReservedBandwidthPrio7.setStatus("current")
_CienaCesTeResourceGrpTable_Object = MibTable
cienaCesTeResourceGrpTable = _CienaCesTeResourceGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cienaCesTeResourceGrpTable.setStatus("current")
_CienaCesTeResGrpEntry_Object = MibTableRow
cienaCesTeResGrpEntry = _CienaCesTeResGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 2, 1)
)
cienaCesTeResGrpEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesTeResourceColorGrpIndex"),
)
if mibBuilder.loadTexts:
    cienaCesTeResGrpEntry.setStatus("current")


class _CienaCesTeResourceColorGrpIndex_Type(Unsigned32):
    """Custom type cienaCesTeResourceColorGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CienaCesTeResourceColorGrpIndex_Type.__name__ = "Unsigned32"
_CienaCesTeResourceColorGrpIndex_Object = MibTableColumn
cienaCesTeResourceColorGrpIndex = _CienaCesTeResourceColorGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 2, 1, 1),
    _CienaCesTeResourceColorGrpIndex_Type()
)
cienaCesTeResourceColorGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesTeResourceColorGrpIndex.setStatus("current")


class _CienaCesTeResourceGrpName_Type(DisplayString):
    """Custom type cienaCesTeResourceGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesTeResourceGrpName_Type.__name__ = "DisplayString"
_CienaCesTeResourceGrpName_Object = MibTableColumn
cienaCesTeResourceGrpName = _CienaCesTeResourceGrpName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 2, 1, 2),
    _CienaCesTeResourceGrpName_Type()
)
cienaCesTeResourceGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeResourceGrpName.setStatus("current")


class _CienaCesTeResourceColorGroupBitMask_Type(OctetString):
    """Custom type cienaCesTeResourceColorGroupBitMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CienaCesTeResourceColorGroupBitMask_Type.__name__ = "OctetString"
_CienaCesTeResourceColorGroupBitMask_Object = MibTableColumn
cienaCesTeResourceColorGroupBitMask = _CienaCesTeResourceColorGroupBitMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 2, 1, 3),
    _CienaCesTeResourceColorGroupBitMask_Type()
)
cienaCesTeResourceColorGroupBitMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeResourceColorGroupBitMask.setStatus("current")
_CienaCesTeResourceColorGroupUseCount_Type = Counter32
_CienaCesTeResourceColorGroupUseCount_Object = MibTableColumn
cienaCesTeResourceColorGroupUseCount = _CienaCesTeResourceColorGroupUseCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 2, 1, 4),
    _CienaCesTeResourceColorGroupUseCount_Type()
)
cienaCesTeResourceColorGroupUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeResourceColorGroupUseCount.setStatus("current")
_CienaCesTeResourceColorsTable_Object = MibTable
cienaCesTeResourceColorsTable = _CienaCesTeResourceColorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cienaCesTeResourceColorsTable.setStatus("current")
_CienaCesTeResColorEntry_Object = MibTableRow
cienaCesTeResColorEntry = _CienaCesTeResColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 3, 1)
)
cienaCesTeResColorEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesTeResourceColorGrpIndex"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesTeResourceColorIndex"),
)
if mibBuilder.loadTexts:
    cienaCesTeResColorEntry.setStatus("current")


class _CienaCesTeResourceColorIndex_Type(Unsigned32):
    """Custom type cienaCesTeResourceColorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CienaCesTeResourceColorIndex_Type.__name__ = "Unsigned32"
_CienaCesTeResourceColorIndex_Object = MibTableColumn
cienaCesTeResourceColorIndex = _CienaCesTeResourceColorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 3, 1, 1),
    _CienaCesTeResourceColorIndex_Type()
)
cienaCesTeResourceColorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesTeResourceColorIndex.setStatus("current")


class _CienaCesTeResourceColorName_Type(DisplayString):
    """Custom type cienaCesTeResourceColorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesTeResourceColorName_Type.__name__ = "DisplayString"
_CienaCesTeResourceColorName_Object = MibTableColumn
cienaCesTeResourceColorName = _CienaCesTeResourceColorName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 3, 1, 2),
    _CienaCesTeResourceColorName_Type()
)
cienaCesTeResourceColorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeResourceColorName.setStatus("current")


class _CienaCesTeResourceColorBit_Type(OctetString):
    """Custom type cienaCesTeResourceColorBit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CienaCesTeResourceColorBit_Type.__name__ = "OctetString"
_CienaCesTeResourceColorBit_Object = MibTableColumn
cienaCesTeResourceColorBit = _CienaCesTeResourceColorBit_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 3, 1, 3),
    _CienaCesTeResourceColorBit_Type()
)
cienaCesTeResourceColorBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeResourceColorBit.setStatus("current")
_CienaCesTeResourceColorUseCount_Type = Counter32
_CienaCesTeResourceColorUseCount_Object = MibTableColumn
cienaCesTeResourceColorUseCount = _CienaCesTeResourceColorUseCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 3, 1, 4),
    _CienaCesTeResourceColorUseCount_Type()
)
cienaCesTeResourceColorUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeResourceColorUseCount.setStatus("current")
_CienaCesTeLinkSrlgTable_Object = MibTable
cienaCesTeLinkSrlgTable = _CienaCesTeLinkSrlgTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 4)
)
if mibBuilder.loadTexts:
    cienaCesTeLinkSrlgTable.setStatus("current")
_CienaCesTeLinkSrlgEntry_Object = MibTableRow
cienaCesTeLinkSrlgEntry = _CienaCesTeLinkSrlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 4, 1)
)
cienaCesTeLinkSrlgEntry.setIndexNames(
    (0, "CIENA-CES-MPLS-MIB", "cienaCesTeIfIndex"),
    (0, "CIENA-CES-MPLS-MIB", "cienaCesTeLinkSrlg"),
)
if mibBuilder.loadTexts:
    cienaCesTeLinkSrlgEntry.setStatus("current")


class _CienaCesTeLinkSrlg_Type(Unsigned32):
    """Custom type cienaCesTeLinkSrlg based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CienaCesTeLinkSrlg_Type.__name__ = "Unsigned32"
_CienaCesTeLinkSrlg_Object = MibTableColumn
cienaCesTeLinkSrlg = _CienaCesTeLinkSrlg_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 4, 1, 1),
    _CienaCesTeLinkSrlg_Type()
)
cienaCesTeLinkSrlg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesTeLinkSrlg.setStatus("current")
_CienaCesTeLinkSrlgStatus_Type = SRLGState
_CienaCesTeLinkSrlgStatus_Object = MibTableColumn
cienaCesTeLinkSrlgStatus = _CienaCesTeLinkSrlgStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 18, 1, 5, 4, 1, 2),
    _CienaCesTeLinkSrlgStatus_Type()
)
cienaCesTeLinkSrlgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTeLinkSrlgStatus.setStatus("current")
_CienaCesMplsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesMplsMIBNotificationPrefix = _CienaCesMplsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17)
)
_CienaCesMplsMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesMplsMIBNotifications = _CienaCesMplsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 0)
)
_CienaCesGmplsMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesGmplsMIBNotifications = _CienaCesGmplsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1)
)
_CienaCesMplsPwMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesMplsPwMIBNotifications = _CienaCesMplsPwMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 2)
)

# Managed Objects groups


# Notification objects

cienaCesMplsTunnelOperStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 0, 1)
)
cienaCesMplsTunnelOperStateChgTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelAdminState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelOperState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelOamFaulted"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelFaultedNodeId"))
)
if mibBuilder.loadTexts:
    cienaCesMplsTunnelOperStateChgTrap.setStatus(
        "current"
    )

cienaCesMplsEncapTunnelGrpActiveEncapTunnelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 0, 2)
)
cienaCesMplsEncapTunnelGrpActiveEncapTunnelChange.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelGrpIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelGrpName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlType"))
)
if mibBuilder.loadTexts:
    cienaCesMplsEncapTunnelGrpActiveEncapTunnelChange.setStatus(
        "current"
    )

cienaCesMplsTransitTunnelOperStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 0, 3)
)
cienaCesMplsTransitTunnelOperStateChgTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifTransitTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifTransitTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifTransitTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifTransitTunnelAdminState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifTransitTunnelOperState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifTransitTunnelOamFaulted"))
)
if mibBuilder.loadTexts:
    cienaCesMplsTransitTunnelOperStateChgTrap.setStatus(
        "current"
    )

cienaCesMplsAssociatedTunnelOperStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 0, 6)
)
cienaCesMplsAssociatedTunnelOperStateChgTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifAssociatedTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifAssociatedTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifAssociatedTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifAssociatedTunnelAdminState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifAssociatedTunnelOperState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifAssociatedTunnelOamFaulted"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifAssociatedTunnelFaultedNodeId"))
)
if mibBuilder.loadTexts:
    cienaCesMplsAssociatedTunnelOperStateChgTrap.setStatus(
        "current"
    )

cienaCesMplsCacInterfaceThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 0, 7)
)
cienaCesMplsCacInterfaceThresholdTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifCacInterfaceIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifCacInterfaceClassType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifCacInterfaceName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsNotifCacInterfaceThreshold"))
)
if mibBuilder.loadTexts:
    cienaCesMplsCacInterfaceThresholdTrap.setStatus(
        "current"
    )

cienaCesGmplsEncapUnidirTunnelOperStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 1)
)
cienaCesGmplsEncapUnidirTunnelOperStateChgTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelAdminState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelOperState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelOamFaulted"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelFaultedNodeId"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsEncapUnidirTunnelOperStateChgTrap.setStatus(
        "current"
    )

cienaCesGmplsEncapCoroutedTunnelOperStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 2)
)
cienaCesGmplsEncapCoroutedTunnelOperStateChgTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelAdminState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelOperState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelOamFaulted"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelFaultedNodeId"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsEncapCoroutedTunnelOperStateChgTrap.setStatus(
        "current"
    )

cienaCesGmplsDecapCoroutedTunnelOperStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 3)
)
cienaCesGmplsDecapCoroutedTunnelOperStateChgTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelAdminState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelOperState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelOamFaulted"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelFaultedNodeId"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsDecapCoroutedTunnelOperStateChgTrap.setStatus(
        "current"
    )

cienaCesGmplsTransitUnidirTunnelOperStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 4)
)
cienaCesGmplsTransitUnidirTunnelOperStateChgTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelAdminState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelOperState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelOamFaulted"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsTransitUnidirTunnelOperStateChgTrap.setStatus(
        "current"
    )

cienaCesGmplsTransitCoroutedTunnelOperStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 5)
)
cienaCesGmplsTransitCoroutedTunnelOperStateChgTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelAdminState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelOperState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTransitTunnelOamFaulted"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsTransitCoroutedTunnelOperStateChgTrap.setStatus(
        "current"
    )

cienaCesGmplsEncapUnidirTunnelGrpActiveEncapTunnelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 6)
)
cienaCesGmplsEncapUnidirTunnelGrpActiveEncapTunnelChangeTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelGrpIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelGrpName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsEncapUnidirTunnelGrpActiveEncapTunnelChangeTrap.setStatus(
        "current"
    )

cienaCesGmplsEncapCoroutedTunnelGrpActiveEncapTunnelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 7)
)
cienaCesGmplsEncapCoroutedTunnelGrpActiveEncapTunnelChangeTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelGrpIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelGrpName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsEncapCoroutedTunnelGrpActiveEncapTunnelChangeTrap.setStatus(
        "current"
    )

cienaCesGmplsDecapCoroutedTunnelGrpActiveDecapTunnelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 8)
)
cienaCesGmplsDecapCoroutedTunnelGrpActiveDecapTunnelChangeTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelGrpIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelGrpName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlType"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsDecapCoroutedTunnelGrpActiveDecapTunnelChangeTrap.setStatus(
        "current"
    )

cienaCesGmplsAssociatedTunnelOperStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 9)
)
cienaCesGmplsAssociatedTunnelOperStateChgTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelAdminState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelOperState"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelOamFaulted"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelFaultedNodeId"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedTunnelOperStateChgTrap.setStatus(
        "current"
    )

cienaCesGmplsEncapCoroutedTunnelAisFaultStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 10)
)
cienaCesGmplsEncapCoroutedTunnelAisFaultStateChgTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelAisFaulted"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelFaultedNodeId"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelFarEndLerId"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsEncapCoroutedTunnelAisFaultStateChgTrap.setStatus(
        "obsolete"
    )

cienaCesGmplsDecapCoroutedTunnelAisFaultStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 11)
)
cienaCesGmplsDecapCoroutedTunnelAisFaultStateChgTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelAisFaulted"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelFaultedNodeId"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifDecapTunnelFarEndLerId"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsDecapCoroutedTunnelAisFaultStateChgTrap.setStatus(
        "obsolete"
    )

cienaCesGmplsAssociatedTunnelAisFaultStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 12)
)
cienaCesGmplsAssociatedTunnelAisFaultStateChgTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelAisFaulted"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelFaultedNodeId"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifAssociatedTunnelFarEndLerId"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsAssociatedTunnelAisFaultStateChgTrap.setStatus(
        "obsolete"
    )

cienaCesGmplsTunnelAisFaultErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 13)
)
cienaCesGmplsTunnelAisFaultErrorTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTunnelDecapLabel"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifTunnelErrorMsg"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsTunnelAisFaultErrorTrap.setStatus(
        "current"
    )

cienaCesGmplsEncapTunnelResizeResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 14)
)
cienaCesGmplsEncapTunnelResizeResultTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelResult"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelProtectionRole"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelRequestedBw"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelOperationalBw"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsEncapTunnelResizeResultTrap.setStatus(
        "current"
    )

cienaCesGmplsEncapTunnelMbbResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 1, 15)
)
cienaCesGmplsEncapTunnelMbbResultTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelType"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelResult"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelProtectionRole"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelRequestedBw"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelOperationalBw"),
        ("CIENA-CES-MPLS-MIB", "cienaCesGmplsNotifEncapTunnelMbbParentApp"))
)
if mibBuilder.loadTexts:
    cienaCesGmplsEncapTunnelMbbResultTrap.setStatus(
        "current"
    )

cienaCesMplsPwDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 2, 1)
)
cienaCesMplsPwDown.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifPwIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifPwName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifPwId"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifPwPeerIpAddr"))
)
if mibBuilder.loadTexts:
    cienaCesMplsPwDown.setStatus(
        "current"
    )

cienaCesMplsPwUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 2, 2)
)
cienaCesMplsPwUp.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifPwIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifPwName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifPwId"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifPwPeerIpAddr"))
)
if mibBuilder.loadTexts:
    cienaCesMplsPwUp.setStatus(
        "current"
    )

cienaCesMplsPwBundleActivePwChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 17, 2, 3)
)
cienaCesMplsPwBundleActivePwChange.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifActPwIndex"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifActPwName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifActPwId"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifActPwPeerIpAddr"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifPriPwName"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifPriPwId"),
        ("CIENA-CES-MPLS-MIB", "cienaCesMplsPwNotifPriPwPeerIpAddr"))
)
if mibBuilder.loadTexts:
    cienaCesMplsPwBundleActivePwChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-MPLS-MIB",
    **{"TTLPolicy": TTLPolicy,
       "PseudoWireType": PseudoWireType,
       "RCosPolicy": RCosPolicy,
       "FCosPolicy": FCosPolicy,
       "PrivateForwardGroup": PrivateForwardGroup,
       "OperState": OperState,
       "VCFailReason": VCFailReason,
       "VCStatus": VCStatus,
       "VCState": VCState,
       "AttachGroupType": AttachGroupType,
       "TunnelType": TunnelType,
       "TunnelAisFault": TunnelAisFault,
       "TunnelOamFault": TunnelOamFault,
       "AutoSizeFailHdlr": AutoSizeFailHdlr,
       "AutoSizeState": AutoSizeState,
       "AutoSizeMode": AutoSizeMode,
       "CacPolicy": CacPolicy,
       "PathDisjointType": PathDisjointType,
       "PathDisjointMode": PathDisjointMode,
       "SRLGState": SRLGState,
       "TEMode": TEMode,
       "MplsGlobalState": MplsGlobalState,
       "cienaCesMplsMIB": cienaCesMplsMIB,
       "cienaCesMplsMIBObjects": cienaCesMplsMIBObjects,
       "cienaCesMpls": cienaCesMpls,
       "cienaCesMplsGlobalAttrs": cienaCesMplsGlobalAttrs,
       "cienaCesMplsStaticAdminLabelRangeStart": cienaCesMplsStaticAdminLabelRangeStart,
       "cienaCesMplsStaticAdminLabelRangeEnd": cienaCesMplsStaticAdminLabelRangeEnd,
       "cienaCesMplsStaticOperLabelRangeStart": cienaCesMplsStaticOperLabelRangeStart,
       "cienaCesMplsStaticOperLabelRangeEnd": cienaCesMplsStaticOperLabelRangeEnd,
       "cienaCesMplsDynamicAdminLabelRangeStart": cienaCesMplsDynamicAdminLabelRangeStart,
       "cienaCesMplsDynamicAdminLabelRangeEnd": cienaCesMplsDynamicAdminLabelRangeEnd,
       "cienaCesMplsDynamicOperLabelRangeStart": cienaCesMplsDynamicOperLabelRangeStart,
       "cienaCesMplsDynamicOperLabelRangeEnd": cienaCesMplsDynamicOperLabelRangeEnd,
       "cienaCesMplsStaticIngressTunnelTable": cienaCesMplsStaticIngressTunnelTable,
       "cienaCesMplsStaticIngressTunnelEntry": cienaCesMplsStaticIngressTunnelEntry,
       "cienaCesMplsStaticIngressTunnelIndex": cienaCesMplsStaticIngressTunnelIndex,
       "cienaCesMplsStaticIngressTunnelName": cienaCesMplsStaticIngressTunnelName,
       "cienaCesMplsStaticIngressTunnelWeight": cienaCesMplsStaticIngressTunnelWeight,
       "cienaCesMplsStaticIngressTunnelNextHopIp": cienaCesMplsStaticIngressTunnelNextHopIp,
       "cienaCesMplsStaticIngressTunnelAdminState": cienaCesMplsStaticIngressTunnelAdminState,
       "cienaCesMplsStaticIngressTunnelOperState": cienaCesMplsStaticIngressTunnelOperState,
       "cienaCesMplsStaticIngressTunnelDestIpAddr": cienaCesMplsStaticIngressTunnelDestIpAddr,
       "cienaCesMplsStaticIngressTunnelLabel": cienaCesMplsStaticIngressTunnelLabel,
       "cienaCesMplsStaticIngressTunnelFrmCosPolicy": cienaCesMplsStaticIngressTunnelFrmCosPolicy,
       "cienaCesMplsStaticIngressTunnelFrmCosMapId": cienaCesMplsStaticIngressTunnelFrmCosMapId,
       "cienaCesMplsStaticIngressTunnelFixedExp": cienaCesMplsStaticIngressTunnelFixedExp,
       "cienaCesMplsStaticIngressTunnelTTLPolicy": cienaCesMplsStaticIngressTunnelTTLPolicy,
       "cienaCesMplsStaticIngressTunnelFixedTTL": cienaCesMplsStaticIngressTunnelFixedTTL,
       "cienaCesMplsStaticIngressTunnelGrpIndex": cienaCesMplsStaticIngressTunnelGrpIndex,
       "cienaCesMplsStaticIngressTunnelReversion": cienaCesMplsStaticIngressTunnelReversion,
       "cienaCesMplsStaticIngressTunnelReversionTimeout": cienaCesMplsStaticIngressTunnelReversionTimeout,
       "cienaCesMplsStaticIngressTunnelPrimaryTunnelName": cienaCesMplsStaticIngressTunnelPrimaryTunnelName,
       "cienaCesMplsStaticIngressTunnelFixedTC": cienaCesMplsStaticIngressTunnelFixedTC,
       "cienaCesMplsStaticIngressTunnelProtectionRole": cienaCesMplsStaticIngressTunnelProtectionRole,
       "cienaCesMplsStaticIngressTunnelProtectionState": cienaCesMplsStaticIngressTunnelProtectionState,
       "cienaCesMplsStaticIngressTunnelProtectionPartnerName": cienaCesMplsStaticIngressTunnelProtectionPartnerName,
       "cienaCesMplsStaticIngressTunnelCosProfileIndex": cienaCesMplsStaticIngressTunnelCosProfileIndex,
       "cienaCesMplsStaticIngressTunnelCosProfileName": cienaCesMplsStaticIngressTunnelCosProfileName,
       "cienaCesMplsStaticIngressTunnelRecoveryDisjoint": cienaCesMplsStaticIngressTunnelRecoveryDisjoint,
       "cienaCesMplsDynamicIngressTunnelTable": cienaCesMplsDynamicIngressTunnelTable,
       "cienaCesMplsDynamicIngressTunnelEntry": cienaCesMplsDynamicIngressTunnelEntry,
       "cienaCesMplsDynamicIngressTunnelIndex": cienaCesMplsDynamicIngressTunnelIndex,
       "cienaCesMplsDynamicIngressTunnelName": cienaCesMplsDynamicIngressTunnelName,
       "cienaCesMplsDynamicIngressTunnelWeight": cienaCesMplsDynamicIngressTunnelWeight,
       "cienaCesMplsDynamicIngressTunnelLspId": cienaCesMplsDynamicIngressTunnelLspId,
       "cienaCesMplsDynamicIngressTunnelNextHopIp": cienaCesMplsDynamicIngressTunnelNextHopIp,
       "cienaCesMplsDynamicIngressTunnelAdminState": cienaCesMplsDynamicIngressTunnelAdminState,
       "cienaCesMplsDynamicIngressTunnelOperState": cienaCesMplsDynamicIngressTunnelOperState,
       "cienaCesMplsDynamicIngressTunnelDestIpAddr": cienaCesMplsDynamicIngressTunnelDestIpAddr,
       "cienaCesMplsDynamicIngressTunnelLabel": cienaCesMplsDynamicIngressTunnelLabel,
       "cienaCesMplsDynamicIngressTunnelFrmCosPolicy": cienaCesMplsDynamicIngressTunnelFrmCosPolicy,
       "cienaCesMplsDynamicIngressTunnelFrmCosMapId": cienaCesMplsDynamicIngressTunnelFrmCosMapId,
       "cienaCesMplsDynamicIngressTunnelFixedExp": cienaCesMplsDynamicIngressTunnelFixedExp,
       "cienaCesMplsDynamicIngressTunnelSetupPriority": cienaCesMplsDynamicIngressTunnelSetupPriority,
       "cienaCesMplsDynamicIngressTunnelHoldPriority": cienaCesMplsDynamicIngressTunnelHoldPriority,
       "cienaCesMplsDynamicIngressTunnelRecordRoute": cienaCesMplsDynamicIngressTunnelRecordRoute,
       "cienaCesMplsDynamicIngressTunnelFastRoute": cienaCesMplsDynamicIngressTunnelFastRoute,
       "cienaCesMplsDynamicIngressTunnelTTLPolicy": cienaCesMplsDynamicIngressTunnelTTLPolicy,
       "cienaCesMplsDynamicIngressTunnelFixedTTL": cienaCesMplsDynamicIngressTunnelFixedTTL,
       "cienaCesMplsDynamicIngressTunnelPathIndex": cienaCesMplsDynamicIngressTunnelPathIndex,
       "cienaCesMplsDynamicIngressTunnelPathName": cienaCesMplsDynamicIngressTunnelPathName,
       "cienaCesMplsDynamicIngressTunnelGrpIndex": cienaCesMplsDynamicIngressTunnelGrpIndex,
       "cienaCesMplsDynamicIngressTunnelResourcePointer": cienaCesMplsDynamicIngressTunnelResourcePointer,
       "cienaCesMplsDynamicIngressTunnelReversion": cienaCesMplsDynamicIngressTunnelReversion,
       "cienaCesMplsDynamicIngressTunnelReversionTimeout": cienaCesMplsDynamicIngressTunnelReversionTimeout,
       "cienaCesMplsDynamicIngressTunnelBandwidthProfile": cienaCesMplsDynamicIngressTunnelBandwidthProfile,
       "cienaCesMplsDynamicIngressTunnelPrimaryTunnelName": cienaCesMplsDynamicIngressTunnelPrimaryTunnelName,
       "cienaCesMplsDynamicIngressTunnelFixedTC": cienaCesMplsDynamicIngressTunnelFixedTC,
       "cienaCesMplsDynamicIngressTunnelProtectionRole": cienaCesMplsDynamicIngressTunnelProtectionRole,
       "cienaCesMplsDynamicIngressTunnelProtectionState": cienaCesMplsDynamicIngressTunnelProtectionState,
       "cienaCesMplsDynamicIngressTunnelProtectionPartnerName": cienaCesMplsDynamicIngressTunnelProtectionPartnerName,
       "cienaCesMplsDynamicIngressTunnelCosProfileIndex": cienaCesMplsDynamicIngressTunnelCosProfileIndex,
       "cienaCesMplsDynamicIngressTunnelCosProfileName": cienaCesMplsDynamicIngressTunnelCosProfileName,
       "cienaCesMplsStaticEgressTunnelTable": cienaCesMplsStaticEgressTunnelTable,
       "cienaCesMplsStaticEgressTunnelEntry": cienaCesMplsStaticEgressTunnelEntry,
       "cienaCesMplsStaticEgressTunnelIndex": cienaCesMplsStaticEgressTunnelIndex,
       "cienaCesMplsStaticEgressTunnelName": cienaCesMplsStaticEgressTunnelName,
       "cienaCesMplsStaticEgressTunnelAdminState": cienaCesMplsStaticEgressTunnelAdminState,
       "cienaCesMplsStaticEgressTunnelOperState": cienaCesMplsStaticEgressTunnelOperState,
       "cienaCesMplsStaticEgressTunnelSourceIpAddr": cienaCesMplsStaticEgressTunnelSourceIpAddr,
       "cienaCesMplsStaticEgressTunnelLabel": cienaCesMplsStaticEgressTunnelLabel,
       "cienaCesMplsDynamicEgressTunnelTable": cienaCesMplsDynamicEgressTunnelTable,
       "cienaCesMplsDynamicEgressTunnelEntry": cienaCesMplsDynamicEgressTunnelEntry,
       "cienaCesMplsDynamicEgressTunnelIndex": cienaCesMplsDynamicEgressTunnelIndex,
       "cienaCesMplsDynamicEgressTunnelName": cienaCesMplsDynamicEgressTunnelName,
       "cienaCesMplsDynamicEgressTunnelAdminState": cienaCesMplsDynamicEgressTunnelAdminState,
       "cienaCesMplsDynamicEgressTunnelOperState": cienaCesMplsDynamicEgressTunnelOperState,
       "cienaCesMplsDynamicEgressTunnelInstance": cienaCesMplsDynamicEgressTunnelInstance,
       "cienaCesMplsDynamicEgressTunnelSourceIpAddr": cienaCesMplsDynamicEgressTunnelSourceIpAddr,
       "cienaCesMplsDynamicEgressTunnelDestIpAddr": cienaCesMplsDynamicEgressTunnelDestIpAddr,
       "cienaCesMplsDynamicEgressTunnelLabel": cienaCesMplsDynamicEgressTunnelLabel,
       "cienaCesMplsStaticTransitTunnelTable": cienaCesMplsStaticTransitTunnelTable,
       "cienaCesMplsStaticTransitTunnelEntry": cienaCesMplsStaticTransitTunnelEntry,
       "cienaCesMplsStaticTransitTunnelIndex": cienaCesMplsStaticTransitTunnelIndex,
       "cienaCesMplsStaticTransitTunnelName": cienaCesMplsStaticTransitTunnelName,
       "cienaCesMplsStaticTransitTunnelAdminState": cienaCesMplsStaticTransitTunnelAdminState,
       "cienaCesMplsStaticTransitTunnelOperState": cienaCesMplsStaticTransitTunnelOperState,
       "cienaCesMplsStaticTransitTunnelNextHopIpAddr": cienaCesMplsStaticTransitTunnelNextHopIpAddr,
       "cienaCesMplsStaticTransitTunnelInLabel": cienaCesMplsStaticTransitTunnelInLabel,
       "cienaCesMplsStaticTransitTunnelOutLabel": cienaCesMplsStaticTransitTunnelOutLabel,
       "cienaCesMplsStaticTransitTunnelFcosPolicy": cienaCesMplsStaticTransitTunnelFcosPolicy,
       "cienaCesMplsStaticTransitTunnelFixedTc": cienaCesMplsStaticTransitTunnelFixedTc,
       "cienaCesMplsStaticTransitTunnelFrmCosMapId": cienaCesMplsStaticTransitTunnelFrmCosMapId,
       "cienaCesMplsStaticTransitTunnelTTLPolicy": cienaCesMplsStaticTransitTunnelTTLPolicy,
       "cienaCesMplsStaticTransitTunnelFixedTTL": cienaCesMplsStaticTransitTunnelFixedTTL,
       "cienaCesMplsStaticTransitTunnelRcosPolicy": cienaCesMplsStaticTransitTunnelRcosPolicy,
       "cienaCesMplsStaticTransitTunnelRCosMapId": cienaCesMplsStaticTransitTunnelRCosMapId,
       "cienaCesMplsStaticTransitTunnelCosProfileIndex": cienaCesMplsStaticTransitTunnelCosProfileIndex,
       "cienaCesMplsStaticTransitTunnelCosProfileName": cienaCesMplsStaticTransitTunnelCosProfileName,
       "cienaCesMplsStaticTransitTunnelSourceIpAddr": cienaCesMplsStaticTransitTunnelSourceIpAddr,
       "cienaCesMplsStaticTransitTunnelDestIpAddr": cienaCesMplsStaticTransitTunnelDestIpAddr,
       "cienaCesMplsStaticTransitTunnelIncomingPackets": cienaCesMplsStaticTransitTunnelIncomingPackets,
       "cienaCesMplsStaticTransitTunnelOutgoingPackets": cienaCesMplsStaticTransitTunnelOutgoingPackets,
       "cienaCesMplsStaticTransitTunnelIncomingBytes": cienaCesMplsStaticTransitTunnelIncomingBytes,
       "cienaCesMplsStaticTransitTunnelOutgoingBytes": cienaCesMplsStaticTransitTunnelOutgoingBytes,
       "cienaCesMplsDynamicTransitTunnelTable": cienaCesMplsDynamicTransitTunnelTable,
       "cienaCesMplsDynamicTransitTunnelEntry": cienaCesMplsDynamicTransitTunnelEntry,
       "cienaCesMplsDynamicTransitTunnelIndex": cienaCesMplsDynamicTransitTunnelIndex,
       "cienaCesMplsDynamicTransitTunnelName": cienaCesMplsDynamicTransitTunnelName,
       "cienaCesMplsDynamicTransitTunnelAdminState": cienaCesMplsDynamicTransitTunnelAdminState,
       "cienaCesMplsDynamicTransitTunnelOperState": cienaCesMplsDynamicTransitTunnelOperState,
       "cienaCesMplsDynamicTransitTunnelInLabel": cienaCesMplsDynamicTransitTunnelInLabel,
       "cienaCesMplsDynamicTransitTunnelOutLabel": cienaCesMplsDynamicTransitTunnelOutLabel,
       "cienaCesMplsDynamicTransitTunnelNextHopIpAddr": cienaCesMplsDynamicTransitTunnelNextHopIpAddr,
       "cienaCesMplsDynamicTransitTunnelSourceIpAddr": cienaCesMplsDynamicTransitTunnelSourceIpAddr,
       "cienaCesMplsDynamicTransitTunnelDestIpAddr": cienaCesMplsDynamicTransitTunnelDestIpAddr,
       "cienaCesMplsDynamicTransitTunnelIncomingPackets": cienaCesMplsDynamicTransitTunnelIncomingPackets,
       "cienaCesMplsDynamicTransitTunnelOutgoingPackets": cienaCesMplsDynamicTransitTunnelOutgoingPackets,
       "cienaCesMplsDynamicTransitTunnelIncomingBytes": cienaCesMplsDynamicTransitTunnelIncomingBytes,
       "cienaCesMplsDynamicTransitTunnelOutgoingBytes": cienaCesMplsDynamicTransitTunnelOutgoingBytes,
       "cienaCesMplsTunnelPath": cienaCesMplsTunnelPath,
       "cienaCesMplsTunnelPathTable": cienaCesMplsTunnelPathTable,
       "cienaCesMplsTunnelPathEntry": cienaCesMplsTunnelPathEntry,
       "cienaCesMplsTunnelPathIndex": cienaCesMplsTunnelPathIndex,
       "cienaCesMplsTunnelPathName": cienaCesMplsTunnelPathName,
       "cienaCesMplsTunnelPathUseCount": cienaCesMplsTunnelPathUseCount,
       "cienaCesMplsTunnelPathHopTable": cienaCesMplsTunnelPathHopTable,
       "cienaCesMplsTunnelPathHopEntry": cienaCesMplsTunnelPathHopEntry,
       "cienaCesMplsTunnelPathHopIndex": cienaCesMplsTunnelPathHopIndex,
       "cienaCesMplsTunnelPathHopIpAddr": cienaCesMplsTunnelPathHopIpAddr,
       "cienaCesMplsTunnelPathHopType": cienaCesMplsTunnelPathHopType,
       "cienaCesMplsEncapTunnelNotif": cienaCesMplsEncapTunnelNotif,
       "cienaCesMplsNotifEncapTunnelTable": cienaCesMplsNotifEncapTunnelTable,
       "cienaCesMplsNotifEncapTunnelEntry": cienaCesMplsNotifEncapTunnelEntry,
       "cienaCesMplsNotifEncapTunnelIndex": cienaCesMplsNotifEncapTunnelIndex,
       "cienaCesMplsNotifEncapTunnelType": cienaCesMplsNotifEncapTunnelType,
       "cienaCesMplsNotifEncapTunnelName": cienaCesMplsNotifEncapTunnelName,
       "cienaCesMplsNotifEncapTunnelAdminState": cienaCesMplsNotifEncapTunnelAdminState,
       "cienaCesMplsNotifEncapTunnelOperState": cienaCesMplsNotifEncapTunnelOperState,
       "cienaCesMplsNotifEncapTunnelOamFaulted": cienaCesMplsNotifEncapTunnelOamFaulted,
       "cienaCesMplsNotifEncapTunnelFaultedNodeId": cienaCesMplsNotifEncapTunnelFaultedNodeId,
       "cienaCesMplsTransitTunnelNotif": cienaCesMplsTransitTunnelNotif,
       "cienaCesMplsNotifTransitTunnelTable": cienaCesMplsNotifTransitTunnelTable,
       "cienaCesMplsNotifTransitTunnelEntry": cienaCesMplsNotifTransitTunnelEntry,
       "cienaCesMplsNotifTransitTunnelIndex": cienaCesMplsNotifTransitTunnelIndex,
       "cienaCesMplsNotifTransitTunnelType": cienaCesMplsNotifTransitTunnelType,
       "cienaCesMplsNotifTransitTunnelName": cienaCesMplsNotifTransitTunnelName,
       "cienaCesMplsNotifTransitTunnelAdminState": cienaCesMplsNotifTransitTunnelAdminState,
       "cienaCesMplsNotifTransitTunnelOperState": cienaCesMplsNotifTransitTunnelOperState,
       "cienaCesMplsNotifTransitTunnelOamFaulted": cienaCesMplsNotifTransitTunnelOamFaulted,
       "cienaCesMplsEncapTunnelGrpNotif": cienaCesMplsEncapTunnelGrpNotif,
       "cienaCesMplsNotifEncapTunnelGrpTable": cienaCesMplsNotifEncapTunnelGrpTable,
       "cienaCesMplsNotifEncapTunnelGrpEntry": cienaCesMplsNotifEncapTunnelGrpEntry,
       "cienaCesMplsNotifEncapTunnelGrpIndex": cienaCesMplsNotifEncapTunnelGrpIndex,
       "cienaCesMplsNotifEncapTunnelGrpName": cienaCesMplsNotifEncapTunnelGrpName,
       "cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlIndex": cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlIndex,
       "cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlName": cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlName,
       "cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlType": cienaCesMplsNotifEncapTunnelGrpActiveEncapTunlType,
       "cienaCesMplsAssociatedTunnelTable": cienaCesMplsAssociatedTunnelTable,
       "cienaCesMplsAssociatedTunnelEntry": cienaCesMplsAssociatedTunnelEntry,
       "cienaCesMplsAssociatedTunnelIndex": cienaCesMplsAssociatedTunnelIndex,
       "cienaCesMplsAssociatedTunnelName": cienaCesMplsAssociatedTunnelName,
       "cienaCesMplsAssociatedForwardTunnelName": cienaCesMplsAssociatedForwardTunnelName,
       "cienaCesMplsAssociatedForwardTunnelType": cienaCesMplsAssociatedForwardTunnelType,
       "cienaCesMplsAssociatedReverseTunnelName": cienaCesMplsAssociatedReverseTunnelName,
       "cienaCesMplsAssociatedReverseTunnelType": cienaCesMplsAssociatedReverseTunnelType,
       "cienaCesMplsAssociatedForwardTunnelDestIpAddr": cienaCesMplsAssociatedForwardTunnelDestIpAddr,
       "cienaCesMplsAssociatedDynamicTunnelSrcIpAddr": cienaCesMplsAssociatedDynamicTunnelSrcIpAddr,
       "cienaCesMplsAssociatedTunnelAdminState": cienaCesMplsAssociatedTunnelAdminState,
       "cienaCesMplsAssociatedTunnelOperState": cienaCesMplsAssociatedTunnelOperState,
       "cienaCesMplsAssociatedForwardTunnelOperState": cienaCesMplsAssociatedForwardTunnelOperState,
       "cienaCesMplsAssociatedReverseTunnelOperState": cienaCesMplsAssociatedReverseTunnelOperState,
       "cienaCesMplsAssociatedProtectionRole": cienaCesMplsAssociatedProtectionRole,
       "cienaCesMplsAssociatedProtectionState": cienaCesMplsAssociatedProtectionState,
       "cienaCesMplsAssociatedTunnelProtectionPartnerName": cienaCesMplsAssociatedTunnelProtectionPartnerName,
       "cienaCesMplsAssociatedBfdMonitoring": cienaCesMplsAssociatedBfdMonitoring,
       "cienaCesMplsAssociatedBfdProfileName": cienaCesMplsAssociatedBfdProfileName,
       "cienaCesMplsAssociatedBfdSessionName": cienaCesMplsAssociatedBfdSessionName,
       "cienaCesMplsAssociatedBfdSessionFaulted": cienaCesMplsAssociatedBfdSessionFaulted,
       "cienaCesMplsAssociatedBfdProfileIndex": cienaCesMplsAssociatedBfdProfileIndex,
       "cienaCesMplsTunnelARHopTable": cienaCesMplsTunnelARHopTable,
       "cienaCesMplsTunnelARHopEntry": cienaCesMplsTunnelARHopEntry,
       "cienaMplsTunnelARHopListIndex": cienaMplsTunnelARHopListIndex,
       "cienaMplsTunnelARHopIndex": cienaMplsTunnelARHopIndex,
       "cienaMplsTunnelARHopAddrType": cienaMplsTunnelARHopAddrType,
       "cienaMplsTunnelARHopIpAddr": cienaMplsTunnelARHopIpAddr,
       "cienaMplsTunnelARHopAddrUnnum": cienaMplsTunnelARHopAddrUnnum,
       "cienaMplsTunnelARHopLspId": cienaMplsTunnelARHopLspId,
       "cienaCesMplsAssociatedTunnelNotif": cienaCesMplsAssociatedTunnelNotif,
       "cienaCesMplsNotifAssociatedTunnelTable": cienaCesMplsNotifAssociatedTunnelTable,
       "cienaCesMplsNotifAssociatedTunnelEntry": cienaCesMplsNotifAssociatedTunnelEntry,
       "cienaCesMplsNotifAssociatedTunnelIndex": cienaCesMplsNotifAssociatedTunnelIndex,
       "cienaCesMplsNotifAssociatedTunnelType": cienaCesMplsNotifAssociatedTunnelType,
       "cienaCesMplsNotifAssociatedTunnelName": cienaCesMplsNotifAssociatedTunnelName,
       "cienaCesMplsNotifAssociatedTunnelAdminState": cienaCesMplsNotifAssociatedTunnelAdminState,
       "cienaCesMplsNotifAssociatedTunnelOperState": cienaCesMplsNotifAssociatedTunnelOperState,
       "cienaCesMplsNotifAssociatedTunnelOamFaulted": cienaCesMplsNotifAssociatedTunnelOamFaulted,
       "cienaCesMplsNotifAssociatedTunnelFaultedNodeId": cienaCesMplsNotifAssociatedTunnelFaultedNodeId,
       "cienaCesMplsCacInterfaceNotif": cienaCesMplsCacInterfaceNotif,
       "cienaCesMplsNotifCacInterfaceTable": cienaCesMplsNotifCacInterfaceTable,
       "cienaCesMplsNotifCacInterfaceEntry": cienaCesMplsNotifCacInterfaceEntry,
       "cienaCesMplsNotifCacInterfaceIndex": cienaCesMplsNotifCacInterfaceIndex,
       "cienaCesMplsNotifCacInterfaceClassType": cienaCesMplsNotifCacInterfaceClassType,
       "cienaCesMplsNotifCacInterfaceName": cienaCesMplsNotifCacInterfaceName,
       "cienaCesMplsNotifCacInterfaceThreshold": cienaCesMplsNotifCacInterfaceThreshold,
       "cienaCesMplsClassProfileTable": cienaCesMplsClassProfileTable,
       "cienaCesMplsClassProfileEntry": cienaCesMplsClassProfileEntry,
       "cienaCesMplsClassProfileIndex": cienaCesMplsClassProfileIndex,
       "cienaCesMplsClassProfileName": cienaCesMplsClassProfileName,
       "cienaCesMplsClassProfileCacPolicy": cienaCesMplsClassProfileCacPolicy,
       "cienaCesMplsTEClassTypeTable": cienaCesMplsTEClassTypeTable,
       "cienaCesMplsTEClassTypeEntry": cienaCesMplsTEClassTypeEntry,
       "cienaCesMplsClassType": cienaCesMplsClassType,
       "cienaCesMplsClassTypeQueueGroupIndex": cienaCesMplsClassTypeQueueGroupIndex,
       "cienaCesMplsClassTypeQueueGroupInstance": cienaCesMplsClassTypeQueueGroupInstance,
       "cienaCesMplsClassTypeLom": cienaCesMplsClassTypeLom,
       "cienaCesMplsClassTypeAlarmThreshold": cienaCesMplsClassTypeAlarmThreshold,
       "cienaCesGmpls": cienaCesGmpls,
       "cienaCesGmplsStaticIngressUniDirTunnelTable": cienaCesGmplsStaticIngressUniDirTunnelTable,
       "cienaCesGmplsStaticIngressUniDirTunnelEntry": cienaCesGmplsStaticIngressUniDirTunnelEntry,
       "cienaCesGmplsStaticIngressUniDirTunnelIndex": cienaCesGmplsStaticIngressUniDirTunnelIndex,
       "cienaCesGmplsStaticIngressUniDirTunnelName": cienaCesGmplsStaticIngressUniDirTunnelName,
       "cienaCesGmplsStaticIngressUniDirTunnelNextHopIp": cienaCesGmplsStaticIngressUniDirTunnelNextHopIp,
       "cienaCesGmplsStaticIngressUniDirTunnelSrcIpAddr": cienaCesGmplsStaticIngressUniDirTunnelSrcIpAddr,
       "cienaCesGmplsStaticIngressUniDirTunnelDestIpAddr": cienaCesGmplsStaticIngressUniDirTunnelDestIpAddr,
       "cienaCesGmplsStaticIngressUniDirTunnelAdminState": cienaCesGmplsStaticIngressUniDirTunnelAdminState,
       "cienaCesGmplsStaticIngressUniDirTunnelOperState": cienaCesGmplsStaticIngressUniDirTunnelOperState,
       "cienaCesGmplsStaticIngressUniDirTunnelForwardOutLabel": cienaCesGmplsStaticIngressUniDirTunnelForwardOutLabel,
       "cienaCesGmplsStaticIngressUniDirTunnelProtectionRole": cienaCesGmplsStaticIngressUniDirTunnelProtectionRole,
       "cienaCesGmplsStaticIngressUniDirTunnelProtectionPartnerName": cienaCesGmplsStaticIngressUniDirTunnelProtectionPartnerName,
       "cienaCesGmplsStaticIngressUniDirTunnelProtectionState": cienaCesGmplsStaticIngressUniDirTunnelProtectionState,
       "cienaCesGmplsStaticIngressUniDirTunnelTTLPolicy": cienaCesGmplsStaticIngressUniDirTunnelTTLPolicy,
       "cienaCesGmplsStaticIngressUniDirTunnelFixedTTL": cienaCesGmplsStaticIngressUniDirTunnelFixedTTL,
       "cienaCesGmplsStaticIngressUniDirTunnelGrpIndex": cienaCesGmplsStaticIngressUniDirTunnelGrpIndex,
       "cienaCesGmplsStaticIngressUniDirTunnelReversion": cienaCesGmplsStaticIngressUniDirTunnelReversion,
       "cienaCesGmplsStaticIngressUniDirTunnelReversionTimeout": cienaCesGmplsStaticIngressUniDirTunnelReversionTimeout,
       "cienaCesGmplsStaticIngressUniDirTunnelCosProfileIndex": cienaCesGmplsStaticIngressUniDirTunnelCosProfileIndex,
       "cienaCesGmplsStaticIngressUniDirTunnelCosProfileName": cienaCesGmplsStaticIngressUniDirTunnelCosProfileName,
       "cienaCesGmplsStaticIngressUniDirTunnelRecoveryDisjoint": cienaCesGmplsStaticIngressUniDirTunnelRecoveryDisjoint,
       "cienaCesGmplsStaticIngressCoroutedTunnelTable": cienaCesGmplsStaticIngressCoroutedTunnelTable,
       "cienaCesGmplsStaticIngressCoroutedTunnelEntry": cienaCesGmplsStaticIngressCoroutedTunnelEntry,
       "cienaCesGmplsStaticIngressCoroutedTunnelIndex": cienaCesGmplsStaticIngressCoroutedTunnelIndex,
       "cienaCesGmplsStaticIngressCoroutedTunnelName": cienaCesGmplsStaticIngressCoroutedTunnelName,
       "cienaCesGmplsStaticIngressCoroutedTunnelNextHopIp": cienaCesGmplsStaticIngressCoroutedTunnelNextHopIp,
       "cienaCesGmplsStaticIngressCoroutedTunnelSrcIpAddr": cienaCesGmplsStaticIngressCoroutedTunnelSrcIpAddr,
       "cienaCesGmplsStaticIngressCoroutedTunnelDestIpAddr": cienaCesGmplsStaticIngressCoroutedTunnelDestIpAddr,
       "cienaCesGmplsStaticIngressCoroutedTunnelAdminState": cienaCesGmplsStaticIngressCoroutedTunnelAdminState,
       "cienaCesGmplsStaticIngressCoroutedTunnelOperState": cienaCesGmplsStaticIngressCoroutedTunnelOperState,
       "cienaCesGmplsStaticIngressCoroutedTunnelForwardOutLabel": cienaCesGmplsStaticIngressCoroutedTunnelForwardOutLabel,
       "cienaCesGmplsStaticIngressCoroutedTunnelReverseInLabel": cienaCesGmplsStaticIngressCoroutedTunnelReverseInLabel,
       "cienaCesGmplsStaticIngressCoroutedTunnelProtectionRole": cienaCesGmplsStaticIngressCoroutedTunnelProtectionRole,
       "cienaCesGmplsStaticIngressCoroutedTunnelProtectionPartnerName": cienaCesGmplsStaticIngressCoroutedTunnelProtectionPartnerName,
       "cienaCesGmplsStaticIngressCoroutedTunnelProtectionState": cienaCesGmplsStaticIngressCoroutedTunnelProtectionState,
       "cienaCesGmplsStaticIngressCoroutedTunnelTTLPolicy": cienaCesGmplsStaticIngressCoroutedTunnelTTLPolicy,
       "cienaCesGmplsStaticIngressCoroutedTunnelFixedTTL": cienaCesGmplsStaticIngressCoroutedTunnelFixedTTL,
       "cienaCesGmplsStaticIngressCoroutedTunnelGrpIndex": cienaCesGmplsStaticIngressCoroutedTunnelGrpIndex,
       "cienaCesGmplsStaticIngressCoroutedTunnelReversion": cienaCesGmplsStaticIngressCoroutedTunnelReversion,
       "cienaCesGmplsStaticIngressCoroutedTunnelReversionTimeout": cienaCesGmplsStaticIngressCoroutedTunnelReversionTimeout,
       "cienaCesGmplsStaticIngressCoroutedTunnelCosProfileIndex": cienaCesGmplsStaticIngressCoroutedTunnelCosProfileIndex,
       "cienaCesGmplsStaticIngressCoroutedTunnelCosProfileName": cienaCesGmplsStaticIngressCoroutedTunnelCosProfileName,
       "cienaCesGmplsStaticIngressCoroutedTunnelBfdMonitoring": cienaCesGmplsStaticIngressCoroutedTunnelBfdMonitoring,
       "cienaCesGmplsStaticIngressCoroutedTunnelBfdProfileName": cienaCesGmplsStaticIngressCoroutedTunnelBfdProfileName,
       "cienaCesGmplsStaticIngressCoroutedTunnelBfdSessionName": cienaCesGmplsStaticIngressCoroutedTunnelBfdSessionName,
       "cienaCesGmplsStaticIngressCoroutedTunnelAisMonitoring": cienaCesGmplsStaticIngressCoroutedTunnelAisMonitoring,
       "cienaCesGmplsStaticIngressCoroutedTunnelAisProfileName": cienaCesGmplsStaticIngressCoroutedTunnelAisProfileName,
       "cienaCesGmplsStaticIngressCoroutedTunnelBfdSessionFaulted": cienaCesGmplsStaticIngressCoroutedTunnelBfdSessionFaulted,
       "cienaCesGmplsStaticIngressCoroutedTunnelBfdProfileIndex": cienaCesGmplsStaticIngressCoroutedTunnelBfdProfileIndex,
       "cienaCesGmplsStaticIngressCoroutedTunnelRecoveryDisjoint": cienaCesGmplsStaticIngressCoroutedTunnelRecoveryDisjoint,
       "cienaCesGmplsStaticIngressCoroutedTunnelNextHopIfNum": cienaCesGmplsStaticIngressCoroutedTunnelNextHopIfNum,
       "cienaCesGmplsStaticIngressCoroutedTunnelLspId": cienaCesGmplsStaticIngressCoroutedTunnelLspId,
       "cienaCesGmplsStaticIngressCoroutedTunnelSrcTunnelId": cienaCesGmplsStaticIngressCoroutedTunnelSrcTunnelId,
       "cienaCesGmplsStaticIngressCoroutedTunnelDestTunnelId": cienaCesGmplsStaticIngressCoroutedTunnelDestTunnelId,
       "cienaCesGmplsDynamicIngressUniDirTunnelTable": cienaCesGmplsDynamicIngressUniDirTunnelTable,
       "cienaCesGmplsDynamicIngressUniDirTunnelEntry": cienaCesGmplsDynamicIngressUniDirTunnelEntry,
       "cienaCesGmplsDynamicIngressUniDirTunnelIndex": cienaCesGmplsDynamicIngressUniDirTunnelIndex,
       "cienaCesGmplsDynamicIngressUniDirTunnelName": cienaCesGmplsDynamicIngressUniDirTunnelName,
       "cienaCesMplsDynamicIngressUniDirTunnelLspId": cienaCesMplsDynamicIngressUniDirTunnelLspId,
       "cienaCesGmplsDynamicIngressUniDirTunnelNextHopIp": cienaCesGmplsDynamicIngressUniDirTunnelNextHopIp,
       "cienaCesGmplsDynamicIngressUniDirTunnelSrcIpAddr": cienaCesGmplsDynamicIngressUniDirTunnelSrcIpAddr,
       "cienaCesGmplsDynamicIngressUniDirTunnelDestIpAddr": cienaCesGmplsDynamicIngressUniDirTunnelDestIpAddr,
       "cienaCesGmplsDynamicIngressUniDirTunnelAdminState": cienaCesGmplsDynamicIngressUniDirTunnelAdminState,
       "cienaCesGmplsDynamicIngressUniDirTunnelOperState": cienaCesGmplsDynamicIngressUniDirTunnelOperState,
       "cienaCesGmplsDynamicIngressUniDirTunnelForwardOutLabel": cienaCesGmplsDynamicIngressUniDirTunnelForwardOutLabel,
       "cienaCesGmplsDynamicIngressUniDirTunnelProtectionRole": cienaCesGmplsDynamicIngressUniDirTunnelProtectionRole,
       "cienaCesGmplsDynamicIngressUniDirTunnelProtectionPartnerName": cienaCesGmplsDynamicIngressUniDirTunnelProtectionPartnerName,
       "cienaCesGmplsDynamicIngressUniDirTunnelProtectionState": cienaCesGmplsDynamicIngressUniDirTunnelProtectionState,
       "cienaCesGmplsDynamicIngressUniDirTunnelTTLPolicy": cienaCesGmplsDynamicIngressUniDirTunnelTTLPolicy,
       "cienaCesGmplsDynamicIngressUniDirTunnelFixedTTL": cienaCesGmplsDynamicIngressUniDirTunnelFixedTTL,
       "cienaCesGmplsDynamicIngressUniDirTunnelGrpIndex": cienaCesGmplsDynamicIngressUniDirTunnelGrpIndex,
       "cienaCesGmplsDynamicIngressUniDirTunnelReversion": cienaCesGmplsDynamicIngressUniDirTunnelReversion,
       "cienaCesGmplsDynamicIngressUniDirTunnelReversionTimeout": cienaCesGmplsDynamicIngressUniDirTunnelReversionTimeout,
       "cienaCesGmplsDynamicIngressUniDirTunnelCosProfileIndex": cienaCesGmplsDynamicIngressUniDirTunnelCosProfileIndex,
       "cienaCesGmplsDynamicIngressUniDirTunnelCosProfileName": cienaCesGmplsDynamicIngressUniDirTunnelCosProfileName,
       "cienaCesGmplsDynamicIngressUniDirTunnelRecordRoute": cienaCesGmplsDynamicIngressUniDirTunnelRecordRoute,
       "cienaCesGmplsDynamicIngressUniDirTunnelFastRoute": cienaCesGmplsDynamicIngressUniDirTunnelFastRoute,
       "cienaCesGmplsDynamicIngressUniDirTunnelSetupPriority": cienaCesGmplsDynamicIngressUniDirTunnelSetupPriority,
       "cienaCesGmplsDynamicIngressUniDirTunnelHoldPriority": cienaCesGmplsDynamicIngressUniDirTunnelHoldPriority,
       "cienaCesGmplsDynamicIngressUniDirTunnelPathIndex": cienaCesGmplsDynamicIngressUniDirTunnelPathIndex,
       "cienaCesGmplsDynamicIngressUniDirTunnelPathName": cienaCesGmplsDynamicIngressUniDirTunnelPathName,
       "cienaCesGmplsDynamicIngressUniDirTunnelBandwidthProfile": cienaCesGmplsDynamicIngressUniDirTunnelBandwidthProfile,
       "cienaCesGmplsDynamicIngressUniDirTunnelResourcePointer": cienaCesGmplsDynamicIngressUniDirTunnelResourcePointer,
       "cienaCesGmplsDynamicIngressCoroutedTunnelTable": cienaCesGmplsDynamicIngressCoroutedTunnelTable,
       "cienaCesGmplsDynamicIngressCoroutedTunnelEntry": cienaCesGmplsDynamicIngressCoroutedTunnelEntry,
       "cienaCesGmplsDynamicIngressCoroutedTunnelIndex": cienaCesGmplsDynamicIngressCoroutedTunnelIndex,
       "cienaCesGmplsDynamicIngressCoroutedTunnelName": cienaCesGmplsDynamicIngressCoroutedTunnelName,
       "cienaCesGmplsDynamicIngressCoroutedTunnelNextHopIp": cienaCesGmplsDynamicIngressCoroutedTunnelNextHopIp,
       "cienaCesGmplsDynamicIngressCoroutedTunnelSrcIpAddr": cienaCesGmplsDynamicIngressCoroutedTunnelSrcIpAddr,
       "cienaCesGmplsDynamicIngressCoroutedTunnelDestIpAddr": cienaCesGmplsDynamicIngressCoroutedTunnelDestIpAddr,
       "cienaCesGmplsDynamicIngressCoroutedTunnelAdminState": cienaCesGmplsDynamicIngressCoroutedTunnelAdminState,
       "cienaCesGmplsDynamicIngressCoroutedTunnelOperState": cienaCesGmplsDynamicIngressCoroutedTunnelOperState,
       "cienaCesGmplsDynamicIngressCoroutedTunnelForwardOutLabel": cienaCesGmplsDynamicIngressCoroutedTunnelForwardOutLabel,
       "cienaCesGmplsDynamicIngressCoroutedTunnelReverseInLabel": cienaCesGmplsDynamicIngressCoroutedTunnelReverseInLabel,
       "cienaCesGmplsDynamicIngressCoroutedTunnelProtectionRole": cienaCesGmplsDynamicIngressCoroutedTunnelProtectionRole,
       "cienaCesGmplsDynamicIngressCoroutedTunnelProtectionPartnerName": cienaCesGmplsDynamicIngressCoroutedTunnelProtectionPartnerName,
       "cienaCesGmplsDynamicIngressCoroutedTunnelProtectionState": cienaCesGmplsDynamicIngressCoroutedTunnelProtectionState,
       "cienaCesGmplsDynamicIngressCoroutedTunnelTTLPolicy": cienaCesGmplsDynamicIngressCoroutedTunnelTTLPolicy,
       "cienaCesGmplsDynamicIngressCoroutedTunnelFixedTTL": cienaCesGmplsDynamicIngressCoroutedTunnelFixedTTL,
       "cienaCesGmplsDynamicIngressCoroutedTunnelGrpIndex": cienaCesGmplsDynamicIngressCoroutedTunnelGrpIndex,
       "cienaCesGmplsDynamicIngressCoroutedTunnelReversion": cienaCesGmplsDynamicIngressCoroutedTunnelReversion,
       "cienaCesGmplsDynamicIngressCoroutedTunnelReversionTimeout": cienaCesGmplsDynamicIngressCoroutedTunnelReversionTimeout,
       "cienaCesGmplsDynamicIngressCoroutedTunnelCosProfileIndex": cienaCesGmplsDynamicIngressCoroutedTunnelCosProfileIndex,
       "cienaCesGmplsDynamicIngressCoroutedTunnelCosProfileName": cienaCesGmplsDynamicIngressCoroutedTunnelCosProfileName,
       "cienaCesGmplsDynamicIngressCoroutedTunnelRecordRoute": cienaCesGmplsDynamicIngressCoroutedTunnelRecordRoute,
       "cienaCesGmplsDynamicIngressCoroutedTunnelFastRoute": cienaCesGmplsDynamicIngressCoroutedTunnelFastRoute,
       "cienaCesGmplsDynamicIngressCoroutedTunnelSetupPriority": cienaCesGmplsDynamicIngressCoroutedTunnelSetupPriority,
       "cienaCesGmplsDynamicIngressCoroutedTunnelHoldPriority": cienaCesGmplsDynamicIngressCoroutedTunnelHoldPriority,
       "cienaCesGmplsDynamicIngressCoroutedTunnelPathIndex": cienaCesGmplsDynamicIngressCoroutedTunnelPathIndex,
       "cienaCesGmplsDynamicIngressCoroutedTunnelPathName": cienaCesGmplsDynamicIngressCoroutedTunnelPathName,
       "cienaCesGmplsDynamicIngressCoroutedTunnelBandwidthProfile": cienaCesGmplsDynamicIngressCoroutedTunnelBandwidthProfile,
       "cienaCesGmplsDynamicIngressCoroutedTunnelResourcePointer": cienaCesGmplsDynamicIngressCoroutedTunnelResourcePointer,
       "cienaCesGmplsDynamicIngressCoroutedTunnelBfdMonitoring": cienaCesGmplsDynamicIngressCoroutedTunnelBfdMonitoring,
       "cienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileName": cienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileName,
       "cienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionName": cienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionName,
       "cienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionFaulted": cienaCesGmplsDynamicIngressCoroutedTunnelBfdSessionFaulted,
       "cienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileIndex": cienaCesGmplsDynamicIngressCoroutedTunnelBfdProfileIndex,
       "cienaCesGmplsDynamicIngressCoroutedTunnelAutoBackupEnable": cienaCesGmplsDynamicIngressCoroutedTunnelAutoBackupEnable,
       "cienaCesGmplsDynamicIngressCoroutedTunnelLspReoptimization": cienaCesGmplsDynamicIngressCoroutedTunnelLspReoptimization,
       "cienaCesGmplsDynamicIngressCoroutedTunnelLspReOptTimeInterval": cienaCesGmplsDynamicIngressCoroutedTunnelLspReOptTimeInterval,
       "cienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointType": cienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointType,
       "cienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointMode": cienaCesGmplsDynamicIngressCoroutedTunnelPathDisjointMode,
       "cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeEnable": cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeEnable,
       "cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeInterval": cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeInterval,
       "cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeFailureHdlr": cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeFailureHdlr,
       "cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeState": cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeState,
       "cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeMode": cienaCesGmplsDynamicIngressCoroutedTunnelAutoSizeMode,
       "cienaCesGmplsDynamicIngressCoroutedTunnelMinBandwidth": cienaCesGmplsDynamicIngressCoroutedTunnelMinBandwidth,
       "cienaCesGmplsDynamicIngressCoroutedTunnelMaxBandwidth": cienaCesGmplsDynamicIngressCoroutedTunnelMaxBandwidth,
       "cienaCesGmplsDynamicIngressCoroutedTunnelIncBandwidth": cienaCesGmplsDynamicIngressCoroutedTunnelIncBandwidth,
       "cienaCesGmplsDynamicIngressCoroutedTunnelCurBandwidth": cienaCesGmplsDynamicIngressCoroutedTunnelCurBandwidth,
       "cienaCesGmplsDynamicIngressCoroutedTunnelReqBandwidth": cienaCesGmplsDynamicIngressCoroutedTunnelReqBandwidth,
       "cienaCesGmplsDynamicIngressCoroutedTunnelUsedBandwidth": cienaCesGmplsDynamicIngressCoroutedTunnelUsedBandwidth,
       "cienaCesGmplsDynamicIngressCoroutedTunnelClassType": cienaCesGmplsDynamicIngressCoroutedTunnelClassType,
       "cienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAll": cienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAll,
       "cienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAny": cienaCesGmplsDynamicIngressCoroutedTunnelResourceIncludeAny,
       "cienaCesGmplsDynamicIngressCoroutedTunnelResourceExcludeAny": cienaCesGmplsDynamicIngressCoroutedTunnelResourceExcludeAny,
       "cienaCesGmplsDynamicIngressCoroutedLspId": cienaCesGmplsDynamicIngressCoroutedLspId,
       "cienaCesGmplsStaticEgressUniDirTunnelTable": cienaCesGmplsStaticEgressUniDirTunnelTable,
       "cienaCesGmplsStaticEgressUniDirTunnelEntry": cienaCesGmplsStaticEgressUniDirTunnelEntry,
       "cienaCesGmplsStaticEgressUniDirTunnelIndex": cienaCesGmplsStaticEgressUniDirTunnelIndex,
       "cienaCesGmplsStaticEgressUniDirTunnelName": cienaCesGmplsStaticEgressUniDirTunnelName,
       "cienaCesGmplsStaticEgressUniDirTunnelAdminState": cienaCesGmplsStaticEgressUniDirTunnelAdminState,
       "cienaCesGmplsStaticEgressUniDirTunnelOperState": cienaCesGmplsStaticEgressUniDirTunnelOperState,
       "cienaCesGmplsStaticEgressUniDirTunnelPrevHopIpAddr": cienaCesGmplsStaticEgressUniDirTunnelPrevHopIpAddr,
       "cienaCesGmplsStaticEgressUniDirTunnelSourceIpAddr": cienaCesGmplsStaticEgressUniDirTunnelSourceIpAddr,
       "cienaCesGmplsStaticEgressUniDirTunnelDestIpAddr": cienaCesGmplsStaticEgressUniDirTunnelDestIpAddr,
       "cienaCesGmplsStaticEgressUniDirTunnelForwardInLabel": cienaCesGmplsStaticEgressUniDirTunnelForwardInLabel,
       "cienaCesGmplsStaticEgressCoroutedTunnelTable": cienaCesGmplsStaticEgressCoroutedTunnelTable,
       "cienaCesGmplsStaticEgressCoroutedTunnelEntry": cienaCesGmplsStaticEgressCoroutedTunnelEntry,
       "cienaCesGmplsStaticEgressCoroutedTunnelIndex": cienaCesGmplsStaticEgressCoroutedTunnelIndex,
       "cienaCesGmplsStaticEgressCoroutedTunnelName": cienaCesGmplsStaticEgressCoroutedTunnelName,
       "cienaCesGmplsStaticEgressCoroutedTunnelAdminState": cienaCesGmplsStaticEgressCoroutedTunnelAdminState,
       "cienaCesGmplsStaticEgressCoroutedTunnelOperState": cienaCesGmplsStaticEgressCoroutedTunnelOperState,
       "cienaCesGmplsStaticEgressCoroutedTunnelPrevHopIpAddr": cienaCesGmplsStaticEgressCoroutedTunnelPrevHopIpAddr,
       "cienaCesGmplsStaticEgressCoroutedTunnelSourceIpAddr": cienaCesGmplsStaticEgressCoroutedTunnelSourceIpAddr,
       "cienaCesGmplsStaticEgressCoroutedTunnelDestIpAddr": cienaCesGmplsStaticEgressCoroutedTunnelDestIpAddr,
       "cienaCesGmplsStaticEgressCoroutedTunnelForwardInLabel": cienaCesGmplsStaticEgressCoroutedTunnelForwardInLabel,
       "cienaCesGmplsStaticEgressCoroutedTunnelReverseOutLabel": cienaCesGmplsStaticEgressCoroutedTunnelReverseOutLabel,
       "cienaCesGmplsStaticEgressCoroutedTunnelProtectionRole": cienaCesGmplsStaticEgressCoroutedTunnelProtectionRole,
       "cienaCesGmplsStaticEgressCoroutedTunnelProtectionPartnerName": cienaCesGmplsStaticEgressCoroutedTunnelProtectionPartnerName,
       "cienaCesGmplsStaticEgressCoroutedTunnelProtectionState": cienaCesGmplsStaticEgressCoroutedTunnelProtectionState,
       "cienaCesGmplsStaticEgressCoroutedTunnelGrpIndex": cienaCesGmplsStaticEgressCoroutedTunnelGrpIndex,
       "cienaCesGmplsStaticEgressCoroutedTunnelReversion": cienaCesGmplsStaticEgressCoroutedTunnelReversion,
       "cienaCesGmplsStaticEgressCoroutedTunnelReversionTimeout": cienaCesGmplsStaticEgressCoroutedTunnelReversionTimeout,
       "cienaCesGmplsStaticEgressCoroutedTunnelCosProfileIndex": cienaCesGmplsStaticEgressCoroutedTunnelCosProfileIndex,
       "cienaCesGmplsStaticEgressCoroutedTunnelCosProfileName": cienaCesGmplsStaticEgressCoroutedTunnelCosProfileName,
       "cienaCesGmplsStaticEgressCoroutedTunnelBfdMonitoring": cienaCesGmplsStaticEgressCoroutedTunnelBfdMonitoring,
       "cienaCesGmplsStaticEgressCoroutedTunnelBfdProfileName": cienaCesGmplsStaticEgressCoroutedTunnelBfdProfileName,
       "cienaCesGmplsStaticEgressCoroutedTunnelBfdSessionName": cienaCesGmplsStaticEgressCoroutedTunnelBfdSessionName,
       "cienaCesGmplsStaticEgressCoroutedTunnelAisMonitoring": cienaCesGmplsStaticEgressCoroutedTunnelAisMonitoring,
       "cienaCesGmplsStaticEgressCoroutedTunnelAisProfileName": cienaCesGmplsStaticEgressCoroutedTunnelAisProfileName,
       "cienaCesGmplsStaticEgressCoroutedTunnelBfdSessionFaulted": cienaCesGmplsStaticEgressCoroutedTunnelBfdSessionFaulted,
       "cienaCesGmplsStaticEgressCoroutedTunnelBfdProfileIndex": cienaCesGmplsStaticEgressCoroutedTunnelBfdProfileIndex,
       "cienaCesGmplsStaticEgressCoroutedTunnelRecoveryDisjoint": cienaCesGmplsStaticEgressCoroutedTunnelRecoveryDisjoint,
       "cienaCesGmplsStaticEgressCoroutedTunnelTTLPolicy": cienaCesGmplsStaticEgressCoroutedTunnelTTLPolicy,
       "cienaCesGmplsStaticEgressCoroutedTunnelFixedTTL": cienaCesGmplsStaticEgressCoroutedTunnelFixedTTL,
       "cienaCesGmplsStaticEgressCoroutedTunnelPrevHopIfNum": cienaCesGmplsStaticEgressCoroutedTunnelPrevHopIfNum,
       "cienaCesGmplsStaticEgressCoroutedTunnelLspId": cienaCesGmplsStaticEgressCoroutedTunnelLspId,
       "cienaCesGmplsStaticEgressCoroutedTunnelSrcTunnelId": cienaCesGmplsStaticEgressCoroutedTunnelSrcTunnelId,
       "cienaCesGmplsStaticEgressCoroutedTunnelDestTunnelId": cienaCesGmplsStaticEgressCoroutedTunnelDestTunnelId,
       "cienaCesGmplsDynamicEgressUniDirTunnelTable": cienaCesGmplsDynamicEgressUniDirTunnelTable,
       "cienaCesGmplsDynamicEgressUniDirTunnelEntry": cienaCesGmplsDynamicEgressUniDirTunnelEntry,
       "cienaCesGmplsDynamicEgressUniDirTunnelIndex": cienaCesGmplsDynamicEgressUniDirTunnelIndex,
       "cienaCesGmplsDynamicEgressUniDirTunnelName": cienaCesGmplsDynamicEgressUniDirTunnelName,
       "cienaCesGmplsDynamicEgressUniDirTunnelAdminState": cienaCesGmplsDynamicEgressUniDirTunnelAdminState,
       "cienaCesGmplsDynamicEgressUniDirTunnelOperState": cienaCesGmplsDynamicEgressUniDirTunnelOperState,
       "cienaCesGmplsDynamicEgressUniDirLspId": cienaCesGmplsDynamicEgressUniDirLspId,
       "cienaCesGmplsDynamicEgressUniDirTunnelPrevHopIpAddr": cienaCesGmplsDynamicEgressUniDirTunnelPrevHopIpAddr,
       "cienaCesGmplsDynamicEgressUniDirTunnelSourceIpAddr": cienaCesGmplsDynamicEgressUniDirTunnelSourceIpAddr,
       "cienaCesGmplsDynamicEgressUniDirTunnelDestIpAddr": cienaCesGmplsDynamicEgressUniDirTunnelDestIpAddr,
       "cienaCesGmplsDynamicEgressUniDirTunnelForwardInLabel": cienaCesGmplsDynamicEgressUniDirTunnelForwardInLabel,
       "cienaCesGmplsDynamicEgressCoroutedTunnelTable": cienaCesGmplsDynamicEgressCoroutedTunnelTable,
       "cienaCesGmplsDynamicEgressCoroutedTunnelEntry": cienaCesGmplsDynamicEgressCoroutedTunnelEntry,
       "cienaCesGmplsDynamicEgressCoroutedTunnelIndex": cienaCesGmplsDynamicEgressCoroutedTunnelIndex,
       "cienaCesGmplsDynamicEgressCoroutedTunnelName": cienaCesGmplsDynamicEgressCoroutedTunnelName,
       "cienaCesGmplsDynamicEgressCoroutedTunnelAdminState": cienaCesGmplsDynamicEgressCoroutedTunnelAdminState,
       "cienaCesGmplsDynamicEgressCoroutedTunnelOperState": cienaCesGmplsDynamicEgressCoroutedTunnelOperState,
       "cienaCesGmplsDynamicEgressCoroutedLspId": cienaCesGmplsDynamicEgressCoroutedLspId,
       "cienaCesGmplsDynamicEgressCoroutedTunnelPrevHopIpAddr": cienaCesGmplsDynamicEgressCoroutedTunnelPrevHopIpAddr,
       "cienaCesGmplsDynamicEgressCoroutedTunnelSourceIpAddr": cienaCesGmplsDynamicEgressCoroutedTunnelSourceIpAddr,
       "cienaCesGmplsDynamicEgressCoroutedTunnelDestIpAddr": cienaCesGmplsDynamicEgressCoroutedTunnelDestIpAddr,
       "cienaCesGmplsDynamicEgressCoroutedTunnelForwardInLabel": cienaCesGmplsDynamicEgressCoroutedTunnelForwardInLabel,
       "cienaCesGmplsDynamicEgressCoroutedTunnelReverseOutLabel": cienaCesGmplsDynamicEgressCoroutedTunnelReverseOutLabel,
       "cienaCesGmplsDynamicEgressCoroutedTunnelProtectionRole": cienaCesGmplsDynamicEgressCoroutedTunnelProtectionRole,
       "cienaCesGmplsDynamicEgressCoroutedTunnelProtectionPartnerName": cienaCesGmplsDynamicEgressCoroutedTunnelProtectionPartnerName,
       "cienaCesGmplsDynamicEgressCoroutedTunnelProtectionState": cienaCesGmplsDynamicEgressCoroutedTunnelProtectionState,
       "cienaCesGmplsDynamicEgressCoroutedTunnelGrpIndex": cienaCesGmplsDynamicEgressCoroutedTunnelGrpIndex,
       "cienaCesGmplsDynamicEgressCoroutedTunnelReversion": cienaCesGmplsDynamicEgressCoroutedTunnelReversion,
       "cienaCesGmplsDynamicEgressCoroutedTunnelReversionTimeout": cienaCesGmplsDynamicEgressCoroutedTunnelReversionTimeout,
       "cienaCesGmplsDynamicEgressCoroutedTunnelCosProfileIndex": cienaCesGmplsDynamicEgressCoroutedTunnelCosProfileIndex,
       "cienaCesGmplsDynamicEgressCoroutedTunnelCosProfileName": cienaCesGmplsDynamicEgressCoroutedTunnelCosProfileName,
       "cienaCesGmplsDynamicEgressCoroutedTunnelBfdMonitoring": cienaCesGmplsDynamicEgressCoroutedTunnelBfdMonitoring,
       "cienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileName": cienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileName,
       "cienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionName": cienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionName,
       "cienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionFaulted": cienaCesGmplsDynamicEgressCoroutedTunnelBfdSessionFaulted,
       "cienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileIndex": cienaCesGmplsDynamicEgressCoroutedTunnelBfdProfileIndex,
       "cienaCesGmplsDynamicEgressCoroutedTunnelTTLPolicy": cienaCesGmplsDynamicEgressCoroutedTunnelTTLPolicy,
       "cienaCesGmplsDynamicEgressCoroutedTunnelFixedTTL": cienaCesGmplsDynamicEgressCoroutedTunnelFixedTTL,
       "cienaCesGmplsStaticTransitUniDirTunnelTable": cienaCesGmplsStaticTransitUniDirTunnelTable,
       "cienaCesGmplsStaticTransitUniDirTunnelEntry": cienaCesGmplsStaticTransitUniDirTunnelEntry,
       "cienaCesGmplsStaticTransitUniDirTunnelIndex": cienaCesGmplsStaticTransitUniDirTunnelIndex,
       "cienaCesGmplsStaticTransitUniDirTunnelName": cienaCesGmplsStaticTransitUniDirTunnelName,
       "cienaCesGmplsStaticTransitUniDirTunnelAdminState": cienaCesGmplsStaticTransitUniDirTunnelAdminState,
       "cienaCesGmplsStaticTransitUniDirTunnelOperState": cienaCesGmplsStaticTransitUniDirTunnelOperState,
       "cienaCesGmplsStaticTransitUniDirTunnelSourceIpAddr": cienaCesGmplsStaticTransitUniDirTunnelSourceIpAddr,
       "cienaCesGmplsStaticTransitUniDirTunnelDestIpAddr": cienaCesGmplsStaticTransitUniDirTunnelDestIpAddr,
       "cienaCesGmplsStaticTransitUniDirTunnelNextHopIpAddr": cienaCesGmplsStaticTransitUniDirTunnelNextHopIpAddr,
       "cienaCesGmplsStaticTransitUniDirTunnelPrevHopIpAddr": cienaCesGmplsStaticTransitUniDirTunnelPrevHopIpAddr,
       "cienaCesGmplsStaticTransitUniDirTunnelForwardInLabel": cienaCesGmplsStaticTransitUniDirTunnelForwardInLabel,
       "cienaCesGmplsStaticTransitUniDirTunnelForwardOutLabel": cienaCesGmplsStaticTransitUniDirTunnelForwardOutLabel,
       "cienaCesGmplsStaticTransitUniDirTunnelTTLPolicy": cienaCesGmplsStaticTransitUniDirTunnelTTLPolicy,
       "cienaCesGmplsStaticTransitUniDirTunnelFixedTTL": cienaCesGmplsStaticTransitUniDirTunnelFixedTTL,
       "cienaCesGmplsStaticTransitUniDirTunnelCosProfileIndex": cienaCesGmplsStaticTransitUniDirTunnelCosProfileIndex,
       "cienaCesGmplsStaticTransitUniDirTunnelCosProfileName": cienaCesGmplsStaticTransitUniDirTunnelCosProfileName,
       "cienaCesGmplsStaticTransitUniDirTunnelAisMonitoring": cienaCesGmplsStaticTransitUniDirTunnelAisMonitoring,
       "cienaCesGmplsStaticTransitUniDirTunnelAisProfileName": cienaCesGmplsStaticTransitUniDirTunnelAisProfileName,
       "cienaCesGmplsStaticTransitUniDirTunnelIncomingPackets": cienaCesGmplsStaticTransitUniDirTunnelIncomingPackets,
       "cienaCesGmplsStaticTransitUniDirTunnelOutgoingPackets": cienaCesGmplsStaticTransitUniDirTunnelOutgoingPackets,
       "cienaCesGmplsStaticTransitUniDirTunnelIncomingBytes": cienaCesGmplsStaticTransitUniDirTunnelIncomingBytes,
       "cienaCesGmplsStaticTransitUniDirTunnelOutgoingBytes": cienaCesGmplsStaticTransitUniDirTunnelOutgoingBytes,
       "cienaCesGmplsStaticTransitCoroutedTunnelTable": cienaCesGmplsStaticTransitCoroutedTunnelTable,
       "cienaCesGmplsStaticTransitCoroutedTunnelEntry": cienaCesGmplsStaticTransitCoroutedTunnelEntry,
       "cienaCesGmplsStaticTransitCoroutedTunnelIndex": cienaCesGmplsStaticTransitCoroutedTunnelIndex,
       "cienaCesGmplsStaticTransitCoroutedTunnelName": cienaCesGmplsStaticTransitCoroutedTunnelName,
       "cienaCesGmplsStaticTransitCoroutedTunnelAdminState": cienaCesGmplsStaticTransitCoroutedTunnelAdminState,
       "cienaCesGmplsStaticTransitCoroutedTunnelOperState": cienaCesGmplsStaticTransitCoroutedTunnelOperState,
       "cienaCesGmplsStaticTransitCoroutedTunnelSourceIpAddr": cienaCesGmplsStaticTransitCoroutedTunnelSourceIpAddr,
       "cienaCesGmplsStaticTransitCoroutedTunnelDestIpAddr": cienaCesGmplsStaticTransitCoroutedTunnelDestIpAddr,
       "cienaCesGmplsStaticTransitCoroutedTunnelNextHopIpAddr": cienaCesGmplsStaticTransitCoroutedTunnelNextHopIpAddr,
       "cienaCesGmplsStaticTransitCoroutedTunnelPrevHopIpAddr": cienaCesGmplsStaticTransitCoroutedTunnelPrevHopIpAddr,
       "cienaCesGmplsStaticTransitCoroutedTunnelForwardInLabel": cienaCesGmplsStaticTransitCoroutedTunnelForwardInLabel,
       "cienaCesGmplsStaticTransitCoroutedTunnelForwardOutLabel": cienaCesGmplsStaticTransitCoroutedTunnelForwardOutLabel,
       "cienaCesGmplsStaticTransitCoroutedTunnelReverseInLabel": cienaCesGmplsStaticTransitCoroutedTunnelReverseInLabel,
       "cienaCesGmplsStaticTransitCoroutedTunnelReverseOutLabel": cienaCesGmplsStaticTransitCoroutedTunnelReverseOutLabel,
       "cienaCesGmplsStaticTransitCoroutedTunnelTTLPolicy": cienaCesGmplsStaticTransitCoroutedTunnelTTLPolicy,
       "cienaCesGmplsStaticTransitCoroutedTunnelFixedTTL": cienaCesGmplsStaticTransitCoroutedTunnelFixedTTL,
       "cienaCesGmplsStaticTransitCoroutedTunnelCosProfileIndex": cienaCesGmplsStaticTransitCoroutedTunnelCosProfileIndex,
       "cienaCesGmplsStaticTransitCoroutedTunnelCosProfileName": cienaCesGmplsStaticTransitCoroutedTunnelCosProfileName,
       "cienaCesGmplsStaticTransitCoroutedTunnelAisMonitoring": cienaCesGmplsStaticTransitCoroutedTunnelAisMonitoring,
       "cienaCesGmplsStaticTransitCoroutedTunnelAisProfileName": cienaCesGmplsStaticTransitCoroutedTunnelAisProfileName,
       "cienaCesGmplsStaticTransitCoroutedTunnelPrevHopIfNum": cienaCesGmplsStaticTransitCoroutedTunnelPrevHopIfNum,
       "cienaCesGmplsStaticTransitCoroutedTunnelNextHopIfNum": cienaCesGmplsStaticTransitCoroutedTunnelNextHopIfNum,
       "cienaCesGmplsStaticTransitCoroutedTunnelLspId": cienaCesGmplsStaticTransitCoroutedTunnelLspId,
       "cienaCesGmplsStaticTransitCoroutedTunnelSrcTunnelId": cienaCesGmplsStaticTransitCoroutedTunnelSrcTunnelId,
       "cienaCesGmplsStaticTransitCoroutedTunnelDestTunnelId": cienaCesGmplsStaticTransitCoroutedTunnelDestTunnelId,
       "cienaCesGmplsStaticTransitCoroutedTunnelIncomingPackets": cienaCesGmplsStaticTransitCoroutedTunnelIncomingPackets,
       "cienaCesGmplsStaticTransitCoroutedTunnelOutgoingPackets": cienaCesGmplsStaticTransitCoroutedTunnelOutgoingPackets,
       "cienaCesGmplsStaticTransitCoroutedTunnelIncomingBytes": cienaCesGmplsStaticTransitCoroutedTunnelIncomingBytes,
       "cienaCesGmplsStaticTransitCoroutedTunnelOutgoingBytes": cienaCesGmplsStaticTransitCoroutedTunnelOutgoingBytes,
       "cienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingPackets": cienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingPackets,
       "cienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingPackets": cienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingPackets,
       "cienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingBytes": cienaCesGmplsStaticTransitCoroutedTunnelReverseIncomingBytes,
       "cienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingBytes": cienaCesGmplsStaticTransitCoroutedTunnelReverseOutgoingBytes,
       "cienaCesGmplsDynamicTransitUniDirTunnelTable": cienaCesGmplsDynamicTransitUniDirTunnelTable,
       "cienaCesGmplsDynamicTransitUniDirTunnelEntry": cienaCesGmplsDynamicTransitUniDirTunnelEntry,
       "cienaCesGmplsDynamicTransitUniDirTunnelIndex": cienaCesGmplsDynamicTransitUniDirTunnelIndex,
       "cienaCesGmplsDynamicTransitUniDirTunnelName": cienaCesGmplsDynamicTransitUniDirTunnelName,
       "cienaCesGmplsDynamicTransitUniDirTunnelAdminState": cienaCesGmplsDynamicTransitUniDirTunnelAdminState,
       "cienaCesGmplsDynamicTransitUniDirTunnelOperState": cienaCesGmplsDynamicTransitUniDirTunnelOperState,
       "cienaCesGmplsDynamicTransitUniDirTunnelSourceIpAddr": cienaCesGmplsDynamicTransitUniDirTunnelSourceIpAddr,
       "cienaCesGmplsDynamicTransitUniDirTunnelDestIpAddr": cienaCesGmplsDynamicTransitUniDirTunnelDestIpAddr,
       "cienaCesGmplsDynamicTransitUniDirTunnelNextHopIpAddr": cienaCesGmplsDynamicTransitUniDirTunnelNextHopIpAddr,
       "cienaCesGmplsDynamicTransitUniDirTunnelForwardInLabel": cienaCesGmplsDynamicTransitUniDirTunnelForwardInLabel,
       "cienaCesGmplsDynamicTransitUniDirTunnelForwardOutLabel": cienaCesGmplsDynamicTransitUniDirTunnelForwardOutLabel,
       "cienaCesGmplsDynamicTransitUniDirTunnelTTLPolicy": cienaCesGmplsDynamicTransitUniDirTunnelTTLPolicy,
       "cienaCesGmplsDynamicTransitUniDirTunnelFixedTTL": cienaCesGmplsDynamicTransitUniDirTunnelFixedTTL,
       "cienaCesGmplsDynamicTransitUniDirTunnelIncomingPackets": cienaCesGmplsDynamicTransitUniDirTunnelIncomingPackets,
       "cienaCesGmplsDynamicTransitUniDirTunnelOutgoingPackets": cienaCesGmplsDynamicTransitUniDirTunnelOutgoingPackets,
       "cienaCesGmplsDynamicTransitUniDirTunnelIncomingBytes": cienaCesGmplsDynamicTransitUniDirTunnelIncomingBytes,
       "cienaCesGmplsDynamicTransitUniDirTunnelOutgoingBytes": cienaCesGmplsDynamicTransitUniDirTunnelOutgoingBytes,
       "cienaCesGmplsDynamicTransitCoroutedTunnelTable": cienaCesGmplsDynamicTransitCoroutedTunnelTable,
       "cienaCesGmplsDynamicTransitCoroutedTunnelEntry": cienaCesGmplsDynamicTransitCoroutedTunnelEntry,
       "cienaCesGmplsDynamicTransitCoroutedTunnelIndex": cienaCesGmplsDynamicTransitCoroutedTunnelIndex,
       "cienaCesGmplsDynamicTransitCoroutedTunnelName": cienaCesGmplsDynamicTransitCoroutedTunnelName,
       "cienaCesGmplsDynamicTransitCoroutedTunnelAdminState": cienaCesGmplsDynamicTransitCoroutedTunnelAdminState,
       "cienaCesGmplsDynamicTransitCoroutedTunnelOperState": cienaCesGmplsDynamicTransitCoroutedTunnelOperState,
       "cienaCesGmplsDynamicTransitCoroutedTunnelSourceIpAddr": cienaCesGmplsDynamicTransitCoroutedTunnelSourceIpAddr,
       "cienaCesGmplsDynamicTransitCoroutedTunnelDestIpAddr": cienaCesGmplsDynamicTransitCoroutedTunnelDestIpAddr,
       "cienaCesGmplsDynamicTransitCoroutedTunnelNextHopIpAddr": cienaCesGmplsDynamicTransitCoroutedTunnelNextHopIpAddr,
       "cienaCesGmplsDynamicTransitCoroutedTunnelPrevHopIpAddr": cienaCesGmplsDynamicTransitCoroutedTunnelPrevHopIpAddr,
       "cienaCesGmplsDynamicTransitCoroutedTunnelForwardInLabel": cienaCesGmplsDynamicTransitCoroutedTunnelForwardInLabel,
       "cienaCesGmplsDynamicTransitCoroutedTunnelForwardOutLabel": cienaCesGmplsDynamicTransitCoroutedTunnelForwardOutLabel,
       "cienaCesGmplsDynamicTransitCoroutedTunnelReverseInLabel": cienaCesGmplsDynamicTransitCoroutedTunnelReverseInLabel,
       "cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutLabel": cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutLabel,
       "cienaCesGmplsDynamicTransitCoroutedTunnelTTLPolicy": cienaCesGmplsDynamicTransitCoroutedTunnelTTLPolicy,
       "cienaCesGmplsDynamicTransitCoroutedTunnelFixedTTL": cienaCesGmplsDynamicTransitCoroutedTunnelFixedTTL,
       "cienaCesGmplsDynamicTransitCoroutedTunnelIncomingPackets": cienaCesGmplsDynamicTransitCoroutedTunnelIncomingPackets,
       "cienaCesGmplsDynamicTransitCoroutedTunnelOutgoingPackets": cienaCesGmplsDynamicTransitCoroutedTunnelOutgoingPackets,
       "cienaCesGmplsDynamicTransitCoroutedTunnelIncomingBytes": cienaCesGmplsDynamicTransitCoroutedTunnelIncomingBytes,
       "cienaCesGmplsDynamicTransitCoroutedTunnelOutgoingBytes": cienaCesGmplsDynamicTransitCoroutedTunnelOutgoingBytes,
       "cienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingPackets": cienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingPackets,
       "cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingPackets": cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingPackets,
       "cienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingBytes": cienaCesGmplsDynamicTransitCoroutedTunnelReverseIncomingBytes,
       "cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingBytes": cienaCesGmplsDynamicTransitCoroutedTunnelReverseOutgoingBytes,
       "cienaCesGmplsAssociatedTunnelTable": cienaCesGmplsAssociatedTunnelTable,
       "cienaCesGmplsAssociatedTunnelEntry": cienaCesGmplsAssociatedTunnelEntry,
       "cienaCesGmplsAssociatedTunnelIndex": cienaCesGmplsAssociatedTunnelIndex,
       "cienaCesGmplsAssociatedTunnelName": cienaCesGmplsAssociatedTunnelName,
       "cienaCesGmplsAssociatedForwardTunnelName": cienaCesGmplsAssociatedForwardTunnelName,
       "cienaCesGmplsAssociatedForwardTunnelType": cienaCesGmplsAssociatedForwardTunnelType,
       "cienaCesGmplsAssociatedReverseTunnelName": cienaCesGmplsAssociatedReverseTunnelName,
       "cienaCesGmplsAssociatedReverseTunnelType": cienaCesGmplsAssociatedReverseTunnelType,
       "cienaCesGmplsAssociatedForwardTunnelDestIpAddr": cienaCesGmplsAssociatedForwardTunnelDestIpAddr,
       "cienaCesGmplsAssociatedDynamicTunnelSrcIpAddr": cienaCesGmplsAssociatedDynamicTunnelSrcIpAddr,
       "cienaCesGmplsAssociatedTunnelAdminState": cienaCesGmplsAssociatedTunnelAdminState,
       "cienaCesGmplsAssociatedTunnelOperState": cienaCesGmplsAssociatedTunnelOperState,
       "cienaCesGmplsAssociatedForwardTunnelOperState": cienaCesGmplsAssociatedForwardTunnelOperState,
       "cienaCesGmplsAssociatedReverseTunnelOperState": cienaCesGmplsAssociatedReverseTunnelOperState,
       "cienaCesGmplsAssociatedProtectionRole": cienaCesGmplsAssociatedProtectionRole,
       "cienaCesGmplsAssociatedProtectionState": cienaCesGmplsAssociatedProtectionState,
       "cienaCesGmplsAssociatedTunnelProtectionPartnerName": cienaCesGmplsAssociatedTunnelProtectionPartnerName,
       "cienaCesGmplsAssociatedBfdMonitoring": cienaCesGmplsAssociatedBfdMonitoring,
       "cienaCesGmplsAssociatedBfdProfileName": cienaCesGmplsAssociatedBfdProfileName,
       "cienaCesGmplsAssociatedBfdSessionName": cienaCesGmplsAssociatedBfdSessionName,
       "cienaCesGmplsAssociatedAisMonitoring": cienaCesGmplsAssociatedAisMonitoring,
       "cienaCesGmplsAssociatedAisProfileName": cienaCesGmplsAssociatedAisProfileName,
       "cienaCesGmplsAssociatedBfdSessionFaulted": cienaCesGmplsAssociatedBfdSessionFaulted,
       "cienaCesGmplsAssociatedBfdProfileIndex": cienaCesGmplsAssociatedBfdProfileIndex,
       "cienaCesGmplsTunnelARHopTable": cienaCesGmplsTunnelARHopTable,
       "cienaCesGmplsTunnelARHopEntry": cienaCesGmplsTunnelARHopEntry,
       "cienaGmplsTunnelARHopListIndex": cienaGmplsTunnelARHopListIndex,
       "cienaGmplsTunnelARHopIndex": cienaGmplsTunnelARHopIndex,
       "cienaGmplsTunnelARHopAddrType": cienaGmplsTunnelARHopAddrType,
       "cienaGmplsTunnelARHopIpAddr": cienaGmplsTunnelARHopIpAddr,
       "cienaGmplsTunnelARHopAddrUnnum": cienaGmplsTunnelARHopAddrUnnum,
       "cienaGmplsTunnelARHopLspId": cienaGmplsTunnelARHopLspId,
       "cienaCesGmplsEncapTunnelNotif": cienaCesGmplsEncapTunnelNotif,
       "cienaCesGmplsNotifEncapTunnelTable": cienaCesGmplsNotifEncapTunnelTable,
       "cienaCesGmplsNotifEncapTunnelEntry": cienaCesGmplsNotifEncapTunnelEntry,
       "cienaCesGmplsNotifEncapTunnelIndex": cienaCesGmplsNotifEncapTunnelIndex,
       "cienaCesGmplsNotifEncapTunnelType": cienaCesGmplsNotifEncapTunnelType,
       "cienaCesGmplsNotifEncapTunnelName": cienaCesGmplsNotifEncapTunnelName,
       "cienaCesGmplsNotifEncapTunnelAdminState": cienaCesGmplsNotifEncapTunnelAdminState,
       "cienaCesGmplsNotifEncapTunnelOperState": cienaCesGmplsNotifEncapTunnelOperState,
       "cienaCesGmplsNotifEncapTunnelAisFaulted": cienaCesGmplsNotifEncapTunnelAisFaulted,
       "cienaCesGmplsNotifEncapTunnelFaultedNodeId": cienaCesGmplsNotifEncapTunnelFaultedNodeId,
       "cienaCesGmplsNotifEncapTunnelFarEndLerId": cienaCesGmplsNotifEncapTunnelFarEndLerId,
       "cienaCesGmplsNotifEncapTunnelResult": cienaCesGmplsNotifEncapTunnelResult,
       "cienaCesGmplsNotifEncapTunnelProtectionRole": cienaCesGmplsNotifEncapTunnelProtectionRole,
       "cienaCesGmplsNotifEncapTunnelRequestedBw": cienaCesGmplsNotifEncapTunnelRequestedBw,
       "cienaCesGmplsNotifEncapTunnelOperationalBw": cienaCesGmplsNotifEncapTunnelOperationalBw,
       "cienaCesGmplsNotifEncapTunnelMbbParentApp": cienaCesGmplsNotifEncapTunnelMbbParentApp,
       "cienaCesGmplsNotifEncapTunnelOamFaulted": cienaCesGmplsNotifEncapTunnelOamFaulted,
       "cienaCesGmplsDecapTunnelNotif": cienaCesGmplsDecapTunnelNotif,
       "cienaCesGmplsNotifDecapTunnelTable": cienaCesGmplsNotifDecapTunnelTable,
       "cienaCesGmplsNotifDecapTunnelEntry": cienaCesGmplsNotifDecapTunnelEntry,
       "cienaCesGmplsNotifDecapTunnelIndex": cienaCesGmplsNotifDecapTunnelIndex,
       "cienaCesGmplsNotifDecapTunnelType": cienaCesGmplsNotifDecapTunnelType,
       "cienaCesGmplsNotifDecapTunnelName": cienaCesGmplsNotifDecapTunnelName,
       "cienaCesGmplsNotifDecapTunnelAdminState": cienaCesGmplsNotifDecapTunnelAdminState,
       "cienaCesGmplsNotifDecapTunnelOperState": cienaCesGmplsNotifDecapTunnelOperState,
       "cienaCesGmplsNotifDecapTunnelAisFaulted": cienaCesGmplsNotifDecapTunnelAisFaulted,
       "cienaCesGmplsNotifDecapTunnelFaultedNodeId": cienaCesGmplsNotifDecapTunnelFaultedNodeId,
       "cienaCesGmplsNotifDecapTunnelFarEndLerId": cienaCesGmplsNotifDecapTunnelFarEndLerId,
       "cienaCesGmplsNotifDecapTunnelOamFaulted": cienaCesGmplsNotifDecapTunnelOamFaulted,
       "cienaCesGmplsTransitTunnelNotif": cienaCesGmplsTransitTunnelNotif,
       "cienaCesGmplsNotifTransitTunnelTable": cienaCesGmplsNotifTransitTunnelTable,
       "cienaCesGmplsNotifTransitTunnelEntry": cienaCesGmplsNotifTransitTunnelEntry,
       "cienaCesGmplsNotifTransitTunnelIndex": cienaCesGmplsNotifTransitTunnelIndex,
       "cienaCesGmplsNotifTransitTunnelType": cienaCesGmplsNotifTransitTunnelType,
       "cienaCesGmplsNotifTransitTunnelName": cienaCesGmplsNotifTransitTunnelName,
       "cienaCesGmplsNotifTransitTunnelAdminState": cienaCesGmplsNotifTransitTunnelAdminState,
       "cienaCesGmplsNotifTransitTunnelOperState": cienaCesGmplsNotifTransitTunnelOperState,
       "cienaCesGmplsNotifTransitTunnelOamFaulted": cienaCesGmplsNotifTransitTunnelOamFaulted,
       "cienaCesGmplsAssociatedTunnelNotif": cienaCesGmplsAssociatedTunnelNotif,
       "cienaCesGmplsNotifAssociatedTunnelTable": cienaCesGmplsNotifAssociatedTunnelTable,
       "cienaCesGmplsNotifAssociatedTunnelEntry": cienaCesGmplsNotifAssociatedTunnelEntry,
       "cienaCesGmplsNotifAssociatedTunnelIndex": cienaCesGmplsNotifAssociatedTunnelIndex,
       "cienaCesGmplsNotifAssociatedTunnelType": cienaCesGmplsNotifAssociatedTunnelType,
       "cienaCesGmplsNotifAssociatedTunnelName": cienaCesGmplsNotifAssociatedTunnelName,
       "cienaCesGmplsNotifAssociatedTunnelAdminState": cienaCesGmplsNotifAssociatedTunnelAdminState,
       "cienaCesGmplsNotifAssociatedTunnelOperState": cienaCesGmplsNotifAssociatedTunnelOperState,
       "cienaCesGmplsNotifAssociatedTunnelAisFaulted": cienaCesGmplsNotifAssociatedTunnelAisFaulted,
       "cienaCesGmplsNotifAssociatedTunnelFaultedNodeId": cienaCesGmplsNotifAssociatedTunnelFaultedNodeId,
       "cienaCesGmplsNotifAssociatedTunnelFarEndLerId": cienaCesGmplsNotifAssociatedTunnelFarEndLerId,
       "cienaCesGmplsNotifAssociatedTunnelOamFaulted": cienaCesGmplsNotifAssociatedTunnelOamFaulted,
       "cienaCesGmplsEncapTunnelGrpNotif": cienaCesGmplsEncapTunnelGrpNotif,
       "cienaCesGmplsNotifEncapTunnelGrpTable": cienaCesGmplsNotifEncapTunnelGrpTable,
       "cienaCesGmplsNotifEncapTunnelGrpEntry": cienaCesGmplsNotifEncapTunnelGrpEntry,
       "cienaCesGmplsNotifEncapTunnelGrpIndex": cienaCesGmplsNotifEncapTunnelGrpIndex,
       "cienaCesGmplsNotifEncapTunnelGrpName": cienaCesGmplsNotifEncapTunnelGrpName,
       "cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex": cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlIndex,
       "cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlName": cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlName,
       "cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType": cienaCesGmplsNotifEncapTunnelGrpActiveEncapTunlType,
       "cienaCesGmplsDecapTunnelGrpNotif": cienaCesGmplsDecapTunnelGrpNotif,
       "cienaCesGmplsNotifDecapTunnelGrpTable": cienaCesGmplsNotifDecapTunnelGrpTable,
       "cienaCesGmplsNotifDecapTunnelGrpEntry": cienaCesGmplsNotifDecapTunnelGrpEntry,
       "cienaCesGmplsNotifDecapTunnelGrpIndex": cienaCesGmplsNotifDecapTunnelGrpIndex,
       "cienaCesGmplsNotifDecapTunnelGrpName": cienaCesGmplsNotifDecapTunnelGrpName,
       "cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlIndex": cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlIndex,
       "cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlName": cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlName,
       "cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlType": cienaCesGmplsNotifDecapTunnelGrpActiveDecapTunlType,
       "cienaCesGmplsTunnelAisFaultErrorNotif": cienaCesGmplsTunnelAisFaultErrorNotif,
       "cienaCesGmplsNotifTunnelAisFaultErrorTable": cienaCesGmplsNotifTunnelAisFaultErrorTable,
       "cienaCesGmplsNotifTunnelAisFaultErrorEntry": cienaCesGmplsNotifTunnelAisFaultErrorEntry,
       "cienaCesGmplsNotifTunnelDecapLabel": cienaCesGmplsNotifTunnelDecapLabel,
       "cienaCesGmplsNotifTunnelErrorMsg": cienaCesGmplsNotifTunnelErrorMsg,
       "cienaCesMplsGlobal": cienaCesMplsGlobal,
       "cienaCesMplsAttrs": cienaCesMplsAttrs,
       "cienaCesMplsGlobalStaticAdminLabelRangeStart": cienaCesMplsGlobalStaticAdminLabelRangeStart,
       "cienaCesMplsGlobalStaticAdminLabelRangeEnd": cienaCesMplsGlobalStaticAdminLabelRangeEnd,
       "cienaCesMplsGlobalStaticOperLabelRangeStart": cienaCesMplsGlobalStaticOperLabelRangeStart,
       "cienaCesMplsGlobalStaticOperLabelRangeEnd": cienaCesMplsGlobalStaticOperLabelRangeEnd,
       "cienaCesMplsGlobalDynamicAdminLabelRangeStart": cienaCesMplsGlobalDynamicAdminLabelRangeStart,
       "cienaCesMplsGlobalDynamicAdminLabelRangeEnd": cienaCesMplsGlobalDynamicAdminLabelRangeEnd,
       "cienaCesMplsGlobalDynamicOperLabelRangeStart": cienaCesMplsGlobalDynamicOperLabelRangeStart,
       "cienaCesMplsGlobalDynamicOperLabelRangeEnd": cienaCesMplsGlobalDynamicOperLabelRangeEnd,
       "cienaCesMplsGlobalStaticAdminTunnelLabelRangeStart": cienaCesMplsGlobalStaticAdminTunnelLabelRangeStart,
       "cienaCesMplsGlobalStaticAdminTunnelLabelRangeEnd": cienaCesMplsGlobalStaticAdminTunnelLabelRangeEnd,
       "cienaCesMplsGlobalStaticOperTunnelLabelRangeStart": cienaCesMplsGlobalStaticOperTunnelLabelRangeStart,
       "cienaCesMplsGlobalStaticOperTunnelLabelRangeEnd": cienaCesMplsGlobalStaticOperTunnelLabelRangeEnd,
       "cienaCesMplsGlobalStaticAdminVcLabelRangeStart": cienaCesMplsGlobalStaticAdminVcLabelRangeStart,
       "cienaCesMplsGlobalStaticAdminVcLabelRangeEnd": cienaCesMplsGlobalStaticAdminVcLabelRangeEnd,
       "cienaCesMplsGlobalStaticOperVcLabelRangeStart": cienaCesMplsGlobalStaticOperVcLabelRangeStart,
       "cienaCesMplsGlobalStaticOperVcLabelRangeEnd": cienaCesMplsGlobalStaticOperVcLabelRangeEnd,
       "cienaCesMplsGlobalNextFreeStaticVcLabel": cienaCesMplsGlobalNextFreeStaticVcLabel,
       "cienaCesMplsTunnelCosProfileTable": cienaCesMplsTunnelCosProfileTable,
       "cienaCesMplsTunnelCosProfileEntry": cienaCesMplsTunnelCosProfileEntry,
       "cienaCesMplsTunnelCosProfileIndex": cienaCesMplsTunnelCosProfileIndex,
       "cienaCesMplsTunnelCosProfileName": cienaCesMplsTunnelCosProfileName,
       "cienaCesMplsTunnelFrmCosPolicy": cienaCesMplsTunnelFrmCosPolicy,
       "cienaCesMplsTunnelFrmCosMapId": cienaCesMplsTunnelFrmCosMapId,
       "cienaCesMplsTunnelFrmCosMapName": cienaCesMplsTunnelFrmCosMapName,
       "cienaCesMplsTunnelFixedTC": cienaCesMplsTunnelFixedTC,
       "cienaCesMplsTunnelRcosPolicy": cienaCesMplsTunnelRcosPolicy,
       "cienaCesMplsTunnelRcosMapName": cienaCesMplsTunnelRcosMapName,
       "cienaCesMplsTunnelRCosMapId": cienaCesMplsTunnelRCosMapId,
       "cienaCesMplsTunnelRcosProfileName": cienaCesMplsTunnelRcosProfileName,
       "cienaCesMplsTunnelRCosProfileId": cienaCesMplsTunnelRCosProfileId,
       "cienaCesMplsGlobalTunnelPath": cienaCesMplsGlobalTunnelPath,
       "cienaCesMplsGlobalTunnelPathTable": cienaCesMplsGlobalTunnelPathTable,
       "cienaCesMplsGlobalTunnelPathEntry": cienaCesMplsGlobalTunnelPathEntry,
       "cienaCesMplsGlobalTunnelPathIndex": cienaCesMplsGlobalTunnelPathIndex,
       "cienaCesMplsGlobalTunnelPathName": cienaCesMplsGlobalTunnelPathName,
       "cienaCesMplsGlobalTunnelPathUseCount": cienaCesMplsGlobalTunnelPathUseCount,
       "cienaCesMplsGlobalTunnelPathHopTable": cienaCesMplsGlobalTunnelPathHopTable,
       "cienaCesMplsGlobalTunnelPathHopEntry": cienaCesMplsGlobalTunnelPathHopEntry,
       "cienaCesMplsGlobalTunnelPathHopIndex": cienaCesMplsGlobalTunnelPathHopIndex,
       "cienaCesMplsGlobalTunnelPathHopIpAddr": cienaCesMplsGlobalTunnelPathHopIpAddr,
       "cienaCesMplsGlobalTunnelPathHopType": cienaCesMplsGlobalTunnelPathHopType,
       "cienaCesMplsGlobalFreeStaticTunnelLabelTable": cienaCesMplsGlobalFreeStaticTunnelLabelTable,
       "cienaCesMplsGlobalFreeStaticTunnelLabelEntry": cienaCesMplsGlobalFreeStaticTunnelLabelEntry,
       "cienaCesMplsGlobalFreeStaticTunnelLabelIndex": cienaCesMplsGlobalFreeStaticTunnelLabelIndex,
       "cienaCesMplsGlobalFreeStaticTunnelLabel": cienaCesMplsGlobalFreeStaticTunnelLabel,
       "cienaCesMplsPw": cienaCesMplsPw,
       "cienaCesMplsPwTable": cienaCesMplsPwTable,
       "cienaCesMplsPwEntry": cienaCesMplsPwEntry,
       "cienaCesMplsPwIndex": cienaCesMplsPwIndex,
       "cienaCesMplsPwSignallingType": cienaCesMplsPwSignallingType,
       "cienaCesMplsPwId": cienaCesMplsPwId,
       "cienaCesMplsPwName": cienaCesMplsPwName,
       "cienaCesMplsPwCustomerName": cienaCesMplsPwCustomerName,
       "cienaCesMplsPwAdminState": cienaCesMplsPwAdminState,
       "cienaCesMplsPwOperState": cienaCesMplsPwOperState,
       "cienaCesMplsPwPeerIpAddr": cienaCesMplsPwPeerIpAddr,
       "cienaCesMplsPwInLabel": cienaCesMplsPwInLabel,
       "cienaCesMplsPwOutLabel": cienaCesMplsPwOutLabel,
       "cienaCesMplsPwStatusTlv": cienaCesMplsPwStatusTlv,
       "cienaCesMplsPwRefreshStatusIntvl": cienaCesMplsPwRefreshStatusIntvl,
       "cienaCesMplsPwLocalFault": cienaCesMplsPwLocalFault,
       "cienaCesMplsPwRemoteFault": cienaCesMplsPwRemoteFault,
       "cienaCesMplsPwMtu": cienaCesMplsPwMtu,
       "cienaCesMplsPwType": cienaCesMplsPwType,
       "cienaCesMplsPwMode": cienaCesMplsPwMode,
       "cienaCesMplsPwCoSProfileName": cienaCesMplsPwCoSProfileName,
       "cienaCesMplsPwCoSProfileIndex": cienaCesMplsPwCoSProfileIndex,
       "cienaCesMplsPwEgressL2PtTransform": cienaCesMplsPwEgressL2PtTransform,
       "cienaCesMplsPwVccVProfileName": cienaCesMplsPwVccVProfileName,
       "cienaCesMplsPwVccVProfileIndex": cienaCesMplsPwVccVProfileIndex,
       "cienaCesMplsPwLocalCcCv": cienaCesMplsPwLocalCcCv,
       "cienaCesMplsPwRemoteCcCv": cienaCesMplsPwRemoteCcCv,
       "cienaCesMplsPwOperatingCcCv": cienaCesMplsPwOperatingCcCv,
       "cienaCesMplsPwBlocking": cienaCesMplsPwBlocking,
       "cienaCesMplsPwVifIndex": cienaCesMplsPwVifIndex,
       "cienaCesMplsPwConfigTunnelName": cienaCesMplsPwConfigTunnelName,
       "cienaCesMplsPwConfigTunnelType": cienaCesMplsPwConfigTunnelType,
       "cienaCesMplsPwConfigTunnelIndex": cienaCesMplsPwConfigTunnelIndex,
       "cienaCesMplsPwActiveTunnelName": cienaCesMplsPwActiveTunnelName,
       "cienaCesMplsPwActiveTunnelType": cienaCesMplsPwActiveTunnelType,
       "cienaCesMplsPwActiveTunnelIndex": cienaCesMplsPwActiveTunnelIndex,
       "cienaCesMplsPwRole": cienaCesMplsPwRole,
       "cienaCesMplsPwPrimaryPwName": cienaCesMplsPwPrimaryPwName,
       "cienaCesMplsPwPrimaryPwIndex": cienaCesMplsPwPrimaryPwIndex,
       "cienaCesMplsPwVsIndex": cienaCesMplsPwVsIndex,
       "cienaCesServiceDelimiterVID": cienaCesServiceDelimiterVID,
       "cienaCesServiceDelimiterTPID": cienaCesServiceDelimiterTPID,
       "cienaCesMplsPwReversion": cienaCesMplsPwReversion,
       "cienaCesMplsPwRevertTime": cienaCesMplsPwRevertTime,
       "cienaCesMplsPwProtectionRole": cienaCesMplsPwProtectionRole,
       "cienaCesMplsPwProtectionState": cienaCesMplsPwProtectionState,
       "cienaCesMplsPwVsName": cienaCesMplsPwVsName,
       "cienaCesMplsPwStatusQuery": cienaCesMplsPwStatusQuery,
       "cienaCesMplsMsPwPeerPwName": cienaCesMplsMsPwPeerPwName,
       "cienaCesMplsMsPwPeerPwIndex": cienaCesMplsMsPwPeerPwIndex,
       "cienaCesMplsPwIdInRemoteFault": cienaCesMplsPwIdInRemoteFault,
       "cienaCesMplsLocalIpInRemoteFault": cienaCesMplsLocalIpInRemoteFault,
       "cienaCesMplsRemoteIpInRemoteFault": cienaCesMplsRemoteIpInRemoteFault,
       "cienaCesMplsPwFaultToNextHop": cienaCesMplsPwFaultToNextHop,
       "cienaCesMplsPwIdInFaultToNextHop": cienaCesMplsPwIdInFaultToNextHop,
       "cienaCesMplsLocalIpInFaultToNextHop": cienaCesMplsLocalIpInFaultToNextHop,
       "cienaCesMplsRemoteIpInFaultToNextHop": cienaCesMplsRemoteIpInFaultToNextHop,
       "cienaCesMplsPwConfigBandwidth": cienaCesMplsPwConfigBandwidth,
       "cienaCesMplsPwOperBandwidth": cienaCesMplsPwOperBandwidth,
       "cienaCesMplsPwBandwidthState": cienaCesMplsPwBandwidthState,
       "cienaCesMplsPwCosProfileTable": cienaCesMplsPwCosProfileTable,
       "cienaCesMplsPwCosProfileEntry": cienaCesMplsPwCosProfileEntry,
       "cienaCesMplsPwCosProfileIndex": cienaCesMplsPwCosProfileIndex,
       "cienaCesMplsPwCosProfileName": cienaCesMplsPwCosProfileName,
       "cienaCesMplsPwCosProfileFrmCosPolicy": cienaCesMplsPwCosProfileFrmCosPolicy,
       "cienaCesMplsPwCosProfileFrmCosMapId": cienaCesMplsPwCosProfileFrmCosMapId,
       "cienaCesMplsPwCosProfileFrmCosMapName": cienaCesMplsPwCosProfileFrmCosMapName,
       "cienaCesMplsPwCosProfileFixedTC": cienaCesMplsPwCosProfileFixedTC,
       "cienaCesMplsPwCosProfileRcosPolicy": cienaCesMplsPwCosProfileRcosPolicy,
       "cienaCesMplsPwCosProfileRcosMapName": cienaCesMplsPwCosProfileRcosMapName,
       "cienaCesMplsPwCosProfileRCosMapId": cienaCesMplsPwCosProfileRCosMapId,
       "cienaCesMplsPwCosProfileRcosProfileName": cienaCesMplsPwCosProfileRcosProfileName,
       "cienaCesMplsPwCosProfileRCosProfileId": cienaCesMplsPwCosProfileRCosProfileId,
       "cienaCesMplsPwCosProfileRCosFixed": cienaCesMplsPwCosProfileRCosFixed,
       "cienaCesMplsPwVccvProfileTable": cienaCesMplsPwVccvProfileTable,
       "cienaCesMplsPwVccvProfileEntry": cienaCesMplsPwVccvProfileEntry,
       "cienaCesMplsPwVccvProfileIndex": cienaCesMplsPwVccvProfileIndex,
       "cienaCesMplsPwVccvProfileName": cienaCesMplsPwVccvProfileName,
       "cienaCesMplsPwVccvProfileCcTtlExp": cienaCesMplsPwVccvProfileCcTtlExp,
       "cienaCesMplsPwVccvProfileCcCienaOob": cienaCesMplsPwVccvProfileCcCienaOob,
       "cienaCesMplsPwNotif": cienaCesMplsPwNotif,
       "cienaCesMplsPwNotifTable": cienaCesMplsPwNotifTable,
       "cienaCesMplsPwNotifEntry": cienaCesMplsPwNotifEntry,
       "cienaCesMplsPwNotifPwIndex": cienaCesMplsPwNotifPwIndex,
       "cienaCesMplsPwNotifPwId": cienaCesMplsPwNotifPwId,
       "cienaCesMplsPwNotifPwName": cienaCesMplsPwNotifPwName,
       "cienaCesMplsPwNotifPwPeerIpAddr": cienaCesMplsPwNotifPwPeerIpAddr,
       "cienaCesMplsPwNotifPriPwId": cienaCesMplsPwNotifPriPwId,
       "cienaCesMplsPwNotifPriPwName": cienaCesMplsPwNotifPriPwName,
       "cienaCesMplsPwNotifPriPwPeerIpAddr": cienaCesMplsPwNotifPriPwPeerIpAddr,
       "cienaCesMplsPwNotifActPwIndex": cienaCesMplsPwNotifActPwIndex,
       "cienaCesMplsPwNotifActPwId": cienaCesMplsPwNotifActPwId,
       "cienaCesMplsPwNotifActPwName": cienaCesMplsPwNotifActPwName,
       "cienaCesMplsPwNotifActPwPeerIpAddr": cienaCesMplsPwNotifActPwPeerIpAddr,
       "cienaCesMplsPWTrafficStatsTable": cienaCesMplsPWTrafficStatsTable,
       "cienaCesMplsPWTrafficStatsEntry": cienaCesMplsPWTrafficStatsEntry,
       "cienaCesMplsPWTrafficStatsPWIndex": cienaCesMplsPWTrafficStatsPWIndex,
       "cienaCesMplsPWTrafficStatsIncomingPackets": cienaCesMplsPWTrafficStatsIncomingPackets,
       "cienaCesMplsPWTrafficStatsOutgoingPackets": cienaCesMplsPWTrafficStatsOutgoingPackets,
       "cienaCesMplsPWTrafficStatsIncomingBytes": cienaCesMplsPWTrafficStatsIncomingBytes,
       "cienaCesMplsPWTrafficStatsOutgoingBytes": cienaCesMplsPWTrafficStatsOutgoingBytes,
       "cienaCesMplsTe": cienaCesMplsTe,
       "cienaCesTeLinkTable": cienaCesTeLinkTable,
       "cienaCesTeLinkEntry": cienaCesTeLinkEntry,
       "cienaCesTeIfIndex": cienaCesTeIfIndex,
       "cienaCesTeInterfaceName": cienaCesTeInterfaceName,
       "cienaCesTeLinkMetric": cienaCesTeLinkMetric,
       "cienaCesTeResourceColorGroupIndex": cienaCesTeResourceColorGroupIndex,
       "cienaCesTeResourceColorBitMask": cienaCesTeResourceColorBitMask,
       "cienaCesMplsClassProfIndex": cienaCesMplsClassProfIndex,
       "cienaCesTeLinkMode": cienaCesTeLinkMode,
       "cienaCesTeLinkSrlgCount": cienaCesTeLinkSrlgCount,
       "cienaCesTeLinkMaximumBandwidth": cienaCesTeLinkMaximumBandwidth,
       "cienaCesTeLinkMaximumReservableBandwidth": cienaCesTeLinkMaximumReservableBandwidth,
       "cienaCesTeLinkTotalBandwidthPrio0": cienaCesTeLinkTotalBandwidthPrio0,
       "cienaCesTeLinkReservedBandwidthPrio0": cienaCesTeLinkReservedBandwidthPrio0,
       "cienaCesTeLinkUnReservedBandwidthPrio0": cienaCesTeLinkUnReservedBandwidthPrio0,
       "cienaCesTeLinkTotalBandwidthPrio1": cienaCesTeLinkTotalBandwidthPrio1,
       "cienaCesTeLinkReservedBandwidthPrio1": cienaCesTeLinkReservedBandwidthPrio1,
       "cienaCesTeLinkUnReservedBandwidthPrio1": cienaCesTeLinkUnReservedBandwidthPrio1,
       "cienaCesTeLinkTotalBandwidthPrio2": cienaCesTeLinkTotalBandwidthPrio2,
       "cienaCesTeLinkReservedBandwidthPrio2": cienaCesTeLinkReservedBandwidthPrio2,
       "cienaCesTeLinkUnReservedBandwidthPrio2": cienaCesTeLinkUnReservedBandwidthPrio2,
       "cienaCesTeLinkTotalBandwidthPrio3": cienaCesTeLinkTotalBandwidthPrio3,
       "cienaCesTeLinkReservedBandwidthPrio3": cienaCesTeLinkReservedBandwidthPrio3,
       "cienaCesTeLinkUnReservedBandwidthPrio3": cienaCesTeLinkUnReservedBandwidthPrio3,
       "cienaCesTeLinkTotalBandwidthPrio4": cienaCesTeLinkTotalBandwidthPrio4,
       "cienaCesTeLinkReservedBandwidthPrio4": cienaCesTeLinkReservedBandwidthPrio4,
       "cienaCesTeLinkUnReservedBandwidthPrio4": cienaCesTeLinkUnReservedBandwidthPrio4,
       "cienaCesTeLinkTotalBandwidthPrio5": cienaCesTeLinkTotalBandwidthPrio5,
       "cienaCesTeLinkReservedBandwidthPrio5": cienaCesTeLinkReservedBandwidthPrio5,
       "cienaCesTeLinkUnReservedBandwidthPrio5": cienaCesTeLinkUnReservedBandwidthPrio5,
       "cienaCesTeLinkTotalBandwidthPrio6": cienaCesTeLinkTotalBandwidthPrio6,
       "cienaCesTeLinkReservedBandwidthPrio6": cienaCesTeLinkReservedBandwidthPrio6,
       "cienaCesTeLinkUnReservedBandwidthPrio6": cienaCesTeLinkUnReservedBandwidthPrio6,
       "cienaCesTeLinkTotalBandwidthPrio7": cienaCesTeLinkTotalBandwidthPrio7,
       "cienaCesTeLinkReservedBandwidthPrio7": cienaCesTeLinkReservedBandwidthPrio7,
       "cienaCesTeLinkUnReservedBandwidthPrio7": cienaCesTeLinkUnReservedBandwidthPrio7,
       "cienaCesTeResourceGrpTable": cienaCesTeResourceGrpTable,
       "cienaCesTeResGrpEntry": cienaCesTeResGrpEntry,
       "cienaCesTeResourceColorGrpIndex": cienaCesTeResourceColorGrpIndex,
       "cienaCesTeResourceGrpName": cienaCesTeResourceGrpName,
       "cienaCesTeResourceColorGroupBitMask": cienaCesTeResourceColorGroupBitMask,
       "cienaCesTeResourceColorGroupUseCount": cienaCesTeResourceColorGroupUseCount,
       "cienaCesTeResourceColorsTable": cienaCesTeResourceColorsTable,
       "cienaCesTeResColorEntry": cienaCesTeResColorEntry,
       "cienaCesTeResourceColorIndex": cienaCesTeResourceColorIndex,
       "cienaCesTeResourceColorName": cienaCesTeResourceColorName,
       "cienaCesTeResourceColorBit": cienaCesTeResourceColorBit,
       "cienaCesTeResourceColorUseCount": cienaCesTeResourceColorUseCount,
       "cienaCesTeLinkSrlgTable": cienaCesTeLinkSrlgTable,
       "cienaCesTeLinkSrlgEntry": cienaCesTeLinkSrlgEntry,
       "cienaCesTeLinkSrlg": cienaCesTeLinkSrlg,
       "cienaCesTeLinkSrlgStatus": cienaCesTeLinkSrlgStatus,
       "cienaCesMplsMIBNotificationPrefix": cienaCesMplsMIBNotificationPrefix,
       "cienaCesMplsMIBNotifications": cienaCesMplsMIBNotifications,
       "cienaCesMplsTunnelOperStateChgTrap": cienaCesMplsTunnelOperStateChgTrap,
       "cienaCesMplsEncapTunnelGrpActiveEncapTunnelChange": cienaCesMplsEncapTunnelGrpActiveEncapTunnelChange,
       "cienaCesMplsTransitTunnelOperStateChgTrap": cienaCesMplsTransitTunnelOperStateChgTrap,
       "cienaCesMplsAssociatedTunnelOperStateChgTrap": cienaCesMplsAssociatedTunnelOperStateChgTrap,
       "cienaCesMplsCacInterfaceThresholdTrap": cienaCesMplsCacInterfaceThresholdTrap,
       "cienaCesGmplsMIBNotifications": cienaCesGmplsMIBNotifications,
       "cienaCesGmplsEncapUnidirTunnelOperStateChgTrap": cienaCesGmplsEncapUnidirTunnelOperStateChgTrap,
       "cienaCesGmplsEncapCoroutedTunnelOperStateChgTrap": cienaCesGmplsEncapCoroutedTunnelOperStateChgTrap,
       "cienaCesGmplsDecapCoroutedTunnelOperStateChgTrap": cienaCesGmplsDecapCoroutedTunnelOperStateChgTrap,
       "cienaCesGmplsTransitUnidirTunnelOperStateChgTrap": cienaCesGmplsTransitUnidirTunnelOperStateChgTrap,
       "cienaCesGmplsTransitCoroutedTunnelOperStateChgTrap": cienaCesGmplsTransitCoroutedTunnelOperStateChgTrap,
       "cienaCesGmplsEncapUnidirTunnelGrpActiveEncapTunnelChangeTrap": cienaCesGmplsEncapUnidirTunnelGrpActiveEncapTunnelChangeTrap,
       "cienaCesGmplsEncapCoroutedTunnelGrpActiveEncapTunnelChangeTrap": cienaCesGmplsEncapCoroutedTunnelGrpActiveEncapTunnelChangeTrap,
       "cienaCesGmplsDecapCoroutedTunnelGrpActiveDecapTunnelChangeTrap": cienaCesGmplsDecapCoroutedTunnelGrpActiveDecapTunnelChangeTrap,
       "cienaCesGmplsAssociatedTunnelOperStateChgTrap": cienaCesGmplsAssociatedTunnelOperStateChgTrap,
       "cienaCesGmplsEncapCoroutedTunnelAisFaultStateChgTrap": cienaCesGmplsEncapCoroutedTunnelAisFaultStateChgTrap,
       "cienaCesGmplsDecapCoroutedTunnelAisFaultStateChgTrap": cienaCesGmplsDecapCoroutedTunnelAisFaultStateChgTrap,
       "cienaCesGmplsAssociatedTunnelAisFaultStateChgTrap": cienaCesGmplsAssociatedTunnelAisFaultStateChgTrap,
       "cienaCesGmplsTunnelAisFaultErrorTrap": cienaCesGmplsTunnelAisFaultErrorTrap,
       "cienaCesGmplsEncapTunnelResizeResultTrap": cienaCesGmplsEncapTunnelResizeResultTrap,
       "cienaCesGmplsEncapTunnelMbbResultTrap": cienaCesGmplsEncapTunnelMbbResultTrap,
       "cienaCesMplsPwMIBNotifications": cienaCesMplsPwMIBNotifications,
       "cienaCesMplsPwDown": cienaCesMplsPwDown,
       "cienaCesMplsPwUp": cienaCesMplsPwUp,
       "cienaCesMplsPwBundleActivePwChange": cienaCesMplsPwBundleActivePwChange}
)
