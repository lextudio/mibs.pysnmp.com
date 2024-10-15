# SNMP MIB module (SUN-T300-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUN-T300-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:39 2024
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

t300 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Storage_subsystem_ObjectIdentity = ObjectIdentity
storage_subsystem = _Storage_subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28)
)
_T300Reg_ObjectIdentity = ObjectIdentity
t300Reg = _T300Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 1)
)
_T300Purple1_ObjectIdentity = ObjectIdentity
t300Purple1 = _T300Purple1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t300Purple1.setStatus("current")
_T300Objs_ObjectIdentity = ObjectIdentity
t300Objs = _T300Objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2)
)
_T300SystemObjs_ObjectIdentity = ObjectIdentity
t300SystemObjs = _T300SystemObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1)
)


class _SysId_Type(DisplayString):
    """Custom type sysId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysId_Type.__name__ = "DisplayString"
_SysId_Object = MibScalar
sysId = _SysId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 1),
    _SysId_Type()
)
sysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysId.setStatus("mandatory")


class _SysVendor_Type(DisplayString):
    """Custom type sysVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysVendor_Type.__name__ = "DisplayString"
_SysVendor_Object = MibScalar
sysVendor = _SysVendor_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 2),
    _SysVendor_Type()
)
sysVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVendor.setStatus("mandatory")


class _SysModel_Type(DisplayString):
    """Custom type sysModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysModel_Type.__name__ = "DisplayString"
_SysModel_Object = MibScalar
sysModel = _SysModel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 3),
    _SysModel_Type()
)
sysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysModel.setStatus("mandatory")


class _SysRevision_Type(DisplayString):
    """Custom type sysRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysRevision_Type.__name__ = "DisplayString"
_SysRevision_Object = MibScalar
sysRevision = _SysRevision_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 4),
    _SysRevision_Type()
)
sysRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRevision.setStatus("mandatory")
_SysStripeUnitSize_Type = Integer32
_SysStripeUnitSize_Object = MibScalar
sysStripeUnitSize = _SysStripeUnitSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 5),
    _SysStripeUnitSize_Type()
)
sysStripeUnitSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStripeUnitSize.setStatus("mandatory")


class _SysCacheMode_Type(Integer32):
    """Custom type sysCacheMode based on Integer32"""
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
        *(("auto", 4),
          ("disabled", 1),
          ("writeBehind", 3),
          ("writeThrough", 2))
    )


_SysCacheMode_Type.__name__ = "Integer32"
_SysCacheMode_Object = MibScalar
sysCacheMode = _SysCacheMode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 6),
    _SysCacheMode_Type()
)
sysCacheMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCacheMode.setStatus("mandatory")


class _SysCacheMirror_Type(Integer32):
    """Custom type sysCacheMirror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("off", 1))
    )


_SysCacheMirror_Type.__name__ = "Integer32"
_SysCacheMirror_Object = MibScalar
sysCacheMirror = _SysCacheMirror_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 7),
    _SysCacheMirror_Type()
)
sysCacheMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCacheMirror.setStatus("mandatory")


class _SysAutoDisable_Type(Integer32):
    """Custom type sysAutoDisable based on Integer32"""
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
        *(("disableOnly", 2),
          ("disableRecon", 3),
          ("none", 1),
          ("reconOnly", 4))
    )


_SysAutoDisable_Type.__name__ = "Integer32"
_SysAutoDisable_Object = MibScalar
sysAutoDisable = _SysAutoDisable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 8),
    _SysAutoDisable_Type()
)
sysAutoDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAutoDisable.setStatus("obsolete")


class _SysMpSupport_Type(Integer32):
    """Custom type sysMpSupport based on Integer32"""
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
        *(("mpxio", 3),
          ("none", 1),
          ("readWrite", 2),
          ("std", 4))
    )


_SysMpSupport_Type.__name__ = "Integer32"
_SysMpSupport_Object = MibScalar
sysMpSupport = _SysMpSupport_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 9),
    _SysMpSupport_Type()
)
sysMpSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMpSupport.setStatus("mandatory")


class _SysReadAhead_Type(Integer32):
    """Custom type sysReadAhead based on Integer32"""
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


_SysReadAhead_Type.__name__ = "Integer32"
_SysReadAhead_Object = MibScalar
sysReadAhead = _SysReadAhead_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 10),
    _SysReadAhead_Type()
)
sysReadAhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysReadAhead.setStatus("mandatory")


class _SysReconRate_Type(Integer32):
    """Custom type sysReconRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_SysReconRate_Type.__name__ = "Integer32"
_SysReconRate_Object = MibScalar
sysReconRate = _SysReconRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 11),
    _SysReconRate_Type()
)
sysReconRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysReconRate.setStatus("mandatory")


class _SysOndgMode_Type(Integer32):
    """Custom type sysOndgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("off", 1),
          ("passive", 2))
    )


_SysOndgMode_Type.__name__ = "Integer32"
_SysOndgMode_Object = MibScalar
sysOndgMode = _SysOndgMode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 12),
    _SysOndgMode_Type()
)
sysOndgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOndgMode.setStatus("mandatory")
_SysOndgTimeslice_Type = Integer32
_SysOndgTimeslice_Object = MibScalar
sysOndgTimeslice = _SysOndgTimeslice_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 13),
    _SysOndgTimeslice_Type()
)
sysOndgTimeslice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOndgTimeslice.setStatus("mandatory")
_SysIdleDiskTimeout_Type = Integer32
_SysIdleDiskTimeout_Object = MibScalar
sysIdleDiskTimeout = _SysIdleDiskTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 14),
    _SysIdleDiskTimeout_Type()
)
sysIdleDiskTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIdleDiskTimeout.setStatus("obsolete")
_SysFruRemovalShutdown_Type = Integer32
_SysFruRemovalShutdown_Object = MibScalar
sysFruRemovalShutdown = _SysFruRemovalShutdown_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 15),
    _SysFruRemovalShutdown_Type()
)
sysFruRemovalShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFruRemovalShutdown.setStatus("mandatory")


class _SysBootMode_Type(Integer32):
    """Custom type sysBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("none", 1),
          ("tftp", 3))
    )


_SysBootMode_Type.__name__ = "Integer32"
_SysBootMode_Object = MibScalar
sysBootMode = _SysBootMode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 16),
    _SysBootMode_Type()
)
sysBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootMode.setStatus("mandatory")
_SysBootDelay_Type = Integer32
_SysBootDelay_Object = MibScalar
sysBootDelay = _SysBootDelay_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 17),
    _SysBootDelay_Type()
)
sysBootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootDelay.setStatus("mandatory")
_SysSpinDelay_Type = Integer32
_SysSpinDelay_Object = MibScalar
sysSpinDelay = _SysSpinDelay_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 18),
    _SysSpinDelay_Type()
)
sysSpinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSpinDelay.setStatus("obsolete")
_SysTftpHost_Type = IpAddress
_SysTftpHost_Object = MibScalar
sysTftpHost = _SysTftpHost_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 19),
    _SysTftpHost_Type()
)
sysTftpHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTftpHost.setStatus("mandatory")


