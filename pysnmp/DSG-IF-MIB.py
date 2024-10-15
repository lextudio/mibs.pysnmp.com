# SNMP MIB module (DSG-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DSG-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:39 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(Dsid,) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "Dsid")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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

dsgIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3)
)
dsgIfMIB.setRevisions(
        ("2017-06-15 00:00",
         "2011-11-17 00:00",
         "2009-05-29 00:00",
         "2008-06-26 00:00",
         "2006-07-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DsgIfMIBNotifications_ObjectIdentity = ObjectIdentity
dsgIfMIBNotifications = _DsgIfMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 0)
)
_DsgIfMIBObjects_ObjectIdentity = ObjectIdentity
dsgIfMIBObjects = _DsgIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1)
)
_DsgIfClassifier_ObjectIdentity = ObjectIdentity
dsgIfClassifier = _DsgIfClassifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1)
)
_DsgIfClassifierTable_Object = MibTable
dsgIfClassifierTable = _DsgIfClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dsgIfClassifierTable.setStatus("current")
_DsgIfClassifierEntry_Object = MibTableRow
dsgIfClassifierEntry = _DsgIfClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1, 1)
)
dsgIfClassifierEntry.setIndexNames(
    (0, "DSG-IF-MIB", "dsgIfTunnelIndex"),
    (0, "DSG-IF-MIB", "dsgIfClassId"),
)
if mibBuilder.loadTexts:
    dsgIfClassifierEntry.setStatus("current")


class _DsgIfClassId_Type(Unsigned32):
    """Custom type dsgIfClassId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsgIfClassId_Type.__name__ = "Unsigned32"
_DsgIfClassId_Object = MibTableColumn
dsgIfClassId = _DsgIfClassId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1, 1, 1),
    _DsgIfClassId_Type()
)
dsgIfClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfClassId.setStatus("current")


class _DsgIfClassPriority_Type(Unsigned32):
    """Custom type dsgIfClassPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DsgIfClassPriority_Type.__name__ = "Unsigned32"
_DsgIfClassPriority_Object = MibTableColumn
dsgIfClassPriority = _DsgIfClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1, 1, 2),
    _DsgIfClassPriority_Type()
)
dsgIfClassPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClassPriority.setStatus("current")


class _DsgIfClassSrcIpAddrType_Type(InetAddressType):
    """Custom type dsgIfClassSrcIpAddrType based on InetAddressType"""


_DsgIfClassSrcIpAddrType_Object = MibTableColumn
dsgIfClassSrcIpAddrType = _DsgIfClassSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1, 1, 3),
    _DsgIfClassSrcIpAddrType_Type()
)
dsgIfClassSrcIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClassSrcIpAddrType.setStatus("current")


class _DsgIfClassSrcIpAddr_Type(InetAddress):
    """Custom type dsgIfClassSrcIpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_DsgIfClassSrcIpAddr_Object = MibTableColumn
dsgIfClassSrcIpAddr = _DsgIfClassSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1, 1, 4),
    _DsgIfClassSrcIpAddr_Type()
)
dsgIfClassSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClassSrcIpAddr.setStatus("current")


class _DsgIfClassSrcIpPrefixLength_Type(InetAddressPrefixLength):
    """Custom type dsgIfClassSrcIpPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 32


_DsgIfClassSrcIpPrefixLength_Object = MibTableColumn
dsgIfClassSrcIpPrefixLength = _DsgIfClassSrcIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1, 1, 5),
    _DsgIfClassSrcIpPrefixLength_Type()
)
dsgIfClassSrcIpPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClassSrcIpPrefixLength.setStatus("current")


class _DsgIfClassDestIpAddressType_Type(InetAddressType):
    """Custom type dsgIfClassDestIpAddressType based on InetAddressType"""


_DsgIfClassDestIpAddressType_Object = MibTableColumn
dsgIfClassDestIpAddressType = _DsgIfClassDestIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1, 1, 6),
    _DsgIfClassDestIpAddressType_Type()
)
dsgIfClassDestIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClassDestIpAddressType.setStatus("current")


class _DsgIfClassDestIpAddress_Type(InetAddress):
    """Custom type dsgIfClassDestIpAddress based on InetAddress"""
    defaultHexValue = "00000000"


_DsgIfClassDestIpAddress_Object = MibTableColumn
dsgIfClassDestIpAddress = _DsgIfClassDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1, 1, 7),
    _DsgIfClassDestIpAddress_Type()
)
dsgIfClassDestIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClassDestIpAddress.setStatus("current")


class _DsgIfClassDestPortStart_Type(InetPortNumber):
    """Custom type dsgIfClassDestPortStart based on InetPortNumber"""
    defaultValue = 0


_DsgIfClassDestPortStart_Object = MibTableColumn
dsgIfClassDestPortStart = _DsgIfClassDestPortStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1, 1, 8),
    _DsgIfClassDestPortStart_Type()
)
dsgIfClassDestPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClassDestPortStart.setStatus("current")


