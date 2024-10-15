# SNMP MIB module (NetWare-Server-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NetWare-Server-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:08 2024
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

(InternationalDisplayString,
 KBytes) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString",
    "KBytes")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Seconds(Integer32):
    """Custom type Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class IPXNetNumber(OctetString):
    """Custom type IPXNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class TransportDomain(Integer32):
    """Custom type TransportDomain based on Integer32"""
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
        *(("appleTalkDDP", 4),
          ("ip", 3),
          ("ipx", 2),
          ("noAddress", 1))
    )





class TransportAddress(OctetString):
    """Custom type TransportAddress based on OctetString"""




class EngineType(Integer32):
    """Custom type EngineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ioEnginePrimary", 2),
          ("ioEngineSecondary", 3),
          ("msEngine", 1))
    )





class DSTType(OctetString):
    """Custom type DSTType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
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
_NwServer_ObjectIdentity = ObjectIdentity
nwServer = _NwServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 28)
)
_NwSystem_ObjectIdentity = ObjectIdentity
nwSystem = _NwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1)
)


class _NwSysServerName_Type(InternationalDisplayString):
    """Custom type nwSysServerName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_NwSysServerName_Type.__name__ = "InternationalDisplayString"
_NwSysServerName_Object = MibScalar
nwSysServerName = _NwSysServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 1),
    _NwSysServerName_Type()
)
nwSysServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysServerName.setStatus("mandatory")
_NwSysSerialNumber_Type = InternationalDisplayString
_NwSysSerialNumber_Object = MibScalar
nwSysSerialNumber = _NwSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 2),
    _NwSysSerialNumber_Type()
)
nwSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysSerialNumber.setStatus("mandatory")
_NwSysInternalNetNum_Type = IPXNetNumber
_NwSysInternalNetNum_Object = MibScalar
nwSysInternalNetNum = _NwSysInternalNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 3),
    _NwSysInternalNetNum_Type()
)
nwSysInternalNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysInternalNetNum.setStatus("mandatory")
_NwSysServerUpTime_Type = TimeTicks
_NwSysServerUpTime_Object = MibScalar
nwSysServerUpTime = _NwSysServerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 4),
    _NwSysServerUpTime_Type()
)
nwSysServerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysServerUpTime.setStatus("mandatory")


class _NwSysOSSFTLevel_Type(Integer32):
    """Custom type nwSysOSSFTLevel based on Integer32"""
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
        *(("other", 1),
          ("sftI", 2),
          ("sftII", 3),
          ("sftIII", 4))
    )


_NwSysOSSFTLevel_Type.__name__ = "Integer32"
_NwSysOSSFTLevel_Object = MibScalar
nwSysOSSFTLevel = _NwSysOSSFTLevel_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 5),
    _NwSysOSSFTLevel_Type()
)
nwSysOSSFTLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysOSSFTLevel.setStatus("mandatory")
_NwSysOSMajorVer_Type = Integer32
_NwSysOSMajorVer_Object = MibScalar
nwSysOSMajorVer = _NwSysOSMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 6),
    _NwSysOSMajorVer_Type()
)
nwSysOSMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysOSMajorVer.setStatus("mandatory")
_NwSysOSMinorVer_Type = Integer32
_NwSysOSMinorVer_Object = MibScalar
nwSysOSMinorVer = _NwSysOSMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 7),
    _NwSysOSMinorVer_Type()
)
nwSysOSMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysOSMinorVer.setStatus("mandatory")
_NwSysOSReleaseDate_Type = DateAndTime
_NwSysOSReleaseDate_Object = MibScalar
nwSysOSReleaseDate = _NwSysOSReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 8),
    _NwSysOSReleaseDate_Type()
)
nwSysOSReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysOSReleaseDate.setStatus("mandatory")


class _NwSysOSDescription_Type(InternationalDisplayString):
    """Custom type nwSysOSDescription based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NwSysOSDescription_Type.__name__ = "InternationalDisplayString"
_NwSysOSDescription_Object = MibScalar
nwSysOSDescription = _NwSysOSDescription_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 9),
    _NwSysOSDescription_Type()
)
nwSysOSDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysOSDescription.setStatus("mandatory")
_NwSysOSCopyright_Type = InternationalDisplayString
_NwSysOSCopyright_Object = MibScalar
nwSysOSCopyright = _NwSysOSCopyright_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 10),
    _NwSysOSCopyright_Type()
)
nwSysOSCopyright.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysOSCopyright.setStatus("mandatory")
_NwSysTime_Type = DateAndTime
_NwSysTime_Object = MibScalar
nwSysTime = _NwSysTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 11),
    _NwSysTime_Type()
)
nwSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwSysTime.setStatus("mandatory")


class _NwSysTimeZone_Type(InternationalDisplayString):
    """Custom type nwSysTimeZone based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NwSysTimeZone_Type.__name__ = "InternationalDisplayString"
_NwSysTimeZone_Object = MibScalar
nwSysTimeZone = _NwSysTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 12),
    _NwSysTimeZone_Type()
)
nwSysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwSysTimeZone.setStatus("mandatory")


class _NwSysLoginState_Type(Integer32):
    """Custom type nwSysLoginState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("notApplicable", 1))
    )


_NwSysLoginState_Type.__name__ = "Integer32"
_NwSysLoginState_Object = MibScalar
nwSysLoginState = _NwSysLoginState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 13),
    _NwSysLoginState_Type()
)
nwSysLoginState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwSysLoginState.setStatus("mandatory")


class _NwSysLanguageID_Type(Integer32):
    """Custom type nwSysLanguageID based on Integer32"""
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
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("canadianFrench", 2),
          ("chinese", 3),
          ("danish", 4),
          ("dutch", 5),
          ("english", 6),
          ("finnish", 7),
          ("french", 8),
          ("german", 9),
          ("italian", 10),
          ("japanese", 11),
          ("other", 1),
          ("portuguese", 14),
          ("russian", 15),
          ("spanish", 16),
          ("swedish", 17))
    )


_NwSysLanguageID_Type.__name__ = "Integer32"
_NwSysLanguageID_Object = MibScalar
nwSysLanguageID = _NwSysLanguageID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 14),
    _NwSysLanguageID_Type()
)
nwSysLanguageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysLanguageID.setStatus("mandatory")
_NwSysNMASerialNumber_Type = InternationalDisplayString
_NwSysNMASerialNumber_Object = MibScalar
nwSysNMASerialNumber = _NwSysNMASerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 15),
    _NwSysNMASerialNumber_Type()
)
nwSysNMASerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysNMASerialNumber.setStatus("mandatory")
_NwSysNMACopiesAllowed_Type = Integer32
_NwSysNMACopiesAllowed_Object = MibScalar
nwSysNMACopiesAllowed = _NwSysNMACopiesAllowed_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 16),
    _NwSysNMACopiesAllowed_Type()
)
nwSysNMACopiesAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysNMACopiesAllowed.setStatus("mandatory")
_NwSysDirectoryTree_Type = InternationalDisplayString
_NwSysDirectoryTree_Object = MibScalar
nwSysDirectoryTree = _NwSysDirectoryTree_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 17),
    _NwSysDirectoryTree_Type()
)
nwSysDirectoryTree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysDirectoryTree.setStatus("mandatory")
_NwSysBinderyContext_Type = InternationalDisplayString
_NwSysBinderyContext_Object = MibScalar
nwSysBinderyContext = _NwSysBinderyContext_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 18),
    _NwSysBinderyContext_Type()
)
nwSysBinderyContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysBinderyContext.setStatus("mandatory")
_NwSysServerDSName_Type = InternationalDisplayString
_NwSysServerDSName_Object = MibScalar
nwSysServerDSName = _NwSysServerDSName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 19),
    _NwSysServerDSName_Type()
)
nwSysServerDSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysServerDSName.setStatus("mandatory")
_NwSysDaylightSavingsStart_Type = DSTType
_NwSysDaylightSavingsStart_Object = MibScalar
nwSysDaylightSavingsStart = _NwSysDaylightSavingsStart_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 20),
    _NwSysDaylightSavingsStart_Type()
)
nwSysDaylightSavingsStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysDaylightSavingsStart.setStatus("mandatory")
_NwSysDaylightSavingsEnd_Type = DSTType
_NwSysDaylightSavingsEnd_Object = MibScalar
nwSysDaylightSavingsEnd = _NwSysDaylightSavingsEnd_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 21),
    _NwSysDaylightSavingsEnd_Type()
)
nwSysDaylightSavingsEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysDaylightSavingsEnd.setStatus("mandatory")
_NwSysDaylightSavingsOffset_Type = Integer32
_NwSysDaylightSavingsOffset_Object = MibScalar
nwSysDaylightSavingsOffset = _NwSysDaylightSavingsOffset_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 22),
    _NwSysDaylightSavingsOffset_Type()
)
nwSysDaylightSavingsOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysDaylightSavingsOffset.setStatus("mandatory")


class _NwSysDaylightSavingsStatus_Type(Integer32):
    """Custom type nwSysDaylightSavingsStatus based on Integer32"""
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


