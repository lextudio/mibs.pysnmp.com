# SNMP MIB module (CISCO-DLSW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DLSW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:11 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(sdlcLSAddress,) = mibBuilder.importSymbols(
    "SNA-SDLC-MIB",
    "sdlcLSAddress")

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
 InstancePointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "InstancePointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDlswMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9)
)
ciscoDlswMIB.setRevisions(
        ("1995-12-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NBName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class MacAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )



class TAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class DlswTimeStamp(TimeTicks, TextualConvention):
    status = "current"


class EndStationLocation(Integer32, TextualConvention):
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
        *(("internal", 2),
          ("local", 4),
          ("other", 1),
          ("remote", 3))
    )



class DlcType(Integer32, TextualConvention):
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
        *(("llc", 3),
          ("na", 2),
          ("other", 1),
          ("qllc", 5),
          ("sdlc", 4))
    )



class LFSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(516,
              635,
              754,
              873,
              993,
              1112,
              1231,
              1350,
              1470,
              1542,
              1615,
              1688,
              1761,
              1833,
              1906,
              1979,
              2052,
              2345,
              2638,
              2932,
              3225,
              3518,
              3812,
              4105,
              4399,
              4865,
              5331,
              5798,
              6264,
              6730,
              7197,
              7663,
              8130,
              8539,
              8949,
              9358,
              9768,
              10178,
              10587,
              10997,
              11407,
              12199,
              12992,
              13785,
              14578,
              15370,
              16163,
              16956,
              17749,
              20730,
              23711,
              26693,
              29674,
              32655,
              38618,
              41600,
              44591,
              47583,
              50575,
              53567,
              56559,
              59551,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("lfs10178", 10178),
          ("lfs10587", 10587),
          ("lfs10997", 10997),
          ("lfs1112", 1112),
          ("lfs11407", 11407),
          ("lfs12199", 12199),
          ("lfs1231", 1231),
          ("lfs12992", 12992),
          ("lfs1350", 1350),
          ("lfs13785", 13785),
          ("lfs14578", 14578),
          ("lfs1470", 1470),
          ("lfs15370", 15370),
          ("lfs1542", 1542),
          ("lfs1615", 1615),
          ("lfs16163", 16163),
          ("lfs1688", 1688),
          ("lfs16956", 16956),
          ("lfs1761", 1761),
          ("lfs17749", 17749),
          ("lfs1833", 1833),
          ("lfs1906", 1906),
          ("lfs1979", 1979),
          ("lfs2052", 2052),
          ("lfs20730", 20730),
          ("lfs2345", 2345),
          ("lfs23711", 23711),
          ("lfs2638", 2638),
          ("lfs26693", 26693),
          ("lfs2932", 2932),
          ("lfs29674", 29674),
          ("lfs3225", 3225),
          ("lfs32655", 32655),
          ("lfs3518", 3518),
          ("lfs3812", 3812),
          ("lfs38618", 38618),
          ("lfs4105", 4105),
          ("lfs41600", 41600),
          ("lfs4399", 4399),
          ("lfs44591", 44591),
          ("lfs47583", 47583),
          ("lfs4865", 4865),
          ("lfs50575", 50575),
          ("lfs516", 516),
          ("lfs5331", 5331),
          ("lfs53567", 53567),
          ("lfs56559", 56559),
          ("lfs5798", 5798),
          ("lfs59551", 59551),
          ("lfs6264", 6264),
          ("lfs635", 635),
          ("lfs65535", 65535),
          ("lfs6730", 6730),
          ("lfs7197", 7197),
          ("lfs754", 754),
          ("lfs7663", 7663),
          ("lfs8130", 8130),
          ("lfs8539", 8539),
          ("lfs873", 873),
          ("lfs8949", 8949),
          ("lfs9358", 9358),
          ("lfs9768", 9768),
          ("lfs993", 993))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDlswMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDlswMIBObjects = _CiscoDlswMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1)
)
_CiscoDlswNode_ObjectIdentity = ObjectIdentity
ciscoDlswNode = _CiscoDlswNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1)
)


class _CiscoDlswVersion_Type(OctetString):
    """Custom type ciscoDlswVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CiscoDlswVersion_Type.__name__ = "OctetString"
_CiscoDlswVersion_Object = MibScalar
ciscoDlswVersion = _CiscoDlswVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 1),
    _CiscoDlswVersion_Type()
)
ciscoDlswVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswVersion.setStatus("current")


class _CiscoDlswVendorID_Type(OctetString):
    """Custom type ciscoDlswVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CiscoDlswVendorID_Type.__name__ = "OctetString"
_CiscoDlswVendorID_Object = MibScalar
ciscoDlswVendorID = _CiscoDlswVendorID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 2),
    _CiscoDlswVendorID_Type()
)
ciscoDlswVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswVendorID.setStatus("current")


class _CiscoDlswVersionString_Type(DisplayString):
    """Custom type ciscoDlswVersionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoDlswVersionString_Type.__name__ = "DisplayString"
_CiscoDlswVersionString_Object = MibScalar
ciscoDlswVersionString = _CiscoDlswVersionString_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 3),
    _CiscoDlswVersionString_Type()
)
ciscoDlswVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswVersionString.setStatus("current")


class _CiscoDlswStdPacingSupport_Type(Integer32):
    """Custom type ciscoDlswStdPacingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveRcvWindow", 2),
          ("fixedRcvWindow", 3),
          ("none", 1))
    )


_CiscoDlswStdPacingSupport_Type.__name__ = "Integer32"
_CiscoDlswStdPacingSupport_Object = MibScalar
ciscoDlswStdPacingSupport = _CiscoDlswStdPacingSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 4),
    _CiscoDlswStdPacingSupport_Type()
)
ciscoDlswStdPacingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswStdPacingSupport.setStatus("current")


class _CiscoDlswStatus_Type(Integer32):
    """Custom type ciscoDlswStatus based on Integer32"""
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


_CiscoDlswStatus_Type.__name__ = "Integer32"
_CiscoDlswStatus_Object = MibScalar
ciscoDlswStatus = _CiscoDlswStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 5),
    _CiscoDlswStatus_Type()
)
ciscoDlswStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswStatus.setStatus("current")
_CiscoDlswUpTime_Type = TimeTicks
_CiscoDlswUpTime_Object = MibScalar
ciscoDlswUpTime = _CiscoDlswUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 6),
    _CiscoDlswUpTime_Type()
)
ciscoDlswUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswUpTime.setStatus("current")


class _CiscoDlswVirtualSegmentLFSize_Type(LFSize):
    """Custom type ciscoDlswVirtualSegmentLFSize based on LFSize"""


_CiscoDlswVirtualSegmentLFSize_Object = MibScalar
ciscoDlswVirtualSegmentLFSize = _CiscoDlswVirtualSegmentLFSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 7),
    _CiscoDlswVirtualSegmentLFSize_Type()
)
ciscoDlswVirtualSegmentLFSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswVirtualSegmentLFSize.setStatus("current")
_CiscoDlswResourceNBExclusivity_Type = TruthValue
_CiscoDlswResourceNBExclusivity_Object = MibScalar
ciscoDlswResourceNBExclusivity = _CiscoDlswResourceNBExclusivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 8),
    _CiscoDlswResourceNBExclusivity_Type()
)
ciscoDlswResourceNBExclusivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswResourceNBExclusivity.setStatus("current")
_CiscoDlswResourceMacExclusivity_Type = TruthValue
_CiscoDlswResourceMacExclusivity_Object = MibScalar
ciscoDlswResourceMacExclusivity = _CiscoDlswResourceMacExclusivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 9),
    _CiscoDlswResourceMacExclusivity_Type()
)
ciscoDlswResourceMacExclusivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswResourceMacExclusivity.setStatus("current")
_CiscoDlswTrapControl_ObjectIdentity = ObjectIdentity
ciscoDlswTrapControl = _CiscoDlswTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 10)
)


class _CiscoDlswTrapCntlTConnPartnerReject_Type(Integer32):
    """Custom type ciscoDlswTrapCntlTConnPartnerReject based on Integer32"""
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
          ("partial", 3))
    )


_CiscoDlswTrapCntlTConnPartnerReject_Type.__name__ = "Integer32"
_CiscoDlswTrapCntlTConnPartnerReject_Object = MibScalar
ciscoDlswTrapCntlTConnPartnerReject = _CiscoDlswTrapCntlTConnPartnerReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 10, 1),
    _CiscoDlswTrapCntlTConnPartnerReject_Type()
)
ciscoDlswTrapCntlTConnPartnerReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTrapCntlTConnPartnerReject.setStatus("current")
_CiscoDlswTrapCntlTConnProtViolation_Type = TruthValue
_CiscoDlswTrapCntlTConnProtViolation_Object = MibScalar
ciscoDlswTrapCntlTConnProtViolation = _CiscoDlswTrapCntlTConnProtViolation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 10, 2),
    _CiscoDlswTrapCntlTConnProtViolation_Type()
)
ciscoDlswTrapCntlTConnProtViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTrapCntlTConnProtViolation.setStatus("current")


class _CiscoDlswTrapCntlTConn_Type(Integer32):
    """Custom type ciscoDlswTrapCntlTConn based on Integer32"""
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
          ("partial", 3))
    )


_CiscoDlswTrapCntlTConn_Type.__name__ = "Integer32"
_CiscoDlswTrapCntlTConn_Object = MibScalar
ciscoDlswTrapCntlTConn = _CiscoDlswTrapCntlTConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 10, 3),
    _CiscoDlswTrapCntlTConn_Type()
)
ciscoDlswTrapCntlTConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTrapCntlTConn.setStatus("current")


class _CiscoDlswTrapCntlCircuit_Type(Integer32):
    """Custom type ciscoDlswTrapCntlCircuit based on Integer32"""
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
          ("partial", 3))
    )


_CiscoDlswTrapCntlCircuit_Type.__name__ = "Integer32"
_CiscoDlswTrapCntlCircuit_Object = MibScalar
ciscoDlswTrapCntlCircuit = _CiscoDlswTrapCntlCircuit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 1, 10, 4),
    _CiscoDlswTrapCntlCircuit_Type()
)
ciscoDlswTrapCntlCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTrapCntlCircuit.setStatus("current")
_CiscoDlswTConn_ObjectIdentity = ObjectIdentity
ciscoDlswTConn = _CiscoDlswTConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2)
)
_CiscoDlswTConnStat_ObjectIdentity = ObjectIdentity
ciscoDlswTConnStat = _CiscoDlswTConnStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 1)
)
_CiscoDlswTConnStatActiveConnections_Type = Gauge32
_CiscoDlswTConnStatActiveConnections_Object = MibScalar
ciscoDlswTConnStatActiveConnections = _CiscoDlswTConnStatActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 1, 1),
    _CiscoDlswTConnStatActiveConnections_Type()
)
ciscoDlswTConnStatActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnStatActiveConnections.setStatus("current")
_CiscoDlswTConnStatCloseIdles_Type = Counter32
_CiscoDlswTConnStatCloseIdles_Object = MibScalar
ciscoDlswTConnStatCloseIdles = _CiscoDlswTConnStatCloseIdles_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 1, 2),
    _CiscoDlswTConnStatCloseIdles_Type()
)
ciscoDlswTConnStatCloseIdles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnStatCloseIdles.setStatus("current")
_CiscoDlswTConnStatCloseBusys_Type = Counter32
_CiscoDlswTConnStatCloseBusys_Object = MibScalar
ciscoDlswTConnStatCloseBusys = _CiscoDlswTConnStatCloseBusys_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 1, 3),
    _CiscoDlswTConnStatCloseBusys_Type()
)
ciscoDlswTConnStatCloseBusys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnStatCloseBusys.setStatus("current")
_CiscoDlswTConnConfigTable_Object = MibTable
ciscoDlswTConnConfigTable = _CiscoDlswTConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigTable.setStatus("current")
_CiscoDlswTConnConfigEntry_Object = MibTableRow
ciscoDlswTConnConfigEntry = _CiscoDlswTConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1)
)
ciscoDlswTConnConfigEntry.setIndexNames(
    (0, "CISCO-DLSW-MIB", "ciscoDlswTConnConfigIndex"),
)
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigEntry.setStatus("current")


class _CiscoDlswTConnConfigIndex_Type(Integer32):
    """Custom type ciscoDlswTConnConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_CiscoDlswTConnConfigIndex_Type.__name__ = "Integer32"
_CiscoDlswTConnConfigIndex_Object = MibTableColumn
ciscoDlswTConnConfigIndex = _CiscoDlswTConnConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 1),
    _CiscoDlswTConnConfigIndex_Type()
)
ciscoDlswTConnConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigIndex.setStatus("current")
_CiscoDlswTConnConfigTDomain_Type = ObjectIdentifier
_CiscoDlswTConnConfigTDomain_Object = MibTableColumn
ciscoDlswTConnConfigTDomain = _CiscoDlswTConnConfigTDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 2),
    _CiscoDlswTConnConfigTDomain_Type()
)
ciscoDlswTConnConfigTDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigTDomain.setStatus("current")
_CiscoDlswTConnConfigLocalTAddr_Type = TAddress
_CiscoDlswTConnConfigLocalTAddr_Object = MibTableColumn
ciscoDlswTConnConfigLocalTAddr = _CiscoDlswTConnConfigLocalTAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 3),
    _CiscoDlswTConnConfigLocalTAddr_Type()
)
ciscoDlswTConnConfigLocalTAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigLocalTAddr.setStatus("current")
_CiscoDlswTConnConfigRemoteTAddr_Type = TAddress
_CiscoDlswTConnConfigRemoteTAddr_Object = MibTableColumn
ciscoDlswTConnConfigRemoteTAddr = _CiscoDlswTConnConfigRemoteTAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 4),
    _CiscoDlswTConnConfigRemoteTAddr_Type()
)
ciscoDlswTConnConfigRemoteTAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigRemoteTAddr.setStatus("current")
_CiscoDlswTConnConfigLastModifyTime_Type = DlswTimeStamp
_CiscoDlswTConnConfigLastModifyTime_Object = MibTableColumn
ciscoDlswTConnConfigLastModifyTime = _CiscoDlswTConnConfigLastModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 5),
    _CiscoDlswTConnConfigLastModifyTime_Type()
)
ciscoDlswTConnConfigLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigLastModifyTime.setStatus("current")


class _CiscoDlswTConnConfigEntryType_Type(Integer32):
    """Custom type ciscoDlswTConnConfigEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 2),
          ("group", 3),
          ("individual", 1))
    )


