# SNMP MIB module (IBMIROC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBMIROC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:55 2024
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

(proElsSubSysEventMsg,
 proResMemHeapNeverAlloc,
 proResMemHeapTotal) = mibBuilder.importSymbols(
    "PROTEON-MIB",
    "proElsSubSysEventMsg",
    "proResMemHeapNeverAlloc",
    "proResMemHeapTotal")

(frCircuitDlci,
 frCircuitIfIndex) = mibBuilder.importSymbols(
    "RFC1315-MIB",
    "frCircuitDlci",
    "frCircuitIfIndex")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddressNCIROC(OctetString):
    """Custom type MacAddressNCIROC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_IbmIROC_ObjectIdentity = ObjectIdentity
ibmIROC = _IbmIROC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119)
)
_IbmIROCadmin_ObjectIdentity = ObjectIdentity
ibmIROCadmin = _IbmIROCadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 1)
)
_IbmIROCadminproducts_ObjectIdentity = ObjectIdentity
ibmIROCadminproducts = _IbmIROCadminproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 1, 1)
)
_IbmIROCadminOID_ObjectIdentity = ObjectIdentity
ibmIROCadminOID = _IbmIROCadminOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 1, 2)
)
_IbmIROCadminDebug_ObjectIdentity = ObjectIdentity
ibmIROCadminDebug = _IbmIROCadminDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 1, 3)
)
_IbmIROCAgentDebug_ObjectIdentity = ObjectIdentity
ibmIROCAgentDebug = _IbmIROCAgentDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 1, 3, 1)
)
_AgentMemUse_Type = Gauge32
_AgentMemUse_Object = MibScalar
agentMemUse = _AgentMemUse_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 1, 3, 1, 1),
    _AgentMemUse_Type()
)
agentMemUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMemUse.setStatus("mandatory")
_IbmIROCadminSnmp_ObjectIdentity = ObjectIdentity
ibmIROCadminSnmp = _IbmIROCadminSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 1, 4)
)
_IbmIROCSnmpAuthFail_ObjectIdentity = ObjectIdentity
ibmIROCSnmpAuthFail = _IbmIROCSnmpAuthFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 1, 4, 1)
)
_AuthTrapSourceIPAddr_Type = IpAddress
_AuthTrapSourceIPAddr_Object = MibScalar
authTrapSourceIPAddr = _AuthTrapSourceIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 1, 4, 1, 1),
    _AuthTrapSourceIPAddr_Type()
)
authTrapSourceIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authTrapSourceIPAddr.setStatus("mandatory")
_IbmIROCsystem_ObjectIdentity = ObjectIdentity
ibmIROCsystem = _IbmIROCsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2)
)
_IbmIROCsystemInfo_ObjectIdentity = ObjectIdentity
ibmIROCsystemInfo = _IbmIROCsystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 1)
)
_IbmIROCcfgInfo_ObjectIdentity = ObjectIdentity
ibmIROCcfgInfo = _IbmIROCcfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 2)
)
_IbmIROCdumpInfo_ObjectIdentity = ObjectIdentity
ibmIROCdumpInfo = _IbmIROCdumpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4)
)
_IbmSysDumpTable_Object = MibTable
ibmSysDumpTable = _IbmSysDumpTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ibmSysDumpTable.setStatus("mandatory")
_IbmSysDumpEntry_Object = MibTableRow
ibmSysDumpEntry = _IbmSysDumpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1)
)
ibmSysDumpEntry.setIndexNames(
    (0, "IBMIROC-MIB", "ibmSysDumpIndex"),
)
if mibBuilder.loadTexts:
    ibmSysDumpEntry.setStatus("mandatory")
_IbmSysDumpIndex_Type = Integer32
_IbmSysDumpIndex_Object = MibTableColumn
ibmSysDumpIndex = _IbmSysDumpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 1),
    _IbmSysDumpIndex_Type()
)
ibmSysDumpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpIndex.setStatus("mandatory")
_IbmSysDumpFileName_Type = DisplayString
_IbmSysDumpFileName_Object = MibTableColumn
ibmSysDumpFileName = _IbmSysDumpFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 2),
    _IbmSysDumpFileName_Type()
)
ibmSysDumpFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpFileName.setStatus("mandatory")
_IbmSysDumpFileDate_Type = DisplayString
_IbmSysDumpFileDate_Object = MibTableColumn
ibmSysDumpFileDate = _IbmSysDumpFileDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 3),
    _IbmSysDumpFileDate_Type()
)
ibmSysDumpFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpFileDate.setStatus("mandatory")
_IbmSysDumpBuild_Type = DisplayString
_IbmSysDumpBuild_Object = MibTableColumn
ibmSysDumpBuild = _IbmSysDumpBuild_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 4),
    _IbmSysDumpBuild_Type()
)
ibmSysDumpBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpBuild.setStatus("mandatory")
_IbmSysDumpBuilder_Type = DisplayString
_IbmSysDumpBuilder_Object = MibTableColumn
ibmSysDumpBuilder = _IbmSysDumpBuilder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 5),
    _IbmSysDumpBuilder_Type()
)
ibmSysDumpBuilder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpBuilder.setStatus("mandatory")
_IbmSysDumpBuildName_Type = DisplayString
_IbmSysDumpBuildName_Object = MibTableColumn
ibmSysDumpBuildName = _IbmSysDumpBuildName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 6),
    _IbmSysDumpBuildName_Type()
)
ibmSysDumpBuildName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpBuildName.setStatus("mandatory")
_IbmSysDumpRetainName_Type = DisplayString
_IbmSysDumpRetainName_Object = MibTableColumn
ibmSysDumpRetainName = _IbmSysDumpRetainName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 7),
    _IbmSysDumpRetainName_Type()
)
ibmSysDumpRetainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpRetainName.setStatus("mandatory")
_IbmSysDumpProductNumber_Type = DisplayString
_IbmSysDumpProductNumber_Object = MibTableColumn
ibmSysDumpProductNumber = _IbmSysDumpProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 8),
    _IbmSysDumpProductNumber_Type()
)
ibmSysDumpProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpProductNumber.setStatus("mandatory")
_IbmSysDumpBuildDate_Type = DisplayString
_IbmSysDumpBuildDate_Object = MibTableColumn
ibmSysDumpBuildDate = _IbmSysDumpBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 9),
    _IbmSysDumpBuildDate_Type()
)
ibmSysDumpBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpBuildDate.setStatus("mandatory")
_IbmSysDumpFatalMsg1_Type = DisplayString
_IbmSysDumpFatalMsg1_Object = MibTableColumn
ibmSysDumpFatalMsg1 = _IbmSysDumpFatalMsg1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 10),
    _IbmSysDumpFatalMsg1_Type()
)
ibmSysDumpFatalMsg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpFatalMsg1.setStatus("mandatory")
_IbmSysDumpFatalMsg2_Type = DisplayString
_IbmSysDumpFatalMsg2_Object = MibTableColumn
ibmSysDumpFatalMsg2 = _IbmSysDumpFatalMsg2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 11),
    _IbmSysDumpFatalMsg2_Type()
)
ibmSysDumpFatalMsg2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpFatalMsg2.setStatus("mandatory")
_IbmSysDumpFatalMsg3_Type = DisplayString
_IbmSysDumpFatalMsg3_Object = MibTableColumn
ibmSysDumpFatalMsg3 = _IbmSysDumpFatalMsg3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 12),
    _IbmSysDumpFatalMsg3_Type()
)
ibmSysDumpFatalMsg3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpFatalMsg3.setStatus("mandatory")
_IbmSysDumpFatalMsg4_Type = DisplayString
_IbmSysDumpFatalMsg4_Object = MibTableColumn
ibmSysDumpFatalMsg4 = _IbmSysDumpFatalMsg4_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 13),
    _IbmSysDumpFatalMsg4_Type()
)
ibmSysDumpFatalMsg4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpFatalMsg4.setStatus("mandatory")
_IbmSysDumpFatalMsg5_Type = DisplayString
_IbmSysDumpFatalMsg5_Object = MibTableColumn
ibmSysDumpFatalMsg5 = _IbmSysDumpFatalMsg5_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 14),
    _IbmSysDumpFatalMsg5_Type()
)
ibmSysDumpFatalMsg5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpFatalMsg5.setStatus("mandatory")
_IbmSysDumpRemoteIPAddr_Type = DisplayString
_IbmSysDumpRemoteIPAddr_Object = MibTableColumn
ibmSysDumpRemoteIPAddr = _IbmSysDumpRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 15),
    _IbmSysDumpRemoteIPAddr_Type()
)
ibmSysDumpRemoteIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpRemoteIPAddr.setStatus("mandatory")
_IbmSysDumpRemotePath_Type = DisplayString
_IbmSysDumpRemotePath_Object = MibTableColumn
ibmSysDumpRemotePath = _IbmSysDumpRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 4, 1, 1, 16),
    _IbmSysDumpRemotePath_Type()
)
ibmSysDumpRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSysDumpRemotePath.setStatus("mandatory")
_IbmIROChardware_ObjectIdentity = ObjectIdentity
ibmIROChardware = _IbmIROChardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 3)
)
_IbmIROChardwareInfo_ObjectIdentity = ObjectIdentity
ibmIROChardwareInfo = _IbmIROChardwareInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 3, 1)
)


class _PlatformType_Type(Integer32):
    """Custom type platformType based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42)
        )
    )
    namedValues = NamedValues(
        *(("plat-2210-121", 16),
          ("plat-2210-122", 20),
          ("plat-2210-125", 14),
          ("plat-2210-126", 18),
          ("plat-2210-127", 15),
          ("plat-2210-128", 19),
          ("plat-2210-12e", 21),
          ("plat-2210-12t", 17),
          ("plat-2210-14t", 13),
          ("plat-2210-1s4", 6),
          ("plat-2210-1s8", 7),
          ("plat-2210-1u4", 8),
          ("plat-2210-1u8", 9),
          ("plat-2210-24e", 10),
          ("plat-2210-24m", 11),
          ("plat-2210-24t", 12),
          ("plat-2212-10F", 28),
          ("plat-2212-10H", 29),
          ("plat-2212-15F", 34),
          ("plat-2212-15H", 35),
          ("plat-2212-40F", 30),
          ("plat-2212-40H", 31),
          ("plat-2212-45F", 36),
          ("plat-2212-45H", 37),
          ("plat-2216-400", 5),
          ("plat-2220-200", 22),
          ("plat-3746-MAE", 23),
          ("plat-8275-RR", 40),
          ("plat-8371", 32),
          ("plat-8371-8260B", 41),
          ("plat-8375", 33),
          ("plat-mss-8210", 2),
          ("plat-mss-8210V2", 25),
          ("plat-mss-blade", 3),
          ("plat-mss-bladeV2", 26),
          ("plat-mss-client", 4),
          ("plat-mss-domain-client", 24),
          ("plat-netu-xx1", 27),
          ("plat-other", 1),
          ("plat-reserved", 42),
          ("plat-reserved1", 38),
          ("plat-reserved2", 39))
    )


_PlatformType_Type.__name__ = "Integer32"
_PlatformType_Object = MibScalar
platformType = _PlatformType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 3, 1, 1),
    _PlatformType_Type()
)
platformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformType.setStatus("mandatory")
_PlatformDRAMSize_Type = Integer32
_PlatformDRAMSize_Object = MibScalar
platformDRAMSize = _PlatformDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 3, 1, 2),
    _PlatformDRAMSize_Type()
)
platformDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformDRAMSize.setStatus("mandatory")
_PlatformFLASHSize_Type = Integer32
_PlatformFLASHSize_Object = MibScalar
platformFLASHSize = _PlatformFLASHSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 3, 1, 3),
    _PlatformFLASHSize_Type()
)
platformFLASHSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformFLASHSize.setStatus("mandatory")
_PlatformNVRAMSize_Type = Integer32
_PlatformNVRAMSize_Object = MibScalar
platformNVRAMSize = _PlatformNVRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 3, 1, 4),
    _PlatformNVRAMSize_Type()
)
platformNVRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformNVRAMSize.setStatus("mandatory")


class _PlatformFeatureSlot_Type(Integer32):
    """Custom type platformFeatureSlot based on Integer32"""
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
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("atm-155", 6),
          ("atm-25", 7),
          ("isdn-BRI-4port-ST", 12),
          ("isdn-BRI-4port-U", 13),
          ("isdn-BRI-ST", 2),
          ("isdn-PRI-E1-120", 3),
          ("isdn-PRI-E1-75", 4),
          ("isdn-PRI-T1J1", 5),
          ("isdn-voice-ST-EM", 16),
          ("isdn-voice-ST-FXO", 14),
          ("isdn-voice-ST-FXS", 15),
          ("isdn-voice-U-EM", 19),
          ("isdn-voice-U-FXO", 17),
          ("isdn-voice-U-FXS", 18),
          ("modem-4port", 10),
          ("modem-8port", 11),
          ("none", 1),
          ("serial-wan-4port", 8),
          ("serial-wan-8port", 9))
    )


_PlatformFeatureSlot_Type.__name__ = "Integer32"
_PlatformFeatureSlot_Object = MibScalar
platformFeatureSlot = _PlatformFeatureSlot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 3, 1, 5),
    _PlatformFeatureSlot_Type()
)
platformFeatureSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformFeatureSlot.setStatus("mandatory")
_IbmIROCrouting_ObjectIdentity = ObjectIdentity
ibmIROCrouting = _IbmIROCrouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4)
)
_IbmIROCroutingppp_ObjectIdentity = ObjectIdentity
ibmIROCroutingppp = _IbmIROCroutingppp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2)
)
_PppProtocolTable_Object = MibTable
pppProtocolTable = _PppProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1)
)
if mibBuilder.loadTexts:
    pppProtocolTable.setStatus("mandatory")
_PppProtocolEntry_Object = MibTableRow
pppProtocolEntry = _PppProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1)
)
pppProtocolEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppProtocolIfIndex"),
    (0, "IBMIROC-MIB", "pppProtocolId"),
)
if mibBuilder.loadTexts:
    pppProtocolEntry.setStatus("mandatory")


class _PppProtocolIfIndex_Type(Integer32):
    """Custom type pppProtocolIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppProtocolIfIndex_Type.__name__ = "Integer32"
_PppProtocolIfIndex_Object = MibTableColumn
pppProtocolIfIndex = _PppProtocolIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 1),
    _PppProtocolIfIndex_Type()
)
pppProtocolIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolIfIndex.setStatus("mandatory")


class _PppProtocolId_Type(Integer32):
    """Custom type pppProtocolId based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 5),
          ("appnhpr", 7),
          ("appnisr", 8),
          ("bandwidth-allocation", 13),
          ("bridge", 4),
          ("compression", 10),
          ("decnet", 2),
          ("encryption", 14),
          ("ip", 1),
          ("ipv6", 15),
          ("ipx", 3),
          ("netbios", 11),
          ("netbios-forw", 12),
          ("osi", 6),
          ("vines", 9))
    )


_PppProtocolId_Type.__name__ = "Integer32"
_PppProtocolId_Object = MibTableColumn
pppProtocolId = _PppProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 2),
    _PppProtocolId_Type()
)
pppProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolId.setStatus("mandatory")


class _PppProtocolRegistered_Type(Integer32):
    """Custom type pppProtocolRegistered based on Integer32"""
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


_PppProtocolRegistered_Type.__name__ = "Integer32"
_PppProtocolRegistered_Object = MibTableColumn
pppProtocolRegistered = _PppProtocolRegistered_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 3),
    _PppProtocolRegistered_Type()
)
pppProtocolRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolRegistered.setStatus("mandatory")


class _PppProtocolState_Type(Integer32):
    """Custom type pppProtocolState based on Integer32"""
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
        *(("ackReceived", 4),
          ("ackSent", 5),
          ("closed", 1),
          ("listen", 2),
          ("opened", 6),
          ("requestSent", 3),
          ("termSent", 7))
    )


_PppProtocolState_Type.__name__ = "Integer32"
_PppProtocolState_Object = MibTableColumn
pppProtocolState = _PppProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 4),
    _PppProtocolState_Type()
)
pppProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolState.setStatus("mandatory")


class _PppProtocolPreviousState_Type(Integer32):
    """Custom type pppProtocolPreviousState based on Integer32"""
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
        *(("ackReceived", 4),
          ("ackSent", 5),
          ("closed", 1),
          ("listen", 2),
          ("opened", 6),
          ("requestSent", 3),
          ("termSent", 7))
    )


_PppProtocolPreviousState_Type.__name__ = "Integer32"
_PppProtocolPreviousState_Object = MibTableColumn
pppProtocolPreviousState = _PppProtocolPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 5),
    _PppProtocolPreviousState_Type()
)
pppProtocolPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolPreviousState.setStatus("mandatory")
_PppProtocolLastTimeChange_Type = TimeTicks
_PppProtocolLastTimeChange_Object = MibTableColumn
pppProtocolLastTimeChange = _PppProtocolLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 6),
    _PppProtocolLastTimeChange_Type()
)
pppProtocolLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolLastTimeChange.setStatus("mandatory")
_PppProtocolCtlInRejects_Type = Counter32
_PppProtocolCtlInRejects_Object = MibTableColumn
pppProtocolCtlInRejects = _PppProtocolCtlInRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 7),
    _PppProtocolCtlInRejects_Type()
)
pppProtocolCtlInRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolCtlInRejects.setStatus("mandatory")
_PppProtocolCtlInOctets_Type = Counter32
_PppProtocolCtlInOctets_Object = MibTableColumn
pppProtocolCtlInOctets = _PppProtocolCtlInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 8),
    _PppProtocolCtlInOctets_Type()
)
pppProtocolCtlInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolCtlInOctets.setStatus("mandatory")
_PppProtocolCtlInPkts_Type = Counter32
_PppProtocolCtlInPkts_Object = MibTableColumn
pppProtocolCtlInPkts = _PppProtocolCtlInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 9),
    _PppProtocolCtlInPkts_Type()
)
pppProtocolCtlInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolCtlInPkts.setStatus("mandatory")
_PppProtocolCtlOutOctets_Type = Counter32
_PppProtocolCtlOutOctets_Object = MibTableColumn
pppProtocolCtlOutOctets = _PppProtocolCtlOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 10),
    _PppProtocolCtlOutOctets_Type()
)
pppProtocolCtlOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolCtlOutOctets.setStatus("mandatory")
_PppProtocolCtlOutPkts_Type = Counter32
_PppProtocolCtlOutPkts_Object = MibTableColumn
pppProtocolCtlOutPkts = _PppProtocolCtlOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 11),
    _PppProtocolCtlOutPkts_Type()
)
pppProtocolCtlOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolCtlOutPkts.setStatus("mandatory")
_PppProtocolDataInRejects_Type = Counter32
_PppProtocolDataInRejects_Object = MibTableColumn
pppProtocolDataInRejects = _PppProtocolDataInRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 12),
    _PppProtocolDataInRejects_Type()
)
pppProtocolDataInRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolDataInRejects.setStatus("mandatory")
_PppProtocolDataInOctets_Type = Counter32
_PppProtocolDataInOctets_Object = MibTableColumn
pppProtocolDataInOctets = _PppProtocolDataInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 13),
    _PppProtocolDataInOctets_Type()
)
pppProtocolDataInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolDataInOctets.setStatus("mandatory")
_PppProtocolDataInPkts_Type = Counter32
_PppProtocolDataInPkts_Object = MibTableColumn
pppProtocolDataInPkts = _PppProtocolDataInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 14),
    _PppProtocolDataInPkts_Type()
)
pppProtocolDataInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolDataInPkts.setStatus("mandatory")
_PppProtocolDataOutOctets_Type = Counter32
_PppProtocolDataOutOctets_Object = MibTableColumn
pppProtocolDataOutOctets = _PppProtocolDataOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 15),
    _PppProtocolDataOutOctets_Type()
)
pppProtocolDataOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolDataOutOctets.setStatus("mandatory")
_PppProtocolDataOutPkts_Type = Counter32
_PppProtocolDataOutPkts_Object = MibTableColumn
pppProtocolDataOutPkts = _PppProtocolDataOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 1, 1, 16),
    _PppProtocolDataOutPkts_Type()
)
pppProtocolDataOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppProtocolDataOutPkts.setStatus("mandatory")
_PppLinkErrTable_Object = MibTable
pppLinkErrTable = _PppLinkErrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2)
)
if mibBuilder.loadTexts:
    pppLinkErrTable.setStatus("mandatory")