class _DsgIfClassDestPortEnd_Type(InetPortNumber):
    """Custom type dsgIfClassDestPortEnd based on InetPortNumber"""
    defaultValue = 65535


_DsgIfClassDestPortEnd_Object = MibTableColumn
dsgIfClassDestPortEnd = _DsgIfClassDestPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1, 1, 9),
    _DsgIfClassDestPortEnd_Type()
)
dsgIfClassDestPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClassDestPortEnd.setStatus("current")
_DsgIfClassRowStatus_Type = RowStatus
_DsgIfClassRowStatus_Object = MibTableColumn
dsgIfClassRowStatus = _DsgIfClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1, 1, 10),
    _DsgIfClassRowStatus_Type()
)
dsgIfClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClassRowStatus.setStatus("current")


class _DsgIfClassIncludeInDCD_Type(TruthValue):
    """Custom type dsgIfClassIncludeInDCD based on TruthValue"""


_DsgIfClassIncludeInDCD_Object = MibTableColumn
dsgIfClassIncludeInDCD = _DsgIfClassIncludeInDCD_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 1, 1, 1, 11),
    _DsgIfClassIncludeInDCD_Type()
)
dsgIfClassIncludeInDCD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClassIncludeInDCD.setStatus("current")
_DsgIfTunnel_ObjectIdentity = ObjectIdentity
dsgIfTunnel = _DsgIfTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 2)
)
_DsgIfTunnelTable_Object = MibTable
dsgIfTunnelTable = _DsgIfTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsgIfTunnelTable.setStatus("current")
_DsgIfTunnelEntry_Object = MibTableRow
dsgIfTunnelEntry = _DsgIfTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 2, 1, 1)
)
dsgIfTunnelEntry.setIndexNames(
    (0, "DSG-IF-MIB", "dsgIfTunnelIndex"),
)
if mibBuilder.loadTexts:
    dsgIfTunnelEntry.setStatus("current")
_DsgIfTunnelIndex_Type = Unsigned32
_DsgIfTunnelIndex_Object = MibTableColumn
dsgIfTunnelIndex = _DsgIfTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 2, 1, 1, 1),
    _DsgIfTunnelIndex_Type()
)
dsgIfTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfTunnelIndex.setStatus("current")
_DsgIfTunnelGroupIndex_Type = Unsigned32
_DsgIfTunnelGroupIndex_Object = MibTableColumn
dsgIfTunnelGroupIndex = _DsgIfTunnelGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 2, 1, 1, 2),
    _DsgIfTunnelGroupIndex_Type()
)
dsgIfTunnelGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTunnelGroupIndex.setStatus("current")
_DsgIfTunnelClientIdListIndex_Type = Unsigned32
_DsgIfTunnelClientIdListIndex_Object = MibTableColumn
dsgIfTunnelClientIdListIndex = _DsgIfTunnelClientIdListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 2, 1, 1, 3),
    _DsgIfTunnelClientIdListIndex_Type()
)
dsgIfTunnelClientIdListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTunnelClientIdListIndex.setStatus("current")


class _DsgIfTunnelMacAddress_Type(MacAddress):
    """Custom type dsgIfTunnelMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_DsgIfTunnelMacAddress_Object = MibTableColumn
dsgIfTunnelMacAddress = _DsgIfTunnelMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 2, 1, 1, 4),
    _DsgIfTunnelMacAddress_Type()
)
dsgIfTunnelMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTunnelMacAddress.setStatus("current")
_DsgIfTunnelServiceClassName_Type = SnmpAdminString
_DsgIfTunnelServiceClassName_Object = MibTableColumn
dsgIfTunnelServiceClassName = _DsgIfTunnelServiceClassName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 2, 1, 1, 5),
    _DsgIfTunnelServiceClassName_Type()
)
dsgIfTunnelServiceClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTunnelServiceClassName.setStatus("current")
_DsgIfTunnelRowStatus_Type = RowStatus
_DsgIfTunnelRowStatus_Object = MibTableColumn
dsgIfTunnelRowStatus = _DsgIfTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 2, 1, 1, 6),
    _DsgIfTunnelRowStatus_Type()
)
dsgIfTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTunnelRowStatus.setStatus("current")
_DsgIfTunnelGrpToChannel_ObjectIdentity = ObjectIdentity
dsgIfTunnelGrpToChannel = _DsgIfTunnelGrpToChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 3)
)
_DsgIfTunnelGrpToChannelTable_Object = MibTable
dsgIfTunnelGrpToChannelTable = _DsgIfTunnelGrpToChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dsgIfTunnelGrpToChannelTable.setStatus("current")
_DsgIfTunnelGrpToChannelEntry_Object = MibTableRow
dsgIfTunnelGrpToChannelEntry = _DsgIfTunnelGrpToChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 3, 1, 1)
)
dsgIfTunnelGrpToChannelEntry.setIndexNames(
    (0, "DSG-IF-MIB", "dsgIfTunnelGrpIndex"),
    (0, "DSG-IF-MIB", "dsgIfTunnelGrpChannelIndex"),
)
if mibBuilder.loadTexts:
    dsgIfTunnelGrpToChannelEntry.setStatus("current")
_DsgIfTunnelGrpIndex_Type = Unsigned32
_DsgIfTunnelGrpIndex_Object = MibTableColumn
dsgIfTunnelGrpIndex = _DsgIfTunnelGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 3, 1, 1, 1),
    _DsgIfTunnelGrpIndex_Type()
)
dsgIfTunnelGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfTunnelGrpIndex.setStatus("current")
_DsgIfTunnelGrpChannelIndex_Type = Unsigned32
_DsgIfTunnelGrpChannelIndex_Object = MibTableColumn
dsgIfTunnelGrpChannelIndex = _DsgIfTunnelGrpChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 3, 1, 1, 2),
    _DsgIfTunnelGrpChannelIndex_Type()
)
dsgIfTunnelGrpChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfTunnelGrpChannelIndex.setStatus("current")
_DsgIfTunnelGrpDsIfIndex_Type = InterfaceIndex
_DsgIfTunnelGrpDsIfIndex_Object = MibTableColumn
dsgIfTunnelGrpDsIfIndex = _DsgIfTunnelGrpDsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 3, 1, 1, 3),
    _DsgIfTunnelGrpDsIfIndex_Type()
)
dsgIfTunnelGrpDsIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTunnelGrpDsIfIndex.setStatus("current")


class _DsgIfTunnelGrpRulePriority_Type(Unsigned32):
    """Custom type dsgIfTunnelGrpRulePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DsgIfTunnelGrpRulePriority_Type.__name__ = "Unsigned32"
