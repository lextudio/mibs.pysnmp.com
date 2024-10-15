# SNMP MIB module (SMSAGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SMSAGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:39 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Unisys_ObjectIdentity = ObjectIdentity
unisys = _Unisys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223)
)
_UnisysOpen_ObjectIdentity = ObjectIdentity
unisysOpen = _UnisysOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10)
)
_CfgAgent_ObjectIdentity = ObjectIdentity
cfgAgent = _CfgAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 7)
)
_CfgAgentVersion_Type = Integer32
_CfgAgentVersion_Object = MibScalar
cfgAgentVersion = _CfgAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 1),
    _CfgAgentVersion_Type()
)
cfgAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentVersion.setStatus("mandatory")
_CfgAgentRevision_Type = Integer32
_CfgAgentRevision_Object = MibScalar
cfgAgentRevision = _CfgAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 2),
    _CfgAgentRevision_Type()
)
cfgAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentRevision.setStatus("mandatory")
_CfgAgentMIBVersion_Type = Integer32
_CfgAgentMIBVersion_Object = MibScalar
cfgAgentMIBVersion = _CfgAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 3),
    _CfgAgentMIBVersion_Type()
)
cfgAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMIBVersion.setStatus("mandatory")
_CfgAgentMIBRevision_Type = Integer32
_CfgAgentMIBRevision_Object = MibScalar
cfgAgentMIBRevision = _CfgAgentMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 4),
    _CfgAgentMIBRevision_Type()
)
cfgAgentMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMIBRevision.setStatus("mandatory")
_CfgAgentBIOSVendor_Type = DisplayString
_CfgAgentBIOSVendor_Object = MibScalar
cfgAgentBIOSVendor = _CfgAgentBIOSVendor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 5),
    _CfgAgentBIOSVendor_Type()
)
cfgAgentBIOSVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSVendor.setStatus("mandatory")
_CfgAgentBIOSVersion_Type = DisplayString
_CfgAgentBIOSVersion_Object = MibScalar
cfgAgentBIOSVersion = _CfgAgentBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 6),
    _CfgAgentBIOSVersion_Type()
)
cfgAgentBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSVersion.setStatus("mandatory")
_CfgAgentBIOSDate_Type = DisplayString
_CfgAgentBIOSDate_Object = MibScalar
cfgAgentBIOSDate = _CfgAgentBIOSDate_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 7),
    _CfgAgentBIOSDate_Type()
)
cfgAgentBIOSDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSDate.setStatus("mandatory")
_CfgAgentBIOSsROMInKb_Type = Integer32
_CfgAgentBIOSsROMInKb_Object = MibScalar
cfgAgentBIOSsROMInKb = _CfgAgentBIOSsROMInKb_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 8),
    _CfgAgentBIOSsROMInKb_Type()
)
cfgAgentBIOSsROMInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSsROMInKb.setStatus("mandatory")
_CfgAgentBIOSBusSupport_Type = DisplayString
_CfgAgentBIOSBusSupport_Object = MibScalar
cfgAgentBIOSBusSupport = _CfgAgentBIOSBusSupport_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 9),
    _CfgAgentBIOSBusSupport_Type()
)
cfgAgentBIOSBusSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSBusSupport.setStatus("mandatory")
_CfgAgentBIOSAddress_Type = Integer32
_CfgAgentBIOSAddress_Object = MibScalar
cfgAgentBIOSAddress = _CfgAgentBIOSAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 10),
    _CfgAgentBIOSAddress_Type()
)
cfgAgentBIOSAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSAddress.setStatus("mandatory")
_CfgAgentBIOSInterruptId_Type = Integer32
_CfgAgentBIOSInterruptId_Object = MibScalar
cfgAgentBIOSInterruptId = _CfgAgentBIOSInterruptId_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 11),
    _CfgAgentBIOSInterruptId_Type()
)
cfgAgentBIOSInterruptId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSInterruptId.setStatus("mandatory")
_CfgAgentnCPUs_Type = Integer32
_CfgAgentnCPUs_Object = MibScalar
cfgAgentnCPUs = _CfgAgentnCPUs_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 12),
    _CfgAgentnCPUs_Type()
)
cfgAgentnCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnCPUs.setStatus("mandatory")
_CfgAgentCPUsTbl_Object = MibTable
cfgAgentCPUsTbl = _CfgAgentCPUsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13)
)
if mibBuilder.loadTexts:
    cfgAgentCPUsTbl.setStatus("mandatory")
_CfgAgentCPUsTblEntry_Object = MibTableRow
cfgAgentCPUsTblEntry = _CfgAgentCPUsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1)
)
if mibBuilder.loadTexts:
    cfgAgentCPUsTblEntry.setStatus("mandatory")
_CfgAgentCPUClass_Type = DisplayString
_CfgAgentCPUClass_Object = MibTableColumn
cfgAgentCPUClass = _CfgAgentCPUClass_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1, 1),
    _CfgAgentCPUClass_Type()
)
cfgAgentCPUClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCPUClass.setStatus("mandatory")
_CfgAgentCPUName_Type = DisplayString
_CfgAgentCPUName_Object = MibTableColumn
cfgAgentCPUName = _CfgAgentCPUName_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1, 2),
    _CfgAgentCPUName_Type()
)
cfgAgentCPUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCPUName.setStatus("mandatory")
_CfgAgentCPUVendor_Type = DisplayString
_CfgAgentCPUVendor_Object = MibTableColumn
cfgAgentCPUVendor = _CfgAgentCPUVendor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1, 3),
    _CfgAgentCPUVendor_Type()
)
cfgAgentCPUVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCPUVendor.setStatus("mandatory")
_CfgAgentCPUSpeed_Type = Integer32
_CfgAgentCPUSpeed_Object = MibTableColumn
cfgAgentCPUSpeed = _CfgAgentCPUSpeed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1, 4),
    _CfgAgentCPUSpeed_Type()
)
cfgAgentCPUSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCPUSpeed.setStatus("mandatory")
_CfgAgentCPUsCacheInKb_Type = Integer32
_CfgAgentCPUsCacheInKb_Object = MibTableColumn
cfgAgentCPUsCacheInKb = _CfgAgentCPUsCacheInKb_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1, 5),
    _CfgAgentCPUsCacheInKb_Type()
)
cfgAgentCPUsCacheInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCPUsCacheInKb.setStatus("mandatory")