_NwSysDaylightSavingsStatus_Type.__name__ = "Integer32"
_NwSysDaylightSavingsStatus_Object = MibScalar
nwSysDaylightSavingsStatus = _NwSysDaylightSavingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 1, 23),
    _NwSysDaylightSavingsStatus_Type()
)
nwSysDaylightSavingsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSysDaylightSavingsStatus.setStatus("mandatory")
_NwFileSystem_ObjectIdentity = ObjectIdentity
nwFileSystem = _NwFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2)
)
_NwFSReads_Type = Counter32
_NwFSReads_Object = MibScalar
nwFSReads = _NwFSReads_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 1),
    _NwFSReads_Type()
)
nwFSReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSReads.setStatus("mandatory")
_NwFSWrites_Type = Counter32
_NwFSWrites_Object = MibScalar
nwFSWrites = _NwFSWrites_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 2),
    _NwFSWrites_Type()
)
nwFSWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSWrites.setStatus("mandatory")
_NwFSReadKBytes_Type = Counter32
_NwFSReadKBytes_Object = MibScalar
nwFSReadKBytes = _NwFSReadKBytes_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 3),
    _NwFSReadKBytes_Type()
)
nwFSReadKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSReadKBytes.setStatus("mandatory")
_NwFSWrittenKBytes_Type = Counter32
_NwFSWrittenKBytes_Object = MibScalar
nwFSWrittenKBytes = _NwFSWrittenKBytes_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 4),
    _NwFSWrittenKBytes_Type()
)
nwFSWrittenKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSWrittenKBytes.setStatus("mandatory")
_NwFSCacheChecks_Type = Counter32
_NwFSCacheChecks_Object = MibScalar
nwFSCacheChecks = _NwFSCacheChecks_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 5),
    _NwFSCacheChecks_Type()
)
nwFSCacheChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSCacheChecks.setStatus("mandatory")
_NwFSCacheHits_Type = Counter32
_NwFSCacheHits_Object = MibScalar
nwFSCacheHits = _NwFSCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 6),
    _NwFSCacheHits_Type()
)
nwFSCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSCacheHits.setStatus("mandatory")
_NwFSOpenFiles_Type = Integer32
_NwFSOpenFiles_Object = MibScalar
nwFSOpenFiles = _NwFSOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 7),
    _NwFSOpenFiles_Type()
)
nwFSOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSOpenFiles.setStatus("mandatory")
_NwFSMaxOpenFiles_Type = Integer32
_NwFSMaxOpenFiles_Object = MibScalar
nwFSMaxOpenFiles = _NwFSMaxOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 8),
    _NwFSMaxOpenFiles_Type()
)
nwFSMaxOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSMaxOpenFiles.setStatus("mandatory")
_NwFSRecordLocks_Type = Integer32
_NwFSRecordLocks_Object = MibScalar
nwFSRecordLocks = _NwFSRecordLocks_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 9),
    _NwFSRecordLocks_Type()
)
nwFSRecordLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSRecordLocks.setStatus("mandatory")
_NwFSMaxRecordLocks_Type = Integer32
_NwFSMaxRecordLocks_Object = MibScalar
nwFSMaxRecordLocks = _NwFSMaxRecordLocks_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 10),
    _NwFSMaxRecordLocks_Type()
)
nwFSMaxRecordLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSMaxRecordLocks.setStatus("mandatory")
_NwFSMaxSubdirectoryTreeDepth_Type = Integer32
_NwFSMaxSubdirectoryTreeDepth_Object = MibScalar
nwFSMaxSubdirectoryTreeDepth = _NwFSMaxSubdirectoryTreeDepth_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 11),
    _NwFSMaxSubdirectoryTreeDepth_Type()
)
nwFSMaxSubdirectoryTreeDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSMaxSubdirectoryTreeDepth.setStatus("mandatory")


class _NwFSMaxPercentOfVolumeUsedByDir_Type(Integer32):
    """Custom type nwFSMaxPercentOfVolumeUsedByDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NwFSMaxPercentOfVolumeUsedByDir_Type.__name__ = "Integer32"
_NwFSMaxPercentOfVolumeUsedByDir_Object = MibScalar
nwFSMaxPercentOfVolumeUsedByDir = _NwFSMaxPercentOfVolumeUsedByDir_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 12),
    _NwFSMaxPercentOfVolumeUsedByDir_Type()
)
nwFSMaxPercentOfVolumeUsedByDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSMaxPercentOfVolumeUsedByDir.setStatus("mandatory")
_NwFSVolCount_Type = Integer32
_NwFSVolCount_Object = MibScalar
nwFSVolCount = _NwFSVolCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 13),
    _NwFSVolCount_Type()
)
nwFSVolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFSVolCount.setStatus("mandatory")
_NwFSVolTable_Object = MibTable
nwFSVolTable = _NwFSVolTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14)
)
if mibBuilder.loadTexts:
    nwFSVolTable.setStatus("mandatory")
_NwFSVolEntry_Object = MibTableRow
nwFSVolEntry = _NwFSVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1)
)
nwFSVolEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwVolID"),
)
if mibBuilder.loadTexts:
    nwFSVolEntry.setStatus("mandatory")


class _NwVolID_Type(Integer32):
    """Custom type nwVolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwVolID_Type.__name__ = "Integer32"
_NwVolID_Object = MibTableColumn
nwVolID = _NwVolID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 1),
    _NwVolID_Type()
)
nwVolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolID.setStatus("mandatory")


class _NwVolPhysicalName_Type(InternationalDisplayString):
    """Custom type nwVolPhysicalName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NwVolPhysicalName_Type.__name__ = "InternationalDisplayString"
_NwVolPhysicalName_Object = MibTableColumn
nwVolPhysicalName = _NwVolPhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 2),
    _NwVolPhysicalName_Type()
)
nwVolPhysicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolPhysicalName.setStatus("mandatory")
_NwVolSize_Type = KBytes
_NwVolSize_Object = MibTableColumn
nwVolSize = _NwVolSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 3),
    _NwVolSize_Type()
)
nwVolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolSize.setStatus("mandatory")
_NwVolFree_Type = KBytes
_NwVolFree_Object = MibTableColumn
nwVolFree = _NwVolFree_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 4),
    _NwVolFree_Type()
)
nwVolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolFree.setStatus("mandatory")
_NwVolFreeable_Type = KBytes
_NwVolFreeable_Object = MibTableColumn
nwVolFreeable = _NwVolFreeable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 5),
    _NwVolFreeable_Type()
)
nwVolFreeable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolFreeable.setStatus("mandatory")
_NwVolNonFreeable_Type = KBytes
_NwVolNonFreeable_Object = MibTableColumn
nwVolNonFreeable = _NwVolNonFreeable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 6),
    _NwVolNonFreeable_Type()
)
nwVolNonFreeable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolNonFreeable.setStatus("mandatory")
_NwVolBlockSize_Type = Integer32
_NwVolBlockSize_Object = MibTableColumn
nwVolBlockSize = _NwVolBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 7),
    _NwVolBlockSize_Type()
)
nwVolBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolBlockSize.setStatus("mandatory")


class _NwVolMounted_Type(Integer32):
    """Custom type nwVolMounted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dismounted", 2),
          ("mounted", 1))
    )


_NwVolMounted_Type.__name__ = "Integer32"
_NwVolMounted_Object = MibTableColumn
nwVolMounted = _NwVolMounted_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 8),
    _NwVolMounted_Type()
)
nwVolMounted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwVolMounted.setStatus("mandatory")


class _NwVolAttributes_Type(Integer32):
    """Custom type nwVolAttributes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_NwVolAttributes_Type.__name__ = "Integer32"
_NwVolAttributes_Object = MibTableColumn
nwVolAttributes = _NwVolAttributes_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 9),
    _NwVolAttributes_Type()
)
nwVolAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolAttributes.setStatus("mandatory")


class _NwVolNameSpaces_Type(Integer32):
    """Custom type nwVolNameSpaces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NwVolNameSpaces_Type.__name__ = "Integer32"
_NwVolNameSpaces_Object = MibTableColumn
nwVolNameSpaces = _NwVolNameSpaces_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 10),
    _NwVolNameSpaces_Type()
)
nwVolNameSpaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolNameSpaces.setStatus("mandatory")
_NwVolTotalDirEntries_Type = Integer32
_NwVolTotalDirEntries_Object = MibTableColumn
nwVolTotalDirEntries = _NwVolTotalDirEntries_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 11),
    _NwVolTotalDirEntries_Type()
)
nwVolTotalDirEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolTotalDirEntries.setStatus("mandatory")
_NwVolUsedDirEntries_Type = Integer32
_NwVolUsedDirEntries_Object = MibTableColumn
nwVolUsedDirEntries = _NwVolUsedDirEntries_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 12),
    _NwVolUsedDirEntries_Type()
)
nwVolUsedDirEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolUsedDirEntries.setStatus("mandatory")
_NwVolSegmentCount_Type = Integer32
_NwVolSegmentCount_Object = MibTableColumn
nwVolSegmentCount = _NwVolSegmentCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 13),
    _NwVolSegmentCount_Type()
)
nwVolSegmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolSegmentCount.setStatus("mandatory")
_NwVolDSName_Type = InternationalDisplayString
_NwVolDSName_Object = MibTableColumn
nwVolDSName = _NwVolDSName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 14),
    _NwVolDSName_Type()
)
nwVolDSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolDSName.setStatus("mandatory")


class _NwVolFileSystemID_Type(Integer32):
    """Custom type nwVolFileSystemID based on Integer32"""
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
        *(("netWareVolume", 3),
          ("nfsVolume", 4),
          ("other", 1),
          ("unknown", 2))
    )


_NwVolFileSystemID_Type.__name__ = "Integer32"
_NwVolFileSystemID_Object = MibTableColumn
nwVolFileSystemID = _NwVolFileSystemID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 15),
    _NwVolFileSystemID_Type()
)
nwVolFileSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolFileSystemID.setStatus("mandatory")
_NwVolFileSystemName_Type = InternationalDisplayString
_NwVolFileSystemName_Object = MibTableColumn
nwVolFileSystemName = _NwVolFileSystemName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 14, 1, 16),
    _NwVolFileSystemName_Type()
)
nwVolFileSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolFileSystemName.setStatus("mandatory")
_NwFSOpenFileTable_Object = MibTable
nwFSOpenFileTable = _NwFSOpenFileTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 15)
)
if mibBuilder.loadTexts:
    nwFSOpenFileTable.setStatus("mandatory")
_NwFSOpenFileEntry_Object = MibTableRow
nwFSOpenFileEntry = _NwFSOpenFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 15, 1)
)
nwFSOpenFileEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwOfileVolID"),
    (0, "NetWare-Server-MIB", "nwOfileDirectoryNumber"),
    (0, "NetWare-Server-MIB", "nwOfileConnection"),
)
if mibBuilder.loadTexts:
    nwFSOpenFileEntry.setStatus("mandatory")


class _NwOfileVolID_Type(Integer32):
    """Custom type nwOfileVolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwOfileVolID_Type.__name__ = "Integer32"
_NwOfileVolID_Object = MibTableColumn
nwOfileVolID = _NwOfileVolID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 15, 1, 1),
    _NwOfileVolID_Type()
)
nwOfileVolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwOfileVolID.setStatus("mandatory")
_NwOfileDirectoryNumber_Type = Integer32
_NwOfileDirectoryNumber_Object = MibTableColumn
nwOfileDirectoryNumber = _NwOfileDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 15, 1, 2),
    _NwOfileDirectoryNumber_Type()
)
nwOfileDirectoryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwOfileDirectoryNumber.setStatus("mandatory")
_NwOfileConnection_Type = Integer32
_NwOfileConnection_Object = MibTableColumn
nwOfileConnection = _NwOfileConnection_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 15, 1, 3),
    _NwOfileConnection_Type()
)
nwOfileConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwOfileConnection.setStatus("mandatory")


class _NwOfileVolumeName_Type(InternationalDisplayString):
    """Custom type nwOfileVolumeName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NwOfileVolumeName_Type.__name__ = "InternationalDisplayString"