_DsgIfTunnelGrpRulePriority_Object = MibTableColumn
dsgIfTunnelGrpRulePriority = _DsgIfTunnelGrpRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 3, 1, 1, 4),
    _DsgIfTunnelGrpRulePriority_Type()
)
dsgIfTunnelGrpRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTunnelGrpRulePriority.setStatus("current")


class _DsgIfTunnelGrpUcidList_Type(OctetString):
    """Custom type dsgIfTunnelGrpUcidList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsgIfTunnelGrpUcidList_Type.__name__ = "OctetString"
_DsgIfTunnelGrpUcidList_Object = MibTableColumn
dsgIfTunnelGrpUcidList = _DsgIfTunnelGrpUcidList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 3, 1, 1, 5),
    _DsgIfTunnelGrpUcidList_Type()
)
dsgIfTunnelGrpUcidList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTunnelGrpUcidList.setStatus("deprecated")


class _DsgIfTunnelGrpVendorParamId_Type(Unsigned32):
    """Custom type dsgIfTunnelGrpVendorParamId based on Unsigned32"""
    defaultValue = 0


_DsgIfTunnelGrpVendorParamId_Object = MibTableColumn
dsgIfTunnelGrpVendorParamId = _DsgIfTunnelGrpVendorParamId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 3, 1, 1, 6),
    _DsgIfTunnelGrpVendorParamId_Type()
)
dsgIfTunnelGrpVendorParamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTunnelGrpVendorParamId.setStatus("current")
_DsgIfTunnelGrpRowStatus_Type = RowStatus
_DsgIfTunnelGrpRowStatus_Object = MibTableColumn
dsgIfTunnelGrpRowStatus = _DsgIfTunnelGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 3, 1, 1, 7),
    _DsgIfTunnelGrpRowStatus_Type()
)
dsgIfTunnelGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTunnelGrpRowStatus.setStatus("current")
_DsgIfDownstreamChannel_ObjectIdentity = ObjectIdentity
dsgIfDownstreamChannel = _DsgIfDownstreamChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 4)
)
_DsgIfDownstreamTable_Object = MibTable
dsgIfDownstreamTable = _DsgIfDownstreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dsgIfDownstreamTable.setStatus("current")
_DsgIfDownstreamEntry_Object = MibTableRow
dsgIfDownstreamEntry = _DsgIfDownstreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 4, 1, 1)
)
dsgIfDownstreamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsgIfDownstreamEntry.setStatus("current")


class _DsgIfDownTimerIndex_Type(Unsigned32):
    """Custom type dsgIfDownTimerIndex based on Unsigned32"""
    defaultValue = 0


_DsgIfDownTimerIndex_Object = MibTableColumn
dsgIfDownTimerIndex = _DsgIfDownTimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 4, 1, 1, 1),
    _DsgIfDownTimerIndex_Type()
)
dsgIfDownTimerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsgIfDownTimerIndex.setStatus("current")


class _DsgIfDownVendorParamId_Type(Unsigned32):
    """Custom type dsgIfDownVendorParamId based on Unsigned32"""
    defaultValue = 0


_DsgIfDownVendorParamId_Object = MibTableColumn
dsgIfDownVendorParamId = _DsgIfDownVendorParamId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 4, 1, 1, 2),
    _DsgIfDownVendorParamId_Type()
)
dsgIfDownVendorParamId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsgIfDownVendorParamId.setStatus("current")


class _DsgIfDownChannelListIndex_Type(Unsigned32):
    """Custom type dsgIfDownChannelListIndex based on Unsigned32"""
    defaultValue = 0


_DsgIfDownChannelListIndex_Object = MibTableColumn
dsgIfDownChannelListIndex = _DsgIfDownChannelListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 4, 1, 1, 3),
    _DsgIfDownChannelListIndex_Type()
)
dsgIfDownChannelListIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsgIfDownChannelListIndex.setStatus("current")
_DsgIfDownEnableDCD_Type = TruthValue
_DsgIfDownEnableDCD_Object = MibTableColumn
dsgIfDownEnableDCD = _DsgIfDownEnableDCD_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 4, 1, 1, 4),
    _DsgIfDownEnableDCD_Type()
)
dsgIfDownEnableDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsgIfDownEnableDCD.setStatus("current")
_DsgIfDCD_ObjectIdentity = ObjectIdentity
dsgIfDCD = _DsgIfDCD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5)
)
_DsgIfClientIdTable_Object = MibTable
dsgIfClientIdTable = _DsgIfClientIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dsgIfClientIdTable.setStatus("current")
_DsgIfClientIdEntry_Object = MibTableRow
dsgIfClientIdEntry = _DsgIfClientIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 1, 1)
)
dsgIfClientIdEntry.setIndexNames(
    (0, "DSG-IF-MIB", "dsgIfClientIdListIndex"),
    (0, "DSG-IF-MIB", "dsgIfClientIdIndex"),
)
if mibBuilder.loadTexts:
    dsgIfClientIdEntry.setStatus("current")
_DsgIfClientIdListIndex_Type = Unsigned32
_DsgIfClientIdListIndex_Object = MibTableColumn
dsgIfClientIdListIndex = _DsgIfClientIdListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 1, 1, 1),
    _DsgIfClientIdListIndex_Type()
)
dsgIfClientIdListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfClientIdListIndex.setStatus("current")
_DsgIfClientIdIndex_Type = Unsigned32
_DsgIfClientIdIndex_Object = MibTableColumn
dsgIfClientIdIndex = _DsgIfClientIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 1, 1, 2),
    _DsgIfClientIdIndex_Type()
)
dsgIfClientIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfClientIdIndex.setStatus("current")


class _DsgIfClientIdType_Type(Integer32):
    """Custom type dsgIfClientIdType based on Integer32"""
    defaultValue = 1

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
        *(("applicationId", 4),
          ("broadcast", 1),
          ("caSystemId", 3),
          ("macAddress", 2))
    )


_DsgIfClientIdType_Type.__name__ = "Integer32"
_DsgIfClientIdType_Object = MibTableColumn
dsgIfClientIdType = _DsgIfClientIdType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 1, 1, 3),
    _DsgIfClientIdType_Type()
)
dsgIfClientIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClientIdType.setStatus("current")


class _DsgIfClientIdValue_Type(OctetString):
    """Custom type dsgIfClientIdValue based on OctetString"""
    defaultHexValue = "000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_DsgIfClientIdValue_Type.__name__ = "OctetString"
_DsgIfClientIdValue_Object = MibTableColumn
dsgIfClientIdValue = _DsgIfClientIdValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 1, 1, 4),
    _DsgIfClientIdValue_Type()
)
dsgIfClientIdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClientIdValue.setStatus("current")


class _DsgIfClientVendorParamId_Type(Unsigned32):
    """Custom type dsgIfClientVendorParamId based on Unsigned32"""
    defaultValue = 0


_DsgIfClientVendorParamId_Object = MibTableColumn
dsgIfClientVendorParamId = _DsgIfClientVendorParamId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 1, 1, 5),
    _DsgIfClientVendorParamId_Type()
)
dsgIfClientVendorParamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClientVendorParamId.setStatus("current")
_DsgIfClientRowStatus_Type = RowStatus
_DsgIfClientRowStatus_Object = MibTableColumn
dsgIfClientRowStatus = _DsgIfClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 1, 1, 6),
    _DsgIfClientRowStatus_Type()
)
dsgIfClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfClientRowStatus.setStatus("current")
_DsgIfVendorParamTable_Object = MibTable
dsgIfVendorParamTable = _DsgIfVendorParamTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    dsgIfVendorParamTable.setStatus("current")
_DsgIfVendorParamEntry_Object = MibTableRow
dsgIfVendorParamEntry = _DsgIfVendorParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 2, 1)
)
dsgIfVendorParamEntry.setIndexNames(
    (0, "DSG-IF-MIB", "dsgIfVendorParamId"),
    (0, "DSG-IF-MIB", "dsgIfVendorIndex"),
)
if mibBuilder.loadTexts:
    dsgIfVendorParamEntry.setStatus("current")
_DsgIfVendorParamId_Type = Unsigned32
_DsgIfVendorParamId_Object = MibTableColumn
dsgIfVendorParamId = _DsgIfVendorParamId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 2, 1, 1),
    _DsgIfVendorParamId_Type()
)
dsgIfVendorParamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfVendorParamId.setStatus("current")
_DsgIfVendorIndex_Type = Unsigned32
_DsgIfVendorIndex_Object = MibTableColumn
dsgIfVendorIndex = _DsgIfVendorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 2, 1, 2),
    _DsgIfVendorIndex_Type()
)
dsgIfVendorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfVendorIndex.setStatus("current")


class _DsgIfVendorOUI_Type(OctetString):
    """Custom type dsgIfVendorOUI based on OctetString"""
    defaultHexValue = "000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_DsgIfVendorOUI_Type.__name__ = "OctetString"
_DsgIfVendorOUI_Object = MibTableColumn
dsgIfVendorOUI = _DsgIfVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 2, 1, 3),
    _DsgIfVendorOUI_Type()
)
dsgIfVendorOUI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfVendorOUI.setStatus("current")


class _DsgIfVendorValue_Type(OctetString):
    """Custom type dsgIfVendorValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DsgIfVendorValue_Type.__name__ = "OctetString"