_CiscoDlswTConnConfigEntryType_Type.__name__ = "Integer32"
_CiscoDlswTConnConfigEntryType_Object = MibTableColumn
ciscoDlswTConnConfigEntryType = _CiscoDlswTConnConfigEntryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 6),
    _CiscoDlswTConnConfigEntryType_Type()
)
ciscoDlswTConnConfigEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigEntryType.setStatus("current")
_CiscoDlswTConnConfigGroupDefinition_Type = InstancePointer
_CiscoDlswTConnConfigGroupDefinition_Object = MibTableColumn
ciscoDlswTConnConfigGroupDefinition = _CiscoDlswTConnConfigGroupDefinition_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 7),
    _CiscoDlswTConnConfigGroupDefinition_Type()
)
ciscoDlswTConnConfigGroupDefinition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigGroupDefinition.setStatus("current")


class _CiscoDlswTConnConfigSetupType_Type(Integer32):
    """Custom type ciscoDlswTConnConfigSetupType based on Integer32"""
    defaultValue = 2

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
        *(("activeOnDemand", 3),
          ("activePersistent", 2),
          ("excluded", 5),
          ("other", 1),
          ("passive", 4))
    )


_CiscoDlswTConnConfigSetupType_Type.__name__ = "Integer32"
_CiscoDlswTConnConfigSetupType_Object = MibTableColumn
ciscoDlswTConnConfigSetupType = _CiscoDlswTConnConfigSetupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 8),
    _CiscoDlswTConnConfigSetupType_Type()
)
ciscoDlswTConnConfigSetupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigSetupType.setStatus("current")


class _CiscoDlswTConnConfigSapList_Type(OctetString):
    """Custom type ciscoDlswTConnConfigSapList based on OctetString"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CiscoDlswTConnConfigSapList_Type.__name__ = "OctetString"
_CiscoDlswTConnConfigSapList_Object = MibTableColumn
ciscoDlswTConnConfigSapList = _CiscoDlswTConnConfigSapList_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 9),
    _CiscoDlswTConnConfigSapList_Type()
)
ciscoDlswTConnConfigSapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigSapList.setStatus("current")


class _CiscoDlswTConnConfigAdvertiseMacNB_Type(TruthValue):
    """Custom type ciscoDlswTConnConfigAdvertiseMacNB based on TruthValue"""


_CiscoDlswTConnConfigAdvertiseMacNB_Object = MibTableColumn
ciscoDlswTConnConfigAdvertiseMacNB = _CiscoDlswTConnConfigAdvertiseMacNB_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 10),
    _CiscoDlswTConnConfigAdvertiseMacNB_Type()
)
ciscoDlswTConnConfigAdvertiseMacNB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigAdvertiseMacNB.setStatus("current")


class _CiscoDlswTConnConfigInitCirRecvWndw_Type(Integer32):
    """Custom type ciscoDlswTConnConfigInitCirRecvWndw based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoDlswTConnConfigInitCirRecvWndw_Type.__name__ = "Integer32"
_CiscoDlswTConnConfigInitCirRecvWndw_Object = MibTableColumn
ciscoDlswTConnConfigInitCirRecvWndw = _CiscoDlswTConnConfigInitCirRecvWndw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 11),
    _CiscoDlswTConnConfigInitCirRecvWndw_Type()
)
ciscoDlswTConnConfigInitCirRecvWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigInitCirRecvWndw.setStatus("current")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigInitCirRecvWndw.setUnits("SSP messages")
_CiscoDlswTConnConfigOpens_Type = Counter32
_CiscoDlswTConnConfigOpens_Object = MibTableColumn
ciscoDlswTConnConfigOpens = _CiscoDlswTConnConfigOpens_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 12),
    _CiscoDlswTConnConfigOpens_Type()
)
ciscoDlswTConnConfigOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigOpens.setStatus("current")
_CiscoDlswTConnConfigRowStatus_Type = RowStatus
_CiscoDlswTConnConfigRowStatus_Object = MibTableColumn
ciscoDlswTConnConfigRowStatus = _CiscoDlswTConnConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 2, 1, 13),
    _CiscoDlswTConnConfigRowStatus_Type()
)
ciscoDlswTConnConfigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigRowStatus.setStatus("current")
_CiscoDlswTConnOperTable_Object = MibTable
ciscoDlswTConnOperTable = _CiscoDlswTConnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ciscoDlswTConnOperTable.setStatus("current")
_CiscoDlswTConnOperEntry_Object = MibTableRow
ciscoDlswTConnOperEntry = _CiscoDlswTConnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1)
)
ciscoDlswTConnOperEntry.setIndexNames(
    (0, "CISCO-DLSW-MIB", "ciscoDlswTConnOperTDomain"),
    (0, "CISCO-DLSW-MIB", "ciscoDlswTConnOperRemoteTAddr"),
)
if mibBuilder.loadTexts:
    ciscoDlswTConnOperEntry.setStatus("current")
_CiscoDlswTConnOperTDomain_Type = ObjectIdentifier
_CiscoDlswTConnOperTDomain_Object = MibTableColumn
ciscoDlswTConnOperTDomain = _CiscoDlswTConnOperTDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 1),
    _CiscoDlswTConnOperTDomain_Type()
)
ciscoDlswTConnOperTDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperTDomain.setStatus("current")
_CiscoDlswTConnOperLocalTAddr_Type = TAddress
_CiscoDlswTConnOperLocalTAddr_Object = MibTableColumn
ciscoDlswTConnOperLocalTAddr = _CiscoDlswTConnOperLocalTAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 2),
    _CiscoDlswTConnOperLocalTAddr_Type()
)
ciscoDlswTConnOperLocalTAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperLocalTAddr.setStatus("current")
_CiscoDlswTConnOperRemoteTAddr_Type = TAddress
_CiscoDlswTConnOperRemoteTAddr_Object = MibTableColumn
ciscoDlswTConnOperRemoteTAddr = _CiscoDlswTConnOperRemoteTAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 3),
    _CiscoDlswTConnOperRemoteTAddr_Type()
)
ciscoDlswTConnOperRemoteTAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperRemoteTAddr.setStatus("current")
_CiscoDlswTConnOperEntryTime_Type = DlswTimeStamp
_CiscoDlswTConnOperEntryTime_Object = MibTableColumn
ciscoDlswTConnOperEntryTime = _CiscoDlswTConnOperEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 4),
    _CiscoDlswTConnOperEntryTime_Type()
)
ciscoDlswTConnOperEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperEntryTime.setStatus("current")
_CiscoDlswTConnOperConnectTime_Type = DlswTimeStamp
_CiscoDlswTConnOperConnectTime_Object = MibTableColumn
ciscoDlswTConnOperConnectTime = _CiscoDlswTConnOperConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 5),
    _CiscoDlswTConnOperConnectTime_Type()
)
ciscoDlswTConnOperConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperConnectTime.setStatus("current")


class _CiscoDlswTConnOperState_Type(Integer32):
    """Custom type ciscoDlswTConnOperState based on Integer32"""
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
        *(("connected", 3),
          ("connecting", 1),
          ("disconnected", 6),
          ("disconnecting", 5),
          ("initCapExchange", 2),
          ("quiescing", 4))
    )


_CiscoDlswTConnOperState_Type.__name__ = "Integer32"
_CiscoDlswTConnOperState_Object = MibTableColumn
ciscoDlswTConnOperState = _CiscoDlswTConnOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 6),
    _CiscoDlswTConnOperState_Type()
)
ciscoDlswTConnOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperState.setStatus("current")


class _CiscoDlswTConnOperConfigIndex_Type(Integer32):
    """Custom type ciscoDlswTConnOperConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_CiscoDlswTConnOperConfigIndex_Type.__name__ = "Integer32"
_CiscoDlswTConnOperConfigIndex_Object = MibTableColumn
ciscoDlswTConnOperConfigIndex = _CiscoDlswTConnOperConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 7),
    _CiscoDlswTConnOperConfigIndex_Type()
)
ciscoDlswTConnOperConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperConfigIndex.setStatus("current")


class _CiscoDlswTConnOperFlowCntlMode_Type(Integer32):
    """Custom type ciscoDlswTConnOperFlowCntlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("pacing", 2),
          ("undetermined", 1))
    )


_CiscoDlswTConnOperFlowCntlMode_Type.__name__ = "Integer32"
_CiscoDlswTConnOperFlowCntlMode_Object = MibTableColumn
ciscoDlswTConnOperFlowCntlMode = _CiscoDlswTConnOperFlowCntlMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 8),
    _CiscoDlswTConnOperFlowCntlMode_Type()
)
ciscoDlswTConnOperFlowCntlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperFlowCntlMode.setStatus("current")


class _CiscoDlswTConnOperPartnerVersion_Type(OctetString):
    """Custom type ciscoDlswTConnOperPartnerVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )


_CiscoDlswTConnOperPartnerVersion_Type.__name__ = "OctetString"
_CiscoDlswTConnOperPartnerVersion_Object = MibTableColumn
ciscoDlswTConnOperPartnerVersion = _CiscoDlswTConnOperPartnerVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 9),
    _CiscoDlswTConnOperPartnerVersion_Type()
)
ciscoDlswTConnOperPartnerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperPartnerVersion.setStatus("current")


class _CiscoDlswTConnOperPartnerVendorID_Type(OctetString):
    """Custom type ciscoDlswTConnOperPartnerVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 3),
    )


_CiscoDlswTConnOperPartnerVendorID_Type.__name__ = "OctetString"
_CiscoDlswTConnOperPartnerVendorID_Object = MibTableColumn
ciscoDlswTConnOperPartnerVendorID = _CiscoDlswTConnOperPartnerVendorID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 10),
    _CiscoDlswTConnOperPartnerVendorID_Type()
)
ciscoDlswTConnOperPartnerVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperPartnerVendorID.setStatus("current")


class _CiscoDlswTConnOperPartnerVersionStr_Type(DisplayString):
    """Custom type ciscoDlswTConnOperPartnerVersionStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_CiscoDlswTConnOperPartnerVersionStr_Type.__name__ = "DisplayString"
_CiscoDlswTConnOperPartnerVersionStr_Object = MibTableColumn
ciscoDlswTConnOperPartnerVersionStr = _CiscoDlswTConnOperPartnerVersionStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 11),
    _CiscoDlswTConnOperPartnerVersionStr_Type()
)
ciscoDlswTConnOperPartnerVersionStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperPartnerVersionStr.setStatus("current")


class _CiscoDlswTConnOperPartnerInitPacingWndw_Type(Integer32):
    """Custom type ciscoDlswTConnOperPartnerInitPacingWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoDlswTConnOperPartnerInitPacingWndw_Type.__name__ = "Integer32"
_CiscoDlswTConnOperPartnerInitPacingWndw_Object = MibTableColumn
ciscoDlswTConnOperPartnerInitPacingWndw = _CiscoDlswTConnOperPartnerInitPacingWndw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 12),
    _CiscoDlswTConnOperPartnerInitPacingWndw_Type()
)
ciscoDlswTConnOperPartnerInitPacingWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperPartnerInitPacingWndw.setStatus("current")


class _CiscoDlswTConnOperPartnerSapList_Type(OctetString):
    """Custom type ciscoDlswTConnOperPartnerSapList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_CiscoDlswTConnOperPartnerSapList_Type.__name__ = "OctetString"
_CiscoDlswTConnOperPartnerSapList_Object = MibTableColumn
ciscoDlswTConnOperPartnerSapList = _CiscoDlswTConnOperPartnerSapList_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 13),
    _CiscoDlswTConnOperPartnerSapList_Type()
)
ciscoDlswTConnOperPartnerSapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperPartnerSapList.setStatus("current")
_CiscoDlswTConnOperPartnerNBExcl_Type = TruthValue
_CiscoDlswTConnOperPartnerNBExcl_Object = MibTableColumn
ciscoDlswTConnOperPartnerNBExcl = _CiscoDlswTConnOperPartnerNBExcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 14),
    _CiscoDlswTConnOperPartnerNBExcl_Type()
)
ciscoDlswTConnOperPartnerNBExcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperPartnerNBExcl.setStatus("current")
_CiscoDlswTConnOperPartnerMacExcl_Type = TruthValue
_CiscoDlswTConnOperPartnerMacExcl_Object = MibTableColumn
ciscoDlswTConnOperPartnerMacExcl = _CiscoDlswTConnOperPartnerMacExcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 15),
    _CiscoDlswTConnOperPartnerMacExcl_Type()
)
ciscoDlswTConnOperPartnerMacExcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperPartnerMacExcl.setStatus("current")


class _CiscoDlswTConnOperPartnerNBInfo_Type(Integer32):
    """Custom type ciscoDlswTConnOperPartnerNBInfo based on Integer32"""
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
        *(("complete", 3),
          ("none", 1),
          ("notApplicable", 4),
          ("partial", 2))
    )


_CiscoDlswTConnOperPartnerNBInfo_Type.__name__ = "Integer32"
_CiscoDlswTConnOperPartnerNBInfo_Object = MibTableColumn
ciscoDlswTConnOperPartnerNBInfo = _CiscoDlswTConnOperPartnerNBInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 16),
    _CiscoDlswTConnOperPartnerNBInfo_Type()
)
ciscoDlswTConnOperPartnerNBInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperPartnerNBInfo.setStatus("current")


class _CiscoDlswTConnOperPartnerMacInfo_Type(Integer32):
    """Custom type ciscoDlswTConnOperPartnerMacInfo based on Integer32"""
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
        *(("complete", 3),
          ("none", 1),
          ("notApplicable", 4),
          ("partial", 2))
    )


_CiscoDlswTConnOperPartnerMacInfo_Type.__name__ = "Integer32"
_CiscoDlswTConnOperPartnerMacInfo_Object = MibTableColumn
ciscoDlswTConnOperPartnerMacInfo = _CiscoDlswTConnOperPartnerMacInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 17),
    _CiscoDlswTConnOperPartnerMacInfo_Type()
)
ciscoDlswTConnOperPartnerMacInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperPartnerMacInfo.setStatus("current")
_CiscoDlswTConnOperDiscTime_Type = DlswTimeStamp
_CiscoDlswTConnOperDiscTime_Object = MibTableColumn
ciscoDlswTConnOperDiscTime = _CiscoDlswTConnOperDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 18),
    _CiscoDlswTConnOperDiscTime_Type()
)
ciscoDlswTConnOperDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperDiscTime.setStatus("current")


class _CiscoDlswTConnOperDiscReason_Type(Integer32):
    """Custom type ciscoDlswTConnOperDiscReason based on Integer32"""
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
        *(("capExFailed", 2),
          ("lastCircuitDiscd", 5),
          ("operatorCommand", 4),
          ("other", 1),
          ("protocolError", 6),
          ("transportLayerDisc", 3))
    )


_CiscoDlswTConnOperDiscReason_Type.__name__ = "Integer32"
_CiscoDlswTConnOperDiscReason_Object = MibTableColumn
ciscoDlswTConnOperDiscReason = _CiscoDlswTConnOperDiscReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 19),
    _CiscoDlswTConnOperDiscReason_Type()
)
ciscoDlswTConnOperDiscReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperDiscReason.setStatus("current")


class _CiscoDlswTConnOperDiscActiveCir_Type(Integer32):
    """Custom type ciscoDlswTConnOperDiscActiveCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_CiscoDlswTConnOperDiscActiveCir_Type.__name__ = "Integer32"