_NwOfileVolumeName_Object = MibTableColumn
nwOfileVolumeName = _NwOfileVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 15, 1, 4),
    _NwOfileVolumeName_Type()
)
nwOfileVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwOfileVolumeName.setStatus("mandatory")


class _NwOfileName_Type(InternationalDisplayString):
    """Custom type nwOfileName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_NwOfileName_Type.__name__ = "InternationalDisplayString"
_NwOfileName_Object = MibTableColumn
nwOfileName = _NwOfileName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 15, 1, 5),
    _NwOfileName_Type()
)
nwOfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwOfileName.setStatus("mandatory")
_NwOfileLoginName_Type = InternationalDisplayString
_NwOfileLoginName_Object = MibTableColumn
nwOfileLoginName = _NwOfileLoginName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 2, 15, 1, 6),
    _NwOfileLoginName_Type()
)
nwOfileLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwOfileLoginName.setStatus("mandatory")
_NwUsers_ObjectIdentity = ObjectIdentity
nwUsers = _NwUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3)
)
_NwUserCount_Type = Integer32
_NwUserCount_Object = MibScalar
nwUserCount = _NwUserCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 1),
    _NwUserCount_Type()
)
nwUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserCount.setStatus("mandatory")
_NwLoginCount_Type = Integer32
_NwLoginCount_Object = MibScalar
nwLoginCount = _NwLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 2),
    _NwLoginCount_Type()
)
nwLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwLoginCount.setStatus("mandatory")
_NwMaxLogins_Type = Integer32
_NwMaxLogins_Object = MibScalar
nwMaxLogins = _NwMaxLogins_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 3),
    _NwMaxLogins_Type()
)
nwMaxLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwMaxLogins.setStatus("mandatory")
_NwConnectionCount_Type = Integer32
_NwConnectionCount_Object = MibScalar
nwConnectionCount = _NwConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 4),
    _NwConnectionCount_Type()
)
nwConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionCount.setStatus("mandatory")
_NwPeakRemoteConnections_Type = Integer32
_NwPeakRemoteConnections_Object = MibScalar
nwPeakRemoteConnections = _NwPeakRemoteConnections_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 5),
    _NwPeakRemoteConnections_Type()
)
nwPeakRemoteConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwPeakRemoteConnections.setStatus("mandatory")
_NwMaxConnections_Type = Integer32
_NwMaxConnections_Object = MibScalar
nwMaxConnections = _NwMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 6),
    _NwMaxConnections_Type()
)
nwMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwMaxConnections.setStatus("mandatory")
_NwNLMConnections_Type = Integer32
_NwNLMConnections_Object = MibScalar
nwNLMConnections = _NwNLMConnections_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 7),
    _NwNLMConnections_Type()
)
nwNLMConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNLMConnections.setStatus("mandatory")
_NwConnectionTable_Object = MibTable
nwConnectionTable = _NwConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8)
)
if mibBuilder.loadTexts:
    nwConnectionTable.setStatus("mandatory")
_NwConnectionEntry_Object = MibTableRow
nwConnectionEntry = _NwConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1)
)
nwConnectionEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwConnectionNumber"),
)
if mibBuilder.loadTexts:
    nwConnectionEntry.setStatus("mandatory")
_NwConnectionNumber_Type = Integer32
_NwConnectionNumber_Object = MibTableColumn
nwConnectionNumber = _NwConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1, 1),
    _NwConnectionNumber_Type()
)
nwConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionNumber.setStatus("mandatory")
_NwConnectionLoginName_Type = InternationalDisplayString
_NwConnectionLoginName_Object = MibTableColumn
nwConnectionLoginName = _NwConnectionLoginName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1, 2),
    _NwConnectionLoginName_Type()
)
nwConnectionLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionLoginName.setStatus("mandatory")
_NwConnectionTransportDomain_Type = TransportDomain
_NwConnectionTransportDomain_Object = MibTableColumn
nwConnectionTransportDomain = _NwConnectionTransportDomain_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1, 3),
    _NwConnectionTransportDomain_Type()
)
nwConnectionTransportDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionTransportDomain.setStatus("mandatory")
_NwConnectionTransportAddress_Type = TransportAddress
_NwConnectionTransportAddress_Object = MibTableColumn
nwConnectionTransportAddress = _NwConnectionTransportAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1, 4),
    _NwConnectionTransportAddress_Type()
)
nwConnectionTransportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionTransportAddress.setStatus("mandatory")
_NwConnectionTime_Type = DateAndTime
_NwConnectionTime_Object = MibTableColumn
nwConnectionTime = _NwConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1, 5),
    _NwConnectionTime_Type()
)
nwConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionTime.setStatus("mandatory")
_NwConnectionReadKBytes_Type = Counter32
_NwConnectionReadKBytes_Object = MibTableColumn
nwConnectionReadKBytes = _NwConnectionReadKBytes_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1, 6),
    _NwConnectionReadKBytes_Type()
)
nwConnectionReadKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionReadKBytes.setStatus("mandatory")
_NwConnectionWrittenKBytes_Type = Counter32
_NwConnectionWrittenKBytes_Object = MibTableColumn
nwConnectionWrittenKBytes = _NwConnectionWrittenKBytes_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1, 7),
    _NwConnectionWrittenKBytes_Type()
)
nwConnectionWrittenKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionWrittenKBytes.setStatus("mandatory")
_NwConnectionNcpRequests_Type = Counter32
_NwConnectionNcpRequests_Object = MibTableColumn
nwConnectionNcpRequests = _NwConnectionNcpRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1, 8),
    _NwConnectionNcpRequests_Type()
)
nwConnectionNcpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionNcpRequests.setStatus("mandatory")
_NwConnectionFilesOpen_Type = Integer32
_NwConnectionFilesOpen_Object = MibTableColumn
nwConnectionFilesOpen = _NwConnectionFilesOpen_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1, 9),
    _NwConnectionFilesOpen_Type()
)
nwConnectionFilesOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionFilesOpen.setStatus("mandatory")
_NwConnectionRecordsLocked_Type = Integer32
_NwConnectionRecordsLocked_Object = MibTableColumn
nwConnectionRecordsLocked = _NwConnectionRecordsLocked_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1, 10),
    _NwConnectionRecordsLocked_Type()
)
nwConnectionRecordsLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionRecordsLocked.setStatus("mandatory")


class _NwConnectionPrivilege_Type(Integer32):
    """Custom type nwConnectionPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NwConnectionPrivilege_Type.__name__ = "Integer32"
_NwConnectionPrivilege_Object = MibTableColumn
nwConnectionPrivilege = _NwConnectionPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1, 11),
    _NwConnectionPrivilege_Type()
)
nwConnectionPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionPrivilege.setStatus("mandatory")


class _NwConnectionStatus_Type(Integer32):
    """Custom type nwConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_NwConnectionStatus_Type.__name__ = "Integer32"
_NwConnectionStatus_Object = MibTableColumn
nwConnectionStatus = _NwConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 3, 8, 1, 12),
    _NwConnectionStatus_Type()
)
nwConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConnectionStatus.setStatus("mandatory")
_NwQueue_ObjectIdentity = ObjectIdentity
nwQueue = _NwQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4)
)
_NwQueueCount_Type = Integer32
_NwQueueCount_Object = MibScalar
nwQueueCount = _NwQueueCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 1),
    _NwQueueCount_Type()
)
nwQueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQueueCount.setStatus("mandatory")
_NwQueueTable_Object = MibTable
nwQueueTable = _NwQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 2)
)
if mibBuilder.loadTexts:
    nwQueueTable.setStatus("mandatory")
_NwQueueEntry_Object = MibTableRow
nwQueueEntry = _NwQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 2, 1)
)
nwQueueEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwQID"),
)
if mibBuilder.loadTexts:
    nwQueueEntry.setStatus("mandatory")


class _NwQID_Type(Integer32):
    """Custom type nwQID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwQID_Type.__name__ = "Integer32"
_NwQID_Object = MibTableColumn
nwQID = _NwQID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 2, 1, 1),
    _NwQID_Type()
)
nwQID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQID.setStatus("mandatory")
_NwQName_Type = InternationalDisplayString
_NwQName_Object = MibTableColumn
nwQName = _NwQName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 2, 1, 2),
    _NwQName_Type()
)
nwQName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQName.setStatus("mandatory")


class _NwQType_Type(Integer32):
    """Custom type nwQType based on Integer32"""
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
        *(("archiveQueue", 3),
          ("jobQueue", 4),
          ("other", 1),
          ("printQueue", 2))
    )


_NwQType_Type.__name__ = "Integer32"
_NwQType_Object = MibTableColumn
nwQType = _NwQType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 2, 1, 3),
    _NwQType_Type()
)
nwQType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQType.setStatus("mandatory")


class _NwQAddJobState_Type(Integer32):
    """Custom type nwQAddJobState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("canAddJobs", 1),
          ("cannotAddJobs", 2))
    )


_NwQAddJobState_Type.__name__ = "Integer32"
_NwQAddJobState_Object = MibTableColumn
nwQAddJobState = _NwQAddJobState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 2, 1, 4),
    _NwQAddJobState_Type()
)
nwQAddJobState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQAddJobState.setStatus("mandatory")


class _NwQAttachState_Type(Integer32):
    """Custom type nwQAttachState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("canAttach", 1),
          ("cannotAttach", 2))
    )


_NwQAttachState_Type.__name__ = "Integer32"
_NwQAttachState_Object = MibTableColumn
nwQAttachState = _NwQAttachState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 2, 1, 5),
    _NwQAttachState_Type()
)
nwQAttachState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQAttachState.setStatus("mandatory")


class _NwQServiceJobState_Type(Integer32):
    """Custom type nwQServiceJobState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("canService", 1),
          ("cannotService", 2))
    )


_NwQServiceJobState_Type.__name__ = "Integer32"
_NwQServiceJobState_Object = MibTableColumn
nwQServiceJobState = _NwQServiceJobState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 2, 1, 6),
    _NwQServiceJobState_Type()
)
nwQServiceJobState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQServiceJobState.setStatus("mandatory")


class _NwQDirVolName_Type(InternationalDisplayString):
    """Custom type nwQDirVolName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NwQDirVolName_Type.__name__ = "InternationalDisplayString"
