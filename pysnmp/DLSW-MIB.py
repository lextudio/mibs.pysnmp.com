# SNMP MIB module (DLSW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLSW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:03 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlsw = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 46)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NBName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class MacAddressNC(OctetString, TextualConvention):
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
        ValueSizeConstraint(0, 255),
    )



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



class DlswTCPAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_Null_ObjectIdentity = ObjectIdentity
null = _Null_ObjectIdentity(
    (0, 0)
)
_DlswMIB_ObjectIdentity = ObjectIdentity
dlswMIB = _DlswMIB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1)
)
_DlswTraps_ObjectIdentity = ObjectIdentity
dlswTraps = _DlswTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 0)
)
_DlswNode_ObjectIdentity = ObjectIdentity
dlswNode = _DlswNode_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 1)
)


class _DlswNodeVersion_Type(OctetString):
    """Custom type dlswNodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DlswNodeVersion_Type.__name__ = "OctetString"
_DlswNodeVersion_Object = MibScalar
dlswNodeVersion = _DlswNodeVersion_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 1),
    _DlswNodeVersion_Type()
)
dlswNodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswNodeVersion.setStatus("current")


class _DlswNodeVendorID_Type(OctetString):
    """Custom type dlswNodeVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_DlswNodeVendorID_Type.__name__ = "OctetString"
_DlswNodeVendorID_Object = MibScalar
dlswNodeVendorID = _DlswNodeVendorID_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 2),
    _DlswNodeVendorID_Type()
)
dlswNodeVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswNodeVendorID.setStatus("current")
_DlswNodeVersionString_Type = DisplayString
_DlswNodeVersionString_Object = MibScalar
dlswNodeVersionString = _DlswNodeVersionString_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 3),
    _DlswNodeVersionString_Type()
)
dlswNodeVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswNodeVersionString.setStatus("current")


class _DlswNodeStdPacingSupport_Type(Integer32):
    """Custom type dlswNodeStdPacingSupport based on Integer32"""
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


_DlswNodeStdPacingSupport_Type.__name__ = "Integer32"
_DlswNodeStdPacingSupport_Object = MibScalar
dlswNodeStdPacingSupport = _DlswNodeStdPacingSupport_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 4),
    _DlswNodeStdPacingSupport_Type()
)
dlswNodeStdPacingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswNodeStdPacingSupport.setStatus("current")


class _DlswNodeStatus_Type(Integer32):
    """Custom type dlswNodeStatus based on Integer32"""
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


_DlswNodeStatus_Type.__name__ = "Integer32"
_DlswNodeStatus_Object = MibScalar
dlswNodeStatus = _DlswNodeStatus_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 5),
    _DlswNodeStatus_Type()
)
dlswNodeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeStatus.setStatus("current")
_DlswNodeUpTime_Type = TimeTicks
_DlswNodeUpTime_Object = MibScalar
dlswNodeUpTime = _DlswNodeUpTime_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 6),
    _DlswNodeUpTime_Type()
)
dlswNodeUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswNodeUpTime.setStatus("current")
if mibBuilder.loadTexts:
    dlswNodeUpTime.setUnits("hundredths of a second")


class _DlswNodeVirtualSegmentLFSize_Type(LFSize):
    """Custom type dlswNodeVirtualSegmentLFSize based on LFSize"""


_DlswNodeVirtualSegmentLFSize_Object = MibScalar
dlswNodeVirtualSegmentLFSize = _DlswNodeVirtualSegmentLFSize_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 7),
    _DlswNodeVirtualSegmentLFSize_Type()
)
dlswNodeVirtualSegmentLFSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeVirtualSegmentLFSize.setStatus("current")
_DlswNodeResourceNBExclusivity_Type = TruthValue
_DlswNodeResourceNBExclusivity_Object = MibScalar
dlswNodeResourceNBExclusivity = _DlswNodeResourceNBExclusivity_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 8),
    _DlswNodeResourceNBExclusivity_Type()
)
dlswNodeResourceNBExclusivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeResourceNBExclusivity.setStatus("current")
_DlswNodeResourceMacExclusivity_Type = TruthValue
_DlswNodeResourceMacExclusivity_Object = MibScalar
dlswNodeResourceMacExclusivity = _DlswNodeResourceMacExclusivity_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 9),
    _DlswNodeResourceMacExclusivity_Type()
)
dlswNodeResourceMacExclusivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeResourceMacExclusivity.setStatus("current")
_DlswTrapControl_ObjectIdentity = ObjectIdentity
dlswTrapControl = _DlswTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 10)
)


class _DlswTrapCntlTConnPartnerReject_Type(Integer32):
    """Custom type dlswTrapCntlTConnPartnerReject based on Integer32"""
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


_DlswTrapCntlTConnPartnerReject_Type.__name__ = "Integer32"
_DlswTrapCntlTConnPartnerReject_Object = MibScalar
dlswTrapCntlTConnPartnerReject = _DlswTrapCntlTConnPartnerReject_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 10, 1),
    _DlswTrapCntlTConnPartnerReject_Type()
)
dlswTrapCntlTConnPartnerReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTrapCntlTConnPartnerReject.setStatus("current")
_DlswTrapCntlTConnProtViolation_Type = TruthValue
_DlswTrapCntlTConnProtViolation_Object = MibScalar
dlswTrapCntlTConnProtViolation = _DlswTrapCntlTConnProtViolation_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 10, 2),
    _DlswTrapCntlTConnProtViolation_Type()
)
dlswTrapCntlTConnProtViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTrapCntlTConnProtViolation.setStatus("current")


class _DlswTrapCntlTConn_Type(Integer32):
    """Custom type dlswTrapCntlTConn based on Integer32"""
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


_DlswTrapCntlTConn_Type.__name__ = "Integer32"
_DlswTrapCntlTConn_Object = MibScalar
dlswTrapCntlTConn = _DlswTrapCntlTConn_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 10, 3),
    _DlswTrapCntlTConn_Type()
)
dlswTrapCntlTConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTrapCntlTConn.setStatus("current")


class _DlswTrapCntlCircuit_Type(Integer32):
    """Custom type dlswTrapCntlCircuit based on Integer32"""
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


_DlswTrapCntlCircuit_Type.__name__ = "Integer32"
_DlswTrapCntlCircuit_Object = MibScalar
dlswTrapCntlCircuit = _DlswTrapCntlCircuit_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 1, 10, 4),
    _DlswTrapCntlCircuit_Type()
)
dlswTrapCntlCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTrapCntlCircuit.setStatus("current")
_DlswTConn_ObjectIdentity = ObjectIdentity
dlswTConn = _DlswTConn_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 2)
)
_DlswTConnStat_ObjectIdentity = ObjectIdentity
dlswTConnStat = _DlswTConnStat_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 1)
)
_DlswTConnStatActiveConnections_Type = Gauge32
_DlswTConnStatActiveConnections_Object = MibScalar
dlswTConnStatActiveConnections = _DlswTConnStatActiveConnections_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 1, 1),
    _DlswTConnStatActiveConnections_Type()
)
dlswTConnStatActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnStatActiveConnections.setStatus("current")
_DlswTConnStatCloseIdles_Type = Counter32
_DlswTConnStatCloseIdles_Object = MibScalar
dlswTConnStatCloseIdles = _DlswTConnStatCloseIdles_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 1, 2),
    _DlswTConnStatCloseIdles_Type()
)
dlswTConnStatCloseIdles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnStatCloseIdles.setStatus("current")
_DlswTConnStatCloseBusys_Type = Counter32
_DlswTConnStatCloseBusys_Object = MibScalar
dlswTConnStatCloseBusys = _DlswTConnStatCloseBusys_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 1, 3),
    _DlswTConnStatCloseBusys_Type()
)
dlswTConnStatCloseBusys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnStatCloseBusys.setStatus("current")
_DlswTConnConfigTable_Object = MibTable
dlswTConnConfigTable = _DlswTConnConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dlswTConnConfigTable.setStatus("current")
_DlswTConnConfigEntry_Object = MibTableRow
dlswTConnConfigEntry = _DlswTConnConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1)
)
dlswTConnConfigEntry.setIndexNames(
    (0, "DLSW-MIB", "dlswTConnConfigIndex"),
)
if mibBuilder.loadTexts:
    dlswTConnConfigEntry.setStatus("current")


class _DlswTConnConfigIndex_Type(Integer32):
    """Custom type dlswTConnConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlswTConnConfigIndex_Type.__name__ = "Integer32"
_DlswTConnConfigIndex_Object = MibTableColumn
dlswTConnConfigIndex = _DlswTConnConfigIndex_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 1),
    _DlswTConnConfigIndex_Type()
)
dlswTConnConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswTConnConfigIndex.setStatus("current")
_DlswTConnConfigTDomain_Type = ObjectIdentifier
_DlswTConnConfigTDomain_Object = MibTableColumn
dlswTConnConfigTDomain = _DlswTConnConfigTDomain_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 2),
    _DlswTConnConfigTDomain_Type()
)
dlswTConnConfigTDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnConfigTDomain.setStatus("current")
_DlswTConnConfigLocalTAddr_Type = TAddress
_DlswTConnConfigLocalTAddr_Object = MibTableColumn
dlswTConnConfigLocalTAddr = _DlswTConnConfigLocalTAddr_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 3),
    _DlswTConnConfigLocalTAddr_Type()
)
dlswTConnConfigLocalTAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnConfigLocalTAddr.setStatus("current")
_DlswTConnConfigRemoteTAddr_Type = TAddress
_DlswTConnConfigRemoteTAddr_Object = MibTableColumn
dlswTConnConfigRemoteTAddr = _DlswTConnConfigRemoteTAddr_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 4),
    _DlswTConnConfigRemoteTAddr_Type()
)
dlswTConnConfigRemoteTAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnConfigRemoteTAddr.setStatus("current")
_DlswTConnConfigLastModifyTime_Type = TimeTicks
_DlswTConnConfigLastModifyTime_Object = MibTableColumn
dlswTConnConfigLastModifyTime = _DlswTConnConfigLastModifyTime_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 5),
    _DlswTConnConfigLastModifyTime_Type()
)
dlswTConnConfigLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnConfigLastModifyTime.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnConfigLastModifyTime.setUnits("hundredths of a second")


class _DlswTConnConfigEntryType_Type(Integer32):
    """Custom type dlswTConnConfigEntryType based on Integer32"""
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


_DlswTConnConfigEntryType_Type.__name__ = "Integer32"
_DlswTConnConfigEntryType_Object = MibTableColumn
dlswTConnConfigEntryType = _DlswTConnConfigEntryType_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 6),
    _DlswTConnConfigEntryType_Type()
)
dlswTConnConfigEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnConfigEntryType.setStatus("current")
_DlswTConnConfigGroupDefinition_Type = RowPointer
_DlswTConnConfigGroupDefinition_Object = MibTableColumn
dlswTConnConfigGroupDefinition = _DlswTConnConfigGroupDefinition_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 7),
    _DlswTConnConfigGroupDefinition_Type()
)
dlswTConnConfigGroupDefinition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnConfigGroupDefinition.setStatus("current")


class _DlswTConnConfigSetupType_Type(Integer32):
    """Custom type dlswTConnConfigSetupType based on Integer32"""
    defaultValue = 4

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


_DlswTConnConfigSetupType_Type.__name__ = "Integer32"
_DlswTConnConfigSetupType_Object = MibTableColumn
dlswTConnConfigSetupType = _DlswTConnConfigSetupType_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 8),
    _DlswTConnConfigSetupType_Type()
)
dlswTConnConfigSetupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnConfigSetupType.setStatus("current")


class _DlswTConnConfigSapList_Type(OctetString):
    """Custom type dlswTConnConfigSapList based on OctetString"""
    defaultHexValue = "AA000000000000000000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_DlswTConnConfigSapList_Type.__name__ = "OctetString"
_DlswTConnConfigSapList_Object = MibTableColumn
dlswTConnConfigSapList = _DlswTConnConfigSapList_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 9),
    _DlswTConnConfigSapList_Type()
)
dlswTConnConfigSapList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnConfigSapList.setStatus("current")


class _DlswTConnConfigAdvertiseMacNB_Type(TruthValue):
    """Custom type dlswTConnConfigAdvertiseMacNB based on TruthValue"""


_DlswTConnConfigAdvertiseMacNB_Object = MibTableColumn
dlswTConnConfigAdvertiseMacNB = _DlswTConnConfigAdvertiseMacNB_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 10),
    _DlswTConnConfigAdvertiseMacNB_Type()
)
dlswTConnConfigAdvertiseMacNB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnConfigAdvertiseMacNB.setStatus("current")


class _DlswTConnConfigInitCirRecvWndw_Type(Integer32):
    """Custom type dlswTConnConfigInitCirRecvWndw based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswTConnConfigInitCirRecvWndw_Type.__name__ = "Integer32"
