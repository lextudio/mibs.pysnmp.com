# SNMP MIB module (AT-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:25 2024
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

atNtp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502)
)
atNtp.setRevisions(
        ("2010-09-07 00:00",
         "2010-06-15 00:15",
         "2008-11-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AtNtpPeerIndexNext_Type(Integer32):
    """Custom type atNtpPeerIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtNtpPeerIndexNext_Type.__name__ = "Integer32"
_AtNtpPeerIndexNext_Object = MibScalar
atNtpPeerIndexNext = _AtNtpPeerIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 6),
    _AtNtpPeerIndexNext_Type()
)
atNtpPeerIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpPeerIndexNext.setStatus("current")
_AtNtpPeerTable_Object = MibTable
atNtpPeerTable = _AtNtpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7)
)
if mibBuilder.loadTexts:
    atNtpPeerTable.setStatus("current")
_AtNtpPeerEntry_Object = MibTableRow
atNtpPeerEntry = _AtNtpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1)
)
atNtpPeerEntry.setIndexNames(
    (0, "AT-NTP-MIB", "atNtpPeerIndex"),
)
if mibBuilder.loadTexts:
    atNtpPeerEntry.setStatus("current")


class _AtNtpPeerIndex_Type(Integer32):
    """Custom type atNtpPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtNtpPeerIndex_Type.__name__ = "Integer32"
_AtNtpPeerIndex_Object = MibTableColumn
atNtpPeerIndex = _AtNtpPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 1),
    _AtNtpPeerIndex_Type()
)
atNtpPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atNtpPeerIndex.setStatus("current")


class _AtNtpPeerNameAddr_Type(DisplayString):
    """Custom type atNtpPeerNameAddr based on DisplayString"""
    defaultValue = OctetString("0.0.0.0")


_AtNtpPeerNameAddr_Object = MibTableColumn
atNtpPeerNameAddr = _AtNtpPeerNameAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 2),
    _AtNtpPeerNameAddr_Type()
)
atNtpPeerNameAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNtpPeerNameAddr.setStatus("current")


class _AtNtpPeerMode_Type(Integer32):
    """Custom type atNtpPeerMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("peer", 2),
          ("server", 1))
    )


_AtNtpPeerMode_Type.__name__ = "Integer32"
_AtNtpPeerMode_Object = MibTableColumn
atNtpPeerMode = _AtNtpPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 3),
    _AtNtpPeerMode_Type()
)
atNtpPeerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNtpPeerMode.setStatus("current")


class _AtNtpPeerPreference_Type(Integer32):
    """Custom type atNtpPeerPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AtNtpPeerPreference_Type.__name__ = "Integer32"
_AtNtpPeerPreference_Object = MibTableColumn
atNtpPeerPreference = _AtNtpPeerPreference_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 4),
    _AtNtpPeerPreference_Type()
)
atNtpPeerPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNtpPeerPreference.setStatus("current")


class _AtNtpPeerVersion_Type(Integer32):
    """Custom type atNtpPeerVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AtNtpPeerVersion_Type.__name__ = "Integer32"
_AtNtpPeerVersion_Object = MibTableColumn
atNtpPeerVersion = _AtNtpPeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 5),
    _AtNtpPeerVersion_Type()
)
atNtpPeerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNtpPeerVersion.setStatus("current")


class _AtNtpPeerKeyNumber_Type(Unsigned32):
    """Custom type atNtpPeerKeyNumber based on Unsigned32"""
    defaultValue = 0


_AtNtpPeerKeyNumber_Object = MibTableColumn
atNtpPeerKeyNumber = _AtNtpPeerKeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 6),
    _AtNtpPeerKeyNumber_Type()
)
atNtpPeerKeyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNtpPeerKeyNumber.setStatus("current")


class _AtNtpPeerRowStatus_Type(RowStatus):
    """Custom type atNtpPeerRowStatus based on RowStatus"""
    defaultValue = 1


_AtNtpPeerRowStatus_Object = MibTableColumn
atNtpPeerRowStatus = _AtNtpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 7),
    _AtNtpPeerRowStatus_Type()
)
atNtpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atNtpPeerRowStatus.setStatus("current")
_AtNtpAssociationTable_Object = MibTable
atNtpAssociationTable = _AtNtpAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10)
)
if mibBuilder.loadTexts:
    atNtpAssociationTable.setStatus("current")
_AtNtpAssociationEntry_Object = MibTableRow
atNtpAssociationEntry = _AtNtpAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1)
)
atNtpAssociationEntry.setIndexNames(
    (0, "AT-NTP-MIB", "atNtpAssociationIndex"),
)
if mibBuilder.loadTexts:
    atNtpAssociationEntry.setStatus("current")


class _AtNtpAssociationIndex_Type(Integer32):
    """Custom type atNtpAssociationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtNtpAssociationIndex_Type.__name__ = "Integer32"
