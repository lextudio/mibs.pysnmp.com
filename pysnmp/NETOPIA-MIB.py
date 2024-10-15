# SNMP MIB module (NETOPIA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETOPIA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:39 2024
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

(DdpAddress,) = mibBuilder.importSymbols(
    "RFC1243-MIB",
    "DdpAddress")

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



class ATNetworkNumber(OctetString):
    """Custom type ATNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )





class HostNameOrIpAddr(OctetString):
    """Custom type HostNameOrIpAddr based on OctetString"""




class UInteger(Gauge32):
    """Custom type UInteger based on Gauge32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Farallon_ObjectIdentity = ObjectIdentity
farallon = _Farallon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304)
)
_Netopia_ObjectIdentity = ObjectIdentity
netopia = _Netopia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1)
)
_SysParams_ObjectIdentity = ObjectIdentity
sysParams = _SysParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 1)
)


class _HwVersion_Type(OctetString):
    """Custom type hwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HwVersion_Type.__name__ = "OctetString"
_HwVersion_Object = MibScalar
hwVersion = _HwVersion_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 1, 1),
    _HwVersion_Type()
)
hwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVersion.setStatus("mandatory")


class _FwVersion_Type(OctetString):
    """Custom type fwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_FwVersion_Type.__name__ = "OctetString"
_FwVersion_Object = MibScalar
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 1, 2),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("mandatory")


class _ProductMIBVersion_Type(OctetString):
    """Custom type productMIBVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ProductMIBVersion_Type.__name__ = "OctetString"
_ProductMIBVersion_Object = MibScalar
productMIBVersion = _ProductMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 1, 3),
    _ProductMIBVersion_Type()
)
productMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMIBVersion.setStatus("mandatory")


class _SerialNumber_Type(OctetString):
    """Custom type serialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SerialNumber_Type.__name__ = "OctetString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 1, 4),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")
_ModelNumber_Type = Integer32
_ModelNumber_Object = MibScalar
modelNumber = _ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 1, 5),
    _ModelNumber_Type()
)
modelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelNumber.setStatus("mandatory")
_ClockParams_ObjectIdentity = ObjectIdentity
clockParams = _ClockParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 2)
)
_BootTime_Type = DisplayString
_BootTime_Object = MibScalar
bootTime = _BootTime_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 2, 1),
    _BootTime_Type()
)
bootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootTime.setStatus("mandatory")


class _SystemClock_Type(OctetString):
    """Custom type systemClock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_SystemClock_Type.__name__ = "OctetString"
_SystemClock_Object = MibScalar
systemClock = _SystemClock_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 2, 2),
    _SystemClock_Type()
)
systemClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemClock.setStatus("mandatory")
_SysStats_ObjectIdentity = ObjectIdentity
sysStats = _SysStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 3)
)


class _CurrentCpuUtil_Type(Integer32):
    """Custom type currentCpuUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CurrentCpuUtil_Type.__name__ = "Integer32"
_CurrentCpuUtil_Object = MibScalar
currentCpuUtil = _CurrentCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 3, 1),
    _CurrentCpuUtil_Type()
)
currentCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentCpuUtil.setStatus("mandatory")


class _AverageCpuUtil_Type(Integer32):
    """Custom type averageCpuUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AverageCpuUtil_Type.__name__ = "Integer32"
_AverageCpuUtil_Object = MibScalar
averageCpuUtil = _AverageCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 3, 2),
    _AverageCpuUtil_Type()
)
averageCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageCpuUtil.setStatus("mandatory")


class _CurrentBufs_Type(Integer32):
    """Custom type currentBufs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CurrentBufs_Type.__name__ = "Integer32"
_CurrentBufs_Object = MibScalar
currentBufs = _CurrentBufs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 3, 3),
    _CurrentBufs_Type()
)
currentBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentBufs.setStatus("mandatory")


class _AverageBufs_Type(Integer32):
    """Custom type averageBufs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AverageBufs_Type.__name__ = "Integer32"
_AverageBufs_Object = MibScalar
averageBufs = _AverageBufs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 3, 4),
    _AverageBufs_Type()
)
averageBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageBufs.setStatus("mandatory")
_TotalRAM_Type = Integer32
_TotalRAM_Object = MibScalar
totalRAM = _TotalRAM_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 3, 5),
    _TotalRAM_Type()
)
totalRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRAM.setStatus("mandatory")
_UsedRAM_Type = Integer32
_UsedRAM_Object = MibScalar
usedRAM = _UsedRAM_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 3, 6),
    _UsedRAM_Type()
)
usedRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedRAM.setStatus("mandatory")
_TotalFEPROM_Type = Integer32
_TotalFEPROM_Object = MibScalar
totalFEPROM = _TotalFEPROM_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 3, 7),
    _TotalFEPROM_Type()
)
totalFEPROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalFEPROM.setStatus("mandatory")
_UsedFEPROM_Type = Integer32
_UsedFEPROM_Object = MibScalar
usedFEPROM = _UsedFEPROM_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 3, 8),
    _UsedFEPROM_Type()
)
usedFEPROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedFEPROM.setStatus("mandatory")
_IpParams_ObjectIdentity = ObjectIdentity
ipParams = _IpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 4)
)
_IpAddr_Type = IpAddress
_IpAddr_Object = MibScalar
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 4, 1),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddr.setStatus("mandatory")
_IpNetMask_Type = IpAddress
_IpNetMask_Object = MibScalar
ipNetMask = _IpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 4, 2),
    _IpNetMask_Type()
)
ipNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetMask.setStatus("mandatory")


class _IpBcastForm_Type(Integer32):
    """Custom type ipBcastForm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 1),
          ("allZeros", 2))
    )


_IpBcastForm_Type.__name__ = "Integer32"
_IpBcastForm_Object = MibScalar
ipBcastForm = _IpBcastForm_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 4, 3),
    _IpBcastForm_Type()
)
ipBcastForm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBcastForm.setStatus("mandatory")


class _IpEncap_Type(Integer32):
    """Custom type ipEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8022", 2))
    )


_IpEncap_Type.__name__ = "Integer32"
_IpEncap_Object = MibScalar
ipEncap = _IpEncap_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 4, 4),
    _IpEncap_Type()
)
ipEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipEncap.setStatus("mandatory")
_IpDefaultGateway_Type = IpAddress
_IpDefaultGateway_Object = MibScalar
ipDefaultGateway = _IpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 4, 5),
    _IpDefaultGateway_Type()
)
ipDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDefaultGateway.setStatus("mandatory")
_IpDomainName_Type = OctetString
_IpDomainName_Object = MibScalar
ipDomainName = _IpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 4, 6),
    _IpDomainName_Type()
)
ipDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDomainName.setStatus("mandatory")
_IpDNSServerTable_Object = MibTable
ipDNSServerTable = _IpDNSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 4, 7)
)
if mibBuilder.loadTexts:
    ipDNSServerTable.setStatus("mandatory")
_IpDNSServerEntry_Object = MibTableRow
ipDNSServerEntry = _IpDNSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 4, 7, 1)
)
ipDNSServerEntry.setIndexNames(
    (0, "NETOPIA-MIB", "ipDNSServerIndex"),
)
if mibBuilder.loadTexts:
    ipDNSServerEntry.setStatus("mandatory")
_IpDNSServerIndex_Type = Integer32
_IpDNSServerIndex_Object = MibTableColumn
ipDNSServerIndex = _IpDNSServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 4, 7, 1, 1),
    _IpDNSServerIndex_Type()
)
ipDNSServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDNSServerIndex.setStatus("mandatory")
_IpDNSServerAddress_Type = IpAddress
_IpDNSServerAddress_Object = MibTableColumn
ipDNSServerAddress = _IpDNSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 4, 7, 1, 2),
    _IpDNSServerAddress_Type()
)
ipDNSServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDNSServerAddress.setStatus("mandatory")


class _IpDNSServerStatus_Type(Integer32):
    """Custom type ipDNSServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_IpDNSServerStatus_Type.__name__ = "Integer32"
_IpDNSServerStatus_Object = MibTableColumn
ipDNSServerStatus = _IpDNSServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 4, 7, 1, 3),
    _IpDNSServerStatus_Type()
)
ipDNSServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDNSServerStatus.setStatus("mandatory")
_RipParams_ObjectIdentity = ObjectIdentity
ripParams = _RipParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 5)
)


class _RipEnTxEnable_Type(Integer32):
    """Custom type ripEnTxEnable based on Integer32"""
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


_RipEnTxEnable_Type.__name__ = "Integer32"
_RipEnTxEnable_Object = MibScalar
ripEnTxEnable = _RipEnTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 5, 1),
    _RipEnTxEnable_Type()
)
ripEnTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripEnTxEnable.setStatus("mandatory")


class _RipEnRxEnable_Type(Integer32):
    """Custom type ripEnRxEnable based on Integer32"""
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


_RipEnRxEnable_Type.__name__ = "Integer32"
_RipEnRxEnable_Object = MibScalar
ripEnRxEnable = _RipEnRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 5, 2),
    _RipEnRxEnable_Type()
)
ripEnRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripEnRxEnable.setStatus("mandatory")
_AtParams_ObjectIdentity = ObjectIdentity
atParams = _AtParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6)
)
_AtportXTable_Object = MibTable
atportXTable = _AtportXTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    atportXTable.setStatus("mandatory")
_AtportXEntry_Object = MibTableRow
atportXEntry = _AtportXEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 1, 1)
)
atportXEntry.setIndexNames(
    (0, "NETOPIA-MIB", "atportXIndex"),
)
if mibBuilder.loadTexts:
    atportXEntry.setStatus("mandatory")
_AtportXIndex_Type = Integer32
_AtportXIndex_Object = MibTableColumn
atportXIndex = _AtportXIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 1, 1, 1),
    _AtportXIndex_Type()
)
atportXIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportXIndex.setStatus("mandatory")


class _AtportXHide_Type(Integer32):
    """Custom type atportXHide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 2),
          ("visible", 1))
    )


_AtportXHide_Type.__name__ = "Integer32"
_AtportXHide_Object = MibTableColumn
atportXHide = _AtportXHide_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 1, 1, 2),
    _AtportXHide_Type()
)
atportXHide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportXHide.setStatus("mandatory")


class _AtportXSeed_Type(Integer32):
    """Custom type atportXSeed based on Integer32"""
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
        *(("hardseed", 3),
          ("noseed", 4),
          ("other", 1),
          ("softseed", 2))
    )


_AtportXSeed_Type.__name__ = "Integer32"
_AtportXSeed_Object = MibTableColumn
atportXSeed = _AtportXSeed_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 1, 1, 3),
    _AtportXSeed_Type()
)
atportXSeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportXSeed.setStatus("mandatory")
_AtportZoneTable_Object = MibTable
atportZoneTable = _AtportZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    atportZoneTable.setStatus("mandatory")
_AtportZoneEntry_Object = MibTableRow
atportZoneEntry = _AtportZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 2, 1)
)
atportZoneEntry.setIndexNames(
    (0, "NETOPIA-MIB", "atportZonePort"),
    (0, "NETOPIA-MIB", "atportZoneName"),
)
if mibBuilder.loadTexts:
    atportZoneEntry.setStatus("mandatory")
_AtportZonePort_Type = Integer32
_AtportZonePort_Object = MibTableColumn
atportZonePort = _AtportZonePort_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 2, 1, 1),
    _AtportZonePort_Type()
)
atportZonePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportZonePort.setStatus("mandatory")


class _AtportZoneName_Type(OctetString):
    """Custom type atportZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AtportZoneName_Type.__name__ = "OctetString"
_AtportZoneName_Object = MibTableColumn
atportZoneName = _AtportZoneName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 2, 1, 2),
    _AtportZoneName_Type()
)
atportZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportZoneName.setStatus("mandatory")


class _AtportZoneDefault_Type(Integer32):
    """Custom type atportZoneDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("notDefault", 2))
    )


_AtportZoneDefault_Type.__name__ = "Integer32"
_AtportZoneDefault_Object = MibTableColumn
atportZoneDefault = _AtportZoneDefault_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 2, 1, 3),
    _AtportZoneDefault_Type()
)
atportZoneDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportZoneDefault.setStatus("mandatory")


class _AtportZoneStatus_Type(Integer32):
    """Custom type atportZoneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AtportZoneStatus_Type.__name__ = "Integer32"
_AtportZoneStatus_Object = MibTableColumn
atportZoneStatus = _AtportZoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 2, 1, 4),
    _AtportZoneStatus_Type()
)
atportZoneStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportZoneStatus.setStatus("mandatory")
_AtportTrafficTable_Object = MibTable
atportTrafficTable = _AtportTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 3)
)
if mibBuilder.loadTexts:
    atportTrafficTable.setStatus("mandatory")
_AtportTrafficEntry_Object = MibTableRow
atportTrafficEntry = _AtportTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 3, 1)
)
atportTrafficEntry.setIndexNames(
    (0, "NETOPIA-MIB", "atportTrafficIndex"),
)
if mibBuilder.loadTexts:
    atportTrafficEntry.setStatus("mandatory")
_AtportTrafficIndex_Type = Integer32
_AtportTrafficIndex_Object = MibTableColumn
atportTrafficIndex = _AtportTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 3, 1, 1),
    _AtportTrafficIndex_Type()
)
atportTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportTrafficIndex.setStatus("mandatory")
_AtportTrafficRxBytes_Type = Counter32
_AtportTrafficRxBytes_Object = MibTableColumn
atportTrafficRxBytes = _AtportTrafficRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 3, 1, 2),
    _AtportTrafficRxBytes_Type()
)
atportTrafficRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportTrafficRxBytes.setStatus("mandatory")
_AtportTrafficRxPackets_Type = Counter32
_AtportTrafficRxPackets_Object = MibTableColumn
atportTrafficRxPackets = _AtportTrafficRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 3, 1, 3),
    _AtportTrafficRxPackets_Type()
)
atportTrafficRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportTrafficRxPackets.setStatus("mandatory")
_AtportTrafficTxBytes_Type = Counter32
_AtportTrafficTxBytes_Object = MibTableColumn
atportTrafficTxBytes = _AtportTrafficTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 3, 1, 4),
    _AtportTrafficTxBytes_Type()
)
atportTrafficTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportTrafficTxBytes.setStatus("mandatory")
_AtportTrafficTxPackets_Type = Counter32
_AtportTrafficTxPackets_Object = MibTableColumn
atportTrafficTxPackets = _AtportTrafficTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 3, 1, 5),
    _AtportTrafficTxPackets_Type()
)
atportTrafficTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atportTrafficTxPackets.setStatus("mandatory")


class _DeviceNBPObject_Type(OctetString):
    """Custom type deviceNBPObject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DeviceNBPObject_Type.__name__ = "OctetString"
_DeviceNBPObject_Object = MibScalar
deviceNBPObject = _DeviceNBPObject_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 6, 4),
    _DeviceNBPObject_Type()
)
deviceNBPObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceNBPObject.setStatus("mandatory")
_MacipParams_ObjectIdentity = ObjectIdentity
macipParams = _MacipParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7)
)


class _MacipSupport_Type(Integer32):
    """Custom type macipSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("ipSubnetting", 2),
          ("kipForwarding", 3))
    )


_MacipSupport_Type.__name__ = "Integer32"
_MacipSupport_Object = MibScalar
macipSupport = _MacipSupport_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 1),
    _MacipSupport_Type()
)
macipSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macipSupport.setStatus("mandatory")
_MacipIpSubIpAddr_Type = IpAddress
_MacipIpSubIpAddr_Object = MibScalar
macipIpSubIpAddr = _MacipIpSubIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 2),
    _MacipIpSubIpAddr_Type()
)
macipIpSubIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macipIpSubIpAddr.setStatus("mandatory")
_MacipIpSubNetMask_Type = IpAddress
_MacipIpSubNetMask_Object = MibScalar
macipIpSubNetMask = _MacipIpSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 3),
    _MacipIpSubNetMask_Type()
)
macipIpSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macipIpSubNetMask.setStatus("mandatory")
_MacipFirstClientIpAddr_Type = IpAddress
_MacipFirstClientIpAddr_Object = MibScalar
macipFirstClientIpAddr = _MacipFirstClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 4),
    _MacipFirstClientIpAddr_Type()
)
macipFirstClientIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macipFirstClientIpAddr.setStatus("mandatory")
_MacipNumStaticAddrs_Type = Integer32
_MacipNumStaticAddrs_Object = MibScalar
macipNumStaticAddrs = _MacipNumStaticAddrs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 5),
    _MacipNumStaticAddrs_Type()
)
macipNumStaticAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macipNumStaticAddrs.setStatus("mandatory")
_MacipNumDynamicAddrs_Type = Integer32
_MacipNumDynamicAddrs_Object = MibScalar
macipNumDynamicAddrs = _MacipNumDynamicAddrs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 6),
    _MacipNumDynamicAddrs_Type()
)
macipNumDynamicAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macipNumDynamicAddrs.setStatus("mandatory")
_MacipMaxAddrs_Type = Integer32
_MacipMaxAddrs_Object = MibScalar
macipMaxAddrs = _MacipMaxAddrs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 7),
    _MacipMaxAddrs_Type()
)
macipMaxAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipMaxAddrs.setStatus("mandatory")
_MacipUnusedDynamicAddrs_Type = Gauge32
_MacipUnusedDynamicAddrs_Object = MibScalar
macipUnusedDynamicAddrs = _MacipUnusedDynamicAddrs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 8),
    _MacipUnusedDynamicAddrs_Type()
)
macipUnusedDynamicAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipUnusedDynamicAddrs.setStatus("mandatory")
_MacipAssignRequests_Type = Counter32
_MacipAssignRequests_Object = MibScalar
macipAssignRequests = _MacipAssignRequests_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 9),
    _MacipAssignRequests_Type()
)
macipAssignRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipAssignRequests.setStatus("mandatory")
_MacipServerRequests_Type = Counter32
_MacipServerRequests_Object = MibScalar
macipServerRequests = _MacipServerRequests_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 10),
    _MacipServerRequests_Type()
)
macipServerRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipServerRequests.setStatus("mandatory")
_MacipRefusedAssignRequests_Type = Counter32
_MacipRefusedAssignRequests_Object = MibScalar
macipRefusedAssignRequests = _MacipRefusedAssignRequests_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 11),
    _MacipRefusedAssignRequests_Type()
)
macipRefusedAssignRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipRefusedAssignRequests.setStatus("mandatory")
_MacipBadRequests_Type = Counter32
_MacipBadRequests_Object = MibScalar
macipBadRequests = _MacipBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 12),
    _MacipBadRequests_Type()
)
macipBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipBadRequests.setStatus("mandatory")
_MacipForwardedAtFrames_Type = Counter32
_MacipForwardedAtFrames_Object = MibScalar
macipForwardedAtFrames = _MacipForwardedAtFrames_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 13),
    _MacipForwardedAtFrames_Type()
)
macipForwardedAtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipForwardedAtFrames.setStatus("mandatory")
_MacipForwardedAtOctets_Type = Counter32
_MacipForwardedAtOctets_Object = MibScalar
macipForwardedAtOctets = _MacipForwardedAtOctets_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 14),
    _MacipForwardedAtOctets_Type()
)
macipForwardedAtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipForwardedAtOctets.setStatus("mandatory")
_MacipDroppedAtFrames_Type = Counter32
_MacipDroppedAtFrames_Object = MibScalar
macipDroppedAtFrames = _MacipDroppedAtFrames_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 15),
    _MacipDroppedAtFrames_Type()
)
macipDroppedAtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipDroppedAtFrames.setStatus("mandatory")
_MacipForwardedIpFrames_Type = Counter32
_MacipForwardedIpFrames_Object = MibScalar
macipForwardedIpFrames = _MacipForwardedIpFrames_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 16),
    _MacipForwardedIpFrames_Type()
)
macipForwardedIpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipForwardedIpFrames.setStatus("mandatory")
_MacipForwardedIpOctets_Type = Counter32
_MacipForwardedIpOctets_Object = MibScalar
macipForwardedIpOctets = _MacipForwardedIpOctets_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 17),
    _MacipForwardedIpOctets_Type()
)
macipForwardedIpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipForwardedIpOctets.setStatus("mandatory")
_MacipDroppedIpFrames_Type = Counter32
_MacipDroppedIpFrames_Object = MibScalar
macipDroppedIpFrames = _MacipDroppedIpFrames_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 18),
    _MacipDroppedIpFrames_Type()
)
macipDroppedIpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipDroppedIpFrames.setStatus("mandatory")
_MacipClientTable_Object = MibTable
macipClientTable = _MacipClientTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 19)
)
if mibBuilder.loadTexts:
    macipClientTable.setStatus("mandatory")
