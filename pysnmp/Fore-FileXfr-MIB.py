# SNMP MIB module (Fore-FileXfr-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-FileXfr-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:00 2024
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

(EntryStatus,
 fileXfr) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "EntryStatus",
    "fileXfr")

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
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

foreFileXfrModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FXfrGroup_ObjectIdentity = ObjectIdentity
fXfrGroup = _FXfrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2)
)
_FXfrNextIndex_Type = TestAndIncr
_FXfrNextIndex_Object = MibScalar
fXfrNextIndex = _FXfrNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 1),
    _FXfrNextIndex_Type()
)
fXfrNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fXfrNextIndex.setStatus("current")
_FXfrTable_Object = MibTable
fXfrTable = _FXfrTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    fXfrTable.setStatus("current")
_FXfrEntry_Object = MibTableRow
fXfrEntry = _FXfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1)
)
fXfrEntry.setIndexNames(
    (0, "Fore-FileXfr-MIB", "fXfrIndex"),
)
if mibBuilder.loadTexts:
    fXfrEntry.setStatus("current")
_FXfrIndex_Type = Integer32
_FXfrIndex_Object = MibTableColumn
fXfrIndex = _FXfrIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1, 1),
    _FXfrIndex_Type()
)
fXfrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fXfrIndex.setStatus("current")
_FXfrRemoteFileUrl_Type = DisplayString
_FXfrRemoteFileUrl_Object = MibTableColumn
fXfrRemoteFileUrl = _FXfrRemoteFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1, 2),
    _FXfrRemoteFileUrl_Type()
)
fXfrRemoteFileUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fXfrRemoteFileUrl.setStatus("current")
_FXfrLocalFile_Type = DisplayString
_FXfrLocalFile_Object = MibTableColumn
fXfrLocalFile = _FXfrLocalFile_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1, 3),
    _FXfrLocalFile_Type()
)
fXfrLocalFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fXfrLocalFile.setStatus("current")


class _FXfrDirection_Type(Integer32):
    """Custom type fXfrDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("put", 2))
    )


_FXfrDirection_Type.__name__ = "Integer32"
_FXfrDirection_Object = MibTableColumn
fXfrDirection = _FXfrDirection_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1, 4),
    _FXfrDirection_Type()
)
fXfrDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fXfrDirection.setStatus("current")
_FXfrEntryStatus_Type = EntryStatus
_FXfrEntryStatus_Object = MibTableColumn
fXfrEntryStatus = _FXfrEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1, 5),
    _FXfrEntryStatus_Type()
)
fXfrEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fXfrEntryStatus.setStatus("current")


class _FXfrStatus_Type(Integer32):
    """Custom type fXfrStatus based on Integer32"""
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
        *(("busy", 7),
          ("failed", 6),
          ("go", 2),
          ("idle", 1),
          ("inProgress", 4),
          ("inQueue", 3),
          ("succeeded", 5))
    )


_FXfrStatus_Type.__name__ = "Integer32"
_FXfrStatus_Object = MibTableColumn
fXfrStatus = _FXfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1, 6),
    _FXfrStatus_Type()
)
fXfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fXfrStatus.setStatus("current")
_FXfrStatusText_Type = DisplayString
_FXfrStatusText_Object = MibTableColumn
fXfrStatusText = _FXfrStatusText_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1, 7),
    _FXfrStatusText_Type()
)
fXfrStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fXfrStatusText.setStatus("current")
_FXfrOwnerIpAddress_Type = IpAddress
_FXfrOwnerIpAddress_Object = MibTableColumn
fXfrOwnerIpAddress = _FXfrOwnerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1, 8),
    _FXfrOwnerIpAddress_Type()
)
fXfrOwnerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fXfrOwnerIpAddress.setStatus("current")
_FXfrOwnerSignature_Type = DisplayString
_FXfrOwnerSignature_Object = MibTableColumn
fXfrOwnerSignature = _FXfrOwnerSignature_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1, 9),
    _FXfrOwnerSignature_Type()
)
fXfrOwnerSignature.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fXfrOwnerSignature.setStatus("current")


class _FXfrTransferType_Type(Integer32):
    """Custom type fXfrTransferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("binary", 1))
    )


_FXfrTransferType_Type.__name__ = "Integer32"
_FXfrTransferType_Object = MibTableColumn
fXfrTransferType = _FXfrTransferType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1, 10),
    _FXfrTransferType_Type()
)
fXfrTransferType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fXfrTransferType.setStatus("current")
_FXfrUserId_Type = DisplayString
_FXfrUserId_Object = MibTableColumn
fXfrUserId = _FXfrUserId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1, 11),
    _FXfrUserId_Type()
)
fXfrUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fXfrUserId.setStatus("current")
_FXfrPassword_Type = DisplayString
_FXfrPassword_Object = MibTableColumn
fXfrPassword = _FXfrPassword_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 6, 2, 2, 1, 12),
    _FXfrPassword_Type()
)
fXfrPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fXfrPassword.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-FileXfr-MIB",
    **{"foreFileXfrModule": foreFileXfrModule,
       "fXfrGroup": fXfrGroup,
       "fXfrNextIndex": fXfrNextIndex,
       "fXfrTable": fXfrTable,
       "fXfrEntry": fXfrEntry,
       "fXfrIndex": fXfrIndex,
       "fXfrRemoteFileUrl": fXfrRemoteFileUrl,
       "fXfrLocalFile": fXfrLocalFile,
       "fXfrDirection": fXfrDirection,
       "fXfrEntryStatus": fXfrEntryStatus,
       "fXfrStatus": fXfrStatus,
       "fXfrStatusText": fXfrStatusText,
       "fXfrOwnerIpAddress": fXfrOwnerIpAddress,
       "fXfrOwnerSignature": fXfrOwnerSignature,
       "fXfrTransferType": fXfrTransferType,
       "fXfrUserId": fXfrUserId,
       "fXfrPassword": fXfrPassword}
)
