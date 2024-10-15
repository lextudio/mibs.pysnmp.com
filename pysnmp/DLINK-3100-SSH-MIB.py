# SNMP MIB module (DLINK-3100-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-SSH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:20 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rlSsh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78)
)
rlSsh.setRevisions(
        ("2003-01-03 00:24",
         "2003-09-21 00:24")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlSshPublicKeyAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              999)
        )
    )
    namedValues = NamedValues(
        *(("dsa", 2),
          ("none", 999),
          ("rsa", 1),
          ("rsa1", 0))
    )



class RlSshPublicKeyDigestFormat(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bubbleBabble", 1),
          ("hex", 0))
    )



# MIB Managed Objects in the order of their OIDs

_RlSshMibVersion_Type = Integer32
_RlSshMibVersion_Object = MibScalar
rlSshMibVersion = _RlSshMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 1),
    _RlSshMibVersion_Type()
)
rlSshMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshMibVersion.setStatus("current")
_RlSshServer_ObjectIdentity = ObjectIdentity
rlSshServer = _RlSshServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2)
)
_RlSshServerHostPublicKeyTable_Object = MibTable
rlSshServerHostPublicKeyTable = _RlSshServerHostPublicKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 1)
)
if mibBuilder.loadTexts:
    rlSshServerHostPublicKeyTable.setStatus("current")
_RlSshServerHostPublicKeyTableEntry_Object = MibTableRow
rlSshServerHostPublicKeyTableEntry = _RlSshServerHostPublicKeyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 1, 1)
)
rlSshServerHostPublicKeyTableEntry.setIndexNames(
    (0, "DLINK-3100-SSH-MIB", "rlSshServerHostPublicKeyAlgorithm"),
    (0, "DLINK-3100-SSH-MIB", "rlSshServerHostPublicKeyFragmentId"),
)
if mibBuilder.loadTexts:
    rlSshServerHostPublicKeyTableEntry.setStatus("current")
_RlSshServerHostPublicKeyAlgorithm_Type = RlSshPublicKeyAlgorithm
_RlSshServerHostPublicKeyAlgorithm_Object = MibTableColumn
rlSshServerHostPublicKeyAlgorithm = _RlSshServerHostPublicKeyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 1, 1, 1),
    _RlSshServerHostPublicKeyAlgorithm_Type()
)
rlSshServerHostPublicKeyAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerHostPublicKeyAlgorithm.setStatus("current")
_RlSshServerHostPublicKeyFragmentId_Type = Unsigned32
_RlSshServerHostPublicKeyFragmentId_Object = MibTableColumn
rlSshServerHostPublicKeyFragmentId = _RlSshServerHostPublicKeyFragmentId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 1, 1, 2),
    _RlSshServerHostPublicKeyFragmentId_Type()
)
rlSshServerHostPublicKeyFragmentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerHostPublicKeyFragmentId.setStatus("current")
_RlSshServerHostPublicKeyFragmentText_Type = DisplayString
_RlSshServerHostPublicKeyFragmentText_Object = MibTableColumn
rlSshServerHostPublicKeyFragmentText = _RlSshServerHostPublicKeyFragmentText_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 1, 1, 3),
    _RlSshServerHostPublicKeyFragmentText_Type()
)
rlSshServerHostPublicKeyFragmentText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerHostPublicKeyFragmentText.setStatus("current")
_RlSshServerHostPublicKeyFingerprintTable_Object = MibTable
rlSshServerHostPublicKeyFingerprintTable = _RlSshServerHostPublicKeyFingerprintTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 2)
)
if mibBuilder.loadTexts:
    rlSshServerHostPublicKeyFingerprintTable.setStatus("current")
_RlSshServerHostPublicKeyFingerprintTableEntry_Object = MibTableRow
rlSshServerHostPublicKeyFingerprintTableEntry = _RlSshServerHostPublicKeyFingerprintTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 2, 1)
)
rlSshServerHostPublicKeyFingerprintTableEntry.setIndexNames(
    (0, "DLINK-3100-SSH-MIB", "rlSshServerHostPublicKeyFingerprintAlgorithm"),
    (0, "DLINK-3100-SSH-MIB", "rlSshServerHostPublicKeyFingerprintDigestFormat"),
)
if mibBuilder.loadTexts:
    rlSshServerHostPublicKeyFingerprintTableEntry.setStatus("current")
