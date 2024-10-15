# SNMP MIB module (CISCO-IETF-PW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-PW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:52 2024
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

(CpwGroupID,
 CpwOperStatus,
 CpwVcIDType,
 CpwVcIndexType,
 CpwVcType) = mibBuilder.importSymbols(
    "CISCO-IETF-PW-TC-MIB",
    "CpwGroupID",
    "CpwOperStatus",
    "CpwVcIDType",
    "CpwVcIndexType",
    "CpwVcType")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cpwVcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 106)
)
cpwVcMIB.setRevisions(
        ("2004-03-17 12:00",
         "2003-02-26 12:00",
         "2002-05-26 12:00",
         "2002-01-30 12:00",
         "2001-11-07 12:00",
         "2001-07-11 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpwVcObjects_ObjectIdentity = ObjectIdentity
cpwVcObjects = _CpwVcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1)
)
_CpwVcIndexNext_Type = Unsigned32
_CpwVcIndexNext_Object = MibScalar
cpwVcIndexNext = _CpwVcIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 1),
    _CpwVcIndexNext_Type()
)
cpwVcIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcIndexNext.setStatus("current")
_CpwVcTable_Object = MibTable
cpwVcTable = _CpwVcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2)
)
if mibBuilder.loadTexts:
    cpwVcTable.setStatus("current")
_CpwVcEntry_Object = MibTableRow
cpwVcEntry = _CpwVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1)
)
cpwVcEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcEntry.setStatus("current")
_CpwVcIndex_Type = CpwVcIndexType
_CpwVcIndex_Object = MibTableColumn
cpwVcIndex = _CpwVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 1),
    _CpwVcIndex_Type()
)
cpwVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcIndex.setStatus("current")
_CpwVcType_Type = CpwVcType
_CpwVcType_Object = MibTableColumn
cpwVcType = _CpwVcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 2),
    _CpwVcType_Type()
)
cpwVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcType.setStatus("current")


class _CpwVcOwner_Type(Integer32):
    """Custom type cpwVcOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("maintenanceProtocol", 2),
          ("manual", 1),
          ("other", 3))
    )


_CpwVcOwner_Type.__name__ = "Integer32"
_CpwVcOwner_Object = MibTableColumn
cpwVcOwner = _CpwVcOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 3),
    _CpwVcOwner_Type()
)
cpwVcOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcOwner.setStatus("current")


class _CpwVcPsnType_Type(Integer32):
    """Custom type cpwVcPsnType based on Integer32"""
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
        *(("gre", 5),
          ("ip", 3),
          ("l2tp", 2),
          ("mpls", 1),
          ("mplsOverIp", 4),
          ("other", 6))
    )


_CpwVcPsnType_Type.__name__ = "Integer32"
_CpwVcPsnType_Object = MibTableColumn
cpwVcPsnType = _CpwVcPsnType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 4),
    _CpwVcPsnType_Type()
)
cpwVcPsnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcPsnType.setStatus("current")


class _CpwVcSetUpPriority_Type(Integer32):
    """Custom type cpwVcSetUpPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CpwVcSetUpPriority_Type.__name__ = "Integer32"
_CpwVcSetUpPriority_Object = MibTableColumn
cpwVcSetUpPriority = _CpwVcSetUpPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 5),
    _CpwVcSetUpPriority_Type()
)
cpwVcSetUpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcSetUpPriority.setStatus("current")


class _CpwVcHoldingPriority_Type(Integer32):
    """Custom type cpwVcHoldingPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CpwVcHoldingPriority_Type.__name__ = "Integer32"
_CpwVcHoldingPriority_Object = MibTableColumn
cpwVcHoldingPriority = _CpwVcHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 6),
    _CpwVcHoldingPriority_Type()
)
cpwVcHoldingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcHoldingPriority.setStatus("current")


class _CpwVcInboundMode_Type(Integer32):
    """Custom type cpwVcInboundMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 1),
          ("strict", 2))
    )


_CpwVcInboundMode_Type.__name__ = "Integer32"
_CpwVcInboundMode_Object = MibTableColumn
cpwVcInboundMode = _CpwVcInboundMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 7),
    _CpwVcInboundMode_Type()
)
cpwVcInboundMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcInboundMode.setStatus("current")


class _CpwVcPeerAddrType_Type(InetAddressType):
    """Custom type cpwVcPeerAddrType based on InetAddressType"""


_CpwVcPeerAddrType_Object = MibTableColumn
cpwVcPeerAddrType = _CpwVcPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 8),
    _CpwVcPeerAddrType_Type()
)
cpwVcPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcPeerAddrType.setStatus("current")
_CpwVcPeerAddr_Type = InetAddress
_CpwVcPeerAddr_Object = MibTableColumn
cpwVcPeerAddr = _CpwVcPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 9),
    _CpwVcPeerAddr_Type()
)
cpwVcPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcPeerAddr.setStatus("current")
_CpwVcID_Type = CpwVcIDType
_CpwVcID_Object = MibTableColumn
cpwVcID = _CpwVcID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 10),
    _CpwVcID_Type()
)
cpwVcID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcID.setStatus("current")
_CpwVcLocalGroupID_Type = CpwGroupID
_CpwVcLocalGroupID_Object = MibTableColumn
cpwVcLocalGroupID = _CpwVcLocalGroupID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 11),
    _CpwVcLocalGroupID_Type()
)
cpwVcLocalGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcLocalGroupID.setStatus("current")


