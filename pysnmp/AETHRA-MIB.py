# SNMP MIB module (AETHRA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AETHRA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:52 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aethra_ObjectIdentity = ObjectIdentity
aethra = _Aethra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745)
)
_Atosnt_ObjectIdentity = ObjectIdentity
atosnt = _Atosnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5)
)
_Tools_ObjectIdentity = ObjectIdentity
tools = _Tools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1)
)
_FileTransfer_ObjectIdentity = ObjectIdentity
fileTransfer = _FileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 1)
)


class _FileTransferProtocol_Type(Integer32):
    """Custom type fileTransferProtocol based on Integer32"""
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
        *(("file", 4),
          ("ftp", 2),
          ("http", 3),
          ("scp", 5),
          ("tftp", 1))
    )


_FileTransferProtocol_Type.__name__ = "Integer32"
_FileTransferProtocol_Object = MibScalar
fileTransferProtocol = _FileTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 1, 1),
    _FileTransferProtocol_Type()
)
fileTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferProtocol.setStatus("mandatory")
_FileTransferFileName_Type = DisplayString
_FileTransferFileName_Object = MibScalar
fileTransferFileName = _FileTransferFileName_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 1, 2),
    _FileTransferFileName_Type()
)
fileTransferFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferFileName.setStatus("mandatory")
_FileTransferServerName_Type = DisplayString
_FileTransferServerName_Object = MibScalar
fileTransferServerName = _FileTransferServerName_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 1, 3),
    _FileTransferServerName_Type()
)
fileTransferServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferServerName.setStatus("mandatory")


class _FileTransferOption_Type(Integer32):
    """Custom type fileTransferOption based on Integer32"""
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
        *(("bannerPost", 12),
          ("bannerPre", 11),
          ("boot", 2),
          ("certificate", 9),
          ("defaultconf", 10),
          ("firmware", 1),
          ("license", 8),
          ("localfile", 6),
          ("logs", 4),
          ("package", 5),
          ("userconf", 3),
          ("welcome", 7))
    )


_FileTransferOption_Type.__name__ = "Integer32"
_FileTransferOption_Object = MibScalar
fileTransferOption = _FileTransferOption_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 1, 4),
    _FileTransferOption_Type()
)
fileTransferOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferOption.setStatus("mandatory")
_FileTransferStorageFileName_Type = DisplayString
_FileTransferStorageFileName_Object = MibScalar
fileTransferStorageFileName = _FileTransferStorageFileName_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 1, 5),
    _FileTransferStorageFileName_Type()
)
fileTransferStorageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferStorageFileName.setStatus("mandatory")


class _FileTransferExec_Type(Integer32):
    """Custom type fileTransferExec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("noaction", 0),
          ("upload", 2))
    )


_FileTransferExec_Type.__name__ = "Integer32"
_FileTransferExec_Object = MibScalar
fileTransferExec = _FileTransferExec_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 1, 6),
    _FileTransferExec_Type()
)
fileTransferExec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferExec.setStatus("mandatory")
_FileTransferStatus_Type = DisplayString
_FileTransferStatus_Object = MibScalar
fileTransferStatus = _FileTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 1, 7),
    _FileTransferStatus_Type()
)
fileTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileTransferStatus.setStatus("mandatory")
_Ping_ObjectIdentity = ObjectIdentity
ping = _Ping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2)
)
_PingParameters_ObjectIdentity = ObjectIdentity
pingParameters = _PingParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 1)
)
_PingHost_Type = DisplayString
_PingHost_Object = MibScalar
pingHost = _PingHost_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 1, 1),
    _PingHost_Type()
)
pingHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingHost.setStatus("mandatory")


class _PingSize_Type(Integer32):
    """Custom type pingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_PingSize_Type.__name__ = "Integer32"
_PingSize_Object = MibScalar
pingSize = _PingSize_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 1, 2),
    _PingSize_Type()
)
pingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingSize.setStatus("mandatory")


class _PingTries_Type(Integer32):
    """Custom type pingTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PingTries_Type.__name__ = "Integer32"
_PingTries_Object = MibScalar
pingTries = _PingTries_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 1, 3),
    _PingTries_Type()
)
pingTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTries.setStatus("mandatory")


class _PingTTL_Type(Integer32):
    """Custom type pingTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PingTTL_Type.__name__ = "Integer32"
_PingTTL_Object = MibScalar
pingTTL = _PingTTL_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 1, 4),
    _PingTTL_Type()
)
pingTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTTL.setStatus("mandatory")


class _PingTimeOut_Type(Integer32):
    """Custom type pingTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PingTimeOut_Type.__name__ = "Integer32"
_PingTimeOut_Object = MibScalar
pingTimeOut = _PingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 1, 5),
    _PingTimeOut_Type()
)
pingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTimeOut.setStatus("mandatory")
_PingSource_Type = DisplayString
_PingSource_Object = MibScalar
pingSource = _PingSource_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 1, 6),
    _PingSource_Type()
)
pingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingSource.setStatus("mandatory")


class _PingStart_Type(Integer32):
    """Custom type pingStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 0),
          ("start", 1))
    )


_PingStart_Type.__name__ = "Integer32"
_PingStart_Object = MibScalar
pingStart = _PingStart_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 1, 7),
    _PingStart_Type()
)
pingStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingStart.setStatus("mandatory")
_PingStatus_Type = DisplayString
_PingStatus_Object = MibScalar
pingStatus = _PingStatus_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 1, 8),
    _PingStatus_Type()
)
pingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingStatus.setStatus("mandatory")
_PingStatistics_ObjectIdentity = ObjectIdentity
pingStatistics = _PingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 2)
)
_PingTXpacket_Type = Integer32
_PingTXpacket_Object = MibScalar
pingTXpacket = _PingTXpacket_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 2, 1),
    _PingTXpacket_Type()
)
pingTXpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingTXpacket.setStatus("mandatory")
_PingRXpacket_Type = Integer32
_PingRXpacket_Object = MibScalar
pingRXpacket = _PingRXpacket_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 2, 2),
    _PingRXpacket_Type()
)
pingRXpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingRXpacket.setStatus("mandatory")
_PingLOSTpacket_Type = Integer32
_PingLOSTpacket_Object = MibScalar
pingLOSTpacket = _PingLOSTpacket_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 2, 3),
    _PingLOSTpacket_Type()
)
pingLOSTpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingLOSTpacket.setStatus("mandatory")
_PingMinRTT_Type = Integer32
_PingMinRTT_Object = MibScalar
pingMinRTT = _PingMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 2, 4),
    _PingMinRTT_Type()
)
pingMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingMinRTT.setStatus("mandatory")
_PingMaxRTT_Type = Integer32
_PingMaxRTT_Object = MibScalar
pingMaxRTT = _PingMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 2, 5),
    _PingMaxRTT_Type()
)
pingMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingMaxRTT.setStatus("mandatory")
_PingAvgRTT_Type = Integer32
_PingAvgRTT_Object = MibScalar
pingAvgRTT = _PingAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 1, 2, 2, 6),
    _PingAvgRTT_Type()
)
pingAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingAvgRTT.setStatus("mandatory")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2)
)