_MacipClientEntry_Object = MibTableRow
macipClientEntry = _MacipClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 19, 1)
)
macipClientEntry.setIndexNames(
    (0, "NETOPIA-MIB", "macipClientIpAddr"),
)
if mibBuilder.loadTexts:
    macipClientEntry.setStatus("mandatory")
_MacipClientIpAddr_Type = IpAddress
_MacipClientIpAddr_Object = MibTableColumn
macipClientIpAddr = _MacipClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 19, 1, 1),
    _MacipClientIpAddr_Type()
)
macipClientIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipClientIpAddr.setStatus("mandatory")


class _MacipClientIpAddrType_Type(Integer32):
    """Custom type macipClientIpAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MacipClientIpAddrType_Type.__name__ = "Integer32"
_MacipClientIpAddrType_Object = MibTableColumn
macipClientIpAddrType = _MacipClientIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 19, 1, 2),
    _MacipClientIpAddrType_Type()
)
macipClientIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipClientIpAddrType.setStatus("mandatory")
_MacipClientAtAddr_Type = DdpAddress
_MacipClientAtAddr_Object = MibTableColumn
macipClientAtAddr = _MacipClientAtAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 19, 1, 3),
    _MacipClientAtAddr_Type()
)
macipClientAtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipClientAtAddr.setStatus("mandatory")
_MacipClientIdleTime_Type = Integer32
_MacipClientIdleTime_Object = MibTableColumn
macipClientIdleTime = _MacipClientIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 7, 19, 1, 4),
    _MacipClientIdleTime_Type()
)
macipClientIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macipClientIdleTime.setStatus("mandatory")
_DhcpParams_ObjectIdentity = ObjectIdentity
dhcpParams = _DhcpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8)
)
_DhcpConfig_ObjectIdentity = ObjectIdentity
dhcpConfig = _DhcpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1)
)


class _DhcpSupport_Type(Integer32):
    """Custom type dhcpSupport based on Integer32"""
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


_DhcpSupport_Type.__name__ = "Integer32"
_DhcpSupport_Object = MibScalar
dhcpSupport = _DhcpSupport_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 1),
    _DhcpSupport_Type()
)
dhcpSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSupport.setStatus("mandatory")
_DhcpFirstClientAddr_Type = IpAddress
_DhcpFirstClientAddr_Object = MibScalar
dhcpFirstClientAddr = _DhcpFirstClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 2),
    _DhcpFirstClientAddr_Type()
)
dhcpFirstClientAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpFirstClientAddr.setStatus("mandatory")
_DhcpNumClientAddrs_Type = Integer32
_DhcpNumClientAddrs_Object = MibScalar
dhcpNumClientAddrs = _DhcpNumClientAddrs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 3),
    _DhcpNumClientAddrs_Type()
)
dhcpNumClientAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpNumClientAddrs.setStatus("mandatory")
_DhcpMaxClientAddrs_Type = Integer32
_DhcpMaxClientAddrs_Object = MibScalar
dhcpMaxClientAddrs = _DhcpMaxClientAddrs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 4),
    _DhcpMaxClientAddrs_Type()
)
dhcpMaxClientAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpMaxClientAddrs.setStatus("mandatory")


class _DhcpServerName_Type(OctetString):
    """Custom type dhcpServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DhcpServerName_Type.__name__ = "OctetString"
_DhcpServerName_Object = MibScalar
dhcpServerName = _DhcpServerName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 5),
    _DhcpServerName_Type()
)
dhcpServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerName.setStatus("mandatory")
_DhcpOptions_ObjectIdentity = ObjectIdentity
dhcpOptions = _DhcpOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6)
)
_DhcpOptionTable_Object = MibTable
dhcpOptionTable = _DhcpOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dhcpOptionTable.setStatus("mandatory")
_DhcpOptionEntry_Object = MibTableRow
dhcpOptionEntry = _DhcpOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 1, 1)
)
dhcpOptionEntry.setIndexNames(
    (0, "NETOPIA-MIB", "dhcpOptionCode"),
)
if mibBuilder.loadTexts:
    dhcpOptionEntry.setStatus("mandatory")


class _DhcpOptionCode_Type(Integer32):
    """Custom type dhcpOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DhcpOptionCode_Type.__name__ = "Integer32"
_DhcpOptionCode_Object = MibTableColumn
dhcpOptionCode = _DhcpOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 1, 1, 1),
    _DhcpOptionCode_Type()
)
dhcpOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpOptionCode.setStatus("mandatory")
_DhcpOptionName_Type = DisplayString
_DhcpOptionName_Object = MibTableColumn
dhcpOptionName = _DhcpOptionName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 1, 1, 2),
    _DhcpOptionName_Type()
)
dhcpOptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpOptionName.setStatus("mandatory")
_DhcpOptionValueObject_Type = ObjectIdentifier
_DhcpOptionValueObject_Object = MibTableColumn
dhcpOptionValueObject = _DhcpOptionValueObject_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 1, 1, 3),
    _DhcpOptionValueObject_Type()
)
dhcpOptionValueObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpOptionValueObject.setStatus("mandatory")


class _DhcpOptionStatus_Type(Integer32):
    """Custom type dhcpOptionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beingServed", 1),
          ("notBeingServed", 2))
    )


_DhcpOptionStatus_Type.__name__ = "Integer32"
_DhcpOptionStatus_Object = MibTableColumn
dhcpOptionStatus = _DhcpOptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 1, 1, 4),
    _DhcpOptionStatus_Type()
)
dhcpOptionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOptionStatus.setStatus("mandatory")
_DhcpDefaultGateway_Type = IpAddress
_DhcpDefaultGateway_Object = MibScalar
dhcpDefaultGateway = _DhcpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 2),
    _DhcpDefaultGateway_Type()
)
dhcpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpDefaultGateway.setStatus("mandatory")
_DhcpDNSServerTable_Object = MibTable
dhcpDNSServerTable = _DhcpDNSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 3)
)
if mibBuilder.loadTexts:
    dhcpDNSServerTable.setStatus("mandatory")
_DhcpDNSServerEntry_Object = MibTableRow
dhcpDNSServerEntry = _DhcpDNSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 3, 1)
)
dhcpDNSServerEntry.setIndexNames(
    (0, "NETOPIA-MIB", "dhcpDNSServerIndex"),
)
if mibBuilder.loadTexts:
    dhcpDNSServerEntry.setStatus("mandatory")
_DhcpDNSServerIndex_Type = Integer32
_DhcpDNSServerIndex_Object = MibTableColumn
dhcpDNSServerIndex = _DhcpDNSServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 3, 1, 1),
    _DhcpDNSServerIndex_Type()
)
dhcpDNSServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDNSServerIndex.setStatus("mandatory")
_DhcpDNSServerAddress_Type = IpAddress
_DhcpDNSServerAddress_Object = MibTableColumn
dhcpDNSServerAddress = _DhcpDNSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 3, 1, 2),
    _DhcpDNSServerAddress_Type()
)
dhcpDNSServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpDNSServerAddress.setStatus("mandatory")


class _DhcpDNSServerStatus_Type(Integer32):
    """Custom type dhcpDNSServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_DhcpDNSServerStatus_Type.__name__ = "Integer32"
_DhcpDNSServerStatus_Object = MibTableColumn
dhcpDNSServerStatus = _DhcpDNSServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 3, 1, 3),
    _DhcpDNSServerStatus_Type()
)
dhcpDNSServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpDNSServerStatus.setStatus("mandatory")
_DhcpDomainName_Type = OctetString
_DhcpDomainName_Object = MibScalar
dhcpDomainName = _DhcpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 4),
    _DhcpDomainName_Type()
)
dhcpDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpDomainName.setStatus("mandatory")
_DhcpNetBiosNameServer_Type = IpAddress
_DhcpNetBiosNameServer_Object = MibScalar
dhcpNetBiosNameServer = _DhcpNetBiosNameServer_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 5),
    _DhcpNetBiosNameServer_Type()
)
dhcpNetBiosNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpNetBiosNameServer.setStatus("mandatory")


class _DhcpNetBiosTcpNodeType_Type(Integer32):
    """Custom type dhcpNetBiosTcpNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("nodeTypeB", 1),
          ("nodeTypeH", 8),
          ("nodeTypeM", 4),
          ("nodeTypeP", 2))
    )


_DhcpNetBiosTcpNodeType_Type.__name__ = "Integer32"
_DhcpNetBiosTcpNodeType_Object = MibScalar
dhcpNetBiosTcpNodeType = _DhcpNetBiosTcpNodeType_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 6),
    _DhcpNetBiosTcpNodeType_Type()
)
dhcpNetBiosTcpNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpNetBiosTcpNodeType.setStatus("mandatory")


class _DhcpNetBiosTcpScope_Type(OctetString):
    """Custom type dhcpNetBiosTcpScope based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpNetBiosTcpScope_Type.__name__ = "OctetString"
_DhcpNetBiosTcpScope_Object = MibScalar
dhcpNetBiosTcpScope = _DhcpNetBiosTcpScope_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 1, 6, 7),
    _DhcpNetBiosTcpScope_Type()
)
dhcpNetBiosTcpScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpNetBiosTcpScope.setStatus("mandatory")
_DhcpInfo_ObjectIdentity = ObjectIdentity
dhcpInfo = _DhcpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 2)
)
_DhcpUnassignedClientAddrs_Type = Gauge32
_DhcpUnassignedClientAddrs_Object = MibScalar
dhcpUnassignedClientAddrs = _DhcpUnassignedClientAddrs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 2, 1),
    _DhcpUnassignedClientAddrs_Type()
)
dhcpUnassignedClientAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpUnassignedClientAddrs.setStatus("mandatory")
_DhcpClientTable_Object = MibTable
dhcpClientTable = _DhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    dhcpClientTable.setStatus("mandatory")
_DhcpClientEntry_Object = MibTableRow
dhcpClientEntry = _DhcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 2, 2, 1)
)
dhcpClientEntry.setIndexNames(
    (0, "NETOPIA-MIB", "dhcpClientIpAddr"),
)
if mibBuilder.loadTexts:
    dhcpClientEntry.setStatus("mandatory")
_DhcpClientIpAddr_Type = IpAddress
_DhcpClientIpAddr_Object = MibTableColumn
dhcpClientIpAddr = _DhcpClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 2, 2, 1, 1),
    _DhcpClientIpAddr_Type()
)
dhcpClientIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientIpAddr.setStatus("mandatory")


class _DhcpClientIdentifier_Type(OctetString):
    """Custom type dhcpClientIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpClientIdentifier_Type.__name__ = "OctetString"
_DhcpClientIdentifier_Object = MibTableColumn
dhcpClientIdentifier = _DhcpClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 2, 2, 1, 2),
    _DhcpClientIdentifier_Type()
)
dhcpClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientIdentifier.setStatus("mandatory")


class _DhcpClientState_Type(Integer32):
    """Custom type dhcpClientState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leased", 2),
          ("offered", 1))
    )


_DhcpClientState_Type.__name__ = "Integer32"
_DhcpClientState_Object = MibTableColumn
dhcpClientState = _DhcpClientState_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 2, 2, 1, 3),
    _DhcpClientState_Type()
)
dhcpClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientState.setStatus("mandatory")
_DhcpClientTimeLeft_Type = Integer32
_DhcpClientTimeLeft_Object = MibTableColumn
dhcpClientTimeLeft = _DhcpClientTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 2, 2, 1, 4),
    _DhcpClientTimeLeft_Type()
)
dhcpClientTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientTimeLeft.setStatus("mandatory")
_DhcpMRBindingTable_Object = MibTable
dhcpMRBindingTable = _DhcpMRBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 2, 3)
)
if mibBuilder.loadTexts:
    dhcpMRBindingTable.setStatus("mandatory")
_DhcpMRBindingEntry_Object = MibTableRow
dhcpMRBindingEntry = _DhcpMRBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 2, 3, 1)
)
dhcpMRBindingEntry.setIndexNames(
    (0, "NETOPIA-MIB", "dhcpMRBindingIpAddr"),
)
if mibBuilder.loadTexts:
    dhcpMRBindingEntry.setStatus("mandatory")
_DhcpMRBindingIpAddr_Type = IpAddress
_DhcpMRBindingIpAddr_Object = MibTableColumn
dhcpMRBindingIpAddr = _DhcpMRBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 2, 3, 1, 1),
    _DhcpMRBindingIpAddr_Type()
)
dhcpMRBindingIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpMRBindingIpAddr.setStatus("mandatory")


class _DhcpMRBindingClientIdentifier_Type(OctetString):
    """Custom type dhcpMRBindingClientIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpMRBindingClientIdentifier_Type.__name__ = "OctetString"
_DhcpMRBindingClientIdentifier_Object = MibTableColumn
dhcpMRBindingClientIdentifier = _DhcpMRBindingClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 8, 2, 3, 1, 2),
    _DhcpMRBindingClientIdentifier_Type()
)
dhcpMRBindingClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpMRBindingClientIdentifier.setStatus("mandatory")
_AurpParams_ObjectIdentity = ObjectIdentity
aurpParams = _AurpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9)
)
_AurpConfig_ObjectIdentity = ObjectIdentity
aurpConfig = _AurpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1)
)
_AurpTunCfgTable_Object = MibTable
aurpTunCfgTable = _AurpTunCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    aurpTunCfgTable.setStatus("mandatory")
_AurpTunCfgEntry_Object = MibTableRow
aurpTunCfgEntry = _AurpTunCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 1, 1)
)
aurpTunCfgEntry.setIndexNames(
    (0, "NETOPIA-MIB", "aurpTunCfgPortIndex"),
)
if mibBuilder.loadTexts:
    aurpTunCfgEntry.setStatus("mandatory")
_AurpTunCfgPortIndex_Type = Integer32
_AurpTunCfgPortIndex_Object = MibTableColumn
aurpTunCfgPortIndex = _AurpTunCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 1, 1, 1),
    _AurpTunCfgPortIndex_Type()
)
aurpTunCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunCfgPortIndex.setStatus("mandatory")


class _AurpTunCfgSupport_Type(Integer32):
    """Custom type aurpTunCfgSupport based on Integer32"""
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


_AurpTunCfgSupport_Type.__name__ = "Integer32"
_AurpTunCfgSupport_Object = MibTableColumn
aurpTunCfgSupport = _AurpTunCfgSupport_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 1, 1, 2),
    _AurpTunCfgSupport_Type()
)
aurpTunCfgSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aurpTunCfgSupport.setStatus("mandatory")


