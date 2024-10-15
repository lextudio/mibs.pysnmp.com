# SNMP MIB module (CTRON-DOWNLOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-DOWNLOAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:45 2024
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

(ctDownLoad,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctDownLoad")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtDL_ObjectIdentity = ObjectIdentity
ctDL = _CtDL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1)
)
_CtDLForceOnBoot_Type = Integer32
_CtDLForceOnBoot_Object = MibScalar
ctDLForceOnBoot = _CtDLForceOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 1),
    _CtDLForceOnBoot_Type()
)
ctDLForceOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDLForceOnBoot.setStatus("obsolete")
_CtDLCommitRAMToFlash_Type = Integer32
_CtDLCommitRAMToFlash_Object = MibScalar
ctDLCommitRAMToFlash = _CtDLCommitRAMToFlash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 2),
    _CtDLCommitRAMToFlash_Type()
)
ctDLCommitRAMToFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDLCommitRAMToFlash.setStatus("obsolete")
_CtDLInitiateColdBoot_Type = Integer32
_CtDLInitiateColdBoot_Object = MibScalar
ctDLInitiateColdBoot = _CtDLInitiateColdBoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 3),
    _CtDLInitiateColdBoot_Type()
)
ctDLInitiateColdBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDLInitiateColdBoot.setStatus("mandatory")
_CtDLTFTPRequestHost_Type = IpAddress
_CtDLTFTPRequestHost_Object = MibScalar
ctDLTFTPRequestHost = _CtDLTFTPRequestHost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 4),
    _CtDLTFTPRequestHost_Type()
)
ctDLTFTPRequestHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDLTFTPRequestHost.setStatus("obsolete")
_CtDLTFTPRequest_Type = DisplayString
_CtDLTFTPRequest_Object = MibScalar
ctDLTFTPRequest = _CtDLTFTPRequest_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 5),
    _CtDLTFTPRequest_Type()
)
ctDLTFTPRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDLTFTPRequest.setStatus("obsolete")
_CtDLLastImageFilename_Type = DisplayString
_CtDLLastImageFilename_Object = MibScalar
ctDLLastImageFilename = _CtDLLastImageFilename_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 6),
    _CtDLLastImageFilename_Type()
)
ctDLLastImageFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDLLastImageFilename.setStatus("mandatory")
_CtDLLastServerIPAddress_Type = IpAddress
_CtDLLastServerIPAddress_Object = MibScalar
ctDLLastServerIPAddress = _CtDLLastServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 7),
    _CtDLLastServerIPAddress_Type()
)
ctDLLastServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDLLastServerIPAddress.setStatus("mandatory")
_CtDLFlashSize_Type = Integer32
_CtDLFlashSize_Object = MibScalar
ctDLFlashSize = _CtDLFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 8),
    _CtDLFlashSize_Type()
)
ctDLFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDLFlashSize.setStatus("obsolete")
_CtDLFlashCount_Type = Integer32
_CtDLFlashCount_Object = MibScalar
ctDLFlashCount = _CtDLFlashCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 9),
    _CtDLFlashCount_Type()
)
ctDLFlashCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDLFlashCount.setStatus("obsolete")
_CtDLFirmwareBase_Type = Integer32
_CtDLFirmwareBase_Object = MibScalar
ctDLFirmwareBase = _CtDLFirmwareBase_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 10),
    _CtDLFirmwareBase_Type()
)
ctDLFirmwareBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDLFirmwareBase.setStatus("obsolete")
_CtDLFirmwareTop_Type = Integer32
_CtDLFirmwareTop_Object = MibScalar
ctDLFirmwareTop = _CtDLFirmwareTop_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 11),
    _CtDLFirmwareTop_Type()
)
ctDLFirmwareTop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDLFirmwareTop.setStatus("obsolete")
_CtDLFirmwareStart_Type = Integer32
_CtDLFirmwareStart_Object = MibScalar
ctDLFirmwareStart = _CtDLFirmwareStart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 12),
    _CtDLFirmwareStart_Type()
)
ctDLFirmwareStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDLFirmwareStart.setStatus("obsolete")