class _SysTftpFile_Type(DisplayString):
    """Custom type sysTftpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysTftpFile_Type.__name__ = "DisplayString"
_SysTftpFile_Object = MibScalar
sysTftpFile = _SysTftpFile_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 20),
    _SysTftpFile_Type()
)
sysTftpFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTftpFile.setStatus("mandatory")
_SysIpAddr_Type = IpAddress
_SysIpAddr_Object = MibScalar
sysIpAddr = _SysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 21),
    _SysIpAddr_Type()
)
sysIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIpAddr.setStatus("mandatory")
_SysSubNet_Type = IpAddress
_SysSubNet_Object = MibScalar
sysSubNet = _SysSubNet_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 22),
    _SysSubNet_Type()
)
sysSubNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSubNet.setStatus("mandatory")
_SysGateway_Type = IpAddress
_SysGateway_Object = MibScalar
sysGateway = _SysGateway_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 23),
    _SysGateway_Type()
)
sysGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysGateway.setStatus("mandatory")
_SysWriteRequests_Type = Counter32
_SysWriteRequests_Object = MibScalar
sysWriteRequests = _SysWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 24),
    _SysWriteRequests_Type()
)
sysWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysWriteRequests.setStatus("mandatory")
_SysReadRequests_Type = Counter32
_SysReadRequests_Object = MibScalar
sysReadRequests = _SysReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 25),
    _SysReadRequests_Type()
)
sysReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysReadRequests.setStatus("mandatory")
_SysBlocksWritten_Type = Counter32
_SysBlocksWritten_Object = MibScalar
sysBlocksWritten = _SysBlocksWritten_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 26),
    _SysBlocksWritten_Type()
)
sysBlocksWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBlocksWritten.setStatus("mandatory")
_SysBlocksRead_Type = Counter32
_SysBlocksRead_Object = MibScalar
sysBlocksRead = _SysBlocksRead_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 27),
    _SysBlocksRead_Type()
)
sysBlocksRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBlocksRead.setStatus("mandatory")
_SysCacheWriteHits_Type = Counter32
_SysCacheWriteHits_Object = MibScalar
sysCacheWriteHits = _SysCacheWriteHits_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 28),
    _SysCacheWriteHits_Type()
)
sysCacheWriteHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCacheWriteHits.setStatus("mandatory")
_SysCacheWriteMisses_Type = Counter32
_SysCacheWriteMisses_Object = MibScalar
sysCacheWriteMisses = _SysCacheWriteMisses_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 29),
    _SysCacheWriteMisses_Type()
)
sysCacheWriteMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCacheWriteMisses.setStatus("mandatory")
_SysCacheReadHits_Type = Counter32
_SysCacheReadHits_Object = MibScalar
sysCacheReadHits = _SysCacheReadHits_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 30),
    _SysCacheReadHits_Type()
)
sysCacheReadHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCacheReadHits.setStatus("mandatory")
_SysCacheReadMisses_Type = Counter32
_SysCacheReadMisses_Object = MibScalar
sysCacheReadMisses = _SysCacheReadMisses_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 31),
    _SysCacheReadMisses_Type()
)
sysCacheReadMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCacheReadMisses.setStatus("mandatory")
_SysCacheRmwFlushes_Type = Counter32
_SysCacheRmwFlushes_Object = MibScalar
sysCacheRmwFlushes = _SysCacheRmwFlushes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 32),
    _SysCacheRmwFlushes_Type()
)
sysCacheRmwFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCacheRmwFlushes.setStatus("mandatory")
_SysCacheReconFlushes_Type = Counter32
_SysCacheReconFlushes_Object = MibScalar
sysCacheReconFlushes = _SysCacheReconFlushes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 33),
    _SysCacheReconFlushes_Type()
)
sysCacheReconFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCacheReconFlushes.setStatus("mandatory")
_SysCacheStripeFlushes_Type = Counter32
_SysCacheStripeFlushes_Object = MibScalar
sysCacheStripeFlushes = _SysCacheStripeFlushes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 34),
    _SysCacheStripeFlushes_Type()
)
sysCacheStripeFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCacheStripeFlushes.setStatus("mandatory")


class _SysTimezone_Type(DisplayString):
    """Custom type sysTimezone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysTimezone_Type.__name__ = "DisplayString"
_SysTimezone_Object = MibScalar
sysTimezone = _SysTimezone_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 35),
    _SysTimezone_Type()
)
sysTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTimezone.setStatus("mandatory")


class _SysDate_Type(DisplayString):
    """Custom type sysDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysDate_Type.__name__ = "DisplayString"
_SysDate_Object = MibScalar
sysDate = _SysDate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 36),
    _SysDate_Type()
)
sysDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDate.setStatus("mandatory")


class _SysTime_Type(DisplayString):
    """Custom type sysTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysTime_Type.__name__ = "DisplayString"
_SysTime_Object = MibScalar
sysTime = _SysTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 37),
    _SysTime_Type()
)
sysTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTime.setStatus("mandatory")
_SysRootSession_Type = Integer32
_SysRootSession_Object = MibScalar
sysRootSession = _SysRootSession_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 38),
    _SysRootSession_Type()
)
sysRootSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRootSession.setStatus("obsolete")
_SysGuestSession_Type = Integer32
_SysGuestSession_Object = MibScalar
sysGuestSession = _SysGuestSession_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 39),
    _SysGuestSession_Type()
)
sysGuestSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysGuestSession.setStatus("obsolete")
_SysLastMessage_Type = DisplayString
_SysLastMessage_Object = MibScalar
sysLastMessage = _SysLastMessage_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 40),
    _SysLastMessage_Type()
)
sysLastMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLastMessage.setStatus("mandatory")


class _SysRarpEnabled_Type(Integer32):
    """Custom type sysRarpEnabled based on Integer32"""
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


_SysRarpEnabled_Type.__name__ = "Integer32"
_SysRarpEnabled_Object = MibScalar
sysRarpEnabled = _SysRarpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 41),
    _SysRarpEnabled_Type()
)
sysRarpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRarpEnabled.setStatus("mandatory")


class _SysLoop1Split_Type(Integer32):
    """Custom type sysLoop1Split based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("off", 1))
    )


_SysLoop1Split_Type.__name__ = "Integer32"
_SysLoop1Split_Object = MibScalar
sysLoop1Split = _SysLoop1Split_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 42),
    _SysLoop1Split_Type()
)
sysLoop1Split.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLoop1Split.setStatus("mandatory")


class _SysLastRestart_Type(DisplayString):
    """Custom type sysLastRestart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysLastRestart_Type.__name__ = "DisplayString"
_SysLastRestart_Object = MibScalar
sysLastRestart = _SysLastRestart_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 43),
    _SysLastRestart_Type()
)
sysLastRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLastRestart.setStatus("mandatory")


class _SysCtime_Type(DisplayString):
    """Custom type sysCtime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysCtime_Type.__name__ = "DisplayString"
_SysCtime_Object = MibScalar
sysCtime = _SysCtime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 44),
    _SysCtime_Type()
)
sysCtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCtime.setStatus("mandatory")


class _SysHasVolumes_Type(Integer32):
    """Custom type sysHasVolumes based on Integer32"""
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


_SysHasVolumes_Type.__name__ = "Integer32"
_SysHasVolumes_Object = MibScalar
sysHasVolumes = _SysHasVolumes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 1, 45),
    _SysHasVolumes_Type()
)
sysHasVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHasVolumes.setStatus("mandatory")
_T300UnitObjs_ObjectIdentity = ObjectIdentity
t300UnitObjs = _T300UnitObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 2)
)
_UnitCount_Type = Integer32
_UnitCount_Object = MibScalar
unitCount = _UnitCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 2, 1),
    _UnitCount_Type()
)
unitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCount.setStatus("mandatory")
_UnitTable_Object = MibTable
unitTable = _UnitTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    unitTable.setStatus("mandatory")
_UnitEntry_Object = MibTableRow
unitEntry = _UnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 2, 2, 1)
)
unitEntry.setIndexNames(
    (0, "SUN-T300-MIB", "unitIndex"),
)
if mibBuilder.loadTexts:
    unitEntry.setStatus("mandatory")
_UnitIndex_Type = Integer32
_UnitIndex_Object = MibTableColumn
unitIndex = _UnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 2, 2, 1, 1),
    _UnitIndex_Type()
)
unitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitIndex.setStatus("mandatory")


class _UnitId_Type(DisplayString):
    """Custom type unitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_UnitId_Type.__name__ = "DisplayString"
_UnitId_Object = MibTableColumn
unitId = _UnitId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 2, 2, 1, 2),
    _UnitId_Type()
)
unitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitId.setStatus("mandatory")


class _UnitType_Type(Integer32):
    """Custom type unitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controller", 1),
          ("expansion", 2))
    )


_UnitType_Type.__name__ = "Integer32"
_UnitType_Object = MibTableColumn
unitType = _UnitType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 2, 2, 1, 3),
    _UnitType_Type()
)
unitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitType.setStatus("mandatory")


class _UnitStandby_Type(Integer32):
    """Custom type unitStandby based on Integer32"""
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


_UnitStandby_Type.__name__ = "Integer32"
_UnitStandby_Object = MibTableColumn
unitStandby = _UnitStandby_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 2, 2, 1, 4),
    _UnitStandby_Type()
)
unitStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitStandby.setStatus("mandatory")
_T300FruObjs_ObjectIdentity = ObjectIdentity
t300FruObjs = _T300FruObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3)
)
_FruCount_Type = Integer32
_FruCount_Object = MibScalar
fruCount = _FruCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 1),
    _FruCount_Type()
)
fruCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruCount.setStatus("mandatory")
_FruTable_Object = MibTable
fruTable = _FruTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fruTable.setStatus("mandatory")
_FruEntry_Object = MibTableRow
fruEntry = _FruEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 2, 1)
)
fruEntry.setIndexNames(
    (0, "SUN-T300-MIB", "unitIndex"),
    (0, "SUN-T300-MIB", "fruIndex"),
)
if mibBuilder.loadTexts:
    fruEntry.setStatus("mandatory")
_FruIndex_Type = Integer32
_FruIndex_Object = MibTableColumn
fruIndex = _FruIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 2, 1, 1),
    _FruIndex_Type()
)
fruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruIndex.setStatus("mandatory")


class _FruId_Type(DisplayString):
    """Custom type fruId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruId_Type.__name__ = "DisplayString"