_PppLinkErrEntry_Object = MibTableRow
pppLinkErrEntry = _PppLinkErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2, 1)
)
pppLinkErrEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppLinkErrIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkErrEntry.setStatus("mandatory")


class _PppLinkErrIfIndex_Type(Integer32):
    """Custom type pppLinkErrIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppLinkErrIfIndex_Type.__name__ = "Integer32"
_PppLinkErrIfIndex_Object = MibTableColumn
pppLinkErrIfIndex = _PppLinkErrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2, 1, 1),
    _PppLinkErrIfIndex_Type()
)
pppLinkErrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkErrIfIndex.setStatus("mandatory")
_PppLinkErrBadAddrs_Type = Counter32
_PppLinkErrBadAddrs_Object = MibTableColumn
pppLinkErrBadAddrs = _PppLinkErrBadAddrs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2, 1, 2),
    _PppLinkErrBadAddrs_Type()
)
pppLinkErrBadAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkErrBadAddrs.setStatus("mandatory")


class _PppLinkErrLastBadAddr_Type(OctetString):
    """Custom type pppLinkErrLastBadAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PppLinkErrLastBadAddr_Type.__name__ = "OctetString"
_PppLinkErrLastBadAddr_Object = MibTableColumn
pppLinkErrLastBadAddr = _PppLinkErrLastBadAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2, 1, 3),
    _PppLinkErrLastBadAddr_Type()
)
pppLinkErrLastBadAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkErrLastBadAddr.setStatus("mandatory")
_PppLinkErrBadCtrls_Type = Counter32
_PppLinkErrBadCtrls_Object = MibTableColumn
pppLinkErrBadCtrls = _PppLinkErrBadCtrls_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2, 1, 4),
    _PppLinkErrBadCtrls_Type()
)
pppLinkErrBadCtrls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkErrBadCtrls.setStatus("mandatory")


class _PppLinkErrLastBadCtrl_Type(OctetString):
    """Custom type pppLinkErrLastBadCtrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PppLinkErrLastBadCtrl_Type.__name__ = "OctetString"
_PppLinkErrLastBadCtrl_Object = MibTableColumn
pppLinkErrLastBadCtrl = _PppLinkErrLastBadCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2, 1, 5),
    _PppLinkErrLastBadCtrl_Type()
)
pppLinkErrLastBadCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkErrLastBadCtrl.setStatus("mandatory")
_PppLinkErrUnkProtos_Type = Counter32
_PppLinkErrUnkProtos_Object = MibTableColumn
pppLinkErrUnkProtos = _PppLinkErrUnkProtos_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2, 1, 6),
    _PppLinkErrUnkProtos_Type()
)
pppLinkErrUnkProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkErrUnkProtos.setStatus("mandatory")


class _PppLinkErrLastUnkProto_Type(OctetString):
    """Custom type pppLinkErrLastUnkProto based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PppLinkErrLastUnkProto_Type.__name__ = "OctetString"
_PppLinkErrLastUnkProto_Object = MibTableColumn
pppLinkErrLastUnkProto = _PppLinkErrLastUnkProto_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2, 1, 7),
    _PppLinkErrLastUnkProto_Type()
)
pppLinkErrLastUnkProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkErrLastUnkProto.setStatus("mandatory")
_PppLinkErrInvProtos_Type = Counter32
_PppLinkErrInvProtos_Object = MibTableColumn
pppLinkErrInvProtos = _PppLinkErrInvProtos_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2, 1, 8),
    _PppLinkErrInvProtos_Type()
)
pppLinkErrInvProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkErrInvProtos.setStatus("mandatory")


class _PppLinkErrLastInvProto_Type(OctetString):
    """Custom type pppLinkErrLastInvProto based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PppLinkErrLastInvProto_Type.__name__ = "OctetString"
_PppLinkErrLastInvProto_Object = MibTableColumn
pppLinkErrLastInvProto = _PppLinkErrLastInvProto_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2, 1, 9),
    _PppLinkErrLastInvProto_Type()
)
pppLinkErrLastInvProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkErrLastInvProto.setStatus("mandatory")
_PppLinkErrConfigTOs_Type = Counter32
_PppLinkErrConfigTOs_Object = MibTableColumn
pppLinkErrConfigTOs = _PppLinkErrConfigTOs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2, 1, 10),
    _PppLinkErrConfigTOs_Type()
)
pppLinkErrConfigTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkErrConfigTOs.setStatus("mandatory")
_PppLinkErrTermTOs_Type = Counter32
_PppLinkErrTermTOs_Object = MibTableColumn
pppLinkErrTermTOs = _PppLinkErrTermTOs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 2, 1, 11),
    _PppLinkErrTermTOs_Type()
)
pppLinkErrTermTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkErrTermTOs.setStatus("mandatory")
_PppLCProtoTable_Object = MibTable
pppLCProtoTable = _PppLCProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3)
)
if mibBuilder.loadTexts:
    pppLCProtoTable.setStatus("mandatory")
_PppLCProtoEntry_Object = MibTableRow
pppLCProtoEntry = _PppLCProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1)
)
pppLCProtoEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppLCProtoIfIndex"),
)
if mibBuilder.loadTexts:
    pppLCProtoEntry.setStatus("mandatory")


class _PppLCProtoIfIndex_Type(Integer32):
    """Custom type pppLCProtoIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppLCProtoIfIndex_Type.__name__ = "Integer32"
_PppLCProtoIfIndex_Object = MibTableColumn
pppLCProtoIfIndex = _PppLCProtoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 1),
    _PppLCProtoIfIndex_Type()
)
pppLCProtoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoIfIndex.setStatus("mandatory")


class _PppLCProtoState_Type(Integer32):
    """Custom type pppLCProtoState based on Integer32"""
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
        *(("ackReceived", 4),
          ("ackSent", 5),
          ("closed", 1),
          ("listen", 2),
          ("opened", 6),
          ("requestSent", 3),
          ("termSent", 7))
    )


_PppLCProtoState_Type.__name__ = "Integer32"
_PppLCProtoState_Object = MibTableColumn
pppLCProtoState = _PppLCProtoState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 2),
    _PppLCProtoState_Type()
)
pppLCProtoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoState.setStatus("mandatory")


class _PppLCProtoPreviousState_Type(Integer32):
    """Custom type pppLCProtoPreviousState based on Integer32"""
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
        *(("ackReceived", 4),
          ("ackSent", 5),
          ("closed", 1),
          ("listen", 2),
          ("opened", 6),
          ("requestSent", 3),
          ("termSent", 7))
    )


_PppLCProtoPreviousState_Type.__name__ = "Integer32"
_PppLCProtoPreviousState_Object = MibTableColumn
pppLCProtoPreviousState = _PppLCProtoPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 3),
    _PppLCProtoPreviousState_Type()
)
pppLCProtoPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoPreviousState.setStatus("mandatory")
_PppLCProtoLastTimeChange_Type = TimeTicks
_PppLCProtoLastTimeChange_Object = MibTableColumn
pppLCProtoLastTimeChange = _PppLCProtoLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 4),
    _PppLCProtoLastTimeChange_Type()
)
pppLCProtoLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoLastTimeChange.setStatus("mandatory")
_PppLCProtoOutPackets_Type = Counter32
_PppLCProtoOutPackets_Object = MibTableColumn
pppLCProtoOutPackets = _PppLCProtoOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 5),
    _PppLCProtoOutPackets_Type()
)
pppLCProtoOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutPackets.setStatus("mandatory")
_PppLCProtoOutOctets_Type = Counter32
_PppLCProtoOutOctets_Object = MibTableColumn
pppLCProtoOutOctets = _PppLCProtoOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 6),
    _PppLCProtoOutOctets_Type()
)
pppLCProtoOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutOctets.setStatus("mandatory")
_PppLCProtoOutCRs_Type = Counter32
_PppLCProtoOutCRs_Object = MibTableColumn
pppLCProtoOutCRs = _PppLCProtoOutCRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 7),
    _PppLCProtoOutCRs_Type()
)
pppLCProtoOutCRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutCRs.setStatus("mandatory")
_PppLCProtoOutCAs_Type = Counter32
_PppLCProtoOutCAs_Object = MibTableColumn
pppLCProtoOutCAs = _PppLCProtoOutCAs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 8),
    _PppLCProtoOutCAs_Type()
)
pppLCProtoOutCAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutCAs.setStatus("mandatory")
_PppLCProtoOutCNs_Type = Counter32
_PppLCProtoOutCNs_Object = MibTableColumn
pppLCProtoOutCNs = _PppLCProtoOutCNs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 9),
    _PppLCProtoOutCNs_Type()
)
pppLCProtoOutCNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutCNs.setStatus("mandatory")
_PppLCProtoOutCRejs_Type = Counter32
_PppLCProtoOutCRejs_Object = MibTableColumn
pppLCProtoOutCRejs = _PppLCProtoOutCRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 10),
    _PppLCProtoOutCRejs_Type()
)
pppLCProtoOutCRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutCRejs.setStatus("mandatory")
_PppLCProtoOutTRs_Type = Counter32
_PppLCProtoOutTRs_Object = MibTableColumn
pppLCProtoOutTRs = _PppLCProtoOutTRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 11),
    _PppLCProtoOutTRs_Type()
)
pppLCProtoOutTRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutTRs.setStatus("mandatory")
_PppLCProtoOutTAs_Type = Counter32
_PppLCProtoOutTAs_Object = MibTableColumn
pppLCProtoOutTAs = _PppLCProtoOutTAs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 12),
    _PppLCProtoOutTAs_Type()
)
pppLCProtoOutTAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutTAs.setStatus("mandatory")
_PppLCProtoOutCodeRejs_Type = Counter32
_PppLCProtoOutCodeRejs_Object = MibTableColumn
pppLCProtoOutCodeRejs = _PppLCProtoOutCodeRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 13),
    _PppLCProtoOutCodeRejs_Type()
)
pppLCProtoOutCodeRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutCodeRejs.setStatus("mandatory")
_PppLCProtoOutEchoReqs_Type = Counter32
_PppLCProtoOutEchoReqs_Object = MibTableColumn
pppLCProtoOutEchoReqs = _PppLCProtoOutEchoReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 14),
    _PppLCProtoOutEchoReqs_Type()
)
pppLCProtoOutEchoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutEchoReqs.setStatus("mandatory")
_PppLCProtoOutEchoReps_Type = Counter32
_PppLCProtoOutEchoReps_Object = MibTableColumn
pppLCProtoOutEchoReps = _PppLCProtoOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 15),
    _PppLCProtoOutEchoReps_Type()
)
pppLCProtoOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutEchoReps.setStatus("mandatory")
_PppLCProtoOutDiscReqs_Type = Counter32
_PppLCProtoOutDiscReqs_Object = MibTableColumn
pppLCProtoOutDiscReqs = _PppLCProtoOutDiscReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 16),
    _PppLCProtoOutDiscReqs_Type()
)
pppLCProtoOutDiscReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutDiscReqs.setStatus("mandatory")
_PppLCProtoOutResetReqs_Type = Counter32
_PppLCProtoOutResetReqs_Object = MibTableColumn
pppLCProtoOutResetReqs = _PppLCProtoOutResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 17),
    _PppLCProtoOutResetReqs_Type()
)
pppLCProtoOutResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutResetReqs.setStatus("mandatory")
_PppLCProtoOutResetAcks_Type = Counter32
_PppLCProtoOutResetAcks_Object = MibTableColumn
pppLCProtoOutResetAcks = _PppLCProtoOutResetAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 18),
    _PppLCProtoOutResetAcks_Type()
)
pppLCProtoOutResetAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutResetAcks.setStatus("mandatory")
_PppLCProtoOutIdents_Type = Counter32
_PppLCProtoOutIdents_Object = MibTableColumn
pppLCProtoOutIdents = _PppLCProtoOutIdents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 19),
    _PppLCProtoOutIdents_Type()
)
pppLCProtoOutIdents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutIdents.setStatus("mandatory")
_PppLCProtoOutTimeRemains_Type = Counter32
_PppLCProtoOutTimeRemains_Object = MibTableColumn
pppLCProtoOutTimeRemains = _PppLCProtoOutTimeRemains_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 20),
    _PppLCProtoOutTimeRemains_Type()
)
pppLCProtoOutTimeRemains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoOutTimeRemains.setStatus("mandatory")
_PppLCProtoInRejects_Type = Counter32
_PppLCProtoInRejects_Object = MibTableColumn
pppLCProtoInRejects = _PppLCProtoInRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 21),
    _PppLCProtoInRejects_Type()
)
pppLCProtoInRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInRejects.setStatus("mandatory")
_PppLCProtoInPackets_Type = Counter32
_PppLCProtoInPackets_Object = MibTableColumn
pppLCProtoInPackets = _PppLCProtoInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 22),
    _PppLCProtoInPackets_Type()
)
pppLCProtoInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInPackets.setStatus("mandatory")
_PppLCProtoInOctets_Type = Counter32
_PppLCProtoInOctets_Object = MibTableColumn
pppLCProtoInOctets = _PppLCProtoInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 23),
    _PppLCProtoInOctets_Type()
)
pppLCProtoInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInOctets.setStatus("mandatory")
_PppLCProtoInCRs_Type = Counter32
_PppLCProtoInCRs_Object = MibTableColumn
pppLCProtoInCRs = _PppLCProtoInCRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 24),
    _PppLCProtoInCRs_Type()
)
pppLCProtoInCRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInCRs.setStatus("mandatory")
_PppLCProtoInCAs_Type = Counter32
_PppLCProtoInCAs_Object = MibTableColumn
pppLCProtoInCAs = _PppLCProtoInCAs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 25),
    _PppLCProtoInCAs_Type()
)
pppLCProtoInCAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInCAs.setStatus("mandatory")
_PppLCProtoInCNs_Type = Counter32
_PppLCProtoInCNs_Object = MibTableColumn
pppLCProtoInCNs = _PppLCProtoInCNs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 26),
    _PppLCProtoInCNs_Type()
)
pppLCProtoInCNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInCNs.setStatus("mandatory")
_PppLCProtoInCRejs_Type = Counter32
_PppLCProtoInCRejs_Object = MibTableColumn
pppLCProtoInCRejs = _PppLCProtoInCRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 27),
    _PppLCProtoInCRejs_Type()
)
pppLCProtoInCRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInCRejs.setStatus("mandatory")
_PppLCProtoInTRs_Type = Counter32
_PppLCProtoInTRs_Object = MibTableColumn
pppLCProtoInTRs = _PppLCProtoInTRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 28),
    _PppLCProtoInTRs_Type()
)
pppLCProtoInTRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInTRs.setStatus("mandatory")
_PppLCProtoInTAs_Type = Counter32
_PppLCProtoInTAs_Object = MibTableColumn
pppLCProtoInTAs = _PppLCProtoInTAs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 29),
    _PppLCProtoInTAs_Type()
)
pppLCProtoInTAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInTAs.setStatus("mandatory")
_PppLCProtoInCodeRejs_Type = Counter32
_PppLCProtoInCodeRejs_Object = MibTableColumn
pppLCProtoInCodeRejs = _PppLCProtoInCodeRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 30),
    _PppLCProtoInCodeRejs_Type()
)
pppLCProtoInCodeRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInCodeRejs.setStatus("mandatory")
_PppLCProtoInEchoReqs_Type = Counter32
_PppLCProtoInEchoReqs_Object = MibTableColumn
pppLCProtoInEchoReqs = _PppLCProtoInEchoReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 31),
    _PppLCProtoInEchoReqs_Type()
)
pppLCProtoInEchoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInEchoReqs.setStatus("mandatory")
_PppLCProtoInEchoReps_Type = Counter32
_PppLCProtoInEchoReps_Object = MibTableColumn
pppLCProtoInEchoReps = _PppLCProtoInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 32),
    _PppLCProtoInEchoReps_Type()
)
pppLCProtoInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInEchoReps.setStatus("mandatory")
_PppLCProtoInDiscReqs_Type = Counter32
_PppLCProtoInDiscReqs_Object = MibTableColumn
pppLCProtoInDiscReqs = _PppLCProtoInDiscReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 33),
    _PppLCProtoInDiscReqs_Type()
)
pppLCProtoInDiscReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInDiscReqs.setStatus("mandatory")
_PppLCProtoInResetReqs_Type = Counter32
_PppLCProtoInResetReqs_Object = MibTableColumn
pppLCProtoInResetReqs = _PppLCProtoInResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 34),
    _PppLCProtoInResetReqs_Type()
)
pppLCProtoInResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInResetReqs.setStatus("mandatory")
_PppLCProtoInResetAcks_Type = Counter32
_PppLCProtoInResetAcks_Object = MibTableColumn
pppLCProtoInResetAcks = _PppLCProtoInResetAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 35),
    _PppLCProtoInResetAcks_Type()
)
pppLCProtoInResetAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInResetAcks.setStatus("mandatory")
_PppLCProtoInIdents_Type = Counter32
_PppLCProtoInIdents_Object = MibTableColumn
pppLCProtoInIdents = _PppLCProtoInIdents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 36),
    _PppLCProtoInIdents_Type()
)
pppLCProtoInIdents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInIdents.setStatus("mandatory")
_PppLCProtoInTimeRemains_Type = Counter32
_PppLCProtoInTimeRemains_Object = MibTableColumn
pppLCProtoInTimeRemains = _PppLCProtoInTimeRemains_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 3, 1, 37),
    _PppLCProtoInTimeRemains_Type()
)
pppLCProtoInTimeRemains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCProtoInTimeRemains.setStatus("mandatory")
_PppPAPTable_Object = MibTable
pppPAPTable = _PppPAPTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4)
)
if mibBuilder.loadTexts:
    pppPAPTable.setStatus("mandatory")