_AtNtpAssociationIndex_Object = MibTableColumn
atNtpAssociationIndex = _AtNtpAssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 1),
    _AtNtpAssociationIndex_Type()
)
atNtpAssociationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atNtpAssociationIndex.setStatus("current")
_AtNtpAssociationPeerAddr_Type = DisplayString
_AtNtpAssociationPeerAddr_Object = MibTableColumn
atNtpAssociationPeerAddr = _AtNtpAssociationPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 2),
    _AtNtpAssociationPeerAddr_Type()
)
atNtpAssociationPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpAssociationPeerAddr.setStatus("current")
_AtNtpAssocaitionStatus_Type = DisplayString
_AtNtpAssocaitionStatus_Object = MibTableColumn
atNtpAssocaitionStatus = _AtNtpAssocaitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 3),
    _AtNtpAssocaitionStatus_Type()
)
atNtpAssocaitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpAssocaitionStatus.setStatus("current")
_AtNtpAssociationConfigured_Type = DisplayString
_AtNtpAssociationConfigured_Object = MibTableColumn
atNtpAssociationConfigured = _AtNtpAssociationConfigured_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 4),
    _AtNtpAssociationConfigured_Type()
)
atNtpAssociationConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpAssociationConfigured.setStatus("current")
_AtNtpAssociationRefClkAddr_Type = DisplayString
_AtNtpAssociationRefClkAddr_Object = MibTableColumn
atNtpAssociationRefClkAddr = _AtNtpAssociationRefClkAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 5),
    _AtNtpAssociationRefClkAddr_Type()
)
atNtpAssociationRefClkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpAssociationRefClkAddr.setStatus("current")
_AtNtpAssociationStratum_Type = Integer32
_AtNtpAssociationStratum_Object = MibTableColumn
atNtpAssociationStratum = _AtNtpAssociationStratum_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 6),
    _AtNtpAssociationStratum_Type()
)
atNtpAssociationStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpAssociationStratum.setStatus("current")
_AtNtpAssociationPoll_Type = Integer32
_AtNtpAssociationPoll_Object = MibTableColumn
atNtpAssociationPoll = _AtNtpAssociationPoll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 7),
    _AtNtpAssociationPoll_Type()
)
atNtpAssociationPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpAssociationPoll.setStatus("current")
if mibBuilder.loadTexts:
    atNtpAssociationPoll.setUnits("seconds")
_AtNtpAssociationReach_Type = Integer32
_AtNtpAssociationReach_Object = MibTableColumn
atNtpAssociationReach = _AtNtpAssociationReach_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 8),
    _AtNtpAssociationReach_Type()
)
atNtpAssociationReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpAssociationReach.setStatus("current")
_AtNtpAssociationDelay_Type = DisplayString
_AtNtpAssociationDelay_Object = MibTableColumn
atNtpAssociationDelay = _AtNtpAssociationDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 9),
    _AtNtpAssociationDelay_Type()
)
atNtpAssociationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpAssociationDelay.setStatus("current")
_AtNtpAssociationOffset_Type = DisplayString
_AtNtpAssociationOffset_Object = MibTableColumn
atNtpAssociationOffset = _AtNtpAssociationOffset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 10),
    _AtNtpAssociationOffset_Type()
)
atNtpAssociationOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpAssociationOffset.setStatus("current")
_AtNtpAssociationDisp_Type = DisplayString
_AtNtpAssociationDisp_Object = MibTableColumn
atNtpAssociationDisp = _AtNtpAssociationDisp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 11),
    _AtNtpAssociationDisp_Type()
)
atNtpAssociationDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpAssociationDisp.setStatus("current")
_AtNtpStatus_ObjectIdentity = ObjectIdentity
atNtpStatus = _AtNtpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11)
)
_AtNtpSysClockSync_Type = TruthValue
_AtNtpSysClockSync_Object = MibScalar
atNtpSysClockSync = _AtNtpSysClockSync_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 1),
    _AtNtpSysClockSync_Type()
)
atNtpSysClockSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpSysClockSync.setStatus("current")
_AtNtpSysStratum_Type = Integer32
_AtNtpSysStratum_Object = MibScalar
atNtpSysStratum = _AtNtpSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 2),
    _AtNtpSysStratum_Type()
)
atNtpSysStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpSysStratum.setStatus("current")
_AtNtpSysReference_Type = DisplayString
_AtNtpSysReference_Object = MibScalar
atNtpSysReference = _AtNtpSysReference_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 3),
    _AtNtpSysReference_Type()
)
atNtpSysReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpSysReference.setStatus("current")
_AtNtpSysFrequency_Type = Integer32
_AtNtpSysFrequency_Object = MibScalar
atNtpSysFrequency = _AtNtpSysFrequency_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 4),
    _AtNtpSysFrequency_Type()
)
atNtpSysFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpSysFrequency.setStatus("current")
if mibBuilder.loadTexts:
    atNtpSysFrequency.setUnits("Hz")
