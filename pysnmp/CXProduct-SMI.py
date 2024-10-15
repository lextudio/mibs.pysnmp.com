# SNMP MIB module (CXProduct-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXProduct-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:02 2024
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

(cxProduct,) = mibBuilder.importSymbols(
    "MEMOTEC-SMI",
    "cxProduct")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class SapIndex(Integer32):
    """Custom type SapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )





class Alias(DisplayString):
    """Custom type Alias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )





class ThruputClass(Integer32):
    """Custom type ThruputClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
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
        *(("bps1200", 7),
          ("bps150", 4),
          ("bps19200", 11),
          ("bps2400", 8),
          ("bps300", 5),
          ("bps4800", 9),
          ("bps48000", 12),
          ("bps600", 6),
          ("bps64000", 13),
          ("bps75", 3),
          ("bps9600", 10))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CxMc600_ObjectIdentity = ObjectIdentity
cxMc600 = _CxMc600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1)
)
_CxPx600_ObjectIdentity = ObjectIdentity
cxPx600 = _CxPx600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 2)
)
_CxViewing_ObjectIdentity = ObjectIdentity
cxViewing = _CxViewing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 3)
)
_CxChassis_ObjectIdentity = ObjectIdentity
cxChassis = _CxChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 4)
)
_CxSystem_ObjectIdentity = ObjectIdentity
cxSystem = _CxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5)
)
_CxModuleHardware_ObjectIdentity = ObjectIdentity
cxModuleHardware = _CxModuleHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1)
)
_CxIoHardware_ObjectIdentity = ObjectIdentity
cxIoHardware = _CxIoHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2)
)
_CxFileServer_ObjectIdentity = ObjectIdentity
cxFileServer = _CxFileServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3)
)
_CxSecurityLevel_ObjectIdentity = ObjectIdentity
cxSecurityLevel = _CxSecurityLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 4)
)
_CxOperatingSystem_ObjectIdentity = ObjectIdentity
cxOperatingSystem = _CxOperatingSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5)
)
_CxConsoleDriver_ObjectIdentity = ObjectIdentity
cxConsoleDriver = _CxConsoleDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6)
)
_CxInterApplicationModule_ObjectIdentity = ObjectIdentity
cxInterApplicationModule = _CxInterApplicationModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 7)
)
_CxUserInterface_ObjectIdentity = ObjectIdentity
cxUserInterface = _CxUserInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 8)
)
_CxTokenBus_ObjectIdentity = ObjectIdentity
cxTokenBus = _CxTokenBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9)
)
_CxLanIoPort_ObjectIdentity = ObjectIdentity
cxLanIoPort = _CxLanIoPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10)
)
_CxSubSysInfo_ObjectIdentity = ObjectIdentity
cxSubSysInfo = _CxSubSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 11)
)
_CxIoHwInfo_ObjectIdentity = ObjectIdentity
cxIoHwInfo = _CxIoHwInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 12)
)
_CxSystemManagement_ObjectIdentity = ObjectIdentity
cxSystemManagement = _CxSystemManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 13)
)
_CxCommonConsole_ObjectIdentity = ObjectIdentity
cxCommonConsole = _CxCommonConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14)
)
_CxPmb_ObjectIdentity = ObjectIdentity
cxPmb = _CxPmb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 15)
)
_CxPortManager_ObjectIdentity = ObjectIdentity
cxPortManager = _CxPortManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16)
)
_CxEventManager_ObjectIdentity = ObjectIdentity
cxEventManager = _CxEventManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17)
)
_CxDownload_ObjectIdentity = ObjectIdentity
cxDownload = _CxDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 18)
)
_CxApplication_ObjectIdentity = ObjectIdentity
cxApplication = _CxApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6)
)
_CxBitOrientedProtocolDriver_ObjectIdentity = ObjectIdentity
cxBitOrientedProtocolDriver = _CxBitOrientedProtocolDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 1)
)
_CxFrameRelayInterfaceModule_ObjectIdentity = ObjectIdentity
cxFrameRelayInterfaceModule = _CxFrameRelayInterfaceModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2)
)
_CxFrameRelay_ObjectIdentity = ObjectIdentity
cxFrameRelay = _CxFrameRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3)
)
_CxSdxi_ObjectIdentity = ObjectIdentity
cxSdxi = _CxSdxi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 4)
)
_CxGwMux_ObjectIdentity = ObjectIdentity
cxGwMux = _CxGwMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5)
)
_CxIf_ObjectIdentity = ObjectIdentity
cxIf = _CxIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 6)
)
_CxTransmission_ObjectIdentity = ObjectIdentity
cxTransmission = _CxTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 7)
)
_CxConv_ObjectIdentity = ObjectIdentity
cxConv = _CxConv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8)
)
_CxDot1dBridge_ObjectIdentity = ObjectIdentity
cxDot1dBridge = _CxDot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 9)
)
_CxIp_ObjectIdentity = ObjectIdentity
cxIp = _CxIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 10)
)
_CxIcmp_ObjectIdentity = ObjectIdentity
cxIcmp = _CxIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11)
)
_CxUdp_ObjectIdentity = ObjectIdentity
cxUdp = _CxUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 12)
)
_CxIpx_ObjectIdentity = ObjectIdentity
cxIpx = _CxIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13)
)
_CxCfgDot1dBase_ObjectIdentity = ObjectIdentity
cxCfgDot1dBase = _CxCfgDot1dBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14)
)
_CxCfgIpSap_ObjectIdentity = ObjectIdentity
cxCfgIpSap = _CxCfgIpSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15)
)
_CxCfgIp_ObjectIdentity = ObjectIdentity
cxCfgIp = _CxCfgIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16)
)
_CxCfgSrBase_ObjectIdentity = ObjectIdentity
cxCfgSrBase = _CxCfgSrBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17)
)
_CxGwFr_ObjectIdentity = ObjectIdentity
cxGwFr = _CxGwFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18)
)
_CxGwX25_ObjectIdentity = ObjectIdentity
cxGwX25 = _CxGwX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 19)
)
_CxPppAsyncDriver_ObjectIdentity = ObjectIdentity
cxPppAsyncDriver = _CxPppAsyncDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 20)
)
_CxFltIp_ObjectIdentity = ObjectIdentity
cxFltIp = _CxFltIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21)
)
_CxFltIpx_ObjectIdentity = ObjectIdentity
cxFltIpx = _CxFltIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22)
)
_CxAdxi_ObjectIdentity = ObjectIdentity
cxAdxi = _CxAdxi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 23)
)
_CxCompression_ObjectIdentity = ObjectIdentity
cxCompression = _CxCompression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 24)
)
_CxEthernetDriver_ObjectIdentity = ObjectIdentity
cxEthernetDriver = _CxEthernetDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 25)
)
_CxPpp_ObjectIdentity = ObjectIdentity
cxPpp = _CxPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 26)
)
_CxLapBD_ObjectIdentity = ObjectIdentity
cxLapBD = _CxLapBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27)
)
_CxLapBConv_ObjectIdentity = ObjectIdentity
cxLapBConv = _CxLapBConv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28)
)
_CxX25_ObjectIdentity = ObjectIdentity
cxX25 = _CxX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29)
)
_CxAsync_ObjectIdentity = ObjectIdentity
cxAsync = _CxAsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30)
)
_CxSNA_ObjectIdentity = ObjectIdentity
cxSNA = _CxSNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 31)
)
_CxISDN_ObjectIdentity = ObjectIdentity
cxISDN = _CxISDN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32)
)
_CxLlcFrConv_ObjectIdentity = ObjectIdentity
cxLlcFrConv = _CxLlcFrConv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33)
)
_CxLlcim_ObjectIdentity = ObjectIdentity
cxLlcim = _CxLlcim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 34)
)
_CxSnalc_ObjectIdentity = ObjectIdentity
cxSnalc = _CxSnalc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35)
)
_CxBOPIO_ObjectIdentity = ObjectIdentity
cxBOPIO = _CxBOPIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36)
)
_CxSDLC_ObjectIdentity = ObjectIdentity
cxSDLC = _CxSDLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37)
)
_CxQLLC_ObjectIdentity = ObjectIdentity
cxQLLC = _CxQLLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38)
)
_CxDds_ObjectIdentity = ObjectIdentity
cxDds = _CxDds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39)
)
_CxUTst_ObjectIdentity = ObjectIdentity
cxUTst = _CxUTst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40)
)
_CxUDrv_ObjectIdentity = ObjectIdentity
cxUDrv = _CxUDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41)
)
_CxV34_ObjectIdentity = ObjectIdentity
cxV34 = _CxV34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42)
)
_CxOSP_ObjectIdentity = ObjectIdentity
cxOSP = _CxOSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 43)
)
_CxAsyncIo_ObjectIdentity = ObjectIdentity
cxAsyncIo = _CxAsyncIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44)
)
_CxEthIo_ObjectIdentity = ObjectIdentity
cxEthIo = _CxEthIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45)
)
_CxDial_ObjectIdentity = ObjectIdentity
cxDial = _CxDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46)
)
_CxLlcLanConv_ObjectIdentity = ObjectIdentity
cxLlcLanConv = _CxLlcLanConv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47)
)
_CxBCM_ObjectIdentity = ObjectIdentity
cxBCM = _CxBCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48)
)
_CxMLPPP_ObjectIdentity = ObjectIdentity
cxMLPPP = _CxMLPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49)
)
_CxVR_ObjectIdentity = ObjectIdentity
cxVR = _CxVR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50)
)
_CxTrdIo_ObjectIdentity = ObjectIdentity
cxTrdIo = _CxTrdIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51)
)
_CxDSX1_ObjectIdentity = ObjectIdentity
cxDSX1 = _CxDSX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 52)
)
_CxDSX1Ext_ObjectIdentity = ObjectIdentity
cxDSX1Ext = _CxDSX1Ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53)
)
_CxGim_ObjectIdentity = ObjectIdentity
cxGim = _CxGim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55)
)
_CxBsc_ObjectIdentity = ObjectIdentity
cxBsc = _CxBsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56)
)
_CxDsp_ObjectIdentity = ObjectIdentity
cxDsp = _CxDsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57)
)
_CxAtmDxi_ObjectIdentity = ObjectIdentity
cxAtmDxi = _CxAtmDxi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58)
)
_CxCAS_ObjectIdentity = ObjectIdentity
cxCAS = _CxCAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59)
)
_CxST_ObjectIdentity = ObjectIdentity
cxST = _CxST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60)
)
_CxAtmPhy_ObjectIdentity = ObjectIdentity
cxAtmPhy = _CxAtmPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61)
)
_CxAtmExt_ObjectIdentity = ObjectIdentity
cxAtmExt = _CxAtmExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 62)
)
_CxPCM_ObjectIdentity = ObjectIdentity
cxPCM = _CxPCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63)
)
_CxRegistration_ObjectIdentity = ObjectIdentity
cxRegistration = _CxRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7)
)
_CxRegChassis_ObjectIdentity = ObjectIdentity
cxRegChassis = _CxRegChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1)
)
_CxRegChasCX1000_ObjectIdentity = ObjectIdentity
cxRegChasCX1000 = _CxRegChasCX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1, 1)
)
_CxRegChasCX900_ObjectIdentity = ObjectIdentity
cxRegChasCX900 = _CxRegChasCX900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1, 2)
)
_CxRegChasCX950_ObjectIdentity = ObjectIdentity
cxRegChasCX950 = _CxRegChasCX950_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1, 3)
)
_CxRegSubSystem_ObjectIdentity = ObjectIdentity
cxRegSubSystem = _CxRegSubSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2)
)
_CxRegSubSysMC600_ObjectIdentity = ObjectIdentity
cxRegSubSysMC600 = _CxRegSubSysMC600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 1)
)
_CxRegSubSysAC600_ObjectIdentity = ObjectIdentity
cxRegSubSysAC600 = _CxRegSubSysAC600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 2)
)
_CxRegSubSysPX600_ObjectIdentity = ObjectIdentity
cxRegSubSysPX600 = _CxRegSubSysPX600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 3)
)
_CxRegSubSysFR600_ObjectIdentity = ObjectIdentity
cxRegSubSysFR600 = _CxRegSubSysFR600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 4)
)
_CxRegSubSysCL600_ObjectIdentity = ObjectIdentity
cxRegSubSysCL600 = _CxRegSubSysCL600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 5)
)
_CxRegSubSysLF600_ObjectIdentity = ObjectIdentity
cxRegSubSysLF600 = _CxRegSubSysLF600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 6)
)
_CxRegSubSysDI600_ObjectIdentity = ObjectIdentity
cxRegSubSysDI600 = _CxRegSubSysDI600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 7)
)
_CxRegSubSysFX600_ObjectIdentity = ObjectIdentity
cxRegSubSysFX600 = _CxRegSubSysFX600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 8)
)
_CxPrivate_ObjectIdentity = ObjectIdentity
cxPrivate = _CxPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8)
)
_CxACTE_ObjectIdentity = ObjectIdentity
cxACTE = _CxACTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1)
)
_CxT1E1_ObjectIdentity = ObjectIdentity
cxT1E1 = _CxT1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 2)
)
_CxDataScope_ObjectIdentity = ObjectIdentity
cxDataScope = _CxDataScope_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3)
)
_CxBri_ObjectIdentity = ObjectIdentity
cxBri = _CxBri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 4)
)
_CxChassis2_ObjectIdentity = ObjectIdentity
cxChassis2 = _CxChassis2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXProduct-SMI",
    **{"SapIndex": SapIndex,
       "Alias": Alias,
       "ThruputClass": ThruputClass,
       "cxMc600": cxMc600,
       "cxPx600": cxPx600,
       "cxViewing": cxViewing,
       "cxChassis": cxChassis,
       "cxSystem": cxSystem,
       "cxModuleHardware": cxModuleHardware,
       "cxIoHardware": cxIoHardware,
       "cxFileServer": cxFileServer,
       "cxSecurityLevel": cxSecurityLevel,
       "cxOperatingSystem": cxOperatingSystem,
       "cxConsoleDriver": cxConsoleDriver,
       "cxInterApplicationModule": cxInterApplicationModule,
       "cxUserInterface": cxUserInterface,
       "cxTokenBus": cxTokenBus,
       "cxLanIoPort": cxLanIoPort,
       "cxSubSysInfo": cxSubSysInfo,
       "cxIoHwInfo": cxIoHwInfo,
       "cxSystemManagement": cxSystemManagement,
       "cxCommonConsole": cxCommonConsole,
       "cxPmb": cxPmb,
       "cxPortManager": cxPortManager,
       "cxEventManager": cxEventManager,
       "cxDownload": cxDownload,
       "cxApplication": cxApplication,
       "cxBitOrientedProtocolDriver": cxBitOrientedProtocolDriver,
       "cxFrameRelayInterfaceModule": cxFrameRelayInterfaceModule,
       "cxFrameRelay": cxFrameRelay,
       "cxSdxi": cxSdxi,
       "cxGwMux": cxGwMux,
       "cxIf": cxIf,
       "cxTransmission": cxTransmission,
       "cxConv": cxConv,
       "cxDot1dBridge": cxDot1dBridge,
       "cxIp": cxIp,
       "cxIcmp": cxIcmp,
       "cxUdp": cxUdp,
       "cxIpx": cxIpx,
       "cxCfgDot1dBase": cxCfgDot1dBase,
       "cxCfgIpSap": cxCfgIpSap,
       "cxCfgIp": cxCfgIp,
       "cxCfgSrBase": cxCfgSrBase,
       "cxGwFr": cxGwFr,
       "cxGwX25": cxGwX25,
       "cxPppAsyncDriver": cxPppAsyncDriver,
       "cxFltIp": cxFltIp,
       "cxFltIpx": cxFltIpx,
       "cxAdxi": cxAdxi,
       "cxCompression": cxCompression,
       "cxEthernetDriver": cxEthernetDriver,
       "cxPpp": cxPpp,
       "cxLapBD": cxLapBD,
       "cxLapBConv": cxLapBConv,
       "cxX25": cxX25,
       "cxAsync": cxAsync,
       "cxSNA": cxSNA,
       "cxISDN": cxISDN,
       "cxLlcFrConv": cxLlcFrConv,
       "cxLlcim": cxLlcim,
       "cxSnalc": cxSnalc,
       "cxBOPIO": cxBOPIO,
       "cxSDLC": cxSDLC,
       "cxQLLC": cxQLLC,
       "cxDds": cxDds,
       "cxUTst": cxUTst,
       "cxUDrv": cxUDrv,
       "cxV34": cxV34,
       "cxOSP": cxOSP,
       "cxAsyncIo": cxAsyncIo,
       "cxEthIo": cxEthIo,
       "cxDial": cxDial,
       "cxLlcLanConv": cxLlcLanConv,
       "cxBCM": cxBCM,
       "cxMLPPP": cxMLPPP,
       "cxVR": cxVR,
       "cxTrdIo": cxTrdIo,
       "cxDSX1": cxDSX1,
       "cxDSX1Ext": cxDSX1Ext,
       "cxGim": cxGim,
       "cxBsc": cxBsc,
       "cxDsp": cxDsp,
       "cxAtmDxi": cxAtmDxi,
       "cxCAS": cxCAS,
       "cxST": cxST,
       "cxAtmPhy": cxAtmPhy,
       "cxAtmExt": cxAtmExt,
       "cxPCM": cxPCM,
       "cxRegistration": cxRegistration,
       "cxRegChassis": cxRegChassis,
       "cxRegChasCX1000": cxRegChasCX1000,
       "cxRegChasCX900": cxRegChasCX900,
       "cxRegChasCX950": cxRegChasCX950,
       "cxRegSubSystem": cxRegSubSystem,
       "cxRegSubSysMC600": cxRegSubSysMC600,
       "cxRegSubSysAC600": cxRegSubSysAC600,
       "cxRegSubSysPX600": cxRegSubSysPX600,
       "cxRegSubSysFR600": cxRegSubSysFR600,
       "cxRegSubSysCL600": cxRegSubSysCL600,
       "cxRegSubSysLF600": cxRegSubSysLF600,
       "cxRegSubSysDI600": cxRegSubSysDI600,
       "cxRegSubSysFX600": cxRegSubSysFX600,
       "cxPrivate": cxPrivate,
       "cxACTE": cxACTE,
       "cxT1E1": cxT1E1,
       "cxDataScope": cxDataScope,
       "cxBri": cxBri,
       "cxChassis2": cxChassis2}
)