_CiscoDlswTConnOperDiscActiveCir_Object = MibTableColumn
ciscoDlswTConnOperDiscActiveCir = _CiscoDlswTConnOperDiscActiveCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 20),
    _CiscoDlswTConnOperDiscActiveCir_Type()
)
ciscoDlswTConnOperDiscActiveCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperDiscActiveCir.setStatus("current")
_CiscoDlswTConnOperInDataPkts_Type = Counter32
_CiscoDlswTConnOperInDataPkts_Object = MibTableColumn
ciscoDlswTConnOperInDataPkts = _CiscoDlswTConnOperInDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 21),
    _CiscoDlswTConnOperInDataPkts_Type()
)
ciscoDlswTConnOperInDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperInDataPkts.setStatus("current")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperInDataPkts.setUnits("SSP messages")
_CiscoDlswTConnOperOutDataPkts_Type = Counter32
_CiscoDlswTConnOperOutDataPkts_Object = MibTableColumn
ciscoDlswTConnOperOutDataPkts = _CiscoDlswTConnOperOutDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 22),
    _CiscoDlswTConnOperOutDataPkts_Type()
)
ciscoDlswTConnOperOutDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperOutDataPkts.setStatus("current")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperOutDataPkts.setUnits("SSP messages")
_CiscoDlswTConnOperInDataOctets_Type = Counter32
_CiscoDlswTConnOperInDataOctets_Object = MibTableColumn
ciscoDlswTConnOperInDataOctets = _CiscoDlswTConnOperInDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 23),
    _CiscoDlswTConnOperInDataOctets_Type()
)
ciscoDlswTConnOperInDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperInDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperInDataOctets.setUnits("octets")
_CiscoDlswTConnOperOutDataOctets_Type = Counter32
_CiscoDlswTConnOperOutDataOctets_Object = MibTableColumn
ciscoDlswTConnOperOutDataOctets = _CiscoDlswTConnOperOutDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 24),
    _CiscoDlswTConnOperOutDataOctets_Type()
)
ciscoDlswTConnOperOutDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperOutDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperOutDataOctets.setUnits("octets")
_CiscoDlswTConnOperInCntlPkts_Type = Counter32
_CiscoDlswTConnOperInCntlPkts_Object = MibTableColumn
ciscoDlswTConnOperInCntlPkts = _CiscoDlswTConnOperInCntlPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 25),
    _CiscoDlswTConnOperInCntlPkts_Type()
)
ciscoDlswTConnOperInCntlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperInCntlPkts.setStatus("current")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperInCntlPkts.setUnits("SSP messages")
_CiscoDlswTConnOperOutCntlPkts_Type = Counter32
_CiscoDlswTConnOperOutCntlPkts_Object = MibTableColumn
ciscoDlswTConnOperOutCntlPkts = _CiscoDlswTConnOperOutCntlPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 26),
    _CiscoDlswTConnOperOutCntlPkts_Type()
)
ciscoDlswTConnOperOutCntlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperOutCntlPkts.setStatus("current")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperOutCntlPkts.setUnits("SSP messages")
_CiscoDlswTConnOperCURexSents_Type = Counter32
_CiscoDlswTConnOperCURexSents_Object = MibTableColumn
ciscoDlswTConnOperCURexSents = _CiscoDlswTConnOperCURexSents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 27),
    _CiscoDlswTConnOperCURexSents_Type()
)
ciscoDlswTConnOperCURexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperCURexSents.setStatus("current")
_CiscoDlswTConnOperICRexRcvds_Type = Counter32
_CiscoDlswTConnOperICRexRcvds_Object = MibTableColumn
ciscoDlswTConnOperICRexRcvds = _CiscoDlswTConnOperICRexRcvds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 28),
    _CiscoDlswTConnOperICRexRcvds_Type()
)
ciscoDlswTConnOperICRexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperICRexRcvds.setStatus("current")
_CiscoDlswTConnOperCURexRcvds_Type = Counter32
_CiscoDlswTConnOperCURexRcvds_Object = MibTableColumn
ciscoDlswTConnOperCURexRcvds = _CiscoDlswTConnOperCURexRcvds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 29),
    _CiscoDlswTConnOperCURexRcvds_Type()
)
ciscoDlswTConnOperCURexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperCURexRcvds.setStatus("current")
_CiscoDlswTConnOperICRexSents_Type = Counter32
_CiscoDlswTConnOperICRexSents_Object = MibTableColumn
ciscoDlswTConnOperICRexSents = _CiscoDlswTConnOperICRexSents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 30),
    _CiscoDlswTConnOperICRexSents_Type()
)
ciscoDlswTConnOperICRexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperICRexSents.setStatus("current")
_CiscoDlswTConnOperNQexSents_Type = Counter32
_CiscoDlswTConnOperNQexSents_Object = MibTableColumn
ciscoDlswTConnOperNQexSents = _CiscoDlswTConnOperNQexSents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 31),
    _CiscoDlswTConnOperNQexSents_Type()
)
ciscoDlswTConnOperNQexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperNQexSents.setStatus("current")
_CiscoDlswTConnOperNRexRcvds_Type = Counter32
_CiscoDlswTConnOperNRexRcvds_Object = MibTableColumn
ciscoDlswTConnOperNRexRcvds = _CiscoDlswTConnOperNRexRcvds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 32),
    _CiscoDlswTConnOperNRexRcvds_Type()
)
ciscoDlswTConnOperNRexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperNRexRcvds.setStatus("current")
_CiscoDlswTConnOperNQexRcvds_Type = Counter32
_CiscoDlswTConnOperNQexRcvds_Object = MibTableColumn
ciscoDlswTConnOperNQexRcvds = _CiscoDlswTConnOperNQexRcvds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 33),
    _CiscoDlswTConnOperNQexRcvds_Type()
)
ciscoDlswTConnOperNQexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperNQexRcvds.setStatus("current")
_CiscoDlswTConnOperNRexSents_Type = Counter32
_CiscoDlswTConnOperNRexSents_Object = MibTableColumn
ciscoDlswTConnOperNRexSents = _CiscoDlswTConnOperNRexSents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 34),
    _CiscoDlswTConnOperNRexSents_Type()
)
ciscoDlswTConnOperNRexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperNRexSents.setStatus("current")
_CiscoDlswTConnOperCirCreates_Type = Counter32
_CiscoDlswTConnOperCirCreates_Object = MibTableColumn
ciscoDlswTConnOperCirCreates = _CiscoDlswTConnOperCirCreates_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 35),
    _CiscoDlswTConnOperCirCreates_Type()
)
ciscoDlswTConnOperCirCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperCirCreates.setStatus("current")
_CiscoDlswTConnOperCircuits_Type = Gauge32
_CiscoDlswTConnOperCircuits_Object = MibTableColumn
ciscoDlswTConnOperCircuits = _CiscoDlswTConnOperCircuits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 3, 1, 36),
    _CiscoDlswTConnOperCircuits_Type()
)
ciscoDlswTConnOperCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnOperCircuits.setStatus("current")
_CiscoDlswTConnSpecific_ObjectIdentity = ObjectIdentity
ciscoDlswTConnSpecific = _CiscoDlswTConnSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 4)
)
_CiscoDlswTConnTcp_ObjectIdentity = ObjectIdentity
ciscoDlswTConnTcp = _CiscoDlswTConnTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 4, 1)
)
_CiscoDlswTConnTcpConfigTable_Object = MibTable
ciscoDlswTConnTcpConfigTable = _CiscoDlswTConnTcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpConfigTable.setStatus("current")
_CiscoDlswTConnTcpConfigEntry_Object = MibTableRow
ciscoDlswTConnTcpConfigEntry = _CiscoDlswTConnTcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 4, 1, 1, 1)
)
ciscoDlswTConnTcpConfigEntry.setIndexNames(
    (0, "CISCO-DLSW-MIB", "ciscoDlswTConnConfigIndex"),
)
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpConfigEntry.setStatus("current")


class _CiscoDlswTConnTcpConfigKeepAliveInt_Type(Integer32):
    """Custom type ciscoDlswTConnTcpConfigKeepAliveInt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_CiscoDlswTConnTcpConfigKeepAliveInt_Type.__name__ = "Integer32"
_CiscoDlswTConnTcpConfigKeepAliveInt_Object = MibTableColumn
ciscoDlswTConnTcpConfigKeepAliveInt = _CiscoDlswTConnTcpConfigKeepAliveInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 4, 1, 1, 1, 1),
    _CiscoDlswTConnTcpConfigKeepAliveInt_Type()
)
ciscoDlswTConnTcpConfigKeepAliveInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpConfigKeepAliveInt.setStatus("current")
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpConfigKeepAliveInt.setUnits("seconds")


class _CiscoDlswTConnTcpConfigTcpConnections_Type(Integer32):
    """Custom type ciscoDlswTConnTcpConfigTcpConnections based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CiscoDlswTConnTcpConfigTcpConnections_Type.__name__ = "Integer32"
_CiscoDlswTConnTcpConfigTcpConnections_Object = MibTableColumn
ciscoDlswTConnTcpConfigTcpConnections = _CiscoDlswTConnTcpConfigTcpConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 4, 1, 1, 1, 2),
    _CiscoDlswTConnTcpConfigTcpConnections_Type()
)
ciscoDlswTConnTcpConfigTcpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpConfigTcpConnections.setStatus("current")


class _CiscoDlswTConnTcpConfigMaxSegmentSize_Type(Integer32):
    """Custom type ciscoDlswTConnTcpConfigMaxSegmentSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoDlswTConnTcpConfigMaxSegmentSize_Type.__name__ = "Integer32"
_CiscoDlswTConnTcpConfigMaxSegmentSize_Object = MibTableColumn
ciscoDlswTConnTcpConfigMaxSegmentSize = _CiscoDlswTConnTcpConfigMaxSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 4, 1, 1, 1, 3),
    _CiscoDlswTConnTcpConfigMaxSegmentSize_Type()
)
ciscoDlswTConnTcpConfigMaxSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpConfigMaxSegmentSize.setStatus("current")
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpConfigMaxSegmentSize.setUnits("packets")
_CiscoDlswTConnTcpOperTable_Object = MibTable
ciscoDlswTConnTcpOperTable = _CiscoDlswTConnTcpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpOperTable.setStatus("current")
_CiscoDlswTConnTcpOperEntry_Object = MibTableRow
ciscoDlswTConnTcpOperEntry = _CiscoDlswTConnTcpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 4, 1, 2, 1)
)
ciscoDlswTConnTcpOperEntry.setIndexNames(
    (0, "CISCO-DLSW-MIB", "ciscoDlswTConnOperTDomain"),
    (0, "CISCO-DLSW-MIB", "ciscoDlswTConnOperRemoteTAddr"),
)
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpOperEntry.setStatus("current")


class _CiscoDlswTConnTcpOperKeepAliveInt_Type(Integer32):
    """Custom type ciscoDlswTConnTcpOperKeepAliveInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_CiscoDlswTConnTcpOperKeepAliveInt_Type.__name__ = "Integer32"
_CiscoDlswTConnTcpOperKeepAliveInt_Object = MibTableColumn
ciscoDlswTConnTcpOperKeepAliveInt = _CiscoDlswTConnTcpOperKeepAliveInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 4, 1, 2, 1, 1),
    _CiscoDlswTConnTcpOperKeepAliveInt_Type()
)
ciscoDlswTConnTcpOperKeepAliveInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpOperKeepAliveInt.setStatus("current")
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpOperKeepAliveInt.setUnits("seconds")


class _CiscoDlswTConnTcpOperPrefTcpConnections_Type(Integer32):
    """Custom type ciscoDlswTConnTcpOperPrefTcpConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CiscoDlswTConnTcpOperPrefTcpConnections_Type.__name__ = "Integer32"
_CiscoDlswTConnTcpOperPrefTcpConnections_Object = MibTableColumn
ciscoDlswTConnTcpOperPrefTcpConnections = _CiscoDlswTConnTcpOperPrefTcpConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 4, 1, 2, 1, 2),
    _CiscoDlswTConnTcpOperPrefTcpConnections_Type()
)
ciscoDlswTConnTcpOperPrefTcpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpOperPrefTcpConnections.setStatus("current")


class _CiscoDlswTConnTcpOperTcpConnections_Type(Integer32):
    """Custom type ciscoDlswTConnTcpOperTcpConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CiscoDlswTConnTcpOperTcpConnections_Type.__name__ = "Integer32"
_CiscoDlswTConnTcpOperTcpConnections_Object = MibTableColumn
ciscoDlswTConnTcpOperTcpConnections = _CiscoDlswTConnTcpOperTcpConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 2, 4, 1, 2, 1, 3),
    _CiscoDlswTConnTcpOperTcpConnections_Type()
)
ciscoDlswTConnTcpOperTcpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpOperTcpConnections.setStatus("current")
_CiscoDlswInterface_ObjectIdentity = ObjectIdentity
ciscoDlswInterface = _CiscoDlswInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 3)
)
_CiscoDlswIfTable_Object = MibTable
ciscoDlswIfTable = _CiscoDlswIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoDlswIfTable.setStatus("current")
_CiscoDlswIfEntry_Object = MibTableRow
ciscoDlswIfEntry = _CiscoDlswIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 3, 1, 1)
)
ciscoDlswIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciscoDlswIfEntry.setStatus("current")
_CiscoDlswIfRowStatus_Type = RowStatus
_CiscoDlswIfRowStatus_Object = MibTableColumn
ciscoDlswIfRowStatus = _CiscoDlswIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 3, 1, 1, 1),
    _CiscoDlswIfRowStatus_Type()
)
ciscoDlswIfRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswIfRowStatus.setStatus("current")