class _SystemLoglevel_Type(Integer32):
    """Custom type systemLoglevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SystemLoglevel_Type.__name__ = "Integer32"
_SystemLoglevel_Object = MibScalar
systemLoglevel = _SystemLoglevel_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 1),
    _SystemLoglevel_Type()
)
systemLoglevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLoglevel.setStatus("mandatory")
_SystemDescription_Type = DisplayString
_SystemDescription_Object = MibScalar
systemDescription = _SystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 2),
    _SystemDescription_Type()
)
systemDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDescription.setStatus("mandatory")
_SystemName_Type = DisplayString
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 3),
    _SystemName_Type()
)
systemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemName.setStatus("mandatory")
_SystemLocalDomain_Type = DisplayString
_SystemLocalDomain_Object = MibScalar
systemLocalDomain = _SystemLocalDomain_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 4),
    _SystemLocalDomain_Type()
)
systemLocalDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocalDomain.setStatus("mandatory")
_SystemDefaultTftpServer_Type = DisplayString
_SystemDefaultTftpServer_Object = MibScalar
systemDefaultTftpServer = _SystemDefaultTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 5),
    _SystemDefaultTftpServer_Type()
)
systemDefaultTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDefaultTftpServer.setStatus("mandatory")
_SystemTftpLocalAdd_Type = IpAddress
_SystemTftpLocalAdd_Object = MibScalar
systemTftpLocalAdd = _SystemTftpLocalAdd_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 6),
    _SystemTftpLocalAdd_Type()
)
systemTftpLocalAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTftpLocalAdd.setStatus("mandatory")
_SystemDefaultFtpServer_Type = DisplayString
_SystemDefaultFtpServer_Object = MibScalar
systemDefaultFtpServer = _SystemDefaultFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 7),
    _SystemDefaultFtpServer_Type()
)
systemDefaultFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDefaultFtpServer.setStatus("mandatory")
_SystemFtpLocalAdd_Type = IpAddress
_SystemFtpLocalAdd_Object = MibScalar
systemFtpLocalAdd = _SystemFtpLocalAdd_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 8),
    _SystemFtpLocalAdd_Type()
)
systemFtpLocalAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFtpLocalAdd.setStatus("mandatory")
_SystemFtpUsername_Type = DisplayString
_SystemFtpUsername_Object = MibScalar
systemFtpUsername = _SystemFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 9),
    _SystemFtpUsername_Type()
)
systemFtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFtpUsername.setStatus("mandatory")
_SystemFtpPassword_Type = DisplayString
_SystemFtpPassword_Object = MibScalar
systemFtpPassword = _SystemFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 10),
    _SystemFtpPassword_Type()
)
systemFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFtpPassword.setStatus("mandatory")
_SystemAAAProfile_Type = DisplayString
_SystemAAAProfile_Object = MibScalar
systemAAAProfile = _SystemAAAProfile_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 11),
    _SystemAAAProfile_Type()
)
systemAAAProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAAAProfile.setStatus("mandatory")


class _SystemAAALogTimeout_Type(Integer32):
    """Custom type systemAAALogTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_SystemAAALogTimeout_Type.__name__ = "Integer32"
_SystemAAALogTimeout_Object = MibScalar
systemAAALogTimeout = _SystemAAALogTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 12),
    _SystemAAALogTimeout_Type()
)
systemAAALogTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAAALogTimeout.setStatus("mandatory")


class _SystemBackupAuth_Type(Integer32):
    """Custom type systemBackupAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SystemBackupAuth_Type.__name__ = "Integer32"
_SystemBackupAuth_Object = MibScalar
systemBackupAuth = _SystemBackupAuth_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 13),
    _SystemBackupAuth_Type()
)
systemBackupAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemBackupAuth.setStatus("mandatory")


class _SystemScrollLine_Type(Integer32):
    """Custom type systemScrollLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SystemScrollLine_Type.__name__ = "Integer32"
_SystemScrollLine_Object = MibScalar
systemScrollLine = _SystemScrollLine_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 14),
    _SystemScrollLine_Type()
)
systemScrollLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemScrollLine.setStatus("mandatory")


class _SystemKernelLogs_Type(Integer32):
    """Custom type systemKernelLogs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SystemKernelLogs_Type.__name__ = "Integer32"
_SystemKernelLogs_Object = MibScalar
systemKernelLogs = _SystemKernelLogs_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 15),
    _SystemKernelLogs_Type()
)
systemKernelLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemKernelLogs.setStatus("mandatory")


class _SystemCryptedPassword_Type(Integer32):
    """Custom type systemCryptedPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SystemCryptedPassword_Type.__name__ = "Integer32"
_SystemCryptedPassword_Object = MibScalar
systemCryptedPassword = _SystemCryptedPassword_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 16),
    _SystemCryptedPassword_Type()
)
systemCryptedPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemCryptedPassword.setStatus("mandatory")


class _SystemSave_Type(Integer32):
    """Custom type systemSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 0),
          ("save", 1))
    )


_SystemSave_Type.__name__ = "Integer32"
_SystemSave_Object = MibScalar
systemSave = _SystemSave_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 17),
    _SystemSave_Type()
)
systemSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSave.setStatus("mandatory")
_SystemRestart_ObjectIdentity = ObjectIdentity
systemRestart = _SystemRestart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 18)
)


class _RestartOption_Type(Integer32):
    """Custom type restartOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSaveConf", 1),
          ("restoreDefaultConf", 2),
          ("restoreFactoryDefault", 3),
          ("saveConf", 0))
    )


_RestartOption_Type.__name__ = "Integer32"
_RestartOption_Object = MibScalar
restartOption = _RestartOption_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 18, 1),
    _RestartOption_Type()
)
restartOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartOption.setStatus("mandatory")


class _RestartDelay_Type(Integer32):
    """Custom type restartDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_RestartDelay_Type.__name__ = "Integer32"
_RestartDelay_Object = MibScalar
restartDelay = _RestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 18, 2),
    _RestartDelay_Type()
)
restartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartDelay.setStatus("mandatory")


class _RestartExec_Type(Integer32):
    """Custom type restartExec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 0),
          ("restart", 1))
    )


_RestartExec_Type.__name__ = "Integer32"
_RestartExec_Object = MibScalar
restartExec = _RestartExec_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 18, 3),
    _RestartExec_Type()
)
restartExec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartExec.setStatus("mandatory")
_RestartStatus_Type = DisplayString
_RestartStatus_Object = MibScalar
restartStatus = _RestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 18, 4),
    _RestartStatus_Type()
)
restartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restartStatus.setStatus("mandatory")
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 19)
)
_PerformanceCpuAvg1min_Type = Integer32
_PerformanceCpuAvg1min_Object = MibScalar
performanceCpuAvg1min = _PerformanceCpuAvg1min_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 19, 1),
    _PerformanceCpuAvg1min_Type()
)
performanceCpuAvg1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceCpuAvg1min.setStatus("mandatory")
_PerformanceCpuAvg5min_Type = Integer32
_PerformanceCpuAvg5min_Object = MibScalar
performanceCpuAvg5min = _PerformanceCpuAvg5min_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 19, 2),
    _PerformanceCpuAvg5min_Type()
)
performanceCpuAvg5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceCpuAvg5min.setStatus("mandatory")
_PerformanceCpuAvg15min_Type = Integer32
_PerformanceCpuAvg15min_Object = MibScalar
performanceCpuAvg15min = _PerformanceCpuAvg15min_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 19, 3),
    _PerformanceCpuAvg15min_Type()
)
performanceCpuAvg15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceCpuAvg15min.setStatus("mandatory")
_PerformanceDynMemLoad_Type = Integer32
_PerformanceDynMemLoad_Object = MibScalar
performanceDynMemLoad = _PerformanceDynMemLoad_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 19, 4),
    _PerformanceDynMemLoad_Type()
)
performanceDynMemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceDynMemLoad.setStatus("mandatory")
_PerformanceDynMemTotal_Type = Integer32
_PerformanceDynMemTotal_Object = MibScalar
performanceDynMemTotal = _PerformanceDynMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 19, 5),
    _PerformanceDynMemTotal_Type()
)
performanceDynMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceDynMemTotal.setStatus("mandatory")
_PerformanceDynMemFree_Type = Integer32
_PerformanceDynMemFree_Object = MibScalar
performanceDynMemFree = _PerformanceDynMemFree_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 19, 6),
    _PerformanceDynMemFree_Type()
)
performanceDynMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceDynMemFree.setStatus("mandatory")
_SystemDefaultScpServer_Type = DisplayString
_SystemDefaultScpServer_Object = MibScalar
systemDefaultScpServer = _SystemDefaultScpServer_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 20),
    _SystemDefaultScpServer_Type()
)
systemDefaultScpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDefaultScpServer.setStatus("mandatory")
_SystemScpUsername_Type = DisplayString
_SystemScpUsername_Object = MibScalar
systemScpUsername = _SystemScpUsername_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 21),
    _SystemScpUsername_Type()
)
systemScpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemScpUsername.setStatus("mandatory")
_SystemScpPassword_Type = DisplayString
_SystemScpPassword_Object = MibScalar
systemScpPassword = _SystemScpPassword_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 22),
    _SystemScpPassword_Type()
)
systemScpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemScpPassword.setStatus("mandatory")