class _CfgAgentCPUState_Type(Integer32):
    """Custom type cfgAgentCPUState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disabled", 2))
    )


_CfgAgentCPUState_Type.__name__ = "Integer32"
_CfgAgentCPUState_Object = MibTableColumn
cfgAgentCPUState = _CfgAgentCPUState_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1, 6),
    _CfgAgentCPUState_Type()
)
cfgAgentCPUState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCPUState.setStatus("mandatory")
_CfgAgentSysName_Type = DisplayString
_CfgAgentSysName_Object = MibScalar
cfgAgentSysName = _CfgAgentSysName_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 14),
    _CfgAgentSysName_Type()
)
cfgAgentSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentSysName.setStatus("mandatory")
_CfgAgentSysBoardVersion_Type = DisplayString
_CfgAgentSysBoardVersion_Object = MibScalar
cfgAgentSysBoardVersion = _CfgAgentSysBoardVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 15),
    _CfgAgentSysBoardVersion_Type()
)
cfgAgentSysBoardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentSysBoardVersion.setStatus("mandatory")
_CfgAgentSysUptimeMilSec_Type = Integer32
_CfgAgentSysUptimeMilSec_Object = MibScalar
cfgAgentSysUptimeMilSec = _CfgAgentSysUptimeMilSec_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 16),
    _CfgAgentSysUptimeMilSec_Type()
)
cfgAgentSysUptimeMilSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentSysUptimeMilSec.setStatus("mandatory")
_CfgAgentSysOS_Type = DisplayString
_CfgAgentSysOS_Object = MibScalar
cfgAgentSysOS = _CfgAgentSysOS_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 17),
    _CfgAgentSysOS_Type()
)
cfgAgentSysOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentSysOS.setStatus("mandatory")
_CfgAgentSysnDMAs_Type = Integer32
_CfgAgentSysnDMAs_Object = MibScalar
cfgAgentSysnDMAs = _CfgAgentSysnDMAs_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 18),
    _CfgAgentSysnDMAs_Type()
)
cfgAgentSysnDMAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentSysnDMAs.setStatus("mandatory")
_CfgAgentnIRQs_Type = Integer32
_CfgAgentnIRQs_Object = MibScalar
cfgAgentnIRQs = _CfgAgentnIRQs_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 19),
    _CfgAgentnIRQs_Type()
)
cfgAgentnIRQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnIRQs.setStatus("mandatory")
_CfgAgentIRQsTbl_Object = MibTable
cfgAgentIRQsTbl = _CfgAgentIRQsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 20)
)
if mibBuilder.loadTexts:
    cfgAgentIRQsTbl.setStatus("mandatory")
_CfgAgentIRQsTblEntry_Object = MibTableRow
cfgAgentIRQsTblEntry = _CfgAgentIRQsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 20, 1)
)
if mibBuilder.loadTexts:
    cfgAgentIRQsTblEntry.setStatus("mandatory")
_CfgAgentIRQ_Type = Integer32
_CfgAgentIRQ_Object = MibTableColumn
cfgAgentIRQ = _CfgAgentIRQ_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 20, 1, 1),
    _CfgAgentIRQ_Type()
)
cfgAgentIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIRQ.setStatus("mandatory")
_CfgAgentIRQOwner_Type = DisplayString
_CfgAgentIRQOwner_Object = MibTableColumn
cfgAgentIRQOwner = _CfgAgentIRQOwner_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 20, 1, 2),
    _CfgAgentIRQOwner_Type()
)
cfgAgentIRQOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIRQOwner.setStatus("mandatory")
_CfgAgentIRQBus_Type = DisplayString
_CfgAgentIRQBus_Object = MibTableColumn
cfgAgentIRQBus = _CfgAgentIRQBus_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 20, 1, 3),
    _CfgAgentIRQBus_Type()
)
cfgAgentIRQBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIRQBus.setStatus("mandatory")
_CfgAgentIRQClass_Type = DisplayString
_CfgAgentIRQClass_Object = MibTableColumn
cfgAgentIRQClass = _CfgAgentIRQClass_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 20, 1, 4),
    _CfgAgentIRQClass_Type()
)
cfgAgentIRQClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIRQClass.setStatus("mandatory")
_CfgAgentMemSizeInMb_Type = Integer32
_CfgAgentMemSizeInMb_Object = MibScalar
cfgAgentMemSizeInMb = _CfgAgentMemSizeInMb_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 21),
    _CfgAgentMemSizeInMb_Type()
)
cfgAgentMemSizeInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMemSizeInMb.setStatus("mandatory")
_CfgAgentMemType_Type = DisplayString
_CfgAgentMemType_Object = MibScalar
cfgAgentMemType = _CfgAgentMemType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 22),
    _CfgAgentMemType_Type()
)
cfgAgentMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMemType.setStatus("mandatory")
_CfgAgentMemSpeed_Type = Integer32
_CfgAgentMemSpeed_Object = MibScalar
cfgAgentMemSpeed = _CfgAgentMemSpeed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 23),
    _CfgAgentMemSpeed_Type()
)
cfgAgentMemSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMemSpeed.setStatus("mandatory")
_CfgAgentMemCacheInKb_Type = Integer32
_CfgAgentMemCacheInKb_Object = MibScalar
cfgAgentMemCacheInKb = _CfgAgentMemCacheInKb_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 24),
    _CfgAgentMemCacheInKb_Type()
)
cfgAgentMemCacheInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMemCacheInKb.setStatus("mandatory")
_CfgAgentMemBanks_Type = Integer32
_CfgAgentMemBanks_Object = MibScalar
cfgAgentMemBanks = _CfgAgentMemBanks_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 25),
    _CfgAgentMemBanks_Type()
)
cfgAgentMemBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMemBanks.setStatus("mandatory")
_CfgAgentMemSpeedSupported_Type = Integer32
_CfgAgentMemSpeedSupported_Object = MibScalar
cfgAgentMemSpeedSupported = _CfgAgentMemSpeedSupported_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 26),
    _CfgAgentMemSpeedSupported_Type()
)
cfgAgentMemSpeedSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMemSpeedSupported.setStatus("mandatory")
_CfgAgentIOKbdType_Type = DisplayString
_CfgAgentIOKbdType_Object = MibScalar
cfgAgentIOKbdType = _CfgAgentIOKbdType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 27),
    _CfgAgentIOKbdType_Type()
)
cfgAgentIOKbdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIOKbdType.setStatus("mandatory")
_CfgAgentIOMouseType_Type = DisplayString
_CfgAgentIOMouseType_Object = MibScalar
cfgAgentIOMouseType = _CfgAgentIOMouseType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 28),
    _CfgAgentIOMouseType_Type()
)
cfgAgentIOMouseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIOMouseType.setStatus("mandatory")
_CfgAgentIOVidType_Type = DisplayString
_CfgAgentIOVidType_Object = MibScalar
cfgAgentIOVidType = _CfgAgentIOVidType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 29),
    _CfgAgentIOVidType_Type()
)
cfgAgentIOVidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIOVidType.setStatus("mandatory")
_CfgAgentnSerials_Type = Integer32
_CfgAgentnSerials_Object = MibScalar
cfgAgentnSerials = _CfgAgentnSerials_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 30),
    _CfgAgentnSerials_Type()
)
cfgAgentnSerials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnSerials.setStatus("mandatory")
_CfgAgentSerialsTbl_Object = MibTable
cfgAgentSerialsTbl = _CfgAgentSerialsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 31)
)
if mibBuilder.loadTexts:
    cfgAgentSerialsTbl.setStatus("mandatory")
_CfgAgentSerialsTblEntry_Object = MibTableRow
cfgAgentSerialsTblEntry = _CfgAgentSerialsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 31, 1)
)
if mibBuilder.loadTexts:
    cfgAgentSerialsTblEntry.setStatus("mandatory")
_CfgAgentSerialPort_Type = Integer32
_CfgAgentSerialPort_Object = MibTableColumn
cfgAgentSerialPort = _CfgAgentSerialPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 31, 1, 1),
    _CfgAgentSerialPort_Type()
)
cfgAgentSerialPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentSerialPort.setStatus("mandatory")
_CfgAgentnParallels_Type = Integer32
_CfgAgentnParallels_Object = MibScalar
cfgAgentnParallels = _CfgAgentnParallels_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 32),
    _CfgAgentnParallels_Type()
)
cfgAgentnParallels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnParallels.setStatus("mandatory")
_CfgAgentParallelsTbl_Object = MibTable
cfgAgentParallelsTbl = _CfgAgentParallelsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 33)
)
if mibBuilder.loadTexts:
    cfgAgentParallelsTbl.setStatus("mandatory")
_CfgAgentParallelsTblEntry_Object = MibTableRow
cfgAgentParallelsTblEntry = _CfgAgentParallelsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 33, 1)
)
if mibBuilder.loadTexts:
    cfgAgentParallelsTblEntry.setStatus("mandatory")
_CfgAgentParallelPort_Type = Integer32
_CfgAgentParallelPort_Object = MibTableColumn
cfgAgentParallelPort = _CfgAgentParallelPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 33, 1, 1),
    _CfgAgentParallelPort_Type()
)
cfgAgentParallelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentParallelPort.setStatus("mandatory")
_CfgAgentnControllers_Type = Integer32
_CfgAgentnControllers_Object = MibScalar
cfgAgentnControllers = _CfgAgentnControllers_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 34),
    _CfgAgentnControllers_Type()
)
cfgAgentnControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnControllers.setStatus("mandatory")
_CfgAgentControllersTbl_Object = MibTable
cfgAgentControllersTbl = _CfgAgentControllersTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 35)
)
if mibBuilder.loadTexts:
    cfgAgentControllersTbl.setStatus("mandatory")
_CfgAgentControllersTblEntry_Object = MibTableRow
cfgAgentControllersTblEntry = _CfgAgentControllersTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 35, 1)
)
if mibBuilder.loadTexts:
    cfgAgentControllersTblEntry.setStatus("mandatory")
_CfgAgentControllerType_Type = DisplayString
_CfgAgentControllerType_Object = MibTableColumn
cfgAgentControllerType = _CfgAgentControllerType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 35, 1, 1),
    _CfgAgentControllerType_Type()
)
cfgAgentControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentControllerType.setStatus("mandatory")
_CfgAgentControllerName_Type = DisplayString
_CfgAgentControllerName_Object = MibTableColumn
cfgAgentControllerName = _CfgAgentControllerName_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 35, 1, 2),
    _CfgAgentControllerName_Type()
)
cfgAgentControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentControllerName.setStatus("mandatory")
_CfgAgentControllerIRQ_Type = Integer32
_CfgAgentControllerIRQ_Object = MibTableColumn
cfgAgentControllerIRQ = _CfgAgentControllerIRQ_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 35, 1, 3),
    _CfgAgentControllerIRQ_Type()
)
cfgAgentControllerIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentControllerIRQ.setStatus("mandatory")
_CfgAgentnTrapDests_Type = Integer32
_CfgAgentnTrapDests_Object = MibScalar
cfgAgentnTrapDests = _CfgAgentnTrapDests_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 36),
    _CfgAgentnTrapDests_Type()
)
cfgAgentnTrapDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnTrapDests.setStatus("mandatory")
_CfgAgentTrapDestsTbl_Object = MibTable
cfgAgentTrapDestsTbl = _CfgAgentTrapDestsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 37)
)
if mibBuilder.loadTexts:
    cfgAgentTrapDestsTbl.setStatus("mandatory")
_CfgAgentTrapDestsTblEntry_Object = MibTableRow
cfgAgentTrapDestsTblEntry = _CfgAgentTrapDestsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 37, 1)
)
if mibBuilder.loadTexts:
    cfgAgentTrapDestsTblEntry.setStatus("mandatory")
_CfgAgentTrapDestId_Type = DisplayString
_CfgAgentTrapDestId_Object = MibTableColumn
cfgAgentTrapDestId = _CfgAgentTrapDestId_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 37, 1, 1),
    _CfgAgentTrapDestId_Type()
)
cfgAgentTrapDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentTrapDestId.setStatus("mandatory")
_CfgAgentTrapDestIPAddr_Type = DisplayString
_CfgAgentTrapDestIPAddr_Object = MibTableColumn
cfgAgentTrapDestIPAddr = _CfgAgentTrapDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 37, 1, 2),
    _CfgAgentTrapDestIPAddr_Type()
)
cfgAgentTrapDestIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAgentTrapDestIPAddr.setStatus("mandatory")
_CfgAgentCommunityString_Type = DisplayString
_CfgAgentCommunityString_Object = MibTableColumn
cfgAgentCommunityString = _CfgAgentCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 37, 1, 3),
    _CfgAgentCommunityString_Type()
)
cfgAgentCommunityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCommunityString.setStatus("mandatory")
_CfgAgentnPlatforms_Type = Integer32
_CfgAgentnPlatforms_Object = MibScalar
cfgAgentnPlatforms = _CfgAgentnPlatforms_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 38),
    _CfgAgentnPlatforms_Type()
)
cfgAgentnPlatforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnPlatforms.setStatus("mandatory")
_CfgAgentPlatforms_Object = MibTable
cfgAgentPlatforms = _CfgAgentPlatforms_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 39)
)
if mibBuilder.loadTexts:
    cfgAgentPlatforms.setStatus("mandatory")
_CfgAgentPlatformTblEntry_Object = MibTableRow
cfgAgentPlatformTblEntry = _CfgAgentPlatformTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 39, 1)
)
if mibBuilder.loadTexts:
    cfgAgentPlatformTblEntry.setStatus("mandatory")
_CfgAgentOEMPlatform_Type = DisplayString
_CfgAgentOEMPlatform_Object = MibTableColumn
cfgAgentOEMPlatform = _CfgAgentOEMPlatform_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 39, 1, 1),
    _CfgAgentOEMPlatform_Type()
)
cfgAgentOEMPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentOEMPlatform.setStatus("mandatory")
_CfgAgentProductID_Type = DisplayString
_CfgAgentProductID_Object = MibTableColumn
cfgAgentProductID = _CfgAgentProductID_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 39, 1, 2),
    _CfgAgentProductID_Type()
)
cfgAgentProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentProductID.setStatus("mandatory")
_CfgAgentnConsoleMgr_Type = Integer32
_CfgAgentnConsoleMgr_Object = MibScalar
cfgAgentnConsoleMgr = _CfgAgentnConsoleMgr_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 40),
    _CfgAgentnConsoleMgr_Type()
)
cfgAgentnConsoleMgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnConsoleMgr.setStatus("mandatory")
_CfgAgentConsoleMgr_Object = MibTable
cfgAgentConsoleMgr = _CfgAgentConsoleMgr_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 41)
)
if mibBuilder.loadTexts:
    cfgAgentConsoleMgr.setStatus("mandatory")
_CfgAgentConsoleMgrTblEntry_Object = MibTableRow
cfgAgentConsoleMgrTblEntry = _CfgAgentConsoleMgrTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 41, 1)
)
if mibBuilder.loadTexts:
    cfgAgentConsoleMgrTblEntry.setStatus("mandatory")
_CfgAgentCMCardIndex_Type = Integer32
_CfgAgentCMCardIndex_Object = MibTableColumn
cfgAgentCMCardIndex = _CfgAgentCMCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 41, 1, 1),
    _CfgAgentCMCardIndex_Type()
)
cfgAgentCMCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCMCardIndex.setStatus("mandatory")
_CfgAgentCMIPAddress_Type = DisplayString
_CfgAgentCMIPAddress_Object = MibTableColumn
cfgAgentCMIPAddress = _CfgAgentCMIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 41, 1, 2),
    _CfgAgentCMIPAddress_Type()
)
cfgAgentCMIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCMIPAddress.setStatus("mandatory")
_CfgAgentCMHostName_Type = DisplayString
_CfgAgentCMHostName_Object = MibTableColumn
cfgAgentCMHostName = _CfgAgentCMHostName_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 41, 1, 3),
    _CfgAgentCMHostName_Type()
)
cfgAgentCMHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCMHostName.setStatus("mandatory")
_CfgAgentCMHardwareVer_Type = DisplayString
_CfgAgentCMHardwareVer_Object = MibTableColumn
cfgAgentCMHardwareVer = _CfgAgentCMHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 41, 1, 4),
    _CfgAgentCMHardwareVer_Type()
)
cfgAgentCMHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCMHardwareVer.setStatus("mandatory")
_CfgAgentCMFirmwareVer_Type = DisplayString
_CfgAgentCMFirmwareVer_Object = MibTableColumn
cfgAgentCMFirmwareVer = _CfgAgentCMFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 41, 1, 5),
    _CfgAgentCMFirmwareVer_Type()
)
cfgAgentCMFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCMFirmwareVer.setStatus("mandatory")
_NetAgent_ObjectIdentity = ObjectIdentity
netAgent = _NetAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 8)
)
_NetAgentVersion_Type = Integer32
_NetAgentVersion_Object = MibScalar
netAgentVersion = _NetAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 1),
    _NetAgentVersion_Type()
)
netAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentVersion.setStatus("mandatory")
_NetAgentRevision_Type = Integer32
_NetAgentRevision_Object = MibScalar
netAgentRevision = _NetAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 2),
    _NetAgentRevision_Type()
)
netAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentRevision.setStatus("mandatory")
_NetAgentMIBVersion_Type = Integer32
_NetAgentMIBVersion_Object = MibScalar
netAgentMIBVersion = _NetAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 3),
    _NetAgentMIBVersion_Type()
)
netAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentMIBVersion.setStatus("mandatory")
_NetAgentMIBRevision_Type = Integer32
_NetAgentMIBRevision_Object = MibScalar
netAgentMIBRevision = _NetAgentMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 4),
    _NetAgentMIBRevision_Type()
)
netAgentMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentMIBRevision.setStatus("mandatory")
_NetAgentMachineName_Type = DisplayString
_NetAgentMachineName_Object = MibScalar
netAgentMachineName = _NetAgentMachineName_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 5),
    _NetAgentMachineName_Type()
)
netAgentMachineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentMachineName.setStatus("mandatory")
_NetAgentLogonServer_Type = DisplayString
_NetAgentLogonServer_Object = MibScalar
netAgentLogonServer = _NetAgentLogonServer_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 6),
    _NetAgentLogonServer_Type()
)
netAgentLogonServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentLogonServer.setStatus("mandatory")
_NetAgentnNICs_Type = Integer32
_NetAgentnNICs_Object = MibScalar
netAgentnNICs = _NetAgentnNICs_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 7),
    _NetAgentnNICs_Type()
)
netAgentnNICs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentnNICs.setStatus("mandatory")
_NetAgentNICsTbl_Object = MibTable
netAgentNICsTbl = _NetAgentNICsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8)
)
if mibBuilder.loadTexts:
    netAgentNICsTbl.setStatus("mandatory")
_NetAgentNICTblEntry_Object = MibTableRow
netAgentNICTblEntry = _NetAgentNICTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1)
)
if mibBuilder.loadTexts:
    netAgentNICTblEntry.setStatus("mandatory")
_NetAgentVendorID_Type = DisplayString
_NetAgentVendorID_Object = MibTableColumn
netAgentVendorID = _NetAgentVendorID_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 1),
    _NetAgentVendorID_Type()
)
netAgentVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentVendorID.setStatus("mandatory")
_NetAgentMACAddress_Type = DisplayString
_NetAgentMACAddress_Object = MibTableColumn
netAgentMACAddress = _NetAgentMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 2),
    _NetAgentMACAddress_Type()
)
netAgentMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentMACAddress.setStatus("mandatory")
_NetAgentFirmwareVersion_Type = Integer32
_NetAgentFirmwareVersion_Object = MibTableColumn
netAgentFirmwareVersion = _NetAgentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 3),
    _NetAgentFirmwareVersion_Type()
)
netAgentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentFirmwareVersion.setStatus("mandatory")
_NetAgentFirmwareRevision_Type = Integer32
_NetAgentFirmwareRevision_Object = MibTableColumn
netAgentFirmwareRevision = _NetAgentFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 4),
    _NetAgentFirmwareRevision_Type()
)
netAgentFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentFirmwareRevision.setStatus("mandatory")
_NetAgentControllerType_Type = DisplayString
_NetAgentControllerType_Object = MibTableColumn
netAgentControllerType = _NetAgentControllerType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 5),
    _NetAgentControllerType_Type()
)
netAgentControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentControllerType.setStatus("mandatory")
_NetAgentControllerPort_Type = Integer32
_NetAgentControllerPort_Object = MibTableColumn
netAgentControllerPort = _NetAgentControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 6),
    _NetAgentControllerPort_Type()
)
netAgentControllerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentControllerPort.setStatus("mandatory")
_NetAgentControllerIRQ_Type = Integer32
_NetAgentControllerIRQ_Object = MibTableColumn
netAgentControllerIRQ = _NetAgentControllerIRQ_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 7),
    _NetAgentControllerIRQ_Type()
)
netAgentControllerIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentControllerIRQ.setStatus("mandatory")
_NetAgentControllerBaseIO_Type = Integer32
_NetAgentControllerBaseIO_Object = MibTableColumn
netAgentControllerBaseIO = _NetAgentControllerBaseIO_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 8),
    _NetAgentControllerBaseIO_Type()
)
netAgentControllerBaseIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentControllerBaseIO.setStatus("mandatory")
_NetAgentDataSent_Type = Integer32
_NetAgentDataSent_Object = MibTableColumn
netAgentDataSent = _NetAgentDataSent_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 9),
    _NetAgentDataSent_Type()
)
netAgentDataSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentDataSent.setStatus("mandatory")
_NetAgentDataReceived_Type = Integer32
_NetAgentDataReceived_Object = MibTableColumn
netAgentDataReceived = _NetAgentDataReceived_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 10),
    _NetAgentDataReceived_Type()
)
netAgentDataReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentDataReceived.setStatus("mandatory")
_NetAgentNICDriver_Type = DisplayString
_NetAgentNICDriver_Object = MibTableColumn
netAgentNICDriver = _NetAgentNICDriver_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 11),
    _NetAgentNICDriver_Type()
)
netAgentNICDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentNICDriver.setStatus("mandatory")
_NetAgentDriverName_Type = DisplayString
_NetAgentDriverName_Object = MibTableColumn
netAgentDriverName = _NetAgentDriverName_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 12),
    _NetAgentDriverName_Type()
)
netAgentDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentDriverName.setStatus("mandatory")
_SftAgent_ObjectIdentity = ObjectIdentity
sftAgent = _SftAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 9)
)
_SftAgentVersion_Type = Integer32
_SftAgentVersion_Object = MibScalar
sftAgentVersion = _SftAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 1),
    _SftAgentVersion_Type()
)
sftAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentVersion.setStatus("mandatory")
_SftAgentRevision_Type = Integer32
_SftAgentRevision_Object = MibScalar
sftAgentRevision = _SftAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 2),
    _SftAgentRevision_Type()
)
sftAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentRevision.setStatus("mandatory")
_SftAgentMIBVersion_Type = Integer32
_SftAgentMIBVersion_Object = MibScalar
sftAgentMIBVersion = _SftAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 3),
    _SftAgentMIBVersion_Type()
)
sftAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentMIBVersion.setStatus("mandatory")
_SftAgentMIBRevision_Type = Integer32
_SftAgentMIBRevision_Object = MibScalar
sftAgentMIBRevision = _SftAgentMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 4),
    _SftAgentMIBRevision_Type()
)
sftAgentMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentMIBRevision.setStatus("mandatory")
_SftAgentnPackages_Type = Integer32
_SftAgentnPackages_Object = MibScalar
sftAgentnPackages = _SftAgentnPackages_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 5),
    _SftAgentnPackages_Type()
)
sftAgentnPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentnPackages.setStatus("mandatory")
_SftAgentPackagesTbl_Object = MibTable
sftAgentPackagesTbl = _SftAgentPackagesTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 6)
)
if mibBuilder.loadTexts:
    sftAgentPackagesTbl.setStatus("mandatory")
_SftAgentPackagesTblEntry_Object = MibTableRow
sftAgentPackagesTblEntry = _SftAgentPackagesTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 6, 1)
)
if mibBuilder.loadTexts:
    sftAgentPackagesTblEntry.setStatus("mandatory")
_SftAgentPackage_Type = DisplayString
_SftAgentPackage_Object = MibTableColumn
sftAgentPackage = _SftAgentPackage_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 6, 1, 1),
    _SftAgentPackage_Type()
)
sftAgentPackage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentPackage.setStatus("mandatory")
_SftAgentnServices_Type = Integer32
_SftAgentnServices_Object = MibScalar
sftAgentnServices = _SftAgentnServices_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 7),
    _SftAgentnServices_Type()
)
sftAgentnServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentnServices.setStatus("mandatory")
_SftAgentServicesTbl_Object = MibTable
sftAgentServicesTbl = _SftAgentServicesTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 8)
)
if mibBuilder.loadTexts:
    sftAgentServicesTbl.setStatus("mandatory")
_SftAgentServicesTblEntry_Object = MibTableRow
sftAgentServicesTblEntry = _SftAgentServicesTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 8, 1)
)
if mibBuilder.loadTexts:
    sftAgentServicesTblEntry.setStatus("mandatory")
_SftAgentService_Type = DisplayString
_SftAgentService_Object = MibTableColumn
sftAgentService = _SftAgentService_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 8, 1, 1),
    _SftAgentService_Type()
)
sftAgentService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentService.setStatus("mandatory")


class _SftAgentServiceStartup_Type(Integer32):
    """Custom type sftAgentServiceStartup based on Integer32"""
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
        *(("auto", 2),
          ("boot", 0),
          ("disabled", 4),
          ("manual", 3),
          ("system", 1))
    )


_SftAgentServiceStartup_Type.__name__ = "Integer32"
_SftAgentServiceStartup_Object = MibTableColumn
sftAgentServiceStartup = _SftAgentServiceStartup_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 8, 1, 2),
    _SftAgentServiceStartup_Type()
)
sftAgentServiceStartup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentServiceStartup.setStatus("mandatory")


class _SftAgentServiceStatus_Type(Integer32):
    """Custom type sftAgentServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 2),
          ("stopped", 1))
    )