_DlswTConnConfigInitCirRecvWndw_Object = MibTableColumn
dlswTConnConfigInitCirRecvWndw = _DlswTConnConfigInitCirRecvWndw_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 11),
    _DlswTConnConfigInitCirRecvWndw_Type()
)
dlswTConnConfigInitCirRecvWndw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnConfigInitCirRecvWndw.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnConfigInitCirRecvWndw.setUnits("SSP messages")
_DlswTConnConfigOpens_Type = Counter32
_DlswTConnConfigOpens_Object = MibTableColumn
dlswTConnConfigOpens = _DlswTConnConfigOpens_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 12),
    _DlswTConnConfigOpens_Type()
)
dlswTConnConfigOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnConfigOpens.setStatus("current")
_DlswTConnConfigRowStatus_Type = RowStatus
_DlswTConnConfigRowStatus_Object = MibTableColumn
dlswTConnConfigRowStatus = _DlswTConnConfigRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 2, 1, 13),
    _DlswTConnConfigRowStatus_Type()
)
dlswTConnConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnConfigRowStatus.setStatus("current")
_DlswTConnOperTable_Object = MibTable
dlswTConnOperTable = _DlswTConnOperTable_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dlswTConnOperTable.setStatus("current")
_DlswTConnOperEntry_Object = MibTableRow
dlswTConnOperEntry = _DlswTConnOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1)
)
dlswTConnOperEntry.setIndexNames(
    (0, "DLSW-MIB", "dlswTConnOperTDomain"),
    (0, "DLSW-MIB", "dlswTConnOperRemoteTAddr"),
)
if mibBuilder.loadTexts:
    dlswTConnOperEntry.setStatus("current")
_DlswTConnOperTDomain_Type = ObjectIdentifier
_DlswTConnOperTDomain_Object = MibTableColumn
dlswTConnOperTDomain = _DlswTConnOperTDomain_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 1),
    _DlswTConnOperTDomain_Type()
)
dlswTConnOperTDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswTConnOperTDomain.setStatus("current")
_DlswTConnOperLocalTAddr_Type = TAddress
_DlswTConnOperLocalTAddr_Object = MibTableColumn
dlswTConnOperLocalTAddr = _DlswTConnOperLocalTAddr_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 2),
    _DlswTConnOperLocalTAddr_Type()
)
dlswTConnOperLocalTAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperLocalTAddr.setStatus("current")
_DlswTConnOperRemoteTAddr_Type = TAddress
_DlswTConnOperRemoteTAddr_Object = MibTableColumn
dlswTConnOperRemoteTAddr = _DlswTConnOperRemoteTAddr_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 3),
    _DlswTConnOperRemoteTAddr_Type()
)
dlswTConnOperRemoteTAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswTConnOperRemoteTAddr.setStatus("current")
_DlswTConnOperEntryTime_Type = TimeTicks
_DlswTConnOperEntryTime_Object = MibTableColumn
dlswTConnOperEntryTime = _DlswTConnOperEntryTime_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 4),
    _DlswTConnOperEntryTime_Type()
)
dlswTConnOperEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperEntryTime.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnOperEntryTime.setUnits("hundredths of a second")
_DlswTConnOperConnectTime_Type = TimeTicks
_DlswTConnOperConnectTime_Object = MibTableColumn
dlswTConnOperConnectTime = _DlswTConnOperConnectTime_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 5),
    _DlswTConnOperConnectTime_Type()
)
dlswTConnOperConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperConnectTime.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnOperConnectTime.setUnits("hundredths of a second")


class _DlswTConnOperState_Type(Integer32):
    """Custom type dlswTConnOperState based on Integer32"""
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


_DlswTConnOperState_Type.__name__ = "Integer32"
_DlswTConnOperState_Object = MibTableColumn
dlswTConnOperState = _DlswTConnOperState_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 6),
    _DlswTConnOperState_Type()
)
dlswTConnOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTConnOperState.setStatus("current")


class _DlswTConnOperConfigIndex_Type(Integer32):
    """Custom type dlswTConnOperConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlswTConnOperConfigIndex_Type.__name__ = "Integer32"
_DlswTConnOperConfigIndex_Object = MibTableColumn
dlswTConnOperConfigIndex = _DlswTConnOperConfigIndex_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 7),
    _DlswTConnOperConfigIndex_Type()
)
dlswTConnOperConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperConfigIndex.setStatus("current")


class _DlswTConnOperFlowCntlMode_Type(Integer32):
    """Custom type dlswTConnOperFlowCntlMode based on Integer32"""
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


_DlswTConnOperFlowCntlMode_Type.__name__ = "Integer32"
_DlswTConnOperFlowCntlMode_Object = MibTableColumn
dlswTConnOperFlowCntlMode = _DlswTConnOperFlowCntlMode_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 8),
    _DlswTConnOperFlowCntlMode_Type()
)
dlswTConnOperFlowCntlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperFlowCntlMode.setStatus("current")


class _DlswTConnOperPartnerVersion_Type(OctetString):
    """Custom type dlswTConnOperPartnerVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )


_DlswTConnOperPartnerVersion_Type.__name__ = "OctetString"
_DlswTConnOperPartnerVersion_Object = MibTableColumn
dlswTConnOperPartnerVersion = _DlswTConnOperPartnerVersion_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 9),
    _DlswTConnOperPartnerVersion_Type()
)
dlswTConnOperPartnerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerVersion.setStatus("current")


class _DlswTConnOperPartnerVendorID_Type(OctetString):
    """Custom type dlswTConnOperPartnerVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 3),
    )


_DlswTConnOperPartnerVendorID_Type.__name__ = "OctetString"
_DlswTConnOperPartnerVendorID_Object = MibTableColumn
dlswTConnOperPartnerVendorID = _DlswTConnOperPartnerVendorID_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 10),
    _DlswTConnOperPartnerVendorID_Type()
)
dlswTConnOperPartnerVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerVendorID.setStatus("current")


class _DlswTConnOperPartnerVersionStr_Type(DisplayString):
    """Custom type dlswTConnOperPartnerVersionStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_DlswTConnOperPartnerVersionStr_Type.__name__ = "DisplayString"
_DlswTConnOperPartnerVersionStr_Object = MibTableColumn
dlswTConnOperPartnerVersionStr = _DlswTConnOperPartnerVersionStr_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 11),
    _DlswTConnOperPartnerVersionStr_Type()
)
dlswTConnOperPartnerVersionStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerVersionStr.setStatus("current")


class _DlswTConnOperPartnerInitPacingWndw_Type(Integer32):
    """Custom type dlswTConnOperPartnerInitPacingWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswTConnOperPartnerInitPacingWndw_Type.__name__ = "Integer32"
_DlswTConnOperPartnerInitPacingWndw_Object = MibTableColumn
dlswTConnOperPartnerInitPacingWndw = _DlswTConnOperPartnerInitPacingWndw_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 12),
    _DlswTConnOperPartnerInitPacingWndw_Type()
)
dlswTConnOperPartnerInitPacingWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerInitPacingWndw.setStatus("current")


class _DlswTConnOperPartnerSapList_Type(OctetString):
    """Custom type dlswTConnOperPartnerSapList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_DlswTConnOperPartnerSapList_Type.__name__ = "OctetString"
_DlswTConnOperPartnerSapList_Object = MibTableColumn
dlswTConnOperPartnerSapList = _DlswTConnOperPartnerSapList_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 13),
    _DlswTConnOperPartnerSapList_Type()
)
dlswTConnOperPartnerSapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerSapList.setStatus("current")
_DlswTConnOperPartnerNBExcl_Type = TruthValue
_DlswTConnOperPartnerNBExcl_Object = MibTableColumn
dlswTConnOperPartnerNBExcl = _DlswTConnOperPartnerNBExcl_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 14),
    _DlswTConnOperPartnerNBExcl_Type()
)
dlswTConnOperPartnerNBExcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerNBExcl.setStatus("current")
_DlswTConnOperPartnerMacExcl_Type = TruthValue
_DlswTConnOperPartnerMacExcl_Object = MibTableColumn
dlswTConnOperPartnerMacExcl = _DlswTConnOperPartnerMacExcl_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 15),
    _DlswTConnOperPartnerMacExcl_Type()
)
dlswTConnOperPartnerMacExcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerMacExcl.setStatus("current")


class _DlswTConnOperPartnerNBInfo_Type(Integer32):
    """Custom type dlswTConnOperPartnerNBInfo based on Integer32"""
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


_DlswTConnOperPartnerNBInfo_Type.__name__ = "Integer32"
_DlswTConnOperPartnerNBInfo_Object = MibTableColumn
dlswTConnOperPartnerNBInfo = _DlswTConnOperPartnerNBInfo_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 16),
    _DlswTConnOperPartnerNBInfo_Type()
)
dlswTConnOperPartnerNBInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerNBInfo.setStatus("current")


class _DlswTConnOperPartnerMacInfo_Type(Integer32):
    """Custom type dlswTConnOperPartnerMacInfo based on Integer32"""
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


_DlswTConnOperPartnerMacInfo_Type.__name__ = "Integer32"
_DlswTConnOperPartnerMacInfo_Object = MibTableColumn
dlswTConnOperPartnerMacInfo = _DlswTConnOperPartnerMacInfo_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 17),
    _DlswTConnOperPartnerMacInfo_Type()
)
dlswTConnOperPartnerMacInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperPartnerMacInfo.setStatus("current")
_DlswTConnOperDiscTime_Type = TimeTicks
_DlswTConnOperDiscTime_Object = MibTableColumn
dlswTConnOperDiscTime = _DlswTConnOperDiscTime_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 18),
    _DlswTConnOperDiscTime_Type()
)
dlswTConnOperDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperDiscTime.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnOperDiscTime.setUnits("hundredths of a second")


class _DlswTConnOperDiscReason_Type(Integer32):
    """Custom type dlswTConnOperDiscReason based on Integer32"""
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


_DlswTConnOperDiscReason_Type.__name__ = "Integer32"
_DlswTConnOperDiscReason_Object = MibTableColumn
dlswTConnOperDiscReason = _DlswTConnOperDiscReason_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 19),
    _DlswTConnOperDiscReason_Type()
)
dlswTConnOperDiscReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperDiscReason.setStatus("current")