_NwQDirVolName_Object = MibTableColumn
nwQDirVolName = _NwQDirVolName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 2, 1, 7),
    _NwQDirVolName_Type()
)
nwQDirVolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQDirVolName.setStatus("mandatory")
_NwQNumJobEntries_Type = Integer32
_NwQNumJobEntries_Object = MibTableColumn
nwQNumJobEntries = _NwQNumJobEntries_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 2, 1, 8),
    _NwQNumJobEntries_Type()
)
nwQNumJobEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQNumJobEntries.setStatus("mandatory")
_NwQNumAssignedServers_Type = Integer32
_NwQNumAssignedServers_Object = MibTableColumn
nwQNumAssignedServers = _NwQNumAssignedServers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 2, 1, 9),
    _NwQNumAssignedServers_Type()
)
nwQNumAssignedServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQNumAssignedServers.setStatus("mandatory")
_NwQueueJobTable_Object = MibTable
nwQueueJobTable = _NwQueueJobTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3)
)
if mibBuilder.loadTexts:
    nwQueueJobTable.setStatus("mandatory")
_NwQueueJobEntry_Object = MibTableRow
nwQueueJobEntry = _NwQueueJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3, 1)
)
nwQueueJobEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwQJobQID"),
    (0, "NetWare-Server-MIB", "nwQJobNumber"),
)
if mibBuilder.loadTexts:
    nwQueueJobEntry.setStatus("mandatory")


class _NwQJobQID_Type(Integer32):
    """Custom type nwQJobQID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwQJobQID_Type.__name__ = "Integer32"
_NwQJobQID_Object = MibTableColumn
nwQJobQID = _NwQJobQID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3, 1, 1),
    _NwQJobQID_Type()
)
nwQJobQID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQJobQID.setStatus("mandatory")
_NwQJobNumber_Type = Integer32
_NwQJobNumber_Object = MibTableColumn
nwQJobNumber = _NwQJobNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3, 1, 2),
    _NwQJobNumber_Type()
)
nwQJobNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQJobNumber.setStatus("mandatory")


class _NwQJobDescription_Type(InternationalDisplayString):
    """Custom type nwQJobDescription based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NwQJobDescription_Type.__name__ = "InternationalDisplayString"
_NwQJobDescription_Object = MibTableColumn
nwQJobDescription = _NwQJobDescription_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3, 1, 3),
    _NwQJobDescription_Type()
)
nwQJobDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQJobDescription.setStatus("mandatory")
_NwQJobEntryDateTime_Type = DateAndTime
_NwQJobEntryDateTime_Object = MibTableColumn
nwQJobEntryDateTime = _NwQJobEntryDateTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3, 1, 4),
    _NwQJobEntryDateTime_Type()
)
nwQJobEntryDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQJobEntryDateTime.setStatus("mandatory")
_NwQJobPosition_Type = Integer32
_NwQJobPosition_Object = MibTableColumn
nwQJobPosition = _NwQJobPosition_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3, 1, 5),
    _NwQJobPosition_Type()
)
nwQJobPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQJobPosition.setStatus("mandatory")
_NwQJobSize_Type = Integer32
_NwQJobSize_Object = MibTableColumn
nwQJobSize = _NwQJobSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3, 1, 6),
    _NwQJobSize_Type()
)
nwQJobSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQJobSize.setStatus("mandatory")
_NwQJobControlFlags_Type = Integer32
_NwQJobControlFlags_Object = MibTableColumn
nwQJobControlFlags = _NwQJobControlFlags_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3, 1, 7),
    _NwQJobControlFlags_Type()
)
nwQJobControlFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQJobControlFlags.setStatus("mandatory")
_NwQJobUserName_Type = InternationalDisplayString
_NwQJobUserName_Object = MibTableColumn
nwQJobUserName = _NwQJobUserName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3, 1, 8),
    _NwQJobUserName_Type()
)
nwQJobUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQJobUserName.setStatus("mandatory")
_NwQJobTargetServerName_Type = InternationalDisplayString
_NwQJobTargetServerName_Object = MibTableColumn
nwQJobTargetServerName = _NwQJobTargetServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3, 1, 9),
    _NwQJobTargetServerName_Type()
)
nwQJobTargetServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQJobTargetServerName.setStatus("mandatory")
_NwQJobTargetDateTime_Type = DateAndTime
_NwQJobTargetDateTime_Object = MibTableColumn
nwQJobTargetDateTime = _NwQJobTargetDateTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3, 1, 10),
    _NwQJobTargetDateTime_Type()
)
nwQJobTargetDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQJobTargetDateTime.setStatus("mandatory")
_NwQJobServerName_Type = InternationalDisplayString
_NwQJobServerName_Object = MibTableColumn
nwQJobServerName = _NwQJobServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 3, 1, 11),
    _NwQJobServerName_Type()
)
nwQJobServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQJobServerName.setStatus("mandatory")
_NwQueueServerTable_Object = MibTable
nwQueueServerTable = _NwQueueServerTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 4)
)
if mibBuilder.loadTexts:
    nwQueueServerTable.setStatus("mandatory")
_NwQueueServerEntry_Object = MibTableRow
nwQueueServerEntry = _NwQueueServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 4, 1)
)
nwQueueServerEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwQServerQID"),
    (0, "NetWare-Server-MIB", "nwQServerID"),
)
if mibBuilder.loadTexts:
    nwQueueServerEntry.setStatus("mandatory")


class _NwQServerQID_Type(Integer32):
    """Custom type nwQServerQID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwQServerQID_Type.__name__ = "Integer32"
_NwQServerQID_Object = MibTableColumn
nwQServerQID = _NwQServerQID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 4, 1, 1),
    _NwQServerQID_Type()
)
nwQServerQID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQServerQID.setStatus("mandatory")


class _NwQServerID_Type(Integer32):
    """Custom type nwQServerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwQServerID_Type.__name__ = "Integer32"
_NwQServerID_Object = MibTableColumn
nwQServerID = _NwQServerID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 4, 1, 2),
    _NwQServerID_Type()
)
nwQServerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQServerID.setStatus("mandatory")
_NwQServerName_Type = InternationalDisplayString
_NwQServerName_Object = MibTableColumn
nwQServerName = _NwQServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 4, 1, 3),
    _NwQServerName_Type()
)
nwQServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQServerName.setStatus("mandatory")


class _NwQServerStatus_Type(Integer32):
    """Custom type nwQServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("unknown", 1))
    )


_NwQServerStatus_Type.__name__ = "Integer32"
_NwQServerStatus_Object = MibTableColumn
nwQServerStatus = _NwQServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 4, 4, 1, 4),
    _NwQServerStatus_Type()
)
nwQServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwQServerStatus.setStatus("mandatory")
_NwOdi_ObjectIdentity = ObjectIdentity
nwOdi = _NwOdi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 5)
)
_NwOdiLslEnqSendCount_Type = Integer32
_NwOdiLslEnqSendCount_Object = MibScalar
nwOdiLslEnqSendCount = _NwOdiLslEnqSendCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 5, 1),
    _NwOdiLslEnqSendCount_Type()
)
nwOdiLslEnqSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwOdiLslEnqSendCount.setStatus("mandatory")
_NwOdiOsPktRcvBuffer_Type = Integer32
_NwOdiOsPktRcvBuffer_Object = MibScalar
nwOdiOsPktRcvBuffer = _NwOdiOsPktRcvBuffer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 5, 2),
    _NwOdiOsPktRcvBuffer_Type()
)
nwOdiOsPktRcvBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwOdiOsPktRcvBuffer.setStatus("mandatory")
_NwOdiOsMaxPktRcvBuffers_Type = Integer32
_NwOdiOsMaxPktRcvBuffers_Object = MibScalar
nwOdiOsMaxPktRcvBuffers = _NwOdiOsMaxPktRcvBuffers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 5, 3),
    _NwOdiOsMaxPktRcvBuffers_Type()
)
nwOdiOsMaxPktRcvBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwOdiOsMaxPktRcvBuffers.setStatus("mandatory")
_NwOdiOsMinPktRcvBuffers_Type = Integer32
_NwOdiOsMinPktRcvBuffers_Object = MibScalar
nwOdiOsMinPktRcvBuffers = _NwOdiOsMinPktRcvBuffers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 5, 4),
    _NwOdiOsMinPktRcvBuffers_Type()
)
nwOdiOsMinPktRcvBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwOdiOsMinPktRcvBuffers.setStatus("mandatory")
_NwSft3_ObjectIdentity = ObjectIdentity
nwSft3 = _NwSft3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 6)
)
_NwSft3Engine_Type = EngineType
_NwSft3Engine_Object = MibScalar
nwSft3Engine = _NwSft3Engine_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 6, 1),
    _NwSft3Engine_Type()
)
nwSft3Engine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSft3Engine.setStatus("mandatory")


class _NwSft3EngineState_Type(Integer32):
    """Custom type nwSft3EngineState based on Integer32"""
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
        *(("down", 5),
          ("mirrored", 3),
          ("noSecondary", 4),
          ("synchronizing", 2),
          ("unknown", 1))
    )


_NwSft3EngineState_Type.__name__ = "Integer32"
_NwSft3EngineState_Object = MibScalar
nwSft3EngineState = _NwSft3EngineState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 6, 2),
    _NwSft3EngineState_Type()
)
nwSft3EngineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSft3EngineState.setStatus("mandatory")
_NwSft3EngineTable_Object = MibTable
nwSft3EngineTable = _NwSft3EngineTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 6, 3)
)
if mibBuilder.loadTexts:
    nwSft3EngineTable.setStatus("mandatory")
_NwSft3EngineEntry_Object = MibTableRow
nwSft3EngineEntry = _NwSft3EngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 6, 3, 1)
)
nwSft3EngineEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwSft3EngineType"),
)
if mibBuilder.loadTexts:
    nwSft3EngineEntry.setStatus("mandatory")
_NwSft3EngineType_Type = EngineType
_NwSft3EngineType_Object = MibTableColumn
nwSft3EngineType = _NwSft3EngineType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 6, 3, 1, 1),
    _NwSft3EngineType_Type()
)
nwSft3EngineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSft3EngineType.setStatus("mandatory")
_NwSft3EngineName_Type = InternationalDisplayString
_NwSft3EngineName_Object = MibTableColumn
nwSft3EngineName = _NwSft3EngineName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 6, 3, 1, 2),
    _NwSft3EngineName_Type()
)
nwSft3EngineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSft3EngineName.setStatus("mandatory")
_NwSft3EngineInternalNetNum_Type = IPXNetNumber
_NwSft3EngineInternalNetNum_Object = MibTableColumn
nwSft3EngineInternalNetNum = _NwSft3EngineInternalNetNum_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 6, 3, 1, 3),
    _NwSft3EngineInternalNetNum_Type()
)
nwSft3EngineInternalNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSft3EngineInternalNetNum.setStatus("mandatory")
_NwNCP_ObjectIdentity = ObjectIdentity
nwNCP = _NwNCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7)
)


class _NwNCPIPXChecksums_Type(Integer32):
    """Custom type nwNCPIPXChecksums based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("checksumIfEnabledAtClient", 2),
          ("noChecksums", 1),
          ("requireChecksums", 3))
    )


