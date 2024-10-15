# SNMP MIB module (CISCO-WAN-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-TOPOLOGY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:23 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PnniNodeId,) = mibBuilder.importSymbols(
    "PNNI-MIB",
    "PnniNodeId")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoWanTopologyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 234)
)
ciscoWanTopologyMIB.setRevisions(
        ("2002-07-16 00:00",
         "2002-05-20 00:00",
         "2002-04-22 00:00",
         "2001-12-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CwtNodeInfoTableIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoWanTopologyMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWanTopologyMIBNotifs = _CiscoWanTopologyMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 0)
)
_CiscoWanTopologyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanTopologyMIBObjects = _CiscoWanTopologyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1)
)
_CwtSystemGroup_ObjectIdentity = ObjectIdentity
cwtSystemGroup = _CwtSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 1)
)


class _CwtGatewayAdminStatus_Type(Integer32):
    """Custom type cwtGatewayAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CwtGatewayAdminStatus_Type.__name__ = "Integer32"
_CwtGatewayAdminStatus_Object = MibScalar
cwtGatewayAdminStatus = _CwtGatewayAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 1, 1),
    _CwtGatewayAdminStatus_Type()
)
cwtGatewayAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwtGatewayAdminStatus.setStatus("current")


class _CwtGatewayNodeOperStatus_Type(Integer32):
    """Custom type cwtGatewayNodeOperStatus based on Integer32"""
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
        *(("disabled", 1),
          ("disabling", 3),
          ("enabled", 2),
          ("enabledAndFull", 5),
          ("enabling", 4))
    )


_CwtGatewayNodeOperStatus_Type.__name__ = "Integer32"
_CwtGatewayNodeOperStatus_Object = MibScalar
cwtGatewayNodeOperStatus = _CwtGatewayNodeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 1, 2),
    _CwtGatewayNodeOperStatus_Type()
)
cwtGatewayNodeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtGatewayNodeOperStatus.setStatus("current")
_CwtDBLastChange_Type = TimeStamp
_CwtDBLastChange_Object = MibScalar
cwtDBLastChange = _CwtDBLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 1, 3),
    _CwtDBLastChange_Type()
)
cwtDBLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtDBLastChange.setStatus("current")
_CwtNodalInfoGroup_ObjectIdentity = ObjectIdentity
cwtNodalInfoGroup = _CwtNodalInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2)
)
_CwtNodeInfoTable_Object = MibTable
cwtNodeInfoTable = _CwtNodeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwtNodeInfoTable.setStatus("current")
_CwtNodeInfoEntry_Object = MibTableRow
cwtNodeInfoEntry = _CwtNodeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1)
)
cwtNodeInfoEntry.setIndexNames(
    (0, "CISCO-WAN-TOPOLOGY-MIB", "cwtIndex"),
)
if mibBuilder.loadTexts:
    cwtNodeInfoEntry.setStatus("current")
_CwtIndex_Type = CwtNodeInfoTableIndex
_CwtIndex_Object = MibTableColumn
cwtIndex = _CwtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 1),
    _CwtIndex_Type()
)
cwtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwtIndex.setStatus("current")
_CwtGatewayNodeFlag_Type = TruthValue
_CwtGatewayNodeFlag_Object = MibTableColumn
cwtGatewayNodeFlag = _CwtGatewayNodeFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 2),
    _CwtGatewayNodeFlag_Type()
)
cwtGatewayNodeFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtGatewayNodeFlag.setStatus("current")
_CwtNodeId_Type = PnniNodeId
_CwtNodeId_Object = MibTableColumn
cwtNodeId = _CwtNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 3),
    _CwtNodeId_Type()
)
cwtNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtNodeId.setStatus("current")
_CwtNodeName_Type = SnmpAdminString
_CwtNodeName_Object = MibTableColumn
cwtNodeName = _CwtNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 4),
    _CwtNodeName_Type()
)
cwtNodeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtNodeName.setStatus("current")
_CwtPrimIPIfType_Type = IANAifType
_CwtPrimIPIfType_Object = MibTableColumn
cwtPrimIPIfType = _CwtPrimIPIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 5),
    _CwtPrimIPIfType_Type()
)
cwtPrimIPIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtPrimIPIfType.setStatus("current")
_CwtPrimIPIfName_Type = SnmpAdminString
_CwtPrimIPIfName_Object = MibTableColumn
cwtPrimIPIfName = _CwtPrimIPIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 6),
    _CwtPrimIPIfName_Type()
)
cwtPrimIPIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtPrimIPIfName.setStatus("current")
_CwtPrimIPAddrType_Type = InetAddressType
_CwtPrimIPAddrType_Object = MibTableColumn
cwtPrimIPAddrType = _CwtPrimIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 7),
    _CwtPrimIPAddrType_Type()
)
cwtPrimIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtPrimIPAddrType.setStatus("current")
_CwtPrimIP_Type = InetAddress
_CwtPrimIP_Object = MibTableColumn
cwtPrimIP = _CwtPrimIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 8),
    _CwtPrimIP_Type()
)
cwtPrimIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtPrimIP.setStatus("current")
_CwtSecIPIfType_Type = IANAifType
_CwtSecIPIfType_Object = MibTableColumn
cwtSecIPIfType = _CwtSecIPIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 9),
    _CwtSecIPIfType_Type()
)
cwtSecIPIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtSecIPIfType.setStatus("current")
_CwtSecIPIfName_Type = SnmpAdminString
_CwtSecIPIfName_Object = MibTableColumn
cwtSecIPIfName = _CwtSecIPIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 10),
    _CwtSecIPIfName_Type()
)
cwtSecIPIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtSecIPIfName.setStatus("current")
_CwtSecIPAddrType_Type = InetAddressType
_CwtSecIPAddrType_Object = MibTableColumn
cwtSecIPAddrType = _CwtSecIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 11),
    _CwtSecIPAddrType_Type()
)
cwtSecIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtSecIPAddrType.setStatus("current")
_CwtSecIP_Type = InetAddress
_CwtSecIP_Object = MibTableColumn
cwtSecIP = _CwtSecIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 12),
    _CwtSecIP_Type()
)
cwtSecIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtSecIP.setStatus("current")
_CwtSysObjId_Type = ObjectIdentifier
_CwtSysObjId_Object = MibTableColumn
cwtSysObjId = _CwtSysObjId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 13),
    _CwtSysObjId_Type()
)
cwtSysObjId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtSysObjId.setStatus("current")
_CwtNodeInfoTimeOutFlag_Type = TruthValue
_CwtNodeInfoTimeOutFlag_Object = MibTableColumn
cwtNodeInfoTimeOutFlag = _CwtNodeInfoTimeOutFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 14),
    _CwtNodeInfoTimeOutFlag_Type()
)
cwtNodeInfoTimeOutFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtNodeInfoTimeOutFlag.setStatus("current")
_CwtRowStatus_Type = RowStatus
_CwtRowStatus_Object = MibTableColumn
cwtRowStatus = _CwtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 2, 1, 1, 15),
    _CwtRowStatus_Type()
)
cwtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtRowStatus.setStatus("current")
_CwtFeederInfoGroup_ObjectIdentity = ObjectIdentity
cwtFeederInfoGroup = _CwtFeederInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3)
)
_CwtFeederInfoTable_Object = MibTable
cwtFeederInfoTable = _CwtFeederInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwtFeederInfoTable.setStatus("current")
_CwtFeederInfoEntry_Object = MibTableRow
cwtFeederInfoEntry = _CwtFeederInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1)
)
cwtFeederInfoEntry.setIndexNames(
    (0, "CISCO-WAN-TOPOLOGY-MIB", "cwtFeederIndex"),
)
if mibBuilder.loadTexts:
    cwtFeederInfoEntry.setStatus("current")
_CwtFeederIndex_Type = Integer32
_CwtFeederIndex_Object = MibTableColumn
cwtFeederIndex = _CwtFeederIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 1),
    _CwtFeederIndex_Type()
)
cwtFeederIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwtFeederIndex.setStatus("current")
_CwtLocalNodeId_Type = PnniNodeId
_CwtLocalNodeId_Object = MibTableColumn
cwtLocalNodeId = _CwtLocalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 2),
    _CwtLocalNodeId_Type()
)
cwtLocalNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtLocalNodeId.setStatus("current")
_CwtLocalIfIndex_Type = InterfaceIndex
_CwtLocalIfIndex_Object = MibTableColumn
cwtLocalIfIndex = _CwtLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 3),
    _CwtLocalIfIndex_Type()
)
cwtLocalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtLocalIfIndex.setStatus("current")
_CwtLocalIfName_Type = SnmpAdminString
_CwtLocalIfName_Object = MibTableColumn
cwtLocalIfName = _CwtLocalIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 4),
    _CwtLocalIfName_Type()
)
cwtLocalIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtLocalIfName.setStatus("current")


class _CwtFeederShelf_Type(Integer32):
    """Custom type cwtFeederShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CwtFeederShelf_Type.__name__ = "Integer32"