_FruId_Object = MibTableColumn
fruId = _FruId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 2, 1, 2),
    _FruId_Type()
)
fruId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruId.setStatus("mandatory")


class _FruType_Type(Integer32):
    """Custom type fruType based on Integer32"""
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
        *(("controllerCard", 2),
          ("diskDrive", 1),
          ("loopCard", 3),
          ("midplane", 5),
          ("powerUnit", 4))
    )


_FruType_Type.__name__ = "Integer32"
_FruType_Object = MibTableColumn
fruType = _FruType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 2, 1, 3),
    _FruType_Type()
)
fruType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruType.setStatus("mandatory")


class _FruStatus_Type(Integer32):
    """Custom type fruStatus based on Integer32"""
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
        *(("booting", 5),
          ("fault", 2),
          ("notInstalled", 1),
          ("offline", 4),
          ("ready", 3))
    )


_FruStatus_Type.__name__ = "Integer32"
_FruStatus_Object = MibTableColumn
fruStatus = _FruStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 2, 1, 4),
    _FruStatus_Type()
)
fruStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruStatus.setStatus("mandatory")


class _FruState_Type(Integer32):
    """Custom type fruState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("missing", 4),
          ("substituted", 3))
    )


_FruState_Type.__name__ = "Integer32"
_FruState_Object = MibTableColumn
fruState = _FruState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 2, 1, 5),
    _FruState_Type()
)
fruState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruState.setStatus("mandatory")


class _FruVendor_Type(DisplayString):
    """Custom type fruVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruVendor_Type.__name__ = "DisplayString"
_FruVendor_Object = MibTableColumn
fruVendor = _FruVendor_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 2, 1, 6),
    _FruVendor_Type()
)
fruVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruVendor.setStatus("mandatory")


class _FruModel_Type(DisplayString):
    """Custom type fruModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruModel_Type.__name__ = "DisplayString"
_FruModel_Object = MibTableColumn
fruModel = _FruModel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 2, 1, 7),
    _FruModel_Type()
)
fruModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruModel.setStatus("mandatory")


class _FruRevision_Type(DisplayString):
    """Custom type fruRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruRevision_Type.__name__ = "DisplayString"
_FruRevision_Object = MibTableColumn
fruRevision = _FruRevision_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 2, 1, 8),
    _FruRevision_Type()
)
fruRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruRevision.setStatus("mandatory")


class _FruSerialNo_Type(DisplayString):
    """Custom type fruSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruSerialNo_Type.__name__ = "DisplayString"
_FruSerialNo_Object = MibTableColumn
fruSerialNo = _FruSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 2, 1, 9),
    _FruSerialNo_Type()
)
fruSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruSerialNo.setStatus("mandatory")
_FruErrors_Type = Integer32
_FruErrors_Object = MibTableColumn
fruErrors = _FruErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 2, 1, 10),
    _FruErrors_Type()
)
fruErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruErrors.setStatus("mandatory")
_FruDiskCount_Type = Integer32
_FruDiskCount_Object = MibScalar
fruDiskCount = _FruDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 3),
    _FruDiskCount_Type()
)
fruDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDiskCount.setStatus("mandatory")
_FruDiskTable_Object = MibTable
fruDiskTable = _FruDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    fruDiskTable.setStatus("mandatory")
_FruDiskEntry_Object = MibTableRow
fruDiskEntry = _FruDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 4, 1)
)
fruDiskEntry.setIndexNames(
    (0, "SUN-T300-MIB", "unitIndex"),
    (0, "SUN-T300-MIB", "fruIndex"),
)
if mibBuilder.loadTexts:
    fruDiskEntry.setStatus("mandatory")


class _FruDiskRole_Type(Integer32):
    """Custom type fruDiskRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dataDisk", 2),
          ("standbyDisk", 3),
          ("unassigned", 1))
    )


_FruDiskRole_Type.__name__ = "Integer32"
_FruDiskRole_Object = MibTableColumn
fruDiskRole = _FruDiskRole_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 4, 1, 1),
    _FruDiskRole_Type()
)
fruDiskRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDiskRole.setStatus("mandatory")


class _FruDiskPort1State_Type(Integer32):
    """Custom type fruDiskPort1State based on Integer32"""
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
        *(("bypass", 3),
          ("notReady", 2),
          ("ready", 1),
          ("unknown", 4))
    )


_FruDiskPort1State_Type.__name__ = "Integer32"
_FruDiskPort1State_Object = MibTableColumn
fruDiskPort1State = _FruDiskPort1State_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 4, 1, 2),
    _FruDiskPort1State_Type()
)
fruDiskPort1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDiskPort1State.setStatus("mandatory")


class _FruDiskPort2State_Type(Integer32):
    """Custom type fruDiskPort2State based on Integer32"""
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
        *(("bypass", 3),
          ("notReady", 2),
          ("ready", 1),
          ("unknown", 4))
    )


_FruDiskPort2State_Type.__name__ = "Integer32"
_FruDiskPort2State_Object = MibTableColumn
fruDiskPort2State = _FruDiskPort2State_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 4, 1, 3),
    _FruDiskPort2State_Type()
)
fruDiskPort2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDiskPort2State.setStatus("mandatory")
_FruDiskCapacity_Type = Integer32
_FruDiskCapacity_Object = MibTableColumn
fruDiskCapacity = _FruDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 4, 1, 4),
    _FruDiskCapacity_Type()
)
fruDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDiskCapacity.setStatus("mandatory")


class _FruDiskStatusCode_Type(DisplayString):
    """Custom type fruDiskStatusCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruDiskStatusCode_Type.__name__ = "DisplayString"
_FruDiskStatusCode_Object = MibTableColumn
fruDiskStatusCode = _FruDiskStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 4, 1, 5),
    _FruDiskStatusCode_Type()
)
fruDiskStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDiskStatusCode.setStatus("mandatory")


class _FruDiskVolName_Type(DisplayString):
    """Custom type fruDiskVolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruDiskVolName_Type.__name__ = "DisplayString"
_FruDiskVolName_Object = MibTableColumn
fruDiskVolName = _FruDiskVolName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 4, 1, 6),
    _FruDiskVolName_Type()
)
fruDiskVolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDiskVolName.setStatus("mandatory")
_FruDiskTemp_Type = Integer32
_FruDiskTemp_Object = MibTableColumn
fruDiskTemp = _FruDiskTemp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 4, 1, 7),
    _FruDiskTemp_Type()
)
fruDiskTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruDiskTemp.setStatus("mandatory")
_FruCtlrCount_Type = Integer32
_FruCtlrCount_Object = MibScalar
fruCtlrCount = _FruCtlrCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 5),
    _FruCtlrCount_Type()
)
fruCtlrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruCtlrCount.setStatus("mandatory")
_FruCtlrTable_Object = MibTable
fruCtlrTable = _FruCtlrTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 6)
)
if mibBuilder.loadTexts:
    fruCtlrTable.setStatus("mandatory")
_FruCtlrEntry_Object = MibTableRow
fruCtlrEntry = _FruCtlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 6, 1)
)
fruCtlrEntry.setIndexNames(
    (0, "SUN-T300-MIB", "unitIndex"),
    (0, "SUN-T300-MIB", "fruIndex"),
)
if mibBuilder.loadTexts:
    fruCtlrEntry.setStatus("mandatory")


class _FruCtlrCpuDesc_Type(DisplayString):
    """Custom type fruCtlrCpuDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruCtlrCpuDesc_Type.__name__ = "DisplayString"
_FruCtlrCpuDesc_Object = MibTableColumn
fruCtlrCpuDesc = _FruCtlrCpuDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 6, 1, 1),
    _FruCtlrCpuDesc_Type()
)
fruCtlrCpuDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruCtlrCpuDesc.setStatus("mandatory")


class _FruCtlrRole_Type(Integer32):
    """Custom type fruCtlrRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternateMaster", 2),
          ("master", 1),
          ("slave", 3))
    )


_FruCtlrRole_Type.__name__ = "Integer32"
_FruCtlrRole_Object = MibTableColumn
fruCtlrRole = _FruCtlrRole_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 6, 1, 2),
    _FruCtlrRole_Type()
)
fruCtlrRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruCtlrRole.setStatus("mandatory")