_NwNCPIPXChecksums_Type.__name__ = "Integer32"
_NwNCPIPXChecksums_Object = MibScalar
nwNCPIPXChecksums = _NwNCPIPXChecksums_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7, 1),
    _NwNCPIPXChecksums_Type()
)
nwNCPIPXChecksums.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNCPIPXChecksums.setStatus("mandatory")


class _NwNCPPacketSignatures_Type(Integer32):
    """Custom type nwNCPPacketSignatures based on Integer32"""
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
        *(("serverMandatesSigning", 4),
          ("serverNeverSigns", 1),
          ("serverSignsIfClientCapable", 3),
          ("serverSignsOnClientRequest", 2))
    )


_NwNCPPacketSignatures_Type.__name__ = "Integer32"
_NwNCPPacketSignatures_Object = MibScalar
nwNCPPacketSignatures = _NwNCPPacketSignatures_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7, 2),
    _NwNCPPacketSignatures_Type()
)
nwNCPPacketSignatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNCPPacketSignatures.setStatus("mandatory")
_NwNCPNumNCPReqs_Type = Counter32
_NwNCPNumNCPReqs_Object = MibScalar
nwNCPNumNCPReqs = _NwNCPNumNCPReqs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7, 3),
    _NwNCPNumNCPReqs_Type()
)
nwNCPNumNCPReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNCPNumNCPReqs.setStatus("mandatory")
_NwNCPUseCount_Type = Integer32
_NwNCPUseCount_Object = MibScalar
nwNCPUseCount = _NwNCPUseCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7, 4),
    _NwNCPUseCount_Type()
)
nwNCPUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNCPUseCount.setStatus("mandatory")
_NwNCPPeakUseCount_Type = Integer32
_NwNCPPeakUseCount_Object = MibScalar
nwNCPPeakUseCount = _NwNCPPeakUseCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7, 5),
    _NwNCPPeakUseCount_Type()
)
nwNCPPeakUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNCPPeakUseCount.setStatus("mandatory")
_NwNCPForgedPkts_Type = Counter32
_NwNCPForgedPkts_Object = MibScalar
nwNCPForgedPkts = _NwNCPForgedPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7, 6),
    _NwNCPForgedPkts_Type()
)
nwNCPForgedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNCPForgedPkts.setStatus("mandatory")
_NwNCPBeingProcesseds_Type = Counter32
_NwNCPBeingProcesseds_Object = MibScalar
nwNCPBeingProcesseds = _NwNCPBeingProcesseds_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7, 7),
    _NwNCPBeingProcesseds_Type()
)
nwNCPBeingProcesseds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNCPBeingProcesseds.setStatus("mandatory")
_NwNCPNoAvailConns_Type = Counter32
_NwNCPNoAvailConns_Object = MibScalar
nwNCPNoAvailConns = _NwNCPNoAvailConns_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7, 8),
    _NwNCPNoAvailConns_Type()
)
nwNCPNoAvailConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNCPNoAvailConns.setStatus("mandatory")
_NwNCPIPXChecksumErrs_Type = Counter32
_NwNCPIPXChecksumErrs_Object = MibScalar
nwNCPIPXChecksumErrs = _NwNCPIPXChecksumErrs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7, 9),
    _NwNCPIPXChecksumErrs_Type()
)
nwNCPIPXChecksumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNCPIPXChecksumErrs.setStatus("mandatory")
_NwNCPInvalidPacketSigs_Type = Counter32
_NwNCPInvalidPacketSigs_Object = MibScalar
nwNCPInvalidPacketSigs = _NwNCPInvalidPacketSigs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7, 10),
    _NwNCPInvalidPacketSigs_Type()
)
nwNCPInvalidPacketSigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNCPInvalidPacketSigs.setStatus("mandatory")
_NwNCPExtNumReg_Type = Integer32
_NwNCPExtNumReg_Object = MibScalar
nwNCPExtNumReg = _NwNCPExtNumReg_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7, 11),
    _NwNCPExtNumReg_Type()
)
nwNCPExtNumReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNCPExtNumReg.setStatus("mandatory")
_NwNCPExtInvalidReqs_Type = Counter32
_NwNCPExtInvalidReqs_Object = MibScalar
nwNCPExtInvalidReqs = _NwNCPExtInvalidReqs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 7, 12),
    _NwNCPExtInvalidReqs_Type()
)
nwNCPExtInvalidReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNCPExtInvalidReqs.setStatus("mandatory")
_NwWatchdog_ObjectIdentity = ObjectIdentity
nwWatchdog = _NwWatchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 8)
)
_NwWDTimeBeforeFirstPkt_Type = Integer32
_NwWDTimeBeforeFirstPkt_Object = MibScalar
nwWDTimeBeforeFirstPkt = _NwWDTimeBeforeFirstPkt_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 8, 1),
    _NwWDTimeBeforeFirstPkt_Type()
)
nwWDTimeBeforeFirstPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwWDTimeBeforeFirstPkt.setStatus("mandatory")
_NwWDTimeBetweenPkts_Type = Seconds
_NwWDTimeBetweenPkts_Object = MibScalar
nwWDTimeBetweenPkts = _NwWDTimeBetweenPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 8, 2),
    _NwWDTimeBetweenPkts_Type()
)
nwWDTimeBetweenPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwWDTimeBetweenPkts.setStatus("mandatory")
_NwWDNumPktsToSend_Type = Integer32
_NwWDNumPktsToSend_Object = MibScalar
nwWDNumPktsToSend = _NwWDNumPktsToSend_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 8, 3),
    _NwWDNumPktsToSend_Type()
)
nwWDNumPktsToSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwWDNumPktsToSend.setStatus("mandatory")


class _NwWDCurrentState_Type(Integer32):
    """Custom type nwWDCurrentState based on Integer32"""
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
        *(("clearingStations", 4),
          ("sendingPackets", 3),
          ("unknown", 1),
          ("waiting", 2))
    )


_NwWDCurrentState_Type.__name__ = "Integer32"
_NwWDCurrentState_Object = MibScalar
nwWDCurrentState = _NwWDCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 8, 4),
    _NwWDCurrentState_Type()
)
nwWDCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwWDCurrentState.setStatus("mandatory")


class _NwWDNotifyConsoleFlag_Type(Integer32):
    """Custom type nwWDNotifyConsoleFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotNotify", 1),
          ("notify", 2))
    )


_NwWDNotifyConsoleFlag_Type.__name__ = "Integer32"
_NwWDNotifyConsoleFlag_Object = MibScalar
nwWDNotifyConsoleFlag = _NwWDNotifyConsoleFlag_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 8, 5),
    _NwWDNotifyConsoleFlag_Type()
)
nwWDNotifyConsoleFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwWDNotifyConsoleFlag.setStatus("mandatory")
_NwNLM_ObjectIdentity = ObjectIdentity
nwNLM = _NwNLM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9)
)
_NwNLMTable_Object = MibTable
nwNLMTable = _NwNLMTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9, 1)
)
if mibBuilder.loadTexts:
    nwNLMTable.setStatus("mandatory")
_NwNLMEntry_Object = MibTableRow
nwNLMEntry = _NwNLMEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9, 1, 1)
)
nwNLMEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwNLMIndex"),
)
if mibBuilder.loadTexts:
    nwNLMEntry.setStatus("mandatory")


class _NwNLMIndex_Type(Integer32):
    """Custom type nwNLMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwNLMIndex_Type.__name__ = "Integer32"
_NwNLMIndex_Object = MibTableColumn
nwNLMIndex = _NwNLMIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9, 1, 1, 1),
    _NwNLMIndex_Type()
)
nwNLMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNLMIndex.setStatus("mandatory")


class _NwNLMName_Type(InternationalDisplayString):
    """Custom type nwNLMName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_NwNLMName_Type.__name__ = "InternationalDisplayString"
_NwNLMName_Object = MibTableColumn
nwNLMName = _NwNLMName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9, 1, 1, 2),
    _NwNLMName_Type()
)
nwNLMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNLMName.setStatus("mandatory")


class _NwNLMDescription_Type(InternationalDisplayString):
    """Custom type nwNLMDescription based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NwNLMDescription_Type.__name__ = "InternationalDisplayString"
_NwNLMDescription_Object = MibTableColumn
nwNLMDescription = _NwNLMDescription_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9, 1, 1, 3),
    _NwNLMDescription_Type()
)
nwNLMDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNLMDescription.setStatus("mandatory")
_NwNLMTotalMemory_Type = Integer32
_NwNLMTotalMemory_Object = MibTableColumn
nwNLMTotalMemory = _NwNLMTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9, 1, 1, 4),
    _NwNLMTotalMemory_Type()
)
nwNLMTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNLMTotalMemory.setStatus("mandatory")
_NwNLMCopyright_Type = InternationalDisplayString
_NwNLMCopyright_Object = MibTableColumn
nwNLMCopyright = _NwNLMCopyright_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9, 1, 1, 5),
    _NwNLMCopyright_Type()
)
nwNLMCopyright.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNLMCopyright.setStatus("mandatory")