class _CiscoDlswIfVirtualSegment_Type(Integer32):
    """Custom type ciscoDlswIfVirtualSegment based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_CiscoDlswIfVirtualSegment_Type.__name__ = "Integer32"
_CiscoDlswIfVirtualSegment_Object = MibTableColumn
ciscoDlswIfVirtualSegment = _CiscoDlswIfVirtualSegment_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 3, 1, 1, 2),
    _CiscoDlswIfVirtualSegment_Type()
)
ciscoDlswIfVirtualSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswIfVirtualSegment.setStatus("current")


class _CiscoDlswIfSapList_Type(OctetString):
    """Custom type ciscoDlswIfSapList based on OctetString"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CiscoDlswIfSapList_Type.__name__ = "OctetString"
_CiscoDlswIfSapList_Object = MibTableColumn
ciscoDlswIfSapList = _CiscoDlswIfSapList_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 3, 1, 1, 3),
    _CiscoDlswIfSapList_Type()
)
ciscoDlswIfSapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswIfSapList.setStatus("current")
_CiscoDlswDirectory_ObjectIdentity = ObjectIdentity
ciscoDlswDirectory = _CiscoDlswDirectory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4)
)
_CiscoDlswDirStat_ObjectIdentity = ObjectIdentity
ciscoDlswDirStat = _CiscoDlswDirStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 1)
)
_CiscoDlswDirMacEntries_Type = Gauge32
_CiscoDlswDirMacEntries_Object = MibScalar
ciscoDlswDirMacEntries = _CiscoDlswDirMacEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 1, 1),
    _CiscoDlswDirMacEntries_Type()
)
ciscoDlswDirMacEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirMacEntries.setStatus("current")
_CiscoDlswDirMacCacheHits_Type = Counter32
_CiscoDlswDirMacCacheHits_Object = MibScalar
ciscoDlswDirMacCacheHits = _CiscoDlswDirMacCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 1, 2),
    _CiscoDlswDirMacCacheHits_Type()
)
ciscoDlswDirMacCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirMacCacheHits.setStatus("current")
_CiscoDlswDirMacCacheMisses_Type = Counter32
_CiscoDlswDirMacCacheMisses_Object = MibScalar
ciscoDlswDirMacCacheMisses = _CiscoDlswDirMacCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 1, 3),
    _CiscoDlswDirMacCacheMisses_Type()
)
ciscoDlswDirMacCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirMacCacheMisses.setStatus("current")
_CiscoDlswDirNBEntries_Type = Gauge32
_CiscoDlswDirNBEntries_Object = MibScalar
ciscoDlswDirNBEntries = _CiscoDlswDirNBEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 1, 4),
    _CiscoDlswDirNBEntries_Type()
)
ciscoDlswDirNBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirNBEntries.setStatus("current")
_CiscoDlswDirNBCacheHits_Type = Counter32
_CiscoDlswDirNBCacheHits_Object = MibScalar
ciscoDlswDirNBCacheHits = _CiscoDlswDirNBCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 1, 5),
    _CiscoDlswDirNBCacheHits_Type()
)
ciscoDlswDirNBCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirNBCacheHits.setStatus("current")
_CiscoDlswDirNBCacheMisses_Type = Counter32
_CiscoDlswDirNBCacheMisses_Object = MibScalar
ciscoDlswDirNBCacheMisses = _CiscoDlswDirNBCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 1, 6),
    _CiscoDlswDirNBCacheMisses_Type()
)
ciscoDlswDirNBCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirNBCacheMisses.setStatus("current")
_CiscoDlswDirCache_ObjectIdentity = ObjectIdentity
ciscoDlswDirCache = _CiscoDlswDirCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2)
)
_CiscoDlswDirMacTable_Object = MibTable
ciscoDlswDirMacTable = _CiscoDlswDirMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoDlswDirMacTable.setStatus("current")
_CiscoDlswDirMacEntry_Object = MibTableRow
ciscoDlswDirMacEntry = _CiscoDlswDirMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 1, 1)
)
ciscoDlswDirMacEntry.setIndexNames(
    (0, "CISCO-DLSW-MIB", "ciscoDlswDirMacIndex"),
)
if mibBuilder.loadTexts:
    ciscoDlswDirMacEntry.setStatus("current")


class _CiscoDlswDirMacIndex_Type(Integer32):
    """Custom type ciscoDlswDirMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_CiscoDlswDirMacIndex_Type.__name__ = "Integer32"
_CiscoDlswDirMacIndex_Object = MibTableColumn
ciscoDlswDirMacIndex = _CiscoDlswDirMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 1, 1, 1),
    _CiscoDlswDirMacIndex_Type()
)
ciscoDlswDirMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswDirMacIndex.setStatus("current")
_CiscoDlswDirMacMac_Type = MacAddress
_CiscoDlswDirMacMac_Object = MibTableColumn
ciscoDlswDirMacMac = _CiscoDlswDirMacMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 1, 1, 2),
    _CiscoDlswDirMacMac_Type()
)
ciscoDlswDirMacMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirMacMac.setStatus("current")


class _CiscoDlswDirMacMask_Type(MacAddress):
    """Custom type ciscoDlswDirMacMask based on MacAddress"""
    defaultHexValue = "ffffffffffff"


_CiscoDlswDirMacMask_Object = MibTableColumn
ciscoDlswDirMacMask = _CiscoDlswDirMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 1, 1, 3),
    _CiscoDlswDirMacMask_Type()
)
ciscoDlswDirMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirMacMask.setStatus("current")


class _CiscoDlswDirMacEntryType_Type(Integer32):
    """Custom type ciscoDlswDirMacEntryType based on Integer32"""
    defaultValue = 2

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
        *(("dynamic", 5),
          ("other", 1),
          ("partnerCapExMsg", 4),
          ("userConfiguredPrivate", 3),
          ("userConfiguredPublic", 2))
    )


_CiscoDlswDirMacEntryType_Type.__name__ = "Integer32"
_CiscoDlswDirMacEntryType_Object = MibTableColumn
ciscoDlswDirMacEntryType = _CiscoDlswDirMacEntryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 1, 1, 4),
    _CiscoDlswDirMacEntryType_Type()
)
ciscoDlswDirMacEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirMacEntryType.setStatus("current")


class _CiscoDlswDirMacLocationType_Type(Integer32):
    """Custom type ciscoDlswDirMacLocationType based on Integer32"""
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
        *(("local", 2),
          ("other", 1),
          ("remote", 3))
    )


_CiscoDlswDirMacLocationType_Type.__name__ = "Integer32"
_CiscoDlswDirMacLocationType_Object = MibTableColumn
ciscoDlswDirMacLocationType = _CiscoDlswDirMacLocationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 1, 1, 5),
    _CiscoDlswDirMacLocationType_Type()
)
ciscoDlswDirMacLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirMacLocationType.setStatus("current")
_CiscoDlswDirMacLocation_Type = InstancePointer
_CiscoDlswDirMacLocation_Object = MibTableColumn
ciscoDlswDirMacLocation = _CiscoDlswDirMacLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 1, 1, 6),
    _CiscoDlswDirMacLocation_Type()
)
ciscoDlswDirMacLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirMacLocation.setStatus("current")


class _CiscoDlswDirMacStatus_Type(Integer32):
    """Custom type ciscoDlswDirMacStatus based on Integer32"""
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
        *(("notReachable", 3),
          ("reachable", 2),
          ("unknown", 1))
    )


_CiscoDlswDirMacStatus_Type.__name__ = "Integer32"
_CiscoDlswDirMacStatus_Object = MibTableColumn
ciscoDlswDirMacStatus = _CiscoDlswDirMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 1, 1, 7),
    _CiscoDlswDirMacStatus_Type()
)
ciscoDlswDirMacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirMacStatus.setStatus("current")


class _CiscoDlswDirMacLFSize_Type(LFSize):
    """Custom type ciscoDlswDirMacLFSize based on LFSize"""


_CiscoDlswDirMacLFSize_Object = MibTableColumn
ciscoDlswDirMacLFSize = _CiscoDlswDirMacLFSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 1, 1, 8),
    _CiscoDlswDirMacLFSize_Type()
)
ciscoDlswDirMacLFSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirMacLFSize.setStatus("current")
_CiscoDlswDirMacRowStatus_Type = RowStatus
_CiscoDlswDirMacRowStatus_Object = MibTableColumn
ciscoDlswDirMacRowStatus = _CiscoDlswDirMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 1, 1, 9),
    _CiscoDlswDirMacRowStatus_Type()
)
ciscoDlswDirMacRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirMacRowStatus.setStatus("current")
_CiscoDlswDirNBTable_Object = MibTable
ciscoDlswDirNBTable = _CiscoDlswDirNBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoDlswDirNBTable.setStatus("current")
_CiscoDlswDirNBEntry_Object = MibTableRow
ciscoDlswDirNBEntry = _CiscoDlswDirNBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 2, 1)
)
ciscoDlswDirNBEntry.setIndexNames(
    (0, "CISCO-DLSW-MIB", "ciscoDlswDirNBIndex"),
)
if mibBuilder.loadTexts:
    ciscoDlswDirNBEntry.setStatus("current")


class _CiscoDlswDirNBIndex_Type(Integer32):
    """Custom type ciscoDlswDirNBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_CiscoDlswDirNBIndex_Type.__name__ = "Integer32"
_CiscoDlswDirNBIndex_Object = MibTableColumn
ciscoDlswDirNBIndex = _CiscoDlswDirNBIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 2, 1, 1),
    _CiscoDlswDirNBIndex_Type()
)
ciscoDlswDirNBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswDirNBIndex.setStatus("current")
_CiscoDlswDirNBName_Type = NBName
_CiscoDlswDirNBName_Object = MibTableColumn
ciscoDlswDirNBName = _CiscoDlswDirNBName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 2, 1, 2),
    _CiscoDlswDirNBName_Type()
)
ciscoDlswDirNBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirNBName.setStatus("current")


class _CiscoDlswDirNBNameType_Type(Integer32):
    """Custom type ciscoDlswDirNBNameType based on Integer32"""
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
        *(("group", 3),
          ("individual", 2),
          ("unknown", 1))
    )


_CiscoDlswDirNBNameType_Type.__name__ = "Integer32"
_CiscoDlswDirNBNameType_Object = MibTableColumn
ciscoDlswDirNBNameType = _CiscoDlswDirNBNameType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 2, 1, 3),
    _CiscoDlswDirNBNameType_Type()
)
ciscoDlswDirNBNameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirNBNameType.setStatus("current")


class _CiscoDlswDirNBEntryType_Type(Integer32):
    """Custom type ciscoDlswDirNBEntryType based on Integer32"""
    defaultValue = 2

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
        *(("dynamic", 5),
          ("other", 1),
          ("partnerCapExMsg", 4),
          ("userConfiguredPrivate", 3),
          ("userConfiguredPublic", 2))
    )


_CiscoDlswDirNBEntryType_Type.__name__ = "Integer32"
_CiscoDlswDirNBEntryType_Object = MibTableColumn
ciscoDlswDirNBEntryType = _CiscoDlswDirNBEntryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 2, 1, 4),
    _CiscoDlswDirNBEntryType_Type()
)
ciscoDlswDirNBEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirNBEntryType.setStatus("current")


class _CiscoDlswDirNBLocationType_Type(Integer32):
    """Custom type ciscoDlswDirNBLocationType based on Integer32"""
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
        *(("local", 2),
          ("other", 1),
          ("remote", 3))
    )


_CiscoDlswDirNBLocationType_Type.__name__ = "Integer32"
_CiscoDlswDirNBLocationType_Object = MibTableColumn
ciscoDlswDirNBLocationType = _CiscoDlswDirNBLocationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 2, 1, 5),
    _CiscoDlswDirNBLocationType_Type()
)
ciscoDlswDirNBLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirNBLocationType.setStatus("current")
_CiscoDlswDirNBLocation_Type = InstancePointer
_CiscoDlswDirNBLocation_Object = MibTableColumn
ciscoDlswDirNBLocation = _CiscoDlswDirNBLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 2, 1, 6),
    _CiscoDlswDirNBLocation_Type()
)
ciscoDlswDirNBLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirNBLocation.setStatus("current")


class _CiscoDlswDirNBStatus_Type(Integer32):
    """Custom type ciscoDlswDirNBStatus based on Integer32"""
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
        *(("notReachable", 3),
          ("reachable", 2),
          ("unknown", 1))
    )


_CiscoDlswDirNBStatus_Type.__name__ = "Integer32"
_CiscoDlswDirNBStatus_Object = MibTableColumn
ciscoDlswDirNBStatus = _CiscoDlswDirNBStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 2, 1, 7),
    _CiscoDlswDirNBStatus_Type()
)
ciscoDlswDirNBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirNBStatus.setStatus("current")


class _CiscoDlswDirNBLFSize_Type(LFSize):
    """Custom type ciscoDlswDirNBLFSize based on LFSize"""


_CiscoDlswDirNBLFSize_Object = MibTableColumn
ciscoDlswDirNBLFSize = _CiscoDlswDirNBLFSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 2, 1, 8),
    _CiscoDlswDirNBLFSize_Type()
)
ciscoDlswDirNBLFSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirNBLFSize.setStatus("current")
_CiscoDlswDirNBRowStatus_Type = RowStatus
_CiscoDlswDirNBRowStatus_Object = MibTableColumn
ciscoDlswDirNBRowStatus = _CiscoDlswDirNBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 2, 2, 1, 9),
    _CiscoDlswDirNBRowStatus_Type()
)
ciscoDlswDirNBRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirNBRowStatus.setStatus("current")
_CiscoDlswDirLocate_ObjectIdentity = ObjectIdentity
ciscoDlswDirLocate = _CiscoDlswDirLocate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 3)
)
_CiscoDlswDirLocateMacTable_Object = MibTable
ciscoDlswDirLocateMacTable = _CiscoDlswDirLocateMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoDlswDirLocateMacTable.setStatus("current")
_CiscoDlswDirLocateMacEntry_Object = MibTableRow
ciscoDlswDirLocateMacEntry = _CiscoDlswDirLocateMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 3, 1, 1)
)
ciscoDlswDirLocateMacEntry.setIndexNames(
    (0, "CISCO-DLSW-MIB", "ciscoDlswDirLocateMacMac"),
    (0, "CISCO-DLSW-MIB", "ciscoDlswDirLocateMacMatch"),
)
if mibBuilder.loadTexts:
    ciscoDlswDirLocateMacEntry.setStatus("current")
