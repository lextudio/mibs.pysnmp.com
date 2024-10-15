# SNMP MIB module (FOUNDRY-SN-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-ROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:18 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

foundry = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991)
)
foundry.setRevisions(
        ("2010-06-02 00:00",
         "2009-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnTraps_ObjectIdentity = ObjectIdentity
snTraps = _SnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 0)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1)
)
_SnChassis_ObjectIdentity = ObjectIdentity
snChassis = _SnChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1)
)
_SnAgentSys_ObjectIdentity = ObjectIdentity
snAgentSys = _SnAgentSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2)
)
_SnSwitch_ObjectIdentity = ObjectIdentity
snSwitch = _SnSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3)
)
_SnL4_ObjectIdentity = ObjectIdentity
snL4 = _SnL4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 4)
)
_SnStack_ObjectIdentity = ObjectIdentity
snStack = _SnStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5)
)
_SnSci_ObjectIdentity = ObjectIdentity
snSci = _SnSci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 6)
)
_FdrySntp_ObjectIdentity = ObjectIdentity
fdrySntp = _FdrySntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7)
)
_FdryRadius_ObjectIdentity = ObjectIdentity
fdryRadius = _FdryRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 8)
)
_FdryTacacs_ObjectIdentity = ObjectIdentity
fdryTacacs = _FdryTacacs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 9)
)
_FdryTrap_ObjectIdentity = ObjectIdentity
fdryTrap = _FdryTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 10)
)
_BrcdSysLog_ObjectIdentity = ObjectIdentity
brcdSysLog = _BrcdSysLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 11)
)
_BrcdMct_ObjectIdentity = ObjectIdentity
brcdMct = _BrcdMct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 12)
)
_BrcdFabric_ObjectIdentity = ObjectIdentity
brcdFabric = _BrcdFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 13)
)
_BrcdQos_ObjectIdentity = ObjectIdentity
brcdQos = _BrcdQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 14)
)
_BrcdIPSec_ObjectIdentity = ObjectIdentity
brcdIPSec = _BrcdIPSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 15)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2)
)
_SnIpx_ObjectIdentity = ObjectIdentity
snIpx = _SnIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1)
)
_SnIp_ObjectIdentity = ObjectIdentity
snIp = _SnIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2)
)
_SnRip_ObjectIdentity = ObjectIdentity
snRip = _SnRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 3)
)
_SnOspf_ObjectIdentity = ObjectIdentity
snOspf = _SnOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4)
)
_SnDvmrp_ObjectIdentity = ObjectIdentity
snDvmrp = _SnDvmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 5)
)
_SnIgmp_ObjectIdentity = ObjectIdentity
snIgmp = _SnIgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 6)
)
_SnFsrp_ObjectIdentity = ObjectIdentity
snFsrp = _SnFsrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 7)
)
_SnGblRt_ObjectIdentity = ObjectIdentity
snGblRt = _SnGblRt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 8)
)
_SnPim_ObjectIdentity = ObjectIdentity
snPim = _SnPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 9)
)
_SnAppleTalk_ObjectIdentity = ObjectIdentity
snAppleTalk = _SnAppleTalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10)
)
_SnBgp4_ObjectIdentity = ObjectIdentity
snBgp4 = _SnBgp4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 11)
)
_SnVrrp_ObjectIdentity = ObjectIdentity
snVrrp = _SnVrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 12)
)
_SnLoopbackIf_ObjectIdentity = ObjectIdentity
snLoopbackIf = _SnLoopbackIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 13)
)
_SnPOS_ObjectIdentity = ObjectIdentity
snPOS = _SnPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14)
)
_SnMpls_ObjectIdentity = ObjectIdentity
snMpls = _SnMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15)
)
_FdryAcl_ObjectIdentity = ObjectIdentity
fdryAcl = _FdryAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 16)
)
_FdryIpv6_ObjectIdentity = ObjectIdentity
fdryIpv6 = _FdryIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 17)
)
_Registration_ObjectIdentity = ObjectIdentity
registration = _Registration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3)
)
_SnFastIron_ObjectIdentity = ObjectIdentity
snFastIron = _SnFastIron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 1)
)
_SnFIWGSwitch_ObjectIdentity = ObjectIdentity
snFIWGSwitch = _SnFIWGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 1, 1)
)
_SnFIBBSwitch_ObjectIdentity = ObjectIdentity
snFIBBSwitch = _SnFIBBSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 1, 2)
)
_SnNetIron_ObjectIdentity = ObjectIdentity
snNetIron = _SnNetIron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 2)
)
_SnNIRouter_ObjectIdentity = ObjectIdentity
snNIRouter = _SnNIRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 2, 1)
)
_SnServerIron_ObjectIdentity = ObjectIdentity
snServerIron = _SnServerIron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 3)
)
_SnSI_ObjectIdentity = ObjectIdentity
snSI = _SnSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 3, 1)
)
_SnSIXL_ObjectIdentity = ObjectIdentity
snSIXL = _SnSIXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 3, 2)
)
_SnSIXLTCS_ObjectIdentity = ObjectIdentity
snSIXLTCS = _SnSIXLTCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 3, 3)
)
_SnTurboIron_ObjectIdentity = ObjectIdentity
snTurboIron = _SnTurboIron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 4)
)
_SnTISwitch_ObjectIdentity = ObjectIdentity
snTISwitch = _SnTISwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 4, 1)
)
_SnTIRouter_ObjectIdentity = ObjectIdentity
snTIRouter = _SnTIRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 4, 2)
)
_SnTurboIron8_ObjectIdentity = ObjectIdentity
snTurboIron8 = _SnTurboIron8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 5)
)
_SnT8Switch_ObjectIdentity = ObjectIdentity
snT8Switch = _SnT8Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 5, 1)
)
_SnT8Router_ObjectIdentity = ObjectIdentity
snT8Router = _SnT8Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 5, 2)
)
_SnT8SI_ObjectIdentity = ObjectIdentity
snT8SI = _SnT8SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 5, 3)
)
_SnT8SIXLG_ObjectIdentity = ObjectIdentity
snT8SIXLG = _SnT8SIXLG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 5, 4)
)
_SnBigIron4000_ObjectIdentity = ObjectIdentity
snBigIron4000 = _SnBigIron4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 6)
)
_SnBI4000Switch_ObjectIdentity = ObjectIdentity
snBI4000Switch = _SnBI4000Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 6, 1)
)
_SnBI4000Router_ObjectIdentity = ObjectIdentity
snBI4000Router = _SnBI4000Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 6, 2)
)
_SnBI4000SI_ObjectIdentity = ObjectIdentity
snBI4000SI = _SnBI4000SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 6, 3)
)
_SnBigIron8000_ObjectIdentity = ObjectIdentity
snBigIron8000 = _SnBigIron8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 7)
)
_SnBI8000Switch_ObjectIdentity = ObjectIdentity
snBI8000Switch = _SnBI8000Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 7, 1)
)
_SnBI8000Router_ObjectIdentity = ObjectIdentity
snBI8000Router = _SnBI8000Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 7, 2)
)
_SnBI8000SI_ObjectIdentity = ObjectIdentity
snBI8000SI = _SnBI8000SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 7, 3)
)
_SnFastIron2_ObjectIdentity = ObjectIdentity
snFastIron2 = _SnFastIron2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 8)
)
_SnFI2Switch_ObjectIdentity = ObjectIdentity
snFI2Switch = _SnFI2Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 8, 1)
)
_SnFI2Router_ObjectIdentity = ObjectIdentity
snFI2Router = _SnFI2Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 8, 2)
)
_SnFastIron2Plus_ObjectIdentity = ObjectIdentity
snFastIron2Plus = _SnFastIron2Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 9)
)
_SnFI2PlusSwitch_ObjectIdentity = ObjectIdentity
snFI2PlusSwitch = _SnFI2PlusSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 9, 1)
)
_SnFI2PlusRouter_ObjectIdentity = ObjectIdentity
snFI2PlusRouter = _SnFI2PlusRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 9, 2)
)
_SnNetIron400_ObjectIdentity = ObjectIdentity
snNetIron400 = _SnNetIron400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 10)
)
_SnNI400Router_ObjectIdentity = ObjectIdentity
snNI400Router = _SnNI400Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 10, 1)
)
_SnNetIron800_ObjectIdentity = ObjectIdentity
snNetIron800 = _SnNetIron800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 11)
)
_SnNI800Router_ObjectIdentity = ObjectIdentity
snNI800Router = _SnNI800Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 11, 1)
)
_SnFastIron2GC_ObjectIdentity = ObjectIdentity
snFastIron2GC = _SnFastIron2GC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 12)
)
_SnFI2GCSwitch_ObjectIdentity = ObjectIdentity
snFI2GCSwitch = _SnFI2GCSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 12, 1)
)
_SnFI2GCRouter_ObjectIdentity = ObjectIdentity
snFI2GCRouter = _SnFI2GCRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 12, 2)
)
_SnFastIron2PlusGC_ObjectIdentity = ObjectIdentity
snFastIron2PlusGC = _SnFastIron2PlusGC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 13)
)
_SnFI2PlusGCSwitch_ObjectIdentity = ObjectIdentity
snFI2PlusGCSwitch = _SnFI2PlusGCSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 13, 1)
)
_SnFI2PlusGCRouter_ObjectIdentity = ObjectIdentity
snFI2PlusGCRouter = _SnFI2PlusGCRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 13, 2)
)
_SnBigIron15000_ObjectIdentity = ObjectIdentity
snBigIron15000 = _SnBigIron15000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 14)
)
_SnBI15000Switch_ObjectIdentity = ObjectIdentity
snBI15000Switch = _SnBI15000Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 14, 1)
)
_SnBI15000Router_ObjectIdentity = ObjectIdentity
snBI15000Router = _SnBI15000Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 14, 2)
)
_SnBI15000SI_ObjectIdentity = ObjectIdentity
snBI15000SI = _SnBI15000SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 14, 3)
)
_SnNetIron1500_ObjectIdentity = ObjectIdentity
snNetIron1500 = _SnNetIron1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 15)
)
_SnNI1500Router_ObjectIdentity = ObjectIdentity
snNI1500Router = _SnNI1500Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 15, 1)
)
_SnFastIron3_ObjectIdentity = ObjectIdentity
snFastIron3 = _SnFastIron3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 16)
)
_SnFI3Switch_ObjectIdentity = ObjectIdentity
snFI3Switch = _SnFI3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 16, 1)
)
_SnFI3Router_ObjectIdentity = ObjectIdentity
snFI3Router = _SnFI3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 16, 2)
)
_SnFastIron3GC_ObjectIdentity = ObjectIdentity
snFastIron3GC = _SnFastIron3GC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 17)
)
_SnFI3GCSwitch_ObjectIdentity = ObjectIdentity
snFI3GCSwitch = _SnFI3GCSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 17, 1)
)
_SnFI3GCRouter_ObjectIdentity = ObjectIdentity
snFI3GCRouter = _SnFI3GCRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 17, 2)
)
_SnServerIron400_ObjectIdentity = ObjectIdentity
snServerIron400 = _SnServerIron400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 18)
)
_SnSI400Switch_ObjectIdentity = ObjectIdentity
snSI400Switch = _SnSI400Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 18, 1)
)
_SnSI400Router_ObjectIdentity = ObjectIdentity
snSI400Router = _SnSI400Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 18, 2)
)
_SnServerIron800_ObjectIdentity = ObjectIdentity
snServerIron800 = _SnServerIron800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 19)
)
_SnSI800Switch_ObjectIdentity = ObjectIdentity
snSI800Switch = _SnSI800Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 19, 1)
)
_SnSI800Router_ObjectIdentity = ObjectIdentity
snSI800Router = _SnSI800Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 19, 2)
)
_SnServerIron1500_ObjectIdentity = ObjectIdentity
snServerIron1500 = _SnServerIron1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 20)
)
_SnSI1500Switch_ObjectIdentity = ObjectIdentity
snSI1500Switch = _SnSI1500Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 20, 1)
)
_SnSI1500Router_ObjectIdentity = ObjectIdentity
snSI1500Router = _SnSI1500Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 20, 2)
)
_Sn4802_ObjectIdentity = ObjectIdentity
sn4802 = _Sn4802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 21)
)
_Sn4802Switch_ObjectIdentity = ObjectIdentity
sn4802Switch = _Sn4802Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 21, 1)
)
_Sn4802Router_ObjectIdentity = ObjectIdentity
sn4802Router = _Sn4802Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 21, 2)
)
_Sn4802SI_ObjectIdentity = ObjectIdentity
sn4802SI = _Sn4802SI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 21, 3)
)
_SnFastIron400_ObjectIdentity = ObjectIdentity
snFastIron400 = _SnFastIron400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 22)
)
_SnFI400Switch_ObjectIdentity = ObjectIdentity
snFI400Switch = _SnFI400Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 22, 1)
)
_SnFI400Router_ObjectIdentity = ObjectIdentity
snFI400Router = _SnFI400Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 22, 2)
)
_SnFastIron800_ObjectIdentity = ObjectIdentity
snFastIron800 = _SnFastIron800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 23)
)
_SnFI800Switch_ObjectIdentity = ObjectIdentity
snFI800Switch = _SnFI800Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 23, 1)
)
_SnFI800Router_ObjectIdentity = ObjectIdentity
snFI800Router = _SnFI800Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 23, 2)
)
_SnFastIron1500_ObjectIdentity = ObjectIdentity
snFastIron1500 = _SnFastIron1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 24)
)
_SnFI1500Switch_ObjectIdentity = ObjectIdentity
snFI1500Switch = _SnFI1500Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 24, 1)
)
_SnFI1500Router_ObjectIdentity = ObjectIdentity
snFI1500Router = _SnFI1500Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 24, 2)
)
_SnFES2402_ObjectIdentity = ObjectIdentity
snFES2402 = _SnFES2402_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 25)
)
_SnFES2402Switch_ObjectIdentity = ObjectIdentity
snFES2402Switch = _SnFES2402Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 25, 1)
)
_SnFES2402Router_ObjectIdentity = ObjectIdentity
snFES2402Router = _SnFES2402Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 25, 2)
)
_SnFES4802_ObjectIdentity = ObjectIdentity
snFES4802 = _SnFES4802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 26)
)
_SnFES4802Switch_ObjectIdentity = ObjectIdentity
snFES4802Switch = _SnFES4802Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 26, 1)
)
_SnFES4802Router_ObjectIdentity = ObjectIdentity
snFES4802Router = _SnFES4802Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 26, 2)
)
_SnFES9604_ObjectIdentity = ObjectIdentity
snFES9604 = _SnFES9604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 27)
)
_SnFES9604Switch_ObjectIdentity = ObjectIdentity
snFES9604Switch = _SnFES9604Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 27, 1)
)
_SnFES9604Router_ObjectIdentity = ObjectIdentity
snFES9604Router = _SnFES9604Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 27, 2)
)
_SnFES12GCF_ObjectIdentity = ObjectIdentity
snFES12GCF = _SnFES12GCF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 28)
)
_SnFES12GCFSwitch_ObjectIdentity = ObjectIdentity
snFES12GCFSwitch = _SnFES12GCFSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 28, 1)
)
_SnFES12GCFRouter_ObjectIdentity = ObjectIdentity
snFES12GCFRouter = _SnFES12GCFRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 28, 2)
)
_SnFES2402POE_ObjectIdentity = ObjectIdentity
snFES2402POE = _SnFES2402POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 29)
)
_SnFES2402POESwitch_ObjectIdentity = ObjectIdentity
snFES2402POESwitch = _SnFES2402POESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 29, 1)
)
_SnFES2402POERouter_ObjectIdentity = ObjectIdentity
snFES2402POERouter = _SnFES2402POERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 29, 2)
)
_SnFES4802POE_ObjectIdentity = ObjectIdentity
snFES4802POE = _SnFES4802POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 30)
)
_SnFES4802POESwitch_ObjectIdentity = ObjectIdentity
snFES4802POESwitch = _SnFES4802POESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 30, 1)
)
_SnFES4802POERouter_ObjectIdentity = ObjectIdentity
snFES4802POERouter = _SnFES4802POERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 30, 2)
)
_SnNetIron4802_ObjectIdentity = ObjectIdentity
snNetIron4802 = _SnNetIron4802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 31)
)
_SnNI4802Switch_ObjectIdentity = ObjectIdentity
snNI4802Switch = _SnNI4802Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 31, 1)
)
_SnNI4802Router_ObjectIdentity = ObjectIdentity
snNI4802Router = _SnNI4802Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 31, 2)
)
_SnBigIronMG8_ObjectIdentity = ObjectIdentity
snBigIronMG8 = _SnBigIronMG8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 32)
)
_SnBIMG8Switch_ObjectIdentity = ObjectIdentity
snBIMG8Switch = _SnBIMG8Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 32, 1)
)
_SnBIMG8Router_ObjectIdentity = ObjectIdentity
snBIMG8Router = _SnBIMG8Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 32, 2)
)
_SnNetIron40G_ObjectIdentity = ObjectIdentity
snNetIron40G = _SnNetIron40G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 33)
)
_SnNI40GRouter_ObjectIdentity = ObjectIdentity
snNI40GRouter = _SnNI40GRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 33, 2)
)
_SnFESXFamily_ObjectIdentity = ObjectIdentity
snFESXFamily = _SnFESXFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34)
)
_SnFESX424Family_ObjectIdentity = ObjectIdentity
snFESX424Family = _SnFESX424Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1)
)
_SnFESX424BaseFamily_ObjectIdentity = ObjectIdentity
snFESX424BaseFamily = _SnFESX424BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 1)
)
_SnFESX424_ObjectIdentity = ObjectIdentity
snFESX424 = _SnFESX424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 1, 1)
)
_SnFESX424Switch_ObjectIdentity = ObjectIdentity
snFESX424Switch = _SnFESX424Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 1, 1, 1)
)
_SnFESX424Router_ObjectIdentity = ObjectIdentity
snFESX424Router = _SnFESX424Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 1, 1, 2)
)
_SnFESX424Prem_ObjectIdentity = ObjectIdentity
snFESX424Prem = _SnFESX424Prem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 1, 2)
)
_SnFESX424PremSwitch_ObjectIdentity = ObjectIdentity
snFESX424PremSwitch = _SnFESX424PremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 1, 2, 1)
)
_SnFESX424PremRouter_ObjectIdentity = ObjectIdentity
snFESX424PremRouter = _SnFESX424PremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 1, 2, 2)
)
_SnFESX424Plus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX424Plus1XGFamily = _SnFESX424Plus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 2)
)
_SnFESX424Plus1XG_ObjectIdentity = ObjectIdentity
snFESX424Plus1XG = _SnFESX424Plus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 2, 1)
)
_SnFESX424Plus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX424Plus1XGSwitch = _SnFESX424Plus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 2, 1, 1)
)
_SnFESX424Plus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX424Plus1XGRouter = _SnFESX424Plus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 2, 1, 2)
)
_SnFESX424Plus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX424Plus1XGPrem = _SnFESX424Plus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 2, 2)
)
_SnFESX424Plus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX424Plus1XGPremSwitch = _SnFESX424Plus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 2, 2, 1)
)
_SnFESX424Plus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX424Plus1XGPremRouter = _SnFESX424Plus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 2, 2, 2)
)
_SnFESX424Plus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX424Plus2XGFamily = _SnFESX424Plus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 3)
)
_SnFESX424Plus2XG_ObjectIdentity = ObjectIdentity
snFESX424Plus2XG = _SnFESX424Plus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 3, 1)
)
_SnFESX424Plus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX424Plus2XGSwitch = _SnFESX424Plus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 3, 1, 1)
)
_SnFESX424Plus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX424Plus2XGRouter = _SnFESX424Plus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 3, 1, 2)
)
_SnFESX424Plus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX424Plus2XGPrem = _SnFESX424Plus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 3, 2)
)
_SnFESX424Plus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX424Plus2XGPremSwitch = _SnFESX424Plus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 3, 2, 1)
)
_SnFESX424Plus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX424Plus2XGPremRouter = _SnFESX424Plus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 1, 3, 2, 2)
)
_SnFESX448Family_ObjectIdentity = ObjectIdentity
snFESX448Family = _SnFESX448Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2)
)
_SnFESX448BaseFamily_ObjectIdentity = ObjectIdentity
snFESX448BaseFamily = _SnFESX448BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 1)
)
_SnFESX448_ObjectIdentity = ObjectIdentity
snFESX448 = _SnFESX448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 1, 1)
)
_SnFESX448Switch_ObjectIdentity = ObjectIdentity
snFESX448Switch = _SnFESX448Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 1, 1, 1)
)
_SnFESX448Router_ObjectIdentity = ObjectIdentity
snFESX448Router = _SnFESX448Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 1, 1, 2)
)
_SnFESX448Prem_ObjectIdentity = ObjectIdentity
snFESX448Prem = _SnFESX448Prem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 1, 2)
)
_SnFESX448PremSwitch_ObjectIdentity = ObjectIdentity
snFESX448PremSwitch = _SnFESX448PremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 1, 2, 1)
)
_SnFESX448PremRouter_ObjectIdentity = ObjectIdentity
snFESX448PremRouter = _SnFESX448PremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 1, 2, 2)
)
_SnFESX448Plus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX448Plus1XGFamily = _SnFESX448Plus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 2)
)
_SnFESX448Plus1XG_ObjectIdentity = ObjectIdentity
snFESX448Plus1XG = _SnFESX448Plus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 2, 1)
)
_SnFESX448Plus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX448Plus1XGSwitch = _SnFESX448Plus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 2, 1, 1)
)
_SnFESX448Plus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX448Plus1XGRouter = _SnFESX448Plus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 2, 1, 2)
)
_SnFESX448Plus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX448Plus1XGPrem = _SnFESX448Plus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 2, 2)
)
_SnFESX448Plus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX448Plus1XGPremSwitch = _SnFESX448Plus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 2, 2, 1)
)
_SnFESX448Plus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX448Plus1XGPremRouter = _SnFESX448Plus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 2, 2, 2)
)
_SnFESX448Plus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX448Plus2XGFamily = _SnFESX448Plus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 3)
)
_SnFESX448Plus2XG_ObjectIdentity = ObjectIdentity
snFESX448Plus2XG = _SnFESX448Plus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 3, 1)
)
_SnFESX448Plus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX448Plus2XGSwitch = _SnFESX448Plus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 3, 1, 1)
)
_SnFESX448Plus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX448Plus2XGRouter = _SnFESX448Plus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 3, 1, 2)
)
_SnFESX448Plus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX448Plus2XGPrem = _SnFESX448Plus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 3, 2)
)
_SnFESX448Plus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX448Plus2XGPremSwitch = _SnFESX448Plus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 3, 2, 1)
)
_SnFESX448Plus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX448Plus2XGPremRouter = _SnFESX448Plus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 2, 3, 2, 2)
)
_SnFESX424FiberFamily_ObjectIdentity = ObjectIdentity
snFESX424FiberFamily = _SnFESX424FiberFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3)
)
_SnFESX424FiberBaseFamily_ObjectIdentity = ObjectIdentity
snFESX424FiberBaseFamily = _SnFESX424FiberBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 1)
)
_SnFESX424Fiber_ObjectIdentity = ObjectIdentity
snFESX424Fiber = _SnFESX424Fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 1, 1)
)
_SnFESX424FiberSwitch_ObjectIdentity = ObjectIdentity
snFESX424FiberSwitch = _SnFESX424FiberSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 1, 1, 1)
)
_SnFESX424FiberRouter_ObjectIdentity = ObjectIdentity
snFESX424FiberRouter = _SnFESX424FiberRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 1, 1, 2)
)
_SnFESX424FiberPrem_ObjectIdentity = ObjectIdentity
snFESX424FiberPrem = _SnFESX424FiberPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 1, 2)
)
_SnFESX424FiberPremSwitch_ObjectIdentity = ObjectIdentity
snFESX424FiberPremSwitch = _SnFESX424FiberPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 1, 2, 1)
)
_SnFESX424FiberPremRouter_ObjectIdentity = ObjectIdentity
snFESX424FiberPremRouter = _SnFESX424FiberPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 1, 2, 2)
)
_SnFESX424FiberPlus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus1XGFamily = _SnFESX424FiberPlus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 2)
)
_SnFESX424FiberPlus1XG_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus1XG = _SnFESX424FiberPlus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 2, 1)
)
_SnFESX424FiberPlus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus1XGSwitch = _SnFESX424FiberPlus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 2, 1, 1)
)
_SnFESX424FiberPlus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus1XGRouter = _SnFESX424FiberPlus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 2, 1, 2)
)
_SnFESX424FiberPlus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus1XGPrem = _SnFESX424FiberPlus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 2, 2)
)
_SnFESX424FiberPlus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus1XGPremSwitch = _SnFESX424FiberPlus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 2, 2, 1)
)
_SnFESX424FiberPlus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus1XGPremRouter = _SnFESX424FiberPlus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 2, 2, 2)
)
_SnFESX424FiberPlus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus2XGFamily = _SnFESX424FiberPlus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 3)
)
_SnFESX424FiberPlus2XG_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus2XG = _SnFESX424FiberPlus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 3, 1)
)
_SnFESX424FiberPlus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus2XGSwitch = _SnFESX424FiberPlus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 3, 1, 1)
)
_SnFESX424FiberPlus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus2XGRouter = _SnFESX424FiberPlus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 3, 1, 2)
)
_SnFESX424FiberPlus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus2XGPrem = _SnFESX424FiberPlus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 3, 2)
)
_SnFESX424FiberPlus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus2XGPremSwitch = _SnFESX424FiberPlus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 3, 2, 1)
)
_SnFESX424FiberPlus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX424FiberPlus2XGPremRouter = _SnFESX424FiberPlus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 3, 3, 2, 2)
)
_SnFESX448FiberFamily_ObjectIdentity = ObjectIdentity
snFESX448FiberFamily = _SnFESX448FiberFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4)
)
_SnFESX448FiberBaseFamily_ObjectIdentity = ObjectIdentity
snFESX448FiberBaseFamily = _SnFESX448FiberBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 1)
)
_SnFESX448Fiber_ObjectIdentity = ObjectIdentity
snFESX448Fiber = _SnFESX448Fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 1, 1)
)
_SnFESX448FiberSwitch_ObjectIdentity = ObjectIdentity
snFESX448FiberSwitch = _SnFESX448FiberSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 1, 1, 1)
)
_SnFESX448FiberRouter_ObjectIdentity = ObjectIdentity
snFESX448FiberRouter = _SnFESX448FiberRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 1, 1, 2)
)
_SnFESX448FiberPrem_ObjectIdentity = ObjectIdentity
snFESX448FiberPrem = _SnFESX448FiberPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 1, 2)
)
_SnFESX448FiberPremSwitch_ObjectIdentity = ObjectIdentity
snFESX448FiberPremSwitch = _SnFESX448FiberPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 1, 2, 1)
)
_SnFESX448FiberPremRouter_ObjectIdentity = ObjectIdentity
snFESX448FiberPremRouter = _SnFESX448FiberPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 1, 2, 2)
)
_SnFESX448FiberPlus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus1XGFamily = _SnFESX448FiberPlus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 2)
)
_SnFESX448FiberPlus1XG_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus1XG = _SnFESX448FiberPlus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 2, 1)
)
_SnFESX448FiberPlus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus1XGSwitch = _SnFESX448FiberPlus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 2, 1, 1)
)
_SnFESX448FiberPlus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus1XGRouter = _SnFESX448FiberPlus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 2, 1, 2)
)
_SnFESX448FiberPlus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus1XGPrem = _SnFESX448FiberPlus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 2, 2)
)
_SnFESX448FiberPlus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus1XGPremSwitch = _SnFESX448FiberPlus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 2, 2, 1)
)
_SnFESX448FiberPlus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus1XGPremRouter = _SnFESX448FiberPlus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 2, 2, 2)
)
_SnFESX448FiberPlus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus2XGFamily = _SnFESX448FiberPlus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 3)
)
_SnFESX448FiberPlus2XG_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus2XG = _SnFESX448FiberPlus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 3, 1)
)
_SnFESX448FiberPlus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus2XGSwitch = _SnFESX448FiberPlus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 3, 1, 1)
)
_SnFESX448FiberPlus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus2XGRouter = _SnFESX448FiberPlus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 3, 1, 2)
)
_SnFESX448FiberPlus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus2XGPrem = _SnFESX448FiberPlus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 3, 2)
)
_SnFESX448FiberPlus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus2XGPremSwitch = _SnFESX448FiberPlus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 3, 2, 1)
)
_SnFESX448FiberPlus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX448FiberPlus2XGPremRouter = _SnFESX448FiberPlus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 4, 3, 2, 2)
)
_SnFESX424POEFamily_ObjectIdentity = ObjectIdentity
snFESX424POEFamily = _SnFESX424POEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5)
)
_SnFESX424POEBaseFamily_ObjectIdentity = ObjectIdentity
snFESX424POEBaseFamily = _SnFESX424POEBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 1)
)
_SnFESX424POE_ObjectIdentity = ObjectIdentity
snFESX424POE = _SnFESX424POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 1, 1)
)
_SnFESX424POESwitch_ObjectIdentity = ObjectIdentity
snFESX424POESwitch = _SnFESX424POESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 1, 1, 1)
)
_SnFESX424POERouter_ObjectIdentity = ObjectIdentity
snFESX424POERouter = _SnFESX424POERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 1, 1, 2)
)
_SnFESX424POEPrem_ObjectIdentity = ObjectIdentity
snFESX424POEPrem = _SnFESX424POEPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 1, 2)
)
_SnFESX424POEPremSwitch_ObjectIdentity = ObjectIdentity
snFESX424POEPremSwitch = _SnFESX424POEPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 1, 2, 1)
)
_SnFESX424POEPremRouter_ObjectIdentity = ObjectIdentity
snFESX424POEPremRouter = _SnFESX424POEPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 1, 2, 2)
)
_SnFESX424POEPlus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX424POEPlus1XGFamily = _SnFESX424POEPlus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 2)
)
_SnFESX424POEPlus1XG_ObjectIdentity = ObjectIdentity
snFESX424POEPlus1XG = _SnFESX424POEPlus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 2, 1)
)
_SnFESX424POEPlus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX424POEPlus1XGSwitch = _SnFESX424POEPlus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 2, 1, 1)
)
_SnFESX424POEPlus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX424POEPlus1XGRouter = _SnFESX424POEPlus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 2, 1, 2)
)
_SnFESX424POEPlus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX424POEPlus1XGPrem = _SnFESX424POEPlus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 2, 2)
)
_SnFESX424POEPlus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX424POEPlus1XGPremSwitch = _SnFESX424POEPlus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 2, 2, 1)
)
_SnFESX424POEPlus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX424POEPlus1XGPremRouter = _SnFESX424POEPlus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 2, 2, 2)
)
_SnFESX424POEPlus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX424POEPlus2XGFamily = _SnFESX424POEPlus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 3)
)
_SnFESX424POEPlus2XG_ObjectIdentity = ObjectIdentity
snFESX424POEPlus2XG = _SnFESX424POEPlus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 3, 1)
)
_SnFESX424POEPlus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX424POEPlus2XGSwitch = _SnFESX424POEPlus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 3, 1, 1)
)
_SnFESX424POEPlus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX424POEPlus2XGRouter = _SnFESX424POEPlus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 3, 1, 2)
)
_SnFESX424POEPlus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX424POEPlus2XGPrem = _SnFESX424POEPlus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 3, 2)
)
_SnFESX424POEPlus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX424POEPlus2XGPremSwitch = _SnFESX424POEPlus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 3, 2, 1)
)
_SnFESX424POEPlus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX424POEPlus2XGPremRouter = _SnFESX424POEPlus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 5, 3, 2, 2)
)
_SnFESX624Family_ObjectIdentity = ObjectIdentity
snFESX624Family = _SnFESX624Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6)
)
_SnFESX624BaseFamily_ObjectIdentity = ObjectIdentity
snFESX624BaseFamily = _SnFESX624BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 1)
)
_SnFESX624_ObjectIdentity = ObjectIdentity
snFESX624 = _SnFESX624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 1, 1)
)
_SnFESX624Switch_ObjectIdentity = ObjectIdentity
snFESX624Switch = _SnFESX624Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 1, 1, 1)
)
_SnFESX624Router_ObjectIdentity = ObjectIdentity
snFESX624Router = _SnFESX624Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 1, 1, 2)
)
_SnFESX624Prem_ObjectIdentity = ObjectIdentity
snFESX624Prem = _SnFESX624Prem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 1, 2)
)
_SnFESX624PremSwitch_ObjectIdentity = ObjectIdentity
snFESX624PremSwitch = _SnFESX624PremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 1, 2, 1)
)
_SnFESX624PremRouter_ObjectIdentity = ObjectIdentity
snFESX624PremRouter = _SnFESX624PremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 1, 2, 2)
)
_SnFESX624Prem6Router_ObjectIdentity = ObjectIdentity
snFESX624Prem6Router = _SnFESX624Prem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 1, 2, 3)
)
_SnFESX624Plus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX624Plus1XGFamily = _SnFESX624Plus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 2)
)
_SnFESX624Plus1XG_ObjectIdentity = ObjectIdentity
snFESX624Plus1XG = _SnFESX624Plus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 2, 1)
)
_SnFESX624Plus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX624Plus1XGSwitch = _SnFESX624Plus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 2, 1, 1)
)
_SnFESX624Plus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX624Plus1XGRouter = _SnFESX624Plus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 2, 1, 2)
)
_SnFESX624Plus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX624Plus1XGPrem = _SnFESX624Plus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 2, 2)
)
_SnFESX624Plus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624Plus1XGPremSwitch = _SnFESX624Plus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 2, 2, 1)
)
_SnFESX624Plus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX624Plus1XGPremRouter = _SnFESX624Plus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 2, 2, 2)
)
_SnFESX624Plus1XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624Plus1XGPrem6Router = _SnFESX624Plus1XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 2, 2, 3)
)
_SnFESX624Plus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX624Plus2XGFamily = _SnFESX624Plus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 3)
)
_SnFESX624Plus2XG_ObjectIdentity = ObjectIdentity
snFESX624Plus2XG = _SnFESX624Plus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 3, 1)
)
_SnFESX624Plus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX624Plus2XGSwitch = _SnFESX624Plus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 3, 1, 1)
)
_SnFESX624Plus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX624Plus2XGRouter = _SnFESX624Plus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 3, 1, 2)
)
_SnFESX624Plus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX624Plus2XGPrem = _SnFESX624Plus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 3, 2)
)
_SnFESX624Plus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624Plus2XGPremSwitch = _SnFESX624Plus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 3, 2, 1)
)
_SnFESX624Plus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX624Plus2XGPremRouter = _SnFESX624Plus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 3, 2, 2)
)
_SnFESX624Plus2XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624Plus2XGPrem6Router = _SnFESX624Plus2XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 6, 3, 2, 3)
)
_SnFESX648Family_ObjectIdentity = ObjectIdentity
snFESX648Family = _SnFESX648Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7)
)
_SnFESX648BaseFamily_ObjectIdentity = ObjectIdentity
snFESX648BaseFamily = _SnFESX648BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 1)
)
_SnFESX648_ObjectIdentity = ObjectIdentity
snFESX648 = _SnFESX648_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 1, 1)
)
_SnFESX648Switch_ObjectIdentity = ObjectIdentity
snFESX648Switch = _SnFESX648Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 1, 1, 1)
)
_SnFESX648Router_ObjectIdentity = ObjectIdentity
snFESX648Router = _SnFESX648Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 1, 1, 2)
)
_SnFESX648Prem_ObjectIdentity = ObjectIdentity
snFESX648Prem = _SnFESX648Prem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 1, 2)
)
_SnFESX648PremSwitch_ObjectIdentity = ObjectIdentity
snFESX648PremSwitch = _SnFESX648PremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 1, 2, 1)
)
_SnFESX648PremRouter_ObjectIdentity = ObjectIdentity
snFESX648PremRouter = _SnFESX648PremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 1, 2, 2)
)
_SnFESX648Prem6Router_ObjectIdentity = ObjectIdentity
snFESX648Prem6Router = _SnFESX648Prem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 1, 2, 3)
)
_SnFESX648Plus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX648Plus1XGFamily = _SnFESX648Plus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 2)
)
_SnFESX648Plus1XG_ObjectIdentity = ObjectIdentity
snFESX648Plus1XG = _SnFESX648Plus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 2, 1)
)
_SnFESX648Plus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX648Plus1XGSwitch = _SnFESX648Plus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 2, 1, 1)
)
_SnFESX648Plus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX648Plus1XGRouter = _SnFESX648Plus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 2, 1, 2)
)
_SnFESX648Plus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX648Plus1XGPrem = _SnFESX648Plus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 2, 2)
)
_SnFESX648Plus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX648Plus1XGPremSwitch = _SnFESX648Plus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 2, 2, 1)
)
_SnFESX648Plus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX648Plus1XGPremRouter = _SnFESX648Plus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 2, 2, 2)
)
_SnFESX648Plus1XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX648Plus1XGPrem6Router = _SnFESX648Plus1XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 2, 2, 3)
)
_SnFESX648Plus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX648Plus2XGFamily = _SnFESX648Plus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 3)
)
_SnFESX648Plus2XG_ObjectIdentity = ObjectIdentity
snFESX648Plus2XG = _SnFESX648Plus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 3, 1)
)
_SnFESX648Plus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX648Plus2XGSwitch = _SnFESX648Plus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 3, 1, 1)
)
_SnFESX648Plus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX648Plus2XGRouter = _SnFESX648Plus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 3, 1, 2)
)
_SnFESX648Plus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX648Plus2XGPrem = _SnFESX648Plus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 3, 2)
)
_SnFESX648Plus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX648Plus2XGPremSwitch = _SnFESX648Plus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 3, 2, 1)
)
_SnFESX648Plus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX648Plus2XGPremRouter = _SnFESX648Plus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 3, 2, 2)
)
_SnFESX648Plus2XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX648Plus2XGPrem6Router = _SnFESX648Plus2XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 7, 3, 2, 3)
)
_SnFESX624FiberFamily_ObjectIdentity = ObjectIdentity
snFESX624FiberFamily = _SnFESX624FiberFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8)
)
_SnFESX624FiberBaseFamily_ObjectIdentity = ObjectIdentity
snFESX624FiberBaseFamily = _SnFESX624FiberBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 1)
)
_SnFESX624Fiber_ObjectIdentity = ObjectIdentity
snFESX624Fiber = _SnFESX624Fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 1, 1)
)
_SnFESX624FiberSwitch_ObjectIdentity = ObjectIdentity
snFESX624FiberSwitch = _SnFESX624FiberSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 1, 1, 1)
)
_SnFESX624FiberRouter_ObjectIdentity = ObjectIdentity
snFESX624FiberRouter = _SnFESX624FiberRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 1, 1, 2)
)
_SnFESX624FiberPrem_ObjectIdentity = ObjectIdentity
snFESX624FiberPrem = _SnFESX624FiberPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 1, 2)
)
_SnFESX624FiberPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624FiberPremSwitch = _SnFESX624FiberPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 1, 2, 1)
)
_SnFESX624FiberPremRouter_ObjectIdentity = ObjectIdentity
snFESX624FiberPremRouter = _SnFESX624FiberPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 1, 2, 2)
)
_SnFESX624FiberPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624FiberPrem6Router = _SnFESX624FiberPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 1, 2, 3)
)
_SnFESX624FiberPlus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus1XGFamily = _SnFESX624FiberPlus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 2)
)
_SnFESX624FiberPlus1XG_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus1XG = _SnFESX624FiberPlus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 2, 1)
)
_SnFESX624FiberPlus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus1XGSwitch = _SnFESX624FiberPlus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 2, 1, 1)
)
_SnFESX624FiberPlus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus1XGRouter = _SnFESX624FiberPlus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 2, 1, 2)
)
_SnFESX624FiberPlus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus1XGPrem = _SnFESX624FiberPlus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 2, 2)
)
_SnFESX624FiberPlus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus1XGPremSwitch = _SnFESX624FiberPlus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 2, 2, 1)
)
_SnFESX624FiberPlus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus1XGPremRouter = _SnFESX624FiberPlus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 2, 2, 2)
)
_SnFESX624FiberPlus1XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus1XGPrem6Router = _SnFESX624FiberPlus1XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 2, 2, 3)
)
_SnFESX624FiberPlus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus2XGFamily = _SnFESX624FiberPlus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 3)
)
_SnFESX624FiberPlus2XG_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus2XG = _SnFESX624FiberPlus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 3, 1)
)
_SnFESX624FiberPlus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus2XGSwitch = _SnFESX624FiberPlus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 3, 1, 1)
)
_SnFESX624FiberPlus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus2XGRouter = _SnFESX624FiberPlus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 3, 1, 2)
)
_SnFESX624FiberPlus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus2XGPrem = _SnFESX624FiberPlus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 3, 2)
)
_SnFESX624FiberPlus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus2XGPremSwitch = _SnFESX624FiberPlus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 3, 2, 1)
)
_SnFESX624FiberPlus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus2XGPremRouter = _SnFESX624FiberPlus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 3, 2, 2)
)
_SnFESX624FiberPlus2XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624FiberPlus2XGPrem6Router = _SnFESX624FiberPlus2XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 8, 3, 2, 3)
)
_SnFESX648FiberFamily_ObjectIdentity = ObjectIdentity
snFESX648FiberFamily = _SnFESX648FiberFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9)
)
_SnFESX648FiberBaseFamily_ObjectIdentity = ObjectIdentity
snFESX648FiberBaseFamily = _SnFESX648FiberBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 1)
)
_SnFESX648Fiber_ObjectIdentity = ObjectIdentity
snFESX648Fiber = _SnFESX648Fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 1, 1)
)
_SnFESX648FiberSwitch_ObjectIdentity = ObjectIdentity
snFESX648FiberSwitch = _SnFESX648FiberSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 1, 1, 1)
)
_SnFESX648FiberRouter_ObjectIdentity = ObjectIdentity
snFESX648FiberRouter = _SnFESX648FiberRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 1, 1, 2)
)
_SnFESX648FiberPrem_ObjectIdentity = ObjectIdentity
snFESX648FiberPrem = _SnFESX648FiberPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 1, 2)
)
_SnFESX648FiberPremSwitch_ObjectIdentity = ObjectIdentity
snFESX648FiberPremSwitch = _SnFESX648FiberPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 1, 2, 1)
)
_SnFESX648FiberPremRouter_ObjectIdentity = ObjectIdentity
snFESX648FiberPremRouter = _SnFESX648FiberPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 1, 2, 2)
)
_SnFESX648FiberPrem6Router_ObjectIdentity = ObjectIdentity
snFESX648FiberPrem6Router = _SnFESX648FiberPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 1, 2, 3)
)
_SnFESX648FiberPlus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus1XGFamily = _SnFESX648FiberPlus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 2)
)
_SnFESX648FiberPlus1XG_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus1XG = _SnFESX648FiberPlus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 2, 1)
)
_SnFESX648FiberPlus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus1XGSwitch = _SnFESX648FiberPlus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 2, 1, 1)
)
_SnFESX648FiberPlus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus1XGRouter = _SnFESX648FiberPlus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 2, 1, 2)
)
_SnFESX648FiberPlus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus1XGPrem = _SnFESX648FiberPlus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 2, 2)
)
_SnFESX648FiberPlus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus1XGPremSwitch = _SnFESX648FiberPlus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 2, 2, 1)
)
_SnFESX648FiberPlus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus1XGPremRouter = _SnFESX648FiberPlus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 2, 2, 2)
)
_SnFESX648FiberPlus1XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus1XGPrem6Router = _SnFESX648FiberPlus1XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 2, 2, 3)
)
_SnFESX648FiberPlus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus2XGFamily = _SnFESX648FiberPlus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 3)
)
_SnFESX648FiberPlus2XG_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus2XG = _SnFESX648FiberPlus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 3, 1)
)
_SnFESX648FiberPlus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus2XGSwitch = _SnFESX648FiberPlus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 3, 1, 1)
)
_SnFESX648FiberPlus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus2XGRouter = _SnFESX648FiberPlus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 3, 1, 2)
)
_SnFESX648FiberPlus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus2XGPrem = _SnFESX648FiberPlus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 3, 2)
)
_SnFESX648FiberPlus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus2XGPremSwitch = _SnFESX648FiberPlus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 3, 2, 1)
)
_SnFESX648FiberPlus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus2XGPremRouter = _SnFESX648FiberPlus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 3, 2, 2)
)
_SnFESX648FiberPlus2XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX648FiberPlus2XGPrem6Router = _SnFESX648FiberPlus2XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 9, 3, 2, 3)
)
_SnFESX624POEFamily_ObjectIdentity = ObjectIdentity
snFESX624POEFamily = _SnFESX624POEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10)
)
_SnFESX624POEBaseFamily_ObjectIdentity = ObjectIdentity
snFESX624POEBaseFamily = _SnFESX624POEBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 1)
)
_SnFESX624POE_ObjectIdentity = ObjectIdentity
snFESX624POE = _SnFESX624POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 1, 1)
)
_SnFESX624POESwitch_ObjectIdentity = ObjectIdentity
snFESX624POESwitch = _SnFESX624POESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 1, 1, 1)
)
_SnFESX624POERouter_ObjectIdentity = ObjectIdentity
snFESX624POERouter = _SnFESX624POERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 1, 1, 2)
)
_SnFESX624POEPrem_ObjectIdentity = ObjectIdentity
snFESX624POEPrem = _SnFESX624POEPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 1, 2)
)
_SnFESX624POEPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624POEPremSwitch = _SnFESX624POEPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 1, 2, 1)
)
_SnFESX624POEPremRouter_ObjectIdentity = ObjectIdentity
snFESX624POEPremRouter = _SnFESX624POEPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 1, 2, 2)
)
_SnFESX624POEPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624POEPrem6Router = _SnFESX624POEPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 1, 2, 3)
)
_SnFESX624POEPlus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX624POEPlus1XGFamily = _SnFESX624POEPlus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 2)
)
_SnFESX624POEPlus1XG_ObjectIdentity = ObjectIdentity
snFESX624POEPlus1XG = _SnFESX624POEPlus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 2, 1)
)
_SnFESX624POEPlus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX624POEPlus1XGSwitch = _SnFESX624POEPlus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 2, 1, 1)
)
_SnFESX624POEPlus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX624POEPlus1XGRouter = _SnFESX624POEPlus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 2, 1, 2)
)
_SnFESX624POEPlus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX624POEPlus1XGPrem = _SnFESX624POEPlus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 2, 2)
)
_SnFESX624POEPlus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624POEPlus1XGPremSwitch = _SnFESX624POEPlus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 2, 2, 1)
)
_SnFESX624POEPlus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX624POEPlus1XGPremRouter = _SnFESX624POEPlus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 2, 2, 2)
)
_SnFESX624POEPlus1XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624POEPlus1XGPrem6Router = _SnFESX624POEPlus1XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 2, 2, 3)
)
_SnFESX624POEPlus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX624POEPlus2XGFamily = _SnFESX624POEPlus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 3)
)
_SnFESX624POEPlus2XG_ObjectIdentity = ObjectIdentity
snFESX624POEPlus2XG = _SnFESX624POEPlus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 3, 1)
)
_SnFESX624POEPlus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX624POEPlus2XGSwitch = _SnFESX624POEPlus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 3, 1, 1)
)
_SnFESX624POEPlus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX624POEPlus2XGRouter = _SnFESX624POEPlus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 3, 1, 2)
)
_SnFESX624POEPlus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX624POEPlus2XGPrem = _SnFESX624POEPlus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 3, 2)
)
_SnFESX624POEPlus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624POEPlus2XGPremSwitch = _SnFESX624POEPlus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 3, 2, 1)
)
_SnFESX624POEPlus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX624POEPlus2XGPremRouter = _SnFESX624POEPlus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 3, 2, 2)
)
_SnFESX624POEPlus2XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624POEPlus2XGPrem6Router = _SnFESX624POEPlus2XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 10, 3, 2, 3)
)
_SnFESX624EFamily_ObjectIdentity = ObjectIdentity
snFESX624EFamily = _SnFESX624EFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11)
)
_SnFESX624EBaseFamily_ObjectIdentity = ObjectIdentity
snFESX624EBaseFamily = _SnFESX624EBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 1)
)
_SnFESX624E_ObjectIdentity = ObjectIdentity
snFESX624E = _SnFESX624E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 1, 1)
)
_SnFESX624ESwitch_ObjectIdentity = ObjectIdentity
snFESX624ESwitch = _SnFESX624ESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 1, 1, 1)
)
_SnFESX624ERouter_ObjectIdentity = ObjectIdentity
snFESX624ERouter = _SnFESX624ERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 1, 1, 2)
)
_SnFESX624EPrem_ObjectIdentity = ObjectIdentity
snFESX624EPrem = _SnFESX624EPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 1, 2)
)
_SnFESX624EPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624EPremSwitch = _SnFESX624EPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 1, 2, 1)
)
_SnFESX624EPremRouter_ObjectIdentity = ObjectIdentity
snFESX624EPremRouter = _SnFESX624EPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 1, 2, 2)
)
_SnFESX624EPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624EPrem6Router = _SnFESX624EPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 1, 2, 3)
)
_SnFESX624EPlus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX624EPlus1XGFamily = _SnFESX624EPlus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 2)
)
_SnFESX624EPlus1XG_ObjectIdentity = ObjectIdentity
snFESX624EPlus1XG = _SnFESX624EPlus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 2, 1)
)
_SnFESX624EPlus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX624EPlus1XGSwitch = _SnFESX624EPlus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 2, 1, 1)
)
_SnFESX624EPlus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX624EPlus1XGRouter = _SnFESX624EPlus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 2, 1, 2)
)
_SnFESX624EPlus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX624EPlus1XGPrem = _SnFESX624EPlus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 2, 2)
)
_SnFESX624EPlus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624EPlus1XGPremSwitch = _SnFESX624EPlus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 2, 2, 1)
)
_SnFESX624EPlus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX624EPlus1XGPremRouter = _SnFESX624EPlus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 2, 2, 2)
)
_SnFESX624EPlus1XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624EPlus1XGPrem6Router = _SnFESX624EPlus1XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 2, 2, 3)
)
_SnFESX624EPlus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX624EPlus2XGFamily = _SnFESX624EPlus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 3)
)
_SnFESX624EPlus2XG_ObjectIdentity = ObjectIdentity
snFESX624EPlus2XG = _SnFESX624EPlus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 3, 1)
)
_SnFESX624EPlus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX624EPlus2XGSwitch = _SnFESX624EPlus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 3, 1, 1)
)
_SnFESX624EPlus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX624EPlus2XGRouter = _SnFESX624EPlus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 3, 1, 2)
)
_SnFESX624EPlus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX624EPlus2XGPrem = _SnFESX624EPlus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 3, 2)
)
_SnFESX624EPlus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624EPlus2XGPremSwitch = _SnFESX624EPlus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 3, 2, 1)
)
_SnFESX624EPlus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX624EPlus2XGPremRouter = _SnFESX624EPlus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 3, 2, 2)
)
_SnFESX624EPlus2XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624EPlus2XGPrem6Router = _SnFESX624EPlus2XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 11, 3, 2, 3)
)
_SnFESX624EFiberFamily_ObjectIdentity = ObjectIdentity
snFESX624EFiberFamily = _SnFESX624EFiberFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12)
)
_SnFESX624EFiberBaseFamily_ObjectIdentity = ObjectIdentity
snFESX624EFiberBaseFamily = _SnFESX624EFiberBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 1)
)
_SnFESX624EFiber_ObjectIdentity = ObjectIdentity
snFESX624EFiber = _SnFESX624EFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 1, 1)
)
_SnFESX624EFiberSwitch_ObjectIdentity = ObjectIdentity
snFESX624EFiberSwitch = _SnFESX624EFiberSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 1, 1, 1)
)
_SnFESX624EFiberRouter_ObjectIdentity = ObjectIdentity
snFESX624EFiberRouter = _SnFESX624EFiberRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 1, 1, 2)
)
_SnFESX624EFiberPrem_ObjectIdentity = ObjectIdentity
snFESX624EFiberPrem = _SnFESX624EFiberPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 1, 2)
)
_SnFESX624EFiberPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624EFiberPremSwitch = _SnFESX624EFiberPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 1, 2, 1)
)
_SnFESX624EFiberPremRouter_ObjectIdentity = ObjectIdentity
snFESX624EFiberPremRouter = _SnFESX624EFiberPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 1, 2, 2)
)
_SnFESX624EFiberPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624EFiberPrem6Router = _SnFESX624EFiberPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 1, 2, 3)
)
_SnFESX624EFiberPlus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus1XGFamily = _SnFESX624EFiberPlus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 2)
)
_SnFESX624EFiberPlus1XG_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus1XG = _SnFESX624EFiberPlus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 2, 1)
)
_SnFESX624EFiberPlus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus1XGSwitch = _SnFESX624EFiberPlus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 2, 1, 1)
)
_SnFESX624EFiberPlus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus1XGRouter = _SnFESX624EFiberPlus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 2, 1, 2)
)
_SnFESX624EFiberPlus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus1XGPrem = _SnFESX624EFiberPlus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 2, 2)
)
_SnFESX624EFiberPlus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus1XGPremSwitch = _SnFESX624EFiberPlus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 2, 2, 1)
)
_SnFESX624EFiberPlus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus1XGPremRouter = _SnFESX624EFiberPlus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 2, 2, 2)
)
_SnFESX624EFiberPlus1XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus1XGPrem6Router = _SnFESX624EFiberPlus1XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 2, 2, 3)
)
_SnFESX624EFiberPlus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus2XGFamily = _SnFESX624EFiberPlus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 3)
)
_SnFESX624EFiberPlus2XG_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus2XG = _SnFESX624EFiberPlus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 3, 1)
)
_SnFESX624EFiberPlus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus2XGSwitch = _SnFESX624EFiberPlus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 3, 1, 1)
)
_SnFESX624EFiberPlus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus2XGRouter = _SnFESX624EFiberPlus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 3, 1, 2)
)
_SnFESX624EFiberPlus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus2XGPrem = _SnFESX624EFiberPlus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 3, 2)
)
_SnFESX624EFiberPlus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus2XGPremSwitch = _SnFESX624EFiberPlus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 3, 2, 1)
)
_SnFESX624EFiberPlus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus2XGPremRouter = _SnFESX624EFiberPlus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 3, 2, 2)
)
_SnFESX624EFiberPlus2XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX624EFiberPlus2XGPrem6Router = _SnFESX624EFiberPlus2XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 12, 3, 2, 3)
)
_SnFESX648EFamily_ObjectIdentity = ObjectIdentity
snFESX648EFamily = _SnFESX648EFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13)
)
_SnFESX648EBaseFamily_ObjectIdentity = ObjectIdentity
snFESX648EBaseFamily = _SnFESX648EBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 1)
)
_SnFESX648E_ObjectIdentity = ObjectIdentity
snFESX648E = _SnFESX648E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 1, 1)
)
_SnFESX648ESwitch_ObjectIdentity = ObjectIdentity
snFESX648ESwitch = _SnFESX648ESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 1, 1, 1)
)
_SnFESX648ERouter_ObjectIdentity = ObjectIdentity
snFESX648ERouter = _SnFESX648ERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 1, 1, 2)
)
_SnFESX648EPrem_ObjectIdentity = ObjectIdentity
snFESX648EPrem = _SnFESX648EPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 1, 2)
)
_SnFESX648EPremSwitch_ObjectIdentity = ObjectIdentity
snFESX648EPremSwitch = _SnFESX648EPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 1, 2, 1)
)
_SnFESX648EPremRouter_ObjectIdentity = ObjectIdentity
snFESX648EPremRouter = _SnFESX648EPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 1, 2, 2)
)
_SnFESX648EPrem6Router_ObjectIdentity = ObjectIdentity
snFESX648EPrem6Router = _SnFESX648EPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 1, 2, 3)
)
_SnFESX648EPlus1XGFamily_ObjectIdentity = ObjectIdentity
snFESX648EPlus1XGFamily = _SnFESX648EPlus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 2)
)
_SnFESX648EPlus1XG_ObjectIdentity = ObjectIdentity
snFESX648EPlus1XG = _SnFESX648EPlus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 2, 1)
)
_SnFESX648EPlus1XGSwitch_ObjectIdentity = ObjectIdentity
snFESX648EPlus1XGSwitch = _SnFESX648EPlus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 2, 1, 1)
)
_SnFESX648EPlus1XGRouter_ObjectIdentity = ObjectIdentity
snFESX648EPlus1XGRouter = _SnFESX648EPlus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 2, 1, 2)
)
_SnFESX648EPlus1XGPrem_ObjectIdentity = ObjectIdentity
snFESX648EPlus1XGPrem = _SnFESX648EPlus1XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 2, 2)
)
_SnFESX648EPlus1XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX648EPlus1XGPremSwitch = _SnFESX648EPlus1XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 2, 2, 1)
)
_SnFESX648EPlus1XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX648EPlus1XGPremRouter = _SnFESX648EPlus1XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 2, 2, 2)
)
_SnFESX648EPlus1XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX648EPlus1XGPrem6Router = _SnFESX648EPlus1XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 2, 2, 3)
)
_SnFESX648EPlus2XGFamily_ObjectIdentity = ObjectIdentity
snFESX648EPlus2XGFamily = _SnFESX648EPlus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 3)
)
_SnFESX648EPlus2XG_ObjectIdentity = ObjectIdentity
snFESX648EPlus2XG = _SnFESX648EPlus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 3, 1)
)
_SnFESX648EPlus2XGSwitch_ObjectIdentity = ObjectIdentity
snFESX648EPlus2XGSwitch = _SnFESX648EPlus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 3, 1, 1)
)
_SnFESX648EPlus2XGRouter_ObjectIdentity = ObjectIdentity
snFESX648EPlus2XGRouter = _SnFESX648EPlus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 3, 1, 2)
)
_SnFESX648EPlus2XGPrem_ObjectIdentity = ObjectIdentity
snFESX648EPlus2XGPrem = _SnFESX648EPlus2XGPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 3, 2)
)
_SnFESX648EPlus2XGPremSwitch_ObjectIdentity = ObjectIdentity
snFESX648EPlus2XGPremSwitch = _SnFESX648EPlus2XGPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 3, 2, 1)
)
_SnFESX648EPlus2XGPremRouter_ObjectIdentity = ObjectIdentity
snFESX648EPlus2XGPremRouter = _SnFESX648EPlus2XGPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 3, 2, 2)
)
_SnFESX648EPlus2XGPrem6Router_ObjectIdentity = ObjectIdentity
snFESX648EPlus2XGPrem6Router = _SnFESX648EPlus2XGPrem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 34, 13, 3, 2, 3)
)
_SnFWSXFamily_ObjectIdentity = ObjectIdentity
snFWSXFamily = _SnFWSXFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35)
)
_SnFWSX424Family_ObjectIdentity = ObjectIdentity
snFWSX424Family = _SnFWSX424Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1)
)
_SnFWSX424BaseFamily_ObjectIdentity = ObjectIdentity
snFWSX424BaseFamily = _SnFWSX424BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1, 1)
)
_SnFWSX424_ObjectIdentity = ObjectIdentity
snFWSX424 = _SnFWSX424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1, 1, 1)
)
_SnFWSX424Switch_ObjectIdentity = ObjectIdentity
snFWSX424Switch = _SnFWSX424Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1, 1, 1, 1)
)
_SnFWSX424Router_ObjectIdentity = ObjectIdentity
snFWSX424Router = _SnFWSX424Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1, 1, 1, 2)
)
_SnFWSX424Plus1XGFamily_ObjectIdentity = ObjectIdentity
snFWSX424Plus1XGFamily = _SnFWSX424Plus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1, 2)
)
_SnFWSX424Plus1XG_ObjectIdentity = ObjectIdentity
snFWSX424Plus1XG = _SnFWSX424Plus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1, 2, 1)
)
_SnFWSX424Plus1XGSwitch_ObjectIdentity = ObjectIdentity
snFWSX424Plus1XGSwitch = _SnFWSX424Plus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1, 2, 1, 1)
)
_SnFWSX424Plus1XGRouter_ObjectIdentity = ObjectIdentity
snFWSX424Plus1XGRouter = _SnFWSX424Plus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1, 2, 1, 2)
)
_SnFWSX424Plus2XGFamily_ObjectIdentity = ObjectIdentity
snFWSX424Plus2XGFamily = _SnFWSX424Plus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1, 3)
)
_SnFWSX424Plus2XG_ObjectIdentity = ObjectIdentity
snFWSX424Plus2XG = _SnFWSX424Plus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1, 3, 1)
)
_SnFWSX424Plus2XGSwitch_ObjectIdentity = ObjectIdentity
snFWSX424Plus2XGSwitch = _SnFWSX424Plus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1, 3, 1, 1)
)
_SnFWSX424Plus2XGRouter_ObjectIdentity = ObjectIdentity
snFWSX424Plus2XGRouter = _SnFWSX424Plus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 1, 3, 1, 2)
)
_SnFWSX448Family_ObjectIdentity = ObjectIdentity
snFWSX448Family = _SnFWSX448Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2)
)
_SnFWSX448BaseFamily_ObjectIdentity = ObjectIdentity
snFWSX448BaseFamily = _SnFWSX448BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2, 1)
)
_SnFWSX448_ObjectIdentity = ObjectIdentity
snFWSX448 = _SnFWSX448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2, 1, 1)
)
_SnFWSX448Switch_ObjectIdentity = ObjectIdentity
snFWSX448Switch = _SnFWSX448Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2, 1, 1, 1)
)
_SnFWSX448Router_ObjectIdentity = ObjectIdentity
snFWSX448Router = _SnFWSX448Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2, 1, 1, 2)
)
_SnFWSX448Plus1XGFamily_ObjectIdentity = ObjectIdentity
snFWSX448Plus1XGFamily = _SnFWSX448Plus1XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2, 2)
)
_SnFWSX448Plus1XG_ObjectIdentity = ObjectIdentity
snFWSX448Plus1XG = _SnFWSX448Plus1XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2, 2, 1)
)
_SnFWSX448Plus1XGSwitch_ObjectIdentity = ObjectIdentity
snFWSX448Plus1XGSwitch = _SnFWSX448Plus1XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2, 2, 1, 1)
)
_SnFWSX448Plus1XGRouter_ObjectIdentity = ObjectIdentity
snFWSX448Plus1XGRouter = _SnFWSX448Plus1XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2, 2, 1, 2)
)
_SnFWSX448Plus2XGFamily_ObjectIdentity = ObjectIdentity
snFWSX448Plus2XGFamily = _SnFWSX448Plus2XGFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2, 3)
)
_SnFWSX448Plus2XG_ObjectIdentity = ObjectIdentity
snFWSX448Plus2XG = _SnFWSX448Plus2XG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2, 3, 1)
)
_SnFWSX448Plus2XGSwitch_ObjectIdentity = ObjectIdentity
snFWSX448Plus2XGSwitch = _SnFWSX448Plus2XGSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2, 3, 1, 1)
)
_SnFWSX448Plus2XGRouter_ObjectIdentity = ObjectIdentity
snFWSX448Plus2XGRouter = _SnFWSX448Plus2XGRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 35, 2, 3, 1, 2)
)
_SnFastIronSuperXFamily_ObjectIdentity = ObjectIdentity
snFastIronSuperXFamily = _SnFastIronSuperXFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36)
)
_SnFastIronSuperX_ObjectIdentity = ObjectIdentity
snFastIronSuperX = _SnFastIronSuperX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 1)
)
_SnFastIronSuperXSwitch_ObjectIdentity = ObjectIdentity
snFastIronSuperXSwitch = _SnFastIronSuperXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 1, 1)
)
_SnFastIronSuperXRouter_ObjectIdentity = ObjectIdentity
snFastIronSuperXRouter = _SnFastIronSuperXRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 1, 2)
)
_SnFastIronSuperXBaseL3Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperXBaseL3Switch = _SnFastIronSuperXBaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 1, 3)
)
_SnFastIronSuperXPrem_ObjectIdentity = ObjectIdentity
snFastIronSuperXPrem = _SnFastIronSuperXPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 2)
)
_SnFastIronSuperXPremSwitch_ObjectIdentity = ObjectIdentity
snFastIronSuperXPremSwitch = _SnFastIronSuperXPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 2, 1)
)
_SnFastIronSuperXPremRouter_ObjectIdentity = ObjectIdentity
snFastIronSuperXPremRouter = _SnFastIronSuperXPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 2, 2)
)
_SnFastIronSuperXPremBaseL3Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperXPremBaseL3Switch = _SnFastIronSuperXPremBaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 2, 3)
)
_SnFastIronSuperX800_ObjectIdentity = ObjectIdentity
snFastIronSuperX800 = _SnFastIronSuperX800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 3)
)
_SnFastIronSuperX800Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperX800Switch = _SnFastIronSuperX800Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 3, 1)
)
_SnFastIronSuperX800Router_ObjectIdentity = ObjectIdentity
snFastIronSuperX800Router = _SnFastIronSuperX800Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 3, 2)
)
_SnFastIronSuperX800BaseL3Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperX800BaseL3Switch = _SnFastIronSuperX800BaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 3, 3)
)
_SnFastIronSuperX800Prem_ObjectIdentity = ObjectIdentity
snFastIronSuperX800Prem = _SnFastIronSuperX800Prem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 4)
)
_SnFastIronSuperX800PremSwitch_ObjectIdentity = ObjectIdentity
snFastIronSuperX800PremSwitch = _SnFastIronSuperX800PremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 4, 1)
)
_SnFastIronSuperX800PremRouter_ObjectIdentity = ObjectIdentity
snFastIronSuperX800PremRouter = _SnFastIronSuperX800PremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 4, 2)
)
_SnFastIronSuperX800PremBaseL3Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperX800PremBaseL3Switch = _SnFastIronSuperX800PremBaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 4, 3)
)
_SnFastIronSuperX1600_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600 = _SnFastIronSuperX1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 5)
)
_SnFastIronSuperX1600Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600Switch = _SnFastIronSuperX1600Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 5, 1)
)
_SnFastIronSuperX1600Router_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600Router = _SnFastIronSuperX1600Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 5, 2)
)
_SnFastIronSuperX1600BaseL3Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600BaseL3Switch = _SnFastIronSuperX1600BaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 5, 3)
)
_SnFastIronSuperX1600Prem_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600Prem = _SnFastIronSuperX1600Prem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 6)
)
_SnFastIronSuperX1600PremSwitch_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600PremSwitch = _SnFastIronSuperX1600PremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 6, 1)
)
_SnFastIronSuperX1600PremRouter_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600PremRouter = _SnFastIronSuperX1600PremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 6, 2)
)
_SnFastIronSuperX1600PremBaseL3Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600PremBaseL3Switch = _SnFastIronSuperX1600PremBaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 6, 3)
)
_SnFastIronSuperXV6_ObjectIdentity = ObjectIdentity
snFastIronSuperXV6 = _SnFastIronSuperXV6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 7)
)
_SnFastIronSuperXV6Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperXV6Switch = _SnFastIronSuperXV6Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 7, 1)
)
_SnFastIronSuperXV6Router_ObjectIdentity = ObjectIdentity
snFastIronSuperXV6Router = _SnFastIronSuperXV6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 7, 2)
)
_SnFastIronSuperXV6BaseL3Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperXV6BaseL3Switch = _SnFastIronSuperXV6BaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 7, 3)
)
_SnFastIronSuperXV6Prem_ObjectIdentity = ObjectIdentity
snFastIronSuperXV6Prem = _SnFastIronSuperXV6Prem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 8)
)
_SnFastIronSuperXV6PremSwitch_ObjectIdentity = ObjectIdentity
snFastIronSuperXV6PremSwitch = _SnFastIronSuperXV6PremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 8, 1)
)
_SnFastIronSuperXV6PremRouter_ObjectIdentity = ObjectIdentity
snFastIronSuperXV6PremRouter = _SnFastIronSuperXV6PremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 8, 2)
)
_SnFastIronSuperXV6PremBaseL3Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperXV6PremBaseL3Switch = _SnFastIronSuperXV6PremBaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 8, 3)
)
_SnFastIronSuperXV6Prem6Router_ObjectIdentity = ObjectIdentity
snFastIronSuperXV6Prem6Router = _SnFastIronSuperXV6Prem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 8, 4)
)
_SnFastIronSuperX800V6_ObjectIdentity = ObjectIdentity
snFastIronSuperX800V6 = _SnFastIronSuperX800V6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 9)
)
_SnFastIronSuperX800V6Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperX800V6Switch = _SnFastIronSuperX800V6Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 9, 1)
)
_SnFastIronSuperX800V6Router_ObjectIdentity = ObjectIdentity
snFastIronSuperX800V6Router = _SnFastIronSuperX800V6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 9, 2)
)
_SnFastIronSuperX800V6BaseL3Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperX800V6BaseL3Switch = _SnFastIronSuperX800V6BaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 9, 3)
)
_SnFastIronSuperX800V6Prem_ObjectIdentity = ObjectIdentity
snFastIronSuperX800V6Prem = _SnFastIronSuperX800V6Prem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 10)
)
_SnFastIronSuperX800V6PremSwitch_ObjectIdentity = ObjectIdentity
snFastIronSuperX800V6PremSwitch = _SnFastIronSuperX800V6PremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 10, 1)
)
_SnFastIronSuperX800V6PremRouter_ObjectIdentity = ObjectIdentity
snFastIronSuperX800V6PremRouter = _SnFastIronSuperX800V6PremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 10, 2)
)
_SnFastIronSuperX800V6PremBaseL3Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperX800V6PremBaseL3Switch = _SnFastIronSuperX800V6PremBaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 10, 3)
)
_SnFastIronSuperX800V6Prem6Router_ObjectIdentity = ObjectIdentity
snFastIronSuperX800V6Prem6Router = _SnFastIronSuperX800V6Prem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 10, 4)
)
_SnFastIronSuperX1600V6_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600V6 = _SnFastIronSuperX1600V6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 11)
)
_SnFastIronSuperX1600V6Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600V6Switch = _SnFastIronSuperX1600V6Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 11, 1)
)
_SnFastIronSuperX1600V6Router_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600V6Router = _SnFastIronSuperX1600V6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 11, 2)
)
_SnFastIronSuperX1600V6BaseL3Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600V6BaseL3Switch = _SnFastIronSuperX1600V6BaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 11, 3)
)
_SnFastIronSuperX1600V6Prem_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600V6Prem = _SnFastIronSuperX1600V6Prem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 12)
)
_SnFastIronSuperX1600V6PremSwitch_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600V6PremSwitch = _SnFastIronSuperX1600V6PremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 12, 1)
)
_SnFastIronSuperX1600V6PremRouter_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600V6PremRouter = _SnFastIronSuperX1600V6PremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 12, 2)
)
_SnFastIronSuperX1600V6PremBaseL3Switch_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600V6PremBaseL3Switch = _SnFastIronSuperX1600V6PremBaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 12, 3)
)
_SnFastIronSuperX1600V6Prem6Router_ObjectIdentity = ObjectIdentity
snFastIronSuperX1600V6Prem6Router = _SnFastIronSuperX1600V6Prem6Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 36, 12, 4)
)
_SnBigIronSuperXFamily_ObjectIdentity = ObjectIdentity
snBigIronSuperXFamily = _SnBigIronSuperXFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 37)
)
_SnBigIronSuperX_ObjectIdentity = ObjectIdentity
snBigIronSuperX = _SnBigIronSuperX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 37, 1)
)
_SnBigIronSuperXSwitch_ObjectIdentity = ObjectIdentity
snBigIronSuperXSwitch = _SnBigIronSuperXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 37, 1, 1)
)
_SnBigIronSuperXRouter_ObjectIdentity = ObjectIdentity
snBigIronSuperXRouter = _SnBigIronSuperXRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 37, 1, 2)
)
_SnBigIronSuperXBaseL3Switch_ObjectIdentity = ObjectIdentity
snBigIronSuperXBaseL3Switch = _SnBigIronSuperXBaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 37, 1, 3)
)
_SnTurboIronSuperXFamily_ObjectIdentity = ObjectIdentity
snTurboIronSuperXFamily = _SnTurboIronSuperXFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 38)
)
_SnTurboIronSuperX_ObjectIdentity = ObjectIdentity
snTurboIronSuperX = _SnTurboIronSuperX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 38, 1)
)
_SnTurboIronSuperXSwitch_ObjectIdentity = ObjectIdentity
snTurboIronSuperXSwitch = _SnTurboIronSuperXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 38, 1, 1)
)
_SnTurboIronSuperXRouter_ObjectIdentity = ObjectIdentity
snTurboIronSuperXRouter = _SnTurboIronSuperXRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 38, 1, 2)
)
_SnTurboIronSuperXBaseL3Switch_ObjectIdentity = ObjectIdentity
snTurboIronSuperXBaseL3Switch = _SnTurboIronSuperXBaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 38, 1, 3)
)
_SnTurboIronSuperXPrem_ObjectIdentity = ObjectIdentity
snTurboIronSuperXPrem = _SnTurboIronSuperXPrem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 38, 2)
)
_SnTurboIronSuperXPremSwitch_ObjectIdentity = ObjectIdentity
snTurboIronSuperXPremSwitch = _SnTurboIronSuperXPremSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 38, 2, 1)
)
_SnTurboIronSuperXPremRouter_ObjectIdentity = ObjectIdentity
snTurboIronSuperXPremRouter = _SnTurboIronSuperXPremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 38, 2, 2)
)
_SnTurboIronSuperXPremBaseL3Switch_ObjectIdentity = ObjectIdentity
snTurboIronSuperXPremBaseL3Switch = _SnTurboIronSuperXPremBaseL3Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 38, 2, 3)
)
_SnIMRFamily_ObjectIdentity = ObjectIdentity
snIMRFamily = _SnIMRFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 39)
)
_SnNetIronIMR_ObjectIdentity = ObjectIdentity
snNetIronIMR = _SnNetIronIMR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 39, 1)
)
_SnNIIMRRouter_ObjectIdentity = ObjectIdentity
snNIIMRRouter = _SnNIIMRRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 39, 1, 2)
)
_SnBigIronRXFamily_ObjectIdentity = ObjectIdentity
snBigIronRXFamily = _SnBigIronRXFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40)
)
_SnBigIronRX16_ObjectIdentity = ObjectIdentity
snBigIronRX16 = _SnBigIronRX16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40, 1)
)
_SnBIRX16Switch_ObjectIdentity = ObjectIdentity
snBIRX16Switch = _SnBIRX16Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40, 1, 1)
)
_SnBIRX16Router_ObjectIdentity = ObjectIdentity
snBIRX16Router = _SnBIRX16Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40, 1, 2)
)
_SnBigIronRX8_ObjectIdentity = ObjectIdentity
snBigIronRX8 = _SnBigIronRX8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40, 2)
)
_SnBIRX8Switch_ObjectIdentity = ObjectIdentity
snBIRX8Switch = _SnBIRX8Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40, 2, 1)
)
_SnBIRX8Router_ObjectIdentity = ObjectIdentity
snBIRX8Router = _SnBIRX8Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40, 2, 2)
)
_SnBigIronRX4_ObjectIdentity = ObjectIdentity
snBigIronRX4 = _SnBigIronRX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40, 3)
)
_SnBIRX4Switch_ObjectIdentity = ObjectIdentity
snBIRX4Switch = _SnBIRX4Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40, 3, 1)
)
_SnBIRX4Router_ObjectIdentity = ObjectIdentity
snBIRX4Router = _SnBIRX4Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40, 3, 2)
)
_SnBigIronRX32_ObjectIdentity = ObjectIdentity
snBigIronRX32 = _SnBigIronRX32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40, 4)
)
_SnBIRX32Switch_ObjectIdentity = ObjectIdentity
snBIRX32Switch = _SnBIRX32Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40, 4, 1)
)
_SnBIRX32Router_ObjectIdentity = ObjectIdentity
snBIRX32Router = _SnBIRX32Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 40, 4, 2)
)
_SnNetIronXMRFamily_ObjectIdentity = ObjectIdentity
snNetIronXMRFamily = _SnNetIronXMRFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 41)
)
_SnNetIronXMR16000_ObjectIdentity = ObjectIdentity
snNetIronXMR16000 = _SnNetIronXMR16000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 41, 1)
)
_SnNIXMR16000Router_ObjectIdentity = ObjectIdentity
snNIXMR16000Router = _SnNIXMR16000Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 41, 1, 2)
)
_SnNetIronXMR8000_ObjectIdentity = ObjectIdentity
snNetIronXMR8000 = _SnNetIronXMR8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 41, 2)
)
_SnNIXMR8000Router_ObjectIdentity = ObjectIdentity
snNIXMR8000Router = _SnNIXMR8000Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 41, 2, 2)
)
_SnNetIronXMR4000_ObjectIdentity = ObjectIdentity
snNetIronXMR4000 = _SnNetIronXMR4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 41, 3)
)
_SnNIXMR4000Router_ObjectIdentity = ObjectIdentity
snNIXMR4000Router = _SnNIXMR4000Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 41, 3, 2)
)
_SnNetIronXMR32000_ObjectIdentity = ObjectIdentity
snNetIronXMR32000 = _SnNetIronXMR32000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 41, 4)
)
_SnNIXMR32000Router_ObjectIdentity = ObjectIdentity
snNIXMR32000Router = _SnNIXMR32000Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 41, 4, 2)
)
_SnSecureIronFamily_ObjectIdentity = ObjectIdentity
snSecureIronFamily = _SnSecureIronFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42)
)
_SnSecureIronLSFamily_ObjectIdentity = ObjectIdentity
snSecureIronLSFamily = _SnSecureIronLSFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 9)
)
_SnSecureIronLS100_ObjectIdentity = ObjectIdentity
snSecureIronLS100 = _SnSecureIronLS100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 9, 1)
)
_SnSecureIronLS100Switch_ObjectIdentity = ObjectIdentity
snSecureIronLS100Switch = _SnSecureIronLS100Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 9, 1, 1)
)
_SnSecureIronLS100Router_ObjectIdentity = ObjectIdentity
snSecureIronLS100Router = _SnSecureIronLS100Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 9, 1, 2)
)
_SnSecureIronLS300_ObjectIdentity = ObjectIdentity
snSecureIronLS300 = _SnSecureIronLS300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 9, 2)
)
_SnSecureIronLS300Switch_ObjectIdentity = ObjectIdentity
snSecureIronLS300Switch = _SnSecureIronLS300Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 9, 2, 1)
)
_SnSecureIronLS300Router_ObjectIdentity = ObjectIdentity
snSecureIronLS300Router = _SnSecureIronLS300Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 9, 2, 2)
)
_SnSecureIronTMFamily_ObjectIdentity = ObjectIdentity
snSecureIronTMFamily = _SnSecureIronTMFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 10)
)
_SnSecureIronTM100_ObjectIdentity = ObjectIdentity
snSecureIronTM100 = _SnSecureIronTM100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 10, 1)
)
_SnSecureIronTM100Switch_ObjectIdentity = ObjectIdentity
snSecureIronTM100Switch = _SnSecureIronTM100Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 10, 1, 1)
)
_SnSecureIronTM100Router_ObjectIdentity = ObjectIdentity
snSecureIronTM100Router = _SnSecureIronTM100Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 10, 1, 2)
)
_SnSecureIronTM300_ObjectIdentity = ObjectIdentity
snSecureIronTM300 = _SnSecureIronTM300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 10, 2)
)
_SnSecureIronTM300Switch_ObjectIdentity = ObjectIdentity
snSecureIronTM300Switch = _SnSecureIronTM300Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 10, 2, 1)
)
_SnSecureIronTM300Router_ObjectIdentity = ObjectIdentity
snSecureIronTM300Router = _SnSecureIronTM300Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 42, 10, 2, 2)
)
_SnNetIronMLXFamily_ObjectIdentity = ObjectIdentity
snNetIronMLXFamily = _SnNetIronMLXFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 44)
)
_SnNetIronMLX16_ObjectIdentity = ObjectIdentity
snNetIronMLX16 = _SnNetIronMLX16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 44, 1)
)
_SnNetIronMLX16Router_ObjectIdentity = ObjectIdentity
snNetIronMLX16Router = _SnNetIronMLX16Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 44, 1, 2)
)
_SnNetIronMLX8_ObjectIdentity = ObjectIdentity
snNetIronMLX8 = _SnNetIronMLX8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 44, 2)
)
_SnNetIronMLX8Router_ObjectIdentity = ObjectIdentity
snNetIronMLX8Router = _SnNetIronMLX8Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 44, 2, 2)
)
_SnNetIronMLX4_ObjectIdentity = ObjectIdentity
snNetIronMLX4 = _SnNetIronMLX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 44, 3)
)
_SnNetIronMLX4Router_ObjectIdentity = ObjectIdentity
snNetIronMLX4Router = _SnNetIronMLX4Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 44, 3, 2)
)
_SnNetIronMLX32_ObjectIdentity = ObjectIdentity
snNetIronMLX32 = _SnNetIronMLX32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 44, 4)
)
_SnNetIronMLX32Router_ObjectIdentity = ObjectIdentity
snNetIronMLX32Router = _SnNetIronMLX32Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 44, 4, 2)
)
_SnFGSFamily_ObjectIdentity = ObjectIdentity
snFGSFamily = _SnFGSFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45)
)
_SnFGS624Family_ObjectIdentity = ObjectIdentity
snFGS624Family = _SnFGS624Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1)
)
_SnFGS624PBaseFamily_ObjectIdentity = ObjectIdentity
snFGS624PBaseFamily = _SnFGS624PBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 1)
)
_SnFGS624P_ObjectIdentity = ObjectIdentity
snFGS624P = _SnFGS624P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 1, 1)
)
_SnFGS624PSwitch_ObjectIdentity = ObjectIdentity
snFGS624PSwitch = _SnFGS624PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 1, 1, 1)
)
_SnFGS624PRouter_ObjectIdentity = ObjectIdentity
snFGS624PRouter = _SnFGS624PRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 1, 1, 2)
)
_SnFGS624XGPFamily_ObjectIdentity = ObjectIdentity
snFGS624XGPFamily = _SnFGS624XGPFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 2)
)
_SnFGS624XGP_ObjectIdentity = ObjectIdentity
snFGS624XGP = _SnFGS624XGP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 2, 1)
)
_SnFGS624XGPSwitch_ObjectIdentity = ObjectIdentity
snFGS624XGPSwitch = _SnFGS624XGPSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 2, 1, 1)
)
_SnFGS624XGPRouter_ObjectIdentity = ObjectIdentity
snFGS624XGPRouter = _SnFGS624XGPRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 2, 1, 2)
)
_SnFGS624PPOEFamily_ObjectIdentity = ObjectIdentity
snFGS624PPOEFamily = _SnFGS624PPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 3)
)
_SnFGS624PPOE_ObjectIdentity = ObjectIdentity
snFGS624PPOE = _SnFGS624PPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 3, 1)
)
_SnFGS624PPOESwitch_ObjectIdentity = ObjectIdentity
snFGS624PPOESwitch = _SnFGS624PPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 3, 1, 1)
)
_SnFGS624PPOERouter_ObjectIdentity = ObjectIdentity
snFGS624PPOERouter = _SnFGS624PPOERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 3, 1, 2)
)
_SnFGS624XGPPOEFamily_ObjectIdentity = ObjectIdentity
snFGS624XGPPOEFamily = _SnFGS624XGPPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 4)
)
_SnFGS624XGPPOE_ObjectIdentity = ObjectIdentity
snFGS624XGPPOE = _SnFGS624XGPPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 4, 1)
)
_SnFGS624XGPPOESwitch_ObjectIdentity = ObjectIdentity
snFGS624XGPPOESwitch = _SnFGS624XGPPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 4, 1, 1)
)
_SnFGS624XGPPOERouter_ObjectIdentity = ObjectIdentity
snFGS624XGPPOERouter = _SnFGS624XGPPOERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 1, 4, 1, 2)
)
_SnFGS648Family_ObjectIdentity = ObjectIdentity
snFGS648Family = _SnFGS648Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 2)
)
_SnFGS648PBaseFamily_ObjectIdentity = ObjectIdentity
snFGS648PBaseFamily = _SnFGS648PBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 2, 1)
)
_SnFGS648P_ObjectIdentity = ObjectIdentity
snFGS648P = _SnFGS648P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 2, 1, 1)
)
_SnFGS648PSwitch_ObjectIdentity = ObjectIdentity
snFGS648PSwitch = _SnFGS648PSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 2, 1, 1, 1)
)
_SnFGS648PRouter_ObjectIdentity = ObjectIdentity
snFGS648PRouter = _SnFGS648PRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 2, 1, 1, 2)
)
_SnFGS648PPOEFamily_ObjectIdentity = ObjectIdentity
snFGS648PPOEFamily = _SnFGS648PPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 2, 2)
)
_SnFGS648PPOE_ObjectIdentity = ObjectIdentity
snFGS648PPOE = _SnFGS648PPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 2, 2, 1)
)
_SnFGS648PPOESwitch_ObjectIdentity = ObjectIdentity
snFGS648PPOESwitch = _SnFGS648PPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 2, 2, 1, 1)
)
_SnFGS648PPOERouter_ObjectIdentity = ObjectIdentity
snFGS648PPOERouter = _SnFGS648PPOERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 45, 2, 2, 1, 2)
)
_SnFLSFamily_ObjectIdentity = ObjectIdentity
snFLSFamily = _SnFLSFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 46)
)
_SnFLS624Family_ObjectIdentity = ObjectIdentity
snFLS624Family = _SnFLS624Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 46, 1)
)
_SnFLS624BaseFamily_ObjectIdentity = ObjectIdentity
snFLS624BaseFamily = _SnFLS624BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 46, 1, 1)
)
_SnFLS624_ObjectIdentity = ObjectIdentity
snFLS624 = _SnFLS624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 46, 1, 1, 1)
)
_SnFLS624Switch_ObjectIdentity = ObjectIdentity
snFLS624Switch = _SnFLS624Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 46, 1, 1, 1, 1)
)
_SnFLS624Router_ObjectIdentity = ObjectIdentity
snFLS624Router = _SnFLS624Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 46, 1, 1, 1, 2)
)
_SnFLS648Family_ObjectIdentity = ObjectIdentity
snFLS648Family = _SnFLS648Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 46, 2)
)
_SnFLS648BaseFamily_ObjectIdentity = ObjectIdentity
snFLS648BaseFamily = _SnFLS648BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 46, 2, 1)
)
_SnFLS648_ObjectIdentity = ObjectIdentity
snFLS648 = _SnFLS648_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 46, 2, 1, 1)
)
_SnFLS648Switch_ObjectIdentity = ObjectIdentity
snFLS648Switch = _SnFLS648Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 46, 2, 1, 1, 1)
)
_SnFLS648Router_ObjectIdentity = ObjectIdentity
snFLS648Router = _SnFLS648Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 46, 2, 1, 1, 2)
)
_SnSIFamily_ObjectIdentity = ObjectIdentity
snSIFamily = _SnSIFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47)
)
_SnSI100_ObjectIdentity = ObjectIdentity
snSI100 = _SnSI100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 1)
)
_SnSI100Switch_ObjectIdentity = ObjectIdentity
snSI100Switch = _SnSI100Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 1, 1)
)
_SnSI100Router_ObjectIdentity = ObjectIdentity
snSI100Router = _SnSI100Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 1, 2)
)
_SnSI350_ObjectIdentity = ObjectIdentity
snSI350 = _SnSI350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 2)
)
_SnSI350Switch_ObjectIdentity = ObjectIdentity
snSI350Switch = _SnSI350Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 2, 1)
)
_SnSI350Router_ObjectIdentity = ObjectIdentity
snSI350Router = _SnSI350Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 2, 2)
)
_SnSI450_ObjectIdentity = ObjectIdentity
snSI450 = _SnSI450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 3)
)
_SnSI450Switch_ObjectIdentity = ObjectIdentity
snSI450Switch = _SnSI450Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 3, 1)
)
_SnSI450Router_ObjectIdentity = ObjectIdentity
snSI450Router = _SnSI450Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 3, 2)
)
_SnSI850_ObjectIdentity = ObjectIdentity
snSI850 = _SnSI850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 4)
)
_SnSI850Switch_ObjectIdentity = ObjectIdentity
snSI850Switch = _SnSI850Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 4, 1)
)
_SnSI850Router_ObjectIdentity = ObjectIdentity
snSI850Router = _SnSI850Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 4, 2)
)
_SnSI350Plus_ObjectIdentity = ObjectIdentity
snSI350Plus = _SnSI350Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 5)
)
_SnSI350PlusSwitch_ObjectIdentity = ObjectIdentity
snSI350PlusSwitch = _SnSI350PlusSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 5, 1)
)
_SnSI350PlusRouter_ObjectIdentity = ObjectIdentity
snSI350PlusRouter = _SnSI350PlusRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 5, 2)
)
_SnSI450Plus_ObjectIdentity = ObjectIdentity
snSI450Plus = _SnSI450Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 6)
)
_SnSI450PlusSwitch_ObjectIdentity = ObjectIdentity
snSI450PlusSwitch = _SnSI450PlusSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 6, 1)
)
_SnSI450PlusRouter_ObjectIdentity = ObjectIdentity
snSI450PlusRouter = _SnSI450PlusRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 6, 2)
)
_SnSI850Plus_ObjectIdentity = ObjectIdentity
snSI850Plus = _SnSI850Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 7)
)
_SnSI850PlusSwitch_ObjectIdentity = ObjectIdentity
snSI850PlusSwitch = _SnSI850PlusSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 7, 1)
)
_SnSI850PlusRouter_ObjectIdentity = ObjectIdentity
snSI850PlusRouter = _SnSI850PlusRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 7, 2)
)
_SnServerIronGTc_ObjectIdentity = ObjectIdentity
snServerIronGTc = _SnServerIronGTc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 8)
)
_SnServerIronGTcSwitch_ObjectIdentity = ObjectIdentity
snServerIronGTcSwitch = _SnServerIronGTcSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 8, 1)
)
_SnServerIronGTcRouter_ObjectIdentity = ObjectIdentity
snServerIronGTcRouter = _SnServerIronGTcRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 8, 2)
)
_SnServerIronGTe_ObjectIdentity = ObjectIdentity
snServerIronGTe = _SnServerIronGTe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 9)
)
_SnServerIronGTeSwitch_ObjectIdentity = ObjectIdentity
snServerIronGTeSwitch = _SnServerIronGTeSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 9, 1)
)
_SnServerIronGTeRouter_ObjectIdentity = ObjectIdentity
snServerIronGTeRouter = _SnServerIronGTeRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 9, 2)
)
_SnServerIronGTePlus_ObjectIdentity = ObjectIdentity
snServerIronGTePlus = _SnServerIronGTePlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 10)
)
_SnServerIronGTePlusSwitch_ObjectIdentity = ObjectIdentity
snServerIronGTePlusSwitch = _SnServerIronGTePlusSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 10, 1)
)
_SnServerIronGTePlusRouter_ObjectIdentity = ObjectIdentity
snServerIronGTePlusRouter = _SnServerIronGTePlusRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 10, 2)
)
_SnServerIron4G_ObjectIdentity = ObjectIdentity
snServerIron4G = _SnServerIron4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 11)
)
_SnServerIron4GSwitch_ObjectIdentity = ObjectIdentity
snServerIron4GSwitch = _SnServerIron4GSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 11, 1)
)
_SnServerIron4GRouter_ObjectIdentity = ObjectIdentity
snServerIron4GRouter = _SnServerIron4GRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 11, 2)
)
_ServerIronAdx1000_ObjectIdentity = ObjectIdentity
serverIronAdx1000 = _ServerIronAdx1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 12)
)
_ServerIronAdx1000Switch_ObjectIdentity = ObjectIdentity
serverIronAdx1000Switch = _ServerIronAdx1000Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 12, 1)
)
_ServerIronAdx1000Router_ObjectIdentity = ObjectIdentity
serverIronAdx1000Router = _ServerIronAdx1000Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 12, 2)
)
_ServerIronAdx1000Ssl_ObjectIdentity = ObjectIdentity
serverIronAdx1000Ssl = _ServerIronAdx1000Ssl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 13)
)
_ServerIronAdx1000SslSwitch_ObjectIdentity = ObjectIdentity
serverIronAdx1000SslSwitch = _ServerIronAdx1000SslSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 13, 1)
)
_ServerIronAdx1000SslRouter_ObjectIdentity = ObjectIdentity
serverIronAdx1000SslRouter = _ServerIronAdx1000SslRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 13, 2)
)
_ServerIronAdx4000_ObjectIdentity = ObjectIdentity
serverIronAdx4000 = _ServerIronAdx4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 14)
)
_ServerIronAdx4000Switch_ObjectIdentity = ObjectIdentity
serverIronAdx4000Switch = _ServerIronAdx4000Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 14, 1)
)
_ServerIronAdx4000Router_ObjectIdentity = ObjectIdentity
serverIronAdx4000Router = _ServerIronAdx4000Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 14, 2)
)
_ServerIronAdx4000Ssl_ObjectIdentity = ObjectIdentity
serverIronAdx4000Ssl = _ServerIronAdx4000Ssl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 15)
)
_ServerIronAdx4000SslSwitch_ObjectIdentity = ObjectIdentity
serverIronAdx4000SslSwitch = _ServerIronAdx4000SslSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 15, 1)
)
_ServerIronAdx4000SslRouter_ObjectIdentity = ObjectIdentity
serverIronAdx4000SslRouter = _ServerIronAdx4000SslRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 15, 2)
)
_ServerIronAdx8000_ObjectIdentity = ObjectIdentity
serverIronAdx8000 = _ServerIronAdx8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 16)
)
_ServerIronAdx8000Switch_ObjectIdentity = ObjectIdentity
serverIronAdx8000Switch = _ServerIronAdx8000Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 16, 1)
)
_ServerIronAdx8000Router_ObjectIdentity = ObjectIdentity
serverIronAdx8000Router = _ServerIronAdx8000Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 16, 2)
)
_ServerIronAdx8000Ssl_ObjectIdentity = ObjectIdentity
serverIronAdx8000Ssl = _ServerIronAdx8000Ssl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 17)
)
_ServerIronAdx8000SslSwitch_ObjectIdentity = ObjectIdentity
serverIronAdx8000SslSwitch = _ServerIronAdx8000SslSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 17, 1)
)
_ServerIronAdx8000SslRouter_ObjectIdentity = ObjectIdentity
serverIronAdx8000SslRouter = _ServerIronAdx8000SslRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 17, 2)
)
_ServerIronAdx10000_ObjectIdentity = ObjectIdentity
serverIronAdx10000 = _ServerIronAdx10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 18)
)
_ServerIronAdx10000Switch_ObjectIdentity = ObjectIdentity
serverIronAdx10000Switch = _ServerIronAdx10000Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 18, 1)
)
_ServerIronAdx10000Router_ObjectIdentity = ObjectIdentity
serverIronAdx10000Router = _ServerIronAdx10000Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 18, 2)
)
_ServerIronAdx10000Ssl_ObjectIdentity = ObjectIdentity
serverIronAdx10000Ssl = _ServerIronAdx10000Ssl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 19)
)
_ServerIronAdx10000SslSwitch_ObjectIdentity = ObjectIdentity
serverIronAdx10000SslSwitch = _ServerIronAdx10000SslSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 19, 1)
)
_ServerIronAdx10000SslRouter_ObjectIdentity = ObjectIdentity
serverIronAdx10000SslRouter = _ServerIronAdx10000SslRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 47, 19, 2)
)
_SnFastIronStackFamily_ObjectIdentity = ObjectIdentity
snFastIronStackFamily = _SnFastIronStackFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48)
)
_SnFastIronStack_ObjectIdentity = ObjectIdentity
snFastIronStack = _SnFastIronStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 1)
)
_SnFastIronStackSwitch_ObjectIdentity = ObjectIdentity
snFastIronStackSwitch = _SnFastIronStackSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 1, 1)
)
_SnFastIronStackRouter_ObjectIdentity = ObjectIdentity
snFastIronStackRouter = _SnFastIronStackRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 1, 2)
)
_SnFastIronStackFCX_ObjectIdentity = ObjectIdentity
snFastIronStackFCX = _SnFastIronStackFCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 2)
)
_SnFastIronStackFCXSwitch_ObjectIdentity = ObjectIdentity
snFastIronStackFCXSwitch = _SnFastIronStackFCXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 2, 1)
)
_SnFastIronStackFCXBaseL3Router_ObjectIdentity = ObjectIdentity
snFastIronStackFCXBaseL3Router = _SnFastIronStackFCXBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 2, 2)
)
_SnFastIronStackFCXRouter_ObjectIdentity = ObjectIdentity
snFastIronStackFCXRouter = _SnFastIronStackFCXRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 2, 3)
)
_SnFastIronStackFCXAdvRouter_ObjectIdentity = ObjectIdentity
snFastIronStackFCXAdvRouter = _SnFastIronStackFCXAdvRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 2, 4)
)
_SnFastIronStackICX6610_ObjectIdentity = ObjectIdentity
snFastIronStackICX6610 = _SnFastIronStackICX6610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 3)
)
_SnFastIronStackICX6610Switch_ObjectIdentity = ObjectIdentity
snFastIronStackICX6610Switch = _SnFastIronStackICX6610Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 3, 1)
)
_SnFastIronStackICX6610BaseL3Router_ObjectIdentity = ObjectIdentity
snFastIronStackICX6610BaseL3Router = _SnFastIronStackICX6610BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 3, 2)
)
_SnFastIronStackICX6610Router_ObjectIdentity = ObjectIdentity
snFastIronStackICX6610Router = _SnFastIronStackICX6610Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 3, 3)
)
_SnFastIronStackICX6610PRouter_ObjectIdentity = ObjectIdentity
snFastIronStackICX6610PRouter = _SnFastIronStackICX6610PRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 3, 4)
)
_SnFastIronStackICX6610ARouter_ObjectIdentity = ObjectIdentity
snFastIronStackICX6610ARouter = _SnFastIronStackICX6610ARouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 3, 5)
)
_SnFastIronStackICX6430_ObjectIdentity = ObjectIdentity
snFastIronStackICX6430 = _SnFastIronStackICX6430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 4)
)
_SnFastIronStackICX6430Switch_ObjectIdentity = ObjectIdentity
snFastIronStackICX6430Switch = _SnFastIronStackICX6430Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 4, 1)
)
_SnFastIronStackICX6450_ObjectIdentity = ObjectIdentity
snFastIronStackICX6450 = _SnFastIronStackICX6450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 5)
)
_SnFastIronStackICX6450Switch_ObjectIdentity = ObjectIdentity
snFastIronStackICX6450Switch = _SnFastIronStackICX6450Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 5, 1)
)
_SnFastIronStackICX6450BaseL3Router_ObjectIdentity = ObjectIdentity
snFastIronStackICX6450BaseL3Router = _SnFastIronStackICX6450BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 5, 2)
)
_SnFastIronStackICX6450Router_ObjectIdentity = ObjectIdentity
snFastIronStackICX6450Router = _SnFastIronStackICX6450Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 5, 3)
)
_SnFastIronStackICX6450PRouter_ObjectIdentity = ObjectIdentity
snFastIronStackICX6450PRouter = _SnFastIronStackICX6450PRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 5, 4)
)
_SnFastIronStackMixedStack_ObjectIdentity = ObjectIdentity
snFastIronStackMixedStack = _SnFastIronStackMixedStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 6)
)
_SnFastIronStackMixedStackSwitch_ObjectIdentity = ObjectIdentity
snFastIronStackMixedStackSwitch = _SnFastIronStackMixedStackSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 6, 1)
)
_SnFastIronStackMixedStackBaseL3Router_ObjectIdentity = ObjectIdentity
snFastIronStackMixedStackBaseL3Router = _SnFastIronStackMixedStackBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 6, 2)
)
_SnFastIronStackMixedStackRouter_ObjectIdentity = ObjectIdentity
snFastIronStackMixedStackRouter = _SnFastIronStackMixedStackRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 6, 3)
)
_SnFastIronStackMixedStackPRouter_ObjectIdentity = ObjectIdentity
snFastIronStackMixedStackPRouter = _SnFastIronStackMixedStackPRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 6, 4)
)
_SnFastIronStackMixedStackARouter_ObjectIdentity = ObjectIdentity
snFastIronStackMixedStackARouter = _SnFastIronStackMixedStackARouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 6, 5)
)
_SnFastIronStackICX7750_ObjectIdentity = ObjectIdentity
snFastIronStackICX7750 = _SnFastIronStackICX7750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 7)
)
_SnFastIronStackICX7750Switch_ObjectIdentity = ObjectIdentity
snFastIronStackICX7750Switch = _SnFastIronStackICX7750Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 7, 1)
)
_SnFastIronStackICX7750BaseL3Router_ObjectIdentity = ObjectIdentity
snFastIronStackICX7750BaseL3Router = _SnFastIronStackICX7750BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 7, 2)
)
_SnFastIronStackICX7750Router_ObjectIdentity = ObjectIdentity
snFastIronStackICX7750Router = _SnFastIronStackICX7750Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 7, 3)
)
_SnFastIronStackICX7450_ObjectIdentity = ObjectIdentity
snFastIronStackICX7450 = _SnFastIronStackICX7450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 8)
)
_SnFastIronStackICX7450Switch_ObjectIdentity = ObjectIdentity
snFastIronStackICX7450Switch = _SnFastIronStackICX7450Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 8, 1)
)
_SnFastIronStackICX7450BaseL3Router_ObjectIdentity = ObjectIdentity
snFastIronStackICX7450BaseL3Router = _SnFastIronStackICX7450BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 8, 2)
)
_SnFastIronStackICX7450Router_ObjectIdentity = ObjectIdentity
snFastIronStackICX7450Router = _SnFastIronStackICX7450Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 48, 8, 3)
)
_SnCes2000Family_ObjectIdentity = ObjectIdentity
snCes2000Family = _SnCes2000Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 49)
)
_SnCes2024F_ObjectIdentity = ObjectIdentity
snCes2024F = _SnCes2024F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 49, 1)
)
_SnCes2024C_ObjectIdentity = ObjectIdentity
snCes2024C = _SnCes2024C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 49, 2)
)
_SnCes2048F_ObjectIdentity = ObjectIdentity
snCes2048F = _SnCes2048F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 49, 3)
)
_SnCes2048C_ObjectIdentity = ObjectIdentity
snCes2048C = _SnCes2048C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 49, 4)
)
_SnCes2048FX_ObjectIdentity = ObjectIdentity
snCes2048FX = _SnCes2048FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 49, 5)
)
_SnCes2048CX_ObjectIdentity = ObjectIdentity
snCes2048CX = _SnCes2048CX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 49, 6)
)
_SnCes2024F4X_ObjectIdentity = ObjectIdentity
snCes2024F4X = _SnCes2024F4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 49, 7)
)
_SnCes2024C4X_ObjectIdentity = ObjectIdentity
snCes2024C4X = _SnCes2024C4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 49, 8)
)
_SnFLSLCFamily_ObjectIdentity = ObjectIdentity
snFLSLCFamily = _SnFLSLCFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50)
)
_SnFLSLC624Family_ObjectIdentity = ObjectIdentity
snFLSLC624Family = _SnFLSLC624Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 1)
)
_SnFLSLC624BaseFamily_ObjectIdentity = ObjectIdentity
snFLSLC624BaseFamily = _SnFLSLC624BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 1, 1)
)
_SnFLSLC624_ObjectIdentity = ObjectIdentity
snFLSLC624 = _SnFLSLC624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 1, 1, 1)
)
_SnFLSLC624Switch_ObjectIdentity = ObjectIdentity
snFLSLC624Switch = _SnFLSLC624Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 1, 1, 1, 1)
)
_SnFLSLC624Router_ObjectIdentity = ObjectIdentity
snFLSLC624Router = _SnFLSLC624Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 1, 1, 1, 2)
)
_SnFLSLC624POEFamily_ObjectIdentity = ObjectIdentity
snFLSLC624POEFamily = _SnFLSLC624POEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 1, 2)
)
_SnFLSLC624POE_ObjectIdentity = ObjectIdentity
snFLSLC624POE = _SnFLSLC624POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 1, 2, 1)
)
_SnFLSLC624POESwitch_ObjectIdentity = ObjectIdentity
snFLSLC624POESwitch = _SnFLSLC624POESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 1, 2, 1, 1)
)
_SnFLSLC624POERouter_ObjectIdentity = ObjectIdentity
snFLSLC624POERouter = _SnFLSLC624POERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 1, 2, 1, 2)
)
_SnFLSLC648Family_ObjectIdentity = ObjectIdentity
snFLSLC648Family = _SnFLSLC648Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 2)
)
_SnFLSLC648BaseFamily_ObjectIdentity = ObjectIdentity
snFLSLC648BaseFamily = _SnFLSLC648BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 2, 1)
)
_SnFLSLC648_ObjectIdentity = ObjectIdentity
snFLSLC648 = _SnFLSLC648_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 2, 1, 1)
)
_SnFLSLC648Switch_ObjectIdentity = ObjectIdentity
snFLSLC648Switch = _SnFLSLC648Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 2, 1, 1, 1)
)
_SnFLSLC648Router_ObjectIdentity = ObjectIdentity
snFLSLC648Router = _SnFLSLC648Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 2, 1, 1, 2)
)
_SnFLSLC648POEFamily_ObjectIdentity = ObjectIdentity
snFLSLC648POEFamily = _SnFLSLC648POEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 2, 2)
)
_SnFLSLC648POE_ObjectIdentity = ObjectIdentity
snFLSLC648POE = _SnFLSLC648POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 2, 2, 1)
)
_SnFLSLC648POESwitch_ObjectIdentity = ObjectIdentity
snFLSLC648POESwitch = _SnFLSLC648POESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 2, 2, 1, 1)
)
_SnFLSLC648POERouter_ObjectIdentity = ObjectIdentity
snFLSLC648POERouter = _SnFLSLC648POERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 50, 2, 2, 1, 2)
)
_SnCer2000Family_ObjectIdentity = ObjectIdentity
snCer2000Family = _SnCer2000Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 51)
)
_SnCer2024F_ObjectIdentity = ObjectIdentity
snCer2024F = _SnCer2024F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 51, 1)
)
_SnCer2024C_ObjectIdentity = ObjectIdentity
snCer2024C = _SnCer2024C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 51, 2)
)
_SnCer2048F_ObjectIdentity = ObjectIdentity
snCer2048F = _SnCer2048F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 51, 3)
)
_SnCer2048C_ObjectIdentity = ObjectIdentity
snCer2048C = _SnCer2048C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 51, 4)
)
_SnCer2048FX_ObjectIdentity = ObjectIdentity
snCer2048FX = _SnCer2048FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 51, 5)
)
_SnCer2048CX_ObjectIdentity = ObjectIdentity
snCer2048CX = _SnCer2048CX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 51, 6)
)
_SnCer2024F4X_ObjectIdentity = ObjectIdentity
snCer2024F4X = _SnCer2024F4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 51, 7)
)
_SnCer2024C4X_ObjectIdentity = ObjectIdentity
snCer2024C4X = _SnCer2024C4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 51, 8)
)
_SnFWSFamily_ObjectIdentity = ObjectIdentity
snFWSFamily = _SnFWSFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52)
)
_SnFWS624Family_ObjectIdentity = ObjectIdentity
snFWS624Family = _SnFWS624Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1)
)
_SnFWS624BaseFamily_ObjectIdentity = ObjectIdentity
snFWS624BaseFamily = _SnFWS624BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 1)
)
_SnFWS624_ObjectIdentity = ObjectIdentity
snFWS624 = _SnFWS624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 1, 1)
)
_SnFWS624Switch_ObjectIdentity = ObjectIdentity
snFWS624Switch = _SnFWS624Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 1, 1, 1)
)
_SnFWS624BaseL3Router_ObjectIdentity = ObjectIdentity
snFWS624BaseL3Router = _SnFWS624BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 1, 1, 2)
)
_SnFWS624EdgePremRouter_ObjectIdentity = ObjectIdentity
snFWS624EdgePremRouter = _SnFWS624EdgePremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 1, 1, 3)
)
_SnFWS624GFamily_ObjectIdentity = ObjectIdentity
snFWS624GFamily = _SnFWS624GFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 2)
)
_SnFWS624G_ObjectIdentity = ObjectIdentity
snFWS624G = _SnFWS624G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 2, 1)
)
_SnFWS624GSwitch_ObjectIdentity = ObjectIdentity
snFWS624GSwitch = _SnFWS624GSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 2, 1, 1)
)
_SnFWS624GBaseL3Router_ObjectIdentity = ObjectIdentity
snFWS624GBaseL3Router = _SnFWS624GBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 2, 1, 2)
)
_SnFWS624GEdgePremRouter_ObjectIdentity = ObjectIdentity
snFWS624GEdgePremRouter = _SnFWS624GEdgePremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 2, 1, 3)
)
_SnFWS624POEFamily_ObjectIdentity = ObjectIdentity
snFWS624POEFamily = _SnFWS624POEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 3)
)
_SnFWS624POE_ObjectIdentity = ObjectIdentity
snFWS624POE = _SnFWS624POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 3, 1)
)
_SnFWS624POESwitch_ObjectIdentity = ObjectIdentity
snFWS624POESwitch = _SnFWS624POESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 3, 1, 1)
)
_SnFWS624POEBaseL3Router_ObjectIdentity = ObjectIdentity
snFWS624POEBaseL3Router = _SnFWS624POEBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 3, 1, 2)
)
_SnFWS624POEEdgePremRouter_ObjectIdentity = ObjectIdentity
snFWS624POEEdgePremRouter = _SnFWS624POEEdgePremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 3, 1, 3)
)
_SnFWS624GPOEFamily_ObjectIdentity = ObjectIdentity
snFWS624GPOEFamily = _SnFWS624GPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 4)
)
_SnFWS624GPOE_ObjectIdentity = ObjectIdentity
snFWS624GPOE = _SnFWS624GPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 4, 1)
)
_SnFWS624GPOESwitch_ObjectIdentity = ObjectIdentity
snFWS624GPOESwitch = _SnFWS624GPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 4, 1, 1)
)
_SnFWS624GPOEBaseL3Router_ObjectIdentity = ObjectIdentity
snFWS624GPOEBaseL3Router = _SnFWS624GPOEBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 4, 1, 2)
)
_SnFWS624GPOEEdgePremRouter_ObjectIdentity = ObjectIdentity
snFWS624GPOEEdgePremRouter = _SnFWS624GPOEEdgePremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 1, 4, 1, 3)
)
_SnFWS648Family_ObjectIdentity = ObjectIdentity
snFWS648Family = _SnFWS648Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2)
)
_SnFWS648BaseFamily_ObjectIdentity = ObjectIdentity
snFWS648BaseFamily = _SnFWS648BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 1)
)
_SnFWS648_ObjectIdentity = ObjectIdentity
snFWS648 = _SnFWS648_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 1, 1)
)
_SnFWS648Switch_ObjectIdentity = ObjectIdentity
snFWS648Switch = _SnFWS648Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 1, 1, 1)
)
_SnFWS648BaseL3Router_ObjectIdentity = ObjectIdentity
snFWS648BaseL3Router = _SnFWS648BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 1, 1, 2)
)
_SnFWS648EdgePremRouter_ObjectIdentity = ObjectIdentity
snFWS648EdgePremRouter = _SnFWS648EdgePremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 1, 1, 3)
)
_SnFWS648GFamily_ObjectIdentity = ObjectIdentity
snFWS648GFamily = _SnFWS648GFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 2)
)
_SnFWS648G_ObjectIdentity = ObjectIdentity
snFWS648G = _SnFWS648G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 2, 1)
)
_SnFWS648GSwitch_ObjectIdentity = ObjectIdentity
snFWS648GSwitch = _SnFWS648GSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 2, 1, 1)
)
_SnFWS648GBaseL3Router_ObjectIdentity = ObjectIdentity
snFWS648GBaseL3Router = _SnFWS648GBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 2, 1, 2)
)
_SnFWS648GEdgePremRouter_ObjectIdentity = ObjectIdentity
snFWS648GEdgePremRouter = _SnFWS648GEdgePremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 2, 1, 3)
)
_SnFWS648POEFamily_ObjectIdentity = ObjectIdentity
snFWS648POEFamily = _SnFWS648POEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 3)
)
_SnFWS648POE_ObjectIdentity = ObjectIdentity
snFWS648POE = _SnFWS648POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 3, 1)
)
_SnFWS648POESwitch_ObjectIdentity = ObjectIdentity
snFWS648POESwitch = _SnFWS648POESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 3, 1, 1)
)
_SnFWS648POEBaseL3Router_ObjectIdentity = ObjectIdentity
snFWS648POEBaseL3Router = _SnFWS648POEBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 3, 1, 2)
)
_SnFWS648POEEdgePremRouter_ObjectIdentity = ObjectIdentity
snFWS648POEEdgePremRouter = _SnFWS648POEEdgePremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 3, 1, 3)
)
_SnFWS648GPOEFamily_ObjectIdentity = ObjectIdentity
snFWS648GPOEFamily = _SnFWS648GPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 4)
)
_SnFWS648GPOE_ObjectIdentity = ObjectIdentity
snFWS648GPOE = _SnFWS648GPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 4, 1)
)
_SnFWS648GPOESwitch_ObjectIdentity = ObjectIdentity
snFWS648GPOESwitch = _SnFWS648GPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 4, 1, 1)
)
_SnFWS648GPOEBaseL3Router_ObjectIdentity = ObjectIdentity
snFWS648GPOEBaseL3Router = _SnFWS648GPOEBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 4, 1, 2)
)
_SnFWS648GPOEEdgePremRouter_ObjectIdentity = ObjectIdentity
snFWS648GPOEEdgePremRouter = _SnFWS648GPOEEdgePremRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 52, 2, 4, 1, 3)
)
_SnTurboIron2_ObjectIdentity = ObjectIdentity
snTurboIron2 = _SnTurboIron2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 53)
)
_SnTI2X24Family_ObjectIdentity = ObjectIdentity
snTI2X24Family = _SnTI2X24Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 53, 1)
)
_SnTI2X24Switch_ObjectIdentity = ObjectIdentity
snTI2X24Switch = _SnTI2X24Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 53, 1, 1)
)
_SnTI2X24Router_ObjectIdentity = ObjectIdentity
snTI2X24Router = _SnTI2X24Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 53, 1, 2)
)
_SnTI2X48Family_ObjectIdentity = ObjectIdentity
snTI2X48Family = _SnTI2X48Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 53, 2)
)
_SnTI2X48Switch_ObjectIdentity = ObjectIdentity
snTI2X48Switch = _SnTI2X48Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 53, 2, 1)
)
_SnTI2X48Router_ObjectIdentity = ObjectIdentity
snTI2X48Router = _SnTI2X48Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 53, 2, 2)
)
_SnFCXFamily_ObjectIdentity = ObjectIdentity
snFCXFamily = _SnFCXFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54)
)
_SnFCX624Family_ObjectIdentity = ObjectIdentity
snFCX624Family = _SnFCX624Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1)
)
_SnFCX624SBaseFamily_ObjectIdentity = ObjectIdentity
snFCX624SBaseFamily = _SnFCX624SBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 1)
)
_SnFCX624S_ObjectIdentity = ObjectIdentity
snFCX624S = _SnFCX624S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 1, 1)
)
_SnFCX624SSwitch_ObjectIdentity = ObjectIdentity
snFCX624SSwitch = _SnFCX624SSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 1, 1, 1)
)
_SnFCX624SBaseL3Router_ObjectIdentity = ObjectIdentity
snFCX624SBaseL3Router = _SnFCX624SBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 1, 1, 2)
)
_SnFCX624SRouter_ObjectIdentity = ObjectIdentity
snFCX624SRouter = _SnFCX624SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 1, 1, 3)
)
_SnFCX624SAdvRouter_ObjectIdentity = ObjectIdentity
snFCX624SAdvRouter = _SnFCX624SAdvRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 1, 1, 4)
)
_SnFCX624SHPOEFamily_ObjectIdentity = ObjectIdentity
snFCX624SHPOEFamily = _SnFCX624SHPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 2)
)
_SnFCX624SHPOE_ObjectIdentity = ObjectIdentity
snFCX624SHPOE = _SnFCX624SHPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 2, 1)
)
_SnFCX624SHPOESwitch_ObjectIdentity = ObjectIdentity
snFCX624SHPOESwitch = _SnFCX624SHPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 2, 1, 1)
)
_SnFCX624SHPOEBaseL3Router_ObjectIdentity = ObjectIdentity
snFCX624SHPOEBaseL3Router = _SnFCX624SHPOEBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 2, 1, 2)
)
_SnFCX624SHPOERouter_ObjectIdentity = ObjectIdentity
snFCX624SHPOERouter = _SnFCX624SHPOERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 2, 1, 3)
)
_SnFCX624SHPOEAdvRouter_ObjectIdentity = ObjectIdentity
snFCX624SHPOEAdvRouter = _SnFCX624SHPOEAdvRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 2, 1, 4)
)
_SnFCX624SFFamily_ObjectIdentity = ObjectIdentity
snFCX624SFFamily = _SnFCX624SFFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 3)
)
_SnFCX624SF_ObjectIdentity = ObjectIdentity
snFCX624SF = _SnFCX624SF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 3, 1)
)
_SnFCX624SFSwitch_ObjectIdentity = ObjectIdentity
snFCX624SFSwitch = _SnFCX624SFSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 3, 1, 1)
)
_SnFCX624SFBaseL3Router_ObjectIdentity = ObjectIdentity
snFCX624SFBaseL3Router = _SnFCX624SFBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 3, 1, 2)
)
_SnFCX624SFRouter_ObjectIdentity = ObjectIdentity
snFCX624SFRouter = _SnFCX624SFRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 3, 1, 3)
)
_SnFCX624SFAdvRouter_ObjectIdentity = ObjectIdentity
snFCX624SFAdvRouter = _SnFCX624SFAdvRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 3, 1, 4)
)
_SnFCX624BaseFamily_ObjectIdentity = ObjectIdentity
snFCX624BaseFamily = _SnFCX624BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 4)
)
_SnFCX624_ObjectIdentity = ObjectIdentity
snFCX624 = _SnFCX624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 4, 1)
)
_SnFCX624Switch_ObjectIdentity = ObjectIdentity
snFCX624Switch = _SnFCX624Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 4, 1, 1)
)
_SnFCX624BaseL3Router_ObjectIdentity = ObjectIdentity
snFCX624BaseL3Router = _SnFCX624BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 4, 1, 2)
)
_SnFCX624Router_ObjectIdentity = ObjectIdentity
snFCX624Router = _SnFCX624Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 4, 1, 3)
)
_SnFCX624AdvRouter_ObjectIdentity = ObjectIdentity
snFCX624AdvRouter = _SnFCX624AdvRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 1, 4, 1, 4)
)
_SnFCX648Family_ObjectIdentity = ObjectIdentity
snFCX648Family = _SnFCX648Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2)
)
_SnFCX648SBaseFamily_ObjectIdentity = ObjectIdentity
snFCX648SBaseFamily = _SnFCX648SBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 1)
)
_SnFCX648S_ObjectIdentity = ObjectIdentity
snFCX648S = _SnFCX648S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 1, 1)
)
_SnFCX648SSwitch_ObjectIdentity = ObjectIdentity
snFCX648SSwitch = _SnFCX648SSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 1, 1, 1)
)
_SnFCX648SBaseL3Router_ObjectIdentity = ObjectIdentity
snFCX648SBaseL3Router = _SnFCX648SBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 1, 1, 2)
)
_SnFCX648SRouter_ObjectIdentity = ObjectIdentity
snFCX648SRouter = _SnFCX648SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 1, 1, 3)
)
_SnFCX648SAdvRouter_ObjectIdentity = ObjectIdentity
snFCX648SAdvRouter = _SnFCX648SAdvRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 1, 1, 4)
)
_SnFCX648SHPOEFamily_ObjectIdentity = ObjectIdentity
snFCX648SHPOEFamily = _SnFCX648SHPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 2)
)
_SnFCX648SHPOE_ObjectIdentity = ObjectIdentity
snFCX648SHPOE = _SnFCX648SHPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 2, 1)
)
_SnFCX648SHPOESwitch_ObjectIdentity = ObjectIdentity
snFCX648SHPOESwitch = _SnFCX648SHPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 2, 1, 1)
)
_SnFCX648SHPOEBaseL3Router_ObjectIdentity = ObjectIdentity
snFCX648SHPOEBaseL3Router = _SnFCX648SHPOEBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 2, 1, 2)
)
_SnFCX648SHPOERouter_ObjectIdentity = ObjectIdentity
snFCX648SHPOERouter = _SnFCX648SHPOERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 2, 1, 3)
)
_SnFCX648SHPOEAdvRouter_ObjectIdentity = ObjectIdentity
snFCX648SHPOEAdvRouter = _SnFCX648SHPOEAdvRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 2, 1, 4)
)
_SnFCX648BaseFamily_ObjectIdentity = ObjectIdentity
snFCX648BaseFamily = _SnFCX648BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 4)
)
_SnFCX648_ObjectIdentity = ObjectIdentity
snFCX648 = _SnFCX648_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 4, 1)
)
_SnFCX648Switch_ObjectIdentity = ObjectIdentity
snFCX648Switch = _SnFCX648Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 4, 1, 1)
)
_SnFCX648BaseL3Router_ObjectIdentity = ObjectIdentity
snFCX648BaseL3Router = _SnFCX648BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 4, 1, 2)
)
_SnFCX648Router_ObjectIdentity = ObjectIdentity
snFCX648Router = _SnFCX648Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 4, 1, 3)
)
_SnFCX648AdvRouter_ObjectIdentity = ObjectIdentity
snFCX648AdvRouter = _SnFCX648AdvRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 54, 2, 4, 1, 4)
)
_SnBrocadeMLXeFamily_ObjectIdentity = ObjectIdentity
snBrocadeMLXeFamily = _SnBrocadeMLXeFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 55)
)
_SnBrocadeMLXe16_ObjectIdentity = ObjectIdentity
snBrocadeMLXe16 = _SnBrocadeMLXe16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 55, 1)
)
_SnBrocadeMLXe16Router_ObjectIdentity = ObjectIdentity
snBrocadeMLXe16Router = _SnBrocadeMLXe16Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 55, 1, 2)
)
_SnBrocadeMLXe8_ObjectIdentity = ObjectIdentity
snBrocadeMLXe8 = _SnBrocadeMLXe8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 55, 2)
)
_SnBrocadeMLXe8Router_ObjectIdentity = ObjectIdentity
snBrocadeMLXe8Router = _SnBrocadeMLXe8Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 55, 2, 2)
)
_SnBrocadeMLXe4_ObjectIdentity = ObjectIdentity
snBrocadeMLXe4 = _SnBrocadeMLXe4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 55, 3)
)
_SnBrocadeMLXe4Router_ObjectIdentity = ObjectIdentity
snBrocadeMLXe4Router = _SnBrocadeMLXe4Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 55, 3, 2)
)
_SnBrocadeMLXe32_ObjectIdentity = ObjectIdentity
snBrocadeMLXe32 = _SnBrocadeMLXe32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 55, 4)
)
_SnBrocadeMLXe32Router_ObjectIdentity = ObjectIdentity
snBrocadeMLXe32Router = _SnBrocadeMLXe32Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 55, 4, 2)
)
_SnICX6610Family_ObjectIdentity = ObjectIdentity
snICX6610Family = _SnICX6610Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56)
)
_SnICX661024Family_ObjectIdentity = ObjectIdentity
snICX661024Family = _SnICX661024Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1)
)
_SnICX661024BaseFamily_ObjectIdentity = ObjectIdentity
snICX661024BaseFamily = _SnICX661024BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 1)
)
_SnICX661024_ObjectIdentity = ObjectIdentity
snICX661024 = _SnICX661024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 1, 1)
)
_SnICX661024Switch_ObjectIdentity = ObjectIdentity
snICX661024Switch = _SnICX661024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 1, 1, 1)
)
_SnICX661024BaseL3Router_ObjectIdentity = ObjectIdentity
snICX661024BaseL3Router = _SnICX661024BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 1, 1, 2)
)
_SnICX661024Router_ObjectIdentity = ObjectIdentity
snICX661024Router = _SnICX661024Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 1, 1, 3)
)
_SnICX661024PRouter_ObjectIdentity = ObjectIdentity
snICX661024PRouter = _SnICX661024PRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 1, 1, 4)
)
_SnICX661024ARouter_ObjectIdentity = ObjectIdentity
snICX661024ARouter = _SnICX661024ARouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 1, 1, 5)
)
_SnICX661024HPOEFamily_ObjectIdentity = ObjectIdentity
snICX661024HPOEFamily = _SnICX661024HPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 2)
)
_SnICX661024HPOE_ObjectIdentity = ObjectIdentity
snICX661024HPOE = _SnICX661024HPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 2, 1)
)
_SnICX661024HPOESwitch_ObjectIdentity = ObjectIdentity
snICX661024HPOESwitch = _SnICX661024HPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 2, 1, 1)
)
_SnICX661024HPOEBaseL3Router_ObjectIdentity = ObjectIdentity
snICX661024HPOEBaseL3Router = _SnICX661024HPOEBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 2, 1, 2)
)
_SnICX661024HPOERouter_ObjectIdentity = ObjectIdentity
snICX661024HPOERouter = _SnICX661024HPOERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 2, 1, 3)
)
_SnICX661024HPOEPRouter_ObjectIdentity = ObjectIdentity
snICX661024HPOEPRouter = _SnICX661024HPOEPRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 2, 1, 4)
)
_SnICX661024HPOEARouter_ObjectIdentity = ObjectIdentity
snICX661024HPOEARouter = _SnICX661024HPOEARouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 2, 1, 5)
)
_SnICX661024FFamily_ObjectIdentity = ObjectIdentity
snICX661024FFamily = _SnICX661024FFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 3)
)
_SnICX661024F_ObjectIdentity = ObjectIdentity
snICX661024F = _SnICX661024F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 3, 1)
)
_SnICX661024FSwitch_ObjectIdentity = ObjectIdentity
snICX661024FSwitch = _SnICX661024FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 3, 1, 1)
)
_SnICX661024FBaseL3Router_ObjectIdentity = ObjectIdentity
snICX661024FBaseL3Router = _SnICX661024FBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 3, 1, 2)
)
_SnICX661024FRouter_ObjectIdentity = ObjectIdentity
snICX661024FRouter = _SnICX661024FRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 3, 1, 3)
)
_SnICX661024FPRouter_ObjectIdentity = ObjectIdentity
snICX661024FPRouter = _SnICX661024FPRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 3, 1, 4)
)
_SnICX661024FARouter_ObjectIdentity = ObjectIdentity
snICX661024FARouter = _SnICX661024FARouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 1, 3, 1, 5)
)
_SnICX661048Family_ObjectIdentity = ObjectIdentity
snICX661048Family = _SnICX661048Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2)
)
_SnICX661048BaseFamily_ObjectIdentity = ObjectIdentity
snICX661048BaseFamily = _SnICX661048BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 1)
)
_SnICX661048_ObjectIdentity = ObjectIdentity
snICX661048 = _SnICX661048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 1, 1)
)
_SnICX661048Switch_ObjectIdentity = ObjectIdentity
snICX661048Switch = _SnICX661048Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 1, 1, 1)
)
_SnICX661048BaseL3Router_ObjectIdentity = ObjectIdentity
snICX661048BaseL3Router = _SnICX661048BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 1, 1, 2)
)
_SnICX661048Router_ObjectIdentity = ObjectIdentity
snICX661048Router = _SnICX661048Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 1, 1, 3)
)
_SnICX661048PRouter_ObjectIdentity = ObjectIdentity
snICX661048PRouter = _SnICX661048PRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 1, 1, 4)
)
_SnICX661048ARouter_ObjectIdentity = ObjectIdentity
snICX661048ARouter = _SnICX661048ARouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 1, 1, 5)
)
_SnICX661048HPOEFamily_ObjectIdentity = ObjectIdentity
snICX661048HPOEFamily = _SnICX661048HPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 2)
)
_SnICX661048HPOE_ObjectIdentity = ObjectIdentity
snICX661048HPOE = _SnICX661048HPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 2, 1)
)
_SnICX661048HPOESwitch_ObjectIdentity = ObjectIdentity
snICX661048HPOESwitch = _SnICX661048HPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 2, 1, 1)
)
_SnICX661048HPOEBaseL3Router_ObjectIdentity = ObjectIdentity
snICX661048HPOEBaseL3Router = _SnICX661048HPOEBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 2, 1, 2)
)
_SnICX661048HPOERouter_ObjectIdentity = ObjectIdentity
snICX661048HPOERouter = _SnICX661048HPOERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 2, 1, 3)
)
_SnICX661048HPOEPRouter_ObjectIdentity = ObjectIdentity
snICX661048HPOEPRouter = _SnICX661048HPOEPRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 2, 1, 4)
)
_SnICX661048HPOEARouter_ObjectIdentity = ObjectIdentity
snICX661048HPOEARouter = _SnICX661048HPOEARouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 56, 2, 2, 1, 5)
)
_SnICX6430Family_ObjectIdentity = ObjectIdentity
snICX6430Family = _SnICX6430Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57)
)
_SnICX643024Family_ObjectIdentity = ObjectIdentity
snICX643024Family = _SnICX643024Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 1)
)
_SnICX643024BaseFamily_ObjectIdentity = ObjectIdentity
snICX643024BaseFamily = _SnICX643024BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 1, 1)
)
_SnICX643024_ObjectIdentity = ObjectIdentity
snICX643024 = _SnICX643024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 1, 1, 1)
)
_SnICX643024Switch_ObjectIdentity = ObjectIdentity
snICX643024Switch = _SnICX643024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 1, 1, 1, 1)
)
_SnICX643024HPOEFamily_ObjectIdentity = ObjectIdentity
snICX643024HPOEFamily = _SnICX643024HPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 1, 2)
)
_SnICX643024HPOE_ObjectIdentity = ObjectIdentity
snICX643024HPOE = _SnICX643024HPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 1, 2, 1)
)
_SnICX643024HPOESwitch_ObjectIdentity = ObjectIdentity
snICX643024HPOESwitch = _SnICX643024HPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 1, 2, 1, 1)
)
_SnICX643048Family_ObjectIdentity = ObjectIdentity
snICX643048Family = _SnICX643048Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 2)
)
_SnICX643048BaseFamily_ObjectIdentity = ObjectIdentity
snICX643048BaseFamily = _SnICX643048BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 2, 1)
)
_SnICX643048_ObjectIdentity = ObjectIdentity
snICX643048 = _SnICX643048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 2, 1, 1)
)
_SnICX643048Switch_ObjectIdentity = ObjectIdentity
snICX643048Switch = _SnICX643048Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 2, 1, 1, 1)
)
_SnICX643048HPOEFamily_ObjectIdentity = ObjectIdentity
snICX643048HPOEFamily = _SnICX643048HPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 2, 2)
)
_SnICX643048HPOE_ObjectIdentity = ObjectIdentity
snICX643048HPOE = _SnICX643048HPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 2, 2, 1)
)
_SnICX643048HPOESwitch_ObjectIdentity = ObjectIdentity
snICX643048HPOESwitch = _SnICX643048HPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 2, 2, 1, 1)
)
_SnICX6430C12Family_ObjectIdentity = ObjectIdentity
snICX6430C12Family = _SnICX6430C12Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 3)
)
_SnICX6430C12BaseFamily_ObjectIdentity = ObjectIdentity
snICX6430C12BaseFamily = _SnICX6430C12BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 3, 1)
)
_SnICX6430C12_ObjectIdentity = ObjectIdentity
snICX6430C12 = _SnICX6430C12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 3, 1, 1)
)
_SnICX6430C12Switch_ObjectIdentity = ObjectIdentity
snICX6430C12Switch = _SnICX6430C12Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 57, 3, 1, 1, 1)
)
_SnICX6450Family_ObjectIdentity = ObjectIdentity
snICX6450Family = _SnICX6450Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58)
)
_SnICX645024Family_ObjectIdentity = ObjectIdentity
snICX645024Family = _SnICX645024Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1)
)
_SnICX645024BaseFamily_ObjectIdentity = ObjectIdentity
snICX645024BaseFamily = _SnICX645024BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1, 1)
)
_SnICX645024_ObjectIdentity = ObjectIdentity
snICX645024 = _SnICX645024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1, 1, 1)
)
_SnICX645024Switch_ObjectIdentity = ObjectIdentity
snICX645024Switch = _SnICX645024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1, 1, 1, 1)
)
_SnICX645024BaseL3Router_ObjectIdentity = ObjectIdentity
snICX645024BaseL3Router = _SnICX645024BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1, 1, 1, 2)
)
_SnICX645024Router_ObjectIdentity = ObjectIdentity
snICX645024Router = _SnICX645024Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1, 1, 1, 3)
)
_SnICX645024PRouter_ObjectIdentity = ObjectIdentity
snICX645024PRouter = _SnICX645024PRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1, 1, 1, 4)
)
_SnICX645024HPOEFamily_ObjectIdentity = ObjectIdentity
snICX645024HPOEFamily = _SnICX645024HPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1, 2)
)
_SnICX645024HPOE_ObjectIdentity = ObjectIdentity
snICX645024HPOE = _SnICX645024HPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1, 2, 1)
)
_SnICX645024HPOESwitch_ObjectIdentity = ObjectIdentity
snICX645024HPOESwitch = _SnICX645024HPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1, 2, 1, 1)
)
_SnICX645024HPOEBaseL3Router_ObjectIdentity = ObjectIdentity
snICX645024HPOEBaseL3Router = _SnICX645024HPOEBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1, 2, 1, 2)
)
_SnICX645024HPOERouter_ObjectIdentity = ObjectIdentity
snICX645024HPOERouter = _SnICX645024HPOERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1, 2, 1, 3)
)
_SnICX645024HPOEPRouter_ObjectIdentity = ObjectIdentity
snICX645024HPOEPRouter = _SnICX645024HPOEPRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 1, 2, 1, 4)
)
_SnICX645048Family_ObjectIdentity = ObjectIdentity
snICX645048Family = _SnICX645048Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2)
)
_SnICX645048BaseFamily_ObjectIdentity = ObjectIdentity
snICX645048BaseFamily = _SnICX645048BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2, 1)
)
_SnICX645048_ObjectIdentity = ObjectIdentity
snICX645048 = _SnICX645048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2, 1, 1)
)
_SnICX645048Switch_ObjectIdentity = ObjectIdentity
snICX645048Switch = _SnICX645048Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2, 1, 1, 1)
)
_SnICX645048BaseL3Router_ObjectIdentity = ObjectIdentity
snICX645048BaseL3Router = _SnICX645048BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2, 1, 1, 2)
)
_SnICX645048Router_ObjectIdentity = ObjectIdentity
snICX645048Router = _SnICX645048Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2, 1, 1, 3)
)
_SnICX645048PRouter_ObjectIdentity = ObjectIdentity
snICX645048PRouter = _SnICX645048PRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2, 1, 1, 4)
)
_SnICX645048HPOEFamily_ObjectIdentity = ObjectIdentity
snICX645048HPOEFamily = _SnICX645048HPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2, 2)
)
_SnICX645048HPOE_ObjectIdentity = ObjectIdentity
snICX645048HPOE = _SnICX645048HPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2, 2, 1)
)
_SnICX645048HPOESwitch_ObjectIdentity = ObjectIdentity
snICX645048HPOESwitch = _SnICX645048HPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2, 2, 1, 1)
)
_SnICX645048HPOEBaseL3Router_ObjectIdentity = ObjectIdentity
snICX645048HPOEBaseL3Router = _SnICX645048HPOEBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2, 2, 1, 2)
)
_SnICX645048HPOERouter_ObjectIdentity = ObjectIdentity
snICX645048HPOERouter = _SnICX645048HPOERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2, 2, 1, 3)
)
_SnICX645048HPOEPRouter_ObjectIdentity = ObjectIdentity
snICX645048HPOEPRouter = _SnICX645048HPOEPRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 2, 2, 1, 4)
)
_SnICX6450C12PDFamily_ObjectIdentity = ObjectIdentity
snICX6450C12PDFamily = _SnICX6450C12PDFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 3)
)
_SnICX6450C12PDBaseFamily_ObjectIdentity = ObjectIdentity
snICX6450C12PDBaseFamily = _SnICX6450C12PDBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 3, 1)
)
_SnICX6450C12PD_ObjectIdentity = ObjectIdentity
snICX6450C12PD = _SnICX6450C12PD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 3, 1, 1)
)
_SnICX6450C12PDSwitch_ObjectIdentity = ObjectIdentity
snICX6450C12PDSwitch = _SnICX6450C12PDSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 3, 1, 1, 1)
)
_SnICX6450C12PDBaseL3Router_ObjectIdentity = ObjectIdentity
snICX6450C12PDBaseL3Router = _SnICX6450C12PDBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 3, 1, 1, 2)
)
_SnICX6450C12PDRouter_ObjectIdentity = ObjectIdentity
snICX6450C12PDRouter = _SnICX6450C12PDRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 3, 1, 1, 3)
)
_SnICX6450C12PDPRouter_ObjectIdentity = ObjectIdentity
snICX6450C12PDPRouter = _SnICX6450C12PDPRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 58, 3, 1, 1, 4)
)
_SnICX6650Family_ObjectIdentity = ObjectIdentity
snICX6650Family = _SnICX6650Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 59)
)
_SnICX665064Family_ObjectIdentity = ObjectIdentity
snICX665064Family = _SnICX665064Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 59, 1)
)
_SnICX665064BaseFamily_ObjectIdentity = ObjectIdentity
snICX665064BaseFamily = _SnICX665064BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 59, 1, 1)
)
_SnICX665064_ObjectIdentity = ObjectIdentity
snICX665064 = _SnICX665064_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 59, 1, 1, 1)
)
_SnICX665064Switch_ObjectIdentity = ObjectIdentity
snICX665064Switch = _SnICX665064Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 59, 1, 1, 1, 1)
)
_SnICX665064BaseL3Router_ObjectIdentity = ObjectIdentity
snICX665064BaseL3Router = _SnICX665064BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 59, 1, 1, 1, 2)
)
_SnICX665064Router_ObjectIdentity = ObjectIdentity
snICX665064Router = _SnICX665064Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 59, 1, 1, 1, 3)
)
_SnICX7750Family_ObjectIdentity = ObjectIdentity
snICX7750Family = _SnICX7750Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60)
)
_SnICX775048CFamily_ObjectIdentity = ObjectIdentity
snICX775048CFamily = _SnICX775048CFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 1)
)
_SnICX775048CBaseFamily_ObjectIdentity = ObjectIdentity
snICX775048CBaseFamily = _SnICX775048CBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 1, 1)
)
_SnICX775048C_ObjectIdentity = ObjectIdentity
snICX775048C = _SnICX775048C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 1, 1, 1)
)
_SnICX775048CSwitch_ObjectIdentity = ObjectIdentity
snICX775048CSwitch = _SnICX775048CSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 1, 1, 1, 1)
)
_SnICX775048CBaseL3Router_ObjectIdentity = ObjectIdentity
snICX775048CBaseL3Router = _SnICX775048CBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 1, 1, 1, 2)
)
_SnICX775048CRouter_ObjectIdentity = ObjectIdentity
snICX775048CRouter = _SnICX775048CRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 1, 1, 1, 3)
)
_SnICX775048FFamily_ObjectIdentity = ObjectIdentity
snICX775048FFamily = _SnICX775048FFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 2)
)
_SnICX775048FBaseFamily_ObjectIdentity = ObjectIdentity
snICX775048FBaseFamily = _SnICX775048FBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 2, 1)
)
_SnICX775048F_ObjectIdentity = ObjectIdentity
snICX775048F = _SnICX775048F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 2, 1, 1)
)
_SnICX775048FSwitch_ObjectIdentity = ObjectIdentity
snICX775048FSwitch = _SnICX775048FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 2, 1, 1, 1)
)
_SnICX775048FBaseL3Router_ObjectIdentity = ObjectIdentity
snICX775048FBaseL3Router = _SnICX775048FBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 2, 1, 1, 2)
)
_SnICX775048FRouter_ObjectIdentity = ObjectIdentity
snICX775048FRouter = _SnICX775048FRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 2, 1, 1, 3)
)
_SnICX775026QFamily_ObjectIdentity = ObjectIdentity
snICX775026QFamily = _SnICX775026QFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 3)
)
_SnICX775026QBaseFamily_ObjectIdentity = ObjectIdentity
snICX775026QBaseFamily = _SnICX775026QBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 3, 1)
)
_SnICX775026Q_ObjectIdentity = ObjectIdentity
snICX775026Q = _SnICX775026Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 3, 1, 1)
)
_SnICX775026QSwitch_ObjectIdentity = ObjectIdentity
snICX775026QSwitch = _SnICX775026QSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 3, 1, 1, 1)
)
_SnICX775026QBaseL3Router_ObjectIdentity = ObjectIdentity
snICX775026QBaseL3Router = _SnICX775026QBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 3, 1, 1, 2)
)
_SnICX775026QRouter_ObjectIdentity = ObjectIdentity
snICX775026QRouter = _SnICX775026QRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 60, 3, 1, 1, 3)
)
_SnICX7450Family_ObjectIdentity = ObjectIdentity
snICX7450Family = _SnICX7450Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61)
)
_SnICX745024Family_ObjectIdentity = ObjectIdentity
snICX745024Family = _SnICX745024Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 1)
)
_SnICX745024BaseFamily_ObjectIdentity = ObjectIdentity
snICX745024BaseFamily = _SnICX745024BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 1, 1)
)
_SnICX745024_ObjectIdentity = ObjectIdentity
snICX745024 = _SnICX745024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 1, 1, 1)
)
_SnICX745024Switch_ObjectIdentity = ObjectIdentity
snICX745024Switch = _SnICX745024Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 1, 1, 1, 1)
)
_SnICX745024BaseL3Router_ObjectIdentity = ObjectIdentity
snICX745024BaseL3Router = _SnICX745024BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 1, 1, 1, 2)
)
_SnICX745024Router_ObjectIdentity = ObjectIdentity
snICX745024Router = _SnICX745024Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 1, 1, 1, 3)
)
_SnICX745024HPOEFamily_ObjectIdentity = ObjectIdentity
snICX745024HPOEFamily = _SnICX745024HPOEFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 1, 2)
)
_SnICX745024HPOE_ObjectIdentity = ObjectIdentity
snICX745024HPOE = _SnICX745024HPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 1, 2, 1)
)
_SnICX745024HPOESwitch_ObjectIdentity = ObjectIdentity
snICX745024HPOESwitch = _SnICX745024HPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 1, 2, 1, 1)
)
_SnICX745024HPOEBaseL3Router_ObjectIdentity = ObjectIdentity
snICX745024HPOEBaseL3Router = _SnICX745024HPOEBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 1, 2, 1, 2)
)
_SnICX745024HPOERouter_ObjectIdentity = ObjectIdentity
snICX745024HPOERouter = _SnICX745024HPOERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 1, 2, 1, 3)
)
_SnICX745048Family_ObjectIdentity = ObjectIdentity
snICX745048Family = _SnICX745048Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2)
)
_SnICX745048BaseFamily_ObjectIdentity = ObjectIdentity
snICX745048BaseFamily = _SnICX745048BaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 1)
)
_SnICX745048_ObjectIdentity = ObjectIdentity
snICX745048 = _SnICX745048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 1, 1)
)
_SnICX745048Switch_ObjectIdentity = ObjectIdentity
snICX745048Switch = _SnICX745048Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 1, 1, 1)
)
_SnICX745048BaseL3Router_ObjectIdentity = ObjectIdentity
snICX745048BaseL3Router = _SnICX745048BaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 1, 1, 2)
)
_SnICX745048Router_ObjectIdentity = ObjectIdentity
snICX745048Router = _SnICX745048Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 1, 1, 3)
)
_SnICX745048HPOEBaseFamily_ObjectIdentity = ObjectIdentity
snICX745048HPOEBaseFamily = _SnICX745048HPOEBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 2)
)
_SnICX745048HPOE_ObjectIdentity = ObjectIdentity
snICX745048HPOE = _SnICX745048HPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 2, 1)
)
_SnICX745048HPOESwitch_ObjectIdentity = ObjectIdentity
snICX745048HPOESwitch = _SnICX745048HPOESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 2, 1, 1)
)
_SnICX745048HPOEBaseL3Router_ObjectIdentity = ObjectIdentity
snICX745048HPOEBaseL3Router = _SnICX745048HPOEBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 2, 1, 2)
)
_SnICX745048HPOERouter_ObjectIdentity = ObjectIdentity
snICX745048HPOERouter = _SnICX745048HPOERouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 2, 1, 3)
)
_SnICX745048FBaseFamily_ObjectIdentity = ObjectIdentity
snICX745048FBaseFamily = _SnICX745048FBaseFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 3)
)
_SnICX745048F_ObjectIdentity = ObjectIdentity
snICX745048F = _SnICX745048F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 3, 1)
)
_SnICX745048FSwitch_ObjectIdentity = ObjectIdentity
snICX745048FSwitch = _SnICX745048FSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 3, 1, 1)
)
_SnICX745048FBaseL3Router_ObjectIdentity = ObjectIdentity
snICX745048FBaseL3Router = _SnICX745048FBaseL3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 3, 1, 2)
)
_SnICX745048FRouter_ObjectIdentity = ObjectIdentity
snICX745048FRouter = _SnICX745048FRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 3, 61, 2, 3, 1, 3)
)
_EdgeIron_ObjectIdentity = ObjectIdentity
edgeIron = _EdgeIron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 4)
)
_EdgeIronMib_ObjectIdentity = ObjectIdentity
edgeIronMib = _EdgeIronMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 4, 1)
)
_EdgeIronType2_ObjectIdentity = ObjectIdentity
edgeIronType2 = _EdgeIronType2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 5)
)
_EdgeIronType2Mib_ObjectIdentity = ObjectIdentity
edgeIronType2Mib = _EdgeIronType2Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 5, 1)
)
_WirelessAp_ObjectIdentity = ObjectIdentity
wirelessAp = _WirelessAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 6)
)
_WirelessProbe_ObjectIdentity = ObjectIdentity
wirelessProbe = _WirelessProbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 7)
)
_AccessIron_ObjectIdentity = ObjectIdentity
accessIron = _AccessIron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 8)
)
_ServerIronSA_ObjectIdentity = ObjectIdentity
serverIronSA = _ServerIronSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 9)
)
_WirelessApplication_ObjectIdentity = ObjectIdentity
wirelessApplication = _WirelessApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 10)
)
_WirelessLocation_ObjectIdentity = ObjectIdentity
wirelessLocation = _WirelessLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 10, 1)
)
_IronPointMobility_ObjectIdentity = ObjectIdentity
ironPointMobility = _IronPointMobility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 11)
)
_IronPointMC_ObjectIdentity = ObjectIdentity
ironPointMC = _IronPointMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 11, 1)
)
_NetIronMtuCpeFamily_ObjectIdentity = ObjectIdentity
netIronMtuCpeFamily = _NetIronMtuCpeFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 12)
)
_NetIronM2404_ObjectIdentity = ObjectIdentity
netIronM2404 = _NetIronM2404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 12, 1)
)
_IronView_ObjectIdentity = ObjectIdentity
ironView = _IronView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 13)
)
_Platform_ObjectIdentity = ObjectIdentity
platform = _Platform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 14)
)
_IronPointWireless_ObjectIdentity = ObjectIdentity
ironPointWireless = _IronPointWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 15)
)
_IronPointWirelessRFS_ObjectIdentity = ObjectIdentity
ironPointWirelessRFS = _IronPointWirelessRFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 15, 1)
)
_IronPointWirelessAP_ObjectIdentity = ObjectIdentity
ironPointWirelessAP = _IronPointWirelessAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 15, 2)
)
_EthernetAccessSwitchFamily_ObjectIdentity = ObjectIdentity
ethernetAccessSwitchFamily = _EthernetAccessSwitchFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 16)
)
_EthernetAccessSwitchBr6910_ObjectIdentity = ObjectIdentity
ethernetAccessSwitchBr6910 = _EthernetAccessSwitchBr6910_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 16, 1)
)
_Vendors_ObjectIdentity = ObjectIdentity
vendors = _Vendors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 2)
)
_DigitalChina_ObjectIdentity = ObjectIdentity
digitalChina = _DigitalChina_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 2, 1)
)
_Dcrs7504_ObjectIdentity = ObjectIdentity
dcrs7504 = _Dcrs7504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 2, 1, 1)
)
_Dcrs7504Switch_ObjectIdentity = ObjectIdentity
dcrs7504Switch = _Dcrs7504Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 2, 1, 1, 1)
)
_Dcrs7504Router_ObjectIdentity = ObjectIdentity
dcrs7504Router = _Dcrs7504Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 2, 1, 1, 2)
)
_Dcrs7508_ObjectIdentity = ObjectIdentity
dcrs7508 = _Dcrs7508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 2, 1, 2)
)
_Dcrs7508Switch_ObjectIdentity = ObjectIdentity
dcrs7508Switch = _Dcrs7508Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 2, 1, 2, 1)
)
_Dcrs7508Router_ObjectIdentity = ObjectIdentity
dcrs7508Router = _Dcrs7508Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 2, 1, 2, 2)
)
_Dcrs7515_ObjectIdentity = ObjectIdentity
dcrs7515 = _Dcrs7515_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 2, 1, 3)
)
_Dcrs7515Switch_ObjectIdentity = ObjectIdentity
dcrs7515Switch = _Dcrs7515Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 2, 1, 3, 1)
)
_Dcrs7515Router_ObjectIdentity = ObjectIdentity
dcrs7515Router = _Dcrs7515Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 2, 1, 3, 2)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3)
)
_Pwe3_ObjectIdentity = ObjectIdentity
pwe3 = _Pwe3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 1)
)
_L3vpn_ObjectIdentity = ObjectIdentity
l3vpn = _L3vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 2)
)
_Bfd_ObjectIdentity = ObjectIdentity
bfd = _Bfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 3)
)
_VplsRoot_ObjectIdentity = ObjectIdentity
vplsRoot = _VplsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 4)
)
_Bgp4V2Root_ObjectIdentity = ObjectIdentity
bgp4V2Root = _Bgp4V2Root_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    **{"foundry": foundry,
       "snTraps": snTraps,
       "products": products,
       "switch": switch,
       "snChassis": snChassis,
       "snAgentSys": snAgentSys,
       "snSwitch": snSwitch,
       "snL4": snL4,
       "snStack": snStack,
       "snSci": snSci,
       "fdrySntp": fdrySntp,
       "fdryRadius": fdryRadius,
       "fdryTacacs": fdryTacacs,
       "fdryTrap": fdryTrap,
       "brcdSysLog": brcdSysLog,
       "brcdMct": brcdMct,
       "brcdFabric": brcdFabric,
       "brcdQos": brcdQos,
       "brcdIPSec": brcdIPSec,
       "router": router,
       "snIpx": snIpx,
       "snIp": snIp,
       "snRip": snRip,
       "snOspf": snOspf,
       "snDvmrp": snDvmrp,
       "snIgmp": snIgmp,
       "snFsrp": snFsrp,
       "snGblRt": snGblRt,
       "snPim": snPim,
       "snAppleTalk": snAppleTalk,
       "snBgp4": snBgp4,
       "snVrrp": snVrrp,
       "snLoopbackIf": snLoopbackIf,
       "snPOS": snPOS,
       "snMpls": snMpls,
       "fdryAcl": fdryAcl,
       "fdryIpv6": fdryIpv6,
       "registration": registration,
       "snFastIron": snFastIron,
       "snFIWGSwitch": snFIWGSwitch,
       "snFIBBSwitch": snFIBBSwitch,
       "snNetIron": snNetIron,
       "snNIRouter": snNIRouter,
       "snServerIron": snServerIron,
       "snSI": snSI,
       "snSIXL": snSIXL,
       "snSIXLTCS": snSIXLTCS,
       "snTurboIron": snTurboIron,
       "snTISwitch": snTISwitch,
       "snTIRouter": snTIRouter,
       "snTurboIron8": snTurboIron8,
       "snT8Switch": snT8Switch,
       "snT8Router": snT8Router,
       "snT8SI": snT8SI,
       "snT8SIXLG": snT8SIXLG,
       "snBigIron4000": snBigIron4000,
       "snBI4000Switch": snBI4000Switch,
       "snBI4000Router": snBI4000Router,
       "snBI4000SI": snBI4000SI,
       "snBigIron8000": snBigIron8000,
       "snBI8000Switch": snBI8000Switch,
       "snBI8000Router": snBI8000Router,
       "snBI8000SI": snBI8000SI,
       "snFastIron2": snFastIron2,
       "snFI2Switch": snFI2Switch,
       "snFI2Router": snFI2Router,
       "snFastIron2Plus": snFastIron2Plus,
       "snFI2PlusSwitch": snFI2PlusSwitch,
       "snFI2PlusRouter": snFI2PlusRouter,
       "snNetIron400": snNetIron400,
       "snNI400Router": snNI400Router,
       "snNetIron800": snNetIron800,
       "snNI800Router": snNI800Router,
       "snFastIron2GC": snFastIron2GC,
       "snFI2GCSwitch": snFI2GCSwitch,
       "snFI2GCRouter": snFI2GCRouter,
       "snFastIron2PlusGC": snFastIron2PlusGC,
       "snFI2PlusGCSwitch": snFI2PlusGCSwitch,
       "snFI2PlusGCRouter": snFI2PlusGCRouter,
       "snBigIron15000": snBigIron15000,
       "snBI15000Switch": snBI15000Switch,
       "snBI15000Router": snBI15000Router,
       "snBI15000SI": snBI15000SI,
       "snNetIron1500": snNetIron1500,
       "snNI1500Router": snNI1500Router,
       "snFastIron3": snFastIron3,
       "snFI3Switch": snFI3Switch,
       "snFI3Router": snFI3Router,
       "snFastIron3GC": snFastIron3GC,
       "snFI3GCSwitch": snFI3GCSwitch,
       "snFI3GCRouter": snFI3GCRouter,
       "snServerIron400": snServerIron400,
       "snSI400Switch": snSI400Switch,
       "snSI400Router": snSI400Router,
       "snServerIron800": snServerIron800,
       "snSI800Switch": snSI800Switch,
       "snSI800Router": snSI800Router,
       "snServerIron1500": snServerIron1500,
       "snSI1500Switch": snSI1500Switch,
       "snSI1500Router": snSI1500Router,
       "sn4802": sn4802,
       "sn4802Switch": sn4802Switch,
       "sn4802Router": sn4802Router,
       "sn4802SI": sn4802SI,
       "snFastIron400": snFastIron400,
       "snFI400Switch": snFI400Switch,
       "snFI400Router": snFI400Router,
       "snFastIron800": snFastIron800,
       "snFI800Switch": snFI800Switch,
       "snFI800Router": snFI800Router,
       "snFastIron1500": snFastIron1500,
       "snFI1500Switch": snFI1500Switch,
       "snFI1500Router": snFI1500Router,
       "snFES2402": snFES2402,
       "snFES2402Switch": snFES2402Switch,
       "snFES2402Router": snFES2402Router,
       "snFES4802": snFES4802,
       "snFES4802Switch": snFES4802Switch,
       "snFES4802Router": snFES4802Router,
       "snFES9604": snFES9604,
       "snFES9604Switch": snFES9604Switch,
       "snFES9604Router": snFES9604Router,
       "snFES12GCF": snFES12GCF,
       "snFES12GCFSwitch": snFES12GCFSwitch,
       "snFES12GCFRouter": snFES12GCFRouter,
       "snFES2402POE": snFES2402POE,
       "snFES2402POESwitch": snFES2402POESwitch,
       "snFES2402POERouter": snFES2402POERouter,
       "snFES4802POE": snFES4802POE,
       "snFES4802POESwitch": snFES4802POESwitch,
       "snFES4802POERouter": snFES4802POERouter,
       "snNetIron4802": snNetIron4802,
       "snNI4802Switch": snNI4802Switch,
       "snNI4802Router": snNI4802Router,
       "snBigIronMG8": snBigIronMG8,
       "snBIMG8Switch": snBIMG8Switch,
       "snBIMG8Router": snBIMG8Router,
       "snNetIron40G": snNetIron40G,
       "snNI40GRouter": snNI40GRouter,
       "snFESXFamily": snFESXFamily,
       "snFESX424Family": snFESX424Family,
       "snFESX424BaseFamily": snFESX424BaseFamily,
       "snFESX424": snFESX424,
       "snFESX424Switch": snFESX424Switch,
       "snFESX424Router": snFESX424Router,
       "snFESX424Prem": snFESX424Prem,
       "snFESX424PremSwitch": snFESX424PremSwitch,
       "snFESX424PremRouter": snFESX424PremRouter,
       "snFESX424Plus1XGFamily": snFESX424Plus1XGFamily,
       "snFESX424Plus1XG": snFESX424Plus1XG,
       "snFESX424Plus1XGSwitch": snFESX424Plus1XGSwitch,
       "snFESX424Plus1XGRouter": snFESX424Plus1XGRouter,
       "snFESX424Plus1XGPrem": snFESX424Plus1XGPrem,
       "snFESX424Plus1XGPremSwitch": snFESX424Plus1XGPremSwitch,
       "snFESX424Plus1XGPremRouter": snFESX424Plus1XGPremRouter,
       "snFESX424Plus2XGFamily": snFESX424Plus2XGFamily,
       "snFESX424Plus2XG": snFESX424Plus2XG,
       "snFESX424Plus2XGSwitch": snFESX424Plus2XGSwitch,
       "snFESX424Plus2XGRouter": snFESX424Plus2XGRouter,
       "snFESX424Plus2XGPrem": snFESX424Plus2XGPrem,
       "snFESX424Plus2XGPremSwitch": snFESX424Plus2XGPremSwitch,
       "snFESX424Plus2XGPremRouter": snFESX424Plus2XGPremRouter,
       "snFESX448Family": snFESX448Family,
       "snFESX448BaseFamily": snFESX448BaseFamily,
       "snFESX448": snFESX448,
       "snFESX448Switch": snFESX448Switch,
       "snFESX448Router": snFESX448Router,
       "snFESX448Prem": snFESX448Prem,
       "snFESX448PremSwitch": snFESX448PremSwitch,
       "snFESX448PremRouter": snFESX448PremRouter,
       "snFESX448Plus1XGFamily": snFESX448Plus1XGFamily,
       "snFESX448Plus1XG": snFESX448Plus1XG,
       "snFESX448Plus1XGSwitch": snFESX448Plus1XGSwitch,
       "snFESX448Plus1XGRouter": snFESX448Plus1XGRouter,
       "snFESX448Plus1XGPrem": snFESX448Plus1XGPrem,
       "snFESX448Plus1XGPremSwitch": snFESX448Plus1XGPremSwitch,
       "snFESX448Plus1XGPremRouter": snFESX448Plus1XGPremRouter,
       "snFESX448Plus2XGFamily": snFESX448Plus2XGFamily,
       "snFESX448Plus2XG": snFESX448Plus2XG,
       "snFESX448Plus2XGSwitch": snFESX448Plus2XGSwitch,
       "snFESX448Plus2XGRouter": snFESX448Plus2XGRouter,
       "snFESX448Plus2XGPrem": snFESX448Plus2XGPrem,
       "snFESX448Plus2XGPremSwitch": snFESX448Plus2XGPremSwitch,
       "snFESX448Plus2XGPremRouter": snFESX448Plus2XGPremRouter,
       "snFESX424FiberFamily": snFESX424FiberFamily,
       "snFESX424FiberBaseFamily": snFESX424FiberBaseFamily,
       "snFESX424Fiber": snFESX424Fiber,
       "snFESX424FiberSwitch": snFESX424FiberSwitch,
       "snFESX424FiberRouter": snFESX424FiberRouter,
       "snFESX424FiberPrem": snFESX424FiberPrem,
       "snFESX424FiberPremSwitch": snFESX424FiberPremSwitch,
       "snFESX424FiberPremRouter": snFESX424FiberPremRouter,
       "snFESX424FiberPlus1XGFamily": snFESX424FiberPlus1XGFamily,
       "snFESX424FiberPlus1XG": snFESX424FiberPlus1XG,
       "snFESX424FiberPlus1XGSwitch": snFESX424FiberPlus1XGSwitch,
       "snFESX424FiberPlus1XGRouter": snFESX424FiberPlus1XGRouter,
       "snFESX424FiberPlus1XGPrem": snFESX424FiberPlus1XGPrem,
       "snFESX424FiberPlus1XGPremSwitch": snFESX424FiberPlus1XGPremSwitch,
       "snFESX424FiberPlus1XGPremRouter": snFESX424FiberPlus1XGPremRouter,
       "snFESX424FiberPlus2XGFamily": snFESX424FiberPlus2XGFamily,
       "snFESX424FiberPlus2XG": snFESX424FiberPlus2XG,
       "snFESX424FiberPlus2XGSwitch": snFESX424FiberPlus2XGSwitch,
       "snFESX424FiberPlus2XGRouter": snFESX424FiberPlus2XGRouter,
       "snFESX424FiberPlus2XGPrem": snFESX424FiberPlus2XGPrem,
       "snFESX424FiberPlus2XGPremSwitch": snFESX424FiberPlus2XGPremSwitch,
       "snFESX424FiberPlus2XGPremRouter": snFESX424FiberPlus2XGPremRouter,
       "snFESX448FiberFamily": snFESX448FiberFamily,
       "snFESX448FiberBaseFamily": snFESX448FiberBaseFamily,
       "snFESX448Fiber": snFESX448Fiber,
       "snFESX448FiberSwitch": snFESX448FiberSwitch,
       "snFESX448FiberRouter": snFESX448FiberRouter,
       "snFESX448FiberPrem": snFESX448FiberPrem,
       "snFESX448FiberPremSwitch": snFESX448FiberPremSwitch,
       "snFESX448FiberPremRouter": snFESX448FiberPremRouter,
       "snFESX448FiberPlus1XGFamily": snFESX448FiberPlus1XGFamily,
       "snFESX448FiberPlus1XG": snFESX448FiberPlus1XG,
       "snFESX448FiberPlus1XGSwitch": snFESX448FiberPlus1XGSwitch,
       "snFESX448FiberPlus1XGRouter": snFESX448FiberPlus1XGRouter,
       "snFESX448FiberPlus1XGPrem": snFESX448FiberPlus1XGPrem,
       "snFESX448FiberPlus1XGPremSwitch": snFESX448FiberPlus1XGPremSwitch,
       "snFESX448FiberPlus1XGPremRouter": snFESX448FiberPlus1XGPremRouter,
       "snFESX448FiberPlus2XGFamily": snFESX448FiberPlus2XGFamily,
       "snFESX448FiberPlus2XG": snFESX448FiberPlus2XG,
       "snFESX448FiberPlus2XGSwitch": snFESX448FiberPlus2XGSwitch,
       "snFESX448FiberPlus2XGRouter": snFESX448FiberPlus2XGRouter,
       "snFESX448FiberPlus2XGPrem": snFESX448FiberPlus2XGPrem,
       "snFESX448FiberPlus2XGPremSwitch": snFESX448FiberPlus2XGPremSwitch,
       "snFESX448FiberPlus2XGPremRouter": snFESX448FiberPlus2XGPremRouter,
       "snFESX424POEFamily": snFESX424POEFamily,
       "snFESX424POEBaseFamily": snFESX424POEBaseFamily,
       "snFESX424POE": snFESX424POE,
       "snFESX424POESwitch": snFESX424POESwitch,
       "snFESX424POERouter": snFESX424POERouter,
       "snFESX424POEPrem": snFESX424POEPrem,
       "snFESX424POEPremSwitch": snFESX424POEPremSwitch,
       "snFESX424POEPremRouter": snFESX424POEPremRouter,
       "snFESX424POEPlus1XGFamily": snFESX424POEPlus1XGFamily,
       "snFESX424POEPlus1XG": snFESX424POEPlus1XG,
       "snFESX424POEPlus1XGSwitch": snFESX424POEPlus1XGSwitch,
       "snFESX424POEPlus1XGRouter": snFESX424POEPlus1XGRouter,
       "snFESX424POEPlus1XGPrem": snFESX424POEPlus1XGPrem,
       "snFESX424POEPlus1XGPremSwitch": snFESX424POEPlus1XGPremSwitch,
       "snFESX424POEPlus1XGPremRouter": snFESX424POEPlus1XGPremRouter,
       "snFESX424POEPlus2XGFamily": snFESX424POEPlus2XGFamily,
       "snFESX424POEPlus2XG": snFESX424POEPlus2XG,
       "snFESX424POEPlus2XGSwitch": snFESX424POEPlus2XGSwitch,
       "snFESX424POEPlus2XGRouter": snFESX424POEPlus2XGRouter,
       "snFESX424POEPlus2XGPrem": snFESX424POEPlus2XGPrem,
       "snFESX424POEPlus2XGPremSwitch": snFESX424POEPlus2XGPremSwitch,
       "snFESX424POEPlus2XGPremRouter": snFESX424POEPlus2XGPremRouter,
       "snFESX624Family": snFESX624Family,
       "snFESX624BaseFamily": snFESX624BaseFamily,
       "snFESX624": snFESX624,
       "snFESX624Switch": snFESX624Switch,
       "snFESX624Router": snFESX624Router,
       "snFESX624Prem": snFESX624Prem,
       "snFESX624PremSwitch": snFESX624PremSwitch,
       "snFESX624PremRouter": snFESX624PremRouter,
       "snFESX624Prem6Router": snFESX624Prem6Router,
       "snFESX624Plus1XGFamily": snFESX624Plus1XGFamily,
       "snFESX624Plus1XG": snFESX624Plus1XG,
       "snFESX624Plus1XGSwitch": snFESX624Plus1XGSwitch,
       "snFESX624Plus1XGRouter": snFESX624Plus1XGRouter,
       "snFESX624Plus1XGPrem": snFESX624Plus1XGPrem,
       "snFESX624Plus1XGPremSwitch": snFESX624Plus1XGPremSwitch,
       "snFESX624Plus1XGPremRouter": snFESX624Plus1XGPremRouter,
       "snFESX624Plus1XGPrem6Router": snFESX624Plus1XGPrem6Router,
       "snFESX624Plus2XGFamily": snFESX624Plus2XGFamily,
       "snFESX624Plus2XG": snFESX624Plus2XG,
       "snFESX624Plus2XGSwitch": snFESX624Plus2XGSwitch,
       "snFESX624Plus2XGRouter": snFESX624Plus2XGRouter,
       "snFESX624Plus2XGPrem": snFESX624Plus2XGPrem,
       "snFESX624Plus2XGPremSwitch": snFESX624Plus2XGPremSwitch,
       "snFESX624Plus2XGPremRouter": snFESX624Plus2XGPremRouter,
       "snFESX624Plus2XGPrem6Router": snFESX624Plus2XGPrem6Router,
       "snFESX648Family": snFESX648Family,
       "snFESX648BaseFamily": snFESX648BaseFamily,
       "snFESX648": snFESX648,
       "snFESX648Switch": snFESX648Switch,
       "snFESX648Router": snFESX648Router,
       "snFESX648Prem": snFESX648Prem,
       "snFESX648PremSwitch": snFESX648PremSwitch,
       "snFESX648PremRouter": snFESX648PremRouter,
       "snFESX648Prem6Router": snFESX648Prem6Router,
       "snFESX648Plus1XGFamily": snFESX648Plus1XGFamily,
       "snFESX648Plus1XG": snFESX648Plus1XG,
       "snFESX648Plus1XGSwitch": snFESX648Plus1XGSwitch,
       "snFESX648Plus1XGRouter": snFESX648Plus1XGRouter,
       "snFESX648Plus1XGPrem": snFESX648Plus1XGPrem,
       "snFESX648Plus1XGPremSwitch": snFESX648Plus1XGPremSwitch,
       "snFESX648Plus1XGPremRouter": snFESX648Plus1XGPremRouter,
       "snFESX648Plus1XGPrem6Router": snFESX648Plus1XGPrem6Router,
       "snFESX648Plus2XGFamily": snFESX648Plus2XGFamily,
       "snFESX648Plus2XG": snFESX648Plus2XG,
       "snFESX648Plus2XGSwitch": snFESX648Plus2XGSwitch,
       "snFESX648Plus2XGRouter": snFESX648Plus2XGRouter,
       "snFESX648Plus2XGPrem": snFESX648Plus2XGPrem,
       "snFESX648Plus2XGPremSwitch": snFESX648Plus2XGPremSwitch,
       "snFESX648Plus2XGPremRouter": snFESX648Plus2XGPremRouter,
       "snFESX648Plus2XGPrem6Router": snFESX648Plus2XGPrem6Router,
       "snFESX624FiberFamily": snFESX624FiberFamily,
       "snFESX624FiberBaseFamily": snFESX624FiberBaseFamily,
       "snFESX624Fiber": snFESX624Fiber,
       "snFESX624FiberSwitch": snFESX624FiberSwitch,
       "snFESX624FiberRouter": snFESX624FiberRouter,
       "snFESX624FiberPrem": snFESX624FiberPrem,
       "snFESX624FiberPremSwitch": snFESX624FiberPremSwitch,
       "snFESX624FiberPremRouter": snFESX624FiberPremRouter,
       "snFESX624FiberPrem6Router": snFESX624FiberPrem6Router,
       "snFESX624FiberPlus1XGFamily": snFESX624FiberPlus1XGFamily,
       "snFESX624FiberPlus1XG": snFESX624FiberPlus1XG,
       "snFESX624FiberPlus1XGSwitch": snFESX624FiberPlus1XGSwitch,
       "snFESX624FiberPlus1XGRouter": snFESX624FiberPlus1XGRouter,
       "snFESX624FiberPlus1XGPrem": snFESX624FiberPlus1XGPrem,
       "snFESX624FiberPlus1XGPremSwitch": snFESX624FiberPlus1XGPremSwitch,
       "snFESX624FiberPlus1XGPremRouter": snFESX624FiberPlus1XGPremRouter,
       "snFESX624FiberPlus1XGPrem6Router": snFESX624FiberPlus1XGPrem6Router,
       "snFESX624FiberPlus2XGFamily": snFESX624FiberPlus2XGFamily,
       "snFESX624FiberPlus2XG": snFESX624FiberPlus2XG,
       "snFESX624FiberPlus2XGSwitch": snFESX624FiberPlus2XGSwitch,
       "snFESX624FiberPlus2XGRouter": snFESX624FiberPlus2XGRouter,
       "snFESX624FiberPlus2XGPrem": snFESX624FiberPlus2XGPrem,
       "snFESX624FiberPlus2XGPremSwitch": snFESX624FiberPlus2XGPremSwitch,
       "snFESX624FiberPlus2XGPremRouter": snFESX624FiberPlus2XGPremRouter,
       "snFESX624FiberPlus2XGPrem6Router": snFESX624FiberPlus2XGPrem6Router,
       "snFESX648FiberFamily": snFESX648FiberFamily,
       "snFESX648FiberBaseFamily": snFESX648FiberBaseFamily,
       "snFESX648Fiber": snFESX648Fiber,
       "snFESX648FiberSwitch": snFESX648FiberSwitch,
       "snFESX648FiberRouter": snFESX648FiberRouter,
       "snFESX648FiberPrem": snFESX648FiberPrem,
       "snFESX648FiberPremSwitch": snFESX648FiberPremSwitch,
       "snFESX648FiberPremRouter": snFESX648FiberPremRouter,
       "snFESX648FiberPrem6Router": snFESX648FiberPrem6Router,
       "snFESX648FiberPlus1XGFamily": snFESX648FiberPlus1XGFamily,
       "snFESX648FiberPlus1XG": snFESX648FiberPlus1XG,
       "snFESX648FiberPlus1XGSwitch": snFESX648FiberPlus1XGSwitch,
       "snFESX648FiberPlus1XGRouter": snFESX648FiberPlus1XGRouter,
       "snFESX648FiberPlus1XGPrem": snFESX648FiberPlus1XGPrem,
       "snFESX648FiberPlus1XGPremSwitch": snFESX648FiberPlus1XGPremSwitch,
       "snFESX648FiberPlus1XGPremRouter": snFESX648FiberPlus1XGPremRouter,
       "snFESX648FiberPlus1XGPrem6Router": snFESX648FiberPlus1XGPrem6Router,
       "snFESX648FiberPlus2XGFamily": snFESX648FiberPlus2XGFamily,
       "snFESX648FiberPlus2XG": snFESX648FiberPlus2XG,
       "snFESX648FiberPlus2XGSwitch": snFESX648FiberPlus2XGSwitch,
       "snFESX648FiberPlus2XGRouter": snFESX648FiberPlus2XGRouter,
       "snFESX648FiberPlus2XGPrem": snFESX648FiberPlus2XGPrem,
       "snFESX648FiberPlus2XGPremSwitch": snFESX648FiberPlus2XGPremSwitch,
       "snFESX648FiberPlus2XGPremRouter": snFESX648FiberPlus2XGPremRouter,
       "snFESX648FiberPlus2XGPrem6Router": snFESX648FiberPlus2XGPrem6Router,
       "snFESX624POEFamily": snFESX624POEFamily,
       "snFESX624POEBaseFamily": snFESX624POEBaseFamily,
       "snFESX624POE": snFESX624POE,
       "snFESX624POESwitch": snFESX624POESwitch,
       "snFESX624POERouter": snFESX624POERouter,
       "snFESX624POEPrem": snFESX624POEPrem,
       "snFESX624POEPremSwitch": snFESX624POEPremSwitch,
       "snFESX624POEPremRouter": snFESX624POEPremRouter,
       "snFESX624POEPrem6Router": snFESX624POEPrem6Router,
       "snFESX624POEPlus1XGFamily": snFESX624POEPlus1XGFamily,
       "snFESX624POEPlus1XG": snFESX624POEPlus1XG,
       "snFESX624POEPlus1XGSwitch": snFESX624POEPlus1XGSwitch,
       "snFESX624POEPlus1XGRouter": snFESX624POEPlus1XGRouter,
       "snFESX624POEPlus1XGPrem": snFESX624POEPlus1XGPrem,
       "snFESX624POEPlus1XGPremSwitch": snFESX624POEPlus1XGPremSwitch,
       "snFESX624POEPlus1XGPremRouter": snFESX624POEPlus1XGPremRouter,
       "snFESX624POEPlus1XGPrem6Router": snFESX624POEPlus1XGPrem6Router,
       "snFESX624POEPlus2XGFamily": snFESX624POEPlus2XGFamily,
       "snFESX624POEPlus2XG": snFESX624POEPlus2XG,
       "snFESX624POEPlus2XGSwitch": snFESX624POEPlus2XGSwitch,
       "snFESX624POEPlus2XGRouter": snFESX624POEPlus2XGRouter,
       "snFESX624POEPlus2XGPrem": snFESX624POEPlus2XGPrem,
       "snFESX624POEPlus2XGPremSwitch": snFESX624POEPlus2XGPremSwitch,
       "snFESX624POEPlus2XGPremRouter": snFESX624POEPlus2XGPremRouter,
       "snFESX624POEPlus2XGPrem6Router": snFESX624POEPlus2XGPrem6Router,
       "snFESX624EFamily": snFESX624EFamily,
       "snFESX624EBaseFamily": snFESX624EBaseFamily,
       "snFESX624E": snFESX624E,
       "snFESX624ESwitch": snFESX624ESwitch,
       "snFESX624ERouter": snFESX624ERouter,
       "snFESX624EPrem": snFESX624EPrem,
       "snFESX624EPremSwitch": snFESX624EPremSwitch,
       "snFESX624EPremRouter": snFESX624EPremRouter,
       "snFESX624EPrem6Router": snFESX624EPrem6Router,
       "snFESX624EPlus1XGFamily": snFESX624EPlus1XGFamily,
       "snFESX624EPlus1XG": snFESX624EPlus1XG,
       "snFESX624EPlus1XGSwitch": snFESX624EPlus1XGSwitch,
       "snFESX624EPlus1XGRouter": snFESX624EPlus1XGRouter,
       "snFESX624EPlus1XGPrem": snFESX624EPlus1XGPrem,
       "snFESX624EPlus1XGPremSwitch": snFESX624EPlus1XGPremSwitch,
       "snFESX624EPlus1XGPremRouter": snFESX624EPlus1XGPremRouter,
       "snFESX624EPlus1XGPrem6Router": snFESX624EPlus1XGPrem6Router,
       "snFESX624EPlus2XGFamily": snFESX624EPlus2XGFamily,
       "snFESX624EPlus2XG": snFESX624EPlus2XG,
       "snFESX624EPlus2XGSwitch": snFESX624EPlus2XGSwitch,
       "snFESX624EPlus2XGRouter": snFESX624EPlus2XGRouter,
       "snFESX624EPlus2XGPrem": snFESX624EPlus2XGPrem,
       "snFESX624EPlus2XGPremSwitch": snFESX624EPlus2XGPremSwitch,
       "snFESX624EPlus2XGPremRouter": snFESX624EPlus2XGPremRouter,
       "snFESX624EPlus2XGPrem6Router": snFESX624EPlus2XGPrem6Router,
       "snFESX624EFiberFamily": snFESX624EFiberFamily,
       "snFESX624EFiberBaseFamily": snFESX624EFiberBaseFamily,
       "snFESX624EFiber": snFESX624EFiber,
       "snFESX624EFiberSwitch": snFESX624EFiberSwitch,
       "snFESX624EFiberRouter": snFESX624EFiberRouter,
       "snFESX624EFiberPrem": snFESX624EFiberPrem,
       "snFESX624EFiberPremSwitch": snFESX624EFiberPremSwitch,
       "snFESX624EFiberPremRouter": snFESX624EFiberPremRouter,
       "snFESX624EFiberPrem6Router": snFESX624EFiberPrem6Router,
       "snFESX624EFiberPlus1XGFamily": snFESX624EFiberPlus1XGFamily,
       "snFESX624EFiberPlus1XG": snFESX624EFiberPlus1XG,
       "snFESX624EFiberPlus1XGSwitch": snFESX624EFiberPlus1XGSwitch,
       "snFESX624EFiberPlus1XGRouter": snFESX624EFiberPlus1XGRouter,
       "snFESX624EFiberPlus1XGPrem": snFESX624EFiberPlus1XGPrem,
       "snFESX624EFiberPlus1XGPremSwitch": snFESX624EFiberPlus1XGPremSwitch,
       "snFESX624EFiberPlus1XGPremRouter": snFESX624EFiberPlus1XGPremRouter,
       "snFESX624EFiberPlus1XGPrem6Router": snFESX624EFiberPlus1XGPrem6Router,
       "snFESX624EFiberPlus2XGFamily": snFESX624EFiberPlus2XGFamily,
       "snFESX624EFiberPlus2XG": snFESX624EFiberPlus2XG,
       "snFESX624EFiberPlus2XGSwitch": snFESX624EFiberPlus2XGSwitch,
       "snFESX624EFiberPlus2XGRouter": snFESX624EFiberPlus2XGRouter,
       "snFESX624EFiberPlus2XGPrem": snFESX624EFiberPlus2XGPrem,
       "snFESX624EFiberPlus2XGPremSwitch": snFESX624EFiberPlus2XGPremSwitch,
       "snFESX624EFiberPlus2XGPremRouter": snFESX624EFiberPlus2XGPremRouter,
       "snFESX624EFiberPlus2XGPrem6Router": snFESX624EFiberPlus2XGPrem6Router,
       "snFESX648EFamily": snFESX648EFamily,
       "snFESX648EBaseFamily": snFESX648EBaseFamily,
       "snFESX648E": snFESX648E,
       "snFESX648ESwitch": snFESX648ESwitch,
       "snFESX648ERouter": snFESX648ERouter,
       "snFESX648EPrem": snFESX648EPrem,
       "snFESX648EPremSwitch": snFESX648EPremSwitch,
       "snFESX648EPremRouter": snFESX648EPremRouter,
       "snFESX648EPrem6Router": snFESX648EPrem6Router,
       "snFESX648EPlus1XGFamily": snFESX648EPlus1XGFamily,
       "snFESX648EPlus1XG": snFESX648EPlus1XG,
       "snFESX648EPlus1XGSwitch": snFESX648EPlus1XGSwitch,
       "snFESX648EPlus1XGRouter": snFESX648EPlus1XGRouter,
       "snFESX648EPlus1XGPrem": snFESX648EPlus1XGPrem,
       "snFESX648EPlus1XGPremSwitch": snFESX648EPlus1XGPremSwitch,
       "snFESX648EPlus1XGPremRouter": snFESX648EPlus1XGPremRouter,
       "snFESX648EPlus1XGPrem6Router": snFESX648EPlus1XGPrem6Router,
       "snFESX648EPlus2XGFamily": snFESX648EPlus2XGFamily,
       "snFESX648EPlus2XG": snFESX648EPlus2XG,
       "snFESX648EPlus2XGSwitch": snFESX648EPlus2XGSwitch,
       "snFESX648EPlus2XGRouter": snFESX648EPlus2XGRouter,
       "snFESX648EPlus2XGPrem": snFESX648EPlus2XGPrem,
       "snFESX648EPlus2XGPremSwitch": snFESX648EPlus2XGPremSwitch,
       "snFESX648EPlus2XGPremRouter": snFESX648EPlus2XGPremRouter,
       "snFESX648EPlus2XGPrem6Router": snFESX648EPlus2XGPrem6Router,
       "snFWSXFamily": snFWSXFamily,
       "snFWSX424Family": snFWSX424Family,
       "snFWSX424BaseFamily": snFWSX424BaseFamily,
       "snFWSX424": snFWSX424,
       "snFWSX424Switch": snFWSX424Switch,
       "snFWSX424Router": snFWSX424Router,
       "snFWSX424Plus1XGFamily": snFWSX424Plus1XGFamily,
       "snFWSX424Plus1XG": snFWSX424Plus1XG,
       "snFWSX424Plus1XGSwitch": snFWSX424Plus1XGSwitch,
       "snFWSX424Plus1XGRouter": snFWSX424Plus1XGRouter,
       "snFWSX424Plus2XGFamily": snFWSX424Plus2XGFamily,
       "snFWSX424Plus2XG": snFWSX424Plus2XG,
       "snFWSX424Plus2XGSwitch": snFWSX424Plus2XGSwitch,
       "snFWSX424Plus2XGRouter": snFWSX424Plus2XGRouter,
       "snFWSX448Family": snFWSX448Family,
       "snFWSX448BaseFamily": snFWSX448BaseFamily,
       "snFWSX448": snFWSX448,
       "snFWSX448Switch": snFWSX448Switch,
       "snFWSX448Router": snFWSX448Router,
       "snFWSX448Plus1XGFamily": snFWSX448Plus1XGFamily,
       "snFWSX448Plus1XG": snFWSX448Plus1XG,
       "snFWSX448Plus1XGSwitch": snFWSX448Plus1XGSwitch,
       "snFWSX448Plus1XGRouter": snFWSX448Plus1XGRouter,
       "snFWSX448Plus2XGFamily": snFWSX448Plus2XGFamily,
       "snFWSX448Plus2XG": snFWSX448Plus2XG,
       "snFWSX448Plus2XGSwitch": snFWSX448Plus2XGSwitch,
       "snFWSX448Plus2XGRouter": snFWSX448Plus2XGRouter,
       "snFastIronSuperXFamily": snFastIronSuperXFamily,
       "snFastIronSuperX": snFastIronSuperX,
       "snFastIronSuperXSwitch": snFastIronSuperXSwitch,
       "snFastIronSuperXRouter": snFastIronSuperXRouter,
       "snFastIronSuperXBaseL3Switch": snFastIronSuperXBaseL3Switch,
       "snFastIronSuperXPrem": snFastIronSuperXPrem,
       "snFastIronSuperXPremSwitch": snFastIronSuperXPremSwitch,
       "snFastIronSuperXPremRouter": snFastIronSuperXPremRouter,
       "snFastIronSuperXPremBaseL3Switch": snFastIronSuperXPremBaseL3Switch,
       "snFastIronSuperX800": snFastIronSuperX800,
       "snFastIronSuperX800Switch": snFastIronSuperX800Switch,
       "snFastIronSuperX800Router": snFastIronSuperX800Router,
       "snFastIronSuperX800BaseL3Switch": snFastIronSuperX800BaseL3Switch,
       "snFastIronSuperX800Prem": snFastIronSuperX800Prem,
       "snFastIronSuperX800PremSwitch": snFastIronSuperX800PremSwitch,
       "snFastIronSuperX800PremRouter": snFastIronSuperX800PremRouter,
       "snFastIronSuperX800PremBaseL3Switch": snFastIronSuperX800PremBaseL3Switch,
       "snFastIronSuperX1600": snFastIronSuperX1600,
       "snFastIronSuperX1600Switch": snFastIronSuperX1600Switch,
       "snFastIronSuperX1600Router": snFastIronSuperX1600Router,
       "snFastIronSuperX1600BaseL3Switch": snFastIronSuperX1600BaseL3Switch,
       "snFastIronSuperX1600Prem": snFastIronSuperX1600Prem,
       "snFastIronSuperX1600PremSwitch": snFastIronSuperX1600PremSwitch,
       "snFastIronSuperX1600PremRouter": snFastIronSuperX1600PremRouter,
       "snFastIronSuperX1600PremBaseL3Switch": snFastIronSuperX1600PremBaseL3Switch,
       "snFastIronSuperXV6": snFastIronSuperXV6,
       "snFastIronSuperXV6Switch": snFastIronSuperXV6Switch,
       "snFastIronSuperXV6Router": snFastIronSuperXV6Router,
       "snFastIronSuperXV6BaseL3Switch": snFastIronSuperXV6BaseL3Switch,
       "snFastIronSuperXV6Prem": snFastIronSuperXV6Prem,
       "snFastIronSuperXV6PremSwitch": snFastIronSuperXV6PremSwitch,
       "snFastIronSuperXV6PremRouter": snFastIronSuperXV6PremRouter,
       "snFastIronSuperXV6PremBaseL3Switch": snFastIronSuperXV6PremBaseL3Switch,
       "snFastIronSuperXV6Prem6Router": snFastIronSuperXV6Prem6Router,
       "snFastIronSuperX800V6": snFastIronSuperX800V6,
       "snFastIronSuperX800V6Switch": snFastIronSuperX800V6Switch,
       "snFastIronSuperX800V6Router": snFastIronSuperX800V6Router,
       "snFastIronSuperX800V6BaseL3Switch": snFastIronSuperX800V6BaseL3Switch,
       "snFastIronSuperX800V6Prem": snFastIronSuperX800V6Prem,
       "snFastIronSuperX800V6PremSwitch": snFastIronSuperX800V6PremSwitch,
       "snFastIronSuperX800V6PremRouter": snFastIronSuperX800V6PremRouter,
       "snFastIronSuperX800V6PremBaseL3Switch": snFastIronSuperX800V6PremBaseL3Switch,
       "snFastIronSuperX800V6Prem6Router": snFastIronSuperX800V6Prem6Router,
       "snFastIronSuperX1600V6": snFastIronSuperX1600V6,
       "snFastIronSuperX1600V6Switch": snFastIronSuperX1600V6Switch,
       "snFastIronSuperX1600V6Router": snFastIronSuperX1600V6Router,
       "snFastIronSuperX1600V6BaseL3Switch": snFastIronSuperX1600V6BaseL3Switch,
       "snFastIronSuperX1600V6Prem": snFastIronSuperX1600V6Prem,
       "snFastIronSuperX1600V6PremSwitch": snFastIronSuperX1600V6PremSwitch,
       "snFastIronSuperX1600V6PremRouter": snFastIronSuperX1600V6PremRouter,
       "snFastIronSuperX1600V6PremBaseL3Switch": snFastIronSuperX1600V6PremBaseL3Switch,
       "snFastIronSuperX1600V6Prem6Router": snFastIronSuperX1600V6Prem6Router,
       "snBigIronSuperXFamily": snBigIronSuperXFamily,
       "snBigIronSuperX": snBigIronSuperX,
       "snBigIronSuperXSwitch": snBigIronSuperXSwitch,
       "snBigIronSuperXRouter": snBigIronSuperXRouter,
       "snBigIronSuperXBaseL3Switch": snBigIronSuperXBaseL3Switch,
       "snTurboIronSuperXFamily": snTurboIronSuperXFamily,
       "snTurboIronSuperX": snTurboIronSuperX,
       "snTurboIronSuperXSwitch": snTurboIronSuperXSwitch,
       "snTurboIronSuperXRouter": snTurboIronSuperXRouter,
       "snTurboIronSuperXBaseL3Switch": snTurboIronSuperXBaseL3Switch,
       "snTurboIronSuperXPrem": snTurboIronSuperXPrem,
       "snTurboIronSuperXPremSwitch": snTurboIronSuperXPremSwitch,
       "snTurboIronSuperXPremRouter": snTurboIronSuperXPremRouter,
       "snTurboIronSuperXPremBaseL3Switch": snTurboIronSuperXPremBaseL3Switch,
       "snIMRFamily": snIMRFamily,
       "snNetIronIMR": snNetIronIMR,
       "snNIIMRRouter": snNIIMRRouter,
       "snBigIronRXFamily": snBigIronRXFamily,
       "snBigIronRX16": snBigIronRX16,
       "snBIRX16Switch": snBIRX16Switch,
       "snBIRX16Router": snBIRX16Router,
       "snBigIronRX8": snBigIronRX8,
       "snBIRX8Switch": snBIRX8Switch,
       "snBIRX8Router": snBIRX8Router,
       "snBigIronRX4": snBigIronRX4,
       "snBIRX4Switch": snBIRX4Switch,
       "snBIRX4Router": snBIRX4Router,
       "snBigIronRX32": snBigIronRX32,
       "snBIRX32Switch": snBIRX32Switch,
       "snBIRX32Router": snBIRX32Router,
       "snNetIronXMRFamily": snNetIronXMRFamily,
       "snNetIronXMR16000": snNetIronXMR16000,
       "snNIXMR16000Router": snNIXMR16000Router,
       "snNetIronXMR8000": snNetIronXMR8000,
       "snNIXMR8000Router": snNIXMR8000Router,
       "snNetIronXMR4000": snNetIronXMR4000,
       "snNIXMR4000Router": snNIXMR4000Router,
       "snNetIronXMR32000": snNetIronXMR32000,
       "snNIXMR32000Router": snNIXMR32000Router,
       "snSecureIronFamily": snSecureIronFamily,
       "snSecureIronLSFamily": snSecureIronLSFamily,
       "snSecureIronLS100": snSecureIronLS100,
       "snSecureIronLS100Switch": snSecureIronLS100Switch,
       "snSecureIronLS100Router": snSecureIronLS100Router,
       "snSecureIronLS300": snSecureIronLS300,
       "snSecureIronLS300Switch": snSecureIronLS300Switch,
       "snSecureIronLS300Router": snSecureIronLS300Router,
       "snSecureIronTMFamily": snSecureIronTMFamily,
       "snSecureIronTM100": snSecureIronTM100,
       "snSecureIronTM100Switch": snSecureIronTM100Switch,
       "snSecureIronTM100Router": snSecureIronTM100Router,
       "snSecureIronTM300": snSecureIronTM300,
       "snSecureIronTM300Switch": snSecureIronTM300Switch,
       "snSecureIronTM300Router": snSecureIronTM300Router,
       "snNetIronMLXFamily": snNetIronMLXFamily,
       "snNetIronMLX16": snNetIronMLX16,
       "snNetIronMLX16Router": snNetIronMLX16Router,
       "snNetIronMLX8": snNetIronMLX8,
       "snNetIronMLX8Router": snNetIronMLX8Router,
       "snNetIronMLX4": snNetIronMLX4,
       "snNetIronMLX4Router": snNetIronMLX4Router,
       "snNetIronMLX32": snNetIronMLX32,
       "snNetIronMLX32Router": snNetIronMLX32Router,
       "snFGSFamily": snFGSFamily,
       "snFGS624Family": snFGS624Family,
       "snFGS624PBaseFamily": snFGS624PBaseFamily,
       "snFGS624P": snFGS624P,
       "snFGS624PSwitch": snFGS624PSwitch,
       "snFGS624PRouter": snFGS624PRouter,
       "snFGS624XGPFamily": snFGS624XGPFamily,
       "snFGS624XGP": snFGS624XGP,
       "snFGS624XGPSwitch": snFGS624XGPSwitch,
       "snFGS624XGPRouter": snFGS624XGPRouter,
       "snFGS624PPOEFamily": snFGS624PPOEFamily,
       "snFGS624PPOE": snFGS624PPOE,
       "snFGS624PPOESwitch": snFGS624PPOESwitch,
       "snFGS624PPOERouter": snFGS624PPOERouter,
       "snFGS624XGPPOEFamily": snFGS624XGPPOEFamily,
       "snFGS624XGPPOE": snFGS624XGPPOE,
       "snFGS624XGPPOESwitch": snFGS624XGPPOESwitch,
       "snFGS624XGPPOERouter": snFGS624XGPPOERouter,
       "snFGS648Family": snFGS648Family,
       "snFGS648PBaseFamily": snFGS648PBaseFamily,
       "snFGS648P": snFGS648P,
       "snFGS648PSwitch": snFGS648PSwitch,
       "snFGS648PRouter": snFGS648PRouter,
       "snFGS648PPOEFamily": snFGS648PPOEFamily,
       "snFGS648PPOE": snFGS648PPOE,
       "snFGS648PPOESwitch": snFGS648PPOESwitch,
       "snFGS648PPOERouter": snFGS648PPOERouter,
       "snFLSFamily": snFLSFamily,
       "snFLS624Family": snFLS624Family,
       "snFLS624BaseFamily": snFLS624BaseFamily,
       "snFLS624": snFLS624,
       "snFLS624Switch": snFLS624Switch,
       "snFLS624Router": snFLS624Router,
       "snFLS648Family": snFLS648Family,
       "snFLS648BaseFamily": snFLS648BaseFamily,
       "snFLS648": snFLS648,
       "snFLS648Switch": snFLS648Switch,
       "snFLS648Router": snFLS648Router,
       "snSIFamily": snSIFamily,
       "snSI100": snSI100,
       "snSI100Switch": snSI100Switch,
       "snSI100Router": snSI100Router,
       "snSI350": snSI350,
       "snSI350Switch": snSI350Switch,
       "snSI350Router": snSI350Router,
       "snSI450": snSI450,
       "snSI450Switch": snSI450Switch,
       "snSI450Router": snSI450Router,
       "snSI850": snSI850,
       "snSI850Switch": snSI850Switch,
       "snSI850Router": snSI850Router,
       "snSI350Plus": snSI350Plus,
       "snSI350PlusSwitch": snSI350PlusSwitch,
       "snSI350PlusRouter": snSI350PlusRouter,
       "snSI450Plus": snSI450Plus,
       "snSI450PlusSwitch": snSI450PlusSwitch,
       "snSI450PlusRouter": snSI450PlusRouter,
       "snSI850Plus": snSI850Plus,
       "snSI850PlusSwitch": snSI850PlusSwitch,
       "snSI850PlusRouter": snSI850PlusRouter,
       "snServerIronGTc": snServerIronGTc,
       "snServerIronGTcSwitch": snServerIronGTcSwitch,
       "snServerIronGTcRouter": snServerIronGTcRouter,
       "snServerIronGTe": snServerIronGTe,
       "snServerIronGTeSwitch": snServerIronGTeSwitch,
       "snServerIronGTeRouter": snServerIronGTeRouter,
       "snServerIronGTePlus": snServerIronGTePlus,
       "snServerIronGTePlusSwitch": snServerIronGTePlusSwitch,
       "snServerIronGTePlusRouter": snServerIronGTePlusRouter,
       "snServerIron4G": snServerIron4G,
       "snServerIron4GSwitch": snServerIron4GSwitch,
       "snServerIron4GRouter": snServerIron4GRouter,
       "serverIronAdx1000": serverIronAdx1000,
       "serverIronAdx1000Switch": serverIronAdx1000Switch,
       "serverIronAdx1000Router": serverIronAdx1000Router,
       "serverIronAdx1000Ssl": serverIronAdx1000Ssl,
       "serverIronAdx1000SslSwitch": serverIronAdx1000SslSwitch,
       "serverIronAdx1000SslRouter": serverIronAdx1000SslRouter,
       "serverIronAdx4000": serverIronAdx4000,
       "serverIronAdx4000Switch": serverIronAdx4000Switch,
       "serverIronAdx4000Router": serverIronAdx4000Router,
       "serverIronAdx4000Ssl": serverIronAdx4000Ssl,
       "serverIronAdx4000SslSwitch": serverIronAdx4000SslSwitch,
       "serverIronAdx4000SslRouter": serverIronAdx4000SslRouter,
       "serverIronAdx8000": serverIronAdx8000,
       "serverIronAdx8000Switch": serverIronAdx8000Switch,
       "serverIronAdx8000Router": serverIronAdx8000Router,
       "serverIronAdx8000Ssl": serverIronAdx8000Ssl,
       "serverIronAdx8000SslSwitch": serverIronAdx8000SslSwitch,
       "serverIronAdx8000SslRouter": serverIronAdx8000SslRouter,
       "serverIronAdx10000": serverIronAdx10000,
       "serverIronAdx10000Switch": serverIronAdx10000Switch,
       "serverIronAdx10000Router": serverIronAdx10000Router,
       "serverIronAdx10000Ssl": serverIronAdx10000Ssl,
       "serverIronAdx10000SslSwitch": serverIronAdx10000SslSwitch,
       "serverIronAdx10000SslRouter": serverIronAdx10000SslRouter,
       "snFastIronStackFamily": snFastIronStackFamily,
       "snFastIronStack": snFastIronStack,
       "snFastIronStackSwitch": snFastIronStackSwitch,
       "snFastIronStackRouter": snFastIronStackRouter,
       "snFastIronStackFCX": snFastIronStackFCX,
       "snFastIronStackFCXSwitch": snFastIronStackFCXSwitch,
       "snFastIronStackFCXBaseL3Router": snFastIronStackFCXBaseL3Router,
       "snFastIronStackFCXRouter": snFastIronStackFCXRouter,
       "snFastIronStackFCXAdvRouter": snFastIronStackFCXAdvRouter,
       "snFastIronStackICX6610": snFastIronStackICX6610,
       "snFastIronStackICX6610Switch": snFastIronStackICX6610Switch,
       "snFastIronStackICX6610BaseL3Router": snFastIronStackICX6610BaseL3Router,
       "snFastIronStackICX6610Router": snFastIronStackICX6610Router,
       "snFastIronStackICX6610PRouter": snFastIronStackICX6610PRouter,
       "snFastIronStackICX6610ARouter": snFastIronStackICX6610ARouter,
       "snFastIronStackICX6430": snFastIronStackICX6430,
       "snFastIronStackICX6430Switch": snFastIronStackICX6430Switch,
       "snFastIronStackICX6450": snFastIronStackICX6450,
       "snFastIronStackICX6450Switch": snFastIronStackICX6450Switch,
       "snFastIronStackICX6450BaseL3Router": snFastIronStackICX6450BaseL3Router,
       "snFastIronStackICX6450Router": snFastIronStackICX6450Router,
       "snFastIronStackICX6450PRouter": snFastIronStackICX6450PRouter,
       "snFastIronStackMixedStack": snFastIronStackMixedStack,
       "snFastIronStackMixedStackSwitch": snFastIronStackMixedStackSwitch,
       "snFastIronStackMixedStackBaseL3Router": snFastIronStackMixedStackBaseL3Router,
       "snFastIronStackMixedStackRouter": snFastIronStackMixedStackRouter,
       "snFastIronStackMixedStackPRouter": snFastIronStackMixedStackPRouter,
       "snFastIronStackMixedStackARouter": snFastIronStackMixedStackARouter,
       "snFastIronStackICX7750": snFastIronStackICX7750,
       "snFastIronStackICX7750Switch": snFastIronStackICX7750Switch,
       "snFastIronStackICX7750BaseL3Router": snFastIronStackICX7750BaseL3Router,
       "snFastIronStackICX7750Router": snFastIronStackICX7750Router,
       "snFastIronStackICX7450": snFastIronStackICX7450,
       "snFastIronStackICX7450Switch": snFastIronStackICX7450Switch,
       "snFastIronStackICX7450BaseL3Router": snFastIronStackICX7450BaseL3Router,
       "snFastIronStackICX7450Router": snFastIronStackICX7450Router,
       "snCes2000Family": snCes2000Family,
       "snCes2024F": snCes2024F,
       "snCes2024C": snCes2024C,
       "snCes2048F": snCes2048F,
       "snCes2048C": snCes2048C,
       "snCes2048FX": snCes2048FX,
       "snCes2048CX": snCes2048CX,
       "snCes2024F4X": snCes2024F4X,
       "snCes2024C4X": snCes2024C4X,
       "snFLSLCFamily": snFLSLCFamily,
       "snFLSLC624Family": snFLSLC624Family,
       "snFLSLC624BaseFamily": snFLSLC624BaseFamily,
       "snFLSLC624": snFLSLC624,
       "snFLSLC624Switch": snFLSLC624Switch,
       "snFLSLC624Router": snFLSLC624Router,
       "snFLSLC624POEFamily": snFLSLC624POEFamily,
       "snFLSLC624POE": snFLSLC624POE,
       "snFLSLC624POESwitch": snFLSLC624POESwitch,
       "snFLSLC624POERouter": snFLSLC624POERouter,
       "snFLSLC648Family": snFLSLC648Family,
       "snFLSLC648BaseFamily": snFLSLC648BaseFamily,
       "snFLSLC648": snFLSLC648,
       "snFLSLC648Switch": snFLSLC648Switch,
       "snFLSLC648Router": snFLSLC648Router,
       "snFLSLC648POEFamily": snFLSLC648POEFamily,
       "snFLSLC648POE": snFLSLC648POE,
       "snFLSLC648POESwitch": snFLSLC648POESwitch,
       "snFLSLC648POERouter": snFLSLC648POERouter,
       "snCer2000Family": snCer2000Family,
       "snCer2024F": snCer2024F,
       "snCer2024C": snCer2024C,
       "snCer2048F": snCer2048F,
       "snCer2048C": snCer2048C,
       "snCer2048FX": snCer2048FX,
       "snCer2048CX": snCer2048CX,
       "snCer2024F4X": snCer2024F4X,
       "snCer2024C4X": snCer2024C4X,
       "snFWSFamily": snFWSFamily,
       "snFWS624Family": snFWS624Family,
       "snFWS624BaseFamily": snFWS624BaseFamily,
       "snFWS624": snFWS624,
       "snFWS624Switch": snFWS624Switch,
       "snFWS624BaseL3Router": snFWS624BaseL3Router,
       "snFWS624EdgePremRouter": snFWS624EdgePremRouter,
       "snFWS624GFamily": snFWS624GFamily,
       "snFWS624G": snFWS624G,
       "snFWS624GSwitch": snFWS624GSwitch,
       "snFWS624GBaseL3Router": snFWS624GBaseL3Router,
       "snFWS624GEdgePremRouter": snFWS624GEdgePremRouter,
       "snFWS624POEFamily": snFWS624POEFamily,
       "snFWS624POE": snFWS624POE,
       "snFWS624POESwitch": snFWS624POESwitch,
       "snFWS624POEBaseL3Router": snFWS624POEBaseL3Router,
       "snFWS624POEEdgePremRouter": snFWS624POEEdgePremRouter,
       "snFWS624GPOEFamily": snFWS624GPOEFamily,
       "snFWS624GPOE": snFWS624GPOE,
       "snFWS624GPOESwitch": snFWS624GPOESwitch,
       "snFWS624GPOEBaseL3Router": snFWS624GPOEBaseL3Router,
       "snFWS624GPOEEdgePremRouter": snFWS624GPOEEdgePremRouter,
       "snFWS648Family": snFWS648Family,
       "snFWS648BaseFamily": snFWS648BaseFamily,
       "snFWS648": snFWS648,
       "snFWS648Switch": snFWS648Switch,
       "snFWS648BaseL3Router": snFWS648BaseL3Router,
       "snFWS648EdgePremRouter": snFWS648EdgePremRouter,
       "snFWS648GFamily": snFWS648GFamily,
       "snFWS648G": snFWS648G,
       "snFWS648GSwitch": snFWS648GSwitch,
       "snFWS648GBaseL3Router": snFWS648GBaseL3Router,
       "snFWS648GEdgePremRouter": snFWS648GEdgePremRouter,
       "snFWS648POEFamily": snFWS648POEFamily,
       "snFWS648POE": snFWS648POE,
       "snFWS648POESwitch": snFWS648POESwitch,
       "snFWS648POEBaseL3Router": snFWS648POEBaseL3Router,
       "snFWS648POEEdgePremRouter": snFWS648POEEdgePremRouter,
       "snFWS648GPOEFamily": snFWS648GPOEFamily,
       "snFWS648GPOE": snFWS648GPOE,
       "snFWS648GPOESwitch": snFWS648GPOESwitch,
       "snFWS648GPOEBaseL3Router": snFWS648GPOEBaseL3Router,
       "snFWS648GPOEEdgePremRouter": snFWS648GPOEEdgePremRouter,
       "snTurboIron2": snTurboIron2,
       "snTI2X24Family": snTI2X24Family,
       "snTI2X24Switch": snTI2X24Switch,
       "snTI2X24Router": snTI2X24Router,
       "snTI2X48Family": snTI2X48Family,
       "snTI2X48Switch": snTI2X48Switch,
       "snTI2X48Router": snTI2X48Router,
       "snFCXFamily": snFCXFamily,
       "snFCX624Family": snFCX624Family,
       "snFCX624SBaseFamily": snFCX624SBaseFamily,
       "snFCX624S": snFCX624S,
       "snFCX624SSwitch": snFCX624SSwitch,
       "snFCX624SBaseL3Router": snFCX624SBaseL3Router,
       "snFCX624SRouter": snFCX624SRouter,
       "snFCX624SAdvRouter": snFCX624SAdvRouter,
       "snFCX624SHPOEFamily": snFCX624SHPOEFamily,
       "snFCX624SHPOE": snFCX624SHPOE,
       "snFCX624SHPOESwitch": snFCX624SHPOESwitch,
       "snFCX624SHPOEBaseL3Router": snFCX624SHPOEBaseL3Router,
       "snFCX624SHPOERouter": snFCX624SHPOERouter,
       "snFCX624SHPOEAdvRouter": snFCX624SHPOEAdvRouter,
       "snFCX624SFFamily": snFCX624SFFamily,
       "snFCX624SF": snFCX624SF,
       "snFCX624SFSwitch": snFCX624SFSwitch,
       "snFCX624SFBaseL3Router": snFCX624SFBaseL3Router,
       "snFCX624SFRouter": snFCX624SFRouter,
       "snFCX624SFAdvRouter": snFCX624SFAdvRouter,
       "snFCX624BaseFamily": snFCX624BaseFamily,
       "snFCX624": snFCX624,
       "snFCX624Switch": snFCX624Switch,
       "snFCX624BaseL3Router": snFCX624BaseL3Router,
       "snFCX624Router": snFCX624Router,
       "snFCX624AdvRouter": snFCX624AdvRouter,
       "snFCX648Family": snFCX648Family,
       "snFCX648SBaseFamily": snFCX648SBaseFamily,
       "snFCX648S": snFCX648S,
       "snFCX648SSwitch": snFCX648SSwitch,
       "snFCX648SBaseL3Router": snFCX648SBaseL3Router,
       "snFCX648SRouter": snFCX648SRouter,
       "snFCX648SAdvRouter": snFCX648SAdvRouter,
       "snFCX648SHPOEFamily": snFCX648SHPOEFamily,
       "snFCX648SHPOE": snFCX648SHPOE,
       "snFCX648SHPOESwitch": snFCX648SHPOESwitch,
       "snFCX648SHPOEBaseL3Router": snFCX648SHPOEBaseL3Router,
       "snFCX648SHPOERouter": snFCX648SHPOERouter,
       "snFCX648SHPOEAdvRouter": snFCX648SHPOEAdvRouter,
       "snFCX648BaseFamily": snFCX648BaseFamily,
       "snFCX648": snFCX648,
       "snFCX648Switch": snFCX648Switch,
       "snFCX648BaseL3Router": snFCX648BaseL3Router,
       "snFCX648Router": snFCX648Router,
       "snFCX648AdvRouter": snFCX648AdvRouter,
       "snBrocadeMLXeFamily": snBrocadeMLXeFamily,
       "snBrocadeMLXe16": snBrocadeMLXe16,
       "snBrocadeMLXe16Router": snBrocadeMLXe16Router,
       "snBrocadeMLXe8": snBrocadeMLXe8,
       "snBrocadeMLXe8Router": snBrocadeMLXe8Router,
       "snBrocadeMLXe4": snBrocadeMLXe4,
       "snBrocadeMLXe4Router": snBrocadeMLXe4Router,
       "snBrocadeMLXe32": snBrocadeMLXe32,
       "snBrocadeMLXe32Router": snBrocadeMLXe32Router,
       "snICX6610Family": snICX6610Family,
       "snICX661024Family": snICX661024Family,
       "snICX661024BaseFamily": snICX661024BaseFamily,
       "snICX661024": snICX661024,
       "snICX661024Switch": snICX661024Switch,
       "snICX661024BaseL3Router": snICX661024BaseL3Router,
       "snICX661024Router": snICX661024Router,
       "snICX661024PRouter": snICX661024PRouter,
       "snICX661024ARouter": snICX661024ARouter,
       "snICX661024HPOEFamily": snICX661024HPOEFamily,
       "snICX661024HPOE": snICX661024HPOE,
       "snICX661024HPOESwitch": snICX661024HPOESwitch,
       "snICX661024HPOEBaseL3Router": snICX661024HPOEBaseL3Router,
       "snICX661024HPOERouter": snICX661024HPOERouter,
       "snICX661024HPOEPRouter": snICX661024HPOEPRouter,
       "snICX661024HPOEARouter": snICX661024HPOEARouter,
       "snICX661024FFamily": snICX661024FFamily,
       "snICX661024F": snICX661024F,
       "snICX661024FSwitch": snICX661024FSwitch,
       "snICX661024FBaseL3Router": snICX661024FBaseL3Router,
       "snICX661024FRouter": snICX661024FRouter,
       "snICX661024FPRouter": snICX661024FPRouter,
       "snICX661024FARouter": snICX661024FARouter,
       "snICX661048Family": snICX661048Family,
       "snICX661048BaseFamily": snICX661048BaseFamily,
       "snICX661048": snICX661048,
       "snICX661048Switch": snICX661048Switch,
       "snICX661048BaseL3Router": snICX661048BaseL3Router,
       "snICX661048Router": snICX661048Router,
       "snICX661048PRouter": snICX661048PRouter,
       "snICX661048ARouter": snICX661048ARouter,
       "snICX661048HPOEFamily": snICX661048HPOEFamily,
       "snICX661048HPOE": snICX661048HPOE,
       "snICX661048HPOESwitch": snICX661048HPOESwitch,
       "snICX661048HPOEBaseL3Router": snICX661048HPOEBaseL3Router,
       "snICX661048HPOERouter": snICX661048HPOERouter,
       "snICX661048HPOEPRouter": snICX661048HPOEPRouter,
       "snICX661048HPOEARouter": snICX661048HPOEARouter,
       "snICX6430Family": snICX6430Family,
       "snICX643024Family": snICX643024Family,
       "snICX643024BaseFamily": snICX643024BaseFamily,
       "snICX643024": snICX643024,
       "snICX643024Switch": snICX643024Switch,
       "snICX643024HPOEFamily": snICX643024HPOEFamily,
       "snICX643024HPOE": snICX643024HPOE,
       "snICX643024HPOESwitch": snICX643024HPOESwitch,
       "snICX643048Family": snICX643048Family,
       "snICX643048BaseFamily": snICX643048BaseFamily,
       "snICX643048": snICX643048,
       "snICX643048Switch": snICX643048Switch,
       "snICX643048HPOEFamily": snICX643048HPOEFamily,
       "snICX643048HPOE": snICX643048HPOE,
       "snICX643048HPOESwitch": snICX643048HPOESwitch,
       "snICX6430C12Family": snICX6430C12Family,
       "snICX6430C12BaseFamily": snICX6430C12BaseFamily,
       "snICX6430C12": snICX6430C12,
       "snICX6430C12Switch": snICX6430C12Switch,
       "snICX6450Family": snICX6450Family,
       "snICX645024Family": snICX645024Family,
       "snICX645024BaseFamily": snICX645024BaseFamily,
       "snICX645024": snICX645024,
       "snICX645024Switch": snICX645024Switch,
       "snICX645024BaseL3Router": snICX645024BaseL3Router,
       "snICX645024Router": snICX645024Router,
       "snICX645024PRouter": snICX645024PRouter,
       "snICX645024HPOEFamily": snICX645024HPOEFamily,
       "snICX645024HPOE": snICX645024HPOE,
       "snICX645024HPOESwitch": snICX645024HPOESwitch,
       "snICX645024HPOEBaseL3Router": snICX645024HPOEBaseL3Router,
       "snICX645024HPOERouter": snICX645024HPOERouter,
       "snICX645024HPOEPRouter": snICX645024HPOEPRouter,
       "snICX645048Family": snICX645048Family,
       "snICX645048BaseFamily": snICX645048BaseFamily,
       "snICX645048": snICX645048,
       "snICX645048Switch": snICX645048Switch,
       "snICX645048BaseL3Router": snICX645048BaseL3Router,
       "snICX645048Router": snICX645048Router,
       "snICX645048PRouter": snICX645048PRouter,
       "snICX645048HPOEFamily": snICX645048HPOEFamily,
       "snICX645048HPOE": snICX645048HPOE,
       "snICX645048HPOESwitch": snICX645048HPOESwitch,
       "snICX645048HPOEBaseL3Router": snICX645048HPOEBaseL3Router,
       "snICX645048HPOERouter": snICX645048HPOERouter,
       "snICX645048HPOEPRouter": snICX645048HPOEPRouter,
       "snICX6450C12PDFamily": snICX6450C12PDFamily,
       "snICX6450C12PDBaseFamily": snICX6450C12PDBaseFamily,
       "snICX6450C12PD": snICX6450C12PD,
       "snICX6450C12PDSwitch": snICX6450C12PDSwitch,
       "snICX6450C12PDBaseL3Router": snICX6450C12PDBaseL3Router,
       "snICX6450C12PDRouter": snICX6450C12PDRouter,
       "snICX6450C12PDPRouter": snICX6450C12PDPRouter,
       "snICX6650Family": snICX6650Family,
       "snICX665064Family": snICX665064Family,
       "snICX665064BaseFamily": snICX665064BaseFamily,
       "snICX665064": snICX665064,
       "snICX665064Switch": snICX665064Switch,
       "snICX665064BaseL3Router": snICX665064BaseL3Router,
       "snICX665064Router": snICX665064Router,
       "snICX7750Family": snICX7750Family,
       "snICX775048CFamily": snICX775048CFamily,
       "snICX775048CBaseFamily": snICX775048CBaseFamily,
       "snICX775048C": snICX775048C,
       "snICX775048CSwitch": snICX775048CSwitch,
       "snICX775048CBaseL3Router": snICX775048CBaseL3Router,
       "snICX775048CRouter": snICX775048CRouter,
       "snICX775048FFamily": snICX775048FFamily,
       "snICX775048FBaseFamily": snICX775048FBaseFamily,
       "snICX775048F": snICX775048F,
       "snICX775048FSwitch": snICX775048FSwitch,
       "snICX775048FBaseL3Router": snICX775048FBaseL3Router,
       "snICX775048FRouter": snICX775048FRouter,
       "snICX775026QFamily": snICX775026QFamily,
       "snICX775026QBaseFamily": snICX775026QBaseFamily,
       "snICX775026Q": snICX775026Q,
       "snICX775026QSwitch": snICX775026QSwitch,
       "snICX775026QBaseL3Router": snICX775026QBaseL3Router,
       "snICX775026QRouter": snICX775026QRouter,
       "snICX7450Family": snICX7450Family,
       "snICX745024Family": snICX745024Family,
       "snICX745024BaseFamily": snICX745024BaseFamily,
       "snICX745024": snICX745024,
       "snICX745024Switch": snICX745024Switch,
       "snICX745024BaseL3Router": snICX745024BaseL3Router,
       "snICX745024Router": snICX745024Router,
       "snICX745024HPOEFamily": snICX745024HPOEFamily,
       "snICX745024HPOE": snICX745024HPOE,
       "snICX745024HPOESwitch": snICX745024HPOESwitch,
       "snICX745024HPOEBaseL3Router": snICX745024HPOEBaseL3Router,
       "snICX745024HPOERouter": snICX745024HPOERouter,
       "snICX745048Family": snICX745048Family,
       "snICX745048BaseFamily": snICX745048BaseFamily,
       "snICX745048": snICX745048,
       "snICX745048Switch": snICX745048Switch,
       "snICX745048BaseL3Router": snICX745048BaseL3Router,
       "snICX745048Router": snICX745048Router,
       "snICX745048HPOEBaseFamily": snICX745048HPOEBaseFamily,
       "snICX745048HPOE": snICX745048HPOE,
       "snICX745048HPOESwitch": snICX745048HPOESwitch,
       "snICX745048HPOEBaseL3Router": snICX745048HPOEBaseL3Router,
       "snICX745048HPOERouter": snICX745048HPOERouter,
       "snICX745048FBaseFamily": snICX745048FBaseFamily,
       "snICX745048F": snICX745048F,
       "snICX745048FSwitch": snICX745048FSwitch,
       "snICX745048FBaseL3Router": snICX745048FBaseL3Router,
       "snICX745048FRouter": snICX745048FRouter,
       "edgeIron": edgeIron,
       "edgeIronMib": edgeIronMib,
       "edgeIronType2": edgeIronType2,
       "edgeIronType2Mib": edgeIronType2Mib,
       "wirelessAp": wirelessAp,
       "wirelessProbe": wirelessProbe,
       "accessIron": accessIron,
       "serverIronSA": serverIronSA,
       "wirelessApplication": wirelessApplication,
       "wirelessLocation": wirelessLocation,
       "ironPointMobility": ironPointMobility,
       "ironPointMC": ironPointMC,
       "netIronMtuCpeFamily": netIronMtuCpeFamily,
       "netIronM2404": netIronM2404,
       "ironView": ironView,
       "platform": platform,
       "ironPointWireless": ironPointWireless,
       "ironPointWirelessRFS": ironPointWirelessRFS,
       "ironPointWirelessAP": ironPointWirelessAP,
       "ethernetAccessSwitchFamily": ethernetAccessSwitchFamily,
       "ethernetAccessSwitchBr6910": ethernetAccessSwitchBr6910,
       "vendors": vendors,
       "digitalChina": digitalChina,
       "dcrs7504": dcrs7504,
       "dcrs7504Switch": dcrs7504Switch,
       "dcrs7504Router": dcrs7504Router,
       "dcrs7508": dcrs7508,
       "dcrs7508Switch": dcrs7508Switch,
       "dcrs7508Router": dcrs7508Router,
       "dcrs7515": dcrs7515,
       "dcrs7515Switch": dcrs7515Switch,
       "dcrs7515Router": dcrs7515Router,
       "experimental": experimental,
       "pwe3": pwe3,
       "l3vpn": l3vpn,
       "bfd": bfd,
       "vplsRoot": vplsRoot,
       "bgp4V2Root": bgp4V2Root}
)