class _DlswTConnOperDiscActiveCir_Type(Integer32):
    """Custom type dlswTConnOperDiscActiveCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlswTConnOperDiscActiveCir_Type.__name__ = "Integer32"
_DlswTConnOperDiscActiveCir_Object = MibTableColumn
dlswTConnOperDiscActiveCir = _DlswTConnOperDiscActiveCir_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 20),
    _DlswTConnOperDiscActiveCir_Type()
)
dlswTConnOperDiscActiveCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperDiscActiveCir.setStatus("current")
_DlswTConnOperInDataPkts_Type = Counter32
_DlswTConnOperInDataPkts_Object = MibTableColumn
dlswTConnOperInDataPkts = _DlswTConnOperInDataPkts_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 21),
    _DlswTConnOperInDataPkts_Type()
)
dlswTConnOperInDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperInDataPkts.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnOperInDataPkts.setUnits("SSP messages")
_DlswTConnOperOutDataPkts_Type = Counter32
_DlswTConnOperOutDataPkts_Object = MibTableColumn
dlswTConnOperOutDataPkts = _DlswTConnOperOutDataPkts_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 22),
    _DlswTConnOperOutDataPkts_Type()
)
dlswTConnOperOutDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperOutDataPkts.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnOperOutDataPkts.setUnits("SSP messages")
_DlswTConnOperInDataOctets_Type = Counter32
_DlswTConnOperInDataOctets_Object = MibTableColumn
dlswTConnOperInDataOctets = _DlswTConnOperInDataOctets_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 23),
    _DlswTConnOperInDataOctets_Type()
)
dlswTConnOperInDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperInDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnOperInDataOctets.setUnits("octets")
_DlswTConnOperOutDataOctets_Type = Counter32
_DlswTConnOperOutDataOctets_Object = MibTableColumn
dlswTConnOperOutDataOctets = _DlswTConnOperOutDataOctets_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 24),
    _DlswTConnOperOutDataOctets_Type()
)
dlswTConnOperOutDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperOutDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnOperOutDataOctets.setUnits("octets")
_DlswTConnOperInCntlPkts_Type = Counter32
_DlswTConnOperInCntlPkts_Object = MibTableColumn
dlswTConnOperInCntlPkts = _DlswTConnOperInCntlPkts_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 25),
    _DlswTConnOperInCntlPkts_Type()
)
dlswTConnOperInCntlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperInCntlPkts.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnOperInCntlPkts.setUnits("SSP messages")
_DlswTConnOperOutCntlPkts_Type = Counter32
_DlswTConnOperOutCntlPkts_Object = MibTableColumn
dlswTConnOperOutCntlPkts = _DlswTConnOperOutCntlPkts_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 26),
    _DlswTConnOperOutCntlPkts_Type()
)
dlswTConnOperOutCntlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperOutCntlPkts.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnOperOutCntlPkts.setUnits("SSP messages")
_DlswTConnOperCURexSents_Type = Counter32
_DlswTConnOperCURexSents_Object = MibTableColumn
dlswTConnOperCURexSents = _DlswTConnOperCURexSents_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 27),
    _DlswTConnOperCURexSents_Type()
)
dlswTConnOperCURexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperCURexSents.setStatus("current")
_DlswTConnOperICRexRcvds_Type = Counter32
_DlswTConnOperICRexRcvds_Object = MibTableColumn
dlswTConnOperICRexRcvds = _DlswTConnOperICRexRcvds_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 28),
    _DlswTConnOperICRexRcvds_Type()
)
dlswTConnOperICRexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperICRexRcvds.setStatus("current")
_DlswTConnOperCURexRcvds_Type = Counter32
_DlswTConnOperCURexRcvds_Object = MibTableColumn
dlswTConnOperCURexRcvds = _DlswTConnOperCURexRcvds_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 29),
    _DlswTConnOperCURexRcvds_Type()
)
dlswTConnOperCURexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperCURexRcvds.setStatus("current")
_DlswTConnOperICRexSents_Type = Counter32
_DlswTConnOperICRexSents_Object = MibTableColumn
dlswTConnOperICRexSents = _DlswTConnOperICRexSents_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 30),
    _DlswTConnOperICRexSents_Type()
)
dlswTConnOperICRexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperICRexSents.setStatus("current")
_DlswTConnOperNQexSents_Type = Counter32
_DlswTConnOperNQexSents_Object = MibTableColumn
dlswTConnOperNQexSents = _DlswTConnOperNQexSents_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 31),
    _DlswTConnOperNQexSents_Type()
)
dlswTConnOperNQexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperNQexSents.setStatus("current")
_DlswTConnOperNRexRcvds_Type = Counter32
_DlswTConnOperNRexRcvds_Object = MibTableColumn
dlswTConnOperNRexRcvds = _DlswTConnOperNRexRcvds_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 32),
    _DlswTConnOperNRexRcvds_Type()
)
dlswTConnOperNRexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperNRexRcvds.setStatus("current")
_DlswTConnOperNQexRcvds_Type = Counter32
_DlswTConnOperNQexRcvds_Object = MibTableColumn
dlswTConnOperNQexRcvds = _DlswTConnOperNQexRcvds_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 33),
    _DlswTConnOperNQexRcvds_Type()
)
dlswTConnOperNQexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperNQexRcvds.setStatus("current")
_DlswTConnOperNRexSents_Type = Counter32
_DlswTConnOperNRexSents_Object = MibTableColumn
dlswTConnOperNRexSents = _DlswTConnOperNRexSents_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 34),
    _DlswTConnOperNRexSents_Type()
)
dlswTConnOperNRexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperNRexSents.setStatus("current")
_DlswTConnOperCirCreates_Type = Counter32
_DlswTConnOperCirCreates_Object = MibTableColumn
dlswTConnOperCirCreates = _DlswTConnOperCirCreates_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 35),
    _DlswTConnOperCirCreates_Type()
)
dlswTConnOperCirCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperCirCreates.setStatus("current")
_DlswTConnOperCircuits_Type = Gauge32
_DlswTConnOperCircuits_Object = MibTableColumn
dlswTConnOperCircuits = _DlswTConnOperCircuits_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 3, 1, 36),
    _DlswTConnOperCircuits_Type()
)
dlswTConnOperCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnOperCircuits.setStatus("current")
_DlswTConnSpecific_ObjectIdentity = ObjectIdentity
dlswTConnSpecific = _DlswTConnSpecific_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 4)
)
_DlswTConnTcp_ObjectIdentity = ObjectIdentity
dlswTConnTcp = _DlswTConnTcp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 4, 1)
)
_DlswTConnTcpConfigTable_Object = MibTable
dlswTConnTcpConfigTable = _DlswTConnTcpConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dlswTConnTcpConfigTable.setStatus("current")
_DlswTConnTcpConfigEntry_Object = MibTableRow
dlswTConnTcpConfigEntry = _DlswTConnTcpConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 4, 1, 1, 1)
)
dlswTConnTcpConfigEntry.setIndexNames(
    (0, "DLSW-MIB", "dlswTConnConfigIndex"),
)
if mibBuilder.loadTexts:
    dlswTConnTcpConfigEntry.setStatus("current")


class _DlswTConnTcpConfigKeepAliveInt_Type(Integer32):
    """Custom type dlswTConnTcpConfigKeepAliveInt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_DlswTConnTcpConfigKeepAliveInt_Type.__name__ = "Integer32"
_DlswTConnTcpConfigKeepAliveInt_Object = MibTableColumn
dlswTConnTcpConfigKeepAliveInt = _DlswTConnTcpConfigKeepAliveInt_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 4, 1, 1, 1, 1),
    _DlswTConnTcpConfigKeepAliveInt_Type()
)
dlswTConnTcpConfigKeepAliveInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnTcpConfigKeepAliveInt.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnTcpConfigKeepAliveInt.setUnits("seconds")


class _DlswTConnTcpConfigTcpConnections_Type(Integer32):
    """Custom type dlswTConnTcpConfigTcpConnections based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DlswTConnTcpConfigTcpConnections_Type.__name__ = "Integer32"
_DlswTConnTcpConfigTcpConnections_Object = MibTableColumn
dlswTConnTcpConfigTcpConnections = _DlswTConnTcpConfigTcpConnections_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 4, 1, 1, 1, 2),
    _DlswTConnTcpConfigTcpConnections_Type()
)
dlswTConnTcpConfigTcpConnections.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnTcpConfigTcpConnections.setStatus("current")


class _DlswTConnTcpConfigMaxSegmentSize_Type(Integer32):
    """Custom type dlswTConnTcpConfigMaxSegmentSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswTConnTcpConfigMaxSegmentSize_Type.__name__ = "Integer32"
_DlswTConnTcpConfigMaxSegmentSize_Object = MibTableColumn
dlswTConnTcpConfigMaxSegmentSize = _DlswTConnTcpConfigMaxSegmentSize_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 4, 1, 1, 1, 3),
    _DlswTConnTcpConfigMaxSegmentSize_Type()
)
dlswTConnTcpConfigMaxSegmentSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswTConnTcpConfigMaxSegmentSize.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnTcpConfigMaxSegmentSize.setUnits("packets")
_DlswTConnTcpOperTable_Object = MibTable
dlswTConnTcpOperTable = _DlswTConnTcpOperTable_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    dlswTConnTcpOperTable.setStatus("current")
_DlswTConnTcpOperEntry_Object = MibTableRow
dlswTConnTcpOperEntry = _DlswTConnTcpOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 4, 1, 2, 1)
)
dlswTConnTcpOperEntry.setIndexNames(
    (0, "DLSW-MIB", "dlswTConnOperTDomain"),
    (0, "DLSW-MIB", "dlswTConnOperRemoteTAddr"),
)
if mibBuilder.loadTexts:
    dlswTConnTcpOperEntry.setStatus("current")


class _DlswTConnTcpOperKeepAliveInt_Type(Integer32):
    """Custom type dlswTConnTcpOperKeepAliveInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_DlswTConnTcpOperKeepAliveInt_Type.__name__ = "Integer32"
_DlswTConnTcpOperKeepAliveInt_Object = MibTableColumn
dlswTConnTcpOperKeepAliveInt = _DlswTConnTcpOperKeepAliveInt_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 4, 1, 2, 1, 1),
    _DlswTConnTcpOperKeepAliveInt_Type()
)
dlswTConnTcpOperKeepAliveInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnTcpOperKeepAliveInt.setStatus("current")
if mibBuilder.loadTexts:
    dlswTConnTcpOperKeepAliveInt.setUnits("seconds")


class _DlswTConnTcpOperPrefTcpConnections_Type(Integer32):
    """Custom type dlswTConnTcpOperPrefTcpConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DlswTConnTcpOperPrefTcpConnections_Type.__name__ = "Integer32"
_DlswTConnTcpOperPrefTcpConnections_Object = MibTableColumn
dlswTConnTcpOperPrefTcpConnections = _DlswTConnTcpOperPrefTcpConnections_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 4, 1, 2, 1, 2),
    _DlswTConnTcpOperPrefTcpConnections_Type()
)
dlswTConnTcpOperPrefTcpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnTcpOperPrefTcpConnections.setStatus("current")


class _DlswTConnTcpOperTcpConnections_Type(Integer32):
    """Custom type dlswTConnTcpOperTcpConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DlswTConnTcpOperTcpConnections_Type.__name__ = "Integer32"
_DlswTConnTcpOperTcpConnections_Object = MibTableColumn
dlswTConnTcpOperTcpConnections = _DlswTConnTcpOperTcpConnections_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 2, 4, 1, 2, 1, 3),
    _DlswTConnTcpOperTcpConnections_Type()
)
dlswTConnTcpOperTcpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswTConnTcpOperTcpConnections.setStatus("current")
_DlswInterface_ObjectIdentity = ObjectIdentity
dlswInterface = _DlswInterface_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 3)
)
_DlswIfTable_Object = MibTable
dlswIfTable = _DlswIfTable_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dlswIfTable.setStatus("current")
_DlswIfEntry_Object = MibTableRow
dlswIfEntry = _DlswIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 3, 1, 1)
)
dlswIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dlswIfEntry.setStatus("current")
_DlswIfRowStatus_Type = RowStatus
_DlswIfRowStatus_Object = MibTableColumn
dlswIfRowStatus = _DlswIfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 3, 1, 1, 1),
    _DlswIfRowStatus_Type()
)
dlswIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswIfRowStatus.setStatus("current")


class _DlswIfVirtualSegment_Type(Integer32):
    """Custom type dlswIfVirtualSegment based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_DlswIfVirtualSegment_Type.__name__ = "Integer32"
_DlswIfVirtualSegment_Object = MibTableColumn
dlswIfVirtualSegment = _DlswIfVirtualSegment_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 3, 1, 1, 2),
    _DlswIfVirtualSegment_Type()
)
dlswIfVirtualSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswIfVirtualSegment.setStatus("current")


class _DlswIfSapList_Type(OctetString):
    """Custom type dlswIfSapList based on OctetString"""
    defaultHexValue = "AA000000000000000000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_DlswIfSapList_Type.__name__ = "OctetString"
_DlswIfSapList_Object = MibTableColumn
dlswIfSapList = _DlswIfSapList_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 3, 1, 1, 3),
    _DlswIfSapList_Type()
)
dlswIfSapList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswIfSapList.setStatus("current")
_DlswDirectory_ObjectIdentity = ObjectIdentity
dlswDirectory = _DlswDirectory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 4)
)
_DlswDirStat_ObjectIdentity = ObjectIdentity
dlswDirStat = _DlswDirStat_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 1)
)
_DlswDirMacEntries_Type = Gauge32
_DlswDirMacEntries_Object = MibScalar
dlswDirMacEntries = _DlswDirMacEntries_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 1, 1),
    _DlswDirMacEntries_Type()
)
dlswDirMacEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacEntries.setStatus("current")
_DlswDirMacCacheHits_Type = Counter32
_DlswDirMacCacheHits_Object = MibScalar
dlswDirMacCacheHits = _DlswDirMacCacheHits_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 1, 2),
    _DlswDirMacCacheHits_Type()
)
dlswDirMacCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacCacheHits.setStatus("current")
_DlswDirMacCacheMisses_Type = Counter32
_DlswDirMacCacheMisses_Object = MibScalar
dlswDirMacCacheMisses = _DlswDirMacCacheMisses_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 1, 3),
    _DlswDirMacCacheMisses_Type()
)
dlswDirMacCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacCacheMisses.setStatus("current")


class _DlswDirMacCacheNextIndex_Type(Integer32):
    """Custom type dlswDirMacCacheNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlswDirMacCacheNextIndex_Type.__name__ = "Integer32"
_DlswDirMacCacheNextIndex_Object = MibScalar
dlswDirMacCacheNextIndex = _DlswDirMacCacheNextIndex_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 1, 4),
    _DlswDirMacCacheNextIndex_Type()
)
dlswDirMacCacheNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirMacCacheNextIndex.setStatus("current")
_DlswDirNBEntries_Type = Gauge32
_DlswDirNBEntries_Object = MibScalar
dlswDirNBEntries = _DlswDirNBEntries_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 1, 5),
    _DlswDirNBEntries_Type()
)
dlswDirNBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBEntries.setStatus("current")
_DlswDirNBCacheHits_Type = Counter32
_DlswDirNBCacheHits_Object = MibScalar
dlswDirNBCacheHits = _DlswDirNBCacheHits_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 1, 6),
    _DlswDirNBCacheHits_Type()
)
dlswDirNBCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBCacheHits.setStatus("current")
_DlswDirNBCacheMisses_Type = Counter32
_DlswDirNBCacheMisses_Object = MibScalar
dlswDirNBCacheMisses = _DlswDirNBCacheMisses_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 1, 7),
    _DlswDirNBCacheMisses_Type()
)
dlswDirNBCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBCacheMisses.setStatus("current")


class _DlswDirNBCacheNextIndex_Type(Integer32):
    """Custom type dlswDirNBCacheNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlswDirNBCacheNextIndex_Type.__name__ = "Integer32"