class _CpwVcControlWord_Type(TruthValue):
    """Custom type cpwVcControlWord based on TruthValue"""


_CpwVcControlWord_Object = MibTableColumn
cpwVcControlWord = _CpwVcControlWord_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 12),
    _CpwVcControlWord_Type()
)
cpwVcControlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcControlWord.setStatus("current")


class _CpwVcLocalIfMtu_Type(Unsigned32):
    """Custom type cpwVcLocalIfMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpwVcLocalIfMtu_Type.__name__ = "Unsigned32"
_CpwVcLocalIfMtu_Object = MibTableColumn
cpwVcLocalIfMtu = _CpwVcLocalIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 13),
    _CpwVcLocalIfMtu_Type()
)
cpwVcLocalIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcLocalIfMtu.setStatus("current")


class _CpwVcLocalIfString_Type(TruthValue):
    """Custom type cpwVcLocalIfString based on TruthValue"""


_CpwVcLocalIfString_Object = MibTableColumn
cpwVcLocalIfString = _CpwVcLocalIfString_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 14),
    _CpwVcLocalIfString_Type()
)
cpwVcLocalIfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcLocalIfString.setStatus("current")
_CpwVcRemoteGroupID_Type = CpwGroupID
_CpwVcRemoteGroupID_Object = MibTableColumn
cpwVcRemoteGroupID = _CpwVcRemoteGroupID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 15),
    _CpwVcRemoteGroupID_Type()
)
cpwVcRemoteGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcRemoteGroupID.setStatus("current")


class _CpwVcRemoteControlWord_Type(Integer32):
    """Custom type cpwVcRemoteControlWord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noControlWord", 1),
          ("notYetKnown", 3),
          ("withControlWord", 2))
    )


_CpwVcRemoteControlWord_Type.__name__ = "Integer32"
_CpwVcRemoteControlWord_Object = MibTableColumn
cpwVcRemoteControlWord = _CpwVcRemoteControlWord_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 16),
    _CpwVcRemoteControlWord_Type()
)
cpwVcRemoteControlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcRemoteControlWord.setStatus("current")
_CpwVcRemoteIfMtu_Type = Unsigned32
_CpwVcRemoteIfMtu_Object = MibTableColumn
cpwVcRemoteIfMtu = _CpwVcRemoteIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 17),
    _CpwVcRemoteIfMtu_Type()
)
cpwVcRemoteIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcRemoteIfMtu.setStatus("current")


class _CpwVcRemoteIfString_Type(SnmpAdminString):
    """Custom type cpwVcRemoteIfString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpwVcRemoteIfString_Type.__name__ = "SnmpAdminString"
_CpwVcRemoteIfString_Object = MibTableColumn
cpwVcRemoteIfString = _CpwVcRemoteIfString_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 18),
    _CpwVcRemoteIfString_Type()
)
cpwVcRemoteIfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcRemoteIfString.setStatus("current")
_CpwVcOutboundVcLabel_Type = Unsigned32
_CpwVcOutboundVcLabel_Object = MibTableColumn
cpwVcOutboundVcLabel = _CpwVcOutboundVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 19),
    _CpwVcOutboundVcLabel_Type()
)
cpwVcOutboundVcLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcOutboundVcLabel.setStatus("current")
_CpwVcInboundVcLabel_Type = Unsigned32
_CpwVcInboundVcLabel_Object = MibTableColumn
cpwVcInboundVcLabel = _CpwVcInboundVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 20),
    _CpwVcInboundVcLabel_Type()
)
cpwVcInboundVcLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcInboundVcLabel.setStatus("current")
_CpwVcName_Type = SnmpAdminString
_CpwVcName_Object = MibTableColumn
cpwVcName = _CpwVcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 21),
    _CpwVcName_Type()
)
cpwVcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcName.setStatus("current")
_CpwVcDescr_Type = SnmpAdminString
_CpwVcDescr_Object = MibTableColumn
cpwVcDescr = _CpwVcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 22),
    _CpwVcDescr_Type()
)
cpwVcDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcDescr.setStatus("current")
_CpwVcCreateTime_Type = TimeStamp
_CpwVcCreateTime_Object = MibTableColumn
cpwVcCreateTime = _CpwVcCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 23),
    _CpwVcCreateTime_Type()
)
cpwVcCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcCreateTime.setStatus("current")
_CpwVcUpTime_Type = TimeTicks
_CpwVcUpTime_Object = MibTableColumn
cpwVcUpTime = _CpwVcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 24),
    _CpwVcUpTime_Type()
)
cpwVcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcUpTime.setStatus("current")


class _CpwVcAdminStatus_Type(Integer32):
    """Custom type cpwVcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_CpwVcAdminStatus_Type.__name__ = "Integer32"