class _FruCtlrPartnerId_Type(DisplayString):
    """Custom type fruCtlrPartnerId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruCtlrPartnerId_Type.__name__ = "DisplayString"
_FruCtlrPartnerId_Object = MibTableColumn
fruCtlrPartnerId = _FruCtlrPartnerId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 6, 1, 3),
    _FruCtlrPartnerId_Type()
)
fruCtlrPartnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruCtlrPartnerId.setStatus("mandatory")


class _FruCtlrCtState_Type(Integer32):
    """Custom type fruCtlrCtState based on Integer32"""
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
        *(("booting", 2),
          ("disabled", 4),
          ("disabling", 5),
          ("expansionUnit", 1),
          ("hotPlug", 9),
          ("online", 3),
          ("reconfig", 8),
          ("reset", 6),
          ("resetting", 7),
          ("virtual", 10))
    )


_FruCtlrCtState_Type.__name__ = "Integer32"
_FruCtlrCtState_Object = MibTableColumn
fruCtlrCtState = _FruCtlrCtState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 6, 1, 4),
    _FruCtlrCtState_Type()
)
fruCtlrCtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruCtlrCtState.setStatus("mandatory")
_FruCtlrCacheSize_Type = Integer32
_FruCtlrCacheSize_Object = MibTableColumn
fruCtlrCacheSize = _FruCtlrCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 6, 1, 5),
    _FruCtlrCacheSize_Type()
)
fruCtlrCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruCtlrCacheSize.setStatus("mandatory")
_FruCtlrTemp_Type = Integer32
_FruCtlrTemp_Object = MibTableColumn
fruCtlrTemp = _FruCtlrTemp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 6, 1, 6),
    _FruCtlrTemp_Type()
)
fruCtlrTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruCtlrTemp.setStatus("mandatory")


class _FruCtlrMdate_Type(DisplayString):
    """Custom type fruCtlrMdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruCtlrMdate_Type.__name__ = "DisplayString"
_FruCtlrMdate_Object = MibTableColumn
fruCtlrMdate = _FruCtlrMdate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 6, 1, 7),
    _FruCtlrMdate_Type()
)
fruCtlrMdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruCtlrMdate.setStatus("mandatory")
_FruCtlrConsoleBaud_Type = Integer32
_FruCtlrConsoleBaud_Object = MibTableColumn
fruCtlrConsoleBaud = _FruCtlrConsoleBaud_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 6, 1, 8),
    _FruCtlrConsoleBaud_Type()
)
fruCtlrConsoleBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruCtlrConsoleBaud.setStatus("mandatory")
_FruLoopCount_Type = Integer32
_FruLoopCount_Object = MibScalar
fruLoopCount = _FruLoopCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 7),
    _FruLoopCount_Type()
)
fruLoopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruLoopCount.setStatus("mandatory")
_FruLoopTable_Object = MibTable
fruLoopTable = _FruLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    fruLoopTable.setStatus("mandatory")
_FruLoopEntry_Object = MibTableRow
fruLoopEntry = _FruLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 8, 1)
)
fruLoopEntry.setIndexNames(
    (0, "SUN-T300-MIB", "unitIndex"),
    (0, "SUN-T300-MIB", "fruIndex"),
)
if mibBuilder.loadTexts:
    fruLoopEntry.setStatus("mandatory")


class _FruLoopMode_Type(Integer32):
    """Custom type fruLoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_FruLoopMode_Type.__name__ = "Integer32"
_FruLoopMode_Object = MibTableColumn
fruLoopMode = _FruLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 8, 1, 1),
    _FruLoopMode_Type()
)
fruLoopMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruLoopMode.setStatus("mandatory")
_FruLoopTemp_Type = Integer32
_FruLoopTemp_Object = MibTableColumn
fruLoopTemp = _FruLoopTemp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 8, 1, 2),
    _FruLoopTemp_Type()
)
fruLoopTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruLoopTemp.setStatus("mandatory")


class _FruLoopCable1State_Type(Integer32):
    """Custom type fruLoopCable1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_FruLoopCable1State_Type.__name__ = "Integer32"
_FruLoopCable1State_Object = MibTableColumn
fruLoopCable1State = _FruLoopCable1State_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 8, 1, 3),
    _FruLoopCable1State_Type()
)
fruLoopCable1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruLoopCable1State.setStatus("mandatory")


class _FruLoopCable2State_Type(Integer32):
    """Custom type fruLoopCable2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_FruLoopCable2State_Type.__name__ = "Integer32"
_FruLoopCable2State_Object = MibTableColumn
fruLoopCable2State = _FruLoopCable2State_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 8, 1, 4),
    _FruLoopCable2State_Type()
)
fruLoopCable2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruLoopCable2State.setStatus("mandatory")


class _FruLoopMdate_Type(DisplayString):
    """Custom type fruLoopMdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruLoopMdate_Type.__name__ = "DisplayString"
_FruLoopMdate_Object = MibTableColumn
fruLoopMdate = _FruLoopMdate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 8, 1, 5),
    _FruLoopMdate_Type()
)
fruLoopMdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruLoopMdate.setStatus("mandatory")
_FruPowerCount_Type = Integer32
_FruPowerCount_Object = MibScalar
fruPowerCount = _FruPowerCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 9),
    _FruPowerCount_Type()
)
fruPowerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPowerCount.setStatus("mandatory")
_FruPowerTable_Object = MibTable
fruPowerTable = _FruPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 10)
)
if mibBuilder.loadTexts:
    fruPowerTable.setStatus("mandatory")
_FruPowerEntry_Object = MibTableRow
fruPowerEntry = _FruPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 10, 1)
)
fruPowerEntry.setIndexNames(
    (0, "SUN-T300-MIB", "unitIndex"),
    (0, "SUN-T300-MIB", "fruIndex"),
)
if mibBuilder.loadTexts:
    fruPowerEntry.setStatus("mandatory")


class _FruPowerPowOutput_Type(Integer32):
    """Custom type fruPowerPowOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("normal", 2),
          ("off", 1))
    )


_FruPowerPowOutput_Type.__name__ = "Integer32"
_FruPowerPowOutput_Object = MibTableColumn
fruPowerPowOutput = _FruPowerPowOutput_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 10, 1, 1),
    _FruPowerPowOutput_Type()
)
fruPowerPowOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPowerPowOutput.setStatus("mandatory")


class _FruPowerPowSource_Type(Integer32):
    """Custom type fruPowerPowSource based on Integer32"""
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
        *(("battery", 2),
          ("line", 1),
          ("none", 4),
          ("unknown", 3))
    )


_FruPowerPowSource_Type.__name__ = "Integer32"
_FruPowerPowSource_Object = MibTableColumn
fruPowerPowSource = _FruPowerPowSource_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 10, 1, 2),
    _FruPowerPowSource_Type()
)
fruPowerPowSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPowerPowSource.setStatus("mandatory")


class _FruPowerPowTemp_Type(Integer32):
    """Custom type fruPowerPowTemp based on Integer32"""
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
        *(("none", 4),
          ("normal", 1),
          ("overTemp", 2),
          ("unknown", 3))
    )


_FruPowerPowTemp_Type.__name__ = "Integer32"
_FruPowerPowTemp_Object = MibTableColumn
fruPowerPowTemp = _FruPowerPowTemp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 10, 1, 3),
    _FruPowerPowTemp_Type()
)
fruPowerPowTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPowerPowTemp.setStatus("mandatory")


class _FruPowerFan1State_Type(Integer32):
    """Custom type fruPowerFan1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("missing", 3),
          ("normal", 1))
    )


_FruPowerFan1State_Type.__name__ = "Integer32"
_FruPowerFan1State_Object = MibTableColumn
fruPowerFan1State = _FruPowerFan1State_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 10, 1, 4),
    _FruPowerFan1State_Type()
)
fruPowerFan1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPowerFan1State.setStatus("mandatory")


class _FruPowerFan2State_Type(Integer32):
    """Custom type fruPowerFan2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("missing", 3),
          ("normal", 1))
    )


_FruPowerFan2State_Type.__name__ = "Integer32"
_FruPowerFan2State_Object = MibTableColumn
fruPowerFan2State = _FruPowerFan2State_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 10, 1, 5),
    _FruPowerFan2State_Type()
)
fruPowerFan2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPowerFan2State.setStatus("mandatory")


class _FruPowerBatState_Type(Integer32):
    """Custom type fruPowerBatState based on Integer32"""
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
        *(("fault", 3),
          ("normal", 2),
          ("notInstalled", 1),
          ("refreshing", 4),
          ("unknown", 5))
    )


_FruPowerBatState_Type.__name__ = "Integer32"
_FruPowerBatState_Object = MibTableColumn
fruPowerBatState = _FruPowerBatState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 10, 1, 6),
    _FruPowerBatState_Type()
)
fruPowerBatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPowerBatState.setStatus("mandatory")
_FruPowerBatLife_Type = Integer32
_FruPowerBatLife_Object = MibTableColumn
fruPowerBatLife = _FruPowerBatLife_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 10, 1, 7),
    _FruPowerBatLife_Type()
)
fruPowerBatLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPowerBatLife.setStatus("mandatory")
_FruPowerBatUsed_Type = Integer32
_FruPowerBatUsed_Object = MibTableColumn
fruPowerBatUsed = _FruPowerBatUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 10, 1, 8),
    _FruPowerBatUsed_Type()
)
fruPowerBatUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPowerBatUsed.setStatus("mandatory")


class _FruPowerPowMdate_Type(DisplayString):
    """Custom type fruPowerPowMdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruPowerPowMdate_Type.__name__ = "DisplayString"