_RlSshServerHostPublicKeyFingerprintAlgorithm_Type = RlSshPublicKeyAlgorithm
_RlSshServerHostPublicKeyFingerprintAlgorithm_Object = MibTableColumn
rlSshServerHostPublicKeyFingerprintAlgorithm = _RlSshServerHostPublicKeyFingerprintAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 2, 1, 1),
    _RlSshServerHostPublicKeyFingerprintAlgorithm_Type()
)
rlSshServerHostPublicKeyFingerprintAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerHostPublicKeyFingerprintAlgorithm.setStatus("current")
_RlSshServerHostPublicKeyFingerprintDigestFormat_Type = RlSshPublicKeyDigestFormat
_RlSshServerHostPublicKeyFingerprintDigestFormat_Object = MibTableColumn
rlSshServerHostPublicKeyFingerprintDigestFormat = _RlSshServerHostPublicKeyFingerprintDigestFormat_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 2, 1, 2),
    _RlSshServerHostPublicKeyFingerprintDigestFormat_Type()
)
rlSshServerHostPublicKeyFingerprintDigestFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerHostPublicKeyFingerprintDigestFormat.setStatus("current")
_RlSshServerHostPublicKeyFingerprint_Type = DisplayString
_RlSshServerHostPublicKeyFingerprint_Object = MibTableColumn
rlSshServerHostPublicKeyFingerprint = _RlSshServerHostPublicKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 2, 1, 3),
    _RlSshServerHostPublicKeyFingerprint_Type()
)
rlSshServerHostPublicKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerHostPublicKeyFingerprint.setStatus("current")
_RlSshServerAuthorizedUsersPublicKeyTable_Object = MibTable
rlSshServerAuthorizedUsersPublicKeyTable = _RlSshServerAuthorizedUsersPublicKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 3)
)
if mibBuilder.loadTexts:
    rlSshServerAuthorizedUsersPublicKeyTable.setStatus("current")
_RlSshServerAuthorizedUsersPublicKeyTableEntry_Object = MibTableRow
rlSshServerAuthorizedUsersPublicKeyTableEntry = _RlSshServerAuthorizedUsersPublicKeyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 3, 1)
)
rlSshServerAuthorizedUsersPublicKeyTableEntry.setIndexNames(
    (0, "DLINK-3100-SSH-MIB", "rlSshServerAuthorizedUserName"),
    (0, "DLINK-3100-SSH-MIB", "rlSshServerAuthorizedUserPublicKeyFragmentId"),
)
if mibBuilder.loadTexts:
    rlSshServerAuthorizedUsersPublicKeyTableEntry.setStatus("current")