_PppPAPEntry_Object = MibTableRow
pppPAPEntry = _PppPAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4, 1)
)
pppPAPEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppPAPIfIndex"),
)
if mibBuilder.loadTexts:
    pppPAPEntry.setStatus("mandatory")


class _PppPAPIfIndex_Type(Integer32):
    """Custom type pppPAPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppPAPIfIndex_Type.__name__ = "Integer32"
_PppPAPIfIndex_Object = MibTableColumn
pppPAPIfIndex = _PppPAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4, 1, 1),
    _PppPAPIfIndex_Type()
)
pppPAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPAPIfIndex.setStatus("mandatory")
_PppPAPInPackets_Type = Counter32
_PppPAPInPackets_Object = MibTableColumn
pppPAPInPackets = _PppPAPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4, 1, 2),
    _PppPAPInPackets_Type()
)
pppPAPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPAPInPackets.setStatus("mandatory")
_PppPAPInOctets_Type = Counter32
_PppPAPInOctets_Object = MibTableColumn
pppPAPInOctets = _PppPAPInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4, 1, 3),
    _PppPAPInOctets_Type()
)
pppPAPInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPAPInOctets.setStatus("mandatory")
_PppPAPInRequests_Type = Counter32
_PppPAPInRequests_Object = MibTableColumn
pppPAPInRequests = _PppPAPInRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4, 1, 4),
    _PppPAPInRequests_Type()
)
pppPAPInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPAPInRequests.setStatus("mandatory")
_PppPAPInAcks_Type = Counter32
_PppPAPInAcks_Object = MibTableColumn
pppPAPInAcks = _PppPAPInAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4, 1, 5),
    _PppPAPInAcks_Type()
)
pppPAPInAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPAPInAcks.setStatus("mandatory")
_PppPAPInNacks_Type = Counter32
_PppPAPInNacks_Object = MibTableColumn
pppPAPInNacks = _PppPAPInNacks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4, 1, 6),
    _PppPAPInNacks_Type()
)
pppPAPInNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPAPInNacks.setStatus("mandatory")
_PppPAPOutPackets_Type = Counter32
_PppPAPOutPackets_Object = MibTableColumn
pppPAPOutPackets = _PppPAPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4, 1, 7),
    _PppPAPOutPackets_Type()
)
pppPAPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPAPOutPackets.setStatus("mandatory")
_PppPAPOutOctets_Type = Counter32
_PppPAPOutOctets_Object = MibTableColumn
pppPAPOutOctets = _PppPAPOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4, 1, 8),
    _PppPAPOutOctets_Type()
)
pppPAPOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPAPOutOctets.setStatus("mandatory")
_PppPAPOutRequests_Type = Counter32
_PppPAPOutRequests_Object = MibTableColumn
pppPAPOutRequests = _PppPAPOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4, 1, 9),
    _PppPAPOutRequests_Type()
)
pppPAPOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPAPOutRequests.setStatus("mandatory")
_PppPAPOutAcks_Type = Counter32
_PppPAPOutAcks_Object = MibTableColumn
pppPAPOutAcks = _PppPAPOutAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4, 1, 10),
    _PppPAPOutAcks_Type()
)
pppPAPOutAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPAPOutAcks.setStatus("mandatory")
_PppPAPOutNacks_Type = Counter32
_PppPAPOutNacks_Object = MibTableColumn
pppPAPOutNacks = _PppPAPOutNacks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 4, 1, 11),
    _PppPAPOutNacks_Type()
)
pppPAPOutNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPAPOutNacks.setStatus("mandatory")
_PppCHAPTable_Object = MibTable
pppCHAPTable = _PppCHAPTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5)
)
if mibBuilder.loadTexts:
    pppCHAPTable.setStatus("mandatory")
_PppCHAPEntry_Object = MibTableRow
pppCHAPEntry = _PppCHAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1)
)
pppCHAPEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppCHAPIfIndex"),
)
if mibBuilder.loadTexts:
    pppCHAPEntry.setStatus("mandatory")


class _PppCHAPIfIndex_Type(Integer32):
    """Custom type pppCHAPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppCHAPIfIndex_Type.__name__ = "Integer32"
_PppCHAPIfIndex_Object = MibTableColumn
pppCHAPIfIndex = _PppCHAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 1),
    _PppCHAPIfIndex_Type()
)
pppCHAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPIfIndex.setStatus("mandatory")
_PppCHAPInPackets_Type = Counter32
_PppCHAPInPackets_Object = MibTableColumn
pppCHAPInPackets = _PppCHAPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 2),
    _PppCHAPInPackets_Type()
)
pppCHAPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPInPackets.setStatus("mandatory")
_PppCHAPInOctets_Type = Counter32
_PppCHAPInOctets_Object = MibTableColumn
pppCHAPInOctets = _PppCHAPInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 3),
    _PppCHAPInOctets_Type()
)
pppCHAPInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPInOctets.setStatus("mandatory")
_PppCHAPInChallenges_Type = Counter32
_PppCHAPInChallenges_Object = MibTableColumn
pppCHAPInChallenges = _PppCHAPInChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 4),
    _PppCHAPInChallenges_Type()
)
pppCHAPInChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPInChallenges.setStatus("mandatory")
_PppCHAPInResponses_Type = Counter32
_PppCHAPInResponses_Object = MibTableColumn
pppCHAPInResponses = _PppCHAPInResponses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 5),
    _PppCHAPInResponses_Type()
)
pppCHAPInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPInResponses.setStatus("mandatory")
_PppCHAPInSuccesses_Type = Counter32
_PppCHAPInSuccesses_Object = MibTableColumn
pppCHAPInSuccesses = _PppCHAPInSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 6),
    _PppCHAPInSuccesses_Type()
)
pppCHAPInSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPInSuccesses.setStatus("mandatory")
_PppCHAPInFailures_Type = Counter32
_PppCHAPInFailures_Object = MibTableColumn
pppCHAPInFailures = _PppCHAPInFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 7),
    _PppCHAPInFailures_Type()
)
pppCHAPInFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPInFailures.setStatus("mandatory")
_PppCHAPOutPackets_Type = Counter32
_PppCHAPOutPackets_Object = MibTableColumn
pppCHAPOutPackets = _PppCHAPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 8),
    _PppCHAPOutPackets_Type()
)
pppCHAPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPOutPackets.setStatus("mandatory")
_PppCHAPOutOctets_Type = Counter32
_PppCHAPOutOctets_Object = MibTableColumn
pppCHAPOutOctets = _PppCHAPOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 9),
    _PppCHAPOutOctets_Type()
)
pppCHAPOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPOutOctets.setStatus("mandatory")
_PppCHAPOutChallenges_Type = Counter32
_PppCHAPOutChallenges_Object = MibTableColumn
pppCHAPOutChallenges = _PppCHAPOutChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 10),
    _PppCHAPOutChallenges_Type()
)
pppCHAPOutChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPOutChallenges.setStatus("mandatory")
_PppCHAPOutResponses_Type = Counter32
_PppCHAPOutResponses_Object = MibTableColumn
pppCHAPOutResponses = _PppCHAPOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 11),
    _PppCHAPOutResponses_Type()
)
pppCHAPOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPOutResponses.setStatus("mandatory")
_PppCHAPOutSuccesses_Type = Counter32
_PppCHAPOutSuccesses_Object = MibTableColumn
pppCHAPOutSuccesses = _PppCHAPOutSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 12),
    _PppCHAPOutSuccesses_Type()
)
pppCHAPOutSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPOutSuccesses.setStatus("mandatory")
_PppCHAPOutFailures_Type = Counter32
_PppCHAPOutFailures_Object = MibTableColumn
pppCHAPOutFailures = _PppCHAPOutFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 5, 1, 13),
    _PppCHAPOutFailures_Type()
)
pppCHAPOutFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCHAPOutFailures.setStatus("mandatory")
_PppSPAPTable_Object = MibTable
pppSPAPTable = _PppSPAPTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6)
)
if mibBuilder.loadTexts:
    pppSPAPTable.setStatus("mandatory")
_PppSPAPEntry_Object = MibTableRow
pppSPAPEntry = _PppSPAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1)
)
pppSPAPEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppSPAPIfIndex"),
)
if mibBuilder.loadTexts:
    pppSPAPEntry.setStatus("mandatory")


class _PppSPAPIfIndex_Type(Integer32):
    """Custom type pppSPAPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppSPAPIfIndex_Type.__name__ = "Integer32"
_PppSPAPIfIndex_Object = MibTableColumn
pppSPAPIfIndex = _PppSPAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 1),
    _PppSPAPIfIndex_Type()
)
pppSPAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPIfIndex.setStatus("mandatory")
_PppSPAPInPackets_Type = Counter32
_PppSPAPInPackets_Object = MibTableColumn
pppSPAPInPackets = _PppSPAPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 2),
    _PppSPAPInPackets_Type()
)
pppSPAPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPInPackets.setStatus("mandatory")
_PppSPAPInOctets_Type = Counter32
_PppSPAPInOctets_Object = MibTableColumn
pppSPAPInOctets = _PppSPAPInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 3),
    _PppSPAPInOctets_Type()
)
pppSPAPInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPInOctets.setStatus("mandatory")
_PppSPAPInRequests_Type = Counter32
_PppSPAPInRequests_Object = MibTableColumn
pppSPAPInRequests = _PppSPAPInRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 4),
    _PppSPAPInRequests_Type()
)
pppSPAPInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPInRequests.setStatus("mandatory")
_PppSPAPInAcks_Type = Counter32
_PppSPAPInAcks_Object = MibTableColumn
pppSPAPInAcks = _PppSPAPInAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 5),
    _PppSPAPInAcks_Type()
)
pppSPAPInAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPInAcks.setStatus("mandatory")
_PppSPAPInNacks_Type = Counter32
_PppSPAPInNacks_Object = MibTableColumn
pppSPAPInNacks = _PppSPAPInNacks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 6),
    _PppSPAPInNacks_Type()
)
pppSPAPInNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPInNacks.setStatus("mandatory")
_PppSPAPInDialbacks_Type = Counter32
_PppSPAPInDialbacks_Object = MibTableColumn
pppSPAPInDialbacks = _PppSPAPInDialbacks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 7),
    _PppSPAPInDialbacks_Type()
)
pppSPAPInDialbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPInDialbacks.setStatus("mandatory")
_PppSPAPInPleaseAuthenticates_Type = Counter32
_PppSPAPInPleaseAuthenticates_Object = MibTableColumn
pppSPAPInPleaseAuthenticates = _PppSPAPInPleaseAuthenticates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 8),
    _PppSPAPInPleaseAuthenticates_Type()
)
pppSPAPInPleaseAuthenticates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPInPleaseAuthenticates.setStatus("mandatory")
_PppSPAPInChangePasswords_Type = Counter32
_PppSPAPInChangePasswords_Object = MibTableColumn
pppSPAPInChangePasswords = _PppSPAPInChangePasswords_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 9),
    _PppSPAPInChangePasswords_Type()
)
pppSPAPInChangePasswords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPInChangePasswords.setStatus("mandatory")
_PppSPAPInAlerts_Type = Counter32
_PppSPAPInAlerts_Object = MibTableColumn
pppSPAPInAlerts = _PppSPAPInAlerts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 10),
    _PppSPAPInAlerts_Type()
)
pppSPAPInAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPInAlerts.setStatus("mandatory")
_PppSPAPInAlertAcks_Type = Counter32
_PppSPAPInAlertAcks_Object = MibTableColumn
pppSPAPInAlertAcks = _PppSPAPInAlertAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 11),
    _PppSPAPInAlertAcks_Type()
)
pppSPAPInAlertAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPInAlertAcks.setStatus("mandatory")
_PppSPAPOutPackets_Type = Counter32
_PppSPAPOutPackets_Object = MibTableColumn
pppSPAPOutPackets = _PppSPAPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 12),
    _PppSPAPOutPackets_Type()
)
pppSPAPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPOutPackets.setStatus("mandatory")
_PppSPAPOutOctets_Type = Counter32
_PppSPAPOutOctets_Object = MibTableColumn
pppSPAPOutOctets = _PppSPAPOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 13),
    _PppSPAPOutOctets_Type()
)
pppSPAPOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPOutOctets.setStatus("mandatory")
_PppSPAPOutRequests_Type = Counter32
_PppSPAPOutRequests_Object = MibTableColumn
pppSPAPOutRequests = _PppSPAPOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 14),
    _PppSPAPOutRequests_Type()
)
pppSPAPOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPOutRequests.setStatus("mandatory")
_PppSPAPOutAcks_Type = Counter32
_PppSPAPOutAcks_Object = MibTableColumn
pppSPAPOutAcks = _PppSPAPOutAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 15),
    _PppSPAPOutAcks_Type()
)
pppSPAPOutAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPOutAcks.setStatus("mandatory")
_PppSPAPOutNacks_Type = Counter32
_PppSPAPOutNacks_Object = MibTableColumn
pppSPAPOutNacks = _PppSPAPOutNacks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 16),
    _PppSPAPOutNacks_Type()
)
pppSPAPOutNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPOutNacks.setStatus("mandatory")
_PppSPAPOutDialbacks_Type = Counter32
_PppSPAPOutDialbacks_Object = MibTableColumn
pppSPAPOutDialbacks = _PppSPAPOutDialbacks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 17),
    _PppSPAPOutDialbacks_Type()
)
pppSPAPOutDialbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPOutDialbacks.setStatus("mandatory")
_PppSPAPOutPleaseAuthenticates_Type = Counter32
_PppSPAPOutPleaseAuthenticates_Object = MibTableColumn
pppSPAPOutPleaseAuthenticates = _PppSPAPOutPleaseAuthenticates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 18),
    _PppSPAPOutPleaseAuthenticates_Type()
)
pppSPAPOutPleaseAuthenticates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPOutPleaseAuthenticates.setStatus("mandatory")
_PppSPAPOutChangePasswords_Type = Counter32
_PppSPAPOutChangePasswords_Object = MibTableColumn
pppSPAPOutChangePasswords = _PppSPAPOutChangePasswords_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 19),
    _PppSPAPOutChangePasswords_Type()
)
pppSPAPOutChangePasswords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPOutChangePasswords.setStatus("mandatory")
_PppSPAPOutAlerts_Type = Counter32
_PppSPAPOutAlerts_Object = MibTableColumn
pppSPAPOutAlerts = _PppSPAPOutAlerts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 20),
    _PppSPAPOutAlerts_Type()
)
pppSPAPOutAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPOutAlerts.setStatus("mandatory")
_PppSPAPOutAlertAcks_Type = Counter32
_PppSPAPOutAlertAcks_Object = MibTableColumn
pppSPAPOutAlertAcks = _PppSPAPOutAlertAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 6, 1, 21),
    _PppSPAPOutAlertAcks_Type()
)
pppSPAPOutAlertAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSPAPOutAlertAcks.setStatus("mandatory")
_PppBAPTable_Object = MibTable
pppBAPTable = _PppBAPTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7)
)
if mibBuilder.loadTexts:
    pppBAPTable.setStatus("mandatory")
_PppBAPEntry_Object = MibTableRow
pppBAPEntry = _PppBAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1)
)
pppBAPEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppBAPIfIndex"),
)
if mibBuilder.loadTexts:
    pppBAPEntry.setStatus("mandatory")


class _PppBAPIfIndex_Type(Integer32):
    """Custom type pppBAPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppBAPIfIndex_Type.__name__ = "Integer32"