_FruPowerPowMdate_Object = MibTableColumn
fruPowerPowMdate = _FruPowerPowMdate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 10, 1, 9),
    _FruPowerPowMdate_Type()
)
fruPowerPowMdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPowerPowMdate.setStatus("mandatory")


class _FruPowerBatMdate_Type(DisplayString):
    """Custom type fruPowerBatMdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruPowerBatMdate_Type.__name__ = "DisplayString"
_FruPowerBatMdate_Object = MibTableColumn
fruPowerBatMdate = _FruPowerBatMdate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 10, 1, 10),
    _FruPowerBatMdate_Type()
)
fruPowerBatMdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruPowerBatMdate.setStatus("mandatory")
_FruMidplaneCount_Type = Integer32
_FruMidplaneCount_Object = MibScalar
fruMidplaneCount = _FruMidplaneCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 11),
    _FruMidplaneCount_Type()
)
fruMidplaneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruMidplaneCount.setStatus("mandatory")
_FruMidplaneTable_Object = MibTable
fruMidplaneTable = _FruMidplaneTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 12)
)
if mibBuilder.loadTexts:
    fruMidplaneTable.setStatus("mandatory")
_FruMidplaneEntry_Object = MibTableRow
fruMidplaneEntry = _FruMidplaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 12, 1)
)
fruMidplaneEntry.setIndexNames(
    (0, "SUN-T300-MIB", "unitIndex"),
    (0, "SUN-T300-MIB", "fruIndex"),
)
if mibBuilder.loadTexts:
    fruMidplaneEntry.setStatus("mandatory")


class _FruMidplaneMdate_Type(DisplayString):
    """Custom type fruMidplaneMdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FruMidplaneMdate_Type.__name__ = "DisplayString"
_FruMidplaneMdate_Object = MibTableColumn
fruMidplaneMdate = _FruMidplaneMdate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 3, 12, 1, 1),
    _FruMidplaneMdate_Type()
)
fruMidplaneMdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruMidplaneMdate.setStatus("mandatory")
_T300VolumeObjs_ObjectIdentity = ObjectIdentity
t300VolumeObjs = _T300VolumeObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4)
)
_VolCount_Type = Integer32
_VolCount_Object = MibScalar
volCount = _VolCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 1),
    _VolCount_Type()
)
volCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCount.setStatus("mandatory")
_VolTable_Object = MibTable
volTable = _VolTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    volTable.setStatus("mandatory")
_VolEntry_Object = MibTableRow
volEntry = _VolEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1)
)
volEntry.setIndexNames(
    (0, "SUN-T300-MIB", "unitIndex"),
    (0, "SUN-T300-MIB", "volIndex"),
)
if mibBuilder.loadTexts:
    volEntry.setStatus("mandatory")
_VolIndex_Type = Integer32
_VolIndex_Object = MibTableColumn
volIndex = _VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 1),
    _VolIndex_Type()
)
volIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIndex.setStatus("mandatory")


class _VolId_Type(DisplayString):
    """Custom type volId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VolId_Type.__name__ = "DisplayString"
_VolId_Object = MibTableColumn
volId = _VolId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 2),
    _VolId_Type()
)
volId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volId.setStatus("mandatory")


class _VolName_Type(DisplayString):
    """Custom type volName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VolName_Type.__name__ = "DisplayString"
_VolName_Object = MibTableColumn
volName = _VolName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 3),
    _VolName_Type()
)
volName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volName.setStatus("mandatory")


class _VolWWN_Type(DisplayString):
    """Custom type volWWN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VolWWN_Type.__name__ = "DisplayString"
_VolWWN_Object = MibTableColumn
volWWN = _VolWWN_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 4),
    _VolWWN_Type()
)
volWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volWWN.setStatus("mandatory")


class _VolStatus_Type(Integer32):
    """Custom type volStatus based on Integer32"""
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
        *(("deleted", 1),
          ("mounted", 4),
          ("uninitialized", 2),
          ("unmounted", 3))
    )


_VolStatus_Type.__name__ = "Integer32"
_VolStatus_Object = MibTableColumn
volStatus = _VolStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 5),
    _VolStatus_Type()
)
volStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volStatus.setStatus("mandatory")


class _VolCacheMode_Type(Integer32):
    """Custom type volCacheMode based on Integer32"""
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
        *(("auto", 4),
          ("disabled", 1),
          ("writeBehind", 3),
          ("writeThrough", 2))
    )


_VolCacheMode_Type.__name__ = "Integer32"
_VolCacheMode_Object = MibTableColumn
volCacheMode = _VolCacheMode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 6),
    _VolCacheMode_Type()
)
volCacheMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCacheMode.setStatus("mandatory")


class _VolCacheMirror_Type(Integer32):
    """Custom type volCacheMirror based on Integer32"""
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


_VolCacheMirror_Type.__name__ = "Integer32"
_VolCacheMirror_Object = MibTableColumn
volCacheMirror = _VolCacheMirror_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 7),
    _VolCacheMirror_Type()
)
volCacheMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCacheMirror.setStatus("mandatory")
_VolCapacity_Type = Integer32
_VolCapacity_Object = MibTableColumn
volCapacity = _VolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 8),
    _VolCapacity_Type()
)
volCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCapacity.setStatus("mandatory")
_VolArrayWidth_Type = Integer32
_VolArrayWidth_Object = MibTableColumn
volArrayWidth = _VolArrayWidth_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 9),
    _VolArrayWidth_Type()
)
volArrayWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volArrayWidth.setStatus("mandatory")


class _VolRaidLevel_Type(Integer32):
    """Custom type volRaidLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("raid0", 1),
          ("raid1", 2),
          ("raid5", 3))
    )


_VolRaidLevel_Type.__name__ = "Integer32"
_VolRaidLevel_Object = MibTableColumn
volRaidLevel = _VolRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 10),
    _VolRaidLevel_Type()
)
volRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volRaidLevel.setStatus("mandatory")
_VolWriteRequests_Type = Counter32
_VolWriteRequests_Object = MibTableColumn
volWriteRequests = _VolWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 11),
    _VolWriteRequests_Type()
)
volWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volWriteRequests.setStatus("mandatory")
_VolReadRequests_Type = Counter32
_VolReadRequests_Object = MibTableColumn
volReadRequests = _VolReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 12),
    _VolReadRequests_Type()
)
volReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volReadRequests.setStatus("mandatory")
_VolBlocksWritten_Type = Counter32
_VolBlocksWritten_Object = MibTableColumn
volBlocksWritten = _VolBlocksWritten_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 13),
    _VolBlocksWritten_Type()
)
volBlocksWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volBlocksWritten.setStatus("mandatory")
_VolBlocksRead_Type = Counter32
_VolBlocksRead_Object = MibTableColumn
volBlocksRead = _VolBlocksRead_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 14),
    _VolBlocksRead_Type()
)
volBlocksRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volBlocksRead.setStatus("mandatory")
_VolSoftErrors_Type = Counter32
_VolSoftErrors_Object = MibTableColumn
volSoftErrors = _VolSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 15),
    _VolSoftErrors_Type()
)
volSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volSoftErrors.setStatus("mandatory")
_VolFirmErrors_Type = Counter32
_VolFirmErrors_Object = MibTableColumn
volFirmErrors = _VolFirmErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 16),
    _VolFirmErrors_Type()
)
volFirmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volFirmErrors.setStatus("mandatory")
_VolHardErrors_Type = Counter32
_VolHardErrors_Object = MibTableColumn
volHardErrors = _VolHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 17),
    _VolHardErrors_Type()
)
volHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volHardErrors.setStatus("mandatory")
_VolCacheWriteHits_Type = Counter32
_VolCacheWriteHits_Object = MibTableColumn
volCacheWriteHits = _VolCacheWriteHits_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 18),
    _VolCacheWriteHits_Type()
)
volCacheWriteHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCacheWriteHits.setStatus("mandatory")
_VolCacheWriteMisses_Type = Counter32
_VolCacheWriteMisses_Object = MibTableColumn
volCacheWriteMisses = _VolCacheWriteMisses_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 19),
    _VolCacheWriteMisses_Type()
)
volCacheWriteMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCacheWriteMisses.setStatus("mandatory")
_VolCacheReadHits_Type = Counter32
_VolCacheReadHits_Object = MibTableColumn
volCacheReadHits = _VolCacheReadHits_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 20),
    _VolCacheReadHits_Type()
)
volCacheReadHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCacheReadHits.setStatus("mandatory")
_VolCacheReadMisses_Type = Counter32
_VolCacheReadMisses_Object = MibTableColumn
volCacheReadMisses = _VolCacheReadMisses_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 21),
    _VolCacheReadMisses_Type()
)
volCacheReadMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCacheReadMisses.setStatus("mandatory")
_VolCacheRmwFlushes_Type = Counter32
_VolCacheRmwFlushes_Object = MibTableColumn
volCacheRmwFlushes = _VolCacheRmwFlushes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 22),
    _VolCacheRmwFlushes_Type()
)
volCacheRmwFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCacheRmwFlushes.setStatus("mandatory")
_VolCacheReconFlushes_Type = Counter32
_VolCacheReconFlushes_Object = MibTableColumn
volCacheReconFlushes = _VolCacheReconFlushes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 23),
    _VolCacheReconFlushes_Type()
)
volCacheReconFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCacheReconFlushes.setStatus("mandatory")
_VolCacheStripeFlushes_Type = Counter32
_VolCacheStripeFlushes_Object = MibTableColumn
volCacheStripeFlushes = _VolCacheStripeFlushes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 24),
    _VolCacheStripeFlushes_Type()
)
volCacheStripeFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCacheStripeFlushes.setStatus("mandatory")