_CwtFeederShelf_Object = MibTableColumn
cwtFeederShelf = _CwtFeederShelf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 5),
    _CwtFeederShelf_Type()
)
cwtFeederShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtFeederShelf.setStatus("current")


class _CwtFeederSlot_Type(Integer32):
    """Custom type cwtFeederSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CwtFeederSlot_Type.__name__ = "Integer32"
_CwtFeederSlot_Object = MibTableColumn
cwtFeederSlot = _CwtFeederSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 6),
    _CwtFeederSlot_Type()
)
cwtFeederSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtFeederSlot.setStatus("current")


class _CwtFeederPort_Type(Integer32):
    """Custom type cwtFeederPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CwtFeederPort_Type.__name__ = "Integer32"
_CwtFeederPort_Object = MibTableColumn
cwtFeederPort = _CwtFeederPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 7),
    _CwtFeederPort_Type()
)
cwtFeederPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtFeederPort.setStatus("current")


class _CwtFeederLMIType_Type(Integer32):
    """Custom type cwtFeederLMIType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("feeder", 1),
          ("xLMI", 2))
    )


_CwtFeederLMIType_Type.__name__ = "Integer32"
_CwtFeederLMIType_Object = MibTableColumn
cwtFeederLMIType = _CwtFeederLMIType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 8),
    _CwtFeederLMIType_Type()
)
cwtFeederLMIType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtFeederLMIType.setStatus("current")


class _CwtFeederType_Type(Integer32):
    """Custom type cwtFeederType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("fdrAPS", 7),
          ("fdrBASIS", 4),
          ("fdrBPX", 2),
          ("fdrIGX", 8),
          ("fdrIPX", 1),
          ("fdrIgxAF", 9),
          ("fdrIpxAF", 3),
          ("fdrNON", 12),
          ("fdrPAR", 11),
          ("fdrUNI", 6),
          ("fdrUNKNOWN", 5),
          ("fdrVSI", 10))
    )


