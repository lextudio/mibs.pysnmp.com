# SNMP MIB module (PCA-Alert-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PCA-Alert-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:03 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Symantec_ObjectIdentity = ObjectIdentity
symantec = _Symantec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 393)
)
_Pcanywhere_ObjectIdentity = ObjectIdentity
pcanywhere = _Pcanywhere_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 393, 100)
)
_Pcaversionnine_ObjectIdentity = ObjectIdentity
pcaversionnine = _Pcaversionnine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 393, 100, 9)
)
_PcaHost_ObjectIdentity = ObjectIdentity
pcaHost = _PcaHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1)
)
_PcaRemote_ObjectIdentity = ObjectIdentity
pcaRemote = _PcaRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 2)
)
_PcaFileXfer_ObjectIdentity = ObjectIdentity
pcaFileXfer = _PcaFileXfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 3)
)
_PcaGateway_ObjectIdentity = ObjectIdentity
pcaGateway = _PcaGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 4)
)
_PcaMonitor_ObjectIdentity = ObjectIdentity
pcaMonitor = _PcaMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 5)
)
_PcaInstall_ObjectIdentity = ObjectIdentity
pcaInstall = _PcaInstall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 6)
)
_PcaReset_ObjectIdentity = ObjectIdentity
pcaReset = _PcaReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 7)
)
_PcaLDAP_ObjectIdentity = ObjectIdentity
pcaLDAP = _PcaLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 8)
)
_PcaObject_ObjectIdentity = ObjectIdentity
pcaObject = _PcaObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9)
)


class _HostComputerName_Type(DisplayString):
    """Custom type hostComputerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HostComputerName_Type.__name__ = "DisplayString"
_HostComputerName_Object = MibScalar
hostComputerName = _HostComputerName_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 1),
    _HostComputerName_Type()
)
hostComputerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostComputerName.setStatus("optional")


class _RemoteComputerName_Type(DisplayString):
    """Custom type remoteComputerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RemoteComputerName_Type.__name__ = "DisplayString"
_RemoteComputerName_Object = MibScalar
remoteComputerName = _RemoteComputerName_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 2),
    _RemoteComputerName_Type()
)
remoteComputerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteComputerName.setStatus("optional")


class _CallerName_Type(DisplayString):
    """Custom type callerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CallerName_Type.__name__ = "DisplayString"
_CallerName_Object = MibScalar
callerName = _CallerName_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 3),
    _CallerName_Type()
)
callerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callerName.setStatus("optional")


class _HostConnectionObject_Type(DisplayString):
    """Custom type hostConnectionObject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HostConnectionObject_Type.__name__ = "DisplayString"
_HostConnectionObject_Object = MibScalar
hostConnectionObject = _HostConnectionObject_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 4),
    _HostConnectionObject_Type()
)
hostConnectionObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostConnectionObject.setStatus("optional")


class _RemoteConnectionObject_Type(DisplayString):
    """Custom type remoteConnectionObject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RemoteConnectionObject_Type.__name__ = "DisplayString"
_RemoteConnectionObject_Object = MibScalar
remoteConnectionObject = _RemoteConnectionObject_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 5),
    _RemoteConnectionObject_Type()
)
remoteConnectionObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteConnectionObject.setStatus("optional")
_XferFiles_Type = Integer32
_XferFiles_Object = MibScalar
xferFiles = _XferFiles_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 6),
    _XferFiles_Type()
)
xferFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xferFiles.setStatus("optional")
_XferBytes_Type = Integer32
_XferBytes_Object = MibScalar
xferBytes = _XferBytes_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 7),
    _XferBytes_Type()
)
xferBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xferBytes.setStatus("optional")
_XferOperation_Type = Integer32
_XferOperation_Object = MibScalar
xferOperation = _XferOperation_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 8),
    _XferOperation_Type()
)
xferOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xferOperation.setStatus("optional")
_XferVirusFlag_Type = Integer32
_XferVirusFlag_Object = MibScalar
xferVirusFlag = _XferVirusFlag_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 9),
    _XferVirusFlag_Type()
)
xferVirusFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xferVirusFlag.setStatus("optional")


class _XferSourceFile_Type(DisplayString):
    """Custom type xferSourceFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XferSourceFile_Type.__name__ = "DisplayString"