_SftAgentServiceStatus_Type.__name__ = "Integer32"
_SftAgentServiceStatus_Object = MibTableColumn
sftAgentServiceStatus = _SftAgentServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 8, 1, 3),
    _SftAgentServiceStatus_Type()
)
sftAgentServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentServiceStatus.setStatus("mandatory")


class _SftAgentServiceDesired_Type(Integer32):
    """Custom type sftAgentServiceDesired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 3),
          ("running", 2),
          ("stopping", 1))
    )


_SftAgentServiceDesired_Type.__name__ = "Integer32"
_SftAgentServiceDesired_Object = MibTableColumn
sftAgentServiceDesired = _SftAgentServiceDesired_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 8, 1, 4),
    _SftAgentServiceDesired_Type()
)
sftAgentServiceDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sftAgentServiceDesired.setStatus("mandatory")
_SftAgentnDevices_Type = Integer32
_SftAgentnDevices_Object = MibScalar
sftAgentnDevices = _SftAgentnDevices_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 9),
    _SftAgentnDevices_Type()
)
sftAgentnDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentnDevices.setStatus("mandatory")
_SftAgentDevicesTbl_Object = MibTable
sftAgentDevicesTbl = _SftAgentDevicesTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 10)
)
if mibBuilder.loadTexts:
    sftAgentDevicesTbl.setStatus("mandatory")
_SftAgentDevicesTblEntry_Object = MibTableRow
sftAgentDevicesTblEntry = _SftAgentDevicesTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 10, 1)
)
if mibBuilder.loadTexts:
    sftAgentDevicesTblEntry.setStatus("mandatory")
_SftAgentDevice_Type = DisplayString
_SftAgentDevice_Object = MibTableColumn
sftAgentDevice = _SftAgentDevice_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 10, 1, 1),
    _SftAgentDevice_Type()
)
sftAgentDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentDevice.setStatus("mandatory")


class _SftAgentDeviceStartup_Type(Integer32):
    """Custom type sftAgentDeviceStartup based on Integer32"""
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
        *(("auto", 2),
          ("boot", 0),
          ("disabled", 4),
          ("manual", 3),
          ("system", 1))
    )


_SftAgentDeviceStartup_Type.__name__ = "Integer32"
_SftAgentDeviceStartup_Object = MibTableColumn
sftAgentDeviceStartup = _SftAgentDeviceStartup_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 10, 1, 2),
    _SftAgentDeviceStartup_Type()
)
sftAgentDeviceStartup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentDeviceStartup.setStatus("mandatory")
_SftAgentCriticalServices_Type = Integer32
_SftAgentCriticalServices_Object = MibScalar
sftAgentCriticalServices = _SftAgentCriticalServices_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 11),
    _SftAgentCriticalServices_Type()
)
sftAgentCriticalServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentCriticalServices.setStatus("mandatory")
_SftAgentSvcIndex_Type = Integer32
_SftAgentSvcIndex_Object = MibScalar
sftAgentSvcIndex = _SftAgentSvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 99),
    _SftAgentSvcIndex_Type()
)
sftAgentSvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sftAgentSvcIndex.setStatus("mandatory")
_StrAgent_ObjectIdentity = ObjectIdentity
strAgent = _StrAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 10)
)
_StrAgentVersion_Type = Integer32
_StrAgentVersion_Object = MibScalar
strAgentVersion = _StrAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 1),
    _StrAgentVersion_Type()
)
strAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVersion.setStatus("mandatory")
_StrAgentRevision_Type = Integer32
_StrAgentRevision_Object = MibScalar
strAgentRevision = _StrAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 2),
    _StrAgentRevision_Type()
)
strAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentRevision.setStatus("mandatory")
_StrAgentMIBVersion_Type = Integer32
_StrAgentMIBVersion_Object = MibScalar
strAgentMIBVersion = _StrAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 3),
    _StrAgentMIBVersion_Type()
)
strAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentMIBVersion.setStatus("mandatory")
_StrAgentMIBRevision_Type = Integer32
_StrAgentMIBRevision_Object = MibScalar
strAgentMIBRevision = _StrAgentMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 4),
    _StrAgentMIBRevision_Type()
)
strAgentMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentMIBRevision.setStatus("mandatory")
_StrAgentnControllers_Type = Integer32
_StrAgentnControllers_Object = MibScalar
strAgentnControllers = _StrAgentnControllers_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 5),
    _StrAgentnControllers_Type()
)
strAgentnControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentnControllers.setStatus("mandatory")
_StrAgentControllersTbl_Object = MibTable
strAgentControllersTbl = _StrAgentControllersTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6)
)
if mibBuilder.loadTexts:
    strAgentControllersTbl.setStatus("mandatory")
_StrAgentControllersTblEntry_Object = MibTableRow
strAgentControllersTblEntry = _StrAgentControllersTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1)
)
if mibBuilder.loadTexts:
    strAgentControllersTblEntry.setStatus("mandatory")
_StrAgentCtlrType_Type = DisplayString
_StrAgentCtlrType_Object = MibTableColumn
strAgentCtlrType = _StrAgentCtlrType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 1),
    _StrAgentCtlrType_Type()
)
strAgentCtlrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrType.setStatus("mandatory")
_StrAgentCtlrVendor_Type = DisplayString
_StrAgentCtlrVendor_Object = MibTableColumn
strAgentCtlrVendor = _StrAgentCtlrVendor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 2),
    _StrAgentCtlrVendor_Type()
)
strAgentCtlrVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrVendor.setStatus("mandatory")
_StrAgentCtlrFirmware_Type = DisplayString
_StrAgentCtlrFirmware_Object = MibTableColumn
strAgentCtlrFirmware = _StrAgentCtlrFirmware_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 3),
    _StrAgentCtlrFirmware_Type()
)
strAgentCtlrFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrFirmware.setStatus("mandatory")
_StrAgentCtlrSerialNo_Type = DisplayString
_StrAgentCtlrSerialNo_Object = MibTableColumn
strAgentCtlrSerialNo = _StrAgentCtlrSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 4),
    _StrAgentCtlrSerialNo_Type()
)
strAgentCtlrSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrSerialNo.setStatus("mandatory")
_StrAgentCtlrDMA_Type = Integer32
_StrAgentCtlrDMA_Object = MibTableColumn
strAgentCtlrDMA = _StrAgentCtlrDMA_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 5),
    _StrAgentCtlrDMA_Type()
)
strAgentCtlrDMA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrDMA.setStatus("mandatory")
_StrAgentCtlrIRQ_Type = Integer32
_StrAgentCtlrIRQ_Object = MibTableColumn
strAgentCtlrIRQ = _StrAgentCtlrIRQ_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 6),
    _StrAgentCtlrIRQ_Type()
)
strAgentCtlrIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrIRQ.setStatus("mandatory")
_StrAgentCtlrAddress_Type = Integer32
_StrAgentCtlrAddress_Object = MibTableColumn
strAgentCtlrAddress = _StrAgentCtlrAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 7),
    _StrAgentCtlrAddress_Type()
)
strAgentCtlrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrAddress.setStatus("mandatory")
_StrAgentCtlrIOPort_Type = Gauge32
_StrAgentCtlrIOPort_Object = MibTableColumn
strAgentCtlrIOPort = _StrAgentCtlrIOPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 8),
    _StrAgentCtlrIOPort_Type()
)
strAgentCtlrIOPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrIOPort.setStatus("mandatory")
_StrAgentnDisks_Type = Integer32
_StrAgentnDisks_Object = MibScalar
strAgentnDisks = _StrAgentnDisks_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 7),
    _StrAgentnDisks_Type()
)
strAgentnDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentnDisks.setStatus("mandatory")
_StrAgentDisksTbl_Object = MibTable
strAgentDisksTbl = _StrAgentDisksTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8)
)
if mibBuilder.loadTexts:
    strAgentDisksTbl.setStatus("mandatory")
_StrAgentDisksTblEntry_Object = MibTableRow
strAgentDisksTblEntry = _StrAgentDisksTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1)
)
if mibBuilder.loadTexts:
    strAgentDisksTblEntry.setStatus("mandatory")
_StrAgentDiskVendor_Type = DisplayString
_StrAgentDiskVendor_Object = MibTableColumn
strAgentDiskVendor = _StrAgentDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 1),
    _StrAgentDiskVendor_Type()
)
strAgentDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskVendor.setStatus("mandatory")
_StrAgentDiskDescription_Type = DisplayString
_StrAgentDiskDescription_Object = MibTableColumn
strAgentDiskDescription = _StrAgentDiskDescription_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 2),
    _StrAgentDiskDescription_Type()
)
strAgentDiskDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskDescription.setStatus("mandatory")
_StrAgentDiskFirmware_Type = DisplayString
_StrAgentDiskFirmware_Object = MibTableColumn
strAgentDiskFirmware = _StrAgentDiskFirmware_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 3),
    _StrAgentDiskFirmware_Type()
)
strAgentDiskFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskFirmware.setStatus("mandatory")
_StrAgentDiskPort_Type = Integer32
_StrAgentDiskPort_Object = MibTableColumn
strAgentDiskPort = _StrAgentDiskPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 4),
    _StrAgentDiskPort_Type()
)
strAgentDiskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskPort.setStatus("mandatory")
_StrAgentDiskBus_Type = Integer32
_StrAgentDiskBus_Object = MibTableColumn
strAgentDiskBus = _StrAgentDiskBus_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 5),
    _StrAgentDiskBus_Type()
)
strAgentDiskBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskBus.setStatus("mandatory")
_StrAgentDiskLUN_Type = Integer32
_StrAgentDiskLUN_Object = MibTableColumn
strAgentDiskLUN = _StrAgentDiskLUN_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 6),
    _StrAgentDiskLUN_Type()
)
strAgentDiskLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskLUN.setStatus("mandatory")
_StrAgentDiskID_Type = Integer32
_StrAgentDiskID_Object = MibTableColumn
strAgentDiskID = _StrAgentDiskID_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 7),
    _StrAgentDiskID_Type()
)
strAgentDiskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskID.setStatus("mandatory")
_StrAgentDiskSerialNo_Type = DisplayString
_StrAgentDiskSerialNo_Object = MibTableColumn
strAgentDiskSerialNo = _StrAgentDiskSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 8),
    _StrAgentDiskSerialNo_Type()
)
strAgentDiskSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskSerialNo.setStatus("mandatory")
_StrAgentDisknSectors_Type = Integer32
_StrAgentDisknSectors_Object = MibTableColumn
strAgentDisknSectors = _StrAgentDisknSectors_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 9),
    _StrAgentDisknSectors_Type()
)
strAgentDisknSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDisknSectors.setStatus("mandatory")
_StrAgentDiskDriveLetters_Type = DisplayString
_StrAgentDiskDriveLetters_Object = MibTableColumn
strAgentDiskDriveLetters = _StrAgentDiskDriveLetters_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 10),
    _StrAgentDiskDriveLetters_Type()
)
strAgentDiskDriveLetters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskDriveLetters.setStatus("mandatory")
_StrAgentDiskSizeInMb_Type = Integer32
_StrAgentDiskSizeInMb_Object = MibTableColumn
strAgentDiskSizeInMb = _StrAgentDiskSizeInMb_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 11),
    _StrAgentDiskSizeInMb_Type()
)
strAgentDiskSizeInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskSizeInMb.setStatus("mandatory")


class _StrAgentDiskState_Type(Integer32):
    """Custom type strAgentDiskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accessable", 1),
          ("offline", 2))
    )


