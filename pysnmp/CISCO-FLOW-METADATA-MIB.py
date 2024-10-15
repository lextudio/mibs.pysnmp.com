# SNMP MIB module (CISCO-FLOW-METADATA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FLOW-METADATA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:39 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoFlowMetadataMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 789)
)
ciscoFlowMetadataMIB.setRevisions(
        ("2012-12-17 00:00",
         "2011-03-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CfmMetadataFlowAttributeType(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              94,
              95,
              96,
              97,
              98,
              100,
              101,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              134,
              135,
              136,
              137,
              138,
              139)
        )
    )
    namedValues = NamedValues(
        *(("appDescription", 94),
          ("appName", 96),
          ("appTag", 95),
          ("appVendor", 98),
          ("appVersion", 97),
          ("audioCodec", 128),
          ("bandwidth", 123),
          ("bandwidthConsumed", 129),
          ("cname", 134),
          ("deviceClass", 125),
          ("deviceName", 124),
          ("domainName", 137),
          ("endpointIPAddressLength", 118),
          ("endpointIPAddressType", 117),
          ("endpointIPAddressValue", 119),
          ("endpointModel", 113),
          ("endpointSwVersion", 138),
          ("endpointVendor", 114),
          ("endpointVersion", 115),
          ("extrapolatedBandwidth", 132),
          ("globalSessionID", 107),
          ("l3Bitrate", 104),
          ("mediaBitrate", 105),
          ("mediaEncryptionStatus", 110),
          ("mediaVideoPaksize", 106),
          ("meteringPriority", 112),
          ("mimeType", 131),
          ("multipartySessionID", 108),
          ("other", 0),
          ("pakRate", 103),
          ("payloadType", 130),
          ("rtpMediaFlow", 109),
          ("sdpSessionID", 136),
          ("sipEmail", 127),
          ("sipProxyServerLength", 121),
          ("sipProxyServerType", 120),
          ("sipProxyServerValue", 122),
          ("sipUserName", 126),
          ("ssrc", 116),
          ("syntheticTraffic", 111),
          ("tosDscp", 139),
          ("videoCodec", 135),
          ("vmFlowTimeout", 100),
          ("vmRTPClockFrequency", 101))
    )



class CfmMetadataFlowAttrVal(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CFlowMetadataMIBNotifs_ObjectIdentity = ObjectIdentity
cFlowMetadataMIBNotifs = _CFlowMetadataMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 0)
)
_CFlowMetadataMIBObjects_ObjectIdentity = ObjectIdentity
cFlowMetadataMIBObjects = _CFlowMetadataMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1)
)
_CfmMetadataFlowTable_Object = MibTable
cfmMetadataFlowTable = _CfmMetadataFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1)
)
if mibBuilder.loadTexts:
    cfmMetadataFlowTable.setStatus("current")
_CfmMetadataFlowEntry_Object = MibTableRow
cfmMetadataFlowEntry = _CfmMetadataFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1)
)
cfmMetadataFlowEntry.setIndexNames(
    (0, "CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowId"),
)
if mibBuilder.loadTexts:
    cfmMetadataFlowEntry.setStatus("current")
_CfmMetadataFlowId_Type = Unsigned32
_CfmMetadataFlowId_Object = MibTableColumn
cfmMetadataFlowId = _CfmMetadataFlowId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 1),
    _CfmMetadataFlowId_Type()
)
cfmMetadataFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmMetadataFlowId.setStatus("current")