class _VolDisabledDisk_Type(DisplayString):
    """Custom type volDisabledDisk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VolDisabledDisk_Type.__name__ = "DisplayString"
_VolDisabledDisk_Object = MibTableColumn
volDisabledDisk = _VolDisabledDisk_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 25),
    _VolDisabledDisk_Type()
)
volDisabledDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDisabledDisk.setStatus("mandatory")


class _VolSubstitutedDisk_Type(DisplayString):
    """Custom type volSubstitutedDisk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VolSubstitutedDisk_Type.__name__ = "DisplayString"
_VolSubstitutedDisk_Object = MibTableColumn
volSubstitutedDisk = _VolSubstitutedDisk_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 26),
    _VolSubstitutedDisk_Type()
)
volSubstitutedDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volSubstitutedDisk.setStatus("mandatory")


class _VolOper_Type(Integer32):
    """Custom type volOper based on Integer32"""
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
        *(("copyingFromStandby", 4),
          ("copyingToStandby", 5),
          ("initializing", 6),
          ("none", 1),
          ("reconstructing", 2),
          ("reconstructingToStandby", 3),
          ("verifying", 7))
    )


_VolOper_Type.__name__ = "Integer32"
_VolOper_Object = MibTableColumn
volOper = _VolOper_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 27),
    _VolOper_Type()
)
volOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volOper.setStatus("mandatory")
_VolOperProgress_Type = Integer32
_VolOperProgress_Object = MibTableColumn
volOperProgress = _VolOperProgress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 28),
    _VolOperProgress_Type()
)
volOperProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volOperProgress.setStatus("mandatory")
_VolInitRate_Type = Integer32
_VolInitRate_Object = MibTableColumn
volInitRate = _VolInitRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 29),
    _VolInitRate_Type()
)
volInitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volInitRate.setStatus("mandatory")
_VolVerifyRate_Type = Integer32
_VolVerifyRate_Object = MibTableColumn
volVerifyRate = _VolVerifyRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 4, 2, 1, 30),
    _VolVerifyRate_Type()
)
volVerifyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volVerifyRate.setStatus("mandatory")
_T300PortObjs_ObjectIdentity = ObjectIdentity
t300PortObjs = _T300PortObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5)
)
_PortCount_Type = Integer32
_PortCount_Object = MibScalar
portCount = _PortCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 1),
    _PortCount_Type()
)
portCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCount.setStatus("mandatory")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1)
)
portEntry.setIndexNames(
    (0, "SUN-T300-MIB", "unitIndex"),
    (0, "SUN-T300-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")


class _PortId_Type(DisplayString):
    """Custom type portId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_PortId_Type.__name__ = "DisplayString"
_PortId_Object = MibTableColumn
portId = _PortId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1, 2),
    _PortId_Type()
)
portId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portId.setStatus("mandatory")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fibreChannel", 2),
          ("ultraScsi", 1))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1, 3),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("mandatory")


class _PortFruId_Type(DisplayString):
    """Custom type portFruId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_PortFruId_Type.__name__ = "DisplayString"
_PortFruId_Object = MibTableColumn
portFruId = _PortFruId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1, 4),
    _PortFruId_Type()
)
portFruId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFruId.setStatus("mandatory")
_PortWriteRequests_Type = Counter32
_PortWriteRequests_Object = MibTableColumn
portWriteRequests = _PortWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1, 5),
    _PortWriteRequests_Type()
)
portWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portWriteRequests.setStatus("mandatory")
_PortReadRequests_Type = Counter32
_PortReadRequests_Object = MibTableColumn
portReadRequests = _PortReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1, 6),
    _PortReadRequests_Type()
)
portReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portReadRequests.setStatus("mandatory")
_PortBlocksWritten_Type = Counter32
_PortBlocksWritten_Object = MibTableColumn
portBlocksWritten = _PortBlocksWritten_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1, 7),
    _PortBlocksWritten_Type()
)
portBlocksWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBlocksWritten.setStatus("mandatory")
_PortBlocksRead_Type = Counter32
_PortBlocksRead_Object = MibTableColumn
portBlocksRead = _PortBlocksRead_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1, 8),
    _PortBlocksRead_Type()
)
portBlocksRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBlocksRead.setStatus("mandatory")


class _PortSunHost_Type(Integer32):
    """Custom type portSunHost based on Integer32"""
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


_PortSunHost_Type.__name__ = "Integer32"
_PortSunHost_Object = MibTableColumn
portSunHost = _PortSunHost_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1, 9),
    _PortSunHost_Type()
)
portSunHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSunHost.setStatus("mandatory")


class _PortWWN_Type(DisplayString):
    """Custom type portWWN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 136),
    )


_PortWWN_Type.__name__ = "DisplayString"
_PortWWN_Object = MibTableColumn
portWWN = _PortWWN_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1, 10),
    _PortWWN_Type()
)
portWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portWWN.setStatus("mandatory")


class _PortStatus_Type(Integer32):
    """Custom type portStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )


_PortStatus_Type.__name__ = "Integer32"
_PortStatus_Object = MibTableColumn
portStatus = _PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1, 11),
    _PortStatus_Type()
)
portStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatus.setStatus("mandatory")
_PortErrors_Type = Integer32
_PortErrors_Object = MibTableColumn
portErrors = _PortErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 2, 1, 12),
    _PortErrors_Type()
)
portErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portErrors.setStatus("mandatory")
_PortFibreCount_Type = Integer32
_PortFibreCount_Object = MibScalar
portFibreCount = _PortFibreCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 3),
    _PortFibreCount_Type()
)
portFibreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFibreCount.setStatus("mandatory")
_PortFibreTable_Object = MibTable
portFibreTable = _PortFibreTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 4)
)
if mibBuilder.loadTexts:
    portFibreTable.setStatus("mandatory")
_PortFibreEntry_Object = MibTableRow
portFibreEntry = _PortFibreEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 4, 1)
)
portFibreEntry.setIndexNames(
    (0, "SUN-T300-MIB", "unitIndex"),
    (0, "SUN-T300-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portFibreEntry.setStatus("mandatory")


class _PortFibreAlpaMode_Type(Integer32):
    """Custom type portFibreAlpaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 2))
    )


_PortFibreAlpaMode_Type.__name__ = "Integer32"
_PortFibreAlpaMode_Object = MibTableColumn
portFibreAlpaMode = _PortFibreAlpaMode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 4, 1, 1),
    _PortFibreAlpaMode_Type()
)
portFibreAlpaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFibreAlpaMode.setStatus("mandatory")
_PortFibreAlpa_Type = Integer32
_PortFibreAlpa_Object = MibTableColumn
portFibreAlpa = _PortFibreAlpa_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 5, 4, 1, 2),
    _PortFibreAlpa_Type()
)
portFibreAlpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFibreAlpa.setStatus("mandatory")
_T300AttachObjs_ObjectIdentity = ObjectIdentity
t300AttachObjs = _T300AttachObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 6)
)
_AttachCount_Type = Integer32
_AttachCount_Object = MibScalar
attachCount = _AttachCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 6, 1),
    _AttachCount_Type()
)
attachCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attachCount.setStatus("mandatory")
_AttachTable_Object = MibTable
attachTable = _AttachTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 6, 2)
)
if mibBuilder.loadTexts:
    attachTable.setStatus("mandatory")
_AttachEntry_Object = MibTableRow
attachEntry = _AttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 6, 2, 1)
)
attachEntry.setIndexNames(
    (0, "SUN-T300-MIB", "unitIndex"),
    (0, "SUN-T300-MIB", "portIndex"),
    (0, "SUN-T300-MIB", "attachIndex"),
)
if mibBuilder.loadTexts:
    attachEntry.setStatus("mandatory")
_AttachIndex_Type = Integer32
_AttachIndex_Object = MibTableColumn
attachIndex = _AttachIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 6, 2, 1, 1),
    _AttachIndex_Type()
)
attachIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attachIndex.setStatus("mandatory")
_AttachLun_Type = Integer32
_AttachLun_Object = MibTableColumn
attachLun = _AttachLun_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 6, 2, 1, 2),
    _AttachLun_Type()
)
attachLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attachLun.setStatus("mandatory")


class _AttachMode_Type(Integer32):
    """Custom type attachMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failover", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_AttachMode_Type.__name__ = "Integer32"
_AttachMode_Object = MibTableColumn
attachMode = _AttachMode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 6, 2, 1, 3),
    _AttachMode_Type()
)
attachMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attachMode.setStatus("mandatory")