class _AurpTunCfgAcceptAnyPartner_Type(Integer32):
    """Custom type aurpTunCfgAcceptAnyPartner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acceptAnyPartner", 1),
          ("dontAcceptAnyPartner", 2))
    )


_AurpTunCfgAcceptAnyPartner_Type.__name__ = "Integer32"
_AurpTunCfgAcceptAnyPartner_Object = MibTableColumn
aurpTunCfgAcceptAnyPartner = _AurpTunCfgAcceptAnyPartner_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 1, 1, 3),
    _AurpTunCfgAcceptAnyPartner_Type()
)
aurpTunCfgAcceptAnyPartner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aurpTunCfgAcceptAnyPartner.setStatus("mandatory")


class _AurpTunCfgNetworkRemapping_Type(Integer32):
    """Custom type aurpTunCfgNetworkRemapping based on Integer32"""
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


_AurpTunCfgNetworkRemapping_Type.__name__ = "Integer32"
_AurpTunCfgNetworkRemapping_Object = MibTableColumn
aurpTunCfgNetworkRemapping = _AurpTunCfgNetworkRemapping_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 1, 1, 4),
    _AurpTunCfgNetworkRemapping_Type()
)
aurpTunCfgNetworkRemapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aurpTunCfgNetworkRemapping.setStatus("mandatory")


class _AurpTunCfgClustering_Type(Integer32):
    """Custom type aurpTunCfgClustering based on Integer32"""
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


_AurpTunCfgClustering_Type.__name__ = "Integer32"
_AurpTunCfgClustering_Object = MibTableColumn
aurpTunCfgClustering = _AurpTunCfgClustering_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 1, 1, 5),
    _AurpTunCfgClustering_Type()
)
aurpTunCfgClustering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aurpTunCfgClustering.setStatus("mandatory")


class _AurpTunCfgHopCountReduction_Type(Integer32):
    """Custom type aurpTunCfgHopCountReduction based on Integer32"""
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


_AurpTunCfgHopCountReduction_Type.__name__ = "Integer32"
_AurpTunCfgHopCountReduction_Object = MibTableColumn
aurpTunCfgHopCountReduction = _AurpTunCfgHopCountReduction_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 1, 1, 6),
    _AurpTunCfgHopCountReduction_Type()
)
aurpTunCfgHopCountReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aurpTunCfgHopCountReduction.setStatus("mandatory")
_AurpRemapRangeCfgTable_Object = MibTable
aurpRemapRangeCfgTable = _AurpRemapRangeCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    aurpRemapRangeCfgTable.setStatus("mandatory")
_AurpRemapRangeCfgEntry_Object = MibTableRow
aurpRemapRangeCfgEntry = _AurpRemapRangeCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 2, 1)
)
aurpRemapRangeCfgEntry.setIndexNames(
    (0, "NETOPIA-MIB", "aurpRemapRangeCfgPortIndex"),
    (0, "NETOPIA-MIB", "aurpRemapRangeCfgIndex"),
)
if mibBuilder.loadTexts:
    aurpRemapRangeCfgEntry.setStatus("mandatory")
_AurpRemapRangeCfgPortIndex_Type = Integer32
_AurpRemapRangeCfgPortIndex_Object = MibTableColumn
aurpRemapRangeCfgPortIndex = _AurpRemapRangeCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 2, 1, 1),
    _AurpRemapRangeCfgPortIndex_Type()
)
aurpRemapRangeCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapRangeCfgPortIndex.setStatus("mandatory")
_AurpRemapRangeCfgIndex_Type = Integer32
_AurpRemapRangeCfgIndex_Object = MibTableColumn
aurpRemapRangeCfgIndex = _AurpRemapRangeCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 2, 1, 2),
    _AurpRemapRangeCfgIndex_Type()
)
aurpRemapRangeCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapRangeCfgIndex.setStatus("mandatory")
_AurpRemapRangeCfgNetStart_Type = ATNetworkNumber
_AurpRemapRangeCfgNetStart_Object = MibTableColumn
aurpRemapRangeCfgNetStart = _AurpRemapRangeCfgNetStart_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 2, 1, 3),
    _AurpRemapRangeCfgNetStart_Type()
)
aurpRemapRangeCfgNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapRangeCfgNetStart.setStatus("mandatory")
_AurpRemapRangeCfgNetEnd_Type = ATNetworkNumber
_AurpRemapRangeCfgNetEnd_Object = MibTableColumn
aurpRemapRangeCfgNetEnd = _AurpRemapRangeCfgNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 2, 1, 4),
    _AurpRemapRangeCfgNetEnd_Type()
)
aurpRemapRangeCfgNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aurpRemapRangeCfgNetEnd.setStatus("mandatory")
_AurpCfgPartnerTable_Object = MibTable
aurpCfgPartnerTable = _AurpCfgPartnerTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    aurpCfgPartnerTable.setStatus("mandatory")
_AurpCfgPartnerEntry_Object = MibTableRow
aurpCfgPartnerEntry = _AurpCfgPartnerEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 3, 1)
)
aurpCfgPartnerEntry.setIndexNames(
    (0, "NETOPIA-MIB", "aurpCfgPartnerPortIndex"),
    (0, "NETOPIA-MIB", "aurpCfgPartnerName"),
)
if mibBuilder.loadTexts:
    aurpCfgPartnerEntry.setStatus("mandatory")
_AurpCfgPartnerPortIndex_Type = Integer32
_AurpCfgPartnerPortIndex_Object = MibTableColumn
aurpCfgPartnerPortIndex = _AurpCfgPartnerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 3, 1, 1),
    _AurpCfgPartnerPortIndex_Type()
)
aurpCfgPartnerPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpCfgPartnerPortIndex.setStatus("mandatory")
_AurpCfgPartnerName_Type = HostNameOrIpAddr
_AurpCfgPartnerName_Object = MibTableColumn
aurpCfgPartnerName = _AurpCfgPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 3, 1, 2),
    _AurpCfgPartnerName_Type()
)
aurpCfgPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpCfgPartnerName.setStatus("mandatory")
_AurpCfgPartnerIpAddr_Type = IpAddress
_AurpCfgPartnerIpAddr_Object = MibTableColumn
aurpCfgPartnerIpAddr = _AurpCfgPartnerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 3, 1, 3),
    _AurpCfgPartnerIpAddr_Type()
)
aurpCfgPartnerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpCfgPartnerIpAddr.setStatus("mandatory")


class _AurpCfgPartnerInitiateConnection_Type(Integer32):
    """Custom type aurpCfgPartnerInitiateConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontInitiate", 2),
          ("initiate", 1))
    )


_AurpCfgPartnerInitiateConnection_Type.__name__ = "Integer32"
_AurpCfgPartnerInitiateConnection_Object = MibTableColumn
aurpCfgPartnerInitiateConnection = _AurpCfgPartnerInitiateConnection_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 3, 1, 4),
    _AurpCfgPartnerInitiateConnection_Type()
)
aurpCfgPartnerInitiateConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aurpCfgPartnerInitiateConnection.setStatus("mandatory")


class _AurpCfgPartnerStatus_Type(Integer32):
    """Custom type aurpCfgPartnerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AurpCfgPartnerStatus_Type.__name__ = "Integer32"
_AurpCfgPartnerStatus_Object = MibTableColumn
aurpCfgPartnerStatus = _AurpCfgPartnerStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 1, 3, 1, 5),
    _AurpCfgPartnerStatus_Type()
)
aurpCfgPartnerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aurpCfgPartnerStatus.setStatus("mandatory")
_AurpInfo_ObjectIdentity = ObjectIdentity
aurpInfo = _AurpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2)
)
_AurpTunnelTable_Object = MibTable
aurpTunnelTable = _AurpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    aurpTunnelTable.setStatus("mandatory")
_AurpTunnelEntry_Object = MibTableRow
aurpTunnelEntry = _AurpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1)
)
aurpTunnelEntry.setIndexNames(
    (0, "NETOPIA-MIB", "aurpTunnelPortIndex"),
)
if mibBuilder.loadTexts:
    aurpTunnelEntry.setStatus("mandatory")
_AurpTunnelPortIndex_Type = Integer32
_AurpTunnelPortIndex_Object = MibTableColumn
aurpTunnelPortIndex = _AurpTunnelPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 1),
    _AurpTunnelPortIndex_Type()
)
aurpTunnelPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelPortIndex.setStatus("mandatory")


class _AurpTunnelPortType_Type(Integer32):
    """Custom type aurpTunnelPortType based on Integer32"""
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
        *(("decnetIV", 8),
          ("frameRelay", 5),
          ("ip", 2),
          ("ipx", 9),
          ("osi", 7),
          ("other", 1),
          ("serialNonStandard", 4),
          ("serialPpp", 3),
          ("x25", 6))
    )


_AurpTunnelPortType_Type.__name__ = "Integer32"
_AurpTunnelPortType_Object = MibTableColumn
aurpTunnelPortType = _AurpTunnelPortType_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 2),
    _AurpTunnelPortType_Type()
)
aurpTunnelPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelPortType.setStatus("mandatory")


class _AurpTunnelStatus_Type(Integer32):
    """Custom type aurpTunnelStatus based on Integer32"""
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
        *(("hasActiveConnections", 2),
          ("inactive", 4),
          ("inactiveLoopDetected", 5),
          ("noActiveConnections", 3),
          ("other", 1))
    )


_AurpTunnelStatus_Type.__name__ = "Integer32"
_AurpTunnelStatus_Object = MibTableColumn
aurpTunnelStatus = _AurpTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 3),
    _AurpTunnelStatus_Type()
)
aurpTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelStatus.setStatus("mandatory")


class _AurpTunnelAcceptAnyPartner_Type(Integer32):
    """Custom type aurpTunnelAcceptAnyPartner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("dontAccept", 2))
    )


_AurpTunnelAcceptAnyPartner_Type.__name__ = "Integer32"
_AurpTunnelAcceptAnyPartner_Object = MibTableColumn
aurpTunnelAcceptAnyPartner = _AurpTunnelAcceptAnyPartner_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 4),
    _AurpTunnelAcceptAnyPartner_Type()
)
aurpTunnelAcceptAnyPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelAcceptAnyPartner.setStatus("mandatory")


class _AurpTunnelNetworkRemapping_Type(Integer32):
    """Custom type aurpTunnelNetworkRemapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AurpTunnelNetworkRemapping_Type.__name__ = "Integer32"
_AurpTunnelNetworkRemapping_Object = MibTableColumn
aurpTunnelNetworkRemapping = _AurpTunnelNetworkRemapping_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 5),
    _AurpTunnelNetworkRemapping_Type()
)
aurpTunnelNetworkRemapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelNetworkRemapping.setStatus("mandatory")


class _AurpTunnelClustering_Type(Integer32):
    """Custom type aurpTunnelClustering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AurpTunnelClustering_Type.__name__ = "Integer32"
_AurpTunnelClustering_Object = MibTableColumn
aurpTunnelClustering = _AurpTunnelClustering_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 6),
    _AurpTunnelClustering_Type()
)
aurpTunnelClustering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelClustering.setStatus("mandatory")