_DsgIfVendorValue_Object = MibTableColumn
dsgIfVendorValue = _DsgIfVendorValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 2, 1, 4),
    _DsgIfVendorValue_Type()
)
dsgIfVendorValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfVendorValue.setStatus("current")
_DsgIfVendorRowStatus_Type = RowStatus
_DsgIfVendorRowStatus_Object = MibTableColumn
dsgIfVendorRowStatus = _DsgIfVendorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 2, 1, 5),
    _DsgIfVendorRowStatus_Type()
)
dsgIfVendorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfVendorRowStatus.setStatus("current")
_DsgIfChannelListTable_Object = MibTable
dsgIfChannelListTable = _DsgIfChannelListTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    dsgIfChannelListTable.setStatus("current")
_DsgIfChannelListEntry_Object = MibTableRow
dsgIfChannelListEntry = _DsgIfChannelListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 3, 1)
)
dsgIfChannelListEntry.setIndexNames(
    (0, "DSG-IF-MIB", "dsgIfChannelListIndex"),
    (0, "DSG-IF-MIB", "dsgIfChannelIndex"),
)
if mibBuilder.loadTexts:
    dsgIfChannelListEntry.setStatus("current")
_DsgIfChannelListIndex_Type = Unsigned32
_DsgIfChannelListIndex_Object = MibTableColumn
dsgIfChannelListIndex = _DsgIfChannelListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 3, 1, 1),
    _DsgIfChannelListIndex_Type()
)
dsgIfChannelListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfChannelListIndex.setStatus("current")
_DsgIfChannelIndex_Type = Unsigned32
_DsgIfChannelIndex_Object = MibTableColumn
dsgIfChannelIndex = _DsgIfChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 3, 1, 2),
    _DsgIfChannelIndex_Type()
)
dsgIfChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfChannelIndex.setStatus("current")