class _SystemConsoleEnable_Type(Integer32):
    """Custom type systemConsoleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SystemConsoleEnable_Type.__name__ = "Integer32"
_SystemConsoleEnable_Object = MibScalar
systemConsoleEnable = _SystemConsoleEnable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 23),
    _SystemConsoleEnable_Type()
)
systemConsoleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConsoleEnable.setStatus("mandatory")


class _SystemLogMsgRate_Type(Integer32):
    """Custom type systemLogMsgRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_SystemLogMsgRate_Type.__name__ = "Integer32"
_SystemLogMsgRate_Object = MibScalar
systemLogMsgRate = _SystemLogMsgRate_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 2, 24),
    _SystemLogMsgRate_Type()
)
systemLogMsgRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogMsgRate.setStatus("mandatory")
_Dsl_ObjectIdentity = ObjectIdentity
dsl = _Dsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3)
)
_Xdsl_ObjectIdentity = ObjectIdentity
xdsl = _Xdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1)
)
_XdslTable_Object = MibTable
xdslTable = _XdslTable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xdslTable.setStatus("mandatory")
_XdslEntry_Object = MibTableRow
xdslEntry = _XdslEntry_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1)
)
xdslEntry.setIndexNames(
    (0, "AETHRA-MIB", "xdslIndex"),
)
if mibBuilder.loadTexts:
    xdslEntry.setStatus("mandatory")


class _XdslIndex_Type(Integer32):
    """Custom type xdslIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XdslIndex_Type.__name__ = "Integer32"
_XdslIndex_Object = MibTableColumn
xdslIndex = _XdslIndex_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 1),
    _XdslIndex_Type()
)
xdslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslIndex.setStatus("mandatory")
_XdslLinkStatus_Type = DisplayString
_XdslLinkStatus_Object = MibTableColumn
xdslLinkStatus = _XdslLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 2),
    _XdslLinkStatus_Type()
)
xdslLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslLinkStatus.setStatus("mandatory")
_XdslTc_Type = DisplayString
_XdslTc_Object = MibTableColumn
xdslTc = _XdslTc_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 3),
    _XdslTc_Type()
)
xdslTc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslTc.setStatus("mandatory")
_XdslUsAttenuation_Type = Integer32
_XdslUsAttenuation_Object = MibTableColumn
xdslUsAttenuation = _XdslUsAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 4),
    _XdslUsAttenuation_Type()
)
xdslUsAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslUsAttenuation.setStatus("mandatory")
_XdslDsAttenuation_Type = Integer32
_XdslDsAttenuation_Object = MibTableColumn
xdslDsAttenuation = _XdslDsAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 5),
    _XdslDsAttenuation_Type()
)
xdslDsAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDsAttenuation.setStatus("mandatory")
_XdslUsNoiseMargin_Type = Integer32
_XdslUsNoiseMargin_Object = MibTableColumn
xdslUsNoiseMargin = _XdslUsNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 6),
    _XdslUsNoiseMargin_Type()
)
xdslUsNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslUsNoiseMargin.setStatus("mandatory")
_XdslDsNoiseMargin_Type = Integer32
_XdslDsNoiseMargin_Object = MibTableColumn
xdslDsNoiseMargin = _XdslDsNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 7),
    _XdslDsNoiseMargin_Type()
)
xdslDsNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDsNoiseMargin.setStatus("mandatory")
_XdslUsCurrRate_Type = Integer32
_XdslUsCurrRate_Object = MibTableColumn
xdslUsCurrRate = _XdslUsCurrRate_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 8),
    _XdslUsCurrRate_Type()
)
xdslUsCurrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslUsCurrRate.setStatus("mandatory")
_XdslDsCurrRate_Type = Integer32
_XdslDsCurrRate_Object = MibTableColumn
xdslDsCurrRate = _XdslDsCurrRate_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 9),
    _XdslDsCurrRate_Type()
)
xdslDsCurrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDsCurrRate.setStatus("mandatory")
_XdslModulationType_Type = DisplayString
_XdslModulationType_Object = MibTableColumn
xdslModulationType = _XdslModulationType_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 10),
    _XdslModulationType_Type()
)
xdslModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslModulationType.setStatus("mandatory")
_XdslUsMaxTheorRate_Type = Integer32
_XdslUsMaxTheorRate_Object = MibTableColumn
xdslUsMaxTheorRate = _XdslUsMaxTheorRate_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 11),
    _XdslUsMaxTheorRate_Type()
)
xdslUsMaxTheorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslUsMaxTheorRate.setStatus("mandatory")
_XdslDsMaxTheorRate_Type = Integer32
_XdslDsMaxTheorRate_Object = MibTableColumn
xdslDsMaxTheorRate = _XdslDsMaxTheorRate_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 12),
    _XdslDsMaxTheorRate_Type()
)
xdslDsMaxTheorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDsMaxTheorRate.setStatus("mandatory")
_XdslUsTotBytes_Type = Integer32
_XdslUsTotBytes_Object = MibTableColumn
xdslUsTotBytes = _XdslUsTotBytes_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 13),
    _XdslUsTotBytes_Type()
)
xdslUsTotBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslUsTotBytes.setStatus("mandatory")
_XdslDsTotBytes_Type = Integer32
_XdslDsTotBytes_Object = MibTableColumn
xdslDsTotBytes = _XdslDsTotBytes_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 14),
    _XdslDsTotBytes_Type()
)
xdslDsTotBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDsTotBytes.setStatus("mandatory")
_XdslNeTotCrcErr_Type = Integer32
_XdslNeTotCrcErr_Object = MibTableColumn
xdslNeTotCrcErr = _XdslNeTotCrcErr_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 15),
    _XdslNeTotCrcErr_Type()
)
xdslNeTotCrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslNeTotCrcErr.setStatus("mandatory")
_XdslNeShowtimeCrcErr_Type = Integer32
_XdslNeShowtimeCrcErr_Object = MibTableColumn
xdslNeShowtimeCrcErr = _XdslNeShowtimeCrcErr_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 1, 1, 1, 16),
    _XdslNeShowtimeCrcErr_Type()
)
xdslNeShowtimeCrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslNeShowtimeCrcErr.setStatus("mandatory")
_Shdsl_ObjectIdentity = ObjectIdentity
shdsl = _Shdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2)
)
_ShdslTable_Object = MibTable
shdslTable = _ShdslTable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    shdslTable.setStatus("mandatory")
_ShdslEntry_Object = MibTableRow
shdslEntry = _ShdslEntry_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1)
)
shdslEntry.setIndexNames(
    (0, "AETHRA-MIB", "shdslIndex"),
)
if mibBuilder.loadTexts:
    shdslEntry.setStatus("mandatory")


class _ShdslIndex_Type(Integer32):
    """Custom type shdslIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ShdslIndex_Type.__name__ = "Integer32"