class _CfmMetadataFlowProtocolType_Type(Integer32):
    """Custom type cfmMetadataFlowProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_CfmMetadataFlowProtocolType_Type.__name__ = "Integer32"
_CfmMetadataFlowProtocolType_Object = MibTableColumn
cfmMetadataFlowProtocolType = _CfmMetadataFlowProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 2),
    _CfmMetadataFlowProtocolType_Type()
)
cfmMetadataFlowProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMetadataFlowProtocolType.setStatus("current")
_CfmMetadataFlowDestAddrType_Type = InetAddressType
_CfmMetadataFlowDestAddrType_Object = MibTableColumn
cfmMetadataFlowDestAddrType = _CfmMetadataFlowDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 3),
    _CfmMetadataFlowDestAddrType_Type()
)
cfmMetadataFlowDestAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMetadataFlowDestAddrType.setStatus("current")
_CfmMetadataFlowDestAddr_Type = InetAddress
_CfmMetadataFlowDestAddr_Object = MibTableColumn
cfmMetadataFlowDestAddr = _CfmMetadataFlowDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 4),
    _CfmMetadataFlowDestAddr_Type()
)
cfmMetadataFlowDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMetadataFlowDestAddr.setStatus("current")
_CfmMetadataFlowDestPort_Type = InetPortNumber
_CfmMetadataFlowDestPort_Object = MibTableColumn
cfmMetadataFlowDestPort = _CfmMetadataFlowDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 5),
    _CfmMetadataFlowDestPort_Type()
)
cfmMetadataFlowDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMetadataFlowDestPort.setStatus("current")
_CfmMetadataFlowSrcAddrType_Type = InetAddressType
_CfmMetadataFlowSrcAddrType_Object = MibTableColumn
cfmMetadataFlowSrcAddrType = _CfmMetadataFlowSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 6),
    _CfmMetadataFlowSrcAddrType_Type()
)
cfmMetadataFlowSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMetadataFlowSrcAddrType.setStatus("current")
_CfmMetadataFlowSrcAddr_Type = InetAddress
_CfmMetadataFlowSrcAddr_Object = MibTableColumn
cfmMetadataFlowSrcAddr = _CfmMetadataFlowSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 7),
    _CfmMetadataFlowSrcAddr_Type()
)
cfmMetadataFlowSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMetadataFlowSrcAddr.setStatus("current")
_CfmMetadataFlowSrcPort_Type = InetPortNumber
_CfmMetadataFlowSrcPort_Object = MibTableColumn
cfmMetadataFlowSrcPort = _CfmMetadataFlowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 8),
    _CfmMetadataFlowSrcPort_Type()
)
cfmMetadataFlowSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMetadataFlowSrcPort.setStatus("current")


class _CfmMetadataFlowSSRC_Type(Unsigned32):
    """Custom type cfmMetadataFlowSSRC based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CfmMetadataFlowSSRC_Type.__name__ = "Unsigned32"
_CfmMetadataFlowSSRC_Object = MibTableColumn
cfmMetadataFlowSSRC = _CfmMetadataFlowSSRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 9),
    _CfmMetadataFlowSSRC_Type()
)
cfmMetadataFlowSSRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMetadataFlowSSRC.setStatus("current")
_CfmMetadataFlowAttrTable_Object = MibTable
cfmMetadataFlowAttrTable = _CfmMetadataFlowAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 2)
)
if mibBuilder.loadTexts:
    cfmMetadataFlowAttrTable.setStatus("deprecated")
_CfmMetadataFlowAttrEntry_Object = MibTableRow
cfmMetadataFlowAttrEntry = _CfmMetadataFlowAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 2, 1)
)
cfmMetadataFlowAttrEntry.setIndexNames(
    (0, "CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowId"),
    (0, "CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowAttrType"),
)
if mibBuilder.loadTexts:
    cfmMetadataFlowAttrEntry.setStatus("deprecated")
_CfmMetadataFlowAttrType_Type = CfmMetadataFlowAttributeType
_CfmMetadataFlowAttrType_Object = MibTableColumn
cfmMetadataFlowAttrType = _CfmMetadataFlowAttrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 2, 1, 1),
    _CfmMetadataFlowAttrType_Type()
)
cfmMetadataFlowAttrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMetadataFlowAttrType.setStatus("deprecated")
_CfmMetadataFlowAttrValue_Type = CfmMetadataFlowAttrVal
_CfmMetadataFlowAttrValue_Object = MibTableColumn
cfmMetadataFlowAttrValue = _CfmMetadataFlowAttrValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 2, 1, 2),
    _CfmMetadataFlowAttrValue_Type()
)
cfmMetadataFlowAttrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMetadataFlowAttrValue.setStatus("deprecated")
_CfmMetadataFlowAllAttrTable_Object = MibTable
cfmMetadataFlowAllAttrTable = _CfmMetadataFlowAllAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 3)
)
if mibBuilder.loadTexts:
    cfmMetadataFlowAllAttrTable.setStatus("current")