_PppBAPIfIndex_Object = MibTableColumn
pppBAPIfIndex = _PppBAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 1),
    _PppBAPIfIndex_Type()
)
pppBAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPIfIndex.setStatus("mandatory")
_PppBAPInCallReqs_Type = Counter32
_PppBAPInCallReqs_Object = MibTableColumn
pppBAPInCallReqs = _PppBAPInCallReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 2),
    _PppBAPInCallReqs_Type()
)
pppBAPInCallReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInCallReqs.setStatus("mandatory")
_PppBAPInCallAcks_Type = Counter32
_PppBAPInCallAcks_Object = MibTableColumn
pppBAPInCallAcks = _PppBAPInCallAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 3),
    _PppBAPInCallAcks_Type()
)
pppBAPInCallAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInCallAcks.setStatus("mandatory")
_PppBAPInCallNaks_Type = Counter32
_PppBAPInCallNaks_Object = MibTableColumn
pppBAPInCallNaks = _PppBAPInCallNaks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 4),
    _PppBAPInCallNaks_Type()
)
pppBAPInCallNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInCallNaks.setStatus("mandatory")
_PppBAPInCallRejs_Type = Counter32
_PppBAPInCallRejs_Object = MibTableColumn
pppBAPInCallRejs = _PppBAPInCallRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 5),
    _PppBAPInCallRejs_Type()
)
pppBAPInCallRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInCallRejs.setStatus("mandatory")
_PppBAPInCallBackReqs_Type = Counter32
_PppBAPInCallBackReqs_Object = MibTableColumn
pppBAPInCallBackReqs = _PppBAPInCallBackReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 6),
    _PppBAPInCallBackReqs_Type()
)
pppBAPInCallBackReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInCallBackReqs.setStatus("mandatory")
_PppBAPInCallBackAcks_Type = Counter32
_PppBAPInCallBackAcks_Object = MibTableColumn
pppBAPInCallBackAcks = _PppBAPInCallBackAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 7),
    _PppBAPInCallBackAcks_Type()
)
pppBAPInCallBackAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInCallBackAcks.setStatus("mandatory")
_PppBAPInCallBackNaks_Type = Counter32
_PppBAPInCallBackNaks_Object = MibTableColumn
pppBAPInCallBackNaks = _PppBAPInCallBackNaks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 8),
    _PppBAPInCallBackNaks_Type()
)
pppBAPInCallBackNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInCallBackNaks.setStatus("mandatory")
_PppBAPInCallBackRejs_Type = Counter32
_PppBAPInCallBackRejs_Object = MibTableColumn
pppBAPInCallBackRejs = _PppBAPInCallBackRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 9),
    _PppBAPInCallBackRejs_Type()
)
pppBAPInCallBackRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInCallBackRejs.setStatus("mandatory")
_PppBAPInDropReqs_Type = Counter32
_PppBAPInDropReqs_Object = MibTableColumn
pppBAPInDropReqs = _PppBAPInDropReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 10),
    _PppBAPInDropReqs_Type()
)
pppBAPInDropReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInDropReqs.setStatus("mandatory")
_PppBAPInDropAcks_Type = Counter32
_PppBAPInDropAcks_Object = MibTableColumn
pppBAPInDropAcks = _PppBAPInDropAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 11),
    _PppBAPInDropAcks_Type()
)
pppBAPInDropAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInDropAcks.setStatus("mandatory")
_PppBAPInDropNaks_Type = Counter32
_PppBAPInDropNaks_Object = MibTableColumn
pppBAPInDropNaks = _PppBAPInDropNaks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 12),
    _PppBAPInDropNaks_Type()
)
pppBAPInDropNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInDropNaks.setStatus("mandatory")
_PppBAPInDropRejs_Type = Counter32
_PppBAPInDropRejs_Object = MibTableColumn
pppBAPInDropRejs = _PppBAPInDropRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 13),
    _PppBAPInDropRejs_Type()
)
pppBAPInDropRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInDropRejs.setStatus("mandatory")
_PppBAPInStatSuccs_Type = Counter32
_PppBAPInStatSuccs_Object = MibTableColumn
pppBAPInStatSuccs = _PppBAPInStatSuccs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 14),
    _PppBAPInStatSuccs_Type()
)
pppBAPInStatSuccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInStatSuccs.setStatus("mandatory")
_PppBAPInStatFails_Type = Counter32
_PppBAPInStatFails_Object = MibTableColumn
pppBAPInStatFails = _PppBAPInStatFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 15),
    _PppBAPInStatFails_Type()
)
pppBAPInStatFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPInStatFails.setStatus("mandatory")
_PppBAPOutCallReqs_Type = Counter32
_PppBAPOutCallReqs_Object = MibTableColumn
pppBAPOutCallReqs = _PppBAPOutCallReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 16),
    _PppBAPOutCallReqs_Type()
)
pppBAPOutCallReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutCallReqs.setStatus("mandatory")
_PppBAPOutCallAcks_Type = Counter32
_PppBAPOutCallAcks_Object = MibTableColumn
pppBAPOutCallAcks = _PppBAPOutCallAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 17),
    _PppBAPOutCallAcks_Type()
)
pppBAPOutCallAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutCallAcks.setStatus("mandatory")
_PppBAPOutCallNaks_Type = Counter32
_PppBAPOutCallNaks_Object = MibTableColumn
pppBAPOutCallNaks = _PppBAPOutCallNaks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 18),
    _PppBAPOutCallNaks_Type()
)
pppBAPOutCallNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutCallNaks.setStatus("mandatory")
_PppBAPOutCallRejs_Type = Counter32
_PppBAPOutCallRejs_Object = MibTableColumn
pppBAPOutCallRejs = _PppBAPOutCallRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 19),
    _PppBAPOutCallRejs_Type()
)
pppBAPOutCallRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutCallRejs.setStatus("mandatory")
_PppBAPOutCallBackReqs_Type = Counter32
_PppBAPOutCallBackReqs_Object = MibTableColumn
pppBAPOutCallBackReqs = _PppBAPOutCallBackReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 20),
    _PppBAPOutCallBackReqs_Type()
)
pppBAPOutCallBackReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutCallBackReqs.setStatus("mandatory")
_PppBAPOutCallBackAcks_Type = Counter32
_PppBAPOutCallBackAcks_Object = MibTableColumn
pppBAPOutCallBackAcks = _PppBAPOutCallBackAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 21),
    _PppBAPOutCallBackAcks_Type()
)
pppBAPOutCallBackAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutCallBackAcks.setStatus("mandatory")
_PppBAPOutCallBackNaks_Type = Counter32
_PppBAPOutCallBackNaks_Object = MibTableColumn
pppBAPOutCallBackNaks = _PppBAPOutCallBackNaks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 22),
    _PppBAPOutCallBackNaks_Type()
)
pppBAPOutCallBackNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutCallBackNaks.setStatus("mandatory")
_PppBAPOutCallBackRejs_Type = Counter32
_PppBAPOutCallBackRejs_Object = MibTableColumn
pppBAPOutCallBackRejs = _PppBAPOutCallBackRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 23),
    _PppBAPOutCallBackRejs_Type()
)
pppBAPOutCallBackRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutCallBackRejs.setStatus("mandatory")
_PppBAPOutDropReqs_Type = Counter32
_PppBAPOutDropReqs_Object = MibTableColumn
pppBAPOutDropReqs = _PppBAPOutDropReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 24),
    _PppBAPOutDropReqs_Type()
)
pppBAPOutDropReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutDropReqs.setStatus("mandatory")
_PppBAPOutDropAcks_Type = Counter32
_PppBAPOutDropAcks_Object = MibTableColumn
pppBAPOutDropAcks = _PppBAPOutDropAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 25),
    _PppBAPOutDropAcks_Type()
)
pppBAPOutDropAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutDropAcks.setStatus("mandatory")
_PppBAPOutDropNaks_Type = Counter32
_PppBAPOutDropNaks_Object = MibTableColumn
pppBAPOutDropNaks = _PppBAPOutDropNaks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 26),
    _PppBAPOutDropNaks_Type()
)
pppBAPOutDropNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutDropNaks.setStatus("mandatory")
_PppBAPOutDropRejs_Type = Counter32
_PppBAPOutDropRejs_Object = MibTableColumn
pppBAPOutDropRejs = _PppBAPOutDropRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 27),
    _PppBAPOutDropRejs_Type()
)
pppBAPOutDropRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutDropRejs.setStatus("mandatory")
_PppBAPOutStatSuccs_Type = Counter32
_PppBAPOutStatSuccs_Object = MibTableColumn
pppBAPOutStatSuccs = _PppBAPOutStatSuccs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 28),
    _PppBAPOutStatSuccs_Type()
)
pppBAPOutStatSuccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutStatSuccs.setStatus("mandatory")
_PppBAPOutStatFails_Type = Counter32
_PppBAPOutStatFails_Object = MibTableColumn
pppBAPOutStatFails = _PppBAPOutStatFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 7, 1, 29),
    _PppBAPOutStatFails_Type()
)
pppBAPOutStatFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBAPOutStatFails.setStatus("mandatory")
_PppCPTable_Object = MibTable
pppCPTable = _PppCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8)
)
if mibBuilder.loadTexts:
    pppCPTable.setStatus("mandatory")
_PppCPEntry_Object = MibTableRow
pppCPEntry = _PppCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1)
)
pppCPEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppCPIfIndex"),
)
if mibBuilder.loadTexts:
    pppCPEntry.setStatus("mandatory")


class _PppCPIfIndex_Type(Integer32):
    """Custom type pppCPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppCPIfIndex_Type.__name__ = "Integer32"
_PppCPIfIndex_Object = MibTableColumn
pppCPIfIndex = _PppCPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 1),
    _PppCPIfIndex_Type()
)
pppCPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCPIfIndex.setStatus("mandatory")
_PppCPInCompressedOctets_Type = Counter32
_PppCPInCompressedOctets_Object = MibTableColumn
pppCPInCompressedOctets = _PppCPInCompressedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 2),
    _PppCPInCompressedOctets_Type()
)
pppCPInCompressedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCPInCompressedOctets.setStatus("mandatory")
_PppCPInInCompressablePkts_Type = Counter32
_PppCPInInCompressablePkts_Object = MibTableColumn
pppCPInInCompressablePkts = _PppCPInInCompressablePkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 3),
    _PppCPInInCompressablePkts_Type()
)
pppCPInInCompressablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCPInInCompressablePkts.setStatus("mandatory")
_PppCPInDestroyeds_Type = Counter32
_PppCPInDestroyeds_Object = MibTableColumn
pppCPInDestroyeds = _PppCPInDestroyeds_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 4),
    _PppCPInDestroyeds_Type()
)
pppCPInDestroyeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCPInDestroyeds.setStatus("mandatory")
_PppCPInCopies_Type = Counter32
_PppCPInCopies_Object = MibTableColumn
pppCPInCopies = _PppCPInCopies_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 5),
    _PppCPInCopies_Type()
)
pppCPInCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCPInCopies.setStatus("mandatory")
_PppCPOutCompressedOctets_Type = Counter32
_PppCPOutCompressedOctets_Object = MibTableColumn
pppCPOutCompressedOctets = _PppCPOutCompressedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 6),
    _PppCPOutCompressedOctets_Type()
)
pppCPOutCompressedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCPOutCompressedOctets.setStatus("mandatory")
_PppCPOutInCompressablePkts_Type = Counter32
_PppCPOutInCompressablePkts_Object = MibTableColumn
pppCPOutInCompressablePkts = _PppCPOutInCompressablePkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 7),
    _PppCPOutInCompressablePkts_Type()
)
pppCPOutInCompressablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCPOutInCompressablePkts.setStatus("mandatory")
_PppCPOutDestroyeds_Type = Counter32
_PppCPOutDestroyeds_Object = MibTableColumn
pppCPOutDestroyeds = _PppCPOutDestroyeds_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 8),
    _PppCPOutDestroyeds_Type()
)
pppCPOutDestroyeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCPOutDestroyeds.setStatus("mandatory")
_PppCPOutCopies_Type = Counter32
_PppCPOutCopies_Object = MibTableColumn
pppCPOutCopies = _PppCPOutCopies_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 9),
    _PppCPOutCopies_Type()
)
pppCPOutCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCPOutCopies.setStatus("mandatory")
_PppCCPInResetReqs_Type = Counter32
_PppCCPInResetReqs_Object = MibTableColumn
pppCCPInResetReqs = _PppCCPInResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 10),
    _PppCCPInResetReqs_Type()
)
pppCCPInResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCCPInResetReqs.setStatus("mandatory")
_PppCCPInResetAcks_Type = Counter32
_PppCCPInResetAcks_Object = MibTableColumn
pppCCPInResetAcks = _PppCCPInResetAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 11),
    _PppCCPInResetAcks_Type()
)
pppCCPInResetAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCCPInResetAcks.setStatus("mandatory")
_PppCCPInDictResets_Type = Counter32
_PppCCPInDictResets_Object = MibTableColumn
pppCCPInDictResets = _PppCCPInDictResets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 12),
    _PppCCPInDictResets_Type()
)
pppCCPInDictResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCCPInDictResets.setStatus("mandatory")
_PppCCPOutResetReqs_Type = Counter32
_PppCCPOutResetReqs_Object = MibTableColumn
pppCCPOutResetReqs = _PppCCPOutResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 13),
    _PppCCPOutResetReqs_Type()
)
pppCCPOutResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCCPOutResetReqs.setStatus("mandatory")
_PppCCPOutResetAcks_Type = Counter32
_PppCCPOutResetAcks_Object = MibTableColumn
pppCCPOutResetAcks = _PppCCPOutResetAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 14),
    _PppCCPOutResetAcks_Type()
)
pppCCPOutResetAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCCPOutResetAcks.setStatus("mandatory")
_PppCCPOutDictResets_Type = Counter32
_PppCCPOutDictResets_Object = MibTableColumn
pppCCPOutDictResets = _PppCCPOutDictResets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 15),
    _PppCCPOutDictResets_Type()
)
pppCCPOutDictResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCCPOutDictResets.setStatus("mandatory")
_PppCCPPacketDiscards_Type = Counter32
_PppCCPPacketDiscards_Object = MibTableColumn
pppCCPPacketDiscards = _PppCCPPacketDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 16),
    _PppCCPPacketDiscards_Type()
)
pppCCPPacketDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCCPPacketDiscards.setStatus("mandatory")
_PppCCPOctetDiscards_Type = Counter32
_PppCCPOctetDiscards_Object = MibTableColumn
pppCCPOctetDiscards = _PppCCPOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 8, 1, 17),
    _PppCCPOctetDiscards_Type()
)
pppCCPOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCCPOctetDiscards.setStatus("mandatory")
_PppEPTable_Object = MibTable
pppEPTable = _PppEPTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9)
)
if mibBuilder.loadTexts:
    pppEPTable.setStatus("mandatory")
_PppEPEntry_Object = MibTableRow
pppEPEntry = _PppEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1)
)
pppEPEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppEPIfIndex"),
)
if mibBuilder.loadTexts:
    pppEPEntry.setStatus("mandatory")


class _PppEPIfIndex_Type(Integer32):
    """Custom type pppEPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppEPIfIndex_Type.__name__ = "Integer32"
_PppEPIfIndex_Object = MibTableColumn
pppEPIfIndex = _PppEPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 1),
    _PppEPIfIndex_Type()
)
pppEPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEPIfIndex.setStatus("mandatory")
_PppEPInEncryptedOctets_Type = Counter32
_PppEPInEncryptedOctets_Object = MibTableColumn
pppEPInEncryptedOctets = _PppEPInEncryptedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 2),
    _PppEPInEncryptedOctets_Type()
)
pppEPInEncryptedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEPInEncryptedOctets.setStatus("mandatory")
_PppEPInDestroyeds_Type = Counter32
_PppEPInDestroyeds_Object = MibTableColumn
pppEPInDestroyeds = _PppEPInDestroyeds_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 3),
    _PppEPInDestroyeds_Type()
)
pppEPInDestroyeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEPInDestroyeds.setStatus("mandatory")
_PppEPInCopies_Type = Counter32
_PppEPInCopies_Object = MibTableColumn
pppEPInCopies = _PppEPInCopies_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 4),
    _PppEPInCopies_Type()
)
pppEPInCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEPInCopies.setStatus("mandatory")
_PppEPOutEncryptedOctets_Type = Counter32
_PppEPOutEncryptedOctets_Object = MibTableColumn
pppEPOutEncryptedOctets = _PppEPOutEncryptedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 5),
    _PppEPOutEncryptedOctets_Type()
)
pppEPOutEncryptedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEPOutEncryptedOctets.setStatus("mandatory")
_PppEPOutDestroyeds_Type = Counter32
_PppEPOutDestroyeds_Object = MibTableColumn
pppEPOutDestroyeds = _PppEPOutDestroyeds_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 6),
    _PppEPOutDestroyeds_Type()
)
pppEPOutDestroyeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEPOutDestroyeds.setStatus("mandatory")
_PppEPOutCopies_Type = Counter32
_PppEPOutCopies_Object = MibTableColumn
pppEPOutCopies = _PppEPOutCopies_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 7),
    _PppEPOutCopies_Type()
)
pppEPOutCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEPOutCopies.setStatus("mandatory")
_PppECPInResetReqs_Type = Counter32
_PppECPInResetReqs_Object = MibTableColumn
pppECPInResetReqs = _PppECPInResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 8),
    _PppECPInResetReqs_Type()
)
pppECPInResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppECPInResetReqs.setStatus("mandatory")
_PppECPInResetAcks_Type = Counter32
_PppECPInResetAcks_Object = MibTableColumn
pppECPInResetAcks = _PppECPInResetAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 9),
    _PppECPInResetAcks_Type()
)
pppECPInResetAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppECPInResetAcks.setStatus("mandatory")
_PppECPInDictResets_Type = Counter32
_PppECPInDictResets_Object = MibTableColumn
pppECPInDictResets = _PppECPInDictResets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 10),
    _PppECPInDictResets_Type()
)
pppECPInDictResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppECPInDictResets.setStatus("mandatory")
_PppECPOutResetReqs_Type = Counter32
_PppECPOutResetReqs_Object = MibTableColumn
pppECPOutResetReqs = _PppECPOutResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 11),
    _PppECPOutResetReqs_Type()
)
pppECPOutResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppECPOutResetReqs.setStatus("mandatory")
_PppECPOutResetAcks_Type = Counter32
_PppECPOutResetAcks_Object = MibTableColumn
pppECPOutResetAcks = _PppECPOutResetAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 12),
    _PppECPOutResetAcks_Type()
)
pppECPOutResetAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppECPOutResetAcks.setStatus("mandatory")
_PppECPOutDictResets_Type = Counter32
_PppECPOutDictResets_Object = MibTableColumn
pppECPOutDictResets = _PppECPOutDictResets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 13),
    _PppECPOutDictResets_Type()
)
pppECPOutDictResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppECPOutDictResets.setStatus("mandatory")
_PppECPPacketDiscards_Type = Counter32
_PppECPPacketDiscards_Object = MibTableColumn
pppECPPacketDiscards = _PppECPPacketDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 14),
    _PppECPPacketDiscards_Type()
)
pppECPPacketDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppECPPacketDiscards.setStatus("mandatory")
_PppECPOctetDiscards_Type = Counter32
_PppECPOctetDiscards_Object = MibTableColumn
pppECPOctetDiscards = _PppECPOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 9, 1, 15),
    _PppECPOctetDiscards_Type()
)
pppECPOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppECPOctetDiscards.setStatus("mandatory")
_PppMSCHAPTable_Object = MibTable
pppMSCHAPTable = _PppMSCHAPTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10)
)
if mibBuilder.loadTexts:
    pppMSCHAPTable.setStatus("mandatory")
_PppMSCHAPEntry_Object = MibTableRow
pppMSCHAPEntry = _PppMSCHAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1)
)
pppMSCHAPEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppMSCHAPIfIndex"),
)
if mibBuilder.loadTexts:
    pppMSCHAPEntry.setStatus("mandatory")