_DlswDirNBCacheNextIndex_Object = MibScalar
dlswDirNBCacheNextIndex = _DlswDirNBCacheNextIndex_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 1, 8),
    _DlswDirNBCacheNextIndex_Type()
)
dlswDirNBCacheNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirNBCacheNextIndex.setStatus("current")
_DlswDirCache_ObjectIdentity = ObjectIdentity
dlswDirCache = _DlswDirCache_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2)
)
_DlswDirMacTable_Object = MibTable
dlswDirMacTable = _DlswDirMacTable_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dlswDirMacTable.setStatus("current")
_DlswDirMacEntry_Object = MibTableRow
dlswDirMacEntry = _DlswDirMacEntry_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 1, 1)
)
dlswDirMacEntry.setIndexNames(
    (0, "DLSW-MIB", "dlswDirMacIndex"),
)
if mibBuilder.loadTexts:
    dlswDirMacEntry.setStatus("current")


class _DlswDirMacIndex_Type(Integer32):
    """Custom type dlswDirMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlswDirMacIndex_Type.__name__ = "Integer32"
_DlswDirMacIndex_Object = MibTableColumn
dlswDirMacIndex = _DlswDirMacIndex_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 1, 1, 1),
    _DlswDirMacIndex_Type()
)
dlswDirMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswDirMacIndex.setStatus("current")
_DlswDirMacMac_Type = MacAddressNC
_DlswDirMacMac_Object = MibTableColumn
dlswDirMacMac = _DlswDirMacMac_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 1, 1, 2),
    _DlswDirMacMac_Type()
)
dlswDirMacMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirMacMac.setStatus("current")


class _DlswDirMacMask_Type(MacAddressNC):
    """Custom type dlswDirMacMask based on MacAddressNC"""
    defaultHexValue = "FFFFFFFFFFFF"


_DlswDirMacMask_Object = MibTableColumn
dlswDirMacMask = _DlswDirMacMask_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 1, 1, 3),
    _DlswDirMacMask_Type()
)
dlswDirMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirMacMask.setStatus("current")


class _DlswDirMacEntryType_Type(Integer32):
    """Custom type dlswDirMacEntryType based on Integer32"""
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


_DlswDirMacEntryType_Type.__name__ = "Integer32"
_DlswDirMacEntryType_Object = MibTableColumn
dlswDirMacEntryType = _DlswDirMacEntryType_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 1, 1, 4),
    _DlswDirMacEntryType_Type()
)
dlswDirMacEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirMacEntryType.setStatus("current")


class _DlswDirMacLocationType_Type(Integer32):
    """Custom type dlswDirMacLocationType based on Integer32"""
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


_DlswDirMacLocationType_Type.__name__ = "Integer32"
_DlswDirMacLocationType_Object = MibTableColumn
dlswDirMacLocationType = _DlswDirMacLocationType_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 1, 1, 5),
    _DlswDirMacLocationType_Type()
)
dlswDirMacLocationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirMacLocationType.setStatus("current")


class _DlswDirMacLocation_Type(RowPointer):
    """Custom type dlswDirMacLocation based on RowPointer"""
    defaultValue = (0, 0)


_DlswDirMacLocation_Object = MibTableColumn
dlswDirMacLocation = _DlswDirMacLocation_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 1, 1, 6),
    _DlswDirMacLocation_Type()
)
dlswDirMacLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirMacLocation.setStatus("current")


class _DlswDirMacStatus_Type(Integer32):
    """Custom type dlswDirMacStatus based on Integer32"""
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


_DlswDirMacStatus_Type.__name__ = "Integer32"
_DlswDirMacStatus_Object = MibTableColumn
dlswDirMacStatus = _DlswDirMacStatus_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 1, 1, 7),
    _DlswDirMacStatus_Type()
)
dlswDirMacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirMacStatus.setStatus("current")


class _DlswDirMacLFSize_Type(LFSize):
    """Custom type dlswDirMacLFSize based on LFSize"""


_DlswDirMacLFSize_Object = MibTableColumn
dlswDirMacLFSize = _DlswDirMacLFSize_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 1, 1, 8),
    _DlswDirMacLFSize_Type()
)
dlswDirMacLFSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirMacLFSize.setStatus("current")
_DlswDirMacRowStatus_Type = RowStatus
_DlswDirMacRowStatus_Object = MibTableColumn
dlswDirMacRowStatus = _DlswDirMacRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 1, 1, 9),
    _DlswDirMacRowStatus_Type()
)
dlswDirMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirMacRowStatus.setStatus("current")
_DlswDirNBTable_Object = MibTable
dlswDirNBTable = _DlswDirNBTable_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    dlswDirNBTable.setStatus("current")
_DlswDirNBEntry_Object = MibTableRow
dlswDirNBEntry = _DlswDirNBEntry_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 2, 1)
)
dlswDirNBEntry.setIndexNames(
    (0, "DLSW-MIB", "dlswDirNBIndex"),
)
if mibBuilder.loadTexts:
    dlswDirNBEntry.setStatus("current")


class _DlswDirNBIndex_Type(Integer32):
    """Custom type dlswDirNBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlswDirNBIndex_Type.__name__ = "Integer32"
_DlswDirNBIndex_Object = MibTableColumn
dlswDirNBIndex = _DlswDirNBIndex_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 2, 1, 1),
    _DlswDirNBIndex_Type()
)
dlswDirNBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswDirNBIndex.setStatus("current")
_DlswDirNBName_Type = NBName
_DlswDirNBName_Object = MibTableColumn
dlswDirNBName = _DlswDirNBName_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 2, 1, 2),
    _DlswDirNBName_Type()
)
dlswDirNBName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirNBName.setStatus("current")


class _DlswDirNBNameType_Type(Integer32):
    """Custom type dlswDirNBNameType based on Integer32"""
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


_DlswDirNBNameType_Type.__name__ = "Integer32"
_DlswDirNBNameType_Object = MibTableColumn
dlswDirNBNameType = _DlswDirNBNameType_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 2, 1, 3),
    _DlswDirNBNameType_Type()
)
dlswDirNBNameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirNBNameType.setStatus("current")


class _DlswDirNBEntryType_Type(Integer32):
    """Custom type dlswDirNBEntryType based on Integer32"""
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


_DlswDirNBEntryType_Type.__name__ = "Integer32"
_DlswDirNBEntryType_Object = MibTableColumn
dlswDirNBEntryType = _DlswDirNBEntryType_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 2, 1, 4),
    _DlswDirNBEntryType_Type()
)
dlswDirNBEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirNBEntryType.setStatus("current")


class _DlswDirNBLocationType_Type(Integer32):
    """Custom type dlswDirNBLocationType based on Integer32"""
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


_DlswDirNBLocationType_Type.__name__ = "Integer32"
_DlswDirNBLocationType_Object = MibTableColumn
dlswDirNBLocationType = _DlswDirNBLocationType_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 2, 1, 5),
    _DlswDirNBLocationType_Type()
)
dlswDirNBLocationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirNBLocationType.setStatus("current")


class _DlswDirNBLocation_Type(RowPointer):
    """Custom type dlswDirNBLocation based on RowPointer"""
    defaultValue = (0, 0)


_DlswDirNBLocation_Object = MibTableColumn
dlswDirNBLocation = _DlswDirNBLocation_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 2, 1, 6),
    _DlswDirNBLocation_Type()
)
dlswDirNBLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirNBLocation.setStatus("current")


class _DlswDirNBStatus_Type(Integer32):
    """Custom type dlswDirNBStatus based on Integer32"""
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


_DlswDirNBStatus_Type.__name__ = "Integer32"
_DlswDirNBStatus_Object = MibTableColumn
dlswDirNBStatus = _DlswDirNBStatus_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 2, 1, 7),
    _DlswDirNBStatus_Type()
)
dlswDirNBStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirNBStatus.setStatus("current")


class _DlswDirNBLFSize_Type(LFSize):
    """Custom type dlswDirNBLFSize based on LFSize"""


_DlswDirNBLFSize_Object = MibTableColumn
dlswDirNBLFSize = _DlswDirNBLFSize_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 2, 1, 8),
    _DlswDirNBLFSize_Type()
)
dlswDirNBLFSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirNBLFSize.setStatus("current")
_DlswDirNBRowStatus_Type = RowStatus
_DlswDirNBRowStatus_Object = MibTableColumn
dlswDirNBRowStatus = _DlswDirNBRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 2, 2, 1, 9),
    _DlswDirNBRowStatus_Type()
)
dlswDirNBRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswDirNBRowStatus.setStatus("current")
_DlswDirLocate_ObjectIdentity = ObjectIdentity
dlswDirLocate = _DlswDirLocate_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 3)
)
_DlswDirLocateMacTable_Object = MibTable
dlswDirLocateMacTable = _DlswDirLocateMacTable_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    dlswDirLocateMacTable.setStatus("current")
_DlswDirLocateMacEntry_Object = MibTableRow
dlswDirLocateMacEntry = _DlswDirLocateMacEntry_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 3, 1, 1)
)
dlswDirLocateMacEntry.setIndexNames(
    (0, "DLSW-MIB", "dlswDirLocateMacMac"),
    (0, "DLSW-MIB", "dlswDirLocateMacMatch"),
)
if mibBuilder.loadTexts:
    dlswDirLocateMacEntry.setStatus("current")
_DlswDirLocateMacMac_Type = MacAddressNC
_DlswDirLocateMacMac_Object = MibTableColumn
dlswDirLocateMacMac = _DlswDirLocateMacMac_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 3, 1, 1, 1),
    _DlswDirLocateMacMac_Type()
)
dlswDirLocateMacMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswDirLocateMacMac.setStatus("current")


class _DlswDirLocateMacMatch_Type(Integer32):
    """Custom type dlswDirLocateMacMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DlswDirLocateMacMatch_Type.__name__ = "Integer32"
_DlswDirLocateMacMatch_Object = MibTableColumn
dlswDirLocateMacMatch = _DlswDirLocateMacMatch_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 3, 1, 1, 2),
    _DlswDirLocateMacMatch_Type()
)
dlswDirLocateMacMatch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswDirLocateMacMatch.setStatus("current")
_DlswDirLocateMacLocation_Type = RowPointer
_DlswDirLocateMacLocation_Object = MibTableColumn
dlswDirLocateMacLocation = _DlswDirLocateMacLocation_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 3, 1, 1, 3),
    _DlswDirLocateMacLocation_Type()
)
dlswDirLocateMacLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirLocateMacLocation.setStatus("current")
_DlswDirLocateNBTable_Object = MibTable
dlswDirLocateNBTable = _DlswDirLocateNBTable_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    dlswDirLocateNBTable.setStatus("current")
_DlswDirLocateNBEntry_Object = MibTableRow
dlswDirLocateNBEntry = _DlswDirLocateNBEntry_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 3, 2, 1)
)
dlswDirLocateNBEntry.setIndexNames(
    (0, "DLSW-MIB", "dlswDirLocateNBName"),
    (0, "DLSW-MIB", "dlswDirLocateNBMatch"),
)
if mibBuilder.loadTexts:
    dlswDirLocateNBEntry.setStatus("current")
_DlswDirLocateNBName_Type = NBName
_DlswDirLocateNBName_Object = MibTableColumn
dlswDirLocateNBName = _DlswDirLocateNBName_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 3, 2, 1, 1),
    _DlswDirLocateNBName_Type()
)
dlswDirLocateNBName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswDirLocateNBName.setStatus("current")


class _DlswDirLocateNBMatch_Type(Integer32):
    """Custom type dlswDirLocateNBMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DlswDirLocateNBMatch_Type.__name__ = "Integer32"
_DlswDirLocateNBMatch_Object = MibTableColumn
dlswDirLocateNBMatch = _DlswDirLocateNBMatch_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 3, 2, 1, 2),
    _DlswDirLocateNBMatch_Type()
)
dlswDirLocateNBMatch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswDirLocateNBMatch.setStatus("current")
_DlswDirLocateNBLocation_Type = RowPointer
_DlswDirLocateNBLocation_Object = MibTableColumn
dlswDirLocateNBLocation = _DlswDirLocateNBLocation_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 4, 3, 2, 1, 3),
    _DlswDirLocateNBLocation_Type()
)
dlswDirLocateNBLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswDirLocateNBLocation.setStatus("current")
_DlswCircuit_ObjectIdentity = ObjectIdentity
dlswCircuit = _DlswCircuit_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 5)
)
_DlswCircuitStat_ObjectIdentity = ObjectIdentity
dlswCircuitStat = _DlswCircuitStat_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 1)
)
_DlswCircuitStatActives_Type = Gauge32
_DlswCircuitStatActives_Object = MibScalar
dlswCircuitStatActives = _DlswCircuitStatActives_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 1, 1),
    _DlswCircuitStatActives_Type()
)
dlswCircuitStatActives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitStatActives.setStatus("current")
_DlswCircuitStatCreates_Type = Counter32
_DlswCircuitStatCreates_Object = MibScalar
dlswCircuitStatCreates = _DlswCircuitStatCreates_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 1, 2),
    _DlswCircuitStatCreates_Type()
)
dlswCircuitStatCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitStatCreates.setStatus("current")
_DlswCircuitTable_Object = MibTable
dlswCircuitTable = _DlswCircuitTable_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2)
)
if mibBuilder.loadTexts:
    dlswCircuitTable.setStatus("current")