_XferSourceFile_Object = MibScalar
xferSourceFile = _XferSourceFile_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 10),
    _XferSourceFile_Type()
)
xferSourceFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xferSourceFile.setStatus("optional")


class _XferDestFile_Type(DisplayString):
    """Custom type xferDestFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XferDestFile_Type.__name__ = "DisplayString"
_XferDestFile_Object = MibScalar
xferDestFile = _XferDestFile_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 11),
    _XferDestFile_Type()
)
xferDestFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xferDestFile.setStatus("optional")
_HostEncryptionLevel_Type = Integer32
_HostEncryptionLevel_Object = MibScalar
hostEncryptionLevel = _HostEncryptionLevel_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 12),
    _HostEncryptionLevel_Type()
)
hostEncryptionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostEncryptionLevel.setStatus("optional")
_RemoteEncryptionLevel_Type = Integer32
_RemoteEncryptionLevel_Object = MibScalar
remoteEncryptionLevel = _RemoteEncryptionLevel_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 13),
    _RemoteEncryptionLevel_Type()
)
remoteEncryptionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteEncryptionLevel.setStatus("optional")
_HostEndedReason_Type = Integer32
_HostEndedReason_Object = MibScalar
hostEndedReason = _HostEndedReason_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 14),
    _HostEndedReason_Type()
)
hostEndedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostEndedReason.setStatus("optional")
_DeviceType_Type = Integer32
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 15),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("optional")
_XFerFailedFlag_Type = Integer32
_XFerFailedFlag_Object = MibScalar
xFerFailedFlag = _XFerFailedFlag_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 16),
    _XFerFailedFlag_Type()
)
xFerFailedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xFerFailedFlag.setStatus("optional")


class _EncryptionErrorMessage_Type(DisplayString):
    """Custom type encryptionErrorMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EncryptionErrorMessage_Type.__name__ = "DisplayString"
_EncryptionErrorMessage_Object = MibScalar
encryptionErrorMessage = _EncryptionErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 17),
    _EncryptionErrorMessage_Type()
)
encryptionErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionErrorMessage.setStatus("optional")


class _P3SerialNumber_Type(DisplayString):
    """Custom type p3SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_P3SerialNumber_Type.__name__ = "DisplayString"
_P3SerialNumber_Object = MibScalar
p3SerialNumber = _P3SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 18),
    _P3SerialNumber_Type()
)
p3SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p3SerialNumber.setStatus("optional")


class _SystemName_Type(DisplayString):
    """Custom type systemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemName_Type.__name__ = "DisplayString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 9, 19),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("optional")

# Managed Objects groups


# Notification objects

pcaHostStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1, 0, 1)
)
pcaHostStarted.setObjects(
      *(("PCA-Alert-MIB", "deviceType"),
        ("PCA-Alert-MIB", "hostConnectionObject"),
        ("PCA-Alert-MIB", "p3SerialNumber"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaHostStarted.setStatus(
        ""
    )

pcaHostEndSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1, 0, 2)
)
pcaHostEndSession.setObjects(
      *(("PCA-Alert-MIB", "hostEndedReason"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaHostEndSession.setStatus(
        ""
    )

pcaHostAbnormalEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1, 0, 3)
)
if mibBuilder.loadTexts:
    pcaHostAbnormalEnd.setStatus(
        ""
    )

pcaHostConnFailDeviceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1, 0, 4)
)
pcaHostConnFailDeviceError.setObjects(
      *(("PCA-Alert-MIB", "deviceType"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaHostConnFailDeviceError.setStatus(
        ""
    )

pcaHostStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1, 0, 5)
)
pcaHostStopped.setObjects(
      *(("PCA-Alert-MIB", "hostEndedReason"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaHostStopped.setStatus(
        ""
    )

pcaHostInSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1, 0, 6)
)
pcaHostInSession.setObjects(
      *(("PCA-Alert-MIB", "remoteComputerName"),
        ("PCA-Alert-MIB", "callerName"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaHostInSession.setStatus(
        ""
    )

pcaHostConnFailAccessDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1, 0, 7)
)
pcaHostConnFailAccessDenied.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaHostConnFailAccessDenied.setStatus(
        ""
    )

pcaHostConnFailEncrypt = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1, 0, 8)
)
pcaHostConnFailEncrypt.setObjects(
      *(("PCA-Alert-MIB", "encryptionErrorMessage"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaHostConnFailEncrypt.setStatus(
        ""
    )

pcaHostUnsecuredHostStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1, 0, 9)
)
pcaHostUnsecuredHostStarted.setObjects(
      *(("PCA-Alert-MIB", "hostConnectionObject"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaHostUnsecuredHostStarted.setStatus(
        ""
    )

pcaHostRebooting = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1, 0, 10)
)
pcaHostRebooting.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaHostRebooting.setStatus(
        ""
    )

pcaHostLockingWorkstation = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1, 0, 11)
)
pcaHostLockingWorkstation.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaHostLockingWorkstation.setStatus(
        ""
    )

pcaHostLoggingOffUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 1, 0, 12)
)
pcaHostLoggingOffUser.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaHostLoggingOffUser.setStatus(
        ""
    )

pcaRemoteStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 2, 0, 1)
)
pcaRemoteStarted.setObjects(
      *(("PCA-Alert-MIB", "deviceType"),
        ("PCA-Alert-MIB", "remoteConnectionObject"),
        ("PCA-Alert-MIB", "p3SerialNumber"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaRemoteStarted.setStatus(
        ""
    )

pcaRemoteInSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 2, 0, 2)
)
pcaRemoteInSession.setObjects(
      *(("PCA-Alert-MIB", "hostComputerName"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaRemoteInSession.setStatus(
        ""
    )

pcaRemoteEndSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 2, 0, 3)
)
pcaRemoteEndSession.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaRemoteEndSession.setStatus(
        ""
    )

pcaRemoteAbnormalEndSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 2, 0, 4)
)
pcaRemoteAbnormalEndSession.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaRemoteAbnormalEndSession.setStatus(
        ""
    )

pcaRemoteConnFailDeviceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 2, 0, 5)
)
pcaRemoteConnFailDeviceError.setObjects(
      *(("PCA-Alert-MIB", "deviceType"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaRemoteConnFailDeviceError.setStatus(
        ""
    )

pcaRemoteConnFailHostBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 2, 0, 6)
)
pcaRemoteConnFailHostBusy.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaRemoteConnFailHostBusy.setStatus(
        ""
    )

pcaRemoteConnFailHostNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 2, 0, 7)
)
pcaRemoteConnFailHostNotFound.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaRemoteConnFailHostNotFound.setStatus(
        ""
    )

pcaRemoteConnFailBadPassword = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 2, 0, 8)
)
pcaRemoteConnFailBadPassword.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaRemoteConnFailBadPassword.setStatus(
        ""
    )

pcaRemoteConnFailEncryption = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 2, 0, 9)
)
pcaRemoteConnFailEncryption.setObjects(
      *(("PCA-Alert-MIB", "encryptionErrorMessage"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaRemoteConnFailEncryption.setStatus(
        ""
    )

pcaFileXferStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 3, 0, 1)
)
pcaFileXferStarted.setObjects(
      *(("PCA-Alert-MIB", "hostComputerName"),
        ("PCA-Alert-MIB", "remoteComputerName"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaFileXferStarted.setStatus(
        ""
    )

pcaFileXferEnded = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 3, 0, 2)
)
pcaFileXferEnded.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaFileXferEnded.setStatus(
        ""
    )

pcaFileXferAbnormalEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 3, 0, 3)
)
pcaFileXferAbnormalEnd.setObjects(
      *(("PCA-Alert-MIB", "hostComputerName"),
        ("PCA-Alert-MIB", "remoteComputerName"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaFileXferAbnormalEnd.setStatus(
        ""
    )

pcaFileXferOperationCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 3, 0, 4)
)
pcaFileXferOperationCancelled.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaFileXferOperationCancelled.setStatus(
        ""
    )

pcaFileXferOperation = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 3, 0, 5)
)
pcaFileXferOperation.setObjects(
      *(("PCA-Alert-MIB", "xferOperation"),
        ("PCA-Alert-MIB", "xferSourceFile"),
        ("PCA-Alert-MIB", "xferDestFile"),
        ("PCA-Alert-MIB", "xferBytes"),
        ("PCA-Alert-MIB", "xferVirusFlag"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaFileXferOperation.setStatus(
        ""
    )

pcaFileXferVirusFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 3, 0, 6)
)
pcaFileXferVirusFound.setObjects(
      *(("PCA-Alert-MIB", "xferSourceFile"),
        ("PCA-Alert-MIB", "systemName"))
)
if mibBuilder.loadTexts:
    pcaFileXferVirusFound.setStatus(
        ""
    )

pcaMonitorFullProductNotInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 5, 0, 1)
)
pcaMonitorFullProductNotInstalled.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaMonitorFullProductNotInstalled.setStatus(
        ""
    )

pcaMonitorHostNotInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 5, 0, 2)
)
pcaMonitorHostNotInstalled.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaMonitorHostNotInstalled.setStatus(
        ""
    )

pcaMonitorRemoteNotInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 5, 0, 3)
)
pcaMonitorRemoteNotInstalled.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaMonitorRemoteNotInstalled.setStatus(
        ""
    )

pcaMonitorHostNotWaiting = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 5, 0, 4)
)
pcaMonitorHostNotWaiting.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaMonitorHostNotWaiting.setStatus(
        ""
    )

pcaMonitorHostNotAutoStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 5, 0, 5)
)
pcaMonitorHostNotAutoStart.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaMonitorHostNotAutoStart.setStatus(
        ""
    )

pcaMonitorHostNotWaitingOnDialup = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 5, 0, 6)
)
pcaMonitorHostNotWaitingOnDialup.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaMonitorHostNotWaitingOnDialup.setStatus(
        ""
    )

pcaMonitorHostLanOnlyNotInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 5, 0, 7)
)
pcaMonitorHostLanOnlyNotInstalled.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaMonitorHostLanOnlyNotInstalled.setStatus(
        ""
    )

pcaMonitorLiveUpdateNotRun = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 5, 0, 8)
)
pcaMonitorLiveUpdateNotRun.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaMonitorLiveUpdateNotRun.setStatus(
        ""
    )

pcaInstallRebootRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 6, 0, 1)
)
pcaInstallRebootRequired.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaInstallRebootRequired.setStatus(
        ""
    )

pcaResetNotInstalledReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 7, 0, 1)
)
pcaResetNotInstalledReset.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaResetNotInstalledReset.setStatus(
        ""
    )

pcaResetHostNotWaitingReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 7, 0, 2)
)
pcaResetHostNotWaitingReset.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaResetHostNotWaitingReset.setStatus(
        ""
    )

pcaResetHostNotAutoStartReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 7, 0, 3)
)
pcaResetHostNotAutoStartReset.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaResetHostNotAutoStartReset.setStatus(
        ""
    )

pcaResetHostWaitingOnDialupReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 7, 0, 4)
)
pcaResetHostWaitingOnDialupReset.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaResetHostWaitingOnDialupReset.setStatus(
        ""
    )

pcaResetLiveUpdateNotRunReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 393, 100, 9, 7, 0, 5)
)
pcaResetLiveUpdateNotRunReset.setObjects(
    ("PCA-Alert-MIB", "systemName")
)
if mibBuilder.loadTexts:
    pcaResetLiveUpdateNotRunReset.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PCA-Alert-MIB",
    **{"symantec": symantec,
       "pcanywhere": pcanywhere,
       "pcaversionnine": pcaversionnine,
       "pcaHost": pcaHost,
       "pcaHostStarted": pcaHostStarted,
       "pcaHostEndSession": pcaHostEndSession,
       "pcaHostAbnormalEnd": pcaHostAbnormalEnd,
       "pcaHostConnFailDeviceError": pcaHostConnFailDeviceError,
       "pcaHostStopped": pcaHostStopped,
       "pcaHostInSession": pcaHostInSession,
       "pcaHostConnFailAccessDenied": pcaHostConnFailAccessDenied,
       "pcaHostConnFailEncrypt": pcaHostConnFailEncrypt,
       "pcaHostUnsecuredHostStarted": pcaHostUnsecuredHostStarted,
       "pcaHostRebooting": pcaHostRebooting,
       "pcaHostLockingWorkstation": pcaHostLockingWorkstation,
       "pcaHostLoggingOffUser": pcaHostLoggingOffUser,
       "pcaRemote": pcaRemote,
       "pcaRemoteStarted": pcaRemoteStarted,
       "pcaRemoteInSession": pcaRemoteInSession,
       "pcaRemoteEndSession": pcaRemoteEndSession,
       "pcaRemoteAbnormalEndSession": pcaRemoteAbnormalEndSession,
       "pcaRemoteConnFailDeviceError": pcaRemoteConnFailDeviceError,
       "pcaRemoteConnFailHostBusy": pcaRemoteConnFailHostBusy,
       "pcaRemoteConnFailHostNotFound": pcaRemoteConnFailHostNotFound,
       "pcaRemoteConnFailBadPassword": pcaRemoteConnFailBadPassword,
       "pcaRemoteConnFailEncryption": pcaRemoteConnFailEncryption,
       "pcaFileXfer": pcaFileXfer,
       "pcaFileXferStarted": pcaFileXferStarted,
       "pcaFileXferEnded": pcaFileXferEnded,
       "pcaFileXferAbnormalEnd": pcaFileXferAbnormalEnd,
       "pcaFileXferOperationCancelled": pcaFileXferOperationCancelled,
       "pcaFileXferOperation": pcaFileXferOperation,
       "pcaFileXferVirusFound": pcaFileXferVirusFound,
       "pcaGateway": pcaGateway,
       "pcaMonitor": pcaMonitor,
       "pcaMonitorFullProductNotInstalled": pcaMonitorFullProductNotInstalled,
       "pcaMonitorHostNotInstalled": pcaMonitorHostNotInstalled,
       "pcaMonitorRemoteNotInstalled": pcaMonitorRemoteNotInstalled,
       "pcaMonitorHostNotWaiting": pcaMonitorHostNotWaiting,
       "pcaMonitorHostNotAutoStart": pcaMonitorHostNotAutoStart,
       "pcaMonitorHostNotWaitingOnDialup": pcaMonitorHostNotWaitingOnDialup,
       "pcaMonitorHostLanOnlyNotInstalled": pcaMonitorHostLanOnlyNotInstalled,
       "pcaMonitorLiveUpdateNotRun": pcaMonitorLiveUpdateNotRun,
       "pcaInstall": pcaInstall,
       "pcaInstallRebootRequired": pcaInstallRebootRequired,
       "pcaReset": pcaReset,
       "pcaResetNotInstalledReset": pcaResetNotInstalledReset,
       "pcaResetHostNotWaitingReset": pcaResetHostNotWaitingReset,
       "pcaResetHostNotAutoStartReset": pcaResetHostNotAutoStartReset,
       "pcaResetHostWaitingOnDialupReset": pcaResetHostWaitingOnDialupReset,
       "pcaResetLiveUpdateNotRunReset": pcaResetLiveUpdateNotRunReset,
       "pcaLDAP": pcaLDAP,
       "pcaObject": pcaObject,
       "hostComputerName": hostComputerName,
       "remoteComputerName": remoteComputerName,
       "callerName": callerName,
       "hostConnectionObject": hostConnectionObject,
       "remoteConnectionObject": remoteConnectionObject,
       "xferFiles": xferFiles,
       "xferBytes": xferBytes,
       "xferOperation": xferOperation,
       "xferVirusFlag": xferVirusFlag,
       "xferSourceFile": xferSourceFile,
       "xferDestFile": xferDestFile,
       "hostEncryptionLevel": hostEncryptionLevel,
       "remoteEncryptionLevel": remoteEncryptionLevel,
       "hostEndedReason": hostEndedReason,
       "deviceType": deviceType,
       "xFerFailedFlag": xFerFailedFlag,
       "encryptionErrorMessage": encryptionErrorMessage,
       "p3SerialNumber": p3SerialNumber,
       "systemName": systemName}
)