_CwtFeederType_Type.__name__ = "Integer32"
_CwtFeederType_Object = MibTableColumn
cwtFeederType = _CwtFeederType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 9),
    _CwtFeederType_Type()
)
cwtFeederType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtFeederType.setStatus("current")
_CwtFeederName_Type = SnmpAdminString
_CwtFeederName_Object = MibTableColumn
cwtFeederName = _CwtFeederName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 10),
    _CwtFeederName_Type()
)
cwtFeederName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtFeederName.setStatus("current")
_CwtFeederLanIPAddrType_Type = InetAddressType
_CwtFeederLanIPAddrType_Object = MibTableColumn
cwtFeederLanIPAddrType = _CwtFeederLanIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 11),
    _CwtFeederLanIPAddrType_Type()
)
cwtFeederLanIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtFeederLanIPAddrType.setStatus("current")
_CwtFeederLanIP_Type = InetAddress
_CwtFeederLanIP_Object = MibTableColumn
cwtFeederLanIP = _CwtFeederLanIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 12),
    _CwtFeederLanIP_Type()
)
cwtFeederLanIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtFeederLanIP.setStatus("current")
_CwtFeederAtmIPAddrType_Type = InetAddressType
_CwtFeederAtmIPAddrType_Object = MibTableColumn
cwtFeederAtmIPAddrType = _CwtFeederAtmIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 13),
    _CwtFeederAtmIPAddrType_Type()
)
cwtFeederAtmIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtFeederAtmIPAddrType.setStatus("current")
_CwtFeederAtmIP_Type = InetAddress
_CwtFeederAtmIP_Object = MibTableColumn
cwtFeederAtmIP = _CwtFeederAtmIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 14),
    _CwtFeederAtmIP_Type()
)
cwtFeederAtmIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtFeederAtmIP.setStatus("current")