class _AttachVolId_Type(DisplayString):
    """Custom type attachVolId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AttachVolId_Type.__name__ = "DisplayString"
_AttachVolId_Object = MibTableColumn
attachVolId = _AttachVolId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 6, 2, 1, 4),
    _AttachVolId_Type()
)
attachVolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attachVolId.setStatus("mandatory")


class _AttachVolName_Type(DisplayString):
    """Custom type attachVolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AttachVolName_Type.__name__ = "DisplayString"
_AttachVolName_Object = MibTableColumn
attachVolName = _AttachVolName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 6, 2, 1, 5),
    _AttachVolName_Type()
)
attachVolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attachVolName.setStatus("mandatory")


class _AttachVolOwner_Type(DisplayString):
    """Custom type attachVolOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AttachVolOwner_Type.__name__ = "DisplayString"
_AttachVolOwner_Object = MibTableColumn
attachVolOwner = _AttachVolOwner_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 6, 2, 1, 6),
    _AttachVolOwner_Type()
)
attachVolOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attachVolOwner.setStatus("mandatory")
_T300LoopObjs_ObjectIdentity = ObjectIdentity
t300LoopObjs = _T300LoopObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 7)
)
_LoopCount_Type = Integer32
_LoopCount_Object = MibScalar
loopCount = _LoopCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 7, 1),
    _LoopCount_Type()
)
loopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopCount.setStatus("mandatory")
_LoopTable_Object = MibTable
loopTable = _LoopTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 7, 2)
)
if mibBuilder.loadTexts:
    loopTable.setStatus("mandatory")
_LoopEntry_Object = MibTableRow
loopEntry = _LoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 7, 2, 1)
)
loopEntry.setIndexNames(
    (0, "SUN-T300-MIB", "unitIndex"),
    (0, "SUN-T300-MIB", "loopIndex"),
)
if mibBuilder.loadTexts:
    loopEntry.setStatus("mandatory")
_LoopIndex_Type = Integer32
_LoopIndex_Object = MibTableColumn
loopIndex = _LoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 7, 2, 1, 1),
    _LoopIndex_Type()
)
loopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopIndex.setStatus("mandatory")


class _LoopId_Type(DisplayString):
    """Custom type loopId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LoopId_Type.__name__ = "DisplayString"
_LoopId_Object = MibTableColumn
loopId = _LoopId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 7, 2, 1, 2),
    _LoopId_Type()
)
loopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopId.setStatus("mandatory")


class _LoopStatus_Type(Integer32):
    """Custom type loopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("reserved", 2))
    )


_LoopStatus_Type.__name__ = "Integer32"
_LoopStatus_Object = MibTableColumn
loopStatus = _LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 7, 2, 1, 3),
    _LoopStatus_Type()
)
loopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopStatus.setStatus("mandatory")


class _LoopMux_Type(Integer32):
    """Custom type loopMux based on Integer32"""
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
        *(("bottom", 3),
          ("isolated", 1),
          ("middle", 4),
          ("top", 2))
    )


_LoopMux_Type.__name__ = "Integer32"
_LoopMux_Object = MibTableColumn
loopMux = _LoopMux_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 7, 2, 1, 4),
    _LoopMux_Type()
)
loopMux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopMux.setStatus("mandatory")
_T300LogObjs_ObjectIdentity = ObjectIdentity
t300LogObjs = _T300LogObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 8)
)


class _LogStatus_Type(Integer32):
    """Custom type logStatus based on Integer32"""
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


_LogStatus_Type.__name__ = "Integer32"
_LogStatus_Object = MibScalar
logStatus = _LogStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 8, 1),
    _LogStatus_Type()
)
logStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logStatus.setStatus("mandatory")


class _LogTo_Type(DisplayString):
    """Custom type logTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LogTo_Type.__name__ = "DisplayString"
_LogTo_Object = MibScalar
logTo = _LogTo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 8, 2),
    _LogTo_Type()
)
logTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTo.setStatus("mandatory")


class _LogFile_Type(DisplayString):
    """Custom type logFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LogFile_Type.__name__ = "DisplayString"
_LogFile_Object = MibScalar
logFile = _LogFile_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 8, 3),
    _LogFile_Type()
)
logFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFile.setStatus("mandatory")


class _LogLevel_Type(Integer32):
    """Custom type logLevel based on Integer32"""
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
        *(("all-4", 5),
          ("error-1", 2),
          ("none-0", 1),
          ("notice-3", 4),
          ("warning-2", 3))
    )


_LogLevel_Type.__name__ = "Integer32"
_LogLevel_Object = MibScalar
logLevel = _LogLevel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 8, 4),
    _LogLevel_Type()
)
logLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logLevel.setStatus("mandatory")
_LogPort_Type = Integer32
_LogPort_Object = MibScalar
logPort = _LogPort_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 8, 5),
    _LogPort_Type()
)
logPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logPort.setStatus("mandatory")
_T300OndgObjs_ObjectIdentity = ObjectIdentity
t300OndgObjs = _T300OndgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 9)
)


class _OndgOper_Type(Integer32):
    """Custom type ondgOper based on Integer32"""
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
        *(("fastFind", 4),
          ("fastTest", 2),
          ("find", 3),
          ("healthCheck", 5),
          ("test", 1))
    )


_OndgOper_Type.__name__ = "Integer32"
_OndgOper_Object = MibScalar
ondgOper = _OndgOper_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 9, 1),
    _OndgOper_Type()
)
ondgOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ondgOper.setStatus("mandatory")


class _OndgOperPending_Type(Integer32):
    """Custom type ondgOperPending based on Integer32"""
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


_OndgOperPending_Type.__name__ = "Integer32"
_OndgOperPending_Object = MibScalar
ondgOperPending = _OndgOperPending_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 9, 2),
    _OndgOperPending_Type()
)
ondgOperPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ondgOperPending.setStatus("mandatory")
_OndgOperProgress_Type = Integer32
_OndgOperProgress_Object = MibScalar
ondgOperProgress = _OndgOperProgress_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 9, 3),
    _OndgOperProgress_Type()
)
ondgOperProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ondgOperProgress.setStatus("mandatory")


class _OndgError_Type(DisplayString):
    """Custom type ondgError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_OndgError_Type.__name__ = "DisplayString"
_OndgError_Object = MibScalar
ondgError = _OndgError_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 9, 4),
    _OndgError_Type()
)
ondgError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ondgError.setStatus("mandatory")
_OndgId_Type = Integer32
_OndgId_Object = MibScalar
ondgId = _OndgId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 2, 9, 5),
    _OndgId_Type()
)
ondgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ondgId.setStatus("mandatory")
_T300Events_ObjectIdentity = ObjectIdentity
t300Events = _T300Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 3)
)
_T300EventsV2_ObjectIdentity = ObjectIdentity
t300EventsV2 = _T300EventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 3, 0)
)

# Managed Objects groups


# Notification objects

sysMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 28, 2, 3, 0, 1)
)
sysMessage.setObjects(
    ("SUN-T300-MIB", "sysLastMessage")
)
if mibBuilder.loadTexts:
    sysMessage.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUN-T300-MIB",
    **{"sun": sun,
       "products": products,
       "storage-subsystem": storage_subsystem,
       "t300": t300,
       "t300Reg": t300Reg,
       "t300Purple1": t300Purple1,
       "t300Objs": t300Objs,
       "t300SystemObjs": t300SystemObjs,
       "sysId": sysId,
       "sysVendor": sysVendor,
       "sysModel": sysModel,
       "sysRevision": sysRevision,
       "sysStripeUnitSize": sysStripeUnitSize,
       "sysCacheMode": sysCacheMode,
       "sysCacheMirror": sysCacheMirror,
       "sysAutoDisable": sysAutoDisable,
       "sysMpSupport": sysMpSupport,
       "sysReadAhead": sysReadAhead,
       "sysReconRate": sysReconRate,
       "sysOndgMode": sysOndgMode,
       "sysOndgTimeslice": sysOndgTimeslice,
       "sysIdleDiskTimeout": sysIdleDiskTimeout,
       "sysFruRemovalShutdown": sysFruRemovalShutdown,
       "sysBootMode": sysBootMode,
       "sysBootDelay": sysBootDelay,
       "sysSpinDelay": sysSpinDelay,
       "sysTftpHost": sysTftpHost,
       "sysTftpFile": sysTftpFile,
       "sysIpAddr": sysIpAddr,
       "sysSubNet": sysSubNet,
       "sysGateway": sysGateway,
       "sysWriteRequests": sysWriteRequests,
       "sysReadRequests": sysReadRequests,
       "sysBlocksWritten": sysBlocksWritten,
       "sysBlocksRead": sysBlocksRead,
       "sysCacheWriteHits": sysCacheWriteHits,
       "sysCacheWriteMisses": sysCacheWriteMisses,
       "sysCacheReadHits": sysCacheReadHits,
       "sysCacheReadMisses": sysCacheReadMisses,
       "sysCacheRmwFlushes": sysCacheRmwFlushes,
       "sysCacheReconFlushes": sysCacheReconFlushes,
       "sysCacheStripeFlushes": sysCacheStripeFlushes,
       "sysTimezone": sysTimezone,
       "sysDate": sysDate,
       "sysTime": sysTime,
       "sysRootSession": sysRootSession,
       "sysGuestSession": sysGuestSession,
       "sysLastMessage": sysLastMessage,
       "sysRarpEnabled": sysRarpEnabled,
       "sysLoop1Split": sysLoop1Split,
       "sysLastRestart": sysLastRestart,
       "sysCtime": sysCtime,
       "sysHasVolumes": sysHasVolumes,
       "t300UnitObjs": t300UnitObjs,
       "unitCount": unitCount,
       "unitTable": unitTable,
       "unitEntry": unitEntry,
       "unitIndex": unitIndex,
       "unitId": unitId,
       "unitType": unitType,
       "unitStandby": unitStandby,
       "t300FruObjs": t300FruObjs,
       "fruCount": fruCount,
       "fruTable": fruTable,
       "fruEntry": fruEntry,
       "fruIndex": fruIndex,
       "fruId": fruId,
       "fruType": fruType,
       "fruStatus": fruStatus,
       "fruState": fruState,
       "fruVendor": fruVendor,
       "fruModel": fruModel,
       "fruRevision": fruRevision,
       "fruSerialNo": fruSerialNo,
       "fruErrors": fruErrors,
       "fruDiskCount": fruDiskCount,
       "fruDiskTable": fruDiskTable,
       "fruDiskEntry": fruDiskEntry,
       "fruDiskRole": fruDiskRole,
       "fruDiskPort1State": fruDiskPort1State,
       "fruDiskPort2State": fruDiskPort2State,
       "fruDiskCapacity": fruDiskCapacity,
       "fruDiskStatusCode": fruDiskStatusCode,
       "fruDiskVolName": fruDiskVolName,
       "fruDiskTemp": fruDiskTemp,
       "fruCtlrCount": fruCtlrCount,
       "fruCtlrTable": fruCtlrTable,
       "fruCtlrEntry": fruCtlrEntry,
       "fruCtlrCpuDesc": fruCtlrCpuDesc,
       "fruCtlrRole": fruCtlrRole,
       "fruCtlrPartnerId": fruCtlrPartnerId,
       "fruCtlrCtState": fruCtlrCtState,
       "fruCtlrCacheSize": fruCtlrCacheSize,
       "fruCtlrTemp": fruCtlrTemp,
       "fruCtlrMdate": fruCtlrMdate,
       "fruCtlrConsoleBaud": fruCtlrConsoleBaud,
       "fruLoopCount": fruLoopCount,
       "fruLoopTable": fruLoopTable,
       "fruLoopEntry": fruLoopEntry,
       "fruLoopMode": fruLoopMode,
       "fruLoopTemp": fruLoopTemp,
       "fruLoopCable1State": fruLoopCable1State,
       "fruLoopCable2State": fruLoopCable2State,
       "fruLoopMdate": fruLoopMdate,
       "fruPowerCount": fruPowerCount,
       "fruPowerTable": fruPowerTable,
       "fruPowerEntry": fruPowerEntry,
       "fruPowerPowOutput": fruPowerPowOutput,
       "fruPowerPowSource": fruPowerPowSource,
       "fruPowerPowTemp": fruPowerPowTemp,
       "fruPowerFan1State": fruPowerFan1State,
       "fruPowerFan2State": fruPowerFan2State,
       "fruPowerBatState": fruPowerBatState,
       "fruPowerBatLife": fruPowerBatLife,
       "fruPowerBatUsed": fruPowerBatUsed,
       "fruPowerPowMdate": fruPowerPowMdate,
       "fruPowerBatMdate": fruPowerBatMdate,
       "fruMidplaneCount": fruMidplaneCount,
       "fruMidplaneTable": fruMidplaneTable,
       "fruMidplaneEntry": fruMidplaneEntry,
       "fruMidplaneMdate": fruMidplaneMdate,
       "t300VolumeObjs": t300VolumeObjs,
       "volCount": volCount,
       "volTable": volTable,
       "volEntry": volEntry,
       "volIndex": volIndex,
       "volId": volId,
       "volName": volName,
       "volWWN": volWWN,
       "volStatus": volStatus,
       "volCacheMode": volCacheMode,
       "volCacheMirror": volCacheMirror,
       "volCapacity": volCapacity,
       "volArrayWidth": volArrayWidth,
       "volRaidLevel": volRaidLevel,
       "volWriteRequests": volWriteRequests,
       "volReadRequests": volReadRequests,
       "volBlocksWritten": volBlocksWritten,
       "volBlocksRead": volBlocksRead,
       "volSoftErrors": volSoftErrors,
       "volFirmErrors": volFirmErrors,
       "volHardErrors": volHardErrors,
       "volCacheWriteHits": volCacheWriteHits,
       "volCacheWriteMisses": volCacheWriteMisses,
       "volCacheReadHits": volCacheReadHits,
       "volCacheReadMisses": volCacheReadMisses,
       "volCacheRmwFlushes": volCacheRmwFlushes,
       "volCacheReconFlushes": volCacheReconFlushes,
       "volCacheStripeFlushes": volCacheStripeFlushes,
       "volDisabledDisk": volDisabledDisk,
       "volSubstitutedDisk": volSubstitutedDisk,
       "volOper": volOper,
       "volOperProgress": volOperProgress,
       "volInitRate": volInitRate,
       "volVerifyRate": volVerifyRate,
       "t300PortObjs": t300PortObjs,
       "portCount": portCount,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portId": portId,
       "portType": portType,
       "portFruId": portFruId,
       "portWriteRequests": portWriteRequests,
       "portReadRequests": portReadRequests,
       "portBlocksWritten": portBlocksWritten,
       "portBlocksRead": portBlocksRead,
       "portSunHost": portSunHost,
       "portWWN": portWWN,
       "portStatus": portStatus,
       "portErrors": portErrors,
       "portFibreCount": portFibreCount,
       "portFibreTable": portFibreTable,
       "portFibreEntry": portFibreEntry,
       "portFibreAlpaMode": portFibreAlpaMode,
       "portFibreAlpa": portFibreAlpa,
       "t300AttachObjs": t300AttachObjs,
       "attachCount": attachCount,
       "attachTable": attachTable,
       "attachEntry": attachEntry,
       "attachIndex": attachIndex,
       "attachLun": attachLun,
       "attachMode": attachMode,
       "attachVolId": attachVolId,
       "attachVolName": attachVolName,
       "attachVolOwner": attachVolOwner,
       "t300LoopObjs": t300LoopObjs,
       "loopCount": loopCount,
       "loopTable": loopTable,
       "loopEntry": loopEntry,
       "loopIndex": loopIndex,
       "loopId": loopId,
       "loopStatus": loopStatus,
       "loopMux": loopMux,
       "t300LogObjs": t300LogObjs,
       "logStatus": logStatus,
       "logTo": logTo,
       "logFile": logFile,
       "logLevel": logLevel,
       "logPort": logPort,
       "t300OndgObjs": t300OndgObjs,
       "ondgOper": ondgOper,
       "ondgOperPending": ondgOperPending,
       "ondgOperProgress": ondgOperProgress,
       "ondgError": ondgError,
       "ondgId": ondgId,
       "t300Events": t300Events,
       "t300EventsV2": t300EventsV2,
       "sysMessage": sysMessage}
)