class _NwNLMProtectionDomain_Type(Integer32):
    """Custom type nwNLMProtectionDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("osDomain", 1),
          ("protectedDomain", 2))
    )


_NwNLMProtectionDomain_Type.__name__ = "Integer32"
_NwNLMProtectionDomain_Object = MibTableColumn
nwNLMProtectionDomain = _NwNLMProtectionDomain_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9, 1, 1, 6),
    _NwNLMProtectionDomain_Type()
)
nwNLMProtectionDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNLMProtectionDomain.setStatus("mandatory")
_NwNLMMajorVer_Type = Integer32
_NwNLMMajorVer_Object = MibTableColumn
nwNLMMajorVer = _NwNLMMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9, 1, 1, 7),
    _NwNLMMajorVer_Type()
)
nwNLMMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNLMMajorVer.setStatus("mandatory")
_NwNLMMinorVer_Type = Integer32
_NwNLMMinorVer_Object = MibTableColumn
nwNLMMinorVer = _NwNLMMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9, 1, 1, 8),
    _NwNLMMinorVer_Type()
)
nwNLMMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNLMMinorVer.setStatus("mandatory")
_NwNLMRevision_Type = Integer32
_NwNLMRevision_Object = MibTableColumn
nwNLMRevision = _NwNLMRevision_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9, 1, 1, 9),
    _NwNLMRevision_Type()
)
nwNLMRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNLMRevision.setStatus("mandatory")
_NwNLMReleaseDate_Type = DateAndTime
_NwNLMReleaseDate_Object = MibTableColumn
nwNLMReleaseDate = _NwNLMReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 9, 1, 1, 10),
    _NwNLMReleaseDate_Type()
)
nwNLMReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNLMReleaseDate.setStatus("mandatory")
_NwSetParams_ObjectIdentity = ObjectIdentity
nwSetParams = _NwSetParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10)
)
_NwSetCategoryTable_Object = MibTable
nwSetCategoryTable = _NwSetCategoryTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 1)
)
if mibBuilder.loadTexts:
    nwSetCategoryTable.setStatus("mandatory")
_NwSetCategoryEntry_Object = MibTableRow
nwSetCategoryEntry = _NwSetCategoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 1, 1)
)
nwSetCategoryEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwSetCategoryIndex"),
)
if mibBuilder.loadTexts:
    nwSetCategoryEntry.setStatus("mandatory")


class _NwSetCategoryIndex_Type(Integer32):
    """Custom type nwSetCategoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwSetCategoryIndex_Type.__name__ = "Integer32"
_NwSetCategoryIndex_Object = MibTableColumn
nwSetCategoryIndex = _NwSetCategoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 1, 1, 1),
    _NwSetCategoryIndex_Type()
)
nwSetCategoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetCategoryIndex.setStatus("mandatory")
_NwSetCategoryName_Type = InternationalDisplayString
_NwSetCategoryName_Object = MibTableColumn
nwSetCategoryName = _NwSetCategoryName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 1, 1, 2),
    _NwSetCategoryName_Type()
)
nwSetCategoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetCategoryName.setStatus("mandatory")
_NwSetParamTable_Object = MibTable
nwSetParamTable = _NwSetParamTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 2)
)
if mibBuilder.loadTexts:
    nwSetParamTable.setStatus("mandatory")
_NwSetParamEntry_Object = MibTableRow
nwSetParamEntry = _NwSetParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 2, 1)
)
nwSetParamEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwSetParamCategoryIndex"),
    (0, "NetWare-Server-MIB", "nwSetParamIndex"),
)
if mibBuilder.loadTexts:
    nwSetParamEntry.setStatus("mandatory")


class _NwSetParamCategoryIndex_Type(Integer32):
    """Custom type nwSetParamCategoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwSetParamCategoryIndex_Type.__name__ = "Integer32"
_NwSetParamCategoryIndex_Object = MibTableColumn
nwSetParamCategoryIndex = _NwSetParamCategoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 2, 1, 1),
    _NwSetParamCategoryIndex_Type()
)
nwSetParamCategoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetParamCategoryIndex.setStatus("mandatory")


class _NwSetParamIndex_Type(Integer32):
    """Custom type nwSetParamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwSetParamIndex_Type.__name__ = "Integer32"
_NwSetParamIndex_Object = MibTableColumn
nwSetParamIndex = _NwSetParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 2, 1, 2),
    _NwSetParamIndex_Type()
)
nwSetParamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetParamIndex.setStatus("mandatory")
_NwSetParamName_Type = InternationalDisplayString
_NwSetParamName_Object = MibTableColumn
nwSetParamName = _NwSetParamName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 2, 1, 3),
    _NwSetParamName_Type()
)
nwSetParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetParamName.setStatus("mandatory")


class _NwSetParamType_Type(Integer32):
    """Custom type nwSetParamType based on Integer32"""
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
        *(("blockShift", 4),
          ("boolean", 2),
          ("number", 1),
          ("string", 6),
          ("ticks", 3),
          ("timeOffset", 5),
          ("trigger", 7))
    )


_NwSetParamType_Type.__name__ = "Integer32"
_NwSetParamType_Object = MibTableColumn
nwSetParamType = _NwSetParamType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 2, 1, 4),
    _NwSetParamType_Type()
)
nwSetParamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetParamType.setStatus("mandatory")
_NwSetParamValueInteger_Type = Integer32
_NwSetParamValueInteger_Object = MibTableColumn
nwSetParamValueInteger = _NwSetParamValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 2, 1, 5),
    _NwSetParamValueInteger_Type()
)
nwSetParamValueInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwSetParamValueInteger.setStatus("mandatory")
_NwSetParamValueString_Type = InternationalDisplayString
_NwSetParamValueString_Object = MibTableColumn
nwSetParamValueString = _NwSetParamValueString_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 2, 1, 6),
    _NwSetParamValueString_Type()
)
nwSetParamValueString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwSetParamValueString.setStatus("mandatory")
_NwSetParamLowerLimit_Type = Integer32
_NwSetParamLowerLimit_Object = MibTableColumn
nwSetParamLowerLimit = _NwSetParamLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 2, 1, 7),
    _NwSetParamLowerLimit_Type()
)
nwSetParamLowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetParamLowerLimit.setStatus("mandatory")
_NwSetParamUpperLimit_Type = Integer32
_NwSetParamUpperLimit_Object = MibTableColumn
nwSetParamUpperLimit = _NwSetParamUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 2, 1, 8),
    _NwSetParamUpperLimit_Type()
)
nwSetParamUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetParamUpperLimit.setStatus("mandatory")
_NwSetParamDescrLength_Type = Integer32
_NwSetParamDescrLength_Object = MibTableColumn
nwSetParamDescrLength = _NwSetParamDescrLength_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 2, 1, 9),
    _NwSetParamDescrLength_Type()
)
nwSetParamDescrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetParamDescrLength.setStatus("mandatory")


class _NwSetParamMode_Type(Integer32):
    """Custom type nwSetParamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NwSetParamMode_Type.__name__ = "Integer32"
_NwSetParamMode_Object = MibTableColumn
nwSetParamMode = _NwSetParamMode_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 2, 1, 10),
    _NwSetParamMode_Type()
)
nwSetParamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwSetParamMode.setStatus("mandatory")
_NwSetDescrTable_Object = MibTable
nwSetDescrTable = _NwSetDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 3)
)
if mibBuilder.loadTexts:
    nwSetDescrTable.setStatus("mandatory")
_NwSetDescrEntry_Object = MibTableRow
nwSetDescrEntry = _NwSetDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 3, 1)
)
nwSetDescrEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwSetDescrCategoryIndex"),
    (0, "NetWare-Server-MIB", "nwSetDescrParamIndex"),
    (0, "NetWare-Server-MIB", "nwSetDescrIndex"),
)
if mibBuilder.loadTexts:
    nwSetDescrEntry.setStatus("mandatory")


class _NwSetDescrCategoryIndex_Type(Integer32):
    """Custom type nwSetDescrCategoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwSetDescrCategoryIndex_Type.__name__ = "Integer32"
_NwSetDescrCategoryIndex_Object = MibTableColumn
nwSetDescrCategoryIndex = _NwSetDescrCategoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 3, 1, 1),
    _NwSetDescrCategoryIndex_Type()
)
nwSetDescrCategoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetDescrCategoryIndex.setStatus("mandatory")


class _NwSetDescrParamIndex_Type(Integer32):
    """Custom type nwSetDescrParamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwSetDescrParamIndex_Type.__name__ = "Integer32"
_NwSetDescrParamIndex_Object = MibTableColumn
nwSetDescrParamIndex = _NwSetDescrParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 3, 1, 2),
    _NwSetDescrParamIndex_Type()
)
nwSetDescrParamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetDescrParamIndex.setStatus("mandatory")


class _NwSetDescrIndex_Type(Integer32):
    """Custom type nwSetDescrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NwSetDescrIndex_Type.__name__ = "Integer32"
_NwSetDescrIndex_Object = MibTableColumn
nwSetDescrIndex = _NwSetDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 3, 1, 3),
    _NwSetDescrIndex_Type()
)
nwSetDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetDescrIndex.setStatus("mandatory")
_NwSetDescription_Type = InternationalDisplayString
_NwSetDescription_Object = MibTableColumn
nwSetDescription = _NwSetDescription_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 10, 3, 1, 4),
    _NwSetDescription_Type()
)
nwSetDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSetDescription.setStatus("mandatory")
_NwUserAccounts_ObjectIdentity = ObjectIdentity
nwUserAccounts = _NwUserAccounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11)
)
_NwUserAcctTable_Object = MibTable
nwUserAcctTable = _NwUserAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 1)
)
if mibBuilder.loadTexts:
    nwUserAcctTable.setStatus("mandatory")
_NwUserAcctEntry_Object = MibTableRow
nwUserAcctEntry = _NwUserAcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 1, 1)
)
nwUserAcctEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwUserID"),
)
if mibBuilder.loadTexts:
    nwUserAcctEntry.setStatus("mandatory")


class _NwUserID_Type(Integer32):
    """Custom type nwUserID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwUserID_Type.__name__ = "Integer32"
_NwUserID_Object = MibTableColumn
nwUserID = _NwUserID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 1, 1, 1),
    _NwUserID_Type()
)
nwUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserID.setStatus("mandatory")
_NwUserName_Type = InternationalDisplayString
_NwUserName_Object = MibTableColumn
nwUserName = _NwUserName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 1, 1, 2),
    _NwUserName_Type()
)
nwUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserName.setStatus("mandatory")
_NwUserDiskUsage_Type = KBytes
_NwUserDiskUsage_Object = MibTableColumn
nwUserDiskUsage = _NwUserDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 1, 1, 3),
    _NwUserDiskUsage_Type()
)
nwUserDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserDiskUsage.setStatus("mandatory")
_NwUserLastLoginTime_Type = DateAndTime
_NwUserLastLoginTime_Object = MibTableColumn
nwUserLastLoginTime = _NwUserLastLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 1, 1, 4),
    _NwUserLastLoginTime_Type()
)
nwUserLastLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserLastLoginTime.setStatus("mandatory")


class _NwUserAccountStatus_Type(Integer32):
    """Custom type nwUserAccountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("expired", 2),
          ("valid", 1))
    )


_NwUserAccountStatus_Type.__name__ = "Integer32"
_NwUserAccountStatus_Object = MibTableColumn
nwUserAccountStatus = _NwUserAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 1, 1, 5),
    _NwUserAccountStatus_Type()
)
nwUserAccountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserAccountStatus.setStatus("mandatory")


