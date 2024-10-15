# SNMP MIB module (NEOTERIS-IVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NEOTERIS-IVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:20 2024
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

neoteris = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12532)
)
neoteris.setRevisions(
        ("2002-03-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LogFullPercent_Type = Integer32
_LogFullPercent_Object = MibScalar
logFullPercent = _LogFullPercent_Object(
    (1, 3, 6, 1, 4, 1, 12532, 1),
    _LogFullPercent_Type()
)
logFullPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFullPercent.setStatus("current")
_SignedInWebUsers_Type = Integer32
_SignedInWebUsers_Object = MibScalar
signedInWebUsers = _SignedInWebUsers_Object(
    (1, 3, 6, 1, 4, 1, 12532, 2),
    _SignedInWebUsers_Type()
)
signedInWebUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signedInWebUsers.setStatus("current")
_SignedInMailUsers_Type = Integer32
_SignedInMailUsers_Object = MibScalar
signedInMailUsers = _SignedInMailUsers_Object(
    (1, 3, 6, 1, 4, 1, 12532, 3),
    _SignedInMailUsers_Type()
)
signedInMailUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signedInMailUsers.setStatus("current")
_BlockedIP_Type = IpAddress
_BlockedIP_Object = MibScalar
blockedIP = _BlockedIP_Object(
    (1, 3, 6, 1, 4, 1, 12532, 4),
    _BlockedIP_Type()
)
blockedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockedIP.setStatus("current")
_AuthServerName_Type = OctetString
_AuthServerName_Object = MibScalar
authServerName = _AuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 12532, 5),
    _AuthServerName_Type()
)
authServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authServerName.setStatus("current")
_ProductName_Type = OctetString
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 12532, 6),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")
_ProductVersion_Type = OctetString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 12532, 7),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")
_FileName_Type = OctetString
_FileName_Object = MibScalar
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 12532, 8),
    _FileName_Type()
)
fileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileName.setStatus("current")
_MeetingUserCount_Type = Integer32
_MeetingUserCount_Object = MibScalar
meetingUserCount = _MeetingUserCount_Object(
    (1, 3, 6, 1, 4, 1, 12532, 9),
    _MeetingUserCount_Type()
)
meetingUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meetingUserCount.setStatus("current")
_IveCpuUtil_Type = Integer32
_IveCpuUtil_Object = MibScalar
iveCpuUtil = _IveCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 12532, 10),
    _IveCpuUtil_Type()
)
iveCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveCpuUtil.setStatus("current")
_IveMemoryUtil_Type = Integer32
_IveMemoryUtil_Object = MibScalar
iveMemoryUtil = _IveMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 12532, 11),
    _IveMemoryUtil_Type()
)
iveMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveMemoryUtil.setStatus("current")
_IveConcurrentUsers_Type = Counter32
_IveConcurrentUsers_Object = MibScalar
iveConcurrentUsers = _IveConcurrentUsers_Object(
    (1, 3, 6, 1, 4, 1, 12532, 12),
    _IveConcurrentUsers_Type()
)
iveConcurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveConcurrentUsers.setStatus("current")
_ClusterConcurrentUsers_Type = Counter32
_ClusterConcurrentUsers_Object = MibScalar
clusterConcurrentUsers = _ClusterConcurrentUsers_Object(
    (1, 3, 6, 1, 4, 1, 12532, 13),
    _ClusterConcurrentUsers_Type()
)
clusterConcurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterConcurrentUsers.setStatus("current")
_IveTotalHits_Type = Counter64
_IveTotalHits_Object = MibScalar
iveTotalHits = _IveTotalHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 14),
    _IveTotalHits_Type()
)
iveTotalHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveTotalHits.setStatus("current")
_IveFileHits_Type = Counter64
_IveFileHits_Object = MibScalar
iveFileHits = _IveFileHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 15),
    _IveFileHits_Type()
)
iveFileHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveFileHits.setStatus("current")
_IveWebHits_Type = Counter64
_IveWebHits_Object = MibScalar
iveWebHits = _IveWebHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 16),
    _IveWebHits_Type()
)
iveWebHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveWebHits.setStatus("current")
_IveAppletHits_Type = Counter64
_IveAppletHits_Object = MibScalar
iveAppletHits = _IveAppletHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 17),
    _IveAppletHits_Type()
)
iveAppletHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveAppletHits.setStatus("current")
_IvetermHits_Type = Counter64
_IvetermHits_Object = MibScalar
ivetermHits = _IvetermHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 18),
    _IvetermHits_Type()
)
ivetermHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ivetermHits.setStatus("current")
_IveSAMHits_Type = Counter64
_IveSAMHits_Object = MibScalar
iveSAMHits = _IveSAMHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 19),
    _IveSAMHits_Type()
)
iveSAMHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveSAMHits.setStatus("current")
_IveNCHits_Type = Counter64
_IveNCHits_Object = MibScalar
iveNCHits = _IveNCHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 20),
    _IveNCHits_Type()
)
iveNCHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iveNCHits.setStatus("current")
_MeetingHits_Type = Counter64
_MeetingHits_Object = MibScalar
meetingHits = _MeetingHits_Object(
    (1, 3, 6, 1, 4, 1, 12532, 21),
    _MeetingHits_Type()
)
meetingHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meetingHits.setStatus("current")
_IveTraps_ObjectIdentity = ObjectIdentity
iveTraps = _IveTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12532, 251)
)

