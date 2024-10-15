# SNMP MIB module (PUBLISHEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PUBLISHEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:00 2024
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

(publishExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "publishExt")

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

apPublishExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApPubTable_Object = MibTable
apPubTable = _ApPubTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2)
)
if mibBuilder.loadTexts:
    apPubTable.setStatus("current")
_ApPubEntry_Object = MibTableRow
apPubEntry = _ApPubEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1)
)
apPubEntry.setIndexNames(
    (0, "PUBLISHEXT-MIB", "apPubName"),
)
if mibBuilder.loadTexts:
    apPubEntry.setStatus("current")
_ApPubName_Type = DisplayString
_ApPubName_Object = MibTableColumn
apPubName = _ApPubName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 1),
    _ApPubName_Type()
)
apPubName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubName.setStatus("current")


class _ApPubState_Type(Integer32):
    """Custom type apPubState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("accessFail", 3),
          ("busyPublisher", 5),
          ("busyScan", 6),
          ("down", 11),
          ("initializing", 7),
          ("invalid", 12),
          ("needsConfig", 2),
          ("online", 9),
          ("publisherRegister", 0),
          ("ready", 4),
          ("subscriberRegister", 1),
          ("suspended", 10),
          ("waitsConfig", 8))
    )


_ApPubState_Type.__name__ = "Integer32"
_ApPubState_Object = MibTableColumn
apPubState = _ApPubState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 2),
    _ApPubState_Type()
)
apPubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubState.setStatus("current")
_ApPubAccessError_Type = DisplayString
_ApPubAccessError_Object = MibTableColumn
apPubAccessError = _ApPubAccessError_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 3),
    _ApPubAccessError_Type()
)
apPubAccessError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubAccessError.setStatus("current")
_ApPubAccessIP_Type = IpAddress
_ApPubAccessIP_Object = MibTableColumn
apPubAccessIP = _ApPubAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 4),
    _ApPubAccessIP_Type()
)
apPubAccessIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubAccessIP.setStatus("current")
_ApPubAccessUserName_Type = DisplayString
_ApPubAccessUserName_Object = MibTableColumn
apPubAccessUserName = _ApPubAccessUserName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 5),
    _ApPubAccessUserName_Type()
)
apPubAccessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubAccessUserName.setStatus("current")
_ApPubPublishedFiles_Type = Integer32
_ApPubPublishedFiles_Object = MibTableColumn
apPubPublishedFiles = _ApPubPublishedFiles_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 6),
    _ApPubPublishedFiles_Type()
)
apPubPublishedFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubPublishedFiles.setStatus("current")
_ApPubSubscribers_Type = Integer32
_ApPubSubscribers_Object = MibTableColumn
apPubSubscribers = _ApPubSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 7),
    _ApPubSubscribers_Type()
)
apPubSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubSubscribers.setStatus("current")
_ApPubPublishInterval_Type = Integer32
_ApPubPublishInterval_Object = MibTableColumn
apPubPublishInterval = _ApPubPublishInterval_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 8),
    _ApPubPublishInterval_Type()
)
apPubPublishInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubPublishInterval.setStatus("current")
_ApPubManagedFiles_Type = Integer32
_ApPubManagedFiles_Object = MibTableColumn
apPubManagedFiles = _ApPubManagedFiles_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 9),
    _ApPubManagedFiles_Type()
)
apPubManagedFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubManagedFiles.setStatus("current")
_ApPubManagedDirs_Type = Integer32
_ApPubManagedDirs_Object = MibTableColumn
apPubManagedDirs = _ApPubManagedDirs_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 10),
    _ApPubManagedDirs_Type()
)
apPubManagedDirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubManagedDirs.setStatus("current")
_ApPubLastMethod_Type = DisplayString
_ApPubLastMethod_Object = MibTableColumn
apPubLastMethod = _ApPubLastMethod_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 11),
    _ApPubLastMethod_Type()
)
apPubLastMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubLastMethod.setStatus("current")


class _ApPubAccessType_Type(Integer32):
    """Custom type apPubAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 0),
          ("http", 1))
    )