class _NwUserPasswordStatus_Type(Integer32):
    """Custom type nwUserPasswordStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("expired", 2),
          ("valid", 1))
    )


_NwUserPasswordStatus_Type.__name__ = "Integer32"
_NwUserPasswordStatus_Object = MibTableColumn
nwUserPasswordStatus = _NwUserPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 1, 1, 6),
    _NwUserPasswordStatus_Type()
)
nwUserPasswordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserPasswordStatus.setStatus("mandatory")
_NwUserBadLoginTransport_Type = TransportDomain
_NwUserBadLoginTransport_Object = MibTableColumn
nwUserBadLoginTransport = _NwUserBadLoginTransport_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 1, 1, 7),
    _NwUserBadLoginTransport_Type()
)
nwUserBadLoginTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserBadLoginTransport.setStatus("mandatory")
_NwUserBadLoginAddress_Type = TransportAddress
_NwUserBadLoginAddress_Object = MibTableColumn
nwUserBadLoginAddress = _NwUserBadLoginAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 1, 1, 8),
    _NwUserBadLoginAddress_Type()
)
nwUserBadLoginAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserBadLoginAddress.setStatus("mandatory")
_NwUserBadLoginAttempts_Type = Integer32
_NwUserBadLoginAttempts_Object = MibTableColumn
nwUserBadLoginAttempts = _NwUserBadLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 1, 1, 9),
    _NwUserBadLoginAttempts_Type()
)
nwUserBadLoginAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserBadLoginAttempts.setStatus("mandatory")
_NwUserFullName_Type = InternationalDisplayString
_NwUserFullName_Object = MibTableColumn
nwUserFullName = _NwUserFullName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 1, 1, 10),
    _NwUserFullName_Type()
)
nwUserFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserFullName.setStatus("mandatory")
_NwUserVolUsageTable_Object = MibTable
nwUserVolUsageTable = _NwUserVolUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 2)
)
if mibBuilder.loadTexts:
    nwUserVolUsageTable.setStatus("mandatory")
_NwUserVolUsageEntry_Object = MibTableRow
nwUserVolUsageEntry = _NwUserVolUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 2, 1)
)
nwUserVolUsageEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwUserVolUserID"),
    (0, "NetWare-Server-MIB", "nwUserVolVolID"),
)
if mibBuilder.loadTexts:
    nwUserVolUsageEntry.setStatus("mandatory")


class _NwUserVolUserID_Type(Integer32):
    """Custom type nwUserVolUserID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwUserVolUserID_Type.__name__ = "Integer32"
_NwUserVolUserID_Object = MibTableColumn
nwUserVolUserID = _NwUserVolUserID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 2, 1, 1),
    _NwUserVolUserID_Type()
)
nwUserVolUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserVolUserID.setStatus("mandatory")


class _NwUserVolVolID_Type(Integer32):
    """Custom type nwUserVolVolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwUserVolVolID_Type.__name__ = "Integer32"
_NwUserVolVolID_Object = MibTableColumn
nwUserVolVolID = _NwUserVolVolID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 2, 1, 2),
    _NwUserVolVolID_Type()
)
nwUserVolVolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserVolVolID.setStatus("mandatory")
_NwUserVolUsageUser_Type = InternationalDisplayString
_NwUserVolUsageUser_Object = MibTableColumn
nwUserVolUsageUser = _NwUserVolUsageUser_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 2, 1, 3),
    _NwUserVolUsageUser_Type()
)
nwUserVolUsageUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserVolUsageUser.setStatus("mandatory")


class _NwUserVolUsageVolume_Type(InternationalDisplayString):
    """Custom type nwUserVolUsageVolume based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NwUserVolUsageVolume_Type.__name__ = "InternationalDisplayString"
_NwUserVolUsageVolume_Object = MibTableColumn
nwUserVolUsageVolume = _NwUserVolUsageVolume_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 2, 1, 4),
    _NwUserVolUsageVolume_Type()
)
nwUserVolUsageVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserVolUsageVolume.setStatus("mandatory")
_NwUserVolUsageSpaceUsed_Type = KBytes
_NwUserVolUsageSpaceUsed_Object = MibTableColumn
nwUserVolUsageSpaceUsed = _NwUserVolUsageSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 2, 1, 5),
    _NwUserVolUsageSpaceUsed_Type()
)
nwUserVolUsageSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserVolUsageSpaceUsed.setStatus("mandatory")
_NwUserVolUsageLimit_Type = KBytes
_NwUserVolUsageLimit_Object = MibTableColumn
nwUserVolUsageLimit = _NwUserVolUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 2, 1, 6),
    _NwUserVolUsageLimit_Type()
)
nwUserVolUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwUserVolUsageLimit.setStatus("mandatory")
_NwVolUsageTable_Object = MibTable
nwVolUsageTable = _NwVolUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 3)
)
if mibBuilder.loadTexts:
    nwVolUsageTable.setStatus("mandatory")
_NwVolUsageEntry_Object = MibTableRow
nwVolUsageEntry = _NwVolUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 3, 1)
)
nwVolUsageEntry.setIndexNames(
    (0, "NetWare-Server-MIB", "nwVolUsageVolID"),
    (0, "NetWare-Server-MIB", "nwVolUsageUserID"),
)
if mibBuilder.loadTexts:
    nwVolUsageEntry.setStatus("mandatory")


class _NwVolUsageVolID_Type(Integer32):
    """Custom type nwVolUsageVolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwVolUsageVolID_Type.__name__ = "Integer32"
_NwVolUsageVolID_Object = MibTableColumn
nwVolUsageVolID = _NwVolUsageVolID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 3, 1, 1),
    _NwVolUsageVolID_Type()
)
nwVolUsageVolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolUsageVolID.setStatus("mandatory")


class _NwVolUsageUserID_Type(Integer32):
    """Custom type nwVolUsageUserID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwVolUsageUserID_Type.__name__ = "Integer32"
_NwVolUsageUserID_Object = MibTableColumn
nwVolUsageUserID = _NwVolUsageUserID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 3, 1, 2),
    _NwVolUsageUserID_Type()
)
nwVolUsageUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolUsageUserID.setStatus("mandatory")