class _PppMSCHAPIfIndex_Type(Integer32):
    """Custom type pppMSCHAPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppMSCHAPIfIndex_Type.__name__ = "Integer32"
_PppMSCHAPIfIndex_Object = MibTableColumn
pppMSCHAPIfIndex = _PppMSCHAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 1),
    _PppMSCHAPIfIndex_Type()
)
pppMSCHAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPIfIndex.setStatus("mandatory")
_PppMSCHAPInPackets_Type = Counter32
_PppMSCHAPInPackets_Object = MibTableColumn
pppMSCHAPInPackets = _PppMSCHAPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 2),
    _PppMSCHAPInPackets_Type()
)
pppMSCHAPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInPackets.setStatus("mandatory")
_PppMSCHAPInOctets_Type = Counter32
_PppMSCHAPInOctets_Object = MibTableColumn
pppMSCHAPInOctets = _PppMSCHAPInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 3),
    _PppMSCHAPInOctets_Type()
)
pppMSCHAPInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInOctets.setStatus("mandatory")
_PppMSCHAPInChallenges_Type = Counter32
_PppMSCHAPInChallenges_Object = MibTableColumn
pppMSCHAPInChallenges = _PppMSCHAPInChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 4),
    _PppMSCHAPInChallenges_Type()
)
pppMSCHAPInChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInChallenges.setStatus("mandatory")
_PppMSCHAPInResponses_Type = Counter32
_PppMSCHAPInResponses_Object = MibTableColumn
pppMSCHAPInResponses = _PppMSCHAPInResponses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 5),
    _PppMSCHAPInResponses_Type()
)
pppMSCHAPInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInResponses.setStatus("mandatory")
_PppMSCHAPInSuccesses_Type = Counter32
_PppMSCHAPInSuccesses_Object = MibTableColumn
pppMSCHAPInSuccesses = _PppMSCHAPInSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 6),
    _PppMSCHAPInSuccesses_Type()
)
pppMSCHAPInSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInSuccesses.setStatus("mandatory")
_PppMSCHAPInFailures_Type = Counter32
_PppMSCHAPInFailures_Object = MibTableColumn
pppMSCHAPInFailures = _PppMSCHAPInFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 7),
    _PppMSCHAPInFailures_Type()
)
pppMSCHAPInFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInFailures.setStatus("mandatory")
_PppMSCHAPInChangePasswords_Type = Counter32
_PppMSCHAPInChangePasswords_Object = MibTableColumn
pppMSCHAPInChangePasswords = _PppMSCHAPInChangePasswords_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 8),
    _PppMSCHAPInChangePasswords_Type()
)
pppMSCHAPInChangePasswords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInChangePasswords.setStatus("mandatory")
_PppMSCHAPInRestrictedHoursFailures_Type = Counter32
_PppMSCHAPInRestrictedHoursFailures_Object = MibTableColumn
pppMSCHAPInRestrictedHoursFailures = _PppMSCHAPInRestrictedHoursFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 9),
    _PppMSCHAPInRestrictedHoursFailures_Type()
)
pppMSCHAPInRestrictedHoursFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInRestrictedHoursFailures.setStatus("mandatory")
_PppMSCHAPInAccountDisabledFailures_Type = Counter32
_PppMSCHAPInAccountDisabledFailures_Object = MibTableColumn
pppMSCHAPInAccountDisabledFailures = _PppMSCHAPInAccountDisabledFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 10),
    _PppMSCHAPInAccountDisabledFailures_Type()
)
pppMSCHAPInAccountDisabledFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInAccountDisabledFailures.setStatus("mandatory")
_PppMSCHAPInPasswordExpiredFailures_Type = Counter32
_PppMSCHAPInPasswordExpiredFailures_Object = MibTableColumn
pppMSCHAPInPasswordExpiredFailures = _PppMSCHAPInPasswordExpiredFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 11),
    _PppMSCHAPInPasswordExpiredFailures_Type()
)
pppMSCHAPInPasswordExpiredFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInPasswordExpiredFailures.setStatus("mandatory")
_PppMSCHAPInNoPermissionFailures_Type = Counter32
_PppMSCHAPInNoPermissionFailures_Object = MibTableColumn
pppMSCHAPInNoPermissionFailures = _PppMSCHAPInNoPermissionFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 12),
    _PppMSCHAPInNoPermissionFailures_Type()
)
pppMSCHAPInNoPermissionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInNoPermissionFailures.setStatus("mandatory")
_PppMSCHAPInAuthenticationFailures_Type = Counter32
_PppMSCHAPInAuthenticationFailures_Object = MibTableColumn
pppMSCHAPInAuthenticationFailures = _PppMSCHAPInAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 13),
    _PppMSCHAPInAuthenticationFailures_Type()
)
pppMSCHAPInAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInAuthenticationFailures.setStatus("mandatory")
_PppMSCHAPInChangePasswordFailures_Type = Counter32
_PppMSCHAPInChangePasswordFailures_Object = MibTableColumn
pppMSCHAPInChangePasswordFailures = _PppMSCHAPInChangePasswordFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 14),
    _PppMSCHAPInChangePasswordFailures_Type()
)
pppMSCHAPInChangePasswordFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPInChangePasswordFailures.setStatus("mandatory")
_PppMSCHAPOutPackets_Type = Counter32
_PppMSCHAPOutPackets_Object = MibTableColumn
pppMSCHAPOutPackets = _PppMSCHAPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 15),
    _PppMSCHAPOutPackets_Type()
)
pppMSCHAPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutPackets.setStatus("mandatory")
_PppMSCHAPOutOctets_Type = Counter32
_PppMSCHAPOutOctets_Object = MibTableColumn
pppMSCHAPOutOctets = _PppMSCHAPOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 16),
    _PppMSCHAPOutOctets_Type()
)
pppMSCHAPOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutOctets.setStatus("mandatory")
_PppMSCHAPOutChallenges_Type = Counter32
_PppMSCHAPOutChallenges_Object = MibTableColumn
pppMSCHAPOutChallenges = _PppMSCHAPOutChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 17),
    _PppMSCHAPOutChallenges_Type()
)
pppMSCHAPOutChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutChallenges.setStatus("mandatory")
_PppMSCHAPOutResponses_Type = Counter32
_PppMSCHAPOutResponses_Object = MibTableColumn
pppMSCHAPOutResponses = _PppMSCHAPOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 18),
    _PppMSCHAPOutResponses_Type()
)
pppMSCHAPOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutResponses.setStatus("mandatory")
_PppMSCHAPOutSuccesses_Type = Counter32
_PppMSCHAPOutSuccesses_Object = MibTableColumn
pppMSCHAPOutSuccesses = _PppMSCHAPOutSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 19),
    _PppMSCHAPOutSuccesses_Type()
)
pppMSCHAPOutSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutSuccesses.setStatus("mandatory")
_PppMSCHAPOutFailures_Type = Counter32
_PppMSCHAPOutFailures_Object = MibTableColumn
pppMSCHAPOutFailures = _PppMSCHAPOutFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 20),
    _PppMSCHAPOutFailures_Type()
)
pppMSCHAPOutFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutFailures.setStatus("mandatory")
_PppMSCHAPOutChangePasswords_Type = Counter32
_PppMSCHAPOutChangePasswords_Object = MibTableColumn
pppMSCHAPOutChangePasswords = _PppMSCHAPOutChangePasswords_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 21),
    _PppMSCHAPOutChangePasswords_Type()
)
pppMSCHAPOutChangePasswords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutChangePasswords.setStatus("mandatory")
_PppMSCHAPOutRestrictedHoursFailures_Type = Counter32
_PppMSCHAPOutRestrictedHoursFailures_Object = MibTableColumn
pppMSCHAPOutRestrictedHoursFailures = _PppMSCHAPOutRestrictedHoursFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 22),
    _PppMSCHAPOutRestrictedHoursFailures_Type()
)
pppMSCHAPOutRestrictedHoursFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutRestrictedHoursFailures.setStatus("mandatory")
_PppMSCHAPOutAccountDisabledFailures_Type = Counter32
_PppMSCHAPOutAccountDisabledFailures_Object = MibTableColumn
pppMSCHAPOutAccountDisabledFailures = _PppMSCHAPOutAccountDisabledFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 23),
    _PppMSCHAPOutAccountDisabledFailures_Type()
)
pppMSCHAPOutAccountDisabledFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutAccountDisabledFailures.setStatus("mandatory")
_PppMSCHAPOutPasswordExpiredFailures_Type = Counter32
_PppMSCHAPOutPasswordExpiredFailures_Object = MibTableColumn
pppMSCHAPOutPasswordExpiredFailures = _PppMSCHAPOutPasswordExpiredFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 24),
    _PppMSCHAPOutPasswordExpiredFailures_Type()
)
pppMSCHAPOutPasswordExpiredFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutPasswordExpiredFailures.setStatus("mandatory")
_PppMSCHAPOutNoPermissionFailures_Type = Counter32
_PppMSCHAPOutNoPermissionFailures_Object = MibTableColumn
pppMSCHAPOutNoPermissionFailures = _PppMSCHAPOutNoPermissionFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 25),
    _PppMSCHAPOutNoPermissionFailures_Type()
)
pppMSCHAPOutNoPermissionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutNoPermissionFailures.setStatus("mandatory")
_PppMSCHAPOutAuthenticationFailures_Type = Counter32
_PppMSCHAPOutAuthenticationFailures_Object = MibTableColumn
pppMSCHAPOutAuthenticationFailures = _PppMSCHAPOutAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 26),
    _PppMSCHAPOutAuthenticationFailures_Type()
)
pppMSCHAPOutAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutAuthenticationFailures.setStatus("mandatory")
_PppMSCHAPOutChangePasswordFailures_Type = Counter32
_PppMSCHAPOutChangePasswordFailures_Object = MibTableColumn
pppMSCHAPOutChangePasswordFailures = _PppMSCHAPOutChangePasswordFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 10, 1, 27),
    _PppMSCHAPOutChangePasswordFailures_Type()
)
pppMSCHAPOutChangePasswordFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMSCHAPOutChangePasswordFailures.setStatus("mandatory")
_PppCBCPTable_Object = MibTable
pppCBCPTable = _PppCBCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 11)
)
if mibBuilder.loadTexts:
    pppCBCPTable.setStatus("mandatory")
_PppCBCPEntry_Object = MibTableRow
pppCBCPEntry = _PppCBCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 11, 1)
)
pppCBCPEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppCBCPIfIndex"),
)
if mibBuilder.loadTexts:
    pppCBCPEntry.setStatus("mandatory")


class _PppCBCPIfIndex_Type(Integer32):
    """Custom type pppCBCPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppCBCPIfIndex_Type.__name__ = "Integer32"
_PppCBCPIfIndex_Object = MibTableColumn
pppCBCPIfIndex = _PppCBCPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 11, 1, 1),
    _PppCBCPIfIndex_Type()
)
pppCBCPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCBCPIfIndex.setStatus("mandatory")
_PppCBCPInPackets_Type = Counter32
_PppCBCPInPackets_Object = MibTableColumn
pppCBCPInPackets = _PppCBCPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 11, 1, 2),
    _PppCBCPInPackets_Type()
)
pppCBCPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCBCPInPackets.setStatus("mandatory")
_PppCBCPInOctets_Type = Counter32
_PppCBCPInOctets_Object = MibTableColumn
pppCBCPInOctets = _PppCBCPInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 11, 1, 3),
    _PppCBCPInOctets_Type()
)
pppCBCPInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCBCPInOctets.setStatus("mandatory")
_PppCBCPOutPackets_Type = Counter32
_PppCBCPOutPackets_Object = MibTableColumn
pppCBCPOutPackets = _PppCBCPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 11, 1, 4),
    _PppCBCPOutPackets_Type()
)
pppCBCPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCBCPOutPackets.setStatus("mandatory")
_PppCBCPOutOctets_Type = Counter32
_PppCBCPOutOctets_Object = MibTableColumn
pppCBCPOutOctets = _PppCBCPOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 11, 1, 5),
    _PppCBCPOutOctets_Type()
)
pppCBCPOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCBCPOutOctets.setStatus("mandatory")
_PppCBCPAttempts_Type = Counter32
_PppCBCPAttempts_Object = MibTableColumn
pppCBCPAttempts = _PppCBCPAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 11, 1, 6),
    _PppCBCPAttempts_Type()
)
pppCBCPAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCBCPAttempts.setStatus("mandatory")
_PppCBCPSuccess_Type = Counter32
_PppCBCPSuccess_Object = MibTableColumn
pppCBCPSuccess = _PppCBCPSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 11, 1, 7),
    _PppCBCPSuccess_Type()
)
pppCBCPSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppCBCPSuccess.setStatus("mandatory")
_PppEAPTable_Object = MibTable
pppEAPTable = _PppEAPTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12)
)
if mibBuilder.loadTexts:
    pppEAPTable.setStatus("mandatory")
_PppEAPEntry_Object = MibTableRow
pppEAPEntry = _PppEAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12, 1)
)
pppEAPEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppEAPIfIndex"),
)
if mibBuilder.loadTexts:
    pppEAPEntry.setStatus("mandatory")


class _PppEAPIfIndex_Type(Integer32):
    """Custom type pppEAPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppEAPIfIndex_Type.__name__ = "Integer32"
_PppEAPIfIndex_Object = MibTableColumn
pppEAPIfIndex = _PppEAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12, 1, 1),
    _PppEAPIfIndex_Type()
)
pppEAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEAPIfIndex.setStatus("mandatory")
_PppEAPInPackets_Type = Counter32
_PppEAPInPackets_Object = MibTableColumn
pppEAPInPackets = _PppEAPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12, 1, 2),
    _PppEAPInPackets_Type()
)
pppEAPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEAPInPackets.setStatus("mandatory")
_PppEAPInOctets_Type = Counter32
_PppEAPInOctets_Object = MibTableColumn
pppEAPInOctets = _PppEAPInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12, 1, 3),
    _PppEAPInOctets_Type()
)
pppEAPInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEAPInOctets.setStatus("mandatory")
_PppEAPInRequests_Type = Counter32
_PppEAPInRequests_Object = MibTableColumn
pppEAPInRequests = _PppEAPInRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12, 1, 4),
    _PppEAPInRequests_Type()
)
pppEAPInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEAPInRequests.setStatus("mandatory")
_PppEAPInAcks_Type = Counter32
_PppEAPInAcks_Object = MibTableColumn
pppEAPInAcks = _PppEAPInAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12, 1, 5),
    _PppEAPInAcks_Type()
)
pppEAPInAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEAPInAcks.setStatus("mandatory")
_PppEAPInNaks_Type = Counter32
_PppEAPInNaks_Object = MibTableColumn
pppEAPInNaks = _PppEAPInNaks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12, 1, 6),
    _PppEAPInNaks_Type()
)
pppEAPInNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEAPInNaks.setStatus("mandatory")
_PppEAPOutPackets_Type = Counter32
_PppEAPOutPackets_Object = MibTableColumn
pppEAPOutPackets = _PppEAPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12, 1, 7),
    _PppEAPOutPackets_Type()
)
pppEAPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEAPOutPackets.setStatus("mandatory")
_PppEAPOutOctets_Type = Counter32
_PppEAPOutOctets_Object = MibTableColumn
pppEAPOutOctets = _PppEAPOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12, 1, 8),
    _PppEAPOutOctets_Type()
)
pppEAPOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEAPOutOctets.setStatus("mandatory")
_PppEAPOutRequests_Type = Counter32
_PppEAPOutRequests_Object = MibTableColumn
pppEAPOutRequests = _PppEAPOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12, 1, 9),
    _PppEAPOutRequests_Type()
)
pppEAPOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEAPOutRequests.setStatus("mandatory")
_PppEAPOutAcks_Type = Counter32
_PppEAPOutAcks_Object = MibTableColumn
pppEAPOutAcks = _PppEAPOutAcks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12, 1, 10),
    _PppEAPOutAcks_Type()
)
pppEAPOutAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEAPOutAcks.setStatus("mandatory")
_PppEAPOutNaks_Type = Counter32
_PppEAPOutNaks_Object = MibTableColumn
pppEAPOutNaks = _PppEAPOutNaks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 12, 1, 11),
    _PppEAPOutNaks_Type()
)
pppEAPOutNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppEAPOutNaks.setStatus("mandatory")
_PppMPPETable_Object = MibTable
pppMPPETable = _PppMPPETable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 13)
)
if mibBuilder.loadTexts:
    pppMPPETable.setStatus("mandatory")
_PppMPPEEntry_Object = MibTableRow
pppMPPEEntry = _PppMPPEEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 13, 1)
)
pppMPPEEntry.setIndexNames(
    (0, "IBMIROC-MIB", "pppMPPEIfIndex"),
)
if mibBuilder.loadTexts:
    pppMPPEEntry.setStatus("mandatory")


class _PppMPPEIfIndex_Type(Integer32):
    """Custom type pppMPPEIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppMPPEIfIndex_Type.__name__ = "Integer32"
_PppMPPEIfIndex_Object = MibTableColumn
pppMPPEIfIndex = _PppMPPEIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 13, 1, 1),
    _PppMPPEIfIndex_Type()
)
pppMPPEIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMPPEIfIndex.setStatus("mandatory")
_PppMPPEInPackets_Type = Counter32
_PppMPPEInPackets_Object = MibTableColumn
pppMPPEInPackets = _PppMPPEInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 13, 1, 2),
    _PppMPPEInPackets_Type()
)
pppMPPEInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMPPEInPackets.setStatus("mandatory")
_PppMPPEInOctets_Type = Counter32
_PppMPPEInOctets_Object = MibTableColumn
pppMPPEInOctets = _PppMPPEInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 13, 1, 3),
    _PppMPPEInOctets_Type()
)
pppMPPEInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMPPEInOctets.setStatus("mandatory")
_PppMPPEInDestroyed_Type = Counter32
_PppMPPEInDestroyed_Object = MibTableColumn
pppMPPEInDestroyed = _PppMPPEInDestroyed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 13, 1, 4),
    _PppMPPEInDestroyed_Type()
)
pppMPPEInDestroyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMPPEInDestroyed.setStatus("mandatory")
_PppMPPEOutPackets_Type = Counter32
_PppMPPEOutPackets_Object = MibTableColumn
pppMPPEOutPackets = _PppMPPEOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 13, 1, 5),
    _PppMPPEOutPackets_Type()
)
pppMPPEOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMPPEOutPackets.setStatus("mandatory")
_PppMPPEOutOctets_Type = Counter32
_PppMPPEOutOctets_Object = MibTableColumn
pppMPPEOutOctets = _PppMPPEOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 13, 1, 6),
    _PppMPPEOutOctets_Type()
)
pppMPPEOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMPPEOutOctets.setStatus("mandatory")
_PppMPPEOutDestroyed_Type = Counter32
_PppMPPEOutDestroyed_Object = MibTableColumn
pppMPPEOutDestroyed = _PppMPPEOutDestroyed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 2, 13, 1, 7),
    _PppMPPEOutDestroyed_Type()
)
pppMPPEOutDestroyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppMPPEOutDestroyed.setStatus("mandatory")
_IbmIROCroutingdlsw_ObjectIdentity = ObjectIdentity
ibmIROCroutingdlsw = _IbmIROCroutingdlsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3)
)
_IbmdlswTConnGroupOperTable_Object = MibTable
ibmdlswTConnGroupOperTable = _IbmdlswTConnGroupOperTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperTable.setStatus("mandatory")
_IbmdlswTConnGroupOperEntry_Object = MibTableRow
ibmdlswTConnGroupOperEntry = _IbmdlswTConnGroupOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1)
)
ibmdlswTConnGroupOperEntry.setIndexNames(
    (0, "IBMIROC-MIB", "ibmdlswTConnGroupOperIndex"),
)
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperEntry.setStatus("mandatory")


class _IbmdlswTConnGroupOperIndex_Type(Integer32):
    """Custom type ibmdlswTConnGroupOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmdlswTConnGroupOperIndex_Type.__name__ = "Integer32"
_IbmdlswTConnGroupOperIndex_Object = MibTableColumn
ibmdlswTConnGroupOperIndex = _IbmdlswTConnGroupOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 1),
    _IbmdlswTConnGroupOperIndex_Type()
)
ibmdlswTConnGroupOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperIndex.setStatus("mandatory")


class _IbmdlswTConnGroupOperRole_Type(Integer32):
    """Custom type ibmdlswTConnGroupOperRole based on Integer32"""
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
        *(("client", 2),
          ("other", 7),
          ("peer", 1),
          ("readonly", 4),
          ("readwrite", 6),
          ("server", 3),
          ("writeonly", 5))
    )


_IbmdlswTConnGroupOperRole_Type.__name__ = "Integer32"
_IbmdlswTConnGroupOperRole_Object = MibTableColumn
ibmdlswTConnGroupOperRole = _IbmdlswTConnGroupOperRole_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 2),
    _IbmdlswTConnGroupOperRole_Type()
)
ibmdlswTConnGroupOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperRole.setStatus("mandatory")
_IbmdlswTConnGroupOperJoinTime_Type = TimeTicks
_IbmdlswTConnGroupOperJoinTime_Object = MibTableColumn
ibmdlswTConnGroupOperJoinTime = _IbmdlswTConnGroupOperJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 3),
    _IbmdlswTConnGroupOperJoinTime_Type()
)
ibmdlswTConnGroupOperJoinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperJoinTime.setStatus("mandatory")


class _IbmdlswTConnGroupOperConfigIndex_Type(Integer32):
    """Custom type ibmdlswTConnGroupOperConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmdlswTConnGroupOperConfigIndex_Type.__name__ = "Integer32"