_ShdslIndex_Object = MibTableColumn
shdslIndex = _ShdslIndex_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 1),
    _ShdslIndex_Type()
)
shdslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslIndex.setStatus("mandatory")
_ShdslPhyStatus_Type = DisplayString
_ShdslPhyStatus_Object = MibTableColumn
shdslPhyStatus = _ShdslPhyStatus_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 2),
    _ShdslPhyStatus_Type()
)
shdslPhyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslPhyStatus.setStatus("mandatory")
_ShdslTc_Type = DisplayString
_ShdslTc_Object = MibTableColumn
shdslTc = _ShdslTc_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 3),
    _ShdslTc_Type()
)
shdslTc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslTc.setStatus("mandatory")
_ShdslUsAttenuation_Type = Integer32
_ShdslUsAttenuation_Object = MibTableColumn
shdslUsAttenuation = _ShdslUsAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 4),
    _ShdslUsAttenuation_Type()
)
shdslUsAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslUsAttenuation.setStatus("mandatory")
_ShdslDsAttenuation_Type = Integer32
_ShdslDsAttenuation_Object = MibTableColumn
shdslDsAttenuation = _ShdslDsAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 5),
    _ShdslDsAttenuation_Type()
)
shdslDsAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDsAttenuation.setStatus("mandatory")
_ShdslUsNoiseMargin_Type = Integer32
_ShdslUsNoiseMargin_Object = MibTableColumn
shdslUsNoiseMargin = _ShdslUsNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 6),
    _ShdslUsNoiseMargin_Type()
)
shdslUsNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslUsNoiseMargin.setStatus("mandatory")
_ShdslDsNoiseMargin_Type = Integer32
_ShdslDsNoiseMargin_Object = MibTableColumn
shdslDsNoiseMargin = _ShdslDsNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 7),
    _ShdslDsNoiseMargin_Type()
)
shdslDsNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDsNoiseMargin.setStatus("mandatory")
_ShdslUsCurrRate_Type = Integer32
_ShdslUsCurrRate_Object = MibTableColumn
shdslUsCurrRate = _ShdslUsCurrRate_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 8),
    _ShdslUsCurrRate_Type()
)
shdslUsCurrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslUsCurrRate.setStatus("mandatory")
_ShdslDsCurrRate_Type = Integer32
_ShdslDsCurrRate_Object = MibTableColumn
shdslDsCurrRate = _ShdslDsCurrRate_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 9),
    _ShdslDsCurrRate_Type()
)
shdslDsCurrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDsCurrRate.setStatus("mandatory")
_ShdslModulationType_Type = DisplayString
_ShdslModulationType_Object = MibTableColumn
shdslModulationType = _ShdslModulationType_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 10),
    _ShdslModulationType_Type()
)
shdslModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslModulationType.setStatus("mandatory")
_ShdslUsMaxTheorRate_Type = Integer32
_ShdslUsMaxTheorRate_Object = MibTableColumn
shdslUsMaxTheorRate = _ShdslUsMaxTheorRate_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 11),
    _ShdslUsMaxTheorRate_Type()
)
shdslUsMaxTheorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslUsMaxTheorRate.setStatus("mandatory")
_ShdslDsMaxTheorRate_Type = Integer32
_ShdslDsMaxTheorRate_Object = MibTableColumn
shdslDsMaxTheorRate = _ShdslDsMaxTheorRate_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 12),
    _ShdslDsMaxTheorRate_Type()
)
shdslDsMaxTheorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDsMaxTheorRate.setStatus("mandatory")
_ShdslUsTotBytes_Type = Integer32
_ShdslUsTotBytes_Object = MibTableColumn
shdslUsTotBytes = _ShdslUsTotBytes_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 13),
    _ShdslUsTotBytes_Type()
)
shdslUsTotBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslUsTotBytes.setStatus("mandatory")
_ShdslDsTotBytes_Type = Integer32
_ShdslDsTotBytes_Object = MibTableColumn
shdslDsTotBytes = _ShdslDsTotBytes_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 14),
    _ShdslDsTotBytes_Type()
)
shdslDsTotBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDsTotBytes.setStatus("mandatory")
_ShdslNeTotCrcErr_Type = Integer32
_ShdslNeTotCrcErr_Object = MibTableColumn
shdslNeTotCrcErr = _ShdslNeTotCrcErr_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 15),
    _ShdslNeTotCrcErr_Type()
)
shdslNeTotCrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslNeTotCrcErr.setStatus("mandatory")
_ShdslNeShowtimeCrcErr_Type = Integer32
_ShdslNeShowtimeCrcErr_Object = MibTableColumn
shdslNeShowtimeCrcErr = _ShdslNeShowtimeCrcErr_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 16),
    _ShdslNeShowtimeCrcErr_Type()
)
shdslNeShowtimeCrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslNeShowtimeCrcErr.setStatus("mandatory")
_ShdslUsPower_Type = Integer32
_ShdslUsPower_Object = MibTableColumn
shdslUsPower = _ShdslUsPower_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 17),
    _ShdslUsPower_Type()
)
shdslUsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslUsPower.setStatus("mandatory")
_ShdslDsPower_Type = Integer32
_ShdslDsPower_Object = MibTableColumn
shdslDsPower = _ShdslDsPower_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 3, 2, 1, 1, 18),
    _ShdslDsPower_Type()
)
shdslDsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDsPower.setStatus("mandatory")
_Voip_ObjectIdentity = ObjectIdentity
voip = _Voip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4)
)
_Trunk_ObjectIdentity = ObjectIdentity
trunk = _Trunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1)
)
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("mandatory")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1, 1)
)
trunkEntry.setIndexNames(
    (0, "AETHRA-MIB", "trunkIndex"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("mandatory")


class _TrunkIndex_Type(Integer32):
    """Custom type trunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TrunkIndex_Type.__name__ = "Integer32"
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("mandatory")
_TrunkName_Type = DisplayString
_TrunkName_Object = MibTableColumn
trunkName = _TrunkName_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1, 1, 2),
    _TrunkName_Type()
)
trunkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkName.setStatus("mandatory")
_TrunkType_Type = DisplayString
_TrunkType_Object = MibTableColumn
trunkType = _TrunkType_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1, 1, 3),
    _TrunkType_Type()
)
trunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkType.setStatus("mandatory")


class _TrunkEnable_Type(Integer32):
    """Custom type trunkEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("registered", 1),
          ("unregistered", 2))
    )