_DlswCircuitEntry_Object = MibTableRow
dlswCircuitEntry = _DlswCircuitEntry_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1)
)
dlswCircuitEntry.setIndexNames(
    (0, "DLSW-MIB", "dlswCircuitS1Mac"),
    (0, "DLSW-MIB", "dlswCircuitS1Sap"),
    (0, "DLSW-MIB", "dlswCircuitS2Mac"),
    (0, "DLSW-MIB", "dlswCircuitS2Sap"),
)
if mibBuilder.loadTexts:
    dlswCircuitEntry.setStatus("current")
_DlswCircuitS1Mac_Type = MacAddressNC
_DlswCircuitS1Mac_Object = MibTableColumn
dlswCircuitS1Mac = _DlswCircuitS1Mac_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 1),
    _DlswCircuitS1Mac_Type()
)
dlswCircuitS1Mac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswCircuitS1Mac.setStatus("current")


class _DlswCircuitS1Sap_Type(OctetString):
    """Custom type dlswCircuitS1Sap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DlswCircuitS1Sap_Type.__name__ = "OctetString"
_DlswCircuitS1Sap_Object = MibTableColumn
dlswCircuitS1Sap = _DlswCircuitS1Sap_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 2),
    _DlswCircuitS1Sap_Type()
)
dlswCircuitS1Sap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswCircuitS1Sap.setStatus("current")


class _DlswCircuitS1IfIndex_Type(Integer32):
    """Custom type dlswCircuitS1IfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlswCircuitS1IfIndex_Type.__name__ = "Integer32"
_DlswCircuitS1IfIndex_Object = MibTableColumn
dlswCircuitS1IfIndex = _DlswCircuitS1IfIndex_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 3),
    _DlswCircuitS1IfIndex_Type()
)
dlswCircuitS1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1IfIndex.setStatus("current")
_DlswCircuitS1DlcType_Type = DlcType
_DlswCircuitS1DlcType_Object = MibTableColumn
dlswCircuitS1DlcType = _DlswCircuitS1DlcType_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 4),
    _DlswCircuitS1DlcType_Type()
)
dlswCircuitS1DlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1DlcType.setStatus("current")


class _DlswCircuitS1RouteInfo_Type(OctetString):
    """Custom type dlswCircuitS1RouteInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DlswCircuitS1RouteInfo_Type.__name__ = "OctetString"
_DlswCircuitS1RouteInfo_Object = MibTableColumn
dlswCircuitS1RouteInfo = _DlswCircuitS1RouteInfo_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 5),
    _DlswCircuitS1RouteInfo_Type()
)
dlswCircuitS1RouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1RouteInfo.setStatus("current")


class _DlswCircuitS1CircuitId_Type(OctetString):
    """Custom type dlswCircuitS1CircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_DlswCircuitS1CircuitId_Type.__name__ = "OctetString"
_DlswCircuitS1CircuitId_Object = MibTableColumn
dlswCircuitS1CircuitId = _DlswCircuitS1CircuitId_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 6),
    _DlswCircuitS1CircuitId_Type()
)
dlswCircuitS1CircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1CircuitId.setStatus("current")
_DlswCircuitS1Dlc_Type = RowPointer
_DlswCircuitS1Dlc_Object = MibTableColumn
dlswCircuitS1Dlc = _DlswCircuitS1Dlc_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 7),
    _DlswCircuitS1Dlc_Type()
)
dlswCircuitS1Dlc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1Dlc.setStatus("current")
_DlswCircuitS2Mac_Type = MacAddressNC
_DlswCircuitS2Mac_Object = MibTableColumn
dlswCircuitS2Mac = _DlswCircuitS2Mac_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 8),
    _DlswCircuitS2Mac_Type()
)
dlswCircuitS2Mac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswCircuitS2Mac.setStatus("current")


class _DlswCircuitS2Sap_Type(OctetString):
    """Custom type dlswCircuitS2Sap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DlswCircuitS2Sap_Type.__name__ = "OctetString"
_DlswCircuitS2Sap_Object = MibTableColumn
dlswCircuitS2Sap = _DlswCircuitS2Sap_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 9),
    _DlswCircuitS2Sap_Type()
)
dlswCircuitS2Sap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswCircuitS2Sap.setStatus("current")
_DlswCircuitS2Location_Type = EndStationLocation
_DlswCircuitS2Location_Object = MibTableColumn
dlswCircuitS2Location = _DlswCircuitS2Location_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 10),
    _DlswCircuitS2Location_Type()
)
dlswCircuitS2Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2Location.setStatus("current")
_DlswCircuitS2TDomain_Type = ObjectIdentifier
_DlswCircuitS2TDomain_Object = MibTableColumn
dlswCircuitS2TDomain = _DlswCircuitS2TDomain_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 11),
    _DlswCircuitS2TDomain_Type()
)
dlswCircuitS2TDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2TDomain.setStatus("current")
_DlswCircuitS2TAddress_Type = TAddress
_DlswCircuitS2TAddress_Object = MibTableColumn
dlswCircuitS2TAddress = _DlswCircuitS2TAddress_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 12),
    _DlswCircuitS2TAddress_Type()
)
dlswCircuitS2TAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2TAddress.setStatus("current")


class _DlswCircuitS2CircuitId_Type(OctetString):
    """Custom type dlswCircuitS2CircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_DlswCircuitS2CircuitId_Type.__name__ = "OctetString"
_DlswCircuitS2CircuitId_Object = MibTableColumn
dlswCircuitS2CircuitId = _DlswCircuitS2CircuitId_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 13),
    _DlswCircuitS2CircuitId_Type()
)
dlswCircuitS2CircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2CircuitId.setStatus("current")


class _DlswCircuitOrigin_Type(Integer32):
    """Custom type dlswCircuitOrigin based on Integer32"""
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


_DlswCircuitOrigin_Type.__name__ = "Integer32"
_DlswCircuitOrigin_Object = MibTableColumn
dlswCircuitOrigin = _DlswCircuitOrigin_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 14),
    _DlswCircuitOrigin_Type()
)
dlswCircuitOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitOrigin.setStatus("current")
_DlswCircuitEntryTime_Type = TimeTicks
_DlswCircuitEntryTime_Object = MibTableColumn
dlswCircuitEntryTime = _DlswCircuitEntryTime_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 15),
    _DlswCircuitEntryTime_Type()
)
dlswCircuitEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitEntryTime.setStatus("current")
if mibBuilder.loadTexts:
    dlswCircuitEntryTime.setUnits("hundredths of a second")
_DlswCircuitStateTime_Type = TimeTicks
_DlswCircuitStateTime_Object = MibTableColumn
dlswCircuitStateTime = _DlswCircuitStateTime_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 16),
    _DlswCircuitStateTime_Type()
)
dlswCircuitStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitStateTime.setStatus("current")
if mibBuilder.loadTexts:
    dlswCircuitStateTime.setUnits("hundredths of a second")


class _DlswCircuitState_Type(Integer32):
    """Custom type dlswCircuitState based on Integer32"""
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


_DlswCircuitState_Type.__name__ = "Integer32"
_DlswCircuitState_Object = MibTableColumn
dlswCircuitState = _DlswCircuitState_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 17),
    _DlswCircuitState_Type()
)
dlswCircuitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswCircuitState.setStatus("current")


class _DlswCircuitPriority_Type(Integer32):
    """Custom type dlswCircuitPriority based on Integer32"""
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
        *(("high", 4),
          ("highest", 5),
          ("low", 2),
          ("medium", 3),
          ("unsupported", 1))
    )


_DlswCircuitPriority_Type.__name__ = "Integer32"
_DlswCircuitPriority_Object = MibTableColumn
dlswCircuitPriority = _DlswCircuitPriority_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 18),
    _DlswCircuitPriority_Type()
)
dlswCircuitPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitPriority.setStatus("current")


class _DlswCircuitFCSendGrantedUnits_Type(Integer32):
    """Custom type dlswCircuitFCSendGrantedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswCircuitFCSendGrantedUnits_Type.__name__ = "Integer32"
_DlswCircuitFCSendGrantedUnits_Object = MibTableColumn
dlswCircuitFCSendGrantedUnits = _DlswCircuitFCSendGrantedUnits_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 19),
    _DlswCircuitFCSendGrantedUnits_Type()
)
dlswCircuitFCSendGrantedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCSendGrantedUnits.setStatus("current")


class _DlswCircuitFCSendCurrentWndw_Type(Integer32):
    """Custom type dlswCircuitFCSendCurrentWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswCircuitFCSendCurrentWndw_Type.__name__ = "Integer32"
_DlswCircuitFCSendCurrentWndw_Object = MibTableColumn
dlswCircuitFCSendCurrentWndw = _DlswCircuitFCSendCurrentWndw_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 20),
    _DlswCircuitFCSendCurrentWndw_Type()
)
dlswCircuitFCSendCurrentWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCSendCurrentWndw.setStatus("current")


class _DlswCircuitFCRecvGrantedUnits_Type(Integer32):
    """Custom type dlswCircuitFCRecvGrantedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswCircuitFCRecvGrantedUnits_Type.__name__ = "Integer32"
_DlswCircuitFCRecvGrantedUnits_Object = MibTableColumn
dlswCircuitFCRecvGrantedUnits = _DlswCircuitFCRecvGrantedUnits_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 21),
    _DlswCircuitFCRecvGrantedUnits_Type()
)
dlswCircuitFCRecvGrantedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCRecvGrantedUnits.setStatus("current")


class _DlswCircuitFCRecvCurrentWndw_Type(Integer32):
    """Custom type dlswCircuitFCRecvCurrentWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswCircuitFCRecvCurrentWndw_Type.__name__ = "Integer32"
_DlswCircuitFCRecvCurrentWndw_Object = MibTableColumn
dlswCircuitFCRecvCurrentWndw = _DlswCircuitFCRecvCurrentWndw_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 22),
    _DlswCircuitFCRecvCurrentWndw_Type()
)
dlswCircuitFCRecvCurrentWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCRecvCurrentWndw.setStatus("current")
_DlswCircuitFCLargestRecvGranted_Type = Gauge32
_DlswCircuitFCLargestRecvGranted_Object = MibTableColumn
dlswCircuitFCLargestRecvGranted = _DlswCircuitFCLargestRecvGranted_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 23),
    _DlswCircuitFCLargestRecvGranted_Type()
)
dlswCircuitFCLargestRecvGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCLargestRecvGranted.setStatus("current")
_DlswCircuitFCLargestSendGranted_Type = Gauge32
_DlswCircuitFCLargestSendGranted_Object = MibTableColumn
dlswCircuitFCLargestSendGranted = _DlswCircuitFCLargestSendGranted_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 24),
    _DlswCircuitFCLargestSendGranted_Type()
)
dlswCircuitFCLargestSendGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCLargestSendGranted.setStatus("current")
_DlswCircuitFCHalveWndwSents_Type = Counter32
_DlswCircuitFCHalveWndwSents_Object = MibTableColumn
dlswCircuitFCHalveWndwSents = _DlswCircuitFCHalveWndwSents_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 25),
    _DlswCircuitFCHalveWndwSents_Type()
)
dlswCircuitFCHalveWndwSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCHalveWndwSents.setStatus("current")
_DlswCircuitFCResetOpSents_Type = Counter32
_DlswCircuitFCResetOpSents_Object = MibTableColumn
dlswCircuitFCResetOpSents = _DlswCircuitFCResetOpSents_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 26),
    _DlswCircuitFCResetOpSents_Type()
)
dlswCircuitFCResetOpSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCResetOpSents.setStatus("current")
_DlswCircuitFCHalveWndwRcvds_Type = Counter32
_DlswCircuitFCHalveWndwRcvds_Object = MibTableColumn
dlswCircuitFCHalveWndwRcvds = _DlswCircuitFCHalveWndwRcvds_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 27),
    _DlswCircuitFCHalveWndwRcvds_Type()
)
dlswCircuitFCHalveWndwRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCHalveWndwRcvds.setStatus("current")
_DlswCircuitFCResetOpRcvds_Type = Counter32
_DlswCircuitFCResetOpRcvds_Object = MibTableColumn
dlswCircuitFCResetOpRcvds = _DlswCircuitFCResetOpRcvds_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 28),
    _DlswCircuitFCResetOpRcvds_Type()
)
dlswCircuitFCResetOpRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCResetOpRcvds.setStatus("current")


class _DlswCircuitDiscReasonLocal_Type(Integer32):
    """Custom type dlswCircuitDiscReasonLocal based on Integer32"""
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


_DlswCircuitDiscReasonLocal_Type.__name__ = "Integer32"
_DlswCircuitDiscReasonLocal_Object = MibTableColumn
dlswCircuitDiscReasonLocal = _DlswCircuitDiscReasonLocal_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 29),
    _DlswCircuitDiscReasonLocal_Type()
)
dlswCircuitDiscReasonLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitDiscReasonLocal.setStatus("current")


class _DlswCircuitDiscReasonRemote_Type(Integer32):
    """Custom type dlswCircuitDiscReasonRemote based on Integer32"""
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
        *(("endStationDiscRcvd", 2),
          ("endStationDlcError", 3),
          ("operatorCommand", 5),
          ("protocolError", 4),
          ("unknown", 1))
    )