_StrAgentDiskState_Type.__name__ = "Integer32"
_StrAgentDiskState_Object = MibTableColumn
strAgentDiskState = _StrAgentDiskState_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 12),
    _StrAgentDiskState_Type()
)
strAgentDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskState.setStatus("mandatory")
_StrAgentDiskXfersPerSec_Type = Integer32
_StrAgentDiskXfersPerSec_Object = MibTableColumn
strAgentDiskXfersPerSec = _StrAgentDiskXfersPerSec_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 13),
    _StrAgentDiskXfersPerSec_Type()
)
strAgentDiskXfersPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskXfersPerSec.setStatus("mandatory")


class _StrAgentDiskSmartCond_Type(Integer32):
    """Custom type strAgentDiskSmartCond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 2),
          ("safe", 1),
          ("unknown", 0))
    )


_StrAgentDiskSmartCond_Type.__name__ = "Integer32"
_StrAgentDiskSmartCond_Object = MibTableColumn
strAgentDiskSmartCond = _StrAgentDiskSmartCond_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 14),
    _StrAgentDiskSmartCond_Type()
)
strAgentDiskSmartCond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskSmartCond.setStatus("mandatory")
_StrAgentnFloppies_Type = Integer32
_StrAgentnFloppies_Object = MibScalar
strAgentnFloppies = _StrAgentnFloppies_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 9),
    _StrAgentnFloppies_Type()
)
strAgentnFloppies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentnFloppies.setStatus("mandatory")
_StrAgentFloppyTbl_Object = MibTable
strAgentFloppyTbl = _StrAgentFloppyTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 10)
)
if mibBuilder.loadTexts:
    strAgentFloppyTbl.setStatus("mandatory")
_StrAgentFloppyTblEntry_Object = MibTableRow
strAgentFloppyTblEntry = _StrAgentFloppyTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 10, 1)
)
if mibBuilder.loadTexts:
    strAgentFloppyTblEntry.setStatus("mandatory")
_StrAgentFlopVendor_Type = DisplayString
_StrAgentFlopVendor_Object = MibTableColumn
strAgentFlopVendor = _StrAgentFlopVendor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 10, 1, 1),
    _StrAgentFlopVendor_Type()
)
strAgentFlopVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentFlopVendor.setStatus("mandatory")
_StrAgentFlopDescription_Type = DisplayString
_StrAgentFlopDescription_Object = MibTableColumn
strAgentFlopDescription = _StrAgentFlopDescription_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 10, 1, 2),
    _StrAgentFlopDescription_Type()
)
strAgentFlopDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentFlopDescription.setStatus("mandatory")
_StrAgentFlopFirmware_Type = DisplayString
_StrAgentFlopFirmware_Object = MibTableColumn
strAgentFlopFirmware = _StrAgentFlopFirmware_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 10, 1, 3),
    _StrAgentFlopFirmware_Type()
)
strAgentFlopFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentFlopFirmware.setStatus("mandatory")
_StrAgentFlopSerialNo_Type = DisplayString
_StrAgentFlopSerialNo_Object = MibTableColumn
strAgentFlopSerialNo = _StrAgentFlopSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 10, 1, 4),
    _StrAgentFlopSerialNo_Type()
)
strAgentFlopSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentFlopSerialNo.setStatus("mandatory")
_StrAgentnVolumes_Type = Integer32
_StrAgentnVolumes_Object = MibScalar
strAgentnVolumes = _StrAgentnVolumes_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 11),
    _StrAgentnVolumes_Type()
)
strAgentnVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentnVolumes.setStatus("mandatory")
_StrAgentVolumesTbl_Object = MibTable
strAgentVolumesTbl = _StrAgentVolumesTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12)
)
if mibBuilder.loadTexts:
    strAgentVolumesTbl.setStatus("mandatory")
_StrAgentVolumesTblEntry_Object = MibTableRow
strAgentVolumesTblEntry = _StrAgentVolumesTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1)
)
if mibBuilder.loadTexts:
    strAgentVolumesTblEntry.setStatus("mandatory")
_StrAgentVolDriveLetter_Type = DisplayString
_StrAgentVolDriveLetter_Object = MibTableColumn
strAgentVolDriveLetter = _StrAgentVolDriveLetter_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 1),
    _StrAgentVolDriveLetter_Type()
)
strAgentVolDriveLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVolDriveLetter.setStatus("mandatory")
_StrAgentVolDriveLabel_Type = DisplayString
_StrAgentVolDriveLabel_Object = MibTableColumn
strAgentVolDriveLabel = _StrAgentVolDriveLabel_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 2),
    _StrAgentVolDriveLabel_Type()
)
strAgentVolDriveLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVolDriveLabel.setStatus("mandatory")
_StrAgentVolFileSystemType_Type = DisplayString
_StrAgentVolFileSystemType_Object = MibTableColumn
strAgentVolFileSystemType = _StrAgentVolFileSystemType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 3),
    _StrAgentVolFileSystemType_Type()
)
strAgentVolFileSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVolFileSystemType.setStatus("mandatory")
_StrAgentVolCapacityInMb_Type = Integer32
_StrAgentVolCapacityInMb_Object = MibTableColumn
strAgentVolCapacityInMb = _StrAgentVolCapacityInMb_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 4),
    _StrAgentVolCapacityInMb_Type()
)
strAgentVolCapacityInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVolCapacityInMb.setStatus("mandatory")
_StrAgentVolClusterSize_Type = Integer32
_StrAgentVolClusterSize_Object = MibTableColumn
strAgentVolClusterSize = _StrAgentVolClusterSize_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 5),
    _StrAgentVolClusterSize_Type()
)
strAgentVolClusterSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVolClusterSize.setStatus("mandatory")
_StrAgentVolPercentUsed_Type = Integer32
_StrAgentVolPercentUsed_Object = MibTableColumn
strAgentVolPercentUsed = _StrAgentVolPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 6),
    _StrAgentVolPercentUsed_Type()
)
strAgentVolPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVolPercentUsed.setStatus("mandatory")
_StrAgentVolThreshold_Type = Integer32
_StrAgentVolThreshold_Object = MibTableColumn
strAgentVolThreshold = _StrAgentVolThreshold_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 7),
    _StrAgentVolThreshold_Type()
)
strAgentVolThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strAgentVolThreshold.setStatus("mandatory")
_StrAgentStateThreshhold_Type = Integer32
_StrAgentStateThreshhold_Object = MibScalar
strAgentStateThreshhold = _StrAgentStateThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 13),
    _StrAgentStateThreshhold_Type()
)
strAgentStateThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strAgentStateThreshhold.setStatus("mandatory")
_StrAgentSpaceThreshhold_Type = Integer32
_StrAgentSpaceThreshhold_Object = MibScalar
strAgentSpaceThreshhold = _StrAgentSpaceThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 14),
    _StrAgentSpaceThreshhold_Type()
)
strAgentSpaceThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strAgentSpaceThreshhold.setStatus("deprecated")
_StrAgentCriticalVol_Type = Integer32
_StrAgentCriticalVol_Object = MibScalar
strAgentCriticalVol = _StrAgentCriticalVol_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 15),
    _StrAgentCriticalVol_Type()
)
strAgentCriticalVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCriticalVol.setStatus("mandatory")
_StrAgentIndex_Type = Integer32
_StrAgentIndex_Object = MibScalar
strAgentIndex = _StrAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 99),
    _StrAgentIndex_Type()
)
strAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    strAgentIndex.setStatus("mandatory")
_SysAgent_ObjectIdentity = ObjectIdentity
sysAgent = _SysAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 11)
)
_SysAgentVersion_Type = Integer32
_SysAgentVersion_Object = MibScalar
sysAgentVersion = _SysAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 1),
    _SysAgentVersion_Type()
)
sysAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentVersion.setStatus("mandatory")
_SysAgentRevision_Type = Integer32
_SysAgentRevision_Object = MibScalar
sysAgentRevision = _SysAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 2),
    _SysAgentRevision_Type()
)
sysAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentRevision.setStatus("mandatory")
_SysAgentMIBVersion_Type = Integer32
_SysAgentMIBVersion_Object = MibScalar
sysAgentMIBVersion = _SysAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 3),
    _SysAgentMIBVersion_Type()
)
sysAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentMIBVersion.setStatus("mandatory")
_SysAgentMIBRevision_Type = Integer32
_SysAgentMIBRevision_Object = MibScalar
sysAgentMIBRevision = _SysAgentMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 4),
    _SysAgentMIBRevision_Type()
)
sysAgentMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentMIBRevision.setStatus("mandatory")
_SysAgentCPUCyclesUsed_Type = Integer32
_SysAgentCPUCyclesUsed_Object = MibScalar
sysAgentCPUCyclesUsed = _SysAgentCPUCyclesUsed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 5),
    _SysAgentCPUCyclesUsed_Type()
)
sysAgentCPUCyclesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentCPUCyclesUsed.setStatus("mandatory")
_SysAgentPCICyclesUsed_Type = Integer32
_SysAgentPCICyclesUsed_Object = MibScalar
sysAgentPCICyclesUsed = _SysAgentPCICyclesUsed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 6),
    _SysAgentPCICyclesUsed_Type()
)
sysAgentPCICyclesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentPCICyclesUsed.setStatus("mandatory")
_SysAgentInterrupts_Type = Integer32
_SysAgentInterrupts_Object = MibScalar
sysAgentInterrupts = _SysAgentInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 7),
    _SysAgentInterrupts_Type()
)
sysAgentInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentInterrupts.setStatus("mandatory")
_SysAgentMemorySize_Type = Integer32
_SysAgentMemorySize_Object = MibScalar
sysAgentMemorySize = _SysAgentMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 8),
    _SysAgentMemorySize_Type()
)
sysAgentMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentMemorySize.setStatus("mandatory")
_SysAgentMemoryUsed_Type = Integer32
_SysAgentMemoryUsed_Object = MibScalar
sysAgentMemoryUsed = _SysAgentMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 9),
    _SysAgentMemoryUsed_Type()
)
sysAgentMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentMemoryUsed.setStatus("mandatory")
_SysAgentPageFaults_Type = Integer32
_SysAgentPageFaults_Object = MibScalar
sysAgentPageFaults = _SysAgentPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 10),
    _SysAgentPageFaults_Type()
)
sysAgentPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentPageFaults.setStatus("mandatory")
_SysAgentPageFaultThreshhold_Type = Integer32
_SysAgentPageFaultThreshhold_Object = MibScalar
sysAgentPageFaultThreshhold = _SysAgentPageFaultThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 11),
    _SysAgentPageFaultThreshhold_Type()
)
sysAgentPageFaultThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAgentPageFaultThreshhold.setStatus("mandatory")
_SysAgentMemoryThreshhold_Type = Integer32
_SysAgentMemoryThreshhold_Object = MibScalar
sysAgentMemoryThreshhold = _SysAgentMemoryThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 12),
    _SysAgentMemoryThreshhold_Type()
)
sysAgentMemoryThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAgentMemoryThreshhold.setStatus("mandatory")
_SysAgentCpuThreshhold_Type = Integer32
_SysAgentCpuThreshhold_Object = MibScalar
sysAgentCpuThreshhold = _SysAgentCpuThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 13),
    _SysAgentCpuThreshhold_Type()
)
sysAgentCpuThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAgentCpuThreshhold.setStatus("mandatory")
_SysAgentTotalNoCpu_Type = Integer32
_SysAgentTotalNoCpu_Object = MibScalar
sysAgentTotalNoCpu = _SysAgentTotalNoCpu_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 14),
    _SysAgentTotalNoCpu_Type()
)
sysAgentTotalNoCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentTotalNoCpu.setStatus("mandatory")
_SysAgentCPUsTbl_Object = MibTable
sysAgentCPUsTbl = _SysAgentCPUsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 15)
)
if mibBuilder.loadTexts:
    sysAgentCPUsTbl.setStatus("mandatory")
_SysAgentCPUsTblEntry_Object = MibTableRow
sysAgentCPUsTblEntry = _SysAgentCPUsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 15, 1)
)
if mibBuilder.loadTexts:
    sysAgentCPUsTblEntry.setStatus("mandatory")
_SysAgentCPUIndex_Type = Integer32
_SysAgentCPUIndex_Object = MibTableColumn
sysAgentCPUIndex = _SysAgentCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 15, 1, 1),
    _SysAgentCPUIndex_Type()
)
sysAgentCPUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentCPUIndex.setStatus("mandatory")
_SysAgentCPUCycleUsed_Type = Integer32
_SysAgentCPUCycleUsed_Object = MibTableColumn
sysAgentCPUCycleUsed = _SysAgentCPUCycleUsed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 15, 1, 2),
    _SysAgentCPUCycleUsed_Type()
)
sysAgentCPUCycleUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentCPUCycleUsed.setStatus("mandatory")
_SysAgentIndex_Type = Integer32
_SysAgentIndex_Object = MibScalar
sysAgentIndex = _SysAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 99),
    _SysAgentIndex_Type()
)
sysAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysAgentIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sftAgentSvcStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 0, 1)
)
sftAgentSvcStateTrap.setObjects(
      *(("SMSAGENT-MIB", "sftAgentService"),
        ("SMSAGENT-MIB", "sftAgentServiceStatus"),
        ("SMSAGENT-MIB", "sftAgentServiceDesired"),
        ("SMSAGENT-MIB", "sftAgentCriticalServices"))
)
if mibBuilder.loadTexts:
    sftAgentSvcStateTrap.setStatus(
        ""
    )

sftAgentSvcStateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 0, 11)
)
sftAgentSvcStateOkTrap.setObjects(
      *(("SMSAGENT-MIB", "sftAgentService"),
        ("SMSAGENT-MIB", "sftAgentServiceStatus"),
        ("SMSAGENT-MIB", "sftAgentServiceDesired"),
        ("SMSAGENT-MIB", "sftAgentCriticalServices"))
)
if mibBuilder.loadTexts:
    sftAgentSvcStateOkTrap.setStatus(
        ""
    )

strAgentStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 1)
)
strAgentStateTrap.setObjects(
      *(("SMSAGENT-MIB", "strAgentDiskState"),
        ("SMSAGENT-MIB", "strAgentIndex"))
)
if mibBuilder.loadTexts:
    strAgentStateTrap.setStatus(
        ""
    )

strAgentSpaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 2)
)
strAgentSpaceTrap.setObjects(
      *(("SMSAGENT-MIB", "strAgentVolPercentUsed"),
        ("SMSAGENT-MIB", "strAgentIndex"))
)
if mibBuilder.loadTexts:
    strAgentSpaceTrap.setStatus(
        ""
    )

strAgentSmartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 3)
)
strAgentSmartTrap.setObjects(
      *(("SMSAGENT-MIB", "strAgentDiskSmartCond"),
        ("SMSAGENT-MIB", "strAgentIndex"))
)
if mibBuilder.loadTexts:
    strAgentSmartTrap.setStatus(
        ""
    )

strAgentVolSpaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 4)
)
strAgentVolSpaceTrap.setObjects(
      *(("SMSAGENT-MIB", "strAgentVolDriveLetter"),
        ("SMSAGENT-MIB", "strAgentVolPercentUsed"),
        ("SMSAGENT-MIB", "strAgentVolThreshold"),
        ("SMSAGENT-MIB", "strAgentCriticalVol"))
)
if mibBuilder.loadTexts:
    strAgentVolSpaceTrap.setStatus(
        ""
    )

strAgentStateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 11)
)
strAgentStateOkTrap.setObjects(
      *(("SMSAGENT-MIB", "strAgentDiskState"),
        ("SMSAGENT-MIB", "strAgentIndex"))
)
if mibBuilder.loadTexts:
    strAgentStateOkTrap.setStatus(
        ""
    )

strAgentSpaceOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 12)
)
strAgentSpaceOkTrap.setObjects(
      *(("SMSAGENT-MIB", "strAgentVolPercentUsed"),
        ("SMSAGENT-MIB", "strAgentIndex"))
)
if mibBuilder.loadTexts:
    strAgentSpaceOkTrap.setStatus(
        ""
    )

strAgentSmartOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 13)
)
strAgentSmartOKTrap.setObjects(
      *(("SMSAGENT-MIB", "strAgentDiskSmartCond"),
        ("SMSAGENT-MIB", "strAgentIndex"))
)
if mibBuilder.loadTexts:
    strAgentSmartOKTrap.setStatus(
        ""
    )

strAgentVolSpaceOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 14)
)
strAgentVolSpaceOkTrap.setObjects(
      *(("SMSAGENT-MIB", "strAgentVolDriveLetter"),
        ("SMSAGENT-MIB", "strAgentVolPercentUsed"),
        ("SMSAGENT-MIB", "strAgentVolThreshold"),
        ("SMSAGENT-MIB", "strAgentCriticalVol"))
)
if mibBuilder.loadTexts:
    strAgentVolSpaceOkTrap.setStatus(
        ""
    )

sysAgentMemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 1)
)
sysAgentMemTrap.setObjects(
      *(("SMSAGENT-MIB", "sysAgentMemoryUsed"),
        ("SMSAGENT-MIB", "sysAgentIndex"))
)
if mibBuilder.loadTexts:
    sysAgentMemTrap.setStatus(
        ""
    )

sysAgentPageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 2)
)
sysAgentPageTrap.setObjects(
      *(("SMSAGENT-MIB", "sysAgentPageFaults"),
        ("SMSAGENT-MIB", "sysAgentIndex"))
)
if mibBuilder.loadTexts:
    sysAgentPageTrap.setStatus(
        ""
    )

sysAgentCpuTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 3)
)
sysAgentCpuTrap.setObjects(
      *(("SMSAGENT-MIB", "SysAgentCpuCycleUsed"),
        ("SMSAGENT-MIB", "SysAgentIndex"))
)
if mibBuilder.loadTexts:
    sysAgentCpuTrap.setStatus(
        ""
    )

sysAgentMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 4)
)
sysAgentMemoryTrap.setObjects(
      *(("SMSAGENT-MIB", "sysAgentMemoryUsed"),
        ("SMSAGENT-MIB", "sysAgentMemoryThreshhold"))
)
if mibBuilder.loadTexts:
    sysAgentMemoryTrap.setStatus(
        ""
    )

sysAgentPageFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 5)
)
sysAgentPageFaultTrap.setObjects(
      *(("SMSAGENT-MIB", "sysAgentPageFaults"),
        ("SMSAGENT-MIB", "sysAgentPageFaultThreshhold"))
)
if mibBuilder.loadTexts:
    sysAgentPageFaultTrap.setStatus(
        ""
    )

sysAgentProcessorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 6)
)
sysAgentProcessorTrap.setObjects(
      *(("SMSAGENT-MIB", "SysAgentCpuCycleUsed"),
        ("SMSAGENT-MIB", "sysAgentCpuThreshhold"))
)
if mibBuilder.loadTexts:
    sysAgentProcessorTrap.setStatus(
        ""
    )

sysAgentMemOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 11)
)
sysAgentMemOkTrap.setObjects(
      *(("SMSAGENT-MIB", "sysAgentMemoryUsed"),
        ("SMSAGENT-MIB", "sysAgentIndex"))
)
if mibBuilder.loadTexts:
    sysAgentMemOkTrap.setStatus(
        ""
    )

sysAgentPageOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 12)
)
sysAgentPageOkTrap.setObjects(
      *(("SMSAGENT-MIB", "sysAgentPageFaults"),
        ("SMSAGENT-MIB", "sysAgentIndex"))
)
if mibBuilder.loadTexts:
    sysAgentPageOkTrap.setStatus(
        ""
    )

sysAgentCpuOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 13)
)
sysAgentCpuOKTrap.setObjects(
      *(("SMSAGENT-MIB", "SysAgentCpuCycleUsed"),
        ("SMSAGENT-MIB", "SysAgentIndex"))
)
if mibBuilder.loadTexts:
    sysAgentCpuOKTrap.setStatus(
        ""
    )

sysAgentMemoryOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 14)
)
sysAgentMemoryOkTrap.setObjects(
      *(("SMSAGENT-MIB", "sysAgentMemoryUsed"),
        ("SMSAGENT-MIB", "sysAgentMemoryThreshhold"))
)
if mibBuilder.loadTexts:
    sysAgentMemoryOkTrap.setStatus(
        ""
    )

sysAgentPageFaultOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 15)
)
sysAgentPageFaultOkTrap.setObjects(
      *(("SMSAGENT-MIB", "sysAgentPageFaults"),
        ("SMSAGENT-MIB", "sysAgentPageFaultThreshhold"))
)
if mibBuilder.loadTexts:
    sysAgentPageFaultOkTrap.setStatus(
        ""
    )

sysAgentProcessorOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 16)
)
sysAgentProcessorOKTrap.setObjects(
      *(("SMSAGENT-MIB", "SysAgentCpuCycleUsed"),
        ("SMSAGENT-MIB", "sysAgentCpuThreshhold"))
)
if mibBuilder.loadTexts:
    sysAgentProcessorOKTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMSAGENT-MIB",
    **{"unisys": unisys,
       "unisysOpen": unisysOpen,
       "cfgAgent": cfgAgent,
       "cfgAgentVersion": cfgAgentVersion,
       "cfgAgentRevision": cfgAgentRevision,
       "cfgAgentMIBVersion": cfgAgentMIBVersion,
       "cfgAgentMIBRevision": cfgAgentMIBRevision,
       "cfgAgentBIOSVendor": cfgAgentBIOSVendor,
       "cfgAgentBIOSVersion": cfgAgentBIOSVersion,
       "cfgAgentBIOSDate": cfgAgentBIOSDate,
       "cfgAgentBIOSsROMInKb": cfgAgentBIOSsROMInKb,
       "cfgAgentBIOSBusSupport": cfgAgentBIOSBusSupport,
       "cfgAgentBIOSAddress": cfgAgentBIOSAddress,
       "cfgAgentBIOSInterruptId": cfgAgentBIOSInterruptId,
       "cfgAgentnCPUs": cfgAgentnCPUs,
       "cfgAgentCPUsTbl": cfgAgentCPUsTbl,
       "cfgAgentCPUsTblEntry": cfgAgentCPUsTblEntry,
       "cfgAgentCPUClass": cfgAgentCPUClass,
       "cfgAgentCPUName": cfgAgentCPUName,
       "cfgAgentCPUVendor": cfgAgentCPUVendor,
       "cfgAgentCPUSpeed": cfgAgentCPUSpeed,
       "cfgAgentCPUsCacheInKb": cfgAgentCPUsCacheInKb,
       "cfgAgentCPUState": cfgAgentCPUState,
       "cfgAgentSysName": cfgAgentSysName,
       "cfgAgentSysBoardVersion": cfgAgentSysBoardVersion,
       "cfgAgentSysUptimeMilSec": cfgAgentSysUptimeMilSec,
       "cfgAgentSysOS": cfgAgentSysOS,
       "cfgAgentSysnDMAs": cfgAgentSysnDMAs,
       "cfgAgentnIRQs": cfgAgentnIRQs,
       "cfgAgentIRQsTbl": cfgAgentIRQsTbl,
       "cfgAgentIRQsTblEntry": cfgAgentIRQsTblEntry,
       "cfgAgentIRQ": cfgAgentIRQ,
       "cfgAgentIRQOwner": cfgAgentIRQOwner,
       "cfgAgentIRQBus": cfgAgentIRQBus,
       "cfgAgentIRQClass": cfgAgentIRQClass,
       "cfgAgentMemSizeInMb": cfgAgentMemSizeInMb,
       "cfgAgentMemType": cfgAgentMemType,
       "cfgAgentMemSpeed": cfgAgentMemSpeed,
       "cfgAgentMemCacheInKb": cfgAgentMemCacheInKb,
       "cfgAgentMemBanks": cfgAgentMemBanks,
       "cfgAgentMemSpeedSupported": cfgAgentMemSpeedSupported,
       "cfgAgentIOKbdType": cfgAgentIOKbdType,
       "cfgAgentIOMouseType": cfgAgentIOMouseType,
       "cfgAgentIOVidType": cfgAgentIOVidType,
       "cfgAgentnSerials": cfgAgentnSerials,
       "cfgAgentSerialsTbl": cfgAgentSerialsTbl,
       "cfgAgentSerialsTblEntry": cfgAgentSerialsTblEntry,
       "cfgAgentSerialPort": cfgAgentSerialPort,
       "cfgAgentnParallels": cfgAgentnParallels,
       "cfgAgentParallelsTbl": cfgAgentParallelsTbl,
       "cfgAgentParallelsTblEntry": cfgAgentParallelsTblEntry,
       "cfgAgentParallelPort": cfgAgentParallelPort,
       "cfgAgentnControllers": cfgAgentnControllers,
       "cfgAgentControllersTbl": cfgAgentControllersTbl,
       "cfgAgentControllersTblEntry": cfgAgentControllersTblEntry,
       "cfgAgentControllerType": cfgAgentControllerType,
       "cfgAgentControllerName": cfgAgentControllerName,
       "cfgAgentControllerIRQ": cfgAgentControllerIRQ,
       "cfgAgentnTrapDests": cfgAgentnTrapDests,
       "cfgAgentTrapDestsTbl": cfgAgentTrapDestsTbl,
       "cfgAgentTrapDestsTblEntry": cfgAgentTrapDestsTblEntry,
       "cfgAgentTrapDestId": cfgAgentTrapDestId,
       "cfgAgentTrapDestIPAddr": cfgAgentTrapDestIPAddr,
       "cfgAgentCommunityString": cfgAgentCommunityString,
       "cfgAgentnPlatforms": cfgAgentnPlatforms,
       "cfgAgentPlatforms": cfgAgentPlatforms,
       "cfgAgentPlatformTblEntry": cfgAgentPlatformTblEntry,
       "cfgAgentOEMPlatform": cfgAgentOEMPlatform,
       "cfgAgentProductID": cfgAgentProductID,
       "cfgAgentnConsoleMgr": cfgAgentnConsoleMgr,
       "cfgAgentConsoleMgr": cfgAgentConsoleMgr,
       "cfgAgentConsoleMgrTblEntry": cfgAgentConsoleMgrTblEntry,
       "cfgAgentCMCardIndex": cfgAgentCMCardIndex,
       "cfgAgentCMIPAddress": cfgAgentCMIPAddress,
       "cfgAgentCMHostName": cfgAgentCMHostName,
       "cfgAgentCMHardwareVer": cfgAgentCMHardwareVer,
       "cfgAgentCMFirmwareVer": cfgAgentCMFirmwareVer,
       "netAgent": netAgent,
       "netAgentVersion": netAgentVersion,
       "netAgentRevision": netAgentRevision,
       "netAgentMIBVersion": netAgentMIBVersion,
       "netAgentMIBRevision": netAgentMIBRevision,
       "netAgentMachineName": netAgentMachineName,
       "netAgentLogonServer": netAgentLogonServer,
       "netAgentnNICs": netAgentnNICs,
       "netAgentNICsTbl": netAgentNICsTbl,
       "netAgentNICTblEntry": netAgentNICTblEntry,
       "netAgentVendorID": netAgentVendorID,
       "netAgentMACAddress": netAgentMACAddress,
       "netAgentFirmwareVersion": netAgentFirmwareVersion,
       "netAgentFirmwareRevision": netAgentFirmwareRevision,
       "netAgentControllerType": netAgentControllerType,
       "netAgentControllerPort": netAgentControllerPort,
       "netAgentControllerIRQ": netAgentControllerIRQ,
       "netAgentControllerBaseIO": netAgentControllerBaseIO,
       "netAgentDataSent": netAgentDataSent,
       "netAgentDataReceived": netAgentDataReceived,
       "netAgentNICDriver": netAgentNICDriver,
       "netAgentDriverName": netAgentDriverName,
       "sftAgent": sftAgent,
       "sftAgentSvcStateTrap": sftAgentSvcStateTrap,
       "sftAgentSvcStateOkTrap": sftAgentSvcStateOkTrap,
       "sftAgentVersion": sftAgentVersion,
       "sftAgentRevision": sftAgentRevision,
       "sftAgentMIBVersion": sftAgentMIBVersion,
       "sftAgentMIBRevision": sftAgentMIBRevision,
       "sftAgentnPackages": sftAgentnPackages,
       "sftAgentPackagesTbl": sftAgentPackagesTbl,
       "sftAgentPackagesTblEntry": sftAgentPackagesTblEntry,
       "sftAgentPackage": sftAgentPackage,
       "sftAgentnServices": sftAgentnServices,
       "sftAgentServicesTbl": sftAgentServicesTbl,
       "sftAgentServicesTblEntry": sftAgentServicesTblEntry,
       "sftAgentService": sftAgentService,
       "sftAgentServiceStartup": sftAgentServiceStartup,
       "sftAgentServiceStatus": sftAgentServiceStatus,
       "sftAgentServiceDesired": sftAgentServiceDesired,
       "sftAgentnDevices": sftAgentnDevices,
       "sftAgentDevicesTbl": sftAgentDevicesTbl,
       "sftAgentDevicesTblEntry": sftAgentDevicesTblEntry,
       "sftAgentDevice": sftAgentDevice,
       "sftAgentDeviceStartup": sftAgentDeviceStartup,
       "sftAgentCriticalServices": sftAgentCriticalServices,
       "sftAgentSvcIndex": sftAgentSvcIndex,
       "strAgent": strAgent,
       "strAgentStateTrap": strAgentStateTrap,
       "strAgentSpaceTrap": strAgentSpaceTrap,
       "strAgentSmartTrap": strAgentSmartTrap,
       "strAgentVolSpaceTrap": strAgentVolSpaceTrap,
       "strAgentStateOkTrap": strAgentStateOkTrap,
       "strAgentSpaceOkTrap": strAgentSpaceOkTrap,
       "strAgentSmartOKTrap": strAgentSmartOKTrap,
       "strAgentVolSpaceOkTrap": strAgentVolSpaceOkTrap,
       "strAgentVersion": strAgentVersion,
       "strAgentRevision": strAgentRevision,
       "strAgentMIBVersion": strAgentMIBVersion,
       "strAgentMIBRevision": strAgentMIBRevision,
       "strAgentnControllers": strAgentnControllers,
       "strAgentControllersTbl": strAgentControllersTbl,
       "strAgentControllersTblEntry": strAgentControllersTblEntry,
       "strAgentCtlrType": strAgentCtlrType,
       "strAgentCtlrVendor": strAgentCtlrVendor,
       "strAgentCtlrFirmware": strAgentCtlrFirmware,
       "strAgentCtlrSerialNo": strAgentCtlrSerialNo,
       "strAgentCtlrDMA": strAgentCtlrDMA,
       "strAgentCtlrIRQ": strAgentCtlrIRQ,
       "strAgentCtlrAddress": strAgentCtlrAddress,
       "strAgentCtlrIOPort": strAgentCtlrIOPort,
       "strAgentnDisks": strAgentnDisks,
       "strAgentDisksTbl": strAgentDisksTbl,
       "strAgentDisksTblEntry": strAgentDisksTblEntry,
       "strAgentDiskVendor": strAgentDiskVendor,
       "strAgentDiskDescription": strAgentDiskDescription,
       "strAgentDiskFirmware": strAgentDiskFirmware,
       "strAgentDiskPort": strAgentDiskPort,
       "strAgentDiskBus": strAgentDiskBus,
       "strAgentDiskLUN": strAgentDiskLUN,
       "strAgentDiskID": strAgentDiskID,
       "strAgentDiskSerialNo": strAgentDiskSerialNo,
       "strAgentDisknSectors": strAgentDisknSectors,
       "strAgentDiskDriveLetters": strAgentDiskDriveLetters,
       "strAgentDiskSizeInMb": strAgentDiskSizeInMb,
       "strAgentDiskState": strAgentDiskState,
       "strAgentDiskXfersPerSec": strAgentDiskXfersPerSec,
       "strAgentDiskSmartCond": strAgentDiskSmartCond,
       "strAgentnFloppies": strAgentnFloppies,
       "strAgentFloppyTbl": strAgentFloppyTbl,
       "strAgentFloppyTblEntry": strAgentFloppyTblEntry,
       "strAgentFlopVendor": strAgentFlopVendor,
       "strAgentFlopDescription": strAgentFlopDescription,
       "strAgentFlopFirmware": strAgentFlopFirmware,
       "strAgentFlopSerialNo": strAgentFlopSerialNo,
       "strAgentnVolumes": strAgentnVolumes,
       "strAgentVolumesTbl": strAgentVolumesTbl,
       "strAgentVolumesTblEntry": strAgentVolumesTblEntry,
       "strAgentVolDriveLetter": strAgentVolDriveLetter,
       "strAgentVolDriveLabel": strAgentVolDriveLabel,
       "strAgentVolFileSystemType": strAgentVolFileSystemType,
       "strAgentVolCapacityInMb": strAgentVolCapacityInMb,
       "strAgentVolClusterSize": strAgentVolClusterSize,
       "strAgentVolPercentUsed": strAgentVolPercentUsed,
       "strAgentVolThreshold": strAgentVolThreshold,
       "strAgentStateThreshhold": strAgentStateThreshhold,
       "strAgentSpaceThreshhold": strAgentSpaceThreshhold,
       "strAgentCriticalVol": strAgentCriticalVol,
       "strAgentIndex": strAgentIndex,
       "sysAgent": sysAgent,
       "sysAgentMemTrap": sysAgentMemTrap,
       "sysAgentPageTrap": sysAgentPageTrap,
       "sysAgentCpuTrap": sysAgentCpuTrap,
       "sysAgentMemoryTrap": sysAgentMemoryTrap,
       "sysAgentPageFaultTrap": sysAgentPageFaultTrap,
       "sysAgentProcessorTrap": sysAgentProcessorTrap,
       "sysAgentMemOkTrap": sysAgentMemOkTrap,
       "sysAgentPageOkTrap": sysAgentPageOkTrap,
       "sysAgentCpuOKTrap": sysAgentCpuOKTrap,
       "sysAgentMemoryOkTrap": sysAgentMemoryOkTrap,
       "sysAgentPageFaultOkTrap": sysAgentPageFaultOkTrap,
       "sysAgentProcessorOKTrap": sysAgentProcessorOKTrap,
       "sysAgentVersion": sysAgentVersion,
       "sysAgentRevision": sysAgentRevision,
       "sysAgentMIBVersion": sysAgentMIBVersion,
       "sysAgentMIBRevision": sysAgentMIBRevision,
       "sysAgentCPUCyclesUsed": sysAgentCPUCyclesUsed,
       "sysAgentPCICyclesUsed": sysAgentPCICyclesUsed,
       "sysAgentInterrupts": sysAgentInterrupts,
       "sysAgentMemorySize": sysAgentMemorySize,
       "sysAgentMemoryUsed": sysAgentMemoryUsed,
       "sysAgentPageFaults": sysAgentPageFaults,
       "sysAgentPageFaultThreshhold": sysAgentPageFaultThreshhold,
       "sysAgentMemoryThreshhold": sysAgentMemoryThreshhold,
       "sysAgentCpuThreshhold": sysAgentCpuThreshhold,
       "sysAgentTotalNoCpu": sysAgentTotalNoCpu,
       "sysAgentCPUsTbl": sysAgentCPUsTbl,
       "sysAgentCPUsTblEntry": sysAgentCPUsTblEntry,
       "sysAgentCPUIndex": sysAgentCPUIndex,
       "sysAgentCPUCycleUsed": sysAgentCPUCycleUsed,
       "sysAgentIndex": sysAgentIndex}
)