_TrunkEnable_Type.__name__ = "Integer32"
_TrunkEnable_Object = MibTableColumn
trunkEnable = _TrunkEnable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1, 1, 4),
    _TrunkEnable_Type()
)
trunkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkEnable.setStatus("mandatory")
_TrunkDescription_Type = DisplayString
_TrunkDescription_Object = MibTableColumn
trunkDescription = _TrunkDescription_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1, 1, 5),
    _TrunkDescription_Type()
)
trunkDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkDescription.setStatus("mandatory")
_TrunkUserName_Type = DisplayString
_TrunkUserName_Object = MibTableColumn
trunkUserName = _TrunkUserName_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1, 1, 6),
    _TrunkUserName_Type()
)
trunkUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkUserName.setStatus("mandatory")
_TrunkRegHost_Type = DisplayString
_TrunkRegHost_Object = MibTableColumn
trunkRegHost = _TrunkRegHost_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1, 1, 7),
    _TrunkRegHost_Type()
)
trunkRegHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRegHost.setStatus("mandatory")
_TrunkProxyHost_Type = DisplayString
_TrunkProxyHost_Object = MibTableColumn
trunkProxyHost = _TrunkProxyHost_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1, 1, 8),
    _TrunkProxyHost_Type()
)
trunkProxyHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkProxyHost.setStatus("mandatory")
_TrunkIfcStatus_Type = DisplayString
_TrunkIfcStatus_Object = MibTableColumn
trunkIfcStatus = _TrunkIfcStatus_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1, 1, 9),
    _TrunkIfcStatus_Type()
)
trunkIfcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkIfcStatus.setStatus("mandatory")
_TrunkRegStatus_Type = DisplayString
_TrunkRegStatus_Object = MibTableColumn
trunkRegStatus = _TrunkRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1, 1, 10),
    _TrunkRegStatus_Type()
)
trunkRegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRegStatus.setStatus("mandatory")
_TrunkMsgWait_Type = DisplayString
_TrunkMsgWait_Object = MibTableColumn
trunkMsgWait = _TrunkMsgWait_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 1, 1, 11),
    _TrunkMsgWait_Type()
)
trunkMsgWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkMsgWait.setStatus("mandatory")
_TrunkIsdnTable_Object = MibTable
trunkIsdnTable = _TrunkIsdnTable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 2)
)
if mibBuilder.loadTexts:
    trunkIsdnTable.setStatus("mandatory")
_TrunkIsdnEntry_Object = MibTableRow
trunkIsdnEntry = _TrunkIsdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 2, 1)
)
trunkIsdnEntry.setIndexNames(
    (0, "AETHRA-MIB", "trunkIsdnIndex"),
)
if mibBuilder.loadTexts:
    trunkIsdnEntry.setStatus("mandatory")


class _TrunkIsdnIndex_Type(Integer32):
    """Custom type trunkIsdnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TrunkIsdnIndex_Type.__name__ = "Integer32"
_TrunkIsdnIndex_Object = MibTableColumn
trunkIsdnIndex = _TrunkIsdnIndex_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 2, 1, 1),
    _TrunkIsdnIndex_Type()
)
trunkIsdnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkIsdnIndex.setStatus("mandatory")
_TrunkIsdnName_Type = DisplayString
_TrunkIsdnName_Object = MibTableColumn
trunkIsdnName = _TrunkIsdnName_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 2, 1, 2),
    _TrunkIsdnName_Type()
)
trunkIsdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkIsdnName.setStatus("mandatory")
_TrunkIsdnType_Type = DisplayString
_TrunkIsdnType_Object = MibTableColumn
trunkIsdnType = _TrunkIsdnType_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 2, 1, 3),
    _TrunkIsdnType_Type()
)
trunkIsdnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkIsdnType.setStatus("mandatory")


class _TrunkIsdnEnable_Type(Integer32):
    """Custom type trunkIsdnEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TrunkIsdnEnable_Type.__name__ = "Integer32"
_TrunkIsdnEnable_Object = MibTableColumn
trunkIsdnEnable = _TrunkIsdnEnable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 2, 1, 4),
    _TrunkIsdnEnable_Type()
)
trunkIsdnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkIsdnEnable.setStatus("mandatory")
_TrunkIsdnDescription_Type = DisplayString
_TrunkIsdnDescription_Object = MibTableColumn
trunkIsdnDescription = _TrunkIsdnDescription_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 2, 1, 5),
    _TrunkIsdnDescription_Type()
)
trunkIsdnDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkIsdnDescription.setStatus("mandatory")
_TrunkIsdnB1Status_Type = DisplayString
_TrunkIsdnB1Status_Object = MibTableColumn
trunkIsdnB1Status = _TrunkIsdnB1Status_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 2, 1, 6),
    _TrunkIsdnB1Status_Type()
)
trunkIsdnB1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkIsdnB1Status.setStatus("mandatory")
_TrunkIsdnB2Status_Type = DisplayString
_TrunkIsdnB2Status_Object = MibTableColumn
trunkIsdnB2Status = _TrunkIsdnB2Status_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 2, 1, 7),
    _TrunkIsdnB2Status_Type()
)
trunkIsdnB2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkIsdnB2Status.setStatus("mandatory")
_TrunkFxoTable_Object = MibTable
trunkFxoTable = _TrunkFxoTable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 3)
)
if mibBuilder.loadTexts:
    trunkFxoTable.setStatus("mandatory")
_TrunkFxoEntry_Object = MibTableRow
trunkFxoEntry = _TrunkFxoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 3, 1)
)
trunkFxoEntry.setIndexNames(
    (0, "AETHRA-MIB", "trunkFxoIndex"),
)
if mibBuilder.loadTexts:
    trunkFxoEntry.setStatus("mandatory")


class _TrunkFxoIndex_Type(Integer32):
    """Custom type trunkFxoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TrunkFxoIndex_Type.__name__ = "Integer32"
_TrunkFxoIndex_Object = MibTableColumn
trunkFxoIndex = _TrunkFxoIndex_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 3, 1, 1),
    _TrunkFxoIndex_Type()
)
trunkFxoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkFxoIndex.setStatus("mandatory")
_TrunkFxoName_Type = DisplayString
_TrunkFxoName_Object = MibTableColumn
trunkFxoName = _TrunkFxoName_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 3, 1, 2),
    _TrunkFxoName_Type()
)
trunkFxoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkFxoName.setStatus("mandatory")
_TrunkFxoType_Type = DisplayString
_TrunkFxoType_Object = MibTableColumn
trunkFxoType = _TrunkFxoType_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 3, 1, 3),
    _TrunkFxoType_Type()
)
trunkFxoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkFxoType.setStatus("mandatory")


class _TrunkFxoEnable_Type(Integer32):
    """Custom type trunkFxoEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TrunkFxoEnable_Type.__name__ = "Integer32"
_TrunkFxoEnable_Object = MibTableColumn
trunkFxoEnable = _TrunkFxoEnable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 3, 1, 4),
    _TrunkFxoEnable_Type()
)
trunkFxoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkFxoEnable.setStatus("mandatory")
_TrunkFxoDescription_Type = DisplayString
_TrunkFxoDescription_Object = MibTableColumn
trunkFxoDescription = _TrunkFxoDescription_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 3, 1, 5),
    _TrunkFxoDescription_Type()
)
trunkFxoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkFxoDescription.setStatus("mandatory")
_TrunkFxoStatus_Type = DisplayString
_TrunkFxoStatus_Object = MibTableColumn
trunkFxoStatus = _TrunkFxoStatus_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 1, 3, 1, 6),
    _TrunkFxoStatus_Type()
)
trunkFxoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkFxoStatus.setStatus("mandatory")
_UserTerminal_ObjectIdentity = ObjectIdentity
userTerminal = _UserTerminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2)
)
_UsTermPotsTable_Object = MibTable
usTermPotsTable = _UsTermPotsTable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    usTermPotsTable.setStatus("mandatory")
_UsTermPotsEntry_Object = MibTableRow
usTermPotsEntry = _UsTermPotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 1, 1)
)
usTermPotsEntry.setIndexNames(
    (0, "AETHRA-MIB", "usTermPotsIndex"),
)
if mibBuilder.loadTexts:
    usTermPotsEntry.setStatus("mandatory")