class _RlSshServerAuthorizedUserName_Type(DisplayString):
    """Custom type rlSshServerAuthorizedUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RlSshServerAuthorizedUserName_Type.__name__ = "DisplayString"
_RlSshServerAuthorizedUserName_Object = MibTableColumn
rlSshServerAuthorizedUserName = _RlSshServerAuthorizedUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 3, 1, 1),
    _RlSshServerAuthorizedUserName_Type()
)
rlSshServerAuthorizedUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSshServerAuthorizedUserName.setStatus("current")
_RlSshServerAuthorizedUserPublicKeyFragmentId_Type = Unsigned32
_RlSshServerAuthorizedUserPublicKeyFragmentId_Object = MibTableColumn
rlSshServerAuthorizedUserPublicKeyFragmentId = _RlSshServerAuthorizedUserPublicKeyFragmentId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 3, 1, 2),
    _RlSshServerAuthorizedUserPublicKeyFragmentId_Type()
)
rlSshServerAuthorizedUserPublicKeyFragmentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSshServerAuthorizedUserPublicKeyFragmentId.setStatus("current")
_RlSshServerAuthorizedUserPublicKeyFragmentText_Type = DisplayString
_RlSshServerAuthorizedUserPublicKeyFragmentText_Object = MibTableColumn
rlSshServerAuthorizedUserPublicKeyFragmentText = _RlSshServerAuthorizedUserPublicKeyFragmentText_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 3, 1, 3),
    _RlSshServerAuthorizedUserPublicKeyFragmentText_Type()
)
rlSshServerAuthorizedUserPublicKeyFragmentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSshServerAuthorizedUserPublicKeyFragmentText.setStatus("current")
_RlSshServerAuthorizedUserPublicKeyFragmentStatus_Type = RowStatus
_RlSshServerAuthorizedUserPublicKeyFragmentStatus_Object = MibTableColumn
rlSshServerAuthorizedUserPublicKeyFragmentStatus = _RlSshServerAuthorizedUserPublicKeyFragmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 3, 1, 4),
    _RlSshServerAuthorizedUserPublicKeyFragmentStatus_Type()
)
rlSshServerAuthorizedUserPublicKeyFragmentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSshServerAuthorizedUserPublicKeyFragmentStatus.setStatus("current")
_RlSshServerAuthorizedUsersPublicKeyFingerprintTable_Object = MibTable
rlSshServerAuthorizedUsersPublicKeyFingerprintTable = _RlSshServerAuthorizedUsersPublicKeyFingerprintTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 5)
)
if mibBuilder.loadTexts:
    rlSshServerAuthorizedUsersPublicKeyFingerprintTable.setStatus("current")
_RlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry_Object = MibTableRow
rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry = _RlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 5, 1)
)
rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry.setIndexNames(
    (0, "DLINK-3100-SSH-MIB", "rlSshServerAuthorizedUserFingerprintName"),
    (0, "DLINK-3100-SSH-MIB", "rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat"),
)
if mibBuilder.loadTexts:
    rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry.setStatus("current")


class _RlSshServerAuthorizedUserFingerprintName_Type(DisplayString):
    """Custom type rlSshServerAuthorizedUserFingerprintName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RlSshServerAuthorizedUserFingerprintName_Type.__name__ = "DisplayString"
_RlSshServerAuthorizedUserFingerprintName_Object = MibTableColumn
rlSshServerAuthorizedUserFingerprintName = _RlSshServerAuthorizedUserFingerprintName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 5, 1, 1),
    _RlSshServerAuthorizedUserFingerprintName_Type()
)
rlSshServerAuthorizedUserFingerprintName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSshServerAuthorizedUserFingerprintName.setStatus("current")
_RlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm_Type = RlSshPublicKeyAlgorithm
_RlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm_Object = MibTableColumn
rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm = _RlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 5, 1, 2),
    _RlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm_Type()
)
rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm.setStatus("current")
_RlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat_Type = RlSshPublicKeyDigestFormat
_RlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat_Object = MibTableColumn
rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat = _RlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 5, 1, 3),
    _RlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat_Type()
)
rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat.setStatus("current")
_RlSshServerAuthorizedUserPublicKeyFingerprint_Type = DisplayString
_RlSshServerAuthorizedUserPublicKeyFingerprint_Object = MibTableColumn
rlSshServerAuthorizedUserPublicKeyFingerprint = _RlSshServerAuthorizedUserPublicKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 5, 1, 4),
    _RlSshServerAuthorizedUserPublicKeyFingerprint_Type()
)
rlSshServerAuthorizedUserPublicKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerAuthorizedUserPublicKeyFingerprint.setStatus("current")
_RlSshServerSessionTable_Object = MibTable
rlSshServerSessionTable = _RlSshServerSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 6)
)
if mibBuilder.loadTexts:
    rlSshServerSessionTable.setStatus("current")
_RlSshServerSessionTableEntry_Object = MibTableRow
rlSshServerSessionTableEntry = _RlSshServerSessionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 6, 1)
)
rlSshServerSessionTableEntry.setIndexNames(
    (0, "DLINK-3100-SSH-MIB", "rlSshServerSessionIdentifier"),
)
if mibBuilder.loadTexts:
    rlSshServerSessionTableEntry.setStatus("current")