_IbmdlswTConnGroupOperConfigIndex_Object = MibTableColumn
ibmdlswTConnGroupOperConfigIndex = _IbmdlswTConnGroupOperConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 4),
    _IbmdlswTConnGroupOperConfigIndex_Type()
)
ibmdlswTConnGroupOperConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperConfigIndex.setStatus("mandatory")
_IbmdlswTConnGroupOperInDataPkts_Type = Counter32
_IbmdlswTConnGroupOperInDataPkts_Object = MibTableColumn
ibmdlswTConnGroupOperInDataPkts = _IbmdlswTConnGroupOperInDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 5),
    _IbmdlswTConnGroupOperInDataPkts_Type()
)
ibmdlswTConnGroupOperInDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperInDataPkts.setStatus("mandatory")
_IbmdlswTConnGroupOperOutDataPkts_Type = Counter32
_IbmdlswTConnGroupOperOutDataPkts_Object = MibTableColumn
ibmdlswTConnGroupOperOutDataPkts = _IbmdlswTConnGroupOperOutDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 6),
    _IbmdlswTConnGroupOperOutDataPkts_Type()
)
ibmdlswTConnGroupOperOutDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperOutDataPkts.setStatus("mandatory")
_IbmdlswTConnGroupOperInDataOctets_Type = Counter32
_IbmdlswTConnGroupOperInDataOctets_Object = MibTableColumn
ibmdlswTConnGroupOperInDataOctets = _IbmdlswTConnGroupOperInDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 7),
    _IbmdlswTConnGroupOperInDataOctets_Type()
)
ibmdlswTConnGroupOperInDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperInDataOctets.setStatus("mandatory")
_IbmdlswTConnGroupOperOutDataOctets_Type = Counter32
_IbmdlswTConnGroupOperOutDataOctets_Object = MibTableColumn
ibmdlswTConnGroupOperOutDataOctets = _IbmdlswTConnGroupOperOutDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 8),
    _IbmdlswTConnGroupOperOutDataOctets_Type()
)
ibmdlswTConnGroupOperOutDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperOutDataOctets.setStatus("mandatory")
_IbmdlswTConnGroupOperInCntlPkts_Type = Counter32
_IbmdlswTConnGroupOperInCntlPkts_Object = MibTableColumn
ibmdlswTConnGroupOperInCntlPkts = _IbmdlswTConnGroupOperInCntlPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 9),
    _IbmdlswTConnGroupOperInCntlPkts_Type()
)
ibmdlswTConnGroupOperInCntlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperInCntlPkts.setStatus("mandatory")
_IbmdlswTConnGroupOperOutCntlPkts_Type = Counter32
_IbmdlswTConnGroupOperOutCntlPkts_Object = MibTableColumn
ibmdlswTConnGroupOperOutCntlPkts = _IbmdlswTConnGroupOperOutCntlPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 10),
    _IbmdlswTConnGroupOperOutCntlPkts_Type()
)
ibmdlswTConnGroupOperOutCntlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperOutCntlPkts.setStatus("mandatory")
_IbmdlswTConnGroupOperCURexSents_Type = Counter32
_IbmdlswTConnGroupOperCURexSents_Object = MibTableColumn
ibmdlswTConnGroupOperCURexSents = _IbmdlswTConnGroupOperCURexSents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 11),
    _IbmdlswTConnGroupOperCURexSents_Type()
)
ibmdlswTConnGroupOperCURexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperCURexSents.setStatus("mandatory")
_IbmdlswTConnGroupOperICRexRcvds_Type = Counter32
_IbmdlswTConnGroupOperICRexRcvds_Object = MibTableColumn
ibmdlswTConnGroupOperICRexRcvds = _IbmdlswTConnGroupOperICRexRcvds_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 12),
    _IbmdlswTConnGroupOperICRexRcvds_Type()
)
ibmdlswTConnGroupOperICRexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperICRexRcvds.setStatus("mandatory")
_IbmdlswTConnGroupOperCURexRcvds_Type = Counter32
_IbmdlswTConnGroupOperCURexRcvds_Object = MibTableColumn
ibmdlswTConnGroupOperCURexRcvds = _IbmdlswTConnGroupOperCURexRcvds_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 13),
    _IbmdlswTConnGroupOperCURexRcvds_Type()
)
ibmdlswTConnGroupOperCURexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperCURexRcvds.setStatus("mandatory")
_IbmdlswTConnGroupOperICRexSents_Type = Counter32
_IbmdlswTConnGroupOperICRexSents_Object = MibTableColumn
ibmdlswTConnGroupOperICRexSents = _IbmdlswTConnGroupOperICRexSents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 14),
    _IbmdlswTConnGroupOperICRexSents_Type()
)
ibmdlswTConnGroupOperICRexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperICRexSents.setStatus("mandatory")
_IbmdlswTConnGroupOperNQexSents_Type = Counter32
_IbmdlswTConnGroupOperNQexSents_Object = MibTableColumn
ibmdlswTConnGroupOperNQexSents = _IbmdlswTConnGroupOperNQexSents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 15),
    _IbmdlswTConnGroupOperNQexSents_Type()
)
ibmdlswTConnGroupOperNQexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperNQexSents.setStatus("mandatory")
_IbmdlswTConnGroupOperNRexRcvds_Type = Counter32
_IbmdlswTConnGroupOperNRexRcvds_Object = MibTableColumn
ibmdlswTConnGroupOperNRexRcvds = _IbmdlswTConnGroupOperNRexRcvds_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 16),
    _IbmdlswTConnGroupOperNRexRcvds_Type()
)
ibmdlswTConnGroupOperNRexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperNRexRcvds.setStatus("mandatory")
_IbmdlswTConnGroupOperNQexRcvds_Type = Counter32
_IbmdlswTConnGroupOperNQexRcvds_Object = MibTableColumn
ibmdlswTConnGroupOperNQexRcvds = _IbmdlswTConnGroupOperNQexRcvds_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 17),
    _IbmdlswTConnGroupOperNQexRcvds_Type()
)
ibmdlswTConnGroupOperNQexRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperNQexRcvds.setStatus("mandatory")
_IbmdlswTConnGroupOperNRexSents_Type = Counter32
_IbmdlswTConnGroupOperNRexSents_Object = MibTableColumn
ibmdlswTConnGroupOperNRexSents = _IbmdlswTConnGroupOperNRexSents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 1, 1, 18),
    _IbmdlswTConnGroupOperNRexSents_Type()
)
ibmdlswTConnGroupOperNRexSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswTConnGroupOperNRexSents.setStatus("mandatory")
_IbmdlswQllcLsTable_Object = MibTable
ibmdlswQllcLsTable = _IbmdlswQllcLsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2)
)
if mibBuilder.loadTexts:
    ibmdlswQllcLsTable.setStatus("mandatory")
_IbmdlswQllcLsEntry_Object = MibTableRow
ibmdlswQllcLsEntry = _IbmdlswQllcLsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2, 1)
)
ibmdlswQllcLsEntry.setIndexNames(
    (0, "IBMIROC-MIB", "ibmdlswQllcLsIfIndex"),
    (0, "IBMIROC-MIB", "ibmdlswQllcLsQdomain"),
    (0, "IBMIROC-MIB", "ibmdlswQllcLsQaddress"),
)
if mibBuilder.loadTexts:
    ibmdlswQllcLsEntry.setStatus("mandatory")
_IbmdlswQllcLsIfIndex_Type = Integer32
_IbmdlswQllcLsIfIndex_Object = MibTableColumn
ibmdlswQllcLsIfIndex = _IbmdlswQllcLsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2, 1, 1),
    _IbmdlswQllcLsIfIndex_Type()
)
ibmdlswQllcLsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswQllcLsIfIndex.setStatus("mandatory")


class _IbmdlswQllcLsQdomain_Type(Integer32):
    """Custom type ibmdlswQllcLsQdomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_IbmdlswQllcLsQdomain_Type.__name__ = "Integer32"
_IbmdlswQllcLsQdomain_Object = MibTableColumn
ibmdlswQllcLsQdomain = _IbmdlswQllcLsQdomain_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2, 1, 2),
    _IbmdlswQllcLsQdomain_Type()
)
ibmdlswQllcLsQdomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswQllcLsQdomain.setStatus("mandatory")


class _IbmdlswQllcLsQaddress_Type(OctetString):
    """Custom type ibmdlswQllcLsQaddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IbmdlswQllcLsQaddress_Type.__name__ = "OctetString"
_IbmdlswQllcLsQaddress_Object = MibTableColumn
ibmdlswQllcLsQaddress = _IbmdlswQllcLsQaddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2, 1, 3),
    _IbmdlswQllcLsQaddress_Type()
)
ibmdlswQllcLsQaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdlswQllcLsQaddress.setStatus("mandatory")


class _IbmdlswQllcLsChannel_Type(Integer32):
    """Custom type ibmdlswQllcLsChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IbmdlswQllcLsChannel_Type.__name__ = "Integer32"
_IbmdlswQllcLsChannel_Object = MibTableColumn
ibmdlswQllcLsChannel = _IbmdlswQllcLsChannel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2, 1, 4),
    _IbmdlswQllcLsChannel_Type()
)
ibmdlswQllcLsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswQllcLsChannel.setStatus("mandatory")
_IbmdlswQllcLsLocalMac_Type = MacAddressNCIROC
_IbmdlswQllcLsLocalMac_Object = MibTableColumn
ibmdlswQllcLsLocalMac = _IbmdlswQllcLsLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2, 1, 5),
    _IbmdlswQllcLsLocalMac_Type()
)
ibmdlswQllcLsLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswQllcLsLocalMac.setStatus("mandatory")
_IbmdlswQllcLsLocalSap_Type = OctetString
_IbmdlswQllcLsLocalSap_Object = MibTableColumn
ibmdlswQllcLsLocalSap = _IbmdlswQllcLsLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2, 1, 6),
    _IbmdlswQllcLsLocalSap_Type()
)
ibmdlswQllcLsLocalSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswQllcLsLocalSap.setStatus("mandatory")
_IbmdlswQllcLsRemoteMac_Type = MacAddressNCIROC
_IbmdlswQllcLsRemoteMac_Object = MibTableColumn
ibmdlswQllcLsRemoteMac = _IbmdlswQllcLsRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2, 1, 7),
    _IbmdlswQllcLsRemoteMac_Type()
)
ibmdlswQllcLsRemoteMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswQllcLsRemoteMac.setStatus("mandatory")
_IbmdlswQllcLsRemoteSap_Type = OctetString
_IbmdlswQllcLsRemoteSap_Object = MibTableColumn
ibmdlswQllcLsRemoteSap = _IbmdlswQllcLsRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2, 1, 8),
    _IbmdlswQllcLsRemoteSap_Type()
)
ibmdlswQllcLsRemoteSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswQllcLsRemoteSap.setStatus("mandatory")


class _IbmdlswQllcLsPuType_Type(Integer32):
    """Custom type ibmdlswQllcLsPuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 6),
          ("type1", 1),
          ("type2", 2),
          ("type4", 4),
          ("type5", 5))
    )


_IbmdlswQllcLsPuType_Type.__name__ = "Integer32"
_IbmdlswQllcLsPuType_Object = MibTableColumn
ibmdlswQllcLsPuType = _IbmdlswQllcLsPuType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2, 1, 9),
    _IbmdlswQllcLsPuType_Type()
)
ibmdlswQllcLsPuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswQllcLsPuType.setStatus("mandatory")


class _IbmdlswQllcLsBlkNum_Type(DisplayString):
    """Custom type ibmdlswQllcLsBlkNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_IbmdlswQllcLsBlkNum_Type.__name__ = "DisplayString"
_IbmdlswQllcLsBlkNum_Object = MibTableColumn
ibmdlswQllcLsBlkNum = _IbmdlswQllcLsBlkNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2, 1, 10),
    _IbmdlswQllcLsBlkNum_Type()
)
ibmdlswQllcLsBlkNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswQllcLsBlkNum.setStatus("mandatory")


class _IbmdlswQllcLsIdNum_Type(DisplayString):
    """Custom type ibmdlswQllcLsIdNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_IbmdlswQllcLsIdNum_Type.__name__ = "DisplayString"
_IbmdlswQllcLsIdNum_Object = MibTableColumn
ibmdlswQllcLsIdNum = _IbmdlswQllcLsIdNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 3, 2, 1, 11),
    _IbmdlswQllcLsIdNum_Type()
)
ibmdlswQllcLsIdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlswQllcLsIdNum.setStatus("mandatory")
_IbmIROCroutingfr_ObjectIdentity = ObjectIdentity
ibmIROCroutingfr = _IbmIROCroutingfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4)
)
_FrCLLMStatsTable_Object = MibTable
frCLLMStatsTable = _FrCLLMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 1)
)
if mibBuilder.loadTexts:
    frCLLMStatsTable.setStatus("mandatory")
_FrCLLMStatsEntry_Object = MibTableRow
frCLLMStatsEntry = _FrCLLMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 1, 1)
)
frCLLMStatsEntry.setIndexNames(
    (0, "IBMIROC-MIB", "frCLLMStatsIfIndex"),
    (0, "IBMIROC-MIB", "frCLLMStatsDlci"),
)
if mibBuilder.loadTexts:
    frCLLMStatsEntry.setStatus("mandatory")
_FrCLLMStatsIfIndex_Type = Integer32
_FrCLLMStatsIfIndex_Object = MibTableColumn
frCLLMStatsIfIndex = _FrCLLMStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 1, 1, 1),
    _FrCLLMStatsIfIndex_Type()
)
frCLLMStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCLLMStatsIfIndex.setStatus("mandatory")
_FrCLLMStatsDlci_Type = Integer32
_FrCLLMStatsDlci_Object = MibTableColumn
frCLLMStatsDlci = _FrCLLMStatsDlci_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 1, 1, 2),
    _FrCLLMStatsDlci_Type()
)
frCLLMStatsDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCLLMStatsDlci.setStatus("mandatory")
_FrCLLMStatsRcvds_Type = Counter32
_FrCLLMStatsRcvds_Object = MibTableColumn
frCLLMStatsRcvds = _FrCLLMStatsRcvds_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 1, 1, 3),
    _FrCLLMStatsRcvds_Type()
)
frCLLMStatsRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCLLMStatsRcvds.setStatus("mandatory")
_FrCLLMCauseTable_Object = MibTable
frCLLMCauseTable = _FrCLLMCauseTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 2)
)
if mibBuilder.loadTexts:
    frCLLMCauseTable.setStatus("mandatory")
_FrCLLMCauseEntry_Object = MibTableRow
frCLLMCauseEntry = _FrCLLMCauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 2, 1)
)
frCLLMCauseEntry.setIndexNames(
    (0, "IBMIROC-MIB", "frCLLMCauseIfIndex"),
)
if mibBuilder.loadTexts:
    frCLLMCauseEntry.setStatus("mandatory")
_FrCLLMCauseIfIndex_Type = Integer32
_FrCLLMCauseIfIndex_Object = MibTableColumn
frCLLMCauseIfIndex = _FrCLLMCauseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 2, 1, 1),
    _FrCLLMCauseIfIndex_Type()
)
frCLLMCauseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCLLMCauseIfIndex.setStatus("mandatory")
_FrCLLMCauseCode_Type = Integer32
_FrCLLMCauseCode_Object = MibTableColumn
frCLLMCauseCode = _FrCLLMCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 2, 1, 2),
    _FrCLLMCauseCode_Type()
)
frCLLMCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCLLMCauseCode.setStatus("mandatory")
_FrSimpleObjs_ObjectIdentity = ObjectIdentity
frSimpleObjs = _FrSimpleObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 3)
)