class _DsgIfChannelDsFreq_Type(Integer32):
    """Custom type dsgIfChannelDsFreq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DsgIfChannelDsFreq_Type.__name__ = "Integer32"
_DsgIfChannelDsFreq_Object = MibTableColumn
dsgIfChannelDsFreq = _DsgIfChannelDsFreq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 3, 1, 3),
    _DsgIfChannelDsFreq_Type()
)
dsgIfChannelDsFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfChannelDsFreq.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfChannelDsFreq.setUnits("hertz")
_DsgIfChannelRowStatus_Type = RowStatus
_DsgIfChannelRowStatus_Object = MibTableColumn
dsgIfChannelRowStatus = _DsgIfChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 3, 1, 4),
    _DsgIfChannelRowStatus_Type()
)
dsgIfChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfChannelRowStatus.setStatus("current")
_DsgIfTimerTable_Object = MibTable
dsgIfTimerTable = _DsgIfTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 4)
)
if mibBuilder.loadTexts:
    dsgIfTimerTable.setStatus("current")
_DsgIfTimerEntry_Object = MibTableRow
dsgIfTimerEntry = _DsgIfTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 4, 1)
)
dsgIfTimerEntry.setIndexNames(
    (0, "DSG-IF-MIB", "dsgIfTimerIndex"),
)
if mibBuilder.loadTexts:
    dsgIfTimerEntry.setStatus("current")
_DsgIfTimerIndex_Type = Unsigned32
_DsgIfTimerIndex_Object = MibTableColumn
dsgIfTimerIndex = _DsgIfTimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 4, 1, 1),
    _DsgIfTimerIndex_Type()
)
dsgIfTimerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsgIfTimerIndex.setStatus("current")


class _DsgIfTimerTdsg1_Type(Unsigned32):
    """Custom type dsgIfTimerTdsg1 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsgIfTimerTdsg1_Type.__name__ = "Unsigned32"
_DsgIfTimerTdsg1_Object = MibTableColumn
dsgIfTimerTdsg1 = _DsgIfTimerTdsg1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 4, 1, 2),
    _DsgIfTimerTdsg1_Type()
)
dsgIfTimerTdsg1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTimerTdsg1.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfTimerTdsg1.setUnits("second")