_RlSshServerSessionIdentifier_Type = Unsigned32
_RlSshServerSessionIdentifier_Object = MibTableColumn
rlSshServerSessionIdentifier = _RlSshServerSessionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 6, 1, 1),
    _RlSshServerSessionIdentifier_Type()
)
rlSshServerSessionIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionIdentifier.setStatus("current")
_RlSshServerSessionPeerAddress_Type = IpAddress
_RlSshServerSessionPeerAddress_Object = MibTableColumn
rlSshServerSessionPeerAddress = _RlSshServerSessionPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 6, 1, 2),
    _RlSshServerSessionPeerAddress_Type()
)
rlSshServerSessionPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionPeerAddress.setStatus("current")
_RlSshServerSessionPeerPort_Type = Unsigned32
_RlSshServerSessionPeerPort_Object = MibTableColumn
rlSshServerSessionPeerPort = _RlSshServerSessionPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 6, 1, 3),
    _RlSshServerSessionPeerPort_Type()
)
rlSshServerSessionPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionPeerPort.setStatus("current")
_RlSshServerSessionPeerVersion_Type = DisplayString
_RlSshServerSessionPeerVersion_Object = MibTableColumn
rlSshServerSessionPeerVersion = _RlSshServerSessionPeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 6, 1, 4),
    _RlSshServerSessionPeerVersion_Type()
)
rlSshServerSessionPeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionPeerVersion.setStatus("current")
_RlSshServerSessionUsername_Type = DisplayString
_RlSshServerSessionUsername_Object = MibTableColumn
rlSshServerSessionUsername = _RlSshServerSessionUsername_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 6, 1, 5),
    _RlSshServerSessionUsername_Type()
)
rlSshServerSessionUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionUsername.setStatus("current")
_RlSshServerSessionCipher_Type = DisplayString
_RlSshServerSessionCipher_Object = MibTableColumn
rlSshServerSessionCipher = _RlSshServerSessionCipher_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 6, 1, 6),
    _RlSshServerSessionCipher_Type()
)
rlSshServerSessionCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionCipher.setStatus("current")
_RlSshServerSessionHMAC_Type = DisplayString
_RlSshServerSessionHMAC_Object = MibTableColumn
rlSshServerSessionHMAC = _RlSshServerSessionHMAC_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 6, 1, 7),
    _RlSshServerSessionHMAC_Type()
)
rlSshServerSessionHMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionHMAC.setStatus("current")
_RlSshServerSessionInetTable_Object = MibTable
rlSshServerSessionInetTable = _RlSshServerSessionInetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 7)
)
if mibBuilder.loadTexts:
    rlSshServerSessionInetTable.setStatus("current")
_RlSshServerSessionInetTableEntry_Object = MibTableRow
rlSshServerSessionInetTableEntry = _RlSshServerSessionInetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 7, 1)
)
rlSshServerSessionInetTableEntry.setIndexNames(
    (0, "DLINK-3100-SSH-MIB", "rlSshServerSessionInetIdentifier"),
)
if mibBuilder.loadTexts:
    rlSshServerSessionInetTableEntry.setStatus("current")