_CiscoDlswDirLocateMacMac_Type = MacAddress
_CiscoDlswDirLocateMacMac_Object = MibTableColumn
ciscoDlswDirLocateMacMac = _CiscoDlswDirLocateMacMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 3, 1, 1, 1),
    _CiscoDlswDirLocateMacMac_Type()
)
ciscoDlswDirLocateMacMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswDirLocateMacMac.setStatus("current")


class _CiscoDlswDirLocateMacMatch_Type(Integer32):
    """Custom type ciscoDlswDirLocateMacMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoDlswDirLocateMacMatch_Type.__name__ = "Integer32"
_CiscoDlswDirLocateMacMatch_Object = MibTableColumn
ciscoDlswDirLocateMacMatch = _CiscoDlswDirLocateMacMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 3, 1, 1, 2),
    _CiscoDlswDirLocateMacMatch_Type()
)
ciscoDlswDirLocateMacMatch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswDirLocateMacMatch.setStatus("current")
_CiscoDlswDirLocateMacLocation_Type = InstancePointer
_CiscoDlswDirLocateMacLocation_Object = MibTableColumn
ciscoDlswDirLocateMacLocation = _CiscoDlswDirLocateMacLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 3, 1, 1, 3),
    _CiscoDlswDirLocateMacLocation_Type()
)
ciscoDlswDirLocateMacLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirLocateMacLocation.setStatus("current")
_CiscoDlswDirLocateNBTable_Object = MibTable
ciscoDlswDirLocateNBTable = _CiscoDlswDirLocateNBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    ciscoDlswDirLocateNBTable.setStatus("current")
_CiscoDlswDirLocateNBEntry_Object = MibTableRow
ciscoDlswDirLocateNBEntry = _CiscoDlswDirLocateNBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 3, 2, 1)
)
ciscoDlswDirLocateNBEntry.setIndexNames(
    (0, "CISCO-DLSW-MIB", "ciscoDlswDirLocateNBName"),
    (0, "CISCO-DLSW-MIB", "ciscoDlswDirLocateNBMatch"),
)
if mibBuilder.loadTexts:
    ciscoDlswDirLocateNBEntry.setStatus("current")
_CiscoDlswDirLocateNBName_Type = NBName
_CiscoDlswDirLocateNBName_Object = MibTableColumn
ciscoDlswDirLocateNBName = _CiscoDlswDirLocateNBName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 3, 2, 1, 1),
    _CiscoDlswDirLocateNBName_Type()
)
ciscoDlswDirLocateNBName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswDirLocateNBName.setStatus("current")


class _CiscoDlswDirLocateNBMatch_Type(Integer32):
    """Custom type ciscoDlswDirLocateNBMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoDlswDirLocateNBMatch_Type.__name__ = "Integer32"
_CiscoDlswDirLocateNBMatch_Object = MibTableColumn
ciscoDlswDirLocateNBMatch = _CiscoDlswDirLocateNBMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 3, 2, 1, 2),
    _CiscoDlswDirLocateNBMatch_Type()
)
ciscoDlswDirLocateNBMatch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswDirLocateNBMatch.setStatus("current")
_CiscoDlswDirLocateNBLocation_Type = InstancePointer
_CiscoDlswDirLocateNBLocation_Object = MibTableColumn
ciscoDlswDirLocateNBLocation = _CiscoDlswDirLocateNBLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 4, 3, 2, 1, 3),
    _CiscoDlswDirLocateNBLocation_Type()
)
ciscoDlswDirLocateNBLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswDirLocateNBLocation.setStatus("current")
_CiscoDlswCircuit_ObjectIdentity = ObjectIdentity
ciscoDlswCircuit = _CiscoDlswCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5)
)
_CiscoDlswCircuitStat_ObjectIdentity = ObjectIdentity
ciscoDlswCircuitStat = _CiscoDlswCircuitStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 1)
)
_CiscoDlswActiveCircuits_Type = Gauge32
_CiscoDlswActiveCircuits_Object = MibScalar
ciscoDlswActiveCircuits = _CiscoDlswActiveCircuits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 1, 1),
    _CiscoDlswActiveCircuits_Type()
)
ciscoDlswActiveCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswActiveCircuits.setStatus("current")
_CiscoDlswCircuitCreates_Type = Counter32
_CiscoDlswCircuitCreates_Object = MibScalar
ciscoDlswCircuitCreates = _CiscoDlswCircuitCreates_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 1, 2),
    _CiscoDlswCircuitCreates_Type()
)
ciscoDlswCircuitCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitCreates.setStatus("current")
_CiscoDlswCircuitTable_Object = MibTable
ciscoDlswCircuitTable = _CiscoDlswCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ciscoDlswCircuitTable.setStatus("current")
_CiscoDlswCircuitEntry_Object = MibTableRow
ciscoDlswCircuitEntry = _CiscoDlswCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1)
)
ciscoDlswCircuitEntry.setIndexNames(
    (0, "CISCO-DLSW-MIB", "ciscoDlswCircuitS1Mac"),
    (0, "CISCO-DLSW-MIB", "ciscoDlswCircuitS1Sap"),
    (0, "CISCO-DLSW-MIB", "ciscoDlswCircuitS2Mac"),
    (0, "CISCO-DLSW-MIB", "ciscoDlswCircuitS2Sap"),
)
if mibBuilder.loadTexts:
    ciscoDlswCircuitEntry.setStatus("current")
_CiscoDlswCircuitS1Mac_Type = MacAddress
_CiscoDlswCircuitS1Mac_Object = MibTableColumn
ciscoDlswCircuitS1Mac = _CiscoDlswCircuitS1Mac_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 1),
    _CiscoDlswCircuitS1Mac_Type()
)
ciscoDlswCircuitS1Mac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS1Mac.setStatus("current")


class _CiscoDlswCircuitS1Sap_Type(OctetString):
    """Custom type ciscoDlswCircuitS1Sap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CiscoDlswCircuitS1Sap_Type.__name__ = "OctetString"
_CiscoDlswCircuitS1Sap_Object = MibTableColumn
ciscoDlswCircuitS1Sap = _CiscoDlswCircuitS1Sap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 2),
    _CiscoDlswCircuitS1Sap_Type()
)
ciscoDlswCircuitS1Sap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS1Sap.setStatus("current")


class _CiscoDlswCircuitS1IfIndex_Type(Integer32):
    """Custom type ciscoDlswCircuitS1IfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_CiscoDlswCircuitS1IfIndex_Type.__name__ = "Integer32"
_CiscoDlswCircuitS1IfIndex_Object = MibTableColumn
ciscoDlswCircuitS1IfIndex = _CiscoDlswCircuitS1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 3),
    _CiscoDlswCircuitS1IfIndex_Type()
)
ciscoDlswCircuitS1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS1IfIndex.setStatus("current")
_CiscoDlswCircuitS1DlcType_Type = DlcType
_CiscoDlswCircuitS1DlcType_Object = MibTableColumn
ciscoDlswCircuitS1DlcType = _CiscoDlswCircuitS1DlcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 4),
    _CiscoDlswCircuitS1DlcType_Type()
)
ciscoDlswCircuitS1DlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS1DlcType.setStatus("current")


class _CiscoDlswCircuitS1RouteInfo_Type(OctetString):
    """Custom type ciscoDlswCircuitS1RouteInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CiscoDlswCircuitS1RouteInfo_Type.__name__ = "OctetString"
_CiscoDlswCircuitS1RouteInfo_Object = MibTableColumn
ciscoDlswCircuitS1RouteInfo = _CiscoDlswCircuitS1RouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 5),
    _CiscoDlswCircuitS1RouteInfo_Type()
)
ciscoDlswCircuitS1RouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS1RouteInfo.setStatus("current")


class _CiscoDlswCircuitS1CircuitId_Type(OctetString):
    """Custom type ciscoDlswCircuitS1CircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_CiscoDlswCircuitS1CircuitId_Type.__name__ = "OctetString"
_CiscoDlswCircuitS1CircuitId_Object = MibTableColumn
ciscoDlswCircuitS1CircuitId = _CiscoDlswCircuitS1CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 6),
    _CiscoDlswCircuitS1CircuitId_Type()
)
ciscoDlswCircuitS1CircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS1CircuitId.setStatus("current")
_CiscoDlswCircuitS1Dlc_Type = InstancePointer
_CiscoDlswCircuitS1Dlc_Object = MibTableColumn
ciscoDlswCircuitS1Dlc = _CiscoDlswCircuitS1Dlc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 7),
    _CiscoDlswCircuitS1Dlc_Type()
)
ciscoDlswCircuitS1Dlc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS1Dlc.setStatus("current")
_CiscoDlswCircuitS2Mac_Type = MacAddress
_CiscoDlswCircuitS2Mac_Object = MibTableColumn
ciscoDlswCircuitS2Mac = _CiscoDlswCircuitS2Mac_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 8),
    _CiscoDlswCircuitS2Mac_Type()
)
ciscoDlswCircuitS2Mac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS2Mac.setStatus("current")


class _CiscoDlswCircuitS2Sap_Type(OctetString):
    """Custom type ciscoDlswCircuitS2Sap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CiscoDlswCircuitS2Sap_Type.__name__ = "OctetString"
_CiscoDlswCircuitS2Sap_Object = MibTableColumn
ciscoDlswCircuitS2Sap = _CiscoDlswCircuitS2Sap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 9),
    _CiscoDlswCircuitS2Sap_Type()
)
ciscoDlswCircuitS2Sap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS2Sap.setStatus("current")
_CiscoDlswCircuitS2Location_Type = EndStationLocation
_CiscoDlswCircuitS2Location_Object = MibTableColumn
ciscoDlswCircuitS2Location = _CiscoDlswCircuitS2Location_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 10),
    _CiscoDlswCircuitS2Location_Type()
)
ciscoDlswCircuitS2Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS2Location.setStatus("current")
_CiscoDlswCircuitS2TDomain_Type = ObjectIdentifier
_CiscoDlswCircuitS2TDomain_Object = MibTableColumn
ciscoDlswCircuitS2TDomain = _CiscoDlswCircuitS2TDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 11),
    _CiscoDlswCircuitS2TDomain_Type()
)
ciscoDlswCircuitS2TDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS2TDomain.setStatus("current")
_CiscoDlswCircuitS2TAddress_Type = TAddress
_CiscoDlswCircuitS2TAddress_Object = MibTableColumn
ciscoDlswCircuitS2TAddress = _CiscoDlswCircuitS2TAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 12),
    _CiscoDlswCircuitS2TAddress_Type()
)
ciscoDlswCircuitS2TAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS2TAddress.setStatus("current")


class _CiscoDlswCircuitS2CircuitId_Type(OctetString):
    """Custom type ciscoDlswCircuitS2CircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_CiscoDlswCircuitS2CircuitId_Type.__name__ = "OctetString"
_CiscoDlswCircuitS2CircuitId_Object = MibTableColumn
ciscoDlswCircuitS2CircuitId = _CiscoDlswCircuitS2CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 13),
    _CiscoDlswCircuitS2CircuitId_Type()
)
ciscoDlswCircuitS2CircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitS2CircuitId.setStatus("current")


class _CiscoDlswCircuitOrigin_Type(Integer32):
    """Custom type ciscoDlswCircuitOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 2))
    )


_CiscoDlswCircuitOrigin_Type.__name__ = "Integer32"
_CiscoDlswCircuitOrigin_Object = MibTableColumn
ciscoDlswCircuitOrigin = _CiscoDlswCircuitOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 14),
    _CiscoDlswCircuitOrigin_Type()
)
ciscoDlswCircuitOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitOrigin.setStatus("current")
_CiscoDlswCircuitEntryTime_Type = DlswTimeStamp
_CiscoDlswCircuitEntryTime_Object = MibTableColumn
ciscoDlswCircuitEntryTime = _CiscoDlswCircuitEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 15),
    _CiscoDlswCircuitEntryTime_Type()
)
ciscoDlswCircuitEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitEntryTime.setStatus("current")
_CiscoDlswCircuitStateTime_Type = DlswTimeStamp
_CiscoDlswCircuitStateTime_Object = MibTableColumn
ciscoDlswCircuitStateTime = _CiscoDlswCircuitStateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 16),
    _CiscoDlswCircuitStateTime_Type()
)
ciscoDlswCircuitStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitStateTime.setStatus("current")


class _CiscoDlswCircuitState_Type(Integer32):
    """Custom type ciscoDlswCircuitState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("circuitEstablished", 5),
          ("circuitPending", 4),
          ("circuitRestart", 12),
          ("circuitStart", 2),
          ("connectPending", 6),
          ("connected", 8),
          ("contactPending", 7),
          ("disconnectPending", 9),
          ("disconnected", 1),
          ("haltPending", 10),
          ("haltPendingNoack", 11),
          ("resolvePending", 3),
          ("restartPending", 13))
    )


_CiscoDlswCircuitState_Type.__name__ = "Integer32"
_CiscoDlswCircuitState_Object = MibTableColumn
ciscoDlswCircuitState = _CiscoDlswCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 17),
    _CiscoDlswCircuitState_Type()
)
ciscoDlswCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitState.setStatus("current")


class _CiscoDlswCircuitPriority_Type(Integer32):
    """Custom type ciscoDlswCircuitPriority based on Integer32"""
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
        *(("high", 3),
          ("highest", 4),
          ("low", 1),
          ("medium", 2),
          ("unsupported", 0))
    )


_CiscoDlswCircuitPriority_Type.__name__ = "Integer32"
_CiscoDlswCircuitPriority_Object = MibTableColumn
ciscoDlswCircuitPriority = _CiscoDlswCircuitPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 18),
    _CiscoDlswCircuitPriority_Type()
)
ciscoDlswCircuitPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitPriority.setStatus("current")


class _CiscoDlswCircuitFCSendGrantedUnits_Type(Integer32):
    """Custom type ciscoDlswCircuitFCSendGrantedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoDlswCircuitFCSendGrantedUnits_Type.__name__ = "Integer32"
_CiscoDlswCircuitFCSendGrantedUnits_Object = MibTableColumn
ciscoDlswCircuitFCSendGrantedUnits = _CiscoDlswCircuitFCSendGrantedUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 19),
    _CiscoDlswCircuitFCSendGrantedUnits_Type()
)
ciscoDlswCircuitFCSendGrantedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitFCSendGrantedUnits.setStatus("current")


class _CiscoDlswCircuitFCSendCurrentWndw_Type(Integer32):
    """Custom type ciscoDlswCircuitFCSendCurrentWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoDlswCircuitFCSendCurrentWndw_Type.__name__ = "Integer32"
