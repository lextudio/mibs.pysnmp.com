# SNMP MIB module (NetWare-Server-Alarm-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NetWare-Server-Alarm-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:07 2024
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

(InternationalDisplayString,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString")

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



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Nwalarm_mib_ObjectIdentity = ObjectIdentity
nwalarm_mib = _Nwalarm_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 10)
)
_Trapinfo_ObjectIdentity = ObjectIdentity
trapinfo = _Trapinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1)
)
_MemoryAddress_Type = Integer32
_MemoryAddress_Object = MibScalar
memoryAddress = _MemoryAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 1),
    _MemoryAddress_Type()
)
memoryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    memoryAddress.setStatus("mandatory")
_AuditEventNumber_Type = Integer32
_AuditEventNumber_Object = MibScalar
auditEventNumber = _AuditEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 2),
    _AuditEventNumber_Type()
)
auditEventNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    auditEventNumber.setStatus("mandatory")
_BlockNumber_Type = Integer32
_BlockNumber_Object = MibScalar
blockNumber = _BlockNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 3),
    _BlockNumber_Type()
)
blockNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blockNumber.setStatus("mandatory")
_NumberOfBlocks_Type = Integer32
_NumberOfBlocks_Object = MibScalar
numberOfBlocks = _NumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 4),
    _NumberOfBlocks_Type()
)
numberOfBlocks.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numberOfBlocks.setStatus("mandatory")
_PacketSize_Type = Integer32
_PacketSize_Object = MibScalar
packetSize = _PacketSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 5),
    _PacketSize_Type()
)
packetSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    packetSize.setStatus("mandatory")
_BoardNumber_Type = Integer32
_BoardNumber_Object = MibScalar
boardNumber = _BoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 6),
    _BoardNumber_Type()
)
boardNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardNumber.setStatus("mandatory")
_CodeOffset_Type = Integer32
_CodeOffset_Object = MibScalar
codeOffset = _CodeOffset_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 7),
    _CodeOffset_Type()
)
codeOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    codeOffset.setStatus("mandatory")
_ConnectionNumber_Type = Integer32
_ConnectionNumber_Object = MibScalar
connectionNumber = _ConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 8),
    _ConnectionNumber_Type()
)
connectionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connectionNumber.setStatus("mandatory")
_DataStreamNumber_Type = Integer32
_DataStreamNumber_Object = MibScalar
dataStreamNumber = _DataStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 9),
    _DataStreamNumber_Type()
)
dataStreamNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataStreamNumber.setStatus("mandatory")
_DiskSpace_Type = Integer32
_DiskSpace_Object = MibScalar
diskSpace = _DiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 10),
    _DiskSpace_Type()
)
diskSpace.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskSpace.setStatus("mandatory")


class _DomainName_Type(InternationalDisplayString):
    """Custom type domainName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DomainName_Type.__name__ = "InternationalDisplayString"
_DomainName_Object = MibScalar
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 11),
    _DomainName_Type()
)
domainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    domainName.setStatus("mandatory")


class _ResourceDescription_Type(InternationalDisplayString):
    """Custom type resourceDescription based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ResourceDescription_Type.__name__ = "InternationalDisplayString"
_ResourceDescription_Object = MibScalar
resourceDescription = _ResourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 12),
    _ResourceDescription_Type()
)
resourceDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    resourceDescription.setStatus("mandatory")


class _DeviceName_Type(InternationalDisplayString):
    """Custom type deviceName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DeviceName_Type.__name__ = "InternationalDisplayString"
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 13),
    _DeviceName_Type()
)
deviceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceName.setStatus("mandatory")
_DosType_Type = Integer32
_DosType_Object = MibScalar
dosType = _DosType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 14),
    _DosType_Type()
)
dosType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dosType.setStatus("mandatory")
_ErrorNumber_Type = Integer32
_ErrorNumber_Object = MibScalar
errorNumber = _ErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 15),
    _ErrorNumber_Type()
)
errorNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    errorNumber.setStatus("mandatory")


class _ExceptionName_Type(InternationalDisplayString):
    """Custom type exceptionName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExceptionName_Type.__name__ = "InternationalDisplayString"
_ExceptionName_Object = MibScalar
exceptionName = _ExceptionName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 16),
    _ExceptionName_Type()
)
exceptionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exceptionName.setStatus("mandatory")
_EipAddress_Type = Integer32
_EipAddress_Object = MibScalar
eipAddress = _EipAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 17),
    _EipAddress_Type()
)
eipAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eipAddress.setStatus("mandatory")


class _FileName_Type(InternationalDisplayString):
    """Custom type fileName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FileName_Type.__name__ = "InternationalDisplayString"
_FileName_Object = MibScalar
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 18),
    _FileName_Type()
)
fileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileName.setStatus("mandatory")


class _PathName_Type(InternationalDisplayString):
    """Custom type pathName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 124),
    )


_PathName_Type.__name__ = "InternationalDisplayString"
_PathName_Object = MibScalar
pathName = _PathName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 19),
    _PathName_Type()
)
pathName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pathName.setStatus("mandatory")
_FileOffset_Type = Integer32
_FileOffset_Object = MibScalar
fileOffset = _FileOffset_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 20),
    _FileOffset_Type()
)
fileOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileOffset.setStatus("mandatory")
_NcpFunctionNumber_Type = Integer32
_NcpFunctionNumber_Object = MibScalar
ncpFunctionNumber = _NcpFunctionNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 21),
    _NcpFunctionNumber_Type()
)
ncpFunctionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ncpFunctionNumber.setStatus("mandatory")
_FileSize_Type = Integer32
_FileSize_Object = MibScalar
fileSize = _FileSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 22),
    _FileSize_Type()
)
fileSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileSize.setStatus("mandatory")
_FileValue_Type = Integer32
_FileValue_Object = MibScalar
fileValue = _FileValue_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 23),
    _FileValue_Type()
)
fileValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileValue.setStatus("mandatory")
_FileLength_Type = Integer32
_FileLength_Object = MibScalar
fileLength = _FileLength_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 24),
    _FileLength_Type()
)
fileLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileLength.setStatus("mandatory")
_InterruptNumber_Type = Integer32
_InterruptNumber_Object = MibScalar
interruptNumber = _InterruptNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 25),
    _InterruptNumber_Type()
)
interruptNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interruptNumber.setStatus("mandatory")


class _NlmName_Type(InternationalDisplayString):
    """Custom type nlmName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_NlmName_Type.__name__ = "InternationalDisplayString"
_NlmName_Object = MibScalar
nlmName = _NlmName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 26),
    _NlmName_Type()
)
nlmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlmName.setStatus("mandatory")


class _MediaLabel_Type(InternationalDisplayString):
    """Custom type mediaLabel based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MediaLabel_Type.__name__ = "InternationalDisplayString"
_MediaLabel_Object = MibScalar
mediaLabel = _MediaLabel_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 27),
    _MediaLabel_Type()
)
mediaLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mediaLabel.setStatus("mandatory")


class _Message_Type(InternationalDisplayString):
    """Custom type message based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_Message_Type.__name__ = "InternationalDisplayString"
_Message_Object = MibScalar
message = _Message_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 28),
    _Message_Type()
)
message.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    message.setStatus("mandatory")
_NumberOfFailedMemoryAllocAttempts_Type = Integer32
_NumberOfFailedMemoryAllocAttempts_Object = MibScalar
numberOfFailedMemoryAllocAttempts = _NumberOfFailedMemoryAllocAttempts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 29),
    _NumberOfFailedMemoryAllocAttempts_Type()
)
numberOfFailedMemoryAllocAttempts.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numberOfFailedMemoryAllocAttempts.setStatus("mandatory")
_NumberOfResources_Type = Integer32
_NumberOfResources_Object = MibScalar
numberOfResources = _NumberOfResources_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 30),
    _NumberOfResources_Type()
)
numberOfResources.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numberOfResources.setStatus("mandatory")
_NetworkAddress_Type = NetNumber
_NetworkAddress_Object = MibScalar
networkAddress = _NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 31),
    _NetworkAddress_Type()
)
networkAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAddress.setStatus("mandatory")
_NumberOfFailedFileLockRequests_Type = Integer32
_NumberOfFailedFileLockRequests_Object = MibScalar
numberOfFailedFileLockRequests = _NumberOfFailedFileLockRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 32),
    _NumberOfFailedFileLockRequests_Type()
)
numberOfFailedFileLockRequests.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numberOfFailedFileLockRequests.setStatus("mandatory")


class _ProcessName_Type(InternationalDisplayString):
    """Custom type processName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ProcessName_Type.__name__ = "InternationalDisplayString"
_ProcessName_Object = MibScalar
processName = _ProcessName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 33),
    _ProcessName_Type()
)
processName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    processName.setStatus("mandatory")
_PartitionNumber_Type = Integer32
_PartitionNumber_Object = MibScalar
partitionNumber = _PartitionNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 34),
    _PartitionNumber_Type()
)
partitionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    partitionNumber.setStatus("mandatory")


class _ProtocolName_Type(InternationalDisplayString):
    """Custom type protocolName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ProtocolName_Type.__name__ = "InternationalDisplayString"
_ProtocolName_Object = MibScalar
protocolName = _ProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 35),
    _ProtocolName_Type()
)
protocolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protocolName.setStatus("mandatory")
_NumberOfPackets_Type = Integer32
_NumberOfPackets_Object = MibScalar
numberOfPackets = _NumberOfPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 36),
    _NumberOfPackets_Type()
)
numberOfPackets.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numberOfPackets.setStatus("mandatory")


class _ResourceName_Type(InternationalDisplayString):
    """Custom type resourceName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ResourceName_Type.__name__ = "InternationalDisplayString"
_ResourceName_Object = MibScalar
resourceName = _ResourceName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 37),
    _ResourceName_Type()
)
resourceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    resourceName.setStatus("mandatory")
_NumberOfFailedRecordLockRequests_Type = Integer32
_NumberOfFailedRecordLockRequests_Object = MibScalar
numberOfFailedRecordLockRequests = _NumberOfFailedRecordLockRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 38),
    _NumberOfFailedRecordLockRequests_Type()
)
numberOfFailedRecordLockRequests.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numberOfFailedRecordLockRequests.setStatus("mandatory")


class _ServerName_Type(InternationalDisplayString):
    """Custom type serverName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_ServerName_Type.__name__ = "InternationalDisplayString"
_ServerName_Object = MibScalar
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 39),
    _ServerName_Type()
)
serverName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serverName.setStatus("mandatory")
_StationNumber_Type = Integer32
_StationNumber_Object = MibScalar
stationNumber = _StationNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 40),
    _StationNumber_Type()
)
stationNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stationNumber.setStatus("mandatory")
_NetworkAddress1_Type = NetNumber
_NetworkAddress1_Object = MibScalar
networkAddress1 = _NetworkAddress1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 41),
    _NetworkAddress1_Type()
)
networkAddress1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAddress1.setStatus("mandatory")
_NcpSubFunctionNumber_Type = Integer32
_NcpSubFunctionNumber_Object = MibScalar
ncpSubFunctionNumber = _NcpSubFunctionNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 42),
    _NcpSubFunctionNumber_Type()
)
ncpSubFunctionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ncpSubFunctionNumber.setStatus("mandatory")


class _NlmSeverity_Type(Integer32):
    """Custom type nlmSeverity based on Integer32"""
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
        *(("critical", 4),
          ("fatal", 5),
          ("informational", 1),
          ("operationAborted", 6),
          ("recoverable", 3),
          ("warning", 2))
    )


_NlmSeverity_Type.__name__ = "Integer32"
_NlmSeverity_Object = MibScalar
nlmSeverity = _NlmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 43),
    _NlmSeverity_Type()
)
nlmSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlmSeverity.setStatus("mandatory")
_TrapTime_Type = Integer32
_TrapTime_Object = MibScalar
trapTime = _TrapTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 44),
    _TrapTime_Type()
)
trapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapTime.setStatus("mandatory")
_TaskNumber_Type = Integer32
_TaskNumber_Object = MibScalar
taskNumber = _TaskNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 45),
    _TaskNumber_Type()
)
taskNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    taskNumber.setStatus("mandatory")
_NumberOfTransactions_Type = Integer32
_NumberOfTransactions_Object = MibScalar
numberOfTransactions = _NumberOfTransactions_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 46),
    _NumberOfTransactions_Type()
)
numberOfTransactions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numberOfTransactions.setStatus("mandatory")
_ServerTime_Type = Integer32
_ServerTime_Object = MibScalar
serverTime = _ServerTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 47),
    _ServerTime_Type()
)
serverTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serverTime.setStatus("mandatory")


class _PathFileName_Type(InternationalDisplayString):
    """Custom type pathFileName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 124),
    )


_PathFileName_Type.__name__ = "InternationalDisplayString"
_PathFileName_Object = MibScalar
pathFileName = _PathFileName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 48),
    _PathFileName_Type()
)
pathFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pathFileName.setStatus("mandatory")


class _UserName_Type(InternationalDisplayString):
    """Custom type userName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_UserName_Type.__name__ = "InternationalDisplayString"
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 49),
    _UserName_Type()
)
userName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userName.setStatus("mandatory")


class _VolumeName_Type(InternationalDisplayString):
    """Custom type volumeName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_VolumeName_Type.__name__ = "InternationalDisplayString"
_VolumeName_Object = MibScalar
volumeName = _VolumeName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 50),
    _VolumeName_Type()
)
volumeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    volumeName.setStatus("mandatory")
_VolumeNumber_Type = Integer32
_VolumeNumber_Object = MibScalar
volumeNumber = _VolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 51),
    _VolumeNumber_Type()
)
volumeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    volumeNumber.setStatus("mandatory")


class _LanDriverName_Type(InternationalDisplayString):
    """Custom type lanDriverName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_LanDriverName_Type.__name__ = "InternationalDisplayString"
_LanDriverName_Object = MibScalar
lanDriverName = _LanDriverName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 52),
    _LanDriverName_Type()
)
lanDriverName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lanDriverName.setStatus("mandatory")


class _RouterName_Type(InternationalDisplayString):
    """Custom type routerName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RouterName_Type.__name__ = "InternationalDisplayString"
_RouterName_Object = MibScalar
routerName = _RouterName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 53),
    _RouterName_Type()
)
routerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    routerName.setStatus("mandatory")


class _MacAddress_Type(OctetString):
    """Custom type macAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MacAddress_Type.__name__ = "OctetString"
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 54),
    _MacAddress_Type()
)
macAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macAddress.setStatus("mandatory")


class _MacAddress1_Type(OctetString):
    """Custom type macAddress1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MacAddress1_Type.__name__ = "OctetString"
_MacAddress1_Object = MibScalar
macAddress1 = _MacAddress1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 55),
    _MacAddress1_Type()
)
macAddress1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macAddress1.setStatus("mandatory")
_NumberOfConnections_Type = Integer32
_NumberOfConnections_Object = MibScalar
numberOfConnections = _NumberOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 56),
    _NumberOfConnections_Type()
)
numberOfConnections.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numberOfConnections.setStatus("mandatory")
_SocketNumber_Type = Integer32
_SocketNumber_Object = MibScalar
socketNumber = _SocketNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 57),
    _SocketNumber_Type()
)
socketNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    socketNumber.setStatus("mandatory")