# Managed Objects groups


# Notification objects

iveLogNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 4)
)
iveLogNearlyFull.setObjects(
    ("NEOTERIS-IVE-MIB", "logFullPercent")
)
if mibBuilder.loadTexts:
    iveLogNearlyFull.setStatus(
        "current"
    )

iveLogFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 5)
)
if mibBuilder.loadTexts:
    iveLogFull.setStatus(
        "current"
    )

iveMaxConcurrentUsersSignedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 6)
)
if mibBuilder.loadTexts:
    iveMaxConcurrentUsersSignedIn.setStatus(
        "current"
    )

iveTooManyFailedLoginAttempts = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 7)
)
iveTooManyFailedLoginAttempts.setObjects(
    ("NEOTERIS-IVE-MIB", "blockedIP")
)
if mibBuilder.loadTexts:
    iveTooManyFailedLoginAttempts.setStatus(
        "current"
    )

externalAuthServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 8)
)
externalAuthServerUnreachable.setObjects(
    ("NEOTERIS-IVE-MIB", "authServerName")
)
if mibBuilder.loadTexts:
    externalAuthServerUnreachable.setStatus(
        "current"
    )

iveStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 9)
)
if mibBuilder.loadTexts:
    iveStart.setStatus(
        "current"
    )

iveShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 10)
)
if mibBuilder.loadTexts:
    iveShutdown.setStatus(
        "current"
    )

iveReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 11)
)
if mibBuilder.loadTexts:
    iveReboot.setStatus(
        "current"
    )

archiveServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 12)
)
if mibBuilder.loadTexts:
    archiveServerUnreachable.setStatus(
        "current"
    )

archiveServerLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 13)
)
if mibBuilder.loadTexts:
    archiveServerLoginFailed.setStatus(
        "current"
    )

archiveFileTransferFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 14)
)
archiveFileTransferFailed.setObjects(
    ("NEOTERIS-IVE-MIB", "fileName")
)
if mibBuilder.loadTexts:
    archiveFileTransferFailed.setStatus(
        "current"
    )

meetingUserLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 15)
)
meetingUserLimit.setObjects(
    ("NEOTERIS-IVE-MIB", "meetingUserCount")
)
if mibBuilder.loadTexts:
    meetingUserLimit.setStatus(
        "current"
    )

iveRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12532, 251, 16)
)
if mibBuilder.loadTexts:
    iveRestart.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEOTERIS-IVE-MIB",
    **{"neoteris": neoteris,
       "logFullPercent": logFullPercent,
       "signedInWebUsers": signedInWebUsers,
       "signedInMailUsers": signedInMailUsers,
       "blockedIP": blockedIP,
       "authServerName": authServerName,
       "productName": productName,
       "productVersion": productVersion,
       "fileName": fileName,
       "meetingUserCount": meetingUserCount,
       "iveCpuUtil": iveCpuUtil,
       "iveMemoryUtil": iveMemoryUtil,
       "iveConcurrentUsers": iveConcurrentUsers,
       "clusterConcurrentUsers": clusterConcurrentUsers,
       "iveTotalHits": iveTotalHits,
       "iveFileHits": iveFileHits,
       "iveWebHits": iveWebHits,
       "iveAppletHits": iveAppletHits,
       "ivetermHits": ivetermHits,
       "iveSAMHits": iveSAMHits,
       "iveNCHits": iveNCHits,
       "meetingHits": meetingHits,
       "iveTraps": iveTraps,
       "iveLogNearlyFull": iveLogNearlyFull,
       "iveLogFull": iveLogFull,
       "iveMaxConcurrentUsersSignedIn": iveMaxConcurrentUsersSignedIn,
       "iveTooManyFailedLoginAttempts": iveTooManyFailedLoginAttempts,
       "externalAuthServerUnreachable": externalAuthServerUnreachable,
       "iveStart": iveStart,
       "iveShutdown": iveShutdown,
       "iveReboot": iveReboot,
       "archiveServerUnreachable": archiveServerUnreachable,
       "archiveServerLoginFailed": archiveServerLoginFailed,
       "archiveFileTransferFailed": archiveFileTransferFailed,
       "meetingUserLimit": meetingUserLimit,
       "iveRestart": iveRestart}
)
