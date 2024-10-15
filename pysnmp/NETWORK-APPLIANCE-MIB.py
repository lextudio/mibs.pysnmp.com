# SNMP MIB module (NETWORK-APPLIANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETWORK-APPLIANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:17 2024
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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

netappModuleId = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 789)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Netapp_ObjectIdentity = ObjectIdentity
netapp = _Netapp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789)
)
_Netapp1_ObjectIdentity = ObjectIdentity
netapp1 = _Netapp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 1)
)


class _ProductType_Type(Integer32):
    """Custom type productType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eisaBased", 1),
          ("pciBased", 2))
    )


_ProductType_Type.__name__ = "Integer32"
_ProductType_Object = MibScalar
productType = _ProductType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 1),
    _ProductType_Type()
)
productType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productType.setStatus("current")
_ProductVersion_Type = DisplayString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 2),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")
_ProductId_Type = DisplayString
_ProductId_Object = MibScalar
productId = _ProductId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 3),
    _ProductId_Type()
)
productId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productId.setStatus("current")


class _ProductVendor_Type(Integer32):
    """Custom type productVendor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dell", 2),
          ("ibm", 3),
          ("netapp", 1))
    )


_ProductVendor_Type.__name__ = "Integer32"
_ProductVendor_Object = MibScalar
productVendor = _ProductVendor_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 4),
    _ProductVendor_Type()
)
productVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVendor.setStatus("current")
_ProductModel_Type = DisplayString
_ProductModel_Object = MibScalar
productModel = _ProductModel_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 5),
    _ProductModel_Type()
)
productModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productModel.setStatus("current")
_ProductFirmwareVersion_Type = DisplayString
_ProductFirmwareVersion_Object = MibScalar
productFirmwareVersion = _ProductFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 6),
    _ProductFirmwareVersion_Type()
)
productFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productFirmwareVersion.setStatus("current")
_ProductGuiUrl_Type = DisplayString
_ProductGuiUrl_Object = MibScalar
productGuiUrl = _ProductGuiUrl_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 7),
    _ProductGuiUrl_Type()
)
productGuiUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productGuiUrl.setStatus("current")
_ProductApiUrl_Type = DisplayString
_ProductApiUrl_Object = MibScalar
productApiUrl = _ProductApiUrl_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 8),
    _ProductApiUrl_Type()
)
productApiUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productApiUrl.setStatus("current")
_ProductSerialNum_Type = DisplayString
_ProductSerialNum_Object = MibScalar
productSerialNum = _ProductSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 9),
    _ProductSerialNum_Type()
)
productSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productSerialNum.setStatus("current")
_ProductPartnerSerialNum_Type = DisplayString
_ProductPartnerSerialNum_Object = MibScalar
productPartnerSerialNum = _ProductPartnerSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 10),
    _ProductPartnerSerialNum_Type()
)
productPartnerSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productPartnerSerialNum.setStatus("current")


class _ProductCPUArch_Type(Integer32):
    """Custom type productCPUArch based on Integer32"""
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
        *(("alpha", 2),
          ("mips", 3),
          ("sparc", 4),
          ("x86", 1))
    )


_ProductCPUArch_Type.__name__ = "Integer32"
_ProductCPUArch_Object = MibScalar
productCPUArch = _ProductCPUArch_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 11),
    _ProductCPUArch_Type()
)
productCPUArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productCPUArch.setStatus("current")
_ProductTrapData_Type = DisplayString
_ProductTrapData_Object = MibScalar
productTrapData = _ProductTrapData_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 12),
    _ProductTrapData_Type()
)
productTrapData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productTrapData.setStatus("current")
_ProductMachineType_Type = DisplayString
_ProductMachineType_Object = MibScalar
productMachineType = _ProductMachineType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 1, 13),
    _ProductMachineType_Type()
)
productMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMachineType.setStatus("current")
_SysStat_ObjectIdentity = ObjectIdentity
sysStat = _SysStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 2)
)
_Cpu_ObjectIdentity = ObjectIdentity
cpu = _Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1)
)
_CpuUpTime_Type = TimeTicks
_CpuUpTime_Object = MibScalar
cpuUpTime = _CpuUpTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 1),
    _CpuUpTime_Type()
)
cpuUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUpTime.setStatus("current")
_CpuBusyTime_Type = TimeTicks
_CpuBusyTime_Object = MibScalar
cpuBusyTime = _CpuBusyTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 2),
    _CpuBusyTime_Type()
)
cpuBusyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuBusyTime.setStatus("current")


class _CpuBusyTimePerCent_Type(Integer32):
    """Custom type cpuBusyTimePerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuBusyTimePerCent_Type.__name__ = "Integer32"
_CpuBusyTimePerCent_Object = MibScalar
cpuBusyTimePerCent = _CpuBusyTimePerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 3),
    _CpuBusyTimePerCent_Type()
)
cpuBusyTimePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuBusyTimePerCent.setStatus("current")
_CpuIdleTime_Type = TimeTicks
_CpuIdleTime_Object = MibScalar
cpuIdleTime = _CpuIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 4),
    _CpuIdleTime_Type()
)
cpuIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIdleTime.setStatus("current")


class _CpuIdleTimePerCent_Type(Integer32):
    """Custom type cpuIdleTimePerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuIdleTimePerCent_Type.__name__ = "Integer32"
_CpuIdleTimePerCent_Object = MibScalar
cpuIdleTimePerCent = _CpuIdleTimePerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 5),
    _CpuIdleTimePerCent_Type()
)
cpuIdleTimePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIdleTimePerCent.setStatus("current")


class _CpuCount_Type(Integer32):
    """Custom type cpuCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CpuCount_Type.__name__ = "Integer32"
_CpuCount_Object = MibScalar
cpuCount = _CpuCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 6),
    _CpuCount_Type()
)
cpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCount.setStatus("current")
_CpuSwitchInvocations_Type = Counter32
_CpuSwitchInvocations_Object = MibScalar
cpuSwitchInvocations = _CpuSwitchInvocations_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 7),
    _CpuSwitchInvocations_Type()
)
cpuSwitchInvocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuSwitchInvocations.setStatus("current")
_CpuContextSwitches_Type = Counter32
_CpuContextSwitches_Object = MibScalar
cpuContextSwitches = _CpuContextSwitches_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 8),
    _CpuContextSwitches_Type()
)
cpuContextSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuContextSwitches.setStatus("current")
_CpuInterrupts_Type = Counter32
_CpuInterrupts_Object = MibScalar
cpuInterrupts = _CpuInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 9),
    _CpuInterrupts_Type()
)
cpuInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuInterrupts.setStatus("current")
_CpuNonCPInterrupts_Type = Counter32
_CpuNonCPInterrupts_Object = MibScalar
cpuNonCPInterrupts = _CpuNonCPInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 10),
    _CpuNonCPInterrupts_Type()
)
cpuNonCPInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuNonCPInterrupts.setStatus("current")


class _CpuCPInterruptPercent_Type(Integer32):
    """Custom type cpuCPInterruptPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuCPInterruptPercent_Type.__name__ = "Integer32"
_CpuCPInterruptPercent_Object = MibScalar
cpuCPInterruptPercent = _CpuCPInterruptPercent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 11),
    _CpuCPInterruptPercent_Type()
)
cpuCPInterruptPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCPInterruptPercent.setStatus("current")


class _CpuNonCPInterruptPercent_Type(Integer32):
    """Custom type cpuNonCPInterruptPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuNonCPInterruptPercent_Type.__name__ = "Integer32"
_CpuNonCPInterruptPercent_Object = MibScalar
cpuNonCPInterruptPercent = _CpuNonCPInterruptPercent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 12),
    _CpuNonCPInterruptPercent_Type()
)
cpuNonCPInterruptPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuNonCPInterruptPercent.setStatus("current")
_CpuTotalDomainSwitches_Type = Counter32
_CpuTotalDomainSwitches_Object = MibScalar
cpuTotalDomainSwitches = _CpuTotalDomainSwitches_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 1, 13),
    _CpuTotalDomainSwitches_Type()
)
cpuTotalDomainSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotalDomainSwitches.setStatus("current")
_Misc_ObjectIdentity = ObjectIdentity
misc = _Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2)
)
_MiscNfsOps_Type = Integer32
_MiscNfsOps_Object = MibScalar
miscNfsOps = _MiscNfsOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 1),
    _MiscNfsOps_Type()
)
miscNfsOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscNfsOps.setStatus("deprecated")
_MiscNetRcvdKB_Type = Integer32
_MiscNetRcvdKB_Object = MibScalar
miscNetRcvdKB = _MiscNetRcvdKB_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 2),
    _MiscNetRcvdKB_Type()
)
miscNetRcvdKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscNetRcvdKB.setStatus("deprecated")
_MiscNetSentKB_Type = Integer32
_MiscNetSentKB_Object = MibScalar
miscNetSentKB = _MiscNetSentKB_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 3),
    _MiscNetSentKB_Type()
)
miscNetSentKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscNetSentKB.setStatus("deprecated")


class _MiscGlobalStatus_Type(Integer32):
    """Custom type miscGlobalStatus based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )


_MiscGlobalStatus_Type.__name__ = "Integer32"
_MiscGlobalStatus_Object = MibScalar
miscGlobalStatus = _MiscGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 4),
    _MiscGlobalStatus_Type()
)
miscGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscGlobalStatus.setStatus("current")
_MiscHighNfsOps_Type = Counter32
_MiscHighNfsOps_Object = MibScalar
miscHighNfsOps = _MiscHighNfsOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 5),
    _MiscHighNfsOps_Type()
)
miscHighNfsOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscHighNfsOps.setStatus("current")
_MiscLowNfsOps_Type = Counter32
_MiscLowNfsOps_Object = MibScalar
miscLowNfsOps = _MiscLowNfsOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 6),
    _MiscLowNfsOps_Type()
)
miscLowNfsOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscLowNfsOps.setStatus("current")
_MiscHighCifsOps_Type = Counter32
_MiscHighCifsOps_Object = MibScalar
miscHighCifsOps = _MiscHighCifsOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 7),
    _MiscHighCifsOps_Type()
)
miscHighCifsOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscHighCifsOps.setStatus("current")
_MiscLowCifsOps_Type = Counter32
_MiscLowCifsOps_Object = MibScalar
miscLowCifsOps = _MiscLowCifsOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 8),
    _MiscLowCifsOps_Type()
)
miscLowCifsOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscLowCifsOps.setStatus("current")
_MiscHighHttpOps_Type = Counter32
_MiscHighHttpOps_Object = MibScalar
miscHighHttpOps = _MiscHighHttpOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 9),
    _MiscHighHttpOps_Type()
)
miscHighHttpOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscHighHttpOps.setStatus("current")
_MiscLowHttpOps_Type = Counter32
_MiscLowHttpOps_Object = MibScalar
miscLowHttpOps = _MiscLowHttpOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 10),
    _MiscLowHttpOps_Type()
)
miscLowHttpOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscLowHttpOps.setStatus("current")
_MiscHighNetRcvdBytes_Type = Counter32
_MiscHighNetRcvdBytes_Object = MibScalar
miscHighNetRcvdBytes = _MiscHighNetRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 11),
    _MiscHighNetRcvdBytes_Type()
)
miscHighNetRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscHighNetRcvdBytes.setStatus("current")
_MiscLowNetRcvdBytes_Type = Counter32
_MiscLowNetRcvdBytes_Object = MibScalar
miscLowNetRcvdBytes = _MiscLowNetRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 12),
    _MiscLowNetRcvdBytes_Type()
)
miscLowNetRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscLowNetRcvdBytes.setStatus("current")
_MiscHighNetSentBytes_Type = Counter32
_MiscHighNetSentBytes_Object = MibScalar
miscHighNetSentBytes = _MiscHighNetSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 13),
    _MiscHighNetSentBytes_Type()
)
miscHighNetSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscHighNetSentBytes.setStatus("current")
_MiscLowNetSentBytes_Type = Counter32
_MiscLowNetSentBytes_Object = MibScalar
miscLowNetSentBytes = _MiscLowNetSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 14),
    _MiscLowNetSentBytes_Type()
)
miscLowNetSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscLowNetSentBytes.setStatus("current")
_MiscHighDiskReadBytes_Type = Counter32
_MiscHighDiskReadBytes_Object = MibScalar
miscHighDiskReadBytes = _MiscHighDiskReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 15),
    _MiscHighDiskReadBytes_Type()
)
miscHighDiskReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscHighDiskReadBytes.setStatus("current")
_MiscLowDiskReadBytes_Type = Counter32
_MiscLowDiskReadBytes_Object = MibScalar
miscLowDiskReadBytes = _MiscLowDiskReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 16),
    _MiscLowDiskReadBytes_Type()
)
miscLowDiskReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscLowDiskReadBytes.setStatus("current")
_MiscHighDiskWriteBytes_Type = Counter32
_MiscHighDiskWriteBytes_Object = MibScalar
miscHighDiskWriteBytes = _MiscHighDiskWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 17),
    _MiscHighDiskWriteBytes_Type()
)
miscHighDiskWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscHighDiskWriteBytes.setStatus("current")
_MiscLowDiskWriteBytes_Type = Counter32
_MiscLowDiskWriteBytes_Object = MibScalar
miscLowDiskWriteBytes = _MiscLowDiskWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 18),
    _MiscLowDiskWriteBytes_Type()
)
miscLowDiskWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscLowDiskWriteBytes.setStatus("current")
_MiscHighTapeReadBytes_Type = Counter32
_MiscHighTapeReadBytes_Object = MibScalar
miscHighTapeReadBytes = _MiscHighTapeReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 19),
    _MiscHighTapeReadBytes_Type()
)
miscHighTapeReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscHighTapeReadBytes.setStatus("current")
_MiscLowTapeReadBytes_Type = Counter32
_MiscLowTapeReadBytes_Object = MibScalar
miscLowTapeReadBytes = _MiscLowTapeReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 20),
    _MiscLowTapeReadBytes_Type()
)
miscLowTapeReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscLowTapeReadBytes.setStatus("current")
_MiscHighTapeWriteBytes_Type = Counter32
_MiscHighTapeWriteBytes_Object = MibScalar
miscHighTapeWriteBytes = _MiscHighTapeWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 21),
    _MiscHighTapeWriteBytes_Type()
)
miscHighTapeWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscHighTapeWriteBytes.setStatus("current")
_MiscLowTapeWriteBytes_Type = Counter32
_MiscLowTapeWriteBytes_Object = MibScalar
miscLowTapeWriteBytes = _MiscLowTapeWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 22),
    _MiscLowTapeWriteBytes_Type()
)
miscLowTapeWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscLowTapeWriteBytes.setStatus("current")
_MiscCacheAge_Type = Integer32
_MiscCacheAge_Object = MibScalar
miscCacheAge = _MiscCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 23),
    _MiscCacheAge_Type()
)
miscCacheAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscCacheAge.setStatus("current")
_MiscCorrectedMachineChecks_Type = Counter32
_MiscCorrectedMachineChecks_Object = MibScalar
miscCorrectedMachineChecks = _MiscCorrectedMachineChecks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 24),
    _MiscCorrectedMachineChecks_Type()
)
miscCorrectedMachineChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscCorrectedMachineChecks.setStatus("current")
_MiscGlobalStatusMessage_Type = DisplayString
_MiscGlobalStatusMessage_Object = MibScalar
miscGlobalStatusMessage = _MiscGlobalStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 25),
    _MiscGlobalStatusMessage_Type()
)
miscGlobalStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscGlobalStatusMessage.setStatus("current")
_MiscWindowsSetupWizardVersion_Type = Integer32
_MiscWindowsSetupWizardVersion_Object = MibScalar
miscWindowsSetupWizardVersion = _MiscWindowsSetupWizardVersion_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 26),
    _MiscWindowsSetupWizardVersion_Type()
)
miscWindowsSetupWizardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscWindowsSetupWizardVersion.setStatus("current")
_Misc64NfsOps_Type = Counter64
_Misc64NfsOps_Object = MibScalar
misc64NfsOps = _Misc64NfsOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 27),
    _Misc64NfsOps_Type()
)
misc64NfsOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    misc64NfsOps.setStatus("current")
_Misc64CifsOps_Type = Counter64
_Misc64CifsOps_Object = MibScalar
misc64CifsOps = _Misc64CifsOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 28),
    _Misc64CifsOps_Type()
)
misc64CifsOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    misc64CifsOps.setStatus("current")
_Misc64HttpOps_Type = Counter64
_Misc64HttpOps_Object = MibScalar
misc64HttpOps = _Misc64HttpOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 29),
    _Misc64HttpOps_Type()
)
misc64HttpOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    misc64HttpOps.setStatus("current")
_Misc64NetRcvdBytes_Type = Counter64
_Misc64NetRcvdBytes_Object = MibScalar
misc64NetRcvdBytes = _Misc64NetRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 30),
    _Misc64NetRcvdBytes_Type()
)
misc64NetRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    misc64NetRcvdBytes.setStatus("current")
_Misc64NetSentBytes_Type = Counter64
_Misc64NetSentBytes_Object = MibScalar
misc64NetSentBytes = _Misc64NetSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 31),
    _Misc64NetSentBytes_Type()
)
misc64NetSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    misc64NetSentBytes.setStatus("current")
_Misc64DiskReadBytes_Type = Counter64
_Misc64DiskReadBytes_Object = MibScalar
misc64DiskReadBytes = _Misc64DiskReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 32),
    _Misc64DiskReadBytes_Type()
)
misc64DiskReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    misc64DiskReadBytes.setStatus("current")
_Misc64DiskWriteBytes_Type = Counter64
_Misc64DiskWriteBytes_Object = MibScalar
misc64DiskWriteBytes = _Misc64DiskWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 33),
    _Misc64DiskWriteBytes_Type()
)
misc64DiskWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    misc64DiskWriteBytes.setStatus("current")
_Misc64TapeReadBytes_Type = Counter64
_Misc64TapeReadBytes_Object = MibScalar
misc64TapeReadBytes = _Misc64TapeReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 34),
    _Misc64TapeReadBytes_Type()
)
misc64TapeReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    misc64TapeReadBytes.setStatus("current")
_Misc64TapeWriteBytes_Type = Counter64
_Misc64TapeWriteBytes_Object = MibScalar
misc64TapeWriteBytes = _Misc64TapeWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 2, 35),
    _Misc64TapeWriteBytes_Type()
)
misc64TapeWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    misc64TapeWriteBytes.setStatus("current")
_Cf_ObjectIdentity = ObjectIdentity
cf = _Cf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 3)
)


class _CfSettings_Type(Integer32):
    """Custom type cfSettings based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 2),
          ("notConfigured", 1),
          ("takeoverByPartnerDisabled", 4),
          ("thisNodeDead", 5))
    )


_CfSettings_Type.__name__ = "Integer32"
_CfSettings_Object = MibScalar
cfSettings = _CfSettings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 3, 1),
    _CfSettings_Type()
)
cfSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSettings.setStatus("current")


class _CfState_Type(Integer32):
    """Custom type cfState based on Integer32"""
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
        *(("canTakeover", 2),
          ("cannotTakeover", 3),
          ("dead", 1),
          ("takeover", 4))
    )


_CfState_Type.__name__ = "Integer32"
_CfState_Object = MibScalar
cfState = _CfState_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 3, 2),
    _CfState_Type()
)
cfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfState.setStatus("current")


class _CfCannotTakeoverCause_Type(Integer32):
    """Custom type cfCannotTakeoverCause based on Integer32"""
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
        *(("disabledByOperator", 3),
          ("disabledByPartner", 5),
          ("interconnectOffline", 4),
          ("ok", 1),
          ("takeoverFailed", 6),
          ("unknownReason", 2))
    )


_CfCannotTakeoverCause_Type.__name__ = "Integer32"
_CfCannotTakeoverCause_Object = MibScalar
cfCannotTakeoverCause = _CfCannotTakeoverCause_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 3, 3),
    _CfCannotTakeoverCause_Type()
)
cfCannotTakeoverCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfCannotTakeoverCause.setStatus("current")


class _CfPartnerStatus_Type(Integer32):
    """Custom type cfPartnerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dead", 3),
          ("maybeDown", 1),
          ("ok", 2))
    )


_CfPartnerStatus_Type.__name__ = "Integer32"
_CfPartnerStatus_Object = MibScalar
cfPartnerStatus = _CfPartnerStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 3, 4),
    _CfPartnerStatus_Type()
)
cfPartnerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfPartnerStatus.setStatus("current")
_CfPartnerLastStatusUpdate_Type = TimeTicks
_CfPartnerLastStatusUpdate_Object = MibScalar
cfPartnerLastStatusUpdate = _CfPartnerLastStatusUpdate_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 3, 5),
    _CfPartnerLastStatusUpdate_Type()
)
cfPartnerLastStatusUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfPartnerLastStatusUpdate.setStatus("current")
_CfPartnerName_Type = DisplayString
_CfPartnerName_Object = MibScalar
cfPartnerName = _CfPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 3, 6),
    _CfPartnerName_Type()
)
cfPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfPartnerName.setStatus("current")
_CfPartnerSysid_Type = Integer32
_CfPartnerSysid_Object = MibScalar
cfPartnerSysid = _CfPartnerSysid_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 3, 7),
    _CfPartnerSysid_Type()
)
cfPartnerSysid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfPartnerSysid.setStatus("current")


class _CfInterconnectStatus_Type(Integer32):
    """Custom type cfInterconnectStatus based on Integer32"""
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
        *(("down", 2),
          ("notPresent", 1),
          ("partialFailure", 3),
          ("up", 4))
    )


_CfInterconnectStatus_Type.__name__ = "Integer32"
_CfInterconnectStatus_Object = MibScalar
cfInterconnectStatus = _CfInterconnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 3, 8),
    _CfInterconnectStatus_Type()
)
cfInterconnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfInterconnectStatus.setStatus("current")
_Environment_ObjectIdentity = ObjectIdentity
environment = _Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 4)
)


class _EnvOverTemperature_Type(Integer32):
    """Custom type envOverTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_EnvOverTemperature_Type.__name__ = "Integer32"
_EnvOverTemperature_Object = MibScalar
envOverTemperature = _EnvOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 4, 1),
    _EnvOverTemperature_Type()
)
envOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envOverTemperature.setStatus("current")
_EnvFailedFanCount_Type = Integer32
_EnvFailedFanCount_Object = MibScalar
envFailedFanCount = _EnvFailedFanCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 4, 2),
    _EnvFailedFanCount_Type()
)
envFailedFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFailedFanCount.setStatus("current")
_EnvFailedFanMessage_Type = DisplayString
_EnvFailedFanMessage_Object = MibScalar
envFailedFanMessage = _EnvFailedFanMessage_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 4, 3),
    _EnvFailedFanMessage_Type()
)
envFailedFanMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFailedFanMessage.setStatus("current")
_EnvFailedPowerSupplyCount_Type = Integer32
_EnvFailedPowerSupplyCount_Object = MibScalar
envFailedPowerSupplyCount = _EnvFailedPowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 4, 4),
    _EnvFailedPowerSupplyCount_Type()
)
envFailedPowerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFailedPowerSupplyCount.setStatus("current")
_EnvFailedPowerSupplyMessage_Type = DisplayString
_EnvFailedPowerSupplyMessage_Object = MibScalar
envFailedPowerSupplyMessage = _EnvFailedPowerSupplyMessage_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 4, 5),
    _EnvFailedPowerSupplyMessage_Type()
)
envFailedPowerSupplyMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFailedPowerSupplyMessage.setStatus("current")
_Nvram_ObjectIdentity = ObjectIdentity
nvram = _Nvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 5)
)


class _NvramBatteryStatus_Type(Integer32):
    """Custom type nvramBatteryStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("atEndOfLife", 6),
          ("fullyCharged", 9),
          ("fullyDischarged", 3),
          ("nearEndOfLife", 5),
          ("notPresent", 4),
          ("ok", 1),
          ("overCharged", 8),
          ("partiallyDischarged", 2),
          ("unknown", 7))
    )


_NvramBatteryStatus_Type.__name__ = "Integer32"
_NvramBatteryStatus_Object = MibScalar
nvramBatteryStatus = _NvramBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 5, 1),
    _NvramBatteryStatus_Type()
)
nvramBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramBatteryStatus.setStatus("current")
_Cp_ObjectIdentity = ObjectIdentity
cp = _Cp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6)
)
_CpTime_Type = TimeTicks
_CpTime_Object = MibScalar
cpTime = _CpTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 1),
    _CpTime_Type()
)
cpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpTime.setStatus("current")
_CpFromTimerOps_Type = Counter32
_CpFromTimerOps_Object = MibScalar
cpFromTimerOps = _CpFromTimerOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 2),
    _CpFromTimerOps_Type()
)
cpFromTimerOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpFromTimerOps.setStatus("current")
_CpFromSnapshotOps_Type = Counter32
_CpFromSnapshotOps_Object = MibScalar
cpFromSnapshotOps = _CpFromSnapshotOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 3),
    _CpFromSnapshotOps_Type()
)
cpFromSnapshotOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpFromSnapshotOps.setStatus("current")
_CpFromLowWaterOps_Type = Counter32
_CpFromLowWaterOps_Object = MibScalar
cpFromLowWaterOps = _CpFromLowWaterOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 4),
    _CpFromLowWaterOps_Type()
)
cpFromLowWaterOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpFromLowWaterOps.setStatus("current")
_CpFromHighWaterOps_Type = Counter32
_CpFromHighWaterOps_Object = MibScalar
cpFromHighWaterOps = _CpFromHighWaterOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 5),
    _CpFromHighWaterOps_Type()
)
cpFromHighWaterOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpFromHighWaterOps.setStatus("current")
_CpFromLogFullOps_Type = Counter32
_CpFromLogFullOps_Object = MibScalar
cpFromLogFullOps = _CpFromLogFullOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 6),
    _CpFromLogFullOps_Type()
)
cpFromLogFullOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpFromLogFullOps.setStatus("current")
_CpFromCpOps_Type = Counter32
_CpFromCpOps_Object = MibScalar
cpFromCpOps = _CpFromCpOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 7),
    _CpFromCpOps_Type()
)
cpFromCpOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpFromCpOps.setStatus("current")
_CpTotalOps_Type = Counter32
_CpTotalOps_Object = MibScalar
cpTotalOps = _CpTotalOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 8),
    _CpTotalOps_Type()
)
cpTotalOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpTotalOps.setStatus("current")
_CpFromFlushOps_Type = Counter32
_CpFromFlushOps_Object = MibScalar
cpFromFlushOps = _CpFromFlushOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 9),
    _CpFromFlushOps_Type()
)
cpFromFlushOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpFromFlushOps.setStatus("current")
_CpFromSyncOps_Type = Counter32
_CpFromSyncOps_Object = MibScalar
cpFromSyncOps = _CpFromSyncOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 10),
    _CpFromSyncOps_Type()
)
cpFromSyncOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpFromSyncOps.setStatus("current")
_CpFromLowVbufOps_Type = Counter32
_CpFromLowVbufOps_Object = MibScalar
cpFromLowVbufOps = _CpFromLowVbufOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 11),
    _CpFromLowVbufOps_Type()
)
cpFromLowVbufOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpFromLowVbufOps.setStatus("current")
_CpFromCpDeferredOps_Type = Counter32
_CpFromCpDeferredOps_Object = MibScalar
cpFromCpDeferredOps = _CpFromCpDeferredOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 12),
    _CpFromCpDeferredOps_Type()
)
cpFromCpDeferredOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpFromCpDeferredOps.setStatus("current")
_CpFromLowDatavecsOps_Type = Counter32
_CpFromLowDatavecsOps_Object = MibScalar
cpFromLowDatavecsOps = _CpFromLowDatavecsOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 6, 13),
    _CpFromLowDatavecsOps_Type()
)
cpFromLowDatavecsOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpFromLowDatavecsOps.setStatus("current")
_Autosupport_ObjectIdentity = ObjectIdentity
autosupport = _Autosupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 7)
)


class _AutosupportStatus_Type(Integer32):
    """Custom type autosupportStatus based on Integer32"""
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
        *(("ok", 1),
          ("postFailure", 3),
          ("smtpFailure", 2),
          ("smtpPostFailure", 4),
          ("unknown", 5))
    )


_AutosupportStatus_Type.__name__ = "Integer32"
_AutosupportStatus_Object = MibScalar
autosupportStatus = _AutosupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 7, 1),
    _AutosupportStatus_Type()
)
autosupportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autosupportStatus.setStatus("current")
_AutosupportStatusMessage_Type = DisplayString
_AutosupportStatusMessage_Object = MibScalar
autosupportStatusMessage = _AutosupportStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 7, 2),
    _AutosupportStatusMessage_Type()
)
autosupportStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autosupportStatusMessage.setStatus("current")
_AutosupportSuccessfulSends_Type = Counter32
_AutosupportSuccessfulSends_Object = MibScalar
autosupportSuccessfulSends = _AutosupportSuccessfulSends_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 7, 3),
    _AutosupportSuccessfulSends_Type()
)
autosupportSuccessfulSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autosupportSuccessfulSends.setStatus("current")
_AutosupportFailedSends_Type = Counter32
_AutosupportFailedSends_Object = MibScalar
autosupportFailedSends = _AutosupportFailedSends_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 2, 7, 4),
    _AutosupportFailedSends_Type()
)
autosupportFailedSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autosupportFailedSends.setStatus("current")
_Nfs_ObjectIdentity = ObjectIdentity
nfs = _Nfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3)
)
_CurNfs_ObjectIdentity = ObjectIdentity
curNfs = _CurNfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1)
)
_RpcServ_ObjectIdentity = ObjectIdentity
rpcServ = _RpcServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1)
)
_RpcCalls_Type = Counter32
_RpcCalls_Object = MibScalar
rpcCalls = _RpcCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 1),
    _RpcCalls_Type()
)
rpcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcCalls.setStatus("current")
_RpcBadCalls_Type = Counter32
_RpcBadCalls_Object = MibScalar
rpcBadCalls = _RpcBadCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 2),
    _RpcBadCalls_Type()
)
rpcBadCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcBadCalls.setStatus("current")
_RpcNullRecvs_Type = Counter32
_RpcNullRecvs_Object = MibScalar
rpcNullRecvs = _RpcNullRecvs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 3),
    _RpcNullRecvs_Type()
)
rpcNullRecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcNullRecvs.setStatus("current")
_RpcBadLens_Type = Counter32
_RpcBadLens_Object = MibScalar
rpcBadLens = _RpcBadLens_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 4),
    _RpcBadLens_Type()
)
rpcBadLens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcBadLens.setStatus("current")
_RpcServXDRCalls_Type = Counter32
_RpcServXDRCalls_Object = MibScalar
rpcServXDRCalls = _RpcServXDRCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 5),
    _RpcServXDRCalls_Type()
)
rpcServXDRCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcServXDRCalls.setStatus("current")
_RcpTcpCalls_Type = Counter32
_RcpTcpCalls_Object = MibScalar
rcpTcpCalls = _RcpTcpCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 6),
    _RcpTcpCalls_Type()
)
rcpTcpCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcpTcpCalls.setStatus("current")
_RcpTcpBadCalls_Type = Counter32
_RcpTcpBadCalls_Object = MibScalar
rcpTcpBadCalls = _RcpTcpBadCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 7),
    _RcpTcpBadCalls_Type()
)
rcpTcpBadCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcpTcpBadCalls.setStatus("current")
_RcpTcpNullRecvs_Type = Counter32
_RcpTcpNullRecvs_Object = MibScalar
rcpTcpNullRecvs = _RcpTcpNullRecvs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 8),
    _RcpTcpNullRecvs_Type()
)
rcpTcpNullRecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcpTcpNullRecvs.setStatus("current")
_RcpTcpBadLens_Type = Counter32
_RcpTcpBadLens_Object = MibScalar
rcpTcpBadLens = _RcpTcpBadLens_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 9),
    _RcpTcpBadLens_Type()
)
rcpTcpBadLens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcpTcpBadLens.setStatus("current")
_RcpTcpServXDRCalls_Type = Counter32
_RcpTcpServXDRCalls_Object = MibScalar
rcpTcpServXDRCalls = _RcpTcpServXDRCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 10),
    _RcpTcpServXDRCalls_Type()
)
rcpTcpServXDRCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcpTcpServXDRCalls.setStatus("current")
_RpcUdpCalls_Type = Counter32
_RpcUdpCalls_Object = MibScalar
rpcUdpCalls = _RpcUdpCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 11),
    _RpcUdpCalls_Type()
)
rpcUdpCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcUdpCalls.setStatus("current")
_RpcUdpBadCalls_Type = Counter32
_RpcUdpBadCalls_Object = MibScalar
rpcUdpBadCalls = _RpcUdpBadCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 12),
    _RpcUdpBadCalls_Type()
)
rpcUdpBadCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcUdpBadCalls.setStatus("current")
_RpcUdpNullRecvs_Type = Counter32
_RpcUdpNullRecvs_Object = MibScalar
rpcUdpNullRecvs = _RpcUdpNullRecvs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 13),
    _RpcUdpNullRecvs_Type()
)
rpcUdpNullRecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcUdpNullRecvs.setStatus("current")
_RpcUdpBadLens_Type = Counter32
_RpcUdpBadLens_Object = MibScalar
rpcUdpBadLens = _RpcUdpBadLens_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 14),
    _RpcUdpBadLens_Type()
)
rpcUdpBadLens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcUdpBadLens.setStatus("current")
_RpcUdpServXDRCalls_Type = Counter32
_RpcUdpServXDRCalls_Object = MibScalar
rpcUdpServXDRCalls = _RpcUdpServXDRCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 1, 15),
    _RpcUdpServXDRCalls_Type()
)
rpcUdpServXDRCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpcUdpServXDRCalls.setStatus("current")
_NfsServ_ObjectIdentity = ObjectIdentity
nfsServ = _NfsServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2)
)
_NfsCalls_Type = Counter32
_NfsCalls_Object = MibScalar
nfsCalls = _NfsCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 1),
    _NfsCalls_Type()
)
nfsCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCalls.setStatus("current")
_NfsServBadCalls_Type = Counter32
_NfsServBadCalls_Object = MibScalar
nfsServBadCalls = _NfsServBadCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 2),
    _NfsServBadCalls_Type()
)
nfsServBadCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsServBadCalls.setStatus("current")
_NfsV2_ObjectIdentity = ObjectIdentity
nfsV2 = _NfsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3)
)
_V2Calls_ObjectIdentity = ObjectIdentity
v2Calls = _V2Calls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1)
)
_V2cNulls_Type = Counter32
_V2cNulls_Object = MibScalar
v2cNulls = _V2cNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 1),
    _V2cNulls_Type()
)
v2cNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cNulls.setStatus("current")
_V2cGetattrs_Type = Counter32
_V2cGetattrs_Object = MibScalar
v2cGetattrs = _V2cGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 2),
    _V2cGetattrs_Type()
)
v2cGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cGetattrs.setStatus("current")
_V2cSetattrs_Type = Counter32
_V2cSetattrs_Object = MibScalar
v2cSetattrs = _V2cSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 3),
    _V2cSetattrs_Type()
)
v2cSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cSetattrs.setStatus("current")
_V2cRoots_Type = Counter32
_V2cRoots_Object = MibScalar
v2cRoots = _V2cRoots_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 4),
    _V2cRoots_Type()
)
v2cRoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cRoots.setStatus("current")
_V2cLookups_Type = Counter32
_V2cLookups_Object = MibScalar
v2cLookups = _V2cLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 5),
    _V2cLookups_Type()
)
v2cLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cLookups.setStatus("current")
_V2cReadlinks_Type = Counter32
_V2cReadlinks_Object = MibScalar
v2cReadlinks = _V2cReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 6),
    _V2cReadlinks_Type()
)
v2cReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cReadlinks.setStatus("current")
_V2cReads_Type = Counter32
_V2cReads_Object = MibScalar
v2cReads = _V2cReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 7),
    _V2cReads_Type()
)
v2cReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cReads.setStatus("current")
_V2cWrcaches_Type = Counter32
_V2cWrcaches_Object = MibScalar
v2cWrcaches = _V2cWrcaches_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 8),
    _V2cWrcaches_Type()
)
v2cWrcaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cWrcaches.setStatus("current")
_V2cWrites_Type = Counter32
_V2cWrites_Object = MibScalar
v2cWrites = _V2cWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 9),
    _V2cWrites_Type()
)
v2cWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cWrites.setStatus("current")
_V2cCreates_Type = Counter32
_V2cCreates_Object = MibScalar
v2cCreates = _V2cCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 10),
    _V2cCreates_Type()
)
v2cCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cCreates.setStatus("current")
_V2cRemoves_Type = Counter32
_V2cRemoves_Object = MibScalar
v2cRemoves = _V2cRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 11),
    _V2cRemoves_Type()
)
v2cRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cRemoves.setStatus("current")
_V2cRenames_Type = Counter32
_V2cRenames_Object = MibScalar
v2cRenames = _V2cRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 12),
    _V2cRenames_Type()
)
v2cRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cRenames.setStatus("current")
_V2cLinks_Type = Counter32
_V2cLinks_Object = MibScalar
v2cLinks = _V2cLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 13),
    _V2cLinks_Type()
)
v2cLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cLinks.setStatus("current")
_V2cSymlinks_Type = Counter32
_V2cSymlinks_Object = MibScalar
v2cSymlinks = _V2cSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 14),
    _V2cSymlinks_Type()
)
v2cSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cSymlinks.setStatus("current")
_V2cMkdirs_Type = Counter32
_V2cMkdirs_Object = MibScalar
v2cMkdirs = _V2cMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 15),
    _V2cMkdirs_Type()
)
v2cMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cMkdirs.setStatus("current")
_V2cRmdirs_Type = Counter32
_V2cRmdirs_Object = MibScalar
v2cRmdirs = _V2cRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 16),
    _V2cRmdirs_Type()
)
v2cRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cRmdirs.setStatus("current")
_V2cReaddirs_Type = Counter32
_V2cReaddirs_Object = MibScalar
v2cReaddirs = _V2cReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 17),
    _V2cReaddirs_Type()
)
v2cReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cReaddirs.setStatus("current")
_V2cStatfss_Type = Counter32
_V2cStatfss_Object = MibScalar
v2cStatfss = _V2cStatfss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 1, 18),
    _V2cStatfss_Type()
)
v2cStatfss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cStatfss.setStatus("current")
_V2Percent_ObjectIdentity = ObjectIdentity
v2Percent = _V2Percent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2)
)


class _V2pNulls_Type(Integer32):
    """Custom type v2pNulls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pNulls_Type.__name__ = "Integer32"
_V2pNulls_Object = MibScalar
v2pNulls = _V2pNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 1),
    _V2pNulls_Type()
)
v2pNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pNulls.setStatus("current")


class _V2pGetattrs_Type(Integer32):
    """Custom type v2pGetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pGetattrs_Type.__name__ = "Integer32"
_V2pGetattrs_Object = MibScalar
v2pGetattrs = _V2pGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 2),
    _V2pGetattrs_Type()
)
v2pGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pGetattrs.setStatus("current")


class _V2pSetattrs_Type(Integer32):
    """Custom type v2pSetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pSetattrs_Type.__name__ = "Integer32"
_V2pSetattrs_Object = MibScalar
v2pSetattrs = _V2pSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 3),
    _V2pSetattrs_Type()
)
v2pSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pSetattrs.setStatus("current")


class _V2pRoots_Type(Integer32):
    """Custom type v2pRoots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pRoots_Type.__name__ = "Integer32"
_V2pRoots_Object = MibScalar
v2pRoots = _V2pRoots_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 4),
    _V2pRoots_Type()
)
v2pRoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pRoots.setStatus("current")


class _V2pLookups_Type(Integer32):
    """Custom type v2pLookups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pLookups_Type.__name__ = "Integer32"
_V2pLookups_Object = MibScalar
v2pLookups = _V2pLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 5),
    _V2pLookups_Type()
)
v2pLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pLookups.setStatus("current")


class _V2pReadlinks_Type(Integer32):
    """Custom type v2pReadlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pReadlinks_Type.__name__ = "Integer32"
_V2pReadlinks_Object = MibScalar
v2pReadlinks = _V2pReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 6),
    _V2pReadlinks_Type()
)
v2pReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pReadlinks.setStatus("current")


class _V2pReads_Type(Integer32):
    """Custom type v2pReads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pReads_Type.__name__ = "Integer32"
_V2pReads_Object = MibScalar
v2pReads = _V2pReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 7),
    _V2pReads_Type()
)
v2pReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pReads.setStatus("current")


class _V2pWrcaches_Type(Integer32):
    """Custom type v2pWrcaches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pWrcaches_Type.__name__ = "Integer32"
_V2pWrcaches_Object = MibScalar
v2pWrcaches = _V2pWrcaches_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 8),
    _V2pWrcaches_Type()
)
v2pWrcaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pWrcaches.setStatus("current")


class _V2pWrites_Type(Integer32):
    """Custom type v2pWrites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pWrites_Type.__name__ = "Integer32"
_V2pWrites_Object = MibScalar
v2pWrites = _V2pWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 9),
    _V2pWrites_Type()
)
v2pWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pWrites.setStatus("current")


class _V2pCreates_Type(Integer32):
    """Custom type v2pCreates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pCreates_Type.__name__ = "Integer32"
_V2pCreates_Object = MibScalar
v2pCreates = _V2pCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 10),
    _V2pCreates_Type()
)
v2pCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pCreates.setStatus("current")


class _V2pRemoves_Type(Integer32):
    """Custom type v2pRemoves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pRemoves_Type.__name__ = "Integer32"
_V2pRemoves_Object = MibScalar
v2pRemoves = _V2pRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 11),
    _V2pRemoves_Type()
)
v2pRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pRemoves.setStatus("current")


class _V2pRenames_Type(Integer32):
    """Custom type v2pRenames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pRenames_Type.__name__ = "Integer32"
_V2pRenames_Object = MibScalar
v2pRenames = _V2pRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 12),
    _V2pRenames_Type()
)
v2pRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pRenames.setStatus("current")


class _V2pLinks_Type(Integer32):
    """Custom type v2pLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pLinks_Type.__name__ = "Integer32"
_V2pLinks_Object = MibScalar
v2pLinks = _V2pLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 13),
    _V2pLinks_Type()
)
v2pLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pLinks.setStatus("current")


class _V2pSymlinks_Type(Integer32):
    """Custom type v2pSymlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pSymlinks_Type.__name__ = "Integer32"
_V2pSymlinks_Object = MibScalar
v2pSymlinks = _V2pSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 14),
    _V2pSymlinks_Type()
)
v2pSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pSymlinks.setStatus("current")


class _V2pMkdirs_Type(Integer32):
    """Custom type v2pMkdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pMkdirs_Type.__name__ = "Integer32"
_V2pMkdirs_Object = MibScalar
v2pMkdirs = _V2pMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 15),
    _V2pMkdirs_Type()
)
v2pMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pMkdirs.setStatus("current")


class _V2pRmdirs_Type(Integer32):
    """Custom type v2pRmdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pRmdirs_Type.__name__ = "Integer32"
_V2pRmdirs_Object = MibScalar
v2pRmdirs = _V2pRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 16),
    _V2pRmdirs_Type()
)
v2pRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pRmdirs.setStatus("current")


class _V2pReaddirs_Type(Integer32):
    """Custom type v2pReaddirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pReaddirs_Type.__name__ = "Integer32"
_V2pReaddirs_Object = MibScalar
v2pReaddirs = _V2pReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 17),
    _V2pReaddirs_Type()
)
v2pReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pReaddirs.setStatus("current")


class _V2pStatfss_Type(Integer32):
    """Custom type v2pStatfss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2pStatfss_Type.__name__ = "Integer32"
_V2pStatfss_Object = MibScalar
v2pStatfss = _V2pStatfss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 2, 18),
    _V2pStatfss_Type()
)
v2pStatfss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2pStatfss.setStatus("current")
_V2CachedCalls_ObjectIdentity = ObjectIdentity
v2CachedCalls = _V2CachedCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3)
)
_V2ccNulls_Type = Counter32
_V2ccNulls_Object = MibScalar
v2ccNulls = _V2ccNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 1),
    _V2ccNulls_Type()
)
v2ccNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccNulls.setStatus("current")
_V2ccGetattrs_Type = Counter32
_V2ccGetattrs_Object = MibScalar
v2ccGetattrs = _V2ccGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 2),
    _V2ccGetattrs_Type()
)
v2ccGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccGetattrs.setStatus("current")
_V2ccSetattrs_Type = Counter32
_V2ccSetattrs_Object = MibScalar
v2ccSetattrs = _V2ccSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 3),
    _V2ccSetattrs_Type()
)
v2ccSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccSetattrs.setStatus("current")
_V2ccRoots_Type = Counter32
_V2ccRoots_Object = MibScalar
v2ccRoots = _V2ccRoots_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 4),
    _V2ccRoots_Type()
)
v2ccRoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccRoots.setStatus("current")
_V2ccLookups_Type = Counter32
_V2ccLookups_Object = MibScalar
v2ccLookups = _V2ccLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 5),
    _V2ccLookups_Type()
)
v2ccLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccLookups.setStatus("current")
_V2ccReadlinks_Type = Counter32
_V2ccReadlinks_Object = MibScalar
v2ccReadlinks = _V2ccReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 6),
    _V2ccReadlinks_Type()
)
v2ccReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccReadlinks.setStatus("current")
_V2ccReads_Type = Counter32
_V2ccReads_Object = MibScalar
v2ccReads = _V2ccReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 7),
    _V2ccReads_Type()
)
v2ccReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccReads.setStatus("current")
_V2ccWrcaches_Type = Counter32
_V2ccWrcaches_Object = MibScalar
v2ccWrcaches = _V2ccWrcaches_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 8),
    _V2ccWrcaches_Type()
)
v2ccWrcaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccWrcaches.setStatus("current")
_V2ccWrites_Type = Counter32
_V2ccWrites_Object = MibScalar
v2ccWrites = _V2ccWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 9),
    _V2ccWrites_Type()
)
v2ccWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccWrites.setStatus("current")
_V2ccCreates_Type = Counter32
_V2ccCreates_Object = MibScalar
v2ccCreates = _V2ccCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 10),
    _V2ccCreates_Type()
)
v2ccCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccCreates.setStatus("current")
_V2ccRemoves_Type = Counter32
_V2ccRemoves_Object = MibScalar
v2ccRemoves = _V2ccRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 11),
    _V2ccRemoves_Type()
)
v2ccRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccRemoves.setStatus("current")
_V2ccRenames_Type = Counter32
_V2ccRenames_Object = MibScalar
v2ccRenames = _V2ccRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 12),
    _V2ccRenames_Type()
)
v2ccRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccRenames.setStatus("current")
_V2ccLinks_Type = Counter32
_V2ccLinks_Object = MibScalar
v2ccLinks = _V2ccLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 13),
    _V2ccLinks_Type()
)
v2ccLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccLinks.setStatus("current")
_V2ccSymlinks_Type = Counter32
_V2ccSymlinks_Object = MibScalar
v2ccSymlinks = _V2ccSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 14),
    _V2ccSymlinks_Type()
)
v2ccSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccSymlinks.setStatus("current")
_V2ccMkdirs_Type = Counter32
_V2ccMkdirs_Object = MibScalar
v2ccMkdirs = _V2ccMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 15),
    _V2ccMkdirs_Type()
)
v2ccMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccMkdirs.setStatus("current")
_V2ccRmdirs_Type = Counter32
_V2ccRmdirs_Object = MibScalar
v2ccRmdirs = _V2ccRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 16),
    _V2ccRmdirs_Type()
)
v2ccRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccRmdirs.setStatus("current")
_V2ccReaddirs_Type = Counter32
_V2ccReaddirs_Object = MibScalar
v2ccReaddirs = _V2ccReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 17),
    _V2ccReaddirs_Type()
)
v2ccReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccReaddirs.setStatus("current")
_V2ccStatfss_Type = Counter32
_V2ccStatfss_Object = MibScalar
v2ccStatfss = _V2ccStatfss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 3, 18),
    _V2ccStatfss_Type()
)
v2ccStatfss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ccStatfss.setStatus("current")
_V2CachedPerCent_ObjectIdentity = ObjectIdentity
v2CachedPerCent = _V2CachedPerCent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4)
)


class _V2cpNulls_Type(Integer32):
    """Custom type v2cpNulls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpNulls_Type.__name__ = "Integer32"
_V2cpNulls_Object = MibScalar
v2cpNulls = _V2cpNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 1),
    _V2cpNulls_Type()
)
v2cpNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpNulls.setStatus("current")


class _V2cpGetattrs_Type(Integer32):
    """Custom type v2cpGetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpGetattrs_Type.__name__ = "Integer32"
_V2cpGetattrs_Object = MibScalar
v2cpGetattrs = _V2cpGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 2),
    _V2cpGetattrs_Type()
)
v2cpGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpGetattrs.setStatus("current")


class _V2cpSetattrs_Type(Integer32):
    """Custom type v2cpSetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpSetattrs_Type.__name__ = "Integer32"
_V2cpSetattrs_Object = MibScalar
v2cpSetattrs = _V2cpSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 3),
    _V2cpSetattrs_Type()
)
v2cpSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpSetattrs.setStatus("current")


class _V2cpRoots_Type(Integer32):
    """Custom type v2cpRoots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpRoots_Type.__name__ = "Integer32"
_V2cpRoots_Object = MibScalar
v2cpRoots = _V2cpRoots_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 4),
    _V2cpRoots_Type()
)
v2cpRoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpRoots.setStatus("current")


class _V2cpLookups_Type(Integer32):
    """Custom type v2cpLookups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpLookups_Type.__name__ = "Integer32"
_V2cpLookups_Object = MibScalar
v2cpLookups = _V2cpLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 5),
    _V2cpLookups_Type()
)
v2cpLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpLookups.setStatus("current")


class _V2cpReadlinks_Type(Integer32):
    """Custom type v2cpReadlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpReadlinks_Type.__name__ = "Integer32"
_V2cpReadlinks_Object = MibScalar
v2cpReadlinks = _V2cpReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 6),
    _V2cpReadlinks_Type()
)
v2cpReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpReadlinks.setStatus("current")


class _V2cpReads_Type(Integer32):
    """Custom type v2cpReads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpReads_Type.__name__ = "Integer32"
_V2cpReads_Object = MibScalar
v2cpReads = _V2cpReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 7),
    _V2cpReads_Type()
)
v2cpReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpReads.setStatus("current")


class _V2cpWrcaches_Type(Integer32):
    """Custom type v2cpWrcaches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpWrcaches_Type.__name__ = "Integer32"
_V2cpWrcaches_Object = MibScalar
v2cpWrcaches = _V2cpWrcaches_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 8),
    _V2cpWrcaches_Type()
)
v2cpWrcaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpWrcaches.setStatus("current")


class _V2cpWrites_Type(Integer32):
    """Custom type v2cpWrites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpWrites_Type.__name__ = "Integer32"
_V2cpWrites_Object = MibScalar
v2cpWrites = _V2cpWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 9),
    _V2cpWrites_Type()
)
v2cpWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpWrites.setStatus("current")


class _V2cpCreates_Type(Integer32):
    """Custom type v2cpCreates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpCreates_Type.__name__ = "Integer32"
_V2cpCreates_Object = MibScalar
v2cpCreates = _V2cpCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 10),
    _V2cpCreates_Type()
)
v2cpCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpCreates.setStatus("current")


class _V2cpRemoves_Type(Integer32):
    """Custom type v2cpRemoves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpRemoves_Type.__name__ = "Integer32"
_V2cpRemoves_Object = MibScalar
v2cpRemoves = _V2cpRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 11),
    _V2cpRemoves_Type()
)
v2cpRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpRemoves.setStatus("current")


class _V2cpRenames_Type(Integer32):
    """Custom type v2cpRenames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpRenames_Type.__name__ = "Integer32"
_V2cpRenames_Object = MibScalar
v2cpRenames = _V2cpRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 12),
    _V2cpRenames_Type()
)
v2cpRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpRenames.setStatus("current")


class _V2cpLinks_Type(Integer32):
    """Custom type v2cpLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpLinks_Type.__name__ = "Integer32"
_V2cpLinks_Object = MibScalar
v2cpLinks = _V2cpLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 13),
    _V2cpLinks_Type()
)
v2cpLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpLinks.setStatus("current")


class _V2cpSymlinks_Type(Integer32):
    """Custom type v2cpSymlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpSymlinks_Type.__name__ = "Integer32"
_V2cpSymlinks_Object = MibScalar
v2cpSymlinks = _V2cpSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 14),
    _V2cpSymlinks_Type()
)
v2cpSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpSymlinks.setStatus("current")


class _V2cpMkdirs_Type(Integer32):
    """Custom type v2cpMkdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpMkdirs_Type.__name__ = "Integer32"
_V2cpMkdirs_Object = MibScalar
v2cpMkdirs = _V2cpMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 15),
    _V2cpMkdirs_Type()
)
v2cpMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpMkdirs.setStatus("current")


class _V2cpRmdirs_Type(Integer32):
    """Custom type v2cpRmdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpRmdirs_Type.__name__ = "Integer32"
_V2cpRmdirs_Object = MibScalar
v2cpRmdirs = _V2cpRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 16),
    _V2cpRmdirs_Type()
)
v2cpRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpRmdirs.setStatus("current")


class _V2cpReaddirs_Type(Integer32):
    """Custom type v2cpReaddirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpReaddirs_Type.__name__ = "Integer32"
_V2cpReaddirs_Object = MibScalar
v2cpReaddirs = _V2cpReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 17),
    _V2cpReaddirs_Type()
)
v2cpReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpReaddirs.setStatus("current")


class _V2cpStatfss_Type(Integer32):
    """Custom type v2cpStatfss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V2cpStatfss_Type.__name__ = "Integer32"
_V2cpStatfss_Object = MibScalar
v2cpStatfss = _V2cpStatfss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 3, 4, 18),
    _V2cpStatfss_Type()
)
v2cpStatfss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2cpStatfss.setStatus("current")
_NfsV3_ObjectIdentity = ObjectIdentity
nfsV3 = _NfsV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4)
)
_V3Calls_ObjectIdentity = ObjectIdentity
v3Calls = _V3Calls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1)
)
_V3cNulls_Type = Counter32
_V3cNulls_Object = MibScalar
v3cNulls = _V3cNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 1),
    _V3cNulls_Type()
)
v3cNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cNulls.setStatus("current")
_V3cGetattrs_Type = Counter32
_V3cGetattrs_Object = MibScalar
v3cGetattrs = _V3cGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 2),
    _V3cGetattrs_Type()
)
v3cGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cGetattrs.setStatus("current")
_V3cSetattrs_Type = Counter32
_V3cSetattrs_Object = MibScalar
v3cSetattrs = _V3cSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 3),
    _V3cSetattrs_Type()
)
v3cSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cSetattrs.setStatus("current")
_V3cLookups_Type = Counter32
_V3cLookups_Object = MibScalar
v3cLookups = _V3cLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 4),
    _V3cLookups_Type()
)
v3cLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cLookups.setStatus("current")
_V3cAccesss_Type = Counter32
_V3cAccesss_Object = MibScalar
v3cAccesss = _V3cAccesss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 5),
    _V3cAccesss_Type()
)
v3cAccesss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cAccesss.setStatus("current")
_V3cReadlinks_Type = Counter32
_V3cReadlinks_Object = MibScalar
v3cReadlinks = _V3cReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 6),
    _V3cReadlinks_Type()
)
v3cReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cReadlinks.setStatus("current")
_V3cReads_Type = Counter32
_V3cReads_Object = MibScalar
v3cReads = _V3cReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 7),
    _V3cReads_Type()
)
v3cReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cReads.setStatus("current")
_V3cWrites_Type = Counter32
_V3cWrites_Object = MibScalar
v3cWrites = _V3cWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 8),
    _V3cWrites_Type()
)
v3cWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cWrites.setStatus("current")
_V3cCreates_Type = Counter32
_V3cCreates_Object = MibScalar
v3cCreates = _V3cCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 9),
    _V3cCreates_Type()
)
v3cCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cCreates.setStatus("current")
_V3cMkdirs_Type = Counter32
_V3cMkdirs_Object = MibScalar
v3cMkdirs = _V3cMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 10),
    _V3cMkdirs_Type()
)
v3cMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cMkdirs.setStatus("current")
_V3cSymlinks_Type = Counter32
_V3cSymlinks_Object = MibScalar
v3cSymlinks = _V3cSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 11),
    _V3cSymlinks_Type()
)
v3cSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cSymlinks.setStatus("current")
_V3cMknods_Type = Counter32
_V3cMknods_Object = MibScalar
v3cMknods = _V3cMknods_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 12),
    _V3cMknods_Type()
)
v3cMknods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cMknods.setStatus("current")
_V3cRemoves_Type = Counter32
_V3cRemoves_Object = MibScalar
v3cRemoves = _V3cRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 13),
    _V3cRemoves_Type()
)
v3cRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cRemoves.setStatus("current")
_V3cRmdirs_Type = Counter32
_V3cRmdirs_Object = MibScalar
v3cRmdirs = _V3cRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 14),
    _V3cRmdirs_Type()
)
v3cRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cRmdirs.setStatus("current")
_V3cRenames_Type = Counter32
_V3cRenames_Object = MibScalar
v3cRenames = _V3cRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 15),
    _V3cRenames_Type()
)
v3cRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cRenames.setStatus("current")
_V3cLinks_Type = Counter32
_V3cLinks_Object = MibScalar
v3cLinks = _V3cLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 16),
    _V3cLinks_Type()
)
v3cLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cLinks.setStatus("current")
_V3cReaddirs_Type = Counter32
_V3cReaddirs_Object = MibScalar
v3cReaddirs = _V3cReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 17),
    _V3cReaddirs_Type()
)
v3cReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cReaddirs.setStatus("current")
_V3cReaddirPluss_Type = Counter32
_V3cReaddirPluss_Object = MibScalar
v3cReaddirPluss = _V3cReaddirPluss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 18),
    _V3cReaddirPluss_Type()
)
v3cReaddirPluss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cReaddirPluss.setStatus("current")
_V3cFsstats_Type = Counter32
_V3cFsstats_Object = MibScalar
v3cFsstats = _V3cFsstats_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 19),
    _V3cFsstats_Type()
)
v3cFsstats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cFsstats.setStatus("current")
_V3cFsinfos_Type = Counter32
_V3cFsinfos_Object = MibScalar
v3cFsinfos = _V3cFsinfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 20),
    _V3cFsinfos_Type()
)
v3cFsinfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cFsinfos.setStatus("current")
_V3cPathconfs_Type = Counter32
_V3cPathconfs_Object = MibScalar
v3cPathconfs = _V3cPathconfs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 21),
    _V3cPathconfs_Type()
)
v3cPathconfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cPathconfs.setStatus("current")
_V3cCommits_Type = Counter32
_V3cCommits_Object = MibScalar
v3cCommits = _V3cCommits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 1, 22),
    _V3cCommits_Type()
)
v3cCommits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cCommits.setStatus("current")
_V3Percent_ObjectIdentity = ObjectIdentity
v3Percent = _V3Percent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2)
)


class _V3pNulls_Type(Integer32):
    """Custom type v3pNulls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pNulls_Type.__name__ = "Integer32"
_V3pNulls_Object = MibScalar
v3pNulls = _V3pNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 1),
    _V3pNulls_Type()
)
v3pNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pNulls.setStatus("current")


class _V3pGetattrs_Type(Integer32):
    """Custom type v3pGetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pGetattrs_Type.__name__ = "Integer32"
_V3pGetattrs_Object = MibScalar
v3pGetattrs = _V3pGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 2),
    _V3pGetattrs_Type()
)
v3pGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pGetattrs.setStatus("current")


class _V3pSetattrs_Type(Integer32):
    """Custom type v3pSetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pSetattrs_Type.__name__ = "Integer32"
_V3pSetattrs_Object = MibScalar
v3pSetattrs = _V3pSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 3),
    _V3pSetattrs_Type()
)
v3pSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pSetattrs.setStatus("current")


class _V3pLookups_Type(Integer32):
    """Custom type v3pLookups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pLookups_Type.__name__ = "Integer32"
_V3pLookups_Object = MibScalar
v3pLookups = _V3pLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 4),
    _V3pLookups_Type()
)
v3pLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pLookups.setStatus("current")


class _V3pAccesss_Type(Integer32):
    """Custom type v3pAccesss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pAccesss_Type.__name__ = "Integer32"
_V3pAccesss_Object = MibScalar
v3pAccesss = _V3pAccesss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 5),
    _V3pAccesss_Type()
)
v3pAccesss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pAccesss.setStatus("current")


class _V3pReadlinks_Type(Integer32):
    """Custom type v3pReadlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pReadlinks_Type.__name__ = "Integer32"
_V3pReadlinks_Object = MibScalar
v3pReadlinks = _V3pReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 6),
    _V3pReadlinks_Type()
)
v3pReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pReadlinks.setStatus("current")


class _V3pReads_Type(Integer32):
    """Custom type v3pReads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pReads_Type.__name__ = "Integer32"
_V3pReads_Object = MibScalar
v3pReads = _V3pReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 7),
    _V3pReads_Type()
)
v3pReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pReads.setStatus("current")


class _V3pWrites_Type(Integer32):
    """Custom type v3pWrites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pWrites_Type.__name__ = "Integer32"
_V3pWrites_Object = MibScalar
v3pWrites = _V3pWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 8),
    _V3pWrites_Type()
)
v3pWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pWrites.setStatus("current")


class _V3pCreates_Type(Integer32):
    """Custom type v3pCreates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pCreates_Type.__name__ = "Integer32"
_V3pCreates_Object = MibScalar
v3pCreates = _V3pCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 9),
    _V3pCreates_Type()
)
v3pCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pCreates.setStatus("current")


class _V3pMkdirs_Type(Integer32):
    """Custom type v3pMkdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pMkdirs_Type.__name__ = "Integer32"
_V3pMkdirs_Object = MibScalar
v3pMkdirs = _V3pMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 10),
    _V3pMkdirs_Type()
)
v3pMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pMkdirs.setStatus("current")


class _V3pSymlinks_Type(Integer32):
    """Custom type v3pSymlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pSymlinks_Type.__name__ = "Integer32"
_V3pSymlinks_Object = MibScalar
v3pSymlinks = _V3pSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 11),
    _V3pSymlinks_Type()
)
v3pSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pSymlinks.setStatus("current")


class _V3pMknods_Type(Integer32):
    """Custom type v3pMknods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pMknods_Type.__name__ = "Integer32"
_V3pMknods_Object = MibScalar
v3pMknods = _V3pMknods_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 12),
    _V3pMknods_Type()
)
v3pMknods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pMknods.setStatus("current")


class _V3pRemoves_Type(Integer32):
    """Custom type v3pRemoves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pRemoves_Type.__name__ = "Integer32"
_V3pRemoves_Object = MibScalar
v3pRemoves = _V3pRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 13),
    _V3pRemoves_Type()
)
v3pRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pRemoves.setStatus("current")


class _V3pRmdirs_Type(Integer32):
    """Custom type v3pRmdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pRmdirs_Type.__name__ = "Integer32"
_V3pRmdirs_Object = MibScalar
v3pRmdirs = _V3pRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 14),
    _V3pRmdirs_Type()
)
v3pRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pRmdirs.setStatus("current")


class _V3pRenames_Type(Integer32):
    """Custom type v3pRenames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pRenames_Type.__name__ = "Integer32"
_V3pRenames_Object = MibScalar
v3pRenames = _V3pRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 15),
    _V3pRenames_Type()
)
v3pRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pRenames.setStatus("current")


class _V3pLinks_Type(Integer32):
    """Custom type v3pLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pLinks_Type.__name__ = "Integer32"
_V3pLinks_Object = MibScalar
v3pLinks = _V3pLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 16),
    _V3pLinks_Type()
)
v3pLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pLinks.setStatus("current")


class _V3pReaddirs_Type(Integer32):
    """Custom type v3pReaddirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pReaddirs_Type.__name__ = "Integer32"
_V3pReaddirs_Object = MibScalar
v3pReaddirs = _V3pReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 17),
    _V3pReaddirs_Type()
)
v3pReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pReaddirs.setStatus("current")


class _V3pReaddirPluss_Type(Integer32):
    """Custom type v3pReaddirPluss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pReaddirPluss_Type.__name__ = "Integer32"
_V3pReaddirPluss_Object = MibScalar
v3pReaddirPluss = _V3pReaddirPluss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 18),
    _V3pReaddirPluss_Type()
)
v3pReaddirPluss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pReaddirPluss.setStatus("current")


class _V3pFsstats_Type(Integer32):
    """Custom type v3pFsstats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pFsstats_Type.__name__ = "Integer32"
_V3pFsstats_Object = MibScalar
v3pFsstats = _V3pFsstats_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 19),
    _V3pFsstats_Type()
)
v3pFsstats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pFsstats.setStatus("current")


class _V3pFsinfos_Type(Integer32):
    """Custom type v3pFsinfos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pFsinfos_Type.__name__ = "Integer32"
_V3pFsinfos_Object = MibScalar
v3pFsinfos = _V3pFsinfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 20),
    _V3pFsinfos_Type()
)
v3pFsinfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pFsinfos.setStatus("current")


class _V3pPathconfs_Type(Integer32):
    """Custom type v3pPathconfs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pPathconfs_Type.__name__ = "Integer32"
_V3pPathconfs_Object = MibScalar
v3pPathconfs = _V3pPathconfs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 21),
    _V3pPathconfs_Type()
)
v3pPathconfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pPathconfs.setStatus("current")


class _V3pCommits_Type(Integer32):
    """Custom type v3pCommits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3pCommits_Type.__name__ = "Integer32"
_V3pCommits_Object = MibScalar
v3pCommits = _V3pCommits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 2, 22),
    _V3pCommits_Type()
)
v3pCommits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3pCommits.setStatus("current")
_V3CachedCalls_ObjectIdentity = ObjectIdentity
v3CachedCalls = _V3CachedCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3)
)
_V3ccNulls_Type = Counter32
_V3ccNulls_Object = MibScalar
v3ccNulls = _V3ccNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 1),
    _V3ccNulls_Type()
)
v3ccNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccNulls.setStatus("current")
_V3ccGetattrs_Type = Counter32
_V3ccGetattrs_Object = MibScalar
v3ccGetattrs = _V3ccGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 2),
    _V3ccGetattrs_Type()
)
v3ccGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccGetattrs.setStatus("current")
_V3ccSetattrs_Type = Counter32
_V3ccSetattrs_Object = MibScalar
v3ccSetattrs = _V3ccSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 3),
    _V3ccSetattrs_Type()
)
v3ccSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccSetattrs.setStatus("current")
_V3ccLookups_Type = Counter32
_V3ccLookups_Object = MibScalar
v3ccLookups = _V3ccLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 4),
    _V3ccLookups_Type()
)
v3ccLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccLookups.setStatus("current")
_V3ccAccesss_Type = Counter32
_V3ccAccesss_Object = MibScalar
v3ccAccesss = _V3ccAccesss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 5),
    _V3ccAccesss_Type()
)
v3ccAccesss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccAccesss.setStatus("current")
_V3ccReadlinks_Type = Counter32
_V3ccReadlinks_Object = MibScalar
v3ccReadlinks = _V3ccReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 6),
    _V3ccReadlinks_Type()
)
v3ccReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccReadlinks.setStatus("current")
_V3ccReads_Type = Counter32
_V3ccReads_Object = MibScalar
v3ccReads = _V3ccReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 7),
    _V3ccReads_Type()
)
v3ccReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccReads.setStatus("current")
_V3ccWrites_Type = Counter32
_V3ccWrites_Object = MibScalar
v3ccWrites = _V3ccWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 8),
    _V3ccWrites_Type()
)
v3ccWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccWrites.setStatus("current")
_V3ccCreates_Type = Counter32
_V3ccCreates_Object = MibScalar
v3ccCreates = _V3ccCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 9),
    _V3ccCreates_Type()
)
v3ccCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccCreates.setStatus("current")
_V3ccMkdirs_Type = Counter32
_V3ccMkdirs_Object = MibScalar
v3ccMkdirs = _V3ccMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 10),
    _V3ccMkdirs_Type()
)
v3ccMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccMkdirs.setStatus("current")
_V3ccSymlinks_Type = Counter32
_V3ccSymlinks_Object = MibScalar
v3ccSymlinks = _V3ccSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 11),
    _V3ccSymlinks_Type()
)
v3ccSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccSymlinks.setStatus("current")
_V3ccMknods_Type = Counter32
_V3ccMknods_Object = MibScalar
v3ccMknods = _V3ccMknods_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 12),
    _V3ccMknods_Type()
)
v3ccMknods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccMknods.setStatus("current")
_V3ccRemoves_Type = Counter32
_V3ccRemoves_Object = MibScalar
v3ccRemoves = _V3ccRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 13),
    _V3ccRemoves_Type()
)
v3ccRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccRemoves.setStatus("current")
_V3ccRmdirs_Type = Counter32
_V3ccRmdirs_Object = MibScalar
v3ccRmdirs = _V3ccRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 14),
    _V3ccRmdirs_Type()
)
v3ccRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccRmdirs.setStatus("current")
_V3ccRenames_Type = Counter32
_V3ccRenames_Object = MibScalar
v3ccRenames = _V3ccRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 15),
    _V3ccRenames_Type()
)
v3ccRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccRenames.setStatus("current")
_V3ccLinks_Type = Counter32
_V3ccLinks_Object = MibScalar
v3ccLinks = _V3ccLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 16),
    _V3ccLinks_Type()
)
v3ccLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccLinks.setStatus("current")
_V3ccReaddirs_Type = Counter32
_V3ccReaddirs_Object = MibScalar
v3ccReaddirs = _V3ccReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 17),
    _V3ccReaddirs_Type()
)
v3ccReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccReaddirs.setStatus("current")
_V3ccReaddirPluss_Type = Counter32
_V3ccReaddirPluss_Object = MibScalar
v3ccReaddirPluss = _V3ccReaddirPluss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 18),
    _V3ccReaddirPluss_Type()
)
v3ccReaddirPluss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccReaddirPluss.setStatus("current")
_V3ccFsstats_Type = Counter32
_V3ccFsstats_Object = MibScalar
v3ccFsstats = _V3ccFsstats_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 19),
    _V3ccFsstats_Type()
)
v3ccFsstats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccFsstats.setStatus("current")
_V3ccFsinfos_Type = Counter32
_V3ccFsinfos_Object = MibScalar
v3ccFsinfos = _V3ccFsinfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 20),
    _V3ccFsinfos_Type()
)
v3ccFsinfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccFsinfos.setStatus("current")
_V3ccPathconfs_Type = Counter32
_V3ccPathconfs_Object = MibScalar
v3ccPathconfs = _V3ccPathconfs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 21),
    _V3ccPathconfs_Type()
)
v3ccPathconfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccPathconfs.setStatus("current")
_V3ccCommits_Type = Counter32
_V3ccCommits_Object = MibScalar
v3ccCommits = _V3ccCommits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 3, 22),
    _V3ccCommits_Type()
)
v3ccCommits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ccCommits.setStatus("current")
_V3CachedPerCent_ObjectIdentity = ObjectIdentity
v3CachedPerCent = _V3CachedPerCent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4)
)


class _V3cpNulls_Type(Integer32):
    """Custom type v3cpNulls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpNulls_Type.__name__ = "Integer32"
_V3cpNulls_Object = MibScalar
v3cpNulls = _V3cpNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 1),
    _V3cpNulls_Type()
)
v3cpNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpNulls.setStatus("current")


class _V3cpGetattrs_Type(Integer32):
    """Custom type v3cpGetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpGetattrs_Type.__name__ = "Integer32"
_V3cpGetattrs_Object = MibScalar
v3cpGetattrs = _V3cpGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 2),
    _V3cpGetattrs_Type()
)
v3cpGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpGetattrs.setStatus("current")


class _V3cpSetattrs_Type(Integer32):
    """Custom type v3cpSetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpSetattrs_Type.__name__ = "Integer32"
_V3cpSetattrs_Object = MibScalar
v3cpSetattrs = _V3cpSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 3),
    _V3cpSetattrs_Type()
)
v3cpSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpSetattrs.setStatus("current")


class _V3cpLookups_Type(Integer32):
    """Custom type v3cpLookups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpLookups_Type.__name__ = "Integer32"
_V3cpLookups_Object = MibScalar
v3cpLookups = _V3cpLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 4),
    _V3cpLookups_Type()
)
v3cpLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpLookups.setStatus("current")


class _V3cpAccesss_Type(Integer32):
    """Custom type v3cpAccesss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpAccesss_Type.__name__ = "Integer32"
_V3cpAccesss_Object = MibScalar
v3cpAccesss = _V3cpAccesss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 5),
    _V3cpAccesss_Type()
)
v3cpAccesss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpAccesss.setStatus("current")


class _V3cpReadlinks_Type(Integer32):
    """Custom type v3cpReadlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpReadlinks_Type.__name__ = "Integer32"
_V3cpReadlinks_Object = MibScalar
v3cpReadlinks = _V3cpReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 6),
    _V3cpReadlinks_Type()
)
v3cpReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpReadlinks.setStatus("current")


class _V3cpReads_Type(Integer32):
    """Custom type v3cpReads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpReads_Type.__name__ = "Integer32"
_V3cpReads_Object = MibScalar
v3cpReads = _V3cpReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 7),
    _V3cpReads_Type()
)
v3cpReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpReads.setStatus("current")


class _V3cpWrites_Type(Integer32):
    """Custom type v3cpWrites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpWrites_Type.__name__ = "Integer32"
_V3cpWrites_Object = MibScalar
v3cpWrites = _V3cpWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 8),
    _V3cpWrites_Type()
)
v3cpWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpWrites.setStatus("current")


class _V3cpCreates_Type(Integer32):
    """Custom type v3cpCreates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpCreates_Type.__name__ = "Integer32"
_V3cpCreates_Object = MibScalar
v3cpCreates = _V3cpCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 9),
    _V3cpCreates_Type()
)
v3cpCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpCreates.setStatus("current")


class _V3cpMkdirs_Type(Integer32):
    """Custom type v3cpMkdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpMkdirs_Type.__name__ = "Integer32"
_V3cpMkdirs_Object = MibScalar
v3cpMkdirs = _V3cpMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 10),
    _V3cpMkdirs_Type()
)
v3cpMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpMkdirs.setStatus("current")


class _V3cpSymlinks_Type(Integer32):
    """Custom type v3cpSymlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpSymlinks_Type.__name__ = "Integer32"
_V3cpSymlinks_Object = MibScalar
v3cpSymlinks = _V3cpSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 11),
    _V3cpSymlinks_Type()
)
v3cpSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpSymlinks.setStatus("current")


class _V3cpMknods_Type(Integer32):
    """Custom type v3cpMknods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpMknods_Type.__name__ = "Integer32"
_V3cpMknods_Object = MibScalar
v3cpMknods = _V3cpMknods_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 12),
    _V3cpMknods_Type()
)
v3cpMknods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpMknods.setStatus("current")


class _V3cpRemoves_Type(Integer32):
    """Custom type v3cpRemoves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpRemoves_Type.__name__ = "Integer32"
_V3cpRemoves_Object = MibScalar
v3cpRemoves = _V3cpRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 13),
    _V3cpRemoves_Type()
)
v3cpRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpRemoves.setStatus("current")


class _V3cpRmdirs_Type(Integer32):
    """Custom type v3cpRmdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpRmdirs_Type.__name__ = "Integer32"
_V3cpRmdirs_Object = MibScalar
v3cpRmdirs = _V3cpRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 14),
    _V3cpRmdirs_Type()
)
v3cpRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpRmdirs.setStatus("current")


class _V3cpRenames_Type(Integer32):
    """Custom type v3cpRenames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpRenames_Type.__name__ = "Integer32"
_V3cpRenames_Object = MibScalar
v3cpRenames = _V3cpRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 15),
    _V3cpRenames_Type()
)
v3cpRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpRenames.setStatus("current")


class _V3cpLinks_Type(Integer32):
    """Custom type v3cpLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpLinks_Type.__name__ = "Integer32"
_V3cpLinks_Object = MibScalar
v3cpLinks = _V3cpLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 16),
    _V3cpLinks_Type()
)
v3cpLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpLinks.setStatus("current")


class _V3cpReaddirs_Type(Integer32):
    """Custom type v3cpReaddirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpReaddirs_Type.__name__ = "Integer32"
_V3cpReaddirs_Object = MibScalar
v3cpReaddirs = _V3cpReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 17),
    _V3cpReaddirs_Type()
)
v3cpReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpReaddirs.setStatus("current")


class _V3cpReaddirPluss_Type(Integer32):
    """Custom type v3cpReaddirPluss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpReaddirPluss_Type.__name__ = "Integer32"
_V3cpReaddirPluss_Object = MibScalar
v3cpReaddirPluss = _V3cpReaddirPluss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 18),
    _V3cpReaddirPluss_Type()
)
v3cpReaddirPluss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpReaddirPluss.setStatus("current")


class _V3cpFsstats_Type(Integer32):
    """Custom type v3cpFsstats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpFsstats_Type.__name__ = "Integer32"
_V3cpFsstats_Object = MibScalar
v3cpFsstats = _V3cpFsstats_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 19),
    _V3cpFsstats_Type()
)
v3cpFsstats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpFsstats.setStatus("current")


class _V3cpFsinfos_Type(Integer32):
    """Custom type v3cpFsinfos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpFsinfos_Type.__name__ = "Integer32"
_V3cpFsinfos_Object = MibScalar
v3cpFsinfos = _V3cpFsinfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 20),
    _V3cpFsinfos_Type()
)
v3cpFsinfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpFsinfos.setStatus("current")


class _V3cpPathconfs_Type(Integer32):
    """Custom type v3cpPathconfs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpPathconfs_Type.__name__ = "Integer32"
_V3cpPathconfs_Object = MibScalar
v3cpPathconfs = _V3cpPathconfs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 21),
    _V3cpPathconfs_Type()
)
v3cpPathconfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpPathconfs.setStatus("current")


class _V3cpCommits_Type(Integer32):
    """Custom type v3cpCommits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_V3cpCommits_Type.__name__ = "Integer32"
_V3cpCommits_Object = MibScalar
v3cpCommits = _V3cpCommits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 4, 4, 22),
    _V3cpCommits_Type()
)
v3cpCommits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3cpCommits.setStatus("current")
_ReplyCache_ObjectIdentity = ObjectIdentity
replyCache = _ReplyCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5)
)
_RcInProgressHits_Type = Counter32
_RcInProgressHits_Object = MibScalar
rcInProgressHits = _RcInProgressHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 1),
    _RcInProgressHits_Type()
)
rcInProgressHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcInProgressHits.setStatus("current")
_RcDelayHits_Type = Counter32
_RcDelayHits_Object = MibScalar
rcDelayHits = _RcDelayHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 2),
    _RcDelayHits_Type()
)
rcDelayHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDelayHits.setStatus("deprecated")
_RcMisses_Type = Counter32
_RcMisses_Object = MibScalar
rcMisses = _RcMisses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 3),
    _RcMisses_Type()
)
rcMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMisses.setStatus("current")
_RcNonIdemDoneHits_Type = Counter32
_RcNonIdemDoneHits_Object = MibScalar
rcNonIdemDoneHits = _RcNonIdemDoneHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 4),
    _RcNonIdemDoneHits_Type()
)
rcNonIdemDoneHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNonIdemDoneHits.setStatus("current")
_RcNonIdemNotDoneHits_Type = Counter32
_RcNonIdemNotDoneHits_Object = MibScalar
rcNonIdemNotDoneHits = _RcNonIdemNotDoneHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 5),
    _RcNonIdemNotDoneHits_Type()
)
rcNonIdemNotDoneHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcNonIdemNotDoneHits.setStatus("current")
_RcTcpInProgressHits_Type = Counter32
_RcTcpInProgressHits_Object = MibScalar
rcTcpInProgressHits = _RcTcpInProgressHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 6),
    _RcTcpInProgressHits_Type()
)
rcTcpInProgressHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcTcpInProgressHits.setStatus("current")
_RcTcpDelayHits_Type = Counter32
_RcTcpDelayHits_Object = MibScalar
rcTcpDelayHits = _RcTcpDelayHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 7),
    _RcTcpDelayHits_Type()
)
rcTcpDelayHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcTcpDelayHits.setStatus("deprecated")
_RcTcpMisses_Type = Counter32
_RcTcpMisses_Object = MibScalar
rcTcpMisses = _RcTcpMisses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 8),
    _RcTcpMisses_Type()
)
rcTcpMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcTcpMisses.setStatus("current")
_RcTcpNonIdemDoneHits_Type = Counter32
_RcTcpNonIdemDoneHits_Object = MibScalar
rcTcpNonIdemDoneHits = _RcTcpNonIdemDoneHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 9),
    _RcTcpNonIdemDoneHits_Type()
)
rcTcpNonIdemDoneHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcTcpNonIdemDoneHits.setStatus("current")
_RcTcpNonIdemNotDoneHits_Type = Counter32
_RcTcpNonIdemNotDoneHits_Object = MibScalar
rcTcpNonIdemNotDoneHits = _RcTcpNonIdemNotDoneHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 10),
    _RcTcpNonIdemNotDoneHits_Type()
)
rcTcpNonIdemNotDoneHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcTcpNonIdemNotDoneHits.setStatus("current")
_RcUdpInProgressHits_Type = Counter32
_RcUdpInProgressHits_Object = MibScalar
rcUdpInProgressHits = _RcUdpInProgressHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 11),
    _RcUdpInProgressHits_Type()
)
rcUdpInProgressHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcUdpInProgressHits.setStatus("current")
_RcUdpDelayHits_Type = Counter32
_RcUdpDelayHits_Object = MibScalar
rcUdpDelayHits = _RcUdpDelayHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 12),
    _RcUdpDelayHits_Type()
)
rcUdpDelayHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcUdpDelayHits.setStatus("deprecated")
_RcUdpMisses_Type = Counter32
_RcUdpMisses_Object = MibScalar
rcUdpMisses = _RcUdpMisses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 13),
    _RcUdpMisses_Type()
)
rcUdpMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcUdpMisses.setStatus("current")
_RcUdpNonIdemDoneHits_Type = Counter32
_RcUdpNonIdemDoneHits_Object = MibScalar
rcUdpNonIdemDoneHits = _RcUdpNonIdemDoneHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 14),
    _RcUdpNonIdemDoneHits_Type()
)
rcUdpNonIdemDoneHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcUdpNonIdemDoneHits.setStatus("current")
_RcUdpNonIdemNotDoneHits_Type = Counter32
_RcUdpNonIdemNotDoneHits_Object = MibScalar
rcUdpNonIdemNotDoneHits = _RcUdpNonIdemNotDoneHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 5, 15),
    _RcUdpNonIdemNotDoneHits_Type()
)
rcUdpNonIdemNotDoneHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcUdpNonIdemNotDoneHits.setStatus("current")
_NfsrwStats_ObjectIdentity = ObjectIdentity
nfsrwStats = _NfsrwStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6)
)
_V2ReadStats_ObjectIdentity = ObjectIdentity
v2ReadStats = _V2ReadStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 1)
)
_V2Read512Calls_Type = Counter32
_V2Read512Calls_Object = MibScalar
v2Read512Calls = _V2Read512Calls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 1, 1),
    _V2Read512Calls_Type()
)
v2Read512Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Read512Calls.setStatus("current")
_V2Read1KCalls_Type = Counter32
_V2Read1KCalls_Object = MibScalar
v2Read1KCalls = _V2Read1KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 1, 2),
    _V2Read1KCalls_Type()
)
v2Read1KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Read1KCalls.setStatus("current")
_V2Read2KCalls_Type = Counter32
_V2Read2KCalls_Object = MibScalar
v2Read2KCalls = _V2Read2KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 1, 3),
    _V2Read2KCalls_Type()
)
v2Read2KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Read2KCalls.setStatus("current")
_V2Read4KCalls_Type = Counter32
_V2Read4KCalls_Object = MibScalar
v2Read4KCalls = _V2Read4KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 1, 4),
    _V2Read4KCalls_Type()
)
v2Read4KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Read4KCalls.setStatus("current")
_V2Read8KCalls_Type = Counter32
_V2Read8KCalls_Object = MibScalar
v2Read8KCalls = _V2Read8KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 1, 5),
    _V2Read8KCalls_Type()
)
v2Read8KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Read8KCalls.setStatus("current")
_V2Read16KCalls_Type = Counter32
_V2Read16KCalls_Object = MibScalar
v2Read16KCalls = _V2Read16KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 1, 6),
    _V2Read16KCalls_Type()
)
v2Read16KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Read16KCalls.setStatus("current")
_V2Read32KCalls_Type = Counter32
_V2Read32KCalls_Object = MibScalar
v2Read32KCalls = _V2Read32KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 1, 7),
    _V2Read32KCalls_Type()
)
v2Read32KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Read32KCalls.setStatus("current")
_V2Read64KCalls_Type = Counter32
_V2Read64KCalls_Object = MibScalar
v2Read64KCalls = _V2Read64KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 1, 8),
    _V2Read64KCalls_Type()
)
v2Read64KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Read64KCalls.setStatus("current")
_V2Read128KCalls_Type = Counter32
_V2Read128KCalls_Object = MibScalar
v2Read128KCalls = _V2Read128KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 1, 9),
    _V2Read128KCalls_Type()
)
v2Read128KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Read128KCalls.setStatus("current")
_V2WriteStats_ObjectIdentity = ObjectIdentity
v2WriteStats = _V2WriteStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 2)
)
_V2Write512Calls_Type = Counter32
_V2Write512Calls_Object = MibScalar
v2Write512Calls = _V2Write512Calls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 2, 1),
    _V2Write512Calls_Type()
)
v2Write512Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Write512Calls.setStatus("current")
_V2Write1KCalls_Type = Counter32
_V2Write1KCalls_Object = MibScalar
v2Write1KCalls = _V2Write1KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 2, 2),
    _V2Write1KCalls_Type()
)
v2Write1KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Write1KCalls.setStatus("current")
_V2Write2KCalls_Type = Counter32
_V2Write2KCalls_Object = MibScalar
v2Write2KCalls = _V2Write2KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 2, 3),
    _V2Write2KCalls_Type()
)
v2Write2KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Write2KCalls.setStatus("current")
_V2Write4KCalls_Type = Counter32
_V2Write4KCalls_Object = MibScalar
v2Write4KCalls = _V2Write4KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 2, 4),
    _V2Write4KCalls_Type()
)
v2Write4KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Write4KCalls.setStatus("current")
_V2Write8KCalls_Type = Counter32
_V2Write8KCalls_Object = MibScalar
v2Write8KCalls = _V2Write8KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 2, 5),
    _V2Write8KCalls_Type()
)
v2Write8KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Write8KCalls.setStatus("current")
_V2Write16KCalls_Type = Counter32
_V2Write16KCalls_Object = MibScalar
v2Write16KCalls = _V2Write16KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 2, 6),
    _V2Write16KCalls_Type()
)
v2Write16KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Write16KCalls.setStatus("current")
_V2Write32KCalls_Type = Counter32
_V2Write32KCalls_Object = MibScalar
v2Write32KCalls = _V2Write32KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 2, 7),
    _V2Write32KCalls_Type()
)
v2Write32KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Write32KCalls.setStatus("current")
_V2Write64KCalls_Type = Counter32
_V2Write64KCalls_Object = MibScalar
v2Write64KCalls = _V2Write64KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 2, 8),
    _V2Write64KCalls_Type()
)
v2Write64KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Write64KCalls.setStatus("current")
_V2Write128KCalls_Type = Counter32
_V2Write128KCalls_Object = MibScalar
v2Write128KCalls = _V2Write128KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 2, 9),
    _V2Write128KCalls_Type()
)
v2Write128KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2Write128KCalls.setStatus("current")
_V3ReadStats_ObjectIdentity = ObjectIdentity
v3ReadStats = _V3ReadStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 3)
)
_V3Read512Calls_Type = Counter32
_V3Read512Calls_Object = MibScalar
v3Read512Calls = _V3Read512Calls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 3, 1),
    _V3Read512Calls_Type()
)
v3Read512Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Read512Calls.setStatus("current")
_V3Read1KCalls_Type = Counter32
_V3Read1KCalls_Object = MibScalar
v3Read1KCalls = _V3Read1KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 3, 2),
    _V3Read1KCalls_Type()
)
v3Read1KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Read1KCalls.setStatus("current")
_V3Read2KCalls_Type = Counter32
_V3Read2KCalls_Object = MibScalar
v3Read2KCalls = _V3Read2KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 3, 3),
    _V3Read2KCalls_Type()
)
v3Read2KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Read2KCalls.setStatus("current")
_V3Read4KCalls_Type = Counter32
_V3Read4KCalls_Object = MibScalar
v3Read4KCalls = _V3Read4KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 3, 4),
    _V3Read4KCalls_Type()
)
v3Read4KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Read4KCalls.setStatus("current")
_V3Read8KCalls_Type = Counter32
_V3Read8KCalls_Object = MibScalar
v3Read8KCalls = _V3Read8KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 3, 5),
    _V3Read8KCalls_Type()
)
v3Read8KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Read8KCalls.setStatus("current")
_V3Read16KCalls_Type = Counter32
_V3Read16KCalls_Object = MibScalar
v3Read16KCalls = _V3Read16KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 3, 6),
    _V3Read16KCalls_Type()
)
v3Read16KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Read16KCalls.setStatus("current")
_V3Read32KCalls_Type = Counter32
_V3Read32KCalls_Object = MibScalar
v3Read32KCalls = _V3Read32KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 3, 7),
    _V3Read32KCalls_Type()
)
v3Read32KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Read32KCalls.setStatus("current")
_V3Read64KCalls_Type = Counter32
_V3Read64KCalls_Object = MibScalar
v3Read64KCalls = _V3Read64KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 3, 8),
    _V3Read64KCalls_Type()
)
v3Read64KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Read64KCalls.setStatus("current")
_V3Read128KCalls_Type = Counter32
_V3Read128KCalls_Object = MibScalar
v3Read128KCalls = _V3Read128KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 3, 9),
    _V3Read128KCalls_Type()
)
v3Read128KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Read128KCalls.setStatus("current")
_V3WriteStats_ObjectIdentity = ObjectIdentity
v3WriteStats = _V3WriteStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 4)
)
_V3Write512Calls_Type = Counter32
_V3Write512Calls_Object = MibScalar
v3Write512Calls = _V3Write512Calls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 4, 1),
    _V3Write512Calls_Type()
)
v3Write512Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Write512Calls.setStatus("current")
_V3Write1KCalls_Type = Counter32
_V3Write1KCalls_Object = MibScalar
v3Write1KCalls = _V3Write1KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 4, 2),
    _V3Write1KCalls_Type()
)
v3Write1KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Write1KCalls.setStatus("current")
_V3Write2KCalls_Type = Counter32
_V3Write2KCalls_Object = MibScalar
v3Write2KCalls = _V3Write2KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 4, 3),
    _V3Write2KCalls_Type()
)
v3Write2KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Write2KCalls.setStatus("current")
_V3Write4KCalls_Type = Counter32
_V3Write4KCalls_Object = MibScalar
v3Write4KCalls = _V3Write4KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 4, 4),
    _V3Write4KCalls_Type()
)
v3Write4KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Write4KCalls.setStatus("current")
_V3Write8KCalls_Type = Counter32
_V3Write8KCalls_Object = MibScalar
v3Write8KCalls = _V3Write8KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 4, 5),
    _V3Write8KCalls_Type()
)
v3Write8KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Write8KCalls.setStatus("current")
_V3Write16KCalls_Type = Counter32
_V3Write16KCalls_Object = MibScalar
v3Write16KCalls = _V3Write16KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 4, 6),
    _V3Write16KCalls_Type()
)
v3Write16KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Write16KCalls.setStatus("current")
_V3Write32KCalls_Type = Counter32
_V3Write32KCalls_Object = MibScalar
v3Write32KCalls = _V3Write32KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 4, 7),
    _V3Write32KCalls_Type()
)
v3Write32KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Write32KCalls.setStatus("current")
_V3Write64KCalls_Type = Counter32
_V3Write64KCalls_Object = MibScalar
v3Write64KCalls = _V3Write64KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 4, 8),
    _V3Write64KCalls_Type()
)
v3Write64KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Write64KCalls.setStatus("current")
_V3Write128KCalls_Type = Counter32
_V3Write128KCalls_Object = MibScalar
v3Write128KCalls = _V3Write128KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 2, 6, 4, 9),
    _V3Write128KCalls_Type()
)
v3Write128KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3Write128KCalls.setStatus("current")
_NfsPerClient_ObjectIdentity = ObjectIdentity
nfsPerClient = _NfsPerClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3)
)
_PclTable_Object = MibTable
pclTable = _PclTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pclTable.setStatus("current")
_PclEntry_Object = MibTableRow
pclEntry = _PclEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1)
)
pclEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "pclIpAddr"),
)
if mibBuilder.loadTexts:
    pclEntry.setStatus("current")
_PclIpAddr_Type = IpAddress
_PclIpAddr_Object = MibTableColumn
pclIpAddr = _PclIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 1),
    _PclIpAddr_Type()
)
pclIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclIpAddr.setStatus("current")
_PclRpcCalls_Type = Counter32
_PclRpcCalls_Object = MibTableColumn
pclRpcCalls = _PclRpcCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 2),
    _PclRpcCalls_Type()
)
pclRpcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclRpcCalls.setStatus("current")
_PclRpcBadCalls_Type = Counter32
_PclRpcBadCalls_Object = MibTableColumn
pclRpcBadCalls = _PclRpcBadCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 3),
    _PclRpcBadCalls_Type()
)
pclRpcBadCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclRpcBadCalls.setStatus("current")
_PclRpcNullRecvs_Type = Counter32
_PclRpcNullRecvs_Object = MibTableColumn
pclRpcNullRecvs = _PclRpcNullRecvs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 4),
    _PclRpcNullRecvs_Type()
)
pclRpcNullRecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclRpcNullRecvs.setStatus("current")
_PclRpcBadLens_Type = Counter32
_PclRpcBadLens_Object = MibTableColumn
pclRpcBadLens = _PclRpcBadLens_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 5),
    _PclRpcBadLens_Type()
)
pclRpcBadLens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclRpcBadLens.setStatus("current")
_PclRpcServXDRCalls_Type = Counter32
_PclRpcServXDRCalls_Object = MibTableColumn
pclRpcServXDRCalls = _PclRpcServXDRCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 6),
    _PclRpcServXDRCalls_Type()
)
pclRpcServXDRCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclRpcServXDRCalls.setStatus("current")
_PclNfsCalls_Type = Counter32
_PclNfsCalls_Object = MibTableColumn
pclNfsCalls = _PclNfsCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 7),
    _PclNfsCalls_Type()
)
pclNfsCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsCalls.setStatus("current")
_PclNfsServBadCalls_Type = Counter32
_PclNfsServBadCalls_Object = MibTableColumn
pclNfsServBadCalls = _PclNfsServBadCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 8),
    _PclNfsServBadCalls_Type()
)
pclNfsServBadCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsServBadCalls.setStatus("current")
_PclNfsV2Nulls_Type = Counter32
_PclNfsV2Nulls_Object = MibTableColumn
pclNfsV2Nulls = _PclNfsV2Nulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 9),
    _PclNfsV2Nulls_Type()
)
pclNfsV2Nulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Nulls.setStatus("current")
_PclNfsV2Getattrs_Type = Counter32
_PclNfsV2Getattrs_Object = MibTableColumn
pclNfsV2Getattrs = _PclNfsV2Getattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 10),
    _PclNfsV2Getattrs_Type()
)
pclNfsV2Getattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Getattrs.setStatus("current")
_PclNfsV2Setattrs_Type = Counter32
_PclNfsV2Setattrs_Object = MibTableColumn
pclNfsV2Setattrs = _PclNfsV2Setattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 11),
    _PclNfsV2Setattrs_Type()
)
pclNfsV2Setattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Setattrs.setStatus("current")
_PclNfsV2Roots_Type = Counter32
_PclNfsV2Roots_Object = MibTableColumn
pclNfsV2Roots = _PclNfsV2Roots_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 12),
    _PclNfsV2Roots_Type()
)
pclNfsV2Roots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Roots.setStatus("current")
_PclNfsV2Lookups_Type = Counter32
_PclNfsV2Lookups_Object = MibTableColumn
pclNfsV2Lookups = _PclNfsV2Lookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 13),
    _PclNfsV2Lookups_Type()
)
pclNfsV2Lookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Lookups.setStatus("current")
_PclNfsV2Readlinks_Type = Counter32
_PclNfsV2Readlinks_Object = MibTableColumn
pclNfsV2Readlinks = _PclNfsV2Readlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 14),
    _PclNfsV2Readlinks_Type()
)
pclNfsV2Readlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Readlinks.setStatus("current")
_PclNfsV2Reads_Type = Counter32
_PclNfsV2Reads_Object = MibTableColumn
pclNfsV2Reads = _PclNfsV2Reads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 15),
    _PclNfsV2Reads_Type()
)
pclNfsV2Reads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Reads.setStatus("current")
_PclNfsV2Wrcaches_Type = Counter32
_PclNfsV2Wrcaches_Object = MibTableColumn
pclNfsV2Wrcaches = _PclNfsV2Wrcaches_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 16),
    _PclNfsV2Wrcaches_Type()
)
pclNfsV2Wrcaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Wrcaches.setStatus("current")
_PclNfsV2Writes_Type = Counter32
_PclNfsV2Writes_Object = MibTableColumn
pclNfsV2Writes = _PclNfsV2Writes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 17),
    _PclNfsV2Writes_Type()
)
pclNfsV2Writes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Writes.setStatus("current")
_PclNfsV2Creates_Type = Counter32
_PclNfsV2Creates_Object = MibTableColumn
pclNfsV2Creates = _PclNfsV2Creates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 18),
    _PclNfsV2Creates_Type()
)
pclNfsV2Creates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Creates.setStatus("current")
_PclNfsV2Removes_Type = Counter32
_PclNfsV2Removes_Object = MibTableColumn
pclNfsV2Removes = _PclNfsV2Removes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 19),
    _PclNfsV2Removes_Type()
)
pclNfsV2Removes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Removes.setStatus("current")
_PclNfsV2Renames_Type = Counter32
_PclNfsV2Renames_Object = MibTableColumn
pclNfsV2Renames = _PclNfsV2Renames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 20),
    _PclNfsV2Renames_Type()
)
pclNfsV2Renames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Renames.setStatus("current")
_PclNfsV2Links_Type = Counter32
_PclNfsV2Links_Object = MibTableColumn
pclNfsV2Links = _PclNfsV2Links_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 21),
    _PclNfsV2Links_Type()
)
pclNfsV2Links.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Links.setStatus("current")
_PclNfsV2Symlinks_Type = Counter32
_PclNfsV2Symlinks_Object = MibTableColumn
pclNfsV2Symlinks = _PclNfsV2Symlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 22),
    _PclNfsV2Symlinks_Type()
)
pclNfsV2Symlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Symlinks.setStatus("current")
_PclNfsV2Mkdirs_Type = Counter32
_PclNfsV2Mkdirs_Object = MibTableColumn
pclNfsV2Mkdirs = _PclNfsV2Mkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 23),
    _PclNfsV2Mkdirs_Type()
)
pclNfsV2Mkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Mkdirs.setStatus("current")
_PclNfsV2Rmdirs_Type = Counter32
_PclNfsV2Rmdirs_Object = MibTableColumn
pclNfsV2Rmdirs = _PclNfsV2Rmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 24),
    _PclNfsV2Rmdirs_Type()
)
pclNfsV2Rmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Rmdirs.setStatus("current")
_PclNfsV2Readdirs_Type = Counter32
_PclNfsV2Readdirs_Object = MibTableColumn
pclNfsV2Readdirs = _PclNfsV2Readdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 25),
    _PclNfsV2Readdirs_Type()
)
pclNfsV2Readdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Readdirs.setStatus("current")
_PclNfsV2Statfss_Type = Counter32
_PclNfsV2Statfss_Object = MibTableColumn
pclNfsV2Statfss = _PclNfsV2Statfss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 26),
    _PclNfsV2Statfss_Type()
)
pclNfsV2Statfss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Statfss.setStatus("current")
_PclNfsV3Nulls_Type = Counter32
_PclNfsV3Nulls_Object = MibTableColumn
pclNfsV3Nulls = _PclNfsV3Nulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 27),
    _PclNfsV3Nulls_Type()
)
pclNfsV3Nulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Nulls.setStatus("current")
_PclNfsV3Getattrs_Type = Counter32
_PclNfsV3Getattrs_Object = MibTableColumn
pclNfsV3Getattrs = _PclNfsV3Getattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 28),
    _PclNfsV3Getattrs_Type()
)
pclNfsV3Getattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Getattrs.setStatus("current")
_PclNfsV3Setattrs_Type = Counter32
_PclNfsV3Setattrs_Object = MibTableColumn
pclNfsV3Setattrs = _PclNfsV3Setattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 29),
    _PclNfsV3Setattrs_Type()
)
pclNfsV3Setattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Setattrs.setStatus("current")
_PclNfsV3Lookups_Type = Counter32
_PclNfsV3Lookups_Object = MibTableColumn
pclNfsV3Lookups = _PclNfsV3Lookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 30),
    _PclNfsV3Lookups_Type()
)
pclNfsV3Lookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Lookups.setStatus("current")
_PclNfsV3Accesss_Type = Counter32
_PclNfsV3Accesss_Object = MibTableColumn
pclNfsV3Accesss = _PclNfsV3Accesss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 31),
    _PclNfsV3Accesss_Type()
)
pclNfsV3Accesss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Accesss.setStatus("current")
_PclNfsV3Readlinks_Type = Counter32
_PclNfsV3Readlinks_Object = MibTableColumn
pclNfsV3Readlinks = _PclNfsV3Readlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 32),
    _PclNfsV3Readlinks_Type()
)
pclNfsV3Readlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Readlinks.setStatus("current")
_PclNfsV3Reads_Type = Counter32
_PclNfsV3Reads_Object = MibTableColumn
pclNfsV3Reads = _PclNfsV3Reads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 33),
    _PclNfsV3Reads_Type()
)
pclNfsV3Reads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Reads.setStatus("current")
_PclNfsV3Writes_Type = Counter32
_PclNfsV3Writes_Object = MibTableColumn
pclNfsV3Writes = _PclNfsV3Writes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 34),
    _PclNfsV3Writes_Type()
)
pclNfsV3Writes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Writes.setStatus("current")
_PclNfsV3Creates_Type = Counter32
_PclNfsV3Creates_Object = MibTableColumn
pclNfsV3Creates = _PclNfsV3Creates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 35),
    _PclNfsV3Creates_Type()
)
pclNfsV3Creates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Creates.setStatus("current")
_PclNfsV3Mkdirs_Type = Counter32
_PclNfsV3Mkdirs_Object = MibTableColumn
pclNfsV3Mkdirs = _PclNfsV3Mkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 36),
    _PclNfsV3Mkdirs_Type()
)
pclNfsV3Mkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Mkdirs.setStatus("current")
_PclNfsV3Symlinks_Type = Counter32
_PclNfsV3Symlinks_Object = MibTableColumn
pclNfsV3Symlinks = _PclNfsV3Symlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 37),
    _PclNfsV3Symlinks_Type()
)
pclNfsV3Symlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Symlinks.setStatus("current")
_PclNfsV3Mknods_Type = Counter32
_PclNfsV3Mknods_Object = MibTableColumn
pclNfsV3Mknods = _PclNfsV3Mknods_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 38),
    _PclNfsV3Mknods_Type()
)
pclNfsV3Mknods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Mknods.setStatus("current")
_PclNfsV3Removes_Type = Counter32
_PclNfsV3Removes_Object = MibTableColumn
pclNfsV3Removes = _PclNfsV3Removes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 39),
    _PclNfsV3Removes_Type()
)
pclNfsV3Removes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Removes.setStatus("current")
_PclNfsV3Rmdirs_Type = Counter32
_PclNfsV3Rmdirs_Object = MibTableColumn
pclNfsV3Rmdirs = _PclNfsV3Rmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 40),
    _PclNfsV3Rmdirs_Type()
)
pclNfsV3Rmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Rmdirs.setStatus("current")
_PclNfsV3Renames_Type = Counter32
_PclNfsV3Renames_Object = MibTableColumn
pclNfsV3Renames = _PclNfsV3Renames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 41),
    _PclNfsV3Renames_Type()
)
pclNfsV3Renames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Renames.setStatus("current")
_PclNfsV3Links_Type = Counter32
_PclNfsV3Links_Object = MibTableColumn
pclNfsV3Links = _PclNfsV3Links_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 42),
    _PclNfsV3Links_Type()
)
pclNfsV3Links.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Links.setStatus("current")
_PclNfsV3Readdirs_Type = Counter32
_PclNfsV3Readdirs_Object = MibTableColumn
pclNfsV3Readdirs = _PclNfsV3Readdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 43),
    _PclNfsV3Readdirs_Type()
)
pclNfsV3Readdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Readdirs.setStatus("current")
_PclNfsV3ReaddirPluss_Type = Counter32
_PclNfsV3ReaddirPluss_Object = MibTableColumn
pclNfsV3ReaddirPluss = _PclNfsV3ReaddirPluss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 44),
    _PclNfsV3ReaddirPluss_Type()
)
pclNfsV3ReaddirPluss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3ReaddirPluss.setStatus("current")
_PclNfsV3Fsstats_Type = Counter32
_PclNfsV3Fsstats_Object = MibTableColumn
pclNfsV3Fsstats = _PclNfsV3Fsstats_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 45),
    _PclNfsV3Fsstats_Type()
)
pclNfsV3Fsstats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Fsstats.setStatus("current")
_PclNfsV3Fsinfos_Type = Counter32
_PclNfsV3Fsinfos_Object = MibTableColumn
pclNfsV3Fsinfos = _PclNfsV3Fsinfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 46),
    _PclNfsV3Fsinfos_Type()
)
pclNfsV3Fsinfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Fsinfos.setStatus("current")
_PclNfsV3Pathconfs_Type = Counter32
_PclNfsV3Pathconfs_Object = MibTableColumn
pclNfsV3Pathconfs = _PclNfsV3Pathconfs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 47),
    _PclNfsV3Pathconfs_Type()
)
pclNfsV3Pathconfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Pathconfs.setStatus("current")
_PclNfsV3Commits_Type = Counter32
_PclNfsV3Commits_Object = MibTableColumn
pclNfsV3Commits = _PclNfsV3Commits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 48),
    _PclNfsV3Commits_Type()
)
pclNfsV3Commits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Commits.setStatus("current")


class _PclPerCent_Type(Integer32):
    """Custom type pclPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclPerCent_Type.__name__ = "Integer32"
_PclPerCent_Object = MibTableColumn
pclPerCent = _PclPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 49),
    _PclPerCent_Type()
)
pclPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclPerCent.setStatus("current")


class _PclNfsV2NullPerCent_Type(Integer32):
    """Custom type pclNfsV2NullPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2NullPerCent_Type.__name__ = "Integer32"
_PclNfsV2NullPerCent_Object = MibTableColumn
pclNfsV2NullPerCent = _PclNfsV2NullPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 50),
    _PclNfsV2NullPerCent_Type()
)
pclNfsV2NullPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2NullPerCent.setStatus("current")


class _PclNfsV2GetattrPerCent_Type(Integer32):
    """Custom type pclNfsV2GetattrPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2GetattrPerCent_Type.__name__ = "Integer32"
_PclNfsV2GetattrPerCent_Object = MibTableColumn
pclNfsV2GetattrPerCent = _PclNfsV2GetattrPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 51),
    _PclNfsV2GetattrPerCent_Type()
)
pclNfsV2GetattrPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2GetattrPerCent.setStatus("current")


class _PclNfsV2SetattrPerCent_Type(Integer32):
    """Custom type pclNfsV2SetattrPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2SetattrPerCent_Type.__name__ = "Integer32"
_PclNfsV2SetattrPerCent_Object = MibTableColumn
pclNfsV2SetattrPerCent = _PclNfsV2SetattrPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 52),
    _PclNfsV2SetattrPerCent_Type()
)
pclNfsV2SetattrPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2SetattrPerCent.setStatus("current")


class _PclNfsV2RootPerCent_Type(Integer32):
    """Custom type pclNfsV2RootPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2RootPerCent_Type.__name__ = "Integer32"
_PclNfsV2RootPerCent_Object = MibTableColumn
pclNfsV2RootPerCent = _PclNfsV2RootPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 53),
    _PclNfsV2RootPerCent_Type()
)
pclNfsV2RootPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2RootPerCent.setStatus("current")


class _PclNfsV2LookupPerCent_Type(Integer32):
    """Custom type pclNfsV2LookupPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2LookupPerCent_Type.__name__ = "Integer32"
_PclNfsV2LookupPerCent_Object = MibTableColumn
pclNfsV2LookupPerCent = _PclNfsV2LookupPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 54),
    _PclNfsV2LookupPerCent_Type()
)
pclNfsV2LookupPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2LookupPerCent.setStatus("current")


class _PclNfsV2ReadlinkPerCent_Type(Integer32):
    """Custom type pclNfsV2ReadlinkPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2ReadlinkPerCent_Type.__name__ = "Integer32"
_PclNfsV2ReadlinkPerCent_Object = MibTableColumn
pclNfsV2ReadlinkPerCent = _PclNfsV2ReadlinkPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 55),
    _PclNfsV2ReadlinkPerCent_Type()
)
pclNfsV2ReadlinkPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2ReadlinkPerCent.setStatus("current")


class _PclNfsV2ReadPerCent_Type(Integer32):
    """Custom type pclNfsV2ReadPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2ReadPerCent_Type.__name__ = "Integer32"
_PclNfsV2ReadPerCent_Object = MibTableColumn
pclNfsV2ReadPerCent = _PclNfsV2ReadPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 56),
    _PclNfsV2ReadPerCent_Type()
)
pclNfsV2ReadPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2ReadPerCent.setStatus("current")


class _PclNfsV2WrcachePerCent_Type(Integer32):
    """Custom type pclNfsV2WrcachePerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2WrcachePerCent_Type.__name__ = "Integer32"
_PclNfsV2WrcachePerCent_Object = MibTableColumn
pclNfsV2WrcachePerCent = _PclNfsV2WrcachePerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 57),
    _PclNfsV2WrcachePerCent_Type()
)
pclNfsV2WrcachePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2WrcachePerCent.setStatus("current")


class _PclNfsV2WritePerCent_Type(Integer32):
    """Custom type pclNfsV2WritePerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2WritePerCent_Type.__name__ = "Integer32"
_PclNfsV2WritePerCent_Object = MibTableColumn
pclNfsV2WritePerCent = _PclNfsV2WritePerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 58),
    _PclNfsV2WritePerCent_Type()
)
pclNfsV2WritePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2WritePerCent.setStatus("current")


class _PclNfsV2CreatePerCent_Type(Integer32):
    """Custom type pclNfsV2CreatePerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2CreatePerCent_Type.__name__ = "Integer32"
_PclNfsV2CreatePerCent_Object = MibTableColumn
pclNfsV2CreatePerCent = _PclNfsV2CreatePerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 59),
    _PclNfsV2CreatePerCent_Type()
)
pclNfsV2CreatePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2CreatePerCent.setStatus("current")


class _PclNfsV2RemovePerCent_Type(Integer32):
    """Custom type pclNfsV2RemovePerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2RemovePerCent_Type.__name__ = "Integer32"
_PclNfsV2RemovePerCent_Object = MibTableColumn
pclNfsV2RemovePerCent = _PclNfsV2RemovePerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 60),
    _PclNfsV2RemovePerCent_Type()
)
pclNfsV2RemovePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2RemovePerCent.setStatus("current")


class _PclNfsV2RenamePerCent_Type(Integer32):
    """Custom type pclNfsV2RenamePerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2RenamePerCent_Type.__name__ = "Integer32"
_PclNfsV2RenamePerCent_Object = MibTableColumn
pclNfsV2RenamePerCent = _PclNfsV2RenamePerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 61),
    _PclNfsV2RenamePerCent_Type()
)
pclNfsV2RenamePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2RenamePerCent.setStatus("current")


class _PclNfsV2LinkPerCent_Type(Integer32):
    """Custom type pclNfsV2LinkPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2LinkPerCent_Type.__name__ = "Integer32"
_PclNfsV2LinkPerCent_Object = MibTableColumn
pclNfsV2LinkPerCent = _PclNfsV2LinkPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 62),
    _PclNfsV2LinkPerCent_Type()
)
pclNfsV2LinkPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2LinkPerCent.setStatus("current")


class _PclNfsV2SymlinkPerCent_Type(Integer32):
    """Custom type pclNfsV2SymlinkPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2SymlinkPerCent_Type.__name__ = "Integer32"
_PclNfsV2SymlinkPerCent_Object = MibTableColumn
pclNfsV2SymlinkPerCent = _PclNfsV2SymlinkPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 63),
    _PclNfsV2SymlinkPerCent_Type()
)
pclNfsV2SymlinkPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2SymlinkPerCent.setStatus("current")


class _PclNfsV2MkdirPerCent_Type(Integer32):
    """Custom type pclNfsV2MkdirPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2MkdirPerCent_Type.__name__ = "Integer32"
_PclNfsV2MkdirPerCent_Object = MibTableColumn
pclNfsV2MkdirPerCent = _PclNfsV2MkdirPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 64),
    _PclNfsV2MkdirPerCent_Type()
)
pclNfsV2MkdirPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2MkdirPerCent.setStatus("current")


class _PclNfsV2RmdirPerCent_Type(Integer32):
    """Custom type pclNfsV2RmdirPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2RmdirPerCent_Type.__name__ = "Integer32"
_PclNfsV2RmdirPerCent_Object = MibTableColumn
pclNfsV2RmdirPerCent = _PclNfsV2RmdirPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 65),
    _PclNfsV2RmdirPerCent_Type()
)
pclNfsV2RmdirPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2RmdirPerCent.setStatus("current")


class _PclNfsV2ReaddirPerCent_Type(Integer32):
    """Custom type pclNfsV2ReaddirPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2ReaddirPerCent_Type.__name__ = "Integer32"
_PclNfsV2ReaddirPerCent_Object = MibTableColumn
pclNfsV2ReaddirPerCent = _PclNfsV2ReaddirPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 66),
    _PclNfsV2ReaddirPerCent_Type()
)
pclNfsV2ReaddirPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2ReaddirPerCent.setStatus("current")


class _PclNfsV2StatfsPerCent_Type(Integer32):
    """Custom type pclNfsV2StatfsPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV2StatfsPerCent_Type.__name__ = "Integer32"
_PclNfsV2StatfsPerCent_Object = MibTableColumn
pclNfsV2StatfsPerCent = _PclNfsV2StatfsPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 67),
    _PclNfsV2StatfsPerCent_Type()
)
pclNfsV2StatfsPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2StatfsPerCent.setStatus("current")


class _PclNfsV3NullPerCent_Type(Integer32):
    """Custom type pclNfsV3NullPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3NullPerCent_Type.__name__ = "Integer32"
_PclNfsV3NullPerCent_Object = MibTableColumn
pclNfsV3NullPerCent = _PclNfsV3NullPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 68),
    _PclNfsV3NullPerCent_Type()
)
pclNfsV3NullPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3NullPerCent.setStatus("current")


class _PclNfsV3GetattrPerCent_Type(Integer32):
    """Custom type pclNfsV3GetattrPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3GetattrPerCent_Type.__name__ = "Integer32"
_PclNfsV3GetattrPerCent_Object = MibTableColumn
pclNfsV3GetattrPerCent = _PclNfsV3GetattrPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 69),
    _PclNfsV3GetattrPerCent_Type()
)
pclNfsV3GetattrPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3GetattrPerCent.setStatus("current")


class _PclNfsV3SetattrPerCent_Type(Integer32):
    """Custom type pclNfsV3SetattrPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3SetattrPerCent_Type.__name__ = "Integer32"
_PclNfsV3SetattrPerCent_Object = MibTableColumn
pclNfsV3SetattrPerCent = _PclNfsV3SetattrPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 70),
    _PclNfsV3SetattrPerCent_Type()
)
pclNfsV3SetattrPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3SetattrPerCent.setStatus("current")


class _PclNfsV3LookupPerCent_Type(Integer32):
    """Custom type pclNfsV3LookupPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3LookupPerCent_Type.__name__ = "Integer32"
_PclNfsV3LookupPerCent_Object = MibTableColumn
pclNfsV3LookupPerCent = _PclNfsV3LookupPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 71),
    _PclNfsV3LookupPerCent_Type()
)
pclNfsV3LookupPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3LookupPerCent.setStatus("current")


class _PclNfsV3AccessPerCent_Type(Integer32):
    """Custom type pclNfsV3AccessPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3AccessPerCent_Type.__name__ = "Integer32"
_PclNfsV3AccessPerCent_Object = MibTableColumn
pclNfsV3AccessPerCent = _PclNfsV3AccessPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 72),
    _PclNfsV3AccessPerCent_Type()
)
pclNfsV3AccessPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3AccessPerCent.setStatus("current")


class _PclNfsV3ReadlinkPerCent_Type(Integer32):
    """Custom type pclNfsV3ReadlinkPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3ReadlinkPerCent_Type.__name__ = "Integer32"
_PclNfsV3ReadlinkPerCent_Object = MibTableColumn
pclNfsV3ReadlinkPerCent = _PclNfsV3ReadlinkPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 73),
    _PclNfsV3ReadlinkPerCent_Type()
)
pclNfsV3ReadlinkPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3ReadlinkPerCent.setStatus("current")


class _PclNfsV3ReadPerCent_Type(Integer32):
    """Custom type pclNfsV3ReadPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3ReadPerCent_Type.__name__ = "Integer32"
_PclNfsV3ReadPerCent_Object = MibTableColumn
pclNfsV3ReadPerCent = _PclNfsV3ReadPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 74),
    _PclNfsV3ReadPerCent_Type()
)
pclNfsV3ReadPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3ReadPerCent.setStatus("current")


class _PclNfsV3WritePerCent_Type(Integer32):
    """Custom type pclNfsV3WritePerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3WritePerCent_Type.__name__ = "Integer32"
_PclNfsV3WritePerCent_Object = MibTableColumn
pclNfsV3WritePerCent = _PclNfsV3WritePerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 75),
    _PclNfsV3WritePerCent_Type()
)
pclNfsV3WritePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3WritePerCent.setStatus("current")


class _PclNfsV3CreatePerCent_Type(Integer32):
    """Custom type pclNfsV3CreatePerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3CreatePerCent_Type.__name__ = "Integer32"
_PclNfsV3CreatePerCent_Object = MibTableColumn
pclNfsV3CreatePerCent = _PclNfsV3CreatePerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 76),
    _PclNfsV3CreatePerCent_Type()
)
pclNfsV3CreatePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3CreatePerCent.setStatus("current")


class _PclNfsV3MkdirPerCent_Type(Integer32):
    """Custom type pclNfsV3MkdirPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3MkdirPerCent_Type.__name__ = "Integer32"
_PclNfsV3MkdirPerCent_Object = MibTableColumn
pclNfsV3MkdirPerCent = _PclNfsV3MkdirPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 77),
    _PclNfsV3MkdirPerCent_Type()
)
pclNfsV3MkdirPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3MkdirPerCent.setStatus("current")


class _PclNfsV3SymlinkPerCent_Type(Integer32):
    """Custom type pclNfsV3SymlinkPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3SymlinkPerCent_Type.__name__ = "Integer32"
_PclNfsV3SymlinkPerCent_Object = MibTableColumn
pclNfsV3SymlinkPerCent = _PclNfsV3SymlinkPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 78),
    _PclNfsV3SymlinkPerCent_Type()
)
pclNfsV3SymlinkPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3SymlinkPerCent.setStatus("current")


class _PclNfsV3MknodPerCent_Type(Integer32):
    """Custom type pclNfsV3MknodPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3MknodPerCent_Type.__name__ = "Integer32"
_PclNfsV3MknodPerCent_Object = MibTableColumn
pclNfsV3MknodPerCent = _PclNfsV3MknodPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 79),
    _PclNfsV3MknodPerCent_Type()
)
pclNfsV3MknodPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3MknodPerCent.setStatus("current")


class _PclNfsV3RemovePerCent_Type(Integer32):
    """Custom type pclNfsV3RemovePerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3RemovePerCent_Type.__name__ = "Integer32"
_PclNfsV3RemovePerCent_Object = MibTableColumn
pclNfsV3RemovePerCent = _PclNfsV3RemovePerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 80),
    _PclNfsV3RemovePerCent_Type()
)
pclNfsV3RemovePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3RemovePerCent.setStatus("current")


class _PclNfsV3RmdirPerCent_Type(Integer32):
    """Custom type pclNfsV3RmdirPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3RmdirPerCent_Type.__name__ = "Integer32"
_PclNfsV3RmdirPerCent_Object = MibTableColumn
pclNfsV3RmdirPerCent = _PclNfsV3RmdirPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 81),
    _PclNfsV3RmdirPerCent_Type()
)
pclNfsV3RmdirPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3RmdirPerCent.setStatus("current")


class _PclNfsV3RenamePerCent_Type(Integer32):
    """Custom type pclNfsV3RenamePerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3RenamePerCent_Type.__name__ = "Integer32"
_PclNfsV3RenamePerCent_Object = MibTableColumn
pclNfsV3RenamePerCent = _PclNfsV3RenamePerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 82),
    _PclNfsV3RenamePerCent_Type()
)
pclNfsV3RenamePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3RenamePerCent.setStatus("current")


class _PclNfsV3LinkPerCent_Type(Integer32):
    """Custom type pclNfsV3LinkPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3LinkPerCent_Type.__name__ = "Integer32"
_PclNfsV3LinkPerCent_Object = MibTableColumn
pclNfsV3LinkPerCent = _PclNfsV3LinkPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 83),
    _PclNfsV3LinkPerCent_Type()
)
pclNfsV3LinkPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3LinkPerCent.setStatus("current")


class _PclNfsV3ReaddirPerCent_Type(Integer32):
    """Custom type pclNfsV3ReaddirPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3ReaddirPerCent_Type.__name__ = "Integer32"
_PclNfsV3ReaddirPerCent_Object = MibTableColumn
pclNfsV3ReaddirPerCent = _PclNfsV3ReaddirPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 84),
    _PclNfsV3ReaddirPerCent_Type()
)
pclNfsV3ReaddirPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3ReaddirPerCent.setStatus("current")


class _PclNfsV3ReaddirPlusPerCent_Type(Integer32):
    """Custom type pclNfsV3ReaddirPlusPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3ReaddirPlusPerCent_Type.__name__ = "Integer32"
_PclNfsV3ReaddirPlusPerCent_Object = MibTableColumn
pclNfsV3ReaddirPlusPerCent = _PclNfsV3ReaddirPlusPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 85),
    _PclNfsV3ReaddirPlusPerCent_Type()
)
pclNfsV3ReaddirPlusPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3ReaddirPlusPerCent.setStatus("current")


class _PclNfsV3FsstatPerCent_Type(Integer32):
    """Custom type pclNfsV3FsstatPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3FsstatPerCent_Type.__name__ = "Integer32"
_PclNfsV3FsstatPerCent_Object = MibTableColumn
pclNfsV3FsstatPerCent = _PclNfsV3FsstatPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 86),
    _PclNfsV3FsstatPerCent_Type()
)
pclNfsV3FsstatPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3FsstatPerCent.setStatus("current")


class _PclNfsV3FsinfoPerCent_Type(Integer32):
    """Custom type pclNfsV3FsinfoPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3FsinfoPerCent_Type.__name__ = "Integer32"
_PclNfsV3FsinfoPerCent_Object = MibTableColumn
pclNfsV3FsinfoPerCent = _PclNfsV3FsinfoPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 87),
    _PclNfsV3FsinfoPerCent_Type()
)
pclNfsV3FsinfoPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3FsinfoPerCent.setStatus("current")


class _PclNfsV3PathconfPerCent_Type(Integer32):
    """Custom type pclNfsV3PathconfPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3PathconfPerCent_Type.__name__ = "Integer32"
_PclNfsV3PathconfPerCent_Object = MibTableColumn
pclNfsV3PathconfPerCent = _PclNfsV3PathconfPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 88),
    _PclNfsV3PathconfPerCent_Type()
)
pclNfsV3PathconfPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3PathconfPerCent.setStatus("current")


class _PclNfsV3CommitPerCent_Type(Integer32):
    """Custom type pclNfsV3CommitPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PclNfsV3CommitPerCent_Type.__name__ = "Integer32"
_PclNfsV3CommitPerCent_Object = MibTableColumn
pclNfsV3CommitPerCent = _PclNfsV3CommitPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 89),
    _PclNfsV3CommitPerCent_Type()
)
pclNfsV3CommitPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3CommitPerCent.setStatus("current")
_PclNfsV2Read512Calls_Type = Counter32
_PclNfsV2Read512Calls_Object = MibTableColumn
pclNfsV2Read512Calls = _PclNfsV2Read512Calls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 90),
    _PclNfsV2Read512Calls_Type()
)
pclNfsV2Read512Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Read512Calls.setStatus("current")
_PclNfsV2Read1KCalls_Type = Counter32
_PclNfsV2Read1KCalls_Object = MibTableColumn
pclNfsV2Read1KCalls = _PclNfsV2Read1KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 91),
    _PclNfsV2Read1KCalls_Type()
)
pclNfsV2Read1KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Read1KCalls.setStatus("current")
_PclNfsV2Read2KCalls_Type = Counter32
_PclNfsV2Read2KCalls_Object = MibTableColumn
pclNfsV2Read2KCalls = _PclNfsV2Read2KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 92),
    _PclNfsV2Read2KCalls_Type()
)
pclNfsV2Read2KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Read2KCalls.setStatus("current")
_PclNfsV2Read4KCalls_Type = Counter32
_PclNfsV2Read4KCalls_Object = MibTableColumn
pclNfsV2Read4KCalls = _PclNfsV2Read4KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 93),
    _PclNfsV2Read4KCalls_Type()
)
pclNfsV2Read4KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Read4KCalls.setStatus("current")
_PclNfsV2Read8KCalls_Type = Counter32
_PclNfsV2Read8KCalls_Object = MibTableColumn
pclNfsV2Read8KCalls = _PclNfsV2Read8KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 94),
    _PclNfsV2Read8KCalls_Type()
)
pclNfsV2Read8KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Read8KCalls.setStatus("current")
_PclNfsV2Read16KCalls_Type = Counter32
_PclNfsV2Read16KCalls_Object = MibTableColumn
pclNfsV2Read16KCalls = _PclNfsV2Read16KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 95),
    _PclNfsV2Read16KCalls_Type()
)
pclNfsV2Read16KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Read16KCalls.setStatus("current")
_PclNfsV2Read32KCalls_Type = Counter32
_PclNfsV2Read32KCalls_Object = MibTableColumn
pclNfsV2Read32KCalls = _PclNfsV2Read32KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 96),
    _PclNfsV2Read32KCalls_Type()
)
pclNfsV2Read32KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Read32KCalls.setStatus("current")
_PclNfsV2Read64KCalls_Type = Counter32
_PclNfsV2Read64KCalls_Object = MibTableColumn
pclNfsV2Read64KCalls = _PclNfsV2Read64KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 97),
    _PclNfsV2Read64KCalls_Type()
)
pclNfsV2Read64KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Read64KCalls.setStatus("current")
_PclNfsV2Read128KCalls_Type = Counter32
_PclNfsV2Read128KCalls_Object = MibTableColumn
pclNfsV2Read128KCalls = _PclNfsV2Read128KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 98),
    _PclNfsV2Read128KCalls_Type()
)
pclNfsV2Read128KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Read128KCalls.setStatus("current")
_PclNfsV2Write512Calls_Type = Counter32
_PclNfsV2Write512Calls_Object = MibTableColumn
pclNfsV2Write512Calls = _PclNfsV2Write512Calls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 99),
    _PclNfsV2Write512Calls_Type()
)
pclNfsV2Write512Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Write512Calls.setStatus("current")
_PclNfsV2Write1KCalls_Type = Counter32
_PclNfsV2Write1KCalls_Object = MibTableColumn
pclNfsV2Write1KCalls = _PclNfsV2Write1KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 100),
    _PclNfsV2Write1KCalls_Type()
)
pclNfsV2Write1KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Write1KCalls.setStatus("current")
_PclNfsV2Write2KCalls_Type = Counter32
_PclNfsV2Write2KCalls_Object = MibTableColumn
pclNfsV2Write2KCalls = _PclNfsV2Write2KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 101),
    _PclNfsV2Write2KCalls_Type()
)
pclNfsV2Write2KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Write2KCalls.setStatus("current")
_PclNfsV2Write4KCalls_Type = Counter32
_PclNfsV2Write4KCalls_Object = MibTableColumn
pclNfsV2Write4KCalls = _PclNfsV2Write4KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 102),
    _PclNfsV2Write4KCalls_Type()
)
pclNfsV2Write4KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Write4KCalls.setStatus("current")
_PclNfsV2Write8KCalls_Type = Counter32
_PclNfsV2Write8KCalls_Object = MibTableColumn
pclNfsV2Write8KCalls = _PclNfsV2Write8KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 103),
    _PclNfsV2Write8KCalls_Type()
)
pclNfsV2Write8KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Write8KCalls.setStatus("current")
_PclNfsV2Write16KCalls_Type = Counter32
_PclNfsV2Write16KCalls_Object = MibTableColumn
pclNfsV2Write16KCalls = _PclNfsV2Write16KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 104),
    _PclNfsV2Write16KCalls_Type()
)
pclNfsV2Write16KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Write16KCalls.setStatus("current")
_PclNfsV2Write32KCalls_Type = Counter32
_PclNfsV2Write32KCalls_Object = MibTableColumn
pclNfsV2Write32KCalls = _PclNfsV2Write32KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 105),
    _PclNfsV2Write32KCalls_Type()
)
pclNfsV2Write32KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Write32KCalls.setStatus("current")
_PclNfsV2Write64KCalls_Type = Counter32
_PclNfsV2Write64KCalls_Object = MibTableColumn
pclNfsV2Write64KCalls = _PclNfsV2Write64KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 106),
    _PclNfsV2Write64KCalls_Type()
)
pclNfsV2Write64KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Write64KCalls.setStatus("current")
_PclNfsV2Write128KCalls_Type = Counter32
_PclNfsV2Write128KCalls_Object = MibTableColumn
pclNfsV2Write128KCalls = _PclNfsV2Write128KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 107),
    _PclNfsV2Write128KCalls_Type()
)
pclNfsV2Write128KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV2Write128KCalls.setStatus("current")
_PclNfsV3Read512Calls_Type = Counter32
_PclNfsV3Read512Calls_Object = MibTableColumn
pclNfsV3Read512Calls = _PclNfsV3Read512Calls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 108),
    _PclNfsV3Read512Calls_Type()
)
pclNfsV3Read512Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Read512Calls.setStatus("current")
_PclNfsV3Read1KCalls_Type = Counter32
_PclNfsV3Read1KCalls_Object = MibTableColumn
pclNfsV3Read1KCalls = _PclNfsV3Read1KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 109),
    _PclNfsV3Read1KCalls_Type()
)
pclNfsV3Read1KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Read1KCalls.setStatus("current")
_PclNfsV3Read2KCalls_Type = Counter32
_PclNfsV3Read2KCalls_Object = MibTableColumn
pclNfsV3Read2KCalls = _PclNfsV3Read2KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 110),
    _PclNfsV3Read2KCalls_Type()
)
pclNfsV3Read2KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Read2KCalls.setStatus("current")
_PclNfsV3Read4KCalls_Type = Counter32
_PclNfsV3Read4KCalls_Object = MibTableColumn
pclNfsV3Read4KCalls = _PclNfsV3Read4KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 111),
    _PclNfsV3Read4KCalls_Type()
)
pclNfsV3Read4KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Read4KCalls.setStatus("current")
_PclNfsV3Read8KCalls_Type = Counter32
_PclNfsV3Read8KCalls_Object = MibTableColumn
pclNfsV3Read8KCalls = _PclNfsV3Read8KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 112),
    _PclNfsV3Read8KCalls_Type()
)
pclNfsV3Read8KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Read8KCalls.setStatus("current")
_PclNfsV3Read16KCalls_Type = Counter32
_PclNfsV3Read16KCalls_Object = MibTableColumn
pclNfsV3Read16KCalls = _PclNfsV3Read16KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 113),
    _PclNfsV3Read16KCalls_Type()
)
pclNfsV3Read16KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Read16KCalls.setStatus("current")
_PclNfsV3Read32KCalls_Type = Counter32
_PclNfsV3Read32KCalls_Object = MibTableColumn
pclNfsV3Read32KCalls = _PclNfsV3Read32KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 114),
    _PclNfsV3Read32KCalls_Type()
)
pclNfsV3Read32KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Read32KCalls.setStatus("current")
_PclNfsV3Read64KCalls_Type = Counter32
_PclNfsV3Read64KCalls_Object = MibTableColumn
pclNfsV3Read64KCalls = _PclNfsV3Read64KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 115),
    _PclNfsV3Read64KCalls_Type()
)
pclNfsV3Read64KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Read64KCalls.setStatus("current")
_PclNfsV3Read128KCalls_Type = Counter32
_PclNfsV3Read128KCalls_Object = MibTableColumn
pclNfsV3Read128KCalls = _PclNfsV3Read128KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 116),
    _PclNfsV3Read128KCalls_Type()
)
pclNfsV3Read128KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Read128KCalls.setStatus("current")
_PclNfsV3Write512Calls_Type = Counter32
_PclNfsV3Write512Calls_Object = MibTableColumn
pclNfsV3Write512Calls = _PclNfsV3Write512Calls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 117),
    _PclNfsV3Write512Calls_Type()
)
pclNfsV3Write512Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Write512Calls.setStatus("current")
_PclNfsV3Write1KCalls_Type = Counter32
_PclNfsV3Write1KCalls_Object = MibTableColumn
pclNfsV3Write1KCalls = _PclNfsV3Write1KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 118),
    _PclNfsV3Write1KCalls_Type()
)
pclNfsV3Write1KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Write1KCalls.setStatus("current")
_PclNfsV3Write2KCalls_Type = Counter32
_PclNfsV3Write2KCalls_Object = MibTableColumn
pclNfsV3Write2KCalls = _PclNfsV3Write2KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 119),
    _PclNfsV3Write2KCalls_Type()
)
pclNfsV3Write2KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Write2KCalls.setStatus("current")
_PclNfsV3Write4KCalls_Type = Counter32
_PclNfsV3Write4KCalls_Object = MibTableColumn
pclNfsV3Write4KCalls = _PclNfsV3Write4KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 120),
    _PclNfsV3Write4KCalls_Type()
)
pclNfsV3Write4KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Write4KCalls.setStatus("current")
_PclNfsV3Write8KCalls_Type = Counter32
_PclNfsV3Write8KCalls_Object = MibTableColumn
pclNfsV3Write8KCalls = _PclNfsV3Write8KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 121),
    _PclNfsV3Write8KCalls_Type()
)
pclNfsV3Write8KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Write8KCalls.setStatus("current")
_PclNfsV3Write16KCalls_Type = Counter32
_PclNfsV3Write16KCalls_Object = MibTableColumn
pclNfsV3Write16KCalls = _PclNfsV3Write16KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 122),
    _PclNfsV3Write16KCalls_Type()
)
pclNfsV3Write16KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Write16KCalls.setStatus("current")
_PclNfsV3Write32KCalls_Type = Counter32
_PclNfsV3Write32KCalls_Object = MibTableColumn
pclNfsV3Write32KCalls = _PclNfsV3Write32KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 123),
    _PclNfsV3Write32KCalls_Type()
)
pclNfsV3Write32KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Write32KCalls.setStatus("current")
_PclNfsV3Write64KCalls_Type = Counter32
_PclNfsV3Write64KCalls_Object = MibTableColumn
pclNfsV3Write64KCalls = _PclNfsV3Write64KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 124),
    _PclNfsV3Write64KCalls_Type()
)
pclNfsV3Write64KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Write64KCalls.setStatus("current")
_PclNfsV3Write128KCalls_Type = Counter32
_PclNfsV3Write128KCalls_Object = MibTableColumn
pclNfsV3Write128KCalls = _PclNfsV3Write128KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 1, 1, 125),
    _PclNfsV3Write128KCalls_Type()
)
pclNfsV3Write128KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNfsV3Write128KCalls.setStatus("current")
_PclNumber_Type = Integer32
_PclNumber_Object = MibScalar
pclNumber = _PclNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 1, 3, 2),
    _PclNumber_Type()
)
pclNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pclNumber.setStatus("current")
_TotNfs_ObjectIdentity = ObjectIdentity
totNfs = _TotNfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2)
)
_TrpcServ_ObjectIdentity = ObjectIdentity
trpcServ = _TrpcServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 1)
)
_TrpcCalls_Type = Counter32
_TrpcCalls_Object = MibScalar
trpcCalls = _TrpcCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 1, 1),
    _TrpcCalls_Type()
)
trpcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpcCalls.setStatus("current")
_TrpcBadCalls_Type = Counter32
_TrpcBadCalls_Object = MibScalar
trpcBadCalls = _TrpcBadCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 1, 2),
    _TrpcBadCalls_Type()
)
trpcBadCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpcBadCalls.setStatus("current")
_TrpcNullRecvs_Type = Counter32
_TrpcNullRecvs_Object = MibScalar
trpcNullRecvs = _TrpcNullRecvs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 1, 3),
    _TrpcNullRecvs_Type()
)
trpcNullRecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpcNullRecvs.setStatus("current")
_TrpcBadLens_Type = Counter32
_TrpcBadLens_Object = MibScalar
trpcBadLens = _TrpcBadLens_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 1, 4),
    _TrpcBadLens_Type()
)
trpcBadLens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpcBadLens.setStatus("current")
_TrpcServXDRCalls_Type = Counter32
_TrpcServXDRCalls_Object = MibScalar
trpcServXDRCalls = _TrpcServXDRCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 1, 5),
    _TrpcServXDRCalls_Type()
)
trpcServXDRCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpcServXDRCalls.setStatus("current")
_TnfsServ_ObjectIdentity = ObjectIdentity
tnfsServ = _TnfsServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2)
)
_TnfsCalls_Type = Counter32
_TnfsCalls_Object = MibScalar
tnfsCalls = _TnfsCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 1),
    _TnfsCalls_Type()
)
tnfsCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnfsCalls.setStatus("current")
_TnfsServBadCalls_Type = Counter32
_TnfsServBadCalls_Object = MibScalar
tnfsServBadCalls = _TnfsServBadCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 2),
    _TnfsServBadCalls_Type()
)
tnfsServBadCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnfsServBadCalls.setStatus("current")
_TnfsV2_ObjectIdentity = ObjectIdentity
tnfsV2 = _TnfsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3)
)
_Tv2Calls_ObjectIdentity = ObjectIdentity
tv2Calls = _Tv2Calls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1)
)
_Tv2cNulls_Type = Counter32
_Tv2cNulls_Object = MibScalar
tv2cNulls = _Tv2cNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 1),
    _Tv2cNulls_Type()
)
tv2cNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cNulls.setStatus("current")
_Tv2cGetattrs_Type = Counter32
_Tv2cGetattrs_Object = MibScalar
tv2cGetattrs = _Tv2cGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 2),
    _Tv2cGetattrs_Type()
)
tv2cGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cGetattrs.setStatus("current")
_Tv2cSetattrs_Type = Counter32
_Tv2cSetattrs_Object = MibScalar
tv2cSetattrs = _Tv2cSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 3),
    _Tv2cSetattrs_Type()
)
tv2cSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cSetattrs.setStatus("current")
_Tv2cRoots_Type = Counter32
_Tv2cRoots_Object = MibScalar
tv2cRoots = _Tv2cRoots_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 4),
    _Tv2cRoots_Type()
)
tv2cRoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cRoots.setStatus("current")
_Tv2cLookups_Type = Counter32
_Tv2cLookups_Object = MibScalar
tv2cLookups = _Tv2cLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 5),
    _Tv2cLookups_Type()
)
tv2cLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cLookups.setStatus("current")
_Tv2cReadlinks_Type = Counter32
_Tv2cReadlinks_Object = MibScalar
tv2cReadlinks = _Tv2cReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 6),
    _Tv2cReadlinks_Type()
)
tv2cReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cReadlinks.setStatus("current")
_Tv2cReads_Type = Counter32
_Tv2cReads_Object = MibScalar
tv2cReads = _Tv2cReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 7),
    _Tv2cReads_Type()
)
tv2cReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cReads.setStatus("current")
_Tv2cWrcaches_Type = Counter32
_Tv2cWrcaches_Object = MibScalar
tv2cWrcaches = _Tv2cWrcaches_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 8),
    _Tv2cWrcaches_Type()
)
tv2cWrcaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cWrcaches.setStatus("current")
_Tv2cWrites_Type = Counter32
_Tv2cWrites_Object = MibScalar
tv2cWrites = _Tv2cWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 9),
    _Tv2cWrites_Type()
)
tv2cWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cWrites.setStatus("current")
_Tv2cCreates_Type = Counter32
_Tv2cCreates_Object = MibScalar
tv2cCreates = _Tv2cCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 10),
    _Tv2cCreates_Type()
)
tv2cCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cCreates.setStatus("current")
_Tv2cRemoves_Type = Counter32
_Tv2cRemoves_Object = MibScalar
tv2cRemoves = _Tv2cRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 11),
    _Tv2cRemoves_Type()
)
tv2cRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cRemoves.setStatus("current")
_Tv2cRenames_Type = Counter32
_Tv2cRenames_Object = MibScalar
tv2cRenames = _Tv2cRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 12),
    _Tv2cRenames_Type()
)
tv2cRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cRenames.setStatus("current")
_Tv2cLinks_Type = Counter32
_Tv2cLinks_Object = MibScalar
tv2cLinks = _Tv2cLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 13),
    _Tv2cLinks_Type()
)
tv2cLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cLinks.setStatus("current")
_Tv2cSymlinks_Type = Counter32
_Tv2cSymlinks_Object = MibScalar
tv2cSymlinks = _Tv2cSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 14),
    _Tv2cSymlinks_Type()
)
tv2cSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cSymlinks.setStatus("current")
_Tv2cMkdirs_Type = Counter32
_Tv2cMkdirs_Object = MibScalar
tv2cMkdirs = _Tv2cMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 15),
    _Tv2cMkdirs_Type()
)
tv2cMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cMkdirs.setStatus("current")
_Tv2cRmdirs_Type = Counter32
_Tv2cRmdirs_Object = MibScalar
tv2cRmdirs = _Tv2cRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 16),
    _Tv2cRmdirs_Type()
)
tv2cRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cRmdirs.setStatus("current")
_Tv2cReaddirs_Type = Counter32
_Tv2cReaddirs_Object = MibScalar
tv2cReaddirs = _Tv2cReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 17),
    _Tv2cReaddirs_Type()
)
tv2cReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cReaddirs.setStatus("current")
_Tv2cStatfss_Type = Counter32
_Tv2cStatfss_Object = MibScalar
tv2cStatfss = _Tv2cStatfss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 1, 18),
    _Tv2cStatfss_Type()
)
tv2cStatfss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cStatfss.setStatus("current")
_Tv2Percent_ObjectIdentity = ObjectIdentity
tv2Percent = _Tv2Percent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2)
)


class _Tv2pNulls_Type(Integer32):
    """Custom type tv2pNulls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pNulls_Type.__name__ = "Integer32"
_Tv2pNulls_Object = MibScalar
tv2pNulls = _Tv2pNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 1),
    _Tv2pNulls_Type()
)
tv2pNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pNulls.setStatus("current")


class _Tv2pGetattrs_Type(Integer32):
    """Custom type tv2pGetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pGetattrs_Type.__name__ = "Integer32"
_Tv2pGetattrs_Object = MibScalar
tv2pGetattrs = _Tv2pGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 2),
    _Tv2pGetattrs_Type()
)
tv2pGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pGetattrs.setStatus("current")


class _Tv2pSetattrs_Type(Integer32):
    """Custom type tv2pSetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pSetattrs_Type.__name__ = "Integer32"
_Tv2pSetattrs_Object = MibScalar
tv2pSetattrs = _Tv2pSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 3),
    _Tv2pSetattrs_Type()
)
tv2pSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pSetattrs.setStatus("current")


class _Tv2pRoots_Type(Integer32):
    """Custom type tv2pRoots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pRoots_Type.__name__ = "Integer32"
_Tv2pRoots_Object = MibScalar
tv2pRoots = _Tv2pRoots_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 4),
    _Tv2pRoots_Type()
)
tv2pRoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pRoots.setStatus("current")


class _Tv2pLookups_Type(Integer32):
    """Custom type tv2pLookups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pLookups_Type.__name__ = "Integer32"
_Tv2pLookups_Object = MibScalar
tv2pLookups = _Tv2pLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 5),
    _Tv2pLookups_Type()
)
tv2pLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pLookups.setStatus("current")


class _Tv2pReadlinks_Type(Integer32):
    """Custom type tv2pReadlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pReadlinks_Type.__name__ = "Integer32"
_Tv2pReadlinks_Object = MibScalar
tv2pReadlinks = _Tv2pReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 6),
    _Tv2pReadlinks_Type()
)
tv2pReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pReadlinks.setStatus("current")


class _Tv2pReads_Type(Integer32):
    """Custom type tv2pReads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pReads_Type.__name__ = "Integer32"
_Tv2pReads_Object = MibScalar
tv2pReads = _Tv2pReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 7),
    _Tv2pReads_Type()
)
tv2pReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pReads.setStatus("current")


class _Tv2pWrcaches_Type(Integer32):
    """Custom type tv2pWrcaches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pWrcaches_Type.__name__ = "Integer32"
_Tv2pWrcaches_Object = MibScalar
tv2pWrcaches = _Tv2pWrcaches_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 8),
    _Tv2pWrcaches_Type()
)
tv2pWrcaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pWrcaches.setStatus("current")


class _Tv2pWrites_Type(Integer32):
    """Custom type tv2pWrites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pWrites_Type.__name__ = "Integer32"
_Tv2pWrites_Object = MibScalar
tv2pWrites = _Tv2pWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 9),
    _Tv2pWrites_Type()
)
tv2pWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pWrites.setStatus("current")


class _Tv2pCreates_Type(Integer32):
    """Custom type tv2pCreates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pCreates_Type.__name__ = "Integer32"
_Tv2pCreates_Object = MibScalar
tv2pCreates = _Tv2pCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 10),
    _Tv2pCreates_Type()
)
tv2pCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pCreates.setStatus("current")


class _Tv2pRemoves_Type(Integer32):
    """Custom type tv2pRemoves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pRemoves_Type.__name__ = "Integer32"
_Tv2pRemoves_Object = MibScalar
tv2pRemoves = _Tv2pRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 11),
    _Tv2pRemoves_Type()
)
tv2pRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pRemoves.setStatus("current")


class _Tv2pRenames_Type(Integer32):
    """Custom type tv2pRenames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pRenames_Type.__name__ = "Integer32"
_Tv2pRenames_Object = MibScalar
tv2pRenames = _Tv2pRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 12),
    _Tv2pRenames_Type()
)
tv2pRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pRenames.setStatus("current")


class _Tv2pLinks_Type(Integer32):
    """Custom type tv2pLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pLinks_Type.__name__ = "Integer32"
_Tv2pLinks_Object = MibScalar
tv2pLinks = _Tv2pLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 13),
    _Tv2pLinks_Type()
)
tv2pLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pLinks.setStatus("current")


class _Tv2pSymlinks_Type(Integer32):
    """Custom type tv2pSymlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pSymlinks_Type.__name__ = "Integer32"
_Tv2pSymlinks_Object = MibScalar
tv2pSymlinks = _Tv2pSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 14),
    _Tv2pSymlinks_Type()
)
tv2pSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pSymlinks.setStatus("current")


class _Tv2pMkdirs_Type(Integer32):
    """Custom type tv2pMkdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pMkdirs_Type.__name__ = "Integer32"
_Tv2pMkdirs_Object = MibScalar
tv2pMkdirs = _Tv2pMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 15),
    _Tv2pMkdirs_Type()
)
tv2pMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pMkdirs.setStatus("current")


class _Tv2pRmdirs_Type(Integer32):
    """Custom type tv2pRmdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pRmdirs_Type.__name__ = "Integer32"
_Tv2pRmdirs_Object = MibScalar
tv2pRmdirs = _Tv2pRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 16),
    _Tv2pRmdirs_Type()
)
tv2pRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pRmdirs.setStatus("current")


class _Tv2pReaddirs_Type(Integer32):
    """Custom type tv2pReaddirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pReaddirs_Type.__name__ = "Integer32"
_Tv2pReaddirs_Object = MibScalar
tv2pReaddirs = _Tv2pReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 17),
    _Tv2pReaddirs_Type()
)
tv2pReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pReaddirs.setStatus("current")


class _Tv2pStatfss_Type(Integer32):
    """Custom type tv2pStatfss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2pStatfss_Type.__name__ = "Integer32"
_Tv2pStatfss_Object = MibScalar
tv2pStatfss = _Tv2pStatfss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 2, 18),
    _Tv2pStatfss_Type()
)
tv2pStatfss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2pStatfss.setStatus("current")
_Tv2CachedCalls_ObjectIdentity = ObjectIdentity
tv2CachedCalls = _Tv2CachedCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3)
)
_Tv2ccNulls_Type = Counter32
_Tv2ccNulls_Object = MibScalar
tv2ccNulls = _Tv2ccNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 1),
    _Tv2ccNulls_Type()
)
tv2ccNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccNulls.setStatus("current")
_Tv2ccGetattrs_Type = Counter32
_Tv2ccGetattrs_Object = MibScalar
tv2ccGetattrs = _Tv2ccGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 2),
    _Tv2ccGetattrs_Type()
)
tv2ccGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccGetattrs.setStatus("current")
_Tv2ccSetattrs_Type = Counter32
_Tv2ccSetattrs_Object = MibScalar
tv2ccSetattrs = _Tv2ccSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 3),
    _Tv2ccSetattrs_Type()
)
tv2ccSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccSetattrs.setStatus("current")
_Tv2ccRoots_Type = Counter32
_Tv2ccRoots_Object = MibScalar
tv2ccRoots = _Tv2ccRoots_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 4),
    _Tv2ccRoots_Type()
)
tv2ccRoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccRoots.setStatus("current")
_Tv2ccLookups_Type = Counter32
_Tv2ccLookups_Object = MibScalar
tv2ccLookups = _Tv2ccLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 5),
    _Tv2ccLookups_Type()
)
tv2ccLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccLookups.setStatus("current")
_Tv2ccReadlinks_Type = Counter32
_Tv2ccReadlinks_Object = MibScalar
tv2ccReadlinks = _Tv2ccReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 6),
    _Tv2ccReadlinks_Type()
)
tv2ccReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccReadlinks.setStatus("current")
_Tv2ccReads_Type = Counter32
_Tv2ccReads_Object = MibScalar
tv2ccReads = _Tv2ccReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 7),
    _Tv2ccReads_Type()
)
tv2ccReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccReads.setStatus("current")
_Tv2ccWrcaches_Type = Counter32
_Tv2ccWrcaches_Object = MibScalar
tv2ccWrcaches = _Tv2ccWrcaches_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 8),
    _Tv2ccWrcaches_Type()
)
tv2ccWrcaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccWrcaches.setStatus("current")
_Tv2ccWrites_Type = Counter32
_Tv2ccWrites_Object = MibScalar
tv2ccWrites = _Tv2ccWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 9),
    _Tv2ccWrites_Type()
)
tv2ccWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccWrites.setStatus("current")
_Tv2ccCreates_Type = Counter32
_Tv2ccCreates_Object = MibScalar
tv2ccCreates = _Tv2ccCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 10),
    _Tv2ccCreates_Type()
)
tv2ccCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccCreates.setStatus("current")
_Tv2ccRemoves_Type = Counter32
_Tv2ccRemoves_Object = MibScalar
tv2ccRemoves = _Tv2ccRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 11),
    _Tv2ccRemoves_Type()
)
tv2ccRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccRemoves.setStatus("current")
_Tv2ccRenames_Type = Counter32
_Tv2ccRenames_Object = MibScalar
tv2ccRenames = _Tv2ccRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 12),
    _Tv2ccRenames_Type()
)
tv2ccRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccRenames.setStatus("current")
_Tv2ccLinks_Type = Counter32
_Tv2ccLinks_Object = MibScalar
tv2ccLinks = _Tv2ccLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 13),
    _Tv2ccLinks_Type()
)
tv2ccLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccLinks.setStatus("current")
_Tv2ccSymlinks_Type = Counter32
_Tv2ccSymlinks_Object = MibScalar
tv2ccSymlinks = _Tv2ccSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 14),
    _Tv2ccSymlinks_Type()
)
tv2ccSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccSymlinks.setStatus("current")
_Tv2ccMkdirs_Type = Counter32
_Tv2ccMkdirs_Object = MibScalar
tv2ccMkdirs = _Tv2ccMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 15),
    _Tv2ccMkdirs_Type()
)
tv2ccMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccMkdirs.setStatus("current")
_Tv2ccRmdirs_Type = Counter32
_Tv2ccRmdirs_Object = MibScalar
tv2ccRmdirs = _Tv2ccRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 16),
    _Tv2ccRmdirs_Type()
)
tv2ccRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccRmdirs.setStatus("current")
_Tv2ccReaddirs_Type = Counter32
_Tv2ccReaddirs_Object = MibScalar
tv2ccReaddirs = _Tv2ccReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 17),
    _Tv2ccReaddirs_Type()
)
tv2ccReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccReaddirs.setStatus("current")
_Tv2ccStatfss_Type = Counter32
_Tv2ccStatfss_Object = MibScalar
tv2ccStatfss = _Tv2ccStatfss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 3, 18),
    _Tv2ccStatfss_Type()
)
tv2ccStatfss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2ccStatfss.setStatus("current")
_Tv2CachedPerCent_ObjectIdentity = ObjectIdentity
tv2CachedPerCent = _Tv2CachedPerCent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4)
)


class _Tv2cpNulls_Type(Integer32):
    """Custom type tv2cpNulls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpNulls_Type.__name__ = "Integer32"
_Tv2cpNulls_Object = MibScalar
tv2cpNulls = _Tv2cpNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 1),
    _Tv2cpNulls_Type()
)
tv2cpNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpNulls.setStatus("current")


class _Tv2cpGetattrs_Type(Integer32):
    """Custom type tv2cpGetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpGetattrs_Type.__name__ = "Integer32"
_Tv2cpGetattrs_Object = MibScalar
tv2cpGetattrs = _Tv2cpGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 2),
    _Tv2cpGetattrs_Type()
)
tv2cpGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpGetattrs.setStatus("current")


class _Tv2cpSetattrs_Type(Integer32):
    """Custom type tv2cpSetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpSetattrs_Type.__name__ = "Integer32"
_Tv2cpSetattrs_Object = MibScalar
tv2cpSetattrs = _Tv2cpSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 3),
    _Tv2cpSetattrs_Type()
)
tv2cpSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpSetattrs.setStatus("current")


class _Tv2cpRoots_Type(Integer32):
    """Custom type tv2cpRoots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpRoots_Type.__name__ = "Integer32"
_Tv2cpRoots_Object = MibScalar
tv2cpRoots = _Tv2cpRoots_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 4),
    _Tv2cpRoots_Type()
)
tv2cpRoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpRoots.setStatus("current")


class _Tv2cpLookups_Type(Integer32):
    """Custom type tv2cpLookups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpLookups_Type.__name__ = "Integer32"
_Tv2cpLookups_Object = MibScalar
tv2cpLookups = _Tv2cpLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 5),
    _Tv2cpLookups_Type()
)
tv2cpLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpLookups.setStatus("current")


class _Tv2cpReadlinks_Type(Integer32):
    """Custom type tv2cpReadlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpReadlinks_Type.__name__ = "Integer32"
_Tv2cpReadlinks_Object = MibScalar
tv2cpReadlinks = _Tv2cpReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 6),
    _Tv2cpReadlinks_Type()
)
tv2cpReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpReadlinks.setStatus("current")


class _Tv2cpReads_Type(Integer32):
    """Custom type tv2cpReads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpReads_Type.__name__ = "Integer32"
_Tv2cpReads_Object = MibScalar
tv2cpReads = _Tv2cpReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 7),
    _Tv2cpReads_Type()
)
tv2cpReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpReads.setStatus("current")


class _Tv2cpWrcaches_Type(Integer32):
    """Custom type tv2cpWrcaches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpWrcaches_Type.__name__ = "Integer32"
_Tv2cpWrcaches_Object = MibScalar
tv2cpWrcaches = _Tv2cpWrcaches_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 8),
    _Tv2cpWrcaches_Type()
)
tv2cpWrcaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpWrcaches.setStatus("current")


class _Tv2cpWrites_Type(Integer32):
    """Custom type tv2cpWrites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpWrites_Type.__name__ = "Integer32"
_Tv2cpWrites_Object = MibScalar
tv2cpWrites = _Tv2cpWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 9),
    _Tv2cpWrites_Type()
)
tv2cpWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpWrites.setStatus("current")


class _Tv2cpCreates_Type(Integer32):
    """Custom type tv2cpCreates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpCreates_Type.__name__ = "Integer32"
_Tv2cpCreates_Object = MibScalar
tv2cpCreates = _Tv2cpCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 10),
    _Tv2cpCreates_Type()
)
tv2cpCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpCreates.setStatus("current")


class _Tv2cpRemoves_Type(Integer32):
    """Custom type tv2cpRemoves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpRemoves_Type.__name__ = "Integer32"
_Tv2cpRemoves_Object = MibScalar
tv2cpRemoves = _Tv2cpRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 11),
    _Tv2cpRemoves_Type()
)
tv2cpRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpRemoves.setStatus("current")


class _Tv2cpRenames_Type(Integer32):
    """Custom type tv2cpRenames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpRenames_Type.__name__ = "Integer32"
_Tv2cpRenames_Object = MibScalar
tv2cpRenames = _Tv2cpRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 12),
    _Tv2cpRenames_Type()
)
tv2cpRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpRenames.setStatus("current")


class _Tv2cpLinks_Type(Integer32):
    """Custom type tv2cpLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpLinks_Type.__name__ = "Integer32"
_Tv2cpLinks_Object = MibScalar
tv2cpLinks = _Tv2cpLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 13),
    _Tv2cpLinks_Type()
)
tv2cpLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpLinks.setStatus("current")


class _Tv2cpSymlinks_Type(Integer32):
    """Custom type tv2cpSymlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpSymlinks_Type.__name__ = "Integer32"
_Tv2cpSymlinks_Object = MibScalar
tv2cpSymlinks = _Tv2cpSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 14),
    _Tv2cpSymlinks_Type()
)
tv2cpSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpSymlinks.setStatus("current")


class _Tv2cpMkdirs_Type(Integer32):
    """Custom type tv2cpMkdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpMkdirs_Type.__name__ = "Integer32"
_Tv2cpMkdirs_Object = MibScalar
tv2cpMkdirs = _Tv2cpMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 15),
    _Tv2cpMkdirs_Type()
)
tv2cpMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpMkdirs.setStatus("current")


class _Tv2cpRmdirs_Type(Integer32):
    """Custom type tv2cpRmdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpRmdirs_Type.__name__ = "Integer32"
_Tv2cpRmdirs_Object = MibScalar
tv2cpRmdirs = _Tv2cpRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 16),
    _Tv2cpRmdirs_Type()
)
tv2cpRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpRmdirs.setStatus("current")


class _Tv2cpReaddirs_Type(Integer32):
    """Custom type tv2cpReaddirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpReaddirs_Type.__name__ = "Integer32"
_Tv2cpReaddirs_Object = MibScalar
tv2cpReaddirs = _Tv2cpReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 17),
    _Tv2cpReaddirs_Type()
)
tv2cpReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpReaddirs.setStatus("current")


class _Tv2cpStatfss_Type(Integer32):
    """Custom type tv2cpStatfss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv2cpStatfss_Type.__name__ = "Integer32"
_Tv2cpStatfss_Object = MibScalar
tv2cpStatfss = _Tv2cpStatfss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 3, 4, 18),
    _Tv2cpStatfss_Type()
)
tv2cpStatfss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2cpStatfss.setStatus("current")
_TnfsV3_ObjectIdentity = ObjectIdentity
tnfsV3 = _TnfsV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4)
)
_Tv3Calls_ObjectIdentity = ObjectIdentity
tv3Calls = _Tv3Calls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1)
)
_Tv3cNulls_Type = Counter32
_Tv3cNulls_Object = MibScalar
tv3cNulls = _Tv3cNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 1),
    _Tv3cNulls_Type()
)
tv3cNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cNulls.setStatus("current")
_Tv3cGetattrs_Type = Counter32
_Tv3cGetattrs_Object = MibScalar
tv3cGetattrs = _Tv3cGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 2),
    _Tv3cGetattrs_Type()
)
tv3cGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cGetattrs.setStatus("current")
_Tv3cSetattrs_Type = Counter32
_Tv3cSetattrs_Object = MibScalar
tv3cSetattrs = _Tv3cSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 3),
    _Tv3cSetattrs_Type()
)
tv3cSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cSetattrs.setStatus("current")
_Tv3cLookups_Type = Counter32
_Tv3cLookups_Object = MibScalar
tv3cLookups = _Tv3cLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 4),
    _Tv3cLookups_Type()
)
tv3cLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cLookups.setStatus("current")
_Tv3cAccesss_Type = Counter32
_Tv3cAccesss_Object = MibScalar
tv3cAccesss = _Tv3cAccesss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 5),
    _Tv3cAccesss_Type()
)
tv3cAccesss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cAccesss.setStatus("current")
_Tv3cReadlinks_Type = Counter32
_Tv3cReadlinks_Object = MibScalar
tv3cReadlinks = _Tv3cReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 6),
    _Tv3cReadlinks_Type()
)
tv3cReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cReadlinks.setStatus("current")
_Tv3cReads_Type = Counter32
_Tv3cReads_Object = MibScalar
tv3cReads = _Tv3cReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 7),
    _Tv3cReads_Type()
)
tv3cReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cReads.setStatus("current")
_Tv3cWrites_Type = Counter32
_Tv3cWrites_Object = MibScalar
tv3cWrites = _Tv3cWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 8),
    _Tv3cWrites_Type()
)
tv3cWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cWrites.setStatus("current")
_Tv3cCreates_Type = Counter32
_Tv3cCreates_Object = MibScalar
tv3cCreates = _Tv3cCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 9),
    _Tv3cCreates_Type()
)
tv3cCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cCreates.setStatus("current")
_Tv3cMkdirs_Type = Counter32
_Tv3cMkdirs_Object = MibScalar
tv3cMkdirs = _Tv3cMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 10),
    _Tv3cMkdirs_Type()
)
tv3cMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cMkdirs.setStatus("current")
_Tv3cSymlinks_Type = Counter32
_Tv3cSymlinks_Object = MibScalar
tv3cSymlinks = _Tv3cSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 11),
    _Tv3cSymlinks_Type()
)
tv3cSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cSymlinks.setStatus("current")
_Tv3cMknods_Type = Counter32
_Tv3cMknods_Object = MibScalar
tv3cMknods = _Tv3cMknods_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 12),
    _Tv3cMknods_Type()
)
tv3cMknods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cMknods.setStatus("current")
_Tv3cRemoves_Type = Counter32
_Tv3cRemoves_Object = MibScalar
tv3cRemoves = _Tv3cRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 13),
    _Tv3cRemoves_Type()
)
tv3cRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cRemoves.setStatus("current")
_Tv3cRmdirs_Type = Counter32
_Tv3cRmdirs_Object = MibScalar
tv3cRmdirs = _Tv3cRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 14),
    _Tv3cRmdirs_Type()
)
tv3cRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cRmdirs.setStatus("current")
_Tv3cRenames_Type = Counter32
_Tv3cRenames_Object = MibScalar
tv3cRenames = _Tv3cRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 15),
    _Tv3cRenames_Type()
)
tv3cRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cRenames.setStatus("current")
_Tv3cLinks_Type = Counter32
_Tv3cLinks_Object = MibScalar
tv3cLinks = _Tv3cLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 16),
    _Tv3cLinks_Type()
)
tv3cLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cLinks.setStatus("current")
_Tv3cReaddirs_Type = Counter32
_Tv3cReaddirs_Object = MibScalar
tv3cReaddirs = _Tv3cReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 17),
    _Tv3cReaddirs_Type()
)
tv3cReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cReaddirs.setStatus("current")
_Tv3cReaddirPluss_Type = Counter32
_Tv3cReaddirPluss_Object = MibScalar
tv3cReaddirPluss = _Tv3cReaddirPluss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 18),
    _Tv3cReaddirPluss_Type()
)
tv3cReaddirPluss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cReaddirPluss.setStatus("current")
_Tv3cFsstats_Type = Counter32
_Tv3cFsstats_Object = MibScalar
tv3cFsstats = _Tv3cFsstats_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 19),
    _Tv3cFsstats_Type()
)
tv3cFsstats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cFsstats.setStatus("current")
_Tv3cFsinfos_Type = Counter32
_Tv3cFsinfos_Object = MibScalar
tv3cFsinfos = _Tv3cFsinfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 20),
    _Tv3cFsinfos_Type()
)
tv3cFsinfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cFsinfos.setStatus("current")
_Tv3cPathconfs_Type = Counter32
_Tv3cPathconfs_Object = MibScalar
tv3cPathconfs = _Tv3cPathconfs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 21),
    _Tv3cPathconfs_Type()
)
tv3cPathconfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cPathconfs.setStatus("current")
_Tv3cCommits_Type = Counter32
_Tv3cCommits_Object = MibScalar
tv3cCommits = _Tv3cCommits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 1, 22),
    _Tv3cCommits_Type()
)
tv3cCommits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cCommits.setStatus("current")
_Tv3Percent_ObjectIdentity = ObjectIdentity
tv3Percent = _Tv3Percent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2)
)


class _Tv3pNulls_Type(Integer32):
    """Custom type tv3pNulls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pNulls_Type.__name__ = "Integer32"
_Tv3pNulls_Object = MibScalar
tv3pNulls = _Tv3pNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 1),
    _Tv3pNulls_Type()
)
tv3pNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pNulls.setStatus("current")


class _Tv3pGetattrs_Type(Integer32):
    """Custom type tv3pGetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pGetattrs_Type.__name__ = "Integer32"
_Tv3pGetattrs_Object = MibScalar
tv3pGetattrs = _Tv3pGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 2),
    _Tv3pGetattrs_Type()
)
tv3pGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pGetattrs.setStatus("current")


class _Tv3pSetattrs_Type(Integer32):
    """Custom type tv3pSetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pSetattrs_Type.__name__ = "Integer32"
_Tv3pSetattrs_Object = MibScalar
tv3pSetattrs = _Tv3pSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 3),
    _Tv3pSetattrs_Type()
)
tv3pSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pSetattrs.setStatus("current")


class _Tv3pLookups_Type(Integer32):
    """Custom type tv3pLookups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pLookups_Type.__name__ = "Integer32"
_Tv3pLookups_Object = MibScalar
tv3pLookups = _Tv3pLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 4),
    _Tv3pLookups_Type()
)
tv3pLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pLookups.setStatus("current")


class _Tv3pAccesss_Type(Integer32):
    """Custom type tv3pAccesss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pAccesss_Type.__name__ = "Integer32"
_Tv3pAccesss_Object = MibScalar
tv3pAccesss = _Tv3pAccesss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 5),
    _Tv3pAccesss_Type()
)
tv3pAccesss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pAccesss.setStatus("current")


class _Tv3pReadlinks_Type(Integer32):
    """Custom type tv3pReadlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pReadlinks_Type.__name__ = "Integer32"
_Tv3pReadlinks_Object = MibScalar
tv3pReadlinks = _Tv3pReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 6),
    _Tv3pReadlinks_Type()
)
tv3pReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pReadlinks.setStatus("current")


class _Tv3pReads_Type(Integer32):
    """Custom type tv3pReads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pReads_Type.__name__ = "Integer32"
_Tv3pReads_Object = MibScalar
tv3pReads = _Tv3pReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 7),
    _Tv3pReads_Type()
)
tv3pReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pReads.setStatus("current")


class _Tv3pWrites_Type(Integer32):
    """Custom type tv3pWrites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pWrites_Type.__name__ = "Integer32"
_Tv3pWrites_Object = MibScalar
tv3pWrites = _Tv3pWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 8),
    _Tv3pWrites_Type()
)
tv3pWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pWrites.setStatus("current")


class _Tv3pCreates_Type(Integer32):
    """Custom type tv3pCreates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pCreates_Type.__name__ = "Integer32"
_Tv3pCreates_Object = MibScalar
tv3pCreates = _Tv3pCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 9),
    _Tv3pCreates_Type()
)
tv3pCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pCreates.setStatus("current")


class _Tv3pMkdirs_Type(Integer32):
    """Custom type tv3pMkdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pMkdirs_Type.__name__ = "Integer32"
_Tv3pMkdirs_Object = MibScalar
tv3pMkdirs = _Tv3pMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 10),
    _Tv3pMkdirs_Type()
)
tv3pMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pMkdirs.setStatus("current")


class _Tv3pSymlinks_Type(Integer32):
    """Custom type tv3pSymlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pSymlinks_Type.__name__ = "Integer32"
_Tv3pSymlinks_Object = MibScalar
tv3pSymlinks = _Tv3pSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 11),
    _Tv3pSymlinks_Type()
)
tv3pSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pSymlinks.setStatus("current")


class _Tv3pMknods_Type(Integer32):
    """Custom type tv3pMknods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pMknods_Type.__name__ = "Integer32"
_Tv3pMknods_Object = MibScalar
tv3pMknods = _Tv3pMknods_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 12),
    _Tv3pMknods_Type()
)
tv3pMknods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pMknods.setStatus("current")


class _Tv3pRemoves_Type(Integer32):
    """Custom type tv3pRemoves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pRemoves_Type.__name__ = "Integer32"
_Tv3pRemoves_Object = MibScalar
tv3pRemoves = _Tv3pRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 13),
    _Tv3pRemoves_Type()
)
tv3pRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pRemoves.setStatus("current")


class _Tv3pRmdirs_Type(Integer32):
    """Custom type tv3pRmdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pRmdirs_Type.__name__ = "Integer32"
_Tv3pRmdirs_Object = MibScalar
tv3pRmdirs = _Tv3pRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 14),
    _Tv3pRmdirs_Type()
)
tv3pRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pRmdirs.setStatus("current")


class _Tv3pRenames_Type(Integer32):
    """Custom type tv3pRenames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pRenames_Type.__name__ = "Integer32"
_Tv3pRenames_Object = MibScalar
tv3pRenames = _Tv3pRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 15),
    _Tv3pRenames_Type()
)
tv3pRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pRenames.setStatus("current")


class _Tv3pLinks_Type(Integer32):
    """Custom type tv3pLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pLinks_Type.__name__ = "Integer32"
_Tv3pLinks_Object = MibScalar
tv3pLinks = _Tv3pLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 16),
    _Tv3pLinks_Type()
)
tv3pLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pLinks.setStatus("current")


class _Tv3pReaddirs_Type(Integer32):
    """Custom type tv3pReaddirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pReaddirs_Type.__name__ = "Integer32"
_Tv3pReaddirs_Object = MibScalar
tv3pReaddirs = _Tv3pReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 17),
    _Tv3pReaddirs_Type()
)
tv3pReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pReaddirs.setStatus("current")


class _Tv3pReaddirPluss_Type(Integer32):
    """Custom type tv3pReaddirPluss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pReaddirPluss_Type.__name__ = "Integer32"
_Tv3pReaddirPluss_Object = MibScalar
tv3pReaddirPluss = _Tv3pReaddirPluss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 18),
    _Tv3pReaddirPluss_Type()
)
tv3pReaddirPluss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pReaddirPluss.setStatus("current")


class _Tv3pFsstats_Type(Integer32):
    """Custom type tv3pFsstats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pFsstats_Type.__name__ = "Integer32"
_Tv3pFsstats_Object = MibScalar
tv3pFsstats = _Tv3pFsstats_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 19),
    _Tv3pFsstats_Type()
)
tv3pFsstats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pFsstats.setStatus("current")


class _Tv3pFsinfos_Type(Integer32):
    """Custom type tv3pFsinfos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pFsinfos_Type.__name__ = "Integer32"
_Tv3pFsinfos_Object = MibScalar
tv3pFsinfos = _Tv3pFsinfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 20),
    _Tv3pFsinfos_Type()
)
tv3pFsinfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pFsinfos.setStatus("current")


class _Tv3pPathconfs_Type(Integer32):
    """Custom type tv3pPathconfs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pPathconfs_Type.__name__ = "Integer32"
_Tv3pPathconfs_Object = MibScalar
tv3pPathconfs = _Tv3pPathconfs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 21),
    _Tv3pPathconfs_Type()
)
tv3pPathconfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pPathconfs.setStatus("current")


class _Tv3pCommits_Type(Integer32):
    """Custom type tv3pCommits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3pCommits_Type.__name__ = "Integer32"
_Tv3pCommits_Object = MibScalar
tv3pCommits = _Tv3pCommits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 2, 22),
    _Tv3pCommits_Type()
)
tv3pCommits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3pCommits.setStatus("current")
_Tv3CachedCalls_ObjectIdentity = ObjectIdentity
tv3CachedCalls = _Tv3CachedCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3)
)
_Tv3ccNulls_Type = Counter32
_Tv3ccNulls_Object = MibScalar
tv3ccNulls = _Tv3ccNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 1),
    _Tv3ccNulls_Type()
)
tv3ccNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccNulls.setStatus("current")
_Tv3ccGetattrs_Type = Counter32
_Tv3ccGetattrs_Object = MibScalar
tv3ccGetattrs = _Tv3ccGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 2),
    _Tv3ccGetattrs_Type()
)
tv3ccGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccGetattrs.setStatus("current")
_Tv3ccSetattrs_Type = Counter32
_Tv3ccSetattrs_Object = MibScalar
tv3ccSetattrs = _Tv3ccSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 3),
    _Tv3ccSetattrs_Type()
)
tv3ccSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccSetattrs.setStatus("current")
_Tv3ccLookups_Type = Counter32
_Tv3ccLookups_Object = MibScalar
tv3ccLookups = _Tv3ccLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 4),
    _Tv3ccLookups_Type()
)
tv3ccLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccLookups.setStatus("current")
_Tv3ccAccesss_Type = Counter32
_Tv3ccAccesss_Object = MibScalar
tv3ccAccesss = _Tv3ccAccesss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 5),
    _Tv3ccAccesss_Type()
)
tv3ccAccesss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccAccesss.setStatus("current")
_Tv3ccReadlinks_Type = Counter32
_Tv3ccReadlinks_Object = MibScalar
tv3ccReadlinks = _Tv3ccReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 6),
    _Tv3ccReadlinks_Type()
)
tv3ccReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccReadlinks.setStatus("current")
_Tv3ccReads_Type = Counter32
_Tv3ccReads_Object = MibScalar
tv3ccReads = _Tv3ccReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 7),
    _Tv3ccReads_Type()
)
tv3ccReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccReads.setStatus("current")
_Tv3ccWrites_Type = Counter32
_Tv3ccWrites_Object = MibScalar
tv3ccWrites = _Tv3ccWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 8),
    _Tv3ccWrites_Type()
)
tv3ccWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccWrites.setStatus("current")
_Tv3ccCreates_Type = Counter32
_Tv3ccCreates_Object = MibScalar
tv3ccCreates = _Tv3ccCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 9),
    _Tv3ccCreates_Type()
)
tv3ccCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccCreates.setStatus("current")
_Tv3ccMkdirs_Type = Counter32
_Tv3ccMkdirs_Object = MibScalar
tv3ccMkdirs = _Tv3ccMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 10),
    _Tv3ccMkdirs_Type()
)
tv3ccMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccMkdirs.setStatus("current")
_Tv3ccSymlinks_Type = Counter32
_Tv3ccSymlinks_Object = MibScalar
tv3ccSymlinks = _Tv3ccSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 11),
    _Tv3ccSymlinks_Type()
)
tv3ccSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccSymlinks.setStatus("current")
_Tv3ccMknods_Type = Counter32
_Tv3ccMknods_Object = MibScalar
tv3ccMknods = _Tv3ccMknods_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 12),
    _Tv3ccMknods_Type()
)
tv3ccMknods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccMknods.setStatus("current")
_Tv3ccRemoves_Type = Counter32
_Tv3ccRemoves_Object = MibScalar
tv3ccRemoves = _Tv3ccRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 13),
    _Tv3ccRemoves_Type()
)
tv3ccRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccRemoves.setStatus("current")
_Tv3ccRmdirs_Type = Counter32
_Tv3ccRmdirs_Object = MibScalar
tv3ccRmdirs = _Tv3ccRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 14),
    _Tv3ccRmdirs_Type()
)
tv3ccRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccRmdirs.setStatus("current")
_Tv3ccRenames_Type = Counter32
_Tv3ccRenames_Object = MibScalar
tv3ccRenames = _Tv3ccRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 15),
    _Tv3ccRenames_Type()
)
tv3ccRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccRenames.setStatus("current")
_Tv3ccLinks_Type = Counter32
_Tv3ccLinks_Object = MibScalar
tv3ccLinks = _Tv3ccLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 16),
    _Tv3ccLinks_Type()
)
tv3ccLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccLinks.setStatus("current")
_Tv3ccReaddirs_Type = Counter32
_Tv3ccReaddirs_Object = MibScalar
tv3ccReaddirs = _Tv3ccReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 17),
    _Tv3ccReaddirs_Type()
)
tv3ccReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccReaddirs.setStatus("current")
_Tv3ccReaddirPluss_Type = Counter32
_Tv3ccReaddirPluss_Object = MibScalar
tv3ccReaddirPluss = _Tv3ccReaddirPluss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 18),
    _Tv3ccReaddirPluss_Type()
)
tv3ccReaddirPluss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccReaddirPluss.setStatus("current")
_Tv3ccFsstats_Type = Counter32
_Tv3ccFsstats_Object = MibScalar
tv3ccFsstats = _Tv3ccFsstats_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 19),
    _Tv3ccFsstats_Type()
)
tv3ccFsstats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccFsstats.setStatus("current")
_Tv3ccFsinfos_Type = Counter32
_Tv3ccFsinfos_Object = MibScalar
tv3ccFsinfos = _Tv3ccFsinfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 20),
    _Tv3ccFsinfos_Type()
)
tv3ccFsinfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccFsinfos.setStatus("current")
_Tv3ccPathconfs_Type = Counter32
_Tv3ccPathconfs_Object = MibScalar
tv3ccPathconfs = _Tv3ccPathconfs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 21),
    _Tv3ccPathconfs_Type()
)
tv3ccPathconfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccPathconfs.setStatus("current")
_Tv3ccCommits_Type = Counter32
_Tv3ccCommits_Object = MibScalar
tv3ccCommits = _Tv3ccCommits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 3, 22),
    _Tv3ccCommits_Type()
)
tv3ccCommits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3ccCommits.setStatus("current")
_Tv3CachedPerCent_ObjectIdentity = ObjectIdentity
tv3CachedPerCent = _Tv3CachedPerCent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4)
)


class _Tv3cpNulls_Type(Integer32):
    """Custom type tv3cpNulls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpNulls_Type.__name__ = "Integer32"
_Tv3cpNulls_Object = MibScalar
tv3cpNulls = _Tv3cpNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 1),
    _Tv3cpNulls_Type()
)
tv3cpNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpNulls.setStatus("current")


class _Tv3cpGetattrs_Type(Integer32):
    """Custom type tv3cpGetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpGetattrs_Type.__name__ = "Integer32"
_Tv3cpGetattrs_Object = MibScalar
tv3cpGetattrs = _Tv3cpGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 2),
    _Tv3cpGetattrs_Type()
)
tv3cpGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpGetattrs.setStatus("current")


class _Tv3cpSetattrs_Type(Integer32):
    """Custom type tv3cpSetattrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpSetattrs_Type.__name__ = "Integer32"
_Tv3cpSetattrs_Object = MibScalar
tv3cpSetattrs = _Tv3cpSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 3),
    _Tv3cpSetattrs_Type()
)
tv3cpSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpSetattrs.setStatus("current")


class _Tv3cpLookups_Type(Integer32):
    """Custom type tv3cpLookups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpLookups_Type.__name__ = "Integer32"
_Tv3cpLookups_Object = MibScalar
tv3cpLookups = _Tv3cpLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 4),
    _Tv3cpLookups_Type()
)
tv3cpLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpLookups.setStatus("current")


class _Tv3cpAccesss_Type(Integer32):
    """Custom type tv3cpAccesss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpAccesss_Type.__name__ = "Integer32"
_Tv3cpAccesss_Object = MibScalar
tv3cpAccesss = _Tv3cpAccesss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 5),
    _Tv3cpAccesss_Type()
)
tv3cpAccesss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpAccesss.setStatus("current")


class _Tv3cpReadlinks_Type(Integer32):
    """Custom type tv3cpReadlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpReadlinks_Type.__name__ = "Integer32"
_Tv3cpReadlinks_Object = MibScalar
tv3cpReadlinks = _Tv3cpReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 6),
    _Tv3cpReadlinks_Type()
)
tv3cpReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpReadlinks.setStatus("current")


class _Tv3cpReads_Type(Integer32):
    """Custom type tv3cpReads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpReads_Type.__name__ = "Integer32"
_Tv3cpReads_Object = MibScalar
tv3cpReads = _Tv3cpReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 7),
    _Tv3cpReads_Type()
)
tv3cpReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpReads.setStatus("current")


class _Tv3cpWrites_Type(Integer32):
    """Custom type tv3cpWrites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpWrites_Type.__name__ = "Integer32"
_Tv3cpWrites_Object = MibScalar
tv3cpWrites = _Tv3cpWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 8),
    _Tv3cpWrites_Type()
)
tv3cpWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpWrites.setStatus("current")


class _Tv3cpCreates_Type(Integer32):
    """Custom type tv3cpCreates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpCreates_Type.__name__ = "Integer32"
_Tv3cpCreates_Object = MibScalar
tv3cpCreates = _Tv3cpCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 9),
    _Tv3cpCreates_Type()
)
tv3cpCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpCreates.setStatus("current")


class _Tv3cpMkdirs_Type(Integer32):
    """Custom type tv3cpMkdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpMkdirs_Type.__name__ = "Integer32"
_Tv3cpMkdirs_Object = MibScalar
tv3cpMkdirs = _Tv3cpMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 10),
    _Tv3cpMkdirs_Type()
)
tv3cpMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpMkdirs.setStatus("current")


class _Tv3cpSymlinks_Type(Integer32):
    """Custom type tv3cpSymlinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpSymlinks_Type.__name__ = "Integer32"
_Tv3cpSymlinks_Object = MibScalar
tv3cpSymlinks = _Tv3cpSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 11),
    _Tv3cpSymlinks_Type()
)
tv3cpSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpSymlinks.setStatus("current")


class _Tv3cpMknods_Type(Integer32):
    """Custom type tv3cpMknods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpMknods_Type.__name__ = "Integer32"
_Tv3cpMknods_Object = MibScalar
tv3cpMknods = _Tv3cpMknods_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 12),
    _Tv3cpMknods_Type()
)
tv3cpMknods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpMknods.setStatus("current")


class _Tv3cpRemoves_Type(Integer32):
    """Custom type tv3cpRemoves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpRemoves_Type.__name__ = "Integer32"
_Tv3cpRemoves_Object = MibScalar
tv3cpRemoves = _Tv3cpRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 13),
    _Tv3cpRemoves_Type()
)
tv3cpRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpRemoves.setStatus("current")


class _Tv3cpRmdirs_Type(Integer32):
    """Custom type tv3cpRmdirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpRmdirs_Type.__name__ = "Integer32"
_Tv3cpRmdirs_Object = MibScalar
tv3cpRmdirs = _Tv3cpRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 14),
    _Tv3cpRmdirs_Type()
)
tv3cpRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpRmdirs.setStatus("current")


class _Tv3cpRenames_Type(Integer32):
    """Custom type tv3cpRenames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpRenames_Type.__name__ = "Integer32"
_Tv3cpRenames_Object = MibScalar
tv3cpRenames = _Tv3cpRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 15),
    _Tv3cpRenames_Type()
)
tv3cpRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpRenames.setStatus("current")


class _Tv3cpLinks_Type(Integer32):
    """Custom type tv3cpLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpLinks_Type.__name__ = "Integer32"
_Tv3cpLinks_Object = MibScalar
tv3cpLinks = _Tv3cpLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 16),
    _Tv3cpLinks_Type()
)
tv3cpLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpLinks.setStatus("current")


class _Tv3cpReaddirs_Type(Integer32):
    """Custom type tv3cpReaddirs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpReaddirs_Type.__name__ = "Integer32"
_Tv3cpReaddirs_Object = MibScalar
tv3cpReaddirs = _Tv3cpReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 17),
    _Tv3cpReaddirs_Type()
)
tv3cpReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpReaddirs.setStatus("current")


class _Tv3cpReaddirPluss_Type(Integer32):
    """Custom type tv3cpReaddirPluss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpReaddirPluss_Type.__name__ = "Integer32"
_Tv3cpReaddirPluss_Object = MibScalar
tv3cpReaddirPluss = _Tv3cpReaddirPluss_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 18),
    _Tv3cpReaddirPluss_Type()
)
tv3cpReaddirPluss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpReaddirPluss.setStatus("current")


class _Tv3cpFsstats_Type(Integer32):
    """Custom type tv3cpFsstats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpFsstats_Type.__name__ = "Integer32"
_Tv3cpFsstats_Object = MibScalar
tv3cpFsstats = _Tv3cpFsstats_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 19),
    _Tv3cpFsstats_Type()
)
tv3cpFsstats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpFsstats.setStatus("current")


class _Tv3cpFsinfos_Type(Integer32):
    """Custom type tv3cpFsinfos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpFsinfos_Type.__name__ = "Integer32"
_Tv3cpFsinfos_Object = MibScalar
tv3cpFsinfos = _Tv3cpFsinfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 20),
    _Tv3cpFsinfos_Type()
)
tv3cpFsinfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpFsinfos.setStatus("current")


class _Tv3cpPathconfs_Type(Integer32):
    """Custom type tv3cpPathconfs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpPathconfs_Type.__name__ = "Integer32"
_Tv3cpPathconfs_Object = MibScalar
tv3cpPathconfs = _Tv3cpPathconfs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 21),
    _Tv3cpPathconfs_Type()
)
tv3cpPathconfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpPathconfs.setStatus("current")


class _Tv3cpCommits_Type(Integer32):
    """Custom type tv3cpCommits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Tv3cpCommits_Type.__name__ = "Integer32"
_Tv3cpCommits_Object = MibScalar
tv3cpCommits = _Tv3cpCommits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 4, 4, 22),
    _Tv3cpCommits_Type()
)
tv3cpCommits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3cpCommits.setStatus("current")
_TreplyCache_ObjectIdentity = ObjectIdentity
treplyCache = _TreplyCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5)
)
_TrcInProgressHits_Type = Counter32
_TrcInProgressHits_Object = MibScalar
trcInProgressHits = _TrcInProgressHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 1),
    _TrcInProgressHits_Type()
)
trcInProgressHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcInProgressHits.setStatus("current")
_TrcDelayHits_Type = Counter32
_TrcDelayHits_Object = MibScalar
trcDelayHits = _TrcDelayHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 2),
    _TrcDelayHits_Type()
)
trcDelayHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcDelayHits.setStatus("deprecated")
_TrcMisses_Type = Counter32
_TrcMisses_Object = MibScalar
trcMisses = _TrcMisses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 3),
    _TrcMisses_Type()
)
trcMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcMisses.setStatus("current")
_TrcNonIdemDoneHits_Type = Counter32
_TrcNonIdemDoneHits_Object = MibScalar
trcNonIdemDoneHits = _TrcNonIdemDoneHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 4),
    _TrcNonIdemDoneHits_Type()
)
trcNonIdemDoneHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcNonIdemDoneHits.setStatus("current")
_TrcNonIdemNotDoneHits_Type = Counter32
_TrcNonIdemNotDoneHits_Object = MibScalar
trcNonIdemNotDoneHits = _TrcNonIdemNotDoneHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 5),
    _TrcNonIdemNotDoneHits_Type()
)
trcNonIdemNotDoneHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcNonIdemNotDoneHits.setStatus("current")
_TrcTcpInProgressHits_Type = Counter32
_TrcTcpInProgressHits_Object = MibScalar
trcTcpInProgressHits = _TrcTcpInProgressHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 6),
    _TrcTcpInProgressHits_Type()
)
trcTcpInProgressHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcTcpInProgressHits.setStatus("current")
_TrcTcpDelayHits_Type = Counter32
_TrcTcpDelayHits_Object = MibScalar
trcTcpDelayHits = _TrcTcpDelayHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 7),
    _TrcTcpDelayHits_Type()
)
trcTcpDelayHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcTcpDelayHits.setStatus("deprecated")
_TrcTcpMisses_Type = Counter32
_TrcTcpMisses_Object = MibScalar
trcTcpMisses = _TrcTcpMisses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 8),
    _TrcTcpMisses_Type()
)
trcTcpMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcTcpMisses.setStatus("current")
_TrcTcpNonIdemDoneHits_Type = Counter32
_TrcTcpNonIdemDoneHits_Object = MibScalar
trcTcpNonIdemDoneHits = _TrcTcpNonIdemDoneHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 9),
    _TrcTcpNonIdemDoneHits_Type()
)
trcTcpNonIdemDoneHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcTcpNonIdemDoneHits.setStatus("current")
_TrcTcpNonIdemNotDoneHits_Type = Counter32
_TrcTcpNonIdemNotDoneHits_Object = MibScalar
trcTcpNonIdemNotDoneHits = _TrcTcpNonIdemNotDoneHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 10),
    _TrcTcpNonIdemNotDoneHits_Type()
)
trcTcpNonIdemNotDoneHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcTcpNonIdemNotDoneHits.setStatus("current")
_TrcUdpInProgressHits_Type = Counter32
_TrcUdpInProgressHits_Object = MibScalar
trcUdpInProgressHits = _TrcUdpInProgressHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 11),
    _TrcUdpInProgressHits_Type()
)
trcUdpInProgressHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcUdpInProgressHits.setStatus("current")
_TrcUdpDelayHits_Type = Counter32
_TrcUdpDelayHits_Object = MibScalar
trcUdpDelayHits = _TrcUdpDelayHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 12),
    _TrcUdpDelayHits_Type()
)
trcUdpDelayHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcUdpDelayHits.setStatus("deprecated")
_TrcUdpMisses_Type = Counter32
_TrcUdpMisses_Object = MibScalar
trcUdpMisses = _TrcUdpMisses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 13),
    _TrcUdpMisses_Type()
)
trcUdpMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcUdpMisses.setStatus("current")
_TrcUdpNonIdemDoneHits_Type = Counter32
_TrcUdpNonIdemDoneHits_Object = MibScalar
trcUdpNonIdemDoneHits = _TrcUdpNonIdemDoneHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 14),
    _TrcUdpNonIdemDoneHits_Type()
)
trcUdpNonIdemDoneHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcUdpNonIdemDoneHits.setStatus("current")
_TrcUdpNonIdemNotDoneHits_Type = Counter32
_TrcUdpNonIdemNotDoneHits_Object = MibScalar
trcUdpNonIdemNotDoneHits = _TrcUdpNonIdemNotDoneHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 5, 15),
    _TrcUdpNonIdemNotDoneHits_Type()
)
trcUdpNonIdemNotDoneHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcUdpNonIdemNotDoneHits.setStatus("current")
_TnfsrwStats_ObjectIdentity = ObjectIdentity
tnfsrwStats = _TnfsrwStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6)
)
_Tv2ReadStats_ObjectIdentity = ObjectIdentity
tv2ReadStats = _Tv2ReadStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 1)
)
_Tv2Read512Calls_Type = Counter32
_Tv2Read512Calls_Object = MibScalar
tv2Read512Calls = _Tv2Read512Calls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 1, 1),
    _Tv2Read512Calls_Type()
)
tv2Read512Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Read512Calls.setStatus("current")
_Tv2Read1KCalls_Type = Counter32
_Tv2Read1KCalls_Object = MibScalar
tv2Read1KCalls = _Tv2Read1KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 1, 2),
    _Tv2Read1KCalls_Type()
)
tv2Read1KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Read1KCalls.setStatus("current")
_Tv2Read2KCalls_Type = Counter32
_Tv2Read2KCalls_Object = MibScalar
tv2Read2KCalls = _Tv2Read2KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 1, 3),
    _Tv2Read2KCalls_Type()
)
tv2Read2KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Read2KCalls.setStatus("current")
_Tv2Read4KCalls_Type = Counter32
_Tv2Read4KCalls_Object = MibScalar
tv2Read4KCalls = _Tv2Read4KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 1, 4),
    _Tv2Read4KCalls_Type()
)
tv2Read4KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Read4KCalls.setStatus("current")
_Tv2Read8KCalls_Type = Counter32
_Tv2Read8KCalls_Object = MibScalar
tv2Read8KCalls = _Tv2Read8KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 1, 5),
    _Tv2Read8KCalls_Type()
)
tv2Read8KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Read8KCalls.setStatus("current")
_Tv2Read16KCalls_Type = Counter32
_Tv2Read16KCalls_Object = MibScalar
tv2Read16KCalls = _Tv2Read16KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 1, 6),
    _Tv2Read16KCalls_Type()
)
tv2Read16KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Read16KCalls.setStatus("current")
_Tv2Read32KCalls_Type = Counter32
_Tv2Read32KCalls_Object = MibScalar
tv2Read32KCalls = _Tv2Read32KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 1, 7),
    _Tv2Read32KCalls_Type()
)
tv2Read32KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Read32KCalls.setStatus("current")
_Tv2Read64KCalls_Type = Counter32
_Tv2Read64KCalls_Object = MibScalar
tv2Read64KCalls = _Tv2Read64KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 1, 8),
    _Tv2Read64KCalls_Type()
)
tv2Read64KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Read64KCalls.setStatus("current")
_Tv2Read128KCalls_Type = Counter32
_Tv2Read128KCalls_Object = MibScalar
tv2Read128KCalls = _Tv2Read128KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 1, 9),
    _Tv2Read128KCalls_Type()
)
tv2Read128KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Read128KCalls.setStatus("current")
_Tv2WriteStats_ObjectIdentity = ObjectIdentity
tv2WriteStats = _Tv2WriteStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 2)
)
_Tv2Write512Calls_Type = Counter32
_Tv2Write512Calls_Object = MibScalar
tv2Write512Calls = _Tv2Write512Calls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 2, 1),
    _Tv2Write512Calls_Type()
)
tv2Write512Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Write512Calls.setStatus("current")
_Tv2Write1KCalls_Type = Counter32
_Tv2Write1KCalls_Object = MibScalar
tv2Write1KCalls = _Tv2Write1KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 2, 2),
    _Tv2Write1KCalls_Type()
)
tv2Write1KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Write1KCalls.setStatus("current")
_Tv2Write2KCalls_Type = Counter32
_Tv2Write2KCalls_Object = MibScalar
tv2Write2KCalls = _Tv2Write2KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 2, 3),
    _Tv2Write2KCalls_Type()
)
tv2Write2KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Write2KCalls.setStatus("current")
_Tv2Write4KCalls_Type = Counter32
_Tv2Write4KCalls_Object = MibScalar
tv2Write4KCalls = _Tv2Write4KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 2, 4),
    _Tv2Write4KCalls_Type()
)
tv2Write4KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Write4KCalls.setStatus("current")
_Tv2Write8KCalls_Type = Counter32
_Tv2Write8KCalls_Object = MibScalar
tv2Write8KCalls = _Tv2Write8KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 2, 5),
    _Tv2Write8KCalls_Type()
)
tv2Write8KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Write8KCalls.setStatus("current")
_Tv2Write16KCalls_Type = Counter32
_Tv2Write16KCalls_Object = MibScalar
tv2Write16KCalls = _Tv2Write16KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 2, 6),
    _Tv2Write16KCalls_Type()
)
tv2Write16KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Write16KCalls.setStatus("current")
_Tv2Write32KCalls_Type = Counter32
_Tv2Write32KCalls_Object = MibScalar
tv2Write32KCalls = _Tv2Write32KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 2, 7),
    _Tv2Write32KCalls_Type()
)
tv2Write32KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Write32KCalls.setStatus("current")
_Tv2Write64KCalls_Type = Counter32
_Tv2Write64KCalls_Object = MibScalar
tv2Write64KCalls = _Tv2Write64KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 2, 8),
    _Tv2Write64KCalls_Type()
)
tv2Write64KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Write64KCalls.setStatus("current")
_Tv2Write128KCalls_Type = Counter32
_Tv2Write128KCalls_Object = MibScalar
tv2Write128KCalls = _Tv2Write128KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 2, 9),
    _Tv2Write128KCalls_Type()
)
tv2Write128KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv2Write128KCalls.setStatus("current")
_Tv3ReadStats_ObjectIdentity = ObjectIdentity
tv3ReadStats = _Tv3ReadStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 3)
)
_Tv3Read512Calls_Type = Counter32
_Tv3Read512Calls_Object = MibScalar
tv3Read512Calls = _Tv3Read512Calls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 3, 1),
    _Tv3Read512Calls_Type()
)
tv3Read512Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Read512Calls.setStatus("current")
_Tv3Read1KCalls_Type = Counter32
_Tv3Read1KCalls_Object = MibScalar
tv3Read1KCalls = _Tv3Read1KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 3, 2),
    _Tv3Read1KCalls_Type()
)
tv3Read1KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Read1KCalls.setStatus("current")
_Tv3Read2KCalls_Type = Counter32
_Tv3Read2KCalls_Object = MibScalar
tv3Read2KCalls = _Tv3Read2KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 3, 3),
    _Tv3Read2KCalls_Type()
)
tv3Read2KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Read2KCalls.setStatus("current")
_Tv3Read4KCalls_Type = Counter32
_Tv3Read4KCalls_Object = MibScalar
tv3Read4KCalls = _Tv3Read4KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 3, 4),
    _Tv3Read4KCalls_Type()
)
tv3Read4KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Read4KCalls.setStatus("current")
_Tv3Read8KCalls_Type = Counter32
_Tv3Read8KCalls_Object = MibScalar
tv3Read8KCalls = _Tv3Read8KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 3, 5),
    _Tv3Read8KCalls_Type()
)
tv3Read8KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Read8KCalls.setStatus("current")
_Tv3Read16KCalls_Type = Counter32
_Tv3Read16KCalls_Object = MibScalar
tv3Read16KCalls = _Tv3Read16KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 3, 6),
    _Tv3Read16KCalls_Type()
)
tv3Read16KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Read16KCalls.setStatus("current")
_Tv3Read32KCalls_Type = Counter32
_Tv3Read32KCalls_Object = MibScalar
tv3Read32KCalls = _Tv3Read32KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 3, 7),
    _Tv3Read32KCalls_Type()
)
tv3Read32KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Read32KCalls.setStatus("current")
_Tv3Read64KCalls_Type = Counter32
_Tv3Read64KCalls_Object = MibScalar
tv3Read64KCalls = _Tv3Read64KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 3, 8),
    _Tv3Read64KCalls_Type()
)
tv3Read64KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Read64KCalls.setStatus("current")
_Tv3Read128KCalls_Type = Counter32
_Tv3Read128KCalls_Object = MibScalar
tv3Read128KCalls = _Tv3Read128KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 3, 9),
    _Tv3Read128KCalls_Type()
)
tv3Read128KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Read128KCalls.setStatus("current")
_Tv3WriteStats_ObjectIdentity = ObjectIdentity
tv3WriteStats = _Tv3WriteStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 4)
)
_Tv3Write512Calls_Type = Counter32
_Tv3Write512Calls_Object = MibScalar
tv3Write512Calls = _Tv3Write512Calls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 4, 1),
    _Tv3Write512Calls_Type()
)
tv3Write512Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Write512Calls.setStatus("current")
_Tv3Write1KCalls_Type = Counter32
_Tv3Write1KCalls_Object = MibScalar
tv3Write1KCalls = _Tv3Write1KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 4, 2),
    _Tv3Write1KCalls_Type()
)
tv3Write1KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Write1KCalls.setStatus("current")
_Tv3Write2KCalls_Type = Counter32
_Tv3Write2KCalls_Object = MibScalar
tv3Write2KCalls = _Tv3Write2KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 4, 3),
    _Tv3Write2KCalls_Type()
)
tv3Write2KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Write2KCalls.setStatus("current")
_Tv3Write4KCalls_Type = Counter32
_Tv3Write4KCalls_Object = MibScalar
tv3Write4KCalls = _Tv3Write4KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 4, 4),
    _Tv3Write4KCalls_Type()
)
tv3Write4KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Write4KCalls.setStatus("current")
_Tv3Write8KCalls_Type = Counter32
_Tv3Write8KCalls_Object = MibScalar
tv3Write8KCalls = _Tv3Write8KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 4, 5),
    _Tv3Write8KCalls_Type()
)
tv3Write8KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Write8KCalls.setStatus("current")
_Tv3Write16KCalls_Type = Counter32
_Tv3Write16KCalls_Object = MibScalar
tv3Write16KCalls = _Tv3Write16KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 4, 6),
    _Tv3Write16KCalls_Type()
)
tv3Write16KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Write16KCalls.setStatus("current")
_Tv3Write32KCalls_Type = Counter32
_Tv3Write32KCalls_Object = MibScalar
tv3Write32KCalls = _Tv3Write32KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 4, 7),
    _Tv3Write32KCalls_Type()
)
tv3Write32KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Write32KCalls.setStatus("current")
_Tv3Write64KCalls_Type = Counter32
_Tv3Write64KCalls_Object = MibScalar
tv3Write64KCalls = _Tv3Write64KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 4, 8),
    _Tv3Write64KCalls_Type()
)
tv3Write64KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Write64KCalls.setStatus("current")
_Tv3Write128KCalls_Type = Counter32
_Tv3Write128KCalls_Object = MibScalar
tv3Write128KCalls = _Tv3Write128KCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 2, 2, 6, 4, 9),
    _Tv3Write128KCalls_Type()
)
tv3Write128KCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tv3Write128KCalls.setStatus("current")
_NfsOptions_ObjectIdentity = ObjectIdentity
nfsOptions = _NfsOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 3)
)


class _NfsIsLicensed_Type(Integer32):
    """Custom type nfsIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NfsIsLicensed_Type.__name__ = "Integer32"
_NfsIsLicensed_Object = MibScalar
nfsIsLicensed = _NfsIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 3, 3, 1),
    _NfsIsLicensed_Type()
)
nfsIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsIsLicensed.setStatus("current")
_Quota_ObjectIdentity = ObjectIdentity
quota = _Quota_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 4)
)


class _QuotaState_Type(Integer32):
    """Custom type quotaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("quotaStateInit", 3),
          ("quotaStateOff", 1),
          ("quotaStateOn", 2))
    )


_QuotaState_Type.__name__ = "Integer32"
_QuotaState_Object = MibScalar
quotaState = _QuotaState_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 1),
    _QuotaState_Type()
)
quotaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaState.setStatus("deprecated")


class _QuotaInitPercent_Type(Integer32):
    """Custom type quotaInitPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QuotaInitPercent_Type.__name__ = "Integer32"
_QuotaInitPercent_Object = MibScalar
quotaInitPercent = _QuotaInitPercent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 2),
    _QuotaInitPercent_Type()
)
quotaInitPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaInitPercent.setStatus("deprecated")
_QrTable_Object = MibTable
qrTable = _QrTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 3)
)
if mibBuilder.loadTexts:
    qrTable.setStatus("deprecated")
_QrEntry_Object = MibTableRow
qrEntry = _QrEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 3, 1)
)
qrEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "qrIndex"),
)
if mibBuilder.loadTexts:
    qrEntry.setStatus("deprecated")


class _QrIndex_Type(Integer32):
    """Custom type qrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QrIndex_Type.__name__ = "Integer32"
_QrIndex_Object = MibTableColumn
qrIndex = _QrIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 3, 1, 1),
    _QrIndex_Type()
)
qrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrIndex.setStatus("deprecated")


class _QrType_Type(Integer32):
    """Custom type qrType based on Integer32"""
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
        *(("qrTypeGroup", 2),
          ("qrTypeTree", 3),
          ("qrTypeUnknown", 4),
          ("qrTypeUser", 1))
    )


_QrType_Type.__name__ = "Integer32"
_QrType_Object = MibTableColumn
qrType = _QrType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 3, 1, 2),
    _QrType_Type()
)
qrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrType.setStatus("deprecated")
_QrId_Type = Integer32
_QrId_Object = MibTableColumn
qrId = _QrId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 3, 1, 3),
    _QrId_Type()
)
qrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrId.setStatus("deprecated")
_QrKBytesUsed_Type = Integer32
_QrKBytesUsed_Object = MibTableColumn
qrKBytesUsed = _QrKBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 3, 1, 4),
    _QrKBytesUsed_Type()
)
qrKBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrKBytesUsed.setStatus("deprecated")
_QrKBytesLimit_Type = Integer32
_QrKBytesLimit_Object = MibTableColumn
qrKBytesLimit = _QrKBytesLimit_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 3, 1, 5),
    _QrKBytesLimit_Type()
)
qrKBytesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrKBytesLimit.setStatus("deprecated")
_QrFilesUsed_Type = Integer32
_QrFilesUsed_Object = MibTableColumn
qrFilesUsed = _QrFilesUsed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 3, 1, 6),
    _QrFilesUsed_Type()
)
qrFilesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrFilesUsed.setStatus("deprecated")
_QrFileLimit_Type = Integer32
_QrFileLimit_Object = MibTableColumn
qrFileLimit = _QrFileLimit_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 3, 1, 7),
    _QrFileLimit_Type()
)
qrFileLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrFileLimit.setStatus("deprecated")
_QrPathName_Type = DisplayString
_QrPathName_Object = MibTableColumn
qrPathName = _QrPathName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 3, 1, 8),
    _QrPathName_Type()
)
qrPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrPathName.setStatus("deprecated")
_QvStateTable_Object = MibTable
qvStateTable = _QvStateTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 4)
)
if mibBuilder.loadTexts:
    qvStateTable.setStatus("current")
_QvStateEntry_Object = MibTableRow
qvStateEntry = _QvStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 4, 1)
)
qvStateEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "qvStateVolume"),
)
if mibBuilder.loadTexts:
    qvStateEntry.setStatus("current")


class _QvStateVolume_Type(Integer32):
    """Custom type qvStateVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QvStateVolume_Type.__name__ = "Integer32"
_QvStateVolume_Object = MibTableColumn
qvStateVolume = _QvStateVolume_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 4, 1, 1),
    _QvStateVolume_Type()
)
qvStateVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qvStateVolume.setStatus("current")
_QvStateName_Type = DisplayString
_QvStateName_Object = MibTableColumn
qvStateName = _QvStateName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 4, 1, 2),
    _QvStateName_Type()
)
qvStateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qvStateName.setStatus("current")


class _QvStateStat_Type(Integer32):
    """Custom type qvStateStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("quotaStateInit", 3),
          ("quotaStateOff", 1),
          ("quotaStateOn", 2))
    )


_QvStateStat_Type.__name__ = "Integer32"
_QvStateStat_Object = MibTableColumn
qvStateStat = _QvStateStat_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 4, 1, 3),
    _QvStateStat_Type()
)
qvStateStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qvStateStat.setStatus("current")


class _QvStateInitPercent_Type(Integer32):
    """Custom type qvStateInitPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QvStateInitPercent_Type.__name__ = "Integer32"
_QvStateInitPercent_Object = MibTableColumn
qvStateInitPercent = _QvStateInitPercent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 4, 1, 4),
    _QvStateInitPercent_Type()
)
qvStateInitPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qvStateInitPercent.setStatus("current")
_QrVTable_Object = MibTable
qrVTable = _QrVTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5)
)
if mibBuilder.loadTexts:
    qrVTable.setStatus("deprecated")
_QrVEntry_Object = MibTableRow
qrVEntry = _QrVEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1)
)
qrVEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "qrVVolume"),
    (0, "NETWORK-APPLIANCE-MIB", "qrVIndex"),
)
if mibBuilder.loadTexts:
    qrVEntry.setStatus("deprecated")


class _QrVIndex_Type(Integer32):
    """Custom type qrVIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QrVIndex_Type.__name__ = "Integer32"
_QrVIndex_Object = MibTableColumn
qrVIndex = _QrVIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 1),
    _QrVIndex_Type()
)
qrVIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVIndex.setStatus("deprecated")


class _QrVType_Type(Integer32):
    """Custom type qrVType based on Integer32"""
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
        *(("qrVTypeGroup", 2),
          ("qrVTypeGroupDefault", 5),
          ("qrVTypeTree", 3),
          ("qrVTypeUnknown", 6),
          ("qrVTypeUser", 1),
          ("qrVTypeUserDefault", 4))
    )


_QrVType_Type.__name__ = "Integer32"
_QrVType_Object = MibTableColumn
qrVType = _QrVType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 2),
    _QrVType_Type()
)
qrVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVType.setStatus("deprecated")
_QrVId_Type = Integer32
_QrVId_Object = MibTableColumn
qrVId = _QrVId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 3),
    _QrVId_Type()
)
qrVId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVId.setStatus("deprecated")
_QrVKBytesUsed_Type = Integer32
_QrVKBytesUsed_Object = MibTableColumn
qrVKBytesUsed = _QrVKBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 4),
    _QrVKBytesUsed_Type()
)
qrVKBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVKBytesUsed.setStatus("deprecated")
_QrVKBytesLimit_Type = Integer32
_QrVKBytesLimit_Object = MibTableColumn
qrVKBytesLimit = _QrVKBytesLimit_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 5),
    _QrVKBytesLimit_Type()
)
qrVKBytesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVKBytesLimit.setStatus("deprecated")
_QrVFilesUsed_Type = Integer32
_QrVFilesUsed_Object = MibTableColumn
qrVFilesUsed = _QrVFilesUsed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 6),
    _QrVFilesUsed_Type()
)
qrVFilesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVFilesUsed.setStatus("deprecated")
_QrVFileLimit_Type = Integer32
_QrVFileLimit_Object = MibTableColumn
qrVFileLimit = _QrVFileLimit_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 7),
    _QrVFileLimit_Type()
)
qrVFileLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVFileLimit.setStatus("deprecated")
_QrVPathName_Type = DisplayString
_QrVPathName_Object = MibTableColumn
qrVPathName = _QrVPathName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 8),
    _QrVPathName_Type()
)
qrVPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVPathName.setStatus("deprecated")


class _QrVVolume_Type(Integer32):
    """Custom type qrVVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QrVVolume_Type.__name__ = "Integer32"
_QrVVolume_Object = MibTableColumn
qrVVolume = _QrVVolume_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 9),
    _QrVVolume_Type()
)
qrVVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVVolume.setStatus("deprecated")
_QrVTree_Type = DisplayString
_QrVTree_Object = MibTableColumn
qrVTree = _QrVTree_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 10),
    _QrVTree_Type()
)
qrVTree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVTree.setStatus("deprecated")


class _QrVIdType_Type(Integer32):
    """Custom type qrVIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qrVIdValid", 1),
          ("qrVSidValid", 2))
    )


_QrVIdType_Type.__name__ = "Integer32"
_QrVIdType_Object = MibTableColumn
qrVIdType = _QrVIdType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 11),
    _QrVIdType_Type()
)
qrVIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVIdType.setStatus("deprecated")
_QrVSid_Type = DisplayString
_QrVSid_Object = MibTableColumn
qrVSid = _QrVSid_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 12),
    _QrVSid_Type()
)
qrVSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVSid.setStatus("deprecated")
_QrVKBytesThreshold_Type = Integer32
_QrVKBytesThreshold_Object = MibTableColumn
qrVKBytesThreshold = _QrVKBytesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 13),
    _QrVKBytesThreshold_Type()
)
qrVKBytesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVKBytesThreshold.setStatus("deprecated")
_QrVKBytesLimitSoft_Type = Integer32
_QrVKBytesLimitSoft_Object = MibTableColumn
qrVKBytesLimitSoft = _QrVKBytesLimitSoft_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 14),
    _QrVKBytesLimitSoft_Type()
)
qrVKBytesLimitSoft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVKBytesLimitSoft.setStatus("deprecated")
_QrVFileLimitSoft_Type = Integer32
_QrVFileLimitSoft_Object = MibTableColumn
qrVFileLimitSoft = _QrVFileLimitSoft_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 5, 1, 15),
    _QrVFileLimitSoft_Type()
)
qrVFileLimitSoft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrVFileLimitSoft.setStatus("deprecated")
_QrV2Table_Object = MibTable
qrV2Table = _QrV2Table_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6)
)
if mibBuilder.loadTexts:
    qrV2Table.setStatus("current")
_QrV2Entry_Object = MibTableRow
qrV2Entry = _QrV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1)
)
qrV2Entry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "qrV2Volume"),
    (0, "NETWORK-APPLIANCE-MIB", "qrV2Index"),
)
if mibBuilder.loadTexts:
    qrV2Entry.setStatus("current")


class _QrV2Index_Type(Integer32):
    """Custom type qrV2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QrV2Index_Type.__name__ = "Integer32"
_QrV2Index_Object = MibTableColumn
qrV2Index = _QrV2Index_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 1),
    _QrV2Index_Type()
)
qrV2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2Index.setStatus("current")


class _QrV2Type_Type(Integer32):
    """Custom type qrV2Type based on Integer32"""
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
        *(("qrV2TypeGroup", 2),
          ("qrV2TypeGroupDefault", 5),
          ("qrV2TypeTree", 3),
          ("qrV2TypeUnknown", 6),
          ("qrV2TypeUser", 1),
          ("qrV2TypeUserDefault", 4))
    )


_QrV2Type_Type.__name__ = "Integer32"
_QrV2Type_Object = MibTableColumn
qrV2Type = _QrV2Type_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 2),
    _QrV2Type_Type()
)
qrV2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2Type.setStatus("current")
_QrV2Id_Type = Integer32
_QrV2Id_Object = MibTableColumn
qrV2Id = _QrV2Id_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 3),
    _QrV2Id_Type()
)
qrV2Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2Id.setStatus("current")
_QrV2HighKBytesUsed_Type = Integer32
_QrV2HighKBytesUsed_Object = MibTableColumn
qrV2HighKBytesUsed = _QrV2HighKBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 4),
    _QrV2HighKBytesUsed_Type()
)
qrV2HighKBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2HighKBytesUsed.setStatus("current")
_QrV2LowKBytesUsed_Type = Integer32
_QrV2LowKBytesUsed_Object = MibTableColumn
qrV2LowKBytesUsed = _QrV2LowKBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 5),
    _QrV2LowKBytesUsed_Type()
)
qrV2LowKBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2LowKBytesUsed.setStatus("current")


class _QrV2QuotaUnlimited_Type(Integer32):
    """Custom type qrV2QuotaUnlimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_QrV2QuotaUnlimited_Type.__name__ = "Integer32"
_QrV2QuotaUnlimited_Object = MibTableColumn
qrV2QuotaUnlimited = _QrV2QuotaUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 6),
    _QrV2QuotaUnlimited_Type()
)
qrV2QuotaUnlimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2QuotaUnlimited.setStatus("current")
_QrV2HighKBytesLimit_Type = Integer32
_QrV2HighKBytesLimit_Object = MibTableColumn
qrV2HighKBytesLimit = _QrV2HighKBytesLimit_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 7),
    _QrV2HighKBytesLimit_Type()
)
qrV2HighKBytesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2HighKBytesLimit.setStatus("current")
_QrV2LowKBytesLimit_Type = Integer32
_QrV2LowKBytesLimit_Object = MibTableColumn
qrV2LowKBytesLimit = _QrV2LowKBytesLimit_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 8),
    _QrV2LowKBytesLimit_Type()
)
qrV2LowKBytesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2LowKBytesLimit.setStatus("current")
_QrV2FilesUsed_Type = Integer32
_QrV2FilesUsed_Object = MibTableColumn
qrV2FilesUsed = _QrV2FilesUsed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 9),
    _QrV2FilesUsed_Type()
)
qrV2FilesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2FilesUsed.setStatus("current")


class _QrV2FileQuotaUnlimited_Type(Integer32):
    """Custom type qrV2FileQuotaUnlimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_QrV2FileQuotaUnlimited_Type.__name__ = "Integer32"
_QrV2FileQuotaUnlimited_Object = MibTableColumn
qrV2FileQuotaUnlimited = _QrV2FileQuotaUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 10),
    _QrV2FileQuotaUnlimited_Type()
)
qrV2FileQuotaUnlimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2FileQuotaUnlimited.setStatus("current")
_QrV2FileLimit_Type = Integer32
_QrV2FileLimit_Object = MibTableColumn
qrV2FileLimit = _QrV2FileLimit_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 11),
    _QrV2FileLimit_Type()
)
qrV2FileLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2FileLimit.setStatus("current")
_QrV2PathName_Type = DisplayString
_QrV2PathName_Object = MibTableColumn
qrV2PathName = _QrV2PathName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 12),
    _QrV2PathName_Type()
)
qrV2PathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2PathName.setStatus("current")


class _QrV2Volume_Type(Integer32):
    """Custom type qrV2Volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QrV2Volume_Type.__name__ = "Integer32"
_QrV2Volume_Object = MibTableColumn
qrV2Volume = _QrV2Volume_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 13),
    _QrV2Volume_Type()
)
qrV2Volume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2Volume.setStatus("current")
_QrV2Tree_Type = DisplayString
_QrV2Tree_Object = MibTableColumn
qrV2Tree = _QrV2Tree_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 14),
    _QrV2Tree_Type()
)
qrV2Tree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2Tree.setStatus("current")


class _QrV2IdType_Type(Integer32):
    """Custom type qrV2IdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qrV2IdValid", 1),
          ("qrV2SidValid", 2))
    )


_QrV2IdType_Type.__name__ = "Integer32"
_QrV2IdType_Object = MibTableColumn
qrV2IdType = _QrV2IdType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 15),
    _QrV2IdType_Type()
)
qrV2IdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2IdType.setStatus("current")
_QrV2Sid_Type = DisplayString
_QrV2Sid_Object = MibTableColumn
qrV2Sid = _QrV2Sid_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 16),
    _QrV2Sid_Type()
)
qrV2Sid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2Sid.setStatus("current")


class _QrV2ThresholdUnlimited_Type(Integer32):
    """Custom type qrV2ThresholdUnlimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_QrV2ThresholdUnlimited_Type.__name__ = "Integer32"
_QrV2ThresholdUnlimited_Object = MibTableColumn
qrV2ThresholdUnlimited = _QrV2ThresholdUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 17),
    _QrV2ThresholdUnlimited_Type()
)
qrV2ThresholdUnlimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2ThresholdUnlimited.setStatus("current")
_QrV2HighKBytesThreshold_Type = Integer32
_QrV2HighKBytesThreshold_Object = MibTableColumn
qrV2HighKBytesThreshold = _QrV2HighKBytesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 18),
    _QrV2HighKBytesThreshold_Type()
)
qrV2HighKBytesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2HighKBytesThreshold.setStatus("current")
_QrV2LowKBytesThreshold_Type = Integer32
_QrV2LowKBytesThreshold_Object = MibTableColumn
qrV2LowKBytesThreshold = _QrV2LowKBytesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 19),
    _QrV2LowKBytesThreshold_Type()
)
qrV2LowKBytesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2LowKBytesThreshold.setStatus("current")


class _QrV2SoftQuotaUnlimited_Type(Integer32):
    """Custom type qrV2SoftQuotaUnlimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_QrV2SoftQuotaUnlimited_Type.__name__ = "Integer32"
_QrV2SoftQuotaUnlimited_Object = MibTableColumn
qrV2SoftQuotaUnlimited = _QrV2SoftQuotaUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 20),
    _QrV2SoftQuotaUnlimited_Type()
)
qrV2SoftQuotaUnlimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2SoftQuotaUnlimited.setStatus("current")
_QrV2HighKBytesSoftLimit_Type = Integer32
_QrV2HighKBytesSoftLimit_Object = MibTableColumn
qrV2HighKBytesSoftLimit = _QrV2HighKBytesSoftLimit_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 21),
    _QrV2HighKBytesSoftLimit_Type()
)
qrV2HighKBytesSoftLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2HighKBytesSoftLimit.setStatus("current")
_QrV2LowKBytesSoftLimit_Type = Integer32
_QrV2LowKBytesSoftLimit_Object = MibTableColumn
qrV2LowKBytesSoftLimit = _QrV2LowKBytesSoftLimit_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 22),
    _QrV2LowKBytesSoftLimit_Type()
)
qrV2LowKBytesSoftLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2LowKBytesSoftLimit.setStatus("current")


class _QrV2SoftFileQuotaUnlimited_Type(Integer32):
    """Custom type qrV2SoftFileQuotaUnlimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_QrV2SoftFileQuotaUnlimited_Type.__name__ = "Integer32"
_QrV2SoftFileQuotaUnlimited_Object = MibTableColumn
qrV2SoftFileQuotaUnlimited = _QrV2SoftFileQuotaUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 23),
    _QrV2SoftFileQuotaUnlimited_Type()
)
qrV2SoftFileQuotaUnlimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2SoftFileQuotaUnlimited.setStatus("current")
_QrV2SoftFileLimit_Type = Integer32
_QrV2SoftFileLimit_Object = MibTableColumn
qrV2SoftFileLimit = _QrV2SoftFileLimit_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 24),
    _QrV2SoftFileLimit_Type()
)
qrV2SoftFileLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV2SoftFileLimit.setStatus("current")
_QrV264KBytesUsed_Type = Counter64
_QrV264KBytesUsed_Object = MibTableColumn
qrV264KBytesUsed = _QrV264KBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 25),
    _QrV264KBytesUsed_Type()
)
qrV264KBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV264KBytesUsed.setStatus("current")
_QrV264KBytesLimit_Type = Counter64
_QrV264KBytesLimit_Object = MibTableColumn
qrV264KBytesLimit = _QrV264KBytesLimit_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 26),
    _QrV264KBytesLimit_Type()
)
qrV264KBytesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV264KBytesLimit.setStatus("current")
_QrV264KBytesThreshold_Type = Counter64
_QrV264KBytesThreshold_Object = MibTableColumn
qrV264KBytesThreshold = _QrV264KBytesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 27),
    _QrV264KBytesThreshold_Type()
)
qrV264KBytesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV264KBytesThreshold.setStatus("current")
_QrV264KBytesSoftLimit_Type = Counter64
_QrV264KBytesSoftLimit_Object = MibTableColumn
qrV264KBytesSoftLimit = _QrV264KBytesSoftLimit_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 4, 6, 1, 28),
    _QrV264KBytesSoftLimit_Type()
)
qrV264KBytesSoftLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qrV264KBytesSoftLimit.setStatus("current")
_Filesys_ObjectIdentity = ObjectIdentity
filesys = _Filesys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 5)
)
_FilesysMaxfilesAvail_Type = Integer32
_FilesysMaxfilesAvail_Object = MibScalar
filesysMaxfilesAvail = _FilesysMaxfilesAvail_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 1),
    _FilesysMaxfilesAvail_Type()
)
filesysMaxfilesAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filesysMaxfilesAvail.setStatus("deprecated")
_FilesysMaxfilesUsed_Type = Integer32
_FilesysMaxfilesUsed_Object = MibScalar
filesysMaxfilesUsed = _FilesysMaxfilesUsed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 2),
    _FilesysMaxfilesUsed_Type()
)
filesysMaxfilesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filesysMaxfilesUsed.setStatus("deprecated")
_FilesysMaxfilesPossible_Type = Integer32
_FilesysMaxfilesPossible_Object = MibScalar
filesysMaxfilesPossible = _FilesysMaxfilesPossible_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 3),
    _FilesysMaxfilesPossible_Type()
)
filesysMaxfilesPossible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filesysMaxfilesPossible.setStatus("deprecated")
_DfTable_Object = MibTable
dfTable = _DfTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4)
)
if mibBuilder.loadTexts:
    dfTable.setStatus("current")
_DfEntry_Object = MibTableRow
dfEntry = _DfEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1)
)
dfEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "dfIndex"),
)
if mibBuilder.loadTexts:
    dfEntry.setStatus("current")


class _DfIndex_Type(Integer32):
    """Custom type dfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DfIndex_Type.__name__ = "Integer32"
_DfIndex_Object = MibTableColumn
dfIndex = _DfIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 1),
    _DfIndex_Type()
)
dfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfIndex.setStatus("current")
_DfFileSys_Type = DisplayString
_DfFileSys_Object = MibTableColumn
dfFileSys = _DfFileSys_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 2),
    _DfFileSys_Type()
)
dfFileSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfFileSys.setStatus("current")
_DfKBytesTotal_Type = Integer32
_DfKBytesTotal_Object = MibTableColumn
dfKBytesTotal = _DfKBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 3),
    _DfKBytesTotal_Type()
)
dfKBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfKBytesTotal.setStatus("deprecated")
_DfKBytesUsed_Type = Integer32
_DfKBytesUsed_Object = MibTableColumn
dfKBytesUsed = _DfKBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 4),
    _DfKBytesUsed_Type()
)
dfKBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfKBytesUsed.setStatus("deprecated")
_DfKBytesAvail_Type = Integer32
_DfKBytesAvail_Object = MibTableColumn
dfKBytesAvail = _DfKBytesAvail_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 5),
    _DfKBytesAvail_Type()
)
dfKBytesAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfKBytesAvail.setStatus("deprecated")
_DfPerCentKBytesCapacity_Type = Integer32
_DfPerCentKBytesCapacity_Object = MibTableColumn
dfPerCentKBytesCapacity = _DfPerCentKBytesCapacity_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 6),
    _DfPerCentKBytesCapacity_Type()
)
dfPerCentKBytesCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPerCentKBytesCapacity.setStatus("current")
_DfInodesUsed_Type = Integer32
_DfInodesUsed_Object = MibTableColumn
dfInodesUsed = _DfInodesUsed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 7),
    _DfInodesUsed_Type()
)
dfInodesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfInodesUsed.setStatus("current")
_DfInodesFree_Type = Integer32
_DfInodesFree_Object = MibTableColumn
dfInodesFree = _DfInodesFree_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 8),
    _DfInodesFree_Type()
)
dfInodesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfInodesFree.setStatus("current")
_DfPerCentInodeCapacity_Type = Integer32
_DfPerCentInodeCapacity_Object = MibTableColumn
dfPerCentInodeCapacity = _DfPerCentInodeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 9),
    _DfPerCentInodeCapacity_Type()
)
dfPerCentInodeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPerCentInodeCapacity.setStatus("current")
_DfMountedOn_Type = DisplayString
_DfMountedOn_Object = MibTableColumn
dfMountedOn = _DfMountedOn_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 10),
    _DfMountedOn_Type()
)
dfMountedOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfMountedOn.setStatus("current")
_DfMaxFilesAvail_Type = Integer32
_DfMaxFilesAvail_Object = MibTableColumn
dfMaxFilesAvail = _DfMaxFilesAvail_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 11),
    _DfMaxFilesAvail_Type()
)
dfMaxFilesAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfMaxFilesAvail.setStatus("current")
_DfMaxFilesUsed_Type = Integer32
_DfMaxFilesUsed_Object = MibTableColumn
dfMaxFilesUsed = _DfMaxFilesUsed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 12),
    _DfMaxFilesUsed_Type()
)
dfMaxFilesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfMaxFilesUsed.setStatus("current")
_DfMaxFilesPossible_Type = Integer32
_DfMaxFilesPossible_Object = MibTableColumn
dfMaxFilesPossible = _DfMaxFilesPossible_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 13),
    _DfMaxFilesPossible_Type()
)
dfMaxFilesPossible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfMaxFilesPossible.setStatus("current")
_DfHighTotalKBytes_Type = Integer32
_DfHighTotalKBytes_Object = MibTableColumn
dfHighTotalKBytes = _DfHighTotalKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 14),
    _DfHighTotalKBytes_Type()
)
dfHighTotalKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfHighTotalKBytes.setStatus("current")
_DfLowTotalKBytes_Type = Integer32
_DfLowTotalKBytes_Object = MibTableColumn
dfLowTotalKBytes = _DfLowTotalKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 15),
    _DfLowTotalKBytes_Type()
)
dfLowTotalKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfLowTotalKBytes.setStatus("current")
_DfHighUsedKBytes_Type = Integer32
_DfHighUsedKBytes_Object = MibTableColumn
dfHighUsedKBytes = _DfHighUsedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 16),
    _DfHighUsedKBytes_Type()
)
dfHighUsedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfHighUsedKBytes.setStatus("current")
_DfLowUsedKBytes_Type = Integer32
_DfLowUsedKBytes_Object = MibTableColumn
dfLowUsedKBytes = _DfLowUsedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 17),
    _DfLowUsedKBytes_Type()
)
dfLowUsedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfLowUsedKBytes.setStatus("current")
_DfHighAvailKBytes_Type = Integer32
_DfHighAvailKBytes_Object = MibTableColumn
dfHighAvailKBytes = _DfHighAvailKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 18),
    _DfHighAvailKBytes_Type()
)
dfHighAvailKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfHighAvailKBytes.setStatus("current")
_DfLowAvailKBytes_Type = Integer32
_DfLowAvailKBytes_Object = MibTableColumn
dfLowAvailKBytes = _DfLowAvailKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 19),
    _DfLowAvailKBytes_Type()
)
dfLowAvailKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfLowAvailKBytes.setStatus("current")


class _DfStatus_Type(Integer32):
    """Custom type dfStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("creating", 5),
          ("destroying", 4),
          ("frozen", 3),
          ("mounted", 2),
          ("mounting", 6),
          ("nofsinfo", 8),
          ("replayed", 10),
          ("replaying", 9),
          ("unmounted", 1),
          ("unmounting", 7))
    )


_DfStatus_Type.__name__ = "Integer32"
_DfStatus_Object = MibTableColumn
dfStatus = _DfStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 20),
    _DfStatus_Type()
)
dfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfStatus.setStatus("current")


class _DfMirrorStatus_Type(Integer32):
    """Custom type dfMirrorStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cpcheckwait", 4),
          ("degraded", 7),
          ("failed", 9),
          ("invalid", 1),
          ("limbo", 10),
          ("needcpcheck", 3),
          ("normal", 6),
          ("resyncing", 8),
          ("uninitialized", 2),
          ("unmirrored", 5))
    )


_DfMirrorStatus_Type.__name__ = "Integer32"
_DfMirrorStatus_Object = MibTableColumn
dfMirrorStatus = _DfMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 21),
    _DfMirrorStatus_Type()
)
dfMirrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfMirrorStatus.setStatus("current")
_DfPlexCount_Type = Integer32
_DfPlexCount_Object = MibTableColumn
dfPlexCount = _DfPlexCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 22),
    _DfPlexCount_Type()
)
dfPlexCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPlexCount.setStatus("current")


class _DfType_Type(Integer32):
    """Custom type dfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 3),
          ("flexibleVolume", 2),
          ("traditionalVolume", 1))
    )


_DfType_Type.__name__ = "Integer32"
_DfType_Object = MibTableColumn
dfType = _DfType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 23),
    _DfType_Type()
)
dfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfType.setStatus("current")
_DfHighSisSharedKBytes_Type = Integer32
_DfHighSisSharedKBytes_Object = MibTableColumn
dfHighSisSharedKBytes = _DfHighSisSharedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 24),
    _DfHighSisSharedKBytes_Type()
)
dfHighSisSharedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfHighSisSharedKBytes.setStatus("current")
_DfLowSisSharedKBytes_Type = Integer32
_DfLowSisSharedKBytes_Object = MibTableColumn
dfLowSisSharedKBytes = _DfLowSisSharedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 25),
    _DfLowSisSharedKBytes_Type()
)
dfLowSisSharedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfLowSisSharedKBytes.setStatus("current")
_DfHighSisSavedKBytes_Type = Integer32
_DfHighSisSavedKBytes_Object = MibTableColumn
dfHighSisSavedKBytes = _DfHighSisSavedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 26),
    _DfHighSisSavedKBytes_Type()
)
dfHighSisSavedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfHighSisSavedKBytes.setStatus("current")
_DfLowSisSavedKBytes_Type = Integer32
_DfLowSisSavedKBytes_Object = MibTableColumn
dfLowSisSavedKBytes = _DfLowSisSavedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 27),
    _DfLowSisSavedKBytes_Type()
)
dfLowSisSavedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfLowSisSavedKBytes.setStatus("current")
_DfPerCentSaved_Type = Integer32
_DfPerCentSaved_Object = MibTableColumn
dfPerCentSaved = _DfPerCentSaved_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 28),
    _DfPerCentSaved_Type()
)
dfPerCentSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfPerCentSaved.setStatus("current")
_Df64TotalKBytes_Type = Counter64
_Df64TotalKBytes_Object = MibTableColumn
df64TotalKBytes = _Df64TotalKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 29),
    _Df64TotalKBytes_Type()
)
df64TotalKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df64TotalKBytes.setStatus("current")
_Df64UsedKBytes_Type = Counter64
_Df64UsedKBytes_Object = MibTableColumn
df64UsedKBytes = _Df64UsedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 30),
    _Df64UsedKBytes_Type()
)
df64UsedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df64UsedKBytes.setStatus("current")
_Df64AvailKBytes_Type = Counter64
_Df64AvailKBytes_Object = MibTableColumn
df64AvailKBytes = _Df64AvailKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 31),
    _Df64AvailKBytes_Type()
)
df64AvailKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df64AvailKBytes.setStatus("current")
_Df64SisSharedKBytes_Type = Counter64
_Df64SisSharedKBytes_Object = MibTableColumn
df64SisSharedKBytes = _Df64SisSharedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 32),
    _Df64SisSharedKBytes_Type()
)
df64SisSharedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df64SisSharedKBytes.setStatus("current")
_Df64SisSavedKBytes_Type = Counter64
_Df64SisSavedKBytes_Object = MibTableColumn
df64SisSavedKBytes = _Df64SisSavedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 4, 1, 33),
    _Df64SisSavedKBytes_Type()
)
df64SisSavedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df64SisSavedKBytes.setStatus("current")
_Snapshot_ObjectIdentity = ObjectIdentity
snapshot = _Snapshot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5)
)
_SlTable_Object = MibTable
slTable = _SlTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    slTable.setStatus("deprecated")
_SlEntry_Object = MibTableRow
slEntry = _SlEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 1, 1)
)
slEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "slIndex"),
)
if mibBuilder.loadTexts:
    slEntry.setStatus("deprecated")


class _SlIndex_Type(Integer32):
    """Custom type slIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlIndex_Type.__name__ = "Integer32"
_SlIndex_Object = MibTableColumn
slIndex = _SlIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 1, 1, 1),
    _SlIndex_Type()
)
slIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slIndex.setStatus("deprecated")


class _SlMonth_Type(Integer32):
    """Custom type slMonth based on Integer32"""
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
        *(("april", 4),
          ("august", 8),
          ("december", 12),
          ("february", 2),
          ("january", 1),
          ("july", 7),
          ("june", 6),
          ("march", 3),
          ("may", 5),
          ("november", 11),
          ("october", 10),
          ("september", 9))
    )


_SlMonth_Type.__name__ = "Integer32"
_SlMonth_Object = MibTableColumn
slMonth = _SlMonth_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 1, 1, 2),
    _SlMonth_Type()
)
slMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slMonth.setStatus("deprecated")


class _SlDay_Type(Integer32):
    """Custom type slDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SlDay_Type.__name__ = "Integer32"
_SlDay_Object = MibTableColumn
slDay = _SlDay_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 1, 1, 3),
    _SlDay_Type()
)
slDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slDay.setStatus("deprecated")


class _SlHour_Type(Integer32):
    """Custom type slHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SlHour_Type.__name__ = "Integer32"
_SlHour_Object = MibTableColumn
slHour = _SlHour_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 1, 1, 4),
    _SlHour_Type()
)
slHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slHour.setStatus("deprecated")


class _SlMinutes_Type(Integer32):
    """Custom type slMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SlMinutes_Type.__name__ = "Integer32"
_SlMinutes_Object = MibTableColumn
slMinutes = _SlMinutes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 1, 1, 5),
    _SlMinutes_Type()
)
slMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slMinutes.setStatus("deprecated")
_SlName_Type = DisplayString
_SlName_Object = MibTableColumn
slName = _SlName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 1, 1, 6),
    _SlName_Type()
)
slName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slName.setStatus("deprecated")
_SlVTable_Object = MibTable
slVTable = _SlVTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    slVTable.setStatus("current")
_SlVEntry_Object = MibTableRow
slVEntry = _SlVEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 2, 1)
)
slVEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "slVVolume"),
    (0, "NETWORK-APPLIANCE-MIB", "slVIndex"),
)
if mibBuilder.loadTexts:
    slVEntry.setStatus("current")


class _SlVIndex_Type(Integer32):
    """Custom type slVIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlVIndex_Type.__name__ = "Integer32"
_SlVIndex_Object = MibTableColumn
slVIndex = _SlVIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 2, 1, 1),
    _SlVIndex_Type()
)
slVIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slVIndex.setStatus("current")


class _SlVMonth_Type(Integer32):
    """Custom type slVMonth based on Integer32"""
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
        *(("april", 4),
          ("august", 8),
          ("december", 12),
          ("february", 2),
          ("january", 1),
          ("july", 7),
          ("june", 6),
          ("march", 3),
          ("may", 5),
          ("november", 11),
          ("october", 10),
          ("september", 9))
    )


_SlVMonth_Type.__name__ = "Integer32"
_SlVMonth_Object = MibTableColumn
slVMonth = _SlVMonth_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 2, 1, 2),
    _SlVMonth_Type()
)
slVMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slVMonth.setStatus("current")


class _SlVDay_Type(Integer32):
    """Custom type slVDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SlVDay_Type.__name__ = "Integer32"
_SlVDay_Object = MibTableColumn
slVDay = _SlVDay_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 2, 1, 3),
    _SlVDay_Type()
)
slVDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slVDay.setStatus("current")


class _SlVHour_Type(Integer32):
    """Custom type slVHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SlVHour_Type.__name__ = "Integer32"
_SlVHour_Object = MibTableColumn
slVHour = _SlVHour_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 2, 1, 4),
    _SlVHour_Type()
)
slVHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slVHour.setStatus("current")


class _SlVMinutes_Type(Integer32):
    """Custom type slVMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SlVMinutes_Type.__name__ = "Integer32"
_SlVMinutes_Object = MibTableColumn
slVMinutes = _SlVMinutes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 2, 1, 5),
    _SlVMinutes_Type()
)
slVMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slVMinutes.setStatus("current")
_SlVName_Type = DisplayString
_SlVName_Object = MibTableColumn
slVName = _SlVName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 2, 1, 6),
    _SlVName_Type()
)
slVName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slVName.setStatus("current")


class _SlVVolume_Type(Integer32):
    """Custom type slVVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlVVolume_Type.__name__ = "Integer32"
_SlVVolume_Object = MibTableColumn
slVVolume = _SlVVolume_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 2, 1, 7),
    _SlVVolume_Type()
)
slVVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slVVolume.setStatus("current")
_SlVNumber_Type = Integer32
_SlVNumber_Object = MibTableColumn
slVNumber = _SlVNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 2, 1, 8),
    _SlVNumber_Type()
)
slVNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slVNumber.setStatus("current")
_SlVVolumeName_Type = DisplayString
_SlVVolumeName_Object = MibTableColumn
slVVolumeName = _SlVVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 2, 1, 9),
    _SlVVolumeName_Type()
)
slVVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slVVolumeName.setStatus("current")


class _SlVType_Type(Integer32):
    """Custom type slVType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 3),
          ("flexibleVolume", 2),
          ("traditionalVolume", 1))
    )


_SlVType_Type.__name__ = "Integer32"
_SlVType_Object = MibTableColumn
slVType = _SlVType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 2, 1, 10),
    _SlVType_Type()
)
slVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slVType.setStatus("current")
_SlQTable_Object = MibTable
slQTable = _SlQTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 3)
)
if mibBuilder.loadTexts:
    slQTable.setStatus("current")
_SlQEntry_Object = MibTableRow
slQEntry = _SlQEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 3, 1)
)
slQEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "slQVolume"),
    (0, "NETWORK-APPLIANCE-MIB", "slQQtree"),
    (0, "NETWORK-APPLIANCE-MIB", "slQIndex"),
)
if mibBuilder.loadTexts:
    slQEntry.setStatus("current")


class _SlQIndex_Type(Integer32):
    """Custom type slQIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlQIndex_Type.__name__ = "Integer32"
_SlQIndex_Object = MibTableColumn
slQIndex = _SlQIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 3, 1, 1),
    _SlQIndex_Type()
)
slQIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slQIndex.setStatus("current")


class _SlQVolume_Type(Integer32):
    """Custom type slQVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlQVolume_Type.__name__ = "Integer32"
_SlQVolume_Object = MibTableColumn
slQVolume = _SlQVolume_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 3, 1, 2),
    _SlQVolume_Type()
)
slQVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slQVolume.setStatus("current")


class _SlQQtree_Type(Integer32):
    """Custom type slQQtree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlQQtree_Type.__name__ = "Integer32"
_SlQQtree_Object = MibTableColumn
slQQtree = _SlQQtree_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 3, 1, 3),
    _SlQQtree_Type()
)
slQQtree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slQQtree.setStatus("current")
_SlQSnapshotName_Type = DisplayString
_SlQSnapshotName_Object = MibTableColumn
slQSnapshotName = _SlQSnapshotName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 3, 1, 4),
    _SlQSnapshotName_Type()
)
slQSnapshotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slQSnapshotName.setStatus("current")
_SlQSnapshotTime_Type = Integer32
_SlQSnapshotTime_Object = MibTableColumn
slQSnapshotTime = _SlQSnapshotTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 3, 1, 5),
    _SlQSnapshotTime_Type()
)
slQSnapshotTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slQSnapshotTime.setStatus("current")
_SlQQtreeName_Type = DisplayString
_SlQQtreeName_Object = MibTableColumn
slQQtreeName = _SlQQtreeName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 3, 1, 6),
    _SlQQtreeName_Type()
)
slQQtreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slQQtreeName.setStatus("current")


class _SlQQtreeContent_Type(Integer32):
    """Custom type slQQtreeContent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("original", 3),
          ("replica", 1),
          ("transitioning", 2))
    )


_SlQQtreeContent_Type.__name__ = "Integer32"
_SlQQtreeContent_Object = MibTableColumn
slQQtreeContent = _SlQQtreeContent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 3, 1, 7),
    _SlQQtreeContent_Type()
)
slQQtreeContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slQQtreeContent.setStatus("current")
_SlQSource_Type = OctetString
_SlQSource_Object = MibTableColumn
slQSource = _SlQSource_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 3, 1, 8),
    _SlQSource_Type()
)
slQSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slQSource.setStatus("current")
_SlQSourceTime_Type = Integer32
_SlQSourceTime_Object = MibTableColumn
slQSourceTime = _SlQSourceTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 3, 1, 9),
    _SlQSourceTime_Type()
)
slQSourceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slQSourceTime.setStatus("current")
_SlQVolumeName_Type = DisplayString
_SlQVolumeName_Object = MibTableColumn
slQVolumeName = _SlQVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 5, 3, 1, 10),
    _SlQVolumeName_Type()
)
slQVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slQVolumeName.setStatus("current")
_DfNumber_Type = Integer32
_DfNumber_Object = MibScalar
dfNumber = _DfNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 6),
    _DfNumber_Type()
)
dfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfNumber.setStatus("current")
_FsStatus_ObjectIdentity = ObjectIdentity
fsStatus = _FsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 7)
)


class _FsOverallStatus_Type(Integer32):
    """Custom type fsOverallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("nearlyFull", 2),
          ("ok", 1))
    )


_FsOverallStatus_Type.__name__ = "Integer32"
_FsOverallStatus_Object = MibScalar
fsOverallStatus = _FsOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 7, 1),
    _FsOverallStatus_Type()
)
fsOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOverallStatus.setStatus("current")
_FsStatusMessage_Type = DisplayString
_FsStatusMessage_Object = MibScalar
fsStatusMessage = _FsStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 7, 2),
    _FsStatusMessage_Type()
)
fsStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusMessage.setStatus("current")


class _FsMaxUsedBytesPerCent_Type(Integer32):
    """Custom type fsMaxUsedBytesPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsMaxUsedBytesPerCent_Type.__name__ = "Integer32"
_FsMaxUsedBytesPerCent_Object = MibScalar
fsMaxUsedBytesPerCent = _FsMaxUsedBytesPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 7, 3),
    _FsMaxUsedBytesPerCent_Type()
)
fsMaxUsedBytesPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMaxUsedBytesPerCent.setStatus("current")


class _FsMaxUsedInodesPerCent_Type(Integer32):
    """Custom type fsMaxUsedInodesPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsMaxUsedInodesPerCent_Type.__name__ = "Integer32"
_FsMaxUsedInodesPerCent_Object = MibScalar
fsMaxUsedInodesPerCent = _FsMaxUsedInodesPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 7, 4),
    _FsMaxUsedInodesPerCent_Type()
)
fsMaxUsedInodesPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMaxUsedInodesPerCent.setStatus("current")


class _FsMaxUsedReservedPerCent_Type(Integer32):
    """Custom type fsMaxUsedReservedPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsMaxUsedReservedPerCent_Type.__name__ = "Integer32"
_FsMaxUsedReservedPerCent_Object = MibScalar
fsMaxUsedReservedPerCent = _FsMaxUsedReservedPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 7, 5),
    _FsMaxUsedReservedPerCent_Type()
)
fsMaxUsedReservedPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMaxUsedReservedPerCent.setStatus("current")
_VolTable_Object = MibTable
volTable = _VolTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8)
)
if mibBuilder.loadTexts:
    volTable.setStatus("current")
_VolEntry_Object = MibTableRow
volEntry = _VolEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1)
)
volEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "volIndex"),
)
if mibBuilder.loadTexts:
    volEntry.setStatus("current")


class _VolIndex_Type(Integer32):
    """Custom type volIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_VolIndex_Type.__name__ = "Integer32"
_VolIndex_Object = MibTableColumn
volIndex = _VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 1),
    _VolIndex_Type()
)
volIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIndex.setStatus("current")
_VolName_Type = DisplayString
_VolName_Object = MibTableColumn
volName = _VolName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 2),
    _VolName_Type()
)
volName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volName.setStatus("current")
_VolFSID_Type = DisplayString
_VolFSID_Object = MibTableColumn
volFSID = _VolFSID_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 3),
    _VolFSID_Type()
)
volFSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volFSID.setStatus("current")


class _VolOwningHost_Type(Integer32):
    """Custom type volOwningHost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("partner", 2))
    )


_VolOwningHost_Type.__name__ = "Integer32"
_VolOwningHost_Object = MibTableColumn
volOwningHost = _VolOwningHost_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 4),
    _VolOwningHost_Type()
)
volOwningHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volOwningHost.setStatus("current")
_VolState_Type = DisplayString
_VolState_Object = MibTableColumn
volState = _VolState_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 5),
    _VolState_Type()
)
volState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volState.setStatus("current")
_VolStatus_Type = DisplayString
_VolStatus_Object = MibTableColumn
volStatus = _VolStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 6),
    _VolStatus_Type()
)
volStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volStatus.setStatus("current")
_VolOptions_Type = DisplayString
_VolOptions_Object = MibTableColumn
volOptions = _VolOptions_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 7),
    _VolOptions_Type()
)
volOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volOptions.setStatus("current")
_VolUUID_Type = DisplayString
_VolUUID_Object = MibTableColumn
volUUID = _VolUUID_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 8),
    _VolUUID_Type()
)
volUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volUUID.setStatus("current")
_VolAggrName_Type = DisplayString
_VolAggrName_Object = MibTableColumn
volAggrName = _VolAggrName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 9),
    _VolAggrName_Type()
)
volAggrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volAggrName.setStatus("current")


class _VolType_Type(Integer32):
    """Custom type volType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flexible", 2),
          ("traditional", 1))
    )


_VolType_Type.__name__ = "Integer32"
_VolType_Object = MibTableColumn
volType = _VolType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 10),
    _VolType_Type()
)
volType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volType.setStatus("current")


class _VolClone_Type(Integer32):
    """Custom type volClone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VolClone_Type.__name__ = "Integer32"
_VolClone_Object = MibTableColumn
volClone = _VolClone_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 11),
    _VolClone_Type()
)
volClone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volClone.setStatus("current")
_VolCloneOf_Type = DisplayString
_VolCloneOf_Object = MibTableColumn
volCloneOf = _VolCloneOf_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 12),
    _VolCloneOf_Type()
)
volCloneOf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCloneOf.setStatus("current")
_VolCloneSnap_Type = DisplayString
_VolCloneSnap_Object = MibTableColumn
volCloneSnap = _VolCloneSnap_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 8, 1, 13),
    _VolCloneSnap_Type()
)
volCloneSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCloneSnap.setStatus("current")


class _VolNumber_Type(Integer32):
    """Custom type volNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_VolNumber_Type.__name__ = "Integer32"
_VolNumber_Object = MibScalar
volNumber = _VolNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 9),
    _VolNumber_Type()
)
volNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volNumber.setStatus("current")
_QtreeTable_Object = MibTable
qtreeTable = _QtreeTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 10)
)
if mibBuilder.loadTexts:
    qtreeTable.setStatus("current")
_QtreeEntry_Object = MibTableRow
qtreeEntry = _QtreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 10, 1)
)
qtreeEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "qtreeVolume"),
    (0, "NETWORK-APPLIANCE-MIB", "qtreeIndex"),
)
if mibBuilder.loadTexts:
    qtreeEntry.setStatus("current")


class _QtreeIndex_Type(Integer32):
    """Custom type qtreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtreeIndex_Type.__name__ = "Integer32"
_QtreeIndex_Object = MibTableColumn
qtreeIndex = _QtreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 10, 1, 1),
    _QtreeIndex_Type()
)
qtreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtreeIndex.setStatus("current")


class _QtreeVolume_Type(Integer32):
    """Custom type qtreeVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtreeVolume_Type.__name__ = "Integer32"
_QtreeVolume_Object = MibTableColumn
qtreeVolume = _QtreeVolume_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 10, 1, 2),
    _QtreeVolume_Type()
)
qtreeVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtreeVolume.setStatus("current")
_QtreeVolumeName_Type = DisplayString
_QtreeVolumeName_Object = MibTableColumn
qtreeVolumeName = _QtreeVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 10, 1, 3),
    _QtreeVolumeName_Type()
)
qtreeVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtreeVolumeName.setStatus("current")
_QtreeId_Type = Integer32
_QtreeId_Object = MibTableColumn
qtreeId = _QtreeId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 10, 1, 4),
    _QtreeId_Type()
)
qtreeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtreeId.setStatus("current")
_QtreeName_Type = DisplayString
_QtreeName_Object = MibTableColumn
qtreeName = _QtreeName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 10, 1, 5),
    _QtreeName_Type()
)
qtreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtreeName.setStatus("current")


class _QtreeStyle_Type(Integer32):
    """Custom type qtreeStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 3),
          ("ntfs", 2),
          ("unix", 1))
    )


_QtreeStyle_Type.__name__ = "Integer32"
_QtreeStyle_Object = MibTableColumn
qtreeStyle = _QtreeStyle_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 10, 1, 6),
    _QtreeStyle_Type()
)
qtreeStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtreeStyle.setStatus("current")


class _QtreeStatus_Type(Integer32):
    """Custom type qtreeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("snapmirrored", 2),
          ("snapvaulted", 3))
    )


_QtreeStatus_Type.__name__ = "Integer32"
_QtreeStatus_Object = MibTableColumn
qtreeStatus = _QtreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 10, 1, 7),
    _QtreeStatus_Type()
)
qtreeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtreeStatus.setStatus("current")


class _QtreeOplock_Type(Integer32):
    """Custom type qtreeOplock based on Integer32"""
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


_QtreeOplock_Type.__name__ = "Integer32"
_QtreeOplock_Object = MibTableColumn
qtreeOplock = _QtreeOplock_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 10, 1, 8),
    _QtreeOplock_Type()
)
qtreeOplock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtreeOplock.setStatus("current")
_AggrTable_Object = MibTable
aggrTable = _AggrTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11)
)
if mibBuilder.loadTexts:
    aggrTable.setStatus("current")
_AggrEntry_Object = MibTableRow
aggrEntry = _AggrEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11, 1)
)
aggrEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "aggrIndex"),
)
if mibBuilder.loadTexts:
    aggrEntry.setStatus("current")


class _AggrIndex_Type(Integer32):
    """Custom type aggrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_AggrIndex_Type.__name__ = "Integer32"
_AggrIndex_Object = MibTableColumn
aggrIndex = _AggrIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11, 1, 1),
    _AggrIndex_Type()
)
aggrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrIndex.setStatus("current")
_AggrName_Type = DisplayString
_AggrName_Object = MibTableColumn
aggrName = _AggrName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11, 1, 2),
    _AggrName_Type()
)
aggrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrName.setStatus("current")
_AggrFSID_Type = DisplayString
_AggrFSID_Object = MibTableColumn
aggrFSID = _AggrFSID_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11, 1, 3),
    _AggrFSID_Type()
)
aggrFSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrFSID.setStatus("current")


class _AggrOwningHost_Type(Integer32):
    """Custom type aggrOwningHost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("partner", 2))
    )


_AggrOwningHost_Type.__name__ = "Integer32"
_AggrOwningHost_Object = MibTableColumn
aggrOwningHost = _AggrOwningHost_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11, 1, 4),
    _AggrOwningHost_Type()
)
aggrOwningHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrOwningHost.setStatus("current")
_AggrState_Type = DisplayString
_AggrState_Object = MibTableColumn
aggrState = _AggrState_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11, 1, 5),
    _AggrState_Type()
)
aggrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrState.setStatus("current")
_AggrStatus_Type = DisplayString
_AggrStatus_Object = MibTableColumn
aggrStatus = _AggrStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11, 1, 6),
    _AggrStatus_Type()
)
aggrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrStatus.setStatus("current")
_AggrOptions_Type = DisplayString
_AggrOptions_Object = MibTableColumn
aggrOptions = _AggrOptions_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11, 1, 7),
    _AggrOptions_Type()
)
aggrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrOptions.setStatus("current")
_AggrUUID_Type = DisplayString
_AggrUUID_Object = MibTableColumn
aggrUUID = _AggrUUID_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11, 1, 8),
    _AggrUUID_Type()
)
aggrUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrUUID.setStatus("current")


class _AggrFlexvollist_Type(OctetString):
    """Custom type aggrFlexvollist based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AggrFlexvollist_Type.__name__ = "OctetString"
_AggrFlexvollist_Object = MibTableColumn
aggrFlexvollist = _AggrFlexvollist_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11, 1, 9),
    _AggrFlexvollist_Type()
)
aggrFlexvollist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrFlexvollist.setStatus("current")


class _AggrType_Type(Integer32):
    """Custom type aggrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 2),
          ("traditional", 1))
    )


_AggrType_Type.__name__ = "Integer32"
_AggrType_Object = MibTableColumn
aggrType = _AggrType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11, 1, 10),
    _AggrType_Type()
)
aggrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrType.setStatus("current")
_AggrRaidType_Type = DisplayString
_AggrRaidType_Object = MibTableColumn
aggrRaidType = _AggrRaidType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 11, 1, 11),
    _AggrRaidType_Type()
)
aggrRaidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrRaidType.setStatus("current")


class _AggrNumber_Type(Integer32):
    """Custom type aggrNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_AggrNumber_Type.__name__ = "Integer32"
_AggrNumber_Object = MibScalar
aggrNumber = _AggrNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 5, 12),
    _AggrNumber_Type()
)
aggrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrNumber.setStatus("current")
_Raid_ObjectIdentity = ObjectIdentity
raid = _Raid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 6)
)
_RaidTable_Object = MibTable
raidTable = _RaidTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1)
)
if mibBuilder.loadTexts:
    raidTable.setStatus("deprecated")
_RaidEntry_Object = MibTableRow
raidEntry = _RaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1, 1)
)
raidEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "raidIndex"),
)
if mibBuilder.loadTexts:
    raidEntry.setStatus("deprecated")


class _RaidIndex_Type(Integer32):
    """Custom type raidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaidIndex_Type.__name__ = "Integer32"
_RaidIndex_Object = MibTableColumn
raidIndex = _RaidIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1, 1, 1),
    _RaidIndex_Type()
)
raidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidIndex.setStatus("deprecated")
_RaidDiskName_Type = DisplayString
_RaidDiskName_Object = MibTableColumn
raidDiskName = _RaidDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1, 1, 2),
    _RaidDiskName_Type()
)
raidDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskName.setStatus("deprecated")


class _RaidStatus_Type(Integer32):
    """Custom type raidStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("addingSpare", 7),
          ("failed", 6),
          ("offline", 10),
          ("parityReconstructionInProgress", 3),
          ("parityVerificationInProgress", 4),
          ("prefailed", 9),
          ("reconstructionInProgress", 2),
          ("scrubbingInProgress", 5),
          ("spare", 8))
    )


_RaidStatus_Type.__name__ = "Integer32"
_RaidStatus_Object = MibTableColumn
raidStatus = _RaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1, 1, 3),
    _RaidStatus_Type()
)
raidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStatus.setStatus("deprecated")
_RaidDiskId_Type = Integer32
_RaidDiskId_Object = MibTableColumn
raidDiskId = _RaidDiskId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1, 1, 4),
    _RaidDiskId_Type()
)
raidDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskId.setStatus("deprecated")
_RaidScsiAdapter_Type = DisplayString
_RaidScsiAdapter_Object = MibTableColumn
raidScsiAdapter = _RaidScsiAdapter_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1, 1, 5),
    _RaidScsiAdapter_Type()
)
raidScsiAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidScsiAdapter.setStatus("deprecated")


class _RaidScsiId_Type(Integer32):
    """Custom type raidScsiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaidScsiId_Type.__name__ = "Integer32"
_RaidScsiId_Object = MibTableColumn
raidScsiId = _RaidScsiId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1, 1, 6),
    _RaidScsiId_Type()
)
raidScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidScsiId.setStatus("deprecated")
_RaidUsedMb_Type = Integer32
_RaidUsedMb_Object = MibTableColumn
raidUsedMb = _RaidUsedMb_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1, 1, 7),
    _RaidUsedMb_Type()
)
raidUsedMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidUsedMb.setStatus("deprecated")
_RaidUsedBlocks_Type = Integer32
_RaidUsedBlocks_Object = MibTableColumn
raidUsedBlocks = _RaidUsedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1, 1, 8),
    _RaidUsedBlocks_Type()
)
raidUsedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidUsedBlocks.setStatus("deprecated")
_RaidTotalMb_Type = Integer32
_RaidTotalMb_Object = MibTableColumn
raidTotalMb = _RaidTotalMb_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1, 1, 9),
    _RaidTotalMb_Type()
)
raidTotalMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidTotalMb.setStatus("deprecated")
_RaidTotalBlocks_Type = Integer32
_RaidTotalBlocks_Object = MibTableColumn
raidTotalBlocks = _RaidTotalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1, 1, 10),
    _RaidTotalBlocks_Type()
)
raidTotalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidTotalBlocks.setStatus("deprecated")


class _RaidCompletionPerCent_Type(Integer32):
    """Custom type raidCompletionPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaidCompletionPerCent_Type.__name__ = "Integer32"
_RaidCompletionPerCent_Object = MibTableColumn
raidCompletionPerCent = _RaidCompletionPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 1, 1, 11),
    _RaidCompletionPerCent_Type()
)
raidCompletionPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCompletionPerCent.setStatus("deprecated")
_RaidVTable_Object = MibTable
raidVTable = _RaidVTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2)
)
if mibBuilder.loadTexts:
    raidVTable.setStatus("current")
_RaidVEntry_Object = MibTableRow
raidVEntry = _RaidVEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1)
)
raidVEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "raidVVol"),
    (0, "NETWORK-APPLIANCE-MIB", "raidVGroup"),
    (0, "NETWORK-APPLIANCE-MIB", "raidVIndex"),
)
if mibBuilder.loadTexts:
    raidVEntry.setStatus("current")


class _RaidVIndex_Type(Integer32):
    """Custom type raidVIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaidVIndex_Type.__name__ = "Integer32"
_RaidVIndex_Object = MibTableColumn
raidVIndex = _RaidVIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 1),
    _RaidVIndex_Type()
)
raidVIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVIndex.setStatus("current")
_RaidVDiskName_Type = DisplayString
_RaidVDiskName_Object = MibTableColumn
raidVDiskName = _RaidVDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 2),
    _RaidVDiskName_Type()
)
raidVDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDiskName.setStatus("current")


class _RaidVStatus_Type(Integer32):
    """Custom type raidVStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("failed", 6),
          ("offline", 10),
          ("parityReconstructionInProgress", 3),
          ("parityVerificationInProgress", 4),
          ("prefailed", 9),
          ("reconstructionInProgress", 2),
          ("scrubbingInProgress", 5))
    )


_RaidVStatus_Type.__name__ = "Integer32"
_RaidVStatus_Object = MibTableColumn
raidVStatus = _RaidVStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 3),
    _RaidVStatus_Type()
)
raidVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVStatus.setStatus("current")
_RaidVDiskId_Type = Integer32
_RaidVDiskId_Object = MibTableColumn
raidVDiskId = _RaidVDiskId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 4),
    _RaidVDiskId_Type()
)
raidVDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDiskId.setStatus("current")
_RaidVScsiAdapter_Type = DisplayString
_RaidVScsiAdapter_Object = MibTableColumn
raidVScsiAdapter = _RaidVScsiAdapter_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 5),
    _RaidVScsiAdapter_Type()
)
raidVScsiAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVScsiAdapter.setStatus("current")


class _RaidVScsiId_Type(Integer32):
    """Custom type raidVScsiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaidVScsiId_Type.__name__ = "Integer32"
_RaidVScsiId_Object = MibTableColumn
raidVScsiId = _RaidVScsiId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 6),
    _RaidVScsiId_Type()
)
raidVScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVScsiId.setStatus("current")
_RaidVUsedMb_Type = Integer32
_RaidVUsedMb_Object = MibTableColumn
raidVUsedMb = _RaidVUsedMb_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 7),
    _RaidVUsedMb_Type()
)
raidVUsedMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVUsedMb.setStatus("current")
_RaidVUsedBlocks_Type = Integer32
_RaidVUsedBlocks_Object = MibTableColumn
raidVUsedBlocks = _RaidVUsedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 8),
    _RaidVUsedBlocks_Type()
)
raidVUsedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVUsedBlocks.setStatus("current")
_RaidVTotalMb_Type = Integer32
_RaidVTotalMb_Object = MibTableColumn
raidVTotalMb = _RaidVTotalMb_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 9),
    _RaidVTotalMb_Type()
)
raidVTotalMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVTotalMb.setStatus("current")
_RaidVTotalBlocks_Type = Integer32
_RaidVTotalBlocks_Object = MibTableColumn
raidVTotalBlocks = _RaidVTotalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 10),
    _RaidVTotalBlocks_Type()
)
raidVTotalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVTotalBlocks.setStatus("current")


class _RaidVCompletionPerCent_Type(Integer32):
    """Custom type raidVCompletionPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaidVCompletionPerCent_Type.__name__ = "Integer32"
_RaidVCompletionPerCent_Object = MibTableColumn
raidVCompletionPerCent = _RaidVCompletionPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 11),
    _RaidVCompletionPerCent_Type()
)
raidVCompletionPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVCompletionPerCent.setStatus("current")


class _RaidVVol_Type(Integer32):
    """Custom type raidVVol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaidVVol_Type.__name__ = "Integer32"
_RaidVVol_Object = MibTableColumn
raidVVol = _RaidVVol_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 12),
    _RaidVVol_Type()
)
raidVVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVVol.setStatus("current")


class _RaidVGroup_Type(Integer32):
    """Custom type raidVGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaidVGroup_Type.__name__ = "Integer32"
_RaidVGroup_Object = MibTableColumn
raidVGroup = _RaidVGroup_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 13),
    _RaidVGroup_Type()
)
raidVGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVGroup.setStatus("current")
_RaidVDiskNumber_Type = Integer32
_RaidVDiskNumber_Object = MibTableColumn
raidVDiskNumber = _RaidVDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 14),
    _RaidVDiskNumber_Type()
)
raidVDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDiskNumber.setStatus("current")
_RaidVGroupNumber_Type = Integer32
_RaidVGroupNumber_Object = MibTableColumn
raidVGroupNumber = _RaidVGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 15),
    _RaidVGroupNumber_Type()
)
raidVGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVGroupNumber.setStatus("current")


class _RaidVDiskPort_Type(Integer32):
    """Custom type raidVDiskPort based on Integer32"""
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
        *(("portA", 1),
          ("portB", 2),
          ("portNone", 4),
          ("portSingle", 3))
    )


_RaidVDiskPort_Type.__name__ = "Integer32"
_RaidVDiskPort_Object = MibTableColumn
raidVDiskPort = _RaidVDiskPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 16),
    _RaidVDiskPort_Type()
)
raidVDiskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDiskPort.setStatus("current")
_RaidVSecondaryDiskName_Type = DisplayString
_RaidVSecondaryDiskName_Object = MibTableColumn
raidVSecondaryDiskName = _RaidVSecondaryDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 17),
    _RaidVSecondaryDiskName_Type()
)
raidVSecondaryDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVSecondaryDiskName.setStatus("current")


class _RaidVSecondaryDiskPort_Type(Integer32):
    """Custom type raidVSecondaryDiskPort based on Integer32"""
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
        *(("portA", 1),
          ("portB", 2),
          ("portNone", 4),
          ("portSingle", 3))
    )


_RaidVSecondaryDiskPort_Type.__name__ = "Integer32"
_RaidVSecondaryDiskPort_Object = MibTableColumn
raidVSecondaryDiskPort = _RaidVSecondaryDiskPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 18),
    _RaidVSecondaryDiskPort_Type()
)
raidVSecondaryDiskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVSecondaryDiskPort.setStatus("current")
_RaidVShelf_Type = Integer32
_RaidVShelf_Object = MibTableColumn
raidVShelf = _RaidVShelf_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 19),
    _RaidVShelf_Type()
)
raidVShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVShelf.setStatus("current")
_RaidVBay_Type = Integer32
_RaidVBay_Object = MibTableColumn
raidVBay = _RaidVBay_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 20),
    _RaidVBay_Type()
)
raidVBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVBay.setStatus("current")
_RaidVPlex_Type = Integer32
_RaidVPlex_Object = MibTableColumn
raidVPlex = _RaidVPlex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 21),
    _RaidVPlex_Type()
)
raidVPlex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVPlex.setStatus("current")
_RaidVPlexGroup_Type = Integer32
_RaidVPlexGroup_Object = MibTableColumn
raidVPlexGroup = _RaidVPlexGroup_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 22),
    _RaidVPlexGroup_Type()
)
raidVPlexGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVPlexGroup.setStatus("current")


class _RaidVPlexNumber_Type(Integer32):
    """Custom type raidVPlexNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RaidVPlexNumber_Type.__name__ = "Integer32"
_RaidVPlexNumber_Object = MibTableColumn
raidVPlexNumber = _RaidVPlexNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 23),
    _RaidVPlexNumber_Type()
)
raidVPlexNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVPlexNumber.setStatus("current")
_RaidVPlexName_Type = DisplayString
_RaidVPlexName_Object = MibTableColumn
raidVPlexName = _RaidVPlexName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 24),
    _RaidVPlexName_Type()
)
raidVPlexName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVPlexName.setStatus("current")
_RaidVSectorSize_Type = Integer32
_RaidVSectorSize_Object = MibTableColumn
raidVSectorSize = _RaidVSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 25),
    _RaidVSectorSize_Type()
)
raidVSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVSectorSize.setStatus("current")
_RaidVDiskSerialNumber_Type = DisplayString
_RaidVDiskSerialNumber_Object = MibTableColumn
raidVDiskSerialNumber = _RaidVDiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 26),
    _RaidVDiskSerialNumber_Type()
)
raidVDiskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDiskSerialNumber.setStatus("current")
_RaidVDiskVendor_Type = DisplayString
_RaidVDiskVendor_Object = MibTableColumn
raidVDiskVendor = _RaidVDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 27),
    _RaidVDiskVendor_Type()
)
raidVDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDiskVendor.setStatus("current")
_RaidVDiskModel_Type = DisplayString
_RaidVDiskModel_Object = MibTableColumn
raidVDiskModel = _RaidVDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 28),
    _RaidVDiskModel_Type()
)
raidVDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDiskModel.setStatus("current")
_RaidVDiskFirmwareRevision_Type = DisplayString
_RaidVDiskFirmwareRevision_Object = MibTableColumn
raidVDiskFirmwareRevision = _RaidVDiskFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 29),
    _RaidVDiskFirmwareRevision_Type()
)
raidVDiskFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDiskFirmwareRevision.setStatus("current")
_RaidVDiskRPM_Type = DisplayString
_RaidVDiskRPM_Object = MibTableColumn
raidVDiskRPM = _RaidVDiskRPM_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 30),
    _RaidVDiskRPM_Type()
)
raidVDiskRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDiskRPM.setStatus("current")
_RaidVDiskType_Type = DisplayString
_RaidVDiskType_Object = MibTableColumn
raidVDiskType = _RaidVDiskType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 31),
    _RaidVDiskType_Type()
)
raidVDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDiskType.setStatus("current")
_RaidVDiskPool_Type = DisplayString
_RaidVDiskPool_Object = MibTableColumn
raidVDiskPool = _RaidVDiskPool_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 32),
    _RaidVDiskPool_Type()
)
raidVDiskPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDiskPool.setStatus("current")
_RaidVDiskCopyDestDiskName_Type = DisplayString
_RaidVDiskCopyDestDiskName_Object = MibTableColumn
raidVDiskCopyDestDiskName = _RaidVDiskCopyDestDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 2, 1, 33),
    _RaidVDiskCopyDestDiskName_Type()
)
raidVDiskCopyDestDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVDiskCopyDestDiskName.setStatus("current")
_SpareTable_Object = MibTable
spareTable = _SpareTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3)
)
if mibBuilder.loadTexts:
    spareTable.setStatus("current")
_SpareEntry_Object = MibTableRow
spareEntry = _SpareEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1)
)
spareEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "spareIndex"),
)
if mibBuilder.loadTexts:
    spareEntry.setStatus("current")


class _SpareIndex_Type(Integer32):
    """Custom type spareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SpareIndex_Type.__name__ = "Integer32"
_SpareIndex_Object = MibTableColumn
spareIndex = _SpareIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 1),
    _SpareIndex_Type()
)
spareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareIndex.setStatus("current")
_SpareDiskName_Type = DisplayString
_SpareDiskName_Object = MibTableColumn
spareDiskName = _SpareDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 2),
    _SpareDiskName_Type()
)
spareDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareDiskName.setStatus("current")


class _SpareStatus_Type(Integer32):
    """Custom type spareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("addingspare", 2),
          ("bypassed", 3),
          ("offline", 10),
          ("spare", 1),
          ("unknown", 4))
    )


_SpareStatus_Type.__name__ = "Integer32"
_SpareStatus_Object = MibTableColumn
spareStatus = _SpareStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 3),
    _SpareStatus_Type()
)
spareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareStatus.setStatus("current")
_SpareDiskId_Type = Integer32
_SpareDiskId_Object = MibTableColumn
spareDiskId = _SpareDiskId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 4),
    _SpareDiskId_Type()
)
spareDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareDiskId.setStatus("current")
_SpareScsiAdapter_Type = DisplayString
_SpareScsiAdapter_Object = MibTableColumn
spareScsiAdapter = _SpareScsiAdapter_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 5),
    _SpareScsiAdapter_Type()
)
spareScsiAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareScsiAdapter.setStatus("current")


class _SpareScsiId_Type(Integer32):
    """Custom type spareScsiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SpareScsiId_Type.__name__ = "Integer32"
_SpareScsiId_Object = MibTableColumn
spareScsiId = _SpareScsiId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 6),
    _SpareScsiId_Type()
)
spareScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareScsiId.setStatus("current")
_SpareTotalMb_Type = Integer32
_SpareTotalMb_Object = MibTableColumn
spareTotalMb = _SpareTotalMb_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 7),
    _SpareTotalMb_Type()
)
spareTotalMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareTotalMb.setStatus("current")
_SpareTotalBlocks_Type = Integer32
_SpareTotalBlocks_Object = MibTableColumn
spareTotalBlocks = _SpareTotalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 8),
    _SpareTotalBlocks_Type()
)
spareTotalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareTotalBlocks.setStatus("current")


class _SpareDiskPort_Type(Integer32):
    """Custom type spareDiskPort based on Integer32"""
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
        *(("portA", 1),
          ("portB", 2),
          ("portNone", 4),
          ("portSingle", 3))
    )


_SpareDiskPort_Type.__name__ = "Integer32"
_SpareDiskPort_Object = MibTableColumn
spareDiskPort = _SpareDiskPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 9),
    _SpareDiskPort_Type()
)
spareDiskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareDiskPort.setStatus("current")
_SpareSecondaryDiskName_Type = DisplayString
_SpareSecondaryDiskName_Object = MibTableColumn
spareSecondaryDiskName = _SpareSecondaryDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 10),
    _SpareSecondaryDiskName_Type()
)
spareSecondaryDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareSecondaryDiskName.setStatus("current")


class _SpareSecondaryDiskPort_Type(Integer32):
    """Custom type spareSecondaryDiskPort based on Integer32"""
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
        *(("portA", 1),
          ("portB", 2),
          ("portNone", 4),
          ("portSingle", 3))
    )


_SpareSecondaryDiskPort_Type.__name__ = "Integer32"
_SpareSecondaryDiskPort_Object = MibTableColumn
spareSecondaryDiskPort = _SpareSecondaryDiskPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 11),
    _SpareSecondaryDiskPort_Type()
)
spareSecondaryDiskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareSecondaryDiskPort.setStatus("current")
_SpareShelf_Type = Integer32
_SpareShelf_Object = MibTableColumn
spareShelf = _SpareShelf_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 12),
    _SpareShelf_Type()
)
spareShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareShelf.setStatus("current")
_SpareBay_Type = Integer32
_SpareBay_Object = MibTableColumn
spareBay = _SpareBay_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 13),
    _SpareBay_Type()
)
spareBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareBay.setStatus("current")
_SparePool_Type = DisplayString
_SparePool_Object = MibTableColumn
sparePool = _SparePool_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 14),
    _SparePool_Type()
)
sparePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparePool.setStatus("current")
_SpareSectorSize_Type = Integer32
_SpareSectorSize_Object = MibTableColumn
spareSectorSize = _SpareSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 15),
    _SpareSectorSize_Type()
)
spareSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareSectorSize.setStatus("current")
_SpareDiskSerialNumber_Type = DisplayString
_SpareDiskSerialNumber_Object = MibTableColumn
spareDiskSerialNumber = _SpareDiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 16),
    _SpareDiskSerialNumber_Type()
)
spareDiskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareDiskSerialNumber.setStatus("current")
_SpareDiskVendor_Type = DisplayString
_SpareDiskVendor_Object = MibTableColumn
spareDiskVendor = _SpareDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 17),
    _SpareDiskVendor_Type()
)
spareDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareDiskVendor.setStatus("current")
_SpareDiskModel_Type = DisplayString
_SpareDiskModel_Object = MibTableColumn
spareDiskModel = _SpareDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 18),
    _SpareDiskModel_Type()
)
spareDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareDiskModel.setStatus("current")
_SpareDiskFirmwareRevision_Type = DisplayString
_SpareDiskFirmwareRevision_Object = MibTableColumn
spareDiskFirmwareRevision = _SpareDiskFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 19),
    _SpareDiskFirmwareRevision_Type()
)
spareDiskFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareDiskFirmwareRevision.setStatus("current")
_SpareDiskRPM_Type = DisplayString
_SpareDiskRPM_Object = MibTableColumn
spareDiskRPM = _SpareDiskRPM_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 20),
    _SpareDiskRPM_Type()
)
spareDiskRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareDiskRPM.setStatus("current")
_SpareDiskType_Type = DisplayString
_SpareDiskType_Object = MibTableColumn
spareDiskType = _SpareDiskType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 3, 1, 21),
    _SpareDiskType_Type()
)
spareDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareDiskType.setStatus("current")
_DiskSummary_ObjectIdentity = ObjectIdentity
diskSummary = _DiskSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 4)
)
_DiskTotalCount_Type = Integer32
_DiskTotalCount_Object = MibScalar
diskTotalCount = _DiskTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 4, 1),
    _DiskTotalCount_Type()
)
diskTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotalCount.setStatus("current")
_DiskActiveCount_Type = Integer32
_DiskActiveCount_Object = MibScalar
diskActiveCount = _DiskActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 4, 2),
    _DiskActiveCount_Type()
)
diskActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskActiveCount.setStatus("current")
_DiskReconstructingCount_Type = Integer32
_DiskReconstructingCount_Object = MibScalar
diskReconstructingCount = _DiskReconstructingCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 4, 3),
    _DiskReconstructingCount_Type()
)
diskReconstructingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReconstructingCount.setStatus("current")
_DiskReconstructingParityCount_Type = Integer32
_DiskReconstructingParityCount_Object = MibScalar
diskReconstructingParityCount = _DiskReconstructingParityCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 4, 4),
    _DiskReconstructingParityCount_Type()
)
diskReconstructingParityCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReconstructingParityCount.setStatus("current")
_DiskVerifyingParityCount_Type = Integer32
_DiskVerifyingParityCount_Object = MibScalar
diskVerifyingParityCount = _DiskVerifyingParityCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 4, 5),
    _DiskVerifyingParityCount_Type()
)
diskVerifyingParityCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVerifyingParityCount.setStatus("current")
_DiskScrubbingCount_Type = Integer32
_DiskScrubbingCount_Object = MibScalar
diskScrubbingCount = _DiskScrubbingCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 4, 6),
    _DiskScrubbingCount_Type()
)
diskScrubbingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskScrubbingCount.setStatus("current")
_DiskFailedCount_Type = Integer32
_DiskFailedCount_Object = MibScalar
diskFailedCount = _DiskFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 4, 7),
    _DiskFailedCount_Type()
)
diskFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFailedCount.setStatus("current")
_DiskSpareCount_Type = Integer32
_DiskSpareCount_Object = MibScalar
diskSpareCount = _DiskSpareCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 4, 8),
    _DiskSpareCount_Type()
)
diskSpareCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSpareCount.setStatus("current")
_DiskAddingSpareCount_Type = Integer32
_DiskAddingSpareCount_Object = MibScalar
diskAddingSpareCount = _DiskAddingSpareCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 4, 9),
    _DiskAddingSpareCount_Type()
)
diskAddingSpareCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskAddingSpareCount.setStatus("current")
_DiskFailedMessage_Type = DisplayString
_DiskFailedMessage_Object = MibScalar
diskFailedMessage = _DiskFailedMessage_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 4, 10),
    _DiskFailedMessage_Type()
)
diskFailedMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFailedMessage.setStatus("current")
_DiskPrefailedCount_Type = Integer32
_DiskPrefailedCount_Object = MibScalar
diskPrefailedCount = _DiskPrefailedCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 4, 11),
    _DiskPrefailedCount_Type()
)
diskPrefailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPrefailedCount.setStatus("current")
_RaidVNumber_Type = Integer32
_RaidVNumber_Object = MibScalar
raidVNumber = _RaidVNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 5),
    _RaidVNumber_Type()
)
raidVNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVNumber.setStatus("current")
_SpareNumber_Type = Integer32
_SpareNumber_Object = MibScalar
spareNumber = _SpareNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 6),
    _SpareNumber_Type()
)
spareNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareNumber.setStatus("current")
_OtherDiskNumber_Type = Integer32
_OtherDiskNumber_Object = MibScalar
otherDiskNumber = _OtherDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 7),
    _OtherDiskNumber_Type()
)
otherDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskNumber.setStatus("current")
_RaidPNumber_Type = Integer32
_RaidPNumber_Object = MibScalar
raidPNumber = _RaidPNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 8),
    _RaidPNumber_Type()
)
raidPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPNumber.setStatus("current")
_OtherDiskTable_Object = MibTable
otherDiskTable = _OtherDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9)
)
if mibBuilder.loadTexts:
    otherDiskTable.setStatus("current")
_OtherDiskEntry_Object = MibTableRow
otherDiskEntry = _OtherDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1)
)
otherDiskEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "otherDiskIndex"),
)
if mibBuilder.loadTexts:
    otherDiskEntry.setStatus("current")


class _OtherDiskIndex_Type(Integer32):
    """Custom type otherDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OtherDiskIndex_Type.__name__ = "Integer32"
_OtherDiskIndex_Object = MibTableColumn
otherDiskIndex = _OtherDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 1),
    _OtherDiskIndex_Type()
)
otherDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskIndex.setStatus("current")
_OtherDiskDiskName_Type = DisplayString
_OtherDiskDiskName_Object = MibTableColumn
otherDiskDiskName = _OtherDiskDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 2),
    _OtherDiskDiskName_Type()
)
otherDiskDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskDiskName.setStatus("current")


class _OtherDiskStatus_Type(Integer32):
    """Custom type otherDiskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broken", 1),
          ("bypassed", 2),
          ("unknown", 3))
    )


_OtherDiskStatus_Type.__name__ = "Integer32"
_OtherDiskStatus_Object = MibTableColumn
otherDiskStatus = _OtherDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 3),
    _OtherDiskStatus_Type()
)
otherDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskStatus.setStatus("current")
_OtherDiskDiskId_Type = Integer32
_OtherDiskDiskId_Object = MibTableColumn
otherDiskDiskId = _OtherDiskDiskId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 4),
    _OtherDiskDiskId_Type()
)
otherDiskDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskDiskId.setStatus("current")
_OtherDiskScsiAdapter_Type = DisplayString
_OtherDiskScsiAdapter_Object = MibTableColumn
otherDiskScsiAdapter = _OtherDiskScsiAdapter_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 5),
    _OtherDiskScsiAdapter_Type()
)
otherDiskScsiAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskScsiAdapter.setStatus("current")


class _OtherDiskScsiId_Type(Integer32):
    """Custom type otherDiskScsiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OtherDiskScsiId_Type.__name__ = "Integer32"
_OtherDiskScsiId_Object = MibTableColumn
otherDiskScsiId = _OtherDiskScsiId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 6),
    _OtherDiskScsiId_Type()
)
otherDiskScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskScsiId.setStatus("current")
_OtherDiskTotalMb_Type = Integer32
_OtherDiskTotalMb_Object = MibTableColumn
otherDiskTotalMb = _OtherDiskTotalMb_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 7),
    _OtherDiskTotalMb_Type()
)
otherDiskTotalMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskTotalMb.setStatus("current")
_OtherDiskTotalBlocks_Type = Integer32
_OtherDiskTotalBlocks_Object = MibTableColumn
otherDiskTotalBlocks = _OtherDiskTotalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 8),
    _OtherDiskTotalBlocks_Type()
)
otherDiskTotalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskTotalBlocks.setStatus("current")


class _OtherDiskDiskPort_Type(Integer32):
    """Custom type otherDiskDiskPort based on Integer32"""
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
        *(("portA", 1),
          ("portB", 2),
          ("portNone", 4),
          ("portSingle", 3))
    )


_OtherDiskDiskPort_Type.__name__ = "Integer32"
_OtherDiskDiskPort_Object = MibTableColumn
otherDiskDiskPort = _OtherDiskDiskPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 9),
    _OtherDiskDiskPort_Type()
)
otherDiskDiskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskDiskPort.setStatus("current")
_OtherDiskSecondaryDiskName_Type = DisplayString
_OtherDiskSecondaryDiskName_Object = MibTableColumn
otherDiskSecondaryDiskName = _OtherDiskSecondaryDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 10),
    _OtherDiskSecondaryDiskName_Type()
)
otherDiskSecondaryDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskSecondaryDiskName.setStatus("current")


class _OtherDiskSecondaryDiskPort_Type(Integer32):
    """Custom type otherDiskSecondaryDiskPort based on Integer32"""
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
        *(("portA", 1),
          ("portB", 2),
          ("portNone", 4),
          ("portSingle", 3))
    )


_OtherDiskSecondaryDiskPort_Type.__name__ = "Integer32"
_OtherDiskSecondaryDiskPort_Object = MibTableColumn
otherDiskSecondaryDiskPort = _OtherDiskSecondaryDiskPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 11),
    _OtherDiskSecondaryDiskPort_Type()
)
otherDiskSecondaryDiskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskSecondaryDiskPort.setStatus("current")
_OtherDiskShelf_Type = Integer32
_OtherDiskShelf_Object = MibTableColumn
otherDiskShelf = _OtherDiskShelf_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 12),
    _OtherDiskShelf_Type()
)
otherDiskShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskShelf.setStatus("current")
_OtherDiskBay_Type = Integer32
_OtherDiskBay_Object = MibTableColumn
otherDiskBay = _OtherDiskBay_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 13),
    _OtherDiskBay_Type()
)
otherDiskBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskBay.setStatus("current")
_OtherDiskPool_Type = DisplayString
_OtherDiskPool_Object = MibTableColumn
otherDiskPool = _OtherDiskPool_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 14),
    _OtherDiskPool_Type()
)
otherDiskPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskPool.setStatus("current")
_OtherDiskSectorSize_Type = Integer32
_OtherDiskSectorSize_Object = MibTableColumn
otherDiskSectorSize = _OtherDiskSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 15),
    _OtherDiskSectorSize_Type()
)
otherDiskSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskSectorSize.setStatus("current")
_OtherDiskSerialNumber_Type = DisplayString
_OtherDiskSerialNumber_Object = MibTableColumn
otherDiskSerialNumber = _OtherDiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 16),
    _OtherDiskSerialNumber_Type()
)
otherDiskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskSerialNumber.setStatus("current")
_OtherDiskVendor_Type = DisplayString
_OtherDiskVendor_Object = MibTableColumn
otherDiskVendor = _OtherDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 17),
    _OtherDiskVendor_Type()
)
otherDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskVendor.setStatus("current")
_OtherDiskModel_Type = DisplayString
_OtherDiskModel_Object = MibTableColumn
otherDiskModel = _OtherDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 18),
    _OtherDiskModel_Type()
)
otherDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskModel.setStatus("current")
_OtherDiskFirmwareRevision_Type = DisplayString
_OtherDiskFirmwareRevision_Object = MibTableColumn
otherDiskFirmwareRevision = _OtherDiskFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 19),
    _OtherDiskFirmwareRevision_Type()
)
otherDiskFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskFirmwareRevision.setStatus("current")
_OtherDiskRPM_Type = DisplayString
_OtherDiskRPM_Object = MibTableColumn
otherDiskRPM = _OtherDiskRPM_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 20),
    _OtherDiskRPM_Type()
)
otherDiskRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskRPM.setStatus("current")
_OtherDiskType_Type = DisplayString
_OtherDiskType_Object = MibTableColumn
otherDiskType = _OtherDiskType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 9, 1, 21),
    _OtherDiskType_Type()
)
otherDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherDiskType.setStatus("current")
_RaidPTable_Object = MibTable
raidPTable = _RaidPTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10)
)
if mibBuilder.loadTexts:
    raidPTable.setStatus("current")
_RaidPEntry_Object = MibTableRow
raidPEntry = _RaidPEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1)
)
raidPEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "raidPVol"),
    (0, "NETWORK-APPLIANCE-MIB", "raidPPlex"),
    (0, "NETWORK-APPLIANCE-MIB", "raidPGroup"),
    (0, "NETWORK-APPLIANCE-MIB", "raidPIndex"),
)
if mibBuilder.loadTexts:
    raidPEntry.setStatus("current")


class _RaidPIndex_Type(Integer32):
    """Custom type raidPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaidPIndex_Type.__name__ = "Integer32"
_RaidPIndex_Object = MibTableColumn
raidPIndex = _RaidPIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 1),
    _RaidPIndex_Type()
)
raidPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPIndex.setStatus("current")


class _RaidPStatus_Type(Integer32):
    """Custom type raidPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("failed", 6),
          ("offline", 10),
          ("parityReconstructionInProgress", 3),
          ("parityVerificationInProgress", 4),
          ("prefailed", 9),
          ("reconstructionInProgress", 2),
          ("scrubbingInProgress", 5))
    )


_RaidPStatus_Type.__name__ = "Integer32"
_RaidPStatus_Object = MibTableColumn
raidPStatus = _RaidPStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 2),
    _RaidPStatus_Type()
)
raidPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPStatus.setStatus("current")


class _RaidPVol_Type(Integer32):
    """Custom type raidPVol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaidPVol_Type.__name__ = "Integer32"
_RaidPVol_Object = MibTableColumn
raidPVol = _RaidPVol_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 3),
    _RaidPVol_Type()
)
raidPVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPVol.setStatus("current")


class _RaidPPlex_Type(Integer32):
    """Custom type raidPPlex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaidPPlex_Type.__name__ = "Integer32"
_RaidPPlex_Object = MibTableColumn
raidPPlex = _RaidPPlex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 4),
    _RaidPPlex_Type()
)
raidPPlex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPPlex.setStatus("current")


class _RaidPGroup_Type(Integer32):
    """Custom type raidPGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaidPGroup_Type.__name__ = "Integer32"
_RaidPGroup_Object = MibTableColumn
raidPGroup = _RaidPGroup_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 5),
    _RaidPGroup_Type()
)
raidPGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPGroup.setStatus("current")


class _RaidPPlexNumber_Type(Integer32):
    """Custom type raidPPlexNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RaidPPlexNumber_Type.__name__ = "Integer32"
_RaidPPlexNumber_Object = MibTableColumn
raidPPlexNumber = _RaidPPlexNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 6),
    _RaidPPlexNumber_Type()
)
raidPPlexNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPPlexNumber.setStatus("current")
_RaidPGroupNumber_Type = Integer32
_RaidPGroupNumber_Object = MibTableColumn
raidPGroupNumber = _RaidPGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 7),
    _RaidPGroupNumber_Type()
)
raidPGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPGroupNumber.setStatus("current")


class _RaidPDiskNumber_Type(Integer32):
    """Custom type raidPDiskNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RaidPDiskNumber_Type.__name__ = "Integer32"
_RaidPDiskNumber_Object = MibTableColumn
raidPDiskNumber = _RaidPDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 8),
    _RaidPDiskNumber_Type()
)
raidPDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDiskNumber.setStatus("current")
_RaidPPlexName_Type = DisplayString
_RaidPPlexName_Object = MibTableColumn
raidPPlexName = _RaidPPlexName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 9),
    _RaidPPlexName_Type()
)
raidPPlexName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPPlexName.setStatus("current")
_RaidPDiskName_Type = DisplayString
_RaidPDiskName_Object = MibTableColumn
raidPDiskName = _RaidPDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 10),
    _RaidPDiskName_Type()
)
raidPDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDiskName.setStatus("current")


class _RaidPDiskPort_Type(Integer32):
    """Custom type raidPDiskPort based on Integer32"""
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
        *(("portA", 1),
          ("portB", 2),
          ("portNone", 4),
          ("portSingle", 3))
    )


_RaidPDiskPort_Type.__name__ = "Integer32"
_RaidPDiskPort_Object = MibTableColumn
raidPDiskPort = _RaidPDiskPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 11),
    _RaidPDiskPort_Type()
)
raidPDiskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDiskPort.setStatus("current")
_RaidPSecondaryDiskName_Type = DisplayString
_RaidPSecondaryDiskName_Object = MibTableColumn
raidPSecondaryDiskName = _RaidPSecondaryDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 12),
    _RaidPSecondaryDiskName_Type()
)
raidPSecondaryDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPSecondaryDiskName.setStatus("current")


class _RaidPSecondaryDiskPort_Type(Integer32):
    """Custom type raidPSecondaryDiskPort based on Integer32"""
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
        *(("portA", 1),
          ("portB", 2),
          ("portNone", 4),
          ("portSingle", 3))
    )


_RaidPSecondaryDiskPort_Type.__name__ = "Integer32"
_RaidPSecondaryDiskPort_Object = MibTableColumn
raidPSecondaryDiskPort = _RaidPSecondaryDiskPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 13),
    _RaidPSecondaryDiskPort_Type()
)
raidPSecondaryDiskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPSecondaryDiskPort.setStatus("current")
_RaidPScsiAdapter_Type = DisplayString
_RaidPScsiAdapter_Object = MibTableColumn
raidPScsiAdapter = _RaidPScsiAdapter_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 14),
    _RaidPScsiAdapter_Type()
)
raidPScsiAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPScsiAdapter.setStatus("current")


class _RaidPScsiId_Type(Integer32):
    """Custom type raidPScsiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaidPScsiId_Type.__name__ = "Integer32"
_RaidPScsiId_Object = MibTableColumn
raidPScsiId = _RaidPScsiId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 15),
    _RaidPScsiId_Type()
)
raidPScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPScsiId.setStatus("current")
_RaidPDiskId_Type = Integer32
_RaidPDiskId_Object = MibTableColumn
raidPDiskId = _RaidPDiskId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 16),
    _RaidPDiskId_Type()
)
raidPDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDiskId.setStatus("current")
_RaidPShelf_Type = Integer32
_RaidPShelf_Object = MibTableColumn
raidPShelf = _RaidPShelf_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 17),
    _RaidPShelf_Type()
)
raidPShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPShelf.setStatus("current")
_RaidPBay_Type = Integer32
_RaidPBay_Object = MibTableColumn
raidPBay = _RaidPBay_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 18),
    _RaidPBay_Type()
)
raidPBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPBay.setStatus("current")
_RaidPSectorSize_Type = Integer32
_RaidPSectorSize_Object = MibTableColumn
raidPSectorSize = _RaidPSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 19),
    _RaidPSectorSize_Type()
)
raidPSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPSectorSize.setStatus("current")
_RaidPUsedMb_Type = Integer32
_RaidPUsedMb_Object = MibTableColumn
raidPUsedMb = _RaidPUsedMb_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 20),
    _RaidPUsedMb_Type()
)
raidPUsedMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPUsedMb.setStatus("current")
_RaidPUsedBlocks_Type = Integer32
_RaidPUsedBlocks_Object = MibTableColumn
raidPUsedBlocks = _RaidPUsedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 21),
    _RaidPUsedBlocks_Type()
)
raidPUsedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPUsedBlocks.setStatus("current")
_RaidPTotalMb_Type = Integer32
_RaidPTotalMb_Object = MibTableColumn
raidPTotalMb = _RaidPTotalMb_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 22),
    _RaidPTotalMb_Type()
)
raidPTotalMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPTotalMb.setStatus("current")
_RaidPTotalBlocks_Type = Integer32
_RaidPTotalBlocks_Object = MibTableColumn
raidPTotalBlocks = _RaidPTotalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 23),
    _RaidPTotalBlocks_Type()
)
raidPTotalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPTotalBlocks.setStatus("current")


class _RaidPCompletionPerCent_Type(Integer32):
    """Custom type raidPCompletionPerCent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaidPCompletionPerCent_Type.__name__ = "Integer32"
_RaidPCompletionPerCent_Object = MibTableColumn
raidPCompletionPerCent = _RaidPCompletionPerCent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 24),
    _RaidPCompletionPerCent_Type()
)
raidPCompletionPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPCompletionPerCent.setStatus("current")
_RaidPDiskSerialNumber_Type = DisplayString
_RaidPDiskSerialNumber_Object = MibTableColumn
raidPDiskSerialNumber = _RaidPDiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 25),
    _RaidPDiskSerialNumber_Type()
)
raidPDiskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDiskSerialNumber.setStatus("current")
_RaidPDiskVendor_Type = DisplayString
_RaidPDiskVendor_Object = MibTableColumn
raidPDiskVendor = _RaidPDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 26),
    _RaidPDiskVendor_Type()
)
raidPDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDiskVendor.setStatus("current")
_RaidPDiskModel_Type = DisplayString
_RaidPDiskModel_Object = MibTableColumn
raidPDiskModel = _RaidPDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 27),
    _RaidPDiskModel_Type()
)
raidPDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDiskModel.setStatus("current")
_RaidPDiskFirmwareRevision_Type = DisplayString
_RaidPDiskFirmwareRevision_Object = MibTableColumn
raidPDiskFirmwareRevision = _RaidPDiskFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 28),
    _RaidPDiskFirmwareRevision_Type()
)
raidPDiskFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDiskFirmwareRevision.setStatus("current")
_RaidPDiskRPM_Type = DisplayString
_RaidPDiskRPM_Object = MibTableColumn
raidPDiskRPM = _RaidPDiskRPM_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 29),
    _RaidPDiskRPM_Type()
)
raidPDiskRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDiskRPM.setStatus("current")
_RaidPDiskType_Type = DisplayString
_RaidPDiskType_Object = MibTableColumn
raidPDiskType = _RaidPDiskType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 30),
    _RaidPDiskType_Type()
)
raidPDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDiskType.setStatus("current")
_RaidPDiskPool_Type = DisplayString
_RaidPDiskPool_Object = MibTableColumn
raidPDiskPool = _RaidPDiskPool_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 31),
    _RaidPDiskPool_Type()
)
raidPDiskPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDiskPool.setStatus("current")
_RaidPDiskCopyDestDiskName_Type = DisplayString
_RaidPDiskCopyDestDiskName_Object = MibTableColumn
raidPDiskCopyDestDiskName = _RaidPDiskCopyDestDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 10, 1, 32),
    _RaidPDiskCopyDestDiskName_Type()
)
raidPDiskCopyDestDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidPDiskCopyDestDiskName.setStatus("current")
_PlexTable_Object = MibTable
plexTable = _PlexTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 11)
)
if mibBuilder.loadTexts:
    plexTable.setStatus("current")
_PlexEntry_Object = MibTableRow
plexEntry = _PlexEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 11, 1)
)
plexEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "plexIndex"),
)
if mibBuilder.loadTexts:
    plexEntry.setStatus("current")


class _PlexIndex_Type(Integer32):
    """Custom type plexIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PlexIndex_Type.__name__ = "Integer32"
_PlexIndex_Object = MibTableColumn
plexIndex = _PlexIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 11, 1, 1),
    _PlexIndex_Type()
)
plexIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plexIndex.setStatus("current")
_PlexName_Type = DisplayString
_PlexName_Object = MibTableColumn
plexName = _PlexName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 11, 1, 2),
    _PlexName_Type()
)
plexName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plexName.setStatus("current")
_PlexVolName_Type = DisplayString
_PlexVolName_Object = MibTableColumn
plexVolName = _PlexVolName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 11, 1, 3),
    _PlexVolName_Type()
)
plexVolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plexVolName.setStatus("current")


class _PlexStatus_Type(Integer32):
    """Custom type plexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 3),
          ("resyncing", 2))
    )


_PlexStatus_Type.__name__ = "Integer32"
_PlexStatus_Object = MibTableColumn
plexStatus = _PlexStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 11, 1, 4),
    _PlexStatus_Type()
)
plexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plexStatus.setStatus("current")
_PlexPercentResyncing_Type = Integer32
_PlexPercentResyncing_Object = MibTableColumn
plexPercentResyncing = _PlexPercentResyncing_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 11, 1, 5),
    _PlexPercentResyncing_Type()
)
plexPercentResyncing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plexPercentResyncing.setStatus("current")
_OutOfDateDiskCount_Type = Integer32
_OutOfDateDiskCount_Object = MibScalar
outOfDateDiskCount = _OutOfDateDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 12),
    _OutOfDateDiskCount_Type()
)
outOfDateDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskCount.setStatus("current")
_OutOfDateDiskTable_Object = MibTable
outOfDateDiskTable = _OutOfDateDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13)
)
if mibBuilder.loadTexts:
    outOfDateDiskTable.setStatus("current")
_OutOfDateDiskEntry_Object = MibTableRow
outOfDateDiskEntry = _OutOfDateDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1)
)
outOfDateDiskEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "outOfDateDiskIndex"),
)
if mibBuilder.loadTexts:
    outOfDateDiskEntry.setStatus("current")


class _OutOfDateDiskIndex_Type(Integer32):
    """Custom type outOfDateDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OutOfDateDiskIndex_Type.__name__ = "Integer32"
_OutOfDateDiskIndex_Object = MibTableColumn
outOfDateDiskIndex = _OutOfDateDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 1),
    _OutOfDateDiskIndex_Type()
)
outOfDateDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskIndex.setStatus("current")
_OutOfDateDiskDiskName_Type = DisplayString
_OutOfDateDiskDiskName_Object = MibTableColumn
outOfDateDiskDiskName = _OutOfDateDiskDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 2),
    _OutOfDateDiskDiskName_Type()
)
outOfDateDiskDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskDiskName.setStatus("current")
_OutOfDateDiskDiskId_Type = Integer32
_OutOfDateDiskDiskId_Object = MibTableColumn
outOfDateDiskDiskId = _OutOfDateDiskDiskId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 3),
    _OutOfDateDiskDiskId_Type()
)
outOfDateDiskDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskDiskId.setStatus("current")
_OutOfDateDiskScsiAdapter_Type = DisplayString
_OutOfDateDiskScsiAdapter_Object = MibTableColumn
outOfDateDiskScsiAdapter = _OutOfDateDiskScsiAdapter_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 4),
    _OutOfDateDiskScsiAdapter_Type()
)
outOfDateDiskScsiAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskScsiAdapter.setStatus("current")


class _OutOfDateDiskScsiId_Type(Integer32):
    """Custom type outOfDateDiskScsiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OutOfDateDiskScsiId_Type.__name__ = "Integer32"
_OutOfDateDiskScsiId_Object = MibTableColumn
outOfDateDiskScsiId = _OutOfDateDiskScsiId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 5),
    _OutOfDateDiskScsiId_Type()
)
outOfDateDiskScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskScsiId.setStatus("current")
_OutOfDateDiskTotalMb_Type = Integer32
_OutOfDateDiskTotalMb_Object = MibTableColumn
outOfDateDiskTotalMb = _OutOfDateDiskTotalMb_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 6),
    _OutOfDateDiskTotalMb_Type()
)
outOfDateDiskTotalMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskTotalMb.setStatus("current")
_OutOfDateDiskTotalBlocks_Type = Integer32
_OutOfDateDiskTotalBlocks_Object = MibTableColumn
outOfDateDiskTotalBlocks = _OutOfDateDiskTotalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 7),
    _OutOfDateDiskTotalBlocks_Type()
)
outOfDateDiskTotalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskTotalBlocks.setStatus("current")


class _OutOfDateDiskDiskPort_Type(Integer32):
    """Custom type outOfDateDiskDiskPort based on Integer32"""
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
        *(("portA", 1),
          ("portB", 2),
          ("portNone", 4),
          ("portSingle", 3))
    )


_OutOfDateDiskDiskPort_Type.__name__ = "Integer32"
_OutOfDateDiskDiskPort_Object = MibTableColumn
outOfDateDiskDiskPort = _OutOfDateDiskDiskPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 8),
    _OutOfDateDiskDiskPort_Type()
)
outOfDateDiskDiskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskDiskPort.setStatus("current")
_OutOfDateDiskSecondaryDiskName_Type = DisplayString
_OutOfDateDiskSecondaryDiskName_Object = MibTableColumn
outOfDateDiskSecondaryDiskName = _OutOfDateDiskSecondaryDiskName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 9),
    _OutOfDateDiskSecondaryDiskName_Type()
)
outOfDateDiskSecondaryDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskSecondaryDiskName.setStatus("current")


class _OutOfDateDiskSecondaryDiskPort_Type(Integer32):
    """Custom type outOfDateDiskSecondaryDiskPort based on Integer32"""
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
        *(("portA", 1),
          ("portB", 2),
          ("portNone", 4),
          ("portSingle", 3))
    )


_OutOfDateDiskSecondaryDiskPort_Type.__name__ = "Integer32"
_OutOfDateDiskSecondaryDiskPort_Object = MibTableColumn
outOfDateDiskSecondaryDiskPort = _OutOfDateDiskSecondaryDiskPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 10),
    _OutOfDateDiskSecondaryDiskPort_Type()
)
outOfDateDiskSecondaryDiskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskSecondaryDiskPort.setStatus("current")
_OutOfDateDiskShelf_Type = Integer32
_OutOfDateDiskShelf_Object = MibTableColumn
outOfDateDiskShelf = _OutOfDateDiskShelf_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 11),
    _OutOfDateDiskShelf_Type()
)
outOfDateDiskShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskShelf.setStatus("current")
_OutOfDateDiskBay_Type = Integer32
_OutOfDateDiskBay_Object = MibTableColumn
outOfDateDiskBay = _OutOfDateDiskBay_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 12),
    _OutOfDateDiskBay_Type()
)
outOfDateDiskBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskBay.setStatus("current")
_OutOfDateDiskPool_Type = DisplayString
_OutOfDateDiskPool_Object = MibTableColumn
outOfDateDiskPool = _OutOfDateDiskPool_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 13),
    _OutOfDateDiskPool_Type()
)
outOfDateDiskPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskPool.setStatus("current")
_OutOfDateDiskSectorSize_Type = Integer32
_OutOfDateDiskSectorSize_Object = MibTableColumn
outOfDateDiskSectorSize = _OutOfDateDiskSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 14),
    _OutOfDateDiskSectorSize_Type()
)
outOfDateDiskSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskSectorSize.setStatus("current")
_OutOfDateDiskSerialNumber_Type = DisplayString
_OutOfDateDiskSerialNumber_Object = MibTableColumn
outOfDateDiskSerialNumber = _OutOfDateDiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 15),
    _OutOfDateDiskSerialNumber_Type()
)
outOfDateDiskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskSerialNumber.setStatus("current")
_OutOfDateDiskVendor_Type = DisplayString
_OutOfDateDiskVendor_Object = MibTableColumn
outOfDateDiskVendor = _OutOfDateDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 16),
    _OutOfDateDiskVendor_Type()
)
outOfDateDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskVendor.setStatus("current")
_OutOfDateDiskModel_Type = DisplayString
_OutOfDateDiskModel_Object = MibTableColumn
outOfDateDiskModel = _OutOfDateDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 17),
    _OutOfDateDiskModel_Type()
)
outOfDateDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskModel.setStatus("current")
_OutOfDateDiskFirmwareRevision_Type = DisplayString
_OutOfDateDiskFirmwareRevision_Object = MibTableColumn
outOfDateDiskFirmwareRevision = _OutOfDateDiskFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 18),
    _OutOfDateDiskFirmwareRevision_Type()
)
outOfDateDiskFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskFirmwareRevision.setStatus("current")
_OutOfDateDiskRPM_Type = DisplayString
_OutOfDateDiskRPM_Object = MibTableColumn
outOfDateDiskRPM = _OutOfDateDiskRPM_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 19),
    _OutOfDateDiskRPM_Type()
)
outOfDateDiskRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskRPM.setStatus("current")
_OutOfDateDiskType_Type = DisplayString
_OutOfDateDiskType_Object = MibTableColumn
outOfDateDiskType = _OutOfDateDiskType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 6, 13, 1, 20),
    _OutOfDateDiskType_Type()
)
outOfDateDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outOfDateDiskType.setStatus("current")
_Cifs_ObjectIdentity = ObjectIdentity
cifs = _Cifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 7)
)
_CifsOptions_ObjectIdentity = ObjectIdentity
cifsOptions = _CifsOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1)
)


class _CifsIsEnabled_Type(Integer32):
    """Custom type cifsIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CifsIsEnabled_Type.__name__ = "Integer32"
_CifsIsEnabled_Object = MibScalar
cifsIsEnabled = _CifsIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 1),
    _CifsIsEnabled_Type()
)
cifsIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsIsEnabled.setStatus("current")


class _CifsIsLoginEnabled_Type(Integer32):
    """Custom type cifsIsLoginEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CifsIsLoginEnabled_Type.__name__ = "Integer32"
_CifsIsLoginEnabled_Object = MibScalar
cifsIsLoginEnabled = _CifsIsLoginEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 2),
    _CifsIsLoginEnabled_Type()
)
cifsIsLoginEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsIsLoginEnabled.setStatus("current")
_CifsHostName_Type = DisplayString
_CifsHostName_Object = MibScalar
cifsHostName = _CifsHostName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 3),
    _CifsHostName_Type()
)
cifsHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsHostName.setStatus("current")
_CifsAltNames_Type = DisplayString
_CifsAltNames_Object = MibScalar
cifsAltNames = _CifsAltNames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 4),
    _CifsAltNames_Type()
)
cifsAltNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsAltNames.setStatus("current")


class _CifsDomainJoined_Type(Integer32):
    """Custom type cifsDomainJoined based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CifsDomainJoined_Type.__name__ = "Integer32"
_CifsDomainJoined_Object = MibScalar
cifsDomainJoined = _CifsDomainJoined_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 5),
    _CifsDomainJoined_Type()
)
cifsDomainJoined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsDomainJoined.setStatus("current")
_CifsDomainName_Type = DisplayString
_CifsDomainName_Object = MibScalar
cifsDomainName = _CifsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 6),
    _CifsDomainName_Type()
)
cifsDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsDomainName.setStatus("current")
_CifsWGName_Type = DisplayString
_CifsWGName_Object = MibScalar
cifsWGName = _CifsWGName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 7),
    _CifsWGName_Type()
)
cifsWGName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsWGName.setStatus("current")
_CifsDCName_Type = DisplayString
_CifsDCName_Object = MibScalar
cifsDCName = _CifsDCName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 8),
    _CifsDCName_Type()
)
cifsDCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsDCName.setStatus("current")


class _CifsIsWinsEnabled_Type(Integer32):
    """Custom type cifsIsWinsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CifsIsWinsEnabled_Type.__name__ = "Integer32"
_CifsIsWinsEnabled_Object = MibScalar
cifsIsWinsEnabled = _CifsIsWinsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 9),
    _CifsIsWinsEnabled_Type()
)
cifsIsWinsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsIsWinsEnabled.setStatus("current")
_CifsWinsServers_Type = DisplayString
_CifsWinsServers_Object = MibScalar
cifsWinsServers = _CifsWinsServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 10),
    _CifsWinsServers_Type()
)
cifsWinsServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsWinsServers.setStatus("current")


class _CifsSecurityModel_Type(Integer32):
    """Custom type cifsSecurityModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pc", 2),
          ("unix", 1))
    )


_CifsSecurityModel_Type.__name__ = "Integer32"
_CifsSecurityModel_Object = MibScalar
cifsSecurityModel = _CifsSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 11),
    _CifsSecurityModel_Type()
)
cifsSecurityModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsSecurityModel.setStatus("current")
_CifsPCGenericUser_Type = DisplayString
_CifsPCGenericUser_Object = MibScalar
cifsPCGenericUser = _CifsPCGenericUser_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 12),
    _CifsPCGenericUser_Type()
)
cifsPCGenericUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsPCGenericUser.setStatus("current")


class _CifsOplocksEnabled_Type(Integer32):
    """Custom type cifsOplocksEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("notEnabled", 1))
    )


_CifsOplocksEnabled_Type.__name__ = "Integer32"
_CifsOplocksEnabled_Object = MibScalar
cifsOplocksEnabled = _CifsOplocksEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 15),
    _CifsOplocksEnabled_Type()
)
cifsOplocksEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOplocksEnabled.setStatus("current")


class _CifsLevel2OplocksEnabled_Type(Integer32):
    """Custom type cifsLevel2OplocksEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("notEnabled", 1))
    )


_CifsLevel2OplocksEnabled_Type.__name__ = "Integer32"
_CifsLevel2OplocksEnabled_Object = MibScalar
cifsLevel2OplocksEnabled = _CifsLevel2OplocksEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 16),
    _CifsLevel2OplocksEnabled_Type()
)
cifsLevel2OplocksEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsLevel2OplocksEnabled.setStatus("current")


class _CifsPreserveCase_Type(Integer32):
    """Custom type cifsPreserveCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPreserveCase", 1),
          ("preserveCase", 2))
    )


_CifsPreserveCase_Type.__name__ = "Integer32"
_CifsPreserveCase_Object = MibScalar
cifsPreserveCase = _CifsPreserveCase_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 17),
    _CifsPreserveCase_Type()
)
cifsPreserveCase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsPreserveCase.setStatus("current")


class _CifsSymlinksEnabled_Type(Integer32):
    """Custom type cifsSymlinksEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("notEnabled", 1))
    )


_CifsSymlinksEnabled_Type.__name__ = "Integer32"
_CifsSymlinksEnabled_Object = MibScalar
cifsSymlinksEnabled = _CifsSymlinksEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 19),
    _CifsSymlinksEnabled_Type()
)
cifsSymlinksEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsSymlinksEnabled.setStatus("current")


class _CifsSymlinkCycleProtEnabled_Type(Integer32):
    """Custom type cifsSymlinkCycleProtEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("notEnabled", 1))
    )


_CifsSymlinkCycleProtEnabled_Type.__name__ = "Integer32"
_CifsSymlinkCycleProtEnabled_Object = MibScalar
cifsSymlinkCycleProtEnabled = _CifsSymlinkCycleProtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 20),
    _CifsSymlinkCycleProtEnabled_Type()
)
cifsSymlinkCycleProtEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsSymlinkCycleProtEnabled.setStatus("current")


class _CifsIsLicensed_Type(Integer32):
    """Custom type cifsIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CifsIsLicensed_Type.__name__ = "Integer32"
_CifsIsLicensed_Object = MibScalar
cifsIsLicensed = _CifsIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 21),
    _CifsIsLicensed_Type()
)
cifsIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsIsLicensed.setStatus("current")


class _CifsPerClientStatsEnabled_Type(Integer32):
    """Custom type cifsPerClientStatsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CifsPerClientStatsEnabled_Type.__name__ = "Integer32"
_CifsPerClientStatsEnabled_Object = MibScalar
cifsPerClientStatsEnabled = _CifsPerClientStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 1, 22),
    _CifsPerClientStatsEnabled_Type()
)
cifsPerClientStatsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsPerClientStatsEnabled.setStatus("current")
_CifsInfo_ObjectIdentity = ObjectIdentity
cifsInfo = _CifsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2)
)
_CifsStatus_Type = Integer32
_CifsStatus_Object = MibScalar
cifsStatus = _CifsStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 1),
    _CifsStatus_Type()
)
cifsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsStatus.setStatus("current")
_CifsNeedPW_Type = Integer32
_CifsNeedPW_Object = MibScalar
cifsNeedPW = _CifsNeedPW_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 2),
    _CifsNeedPW_Type()
)
cifsNeedPW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNeedPW.setStatus("current")
_CifsTimeToShutdown_Type = Integer32
_CifsTimeToShutdown_Object = MibScalar
cifsTimeToShutdown = _CifsTimeToShutdown_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 3),
    _CifsTimeToShutdown_Type()
)
cifsTimeToShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsTimeToShutdown.setStatus("current")
_CifsMaxConnections_Type = Integer32
_CifsMaxConnections_Object = MibScalar
cifsMaxConnections = _CifsMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 4),
    _CifsMaxConnections_Type()
)
cifsMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsMaxConnections.setStatus("current")
_CifsMaxTrees_Type = Integer32
_CifsMaxTrees_Object = MibScalar
cifsMaxTrees = _CifsMaxTrees_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 5),
    _CifsMaxTrees_Type()
)
cifsMaxTrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsMaxTrees.setStatus("current")
_CifsMaxShares_Type = Integer32
_CifsMaxShares_Object = MibScalar
cifsMaxShares = _CifsMaxShares_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 6),
    _CifsMaxShares_Type()
)
cifsMaxShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsMaxShares.setStatus("current")
_CifsMaxFiles_Type = Integer32
_CifsMaxFiles_Object = MibScalar
cifsMaxFiles = _CifsMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 7),
    _CifsMaxFiles_Type()
)
cifsMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsMaxFiles.setStatus("current")
_CifsMaxACLs_Type = Integer32
_CifsMaxACLs_Object = MibScalar
cifsMaxACLs = _CifsMaxACLs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 8),
    _CifsMaxACLs_Type()
)
cifsMaxACLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsMaxACLs.setStatus("current")
_CifsConnectedUsers_Type = Counter32
_CifsConnectedUsers_Object = MibScalar
cifsConnectedUsers = _CifsConnectedUsers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 9),
    _CifsConnectedUsers_Type()
)
cifsConnectedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsConnectedUsers.setStatus("current")
_CifsNTrees_Type = Counter32
_CifsNTrees_Object = MibScalar
cifsNTrees = _CifsNTrees_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 10),
    _CifsNTrees_Type()
)
cifsNTrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNTrees.setStatus("current")
_CifsNShares_Type = Counter32
_CifsNShares_Object = MibScalar
cifsNShares = _CifsNShares_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 11),
    _CifsNShares_Type()
)
cifsNShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNShares.setStatus("current")
_CifsNSessions_Type = Counter32
_CifsNSessions_Object = MibScalar
cifsNSessions = _CifsNSessions_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 12),
    _CifsNSessions_Type()
)
cifsNSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNSessions.setStatus("current")
_CifsNOpenFiles_Type = Counter32
_CifsNOpenFiles_Object = MibScalar
cifsNOpenFiles = _CifsNOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 13),
    _CifsNOpenFiles_Type()
)
cifsNOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNOpenFiles.setStatus("current")
_CifsNOpenDirs_Type = Counter32
_CifsNOpenDirs_Object = MibScalar
cifsNOpenDirs = _CifsNOpenDirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 14),
    _CifsNOpenDirs_Type()
)
cifsNOpenDirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNOpenDirs.setStatus("current")
_CifsNOplockBreakWaits_Type = Counter32
_CifsNOplockBreakWaits_Object = MibScalar
cifsNOplockBreakWaits = _CifsNOplockBreakWaits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 16),
    _CifsNOplockBreakWaits_Type()
)
cifsNOplockBreakWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNOplockBreakWaits.setStatus("current")
_CifsNOplockAckWaits_Type = Counter32
_CifsNOplockAckWaits_Object = MibScalar
cifsNOplockAckWaits = _CifsNOplockAckWaits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 17),
    _CifsNOplockAckWaits_Type()
)
cifsNOplockAckWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNOplockAckWaits.setStatus("current")
_CifsSuspectOps_Type = Integer32
_CifsSuspectOps_Object = MibScalar
cifsSuspectOps = _CifsSuspectOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 18),
    _CifsSuspectOps_Type()
)
cifsSuspectOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsSuspectOps.setStatus("current")
_CifsNDomainControllers_Type = Integer32
_CifsNDomainControllers_Object = MibScalar
cifsNDomainControllers = _CifsNDomainControllers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 2, 19),
    _CifsNDomainControllers_Type()
)
cifsNDomainControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNDomainControllers.setStatus("current")
_CifsStats_ObjectIdentity = ObjectIdentity
cifsStats = _CifsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3)
)
_CifsServ_ObjectIdentity = ObjectIdentity
cifsServ = _CifsServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1)
)
_CifsOps_ObjectIdentity = ObjectIdentity
cifsOps = _CifsOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 1)
)
_CifsTotalOps_Type = Counter32
_CifsTotalOps_Object = MibScalar
cifsTotalOps = _CifsTotalOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 1, 1),
    _CifsTotalOps_Type()
)
cifsTotalOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsTotalOps.setStatus("current")
_CifsTotalCalls_Type = Counter32
_CifsTotalCalls_Object = MibScalar
cifsTotalCalls = _CifsTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 1, 2),
    _CifsTotalCalls_Type()
)
cifsTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsTotalCalls.setStatus("current")
_CifsBadCalls_Type = Counter32
_CifsBadCalls_Object = MibScalar
cifsBadCalls = _CifsBadCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 1, 3),
    _CifsBadCalls_Type()
)
cifsBadCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsBadCalls.setStatus("current")
_CifsGetAttrs_Type = Counter32
_CifsGetAttrs_Object = MibScalar
cifsGetAttrs = _CifsGetAttrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 1, 4),
    _CifsGetAttrs_Type()
)
cifsGetAttrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsGetAttrs.setStatus("current")
_CifsReads_Type = Counter32
_CifsReads_Object = MibScalar
cifsReads = _CifsReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 1, 5),
    _CifsReads_Type()
)
cifsReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsReads.setStatus("current")
_CifsWrites_Type = Counter32
_CifsWrites_Object = MibScalar
cifsWrites = _CifsWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 1, 6),
    _CifsWrites_Type()
)
cifsWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsWrites.setStatus("current")
_CifsLocks_Type = Counter32
_CifsLocks_Object = MibScalar
cifsLocks = _CifsLocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 1, 7),
    _CifsLocks_Type()
)
cifsLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsLocks.setStatus("current")
_CifsOpens_Type = Counter32
_CifsOpens_Object = MibScalar
cifsOpens = _CifsOpens_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 1, 8),
    _CifsOpens_Type()
)
cifsOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpens.setStatus("current")
_CifsDirOps_Type = Counter32
_CifsDirOps_Object = MibScalar
cifsDirOps = _CifsDirOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 1, 9),
    _CifsDirOps_Type()
)
cifsDirOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsDirOps.setStatus("current")
_CifsOthers_Type = Counter32
_CifsOthers_Object = MibScalar
cifsOthers = _CifsOthers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 1, 10),
    _CifsOthers_Type()
)
cifsOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOthers.setStatus("current")
_CifsReqs_ObjectIdentity = ObjectIdentity
cifsReqs = _CifsReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2)
)
_SmbNegProts_Type = Counter32
_SmbNegProts_Object = MibScalar
smbNegProts = _SmbNegProts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 1),
    _SmbNegProts_Type()
)
smbNegProts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNegProts.setStatus("current")
_SmbSessionSetupAndXs_Type = Counter32
_SmbSessionSetupAndXs_Object = MibScalar
smbSessionSetupAndXs = _SmbSessionSetupAndXs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 2),
    _SmbSessionSetupAndXs_Type()
)
smbSessionSetupAndXs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbSessionSetupAndXs.setStatus("current")
_SmbLogoffAndXs_Type = Counter32
_SmbLogoffAndXs_Object = MibScalar
smbLogoffAndXs = _SmbLogoffAndXs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 3),
    _SmbLogoffAndXs_Type()
)
smbLogoffAndXs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbLogoffAndXs.setStatus("current")
_SmbTreeConnectAndXs_Type = Counter32
_SmbTreeConnectAndXs_Object = MibScalar
smbTreeConnectAndXs = _SmbTreeConnectAndXs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 4),
    _SmbTreeConnectAndXs_Type()
)
smbTreeConnectAndXs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTreeConnectAndXs.setStatus("current")
_SmbTreeDisconnects_Type = Counter32
_SmbTreeDisconnects_Object = MibScalar
smbTreeDisconnects = _SmbTreeDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 5),
    _SmbTreeDisconnects_Type()
)
smbTreeDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTreeDisconnects.setStatus("current")
_SmbTrans2QueryFSInfos_Type = Counter32
_SmbTrans2QueryFSInfos_Object = MibScalar
smbTrans2QueryFSInfos = _SmbTrans2QueryFSInfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 6),
    _SmbTrans2QueryFSInfos_Type()
)
smbTrans2QueryFSInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2QueryFSInfos.setStatus("current")
_SmbEchos_Type = Counter32
_SmbEchos_Object = MibScalar
smbEchos = _SmbEchos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 7),
    _SmbEchos_Type()
)
smbEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbEchos.setStatus("current")
_SmbNTCancels_Type = Counter32
_SmbNTCancels_Object = MibScalar
smbNTCancels = _SmbNTCancels_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 8),
    _SmbNTCancels_Type()
)
smbNTCancels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTCancels.setStatus("current")
_SmbNTCreateAndXs_Type = Counter32
_SmbNTCreateAndXs_Object = MibScalar
smbNTCreateAndXs = _SmbNTCreateAndXs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 9),
    _SmbNTCreateAndXs_Type()
)
smbNTCreateAndXs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTCreateAndXs.setStatus("current")
_SmbNTTransactCreates_Type = Counter32
_SmbNTTransactCreates_Object = MibScalar
smbNTTransactCreates = _SmbNTTransactCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 10),
    _SmbNTTransactCreates_Type()
)
smbNTTransactCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTTransactCreates.setStatus("current")
_SmbCreateTemporaries_Type = Counter32
_SmbCreateTemporaries_Object = MibScalar
smbCreateTemporaries = _SmbCreateTemporaries_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 11),
    _SmbCreateTemporaries_Type()
)
smbCreateTemporaries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbCreateTemporaries.setStatus("current")
_SmbReadAndXs_Type = Counter32
_SmbReadAndXs_Object = MibScalar
smbReadAndXs = _SmbReadAndXs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 12),
    _SmbReadAndXs_Type()
)
smbReadAndXs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbReadAndXs.setStatus("current")
_SmbWriteAndXs_Type = Counter32
_SmbWriteAndXs_Object = MibScalar
smbWriteAndXs = _SmbWriteAndXs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 13),
    _SmbWriteAndXs_Type()
)
smbWriteAndXs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbWriteAndXs.setStatus("current")
_SmbLockingAndXs_Type = Counter32
_SmbLockingAndXs_Object = MibScalar
smbLockingAndXs = _SmbLockingAndXs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 14),
    _SmbLockingAndXs_Type()
)
smbLockingAndXs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbLockingAndXs.setStatus("current")
_SmbSeeks_Type = Counter32
_SmbSeeks_Object = MibScalar
smbSeeks = _SmbSeeks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 15),
    _SmbSeeks_Type()
)
smbSeeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbSeeks.setStatus("current")
_SmbFlushes_Type = Counter32
_SmbFlushes_Object = MibScalar
smbFlushes = _SmbFlushes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 16),
    _SmbFlushes_Type()
)
smbFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbFlushes.setStatus("current")
_SmbCloses_Type = Counter32
_SmbCloses_Object = MibScalar
smbCloses = _SmbCloses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 17),
    _SmbCloses_Type()
)
smbCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbCloses.setStatus("current")
_SmbDeletes_Type = Counter32
_SmbDeletes_Object = MibScalar
smbDeletes = _SmbDeletes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 18),
    _SmbDeletes_Type()
)
smbDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbDeletes.setStatus("current")
_SmbRenames_Type = Counter32
_SmbRenames_Object = MibScalar
smbRenames = _SmbRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 19),
    _SmbRenames_Type()
)
smbRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbRenames.setStatus("current")
_SmbMoves_Type = Counter32
_SmbMoves_Object = MibScalar
smbMoves = _SmbMoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 20),
    _SmbMoves_Type()
)
smbMoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbMoves.setStatus("current")
_SmbCopies_Type = Counter32
_SmbCopies_Object = MibScalar
smbCopies = _SmbCopies_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 21),
    _SmbCopies_Type()
)
smbCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbCopies.setStatus("current")
_SmbTrans2QueryPathInfos_Type = Counter32
_SmbTrans2QueryPathInfos_Object = MibScalar
smbTrans2QueryPathInfos = _SmbTrans2QueryPathInfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 22),
    _SmbTrans2QueryPathInfos_Type()
)
smbTrans2QueryPathInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2QueryPathInfos.setStatus("current")
_SmbTrans2QueryFileInfos_Type = Counter32
_SmbTrans2QueryFileInfos_Object = MibScalar
smbTrans2QueryFileInfos = _SmbTrans2QueryFileInfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 23),
    _SmbTrans2QueryFileInfos_Type()
)
smbTrans2QueryFileInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2QueryFileInfos.setStatus("current")
_SmbTrans2SetPathInfos_Type = Counter32
_SmbTrans2SetPathInfos_Object = MibScalar
smbTrans2SetPathInfos = _SmbTrans2SetPathInfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 24),
    _SmbTrans2SetPathInfos_Type()
)
smbTrans2SetPathInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2SetPathInfos.setStatus("current")
_SmbTrans2SetFileInfos_Type = Counter32
_SmbTrans2SetFileInfos_Object = MibScalar
smbTrans2SetFileInfos = _SmbTrans2SetFileInfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 25),
    _SmbTrans2SetFileInfos_Type()
)
smbTrans2SetFileInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2SetFileInfos.setStatus("current")
_SmbDeleteDirs_Type = Counter32
_SmbDeleteDirs_Object = MibScalar
smbDeleteDirs = _SmbDeleteDirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 26),
    _SmbDeleteDirs_Type()
)
smbDeleteDirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbDeleteDirs.setStatus("current")
_SmbCheckDirs_Type = Counter32
_SmbCheckDirs_Object = MibScalar
smbCheckDirs = _SmbCheckDirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 27),
    _SmbCheckDirs_Type()
)
smbCheckDirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbCheckDirs.setStatus("current")
_SmbTrans2FindFirst2s_Type = Counter32
_SmbTrans2FindFirst2s_Object = MibScalar
smbTrans2FindFirst2s = _SmbTrans2FindFirst2s_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 28),
    _SmbTrans2FindFirst2s_Type()
)
smbTrans2FindFirst2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2FindFirst2s.setStatus("current")
_SmbTrans2FindNext2s_Type = Counter32
_SmbTrans2FindNext2s_Object = MibScalar
smbTrans2FindNext2s = _SmbTrans2FindNext2s_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 29),
    _SmbTrans2FindNext2s_Type()
)
smbTrans2FindNext2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2FindNext2s.setStatus("current")
_SmbFindClose2s_Type = Counter32
_SmbFindClose2s_Object = MibScalar
smbFindClose2s = _SmbFindClose2s_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 30),
    _SmbFindClose2s_Type()
)
smbFindClose2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbFindClose2s.setStatus("current")
_SmbNTTransactNotifyChgs_Type = Counter32
_SmbNTTransactNotifyChgs_Object = MibScalar
smbNTTransactNotifyChgs = _SmbNTTransactNotifyChgs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 31),
    _SmbNTTransactNotifyChgs_Type()
)
smbNTTransactNotifyChgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTTransactNotifyChgs.setStatus("current")
_SmbTrans2GetDFSReferrals_Type = Counter32
_SmbTrans2GetDFSReferrals_Object = MibScalar
smbTrans2GetDFSReferrals = _SmbTrans2GetDFSReferrals_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 32),
    _SmbTrans2GetDFSReferrals_Type()
)
smbTrans2GetDFSReferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2GetDFSReferrals.setStatus("current")
_SmbTrans2ReportDFSIncs_Type = Counter32
_SmbTrans2ReportDFSIncs_Object = MibScalar
smbTrans2ReportDFSIncs = _SmbTrans2ReportDFSIncs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 33),
    _SmbTrans2ReportDFSIncs_Type()
)
smbTrans2ReportDFSIncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2ReportDFSIncs.setStatus("current")
_SmbOpenPrintFiles_Type = Counter32
_SmbOpenPrintFiles_Object = MibScalar
smbOpenPrintFiles = _SmbOpenPrintFiles_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 34),
    _SmbOpenPrintFiles_Type()
)
smbOpenPrintFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbOpenPrintFiles.setStatus("current")
_SmbGetPrintQueues_Type = Counter32
_SmbGetPrintQueues_Object = MibScalar
smbGetPrintQueues = _SmbGetPrintQueues_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 35),
    _SmbGetPrintQueues_Type()
)
smbGetPrintQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbGetPrintQueues.setStatus("current")
_SmbNTTransactIoctls_Type = Counter32
_SmbNTTransactIoctls_Object = MibScalar
smbNTTransactIoctls = _SmbNTTransactIoctls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 36),
    _SmbNTTransactIoctls_Type()
)
smbNTTransactIoctls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTTransactIoctls.setStatus("current")
_SmbNTTransactQuerySecDescs_Type = Counter32
_SmbNTTransactQuerySecDescs_Object = MibScalar
smbNTTransactQuerySecDescs = _SmbNTTransactQuerySecDescs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 37),
    _SmbNTTransactQuerySecDescs_Type()
)
smbNTTransactQuerySecDescs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTTransactQuerySecDescs.setStatus("current")
_SmbNTTransactSetSecDescs_Type = Counter32
_SmbNTTransactSetSecDescs_Object = MibScalar
smbNTTransactSetSecDescs = _SmbNTTransactSetSecDescs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 38),
    _SmbNTTransactSetSecDescs_Type()
)
smbNTTransactSetSecDescs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTTransactSetSecDescs.setStatus("current")
_SmbTrans2CreateDirs_Type = Counter32
_SmbTrans2CreateDirs_Object = MibScalar
smbTrans2CreateDirs = _SmbTrans2CreateDirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 39),
    _SmbTrans2CreateDirs_Type()
)
smbTrans2CreateDirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2CreateDirs.setStatus("current")
_SmbNTCancelCNs_Type = Counter32
_SmbNTCancelCNs_Object = MibScalar
smbNTCancelCNs = _SmbNTCancelCNs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 40),
    _SmbNTCancelCNs_Type()
)
smbNTCancelCNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTCancelCNs.setStatus("current")
_SmbNTCancelOthers_Type = Counter32
_SmbNTCancelOthers_Object = MibScalar
smbNTCancelOthers = _SmbNTCancelOthers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 2, 41),
    _SmbNTCancelOthers_Type()
)
smbNTCancelOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTCancelOthers.setStatus("current")
_CifsPercent_ObjectIdentity = ObjectIdentity
cifsPercent = _CifsPercent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3)
)


class _SmbNegProtPct_Type(Integer32):
    """Custom type smbNegProtPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbNegProtPct_Type.__name__ = "Integer32"
_SmbNegProtPct_Object = MibScalar
smbNegProtPct = _SmbNegProtPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 1),
    _SmbNegProtPct_Type()
)
smbNegProtPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNegProtPct.setStatus("current")


class _SmbSessionSetupAndXPct_Type(Integer32):
    """Custom type smbSessionSetupAndXPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbSessionSetupAndXPct_Type.__name__ = "Integer32"
_SmbSessionSetupAndXPct_Object = MibScalar
smbSessionSetupAndXPct = _SmbSessionSetupAndXPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 2),
    _SmbSessionSetupAndXPct_Type()
)
smbSessionSetupAndXPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbSessionSetupAndXPct.setStatus("current")


class _SmbLogoffAndXPct_Type(Integer32):
    """Custom type smbLogoffAndXPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbLogoffAndXPct_Type.__name__ = "Integer32"
_SmbLogoffAndXPct_Object = MibScalar
smbLogoffAndXPct = _SmbLogoffAndXPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 3),
    _SmbLogoffAndXPct_Type()
)
smbLogoffAndXPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbLogoffAndXPct.setStatus("current")


class _SmbTreeConnectAndXPct_Type(Integer32):
    """Custom type smbTreeConnectAndXPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTreeConnectAndXPct_Type.__name__ = "Integer32"
_SmbTreeConnectAndXPct_Object = MibScalar
smbTreeConnectAndXPct = _SmbTreeConnectAndXPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 4),
    _SmbTreeConnectAndXPct_Type()
)
smbTreeConnectAndXPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTreeConnectAndXPct.setStatus("current")


class _SmbTreeDisconnectAndXPct_Type(Integer32):
    """Custom type smbTreeDisconnectAndXPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTreeDisconnectAndXPct_Type.__name__ = "Integer32"
_SmbTreeDisconnectAndXPct_Object = MibScalar
smbTreeDisconnectAndXPct = _SmbTreeDisconnectAndXPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 5),
    _SmbTreeDisconnectAndXPct_Type()
)
smbTreeDisconnectAndXPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTreeDisconnectAndXPct.setStatus("current")


class _SmbTrans2QueryFSInfoPct_Type(Integer32):
    """Custom type smbTrans2QueryFSInfoPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTrans2QueryFSInfoPct_Type.__name__ = "Integer32"
_SmbTrans2QueryFSInfoPct_Object = MibScalar
smbTrans2QueryFSInfoPct = _SmbTrans2QueryFSInfoPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 6),
    _SmbTrans2QueryFSInfoPct_Type()
)
smbTrans2QueryFSInfoPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2QueryFSInfoPct.setStatus("current")


class _SmbEchoPct_Type(Integer32):
    """Custom type smbEchoPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbEchoPct_Type.__name__ = "Integer32"
_SmbEchoPct_Object = MibScalar
smbEchoPct = _SmbEchoPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 7),
    _SmbEchoPct_Type()
)
smbEchoPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbEchoPct.setStatus("current")


class _SmbNTCancelPct_Type(Integer32):
    """Custom type smbNTCancelPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbNTCancelPct_Type.__name__ = "Integer32"
_SmbNTCancelPct_Object = MibScalar
smbNTCancelPct = _SmbNTCancelPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 8),
    _SmbNTCancelPct_Type()
)
smbNTCancelPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTCancelPct.setStatus("current")


class _SmbCreateAndXPct_Type(Integer32):
    """Custom type smbCreateAndXPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbCreateAndXPct_Type.__name__ = "Integer32"
_SmbCreateAndXPct_Object = MibScalar
smbCreateAndXPct = _SmbCreateAndXPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 9),
    _SmbCreateAndXPct_Type()
)
smbCreateAndXPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbCreateAndXPct.setStatus("current")


class _SmbTransactCreatePct_Type(Integer32):
    """Custom type smbTransactCreatePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTransactCreatePct_Type.__name__ = "Integer32"
_SmbTransactCreatePct_Object = MibScalar
smbTransactCreatePct = _SmbTransactCreatePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 10),
    _SmbTransactCreatePct_Type()
)
smbTransactCreatePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTransactCreatePct.setStatus("current")


class _SmbCreateTemporaryPct_Type(Integer32):
    """Custom type smbCreateTemporaryPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbCreateTemporaryPct_Type.__name__ = "Integer32"
_SmbCreateTemporaryPct_Object = MibScalar
smbCreateTemporaryPct = _SmbCreateTemporaryPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 11),
    _SmbCreateTemporaryPct_Type()
)
smbCreateTemporaryPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbCreateTemporaryPct.setStatus("current")


class _SmbReadAndXPct_Type(Integer32):
    """Custom type smbReadAndXPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbReadAndXPct_Type.__name__ = "Integer32"
_SmbReadAndXPct_Object = MibScalar
smbReadAndXPct = _SmbReadAndXPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 12),
    _SmbReadAndXPct_Type()
)
smbReadAndXPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbReadAndXPct.setStatus("current")


class _SmbWriteAndXPct_Type(Integer32):
    """Custom type smbWriteAndXPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbWriteAndXPct_Type.__name__ = "Integer32"
_SmbWriteAndXPct_Object = MibScalar
smbWriteAndXPct = _SmbWriteAndXPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 13),
    _SmbWriteAndXPct_Type()
)
smbWriteAndXPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbWriteAndXPct.setStatus("current")


class _SmbLockingAndXPct_Type(Integer32):
    """Custom type smbLockingAndXPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbLockingAndXPct_Type.__name__ = "Integer32"
_SmbLockingAndXPct_Object = MibScalar
smbLockingAndXPct = _SmbLockingAndXPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 14),
    _SmbLockingAndXPct_Type()
)
smbLockingAndXPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbLockingAndXPct.setStatus("current")


class _SmbSeekPct_Type(Integer32):
    """Custom type smbSeekPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbSeekPct_Type.__name__ = "Integer32"
_SmbSeekPct_Object = MibScalar
smbSeekPct = _SmbSeekPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 15),
    _SmbSeekPct_Type()
)
smbSeekPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbSeekPct.setStatus("current")


class _SmbFlushPct_Type(Integer32):
    """Custom type smbFlushPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbFlushPct_Type.__name__ = "Integer32"
_SmbFlushPct_Object = MibScalar
smbFlushPct = _SmbFlushPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 16),
    _SmbFlushPct_Type()
)
smbFlushPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbFlushPct.setStatus("current")


class _SmbClosePct_Type(Integer32):
    """Custom type smbClosePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbClosePct_Type.__name__ = "Integer32"
_SmbClosePct_Object = MibScalar
smbClosePct = _SmbClosePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 17),
    _SmbClosePct_Type()
)
smbClosePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbClosePct.setStatus("current")


class _SmbDeletePct_Type(Integer32):
    """Custom type smbDeletePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbDeletePct_Type.__name__ = "Integer32"
_SmbDeletePct_Object = MibScalar
smbDeletePct = _SmbDeletePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 18),
    _SmbDeletePct_Type()
)
smbDeletePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbDeletePct.setStatus("current")


class _SmbRenamePct_Type(Integer32):
    """Custom type smbRenamePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbRenamePct_Type.__name__ = "Integer32"
_SmbRenamePct_Object = MibScalar
smbRenamePct = _SmbRenamePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 19),
    _SmbRenamePct_Type()
)
smbRenamePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbRenamePct.setStatus("current")


class _SmbMovePct_Type(Integer32):
    """Custom type smbMovePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbMovePct_Type.__name__ = "Integer32"
_SmbMovePct_Object = MibScalar
smbMovePct = _SmbMovePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 20),
    _SmbMovePct_Type()
)
smbMovePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbMovePct.setStatus("current")


class _SmbCopyPct_Type(Integer32):
    """Custom type smbCopyPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbCopyPct_Type.__name__ = "Integer32"
_SmbCopyPct_Object = MibScalar
smbCopyPct = _SmbCopyPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 21),
    _SmbCopyPct_Type()
)
smbCopyPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbCopyPct.setStatus("current")


class _SmbTrans2QueryPathInfoPct_Type(Integer32):
    """Custom type smbTrans2QueryPathInfoPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTrans2QueryPathInfoPct_Type.__name__ = "Integer32"
_SmbTrans2QueryPathInfoPct_Object = MibScalar
smbTrans2QueryPathInfoPct = _SmbTrans2QueryPathInfoPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 22),
    _SmbTrans2QueryPathInfoPct_Type()
)
smbTrans2QueryPathInfoPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2QueryPathInfoPct.setStatus("current")


class _SmbTrans2QueryFileInfoPct_Type(Integer32):
    """Custom type smbTrans2QueryFileInfoPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTrans2QueryFileInfoPct_Type.__name__ = "Integer32"
_SmbTrans2QueryFileInfoPct_Object = MibScalar
smbTrans2QueryFileInfoPct = _SmbTrans2QueryFileInfoPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 23),
    _SmbTrans2QueryFileInfoPct_Type()
)
smbTrans2QueryFileInfoPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2QueryFileInfoPct.setStatus("current")


class _SmbTrans2SetPathInfoPct_Type(Integer32):
    """Custom type smbTrans2SetPathInfoPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTrans2SetPathInfoPct_Type.__name__ = "Integer32"
_SmbTrans2SetPathInfoPct_Object = MibScalar
smbTrans2SetPathInfoPct = _SmbTrans2SetPathInfoPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 24),
    _SmbTrans2SetPathInfoPct_Type()
)
smbTrans2SetPathInfoPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2SetPathInfoPct.setStatus("current")


class _SmbTrans2SetFileInfoPct_Type(Integer32):
    """Custom type smbTrans2SetFileInfoPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTrans2SetFileInfoPct_Type.__name__ = "Integer32"
_SmbTrans2SetFileInfoPct_Object = MibScalar
smbTrans2SetFileInfoPct = _SmbTrans2SetFileInfoPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 25),
    _SmbTrans2SetFileInfoPct_Type()
)
smbTrans2SetFileInfoPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2SetFileInfoPct.setStatus("current")


class _SmbDeleteDirPct_Type(Integer32):
    """Custom type smbDeleteDirPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbDeleteDirPct_Type.__name__ = "Integer32"
_SmbDeleteDirPct_Object = MibScalar
smbDeleteDirPct = _SmbDeleteDirPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 26),
    _SmbDeleteDirPct_Type()
)
smbDeleteDirPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbDeleteDirPct.setStatus("current")


class _SmbCheckDirPct_Type(Integer32):
    """Custom type smbCheckDirPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbCheckDirPct_Type.__name__ = "Integer32"
_SmbCheckDirPct_Object = MibScalar
smbCheckDirPct = _SmbCheckDirPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 27),
    _SmbCheckDirPct_Type()
)
smbCheckDirPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbCheckDirPct.setStatus("current")


class _SmbTrans2FindFirst2Pct_Type(Integer32):
    """Custom type smbTrans2FindFirst2Pct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTrans2FindFirst2Pct_Type.__name__ = "Integer32"
_SmbTrans2FindFirst2Pct_Object = MibScalar
smbTrans2FindFirst2Pct = _SmbTrans2FindFirst2Pct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 28),
    _SmbTrans2FindFirst2Pct_Type()
)
smbTrans2FindFirst2Pct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2FindFirst2Pct.setStatus("current")


class _SmbTrans2FindNext2Pct_Type(Integer32):
    """Custom type smbTrans2FindNext2Pct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTrans2FindNext2Pct_Type.__name__ = "Integer32"
_SmbTrans2FindNext2Pct_Object = MibScalar
smbTrans2FindNext2Pct = _SmbTrans2FindNext2Pct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 29),
    _SmbTrans2FindNext2Pct_Type()
)
smbTrans2FindNext2Pct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2FindNext2Pct.setStatus("current")


class _SmbFindClose2Pct_Type(Integer32):
    """Custom type smbFindClose2Pct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbFindClose2Pct_Type.__name__ = "Integer32"
_SmbFindClose2Pct_Object = MibScalar
smbFindClose2Pct = _SmbFindClose2Pct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 30),
    _SmbFindClose2Pct_Type()
)
smbFindClose2Pct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbFindClose2Pct.setStatus("current")


class _SmbNTTransactNotifyChgPct_Type(Integer32):
    """Custom type smbNTTransactNotifyChgPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbNTTransactNotifyChgPct_Type.__name__ = "Integer32"
_SmbNTTransactNotifyChgPct_Object = MibScalar
smbNTTransactNotifyChgPct = _SmbNTTransactNotifyChgPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 31),
    _SmbNTTransactNotifyChgPct_Type()
)
smbNTTransactNotifyChgPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTTransactNotifyChgPct.setStatus("current")


class _SmbTrans2GetDFSReferralPct_Type(Integer32):
    """Custom type smbTrans2GetDFSReferralPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTrans2GetDFSReferralPct_Type.__name__ = "Integer32"
_SmbTrans2GetDFSReferralPct_Object = MibScalar
smbTrans2GetDFSReferralPct = _SmbTrans2GetDFSReferralPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 32),
    _SmbTrans2GetDFSReferralPct_Type()
)
smbTrans2GetDFSReferralPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2GetDFSReferralPct.setStatus("current")


class _SmbTrans2ReportDFSIncPct_Type(Integer32):
    """Custom type smbTrans2ReportDFSIncPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTrans2ReportDFSIncPct_Type.__name__ = "Integer32"
_SmbTrans2ReportDFSIncPct_Object = MibScalar
smbTrans2ReportDFSIncPct = _SmbTrans2ReportDFSIncPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 33),
    _SmbTrans2ReportDFSIncPct_Type()
)
smbTrans2ReportDFSIncPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2ReportDFSIncPct.setStatus("current")


class _SmbOpenPrintFilePct_Type(Integer32):
    """Custom type smbOpenPrintFilePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbOpenPrintFilePct_Type.__name__ = "Integer32"
_SmbOpenPrintFilePct_Object = MibScalar
smbOpenPrintFilePct = _SmbOpenPrintFilePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 34),
    _SmbOpenPrintFilePct_Type()
)
smbOpenPrintFilePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbOpenPrintFilePct.setStatus("current")


class _SmbGetPrintQueuePct_Type(Integer32):
    """Custom type smbGetPrintQueuePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbGetPrintQueuePct_Type.__name__ = "Integer32"
_SmbGetPrintQueuePct_Object = MibScalar
smbGetPrintQueuePct = _SmbGetPrintQueuePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 35),
    _SmbGetPrintQueuePct_Type()
)
smbGetPrintQueuePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbGetPrintQueuePct.setStatus("current")


class _SmbNTTransactIoctlPct_Type(Integer32):
    """Custom type smbNTTransactIoctlPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbNTTransactIoctlPct_Type.__name__ = "Integer32"
_SmbNTTransactIoctlPct_Object = MibScalar
smbNTTransactIoctlPct = _SmbNTTransactIoctlPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 36),
    _SmbNTTransactIoctlPct_Type()
)
smbNTTransactIoctlPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTTransactIoctlPct.setStatus("current")


class _SmbNTTransactQuerySecDescPct_Type(Integer32):
    """Custom type smbNTTransactQuerySecDescPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbNTTransactQuerySecDescPct_Type.__name__ = "Integer32"
_SmbNTTransactQuerySecDescPct_Object = MibScalar
smbNTTransactQuerySecDescPct = _SmbNTTransactQuerySecDescPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 37),
    _SmbNTTransactQuerySecDescPct_Type()
)
smbNTTransactQuerySecDescPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTTransactQuerySecDescPct.setStatus("current")


class _SmbNTTransactSetSecDescPct_Type(Integer32):
    """Custom type smbNTTransactSetSecDescPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbNTTransactSetSecDescPct_Type.__name__ = "Integer32"
_SmbNTTransactSetSecDescPct_Object = MibScalar
smbNTTransactSetSecDescPct = _SmbNTTransactSetSecDescPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 38),
    _SmbNTTransactSetSecDescPct_Type()
)
smbNTTransactSetSecDescPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTTransactSetSecDescPct.setStatus("current")


class _SmbTrans2CreateDirPct_Type(Integer32):
    """Custom type smbTrans2CreateDirPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbTrans2CreateDirPct_Type.__name__ = "Integer32"
_SmbTrans2CreateDirPct_Object = MibScalar
smbTrans2CreateDirPct = _SmbTrans2CreateDirPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 39),
    _SmbTrans2CreateDirPct_Type()
)
smbTrans2CreateDirPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbTrans2CreateDirPct.setStatus("current")


class _SmbNTCancelCNPct_Type(Integer32):
    """Custom type smbNTCancelCNPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbNTCancelCNPct_Type.__name__ = "Integer32"
_SmbNTCancelCNPct_Object = MibScalar
smbNTCancelCNPct = _SmbNTCancelCNPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 40),
    _SmbNTCancelCNPct_Type()
)
smbNTCancelCNPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTCancelCNPct.setStatus("current")


class _SmbNTCancelOtherPct_Type(Integer32):
    """Custom type smbNTCancelOtherPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmbNTCancelOtherPct_Type.__name__ = "Integer32"
_SmbNTCancelOtherPct_Object = MibScalar
smbNTCancelOtherPct = _SmbNTCancelOtherPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 3, 41),
    _SmbNTCancelOtherPct_Type()
)
smbNTCancelOtherPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smbNTCancelOtherPct.setStatus("current")
_CifsObsReqs_ObjectIdentity = ObjectIdentity
cifsObsReqs = _CifsObsReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4)
)
_ObsSmbClosePrintFiles_Type = Counter32
_ObsSmbClosePrintFiles_Object = MibScalar
obsSmbClosePrintFiles = _ObsSmbClosePrintFiles_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 1),
    _ObsSmbClosePrintFiles_Type()
)
obsSmbClosePrintFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbClosePrintFiles.setStatus("current")
_ObsSmbCreates_Type = Counter32
_ObsSmbCreates_Object = MibScalar
obsSmbCreates = _ObsSmbCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 2),
    _ObsSmbCreates_Type()
)
obsSmbCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbCreates.setStatus("current")
_ObsSmbCreateDirs_Type = Counter32
_ObsSmbCreateDirs_Object = MibScalar
obsSmbCreateDirs = _ObsSmbCreateDirs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 3),
    _ObsSmbCreateDirs_Type()
)
obsSmbCreateDirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbCreateDirs.setStatus("current")
_ObsSmbCreateNews_Type = Counter32
_ObsSmbCreateNews_Object = MibScalar
obsSmbCreateNews = _ObsSmbCreateNews_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 4),
    _ObsSmbCreateNews_Type()
)
obsSmbCreateNews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbCreateNews.setStatus("current")
_ObsSmbLockAndReads_Type = Counter32
_ObsSmbLockAndReads_Object = MibScalar
obsSmbLockAndReads = _ObsSmbLockAndReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 5),
    _ObsSmbLockAndReads_Type()
)
obsSmbLockAndReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbLockAndReads.setStatus("current")
_ObsSmbLockByteRanges_Type = Counter32
_ObsSmbLockByteRanges_Object = MibScalar
obsSmbLockByteRanges = _ObsSmbLockByteRanges_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 6),
    _ObsSmbLockByteRanges_Type()
)
obsSmbLockByteRanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbLockByteRanges.setStatus("current")
_ObsSmbOpens_Type = Counter32
_ObsSmbOpens_Object = MibScalar
obsSmbOpens = _ObsSmbOpens_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 7),
    _ObsSmbOpens_Type()
)
obsSmbOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbOpens.setStatus("current")
_ObsSmbOpenAndXs_Type = Counter32
_ObsSmbOpenAndXs_Object = MibScalar
obsSmbOpenAndXs = _ObsSmbOpenAndXs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 8),
    _ObsSmbOpenAndXs_Type()
)
obsSmbOpenAndXs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbOpenAndXs.setStatus("current")
_ObsSmbProcessExits_Type = Counter32
_ObsSmbProcessExits_Object = MibScalar
obsSmbProcessExits = _ObsSmbProcessExits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 9),
    _ObsSmbProcessExits_Type()
)
obsSmbProcessExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbProcessExits.setStatus("current")
_ObsSmbQueryInfos_Type = Counter32
_ObsSmbQueryInfos_Object = MibScalar
obsSmbQueryInfos = _ObsSmbQueryInfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 10),
    _ObsSmbQueryInfos_Type()
)
obsSmbQueryInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbQueryInfos.setStatus("current")
_ObsSmbQueryInfo2s_Type = Counter32
_ObsSmbQueryInfo2s_Object = MibScalar
obsSmbQueryInfo2s = _ObsSmbQueryInfo2s_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 11),
    _ObsSmbQueryInfo2s_Type()
)
obsSmbQueryInfo2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbQueryInfo2s.setStatus("current")
_ObsSmbReads_Type = Counter32
_ObsSmbReads_Object = MibScalar
obsSmbReads = _ObsSmbReads_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 12),
    _ObsSmbReads_Type()
)
obsSmbReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbReads.setStatus("current")
_ObsSmbReadMPXs_Type = Counter32
_ObsSmbReadMPXs_Object = MibScalar
obsSmbReadMPXs = _ObsSmbReadMPXs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 13),
    _ObsSmbReadMPXs_Type()
)
obsSmbReadMPXs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbReadMPXs.setStatus("current")
_ObsSmbReadRaws_Type = Counter32
_ObsSmbReadRaws_Object = MibScalar
obsSmbReadRaws = _ObsSmbReadRaws_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 14),
    _ObsSmbReadRaws_Type()
)
obsSmbReadRaws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbReadRaws.setStatus("current")
_ObsSmbSearchs_Type = Counter32
_ObsSmbSearchs_Object = MibScalar
obsSmbSearchs = _ObsSmbSearchs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 15),
    _ObsSmbSearchs_Type()
)
obsSmbSearchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbSearchs.setStatus("current")
_ObsSmbSetInfos_Type = Counter32
_ObsSmbSetInfos_Object = MibScalar
obsSmbSetInfos = _ObsSmbSetInfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 16),
    _ObsSmbSetInfos_Type()
)
obsSmbSetInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbSetInfos.setStatus("current")
_ObsSmbSetInfo2s_Type = Counter32
_ObsSmbSetInfo2s_Object = MibScalar
obsSmbSetInfo2s = _ObsSmbSetInfo2s_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 17),
    _ObsSmbSetInfo2s_Type()
)
obsSmbSetInfo2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbSetInfo2s.setStatus("current")
_ObsSmbQueryInfoDisks_Type = Counter32
_ObsSmbQueryInfoDisks_Object = MibScalar
obsSmbQueryInfoDisks = _ObsSmbQueryInfoDisks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 18),
    _ObsSmbQueryInfoDisks_Type()
)
obsSmbQueryInfoDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbQueryInfoDisks.setStatus("current")
_ObsSmbTrans2Open2s_Type = Counter32
_ObsSmbTrans2Open2s_Object = MibScalar
obsSmbTrans2Open2s = _ObsSmbTrans2Open2s_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 19),
    _ObsSmbTrans2Open2s_Type()
)
obsSmbTrans2Open2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbTrans2Open2s.setStatus("current")
_ObsSmbTreeConnects_Type = Counter32
_ObsSmbTreeConnects_Object = MibScalar
obsSmbTreeConnects = _ObsSmbTreeConnects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 20),
    _ObsSmbTreeConnects_Type()
)
obsSmbTreeConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbTreeConnects.setStatus("current")
_ObsSmbUnlockByteRanges_Type = Counter32
_ObsSmbUnlockByteRanges_Object = MibScalar
obsSmbUnlockByteRanges = _ObsSmbUnlockByteRanges_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 21),
    _ObsSmbUnlockByteRanges_Type()
)
obsSmbUnlockByteRanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbUnlockByteRanges.setStatus("current")
_ObsSmbWrites_Type = Counter32
_ObsSmbWrites_Object = MibScalar
obsSmbWrites = _ObsSmbWrites_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 22),
    _ObsSmbWrites_Type()
)
obsSmbWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbWrites.setStatus("current")
_ObsSmbWriteAndUnlocks_Type = Counter32
_ObsSmbWriteAndUnlocks_Object = MibScalar
obsSmbWriteAndUnlocks = _ObsSmbWriteAndUnlocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 23),
    _ObsSmbWriteAndUnlocks_Type()
)
obsSmbWriteAndUnlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbWriteAndUnlocks.setStatus("current")
_ObsSmbWriteAndCloses_Type = Counter32
_ObsSmbWriteAndCloses_Object = MibScalar
obsSmbWriteAndCloses = _ObsSmbWriteAndCloses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 24),
    _ObsSmbWriteAndCloses_Type()
)
obsSmbWriteAndCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbWriteAndCloses.setStatus("current")
_ObsSmbWriteMPXs_Type = Counter32
_ObsSmbWriteMPXs_Object = MibScalar
obsSmbWriteMPXs = _ObsSmbWriteMPXs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 25),
    _ObsSmbWriteMPXs_Type()
)
obsSmbWriteMPXs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbWriteMPXs.setStatus("current")
_ObsSmbWritePrintFiles_Type = Counter32
_ObsSmbWritePrintFiles_Object = MibScalar
obsSmbWritePrintFiles = _ObsSmbWritePrintFiles_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 26),
    _ObsSmbWritePrintFiles_Type()
)
obsSmbWritePrintFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbWritePrintFiles.setStatus("current")
_ObsSmbWriteRaws_Type = Counter32
_ObsSmbWriteRaws_Object = MibScalar
obsSmbWriteRaws = _ObsSmbWriteRaws_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 4, 27),
    _ObsSmbWriteRaws_Type()
)
obsSmbWriteRaws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbWriteRaws.setStatus("current")
_CifsObsPercent_ObjectIdentity = ObjectIdentity
cifsObsPercent = _CifsObsPercent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5)
)


class _ObsSmbClosePrintFilePct_Type(Integer32):
    """Custom type obsSmbClosePrintFilePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbClosePrintFilePct_Type.__name__ = "Integer32"
_ObsSmbClosePrintFilePct_Object = MibScalar
obsSmbClosePrintFilePct = _ObsSmbClosePrintFilePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 1),
    _ObsSmbClosePrintFilePct_Type()
)
obsSmbClosePrintFilePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbClosePrintFilePct.setStatus("current")


class _ObsSmbCreatePct_Type(Integer32):
    """Custom type obsSmbCreatePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbCreatePct_Type.__name__ = "Integer32"
_ObsSmbCreatePct_Object = MibScalar
obsSmbCreatePct = _ObsSmbCreatePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 2),
    _ObsSmbCreatePct_Type()
)
obsSmbCreatePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbCreatePct.setStatus("current")


class _ObsSmbCreateDirPct_Type(Integer32):
    """Custom type obsSmbCreateDirPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbCreateDirPct_Type.__name__ = "Integer32"
_ObsSmbCreateDirPct_Object = MibScalar
obsSmbCreateDirPct = _ObsSmbCreateDirPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 3),
    _ObsSmbCreateDirPct_Type()
)
obsSmbCreateDirPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbCreateDirPct.setStatus("current")


class _ObsSmbCreateNewPct_Type(Integer32):
    """Custom type obsSmbCreateNewPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbCreateNewPct_Type.__name__ = "Integer32"
_ObsSmbCreateNewPct_Object = MibScalar
obsSmbCreateNewPct = _ObsSmbCreateNewPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 4),
    _ObsSmbCreateNewPct_Type()
)
obsSmbCreateNewPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbCreateNewPct.setStatus("current")


class _ObsSmbLockAndReadPct_Type(Integer32):
    """Custom type obsSmbLockAndReadPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbLockAndReadPct_Type.__name__ = "Integer32"
_ObsSmbLockAndReadPct_Object = MibScalar
obsSmbLockAndReadPct = _ObsSmbLockAndReadPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 5),
    _ObsSmbLockAndReadPct_Type()
)
obsSmbLockAndReadPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbLockAndReadPct.setStatus("current")


class _ObsSmbLockByteRangePct_Type(Integer32):
    """Custom type obsSmbLockByteRangePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbLockByteRangePct_Type.__name__ = "Integer32"
_ObsSmbLockByteRangePct_Object = MibScalar
obsSmbLockByteRangePct = _ObsSmbLockByteRangePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 6),
    _ObsSmbLockByteRangePct_Type()
)
obsSmbLockByteRangePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbLockByteRangePct.setStatus("current")


class _ObsSmbOpenPct_Type(Integer32):
    """Custom type obsSmbOpenPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbOpenPct_Type.__name__ = "Integer32"
_ObsSmbOpenPct_Object = MibScalar
obsSmbOpenPct = _ObsSmbOpenPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 7),
    _ObsSmbOpenPct_Type()
)
obsSmbOpenPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbOpenPct.setStatus("current")


class _ObsSmbOpenAndXPct_Type(Integer32):
    """Custom type obsSmbOpenAndXPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbOpenAndXPct_Type.__name__ = "Integer32"
_ObsSmbOpenAndXPct_Object = MibScalar
obsSmbOpenAndXPct = _ObsSmbOpenAndXPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 8),
    _ObsSmbOpenAndXPct_Type()
)
obsSmbOpenAndXPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbOpenAndXPct.setStatus("current")


class _ObsSmbProcessExitPct_Type(Integer32):
    """Custom type obsSmbProcessExitPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbProcessExitPct_Type.__name__ = "Integer32"
_ObsSmbProcessExitPct_Object = MibScalar
obsSmbProcessExitPct = _ObsSmbProcessExitPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 9),
    _ObsSmbProcessExitPct_Type()
)
obsSmbProcessExitPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbProcessExitPct.setStatus("current")


class _ObsSmbQueryInfoPct_Type(Integer32):
    """Custom type obsSmbQueryInfoPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbQueryInfoPct_Type.__name__ = "Integer32"
_ObsSmbQueryInfoPct_Object = MibScalar
obsSmbQueryInfoPct = _ObsSmbQueryInfoPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 10),
    _ObsSmbQueryInfoPct_Type()
)
obsSmbQueryInfoPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbQueryInfoPct.setStatus("current")


class _ObsSmbQueryInfo2Pct_Type(Integer32):
    """Custom type obsSmbQueryInfo2Pct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbQueryInfo2Pct_Type.__name__ = "Integer32"
_ObsSmbQueryInfo2Pct_Object = MibScalar
obsSmbQueryInfo2Pct = _ObsSmbQueryInfo2Pct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 11),
    _ObsSmbQueryInfo2Pct_Type()
)
obsSmbQueryInfo2Pct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbQueryInfo2Pct.setStatus("current")


class _ObsSmbReadPct_Type(Integer32):
    """Custom type obsSmbReadPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbReadPct_Type.__name__ = "Integer32"
_ObsSmbReadPct_Object = MibScalar
obsSmbReadPct = _ObsSmbReadPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 12),
    _ObsSmbReadPct_Type()
)
obsSmbReadPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbReadPct.setStatus("current")


class _ObsSmbReadMPXPct_Type(Integer32):
    """Custom type obsSmbReadMPXPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbReadMPXPct_Type.__name__ = "Integer32"
_ObsSmbReadMPXPct_Object = MibScalar
obsSmbReadMPXPct = _ObsSmbReadMPXPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 13),
    _ObsSmbReadMPXPct_Type()
)
obsSmbReadMPXPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbReadMPXPct.setStatus("current")


class _ObsSmbReadRawPct_Type(Integer32):
    """Custom type obsSmbReadRawPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbReadRawPct_Type.__name__ = "Integer32"
_ObsSmbReadRawPct_Object = MibScalar
obsSmbReadRawPct = _ObsSmbReadRawPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 14),
    _ObsSmbReadRawPct_Type()
)
obsSmbReadRawPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbReadRawPct.setStatus("current")


class _ObsSmbSearchPct_Type(Integer32):
    """Custom type obsSmbSearchPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbSearchPct_Type.__name__ = "Integer32"
_ObsSmbSearchPct_Object = MibScalar
obsSmbSearchPct = _ObsSmbSearchPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 15),
    _ObsSmbSearchPct_Type()
)
obsSmbSearchPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbSearchPct.setStatus("current")


class _ObsSmbSetInfoPct_Type(Integer32):
    """Custom type obsSmbSetInfoPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbSetInfoPct_Type.__name__ = "Integer32"
_ObsSmbSetInfoPct_Object = MibScalar
obsSmbSetInfoPct = _ObsSmbSetInfoPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 16),
    _ObsSmbSetInfoPct_Type()
)
obsSmbSetInfoPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbSetInfoPct.setStatus("current")


class _ObsSmbSetInfo2Pct_Type(Integer32):
    """Custom type obsSmbSetInfo2Pct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbSetInfo2Pct_Type.__name__ = "Integer32"
_ObsSmbSetInfo2Pct_Object = MibScalar
obsSmbSetInfo2Pct = _ObsSmbSetInfo2Pct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 17),
    _ObsSmbSetInfo2Pct_Type()
)
obsSmbSetInfo2Pct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbSetInfo2Pct.setStatus("current")


class _ObsSmbQueryInfoDiskPct_Type(Integer32):
    """Custom type obsSmbQueryInfoDiskPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbQueryInfoDiskPct_Type.__name__ = "Integer32"
_ObsSmbQueryInfoDiskPct_Object = MibScalar
obsSmbQueryInfoDiskPct = _ObsSmbQueryInfoDiskPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 18),
    _ObsSmbQueryInfoDiskPct_Type()
)
obsSmbQueryInfoDiskPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbQueryInfoDiskPct.setStatus("current")


class _ObsSmbTrans2Open2Pct_Type(Integer32):
    """Custom type obsSmbTrans2Open2Pct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbTrans2Open2Pct_Type.__name__ = "Integer32"
_ObsSmbTrans2Open2Pct_Object = MibScalar
obsSmbTrans2Open2Pct = _ObsSmbTrans2Open2Pct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 19),
    _ObsSmbTrans2Open2Pct_Type()
)
obsSmbTrans2Open2Pct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbTrans2Open2Pct.setStatus("current")


class _ObsSmbTreeConnectPct_Type(Integer32):
    """Custom type obsSmbTreeConnectPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbTreeConnectPct_Type.__name__ = "Integer32"
_ObsSmbTreeConnectPct_Object = MibScalar
obsSmbTreeConnectPct = _ObsSmbTreeConnectPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 20),
    _ObsSmbTreeConnectPct_Type()
)
obsSmbTreeConnectPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbTreeConnectPct.setStatus("current")


class _ObsSmbUnlockByteRangePct_Type(Integer32):
    """Custom type obsSmbUnlockByteRangePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbUnlockByteRangePct_Type.__name__ = "Integer32"
_ObsSmbUnlockByteRangePct_Object = MibScalar
obsSmbUnlockByteRangePct = _ObsSmbUnlockByteRangePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 21),
    _ObsSmbUnlockByteRangePct_Type()
)
obsSmbUnlockByteRangePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbUnlockByteRangePct.setStatus("current")


class _ObsSmbWritePct_Type(Integer32):
    """Custom type obsSmbWritePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbWritePct_Type.__name__ = "Integer32"
_ObsSmbWritePct_Object = MibScalar
obsSmbWritePct = _ObsSmbWritePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 22),
    _ObsSmbWritePct_Type()
)
obsSmbWritePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbWritePct.setStatus("current")


class _ObsSmbWriteAndUnlockPct_Type(Integer32):
    """Custom type obsSmbWriteAndUnlockPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbWriteAndUnlockPct_Type.__name__ = "Integer32"
_ObsSmbWriteAndUnlockPct_Object = MibScalar
obsSmbWriteAndUnlockPct = _ObsSmbWriteAndUnlockPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 23),
    _ObsSmbWriteAndUnlockPct_Type()
)
obsSmbWriteAndUnlockPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbWriteAndUnlockPct.setStatus("current")


class _ObsSmbWriteAndClosePct_Type(Integer32):
    """Custom type obsSmbWriteAndClosePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbWriteAndClosePct_Type.__name__ = "Integer32"
_ObsSmbWriteAndClosePct_Object = MibScalar
obsSmbWriteAndClosePct = _ObsSmbWriteAndClosePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 24),
    _ObsSmbWriteAndClosePct_Type()
)
obsSmbWriteAndClosePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbWriteAndClosePct.setStatus("current")


class _ObsSmbWriteMPXPct_Type(Integer32):
    """Custom type obsSmbWriteMPXPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbWriteMPXPct_Type.__name__ = "Integer32"
_ObsSmbWriteMPXPct_Object = MibScalar
obsSmbWriteMPXPct = _ObsSmbWriteMPXPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 25),
    _ObsSmbWriteMPXPct_Type()
)
obsSmbWriteMPXPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbWriteMPXPct.setStatus("current")


class _ObsSmbWritePrintFilePct_Type(Integer32):
    """Custom type obsSmbWritePrintFilePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbWritePrintFilePct_Type.__name__ = "Integer32"
_ObsSmbWritePrintFilePct_Object = MibScalar
obsSmbWritePrintFilePct = _ObsSmbWritePrintFilePct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 26),
    _ObsSmbWritePrintFilePct_Type()
)
obsSmbWritePrintFilePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbWritePrintFilePct.setStatus("current")


class _ObsSmbWriteRawPct_Type(Integer32):
    """Custom type obsSmbWriteRawPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ObsSmbWriteRawPct_Type.__name__ = "Integer32"
_ObsSmbWriteRawPct_Object = MibScalar
obsSmbWriteRawPct = _ObsSmbWriteRawPct_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 3, 1, 5, 27),
    _ObsSmbWriteRawPct_Type()
)
obsSmbWriteRawPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSmbWriteRawPct.setStatus("current")
_CifsMisc_ObjectIdentity = ObjectIdentity
cifsMisc = _CifsMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4)
)
_CifsCancelLocks_Type = Counter32
_CifsCancelLocks_Object = MibScalar
cifsCancelLocks = _CifsCancelLocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 1),
    _CifsCancelLocks_Type()
)
cifsCancelLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsCancelLocks.setStatus("current")
_CifsWaitLocks_Type = Counter32
_CifsWaitLocks_Object = MibScalar
cifsWaitLocks = _CifsWaitLocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 2),
    _CifsWaitLocks_Type()
)
cifsWaitLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsWaitLocks.setStatus("current")
_CifsCopyToAligns_Type = Counter32
_CifsCopyToAligns_Object = MibScalar
cifsCopyToAligns = _CifsCopyToAligns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 3),
    _CifsCopyToAligns_Type()
)
cifsCopyToAligns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsCopyToAligns.setStatus("current")
_CifsAlignedSmalls_Type = Counter32
_CifsAlignedSmalls_Object = MibScalar
cifsAlignedSmalls = _CifsAlignedSmalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 4),
    _CifsAlignedSmalls_Type()
)
cifsAlignedSmalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsAlignedSmalls.setStatus("current")
_CifsAlignedLarges_Type = Counter32
_CifsAlignedLarges_Object = MibScalar
cifsAlignedLarges = _CifsAlignedLarges_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 5),
    _CifsAlignedLarges_Type()
)
cifsAlignedLarges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsAlignedLarges.setStatus("current")
_CifsAlignedSmallRels_Type = Counter32
_CifsAlignedSmallRels_Object = MibScalar
cifsAlignedSmallRels = _CifsAlignedSmallRels_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 6),
    _CifsAlignedSmallRels_Type()
)
cifsAlignedSmallRels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsAlignedSmallRels.setStatus("current")
_CifsAlignedLargeRels_Type = Counter32
_CifsAlignedLargeRels_Object = MibScalar
cifsAlignedLargeRels = _CifsAlignedLargeRels_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 7),
    _CifsAlignedLargeRels_Type()
)
cifsAlignedLargeRels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsAlignedLargeRels.setStatus("current")
_CifsMbufWaits_Type = Counter32
_CifsMbufWaits_Object = MibScalar
cifsMbufWaits = _CifsMbufWaits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 8),
    _CifsMbufWaits_Type()
)
cifsMbufWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsMbufWaits.setStatus("current")
_CifsNbtWaits_Type = Counter32
_CifsNbtWaits_Object = MibScalar
cifsNbtWaits = _CifsNbtWaits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 9),
    _CifsNbtWaits_Type()
)
cifsNbtWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNbtWaits.setStatus("current")
_CifsCwaWaits_Type = Counter32
_CifsCwaWaits_Object = MibScalar
cifsCwaWaits = _CifsCwaWaits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 10),
    _CifsCwaWaits_Type()
)
cifsCwaWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsCwaWaits.setStatus("current")
_CifsMultipleVCs_Type = Counter32
_CifsMultipleVCs_Object = MibScalar
cifsMultipleVCs = _CifsMultipleVCs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 11),
    _CifsMultipleVCs_Type()
)
cifsMultipleVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsMultipleVCs.setStatus("current")
_CifsPDCUpcalls_Type = Counter32
_CifsPDCUpcalls_Object = MibScalar
cifsPDCUpcalls = _CifsPDCUpcalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 12),
    _CifsPDCUpcalls_Type()
)
cifsPDCUpcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsPDCUpcalls.setStatus("current")
_CifsQueuedWriteRaws_Type = Counter32
_CifsQueuedWriteRaws_Object = MibScalar
cifsQueuedWriteRaws = _CifsQueuedWriteRaws_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 13),
    _CifsQueuedWriteRaws_Type()
)
cifsQueuedWriteRaws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsQueuedWriteRaws.setStatus("current")
_CifsNBTDisconnects_Type = Counter32
_CifsNBTDisconnects_Object = MibScalar
cifsNBTDisconnects = _CifsNBTDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 14),
    _CifsNBTDisconnects_Type()
)
cifsNBTDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsNBTDisconnects.setStatus("current")
_CifsSMBDisconnects_Type = Counter32
_CifsSMBDisconnects_Object = MibScalar
cifsSMBDisconnects = _CifsSMBDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 15),
    _CifsSMBDisconnects_Type()
)
cifsSMBDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsSMBDisconnects.setStatus("current")
_CifsDupDisconnects_Type = Counter32
_CifsDupDisconnects_Object = MibScalar
cifsDupDisconnects = _CifsDupDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 16),
    _CifsDupDisconnects_Type()
)
cifsDupDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsDupDisconnects.setStatus("current")
_CifsOpLkBatchToL2s_Type = Counter32
_CifsOpLkBatchToL2s_Object = MibScalar
cifsOpLkBatchToL2s = _CifsOpLkBatchToL2s_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 17),
    _CifsOpLkBatchToL2s_Type()
)
cifsOpLkBatchToL2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpLkBatchToL2s.setStatus("current")
_CifsOpLkBatchToNones_Type = Counter32
_CifsOpLkBatchToNones_Object = MibScalar
cifsOpLkBatchToNones = _CifsOpLkBatchToNones_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 18),
    _CifsOpLkBatchToNones_Type()
)
cifsOpLkBatchToNones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpLkBatchToNones.setStatus("current")
_CifsOpLkL2ToNones_Type = Counter32
_CifsOpLkL2ToNones_Object = MibScalar
cifsOpLkL2ToNones = _CifsOpLkL2ToNones_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 19),
    _CifsOpLkL2ToNones_Type()
)
cifsOpLkL2ToNones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpLkL2ToNones.setStatus("current")
_CifsOpLkNoBreakAcks_Type = Counter32
_CifsOpLkNoBreakAcks_Object = MibScalar
cifsOpLkNoBreakAcks = _CifsOpLkNoBreakAcks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 20),
    _CifsOpLkNoBreakAcks_Type()
)
cifsOpLkNoBreakAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpLkNoBreakAcks.setStatus("current")
_CifsOpLkIgnoredAcks_Type = Counter32
_CifsOpLkIgnoredAcks_Object = MibScalar
cifsOpLkIgnoredAcks = _CifsOpLkIgnoredAcks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 21),
    _CifsOpLkIgnoredAcks_Type()
)
cifsOpLkIgnoredAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpLkIgnoredAcks.setStatus("current")
_CifsOpLkMultiWaiters_Type = Counter32
_CifsOpLkMultiWaiters_Object = MibScalar
cifsOpLkMultiWaiters = _CifsOpLkMultiWaiters_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 22),
    _CifsOpLkMultiWaiters_Type()
)
cifsOpLkMultiWaiters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpLkMultiWaiters.setStatus("current")
_CifsSharingErrorRetries_Type = Counter32
_CifsSharingErrorRetries_Object = MibScalar
cifsSharingErrorRetries = _CifsSharingErrorRetries_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 23),
    _CifsSharingErrorRetries_Type()
)
cifsSharingErrorRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsSharingErrorRetries.setStatus("current")
_CifsOpLkWaiterTimedOuts_Type = Counter32
_CifsOpLkWaiterTimedOuts_Object = MibScalar
cifsOpLkWaiterTimedOuts = _CifsOpLkWaiterTimedOuts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 24),
    _CifsOpLkWaiterTimedOuts_Type()
)
cifsOpLkWaiterTimedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpLkWaiterTimedOuts.setStatus("current")
_CifsOpLkDelayedBreaks_Type = Counter32
_CifsOpLkDelayedBreaks_Object = MibScalar
cifsOpLkDelayedBreaks = _CifsOpLkDelayedBreaks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 25),
    _CifsOpLkDelayedBreaks_Type()
)
cifsOpLkDelayedBreaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpLkDelayedBreaks.setStatus("current")
_CifsOpLkEarlyNFSs_Type = Counter32
_CifsOpLkEarlyNFSs_Object = MibScalar
cifsOpLkEarlyNFSs = _CifsOpLkEarlyNFSs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 26),
    _CifsOpLkEarlyNFSs_Type()
)
cifsOpLkEarlyNFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpLkEarlyNFSs.setStatus("current")
_CifsOpLkNFSWaiteds_Type = Counter32
_CifsOpLkNFSWaiteds_Object = MibScalar
cifsOpLkNFSWaiteds = _CifsOpLkNFSWaiteds_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 27),
    _CifsOpLkNFSWaiteds_Type()
)
cifsOpLkNFSWaiteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpLkNFSWaiteds.setStatus("current")
_CifsMaxNFSBkWaiterCount_Type = Integer32
_CifsMaxNFSBkWaiterCount_Object = MibScalar
cifsMaxNFSBkWaiterCount = _CifsMaxNFSBkWaiterCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 28),
    _CifsMaxNFSBkWaiterCount_Type()
)
cifsMaxNFSBkWaiterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsMaxNFSBkWaiterCount.setStatus("current")


class _CifsClearTextPasswd_Type(Integer32):
    """Custom type cifsClearTextPasswd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CifsClearTextPasswd_Type.__name__ = "Integer32"
_CifsClearTextPasswd_Object = MibScalar
cifsClearTextPasswd = _CifsClearTextPasswd_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 7, 4, 29),
    _CifsClearTextPasswd_Type()
)
cifsClearTextPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsClearTextPasswd.setStatus("current")
_Netcache_ObjectIdentity = ObjectIdentity
netcache = _Netcache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8)
)
_NcOptions_ObjectIdentity = ObjectIdentity
ncOptions = _NcOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1)
)


class _NcIsEnabled_Type(Integer32):
    """Custom type ncIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcIsEnabled_Type.__name__ = "Integer32"
_NcIsEnabled_Object = MibScalar
ncIsEnabled = _NcIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 1),
    _NcIsEnabled_Type()
)
ncIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncIsEnabled.setStatus("current")


class _NcIsLicensed_Type(Integer32):
    """Custom type ncIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcIsLicensed_Type.__name__ = "Integer32"
_NcIsLicensed_Object = MibScalar
ncIsLicensed = _NcIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 2),
    _NcIsLicensed_Type()
)
ncIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncIsLicensed.setStatus("current")
_NcDnsOptions_ObjectIdentity = ObjectIdentity
ncDnsOptions = _NcDnsOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 3)
)


class _NcDnsIsEnabled_Type(Integer32):
    """Custom type ncDnsIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcDnsIsEnabled_Type.__name__ = "Integer32"
_NcDnsIsEnabled_Object = MibScalar
ncDnsIsEnabled = _NcDnsIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 3, 1),
    _NcDnsIsEnabled_Type()
)
ncDnsIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsIsEnabled.setStatus("current")
_NcHttpOptions_ObjectIdentity = ObjectIdentity
ncHttpOptions = _NcHttpOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 4)
)


class _NcHttpIsEnabled_Type(Integer32):
    """Custom type ncHttpIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcHttpIsEnabled_Type.__name__ = "Integer32"
_NcHttpIsEnabled_Object = MibScalar
ncHttpIsEnabled = _NcHttpIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 4, 1),
    _NcHttpIsEnabled_Type()
)
ncHttpIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpIsEnabled.setStatus("current")
_NcNntpOptions_ObjectIdentity = ObjectIdentity
ncNntpOptions = _NcNntpOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 5)
)


class _NcNntpIsEnabled_Type(Integer32):
    """Custom type ncNntpIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcNntpIsEnabled_Type.__name__ = "Integer32"
_NcNntpIsEnabled_Object = MibScalar
ncNntpIsEnabled = _NcNntpIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 5, 1),
    _NcNntpIsEnabled_Type()
)
ncNntpIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpIsEnabled.setStatus("current")


class _NcNntpIsLicensed_Type(Integer32):
    """Custom type ncNntpIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcNntpIsLicensed_Type.__name__ = "Integer32"
_NcNntpIsLicensed_Object = MibScalar
ncNntpIsLicensed = _NcNntpIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 5, 2),
    _NcNntpIsLicensed_Type()
)
ncNntpIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpIsLicensed.setStatus("current")
_NcStreamingOptions_ObjectIdentity = ObjectIdentity
ncStreamingOptions = _NcStreamingOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 6)
)


class _NcStreamingMmsIsEnabled_Type(Integer32):
    """Custom type ncStreamingMmsIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcStreamingMmsIsEnabled_Type.__name__ = "Integer32"
_NcStreamingMmsIsEnabled_Object = MibScalar
ncStreamingMmsIsEnabled = _NcStreamingMmsIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 6, 1),
    _NcStreamingMmsIsEnabled_Type()
)
ncStreamingMmsIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingMmsIsEnabled.setStatus("current")


class _NcStreamingMmsIsLicensed_Type(Integer32):
    """Custom type ncStreamingMmsIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcStreamingMmsIsLicensed_Type.__name__ = "Integer32"
_NcStreamingMmsIsLicensed_Object = MibScalar
ncStreamingMmsIsLicensed = _NcStreamingMmsIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 6, 2),
    _NcStreamingMmsIsLicensed_Type()
)
ncStreamingMmsIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingMmsIsLicensed.setStatus("current")


class _NcStreamingMmsProIsLicensed_Type(Integer32):
    """Custom type ncStreamingMmsProIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcStreamingMmsProIsLicensed_Type.__name__ = "Integer32"
_NcStreamingMmsProIsLicensed_Object = MibScalar
ncStreamingMmsProIsLicensed = _NcStreamingMmsProIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 6, 3),
    _NcStreamingMmsProIsLicensed_Type()
)
ncStreamingMmsProIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingMmsProIsLicensed.setStatus("current")


class _NcStreamingRtspIsEnabled_Type(Integer32):
    """Custom type ncStreamingRtspIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcStreamingRtspIsEnabled_Type.__name__ = "Integer32"
_NcStreamingRtspIsEnabled_Object = MibScalar
ncStreamingRtspIsEnabled = _NcStreamingRtspIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 6, 4),
    _NcStreamingRtspIsEnabled_Type()
)
ncStreamingRtspIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRtspIsEnabled.setStatus("current")


class _NcStreamingQuickTimeIsLicensed_Type(Integer32):
    """Custom type ncStreamingQuickTimeIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcStreamingQuickTimeIsLicensed_Type.__name__ = "Integer32"
_NcStreamingQuickTimeIsLicensed_Object = MibScalar
ncStreamingQuickTimeIsLicensed = _NcStreamingQuickTimeIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 6, 5),
    _NcStreamingQuickTimeIsLicensed_Type()
)
ncStreamingQuickTimeIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingQuickTimeIsLicensed.setStatus("current")


class _NcStreamingRealIsLicensed_Type(Integer32):
    """Custom type ncStreamingRealIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcStreamingRealIsLicensed_Type.__name__ = "Integer32"
_NcStreamingRealIsLicensed_Object = MibScalar
ncStreamingRealIsLicensed = _NcStreamingRealIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 6, 6),
    _NcStreamingRealIsLicensed_Type()
)
ncStreamingRealIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRealIsLicensed.setStatus("current")


class _NcStreamingMmsUltraIsLicensed_Type(Integer32):
    """Custom type ncStreamingMmsUltraIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcStreamingMmsUltraIsLicensed_Type.__name__ = "Integer32"
_NcStreamingMmsUltraIsLicensed_Object = MibScalar
ncStreamingMmsUltraIsLicensed = _NcStreamingMmsUltraIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 6, 7),
    _NcStreamingMmsUltraIsLicensed_Type()
)
ncStreamingMmsUltraIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingMmsUltraIsLicensed.setStatus("current")


class _NcStreamingRealProIsLicensed_Type(Integer32):
    """Custom type ncStreamingRealProIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcStreamingRealProIsLicensed_Type.__name__ = "Integer32"
_NcStreamingRealProIsLicensed_Object = MibScalar
ncStreamingRealProIsLicensed = _NcStreamingRealProIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 6, 8),
    _NcStreamingRealProIsLicensed_Type()
)
ncStreamingRealProIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRealProIsLicensed.setStatus("current")


class _NcStreamingRealUltraIsLicensed_Type(Integer32):
    """Custom type ncStreamingRealUltraIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcStreamingRealUltraIsLicensed_Type.__name__ = "Integer32"
_NcStreamingRealUltraIsLicensed_Object = MibScalar
ncStreamingRealUltraIsLicensed = _NcStreamingRealUltraIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 6, 9),
    _NcStreamingRealUltraIsLicensed_Type()
)
ncStreamingRealUltraIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRealUltraIsLicensed.setStatus("current")
_NcIcapOptions_ObjectIdentity = ObjectIdentity
ncIcapOptions = _NcIcapOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 7)
)


class _NcIcapIsEnabled_Type(Integer32):
    """Custom type ncIcapIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcIcapIsEnabled_Type.__name__ = "Integer32"
_NcIcapIsEnabled_Object = MibScalar
ncIcapIsEnabled = _NcIcapIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 7, 1),
    _NcIcapIsEnabled_Type()
)
ncIcapIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncIcapIsEnabled.setStatus("current")


class _NcIcapIsLicensed_Type(Integer32):
    """Custom type ncIcapIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcIcapIsLicensed_Type.__name__ = "Integer32"
_NcIcapIsLicensed_Object = MibScalar
ncIcapIsLicensed = _NcIcapIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 7, 2),
    _NcIcapIsLicensed_Type()
)
ncIcapIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncIcapIsLicensed.setStatus("current")


class _NcIcapv1IsEnabled_Type(Integer32):
    """Custom type ncIcapv1IsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcIcapv1IsEnabled_Type.__name__ = "Integer32"
_NcIcapv1IsEnabled_Object = MibScalar
ncIcapv1IsEnabled = _NcIcapv1IsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 7, 3),
    _NcIcapv1IsEnabled_Type()
)
ncIcapv1IsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncIcapv1IsEnabled.setStatus("current")
_NcGrmOptions_ObjectIdentity = ObjectIdentity
ncGrmOptions = _NcGrmOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 8)
)
_NcGrmServerOptions_ObjectIdentity = ObjectIdentity
ncGrmServerOptions = _NcGrmServerOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 8, 1)
)


class _NcGrmServerIsEnabled_Type(Integer32):
    """Custom type ncGrmServerIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcGrmServerIsEnabled_Type.__name__ = "Integer32"
_NcGrmServerIsEnabled_Object = MibScalar
ncGrmServerIsEnabled = _NcGrmServerIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 8, 1, 1),
    _NcGrmServerIsEnabled_Type()
)
ncGrmServerIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncGrmServerIsEnabled.setStatus("current")


class _NcGrmServerIsLicensed_Type(Integer32):
    """Custom type ncGrmServerIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcGrmServerIsLicensed_Type.__name__ = "Integer32"
_NcGrmServerIsLicensed_Object = MibScalar
ncGrmServerIsLicensed = _NcGrmServerIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 8, 1, 2),
    _NcGrmServerIsLicensed_Type()
)
ncGrmServerIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncGrmServerIsLicensed.setStatus("current")
_NcGrmAgentOptions_ObjectIdentity = ObjectIdentity
ncGrmAgentOptions = _NcGrmAgentOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 8, 2)
)


class _NcGrmAgentIsEnabled_Type(Integer32):
    """Custom type ncGrmAgentIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcGrmAgentIsEnabled_Type.__name__ = "Integer32"
_NcGrmAgentIsEnabled_Object = MibScalar
ncGrmAgentIsEnabled = _NcGrmAgentIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 8, 2, 1),
    _NcGrmAgentIsEnabled_Type()
)
ncGrmAgentIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncGrmAgentIsEnabled.setStatus("current")


class _NcGrmAgentIsLicensed_Type(Integer32):
    """Custom type ncGrmAgentIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcGrmAgentIsLicensed_Type.__name__ = "Integer32"
_NcGrmAgentIsLicensed_Object = MibScalar
ncGrmAgentIsLicensed = _NcGrmAgentIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 8, 2, 2),
    _NcGrmAgentIsLicensed_Type()
)
ncGrmAgentIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncGrmAgentIsLicensed.setStatus("current")
_NcCdOptions_ObjectIdentity = ObjectIdentity
ncCdOptions = _NcCdOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 9)
)


class _NcCdIsEnabled_Type(Integer32):
    """Custom type ncCdIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcCdIsEnabled_Type.__name__ = "Integer32"
_NcCdIsEnabled_Object = MibScalar
ncCdIsEnabled = _NcCdIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 9, 1),
    _NcCdIsEnabled_Type()
)
ncCdIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncCdIsEnabled.setStatus("current")
_NcHttpsProxyOptions_ObjectIdentity = ObjectIdentity
ncHttpsProxyOptions = _NcHttpsProxyOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 10)
)


class _NcHttpsProxyIsEnabled_Type(Integer32):
    """Custom type ncHttpsProxyIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcHttpsProxyIsEnabled_Type.__name__ = "Integer32"
_NcHttpsProxyIsEnabled_Object = MibScalar
ncHttpsProxyIsEnabled = _NcHttpsProxyIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 10, 1),
    _NcHttpsProxyIsEnabled_Type()
)
ncHttpsProxyIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpsProxyIsEnabled.setStatus("current")


class _NcHttpsProxyIsLicensed_Type(Integer32):
    """Custom type ncHttpsProxyIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcHttpsProxyIsLicensed_Type.__name__ = "Integer32"
_NcHttpsProxyIsLicensed_Object = MibScalar
ncHttpsProxyIsLicensed = _NcHttpsProxyIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 10, 2),
    _NcHttpsProxyIsLicensed_Type()
)
ncHttpsProxyIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpsProxyIsLicensed.setStatus("current")
_NcCmsOptions_ObjectIdentity = ObjectIdentity
ncCmsOptions = _NcCmsOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 11)
)


class _NcCmsIsEnabled_Type(Integer32):
    """Custom type ncCmsIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcCmsIsEnabled_Type.__name__ = "Integer32"
_NcCmsIsEnabled_Object = MibScalar
ncCmsIsEnabled = _NcCmsIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 1, 11, 1),
    _NcCmsIsEnabled_Type()
)
ncCmsIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncCmsIsEnabled.setStatus("current")
_NcInfo_ObjectIdentity = ObjectIdentity
ncInfo = _NcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2)
)
_NcVersion_Type = DisplayString
_NcVersion_Object = MibScalar
ncVersion = _NcVersion_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 1),
    _NcVersion_Type()
)
ncVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncVersion.setStatus("current")
_NcAdminPort_Type = Integer32
_NcAdminPort_Object = MibScalar
ncAdminPort = _NcAdminPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 2),
    _NcAdminPort_Type()
)
ncAdminPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncAdminPort.setStatus("current")
_Accelmonitor_ObjectIdentity = ObjectIdentity
accelmonitor = _Accelmonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 3)
)
_AmNumber_Type = Integer32
_AmNumber_Object = MibScalar
amNumber = _AmNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 3, 1),
    _AmNumber_Type()
)
amNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amNumber.setStatus("current")


class _AmMonitor_Type(Integer32):
    """Custom type amMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("togglea", 1),
          ("toggleb", 2))
    )


_AmMonitor_Type.__name__ = "Integer32"
_AmMonitor_Object = MibScalar
amMonitor = _AmMonitor_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 3, 2),
    _AmMonitor_Type()
)
amMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amMonitor.setStatus("current")
_AmMonitorString_Type = DisplayString
_AmMonitorString_Object = MibScalar
amMonitorString = _AmMonitorString_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 3, 3),
    _AmMonitorString_Type()
)
amMonitorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amMonitorString.setStatus("current")
_AmTable_Object = MibTable
amTable = _AmTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 3, 4)
)
if mibBuilder.loadTexts:
    amTable.setStatus("current")
_AmEntry_Object = MibTableRow
amEntry = _AmEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 3, 4, 1)
)
amEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "amIndex"),
)
if mibBuilder.loadTexts:
    amEntry.setStatus("current")


class _AmIndex_Type(Integer32):
    """Custom type amIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AmIndex_Type.__name__ = "Integer32"
_AmIndex_Object = MibTableColumn
amIndex = _AmIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 3, 4, 1, 1),
    _AmIndex_Type()
)
amIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amIndex.setStatus("current")
_AmAddress_Type = IpAddress
_AmAddress_Object = MibTableColumn
amAddress = _AmAddress_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 3, 4, 1, 2),
    _AmAddress_Type()
)
amAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amAddress.setStatus("current")


class _AmPort_Type(Integer32):
    """Custom type amPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AmPort_Type.__name__ = "Integer32"
_AmPort_Object = MibTableColumn
amPort = _AmPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 3, 4, 1, 3),
    _AmPort_Type()
)
amPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amPort.setStatus("current")


class _AmStatus_Type(Integer32):
    """Custom type amStatus based on Integer32"""
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
        *(("active", 1),
          ("down", 3),
          ("inactive", 4),
          ("up", 2))
    )


_AmStatus_Type.__name__ = "Integer32"
_AmStatus_Object = MibTableColumn
amStatus = _AmStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 3, 4, 1, 4),
    _AmStatus_Type()
)
amStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amStatus.setStatus("current")


class _NcLocalConfigChanged_Type(Integer32):
    """Custom type ncLocalConfigChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcLocalConfigChanged_Type.__name__ = "Integer32"
_NcLocalConfigChanged_Object = MibScalar
ncLocalConfigChanged = _NcLocalConfigChanged_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 4),
    _NcLocalConfigChanged_Type()
)
ncLocalConfigChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncLocalConfigChanged.setStatus("current")
_NcLocalConfigVersion_Type = Integer32
_NcLocalConfigVersion_Object = MibScalar
ncLocalConfigVersion = _NcLocalConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 5),
    _NcLocalConfigVersion_Type()
)
ncLocalConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncLocalConfigVersion.setStatus("current")
_GrmMonitor_ObjectIdentity = ObjectIdentity
grmMonitor = _GrmMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 6)
)


class _GrmMonitorToggle_Type(Integer32):
    """Custom type grmMonitorToggle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("togglea", 1),
          ("toggleb", 2))
    )


_GrmMonitorToggle_Type.__name__ = "Integer32"
_GrmMonitorToggle_Object = MibScalar
grmMonitorToggle = _GrmMonitorToggle_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 6, 1),
    _GrmMonitorToggle_Type()
)
grmMonitorToggle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grmMonitorToggle.setStatus("current")
_GrmMonitorString_Type = DisplayString
_GrmMonitorString_Object = MibScalar
grmMonitorString = _GrmMonitorString_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 6, 2),
    _GrmMonitorString_Type()
)
grmMonitorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grmMonitorString.setStatus("current")
_Takeoverinfo_ObjectIdentity = ObjectIdentity
takeoverinfo = _Takeoverinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 7)
)
_TakeoverAddrs_Type = DisplayString
_TakeoverAddrs_Object = MibScalar
takeoverAddrs = _TakeoverAddrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 7, 1),
    _TakeoverAddrs_Type()
)
takeoverAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    takeoverAddrs.setStatus("current")


class _TakeoverMode_Type(Integer32):
    """Custom type takeoverMode based on Integer32"""
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
        *(("giveback", 4),
          ("normal", 1),
          ("takenover", 3),
          ("takingover", 2))
    )


_TakeoverMode_Type.__name__ = "Integer32"
_TakeoverMode_Object = MibScalar
takeoverMode = _TakeoverMode_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 7, 2),
    _TakeoverMode_Type()
)
takeoverMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    takeoverMode.setStatus("current")


class _TakeoverStatus_Type(Integer32):
    """Custom type takeoverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("unknown", 2),
          ("up", 1))
    )


_TakeoverStatus_Type.__name__ = "Integer32"
_TakeoverStatus_Object = MibScalar
takeoverStatus = _TakeoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 2, 7, 3),
    _TakeoverStatus_Type()
)
takeoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    takeoverStatus.setStatus("current")
_NcStats_ObjectIdentity = ObjectIdentity
ncStats = _NcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3)
)
_NcObjectsStored_Type = Integer32
_NcObjectsStored_Object = MibScalar
ncObjectsStored = _NcObjectsStored_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 1),
    _NcObjectsStored_Type()
)
ncObjectsStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncObjectsStored.setStatus("current")
_NcBytesToClients_Type = Counter32
_NcBytesToClients_Object = MibScalar
ncBytesToClients = _NcBytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 2),
    _NcBytesToClients_Type()
)
ncBytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncBytesToClients.setStatus("current")
_NcBytesFromClients_Type = Counter32
_NcBytesFromClients_Object = MibScalar
ncBytesFromClients = _NcBytesFromClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 3),
    _NcBytesFromClients_Type()
)
ncBytesFromClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncBytesFromClients.setStatus("current")
_NcBytesToServers_Type = Counter32
_NcBytesToServers_Object = MibScalar
ncBytesToServers = _NcBytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 4),
    _NcBytesToServers_Type()
)
ncBytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncBytesToServers.setStatus("current")
_NcBytesFromServers_Type = Counter32
_NcBytesFromServers_Object = MibScalar
ncBytesFromServers = _NcBytesFromServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 5),
    _NcBytesFromServers_Type()
)
ncBytesFromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncBytesFromServers.setStatus("current")
_NcHttp_ObjectIdentity = ObjectIdentity
ncHttp = _NcHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6)
)
_NcHttpTotalRequests_Type = Counter32
_NcHttpTotalRequests_Object = MibScalar
ncHttpTotalRequests = _NcHttpTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 1),
    _NcHttpTotalRequests_Type()
)
ncHttpTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpTotalRequests.setStatus("current")
_NcHttpHitRequests_Type = Counter32
_NcHttpHitRequests_Object = MibScalar
ncHttpHitRequests = _NcHttpHitRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 2),
    _NcHttpHitRequests_Type()
)
ncHttpHitRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpHitRequests.setStatus("current")
_NcHttpMissRequests_Type = Counter32
_NcHttpMissRequests_Object = MibScalar
ncHttpMissRequests = _NcHttpMissRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 3),
    _NcHttpMissRequests_Type()
)
ncHttpMissRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpMissRequests.setStatus("current")
_NcHttpServConns_Type = Integer32
_NcHttpServConns_Object = MibScalar
ncHttpServConns = _NcHttpServConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 4),
    _NcHttpServConns_Type()
)
ncHttpServConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpServConns.setStatus("current")
_NcHttpCliConns_Type = Integer32
_NcHttpCliConns_Object = MibScalar
ncHttpCliConns = _NcHttpCliConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 5),
    _NcHttpCliConns_Type()
)
ncHttpCliConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpCliConns.setStatus("current")
_NcHttpBWSavings_Type = Integer32
_NcHttpBWSavings_Object = MibScalar
ncHttpBWSavings = _NcHttpBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 6),
    _NcHttpBWSavings_Type()
)
ncHttpBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpBWSavings.setStatus("current")
_NcHttpObjHitrate_Type = Integer32
_NcHttpObjHitrate_Object = MibScalar
ncHttpObjHitrate = _NcHttpObjHitrate_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 7),
    _NcHttpObjHitrate_Type()
)
ncHttpObjHitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpObjHitrate.setStatus("current")
_NcHttpRespTimePerByte_Type = Integer32
_NcHttpRespTimePerByte_Object = MibScalar
ncHttpRespTimePerByte = _NcHttpRespTimePerByte_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 8),
    _NcHttpRespTimePerByte_Type()
)
ncHttpRespTimePerByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpRespTimePerByte.setStatus("current")
_NcHttpAvgRespTime_Type = Integer32
_NcHttpAvgRespTime_Object = MibScalar
ncHttpAvgRespTime = _NcHttpAvgRespTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 9),
    _NcHttpAvgRespTime_Type()
)
ncHttpAvgRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpAvgRespTime.setStatus("current")
_NcHttpAvgHitRespTime_Type = Integer32
_NcHttpAvgHitRespTime_Object = MibScalar
ncHttpAvgHitRespTime = _NcHttpAvgHitRespTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 10),
    _NcHttpAvgHitRespTime_Type()
)
ncHttpAvgHitRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpAvgHitRespTime.setStatus("current")
_NcHttpAvgMissRespTime_Type = Integer32
_NcHttpAvgMissRespTime_Object = MibScalar
ncHttpAvgMissRespTime = _NcHttpAvgMissRespTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 11),
    _NcHttpAvgMissRespTime_Type()
)
ncHttpAvgMissRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpAvgMissRespTime.setStatus("current")
_NcHttpInstAvgRespTime_Type = Integer32
_NcHttpInstAvgRespTime_Object = MibScalar
ncHttpInstAvgRespTime = _NcHttpInstAvgRespTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 12),
    _NcHttpInstAvgRespTime_Type()
)
ncHttpInstAvgRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpInstAvgRespTime.setStatus("current")
_NcHttpInstAvgHitRespTime_Type = Integer32
_NcHttpInstAvgHitRespTime_Object = MibScalar
ncHttpInstAvgHitRespTime = _NcHttpInstAvgHitRespTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 13),
    _NcHttpInstAvgHitRespTime_Type()
)
ncHttpInstAvgHitRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpInstAvgHitRespTime.setStatus("current")
_NcHttpInstAvgMissRespTime_Type = Integer32
_NcHttpInstAvgMissRespTime_Object = MibScalar
ncHttpInstAvgMissRespTime = _NcHttpInstAvgMissRespTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 14),
    _NcHttpInstAvgMissRespTime_Type()
)
ncHttpInstAvgMissRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpInstAvgMissRespTime.setStatus("current")
_NcHttpTotalRespTime_Type = Integer32
_NcHttpTotalRespTime_Object = MibScalar
ncHttpTotalRespTime = _NcHttpTotalRespTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 15),
    _NcHttpTotalRespTime_Type()
)
ncHttpTotalRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpTotalRespTime.setStatus("current")
_NcHttpTotalHitRespTime_Type = Integer32
_NcHttpTotalHitRespTime_Object = MibScalar
ncHttpTotalHitRespTime = _NcHttpTotalHitRespTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 16),
    _NcHttpTotalHitRespTime_Type()
)
ncHttpTotalHitRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpTotalHitRespTime.setStatus("current")
_NcHttpTotalMissRespTime_Type = Integer32
_NcHttpTotalMissRespTime_Object = MibScalar
ncHttpTotalMissRespTime = _NcHttpTotalMissRespTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 17),
    _NcHttpTotalMissRespTime_Type()
)
ncHttpTotalMissRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpTotalMissRespTime.setStatus("current")
_NcHttpBytesToClients_Type = Counter32
_NcHttpBytesToClients_Object = MibScalar
ncHttpBytesToClients = _NcHttpBytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 18),
    _NcHttpBytesToClients_Type()
)
ncHttpBytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpBytesToClients.setStatus("current")
_NcHttpBytesFromClients_Type = Counter32
_NcHttpBytesFromClients_Object = MibScalar
ncHttpBytesFromClients = _NcHttpBytesFromClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 19),
    _NcHttpBytesFromClients_Type()
)
ncHttpBytesFromClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpBytesFromClients.setStatus("current")
_NcHttpBytesToServers_Type = Counter32
_NcHttpBytesToServers_Object = MibScalar
ncHttpBytesToServers = _NcHttpBytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 20),
    _NcHttpBytesToServers_Type()
)
ncHttpBytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpBytesToServers.setStatus("current")
_NcHttpBytesFromServers_Type = Counter32
_NcHttpBytesFromServers_Object = MibScalar
ncHttpBytesFromServers = _NcHttpBytesFromServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 21),
    _NcHttpBytesFromServers_Type()
)
ncHttpBytesFromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpBytesFromServers.setStatus("current")
_NcHttpHighTotalRespTimes_Type = Counter32
_NcHttpHighTotalRespTimes_Object = MibScalar
ncHttpHighTotalRespTimes = _NcHttpHighTotalRespTimes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 22),
    _NcHttpHighTotalRespTimes_Type()
)
ncHttpHighTotalRespTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpHighTotalRespTimes.setStatus("current")
_NcHttpLowTotalRespTimes_Type = Counter32
_NcHttpLowTotalRespTimes_Object = MibScalar
ncHttpLowTotalRespTimes = _NcHttpLowTotalRespTimes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 23),
    _NcHttpLowTotalRespTimes_Type()
)
ncHttpLowTotalRespTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpLowTotalRespTimes.setStatus("current")
_NcHttpHighTotalHitRespTimes_Type = Counter32
_NcHttpHighTotalHitRespTimes_Object = MibScalar
ncHttpHighTotalHitRespTimes = _NcHttpHighTotalHitRespTimes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 24),
    _NcHttpHighTotalHitRespTimes_Type()
)
ncHttpHighTotalHitRespTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpHighTotalHitRespTimes.setStatus("current")
_NcHttpLowTotalHitRespTimes_Type = Counter32
_NcHttpLowTotalHitRespTimes_Object = MibScalar
ncHttpLowTotalHitRespTimes = _NcHttpLowTotalHitRespTimes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 25),
    _NcHttpLowTotalHitRespTimes_Type()
)
ncHttpLowTotalHitRespTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpLowTotalHitRespTimes.setStatus("current")
_NcHttpHighTotalMissRespTimes_Type = Counter32
_NcHttpHighTotalMissRespTimes_Object = MibScalar
ncHttpHighTotalMissRespTimes = _NcHttpHighTotalMissRespTimes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 26),
    _NcHttpHighTotalMissRespTimes_Type()
)
ncHttpHighTotalMissRespTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpHighTotalMissRespTimes.setStatus("current")
_NcHttpLowTotalMissRespTimes_Type = Counter32
_NcHttpLowTotalMissRespTimes_Object = MibScalar
ncHttpLowTotalMissRespTimes = _NcHttpLowTotalMissRespTimes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 27),
    _NcHttpLowTotalMissRespTimes_Type()
)
ncHttpLowTotalMissRespTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpLowTotalMissRespTimes.setStatus("current")
_NcHttpReqRate_Type = Integer32
_NcHttpReqRate_Object = MibScalar
ncHttpReqRate = _NcHttpReqRate_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 28),
    _NcHttpReqRate_Type()
)
ncHttpReqRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpReqRate.setStatus("current")
_NcHttpObjHitRateLast1Min_Type = Integer32
_NcHttpObjHitRateLast1Min_Object = MibScalar
ncHttpObjHitRateLast1Min = _NcHttpObjHitRateLast1Min_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 29),
    _NcHttpObjHitRateLast1Min_Type()
)
ncHttpObjHitRateLast1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpObjHitRateLast1Min.setStatus("current")
_NcHttpObjHitRateLast5Min_Type = Integer32
_NcHttpObjHitRateLast5Min_Object = MibScalar
ncHttpObjHitRateLast5Min = _NcHttpObjHitRateLast5Min_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 30),
    _NcHttpObjHitRateLast5Min_Type()
)
ncHttpObjHitRateLast5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpObjHitRateLast5Min.setStatus("current")
_NcHttpByteHitRateLast1Min_Type = Integer32
_NcHttpByteHitRateLast1Min_Object = MibScalar
ncHttpByteHitRateLast1Min = _NcHttpByteHitRateLast1Min_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 31),
    _NcHttpByteHitRateLast1Min_Type()
)
ncHttpByteHitRateLast1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpByteHitRateLast1Min.setStatus("current")
_NcHttpByteHitRateLast5Min_Type = Integer32
_NcHttpByteHitRateLast5Min_Object = MibScalar
ncHttpByteHitRateLast5Min = _NcHttpByteHitRateLast5Min_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 32),
    _NcHttpByteHitRateLast5Min_Type()
)
ncHttpByteHitRateLast5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpByteHitRateLast5Min.setStatus("current")
_NcHttpBWSavingsLast1Min_Type = Integer32
_NcHttpBWSavingsLast1Min_Object = MibScalar
ncHttpBWSavingsLast1Min = _NcHttpBWSavingsLast1Min_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 33),
    _NcHttpBWSavingsLast1Min_Type()
)
ncHttpBWSavingsLast1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpBWSavingsLast1Min.setStatus("current")
_NcHttpBWSavingsLast5Min_Type = Integer32
_NcHttpBWSavingsLast5Min_Object = MibScalar
ncHttpBWSavingsLast5Min = _NcHttpBWSavingsLast5Min_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 34),
    _NcHttpBWSavingsLast5Min_Type()
)
ncHttpBWSavingsLast5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpBWSavingsLast5Min.setStatus("current")
_NcHttpActiveServConns_Type = Integer32
_NcHttpActiveServConns_Object = MibScalar
ncHttpActiveServConns = _NcHttpActiveServConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 35),
    _NcHttpActiveServConns_Type()
)
ncHttpActiveServConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpActiveServConns.setStatus("current")
_NcHttpActiveCliConns_Type = Integer32
_NcHttpActiveCliConns_Object = MibScalar
ncHttpActiveCliConns = _NcHttpActiveCliConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 36),
    _NcHttpActiveCliConns_Type()
)
ncHttpActiveCliConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpActiveCliConns.setStatus("current")
_NcHttpAccelTable_Object = MibTable
ncHttpAccelTable = _NcHttpAccelTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 37)
)
if mibBuilder.loadTexts:
    ncHttpAccelTable.setStatus("current")
_NcHttpAccelEntry_Object = MibTableRow
ncHttpAccelEntry = _NcHttpAccelEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 37, 1)
)
ncHttpAccelEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "ncHttpAccelIndex"),
)
if mibBuilder.loadTexts:
    ncHttpAccelEntry.setStatus("current")


class _NcHttpAccelIndex_Type(Integer32):
    """Custom type ncHttpAccelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 513),
    )


_NcHttpAccelIndex_Type.__name__ = "Integer32"
_NcHttpAccelIndex_Object = MibTableColumn
ncHttpAccelIndex = _NcHttpAccelIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 37, 1, 1),
    _NcHttpAccelIndex_Type()
)
ncHttpAccelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpAccelIndex.setStatus("current")
_NcHttpAccelKbytesFromClient_Type = Counter32
_NcHttpAccelKbytesFromClient_Object = MibTableColumn
ncHttpAccelKbytesFromClient = _NcHttpAccelKbytesFromClient_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 37, 1, 2),
    _NcHttpAccelKbytesFromClient_Type()
)
ncHttpAccelKbytesFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpAccelKbytesFromClient.setStatus("current")
_NcHttpAccelKbytesToClient_Type = Counter32
_NcHttpAccelKbytesToClient_Object = MibTableColumn
ncHttpAccelKbytesToClient = _NcHttpAccelKbytesToClient_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 37, 1, 3),
    _NcHttpAccelKbytesToClient_Type()
)
ncHttpAccelKbytesToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpAccelKbytesToClient.setStatus("current")
_NcHttpAccelHits_Type = Counter32
_NcHttpAccelHits_Object = MibTableColumn
ncHttpAccelHits = _NcHttpAccelHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 37, 1, 4),
    _NcHttpAccelHits_Type()
)
ncHttpAccelHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpAccelHits.setStatus("current")
_NcHttpsAccelTable_Object = MibTable
ncHttpsAccelTable = _NcHttpsAccelTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 38)
)
if mibBuilder.loadTexts:
    ncHttpsAccelTable.setStatus("current")
_NcHttpsAccelEntry_Object = MibTableRow
ncHttpsAccelEntry = _NcHttpsAccelEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 38, 1)
)
ncHttpsAccelEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "ncHttpsAccelIndex"),
)
if mibBuilder.loadTexts:
    ncHttpsAccelEntry.setStatus("current")


class _NcHttpsAccelIndex_Type(Integer32):
    """Custom type ncHttpsAccelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 513),
    )


_NcHttpsAccelIndex_Type.__name__ = "Integer32"
_NcHttpsAccelIndex_Object = MibTableColumn
ncHttpsAccelIndex = _NcHttpsAccelIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 38, 1, 1),
    _NcHttpsAccelIndex_Type()
)
ncHttpsAccelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpsAccelIndex.setStatus("current")
_NcHttpsAccelKbytesFromClient_Type = Counter32
_NcHttpsAccelKbytesFromClient_Object = MibTableColumn
ncHttpsAccelKbytesFromClient = _NcHttpsAccelKbytesFromClient_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 38, 1, 2),
    _NcHttpsAccelKbytesFromClient_Type()
)
ncHttpsAccelKbytesFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpsAccelKbytesFromClient.setStatus("current")
_NcHttpsAccelKbytesToClient_Type = Counter32
_NcHttpsAccelKbytesToClient_Object = MibTableColumn
ncHttpsAccelKbytesToClient = _NcHttpsAccelKbytesToClient_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 38, 1, 3),
    _NcHttpsAccelKbytesToClient_Type()
)
ncHttpsAccelKbytesToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpsAccelKbytesToClient.setStatus("current")
_NcHttpsAccelHits_Type = Counter32
_NcHttpsAccelHits_Object = MibTableColumn
ncHttpsAccelHits = _NcHttpsAccelHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 6, 38, 1, 4),
    _NcHttpsAccelHits_Type()
)
ncHttpsAccelHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHttpsAccelHits.setStatus("current")
_NcNntp_ObjectIdentity = ObjectIdentity
ncNntp = _NcNntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7)
)
_NcNntpTotalRequests_Type = Counter32
_NcNntpTotalRequests_Object = MibScalar
ncNntpTotalRequests = _NcNntpTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 1),
    _NcNntpTotalRequests_Type()
)
ncNntpTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpTotalRequests.setStatus("current")
_NcNntpCacheableRequests_Type = Counter32
_NcNntpCacheableRequests_Object = MibScalar
ncNntpCacheableRequests = _NcNntpCacheableRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 2),
    _NcNntpCacheableRequests_Type()
)
ncNntpCacheableRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpCacheableRequests.setStatus("current")
_NcNntpProxyRequests_Type = Counter32
_NcNntpProxyRequests_Object = MibScalar
ncNntpProxyRequests = _NcNntpProxyRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 3),
    _NcNntpProxyRequests_Type()
)
ncNntpProxyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpProxyRequests.setStatus("current")
_NcNntpServConns_Type = Integer32
_NcNntpServConns_Object = MibScalar
ncNntpServConns = _NcNntpServConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 4),
    _NcNntpServConns_Type()
)
ncNntpServConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpServConns.setStatus("current")
_NcNntpCliConns_Type = Integer32
_NcNntpCliConns_Object = MibScalar
ncNntpCliConns = _NcNntpCliConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 5),
    _NcNntpCliConns_Type()
)
ncNntpCliConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpCliConns.setStatus("current")
_NcNntpBWSavings_Type = Integer32
_NcNntpBWSavings_Object = MibScalar
ncNntpBWSavings = _NcNntpBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 6),
    _NcNntpBWSavings_Type()
)
ncNntpBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpBWSavings.setStatus("current")
_NcNntpRespTimePerByte_Type = Integer32
_NcNntpRespTimePerByte_Object = MibScalar
ncNntpRespTimePerByte = _NcNntpRespTimePerByte_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 7),
    _NcNntpRespTimePerByte_Type()
)
ncNntpRespTimePerByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpRespTimePerByte.setStatus("current")
_NcNntpBytesToClients_Type = Counter32
_NcNntpBytesToClients_Object = MibScalar
ncNntpBytesToClients = _NcNntpBytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 8),
    _NcNntpBytesToClients_Type()
)
ncNntpBytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpBytesToClients.setStatus("current")
_NcNntpBytesFromClients_Type = Counter32
_NcNntpBytesFromClients_Object = MibScalar
ncNntpBytesFromClients = _NcNntpBytesFromClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 9),
    _NcNntpBytesFromClients_Type()
)
ncNntpBytesFromClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpBytesFromClients.setStatus("current")
_NcNntpBytesToServers_Type = Counter32
_NcNntpBytesToServers_Object = MibScalar
ncNntpBytesToServers = _NcNntpBytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 10),
    _NcNntpBytesToServers_Type()
)
ncNntpBytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpBytesToServers.setStatus("current")
_NcNntpBytesFromServers_Type = Counter32
_NcNntpBytesFromServers_Object = MibScalar
ncNntpBytesFromServers = _NcNntpBytesFromServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 11),
    _NcNntpBytesFromServers_Type()
)
ncNntpBytesFromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpBytesFromServers.setStatus("current")
_NcNntpObjHitrate_Type = Integer32
_NcNntpObjHitrate_Object = MibScalar
ncNntpObjHitrate = _NcNntpObjHitrate_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 12),
    _NcNntpObjHitrate_Type()
)
ncNntpObjHitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpObjHitrate.setStatus("current")
_NcNntpActiveServConns_Type = Integer32
_NcNntpActiveServConns_Object = MibScalar
ncNntpActiveServConns = _NcNntpActiveServConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 13),
    _NcNntpActiveServConns_Type()
)
ncNntpActiveServConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpActiveServConns.setStatus("current")
_NcNntpActiveCliConns_Type = Integer32
_NcNntpActiveCliConns_Object = MibScalar
ncNntpActiveCliConns = _NcNntpActiveCliConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 7, 14),
    _NcNntpActiveCliConns_Type()
)
ncNntpActiveCliConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNntpActiveCliConns.setStatus("current")
_NcFtp_ObjectIdentity = ObjectIdentity
ncFtp = _NcFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8)
)
_NcFtpTotalRequests_Type = Counter32
_NcFtpTotalRequests_Object = MibScalar
ncFtpTotalRequests = _NcFtpTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 1),
    _NcFtpTotalRequests_Type()
)
ncFtpTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpTotalRequests.setStatus("current")
_NcFtpHitRequests_Type = Counter32
_NcFtpHitRequests_Object = MibScalar
ncFtpHitRequests = _NcFtpHitRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 2),
    _NcFtpHitRequests_Type()
)
ncFtpHitRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpHitRequests.setStatus("current")
_NcFtpMissRequests_Type = Counter32
_NcFtpMissRequests_Object = MibScalar
ncFtpMissRequests = _NcFtpMissRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 3),
    _NcFtpMissRequests_Type()
)
ncFtpMissRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpMissRequests.setStatus("current")
_NcFtpServConns_Type = Integer32
_NcFtpServConns_Object = MibScalar
ncFtpServConns = _NcFtpServConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 4),
    _NcFtpServConns_Type()
)
ncFtpServConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpServConns.setStatus("current")
_NcFtpCliConns_Type = Integer32
_NcFtpCliConns_Object = MibScalar
ncFtpCliConns = _NcFtpCliConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 5),
    _NcFtpCliConns_Type()
)
ncFtpCliConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpCliConns.setStatus("current")
_NcFtpBWSavings_Type = Integer32
_NcFtpBWSavings_Object = MibScalar
ncFtpBWSavings = _NcFtpBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 6),
    _NcFtpBWSavings_Type()
)
ncFtpBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpBWSavings.setStatus("current")
_NcFtpRespTimePerByte_Type = Integer32
_NcFtpRespTimePerByte_Object = MibScalar
ncFtpRespTimePerByte = _NcFtpRespTimePerByte_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 7),
    _NcFtpRespTimePerByte_Type()
)
ncFtpRespTimePerByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpRespTimePerByte.setStatus("current")
_NcFtpBytesToClients_Type = Counter32
_NcFtpBytesToClients_Object = MibScalar
ncFtpBytesToClients = _NcFtpBytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 8),
    _NcFtpBytesToClients_Type()
)
ncFtpBytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpBytesToClients.setStatus("current")
_NcFtpBytesFromClients_Type = Counter32
_NcFtpBytesFromClients_Object = MibScalar
ncFtpBytesFromClients = _NcFtpBytesFromClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 9),
    _NcFtpBytesFromClients_Type()
)
ncFtpBytesFromClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpBytesFromClients.setStatus("current")
_NcFtpBytesToServers_Type = Counter32
_NcFtpBytesToServers_Object = MibScalar
ncFtpBytesToServers = _NcFtpBytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 10),
    _NcFtpBytesToServers_Type()
)
ncFtpBytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpBytesToServers.setStatus("current")
_NcFtpBytesFromServers_Type = Counter32
_NcFtpBytesFromServers_Object = MibScalar
ncFtpBytesFromServers = _NcFtpBytesFromServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 11),
    _NcFtpBytesFromServers_Type()
)
ncFtpBytesFromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpBytesFromServers.setStatus("current")
_NcFtpObjHitrate_Type = Integer32
_NcFtpObjHitrate_Object = MibScalar
ncFtpObjHitrate = _NcFtpObjHitrate_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 12),
    _NcFtpObjHitrate_Type()
)
ncFtpObjHitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpObjHitrate.setStatus("current")
_NcFtpActiveServConns_Type = Integer32
_NcFtpActiveServConns_Object = MibScalar
ncFtpActiveServConns = _NcFtpActiveServConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 13),
    _NcFtpActiveServConns_Type()
)
ncFtpActiveServConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpActiveServConns.setStatus("current")
_NcFtpActiveCliConns_Type = Integer32
_NcFtpActiveCliConns_Object = MibScalar
ncFtpActiveCliConns = _NcFtpActiveCliConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 8, 14),
    _NcFtpActiveCliConns_Type()
)
ncFtpActiveCliConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncFtpActiveCliConns.setStatus("current")
_NcStreaming_ObjectIdentity = ObjectIdentity
ncStreaming = _NcStreaming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9)
)
_NcStreamingServConns_Type = Integer32
_NcStreamingServConns_Object = MibScalar
ncStreamingServConns = _NcStreamingServConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 1),
    _NcStreamingServConns_Type()
)
ncStreamingServConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingServConns.setStatus("current")
_NcStreamingCliConns_Type = Integer32
_NcStreamingCliConns_Object = MibScalar
ncStreamingCliConns = _NcStreamingCliConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 2),
    _NcStreamingCliConns_Type()
)
ncStreamingCliConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingCliConns.setStatus("current")
_NcStreamingBWSavings_Type = Integer32
_NcStreamingBWSavings_Object = MibScalar
ncStreamingBWSavings = _NcStreamingBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 3),
    _NcStreamingBWSavings_Type()
)
ncStreamingBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingBWSavings.setStatus("current")
_NcStreamingRespTimePerByte_Type = Integer32
_NcStreamingRespTimePerByte_Object = MibScalar
ncStreamingRespTimePerByte = _NcStreamingRespTimePerByte_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 4),
    _NcStreamingRespTimePerByte_Type()
)
ncStreamingRespTimePerByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRespTimePerByte.setStatus("current")
_NcStreamingHitRequests_Type = Counter32
_NcStreamingHitRequests_Object = MibScalar
ncStreamingHitRequests = _NcStreamingHitRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 5),
    _NcStreamingHitRequests_Type()
)
ncStreamingHitRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingHitRequests.setStatus("current")
_NcStreamingMissRequests_Type = Counter32
_NcStreamingMissRequests_Object = MibScalar
ncStreamingMissRequests = _NcStreamingMissRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 6),
    _NcStreamingMissRequests_Type()
)
ncStreamingMissRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingMissRequests.setStatus("current")
_NcStreamingTotalRequests_Type = Counter32
_NcStreamingTotalRequests_Object = MibScalar
ncStreamingTotalRequests = _NcStreamingTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 7),
    _NcStreamingTotalRequests_Type()
)
ncStreamingTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingTotalRequests.setStatus("current")
_NcStreamingLiveBytesToClients_Type = Counter32
_NcStreamingLiveBytesToClients_Object = MibScalar
ncStreamingLiveBytesToClients = _NcStreamingLiveBytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 8),
    _NcStreamingLiveBytesToClients_Type()
)
ncStreamingLiveBytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingLiveBytesToClients.setStatus("current")
_NcStreamingLiveBytesFromClients_Type = Counter32
_NcStreamingLiveBytesFromClients_Object = MibScalar
ncStreamingLiveBytesFromClients = _NcStreamingLiveBytesFromClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 9),
    _NcStreamingLiveBytesFromClients_Type()
)
ncStreamingLiveBytesFromClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingLiveBytesFromClients.setStatus("current")
_NcStreamingLiveBytesToServers_Type = Counter32
_NcStreamingLiveBytesToServers_Object = MibScalar
ncStreamingLiveBytesToServers = _NcStreamingLiveBytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 10),
    _NcStreamingLiveBytesToServers_Type()
)
ncStreamingLiveBytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingLiveBytesToServers.setStatus("current")
_NcStreamingLiveBytesFromServers_Type = Counter32
_NcStreamingLiveBytesFromServers_Object = MibScalar
ncStreamingLiveBytesFromServers = _NcStreamingLiveBytesFromServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 11),
    _NcStreamingLiveBytesFromServers_Type()
)
ncStreamingLiveBytesFromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingLiveBytesFromServers.setStatus("current")
_NcStreamingProxyBytesToClients_Type = Counter32
_NcStreamingProxyBytesToClients_Object = MibScalar
ncStreamingProxyBytesToClients = _NcStreamingProxyBytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 12),
    _NcStreamingProxyBytesToClients_Type()
)
ncStreamingProxyBytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingProxyBytesToClients.setStatus("current")
_NcStreamingProxyBytesFromClients_Type = Counter32
_NcStreamingProxyBytesFromClients_Object = MibScalar
ncStreamingProxyBytesFromClients = _NcStreamingProxyBytesFromClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 13),
    _NcStreamingProxyBytesFromClients_Type()
)
ncStreamingProxyBytesFromClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingProxyBytesFromClients.setStatus("current")
_NcStreamingProxyBytesToServers_Type = Counter32
_NcStreamingProxyBytesToServers_Object = MibScalar
ncStreamingProxyBytesToServers = _NcStreamingProxyBytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 14),
    _NcStreamingProxyBytesToServers_Type()
)
ncStreamingProxyBytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingProxyBytesToServers.setStatus("current")
_NcStreamingProxyBytesFromServers_Type = Counter32
_NcStreamingProxyBytesFromServers_Object = MibScalar
ncStreamingProxyBytesFromServers = _NcStreamingProxyBytesFromServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 15),
    _NcStreamingProxyBytesFromServers_Type()
)
ncStreamingProxyBytesFromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingProxyBytesFromServers.setStatus("current")
_NcStreamingOBTClients_Type = Counter32
_NcStreamingOBTClients_Object = MibScalar
ncStreamingOBTClients = _NcStreamingOBTClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 16),
    _NcStreamingOBTClients_Type()
)
ncStreamingOBTClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingOBTClients.setStatus("current")
_NcStreamingOBFClients_Type = Counter32
_NcStreamingOBFClients_Object = MibScalar
ncStreamingOBFClients = _NcStreamingOBFClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 17),
    _NcStreamingOBFClients_Type()
)
ncStreamingOBFClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingOBFClients.setStatus("current")
_NcStreamingOBTServers_Type = Counter32
_NcStreamingOBTServers_Object = MibScalar
ncStreamingOBTServers = _NcStreamingOBTServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 18),
    _NcStreamingOBTServers_Type()
)
ncStreamingOBTServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingOBTServers.setStatus("current")
_NcStreamingOBFServers_Type = Counter32
_NcStreamingOBFServers_Object = MibScalar
ncStreamingOBFServers = _NcStreamingOBFServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 19),
    _NcStreamingOBFServers_Type()
)
ncStreamingOBFServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingOBFServers.setStatus("current")
_NcStreamingObjHitrate_Type = Integer32
_NcStreamingObjHitrate_Object = MibScalar
ncStreamingObjHitrate = _NcStreamingObjHitrate_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 20),
    _NcStreamingObjHitrate_Type()
)
ncStreamingObjHitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingObjHitrate.setStatus("current")
_NcStreamingRealBytesToClients_Type = Counter32
_NcStreamingRealBytesToClients_Object = MibScalar
ncStreamingRealBytesToClients = _NcStreamingRealBytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 21),
    _NcStreamingRealBytesToClients_Type()
)
ncStreamingRealBytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRealBytesToClients.setStatus("current")
_NcStreamingRealBytesFromClients_Type = Counter32
_NcStreamingRealBytesFromClients_Object = MibScalar
ncStreamingRealBytesFromClients = _NcStreamingRealBytesFromClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 22),
    _NcStreamingRealBytesFromClients_Type()
)
ncStreamingRealBytesFromClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRealBytesFromClients.setStatus("current")
_NcStreamingRealBytesToServers_Type = Counter32
_NcStreamingRealBytesToServers_Object = MibScalar
ncStreamingRealBytesToServers = _NcStreamingRealBytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 23),
    _NcStreamingRealBytesToServers_Type()
)
ncStreamingRealBytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRealBytesToServers.setStatus("current")
_NcStreamingRealBytesFromServers_Type = Counter32
_NcStreamingRealBytesFromServers_Object = MibScalar
ncStreamingRealBytesFromServers = _NcStreamingRealBytesFromServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 24),
    _NcStreamingRealBytesFromServers_Type()
)
ncStreamingRealBytesFromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRealBytesFromServers.setStatus("current")
_NcStreamingMmsBytesToClients_Type = Counter32
_NcStreamingMmsBytesToClients_Object = MibScalar
ncStreamingMmsBytesToClients = _NcStreamingMmsBytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 25),
    _NcStreamingMmsBytesToClients_Type()
)
ncStreamingMmsBytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingMmsBytesToClients.setStatus("current")
_NcStreamingMmsBytesFromClients_Type = Counter32
_NcStreamingMmsBytesFromClients_Object = MibScalar
ncStreamingMmsBytesFromClients = _NcStreamingMmsBytesFromClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 26),
    _NcStreamingMmsBytesFromClients_Type()
)
ncStreamingMmsBytesFromClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingMmsBytesFromClients.setStatus("current")
_NcStreamingMmsBytesToServers_Type = Counter32
_NcStreamingMmsBytesToServers_Object = MibScalar
ncStreamingMmsBytesToServers = _NcStreamingMmsBytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 27),
    _NcStreamingMmsBytesToServers_Type()
)
ncStreamingMmsBytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingMmsBytesToServers.setStatus("current")
_NcStreamingMmsBytesFromServers_Type = Counter32
_NcStreamingMmsBytesFromServers_Object = MibScalar
ncStreamingMmsBytesFromServers = _NcStreamingMmsBytesFromServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 28),
    _NcStreamingMmsBytesFromServers_Type()
)
ncStreamingMmsBytesFromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingMmsBytesFromServers.setStatus("current")
_NcStreamingQTBTClients_Type = Counter32
_NcStreamingQTBTClients_Object = MibScalar
ncStreamingQTBTClients = _NcStreamingQTBTClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 29),
    _NcStreamingQTBTClients_Type()
)
ncStreamingQTBTClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingQTBTClients.setStatus("current")
_NcStreamingQTBFClients_Type = Counter32
_NcStreamingQTBFClients_Object = MibScalar
ncStreamingQTBFClients = _NcStreamingQTBFClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 30),
    _NcStreamingQTBFClients_Type()
)
ncStreamingQTBFClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingQTBFClients.setStatus("current")
_NcStreamingQTBTServers_Type = Counter32
_NcStreamingQTBTServers_Object = MibScalar
ncStreamingQTBTServers = _NcStreamingQTBTServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 31),
    _NcStreamingQTBTServers_Type()
)
ncStreamingQTBTServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingQTBTServers.setStatus("current")
_NcStreamingQTBFServers_Type = Counter32
_NcStreamingQTBFServers_Object = MibScalar
ncStreamingQTBFServers = _NcStreamingQTBFServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 32),
    _NcStreamingQTBFServers_Type()
)
ncStreamingQTBFServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingQTBFServers.setStatus("current")
_NcStreamingLiveBWSavings_Type = Integer32
_NcStreamingLiveBWSavings_Object = MibScalar
ncStreamingLiveBWSavings = _NcStreamingLiveBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 33),
    _NcStreamingLiveBWSavings_Type()
)
ncStreamingLiveBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingLiveBWSavings.setStatus("current")
_NcStreamingOndemandBWSavings_Type = Integer32
_NcStreamingOndemandBWSavings_Object = MibScalar
ncStreamingOndemandBWSavings = _NcStreamingOndemandBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 34),
    _NcStreamingOndemandBWSavings_Type()
)
ncStreamingOndemandBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingOndemandBWSavings.setStatus("current")
_NcStreamingRealBWSavings_Type = Integer32
_NcStreamingRealBWSavings_Object = MibScalar
ncStreamingRealBWSavings = _NcStreamingRealBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 35),
    _NcStreamingRealBWSavings_Type()
)
ncStreamingRealBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRealBWSavings.setStatus("current")
_NcStreamingMmsBWSavings_Type = Integer32
_NcStreamingMmsBWSavings_Object = MibScalar
ncStreamingMmsBWSavings = _NcStreamingMmsBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 36),
    _NcStreamingMmsBWSavings_Type()
)
ncStreamingMmsBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingMmsBWSavings.setStatus("current")
_NcStreamingQuickTimeBWSavings_Type = Integer32
_NcStreamingQuickTimeBWSavings_Object = MibScalar
ncStreamingQuickTimeBWSavings = _NcStreamingQuickTimeBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 37),
    _NcStreamingQuickTimeBWSavings_Type()
)
ncStreamingQuickTimeBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingQuickTimeBWSavings.setStatus("current")
_NcStreamingActiveServConns_Type = Integer32
_NcStreamingActiveServConns_Object = MibScalar
ncStreamingActiveServConns = _NcStreamingActiveServConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 38),
    _NcStreamingActiveServConns_Type()
)
ncStreamingActiveServConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingActiveServConns.setStatus("current")
_NcStreamingActiveCliConns_Type = Integer32
_NcStreamingActiveCliConns_Object = MibScalar
ncStreamingActiveCliConns = _NcStreamingActiveCliConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 39),
    _NcStreamingActiveCliConns_Type()
)
ncStreamingActiveCliConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingActiveCliConns.setStatus("current")
_NcStreamingRtspWMBytesToClients_Type = Counter32
_NcStreamingRtspWMBytesToClients_Object = MibScalar
ncStreamingRtspWMBytesToClients = _NcStreamingRtspWMBytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 40),
    _NcStreamingRtspWMBytesToClients_Type()
)
ncStreamingRtspWMBytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRtspWMBytesToClients.setStatus("current")
_NcStreamingRtspWMBFClients_Type = Counter32
_NcStreamingRtspWMBFClients_Object = MibScalar
ncStreamingRtspWMBFClients = _NcStreamingRtspWMBFClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 41),
    _NcStreamingRtspWMBFClients_Type()
)
ncStreamingRtspWMBFClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRtspWMBFClients.setStatus("current")
_NcStreamingRtspWMBytesToServers_Type = Counter32
_NcStreamingRtspWMBytesToServers_Object = MibScalar
ncStreamingRtspWMBytesToServers = _NcStreamingRtspWMBytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 42),
    _NcStreamingRtspWMBytesToServers_Type()
)
ncStreamingRtspWMBytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRtspWMBytesToServers.setStatus("current")
_NcStreamingRtspWMBFServers_Type = Counter32
_NcStreamingRtspWMBFServers_Object = MibScalar
ncStreamingRtspWMBFServers = _NcStreamingRtspWMBFServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 43),
    _NcStreamingRtspWMBFServers_Type()
)
ncStreamingRtspWMBFServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRtspWMBFServers.setStatus("current")
_NcStreamingRtspWMBWSavings_Type = Integer32
_NcStreamingRtspWMBWSavings_Object = MibScalar
ncStreamingRtspWMBWSavings = _NcStreamingRtspWMBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 44),
    _NcStreamingRtspWMBWSavings_Type()
)
ncStreamingRtspWMBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingRtspWMBWSavings.setStatus("current")
_NcStreamingAccelTable_Object = MibTable
ncStreamingAccelTable = _NcStreamingAccelTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 45)
)
if mibBuilder.loadTexts:
    ncStreamingAccelTable.setStatus("current")
_NcStreamingAccelEntry_Object = MibTableRow
ncStreamingAccelEntry = _NcStreamingAccelEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 45, 1)
)
ncStreamingAccelEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "ncStreamingAccelIndex"),
)
if mibBuilder.loadTexts:
    ncStreamingAccelEntry.setStatus("current")


class _NcStreamingAccelIndex_Type(Integer32):
    """Custom type ncStreamingAccelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 513),
    )


_NcStreamingAccelIndex_Type.__name__ = "Integer32"
_NcStreamingAccelIndex_Object = MibTableColumn
ncStreamingAccelIndex = _NcStreamingAccelIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 45, 1, 1),
    _NcStreamingAccelIndex_Type()
)
ncStreamingAccelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingAccelIndex.setStatus("current")
_NcStreamingAccelKbytesFromClient_Type = Counter32
_NcStreamingAccelKbytesFromClient_Object = MibTableColumn
ncStreamingAccelKbytesFromClient = _NcStreamingAccelKbytesFromClient_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 45, 1, 2),
    _NcStreamingAccelKbytesFromClient_Type()
)
ncStreamingAccelKbytesFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingAccelKbytesFromClient.setStatus("current")
_NcStreamingAccelKbytesToClient_Type = Counter32
_NcStreamingAccelKbytesToClient_Object = MibTableColumn
ncStreamingAccelKbytesToClient = _NcStreamingAccelKbytesToClient_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 45, 1, 3),
    _NcStreamingAccelKbytesToClient_Type()
)
ncStreamingAccelKbytesToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingAccelKbytesToClient.setStatus("current")
_NcStreamingAccelHits_Type = Counter32
_NcStreamingAccelHits_Object = MibTableColumn
ncStreamingAccelHits = _NcStreamingAccelHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 45, 1, 4),
    _NcStreamingAccelHits_Type()
)
ncStreamingAccelHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingAccelHits.setStatus("current")
_NcStreamingClientsDelayedSW_Type = Counter32
_NcStreamingClientsDelayedSW_Object = MibScalar
ncStreamingClientsDelayedSW = _NcStreamingClientsDelayedSW_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 9, 46),
    _NcStreamingClientsDelayedSW_Type()
)
ncStreamingClientsDelayedSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStreamingClientsDelayedSW.setStatus("current")
_NcTotalBWSavings_Type = Integer32
_NcTotalBWSavings_Object = MibScalar
ncTotalBWSavings = _NcTotalBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 10),
    _NcTotalBWSavings_Type()
)
ncTotalBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncTotalBWSavings.setStatus("current")
_NcDns_ObjectIdentity = ObjectIdentity
ncDns = _NcDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11)
)
_NcDnsRequestsReceived_Type = Counter32
_NcDnsRequestsReceived_Object = MibScalar
ncDnsRequestsReceived = _NcDnsRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 1),
    _NcDnsRequestsReceived_Type()
)
ncDnsRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsRequestsReceived.setStatus("current")
_NcDnsCacheHits_Type = Counter32
_NcDnsCacheHits_Object = MibScalar
ncDnsCacheHits = _NcDnsCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 2),
    _NcDnsCacheHits_Type()
)
ncDnsCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsCacheHits.setStatus("current")
_NcDnsCacheMisses_Type = Counter32
_NcDnsCacheMisses_Object = MibScalar
ncDnsCacheMisses = _NcDnsCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 3),
    _NcDnsCacheMisses_Type()
)
ncDnsCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsCacheMisses.setStatus("current")
_NcDnsSuccessfulForwardLookups_Type = Counter32
_NcDnsSuccessfulForwardLookups_Object = MibScalar
ncDnsSuccessfulForwardLookups = _NcDnsSuccessfulForwardLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 4),
    _NcDnsSuccessfulForwardLookups_Type()
)
ncDnsSuccessfulForwardLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsSuccessfulForwardLookups.setStatus("current")
_NcDnsFailedForwardLookups_Type = Counter32
_NcDnsFailedForwardLookups_Object = MibScalar
ncDnsFailedForwardLookups = _NcDnsFailedForwardLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 5),
    _NcDnsFailedForwardLookups_Type()
)
ncDnsFailedForwardLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsFailedForwardLookups.setStatus("current")
_NcDnsPendingForwardLookups_Type = Integer32
_NcDnsPendingForwardLookups_Object = MibScalar
ncDnsPendingForwardLookups = _NcDnsPendingForwardLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 6),
    _NcDnsPendingForwardLookups_Type()
)
ncDnsPendingForwardLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsPendingForwardLookups.setStatus("current")
_NcDnsSuccessfulReverseLookups_Type = Counter32
_NcDnsSuccessfulReverseLookups_Object = MibScalar
ncDnsSuccessfulReverseLookups = _NcDnsSuccessfulReverseLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 7),
    _NcDnsSuccessfulReverseLookups_Type()
)
ncDnsSuccessfulReverseLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsSuccessfulReverseLookups.setStatus("current")
_NcDnsFailedReverseLookups_Type = Counter32
_NcDnsFailedReverseLookups_Object = MibScalar
ncDnsFailedReverseLookups = _NcDnsFailedReverseLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 8),
    _NcDnsFailedReverseLookups_Type()
)
ncDnsFailedReverseLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsFailedReverseLookups.setStatus("current")
_NcDnsPendingReverseLookups_Type = Integer32
_NcDnsPendingReverseLookups_Object = MibScalar
ncDnsPendingReverseLookups = _NcDnsPendingReverseLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 9),
    _NcDnsPendingReverseLookups_Type()
)
ncDnsPendingReverseLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsPendingReverseLookups.setStatus("current")
_NcDnsIres_ObjectIdentity = ObjectIdentity
ncDnsIres = _NcDnsIres_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 10)
)


class _NcDnsIresIsEnabled_Type(Integer32):
    """Custom type ncDnsIresIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcDnsIresIsEnabled_Type.__name__ = "Integer32"
_NcDnsIresIsEnabled_Object = MibScalar
ncDnsIresIsEnabled = _NcDnsIresIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 10, 1),
    _NcDnsIresIsEnabled_Type()
)
ncDnsIresIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsIresIsEnabled.setStatus("current")


class _NcDnsIresIsInitialised_Type(Integer32):
    """Custom type ncDnsIresIsInitialised based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcDnsIresIsInitialised_Type.__name__ = "Integer32"
_NcDnsIresIsInitialised_Object = MibScalar
ncDnsIresIsInitialised = _NcDnsIresIsInitialised_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 10, 2),
    _NcDnsIresIsInitialised_Type()
)
ncDnsIresIsInitialised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsIresIsInitialised.setStatus("current")
_NcDnsIresForwardLookups_Type = Counter32
_NcDnsIresForwardLookups_Object = MibScalar
ncDnsIresForwardLookups = _NcDnsIresForwardLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 10, 3),
    _NcDnsIresForwardLookups_Type()
)
ncDnsIresForwardLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsIresForwardLookups.setStatus("current")
_NcDnsIresPendingForwardLookups_Type = Counter32
_NcDnsIresPendingForwardLookups_Object = MibScalar
ncDnsIresPendingForwardLookups = _NcDnsIresPendingForwardLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 10, 4),
    _NcDnsIresPendingForwardLookups_Type()
)
ncDnsIresPendingForwardLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsIresPendingForwardLookups.setStatus("current")
_NcDnsIresReverseLookups_Type = Counter32
_NcDnsIresReverseLookups_Object = MibScalar
ncDnsIresReverseLookups = _NcDnsIresReverseLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 10, 5),
    _NcDnsIresReverseLookups_Type()
)
ncDnsIresReverseLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsIresReverseLookups.setStatus("current")
_NcDnsIresPendingReverseLookups_Type = Counter32
_NcDnsIresPendingReverseLookups_Object = MibScalar
ncDnsIresPendingReverseLookups = _NcDnsIresPendingReverseLookups_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 11, 10, 6),
    _NcDnsIresPendingReverseLookups_Type()
)
ncDnsIresPendingReverseLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncDnsIresPendingReverseLookups.setStatus("current")
_NcAuth_ObjectIdentity = ObjectIdentity
ncAuth = _NcAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 12)
)
_NcNtlm_ObjectIdentity = ObjectIdentity
ncNtlm = _NcNtlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 12, 1)
)


class _NcNtlmPossibleProblem_Type(Integer32):
    """Custom type ncNtlmPossibleProblem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NcNtlmPossibleProblem_Type.__name__ = "Integer32"
_NcNtlmPossibleProblem_Object = MibScalar
ncNtlmPossibleProblem = _NcNtlmPossibleProblem_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 12, 1, 1),
    _NcNtlmPossibleProblem_Type()
)
ncNtlmPossibleProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncNtlmPossibleProblem.setStatus("current")
_NcRM_ObjectIdentity = ObjectIdentity
ncRM = _NcRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 13)
)
_NcRMMem_ObjectIdentity = ObjectIdentity
ncRMMem = _NcRMMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 13, 1)
)
_NcRMMemTotal_Type = Integer32
_NcRMMemTotal_Object = MibScalar
ncRMMemTotal = _NcRMMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 13, 1, 1),
    _NcRMMemTotal_Type()
)
ncRMMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncRMMemTotal.setStatus("current")
_NcRMMemFree_Type = Integer32
_NcRMMemFree_Object = MibScalar
ncRMMemFree = _NcRMMemFree_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 8, 3, 13, 1, 2),
    _NcRMMemFree_Type()
)
ncRMMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncRMMemFree.setStatus("current")
_Snapmirror_ObjectIdentity = ObjectIdentity
snapmirror = _Snapmirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 9)
)


class _SnapmirrorOn_Type(Integer32):
    """Custom type snapmirrorOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SnapmirrorOn_Type.__name__ = "Integer32"
_SnapmirrorOn_Object = MibScalar
snapmirrorOn = _SnapmirrorOn_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 1),
    _SnapmirrorOn_Type()
)
snapmirrorOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorOn.setStatus("current")
_SnapmirrorActiveRestoreCount_Type = Integer32
_SnapmirrorActiveRestoreCount_Object = MibScalar
snapmirrorActiveRestoreCount = _SnapmirrorActiveRestoreCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 2),
    _SnapmirrorActiveRestoreCount_Type()
)
snapmirrorActiveRestoreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorActiveRestoreCount.setStatus("current")
_SnapmirrorScheduledRestoreCount_Type = Integer32
_SnapmirrorScheduledRestoreCount_Object = MibScalar
snapmirrorScheduledRestoreCount = _SnapmirrorScheduledRestoreCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 3),
    _SnapmirrorScheduledRestoreCount_Type()
)
snapmirrorScheduledRestoreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorScheduledRestoreCount.setStatus("current")
_SnapmirrorBackupNumber_Type = Integer32
_SnapmirrorBackupNumber_Object = MibScalar
snapmirrorBackupNumber = _SnapmirrorBackupNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 4),
    _SnapmirrorBackupNumber_Type()
)
snapmirrorBackupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorBackupNumber.setStatus("current")
_SnapmirrorBackupSuccesses_Type = Counter32
_SnapmirrorBackupSuccesses_Object = MibScalar
snapmirrorBackupSuccesses = _SnapmirrorBackupSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 5),
    _SnapmirrorBackupSuccesses_Type()
)
snapmirrorBackupSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorBackupSuccesses.setStatus("current")
_SnapmirrorRestoreSuccesses_Type = Counter32
_SnapmirrorRestoreSuccesses_Object = MibScalar
snapmirrorRestoreSuccesses = _SnapmirrorRestoreSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 6),
    _SnapmirrorRestoreSuccesses_Type()
)
snapmirrorRestoreSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorRestoreSuccesses.setStatus("current")
_SnapmirrorBackupAborts_Type = Counter32
_SnapmirrorBackupAborts_Object = MibScalar
snapmirrorBackupAborts = _SnapmirrorBackupAborts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 7),
    _SnapmirrorBackupAborts_Type()
)
snapmirrorBackupAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorBackupAborts.setStatus("current")
_SnapmirrorRestoreRestartAborts_Type = Counter32
_SnapmirrorRestoreRestartAborts_Object = MibScalar
snapmirrorRestoreRestartAborts = _SnapmirrorRestoreRestartAborts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 8),
    _SnapmirrorRestoreRestartAborts_Type()
)
snapmirrorRestoreRestartAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorRestoreRestartAborts.setStatus("current")
_SnapmirrorRestoreWaitAborts_Type = Counter32
_SnapmirrorRestoreWaitAborts_Object = MibScalar
snapmirrorRestoreWaitAborts = _SnapmirrorRestoreWaitAborts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 9),
    _SnapmirrorRestoreWaitAborts_Type()
)
snapmirrorRestoreWaitAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorRestoreWaitAborts.setStatus("current")
_SnapmirrorWrittenBytes_Type = Counter32
_SnapmirrorWrittenBytes_Object = MibScalar
snapmirrorWrittenBytes = _SnapmirrorWrittenBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 10),
    _SnapmirrorWrittenBytes_Type()
)
snapmirrorWrittenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorWrittenBytes.setStatus("current")
_SnapmirrorReadBytes_Type = Counter32
_SnapmirrorReadBytes_Object = MibScalar
snapmirrorReadBytes = _SnapmirrorReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 11),
    _SnapmirrorReadBytes_Type()
)
snapmirrorReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorReadBytes.setStatus("current")
_SnapmirrorActiveDstNumber_Type = Integer32
_SnapmirrorActiveDstNumber_Object = MibScalar
snapmirrorActiveDstNumber = _SnapmirrorActiveDstNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 12),
    _SnapmirrorActiveDstNumber_Type()
)
snapmirrorActiveDstNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorActiveDstNumber.setStatus("current")
_SnapmirrorActiveSrcNumber_Type = Integer32
_SnapmirrorActiveSrcNumber_Object = MibScalar
snapmirrorActiveSrcNumber = _SnapmirrorActiveSrcNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 13),
    _SnapmirrorActiveSrcNumber_Type()
)
snapmirrorActiveSrcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorActiveSrcNumber.setStatus("current")
_SnapmirrorFilerTotalDstSuccesses_Type = Counter32
_SnapmirrorFilerTotalDstSuccesses_Object = MibScalar
snapmirrorFilerTotalDstSuccesses = _SnapmirrorFilerTotalDstSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 14),
    _SnapmirrorFilerTotalDstSuccesses_Type()
)
snapmirrorFilerTotalDstSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorFilerTotalDstSuccesses.setStatus("current")
_SnapmirrorFilerTotalSrcSuccesses_Type = Counter32
_SnapmirrorFilerTotalSrcSuccesses_Object = MibScalar
snapmirrorFilerTotalSrcSuccesses = _SnapmirrorFilerTotalSrcSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 15),
    _SnapmirrorFilerTotalSrcSuccesses_Type()
)
snapmirrorFilerTotalSrcSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorFilerTotalSrcSuccesses.setStatus("current")
_SnapmirrorFilerTotalSrcFailures_Type = Counter32
_SnapmirrorFilerTotalSrcFailures_Object = MibScalar
snapmirrorFilerTotalSrcFailures = _SnapmirrorFilerTotalSrcFailures_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 16),
    _SnapmirrorFilerTotalSrcFailures_Type()
)
snapmirrorFilerTotalSrcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorFilerTotalSrcFailures.setStatus("current")
_SnapmirrorFilerTotalDstFailures_Type = Counter32
_SnapmirrorFilerTotalDstFailures_Object = MibScalar
snapmirrorFilerTotalDstFailures = _SnapmirrorFilerTotalDstFailures_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 17),
    _SnapmirrorFilerTotalDstFailures_Type()
)
snapmirrorFilerTotalDstFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorFilerTotalDstFailures.setStatus("current")
_SnapmirrorFilerTotalDstDeferments_Type = Counter32
_SnapmirrorFilerTotalDstDeferments_Object = MibScalar
snapmirrorFilerTotalDstDeferments = _SnapmirrorFilerTotalDstDeferments_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 18),
    _SnapmirrorFilerTotalDstDeferments_Type()
)
snapmirrorFilerTotalDstDeferments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorFilerTotalDstDeferments.setStatus("current")


class _SnapmirrorIsLicensed_Type(Integer32):
    """Custom type snapmirrorIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SnapmirrorIsLicensed_Type.__name__ = "Integer32"
_SnapmirrorIsLicensed_Object = MibScalar
snapmirrorIsLicensed = _SnapmirrorIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 19),
    _SnapmirrorIsLicensed_Type()
)
snapmirrorIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorIsLicensed.setStatus("current")
_SnapmirrorStatusTable_Object = MibTable
snapmirrorStatusTable = _SnapmirrorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20)
)
if mibBuilder.loadTexts:
    snapmirrorStatusTable.setStatus("current")
_SnapmirrorStatusEntry_Object = MibTableRow
snapmirrorStatusEntry = _SnapmirrorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1)
)
snapmirrorStatusEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "snapmirrorIndex"),
)
if mibBuilder.loadTexts:
    snapmirrorStatusEntry.setStatus("current")


class _SnapmirrorIndex_Type(Integer32):
    """Custom type snapmirrorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnapmirrorIndex_Type.__name__ = "Integer32"
_SnapmirrorIndex_Object = MibTableColumn
snapmirrorIndex = _SnapmirrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 1),
    _SnapmirrorIndex_Type()
)
snapmirrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorIndex.setStatus("current")
_SnapmirrorSrc_Type = OctetString
_SnapmirrorSrc_Object = MibTableColumn
snapmirrorSrc = _SnapmirrorSrc_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 2),
    _SnapmirrorSrc_Type()
)
snapmirrorSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorSrc.setStatus("current")
_SnapmirrorDst_Type = OctetString
_SnapmirrorDst_Object = MibTableColumn
snapmirrorDst = _SnapmirrorDst_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 3),
    _SnapmirrorDst_Type()
)
snapmirrorDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorDst.setStatus("current")


class _SnapmirrorStatus_Type(Integer32):
    """Custom type snapmirrorStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 4),
          ("idle", 1),
          ("inSync", 10),
          ("migrating", 5),
          ("pending", 3),
          ("quiescing", 6),
          ("resyncing", 7),
          ("syncing", 9),
          ("transferring", 2),
          ("waiting", 8))
    )


_SnapmirrorStatus_Type.__name__ = "Integer32"
_SnapmirrorStatus_Object = MibTableColumn
snapmirrorStatus = _SnapmirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 4),
    _SnapmirrorStatus_Type()
)
snapmirrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorStatus.setStatus("current")


class _SnapmirrorState_Type(Integer32):
    """Custom type snapmirrorState based on Integer32"""
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
        *(("brokenOff", 3),
          ("quiesced", 4),
          ("snapmirrored", 2),
          ("source", 5),
          ("uninitialized", 1),
          ("unknown", 6))
    )


_SnapmirrorState_Type.__name__ = "Integer32"
_SnapmirrorState_Object = MibTableColumn
snapmirrorState = _SnapmirrorState_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 5),
    _SnapmirrorState_Type()
)
snapmirrorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorState.setStatus("current")
_SnapmirrorLag_Type = TimeTicks
_SnapmirrorLag_Object = MibTableColumn
snapmirrorLag = _SnapmirrorLag_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 6),
    _SnapmirrorLag_Type()
)
snapmirrorLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorLag.setStatus("current")
_SnapmirrorTotalSuccesses_Type = Counter32
_SnapmirrorTotalSuccesses_Object = MibTableColumn
snapmirrorTotalSuccesses = _SnapmirrorTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 7),
    _SnapmirrorTotalSuccesses_Type()
)
snapmirrorTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorTotalSuccesses.setStatus("current")
_SnapmirrorTotalRestartSuccesses_Type = Counter32
_SnapmirrorTotalRestartSuccesses_Object = MibTableColumn
snapmirrorTotalRestartSuccesses = _SnapmirrorTotalRestartSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 8),
    _SnapmirrorTotalRestartSuccesses_Type()
)
snapmirrorTotalRestartSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorTotalRestartSuccesses.setStatus("current")
_SnapmirrorTotalFailures_Type = Counter32
_SnapmirrorTotalFailures_Object = MibTableColumn
snapmirrorTotalFailures = _SnapmirrorTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 9),
    _SnapmirrorTotalFailures_Type()
)
snapmirrorTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorTotalFailures.setStatus("current")
_SnapmirrorTotalDeferments_Type = Counter32
_SnapmirrorTotalDeferments_Object = MibTableColumn
snapmirrorTotalDeferments = _SnapmirrorTotalDeferments_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 10),
    _SnapmirrorTotalDeferments_Type()
)
snapmirrorTotalDeferments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorTotalDeferments.setStatus("current")
_SnapmirrorTotalTransMBs_Type = Counter32
_SnapmirrorTotalTransMBs_Object = MibTableColumn
snapmirrorTotalTransMBs = _SnapmirrorTotalTransMBs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 11),
    _SnapmirrorTotalTransMBs_Type()
)
snapmirrorTotalTransMBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorTotalTransMBs.setStatus("current")
_SnapmirrorTotalTransTimeSeconds_Type = Counter32
_SnapmirrorTotalTransTimeSeconds_Object = MibTableColumn
snapmirrorTotalTransTimeSeconds = _SnapmirrorTotalTransTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 12),
    _SnapmirrorTotalTransTimeSeconds_Type()
)
snapmirrorTotalTransTimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorTotalTransTimeSeconds.setStatus("current")
_SnapmirrorThrottleValue_Type = Integer32
_SnapmirrorThrottleValue_Object = MibTableColumn
snapmirrorThrottleValue = _SnapmirrorThrottleValue_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 13),
    _SnapmirrorThrottleValue_Type()
)
snapmirrorThrottleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorThrottleValue.setStatus("current")
_SnapmirrorMirrorTimestamp_Type = DisplayString
_SnapmirrorMirrorTimestamp_Object = MibTableColumn
snapmirrorMirrorTimestamp = _SnapmirrorMirrorTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 14),
    _SnapmirrorMirrorTimestamp_Type()
)
snapmirrorMirrorTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorMirrorTimestamp.setStatus("current")
_SnapmirrorBaseSnapshot_Type = DisplayString
_SnapmirrorBaseSnapshot_Object = MibTableColumn
snapmirrorBaseSnapshot = _SnapmirrorBaseSnapshot_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 15),
    _SnapmirrorBaseSnapshot_Type()
)
snapmirrorBaseSnapshot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorBaseSnapshot.setStatus("current")
_SnapmirrorLastTransType_Type = DisplayString
_SnapmirrorLastTransType_Object = MibTableColumn
snapmirrorLastTransType = _SnapmirrorLastTransType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 16),
    _SnapmirrorLastTransType_Type()
)
snapmirrorLastTransType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorLastTransType.setStatus("current")
_SnapmirrorLastTransMBs_Type = Counter32
_SnapmirrorLastTransMBs_Object = MibTableColumn
snapmirrorLastTransMBs = _SnapmirrorLastTransMBs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 17),
    _SnapmirrorLastTransMBs_Type()
)
snapmirrorLastTransMBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorLastTransMBs.setStatus("current")
_SnapmirrorLastTransTimeSeconds_Type = Counter32
_SnapmirrorLastTransTimeSeconds_Object = MibTableColumn
snapmirrorLastTransTimeSeconds = _SnapmirrorLastTransTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 18),
    _SnapmirrorLastTransTimeSeconds_Type()
)
snapmirrorLastTransTimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorLastTransTimeSeconds.setStatus("current")
_SnapmirrorSchedule_Type = DisplayString
_SnapmirrorSchedule_Object = MibTableColumn
snapmirrorSchedule = _SnapmirrorSchedule_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 19),
    _SnapmirrorSchedule_Type()
)
snapmirrorSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorSchedule.setStatus("current")
_SnapmirrorScheduleDesc_Type = DisplayString
_SnapmirrorScheduleDesc_Object = MibTableColumn
snapmirrorScheduleDesc = _SnapmirrorScheduleDesc_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 20),
    _SnapmirrorScheduleDesc_Type()
)
snapmirrorScheduleDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorScheduleDesc.setStatus("current")
_SnapmirrorArguments_Type = DisplayString
_SnapmirrorArguments_Object = MibTableColumn
snapmirrorArguments = _SnapmirrorArguments_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 21),
    _SnapmirrorArguments_Type()
)
snapmirrorArguments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorArguments.setStatus("current")
_SnapmirrorSyncToAsync_Type = Counter32
_SnapmirrorSyncToAsync_Object = MibTableColumn
snapmirrorSyncToAsync = _SnapmirrorSyncToAsync_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 20, 1, 22),
    _SnapmirrorSyncToAsync_Type()
)
snapmirrorSyncToAsync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorSyncToAsync.setStatus("current")
_SnapmirrorConnTable_Object = MibTable
snapmirrorConnTable = _SnapmirrorConnTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 21)
)
if mibBuilder.loadTexts:
    snapmirrorConnTable.setStatus("current")
_SnapmirrorConnEntry_Object = MibTableRow
snapmirrorConnEntry = _SnapmirrorConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 21, 1)
)
snapmirrorConnEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "snapmirrorConnIndex"),
)
if mibBuilder.loadTexts:
    snapmirrorConnEntry.setStatus("current")


class _SnapmirrorConnIndex_Type(Integer32):
    """Custom type snapmirrorConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnapmirrorConnIndex_Type.__name__ = "Integer32"
_SnapmirrorConnIndex_Object = MibTableColumn
snapmirrorConnIndex = _SnapmirrorConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 21, 1, 1),
    _SnapmirrorConnIndex_Type()
)
snapmirrorConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorConnIndex.setStatus("current")
_SnapmirrorConnName_Type = DisplayString
_SnapmirrorConnName_Object = MibTableColumn
snapmirrorConnName = _SnapmirrorConnName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 21, 1, 2),
    _SnapmirrorConnName_Type()
)
snapmirrorConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorConnName.setStatus("current")


class _SnapmirrorConnType_Type(Integer32):
    """Custom type snapmirrorConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failover", 2),
          ("multi", 1))
    )


_SnapmirrorConnType_Type.__name__ = "Integer32"
_SnapmirrorConnType_Object = MibTableColumn
snapmirrorConnType = _SnapmirrorConnType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 21, 1, 3),
    _SnapmirrorConnType_Type()
)
snapmirrorConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorConnType.setStatus("current")
_SnapmirrorConnSrc1_Type = DisplayString
_SnapmirrorConnSrc1_Object = MibTableColumn
snapmirrorConnSrc1 = _SnapmirrorConnSrc1_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 21, 1, 4),
    _SnapmirrorConnSrc1_Type()
)
snapmirrorConnSrc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorConnSrc1.setStatus("current")
_SnapmirrorConnDst1_Type = DisplayString
_SnapmirrorConnDst1_Object = MibTableColumn
snapmirrorConnDst1 = _SnapmirrorConnDst1_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 21, 1, 5),
    _SnapmirrorConnDst1_Type()
)
snapmirrorConnDst1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorConnDst1.setStatus("current")
_SnapmirrorConnSrc2_Type = DisplayString
_SnapmirrorConnSrc2_Object = MibTableColumn
snapmirrorConnSrc2 = _SnapmirrorConnSrc2_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 21, 1, 6),
    _SnapmirrorConnSrc2_Type()
)
snapmirrorConnSrc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorConnSrc2.setStatus("current")
_SnapmirrorConnDst2_Type = DisplayString
_SnapmirrorConnDst2_Object = MibTableColumn
snapmirrorConnDst2 = _SnapmirrorConnDst2_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 9, 21, 1, 7),
    _SnapmirrorConnDst2_Type()
)
snapmirrorConnDst2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapmirrorConnDst2.setStatus("current")
_Ndmp_ObjectIdentity = ObjectIdentity
ndmp = _Ndmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 10)
)


class _NdmpOn_Type(Integer32):
    """Custom type ndmpOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NdmpOn_Type.__name__ = "Integer32"
_NdmpOn_Object = MibScalar
ndmpOn = _NdmpOn_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 10, 1),
    _NdmpOn_Type()
)
ndmpOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpOn.setStatus("current")
_NdmpSessionOpened_Type = Integer32
_NdmpSessionOpened_Object = MibScalar
ndmpSessionOpened = _NdmpSessionOpened_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 10, 2),
    _NdmpSessionOpened_Type()
)
ndmpSessionOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpSessionOpened.setStatus("current")
_NdmpBackupActive_Type = Integer32
_NdmpBackupActive_Object = MibScalar
ndmpBackupActive = _NdmpBackupActive_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 10, 3),
    _NdmpBackupActive_Type()
)
ndmpBackupActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpBackupActive.setStatus("current")
_NdmpRestoreActive_Type = Integer32
_NdmpRestoreActive_Object = MibScalar
ndmpRestoreActive = _NdmpRestoreActive_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 10, 4),
    _NdmpRestoreActive_Type()
)
ndmpRestoreActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpRestoreActive.setStatus("current")
_NdmpTapeActive_Type = Integer32
_NdmpTapeActive_Object = MibScalar
ndmpTapeActive = _NdmpTapeActive_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 10, 5),
    _NdmpTapeActive_Type()
)
ndmpTapeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpTapeActive.setStatus("current")
_NdmpBackupSuccesses_Type = Counter32
_NdmpBackupSuccesses_Object = MibScalar
ndmpBackupSuccesses = _NdmpBackupSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 10, 6),
    _NdmpBackupSuccesses_Type()
)
ndmpBackupSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpBackupSuccesses.setStatus("current")
_NdmpRestoreSuccesses_Type = Counter32
_NdmpRestoreSuccesses_Object = MibScalar
ndmpRestoreSuccesses = _NdmpRestoreSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 10, 7),
    _NdmpRestoreSuccesses_Type()
)
ndmpRestoreSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpRestoreSuccesses.setStatus("current")
_NdmpBackupFailures_Type = Counter32
_NdmpBackupFailures_Object = MibScalar
ndmpBackupFailures = _NdmpBackupFailures_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 10, 8),
    _NdmpBackupFailures_Type()
)
ndmpBackupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpBackupFailures.setStatus("current")
_NdmpRestoreFailures_Type = Counter32
_NdmpRestoreFailures_Object = MibScalar
ndmpRestoreFailures = _NdmpRestoreFailures_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 10, 9),
    _NdmpRestoreFailures_Type()
)
ndmpRestoreFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpRestoreFailures.setStatus("current")
_NdmpBackupFailureReason_Type = DisplayString
_NdmpBackupFailureReason_Object = MibScalar
ndmpBackupFailureReason = _NdmpBackupFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 10, 10),
    _NdmpBackupFailureReason_Type()
)
ndmpBackupFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpBackupFailureReason.setStatus("current")
_NdmpRestoreFailureReason_Type = DisplayString
_NdmpRestoreFailureReason_Object = MibScalar
ndmpRestoreFailureReason = _NdmpRestoreFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 10, 11),
    _NdmpRestoreFailureReason_Type()
)
ndmpRestoreFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndmpRestoreFailureReason.setStatus("current")
_Fabric_ObjectIdentity = ObjectIdentity
fabric = _Fabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 11)
)
_FabricInstances_Type = Integer32
_FabricInstances_Object = MibScalar
fabricInstances = _FabricInstances_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 1),
    _FabricInstances_Type()
)
fabricInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabricInstances.setStatus("current")
_FabricTable_Object = MibTable
fabricTable = _FabricTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 2)
)
if mibBuilder.loadTexts:
    fabricTable.setStatus("current")
_FabricEntry_Object = MibTableRow
fabricEntry = _FabricEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 2, 1)
)
fabricEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "fabricIndex"),
)
if mibBuilder.loadTexts:
    fabricEntry.setStatus("current")


class _FabricIndex_Type(Integer32):
    """Custom type fabricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FabricIndex_Type.__name__ = "Integer32"
_FabricIndex_Object = MibTableColumn
fabricIndex = _FabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 2, 1, 1),
    _FabricIndex_Type()
)
fabricIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabricIndex.setStatus("current")


class _FabricStatus_Type(Integer32):
    """Custom type fabricStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_FabricStatus_Type.__name__ = "Integer32"
_FabricStatus_Object = MibTableColumn
fabricStatus = _FabricStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 2, 1, 2),
    _FabricStatus_Type()
)
fabricStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabricStatus.setStatus("current")
_FabricStatusMessage_Type = DisplayString
_FabricStatusMessage_Object = MibTableColumn
fabricStatusMessage = _FabricStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 2, 1, 3),
    _FabricStatusMessage_Type()
)
fabricStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabricStatusMessage.setStatus("current")


class _FabricName_Type(OctetString):
    """Custom type fabricName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FabricName_Type.__name__ = "OctetString"
_FabricName_Object = MibTableColumn
fabricName = _FabricName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 2, 1, 4),
    _FabricName_Type()
)
fabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabricName.setStatus("current")


class _FabricOwner_Type(Integer32):
    """Custom type fabricOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("netapp", 1),
          ("other", 2),
          ("unknown", 3))
    )


_FabricOwner_Type.__name__ = "Integer32"
_FabricOwner_Object = MibTableColumn
fabricOwner = _FabricOwner_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 2, 1, 5),
    _FabricOwner_Type()
)
fabricOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabricOwner.setStatus("current")
_SwitchTable_Object = MibTable
switchTable = _SwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3)
)
if mibBuilder.loadTexts:
    switchTable.setStatus("current")
_SwitchEntry_Object = MibTableRow
switchEntry = _SwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1)
)
switchEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "switchFabricIndex"),
    (0, "NETWORK-APPLIANCE-MIB", "switchIndex"),
)
if mibBuilder.loadTexts:
    switchEntry.setStatus("current")


class _SwitchIndex_Type(Integer32):
    """Custom type switchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SwitchIndex_Type.__name__ = "Integer32"
_SwitchIndex_Object = MibTableColumn
switchIndex = _SwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 1),
    _SwitchIndex_Type()
)
switchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIndex.setStatus("current")


class _SwitchName_Type(OctetString):
    """Custom type switchName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwitchName_Type.__name__ = "OctetString"
_SwitchName_Object = MibTableColumn
switchName = _SwitchName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 2),
    _SwitchName_Type()
)
switchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchName.setStatus("current")


class _SwitchSymbolicName_Type(OctetString):
    """Custom type switchSymbolicName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwitchSymbolicName_Type.__name__ = "OctetString"
_SwitchSymbolicName_Object = MibTableColumn
switchSymbolicName = _SwitchSymbolicName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 3),
    _SwitchSymbolicName_Type()
)
switchSymbolicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchSymbolicName.setStatus("current")


class _SwitchType_Type(Integer32):
    """Custom type switchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hub", 1),
          ("switch", 2),
          ("unknown", 3))
    )


_SwitchType_Type.__name__ = "Integer32"
_SwitchType_Object = MibTableColumn
switchType = _SwitchType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 4),
    _SwitchType_Type()
)
switchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchType.setStatus("current")
_SwitchDomain_Type = Integer32
_SwitchDomain_Object = MibTableColumn
switchDomain = _SwitchDomain_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 5),
    _SwitchDomain_Type()
)
switchDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDomain.setStatus("current")
_SwitchManagementId_Type = Integer32
_SwitchManagementId_Object = MibTableColumn
switchManagementId = _SwitchManagementId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 6),
    _SwitchManagementId_Type()
)
switchManagementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchManagementId.setStatus("current")


class _SwitchStatus_Type(Integer32):
    """Custom type switchStatus based on Integer32"""
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
        *(("critical", 5),
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )


_SwitchStatus_Type.__name__ = "Integer32"
_SwitchStatus_Object = MibTableColumn
switchStatus = _SwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 7),
    _SwitchStatus_Type()
)
switchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchStatus.setStatus("current")
_SwitchStatusMessage_Type = DisplayString
_SwitchStatusMessage_Object = MibTableColumn
switchStatusMessage = _SwitchStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 8),
    _SwitchStatusMessage_Type()
)
switchStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchStatusMessage.setStatus("current")
_SwitchLinkSpeed_Type = Integer32
_SwitchLinkSpeed_Object = MibTableColumn
switchLinkSpeed = _SwitchLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 9),
    _SwitchLinkSpeed_Type()
)
switchLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchLinkSpeed.setStatus("current")
_SwitchHighPacketsProcessed_Type = Counter32
_SwitchHighPacketsProcessed_Object = MibTableColumn
switchHighPacketsProcessed = _SwitchHighPacketsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 10),
    _SwitchHighPacketsProcessed_Type()
)
switchHighPacketsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchHighPacketsProcessed.setStatus("current")
_SwitchLowPacketsProcessed_Type = Counter32
_SwitchLowPacketsProcessed_Object = MibTableColumn
switchLowPacketsProcessed = _SwitchLowPacketsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 11),
    _SwitchLowPacketsProcessed_Type()
)
switchLowPacketsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchLowPacketsProcessed.setStatus("current")
_SwitchHighPacketsRejected_Type = Counter32
_SwitchHighPacketsRejected_Object = MibTableColumn
switchHighPacketsRejected = _SwitchHighPacketsRejected_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 12),
    _SwitchHighPacketsRejected_Type()
)
switchHighPacketsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchHighPacketsRejected.setStatus("current")
_SwitchLowPacketsRejected_Type = Counter32
_SwitchLowPacketsRejected_Object = MibTableColumn
switchLowPacketsRejected = _SwitchLowPacketsRejected_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 13),
    _SwitchLowPacketsRejected_Type()
)
switchLowPacketsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchLowPacketsRejected.setStatus("current")


class _SwitchFabricIndex_Type(Integer32):
    """Custom type switchFabricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SwitchFabricIndex_Type.__name__ = "Integer32"
_SwitchFabricIndex_Object = MibTableColumn
switchFabricIndex = _SwitchFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 14),
    _SwitchFabricIndex_Type()
)
switchFabricIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchFabricIndex.setStatus("current")
_Switch64PacketsProcessed_Type = Counter64
_Switch64PacketsProcessed_Object = MibTableColumn
switch64PacketsProcessed = _Switch64PacketsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 15),
    _Switch64PacketsProcessed_Type()
)
switch64PacketsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch64PacketsProcessed.setStatus("current")
_Switch64PacketsRejected_Type = Counter64
_Switch64PacketsRejected_Object = MibTableColumn
switch64PacketsRejected = _Switch64PacketsRejected_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 3, 1, 16),
    _Switch64PacketsRejected_Type()
)
switch64PacketsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch64PacketsRejected.setStatus("current")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 4)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 4, 1)
)
portEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "portFabricIndex"),
    (0, "NETWORK-APPLIANCE-MIB", "portSwitchIndex"),
    (0, "NETWORK-APPLIANCE-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 4, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortName_Type(OctetString):
    """Custom type portName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PortName_Type.__name__ = "OctetString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 4, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortSwitchIndex_Type(Integer32):
    """Custom type portSwitchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortSwitchIndex_Type.__name__ = "Integer32"
_PortSwitchIndex_Object = MibTableColumn
portSwitchIndex = _PortSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 4, 1, 3),
    _PortSwitchIndex_Type()
)
portSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSwitchIndex.setStatus("current")


class _PortSwitchName_Type(OctetString):
    """Custom type portSwitchName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PortSwitchName_Type.__name__ = "OctetString"
_PortSwitchName_Object = MibTableColumn
portSwitchName = _PortSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 4, 1, 4),
    _PortSwitchName_Type()
)
portSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSwitchName.setStatus("current")
_PortNumber_Type = Integer32
_PortNumber_Object = MibTableColumn
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 4, 1, 5),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumber.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
        *(("bPort", 7),
          ("ePort", 6),
          ("fPort", 4),
          ("flPort", 5),
          ("nPort", 2),
          ("nlPort", 3),
          ("unidentified", 1))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 4, 1, 6),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortState_Type(Integer32):
    """Custom type portState based on Integer32"""
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
        *(("faulty", 4),
          ("offline", 2),
          ("online", 1),
          ("testing", 3),
          ("unknown", 5))
    )


_PortState_Type.__name__ = "Integer32"
_PortState_Object = MibTableColumn
portState = _PortState_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 4, 1, 7),
    _PortState_Type()
)
portState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portState.setStatus("current")


class _PortFabricIndex_Type(Integer32):
    """Custom type portFabricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortFabricIndex_Type.__name__ = "Integer32"
_PortFabricIndex_Object = MibTableColumn
portFabricIndex = _PortFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 11, 4, 1, 8),
    _PortFabricIndex_Type()
)
portFabricIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFabricIndex.setStatus("current")
_Dafs_ObjectIdentity = ObjectIdentity
dafs = _Dafs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 12)
)
_DafsOptions_ObjectIdentity = ObjectIdentity
dafsOptions = _DafsOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1)
)


class _DafsIsLicensed_Type(Integer32):
    """Custom type dafsIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DafsIsLicensed_Type.__name__ = "Integer32"
_DafsIsLicensed_Object = MibScalar
dafsIsLicensed = _DafsIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 1),
    _DafsIsLicensed_Type()
)
dafsIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsIsLicensed.setStatus("obsolete")
_DafsMaxRequestsServer_Type = Integer32
_DafsMaxRequestsServer_Object = MibScalar
dafsMaxRequestsServer = _DafsMaxRequestsServer_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 2),
    _DafsMaxRequestsServer_Type()
)
dafsMaxRequestsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsMaxRequestsServer.setStatus("obsolete")
_DafsMaxRequests_Type = Integer32
_DafsMaxRequests_Object = MibScalar
dafsMaxRequests = _DafsMaxRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 3),
    _DafsMaxRequests_Type()
)
dafsMaxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsMaxRequests.setStatus("obsolete")
_DafsMaxRequestSize_Type = Integer32
_DafsMaxRequestSize_Object = MibScalar
dafsMaxRequestSize = _DafsMaxRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 4),
    _DafsMaxRequestSize_Type()
)
dafsMaxRequestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsMaxRequestSize.setStatus("current")
_DafsMaxResponseSize_Type = Integer32
_DafsMaxResponseSize_Object = MibScalar
dafsMaxResponseSize = _DafsMaxResponseSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 5),
    _DafsMaxResponseSize_Type()
)
dafsMaxResponseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsMaxResponseSize.setStatus("current")
_DafsMaxPendingRequestsServer_Type = Integer32
_DafsMaxPendingRequestsServer_Object = MibScalar
dafsMaxPendingRequestsServer = _DafsMaxPendingRequestsServer_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 6),
    _DafsMaxPendingRequestsServer_Type()
)
dafsMaxPendingRequestsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsMaxPendingRequestsServer.setStatus("obsolete")


class _DafsUseChecksums_Type(Integer32):
    """Custom type dafsUseChecksums based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DafsUseChecksums_Type.__name__ = "Integer32"
_DafsUseChecksums_Object = MibScalar
dafsUseChecksums = _DafsUseChecksums_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 7),
    _DafsUseChecksums_Type()
)
dafsUseChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsUseChecksums.setStatus("current")
_DafsNicNumRequestDemons_Type = Integer32
_DafsNicNumRequestDemons_Object = MibScalar
dafsNicNumRequestDemons = _DafsNicNumRequestDemons_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 8),
    _DafsNicNumRequestDemons_Type()
)
dafsNicNumRequestDemons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNicNumRequestDemons.setStatus("obsolete")


class _DafsAnonymousAuthentication_Type(Integer32):
    """Custom type dafsAnonymousAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DafsAnonymousAuthentication_Type.__name__ = "Integer32"
_DafsAnonymousAuthentication_Object = MibScalar
dafsAnonymousAuthentication = _DafsAnonymousAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 9),
    _DafsAnonymousAuthentication_Type()
)
dafsAnonymousAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsAnonymousAuthentication.setStatus("current")


class _DafsServerEnabled_Type(Integer32):
    """Custom type dafsServerEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DafsServerEnabled_Type.__name__ = "Integer32"
_DafsServerEnabled_Object = MibScalar
dafsServerEnabled = _DafsServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 10),
    _DafsServerEnabled_Type()
)
dafsServerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsServerEnabled.setStatus("current")
_DafsDefaultUid_Type = Integer32
_DafsDefaultUid_Object = MibScalar
dafsDefaultUid = _DafsDefaultUid_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 11),
    _DafsDefaultUid_Type()
)
dafsDefaultUid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsDefaultUid.setStatus("current")
_DafsDefaultGid_Type = Integer32
_DafsDefaultGid_Object = MibScalar
dafsDefaultGid = _DafsDefaultGid_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 12),
    _DafsDefaultGid_Type()
)
dafsDefaultGid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsDefaultGid.setStatus("current")
_DafsMaxDisconnectedSessions_Type = Integer32
_DafsMaxDisconnectedSessions_Object = MibScalar
dafsMaxDisconnectedSessions = _DafsMaxDisconnectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 13),
    _DafsMaxDisconnectedSessions_Type()
)
dafsMaxDisconnectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsMaxDisconnectedSessions.setStatus("current")
_DafsMaxIdleSeconds_Type = Integer32
_DafsMaxIdleSeconds_Object = MibScalar
dafsMaxIdleSeconds = _DafsMaxIdleSeconds_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 1, 14),
    _DafsMaxIdleSeconds_Type()
)
dafsMaxIdleSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsMaxIdleSeconds.setStatus("current")
_DafsNicTable_Object = MibTable
dafsNicTable = _DafsNicTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 2)
)
if mibBuilder.loadTexts:
    dafsNicTable.setStatus("current")
_DafsNicEntry_Object = MibTableRow
dafsNicEntry = _DafsNicEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 2, 1)
)
dafsNicEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "dafsNicIndex"),
)
if mibBuilder.loadTexts:
    dafsNicEntry.setStatus("current")


class _DafsNicIndex_Type(Integer32):
    """Custom type dafsNicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DafsNicIndex_Type.__name__ = "Integer32"
_DafsNicIndex_Object = MibTableColumn
dafsNicIndex = _DafsNicIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 2, 1, 1),
    _DafsNicIndex_Type()
)
dafsNicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNicIndex.setStatus("current")


class _DafsNicName_Type(DisplayString):
    """Custom type dafsNicName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DafsNicName_Type.__name__ = "DisplayString"
_DafsNicName_Object = MibTableColumn
dafsNicName = _DafsNicName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 2, 1, 2),
    _DafsNicName_Type()
)
dafsNicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNicName.setStatus("current")


class _DafsNicDevice_Type(DisplayString):
    """Custom type dafsNicDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DafsNicDevice_Type.__name__ = "DisplayString"
_DafsNicDevice_Object = MibTableColumn
dafsNicDevice = _DafsNicDevice_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 2, 1, 3),
    _DafsNicDevice_Type()
)
dafsNicDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNicDevice.setStatus("current")


class _DafsNicState_Type(Integer32):
    """Custom type dafsNicState based on Integer32"""
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


_DafsNicState_Type.__name__ = "Integer32"
_DafsNicState_Object = MibTableColumn
dafsNicState = _DafsNicState_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 2, 1, 4),
    _DafsNicState_Type()
)
dafsNicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNicState.setStatus("current")
_DafsNicListenAddr_Type = OctetString
_DafsNicListenAddr_Object = MibTableColumn
dafsNicListenAddr = _DafsNicListenAddr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 2, 1, 5),
    _DafsNicListenAddr_Type()
)
dafsNicListenAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNicListenAddr.setStatus("current")
_DafsNicNumRqstDemons_Type = Integer32
_DafsNicNumRqstDemons_Object = MibTableColumn
dafsNicNumRqstDemons = _DafsNicNumRqstDemons_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 2, 1, 6),
    _DafsNicNumRqstDemons_Type()
)
dafsNicNumRqstDemons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNicNumRqstDemons.setStatus("obsolete")
_DafsNicInBytes_Type = Counter32
_DafsNicInBytes_Object = MibTableColumn
dafsNicInBytes = _DafsNicInBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 2, 1, 7),
    _DafsNicInBytes_Type()
)
dafsNicInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNicInBytes.setStatus("current")
_DafsNicDirectInBytes_Type = Counter32
_DafsNicDirectInBytes_Object = MibTableColumn
dafsNicDirectInBytes = _DafsNicDirectInBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 2, 1, 8),
    _DafsNicDirectInBytes_Type()
)
dafsNicDirectInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNicDirectInBytes.setStatus("current")
_DafsNicOutBytes_Type = Counter32
_DafsNicOutBytes_Object = MibTableColumn
dafsNicOutBytes = _DafsNicOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 2, 1, 9),
    _DafsNicOutBytes_Type()
)
dafsNicOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNicOutBytes.setStatus("current")
_DafsNicDirectOutBytes_Type = Counter32
_DafsNicDirectOutBytes_Object = MibTableColumn
dafsNicDirectOutBytes = _DafsNicDirectOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 2, 1, 10),
    _DafsNicDirectOutBytes_Type()
)
dafsNicDirectOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNicDirectOutBytes.setStatus("current")
_CurDafs_ObjectIdentity = ObjectIdentity
curDafs = _CurDafs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 3)
)
_DafsPendingRequests_Type = Integer32
_DafsPendingRequests_Object = MibScalar
dafsPendingRequests = _DafsPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 3, 1),
    _DafsPendingRequests_Type()
)
dafsPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsPendingRequests.setStatus("obsolete")
_DafsCurrentRequests_Type = Integer32
_DafsCurrentRequests_Object = MibScalar
dafsCurrentRequests = _DafsCurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 3, 2),
    _DafsCurrentRequests_Type()
)
dafsCurrentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsCurrentRequests.setStatus("obsolete")
_TotDafs_ObjectIdentity = ObjectIdentity
totDafs = _TotDafs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4)
)
_DafsCalls_Type = Counter32
_DafsCalls_Object = MibScalar
dafsCalls = _DafsCalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 1),
    _DafsCalls_Type()
)
dafsCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsCalls.setStatus("current")
_DafsClientAuths_Type = Counter32
_DafsClientAuths_Object = MibScalar
dafsClientAuths = _DafsClientAuths_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 2),
    _DafsClientAuths_Type()
)
dafsClientAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsClientAuths.setStatus("current")
_DafsClientConnects_Type = Counter32
_DafsClientConnects_Object = MibScalar
dafsClientConnects = _DafsClientConnects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 3),
    _DafsClientConnects_Type()
)
dafsClientConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsClientConnects.setStatus("current")
_DafsClientConnectAuths_Type = Counter32
_DafsClientConnectAuths_Object = MibScalar
dafsClientConnectAuths = _DafsClientConnectAuths_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 4),
    _DafsClientConnectAuths_Type()
)
dafsClientConnectAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsClientConnectAuths.setStatus("current")
_DafsConnectBinds_Type = Counter32
_DafsConnectBinds_Object = MibScalar
dafsConnectBinds = _DafsConnectBinds_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 5),
    _DafsConnectBinds_Type()
)
dafsConnectBinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsConnectBinds.setStatus("current")
_DafsDisconnects_Type = Counter32
_DafsDisconnects_Object = MibScalar
dafsDisconnects = _DafsDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 6),
    _DafsDisconnects_Type()
)
dafsDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsDisconnects.setStatus("current")
_DafsRegisterCreds_Type = Counter32
_DafsRegisterCreds_Object = MibScalar
dafsRegisterCreds = _DafsRegisterCreds_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 7),
    _DafsRegisterCreds_Type()
)
dafsRegisterCreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsRegisterCreds.setStatus("current")
_DafsReleaseCreds_Type = Counter32
_DafsReleaseCreds_Object = MibScalar
dafsReleaseCreds = _DafsReleaseCreds_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 8),
    _DafsReleaseCreds_Type()
)
dafsReleaseCreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsReleaseCreds.setStatus("current")
_DafsSecinfos_Type = Counter32
_DafsSecinfos_Object = MibScalar
dafsSecinfos = _DafsSecinfos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 9),
    _DafsSecinfos_Type()
)
dafsSecinfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSecinfos.setStatus("current")
_DafsServerAuths_Type = Counter32
_DafsServerAuths_Object = MibScalar
dafsServerAuths = _DafsServerAuths_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 10),
    _DafsServerAuths_Type()
)
dafsServerAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsServerAuths.setStatus("current")
_DafsCheckResponses_Type = Counter32
_DafsCheckResponses_Object = MibScalar
dafsCheckResponses = _DafsCheckResponses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 11),
    _DafsCheckResponses_Type()
)
dafsCheckResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsCheckResponses.setStatus("current")
_DafsFetchResponses_Type = Counter32
_DafsFetchResponses_Object = MibScalar
dafsFetchResponses = _DafsFetchResponses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 12),
    _DafsFetchResponses_Type()
)
dafsFetchResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsFetchResponses.setStatus("current")
_DafsDiscardResponses_Type = Counter32
_DafsDiscardResponses_Object = MibScalar
dafsDiscardResponses = _DafsDiscardResponses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 13),
    _DafsDiscardResponses_Type()
)
dafsDiscardResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsDiscardResponses.setStatus("current")
_DafsAccesses_Type = Counter32
_DafsAccesses_Object = MibScalar
dafsAccesses = _DafsAccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 14),
    _DafsAccesses_Type()
)
dafsAccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsAccesses.setStatus("current")
_DafsCacheHints_Type = Counter32
_DafsCacheHints_Object = MibScalar
dafsCacheHints = _DafsCacheHints_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 15),
    _DafsCacheHints_Type()
)
dafsCacheHints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsCacheHints.setStatus("current")
_DafsCloses_Type = Counter32
_DafsCloses_Object = MibScalar
dafsCloses = _DafsCloses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 16),
    _DafsCloses_Type()
)
dafsCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsCloses.setStatus("current")
_DafsCommits_Type = Counter32
_DafsCommits_Object = MibScalar
dafsCommits = _DafsCommits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 17),
    _DafsCommits_Type()
)
dafsCommits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsCommits.setStatus("current")
_DafsCreates_Type = Counter32
_DafsCreates_Object = MibScalar
dafsCreates = _DafsCreates_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 18),
    _DafsCreates_Type()
)
dafsCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsCreates.setStatus("current")
_DafsDelegPurges_Type = Counter32
_DafsDelegPurges_Object = MibScalar
dafsDelegPurges = _DafsDelegPurges_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 19),
    _DafsDelegPurges_Type()
)
dafsDelegPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsDelegPurges.setStatus("current")
_DafsDelegReturns_Type = Counter32
_DafsDelegReturns_Object = MibScalar
dafsDelegReturns = _DafsDelegReturns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 20),
    _DafsDelegReturns_Type()
)
dafsDelegReturns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsDelegReturns.setStatus("current")
_DafsGetFsattrs_Type = Counter32
_DafsGetFsattrs_Object = MibScalar
dafsGetFsattrs = _DafsGetFsattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 21),
    _DafsGetFsattrs_Type()
)
dafsGetFsattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsGetFsattrs.setStatus("current")
_DafsGetRootHandles_Type = Counter32
_DafsGetRootHandles_Object = MibScalar
dafsGetRootHandles = _DafsGetRootHandles_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 22),
    _DafsGetRootHandles_Type()
)
dafsGetRootHandles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsGetRootHandles.setStatus("current")
_DafsGetattrInlines_Type = Counter32
_DafsGetattrInlines_Object = MibScalar
dafsGetattrInlines = _DafsGetattrInlines_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 23),
    _DafsGetattrInlines_Type()
)
dafsGetattrInlines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsGetattrInlines.setStatus("current")
_DafsGetattrDirects_Type = Counter32
_DafsGetattrDirects_Object = MibScalar
dafsGetattrDirects = _DafsGetattrDirects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 24),
    _DafsGetattrDirects_Type()
)
dafsGetattrDirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsGetattrDirects.setStatus("current")
_DafsLinks_Type = Counter32
_DafsLinks_Object = MibScalar
dafsLinks = _DafsLinks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 25),
    _DafsLinks_Type()
)
dafsLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsLinks.setStatus("current")
_DafsLocks_Type = Counter32
_DafsLocks_Object = MibScalar
dafsLocks = _DafsLocks_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 26),
    _DafsLocks_Type()
)
dafsLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsLocks.setStatus("current")
_DafsLockts_Type = Counter32
_DafsLockts_Object = MibScalar
dafsLockts = _DafsLockts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 27),
    _DafsLockts_Type()
)
dafsLockts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsLockts.setStatus("current")
_DafsLockus_Type = Counter32
_DafsLockus_Object = MibScalar
dafsLockus = _DafsLockus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 28),
    _DafsLockus_Type()
)
dafsLockus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsLockus.setStatus("current")
_DafsLookUps_Type = Counter32
_DafsLookUps_Object = MibScalar
dafsLookUps = _DafsLookUps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 29),
    _DafsLookUps_Type()
)
dafsLookUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsLookUps.setStatus("current")
_DafsLookUpps_Type = Counter32
_DafsLookUpps_Object = MibScalar
dafsLookUpps = _DafsLookUpps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 30),
    _DafsLookUpps_Type()
)
dafsLookUpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsLookUpps.setStatus("current")
_DafsNulls_Type = Counter32
_DafsNulls_Object = MibScalar
dafsNulls = _DafsNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 31),
    _DafsNulls_Type()
)
dafsNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNulls.setStatus("current")
_DafsNverifys_Type = Counter32
_DafsNverifys_Object = MibScalar
dafsNverifys = _DafsNverifys_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 32),
    _DafsNverifys_Type()
)
dafsNverifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsNverifys.setStatus("current")
_DafsOpens_Type = Counter32
_DafsOpens_Object = MibScalar
dafsOpens = _DafsOpens_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 33),
    _DafsOpens_Type()
)
dafsOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsOpens.setStatus("current")
_DafsOpenDowngrades_Type = Counter32
_DafsOpenDowngrades_Object = MibScalar
dafsOpenDowngrades = _DafsOpenDowngrades_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 34),
    _DafsOpenDowngrades_Type()
)
dafsOpenDowngrades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsOpenDowngrades.setStatus("current")
_DafsOpenattrs_Type = Counter32
_DafsOpenattrs_Object = MibScalar
dafsOpenattrs = _DafsOpenattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 35),
    _DafsOpenattrs_Type()
)
dafsOpenattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsOpenattrs.setStatus("current")
_DafsReadInlines_Type = Counter32
_DafsReadInlines_Object = MibScalar
dafsReadInlines = _DafsReadInlines_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 36),
    _DafsReadInlines_Type()
)
dafsReadInlines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsReadInlines.setStatus("current")
_DafsReadDirects_Type = Counter32
_DafsReadDirects_Object = MibScalar
dafsReadDirects = _DafsReadDirects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 37),
    _DafsReadDirects_Type()
)
dafsReadDirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsReadDirects.setStatus("current")
_DafsReaddirInlines_Type = Counter32
_DafsReaddirInlines_Object = MibScalar
dafsReaddirInlines = _DafsReaddirInlines_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 38),
    _DafsReaddirInlines_Type()
)
dafsReaddirInlines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsReaddirInlines.setStatus("current")
_DafsReaddirDirects_Type = Counter32
_DafsReaddirDirects_Object = MibScalar
dafsReaddirDirects = _DafsReaddirDirects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 39),
    _DafsReaddirDirects_Type()
)
dafsReaddirDirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsReaddirDirects.setStatus("current")
_DafsReadlinkInlines_Type = Counter32
_DafsReadlinkInlines_Object = MibScalar
dafsReadlinkInlines = _DafsReadlinkInlines_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 40),
    _DafsReadlinkInlines_Type()
)
dafsReadlinkInlines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsReadlinkInlines.setStatus("current")
_DafsReadlinkDirects_Type = Counter32
_DafsReadlinkDirects_Object = MibScalar
dafsReadlinkDirects = _DafsReadlinkDirects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 41),
    _DafsReadlinkDirects_Type()
)
dafsReadlinkDirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsReadlinkDirects.setStatus("current")
_DafsRemoves_Type = Counter32
_DafsRemoves_Object = MibScalar
dafsRemoves = _DafsRemoves_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 42),
    _DafsRemoves_Type()
)
dafsRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsRemoves.setStatus("current")
_DafsRenames_Type = Counter32
_DafsRenames_Object = MibScalar
dafsRenames = _DafsRenames_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 43),
    _DafsRenames_Type()
)
dafsRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsRenames.setStatus("current")
_DafsSetattrInlines_Type = Counter32
_DafsSetattrInlines_Object = MibScalar
dafsSetattrInlines = _DafsSetattrInlines_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 44),
    _DafsSetattrInlines_Type()
)
dafsSetattrInlines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSetattrInlines.setStatus("current")
_DafsSetattrDirects_Type = Counter32
_DafsSetattrDirects_Object = MibScalar
dafsSetattrDirects = _DafsSetattrDirects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 45),
    _DafsSetattrDirects_Type()
)
dafsSetattrDirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSetattrDirects.setStatus("current")
_DafsVerifys_Type = Counter32
_DafsVerifys_Object = MibScalar
dafsVerifys = _DafsVerifys_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 46),
    _DafsVerifys_Type()
)
dafsVerifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsVerifys.setStatus("current")
_DafsBatchSubmits_Type = Counter32
_DafsBatchSubmits_Object = MibScalar
dafsBatchSubmits = _DafsBatchSubmits_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 47),
    _DafsBatchSubmits_Type()
)
dafsBatchSubmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsBatchSubmits.setStatus("current")
_DafsWriteInlines_Type = Counter32
_DafsWriteInlines_Object = MibScalar
dafsWriteInlines = _DafsWriteInlines_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 48),
    _DafsWriteInlines_Type()
)
dafsWriteInlines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsWriteInlines.setStatus("current")
_DafsWriteDirects_Type = Counter32
_DafsWriteDirects_Object = MibScalar
dafsWriteDirects = _DafsWriteDirects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 49),
    _DafsWriteDirects_Type()
)
dafsWriteDirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsWriteDirects.setStatus("current")
_DafsBcGetattrs_Type = Counter32
_DafsBcGetattrs_Object = MibScalar
dafsBcGetattrs = _DafsBcGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 50),
    _DafsBcGetattrs_Type()
)
dafsBcGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsBcGetattrs.setStatus("current")
_DafsBcNulls_Type = Counter32
_DafsBcNulls_Object = MibScalar
dafsBcNulls = _DafsBcNulls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 51),
    _DafsBcNulls_Type()
)
dafsBcNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsBcNulls.setStatus("current")
_DafsBcRecalls_Type = Counter32
_DafsBcRecalls_Object = MibScalar
dafsBcRecalls = _DafsBcRecalls_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 52),
    _DafsBcRecalls_Type()
)
dafsBcRecalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsBcRecalls.setStatus("current")
_DafsBcBatchCompletions_Type = Counter32
_DafsBcBatchCompletions_Object = MibScalar
dafsBcBatchCompletions = _DafsBcBatchCompletions_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 53),
    _DafsBcBatchCompletions_Type()
)
dafsBcBatchCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsBcBatchCompletions.setStatus("current")
_DafsAppendInlines_Type = Counter32
_DafsAppendInlines_Object = MibScalar
dafsAppendInlines = _DafsAppendInlines_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 54),
    _DafsAppendInlines_Type()
)
dafsAppendInlines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsAppendInlines.setStatus("current")
_DafsAppendDirects_Type = Counter32
_DafsAppendDirects_Object = MibScalar
dafsAppendDirects = _DafsAppendDirects_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 55),
    _DafsAppendDirects_Type()
)
dafsAppendDirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsAppendDirects.setStatus("current")
_DafsGetFencingLists_Type = Counter32
_DafsGetFencingLists_Object = MibScalar
dafsGetFencingLists = _DafsGetFencingLists_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 56),
    _DafsGetFencingLists_Type()
)
dafsGetFencingLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsGetFencingLists.setStatus("current")
_DafsSetFencingLists_Type = Counter32
_DafsSetFencingLists_Object = MibScalar
dafsSetFencingLists = _DafsSetFencingLists_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 57),
    _DafsSetFencingLists_Type()
)
dafsSetFencingLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSetFencingLists.setStatus("current")
_DafsHurryUps_Type = Counter32
_DafsHurryUps_Object = MibScalar
dafsHurryUps = _DafsHurryUps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 58),
    _DafsHurryUps_Type()
)
dafsHurryUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsHurryUps.setStatus("current")
_DafsInBytes_Type = Counter32
_DafsInBytes_Object = MibScalar
dafsInBytes = _DafsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 59),
    _DafsInBytes_Type()
)
dafsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsInBytes.setStatus("current")
_DafsDirectInBytes_Type = Counter32
_DafsDirectInBytes_Object = MibScalar
dafsDirectInBytes = _DafsDirectInBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 60),
    _DafsDirectInBytes_Type()
)
dafsDirectInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsDirectInBytes.setStatus("current")
_DafsOutBytes_Type = Counter32
_DafsOutBytes_Object = MibScalar
dafsOutBytes = _DafsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 61),
    _DafsOutBytes_Type()
)
dafsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsOutBytes.setStatus("current")
_DafsDirectOutBytes_Type = Counter32
_DafsDirectOutBytes_Object = MibScalar
dafsDirectOutBytes = _DafsDirectOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 4, 62),
    _DafsDirectOutBytes_Type()
)
dafsDirectOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsDirectOutBytes.setStatus("current")
_DafsSessionTable_Object = MibTable
dafsSessionTable = _DafsSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5)
)
if mibBuilder.loadTexts:
    dafsSessionTable.setStatus("current")
_DafsSessionEntry_Object = MibTableRow
dafsSessionEntry = _DafsSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1)
)
dafsSessionEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "dafsSessionIndex"),
)
if mibBuilder.loadTexts:
    dafsSessionEntry.setStatus("current")


class _DafsSessionIndex_Type(Integer32):
    """Custom type dafsSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DafsSessionIndex_Type.__name__ = "Integer32"
_DafsSessionIndex_Object = MibTableColumn
dafsSessionIndex = _DafsSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 1),
    _DafsSessionIndex_Type()
)
dafsSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionIndex.setStatus("current")
_DafsSessionId_Type = OctetString
_DafsSessionId_Object = MibTableColumn
dafsSessionId = _DafsSessionId_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 2),
    _DafsSessionId_Type()
)
dafsSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionId.setStatus("current")


class _DafsSessionEndian_Type(Integer32):
    """Custom type dafsSessionEndian based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bigEndian", 1),
          ("littleEndian", 2))
    )


_DafsSessionEndian_Type.__name__ = "Integer32"
_DafsSessionEndian_Object = MibTableColumn
dafsSessionEndian = _DafsSessionEndian_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 3),
    _DafsSessionEndian_Type()
)
dafsSessionEndian.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionEndian.setStatus("current")


class _DafsSessionAllowBackChannel_Type(Integer32):
    """Custom type dafsSessionAllowBackChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DafsSessionAllowBackChannel_Type.__name__ = "Integer32"
_DafsSessionAllowBackChannel_Object = MibTableColumn
dafsSessionAllowBackChannel = _DafsSessionAllowBackChannel_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 4),
    _DafsSessionAllowBackChannel_Type()
)
dafsSessionAllowBackChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionAllowBackChannel.setStatus("current")


class _DafsSessionAllowRdmaReadChannel_Type(Integer32):
    """Custom type dafsSessionAllowRdmaReadChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DafsSessionAllowRdmaReadChannel_Type.__name__ = "Integer32"
_DafsSessionAllowRdmaReadChannel_Object = MibTableColumn
dafsSessionAllowRdmaReadChannel = _DafsSessionAllowRdmaReadChannel_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 5),
    _DafsSessionAllowRdmaReadChannel_Type()
)
dafsSessionAllowRdmaReadChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionAllowRdmaReadChannel.setStatus("current")


class _DafsSessionUseChecksums_Type(Integer32):
    """Custom type dafsSessionUseChecksums based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DafsSessionUseChecksums_Type.__name__ = "Integer32"
_DafsSessionUseChecksums_Object = MibTableColumn
dafsSessionUseChecksums = _DafsSessionUseChecksums_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 6),
    _DafsSessionUseChecksums_Type()
)
dafsSessionUseChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionUseChecksums.setStatus("current")
_DafsSessionMaxCredentials_Type = Integer32
_DafsSessionMaxCredentials_Object = MibTableColumn
dafsSessionMaxCredentials = _DafsSessionMaxCredentials_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 7),
    _DafsSessionMaxCredentials_Type()
)
dafsSessionMaxCredentials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionMaxCredentials.setStatus("current")
_DafsSessionMaxRequestSize_Type = Integer32
_DafsSessionMaxRequestSize_Object = MibTableColumn
dafsSessionMaxRequestSize = _DafsSessionMaxRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 8),
    _DafsSessionMaxRequestSize_Type()
)
dafsSessionMaxRequestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionMaxRequestSize.setStatus("current")
_DafsSessionMaxResponseSize_Type = Integer32
_DafsSessionMaxResponseSize_Object = MibTableColumn
dafsSessionMaxResponseSize = _DafsSessionMaxResponseSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 9),
    _DafsSessionMaxResponseSize_Type()
)
dafsSessionMaxResponseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionMaxResponseSize.setStatus("current")
_DafsSessionMaxRequests_Type = Integer32
_DafsSessionMaxRequests_Object = MibTableColumn
dafsSessionMaxRequests = _DafsSessionMaxRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 10),
    _DafsSessionMaxRequests_Type()
)
dafsSessionMaxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionMaxRequests.setStatus("current")
_DafsSessionInlineWriteHeaderSize_Type = Integer32
_DafsSessionInlineWriteHeaderSize_Object = MibTableColumn
dafsSessionInlineWriteHeaderSize = _DafsSessionInlineWriteHeaderSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 11),
    _DafsSessionInlineWriteHeaderSize_Type()
)
dafsSessionInlineWriteHeaderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionInlineWriteHeaderSize.setStatus("current")


class _DafsSessionClientIdString_Type(OctetString):
    """Custom type dafsSessionClientIdString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_DafsSessionClientIdString_Type.__name__ = "OctetString"
_DafsSessionClientIdString_Object = MibTableColumn
dafsSessionClientIdString = _DafsSessionClientIdString_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 12),
    _DafsSessionClientIdString_Type()
)
dafsSessionClientIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionClientIdString.setStatus("current")


class _DafsSessionClientVerifier_Type(OctetString):
    """Custom type dafsSessionClientVerifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_DafsSessionClientVerifier_Type.__name__ = "OctetString"
_DafsSessionClientVerifier_Object = MibTableColumn
dafsSessionClientVerifier = _DafsSessionClientVerifier_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 13),
    _DafsSessionClientVerifier_Type()
)
dafsSessionClientVerifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionClientVerifier.setStatus("current")
_DafsSessionNumCredentials_Type = Integer32
_DafsSessionNumCredentials_Object = MibTableColumn
dafsSessionNumCredentials = _DafsSessionNumCredentials_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 14),
    _DafsSessionNumCredentials_Type()
)
dafsSessionNumCredentials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionNumCredentials.setStatus("current")
_DafsSessionNumRequests_Type = Integer32
_DafsSessionNumRequests_Object = MibTableColumn
dafsSessionNumRequests = _DafsSessionNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 5, 1, 15),
    _DafsSessionNumRequests_Type()
)
dafsSessionNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsSessionNumRequests.setStatus("current")
_DafsExportTable_Object = MibTable
dafsExportTable = _DafsExportTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 6)
)
if mibBuilder.loadTexts:
    dafsExportTable.setStatus("current")
_DafsExportEntry_Object = MibTableRow
dafsExportEntry = _DafsExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 6, 1)
)
dafsExportEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "dafsExportIndex"),
)
if mibBuilder.loadTexts:
    dafsExportEntry.setStatus("current")


class _DafsExportIndex_Type(Integer32):
    """Custom type dafsExportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DafsExportIndex_Type.__name__ = "Integer32"
_DafsExportIndex_Object = MibTableColumn
dafsExportIndex = _DafsExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 6, 1, 1),
    _DafsExportIndex_Type()
)
dafsExportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsExportIndex.setStatus("current")


class _DafsExportName_Type(DisplayString):
    """Custom type dafsExportName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DafsExportName_Type.__name__ = "DisplayString"
_DafsExportName_Object = MibTableColumn
dafsExportName = _DafsExportName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 6, 1, 2),
    _DafsExportName_Type()
)
dafsExportName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsExportName.setStatus("current")


class _DafsExportPath_Type(DisplayString):
    """Custom type dafsExportPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DafsExportPath_Type.__name__ = "DisplayString"
_DafsExportPath_Object = MibTableColumn
dafsExportPath = _DafsExportPath_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 6, 1, 3),
    _DafsExportPath_Type()
)
dafsExportPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsExportPath.setStatus("current")


class _DafsExportEnabled_Type(Integer32):
    """Custom type dafsExportEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DafsExportEnabled_Type.__name__ = "Integer32"
_DafsExportEnabled_Object = MibTableColumn
dafsExportEnabled = _DafsExportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 6, 1, 4),
    _DafsExportEnabled_Type()
)
dafsExportEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsExportEnabled.setStatus("current")


class _DafsExportRwMode_Type(Integer32):
    """Custom type dafsExportRwMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readmostly", 2),
          ("readonly", 3),
          ("readwrite", 1))
    )


_DafsExportRwMode_Type.__name__ = "Integer32"
_DafsExportRwMode_Object = MibTableColumn
dafsExportRwMode = _DafsExportRwMode_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 6, 1, 5),
    _DafsExportRwMode_Type()
)
dafsExportRwMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsExportRwMode.setStatus("current")


class _DafsExportAccessList_Type(DisplayString):
    """Custom type dafsExportAccessList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DafsExportAccessList_Type.__name__ = "DisplayString"
_DafsExportAccessList_Object = MibTableColumn
dafsExportAccessList = _DafsExportAccessList_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 12, 6, 1, 6),
    _DafsExportAccessList_Type()
)
dafsExportAccessList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dafsExportAccessList.setStatus("current")
_Vi_ObjectIdentity = ObjectIdentity
vi = _Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 13)
)
_ViaNodeConnection_ObjectIdentity = ObjectIdentity
viaNodeConnection = _ViaNodeConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1)
)


class _ViaNodeSystemName_Type(DisplayString):
    """Custom type viaNodeSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ViaNodeSystemName_Type.__name__ = "DisplayString"
_ViaNodeSystemName_Object = MibScalar
viaNodeSystemName = _ViaNodeSystemName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 1),
    _ViaNodeSystemName_Type()
)
viaNodeSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaNodeSystemName.setStatus("current")
_ViaCreated_Type = Integer32
_ViaCreated_Object = MibScalar
viaCreated = _ViaCreated_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 2),
    _ViaCreated_Type()
)
viaCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaCreated.setStatus("current")
_ViaConnectRequest_Type = Counter32
_ViaConnectRequest_Object = MibScalar
viaConnectRequest = _ViaConnectRequest_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 3),
    _ViaConnectRequest_Type()
)
viaConnectRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnectRequest.setStatus("current")
_ViaConnectWait_Type = Counter32
_ViaConnectWait_Object = MibScalar
viaConnectWait = _ViaConnectWait_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 4),
    _ViaConnectWait_Type()
)
viaConnectWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnectWait.setStatus("current")
_ViaDisconnect_Type = Counter32
_ViaDisconnect_Object = MibScalar
viaDisconnect = _ViaDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 5),
    _ViaDisconnect_Type()
)
viaDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaDisconnect.setStatus("current")
_ViaConnectTimeOut_Type = Counter32
_ViaConnectTimeOut_Object = MibScalar
viaConnectTimeOut = _ViaConnectTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 6),
    _ViaConnectTimeOut_Type()
)
viaConnectTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnectTimeOut.setStatus("current")
_ViaConnected_Type = Counter32
_ViaConnected_Object = MibScalar
viaConnected = _ViaConnected_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 7),
    _ViaConnected_Type()
)
viaConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnected.setStatus("current")
_ViaCurrConnectPending_Type = Gauge32
_ViaCurrConnectPending_Object = MibScalar
viaCurrConnectPending = _ViaCurrConnectPending_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 8),
    _ViaCurrConnectPending_Type()
)
viaCurrConnectPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaCurrConnectPending.setStatus("current")
_ViaCurrConnectWaitPending_Type = Gauge32
_ViaCurrConnectWaitPending_Object = MibScalar
viaCurrConnectWaitPending = _ViaCurrConnectWaitPending_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 9),
    _ViaCurrConnectWaitPending_Type()
)
viaCurrConnectWaitPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaCurrConnectWaitPending.setStatus("current")
_ViaCurrConnected_Type = Gauge32
_ViaCurrConnected_Object = MibScalar
viaCurrConnected = _ViaCurrConnected_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 10),
    _ViaCurrConnected_Type()
)
viaCurrConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaCurrConnected.setStatus("current")
_ViaCurrError_Type = Gauge32
_ViaCurrError_Object = MibScalar
viaCurrError = _ViaCurrError_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 11),
    _ViaCurrError_Type()
)
viaCurrError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaCurrError.setStatus("current")
_ViaTotalError_Type = Counter32
_ViaTotalError_Object = MibScalar
viaTotalError = _ViaTotalError_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 12),
    _ViaTotalError_Type()
)
viaTotalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaTotalError.setStatus("current")
_ViaInMsgs_Type = Counter32
_ViaInMsgs_Object = MibScalar
viaInMsgs = _ViaInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 13),
    _ViaInMsgs_Type()
)
viaInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaInMsgs.setStatus("current")
_ViaInRdma_Type = Counter32
_ViaInRdma_Object = MibScalar
viaInRdma = _ViaInRdma_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 14),
    _ViaInRdma_Type()
)
viaInRdma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaInRdma.setStatus("current")
_ViaInBytes_Type = Counter32
_ViaInBytes_Object = MibScalar
viaInBytes = _ViaInBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 15),
    _ViaInBytes_Type()
)
viaInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaInBytes.setStatus("current")
_ViaInRDMAReadBytes_Type = Counter32
_ViaInRDMAReadBytes_Object = MibScalar
viaInRDMAReadBytes = _ViaInRDMAReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 16),
    _ViaInRDMAReadBytes_Type()
)
viaInRDMAReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaInRDMAReadBytes.setStatus("current")
_ViaInRDMAWriteBytes_Type = Counter32
_ViaInRDMAWriteBytes_Object = MibScalar
viaInRDMAWriteBytes = _ViaInRDMAWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 17),
    _ViaInRDMAWriteBytes_Type()
)
viaInRDMAWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaInRDMAWriteBytes.setStatus("current")
_ViaOutMsgs_Type = Counter32
_ViaOutMsgs_Object = MibScalar
viaOutMsgs = _ViaOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 18),
    _ViaOutMsgs_Type()
)
viaOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaOutMsgs.setStatus("current")
_ViaOutRdma_Type = Counter32
_ViaOutRdma_Object = MibScalar
viaOutRdma = _ViaOutRdma_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 19),
    _ViaOutRdma_Type()
)
viaOutRdma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaOutRdma.setStatus("current")
_ViaOutBytes_Type = Counter32
_ViaOutBytes_Object = MibScalar
viaOutBytes = _ViaOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 20),
    _ViaOutBytes_Type()
)
viaOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaOutBytes.setStatus("current")
_ViaOutRDMAReadBytes_Type = Counter32
_ViaOutRDMAReadBytes_Object = MibScalar
viaOutRDMAReadBytes = _ViaOutRDMAReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 21),
    _ViaOutRDMAReadBytes_Type()
)
viaOutRDMAReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaOutRDMAReadBytes.setStatus("current")
_ViaOutRDMAWriteBytes_Type = Counter32
_ViaOutRDMAWriteBytes_Object = MibScalar
viaOutRDMAWriteBytes = _ViaOutRDMAWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 22),
    _ViaOutRDMAWriteBytes_Type()
)
viaOutRDMAWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaOutRDMAWriteBytes.setStatus("current")
_ViaConnTable_Object = MibTable
viaConnTable = _ViaConnTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23)
)
if mibBuilder.loadTexts:
    viaConnTable.setStatus("current")
_ViaConnEntry_Object = MibTableRow
viaConnEntry = _ViaConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1)
)
viaConnEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "viaConnVINumber"),
)
if mibBuilder.loadTexts:
    viaConnEntry.setStatus("current")


class _ViaConnState_Type(Integer32):
    """Custom type viaConnState based on Integer32"""
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
        *(("connected", 3),
          ("error", 4),
          ("idle", 1),
          ("pendingConnect", 2))
    )


_ViaConnState_Type.__name__ = "Integer32"
_ViaConnState_Object = MibTableColumn
viaConnState = _ViaConnState_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 1),
    _ViaConnState_Type()
)
viaConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnState.setStatus("current")


class _ViaConnVINumber_Type(Integer32):
    """Custom type viaConnVINumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ViaConnVINumber_Type.__name__ = "Integer32"
_ViaConnVINumber_Object = MibTableColumn
viaConnVINumber = _ViaConnVINumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 2),
    _ViaConnVINumber_Type()
)
viaConnVINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnVINumber.setStatus("current")
_ViaConnRemoteNetAddress_Type = IpAddress
_ViaConnRemoteNetAddress_Object = MibTableColumn
viaConnRemoteNetAddress = _ViaConnRemoteNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 3),
    _ViaConnRemoteNetAddress_Type()
)
viaConnRemoteNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnRemoteNetAddress.setStatus("current")
_ViaConnLocalNetAddress_Type = IpAddress
_ViaConnLocalNetAddress_Object = MibTableColumn
viaConnLocalNetAddress = _ViaConnLocalNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 4),
    _ViaConnLocalNetAddress_Type()
)
viaConnLocalNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnLocalNetAddress.setStatus("current")
_ViaConnRemotePortNumber_Type = Integer32
_ViaConnRemotePortNumber_Object = MibTableColumn
viaConnRemotePortNumber = _ViaConnRemotePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 5),
    _ViaConnRemotePortNumber_Type()
)
viaConnRemotePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnRemotePortNumber.setStatus("current")
_ViaConnLocalPortNumber_Type = Integer32
_ViaConnLocalPortNumber_Object = MibTableColumn
viaConnLocalPortNumber = _ViaConnLocalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 6),
    _ViaConnLocalPortNumber_Type()
)
viaConnLocalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnLocalPortNumber.setStatus("current")
_ViaConnLocalDescriminator_Type = OctetString
_ViaConnLocalDescriminator_Object = MibTableColumn
viaConnLocalDescriminator = _ViaConnLocalDescriminator_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 7),
    _ViaConnLocalDescriminator_Type()
)
viaConnLocalDescriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnLocalDescriminator.setStatus("current")
_ViaConnRemoteDescriminator_Type = OctetString
_ViaConnRemoteDescriminator_Object = MibTableColumn
viaConnRemoteDescriminator = _ViaConnRemoteDescriminator_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 8),
    _ViaConnRemoteDescriminator_Type()
)
viaConnRemoteDescriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnRemoteDescriminator.setStatus("current")
_ViaConnLocalMaxTransferSize_Type = Integer32
_ViaConnLocalMaxTransferSize_Object = MibTableColumn
viaConnLocalMaxTransferSize = _ViaConnLocalMaxTransferSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 9),
    _ViaConnLocalMaxTransferSize_Type()
)
viaConnLocalMaxTransferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnLocalMaxTransferSize.setStatus("current")
_ViaConnRemoteMaxTransferSize_Type = Integer32
_ViaConnRemoteMaxTransferSize_Object = MibTableColumn
viaConnRemoteMaxTransferSize = _ViaConnRemoteMaxTransferSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 10),
    _ViaConnRemoteMaxTransferSize_Type()
)
viaConnRemoteMaxTransferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnRemoteMaxTransferSize.setStatus("current")
_ViaConnLocalEnableRdmaWrite_Type = Integer32
_ViaConnLocalEnableRdmaWrite_Object = MibTableColumn
viaConnLocalEnableRdmaWrite = _ViaConnLocalEnableRdmaWrite_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 11),
    _ViaConnLocalEnableRdmaWrite_Type()
)
viaConnLocalEnableRdmaWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnLocalEnableRdmaWrite.setStatus("current")
_ViaConnLocalEnableRdmaRead_Type = Integer32
_ViaConnLocalEnableRdmaRead_Object = MibTableColumn
viaConnLocalEnableRdmaRead = _ViaConnLocalEnableRdmaRead_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 12),
    _ViaConnLocalEnableRdmaRead_Type()
)
viaConnLocalEnableRdmaRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnLocalEnableRdmaRead.setStatus("current")
_ViaConnRemoteEnableRdmaWrite_Type = Integer32
_ViaConnRemoteEnableRdmaWrite_Object = MibTableColumn
viaConnRemoteEnableRdmaWrite = _ViaConnRemoteEnableRdmaWrite_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 13),
    _ViaConnRemoteEnableRdmaWrite_Type()
)
viaConnRemoteEnableRdmaWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnRemoteEnableRdmaWrite.setStatus("current")
_ViaConnRemoteEnableRdmaRead_Type = Integer32
_ViaConnRemoteEnableRdmaRead_Object = MibTableColumn
viaConnRemoteEnableRdmaRead = _ViaConnRemoteEnableRdmaRead_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 14),
    _ViaConnRemoteEnableRdmaRead_Type()
)
viaConnRemoteEnableRdmaRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnRemoteEnableRdmaRead.setStatus("current")
_ViaConnSentMessages_Type = Counter32
_ViaConnSentMessages_Object = MibTableColumn
viaConnSentMessages = _ViaConnSentMessages_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 15),
    _ViaConnSentMessages_Type()
)
viaConnSentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnSentMessages.setStatus("current")
_ViaConnSentRdmaReadMessages_Type = Counter32
_ViaConnSentRdmaReadMessages_Object = MibTableColumn
viaConnSentRdmaReadMessages = _ViaConnSentRdmaReadMessages_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 16),
    _ViaConnSentRdmaReadMessages_Type()
)
viaConnSentRdmaReadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnSentRdmaReadMessages.setStatus("current")
_ViaConnSentRdmaWriteMessages_Type = Counter32
_ViaConnSentRdmaWriteMessages_Object = MibTableColumn
viaConnSentRdmaWriteMessages = _ViaConnSentRdmaWriteMessages_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 17),
    _ViaConnSentRdmaWriteMessages_Type()
)
viaConnSentRdmaWriteMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnSentRdmaWriteMessages.setStatus("current")
_ViaConnRcvdMessages_Type = Counter32
_ViaConnRcvdMessages_Object = MibTableColumn
viaConnRcvdMessages = _ViaConnRcvdMessages_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 18),
    _ViaConnRcvdMessages_Type()
)
viaConnRcvdMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnRcvdMessages.setStatus("current")
_ViaConnRcvdRdmaReadMessages_Type = Counter32
_ViaConnRcvdRdmaReadMessages_Object = MibTableColumn
viaConnRcvdRdmaReadMessages = _ViaConnRcvdRdmaReadMessages_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 19),
    _ViaConnRcvdRdmaReadMessages_Type()
)
viaConnRcvdRdmaReadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnRcvdRdmaReadMessages.setStatus("current")
_ViaConnRcvdRdmaWriteMessages_Type = Counter32
_ViaConnRcvdRdmaWriteMessages_Object = MibTableColumn
viaConnRcvdRdmaWriteMessages = _ViaConnRcvdRdmaWriteMessages_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 1, 23, 1, 20),
    _ViaConnRcvdRdmaWriteMessages_Type()
)
viaConnRcvdRdmaWriteMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnRcvdRdmaWriteMessages.setStatus("current")
_ViaErrors_ObjectIdentity = ObjectIdentity
viaErrors = _ViaErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 2)
)
_ViaErrPostDesc_Type = Counter32
_ViaErrPostDesc_Object = MibScalar
viaErrPostDesc = _ViaErrPostDesc_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 2, 1),
    _ViaErrPostDesc_Type()
)
viaErrPostDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaErrPostDesc.setStatus("current")
_ViaErrConnLost_Type = Counter32
_ViaErrConnLost_Object = MibScalar
viaErrConnLost = _ViaErrConnLost_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 2, 2),
    _ViaErrConnLost_Type()
)
viaErrConnLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaErrConnLost.setStatus("current")
_ViaErrRecvQEmpty_Type = Counter32
_ViaErrRecvQEmpty_Object = MibScalar
viaErrRecvQEmpty = _ViaErrRecvQEmpty_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 2, 3),
    _ViaErrRecvQEmpty_Type()
)
viaErrRecvQEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaErrRecvQEmpty.setStatus("current")
_ViaErrRdmawProt_Type = Counter32
_ViaErrRdmawProt_Object = MibScalar
viaErrRdmawProt = _ViaErrRdmawProt_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 2, 4),
    _ViaErrRdmawProt_Type()
)
viaErrRdmawProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaErrRdmawProt.setStatus("current")
_ViaErrRdmarProt_Type = Counter32
_ViaErrRdmarProt_Object = MibScalar
viaErrRdmarProt = _ViaErrRdmarProt_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 2, 5),
    _ViaErrRdmarProt_Type()
)
viaErrRdmarProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaErrRdmarProt.setStatus("current")
_ViaErrCompProt_Type = Counter32
_ViaErrCompProt_Object = MibScalar
viaErrCompProt = _ViaErrCompProt_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 2, 6),
    _ViaErrCompProt_Type()
)
viaErrCompProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaErrCompProt.setStatus("current")
_ViaErrorThreshold_Type = Integer32
_ViaErrorThreshold_Object = MibScalar
viaErrorThreshold = _ViaErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 2, 7),
    _ViaErrorThreshold_Type()
)
viaErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaErrorThreshold.setStatus("current")
_ViaNicAttributes_ObjectIdentity = ObjectIdentity
viaNicAttributes = _ViaNicAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3)
)
_ViaNicTable_Object = MibTable
viaNicTable = _ViaNicTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    viaNicTable.setStatus("current")
_ViaNicEntry_Object = MibTableRow
viaNicEntry = _ViaNicEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1)
)
viaNicEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "viaNicIndex"),
)
if mibBuilder.loadTexts:
    viaNicEntry.setStatus("current")


class _ViaNicIndex_Type(Integer32):
    """Custom type viaNicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ViaNicIndex_Type.__name__ = "Integer32"
_ViaNicIndex_Object = MibTableColumn
viaNicIndex = _ViaNicIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 1),
    _ViaNicIndex_Type()
)
viaNicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaNicIndex.setStatus("current")


class _ViaName_Type(DisplayString):
    """Custom type viaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ViaName_Type.__name__ = "DisplayString"
_ViaName_Object = MibTableColumn
viaName = _ViaName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 2),
    _ViaName_Type()
)
viaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaName.setStatus("current")


class _ViaHardwareVersion_Type(DisplayString):
    """Custom type viaHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ViaHardwareVersion_Type.__name__ = "DisplayString"
_ViaHardwareVersion_Object = MibTableColumn
viaHardwareVersion = _ViaHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 3),
    _ViaHardwareVersion_Type()
)
viaHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaHardwareVersion.setStatus("current")


class _ViaProviderVersion_Type(DisplayString):
    """Custom type viaProviderVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ViaProviderVersion_Type.__name__ = "DisplayString"
_ViaProviderVersion_Object = MibTableColumn
viaProviderVersion = _ViaProviderVersion_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 4),
    _ViaProviderVersion_Type()
)
viaProviderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaProviderVersion.setStatus("current")
_ViaNicAddress_Type = PhysAddress
_ViaNicAddress_Object = MibTableColumn
viaNicAddress = _ViaNicAddress_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 5),
    _ViaNicAddress_Type()
)
viaNicAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaNicAddress.setStatus("current")
_ViaThreadSafe_Type = Integer32
_ViaThreadSafe_Object = MibTableColumn
viaThreadSafe = _ViaThreadSafe_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 6),
    _ViaThreadSafe_Type()
)
viaThreadSafe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaThreadSafe.setStatus("current")
_ViaMaxDiscriminatorLength_Type = Integer32
_ViaMaxDiscriminatorLength_Object = MibTableColumn
viaMaxDiscriminatorLength = _ViaMaxDiscriminatorLength_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 7),
    _ViaMaxDiscriminatorLength_Type()
)
viaMaxDiscriminatorLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaMaxDiscriminatorLength.setStatus("current")
_ViaMaxRegisterBytes_Type = Integer32
_ViaMaxRegisterBytes_Object = MibTableColumn
viaMaxRegisterBytes = _ViaMaxRegisterBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 8),
    _ViaMaxRegisterBytes_Type()
)
viaMaxRegisterBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaMaxRegisterBytes.setStatus("current")
_ViaMaxRegisterRegions_Type = Integer32
_ViaMaxRegisterRegions_Object = MibTableColumn
viaMaxRegisterRegions = _ViaMaxRegisterRegions_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 9),
    _ViaMaxRegisterRegions_Type()
)
viaMaxRegisterRegions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaMaxRegisterRegions.setStatus("current")
_ViaMaxRegisterBlockBytes_Type = Integer32
_ViaMaxRegisterBlockBytes_Object = MibTableColumn
viaMaxRegisterBlockBytes = _ViaMaxRegisterBlockBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 10),
    _ViaMaxRegisterBlockBytes_Type()
)
viaMaxRegisterBlockBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaMaxRegisterBlockBytes.setStatus("current")
_ViaMaxVI_Type = Integer32
_ViaMaxVI_Object = MibTableColumn
viaMaxVI = _ViaMaxVI_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 11),
    _ViaMaxVI_Type()
)
viaMaxVI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaMaxVI.setStatus("current")
_ViaMaxDescriptorsPerQueue_Type = Integer32
_ViaMaxDescriptorsPerQueue_Object = MibTableColumn
viaMaxDescriptorsPerQueue = _ViaMaxDescriptorsPerQueue_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 12),
    _ViaMaxDescriptorsPerQueue_Type()
)
viaMaxDescriptorsPerQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaMaxDescriptorsPerQueue.setStatus("current")
_ViaMaxSegmentsPerDesc_Type = Integer32
_ViaMaxSegmentsPerDesc_Object = MibTableColumn
viaMaxSegmentsPerDesc = _ViaMaxSegmentsPerDesc_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 13),
    _ViaMaxSegmentsPerDesc_Type()
)
viaMaxSegmentsPerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaMaxSegmentsPerDesc.setStatus("current")
_ViaMaxCQ_Type = Integer32
_ViaMaxCQ_Object = MibTableColumn
viaMaxCQ = _ViaMaxCQ_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 14),
    _ViaMaxCQ_Type()
)
viaMaxCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaMaxCQ.setStatus("current")
_ViaMaxCQEntries_Type = Integer32
_ViaMaxCQEntries_Object = MibTableColumn
viaMaxCQEntries = _ViaMaxCQEntries_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 15),
    _ViaMaxCQEntries_Type()
)
viaMaxCQEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaMaxCQEntries.setStatus("current")
_ViaMaxTransferSize_Type = Integer32
_ViaMaxTransferSize_Object = MibTableColumn
viaMaxTransferSize = _ViaMaxTransferSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 16),
    _ViaMaxTransferSize_Type()
)
viaMaxTransferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaMaxTransferSize.setStatus("current")
_ViaNativeMTU_Type = Integer32
_ViaNativeMTU_Object = MibTableColumn
viaNativeMTU = _ViaNativeMTU_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 17),
    _ViaNativeMTU_Type()
)
viaNativeMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaNativeMTU.setStatus("current")
_ViaMaxPTags_Type = Integer32
_ViaMaxPTags_Object = MibTableColumn
viaMaxPTags = _ViaMaxPTags_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 18),
    _ViaMaxPTags_Type()
)
viaMaxPTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaMaxPTags.setStatus("current")
_ViaCurrRegisterBytes_Type = Integer32
_ViaCurrRegisterBytes_Object = MibTableColumn
viaCurrRegisterBytes = _ViaCurrRegisterBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 19),
    _ViaCurrRegisterBytes_Type()
)
viaCurrRegisterBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaCurrRegisterBytes.setStatus("current")
_ViaCurrRegisterRegions_Type = Integer32
_ViaCurrRegisterRegions_Object = MibTableColumn
viaCurrRegisterRegions = _ViaCurrRegisterRegions_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 20),
    _ViaCurrRegisterRegions_Type()
)
viaCurrRegisterRegions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaCurrRegisterRegions.setStatus("current")
_ViaCurrVI_Type = Integer32
_ViaCurrVI_Object = MibTableColumn
viaCurrVI = _ViaCurrVI_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 21),
    _ViaCurrVI_Type()
)
viaCurrVI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaCurrVI.setStatus("current")
_ViaCurrCQ_Type = Integer32
_ViaCurrCQ_Object = MibTableColumn
viaCurrCQ = _ViaCurrCQ_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 22),
    _ViaCurrCQ_Type()
)
viaCurrCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaCurrCQ.setStatus("current")
_ViaCurrPTags_Type = Integer32
_ViaCurrPTags_Object = MibTableColumn
viaCurrPTags = _ViaCurrPTags_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 23),
    _ViaCurrPTags_Type()
)
viaCurrPTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaCurrPTags.setStatus("current")
_ViaConnectionListenPort_Type = Integer32
_ViaConnectionListenPort_Object = MibTableColumn
viaConnectionListenPort = _ViaConnectionListenPort_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 13, 3, 1, 1, 24),
    _ViaConnectionListenPort_Type()
)
viaConnectionListenPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viaConnectionListenPort.setStatus("current")
_Backup_ObjectIdentity = ObjectIdentity
backup = _Backup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 14)
)
_Dump_ObjectIdentity = ObjectIdentity
dump = _Dump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1)
)
_DmpActives_Type = Integer32
_DmpActives_Object = MibScalar
dmpActives = _DmpActives_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 1),
    _DmpActives_Type()
)
dmpActives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpActives.setStatus("current")
_DmpAttempts_Type = Counter32
_DmpAttempts_Object = MibScalar
dmpAttempts = _DmpAttempts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 2),
    _DmpAttempts_Type()
)
dmpAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpAttempts.setStatus("current")
_DmpSuccesses_Type = Counter32
_DmpSuccesses_Object = MibScalar
dmpSuccesses = _DmpSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 3),
    _DmpSuccesses_Type()
)
dmpSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpSuccesses.setStatus("current")
_DmpFailures_Type = Counter32
_DmpFailures_Object = MibScalar
dmpFailures = _DmpFailures_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 4),
    _DmpFailures_Type()
)
dmpFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpFailures.setStatus("current")
_DmpTable_Object = MibTable
dmpTable = _DmpTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5)
)
if mibBuilder.loadTexts:
    dmpTable.setStatus("current")
_DmpEntry_Object = MibTableRow
dmpEntry = _DmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1)
)
dmpEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "dmpIndex"),
)
if mibBuilder.loadTexts:
    dmpEntry.setStatus("current")


class _DmpIndex_Type(Integer32):
    """Custom type dmpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DmpIndex_Type.__name__ = "Integer32"
_DmpIndex_Object = MibTableColumn
dmpIndex = _DmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1, 1),
    _DmpIndex_Type()
)
dmpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpIndex.setStatus("current")
_DmpStPath_Type = DisplayString
_DmpStPath_Object = MibTableColumn
dmpStPath = _DmpStPath_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1, 2),
    _DmpStPath_Type()
)
dmpStPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpStPath.setStatus("current")
_DmpStAttempts_Type = Counter32
_DmpStAttempts_Object = MibTableColumn
dmpStAttempts = _DmpStAttempts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1, 3),
    _DmpStAttempts_Type()
)
dmpStAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpStAttempts.setStatus("current")
_DmpStSuccesses_Type = Counter32
_DmpStSuccesses_Object = MibTableColumn
dmpStSuccesses = _DmpStSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1, 4),
    _DmpStSuccesses_Type()
)
dmpStSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpStSuccesses.setStatus("current")
_DmpStFailures_Type = Counter32
_DmpStFailures_Object = MibTableColumn
dmpStFailures = _DmpStFailures_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1, 5),
    _DmpStFailures_Type()
)
dmpStFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpStFailures.setStatus("current")
_DmpTime_Type = Integer32
_DmpTime_Object = MibTableColumn
dmpTime = _DmpTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1, 6),
    _DmpTime_Type()
)
dmpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpTime.setStatus("current")


class _DmpStatus_Type(Integer32):
    """Custom type dmpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DmpStatus_Type.__name__ = "Integer32"
_DmpStatus_Object = MibTableColumn
dmpStatus = _DmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1, 7),
    _DmpStatus_Type()
)
dmpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpStatus.setStatus("current")


class _DmpLevel_Type(Integer32):
    """Custom type dmpLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_DmpLevel_Type.__name__ = "Integer32"
_DmpLevel_Object = MibTableColumn
dmpLevel = _DmpLevel_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1, 8),
    _DmpLevel_Type()
)
dmpLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpLevel.setStatus("current")
_DmpNumFiles_Type = Integer32
_DmpNumFiles_Object = MibTableColumn
dmpNumFiles = _DmpNumFiles_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1, 9),
    _DmpNumFiles_Type()
)
dmpNumFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpNumFiles.setStatus("current")
_DmpDataAmount_Type = Integer32
_DmpDataAmount_Object = MibTableColumn
dmpDataAmount = _DmpDataAmount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1, 10),
    _DmpDataAmount_Type()
)
dmpDataAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpDataAmount.setStatus("current")
_DmpStartTime_Type = Integer32
_DmpStartTime_Object = MibTableColumn
dmpStartTime = _DmpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1, 11),
    _DmpStartTime_Type()
)
dmpStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpStartTime.setStatus("current")
_DmpDuration_Type = TimeTicks
_DmpDuration_Object = MibTableColumn
dmpDuration = _DmpDuration_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 1, 5, 1, 12),
    _DmpDuration_Type()
)
dmpDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmpDuration.setStatus("current")
_Restore_ObjectIdentity = ObjectIdentity
restore = _Restore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 2)
)
_RstActives_Type = Integer32
_RstActives_Object = MibScalar
rstActives = _RstActives_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 2, 1),
    _RstActives_Type()
)
rstActives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstActives.setStatus("current")
_RstAttempts_Type = Counter32
_RstAttempts_Object = MibScalar
rstAttempts = _RstAttempts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 2, 2),
    _RstAttempts_Type()
)
rstAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstAttempts.setStatus("current")
_RstSuccesses_Type = Counter32
_RstSuccesses_Object = MibScalar
rstSuccesses = _RstSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 2, 3),
    _RstSuccesses_Type()
)
rstSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstSuccesses.setStatus("current")
_RstFailures_Type = Counter32
_RstFailures_Object = MibScalar
rstFailures = _RstFailures_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 14, 2, 4),
    _RstFailures_Type()
)
rstFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstFailures.setStatus("current")
_Vfiler_ObjectIdentity = ObjectIdentity
vfiler = _Vfiler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 16)
)


class _VfilerIsLicensed_Type(Integer32):
    """Custom type vfilerIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VfilerIsLicensed_Type.__name__ = "Integer32"
_VfilerIsLicensed_Object = MibScalar
vfilerIsLicensed = _VfilerIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 1),
    _VfilerIsLicensed_Type()
)
vfilerIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfilerIsLicensed.setStatus("current")
_VfFilers_Type = Counter32
_VfFilers_Object = MibScalar
vfFilers = _VfFilers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 2),
    _VfFilers_Type()
)
vfFilers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfFilers.setStatus("current")
_VfTable_Object = MibTable
vfTable = _VfTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 3)
)
if mibBuilder.loadTexts:
    vfTable.setStatus("current")
_VfEntry_Object = MibTableRow
vfEntry = _VfEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 3, 1)
)
vfEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "vfIndex"),
)
if mibBuilder.loadTexts:
    vfEntry.setStatus("current")


class _VfIndex_Type(Integer32):
    """Custom type vfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VfIndex_Type.__name__ = "Integer32"
_VfIndex_Object = MibTableColumn
vfIndex = _VfIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 3, 1, 1),
    _VfIndex_Type()
)
vfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfIndex.setStatus("current")
_VfName_Type = DisplayString
_VfName_Object = MibTableColumn
vfName = _VfName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 3, 1, 2),
    _VfName_Type()
)
vfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfName.setStatus("current")


class _VfUuid_Type(OctetString):
    """Custom type vfUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_VfUuid_Type.__name__ = "OctetString"
_VfUuid_Object = MibTableColumn
vfUuid = _VfUuid_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 3, 1, 3),
    _VfUuid_Type()
)
vfUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfUuid.setStatus("current")
_VfIpAddresses_Type = Integer32
_VfIpAddresses_Object = MibTableColumn
vfIpAddresses = _VfIpAddresses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 3, 1, 4),
    _VfIpAddresses_Type()
)
vfIpAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfIpAddresses.setStatus("current")
_VfStoragePaths_Type = Integer32
_VfStoragePaths_Object = MibTableColumn
vfStoragePaths = _VfStoragePaths_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 3, 1, 5),
    _VfStoragePaths_Type()
)
vfStoragePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfStoragePaths.setStatus("current")
_VfIpSpace_Type = DisplayString
_VfIpSpace_Object = MibTableColumn
vfIpSpace = _VfIpSpace_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 3, 1, 6),
    _VfIpSpace_Type()
)
vfIpSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfIpSpace.setStatus("current")
_VfAllowedProtocols_Type = Integer32
_VfAllowedProtocols_Object = MibTableColumn
vfAllowedProtocols = _VfAllowedProtocols_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 3, 1, 7),
    _VfAllowedProtocols_Type()
)
vfAllowedProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfAllowedProtocols.setStatus("current")
_VfDisallowedProtocols_Type = Integer32
_VfDisallowedProtocols_Object = MibTableColumn
vfDisallowedProtocols = _VfDisallowedProtocols_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 3, 1, 8),
    _VfDisallowedProtocols_Type()
)
vfDisallowedProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfDisallowedProtocols.setStatus("current")


class _VfState_Type(Integer32):
    """Custom type vfState based on Integer32"""
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


_VfState_Type.__name__ = "Integer32"
_VfState_Object = MibTableColumn
vfState = _VfState_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 3, 1, 9),
    _VfState_Type()
)
vfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfState.setStatus("current")
_VfIpTable_Object = MibTable
vfIpTable = _VfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 4)
)
if mibBuilder.loadTexts:
    vfIpTable.setStatus("current")
_VfIpEntry_Object = MibTableRow
vfIpEntry = _VfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 4, 1)
)
vfIpEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "vfFiIndex"),
    (0, "NETWORK-APPLIANCE-MIB", "vfIpIndex"),
)
if mibBuilder.loadTexts:
    vfIpEntry.setStatus("current")


class _VfFiIndex_Type(Integer32):
    """Custom type vfFiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VfFiIndex_Type.__name__ = "Integer32"
_VfFiIndex_Object = MibTableColumn
vfFiIndex = _VfFiIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 4, 1, 1),
    _VfFiIndex_Type()
)
vfFiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfFiIndex.setStatus("current")


class _VfIpIndex_Type(Integer32):
    """Custom type vfIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VfIpIndex_Type.__name__ = "Integer32"
_VfIpIndex_Object = MibTableColumn
vfIpIndex = _VfIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 4, 1, 2),
    _VfIpIndex_Type()
)
vfIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfIpIndex.setStatus("current")
_VfIpAddr_Type = IpAddress
_VfIpAddr_Object = MibTableColumn
vfIpAddr = _VfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 4, 1, 3),
    _VfIpAddr_Type()
)
vfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfIpAddr.setStatus("current")
_VfSpTable_Object = MibTable
vfSpTable = _VfSpTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 5)
)
if mibBuilder.loadTexts:
    vfSpTable.setStatus("current")
_VfSpEntry_Object = MibTableRow
vfSpEntry = _VfSpEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 5, 1)
)
vfSpEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "vfFsIndex"),
    (0, "NETWORK-APPLIANCE-MIB", "vfSpIndex"),
)
if mibBuilder.loadTexts:
    vfSpEntry.setStatus("current")


class _VfFsIndex_Type(Integer32):
    """Custom type vfFsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VfFsIndex_Type.__name__ = "Integer32"
_VfFsIndex_Object = MibTableColumn
vfFsIndex = _VfFsIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 5, 1, 1),
    _VfFsIndex_Type()
)
vfFsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfFsIndex.setStatus("current")


class _VfSpIndex_Type(Integer32):
    """Custom type vfSpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VfSpIndex_Type.__name__ = "Integer32"
_VfSpIndex_Object = MibTableColumn
vfSpIndex = _VfSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 5, 1, 2),
    _VfSpIndex_Type()
)
vfSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfSpIndex.setStatus("current")


class _VfSpName_Type(OctetString):
    """Custom type vfSpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_VfSpName_Type.__name__ = "OctetString"
_VfSpName_Object = MibTableColumn
vfSpName = _VfSpName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 5, 1, 3),
    _VfSpName_Type()
)
vfSpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfSpName.setStatus("current")
_VfProTable_Object = MibTable
vfProTable = _VfProTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 6)
)
if mibBuilder.loadTexts:
    vfProTable.setStatus("current")
_VfProEntry_Object = MibTableRow
vfProEntry = _VfProEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 6, 1)
)
vfProEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "vfFpIndex"),
    (0, "NETWORK-APPLIANCE-MIB", "vfProIndex"),
)
if mibBuilder.loadTexts:
    vfProEntry.setStatus("current")


class _VfFpIndex_Type(Integer32):
    """Custom type vfFpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VfFpIndex_Type.__name__ = "Integer32"
_VfFpIndex_Object = MibTableColumn
vfFpIndex = _VfFpIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 6, 1, 1),
    _VfFpIndex_Type()
)
vfFpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfFpIndex.setStatus("current")


class _VfProIndex_Type(Integer32):
    """Custom type vfProIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VfProIndex_Type.__name__ = "Integer32"
_VfProIndex_Object = MibTableColumn
vfProIndex = _VfProIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 6, 1, 2),
    _VfProIndex_Type()
)
vfProIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfProIndex.setStatus("current")


class _VfProName_Type(OctetString):
    """Custom type vfProName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_VfProName_Type.__name__ = "OctetString"
_VfProName_Object = MibTableColumn
vfProName = _VfProName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 6, 1, 3),
    _VfProName_Type()
)
vfProName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfProName.setStatus("current")


class _VfProStatus_Type(Integer32):
    """Custom type vfProStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_VfProStatus_Type.__name__ = "Integer32"
_VfProStatus_Object = MibTableColumn
vfProStatus = _VfProStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 16, 6, 1, 4),
    _VfProStatus_Type()
)
vfProStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfProStatus.setStatus("current")
_Blocks_ObjectIdentity = ObjectIdentity
blocks = _Blocks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 17)
)


class _FcpIsLicensed_Type(Integer32):
    """Custom type fcpIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FcpIsLicensed_Type.__name__ = "Integer32"
_FcpIsLicensed_Object = MibScalar
fcpIsLicensed = _FcpIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 1),
    _FcpIsLicensed_Type()
)
fcpIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpIsLicensed.setStatus("current")


class _IscsiIsLicensed_Type(Integer32):
    """Custom type iscsiIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_IscsiIsLicensed_Type.__name__ = "Integer32"
_IscsiIsLicensed_Object = MibScalar
iscsiIsLicensed = _IscsiIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 2),
    _IscsiIsLicensed_Type()
)
iscsiIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIsLicensed.setStatus("current")
_FcpLowReadBytes_Type = Counter32
_FcpLowReadBytes_Object = MibScalar
fcpLowReadBytes = _FcpLowReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 3),
    _FcpLowReadBytes_Type()
)
fcpLowReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpLowReadBytes.setStatus("current")
_FcpHighReadBytes_Type = Counter32
_FcpHighReadBytes_Object = MibScalar
fcpHighReadBytes = _FcpHighReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 4),
    _FcpHighReadBytes_Type()
)
fcpHighReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpHighReadBytes.setStatus("current")
_FcpLowWriteBytes_Type = Counter32
_FcpLowWriteBytes_Object = MibScalar
fcpLowWriteBytes = _FcpLowWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 5),
    _FcpLowWriteBytes_Type()
)
fcpLowWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpLowWriteBytes.setStatus("current")
_FcpHighWriteBytes_Type = Counter32
_FcpHighWriteBytes_Object = MibScalar
fcpHighWriteBytes = _FcpHighWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 6),
    _FcpHighWriteBytes_Type()
)
fcpHighWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpHighWriteBytes.setStatus("current")
_IscsiLowReadBytes_Type = Counter32
_IscsiLowReadBytes_Object = MibScalar
iscsiLowReadBytes = _IscsiLowReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 7),
    _IscsiLowReadBytes_Type()
)
iscsiLowReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiLowReadBytes.setStatus("current")
_IscsiHighReadBytes_Type = Counter32
_IscsiHighReadBytes_Object = MibScalar
iscsiHighReadBytes = _IscsiHighReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 8),
    _IscsiHighReadBytes_Type()
)
iscsiHighReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiHighReadBytes.setStatus("current")
_IscsiLowWriteBytes_Type = Counter32
_IscsiLowWriteBytes_Object = MibScalar
iscsiLowWriteBytes = _IscsiLowWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 9),
    _IscsiLowWriteBytes_Type()
)
iscsiLowWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiLowWriteBytes.setStatus("current")
_IscsiHighWriteBytes_Type = Counter32
_IscsiHighWriteBytes_Object = MibScalar
iscsiHighWriteBytes = _IscsiHighWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 10),
    _IscsiHighWriteBytes_Type()
)
iscsiHighWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiHighWriteBytes.setStatus("current")
_IscsiHighOps_Type = Counter32
_IscsiHighOps_Object = MibScalar
iscsiHighOps = _IscsiHighOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 11),
    _IscsiHighOps_Type()
)
iscsiHighOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiHighOps.setStatus("current")
_IscsiLowOps_Type = Counter32
_IscsiLowOps_Object = MibScalar
iscsiLowOps = _IscsiLowOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 12),
    _IscsiLowOps_Type()
)
iscsiLowOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiLowOps.setStatus("current")
_FcpHighOps_Type = Counter32
_FcpHighOps_Object = MibScalar
fcpHighOps = _FcpHighOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 13),
    _FcpHighOps_Type()
)
fcpHighOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpHighOps.setStatus("current")
_FcpLowOps_Type = Counter32
_FcpLowOps_Object = MibScalar
fcpLowOps = _FcpLowOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 14),
    _FcpLowOps_Type()
)
fcpLowOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpLowOps.setStatus("current")
_Lun_ObjectIdentity = ObjectIdentity
lun = _Lun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15)
)
_LunCount_Type = Integer32
_LunCount_Object = MibScalar
lunCount = _LunCount_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 1),
    _LunCount_Type()
)
lunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunCount.setStatus("current")
_LunTable_Object = MibTable
lunTable = _LunTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2)
)
if mibBuilder.loadTexts:
    lunTable.setStatus("current")
_LunEntry_Object = MibTableRow
lunEntry = _LunEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1)
)
lunEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "lunIndex"),
)
if mibBuilder.loadTexts:
    lunEntry.setStatus("current")


class _LunIndex_Type(Integer32):
    """Custom type lunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LunIndex_Type.__name__ = "Integer32"
_LunIndex_Object = MibTableColumn
lunIndex = _LunIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 1),
    _LunIndex_Type()
)
lunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunIndex.setStatus("current")
_LunName_Type = DisplayString
_LunName_Object = MibTableColumn
lunName = _LunName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 2),
    _LunName_Type()
)
lunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunName.setStatus("current")
_LunComment_Type = DisplayString
_LunComment_Object = MibTableColumn
lunComment = _LunComment_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 3),
    _LunComment_Type()
)
lunComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunComment.setStatus("current")
_LunSizeLow_Type = Integer32
_LunSizeLow_Object = MibTableColumn
lunSizeLow = _LunSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 4),
    _LunSizeLow_Type()
)
lunSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunSizeLow.setStatus("current")
_LunSizeHigh_Type = Integer32
_LunSizeHigh_Object = MibTableColumn
lunSizeHigh = _LunSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 5),
    _LunSizeHigh_Type()
)
lunSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunSizeHigh.setStatus("current")


class _LunMapped_Type(Integer32):
    """Custom type lunMapped based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_LunMapped_Type.__name__ = "Integer32"
_LunMapped_Object = MibTableColumn
lunMapped = _LunMapped_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 6),
    _LunMapped_Type()
)
lunMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunMapped.setStatus("current")
_LunSerialNumber_Type = DisplayString
_LunSerialNumber_Object = MibTableColumn
lunSerialNumber = _LunSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 7),
    _LunSerialNumber_Type()
)
lunSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunSerialNumber.setStatus("current")
_LunQtreeName_Type = DisplayString
_LunQtreeName_Object = MibTableColumn
lunQtreeName = _LunQtreeName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 8),
    _LunQtreeName_Type()
)
lunQtreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunQtreeName.setStatus("current")
_LunHighOps_Type = Counter32
_LunHighOps_Object = MibTableColumn
lunHighOps = _LunHighOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 9),
    _LunHighOps_Type()
)
lunHighOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunHighOps.setStatus("current")
_LunLowOps_Type = Counter32
_LunLowOps_Object = MibTableColumn
lunLowOps = _LunLowOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 10),
    _LunLowOps_Type()
)
lunLowOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunLowOps.setStatus("current")
_LunHighReadBytes_Type = Counter32
_LunHighReadBytes_Object = MibTableColumn
lunHighReadBytes = _LunHighReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 11),
    _LunHighReadBytes_Type()
)
lunHighReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunHighReadBytes.setStatus("current")
_LunLowReadBytes_Type = Counter32
_LunLowReadBytes_Object = MibTableColumn
lunLowReadBytes = _LunLowReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 12),
    _LunLowReadBytes_Type()
)
lunLowReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunLowReadBytes.setStatus("current")
_LunHighWriteBytes_Type = Counter32
_LunHighWriteBytes_Object = MibTableColumn
lunHighWriteBytes = _LunHighWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 13),
    _LunHighWriteBytes_Type()
)
lunHighWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunHighWriteBytes.setStatus("current")
_LunLowWriteBytes_Type = Counter32
_LunLowWriteBytes_Object = MibTableColumn
lunLowWriteBytes = _LunLowWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 14),
    _LunLowWriteBytes_Type()
)
lunLowWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunLowWriteBytes.setStatus("current")
_LunHighErrors_Type = Counter32
_LunHighErrors_Object = MibTableColumn
lunHighErrors = _LunHighErrors_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 15),
    _LunHighErrors_Type()
)
lunHighErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunHighErrors.setStatus("current")
_LunLowErrors_Type = Counter32
_LunLowErrors_Object = MibTableColumn
lunLowErrors = _LunLowErrors_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 16),
    _LunLowErrors_Type()
)
lunLowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunLowErrors.setStatus("current")


class _LunOnline_Type(Integer32):
    """Custom type lunOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_LunOnline_Type.__name__ = "Integer32"
_LunOnline_Object = MibTableColumn
lunOnline = _LunOnline_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 17),
    _LunOnline_Type()
)
lunOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunOnline.setStatus("current")


class _LunSnapStatus_Type(Integer32):
    """Custom type lunSnapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_LunSnapStatus_Type.__name__ = "Integer32"
_LunSnapStatus_Object = MibTableColumn
lunSnapStatus = _LunSnapStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 18),
    _LunSnapStatus_Type()
)
lunSnapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunSnapStatus.setStatus("current")


class _LunShareStatus_Type(Integer32):
    """Custom type lunShareStatus based on Integer32"""
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
        *(("all", 4),
          ("none", 1),
          ("read", 2),
          ("write", 3))
    )


_LunShareStatus_Type.__name__ = "Integer32"
_LunShareStatus_Object = MibTableColumn
lunShareStatus = _LunShareStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 19),
    _LunShareStatus_Type()
)
lunShareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunShareStatus.setStatus("current")


class _LunSpaceReserved_Type(Integer32):
    """Custom type lunSpaceReserved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_LunSpaceReserved_Type.__name__ = "Integer32"
_LunSpaceReserved_Object = MibTableColumn
lunSpaceReserved = _LunSpaceReserved_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 20),
    _LunSpaceReserved_Type()
)
lunSpaceReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunSpaceReserved.setStatus("current")
_LunStatsResetTime_Type = Integer32
_LunStatsResetTime_Object = MibTableColumn
lunStatsResetTime = _LunStatsResetTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 21),
    _LunStatsResetTime_Type()
)
lunStatsResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunStatsResetTime.setStatus("current")
_LunHighReadOps_Type = Counter32
_LunHighReadOps_Object = MibTableColumn
lunHighReadOps = _LunHighReadOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 22),
    _LunHighReadOps_Type()
)
lunHighReadOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunHighReadOps.setStatus("current")
_LunLowReadOps_Type = Counter32
_LunLowReadOps_Object = MibTableColumn
lunLowReadOps = _LunLowReadOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 23),
    _LunLowReadOps_Type()
)
lunLowReadOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunLowReadOps.setStatus("current")
_LunHighWriteOps_Type = Counter32
_LunHighWriteOps_Object = MibTableColumn
lunHighWriteOps = _LunHighWriteOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 24),
    _LunHighWriteOps_Type()
)
lunHighWriteOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunHighWriteOps.setStatus("current")
_LunLowWriteOps_Type = Counter32
_LunLowWriteOps_Object = MibTableColumn
lunLowWriteOps = _LunLowWriteOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 25),
    _LunLowWriteOps_Type()
)
lunLowWriteOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunLowWriteOps.setStatus("current")
_LunHighOtherOps_Type = Counter32
_LunHighOtherOps_Object = MibTableColumn
lunHighOtherOps = _LunHighOtherOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 26),
    _LunHighOtherOps_Type()
)
lunHighOtherOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunHighOtherOps.setStatus("current")
_LunLowOtherOps_Type = Counter32
_LunLowOtherOps_Object = MibTableColumn
lunLowOtherOps = _LunLowOtherOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 27),
    _LunLowOtherOps_Type()
)
lunLowOtherOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunLowOtherOps.setStatus("current")
_LunSize64_Type = Counter64
_LunSize64_Object = MibTableColumn
lunSize64 = _LunSize64_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 28),
    _LunSize64_Type()
)
lunSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunSize64.setStatus("current")
_Lun64Ops_Type = Counter64
_Lun64Ops_Object = MibTableColumn
lun64Ops = _Lun64Ops_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 29),
    _Lun64Ops_Type()
)
lun64Ops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun64Ops.setStatus("current")
_Lun64ReadBytes_Type = Counter64
_Lun64ReadBytes_Object = MibTableColumn
lun64ReadBytes = _Lun64ReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 30),
    _Lun64ReadBytes_Type()
)
lun64ReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun64ReadBytes.setStatus("current")
_Lun64WriteBytes_Type = Counter64
_Lun64WriteBytes_Object = MibTableColumn
lun64WriteBytes = _Lun64WriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 31),
    _Lun64WriteBytes_Type()
)
lun64WriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun64WriteBytes.setStatus("current")
_Lun64Errors_Type = Counter64
_Lun64Errors_Object = MibTableColumn
lun64Errors = _Lun64Errors_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 32),
    _Lun64Errors_Type()
)
lun64Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun64Errors.setStatus("current")
_Lun64ReadOps_Type = Counter64
_Lun64ReadOps_Object = MibTableColumn
lun64ReadOps = _Lun64ReadOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 33),
    _Lun64ReadOps_Type()
)
lun64ReadOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun64ReadOps.setStatus("current")
_Lun64WriteOps_Type = Counter64
_Lun64WriteOps_Object = MibTableColumn
lun64WriteOps = _Lun64WriteOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 34),
    _Lun64WriteOps_Type()
)
lun64WriteOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun64WriteOps.setStatus("current")
_Lun64OtherOps_Type = Counter64
_Lun64OtherOps_Object = MibTableColumn
lun64OtherOps = _Lun64OtherOps_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 2, 1, 35),
    _Lun64OtherOps_Type()
)
lun64OtherOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun64OtherOps.setStatus("current")
_LunMapTable_Object = MibTable
lunMapTable = _LunMapTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 3)
)
if mibBuilder.loadTexts:
    lunMapTable.setStatus("current")
_LunMapEntry_Object = MibTableRow
lunMapEntry = _LunMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 3, 1)
)
lunMapEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "lunMapLUNIndex"),
    (0, "NETWORK-APPLIANCE-MIB", "lunMapInitiatorGroupIndex"),
)
if mibBuilder.loadTexts:
    lunMapEntry.setStatus("current")


class _LunMapLUNIndex_Type(Integer32):
    """Custom type lunMapLUNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LunMapLUNIndex_Type.__name__ = "Integer32"
_LunMapLUNIndex_Object = MibTableColumn
lunMapLUNIndex = _LunMapLUNIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 3, 1, 1),
    _LunMapLUNIndex_Type()
)
lunMapLUNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunMapLUNIndex.setStatus("current")


class _LunMapInitiatorGroupIndex_Type(Integer32):
    """Custom type lunMapInitiatorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LunMapInitiatorGroupIndex_Type.__name__ = "Integer32"
_LunMapInitiatorGroupIndex_Object = MibTableColumn
lunMapInitiatorGroupIndex = _LunMapInitiatorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 3, 1, 2),
    _LunMapInitiatorGroupIndex_Type()
)
lunMapInitiatorGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunMapInitiatorGroupIndex.setStatus("current")
_LunMapLUNName_Type = DisplayString
_LunMapLUNName_Object = MibTableColumn
lunMapLUNName = _LunMapLUNName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 3, 1, 3),
    _LunMapLUNName_Type()
)
lunMapLUNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunMapLUNName.setStatus("current")
_LunMapInitiatorGroupName_Type = DisplayString
_LunMapInitiatorGroupName_Object = MibTableColumn
lunMapInitiatorGroupName = _LunMapInitiatorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 3, 1, 4),
    _LunMapInitiatorGroupName_Type()
)
lunMapInitiatorGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunMapInitiatorGroupName.setStatus("current")
_LunMapLogicalUnitNumber_Type = Integer32
_LunMapLogicalUnitNumber_Object = MibTableColumn
lunMapLogicalUnitNumber = _LunMapLogicalUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 15, 3, 1, 5),
    _LunMapLogicalUnitNumber_Type()
)
lunMapLogicalUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunMapLogicalUnitNumber.setStatus("current")
_Initiator_ObjectIdentity = ObjectIdentity
initiator = _Initiator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16)
)
_InitiatorGroupTable_Object = MibTable
initiatorGroupTable = _InitiatorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 1)
)
if mibBuilder.loadTexts:
    initiatorGroupTable.setStatus("current")
_InitiatorGroupEntry_Object = MibTableRow
initiatorGroupEntry = _InitiatorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 1, 1)
)
initiatorGroupEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "initiatorGroupIndex"),
)
if mibBuilder.loadTexts:
    initiatorGroupEntry.setStatus("current")


class _InitiatorGroupIndex_Type(Integer32):
    """Custom type initiatorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InitiatorGroupIndex_Type.__name__ = "Integer32"
_InitiatorGroupIndex_Object = MibTableColumn
initiatorGroupIndex = _InitiatorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 1, 1, 1),
    _InitiatorGroupIndex_Type()
)
initiatorGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorGroupIndex.setStatus("current")
_InitiatorGroupName_Type = DisplayString
_InitiatorGroupName_Object = MibTableColumn
initiatorGroupName = _InitiatorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 1, 1, 2),
    _InitiatorGroupName_Type()
)
initiatorGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorGroupName.setStatus("current")


class _InitiatorGroupType_Type(Integer32):
    """Custom type initiatorGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcp", 1),
          ("iSCSI", 2))
    )


_InitiatorGroupType_Type.__name__ = "Integer32"
_InitiatorGroupType_Object = MibTableColumn
initiatorGroupType = _InitiatorGroupType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 1, 1, 3),
    _InitiatorGroupType_Type()
)
initiatorGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorGroupType.setStatus("current")


class _InitiatorGroupOS_Type(Integer32):
    """Custom type initiatorGroupOS based on Integer32"""
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
              256)
        )
    )
    namedValues = NamedValues(
        *(("aix", 5),
          ("default", 1),
          ("defaultPartner", 7),
          ("hpux", 4),
          ("invalid", 256),
          ("linux", 6),
          ("netware", 8),
          ("openvms", 10),
          ("solaris", 2),
          ("vmware", 9),
          ("windows", 3))
    )


_InitiatorGroupOS_Type.__name__ = "Integer32"
_InitiatorGroupOS_Object = MibTableColumn
initiatorGroupOS = _InitiatorGroupOS_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 1, 1, 4),
    _InitiatorGroupOS_Type()
)
initiatorGroupOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorGroupOS.setStatus("current")


class _InitiatorGroupThrottleReserve_Type(Integer32):
    """Custom type initiatorGroupThrottleReserve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_InitiatorGroupThrottleReserve_Type.__name__ = "Integer32"
_InitiatorGroupThrottleReserve_Object = MibTableColumn
initiatorGroupThrottleReserve = _InitiatorGroupThrottleReserve_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 1, 1, 5),
    _InitiatorGroupThrottleReserve_Type()
)
initiatorGroupThrottleReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorGroupThrottleReserve.setStatus("current")


class _InitiatorGroupThrottleBorrow_Type(Integer32):
    """Custom type initiatorGroupThrottleBorrow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_InitiatorGroupThrottleBorrow_Type.__name__ = "Integer32"
_InitiatorGroupThrottleBorrow_Object = MibTableColumn
initiatorGroupThrottleBorrow = _InitiatorGroupThrottleBorrow_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 1, 1, 6),
    _InitiatorGroupThrottleBorrow_Type()
)
initiatorGroupThrottleBorrow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorGroupThrottleBorrow.setStatus("current")


class _InitiatorGroupUsePartner_Type(Integer32):
    """Custom type initiatorGroupUsePartner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_InitiatorGroupUsePartner_Type.__name__ = "Integer32"
_InitiatorGroupUsePartner_Object = MibTableColumn
initiatorGroupUsePartner = _InitiatorGroupUsePartner_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 1, 1, 7),
    _InitiatorGroupUsePartner_Type()
)
initiatorGroupUsePartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorGroupUsePartner.setStatus("current")


class _InitiatorGroupUseALUA_Type(Integer32):
    """Custom type initiatorGroupUseALUA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_InitiatorGroupUseALUA_Type.__name__ = "Integer32"
_InitiatorGroupUseALUA_Object = MibTableColumn
initiatorGroupUseALUA = _InitiatorGroupUseALUA_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 1, 1, 8),
    _InitiatorGroupUseALUA_Type()
)
initiatorGroupUseALUA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorGroupUseALUA.setStatus("current")
_InitiatorGroupMemberTable_Object = MibTable
initiatorGroupMemberTable = _InitiatorGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 2)
)
if mibBuilder.loadTexts:
    initiatorGroupMemberTable.setStatus("current")
_InitiatorGroupMemberEntry_Object = MibTableRow
initiatorGroupMemberEntry = _InitiatorGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 2, 1)
)
initiatorGroupMemberEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "initiatorGroupMemberIndex"),
    (0, "NETWORK-APPLIANCE-MIB", "initiatorGroupMemberNameIndex"),
)
if mibBuilder.loadTexts:
    initiatorGroupMemberEntry.setStatus("current")


class _InitiatorGroupMemberIndex_Type(Integer32):
    """Custom type initiatorGroupMemberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InitiatorGroupMemberIndex_Type.__name__ = "Integer32"
_InitiatorGroupMemberIndex_Object = MibTableColumn
initiatorGroupMemberIndex = _InitiatorGroupMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 2, 1, 1),
    _InitiatorGroupMemberIndex_Type()
)
initiatorGroupMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorGroupMemberIndex.setStatus("current")


class _InitiatorGroupMemberNameIndex_Type(Integer32):
    """Custom type initiatorGroupMemberNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InitiatorGroupMemberNameIndex_Type.__name__ = "Integer32"
_InitiatorGroupMemberNameIndex_Object = MibTableColumn
initiatorGroupMemberNameIndex = _InitiatorGroupMemberNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 2, 1, 2),
    _InitiatorGroupMemberNameIndex_Type()
)
initiatorGroupMemberNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorGroupMemberNameIndex.setStatus("current")
_InitiatorName_Type = DisplayString
_InitiatorName_Object = MibTableColumn
initiatorName = _InitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 2, 1, 3),
    _InitiatorName_Type()
)
initiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorName.setStatus("current")
_InitiatorListTable_Object = MibTable
initiatorListTable = _InitiatorListTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 3)
)
if mibBuilder.loadTexts:
    initiatorListTable.setStatus("current")
_InitiatorListEntry_Object = MibTableRow
initiatorListEntry = _InitiatorListEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 3, 1)
)
initiatorListEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "initiatorListEntryIndex"),
)
if mibBuilder.loadTexts:
    initiatorListEntry.setStatus("current")


class _InitiatorListEntryIndex_Type(Integer32):
    """Custom type initiatorListEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InitiatorListEntryIndex_Type.__name__ = "Integer32"
_InitiatorListEntryIndex_Object = MibTableColumn
initiatorListEntryIndex = _InitiatorListEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 3, 1, 1),
    _InitiatorListEntryIndex_Type()
)
initiatorListEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorListEntryIndex.setStatus("current")
_TargetAdapterName_Type = DisplayString
_TargetAdapterName_Object = MibTableColumn
targetAdapterName = _TargetAdapterName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 3, 1, 2),
    _TargetAdapterName_Type()
)
targetAdapterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetAdapterName.setStatus("current")
_ConnectedInitiatorNodeName_Type = DisplayString
_ConnectedInitiatorNodeName_Object = MibTableColumn
connectedInitiatorNodeName = _ConnectedInitiatorNodeName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 3, 1, 3),
    _ConnectedInitiatorNodeName_Type()
)
connectedInitiatorNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedInitiatorNodeName.setStatus("current")
_ConnectedInitiatorPortName_Type = DisplayString
_ConnectedInitiatorPortName_Object = MibTableColumn
connectedInitiatorPortName = _ConnectedInitiatorPortName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 3, 1, 4),
    _ConnectedInitiatorPortName_Type()
)
connectedInitiatorPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedInitiatorPortName.setStatus("current")


class _ConnectedInitiatorType_Type(Integer32):
    """Custom type connectedInitiatorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcp", 1),
          ("iSCSI", 2))
    )


_ConnectedInitiatorType_Type.__name__ = "Integer32"
_ConnectedInitiatorType_Object = MibTableColumn
connectedInitiatorType = _ConnectedInitiatorType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 3, 1, 5),
    _ConnectedInitiatorType_Type()
)
connectedInitiatorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedInitiatorType.setStatus("current")
_ConnectedInitiatorIsid_Type = DisplayString
_ConnectedInitiatorIsid_Object = MibTableColumn
connectedInitiatorIsid = _ConnectedInitiatorIsid_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 3, 1, 6),
    _ConnectedInitiatorIsid_Type()
)
connectedInitiatorIsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedInitiatorIsid.setStatus("current")
_ConnectedInitiatorPortalGroup_Type = Integer32
_ConnectedInitiatorPortalGroup_Object = MibTableColumn
connectedInitiatorPortalGroup = _ConnectedInitiatorPortalGroup_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 16, 3, 1, 7),
    _ConnectedInitiatorPortalGroup_Type()
)
connectedInitiatorPortalGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedInitiatorPortalGroup.setStatus("current")
_FcpTarget_ObjectIdentity = ObjectIdentity
fcpTarget = _FcpTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 17)
)
_FcpTargetTable_Object = MibTable
fcpTargetTable = _FcpTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 17, 1)
)
if mibBuilder.loadTexts:
    fcpTargetTable.setStatus("current")
_FcpTargetTableEntry_Object = MibTableRow
fcpTargetTableEntry = _FcpTargetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 17, 1, 1)
)
fcpTargetTableEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "fcpTargetTableIndex"),
)
if mibBuilder.loadTexts:
    fcpTargetTableEntry.setStatus("current")


class _FcpTargetTableIndex_Type(Integer32):
    """Custom type fcpTargetTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcpTargetTableIndex_Type.__name__ = "Integer32"
_FcpTargetTableIndex_Object = MibTableColumn
fcpTargetTableIndex = _FcpTargetTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 17, 1, 1, 1),
    _FcpTargetTableIndex_Type()
)
fcpTargetTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpTargetTableIndex.setStatus("current")
_FcpTargetName_Type = DisplayString
_FcpTargetName_Object = MibTableColumn
fcpTargetName = _FcpTargetName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 17, 1, 1, 2),
    _FcpTargetName_Type()
)
fcpTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpTargetName.setStatus("current")
_FcpTargetNN_Type = DisplayString
_FcpTargetNN_Object = MibTableColumn
fcpTargetNN = _FcpTargetNN_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 17, 1, 1, 3),
    _FcpTargetNN_Type()
)
fcpTargetNN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpTargetNN.setStatus("current")
_FcpTargetPN_Type = DisplayString
_FcpTargetPN_Object = MibTableColumn
fcpTargetPN = _FcpTargetPN_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 17, 1, 1, 4),
    _FcpTargetPN_Type()
)
fcpTargetPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpTargetPN.setStatus("current")
_FcpTargetSpeed_Type = Integer32
_FcpTargetSpeed_Object = MibTableColumn
fcpTargetSpeed = _FcpTargetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 17, 1, 1, 5),
    _FcpTargetSpeed_Type()
)
fcpTargetSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpTargetSpeed.setStatus("current")


class _FcpTargetStatus_Type(Integer32):
    """Custom type fcpTargetStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("initializingFW", 3),
          ("linkDisconnected", 7),
          ("linkNotConnected", 4),
          ("offline", 9),
          ("offlinedByUserSystem", 10),
          ("online", 6),
          ("resetting", 8),
          ("startup", 1),
          ("uninitialized", 2),
          ("unknown", 11),
          ("waitingForLinkUp", 5))
    )


_FcpTargetStatus_Type.__name__ = "Integer32"
_FcpTargetStatus_Object = MibTableColumn
fcpTargetStatus = _FcpTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 17, 1, 1, 6),
    _FcpTargetStatus_Type()
)
fcpTargetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpTargetStatus.setStatus("current")


class _FcpTargetStandby_Type(Integer32):
    """Custom type fcpTargetStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FcpTargetStandby_Type.__name__ = "Integer32"
_FcpTargetStandby_Object = MibTableColumn
fcpTargetStandby = _FcpTargetStandby_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 17, 1, 1, 7),
    _FcpTargetStandby_Type()
)
fcpTargetStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpTargetStandby.setStatus("current")


class _FcpTargetTopology_Type(Integer32):
    """Custom type fcpTargetTopology based on Integer32"""
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
        *(("fabric", 2),
          ("loop", 4),
          ("pointToPoint", 3),
          ("unknown", 1))
    )


_FcpTargetTopology_Type.__name__ = "Integer32"
_FcpTargetTopology_Object = MibTableColumn
fcpTargetTopology = _FcpTargetTopology_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 17, 1, 1, 8),
    _FcpTargetTopology_Type()
)
fcpTargetTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpTargetTopology.setStatus("current")


class _FcpTargetType_Type(Integer32):
    """Custom type fcpTargetType based on Integer32"""
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
        *(("local", 2),
          ("partner", 4),
          ("physical", 1),
          ("standby", 3),
          ("unknown", 5))
    )


_FcpTargetType_Type.__name__ = "Integer32"
_FcpTargetType_Object = MibTableColumn
fcpTargetType = _FcpTargetType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 17, 1, 1, 9),
    _FcpTargetType_Type()
)
fcpTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpTargetType.setStatus("current")


class _FcpCfMode_Type(Integer32):
    """Custom type fcpCfMode based on Integer32"""
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
              256)
        )
    )
    namedValues = NamedValues(
        *(("dualFabric", 7),
          ("localPrimary", 6),
          ("mixed", 1),
          ("partner", 3),
          ("partnerProxy", 4),
          ("partnerStandby", 5),
          ("ssi", 8),
          ("standby", 2),
          ("unknown", 256))
    )


_FcpCfMode_Type.__name__ = "Integer32"
_FcpCfMode_Object = MibScalar
fcpCfMode = _FcpCfMode_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 18),
    _FcpCfMode_Type()
)
fcpCfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcpCfMode.setStatus("current")
_Pset_ObjectIdentity = ObjectIdentity
pset = _Pset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 19)
)
_PsetTable_Object = MibTable
psetTable = _PsetTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 19, 1)
)
if mibBuilder.loadTexts:
    psetTable.setStatus("current")
_PsetEntry_Object = MibTableRow
psetEntry = _PsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 19, 1, 1)
)
psetEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "psetIndex"),
)
if mibBuilder.loadTexts:
    psetEntry.setStatus("current")


class _PsetIndex_Type(Integer32):
    """Custom type psetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PsetIndex_Type.__name__ = "Integer32"
_PsetIndex_Object = MibTableColumn
psetIndex = _PsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 19, 1, 1, 1),
    _PsetIndex_Type()
)
psetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psetIndex.setStatus("current")
_PsetName_Type = DisplayString
_PsetName_Object = MibTableColumn
psetName = _PsetName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 19, 1, 1, 2),
    _PsetName_Type()
)
psetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psetName.setStatus("current")


class _PsetType_Type(Integer32):
    """Custom type psetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcp", 1),
          ("iSCSI", 2))
    )


_PsetType_Type.__name__ = "Integer32"
_PsetType_Object = MibTableColumn
psetType = _PsetType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 19, 1, 1, 3),
    _PsetType_Type()
)
psetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psetType.setStatus("current")
_PsetMemberTable_Object = MibTable
psetMemberTable = _PsetMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 19, 2)
)
if mibBuilder.loadTexts:
    psetMemberTable.setStatus("current")
_PsetMemberEntry_Object = MibTableRow
psetMemberEntry = _PsetMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 19, 2, 1)
)
psetMemberEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "psetMemberIndex"),
    (0, "NETWORK-APPLIANCE-MIB", "psetMemberNameIndex"),
)
if mibBuilder.loadTexts:
    psetMemberEntry.setStatus("current")


class _PsetMemberIndex_Type(Integer32):
    """Custom type psetMemberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PsetMemberIndex_Type.__name__ = "Integer32"
_PsetMemberIndex_Object = MibTableColumn
psetMemberIndex = _PsetMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 19, 2, 1, 1),
    _PsetMemberIndex_Type()
)
psetMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psetMemberIndex.setStatus("current")


class _PsetMemberNameIndex_Type(Integer32):
    """Custom type psetMemberNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PsetMemberNameIndex_Type.__name__ = "Integer32"
_PsetMemberNameIndex_Object = MibTableColumn
psetMemberNameIndex = _PsetMemberNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 19, 2, 1, 2),
    _PsetMemberNameIndex_Type()
)
psetMemberNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psetMemberNameIndex.setStatus("current")
_PsetPortName_Type = DisplayString
_PsetPortName_Object = MibTableColumn
psetPortName = _PsetPortName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 19, 2, 1, 3),
    _PsetPortName_Type()
)
psetPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psetPortName.setStatus("current")
_Fcp64ReadBytes_Type = Counter64
_Fcp64ReadBytes_Object = MibScalar
fcp64ReadBytes = _Fcp64ReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 20),
    _Fcp64ReadBytes_Type()
)
fcp64ReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcp64ReadBytes.setStatus("current")
_Fcp64WriteBytes_Type = Counter64
_Fcp64WriteBytes_Object = MibScalar
fcp64WriteBytes = _Fcp64WriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 21),
    _Fcp64WriteBytes_Type()
)
fcp64WriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcp64WriteBytes.setStatus("current")
_Iscsi64ReadBytes_Type = Counter64
_Iscsi64ReadBytes_Object = MibScalar
iscsi64ReadBytes = _Iscsi64ReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 22),
    _Iscsi64ReadBytes_Type()
)
iscsi64ReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi64ReadBytes.setStatus("current")
_Iscsi64WriteBytes_Type = Counter64
_Iscsi64WriteBytes_Object = MibScalar
iscsi64WriteBytes = _Iscsi64WriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 23),
    _Iscsi64WriteBytes_Type()
)
iscsi64WriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi64WriteBytes.setStatus("current")
_Iscsi64Ops_Type = Counter64
_Iscsi64Ops_Object = MibScalar
iscsi64Ops = _Iscsi64Ops_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 24),
    _Iscsi64Ops_Type()
)
iscsi64Ops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi64Ops.setStatus("current")
_Fcp64Ops_Type = Counter64
_Fcp64Ops_Object = MibScalar
fcp64Ops = _Fcp64Ops_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 17, 25),
    _Fcp64Ops_Type()
)
fcp64Ops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcp64Ops.setStatus("current")
_Nfscache_ObjectIdentity = ObjectIdentity
nfscache = _Nfscache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 18)
)
_NfsCacheOptions_ObjectIdentity = ObjectIdentity
nfsCacheOptions = _NfsCacheOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 1)
)


class _NfsCacheIsEnabled_Type(Integer32):
    """Custom type nfsCacheIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NfsCacheIsEnabled_Type.__name__ = "Integer32"
_NfsCacheIsEnabled_Object = MibScalar
nfsCacheIsEnabled = _NfsCacheIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 1, 1),
    _NfsCacheIsEnabled_Type()
)
nfsCacheIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheIsEnabled.setStatus("current")


class _NfsCacheIsLicensed_Type(Integer32):
    """Custom type nfsCacheIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NfsCacheIsLicensed_Type.__name__ = "Integer32"
_NfsCacheIsLicensed_Object = MibScalar
nfsCacheIsLicensed = _NfsCacheIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 1, 2),
    _NfsCacheIsLicensed_Type()
)
nfsCacheIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheIsLicensed.setStatus("current")
_NfsCacheStats_ObjectIdentity = ObjectIdentity
nfsCacheStats = _NfsCacheStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2)
)
_NfsCacheBytesFromClients_Type = Counter32
_NfsCacheBytesFromClients_Object = MibScalar
nfsCacheBytesFromClients = _NfsCacheBytesFromClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 1),
    _NfsCacheBytesFromClients_Type()
)
nfsCacheBytesFromClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheBytesFromClients.setStatus("deprecated")
_NfsCacheBytesToClients_Type = Counter32
_NfsCacheBytesToClients_Object = MibScalar
nfsCacheBytesToClients = _NfsCacheBytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 2),
    _NfsCacheBytesToClients_Type()
)
nfsCacheBytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheBytesToClients.setStatus("deprecated")
_NfsCacheBytesFromServers_Type = Counter32
_NfsCacheBytesFromServers_Object = MibScalar
nfsCacheBytesFromServers = _NfsCacheBytesFromServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 3),
    _NfsCacheBytesFromServers_Type()
)
nfsCacheBytesFromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheBytesFromServers.setStatus("deprecated")
_NfsCacheBytesToServers_Type = Counter32
_NfsCacheBytesToServers_Object = MibScalar
nfsCacheBytesToServers = _NfsCacheBytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 4),
    _NfsCacheBytesToServers_Type()
)
nfsCacheBytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheBytesToServers.setStatus("deprecated")
_NfsCacheTotalRequests_Type = Counter32
_NfsCacheTotalRequests_Object = MibScalar
nfsCacheTotalRequests = _NfsCacheTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 5),
    _NfsCacheTotalRequests_Type()
)
nfsCacheTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheTotalRequests.setStatus("deprecated")
_NfsCacheHitRequests_Type = Counter32
_NfsCacheHitRequests_Object = MibScalar
nfsCacheHitRequests = _NfsCacheHitRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 6),
    _NfsCacheHitRequests_Type()
)
nfsCacheHitRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheHitRequests.setStatus("deprecated")
_NfsCacheMissRequests_Type = Counter32
_NfsCacheMissRequests_Object = MibScalar
nfsCacheMissRequests = _NfsCacheMissRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 7),
    _NfsCacheMissRequests_Type()
)
nfsCacheMissRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheMissRequests.setStatus("deprecated")
_NfsCacheMissCacheableRequests_Type = Counter32
_NfsCacheMissCacheableRequests_Object = MibScalar
nfsCacheMissCacheableRequests = _NfsCacheMissCacheableRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 8),
    _NfsCacheMissCacheableRequests_Type()
)
nfsCacheMissCacheableRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheMissCacheableRequests.setStatus("current")
_NfsCacheMissUnCacheableRequests_Type = Counter32
_NfsCacheMissUnCacheableRequests_Object = MibScalar
nfsCacheMissUnCacheableRequests = _NfsCacheMissUnCacheableRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 9),
    _NfsCacheMissUnCacheableRequests_Type()
)
nfsCacheMissUnCacheableRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheMissUnCacheableRequests.setStatus("current")
_NfsCacheEjectRequests_Type = Counter32
_NfsCacheEjectRequests_Object = MibScalar
nfsCacheEjectRequests = _NfsCacheEjectRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 10),
    _NfsCacheEjectRequests_Type()
)
nfsCacheEjectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheEjectRequests.setStatus("current")
_NfsCacheVerifyRequests_Type = Counter32
_NfsCacheVerifyRequests_Object = MibScalar
nfsCacheVerifyRequests = _NfsCacheVerifyRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 11),
    _NfsCacheVerifyRequests_Type()
)
nfsCacheVerifyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheVerifyRequests.setStatus("current")
_NfsCacheRpcRecords_Type = Counter32
_NfsCacheRpcRecords_Object = MibScalar
nfsCacheRpcRecords = _NfsCacheRpcRecords_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 12),
    _NfsCacheRpcRecords_Type()
)
nfsCacheRpcRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheRpcRecords.setStatus("current")
_NfsCacheBWSavings_Type = Integer32
_NfsCacheBWSavings_Object = MibScalar
nfsCacheBWSavings = _NfsCacheBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 13),
    _NfsCacheBWSavings_Type()
)
nfsCacheBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheBWSavings.setStatus("current")
_NfsCacheHighBytesFromClients_Type = Counter32
_NfsCacheHighBytesFromClients_Object = MibScalar
nfsCacheHighBytesFromClients = _NfsCacheHighBytesFromClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 14),
    _NfsCacheHighBytesFromClients_Type()
)
nfsCacheHighBytesFromClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheHighBytesFromClients.setStatus("current")
_NfsCacheLowBytesFromClients_Type = Counter32
_NfsCacheLowBytesFromClients_Object = MibScalar
nfsCacheLowBytesFromClients = _NfsCacheLowBytesFromClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 15),
    _NfsCacheLowBytesFromClients_Type()
)
nfsCacheLowBytesFromClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheLowBytesFromClients.setStatus("current")
_NfsCacheHighBytesToClients_Type = Counter32
_NfsCacheHighBytesToClients_Object = MibScalar
nfsCacheHighBytesToClients = _NfsCacheHighBytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 16),
    _NfsCacheHighBytesToClients_Type()
)
nfsCacheHighBytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheHighBytesToClients.setStatus("current")
_NfsCacheLowBytesToClients_Type = Counter32
_NfsCacheLowBytesToClients_Object = MibScalar
nfsCacheLowBytesToClients = _NfsCacheLowBytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 17),
    _NfsCacheLowBytesToClients_Type()
)
nfsCacheLowBytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheLowBytesToClients.setStatus("current")
_NfsCacheHighBytesFromServers_Type = Counter32
_NfsCacheHighBytesFromServers_Object = MibScalar
nfsCacheHighBytesFromServers = _NfsCacheHighBytesFromServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 18),
    _NfsCacheHighBytesFromServers_Type()
)
nfsCacheHighBytesFromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheHighBytesFromServers.setStatus("current")
_NfsCacheLowBytesFromServers_Type = Counter32
_NfsCacheLowBytesFromServers_Object = MibScalar
nfsCacheLowBytesFromServers = _NfsCacheLowBytesFromServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 19),
    _NfsCacheLowBytesFromServers_Type()
)
nfsCacheLowBytesFromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheLowBytesFromServers.setStatus("current")
_NfsCacheHighBytesToServers_Type = Counter32
_NfsCacheHighBytesToServers_Object = MibScalar
nfsCacheHighBytesToServers = _NfsCacheHighBytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 20),
    _NfsCacheHighBytesToServers_Type()
)
nfsCacheHighBytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheHighBytesToServers.setStatus("current")
_NfsCacheLowBytesToServers_Type = Counter32
_NfsCacheLowBytesToServers_Object = MibScalar
nfsCacheLowBytesToServers = _NfsCacheLowBytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 21),
    _NfsCacheLowBytesToServers_Type()
)
nfsCacheLowBytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheLowBytesToServers.setStatus("current")
_NfsCacheHighTotalRequests_Type = Counter32
_NfsCacheHighTotalRequests_Object = MibScalar
nfsCacheHighTotalRequests = _NfsCacheHighTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 22),
    _NfsCacheHighTotalRequests_Type()
)
nfsCacheHighTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheHighTotalRequests.setStatus("current")
_NfsCacheLowTotalRequests_Type = Counter32
_NfsCacheLowTotalRequests_Object = MibScalar
nfsCacheLowTotalRequests = _NfsCacheLowTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 23),
    _NfsCacheLowTotalRequests_Type()
)
nfsCacheLowTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheLowTotalRequests.setStatus("current")
_NfsCacheHighHitRequests_Type = Counter32
_NfsCacheHighHitRequests_Object = MibScalar
nfsCacheHighHitRequests = _NfsCacheHighHitRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 24),
    _NfsCacheHighHitRequests_Type()
)
nfsCacheHighHitRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheHighHitRequests.setStatus("current")
_NfsCacheLowHitRequests_Type = Counter32
_NfsCacheLowHitRequests_Object = MibScalar
nfsCacheLowHitRequests = _NfsCacheLowHitRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 25),
    _NfsCacheLowHitRequests_Type()
)
nfsCacheLowHitRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheLowHitRequests.setStatus("current")
_NfsCacheHighMissRequests_Type = Counter32
_NfsCacheHighMissRequests_Object = MibScalar
nfsCacheHighMissRequests = _NfsCacheHighMissRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 26),
    _NfsCacheHighMissRequests_Type()
)
nfsCacheHighMissRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheHighMissRequests.setStatus("current")
_NfsCacheLowMissRequests_Type = Counter32
_NfsCacheLowMissRequests_Object = MibScalar
nfsCacheLowMissRequests = _NfsCacheLowMissRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 27),
    _NfsCacheLowMissRequests_Type()
)
nfsCacheLowMissRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCacheLowMissRequests.setStatus("current")
_NfsCache64BytesFromClients_Type = Counter64
_NfsCache64BytesFromClients_Object = MibScalar
nfsCache64BytesFromClients = _NfsCache64BytesFromClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 28),
    _NfsCache64BytesFromClients_Type()
)
nfsCache64BytesFromClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCache64BytesFromClients.setStatus("current")
_NfsCache64BytesToClients_Type = Counter64
_NfsCache64BytesToClients_Object = MibScalar
nfsCache64BytesToClients = _NfsCache64BytesToClients_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 29),
    _NfsCache64BytesToClients_Type()
)
nfsCache64BytesToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCache64BytesToClients.setStatus("current")
_NfsCache64BytesFromServers_Type = Counter64
_NfsCache64BytesFromServers_Object = MibScalar
nfsCache64BytesFromServers = _NfsCache64BytesFromServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 30),
    _NfsCache64BytesFromServers_Type()
)
nfsCache64BytesFromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCache64BytesFromServers.setStatus("current")
_NfsCache64BytesToServers_Type = Counter64
_NfsCache64BytesToServers_Object = MibScalar
nfsCache64BytesToServers = _NfsCache64BytesToServers_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 31),
    _NfsCache64BytesToServers_Type()
)
nfsCache64BytesToServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCache64BytesToServers.setStatus("current")
_NfsCache64TotalRequests_Type = Counter64
_NfsCache64TotalRequests_Object = MibScalar
nfsCache64TotalRequests = _NfsCache64TotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 32),
    _NfsCache64TotalRequests_Type()
)
nfsCache64TotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCache64TotalRequests.setStatus("current")
_NfsCache64HitRequests_Type = Counter64
_NfsCache64HitRequests_Object = MibScalar
nfsCache64HitRequests = _NfsCache64HitRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 33),
    _NfsCache64HitRequests_Type()
)
nfsCache64HitRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCache64HitRequests.setStatus("current")
_NfsCache64MissRequests_Type = Counter64
_NfsCache64MissRequests_Object = MibScalar
nfsCache64MissRequests = _NfsCache64MissRequests_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 18, 2, 34),
    _NfsCache64MissRequests_Type()
)
nfsCache64MissRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsCache64MissRequests.setStatus("current")
_Snapvault_ObjectIdentity = ObjectIdentity
snapvault = _Snapvault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 19)
)


class _SvOn_Type(Integer32):
    """Custom type svOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SvOn_Type.__name__ = "Integer32"
_SvOn_Object = MibScalar
svOn = _SvOn_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 1),
    _SvOn_Type()
)
svOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svOn.setStatus("current")
_SvSystemActiveDstNumber_Type = Integer32
_SvSystemActiveDstNumber_Object = MibScalar
svSystemActiveDstNumber = _SvSystemActiveDstNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 2),
    _SvSystemActiveDstNumber_Type()
)
svSystemActiveDstNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSystemActiveDstNumber.setStatus("current")
_SvSystemActiveSrcNumber_Type = Integer32
_SvSystemActiveSrcNumber_Object = MibScalar
svSystemActiveSrcNumber = _SvSystemActiveSrcNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 3),
    _SvSystemActiveSrcNumber_Type()
)
svSystemActiveSrcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSystemActiveSrcNumber.setStatus("current")
_SvSystemTotalPrimarySuccesses_Type = Counter32
_SvSystemTotalPrimarySuccesses_Object = MibScalar
svSystemTotalPrimarySuccesses = _SvSystemTotalPrimarySuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 4),
    _SvSystemTotalPrimarySuccesses_Type()
)
svSystemTotalPrimarySuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSystemTotalPrimarySuccesses.setStatus("current")
_SvSystemTotalSecondarySuccesses_Type = Counter32
_SvSystemTotalSecondarySuccesses_Object = MibScalar
svSystemTotalSecondarySuccesses = _SvSystemTotalSecondarySuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 5),
    _SvSystemTotalSecondarySuccesses_Type()
)
svSystemTotalSecondarySuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSystemTotalSecondarySuccesses.setStatus("current")
_SvSystemTotalPrimaryFailures_Type = Counter32
_SvSystemTotalPrimaryFailures_Object = MibScalar
svSystemTotalPrimaryFailures = _SvSystemTotalPrimaryFailures_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 6),
    _SvSystemTotalPrimaryFailures_Type()
)
svSystemTotalPrimaryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSystemTotalPrimaryFailures.setStatus("current")
_SvSystemTotalSecondaryFailures_Type = Counter32
_SvSystemTotalSecondaryFailures_Object = MibScalar
svSystemTotalSecondaryFailures = _SvSystemTotalSecondaryFailures_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 7),
    _SvSystemTotalSecondaryFailures_Type()
)
svSystemTotalSecondaryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSystemTotalSecondaryFailures.setStatus("current")
_SvSystemTotalSecondaryDeferments_Type = Counter32
_SvSystemTotalSecondaryDeferments_Object = MibScalar
svSystemTotalSecondaryDeferments = _SvSystemTotalSecondaryDeferments_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 8),
    _SvSystemTotalSecondaryDeferments_Type()
)
svSystemTotalSecondaryDeferments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSystemTotalSecondaryDeferments.setStatus("current")


class _SvPrimaryIsLicensed_Type(Integer32):
    """Custom type svPrimaryIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SvPrimaryIsLicensed_Type.__name__ = "Integer32"
_SvPrimaryIsLicensed_Object = MibScalar
svPrimaryIsLicensed = _SvPrimaryIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 9),
    _SvPrimaryIsLicensed_Type()
)
svPrimaryIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svPrimaryIsLicensed.setStatus("current")


class _SvSecondaryIsLicensed_Type(Integer32):
    """Custom type svSecondaryIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SvSecondaryIsLicensed_Type.__name__ = "Integer32"
_SvSecondaryIsLicensed_Object = MibScalar
svSecondaryIsLicensed = _SvSecondaryIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 10),
    _SvSecondaryIsLicensed_Type()
)
svSecondaryIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSecondaryIsLicensed.setStatus("current")
_SnapvaultStatusTable_Object = MibTable
snapvaultStatusTable = _SnapvaultStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11)
)
if mibBuilder.loadTexts:
    snapvaultStatusTable.setStatus("current")
_SnapvaultStatusEntry_Object = MibTableRow
snapvaultStatusEntry = _SnapvaultStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1)
)
snapvaultStatusEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "svIndex"),
)
if mibBuilder.loadTexts:
    snapvaultStatusEntry.setStatus("current")


class _SvIndex_Type(Integer32):
    """Custom type svIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SvIndex_Type.__name__ = "Integer32"
_SvIndex_Object = MibTableColumn
svIndex = _SvIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 1),
    _SvIndex_Type()
)
svIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svIndex.setStatus("current")
_SvSrc_Type = OctetString
_SvSrc_Object = MibTableColumn
svSrc = _SvSrc_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 2),
    _SvSrc_Type()
)
svSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSrc.setStatus("current")
_SvDst_Type = OctetString
_SvDst_Object = MibTableColumn
svDst = _SvDst_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 3),
    _SvDst_Type()
)
svDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svDst.setStatus("current")


class _SvStatus_Type(Integer32):
    """Custom type svStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              12)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 4),
          ("idle", 1),
          ("paused", 12),
          ("pending", 3),
          ("quiescing", 6),
          ("resyncing", 7),
          ("transferring", 2))
    )


_SvStatus_Type.__name__ = "Integer32"
_SvStatus_Object = MibTableColumn
svStatus = _SvStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 4),
    _SvStatus_Type()
)
svStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svStatus.setStatus("current")


class _SvState_Type(Integer32):
    """Custom type svState based on Integer32"""
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
        *(("brokenOff", 3),
          ("quiesced", 4),
          ("restoring", 7),
          ("snapvaulted", 2),
          ("source", 5),
          ("uninitialized", 1),
          ("unknown", 6))
    )


_SvState_Type.__name__ = "Integer32"
_SvState_Object = MibTableColumn
svState = _SvState_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 5),
    _SvState_Type()
)
svState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svState.setStatus("current")
_SvLag_Type = TimeTicks
_SvLag_Object = MibTableColumn
svLag = _SvLag_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 6),
    _SvLag_Type()
)
svLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svLag.setStatus("current")
_SvTotalSuccesses_Type = Counter32
_SvTotalSuccesses_Object = MibTableColumn
svTotalSuccesses = _SvTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 7),
    _SvTotalSuccesses_Type()
)
svTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTotalSuccesses.setStatus("current")
_SvTotalRestartSuccesses_Type = Counter32
_SvTotalRestartSuccesses_Object = MibTableColumn
svTotalRestartSuccesses = _SvTotalRestartSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 8),
    _SvTotalRestartSuccesses_Type()
)
svTotalRestartSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTotalRestartSuccesses.setStatus("current")
_SvTotalFailures_Type = Counter32
_SvTotalFailures_Object = MibTableColumn
svTotalFailures = _SvTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 9),
    _SvTotalFailures_Type()
)
svTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTotalFailures.setStatus("current")
_SvTotalDeferments_Type = Counter32
_SvTotalDeferments_Object = MibTableColumn
svTotalDeferments = _SvTotalDeferments_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 10),
    _SvTotalDeferments_Type()
)
svTotalDeferments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTotalDeferments.setStatus("current")
_SvTotalTransMBs_Type = Counter32
_SvTotalTransMBs_Object = MibTableColumn
svTotalTransMBs = _SvTotalTransMBs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 11),
    _SvTotalTransMBs_Type()
)
svTotalTransMBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTotalTransMBs.setStatus("current")
_SvTotalTransTimeSeconds_Type = Counter32
_SvTotalTransTimeSeconds_Object = MibTableColumn
svTotalTransTimeSeconds = _SvTotalTransTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 12),
    _SvTotalTransTimeSeconds_Type()
)
svTotalTransTimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svTotalTransTimeSeconds.setStatus("current")
_SvThrottleValue_Type = Integer32
_SvThrottleValue_Object = MibTableColumn
svThrottleValue = _SvThrottleValue_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 13),
    _SvThrottleValue_Type()
)
svThrottleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svThrottleValue.setStatus("current")
_SvSrcSnapshotTime_Type = Integer32
_SvSrcSnapshotTime_Object = MibTableColumn
svSrcSnapshotTime = _SvSrcSnapshotTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 14),
    _SvSrcSnapshotTime_Type()
)
svSrcSnapshotTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSrcSnapshotTime.setStatus("current")
_SvBaseSnapshot_Type = DisplayString
_SvBaseSnapshot_Object = MibTableColumn
svBaseSnapshot = _SvBaseSnapshot_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 15),
    _SvBaseSnapshot_Type()
)
svBaseSnapshot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svBaseSnapshot.setStatus("current")
_SvLastTransType_Type = DisplayString
_SvLastTransType_Object = MibTableColumn
svLastTransType = _SvLastTransType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 16),
    _SvLastTransType_Type()
)
svLastTransType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svLastTransType.setStatus("current")
_SvLastTransMBs_Type = Integer32
_SvLastTransMBs_Object = MibTableColumn
svLastTransMBs = _SvLastTransMBs_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 17),
    _SvLastTransMBs_Type()
)
svLastTransMBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svLastTransMBs.setStatus("current")
_SvLastTransTimeSeconds_Type = Integer32
_SvLastTransTimeSeconds_Object = MibTableColumn
svLastTransTimeSeconds = _SvLastTransTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 11, 1, 18),
    _SvLastTransTimeSeconds_Type()
)
svLastTransTimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svLastTransTimeSeconds.setStatus("current")
_SnapvaultHostTable_Object = MibTable
snapvaultHostTable = _SnapvaultHostTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 12)
)
if mibBuilder.loadTexts:
    snapvaultHostTable.setStatus("current")
_SnapvaultHostEntry_Object = MibTableRow
snapvaultHostEntry = _SnapvaultHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 12, 1)
)
snapvaultHostEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "svHostIndex"),
)
if mibBuilder.loadTexts:
    snapvaultHostEntry.setStatus("current")


class _SvHostIndex_Type(Integer32):
    """Custom type svHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SvHostIndex_Type.__name__ = "Integer32"
_SvHostIndex_Object = MibTableColumn
svHostIndex = _SvHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 12, 1, 1),
    _SvHostIndex_Type()
)
svHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svHostIndex.setStatus("current")
_SvHostName_Type = DisplayString
_SvHostName_Object = MibTableColumn
svHostName = _SvHostName_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 12, 1, 2),
    _SvHostName_Type()
)
svHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svHostName.setStatus("current")


class _SvHostType_Type(Integer32):
    """Custom type svHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SvHostType_Type.__name__ = "Integer32"
_SvHostType_Object = MibTableColumn
svHostType = _SvHostType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 12, 1, 3),
    _SvHostType_Type()
)
svHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svHostType.setStatus("current")
_SvHostTotalSuccesses_Type = Integer32
_SvHostTotalSuccesses_Object = MibTableColumn
svHostTotalSuccesses = _SvHostTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 12, 1, 4),
    _SvHostTotalSuccesses_Type()
)
svHostTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svHostTotalSuccesses.setStatus("current")
_SvHostTotalFailures_Type = Integer32
_SvHostTotalFailures_Object = MibTableColumn
svHostTotalFailures = _SvHostTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 12, 1, 5),
    _SvHostTotalFailures_Type()
)
svHostTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svHostTotalFailures.setStatus("current")
_SvHostTotalDeferments_Type = Integer32
_SvHostTotalDeferments_Object = MibTableColumn
svHostTotalDeferments = _SvHostTotalDeferments_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 12, 1, 6),
    _SvHostTotalDeferments_Type()
)
svHostTotalDeferments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svHostTotalDeferments.setStatus("current")
_SnapvaultSchedTable_Object = MibTable
snapvaultSchedTable = _SnapvaultSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 13)
)
if mibBuilder.loadTexts:
    snapvaultSchedTable.setStatus("current")
_SnapvaultSchedEntry_Object = MibTableRow
snapvaultSchedEntry = _SnapvaultSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 13, 1)
)
snapvaultSchedEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "svSchedIndex"),
)
if mibBuilder.loadTexts:
    snapvaultSchedEntry.setStatus("current")


class _SvSchedIndex_Type(Integer32):
    """Custom type svSchedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SvSchedIndex_Type.__name__ = "Integer32"
_SvSchedIndex_Object = MibTableColumn
svSchedIndex = _SvSchedIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 13, 1, 1),
    _SvSchedIndex_Type()
)
svSchedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSchedIndex.setStatus("current")
_SvSchedVolume_Type = DisplayString
_SvSchedVolume_Object = MibTableColumn
svSchedVolume = _SvSchedVolume_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 13, 1, 2),
    _SvSchedVolume_Type()
)
svSchedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSchedVolume.setStatus("current")
_SvSchedSnapshot_Type = DisplayString
_SvSchedSnapshot_Object = MibTableColumn
svSchedSnapshot = _SvSchedSnapshot_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 13, 1, 3),
    _SvSchedSnapshot_Type()
)
svSchedSnapshot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSchedSnapshot.setStatus("current")


class _SvSchedStatus_Type(Integer32):
    """Custom type svSchedStatus based on Integer32"""
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
        *(("aborting", 4),
          ("active", 3),
          ("idle", 1),
          ("queued", 2))
    )


_SvSchedStatus_Type.__name__ = "Integer32"
_SvSchedStatus_Object = MibTableColumn
svSchedStatus = _SvSchedStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 13, 1, 4),
    _SvSchedStatus_Type()
)
svSchedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSchedStatus.setStatus("current")


class _SvSchedType_Type(Integer32):
    """Custom type svSchedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 3),
          ("undef", 1),
          ("xfer", 2))
    )


_SvSchedType_Type.__name__ = "Integer32"
_SvSchedType_Object = MibTableColumn
svSchedType = _SvSchedType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 13, 1, 5),
    _SvSchedType_Type()
)
svSchedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSchedType.setStatus("current")
_SvSchedSchedule_Type = DisplayString
_SvSchedSchedule_Object = MibTableColumn
svSchedSchedule = _SvSchedSchedule_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 13, 1, 6),
    _SvSchedSchedule_Type()
)
svSchedSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svSchedSchedule.setStatus("current")


class _SvDrPrimaryIsLicensed_Type(Integer32):
    """Custom type svDrPrimaryIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SvDrPrimaryIsLicensed_Type.__name__ = "Integer32"
_SvDrPrimaryIsLicensed_Object = MibScalar
svDrPrimaryIsLicensed = _SvDrPrimaryIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 19, 14),
    _SvDrPrimaryIsLicensed_Type()
)
svDrPrimaryIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svDrPrimaryIsLicensed.setStatus("current")
_Ftpd_ObjectIdentity = ObjectIdentity
ftpd = _Ftpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 20)
)


class _FtpdOn_Type(Integer32):
    """Custom type ftpdOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FtpdOn_Type.__name__ = "Integer32"
_FtpdOn_Object = MibScalar
ftpdOn = _FtpdOn_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 20, 1),
    _FtpdOn_Type()
)
ftpdOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpdOn.setStatus("current")
_FtpdCurrentConns_Type = Integer32
_FtpdCurrentConns_Object = MibScalar
ftpdCurrentConns = _FtpdCurrentConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 20, 2),
    _FtpdCurrentConns_Type()
)
ftpdCurrentConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpdCurrentConns.setStatus("current")
_FtpdMaxConns_Type = Integer32
_FtpdMaxConns_Object = MibScalar
ftpdMaxConns = _FtpdMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 20, 3),
    _FtpdMaxConns_Type()
)
ftpdMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpdMaxConns.setStatus("current")
_FtpdTotalConns_Type = Integer32
_FtpdTotalConns_Object = MibScalar
ftpdTotalConns = _FtpdTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 20, 4),
    _FtpdTotalConns_Type()
)
ftpdTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpdTotalConns.setStatus("current")
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 21)
)
_Enclosure_ObjectIdentity = ObjectIdentity
enclosure = _Enclosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1)
)
_EnclNumber_Type = Integer32
_EnclNumber_Object = MibScalar
enclNumber = _EnclNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 1),
    _EnclNumber_Type()
)
enclNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclNumber.setStatus("current")
_EnclTable_Object = MibTable
enclTable = _EnclTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2)
)
if mibBuilder.loadTexts:
    enclTable.setStatus("current")
_EnclEntry_Object = MibTableRow
enclEntry = _EnclEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1)
)
enclEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "enclIndex"),
)
if mibBuilder.loadTexts:
    enclEntry.setStatus("current")


class _EnclIndex_Type(Integer32):
    """Custom type enclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnclIndex_Type.__name__ = "Integer32"
_EnclIndex_Object = MibTableColumn
enclIndex = _EnclIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 1),
    _EnclIndex_Type()
)
enclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclIndex.setStatus("current")


class _EnclContactState_Type(Integer32):
    """Custom type enclContactState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 4),
          ("initializing", 1),
          ("nonexistent", 6),
          ("reconfiguring", 5),
          ("transitioning", 2))
    )


_EnclContactState_Type.__name__ = "Integer32"
_EnclContactState_Object = MibTableColumn
enclContactState = _EnclContactState_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 2),
    _EnclContactState_Type()
)
enclContactState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclContactState.setStatus("current")
_EnclChannelShelfAddr_Type = DisplayString
_EnclChannelShelfAddr_Object = MibTableColumn
enclChannelShelfAddr = _EnclChannelShelfAddr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 3),
    _EnclChannelShelfAddr_Type()
)
enclChannelShelfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclChannelShelfAddr.setStatus("current")
_EnclProductLogicalID_Type = DisplayString
_EnclProductLogicalID_Object = MibTableColumn
enclProductLogicalID = _EnclProductLogicalID_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 4),
    _EnclProductLogicalID_Type()
)
enclProductLogicalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclProductLogicalID.setStatus("current")
_EnclProductID_Type = DisplayString
_EnclProductID_Object = MibTableColumn
enclProductID = _EnclProductID_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 5),
    _EnclProductID_Type()
)
enclProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclProductID.setStatus("current")
_EnclProductVendor_Type = DisplayString
_EnclProductVendor_Object = MibTableColumn
enclProductVendor = _EnclProductVendor_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 6),
    _EnclProductVendor_Type()
)
enclProductVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclProductVendor.setStatus("current")
_EnclProductModel_Type = DisplayString
_EnclProductModel_Object = MibTableColumn
enclProductModel = _EnclProductModel_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 7),
    _EnclProductModel_Type()
)
enclProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclProductModel.setStatus("current")
_EnclProductRevision_Type = DisplayString
_EnclProductRevision_Object = MibTableColumn
enclProductRevision = _EnclProductRevision_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 8),
    _EnclProductRevision_Type()
)
enclProductRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclProductRevision.setStatus("current")
_EnclProductSerialNo_Type = DisplayString
_EnclProductSerialNo_Object = MibTableColumn
enclProductSerialNo = _EnclProductSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 9),
    _EnclProductSerialNo_Type()
)
enclProductSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclProductSerialNo.setStatus("current")
_EnclNumberDiskBays_Type = Integer32
_EnclNumberDiskBays_Object = MibTableColumn
enclNumberDiskBays = _EnclNumberDiskBays_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 10),
    _EnclNumberDiskBays_Type()
)
enclNumberDiskBays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclNumberDiskBays.setStatus("current")
_EnclDisksPresent_Type = DisplayString
_EnclDisksPresent_Object = MibTableColumn
enclDisksPresent = _EnclDisksPresent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 11),
    _EnclDisksPresent_Type()
)
enclDisksPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclDisksPresent.setStatus("current")
_EnclPowerSuppliesMaximum_Type = Integer32
_EnclPowerSuppliesMaximum_Object = MibTableColumn
enclPowerSuppliesMaximum = _EnclPowerSuppliesMaximum_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 12),
    _EnclPowerSuppliesMaximum_Type()
)
enclPowerSuppliesMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclPowerSuppliesMaximum.setStatus("current")
_EnclPowerSuppliesPresent_Type = DisplayString
_EnclPowerSuppliesPresent_Object = MibTableColumn
enclPowerSuppliesPresent = _EnclPowerSuppliesPresent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 13),
    _EnclPowerSuppliesPresent_Type()
)
enclPowerSuppliesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclPowerSuppliesPresent.setStatus("current")
_EnclPowerSuppliesSerialNos_Type = DisplayString
_EnclPowerSuppliesSerialNos_Object = MibTableColumn
enclPowerSuppliesSerialNos = _EnclPowerSuppliesSerialNos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 14),
    _EnclPowerSuppliesSerialNos_Type()
)
enclPowerSuppliesSerialNos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclPowerSuppliesSerialNos.setStatus("current")
_EnclPowerSuppliesFailed_Type = DisplayString
_EnclPowerSuppliesFailed_Object = MibTableColumn
enclPowerSuppliesFailed = _EnclPowerSuppliesFailed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 15),
    _EnclPowerSuppliesFailed_Type()
)
enclPowerSuppliesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclPowerSuppliesFailed.setStatus("current")
_EnclFansMaximum_Type = Integer32
_EnclFansMaximum_Object = MibTableColumn
enclFansMaximum = _EnclFansMaximum_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 16),
    _EnclFansMaximum_Type()
)
enclFansMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclFansMaximum.setStatus("current")
_EnclFansPresent_Type = DisplayString
_EnclFansPresent_Object = MibTableColumn
enclFansPresent = _EnclFansPresent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 17),
    _EnclFansPresent_Type()
)
enclFansPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclFansPresent.setStatus("current")
_EnclFansFailed_Type = DisplayString
_EnclFansFailed_Object = MibTableColumn
enclFansFailed = _EnclFansFailed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 18),
    _EnclFansFailed_Type()
)
enclFansFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclFansFailed.setStatus("current")
_EnclTempSensorsMaximum_Type = Integer32
_EnclTempSensorsMaximum_Object = MibTableColumn
enclTempSensorsMaximum = _EnclTempSensorsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 19),
    _EnclTempSensorsMaximum_Type()
)
enclTempSensorsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTempSensorsMaximum.setStatus("current")
_EnclTempSensorsPresent_Type = DisplayString
_EnclTempSensorsPresent_Object = MibTableColumn
enclTempSensorsPresent = _EnclTempSensorsPresent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 20),
    _EnclTempSensorsPresent_Type()
)
enclTempSensorsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTempSensorsPresent.setStatus("current")
_EnclTempSensorsOverTempFail_Type = DisplayString
_EnclTempSensorsOverTempFail_Object = MibTableColumn
enclTempSensorsOverTempFail = _EnclTempSensorsOverTempFail_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 21),
    _EnclTempSensorsOverTempFail_Type()
)
enclTempSensorsOverTempFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTempSensorsOverTempFail.setStatus("current")
_EnclTempSensorsOverTempWarn_Type = DisplayString
_EnclTempSensorsOverTempWarn_Object = MibTableColumn
enclTempSensorsOverTempWarn = _EnclTempSensorsOverTempWarn_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 22),
    _EnclTempSensorsOverTempWarn_Type()
)
enclTempSensorsOverTempWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTempSensorsOverTempWarn.setStatus("current")
_EnclTempSensorsUnderTempFail_Type = DisplayString
_EnclTempSensorsUnderTempFail_Object = MibTableColumn
enclTempSensorsUnderTempFail = _EnclTempSensorsUnderTempFail_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 23),
    _EnclTempSensorsUnderTempFail_Type()
)
enclTempSensorsUnderTempFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTempSensorsUnderTempFail.setStatus("current")
_EnclTempSensorsUnderTempWarn_Type = DisplayString
_EnclTempSensorsUnderTempWarn_Object = MibTableColumn
enclTempSensorsUnderTempWarn = _EnclTempSensorsUnderTempWarn_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 24),
    _EnclTempSensorsUnderTempWarn_Type()
)
enclTempSensorsUnderTempWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTempSensorsUnderTempWarn.setStatus("current")
_EnclTempSensorsCurrentTemp_Type = DisplayString
_EnclTempSensorsCurrentTemp_Object = MibTableColumn
enclTempSensorsCurrentTemp = _EnclTempSensorsCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 25),
    _EnclTempSensorsCurrentTemp_Type()
)
enclTempSensorsCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTempSensorsCurrentTemp.setStatus("current")
_EnclTempSensorsOverTempFailThr_Type = DisplayString
_EnclTempSensorsOverTempFailThr_Object = MibTableColumn
enclTempSensorsOverTempFailThr = _EnclTempSensorsOverTempFailThr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 26),
    _EnclTempSensorsOverTempFailThr_Type()
)
enclTempSensorsOverTempFailThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTempSensorsOverTempFailThr.setStatus("current")
_EnclTempSensorsOverTempWarnThr_Type = DisplayString
_EnclTempSensorsOverTempWarnThr_Object = MibTableColumn
enclTempSensorsOverTempWarnThr = _EnclTempSensorsOverTempWarnThr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 27),
    _EnclTempSensorsOverTempWarnThr_Type()
)
enclTempSensorsOverTempWarnThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTempSensorsOverTempWarnThr.setStatus("current")
_EnclTempSensorsUnderTempFailThr_Type = DisplayString
_EnclTempSensorsUnderTempFailThr_Object = MibTableColumn
enclTempSensorsUnderTempFailThr = _EnclTempSensorsUnderTempFailThr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 28),
    _EnclTempSensorsUnderTempFailThr_Type()
)
enclTempSensorsUnderTempFailThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTempSensorsUnderTempFailThr.setStatus("current")
_EnclTempSensorsUnderTempWarnThr_Type = DisplayString
_EnclTempSensorsUnderTempWarnThr_Object = MibTableColumn
enclTempSensorsUnderTempWarnThr = _EnclTempSensorsUnderTempWarnThr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 29),
    _EnclTempSensorsUnderTempWarnThr_Type()
)
enclTempSensorsUnderTempWarnThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTempSensorsUnderTempWarnThr.setStatus("current")
_EnclElectronicsMaximum_Type = Integer32
_EnclElectronicsMaximum_Object = MibTableColumn
enclElectronicsMaximum = _EnclElectronicsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 30),
    _EnclElectronicsMaximum_Type()
)
enclElectronicsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclElectronicsMaximum.setStatus("current")
_EnclElectronicsPresent_Type = DisplayString
_EnclElectronicsPresent_Object = MibTableColumn
enclElectronicsPresent = _EnclElectronicsPresent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 31),
    _EnclElectronicsPresent_Type()
)
enclElectronicsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclElectronicsPresent.setStatus("current")
_EnclElectronicsSerialNos_Type = DisplayString
_EnclElectronicsSerialNos_Object = MibTableColumn
enclElectronicsSerialNos = _EnclElectronicsSerialNos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 32),
    _EnclElectronicsSerialNos_Type()
)
enclElectronicsSerialNos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclElectronicsSerialNos.setStatus("current")
_EnclElectronicsFailed_Type = DisplayString
_EnclElectronicsFailed_Object = MibTableColumn
enclElectronicsFailed = _EnclElectronicsFailed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 33),
    _EnclElectronicsFailed_Type()
)
enclElectronicsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclElectronicsFailed.setStatus("current")
_EnclVoltSensorsMaximum_Type = Integer32
_EnclVoltSensorsMaximum_Object = MibTableColumn
enclVoltSensorsMaximum = _EnclVoltSensorsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 34),
    _EnclVoltSensorsMaximum_Type()
)
enclVoltSensorsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclVoltSensorsMaximum.setStatus("current")
_EnclVoltSensorsPresent_Type = DisplayString
_EnclVoltSensorsPresent_Object = MibTableColumn
enclVoltSensorsPresent = _EnclVoltSensorsPresent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 35),
    _EnclVoltSensorsPresent_Type()
)
enclVoltSensorsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclVoltSensorsPresent.setStatus("current")
_EnclVoltSensorsOverVoltFail_Type = DisplayString
_EnclVoltSensorsOverVoltFail_Object = MibTableColumn
enclVoltSensorsOverVoltFail = _EnclVoltSensorsOverVoltFail_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 36),
    _EnclVoltSensorsOverVoltFail_Type()
)
enclVoltSensorsOverVoltFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclVoltSensorsOverVoltFail.setStatus("current")
_EnclVoltSensorsOverVoltWarn_Type = DisplayString
_EnclVoltSensorsOverVoltWarn_Object = MibTableColumn
enclVoltSensorsOverVoltWarn = _EnclVoltSensorsOverVoltWarn_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 37),
    _EnclVoltSensorsOverVoltWarn_Type()
)
enclVoltSensorsOverVoltWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclVoltSensorsOverVoltWarn.setStatus("current")
_EnclVoltSensorsUnderVoltFail_Type = DisplayString
_EnclVoltSensorsUnderVoltFail_Object = MibTableColumn
enclVoltSensorsUnderVoltFail = _EnclVoltSensorsUnderVoltFail_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 38),
    _EnclVoltSensorsUnderVoltFail_Type()
)
enclVoltSensorsUnderVoltFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclVoltSensorsUnderVoltFail.setStatus("current")
_EnclVoltSensorsUnderVoltWarn_Type = DisplayString
_EnclVoltSensorsUnderVoltWarn_Object = MibTableColumn
enclVoltSensorsUnderVoltWarn = _EnclVoltSensorsUnderVoltWarn_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 39),
    _EnclVoltSensorsUnderVoltWarn_Type()
)
enclVoltSensorsUnderVoltWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclVoltSensorsUnderVoltWarn.setStatus("current")
_EnclVoltSensorsCurrentVolt_Type = DisplayString
_EnclVoltSensorsCurrentVolt_Object = MibTableColumn
enclVoltSensorsCurrentVolt = _EnclVoltSensorsCurrentVolt_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 40),
    _EnclVoltSensorsCurrentVolt_Type()
)
enclVoltSensorsCurrentVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclVoltSensorsCurrentVolt.setStatus("current")
_EnclVoltSensorsOverVoltFailThr_Type = DisplayString
_EnclVoltSensorsOverVoltFailThr_Object = MibTableColumn
enclVoltSensorsOverVoltFailThr = _EnclVoltSensorsOverVoltFailThr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 41),
    _EnclVoltSensorsOverVoltFailThr_Type()
)
enclVoltSensorsOverVoltFailThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclVoltSensorsOverVoltFailThr.setStatus("current")
_EnclVoltSensorsOverVoltWarnThr_Type = DisplayString
_EnclVoltSensorsOverVoltWarnThr_Object = MibTableColumn
enclVoltSensorsOverVoltWarnThr = _EnclVoltSensorsOverVoltWarnThr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 42),
    _EnclVoltSensorsOverVoltWarnThr_Type()
)
enclVoltSensorsOverVoltWarnThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclVoltSensorsOverVoltWarnThr.setStatus("current")
_EnclVoltSensorsUnderVoltFailThr_Type = DisplayString
_EnclVoltSensorsUnderVoltFailThr_Object = MibTableColumn
enclVoltSensorsUnderVoltFailThr = _EnclVoltSensorsUnderVoltFailThr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 43),
    _EnclVoltSensorsUnderVoltFailThr_Type()
)
enclVoltSensorsUnderVoltFailThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclVoltSensorsUnderVoltFailThr.setStatus("current")
_EnclVoltSensorsUnderVoltWarnThr_Type = DisplayString
_EnclVoltSensorsUnderVoltWarnThr_Object = MibTableColumn
enclVoltSensorsUnderVoltWarnThr = _EnclVoltSensorsUnderVoltWarnThr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 44),
    _EnclVoltSensorsUnderVoltWarnThr_Type()
)
enclVoltSensorsUnderVoltWarnThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclVoltSensorsUnderVoltWarnThr.setStatus("current")
_EnclCurSensorsMaximum_Type = Integer32
_EnclCurSensorsMaximum_Object = MibTableColumn
enclCurSensorsMaximum = _EnclCurSensorsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 45),
    _EnclCurSensorsMaximum_Type()
)
enclCurSensorsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclCurSensorsMaximum.setStatus("current")
_EnclCurSensorsPresent_Type = DisplayString
_EnclCurSensorsPresent_Object = MibTableColumn
enclCurSensorsPresent = _EnclCurSensorsPresent_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 46),
    _EnclCurSensorsPresent_Type()
)
enclCurSensorsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclCurSensorsPresent.setStatus("current")
_EnclCurSensorsOverCurFail_Type = DisplayString
_EnclCurSensorsOverCurFail_Object = MibTableColumn
enclCurSensorsOverCurFail = _EnclCurSensorsOverCurFail_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 47),
    _EnclCurSensorsOverCurFail_Type()
)
enclCurSensorsOverCurFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclCurSensorsOverCurFail.setStatus("current")
_EnclCurSensorsOverCurWarn_Type = DisplayString
_EnclCurSensorsOverCurWarn_Object = MibTableColumn
enclCurSensorsOverCurWarn = _EnclCurSensorsOverCurWarn_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 48),
    _EnclCurSensorsOverCurWarn_Type()
)
enclCurSensorsOverCurWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclCurSensorsOverCurWarn.setStatus("current")
_EnclCurSensorsCurrentCur_Type = DisplayString
_EnclCurSensorsCurrentCur_Object = MibTableColumn
enclCurSensorsCurrentCur = _EnclCurSensorsCurrentCur_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 49),
    _EnclCurSensorsCurrentCur_Type()
)
enclCurSensorsCurrentCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclCurSensorsCurrentCur.setStatus("current")
_EnclCurSensorsOverCurFailThr_Type = DisplayString
_EnclCurSensorsOverCurFailThr_Object = MibTableColumn
enclCurSensorsOverCurFailThr = _EnclCurSensorsOverCurFailThr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 50),
    _EnclCurSensorsOverCurFailThr_Type()
)
enclCurSensorsOverCurFailThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclCurSensorsOverCurFailThr.setStatus("current")
_EnclCurSensorsOverCurWarnThr_Type = DisplayString
_EnclCurSensorsOverCurWarnThr_Object = MibTableColumn
enclCurSensorsOverCurWarnThr = _EnclCurSensorsOverCurWarnThr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 21, 1, 2, 1, 51),
    _EnclCurSensorsOverCurWarnThr_Type()
)
enclCurSensorsOverCurWarnThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclCurSensorsOverCurWarnThr.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 22)
)
_NetInterfaces_ObjectIdentity = ObjectIdentity
netInterfaces = _NetInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1)
)
_NetifNumber_Type = Integer32
_NetifNumber_Object = MibScalar
netifNumber = _NetifNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 1),
    _NetifNumber_Type()
)
netifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netifNumber.setStatus("current")
_NetifTable_Object = MibTable
netifTable = _NetifTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2)
)
if mibBuilder.loadTexts:
    netifTable.setStatus("current")
_NetifEntry_Object = MibTableRow
netifEntry = _NetifEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1)
)
netifEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "netifIndex"),
)
if mibBuilder.loadTexts:
    netifEntry.setStatus("current")


class _NetifIndex_Type(Integer32):
    """Custom type netifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NetifIndex_Type.__name__ = "Integer32"
_NetifIndex_Object = MibTableColumn
netifIndex = _NetifIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 1),
    _NetifIndex_Type()
)
netifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netifIndex.setStatus("current")


class _NetifDescr_Type(DisplayString):
    """Custom type netifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetifDescr_Type.__name__ = "DisplayString"
_NetifDescr_Object = MibTableColumn
netifDescr = _NetifDescr_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 2),
    _NetifDescr_Type()
)
netifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netifDescr.setStatus("current")
_IfHighInOctets_Type = Counter32
_IfHighInOctets_Object = MibTableColumn
ifHighInOctets = _IfHighInOctets_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 3),
    _IfHighInOctets_Type()
)
ifHighInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighInOctets.setStatus("current")
_IfLowInOctets_Type = Counter32
_IfLowInOctets_Object = MibTableColumn
ifLowInOctets = _IfLowInOctets_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 4),
    _IfLowInOctets_Type()
)
ifLowInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLowInOctets.setStatus("current")
_IfHighInUcastPkts_Type = Counter32
_IfHighInUcastPkts_Object = MibTableColumn
ifHighInUcastPkts = _IfHighInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 5),
    _IfHighInUcastPkts_Type()
)
ifHighInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighInUcastPkts.setStatus("current")
_IfLowInUcastPkts_Type = Counter32
_IfLowInUcastPkts_Object = MibTableColumn
ifLowInUcastPkts = _IfLowInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 6),
    _IfLowInUcastPkts_Type()
)
ifLowInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLowInUcastPkts.setStatus("current")
_IfHighInNUcastPkts_Type = Counter32
_IfHighInNUcastPkts_Object = MibTableColumn
ifHighInNUcastPkts = _IfHighInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 7),
    _IfHighInNUcastPkts_Type()
)
ifHighInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighInNUcastPkts.setStatus("current")
_IfLowInNUcastPkts_Type = Counter32
_IfLowInNUcastPkts_Object = MibTableColumn
ifLowInNUcastPkts = _IfLowInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 8),
    _IfLowInNUcastPkts_Type()
)
ifLowInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLowInNUcastPkts.setStatus("current")
_IfHighInDiscards_Type = Counter32
_IfHighInDiscards_Object = MibTableColumn
ifHighInDiscards = _IfHighInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 9),
    _IfHighInDiscards_Type()
)
ifHighInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighInDiscards.setStatus("current")
_IfLowInDiscards_Type = Counter32
_IfLowInDiscards_Object = MibTableColumn
ifLowInDiscards = _IfLowInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 10),
    _IfLowInDiscards_Type()
)
ifLowInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLowInDiscards.setStatus("current")
_IfHighInErrors_Type = Counter32
_IfHighInErrors_Object = MibTableColumn
ifHighInErrors = _IfHighInErrors_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 11),
    _IfHighInErrors_Type()
)
ifHighInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighInErrors.setStatus("current")
_IfLowInErrors_Type = Counter32
_IfLowInErrors_Object = MibTableColumn
ifLowInErrors = _IfLowInErrors_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 12),
    _IfLowInErrors_Type()
)
ifLowInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLowInErrors.setStatus("current")
_IfHighInUnknownProtos_Type = Counter32
_IfHighInUnknownProtos_Object = MibTableColumn
ifHighInUnknownProtos = _IfHighInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 13),
    _IfHighInUnknownProtos_Type()
)
ifHighInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighInUnknownProtos.setStatus("current")
_IfLowInUnknownProtos_Type = Counter32
_IfLowInUnknownProtos_Object = MibTableColumn
ifLowInUnknownProtos = _IfLowInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 14),
    _IfLowInUnknownProtos_Type()
)
ifLowInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLowInUnknownProtos.setStatus("current")
_IfHighOutOctets_Type = Counter32
_IfHighOutOctets_Object = MibTableColumn
ifHighOutOctets = _IfHighOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 15),
    _IfHighOutOctets_Type()
)
ifHighOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighOutOctets.setStatus("current")
_IfLowOutOctets_Type = Counter32
_IfLowOutOctets_Object = MibTableColumn
ifLowOutOctets = _IfLowOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 16),
    _IfLowOutOctets_Type()
)
ifLowOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLowOutOctets.setStatus("current")
_IfHighOutUcastPkts_Type = Counter32
_IfHighOutUcastPkts_Object = MibTableColumn
ifHighOutUcastPkts = _IfHighOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 17),
    _IfHighOutUcastPkts_Type()
)
ifHighOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighOutUcastPkts.setStatus("current")
_IfLowOutUcastPkts_Type = Counter32
_IfLowOutUcastPkts_Object = MibTableColumn
ifLowOutUcastPkts = _IfLowOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 18),
    _IfLowOutUcastPkts_Type()
)
ifLowOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLowOutUcastPkts.setStatus("current")
_IfHighOutNUcastPkts_Type = Counter32
_IfHighOutNUcastPkts_Object = MibTableColumn
ifHighOutNUcastPkts = _IfHighOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 19),
    _IfHighOutNUcastPkts_Type()
)
ifHighOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighOutNUcastPkts.setStatus("current")
_IfLowOutNUcastPkts_Type = Counter32
_IfLowOutNUcastPkts_Object = MibTableColumn
ifLowOutNUcastPkts = _IfLowOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 20),
    _IfLowOutNUcastPkts_Type()
)
ifLowOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLowOutNUcastPkts.setStatus("current")
_IfHighOutDiscards_Type = Counter32
_IfHighOutDiscards_Object = MibTableColumn
ifHighOutDiscards = _IfHighOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 21),
    _IfHighOutDiscards_Type()
)
ifHighOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighOutDiscards.setStatus("current")
_IfLowOutDiscards_Type = Counter32
_IfLowOutDiscards_Object = MibTableColumn
ifLowOutDiscards = _IfLowOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 22),
    _IfLowOutDiscards_Type()
)
ifLowOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLowOutDiscards.setStatus("current")
_IfHighOutErrors_Type = Counter32
_IfHighOutErrors_Object = MibTableColumn
ifHighOutErrors = _IfHighOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 23),
    _IfHighOutErrors_Type()
)
ifHighOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighOutErrors.setStatus("current")
_IfLowOutErrors_Type = Counter32
_IfLowOutErrors_Object = MibTableColumn
ifLowOutErrors = _IfLowOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 24),
    _IfLowOutErrors_Type()
)
ifLowOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLowOutErrors.setStatus("current")
_If64InOctets_Type = Counter64
_If64InOctets_Object = MibTableColumn
if64InOctets = _If64InOctets_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 25),
    _If64InOctets_Type()
)
if64InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    if64InOctets.setStatus("current")
_If64InUcastPkts_Type = Counter64
_If64InUcastPkts_Object = MibTableColumn
if64InUcastPkts = _If64InUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 26),
    _If64InUcastPkts_Type()
)
if64InUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    if64InUcastPkts.setStatus("current")
_If64InNUcastPkts_Type = Counter64
_If64InNUcastPkts_Object = MibTableColumn
if64InNUcastPkts = _If64InNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 27),
    _If64InNUcastPkts_Type()
)
if64InNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    if64InNUcastPkts.setStatus("current")
_If64InDiscards_Type = Counter64
_If64InDiscards_Object = MibTableColumn
if64InDiscards = _If64InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 28),
    _If64InDiscards_Type()
)
if64InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    if64InDiscards.setStatus("current")
_If64InErrors_Type = Counter64
_If64InErrors_Object = MibTableColumn
if64InErrors = _If64InErrors_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 29),
    _If64InErrors_Type()
)
if64InErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    if64InErrors.setStatus("current")
_If64InUnknownProtos_Type = Counter64
_If64InUnknownProtos_Object = MibTableColumn
if64InUnknownProtos = _If64InUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 30),
    _If64InUnknownProtos_Type()
)
if64InUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    if64InUnknownProtos.setStatus("current")
_If64OutOctets_Type = Counter64
_If64OutOctets_Object = MibTableColumn
if64OutOctets = _If64OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 31),
    _If64OutOctets_Type()
)
if64OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    if64OutOctets.setStatus("current")
_If64OutUcastPkts_Type = Counter64
_If64OutUcastPkts_Object = MibTableColumn
if64OutUcastPkts = _If64OutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 32),
    _If64OutUcastPkts_Type()
)
if64OutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    if64OutUcastPkts.setStatus("current")
_If64OutNUcastPkts_Type = Counter64
_If64OutNUcastPkts_Object = MibTableColumn
if64OutNUcastPkts = _If64OutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 33),
    _If64OutNUcastPkts_Type()
)
if64OutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    if64OutNUcastPkts.setStatus("current")
_If64OutDiscards_Type = Counter64
_If64OutDiscards_Object = MibTableColumn
if64OutDiscards = _If64OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 34),
    _If64OutDiscards_Type()
)
if64OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    if64OutDiscards.setStatus("current")
_If64OutErrors_Type = Counter64
_If64OutErrors_Object = MibTableColumn
if64OutErrors = _If64OutErrors_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 22, 1, 2, 1, 35),
    _If64OutErrors_Type()
)
if64OutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    if64OutErrors.setStatus("current")
_Sis_ObjectIdentity = ObjectIdentity
sis = _Sis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 23)
)


class _SisIsLicensed_Type(Integer32):
    """Custom type sisIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SisIsLicensed_Type.__name__ = "Integer32"
_SisIsLicensed_Object = MibScalar
sisIsLicensed = _SisIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 1),
    _SisIsLicensed_Type()
)
sisIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisIsLicensed.setStatus("current")
_SisTable_Object = MibTable
sisTable = _SisTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2)
)
if mibBuilder.loadTexts:
    sisTable.setStatus("current")
_SisEntry_Object = MibTableRow
sisEntry = _SisEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1)
)
sisEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "sisIndex"),
)
if mibBuilder.loadTexts:
    sisEntry.setStatus("current")


class _SisIndex_Type(Integer32):
    """Custom type sisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SisIndex_Type.__name__ = "Integer32"
_SisIndex_Object = MibTableColumn
sisIndex = _SisIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 1),
    _SisIndex_Type()
)
sisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisIndex.setStatus("current")
_SisPath_Type = DisplayString
_SisPath_Object = MibTableColumn
sisPath = _SisPath_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 2),
    _SisPath_Type()
)
sisPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisPath.setStatus("current")


class _SisState_Type(Integer32):
    """Custom type sisState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SisState_Type.__name__ = "Integer32"
_SisState_Object = MibTableColumn
sisState = _SisState_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 3),
    _SisState_Type()
)
sisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisState.setStatus("current")


class _SisStatus_Type(Integer32):
    """Custom type sisStatus based on Integer32"""
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
        *(("active", 2),
          ("idle", 1),
          ("pending", 4),
          ("undoing", 3))
    )


_SisStatus_Type.__name__ = "Integer32"
_SisStatus_Object = MibTableColumn
sisStatus = _SisStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 4),
    _SisStatus_Type()
)
sisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisStatus.setStatus("current")
_SisProgress_Type = DisplayString
_SisProgress_Object = MibTableColumn
sisProgress = _SisProgress_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 5),
    _SisProgress_Type()
)
sisProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisProgress.setStatus("current")


class _SisType_Type(Integer32):
    """Custom type sisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("snapvault", 2))
    )


_SisType_Type.__name__ = "Integer32"
_SisType_Object = MibTableColumn
sisType = _SisType_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 6),
    _SisType_Type()
)
sisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisType.setStatus("current")
_SisSchedule_Type = DisplayString
_SisSchedule_Object = MibTableColumn
sisSchedule = _SisSchedule_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 7),
    _SisSchedule_Type()
)
sisSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisSchedule.setStatus("current")
_SisLastOpBeginTime_Type = DisplayString
_SisLastOpBeginTime_Object = MibTableColumn
sisLastOpBeginTime = _SisLastOpBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 8),
    _SisLastOpBeginTime_Type()
)
sisLastOpBeginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisLastOpBeginTime.setStatus("current")
_SisLastOpEndTime_Type = DisplayString
_SisLastOpEndTime_Object = MibTableColumn
sisLastOpEndTime = _SisLastOpEndTime_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 9),
    _SisLastOpEndTime_Type()
)
sisLastOpEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisLastOpEndTime.setStatus("current")
_SisHighLastOpSize_Type = Integer32
_SisHighLastOpSize_Object = MibTableColumn
sisHighLastOpSize = _SisHighLastOpSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 10),
    _SisHighLastOpSize_Type()
)
sisHighLastOpSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisHighLastOpSize.setStatus("current")
_SisLowLastOpSize_Type = Integer32
_SisLowLastOpSize_Object = MibTableColumn
sisLowLastOpSize = _SisLowLastOpSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 11),
    _SisLowLastOpSize_Type()
)
sisLowLastOpSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisLowLastOpSize.setStatus("current")
_SisLastOpError_Type = DisplayString
_SisLastOpError_Object = MibTableColumn
sisLastOpError = _SisLastOpError_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 12),
    _SisLastOpError_Type()
)
sisLastOpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sisLastOpError.setStatus("current")
_Sis64LastOpSize_Type = Counter64
_Sis64LastOpSize_Object = MibTableColumn
sis64LastOpSize = _Sis64LastOpSize_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 23, 2, 1, 13),
    _Sis64LastOpSize_Type()
)
sis64LastOpSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sis64LastOpSize.setStatus("current")
_Compress_ObjectIdentity = ObjectIdentity
compress = _Compress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 1, 24)
)


class _CompressIsLicensed_Type(Integer32):
    """Custom type compressIsLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_CompressIsLicensed_Type.__name__ = "Integer32"
_CompressIsLicensed_Object = MibScalar
compressIsLicensed = _CompressIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 24, 1),
    _CompressIsLicensed_Type()
)
compressIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressIsLicensed.setStatus("current")
_CompressTable_Object = MibTable
compressTable = _CompressTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 24, 2)
)
if mibBuilder.loadTexts:
    compressTable.setStatus("current")
_CompressEntry_Object = MibTableRow
compressEntry = _CompressEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 24, 2, 1)
)
compressEntry.setIndexNames(
    (0, "NETWORK-APPLIANCE-MIB", "compressIndex"),
)
if mibBuilder.loadTexts:
    compressEntry.setStatus("current")


class _CompressIndex_Type(Integer32):
    """Custom type compressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CompressIndex_Type.__name__ = "Integer32"
_CompressIndex_Object = MibTableColumn
compressIndex = _CompressIndex_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 24, 2, 1, 1),
    _CompressIndex_Type()
)
compressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressIndex.setStatus("current")
_CompressFileSys_Type = DisplayString
_CompressFileSys_Object = MibTableColumn
compressFileSys = _CompressFileSys_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 24, 2, 1, 2),
    _CompressFileSys_Type()
)
compressFileSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressFileSys.setStatus("current")
_CompressHighUsedKBytes_Type = Counter32
_CompressHighUsedKBytes_Object = MibTableColumn
compressHighUsedKBytes = _CompressHighUsedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 24, 2, 1, 3),
    _CompressHighUsedKBytes_Type()
)
compressHighUsedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressHighUsedKBytes.setStatus("current")
_CompressLowUsedKBytes_Type = Counter32
_CompressLowUsedKBytes_Object = MibTableColumn
compressLowUsedKBytes = _CompressLowUsedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 24, 2, 1, 4),
    _CompressLowUsedKBytes_Type()
)
compressLowUsedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressLowUsedKBytes.setStatus("current")
_Compress64UsedKBytes_Type = Counter64
_Compress64UsedKBytes_Object = MibTableColumn
compress64UsedKBytes = _Compress64UsedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 24, 2, 1, 5),
    _Compress64UsedKBytes_Type()
)
compress64UsedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compress64UsedKBytes.setStatus("current")
_CompressHighSavedKBytes_Type = Counter32
_CompressHighSavedKBytes_Object = MibTableColumn
compressHighSavedKBytes = _CompressHighSavedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 24, 2, 1, 6),
    _CompressHighSavedKBytes_Type()
)
compressHighSavedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressHighSavedKBytes.setStatus("current")
_CompressLowSavedKBytes_Type = Counter32
_CompressLowSavedKBytes_Object = MibTableColumn
compressLowSavedKBytes = _CompressLowSavedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 24, 2, 1, 7),
    _CompressLowSavedKBytes_Type()
)
compressLowSavedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressLowSavedKBytes.setStatus("current")
_Compress64SavedKBytes_Type = Counter64
_Compress64SavedKBytes_Object = MibTableColumn
compress64SavedKBytes = _Compress64SavedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 24, 2, 1, 8),
    _Compress64SavedKBytes_Type()
)
compress64SavedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compress64SavedKBytes.setStatus("current")
_CompressPercentSaved_Type = Integer32
_CompressPercentSaved_Object = MibTableColumn
compressPercentSaved = _CompressPercentSaved_Object(
    (1, 3, 6, 1, 4, 1, 789, 1, 24, 2, 1, 9),
    _CompressPercentSaved_Type()
)
compressPercentSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressPercentSaved.setStatus("current")
_NetappProducts_ObjectIdentity = ObjectIdentity
netappProducts = _NetappProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 2)
)
_NetappFiler_ObjectIdentity = ObjectIdentity
netappFiler = _NetappFiler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 2, 1)
)
_NetappNetCache_ObjectIdentity = ObjectIdentity
netappNetCache = _NetappNetCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 2, 2)
)
_NetappClusteredFiler_ObjectIdentity = ObjectIdentity
netappClusteredFiler = _NetappClusteredFiler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 2, 3)
)
_NetappNode_ObjectIdentity = ObjectIdentity
netappNode = _NetappNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 2, 4)
)
_NetappDataFabricManager_ObjectIdentity = ObjectIdentity
netappDataFabricManager = _NetappDataFabricManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 3)
)
_NetappSupportConsole_ObjectIdentity = ObjectIdentity
netappSupportConsole = _NetappSupportConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 4)
)

# Managed Objects groups


# Notification objects

userDefined = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 2)
)
userDefined.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    userDefined.setStatus(
        "current"
    )

dhmNoticeDegradedIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 6)
)
dhmNoticeDegradedIO.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    dhmNoticeDegradedIO.setStatus(
        "current"
    )

dhmNoticePFAEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 7)
)
dhmNoticePFAEvent.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    dhmNoticePFAEvent.setStatus(
        "current"
    )

emergencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 11)
)
emergencyTrap.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    emergencyTrap.setStatus(
        "current"
    )

alertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 12)
)
alertTrap.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    alertTrap.setStatus(
        "current"
    )

criticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 13)
)
criticalTrap.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    criticalTrap.setStatus(
        "current"
    )

errorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 14)
)
errorTrap.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    errorTrap.setStatus(
        "current"
    )

warningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 15)
)
warningTrap.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    warningTrap.setStatus(
        "current"
    )

notificationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 16)
)
notificationTrap.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    notificationTrap.setStatus(
        "current"
    )

informationalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 17)
)
informationalTrap.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    informationalTrap.setStatus(
        "current"
    )

dbgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 18)
)
dbgTrap.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    dbgTrap.setStatus(
        "current"
    )

diskFailedShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 21)
)
diskFailedShutdown.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    diskFailedShutdown.setStatus(
        "current"
    )

diskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 22)
)
diskFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    diskFailed.setStatus(
        "current"
    )

diskRepaired = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 26)
)
diskRepaired.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    diskRepaired.setStatus(
        "current"
    )

fanFailureShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 31)
)
fanFailureShutdown.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    fanFailureShutdown.setStatus(
        "current"
    )

fanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 33)
)
fanFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    fanFailed.setStatus(
        "current"
    )

fanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 35)
)
fanWarning.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    fanWarning.setStatus(
        "current"
    )

fanRepaired = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 36)
)
fanRepaired.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    fanRepaired.setStatus(
        "current"
    )

powerSupplyFailureShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 41)
)
powerSupplyFailureShutdown.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    powerSupplyFailureShutdown.setStatus(
        "current"
    )

powerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 43)
)
powerSupplyFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    powerSupplyFailed.setStatus(
        "current"
    )

powerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 45)
)
powerSupplyWarning.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    powerSupplyWarning.setStatus(
        "current"
    )

powerSupplyRepaired = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 46)
)
powerSupplyRepaired.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    powerSupplyRepaired.setStatus(
        "current"
    )

cpuTooBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 55)
)
cpuTooBusy.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    cpuTooBusy.setStatus(
        "current"
    )

cpuOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 56)
)
cpuOk.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    cpuOk.setStatus(
        "current"
    )

nvramBatteryDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 62)
)
nvramBatteryDischarged.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    nvramBatteryDischarged.setStatus(
        "current"
    )

nvramBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 63)
)
nvramBatteryLow.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    nvramBatteryLow.setStatus(
        "current"
    )

clusterNodeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 72)
)
clusterNodeFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    clusterNodeFailed.setStatus(
        "current"
    )

clusterNodeTakenOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 75)
)
clusterNodeTakenOver.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    clusterNodeTakenOver.setStatus(
        "current"
    )

clusterNodeRepaired = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 76)
)
clusterNodeRepaired.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    clusterNodeRepaired.setStatus(
        "current"
    )

volumeFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 82)
)
volumeFull.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeFull.setStatus(
        "current"
    )

volumeNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 85)
)
volumeNearlyFull.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeNearlyFull.setStatus(
        "current"
    )

volumeRepaired = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 86)
)
volumeRepaired.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeRepaired.setStatus(
        "current"
    )

volumesStillFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 87)
)
volumesStillFull.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumesStillFull.setStatus(
        "current"
    )

overTempShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 91)
)
overTempShutdown.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    overTempShutdown.setStatus(
        "current"
    )

overTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 95)
)
overTemp.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    overTemp.setStatus(
        "current"
    )

overTempRepaired = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 96)
)
overTempRepaired.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    overTempRepaired.setStatus(
        "current"
    )

shelfFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 103)
)
shelfFault.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    shelfFault.setStatus(
        "current"
    )

shelfRepaired = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 106)
)
shelfRepaired.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    shelfRepaired.setStatus(
        "current"
    )

globalStatusNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 111)
)
globalStatusNonRecoverable.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    globalStatusNonRecoverable.setStatus(
        "current"
    )

globalStatusCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 113)
)
globalStatusCritical.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    globalStatusCritical.setStatus(
        "current"
    )

globalStatusNonCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 115)
)
globalStatusNonCritical.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    globalStatusNonCritical.setStatus(
        "current"
    )

globalStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 116)
)
globalStatusOk.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    globalStatusOk.setStatus(
        "current"
    )

softQuotaExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 126)
)
softQuotaExceeded.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    softQuotaExceeded.setStatus(
        "current"
    )

softQuotaNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 127)
)
softQuotaNormal.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    softQuotaNormal.setStatus(
        "current"
    )

autosupportSendError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 134)
)
autosupportSendError.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    autosupportSendError.setStatus(
        "current"
    )

autosupportConfigurationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 135)
)
autosupportConfigurationError.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    autosupportConfigurationError.setStatus(
        "current"
    )

autosupportSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 136)
)
autosupportSent.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    autosupportSent.setStatus(
        "current"
    )

upsLinePowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 142)
)
upsLinePowerOff.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    upsLinePowerOff.setStatus(
        "current"
    )

upsBatteryCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 143)
)
upsBatteryCritical.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    upsBatteryCritical.setStatus(
        "current"
    )

upsShuttingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 144)
)
upsShuttingDown.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    upsShuttingDown.setStatus(
        "current"
    )

upsBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 145)
)
upsBatteryWarning.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    upsBatteryWarning.setStatus(
        "current"
    )

upsLinePowerRetored = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 146)
)
upsLinePowerRetored.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    upsLinePowerRetored.setStatus(
        "current"
    )

appEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 151)
)
appEmergency.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    appEmergency.setStatus(
        "current"
    )

appAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 152)
)
appAlert.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    appAlert.setStatus(
        "current"
    )

appCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 153)
)
appCritical.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    appCritical.setStatus(
        "current"
    )

appError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 154)
)
appError.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    appError.setStatus(
        "current"
    )

appWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 155)
)
appWarning.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    appWarning.setStatus(
        "current"
    )

appNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 156)
)
appNotice.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    appNotice.setStatus(
        "current"
    )

appInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 157)
)
appInfo.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    appInfo.setStatus(
        "current"
    )

appTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 158)
)
appTrap.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    appTrap.setStatus(
        "current"
    )

alfFilewrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 162)
)
alfFilewrap.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    alfFilewrap.setStatus(
        "current"
    )

alfFileSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 166)
)
alfFileSaved.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    alfFileSaved.setStatus(
        "current"
    )

alfFileNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 167)
)
alfFileNearlyFull.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    alfFileNearlyFull.setStatus(
        "current"
    )

quotaExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 176)
)
quotaExceeded.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    quotaExceeded.setStatus(
        "current"
    )

quotaNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 177)
)
quotaNormal.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    quotaNormal.setStatus(
        "current"
    )

waflDirNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 186)
)
waflDirNearlyFull.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    waflDirNearlyFull.setStatus(
        "current"
    )

waflDirFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 187)
)
waflDirFull.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    waflDirFull.setStatus(
        "current"
    )

eccSummary = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 192)
)
eccSummary.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    eccSummary.setStatus(
        "current"
    )

eccMasked = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 195)
)
eccMasked.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    eccMasked.setStatus(
        "current"
    )

ftpdError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 204)
)
ftpdError.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    ftpdError.setStatus(
        "current"
    )

ftpdMaxConnNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 206)
)
ftpdMaxConnNotice.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    ftpdMaxConnNotice.setStatus(
        "current"
    )

ftpdMaxConnThresholdNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 216)
)
ftpdMaxConnThresholdNotice.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    ftpdMaxConnThresholdNotice.setStatus(
        "current"
    )

scsitgtFCPLinkBreak = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 222)
)
scsitgtFCPLinkBreak.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    scsitgtFCPLinkBreak.setStatus(
        "current"
    )

scsitgtPartnerPathMisconfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 224)
)
scsitgtPartnerPathMisconfigured.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    scsitgtPartnerPathMisconfigured.setStatus(
        "current"
    )

scsitgtThrottleNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 226)
)
scsitgtThrottleNotice.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    scsitgtThrottleNotice.setStatus(
        "current"
    )

vifPrimaryLinkFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 237)
)
vifPrimaryLinkFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    vifPrimaryLinkFailed.setStatus(
        "current"
    )

vifAllLinksFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 238)
)
vifAllLinksFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    vifAllLinksFailed.setStatus(
        "current"
    )

vfStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 245)
)
vfStopped.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    vfStopped.setStatus(
        "current"
    )

vfStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 246)
)
vfStarted.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    vfStarted.setStatus(
        "current"
    )

vscanVirusDetectedError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 254)
)
vscanVirusDetectedError.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    vscanVirusDetectedError.setStatus(
        "current"
    )

vscanDisConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 255)
)
vscanDisConnection.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    vscanDisConnection.setStatus(
        "current"
    )

vscanConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 256)
)
vscanConfigurationChange.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    vscanConfigurationChange.setStatus(
        "current"
    )

vscanConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 257)
)
vscanConnection.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    vscanConnection.setStatus(
        "current"
    )

vscanServerUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 266)
)
vscanServerUpgrade.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    vscanServerUpgrade.setStatus(
        "current"
    )

volumeRestrictedByMirrorBigIo = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 272)
)
volumeRestrictedByMirrorBigIo.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeRestrictedByMirrorBigIo.setStatus(
        "current"
    )

volumeInconsistentUmount = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 274)
)
volumeInconsistentUmount.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeInconsistentUmount.setStatus(
        "current"
    )

volumeStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 275)
)
volumeStateChanged.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeStateChanged.setStatus(
        "current"
    )

volumeOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 276)
)
volumeOnline.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeOnline.setStatus(
        "current"
    )

rmcCardNeedsReplacement = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 283)
)
rmcCardNeedsReplacement.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    rmcCardNeedsReplacement.setStatus(
        "current"
    )

rmcCardMissingCables = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 284)
)
rmcCardMissingCables.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    rmcCardMissingCables.setStatus(
        "current"
    )

volumeRemoteUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 294)
)
volumeRemoteUnreachable.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeRemoteUnreachable.setStatus(
        "current"
    )

volumeRemoteOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 296)
)
volumeRemoteOk.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeRemoteOk.setStatus(
        "current"
    )

volumeRemoteRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 297)
)
volumeRemoteRestored.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeRemoteRestored.setStatus(
        "current"
    )

volumeRemoteRestoreBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 298)
)
volumeRemoteRestoreBegin.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeRemoteRestoreBegin.setStatus(
        "current"
    )

volumeRestrictedRootConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 304)
)
volumeRestrictedRootConflict.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeRestrictedRootConflict.setStatus(
        "current"
    )

volumeOfflineTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 314)
)
volumeOfflineTooBig.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeOfflineTooBig.setStatus(
        "current"
    )

volumeOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 324)
)
volumeOffline.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeOffline.setStatus(
        "current"
    )

volumeRestricted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 334)
)
volumeRestricted.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeRestricted.setStatus(
        "current"
    )

volumeDegradedDirty = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 344)
)
volumeDegradedDirty.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeDegradedDirty.setStatus(
        "current"
    )

volumeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 354)
)
volumeError.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeError.setStatus(
        "current"
    )

snapmirrorSyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 364)
)
snapmirrorSyncFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    snapmirrorSyncFailed.setStatus(
        "current"
    )

snapmirrorSyncOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 366)
)
snapmirrorSyncOk.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    snapmirrorSyncOk.setStatus(
        "current"
    )

chassisTemperatureShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 371)
)
chassisTemperatureShutdown.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisTemperatureShutdown.setStatus(
        "current"
    )

chassisTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 372)
)
chassisTemperatureWarning.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisTemperatureWarning.setStatus(
        "current"
    )

chassisTemperatureUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 375)
)
chassisTemperatureUnknown.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisTemperatureUnknown.setStatus(
        "current"
    )

chassisTemperatureOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 376)
)
chassisTemperatureOk.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisTemperatureOk.setStatus(
        "current"
    )

chassisCPUFanStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 381)
)
chassisCPUFanStopped.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisCPUFanStopped.setStatus(
        "current"
    )

chassisCPUFanSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 383)
)
chassisCPUFanSlow.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisCPUFanSlow.setStatus(
        "current"
    )

chassisCPUFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 386)
)
chassisCPUFanOk.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisCPUFanOk.setStatus(
        "current"
    )

chassisPowerSuppliesFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 391)
)
chassisPowerSuppliesFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisPowerSuppliesFailed.setStatus(
        "current"
    )

chassisPowerSupplyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 392)
)
chassisPowerSupplyDegraded.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisPowerSupplyDegraded.setStatus(
        "current"
    )

chassisPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 393)
)
chassisPowerSupplyFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisPowerSupplyFailed.setStatus(
        "current"
    )

chassisPowerSupplyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 394)
)
chassisPowerSupplyRemoved.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisPowerSupplyRemoved.setStatus(
        "current"
    )

chassisPowerSupplyOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 395)
)
chassisPowerSupplyOff.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisPowerSupplyOff.setStatus(
        "current"
    )

chassisPowerSuppliesOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 396)
)
chassisPowerSuppliesOk.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisPowerSuppliesOk.setStatus(
        "current"
    )

chassisPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 397)
)
chassisPowerSupplyOk.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisPowerSupplyOk.setStatus(
        "current"
    )

chassisPowerDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 403)
)
chassisPowerDegraded.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisPowerDegraded.setStatus(
        "current"
    )

chassisPowerOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 406)
)
chassisPowerOk.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisPowerOk.setStatus(
        "current"
    )

chassisFanDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 412)
)
chassisFanDegraded.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisFanDegraded.setStatus(
        "current"
    )

chassisFanRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 413)
)
chassisFanRemoved.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisFanRemoved.setStatus(
        "current"
    )

chassisFanStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 414)
)
chassisFanStopped.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisFanStopped.setStatus(
        "current"
    )

chassisFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 415)
)
chassisFanWarning.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisFanWarning.setStatus(
        "current"
    )

chassisFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 416)
)
chassisFanOk.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisFanOk.setStatus(
        "current"
    )

writeVerificationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 424)
)
writeVerificationFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    writeVerificationFailed.setStatus(
        "current"
    )

domainControllerDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 435)
)
domainControllerDisconnect.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    domainControllerDisconnect.setStatus(
        "current"
    )

dcPasswdChangeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 436)
)
dcPasswdChangeFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    dcPasswdChangeFailed.setStatus(
        "current"
    )

domainControllerConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 437)
)
domainControllerConnected.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    domainControllerConnected.setStatus(
        "current"
    )

plexFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 444)
)
plexFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    plexFailed.setStatus(
        "current"
    )

plexOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 454)
)
plexOffline.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    plexOffline.setStatus(
        "current"
    )

shelfSESElectronicsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 464)
)
shelfSESElectronicsFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    shelfSESElectronicsFailed.setStatus(
        "current"
    )

shelfSESElectronicsInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 467)
)
shelfSESElectronicsInfo.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    shelfSESElectronicsInfo.setStatus(
        "current"
    )

shelfIFModuleFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 473)
)
shelfIFModuleFailed.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    shelfIFModuleFailed.setStatus(
        "current"
    )

shelfIFModuleWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 475)
)
shelfIFModuleWarning.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    shelfIFModuleWarning.setStatus(
        "current"
    )

shelfIFModuleInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 477)
)
shelfIFModuleInfo.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    shelfIFModuleInfo.setStatus(
        "current"
    )

maxDirSizeAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 482)
)
maxDirSizeAlert.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    maxDirSizeAlert.setStatus(
        "current"
    )

maxDirSizeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 485)
)
maxDirSizeWarning.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    maxDirSizeWarning.setStatus(
        "current"
    )

cifsStatsExhaustMemCtrlBlk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 497)
)
cifsStatsExhaustMemCtrlBlk.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    cifsStatsExhaustMemCtrlBlk.setStatus(
        "current"
    )

chassisPSRemovedxMinShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 501)
)
chassisPSRemovedxMinShutdown.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisPSRemovedxMinShutdown.setStatus(
        "current"
    )

chassisPSUsMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 505)
)
chassisPSUsMismatch.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisPSUsMismatch.setStatus(
        "current"
    )

chassisFanFailxMinShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 511)
)
chassisFanFailxMinShutdown.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisFanFailxMinShutdown.setStatus(
        "current"
    )

chassisPSUwrongInput = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 515)
)
chassisPSUwrongInput.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    chassisPSUwrongInput.setStatus(
        "current"
    )

powerSupplyFanFailxMinShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 521)
)
powerSupplyFanFailxMinShutdown.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    powerSupplyFanFailxMinShutdown.setStatus(
        "current"
    )

remoteSystemMgtAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 532)
)
remoteSystemMgtAlert.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    remoteSystemMgtAlert.setStatus(
        "current"
    )

remoteSystemMgmtWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 535)
)
remoteSystemMgmtWarning.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    remoteSystemMgmtWarning.setStatus(
        "current"
    )

remoteSystemMgmtNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 536)
)
remoteSystemMgmtNotification.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    remoteSystemMgmtNotification.setStatus(
        "current"
    )

remoteSystemMgmtPeriodic = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 547)
)
remoteSystemMgmtPeriodic.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    remoteSystemMgmtPeriodic.setStatus(
        "current"
    )

remotesystemMgmtTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 556)
)
remotesystemMgmtTest.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    remotesystemMgmtTest.setStatus(
        "current"
    )

diskMultipathOneSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 562)
)
diskMultipathOneSwitch.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    diskMultipathOneSwitch.setStatus(
        "current"
    )

diskMultipathNoTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 563)
)
diskMultipathNoTakeover.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    diskMultipathNoTakeover.setStatus(
        "current"
    )

diskMultipathWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 565)
)
diskMultipathWarning.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    diskMultipathWarning.setStatus(
        "current"
    )

driveDisableErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 574)
)
driveDisableErr.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    driveDisableErr.setStatus(
        "current"
    )

hbaOfflineInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 587)
)
hbaOfflineInformation.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    hbaOfflineInformation.setStatus(
        "current"
    )

lunSnapRestoreStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 606)
)
lunSnapRestoreStatus.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    lunSnapRestoreStatus.setStatus(
        "current"
    )

lunCloneCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 616)
)
lunCloneCreate.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    lunCloneCreate.setStatus(
        "current"
    )

lunCloneSplitStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 626)
)
lunCloneSplitStart.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    lunCloneSplitStart.setStatus(
        "current"
    )

lunCloneSplitComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 627)
)
lunCloneSplitComplete.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    lunCloneSplitComplete.setStatus(
        "current"
    )

flexCloneSplitStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 636)
)
flexCloneSplitStart.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    flexCloneSplitStart.setStatus(
        "current"
    )

flexCloneSplitComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 637)
)
flexCloneSplitComplete.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    flexCloneSplitComplete.setStatus(
        "current"
    )

volumeCloneCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 646)
)
volumeCloneCreate.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeCloneCreate.setStatus(
        "current"
    )

snapAutoDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 656)
)
snapAutoDelete.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    snapAutoDelete.setStatus(
        "current"
    )

volumeAutogrow = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 0, 666)
)
volumeAutogrow.setObjects(
      *(("NETWORK-APPLIANCE-MIB", "productTrapData"),
        ("NETWORK-APPLIANCE-MIB", "productSerialNum"))
)
if mibBuilder.loadTexts:
    volumeAutogrow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETWORK-APPLIANCE-MIB",
    **{"netapp": netapp,
       "userDefined": userDefined,
       "dhmNoticeDegradedIO": dhmNoticeDegradedIO,
       "dhmNoticePFAEvent": dhmNoticePFAEvent,
       "emergencyTrap": emergencyTrap,
       "alertTrap": alertTrap,
       "criticalTrap": criticalTrap,
       "errorTrap": errorTrap,
       "warningTrap": warningTrap,
       "notificationTrap": notificationTrap,
       "informationalTrap": informationalTrap,
       "dbgTrap": dbgTrap,
       "diskFailedShutdown": diskFailedShutdown,
       "diskFailed": diskFailed,
       "diskRepaired": diskRepaired,
       "fanFailureShutdown": fanFailureShutdown,
       "fanFailed": fanFailed,
       "fanWarning": fanWarning,
       "fanRepaired": fanRepaired,
       "powerSupplyFailureShutdown": powerSupplyFailureShutdown,
       "powerSupplyFailed": powerSupplyFailed,
       "powerSupplyWarning": powerSupplyWarning,
       "powerSupplyRepaired": powerSupplyRepaired,
       "cpuTooBusy": cpuTooBusy,
       "cpuOk": cpuOk,
       "nvramBatteryDischarged": nvramBatteryDischarged,
       "nvramBatteryLow": nvramBatteryLow,
       "clusterNodeFailed": clusterNodeFailed,
       "clusterNodeTakenOver": clusterNodeTakenOver,
       "clusterNodeRepaired": clusterNodeRepaired,
       "volumeFull": volumeFull,
       "volumeNearlyFull": volumeNearlyFull,
       "volumeRepaired": volumeRepaired,
       "volumesStillFull": volumesStillFull,
       "overTempShutdown": overTempShutdown,
       "overTemp": overTemp,
       "overTempRepaired": overTempRepaired,
       "shelfFault": shelfFault,
       "shelfRepaired": shelfRepaired,
       "globalStatusNonRecoverable": globalStatusNonRecoverable,
       "globalStatusCritical": globalStatusCritical,
       "globalStatusNonCritical": globalStatusNonCritical,
       "globalStatusOk": globalStatusOk,
       "softQuotaExceeded": softQuotaExceeded,
       "softQuotaNormal": softQuotaNormal,
       "autosupportSendError": autosupportSendError,
       "autosupportConfigurationError": autosupportConfigurationError,
       "autosupportSent": autosupportSent,
       "upsLinePowerOff": upsLinePowerOff,
       "upsBatteryCritical": upsBatteryCritical,
       "upsShuttingDown": upsShuttingDown,
       "upsBatteryWarning": upsBatteryWarning,
       "upsLinePowerRetored": upsLinePowerRetored,
       "appEmergency": appEmergency,
       "appAlert": appAlert,
       "appCritical": appCritical,
       "appError": appError,
       "appWarning": appWarning,
       "appNotice": appNotice,
       "appInfo": appInfo,
       "appTrap": appTrap,
       "alfFilewrap": alfFilewrap,
       "alfFileSaved": alfFileSaved,
       "alfFileNearlyFull": alfFileNearlyFull,
       "quotaExceeded": quotaExceeded,
       "quotaNormal": quotaNormal,
       "waflDirNearlyFull": waflDirNearlyFull,
       "waflDirFull": waflDirFull,
       "eccSummary": eccSummary,
       "eccMasked": eccMasked,
       "ftpdError": ftpdError,
       "ftpdMaxConnNotice": ftpdMaxConnNotice,
       "ftpdMaxConnThresholdNotice": ftpdMaxConnThresholdNotice,
       "scsitgtFCPLinkBreak": scsitgtFCPLinkBreak,
       "scsitgtPartnerPathMisconfigured": scsitgtPartnerPathMisconfigured,
       "scsitgtThrottleNotice": scsitgtThrottleNotice,
       "vifPrimaryLinkFailed": vifPrimaryLinkFailed,
       "vifAllLinksFailed": vifAllLinksFailed,
       "vfStopped": vfStopped,
       "vfStarted": vfStarted,
       "vscanVirusDetectedError": vscanVirusDetectedError,
       "vscanDisConnection": vscanDisConnection,
       "vscanConfigurationChange": vscanConfigurationChange,
       "vscanConnection": vscanConnection,
       "vscanServerUpgrade": vscanServerUpgrade,
       "volumeRestrictedByMirrorBigIo": volumeRestrictedByMirrorBigIo,
       "volumeInconsistentUmount": volumeInconsistentUmount,
       "volumeStateChanged": volumeStateChanged,
       "volumeOnline": volumeOnline,
       "rmcCardNeedsReplacement": rmcCardNeedsReplacement,
       "rmcCardMissingCables": rmcCardMissingCables,
       "volumeRemoteUnreachable": volumeRemoteUnreachable,
       "volumeRemoteOk": volumeRemoteOk,
       "volumeRemoteRestored": volumeRemoteRestored,
       "volumeRemoteRestoreBegin": volumeRemoteRestoreBegin,
       "volumeRestrictedRootConflict": volumeRestrictedRootConflict,
       "volumeOfflineTooBig": volumeOfflineTooBig,
       "volumeOffline": volumeOffline,
       "volumeRestricted": volumeRestricted,
       "volumeDegradedDirty": volumeDegradedDirty,
       "volumeError": volumeError,
       "snapmirrorSyncFailed": snapmirrorSyncFailed,
       "snapmirrorSyncOk": snapmirrorSyncOk,
       "chassisTemperatureShutdown": chassisTemperatureShutdown,
       "chassisTemperatureWarning": chassisTemperatureWarning,
       "chassisTemperatureUnknown": chassisTemperatureUnknown,
       "chassisTemperatureOk": chassisTemperatureOk,
       "chassisCPUFanStopped": chassisCPUFanStopped,
       "chassisCPUFanSlow": chassisCPUFanSlow,
       "chassisCPUFanOk": chassisCPUFanOk,
       "chassisPowerSuppliesFailed": chassisPowerSuppliesFailed,
       "chassisPowerSupplyDegraded": chassisPowerSupplyDegraded,
       "chassisPowerSupplyFailed": chassisPowerSupplyFailed,
       "chassisPowerSupplyRemoved": chassisPowerSupplyRemoved,
       "chassisPowerSupplyOff": chassisPowerSupplyOff,
       "chassisPowerSuppliesOk": chassisPowerSuppliesOk,
       "chassisPowerSupplyOk": chassisPowerSupplyOk,
       "chassisPowerDegraded": chassisPowerDegraded,
       "chassisPowerOk": chassisPowerOk,
       "chassisFanDegraded": chassisFanDegraded,
       "chassisFanRemoved": chassisFanRemoved,
       "chassisFanStopped": chassisFanStopped,
       "chassisFanWarning": chassisFanWarning,
       "chassisFanOk": chassisFanOk,
       "writeVerificationFailed": writeVerificationFailed,
       "domainControllerDisconnect": domainControllerDisconnect,
       "dcPasswdChangeFailed": dcPasswdChangeFailed,
       "domainControllerConnected": domainControllerConnected,
       "plexFailed": plexFailed,
       "plexOffline": plexOffline,
       "shelfSESElectronicsFailed": shelfSESElectronicsFailed,
       "shelfSESElectronicsInfo": shelfSESElectronicsInfo,
       "shelfIFModuleFailed": shelfIFModuleFailed,
       "shelfIFModuleWarning": shelfIFModuleWarning,
       "shelfIFModuleInfo": shelfIFModuleInfo,
       "maxDirSizeAlert": maxDirSizeAlert,
       "maxDirSizeWarning": maxDirSizeWarning,
       "cifsStatsExhaustMemCtrlBlk": cifsStatsExhaustMemCtrlBlk,
       "chassisPSRemovedxMinShutdown": chassisPSRemovedxMinShutdown,
       "chassisPSUsMismatch": chassisPSUsMismatch,
       "chassisFanFailxMinShutdown": chassisFanFailxMinShutdown,
       "chassisPSUwrongInput": chassisPSUwrongInput,
       "powerSupplyFanFailxMinShutdown": powerSupplyFanFailxMinShutdown,
       "remoteSystemMgtAlert": remoteSystemMgtAlert,
       "remoteSystemMgmtWarning": remoteSystemMgmtWarning,
       "remoteSystemMgmtNotification": remoteSystemMgmtNotification,
       "remoteSystemMgmtPeriodic": remoteSystemMgmtPeriodic,
       "remotesystemMgmtTest": remotesystemMgmtTest,
       "diskMultipathOneSwitch": diskMultipathOneSwitch,
       "diskMultipathNoTakeover": diskMultipathNoTakeover,
       "diskMultipathWarning": diskMultipathWarning,
       "driveDisableErr": driveDisableErr,
       "hbaOfflineInformation": hbaOfflineInformation,
       "lunSnapRestoreStatus": lunSnapRestoreStatus,
       "lunCloneCreate": lunCloneCreate,
       "lunCloneSplitStart": lunCloneSplitStart,
       "lunCloneSplitComplete": lunCloneSplitComplete,
       "flexCloneSplitStart": flexCloneSplitStart,
       "flexCloneSplitComplete": flexCloneSplitComplete,
       "volumeCloneCreate": volumeCloneCreate,
       "snapAutoDelete": snapAutoDelete,
       "volumeAutogrow": volumeAutogrow,
       "netapp1": netapp1,
       "product": product,
       "productType": productType,
       "productVersion": productVersion,
       "productId": productId,
       "productVendor": productVendor,
       "productModel": productModel,
       "productFirmwareVersion": productFirmwareVersion,
       "productGuiUrl": productGuiUrl,
       "productApiUrl": productApiUrl,
       "productSerialNum": productSerialNum,
       "productPartnerSerialNum": productPartnerSerialNum,
       "productCPUArch": productCPUArch,
       "productTrapData": productTrapData,
       "productMachineType": productMachineType,
       "sysStat": sysStat,
       "cpu": cpu,
       "cpuUpTime": cpuUpTime,
       "cpuBusyTime": cpuBusyTime,
       "cpuBusyTimePerCent": cpuBusyTimePerCent,
       "cpuIdleTime": cpuIdleTime,
       "cpuIdleTimePerCent": cpuIdleTimePerCent,
       "cpuCount": cpuCount,
       "cpuSwitchInvocations": cpuSwitchInvocations,
       "cpuContextSwitches": cpuContextSwitches,
       "cpuInterrupts": cpuInterrupts,
       "cpuNonCPInterrupts": cpuNonCPInterrupts,
       "cpuCPInterruptPercent": cpuCPInterruptPercent,
       "cpuNonCPInterruptPercent": cpuNonCPInterruptPercent,
       "cpuTotalDomainSwitches": cpuTotalDomainSwitches,
       "misc": misc,
       "miscNfsOps": miscNfsOps,
       "miscNetRcvdKB": miscNetRcvdKB,
       "miscNetSentKB": miscNetSentKB,
       "miscGlobalStatus": miscGlobalStatus,
       "miscHighNfsOps": miscHighNfsOps,
       "miscLowNfsOps": miscLowNfsOps,
       "miscHighCifsOps": miscHighCifsOps,
       "miscLowCifsOps": miscLowCifsOps,
       "miscHighHttpOps": miscHighHttpOps,
       "miscLowHttpOps": miscLowHttpOps,
       "miscHighNetRcvdBytes": miscHighNetRcvdBytes,
       "miscLowNetRcvdBytes": miscLowNetRcvdBytes,
       "miscHighNetSentBytes": miscHighNetSentBytes,
       "miscLowNetSentBytes": miscLowNetSentBytes,
       "miscHighDiskReadBytes": miscHighDiskReadBytes,
       "miscLowDiskReadBytes": miscLowDiskReadBytes,
       "miscHighDiskWriteBytes": miscHighDiskWriteBytes,
       "miscLowDiskWriteBytes": miscLowDiskWriteBytes,
       "miscHighTapeReadBytes": miscHighTapeReadBytes,
       "miscLowTapeReadBytes": miscLowTapeReadBytes,
       "miscHighTapeWriteBytes": miscHighTapeWriteBytes,
       "miscLowTapeWriteBytes": miscLowTapeWriteBytes,
       "miscCacheAge": miscCacheAge,
       "miscCorrectedMachineChecks": miscCorrectedMachineChecks,
       "miscGlobalStatusMessage": miscGlobalStatusMessage,
       "miscWindowsSetupWizardVersion": miscWindowsSetupWizardVersion,
       "misc64NfsOps": misc64NfsOps,
       "misc64CifsOps": misc64CifsOps,
       "misc64HttpOps": misc64HttpOps,
       "misc64NetRcvdBytes": misc64NetRcvdBytes,
       "misc64NetSentBytes": misc64NetSentBytes,
       "misc64DiskReadBytes": misc64DiskReadBytes,
       "misc64DiskWriteBytes": misc64DiskWriteBytes,
       "misc64TapeReadBytes": misc64TapeReadBytes,
       "misc64TapeWriteBytes": misc64TapeWriteBytes,
       "cf": cf,
       "cfSettings": cfSettings,
       "cfState": cfState,
       "cfCannotTakeoverCause": cfCannotTakeoverCause,
       "cfPartnerStatus": cfPartnerStatus,
       "cfPartnerLastStatusUpdate": cfPartnerLastStatusUpdate,
       "cfPartnerName": cfPartnerName,
       "cfPartnerSysid": cfPartnerSysid,
       "cfInterconnectStatus": cfInterconnectStatus,
       "environment": environment,
       "envOverTemperature": envOverTemperature,
       "envFailedFanCount": envFailedFanCount,
       "envFailedFanMessage": envFailedFanMessage,
       "envFailedPowerSupplyCount": envFailedPowerSupplyCount,
       "envFailedPowerSupplyMessage": envFailedPowerSupplyMessage,
       "nvram": nvram,
       "nvramBatteryStatus": nvramBatteryStatus,
       "cp": cp,
       "cpTime": cpTime,
       "cpFromTimerOps": cpFromTimerOps,
       "cpFromSnapshotOps": cpFromSnapshotOps,
       "cpFromLowWaterOps": cpFromLowWaterOps,
       "cpFromHighWaterOps": cpFromHighWaterOps,
       "cpFromLogFullOps": cpFromLogFullOps,
       "cpFromCpOps": cpFromCpOps,
       "cpTotalOps": cpTotalOps,
       "cpFromFlushOps": cpFromFlushOps,
       "cpFromSyncOps": cpFromSyncOps,
       "cpFromLowVbufOps": cpFromLowVbufOps,
       "cpFromCpDeferredOps": cpFromCpDeferredOps,
       "cpFromLowDatavecsOps": cpFromLowDatavecsOps,
       "autosupport": autosupport,
       "autosupportStatus": autosupportStatus,
       "autosupportStatusMessage": autosupportStatusMessage,
       "autosupportSuccessfulSends": autosupportSuccessfulSends,
       "autosupportFailedSends": autosupportFailedSends,
       "nfs": nfs,
       "curNfs": curNfs,
       "rpcServ": rpcServ,
       "rpcCalls": rpcCalls,
       "rpcBadCalls": rpcBadCalls,
       "rpcNullRecvs": rpcNullRecvs,
       "rpcBadLens": rpcBadLens,
       "rpcServXDRCalls": rpcServXDRCalls,
       "rcpTcpCalls": rcpTcpCalls,
       "rcpTcpBadCalls": rcpTcpBadCalls,
       "rcpTcpNullRecvs": rcpTcpNullRecvs,
       "rcpTcpBadLens": rcpTcpBadLens,
       "rcpTcpServXDRCalls": rcpTcpServXDRCalls,
       "rpcUdpCalls": rpcUdpCalls,
       "rpcUdpBadCalls": rpcUdpBadCalls,
       "rpcUdpNullRecvs": rpcUdpNullRecvs,
       "rpcUdpBadLens": rpcUdpBadLens,
       "rpcUdpServXDRCalls": rpcUdpServXDRCalls,
       "nfsServ": nfsServ,
       "nfsCalls": nfsCalls,
       "nfsServBadCalls": nfsServBadCalls,
       "nfsV2": nfsV2,
       "v2Calls": v2Calls,
       "v2cNulls": v2cNulls,
       "v2cGetattrs": v2cGetattrs,
       "v2cSetattrs": v2cSetattrs,
       "v2cRoots": v2cRoots,
       "v2cLookups": v2cLookups,
       "v2cReadlinks": v2cReadlinks,
       "v2cReads": v2cReads,
       "v2cWrcaches": v2cWrcaches,
       "v2cWrites": v2cWrites,
       "v2cCreates": v2cCreates,
       "v2cRemoves": v2cRemoves,
       "v2cRenames": v2cRenames,
       "v2cLinks": v2cLinks,
       "v2cSymlinks": v2cSymlinks,
       "v2cMkdirs": v2cMkdirs,
       "v2cRmdirs": v2cRmdirs,
       "v2cReaddirs": v2cReaddirs,
       "v2cStatfss": v2cStatfss,
       "v2Percent": v2Percent,
       "v2pNulls": v2pNulls,
       "v2pGetattrs": v2pGetattrs,
       "v2pSetattrs": v2pSetattrs,
       "v2pRoots": v2pRoots,
       "v2pLookups": v2pLookups,
       "v2pReadlinks": v2pReadlinks,
       "v2pReads": v2pReads,
       "v2pWrcaches": v2pWrcaches,
       "v2pWrites": v2pWrites,
       "v2pCreates": v2pCreates,
       "v2pRemoves": v2pRemoves,
       "v2pRenames": v2pRenames,
       "v2pLinks": v2pLinks,
       "v2pSymlinks": v2pSymlinks,
       "v2pMkdirs": v2pMkdirs,
       "v2pRmdirs": v2pRmdirs,
       "v2pReaddirs": v2pReaddirs,
       "v2pStatfss": v2pStatfss,
       "v2CachedCalls": v2CachedCalls,
       "v2ccNulls": v2ccNulls,
       "v2ccGetattrs": v2ccGetattrs,
       "v2ccSetattrs": v2ccSetattrs,
       "v2ccRoots": v2ccRoots,
       "v2ccLookups": v2ccLookups,
       "v2ccReadlinks": v2ccReadlinks,
       "v2ccReads": v2ccReads,
       "v2ccWrcaches": v2ccWrcaches,
       "v2ccWrites": v2ccWrites,
       "v2ccCreates": v2ccCreates,
       "v2ccRemoves": v2ccRemoves,
       "v2ccRenames": v2ccRenames,
       "v2ccLinks": v2ccLinks,
       "v2ccSymlinks": v2ccSymlinks,
       "v2ccMkdirs": v2ccMkdirs,
       "v2ccRmdirs": v2ccRmdirs,
       "v2ccReaddirs": v2ccReaddirs,
       "v2ccStatfss": v2ccStatfss,
       "v2CachedPerCent": v2CachedPerCent,
       "v2cpNulls": v2cpNulls,
       "v2cpGetattrs": v2cpGetattrs,
       "v2cpSetattrs": v2cpSetattrs,
       "v2cpRoots": v2cpRoots,
       "v2cpLookups": v2cpLookups,
       "v2cpReadlinks": v2cpReadlinks,
       "v2cpReads": v2cpReads,
       "v2cpWrcaches": v2cpWrcaches,
       "v2cpWrites": v2cpWrites,
       "v2cpCreates": v2cpCreates,
       "v2cpRemoves": v2cpRemoves,
       "v2cpRenames": v2cpRenames,
       "v2cpLinks": v2cpLinks,
       "v2cpSymlinks": v2cpSymlinks,
       "v2cpMkdirs": v2cpMkdirs,
       "v2cpRmdirs": v2cpRmdirs,
       "v2cpReaddirs": v2cpReaddirs,
       "v2cpStatfss": v2cpStatfss,
       "nfsV3": nfsV3,
       "v3Calls": v3Calls,
       "v3cNulls": v3cNulls,
       "v3cGetattrs": v3cGetattrs,
       "v3cSetattrs": v3cSetattrs,
       "v3cLookups": v3cLookups,
       "v3cAccesss": v3cAccesss,
       "v3cReadlinks": v3cReadlinks,
       "v3cReads": v3cReads,
       "v3cWrites": v3cWrites,
       "v3cCreates": v3cCreates,
       "v3cMkdirs": v3cMkdirs,
       "v3cSymlinks": v3cSymlinks,
       "v3cMknods": v3cMknods,
       "v3cRemoves": v3cRemoves,
       "v3cRmdirs": v3cRmdirs,
       "v3cRenames": v3cRenames,
       "v3cLinks": v3cLinks,
       "v3cReaddirs": v3cReaddirs,
       "v3cReaddirPluss": v3cReaddirPluss,
       "v3cFsstats": v3cFsstats,
       "v3cFsinfos": v3cFsinfos,
       "v3cPathconfs": v3cPathconfs,
       "v3cCommits": v3cCommits,
       "v3Percent": v3Percent,
       "v3pNulls": v3pNulls,
       "v3pGetattrs": v3pGetattrs,
       "v3pSetattrs": v3pSetattrs,
       "v3pLookups": v3pLookups,
       "v3pAccesss": v3pAccesss,
       "v3pReadlinks": v3pReadlinks,
       "v3pReads": v3pReads,
       "v3pWrites": v3pWrites,
       "v3pCreates": v3pCreates,
       "v3pMkdirs": v3pMkdirs,
       "v3pSymlinks": v3pSymlinks,
       "v3pMknods": v3pMknods,
       "v3pRemoves": v3pRemoves,
       "v3pRmdirs": v3pRmdirs,
       "v3pRenames": v3pRenames,
       "v3pLinks": v3pLinks,
       "v3pReaddirs": v3pReaddirs,
       "v3pReaddirPluss": v3pReaddirPluss,
       "v3pFsstats": v3pFsstats,
       "v3pFsinfos": v3pFsinfos,
       "v3pPathconfs": v3pPathconfs,
       "v3pCommits": v3pCommits,
       "v3CachedCalls": v3CachedCalls,
       "v3ccNulls": v3ccNulls,
       "v3ccGetattrs": v3ccGetattrs,
       "v3ccSetattrs": v3ccSetattrs,
       "v3ccLookups": v3ccLookups,
       "v3ccAccesss": v3ccAccesss,
       "v3ccReadlinks": v3ccReadlinks,
       "v3ccReads": v3ccReads,
       "v3ccWrites": v3ccWrites,
       "v3ccCreates": v3ccCreates,
       "v3ccMkdirs": v3ccMkdirs,
       "v3ccSymlinks": v3ccSymlinks,
       "v3ccMknods": v3ccMknods,
       "v3ccRemoves": v3ccRemoves,
       "v3ccRmdirs": v3ccRmdirs,
       "v3ccRenames": v3ccRenames,
       "v3ccLinks": v3ccLinks,
       "v3ccReaddirs": v3ccReaddirs,
       "v3ccReaddirPluss": v3ccReaddirPluss,
       "v3ccFsstats": v3ccFsstats,
       "v3ccFsinfos": v3ccFsinfos,
       "v3ccPathconfs": v3ccPathconfs,
       "v3ccCommits": v3ccCommits,
       "v3CachedPerCent": v3CachedPerCent,
       "v3cpNulls": v3cpNulls,
       "v3cpGetattrs": v3cpGetattrs,
       "v3cpSetattrs": v3cpSetattrs,
       "v3cpLookups": v3cpLookups,
       "v3cpAccesss": v3cpAccesss,
       "v3cpReadlinks": v3cpReadlinks,
       "v3cpReads": v3cpReads,
       "v3cpWrites": v3cpWrites,
       "v3cpCreates": v3cpCreates,
       "v3cpMkdirs": v3cpMkdirs,
       "v3cpSymlinks": v3cpSymlinks,
       "v3cpMknods": v3cpMknods,
       "v3cpRemoves": v3cpRemoves,
       "v3cpRmdirs": v3cpRmdirs,
       "v3cpRenames": v3cpRenames,
       "v3cpLinks": v3cpLinks,
       "v3cpReaddirs": v3cpReaddirs,
       "v3cpReaddirPluss": v3cpReaddirPluss,
       "v3cpFsstats": v3cpFsstats,
       "v3cpFsinfos": v3cpFsinfos,
       "v3cpPathconfs": v3cpPathconfs,
       "v3cpCommits": v3cpCommits,
       "replyCache": replyCache,
       "rcInProgressHits": rcInProgressHits,
       "rcDelayHits": rcDelayHits,
       "rcMisses": rcMisses,
       "rcNonIdemDoneHits": rcNonIdemDoneHits,
       "rcNonIdemNotDoneHits": rcNonIdemNotDoneHits,
       "rcTcpInProgressHits": rcTcpInProgressHits,
       "rcTcpDelayHits": rcTcpDelayHits,
       "rcTcpMisses": rcTcpMisses,
       "rcTcpNonIdemDoneHits": rcTcpNonIdemDoneHits,
       "rcTcpNonIdemNotDoneHits": rcTcpNonIdemNotDoneHits,
       "rcUdpInProgressHits": rcUdpInProgressHits,
       "rcUdpDelayHits": rcUdpDelayHits,
       "rcUdpMisses": rcUdpMisses,
       "rcUdpNonIdemDoneHits": rcUdpNonIdemDoneHits,
       "rcUdpNonIdemNotDoneHits": rcUdpNonIdemNotDoneHits,
       "nfsrwStats": nfsrwStats,
       "v2ReadStats": v2ReadStats,
       "v2Read512Calls": v2Read512Calls,
       "v2Read1KCalls": v2Read1KCalls,
       "v2Read2KCalls": v2Read2KCalls,
       "v2Read4KCalls": v2Read4KCalls,
       "v2Read8KCalls": v2Read8KCalls,
       "v2Read16KCalls": v2Read16KCalls,
       "v2Read32KCalls": v2Read32KCalls,
       "v2Read64KCalls": v2Read64KCalls,
       "v2Read128KCalls": v2Read128KCalls,
       "v2WriteStats": v2WriteStats,
       "v2Write512Calls": v2Write512Calls,
       "v2Write1KCalls": v2Write1KCalls,
       "v2Write2KCalls": v2Write2KCalls,
       "v2Write4KCalls": v2Write4KCalls,
       "v2Write8KCalls": v2Write8KCalls,
       "v2Write16KCalls": v2Write16KCalls,
       "v2Write32KCalls": v2Write32KCalls,
       "v2Write64KCalls": v2Write64KCalls,
       "v2Write128KCalls": v2Write128KCalls,
       "v3ReadStats": v3ReadStats,
       "v3Read512Calls": v3Read512Calls,
       "v3Read1KCalls": v3Read1KCalls,
       "v3Read2KCalls": v3Read2KCalls,
       "v3Read4KCalls": v3Read4KCalls,
       "v3Read8KCalls": v3Read8KCalls,
       "v3Read16KCalls": v3Read16KCalls,
       "v3Read32KCalls": v3Read32KCalls,
       "v3Read64KCalls": v3Read64KCalls,
       "v3Read128KCalls": v3Read128KCalls,
       "v3WriteStats": v3WriteStats,
       "v3Write512Calls": v3Write512Calls,
       "v3Write1KCalls": v3Write1KCalls,
       "v3Write2KCalls": v3Write2KCalls,
       "v3Write4KCalls": v3Write4KCalls,
       "v3Write8KCalls": v3Write8KCalls,
       "v3Write16KCalls": v3Write16KCalls,
       "v3Write32KCalls": v3Write32KCalls,
       "v3Write64KCalls": v3Write64KCalls,
       "v3Write128KCalls": v3Write128KCalls,
       "nfsPerClient": nfsPerClient,
       "pclTable": pclTable,
       "pclEntry": pclEntry,
       "pclIpAddr": pclIpAddr,
       "pclRpcCalls": pclRpcCalls,
       "pclRpcBadCalls": pclRpcBadCalls,
       "pclRpcNullRecvs": pclRpcNullRecvs,
       "pclRpcBadLens": pclRpcBadLens,
       "pclRpcServXDRCalls": pclRpcServXDRCalls,
       "pclNfsCalls": pclNfsCalls,
       "pclNfsServBadCalls": pclNfsServBadCalls,
       "pclNfsV2Nulls": pclNfsV2Nulls,
       "pclNfsV2Getattrs": pclNfsV2Getattrs,
       "pclNfsV2Setattrs": pclNfsV2Setattrs,
       "pclNfsV2Roots": pclNfsV2Roots,
       "pclNfsV2Lookups": pclNfsV2Lookups,
       "pclNfsV2Readlinks": pclNfsV2Readlinks,
       "pclNfsV2Reads": pclNfsV2Reads,
       "pclNfsV2Wrcaches": pclNfsV2Wrcaches,
       "pclNfsV2Writes": pclNfsV2Writes,
       "pclNfsV2Creates": pclNfsV2Creates,
       "pclNfsV2Removes": pclNfsV2Removes,
       "pclNfsV2Renames": pclNfsV2Renames,
       "pclNfsV2Links": pclNfsV2Links,
       "pclNfsV2Symlinks": pclNfsV2Symlinks,
       "pclNfsV2Mkdirs": pclNfsV2Mkdirs,
       "pclNfsV2Rmdirs": pclNfsV2Rmdirs,
       "pclNfsV2Readdirs": pclNfsV2Readdirs,
       "pclNfsV2Statfss": pclNfsV2Statfss,
       "pclNfsV3Nulls": pclNfsV3Nulls,
       "pclNfsV3Getattrs": pclNfsV3Getattrs,
       "pclNfsV3Setattrs": pclNfsV3Setattrs,
       "pclNfsV3Lookups": pclNfsV3Lookups,
       "pclNfsV3Accesss": pclNfsV3Accesss,
       "pclNfsV3Readlinks": pclNfsV3Readlinks,
       "pclNfsV3Reads": pclNfsV3Reads,
       "pclNfsV3Writes": pclNfsV3Writes,
       "pclNfsV3Creates": pclNfsV3Creates,
       "pclNfsV3Mkdirs": pclNfsV3Mkdirs,
       "pclNfsV3Symlinks": pclNfsV3Symlinks,
       "pclNfsV3Mknods": pclNfsV3Mknods,
       "pclNfsV3Removes": pclNfsV3Removes,
       "pclNfsV3Rmdirs": pclNfsV3Rmdirs,
       "pclNfsV3Renames": pclNfsV3Renames,
       "pclNfsV3Links": pclNfsV3Links,
       "pclNfsV3Readdirs": pclNfsV3Readdirs,
       "pclNfsV3ReaddirPluss": pclNfsV3ReaddirPluss,
       "pclNfsV3Fsstats": pclNfsV3Fsstats,
       "pclNfsV3Fsinfos": pclNfsV3Fsinfos,
       "pclNfsV3Pathconfs": pclNfsV3Pathconfs,
       "pclNfsV3Commits": pclNfsV3Commits,
       "pclPerCent": pclPerCent,
       "pclNfsV2NullPerCent": pclNfsV2NullPerCent,
       "pclNfsV2GetattrPerCent": pclNfsV2GetattrPerCent,
       "pclNfsV2SetattrPerCent": pclNfsV2SetattrPerCent,
       "pclNfsV2RootPerCent": pclNfsV2RootPerCent,
       "pclNfsV2LookupPerCent": pclNfsV2LookupPerCent,
       "pclNfsV2ReadlinkPerCent": pclNfsV2ReadlinkPerCent,
       "pclNfsV2ReadPerCent": pclNfsV2ReadPerCent,
       "pclNfsV2WrcachePerCent": pclNfsV2WrcachePerCent,
       "pclNfsV2WritePerCent": pclNfsV2WritePerCent,
       "pclNfsV2CreatePerCent": pclNfsV2CreatePerCent,
       "pclNfsV2RemovePerCent": pclNfsV2RemovePerCent,
       "pclNfsV2RenamePerCent": pclNfsV2RenamePerCent,
       "pclNfsV2LinkPerCent": pclNfsV2LinkPerCent,
       "pclNfsV2SymlinkPerCent": pclNfsV2SymlinkPerCent,
       "pclNfsV2MkdirPerCent": pclNfsV2MkdirPerCent,
       "pclNfsV2RmdirPerCent": pclNfsV2RmdirPerCent,
       "pclNfsV2ReaddirPerCent": pclNfsV2ReaddirPerCent,
       "pclNfsV2StatfsPerCent": pclNfsV2StatfsPerCent,
       "pclNfsV3NullPerCent": pclNfsV3NullPerCent,
       "pclNfsV3GetattrPerCent": pclNfsV3GetattrPerCent,
       "pclNfsV3SetattrPerCent": pclNfsV3SetattrPerCent,
       "pclNfsV3LookupPerCent": pclNfsV3LookupPerCent,
       "pclNfsV3AccessPerCent": pclNfsV3AccessPerCent,
       "pclNfsV3ReadlinkPerCent": pclNfsV3ReadlinkPerCent,
       "pclNfsV3ReadPerCent": pclNfsV3ReadPerCent,
       "pclNfsV3WritePerCent": pclNfsV3WritePerCent,
       "pclNfsV3CreatePerCent": pclNfsV3CreatePerCent,
       "pclNfsV3MkdirPerCent": pclNfsV3MkdirPerCent,
       "pclNfsV3SymlinkPerCent": pclNfsV3SymlinkPerCent,
       "pclNfsV3MknodPerCent": pclNfsV3MknodPerCent,
       "pclNfsV3RemovePerCent": pclNfsV3RemovePerCent,
       "pclNfsV3RmdirPerCent": pclNfsV3RmdirPerCent,
       "pclNfsV3RenamePerCent": pclNfsV3RenamePerCent,
       "pclNfsV3LinkPerCent": pclNfsV3LinkPerCent,
       "pclNfsV3ReaddirPerCent": pclNfsV3ReaddirPerCent,
       "pclNfsV3ReaddirPlusPerCent": pclNfsV3ReaddirPlusPerCent,
       "pclNfsV3FsstatPerCent": pclNfsV3FsstatPerCent,
       "pclNfsV3FsinfoPerCent": pclNfsV3FsinfoPerCent,
       "pclNfsV3PathconfPerCent": pclNfsV3PathconfPerCent,
       "pclNfsV3CommitPerCent": pclNfsV3CommitPerCent,
       "pclNfsV2Read512Calls": pclNfsV2Read512Calls,
       "pclNfsV2Read1KCalls": pclNfsV2Read1KCalls,
       "pclNfsV2Read2KCalls": pclNfsV2Read2KCalls,
       "pclNfsV2Read4KCalls": pclNfsV2Read4KCalls,
       "pclNfsV2Read8KCalls": pclNfsV2Read8KCalls,
       "pclNfsV2Read16KCalls": pclNfsV2Read16KCalls,
       "pclNfsV2Read32KCalls": pclNfsV2Read32KCalls,
       "pclNfsV2Read64KCalls": pclNfsV2Read64KCalls,
       "pclNfsV2Read128KCalls": pclNfsV2Read128KCalls,
       "pclNfsV2Write512Calls": pclNfsV2Write512Calls,
       "pclNfsV2Write1KCalls": pclNfsV2Write1KCalls,
       "pclNfsV2Write2KCalls": pclNfsV2Write2KCalls,
       "pclNfsV2Write4KCalls": pclNfsV2Write4KCalls,
       "pclNfsV2Write8KCalls": pclNfsV2Write8KCalls,
       "pclNfsV2Write16KCalls": pclNfsV2Write16KCalls,
       "pclNfsV2Write32KCalls": pclNfsV2Write32KCalls,
       "pclNfsV2Write64KCalls": pclNfsV2Write64KCalls,
       "pclNfsV2Write128KCalls": pclNfsV2Write128KCalls,
       "pclNfsV3Read512Calls": pclNfsV3Read512Calls,
       "pclNfsV3Read1KCalls": pclNfsV3Read1KCalls,
       "pclNfsV3Read2KCalls": pclNfsV3Read2KCalls,
       "pclNfsV3Read4KCalls": pclNfsV3Read4KCalls,
       "pclNfsV3Read8KCalls": pclNfsV3Read8KCalls,
       "pclNfsV3Read16KCalls": pclNfsV3Read16KCalls,
       "pclNfsV3Read32KCalls": pclNfsV3Read32KCalls,
       "pclNfsV3Read64KCalls": pclNfsV3Read64KCalls,
       "pclNfsV3Read128KCalls": pclNfsV3Read128KCalls,
       "pclNfsV3Write512Calls": pclNfsV3Write512Calls,
       "pclNfsV3Write1KCalls": pclNfsV3Write1KCalls,
       "pclNfsV3Write2KCalls": pclNfsV3Write2KCalls,
       "pclNfsV3Write4KCalls": pclNfsV3Write4KCalls,
       "pclNfsV3Write8KCalls": pclNfsV3Write8KCalls,
       "pclNfsV3Write16KCalls": pclNfsV3Write16KCalls,
       "pclNfsV3Write32KCalls": pclNfsV3Write32KCalls,
       "pclNfsV3Write64KCalls": pclNfsV3Write64KCalls,
       "pclNfsV3Write128KCalls": pclNfsV3Write128KCalls,
       "pclNumber": pclNumber,
       "totNfs": totNfs,
       "trpcServ": trpcServ,
       "trpcCalls": trpcCalls,
       "trpcBadCalls": trpcBadCalls,
       "trpcNullRecvs": trpcNullRecvs,
       "trpcBadLens": trpcBadLens,
       "trpcServXDRCalls": trpcServXDRCalls,
       "tnfsServ": tnfsServ,
       "tnfsCalls": tnfsCalls,
       "tnfsServBadCalls": tnfsServBadCalls,
       "tnfsV2": tnfsV2,
       "tv2Calls": tv2Calls,
       "tv2cNulls": tv2cNulls,
       "tv2cGetattrs": tv2cGetattrs,
       "tv2cSetattrs": tv2cSetattrs,
       "tv2cRoots": tv2cRoots,
       "tv2cLookups": tv2cLookups,
       "tv2cReadlinks": tv2cReadlinks,
       "tv2cReads": tv2cReads,
       "tv2cWrcaches": tv2cWrcaches,
       "tv2cWrites": tv2cWrites,
       "tv2cCreates": tv2cCreates,
       "tv2cRemoves": tv2cRemoves,
       "tv2cRenames": tv2cRenames,
       "tv2cLinks": tv2cLinks,
       "tv2cSymlinks": tv2cSymlinks,
       "tv2cMkdirs": tv2cMkdirs,
       "tv2cRmdirs": tv2cRmdirs,
       "tv2cReaddirs": tv2cReaddirs,
       "tv2cStatfss": tv2cStatfss,
       "tv2Percent": tv2Percent,
       "tv2pNulls": tv2pNulls,
       "tv2pGetattrs": tv2pGetattrs,
       "tv2pSetattrs": tv2pSetattrs,
       "tv2pRoots": tv2pRoots,
       "tv2pLookups": tv2pLookups,
       "tv2pReadlinks": tv2pReadlinks,
       "tv2pReads": tv2pReads,
       "tv2pWrcaches": tv2pWrcaches,
       "tv2pWrites": tv2pWrites,
       "tv2pCreates": tv2pCreates,
       "tv2pRemoves": tv2pRemoves,
       "tv2pRenames": tv2pRenames,
       "tv2pLinks": tv2pLinks,
       "tv2pSymlinks": tv2pSymlinks,
       "tv2pMkdirs": tv2pMkdirs,
       "tv2pRmdirs": tv2pRmdirs,
       "tv2pReaddirs": tv2pReaddirs,
       "tv2pStatfss": tv2pStatfss,
       "tv2CachedCalls": tv2CachedCalls,
       "tv2ccNulls": tv2ccNulls,
       "tv2ccGetattrs": tv2ccGetattrs,
       "tv2ccSetattrs": tv2ccSetattrs,
       "tv2ccRoots": tv2ccRoots,
       "tv2ccLookups": tv2ccLookups,
       "tv2ccReadlinks": tv2ccReadlinks,
       "tv2ccReads": tv2ccReads,
       "tv2ccWrcaches": tv2ccWrcaches,
       "tv2ccWrites": tv2ccWrites,
       "tv2ccCreates": tv2ccCreates,
       "tv2ccRemoves": tv2ccRemoves,
       "tv2ccRenames": tv2ccRenames,
       "tv2ccLinks": tv2ccLinks,
       "tv2ccSymlinks": tv2ccSymlinks,
       "tv2ccMkdirs": tv2ccMkdirs,
       "tv2ccRmdirs": tv2ccRmdirs,
       "tv2ccReaddirs": tv2ccReaddirs,
       "tv2ccStatfss": tv2ccStatfss,
       "tv2CachedPerCent": tv2CachedPerCent,
       "tv2cpNulls": tv2cpNulls,
       "tv2cpGetattrs": tv2cpGetattrs,
       "tv2cpSetattrs": tv2cpSetattrs,
       "tv2cpRoots": tv2cpRoots,
       "tv2cpLookups": tv2cpLookups,
       "tv2cpReadlinks": tv2cpReadlinks,
       "tv2cpReads": tv2cpReads,
       "tv2cpWrcaches": tv2cpWrcaches,
       "tv2cpWrites": tv2cpWrites,
       "tv2cpCreates": tv2cpCreates,
       "tv2cpRemoves": tv2cpRemoves,
       "tv2cpRenames": tv2cpRenames,
       "tv2cpLinks": tv2cpLinks,
       "tv2cpSymlinks": tv2cpSymlinks,
       "tv2cpMkdirs": tv2cpMkdirs,
       "tv2cpRmdirs": tv2cpRmdirs,
       "tv2cpReaddirs": tv2cpReaddirs,
       "tv2cpStatfss": tv2cpStatfss,
       "tnfsV3": tnfsV3,
       "tv3Calls": tv3Calls,
       "tv3cNulls": tv3cNulls,
       "tv3cGetattrs": tv3cGetattrs,
       "tv3cSetattrs": tv3cSetattrs,
       "tv3cLookups": tv3cLookups,
       "tv3cAccesss": tv3cAccesss,
       "tv3cReadlinks": tv3cReadlinks,
       "tv3cReads": tv3cReads,
       "tv3cWrites": tv3cWrites,
       "tv3cCreates": tv3cCreates,
       "tv3cMkdirs": tv3cMkdirs,
       "tv3cSymlinks": tv3cSymlinks,
       "tv3cMknods": tv3cMknods,
       "tv3cRemoves": tv3cRemoves,
       "tv3cRmdirs": tv3cRmdirs,
       "tv3cRenames": tv3cRenames,
       "tv3cLinks": tv3cLinks,
       "tv3cReaddirs": tv3cReaddirs,
       "tv3cReaddirPluss": tv3cReaddirPluss,
       "tv3cFsstats": tv3cFsstats,
       "tv3cFsinfos": tv3cFsinfos,
       "tv3cPathconfs": tv3cPathconfs,
       "tv3cCommits": tv3cCommits,
       "tv3Percent": tv3Percent,
       "tv3pNulls": tv3pNulls,
       "tv3pGetattrs": tv3pGetattrs,
       "tv3pSetattrs": tv3pSetattrs,
       "tv3pLookups": tv3pLookups,
       "tv3pAccesss": tv3pAccesss,
       "tv3pReadlinks": tv3pReadlinks,
       "tv3pReads": tv3pReads,
       "tv3pWrites": tv3pWrites,
       "tv3pCreates": tv3pCreates,
       "tv3pMkdirs": tv3pMkdirs,
       "tv3pSymlinks": tv3pSymlinks,
       "tv3pMknods": tv3pMknods,
       "tv3pRemoves": tv3pRemoves,
       "tv3pRmdirs": tv3pRmdirs,
       "tv3pRenames": tv3pRenames,
       "tv3pLinks": tv3pLinks,
       "tv3pReaddirs": tv3pReaddirs,
       "tv3pReaddirPluss": tv3pReaddirPluss,
       "tv3pFsstats": tv3pFsstats,
       "tv3pFsinfos": tv3pFsinfos,
       "tv3pPathconfs": tv3pPathconfs,
       "tv3pCommits": tv3pCommits,
       "tv3CachedCalls": tv3CachedCalls,
       "tv3ccNulls": tv3ccNulls,
       "tv3ccGetattrs": tv3ccGetattrs,
       "tv3ccSetattrs": tv3ccSetattrs,
       "tv3ccLookups": tv3ccLookups,
       "tv3ccAccesss": tv3ccAccesss,
       "tv3ccReadlinks": tv3ccReadlinks,
       "tv3ccReads": tv3ccReads,
       "tv3ccWrites": tv3ccWrites,
       "tv3ccCreates": tv3ccCreates,
       "tv3ccMkdirs": tv3ccMkdirs,
       "tv3ccSymlinks": tv3ccSymlinks,
       "tv3ccMknods": tv3ccMknods,
       "tv3ccRemoves": tv3ccRemoves,
       "tv3ccRmdirs": tv3ccRmdirs,
       "tv3ccRenames": tv3ccRenames,
       "tv3ccLinks": tv3ccLinks,
       "tv3ccReaddirs": tv3ccReaddirs,
       "tv3ccReaddirPluss": tv3ccReaddirPluss,
       "tv3ccFsstats": tv3ccFsstats,
       "tv3ccFsinfos": tv3ccFsinfos,
       "tv3ccPathconfs": tv3ccPathconfs,
       "tv3ccCommits": tv3ccCommits,
       "tv3CachedPerCent": tv3CachedPerCent,
       "tv3cpNulls": tv3cpNulls,
       "tv3cpGetattrs": tv3cpGetattrs,
       "tv3cpSetattrs": tv3cpSetattrs,
       "tv3cpLookups": tv3cpLookups,
       "tv3cpAccesss": tv3cpAccesss,
       "tv3cpReadlinks": tv3cpReadlinks,
       "tv3cpReads": tv3cpReads,
       "tv3cpWrites": tv3cpWrites,
       "tv3cpCreates": tv3cpCreates,
       "tv3cpMkdirs": tv3cpMkdirs,
       "tv3cpSymlinks": tv3cpSymlinks,
       "tv3cpMknods": tv3cpMknods,
       "tv3cpRemoves": tv3cpRemoves,
       "tv3cpRmdirs": tv3cpRmdirs,
       "tv3cpRenames": tv3cpRenames,
       "tv3cpLinks": tv3cpLinks,
       "tv3cpReaddirs": tv3cpReaddirs,
       "tv3cpReaddirPluss": tv3cpReaddirPluss,
       "tv3cpFsstats": tv3cpFsstats,
       "tv3cpFsinfos": tv3cpFsinfos,
       "tv3cpPathconfs": tv3cpPathconfs,
       "tv3cpCommits": tv3cpCommits,
       "treplyCache": treplyCache,
       "trcInProgressHits": trcInProgressHits,
       "trcDelayHits": trcDelayHits,
       "trcMisses": trcMisses,
       "trcNonIdemDoneHits": trcNonIdemDoneHits,
       "trcNonIdemNotDoneHits": trcNonIdemNotDoneHits,
       "trcTcpInProgressHits": trcTcpInProgressHits,
       "trcTcpDelayHits": trcTcpDelayHits,
       "trcTcpMisses": trcTcpMisses,
       "trcTcpNonIdemDoneHits": trcTcpNonIdemDoneHits,
       "trcTcpNonIdemNotDoneHits": trcTcpNonIdemNotDoneHits,
       "trcUdpInProgressHits": trcUdpInProgressHits,
       "trcUdpDelayHits": trcUdpDelayHits,
       "trcUdpMisses": trcUdpMisses,
       "trcUdpNonIdemDoneHits": trcUdpNonIdemDoneHits,
       "trcUdpNonIdemNotDoneHits": trcUdpNonIdemNotDoneHits,
       "tnfsrwStats": tnfsrwStats,
       "tv2ReadStats": tv2ReadStats,
       "tv2Read512Calls": tv2Read512Calls,
       "tv2Read1KCalls": tv2Read1KCalls,
       "tv2Read2KCalls": tv2Read2KCalls,
       "tv2Read4KCalls": tv2Read4KCalls,
       "tv2Read8KCalls": tv2Read8KCalls,
       "tv2Read16KCalls": tv2Read16KCalls,
       "tv2Read32KCalls": tv2Read32KCalls,
       "tv2Read64KCalls": tv2Read64KCalls,
       "tv2Read128KCalls": tv2Read128KCalls,
       "tv2WriteStats": tv2WriteStats,
       "tv2Write512Calls": tv2Write512Calls,
       "tv2Write1KCalls": tv2Write1KCalls,
       "tv2Write2KCalls": tv2Write2KCalls,
       "tv2Write4KCalls": tv2Write4KCalls,
       "tv2Write8KCalls": tv2Write8KCalls,
       "tv2Write16KCalls": tv2Write16KCalls,
       "tv2Write32KCalls": tv2Write32KCalls,
       "tv2Write64KCalls": tv2Write64KCalls,
       "tv2Write128KCalls": tv2Write128KCalls,
       "tv3ReadStats": tv3ReadStats,
       "tv3Read512Calls": tv3Read512Calls,
       "tv3Read1KCalls": tv3Read1KCalls,
       "tv3Read2KCalls": tv3Read2KCalls,
       "tv3Read4KCalls": tv3Read4KCalls,
       "tv3Read8KCalls": tv3Read8KCalls,
       "tv3Read16KCalls": tv3Read16KCalls,
       "tv3Read32KCalls": tv3Read32KCalls,
       "tv3Read64KCalls": tv3Read64KCalls,
       "tv3Read128KCalls": tv3Read128KCalls,
       "tv3WriteStats": tv3WriteStats,
       "tv3Write512Calls": tv3Write512Calls,
       "tv3Write1KCalls": tv3Write1KCalls,
       "tv3Write2KCalls": tv3Write2KCalls,
       "tv3Write4KCalls": tv3Write4KCalls,
       "tv3Write8KCalls": tv3Write8KCalls,
       "tv3Write16KCalls": tv3Write16KCalls,
       "tv3Write32KCalls": tv3Write32KCalls,
       "tv3Write64KCalls": tv3Write64KCalls,
       "tv3Write128KCalls": tv3Write128KCalls,
       "nfsOptions": nfsOptions,
       "nfsIsLicensed": nfsIsLicensed,
       "quota": quota,
       "quotaState": quotaState,
       "quotaInitPercent": quotaInitPercent,
       "qrTable": qrTable,
       "qrEntry": qrEntry,
       "qrIndex": qrIndex,
       "qrType": qrType,
       "qrId": qrId,
       "qrKBytesUsed": qrKBytesUsed,
       "qrKBytesLimit": qrKBytesLimit,
       "qrFilesUsed": qrFilesUsed,
       "qrFileLimit": qrFileLimit,
       "qrPathName": qrPathName,
       "qvStateTable": qvStateTable,
       "qvStateEntry": qvStateEntry,
       "qvStateVolume": qvStateVolume,
       "qvStateName": qvStateName,
       "qvStateStat": qvStateStat,
       "qvStateInitPercent": qvStateInitPercent,
       "qrVTable": qrVTable,
       "qrVEntry": qrVEntry,
       "qrVIndex": qrVIndex,
       "qrVType": qrVType,
       "qrVId": qrVId,
       "qrVKBytesUsed": qrVKBytesUsed,
       "qrVKBytesLimit": qrVKBytesLimit,
       "qrVFilesUsed": qrVFilesUsed,
       "qrVFileLimit": qrVFileLimit,
       "qrVPathName": qrVPathName,
       "qrVVolume": qrVVolume,
       "qrVTree": qrVTree,
       "qrVIdType": qrVIdType,
       "qrVSid": qrVSid,
       "qrVKBytesThreshold": qrVKBytesThreshold,
       "qrVKBytesLimitSoft": qrVKBytesLimitSoft,
       "qrVFileLimitSoft": qrVFileLimitSoft,
       "qrV2Table": qrV2Table,
       "qrV2Entry": qrV2Entry,
       "qrV2Index": qrV2Index,
       "qrV2Type": qrV2Type,
       "qrV2Id": qrV2Id,
       "qrV2HighKBytesUsed": qrV2HighKBytesUsed,
       "qrV2LowKBytesUsed": qrV2LowKBytesUsed,
       "qrV2QuotaUnlimited": qrV2QuotaUnlimited,
       "qrV2HighKBytesLimit": qrV2HighKBytesLimit,
       "qrV2LowKBytesLimit": qrV2LowKBytesLimit,
       "qrV2FilesUsed": qrV2FilesUsed,
       "qrV2FileQuotaUnlimited": qrV2FileQuotaUnlimited,
       "qrV2FileLimit": qrV2FileLimit,
       "qrV2PathName": qrV2PathName,
       "qrV2Volume": qrV2Volume,
       "qrV2Tree": qrV2Tree,
       "qrV2IdType": qrV2IdType,
       "qrV2Sid": qrV2Sid,
       "qrV2ThresholdUnlimited": qrV2ThresholdUnlimited,
       "qrV2HighKBytesThreshold": qrV2HighKBytesThreshold,
       "qrV2LowKBytesThreshold": qrV2LowKBytesThreshold,
       "qrV2SoftQuotaUnlimited": qrV2SoftQuotaUnlimited,
       "qrV2HighKBytesSoftLimit": qrV2HighKBytesSoftLimit,
       "qrV2LowKBytesSoftLimit": qrV2LowKBytesSoftLimit,
       "qrV2SoftFileQuotaUnlimited": qrV2SoftFileQuotaUnlimited,
       "qrV2SoftFileLimit": qrV2SoftFileLimit,
       "qrV264KBytesUsed": qrV264KBytesUsed,
       "qrV264KBytesLimit": qrV264KBytesLimit,
       "qrV264KBytesThreshold": qrV264KBytesThreshold,
       "qrV264KBytesSoftLimit": qrV264KBytesSoftLimit,
       "filesys": filesys,
       "filesysMaxfilesAvail": filesysMaxfilesAvail,
       "filesysMaxfilesUsed": filesysMaxfilesUsed,
       "filesysMaxfilesPossible": filesysMaxfilesPossible,
       "dfTable": dfTable,
       "dfEntry": dfEntry,
       "dfIndex": dfIndex,
       "dfFileSys": dfFileSys,
       "dfKBytesTotal": dfKBytesTotal,
       "dfKBytesUsed": dfKBytesUsed,
       "dfKBytesAvail": dfKBytesAvail,
       "dfPerCentKBytesCapacity": dfPerCentKBytesCapacity,
       "dfInodesUsed": dfInodesUsed,
       "dfInodesFree": dfInodesFree,
       "dfPerCentInodeCapacity": dfPerCentInodeCapacity,
       "dfMountedOn": dfMountedOn,
       "dfMaxFilesAvail": dfMaxFilesAvail,
       "dfMaxFilesUsed": dfMaxFilesUsed,
       "dfMaxFilesPossible": dfMaxFilesPossible,
       "dfHighTotalKBytes": dfHighTotalKBytes,
       "dfLowTotalKBytes": dfLowTotalKBytes,
       "dfHighUsedKBytes": dfHighUsedKBytes,
       "dfLowUsedKBytes": dfLowUsedKBytes,
       "dfHighAvailKBytes": dfHighAvailKBytes,
       "dfLowAvailKBytes": dfLowAvailKBytes,
       "dfStatus": dfStatus,
       "dfMirrorStatus": dfMirrorStatus,
       "dfPlexCount": dfPlexCount,
       "dfType": dfType,
       "dfHighSisSharedKBytes": dfHighSisSharedKBytes,
       "dfLowSisSharedKBytes": dfLowSisSharedKBytes,
       "dfHighSisSavedKBytes": dfHighSisSavedKBytes,
       "dfLowSisSavedKBytes": dfLowSisSavedKBytes,
       "dfPerCentSaved": dfPerCentSaved,
       "df64TotalKBytes": df64TotalKBytes,
       "df64UsedKBytes": df64UsedKBytes,
       "df64AvailKBytes": df64AvailKBytes,
       "df64SisSharedKBytes": df64SisSharedKBytes,
       "df64SisSavedKBytes": df64SisSavedKBytes,
       "snapshot": snapshot,
       "slTable": slTable,
       "slEntry": slEntry,
       "slIndex": slIndex,
       "slMonth": slMonth,
       "slDay": slDay,
       "slHour": slHour,
       "slMinutes": slMinutes,
       "slName": slName,
       "slVTable": slVTable,
       "slVEntry": slVEntry,
       "slVIndex": slVIndex,
       "slVMonth": slVMonth,
       "slVDay": slVDay,
       "slVHour": slVHour,
       "slVMinutes": slVMinutes,
       "slVName": slVName,
       "slVVolume": slVVolume,
       "slVNumber": slVNumber,
       "slVVolumeName": slVVolumeName,
       "slVType": slVType,
       "slQTable": slQTable,
       "slQEntry": slQEntry,
       "slQIndex": slQIndex,
       "slQVolume": slQVolume,
       "slQQtree": slQQtree,
       "slQSnapshotName": slQSnapshotName,
       "slQSnapshotTime": slQSnapshotTime,
       "slQQtreeName": slQQtreeName,
       "slQQtreeContent": slQQtreeContent,
       "slQSource": slQSource,
       "slQSourceTime": slQSourceTime,
       "slQVolumeName": slQVolumeName,
       "dfNumber": dfNumber,
       "fsStatus": fsStatus,
       "fsOverallStatus": fsOverallStatus,
       "fsStatusMessage": fsStatusMessage,
       "fsMaxUsedBytesPerCent": fsMaxUsedBytesPerCent,
       "fsMaxUsedInodesPerCent": fsMaxUsedInodesPerCent,
       "fsMaxUsedReservedPerCent": fsMaxUsedReservedPerCent,
       "volTable": volTable,
       "volEntry": volEntry,
       "volIndex": volIndex,
       "volName": volName,
       "volFSID": volFSID,
       "volOwningHost": volOwningHost,
       "volState": volState,
       "volStatus": volStatus,
       "volOptions": volOptions,
       "volUUID": volUUID,
       "volAggrName": volAggrName,
       "volType": volType,
       "volClone": volClone,
       "volCloneOf": volCloneOf,
       "volCloneSnap": volCloneSnap,
       "volNumber": volNumber,
       "qtreeTable": qtreeTable,
       "qtreeEntry": qtreeEntry,
       "qtreeIndex": qtreeIndex,
       "qtreeVolume": qtreeVolume,
       "qtreeVolumeName": qtreeVolumeName,
       "qtreeId": qtreeId,
       "qtreeName": qtreeName,
       "qtreeStyle": qtreeStyle,
       "qtreeStatus": qtreeStatus,
       "qtreeOplock": qtreeOplock,
       "aggrTable": aggrTable,
       "aggrEntry": aggrEntry,
       "aggrIndex": aggrIndex,
       "aggrName": aggrName,
       "aggrFSID": aggrFSID,
       "aggrOwningHost": aggrOwningHost,
       "aggrState": aggrState,
       "aggrStatus": aggrStatus,
       "aggrOptions": aggrOptions,
       "aggrUUID": aggrUUID,
       "aggrFlexvollist": aggrFlexvollist,
       "aggrType": aggrType,
       "aggrRaidType": aggrRaidType,
       "aggrNumber": aggrNumber,
       "raid": raid,
       "raidTable": raidTable,
       "raidEntry": raidEntry,
       "raidIndex": raidIndex,
       "raidDiskName": raidDiskName,
       "raidStatus": raidStatus,
       "raidDiskId": raidDiskId,
       "raidScsiAdapter": raidScsiAdapter,
       "raidScsiId": raidScsiId,
       "raidUsedMb": raidUsedMb,
       "raidUsedBlocks": raidUsedBlocks,
       "raidTotalMb": raidTotalMb,
       "raidTotalBlocks": raidTotalBlocks,
       "raidCompletionPerCent": raidCompletionPerCent,
       "raidVTable": raidVTable,
       "raidVEntry": raidVEntry,
       "raidVIndex": raidVIndex,
       "raidVDiskName": raidVDiskName,
       "raidVStatus": raidVStatus,
       "raidVDiskId": raidVDiskId,
       "raidVScsiAdapter": raidVScsiAdapter,
       "raidVScsiId": raidVScsiId,
       "raidVUsedMb": raidVUsedMb,
       "raidVUsedBlocks": raidVUsedBlocks,
       "raidVTotalMb": raidVTotalMb,
       "raidVTotalBlocks": raidVTotalBlocks,
       "raidVCompletionPerCent": raidVCompletionPerCent,
       "raidVVol": raidVVol,
       "raidVGroup": raidVGroup,
       "raidVDiskNumber": raidVDiskNumber,
       "raidVGroupNumber": raidVGroupNumber,
       "raidVDiskPort": raidVDiskPort,
       "raidVSecondaryDiskName": raidVSecondaryDiskName,
       "raidVSecondaryDiskPort": raidVSecondaryDiskPort,
       "raidVShelf": raidVShelf,
       "raidVBay": raidVBay,
       "raidVPlex": raidVPlex,
       "raidVPlexGroup": raidVPlexGroup,
       "raidVPlexNumber": raidVPlexNumber,
       "raidVPlexName": raidVPlexName,
       "raidVSectorSize": raidVSectorSize,
       "raidVDiskSerialNumber": raidVDiskSerialNumber,
       "raidVDiskVendor": raidVDiskVendor,
       "raidVDiskModel": raidVDiskModel,
       "raidVDiskFirmwareRevision": raidVDiskFirmwareRevision,
       "raidVDiskRPM": raidVDiskRPM,
       "raidVDiskType": raidVDiskType,
       "raidVDiskPool": raidVDiskPool,
       "raidVDiskCopyDestDiskName": raidVDiskCopyDestDiskName,
       "spareTable": spareTable,
       "spareEntry": spareEntry,
       "spareIndex": spareIndex,
       "spareDiskName": spareDiskName,
       "spareStatus": spareStatus,
       "spareDiskId": spareDiskId,
       "spareScsiAdapter": spareScsiAdapter,
       "spareScsiId": spareScsiId,
       "spareTotalMb": spareTotalMb,
       "spareTotalBlocks": spareTotalBlocks,
       "spareDiskPort": spareDiskPort,
       "spareSecondaryDiskName": spareSecondaryDiskName,
       "spareSecondaryDiskPort": spareSecondaryDiskPort,
       "spareShelf": spareShelf,
       "spareBay": spareBay,
       "sparePool": sparePool,
       "spareSectorSize": spareSectorSize,
       "spareDiskSerialNumber": spareDiskSerialNumber,
       "spareDiskVendor": spareDiskVendor,
       "spareDiskModel": spareDiskModel,
       "spareDiskFirmwareRevision": spareDiskFirmwareRevision,
       "spareDiskRPM": spareDiskRPM,
       "spareDiskType": spareDiskType,
       "diskSummary": diskSummary,
       "diskTotalCount": diskTotalCount,
       "diskActiveCount": diskActiveCount,
       "diskReconstructingCount": diskReconstructingCount,
       "diskReconstructingParityCount": diskReconstructingParityCount,
       "diskVerifyingParityCount": diskVerifyingParityCount,
       "diskScrubbingCount": diskScrubbingCount,
       "diskFailedCount": diskFailedCount,
       "diskSpareCount": diskSpareCount,
       "diskAddingSpareCount": diskAddingSpareCount,
       "diskFailedMessage": diskFailedMessage,
       "diskPrefailedCount": diskPrefailedCount,
       "raidVNumber": raidVNumber,
       "spareNumber": spareNumber,
       "otherDiskNumber": otherDiskNumber,
       "raidPNumber": raidPNumber,
       "otherDiskTable": otherDiskTable,
       "otherDiskEntry": otherDiskEntry,
       "otherDiskIndex": otherDiskIndex,
       "otherDiskDiskName": otherDiskDiskName,
       "otherDiskStatus": otherDiskStatus,
       "otherDiskDiskId": otherDiskDiskId,
       "otherDiskScsiAdapter": otherDiskScsiAdapter,
       "otherDiskScsiId": otherDiskScsiId,
       "otherDiskTotalMb": otherDiskTotalMb,
       "otherDiskTotalBlocks": otherDiskTotalBlocks,
       "otherDiskDiskPort": otherDiskDiskPort,
       "otherDiskSecondaryDiskName": otherDiskSecondaryDiskName,
       "otherDiskSecondaryDiskPort": otherDiskSecondaryDiskPort,
       "otherDiskShelf": otherDiskShelf,
       "otherDiskBay": otherDiskBay,
       "otherDiskPool": otherDiskPool,
       "otherDiskSectorSize": otherDiskSectorSize,
       "otherDiskSerialNumber": otherDiskSerialNumber,
       "otherDiskVendor": otherDiskVendor,
       "otherDiskModel": otherDiskModel,
       "otherDiskFirmwareRevision": otherDiskFirmwareRevision,
       "otherDiskRPM": otherDiskRPM,
       "otherDiskType": otherDiskType,
       "raidPTable": raidPTable,
       "raidPEntry": raidPEntry,
       "raidPIndex": raidPIndex,
       "raidPStatus": raidPStatus,
       "raidPVol": raidPVol,
       "raidPPlex": raidPPlex,
       "raidPGroup": raidPGroup,
       "raidPPlexNumber": raidPPlexNumber,
       "raidPGroupNumber": raidPGroupNumber,
       "raidPDiskNumber": raidPDiskNumber,
       "raidPPlexName": raidPPlexName,
       "raidPDiskName": raidPDiskName,
       "raidPDiskPort": raidPDiskPort,
       "raidPSecondaryDiskName": raidPSecondaryDiskName,
       "raidPSecondaryDiskPort": raidPSecondaryDiskPort,
       "raidPScsiAdapter": raidPScsiAdapter,
       "raidPScsiId": raidPScsiId,
       "raidPDiskId": raidPDiskId,
       "raidPShelf": raidPShelf,
       "raidPBay": raidPBay,
       "raidPSectorSize": raidPSectorSize,
       "raidPUsedMb": raidPUsedMb,
       "raidPUsedBlocks": raidPUsedBlocks,
       "raidPTotalMb": raidPTotalMb,
       "raidPTotalBlocks": raidPTotalBlocks,
       "raidPCompletionPerCent": raidPCompletionPerCent,
       "raidPDiskSerialNumber": raidPDiskSerialNumber,
       "raidPDiskVendor": raidPDiskVendor,
       "raidPDiskModel": raidPDiskModel,
       "raidPDiskFirmwareRevision": raidPDiskFirmwareRevision,
       "raidPDiskRPM": raidPDiskRPM,
       "raidPDiskType": raidPDiskType,
       "raidPDiskPool": raidPDiskPool,
       "raidPDiskCopyDestDiskName": raidPDiskCopyDestDiskName,
       "plexTable": plexTable,
       "plexEntry": plexEntry,
       "plexIndex": plexIndex,
       "plexName": plexName,
       "plexVolName": plexVolName,
       "plexStatus": plexStatus,
       "plexPercentResyncing": plexPercentResyncing,
       "outOfDateDiskCount": outOfDateDiskCount,
       "outOfDateDiskTable": outOfDateDiskTable,
       "outOfDateDiskEntry": outOfDateDiskEntry,
       "outOfDateDiskIndex": outOfDateDiskIndex,
       "outOfDateDiskDiskName": outOfDateDiskDiskName,
       "outOfDateDiskDiskId": outOfDateDiskDiskId,
       "outOfDateDiskScsiAdapter": outOfDateDiskScsiAdapter,
       "outOfDateDiskScsiId": outOfDateDiskScsiId,
       "outOfDateDiskTotalMb": outOfDateDiskTotalMb,
       "outOfDateDiskTotalBlocks": outOfDateDiskTotalBlocks,
       "outOfDateDiskDiskPort": outOfDateDiskDiskPort,
       "outOfDateDiskSecondaryDiskName": outOfDateDiskSecondaryDiskName,
       "outOfDateDiskSecondaryDiskPort": outOfDateDiskSecondaryDiskPort,
       "outOfDateDiskShelf": outOfDateDiskShelf,
       "outOfDateDiskBay": outOfDateDiskBay,
       "outOfDateDiskPool": outOfDateDiskPool,
       "outOfDateDiskSectorSize": outOfDateDiskSectorSize,
       "outOfDateDiskSerialNumber": outOfDateDiskSerialNumber,
       "outOfDateDiskVendor": outOfDateDiskVendor,
       "outOfDateDiskModel": outOfDateDiskModel,
       "outOfDateDiskFirmwareRevision": outOfDateDiskFirmwareRevision,
       "outOfDateDiskRPM": outOfDateDiskRPM,
       "outOfDateDiskType": outOfDateDiskType,
       "cifs": cifs,
       "cifsOptions": cifsOptions,
       "cifsIsEnabled": cifsIsEnabled,
       "cifsIsLoginEnabled": cifsIsLoginEnabled,
       "cifsHostName": cifsHostName,
       "cifsAltNames": cifsAltNames,
       "cifsDomainJoined": cifsDomainJoined,
       "cifsDomainName": cifsDomainName,
       "cifsWGName": cifsWGName,
       "cifsDCName": cifsDCName,
       "cifsIsWinsEnabled": cifsIsWinsEnabled,
       "cifsWinsServers": cifsWinsServers,
       "cifsSecurityModel": cifsSecurityModel,
       "cifsPCGenericUser": cifsPCGenericUser,
       "cifsOplocksEnabled": cifsOplocksEnabled,
       "cifsLevel2OplocksEnabled": cifsLevel2OplocksEnabled,
       "cifsPreserveCase": cifsPreserveCase,
       "cifsSymlinksEnabled": cifsSymlinksEnabled,
       "cifsSymlinkCycleProtEnabled": cifsSymlinkCycleProtEnabled,
       "cifsIsLicensed": cifsIsLicensed,
       "cifsPerClientStatsEnabled": cifsPerClientStatsEnabled,
       "cifsInfo": cifsInfo,
       "cifsStatus": cifsStatus,
       "cifsNeedPW": cifsNeedPW,
       "cifsTimeToShutdown": cifsTimeToShutdown,
       "cifsMaxConnections": cifsMaxConnections,
       "cifsMaxTrees": cifsMaxTrees,
       "cifsMaxShares": cifsMaxShares,
       "cifsMaxFiles": cifsMaxFiles,
       "cifsMaxACLs": cifsMaxACLs,
       "cifsConnectedUsers": cifsConnectedUsers,
       "cifsNTrees": cifsNTrees,
       "cifsNShares": cifsNShares,
       "cifsNSessions": cifsNSessions,
       "cifsNOpenFiles": cifsNOpenFiles,
       "cifsNOpenDirs": cifsNOpenDirs,
       "cifsNOplockBreakWaits": cifsNOplockBreakWaits,
       "cifsNOplockAckWaits": cifsNOplockAckWaits,
       "cifsSuspectOps": cifsSuspectOps,
       "cifsNDomainControllers": cifsNDomainControllers,
       "cifsStats": cifsStats,
       "cifsServ": cifsServ,
       "cifsOps": cifsOps,
       "cifsTotalOps": cifsTotalOps,
       "cifsTotalCalls": cifsTotalCalls,
       "cifsBadCalls": cifsBadCalls,
       "cifsGetAttrs": cifsGetAttrs,
       "cifsReads": cifsReads,
       "cifsWrites": cifsWrites,
       "cifsLocks": cifsLocks,
       "cifsOpens": cifsOpens,
       "cifsDirOps": cifsDirOps,
       "cifsOthers": cifsOthers,
       "cifsReqs": cifsReqs,
       "smbNegProts": smbNegProts,
       "smbSessionSetupAndXs": smbSessionSetupAndXs,
       "smbLogoffAndXs": smbLogoffAndXs,
       "smbTreeConnectAndXs": smbTreeConnectAndXs,
       "smbTreeDisconnects": smbTreeDisconnects,
       "smbTrans2QueryFSInfos": smbTrans2QueryFSInfos,
       "smbEchos": smbEchos,
       "smbNTCancels": smbNTCancels,
       "smbNTCreateAndXs": smbNTCreateAndXs,
       "smbNTTransactCreates": smbNTTransactCreates,
       "smbCreateTemporaries": smbCreateTemporaries,
       "smbReadAndXs": smbReadAndXs,
       "smbWriteAndXs": smbWriteAndXs,
       "smbLockingAndXs": smbLockingAndXs,
       "smbSeeks": smbSeeks,
       "smbFlushes": smbFlushes,
       "smbCloses": smbCloses,
       "smbDeletes": smbDeletes,
       "smbRenames": smbRenames,
       "smbMoves": smbMoves,
       "smbCopies": smbCopies,
       "smbTrans2QueryPathInfos": smbTrans2QueryPathInfos,
       "smbTrans2QueryFileInfos": smbTrans2QueryFileInfos,
       "smbTrans2SetPathInfos": smbTrans2SetPathInfos,
       "smbTrans2SetFileInfos": smbTrans2SetFileInfos,
       "smbDeleteDirs": smbDeleteDirs,
       "smbCheckDirs": smbCheckDirs,
       "smbTrans2FindFirst2s": smbTrans2FindFirst2s,
       "smbTrans2FindNext2s": smbTrans2FindNext2s,
       "smbFindClose2s": smbFindClose2s,
       "smbNTTransactNotifyChgs": smbNTTransactNotifyChgs,
       "smbTrans2GetDFSReferrals": smbTrans2GetDFSReferrals,
       "smbTrans2ReportDFSIncs": smbTrans2ReportDFSIncs,
       "smbOpenPrintFiles": smbOpenPrintFiles,
       "smbGetPrintQueues": smbGetPrintQueues,
       "smbNTTransactIoctls": smbNTTransactIoctls,
       "smbNTTransactQuerySecDescs": smbNTTransactQuerySecDescs,
       "smbNTTransactSetSecDescs": smbNTTransactSetSecDescs,
       "smbTrans2CreateDirs": smbTrans2CreateDirs,
       "smbNTCancelCNs": smbNTCancelCNs,
       "smbNTCancelOthers": smbNTCancelOthers,
       "cifsPercent": cifsPercent,
       "smbNegProtPct": smbNegProtPct,
       "smbSessionSetupAndXPct": smbSessionSetupAndXPct,
       "smbLogoffAndXPct": smbLogoffAndXPct,
       "smbTreeConnectAndXPct": smbTreeConnectAndXPct,
       "smbTreeDisconnectAndXPct": smbTreeDisconnectAndXPct,
       "smbTrans2QueryFSInfoPct": smbTrans2QueryFSInfoPct,
       "smbEchoPct": smbEchoPct,
       "smbNTCancelPct": smbNTCancelPct,
       "smbCreateAndXPct": smbCreateAndXPct,
       "smbTransactCreatePct": smbTransactCreatePct,
       "smbCreateTemporaryPct": smbCreateTemporaryPct,
       "smbReadAndXPct": smbReadAndXPct,
       "smbWriteAndXPct": smbWriteAndXPct,
       "smbLockingAndXPct": smbLockingAndXPct,
       "smbSeekPct": smbSeekPct,
       "smbFlushPct": smbFlushPct,
       "smbClosePct": smbClosePct,
       "smbDeletePct": smbDeletePct,
       "smbRenamePct": smbRenamePct,
       "smbMovePct": smbMovePct,
       "smbCopyPct": smbCopyPct,
       "smbTrans2QueryPathInfoPct": smbTrans2QueryPathInfoPct,
       "smbTrans2QueryFileInfoPct": smbTrans2QueryFileInfoPct,
       "smbTrans2SetPathInfoPct": smbTrans2SetPathInfoPct,
       "smbTrans2SetFileInfoPct": smbTrans2SetFileInfoPct,
       "smbDeleteDirPct": smbDeleteDirPct,
       "smbCheckDirPct": smbCheckDirPct,
       "smbTrans2FindFirst2Pct": smbTrans2FindFirst2Pct,
       "smbTrans2FindNext2Pct": smbTrans2FindNext2Pct,
       "smbFindClose2Pct": smbFindClose2Pct,
       "smbNTTransactNotifyChgPct": smbNTTransactNotifyChgPct,
       "smbTrans2GetDFSReferralPct": smbTrans2GetDFSReferralPct,
       "smbTrans2ReportDFSIncPct": smbTrans2ReportDFSIncPct,
       "smbOpenPrintFilePct": smbOpenPrintFilePct,
       "smbGetPrintQueuePct": smbGetPrintQueuePct,
       "smbNTTransactIoctlPct": smbNTTransactIoctlPct,
       "smbNTTransactQuerySecDescPct": smbNTTransactQuerySecDescPct,
       "smbNTTransactSetSecDescPct": smbNTTransactSetSecDescPct,
       "smbTrans2CreateDirPct": smbTrans2CreateDirPct,
       "smbNTCancelCNPct": smbNTCancelCNPct,
       "smbNTCancelOtherPct": smbNTCancelOtherPct,
       "cifsObsReqs": cifsObsReqs,
       "obsSmbClosePrintFiles": obsSmbClosePrintFiles,
       "obsSmbCreates": obsSmbCreates,
       "obsSmbCreateDirs": obsSmbCreateDirs,
       "obsSmbCreateNews": obsSmbCreateNews,
       "obsSmbLockAndReads": obsSmbLockAndReads,
       "obsSmbLockByteRanges": obsSmbLockByteRanges,
       "obsSmbOpens": obsSmbOpens,
       "obsSmbOpenAndXs": obsSmbOpenAndXs,
       "obsSmbProcessExits": obsSmbProcessExits,
       "obsSmbQueryInfos": obsSmbQueryInfos,
       "obsSmbQueryInfo2s": obsSmbQueryInfo2s,
       "obsSmbReads": obsSmbReads,
       "obsSmbReadMPXs": obsSmbReadMPXs,
       "obsSmbReadRaws": obsSmbReadRaws,
       "obsSmbSearchs": obsSmbSearchs,
       "obsSmbSetInfos": obsSmbSetInfos,
       "obsSmbSetInfo2s": obsSmbSetInfo2s,
       "obsSmbQueryInfoDisks": obsSmbQueryInfoDisks,
       "obsSmbTrans2Open2s": obsSmbTrans2Open2s,
       "obsSmbTreeConnects": obsSmbTreeConnects,
       "obsSmbUnlockByteRanges": obsSmbUnlockByteRanges,
       "obsSmbWrites": obsSmbWrites,
       "obsSmbWriteAndUnlocks": obsSmbWriteAndUnlocks,
       "obsSmbWriteAndCloses": obsSmbWriteAndCloses,
       "obsSmbWriteMPXs": obsSmbWriteMPXs,
       "obsSmbWritePrintFiles": obsSmbWritePrintFiles,
       "obsSmbWriteRaws": obsSmbWriteRaws,
       "cifsObsPercent": cifsObsPercent,
       "obsSmbClosePrintFilePct": obsSmbClosePrintFilePct,
       "obsSmbCreatePct": obsSmbCreatePct,
       "obsSmbCreateDirPct": obsSmbCreateDirPct,
       "obsSmbCreateNewPct": obsSmbCreateNewPct,
       "obsSmbLockAndReadPct": obsSmbLockAndReadPct,
       "obsSmbLockByteRangePct": obsSmbLockByteRangePct,
       "obsSmbOpenPct": obsSmbOpenPct,
       "obsSmbOpenAndXPct": obsSmbOpenAndXPct,
       "obsSmbProcessExitPct": obsSmbProcessExitPct,
       "obsSmbQueryInfoPct": obsSmbQueryInfoPct,
       "obsSmbQueryInfo2Pct": obsSmbQueryInfo2Pct,
       "obsSmbReadPct": obsSmbReadPct,
       "obsSmbReadMPXPct": obsSmbReadMPXPct,
       "obsSmbReadRawPct": obsSmbReadRawPct,
       "obsSmbSearchPct": obsSmbSearchPct,
       "obsSmbSetInfoPct": obsSmbSetInfoPct,
       "obsSmbSetInfo2Pct": obsSmbSetInfo2Pct,
       "obsSmbQueryInfoDiskPct": obsSmbQueryInfoDiskPct,
       "obsSmbTrans2Open2Pct": obsSmbTrans2Open2Pct,
       "obsSmbTreeConnectPct": obsSmbTreeConnectPct,
       "obsSmbUnlockByteRangePct": obsSmbUnlockByteRangePct,
       "obsSmbWritePct": obsSmbWritePct,
       "obsSmbWriteAndUnlockPct": obsSmbWriteAndUnlockPct,
       "obsSmbWriteAndClosePct": obsSmbWriteAndClosePct,
       "obsSmbWriteMPXPct": obsSmbWriteMPXPct,
       "obsSmbWritePrintFilePct": obsSmbWritePrintFilePct,
       "obsSmbWriteRawPct": obsSmbWriteRawPct,
       "cifsMisc": cifsMisc,
       "cifsCancelLocks": cifsCancelLocks,
       "cifsWaitLocks": cifsWaitLocks,
       "cifsCopyToAligns": cifsCopyToAligns,
       "cifsAlignedSmalls": cifsAlignedSmalls,
       "cifsAlignedLarges": cifsAlignedLarges,
       "cifsAlignedSmallRels": cifsAlignedSmallRels,
       "cifsAlignedLargeRels": cifsAlignedLargeRels,
       "cifsMbufWaits": cifsMbufWaits,
       "cifsNbtWaits": cifsNbtWaits,
       "cifsCwaWaits": cifsCwaWaits,
       "cifsMultipleVCs": cifsMultipleVCs,
       "cifsPDCUpcalls": cifsPDCUpcalls,
       "cifsQueuedWriteRaws": cifsQueuedWriteRaws,
       "cifsNBTDisconnects": cifsNBTDisconnects,
       "cifsSMBDisconnects": cifsSMBDisconnects,
       "cifsDupDisconnects": cifsDupDisconnects,
       "cifsOpLkBatchToL2s": cifsOpLkBatchToL2s,
       "cifsOpLkBatchToNones": cifsOpLkBatchToNones,
       "cifsOpLkL2ToNones": cifsOpLkL2ToNones,
       "cifsOpLkNoBreakAcks": cifsOpLkNoBreakAcks,
       "cifsOpLkIgnoredAcks": cifsOpLkIgnoredAcks,
       "cifsOpLkMultiWaiters": cifsOpLkMultiWaiters,
       "cifsSharingErrorRetries": cifsSharingErrorRetries,
       "cifsOpLkWaiterTimedOuts": cifsOpLkWaiterTimedOuts,
       "cifsOpLkDelayedBreaks": cifsOpLkDelayedBreaks,
       "cifsOpLkEarlyNFSs": cifsOpLkEarlyNFSs,
       "cifsOpLkNFSWaiteds": cifsOpLkNFSWaiteds,
       "cifsMaxNFSBkWaiterCount": cifsMaxNFSBkWaiterCount,
       "cifsClearTextPasswd": cifsClearTextPasswd,
       "netcache": netcache,
       "ncOptions": ncOptions,
       "ncIsEnabled": ncIsEnabled,
       "ncIsLicensed": ncIsLicensed,
       "ncDnsOptions": ncDnsOptions,
       "ncDnsIsEnabled": ncDnsIsEnabled,
       "ncHttpOptions": ncHttpOptions,
       "ncHttpIsEnabled": ncHttpIsEnabled,
       "ncNntpOptions": ncNntpOptions,
       "ncNntpIsEnabled": ncNntpIsEnabled,
       "ncNntpIsLicensed": ncNntpIsLicensed,
       "ncStreamingOptions": ncStreamingOptions,
       "ncStreamingMmsIsEnabled": ncStreamingMmsIsEnabled,
       "ncStreamingMmsIsLicensed": ncStreamingMmsIsLicensed,
       "ncStreamingMmsProIsLicensed": ncStreamingMmsProIsLicensed,
       "ncStreamingRtspIsEnabled": ncStreamingRtspIsEnabled,
       "ncStreamingQuickTimeIsLicensed": ncStreamingQuickTimeIsLicensed,
       "ncStreamingRealIsLicensed": ncStreamingRealIsLicensed,
       "ncStreamingMmsUltraIsLicensed": ncStreamingMmsUltraIsLicensed,
       "ncStreamingRealProIsLicensed": ncStreamingRealProIsLicensed,
       "ncStreamingRealUltraIsLicensed": ncStreamingRealUltraIsLicensed,
       "ncIcapOptions": ncIcapOptions,
       "ncIcapIsEnabled": ncIcapIsEnabled,
       "ncIcapIsLicensed": ncIcapIsLicensed,
       "ncIcapv1IsEnabled": ncIcapv1IsEnabled,
       "ncGrmOptions": ncGrmOptions,
       "ncGrmServerOptions": ncGrmServerOptions,
       "ncGrmServerIsEnabled": ncGrmServerIsEnabled,
       "ncGrmServerIsLicensed": ncGrmServerIsLicensed,
       "ncGrmAgentOptions": ncGrmAgentOptions,
       "ncGrmAgentIsEnabled": ncGrmAgentIsEnabled,
       "ncGrmAgentIsLicensed": ncGrmAgentIsLicensed,
       "ncCdOptions": ncCdOptions,
       "ncCdIsEnabled": ncCdIsEnabled,
       "ncHttpsProxyOptions": ncHttpsProxyOptions,
       "ncHttpsProxyIsEnabled": ncHttpsProxyIsEnabled,
       "ncHttpsProxyIsLicensed": ncHttpsProxyIsLicensed,
       "ncCmsOptions": ncCmsOptions,
       "ncCmsIsEnabled": ncCmsIsEnabled,
       "ncInfo": ncInfo,
       "ncVersion": ncVersion,
       "ncAdminPort": ncAdminPort,
       "accelmonitor": accelmonitor,
       "amNumber": amNumber,
       "amMonitor": amMonitor,
       "amMonitorString": amMonitorString,
       "amTable": amTable,
       "amEntry": amEntry,
       "amIndex": amIndex,
       "amAddress": amAddress,
       "amPort": amPort,
       "amStatus": amStatus,
       "ncLocalConfigChanged": ncLocalConfigChanged,
       "ncLocalConfigVersion": ncLocalConfigVersion,
       "grmMonitor": grmMonitor,
       "grmMonitorToggle": grmMonitorToggle,
       "grmMonitorString": grmMonitorString,
       "takeoverinfo": takeoverinfo,
       "takeoverAddrs": takeoverAddrs,
       "takeoverMode": takeoverMode,
       "takeoverStatus": takeoverStatus,
       "ncStats": ncStats,
       "ncObjectsStored": ncObjectsStored,
       "ncBytesToClients": ncBytesToClients,
       "ncBytesFromClients": ncBytesFromClients,
       "ncBytesToServers": ncBytesToServers,
       "ncBytesFromServers": ncBytesFromServers,
       "ncHttp": ncHttp,
       "ncHttpTotalRequests": ncHttpTotalRequests,
       "ncHttpHitRequests": ncHttpHitRequests,
       "ncHttpMissRequests": ncHttpMissRequests,
       "ncHttpServConns": ncHttpServConns,
       "ncHttpCliConns": ncHttpCliConns,
       "ncHttpBWSavings": ncHttpBWSavings,
       "ncHttpObjHitrate": ncHttpObjHitrate,
       "ncHttpRespTimePerByte": ncHttpRespTimePerByte,
       "ncHttpAvgRespTime": ncHttpAvgRespTime,
       "ncHttpAvgHitRespTime": ncHttpAvgHitRespTime,
       "ncHttpAvgMissRespTime": ncHttpAvgMissRespTime,
       "ncHttpInstAvgRespTime": ncHttpInstAvgRespTime,
       "ncHttpInstAvgHitRespTime": ncHttpInstAvgHitRespTime,
       "ncHttpInstAvgMissRespTime": ncHttpInstAvgMissRespTime,
       "ncHttpTotalRespTime": ncHttpTotalRespTime,
       "ncHttpTotalHitRespTime": ncHttpTotalHitRespTime,
       "ncHttpTotalMissRespTime": ncHttpTotalMissRespTime,
       "ncHttpBytesToClients": ncHttpBytesToClients,
       "ncHttpBytesFromClients": ncHttpBytesFromClients,
       "ncHttpBytesToServers": ncHttpBytesToServers,
       "ncHttpBytesFromServers": ncHttpBytesFromServers,
       "ncHttpHighTotalRespTimes": ncHttpHighTotalRespTimes,
       "ncHttpLowTotalRespTimes": ncHttpLowTotalRespTimes,
       "ncHttpHighTotalHitRespTimes": ncHttpHighTotalHitRespTimes,
       "ncHttpLowTotalHitRespTimes": ncHttpLowTotalHitRespTimes,
       "ncHttpHighTotalMissRespTimes": ncHttpHighTotalMissRespTimes,
       "ncHttpLowTotalMissRespTimes": ncHttpLowTotalMissRespTimes,
       "ncHttpReqRate": ncHttpReqRate,
       "ncHttpObjHitRateLast1Min": ncHttpObjHitRateLast1Min,
       "ncHttpObjHitRateLast5Min": ncHttpObjHitRateLast5Min,
       "ncHttpByteHitRateLast1Min": ncHttpByteHitRateLast1Min,
       "ncHttpByteHitRateLast5Min": ncHttpByteHitRateLast5Min,
       "ncHttpBWSavingsLast1Min": ncHttpBWSavingsLast1Min,
       "ncHttpBWSavingsLast5Min": ncHttpBWSavingsLast5Min,
       "ncHttpActiveServConns": ncHttpActiveServConns,
       "ncHttpActiveCliConns": ncHttpActiveCliConns,
       "ncHttpAccelTable": ncHttpAccelTable,
       "ncHttpAccelEntry": ncHttpAccelEntry,
       "ncHttpAccelIndex": ncHttpAccelIndex,
       "ncHttpAccelKbytesFromClient": ncHttpAccelKbytesFromClient,
       "ncHttpAccelKbytesToClient": ncHttpAccelKbytesToClient,
       "ncHttpAccelHits": ncHttpAccelHits,
       "ncHttpsAccelTable": ncHttpsAccelTable,
       "ncHttpsAccelEntry": ncHttpsAccelEntry,
       "ncHttpsAccelIndex": ncHttpsAccelIndex,
       "ncHttpsAccelKbytesFromClient": ncHttpsAccelKbytesFromClient,
       "ncHttpsAccelKbytesToClient": ncHttpsAccelKbytesToClient,
       "ncHttpsAccelHits": ncHttpsAccelHits,
       "ncNntp": ncNntp,
       "ncNntpTotalRequests": ncNntpTotalRequests,
       "ncNntpCacheableRequests": ncNntpCacheableRequests,
       "ncNntpProxyRequests": ncNntpProxyRequests,
       "ncNntpServConns": ncNntpServConns,
       "ncNntpCliConns": ncNntpCliConns,
       "ncNntpBWSavings": ncNntpBWSavings,
       "ncNntpRespTimePerByte": ncNntpRespTimePerByte,
       "ncNntpBytesToClients": ncNntpBytesToClients,
       "ncNntpBytesFromClients": ncNntpBytesFromClients,
       "ncNntpBytesToServers": ncNntpBytesToServers,
       "ncNntpBytesFromServers": ncNntpBytesFromServers,
       "ncNntpObjHitrate": ncNntpObjHitrate,
       "ncNntpActiveServConns": ncNntpActiveServConns,
       "ncNntpActiveCliConns": ncNntpActiveCliConns,
       "ncFtp": ncFtp,
       "ncFtpTotalRequests": ncFtpTotalRequests,
       "ncFtpHitRequests": ncFtpHitRequests,
       "ncFtpMissRequests": ncFtpMissRequests,
       "ncFtpServConns": ncFtpServConns,
       "ncFtpCliConns": ncFtpCliConns,
       "ncFtpBWSavings": ncFtpBWSavings,
       "ncFtpRespTimePerByte": ncFtpRespTimePerByte,
       "ncFtpBytesToClients": ncFtpBytesToClients,
       "ncFtpBytesFromClients": ncFtpBytesFromClients,
       "ncFtpBytesToServers": ncFtpBytesToServers,
       "ncFtpBytesFromServers": ncFtpBytesFromServers,
       "ncFtpObjHitrate": ncFtpObjHitrate,
       "ncFtpActiveServConns": ncFtpActiveServConns,
       "ncFtpActiveCliConns": ncFtpActiveCliConns,
       "ncStreaming": ncStreaming,
       "ncStreamingServConns": ncStreamingServConns,
       "ncStreamingCliConns": ncStreamingCliConns,
       "ncStreamingBWSavings": ncStreamingBWSavings,
       "ncStreamingRespTimePerByte": ncStreamingRespTimePerByte,
       "ncStreamingHitRequests": ncStreamingHitRequests,
       "ncStreamingMissRequests": ncStreamingMissRequests,
       "ncStreamingTotalRequests": ncStreamingTotalRequests,
       "ncStreamingLiveBytesToClients": ncStreamingLiveBytesToClients,
       "ncStreamingLiveBytesFromClients": ncStreamingLiveBytesFromClients,
       "ncStreamingLiveBytesToServers": ncStreamingLiveBytesToServers,
       "ncStreamingLiveBytesFromServers": ncStreamingLiveBytesFromServers,
       "ncStreamingProxyBytesToClients": ncStreamingProxyBytesToClients,
       "ncStreamingProxyBytesFromClients": ncStreamingProxyBytesFromClients,
       "ncStreamingProxyBytesToServers": ncStreamingProxyBytesToServers,
       "ncStreamingProxyBytesFromServers": ncStreamingProxyBytesFromServers,
       "ncStreamingOBTClients": ncStreamingOBTClients,
       "ncStreamingOBFClients": ncStreamingOBFClients,
       "ncStreamingOBTServers": ncStreamingOBTServers,
       "ncStreamingOBFServers": ncStreamingOBFServers,
       "ncStreamingObjHitrate": ncStreamingObjHitrate,
       "ncStreamingRealBytesToClients": ncStreamingRealBytesToClients,
       "ncStreamingRealBytesFromClients": ncStreamingRealBytesFromClients,
       "ncStreamingRealBytesToServers": ncStreamingRealBytesToServers,
       "ncStreamingRealBytesFromServers": ncStreamingRealBytesFromServers,
       "ncStreamingMmsBytesToClients": ncStreamingMmsBytesToClients,
       "ncStreamingMmsBytesFromClients": ncStreamingMmsBytesFromClients,
       "ncStreamingMmsBytesToServers": ncStreamingMmsBytesToServers,
       "ncStreamingMmsBytesFromServers": ncStreamingMmsBytesFromServers,
       "ncStreamingQTBTClients": ncStreamingQTBTClients,
       "ncStreamingQTBFClients": ncStreamingQTBFClients,
       "ncStreamingQTBTServers": ncStreamingQTBTServers,
       "ncStreamingQTBFServers": ncStreamingQTBFServers,
       "ncStreamingLiveBWSavings": ncStreamingLiveBWSavings,
       "ncStreamingOndemandBWSavings": ncStreamingOndemandBWSavings,
       "ncStreamingRealBWSavings": ncStreamingRealBWSavings,
       "ncStreamingMmsBWSavings": ncStreamingMmsBWSavings,
       "ncStreamingQuickTimeBWSavings": ncStreamingQuickTimeBWSavings,
       "ncStreamingActiveServConns": ncStreamingActiveServConns,
       "ncStreamingActiveCliConns": ncStreamingActiveCliConns,
       "ncStreamingRtspWMBytesToClients": ncStreamingRtspWMBytesToClients,
       "ncStreamingRtspWMBFClients": ncStreamingRtspWMBFClients,
       "ncStreamingRtspWMBytesToServers": ncStreamingRtspWMBytesToServers,
       "ncStreamingRtspWMBFServers": ncStreamingRtspWMBFServers,
       "ncStreamingRtspWMBWSavings": ncStreamingRtspWMBWSavings,
       "ncStreamingAccelTable": ncStreamingAccelTable,
       "ncStreamingAccelEntry": ncStreamingAccelEntry,
       "ncStreamingAccelIndex": ncStreamingAccelIndex,
       "ncStreamingAccelKbytesFromClient": ncStreamingAccelKbytesFromClient,
       "ncStreamingAccelKbytesToClient": ncStreamingAccelKbytesToClient,
       "ncStreamingAccelHits": ncStreamingAccelHits,
       "ncStreamingClientsDelayedSW": ncStreamingClientsDelayedSW,
       "ncTotalBWSavings": ncTotalBWSavings,
       "ncDns": ncDns,
       "ncDnsRequestsReceived": ncDnsRequestsReceived,
       "ncDnsCacheHits": ncDnsCacheHits,
       "ncDnsCacheMisses": ncDnsCacheMisses,
       "ncDnsSuccessfulForwardLookups": ncDnsSuccessfulForwardLookups,
       "ncDnsFailedForwardLookups": ncDnsFailedForwardLookups,
       "ncDnsPendingForwardLookups": ncDnsPendingForwardLookups,
       "ncDnsSuccessfulReverseLookups": ncDnsSuccessfulReverseLookups,
       "ncDnsFailedReverseLookups": ncDnsFailedReverseLookups,
       "ncDnsPendingReverseLookups": ncDnsPendingReverseLookups,
       "ncDnsIres": ncDnsIres,
       "ncDnsIresIsEnabled": ncDnsIresIsEnabled,
       "ncDnsIresIsInitialised": ncDnsIresIsInitialised,
       "ncDnsIresForwardLookups": ncDnsIresForwardLookups,
       "ncDnsIresPendingForwardLookups": ncDnsIresPendingForwardLookups,
       "ncDnsIresReverseLookups": ncDnsIresReverseLookups,
       "ncDnsIresPendingReverseLookups": ncDnsIresPendingReverseLookups,
       "ncAuth": ncAuth,
       "ncNtlm": ncNtlm,
       "ncNtlmPossibleProblem": ncNtlmPossibleProblem,
       "ncRM": ncRM,
       "ncRMMem": ncRMMem,
       "ncRMMemTotal": ncRMMemTotal,
       "ncRMMemFree": ncRMMemFree,
       "snapmirror": snapmirror,
       "snapmirrorOn": snapmirrorOn,
       "snapmirrorActiveRestoreCount": snapmirrorActiveRestoreCount,
       "snapmirrorScheduledRestoreCount": snapmirrorScheduledRestoreCount,
       "snapmirrorBackupNumber": snapmirrorBackupNumber,
       "snapmirrorBackupSuccesses": snapmirrorBackupSuccesses,
       "snapmirrorRestoreSuccesses": snapmirrorRestoreSuccesses,
       "snapmirrorBackupAborts": snapmirrorBackupAborts,
       "snapmirrorRestoreRestartAborts": snapmirrorRestoreRestartAborts,
       "snapmirrorRestoreWaitAborts": snapmirrorRestoreWaitAborts,
       "snapmirrorWrittenBytes": snapmirrorWrittenBytes,
       "snapmirrorReadBytes": snapmirrorReadBytes,
       "snapmirrorActiveDstNumber": snapmirrorActiveDstNumber,
       "snapmirrorActiveSrcNumber": snapmirrorActiveSrcNumber,
       "snapmirrorFilerTotalDstSuccesses": snapmirrorFilerTotalDstSuccesses,
       "snapmirrorFilerTotalSrcSuccesses": snapmirrorFilerTotalSrcSuccesses,
       "snapmirrorFilerTotalSrcFailures": snapmirrorFilerTotalSrcFailures,
       "snapmirrorFilerTotalDstFailures": snapmirrorFilerTotalDstFailures,
       "snapmirrorFilerTotalDstDeferments": snapmirrorFilerTotalDstDeferments,
       "snapmirrorIsLicensed": snapmirrorIsLicensed,
       "snapmirrorStatusTable": snapmirrorStatusTable,
       "snapmirrorStatusEntry": snapmirrorStatusEntry,
       "snapmirrorIndex": snapmirrorIndex,
       "snapmirrorSrc": snapmirrorSrc,
       "snapmirrorDst": snapmirrorDst,
       "snapmirrorStatus": snapmirrorStatus,
       "snapmirrorState": snapmirrorState,
       "snapmirrorLag": snapmirrorLag,
       "snapmirrorTotalSuccesses": snapmirrorTotalSuccesses,
       "snapmirrorTotalRestartSuccesses": snapmirrorTotalRestartSuccesses,
       "snapmirrorTotalFailures": snapmirrorTotalFailures,
       "snapmirrorTotalDeferments": snapmirrorTotalDeferments,
       "snapmirrorTotalTransMBs": snapmirrorTotalTransMBs,
       "snapmirrorTotalTransTimeSeconds": snapmirrorTotalTransTimeSeconds,
       "snapmirrorThrottleValue": snapmirrorThrottleValue,
       "snapmirrorMirrorTimestamp": snapmirrorMirrorTimestamp,
       "snapmirrorBaseSnapshot": snapmirrorBaseSnapshot,
       "snapmirrorLastTransType": snapmirrorLastTransType,
       "snapmirrorLastTransMBs": snapmirrorLastTransMBs,
       "snapmirrorLastTransTimeSeconds": snapmirrorLastTransTimeSeconds,
       "snapmirrorSchedule": snapmirrorSchedule,
       "snapmirrorScheduleDesc": snapmirrorScheduleDesc,
       "snapmirrorArguments": snapmirrorArguments,
       "snapmirrorSyncToAsync": snapmirrorSyncToAsync,
       "snapmirrorConnTable": snapmirrorConnTable,
       "snapmirrorConnEntry": snapmirrorConnEntry,
       "snapmirrorConnIndex": snapmirrorConnIndex,
       "snapmirrorConnName": snapmirrorConnName,
       "snapmirrorConnType": snapmirrorConnType,
       "snapmirrorConnSrc1": snapmirrorConnSrc1,
       "snapmirrorConnDst1": snapmirrorConnDst1,
       "snapmirrorConnSrc2": snapmirrorConnSrc2,
       "snapmirrorConnDst2": snapmirrorConnDst2,
       "ndmp": ndmp,
       "ndmpOn": ndmpOn,
       "ndmpSessionOpened": ndmpSessionOpened,
       "ndmpBackupActive": ndmpBackupActive,
       "ndmpRestoreActive": ndmpRestoreActive,
       "ndmpTapeActive": ndmpTapeActive,
       "ndmpBackupSuccesses": ndmpBackupSuccesses,
       "ndmpRestoreSuccesses": ndmpRestoreSuccesses,
       "ndmpBackupFailures": ndmpBackupFailures,
       "ndmpRestoreFailures": ndmpRestoreFailures,
       "ndmpBackupFailureReason": ndmpBackupFailureReason,
       "ndmpRestoreFailureReason": ndmpRestoreFailureReason,
       "fabric": fabric,
       "fabricInstances": fabricInstances,
       "fabricTable": fabricTable,
       "fabricEntry": fabricEntry,
       "fabricIndex": fabricIndex,
       "fabricStatus": fabricStatus,
       "fabricStatusMessage": fabricStatusMessage,
       "fabricName": fabricName,
       "fabricOwner": fabricOwner,
       "switchTable": switchTable,
       "switchEntry": switchEntry,
       "switchIndex": switchIndex,
       "switchName": switchName,
       "switchSymbolicName": switchSymbolicName,
       "switchType": switchType,
       "switchDomain": switchDomain,
       "switchManagementId": switchManagementId,
       "switchStatus": switchStatus,
       "switchStatusMessage": switchStatusMessage,
       "switchLinkSpeed": switchLinkSpeed,
       "switchHighPacketsProcessed": switchHighPacketsProcessed,
       "switchLowPacketsProcessed": switchLowPacketsProcessed,
       "switchHighPacketsRejected": switchHighPacketsRejected,
       "switchLowPacketsRejected": switchLowPacketsRejected,
       "switchFabricIndex": switchFabricIndex,
       "switch64PacketsProcessed": switch64PacketsProcessed,
       "switch64PacketsRejected": switch64PacketsRejected,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portName": portName,
       "portSwitchIndex": portSwitchIndex,
       "portSwitchName": portSwitchName,
       "portNumber": portNumber,
       "portType": portType,
       "portState": portState,
       "portFabricIndex": portFabricIndex,
       "dafs": dafs,
       "dafsOptions": dafsOptions,
       "dafsIsLicensed": dafsIsLicensed,
       "dafsMaxRequestsServer": dafsMaxRequestsServer,
       "dafsMaxRequests": dafsMaxRequests,
       "dafsMaxRequestSize": dafsMaxRequestSize,
       "dafsMaxResponseSize": dafsMaxResponseSize,
       "dafsMaxPendingRequestsServer": dafsMaxPendingRequestsServer,
       "dafsUseChecksums": dafsUseChecksums,
       "dafsNicNumRequestDemons": dafsNicNumRequestDemons,
       "dafsAnonymousAuthentication": dafsAnonymousAuthentication,
       "dafsServerEnabled": dafsServerEnabled,
       "dafsDefaultUid": dafsDefaultUid,
       "dafsDefaultGid": dafsDefaultGid,
       "dafsMaxDisconnectedSessions": dafsMaxDisconnectedSessions,
       "dafsMaxIdleSeconds": dafsMaxIdleSeconds,
       "dafsNicTable": dafsNicTable,
       "dafsNicEntry": dafsNicEntry,
       "dafsNicIndex": dafsNicIndex,
       "dafsNicName": dafsNicName,
       "dafsNicDevice": dafsNicDevice,
       "dafsNicState": dafsNicState,
       "dafsNicListenAddr": dafsNicListenAddr,
       "dafsNicNumRqstDemons": dafsNicNumRqstDemons,
       "dafsNicInBytes": dafsNicInBytes,
       "dafsNicDirectInBytes": dafsNicDirectInBytes,
       "dafsNicOutBytes": dafsNicOutBytes,
       "dafsNicDirectOutBytes": dafsNicDirectOutBytes,
       "curDafs": curDafs,
       "dafsPendingRequests": dafsPendingRequests,
       "dafsCurrentRequests": dafsCurrentRequests,
       "totDafs": totDafs,
       "dafsCalls": dafsCalls,
       "dafsClientAuths": dafsClientAuths,
       "dafsClientConnects": dafsClientConnects,
       "dafsClientConnectAuths": dafsClientConnectAuths,
       "dafsConnectBinds": dafsConnectBinds,
       "dafsDisconnects": dafsDisconnects,
       "dafsRegisterCreds": dafsRegisterCreds,
       "dafsReleaseCreds": dafsReleaseCreds,
       "dafsSecinfos": dafsSecinfos,
       "dafsServerAuths": dafsServerAuths,
       "dafsCheckResponses": dafsCheckResponses,
       "dafsFetchResponses": dafsFetchResponses,
       "dafsDiscardResponses": dafsDiscardResponses,
       "dafsAccesses": dafsAccesses,
       "dafsCacheHints": dafsCacheHints,
       "dafsCloses": dafsCloses,
       "dafsCommits": dafsCommits,
       "dafsCreates": dafsCreates,
       "dafsDelegPurges": dafsDelegPurges,
       "dafsDelegReturns": dafsDelegReturns,
       "dafsGetFsattrs": dafsGetFsattrs,
       "dafsGetRootHandles": dafsGetRootHandles,
       "dafsGetattrInlines": dafsGetattrInlines,
       "dafsGetattrDirects": dafsGetattrDirects,
       "dafsLinks": dafsLinks,
       "dafsLocks": dafsLocks,
       "dafsLockts": dafsLockts,
       "dafsLockus": dafsLockus,
       "dafsLookUps": dafsLookUps,
       "dafsLookUpps": dafsLookUpps,
       "dafsNulls": dafsNulls,
       "dafsNverifys": dafsNverifys,
       "dafsOpens": dafsOpens,
       "dafsOpenDowngrades": dafsOpenDowngrades,
       "dafsOpenattrs": dafsOpenattrs,
       "dafsReadInlines": dafsReadInlines,
       "dafsReadDirects": dafsReadDirects,
       "dafsReaddirInlines": dafsReaddirInlines,
       "dafsReaddirDirects": dafsReaddirDirects,
       "dafsReadlinkInlines": dafsReadlinkInlines,
       "dafsReadlinkDirects": dafsReadlinkDirects,
       "dafsRemoves": dafsRemoves,
       "dafsRenames": dafsRenames,
       "dafsSetattrInlines": dafsSetattrInlines,
       "dafsSetattrDirects": dafsSetattrDirects,
       "dafsVerifys": dafsVerifys,
       "dafsBatchSubmits": dafsBatchSubmits,
       "dafsWriteInlines": dafsWriteInlines,
       "dafsWriteDirects": dafsWriteDirects,
       "dafsBcGetattrs": dafsBcGetattrs,
       "dafsBcNulls": dafsBcNulls,
       "dafsBcRecalls": dafsBcRecalls,
       "dafsBcBatchCompletions": dafsBcBatchCompletions,
       "dafsAppendInlines": dafsAppendInlines,
       "dafsAppendDirects": dafsAppendDirects,
       "dafsGetFencingLists": dafsGetFencingLists,
       "dafsSetFencingLists": dafsSetFencingLists,
       "dafsHurryUps": dafsHurryUps,
       "dafsInBytes": dafsInBytes,
       "dafsDirectInBytes": dafsDirectInBytes,
       "dafsOutBytes": dafsOutBytes,
       "dafsDirectOutBytes": dafsDirectOutBytes,
       "dafsSessionTable": dafsSessionTable,
       "dafsSessionEntry": dafsSessionEntry,
       "dafsSessionIndex": dafsSessionIndex,
       "dafsSessionId": dafsSessionId,
       "dafsSessionEndian": dafsSessionEndian,
       "dafsSessionAllowBackChannel": dafsSessionAllowBackChannel,
       "dafsSessionAllowRdmaReadChannel": dafsSessionAllowRdmaReadChannel,
       "dafsSessionUseChecksums": dafsSessionUseChecksums,
       "dafsSessionMaxCredentials": dafsSessionMaxCredentials,
       "dafsSessionMaxRequestSize": dafsSessionMaxRequestSize,
       "dafsSessionMaxResponseSize": dafsSessionMaxResponseSize,
       "dafsSessionMaxRequests": dafsSessionMaxRequests,
       "dafsSessionInlineWriteHeaderSize": dafsSessionInlineWriteHeaderSize,
       "dafsSessionClientIdString": dafsSessionClientIdString,
       "dafsSessionClientVerifier": dafsSessionClientVerifier,
       "dafsSessionNumCredentials": dafsSessionNumCredentials,
       "dafsSessionNumRequests": dafsSessionNumRequests,
       "dafsExportTable": dafsExportTable,
       "dafsExportEntry": dafsExportEntry,
       "dafsExportIndex": dafsExportIndex,
       "dafsExportName": dafsExportName,
       "dafsExportPath": dafsExportPath,
       "dafsExportEnabled": dafsExportEnabled,
       "dafsExportRwMode": dafsExportRwMode,
       "dafsExportAccessList": dafsExportAccessList,
       "vi": vi,
       "viaNodeConnection": viaNodeConnection,
       "viaNodeSystemName": viaNodeSystemName,
       "viaCreated": viaCreated,
       "viaConnectRequest": viaConnectRequest,
       "viaConnectWait": viaConnectWait,
       "viaDisconnect": viaDisconnect,
       "viaConnectTimeOut": viaConnectTimeOut,
       "viaConnected": viaConnected,
       "viaCurrConnectPending": viaCurrConnectPending,
       "viaCurrConnectWaitPending": viaCurrConnectWaitPending,
       "viaCurrConnected": viaCurrConnected,
       "viaCurrError": viaCurrError,
       "viaTotalError": viaTotalError,
       "viaInMsgs": viaInMsgs,
       "viaInRdma": viaInRdma,
       "viaInBytes": viaInBytes,
       "viaInRDMAReadBytes": viaInRDMAReadBytes,
       "viaInRDMAWriteBytes": viaInRDMAWriteBytes,
       "viaOutMsgs": viaOutMsgs,
       "viaOutRdma": viaOutRdma,
       "viaOutBytes": viaOutBytes,
       "viaOutRDMAReadBytes": viaOutRDMAReadBytes,
       "viaOutRDMAWriteBytes": viaOutRDMAWriteBytes,
       "viaConnTable": viaConnTable,
       "viaConnEntry": viaConnEntry,
       "viaConnState": viaConnState,
       "viaConnVINumber": viaConnVINumber,
       "viaConnRemoteNetAddress": viaConnRemoteNetAddress,
       "viaConnLocalNetAddress": viaConnLocalNetAddress,
       "viaConnRemotePortNumber": viaConnRemotePortNumber,
       "viaConnLocalPortNumber": viaConnLocalPortNumber,
       "viaConnLocalDescriminator": viaConnLocalDescriminator,
       "viaConnRemoteDescriminator": viaConnRemoteDescriminator,
       "viaConnLocalMaxTransferSize": viaConnLocalMaxTransferSize,
       "viaConnRemoteMaxTransferSize": viaConnRemoteMaxTransferSize,
       "viaConnLocalEnableRdmaWrite": viaConnLocalEnableRdmaWrite,
       "viaConnLocalEnableRdmaRead": viaConnLocalEnableRdmaRead,
       "viaConnRemoteEnableRdmaWrite": viaConnRemoteEnableRdmaWrite,
       "viaConnRemoteEnableRdmaRead": viaConnRemoteEnableRdmaRead,
       "viaConnSentMessages": viaConnSentMessages,
       "viaConnSentRdmaReadMessages": viaConnSentRdmaReadMessages,
       "viaConnSentRdmaWriteMessages": viaConnSentRdmaWriteMessages,
       "viaConnRcvdMessages": viaConnRcvdMessages,
       "viaConnRcvdRdmaReadMessages": viaConnRcvdRdmaReadMessages,
       "viaConnRcvdRdmaWriteMessages": viaConnRcvdRdmaWriteMessages,
       "viaErrors": viaErrors,
       "viaErrPostDesc": viaErrPostDesc,
       "viaErrConnLost": viaErrConnLost,
       "viaErrRecvQEmpty": viaErrRecvQEmpty,
       "viaErrRdmawProt": viaErrRdmawProt,
       "viaErrRdmarProt": viaErrRdmarProt,
       "viaErrCompProt": viaErrCompProt,
       "viaErrorThreshold": viaErrorThreshold,
       "viaNicAttributes": viaNicAttributes,
       "viaNicTable": viaNicTable,
       "viaNicEntry": viaNicEntry,
       "viaNicIndex": viaNicIndex,
       "viaName": viaName,
       "viaHardwareVersion": viaHardwareVersion,
       "viaProviderVersion": viaProviderVersion,
       "viaNicAddress": viaNicAddress,
       "viaThreadSafe": viaThreadSafe,
       "viaMaxDiscriminatorLength": viaMaxDiscriminatorLength,
       "viaMaxRegisterBytes": viaMaxRegisterBytes,
       "viaMaxRegisterRegions": viaMaxRegisterRegions,
       "viaMaxRegisterBlockBytes": viaMaxRegisterBlockBytes,
       "viaMaxVI": viaMaxVI,
       "viaMaxDescriptorsPerQueue": viaMaxDescriptorsPerQueue,
       "viaMaxSegmentsPerDesc": viaMaxSegmentsPerDesc,
       "viaMaxCQ": viaMaxCQ,
       "viaMaxCQEntries": viaMaxCQEntries,
       "viaMaxTransferSize": viaMaxTransferSize,
       "viaNativeMTU": viaNativeMTU,
       "viaMaxPTags": viaMaxPTags,
       "viaCurrRegisterBytes": viaCurrRegisterBytes,
       "viaCurrRegisterRegions": viaCurrRegisterRegions,
       "viaCurrVI": viaCurrVI,
       "viaCurrCQ": viaCurrCQ,
       "viaCurrPTags": viaCurrPTags,
       "viaConnectionListenPort": viaConnectionListenPort,
       "backup": backup,
       "dump": dump,
       "dmpActives": dmpActives,
       "dmpAttempts": dmpAttempts,
       "dmpSuccesses": dmpSuccesses,
       "dmpFailures": dmpFailures,
       "dmpTable": dmpTable,
       "dmpEntry": dmpEntry,
       "dmpIndex": dmpIndex,
       "dmpStPath": dmpStPath,
       "dmpStAttempts": dmpStAttempts,
       "dmpStSuccesses": dmpStSuccesses,
       "dmpStFailures": dmpStFailures,
       "dmpTime": dmpTime,
       "dmpStatus": dmpStatus,
       "dmpLevel": dmpLevel,
       "dmpNumFiles": dmpNumFiles,
       "dmpDataAmount": dmpDataAmount,
       "dmpStartTime": dmpStartTime,
       "dmpDuration": dmpDuration,
       "restore": restore,
       "rstActives": rstActives,
       "rstAttempts": rstAttempts,
       "rstSuccesses": rstSuccesses,
       "rstFailures": rstFailures,
       "vfiler": vfiler,
       "vfilerIsLicensed": vfilerIsLicensed,
       "vfFilers": vfFilers,
       "vfTable": vfTable,
       "vfEntry": vfEntry,
       "vfIndex": vfIndex,
       "vfName": vfName,
       "vfUuid": vfUuid,
       "vfIpAddresses": vfIpAddresses,
       "vfStoragePaths": vfStoragePaths,
       "vfIpSpace": vfIpSpace,
       "vfAllowedProtocols": vfAllowedProtocols,
       "vfDisallowedProtocols": vfDisallowedProtocols,
       "vfState": vfState,
       "vfIpTable": vfIpTable,
       "vfIpEntry": vfIpEntry,
       "vfFiIndex": vfFiIndex,
       "vfIpIndex": vfIpIndex,
       "vfIpAddr": vfIpAddr,
       "vfSpTable": vfSpTable,
       "vfSpEntry": vfSpEntry,
       "vfFsIndex": vfFsIndex,
       "vfSpIndex": vfSpIndex,
       "vfSpName": vfSpName,
       "vfProTable": vfProTable,
       "vfProEntry": vfProEntry,
       "vfFpIndex": vfFpIndex,
       "vfProIndex": vfProIndex,
       "vfProName": vfProName,
       "vfProStatus": vfProStatus,
       "blocks": blocks,
       "fcpIsLicensed": fcpIsLicensed,
       "iscsiIsLicensed": iscsiIsLicensed,
       "fcpLowReadBytes": fcpLowReadBytes,
       "fcpHighReadBytes": fcpHighReadBytes,
       "fcpLowWriteBytes": fcpLowWriteBytes,
       "fcpHighWriteBytes": fcpHighWriteBytes,
       "iscsiLowReadBytes": iscsiLowReadBytes,
       "iscsiHighReadBytes": iscsiHighReadBytes,
       "iscsiLowWriteBytes": iscsiLowWriteBytes,
       "iscsiHighWriteBytes": iscsiHighWriteBytes,
       "iscsiHighOps": iscsiHighOps,
       "iscsiLowOps": iscsiLowOps,
       "fcpHighOps": fcpHighOps,
       "fcpLowOps": fcpLowOps,
       "lun": lun,
       "lunCount": lunCount,
       "lunTable": lunTable,
       "lunEntry": lunEntry,
       "lunIndex": lunIndex,
       "lunName": lunName,
       "lunComment": lunComment,
       "lunSizeLow": lunSizeLow,
       "lunSizeHigh": lunSizeHigh,
       "lunMapped": lunMapped,
       "lunSerialNumber": lunSerialNumber,
       "lunQtreeName": lunQtreeName,
       "lunHighOps": lunHighOps,
       "lunLowOps": lunLowOps,
       "lunHighReadBytes": lunHighReadBytes,
       "lunLowReadBytes": lunLowReadBytes,
       "lunHighWriteBytes": lunHighWriteBytes,
       "lunLowWriteBytes": lunLowWriteBytes,
       "lunHighErrors": lunHighErrors,
       "lunLowErrors": lunLowErrors,
       "lunOnline": lunOnline,
       "lunSnapStatus": lunSnapStatus,
       "lunShareStatus": lunShareStatus,
       "lunSpaceReserved": lunSpaceReserved,
       "lunStatsResetTime": lunStatsResetTime,
       "lunHighReadOps": lunHighReadOps,
       "lunLowReadOps": lunLowReadOps,
       "lunHighWriteOps": lunHighWriteOps,
       "lunLowWriteOps": lunLowWriteOps,
       "lunHighOtherOps": lunHighOtherOps,
       "lunLowOtherOps": lunLowOtherOps,
       "lunSize64": lunSize64,
       "lun64Ops": lun64Ops,
       "lun64ReadBytes": lun64ReadBytes,
       "lun64WriteBytes": lun64WriteBytes,
       "lun64Errors": lun64Errors,
       "lun64ReadOps": lun64ReadOps,
       "lun64WriteOps": lun64WriteOps,
       "lun64OtherOps": lun64OtherOps,
       "lunMapTable": lunMapTable,
       "lunMapEntry": lunMapEntry,
       "lunMapLUNIndex": lunMapLUNIndex,
       "lunMapInitiatorGroupIndex": lunMapInitiatorGroupIndex,
       "lunMapLUNName": lunMapLUNName,
       "lunMapInitiatorGroupName": lunMapInitiatorGroupName,
       "lunMapLogicalUnitNumber": lunMapLogicalUnitNumber,
       "initiator": initiator,
       "initiatorGroupTable": initiatorGroupTable,
       "initiatorGroupEntry": initiatorGroupEntry,
       "initiatorGroupIndex": initiatorGroupIndex,
       "initiatorGroupName": initiatorGroupName,
       "initiatorGroupType": initiatorGroupType,
       "initiatorGroupOS": initiatorGroupOS,
       "initiatorGroupThrottleReserve": initiatorGroupThrottleReserve,
       "initiatorGroupThrottleBorrow": initiatorGroupThrottleBorrow,
       "initiatorGroupUsePartner": initiatorGroupUsePartner,
       "initiatorGroupUseALUA": initiatorGroupUseALUA,
       "initiatorGroupMemberTable": initiatorGroupMemberTable,
       "initiatorGroupMemberEntry": initiatorGroupMemberEntry,
       "initiatorGroupMemberIndex": initiatorGroupMemberIndex,
       "initiatorGroupMemberNameIndex": initiatorGroupMemberNameIndex,
       "initiatorName": initiatorName,
       "initiatorListTable": initiatorListTable,
       "initiatorListEntry": initiatorListEntry,
       "initiatorListEntryIndex": initiatorListEntryIndex,
       "targetAdapterName": targetAdapterName,
       "connectedInitiatorNodeName": connectedInitiatorNodeName,
       "connectedInitiatorPortName": connectedInitiatorPortName,
       "connectedInitiatorType": connectedInitiatorType,
       "connectedInitiatorIsid": connectedInitiatorIsid,
       "connectedInitiatorPortalGroup": connectedInitiatorPortalGroup,
       "fcpTarget": fcpTarget,
       "fcpTargetTable": fcpTargetTable,
       "fcpTargetTableEntry": fcpTargetTableEntry,
       "fcpTargetTableIndex": fcpTargetTableIndex,
       "fcpTargetName": fcpTargetName,
       "fcpTargetNN": fcpTargetNN,
       "fcpTargetPN": fcpTargetPN,
       "fcpTargetSpeed": fcpTargetSpeed,
       "fcpTargetStatus": fcpTargetStatus,
       "fcpTargetStandby": fcpTargetStandby,
       "fcpTargetTopology": fcpTargetTopology,
       "fcpTargetType": fcpTargetType,
       "fcpCfMode": fcpCfMode,
       "pset": pset,
       "psetTable": psetTable,
       "psetEntry": psetEntry,
       "psetIndex": psetIndex,
       "psetName": psetName,
       "psetType": psetType,
       "psetMemberTable": psetMemberTable,
       "psetMemberEntry": psetMemberEntry,
       "psetMemberIndex": psetMemberIndex,
       "psetMemberNameIndex": psetMemberNameIndex,
       "psetPortName": psetPortName,
       "fcp64ReadBytes": fcp64ReadBytes,
       "fcp64WriteBytes": fcp64WriteBytes,
       "iscsi64ReadBytes": iscsi64ReadBytes,
       "iscsi64WriteBytes": iscsi64WriteBytes,
       "iscsi64Ops": iscsi64Ops,
       "fcp64Ops": fcp64Ops,
       "nfscache": nfscache,
       "nfsCacheOptions": nfsCacheOptions,
       "nfsCacheIsEnabled": nfsCacheIsEnabled,
       "nfsCacheIsLicensed": nfsCacheIsLicensed,
       "nfsCacheStats": nfsCacheStats,
       "nfsCacheBytesFromClients": nfsCacheBytesFromClients,
       "nfsCacheBytesToClients": nfsCacheBytesToClients,
       "nfsCacheBytesFromServers": nfsCacheBytesFromServers,
       "nfsCacheBytesToServers": nfsCacheBytesToServers,
       "nfsCacheTotalRequests": nfsCacheTotalRequests,
       "nfsCacheHitRequests": nfsCacheHitRequests,
       "nfsCacheMissRequests": nfsCacheMissRequests,
       "nfsCacheMissCacheableRequests": nfsCacheMissCacheableRequests,
       "nfsCacheMissUnCacheableRequests": nfsCacheMissUnCacheableRequests,
       "nfsCacheEjectRequests": nfsCacheEjectRequests,
       "nfsCacheVerifyRequests": nfsCacheVerifyRequests,
       "nfsCacheRpcRecords": nfsCacheRpcRecords,
       "nfsCacheBWSavings": nfsCacheBWSavings,
       "nfsCacheHighBytesFromClients": nfsCacheHighBytesFromClients,
       "nfsCacheLowBytesFromClients": nfsCacheLowBytesFromClients,
       "nfsCacheHighBytesToClients": nfsCacheHighBytesToClients,
       "nfsCacheLowBytesToClients": nfsCacheLowBytesToClients,
       "nfsCacheHighBytesFromServers": nfsCacheHighBytesFromServers,
       "nfsCacheLowBytesFromServers": nfsCacheLowBytesFromServers,
       "nfsCacheHighBytesToServers": nfsCacheHighBytesToServers,
       "nfsCacheLowBytesToServers": nfsCacheLowBytesToServers,
       "nfsCacheHighTotalRequests": nfsCacheHighTotalRequests,
       "nfsCacheLowTotalRequests": nfsCacheLowTotalRequests,
       "nfsCacheHighHitRequests": nfsCacheHighHitRequests,
       "nfsCacheLowHitRequests": nfsCacheLowHitRequests,
       "nfsCacheHighMissRequests": nfsCacheHighMissRequests,
       "nfsCacheLowMissRequests": nfsCacheLowMissRequests,
       "nfsCache64BytesFromClients": nfsCache64BytesFromClients,
       "nfsCache64BytesToClients": nfsCache64BytesToClients,
       "nfsCache64BytesFromServers": nfsCache64BytesFromServers,
       "nfsCache64BytesToServers": nfsCache64BytesToServers,
       "nfsCache64TotalRequests": nfsCache64TotalRequests,
       "nfsCache64HitRequests": nfsCache64HitRequests,
       "nfsCache64MissRequests": nfsCache64MissRequests,
       "snapvault": snapvault,
       "svOn": svOn,
       "svSystemActiveDstNumber": svSystemActiveDstNumber,
       "svSystemActiveSrcNumber": svSystemActiveSrcNumber,
       "svSystemTotalPrimarySuccesses": svSystemTotalPrimarySuccesses,
       "svSystemTotalSecondarySuccesses": svSystemTotalSecondarySuccesses,
       "svSystemTotalPrimaryFailures": svSystemTotalPrimaryFailures,
       "svSystemTotalSecondaryFailures": svSystemTotalSecondaryFailures,
       "svSystemTotalSecondaryDeferments": svSystemTotalSecondaryDeferments,
       "svPrimaryIsLicensed": svPrimaryIsLicensed,
       "svSecondaryIsLicensed": svSecondaryIsLicensed,
       "snapvaultStatusTable": snapvaultStatusTable,
       "snapvaultStatusEntry": snapvaultStatusEntry,
       "svIndex": svIndex,
       "svSrc": svSrc,
       "svDst": svDst,
       "svStatus": svStatus,
       "svState": svState,
       "svLag": svLag,
       "svTotalSuccesses": svTotalSuccesses,
       "svTotalRestartSuccesses": svTotalRestartSuccesses,
       "svTotalFailures": svTotalFailures,
       "svTotalDeferments": svTotalDeferments,
       "svTotalTransMBs": svTotalTransMBs,
       "svTotalTransTimeSeconds": svTotalTransTimeSeconds,
       "svThrottleValue": svThrottleValue,
       "svSrcSnapshotTime": svSrcSnapshotTime,
       "svBaseSnapshot": svBaseSnapshot,
       "svLastTransType": svLastTransType,
       "svLastTransMBs": svLastTransMBs,
       "svLastTransTimeSeconds": svLastTransTimeSeconds,
       "snapvaultHostTable": snapvaultHostTable,
       "snapvaultHostEntry": snapvaultHostEntry,
       "svHostIndex": svHostIndex,
       "svHostName": svHostName,
       "svHostType": svHostType,
       "svHostTotalSuccesses": svHostTotalSuccesses,
       "svHostTotalFailures": svHostTotalFailures,
       "svHostTotalDeferments": svHostTotalDeferments,
       "snapvaultSchedTable": snapvaultSchedTable,
       "snapvaultSchedEntry": snapvaultSchedEntry,
       "svSchedIndex": svSchedIndex,
       "svSchedVolume": svSchedVolume,
       "svSchedSnapshot": svSchedSnapshot,
       "svSchedStatus": svSchedStatus,
       "svSchedType": svSchedType,
       "svSchedSchedule": svSchedSchedule,
       "svDrPrimaryIsLicensed": svDrPrimaryIsLicensed,
       "ftpd": ftpd,
       "ftpdOn": ftpdOn,
       "ftpdCurrentConns": ftpdCurrentConns,
       "ftpdMaxConns": ftpdMaxConns,
       "ftpdTotalConns": ftpdTotalConns,
       "storage": storage,
       "enclosure": enclosure,
       "enclNumber": enclNumber,
       "enclTable": enclTable,
       "enclEntry": enclEntry,
       "enclIndex": enclIndex,
       "enclContactState": enclContactState,
       "enclChannelShelfAddr": enclChannelShelfAddr,
       "enclProductLogicalID": enclProductLogicalID,
       "enclProductID": enclProductID,
       "enclProductVendor": enclProductVendor,
       "enclProductModel": enclProductModel,
       "enclProductRevision": enclProductRevision,
       "enclProductSerialNo": enclProductSerialNo,
       "enclNumberDiskBays": enclNumberDiskBays,
       "enclDisksPresent": enclDisksPresent,
       "enclPowerSuppliesMaximum": enclPowerSuppliesMaximum,
       "enclPowerSuppliesPresent": enclPowerSuppliesPresent,
       "enclPowerSuppliesSerialNos": enclPowerSuppliesSerialNos,
       "enclPowerSuppliesFailed": enclPowerSuppliesFailed,
       "enclFansMaximum": enclFansMaximum,
       "enclFansPresent": enclFansPresent,
       "enclFansFailed": enclFansFailed,
       "enclTempSensorsMaximum": enclTempSensorsMaximum,
       "enclTempSensorsPresent": enclTempSensorsPresent,
       "enclTempSensorsOverTempFail": enclTempSensorsOverTempFail,
       "enclTempSensorsOverTempWarn": enclTempSensorsOverTempWarn,
       "enclTempSensorsUnderTempFail": enclTempSensorsUnderTempFail,
       "enclTempSensorsUnderTempWarn": enclTempSensorsUnderTempWarn,
       "enclTempSensorsCurrentTemp": enclTempSensorsCurrentTemp,
       "enclTempSensorsOverTempFailThr": enclTempSensorsOverTempFailThr,
       "enclTempSensorsOverTempWarnThr": enclTempSensorsOverTempWarnThr,
       "enclTempSensorsUnderTempFailThr": enclTempSensorsUnderTempFailThr,
       "enclTempSensorsUnderTempWarnThr": enclTempSensorsUnderTempWarnThr,
       "enclElectronicsMaximum": enclElectronicsMaximum,
       "enclElectronicsPresent": enclElectronicsPresent,
       "enclElectronicsSerialNos": enclElectronicsSerialNos,
       "enclElectronicsFailed": enclElectronicsFailed,
       "enclVoltSensorsMaximum": enclVoltSensorsMaximum,
       "enclVoltSensorsPresent": enclVoltSensorsPresent,
       "enclVoltSensorsOverVoltFail": enclVoltSensorsOverVoltFail,
       "enclVoltSensorsOverVoltWarn": enclVoltSensorsOverVoltWarn,
       "enclVoltSensorsUnderVoltFail": enclVoltSensorsUnderVoltFail,
       "enclVoltSensorsUnderVoltWarn": enclVoltSensorsUnderVoltWarn,
       "enclVoltSensorsCurrentVolt": enclVoltSensorsCurrentVolt,
       "enclVoltSensorsOverVoltFailThr": enclVoltSensorsOverVoltFailThr,
       "enclVoltSensorsOverVoltWarnThr": enclVoltSensorsOverVoltWarnThr,
       "enclVoltSensorsUnderVoltFailThr": enclVoltSensorsUnderVoltFailThr,
       "enclVoltSensorsUnderVoltWarnThr": enclVoltSensorsUnderVoltWarnThr,
       "enclCurSensorsMaximum": enclCurSensorsMaximum,
       "enclCurSensorsPresent": enclCurSensorsPresent,
       "enclCurSensorsOverCurFail": enclCurSensorsOverCurFail,
       "enclCurSensorsOverCurWarn": enclCurSensorsOverCurWarn,
       "enclCurSensorsCurrentCur": enclCurSensorsCurrentCur,
       "enclCurSensorsOverCurFailThr": enclCurSensorsOverCurFailThr,
       "enclCurSensorsOverCurWarnThr": enclCurSensorsOverCurWarnThr,
       "network": network,
       "netInterfaces": netInterfaces,
       "netifNumber": netifNumber,
       "netifTable": netifTable,
       "netifEntry": netifEntry,
       "netifIndex": netifIndex,
       "netifDescr": netifDescr,
       "ifHighInOctets": ifHighInOctets,
       "ifLowInOctets": ifLowInOctets,
       "ifHighInUcastPkts": ifHighInUcastPkts,
       "ifLowInUcastPkts": ifLowInUcastPkts,
       "ifHighInNUcastPkts": ifHighInNUcastPkts,
       "ifLowInNUcastPkts": ifLowInNUcastPkts,
       "ifHighInDiscards": ifHighInDiscards,
       "ifLowInDiscards": ifLowInDiscards,
       "ifHighInErrors": ifHighInErrors,
       "ifLowInErrors": ifLowInErrors,
       "ifHighInUnknownProtos": ifHighInUnknownProtos,
       "ifLowInUnknownProtos": ifLowInUnknownProtos,
       "ifHighOutOctets": ifHighOutOctets,
       "ifLowOutOctets": ifLowOutOctets,
       "ifHighOutUcastPkts": ifHighOutUcastPkts,
       "ifLowOutUcastPkts": ifLowOutUcastPkts,
       "ifHighOutNUcastPkts": ifHighOutNUcastPkts,
       "ifLowOutNUcastPkts": ifLowOutNUcastPkts,
       "ifHighOutDiscards": ifHighOutDiscards,
       "ifLowOutDiscards": ifLowOutDiscards,
       "ifHighOutErrors": ifHighOutErrors,
       "ifLowOutErrors": ifLowOutErrors,
       "if64InOctets": if64InOctets,
       "if64InUcastPkts": if64InUcastPkts,
       "if64InNUcastPkts": if64InNUcastPkts,
       "if64InDiscards": if64InDiscards,
       "if64InErrors": if64InErrors,
       "if64InUnknownProtos": if64InUnknownProtos,
       "if64OutOctets": if64OutOctets,
       "if64OutUcastPkts": if64OutUcastPkts,
       "if64OutNUcastPkts": if64OutNUcastPkts,
       "if64OutDiscards": if64OutDiscards,
       "if64OutErrors": if64OutErrors,
       "sis": sis,
       "sisIsLicensed": sisIsLicensed,
       "sisTable": sisTable,
       "sisEntry": sisEntry,
       "sisIndex": sisIndex,
       "sisPath": sisPath,
       "sisState": sisState,
       "sisStatus": sisStatus,
       "sisProgress": sisProgress,
       "sisType": sisType,
       "sisSchedule": sisSchedule,
       "sisLastOpBeginTime": sisLastOpBeginTime,
       "sisLastOpEndTime": sisLastOpEndTime,
       "sisHighLastOpSize": sisHighLastOpSize,
       "sisLowLastOpSize": sisLowLastOpSize,
       "sisLastOpError": sisLastOpError,
       "sis64LastOpSize": sis64LastOpSize,
       "compress": compress,
       "compressIsLicensed": compressIsLicensed,
       "compressTable": compressTable,
       "compressEntry": compressEntry,
       "compressIndex": compressIndex,
       "compressFileSys": compressFileSys,
       "compressHighUsedKBytes": compressHighUsedKBytes,
       "compressLowUsedKBytes": compressLowUsedKBytes,
       "compress64UsedKBytes": compress64UsedKBytes,
       "compressHighSavedKBytes": compressHighSavedKBytes,
       "compressLowSavedKBytes": compressLowSavedKBytes,
       "compress64SavedKBytes": compress64SavedKBytes,
       "compressPercentSaved": compressPercentSaved,
       "netappProducts": netappProducts,
       "netappFiler": netappFiler,
       "netappNetCache": netappNetCache,
       "netappClusteredFiler": netappClusteredFiler,
       "netappNode": netappNode,
       "netappDataFabricManager": netappDataFabricManager,
       "netappSupportConsole": netappSupportConsole,
       "netappModuleId": netappModuleId}
)