class _UsTermPotsIndex_Type(Integer32):
    """Custom type usTermPotsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsTermPotsIndex_Type.__name__ = "Integer32"
_UsTermPotsIndex_Object = MibTableColumn
usTermPotsIndex = _UsTermPotsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 1, 1, 1),
    _UsTermPotsIndex_Type()
)
usTermPotsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usTermPotsIndex.setStatus("mandatory")


class _UsTermPotsEnable_Type(Integer32):
    """Custom type usTermPotsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UsTermPotsEnable_Type.__name__ = "Integer32"
_UsTermPotsEnable_Object = MibTableColumn
usTermPotsEnable = _UsTermPotsEnable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 1, 1, 2),
    _UsTermPotsEnable_Type()
)
usTermPotsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usTermPotsEnable.setStatus("mandatory")
_UsTermPotsDescription_Type = DisplayString
_UsTermPotsDescription_Object = MibTableColumn
usTermPotsDescription = _UsTermPotsDescription_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 1, 1, 3),
    _UsTermPotsDescription_Type()
)
usTermPotsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usTermPotsDescription.setStatus("mandatory")
_UsTermPotsStatus_Type = DisplayString
_UsTermPotsStatus_Object = MibTableColumn
usTermPotsStatus = _UsTermPotsStatus_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 1, 1, 4),
    _UsTermPotsStatus_Type()
)
usTermPotsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usTermPotsStatus.setStatus("mandatory")
_UsTermPotsDspSlic_Type = DisplayString
_UsTermPotsDspSlic_Object = MibTableColumn
usTermPotsDspSlic = _UsTermPotsDspSlic_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 1, 1, 5),
    _UsTermPotsDspSlic_Type()
)
usTermPotsDspSlic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usTermPotsDspSlic.setStatus("mandatory")
_UsTermISDNTable_Object = MibTable
usTermISDNTable = _UsTermISDNTable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 2)
)
if mibBuilder.loadTexts:
    usTermISDNTable.setStatus("mandatory")
_UsTermISDNEntry_Object = MibTableRow
usTermISDNEntry = _UsTermISDNEntry_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 2, 1)
)
usTermISDNEntry.setIndexNames(
    (0, "AETHRA-MIB", "usTermISDNIndex"),
)
if mibBuilder.loadTexts:
    usTermISDNEntry.setStatus("mandatory")


class _UsTermISDNIndex_Type(Integer32):
    """Custom type usTermISDNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsTermISDNIndex_Type.__name__ = "Integer32"
_UsTermISDNIndex_Object = MibTableColumn
usTermISDNIndex = _UsTermISDNIndex_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 2, 1, 1),
    _UsTermISDNIndex_Type()
)
usTermISDNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usTermISDNIndex.setStatus("mandatory")


class _UsTermISDNEnable_Type(Integer32):
    """Custom type usTermISDNEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UsTermISDNEnable_Type.__name__ = "Integer32"
_UsTermISDNEnable_Object = MibTableColumn
usTermISDNEnable = _UsTermISDNEnable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 2, 1, 2),
    _UsTermISDNEnable_Type()
)
usTermISDNEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usTermISDNEnable.setStatus("mandatory")
_UsTermISDNDescription_Type = DisplayString
_UsTermISDNDescription_Object = MibTableColumn
usTermISDNDescription = _UsTermISDNDescription_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 2, 1, 3),
    _UsTermISDNDescription_Type()
)
usTermISDNDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usTermISDNDescription.setStatus("mandatory")
_UsTermIsdnStatusB1_Type = DisplayString
_UsTermIsdnStatusB1_Object = MibTableColumn
usTermIsdnStatusB1 = _UsTermIsdnStatusB1_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 2, 1, 4),
    _UsTermIsdnStatusB1_Type()
)
usTermIsdnStatusB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usTermIsdnStatusB1.setStatus("mandatory")
_UsTermIsdnStatusB2_Type = DisplayString
_UsTermIsdnStatusB2_Object = MibTableColumn
usTermIsdnStatusB2 = _UsTermIsdnStatusB2_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 2, 1, 5),
    _UsTermIsdnStatusB2_Type()
)
usTermIsdnStatusB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usTermIsdnStatusB2.setStatus("mandatory")
_UsTermDectTable_Object = MibTable
usTermDectTable = _UsTermDectTable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 3)
)
if mibBuilder.loadTexts:
    usTermDectTable.setStatus("mandatory")
_UsTermDectEntry_Object = MibTableRow
usTermDectEntry = _UsTermDectEntry_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 3, 1)
)
usTermDectEntry.setIndexNames(
    (0, "AETHRA-MIB", "usTermDectIndex"),
)
if mibBuilder.loadTexts:
    usTermDectEntry.setStatus("mandatory")


class _UsTermDectIndex_Type(Integer32):
    """Custom type usTermDectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsTermDectIndex_Type.__name__ = "Integer32"
_UsTermDectIndex_Object = MibTableColumn
usTermDectIndex = _UsTermDectIndex_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 3, 1, 1),
    _UsTermDectIndex_Type()
)
usTermDectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usTermDectIndex.setStatus("mandatory")


class _UsTermDectEnable_Type(Integer32):
    """Custom type usTermDectEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UsTermDectEnable_Type.__name__ = "Integer32"
_UsTermDectEnable_Object = MibTableColumn
usTermDectEnable = _UsTermDectEnable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 3, 1, 2),
    _UsTermDectEnable_Type()
)
usTermDectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usTermDectEnable.setStatus("mandatory")
_UsTermDectDescription_Type = DisplayString
_UsTermDectDescription_Object = MibTableColumn
usTermDectDescription = _UsTermDectDescription_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 3, 1, 3),
    _UsTermDectDescription_Type()
)
usTermDectDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usTermDectDescription.setStatus("mandatory")
_UsTermDectStatus_Type = DisplayString
_UsTermDectStatus_Object = MibTableColumn
usTermDectStatus = _UsTermDectStatus_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 3, 1, 4),
    _UsTermDectStatus_Type()
)
usTermDectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usTermDectStatus.setStatus("mandatory")
_UsTermDectDspSlic_Type = DisplayString
_UsTermDectDspSlic_Object = MibTableColumn
usTermDectDspSlic = _UsTermDectDspSlic_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 2, 3, 1, 5),
    _UsTermDectDspSlic_Type()
)
usTermDectDspSlic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usTermDectDspSlic.setStatus("mandatory")


class _VoipMaxConnection_Type(Integer32):
    """Custom type voipMaxConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VoipMaxConnection_Type.__name__ = "Integer32"
_VoipMaxConnection_Object = MibScalar
voipMaxConnection = _VoipMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 4, 3),
    _VoipMaxConnection_Type()
)
voipMaxConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipMaxConnection.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5)
)
_GenericError_Type = DisplayString
_GenericError_Object = MibScalar
genericError = _GenericError_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 2),
    _GenericError_Type()
)
genericError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericError.setStatus("mandatory")
_MgmtAccesses_ObjectIdentity = ObjectIdentity
mgmtAccesses = _MgmtAccesses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 7)
)


class _MgmtUser_Type(DisplayString):
    """Custom type mgmtUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MgmtUser_Type.__name__ = "DisplayString"
_MgmtUser_Object = MibScalar
mgmtUser = _MgmtUser_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 7, 1),
    _MgmtUser_Type()
)
mgmtUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtUser.setStatus("mandatory")


class _MgmtPrivilege_Type(DisplayString):
    """Custom type mgmtPrivilege based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MgmtPrivilege_Type.__name__ = "DisplayString"
_MgmtPrivilege_Object = MibScalar
mgmtPrivilege = _MgmtPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 7, 2),
    _MgmtPrivilege_Type()
)
mgmtPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtPrivilege.setStatus("mandatory")


class _MgmtTime_Type(DisplayString):
    """Custom type mgmtTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MgmtTime_Type.__name__ = "DisplayString"