_RlSshServerSessionInetIdentifier_Type = Unsigned32
_RlSshServerSessionInetIdentifier_Object = MibTableColumn
rlSshServerSessionInetIdentifier = _RlSshServerSessionInetIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 7, 1, 1),
    _RlSshServerSessionInetIdentifier_Type()
)
rlSshServerSessionInetIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionInetIdentifier.setStatus("current")
_RlSshServerSessionInetPeerAddressType_Type = InetAddressType
_RlSshServerSessionInetPeerAddressType_Object = MibTableColumn
rlSshServerSessionInetPeerAddressType = _RlSshServerSessionInetPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 7, 1, 2),
    _RlSshServerSessionInetPeerAddressType_Type()
)
rlSshServerSessionInetPeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionInetPeerAddressType.setStatus("current")
_RlSshServerSessionInetPeerAddress_Type = InetAddress
_RlSshServerSessionInetPeerAddress_Object = MibTableColumn
rlSshServerSessionInetPeerAddress = _RlSshServerSessionInetPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 7, 1, 3),
    _RlSshServerSessionInetPeerAddress_Type()
)
rlSshServerSessionInetPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionInetPeerAddress.setStatus("current")
_RlSshServerSessionInetPeerPort_Type = Unsigned32
_RlSshServerSessionInetPeerPort_Object = MibTableColumn
rlSshServerSessionInetPeerPort = _RlSshServerSessionInetPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 7, 1, 4),
    _RlSshServerSessionInetPeerPort_Type()
)
rlSshServerSessionInetPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionInetPeerPort.setStatus("current")
_RlSshServerSessionInetPeerVersion_Type = DisplayString
_RlSshServerSessionInetPeerVersion_Object = MibTableColumn
rlSshServerSessionInetPeerVersion = _RlSshServerSessionInetPeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 7, 1, 5),
    _RlSshServerSessionInetPeerVersion_Type()
)
rlSshServerSessionInetPeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionInetPeerVersion.setStatus("current")
_RlSshServerSessionInetUsername_Type = DisplayString
_RlSshServerSessionInetUsername_Object = MibTableColumn
rlSshServerSessionInetUsername = _RlSshServerSessionInetUsername_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 7, 1, 6),
    _RlSshServerSessionInetUsername_Type()
)
rlSshServerSessionInetUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionInetUsername.setStatus("current")
_RlSshServerSessionInetCipher_Type = DisplayString
_RlSshServerSessionInetCipher_Object = MibTableColumn
rlSshServerSessionInetCipher = _RlSshServerSessionInetCipher_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 7, 1, 7),
    _RlSshServerSessionInetCipher_Type()
)
rlSshServerSessionInetCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionInetCipher.setStatus("current")
_RlSshServerSessionInetHMAC_Type = DisplayString
_RlSshServerSessionInetHMAC_Object = MibTableColumn
rlSshServerSessionInetHMAC = _RlSshServerSessionInetHMAC_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 7, 1, 8),
    _RlSshServerSessionInetHMAC_Type()
)
rlSshServerSessionInetHMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshServerSessionInetHMAC.setStatus("current")


class _RlSshServerPort_Type(Unsigned32):
    """Custom type rlSshServerPort based on Unsigned32"""
    defaultValue = 22

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlSshServerPort_Type.__name__ = "Unsigned32"
_RlSshServerPort_Object = MibScalar
rlSshServerPort = _RlSshServerPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 101),
    _RlSshServerPort_Type()
)
rlSshServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSshServerPort.setStatus("current")


class _RlSshServerEnable_Type(Integer32):
    """Custom type rlSshServerEnable based on Integer32"""
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


_RlSshServerEnable_Type.__name__ = "Integer32"
_RlSshServerEnable_Object = MibScalar
rlSshServerEnable = _RlSshServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 102),
    _RlSshServerEnable_Type()
)
rlSshServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSshServerEnable.setStatus("current")


class _RlSshServerEnablePublicKeyAuthentication_Type(Integer32):
    """Custom type rlSshServerEnablePublicKeyAuthentication based on Integer32"""
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