class _AurpTunnelHopCountReduction_Type(Integer32):
    """Custom type aurpTunnelHopCountReduction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AurpTunnelHopCountReduction_Type.__name__ = "Integer32"
_AurpTunnelHopCountReduction_Object = MibTableColumn
aurpTunnelHopCountReduction = _AurpTunnelHopCountReduction_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 7),
    _AurpTunnelHopCountReduction_Type()
)
aurpTunnelHopCountReduction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelHopCountReduction.setStatus("mandatory")
_AurpTunnelDomainIdentifier_Type = OctetString
_AurpTunnelDomainIdentifier_Object = MibTableColumn
aurpTunnelDomainIdentifier = _AurpTunnelDomainIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 8),
    _AurpTunnelDomainIdentifier_Type()
)
aurpTunnelDomainIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelDomainIdentifier.setStatus("mandatory")
_AurpTunnelOpenRequests_Type = Counter32
_AurpTunnelOpenRequests_Object = MibTableColumn
aurpTunnelOpenRequests = _AurpTunnelOpenRequests_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 9),
    _AurpTunnelOpenRequests_Type()
)
aurpTunnelOpenRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelOpenRequests.setStatus("mandatory")
_AurpTunnelRouterDowns_Type = Counter32
_AurpTunnelRouterDowns_Object = MibTableColumn
aurpTunnelRouterDowns = _AurpTunnelRouterDowns_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 10),
    _AurpTunnelRouterDowns_Type()
)
aurpTunnelRouterDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelRouterDowns.setStatus("mandatory")
_AurpTunnelRemapErrors_Type = Counter32
_AurpTunnelRemapErrors_Object = MibTableColumn
aurpTunnelRemapErrors = _AurpTunnelRemapErrors_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 11),
    _AurpTunnelRemapErrors_Type()
)
aurpTunnelRemapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelRemapErrors.setStatus("mandatory")
_AurpTunnelClusterErrors_Type = Counter32
_AurpTunnelClusterErrors_Object = MibTableColumn
aurpTunnelClusterErrors = _AurpTunnelClusterErrors_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 12),
    _AurpTunnelClusterErrors_Type()
)
aurpTunnelClusterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelClusterErrors.setStatus("mandatory")
_AurpTunnelBrokenConnections_Type = Counter32
_AurpTunnelBrokenConnections_Object = MibTableColumn
aurpTunnelBrokenConnections = _AurpTunnelBrokenConnections_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 13),
    _AurpTunnelBrokenConnections_Type()
)
aurpTunnelBrokenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelBrokenConnections.setStatus("mandatory")
_AurpTunnelInvalidVersionErrors_Type = Counter32
_AurpTunnelInvalidVersionErrors_Object = MibTableColumn
aurpTunnelInvalidVersionErrors = _AurpTunnelInvalidVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 14),
    _AurpTunnelInvalidVersionErrors_Type()
)
aurpTunnelInvalidVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelInvalidVersionErrors.setStatus("mandatory")
_AurpTunnelAuthenticationErrors_Type = Counter32
_AurpTunnelAuthenticationErrors_Object = MibTableColumn
aurpTunnelAuthenticationErrors = _AurpTunnelAuthenticationErrors_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 1, 1, 15),
    _AurpTunnelAuthenticationErrors_Type()
)
aurpTunnelAuthenticationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpTunnelAuthenticationErrors.setStatus("mandatory")
_AurpConnectionTable_Object = MibTable
aurpConnectionTable = _AurpConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    aurpConnectionTable.setStatus("mandatory")
_AurpConnectionEntry_Object = MibTableRow
aurpConnectionEntry = _AurpConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1)
)
aurpConnectionEntry.setIndexNames(
    (0, "NETOPIA-MIB", "aurpConnectionPortIndex"),
    (0, "NETOPIA-MIB", "aurpConnectionIndex"),
)
if mibBuilder.loadTexts:
    aurpConnectionEntry.setStatus("mandatory")
_AurpConnectionPortIndex_Type = Integer32
_AurpConnectionPortIndex_Object = MibTableColumn
aurpConnectionPortIndex = _AurpConnectionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 1),
    _AurpConnectionPortIndex_Type()
)
aurpConnectionPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionPortIndex.setStatus("mandatory")
_AurpConnectionIndex_Type = Integer32
_AurpConnectionIndex_Object = MibTableColumn
aurpConnectionIndex = _AurpConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 2),
    _AurpConnectionIndex_Type()
)
aurpConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionIndex.setStatus("mandatory")
_AurpConnectionAddress_Type = OctetString
_AurpConnectionAddress_Object = MibTableColumn
aurpConnectionAddress = _AurpConnectionAddress_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 3),
    _AurpConnectionAddress_Type()
)
aurpConnectionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionAddress.setStatus("mandatory")
_AurpConnectionSentRIs_Type = Counter32
_AurpConnectionSentRIs_Object = MibTableColumn
aurpConnectionSentRIs = _AurpConnectionSentRIs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 4),
    _AurpConnectionSentRIs_Type()
)
aurpConnectionSentRIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionSentRIs.setStatus("mandatory")
_AurpConnectionRecvRIs_Type = Counter32
_AurpConnectionRecvRIs_Object = MibTableColumn
aurpConnectionRecvRIs = _AurpConnectionRecvRIs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 5),
    _AurpConnectionRecvRIs_Type()
)
aurpConnectionRecvRIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionRecvRIs.setStatus("mandatory")
_AurpConnectionSentZIs_Type = Counter32
_AurpConnectionSentZIs_Object = MibTableColumn
aurpConnectionSentZIs = _AurpConnectionSentZIs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 6),
    _AurpConnectionSentZIs_Type()
)
aurpConnectionSentZIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionSentZIs.setStatus("mandatory")
_AurpConnectionRecvZIs_Type = Counter32
_AurpConnectionRecvZIs_Object = MibTableColumn
aurpConnectionRecvZIs = _AurpConnectionRecvZIs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 7),
    _AurpConnectionRecvZIs_Type()
)
aurpConnectionRecvZIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionRecvZIs.setStatus("mandatory")
_AurpConnectionSentGZNs_Type = Counter32
_AurpConnectionSentGZNs_Object = MibTableColumn
aurpConnectionSentGZNs = _AurpConnectionSentGZNs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 8),
    _AurpConnectionSentGZNs_Type()
)
aurpConnectionSentGZNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionSentGZNs.setStatus("mandatory")
_AurpConnectionRecvGZNs_Type = Counter32
_AurpConnectionRecvGZNs_Object = MibTableColumn
aurpConnectionRecvGZNs = _AurpConnectionRecvGZNs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 9),
    _AurpConnectionRecvGZNs_Type()
)
aurpConnectionRecvGZNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionRecvGZNs.setStatus("mandatory")
_AurpConnectionSentGDZLs_Type = Counter32
_AurpConnectionSentGDZLs_Object = MibTableColumn
aurpConnectionSentGDZLs = _AurpConnectionSentGDZLs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 10),
    _AurpConnectionSentGDZLs_Type()
)
aurpConnectionSentGDZLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionSentGDZLs.setStatus("mandatory")
_AurpConnectionRecvGDZLs_Type = Counter32
_AurpConnectionRecvGDZLs_Object = MibTableColumn
aurpConnectionRecvGDZLs = _AurpConnectionRecvGDZLs_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 11),
    _AurpConnectionRecvGDZLs_Type()
)
aurpConnectionRecvGDZLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionRecvGDZLs.setStatus("mandatory")
_AurpConnectionBadSequence_Type = Counter32
_AurpConnectionBadSequence_Object = MibTableColumn
aurpConnectionBadSequence = _AurpConnectionBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 12),
    _AurpConnectionBadSequence_Type()
)
aurpConnectionBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionBadSequence.setStatus("mandatory")
_AurpConnectionUpdateSendingRate_Type = Integer32
_AurpConnectionUpdateSendingRate_Object = MibTableColumn
aurpConnectionUpdateSendingRate = _AurpConnectionUpdateSendingRate_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 13),
    _AurpConnectionUpdateSendingRate_Type()
)
aurpConnectionUpdateSendingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionUpdateSendingRate.setStatus("mandatory")
_AurpConnectionLastHeardFromTimeout_Type = Integer32
_AurpConnectionLastHeardFromTimeout_Object = MibTableColumn
aurpConnectionLastHeardFromTimeout = _AurpConnectionLastHeardFromTimeout_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 2, 1, 14),
    _AurpConnectionLastHeardFromTimeout_Type()
)
aurpConnectionLastHeardFromTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpConnectionLastHeardFromTimeout.setStatus("mandatory")
_AurpRemapRangeTable_Object = MibTable
aurpRemapRangeTable = _AurpRemapRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 3)
)
if mibBuilder.loadTexts:
    aurpRemapRangeTable.setStatus("mandatory")
_AurpRemapRangeEntry_Object = MibTableRow
aurpRemapRangeEntry = _AurpRemapRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 3, 1)
)
aurpRemapRangeEntry.setIndexNames(
    (0, "NETOPIA-MIB", "aurpRemapRangePortIndex"),
    (0, "NETOPIA-MIB", "aurpRemapRangeNetStart"),
)
if mibBuilder.loadTexts:
    aurpRemapRangeEntry.setStatus("mandatory")
_AurpRemapRangePortIndex_Type = Integer32
_AurpRemapRangePortIndex_Object = MibTableColumn
aurpRemapRangePortIndex = _AurpRemapRangePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 3, 1, 1),
    _AurpRemapRangePortIndex_Type()
)
aurpRemapRangePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapRangePortIndex.setStatus("mandatory")
_AurpRemapRangeNetStart_Type = ATNetworkNumber
_AurpRemapRangeNetStart_Object = MibTableColumn
aurpRemapRangeNetStart = _AurpRemapRangeNetStart_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 3, 1, 2),
    _AurpRemapRangeNetStart_Type()
)
aurpRemapRangeNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapRangeNetStart.setStatus("mandatory")
_AurpRemapRangeNetEnd_Type = ATNetworkNumber
_AurpRemapRangeNetEnd_Object = MibTableColumn
aurpRemapRangeNetEnd = _AurpRemapRangeNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 3, 1, 3),
    _AurpRemapRangeNetEnd_Type()
)
aurpRemapRangeNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapRangeNetEnd.setStatus("mandatory")
_AurpRemapRangeRouterAddress_Type = OctetString
_AurpRemapRangeRouterAddress_Object = MibTableColumn
aurpRemapRangeRouterAddress = _AurpRemapRangeRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 3, 1, 4),
    _AurpRemapRangeRouterAddress_Type()
)
aurpRemapRangeRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapRangeRouterAddress.setStatus("mandatory")
_AurpRemapTable_Object = MibTable
aurpRemapTable = _AurpRemapTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 4)
)
if mibBuilder.loadTexts:
    aurpRemapTable.setStatus("mandatory")
_AurpRemapEntry_Object = MibTableRow
aurpRemapEntry = _AurpRemapEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 4, 1)
)
aurpRemapEntry.setIndexNames(
    (0, "NETOPIA-MIB", "aurpRemapPortIndex"),
    (0, "NETOPIA-MIB", "aurpRemapNetStart"),
)
if mibBuilder.loadTexts:
    aurpRemapEntry.setStatus("mandatory")
_AurpRemapPortIndex_Type = Integer32
_AurpRemapPortIndex_Object = MibTableColumn
aurpRemapPortIndex = _AurpRemapPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 4, 1, 1),
    _AurpRemapPortIndex_Type()
)
aurpRemapPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapPortIndex.setStatus("mandatory")
_AurpRemapNetStart_Type = ATNetworkNumber
_AurpRemapNetStart_Object = MibTableColumn
aurpRemapNetStart = _AurpRemapNetStart_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 4, 1, 2),
    _AurpRemapNetStart_Type()
)
aurpRemapNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapNetStart.setStatus("mandatory")
_AurpRemapNetEnd_Type = ATNetworkNumber
_AurpRemapNetEnd_Object = MibTableColumn
aurpRemapNetEnd = _AurpRemapNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 4, 1, 3),
    _AurpRemapNetEnd_Type()
)
aurpRemapNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapNetEnd.setStatus("mandatory")
_AurpRemapUIDI_Type = OctetString
_AurpRemapUIDI_Object = MibTableColumn
aurpRemapUIDI = _AurpRemapUIDI_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 4, 1, 4),
    _AurpRemapUIDI_Type()
)
aurpRemapUIDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapUIDI.setStatus("mandatory")
_AurpRemapUINetStart_Type = ATNetworkNumber
_AurpRemapUINetStart_Object = MibTableColumn
aurpRemapUINetStart = _AurpRemapUINetStart_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 4, 1, 5),
    _AurpRemapUINetStart_Type()
)
aurpRemapUINetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapUINetStart.setStatus("mandatory")
_AurpRemapUINetEnd_Type = ATNetworkNumber
_AurpRemapUINetEnd_Object = MibTableColumn
aurpRemapUINetEnd = _AurpRemapUINetEnd_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 4, 1, 6),
    _AurpRemapUINetEnd_Type()
)
aurpRemapUINetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpRemapUINetEnd.setStatus("mandatory")
_AurpClusterTable_Object = MibTable
aurpClusterTable = _AurpClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 5)
)
if mibBuilder.loadTexts:
    aurpClusterTable.setStatus("mandatory")
_AurpClusterEntry_Object = MibTableRow
aurpClusterEntry = _AurpClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 5, 1)
)
aurpClusterEntry.setIndexNames(
    (0, "NETOPIA-MIB", "aurpClusterPortIndex"),
    (0, "NETOPIA-MIB", "aurpClusterIndex"),
)
if mibBuilder.loadTexts:
    aurpClusterEntry.setStatus("mandatory")
_AurpClusterPortIndex_Type = Integer32
_AurpClusterPortIndex_Object = MibTableColumn
aurpClusterPortIndex = _AurpClusterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 5, 1, 1),
    _AurpClusterPortIndex_Type()
)
aurpClusterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpClusterPortIndex.setStatus("mandatory")
_AurpClusterIndex_Type = Integer32
_AurpClusterIndex_Object = MibTableColumn
aurpClusterIndex = _AurpClusterIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 5, 1, 2),
    _AurpClusterIndex_Type()
)
aurpClusterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpClusterIndex.setStatus("mandatory")
_AurpClusterNetStart_Type = ATNetworkNumber
_AurpClusterNetStart_Object = MibTableColumn
aurpClusterNetStart = _AurpClusterNetStart_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 5, 1, 3),
    _AurpClusterNetStart_Type()
)
aurpClusterNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpClusterNetStart.setStatus("mandatory")
_AurpClusterNetEnd_Type = ATNetworkNumber
_AurpClusterNetEnd_Object = MibTableColumn
aurpClusterNetEnd = _AurpClusterNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 5, 1, 4),
    _AurpClusterNetEnd_Type()
)
aurpClusterNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpClusterNetEnd.setStatus("mandatory")
_AurpClusterUIDI_Type = OctetString
_AurpClusterUIDI_Object = MibTableColumn
aurpClusterUIDI = _AurpClusterUIDI_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 5, 1, 5),
    _AurpClusterUIDI_Type()
)
aurpClusterUIDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpClusterUIDI.setStatus("mandatory")
_AurpClusterNumberOfNetworks_Type = Integer32
_AurpClusterNumberOfNetworks_Object = MibTableColumn
aurpClusterNumberOfNetworks = _AurpClusterNumberOfNetworks_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 5, 1, 6),
    _AurpClusterNumberOfNetworks_Type()
)
aurpClusterNumberOfNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpClusterNumberOfNetworks.setStatus("mandatory")
_AurpClusterHopCount_Type = Integer32
_AurpClusterHopCount_Object = MibTableColumn
aurpClusterHopCount = _AurpClusterHopCount_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 5, 1, 7),
    _AurpClusterHopCount_Type()
)
aurpClusterHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpClusterHopCount.setStatus("mandatory")
_AurpClusterMemberTable_Object = MibTable
aurpClusterMemberTable = _AurpClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 6)
)
if mibBuilder.loadTexts:
    aurpClusterMemberTable.setStatus("mandatory")
_AurpClusterMemberEntry_Object = MibTableRow
aurpClusterMemberEntry = _AurpClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 6, 1)
)
aurpClusterMemberEntry.setIndexNames(
    (0, "NETOPIA-MIB", "aurpClusterMemberPortIndex"),
    (0, "NETOPIA-MIB", "aurpClusterMemberIndex"),
    (0, "NETOPIA-MIB", "aurpClusterMemberUINetStart"),
)
if mibBuilder.loadTexts:
    aurpClusterMemberEntry.setStatus("mandatory")
_AurpClusterMemberPortIndex_Type = Integer32
_AurpClusterMemberPortIndex_Object = MibTableColumn
aurpClusterMemberPortIndex = _AurpClusterMemberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 6, 1, 1),
    _AurpClusterMemberPortIndex_Type()
)
aurpClusterMemberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpClusterMemberPortIndex.setStatus("mandatory")
_AurpClusterMemberIndex_Type = Integer32
_AurpClusterMemberIndex_Object = MibTableColumn
aurpClusterMemberIndex = _AurpClusterMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 6, 1, 2),
    _AurpClusterMemberIndex_Type()
)
aurpClusterMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpClusterMemberIndex.setStatus("mandatory")
_AurpClusterMemberUINetStart_Type = ATNetworkNumber
_AurpClusterMemberUINetStart_Object = MibTableColumn
aurpClusterMemberUINetStart = _AurpClusterMemberUINetStart_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 6, 1, 3),
    _AurpClusterMemberUINetStart_Type()
)
aurpClusterMemberUINetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpClusterMemberUINetStart.setStatus("mandatory")
_AurpClusterMemberUINetEnd_Type = ATNetworkNumber
_AurpClusterMemberUINetEnd_Object = MibTableColumn
aurpClusterMemberUINetEnd = _AurpClusterMemberUINetEnd_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 9, 2, 6, 1, 4),
    _AurpClusterMemberUINetEnd_Type()
)
aurpClusterMemberUINetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aurpClusterMemberUINetEnd.setStatus("mandatory")
_BootParams_ObjectIdentity = ObjectIdentity
bootParams = _BootParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 10)
)


class _DeviceRestart_Type(Integer32):
    """Custom type deviceRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontRestart", 1),
          ("restart", 2))
    )


_DeviceRestart_Type.__name__ = "Integer32"
_DeviceRestart_Object = MibScalar
deviceRestart = _DeviceRestart_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 10, 1),
    _DeviceRestart_Type()
)
deviceRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceRestart.setStatus("mandatory")


class _RestoreDefaultConfig_Type(Integer32):
    """Custom type restoreDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontRestore", 1),
          ("restore", 2))
    )


_RestoreDefaultConfig_Type.__name__ = "Integer32"
_RestoreDefaultConfig_Object = MibScalar
restoreDefaultConfig = _RestoreDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 10, 2),
    _RestoreDefaultConfig_Type()
)
restoreDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restoreDefaultConfig.setStatus("mandatory")
_TftpParams_ObjectIdentity = ObjectIdentity
tftpParams = _TftpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 10, 3)
)
_TftpMaxRetries_Type = Integer32
_TftpMaxRetries_Object = MibScalar
tftpMaxRetries = _TftpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 10, 3, 1),
    _TftpMaxRetries_Type()
)
tftpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpMaxRetries.setStatus("mandatory")
_TftpServerName_Type = HostNameOrIpAddr
_TftpServerName_Object = MibScalar
tftpServerName = _TftpServerName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 10, 3, 2),
    _TftpServerName_Type()
)
tftpServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerName.setStatus("mandatory")
_TftpFwFileName_Type = OctetString
_TftpFwFileName_Object = MibScalar
tftpFwFileName = _TftpFwFileName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 10, 3, 3),
    _TftpFwFileName_Type()
)
tftpFwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwFileName.setStatus("mandatory")
_TftpConfigFileName_Type = OctetString
_TftpConfigFileName_Object = MibScalar
tftpConfigFileName = _TftpConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 10, 3, 4),
    _TftpConfigFileName_Type()
)
tftpConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpConfigFileName.setStatus("mandatory")


class _TftpReadFw_Type(Integer32):
    """Custom type tftpReadFw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notReadingFw", 2),
          ("readFw", 3),
          ("readingFw", 1))
    )


_TftpReadFw_Type.__name__ = "Integer32"
_TftpReadFw_Object = MibScalar
tftpReadFw = _TftpReadFw_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 10, 3, 5),
    _TftpReadFw_Type()
)
tftpReadFw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpReadFw.setStatus("mandatory")


class _TftpReadConfig_Type(Integer32):
    """Custom type tftpReadConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notReadingConfig", 2),
          ("readConfig", 3),
          ("readingConfig", 1))
    )


_TftpReadConfig_Type.__name__ = "Integer32"
_TftpReadConfig_Object = MibScalar
tftpReadConfig = _TftpReadConfig_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 10, 3, 6),
    _TftpReadConfig_Type()
)
tftpReadConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpReadConfig.setStatus("mandatory")


class _TftpWriteConfig_Type(Integer32):
    """Custom type tftpWriteConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notWritingConfig", 2),
          ("writeConfig", 3),
          ("writingConfig", 1))
    )


_TftpWriteConfig_Type.__name__ = "Integer32"
_TftpWriteConfig_Object = MibScalar
tftpWriteConfig = _TftpWriteConfig_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 10, 3, 7),
    _TftpWriteConfig_Type()
)
tftpWriteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpWriteConfig.setStatus("mandatory")
_TftpCurrentTransferOctets_Type = UInteger
_TftpCurrentTransferOctets_Object = MibScalar
tftpCurrentTransferOctets = _TftpCurrentTransferOctets_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 10, 3, 8),
    _TftpCurrentTransferOctets_Type()
)
tftpCurrentTransferOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpCurrentTransferOctets.setStatus("mandatory")
_SnmpParams_ObjectIdentity = ObjectIdentity
snmpParams = _SnmpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11)
)
_SnmpIpTrapRcvrTable_Object = MibTable
snmpIpTrapRcvrTable = _SnmpIpTrapRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 1)
)
if mibBuilder.loadTexts:
    snmpIpTrapRcvrTable.setStatus("mandatory")
_SnmpIpTrapRcvrEntry_Object = MibTableRow
snmpIpTrapRcvrEntry = _SnmpIpTrapRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 1, 1)
)
snmpIpTrapRcvrEntry.setIndexNames(
    (0, "NETOPIA-MIB", "snmpIpTrapRcvrName"),
)
if mibBuilder.loadTexts:
    snmpIpTrapRcvrEntry.setStatus("mandatory")
_SnmpIpTrapRcvrName_Type = HostNameOrIpAddr
_SnmpIpTrapRcvrName_Object = MibTableColumn
snmpIpTrapRcvrName = _SnmpIpTrapRcvrName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 1, 1, 1),
    _SnmpIpTrapRcvrName_Type()
)
snmpIpTrapRcvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpIpTrapRcvrName.setStatus("mandatory")
_SnmpIpTrapRcvrCommunity_Type = OctetString
_SnmpIpTrapRcvrCommunity_Object = MibTableColumn
snmpIpTrapRcvrCommunity = _SnmpIpTrapRcvrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 1, 1, 2),
    _SnmpIpTrapRcvrCommunity_Type()
)
snmpIpTrapRcvrCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpIpTrapRcvrCommunity.setStatus("mandatory")
_SnmpIpTrapRcvrIpAddress_Type = IpAddress
_SnmpIpTrapRcvrIpAddress_Object = MibTableColumn
snmpIpTrapRcvrIpAddress = _SnmpIpTrapRcvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 1, 1, 3),
    _SnmpIpTrapRcvrIpAddress_Type()
)
snmpIpTrapRcvrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpIpTrapRcvrIpAddress.setStatus("mandatory")


class _SnmpIpTrapRcvrStatus_Type(Integer32):
    """Custom type snmpIpTrapRcvrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SnmpIpTrapRcvrStatus_Type.__name__ = "Integer32"
_SnmpIpTrapRcvrStatus_Object = MibTableColumn
snmpIpTrapRcvrStatus = _SnmpIpTrapRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 1, 1, 4),
    _SnmpIpTrapRcvrStatus_Type()
)
snmpIpTrapRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpIpTrapRcvrStatus.setStatus("mandatory")
_SnmpAtTrapRcvrTable_Object = MibTable
snmpAtTrapRcvrTable = _SnmpAtTrapRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 2)
)
if mibBuilder.loadTexts:
    snmpAtTrapRcvrTable.setStatus("mandatory")
_SnmpAtTrapRcvrEntry_Object = MibTableRow
snmpAtTrapRcvrEntry = _SnmpAtTrapRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 2, 1)
)
snmpAtTrapRcvrEntry.setIndexNames(
    (0, "NETOPIA-MIB", "snmpAtTrapRcvrNBPObject"),
    (0, "NETOPIA-MIB", "snmpAtTrapRcvrNBPZone"),
)
if mibBuilder.loadTexts:
    snmpAtTrapRcvrEntry.setStatus("mandatory")


class _SnmpAtTrapRcvrNBPObject_Type(OctetString):
    """Custom type snmpAtTrapRcvrNBPObject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpAtTrapRcvrNBPObject_Type.__name__ = "OctetString"
_SnmpAtTrapRcvrNBPObject_Object = MibTableColumn
snmpAtTrapRcvrNBPObject = _SnmpAtTrapRcvrNBPObject_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 2, 1, 1),
    _SnmpAtTrapRcvrNBPObject_Type()
)
snmpAtTrapRcvrNBPObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAtTrapRcvrNBPObject.setStatus("mandatory")


class _SnmpAtTrapRcvrNBPZone_Type(OctetString):
    """Custom type snmpAtTrapRcvrNBPZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpAtTrapRcvrNBPZone_Type.__name__ = "OctetString"
_SnmpAtTrapRcvrNBPZone_Object = MibTableColumn
snmpAtTrapRcvrNBPZone = _SnmpAtTrapRcvrNBPZone_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 2, 1, 2),
    _SnmpAtTrapRcvrNBPZone_Type()
)
snmpAtTrapRcvrNBPZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAtTrapRcvrNBPZone.setStatus("mandatory")
_SnmpAtTrapRcvrCommunity_Type = OctetString
_SnmpAtTrapRcvrCommunity_Object = MibTableColumn
snmpAtTrapRcvrCommunity = _SnmpAtTrapRcvrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 2, 1, 3),
    _SnmpAtTrapRcvrCommunity_Type()
)
snmpAtTrapRcvrCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAtTrapRcvrCommunity.setStatus("mandatory")
_SnmpAtTrapRcvrDdpAddress_Type = DdpAddress
_SnmpAtTrapRcvrDdpAddress_Object = MibTableColumn
snmpAtTrapRcvrDdpAddress = _SnmpAtTrapRcvrDdpAddress_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 2, 1, 4),
    _SnmpAtTrapRcvrDdpAddress_Type()
)
snmpAtTrapRcvrDdpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAtTrapRcvrDdpAddress.setStatus("mandatory")
_SnmpAtTrapRcvrLastConfirmTime_Type = DisplayString
_SnmpAtTrapRcvrLastConfirmTime_Object = MibTableColumn
snmpAtTrapRcvrLastConfirmTime = _SnmpAtTrapRcvrLastConfirmTime_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 2, 1, 5),
    _SnmpAtTrapRcvrLastConfirmTime_Type()
)
snmpAtTrapRcvrLastConfirmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAtTrapRcvrLastConfirmTime.setStatus("mandatory")


class _SnmpAtTrapRcvrStatus_Type(Integer32):
    """Custom type snmpAtTrapRcvrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SnmpAtTrapRcvrStatus_Type.__name__ = "Integer32"