_CpwVcAdminStatus_Object = MibTableColumn
cpwVcAdminStatus = _CpwVcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 25),
    _CpwVcAdminStatus_Type()
)
cpwVcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcAdminStatus.setStatus("current")
_CpwVcOperStatus_Type = CpwOperStatus
_CpwVcOperStatus_Object = MibTableColumn
cpwVcOperStatus = _CpwVcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 26),
    _CpwVcOperStatus_Type()
)
cpwVcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcOperStatus.setStatus("current")
_CpwVcInboundOperStatus_Type = CpwOperStatus
_CpwVcInboundOperStatus_Object = MibTableColumn
cpwVcInboundOperStatus = _CpwVcInboundOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 27),
    _CpwVcInboundOperStatus_Type()
)
cpwVcInboundOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcInboundOperStatus.setStatus("current")
_CpwVcOutboundOperStatus_Type = CpwOperStatus
_CpwVcOutboundOperStatus_Object = MibTableColumn
cpwVcOutboundOperStatus = _CpwVcOutboundOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 28),
    _CpwVcOutboundOperStatus_Type()
)
cpwVcOutboundOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcOutboundOperStatus.setStatus("current")


class _CpwVcTimeElapsed_Type(Integer32):
    """Custom type cpwVcTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_CpwVcTimeElapsed_Type.__name__ = "Integer32"
_CpwVcTimeElapsed_Object = MibTableColumn
cpwVcTimeElapsed = _CpwVcTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 29),
    _CpwVcTimeElapsed_Type()
)
cpwVcTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcTimeElapsed.setStatus("current")


class _CpwVcValidIntervals_Type(Integer32):
    """Custom type cpwVcValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CpwVcValidIntervals_Type.__name__ = "Integer32"
_CpwVcValidIntervals_Object = MibTableColumn
cpwVcValidIntervals = _CpwVcValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 30),
    _CpwVcValidIntervals_Type()
)
cpwVcValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcValidIntervals.setStatus("current")
_CpwVcRowStatus_Type = RowStatus
_CpwVcRowStatus_Object = MibTableColumn
cpwVcRowStatus = _CpwVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 31),
    _CpwVcRowStatus_Type()
)
cpwVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcRowStatus.setStatus("current")
_CpwVcStorageType_Type = StorageType
_CpwVcStorageType_Object = MibTableColumn
cpwVcStorageType = _CpwVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 2, 1, 32),
    _CpwVcStorageType_Type()
)
cpwVcStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcStorageType.setStatus("current")
_CpwVcPerfCurrentTable_Object = MibTable
cpwVcPerfCurrentTable = _CpwVcPerfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 3)
)
if mibBuilder.loadTexts:
    cpwVcPerfCurrentTable.setStatus("current")
_CpwVcPerfCurrentEntry_Object = MibTableRow
cpwVcPerfCurrentEntry = _CpwVcPerfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 3, 1)
)
cpwVcPerfCurrentEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcPerfCurrentEntry.setStatus("current")
_CpwVcPerfCurrentInHCPackets_Type = Counter64
_CpwVcPerfCurrentInHCPackets_Object = MibTableColumn
cpwVcPerfCurrentInHCPackets = _CpwVcPerfCurrentInHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 3, 1, 1),
    _CpwVcPerfCurrentInHCPackets_Type()
)
cpwVcPerfCurrentInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfCurrentInHCPackets.setStatus("current")
_CpwVcPerfCurrentInHCBytes_Type = Counter64
_CpwVcPerfCurrentInHCBytes_Object = MibTableColumn
cpwVcPerfCurrentInHCBytes = _CpwVcPerfCurrentInHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 3, 1, 2),
    _CpwVcPerfCurrentInHCBytes_Type()
)
cpwVcPerfCurrentInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfCurrentInHCBytes.setStatus("current")
_CpwVcPerfCurrentOutHCPackets_Type = Counter64
_CpwVcPerfCurrentOutHCPackets_Object = MibTableColumn
cpwVcPerfCurrentOutHCPackets = _CpwVcPerfCurrentOutHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 3, 1, 3),
    _CpwVcPerfCurrentOutHCPackets_Type()
)
cpwVcPerfCurrentOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfCurrentOutHCPackets.setStatus("current")
_CpwVcPerfCurrentOutHCBytes_Type = Counter64
_CpwVcPerfCurrentOutHCBytes_Object = MibTableColumn
cpwVcPerfCurrentOutHCBytes = _CpwVcPerfCurrentOutHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 3, 1, 4),
    _CpwVcPerfCurrentOutHCBytes_Type()
)
cpwVcPerfCurrentOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfCurrentOutHCBytes.setStatus("current")
_CpwVcPerfIntervalTable_Object = MibTable
cpwVcPerfIntervalTable = _CpwVcPerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 4)
)
if mibBuilder.loadTexts:
    cpwVcPerfIntervalTable.setStatus("current")