_DlswCircuitDiscReasonRemote_Type.__name__ = "Integer32"
_DlswCircuitDiscReasonRemote_Object = MibTableColumn
dlswCircuitDiscReasonRemote = _DlswCircuitDiscReasonRemote_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 30),
    _DlswCircuitDiscReasonRemote_Type()
)
dlswCircuitDiscReasonRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitDiscReasonRemote.setStatus("current")


class _DlswCircuitDiscReasonRemoteData_Type(OctetString):
    """Custom type dlswCircuitDiscReasonRemoteData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_DlswCircuitDiscReasonRemoteData_Type.__name__ = "OctetString"
_DlswCircuitDiscReasonRemoteData_Object = MibTableColumn
dlswCircuitDiscReasonRemoteData = _DlswCircuitDiscReasonRemoteData_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 5, 2, 1, 31),
    _DlswCircuitDiscReasonRemoteData_Type()
)
dlswCircuitDiscReasonRemoteData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitDiscReasonRemoteData.setStatus("current")
_DlswSdlc_ObjectIdentity = ObjectIdentity
dlswSdlc = _DlswSdlc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 1, 6)
)
_DlswSdlcLsEntries_Type = Gauge32
_DlswSdlcLsEntries_Object = MibScalar
dlswSdlcLsEntries = _DlswSdlcLsEntries_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 6, 1),
    _DlswSdlcLsEntries_Type()
)
dlswSdlcLsEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswSdlcLsEntries.setStatus("current")
_DlswSdlcLsTable_Object = MibTable
dlswSdlcLsTable = _DlswSdlcLsTable_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 6, 2)
)
if mibBuilder.loadTexts:
    dlswSdlcLsTable.setStatus("current")
_DlswSdlcLsEntry_Object = MibTableRow
dlswSdlcLsEntry = _DlswSdlcLsEntry_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 6, 2, 1)
)
dlswSdlcLsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SNA-SDLC-MIB", "sdlcLSAddress"),
)
if mibBuilder.loadTexts:
    dlswSdlcLsEntry.setStatus("current")
_DlswSdlcLsLocalMac_Type = MacAddressNC
_DlswSdlcLsLocalMac_Object = MibTableColumn
dlswSdlcLsLocalMac = _DlswSdlcLsLocalMac_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 6, 2, 1, 1),
    _DlswSdlcLsLocalMac_Type()
)
dlswSdlcLsLocalMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswSdlcLsLocalMac.setStatus("current")


class _DlswSdlcLsLocalSap_Type(OctetString):
    """Custom type dlswSdlcLsLocalSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DlswSdlcLsLocalSap_Type.__name__ = "OctetString"
_DlswSdlcLsLocalSap_Object = MibTableColumn
dlswSdlcLsLocalSap = _DlswSdlcLsLocalSap_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 6, 2, 1, 2),
    _DlswSdlcLsLocalSap_Type()
)
dlswSdlcLsLocalSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswSdlcLsLocalSap.setStatus("current")


class _DlswSdlcLsLocalIdBlock_Type(DisplayString):
    """Custom type dlswSdlcLsLocalIdBlock based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 3),
    )


_DlswSdlcLsLocalIdBlock_Type.__name__ = "DisplayString"
_DlswSdlcLsLocalIdBlock_Object = MibTableColumn
dlswSdlcLsLocalIdBlock = _DlswSdlcLsLocalIdBlock_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 6, 2, 1, 3),
    _DlswSdlcLsLocalIdBlock_Type()
)
dlswSdlcLsLocalIdBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswSdlcLsLocalIdBlock.setStatus("current")


class _DlswSdlcLsLocalIdNum_Type(DisplayString):
    """Custom type dlswSdlcLsLocalIdNum based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
    )


_DlswSdlcLsLocalIdNum_Type.__name__ = "DisplayString"
_DlswSdlcLsLocalIdNum_Object = MibTableColumn
dlswSdlcLsLocalIdNum = _DlswSdlcLsLocalIdNum_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 6, 2, 1, 4),
    _DlswSdlcLsLocalIdNum_Type()
)
dlswSdlcLsLocalIdNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswSdlcLsLocalIdNum.setStatus("current")


class _DlswSdlcLsRemoteMac_Type(MacAddressNC):
    """Custom type dlswSdlcLsRemoteMac based on MacAddressNC"""
    defaultHexValue = ""


_DlswSdlcLsRemoteMac_Object = MibTableColumn
dlswSdlcLsRemoteMac = _DlswSdlcLsRemoteMac_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 6, 2, 1, 5),
    _DlswSdlcLsRemoteMac_Type()
)
dlswSdlcLsRemoteMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswSdlcLsRemoteMac.setStatus("current")