_MgmtTime_Object = MibScalar
mgmtTime = _MgmtTime_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 7, 3),
    _MgmtTime_Type()
)
mgmtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtTime.setStatus("mandatory")


class _MgmtType_Type(Integer32):
    """Custom type mgmtType based on Integer32"""
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
        *(("console", 1),
          ("snmp", 4),
          ("ssh", 5),
          ("telnet", 2),
          ("tr069", 6),
          ("unknown", 7),
          ("web", 3))
    )


_MgmtType_Type.__name__ = "Integer32"
_MgmtType_Object = MibScalar
mgmtType = _MgmtType_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 7, 4),
    _MgmtType_Type()
)
mgmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtType.setStatus("mandatory")


class _MgmtAddress_Type(DisplayString):
    """Custom type mgmtAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MgmtAddress_Type.__name__ = "DisplayString"
_MgmtAddress_Object = MibScalar
mgmtAddress = _MgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 7, 5),
    _MgmtAddress_Type()
)
mgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtAddress.setStatus("mandatory")
_Ifc_ObjectIdentity = ObjectIdentity
ifc = _Ifc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7745, 5, 6)
)
_IfcTable_Object = MibTable
ifcTable = _IfcTable_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 6, 1)
)
if mibBuilder.loadTexts:
    ifcTable.setStatus("mandatory")
_IfcEntry_Object = MibTableRow
ifcEntry = _IfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 6, 1, 1)
)
ifcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifcEntry.setStatus("mandatory")


class _IfcName_Type(DisplayString):
    """Custom type ifcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfcName_Type.__name__ = "DisplayString"
_IfcName_Object = MibTableColumn
ifcName = _IfcName_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 6, 1, 1, 1),
    _IfcName_Type()
)
ifcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcName.setStatus("mandatory")