_RlSshServerEnablePublicKeyAuthentication_Type.__name__ = "Integer32"
_RlSshServerEnablePublicKeyAuthentication_Object = MibScalar
rlSshServerEnablePublicKeyAuthentication = _RlSshServerEnablePublicKeyAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 103),
    _RlSshServerEnablePublicKeyAuthentication_Type()
)
rlSshServerEnablePublicKeyAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSshServerEnablePublicKeyAuthentication.setStatus("current")
_RlSshServerRegenerateHostKey_Type = RlSshPublicKeyAlgorithm
_RlSshServerRegenerateHostKey_Object = MibScalar
rlSshServerRegenerateHostKey = _RlSshServerRegenerateHostKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 2, 104),
    _RlSshServerRegenerateHostKey_Type()
)
rlSshServerRegenerateHostKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSshServerRegenerateHostKey.setStatus("current")
_RlSshClient_ObjectIdentity = ObjectIdentity
rlSshClient = _RlSshClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3)
)
_RlSshClientUserName_Type = DisplayString
_RlSshClientUserName_Object = MibScalar
rlSshClientUserName = _RlSshClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3, 1),
    _RlSshClientUserName_Type()
)
rlSshClientUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSshClientUserName.setStatus("current")
_RlSshClientRegenerateSelfKey_Type = RlSshPublicKeyAlgorithm
_RlSshClientRegenerateSelfKey_Object = MibScalar
rlSshClientRegenerateSelfKey = _RlSshClientRegenerateSelfKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3, 2),
    _RlSshClientRegenerateSelfKey_Type()
)
rlSshClientRegenerateSelfKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSshClientRegenerateSelfKey.setStatus("current")
_RlSshClientSelfPublicKeyTable_Object = MibTable
rlSshClientSelfPublicKeyTable = _RlSshClientSelfPublicKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3, 3)
)
if mibBuilder.loadTexts:
    rlSshClientSelfPublicKeyTable.setStatus("current")
_RlSshClientSelfPublicKeyTableEntry_Object = MibTableRow
rlSshClientSelfPublicKeyTableEntry = _RlSshClientSelfPublicKeyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3, 3, 1)
)
rlSshClientSelfPublicKeyTableEntry.setIndexNames(
    (0, "DLINK-3100-SSH-MIB", "rlSshClientSelfPublicKeyAlgorithm"),
    (0, "DLINK-3100-SSH-MIB", "rlSshClientSelfPublicKeyFragmentId"),
)
if mibBuilder.loadTexts:
    rlSshClientSelfPublicKeyTableEntry.setStatus("current")
_RlSshClientSelfPublicKeyFragmentId_Type = Unsigned32
_RlSshClientSelfPublicKeyFragmentId_Object = MibTableColumn
rlSshClientSelfPublicKeyFragmentId = _RlSshClientSelfPublicKeyFragmentId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3, 3, 1, 1),
    _RlSshClientSelfPublicKeyFragmentId_Type()
)
rlSshClientSelfPublicKeyFragmentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshClientSelfPublicKeyFragmentId.setStatus("current")
_RlSshClientSelfPublicKeyAlgorithm_Type = RlSshPublicKeyAlgorithm
_RlSshClientSelfPublicKeyAlgorithm_Object = MibTableColumn
rlSshClientSelfPublicKeyAlgorithm = _RlSshClientSelfPublicKeyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3, 3, 1, 2),
    _RlSshClientSelfPublicKeyAlgorithm_Type()
)
rlSshClientSelfPublicKeyAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshClientSelfPublicKeyAlgorithm.setStatus("current")
_RlSshClientSelfPublicKeyFragmentText_Type = DisplayString
_RlSshClientSelfPublicKeyFragmentText_Object = MibTableColumn
rlSshClientSelfPublicKeyFragmentText = _RlSshClientSelfPublicKeyFragmentText_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3, 3, 1, 3),
    _RlSshClientSelfPublicKeyFragmentText_Type()
)
rlSshClientSelfPublicKeyFragmentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSshClientSelfPublicKeyFragmentText.setStatus("current")
_RlSshClientSelfPublicKeyFingerprintTable_Object = MibTable
rlSshClientSelfPublicKeyFingerprintTable = _RlSshClientSelfPublicKeyFingerprintTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3, 4)
)
if mibBuilder.loadTexts:
    rlSshClientSelfPublicKeyFingerprintTable.setStatus("current")
_RlSshClientSelfPublicKeyFingerprintTableEntry_Object = MibTableRow
rlSshClientSelfPublicKeyFingerprintTableEntry = _RlSshClientSelfPublicKeyFingerprintTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3, 4, 1)
)
rlSshClientSelfPublicKeyFingerprintTableEntry.setIndexNames(
    (0, "DLINK-3100-SSH-MIB", "rlSshClientSelfPublicKeyFingerprintAlgorithm"),
    (0, "DLINK-3100-SSH-MIB", "rlSshClientSelfPublicKeyFingerprintDigestFormat"),
)
if mibBuilder.loadTexts:
    rlSshClientSelfPublicKeyFingerprintTableEntry.setStatus("current")