_CiscoDlswCircuitFCSendCurrentWndw_Object = MibTableColumn
ciscoDlswCircuitFCSendCurrentWndw = _CiscoDlswCircuitFCSendCurrentWndw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 20),
    _CiscoDlswCircuitFCSendCurrentWndw_Type()
)
ciscoDlswCircuitFCSendCurrentWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitFCSendCurrentWndw.setStatus("current")


class _CiscoDlswCircuitFCRecvGrantedUnits_Type(Integer32):
    """Custom type ciscoDlswCircuitFCRecvGrantedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoDlswCircuitFCRecvGrantedUnits_Type.__name__ = "Integer32"
_CiscoDlswCircuitFCRecvGrantedUnits_Object = MibTableColumn
ciscoDlswCircuitFCRecvGrantedUnits = _CiscoDlswCircuitFCRecvGrantedUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 21),
    _CiscoDlswCircuitFCRecvGrantedUnits_Type()
)
ciscoDlswCircuitFCRecvGrantedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitFCRecvGrantedUnits.setStatus("current")


class _CiscoDlswCircuitFCRecvCurrentWndw_Type(Integer32):
    """Custom type ciscoDlswCircuitFCRecvCurrentWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoDlswCircuitFCRecvCurrentWndw_Type.__name__ = "Integer32"
_CiscoDlswCircuitFCRecvCurrentWndw_Object = MibTableColumn
ciscoDlswCircuitFCRecvCurrentWndw = _CiscoDlswCircuitFCRecvCurrentWndw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 22),
    _CiscoDlswCircuitFCRecvCurrentWndw_Type()
)
ciscoDlswCircuitFCRecvCurrentWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitFCRecvCurrentWndw.setStatus("current")
_CiscoDlswCircuitFCLargestRecvGranted_Type = Gauge32
_CiscoDlswCircuitFCLargestRecvGranted_Object = MibTableColumn
ciscoDlswCircuitFCLargestRecvGranted = _CiscoDlswCircuitFCLargestRecvGranted_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 23),
    _CiscoDlswCircuitFCLargestRecvGranted_Type()
)
ciscoDlswCircuitFCLargestRecvGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitFCLargestRecvGranted.setStatus("current")
_CiscoDlswCircuitFCLargestSendGranted_Type = Gauge32
_CiscoDlswCircuitFCLargestSendGranted_Object = MibTableColumn
ciscoDlswCircuitFCLargestSendGranted = _CiscoDlswCircuitFCLargestSendGranted_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 24),
    _CiscoDlswCircuitFCLargestSendGranted_Type()
)
ciscoDlswCircuitFCLargestSendGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitFCLargestSendGranted.setStatus("current")
_CiscoDlswCircuitFCHalveWndwSents_Type = Counter32
_CiscoDlswCircuitFCHalveWndwSents_Object = MibTableColumn
ciscoDlswCircuitFCHalveWndwSents = _CiscoDlswCircuitFCHalveWndwSents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 25),
    _CiscoDlswCircuitFCHalveWndwSents_Type()
)
ciscoDlswCircuitFCHalveWndwSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitFCHalveWndwSents.setStatus("current")
_CiscoDlswCircuitFCResetOpSents_Type = Counter32
_CiscoDlswCircuitFCResetOpSents_Object = MibTableColumn
ciscoDlswCircuitFCResetOpSents = _CiscoDlswCircuitFCResetOpSents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 26),
    _CiscoDlswCircuitFCResetOpSents_Type()
)
ciscoDlswCircuitFCResetOpSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitFCResetOpSents.setStatus("current")
_CiscoDlswCircuitFCHalveWndwRcvds_Type = Counter32
_CiscoDlswCircuitFCHalveWndwRcvds_Object = MibTableColumn
ciscoDlswCircuitFCHalveWndwRcvds = _CiscoDlswCircuitFCHalveWndwRcvds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 27),
    _CiscoDlswCircuitFCHalveWndwRcvds_Type()
)
ciscoDlswCircuitFCHalveWndwRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitFCHalveWndwRcvds.setStatus("current")
_CiscoDlswCircuitFCResetOpRcvds_Type = Counter32
_CiscoDlswCircuitFCResetOpRcvds_Object = MibTableColumn
ciscoDlswCircuitFCResetOpRcvds = _CiscoDlswCircuitFCResetOpRcvds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 28),
    _CiscoDlswCircuitFCResetOpRcvds_Type()
)
ciscoDlswCircuitFCResetOpRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitFCResetOpRcvds.setStatus("current")


class _CiscoDlswCircuitDiscReasonLocal_Type(Integer32):
    """Custom type ciscoDlswCircuitDiscReasonLocal based on Integer32"""
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
        *(("endStationDiscRcvd", 1),
          ("endStationDlcError", 2),
          ("haltDlNoAckRcvd", 6),
          ("haltDlRcvd", 5),
          ("operatorCommand", 4),
          ("protocolError", 3),
          ("transportConnClosed", 7))
    )


_CiscoDlswCircuitDiscReasonLocal_Type.__name__ = "Integer32"
_CiscoDlswCircuitDiscReasonLocal_Object = MibTableColumn
ciscoDlswCircuitDiscReasonLocal = _CiscoDlswCircuitDiscReasonLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 29),
    _CiscoDlswCircuitDiscReasonLocal_Type()
)
ciscoDlswCircuitDiscReasonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitDiscReasonLocal.setStatus("current")


class _CiscoDlswCircuitDiscReasonRemote_Type(Integer32):
    """Custom type ciscoDlswCircuitDiscReasonRemote based on Integer32"""
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
        *(("endStationDiscRcvd", 1),
          ("endStationDlcError", 2),
          ("operatorCommand", 4),
          ("protocolError", 3),
          ("unknown", 0))
    )


_CiscoDlswCircuitDiscReasonRemote_Type.__name__ = "Integer32"
_CiscoDlswCircuitDiscReasonRemote_Object = MibTableColumn
ciscoDlswCircuitDiscReasonRemote = _CiscoDlswCircuitDiscReasonRemote_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 30),
    _CiscoDlswCircuitDiscReasonRemote_Type()
)
ciscoDlswCircuitDiscReasonRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitDiscReasonRemote.setStatus("current")


class _CiscoDlswCircuitDiscReasonRemoteData_Type(OctetString):
    """Custom type ciscoDlswCircuitDiscReasonRemoteData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_CiscoDlswCircuitDiscReasonRemoteData_Type.__name__ = "OctetString"
_CiscoDlswCircuitDiscReasonRemoteData_Object = MibTableColumn
ciscoDlswCircuitDiscReasonRemoteData = _CiscoDlswCircuitDiscReasonRemoteData_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 5, 2, 1, 31),
    _CiscoDlswCircuitDiscReasonRemoteData_Type()
)
ciscoDlswCircuitDiscReasonRemoteData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswCircuitDiscReasonRemoteData.setStatus("current")
_CiscoDlswSdlc_ObjectIdentity = ObjectIdentity
ciscoDlswSdlc = _CiscoDlswSdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 6)
)
_CiscoDlswSdlcLsEntries_Type = Gauge32
_CiscoDlswSdlcLsEntries_Object = MibScalar
ciscoDlswSdlcLsEntries = _CiscoDlswSdlcLsEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 6, 1),
    _CiscoDlswSdlcLsEntries_Type()
)
ciscoDlswSdlcLsEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswSdlcLsEntries.setStatus("current")
_CiscoDlswSdlcLsTable_Object = MibTable
ciscoDlswSdlcLsTable = _CiscoDlswSdlcLsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ciscoDlswSdlcLsTable.setStatus("current")
_CiscoDlswSdlcLsEntry_Object = MibTableRow
ciscoDlswSdlcLsEntry = _CiscoDlswSdlcLsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 6, 2, 1)
)
ciscoDlswSdlcLsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SNA-SDLC-MIB", "sdlcLSAddress"),
)
if mibBuilder.loadTexts:
    ciscoDlswSdlcLsEntry.setStatus("current")
_CiscoDlswSdlcLsLocalMac_Type = MacAddress
_CiscoDlswSdlcLsLocalMac_Object = MibTableColumn
ciscoDlswSdlcLsLocalMac = _CiscoDlswSdlcLsLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 6, 2, 1, 1),
    _CiscoDlswSdlcLsLocalMac_Type()
)
ciscoDlswSdlcLsLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswSdlcLsLocalMac.setStatus("current")


class _CiscoDlswSdlcLsLocalSap_Type(OctetString):
    """Custom type ciscoDlswSdlcLsLocalSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CiscoDlswSdlcLsLocalSap_Type.__name__ = "OctetString"
_CiscoDlswSdlcLsLocalSap_Object = MibTableColumn
ciscoDlswSdlcLsLocalSap = _CiscoDlswSdlcLsLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 6, 2, 1, 2),
    _CiscoDlswSdlcLsLocalSap_Type()
)
ciscoDlswSdlcLsLocalSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswSdlcLsLocalSap.setStatus("current")


class _CiscoDlswSdlcLsLocalBlockNum_Type(DisplayString):
    """Custom type ciscoDlswSdlcLsLocalBlockNum based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 3),
    )


_CiscoDlswSdlcLsLocalBlockNum_Type.__name__ = "DisplayString"
_CiscoDlswSdlcLsLocalBlockNum_Object = MibTableColumn
ciscoDlswSdlcLsLocalBlockNum = _CiscoDlswSdlcLsLocalBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 6, 2, 1, 3),
    _CiscoDlswSdlcLsLocalBlockNum_Type()
)
ciscoDlswSdlcLsLocalBlockNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswSdlcLsLocalBlockNum.setStatus("current")


class _CiscoDlswSdlcLsLocalIdNum_Type(DisplayString):
    """Custom type ciscoDlswSdlcLsLocalIdNum based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
    )


_CiscoDlswSdlcLsLocalIdNum_Type.__name__ = "DisplayString"
_CiscoDlswSdlcLsLocalIdNum_Object = MibTableColumn
ciscoDlswSdlcLsLocalIdNum = _CiscoDlswSdlcLsLocalIdNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 6, 2, 1, 4),
    _CiscoDlswSdlcLsLocalIdNum_Type()
)
ciscoDlswSdlcLsLocalIdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswSdlcLsLocalIdNum.setStatus("current")


class _CiscoDlswSdlcLsRemoteMac_Type(MacAddress):
    """Custom type ciscoDlswSdlcLsRemoteMac based on MacAddress"""
    defaultHexValue = ""


_CiscoDlswSdlcLsRemoteMac_Object = MibTableColumn
ciscoDlswSdlcLsRemoteMac = _CiscoDlswSdlcLsRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 6, 2, 1, 5),
    _CiscoDlswSdlcLsRemoteMac_Type()
)
ciscoDlswSdlcLsRemoteMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswSdlcLsRemoteMac.setStatus("current")