class _AccountName_Type(InternationalDisplayString):
    """Custom type accountName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_AccountName_Type.__name__ = "InternationalDisplayString"
_AccountName_Object = MibScalar
accountName = _AccountName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 58),
    _AccountName_Type()
)
accountName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accountName.setStatus("mandatory")
_FileMiscInfo_Type = Integer32
_FileMiscInfo_Object = MibScalar
fileMiscInfo = _FileMiscInfo_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 59),
    _FileMiscInfo_Type()
)
fileMiscInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileMiscInfo.setStatus("mandatory")


class _CallBackNumber_Type(InternationalDisplayString):
    """Custom type callBackNumber based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CallBackNumber_Type.__name__ = "InternationalDisplayString"
_CallBackNumber_Object = MibScalar
callBackNumber = _CallBackNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 60),
    _CallBackNumber_Type()
)
callBackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    callBackNumber.setStatus("mandatory")


class _BaudRate_Type(InternationalDisplayString):
    """Custom type baudRate based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_BaudRate_Type.__name__ = "InternationalDisplayString"
_BaudRate_Object = MibScalar
baudRate = _BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 61),
    _BaudRate_Type()
)
baudRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    baudRate.setStatus("mandatory")


class _ObjectName_Type(InternationalDisplayString):
    """Custom type objectName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_ObjectName_Type.__name__ = "InternationalDisplayString"
_ObjectName_Object = MibScalar
objectName = _ObjectName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 62),
    _ObjectName_Type()
)
objectName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    objectName.setStatus("mandatory")


class _UserName1_Type(InternationalDisplayString):
    """Custom type userName1 based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_UserName1_Type.__name__ = "InternationalDisplayString"
_UserName1_Object = MibScalar
userName1 = _UserName1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 63),
    _UserName1_Type()
)
userName1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userName1.setStatus("mandatory")
_DosType1_Type = Integer32
_DosType1_Object = MibScalar
dosType1 = _DosType1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 64),
    _DosType1_Type()
)
dosType1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dosType1.setStatus("mandatory")
_BlockNumber1_Type = Integer32
_BlockNumber1_Object = MibScalar
blockNumber1 = _BlockNumber1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 65),
    _BlockNumber1_Type()
)
blockNumber1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blockNumber1.setStatus("mandatory")
_InternalNetworkAddress_Type = NetNumber
_InternalNetworkAddress_Object = MibScalar
internalNetworkAddress = _InternalNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 66),
    _InternalNetworkAddress_Type()
)
internalNetworkAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    internalNetworkAddress.setStatus("mandatory")
_InternalNetworkAddress1_Type = NetNumber
_InternalNetworkAddress1_Object = MibScalar
internalNetworkAddress1 = _InternalNetworkAddress1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 67),
    _InternalNetworkAddress1_Type()
)
internalNetworkAddress1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    internalNetworkAddress1.setStatus("mandatory")


class _MacAddress2_Type(OctetString):
    """Custom type macAddress2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MacAddress2_Type.__name__ = "OctetString"
_MacAddress2_Object = MibScalar
macAddress2 = _MacAddress2_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 68),
    _MacAddress2_Type()
)
macAddress2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macAddress2.setStatus("mandatory")


class _ServerName1_Type(InternationalDisplayString):
    """Custom type serverName1 based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_ServerName1_Type.__name__ = "InternationalDisplayString"
_ServerName1_Object = MibScalar
serverName1 = _ServerName1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 69),
    _ServerName1_Type()
)
serverName1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serverName1.setStatus("mandatory")
_SocketNumber1_Type = Integer32
_SocketNumber1_Object = MibScalar
socketNumber1 = _SocketNumber1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 70),
    _SocketNumber1_Type()
)
socketNumber1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    socketNumber1.setStatus("mandatory")
_FileMiscInfo1_Type = Integer32
_FileMiscInfo1_Object = MibScalar
fileMiscInfo1 = _FileMiscInfo1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 71),
    _FileMiscInfo1_Type()
)
fileMiscInfo1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileMiscInfo1.setStatus("mandatory")
_FileSize1_Type = Integer32
_FileSize1_Object = MibScalar
fileSize1 = _FileSize1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 72),
    _FileSize1_Type()
)
fileSize1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileSize1.setStatus("mandatory")
_FileSize2_Type = Integer32
_FileSize2_Object = MibScalar
fileSize2 = _FileSize2_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 73),
    _FileSize2_Type()
)
fileSize2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileSize2.setStatus("mandatory")
_PacketSize1_Type = Integer32
_PacketSize1_Object = MibScalar
packetSize1 = _PacketSize1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 74),
    _PacketSize1_Type()
)
packetSize1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    packetSize1.setStatus("mandatory")


class _DiskName_Type(InternationalDisplayString):
    """Custom type diskName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DiskName_Type.__name__ = "InternationalDisplayString"
_DiskName_Object = MibScalar
diskName = _DiskName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 75),
    _DiskName_Type()
)
diskName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskName.setStatus("mandatory")


class _Reason_Type(InternationalDisplayString):
    """Custom type reason based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_Reason_Type.__name__ = "InternationalDisplayString"
_Reason_Object = MibScalar
reason = _Reason_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 76),
    _Reason_Type()
)
reason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    reason.setStatus("mandatory")
_MaximumPercent_Type = Integer32
_MaximumPercent_Object = MibScalar
maximumPercent = _MaximumPercent_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 77),
    _MaximumPercent_Type()
)
maximumPercent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maximumPercent.setStatus("mandatory")
_IRamLength_Type = Integer32
_IRamLength_Object = MibScalar
iRamLength = _IRamLength_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 78),
    _IRamLength_Type()
)
iRamLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iRamLength.setStatus("mandatory")
_ITimerTicks_Type = Integer32
_ITimerTicks_Object = MibScalar
iTimerTicks = _ITimerTicks_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 79),
    _ITimerTicks_Type()
)
iTimerTicks.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iTimerTicks.setStatus("mandatory")
_PollingLoops_Type = Integer32
_PollingLoops_Object = MibScalar
pollingLoops = _PollingLoops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 80),
    _PollingLoops_Type()
)
pollingLoops.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pollingLoops.setStatus("mandatory")
_IHopsCount_Type = Integer32
_IHopsCount_Object = MibScalar
iHopsCount = _IHopsCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 81),
    _IHopsCount_Type()
)
iHopsCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iHopsCount.setStatus("mandatory")
_SynchronizationRadius_Type = Integer32
_SynchronizationRadius_Object = MibScalar
synchronizationRadius = _SynchronizationRadius_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 82),
    _SynchronizationRadius_Type()
)
synchronizationRadius.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    synchronizationRadius.setStatus("mandatory")


class _CmmndLnPrmtr_Type(InternationalDisplayString):
    """Custom type cmmndLnPrmtr based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CmmndLnPrmtr_Type.__name__ = "InternationalDisplayString"
_CmmndLnPrmtr_Object = MibScalar
cmmndLnPrmtr = _CmmndLnPrmtr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 83),
    _CmmndLnPrmtr_Type()
)
cmmndLnPrmtr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmndLnPrmtr.setStatus("mandatory")
_VolumePercentage_Type = Integer32
_VolumePercentage_Object = MibScalar
volumePercentage = _VolumePercentage_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 84),
    _VolumePercentage_Type()
)
volumePercentage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    volumePercentage.setStatus("mandatory")


