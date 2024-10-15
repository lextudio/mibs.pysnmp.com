# SNMP MIB module (BAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:14 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

basMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BasChassisId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



class BasSlotId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )



class BasInterfaceId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class BasLogicalPortId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class BasCardClass(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("clusterManager", 1),
          ("cmts", 4),
          ("cmtsForwarder", 6),
          ("forwarder", 3),
          ("forwarder1000", 11),
          ("forwarder10100", 10),
          ("forwarderOC12", 12),
          ("forwarderOC3", 15),
          ("forwarderOC48", 16),
          ("routeServer", 2),
          ("routeServer1000", 8),
          ("routeServer10100", 7),
          ("routeServerForwarder", 5),
          ("routeServerOC12", 9),
          ("routeServerOC3", 13),
          ("routeServerOC48", 14))
    )



class BasIfClass(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ccl", 2),
          ("egress", 3),
          ("icl", 1))
    )



class BasChassisType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cuda", 1)
    )



class BasSubnetClass(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 2),
          ("cablemodem", 3),
          ("unauthorized", 1))
    )



# MIB Managed Objects in the order of their OIDs

_BasProductId_ObjectIdentity = ObjectIdentity
basProductId = _BasProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 1)
)
_BasMibGroup_ObjectIdentity = ObjectIdentity
basMibGroup = _BasMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2)
)
_BasExtSys_ObjectIdentity = ObjectIdentity
basExtSys = _BasExtSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1)
)
_BasStartup_ObjectIdentity = ObjectIdentity
basStartup = _BasStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1)
)
_BasCardInfo_ObjectIdentity = ObjectIdentity
basCardInfo = _BasCardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 2)
)
_BasChassisInfo_ObjectIdentity = ObjectIdentity
basChassisInfo = _BasChassisInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3)
)
_BasProvInfo_ObjectIdentity = ObjectIdentity
basProvInfo = _BasProvInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 4)
)
_BasHackedInfo_ObjectIdentity = ObjectIdentity
basHackedInfo = _BasHackedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000)
)
_BasExtIf_ObjectIdentity = ObjectIdentity
basExtIf = _BasExtIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2)
)
_BasExtIp_ObjectIdentity = ObjectIdentity
basExtIp = _BasExtIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3)
)
_BasExtCmts_ObjectIdentity = ObjectIdentity
basExtCmts = _BasExtCmts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 4)
)
_BasFtd_ObjectIdentity = ObjectIdentity
basFtd = _BasFtd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 5)
)
_BasRbp_ObjectIdentity = ObjectIdentity
basRbp = _BasRbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6)
)
_BasAlias_ObjectIdentity = ObjectIdentity
basAlias = _BasAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7)
)
_BasAliasSnmp_ObjectIdentity = ObjectIdentity
basAliasSnmp = _BasAliasSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1)
)
_BasAliasIp_ObjectIdentity = ObjectIdentity
basAliasIp = _BasAliasIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2)
)
_BasAliasTcp_ObjectIdentity = ObjectIdentity
basAliasTcp = _BasAliasTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3)
)
_BasAliasUdp_ObjectIdentity = ObjectIdentity
basAliasUdp = _BasAliasUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4)
)
_BasAliasCidr_ObjectIdentity = ObjectIdentity
basAliasCidr = _BasAliasCidr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 5)
)
_BasAliasRip_ObjectIdentity = ObjectIdentity
basAliasRip = _BasAliasRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 6)
)
_BasAliasOspf_ObjectIdentity = ObjectIdentity
basAliasOspf = _BasAliasOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7)
)
_BasAliasDocsIf_ObjectIdentity = ObjectIdentity
basAliasDocsIf = _BasAliasDocsIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8)
)
_BasAliasDocsCd_ObjectIdentity = ObjectIdentity
basAliasDocsCd = _BasAliasDocsCd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 9)
)
_BasAliasCmtsCfg_ObjectIdentity = ObjectIdentity
basAliasCmtsCfg = _BasAliasCmtsCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 10)
)
_BasExtEvent_ObjectIdentity = ObjectIdentity
basExtEvent = _BasExtEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 8)
)
_BasTopology_ObjectIdentity = ObjectIdentity
basTopology = _BasTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 9)
)
_BasAccessControl_ObjectIdentity = ObjectIdentity
basAccessControl = _BasAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10)
)
_BasPbrfFilter_ObjectIdentity = ObjectIdentity
basPbrfFilter = _BasPbrfFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11)
)
_BasPbrfRIP_ObjectIdentity = ObjectIdentity
basPbrfRIP = _BasPbrfRIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 1)
)
_BasPbrfOSPF_ObjectIdentity = ObjectIdentity
basPbrfOSPF = _BasPbrfOSPF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 11, 2)
)
_BasCmConfig_ObjectIdentity = ObjectIdentity
basCmConfig = _BasCmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12)
)
_BasTrafGen_ObjectIdentity = ObjectIdentity
basTrafGen = _BasTrafGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 13)
)
_BasTrace_ObjectIdentity = ObjectIdentity
basTrace = _BasTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 14)
)
_BasDhcpRelay_ObjectIdentity = ObjectIdentity
basDhcpRelay = _BasDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15)
)
_BasMcc_ObjectIdentity = ObjectIdentity
basMcc = _BasMcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 16)
)
_BasAnalyzer_ObjectIdentity = ObjectIdentity
basAnalyzer = _BasAnalyzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 17)
)
_BasCluster_ObjectIdentity = ObjectIdentity
basCluster = _BasCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18)
)
_BasRip_ObjectIdentity = ObjectIdentity
basRip = _BasRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19)
)
_BasSonet_ObjectIdentity = ObjectIdentity
basSonet = _BasSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20)
)
_BasHackedAccessControl_ObjectIdentity = ObjectIdentity
basHackedAccessControl = _BasHackedAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1001)
)
_BasTrapGroup_ObjectIdentity = ObjectIdentity
basTrapGroup = _BasTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 3)
)
_BasTrapObjects_ObjectIdentity = ObjectIdentity
basTrapObjects = _BasTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1)
)
_BasTrapChassis_Type = BasChassisId
_BasTrapChassis_Object = MibScalar
basTrapChassis = _BasTrapChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 1),
    _BasTrapChassis_Type()
)
basTrapChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapChassis.setStatus("current")
_BasTrapSlot_Type = BasSlotId
_BasTrapSlot_Object = MibScalar
basTrapSlot = _BasTrapSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 2),
    _BasTrapSlot_Type()
)
basTrapSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapSlot.setStatus("current")
_BasTrapIf_Type = BasInterfaceId
_BasTrapIf_Object = MibScalar
basTrapIf = _BasTrapIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 3),
    _BasTrapIf_Type()
)
basTrapIf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapIf.setStatus("current")
_BasTrapLPort_Type = BasLogicalPortId
_BasTrapLPort_Object = MibScalar
basTrapLPort = _BasTrapLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 4),
    _BasTrapLPort_Type()
)
basTrapLPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapLPort.setStatus("current")
_BasTrapCmtsCmMacAddress_Type = MacAddress
_BasTrapCmtsCmMacAddress_Object = MibScalar
basTrapCmtsCmMacAddress = _BasTrapCmtsCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 5),
    _BasTrapCmtsCmMacAddress_Type()
)
basTrapCmtsCmMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapCmtsCmMacAddress.setStatus("current")
_BasTrapCmtsCmIpAddress_Type = IpAddress
_BasTrapCmtsCmIpAddress_Object = MibScalar
basTrapCmtsCmIpAddress = _BasTrapCmtsCmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 6),
    _BasTrapCmtsCmIpAddress_Type()
)
basTrapCmtsCmIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapCmtsCmIpAddress.setStatus("current")
_BasTrapMgmtOneIpAddress_Type = IpAddress
_BasTrapMgmtOneIpAddress_Object = MibScalar
basTrapMgmtOneIpAddress = _BasTrapMgmtOneIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 7),
    _BasTrapMgmtOneIpAddress_Type()
)
basTrapMgmtOneIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapMgmtOneIpAddress.setStatus("current")
_BasTrapMgmtTwoIpAddress_Type = IpAddress
_BasTrapMgmtTwoIpAddress_Object = MibScalar
basTrapMgmtTwoIpAddress = _BasTrapMgmtTwoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 8),
    _BasTrapMgmtTwoIpAddress_Type()
)
basTrapMgmtTwoIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapMgmtTwoIpAddress.setStatus("current")
_BasTrapCraftIpAddress_Type = IpAddress
_BasTrapCraftIpAddress_Object = MibScalar
basTrapCraftIpAddress = _BasTrapCraftIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 9),
    _BasTrapCraftIpAddress_Type()
)
basTrapCraftIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapCraftIpAddress.setStatus("current")
_BasTrapIclClass_Type = BasIfClass
_BasTrapIclClass_Object = MibScalar
basTrapIclClass = _BasTrapIclClass_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 10),
    _BasTrapIclClass_Type()
)
basTrapIclClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapIclClass.setStatus("current")
_BasTrapChassisNumber_Type = Integer32
_BasTrapChassisNumber_Object = MibScalar
basTrapChassisNumber = _BasTrapChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 11),
    _BasTrapChassisNumber_Type()
)
basTrapChassisNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapChassisNumber.setStatus("current")
_BasTrapCmtsCmGwAddress_Type = IpAddress
_BasTrapCmtsCmGwAddress_Object = MibScalar
basTrapCmtsCmGwAddress = _BasTrapCmtsCmGwAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 12),
    _BasTrapCmtsCmGwAddress_Type()
)
basTrapCmtsCmGwAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapCmtsCmGwAddress.setStatus("current")
_BasTrapCardType_Type = BasCardClass
_BasTrapCardType_Object = MibScalar
basTrapCardType = _BasTrapCardType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 13),
    _BasTrapCardType_Type()
)
basTrapCardType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapCardType.setStatus("current")
_BasTrapSubnetType_Type = BasSubnetClass
_BasTrapSubnetType_Object = MibScalar
basTrapSubnetType = _BasTrapSubnetType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 3, 1, 14),
    _BasTrapSubnetType_Type()
)
basTrapSubnetType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    basTrapSubnetType.setStatus("current")
_BasTraps_ObjectIdentity = ObjectIdentity
basTraps = _BasTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2)
)
_BasCudaChassMgr_ObjectIdentity = ObjectIdentity
basCudaChassMgr = _BasCudaChassMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 4)
)
_BasCuda10100Rs_ObjectIdentity = ObjectIdentity
basCuda10100Rs = _BasCuda10100Rs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 5)
)
_BasCuda1000Rs_ObjectIdentity = ObjectIdentity
basCuda1000Rs = _BasCuda1000Rs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 6)
)
_BasCudaOC12Rs_ObjectIdentity = ObjectIdentity
basCudaOC12Rs = _BasCudaOC12Rs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 7)
)
_BasCuda10100_ObjectIdentity = ObjectIdentity
basCuda10100 = _BasCuda10100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 8)
)
_BasCuda1000_ObjectIdentity = ObjectIdentity
basCuda1000 = _BasCuda1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 9)
)
_BasCudaOC12_ObjectIdentity = ObjectIdentity
basCudaOC12 = _BasCudaOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 10)
)
_BasCudaCMTS1_ObjectIdentity = ObjectIdentity
basCudaCMTS1 = _BasCudaCMTS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 11)
)
_BasCudaOC3Rs_ObjectIdentity = ObjectIdentity
basCudaOC3Rs = _BasCudaOC3Rs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 12)
)
_BasCudaOC48Rs_ObjectIdentity = ObjectIdentity
basCudaOC48Rs = _BasCudaOC48Rs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 13)
)
_BasCudaOC3_ObjectIdentity = ObjectIdentity
basCudaOC3 = _BasCudaOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 14)
)
_BasCudaOC48_ObjectIdentity = ObjectIdentity
basCudaOC48 = _BasCudaOC48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-MIB",
    **{"BasChassisId": BasChassisId,
       "BasSlotId": BasSlotId,
       "BasInterfaceId": BasInterfaceId,
       "BasLogicalPortId": BasLogicalPortId,
       "BasCardClass": BasCardClass,
       "BasIfClass": BasIfClass,
       "BasChassisType": BasChassisType,
       "BasSubnetClass": BasSubnetClass,
       "basMIB": basMIB,
       "basProductId": basProductId,
       "basMibGroup": basMibGroup,
       "basExtSys": basExtSys,
       "basStartup": basStartup,
       "basCardInfo": basCardInfo,
       "basChassisInfo": basChassisInfo,
       "basProvInfo": basProvInfo,
       "basHackedInfo": basHackedInfo,
       "basExtIf": basExtIf,
       "basExtIp": basExtIp,
       "basExtCmts": basExtCmts,
       "basFtd": basFtd,
       "basRbp": basRbp,
       "basAlias": basAlias,
       "basAliasSnmp": basAliasSnmp,
       "basAliasIp": basAliasIp,
       "basAliasTcp": basAliasTcp,
       "basAliasUdp": basAliasUdp,
       "basAliasCidr": basAliasCidr,
       "basAliasRip": basAliasRip,
       "basAliasOspf": basAliasOspf,
       "basAliasDocsIf": basAliasDocsIf,
       "basAliasDocsCd": basAliasDocsCd,
       "basAliasCmtsCfg": basAliasCmtsCfg,
       "basExtEvent": basExtEvent,
       "basTopology": basTopology,
       "basAccessControl": basAccessControl,
       "basPbrfFilter": basPbrfFilter,
       "basPbrfRIP": basPbrfRIP,
       "basPbrfOSPF": basPbrfOSPF,
       "basCmConfig": basCmConfig,
       "basTrafGen": basTrafGen,
       "basTrace": basTrace,
       "basDhcpRelay": basDhcpRelay,
       "basMcc": basMcc,
       "basAnalyzer": basAnalyzer,
       "basCluster": basCluster,
       "basRip": basRip,
       "basSonet": basSonet,
       "basHackedAccessControl": basHackedAccessControl,
       "basTrapGroup": basTrapGroup,
       "basTrapObjects": basTrapObjects,
       "basTrapChassis": basTrapChassis,
       "basTrapSlot": basTrapSlot,
       "basTrapIf": basTrapIf,
       "basTrapLPort": basTrapLPort,
       "basTrapCmtsCmMacAddress": basTrapCmtsCmMacAddress,
       "basTrapCmtsCmIpAddress": basTrapCmtsCmIpAddress,
       "basTrapMgmtOneIpAddress": basTrapMgmtOneIpAddress,
       "basTrapMgmtTwoIpAddress": basTrapMgmtTwoIpAddress,
       "basTrapCraftIpAddress": basTrapCraftIpAddress,
       "basTrapIclClass": basTrapIclClass,
       "basTrapChassisNumber": basTrapChassisNumber,
       "basTrapCmtsCmGwAddress": basTrapCmtsCmGwAddress,
       "basTrapCardType": basTrapCardType,
       "basTrapSubnetType": basTrapSubnetType,
       "basTraps": basTraps,
       "basCudaChassMgr": basCudaChassMgr,
       "basCuda10100Rs": basCuda10100Rs,
       "basCuda1000Rs": basCuda1000Rs,
       "basCudaOC12Rs": basCudaOC12Rs,
       "basCuda10100": basCuda10100,
       "basCuda1000": basCuda1000,
       "basCudaOC12": basCudaOC12,
       "basCudaCMTS1": basCudaCMTS1,
       "basCudaOC3Rs": basCudaOC3Rs,
       "basCudaOC48Rs": basCudaOC48Rs,
       "basCudaOC3": basCudaOC3,
       "basCudaOC48": basCudaOC48}
)