class _NwVolUsageVolume_Type(InternationalDisplayString):
    """Custom type nwVolUsageVolume based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NwVolUsageVolume_Type.__name__ = "InternationalDisplayString"
_NwVolUsageVolume_Object = MibTableColumn
nwVolUsageVolume = _NwVolUsageVolume_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 3, 1, 3),
    _NwVolUsageVolume_Type()
)
nwVolUsageVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolUsageVolume.setStatus("mandatory")
_NwVolUsageUser_Type = InternationalDisplayString
_NwVolUsageUser_Object = MibTableColumn
nwVolUsageUser = _NwVolUsageUser_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 3, 1, 4),
    _NwVolUsageUser_Type()
)
nwVolUsageUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolUsageUser.setStatus("mandatory")
_NwVolUsageSpaceUsed_Type = KBytes
_NwVolUsageSpaceUsed_Object = MibTableColumn
nwVolUsageSpaceUsed = _NwVolUsageSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 3, 1, 5),
    _NwVolUsageSpaceUsed_Type()
)
nwVolUsageSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolUsageSpaceUsed.setStatus("mandatory")
_NwVolUsageLimit_Type = KBytes
_NwVolUsageLimit_Object = MibTableColumn
nwVolUsageLimit = _NwVolUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 28, 11, 3, 1, 6),
    _NwVolUsageLimit_Type()
)
nwVolUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwVolUsageLimit.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NetWare-Server-MIB",
    **{"Seconds": Seconds,
       "IPXNetNumber": IPXNetNumber,
       "TransportDomain": TransportDomain,
       "TransportAddress": TransportAddress,
       "EngineType": EngineType,
       "DSTType": DSTType,
       "novell": novell,
       "mibDoc": mibDoc,
       "nwServer": nwServer,
       "nwSystem": nwSystem,
       "nwSysServerName": nwSysServerName,
       "nwSysSerialNumber": nwSysSerialNumber,
       "nwSysInternalNetNum": nwSysInternalNetNum,
       "nwSysServerUpTime": nwSysServerUpTime,
       "nwSysOSSFTLevel": nwSysOSSFTLevel,
       "nwSysOSMajorVer": nwSysOSMajorVer,
       "nwSysOSMinorVer": nwSysOSMinorVer,
       "nwSysOSReleaseDate": nwSysOSReleaseDate,
       "nwSysOSDescription": nwSysOSDescription,
       "nwSysOSCopyright": nwSysOSCopyright,
       "nwSysTime": nwSysTime,
       "nwSysTimeZone": nwSysTimeZone,
       "nwSysLoginState": nwSysLoginState,
       "nwSysLanguageID": nwSysLanguageID,
       "nwSysNMASerialNumber": nwSysNMASerialNumber,
       "nwSysNMACopiesAllowed": nwSysNMACopiesAllowed,
       "nwSysDirectoryTree": nwSysDirectoryTree,
       "nwSysBinderyContext": nwSysBinderyContext,
       "nwSysServerDSName": nwSysServerDSName,
       "nwSysDaylightSavingsStart": nwSysDaylightSavingsStart,
       "nwSysDaylightSavingsEnd": nwSysDaylightSavingsEnd,
       "nwSysDaylightSavingsOffset": nwSysDaylightSavingsOffset,
       "nwSysDaylightSavingsStatus": nwSysDaylightSavingsStatus,
       "nwFileSystem": nwFileSystem,
       "nwFSReads": nwFSReads,
       "nwFSWrites": nwFSWrites,
       "nwFSReadKBytes": nwFSReadKBytes,
       "nwFSWrittenKBytes": nwFSWrittenKBytes,
       "nwFSCacheChecks": nwFSCacheChecks,
       "nwFSCacheHits": nwFSCacheHits,
       "nwFSOpenFiles": nwFSOpenFiles,
       "nwFSMaxOpenFiles": nwFSMaxOpenFiles,
       "nwFSRecordLocks": nwFSRecordLocks,
       "nwFSMaxRecordLocks": nwFSMaxRecordLocks,
       "nwFSMaxSubdirectoryTreeDepth": nwFSMaxSubdirectoryTreeDepth,
       "nwFSMaxPercentOfVolumeUsedByDir": nwFSMaxPercentOfVolumeUsedByDir,
       "nwFSVolCount": nwFSVolCount,
       "nwFSVolTable": nwFSVolTable,
       "nwFSVolEntry": nwFSVolEntry,
       "nwVolID": nwVolID,
       "nwVolPhysicalName": nwVolPhysicalName,
       "nwVolSize": nwVolSize,
       "nwVolFree": nwVolFree,
       "nwVolFreeable": nwVolFreeable,
       "nwVolNonFreeable": nwVolNonFreeable,
       "nwVolBlockSize": nwVolBlockSize,
       "nwVolMounted": nwVolMounted,
       "nwVolAttributes": nwVolAttributes,
       "nwVolNameSpaces": nwVolNameSpaces,
       "nwVolTotalDirEntries": nwVolTotalDirEntries,
       "nwVolUsedDirEntries": nwVolUsedDirEntries,
       "nwVolSegmentCount": nwVolSegmentCount,
       "nwVolDSName": nwVolDSName,
       "nwVolFileSystemID": nwVolFileSystemID,
       "nwVolFileSystemName": nwVolFileSystemName,
       "nwFSOpenFileTable": nwFSOpenFileTable,
       "nwFSOpenFileEntry": nwFSOpenFileEntry,
       "nwOfileVolID": nwOfileVolID,
       "nwOfileDirectoryNumber": nwOfileDirectoryNumber,
       "nwOfileConnection": nwOfileConnection,
       "nwOfileVolumeName": nwOfileVolumeName,
       "nwOfileName": nwOfileName,
       "nwOfileLoginName": nwOfileLoginName,
       "nwUsers": nwUsers,
       "nwUserCount": nwUserCount,
       "nwLoginCount": nwLoginCount,
       "nwMaxLogins": nwMaxLogins,
       "nwConnectionCount": nwConnectionCount,
       "nwPeakRemoteConnections": nwPeakRemoteConnections,
       "nwMaxConnections": nwMaxConnections,
       "nwNLMConnections": nwNLMConnections,
       "nwConnectionTable": nwConnectionTable,
       "nwConnectionEntry": nwConnectionEntry,
       "nwConnectionNumber": nwConnectionNumber,
       "nwConnectionLoginName": nwConnectionLoginName,
       "nwConnectionTransportDomain": nwConnectionTransportDomain,
       "nwConnectionTransportAddress": nwConnectionTransportAddress,
       "nwConnectionTime": nwConnectionTime,
       "nwConnectionReadKBytes": nwConnectionReadKBytes,
       "nwConnectionWrittenKBytes": nwConnectionWrittenKBytes,
       "nwConnectionNcpRequests": nwConnectionNcpRequests,
       "nwConnectionFilesOpen": nwConnectionFilesOpen,
       "nwConnectionRecordsLocked": nwConnectionRecordsLocked,
       "nwConnectionPrivilege": nwConnectionPrivilege,
       "nwConnectionStatus": nwConnectionStatus,
       "nwQueue": nwQueue,
       "nwQueueCount": nwQueueCount,
       "nwQueueTable": nwQueueTable,
       "nwQueueEntry": nwQueueEntry,
       "nwQID": nwQID,
       "nwQName": nwQName,
       "nwQType": nwQType,
       "nwQAddJobState": nwQAddJobState,
       "nwQAttachState": nwQAttachState,
       "nwQServiceJobState": nwQServiceJobState,
       "nwQDirVolName": nwQDirVolName,
       "nwQNumJobEntries": nwQNumJobEntries,
       "nwQNumAssignedServers": nwQNumAssignedServers,
       "nwQueueJobTable": nwQueueJobTable,
       "nwQueueJobEntry": nwQueueJobEntry,
       "nwQJobQID": nwQJobQID,
       "nwQJobNumber": nwQJobNumber,
       "nwQJobDescription": nwQJobDescription,
       "nwQJobEntryDateTime": nwQJobEntryDateTime,
       "nwQJobPosition": nwQJobPosition,
       "nwQJobSize": nwQJobSize,
       "nwQJobControlFlags": nwQJobControlFlags,
       "nwQJobUserName": nwQJobUserName,
       "nwQJobTargetServerName": nwQJobTargetServerName,
       "nwQJobTargetDateTime": nwQJobTargetDateTime,
       "nwQJobServerName": nwQJobServerName,
       "nwQueueServerTable": nwQueueServerTable,
       "nwQueueServerEntry": nwQueueServerEntry,
       "nwQServerQID": nwQServerQID,
       "nwQServerID": nwQServerID,
       "nwQServerName": nwQServerName,
       "nwQServerStatus": nwQServerStatus,
       "nwOdi": nwOdi,
       "nwOdiLslEnqSendCount": nwOdiLslEnqSendCount,
       "nwOdiOsPktRcvBuffer": nwOdiOsPktRcvBuffer,
       "nwOdiOsMaxPktRcvBuffers": nwOdiOsMaxPktRcvBuffers,
       "nwOdiOsMinPktRcvBuffers": nwOdiOsMinPktRcvBuffers,
       "nwSft3": nwSft3,
       "nwSft3Engine": nwSft3Engine,
       "nwSft3EngineState": nwSft3EngineState,
       "nwSft3EngineTable": nwSft3EngineTable,
       "nwSft3EngineEntry": nwSft3EngineEntry,
       "nwSft3EngineType": nwSft3EngineType,
       "nwSft3EngineName": nwSft3EngineName,
       "nwSft3EngineInternalNetNum": nwSft3EngineInternalNetNum,
       "nwNCP": nwNCP,
       "nwNCPIPXChecksums": nwNCPIPXChecksums,
       "nwNCPPacketSignatures": nwNCPPacketSignatures,
       "nwNCPNumNCPReqs": nwNCPNumNCPReqs,
       "nwNCPUseCount": nwNCPUseCount,
       "nwNCPPeakUseCount": nwNCPPeakUseCount,
       "nwNCPForgedPkts": nwNCPForgedPkts,
       "nwNCPBeingProcesseds": nwNCPBeingProcesseds,
       "nwNCPNoAvailConns": nwNCPNoAvailConns,
       "nwNCPIPXChecksumErrs": nwNCPIPXChecksumErrs,
       "nwNCPInvalidPacketSigs": nwNCPInvalidPacketSigs,
       "nwNCPExtNumReg": nwNCPExtNumReg,
       "nwNCPExtInvalidReqs": nwNCPExtInvalidReqs,
       "nwWatchdog": nwWatchdog,
       "nwWDTimeBeforeFirstPkt": nwWDTimeBeforeFirstPkt,
       "nwWDTimeBetweenPkts": nwWDTimeBetweenPkts,
       "nwWDNumPktsToSend": nwWDNumPktsToSend,
       "nwWDCurrentState": nwWDCurrentState,
       "nwWDNotifyConsoleFlag": nwWDNotifyConsoleFlag,
       "nwNLM": nwNLM,
       "nwNLMTable": nwNLMTable,
       "nwNLMEntry": nwNLMEntry,
       "nwNLMIndex": nwNLMIndex,
       "nwNLMName": nwNLMName,
       "nwNLMDescription": nwNLMDescription,
       "nwNLMTotalMemory": nwNLMTotalMemory,
       "nwNLMCopyright": nwNLMCopyright,
       "nwNLMProtectionDomain": nwNLMProtectionDomain,
       "nwNLMMajorVer": nwNLMMajorVer,
       "nwNLMMinorVer": nwNLMMinorVer,
       "nwNLMRevision": nwNLMRevision,
       "nwNLMReleaseDate": nwNLMReleaseDate,
       "nwSetParams": nwSetParams,
       "nwSetCategoryTable": nwSetCategoryTable,
       "nwSetCategoryEntry": nwSetCategoryEntry,
       "nwSetCategoryIndex": nwSetCategoryIndex,
       "nwSetCategoryName": nwSetCategoryName,
       "nwSetParamTable": nwSetParamTable,
       "nwSetParamEntry": nwSetParamEntry,
       "nwSetParamCategoryIndex": nwSetParamCategoryIndex,
       "nwSetParamIndex": nwSetParamIndex,
       "nwSetParamName": nwSetParamName,
       "nwSetParamType": nwSetParamType,
       "nwSetParamValueInteger": nwSetParamValueInteger,
       "nwSetParamValueString": nwSetParamValueString,
       "nwSetParamLowerLimit": nwSetParamLowerLimit,
       "nwSetParamUpperLimit": nwSetParamUpperLimit,
       "nwSetParamDescrLength": nwSetParamDescrLength,
       "nwSetParamMode": nwSetParamMode,
       "nwSetDescrTable": nwSetDescrTable,
       "nwSetDescrEntry": nwSetDescrEntry,
       "nwSetDescrCategoryIndex": nwSetDescrCategoryIndex,
       "nwSetDescrParamIndex": nwSetDescrParamIndex,
       "nwSetDescrIndex": nwSetDescrIndex,
       "nwSetDescription": nwSetDescription,
       "nwUserAccounts": nwUserAccounts,
       "nwUserAcctTable": nwUserAcctTable,
       "nwUserAcctEntry": nwUserAcctEntry,
       "nwUserID": nwUserID,
       "nwUserName": nwUserName,
       "nwUserDiskUsage": nwUserDiskUsage,
       "nwUserLastLoginTime": nwUserLastLoginTime,
       "nwUserAccountStatus": nwUserAccountStatus,
       "nwUserPasswordStatus": nwUserPasswordStatus,
       "nwUserBadLoginTransport": nwUserBadLoginTransport,
       "nwUserBadLoginAddress": nwUserBadLoginAddress,
       "nwUserBadLoginAttempts": nwUserBadLoginAttempts,
       "nwUserFullName": nwUserFullName,
       "nwUserVolUsageTable": nwUserVolUsageTable,
       "nwUserVolUsageEntry": nwUserVolUsageEntry,
       "nwUserVolUserID": nwUserVolUserID,
       "nwUserVolVolID": nwUserVolVolID,
       "nwUserVolUsageUser": nwUserVolUsageUser,
       "nwUserVolUsageVolume": nwUserVolUsageVolume,
       "nwUserVolUsageSpaceUsed": nwUserVolUsageSpaceUsed,
       "nwUserVolUsageLimit": nwUserVolUsageLimit,
       "nwVolUsageTable": nwVolUsageTable,
       "nwVolUsageEntry": nwVolUsageEntry,
       "nwVolUsageVolID": nwVolUsageVolID,
       "nwVolUsageUserID": nwVolUsageUserID,
       "nwVolUsageVolume": nwVolUsageVolume,
       "nwVolUsageUser": nwVolUsageUser,
       "nwVolUsageSpaceUsed": nwVolUsageSpaceUsed,
       "nwVolUsageLimit": nwVolUsageLimit}
)