_SnmpAtTrapRcvrStatus_Object = MibTableColumn
snmpAtTrapRcvrStatus = _SnmpAtTrapRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 2, 1, 6),
    _SnmpAtTrapRcvrStatus_Type()
)
snmpAtTrapRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAtTrapRcvrStatus.setStatus("mandatory")
_SnmpAtTrapRcvrCacheEntryLifetime_Type = Integer32
_SnmpAtTrapRcvrCacheEntryLifetime_Object = MibScalar
snmpAtTrapRcvrCacheEntryLifetime = _SnmpAtTrapRcvrCacheEntryLifetime_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 3),
    _SnmpAtTrapRcvrCacheEntryLifetime_Type()
)
snmpAtTrapRcvrCacheEntryLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAtTrapRcvrCacheEntryLifetime.setStatus("mandatory")
_SnmpUnAuthIpAddr_Type = IpAddress
_SnmpUnAuthIpAddr_Object = MibScalar
snmpUnAuthIpAddr = _SnmpUnAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 4),
    _SnmpUnAuthIpAddr_Type()
)
snmpUnAuthIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUnAuthIpAddr.setStatus("mandatory")
_SnmpUnAuthCommunity_Type = OctetString
_SnmpUnAuthCommunity_Object = MibScalar
snmpUnAuthCommunity = _SnmpUnAuthCommunity_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 11, 5),
    _SnmpUnAuthCommunity_Type()
)
snmpUnAuthCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUnAuthCommunity.setStatus("mandatory")
_IsdnParams_ObjectIdentity = ObjectIdentity
isdnParams = _IsdnParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12)
)


class _IsdnSwitchType_Type(Integer32):
    """Custom type isdnSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("att5essCustom", 2),
          ("nationalIsdn1", 3),
          ("ntDms100Custom", 1))
    )


_IsdnSwitchType_Type.__name__ = "Integer32"
_IsdnSwitchType_Object = MibScalar
isdnSwitchType = _IsdnSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 1),
    _IsdnSwitchType_Type()
)
isdnSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnSwitchType.setStatus("mandatory")
_IsdnDirNum1_Type = OctetString
_IsdnDirNum1_Object = MibScalar
isdnDirNum1 = _IsdnDirNum1_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 2),
    _IsdnDirNum1_Type()
)
isdnDirNum1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDirNum1.setStatus("mandatory")
_IsdnSpid1_Type = OctetString
_IsdnSpid1_Object = MibScalar
isdnSpid1 = _IsdnSpid1_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 3),
    _IsdnSpid1_Type()
)
isdnSpid1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnSpid1.setStatus("mandatory")
_IsdnDirNum2_Type = OctetString
_IsdnDirNum2_Object = MibScalar
isdnDirNum2 = _IsdnDirNum2_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 4),
    _IsdnDirNum2_Type()
)
isdnDirNum2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDirNum2.setStatus("mandatory")
_IsdnSpid2_Type = OctetString
_IsdnSpid2_Object = MibScalar
isdnSpid2 = _IsdnSpid2_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 5),
    _IsdnSpid2_Type()
)
isdnSpid2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnSpid2.setStatus("mandatory")
_ConnProfileTable_Object = MibTable
connProfileTable = _ConnProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6)
)
if mibBuilder.loadTexts:
    connProfileTable.setStatus("mandatory")
_ConnProfileEntry_Object = MibTableRow
connProfileEntry = _ConnProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1)
)
connProfileEntry.setIndexNames(
    (0, "NETOPIA-MIB", "connProfIndex"),
)
if mibBuilder.loadTexts:
    connProfileEntry.setStatus("mandatory")
_ConnProfIndex_Type = Integer32
_ConnProfIndex_Object = MibTableColumn
connProfIndex = _ConnProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 1),
    _ConnProfIndex_Type()
)
connProfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connProfIndex.setStatus("mandatory")


class _ConnProfName_Type(OctetString):
    """Custom type connProfName based on OctetString"""
    defaultHexValue = ""


_ConnProfName_Object = MibTableColumn
connProfName = _ConnProfName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 2),
    _ConnProfName_Type()
)
connProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfName.setStatus("mandatory")


class _ConnProfEnable_Type(Integer32):
    """Custom type connProfEnable based on Integer32"""
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


_ConnProfEnable_Type.__name__ = "Integer32"
_ConnProfEnable_Object = MibTableColumn
connProfEnable = _ConnProfEnable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 3),
    _ConnProfEnable_Type()
)
connProfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfEnable.setStatus("mandatory")


class _ConnProfPermittedUse_Type(Integer32):
    """Custom type connProfPermittedUse based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dialIn", 1),
          ("dialInOrOut", 3),
          ("dialOut", 2))
    )


_ConnProfPermittedUse_Type.__name__ = "Integer32"
_ConnProfPermittedUse_Object = MibTableColumn
connProfPermittedUse = _ConnProfPermittedUse_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 4),
    _ConnProfPermittedUse_Type()
)
connProfPermittedUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfPermittedUse.setStatus("mandatory")


class _ConnProfIsdnDialNum_Type(OctetString):
    """Custom type connProfIsdnDialNum based on OctetString"""
    defaultHexValue = ""


_ConnProfIsdnDialNum_Object = MibTableColumn
connProfIsdnDialNum = _ConnProfIsdnDialNum_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 5),
    _ConnProfIsdnDialNum_Type()
)
connProfIsdnDialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfIsdnDialNum.setStatus("mandatory")


class _ConnProfIsdnBandwidth_Type(Integer32):
    """Custom type connProfIsdnBandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicBandwidth", 3),
          ("oneBChannel", 1),
          ("twoBChannels", 2))
    )


_ConnProfIsdnBandwidth_Type.__name__ = "Integer32"
_ConnProfIsdnBandwidth_Object = MibTableColumn
connProfIsdnBandwidth = _ConnProfIsdnBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 6),
    _ConnProfIsdnBandwidth_Type()
)
connProfIsdnBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfIsdnBandwidth.setStatus("mandatory")


class _ConnProfDialOnDemand_Type(Integer32):
    """Custom type connProfDialOnDemand based on Integer32"""
    defaultValue = 1

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


_ConnProfDialOnDemand_Type.__name__ = "Integer32"
_ConnProfDialOnDemand_Object = MibTableColumn
connProfDialOnDemand = _ConnProfDialOnDemand_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 7),
    _ConnProfDialOnDemand_Type()
)
connProfDialOnDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfDialOnDemand.setStatus("mandatory")


class _ConnProfDialBack_Type(Integer32):
    """Custom type connProfDialBack based on Integer32"""
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


_ConnProfDialBack_Type.__name__ = "Integer32"
_ConnProfDialBack_Object = MibTableColumn
connProfDialBack = _ConnProfDialBack_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 8),
    _ConnProfDialBack_Type()
)
connProfDialBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfDialBack.setStatus("mandatory")


class _ConnProfIsdnOutDataRate_Type(Integer32):
    """Custom type connProfIsdnOutDataRate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("place56KCall", 2),
          ("place64KCall", 1))
    )


_ConnProfIsdnOutDataRate_Type.__name__ = "Integer32"
_ConnProfIsdnOutDataRate_Object = MibTableColumn
connProfIsdnOutDataRate = _ConnProfIsdnOutDataRate_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 9),
    _ConnProfIsdnOutDataRate_Type()
)
connProfIsdnOutDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfIsdnOutDataRate.setStatus("mandatory")


class _ConnProfRemIpAddr_Type(IpAddress):
    """Custom type connProfRemIpAddr based on IpAddress"""
    defaultHexValue = ""


_ConnProfRemIpAddr_Object = MibTableColumn
connProfRemIpAddr = _ConnProfRemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 10),
    _ConnProfRemIpAddr_Type()
)
connProfRemIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfRemIpAddr.setStatus("mandatory")


class _ConnProfRemSubnetMask_Type(IpAddress):
    """Custom type connProfRemSubnetMask based on IpAddress"""
    defaultHexValue = ""


_ConnProfRemSubnetMask_Object = MibTableColumn
connProfRemSubnetMask = _ConnProfRemSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 11),
    _ConnProfRemSubnetMask_Type()
)
connProfRemSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfRemSubnetMask.setStatus("mandatory")


class _ConnProfRxRip_Type(Integer32):
    """Custom type connProfRxRip based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontRxRip", 1),
          ("rxRip", 2))
    )


_ConnProfRxRip_Type.__name__ = "Integer32"
_ConnProfRxRip_Object = MibTableColumn
connProfRxRip = _ConnProfRxRip_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 12),
    _ConnProfRxRip_Type()
)
connProfRxRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfRxRip.setStatus("mandatory")


class _ConnProfTxRip_Type(Integer32):
    """Custom type connProfTxRip based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontTxRip", 1),
          ("txRip", 2))
    )


_ConnProfTxRip_Type.__name__ = "Integer32"
_ConnProfTxRip_Object = MibTableColumn
connProfTxRip = _ConnProfTxRip_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 13),
    _ConnProfTxRip_Type()
)
connProfTxRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfTxRip.setStatus("mandatory")


class _ConnProfFilterSetIndex_Type(Integer32):
    """Custom type connProfFilterSetIndex based on Integer32"""
    defaultValue = 0


_ConnProfFilterSetIndex_Object = MibTableColumn
connProfFilterSetIndex = _ConnProfFilterSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 14),
    _ConnProfFilterSetIndex_Type()
)
connProfFilterSetIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfFilterSetIndex.setStatus("mandatory")


class _ConnProfIdleSeconds_Type(Integer32):
    """Custom type connProfIdleSeconds based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConnProfIdleSeconds_Type.__name__ = "Integer32"
_ConnProfIdleSeconds_Object = MibTableColumn
connProfIdleSeconds = _ConnProfIdleSeconds_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 15),
    _ConnProfIdleSeconds_Type()
)
connProfIdleSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfIdleSeconds.setStatus("mandatory")


class _ConnProfPppMaxRecvUnit_Type(Integer32):
    """Custom type connProfPppMaxRecvUnit based on Integer32"""
    defaultValue = 1500


_ConnProfPppMaxRecvUnit_Object = MibTableColumn
connProfPppMaxRecvUnit = _ConnProfPppMaxRecvUnit_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 16),
    _ConnProfPppMaxRecvUnit_Type()
)
connProfPppMaxRecvUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfPppMaxRecvUnit.setStatus("mandatory")


class _ConnProfPppLinkCompression_Type(Integer32):
    """Custom type connProfPppLinkCompression based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negotiateStacCompression", 1),
          ("noCompression", 2))
    )


_ConnProfPppLinkCompression_Type.__name__ = "Integer32"
_ConnProfPppLinkCompression_Object = MibTableColumn
connProfPppLinkCompression = _ConnProfPppLinkCompression_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 17),
    _ConnProfPppLinkCompression_Type()
)
connProfPppLinkCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfPppLinkCompression.setStatus("mandatory")


class _ConnProfPppSendAuthProt_Type(Integer32):
    """Custom type connProfPppSendAuthProt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authCHAP", 3),
          ("authNone", 1),
          ("authPAP", 2))
    )


_ConnProfPppSendAuthProt_Type.__name__ = "Integer32"
_ConnProfPppSendAuthProt_Object = MibTableColumn
connProfPppSendAuthProt = _ConnProfPppSendAuthProt_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 18),
    _ConnProfPppSendAuthProt_Type()
)
connProfPppSendAuthProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfPppSendAuthProt.setStatus("mandatory")


class _ConnProfPppSendAuthName_Type(OctetString):
    """Custom type connProfPppSendAuthName based on OctetString"""
    defaultHexValue = ""


_ConnProfPppSendAuthName_Object = MibTableColumn
connProfPppSendAuthName = _ConnProfPppSendAuthName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 19),
    _ConnProfPppSendAuthName_Type()
)
connProfPppSendAuthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfPppSendAuthName.setStatus("mandatory")


class _ConnProfPppSendAuthSecret_Type(OctetString):
    """Custom type connProfPppSendAuthSecret based on OctetString"""
    defaultHexValue = ""


_ConnProfPppSendAuthSecret_Object = MibTableColumn
connProfPppSendAuthSecret = _ConnProfPppSendAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 20),
    _ConnProfPppSendAuthSecret_Type()
)
connProfPppSendAuthSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfPppSendAuthSecret.setStatus("mandatory")


class _ConnProfPppRecvAuthName_Type(OctetString):
    """Custom type connProfPppRecvAuthName based on OctetString"""
    defaultHexValue = ""


_ConnProfPppRecvAuthName_Object = MibTableColumn
connProfPppRecvAuthName = _ConnProfPppRecvAuthName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 21),
    _ConnProfPppRecvAuthName_Type()
)
connProfPppRecvAuthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfPppRecvAuthName.setStatus("mandatory")


class _ConnProfPppRecvAuthSecret_Type(OctetString):
    """Custom type connProfPppRecvAuthSecret based on OctetString"""
    defaultHexValue = ""


_ConnProfPppRecvAuthSecret_Object = MibTableColumn
connProfPppRecvAuthSecret = _ConnProfPppRecvAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 22),
    _ConnProfPppRecvAuthSecret_Type()
)
connProfPppRecvAuthSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfPppRecvAuthSecret.setStatus("mandatory")


class _ConnProfStatus_Type(Integer32):
    """Custom type connProfStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_ConnProfStatus_Type.__name__ = "Integer32"
_ConnProfStatus_Object = MibTableColumn
connProfStatus = _ConnProfStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 6, 1, 23),
    _ConnProfStatus_Type()
)
connProfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connProfStatus.setStatus("mandatory")


class _AnsProfConnProfRequired_Type(Integer32):
    """Custom type ansProfConnProfRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connProfNotRequired", 2),
          ("connProfRequired", 1))
    )


_AnsProfConnProfRequired_Type.__name__ = "Integer32"
_AnsProfConnProfRequired_Object = MibScalar
ansProfConnProfRequired = _AnsProfConnProfRequired_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 7),
    _AnsProfConnProfRequired_Type()
)
ansProfConnProfRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansProfConnProfRequired.setStatus("mandatory")


class _AnsProfIsdnBandwidth_Type(Integer32):
    """Custom type ansProfIsdnBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicBandwidth", 3),
          ("oneBChannel", 1),
          ("twoBChannels", 2))
    )


_AnsProfIsdnBandwidth_Type.__name__ = "Integer32"
_AnsProfIsdnBandwidth_Object = MibScalar
ansProfIsdnBandwidth = _AnsProfIsdnBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 8),
    _AnsProfIsdnBandwidth_Type()
)
ansProfIsdnBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansProfIsdnBandwidth.setStatus("mandatory")


class _AnsProfIsdnInForce56K_Type(Integer32):
    """Custom type ansProfIsdnInForce56K based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontForce56K", 1),
          ("force56K", 2))
    )


_AnsProfIsdnInForce56K_Type.__name__ = "Integer32"
_AnsProfIsdnInForce56K_Object = MibScalar
ansProfIsdnInForce56K = _AnsProfIsdnInForce56K_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 9),
    _AnsProfIsdnInForce56K_Type()
)
ansProfIsdnInForce56K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansProfIsdnInForce56K.setStatus("mandatory")


class _AnsProfRxRip_Type(Integer32):
    """Custom type ansProfRxRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontRxRip", 1),
          ("rxRip", 2))
    )


_AnsProfRxRip_Type.__name__ = "Integer32"
_AnsProfRxRip_Object = MibScalar
ansProfRxRip = _AnsProfRxRip_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 10),
    _AnsProfRxRip_Type()
)
ansProfRxRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansProfRxRip.setStatus("mandatory")


class _AnsProfTxRip_Type(Integer32):
    """Custom type ansProfTxRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontTxRip", 1),
          ("txRip", 2))
    )


_AnsProfTxRip_Type.__name__ = "Integer32"
_AnsProfTxRip_Object = MibScalar
ansProfTxRip = _AnsProfTxRip_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 11),
    _AnsProfTxRip_Type()
)
ansProfTxRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansProfTxRip.setStatus("mandatory")
_AnsProfFilterSetIndex_Type = Integer32
_AnsProfFilterSetIndex_Object = MibScalar
ansProfFilterSetIndex = _AnsProfFilterSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 12),
    _AnsProfFilterSetIndex_Type()
)
ansProfFilterSetIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansProfFilterSetIndex.setStatus("mandatory")


class _AnsProfIdleSeconds_Type(Integer32):
    """Custom type ansProfIdleSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AnsProfIdleSeconds_Type.__name__ = "Integer32"
_AnsProfIdleSeconds_Object = MibScalar
ansProfIdleSeconds = _AnsProfIdleSeconds_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 13),
    _AnsProfIdleSeconds_Type()
)
ansProfIdleSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansProfIdleSeconds.setStatus("mandatory")
_AnsProfPppMaxRecvUnit_Type = Integer32
_AnsProfPppMaxRecvUnit_Object = MibScalar
ansProfPppMaxRecvUnit = _AnsProfPppMaxRecvUnit_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 14),
    _AnsProfPppMaxRecvUnit_Type()
)
ansProfPppMaxRecvUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansProfPppMaxRecvUnit.setStatus("mandatory")


class _AnsProfPppLinkCompression_Type(Integer32):
    """Custom type ansProfPppLinkCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negotiateStacCompression", 1),
          ("noCompression", 2))
    )


_AnsProfPppLinkCompression_Type.__name__ = "Integer32"
_AnsProfPppLinkCompression_Object = MibScalar
ansProfPppLinkCompression = _AnsProfPppLinkCompression_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 15),
    _AnsProfPppLinkCompression_Type()
)
ansProfPppLinkCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansProfPppLinkCompression.setStatus("mandatory")


class _AnsProfPppRecvAuthProt_Type(Integer32):
    """Custom type ansProfPppRecvAuthProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authCHAP", 3),
          ("authNone", 1),
          ("authPAP", 2))
    )