_CfmMetadataFlowAllAttrEntry_Object = MibTableRow
cfmMetadataFlowAllAttrEntry = _CfmMetadataFlowAllAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 3, 1)
)
cfmMetadataFlowAllAttrEntry.setIndexNames(
    (0, "CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowId"),
    (0, "CISCO-FLOW-METADATA-MIB", "cfmMetadataIpFixIeId"),
    (0, "CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowAllAttrInstanceId"),
)
if mibBuilder.loadTexts:
    cfmMetadataFlowAllAttrEntry.setStatus("current")


class _CfmMetadataIpFixIeId_Type(Unsigned32):
    """Custom type cfmMetadataIpFixIeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfmMetadataIpFixIeId_Type.__name__ = "Unsigned32"
_CfmMetadataIpFixIeId_Object = MibTableColumn
cfmMetadataIpFixIeId = _CfmMetadataIpFixIeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 3, 1, 1),
    _CfmMetadataIpFixIeId_Type()
)
cfmMetadataIpFixIeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmMetadataIpFixIeId.setStatus("current")


class _CfmMetadataFlowAllAttrInstanceId_Type(Unsigned32):
    """Custom type cfmMetadataFlowAllAttrInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CfmMetadataFlowAllAttrInstanceId_Type.__name__ = "Unsigned32"
_CfmMetadataFlowAllAttrInstanceId_Object = MibTableColumn
cfmMetadataFlowAllAttrInstanceId = _CfmMetadataFlowAllAttrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 3, 1, 2),
    _CfmMetadataFlowAllAttrInstanceId_Type()
)
cfmMetadataFlowAllAttrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmMetadataFlowAllAttrInstanceId.setStatus("current")


class _CfmMetadataFlowAllAttrValue_Type(OctetString):
    """Custom type cfmMetadataFlowAllAttrValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfmMetadataFlowAllAttrValue_Type.__name__ = "OctetString"
_CfmMetadataFlowAllAttrValue_Object = MibTableColumn
cfmMetadataFlowAllAttrValue = _CfmMetadataFlowAllAttrValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 3, 1, 3),
    _CfmMetadataFlowAllAttrValue_Type()
)
cfmMetadataFlowAllAttrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMetadataFlowAllAttrValue.setStatus("current")


class _CfmMetadataFlowAllAttrPen_Type(Unsigned32):
    """Custom type cfmMetadataFlowAllAttrPen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CfmMetadataFlowAllAttrPen_Type.__name__ = "Unsigned32"
_CfmMetadataFlowAllAttrPen_Object = MibTableColumn
cfmMetadataFlowAllAttrPen = _CfmMetadataFlowAllAttrPen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 3, 1, 4),
    _CfmMetadataFlowAllAttrPen_Type()
)
cfmMetadataFlowAllAttrPen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMetadataFlowAllAttrPen.setStatus("current")
_CFlowMetadataMIBConform_ObjectIdentity = ObjectIdentity
cFlowMetadataMIBConform = _CFlowMetadataMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 2)
)
_CfmMetadataMIBCompliances_ObjectIdentity = ObjectIdentity
cfmMetadataMIBCompliances = _CfmMetadataMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 2, 1)
)
_CfmMetadataMIBGroups_ObjectIdentity = ObjectIdentity
cfmMetadataMIBGroups = _CfmMetadataMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 2, 2)
)

# Managed Objects groups

cfmMetadateFlowInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 2, 2, 1)
)
cfmMetadateFlowInfoGroup.setObjects(
      *(("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowProtocolType"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowDestAddrType"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowDestAddr"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowDestPort"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSrcAddrType"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSrcAddr"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSrcPort"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSSRC"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowAttrType"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowAttrValue"))
)
if mibBuilder.loadTexts:
    cfmMetadateFlowInfoGroup.setStatus("deprecated")

cfmMetadateFlowInfoGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 2, 2, 2)
)
cfmMetadateFlowInfoGroupV2.setObjects(
      *(("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowProtocolType"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowDestAddrType"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowDestAddr"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowDestPort"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSrcAddrType"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSrcAddr"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSrcPort"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSSRC"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowAllAttrValue"),
        ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowAllAttrPen"))
)
if mibBuilder.loadTexts:
    cfmMetadateFlowInfoGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cfmMetadataMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cfmMetadataMIBCompliance.setStatus(
        "deprecated"
    )

cfmMetadataMIBComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 789, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cfmMetadataMIBComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FLOW-METADATA-MIB",
    **{"CfmMetadataFlowAttributeType": CfmMetadataFlowAttributeType,
       "CfmMetadataFlowAttrVal": CfmMetadataFlowAttrVal,
       "ciscoFlowMetadataMIB": ciscoFlowMetadataMIB,
       "cFlowMetadataMIBNotifs": cFlowMetadataMIBNotifs,
       "cFlowMetadataMIBObjects": cFlowMetadataMIBObjects,
       "cfmMetadataFlowTable": cfmMetadataFlowTable,
       "cfmMetadataFlowEntry": cfmMetadataFlowEntry,
       "cfmMetadataFlowId": cfmMetadataFlowId,
       "cfmMetadataFlowProtocolType": cfmMetadataFlowProtocolType,
       "cfmMetadataFlowDestAddrType": cfmMetadataFlowDestAddrType,
       "cfmMetadataFlowDestAddr": cfmMetadataFlowDestAddr,
       "cfmMetadataFlowDestPort": cfmMetadataFlowDestPort,
       "cfmMetadataFlowSrcAddrType": cfmMetadataFlowSrcAddrType,
       "cfmMetadataFlowSrcAddr": cfmMetadataFlowSrcAddr,
       "cfmMetadataFlowSrcPort": cfmMetadataFlowSrcPort,
       "cfmMetadataFlowSSRC": cfmMetadataFlowSSRC,
       "cfmMetadataFlowAttrTable": cfmMetadataFlowAttrTable,
       "cfmMetadataFlowAttrEntry": cfmMetadataFlowAttrEntry,
       "cfmMetadataFlowAttrType": cfmMetadataFlowAttrType,
       "cfmMetadataFlowAttrValue": cfmMetadataFlowAttrValue,
       "cfmMetadataFlowAllAttrTable": cfmMetadataFlowAllAttrTable,
       "cfmMetadataFlowAllAttrEntry": cfmMetadataFlowAllAttrEntry,
       "cfmMetadataIpFixIeId": cfmMetadataIpFixIeId,
       "cfmMetadataFlowAllAttrInstanceId": cfmMetadataFlowAllAttrInstanceId,
       "cfmMetadataFlowAllAttrValue": cfmMetadataFlowAllAttrValue,
       "cfmMetadataFlowAllAttrPen": cfmMetadataFlowAllAttrPen,
       "cFlowMetadataMIBConform": cFlowMetadataMIBConform,
       "cfmMetadataMIBCompliances": cfmMetadataMIBCompliances,
       "cfmMetadataMIBCompliance": cfmMetadataMIBCompliance,
       "cfmMetadataMIBComplianceV2": cfmMetadataMIBComplianceV2,
       "cfmMetadataMIBGroups": cfmMetadataMIBGroups,
       "cfmMetadateFlowInfoGroup": cfmMetadateFlowInfoGroup,
       "cfmMetadateFlowInfoGroupV2": cfmMetadateFlowInfoGroupV2}
)