class _SzReason_Type(InternationalDisplayString):
    """Custom type szReason based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_SzReason_Type.__name__ = "InternationalDisplayString"
_SzReason_Object = MibScalar
szReason = _SzReason_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 85),
    _SzReason_Type()
)
szReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    szReason.setStatus("mandatory")
_IRamStart_Type = Integer32
_IRamStart_Object = MibScalar
iRamStart = _IRamStart_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 1, 86),
    _IRamStart_Type()
)
iRamStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iRamStart.setStatus("mandatory")

# Managed Objects groups


# Notification objects

outOfShortTermMemoryRequestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 1)
)
outOfShortTermMemoryRequestFailed.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "numberOfFailedMemoryAllocAttempts"))
)
if mibBuilder.loadTexts:
    outOfShortTermMemoryRequestFailed.setStatus(
        ""
    )

errWritingToTheExtendedDirSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 2)
)
errWritingToTheExtendedDirSpace.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errWritingToTheExtendedDirSpace.setStatus(
        ""
    )

errWritingToFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 3)
)
errWritingToFile.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "dataStreamNumber"))
)
if mibBuilder.loadTexts:
    errWritingToFile.setStatus(
        ""
    )

errWritingToFileUsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 4)
)
errWritingToFileUsr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "dataStreamNumber"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    errWritingToFileUsr.setStatus(
        ""
    )

errWritingToFileDataStream = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 5)
)
errWritingToFileDataStream.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "fileName"),
        ("NetWare-Server-Alarm-MIB", "dataStreamNumber"),
        ("NetWare-Server-Alarm-MIB", "volumeName"),
        ("NetWare-Server-Alarm-MIB", "pathName"))
)
if mibBuilder.loadTexts:
    errWritingToFileDataStream.setStatus(
        ""
    )

errWritingToFileDataStreamUsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 6)
)
errWritingToFileDataStreamUsr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "fileName"),
        ("NetWare-Server-Alarm-MIB", "dataStreamNumber"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "volumeName"),
        ("NetWare-Server-Alarm-MIB", "pathName"))
)
if mibBuilder.loadTexts:
    errWritingToFileDataStreamUsr.setStatus(
        ""
    )

fileReaderrSrvrNofileName = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 7)
)
fileReaderrSrvrNofileName.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "fileOffset"),
        ("NetWare-Server-Alarm-MIB", "dataStreamNumber"))
)
if mibBuilder.loadTexts:
    fileReaderrSrvrNofileName.setStatus(
        ""
    )

fileReaderrUsrNofileName = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 8)
)
fileReaderrUsrNofileName.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "fileOffset"),
        ("NetWare-Server-Alarm-MIB", "dataStreamNumber"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    fileReaderrUsrNofileName.setStatus(
        ""
    )

fileReaderrDSSrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 9)
)
fileReaderrDSSrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "fileName"),
        ("NetWare-Server-Alarm-MIB", "fileOffset"),
        ("NetWare-Server-Alarm-MIB", "dataStreamNumber"),
        ("NetWare-Server-Alarm-MIB", "volumeName"),
        ("NetWare-Server-Alarm-MIB", "pathName"))
)
if mibBuilder.loadTexts:
    fileReaderrDSSrvr.setStatus(
        ""
    )

fileReaderrDSUsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 10)
)
fileReaderrDSUsr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "fileName"),
        ("NetWare-Server-Alarm-MIB", "fileOffset"),
        ("NetWare-Server-Alarm-MIB", "dataStreamNumber"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "volumeName"),
        ("NetWare-Server-Alarm-MIB", "pathName"))
)
if mibBuilder.loadTexts:
    fileReaderrDSUsr.setStatus(
        ""
    )

fileWritePreReaderrSrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 11)
)
fileWritePreReaderrSrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "fileOffset"),
        ("NetWare-Server-Alarm-MIB", "dataStreamNumber"))
)
if mibBuilder.loadTexts:
    fileWritePreReaderrSrvr.setStatus(
        ""
    )

fileWritePreReaderrUsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 12)
)
fileWritePreReaderrUsr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "fileOffset"),
        ("NetWare-Server-Alarm-MIB", "dataStreamNumber"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    fileWritePreReaderrUsr.setStatus(
        ""
    )

fileWritePreReaderrDSSrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 13)
)
fileWritePreReaderrDSSrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "fileName"),
        ("NetWare-Server-Alarm-MIB", "fileOffset"),
        ("NetWare-Server-Alarm-MIB", "dataStreamNumber"),
        ("NetWare-Server-Alarm-MIB", "volumeName"),
        ("NetWare-Server-Alarm-MIB", "pathName"))
)
if mibBuilder.loadTexts:
    fileWritePreReaderrDSSrvr.setStatus(
        ""
    )

fileWritePreReaderrDSUsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 14)
)
fileWritePreReaderrDSUsr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "fileName"),
        ("NetWare-Server-Alarm-MIB", "fileOffset"),
        ("NetWare-Server-Alarm-MIB", "dataStreamNumber"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "volumeName"),
        ("NetWare-Server-Alarm-MIB", "pathName"))
)
if mibBuilder.loadTexts:
    fileWritePreReaderrDSUsr.setStatus(
        ""
    )

cacheMemAllocExceededMinLeftLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 15)
)
cacheMemAllocExceededMinLeftLimit.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    cacheMemAllocExceededMinLeftLimit.setStatus(
        ""
    )

cacheMemAllocOutOfMem = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 16)
)
cacheMemAllocOutOfMem.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    cacheMemAllocOutOfMem.setStatus(
        ""
    )

numberOfCacheBuffersGettingLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 17)
)
numberOfCacheBuffersGettingLow.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    numberOfCacheBuffersGettingLow.setStatus(
        ""
    )

volOfDiskSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 18)
)
volOfDiskSpace.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    volOfDiskSpace.setStatus(
        ""
    )

volOfDiskSpaceNoPurge = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 19)
)
volOfDiskSpaceNoPurge.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"),
        ("NetWare-Server-Alarm-MIB", "diskSpace"))
)
if mibBuilder.loadTexts:
    volOfDiskSpaceNoPurge.setStatus(
        ""
    )

volAlmostOutOfDiskSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 20)
)
volAlmostOutOfDiskSpace.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    volAlmostOutOfDiskSpace.setStatus(
        ""
    )

errWritingFatTables = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 21)
)
errWritingFatTables.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    errWritingFatTables.setStatus(
        ""
    )

errWritingDirectoryBlk = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 22)
)
errWritingDirectoryBlk.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    errWritingDirectoryBlk.setStatus(
        ""
    )

dirCopyReadErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 23)
)
dirCopyReadErr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    dirCopyReadErr.setStatus(
        ""
    )

errReadingBothCopiesofDir = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 24)
)
errReadingBothCopiesofDir.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    errReadingBothCopiesofDir.setStatus(
        ""
    )

allocateDirEntryWriteError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 25)
)
allocateDirEntryWriteError.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    allocateDirEntryWriteError.setStatus(
        ""
    )

errExpandingDirDuetoWriteErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 26)
)
errExpandingDirDuetoWriteErr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    errExpandingDirDuetoWriteErr.setStatus(
        ""
    )

dirReachedItsLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 27)
)
dirReachedItsLimit.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    dirReachedItsLimit.setStatus(
        ""
    )

errExpandingNoDiskSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 28)
)
errExpandingNoDiskSpace.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    errExpandingNoDiskSpace.setStatus(
        ""
    )

errExpandingNoMemSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 29)
)
errExpandingNoMemSpace.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    errExpandingNoMemSpace.setStatus(
        ""
    )

dirSizeGettingTooLrgeForMem = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 30)
)
dirSizeGettingTooLrgeForMem.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    dirSizeGettingTooLrgeForMem.setStatus(
        ""
    )

lanReceiveBuffLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 31)
)
lanReceiveBuffLimitReached.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    lanReceiveBuffLimitReached.setStatus(
        ""
    )

connTerminatedByWatchDog = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 32)
)
connTerminatedByWatchDog.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    connTerminatedByWatchDog.setStatus(
        ""
    )

copyrightViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 33)
)
copyrightViolation.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    copyrightViolation.setStatus(
        ""
    )

writeFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 34)
)
writeFault.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "processName"),
        ("NetWare-Server-Alarm-MIB", "nlmName"),
        ("NetWare-Server-Alarm-MIB", "codeOffset"),
        ("NetWare-Server-Alarm-MIB", "memoryAddress"))
)
if mibBuilder.loadTexts:
    writeFault.setStatus(
        ""
    )

readFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 35)
)
readFault.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "processName"),
        ("NetWare-Server-Alarm-MIB", "nlmName"),
        ("NetWare-Server-Alarm-MIB", "codeOffset"),
        ("NetWare-Server-Alarm-MIB", "memoryAddress"))
)
if mibBuilder.loadTexts:
    readFault.setStatus(
        ""
    )

ipxReceivedIncomPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 36)
)
ipxReceivedIncomPacket.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"),
        ("NetWare-Server-Alarm-MIB", "numberOfPackets"))
)
if mibBuilder.loadTexts:
    ipxReceivedIncomPacket.setStatus(
        ""
    )

unableToCreateVOLERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 37)
)
unableToCreateVOLERR.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    unableToCreateVOLERR.setStatus(
        ""
    )

unableToWriteVOLERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 38)
)
unableToWriteVOLERR.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    unableToWriteVOLERR.setStatus(
        ""
    )

volOprDespiteDeviceDriveDeact = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 39)
)
volOprDespiteDeviceDriveDeact.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    volOprDespiteDeviceDriveDeact.setStatus(
        ""
    )

loginDisabledByUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 40)
)
loginDisabledByUser.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    loginDisabledByUser.setStatus(
        ""
    )

loginEnabledByUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 41)
)
loginEnabledByUser.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    loginEnabledByUser.setStatus(
        ""
    )

clrStnByConsole = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 42)
)
clrStnByConsole.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    clrStnByConsole.setStatus(
        ""
    )

clrStnByUsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 43)
)
clrStnByUsr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "connectionNumber"),
        ("NetWare-Server-Alarm-MIB", "userName1"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    clrStnByUsr.setStatus(
        ""
    )

fileServerDowned = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 44)
)
fileServerDowned.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    fileServerDowned.setStatus(
        ""
    )

errOpeningRIPSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 45)
)
errOpeningRIPSocket.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errOpeningRIPSocket.setStatus(
        ""
    )

rtrConfigErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 46)
)
rtrConfigErr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "macAddress"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "networkAddress1"))
)
if mibBuilder.loadTexts:
    rtrConfigErr.setStatus(
        ""
    )

lanDriverLoopBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 47)
)
lanDriverLoopBack.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"))
)
if mibBuilder.loadTexts:
    lanDriverLoopBack.setStatus(
        ""
    )

dupInternetAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 48)
)
dupInternetAddr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    dupInternetAddr.setStatus(
        ""
    )

lanBdUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 49)
)
lanBdUnreachable.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"))
)
if mibBuilder.loadTexts:
    lanBdUnreachable.setStatus(
        ""
    )

ipxUnbndRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 50)
)
ipxUnbndRequest.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"))
)
if mibBuilder.loadTexts:
    ipxUnbndRequest.setStatus(
        ""
    )

errOpeningSAPSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 51)
)
errOpeningSAPSocket.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errOpeningSAPSocket.setStatus(
        ""
    )

rtrClaimingSameInterAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 52)
)
rtrClaimingSameInterAddr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "routerName"))
)
if mibBuilder.loadTexts:
    rtrClaimingSameInterAddr.setStatus(
        ""
    )

spuriousInt = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 53)
)
spuriousInt.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "interruptNumber"))
)
if mibBuilder.loadTexts:
    spuriousInt.setStatus(
        ""
    )

checksumInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 54)
)
checksumInvalid.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    checksumInvalid.setStatus(
        ""
    )

prmyPicLostInterrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 55)
)
prmyPicLostInterrupt.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    prmyPicLostInterrupt.setStatus(
        ""
    )

scndryPicLostInterrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 56)
)
scndryPicLostInterrupt.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    scndryPicLostInterrupt.setStatus(
        ""
    )

exception = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 57)
)
exception.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "domainName"),
        ("NetWare-Server-Alarm-MIB", "processName"),
        ("NetWare-Server-Alarm-MIB", "nlmName"),
        ("NetWare-Server-Alarm-MIB", "codeOffset"))
)
if mibBuilder.loadTexts:
    exception.setStatus(
        ""
    )

invalidScreenID = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 58)
)
invalidScreenID.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "nlmName"),
        ("NetWare-Server-Alarm-MIB", "codeOffset"))
)
if mibBuilder.loadTexts:
    invalidScreenID.setStatus(
        ""
    )

prssDidNotRelqhCntlFqtly = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 59)
)
prssDidNotRelqhCntlFqtly.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "processName"),
        ("NetWare-Server-Alarm-MIB", "nlmName"),
        ("NetWare-Server-Alarm-MIB", "codeOffset"))
)
if mibBuilder.loadTexts:
    prssDidNotRelqhCntlFqtly.setStatus(
        ""
    )

fileSrvrUsrDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 60)
)
fileSrvrUsrDeleted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"))
)
if mibBuilder.loadTexts:
    fileSrvrUsrDeleted.setStatus(
        ""
    )

usrAcctDeletedByAUsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 61)
)
usrAcctDeletedByAUsr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "accountName"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "numberOfConnections"))
)
if mibBuilder.loadTexts:
    usrAcctDeletedByAUsr.setStatus(
        ""
    )

invalidResourceTag = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 62)
)
invalidResourceTag.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    invalidResourceTag.setStatus(
        ""
    )

diskDeactivatedUnknownReason = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 63)
)
diskDeactivatedUnknownReason.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    diskDeactivatedUnknownReason.setStatus(
        ""
    )

diskDeactivatedDriverUnload = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 64)
)
diskDeactivatedDriverUnload.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    diskDeactivatedDriverUnload.setStatus(
        ""
    )

diskDeactivatedDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 65)
)
diskDeactivatedDeviceFailure.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    diskDeactivatedDeviceFailure.setStatus(
        ""
    )

diskDeactivatedUsrRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 66)
)
diskDeactivatedUsrRequest.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    diskDeactivatedUsrRequest.setStatus(
        ""
    )

diskDeactivatedMediaDismount = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 67)
)
diskDeactivatedMediaDismount.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    diskDeactivatedMediaDismount.setStatus(
        ""
    )

diskDeactivatedEOM = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 68)
)
diskDeactivatedEOM.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    diskDeactivatedEOM.setStatus(
        ""
    )

diskDeactivatedServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 69)
)
diskDeactivatedServerDown.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    diskDeactivatedServerDown.setStatus(
        ""
    )

diskDeactivatedServerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 70)
)
diskDeactivatedServerFailure.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    diskDeactivatedServerFailure.setStatus(
        ""
    )

moduleDidNotReleaseOneResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 71)
)
moduleDidNotReleaseOneResource.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "nlmName"),
        ("NetWare-Server-Alarm-MIB", "resourceName"),
        ("NetWare-Server-Alarm-MIB", "resourceDescription"))
)
if mibBuilder.loadTexts:
    moduleDidNotReleaseOneResource.setStatus(
        ""
    )

mirroredPartNotAllSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 72)
)
mirroredPartNotAllSync.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "partitionNumber"))
)
if mibBuilder.loadTexts:
    mirroredPartNotAllSync.setStatus(
        ""
    )

allMirroredPartAreSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 73)
)
allMirroredPartAreSync.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    allMirroredPartAreSync.setStatus(
        ""
    )

partitionsSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 74)
)
partitionsSync.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "partitionNumber"))
)
if mibBuilder.loadTexts:
    partitionsSync.setStatus(
        ""
    )

partitionsUnSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 75)
)
partitionsUnSync.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "partitionNumber"))
)
if mibBuilder.loadTexts:
    partitionsUnSync.setStatus(
        ""
    )

remirroringPart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 76)
)
remirroringPart.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "partitionNumber"))
)
if mibBuilder.loadTexts:
    remirroringPart.setStatus(
        ""
    )

abortRemirrorPart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 77)
)
abortRemirrorPart.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "partitionNumber"))
)
if mibBuilder.loadTexts:
    abortRemirrorPart.setStatus(
        ""
    )

mirrorInconsistencies = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 78)
)
mirrorInconsistencies.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "partitionNumber"))
)
if mibBuilder.loadTexts:
    mirrorInconsistencies.setStatus(
        ""
    )

systemFileLockThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 79)
)
systemFileLockThresholdReached.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "numberOfFailedFileLockRequests"))
)
if mibBuilder.loadTexts:
    systemFileLockThresholdReached.setStatus(
        ""
    )

stationFileLockThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 80)
)
stationFileLockThresholdReached.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "numberOfFailedFileLockRequests"))
)
if mibBuilder.loadTexts:
    stationFileLockThresholdReached.setStatus(
        ""
    )

systemRecordLockThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 81)
)
systemRecordLockThresholdReached.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "numberOfFailedRecordLockRequests"))
)
if mibBuilder.loadTexts:
    systemRecordLockThresholdReached.setStatus(
        ""
    )

stationRecordLockThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 82)
)
stationRecordLockThresholdReached.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "numberOfFailedRecordLockRequests"))
)
if mibBuilder.loadTexts:
    stationRecordLockThresholdReached.setStatus(
        ""
    )

errorOpeningNetAcctData = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 83)
)
errorOpeningNetAcctData.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errorOpeningNetAcctData.setStatus(
        ""
    )

ncpSearchLimitExecBySrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 84)
)
ncpSearchLimitExecBySrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "connectionNumber"),
        ("NetWare-Server-Alarm-MIB", "userName"))
)
if mibBuilder.loadTexts:
    ncpSearchLimitExecBySrvr.setStatus(
        ""
    )

ncpSearchLimitExecByStation = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 85)
)
ncpSearchLimitExecByStation.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    ncpSearchLimitExecByStation.setStatus(
        ""
    )

insertMediaAck = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 86)
)
insertMediaAck.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    insertMediaAck.setStatus(
        ""
    )

insertMediaAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 87)
)
insertMediaAborted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    insertMediaAborted.setStatus(
        ""
    )

remMediaAck = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 88)
)
remMediaAck.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    remMediaAck.setStatus(
        ""
    )

remMediaAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 89)
)
remMediaAborted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    remMediaAborted.setStatus(
        ""
    )

insertDSMediaInto = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 90)
)
insertDSMediaInto.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "mediaLabel"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    insertDSMediaInto.setStatus(
        ""
    )

removeMediaFrom = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 91)
)
removeMediaFrom.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    removeMediaFrom.setStatus(
        ""
    )

redirectBlk = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 92)
)
redirectBlk.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "blockNumber"),
        ("NetWare-Server-Alarm-MIB", "blockNumber1"),
        ("NetWare-Server-Alarm-MIB", "partitionNumber"))
)
if mibBuilder.loadTexts:
    redirectBlk.setStatus(
        ""
    )

couldNotRedirectBlk = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 93)
)
couldNotRedirectBlk.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "blockNumber"),
        ("NetWare-Server-Alarm-MIB", "partitionNumber"))
)
if mibBuilder.loadTexts:
    couldNotRedirectBlk.setStatus(
        ""
    )

outOfHotFixBlks = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 94)
)
outOfHotFixBlks.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    outOfHotFixBlks.setStatus(
        ""
    )

fewRedirectionBlks = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 95)
)
fewRedirectionBlks.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "numberOfBlocks"))
)
if mibBuilder.loadTexts:
    fewRedirectionBlks.setStatus(
        ""
    )

redirectInconsistNoFix = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 96)
)
redirectInconsistNoFix.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "partitionNumber"))
)
if mibBuilder.loadTexts:
    redirectInconsistNoFix.setStatus(
        ""
    )

redirectInconsistFix = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 97)
)
redirectInconsistFix.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "partitionNumber"))
)
if mibBuilder.loadTexts:
    redirectInconsistFix.setStatus(
        ""
    )

invalidResourceTagPassed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 98)
)
invalidResourceTagPassed.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    invalidResourceTagPassed.setStatus(
        ""
    )

checkAddHardware = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 99)
)
checkAddHardware.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    checkAddHardware.setStatus(
        ""
    )

removeHardwareOptions = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 100)
)
removeHardwareOptions.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    removeHardwareOptions.setStatus(
        ""
    )

errUnloadKilledNlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 101)
)
errUnloadKilledNlm.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errUnloadKilledNlm.setStatus(
        ""
    )

invldRrceTagPsedToCreatePrss = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 102)
)
invldRrceTagPsedToCreatePrss.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    invldRrceTagPsedToCreatePrss.setStatus(
        ""
    )

createPrssReqtdStackTooSmall = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 103)
)
createPrssReqtdStackTooSmall.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    createPrssReqtdStackTooSmall.setStatus(
        ""
    )

createPrssUnableToAllocPrssCntlBlk = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 104)
)
createPrssUnableToAllocPrssCntlBlk.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    createPrssUnableToAllocPrssCntlBlk.setStatus(
        ""
    )

filePreservationErrorDuringErase = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 105)
)
filePreservationErrorDuringErase.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"))
)
if mibBuilder.loadTexts:
    filePreservationErrorDuringErase.setStatus(
        ""
    )

filePreservationErrorInsuffSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 106)
)
filePreservationErrorInsuffSpace.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"))
)
if mibBuilder.loadTexts:
    filePreservationErrorInsuffSpace.setStatus(
        ""
    )

mlidResetLanBd = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 107)
)
mlidResetLanBd.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"),
        ("NetWare-Server-Alarm-MIB", "socketNumber"))
)
if mibBuilder.loadTexts:
    mlidResetLanBd.setStatus(
        ""
    )

requestedRtrReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 108)
)
requestedRtrReset.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"),
        ("NetWare-Server-Alarm-MIB", "socketNumber"))
)
if mibBuilder.loadTexts:
    requestedRtrReset.setStatus(
        ""
    )

volContainstheWrongDOSType = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 109)
)
volContainstheWrongDOSType.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"),
        ("NetWare-Server-Alarm-MIB", "dosType"),
        ("NetWare-Server-Alarm-MIB", "dosType1"))
)
if mibBuilder.loadTexts:
    volContainstheWrongDOSType.setStatus(
        ""
    )

originalNameSpaceNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 110)
)
originalNameSpaceNotFound.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    originalNameSpaceNotFound.setStatus(
        ""
    )

rdTimeDataMigratorModuleChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 111)
)
rdTimeDataMigratorModuleChanged.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    rdTimeDataMigratorModuleChanged.setStatus(
        ""
    )

errCreateOpenTTSLogFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 112)
)
errCreateOpenTTSLogFile.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errCreateOpenTTSLogFile.setStatus(
        ""
    )

errWriteOpenTTSLogFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 113)
)
errWriteOpenTTSLogFile.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errWriteOpenTTSLogFile.setStatus(
        ""
    )

ttsDownbyVolDismount = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 114)
)
ttsDownbyVolDismount.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    ttsDownbyVolDismount.setStatus(
        ""
    )

disableTTSbyUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 115)
)
disableTTSbyUser.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    disableTTSbyUser.setStatus(
        ""
    )

ttsDisabledByOperator = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 116)
)
ttsDisabledByOperator.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    ttsDisabledByOperator.setStatus(
        ""
    )

ttsDisErrReadTTSduringBackout = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 117)
)
ttsDisErrReadTTSduringBackout.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    ttsDisErrReadTTSduringBackout.setStatus(
        ""
    )

ttsDisErrWritingTTSduringBackout = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 118)
)
ttsDisErrWritingTTSduringBackout.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    ttsDisErrWritingTTSduringBackout.setStatus(
        ""
    )

ttsDisErrTooManyDefInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 119)
)
ttsDisErrTooManyDefInfo.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    ttsDisErrTooManyDefInfo.setStatus(
        ""
    )

ttsDisErrWritingVolDefInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 120)
)
ttsDisErrWritingVolDefInfo.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    ttsDisErrWritingVolDefInfo.setStatus(
        ""
    )

ttsDisErrRdBlkFlRecGen = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 121)
)
ttsDisErrRdBlkFlRecGen.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    ttsDisErrRdBlkFlRecGen.setStatus(
        ""
    )

ttsDisGrowMemTables = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 122)
)
ttsDisGrowMemTables.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    ttsDisGrowMemTables.setStatus(
        ""
    )

ttsDisErrAllDiskSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 123)
)
ttsDisErrAllDiskSpace.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    ttsDisErrAllDiskSpace.setStatus(
        ""
    )

ttsDisDirErrOnBkFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 124)
)
ttsDisDirErrOnBkFile.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    ttsDisDirErrOnBkFile.setStatus(
        ""
    )

enableTTSByUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 125)
)
enableTTSByUser.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    enableTTSByUser.setStatus(
        ""
    )

transactionAbortedForStation = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 126)
)
transactionAbortedForStation.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "taskNumber"))
)
if mibBuilder.loadTexts:
    transactionAbortedForStation.setStatus(
        ""
    )

ttsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 127)
)
ttsLimitExceeded.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "numberOfTransactions"))
)
if mibBuilder.loadTexts:
    ttsLimitExceeded.setStatus(
        ""
    )

ttsNoMemForExpandingTxNodeTables = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 128)
)
ttsNoMemForExpandingTxNodeTables.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "numberOfFailedMemoryAllocAttempts"))
)
if mibBuilder.loadTexts:
    ttsNoMemForExpandingTxNodeTables.setStatus(
        ""
    )

auditEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 129)
)
auditEvent.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "auditEventNumber"),
        ("NetWare-Server-Alarm-MIB", "volumeNumber"))
)
if mibBuilder.loadTexts:
    auditEvent.setStatus(
        ""
    )

auditAlertThresholdOverFlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 130)
)
auditAlertThresholdOverFlow.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    auditAlertThresholdOverFlow.setStatus(
        ""
    )

auditAlertInvalidConfigFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 131)
)
auditAlertInvalidConfigFile.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    auditAlertInvalidConfigFile.setStatus(
        ""
    )

auditAlertNoMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 132)
)
auditAlertNoMemory.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    auditAlertNoMemory.setStatus(
        ""
    )

auditFileWriteError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 133)
)
auditFileWriteError.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    auditFileWriteError.setStatus(
        ""
    )

auditFileFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 134)
)
auditFileFull.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    auditFileFull.setStatus(
        ""
    )

invalidConnTypetoAllocConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 135)
)
invalidConnTypetoAllocConn.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    invalidConnTypetoAllocConn.setStatus(
        ""
    )

invalidRsrcTagPassedtoAllocConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 136)
)
invalidRsrcTagPassedtoAllocConn.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    invalidRsrcTagPassedtoAllocConn.setStatus(
        ""
    )

outOfServerConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 137)
)
outOfServerConn.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    outOfServerConn.setStatus(
        ""
    )

connTerminated5MinNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 138)
)
connTerminated5MinNotice.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    connTerminated5MinNotice.setStatus(
        ""
    )

usrAcctDisabledByAUsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 139)
)
usrAcctDisabledByAUsr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "accountName"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "numberOfConnections"))
)
if mibBuilder.loadTexts:
    usrAcctDisabledByAUsr.setStatus(
        ""
    )

useOfUnEncryptedPwd = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 140)
)
useOfUnEncryptedPwd.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    useOfUnEncryptedPwd.setStatus(
        ""
    )

supAcctLockoutClrdByConsole = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 141)
)
supAcctLockoutClrdByConsole.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    supAcctLockoutClrdByConsole.setStatus(
        ""
    )

systemTimeChangedByConsole = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 142)
)
systemTimeChangedByConsole.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"))
)
if mibBuilder.loadTexts:
    systemTimeChangedByConsole.setStatus(
        ""
    )

systemTimeChangedByUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 143)
)
systemTimeChangedByUser.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "userName"))
)
if mibBuilder.loadTexts:
    systemTimeChangedByUser.setStatus(
        ""
    )

volDismountedDueToDriveDeact = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 144)
)
volDismountedDueToDriveDeact.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    volDismountedDueToDriveDeact.setStatus(
        ""
    )

rtrFalsehood = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 145)
)
rtrFalsehood.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "internalNetworkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"),
        ("NetWare-Server-Alarm-MIB", "internalNetworkAddress1"),
        ("NetWare-Server-Alarm-MIB", "macAddress1"),
        ("NetWare-Server-Alarm-MIB", "macAddress2"))
)
if mibBuilder.loadTexts:
    rtrFalsehood.setStatus(
        ""
    )

srvrAddrChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 146)
)
srvrAddrChanged.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "serverName1"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"),
        ("NetWare-Server-Alarm-MIB", "socketNumber"),
        ("NetWare-Server-Alarm-MIB", "networkAddress1"),
        ("NetWare-Server-Alarm-MIB", "macAddress1"),
        ("NetWare-Server-Alarm-MIB", "socketNumber1"),
        ("NetWare-Server-Alarm-MIB", "macAddress2"))
)
if mibBuilder.loadTexts:
    srvrAddrChanged.setStatus(
        ""
    )

extendFileHasNoOwnerToCharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 147)
)
extendFileHasNoOwnerToCharge.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "connectionNumber"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"))
)
if mibBuilder.loadTexts:
    extendFileHasNoOwnerToCharge.setStatus(
        ""
    )

rtrConfigErr3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 148)
)
rtrConfigErr3.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "macAddress"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "networkAddress1"))
)
if mibBuilder.loadTexts:
    rtrConfigErr3.setStatus(
        ""
    )

rtrConfigErr2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 149)
)
rtrConfigErr2.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "macAddress"),
        ("NetWare-Server-Alarm-MIB", "routerName"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "networkAddress1"))
)
if mibBuilder.loadTexts:
    rtrConfigErr2.setStatus(
        ""
    )

dataMgrtrNotLoadedWhenRequested = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 150)
)
dataMgrtrNotLoadedWhenRequested.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    dataMgrtrNotLoadedWhenRequested.setStatus(
        ""
    )

noSpecificSupportModulesLoaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 151)
)
noSpecificSupportModulesLoaded.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    noSpecificSupportModulesLoaded.setStatus(
        ""
    )

notEnoughRAMForComp = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 152)
)
notEnoughRAMForComp.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    notEnoughRAMForComp.setStatus(
        ""
    )

diskErrorCompression = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 153)
)
diskErrorCompression.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    diskErrorCompression.setStatus(
        ""
    )

compressErrorHoleCountMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 154)
)
compressErrorHoleCountMismatch.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"),
        ("NetWare-Server-Alarm-MIB", "volumeNumber"),
        ("NetWare-Server-Alarm-MIB", "fileSize"),
        ("NetWare-Server-Alarm-MIB", "fileMiscInfo"),
        ("NetWare-Server-Alarm-MIB", "fileMiscInfo1"))
)
if mibBuilder.loadTexts:
    compressErrorHoleCountMismatch.setStatus(
        ""
    )

unknownErrorCompression = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 155)
)
unknownErrorCompression.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "errorNumber"))
)
if mibBuilder.loadTexts:
    unknownErrorCompression.setStatus(
        ""
    )

insufficientSpaceForDecompression = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 156)
)
insufficientSpaceForDecompression.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    insufficientSpaceForDecompression.setStatus(
        ""
    )

decompUnknownCompVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 157)
)
decompUnknownCompVersion.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    decompUnknownCompVersion.setStatus(
        ""
    )

unknownErrorDecomp = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 158)
)
unknownErrorDecomp.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "errorNumber"))
)
if mibBuilder.loadTexts:
    unknownErrorDecomp.setStatus(
        ""
    )

insufficientDecompError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 159)
)
insufficientDecompError.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    insufficientDecompError.setStatus(
        ""
    )

compFileCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 160)
)
compFileCorrupted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    compFileCorrupted.setStatus(
        ""
    )

rejectedIncompleteNCP = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 161)
)
rejectedIncompleteNCP.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "ncpFunctionNumber"),
        ("NetWare-Server-Alarm-MIB", "ncpSubFunctionNumber"))
)
if mibBuilder.loadTexts:
    rejectedIncompleteNCP.setStatus(
        ""
    )

stationUsedABadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 162)
)
stationUsedABadPacket.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "ncpFunctionNumber"),
        ("NetWare-Server-Alarm-MIB", "ncpSubFunctionNumber"))
)
if mibBuilder.loadTexts:
    stationUsedABadPacket.setStatus(
        ""
    )

rejectedNCPBadSubfunctionLngth = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 163)
)
rejectedNCPBadSubfunctionLngth.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "ncpFunctionNumber"),
        ("NetWare-Server-Alarm-MIB", "ncpSubFunctionNumber"))
)
if mibBuilder.loadTexts:
    rejectedNCPBadSubfunctionLngth.setStatus(
        ""
    )

processedNCPBadSubfunctionLngth = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 164)
)
processedNCPBadSubfunctionLngth.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "ncpFunctionNumber"),
        ("NetWare-Server-Alarm-MIB", "ncpSubFunctionNumber"))
)
if mibBuilder.loadTexts:
    processedNCPBadSubfunctionLngth.setStatus(
        ""
    )

compFilePathCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 165)
)
compFilePathCorrupted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"))
)
if mibBuilder.loadTexts:
    compFilePathCorrupted.setStatus(
        ""
    )

compFileInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 166)
)
compFileInUse.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    compFileInUse.setStatus(
        ""
    )

nlmNoPriority = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 167)
)
nlmNoPriority.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    nlmNoPriority.setStatus(
        ""
    )

workToDo = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 168)
)
workToDo.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    workToDo.setStatus(
        ""
    )

compErrTempFileErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 169)
)
compErrTempFileErr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"),
        ("NetWare-Server-Alarm-MIB", "volumeNumber"),
        ("NetWare-Server-Alarm-MIB", "fileSize"),
        ("NetWare-Server-Alarm-MIB", "fileOffset"),
        ("NetWare-Server-Alarm-MIB", "fileValue"))
)
if mibBuilder.loadTexts:
    compErrTempFileErr.setStatus(
        ""
    )

compErrLngthTotMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 170)
)
compErrLngthTotMismatch.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"),
        ("NetWare-Server-Alarm-MIB", "volumeNumber"),
        ("NetWare-Server-Alarm-MIB", "fileSize"),
        ("NetWare-Server-Alarm-MIB", "fileMiscInfo"),
        ("NetWare-Server-Alarm-MIB", "fileMiscInfo1"))
)
if mibBuilder.loadTexts:
    compErrLngthTotMismatch.setStatus(
        ""
    )

compErrOffsetTotalsMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 171)
)
compErrOffsetTotalsMismatch.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"),
        ("NetWare-Server-Alarm-MIB", "volumeNumber"),
        ("NetWare-Server-Alarm-MIB", "fileSize"),
        ("NetWare-Server-Alarm-MIB", "fileMiscInfo"),
        ("NetWare-Server-Alarm-MIB", "fileMiscInfo1"))
)
if mibBuilder.loadTexts:
    compErrOffsetTotalsMismatch.setStatus(
        ""
    )

compErrDataCodeCountMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 172)
)
compErrDataCodeCountMismatch.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"),
        ("NetWare-Server-Alarm-MIB", "volumeNumber"),
        ("NetWare-Server-Alarm-MIB", "fileSize"),
        ("NetWare-Server-Alarm-MIB", "fileMiscInfo"),
        ("NetWare-Server-Alarm-MIB", "fileMiscInfo1"))
)
if mibBuilder.loadTexts:
    compErrDataCodeCountMismatch.setStatus(
        ""
    )

compErrLthOffsetCodeCountMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 173)
)
compErrLthOffsetCodeCountMismatch.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"),
        ("NetWare-Server-Alarm-MIB", "volumeNumber"),
        ("NetWare-Server-Alarm-MIB", "fileSize"),
        ("NetWare-Server-Alarm-MIB", "fileMiscInfo"),
        ("NetWare-Server-Alarm-MIB", "fileMiscInfo1"))
)
if mibBuilder.loadTexts:
    compErrLthOffsetCodeCountMismatch.setStatus(
        ""
    )

compErrLgrLngthCodeCountMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 174)
)
compErrLgrLngthCodeCountMismatch.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "message"))
)
if mibBuilder.loadTexts:
    compErrLgrLngthCodeCountMismatch.setStatus(
        ""
    )

compErrReadZeroBytesInt = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 175)
)
compErrReadZeroBytesInt.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeNumber"),
        ("NetWare-Server-Alarm-MIB", "fileSize"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"),
        ("NetWare-Server-Alarm-MIB", "fileOffset"))
)
if mibBuilder.loadTexts:
    compErrReadZeroBytesInt.setStatus(
        ""
    )

compErrTreeTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 176)
)
compErrTreeTooBig.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"),
        ("NetWare-Server-Alarm-MIB", "volumeNumber"),
        ("NetWare-Server-Alarm-MIB", "fileSize"))
)
if mibBuilder.loadTexts:
    compErrTreeTooBig.setStatus(
        ""
    )

compErrMatchSizeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 177)
)
compErrMatchSizeFail.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"),
        ("NetWare-Server-Alarm-MIB", "volumeNumber"),
        ("NetWare-Server-Alarm-MIB", "fileSize"),
        ("NetWare-Server-Alarm-MIB", "fileSize1"),
        ("NetWare-Server-Alarm-MIB", "fileSize2"))
)
if mibBuilder.loadTexts:
    compErrMatchSizeFail.setStatus(
        ""
    )

signatureInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 178)
)
signatureInvalid.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    signatureInvalid.setStatus(
        ""
    )

licenseInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 179)
)
licenseInvalid.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "message"))
)
if mibBuilder.loadTexts:
    licenseInvalid.setStatus(
        ""
    )

deactHotFix = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 180)
)
deactHotFix.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    deactHotFix.setStatus(
        ""
    )

unknownDecompressErrorWithName = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 181)
)
unknownDecompressErrorWithName.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "errorNumber"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"))
)
if mibBuilder.loadTexts:
    unknownDecompressErrorWithName.setStatus(
        ""
    )

insufficientRamToDecompWithName = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 182)
)
insufficientRamToDecompWithName.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"))
)
if mibBuilder.loadTexts:
    insufficientRamToDecompWithName.setStatus(
        ""
    )

decompressUnderFreePercentage = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 183)
)
decompressUnderFreePercentage.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    decompressUnderFreePercentage.setStatus(
        ""
    )

negPktLargeBuffer = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 184)
)
negPktLargeBuffer.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "connectionNumber"),
        ("NetWare-Server-Alarm-MIB", "packetSize"),
        ("NetWare-Server-Alarm-MIB", "packetSize1"))
)
if mibBuilder.loadTexts:
    negPktLargeBuffer.setStatus(
        ""
    )

loginDisabledByConsole = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 185)
)
loginDisabledByConsole.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    loginDisabledByConsole.setStatus(
        ""
    )

loginEnabledByConsole = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 186)
)
loginEnabledByConsole.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    loginEnabledByConsole.setStatus(
        ""
    )

growableStackNotAllocated = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 187)
)
growableStackNotAllocated.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    growableStackNotAllocated.setStatus(
        ""
    )

insertDSMediaAck = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 188)
)
insertDSMediaAck.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    insertDSMediaAck.setStatus(
        ""
    )

insertMagazineAck = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 189)
)
insertMagazineAck.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    insertMagazineAck.setStatus(
        ""
    )

insertDSMediaAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 190)
)
insertDSMediaAborted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    insertDSMediaAborted.setStatus(
        ""
    )

insertMagazineAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 191)
)
insertMagazineAborted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    insertMagazineAborted.setStatus(
        ""
    )

remDSMediaAck = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 192)
)
remDSMediaAck.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    remDSMediaAck.setStatus(
        ""
    )

remMagazineAck = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 193)
)
remMagazineAck.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    remMagazineAck.setStatus(
        ""
    )

remDSMediaAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 194)
)
remDSMediaAborted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    remDSMediaAborted.setStatus(
        ""
    )

remMagazineAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 195)
)
remMagazineAborted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    remMagazineAborted.setStatus(
        ""
    )

insertMagazineInto = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 196)
)
insertMagazineInto.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "mediaLabel"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    insertMagazineInto.setStatus(
        ""
    )

removeDSMediaFrom = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 197)
)
removeDSMediaFrom.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    removeDSMediaFrom.setStatus(
        ""
    )

removeMagazineFrom = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 198)
)
removeMagazineFrom.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    removeMagazineFrom.setStatus(
        ""
    )

moduleDidNotReleaseResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 199)
)
moduleDidNotReleaseResources.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "numberOfResources"),
        ("NetWare-Server-Alarm-MIB", "nlmName"),
        ("NetWare-Server-Alarm-MIB", "resourceName"),
        ("NetWare-Server-Alarm-MIB", "resourceDescription"))
)
if mibBuilder.loadTexts:
    moduleDidNotReleaseResources.setStatus(
        ""
    )

opnBinderyFailSinceVolNotMounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 200)
)
opnBinderyFailSinceVolNotMounted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    opnBinderyFailSinceVolNotMounted.setStatus(
        ""
    )

binderyOpnReqtdByUsrFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 201)
)
binderyOpnReqtdByUsrFailed.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    binderyOpnReqtdByUsrFailed.setStatus(
        ""
    )

binderyOpnReqtdBySrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 202)
)
binderyOpnReqtdBySrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    binderyOpnReqtdBySrvr.setStatus(
        ""
    )

binderyOpnReqtdByUsR = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 203)
)
binderyOpnReqtdByUsR.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    binderyOpnReqtdByUsR.setStatus(
        ""
    )

binderyClosedBySrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 204)
)
binderyClosedBySrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    binderyClosedBySrvr.setStatus(
        ""
    )

binderyClosedByUsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 205)
)
binderyClosedByUsr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    binderyClosedByUsr.setStatus(
        ""
    )

intruderLockout = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 206)
)
intruderLockout.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "accountName"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    intruderLockout.setStatus(
        ""
    )

dsOpenFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 207)
)
dsOpenFailed.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    dsOpenFailed.setStatus(
        ""
    )

dsOpenFailedInconsistentDatabase = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 208)
)
dsOpenFailedInconsistentDatabase.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    dsOpenFailedInconsistentDatabase.setStatus(
        ""
    )

dsopenSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 209)
)
dsopenSucceeded.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    dsopenSucceeded.setStatus(
        ""
    )

dsCloseSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 210)
)
dsCloseSucceeded.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    dsCloseSucceeded.setStatus(
        ""
    )

skulkingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 211)
)
skulkingError.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "errorNumber"))
)
if mibBuilder.loadTexts:
    skulkingError.setStatus(
        ""
    )

dsIntruderNoAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 212)
)
dsIntruderNoAddr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "accountName"))
)
if mibBuilder.loadTexts:
    dsIntruderNoAddr.setStatus(
        ""
    )

domainQuarantined = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 213)
)
domainQuarantined.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "exceptionName"),
        ("NetWare-Server-Alarm-MIB", "domainName"),
        ("NetWare-Server-Alarm-MIB", "processName"),
        ("NetWare-Server-Alarm-MIB", "nlmName"),
        ("NetWare-Server-Alarm-MIB", "eipAddress"))
)
if mibBuilder.loadTexts:
    domainQuarantined.setStatus(
        ""
    )

commandProcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 214)
)
commandProcess.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    commandProcess.setStatus(
        ""
    )

remoteConnGranted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 215)
)
remoteConnGranted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    remoteConnGranted.setStatus(
        ""
    )

remoteConnCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 216)
)
remoteConnCleared.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    remoteConnCleared.setStatus(
        ""
    )

remoteConnRefused = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 217)
)
remoteConnRefused.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    remoteConnRefused.setStatus(
        ""
    )

translatorUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 218)
)
translatorUp.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    translatorUp.setStatus(
        ""
    )

translatorDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 219)
)
translatorDown.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    translatorDown.setStatus(
        ""
    )

volAnyMounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 220)
)
volAnyMounted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    volAnyMounted.setStatus(
        ""
    )

volAnyDismounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 221)
)
volAnyDismounted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"))
)
if mibBuilder.loadTexts:
    volAnyDismounted.setStatus(
        ""
    )

serverDownatServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 222)
)
serverDownatServer.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    serverDownatServer.setStatus(
        ""
    )

protocolBound = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 223)
)
protocolBound.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "lanDriverName"),
        ("NetWare-Server-Alarm-MIB", "boardNumber"),
        ("NetWare-Server-Alarm-MIB", "protocolName"))
)
if mibBuilder.loadTexts:
    protocolBound.setStatus(
        ""
    )

protocolUnBound = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 224)
)
protocolUnBound.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "lanDriverName"),
        ("NetWare-Server-Alarm-MIB", "boardNumber"),
        ("NetWare-Server-Alarm-MIB", "protocolName"))
)
if mibBuilder.loadTexts:
    protocolUnBound.setStatus(
        ""
    )

moduleLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 225)
)
moduleLoad.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "nlmName"))
)
if mibBuilder.loadTexts:
    moduleLoad.setStatus(
        ""
    )

moduleUnLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 226)
)
moduleUnLoad.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "nlmName"))
)
if mibBuilder.loadTexts:
    moduleUnLoad.setStatus(
        ""
    )

mlidRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 227)
)
mlidRegister.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "boardNumber"),
        ("NetWare-Server-Alarm-MIB", "lanDriverName"))
)
if mibBuilder.loadTexts:
    mlidRegister.setStatus(
        ""
    )

mlidUnRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 228)
)
mlidUnRegister.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "boardNumber"),
        ("NetWare-Server-Alarm-MIB", "lanDriverName"))
)
if mibBuilder.loadTexts:
    mlidUnRegister.setStatus(
        ""
    )

clearConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 229)
)
clearConnection.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "connectionNumber"))
)
if mibBuilder.loadTexts:
    clearConnection.setStatus(
        ""
    )

loginConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 230)
)
loginConnection.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "connectionNumber"))
)
if mibBuilder.loadTexts:
    loginConnection.setStatus(
        ""
    )

nlmAlertCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 231)
)
nlmAlertCritical.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "nlmName"),
        ("NetWare-Server-Alarm-MIB", "nlmSeverity"),
        ("NetWare-Server-Alarm-MIB", "message"))
)
if mibBuilder.loadTexts:
    nlmAlertCritical.setStatus(
        ""
    )

logoutConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 232)
)
logoutConnection.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "connectionNumber"))
)
if mibBuilder.loadTexts:
    logoutConnection.setStatus(
        ""
    )

usrAcctDeletedByAUsrSingleConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 233)
)
usrAcctDeletedByAUsrSingleConn.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "accountName"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"))
)
if mibBuilder.loadTexts:
    usrAcctDeletedByAUsrSingleConn.setStatus(
        ""
    )

compErrReadZeroBytesOrig = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 234)
)
compErrReadZeroBytesOrig.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeNumber"),
        ("NetWare-Server-Alarm-MIB", "fileSize"),
        ("NetWare-Server-Alarm-MIB", "fileName"),
        ("NetWare-Server-Alarm-MIB", "fileOffset"))
)
if mibBuilder.loadTexts:
    compErrReadZeroBytesOrig.setStatus(
        ""
    )

diskDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 235)
)
diskDeactivated.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "diskName"),
        ("NetWare-Server-Alarm-MIB", "reason"))
)
if mibBuilder.loadTexts:
    diskDeactivated.setStatus(
        ""
    )

diskMounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 236)
)
diskMounted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "diskName"))
)
if mibBuilder.loadTexts:
    diskMounted.setStatus(
        ""
    )

redirectBlockMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 237)
)
redirectBlockMismatch.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "partitionNumber"),
        ("NetWare-Server-Alarm-MIB", "numberOfPackets"))
)
if mibBuilder.loadTexts:
    redirectBlockMismatch.setStatus(
        ""
    )

shortTermMemoryLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 238)
)
shortTermMemoryLimitExceeded.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "numberOfFailedMemoryAllocAttempts"))
)
if mibBuilder.loadTexts:
    shortTermMemoryLimitExceeded.setStatus(
        ""
    )

semipermanentMemoryExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 239)
)
semipermanentMemoryExhausted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    semipermanentMemoryExhausted.setStatus(
        ""
    )

diskDismounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 240)
)
diskDismounted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "diskName"))
)
if mibBuilder.loadTexts:
    diskDismounted.setStatus(
        ""
    )

diskAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 241)
)
diskAdded.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "diskName"))
)
if mibBuilder.loadTexts:
    diskAdded.setStatus(
        ""
    )

diskActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 242)
)
diskActivated.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "diskName"))
)
if mibBuilder.loadTexts:
    diskActivated.setStatus(
        ""
    )

generalTTSfailures = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 243)
)
generalTTSfailures.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "message"))
)
if mibBuilder.loadTexts:
    generalTTSfailures.setStatus(
        ""
    )

mirroredPartNotAllSynced = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 244)
)
mirroredPartNotAllSynced.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    mirroredPartNotAllSynced.setStatus(
        ""
    )

reqtdRtrReset311 = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 245)
)
reqtdRtrReset311.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    reqtdRtrReset311.setStatus(
        ""
    )

invalidSignatureString = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 246)
)
invalidSignatureString.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    invalidSignatureString.setStatus(
        ""
    )

invalidDuplicateSignature = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 247)
)
invalidDuplicateSignature.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    invalidDuplicateSignature.setStatus(
        ""
    )

invalidPburstSignature = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 248)
)
invalidPburstSignature.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    invalidPburstSignature.setStatus(
        ""
    )

failedToDeleteMigrateFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 249)
)
failedToDeleteMigrateFile.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"),
        ("NetWare-Server-Alarm-MIB", "pathFileName"))
)
if mibBuilder.loadTexts:
    failedToDeleteMigrateFile.setStatus(
        ""
    )

unsignedRemoteConnectionRefused = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 250)
)
unsignedRemoteConnectionRefused.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    unsignedRemoteConnectionRefused.setStatus(
        ""
    )

unsignedRemoteConnectionGranted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 251)
)
unsignedRemoteConnectionGranted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    unsignedRemoteConnectionGranted.setStatus(
        ""
    )

responsePacketNotAllocated = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 252)
)
responsePacketNotAllocated.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    responsePacketNotAllocated.setStatus(
        ""
    )

wsNotLocated = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 253)
)
wsNotLocated.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    wsNotLocated.setStatus(
        ""
    )

remoteConnectionTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 254)
)
remoteConnectionTimedOut.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"))
)
if mibBuilder.loadTexts:
    remoteConnectionTimedOut.setStatus(
        ""
    )

modemConnectionCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 255)
)
modemConnectionCleared.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    modemConnectionCleared.setStatus(
        ""
    )

remoteConnectionClearedNameKnown = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 256)
)
remoteConnectionClearedNameKnown.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"))
)
if mibBuilder.loadTexts:
    remoteConnectionClearedNameKnown.setStatus(
        ""
    )

callBackNumberNotReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 257)
)
callBackNumberNotReceived.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    callBackNumberNotReceived.setStatus(
        ""
    )

nlmUnableToOpenListFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 258)
)
nlmUnableToOpenListFile.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    nlmUnableToOpenListFile.setStatus(
        ""
    )

nlmUnableToReadListFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 259)
)
nlmUnableToReadListFile.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    nlmUnableToReadListFile.setStatus(
        ""
    )

unauthorizedCallBackNumber = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 260)
)
unauthorizedCallBackNumber.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "callBackNumber"))
)
if mibBuilder.loadTexts:
    unauthorizedCallBackNumber.setStatus(
        ""
    )

modemClearedAndCallBackAttempted = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 261)
)
modemClearedAndCallBackAttempted.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    modemClearedAndCallBackAttempted.setStatus(
        ""
    )

attmptngToEstblshCallBckConnectn = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 262)
)
attmptngToEstblshCallBckConnectn.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "callBackNumber"))
)
if mibBuilder.loadTexts:
    attmptngToEstblshCallBckConnectn.setStatus(
        ""
    )

remoteConnectionRefusedNameKnown = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 263)
)
remoteConnectionRefusedNameKnown.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"))
)
if mibBuilder.loadTexts:
    remoteConnectionRefusedNameKnown.setStatus(
        ""
    )

remoteConnectionGrantedNameKnown = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 264)
)
remoteConnectionGrantedNameKnown.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "userName"))
)
if mibBuilder.loadTexts:
    remoteConnectionGrantedNameKnown.setStatus(
        ""
    )

modemConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 265)
)
modemConnectionEstablished.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "baudRate"))
)
if mibBuilder.loadTexts:
    modemConnectionEstablished.setStatus(
        ""
    )

dsAuditFileWriteError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 266)
)
dsAuditFileWriteError.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "objectName"))
)
if mibBuilder.loadTexts:
    dsAuditFileWriteError.setStatus(
        ""
    )

dsAuditFileFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 267)
)
dsAuditFileFull.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "objectName"))
)
if mibBuilder.loadTexts:
    dsAuditFileFull.setStatus(
        ""
    )

dsAuditFileThresholdOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 268)
)
dsAuditFileThresholdOverflow.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "objectName"))
)
if mibBuilder.loadTexts:
    dsAuditFileThresholdOverflow.setStatus(
        ""
    )

dsAuditMemoryAllocation = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 269)
)
dsAuditMemoryAllocation.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    dsAuditMemoryAllocation.setStatus(
        ""
    )

serverUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 270)
)
serverUp.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    serverUp.setStatus(
        ""
    )

volRestrictedSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 271)
)
volRestrictedSpace.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "volumeName"),
        ("NetWare-Server-Alarm-MIB", "volumePercentage"))
)
if mibBuilder.loadTexts:
    volRestrictedSpace.setStatus(
        ""
    )

cannotInitialize = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 272)
)
cannotInitialize.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    cannotInitialize.setStatus(
        ""
    )

cannotStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 273)
)
cannotStart.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    cannotStart.setStatus(
        ""
    )

noSAPSocketTag = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 274)
)
noSAPSocketTag.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noSAPSocketTag.setStatus(
        ""
    )

noSAPSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 275)
)
noSAPSocket.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noSAPSocket.setStatus(
        ""
    )

noSetableParameterTag = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 276)
)
noSetableParameterTag.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noSetableParameterTag.setStatus(
        ""
    )

noTimerTag = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 277)
)
noTimerTag.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noTimerTag.setStatus(
        ""
    )

noAllocTag = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 278)
)
noAllocTag.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noAllocTag.setStatus(
        ""
    )

noResourceTag = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 279)
)
noResourceTag.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noResourceTag.setStatus(
        ""
    )

noProcessTag = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 280)
)
noProcessTag.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noProcessTag.setStatus(
        ""
    )

noEventTag = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 281)
)
noEventTag.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noEventTag.setStatus(
        ""
    )

noGlobalInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 282)
)
noGlobalInfo.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noGlobalInfo.setStatus(
        ""
    )

noParseCommandLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 283)
)
noParseCommandLine.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noParseCommandLine.setStatus(
        ""
    )

noTimeSyncNCPVariable = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 284)
)
noTimeSyncNCPVariable.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noTimeSyncNCPVariable.setStatus(
        ""
    )

cantAllocateMainStack = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 285)
)
cantAllocateMainStack.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    cantAllocateMainStack.setStatus(
        ""
    )

cantCreateMainProcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 286)
)
cantCreateMainProcess.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    cantCreateMainProcess.setStatus(
        ""
    )

syncRadiusLess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 287)
)
syncRadiusLess.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "synchronizationRadius"))
)
if mibBuilder.loadTexts:
    syncRadiusLess.setStatus(
        ""
    )

unrecognizedCommandLinePrmtr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 288)
)
unrecognizedCommandLinePrmtr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "cmmndLnPrmtr"))
)
if mibBuilder.loadTexts:
    unrecognizedCommandLinePrmtr.setStatus(
        ""
    )

unrecognizedCommandLineOption = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 289)
)
unrecognizedCommandLineOption.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "cmmndLnPrmtr"))
)
if mibBuilder.loadTexts:
    unrecognizedCommandLineOption.setStatus(
        ""
    )

serverPolled = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 290)
)
serverPolled.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "serverName1"))
)
if mibBuilder.loadTexts:
    serverPolled.setStatus(
        ""
    )

singleSrvrIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 291)
)
singleSrvrIncompatible.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "serverName1"))
)
if mibBuilder.loadTexts:
    singleSrvrIncompatible.setStatus(
        ""
    )

timeSyncLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 292)
)
timeSyncLost.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "pollingLoops"))
)
if mibBuilder.loadTexts:
    timeSyncLost.setStatus(
        ""
    )

timeSyncEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 293)
)
timeSyncEstablished.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    timeSyncEstablished.setStatus(
        ""
    )

connTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 294)
)
connTerminated.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "connectionNumber"))
)
if mibBuilder.loadTexts:
    connTerminated.setStatus(
        ""
    )

connClearedByUsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 295)
)
connClearedByUsr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "connectionNumber"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "userName"))
)
if mibBuilder.loadTexts:
    connClearedByUsr.setStatus(
        ""
    )

loginDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 296)
)
loginDisabled.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "connectionNumber"),
        ("NetWare-Server-Alarm-MIB", "userName"))
)
if mibBuilder.loadTexts:
    loginDisabled.setStatus(
        ""
    )

downFileServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 297)
)
downFileServer.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "stationNumber"),
        ("NetWare-Server-Alarm-MIB", "userName"))
)
if mibBuilder.loadTexts:
    downFileServer.setStatus(
        ""
    )

loginEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 298)
)
loginEnabled.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "connectionNumber"),
        ("NetWare-Server-Alarm-MIB", "userName"))
)
if mibBuilder.loadTexts:
    loginEnabled.setStatus(
        ""
    )

errLogTransferErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 299)
)
errLogTransferErr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errLogTransferErr.setStatus(
        ""
    )

faultInConsoleCommandHandler = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 300)
)
faultInConsoleCommandHandler.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    faultInConsoleCommandHandler.setStatus(
        ""
    )

commLinkActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 301)
)
commLinkActivated.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    commLinkActivated.setStatus(
        ""
    )

commLinkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 302)
)
commLinkFailure.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    commLinkFailure.setStatus(
        ""
    )

commLinkDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 303)
)
commLinkDeactivated.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    commLinkDeactivated.setStatus(
        ""
    )

srvrAttemptedToSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 304)
)
srvrAttemptedToSync.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    srvrAttemptedToSync.setStatus(
        ""
    )

commLinkBrokeOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 305)
)
commLinkBrokeOK.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    commLinkBrokeOK.setStatus(
        ""
    )

syncStartingAmSecondarySrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 306)
)
syncStartingAmSecondarySrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    syncStartingAmSecondarySrvr.setStatus(
        ""
    )

badSrvrInitMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 307)
)
badSrvrInitMsg.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    badSrvrInitMsg.setStatus(
        ""
    )

commLinkInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 308)
)
commLinkInitFailed.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    commLinkInitFailed.setStatus(
        ""
    )

failedDuringSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 309)
)
failedDuringSync.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "szReason"))
)
if mibBuilder.loadTexts:
    failedDuringSync.setStatus(
        ""
    )

commDriverLoadedDuringActivate = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 310)
)
commDriverLoadedDuringActivate.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    commDriverLoadedDuringActivate.setStatus(
        ""
    )

errWritingStatusDump = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 311)
)
errWritingStatusDump.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errWritingStatusDump.setStatus(
        ""
    )

commDriverFailureOnPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 312)
)
commDriverFailureOnPrimary.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    commDriverFailureOnPrimary.setStatus(
        ""
    )

commDriverFailureOnSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 313)
)
commDriverFailureOnSecondary.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    commDriverFailureOnSecondary.setStatus(
        ""
    )

errFinishingGeneratingStatusDump = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 314)
)
errFinishingGeneratingStatusDump.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errFinishingGeneratingStatusDump.setStatus(
        ""
    )

sFTIIWhatToDoReasonString = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 315)
)
sFTIIWhatToDoReasonString.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    sFTIIWhatToDoReasonString.setStatus(
        ""
    )

sFTIIErrorUnexpected = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 316)
)
sFTIIErrorUnexpected.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    sFTIIErrorUnexpected.setStatus(
        ""
    )

syncErrorGeneratedFromCustomSrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 317)
)
syncErrorGeneratedFromCustomSrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    syncErrorGeneratedFromCustomSrvr.setStatus(
        ""
    )

srvrLinkHasPluggedPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 318)
)
srvrLinkHasPluggedPacket.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    srvrLinkHasPluggedPacket.setStatus(
        ""
    )

srvrToBeRevived = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 319)
)
srvrToBeRevived.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    srvrToBeRevived.setStatus(
        ""
    )

srvrsAreSyncedThisIsThePrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 320)
)
srvrsAreSyncedThisIsThePrimary.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    srvrsAreSyncedThisIsThePrimary.setStatus(
        ""
    )

srvrCantRouteViaIPXToSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 321)
)
srvrCantRouteViaIPXToSecondary.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    srvrCantRouteViaIPXToSecondary.setStatus(
        ""
    )

srvrIPXRouteInfoToSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 322)
)
srvrIPXRouteInfoToSecondary.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "boardNumber"),
        ("NetWare-Server-Alarm-MIB", "iHopsCount"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    srvrIPXRouteInfoToSecondary.setStatus(
        ""
    )

errGivingRAMtoMSEngine = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 323)
)
errGivingRAMtoMSEngine.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errGivingRAMtoMSEngine.setStatus(
        ""
    )

moreRAMgivenToMSEngine = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 324)
)
moreRAMgivenToMSEngine.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "iRamStart"),
        ("NetWare-Server-Alarm-MIB", "iRamLength"))
)
if mibBuilder.loadTexts:
    moreRAMgivenToMSEngine.setStatus(
        ""
    )

srvrsAreSyncedThisIsTheSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 325)
)
srvrsAreSyncedThisIsTheSecondary.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    srvrsAreSyncedThisIsTheSecondary.setStatus(
        ""
    )

srvrCantRouteViaIPXToPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 326)
)
srvrCantRouteViaIPXToPrimary.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    srvrCantRouteViaIPXToPrimary.setStatus(
        ""
    )

srvrIPXRouteInfoToPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 327)
)
srvrIPXRouteInfoToPrimary.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "boardNumber"),
        ("NetWare-Server-Alarm-MIB", "iHopsCount"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    srvrIPXRouteInfoToPrimary.setStatus(
        ""
    )

priSrvrFailedButSecDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 328)
)
priSrvrFailedButSecDown.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "szReason"))
)
if mibBuilder.loadTexts:
    priSrvrFailedButSecDown.setStatus(
        ""
    )

priSrvrFailedNewPri = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 329)
)
priSrvrFailedNewPri.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "szReason"))
)
if mibBuilder.loadTexts:
    priSrvrFailedNewPri.setStatus(
        ""
    )

numMemSegsExceedLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 330)
)
numMemSegsExceedLimit.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    numMemSegsExceedLimit.setStatus(
        ""
    )

numScreenExceedsLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 331)
)
numScreenExceedsLimit.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    numScreenExceedsLimit.setStatus(
        ""
    )

iOVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 332)
)
iOVersionMismatch.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    iOVersionMismatch.setStatus(
        ""
    )

srvrProtectLevelNoMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 333)
)
srvrProtectLevelNoMatch.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    srvrProtectLevelNoMatch.setStatus(
        ""
    )

srvrScreenAddressMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 334)
)
srvrScreenAddressMismatch.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    srvrScreenAddressMismatch.setStatus(
        ""
    )

iOEngineNotLoadedAtSameAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 335)
)
iOEngineNotLoadedAtSameAddress.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "iRamStart"),
        ("NetWare-Server-Alarm-MIB", "iRamLength"))
)
if mibBuilder.loadTexts:
    iOEngineNotLoadedAtSameAddress.setStatus(
        ""
    )

bothSrvrHaveActiveMSEngines = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 336)
)
bothSrvrHaveActiveMSEngines.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    bothSrvrHaveActiveMSEngines.setStatus(
        ""
    )

noActiveMSEngineOnServers = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 337)
)
noActiveMSEngineOnServers.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noActiveMSEngineOnServers.setStatus(
        ""
    )

secSrvrMissingRAM = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 338)
)
secSrvrMissingRAM.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "iRamStart"),
        ("NetWare-Server-Alarm-MIB", "iRamLength"))
)
if mibBuilder.loadTexts:
    secSrvrMissingRAM.setStatus(
        ""
    )

bothSrvrHaveSameIPXAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 339)
)
bothSrvrHaveSameIPXAddr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    bothSrvrHaveSameIPXAddr.setStatus(
        ""
    )

iOEngIPXAddrMatchesMSEngine = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 340)
)
iOEngIPXAddrMatchesMSEngine.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    iOEngIPXAddrMatchesMSEngine.setStatus(
        ""
    )

iOEnginesMismatchLANRxBufferSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 341)
)
iOEnginesMismatchLANRxBufferSize.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "iRamStart"),
        ("NetWare-Server-Alarm-MIB", "iRamLength"))
)
if mibBuilder.loadTexts:
    iOEnginesMismatchLANRxBufferSize.setStatus(
        ""
    )

iOEnginesHaveSameName = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 342)
)
iOEnginesHaveSameName.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    iOEnginesHaveSameName.setStatus(
        ""
    )

noMemoryForIOEngineName = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 343)
)
noMemoryForIOEngineName.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noMemoryForIOEngineName.setStatus(
        ""
    )

srvrToSrvrLinkBeginSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 344)
)
srvrToSrvrLinkBeginSync.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    srvrToSrvrLinkBeginSync.setStatus(
        ""
    )

mSEngineActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 345)
)
mSEngineActivated.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    mSEngineActivated.setStatus(
        ""
    )

mSEngActivatedWillSyncWithOther = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 346)
)
mSEngActivatedWillSyncWithOther.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    mSEngActivatedWillSyncWithOther.setStatus(
        ""
    )

iOtoMSCommBeingUnloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 347)
)
iOtoMSCommBeingUnloaded.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    iOtoMSCommBeingUnloaded.setStatus(
        ""
    )

sFTIIIOutOfMsgCodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 348)
)
sFTIIIOutOfMsgCodes.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    sFTIIIOutOfMsgCodes.setStatus(
        ""
    )

secIOEngSupportModulesNotLoaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 349)
)
secIOEngSupportModulesNotLoaded.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    secIOEngSupportModulesNotLoaded.setStatus(
        ""
    )

errXferDumpToSystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 350)
)
errXferDumpToSystem.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errXferDumpToSystem.setStatus(
        ""
    )

failureCheckingPrimarySrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 351)
)
failureCheckingPrimarySrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "szReason"))
)
if mibBuilder.loadTexts:
    failureCheckingPrimarySrvr.setStatus(
        ""
    )

errStarting2ndProcessor = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 352)
)
errStarting2ndProcessor.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    errStarting2ndProcessor.setStatus(
        ""
    )

srvrFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 353)
)
srvrFailure.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    srvrFailure.setStatus(
        ""
    )

srvsSyncing = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 354)
)
srvsSyncing.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    srvsSyncing.setStatus(
        ""
    )

mSLBoardNumberConnEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 355)
)
mSLBoardNumberConnEstablished.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "boardNumber"))
)
if mibBuilder.loadTexts:
    mSLBoardNumberConnEstablished.setStatus(
        ""
    )

secSrvrLANIsBetter = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 356)
)
secSrvrLANIsBetter.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    secSrvrLANIsBetter.setStatus(
        ""
    )

iPXreturningStatusPackets = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 357)
)
iPXreturningStatusPackets.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"))
)
if mibBuilder.loadTexts:
    iPXreturningStatusPackets.setStatus(
        ""
    )

iPXnotReturningStatCheckPackets = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 358)
)
iPXnotReturningStatCheckPackets.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"))
)
if mibBuilder.loadTexts:
    iPXnotReturningStatCheckPackets.setStatus(
        ""
    )

iPXnotReturningStatPcktLANJammed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 359)
)
iPXnotReturningStatPcktLANJammed.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "networkAddress"))
)
if mibBuilder.loadTexts:
    iPXnotReturningStatPcktLANJammed.setStatus(
        ""
    )

failReasonByOtherSrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 360)
)
failReasonByOtherSrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "serverName1"))
)
if mibBuilder.loadTexts:
    failReasonByOtherSrvr.setStatus(
        ""
    )

iPXInternetIsJammed = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 361)
)
iPXInternetIsJammed.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    iPXInternetIsJammed.setStatus(
        ""
    )

iPXTooSlowForSecSrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 362)
)
iPXTooSlowForSecSrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    iPXTooSlowForSecSrvr.setStatus(
        ""
    )

otherSrvrTooManyHops = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 363)
)
otherSrvrTooManyHops.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    otherSrvrTooManyHops.setStatus(
        ""
    )

iPXappearsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 364)
)
iPXappearsDown.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    iPXappearsDown.setStatus(
        ""
    )

iPXFoundRouteToOtherSrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 365)
)
iPXFoundRouteToOtherSrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    iPXFoundRouteToOtherSrvr.setStatus(
        ""
    )

iPXNewRouteToSecSrvr = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 366)
)
iPXNewRouteToSecSrvr.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "boardNumber"),
        ("NetWare-Server-Alarm-MIB", "iHopsCount"),
        ("NetWare-Server-Alarm-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    iPXNewRouteToSecSrvr.setStatus(
        ""
    )

iPXLostRoute = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 367)
)
iPXLostRoute.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    iPXLostRoute.setStatus(
        ""
    )

secSrvrGoingToDie = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 368)
)
secSrvrGoingToDie.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "szReason"),
        ("NetWare-Server-Alarm-MIB", "iTimerTicks"))
)
if mibBuilder.loadTexts:
    secSrvrGoingToDie.setStatus(
        ""
    )

priSrvrDyingTimerReStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 369)
)
priSrvrDyingTimerReStart.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "szReason"),
        ("NetWare-Server-Alarm-MIB", "iTimerTicks"))
)
if mibBuilder.loadTexts:
    priSrvrDyingTimerReStart.setStatus(
        ""
    )

priSrvrDying = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 370)
)
priSrvrDying.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "szReason"),
        ("NetWare-Server-Alarm-MIB", "iTimerTicks"))
)
if mibBuilder.loadTexts:
    priSrvrDying.setStatus(
        ""
    )

noMemForOtherIOEngScreen = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 371)
)
noMemForOtherIOEngScreen.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    noMemForOtherIOEngScreen.setStatus(
        ""
    )

timesyncErrorMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 372)
)
timesyncErrorMsg.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    timesyncErrorMsg.setStatus(
        ""
    )

dsAlertSetServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 373)
)
dsAlertSetServerDown.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "serverName1"))
)
if mibBuilder.loadTexts:
    dsAlertSetServerDown.setStatus(
        ""
    )

dsAlertSetServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 374)
)
dsAlertSetServerUp.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "serverName1"))
)
if mibBuilder.loadTexts:
    dsAlertSetServerUp.setStatus(
        ""
    )

redirectTableMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 375)
)
redirectTableMismatch.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "partitionNumber"),
        ("NetWare-Server-Alarm-MIB", "numberOfPackets"))
)
if mibBuilder.loadTexts:
    redirectTableMismatch.setStatus(
        ""
    )

nlmAlertMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 376)
)
nlmAlertMajor.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "nlmName"),
        ("NetWare-Server-Alarm-MIB", "nlmSeverity"),
        ("NetWare-Server-Alarm-MIB", "message"))
)
if mibBuilder.loadTexts:
    nlmAlertMajor.setStatus(
        ""
    )

nlmAlertMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 377)
)
nlmAlertMinor.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "nlmName"),
        ("NetWare-Server-Alarm-MIB", "nlmSeverity"),
        ("NetWare-Server-Alarm-MIB", "message"))
)
if mibBuilder.loadTexts:
    nlmAlertMinor.setStatus(
        ""
    )

nlmAlertInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 10, 0, 378)
)
nlmAlertInformational.setObjects(
      *(("NetWare-Server-Alarm-MIB", "serverName"),
        ("NetWare-Server-Alarm-MIB", "trapTime"),
        ("NetWare-Server-Alarm-MIB", "nlmName"),
        ("NetWare-Server-Alarm-MIB", "nlmSeverity"),
        ("NetWare-Server-Alarm-MIB", "message"))
)
if mibBuilder.loadTexts:
    nlmAlertInformational.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NetWare-Server-Alarm-MIB",
    **{"NetNumber": NetNumber,
       "novell": novell,
       "mibDoc": mibDoc,
       "nwalarm-mib": nwalarm_mib,
       "outOfShortTermMemoryRequestFailed": outOfShortTermMemoryRequestFailed,
       "errWritingToTheExtendedDirSpace": errWritingToTheExtendedDirSpace,
       "errWritingToFile": errWritingToFile,
       "errWritingToFileUsr": errWritingToFileUsr,
       "errWritingToFileDataStream": errWritingToFileDataStream,
       "errWritingToFileDataStreamUsr": errWritingToFileDataStreamUsr,
       "fileReaderrSrvrNofileName": fileReaderrSrvrNofileName,
       "fileReaderrUsrNofileName": fileReaderrUsrNofileName,
       "fileReaderrDSSrvr": fileReaderrDSSrvr,
       "fileReaderrDSUsr": fileReaderrDSUsr,
       "fileWritePreReaderrSrvr": fileWritePreReaderrSrvr,
       "fileWritePreReaderrUsr": fileWritePreReaderrUsr,
       "fileWritePreReaderrDSSrvr": fileWritePreReaderrDSSrvr,
       "fileWritePreReaderrDSUsr": fileWritePreReaderrDSUsr,
       "cacheMemAllocExceededMinLeftLimit": cacheMemAllocExceededMinLeftLimit,
       "cacheMemAllocOutOfMem": cacheMemAllocOutOfMem,
       "numberOfCacheBuffersGettingLow": numberOfCacheBuffersGettingLow,
       "volOfDiskSpace": volOfDiskSpace,
       "volOfDiskSpaceNoPurge": volOfDiskSpaceNoPurge,
       "volAlmostOutOfDiskSpace": volAlmostOutOfDiskSpace,
       "errWritingFatTables": errWritingFatTables,
       "errWritingDirectoryBlk": errWritingDirectoryBlk,
       "dirCopyReadErr": dirCopyReadErr,
       "errReadingBothCopiesofDir": errReadingBothCopiesofDir,
       "allocateDirEntryWriteError": allocateDirEntryWriteError,
       "errExpandingDirDuetoWriteErr": errExpandingDirDuetoWriteErr,
       "dirReachedItsLimit": dirReachedItsLimit,
       "errExpandingNoDiskSpace": errExpandingNoDiskSpace,
       "errExpandingNoMemSpace": errExpandingNoMemSpace,
       "dirSizeGettingTooLrgeForMem": dirSizeGettingTooLrgeForMem,
       "lanReceiveBuffLimitReached": lanReceiveBuffLimitReached,
       "connTerminatedByWatchDog": connTerminatedByWatchDog,
       "copyrightViolation": copyrightViolation,
       "writeFault": writeFault,
       "readFault": readFault,
       "ipxReceivedIncomPacket": ipxReceivedIncomPacket,
       "unableToCreateVOLERR": unableToCreateVOLERR,
       "unableToWriteVOLERR": unableToWriteVOLERR,
       "volOprDespiteDeviceDriveDeact": volOprDespiteDeviceDriveDeact,
       "loginDisabledByUser": loginDisabledByUser,
       "loginEnabledByUser": loginEnabledByUser,
       "clrStnByConsole": clrStnByConsole,
       "clrStnByUsr": clrStnByUsr,
       "fileServerDowned": fileServerDowned,
       "errOpeningRIPSocket": errOpeningRIPSocket,
       "rtrConfigErr": rtrConfigErr,
       "lanDriverLoopBack": lanDriverLoopBack,
       "dupInternetAddr": dupInternetAddr,
       "lanBdUnreachable": lanBdUnreachable,
       "ipxUnbndRequest": ipxUnbndRequest,
       "errOpeningSAPSocket": errOpeningSAPSocket,
       "rtrClaimingSameInterAddr": rtrClaimingSameInterAddr,
       "spuriousInt": spuriousInt,
       "checksumInvalid": checksumInvalid,
       "prmyPicLostInterrupt": prmyPicLostInterrupt,
       "scndryPicLostInterrupt": scndryPicLostInterrupt,
       "exception": exception,
       "invalidScreenID": invalidScreenID,
       "prssDidNotRelqhCntlFqtly": prssDidNotRelqhCntlFqtly,
       "fileSrvrUsrDeleted": fileSrvrUsrDeleted,
       "usrAcctDeletedByAUsr": usrAcctDeletedByAUsr,
       "invalidResourceTag": invalidResourceTag,
       "diskDeactivatedUnknownReason": diskDeactivatedUnknownReason,
       "diskDeactivatedDriverUnload": diskDeactivatedDriverUnload,
       "diskDeactivatedDeviceFailure": diskDeactivatedDeviceFailure,
       "diskDeactivatedUsrRequest": diskDeactivatedUsrRequest,
       "diskDeactivatedMediaDismount": diskDeactivatedMediaDismount,
       "diskDeactivatedEOM": diskDeactivatedEOM,
       "diskDeactivatedServerDown": diskDeactivatedServerDown,
       "diskDeactivatedServerFailure": diskDeactivatedServerFailure,
       "moduleDidNotReleaseOneResource": moduleDidNotReleaseOneResource,
       "mirroredPartNotAllSync": mirroredPartNotAllSync,
       "allMirroredPartAreSync": allMirroredPartAreSync,
       "partitionsSync": partitionsSync,
       "partitionsUnSync": partitionsUnSync,
       "remirroringPart": remirroringPart,
       "abortRemirrorPart": abortRemirrorPart,
       "mirrorInconsistencies": mirrorInconsistencies,
       "systemFileLockThresholdReached": systemFileLockThresholdReached,
       "stationFileLockThresholdReached": stationFileLockThresholdReached,
       "systemRecordLockThresholdReached": systemRecordLockThresholdReached,
       "stationRecordLockThresholdReached": stationRecordLockThresholdReached,
       "errorOpeningNetAcctData": errorOpeningNetAcctData,
       "ncpSearchLimitExecBySrvr": ncpSearchLimitExecBySrvr,
       "ncpSearchLimitExecByStation": ncpSearchLimitExecByStation,
       "insertMediaAck": insertMediaAck,
       "insertMediaAborted": insertMediaAborted,
       "remMediaAck": remMediaAck,
       "remMediaAborted": remMediaAborted,
       "insertDSMediaInto": insertDSMediaInto,
       "removeMediaFrom": removeMediaFrom,
       "redirectBlk": redirectBlk,
       "couldNotRedirectBlk": couldNotRedirectBlk,
       "outOfHotFixBlks": outOfHotFixBlks,
       "fewRedirectionBlks": fewRedirectionBlks,
       "redirectInconsistNoFix": redirectInconsistNoFix,
       "redirectInconsistFix": redirectInconsistFix,
       "invalidResourceTagPassed": invalidResourceTagPassed,
       "checkAddHardware": checkAddHardware,
       "removeHardwareOptions": removeHardwareOptions,
       "errUnloadKilledNlm": errUnloadKilledNlm,
       "invldRrceTagPsedToCreatePrss": invldRrceTagPsedToCreatePrss,
       "createPrssReqtdStackTooSmall": createPrssReqtdStackTooSmall,
       "createPrssUnableToAllocPrssCntlBlk": createPrssUnableToAllocPrssCntlBlk,
       "filePreservationErrorDuringErase": filePreservationErrorDuringErase,
       "filePreservationErrorInsuffSpace": filePreservationErrorInsuffSpace,
       "mlidResetLanBd": mlidResetLanBd,
       "requestedRtrReset": requestedRtrReset,
       "volContainstheWrongDOSType": volContainstheWrongDOSType,
       "originalNameSpaceNotFound": originalNameSpaceNotFound,
       "rdTimeDataMigratorModuleChanged": rdTimeDataMigratorModuleChanged,
       "errCreateOpenTTSLogFile": errCreateOpenTTSLogFile,
       "errWriteOpenTTSLogFile": errWriteOpenTTSLogFile,
       "ttsDownbyVolDismount": ttsDownbyVolDismount,
       "disableTTSbyUser": disableTTSbyUser,
       "ttsDisabledByOperator": ttsDisabledByOperator,
       "ttsDisErrReadTTSduringBackout": ttsDisErrReadTTSduringBackout,
       "ttsDisErrWritingTTSduringBackout": ttsDisErrWritingTTSduringBackout,
       "ttsDisErrTooManyDefInfo": ttsDisErrTooManyDefInfo,
       "ttsDisErrWritingVolDefInfo": ttsDisErrWritingVolDefInfo,
       "ttsDisErrRdBlkFlRecGen": ttsDisErrRdBlkFlRecGen,
       "ttsDisGrowMemTables": ttsDisGrowMemTables,
       "ttsDisErrAllDiskSpace": ttsDisErrAllDiskSpace,
       "ttsDisDirErrOnBkFile": ttsDisDirErrOnBkFile,
       "enableTTSByUser": enableTTSByUser,
       "transactionAbortedForStation": transactionAbortedForStation,
       "ttsLimitExceeded": ttsLimitExceeded,
       "ttsNoMemForExpandingTxNodeTables": ttsNoMemForExpandingTxNodeTables,
       "auditEvent": auditEvent,
       "auditAlertThresholdOverFlow": auditAlertThresholdOverFlow,
       "auditAlertInvalidConfigFile": auditAlertInvalidConfigFile,
       "auditAlertNoMemory": auditAlertNoMemory,
       "auditFileWriteError": auditFileWriteError,
       "auditFileFull": auditFileFull,
       "invalidConnTypetoAllocConn": invalidConnTypetoAllocConn,
       "invalidRsrcTagPassedtoAllocConn": invalidRsrcTagPassedtoAllocConn,
       "outOfServerConn": outOfServerConn,
       "connTerminated5MinNotice": connTerminated5MinNotice,
       "usrAcctDisabledByAUsr": usrAcctDisabledByAUsr,
       "useOfUnEncryptedPwd": useOfUnEncryptedPwd,
       "supAcctLockoutClrdByConsole": supAcctLockoutClrdByConsole,
       "systemTimeChangedByConsole": systemTimeChangedByConsole,
       "systemTimeChangedByUser": systemTimeChangedByUser,
       "volDismountedDueToDriveDeact": volDismountedDueToDriveDeact,
       "rtrFalsehood": rtrFalsehood,
       "srvrAddrChanged": srvrAddrChanged,
       "extendFileHasNoOwnerToCharge": extendFileHasNoOwnerToCharge,
       "rtrConfigErr3": rtrConfigErr3,
       "rtrConfigErr2": rtrConfigErr2,
       "dataMgrtrNotLoadedWhenRequested": dataMgrtrNotLoadedWhenRequested,
       "noSpecificSupportModulesLoaded": noSpecificSupportModulesLoaded,
       "notEnoughRAMForComp": notEnoughRAMForComp,
       "diskErrorCompression": diskErrorCompression,
       "compressErrorHoleCountMismatch": compressErrorHoleCountMismatch,
       "unknownErrorCompression": unknownErrorCompression,
       "insufficientSpaceForDecompression": insufficientSpaceForDecompression,
       "decompUnknownCompVersion": decompUnknownCompVersion,
       "unknownErrorDecomp": unknownErrorDecomp,
       "insufficientDecompError": insufficientDecompError,
       "compFileCorrupted": compFileCorrupted,
       "rejectedIncompleteNCP": rejectedIncompleteNCP,
       "stationUsedABadPacket": stationUsedABadPacket,
       "rejectedNCPBadSubfunctionLngth": rejectedNCPBadSubfunctionLngth,
       "processedNCPBadSubfunctionLngth": processedNCPBadSubfunctionLngth,
       "compFilePathCorrupted": compFilePathCorrupted,
       "compFileInUse": compFileInUse,
       "nlmNoPriority": nlmNoPriority,
       "workToDo": workToDo,
       "compErrTempFileErr": compErrTempFileErr,
       "compErrLngthTotMismatch": compErrLngthTotMismatch,
       "compErrOffsetTotalsMismatch": compErrOffsetTotalsMismatch,
       "compErrDataCodeCountMismatch": compErrDataCodeCountMismatch,
       "compErrLthOffsetCodeCountMismatch": compErrLthOffsetCodeCountMismatch,
       "compErrLgrLngthCodeCountMismatch": compErrLgrLngthCodeCountMismatch,
       "compErrReadZeroBytesInt": compErrReadZeroBytesInt,
       "compErrTreeTooBig": compErrTreeTooBig,
       "compErrMatchSizeFail": compErrMatchSizeFail,
       "signatureInvalid": signatureInvalid,
       "licenseInvalid": licenseInvalid,
       "deactHotFix": deactHotFix,
       "unknownDecompressErrorWithName": unknownDecompressErrorWithName,
       "insufficientRamToDecompWithName": insufficientRamToDecompWithName,
       "decompressUnderFreePercentage": decompressUnderFreePercentage,
       "negPktLargeBuffer": negPktLargeBuffer,
       "loginDisabledByConsole": loginDisabledByConsole,
       "loginEnabledByConsole": loginEnabledByConsole,
       "growableStackNotAllocated": growableStackNotAllocated,
       "insertDSMediaAck": insertDSMediaAck,
       "insertMagazineAck": insertMagazineAck,
       "insertDSMediaAborted": insertDSMediaAborted,
       "insertMagazineAborted": insertMagazineAborted,
       "remDSMediaAck": remDSMediaAck,
       "remMagazineAck": remMagazineAck,
       "remDSMediaAborted": remDSMediaAborted,
       "remMagazineAborted": remMagazineAborted,
       "insertMagazineInto": insertMagazineInto,
       "removeDSMediaFrom": removeDSMediaFrom,
       "removeMagazineFrom": removeMagazineFrom,
       "moduleDidNotReleaseResources": moduleDidNotReleaseResources,
       "opnBinderyFailSinceVolNotMounted": opnBinderyFailSinceVolNotMounted,
       "binderyOpnReqtdByUsrFailed": binderyOpnReqtdByUsrFailed,
       "binderyOpnReqtdBySrvr": binderyOpnReqtdBySrvr,
       "binderyOpnReqtdByUsR": binderyOpnReqtdByUsR,
       "binderyClosedBySrvr": binderyClosedBySrvr,
       "binderyClosedByUsr": binderyClosedByUsr,
       "intruderLockout": intruderLockout,
       "dsOpenFailed": dsOpenFailed,
       "dsOpenFailedInconsistentDatabase": dsOpenFailedInconsistentDatabase,
       "dsopenSucceeded": dsopenSucceeded,
       "dsCloseSucceeded": dsCloseSucceeded,
       "skulkingError": skulkingError,
       "dsIntruderNoAddr": dsIntruderNoAddr,
       "domainQuarantined": domainQuarantined,
       "commandProcess": commandProcess,
       "remoteConnGranted": remoteConnGranted,
       "remoteConnCleared": remoteConnCleared,
       "remoteConnRefused": remoteConnRefused,
       "translatorUp": translatorUp,
       "translatorDown": translatorDown,
       "volAnyMounted": volAnyMounted,
       "volAnyDismounted": volAnyDismounted,
       "serverDownatServer": serverDownatServer,
       "protocolBound": protocolBound,
       "protocolUnBound": protocolUnBound,
       "moduleLoad": moduleLoad,
       "moduleUnLoad": moduleUnLoad,
       "mlidRegister": mlidRegister,
       "mlidUnRegister": mlidUnRegister,
       "clearConnection": clearConnection,
       "loginConnection": loginConnection,
       "nlmAlertCritical": nlmAlertCritical,
       "logoutConnection": logoutConnection,
       "usrAcctDeletedByAUsrSingleConn": usrAcctDeletedByAUsrSingleConn,
       "compErrReadZeroBytesOrig": compErrReadZeroBytesOrig,
       "diskDeactivated": diskDeactivated,
       "diskMounted": diskMounted,
       "redirectBlockMismatch": redirectBlockMismatch,
       "shortTermMemoryLimitExceeded": shortTermMemoryLimitExceeded,
       "semipermanentMemoryExhausted": semipermanentMemoryExhausted,
       "diskDismounted": diskDismounted,
       "diskAdded": diskAdded,
       "diskActivated": diskActivated,
       "generalTTSfailures": generalTTSfailures,
       "mirroredPartNotAllSynced": mirroredPartNotAllSynced,
       "reqtdRtrReset311": reqtdRtrReset311,
       "invalidSignatureString": invalidSignatureString,
       "invalidDuplicateSignature": invalidDuplicateSignature,
       "invalidPburstSignature": invalidPburstSignature,
       "failedToDeleteMigrateFile": failedToDeleteMigrateFile,
       "unsignedRemoteConnectionRefused": unsignedRemoteConnectionRefused,
       "unsignedRemoteConnectionGranted": unsignedRemoteConnectionGranted,
       "responsePacketNotAllocated": responsePacketNotAllocated,
       "wsNotLocated": wsNotLocated,
       "remoteConnectionTimedOut": remoteConnectionTimedOut,
       "modemConnectionCleared": modemConnectionCleared,
       "remoteConnectionClearedNameKnown": remoteConnectionClearedNameKnown,
       "callBackNumberNotReceived": callBackNumberNotReceived,
       "nlmUnableToOpenListFile": nlmUnableToOpenListFile,
       "nlmUnableToReadListFile": nlmUnableToReadListFile,
       "unauthorizedCallBackNumber": unauthorizedCallBackNumber,
       "modemClearedAndCallBackAttempted": modemClearedAndCallBackAttempted,
       "attmptngToEstblshCallBckConnectn": attmptngToEstblshCallBckConnectn,
       "remoteConnectionRefusedNameKnown": remoteConnectionRefusedNameKnown,
       "remoteConnectionGrantedNameKnown": remoteConnectionGrantedNameKnown,
       "modemConnectionEstablished": modemConnectionEstablished,
       "dsAuditFileWriteError": dsAuditFileWriteError,
       "dsAuditFileFull": dsAuditFileFull,
       "dsAuditFileThresholdOverflow": dsAuditFileThresholdOverflow,
       "dsAuditMemoryAllocation": dsAuditMemoryAllocation,
       "serverUp": serverUp,
       "volRestrictedSpace": volRestrictedSpace,
       "cannotInitialize": cannotInitialize,
       "cannotStart": cannotStart,
       "noSAPSocketTag": noSAPSocketTag,
       "noSAPSocket": noSAPSocket,
       "noSetableParameterTag": noSetableParameterTag,
       "noTimerTag": noTimerTag,
       "noAllocTag": noAllocTag,
       "noResourceTag": noResourceTag,
       "noProcessTag": noProcessTag,
       "noEventTag": noEventTag,
       "noGlobalInfo": noGlobalInfo,
       "noParseCommandLine": noParseCommandLine,
       "noTimeSyncNCPVariable": noTimeSyncNCPVariable,
       "cantAllocateMainStack": cantAllocateMainStack,
       "cantCreateMainProcess": cantCreateMainProcess,
       "syncRadiusLess": syncRadiusLess,
       "unrecognizedCommandLinePrmtr": unrecognizedCommandLinePrmtr,
       "unrecognizedCommandLineOption": unrecognizedCommandLineOption,
       "serverPolled": serverPolled,
       "singleSrvrIncompatible": singleSrvrIncompatible,
       "timeSyncLost": timeSyncLost,
       "timeSyncEstablished": timeSyncEstablished,
       "connTerminated": connTerminated,
       "connClearedByUsr": connClearedByUsr,
       "loginDisabled": loginDisabled,
       "downFileServer": downFileServer,
       "loginEnabled": loginEnabled,
       "errLogTransferErr": errLogTransferErr,
       "faultInConsoleCommandHandler": faultInConsoleCommandHandler,
       "commLinkActivated": commLinkActivated,
       "commLinkFailure": commLinkFailure,
       "commLinkDeactivated": commLinkDeactivated,
       "srvrAttemptedToSync": srvrAttemptedToSync,
       "commLinkBrokeOK": commLinkBrokeOK,
       "syncStartingAmSecondarySrvr": syncStartingAmSecondarySrvr,
       "badSrvrInitMsg": badSrvrInitMsg,
       "commLinkInitFailed": commLinkInitFailed,
       "failedDuringSync": failedDuringSync,
       "commDriverLoadedDuringActivate": commDriverLoadedDuringActivate,
       "errWritingStatusDump": errWritingStatusDump,
       "commDriverFailureOnPrimary": commDriverFailureOnPrimary,
       "commDriverFailureOnSecondary": commDriverFailureOnSecondary,
       "errFinishingGeneratingStatusDump": errFinishingGeneratingStatusDump,
       "sFTIIWhatToDoReasonString": sFTIIWhatToDoReasonString,
       "sFTIIErrorUnexpected": sFTIIErrorUnexpected,
       "syncErrorGeneratedFromCustomSrvr": syncErrorGeneratedFromCustomSrvr,
       "srvrLinkHasPluggedPacket": srvrLinkHasPluggedPacket,
       "srvrToBeRevived": srvrToBeRevived,
       "srvrsAreSyncedThisIsThePrimary": srvrsAreSyncedThisIsThePrimary,
       "srvrCantRouteViaIPXToSecondary": srvrCantRouteViaIPXToSecondary,
       "srvrIPXRouteInfoToSecondary": srvrIPXRouteInfoToSecondary,
       "errGivingRAMtoMSEngine": errGivingRAMtoMSEngine,
       "moreRAMgivenToMSEngine": moreRAMgivenToMSEngine,
       "srvrsAreSyncedThisIsTheSecondary": srvrsAreSyncedThisIsTheSecondary,
       "srvrCantRouteViaIPXToPrimary": srvrCantRouteViaIPXToPrimary,
       "srvrIPXRouteInfoToPrimary": srvrIPXRouteInfoToPrimary,
       "priSrvrFailedButSecDown": priSrvrFailedButSecDown,
       "priSrvrFailedNewPri": priSrvrFailedNewPri,
       "numMemSegsExceedLimit": numMemSegsExceedLimit,
       "numScreenExceedsLimit": numScreenExceedsLimit,
       "iOVersionMismatch": iOVersionMismatch,
       "srvrProtectLevelNoMatch": srvrProtectLevelNoMatch,
       "srvrScreenAddressMismatch": srvrScreenAddressMismatch,
       "iOEngineNotLoadedAtSameAddress": iOEngineNotLoadedAtSameAddress,
       "bothSrvrHaveActiveMSEngines": bothSrvrHaveActiveMSEngines,
       "noActiveMSEngineOnServers": noActiveMSEngineOnServers,
       "secSrvrMissingRAM": secSrvrMissingRAM,
       "bothSrvrHaveSameIPXAddr": bothSrvrHaveSameIPXAddr,
       "iOEngIPXAddrMatchesMSEngine": iOEngIPXAddrMatchesMSEngine,
       "iOEnginesMismatchLANRxBufferSize": iOEnginesMismatchLANRxBufferSize,
       "iOEnginesHaveSameName": iOEnginesHaveSameName,
       "noMemoryForIOEngineName": noMemoryForIOEngineName,
       "srvrToSrvrLinkBeginSync": srvrToSrvrLinkBeginSync,
       "mSEngineActivated": mSEngineActivated,
       "mSEngActivatedWillSyncWithOther": mSEngActivatedWillSyncWithOther,
       "iOtoMSCommBeingUnloaded": iOtoMSCommBeingUnloaded,
       "sFTIIIOutOfMsgCodes": sFTIIIOutOfMsgCodes,
       "secIOEngSupportModulesNotLoaded": secIOEngSupportModulesNotLoaded,
       "errXferDumpToSystem": errXferDumpToSystem,
       "failureCheckingPrimarySrvr": failureCheckingPrimarySrvr,
       "errStarting2ndProcessor": errStarting2ndProcessor,
       "srvrFailure": srvrFailure,
       "srvsSyncing": srvsSyncing,
       "mSLBoardNumberConnEstablished": mSLBoardNumberConnEstablished,
       "secSrvrLANIsBetter": secSrvrLANIsBetter,
       "iPXreturningStatusPackets": iPXreturningStatusPackets,
       "iPXnotReturningStatCheckPackets": iPXnotReturningStatCheckPackets,
       "iPXnotReturningStatPcktLANJammed": iPXnotReturningStatPcktLANJammed,
       "failReasonByOtherSrvr": failReasonByOtherSrvr,
       "iPXInternetIsJammed": iPXInternetIsJammed,
       "iPXTooSlowForSecSrvr": iPXTooSlowForSecSrvr,
       "otherSrvrTooManyHops": otherSrvrTooManyHops,
       "iPXappearsDown": iPXappearsDown,
       "iPXFoundRouteToOtherSrvr": iPXFoundRouteToOtherSrvr,
       "iPXNewRouteToSecSrvr": iPXNewRouteToSecSrvr,
       "iPXLostRoute": iPXLostRoute,
       "secSrvrGoingToDie": secSrvrGoingToDie,
       "priSrvrDyingTimerReStart": priSrvrDyingTimerReStart,
       "priSrvrDying": priSrvrDying,
       "noMemForOtherIOEngScreen": noMemForOtherIOEngScreen,
       "timesyncErrorMsg": timesyncErrorMsg,
       "dsAlertSetServerDown": dsAlertSetServerDown,
       "dsAlertSetServerUp": dsAlertSetServerUp,
       "redirectTableMismatch": redirectTableMismatch,
       "nlmAlertMajor": nlmAlertMajor,
       "nlmAlertMinor": nlmAlertMinor,
       "nlmAlertInformational": nlmAlertInformational,
       "trapinfo": trapinfo,
       "memoryAddress": memoryAddress,
       "auditEventNumber": auditEventNumber,
       "blockNumber": blockNumber,
       "numberOfBlocks": numberOfBlocks,
       "packetSize": packetSize,
       "boardNumber": boardNumber,
       "codeOffset": codeOffset,
       "connectionNumber": connectionNumber,
       "dataStreamNumber": dataStreamNumber,
       "diskSpace": diskSpace,
       "domainName": domainName,
       "resourceDescription": resourceDescription,
       "deviceName": deviceName,
       "dosType": dosType,
       "errorNumber": errorNumber,
       "exceptionName": exceptionName,
       "eipAddress": eipAddress,
       "fileName": fileName,
       "pathName": pathName,
       "fileOffset": fileOffset,
       "ncpFunctionNumber": ncpFunctionNumber,
       "fileSize": fileSize,
       "fileValue": fileValue,
       "fileLength": fileLength,
       "interruptNumber": interruptNumber,
       "nlmName": nlmName,
       "mediaLabel": mediaLabel,
       "message": message,
       "numberOfFailedMemoryAllocAttempts": numberOfFailedMemoryAllocAttempts,
       "numberOfResources": numberOfResources,
       "networkAddress": networkAddress,
       "numberOfFailedFileLockRequests": numberOfFailedFileLockRequests,
       "processName": processName,
       "partitionNumber": partitionNumber,
       "protocolName": protocolName,
       "numberOfPackets": numberOfPackets,
       "resourceName": resourceName,
       "numberOfFailedRecordLockRequests": numberOfFailedRecordLockRequests,
       "serverName": serverName,
       "stationNumber": stationNumber,
       "networkAddress1": networkAddress1,
       "ncpSubFunctionNumber": ncpSubFunctionNumber,
       "nlmSeverity": nlmSeverity,
       "trapTime": trapTime,
       "taskNumber": taskNumber,
       "numberOfTransactions": numberOfTransactions,
       "serverTime": serverTime,
       "pathFileName": pathFileName,
       "userName": userName,
       "volumeName": volumeName,
       "volumeNumber": volumeNumber,
       "lanDriverName": lanDriverName,
       "routerName": routerName,
       "macAddress": macAddress,
       "macAddress1": macAddress1,
       "numberOfConnections": numberOfConnections,
       "socketNumber": socketNumber,
       "accountName": accountName,
       "fileMiscInfo": fileMiscInfo,
       "callBackNumber": callBackNumber,
       "baudRate": baudRate,
       "objectName": objectName,
       "userName1": userName1,
       "dosType1": dosType1,
       "blockNumber1": blockNumber1,
       "internalNetworkAddress": internalNetworkAddress,
       "internalNetworkAddress1": internalNetworkAddress1,
       "macAddress2": macAddress2,
       "serverName1": serverName1,
       "socketNumber1": socketNumber1,
       "fileMiscInfo1": fileMiscInfo1,
       "fileSize1": fileSize1,
       "fileSize2": fileSize2,
       "packetSize1": packetSize1,
       "diskName": diskName,
       "reason": reason,
       "maximumPercent": maximumPercent,
       "iRamLength": iRamLength,
       "iTimerTicks": iTimerTicks,
       "pollingLoops": pollingLoops,
       "iHopsCount": iHopsCount,
       "synchronizationRadius": synchronizationRadius,
       "cmmndLnPrmtr": cmmndLnPrmtr,
       "volumePercentage": volumePercentage,
       "szReason": szReason,
       "iRamStart": iRamStart}
)