class _IfcDescr_Type(DisplayString):
    """Custom type ifcDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfcDescr_Type.__name__ = "DisplayString"
_IfcDescr_Object = MibTableColumn
ifcDescr = _IfcDescr_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 6, 1, 1, 2),
    _IfcDescr_Type()
)
ifcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcDescr.setStatus("mandatory")
_IfcType_Type = IANAifType
_IfcType_Object = MibTableColumn
ifcType = _IfcType_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 6, 1, 1, 3),
    _IfcType_Type()
)
ifcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcType.setStatus("mandatory")
_IfcPhysAddress_Type = PhysAddress
_IfcPhysAddress_Object = MibTableColumn
ifcPhysAddress = _IfcPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 6, 1, 1, 4),
    _IfcPhysAddress_Type()
)
ifcPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcPhysAddress.setStatus("mandatory")
_IfcMtu_Type = Integer32
_IfcMtu_Object = MibTableColumn
ifcMtu = _IfcMtu_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 6, 1, 1, 5),
    _IfcMtu_Type()
)
ifcMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcMtu.setStatus("mandatory")
_IfcSpeed_Type = Gauge32
_IfcSpeed_Object = MibTableColumn
ifcSpeed = _IfcSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 6, 1, 1, 6),
    _IfcSpeed_Type()
)
ifcSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcSpeed.setStatus("mandatory")
_IfcRxRate_Type = Counter32
_IfcRxRate_Object = MibTableColumn
ifcRxRate = _IfcRxRate_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 6, 1, 1, 7),
    _IfcRxRate_Type()
)
ifcRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcRxRate.setStatus("mandatory")
_IfcTxRate_Type = Counter32
_IfcTxRate_Object = MibTableColumn
ifcTxRate = _IfcTxRate_Object(
    (1, 3, 6, 1, 4, 1, 7745, 5, 6, 1, 1, 8),
    _IfcTxRate_Type()
)
ifcTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcTxRate.setStatus("mandatory")

# Managed Objects groups


# Notification objects

genericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 1)
)
genericTrap.setObjects(
    ("AETHRA-MIB", "genericError")
)
if mibBuilder.loadTexts:
    genericTrap.setStatus(
        "current"
    )

interfaceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 3)
)
interfaceUp.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    interfaceUp.setStatus(
        "current"
    )

interfaceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 4)
)
interfaceDown.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    interfaceDown.setStatus(
        "current"
    )

trunkRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 5)
)
trunkRegistered.setObjects(
    ("AETHRA-MIB", "trunkName")
)
if mibBuilder.loadTexts:
    trunkRegistered.setStatus(
        "current"
    )

trunkUnregistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 6)
)
trunkUnregistered.setObjects(
    ("AETHRA-MIB", "trunkName")
)
if mibBuilder.loadTexts:
    trunkUnregistered.setStatus(
        "current"
    )

mgmtLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 7, 6)
)
mgmtLogin.setObjects(
      *(("AETHRA-MIB", "mgmtUser"),
        ("AETHRA-MIB", "mgmtPrivilege"),
        ("AETHRA-MIB", "mgmtTime"),
        ("AETHRA-MIB", "mgmtType"),
        ("AETHRA-MIB", "mgmtAddress"))
)
if mibBuilder.loadTexts:
    mgmtLogin.setStatus(
        "current"
    )

mgmtLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 7, 7)
)
mgmtLogout.setObjects(
      *(("AETHRA-MIB", "mgmtUser"),
        ("AETHRA-MIB", "mgmtPrivilege"),
        ("AETHRA-MIB", "mgmtTime"),
        ("AETHRA-MIB", "mgmtType"),
        ("AETHRA-MIB", "mgmtAddress"))
)
if mibBuilder.loadTexts:
    mgmtLogout.setStatus(
        "current"
    )

mgmtChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7745, 5, 5, 7, 8)
)
mgmtChange.setObjects(
      *(("AETHRA-MIB", "mgmtUser"),
        ("AETHRA-MIB", "mgmtTime"),
        ("AETHRA-MIB", "mgmtType"),
        ("AETHRA-MIB", "mgmtAddress"))
)
if mibBuilder.loadTexts:
    mgmtChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AETHRA-MIB",
    **{"aethra": aethra,
       "atosnt": atosnt,
       "tools": tools,
       "fileTransfer": fileTransfer,
       "fileTransferProtocol": fileTransferProtocol,
       "fileTransferFileName": fileTransferFileName,
       "fileTransferServerName": fileTransferServerName,
       "fileTransferOption": fileTransferOption,
       "fileTransferStorageFileName": fileTransferStorageFileName,
       "fileTransferExec": fileTransferExec,
       "fileTransferStatus": fileTransferStatus,
       "ping": ping,
       "pingParameters": pingParameters,
       "pingHost": pingHost,
       "pingSize": pingSize,
       "pingTries": pingTries,
       "pingTTL": pingTTL,
       "pingTimeOut": pingTimeOut,
       "pingSource": pingSource,
       "pingStart": pingStart,
       "pingStatus": pingStatus,
       "pingStatistics": pingStatistics,
       "pingTXpacket": pingTXpacket,
       "pingRXpacket": pingRXpacket,
       "pingLOSTpacket": pingLOSTpacket,
       "pingMinRTT": pingMinRTT,
       "pingMaxRTT": pingMaxRTT,
       "pingAvgRTT": pingAvgRTT,
       "system": system,
       "systemLoglevel": systemLoglevel,
       "systemDescription": systemDescription,
       "systemName": systemName,
       "systemLocalDomain": systemLocalDomain,
       "systemDefaultTftpServer": systemDefaultTftpServer,
       "systemTftpLocalAdd": systemTftpLocalAdd,
       "systemDefaultFtpServer": systemDefaultFtpServer,
       "systemFtpLocalAdd": systemFtpLocalAdd,
       "systemFtpUsername": systemFtpUsername,
       "systemFtpPassword": systemFtpPassword,
       "systemAAAProfile": systemAAAProfile,
       "systemAAALogTimeout": systemAAALogTimeout,
       "systemBackupAuth": systemBackupAuth,
       "systemScrollLine": systemScrollLine,
       "systemKernelLogs": systemKernelLogs,
       "systemCryptedPassword": systemCryptedPassword,
       "systemSave": systemSave,
       "systemRestart": systemRestart,
       "restartOption": restartOption,
       "restartDelay": restartDelay,
       "restartExec": restartExec,
       "restartStatus": restartStatus,
       "performance": performance,
       "performanceCpuAvg1min": performanceCpuAvg1min,
       "performanceCpuAvg5min": performanceCpuAvg5min,
       "performanceCpuAvg15min": performanceCpuAvg15min,
       "performanceDynMemLoad": performanceDynMemLoad,
       "performanceDynMemTotal": performanceDynMemTotal,
       "performanceDynMemFree": performanceDynMemFree,
       "systemDefaultScpServer": systemDefaultScpServer,
       "systemScpUsername": systemScpUsername,
       "systemScpPassword": systemScpPassword,
       "systemConsoleEnable": systemConsoleEnable,
       "systemLogMsgRate": systemLogMsgRate,
       "dsl": dsl,
       "xdsl": xdsl,
       "xdslTable": xdslTable,
       "xdslEntry": xdslEntry,
       "xdslIndex": xdslIndex,
       "xdslLinkStatus": xdslLinkStatus,
       "xdslTc": xdslTc,
       "xdslUsAttenuation": xdslUsAttenuation,
       "xdslDsAttenuation": xdslDsAttenuation,
       "xdslUsNoiseMargin": xdslUsNoiseMargin,
       "xdslDsNoiseMargin": xdslDsNoiseMargin,
       "xdslUsCurrRate": xdslUsCurrRate,
       "xdslDsCurrRate": xdslDsCurrRate,
       "xdslModulationType": xdslModulationType,
       "xdslUsMaxTheorRate": xdslUsMaxTheorRate,
       "xdslDsMaxTheorRate": xdslDsMaxTheorRate,
       "xdslUsTotBytes": xdslUsTotBytes,
       "xdslDsTotBytes": xdslDsTotBytes,
       "xdslNeTotCrcErr": xdslNeTotCrcErr,
       "xdslNeShowtimeCrcErr": xdslNeShowtimeCrcErr,
       "shdsl": shdsl,
       "shdslTable": shdslTable,
       "shdslEntry": shdslEntry,
       "shdslIndex": shdslIndex,
       "shdslPhyStatus": shdslPhyStatus,
       "shdslTc": shdslTc,
       "shdslUsAttenuation": shdslUsAttenuation,
       "shdslDsAttenuation": shdslDsAttenuation,
       "shdslUsNoiseMargin": shdslUsNoiseMargin,
       "shdslDsNoiseMargin": shdslDsNoiseMargin,
       "shdslUsCurrRate": shdslUsCurrRate,
       "shdslDsCurrRate": shdslDsCurrRate,
       "shdslModulationType": shdslModulationType,
       "shdslUsMaxTheorRate": shdslUsMaxTheorRate,
       "shdslDsMaxTheorRate": shdslDsMaxTheorRate,
       "shdslUsTotBytes": shdslUsTotBytes,
       "shdslDsTotBytes": shdslDsTotBytes,
       "shdslNeTotCrcErr": shdslNeTotCrcErr,
       "shdslNeShowtimeCrcErr": shdslNeShowtimeCrcErr,
       "shdslUsPower": shdslUsPower,
       "shdslDsPower": shdslDsPower,
       "voip": voip,
       "trunk": trunk,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkIndex": trunkIndex,
       "trunkName": trunkName,
       "trunkType": trunkType,
       "trunkEnable": trunkEnable,
       "trunkDescription": trunkDescription,
       "trunkUserName": trunkUserName,
       "trunkRegHost": trunkRegHost,
       "trunkProxyHost": trunkProxyHost,
       "trunkIfcStatus": trunkIfcStatus,
       "trunkRegStatus": trunkRegStatus,
       "trunkMsgWait": trunkMsgWait,
       "trunkIsdnTable": trunkIsdnTable,
       "trunkIsdnEntry": trunkIsdnEntry,
       "trunkIsdnIndex": trunkIsdnIndex,
       "trunkIsdnName": trunkIsdnName,
       "trunkIsdnType": trunkIsdnType,
       "trunkIsdnEnable": trunkIsdnEnable,
       "trunkIsdnDescription": trunkIsdnDescription,
       "trunkIsdnB1Status": trunkIsdnB1Status,
       "trunkIsdnB2Status": trunkIsdnB2Status,
       "trunkFxoTable": trunkFxoTable,
       "trunkFxoEntry": trunkFxoEntry,
       "trunkFxoIndex": trunkFxoIndex,
       "trunkFxoName": trunkFxoName,
       "trunkFxoType": trunkFxoType,
       "trunkFxoEnable": trunkFxoEnable,
       "trunkFxoDescription": trunkFxoDescription,
       "trunkFxoStatus": trunkFxoStatus,
       "userTerminal": userTerminal,
       "usTermPotsTable": usTermPotsTable,
       "usTermPotsEntry": usTermPotsEntry,
       "usTermPotsIndex": usTermPotsIndex,
       "usTermPotsEnable": usTermPotsEnable,
       "usTermPotsDescription": usTermPotsDescription,
       "usTermPotsStatus": usTermPotsStatus,
       "usTermPotsDspSlic": usTermPotsDspSlic,
       "usTermISDNTable": usTermISDNTable,
       "usTermISDNEntry": usTermISDNEntry,
       "usTermISDNIndex": usTermISDNIndex,
       "usTermISDNEnable": usTermISDNEnable,
       "usTermISDNDescription": usTermISDNDescription,
       "usTermIsdnStatusB1": usTermIsdnStatusB1,
       "usTermIsdnStatusB2": usTermIsdnStatusB2,
       "usTermDectTable": usTermDectTable,
       "usTermDectEntry": usTermDectEntry,
       "usTermDectIndex": usTermDectIndex,
       "usTermDectEnable": usTermDectEnable,
       "usTermDectDescription": usTermDectDescription,
       "usTermDectStatus": usTermDectStatus,
       "usTermDectDspSlic": usTermDectDspSlic,
       "voipMaxConnection": voipMaxConnection,
       "traps": traps,
       "genericTrap": genericTrap,
       "genericError": genericError,
       "interfaceUp": interfaceUp,
       "interfaceDown": interfaceDown,
       "trunkRegistered": trunkRegistered,
       "trunkUnregistered": trunkUnregistered,
       "mgmtAccesses": mgmtAccesses,
       "mgmtUser": mgmtUser,
       "mgmtPrivilege": mgmtPrivilege,
       "mgmtTime": mgmtTime,
       "mgmtType": mgmtType,
       "mgmtAddress": mgmtAddress,
       "mgmtLogin": mgmtLogin,
       "mgmtLogout": mgmtLogout,
       "mgmtChange": mgmtChange,
       "ifc": ifc,
       "ifcTable": ifcTable,
       "ifcEntry": ifcEntry,
       "ifcName": ifcName,
       "ifcDescr": ifcDescr,
       "ifcType": ifcType,
       "ifcPhysAddress": ifcPhysAddress,
       "ifcMtu": ifcMtu,
       "ifcSpeed": ifcSpeed,
       "ifcRxRate": ifcRxRate,
       "ifcTxRate": ifcTxRate}
)