class _DsgIfTimerTdsg2_Type(Unsigned32):
    """Custom type dsgIfTimerTdsg2 based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsgIfTimerTdsg2_Type.__name__ = "Unsigned32"
_DsgIfTimerTdsg2_Object = MibTableColumn
dsgIfTimerTdsg2 = _DsgIfTimerTdsg2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 4, 1, 3),
    _DsgIfTimerTdsg2_Type()
)
dsgIfTimerTdsg2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTimerTdsg2.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfTimerTdsg2.setUnits("second")


class _DsgIfTimerTdsg3_Type(Unsigned32):
    """Custom type dsgIfTimerTdsg3 based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsgIfTimerTdsg3_Type.__name__ = "Unsigned32"
_DsgIfTimerTdsg3_Object = MibTableColumn
dsgIfTimerTdsg3 = _DsgIfTimerTdsg3_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 4, 1, 4),
    _DsgIfTimerTdsg3_Type()
)
dsgIfTimerTdsg3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTimerTdsg3.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfTimerTdsg3.setUnits("second")


class _DsgIfTimerTdsg4_Type(Unsigned32):
    """Custom type dsgIfTimerTdsg4 based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsgIfTimerTdsg4_Type.__name__ = "Unsigned32"
_DsgIfTimerTdsg4_Object = MibTableColumn
dsgIfTimerTdsg4 = _DsgIfTimerTdsg4_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 4, 1, 5),
    _DsgIfTimerTdsg4_Type()
)
dsgIfTimerTdsg4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTimerTdsg4.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfTimerTdsg4.setUnits("second")
_DsgIfTimerRowStatus_Type = RowStatus
_DsgIfTimerRowStatus_Object = MibTableColumn
dsgIfTimerRowStatus = _DsgIfTimerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 5, 4, 1, 6),
    _DsgIfTimerRowStatus_Type()
)
dsgIfTimerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsgIfTimerRowStatus.setStatus("current")
_DsgIfTunnelDsStats_ObjectIdentity = ObjectIdentity
dsgIfTunnelDsStats = _DsgIfTunnelDsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 6)
)
_DsgIfTunnelDsStatsTable_Object = MibTable
dsgIfTunnelDsStatsTable = _DsgIfTunnelDsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dsgIfTunnelDsStatsTable.setStatus("current")
_DsgIfTunnelDsStatsEntry_Object = MibTableRow
dsgIfTunnelDsStatsEntry = _DsgIfTunnelDsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 6, 1, 1)
)
dsgIfTunnelDsStatsEntry.setIndexNames(
    (0, "DSG-IF-MIB", "dsgIfTunnelIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsgIfTunnelDsStatsEntry.setStatus("current")
_DsgIfTunnelDsStatsPkts_Type = Counter64
_DsgIfTunnelDsStatsPkts_Object = MibTableColumn
dsgIfTunnelDsStatsPkts = _DsgIfTunnelDsStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 6, 1, 1, 1),
    _DsgIfTunnelDsStatsPkts_Type()
)
dsgIfTunnelDsStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfTunnelDsStatsPkts.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfTunnelDsStatsPkts.setUnits("packets")
_DsgIfTunnelDsStatsOctets_Type = Counter64
_DsgIfTunnelDsStatsOctets_Object = MibTableColumn
dsgIfTunnelDsStatsOctets = _DsgIfTunnelDsStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 6, 1, 1, 2),
    _DsgIfTunnelDsStatsOctets_Type()
)
dsgIfTunnelDsStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfTunnelDsStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    dsgIfTunnelDsStatsOctets.setUnits("bytes")
_DsgIfTunnelDsStatsDsid_Type = Dsid
_DsgIfTunnelDsStatsDsid_Object = MibTableColumn
dsgIfTunnelDsStatsDsid = _DsgIfTunnelDsStatsDsid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 1, 6, 1, 1, 3),
    _DsgIfTunnelDsStatsDsid_Type()
)
dsgIfTunnelDsStatsDsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsgIfTunnelDsStatsDsid.setStatus("current")
_DsgIfMIBConformance_ObjectIdentity = ObjectIdentity
dsgIfMIBConformance = _DsgIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 2)
)
_DsgIfConformance_ObjectIdentity = ObjectIdentity
dsgIfConformance = _DsgIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 4)
)
_DsgIfGroups_ObjectIdentity = ObjectIdentity
dsgIfGroups = _DsgIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 4, 1)
)
_DsgIfCompliances_ObjectIdentity = ObjectIdentity
dsgIfCompliances = _DsgIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 4, 2)
)

# Managed Objects groups

dsgIfClassifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 4, 1, 1)
)
dsgIfClassifierGroup.setObjects(
      *(("DSG-IF-MIB", "dsgIfClassPriority"),
        ("DSG-IF-MIB", "dsgIfClassSrcIpAddrType"),
        ("DSG-IF-MIB", "dsgIfClassSrcIpAddr"),
        ("DSG-IF-MIB", "dsgIfClassSrcIpPrefixLength"),
        ("DSG-IF-MIB", "dsgIfClassDestIpAddressType"),
        ("DSG-IF-MIB", "dsgIfClassDestIpAddress"),
        ("DSG-IF-MIB", "dsgIfClassDestPortStart"),
        ("DSG-IF-MIB", "dsgIfClassDestPortEnd"),
        ("DSG-IF-MIB", "dsgIfClassRowStatus"),
        ("DSG-IF-MIB", "dsgIfClassIncludeInDCD"))
)
if mibBuilder.loadTexts:
    dsgIfClassifierGroup.setStatus("current")

dsgIfBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 4, 1, 2)
)
dsgIfBaseGroup.setObjects(
      *(("DSG-IF-MIB", "dsgIfTunnelGroupIndex"),
        ("DSG-IF-MIB", "dsgIfTunnelClientIdListIndex"),
        ("DSG-IF-MIB", "dsgIfTunnelMacAddress"),
        ("DSG-IF-MIB", "dsgIfTunnelServiceClassName"),
        ("DSG-IF-MIB", "dsgIfTunnelRowStatus"),
        ("DSG-IF-MIB", "dsgIfTunnelGrpDsIfIndex"),
        ("DSG-IF-MIB", "dsgIfTunnelGrpRulePriority"),
        ("DSG-IF-MIB", "dsgIfTunnelGrpVendorParamId"),
        ("DSG-IF-MIB", "dsgIfTunnelGrpRowStatus"),
        ("DSG-IF-MIB", "dsgIfDownTimerIndex"),
        ("DSG-IF-MIB", "dsgIfDownVendorParamId"),
        ("DSG-IF-MIB", "dsgIfDownChannelListIndex"),
        ("DSG-IF-MIB", "dsgIfDownEnableDCD"))
)
if mibBuilder.loadTexts:
    dsgIfBaseGroup.setStatus("current")

dsgIfDCDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 4, 1, 3)
)
dsgIfDCDGroup.setObjects(
      *(("DSG-IF-MIB", "dsgIfClientIdType"),
        ("DSG-IF-MIB", "dsgIfClientIdValue"),
        ("DSG-IF-MIB", "dsgIfClientVendorParamId"),
        ("DSG-IF-MIB", "dsgIfClientRowStatus"),
        ("DSG-IF-MIB", "dsgIfVendorOUI"),
        ("DSG-IF-MIB", "dsgIfVendorValue"),
        ("DSG-IF-MIB", "dsgIfVendorRowStatus"),
        ("DSG-IF-MIB", "dsgIfChannelDsFreq"),
        ("DSG-IF-MIB", "dsgIfChannelRowStatus"),
        ("DSG-IF-MIB", "dsgIfTimerTdsg1"),
        ("DSG-IF-MIB", "dsgIfTimerTdsg2"),
        ("DSG-IF-MIB", "dsgIfTimerTdsg3"),
        ("DSG-IF-MIB", "dsgIfTimerTdsg4"),
        ("DSG-IF-MIB", "dsgIfTimerRowStatus"))
)
if mibBuilder.loadTexts:
    dsgIfDCDGroup.setStatus("current")

dsgIfDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 4, 1, 4)
)
dsgIfDeprecatedGroup.setObjects(
    ("DSG-IF-MIB", "dsgIfTunnelGrpUcidList")
)
if mibBuilder.loadTexts:
    dsgIfDeprecatedGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dsgIfBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dsgIfBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSG-IF-MIB",
    **{"dsgIfMIB": dsgIfMIB,
       "dsgIfMIBNotifications": dsgIfMIBNotifications,
       "dsgIfMIBObjects": dsgIfMIBObjects,
       "dsgIfClassifier": dsgIfClassifier,
       "dsgIfClassifierTable": dsgIfClassifierTable,
       "dsgIfClassifierEntry": dsgIfClassifierEntry,
       "dsgIfClassId": dsgIfClassId,
       "dsgIfClassPriority": dsgIfClassPriority,
       "dsgIfClassSrcIpAddrType": dsgIfClassSrcIpAddrType,
       "dsgIfClassSrcIpAddr": dsgIfClassSrcIpAddr,
       "dsgIfClassSrcIpPrefixLength": dsgIfClassSrcIpPrefixLength,
       "dsgIfClassDestIpAddressType": dsgIfClassDestIpAddressType,
       "dsgIfClassDestIpAddress": dsgIfClassDestIpAddress,
       "dsgIfClassDestPortStart": dsgIfClassDestPortStart,
       "dsgIfClassDestPortEnd": dsgIfClassDestPortEnd,
       "dsgIfClassRowStatus": dsgIfClassRowStatus,
       "dsgIfClassIncludeInDCD": dsgIfClassIncludeInDCD,
       "dsgIfTunnel": dsgIfTunnel,
       "dsgIfTunnelTable": dsgIfTunnelTable,
       "dsgIfTunnelEntry": dsgIfTunnelEntry,
       "dsgIfTunnelIndex": dsgIfTunnelIndex,
       "dsgIfTunnelGroupIndex": dsgIfTunnelGroupIndex,
       "dsgIfTunnelClientIdListIndex": dsgIfTunnelClientIdListIndex,
       "dsgIfTunnelMacAddress": dsgIfTunnelMacAddress,
       "dsgIfTunnelServiceClassName": dsgIfTunnelServiceClassName,
       "dsgIfTunnelRowStatus": dsgIfTunnelRowStatus,
       "dsgIfTunnelGrpToChannel": dsgIfTunnelGrpToChannel,
       "dsgIfTunnelGrpToChannelTable": dsgIfTunnelGrpToChannelTable,
       "dsgIfTunnelGrpToChannelEntry": dsgIfTunnelGrpToChannelEntry,
       "dsgIfTunnelGrpIndex": dsgIfTunnelGrpIndex,
       "dsgIfTunnelGrpChannelIndex": dsgIfTunnelGrpChannelIndex,
       "dsgIfTunnelGrpDsIfIndex": dsgIfTunnelGrpDsIfIndex,
       "dsgIfTunnelGrpRulePriority": dsgIfTunnelGrpRulePriority,
       "dsgIfTunnelGrpUcidList": dsgIfTunnelGrpUcidList,
       "dsgIfTunnelGrpVendorParamId": dsgIfTunnelGrpVendorParamId,
       "dsgIfTunnelGrpRowStatus": dsgIfTunnelGrpRowStatus,
       "dsgIfDownstreamChannel": dsgIfDownstreamChannel,
       "dsgIfDownstreamTable": dsgIfDownstreamTable,
       "dsgIfDownstreamEntry": dsgIfDownstreamEntry,
       "dsgIfDownTimerIndex": dsgIfDownTimerIndex,
       "dsgIfDownVendorParamId": dsgIfDownVendorParamId,
       "dsgIfDownChannelListIndex": dsgIfDownChannelListIndex,
       "dsgIfDownEnableDCD": dsgIfDownEnableDCD,
       "dsgIfDCD": dsgIfDCD,
       "dsgIfClientIdTable": dsgIfClientIdTable,
       "dsgIfClientIdEntry": dsgIfClientIdEntry,
       "dsgIfClientIdListIndex": dsgIfClientIdListIndex,
       "dsgIfClientIdIndex": dsgIfClientIdIndex,
       "dsgIfClientIdType": dsgIfClientIdType,
       "dsgIfClientIdValue": dsgIfClientIdValue,
       "dsgIfClientVendorParamId": dsgIfClientVendorParamId,
       "dsgIfClientRowStatus": dsgIfClientRowStatus,
       "dsgIfVendorParamTable": dsgIfVendorParamTable,
       "dsgIfVendorParamEntry": dsgIfVendorParamEntry,
       "dsgIfVendorParamId": dsgIfVendorParamId,
       "dsgIfVendorIndex": dsgIfVendorIndex,
       "dsgIfVendorOUI": dsgIfVendorOUI,
       "dsgIfVendorValue": dsgIfVendorValue,
       "dsgIfVendorRowStatus": dsgIfVendorRowStatus,
       "dsgIfChannelListTable": dsgIfChannelListTable,
       "dsgIfChannelListEntry": dsgIfChannelListEntry,
       "dsgIfChannelListIndex": dsgIfChannelListIndex,
       "dsgIfChannelIndex": dsgIfChannelIndex,
       "dsgIfChannelDsFreq": dsgIfChannelDsFreq,
       "dsgIfChannelRowStatus": dsgIfChannelRowStatus,
       "dsgIfTimerTable": dsgIfTimerTable,
       "dsgIfTimerEntry": dsgIfTimerEntry,
       "dsgIfTimerIndex": dsgIfTimerIndex,
       "dsgIfTimerTdsg1": dsgIfTimerTdsg1,
       "dsgIfTimerTdsg2": dsgIfTimerTdsg2,
       "dsgIfTimerTdsg3": dsgIfTimerTdsg3,
       "dsgIfTimerTdsg4": dsgIfTimerTdsg4,
       "dsgIfTimerRowStatus": dsgIfTimerRowStatus,
       "dsgIfTunnelDsStats": dsgIfTunnelDsStats,
       "dsgIfTunnelDsStatsTable": dsgIfTunnelDsStatsTable,
       "dsgIfTunnelDsStatsEntry": dsgIfTunnelDsStatsEntry,
       "dsgIfTunnelDsStatsPkts": dsgIfTunnelDsStatsPkts,
       "dsgIfTunnelDsStatsOctets": dsgIfTunnelDsStatsOctets,
       "dsgIfTunnelDsStatsDsid": dsgIfTunnelDsStatsDsid,
       "dsgIfMIBConformance": dsgIfMIBConformance,
       "dsgIfConformance": dsgIfConformance,
       "dsgIfGroups": dsgIfGroups,
       "dsgIfClassifierGroup": dsgIfClassifierGroup,
       "dsgIfBaseGroup": dsgIfBaseGroup,
       "dsgIfDCDGroup": dsgIfDCDGroup,
       "dsgIfDeprecatedGroup": dsgIfDeprecatedGroup,
       "dsgIfCompliances": dsgIfCompliances,
       "dsgIfBasicCompliance": dsgIfBasicCompliance}
)