class _CiscoDlswSdlcLsRemoteSap_Type(OctetString):
    """Custom type ciscoDlswSdlcLsRemoteSap based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
    )


_CiscoDlswSdlcLsRemoteSap_Type.__name__ = "OctetString"
_CiscoDlswSdlcLsRemoteSap_Object = MibTableColumn
ciscoDlswSdlcLsRemoteSap = _CiscoDlswSdlcLsRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 6, 2, 1, 6),
    _CiscoDlswSdlcLsRemoteSap_Type()
)
ciscoDlswSdlcLsRemoteSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswSdlcLsRemoteSap.setStatus("current")
_CiscoDlswSdlcLsRowStatus_Type = RowStatus
_CiscoDlswSdlcLsRowStatus_Object = MibTableColumn
ciscoDlswSdlcLsRowStatus = _CiscoDlswSdlcLsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 6, 2, 1, 7),
    _CiscoDlswSdlcLsRowStatus_Type()
)
ciscoDlswSdlcLsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoDlswSdlcLsRowStatus.setStatus("current")
_CiscoDlswTraps_ObjectIdentity = ObjectIdentity
ciscoDlswTraps = _CiscoDlswTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 7)
)
_CiscoDlswDomains_ObjectIdentity = ObjectIdentity
ciscoDlswDomains = _CiscoDlswDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 2)
)
_CiscoDlswTCPDomain_ObjectIdentity = ObjectIdentity
ciscoDlswTCPDomain = _CiscoDlswTCPDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 2, 1)
)
_CiscoDlswConformance_ObjectIdentity = ObjectIdentity
ciscoDlswConformance = _CiscoDlswConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3)
)
_CiscoDlswCompliances_ObjectIdentity = ObjectIdentity
ciscoDlswCompliances = _CiscoDlswCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 1)
)
_CiscoDlswGroups_ObjectIdentity = ObjectIdentity
ciscoDlswGroups = _CiscoDlswGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2)
)

# Managed Objects groups

ciscoDlswNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 1)
)
ciscoDlswNodeGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswVersion"),
        ("CISCO-DLSW-MIB", "ciscoDlswVendorID"),
        ("CISCO-DLSW-MIB", "ciscoDlswVersionString"),
        ("CISCO-DLSW-MIB", "ciscoDlswStdPacingSupport"),
        ("CISCO-DLSW-MIB", "ciscoDlswStatus"),
        ("CISCO-DLSW-MIB", "ciscoDlswUpTime"),
        ("CISCO-DLSW-MIB", "ciscoDlswVirtualSegmentLFSize"),
        ("CISCO-DLSW-MIB", "ciscoDlswResourceMacExclusivity"),
        ("CISCO-DLSW-MIB", "ciscoDlswTrapCntlTConnPartnerReject"),
        ("CISCO-DLSW-MIB", "ciscoDlswTrapCntlTConnProtViolation"),
        ("CISCO-DLSW-MIB", "ciscoDlswTrapCntlTConn"),
        ("CISCO-DLSW-MIB", "ciscoDlswTrapCntlCircuit"))
)
if mibBuilder.loadTexts:
    ciscoDlswNodeGroup.setStatus("current")

ciscoDlswNodeNBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 2)
)
ciscoDlswNodeNBGroup.setObjects(
    ("CISCO-DLSW-MIB", "ciscoDlswResourceNBExclusivity")
)
if mibBuilder.loadTexts:
    ciscoDlswNodeNBGroup.setStatus("current")

ciscoDlswTConnStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 3)
)
ciscoDlswTConnStatGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswTConnStatActiveConnections"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnStatCloseIdles"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnStatCloseBusys"))
)
if mibBuilder.loadTexts:
    ciscoDlswTConnStatGroup.setStatus("current")

ciscoDlswTConnConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 4)
)
ciscoDlswTConnConfigGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswTConnConfigTDomain"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnConfigLocalTAddr"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnConfigRemoteTAddr"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnConfigLastModifyTime"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnConfigEntryType"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnConfigGroupDefinition"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnConfigSetupType"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnConfigSapList"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnConfigAdvertiseMacNB"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnConfigInitCirRecvWndw"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnConfigOpens"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnConfigRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDlswTConnConfigGroup.setStatus("current")

ciscoDlswTConnOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 5)
)
ciscoDlswTConnOperGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswTConnOperLocalTAddr"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperEntryTime"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperConnectTime"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperState"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperConfigIndex"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperFlowCntlMode"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperPartnerVersion"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperPartnerVendorID"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperPartnerVersionStr"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperPartnerInitPacingWndw"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperPartnerSapList"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperPartnerMacExcl"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperPartnerMacInfo"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperDiscTime"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperDiscReason"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperDiscActiveCir"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperInDataPkts"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperOutDataPkts"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperInDataOctets"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperOutDataOctets"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperInCntlPkts"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperOutCntlPkts"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperCURexSents"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperICRexRcvds"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperCURexRcvds"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperICRexSents"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperCirCreates"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperCircuits"))
)
if mibBuilder.loadTexts:
    ciscoDlswTConnOperGroup.setStatus("current")

ciscoDlswTConnNBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 6)
)
ciscoDlswTConnNBGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswTConnOperPartnerNBInfo"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperPartnerNBExcl"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperNQexSents"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperNRexRcvds"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperNQexRcvds"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperNRexSents"))
)
if mibBuilder.loadTexts:
    ciscoDlswTConnNBGroup.setStatus("current")

ciscoDlswInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 7)
)
ciscoDlswInterfaceGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswIfRowStatus"),
        ("CISCO-DLSW-MIB", "ciscoDlswIfVirtualSegment"),
        ("CISCO-DLSW-MIB", "ciscoDlswIfSapList"))
)
if mibBuilder.loadTexts:
    ciscoDlswInterfaceGroup.setStatus("current")

ciscoDlswDirGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 8)
)
ciscoDlswDirGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswDirMacEntries"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirMacCacheHits"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirMacCacheMisses"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirMacMac"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirMacMask"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirMacEntryType"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirMacLocationType"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirMacLocation"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirMacStatus"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirMacLFSize"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirMacRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDlswDirGroup.setStatus("current")

ciscoDlswDirNBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 9)
)
ciscoDlswDirNBGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswDirNBEntries"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirNBCacheHits"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirNBCacheMisses"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirNBName"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirNBNameType"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirNBEntryType"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirNBLocationType"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirNBLocation"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirNBStatus"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirNBLFSize"),
        ("CISCO-DLSW-MIB", "ciscoDlswDirNBRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDlswDirNBGroup.setStatus("current")

ciscoDlswDirLocateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 10)
)
ciscoDlswDirLocateGroup.setObjects(
    ("CISCO-DLSW-MIB", "ciscoDlswDirLocateMacLocation")
)
if mibBuilder.loadTexts:
    ciscoDlswDirLocateGroup.setStatus("current")

ciscoDlswDirLocateNBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 11)
)
ciscoDlswDirLocateNBGroup.setObjects(
    ("CISCO-DLSW-MIB", "ciscoDlswDirLocateNBLocation")
)
if mibBuilder.loadTexts:
    ciscoDlswDirLocateNBGroup.setStatus("current")

ciscoDlswCircuitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 12)
)
ciscoDlswCircuitGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswCircuitS1IfIndex"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS1DlcType"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS1RouteInfo"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS1CircuitId"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS1Dlc"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS2Location"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS2TDomain"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS2TAddress"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS2CircuitId"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitOrigin"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitEntryTime"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitStateTime"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitState"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitPriority"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitFCSendGrantedUnits"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitFCSendCurrentWndw"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitFCRecvGrantedUnits"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitFCRecvCurrentWndw"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitFCLargestRecvGranted"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitFCLargestSendGranted"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitFCHalveWndwSents"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitFCResetOpSents"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitFCHalveWndwRcvds"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitFCResetOpRcvds"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitDiscReasonLocal"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitDiscReasonRemote"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitDiscReasonRemoteData"))
)
if mibBuilder.loadTexts:
    ciscoDlswCircuitGroup.setStatus("current")

ciscoDlswSdlcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 13)
)
ciscoDlswSdlcGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswSdlcLsEntries"),
        ("CISCO-DLSW-MIB", "ciscoDlswSdlcLsLocalMac"),
        ("CISCO-DLSW-MIB", "ciscoDlswSdlcLsLocalSap"),
        ("CISCO-DLSW-MIB", "ciscoDlswSdlcLsLocalBlockNum"),
        ("CISCO-DLSW-MIB", "ciscoDlswSdlcLsLocalIdNum"),
        ("CISCO-DLSW-MIB", "ciscoDlswSdlcLsRemoteMac"),
        ("CISCO-DLSW-MIB", "ciscoDlswSdlcLsRemoteSap"),
        ("CISCO-DLSW-MIB", "ciscoDlswSdlcLsRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDlswSdlcGroup.setStatus("current")

ciscoDlswTConnTcpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 15)
)
ciscoDlswTConnTcpConfigGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswTConnTcpConfigKeepAliveInt"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnTcpConfigTcpConnections"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnTcpConfigMaxSegmentSize"))
)
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpConfigGroup.setStatus("current")

ciscoDlswTConnTcpOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 16)
)
ciscoDlswTConnTcpOperGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswTConnTcpOperKeepAliveInt"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnTcpOperPrefTcpConnections"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnTcpOperTcpConnections"))
)
if mibBuilder.loadTexts:
    ciscoDlswTConnTcpOperGroup.setStatus("current")

ciscoDlswCircuitStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 2, 17)
)
ciscoDlswCircuitStatGroup.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswActiveCircuits"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitCreates"))
)
if mibBuilder.loadTexts:
    ciscoDlswCircuitStatGroup.setStatus("current")


# Notification objects

ciscoDlswTrapTConnPartnerReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 7, 1)
)
ciscoDlswTrapTConnPartnerReject.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswTConnOperTDomain"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperRemoteTAddr"))
)
if mibBuilder.loadTexts:
    ciscoDlswTrapTConnPartnerReject.setStatus(
        "current"
    )

ciscoDlswTrapTConnProtViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 7, 2)
)
ciscoDlswTrapTConnProtViolation.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswTConnOperTDomain"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperRemoteTAddr"))
)
if mibBuilder.loadTexts:
    ciscoDlswTrapTConnProtViolation.setStatus(
        "current"
    )

ciscoDlswTrapTConnUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 7, 3)
)
ciscoDlswTrapTConnUp.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswTConnOperTDomain"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperRemoteTAddr"))
)
if mibBuilder.loadTexts:
    ciscoDlswTrapTConnUp.setStatus(
        "current"
    )

ciscoDlswTrapTConnDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 7, 4)
)
ciscoDlswTrapTConnDown.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswTConnOperTDomain"),
        ("CISCO-DLSW-MIB", "ciscoDlswTConnOperRemoteTAddr"))
)
if mibBuilder.loadTexts:
    ciscoDlswTrapTConnDown.setStatus(
        "current"
    )

ciscoDlswTrapCircuitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 7, 5)
)
ciscoDlswTrapCircuitUp.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswCircuitS1Mac"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS1Sap"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS2Mac"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS2Sap"))
)
if mibBuilder.loadTexts:
    ciscoDlswTrapCircuitUp.setStatus(
        "current"
    )

ciscoDlswTrapCircuitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 1, 7, 6)
)
ciscoDlswTrapCircuitDown.setObjects(
      *(("CISCO-DLSW-MIB", "ciscoDlswCircuitS1Mac"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS1Sap"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS2Mac"),
        ("CISCO-DLSW-MIB", "ciscoDlswCircuitS2Sap"))
)
if mibBuilder.loadTexts:
    ciscoDlswTrapCircuitDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDlswCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDlswCoreCompliance.setStatus(
        "obsolete"
    )

ciscoDlswDirCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoDlswDirCompliance.setStatus(
        "obsolete"
    )

ciscoDlswDirLocateCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoDlswDirLocateCompliance.setStatus(
        "current"
    )

ciscoDlswSdlcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoDlswSdlcCompliance.setStatus(
        "obsolete"
    )

ciscoDlswCoreComplianceV11R01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoDlswCoreComplianceV11R01.setStatus(
        "current"
    )

ciscoDlswDirComplianceV11R01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoDlswDirComplianceV11R01.setStatus(
        "current"
    )

ciscoDlswSdlcComplianceV11R01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 9, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoDlswSdlcComplianceV11R01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DLSW-MIB",
    **{"NBName": NBName,
       "MacAddress": MacAddress,
       "TAddress": TAddress,
       "DlswTimeStamp": DlswTimeStamp,
       "EndStationLocation": EndStationLocation,
       "DlcType": DlcType,
       "LFSize": LFSize,
       "ciscoDlswMIB": ciscoDlswMIB,
       "ciscoDlswMIBObjects": ciscoDlswMIBObjects,
       "ciscoDlswNode": ciscoDlswNode,
       "ciscoDlswVersion": ciscoDlswVersion,
       "ciscoDlswVendorID": ciscoDlswVendorID,
       "ciscoDlswVersionString": ciscoDlswVersionString,
       "ciscoDlswStdPacingSupport": ciscoDlswStdPacingSupport,
       "ciscoDlswStatus": ciscoDlswStatus,
       "ciscoDlswUpTime": ciscoDlswUpTime,
       "ciscoDlswVirtualSegmentLFSize": ciscoDlswVirtualSegmentLFSize,
       "ciscoDlswResourceNBExclusivity": ciscoDlswResourceNBExclusivity,
       "ciscoDlswResourceMacExclusivity": ciscoDlswResourceMacExclusivity,
       "ciscoDlswTrapControl": ciscoDlswTrapControl,
       "ciscoDlswTrapCntlTConnPartnerReject": ciscoDlswTrapCntlTConnPartnerReject,
       "ciscoDlswTrapCntlTConnProtViolation": ciscoDlswTrapCntlTConnProtViolation,
       "ciscoDlswTrapCntlTConn": ciscoDlswTrapCntlTConn,
       "ciscoDlswTrapCntlCircuit": ciscoDlswTrapCntlCircuit,
       "ciscoDlswTConn": ciscoDlswTConn,
       "ciscoDlswTConnStat": ciscoDlswTConnStat,
       "ciscoDlswTConnStatActiveConnections": ciscoDlswTConnStatActiveConnections,
       "ciscoDlswTConnStatCloseIdles": ciscoDlswTConnStatCloseIdles,
       "ciscoDlswTConnStatCloseBusys": ciscoDlswTConnStatCloseBusys,
       "ciscoDlswTConnConfigTable": ciscoDlswTConnConfigTable,
       "ciscoDlswTConnConfigEntry": ciscoDlswTConnConfigEntry,
       "ciscoDlswTConnConfigIndex": ciscoDlswTConnConfigIndex,
       "ciscoDlswTConnConfigTDomain": ciscoDlswTConnConfigTDomain,
       "ciscoDlswTConnConfigLocalTAddr": ciscoDlswTConnConfigLocalTAddr,
       "ciscoDlswTConnConfigRemoteTAddr": ciscoDlswTConnConfigRemoteTAddr,
       "ciscoDlswTConnConfigLastModifyTime": ciscoDlswTConnConfigLastModifyTime,
       "ciscoDlswTConnConfigEntryType": ciscoDlswTConnConfigEntryType,
       "ciscoDlswTConnConfigGroupDefinition": ciscoDlswTConnConfigGroupDefinition,
       "ciscoDlswTConnConfigSetupType": ciscoDlswTConnConfigSetupType,
       "ciscoDlswTConnConfigSapList": ciscoDlswTConnConfigSapList,
       "ciscoDlswTConnConfigAdvertiseMacNB": ciscoDlswTConnConfigAdvertiseMacNB,
       "ciscoDlswTConnConfigInitCirRecvWndw": ciscoDlswTConnConfigInitCirRecvWndw,
       "ciscoDlswTConnConfigOpens": ciscoDlswTConnConfigOpens,
       "ciscoDlswTConnConfigRowStatus": ciscoDlswTConnConfigRowStatus,
       "ciscoDlswTConnOperTable": ciscoDlswTConnOperTable,
       "ciscoDlswTConnOperEntry": ciscoDlswTConnOperEntry,
       "ciscoDlswTConnOperTDomain": ciscoDlswTConnOperTDomain,
       "ciscoDlswTConnOperLocalTAddr": ciscoDlswTConnOperLocalTAddr,
       "ciscoDlswTConnOperRemoteTAddr": ciscoDlswTConnOperRemoteTAddr,
       "ciscoDlswTConnOperEntryTime": ciscoDlswTConnOperEntryTime,
       "ciscoDlswTConnOperConnectTime": ciscoDlswTConnOperConnectTime,
       "ciscoDlswTConnOperState": ciscoDlswTConnOperState,
       "ciscoDlswTConnOperConfigIndex": ciscoDlswTConnOperConfigIndex,
       "ciscoDlswTConnOperFlowCntlMode": ciscoDlswTConnOperFlowCntlMode,
       "ciscoDlswTConnOperPartnerVersion": ciscoDlswTConnOperPartnerVersion,
       "ciscoDlswTConnOperPartnerVendorID": ciscoDlswTConnOperPartnerVendorID,
       "ciscoDlswTConnOperPartnerVersionStr": ciscoDlswTConnOperPartnerVersionStr,
       "ciscoDlswTConnOperPartnerInitPacingWndw": ciscoDlswTConnOperPartnerInitPacingWndw,
       "ciscoDlswTConnOperPartnerSapList": ciscoDlswTConnOperPartnerSapList,
       "ciscoDlswTConnOperPartnerNBExcl": ciscoDlswTConnOperPartnerNBExcl,
       "ciscoDlswTConnOperPartnerMacExcl": ciscoDlswTConnOperPartnerMacExcl,
       "ciscoDlswTConnOperPartnerNBInfo": ciscoDlswTConnOperPartnerNBInfo,
       "ciscoDlswTConnOperPartnerMacInfo": ciscoDlswTConnOperPartnerMacInfo,
       "ciscoDlswTConnOperDiscTime": ciscoDlswTConnOperDiscTime,
       "ciscoDlswTConnOperDiscReason": ciscoDlswTConnOperDiscReason,
       "ciscoDlswTConnOperDiscActiveCir": ciscoDlswTConnOperDiscActiveCir,
       "ciscoDlswTConnOperInDataPkts": ciscoDlswTConnOperInDataPkts,
       "ciscoDlswTConnOperOutDataPkts": ciscoDlswTConnOperOutDataPkts,
       "ciscoDlswTConnOperInDataOctets": ciscoDlswTConnOperInDataOctets,
       "ciscoDlswTConnOperOutDataOctets": ciscoDlswTConnOperOutDataOctets,
       "ciscoDlswTConnOperInCntlPkts": ciscoDlswTConnOperInCntlPkts,
       "ciscoDlswTConnOperOutCntlPkts": ciscoDlswTConnOperOutCntlPkts,
       "ciscoDlswTConnOperCURexSents": ciscoDlswTConnOperCURexSents,
       "ciscoDlswTConnOperICRexRcvds": ciscoDlswTConnOperICRexRcvds,
       "ciscoDlswTConnOperCURexRcvds": ciscoDlswTConnOperCURexRcvds,
       "ciscoDlswTConnOperICRexSents": ciscoDlswTConnOperICRexSents,
       "ciscoDlswTConnOperNQexSents": ciscoDlswTConnOperNQexSents,
       "ciscoDlswTConnOperNRexRcvds": ciscoDlswTConnOperNRexRcvds,
       "ciscoDlswTConnOperNQexRcvds": ciscoDlswTConnOperNQexRcvds,
       "ciscoDlswTConnOperNRexSents": ciscoDlswTConnOperNRexSents,
       "ciscoDlswTConnOperCirCreates": ciscoDlswTConnOperCirCreates,
       "ciscoDlswTConnOperCircuits": ciscoDlswTConnOperCircuits,
       "ciscoDlswTConnSpecific": ciscoDlswTConnSpecific,
       "ciscoDlswTConnTcp": ciscoDlswTConnTcp,
       "ciscoDlswTConnTcpConfigTable": ciscoDlswTConnTcpConfigTable,
       "ciscoDlswTConnTcpConfigEntry": ciscoDlswTConnTcpConfigEntry,
       "ciscoDlswTConnTcpConfigKeepAliveInt": ciscoDlswTConnTcpConfigKeepAliveInt,
       "ciscoDlswTConnTcpConfigTcpConnections": ciscoDlswTConnTcpConfigTcpConnections,
       "ciscoDlswTConnTcpConfigMaxSegmentSize": ciscoDlswTConnTcpConfigMaxSegmentSize,
       "ciscoDlswTConnTcpOperTable": ciscoDlswTConnTcpOperTable,
       "ciscoDlswTConnTcpOperEntry": ciscoDlswTConnTcpOperEntry,
       "ciscoDlswTConnTcpOperKeepAliveInt": ciscoDlswTConnTcpOperKeepAliveInt,
       "ciscoDlswTConnTcpOperPrefTcpConnections": ciscoDlswTConnTcpOperPrefTcpConnections,
       "ciscoDlswTConnTcpOperTcpConnections": ciscoDlswTConnTcpOperTcpConnections,
       "ciscoDlswInterface": ciscoDlswInterface,
       "ciscoDlswIfTable": ciscoDlswIfTable,
       "ciscoDlswIfEntry": ciscoDlswIfEntry,
       "ciscoDlswIfRowStatus": ciscoDlswIfRowStatus,
       "ciscoDlswIfVirtualSegment": ciscoDlswIfVirtualSegment,
       "ciscoDlswIfSapList": ciscoDlswIfSapList,
       "ciscoDlswDirectory": ciscoDlswDirectory,
       "ciscoDlswDirStat": ciscoDlswDirStat,
       "ciscoDlswDirMacEntries": ciscoDlswDirMacEntries,
       "ciscoDlswDirMacCacheHits": ciscoDlswDirMacCacheHits,
       "ciscoDlswDirMacCacheMisses": ciscoDlswDirMacCacheMisses,
       "ciscoDlswDirNBEntries": ciscoDlswDirNBEntries,
       "ciscoDlswDirNBCacheHits": ciscoDlswDirNBCacheHits,
       "ciscoDlswDirNBCacheMisses": ciscoDlswDirNBCacheMisses,
       "ciscoDlswDirCache": ciscoDlswDirCache,
       "ciscoDlswDirMacTable": ciscoDlswDirMacTable,
       "ciscoDlswDirMacEntry": ciscoDlswDirMacEntry,
       "ciscoDlswDirMacIndex": ciscoDlswDirMacIndex,
       "ciscoDlswDirMacMac": ciscoDlswDirMacMac,
       "ciscoDlswDirMacMask": ciscoDlswDirMacMask,
       "ciscoDlswDirMacEntryType": ciscoDlswDirMacEntryType,
       "ciscoDlswDirMacLocationType": ciscoDlswDirMacLocationType,
       "ciscoDlswDirMacLocation": ciscoDlswDirMacLocation,
       "ciscoDlswDirMacStatus": ciscoDlswDirMacStatus,
       "ciscoDlswDirMacLFSize": ciscoDlswDirMacLFSize,
       "ciscoDlswDirMacRowStatus": ciscoDlswDirMacRowStatus,
       "ciscoDlswDirNBTable": ciscoDlswDirNBTable,
       "ciscoDlswDirNBEntry": ciscoDlswDirNBEntry,
       "ciscoDlswDirNBIndex": ciscoDlswDirNBIndex,
       "ciscoDlswDirNBName": ciscoDlswDirNBName,
       "ciscoDlswDirNBNameType": ciscoDlswDirNBNameType,
       "ciscoDlswDirNBEntryType": ciscoDlswDirNBEntryType,
       "ciscoDlswDirNBLocationType": ciscoDlswDirNBLocationType,
       "ciscoDlswDirNBLocation": ciscoDlswDirNBLocation,
       "ciscoDlswDirNBStatus": ciscoDlswDirNBStatus,
       "ciscoDlswDirNBLFSize": ciscoDlswDirNBLFSize,
       "ciscoDlswDirNBRowStatus": ciscoDlswDirNBRowStatus,
       "ciscoDlswDirLocate": ciscoDlswDirLocate,
       "ciscoDlswDirLocateMacTable": ciscoDlswDirLocateMacTable,
       "ciscoDlswDirLocateMacEntry": ciscoDlswDirLocateMacEntry,
       "ciscoDlswDirLocateMacMac": ciscoDlswDirLocateMacMac,
       "ciscoDlswDirLocateMacMatch": ciscoDlswDirLocateMacMatch,
       "ciscoDlswDirLocateMacLocation": ciscoDlswDirLocateMacLocation,
       "ciscoDlswDirLocateNBTable": ciscoDlswDirLocateNBTable,
       "ciscoDlswDirLocateNBEntry": ciscoDlswDirLocateNBEntry,
       "ciscoDlswDirLocateNBName": ciscoDlswDirLocateNBName,
       "ciscoDlswDirLocateNBMatch": ciscoDlswDirLocateNBMatch,
       "ciscoDlswDirLocateNBLocation": ciscoDlswDirLocateNBLocation,
       "ciscoDlswCircuit": ciscoDlswCircuit,
       "ciscoDlswCircuitStat": ciscoDlswCircuitStat,
       "ciscoDlswActiveCircuits": ciscoDlswActiveCircuits,
       "ciscoDlswCircuitCreates": ciscoDlswCircuitCreates,
       "ciscoDlswCircuitTable": ciscoDlswCircuitTable,
       "ciscoDlswCircuitEntry": ciscoDlswCircuitEntry,
       "ciscoDlswCircuitS1Mac": ciscoDlswCircuitS1Mac,
       "ciscoDlswCircuitS1Sap": ciscoDlswCircuitS1Sap,
       "ciscoDlswCircuitS1IfIndex": ciscoDlswCircuitS1IfIndex,
       "ciscoDlswCircuitS1DlcType": ciscoDlswCircuitS1DlcType,
       "ciscoDlswCircuitS1RouteInfo": ciscoDlswCircuitS1RouteInfo,
       "ciscoDlswCircuitS1CircuitId": ciscoDlswCircuitS1CircuitId,
       "ciscoDlswCircuitS1Dlc": ciscoDlswCircuitS1Dlc,
       "ciscoDlswCircuitS2Mac": ciscoDlswCircuitS2Mac,
       "ciscoDlswCircuitS2Sap": ciscoDlswCircuitS2Sap,
       "ciscoDlswCircuitS2Location": ciscoDlswCircuitS2Location,
       "ciscoDlswCircuitS2TDomain": ciscoDlswCircuitS2TDomain,
       "ciscoDlswCircuitS2TAddress": ciscoDlswCircuitS2TAddress,
       "ciscoDlswCircuitS2CircuitId": ciscoDlswCircuitS2CircuitId,
       "ciscoDlswCircuitOrigin": ciscoDlswCircuitOrigin,
       "ciscoDlswCircuitEntryTime": ciscoDlswCircuitEntryTime,
       "ciscoDlswCircuitStateTime": ciscoDlswCircuitStateTime,
       "ciscoDlswCircuitState": ciscoDlswCircuitState,
       "ciscoDlswCircuitPriority": ciscoDlswCircuitPriority,
       "ciscoDlswCircuitFCSendGrantedUnits": ciscoDlswCircuitFCSendGrantedUnits,
       "ciscoDlswCircuitFCSendCurrentWndw": ciscoDlswCircuitFCSendCurrentWndw,
       "ciscoDlswCircuitFCRecvGrantedUnits": ciscoDlswCircuitFCRecvGrantedUnits,
       "ciscoDlswCircuitFCRecvCurrentWndw": ciscoDlswCircuitFCRecvCurrentWndw,
       "ciscoDlswCircuitFCLargestRecvGranted": ciscoDlswCircuitFCLargestRecvGranted,
       "ciscoDlswCircuitFCLargestSendGranted": ciscoDlswCircuitFCLargestSendGranted,
       "ciscoDlswCircuitFCHalveWndwSents": ciscoDlswCircuitFCHalveWndwSents,
       "ciscoDlswCircuitFCResetOpSents": ciscoDlswCircuitFCResetOpSents,
       "ciscoDlswCircuitFCHalveWndwRcvds": ciscoDlswCircuitFCHalveWndwRcvds,
       "ciscoDlswCircuitFCResetOpRcvds": ciscoDlswCircuitFCResetOpRcvds,
       "ciscoDlswCircuitDiscReasonLocal": ciscoDlswCircuitDiscReasonLocal,
       "ciscoDlswCircuitDiscReasonRemote": ciscoDlswCircuitDiscReasonRemote,
       "ciscoDlswCircuitDiscReasonRemoteData": ciscoDlswCircuitDiscReasonRemoteData,
       "ciscoDlswSdlc": ciscoDlswSdlc,
       "ciscoDlswSdlcLsEntries": ciscoDlswSdlcLsEntries,
       "ciscoDlswSdlcLsTable": ciscoDlswSdlcLsTable,
       "ciscoDlswSdlcLsEntry": ciscoDlswSdlcLsEntry,
       "ciscoDlswSdlcLsLocalMac": ciscoDlswSdlcLsLocalMac,
       "ciscoDlswSdlcLsLocalSap": ciscoDlswSdlcLsLocalSap,
       "ciscoDlswSdlcLsLocalBlockNum": ciscoDlswSdlcLsLocalBlockNum,
       "ciscoDlswSdlcLsLocalIdNum": ciscoDlswSdlcLsLocalIdNum,
       "ciscoDlswSdlcLsRemoteMac": ciscoDlswSdlcLsRemoteMac,
       "ciscoDlswSdlcLsRemoteSap": ciscoDlswSdlcLsRemoteSap,
       "ciscoDlswSdlcLsRowStatus": ciscoDlswSdlcLsRowStatus,
       "ciscoDlswTraps": ciscoDlswTraps,
       "ciscoDlswTrapTConnPartnerReject": ciscoDlswTrapTConnPartnerReject,
       "ciscoDlswTrapTConnProtViolation": ciscoDlswTrapTConnProtViolation,
       "ciscoDlswTrapTConnUp": ciscoDlswTrapTConnUp,
       "ciscoDlswTrapTConnDown": ciscoDlswTrapTConnDown,
       "ciscoDlswTrapCircuitUp": ciscoDlswTrapCircuitUp,
       "ciscoDlswTrapCircuitDown": ciscoDlswTrapCircuitDown,
       "ciscoDlswDomains": ciscoDlswDomains,
       "ciscoDlswTCPDomain": ciscoDlswTCPDomain,
       "ciscoDlswConformance": ciscoDlswConformance,
       "ciscoDlswCompliances": ciscoDlswCompliances,
       "ciscoDlswCoreCompliance": ciscoDlswCoreCompliance,
       "ciscoDlswDirCompliance": ciscoDlswDirCompliance,
       "ciscoDlswDirLocateCompliance": ciscoDlswDirLocateCompliance,
       "ciscoDlswSdlcCompliance": ciscoDlswSdlcCompliance,
       "ciscoDlswCoreComplianceV11R01": ciscoDlswCoreComplianceV11R01,
       "ciscoDlswDirComplianceV11R01": ciscoDlswDirComplianceV11R01,
       "ciscoDlswSdlcComplianceV11R01": ciscoDlswSdlcComplianceV11R01,
       "ciscoDlswGroups": ciscoDlswGroups,
       "ciscoDlswNodeGroup": ciscoDlswNodeGroup,
       "ciscoDlswNodeNBGroup": ciscoDlswNodeNBGroup,
       "ciscoDlswTConnStatGroup": ciscoDlswTConnStatGroup,
       "ciscoDlswTConnConfigGroup": ciscoDlswTConnConfigGroup,
       "ciscoDlswTConnOperGroup": ciscoDlswTConnOperGroup,
       "ciscoDlswTConnNBGroup": ciscoDlswTConnNBGroup,
       "ciscoDlswInterfaceGroup": ciscoDlswInterfaceGroup,
       "ciscoDlswDirGroup": ciscoDlswDirGroup,
       "ciscoDlswDirNBGroup": ciscoDlswDirNBGroup,
       "ciscoDlswDirLocateGroup": ciscoDlswDirLocateGroup,
       "ciscoDlswDirLocateNBGroup": ciscoDlswDirLocateNBGroup,
       "ciscoDlswCircuitGroup": ciscoDlswCircuitGroup,
       "ciscoDlswSdlcGroup": ciscoDlswSdlcGroup,
       "ciscoDlswTConnTcpConfigGroup": ciscoDlswTConnTcpConfigGroup,
       "ciscoDlswTConnTcpOperGroup": ciscoDlswTConnTcpOperGroup,
       "ciscoDlswCircuitStatGroup": ciscoDlswCircuitStatGroup}
)