_RlSshClientSelfPublicKeyFingerprintAlgorithm_Type = RlSshPublicKeyAlgorithm
_RlSshClientSelfPublicKeyFingerprintAlgorithm_Object = MibTableColumn
rlSshClientSelfPublicKeyFingerprintAlgorithm = _RlSshClientSelfPublicKeyFingerprintAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3, 4, 1, 1),
    _RlSshClientSelfPublicKeyFingerprintAlgorithm_Type()
)
rlSshClientSelfPublicKeyFingerprintAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshClientSelfPublicKeyFingerprintAlgorithm.setStatus("current")
_RlSshClientSelfPublicKeyFingerprintDigestFormat_Type = RlSshPublicKeyDigestFormat
_RlSshClientSelfPublicKeyFingerprintDigestFormat_Object = MibTableColumn
rlSshClientSelfPublicKeyFingerprintDigestFormat = _RlSshClientSelfPublicKeyFingerprintDigestFormat_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3, 4, 1, 2),
    _RlSshClientSelfPublicKeyFingerprintDigestFormat_Type()
)
rlSshClientSelfPublicKeyFingerprintDigestFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshClientSelfPublicKeyFingerprintDigestFormat.setStatus("current")
_RlSshClientSelfPublicKeyFingerprint_Type = DisplayString
_RlSshClientSelfPublicKeyFingerprint_Object = MibTableColumn
rlSshClientSelfPublicKeyFingerprint = _RlSshClientSelfPublicKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 78, 3, 4, 1, 3),
    _RlSshClientSelfPublicKeyFingerprint_Type()
)
rlSshClientSelfPublicKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSshClientSelfPublicKeyFingerprint.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-SSH-MIB",
    **{"RlSshPublicKeyAlgorithm": RlSshPublicKeyAlgorithm,
       "RlSshPublicKeyDigestFormat": RlSshPublicKeyDigestFormat,
       "rlSsh": rlSsh,
       "rlSshMibVersion": rlSshMibVersion,
       "rlSshServer": rlSshServer,
       "rlSshServerHostPublicKeyTable": rlSshServerHostPublicKeyTable,
       "rlSshServerHostPublicKeyTableEntry": rlSshServerHostPublicKeyTableEntry,
       "rlSshServerHostPublicKeyAlgorithm": rlSshServerHostPublicKeyAlgorithm,
       "rlSshServerHostPublicKeyFragmentId": rlSshServerHostPublicKeyFragmentId,
       "rlSshServerHostPublicKeyFragmentText": rlSshServerHostPublicKeyFragmentText,
       "rlSshServerHostPublicKeyFingerprintTable": rlSshServerHostPublicKeyFingerprintTable,
       "rlSshServerHostPublicKeyFingerprintTableEntry": rlSshServerHostPublicKeyFingerprintTableEntry,
       "rlSshServerHostPublicKeyFingerprintAlgorithm": rlSshServerHostPublicKeyFingerprintAlgorithm,
       "rlSshServerHostPublicKeyFingerprintDigestFormat": rlSshServerHostPublicKeyFingerprintDigestFormat,
       "rlSshServerHostPublicKeyFingerprint": rlSshServerHostPublicKeyFingerprint,
       "rlSshServerAuthorizedUsersPublicKeyTable": rlSshServerAuthorizedUsersPublicKeyTable,
       "rlSshServerAuthorizedUsersPublicKeyTableEntry": rlSshServerAuthorizedUsersPublicKeyTableEntry,
       "rlSshServerAuthorizedUserName": rlSshServerAuthorizedUserName,
       "rlSshServerAuthorizedUserPublicKeyFragmentId": rlSshServerAuthorizedUserPublicKeyFragmentId,
       "rlSshServerAuthorizedUserPublicKeyFragmentText": rlSshServerAuthorizedUserPublicKeyFragmentText,
       "rlSshServerAuthorizedUserPublicKeyFragmentStatus": rlSshServerAuthorizedUserPublicKeyFragmentStatus,
       "rlSshServerAuthorizedUsersPublicKeyFingerprintTable": rlSshServerAuthorizedUsersPublicKeyFingerprintTable,
       "rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry": rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry,
       "rlSshServerAuthorizedUserFingerprintName": rlSshServerAuthorizedUserFingerprintName,
       "rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm": rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm,
       "rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat": rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat,
       "rlSshServerAuthorizedUserPublicKeyFingerprint": rlSshServerAuthorizedUserPublicKeyFingerprint,
       "rlSshServerSessionTable": rlSshServerSessionTable,
       "rlSshServerSessionTableEntry": rlSshServerSessionTableEntry,
       "rlSshServerSessionIdentifier": rlSshServerSessionIdentifier,
       "rlSshServerSessionPeerAddress": rlSshServerSessionPeerAddress,
       "rlSshServerSessionPeerPort": rlSshServerSessionPeerPort,
       "rlSshServerSessionPeerVersion": rlSshServerSessionPeerVersion,
       "rlSshServerSessionUsername": rlSshServerSessionUsername,
       "rlSshServerSessionCipher": rlSshServerSessionCipher,
       "rlSshServerSessionHMAC": rlSshServerSessionHMAC,
       "rlSshServerSessionInetTable": rlSshServerSessionInetTable,
       "rlSshServerSessionInetTableEntry": rlSshServerSessionInetTableEntry,
       "rlSshServerSessionInetIdentifier": rlSshServerSessionInetIdentifier,
       "rlSshServerSessionInetPeerAddressType": rlSshServerSessionInetPeerAddressType,
       "rlSshServerSessionInetPeerAddress": rlSshServerSessionInetPeerAddress,
       "rlSshServerSessionInetPeerPort": rlSshServerSessionInetPeerPort,
       "rlSshServerSessionInetPeerVersion": rlSshServerSessionInetPeerVersion,
       "rlSshServerSessionInetUsername": rlSshServerSessionInetUsername,
       "rlSshServerSessionInetCipher": rlSshServerSessionInetCipher,
       "rlSshServerSessionInetHMAC": rlSshServerSessionInetHMAC,
       "rlSshServerPort": rlSshServerPort,
       "rlSshServerEnable": rlSshServerEnable,
       "rlSshServerEnablePublicKeyAuthentication": rlSshServerEnablePublicKeyAuthentication,
       "rlSshServerRegenerateHostKey": rlSshServerRegenerateHostKey,
       "rlSshClient": rlSshClient,
       "rlSshClientUserName": rlSshClientUserName,
       "rlSshClientRegenerateSelfKey": rlSshClientRegenerateSelfKey,
       "rlSshClientSelfPublicKeyTable": rlSshClientSelfPublicKeyTable,
       "rlSshClientSelfPublicKeyTableEntry": rlSshClientSelfPublicKeyTableEntry,
       "rlSshClientSelfPublicKeyFragmentId": rlSshClientSelfPublicKeyFragmentId,
       "rlSshClientSelfPublicKeyAlgorithm": rlSshClientSelfPublicKeyAlgorithm,
       "rlSshClientSelfPublicKeyFragmentText": rlSshClientSelfPublicKeyFragmentText,
       "rlSshClientSelfPublicKeyFingerprintTable": rlSshClientSelfPublicKeyFingerprintTable,
       "rlSshClientSelfPublicKeyFingerprintTableEntry": rlSshClientSelfPublicKeyFingerprintTableEntry,
       "rlSshClientSelfPublicKeyFingerprintAlgorithm": rlSshClientSelfPublicKeyFingerprintAlgorithm,
       "rlSshClientSelfPublicKeyFingerprintDigestFormat": rlSshClientSelfPublicKeyFingerprintDigestFormat,
       "rlSshClientSelfPublicKeyFingerprint": rlSshClientSelfPublicKeyFingerprint}
)