_CpwVcPerfIntervalEntry_Object = MibTableRow
cpwVcPerfIntervalEntry = _CpwVcPerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 4, 1)
)
cpwVcPerfIntervalEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
    (0, "CISCO-IETF-PW-MIB", "cpwVcPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    cpwVcPerfIntervalEntry.setStatus("current")


class _CpwVcPerfIntervalNumber_Type(Integer32):
    """Custom type cpwVcPerfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CpwVcPerfIntervalNumber_Type.__name__ = "Integer32"
_CpwVcPerfIntervalNumber_Object = MibTableColumn
cpwVcPerfIntervalNumber = _CpwVcPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 4, 1, 1),
    _CpwVcPerfIntervalNumber_Type()
)
cpwVcPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcPerfIntervalNumber.setStatus("current")
_CpwVcPerfIntervalValidData_Type = TruthValue
_CpwVcPerfIntervalValidData_Object = MibTableColumn
cpwVcPerfIntervalValidData = _CpwVcPerfIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 4, 1, 2),
    _CpwVcPerfIntervalValidData_Type()
)
cpwVcPerfIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfIntervalValidData.setStatus("current")
_CpwVcPerfIntervalTimeElapsed_Type = Integer32
_CpwVcPerfIntervalTimeElapsed_Object = MibTableColumn
cpwVcPerfIntervalTimeElapsed = _CpwVcPerfIntervalTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 4, 1, 3),
    _CpwVcPerfIntervalTimeElapsed_Type()
)
cpwVcPerfIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfIntervalTimeElapsed.setStatus("current")
_CpwVcPerfIntervalInHCPackets_Type = Counter64
_CpwVcPerfIntervalInHCPackets_Object = MibTableColumn
cpwVcPerfIntervalInHCPackets = _CpwVcPerfIntervalInHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 4, 1, 4),
    _CpwVcPerfIntervalInHCPackets_Type()
)
cpwVcPerfIntervalInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfIntervalInHCPackets.setStatus("current")
_CpwVcPerfIntervalInHCBytes_Type = Counter64
_CpwVcPerfIntervalInHCBytes_Object = MibTableColumn
cpwVcPerfIntervalInHCBytes = _CpwVcPerfIntervalInHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 4, 1, 5),
    _CpwVcPerfIntervalInHCBytes_Type()
)
cpwVcPerfIntervalInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfIntervalInHCBytes.setStatus("current")
_CpwVcPerfIntervalOutHCPackets_Type = Counter64
_CpwVcPerfIntervalOutHCPackets_Object = MibTableColumn
cpwVcPerfIntervalOutHCPackets = _CpwVcPerfIntervalOutHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 4, 1, 6),
    _CpwVcPerfIntervalOutHCPackets_Type()
)
cpwVcPerfIntervalOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfIntervalOutHCPackets.setStatus("current")
_CpwVcPerfIntervalOutHCBytes_Type = Counter64
_CpwVcPerfIntervalOutHCBytes_Object = MibTableColumn
cpwVcPerfIntervalOutHCBytes = _CpwVcPerfIntervalOutHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 4, 1, 7),
    _CpwVcPerfIntervalOutHCBytes_Type()
)
cpwVcPerfIntervalOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfIntervalOutHCBytes.setStatus("current")
_CpwVcPerfTotalTable_Object = MibTable
cpwVcPerfTotalTable = _CpwVcPerfTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 5)
)
if mibBuilder.loadTexts:
    cpwVcPerfTotalTable.setStatus("current")
_CpwVcPerfTotalEntry_Object = MibTableRow
cpwVcPerfTotalEntry = _CpwVcPerfTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 5, 1)
)
cpwVcPerfTotalEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcPerfTotalEntry.setStatus("current")
_CpwVcPerfTotalInHCPackets_Type = Counter64
_CpwVcPerfTotalInHCPackets_Object = MibTableColumn
cpwVcPerfTotalInHCPackets = _CpwVcPerfTotalInHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 5, 1, 1),
    _CpwVcPerfTotalInHCPackets_Type()
)
cpwVcPerfTotalInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfTotalInHCPackets.setStatus("current")
_CpwVcPerfTotalInHCBytes_Type = Counter64
_CpwVcPerfTotalInHCBytes_Object = MibTableColumn
cpwVcPerfTotalInHCBytes = _CpwVcPerfTotalInHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 5, 1, 2),
    _CpwVcPerfTotalInHCBytes_Type()
)
cpwVcPerfTotalInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfTotalInHCBytes.setStatus("current")
_CpwVcPerfTotalOutHCPackets_Type = Counter64
_CpwVcPerfTotalOutHCPackets_Object = MibTableColumn
cpwVcPerfTotalOutHCPackets = _CpwVcPerfTotalOutHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 5, 1, 3),
    _CpwVcPerfTotalOutHCPackets_Type()
)
cpwVcPerfTotalOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfTotalOutHCPackets.setStatus("current")
_CpwVcPerfTotalOutHCBytes_Type = Counter64
_CpwVcPerfTotalOutHCBytes_Object = MibTableColumn
cpwVcPerfTotalOutHCBytes = _CpwVcPerfTotalOutHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 5, 1, 4),
    _CpwVcPerfTotalOutHCBytes_Type()
)
cpwVcPerfTotalOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfTotalOutHCBytes.setStatus("current")
_CpwVcPerfTotalDiscontinuityTime_Type = TimeStamp
_CpwVcPerfTotalDiscontinuityTime_Object = MibTableColumn
cpwVcPerfTotalDiscontinuityTime = _CpwVcPerfTotalDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 5, 1, 5),
    _CpwVcPerfTotalDiscontinuityTime_Type()
)
cpwVcPerfTotalDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfTotalDiscontinuityTime.setStatus("current")
_CpwVcPerfTotalErrorPackets_Type = Counter64
_CpwVcPerfTotalErrorPackets_Object = MibScalar
cpwVcPerfTotalErrorPackets = _CpwVcPerfTotalErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 6),
    _CpwVcPerfTotalErrorPackets_Type()
)
cpwVcPerfTotalErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPerfTotalErrorPackets.setStatus("current")
_CpwVcIdMappingTable_Object = MibTable
cpwVcIdMappingTable = _CpwVcIdMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 7)
)
if mibBuilder.loadTexts:
    cpwVcIdMappingTable.setStatus("current")
_CpwVcIdMappingEntry_Object = MibTableRow
cpwVcIdMappingEntry = _CpwVcIdMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 7, 1)
)
cpwVcIdMappingEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIdMappingVcType"),
    (0, "CISCO-IETF-PW-MIB", "cpwVcIdMappingVcID"),
    (0, "CISCO-IETF-PW-MIB", "cpwVcIdMappingPeerAddrType"),
    (0, "CISCO-IETF-PW-MIB", "cpwVcIdMappingPeerAddr"),
    (0, "CISCO-IETF-PW-MIB", "cpwVcIdMappingVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcIdMappingEntry.setStatus("current")
_CpwVcIdMappingVcType_Type = CpwVcType
_CpwVcIdMappingVcType_Object = MibTableColumn
cpwVcIdMappingVcType = _CpwVcIdMappingVcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 7, 1, 1),
    _CpwVcIdMappingVcType_Type()
)
cpwVcIdMappingVcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcIdMappingVcType.setStatus("current")
_CpwVcIdMappingVcID_Type = CpwVcIDType
_CpwVcIdMappingVcID_Object = MibTableColumn
cpwVcIdMappingVcID = _CpwVcIdMappingVcID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 7, 1, 2),
    _CpwVcIdMappingVcID_Type()
)
cpwVcIdMappingVcID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcIdMappingVcID.setStatus("current")
_CpwVcIdMappingPeerAddrType_Type = InetAddressType
_CpwVcIdMappingPeerAddrType_Object = MibTableColumn
cpwVcIdMappingPeerAddrType = _CpwVcIdMappingPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 7, 1, 3),
    _CpwVcIdMappingPeerAddrType_Type()
)
cpwVcIdMappingPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcIdMappingPeerAddrType.setStatus("current")
_CpwVcIdMappingPeerAddr_Type = InetAddress
_CpwVcIdMappingPeerAddr_Object = MibTableColumn
cpwVcIdMappingPeerAddr = _CpwVcIdMappingPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 7, 1, 4),
    _CpwVcIdMappingPeerAddr_Type()
)
cpwVcIdMappingPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcIdMappingPeerAddr.setStatus("current")
_CpwVcIdMappingVcIndex_Type = CpwVcIndexType
_CpwVcIdMappingVcIndex_Object = MibTableColumn
cpwVcIdMappingVcIndex = _CpwVcIdMappingVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 7, 1, 5),
    _CpwVcIdMappingVcIndex_Type()
)
cpwVcIdMappingVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcIdMappingVcIndex.setStatus("current")
_CpwVcPeerMappingTable_Object = MibTable
cpwVcPeerMappingTable = _CpwVcPeerMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 8)
)
if mibBuilder.loadTexts:
    cpwVcPeerMappingTable.setStatus("current")
_CpwVcPeerMappingEntry_Object = MibTableRow
cpwVcPeerMappingEntry = _CpwVcPeerMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 8, 1)
)
cpwVcPeerMappingEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcPeerMappingPeerAddrType"),
    (0, "CISCO-IETF-PW-MIB", "cpwVcPeerMappingPeerAddr"),
    (0, "CISCO-IETF-PW-MIB", "cpwVcPeerMappingVcType"),
    (0, "CISCO-IETF-PW-MIB", "cpwVcPeerMappingVcID"),
    (0, "CISCO-IETF-PW-MIB", "cpwVcPeerMappingVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcPeerMappingEntry.setStatus("current")
_CpwVcPeerMappingPeerAddrType_Type = InetAddressType
_CpwVcPeerMappingPeerAddrType_Object = MibTableColumn
cpwVcPeerMappingPeerAddrType = _CpwVcPeerMappingPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 8, 1, 1),
    _CpwVcPeerMappingPeerAddrType_Type()
)
cpwVcPeerMappingPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcPeerMappingPeerAddrType.setStatus("current")
_CpwVcPeerMappingPeerAddr_Type = InetAddress
_CpwVcPeerMappingPeerAddr_Object = MibTableColumn
cpwVcPeerMappingPeerAddr = _CpwVcPeerMappingPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 8, 1, 2),
    _CpwVcPeerMappingPeerAddr_Type()
)
cpwVcPeerMappingPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcPeerMappingPeerAddr.setStatus("current")
_CpwVcPeerMappingVcType_Type = CpwVcType
_CpwVcPeerMappingVcType_Object = MibTableColumn
cpwVcPeerMappingVcType = _CpwVcPeerMappingVcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 8, 1, 3),
    _CpwVcPeerMappingVcType_Type()
)
cpwVcPeerMappingVcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcPeerMappingVcType.setStatus("current")
_CpwVcPeerMappingVcID_Type = CpwVcIDType
_CpwVcPeerMappingVcID_Object = MibTableColumn
cpwVcPeerMappingVcID = _CpwVcPeerMappingVcID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 8, 1, 4),
    _CpwVcPeerMappingVcID_Type()
)
cpwVcPeerMappingVcID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcPeerMappingVcID.setStatus("current")
_CpwVcPeerMappingVcIndex_Type = CpwVcIndexType
_CpwVcPeerMappingVcIndex_Object = MibTableColumn
cpwVcPeerMappingVcIndex = _CpwVcPeerMappingVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 8, 1, 5),
    _CpwVcPeerMappingVcIndex_Type()
)
cpwVcPeerMappingVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcPeerMappingVcIndex.setStatus("current")


class _CpwVcUpDownNotifEnable_Type(TruthValue):
    """Custom type cpwVcUpDownNotifEnable based on TruthValue"""


_CpwVcUpDownNotifEnable_Object = MibScalar
cpwVcUpDownNotifEnable = _CpwVcUpDownNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 9),
    _CpwVcUpDownNotifEnable_Type()
)
cpwVcUpDownNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwVcUpDownNotifEnable.setStatus("current")
_CpwVcNotifRate_Type = Unsigned32
_CpwVcNotifRate_Object = MibScalar
cpwVcNotifRate = _CpwVcNotifRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 1, 10),
    _CpwVcNotifRate_Type()
)
cpwVcNotifRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwVcNotifRate.setStatus("current")
_CpwVcNotifications_ObjectIdentity = ObjectIdentity
cpwVcNotifications = _CpwVcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 2)
)
_CpwVcConformance_ObjectIdentity = ObjectIdentity
cpwVcConformance = _CpwVcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 3)
)
_CpwVcGroups_ObjectIdentity = ObjectIdentity
cpwVcGroups = _CpwVcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 3, 1)
)
_CpwVcCompliances_ObjectIdentity = ObjectIdentity
cpwVcCompliances = _CpwVcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 3, 2)
)

# Managed Objects groups

cpwVcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 3, 1, 1)
)
cpwVcGroup.setObjects(
      *(("CISCO-IETF-PW-MIB", "cpwVcIndexNext"),
        ("CISCO-IETF-PW-MIB", "cpwVcType"),
        ("CISCO-IETF-PW-MIB", "cpwVcOwner"),
        ("CISCO-IETF-PW-MIB", "cpwVcPsnType"),
        ("CISCO-IETF-PW-MIB", "cpwVcSetUpPriority"),
        ("CISCO-IETF-PW-MIB", "cpwVcHoldingPriority"),
        ("CISCO-IETF-PW-MIB", "cpwVcInboundMode"),
        ("CISCO-IETF-PW-MIB", "cpwVcPeerAddrType"),
        ("CISCO-IETF-PW-MIB", "cpwVcPeerAddr"),
        ("CISCO-IETF-PW-MIB", "cpwVcID"),
        ("CISCO-IETF-PW-MIB", "cpwVcLocalGroupID"),
        ("CISCO-IETF-PW-MIB", "cpwVcControlWord"),
        ("CISCO-IETF-PW-MIB", "cpwVcLocalIfMtu"),
        ("CISCO-IETF-PW-MIB", "cpwVcLocalIfString"),
        ("CISCO-IETF-PW-MIB", "cpwVcRemoteGroupID"),
        ("CISCO-IETF-PW-MIB", "cpwVcRemoteControlWord"),
        ("CISCO-IETF-PW-MIB", "cpwVcRemoteIfMtu"),
        ("CISCO-IETF-PW-MIB", "cpwVcRemoteIfString"),
        ("CISCO-IETF-PW-MIB", "cpwVcOutboundVcLabel"),
        ("CISCO-IETF-PW-MIB", "cpwVcInboundVcLabel"),
        ("CISCO-IETF-PW-MIB", "cpwVcName"),
        ("CISCO-IETF-PW-MIB", "cpwVcDescr"),
        ("CISCO-IETF-PW-MIB", "cpwVcCreateTime"),
        ("CISCO-IETF-PW-MIB", "cpwVcUpTime"),
        ("CISCO-IETF-PW-MIB", "cpwVcAdminStatus"),
        ("CISCO-IETF-PW-MIB", "cpwVcOperStatus"),
        ("CISCO-IETF-PW-MIB", "cpwVcOutboundOperStatus"),
        ("CISCO-IETF-PW-MIB", "cpwVcInboundOperStatus"),
        ("CISCO-IETF-PW-MIB", "cpwVcTimeElapsed"),
        ("CISCO-IETF-PW-MIB", "cpwVcValidIntervals"),
        ("CISCO-IETF-PW-MIB", "cpwVcRowStatus"),
        ("CISCO-IETF-PW-MIB", "cpwVcStorageType"),
        ("CISCO-IETF-PW-MIB", "cpwVcUpDownNotifEnable"),
        ("CISCO-IETF-PW-MIB", "cpwVcNotifRate"))
)
if mibBuilder.loadTexts:
    cpwVcGroup.setStatus("current")

cpwVcPeformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 3, 1, 2)
)
cpwVcPeformanceGroup.setObjects(
      *(("CISCO-IETF-PW-MIB", "cpwVcPerfCurrentInHCPackets"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfCurrentInHCBytes"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfCurrentOutHCPackets"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfCurrentOutHCBytes"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfIntervalValidData"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfIntervalTimeElapsed"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfIntervalInHCPackets"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfIntervalInHCBytes"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfIntervalOutHCPackets"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfIntervalOutHCBytes"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfTotalInHCPackets"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfTotalInHCBytes"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfTotalOutHCPackets"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfTotalOutHCBytes"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfTotalDiscontinuityTime"),
        ("CISCO-IETF-PW-MIB", "cpwVcPerfTotalErrorPackets"))
)
if mibBuilder.loadTexts:
    cpwVcPeformanceGroup.setStatus("current")

cpwVcMappingTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 3, 1, 3)
)
cpwVcMappingTablesGroup.setObjects(
      *(("CISCO-IETF-PW-MIB", "cpwVcIdMappingVcIndex"),
        ("CISCO-IETF-PW-MIB", "cpwVcPeerMappingVcIndex"))
)
if mibBuilder.loadTexts:
    cpwVcMappingTablesGroup.setStatus("current")


# Notification objects

cpwVcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 2, 1)
)
cpwVcDown.setObjects(
      *(("CISCO-IETF-PW-MIB", "cpwVcOperStatus"),
        ("CISCO-IETF-PW-MIB", "cpwVcOperStatus"))
)
if mibBuilder.loadTexts:
    cpwVcDown.setStatus(
        "current"
    )

cpwVcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 2, 2)
)
cpwVcUp.setObjects(
      *(("CISCO-IETF-PW-MIB", "cpwVcOperStatus"),
        ("CISCO-IETF-PW-MIB", "cpwVcOperStatus"))
)
if mibBuilder.loadTexts:
    cpwVcUp.setStatus(
        "current"
    )


# Notifications groups

cpwVcNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 3, 1, 4)
)
cpwVcNotificationsGroup.setObjects(
      *(("CISCO-IETF-PW-MIB", "cpwVcUp"),
        ("CISCO-IETF-PW-MIB", "cpwVcDown"))
)
if mibBuilder.loadTexts:
    cpwVcNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cpwModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 106, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cpwModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-PW-MIB",
    **{"cpwVcMIB": cpwVcMIB,
       "cpwVcObjects": cpwVcObjects,
       "cpwVcIndexNext": cpwVcIndexNext,
       "cpwVcTable": cpwVcTable,
       "cpwVcEntry": cpwVcEntry,
       "cpwVcIndex": cpwVcIndex,
       "cpwVcType": cpwVcType,
       "cpwVcOwner": cpwVcOwner,
       "cpwVcPsnType": cpwVcPsnType,
       "cpwVcSetUpPriority": cpwVcSetUpPriority,
       "cpwVcHoldingPriority": cpwVcHoldingPriority,
       "cpwVcInboundMode": cpwVcInboundMode,
       "cpwVcPeerAddrType": cpwVcPeerAddrType,
       "cpwVcPeerAddr": cpwVcPeerAddr,
       "cpwVcID": cpwVcID,
       "cpwVcLocalGroupID": cpwVcLocalGroupID,
       "cpwVcControlWord": cpwVcControlWord,
       "cpwVcLocalIfMtu": cpwVcLocalIfMtu,
       "cpwVcLocalIfString": cpwVcLocalIfString,
       "cpwVcRemoteGroupID": cpwVcRemoteGroupID,
       "cpwVcRemoteControlWord": cpwVcRemoteControlWord,
       "cpwVcRemoteIfMtu": cpwVcRemoteIfMtu,
       "cpwVcRemoteIfString": cpwVcRemoteIfString,
       "cpwVcOutboundVcLabel": cpwVcOutboundVcLabel,
       "cpwVcInboundVcLabel": cpwVcInboundVcLabel,
       "cpwVcName": cpwVcName,
       "cpwVcDescr": cpwVcDescr,
       "cpwVcCreateTime": cpwVcCreateTime,
       "cpwVcUpTime": cpwVcUpTime,
       "cpwVcAdminStatus": cpwVcAdminStatus,
       "cpwVcOperStatus": cpwVcOperStatus,
       "cpwVcInboundOperStatus": cpwVcInboundOperStatus,
       "cpwVcOutboundOperStatus": cpwVcOutboundOperStatus,
       "cpwVcTimeElapsed": cpwVcTimeElapsed,
       "cpwVcValidIntervals": cpwVcValidIntervals,
       "cpwVcRowStatus": cpwVcRowStatus,
       "cpwVcStorageType": cpwVcStorageType,
       "cpwVcPerfCurrentTable": cpwVcPerfCurrentTable,
       "cpwVcPerfCurrentEntry": cpwVcPerfCurrentEntry,
       "cpwVcPerfCurrentInHCPackets": cpwVcPerfCurrentInHCPackets,
       "cpwVcPerfCurrentInHCBytes": cpwVcPerfCurrentInHCBytes,
       "cpwVcPerfCurrentOutHCPackets": cpwVcPerfCurrentOutHCPackets,
       "cpwVcPerfCurrentOutHCBytes": cpwVcPerfCurrentOutHCBytes,
       "cpwVcPerfIntervalTable": cpwVcPerfIntervalTable,
       "cpwVcPerfIntervalEntry": cpwVcPerfIntervalEntry,
       "cpwVcPerfIntervalNumber": cpwVcPerfIntervalNumber,
       "cpwVcPerfIntervalValidData": cpwVcPerfIntervalValidData,
       "cpwVcPerfIntervalTimeElapsed": cpwVcPerfIntervalTimeElapsed,
       "cpwVcPerfIntervalInHCPackets": cpwVcPerfIntervalInHCPackets,
       "cpwVcPerfIntervalInHCBytes": cpwVcPerfIntervalInHCBytes,
       "cpwVcPerfIntervalOutHCPackets": cpwVcPerfIntervalOutHCPackets,
       "cpwVcPerfIntervalOutHCBytes": cpwVcPerfIntervalOutHCBytes,
       "cpwVcPerfTotalTable": cpwVcPerfTotalTable,
       "cpwVcPerfTotalEntry": cpwVcPerfTotalEntry,
       "cpwVcPerfTotalInHCPackets": cpwVcPerfTotalInHCPackets,
       "cpwVcPerfTotalInHCBytes": cpwVcPerfTotalInHCBytes,
       "cpwVcPerfTotalOutHCPackets": cpwVcPerfTotalOutHCPackets,
       "cpwVcPerfTotalOutHCBytes": cpwVcPerfTotalOutHCBytes,
       "cpwVcPerfTotalDiscontinuityTime": cpwVcPerfTotalDiscontinuityTime,
       "cpwVcPerfTotalErrorPackets": cpwVcPerfTotalErrorPackets,
       "cpwVcIdMappingTable": cpwVcIdMappingTable,
       "cpwVcIdMappingEntry": cpwVcIdMappingEntry,
       "cpwVcIdMappingVcType": cpwVcIdMappingVcType,
       "cpwVcIdMappingVcID": cpwVcIdMappingVcID,
       "cpwVcIdMappingPeerAddrType": cpwVcIdMappingPeerAddrType,
       "cpwVcIdMappingPeerAddr": cpwVcIdMappingPeerAddr,
       "cpwVcIdMappingVcIndex": cpwVcIdMappingVcIndex,
       "cpwVcPeerMappingTable": cpwVcPeerMappingTable,
       "cpwVcPeerMappingEntry": cpwVcPeerMappingEntry,
       "cpwVcPeerMappingPeerAddrType": cpwVcPeerMappingPeerAddrType,
       "cpwVcPeerMappingPeerAddr": cpwVcPeerMappingPeerAddr,
       "cpwVcPeerMappingVcType": cpwVcPeerMappingVcType,
       "cpwVcPeerMappingVcID": cpwVcPeerMappingVcID,
       "cpwVcPeerMappingVcIndex": cpwVcPeerMappingVcIndex,
       "cpwVcUpDownNotifEnable": cpwVcUpDownNotifEnable,
       "cpwVcNotifRate": cpwVcNotifRate,
       "cpwVcNotifications": cpwVcNotifications,
       "cpwVcDown": cpwVcDown,
       "cpwVcUp": cpwVcUp,
       "cpwVcConformance": cpwVcConformance,
       "cpwVcGroups": cpwVcGroups,
       "cpwVcGroup": cpwVcGroup,
       "cpwVcPeformanceGroup": cpwVcPeformanceGroup,
       "cpwVcMappingTablesGroup": cpwVcMappingTablesGroup,
       "cpwVcNotificationsGroup": cpwVcNotificationsGroup,
       "cpwVcCompliances": cpwVcCompliances,
       "cpwModuleCompliance": cpwModuleCompliance}
)