_AnsProfPppRecvAuthProt_Type.__name__ = "Integer32"
_AnsProfPppRecvAuthProt_Object = MibScalar
ansProfPppRecvAuthProt = _AnsProfPppRecvAuthProt_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 16),
    _AnsProfPppRecvAuthProt_Type()
)
ansProfPppRecvAuthProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansProfPppRecvAuthProt.setStatus("mandatory")
_AnsProfChapChallengeName_Type = OctetString
_AnsProfChapChallengeName_Object = MibScalar
ansProfChapChallengeName = _AnsProfChapChallengeName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 17),
    _AnsProfChapChallengeName_Type()
)
ansProfChapChallengeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansProfChapChallengeName.setStatus("mandatory")
_SchedConnTable_Object = MibTable
schedConnTable = _SchedConnTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 18)
)
if mibBuilder.loadTexts:
    schedConnTable.setStatus("mandatory")
_SchedConnEntry_Object = MibTableRow
schedConnEntry = _SchedConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 18, 1)
)
schedConnEntry.setIndexNames(
    (0, "NETOPIA-MIB", "schedConnIndex"),
)
if mibBuilder.loadTexts:
    schedConnEntry.setStatus("mandatory")
_SchedConnIndex_Type = Integer32
_SchedConnIndex_Object = MibTableColumn
schedConnIndex = _SchedConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 18, 1, 1),
    _SchedConnIndex_Type()
)
schedConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedConnIndex.setStatus("mandatory")


class _SchedConnEnable_Type(Integer32):
    """Custom type schedConnEnable based on Integer32"""
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


_SchedConnEnable_Type.__name__ = "Integer32"
_SchedConnEnable_Object = MibTableColumn
schedConnEnable = _SchedConnEnable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 18, 1, 2),
    _SchedConnEnable_Type()
)
schedConnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedConnEnable.setStatus("mandatory")


class _SchedConnDayMask_Type(Integer32):
    """Custom type schedConnDayMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SchedConnDayMask_Type.__name__ = "Integer32"
_SchedConnDayMask_Object = MibTableColumn
schedConnDayMask = _SchedConnDayMask_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 18, 1, 3),
    _SchedConnDayMask_Type()
)
schedConnDayMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedConnDayMask.setStatus("mandatory")


class _SchedConnStartTime_Type(OctetString):
    """Custom type schedConnStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(12, 12),
    )


_SchedConnStartTime_Type.__name__ = "OctetString"
_SchedConnStartTime_Object = MibTableColumn
schedConnStartTime = _SchedConnStartTime_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 18, 1, 4),
    _SchedConnStartTime_Type()
)
schedConnStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedConnStartTime.setStatus("mandatory")
_SchedConnDuration_Type = Integer32
_SchedConnDuration_Object = MibTableColumn
schedConnDuration = _SchedConnDuration_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 18, 1, 5),
    _SchedConnDuration_Type()
)
schedConnDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedConnDuration.setStatus("mandatory")
_SchedConnRemPeer_Type = Integer32
_SchedConnRemPeer_Object = MibTableColumn
schedConnRemPeer = _SchedConnRemPeer_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 18, 1, 6),
    _SchedConnRemPeer_Type()
)
schedConnRemPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedConnRemPeer.setStatus("mandatory")


class _SchedConnStatus_Type(Integer32):
    """Custom type schedConnStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SchedConnStatus_Type.__name__ = "Integer32"
_SchedConnStatus_Object = MibTableColumn
schedConnStatus = _SchedConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 12, 18, 1, 7),
    _SchedConnStatus_Type()
)
schedConnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedConnStatus.setStatus("mandatory")
_ConsoleParams_ObjectIdentity = ObjectIdentity
consoleParams = _ConsoleParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 13)
)
_ConsolePortSpeed_Type = Integer32
_ConsolePortSpeed_Object = MibScalar
consolePortSpeed = _ConsolePortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 13, 1),
    _ConsolePortSpeed_Type()
)
consolePortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePortSpeed.setStatus("mandatory")


class _ConsolePortDataBits_Type(Integer32):
    """Custom type consolePortDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_ConsolePortDataBits_Type.__name__ = "Integer32"
_ConsolePortDataBits_Object = MibScalar
consolePortDataBits = _ConsolePortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 13, 2),
    _ConsolePortDataBits_Type()
)
consolePortDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePortDataBits.setStatus("mandatory")


class _ConsolePortStopBits_Type(Integer32):
    """Custom type consolePortStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("onePointFive", 3),
          ("two", 2))
    )


_ConsolePortStopBits_Type.__name__ = "Integer32"
_ConsolePortStopBits_Object = MibScalar
consolePortStopBits = _ConsolePortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 13, 3),
    _ConsolePortStopBits_Type()
)
consolePortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePortStopBits.setStatus("mandatory")


class _ConsolePortParity_Type(Integer32):
    """Custom type consolePortParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_ConsolePortParity_Type.__name__ = "Integer32"
_ConsolePortParity_Object = MibScalar
consolePortParity = _ConsolePortParity_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 13, 4),
    _ConsolePortParity_Type()
)
consolePortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePortParity.setStatus("mandatory")
_ConsolePortRxChars_Type = Counter32
_ConsolePortRxChars_Object = MibScalar
consolePortRxChars = _ConsolePortRxChars_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 13, 5),
    _ConsolePortRxChars_Type()
)
consolePortRxChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolePortRxChars.setStatus("mandatory")
_ConsolePortTxChars_Type = Counter32
_ConsolePortTxChars_Object = MibScalar
consolePortTxChars = _ConsolePortTxChars_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 13, 6),
    _ConsolePortTxChars_Type()
)
consolePortTxChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolePortTxChars.setStatus("mandatory")
_ConsolePortParityErrors_Type = Counter32
_ConsolePortParityErrors_Object = MibScalar
consolePortParityErrors = _ConsolePortParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 13, 7),
    _ConsolePortParityErrors_Type()
)
consolePortParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolePortParityErrors.setStatus("mandatory")
_ConsolePortFramingErrors_Type = Counter32
_ConsolePortFramingErrors_Object = MibScalar
consolePortFramingErrors = _ConsolePortFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 13, 8),
    _ConsolePortFramingErrors_Type()
)
consolePortFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolePortFramingErrors.setStatus("mandatory")
_ConsolePortOverrunErrors_Type = Counter32
_ConsolePortOverrunErrors_Object = MibScalar
consolePortOverrunErrors = _ConsolePortOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 13, 9),
    _ConsolePortOverrunErrors_Type()
)
consolePortOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolePortOverrunErrors.setStatus("mandatory")
_PcCardParams_ObjectIdentity = ObjectIdentity
pcCardParams = _PcCardParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14)
)
_PcCardSlotTable_Object = MibTable
pcCardSlotTable = _PcCardSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 1)
)
if mibBuilder.loadTexts:
    pcCardSlotTable.setStatus("mandatory")
_PcCardSlotEntry_Object = MibTableRow
pcCardSlotEntry = _PcCardSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 1, 1)
)
pcCardSlotEntry.setIndexNames(
    (0, "NETOPIA-MIB", "pcCardSlotIndex"),
)
if mibBuilder.loadTexts:
    pcCardSlotEntry.setStatus("mandatory")
_PcCardSlotIndex_Type = Integer32
_PcCardSlotIndex_Object = MibTableColumn
pcCardSlotIndex = _PcCardSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 1, 1, 1),
    _PcCardSlotIndex_Type()
)
pcCardSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardSlotIndex.setStatus("mandatory")


class _PcCardSlotCardPresent_Type(Integer32):
    """Custom type pcCardSlotCardPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1))
    )


_PcCardSlotCardPresent_Type.__name__ = "Integer32"
_PcCardSlotCardPresent_Object = MibTableColumn
pcCardSlotCardPresent = _PcCardSlotCardPresent_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 1, 1, 2),
    _PcCardSlotCardPresent_Type()
)
pcCardSlotCardPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardSlotCardPresent.setStatus("mandatory")
_PcCardCardTable_Object = MibTable
pcCardCardTable = _PcCardCardTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 2)
)
if mibBuilder.loadTexts:
    pcCardCardTable.setStatus("mandatory")
_PcCardCardEntry_Object = MibTableRow
pcCardCardEntry = _PcCardCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 2, 1)
)
pcCardCardEntry.setIndexNames(
    (0, "NETOPIA-MIB", "pcCardSlotIndex"),
)
if mibBuilder.loadTexts:
    pcCardCardEntry.setStatus("mandatory")


class _PcCardCardMfrName_Type(OctetString):
    """Custom type pcCardCardMfrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PcCardCardMfrName_Type.__name__ = "OctetString"
_PcCardCardMfrName_Object = MibTableColumn
pcCardCardMfrName = _PcCardCardMfrName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 2, 1, 1),
    _PcCardCardMfrName_Type()
)
pcCardCardMfrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardCardMfrName.setStatus("mandatory")


class _PcCardCardProdName_Type(OctetString):
    """Custom type pcCardCardProdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PcCardCardProdName_Type.__name__ = "OctetString"
_PcCardCardProdName_Object = MibTableColumn
pcCardCardProdName = _PcCardCardProdName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 2, 1, 2),
    _PcCardCardProdName_Type()
)
pcCardCardProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardCardProdName.setStatus("mandatory")


class _PcCardCardProdInfo1_Type(OctetString):
    """Custom type pcCardCardProdInfo1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PcCardCardProdInfo1_Type.__name__ = "OctetString"
_PcCardCardProdInfo1_Object = MibTableColumn
pcCardCardProdInfo1 = _PcCardCardProdInfo1_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 2, 1, 3),
    _PcCardCardProdInfo1_Type()
)
pcCardCardProdInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardCardProdInfo1.setStatus("mandatory")


class _PcCardCardProdInfo2_Type(OctetString):
    """Custom type pcCardCardProdInfo2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PcCardCardProdInfo2_Type.__name__ = "OctetString"
_PcCardCardProdInfo2_Object = MibTableColumn
pcCardCardProdInfo2 = _PcCardCardProdInfo2_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 2, 1, 4),
    _PcCardCardProdInfo2_Type()
)
pcCardCardProdInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardCardProdInfo2.setStatus("mandatory")


class _PcCardCardFunction_Type(Integer32):
    """Custom type pcCardCardFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PcCardCardFunction_Type.__name__ = "Integer32"
_PcCardCardFunction_Object = MibTableColumn
pcCardCardFunction = _PcCardCardFunction_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 2, 1, 5),
    _PcCardCardFunction_Type()
)
pcCardCardFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardCardFunction.setStatus("mandatory")
_PcCardModemTable_Object = MibTable
pcCardModemTable = _PcCardModemTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 3)
)
if mibBuilder.loadTexts:
    pcCardModemTable.setStatus("mandatory")
_PcCardModemEntry_Object = MibTableRow
pcCardModemEntry = _PcCardModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 3, 1)
)
pcCardModemEntry.setIndexNames(
    (0, "NETOPIA-MIB", "pcCardSlotIndex"),
)
if mibBuilder.loadTexts:
    pcCardModemEntry.setStatus("mandatory")


class _PcCardModemActive_Type(Integer32):
    """Custom type pcCardModemActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_PcCardModemActive_Type.__name__ = "Integer32"
_PcCardModemActive_Object = MibTableColumn
pcCardModemActive = _PcCardModemActive_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 3, 1, 1),
    _PcCardModemActive_Type()
)
pcCardModemActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardModemActive.setStatus("mandatory")
_PcCardModemSessions_Type = Counter32
_PcCardModemSessions_Object = MibTableColumn
pcCardModemSessions = _PcCardModemSessions_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 3, 1, 2),
    _PcCardModemSessions_Type()
)
pcCardModemSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardModemSessions.setStatus("mandatory")
_PcCardModemTotalRxChars_Type = Counter32
_PcCardModemTotalRxChars_Object = MibTableColumn
pcCardModemTotalRxChars = _PcCardModemTotalRxChars_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 3, 1, 3),
    _PcCardModemTotalRxChars_Type()
)
pcCardModemTotalRxChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardModemTotalRxChars.setStatus("mandatory")
_PcCardModemTotalTxChars_Type = Counter32
_PcCardModemTotalTxChars_Object = MibTableColumn
pcCardModemTotalTxChars = _PcCardModemTotalTxChars_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 3, 1, 4),
    _PcCardModemTotalTxChars_Type()
)
pcCardModemTotalTxChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardModemTotalTxChars.setStatus("mandatory")
_PcCardModemConnTable_Object = MibTable
pcCardModemConnTable = _PcCardModemConnTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 4)
)
if mibBuilder.loadTexts:
    pcCardModemConnTable.setStatus("mandatory")
_PcCardModemConnEntry_Object = MibTableRow
pcCardModemConnEntry = _PcCardModemConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 4, 1)
)
pcCardModemConnEntry.setIndexNames(
    (0, "NETOPIA-MIB", "pcCardSlotIndex"),
)
if mibBuilder.loadTexts:
    pcCardModemConnEntry.setStatus("mandatory")
_PcCardModemConnSpeed_Type = Integer32
_PcCardModemConnSpeed_Object = MibTableColumn
pcCardModemConnSpeed = _PcCardModemConnSpeed_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 4, 1, 1),
    _PcCardModemConnSpeed_Type()
)
pcCardModemConnSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardModemConnSpeed.setStatus("mandatory")


class _PcCardModemConnDataBits_Type(Integer32):
    """Custom type pcCardModemConnDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_PcCardModemConnDataBits_Type.__name__ = "Integer32"
_PcCardModemConnDataBits_Object = MibTableColumn
pcCardModemConnDataBits = _PcCardModemConnDataBits_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 4, 1, 2),
    _PcCardModemConnDataBits_Type()
)
pcCardModemConnDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardModemConnDataBits.setStatus("mandatory")


class _PcCardModemConnStopBits_Type(Integer32):
    """Custom type pcCardModemConnStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("onePointFive", 3),
          ("two", 2))
    )


_PcCardModemConnStopBits_Type.__name__ = "Integer32"
_PcCardModemConnStopBits_Object = MibTableColumn
pcCardModemConnStopBits = _PcCardModemConnStopBits_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 4, 1, 3),
    _PcCardModemConnStopBits_Type()
)
pcCardModemConnStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardModemConnStopBits.setStatus("mandatory")


class _PcCardModemConnParity_Type(Integer32):
    """Custom type pcCardModemConnParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_PcCardModemConnParity_Type.__name__ = "Integer32"
_PcCardModemConnParity_Object = MibTableColumn
pcCardModemConnParity = _PcCardModemConnParity_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 4, 1, 4),
    _PcCardModemConnParity_Type()
)
pcCardModemConnParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardModemConnParity.setStatus("mandatory")
_PcCardModemConnRxChars_Type = Counter32
_PcCardModemConnRxChars_Object = MibTableColumn
pcCardModemConnRxChars = _PcCardModemConnRxChars_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 4, 1, 5),
    _PcCardModemConnRxChars_Type()
)
pcCardModemConnRxChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardModemConnRxChars.setStatus("mandatory")
_PcCardModemConnTxChars_Type = Counter32
_PcCardModemConnTxChars_Object = MibTableColumn
pcCardModemConnTxChars = _PcCardModemConnTxChars_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 14, 4, 1, 6),
    _PcCardModemConnTxChars_Type()
)
pcCardModemConnTxChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCardModemConnTxChars.setStatus("mandatory")
_LogParams_ObjectIdentity = ObjectIdentity
logParams = _LogParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15)
)


class _EventLogEnable_Type(Integer32):
    """Custom type eventLogEnable based on Integer32"""
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


_EventLogEnable_Type.__name__ = "Integer32"
_EventLogEnable_Object = MibScalar
eventLogEnable = _EventLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 1),
    _EventLogEnable_Type()
)
eventLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLogEnable.setStatus("mandatory")
_EventLogSize_Type = Integer32
_EventLogSize_Object = MibScalar
eventLogSize = _EventLogSize_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 2),
    _EventLogSize_Type()
)
eventLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogSize.setStatus("mandatory")
_EventLogCount_Type = Counter32
_EventLogCount_Object = MibScalar
eventLogCount = _EventLogCount_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 3),
    _EventLogCount_Type()
)
eventLogCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLogCount.setStatus("mandatory")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 4)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("mandatory")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 4, 1)
)
eventLogEntry.setIndexNames(
    (0, "NETOPIA-MIB", "eventLogIndex"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("mandatory")
_EventLogIndex_Type = Integer32
_EventLogIndex_Object = MibTableColumn
eventLogIndex = _EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 4, 1, 1),
    _EventLogIndex_Type()
)
eventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogIndex.setStatus("mandatory")
_EventLogTime_Type = DisplayString
_EventLogTime_Object = MibTableColumn
eventLogTime = _EventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 4, 1, 2),
    _EventLogTime_Type()
)
eventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogTime.setStatus("mandatory")
_EventLogDescr_Type = DisplayString
_EventLogDescr_Object = MibTableColumn
eventLogDescr = _EventLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 4, 1, 3),
    _EventLogDescr_Type()
)
eventLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDescr.setStatus("mandatory")
_EventLogDetail_Type = DisplayString
_EventLogDetail_Object = MibTableColumn
eventLogDetail = _EventLogDetail_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 4, 1, 4),
    _EventLogDetail_Type()
)
eventLogDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDetail.setStatus("mandatory")
_EventLogRawEntry_Type = OctetString
_EventLogRawEntry_Object = MibTableColumn
eventLogRawEntry = _EventLogRawEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 4, 1, 5),
    _EventLogRawEntry_Type()
)
eventLogRawEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogRawEntry.setStatus("mandatory")


class _IsdnLogEnable_Type(Integer32):
    """Custom type isdnLogEnable based on Integer32"""
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


_IsdnLogEnable_Type.__name__ = "Integer32"
_IsdnLogEnable_Object = MibScalar
isdnLogEnable = _IsdnLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 5),
    _IsdnLogEnable_Type()
)
isdnLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnLogEnable.setStatus("mandatory")
_IsdnLogSize_Type = Integer32
_IsdnLogSize_Object = MibScalar
isdnLogSize = _IsdnLogSize_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 6),
    _IsdnLogSize_Type()
)
isdnLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLogSize.setStatus("mandatory")
_IsdnLogCount_Type = Counter32
_IsdnLogCount_Object = MibScalar
isdnLogCount = _IsdnLogCount_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 7),
    _IsdnLogCount_Type()
)
isdnLogCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnLogCount.setStatus("mandatory")
_IsdnLogTable_Object = MibTable
isdnLogTable = _IsdnLogTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 8)
)
if mibBuilder.loadTexts:
    isdnLogTable.setStatus("mandatory")