class _FrCLLMDlciList_Type(OctetString):
    """Custom type frCLLMDlciList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_FrCLLMDlciList_Type.__name__ = "OctetString"
_FrCLLMDlciList_Object = MibScalar
frCLLMDlciList = _FrCLLMDlciList_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 3, 1),
    _FrCLLMDlciList_Type()
)
frCLLMDlciList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCLLMDlciList.setStatus("mandatory")


class _FrTrapStateFECN_Type(Integer32):
    """Custom type frTrapStateFECN based on Integer32"""
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


_FrTrapStateFECN_Type.__name__ = "Integer32"
_FrTrapStateFECN_Object = MibScalar
frTrapStateFECN = _FrTrapStateFECN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 3, 2),
    _FrTrapStateFECN_Type()
)
frTrapStateFECN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frTrapStateFECN.setStatus("mandatory")


class _FrTrapStateBECN_Type(Integer32):
    """Custom type frTrapStateBECN based on Integer32"""
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


_FrTrapStateBECN_Type.__name__ = "Integer32"
_FrTrapStateBECN_Object = MibScalar
frTrapStateBECN = _FrTrapStateBECN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 3, 3),
    _FrTrapStateBECN_Type()
)
frTrapStateBECN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frTrapStateBECN.setStatus("mandatory")


class _FrTrapStateCLLM_Type(Integer32):
    """Custom type frTrapStateCLLM based on Integer32"""
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


_FrTrapStateCLLM_Type.__name__ = "Integer32"
_FrTrapStateCLLM_Object = MibScalar
frTrapStateCLLM = _FrTrapStateCLLM_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 3, 4),
    _FrTrapStateCLLM_Type()
)
frTrapStateCLLM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frTrapStateCLLM.setStatus("mandatory")
_IbmIROCfrBRS_ObjectIdentity = ObjectIdentity
ibmIROCfrBRS = _IbmIROCfrBRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4)
)
_IbmIROCfrcircuit_ObjectIdentity = ObjectIdentity
ibmIROCfrcircuit = _IbmIROCfrcircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 5)
)
_IbmIROCroutingRlan_ObjectIdentity = ObjectIdentity
ibmIROCroutingRlan = _IbmIROCroutingRlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5)
)
_IbmIROCroutingDialOut_ObjectIdentity = ObjectIdentity
ibmIROCroutingDialOut = _IbmIROCroutingDialOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6)
)
_IbmIROCroutingl2tp_ObjectIdentity = ObjectIdentity
ibmIROCroutingl2tp = _IbmIROCroutingl2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7)
)
_IbmCacheServer_ObjectIdentity = ObjectIdentity
ibmCacheServer = _IbmCacheServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8)
)
_IbmIROCroutingIpSec_ObjectIdentity = ObjectIdentity
ibmIROCroutingIpSec = _IbmIROCroutingIpSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 9)
)
_IbmIROCswhw_ObjectIdentity = ObjectIdentity
ibmIROCswhw = _IbmIROCswhw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 10)
)
_IbmWanRestoralRerouteMIB_ObjectIdentity = ObjectIdentity
ibmWanRestoralRerouteMIB = _IbmWanRestoralRerouteMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11)
)
_IbmBANMIB_ObjectIdentity = ObjectIdentity
ibmBANMIB = _IbmBANMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 12)
)
_IbmIROCrmon_ObjectIdentity = ObjectIdentity
ibmIROCrmon = _IbmIROCrmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 13)
)
_IbmIROCescon_ObjectIdentity = ObjectIdentity
ibmIROCescon = _IbmIROCescon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 14)
)
_IbmIROCVPNpolicy_ObjectIdentity = ObjectIdentity
ibmIROCVPNpolicy = _IbmIROCVPNpolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15)
)
_IbmIROCroutingvoice_ObjectIdentity = ObjectIdentity
ibmIROCroutingvoice = _IbmIROCroutingvoice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 16)
)
_IbmIROCroutinginterface_ObjectIdentity = ObjectIdentity
ibmIROCroutinginterface = _IbmIROCroutinginterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 17)
)
_IbmIROCroutingtn3270e_ObjectIdentity = ObjectIdentity
ibmIROCroutingtn3270e = _IbmIROCroutingtn3270e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 18)
)
_IbmIROCroutingtcpip_ObjectIdentity = ObjectIdentity
ibmIROCroutingtcpip = _IbmIROCroutingtcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20)
)
_TcpiprouteTabSize_Type = Integer32
_TcpiprouteTabSize_Object = MibScalar
tcpiprouteTabSize = _TcpiprouteTabSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 1),
    _TcpiprouteTabSize_Type()
)
tcpiprouteTabSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteTabSize.setStatus("mandatory")
_TcpiprouteTabUsed_Type = Gauge32
_TcpiprouteTabUsed_Object = MibScalar
tcpiprouteTabUsed = _TcpiprouteTabUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 2),
    _TcpiprouteTabUsed_Type()
)
tcpiprouteTabUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteTabUsed.setStatus("mandatory")
_TcpiprouteCacheSize_Type = Integer32
_TcpiprouteCacheSize_Object = MibScalar
tcpiprouteCacheSize = _TcpiprouteCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 3),
    _TcpiprouteCacheSize_Type()
)
tcpiprouteCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteCacheSize.setStatus("mandatory")
_TcpiprouteCacheUsed_Type = Gauge32
_TcpiprouteCacheUsed_Object = MibScalar
tcpiprouteCacheUsed = _TcpiprouteCacheUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 4),
    _TcpiprouteCacheUsed_Type()
)
tcpiprouteCacheUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteCacheUsed.setStatus("mandatory")
_TcpiprouteOverFlow_Type = Counter32
_TcpiprouteOverFlow_Object = MibScalar
tcpiprouteOverFlow = _TcpiprouteOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 5),
    _TcpiprouteOverFlow_Type()
)
tcpiprouteOverFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteOverFlow.setStatus("mandatory")
_TcpiprouteNoReach_Type = Counter32
_TcpiprouteNoReach_Object = MibScalar
tcpiprouteNoReach = _TcpiprouteNoReach_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 6),
    _TcpiprouteNoReach_Type()
)
tcpiprouteNoReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteNoReach.setStatus("mandatory")
_TcpiprouteBadSubnet_Type = Counter32
_TcpiprouteBadSubnet_Object = MibScalar
tcpiprouteBadSubnet = _TcpiprouteBadSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 7),
    _TcpiprouteBadSubnet_Type()
)
tcpiprouteBadSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteBadSubnet.setStatus("mandatory")
_TcpiprouteBadNet_Type = Counter32
_TcpiprouteBadNet_Object = MibScalar
tcpiprouteBadNet = _TcpiprouteBadNet_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 8),
    _TcpiprouteBadNet_Type()
)
tcpiprouteBadNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteBadNet.setStatus("mandatory")
_TcpiprouteUnhBcast_Type = Counter32
_TcpiprouteUnhBcast_Object = MibScalar
tcpiprouteUnhBcast = _TcpiprouteUnhBcast_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 9),
    _TcpiprouteUnhBcast_Type()
)
tcpiprouteUnhBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteUnhBcast.setStatus("mandatory")
_TcpiprouteUnhMcast_Type = Counter32
_TcpiprouteUnhMcast_Object = MibScalar
tcpiprouteUnhMcast = _TcpiprouteUnhMcast_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 10),
    _TcpiprouteUnhMcast_Type()
)
tcpiprouteUnhMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteUnhMcast.setStatus("mandatory")
_TcpiprouteUnhDirBcast_Type = Counter32
_TcpiprouteUnhDirBcast_Object = MibScalar
tcpiprouteUnhDirBcast = _TcpiprouteUnhDirBcast_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 11),
    _TcpiprouteUnhDirBcast_Type()
)
tcpiprouteUnhDirBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteUnhDirBcast.setStatus("mandatory")
_TcpiprouteUnhLLbcast_Type = Counter32
_TcpiprouteUnhLLbcast_Object = MibScalar
tcpiprouteUnhLLbcast = _TcpiprouteUnhLLbcast_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 12),
    _TcpiprouteUnhLLbcast_Type()
)
tcpiprouteUnhLLbcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteUnhLLbcast.setStatus("mandatory")
_TcpiprouteDiscFilt_Type = Counter32
_TcpiprouteDiscFilt_Object = MibScalar
tcpiprouteDiscFilt = _TcpiprouteDiscFilt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 13),
    _TcpiprouteDiscFilt_Type()
)
tcpiprouteDiscFilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteDiscFilt.setStatus("mandatory")
_TcpiprouteMultRcvd_Type = Counter32
_TcpiprouteMultRcvd_Object = MibScalar
tcpiprouteMultRcvd = _TcpiprouteMultRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 14),
    _TcpiprouteMultRcvd_Type()
)
tcpiprouteMultRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpiprouteMultRcvd.setStatus("mandatory")
_TcpCurrConnections_Type = Gauge32
_TcpCurrConnections_Object = MibScalar
tcpCurrConnections = _TcpCurrConnections_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 15),
    _TcpCurrConnections_Type()
)
tcpCurrConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurrConnections.setStatus("mandatory")
_TcpMaxConnections_Type = Integer32
_TcpMaxConnections_Object = MibScalar
tcpMaxConnections = _TcpMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 16),
    _TcpMaxConnections_Type()
)
tcpMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpMaxConnections.setStatus("mandatory")
_ServerCurrConnections_Type = Gauge32
_ServerCurrConnections_Object = MibScalar
serverCurrConnections = _ServerCurrConnections_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 17),
    _ServerCurrConnections_Type()
)
serverCurrConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrConnections.setStatus("mandatory")
_ServerMaxConnections_Type = Integer32
_ServerMaxConnections_Object = MibScalar
serverMaxConnections = _ServerMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 20, 18),
    _ServerMaxConnections_Type()
)
serverMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverMaxConnections.setStatus("mandatory")
_IbmIROCswitching_ObjectIdentity = ObjectIdentity
ibmIROCswitching = _IbmIROCswitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 5)
)
_IbmIROCtraps_ObjectIdentity = ObjectIdentity
ibmIROCtraps = _IbmIROCtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 6)
)
_IbmIROCtrapsfr_ObjectIdentity = ObjectIdentity
ibmIROCtrapsfr = _IbmIROCtrapsfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 6, 1)
)
_IbmIROCtrapssys_ObjectIdentity = ObjectIdentity
ibmIROCtrapssys = _IbmIROCtrapssys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 6, 2)
)
_IbmIROCtrapsels_ObjectIdentity = ObjectIdentity
ibmIROCtrapsels = _IbmIROCtrapsels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 6, 3)
)
_IbmIROCconfig_ObjectIdentity = ObjectIdentity
ibmIROCconfig = _IbmIROCconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7)
)
_IbmIROCconfigAuth_ObjectIdentity = ObjectIdentity
ibmIROCconfigAuth = _IbmIROCconfigAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2)
)


class _IbmIROCconfigWrite_Type(Integer32):
    """Custom type ibmIROCconfigWrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 1),
          ("write", 2))
    )


_IbmIROCconfigWrite_Type.__name__ = "Integer32"
_IbmIROCconfigWrite_Object = MibScalar
ibmIROCconfigWrite = _IbmIROCconfigWrite_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 4),
    _IbmIROCconfigWrite_Type()
)
ibmIROCconfigWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmIROCconfigWrite.setStatus("mandatory")

# Managed Objects groups


# Notification objects

frrcvdFECN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 6, 1, 0, 1)
)
frrcvdFECN.setObjects(
      *(("RFC1315-MIB", "frCircuitIfIndex"),
        ("RFC1315-MIB", "frCircuitDlci"))
)
if mibBuilder.loadTexts:
    frrcvdFECN.setStatus(
        ""
    )

frrcvdBECN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 6, 1, 0, 2)
)
frrcvdBECN.setObjects(
      *(("RFC1315-MIB", "frCircuitIfIndex"),
        ("RFC1315-MIB", "frCircuitDlci"))
)
if mibBuilder.loadTexts:
    frrcvdBECN.setStatus(
        ""
    )

frrcvdCLLM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 6, 1, 0, 3)
)
frrcvdCLLM.setObjects(
      *(("IBMIROC-MIB", "frCLLMCauseIfIndex"),
        ("IBMIROC-MIB", "frCLLMCauseCode"),
        ("IBMIROC-MIB", "frCLLMDlciList"))
)
if mibBuilder.loadTexts:
    frrcvdCLLM.setStatus(
        ""
    )

mosMemLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 6, 2, 0, 1)
)
mosMemLow.setObjects(
      *(("PROTEON-MIB", "proResMemHeapTotal"),
        ("PROTEON-MIB", "proResMemHeapNeverAlloc"))
)
if mibBuilder.loadTexts:
    mosMemLow.setStatus(
        ""
    )

elsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 6, 3, 0, 2)
)
elsTrap.setObjects(
    ("PROTEON-MIB", "proElsSubSysEventMsg")
)
if mibBuilder.loadTexts:
    elsTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMIROC-MIB",
    **{"MacAddressNCIROC": MacAddressNCIROC,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "ibmIROC": ibmIROC,
       "ibmIROCadmin": ibmIROCadmin,
       "ibmIROCadminproducts": ibmIROCadminproducts,
       "ibmIROCadminOID": ibmIROCadminOID,
       "ibmIROCadminDebug": ibmIROCadminDebug,
       "ibmIROCAgentDebug": ibmIROCAgentDebug,
       "agentMemUse": agentMemUse,
       "ibmIROCadminSnmp": ibmIROCadminSnmp,
       "ibmIROCSnmpAuthFail": ibmIROCSnmpAuthFail,
       "authTrapSourceIPAddr": authTrapSourceIPAddr,
       "ibmIROCsystem": ibmIROCsystem,
       "ibmIROCsystemInfo": ibmIROCsystemInfo,
       "ibmIROCcfgInfo": ibmIROCcfgInfo,
       "ibmIROCdumpInfo": ibmIROCdumpInfo,
       "ibmSysDumpTable": ibmSysDumpTable,
       "ibmSysDumpEntry": ibmSysDumpEntry,
       "ibmSysDumpIndex": ibmSysDumpIndex,
       "ibmSysDumpFileName": ibmSysDumpFileName,
       "ibmSysDumpFileDate": ibmSysDumpFileDate,
       "ibmSysDumpBuild": ibmSysDumpBuild,
       "ibmSysDumpBuilder": ibmSysDumpBuilder,
       "ibmSysDumpBuildName": ibmSysDumpBuildName,
       "ibmSysDumpRetainName": ibmSysDumpRetainName,
       "ibmSysDumpProductNumber": ibmSysDumpProductNumber,
       "ibmSysDumpBuildDate": ibmSysDumpBuildDate,
       "ibmSysDumpFatalMsg1": ibmSysDumpFatalMsg1,
       "ibmSysDumpFatalMsg2": ibmSysDumpFatalMsg2,
       "ibmSysDumpFatalMsg3": ibmSysDumpFatalMsg3,
       "ibmSysDumpFatalMsg4": ibmSysDumpFatalMsg4,
       "ibmSysDumpFatalMsg5": ibmSysDumpFatalMsg5,
       "ibmSysDumpRemoteIPAddr": ibmSysDumpRemoteIPAddr,
       "ibmSysDumpRemotePath": ibmSysDumpRemotePath,
       "ibmIROChardware": ibmIROChardware,
       "ibmIROChardwareInfo": ibmIROChardwareInfo,
       "platformType": platformType,
       "platformDRAMSize": platformDRAMSize,
       "platformFLASHSize": platformFLASHSize,
       "platformNVRAMSize": platformNVRAMSize,
       "platformFeatureSlot": platformFeatureSlot,
       "ibmIROCrouting": ibmIROCrouting,
       "ibmIROCroutingppp": ibmIROCroutingppp,
       "pppProtocolTable": pppProtocolTable,
       "pppProtocolEntry": pppProtocolEntry,
       "pppProtocolIfIndex": pppProtocolIfIndex,
       "pppProtocolId": pppProtocolId,
       "pppProtocolRegistered": pppProtocolRegistered,
       "pppProtocolState": pppProtocolState,
       "pppProtocolPreviousState": pppProtocolPreviousState,
       "pppProtocolLastTimeChange": pppProtocolLastTimeChange,
       "pppProtocolCtlInRejects": pppProtocolCtlInRejects,
       "pppProtocolCtlInOctets": pppProtocolCtlInOctets,
       "pppProtocolCtlInPkts": pppProtocolCtlInPkts,
       "pppProtocolCtlOutOctets": pppProtocolCtlOutOctets,
       "pppProtocolCtlOutPkts": pppProtocolCtlOutPkts,
       "pppProtocolDataInRejects": pppProtocolDataInRejects,
       "pppProtocolDataInOctets": pppProtocolDataInOctets,
       "pppProtocolDataInPkts": pppProtocolDataInPkts,
       "pppProtocolDataOutOctets": pppProtocolDataOutOctets,
       "pppProtocolDataOutPkts": pppProtocolDataOutPkts,
       "pppLinkErrTable": pppLinkErrTable,
       "pppLinkErrEntry": pppLinkErrEntry,
       "pppLinkErrIfIndex": pppLinkErrIfIndex,
       "pppLinkErrBadAddrs": pppLinkErrBadAddrs,
       "pppLinkErrLastBadAddr": pppLinkErrLastBadAddr,
       "pppLinkErrBadCtrls": pppLinkErrBadCtrls,
       "pppLinkErrLastBadCtrl": pppLinkErrLastBadCtrl,
       "pppLinkErrUnkProtos": pppLinkErrUnkProtos,
       "pppLinkErrLastUnkProto": pppLinkErrLastUnkProto,
       "pppLinkErrInvProtos": pppLinkErrInvProtos,
       "pppLinkErrLastInvProto": pppLinkErrLastInvProto,
       "pppLinkErrConfigTOs": pppLinkErrConfigTOs,
       "pppLinkErrTermTOs": pppLinkErrTermTOs,
       "pppLCProtoTable": pppLCProtoTable,
       "pppLCProtoEntry": pppLCProtoEntry,
       "pppLCProtoIfIndex": pppLCProtoIfIndex,
       "pppLCProtoState": pppLCProtoState,
       "pppLCProtoPreviousState": pppLCProtoPreviousState,
       "pppLCProtoLastTimeChange": pppLCProtoLastTimeChange,
       "pppLCProtoOutPackets": pppLCProtoOutPackets,
       "pppLCProtoOutOctets": pppLCProtoOutOctets,
       "pppLCProtoOutCRs": pppLCProtoOutCRs,
       "pppLCProtoOutCAs": pppLCProtoOutCAs,
       "pppLCProtoOutCNs": pppLCProtoOutCNs,
       "pppLCProtoOutCRejs": pppLCProtoOutCRejs,
       "pppLCProtoOutTRs": pppLCProtoOutTRs,
       "pppLCProtoOutTAs": pppLCProtoOutTAs,
       "pppLCProtoOutCodeRejs": pppLCProtoOutCodeRejs,
       "pppLCProtoOutEchoReqs": pppLCProtoOutEchoReqs,
       "pppLCProtoOutEchoReps": pppLCProtoOutEchoReps,
       "pppLCProtoOutDiscReqs": pppLCProtoOutDiscReqs,
       "pppLCProtoOutResetReqs": pppLCProtoOutResetReqs,
       "pppLCProtoOutResetAcks": pppLCProtoOutResetAcks,
       "pppLCProtoOutIdents": pppLCProtoOutIdents,
       "pppLCProtoOutTimeRemains": pppLCProtoOutTimeRemains,
       "pppLCProtoInRejects": pppLCProtoInRejects,
       "pppLCProtoInPackets": pppLCProtoInPackets,
       "pppLCProtoInOctets": pppLCProtoInOctets,
       "pppLCProtoInCRs": pppLCProtoInCRs,
       "pppLCProtoInCAs": pppLCProtoInCAs,
       "pppLCProtoInCNs": pppLCProtoInCNs,
       "pppLCProtoInCRejs": pppLCProtoInCRejs,
       "pppLCProtoInTRs": pppLCProtoInTRs,
       "pppLCProtoInTAs": pppLCProtoInTAs,
       "pppLCProtoInCodeRejs": pppLCProtoInCodeRejs,
       "pppLCProtoInEchoReqs": pppLCProtoInEchoReqs,
       "pppLCProtoInEchoReps": pppLCProtoInEchoReps,
       "pppLCProtoInDiscReqs": pppLCProtoInDiscReqs,
       "pppLCProtoInResetReqs": pppLCProtoInResetReqs,
       "pppLCProtoInResetAcks": pppLCProtoInResetAcks,
       "pppLCProtoInIdents": pppLCProtoInIdents,
       "pppLCProtoInTimeRemains": pppLCProtoInTimeRemains,
       "pppPAPTable": pppPAPTable,
       "pppPAPEntry": pppPAPEntry,
       "pppPAPIfIndex": pppPAPIfIndex,
       "pppPAPInPackets": pppPAPInPackets,
       "pppPAPInOctets": pppPAPInOctets,
       "pppPAPInRequests": pppPAPInRequests,
       "pppPAPInAcks": pppPAPInAcks,
       "pppPAPInNacks": pppPAPInNacks,
       "pppPAPOutPackets": pppPAPOutPackets,
       "pppPAPOutOctets": pppPAPOutOctets,
       "pppPAPOutRequests": pppPAPOutRequests,
       "pppPAPOutAcks": pppPAPOutAcks,
       "pppPAPOutNacks": pppPAPOutNacks,
       "pppCHAPTable": pppCHAPTable,
       "pppCHAPEntry": pppCHAPEntry,
       "pppCHAPIfIndex": pppCHAPIfIndex,
       "pppCHAPInPackets": pppCHAPInPackets,
       "pppCHAPInOctets": pppCHAPInOctets,
       "pppCHAPInChallenges": pppCHAPInChallenges,
       "pppCHAPInResponses": pppCHAPInResponses,
       "pppCHAPInSuccesses": pppCHAPInSuccesses,
       "pppCHAPInFailures": pppCHAPInFailures,
       "pppCHAPOutPackets": pppCHAPOutPackets,
       "pppCHAPOutOctets": pppCHAPOutOctets,
       "pppCHAPOutChallenges": pppCHAPOutChallenges,
       "pppCHAPOutResponses": pppCHAPOutResponses,
       "pppCHAPOutSuccesses": pppCHAPOutSuccesses,
       "pppCHAPOutFailures": pppCHAPOutFailures,
       "pppSPAPTable": pppSPAPTable,
       "pppSPAPEntry": pppSPAPEntry,
       "pppSPAPIfIndex": pppSPAPIfIndex,
       "pppSPAPInPackets": pppSPAPInPackets,
       "pppSPAPInOctets": pppSPAPInOctets,
       "pppSPAPInRequests": pppSPAPInRequests,
       "pppSPAPInAcks": pppSPAPInAcks,
       "pppSPAPInNacks": pppSPAPInNacks,
       "pppSPAPInDialbacks": pppSPAPInDialbacks,
       "pppSPAPInPleaseAuthenticates": pppSPAPInPleaseAuthenticates,
       "pppSPAPInChangePasswords": pppSPAPInChangePasswords,
       "pppSPAPInAlerts": pppSPAPInAlerts,
       "pppSPAPInAlertAcks": pppSPAPInAlertAcks,
       "pppSPAPOutPackets": pppSPAPOutPackets,
       "pppSPAPOutOctets": pppSPAPOutOctets,
       "pppSPAPOutRequests": pppSPAPOutRequests,
       "pppSPAPOutAcks": pppSPAPOutAcks,
       "pppSPAPOutNacks": pppSPAPOutNacks,
       "pppSPAPOutDialbacks": pppSPAPOutDialbacks,
       "pppSPAPOutPleaseAuthenticates": pppSPAPOutPleaseAuthenticates,
       "pppSPAPOutChangePasswords": pppSPAPOutChangePasswords,
       "pppSPAPOutAlerts": pppSPAPOutAlerts,
       "pppSPAPOutAlertAcks": pppSPAPOutAlertAcks,
       "pppBAPTable": pppBAPTable,
       "pppBAPEntry": pppBAPEntry,
       "pppBAPIfIndex": pppBAPIfIndex,
       "pppBAPInCallReqs": pppBAPInCallReqs,
       "pppBAPInCallAcks": pppBAPInCallAcks,
       "pppBAPInCallNaks": pppBAPInCallNaks,
       "pppBAPInCallRejs": pppBAPInCallRejs,
       "pppBAPInCallBackReqs": pppBAPInCallBackReqs,
       "pppBAPInCallBackAcks": pppBAPInCallBackAcks,
       "pppBAPInCallBackNaks": pppBAPInCallBackNaks,
       "pppBAPInCallBackRejs": pppBAPInCallBackRejs,
       "pppBAPInDropReqs": pppBAPInDropReqs,
       "pppBAPInDropAcks": pppBAPInDropAcks,
       "pppBAPInDropNaks": pppBAPInDropNaks,
       "pppBAPInDropRejs": pppBAPInDropRejs,
       "pppBAPInStatSuccs": pppBAPInStatSuccs,
       "pppBAPInStatFails": pppBAPInStatFails,
       "pppBAPOutCallReqs": pppBAPOutCallReqs,
       "pppBAPOutCallAcks": pppBAPOutCallAcks,
       "pppBAPOutCallNaks": pppBAPOutCallNaks,
       "pppBAPOutCallRejs": pppBAPOutCallRejs,
       "pppBAPOutCallBackReqs": pppBAPOutCallBackReqs,
       "pppBAPOutCallBackAcks": pppBAPOutCallBackAcks,
       "pppBAPOutCallBackNaks": pppBAPOutCallBackNaks,
       "pppBAPOutCallBackRejs": pppBAPOutCallBackRejs,
       "pppBAPOutDropReqs": pppBAPOutDropReqs,
       "pppBAPOutDropAcks": pppBAPOutDropAcks,
       "pppBAPOutDropNaks": pppBAPOutDropNaks,
       "pppBAPOutDropRejs": pppBAPOutDropRejs,
       "pppBAPOutStatSuccs": pppBAPOutStatSuccs,
       "pppBAPOutStatFails": pppBAPOutStatFails,
       "pppCPTable": pppCPTable,
       "pppCPEntry": pppCPEntry,
       "pppCPIfIndex": pppCPIfIndex,
       "pppCPInCompressedOctets": pppCPInCompressedOctets,
       "pppCPInInCompressablePkts": pppCPInInCompressablePkts,
       "pppCPInDestroyeds": pppCPInDestroyeds,
       "pppCPInCopies": pppCPInCopies,
       "pppCPOutCompressedOctets": pppCPOutCompressedOctets,
       "pppCPOutInCompressablePkts": pppCPOutInCompressablePkts,
       "pppCPOutDestroyeds": pppCPOutDestroyeds,
       "pppCPOutCopies": pppCPOutCopies,
       "pppCCPInResetReqs": pppCCPInResetReqs,
       "pppCCPInResetAcks": pppCCPInResetAcks,
       "pppCCPInDictResets": pppCCPInDictResets,
       "pppCCPOutResetReqs": pppCCPOutResetReqs,
       "pppCCPOutResetAcks": pppCCPOutResetAcks,
       "pppCCPOutDictResets": pppCCPOutDictResets,
       "pppCCPPacketDiscards": pppCCPPacketDiscards,
       "pppCCPOctetDiscards": pppCCPOctetDiscards,
       "pppEPTable": pppEPTable,
       "pppEPEntry": pppEPEntry,
       "pppEPIfIndex": pppEPIfIndex,
       "pppEPInEncryptedOctets": pppEPInEncryptedOctets,
       "pppEPInDestroyeds": pppEPInDestroyeds,
       "pppEPInCopies": pppEPInCopies,
       "pppEPOutEncryptedOctets": pppEPOutEncryptedOctets,
       "pppEPOutDestroyeds": pppEPOutDestroyeds,
       "pppEPOutCopies": pppEPOutCopies,
       "pppECPInResetReqs": pppECPInResetReqs,
       "pppECPInResetAcks": pppECPInResetAcks,
       "pppECPInDictResets": pppECPInDictResets,
       "pppECPOutResetReqs": pppECPOutResetReqs,
       "pppECPOutResetAcks": pppECPOutResetAcks,
       "pppECPOutDictResets": pppECPOutDictResets,
       "pppECPPacketDiscards": pppECPPacketDiscards,
       "pppECPOctetDiscards": pppECPOctetDiscards,
       "pppMSCHAPTable": pppMSCHAPTable,
       "pppMSCHAPEntry": pppMSCHAPEntry,
       "pppMSCHAPIfIndex": pppMSCHAPIfIndex,
       "pppMSCHAPInPackets": pppMSCHAPInPackets,
       "pppMSCHAPInOctets": pppMSCHAPInOctets,
       "pppMSCHAPInChallenges": pppMSCHAPInChallenges,
       "pppMSCHAPInResponses": pppMSCHAPInResponses,
       "pppMSCHAPInSuccesses": pppMSCHAPInSuccesses,
       "pppMSCHAPInFailures": pppMSCHAPInFailures,
       "pppMSCHAPInChangePasswords": pppMSCHAPInChangePasswords,
       "pppMSCHAPInRestrictedHoursFailures": pppMSCHAPInRestrictedHoursFailures,
       "pppMSCHAPInAccountDisabledFailures": pppMSCHAPInAccountDisabledFailures,
       "pppMSCHAPInPasswordExpiredFailures": pppMSCHAPInPasswordExpiredFailures,
       "pppMSCHAPInNoPermissionFailures": pppMSCHAPInNoPermissionFailures,
       "pppMSCHAPInAuthenticationFailures": pppMSCHAPInAuthenticationFailures,
       "pppMSCHAPInChangePasswordFailures": pppMSCHAPInChangePasswordFailures,
       "pppMSCHAPOutPackets": pppMSCHAPOutPackets,
       "pppMSCHAPOutOctets": pppMSCHAPOutOctets,
       "pppMSCHAPOutChallenges": pppMSCHAPOutChallenges,
       "pppMSCHAPOutResponses": pppMSCHAPOutResponses,
       "pppMSCHAPOutSuccesses": pppMSCHAPOutSuccesses,
       "pppMSCHAPOutFailures": pppMSCHAPOutFailures,
       "pppMSCHAPOutChangePasswords": pppMSCHAPOutChangePasswords,
       "pppMSCHAPOutRestrictedHoursFailures": pppMSCHAPOutRestrictedHoursFailures,
       "pppMSCHAPOutAccountDisabledFailures": pppMSCHAPOutAccountDisabledFailures,
       "pppMSCHAPOutPasswordExpiredFailures": pppMSCHAPOutPasswordExpiredFailures,
       "pppMSCHAPOutNoPermissionFailures": pppMSCHAPOutNoPermissionFailures,
       "pppMSCHAPOutAuthenticationFailures": pppMSCHAPOutAuthenticationFailures,
       "pppMSCHAPOutChangePasswordFailures": pppMSCHAPOutChangePasswordFailures,
       "pppCBCPTable": pppCBCPTable,
       "pppCBCPEntry": pppCBCPEntry,
       "pppCBCPIfIndex": pppCBCPIfIndex,
       "pppCBCPInPackets": pppCBCPInPackets,
       "pppCBCPInOctets": pppCBCPInOctets,
       "pppCBCPOutPackets": pppCBCPOutPackets,
       "pppCBCPOutOctets": pppCBCPOutOctets,
       "pppCBCPAttempts": pppCBCPAttempts,
       "pppCBCPSuccess": pppCBCPSuccess,
       "pppEAPTable": pppEAPTable,
       "pppEAPEntry": pppEAPEntry,
       "pppEAPIfIndex": pppEAPIfIndex,
       "pppEAPInPackets": pppEAPInPackets,
       "pppEAPInOctets": pppEAPInOctets,
       "pppEAPInRequests": pppEAPInRequests,
       "pppEAPInAcks": pppEAPInAcks,
       "pppEAPInNaks": pppEAPInNaks,
       "pppEAPOutPackets": pppEAPOutPackets,
       "pppEAPOutOctets": pppEAPOutOctets,
       "pppEAPOutRequests": pppEAPOutRequests,
       "pppEAPOutAcks": pppEAPOutAcks,
       "pppEAPOutNaks": pppEAPOutNaks,
       "pppMPPETable": pppMPPETable,
       "pppMPPEEntry": pppMPPEEntry,
       "pppMPPEIfIndex": pppMPPEIfIndex,
       "pppMPPEInPackets": pppMPPEInPackets,
       "pppMPPEInOctets": pppMPPEInOctets,
       "pppMPPEInDestroyed": pppMPPEInDestroyed,
       "pppMPPEOutPackets": pppMPPEOutPackets,
       "pppMPPEOutOctets": pppMPPEOutOctets,
       "pppMPPEOutDestroyed": pppMPPEOutDestroyed,
       "ibmIROCroutingdlsw": ibmIROCroutingdlsw,
       "ibmdlswTConnGroupOperTable": ibmdlswTConnGroupOperTable,
       "ibmdlswTConnGroupOperEntry": ibmdlswTConnGroupOperEntry,
       "ibmdlswTConnGroupOperIndex": ibmdlswTConnGroupOperIndex,
       "ibmdlswTConnGroupOperRole": ibmdlswTConnGroupOperRole,
       "ibmdlswTConnGroupOperJoinTime": ibmdlswTConnGroupOperJoinTime,
       "ibmdlswTConnGroupOperConfigIndex": ibmdlswTConnGroupOperConfigIndex,
       "ibmdlswTConnGroupOperInDataPkts": ibmdlswTConnGroupOperInDataPkts,
       "ibmdlswTConnGroupOperOutDataPkts": ibmdlswTConnGroupOperOutDataPkts,
       "ibmdlswTConnGroupOperInDataOctets": ibmdlswTConnGroupOperInDataOctets,
       "ibmdlswTConnGroupOperOutDataOctets": ibmdlswTConnGroupOperOutDataOctets,
       "ibmdlswTConnGroupOperInCntlPkts": ibmdlswTConnGroupOperInCntlPkts,
       "ibmdlswTConnGroupOperOutCntlPkts": ibmdlswTConnGroupOperOutCntlPkts,
       "ibmdlswTConnGroupOperCURexSents": ibmdlswTConnGroupOperCURexSents,
       "ibmdlswTConnGroupOperICRexRcvds": ibmdlswTConnGroupOperICRexRcvds,
       "ibmdlswTConnGroupOperCURexRcvds": ibmdlswTConnGroupOperCURexRcvds,
       "ibmdlswTConnGroupOperICRexSents": ibmdlswTConnGroupOperICRexSents,
       "ibmdlswTConnGroupOperNQexSents": ibmdlswTConnGroupOperNQexSents,
       "ibmdlswTConnGroupOperNRexRcvds": ibmdlswTConnGroupOperNRexRcvds,
       "ibmdlswTConnGroupOperNQexRcvds": ibmdlswTConnGroupOperNQexRcvds,
       "ibmdlswTConnGroupOperNRexSents": ibmdlswTConnGroupOperNRexSents,
       "ibmdlswQllcLsTable": ibmdlswQllcLsTable,
       "ibmdlswQllcLsEntry": ibmdlswQllcLsEntry,
       "ibmdlswQllcLsIfIndex": ibmdlswQllcLsIfIndex,
       "ibmdlswQllcLsQdomain": ibmdlswQllcLsQdomain,
       "ibmdlswQllcLsQaddress": ibmdlswQllcLsQaddress,
       "ibmdlswQllcLsChannel": ibmdlswQllcLsChannel,
       "ibmdlswQllcLsLocalMac": ibmdlswQllcLsLocalMac,
       "ibmdlswQllcLsLocalSap": ibmdlswQllcLsLocalSap,
       "ibmdlswQllcLsRemoteMac": ibmdlswQllcLsRemoteMac,
       "ibmdlswQllcLsRemoteSap": ibmdlswQllcLsRemoteSap,
       "ibmdlswQllcLsPuType": ibmdlswQllcLsPuType,
       "ibmdlswQllcLsBlkNum": ibmdlswQllcLsBlkNum,
       "ibmdlswQllcLsIdNum": ibmdlswQllcLsIdNum,
       "ibmIROCroutingfr": ibmIROCroutingfr,
       "frCLLMStatsTable": frCLLMStatsTable,
       "frCLLMStatsEntry": frCLLMStatsEntry,
       "frCLLMStatsIfIndex": frCLLMStatsIfIndex,
       "frCLLMStatsDlci": frCLLMStatsDlci,
       "frCLLMStatsRcvds": frCLLMStatsRcvds,
       "frCLLMCauseTable": frCLLMCauseTable,
       "frCLLMCauseEntry": frCLLMCauseEntry,
       "frCLLMCauseIfIndex": frCLLMCauseIfIndex,
       "frCLLMCauseCode": frCLLMCauseCode,
       "frSimpleObjs": frSimpleObjs,
       "frCLLMDlciList": frCLLMDlciList,
       "frTrapStateFECN": frTrapStateFECN,
       "frTrapStateBECN": frTrapStateBECN,
       "frTrapStateCLLM": frTrapStateCLLM,
       "ibmIROCfrBRS": ibmIROCfrBRS,
       "ibmIROCfrcircuit": ibmIROCfrcircuit,
       "ibmIROCroutingRlan": ibmIROCroutingRlan,
       "ibmIROCroutingDialOut": ibmIROCroutingDialOut,
       "ibmIROCroutingl2tp": ibmIROCroutingl2tp,
       "ibmCacheServer": ibmCacheServer,
       "ibmIROCroutingIpSec": ibmIROCroutingIpSec,
       "ibmIROCswhw": ibmIROCswhw,
       "ibmWanRestoralRerouteMIB": ibmWanRestoralRerouteMIB,
       "ibmBANMIB": ibmBANMIB,
       "ibmIROCrmon": ibmIROCrmon,
       "ibmIROCescon": ibmIROCescon,
       "ibmIROCVPNpolicy": ibmIROCVPNpolicy,
       "ibmIROCroutingvoice": ibmIROCroutingvoice,
       "ibmIROCroutinginterface": ibmIROCroutinginterface,
       "ibmIROCroutingtn3270e": ibmIROCroutingtn3270e,
       "ibmIROCroutingtcpip": ibmIROCroutingtcpip,
       "tcpiprouteTabSize": tcpiprouteTabSize,
       "tcpiprouteTabUsed": tcpiprouteTabUsed,
       "tcpiprouteCacheSize": tcpiprouteCacheSize,
       "tcpiprouteCacheUsed": tcpiprouteCacheUsed,
       "tcpiprouteOverFlow": tcpiprouteOverFlow,
       "tcpiprouteNoReach": tcpiprouteNoReach,
       "tcpiprouteBadSubnet": tcpiprouteBadSubnet,
       "tcpiprouteBadNet": tcpiprouteBadNet,
       "tcpiprouteUnhBcast": tcpiprouteUnhBcast,
       "tcpiprouteUnhMcast": tcpiprouteUnhMcast,
       "tcpiprouteUnhDirBcast": tcpiprouteUnhDirBcast,
       "tcpiprouteUnhLLbcast": tcpiprouteUnhLLbcast,
       "tcpiprouteDiscFilt": tcpiprouteDiscFilt,
       "tcpiprouteMultRcvd": tcpiprouteMultRcvd,
       "tcpCurrConnections": tcpCurrConnections,
       "tcpMaxConnections": tcpMaxConnections,
       "serverCurrConnections": serverCurrConnections,
       "serverMaxConnections": serverMaxConnections,
       "ibmIROCswitching": ibmIROCswitching,
       "ibmIROCtraps": ibmIROCtraps,
       "ibmIROCtrapsfr": ibmIROCtrapsfr,
       "frrcvdFECN": frrcvdFECN,
       "frrcvdBECN": frrcvdBECN,
       "frrcvdCLLM": frrcvdCLLM,
       "ibmIROCtrapssys": ibmIROCtrapssys,
       "mosMemLow": mosMemLow,
       "ibmIROCtrapsels": ibmIROCtrapsels,
       "elsTrap": elsTrap,
       "ibmIROCconfig": ibmIROCconfig,
       "ibmIROCconfigAuth": ibmIROCconfigAuth,
       "ibmIROCconfigWrite": ibmIROCconfigWrite}
)