class _CwtFeederModelNumber_Type(Integer32):
    """Custom type cwtFeederModelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwtFeederModelNumber_Type.__name__ = "Integer32"
_CwtFeederModelNumber_Object = MibTableColumn
cwtFeederModelNumber = _CwtFeederModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 15),
    _CwtFeederModelNumber_Type()
)
cwtFeederModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwtFeederModelNumber.setStatus("current")
_CwtFeederRowStatus_Type = RowStatus
_CwtFeederRowStatus_Object = MibTableColumn
cwtFeederRowStatus = _CwtFeederRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 3, 1, 1, 16),
    _CwtFeederRowStatus_Type()
)
cwtFeederRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwtFeederRowStatus.setStatus("current")
_CwtLinkInfoGroup_ObjectIdentity = ObjectIdentity
cwtLinkInfoGroup = _CwtLinkInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4)
)
_CwtLinkInfoTable_Object = MibTable
cwtLinkInfoTable = _CwtLinkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cwtLinkInfoTable.setStatus("current")
_CwtLinkInfoEntry_Object = MibTableRow
cwtLinkInfoEntry = _CwtLinkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4, 1, 1)
)
cwtLinkInfoEntry.setIndexNames(
    (0, "CISCO-WAN-TOPOLOGY-MIB", "cwtLinkIndex"),
)
if mibBuilder.loadTexts:
    cwtLinkInfoEntry.setStatus("current")
_CwtLinkIndex_Type = Integer32
_CwtLinkIndex_Object = MibTableColumn
cwtLinkIndex = _CwtLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4, 1, 1, 1),
    _CwtLinkIndex_Type()
)
cwtLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwtLinkIndex.setStatus("current")
_CwtLinkLocalNodeId_Type = PnniNodeId
_CwtLinkLocalNodeId_Object = MibTableColumn
cwtLinkLocalNodeId = _CwtLinkLocalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4, 1, 1, 2),
    _CwtLinkLocalNodeId_Type()
)
cwtLinkLocalNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtLinkLocalNodeId.setStatus("current")
_CwtLinkRemoteNodeId_Type = PnniNodeId
_CwtLinkRemoteNodeId_Object = MibTableColumn
cwtLinkRemoteNodeId = _CwtLinkRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4, 1, 1, 3),
    _CwtLinkRemoteNodeId_Type()
)
cwtLinkRemoteNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtLinkRemoteNodeId.setStatus("current")
_CwtLinkLocalIfIndex_Type = InterfaceIndex
_CwtLinkLocalIfIndex_Object = MibTableColumn
cwtLinkLocalIfIndex = _CwtLinkLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4, 1, 1, 4),
    _CwtLinkLocalIfIndex_Type()
)
cwtLinkLocalIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtLinkLocalIfIndex.setStatus("current")
_CwtLinkRemoteIfIndex_Type = InterfaceIndex
_CwtLinkRemoteIfIndex_Object = MibTableColumn
cwtLinkRemoteIfIndex = _CwtLinkRemoteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4, 1, 1, 5),
    _CwtLinkRemoteIfIndex_Type()
)
cwtLinkRemoteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtLinkRemoteIfIndex.setStatus("current")
_CwtLinkLocalPhysicalId_Type = SnmpAdminString
_CwtLinkLocalPhysicalId_Object = MibTableColumn
cwtLinkLocalPhysicalId = _CwtLinkLocalPhysicalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4, 1, 1, 6),
    _CwtLinkLocalPhysicalId_Type()
)
cwtLinkLocalPhysicalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtLinkLocalPhysicalId.setStatus("current")
_CwtLinkRemotePhysicalId_Type = SnmpAdminString
_CwtLinkRemotePhysicalId_Object = MibTableColumn
cwtLinkRemotePhysicalId = _CwtLinkRemotePhysicalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4, 1, 1, 7),
    _CwtLinkRemotePhysicalId_Type()
)
cwtLinkRemotePhysicalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtLinkRemotePhysicalId.setStatus("current")
_CwtLinkInfoTimeOutFlag_Type = TruthValue
_CwtLinkInfoTimeOutFlag_Object = MibTableColumn
cwtLinkInfoTimeOutFlag = _CwtLinkInfoTimeOutFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4, 1, 1, 8),
    _CwtLinkInfoTimeOutFlag_Type()
)
cwtLinkInfoTimeOutFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtLinkInfoTimeOutFlag.setStatus("current")
_CwtLinkOutsideLink_Type = TruthValue
_CwtLinkOutsideLink_Object = MibTableColumn
cwtLinkOutsideLink = _CwtLinkOutsideLink_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4, 1, 1, 9),
    _CwtLinkOutsideLink_Type()
)
cwtLinkOutsideLink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtLinkOutsideLink.setStatus("current")
_CwtLinkRowStatus_Type = RowStatus
_CwtLinkRowStatus_Object = MibTableColumn
cwtLinkRowStatus = _CwtLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 1, 4, 1, 1, 10),
    _CwtLinkRowStatus_Type()
)
cwtLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwtLinkRowStatus.setStatus("current")
_CwtMIBConformance_ObjectIdentity = ObjectIdentity
cwtMIBConformance = _CwtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2)
)
_CwtMIBCompliances_ObjectIdentity = ObjectIdentity
cwtMIBCompliances = _CwtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2, 1)
)
_CwtMIBGroups_ObjectIdentity = ObjectIdentity
cwtMIBGroups = _CwtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2, 2)
)

# Managed Objects groups

cwtSystemMIBGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2, 2, 1)
)
cwtSystemMIBGroups.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtGatewayAdminStatus"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtGatewayNodeOperStatus"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtDBLastChange"))
)
if mibBuilder.loadTexts:
    cwtSystemMIBGroups.setStatus("current")

cwtNodalMIBGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2, 2, 2)
)
cwtNodalMIBGroups.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtGatewayNodeFlag"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtNodeName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtPrimIPIfType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtPrimIPIfName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtPrimIPAddrType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtPrimIP"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSecIPIfType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSecIPIfName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSecIPAddrType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSecIP"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSysObjId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtNodeInfoTimeOutFlag"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtRowStatus"))
)
if mibBuilder.loadTexts:
    cwtNodalMIBGroups.setStatus("current")

cwtFeederMIBGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2, 2, 3)
)
cwtFeederMIBGroups.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtLocalNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLocalIfIndex"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLocalIfName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederShelf"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederSlot"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederPort"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederLMIType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederLanIPAddrType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederLanIP"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederAtmIPAddrType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederAtmIP"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederModelNumber"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederRowStatus"))
)
if mibBuilder.loadTexts:
    cwtFeederMIBGroups.setStatus("current")

cwtLinkMIBGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2, 2, 7)
)
cwtLinkMIBGroups.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkLocalNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkRemoteNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkLocalIfIndex"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkRemoteIfIndex"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkLocalPhysicalId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkRemotePhysicalId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkInfoTimeOutFlag"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkOutsideLink"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkRowStatus"))
)
if mibBuilder.loadTexts:
    cwtLinkMIBGroups.setStatus("current")


# Notification objects

cwtConfigGatewayStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 0, 1)
)
cwtConfigGatewayStatus.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtGatewayAdminStatus"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtDBLastChange"))
)
if mibBuilder.loadTexts:
    cwtConfigGatewayStatus.setStatus(
        "current"
    )

cwtTopoInfoAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 0, 2)
)
cwtTopoInfoAdd.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtGatewayNodeFlag"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtNodeName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtPrimIPIfType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtPrimIPIfName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtPrimIPAddrType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtPrimIP"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSecIPIfType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSecIPIfName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSecIPAddrType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSecIP"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSysObjId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtNodeInfoTimeOutFlag"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtDBLastChange"))
)
if mibBuilder.loadTexts:
    cwtTopoInfoAdd.setStatus(
        "current"
    )

cwtTopoInfoModify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 0, 3)
)
cwtTopoInfoModify.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtGatewayNodeFlag"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtNodeName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtPrimIPIfType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtPrimIPIfName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtPrimIPAddrType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtPrimIP"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSecIPIfType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSecIPIfName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSecIPAddrType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSecIP"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtSysObjId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtNodeInfoTimeOutFlag"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtDBLastChange"))
)
if mibBuilder.loadTexts:
    cwtTopoInfoModify.setStatus(
        "current"
    )

cwtTopoInfoDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 0, 4)
)
cwtTopoInfoDelete.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtDBLastChange"))
)
if mibBuilder.loadTexts:
    cwtTopoInfoDelete.setStatus(
        "current"
    )

cwtTopoDbFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 0, 5)
)
cwtTopoDbFull.setObjects(
    ("CISCO-WAN-TOPOLOGY-MIB", "cwtDBLastChange")
)
if mibBuilder.loadTexts:
    cwtTopoDbFull.setStatus(
        "current"
    )

cwtFeederInfoAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 0, 6)
)
cwtFeederInfoAdd.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtLocalNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLocalIfIndex"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLocalIfName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederShelf"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederSlot"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederPort"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederLMIType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederLanIPAddrType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederLanIP"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederAtmIPAddrType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederAtmIP"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederModelNumber"))
)
if mibBuilder.loadTexts:
    cwtFeederInfoAdd.setStatus(
        "current"
    )

cwtFeederInfoModify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 0, 7)
)
cwtFeederInfoModify.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtLocalNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLocalIfIndex"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederLMIType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederName"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederLanIPAddrType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederLanIP"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederAtmIPAddrType"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederAtmIP"))
)
if mibBuilder.loadTexts:
    cwtFeederInfoModify.setStatus(
        "current"
    )

cwtFeederInfoDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 0, 8)
)
cwtFeederInfoDelete.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtLocalNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLocalIfIndex"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederName"))
)
if mibBuilder.loadTexts:
    cwtFeederInfoDelete.setStatus(
        "current"
    )

cwtLinkInfoAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 0, 9)
)
cwtLinkInfoAdd.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkLocalNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkRemoteNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkLocalIfIndex"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkRemoteIfIndex"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkLocalPhysicalId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkRemotePhysicalId"))
)
if mibBuilder.loadTexts:
    cwtLinkInfoAdd.setStatus(
        "current"
    )

cwtLinkInfoModify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 0, 10)
)
cwtLinkInfoModify.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkLocalNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkRemoteNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkLocalIfIndex"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkRemoteIfIndex"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkInfoTimeOutFlag"))
)
if mibBuilder.loadTexts:
    cwtLinkInfoModify.setStatus(
        "current"
    )

cwtLinkInfoDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 0, 11)
)
cwtLinkInfoDelete.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkLocalNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkRemoteNodeId"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkLocalIfIndex"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkRemoteIfIndex"))
)
if mibBuilder.loadTexts:
    cwtLinkInfoDelete.setStatus(
        "current"
    )


# Notifications groups

cwtNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2, 2, 4)
)
cwtNotificationsGroup.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtConfigGatewayStatus"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtTopoInfoAdd"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtTopoInfoModify"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtTopoInfoDelete"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtTopoDbFull"))
)
if mibBuilder.loadTexts:
    cwtNotificationsGroup.setStatus(
        "deprecated"
    )

cwtNotificationsGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2, 2, 5)
)
cwtNotificationsGroup2.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtConfigGatewayStatus"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtTopoInfoAdd"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtTopoInfoModify"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtTopoInfoDelete"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtTopoDbFull"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederInfoAdd"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederInfoModify"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederInfoDelete"))
)
if mibBuilder.loadTexts:
    cwtNotificationsGroup2.setStatus(
        "deprecated"
    )

cwtNotificationsGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2, 2, 6)
)
cwtNotificationsGroup3.setObjects(
      *(("CISCO-WAN-TOPOLOGY-MIB", "cwtConfigGatewayStatus"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtTopoInfoAdd"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtTopoInfoModify"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtTopoInfoDelete"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtTopoDbFull"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederInfoAdd"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederInfoModify"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtFeederInfoDelete"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkInfoAdd"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkInfoModify"),
        ("CISCO-WAN-TOPOLOGY-MIB", "cwtLinkInfoDelete"))
)
if mibBuilder.loadTexts:
    cwtNotificationsGroup3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cwtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cwtMIBCompliance.setStatus(
        "deprecated"
    )

cwtMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cwtMIBCompliance2.setStatus(
        "deprecated"
    )

cwtMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 234, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cwtMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-TOPOLOGY-MIB",
    **{"CwtNodeInfoTableIndex": CwtNodeInfoTableIndex,
       "ciscoWanTopologyMIB": ciscoWanTopologyMIB,
       "ciscoWanTopologyMIBNotifs": ciscoWanTopologyMIBNotifs,
       "cwtConfigGatewayStatus": cwtConfigGatewayStatus,
       "cwtTopoInfoAdd": cwtTopoInfoAdd,
       "cwtTopoInfoModify": cwtTopoInfoModify,
       "cwtTopoInfoDelete": cwtTopoInfoDelete,
       "cwtTopoDbFull": cwtTopoDbFull,
       "cwtFeederInfoAdd": cwtFeederInfoAdd,
       "cwtFeederInfoModify": cwtFeederInfoModify,
       "cwtFeederInfoDelete": cwtFeederInfoDelete,
       "cwtLinkInfoAdd": cwtLinkInfoAdd,
       "cwtLinkInfoModify": cwtLinkInfoModify,
       "cwtLinkInfoDelete": cwtLinkInfoDelete,
       "ciscoWanTopologyMIBObjects": ciscoWanTopologyMIBObjects,
       "cwtSystemGroup": cwtSystemGroup,
       "cwtGatewayAdminStatus": cwtGatewayAdminStatus,
       "cwtGatewayNodeOperStatus": cwtGatewayNodeOperStatus,
       "cwtDBLastChange": cwtDBLastChange,
       "cwtNodalInfoGroup": cwtNodalInfoGroup,
       "cwtNodeInfoTable": cwtNodeInfoTable,
       "cwtNodeInfoEntry": cwtNodeInfoEntry,
       "cwtIndex": cwtIndex,
       "cwtGatewayNodeFlag": cwtGatewayNodeFlag,
       "cwtNodeId": cwtNodeId,
       "cwtNodeName": cwtNodeName,
       "cwtPrimIPIfType": cwtPrimIPIfType,
       "cwtPrimIPIfName": cwtPrimIPIfName,
       "cwtPrimIPAddrType": cwtPrimIPAddrType,
       "cwtPrimIP": cwtPrimIP,
       "cwtSecIPIfType": cwtSecIPIfType,
       "cwtSecIPIfName": cwtSecIPIfName,
       "cwtSecIPAddrType": cwtSecIPAddrType,
       "cwtSecIP": cwtSecIP,
       "cwtSysObjId": cwtSysObjId,
       "cwtNodeInfoTimeOutFlag": cwtNodeInfoTimeOutFlag,
       "cwtRowStatus": cwtRowStatus,
       "cwtFeederInfoGroup": cwtFeederInfoGroup,
       "cwtFeederInfoTable": cwtFeederInfoTable,
       "cwtFeederInfoEntry": cwtFeederInfoEntry,
       "cwtFeederIndex": cwtFeederIndex,
       "cwtLocalNodeId": cwtLocalNodeId,
       "cwtLocalIfIndex": cwtLocalIfIndex,
       "cwtLocalIfName": cwtLocalIfName,
       "cwtFeederShelf": cwtFeederShelf,
       "cwtFeederSlot": cwtFeederSlot,
       "cwtFeederPort": cwtFeederPort,
       "cwtFeederLMIType": cwtFeederLMIType,
       "cwtFeederType": cwtFeederType,
       "cwtFeederName": cwtFeederName,
       "cwtFeederLanIPAddrType": cwtFeederLanIPAddrType,
       "cwtFeederLanIP": cwtFeederLanIP,
       "cwtFeederAtmIPAddrType": cwtFeederAtmIPAddrType,
       "cwtFeederAtmIP": cwtFeederAtmIP,
       "cwtFeederModelNumber": cwtFeederModelNumber,
       "cwtFeederRowStatus": cwtFeederRowStatus,
       "cwtLinkInfoGroup": cwtLinkInfoGroup,
       "cwtLinkInfoTable": cwtLinkInfoTable,
       "cwtLinkInfoEntry": cwtLinkInfoEntry,
       "cwtLinkIndex": cwtLinkIndex,
       "cwtLinkLocalNodeId": cwtLinkLocalNodeId,
       "cwtLinkRemoteNodeId": cwtLinkRemoteNodeId,
       "cwtLinkLocalIfIndex": cwtLinkLocalIfIndex,
       "cwtLinkRemoteIfIndex": cwtLinkRemoteIfIndex,
       "cwtLinkLocalPhysicalId": cwtLinkLocalPhysicalId,
       "cwtLinkRemotePhysicalId": cwtLinkRemotePhysicalId,
       "cwtLinkInfoTimeOutFlag": cwtLinkInfoTimeOutFlag,
       "cwtLinkOutsideLink": cwtLinkOutsideLink,
       "cwtLinkRowStatus": cwtLinkRowStatus,
       "cwtMIBConformance": cwtMIBConformance,
       "cwtMIBCompliances": cwtMIBCompliances,
       "cwtMIBCompliance": cwtMIBCompliance,
       "cwtMIBCompliance2": cwtMIBCompliance2,
       "cwtMIBCompliance3": cwtMIBCompliance3,
       "cwtMIBGroups": cwtMIBGroups,
       "cwtSystemMIBGroups": cwtSystemMIBGroups,
       "cwtNodalMIBGroups": cwtNodalMIBGroups,
       "cwtFeederMIBGroups": cwtFeederMIBGroups,
       "cwtNotificationsGroup": cwtNotificationsGroup,
       "cwtNotificationsGroup2": cwtNotificationsGroup2,
       "cwtNotificationsGroup3": cwtNotificationsGroup3,
       "cwtLinkMIBGroups": cwtLinkMIBGroups}
)