class _DlswSdlcLsRemoteSap_Type(OctetString):
    """Custom type dlswSdlcLsRemoteSap based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
    )


_DlswSdlcLsRemoteSap_Type.__name__ = "OctetString"
_DlswSdlcLsRemoteSap_Object = MibTableColumn
dlswSdlcLsRemoteSap = _DlswSdlcLsRemoteSap_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 6, 2, 1, 6),
    _DlswSdlcLsRemoteSap_Type()
)
dlswSdlcLsRemoteSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswSdlcLsRemoteSap.setStatus("current")
_DlswSdlcLsRowStatus_Type = RowStatus
_DlswSdlcLsRowStatus_Object = MibTableColumn
dlswSdlcLsRowStatus = _DlswSdlcLsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 46, 1, 6, 2, 1, 7),
    _DlswSdlcLsRowStatus_Type()
)
dlswSdlcLsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dlswSdlcLsRowStatus.setStatus("current")
_DlswDomains_ObjectIdentity = ObjectIdentity
dlswDomains = _DlswDomains_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 2)
)
_DlswTCPDomain_ObjectIdentity = ObjectIdentity
dlswTCPDomain = _DlswTCPDomain_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 2, 1)
)
_DlswConformance_ObjectIdentity = ObjectIdentity
dlswConformance = _DlswConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 3)
)
_DlswCompliances_ObjectIdentity = ObjectIdentity
dlswCompliances = _DlswCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 3, 1)
)
_DlswGroups_ObjectIdentity = ObjectIdentity
dlswGroups = _DlswGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 46, 3, 2)
)

# Managed Objects groups

dlswNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 1)
)
dlswNodeGroup.setObjects(
      *(("DLSW-MIB", "dlswNodeVersion"),
        ("DLSW-MIB", "dlswNodeVendorID"),
        ("DLSW-MIB", "dlswNodeVersionString"),
        ("DLSW-MIB", "dlswNodeStdPacingSupport"),
        ("DLSW-MIB", "dlswNodeStatus"),
        ("DLSW-MIB", "dlswNodeUpTime"),
        ("DLSW-MIB", "dlswNodeVirtualSegmentLFSize"),
        ("DLSW-MIB", "dlswNodeResourceMacExclusivity"),
        ("DLSW-MIB", "dlswTrapCntlTConnPartnerReject"),
        ("DLSW-MIB", "dlswTrapCntlTConnProtViolation"),
        ("DLSW-MIB", "dlswTrapCntlTConn"),
        ("DLSW-MIB", "dlswTrapCntlCircuit"))
)
if mibBuilder.loadTexts:
    dlswNodeGroup.setStatus("current")

dlswNodeNBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 2)
)
dlswNodeNBGroup.setObjects(
    ("DLSW-MIB", "dlswNodeResourceNBExclusivity")
)
if mibBuilder.loadTexts:
    dlswNodeNBGroup.setStatus("current")

dlswTConnStatGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 3)
)
dlswTConnStatGroup.setObjects(
      *(("DLSW-MIB", "dlswTConnStatActiveConnections"),
        ("DLSW-MIB", "dlswTConnStatCloseIdles"),
        ("DLSW-MIB", "dlswTConnStatCloseBusys"))
)
if mibBuilder.loadTexts:
    dlswTConnStatGroup.setStatus("current")

dlswTConnConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 4)
)
dlswTConnConfigGroup.setObjects(
      *(("DLSW-MIB", "dlswTConnConfigTDomain"),
        ("DLSW-MIB", "dlswTConnConfigLocalTAddr"),
        ("DLSW-MIB", "dlswTConnConfigRemoteTAddr"),
        ("DLSW-MIB", "dlswTConnConfigLastModifyTime"),
        ("DLSW-MIB", "dlswTConnConfigEntryType"),
        ("DLSW-MIB", "dlswTConnConfigGroupDefinition"),
        ("DLSW-MIB", "dlswTConnConfigSetupType"),
        ("DLSW-MIB", "dlswTConnConfigSapList"),
        ("DLSW-MIB", "dlswTConnConfigAdvertiseMacNB"),
        ("DLSW-MIB", "dlswTConnConfigInitCirRecvWndw"),
        ("DLSW-MIB", "dlswTConnConfigOpens"),
        ("DLSW-MIB", "dlswTConnConfigRowStatus"))
)
if mibBuilder.loadTexts:
    dlswTConnConfigGroup.setStatus("current")

dlswTConnOperGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 5)
)
dlswTConnOperGroup.setObjects(
      *(("DLSW-MIB", "dlswTConnOperLocalTAddr"),
        ("DLSW-MIB", "dlswTConnOperEntryTime"),
        ("DLSW-MIB", "dlswTConnOperConnectTime"),
        ("DLSW-MIB", "dlswTConnOperState"),
        ("DLSW-MIB", "dlswTConnOperConfigIndex"),
        ("DLSW-MIB", "dlswTConnOperFlowCntlMode"),
        ("DLSW-MIB", "dlswTConnOperPartnerVersion"),
        ("DLSW-MIB", "dlswTConnOperPartnerVendorID"),
        ("DLSW-MIB", "dlswTConnOperPartnerVersionStr"),
        ("DLSW-MIB", "dlswTConnOperPartnerInitPacingWndw"),
        ("DLSW-MIB", "dlswTConnOperPartnerSapList"),
        ("DLSW-MIB", "dlswTConnOperPartnerMacExcl"),
        ("DLSW-MIB", "dlswTConnOperPartnerMacInfo"),
        ("DLSW-MIB", "dlswTConnOperDiscTime"),
        ("DLSW-MIB", "dlswTConnOperDiscReason"),
        ("DLSW-MIB", "dlswTConnOperDiscActiveCir"),
        ("DLSW-MIB", "dlswTConnOperInDataPkts"),
        ("DLSW-MIB", "dlswTConnOperOutDataPkts"),
        ("DLSW-MIB", "dlswTConnOperInDataOctets"),
        ("DLSW-MIB", "dlswTConnOperOutDataOctets"),
        ("DLSW-MIB", "dlswTConnOperInCntlPkts"),
        ("DLSW-MIB", "dlswTConnOperOutCntlPkts"),
        ("DLSW-MIB", "dlswTConnOperCURexSents"),
        ("DLSW-MIB", "dlswTConnOperICRexRcvds"),
        ("DLSW-MIB", "dlswTConnOperCURexRcvds"),
        ("DLSW-MIB", "dlswTConnOperICRexSents"),
        ("DLSW-MIB", "dlswTConnOperCirCreates"),
        ("DLSW-MIB", "dlswTConnOperCircuits"))
)
if mibBuilder.loadTexts:
    dlswTConnOperGroup.setStatus("current")

dlswTConnNBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 6)
)
dlswTConnNBGroup.setObjects(
      *(("DLSW-MIB", "dlswTConnOperPartnerNBExcl"),
        ("DLSW-MIB", "dlswTConnOperPartnerNBInfo"),
        ("DLSW-MIB", "dlswTConnOperNQexSents"),
        ("DLSW-MIB", "dlswTConnOperNRexRcvds"),
        ("DLSW-MIB", "dlswTConnOperNQexRcvds"),
        ("DLSW-MIB", "dlswTConnOperNRexSents"))
)
if mibBuilder.loadTexts:
    dlswTConnNBGroup.setStatus("current")

dlswTConnTcpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 7)
)
dlswTConnTcpConfigGroup.setObjects(
      *(("DLSW-MIB", "dlswTConnTcpConfigKeepAliveInt"),
        ("DLSW-MIB", "dlswTConnTcpConfigTcpConnections"),
        ("DLSW-MIB", "dlswTConnTcpConfigMaxSegmentSize"))
)
if mibBuilder.loadTexts:
    dlswTConnTcpConfigGroup.setStatus("current")

dlswTConnTcpOperGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 8)
)
dlswTConnTcpOperGroup.setObjects(
      *(("DLSW-MIB", "dlswTConnTcpOperKeepAliveInt"),
        ("DLSW-MIB", "dlswTConnTcpOperPrefTcpConnections"),
        ("DLSW-MIB", "dlswTConnTcpOperTcpConnections"))
)
if mibBuilder.loadTexts:
    dlswTConnTcpOperGroup.setStatus("current")

dlswInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 9)
)
dlswInterfaceGroup.setObjects(
      *(("DLSW-MIB", "dlswIfRowStatus"),
        ("DLSW-MIB", "dlswIfVirtualSegment"),
        ("DLSW-MIB", "dlswIfSapList"))
)
if mibBuilder.loadTexts:
    dlswInterfaceGroup.setStatus("current")

dlswDirGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 10)
)
dlswDirGroup.setObjects(
      *(("DLSW-MIB", "dlswDirMacEntries"),
        ("DLSW-MIB", "dlswDirMacCacheHits"),
        ("DLSW-MIB", "dlswDirMacCacheMisses"),
        ("DLSW-MIB", "dlswDirMacCacheNextIndex"),
        ("DLSW-MIB", "dlswDirMacMac"),
        ("DLSW-MIB", "dlswDirMacMask"),
        ("DLSW-MIB", "dlswDirMacEntryType"),
        ("DLSW-MIB", "dlswDirMacLocationType"),
        ("DLSW-MIB", "dlswDirMacLocation"),
        ("DLSW-MIB", "dlswDirMacStatus"),
        ("DLSW-MIB", "dlswDirMacLFSize"),
        ("DLSW-MIB", "dlswDirMacRowStatus"))
)
if mibBuilder.loadTexts:
    dlswDirGroup.setStatus("current")

dlswDirNBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 11)
)
dlswDirNBGroup.setObjects(
      *(("DLSW-MIB", "dlswDirNBEntries"),
        ("DLSW-MIB", "dlswDirNBCacheHits"),
        ("DLSW-MIB", "dlswDirNBCacheMisses"),
        ("DLSW-MIB", "dlswDirNBCacheNextIndex"),
        ("DLSW-MIB", "dlswDirNBName"),
        ("DLSW-MIB", "dlswDirNBNameType"),
        ("DLSW-MIB", "dlswDirNBEntryType"),
        ("DLSW-MIB", "dlswDirNBLocationType"),
        ("DLSW-MIB", "dlswDirNBLocation"),
        ("DLSW-MIB", "dlswDirNBStatus"),
        ("DLSW-MIB", "dlswDirNBLFSize"),
        ("DLSW-MIB", "dlswDirNBRowStatus"))
)
if mibBuilder.loadTexts:
    dlswDirNBGroup.setStatus("current")

dlswDirLocateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 12)
)
dlswDirLocateGroup.setObjects(
    ("DLSW-MIB", "dlswDirLocateMacLocation")
)
if mibBuilder.loadTexts:
    dlswDirLocateGroup.setStatus("current")

dlswDirLocateNBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 13)
)
dlswDirLocateNBGroup.setObjects(
    ("DLSW-MIB", "dlswDirLocateNBLocation")
)
if mibBuilder.loadTexts:
    dlswDirLocateNBGroup.setStatus("current")

dlswCircuitStatGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 14)
)
dlswCircuitStatGroup.setObjects(
      *(("DLSW-MIB", "dlswCircuitStatActives"),
        ("DLSW-MIB", "dlswCircuitStatCreates"))
)
if mibBuilder.loadTexts:
    dlswCircuitStatGroup.setStatus("current")

dlswCircuitGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 15)
)
dlswCircuitGroup.setObjects(
      *(("DLSW-MIB", "dlswCircuitS1IfIndex"),
        ("DLSW-MIB", "dlswCircuitS1DlcType"),
        ("DLSW-MIB", "dlswCircuitS1RouteInfo"),
        ("DLSW-MIB", "dlswCircuitS1CircuitId"),
        ("DLSW-MIB", "dlswCircuitS1Dlc"),
        ("DLSW-MIB", "dlswCircuitS2Location"),
        ("DLSW-MIB", "dlswCircuitS2TDomain"),
        ("DLSW-MIB", "dlswCircuitS2TAddress"),
        ("DLSW-MIB", "dlswCircuitS2CircuitId"),
        ("DLSW-MIB", "dlswCircuitOrigin"),
        ("DLSW-MIB", "dlswCircuitEntryTime"),
        ("DLSW-MIB", "dlswCircuitStateTime"),
        ("DLSW-MIB", "dlswCircuitState"),
        ("DLSW-MIB", "dlswCircuitPriority"),
        ("DLSW-MIB", "dlswCircuitFCSendGrantedUnits"),
        ("DLSW-MIB", "dlswCircuitFCSendCurrentWndw"),
        ("DLSW-MIB", "dlswCircuitFCRecvGrantedUnits"),
        ("DLSW-MIB", "dlswCircuitFCRecvCurrentWndw"),
        ("DLSW-MIB", "dlswCircuitFCLargestRecvGranted"),
        ("DLSW-MIB", "dlswCircuitFCLargestSendGranted"),
        ("DLSW-MIB", "dlswCircuitFCHalveWndwSents"),
        ("DLSW-MIB", "dlswCircuitFCResetOpSents"),
        ("DLSW-MIB", "dlswCircuitFCHalveWndwRcvds"),
        ("DLSW-MIB", "dlswCircuitFCResetOpRcvds"),
        ("DLSW-MIB", "dlswCircuitDiscReasonLocal"),
        ("DLSW-MIB", "dlswCircuitDiscReasonRemote"),
        ("DLSW-MIB", "dlswCircuitDiscReasonRemoteData"))
)
if mibBuilder.loadTexts:
    dlswCircuitGroup.setStatus("current")

dlswSdlcGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 16)
)
dlswSdlcGroup.setObjects(
      *(("DLSW-MIB", "dlswSdlcLsEntries"),
        ("DLSW-MIB", "dlswSdlcLsLocalMac"),
        ("DLSW-MIB", "dlswSdlcLsLocalSap"),
        ("DLSW-MIB", "dlswSdlcLsLocalIdBlock"),
        ("DLSW-MIB", "dlswSdlcLsLocalIdNum"),
        ("DLSW-MIB", "dlswSdlcLsRemoteMac"),
        ("DLSW-MIB", "dlswSdlcLsRemoteSap"),
        ("DLSW-MIB", "dlswSdlcLsRowStatus"))
)
if mibBuilder.loadTexts:
    dlswSdlcGroup.setStatus("current")


# Notification objects

dlswTrapTConnPartnerReject = NotificationType(
    (1, 3, 6, 1, 2, 1, 46, 1, 0, 1)
)
dlswTrapTConnPartnerReject.setObjects(
      *(("DLSW-MIB", "dlswTConnOperTDomain"),
        ("DLSW-MIB", "dlswTConnOperRemoteTAddr"))
)
if mibBuilder.loadTexts:
    dlswTrapTConnPartnerReject.setStatus(
        "current"
    )

dlswTrapTConnProtViolation = NotificationType(
    (1, 3, 6, 1, 2, 1, 46, 1, 0, 2)
)
dlswTrapTConnProtViolation.setObjects(
      *(("DLSW-MIB", "dlswTConnOperTDomain"),
        ("DLSW-MIB", "dlswTConnOperRemoteTAddr"))
)
if mibBuilder.loadTexts:
    dlswTrapTConnProtViolation.setStatus(
        "current"
    )

dlswTrapTConnUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 46, 1, 0, 3)
)
dlswTrapTConnUp.setObjects(
      *(("DLSW-MIB", "dlswTConnOperTDomain"),
        ("DLSW-MIB", "dlswTConnOperRemoteTAddr"))
)
if mibBuilder.loadTexts:
    dlswTrapTConnUp.setStatus(
        "current"
    )

dlswTrapTConnDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 46, 1, 0, 4)
)
dlswTrapTConnDown.setObjects(
      *(("DLSW-MIB", "dlswTConnOperTDomain"),
        ("DLSW-MIB", "dlswTConnOperRemoteTAddr"))
)
if mibBuilder.loadTexts:
    dlswTrapTConnDown.setStatus(
        "current"
    )

dlswTrapCircuitUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 46, 1, 0, 5)
)
dlswTrapCircuitUp.setObjects(
      *(("DLSW-MIB", "dlswCircuitS1Mac"),
        ("DLSW-MIB", "dlswCircuitS1Sap"),
        ("DLSW-MIB", "dlswCircuitS2Mac"),
        ("DLSW-MIB", "dlswCircuitS2Sap"))
)
if mibBuilder.loadTexts:
    dlswTrapCircuitUp.setStatus(
        "current"
    )

dlswTrapCircuitDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 46, 1, 0, 6)
)
dlswTrapCircuitDown.setObjects(
      *(("DLSW-MIB", "dlswCircuitS1Mac"),
        ("DLSW-MIB", "dlswCircuitS1Sap"),
        ("DLSW-MIB", "dlswCircuitS2Mac"),
        ("DLSW-MIB", "dlswCircuitS2Sap"))
)
if mibBuilder.loadTexts:
    dlswTrapCircuitDown.setStatus(
        "current"
    )


# Notifications groups

dlswNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 46, 3, 2, 17)
)
dlswNotificationGroup.setObjects(
      *(("DLSW-MIB", "dlswTrapTConnPartnerReject"),
        ("DLSW-MIB", "dlswTrapTConnProtViolation"),
        ("DLSW-MIB", "dlswTrapTConnUp"),
        ("DLSW-MIB", "dlswTrapTConnDown"),
        ("DLSW-MIB", "dlswTrapCircuitUp"),
        ("DLSW-MIB", "dlswTrapCircuitDown"))
)
if mibBuilder.loadTexts:
    dlswNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dlswCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 46, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dlswCoreCompliance.setStatus(
        "current"
    )

dlswTConnTcpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 46, 3, 1, 2)
)
if mibBuilder.loadTexts:
    dlswTConnTcpCompliance.setStatus(
        "current"
    )

dlswDirCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 46, 3, 1, 3)
)
if mibBuilder.loadTexts:
    dlswDirCompliance.setStatus(
        "current"
    )

dlswDirLocateCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 46, 3, 1, 4)
)
if mibBuilder.loadTexts:
    dlswDirLocateCompliance.setStatus(
        "current"
    )

dlswSdlcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 46, 3, 1, 5)
)
if mibBuilder.loadTexts:
    dlswSdlcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLSW-MIB",
    **{"NBName": NBName,
       "MacAddressNC": MacAddressNC,
       "TAddress": TAddress,
       "EndStationLocation": EndStationLocation,
       "DlcType": DlcType,
       "LFSize": LFSize,
       "DlswTCPAddress": DlswTCPAddress,
       "null": null,
       "dlsw": dlsw,
       "dlswMIB": dlswMIB,
       "dlswTraps": dlswTraps,
       "dlswTrapTConnPartnerReject": dlswTrapTConnPartnerReject,
       "dlswTrapTConnProtViolation": dlswTrapTConnProtViolation,
       "dlswTrapTConnUp": dlswTrapTConnUp,
       "dlswTrapTConnDown": dlswTrapTConnDown,
       "dlswTrapCircuitUp": dlswTrapCircuitUp,
       "dlswTrapCircuitDown": dlswTrapCircuitDown,
       "dlswNode": dlswNode,
       "dlswNodeVersion": dlswNodeVersion,
       "dlswNodeVendorID": dlswNodeVendorID,
       "dlswNodeVersionString": dlswNodeVersionString,
       "dlswNodeStdPacingSupport": dlswNodeStdPacingSupport,
       "dlswNodeStatus": dlswNodeStatus,
       "dlswNodeUpTime": dlswNodeUpTime,
       "dlswNodeVirtualSegmentLFSize": dlswNodeVirtualSegmentLFSize,
       "dlswNodeResourceNBExclusivity": dlswNodeResourceNBExclusivity,
       "dlswNodeResourceMacExclusivity": dlswNodeResourceMacExclusivity,
       "dlswTrapControl": dlswTrapControl,
       "dlswTrapCntlTConnPartnerReject": dlswTrapCntlTConnPartnerReject,
       "dlswTrapCntlTConnProtViolation": dlswTrapCntlTConnProtViolation,
       "dlswTrapCntlTConn": dlswTrapCntlTConn,
       "dlswTrapCntlCircuit": dlswTrapCntlCircuit,
       "dlswTConn": dlswTConn,
       "dlswTConnStat": dlswTConnStat,
       "dlswTConnStatActiveConnections": dlswTConnStatActiveConnections,
       "dlswTConnStatCloseIdles": dlswTConnStatCloseIdles,
       "dlswTConnStatCloseBusys": dlswTConnStatCloseBusys,
       "dlswTConnConfigTable": dlswTConnConfigTable,
       "dlswTConnConfigEntry": dlswTConnConfigEntry,
       "dlswTConnConfigIndex": dlswTConnConfigIndex,
       "dlswTConnConfigTDomain": dlswTConnConfigTDomain,
       "dlswTConnConfigLocalTAddr": dlswTConnConfigLocalTAddr,
       "dlswTConnConfigRemoteTAddr": dlswTConnConfigRemoteTAddr,
       "dlswTConnConfigLastModifyTime": dlswTConnConfigLastModifyTime,
       "dlswTConnConfigEntryType": dlswTConnConfigEntryType,
       "dlswTConnConfigGroupDefinition": dlswTConnConfigGroupDefinition,
       "dlswTConnConfigSetupType": dlswTConnConfigSetupType,
       "dlswTConnConfigSapList": dlswTConnConfigSapList,
       "dlswTConnConfigAdvertiseMacNB": dlswTConnConfigAdvertiseMacNB,
       "dlswTConnConfigInitCirRecvWndw": dlswTConnConfigInitCirRecvWndw,
       "dlswTConnConfigOpens": dlswTConnConfigOpens,
       "dlswTConnConfigRowStatus": dlswTConnConfigRowStatus,
       "dlswTConnOperTable": dlswTConnOperTable,
       "dlswTConnOperEntry": dlswTConnOperEntry,
       "dlswTConnOperTDomain": dlswTConnOperTDomain,
       "dlswTConnOperLocalTAddr": dlswTConnOperLocalTAddr,
       "dlswTConnOperRemoteTAddr": dlswTConnOperRemoteTAddr,
       "dlswTConnOperEntryTime": dlswTConnOperEntryTime,
       "dlswTConnOperConnectTime": dlswTConnOperConnectTime,
       "dlswTConnOperState": dlswTConnOperState,
       "dlswTConnOperConfigIndex": dlswTConnOperConfigIndex,
       "dlswTConnOperFlowCntlMode": dlswTConnOperFlowCntlMode,
       "dlswTConnOperPartnerVersion": dlswTConnOperPartnerVersion,
       "dlswTConnOperPartnerVendorID": dlswTConnOperPartnerVendorID,
       "dlswTConnOperPartnerVersionStr": dlswTConnOperPartnerVersionStr,
       "dlswTConnOperPartnerInitPacingWndw": dlswTConnOperPartnerInitPacingWndw,
       "dlswTConnOperPartnerSapList": dlswTConnOperPartnerSapList,
       "dlswTConnOperPartnerNBExcl": dlswTConnOperPartnerNBExcl,
       "dlswTConnOperPartnerMacExcl": dlswTConnOperPartnerMacExcl,
       "dlswTConnOperPartnerNBInfo": dlswTConnOperPartnerNBInfo,
       "dlswTConnOperPartnerMacInfo": dlswTConnOperPartnerMacInfo,
       "dlswTConnOperDiscTime": dlswTConnOperDiscTime,
       "dlswTConnOperDiscReason": dlswTConnOperDiscReason,
       "dlswTConnOperDiscActiveCir": dlswTConnOperDiscActiveCir,
       "dlswTConnOperInDataPkts": dlswTConnOperInDataPkts,
       "dlswTConnOperOutDataPkts": dlswTConnOperOutDataPkts,
       "dlswTConnOperInDataOctets": dlswTConnOperInDataOctets,
       "dlswTConnOperOutDataOctets": dlswTConnOperOutDataOctets,
       "dlswTConnOperInCntlPkts": dlswTConnOperInCntlPkts,
       "dlswTConnOperOutCntlPkts": dlswTConnOperOutCntlPkts,
       "dlswTConnOperCURexSents": dlswTConnOperCURexSents,
       "dlswTConnOperICRexRcvds": dlswTConnOperICRexRcvds,
       "dlswTConnOperCURexRcvds": dlswTConnOperCURexRcvds,
       "dlswTConnOperICRexSents": dlswTConnOperICRexSents,
       "dlswTConnOperNQexSents": dlswTConnOperNQexSents,
       "dlswTConnOperNRexRcvds": dlswTConnOperNRexRcvds,
       "dlswTConnOperNQexRcvds": dlswTConnOperNQexRcvds,
       "dlswTConnOperNRexSents": dlswTConnOperNRexSents,
       "dlswTConnOperCirCreates": dlswTConnOperCirCreates,
       "dlswTConnOperCircuits": dlswTConnOperCircuits,
       "dlswTConnSpecific": dlswTConnSpecific,
       "dlswTConnTcp": dlswTConnTcp,
       "dlswTConnTcpConfigTable": dlswTConnTcpConfigTable,
       "dlswTConnTcpConfigEntry": dlswTConnTcpConfigEntry,
       "dlswTConnTcpConfigKeepAliveInt": dlswTConnTcpConfigKeepAliveInt,
       "dlswTConnTcpConfigTcpConnections": dlswTConnTcpConfigTcpConnections,
       "dlswTConnTcpConfigMaxSegmentSize": dlswTConnTcpConfigMaxSegmentSize,
       "dlswTConnTcpOperTable": dlswTConnTcpOperTable,
       "dlswTConnTcpOperEntry": dlswTConnTcpOperEntry,
       "dlswTConnTcpOperKeepAliveInt": dlswTConnTcpOperKeepAliveInt,
       "dlswTConnTcpOperPrefTcpConnections": dlswTConnTcpOperPrefTcpConnections,
       "dlswTConnTcpOperTcpConnections": dlswTConnTcpOperTcpConnections,
       "dlswInterface": dlswInterface,
       "dlswIfTable": dlswIfTable,
       "dlswIfEntry": dlswIfEntry,
       "dlswIfRowStatus": dlswIfRowStatus,
       "dlswIfVirtualSegment": dlswIfVirtualSegment,
       "dlswIfSapList": dlswIfSapList,
       "dlswDirectory": dlswDirectory,
       "dlswDirStat": dlswDirStat,
       "dlswDirMacEntries": dlswDirMacEntries,
       "dlswDirMacCacheHits": dlswDirMacCacheHits,
       "dlswDirMacCacheMisses": dlswDirMacCacheMisses,
       "dlswDirMacCacheNextIndex": dlswDirMacCacheNextIndex,
       "dlswDirNBEntries": dlswDirNBEntries,
       "dlswDirNBCacheHits": dlswDirNBCacheHits,
       "dlswDirNBCacheMisses": dlswDirNBCacheMisses,
       "dlswDirNBCacheNextIndex": dlswDirNBCacheNextIndex,
       "dlswDirCache": dlswDirCache,
       "dlswDirMacTable": dlswDirMacTable,
       "dlswDirMacEntry": dlswDirMacEntry,
       "dlswDirMacIndex": dlswDirMacIndex,
       "dlswDirMacMac": dlswDirMacMac,
       "dlswDirMacMask": dlswDirMacMask,
       "dlswDirMacEntryType": dlswDirMacEntryType,
       "dlswDirMacLocationType": dlswDirMacLocationType,
       "dlswDirMacLocation": dlswDirMacLocation,
       "dlswDirMacStatus": dlswDirMacStatus,
       "dlswDirMacLFSize": dlswDirMacLFSize,
       "dlswDirMacRowStatus": dlswDirMacRowStatus,
       "dlswDirNBTable": dlswDirNBTable,
       "dlswDirNBEntry": dlswDirNBEntry,
       "dlswDirNBIndex": dlswDirNBIndex,
       "dlswDirNBName": dlswDirNBName,
       "dlswDirNBNameType": dlswDirNBNameType,
       "dlswDirNBEntryType": dlswDirNBEntryType,
       "dlswDirNBLocationType": dlswDirNBLocationType,
       "dlswDirNBLocation": dlswDirNBLocation,
       "dlswDirNBStatus": dlswDirNBStatus,
       "dlswDirNBLFSize": dlswDirNBLFSize,
       "dlswDirNBRowStatus": dlswDirNBRowStatus,
       "dlswDirLocate": dlswDirLocate,
       "dlswDirLocateMacTable": dlswDirLocateMacTable,
       "dlswDirLocateMacEntry": dlswDirLocateMacEntry,
       "dlswDirLocateMacMac": dlswDirLocateMacMac,
       "dlswDirLocateMacMatch": dlswDirLocateMacMatch,
       "dlswDirLocateMacLocation": dlswDirLocateMacLocation,
       "dlswDirLocateNBTable": dlswDirLocateNBTable,
       "dlswDirLocateNBEntry": dlswDirLocateNBEntry,
       "dlswDirLocateNBName": dlswDirLocateNBName,
       "dlswDirLocateNBMatch": dlswDirLocateNBMatch,
       "dlswDirLocateNBLocation": dlswDirLocateNBLocation,
       "dlswCircuit": dlswCircuit,
       "dlswCircuitStat": dlswCircuitStat,
       "dlswCircuitStatActives": dlswCircuitStatActives,
       "dlswCircuitStatCreates": dlswCircuitStatCreates,
       "dlswCircuitTable": dlswCircuitTable,
       "dlswCircuitEntry": dlswCircuitEntry,
       "dlswCircuitS1Mac": dlswCircuitS1Mac,
       "dlswCircuitS1Sap": dlswCircuitS1Sap,
       "dlswCircuitS1IfIndex": dlswCircuitS1IfIndex,
       "dlswCircuitS1DlcType": dlswCircuitS1DlcType,
       "dlswCircuitS1RouteInfo": dlswCircuitS1RouteInfo,
       "dlswCircuitS1CircuitId": dlswCircuitS1CircuitId,
       "dlswCircuitS1Dlc": dlswCircuitS1Dlc,
       "dlswCircuitS2Mac": dlswCircuitS2Mac,
       "dlswCircuitS2Sap": dlswCircuitS2Sap,
       "dlswCircuitS2Location": dlswCircuitS2Location,
       "dlswCircuitS2TDomain": dlswCircuitS2TDomain,
       "dlswCircuitS2TAddress": dlswCircuitS2TAddress,
       "dlswCircuitS2CircuitId": dlswCircuitS2CircuitId,
       "dlswCircuitOrigin": dlswCircuitOrigin,
       "dlswCircuitEntryTime": dlswCircuitEntryTime,
       "dlswCircuitStateTime": dlswCircuitStateTime,
       "dlswCircuitState": dlswCircuitState,
       "dlswCircuitPriority": dlswCircuitPriority,
       "dlswCircuitFCSendGrantedUnits": dlswCircuitFCSendGrantedUnits,
       "dlswCircuitFCSendCurrentWndw": dlswCircuitFCSendCurrentWndw,
       "dlswCircuitFCRecvGrantedUnits": dlswCircuitFCRecvGrantedUnits,
       "dlswCircuitFCRecvCurrentWndw": dlswCircuitFCRecvCurrentWndw,
       "dlswCircuitFCLargestRecvGranted": dlswCircuitFCLargestRecvGranted,
       "dlswCircuitFCLargestSendGranted": dlswCircuitFCLargestSendGranted,
       "dlswCircuitFCHalveWndwSents": dlswCircuitFCHalveWndwSents,
       "dlswCircuitFCResetOpSents": dlswCircuitFCResetOpSents,
       "dlswCircuitFCHalveWndwRcvds": dlswCircuitFCHalveWndwRcvds,
       "dlswCircuitFCResetOpRcvds": dlswCircuitFCResetOpRcvds,
       "dlswCircuitDiscReasonLocal": dlswCircuitDiscReasonLocal,
       "dlswCircuitDiscReasonRemote": dlswCircuitDiscReasonRemote,
       "dlswCircuitDiscReasonRemoteData": dlswCircuitDiscReasonRemoteData,
       "dlswSdlc": dlswSdlc,
       "dlswSdlcLsEntries": dlswSdlcLsEntries,
       "dlswSdlcLsTable": dlswSdlcLsTable,
       "dlswSdlcLsEntry": dlswSdlcLsEntry,
       "dlswSdlcLsLocalMac": dlswSdlcLsLocalMac,
       "dlswSdlcLsLocalSap": dlswSdlcLsLocalSap,
       "dlswSdlcLsLocalIdBlock": dlswSdlcLsLocalIdBlock,
       "dlswSdlcLsLocalIdNum": dlswSdlcLsLocalIdNum,
       "dlswSdlcLsRemoteMac": dlswSdlcLsRemoteMac,
       "dlswSdlcLsRemoteSap": dlswSdlcLsRemoteSap,
       "dlswSdlcLsRowStatus": dlswSdlcLsRowStatus,
       "dlswDomains": dlswDomains,
       "dlswTCPDomain": dlswTCPDomain,
       "dlswConformance": dlswConformance,
       "dlswCompliances": dlswCompliances,
       "dlswCoreCompliance": dlswCoreCompliance,
       "dlswTConnTcpCompliance": dlswTConnTcpCompliance,
       "dlswDirCompliance": dlswDirCompliance,
       "dlswDirLocateCompliance": dlswDirLocateCompliance,
       "dlswSdlcCompliance": dlswSdlcCompliance,
       "dlswGroups": dlswGroups,
       "dlswNodeGroup": dlswNodeGroup,
       "dlswNodeNBGroup": dlswNodeNBGroup,
       "dlswTConnStatGroup": dlswTConnStatGroup,
       "dlswTConnConfigGroup": dlswTConnConfigGroup,
       "dlswTConnOperGroup": dlswTConnOperGroup,
       "dlswTConnNBGroup": dlswTConnNBGroup,
       "dlswTConnTcpConfigGroup": dlswTConnTcpConfigGroup,
       "dlswTConnTcpOperGroup": dlswTConnTcpOperGroup,
       "dlswInterfaceGroup": dlswInterfaceGroup,
       "dlswDirGroup": dlswDirGroup,
       "dlswDirNBGroup": dlswDirNBGroup,
       "dlswDirLocateGroup": dlswDirLocateGroup,
       "dlswDirLocateNBGroup": dlswDirLocateNBGroup,
       "dlswCircuitStatGroup": dlswCircuitStatGroup,
       "dlswCircuitGroup": dlswCircuitGroup,
       "dlswSdlcGroup": dlswSdlcGroup,
       "dlswNotificationGroup": dlswNotificationGroup}
)