_IsdnLogEntry_Object = MibTableRow
isdnLogEntry = _IsdnLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 8, 1)
)
isdnLogEntry.setIndexNames(
    (0, "NETOPIA-MIB", "eventLogIndex"),
)
if mibBuilder.loadTexts:
    isdnLogEntry.setStatus("mandatory")
_IsdnLogIndex_Type = Integer32
_IsdnLogIndex_Object = MibTableColumn
isdnLogIndex = _IsdnLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 8, 1, 1),
    _IsdnLogIndex_Type()
)
isdnLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLogIndex.setStatus("mandatory")
_IsdnLogTime_Type = DisplayString
_IsdnLogTime_Object = MibTableColumn
isdnLogTime = _IsdnLogTime_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 8, 1, 2),
    _IsdnLogTime_Type()
)
isdnLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLogTime.setStatus("mandatory")
_IsdnLogDescr_Type = DisplayString
_IsdnLogDescr_Object = MibTableColumn
isdnLogDescr = _IsdnLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 8, 1, 3),
    _IsdnLogDescr_Type()
)
isdnLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLogDescr.setStatus("mandatory")
_IsdnLogDetail_Type = DisplayString
_IsdnLogDetail_Object = MibTableColumn
isdnLogDetail = _IsdnLogDetail_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 8, 1, 4),
    _IsdnLogDetail_Type()
)
isdnLogDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLogDetail.setStatus("mandatory")
_IsdnLogRawEntry_Type = OctetString
_IsdnLogRawEntry_Object = MibTableColumn
isdnLogRawEntry = _IsdnLogRawEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 15, 8, 1, 5),
    _IsdnLogRawEntry_Type()
)
isdnLogRawEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLogRawEntry.setStatus("mandatory")
_FilterParams_ObjectIdentity = ObjectIdentity
filterParams = _FilterParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16)
)
_FilterSetTable_Object = MibTable
filterSetTable = _FilterSetTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 1)
)
if mibBuilder.loadTexts:
    filterSetTable.setStatus("mandatory")
_FilterSetEntry_Object = MibTableRow
filterSetEntry = _FilterSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 1, 1)
)
filterSetEntry.setIndexNames(
    (0, "NETOPIA-MIB", "filterSetIndex"),
)
if mibBuilder.loadTexts:
    filterSetEntry.setStatus("mandatory")
_FilterSetIndex_Type = Integer32
_FilterSetIndex_Object = MibTableColumn
filterSetIndex = _FilterSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 1, 1, 1),
    _FilterSetIndex_Type()
)
filterSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterSetIndex.setStatus("mandatory")


class _FilterSetEnable_Type(Integer32):
    """Custom type filterSetEnable based on Integer32"""
    defaultValue = 1

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


_FilterSetEnable_Type.__name__ = "Integer32"
_FilterSetEnable_Object = MibTableColumn
filterSetEnable = _FilterSetEnable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 1, 1, 2),
    _FilterSetEnable_Type()
)
filterSetEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterSetEnable.setStatus("mandatory")


class _FilterSetName_Type(OctetString):
    """Custom type filterSetName based on OctetString"""
    defaultHexValue = ""


_FilterSetName_Object = MibTableColumn
filterSetName = _FilterSetName_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 1, 1, 3),
    _FilterSetName_Type()
)
filterSetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSetName.setStatus("mandatory")


class _FilterSetStatus_Type(Integer32):
    """Custom type filterSetStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_FilterSetStatus_Type.__name__ = "Integer32"
_FilterSetStatus_Object = MibTableColumn
filterSetStatus = _FilterSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 1, 1, 4),
    _FilterSetStatus_Type()
)
filterSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterSetStatus.setStatus("mandatory")
_IpFilterTable_Object = MibTable
ipFilterTable = _IpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2)
)
if mibBuilder.loadTexts:
    ipFilterTable.setStatus("mandatory")
_IpFilterEntry_Object = MibTableRow
ipFilterEntry = _IpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1)
)
ipFilterEntry.setIndexNames(
    (0, "NETOPIA-MIB", "filterSetIndex"),
    (0, "NETOPIA-MIB", "ipFilterDirection"),
    (0, "NETOPIA-MIB", "ipFilterIndex"),
)
if mibBuilder.loadTexts:
    ipFilterEntry.setStatus("mandatory")


class _IpFilterDirection_Type(Integer32):
    """Custom type ipFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_IpFilterDirection_Type.__name__ = "Integer32"
_IpFilterDirection_Object = MibTableColumn
ipFilterDirection = _IpFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 1),
    _IpFilterDirection_Type()
)
ipFilterDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterDirection.setStatus("mandatory")
_IpFilterIndex_Type = Integer32
_IpFilterIndex_Object = MibTableColumn
ipFilterIndex = _IpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 2),
    _IpFilterIndex_Type()
)
ipFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterIndex.setStatus("mandatory")


class _IpFilterEnable_Type(Integer32):
    """Custom type ipFilterEnable based on Integer32"""
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


_IpFilterEnable_Type.__name__ = "Integer32"
_IpFilterEnable_Object = MibTableColumn
ipFilterEnable = _IpFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 3),
    _IpFilterEnable_Type()
)
ipFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterEnable.setStatus("mandatory")


class _IpFilterForward_Type(Integer32):
    """Custom type ipFilterForward based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("forward", 1))
    )


_IpFilterForward_Type.__name__ = "Integer32"
_IpFilterForward_Object = MibTableColumn
ipFilterForward = _IpFilterForward_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 4),
    _IpFilterForward_Type()
)
ipFilterForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterForward.setStatus("mandatory")


class _IpFilterSrcMask_Type(IpAddress):
    """Custom type ipFilterSrcMask based on IpAddress"""
    defaultHexValue = ""


_IpFilterSrcMask_Object = MibTableColumn
ipFilterSrcMask = _IpFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 5),
    _IpFilterSrcMask_Type()
)
ipFilterSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterSrcMask.setStatus("mandatory")


class _IpFilterSrcAddr_Type(IpAddress):
    """Custom type ipFilterSrcAddr based on IpAddress"""
    defaultHexValue = ""


_IpFilterSrcAddr_Object = MibTableColumn
ipFilterSrcAddr = _IpFilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 6),
    _IpFilterSrcAddr_Type()
)
ipFilterSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterSrcAddr.setStatus("mandatory")


class _IpFilterDstMask_Type(IpAddress):
    """Custom type ipFilterDstMask based on IpAddress"""
    defaultHexValue = ""


_IpFilterDstMask_Object = MibTableColumn
ipFilterDstMask = _IpFilterDstMask_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 7),
    _IpFilterDstMask_Type()
)
ipFilterDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterDstMask.setStatus("mandatory")


class _IpFilterDstAddr_Type(IpAddress):
    """Custom type ipFilterDstAddr based on IpAddress"""
    defaultHexValue = ""


_IpFilterDstAddr_Object = MibTableColumn
ipFilterDstAddr = _IpFilterDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 8),
    _IpFilterDstAddr_Type()
)
ipFilterDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterDstAddr.setStatus("mandatory")


class _IpFilterProtType_Type(Integer32):
    """Custom type ipFilterProtType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpFilterProtType_Type.__name__ = "Integer32"
_IpFilterProtType_Object = MibTableColumn
ipFilterProtType = _IpFilterProtType_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 9),
    _IpFilterProtType_Type()
)
ipFilterProtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterProtType.setStatus("mandatory")


class _IpFilterSrcPortComparison_Type(Integer32):
    """Custom type ipFilterSrcPortComparison based on Integer32"""
    defaultValue = 1

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
        *(("eq", 4),
          ("ge", 7),
          ("gt", 6),
          ("le", 3),
          ("lt", 2),
          ("ne", 5),
          ("none", 1))
    )


_IpFilterSrcPortComparison_Type.__name__ = "Integer32"
_IpFilterSrcPortComparison_Object = MibTableColumn
ipFilterSrcPortComparison = _IpFilterSrcPortComparison_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 10),
    _IpFilterSrcPortComparison_Type()
)
ipFilterSrcPortComparison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterSrcPortComparison.setStatus("mandatory")


class _IpFilterSrcPort_Type(Integer32):
    """Custom type ipFilterSrcPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpFilterSrcPort_Type.__name__ = "Integer32"
_IpFilterSrcPort_Object = MibTableColumn
ipFilterSrcPort = _IpFilterSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 11),
    _IpFilterSrcPort_Type()
)
ipFilterSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterSrcPort.setStatus("mandatory")


class _IpFilterDstPortComparison_Type(Integer32):
    """Custom type ipFilterDstPortComparison based on Integer32"""
    defaultValue = 1

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
        *(("eq", 4),
          ("ge", 7),
          ("gt", 6),
          ("le", 3),
          ("lt", 2),
          ("ne", 5),
          ("none", 1))
    )


_IpFilterDstPortComparison_Type.__name__ = "Integer32"
_IpFilterDstPortComparison_Object = MibTableColumn
ipFilterDstPortComparison = _IpFilterDstPortComparison_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 12),
    _IpFilterDstPortComparison_Type()
)
ipFilterDstPortComparison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterDstPortComparison.setStatus("mandatory")


class _IpFilterDstPort_Type(Integer32):
    """Custom type ipFilterDstPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpFilterDstPort_Type.__name__ = "Integer32"
_IpFilterDstPort_Object = MibTableColumn
ipFilterDstPort = _IpFilterDstPort_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 13),
    _IpFilterDstPort_Type()
)
ipFilterDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterDstPort.setStatus("mandatory")


class _IpFilterStatus_Type(Integer32):
    """Custom type ipFilterStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_IpFilterStatus_Type.__name__ = "Integer32"
_IpFilterStatus_Object = MibTableColumn
ipFilterStatus = _IpFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 2, 1, 14),
    _IpFilterStatus_Type()
)
ipFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterStatus.setStatus("mandatory")
_GenericFilterTable_Object = MibTable
genericFilterTable = _GenericFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 3)
)
if mibBuilder.loadTexts:
    genericFilterTable.setStatus("mandatory")
_GenericFilterEntry_Object = MibTableRow
genericFilterEntry = _GenericFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 3, 1)
)
genericFilterEntry.setIndexNames(
    (0, "NETOPIA-MIB", "filterSetIndex"),
    (0, "NETOPIA-MIB", "genericFilterDirection"),
    (0, "NETOPIA-MIB", "genericFilterIndex"),
)
if mibBuilder.loadTexts:
    genericFilterEntry.setStatus("mandatory")


class _GenericFilterDirection_Type(Integer32):
    """Custom type genericFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_GenericFilterDirection_Type.__name__ = "Integer32"
_GenericFilterDirection_Object = MibTableColumn
genericFilterDirection = _GenericFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 3, 1, 1),
    _GenericFilterDirection_Type()
)
genericFilterDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericFilterDirection.setStatus("mandatory")
_GenericFilterIndex_Type = Integer32
_GenericFilterIndex_Object = MibTableColumn
genericFilterIndex = _GenericFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 3, 1, 2),
    _GenericFilterIndex_Type()
)
genericFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericFilterIndex.setStatus("mandatory")


class _GenericFilterEnable_Type(Integer32):
    """Custom type genericFilterEnable based on Integer32"""
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


_GenericFilterEnable_Type.__name__ = "Integer32"
_GenericFilterEnable_Object = MibTableColumn
genericFilterEnable = _GenericFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 3, 1, 3),
    _GenericFilterEnable_Type()
)
genericFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericFilterEnable.setStatus("mandatory")


class _GenericFilterForward_Type(Integer32):
    """Custom type genericFilterForward based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("forward", 1))
    )


_GenericFilterForward_Type.__name__ = "Integer32"
_GenericFilterForward_Object = MibTableColumn
genericFilterForward = _GenericFilterForward_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 3, 1, 4),
    _GenericFilterForward_Type()
)
genericFilterForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericFilterForward.setStatus("mandatory")


class _GenericFilterOffset_Type(Integer32):
    """Custom type genericFilterOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GenericFilterOffset_Type.__name__ = "Integer32"
_GenericFilterOffset_Object = MibTableColumn
genericFilterOffset = _GenericFilterOffset_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 3, 1, 5),
    _GenericFilterOffset_Type()
)
genericFilterOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericFilterOffset.setStatus("mandatory")


class _GenericFilterMask_Type(OctetString):
    """Custom type genericFilterMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_GenericFilterMask_Type.__name__ = "OctetString"
_GenericFilterMask_Object = MibTableColumn
genericFilterMask = _GenericFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 3, 1, 6),
    _GenericFilterMask_Type()
)
genericFilterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericFilterMask.setStatus("mandatory")


class _GenericFilterValue_Type(OctetString):
    """Custom type genericFilterValue based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_GenericFilterValue_Type.__name__ = "OctetString"
_GenericFilterValue_Object = MibTableColumn
genericFilterValue = _GenericFilterValue_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 3, 1, 7),
    _GenericFilterValue_Type()
)
genericFilterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericFilterValue.setStatus("mandatory")


class _GenericFilterComparison_Type(Integer32):
    """Custom type genericFilterComparison based on Integer32"""
    defaultValue = 1

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
        *(("eq", 4),
          ("ge", 7),
          ("gt", 6),
          ("le", 3),
          ("lt", 2),
          ("ne", 5),
          ("none", 1))
    )


_GenericFilterComparison_Type.__name__ = "Integer32"
_GenericFilterComparison_Object = MibTableColumn
genericFilterComparison = _GenericFilterComparison_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 3, 1, 8),
    _GenericFilterComparison_Type()
)
genericFilterComparison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericFilterComparison.setStatus("mandatory")


class _GenericFilterChained_Type(Integer32):
    """Custom type genericFilterChained based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chained", 1),
          ("notChained", 2))
    )


_GenericFilterChained_Type.__name__ = "Integer32"
_GenericFilterChained_Object = MibTableColumn
genericFilterChained = _GenericFilterChained_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 3, 1, 9),
    _GenericFilterChained_Type()
)
genericFilterChained.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericFilterChained.setStatus("mandatory")


class _GenericFilterStatus_Type(Integer32):
    """Custom type genericFilterStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_GenericFilterStatus_Type.__name__ = "Integer32"