_AtNtpSysPrecision_Type = Integer32
_AtNtpSysPrecision_Object = MibScalar
atNtpSysPrecision = _AtNtpSysPrecision_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 5),
    _AtNtpSysPrecision_Type()
)
atNtpSysPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpSysPrecision.setStatus("current")


class _AtNtpSysRefTime_Type(OctetString):
    """Custom type atNtpSysRefTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AtNtpSysRefTime_Type.__name__ = "OctetString"
_AtNtpSysRefTime_Object = MibScalar
atNtpSysRefTime = _AtNtpSysRefTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 6),
    _AtNtpSysRefTime_Type()
)
atNtpSysRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpSysRefTime.setStatus("current")
_AtNtpSysClkOffset_Type = Integer32
_AtNtpSysClkOffset_Object = MibScalar
atNtpSysClkOffset = _AtNtpSysClkOffset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 7),
    _AtNtpSysClkOffset_Type()
)
atNtpSysClkOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpSysClkOffset.setStatus("current")
if mibBuilder.loadTexts:
    atNtpSysClkOffset.setUnits("millisecond")
_AtNtpSysRootDelay_Type = Integer32
_AtNtpSysRootDelay_Object = MibScalar
atNtpSysRootDelay = _AtNtpSysRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 8),
    _AtNtpSysRootDelay_Type()
)
atNtpSysRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpSysRootDelay.setStatus("current")
if mibBuilder.loadTexts:
    atNtpSysRootDelay.setUnits("millisecond")
_AtNtpSysRootDisp_Type = Integer32
_AtNtpSysRootDisp_Object = MibScalar
atNtpSysRootDisp = _AtNtpSysRootDisp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 9),
    _AtNtpSysRootDisp_Type()
)
atNtpSysRootDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNtpSysRootDisp.setStatus("current")
if mibBuilder.loadTexts:
    atNtpSysRootDisp.setUnits("millisecond")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-NTP-MIB",
    **{"atNtp": atNtp,
       "atNtpPeerIndexNext": atNtpPeerIndexNext,
       "atNtpPeerTable": atNtpPeerTable,
       "atNtpPeerEntry": atNtpPeerEntry,
       "atNtpPeerIndex": atNtpPeerIndex,
       "atNtpPeerNameAddr": atNtpPeerNameAddr,
       "atNtpPeerMode": atNtpPeerMode,
       "atNtpPeerPreference": atNtpPeerPreference,
       "atNtpPeerVersion": atNtpPeerVersion,
       "atNtpPeerKeyNumber": atNtpPeerKeyNumber,
       "atNtpPeerRowStatus": atNtpPeerRowStatus,
       "atNtpAssociationTable": atNtpAssociationTable,
       "atNtpAssociationEntry": atNtpAssociationEntry,
       "atNtpAssociationIndex": atNtpAssociationIndex,
       "atNtpAssociationPeerAddr": atNtpAssociationPeerAddr,
       "atNtpAssocaitionStatus": atNtpAssocaitionStatus,
       "atNtpAssociationConfigured": atNtpAssociationConfigured,
       "atNtpAssociationRefClkAddr": atNtpAssociationRefClkAddr,
       "atNtpAssociationStratum": atNtpAssociationStratum,
       "atNtpAssociationPoll": atNtpAssociationPoll,
       "atNtpAssociationReach": atNtpAssociationReach,
       "atNtpAssociationDelay": atNtpAssociationDelay,
       "atNtpAssociationOffset": atNtpAssociationOffset,
       "atNtpAssociationDisp": atNtpAssociationDisp,
       "atNtpStatus": atNtpStatus,
       "atNtpSysClockSync": atNtpSysClockSync,
       "atNtpSysStratum": atNtpSysStratum,
       "atNtpSysReference": atNtpSysReference,
       "atNtpSysFrequency": atNtpSysFrequency,
       "atNtpSysPrecision": atNtpSysPrecision,
       "atNtpSysRefTime": atNtpSysRefTime,
       "atNtpSysClkOffset": atNtpSysClkOffset,
       "atNtpSysRootDelay": atNtpSysRootDelay,
       "atNtpSysRootDisp": atNtpSysRootDisp}
)