class _CtDLBootRev_Type(OctetString):
    """Custom type ctDLBootRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_CtDLBootRev_Type.__name__ = "OctetString"
_CtDLBootRev_Object = MibScalar
ctDLBootRev = _CtDLBootRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 13),
    _CtDLBootRev_Type()
)
ctDLBootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDLBootRev.setStatus("obsolete")
_CtDLForceBootp_Type = Integer32
_CtDLForceBootp_Object = MibScalar
ctDLForceBootp = _CtDLForceBootp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 14),
    _CtDLForceBootp_Type()
)
ctDLForceBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDLForceBootp.setStatus("obsolete")
_CtDLServerName_Type = OctetString
_CtDLServerName_Object = MibScalar
ctDLServerName = _CtDLServerName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 15),
    _CtDLServerName_Type()
)
ctDLServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDLServerName.setStatus("obsolete")


class _CtDLOnLineDownLoad_Type(Integer32):
    """Custom type ctDLOnLineDownLoad based on Integer32"""
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
        *(("downLoadConfiguration", 4),
          ("forceDownLoad", 2),
          ("forceDownLoadReset", 3),
          ("normalOperation", 1),
          ("upLoadConfiguration", 5))
    )


_CtDLOnLineDownLoad_Type.__name__ = "Integer32"
_CtDLOnLineDownLoad_Object = MibScalar
ctDLOnLineDownLoad = _CtDLOnLineDownLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 16),
    _CtDLOnLineDownLoad_Type()
)
ctDLOnLineDownLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDLOnLineDownLoad.setStatus("mandatory")


class _CtDLOperStatus_Type(Integer32):
    """Custom type ctDLOperStatus based on Integer32"""
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
        *(("downLoadActive", 4),
          ("downLoadCompleteError", 5),
          ("normalOperation", 3),
          ("other", 1),
          ("unknown", 2))
    )


_CtDLOperStatus_Type.__name__ = "Integer32"
_CtDLOperStatus_Object = MibScalar
ctDLOperStatus = _CtDLOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 17),
    _CtDLOperStatus_Type()
)
ctDLOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDLOperStatus.setStatus("mandatory")
_CtDLNetAddress_Type = IpAddress
_CtDLNetAddress_Object = MibScalar
ctDLNetAddress = _CtDLNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 18),
    _CtDLNetAddress_Type()
)
ctDLNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDLNetAddress.setStatus("mandatory")


class _CtDLFileName_Type(DisplayString):
    """Custom type ctDLFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CtDLFileName_Type.__name__ = "DisplayString"
_CtDLFileName_Object = MibScalar
ctDLFileName = _CtDLFileName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 19),
    _CtDLFileName_Type()
)
ctDLFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDLFileName.setStatus("mandatory")
_CtDLErrorString_Type = DisplayString
_CtDLErrorString_Object = MibScalar
ctDLErrorString = _CtDLErrorString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 20),
    _CtDLErrorString_Type()
)
ctDLErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDLErrorString.setStatus("mandatory")
_CtDLTftpServerGatewayIPAddress_Type = IpAddress
_CtDLTftpServerGatewayIPAddress_Object = MibScalar
ctDLTftpServerGatewayIPAddress = _CtDLTftpServerGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 21),
    _CtDLTftpServerGatewayIPAddress_Type()
)
ctDLTftpServerGatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDLTftpServerGatewayIPAddress.setStatus("obsolete")
_CtDLBlockCount_Type = Integer32
_CtDLBlockCount_Object = MibScalar
ctDLBlockCount = _CtDLBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 22),
    _CtDLBlockCount_Type()
)
ctDLBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDLBlockCount.setStatus("mandatory")


class _CtDLBootPartitionStatus_Type(Integer32):
    """Custom type ctDLBootPartitionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1),
          ("inProgress", 3))
    )


_CtDLBootPartitionStatus_Type.__name__ = "Integer32"
_CtDLBootPartitionStatus_Object = MibScalar
ctDLBootPartitionStatus = _CtDLBootPartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 23),
    _CtDLBootPartitionStatus_Type()
)
ctDLBootPartitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDLBootPartitionStatus.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-DOWNLOAD-MIB",
    **{"ctDL": ctDL,
       "ctDLForceOnBoot": ctDLForceOnBoot,
       "ctDLCommitRAMToFlash": ctDLCommitRAMToFlash,
       "ctDLInitiateColdBoot": ctDLInitiateColdBoot,
       "ctDLTFTPRequestHost": ctDLTFTPRequestHost,
       "ctDLTFTPRequest": ctDLTFTPRequest,
       "ctDLLastImageFilename": ctDLLastImageFilename,
       "ctDLLastServerIPAddress": ctDLLastServerIPAddress,
       "ctDLFlashSize": ctDLFlashSize,
       "ctDLFlashCount": ctDLFlashCount,
       "ctDLFirmwareBase": ctDLFirmwareBase,
       "ctDLFirmwareTop": ctDLFirmwareTop,
       "ctDLFirmwareStart": ctDLFirmwareStart,
       "ctDLBootRev": ctDLBootRev,
       "ctDLForceBootp": ctDLForceBootp,
       "ctDLServerName": ctDLServerName,
       "ctDLOnLineDownLoad": ctDLOnLineDownLoad,
       "ctDLOperStatus": ctDLOperStatus,
       "ctDLNetAddress": ctDLNetAddress,
       "ctDLFileName": ctDLFileName,
       "ctDLErrorString": ctDLErrorString,
       "ctDLTftpServerGatewayIPAddress": ctDLTftpServerGatewayIPAddress,
       "ctDLBlockCount": ctDLBlockCount,
       "ctDLBootPartitionStatus": ctDLBootPartitionStatus}
)