_GenericFilterStatus_Object = MibTableColumn
genericFilterStatus = _GenericFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 304, 1, 3, 1, 16, 3, 1, 10),
    _GenericFilterStatus_Type()
)
genericFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericFilterStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETOPIA-MIB",
    **{"ATNetworkNumber": ATNetworkNumber,
       "HostNameOrIpAddr": HostNameOrIpAddr,
       "UInteger": UInteger,
       "farallon": farallon,
       "netopia": netopia,
       "sysParams": sysParams,
       "hwVersion": hwVersion,
       "fwVersion": fwVersion,
       "productMIBVersion": productMIBVersion,
       "serialNumber": serialNumber,
       "modelNumber": modelNumber,
       "clockParams": clockParams,
       "bootTime": bootTime,
       "systemClock": systemClock,
       "sysStats": sysStats,
       "currentCpuUtil": currentCpuUtil,
       "averageCpuUtil": averageCpuUtil,
       "currentBufs": currentBufs,
       "averageBufs": averageBufs,
       "totalRAM": totalRAM,
       "usedRAM": usedRAM,
       "totalFEPROM": totalFEPROM,
       "usedFEPROM": usedFEPROM,
       "ipParams": ipParams,
       "ipAddr": ipAddr,
       "ipNetMask": ipNetMask,
       "ipBcastForm": ipBcastForm,
       "ipEncap": ipEncap,
       "ipDefaultGateway": ipDefaultGateway,
       "ipDomainName": ipDomainName,
       "ipDNSServerTable": ipDNSServerTable,
       "ipDNSServerEntry": ipDNSServerEntry,
       "ipDNSServerIndex": ipDNSServerIndex,
       "ipDNSServerAddress": ipDNSServerAddress,
       "ipDNSServerStatus": ipDNSServerStatus,
       "ripParams": ripParams,
       "ripEnTxEnable": ripEnTxEnable,
       "ripEnRxEnable": ripEnRxEnable,
       "atParams": atParams,
       "atportXTable": atportXTable,
       "atportXEntry": atportXEntry,
       "atportXIndex": atportXIndex,
       "atportXHide": atportXHide,
       "atportXSeed": atportXSeed,
       "atportZoneTable": atportZoneTable,
       "atportZoneEntry": atportZoneEntry,
       "atportZonePort": atportZonePort,
       "atportZoneName": atportZoneName,
       "atportZoneDefault": atportZoneDefault,
       "atportZoneStatus": atportZoneStatus,
       "atportTrafficTable": atportTrafficTable,
       "atportTrafficEntry": atportTrafficEntry,
       "atportTrafficIndex": atportTrafficIndex,
       "atportTrafficRxBytes": atportTrafficRxBytes,
       "atportTrafficRxPackets": atportTrafficRxPackets,
       "atportTrafficTxBytes": atportTrafficTxBytes,
       "atportTrafficTxPackets": atportTrafficTxPackets,
       "deviceNBPObject": deviceNBPObject,
       "macipParams": macipParams,
       "macipSupport": macipSupport,
       "macipIpSubIpAddr": macipIpSubIpAddr,
       "macipIpSubNetMask": macipIpSubNetMask,
       "macipFirstClientIpAddr": macipFirstClientIpAddr,
       "macipNumStaticAddrs": macipNumStaticAddrs,
       "macipNumDynamicAddrs": macipNumDynamicAddrs,
       "macipMaxAddrs": macipMaxAddrs,
       "macipUnusedDynamicAddrs": macipUnusedDynamicAddrs,
       "macipAssignRequests": macipAssignRequests,
       "macipServerRequests": macipServerRequests,
       "macipRefusedAssignRequests": macipRefusedAssignRequests,
       "macipBadRequests": macipBadRequests,
       "macipForwardedAtFrames": macipForwardedAtFrames,
       "macipForwardedAtOctets": macipForwardedAtOctets,
       "macipDroppedAtFrames": macipDroppedAtFrames,
       "macipForwardedIpFrames": macipForwardedIpFrames,
       "macipForwardedIpOctets": macipForwardedIpOctets,
       "macipDroppedIpFrames": macipDroppedIpFrames,
       "macipClientTable": macipClientTable,
       "macipClientEntry": macipClientEntry,
       "macipClientIpAddr": macipClientIpAddr,
       "macipClientIpAddrType": macipClientIpAddrType,
       "macipClientAtAddr": macipClientAtAddr,
       "macipClientIdleTime": macipClientIdleTime,
       "dhcpParams": dhcpParams,
       "dhcpConfig": dhcpConfig,
       "dhcpSupport": dhcpSupport,
       "dhcpFirstClientAddr": dhcpFirstClientAddr,
       "dhcpNumClientAddrs": dhcpNumClientAddrs,
       "dhcpMaxClientAddrs": dhcpMaxClientAddrs,
       "dhcpServerName": dhcpServerName,
       "dhcpOptions": dhcpOptions,
       "dhcpOptionTable": dhcpOptionTable,
       "dhcpOptionEntry": dhcpOptionEntry,
       "dhcpOptionCode": dhcpOptionCode,
       "dhcpOptionName": dhcpOptionName,
       "dhcpOptionValueObject": dhcpOptionValueObject,
       "dhcpOptionStatus": dhcpOptionStatus,
       "dhcpDefaultGateway": dhcpDefaultGateway,
       "dhcpDNSServerTable": dhcpDNSServerTable,
       "dhcpDNSServerEntry": dhcpDNSServerEntry,
       "dhcpDNSServerIndex": dhcpDNSServerIndex,
       "dhcpDNSServerAddress": dhcpDNSServerAddress,
       "dhcpDNSServerStatus": dhcpDNSServerStatus,
       "dhcpDomainName": dhcpDomainName,
       "dhcpNetBiosNameServer": dhcpNetBiosNameServer,
       "dhcpNetBiosTcpNodeType": dhcpNetBiosTcpNodeType,
       "dhcpNetBiosTcpScope": dhcpNetBiosTcpScope,
       "dhcpInfo": dhcpInfo,
       "dhcpUnassignedClientAddrs": dhcpUnassignedClientAddrs,
       "dhcpClientTable": dhcpClientTable,
       "dhcpClientEntry": dhcpClientEntry,
       "dhcpClientIpAddr": dhcpClientIpAddr,
       "dhcpClientIdentifier": dhcpClientIdentifier,
       "dhcpClientState": dhcpClientState,
       "dhcpClientTimeLeft": dhcpClientTimeLeft,
       "dhcpMRBindingTable": dhcpMRBindingTable,
       "dhcpMRBindingEntry": dhcpMRBindingEntry,
       "dhcpMRBindingIpAddr": dhcpMRBindingIpAddr,
       "dhcpMRBindingClientIdentifier": dhcpMRBindingClientIdentifier,
       "aurpParams": aurpParams,
       "aurpConfig": aurpConfig,
       "aurpTunCfgTable": aurpTunCfgTable,
       "aurpTunCfgEntry": aurpTunCfgEntry,
       "aurpTunCfgPortIndex": aurpTunCfgPortIndex,
       "aurpTunCfgSupport": aurpTunCfgSupport,
       "aurpTunCfgAcceptAnyPartner": aurpTunCfgAcceptAnyPartner,
       "aurpTunCfgNetworkRemapping": aurpTunCfgNetworkRemapping,
       "aurpTunCfgClustering": aurpTunCfgClustering,
       "aurpTunCfgHopCountReduction": aurpTunCfgHopCountReduction,
       "aurpRemapRangeCfgTable": aurpRemapRangeCfgTable,
       "aurpRemapRangeCfgEntry": aurpRemapRangeCfgEntry,
       "aurpRemapRangeCfgPortIndex": aurpRemapRangeCfgPortIndex,
       "aurpRemapRangeCfgIndex": aurpRemapRangeCfgIndex,
       "aurpRemapRangeCfgNetStart": aurpRemapRangeCfgNetStart,
       "aurpRemapRangeCfgNetEnd": aurpRemapRangeCfgNetEnd,
       "aurpCfgPartnerTable": aurpCfgPartnerTable,
       "aurpCfgPartnerEntry": aurpCfgPartnerEntry,
       "aurpCfgPartnerPortIndex": aurpCfgPartnerPortIndex,
       "aurpCfgPartnerName": aurpCfgPartnerName,
       "aurpCfgPartnerIpAddr": aurpCfgPartnerIpAddr,
       "aurpCfgPartnerInitiateConnection": aurpCfgPartnerInitiateConnection,
       "aurpCfgPartnerStatus": aurpCfgPartnerStatus,
       "aurpInfo": aurpInfo,
       "aurpTunnelTable": aurpTunnelTable,
       "aurpTunnelEntry": aurpTunnelEntry,
       "aurpTunnelPortIndex": aurpTunnelPortIndex,
       "aurpTunnelPortType": aurpTunnelPortType,
       "aurpTunnelStatus": aurpTunnelStatus,
       "aurpTunnelAcceptAnyPartner": aurpTunnelAcceptAnyPartner,
       "aurpTunnelNetworkRemapping": aurpTunnelNetworkRemapping,
       "aurpTunnelClustering": aurpTunnelClustering,
       "aurpTunnelHopCountReduction": aurpTunnelHopCountReduction,
       "aurpTunnelDomainIdentifier": aurpTunnelDomainIdentifier,
       "aurpTunnelOpenRequests": aurpTunnelOpenRequests,
       "aurpTunnelRouterDowns": aurpTunnelRouterDowns,
       "aurpTunnelRemapErrors": aurpTunnelRemapErrors,
       "aurpTunnelClusterErrors": aurpTunnelClusterErrors,
       "aurpTunnelBrokenConnections": aurpTunnelBrokenConnections,
       "aurpTunnelInvalidVersionErrors": aurpTunnelInvalidVersionErrors,
       "aurpTunnelAuthenticationErrors": aurpTunnelAuthenticationErrors,
       "aurpConnectionTable": aurpConnectionTable,
       "aurpConnectionEntry": aurpConnectionEntry,
       "aurpConnectionPortIndex": aurpConnectionPortIndex,
       "aurpConnectionIndex": aurpConnectionIndex,
       "aurpConnectionAddress": aurpConnectionAddress,
       "aurpConnectionSentRIs": aurpConnectionSentRIs,
       "aurpConnectionRecvRIs": aurpConnectionRecvRIs,
       "aurpConnectionSentZIs": aurpConnectionSentZIs,
       "aurpConnectionRecvZIs": aurpConnectionRecvZIs,
       "aurpConnectionSentGZNs": aurpConnectionSentGZNs,
       "aurpConnectionRecvGZNs": aurpConnectionRecvGZNs,
       "aurpConnectionSentGDZLs": aurpConnectionSentGDZLs,
       "aurpConnectionRecvGDZLs": aurpConnectionRecvGDZLs,
       "aurpConnectionBadSequence": aurpConnectionBadSequence,
       "aurpConnectionUpdateSendingRate": aurpConnectionUpdateSendingRate,
       "aurpConnectionLastHeardFromTimeout": aurpConnectionLastHeardFromTimeout,
       "aurpRemapRangeTable": aurpRemapRangeTable,
       "aurpRemapRangeEntry": aurpRemapRangeEntry,
       "aurpRemapRangePortIndex": aurpRemapRangePortIndex,
       "aurpRemapRangeNetStart": aurpRemapRangeNetStart,
       "aurpRemapRangeNetEnd": aurpRemapRangeNetEnd,
       "aurpRemapRangeRouterAddress": aurpRemapRangeRouterAddress,
       "aurpRemapTable": aurpRemapTable,
       "aurpRemapEntry": aurpRemapEntry,
       "aurpRemapPortIndex": aurpRemapPortIndex,
       "aurpRemapNetStart": aurpRemapNetStart,
       "aurpRemapNetEnd": aurpRemapNetEnd,
       "aurpRemapUIDI": aurpRemapUIDI,
       "aurpRemapUINetStart": aurpRemapUINetStart,
       "aurpRemapUINetEnd": aurpRemapUINetEnd,
       "aurpClusterTable": aurpClusterTable,
       "aurpClusterEntry": aurpClusterEntry,
       "aurpClusterPortIndex": aurpClusterPortIndex,
       "aurpClusterIndex": aurpClusterIndex,
       "aurpClusterNetStart": aurpClusterNetStart,
       "aurpClusterNetEnd": aurpClusterNetEnd,
       "aurpClusterUIDI": aurpClusterUIDI,
       "aurpClusterNumberOfNetworks": aurpClusterNumberOfNetworks,
       "aurpClusterHopCount": aurpClusterHopCount,
       "aurpClusterMemberTable": aurpClusterMemberTable,
       "aurpClusterMemberEntry": aurpClusterMemberEntry,
       "aurpClusterMemberPortIndex": aurpClusterMemberPortIndex,
       "aurpClusterMemberIndex": aurpClusterMemberIndex,
       "aurpClusterMemberUINetStart": aurpClusterMemberUINetStart,
       "aurpClusterMemberUINetEnd": aurpClusterMemberUINetEnd,
       "bootParams": bootParams,
       "deviceRestart": deviceRestart,
       "restoreDefaultConfig": restoreDefaultConfig,
       "tftpParams": tftpParams,
       "tftpMaxRetries": tftpMaxRetries,
       "tftpServerName": tftpServerName,
       "tftpFwFileName": tftpFwFileName,
       "tftpConfigFileName": tftpConfigFileName,
       "tftpReadFw": tftpReadFw,
       "tftpReadConfig": tftpReadConfig,
       "tftpWriteConfig": tftpWriteConfig,
       "tftpCurrentTransferOctets": tftpCurrentTransferOctets,
       "snmpParams": snmpParams,
       "snmpIpTrapRcvrTable": snmpIpTrapRcvrTable,
       "snmpIpTrapRcvrEntry": snmpIpTrapRcvrEntry,
       "snmpIpTrapRcvrName": snmpIpTrapRcvrName,
       "snmpIpTrapRcvrCommunity": snmpIpTrapRcvrCommunity,
       "snmpIpTrapRcvrIpAddress": snmpIpTrapRcvrIpAddress,
       "snmpIpTrapRcvrStatus": snmpIpTrapRcvrStatus,
       "snmpAtTrapRcvrTable": snmpAtTrapRcvrTable,
       "snmpAtTrapRcvrEntry": snmpAtTrapRcvrEntry,
       "snmpAtTrapRcvrNBPObject": snmpAtTrapRcvrNBPObject,
       "snmpAtTrapRcvrNBPZone": snmpAtTrapRcvrNBPZone,
       "snmpAtTrapRcvrCommunity": snmpAtTrapRcvrCommunity,
       "snmpAtTrapRcvrDdpAddress": snmpAtTrapRcvrDdpAddress,
       "snmpAtTrapRcvrLastConfirmTime": snmpAtTrapRcvrLastConfirmTime,
       "snmpAtTrapRcvrStatus": snmpAtTrapRcvrStatus,
       "snmpAtTrapRcvrCacheEntryLifetime": snmpAtTrapRcvrCacheEntryLifetime,
       "snmpUnAuthIpAddr": snmpUnAuthIpAddr,
       "snmpUnAuthCommunity": snmpUnAuthCommunity,
       "isdnParams": isdnParams,
       "isdnSwitchType": isdnSwitchType,
       "isdnDirNum1": isdnDirNum1,
       "isdnSpid1": isdnSpid1,
       "isdnDirNum2": isdnDirNum2,
       "isdnSpid2": isdnSpid2,
       "connProfileTable": connProfileTable,
       "connProfileEntry": connProfileEntry,
       "connProfIndex": connProfIndex,
       "connProfName": connProfName,
       "connProfEnable": connProfEnable,
       "connProfPermittedUse": connProfPermittedUse,
       "connProfIsdnDialNum": connProfIsdnDialNum,
       "connProfIsdnBandwidth": connProfIsdnBandwidth,
       "connProfDialOnDemand": connProfDialOnDemand,
       "connProfDialBack": connProfDialBack,
       "connProfIsdnOutDataRate": connProfIsdnOutDataRate,
       "connProfRemIpAddr": connProfRemIpAddr,
       "connProfRemSubnetMask": connProfRemSubnetMask,
       "connProfRxRip": connProfRxRip,
       "connProfTxRip": connProfTxRip,
       "connProfFilterSetIndex": connProfFilterSetIndex,
       "connProfIdleSeconds": connProfIdleSeconds,
       "connProfPppMaxRecvUnit": connProfPppMaxRecvUnit,
       "connProfPppLinkCompression": connProfPppLinkCompression,
       "connProfPppSendAuthProt": connProfPppSendAuthProt,
       "connProfPppSendAuthName": connProfPppSendAuthName,
       "connProfPppSendAuthSecret": connProfPppSendAuthSecret,
       "connProfPppRecvAuthName": connProfPppRecvAuthName,
       "connProfPppRecvAuthSecret": connProfPppRecvAuthSecret,
       "connProfStatus": connProfStatus,
       "ansProfConnProfRequired": ansProfConnProfRequired,
       "ansProfIsdnBandwidth": ansProfIsdnBandwidth,
       "ansProfIsdnInForce56K": ansProfIsdnInForce56K,
       "ansProfRxRip": ansProfRxRip,
       "ansProfTxRip": ansProfTxRip,
       "ansProfFilterSetIndex": ansProfFilterSetIndex,
       "ansProfIdleSeconds": ansProfIdleSeconds,
       "ansProfPppMaxRecvUnit": ansProfPppMaxRecvUnit,
       "ansProfPppLinkCompression": ansProfPppLinkCompression,
       "ansProfPppRecvAuthProt": ansProfPppRecvAuthProt,
       "ansProfChapChallengeName": ansProfChapChallengeName,
       "schedConnTable": schedConnTable,
       "schedConnEntry": schedConnEntry,
       "schedConnIndex": schedConnIndex,
       "schedConnEnable": schedConnEnable,
       "schedConnDayMask": schedConnDayMask,
       "schedConnStartTime": schedConnStartTime,
       "schedConnDuration": schedConnDuration,
       "schedConnRemPeer": schedConnRemPeer,
       "schedConnStatus": schedConnStatus,
       "consoleParams": consoleParams,
       "consolePortSpeed": consolePortSpeed,
       "consolePortDataBits": consolePortDataBits,
       "consolePortStopBits": consolePortStopBits,
       "consolePortParity": consolePortParity,
       "consolePortRxChars": consolePortRxChars,
       "consolePortTxChars": consolePortTxChars,
       "consolePortParityErrors": consolePortParityErrors,
       "consolePortFramingErrors": consolePortFramingErrors,
       "consolePortOverrunErrors": consolePortOverrunErrors,
       "pcCardParams": pcCardParams,
       "pcCardSlotTable": pcCardSlotTable,
       "pcCardSlotEntry": pcCardSlotEntry,
       "pcCardSlotIndex": pcCardSlotIndex,
       "pcCardSlotCardPresent": pcCardSlotCardPresent,
       "pcCardCardTable": pcCardCardTable,
       "pcCardCardEntry": pcCardCardEntry,
       "pcCardCardMfrName": pcCardCardMfrName,
       "pcCardCardProdName": pcCardCardProdName,
       "pcCardCardProdInfo1": pcCardCardProdInfo1,
       "pcCardCardProdInfo2": pcCardCardProdInfo2,
       "pcCardCardFunction": pcCardCardFunction,
       "pcCardModemTable": pcCardModemTable,
       "pcCardModemEntry": pcCardModemEntry,
       "pcCardModemActive": pcCardModemActive,
       "pcCardModemSessions": pcCardModemSessions,
       "pcCardModemTotalRxChars": pcCardModemTotalRxChars,
       "pcCardModemTotalTxChars": pcCardModemTotalTxChars,
       "pcCardModemConnTable": pcCardModemConnTable,
       "pcCardModemConnEntry": pcCardModemConnEntry,
       "pcCardModemConnSpeed": pcCardModemConnSpeed,
       "pcCardModemConnDataBits": pcCardModemConnDataBits,
       "pcCardModemConnStopBits": pcCardModemConnStopBits,
       "pcCardModemConnParity": pcCardModemConnParity,
       "pcCardModemConnRxChars": pcCardModemConnRxChars,
       "pcCardModemConnTxChars": pcCardModemConnTxChars,
       "logParams": logParams,
       "eventLogEnable": eventLogEnable,
       "eventLogSize": eventLogSize,
       "eventLogCount": eventLogCount,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventLogIndex": eventLogIndex,
       "eventLogTime": eventLogTime,
       "eventLogDescr": eventLogDescr,
       "eventLogDetail": eventLogDetail,
       "eventLogRawEntry": eventLogRawEntry,
       "isdnLogEnable": isdnLogEnable,
       "isdnLogSize": isdnLogSize,
       "isdnLogCount": isdnLogCount,
       "isdnLogTable": isdnLogTable,
       "isdnLogEntry": isdnLogEntry,
       "isdnLogIndex": isdnLogIndex,
       "isdnLogTime": isdnLogTime,
       "isdnLogDescr": isdnLogDescr,
       "isdnLogDetail": isdnLogDetail,
       "isdnLogRawEntry": isdnLogRawEntry,
       "filterParams": filterParams,
       "filterSetTable": filterSetTable,
       "filterSetEntry": filterSetEntry,
       "filterSetIndex": filterSetIndex,
       "filterSetEnable": filterSetEnable,
       "filterSetName": filterSetName,
       "filterSetStatus": filterSetStatus,
       "ipFilterTable": ipFilterTable,
       "ipFilterEntry": ipFilterEntry,
       "ipFilterDirection": ipFilterDirection,
       "ipFilterIndex": ipFilterIndex,
       "ipFilterEnable": ipFilterEnable,
       "ipFilterForward": ipFilterForward,
       "ipFilterSrcMask": ipFilterSrcMask,
       "ipFilterSrcAddr": ipFilterSrcAddr,
       "ipFilterDstMask": ipFilterDstMask,
       "ipFilterDstAddr": ipFilterDstAddr,
       "ipFilterProtType": ipFilterProtType,
       "ipFilterSrcPortComparison": ipFilterSrcPortComparison,
       "ipFilterSrcPort": ipFilterSrcPort,
       "ipFilterDstPortComparison": ipFilterDstPortComparison,
       "ipFilterDstPort": ipFilterDstPort,
       "ipFilterStatus": ipFilterStatus,
       "genericFilterTable": genericFilterTable,
       "genericFilterEntry": genericFilterEntry,
       "genericFilterDirection": genericFilterDirection,
       "genericFilterIndex": genericFilterIndex,
       "genericFilterEnable": genericFilterEnable,
       "genericFilterForward": genericFilterForward,
       "genericFilterOffset": genericFilterOffset,
       "genericFilterMask": genericFilterMask,
       "genericFilterValue": genericFilterValue,
       "genericFilterComparison": genericFilterComparison,
       "genericFilterChained": genericFilterChained,
       "genericFilterStatus": genericFilterStatus}
)
