# SNMP MIB module (SONOMASYSTEMS-SONOMA-IPAPPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-IPAPPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:45 2024
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

(sonomaApplications,) = mibBuilder.importSymbols(
    "SONOMASYSTEMS-SONOMA-MIB",
    "sonomaApplications")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpApplications_ObjectIdentity = ObjectIdentity
ipApplications = _IpApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1)
)
_BootpGroup_ObjectIdentity = ObjectIdentity
bootpGroup = _BootpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1)
)
_TftpFileServerIpAddress_Type = IpAddress
_TftpFileServerIpAddress_Object = MibScalar
tftpFileServerIpAddress = _TftpFileServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 1),
    _TftpFileServerIpAddress_Type()
)
tftpFileServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFileServerIpAddress.setStatus("mandatory")


class _TftpFileName_Type(DisplayString):
    """Custom type tftpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TftpFileName_Type.__name__ = "DisplayString"
_TftpFileName_Object = MibScalar
tftpFileName = _TftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 2),
    _TftpFileName_Type()
)
tftpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFileName.setStatus("mandatory")


class _TftpImageNumber_Type(Integer32):
    """Custom type tftpImageNumber based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2),
          ("image3", 3),
          ("image4", 4),
          ("image5", 5),
          ("image6", 6),
          ("image7", 7),
          ("image8", 8))
    )


_TftpImageNumber_Type.__name__ = "Integer32"
_TftpImageNumber_Object = MibScalar
tftpImageNumber = _TftpImageNumber_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 3),
    _TftpImageNumber_Type()
)
tftpImageNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpImageNumber.setStatus("mandatory")


class _TftpFileAction_Type(Integer32):
    """Custom type tftpFileAction based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("startBootPImageDownload", 2),
          ("startPrimaryImageTFTPDownload", 4),
          ("startSecondaryImageTFTPDownload", 5),
          ("startTFTPImageDownload", 3),
          ("startTFTPParameterBinDownload", 6),
          ("startTFTPParameterBinUpload", 8),
          ("startTFTPParameterTextDownload", 7),
          ("startTFTPParameterTextUpload", 9),
          ("startTFTPProfileDownload", 10))
    )


_TftpFileAction_Type.__name__ = "Integer32"
_TftpFileAction_Object = MibScalar
tftpFileAction = _TftpFileAction_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 4),
    _TftpFileAction_Type()
)
tftpFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFileAction.setStatus("mandatory")


class _TftpFileTransferStatus_Type(Integer32):
    """Custom type tftpFileTransferStatus based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("downloadSuccessful", 15),
          ("downloading", 2),
          ("errorServerData", 12),
          ("errorServerResponse", 7),
          ("failBootpNoServer", 5),
          ("failCannotOverwriteActiveImage", 17),
          ("failCannotOverwriteActiveParam", 18),
          ("failFlashChksumError", 11),
          ("failFlashProgError", 10),
          ("failNetworkTimeout", 9),
          ("failTFTPInvalidFile", 8),
          ("failTFTPNoFile", 6),
          ("generalFailure", 16),
          ("idle", 1),
          ("programmingflash", 4),
          ("uploadResultUnknown", 13),
          ("uploadSuccessful", 14),
          ("uploading", 3))
    )


_TftpFileTransferStatus_Type.__name__ = "Integer32"
_TftpFileTransferStatus_Object = MibScalar
tftpFileTransferStatus = _TftpFileTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 5),
    _TftpFileTransferStatus_Type()
)
tftpFileTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpFileTransferStatus.setStatus("mandatory")
_PingGroup_ObjectIdentity = ObjectIdentity
pingGroup = _PingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2)
)
_PingIpAddress_Type = IpAddress
_PingIpAddress_Object = MibScalar
pingIpAddress = _PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 1),
    _PingIpAddress_Type()
)
pingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingIpAddress.setStatus("mandatory")


class _PingTimeout_Type(Integer32):
    """Custom type pingTimeout based on Integer32"""
    defaultValue = 0


_PingTimeout_Object = MibScalar
pingTimeout = _PingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 2),
    _PingTimeout_Type()
)
pingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTimeout.setStatus("mandatory")


class _PingRetries_Type(Integer32):
    """Custom type pingRetries based on Integer32"""
    defaultValue = 1


_PingRetries_Object = MibScalar
pingRetries = _PingRetries_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 3),
    _PingRetries_Type()
)
pingRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingRetries.setStatus("mandatory")


class _PingStatus_Type(DisplayString):
    """Custom type pingStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PingStatus_Type.__name__ = "DisplayString"
_PingStatus_Object = MibScalar
pingStatus = _PingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 4),
    _PingStatus_Type()
)
pingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingStatus.setStatus("mandatory")


class _PingAction_Type(Integer32):
    """Custom type pingAction based on Integer32"""
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
        *(("noAction", 3),
          ("start", 1),
          ("stop", 2))
    )


_PingAction_Type.__name__ = "Integer32"
_PingAction_Object = MibScalar
pingAction = _PingAction_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 5),
    _PingAction_Type()
)
pingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingAction.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-IPAPPS-MIB",
    **{"DisplayString": DisplayString,
       "ipApplications": ipApplications,
       "bootpGroup": bootpGroup,
       "tftpFileServerIpAddress": tftpFileServerIpAddress,
       "tftpFileName": tftpFileName,
       "tftpImageNumber": tftpImageNumber,
       "tftpFileAction": tftpFileAction,
       "tftpFileTransferStatus": tftpFileTransferStatus,
       "pingGroup": pingGroup,
       "pingIpAddress": pingIpAddress,
       "pingTimeout": pingTimeout,
       "pingRetries": pingRetries,
       "pingStatus": pingStatus,
       "pingAction": pingAction}
)