_ApPubAccessType_Type.__name__ = "Integer32"
_ApPubAccessType_Object = MibTableColumn
apPubAccessType = _ApPubAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 12),
    _ApPubAccessType_Type()
)
apPubAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubAccessType.setStatus("current")
_ApPubAccessPort_Type = Integer32
_ApPubAccessPort_Object = MibTableColumn
apPubAccessPort = _ApPubAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 13),
    _ApPubAccessPort_Type()
)
apPubAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubAccessPort.setStatus("current")
_ApPubAccessBaseDir_Type = DisplayString
_ApPubAccessBaseDir_Object = MibTableColumn
apPubAccessBaseDir = _ApPubAccessBaseDir_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 14),
    _ApPubAccessBaseDir_Type()
)
apPubAccessBaseDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubAccessBaseDir.setStatus("current")
_ApPubPublishedBytes_Type = Integer32
_ApPubPublishedBytes_Object = MibTableColumn
apPubPublishedBytes = _ApPubPublishedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 15),
    _ApPubPublishedBytes_Type()
)
apPubPublishedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubPublishedBytes.setStatus("current")
_ApPubTriggerFile_Type = DisplayString
_ApPubTriggerFile_Object = MibTableColumn
apPubTriggerFile = _ApPubTriggerFile_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 16),
    _ApPubTriggerFile_Type()
)
apPubTriggerFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubTriggerFile.setStatus("current")
_ApPubNextInterval_Type = DisplayString
_ApPubNextInterval_Object = MibTableColumn
apPubNextInterval = _ApPubNextInterval_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 17),
    _ApPubNextInterval_Type()
)
apPubNextInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubNextInterval.setStatus("current")
_ApPubSubscrbrsSyncd_Type = Integer32
_ApPubSubscrbrsSyncd_Object = MibTableColumn
apPubSubscrbrsSyncd = _ApPubSubscrbrsSyncd_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 18),
    _ApPubSubscrbrsSyncd_Type()
)
apPubSubscrbrsSyncd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubSubscrbrsSyncd.setStatus("current")
_ApPubManagedBytes_Type = Integer32
_ApPubManagedBytes_Object = MibTableColumn
apPubManagedBytes = _ApPubManagedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 19),
    _ApPubManagedBytes_Type()
)
apPubManagedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubManagedBytes.setStatus("current")
_ApPubLastTime_Type = DisplayString
_ApPubLastTime_Object = MibTableColumn
apPubLastTime = _ApPubLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 57, 2, 1, 20),
    _ApPubLastTime_Type()
)
apPubLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPubLastTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PUBLISHEXT-MIB",
    **{"apPublishExtMib": apPublishExtMib,
       "apPubTable": apPubTable,
       "apPubEntry": apPubEntry,
       "apPubName": apPubName,
       "apPubState": apPubState,
       "apPubAccessError": apPubAccessError,
       "apPubAccessIP": apPubAccessIP,
       "apPubAccessUserName": apPubAccessUserName,
       "apPubPublishedFiles": apPubPublishedFiles,
       "apPubSubscribers": apPubSubscribers,
       "apPubPublishInterval": apPubPublishInterval,
       "apPubManagedFiles": apPubManagedFiles,
       "apPubManagedDirs": apPubManagedDirs,
       "apPubLastMethod": apPubLastMethod,
       "apPubAccessType": apPubAccessType,
       "apPubAccessPort": apPubAccessPort,
       "apPubAccessBaseDir": apPubAccessBaseDir,
       "apPubPublishedBytes": apPubPublishedBytes,
       "apPubTriggerFile": apPubTriggerFile,
       "apPubNextInterval": apPubNextInterval,
       "apPubSubscrbrsSyncd": apPubSubscrbrsSyncd,
       "apPubManagedBytes": apPubManagedBytes,
       "apPubLastTime": apPubLastTime}
)
